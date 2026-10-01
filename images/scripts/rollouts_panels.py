"""Shared drawing code for the rollout figures (fig_experiments_rollout, fig_appendix_rollouts).

Masks come from the caches written by rollouts_regen.py (binarised at the physical 0.5
threshold exactly as train.py binarises them). Every panel is drawn at the physical aspect
ratio of the 49 x 1024 window (5.94 mm tall, 5.82 mm wide).

Encoding of a model panel (change is the symmetric difference against the baseline mask, the
definition behind change-region Dice):
  predicted and true change       -> MASK['tp']   (blue)
  predicted change only           -> MASK['fp']   (orange)
  true change only (missed)       -> MASK['fn']   (purple)
  predicted lesion, unchanged     -> PAL['line']  (light neutral)
  baseline lesion                 -> MASK['baseline'] outline on every panel
A ground-truth panel fills the true lesion with MASK['gt'].
"""
from __future__ import annotations

import numpy as np
from matplotlib.colors import to_rgb
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

from _common import NROWS, NCOLS, DY_MM, DX_MM, EXTENT, CACHE

ANCHOR_YEARS = 1.0 - 0.05          # train.py: first rollout step with cumulative dt >= 0.95 y
XC = (np.arange(NCOLS) + 0.5) * DX_MM
YC = (np.arange(NROWS) + 0.5) * DY_MM

# category codes
BG, UNCH, TP, FP, FN, GT = 0, 1, 2, 3, 4, 5


def colours(pal):
    return {BG: to_rgb(pal.MASK["tn"]), UNCH: to_rgb(pal.PAL["line"]),
            TP: to_rgb(pal.MASK["tp"]), FP: to_rgb(pal.MASK["fp"]),
            FN: to_rgb(pal.MASK["fn"]), GT: to_rgb(pal.MASK["gt"])}


def model_codes(pred, gt, base):
    """Per-pixel category of a model panel."""
    pc, tc = pred != base, gt != base
    c = np.full(pred.shape, BG, np.uint8)
    c[pred & ~pc] = UNCH
    c[pc & tc] = TP
    c[pc & ~tc] = FP
    c[~pc & tc] = FN
    return c


def gt_codes(gt):
    return np.where(gt, GT, BG).astype(np.uint8)


def anchor_step(cum_days):
    """Index of the one-year anchor step (None when the eye never reaches it)."""
    hit = np.nonzero(np.asarray(cum_days) >= ANCHOR_YEARS * 365.0 - 1e-6)[0]
    return int(hit[0]) if len(hit) else None


def draw_panel(ax, codes, base, pal, pad=None, outline_lw=0.6):
    """Draw one en-face panel: categorical fill, zero-padding hatch, baseline outline."""
    cmap = colours(pal)
    rgb = np.zeros(codes.shape + (3,))
    for k, v in cmap.items():
        rgb[codes == k] = v
    ax.imshow(rgb, extent=EXTENT, aspect="equal", interpolation="nearest")
    if pad is not None and pad.any():
        # nodes without data at this visit (all channels zero: crop padding or no layer data): hatched, no fill
        ax.contourf(XC, YC, pad.astype(float), levels=[0.5, 1.5], colors="none",
                    hatches=["//////"], extend="neither")
    if base.any():
        ax.contour(XC, YC, base.astype(float), levels=[0.5], colors=[pal.MASK["baseline"]],
                   linewidths=outline_lw)
    ax.set_xlim(EXTENT[0], EXTENT[1])
    ax.set_ylim(EXTENT[2], EXTENT[3])
    ax.set_xticks([]); ax.set_yticks([])
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(True)
        s.set_color(pal.PAL["line"])
        s.set_linewidth(0.5)


def scale_bar(ax, pal, mm=1.0, label="1 mm", corner="lower left"):
    """Horizontal scale bar inside a panel corner (axes in mm)."""
    if corner == "lower left":
        x0 = EXTENT[0] + 0.25
    else:
        x0 = EXTENT[1] - 0.25 - mm
    x1 = x0 + mm
    y = EXTENT[2] - 0.30
    ax.plot([x0, x1], [y, y], color=pal.PAL["ink"], lw=1.0, solid_capstyle="butt")
    ax.text((x0 + x1) / 2, y - 0.10, label, ha="center", va="bottom", fontsize=6,
            color=pal.PAL["ink"])


