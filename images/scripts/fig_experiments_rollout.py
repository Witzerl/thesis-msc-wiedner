"""Figure fig_experiments_rollout (Chapter 5, section 5.2): what the change-region Dice scores.

One validation eye at the one-year anchor, four panels in one row, cropped to the lesion
(bounding box of baseline, truth and prediction + CROP_MM), at the physical aspect ratio:
  (a) the baseline lesion (the model's input mask);
  (b) truth at the anchor: the baseline lesion kept (light) and the true change (dark);
  (c) prediction of the canonical dilated-stencil GNN (epoch-29 weights), same encoding;
  (d) agreement: predicted and true / predicted only / missed change.
One message: an eye on which the model does well, shown so that truth and prediction can be
compared directly; most of the lesion stays as it is and the metric scores the band of change
along its border. It is a deliberately good example and the caption says so (with the median for
comparison); typical and difficult eyes are in Appendix D (fig_appendix_rollouts.py). Positions
without data are drawn as background; all explanation is in the caption. "Change" is the
symmetric difference against the baseline mask (the definition behind change-region Dice), so it
includes the rare pixels where the true lesion shrinks.

Eye-selection rule (2026-10-18): among the validation eyes of folds 0-2 (the folds with cached
rollouts) whose lesion does not touch the window edge at baseline or at the anchor (truth or
prediction), the eye with the highest change-region Dice of the epoch-29 rollout at the anchor.
This gives fold 0, eye 10 (Dice 0.761, the highest of all 48 eyes; median 0.544). An earlier
median rule (fold 2, eye 6, Dice 0.552) was rejected by the author because it does not show
growth being captured.

Display smoothing (after the poster, masterthesis-docker/poster/poster_figures.ipynb cell 10):
each binary mask is upsampled bilinearly from 49 x 1024 to a display grid at the physical aspect
ratio, blurred (MASK_SIGMA display pixels, stronger than the poster because one native row spans
~12 display pixels here) and thresholded at 0.5; every coloured region is then blurred slightly
(SIGMA display pixels) and drawn as a filled contour at 0.5. For display only: the printed pixel
counts and the Dice of the eye are computed on the native, unsmoothed masks; the script prints
how much the smoothing changes the drawn areas. Pixel-exact panels are in Appendix D.

Data: images/data/rollouts/ANISOGNN_final_dilmean_f{0,1,2}.npz, written and self-checked by
rollouts_regen.py (last.pt = epoch 29; each cache reproduces the logged epoch-29 change-region
Dice@360d).

Include at width=\textwidth.
Run from images/scripts/:  python fig_experiments_rollout.py
"""
from __future__ import annotations

import matplotlib as mpl
import numpy as np
from matplotlib.patches import Patch

from _common import setup, save
import rollouts_panels as RP
from rollouts_panels import load_cache

EXP = "ANISOGNN_final_dilmean"
FOLDS = (0, 1, 2)
PX_MM2 = 0.12118 * 0.00568
DISP_W = 600          # display grid width (columns); height follows the physical aspect ratio
SIGMA = 1.5           # region blur in display pixels (poster: 1.5 for the TP/FP/FN slivers)
MASK_SIGMA = 5.0      # blur of each upsampled mask before thresholding (display px; one native
                      # row is ~12 display px tall), removes the row staircase
FRAC = 1.0
CROP_MM = 0.35        # margin around the lesion bounding box
RP_DX, RP_DY = 0.00568, 0.12118


def upsample(mask, h, w):
    """Binary (49, 1024) mask -> binary (h, w) display mask: bilinear upsampling, a Gaussian
    blur of MASK_SIGMA display pixels, threshold 0.5."""
    import torch
    import torch.nn.functional as F
    t = torch.tensor(mask[None, None], dtype=torch.float32)
    up = F.interpolate(t, size=(h, w), mode="bilinear", align_corners=False)[0, 0].numpy()
    return blur(up, MASK_SIGMA) > 0.5


