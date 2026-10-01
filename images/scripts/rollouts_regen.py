"""Regenerate validation rollouts from trained checkpoints and cache the binarised masks.

For each arm and fold: load <run_dir>/last.pt (epoch-29 weights), rebuild the model from the
checkpoint's OWN saved args exactly as GraphPDE/train.py:main() builds it (backbone dispatch,
anisognn stencil wrapper, Runge-Kutta integrator wrapper), and run the UNMODIFIED evaluation
GraphPDE/train.py:test_rollout_losses over every validation eye along its real visit schedule.
The model is wrapped in a thin recorder that copies every prediction the evaluation makes, so
the masks cached here are the very tensors the metric was computed from.

Self-check (mandatory before any figure uses a cache): the cohort change-region Dice at the
one-year anchor is (a) returned by test_rollout_losses itself and (b) recomputed here from the
cached binarised masks with the same rule; both are compared with the epoch-29 value logged in
that run's metrics.jsonl.

Output: images/data/rollouts/<EXP>_f<F>.npz (np.packbits, compressed),
images/data/rollouts/selfcheck.json, and per-eye partial results in
images/data/rollouts/_partial/<EXP>/ (a rerun resumes from them).

Usage (from images/scripts/), one fold per process (each fold's dataset is held in memory):
  python rollouts_regen.py --arms ANISOGNN_final_dilmean UNET_final_w5 ... --folds 2
Runs on the CPU by default (all caches of 2026-10-01 were made on the CPU and reproduce the
GPU-logged values). When it was written, the host's commit memory was nearly exhausted by an
unrelated process, so the evaluation goes eye by eye with retries on allocation failures and
the BLAS thread pools are capped; neither changes a number.
The code repository is read-only: nothing here writes into it.
"""
from __future__ import annotations

import os
# The host is short of commit memory (see the report): OpenBLAS / MKL reserve a buffer per
# thread at import (~1.5 GB here), so cap their pools before numpy / scipy load. Torch's own
# intra-op pool is set in main().
for _v in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse
import copy
import gc
import json
import math
import random
import sys
import time
from types import SimpleNamespace

import numpy as np
import torch
from torch import nn

from _common import CODE, CACHE, PRECOMP, NROWS, NCOLS, thesis_numbers

GP = CODE / "GraphPDE"
for p in (str(GP), str(CODE)):
    if p not in sys.path:
        sys.path.insert(0, p)

import train as T  # noqa: E402  (imported, never modified)
from utils.utils import _2Dataset_preloaded  # noqa: E402
from moving_mesh_helper import PDE2DMetaMovingMesh  # noqa: E402
from gnn import MP_PDE_Solver_2D  # noqa: E402

OUT = CACHE / "rollouts"
DEFAULT_ARMS = ["ANISOGNN_final_dilmean", "UNET_final_w5", "FEN_final_w96ftp7rk4d45skew",
                "FNO_final_w5", "MPPDE_final_aggrmean", "MPPDE_final_pxmean"]