def scale_bar_fig(fig, pal, x_right_in, y_in, panel_w_in, W, H, mm=1.0, label="1 mm"):
    """Scale bar drawn in figure coordinates outside the panels, at the panels' own mm scale
    (panel_w_in inches span the 5.816 mm window width)."""
    L = panel_w_in * mm / EXTENT[1]
    x1, x0 = x_right_in, x_right_in - L
    fig.add_artist(Line2D([x0 / W, x1 / W], [1 - y_in / H] * 2, transform=fig.transFigure,
                          color=pal.PAL["ink"], lw=1.0, solid_capstyle="butt"))
    fig.text((x0 - 0.04) / W, 1 - y_in / H, label, ha="right", va="center", fontsize=6.5,
             color=pal.PAL["ink"])


def legend_handles(pal, with_pad=False):
    """Legend entries, ordered for a 4-column legend filled column by column: first row
    lesion / unchanged / outline / padding, second row the three change codes."""
    true_l = Patch(fc=pal.MASK["gt"], ec="none", label="True lesion")
    unch = Patch(fc=pal.PAL["line"], ec="none", label="Unchanged lesion")
    outl = Line2D([], [], color=pal.MASK["baseline"], lw=1.0, label="Baseline outline")
    tp = Patch(fc=pal.MASK["tp"], ec="none", label="Change: predicted and true")
    fp = Patch(fc=pal.MASK["fp"], ec="none", label="Change: predicted only")
    fn = Patch(fc=pal.MASK["fn"], ec="none", label="Change: true only")
    h = [true_l, tp, unch, fp, outl, fn]
    if with_pad:
        h.append(Patch(fc="white", ec=pal.PAL["muted"], lw=0.4, hatch="//////",
                       label="No data at this visit"))
    return h


def baseline_pad(fold, eye_idx):
    """Zero-padded nodes of an eye's baseline visit, read from the precompute (window 0, x):
    True where every channel equals the z-value of a zero fill (train.py:_valid_node_mask)."""
    import glob
    import os
    import torch
    from _common import PRECOMP
    d = str(PRECOMP[fold])
    files = sorted(glob.glob(os.path.join(d, "val", "sample_*.pt")))
    meta = torch.load(os.path.join(d, "meta_global.pt"), map_location="cpu", weights_only=False)
    npar = meta["norm_params"]
    mean = torch.as_tensor(npar["mean"], dtype=torch.float32)
    std = torch.as_tensor(npar["std"], dtype=torch.float32)
    pad_z = (0.0 - mean) / std
    w0 = torch.load(files[eye_idx], map_location="cpu", weights_only=False)[0]
    x = w0["x"].to(torch.float32)[:, :, -1].T          # (N, C), latest time of the window
    pad = torch.isclose(x, pad_z.view(1, -1), atol=1e-4, rtol=0.0).all(dim=1)
    return pad.numpy().reshape(NROWS, NCOLS), str(w0.get("eye_id", ""))


def load_cache(exp):
    """Read a cache written by rollouts_regen.py: list of per-eye dicts (pred/gt/valid:
    (S, 49, 1024) bool, base: (49, 1024) bool) and the self-check metadata."""
    z = np.load(CACHE / "rollouts" / f"{exp}.npz")
    n = NROWS * NCOLS
    unpack = lambda a: np.unpackbits(a, axis=1, count=n).astype(bool).reshape(-1, NROWS, NCOLS)
    pred, gt, valid, base = unpack(z["pred"]), unpack(z["gt"]), unpack(z["valid"]), unpack(z["base"])
    off = z["offsets"]
    eyes = []
    for i in range(len(z["eye_idx"])):
        s = slice(off[i], off[i + 1])
        eyes.append(dict(eye_idx=int(z["eye_idx"][i]), eye_id=str(z["eye_id"][i]),
                         base=base[i], pred=pred[s], gt=gt[s], valid=valid[s],
                         dt=z["dt_years"][s], cum_days=z["cum_days"][s],
                         dice_growth=z["dice_growth"][s]))
    meta = dict(run_dir=str(z["run_dir"]), epoch=int(z["epoch"]),
                chg_logged=float(z["chg_dice_logged"]), chg_eval=float(z["chg_dice_eval"]),
                chg_cache=float(z["chg_dice_cache"]))
    return eyes, meta
