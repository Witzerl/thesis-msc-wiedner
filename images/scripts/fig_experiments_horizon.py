"""Figure fig:experiments:horizon (Sections 5.3.3, 5.3.4, 5.5.1): growth-region Dice by
horizon bin.

(a) Profile over the four horizon bins (0-1, 1-2, 2-3, >3 years since baseline) for the
    dilated-stencil graph network, the T-FEN (energy-conserving form), the U-Net and the
    FNO, with the values of Mai et al. (2024, Table 2) as a dashed reference.
(b) The 0-1 year bin only, for the operators whose reach falls short of the per-visit
    front advance (k-NN graph network, one-hop floor, free-form FEN) against the two
    remedies (dilated stencil, T-FEN).

Aggregation is exactly thesis_numbers.py `horizon` (code repo): latest run directory per
fold, complete runs only (30 epochs), late epochs 10-29 of mai/epoch_*.json, every
rollout step's dice_growth pooled over steps, eyes, epochs and folds into the bin
lo < cum_dt_years <= hi. Seed 42.

    python fig_experiments_horizon.py
"""
import json
import os

import matplotlib.pyplot as plt
import numpy as np

from _common import LATE_FROM, panel_label, save, setup, thesis_numbers

pal = setup()
ARM, PAL = pal.ARM, pal.PAL
tn = thesis_numbers()
assert tn.LATE_FROM == LATE_FROM

ARMS = {  # thesis key -> run name (seed 42)
    "stencil": "ANISOGNN_final_dilmean",
    "tfen": "FEN_final_w96ftp7rk4d45skew",
    "unet": "UNET_final_w5",
    "fno": "FNO_final_w5",
    "fno_local": "FNO_final_w5k3",
    "fen": "FEN_final_w96Frk4d45",
    "knn": "MPPDE_final_aggrmean",
    "onehop": "MPPDE_final_l1mean",
}
LABEL = {
    "stencil": "Dilated stencil", "tfen": "T-FEN", "unet": "U-Net", "fno": "FNO",
    "fno_local": "FNO + 3×3", "fen": "FEN, free-form", "knn": "k-NN graph network",
    "onehop": "One-hop floor",
}
MAI = [0.25, 0.38, 0.38, 0.37]          # Mai et al. (2024), Table 2, growth-region DSC
BIN_LABEL = ["0–1", "1–2", "2–3", ">3"]


def horizon(arm):
    """Per-bin pooled late-epoch growth-region Dice and step counts (thesis_numbers logic)."""
    per = [[] for _ in tn.BINS]
    nf = 0
    for f in tn.FOLDS:
        rd = tn.run_dir(arm, f)
        if not tn.complete(rd):
            continue
        nf += 1
        mai = os.path.join(rd, "mai")
        for fn in os.listdir(mai):
            j = json.load(open(os.path.join(mai, fn)))
            if j["epoch"] < tn.LATE_FROM:
                continue
            for s in j["per_step"]:
                v = s["dice_growth"]
                if v != v:
                    continue
                for k, (lo, hi) in enumerate(tn.BINS):
                    if lo < s["cum_dt_years"] <= hi:
                        per[k].append(v)
    return [float(np.mean(p)) if p else float("nan") for p in per], [len(p) for p in per], nf


H, N = {}, {}
print(f"{'arm':12s} {'run':32s}" + "".join(f"{b:>8s}" for b in BIN_LABEL) + "   steps per bin")
for key, arm in ARMS.items():
    v, n, nf = horizon(arm)
    assert nf == 5, f"{arm}: only {nf} complete folds"
    H[key], N[key] = v, n
    print(f"{key:12s} {arm:32s}" + "".join(f"{x:8.3f}" for x in v) + f"   {n}")
print(f"{'mai2024':12s} {'Mai et al. (2024), Table 2':32s}" + "".join(f"{x:8.2f}" for x in MAI))

# ---------------------------------------------------------------- check against the text
# (value quoted in 05-experiments.tex, key, bin index)
TEXT = [
    (0.503, "stencil", 0), (0.600, "stencil", 1), (0.634, "stencil", 2), (0.655, "stencil", 3),
    (0.458, "unet", 0), (0.563, "unet", 1), (0.581, "unet", 2), (0.555, "unet", 3),
    (0.519, "tfen", 0), (0.602, "tfen", 1), (0.633, "tfen", 2), (0.611, "tfen", 3),
    (0.546, "fno", 1), (0.583, "fno", 2), (0.594, "fno", 3),
    (0.553, "fno_local", 1), (0.571, "fno_local", 2), (0.553, "fno_local", 3),
    (0.388, "fen", 0), (0.395, "onehop", 0), (0.393, "knn", 0),
]
# Known (2026-10-01): the text's 0.393 for the k-NN graph network is the 0-1 y value of the
# superseded mean+max arm MPPDE_final_dts; the reported k-NN arm since 2026-09-29 is the
# mean-aggregation MPPDE_final_aggrmean, 0.397, which is what the figure shows.
print("\ncheck: text value vs computed (rounded to 3 decimals)")
bad = 0
for t, key, b in TEXT:
    c = H[key][b]
    ok = round(c, 3) == t
    bad += not ok
    print(f"  {key:10s} {BIN_LABEL[b]:>4s} y  text {t:.3f}  computed {c:.4f}  {'ok' if ok else 'MISMATCH'}")