# --------------------------------------------------------------------------------------------
# Model construction: a line-by-line mirror of train.py:main() section "3. Models" for the
# single-branch, d_embed = 0 case (every arm used here). main() is not factored into a builder,
# so the dispatch is reproduced; every constructor argument is read from the checkpoint args.
# --------------------------------------------------------------------------------------------
def build_model(a, pde, ds, device):
    K, C = ds.K, ds.C
    n_cov = int(getattr(ds, "n_covariates", 0))
    assert not a.moving_mesh, "single-branch arms only"
    assert int(getattr(a, "d_embed", 0)) == 0, "LayerEncoder arms are not handled"
    bb = getattr(a, "backbone", "gnn")
    if bb == "unet":
        from baselines.unet import GAUNet
        model = GAUNet(pde=pde, time_window=K, in_channels=C, n_covariates=n_cov,
                       base_width=a.hidden_dim,
                       euler_dt_scale=bool(getattr(a, "euler_dt_scale", True)))
    elif bb == "fen":
        from baselines.fen import GAFEN
        model = GAFEN(pde=pde, time_window=K, in_channels=C, n_covariates=n_cov,
                      width=a.hidden_dim, depth=int(getattr(a, "fen_depth", 4)),
                      transport=bool(getattr(a, "fen_transport", True)),
                      pitch=int(getattr(a, "fen_pitch", 1)),
                      transport_pitch=int(getattr(a, "fen_transport_pitch", 0) or 0),
                      cell_centre=bool(getattr(a, "fen_cell_centre", False)),
                      vel_gain_mm_per_yr=float(getattr(a, "fen_vel_gain", 0.2)),
                      euler_dt_scale=bool(getattr(a, "euler_dt_scale", True)),
                      transport_form=str(getattr(a, "fen_transport_form", "galerkin")))
    elif bb == "gunet":
        from baselines.gunet import GAGraphUNet
        model = GAGraphUNet(pde=pde, time_window=K, in_channels=C, n_covariates=n_cov,
                            base_width=a.hidden_dim,
                            euler_dt_scale=bool(getattr(a, "euler_dt_scale", True)))
    elif bb == "fno":
        from baselines.fno import GAFNO
        model = GAFNO(pde=pde, time_window=K, in_channels=C, n_covariates=n_cov,
                      width=a.hidden_dim,
                      euler_dt_scale=bool(getattr(a, "euler_dt_scale", True)),
                      modes=tuple(getattr(a, "fno_modes", None) or (14, 14)),
                      local_kernel=int(getattr(a, "fno_local_kernel", 1) or 1))
    else:
        model = MP_PDE_Solver_2D(
            pde=pde, time_window=K, hidden_features=a.hidden_dim,
            hidden_layer=a.hidden_layers, eq_variables={}, in_channels=C,
            n_covariates=n_cov, n_cond_embed=0,
            gnn_aggr=getattr(a, "gnn_aggr", "mean_max"),
            norm_type=getattr(a, "norm_type", "layer"),
            euler_dt_scale=bool(getattr(a, "euler_dt_scale", True)),
            edge_feat_index=bool(getattr(a, "edge_feat_index", False)),
            norm_mlp_sites=bool(getattr(a, "norm_mlp_sites", False)),
            edge_feat_none=bool(getattr(a, "edge_feat_none", False)))
        if bb == "anisognn":
            from baselines.anisognn import GAAnisoGNN
            model = GAAnisoGNN(model, pde=pde,
                               stencil=getattr(a, "aniso_stencil", "dilated"),
                               pitch=int(getattr(a, "aniso_pitch", 7)),
                               taps=int(getattr(a, "aniso_taps", 3)),
                               rows=int(getattr(a, "aniso_rows", 1)))
    integ = str(getattr(a, "integrator", "euler"))
    nsub = int(getattr(a, "ode_substeps", 1))
    sdays = float(getattr(a, "ode_step_days", 0.0) or 0.0)
    if integ != "euler" or nsub != 1 or sdays > 0:
        from baselines.odeint import GAIntegrator
        model = GAIntegrator(model, scheme=integ, substeps=nsub, step_days=sdays,
                             autonomous=bool(getattr(a, "ode_autonomous", True)),
                             checkpoint=bool(getattr(a, "ode_checkpoint", True)))
    return model.to(device)


class Recorder(nn.Module):
    """Pass-through around the model: test_rollout_losses calls it once per rollout step (in
    order, eye by eye); every call's binarised prediction, target, input baseline and anatomy
    (non-pad) mask are copied to CPU as bool arrays (kept small: the host is short of memory)."""

    def __init__(self, inner, thr, C, K, pad_z):
        super().__init__()
        self.inner = inner
        self.thr, self.C, self.K, self.pad_z = float(thr), C, K, pad_z
        self.calls = []

    def forward(self, data):
        out = self.inner(data)
        y = data.y.detach().float().cpu()
        v = T._valid_node_mask(y, self.C, self.K, self.pad_z)
        self.calls.append(dict(
            pred=(out[:, 0].detach().float().cpu() > self.thr).numpy(),  # K = 1: col 0 = mask
            gt=(y[:, 0] > self.thr).numpy(),
            x0=(data.x[:, 0].detach().float().cpu() > self.thr).numpy(),
            valid=(v.numpy() if v is not None else np.ones(y.shape[0], bool)),
            dt=float(data.dt.view(-1)[0].item()),
        ))
        return out


