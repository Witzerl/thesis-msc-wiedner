"""Step-size ladder: evaluate one TRAINED checkpoint with fixed integration steps h = 1 ... 1/32 year.

Supervisor review 2 (2026-10-17, worklist item SV-5.12): "Say t = 1 is 1 year; test different time
steps h = 1, 1/2, 1/4, 1/8, 1/16, 1/32." This is the post-hoc version: no training, the trained
weights are re-evaluated under GraphPDE/baselines/odeint.py:GAIntegrator with step_days = h and run
through the UNMODIFIED GraphPDE/train.py:test_rollout_losses (as solver_swap.py in the code repo
does). It extends the solver-swap test of thesis section 5.5.1 (Table 5.4).

How the step is applied (GAIntegrator, step_days > 0): each rollout step goes from one visit to the
next; that interval Delta t is split into n = ceil(Delta t in days / h) EQUAL substeps, so the step
actually taken is Delta t / n <= h. With h = 365 or 182.5 days most intervals (the modal one is
~180 days) get a single step, i.e. the same as the trained one-step setting; the script records, per
configuration, how many intervals get more than one substep. No visit is skipped to force a true
one-year step (that is a different set-up).

Autonomous flag: False = the network receives the substep length as its Delta t input (the canonical
step-conditioned model); True = that input is zeroed (the networks trained inside the RK4 wrapper).
It must match training; the default is read from the checkpoint's args.

Model construction reuses build_model() of rollouts_regen.py (a mirror of train.py:main() for the
single-branch arms); a run trained inside GAIntegrator comes back wrapped, and the wrapper is peeled
off before re-wrapping it with the ladder's integrator.

Usage (from images/scripts/, conda env MPPDE):
  python step_ladder.py --arm ANISOGNN_final_dilmean --fold 2 --device cuda \
      --configs euler:n1,euler:n4,euler:d365,euler:d182.5,... --tag main
Config syntax: <scheme>:n<k> (k equal substeps per interval) or <scheme>:d<days> (fixed step h);
"ladder:<scheme>" expands to the six steps 365 / 182.5 / 91.25 / 45.625 / 22.8125 / 11.40625 d.
Output: images/data/step_ladder/<arm>_f<fold>[_<tag>].json (git-ignored cache).
  python step_ladder.py --summary     prints one markdown table per cached JSON.
The code repository is read-only: nothing here writes into it.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from types import SimpleNamespace

import numpy as np
import torch
from torch import nn

from _common import CACHE, PRECOMP, thesis_numbers
import rollouts_regen as R          # sets sys.path to the code repo; build_model lives there

import train as T  # noqa: E402  (code repo, imported, never modified)
from utils.utils import _2Dataset_preloaded  # noqa: E402
from moving_mesh_helper import PDE2DMetaMovingMesh  # noqa: E402
from baselines.odeint import GAIntegrator, DAYS_PER_YEAR  # noqa: E402

OUT = CACHE / "step_ladder"
LADDER_DAYS = [365.0 / 2 ** k for k in range(6)]   # 365, 182.5, ..., 11.40625


class StepCounter(nn.Module):
    """Pass-through around the evaluated module; records each call's interval (days) and the
    number of substeps the integrator takes for it (test_rollout_losses passes one graph per call)."""

    def __init__(self, inner):
        super().__init__()
        self.inner = inner
        self.calls = []

    def forward(self, data):
        dt = data.dt.reshape(-1)
        if isinstance(self.inner, GAIntegrator):
            n = self.inner.substeps_per_graph(dt).tolist()
        else:
            n = [1] * int(dt.numel())
        days = (dt.detach().double().cpu() * DAYS_PER_YEAR).tolist()
        self.calls.extend(zip(days, n))
        return self.inner(data)


def load(run_dir, fold, device):
    ck = torch.load(os.path.join(run_dir, "last.pt"), map_location="cpu", weights_only=False)
    a = SimpleNamespace(**ck["args"])
    a.input, a.device = str(PRECOMP[fold]), str(device)
    d = str(PRECOMP[fold])
    ds = _2Dataset_preloaded(pack_dir=os.path.join(d, "val"),
                             edges_pt=os.path.join(d, "edges_global.pt"),
                             meta_pt=os.path.join(d, "meta_global.pt"),
                             map_location="cpu", neighbors=int(a.neighbors))
    loader = SimpleNamespace(dataset=ds)
    b = ds.pde
    pde = PDE2DMetaMovingMesh(Lx=b.Lx, Ly=b.Ly, grid_size=b.grid_size, var_scales=b.var_scales,
                              in_channels=b.in_channels, time_encoding=b.time_encoding,
                              movingmesh_grid_size=None, ori_grid_size=None)
    a.K = ds.K
    model = R.build_model(a, pde, ds, torch.device("cpu"))
    model.load_state_dict(ck["model"], strict=True)          # keys match the trained structure
    inner = model.inner if isinstance(model, GAIntegrator) else model
    inner = inner.to(device).eval()
    C, K = ds.C, ds.K
    thr = T._mask_threshold_in_normalised_space(getattr(ds, "norm_params", {}),
                                                channel_index=0, physical_threshold=0.5)
    crit = T.make_criterion(
        reduction="mean", channel_weights=[float(a.mask_channel_weight)] + [1.0] * (C - 1),
        K=K, mask_soft_dice_weight=float(getattr(a, "mask_soft_dice_weight", 0.0)),
        mask_thr_norm=thr, monotonic_mask_weight=float(getattr(a, "monotonic_mask_weight", 0.0)),
        exclude_pad_nodes=False, pad_z=None)
    if float(getattr(a, "mask_soft_dice_weight", 0.0)) > 0:
        crit.mask_dice_sharpness = float(a.mask_dice_sharpness)
    return ck, a, pde, inner, crit, loader


def expand(configs):
    out = []
    for c in configs.split(","):
        c = c.strip()
        if not c:
            continue
        if c.startswith("ladder:"):
            out += [f"{c.split(':')[1]}:d{h:g}" for h in LADDER_DAYS]
        else:
            out.append(c)
    return out


def wrap(inner, spec, autonomous):
    scheme, s = spec.split(":")
    if s.startswith("d"):
        return GAIntegrator(inner, scheme=scheme, substeps=1, step_days=float(s[1:]),
                            autonomous=autonomous, checkpoint=False)
    return GAIntegrator(inner, scheme=scheme, substeps=int(s[1:]), step_days=0.0,
                        autonomous=autonomous, checkpoint=False)


TRAINED_REF = {"ANISOGNN_final_dilmean": "euler:n1", "ANISOGNN_final_oderk4n1": "rk4:n1",
               "FEN_final_w96ftp7rk4d45skew": "rk4:d45"}


def summary():
    """Print one markdown table per cached JSON (network x fold): the trained setting first,
    then each scheme's ladder, with the difference to the trained setting."""
    for fn in sorted(OUT.glob("*.json")):
        d = json.load(open(fn))
        info, rows = d["info"], d["rows"]
        ref_cfg = TRAINED_REF.get(info["arm"])
        ref = next((r for r in rows if r["config"] == ref_cfg), None)
        print(f"\n#### {info['arm']}, fold {info['fold']} (epoch {info['epoch']}, "
              f"autonomous={info['eval_autonomous']}, trained {ref_cfg}; logged change-region "
              f"Dice {info['chg_dice_logged_epoch']:.6f})\n")
        print("| setting | h nominal (d) | median substeps | intervals > 1 substep | median step (d) "
              "| change-region Dice@360d | diff. to trained | n eyes | s |")
        print("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        order = sorted(rows, key=lambda r: (r["config"] != ref_cfg, r["scheme"],
                                            r["step_days"] is not None,
                                            -(r["step_days"] or 0)))
        for r in order:
            dv = r["chg_dice"]
            diff = (dv - ref["chg_dice"]) if (ref and dv == dv) else float("nan")
            h = f"{r['step_days']:g}" if r["step_days"] is not None else f"n={r['substeps']}"
            print(f"| {r['config']} | {h} | {r['substeps_median']:g} | {r['n_multi']}/{r['n_intervals']} "
                  f"| {r['h_actual_median_days']:.1f} | {dv:.4f} | {diff:+.4f} | {r['n_eyes']} "
                  f"| {r['seconds']:.0f} |")