print(f"  FNO 0-1 y (not quoted in the text): {H['fno'][0]:.4f}; FNO + 3x3 0-1 y: {H['fno_local'][0]:.4f}")
# step counts in tab:experiments:mai-bins: 2980 / 2980 / 2180 / 1420 = 20 x 149 / 149 / 109 / 71
for key in ("stencil", "unet", "tfen"):
    assert N[key] == [2980, 2980, 2180, 1420], (key, N[key])
print("  steps per bin 2980 / 2980 / 2180 / 1420 (= 20 late epochs x 149 / 149 / 109 / 71 visits): ok")
print(f"  {'all text values match' if not bad else f'{bad} MISMATCHES'}")

# ---------------------------------------------------------------- figure
fig, (ax, bx) = plt.subplots(1, 2, figsize=pal.fig_size(1.166, 0.345),
                             gridspec_kw=dict(width_ratios=[1.3, 1.0], wspace=0.80))
YLIM = (0.2, 0.7)
x = np.arange(4)

LINES = [  # key, marker (the same marker per arm in both panels)
    ("stencil", "o"), ("tfen", "D"), ("fno", "^"), ("unet", "s"),
]
ends = []
for key, mk in LINES:
    ax.plot(x, H[key], color=ARM[key], marker=mk, ms=3.6, lw=1.3,
            mfc=ARM[key], mec=ARM[key], zorder=3)
    ends.append((H[key][-1], LABEL[key], ARM[key], mk, "-"))
ax.plot(x, MAI, color=ARM["mai2024"], ls=pal.ARM_STYLE["mai2024"], lw=1.1,
        marker="o", ms=3.0, mfc="white", mec=ARM["mai2024"], zorder=3)
ends.append((MAI[-1], "Mai et al. (2024)", ARM["mai2024"], None, "--"))

# direct labels at the right end (ink, in the vertical order of the line ends), nudged
# apart where two ends are close
ends.sort(key=lambda e: e[0])
MIN_GAP = 0.032
ys = [e[0] for e in ends]
for _ in range(100):
    for i in range(1, len(ys)):
        if ys[i] - ys[i - 1] < MIN_GAP:
            mid = (ys[i] + ys[i - 1]) / 2
            ys[i - 1], ys[i] = mid - MIN_GAP / 2, mid + MIN_GAP / 2
for (y0, lab, col, mk, ls), y1 in zip(ends, ys):
    ax.text(3.2, y1, lab, va="center", ha="left", fontsize=7, color=PAL["ink"],
            clip_on=False)
ax.set_xticks(x, BIN_LABEL)
ax.set_xlim(-0.25, 3.15)
ax.set_ylim(*YLIM)
ax.set_xlabel("Years since baseline")
ax.set_ylabel("Growth-region Dice")
panel_label(ax, "(a)", x=-0.13)

# (b) the 0-1 year bin, on the same Dice scale as (a)
ORDER = [("knn", "o"), ("onehop", "o"), ("fen", "o"), ("stencil", "o"), ("tfen", "D")]
names = {"knn": "k-NN graph", "onehop": "One-hop floor", "fen": "FEN, free-form",
         "stencil": "Dilated stencil", "tfen": "T-FEN"}
yy = np.array([4.0, 3.0, 2.0, 0.6, -0.4])  # gap between the short-reach group and the remedies
for (key, mk), y in zip(ORDER, yy):
    v = H[key][0]
    # light variants get the edge of their family's full colour, so they stay visible on
    # white; they are told apart by the direct labels, not by colour
    edge = {"onehop": ARM["knn"], "fen": ARM["tfen"]}.get(key, ARM[key])
    bx.hlines(y, *YLIM, color=PAL["line"], lw=0.6, zorder=1)   # row guide, not a bar
    bx.plot(v, y, marker=mk, ms=5.0, color=ARM[key], mfc=ARM[key], mec=edge, mew=0.9,
            ls="none", zorder=3)
    bx.text(v + 0.015, y, f"{v:.3f}", va="center", ha="left", fontsize=7, color=PAL["ink"])
bx.set_yticks(yy, [names[k] for k, _ in ORDER])
bx.tick_params(axis="y", length=0, labelsize=7, labelcolor=PAL["ink"])
bx.set_ylim(-1.1, 4.75)
bx.set_xlim(*YLIM)
bx.set_xticks(np.arange(0.2, 0.71, 0.1))
bx.grid(axis="y", visible=False)
bx.grid(axis="x", visible=True)
bx.set_xlabel("Growth-region Dice")
bx.set_title("0–1 years since baseline", fontsize=7.5, fontweight="normal", color=PAL["ink"],
             loc="left", pad=4)
bx.axhline(1.3, color=PAL["line"], lw=0.6, ls=(0, (2, 2)))
bx.text(YLIM[0] + 0.006, 4.55, "reach short of the front", fontsize=6.5,
        color=PAL["ink_2"], va="bottom")
bx.text(YLIM[0] + 0.006, 1.15, "remedies", fontsize=6.5, color=PAL["ink_2"], va="top")
panel_label(bx, "(b)", x=-0.42)

save(fig, "fig_experiments_horizon")