def blur(a, sigma=SIGMA):
    """Separable Gaussian blur (torch, as smooth01 in the poster notebook)."""
    import torch
    import torch.nn.functional as F
    r = int(max(1, round(3 * sigma)))
    xs = torch.arange(-r, r + 1, dtype=torch.float32)
    k = torch.exp(-(xs ** 2) / (2 * sigma ** 2)); k = k / k.sum()
    t = torch.tensor(a.astype(np.float32))[None, None]
    return F.conv2d(t, (k[:, None] * k[None, :])[None, None], padding=r)[0, 0].numpy()


def draw_smooth(ax, regions, outline, pal):
    """regions: list of (bool mask on the display grid, colour), drawn in order as smoothed
    filled contours; outline: display-grid baseline mask drawn as a smoothed contour line."""
    h, w = outline.shape
    xc = (np.arange(w) + 0.5) / w * RP.EXTENT[1]
    yc = (np.arange(h) + 0.5) / h * RP.EXTENT[2]
    for m, col in regions:
        b = blur(m)
        if b.max() >= 0.5:
            ax.contourf(xc, yc, b, levels=[0.5, 1.01], colors=[col])
    ax.contour(xc, yc, blur(outline), levels=[0.5], colors=[pal.MASK["baseline"]],
               linewidths=0.6)
    ax.set_xlim(RP.EXTENT[0], RP.EXTENT[1])
    ax.set_ylim(RP.EXTENT[2], RP.EXTENT[3])
    ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    ax.grid(False)
    for sp in ax.spines.values():
        sp.set_visible(True); sp.set_color(pal.PAL["line"]); sp.set_linewidth(0.5)


def touches_edge(*ms):
    return any(m[0].any() or m[-1].any() or m[:, 0].any() or m[:, -1].any() for m in ms)


def eye_table():
    """One row per validation eye of folds 0-2 (the folds with cached rollouts): change-region
    Dice of the epoch-29 rollout at the one-year anchor, baseline area, edge contact."""
    rows = []
    for fold in FOLDS:
        eyes, meta = load_cache(f"{EXP}_f{fold}")
        assert meta["epoch"] == 29
        assert abs(meta["chg_cache"] - meta["chg_logged"]) < 1e-3, "unverified rollout"
        for e in eyes:
            a = RP.anchor_step(e["cum_days"])
            b, g, p = e["base"], e["gt"][a], e["pred"][a]
            tc, pc = g != b, p != b
            tp, fp, fn = (tc & pc).sum(), (pc & ~tc).sum(), (tc & ~pc).sum()
            rows.append(dict(fold=fold, e=e, a=a, dice=2 * tp / (2 * tp + fp + fn),
                             area=b.sum() * PX_MM2, edge=touches_edge(b, g, p)))
    return rows


def select_eye():
    """Rule: among eyes whose lesion (baseline, truth or prediction at the anchor) does not
    touch the window edge, the one with the highest change-region Dice. A deliberately good
    example; the caption says so and gives the median for comparison."""
    rows = eye_table()
    el = [r for r in rows if not r["edge"]]
    d_all = [r["dice"] for r in rows]
    print(f"{len(rows)} eyes (folds {FOLDS}): median Dice {np.median(d_all):.3f}, "
          f"upper quartile from {np.percentile(d_all, 75):.3f}; {len(el)} without edge contact")
    pick = max(el, key=lambda r: r["dice"])
    rank = sorted(d_all, reverse=True).index(pick["dice"]) + 1
    print(f"  pick: fold {pick['fold']} eye {pick['e']['eye_idx']} ({pick['e']['eye_id']}), "
          f"Dice {pick['dice']:.3f}, rank {rank} of {len(rows)}")
    return pick