_DS = {}


def dataset(fold, neighbors=12):
    """Validation dataset of a fold plus its eye ids, loaded once (main() loads it before the
    first CUDA call, which on this host left too little commit memory for the legacy-format
    torch.load of the precompute files)."""
    key = (fold, int(neighbors))
    if key not in _DS:
        d = str(PRECOMP[fold])
        ds = _2Dataset_preloaded(pack_dir=os.path.join(d, "val"),
                                 edges_pt=os.path.join(d, "edges_global.pt"),
                                 meta_pt=os.path.join(d, "meta_global.pt"),
                                 map_location="cpu", neighbors=int(neighbors))
        ids = []
        for f in ds.files:
            lst = torch.load(f, map_location="cpu", weights_only=False)
            ids.append(str(lst[0].get("eye_id", os.path.basename(f))))
        _DS[key] = (ds, ids)
    return _DS[key]


def load(run_dir, fold, device):
    ck = torch.load(os.path.join(run_dir, "last.pt"), map_location="cpu", weights_only=False)
    a = SimpleNamespace(**ck["args"])
    a.input, a.device = str(PRECOMP[fold]), str(device)
    val_ds, eye_ids = dataset(fold, a.neighbors)
    b = val_ds.pde
    pde = PDE2DMetaMovingMesh(Lx=b.Lx, Ly=b.Ly, grid_size=b.grid_size, var_scales=b.var_scales,
                              in_channels=b.in_channels, time_encoding=b.time_encoding,
                              movingmesh_grid_size=None, ori_grid_size=None)
    a.K = val_ds.K
    model = build_model(a, pde, val_ds, device)
    model.load_state_dict(ck["model"], strict=True)
    model.eval()
    C, K = val_ds.C, val_ds.K
    thr = T._mask_threshold_in_normalised_space(getattr(val_ds, "norm_params", {}),
                                                channel_index=0, physical_threshold=0.5)
    crit = T.make_criterion(
        reduction="mean", channel_weights=[float(a.mask_channel_weight)] + [1.0] * (C - 1),
        K=K, mask_soft_dice_weight=float(getattr(a, "mask_soft_dice_weight", 0.0)),
        mask_thr_norm=thr, monotonic_mask_weight=float(getattr(a, "monotonic_mask_weight", 0.0)),
        exclude_pad_nodes=False, pad_z=None)
    if float(getattr(a, "mask_soft_dice_weight", 0.0)) > 0:
        crit.mask_dice_sharpness = float(a.mask_dice_sharpness)
    return ck, a, pde, model, crit, val_ds, thr, eye_ids


def change_dice_from_cache(eyes):
    """Cohort change-region Dice at the one-year anchor, re-derived from the cached masks with
    the rule of test_rollout_losses: first step whose cumulative dt >= 0.95 y, symmetric
    difference against the baseline, eyes with no change on either side skipped."""
    vals = []
    for e in eyes:
        cum = np.cumsum(e["dt"])
        hit = np.nonzero(cum >= 1.0 - 0.05)[0]
        if len(hit) == 0:
            continue
        s = int(hit[0])
        p, t, b = e["pred"][s], e["gt"][s], e["base"]
        if p.sum() + t.sum() == 0:
            continue
        pc, tc = p != b, t != b
        if pc.sum() + tc.sum() > 0:
            vals.append(2.0 * (pc & tc).sum() / (pc.sum() + tc.sum()))
    return float(np.mean(vals)) if vals else float("nan"), len(vals)


def eye_view(ds, i):
    """A shallow copy of the dataset that holds only sequence i (the evaluation is then run
    eye by eye, so a transient allocation failure costs one eye, not the whole fold)."""
    v = copy.copy(ds)
    for k in ("files", "X", "Y", "t0s", "dts", "covariates", "t0_lookup"):
        setattr(v, k, [getattr(ds, k)[i]])
    return v