def main():
    if "--summary" in sys.argv:
        return summary()
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", required=True)
    ap.add_argument("--fold", type=int, required=True)
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--autonomous", default="auto",
                    help="auto = as trained (args.ode_autonomous if trained in the wrapper, "
                         "else False); or True/False")
    ap.add_argument("--configs", required=True)
    ap.add_argument("--tag", default="")
    args = ap.parse_args()
    T._make_console_utf8_safe()
    random.seed(0); np.random.seed(0); torch.manual_seed(0)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    tn = thesis_numbers()
    rd = tn.run_dir(args.arm, args.fold)
    if rd is None:
        raise SystemExit(f"no run dir for {args.arm} fold {args.fold}")
    device = torch.device(args.device)
    ck, a, pde, inner, crit, loader = load(rd, args.fold, device)
    trained_integ = str(getattr(a, "integrator", "euler"))
    trained_wrapped = (trained_integ != "euler" or int(getattr(a, "ode_substeps", 1)) != 1
                       or float(getattr(a, "ode_step_days", 0.0) or 0.0) > 0)
    if args.autonomous == "auto":
        auto = bool(getattr(a, "ode_autonomous", True)) if trained_wrapped else False
    else:
        auto = args.autonomous.strip().lower() == "true"
    logged = {m["epoch"]: m for m in tn.epochs(rd)}
    chg_log = float(logged[int(ck["epoch"])]["change_region_dice_360d"]) \
        if int(ck["epoch"]) in logged else float("nan")
    info = dict(arm=args.arm, fold=args.fold, run_dir=os.path.basename(rd), epoch=int(ck["epoch"]),
                backbone=a.backbone, trained_integrator=trained_integ,
                trained_substeps=int(getattr(a, "ode_substeps", 1)),
                trained_step_days=float(getattr(a, "ode_step_days", 0.0) or 0.0),
                trained_autonomous=bool(getattr(a, "ode_autonomous", True)) if trained_wrapped else False,
                eval_autonomous=auto, fen_transport_form=getattr(a, "fen_transport_form", None),
                params=sum(p.numel() for p in inner.parameters()),
                chg_dice_logged_epoch=chg_log, device=str(device),
                val_eyes=len(loader.dataset.files))
    print(json.dumps(info), flush=True)

    OUT.mkdir(parents=True, exist_ok=True)
    fn = OUT / f"{args.arm}_f{args.fold}{('_' + args.tag) if args.tag else ''}.json"
    rows = json.load(open(fn))["rows"] if fn.exists() else []
    done = {r["config"] for r in rows}
    for spec in expand(args.configs):
        if spec in done:
            print(f"[skip] {spec} already in {fn.name}")
            continue
        mod = StepCounter(wrap(inner, spec, auto)).to(device).eval()
        t0 = time.time()
        with torch.no_grad():
            m = T.test_rollout_losses(a, pde, int(ck["epoch"]), mod, None, None, None, None, crit,
                                      loader, None, device, layer_encoder=None, device_b=device)
        el = time.time() - t0
        n = np.array([c[1] for c in mod.calls])
        days = np.array([c[0] for c in mod.calls])
        h_act = days / n
        row = dict(config=spec, scheme=spec.split(":")[0],
                   step_days=float(spec.split(":")[1][1:]) if spec.split(":")[1].startswith("d") else None,
                   substeps=int(spec.split(":")[1][1:]) if spec.split(":")[1].startswith("n") else None,
                   chg_dice=m.get("change_region_dice_360d"),
                   n_eyes=m.get("n_sequences_at_360d"),
                   n_identical=m.get("n_identical_to_bootstrap"),
                   mai_0_1y=m.get("mai/bin_0_1y/dice_growth"),
                   mai_3plus=m.get("mai/bin_3plus_y/dice_growth"),
                   n_intervals=int(n.size), n_multi=int((n > 1).sum()),
                   substeps_median=float(np.median(n)), substeps_min=int(n.min()),
                   substeps_max=int(n.max()), substeps_total=int(n.sum()),
                   h_actual_median_days=float(np.median(h_act)),
                   h_actual_max_days=float(h_act.max()),
                   interval_days_median=float(np.median(days)),
                   seconds=round(el, 1))
        rows.append(row)
        json.dump(dict(info=info, rows=rows), open(fn, "w"), indent=2)
        print(f"[run] {spec:<16s} chgDice={row['chg_dice']:.6f}  n_eyes={row['n_eyes']}  "
              f"substeps median {row['substeps_median']:g} (multi {row['n_multi']}/{row['n_intervals']})"
              f"  h_med {row['h_actual_median_days']:.1f} d  ({el:.0f}s)", flush=True)
        if device.type == "cuda":
            torch.cuda.empty_cache()
    print(f"wrote {fn}")


if __name__ == "__main__":
    main()
