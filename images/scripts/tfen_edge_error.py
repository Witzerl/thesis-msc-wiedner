"""Per-pixel free-running layer error of the T-FEN, Galerkin vs energy-conserving form (draft for a
possible figure on where the Galerkin instability starts; author 2026-10-21).

For each form and fold: rebuild the epoch-29 checkpoint exactly as rollouts_regen.py does and run the
UNMODIFIED evaluation (train.test_rollout_losses) eye by eye. A recorder stores, for every rollout
step, the root mean squared error over the ten layer channels (normalised units) per en-face node,
the anatomy mask (non-pad nodes) and the cumulative time. Self-check: the change-region Dice that
test_rollout_losses returns over the eyes is compared with the logged epoch-29 value (as in
rollouts_regen.py, here only as a printout, since the eyes are run one at a time).

Output: images/data/tfen_edge/<EXP>_f<F>.npz (git-ignored): err (steps, 49, 1024) float16 per eye,
valid, cum_days. Usage (from images/scripts/):
    python tfen_edge_error.py --arms FEN_final_w96ftp7rk4d45 FEN_final_w96ftp7rk4d45skew --folds 0
The code repository is read-only: nothing here writes into it.
"""
from __future__ import annotations

import argparse
import os

for _v in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np
import torch
import torch.nn as nn
from types import SimpleNamespace

import rollouts_regen as RR
from rollouts_regen import T, NROWS, NCOLS, load, eye_view
from _common import CACHE, thesis_numbers

OUT = CACHE / "tfen_edge"


class ErrRecorder(nn.Module):
    """Pass-through: per call, RMS error over the layer channels per node, valid mask, dt."""

    def __init__(self, inner, C, K, pad_z):
        super().__init__()
        self.inner, self.C, self.K, self.pad_z = inner, C, K, pad_z
        self.calls = []

    def forward(self, data):
        out = self.inner(data)
        y = data.y.detach().float().cpu()
        o = out.detach().float().cpu()
        v = T._valid_node_mask(y, self.C, self.K, self.pad_z)
        err = torch.sqrt(((o[:, 1:self.C] - y[:, 1:self.C]) ** 2).mean(1))   # K = 1: channels 1-10 = layers
        self.calls.append(dict(err=err.numpy().astype(np.float16),
                               valid=(v.numpy() if v is not None else np.ones(y.shape[0], bool)),
                               dt=float(data.dt.view(-1)[0].item())))
        return out


def run(arm, fold, device):
    tn = thesis_numbers()
    rd = tn.run_dir(arm, fold)
    ck, a, pde, model, crit, ds, thr, eye_ids = load(rd, fold, device)
    assert int(ck.get("epoch", -1)) == 29
    C, K = ds.C, ds.K
    pad_z = T._pad_zvector(getattr(ds, "norm_params", None), C, torch.device("cpu"), torch.float32)
    logged = {m["epoch"]: m for m in tn.epochs(rd)}[29]["change_region_dice_360d"]
    errs, valids, cums, chg = [], [], [], []
    for i in range(len(ds.files)):
        if 0 not in ds.t0_lookup[i]:
            continue
        rec = ErrRecorder(model, C, K, pad_z).to(device).eval()
        with torch.no_grad():
            m = T.test_rollout_losses(a, pde, 29, rec, None, None, None, None, crit,
                                      SimpleNamespace(dataset=eye_view(ds, i)), None, device,
                                      layer_encoder=None, device_b=device)
        errs.append(np.stack([c["err"].reshape(NROWS, NCOLS) for c in rec.calls]))
        valids.append(np.stack([c["valid"].reshape(NROWS, NCOLS) for c in rec.calls]))
        cums.append(np.cumsum([c["dt"] for c in rec.calls]) * 365.0)
        if m["n_sequences_at_360d"]:
            chg.append(float(m["change_region_dice_360d"]))
        print(f"  eye {i:2d}: {len(rec.calls)} steps, largest error {float(errs[-1].max()):.3g}", flush=True)
    print(f"[{arm} f{fold}] logged e29 change-region Dice {logged:.4f}; mean over single-eye runs "
          f"{np.mean(chg):.4f} (not the same estimator: pooled vs per-eye mean)")
    OUT.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(OUT / f"{arm}_f{fold}.npz",
                        **{f"err_{k}": e for k, e in enumerate(errs)},
                        **{f"valid_{k}": v for k, v in enumerate(valids)},
                        **{f"cum_{k}": c for k, c in enumerate(cums)},
                        n=np.array(len(errs)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arms", nargs="+", required=True)
    ap.add_argument("--folds", nargs="+", type=int, default=[0])
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = ap.parse_args()
    torch.set_num_threads(4)
    for arm in args.arms:
        for f in args.folds:
            run(arm, f, torch.device(args.device))


if __name__ == "__main__":
    main()