def eval_eye(a, pde, model, crit, ds, i, thr, device, tries=6):
    """Run the unmodified test_rollout_losses on eye i alone and return what it recorded."""
    C, K = ds.C, ds.K
    pad_z = T._pad_zvector(getattr(ds, "norm_params", None), C, torch.device("cpu"), torch.float32)
    for attempt in range(tries):
        rec = Recorder(model, thr, C, K, pad_z).to(device).eval()
        try:
            with torch.no_grad():
                m = T.test_rollout_losses(a, pde, 29, rec, None, None, None, None, crit,
                                          SimpleNamespace(dataset=eye_view(ds, i)), None, device,
                                          layer_encoder=None, device_b=device)
            break
        except RuntimeError as err:          # "bad allocation" when the host runs out of commit
            print(f"    eye {i}: {str(err)[:60]!r}, retry {attempt + 1}/{tries}", flush=True)
            del rec
            gc.collect()
            time.sleep(10)
    else:
        raise RuntimeError(f"eye {i} failed {tries} times")
    steps = m["mai_per_step_records"]
    assert len(steps) == len(rec.calls), (len(steps), len(rec.calls))
    c0 = rec.calls[0]
    e = dict(base=c0["x0"].reshape(NROWS, NCOLS),
             pred=np.stack([c["pred"].reshape(NROWS, NCOLS) for c in rec.calls]),
             gt=np.stack([c["gt"].reshape(NROWS, NCOLS) for c in rec.calls]),
             valid=np.stack([c["valid"].reshape(NROWS, NCOLS) for c in rec.calls]),
             dt=np.asarray([c["dt"] for c in rec.calls], float),
             dice_growth=np.asarray([s["dice_growth"] for s in steps], float),
             chg=float(m["change_region_dice_360d"]),
             n_ident=int(m["n_identical_to_bootstrap"]), n_at=int(m["n_sequences_at_360d"]))
    for j, s in enumerate(steps):
        assert s["step_idx"] == j and abs(float(np.sum(e["dt"][:j + 1])) - s["cum_dt_years"]) < 1e-5
    return e