def main():
    pal = setup()
    import matplotlib.pyplot as plt
    mpl.rcParams["savefig.bbox"] = "standard"

    r = select_eye()
    e, a = r["e"], r["a"]
    base, gt, pred = e["base"], e["gt"][a], e["pred"][a]
    day = int(round(e["cum_days"][a]))

    tc, pc = gt != base, pred != base
    tp, fp, fn = (tc & pc).sum(), (pc & ~tc).sum(), (tc & ~pc).sum()
    dice = 2 * tp / (2 * tp + fp + fn)
    print(f"eye {e['eye_idx']} ({e['eye_id']}), anchor step {a} = {day} d")
    print(f"  baseline lesion {base.sum()} px, true change {tc.sum()} px "
          f"({tc.sum() / base.sum():.1%} of the baseline lesion), predicted change {pc.sum()} px")
    print(f"  predicted and true {tp}, predicted only {fp}, missed {fn}; "
          f"change-region Dice of this eye {dice:.3f}")

    # display grid at the physical aspect ratio; categories formed on the upsampled masks
    H_d = int(round(DISP_W * RP.EXTENT[2] / RP.EXTENT[1]))
    B, G, P = (upsample(m, H_d, DISP_W) for m in (base, gt, pred))
    tcd, pcd = G != B, P != B
    a_px = (RP.EXTENT[1] / DISP_W) * (RP.EXTENT[2] / H_d)
    print(f"  display areas (mm^2): true change {tcd.sum() * a_px:.3f} (native "
          f"{tc.sum() * PX_MM2:.3f}), predicted change {pcd.sum() * a_px:.3f} "
          f"(native {pc.sum() * PX_MM2:.3f})")
    grey, chg = pal.PAL["line"], pal.MASK["gt"]
    panels = [
        ([(B, grey)], "(a) Baseline"),
        ([(B & G, grey), (tcd, chg)], "(b) Truth"),
        ([(B & P, grey), (pcd, chg)], "(c) Prediction"),
        ([(B & P, grey), (tcd & pcd, pal.MASK["tp"]), (tcd & ~pcd, pal.MASK["fn"]),
          (pcd & ~tcd, pal.MASK["fp"])], "(d) Agreement"),
    ]
    # crop all panels to the lesion: bounding box of baseline, truth and prediction + margin
    ys, xs = np.nonzero(base | gt | pred)
    x0, x1 = xs.min() * RP_DX - CROP_MM, (xs.max() + 1) * RP_DX + CROP_MM
    y0, y1 = ys.min() * RP_DY - CROP_MM, (ys.max() + 1) * RP_DY + CROP_MM
    x0, y0 = max(x0, 0.0), max(y0, 0.0)
    x1, y1 = min(x1, RP.EXTENT[1]), min(y1, RP.EXTENT[2])
    print(f"  crop {x1 - x0:.2f} x {y1 - y0:.2f} mm")

    W = pal.fig_size(FRAC)[0]
    lm, rm, gap, top, leg_h = 0.02, 0.02, 0.10, 0.22, 0.40
    pw = (W - lm - rm - 3 * gap) / 4
    ph = pw * (y1 - y0) / (x1 - x0)
    H = top + ph + leg_h
    fig = plt.figure(figsize=(W, H))
    for k, (regions, title) in enumerate(panels):
        ax = fig.add_axes([(lm + k * (pw + gap)) / W, leg_h / H, pw / W, ph / H])
        draw_smooth(ax, regions, B, pal)
        ax.set_xlim(x0, x1)
        ax.set_ylim(y1, y0)
        ax.set_title(title, fontsize=7.5, pad=3, loc="left", color=pal.PAL["ink"])
    handles = [Patch(fc=grey, ec="none", label="Baseline lesion"),
               Patch(fc=chg, ec="none", label="Change"),
               Patch(fc=pal.MASK["tp"], ec="none", label="Predicted and true"),
               Patch(fc=pal.MASK["fp"], ec="none", label="Predicted only"),
               Patch(fc=pal.MASK["fn"], ec="none", label="Missed")]
    fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, fontsize=7,
               handlelength=1.2, handleheight=0.9, columnspacing=1.0, handletextpad=0.5,
               bbox_to_anchor=(0.5, 0.0))
    save(fig, "fig_experiments_rollout")


if __name__ == "__main__":
    main()