def run_one(arm, fold, device):
    tn = thesis_numbers()
    rd = tn.run_dir(arm, fold)
    if rd is None:
        raise SystemExit(f"no run dir for {arm} fold {fold}")
    exp = f"{arm}_f{fold}"
    ep = tn.epochs(rd)
    logged = {m["epoch"]: m for m in ep}
    ck, a, pde, model, crit, ds, thr, eye_ids = load(rd, fold, device)
    assert int(ck.get("epoch", -1)) == 29, f"last.pt epoch {ck.get('epoch')}"
    nparam = sum(p.numel() for p in model.parameters())
    print(f"[{exp}] run {os.path.basename(rd)}")
    print(f"[{exp}] backbone={a.backbone} integrator={getattr(a, 'integrator', 'euler')} "
          f"step_days={getattr(a, 'ode_step_days', 0)} autonomous={getattr(a, 'ode_autonomous', None)} "
          f"params={nparam:,} epoch={ck.get('epoch')} val_eyes={len(ds.files)} thr_norm={thr:.4f}",
          flush=True)

    # eye by eye, each persisted at once so a hard crash resumes where it stopped
    part = OUT / "_partial" / exp
    part.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    eyes = []
    for i in range(len(ds.files)):
        if 0 not in ds.t0_lookup[i]:
            continue
        fp = part / f"eye_{i:02d}.npz"
        if fp.exists() and str(np.load(fp)["run_dir"]) == os.path.basename(rd):
            z = np.load(fp)
            e = {k: z[k] for k in ("base", "pred", "gt", "valid", "dt", "dice_growth")}
            e.update(chg=float(z["chg"]), n_ident=int(z["n_ident"]), n_at=int(z["n_at"]))
        else:
            e = eval_eye(a, pde, model, crit, ds, i, thr, device)
            np.savez_compressed(fp, run_dir=np.array(os.path.basename(rd)), **e)
        e.update(eye_idx=i, eye_id=eye_ids[i])
        print(f"    eye {i:2d} {e['eye_id']:<14s} steps {len(e['dt']):2d}  chg {e['chg']:.4f}",
              flush=True)
        eyes.append(e)
    el = time.time() - t0
    vals = [e["chg"] for e in eyes if e["chg"] == e["chg"]]
    m = {"change_region_dice_360d": float(np.mean(vals)),
         "n_identical_to_bootstrap": sum(e["n_ident"] for e in eyes),
         "n_sequences_at_360d": sum(e["n_at"] for e in eyes)}

    chg_eval = float(m["change_region_dice_360d"])
    chg_cache, n_cache = change_dice_from_cache(eyes)
    chg_log = float(logged[29]["change_region_dice_360d"])
    n_ident = int(m["n_identical_to_bootstrap"])
    persist_equal = all(np.array_equal(e["pred"][i], e["base"]) for e in eyes
                        for i in range(len(e["pred"])))
    print(f"[{exp}] change-region Dice@360d: logged e29 {chg_log:.6f} | evaluation {chg_eval:.6f} "
          f"| recomputed from cache {chg_cache:.6f} (n={n_cache}) | diff {chg_eval - chg_log:+.2e} "
          f"| identical-to-baseline {n_ident}/{m['n_sequences_at_360d']} | all steps == baseline: "
          f"{persist_equal} | {el:.0f}s")

    # write the cache: per-eye arrays concatenated over steps, bit-packed
    OUT.mkdir(parents=True, exist_ok=True)
    off = np.cumsum([0] + [len(e["dt"]) for e in eyes])
    pk = lambda arrs: np.packbits(np.concatenate(arrs).reshape(-1, NROWS * NCOLS), axis=1)
    np.savez_compressed(
        OUT / f"{exp}.npz",
        eye_idx=np.array([e["eye_idx"] for e in eyes], np.int32),
        eye_id=np.array([e["eye_id"] for e in eyes]),
        offsets=off.astype(np.int32),
        dt_years=np.concatenate([e["dt"] for e in eyes]),
        cum_days=np.concatenate([np.cumsum(e["dt"]) * 365.0 for e in eyes]),
        pred=pk([e["pred"] for e in eyes]),
        gt=pk([e["gt"] for e in eyes]),
        valid=pk([e["valid"] for e in eyes]),
        base=pk([e["base"][None] for e in eyes]),
        dice_growth=np.concatenate([e["dice_growth"] for e in eyes]),
        shape=np.array([NROWS, NCOLS], np.int32),
        run_dir=np.array(os.path.basename(rd)),
        epoch=np.int32(ck["epoch"]),
        chg_dice_logged=chg_log, chg_dice_eval=chg_eval, chg_dice_cache=chg_cache,
    )
    print(f"[{exp}] wrote {OUT / (exp + '.npz')}")
    return dict(exp=exp, run_dir=os.path.basename(rd), backbone=a.backbone, params=nparam,
                epoch=int(ck["epoch"]), n_eyes=len(eyes), n_at_anchor=int(m["n_sequences_at_360d"]),
                chg_logged=chg_log, chg_eval=chg_eval, chg_cache=chg_cache,
                diff=chg_eval - chg_log, n_identical=n_ident, all_steps_equal_baseline=persist_equal,
                seconds=round(el, 1))


from rollouts_panels import load_cache  # noqa: E402,F401  (reader lives with the figures)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arms", nargs="+", default=DEFAULT_ARMS)
    ap.add_argument("--folds", nargs="+", type=int, default=[2])
    ap.add_argument("--device", default="cpu")   # see the memory note in the report
    ap.add_argument("--threads", type=int, default=4)
    args = ap.parse_args()
    T._make_console_utf8_safe()
    torch.set_num_threads(args.threads)
    for f in args.folds:              # before any CUDA call (see dataset())
        dataset(f, 12)
    random.seed(0); np.random.seed(0); torch.manual_seed(0)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    device = torch.device(args.device)
    OUT.mkdir(parents=True, exist_ok=True)
    sc_path = OUT / "selfcheck.json"
    sc = json.load(open(sc_path)) if sc_path.exists() else {}
    for f in args.folds:
        for arm in args.arms:
            r = run_one(arm, f, device)
            sc[r["exp"]] = r
            json.dump(sc, open(sc_path, "w"), indent=2)
            torch.cuda.empty_cache()
    print("\nexp                                   logged_e29   evaluation   from_cache   diff")
    for k, r in sc.items():
        print(f"{k:<38s} {r['chg_logged']:.6f}   {r['chg_eval']:.6f}   {r['chg_cache']:.6f}   "
              f"{r['diff']:+.1e}")


if __name__ == "__main__":
    main()
