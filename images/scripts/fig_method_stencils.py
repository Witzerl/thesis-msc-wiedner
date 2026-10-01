"""Figure fig:method:stencils (Section 4.3.3): the index-space k-NN neighbourhood and the
dilated stencil at the physical aspect ratio of the grid.

Geometry only: grid pitch (0.12118 mm between rows, 0.00568 mm between columns), the
k = 12 index-space neighbourhood (squared index radius <= 4, no self-loop) and the dilated
stencil (rows -1..1 x columns 0, +-7, +-14, +-21; baselines/anisognn.py defaults pitch 7,
taps 3, rows 1). Front-advance quantiles (median 12, 90th percentile 23 columns per
180-day visit) as stated in Section 4.3.3.

    python fig_method_stencils.py
"""
import itertools

import matplotlib.pyplot as plt
import numpy as np

from _common import DX_MM, DY_MM, save, setup

pal = setup()
ARM, PAL = pal.ARM, pal.PAL

# ---------------------------------------------------------------- neighbourhoods
KNN = [(dr, dc) for dr in range(-2, 3) for dc in range(-2, 3)
       if 0 < dr * dr + dc * dc <= 4]
STENCIL = [(dr, dc) for dr in (-1, 0, 1) for dc in (0, -7, 7, -14, 14, -21, 21)
           if (dr, dc) != (0, 0)]
assert len(KNN) == 12 and len(STENCIL) == 20


def two_rounds(nb):
    """Offsets reachable in two message-passing rounds (excluding the node itself)."""
    s = set(nb) | {(0, 0)}
    return sorted({(a[0] + b[0], a[1] + b[1]) for a, b in itertools.product(s, s)} - {(0, 0)})


KNN2, STENCIL2 = two_rounds(KNN), two_rounds(STENCIL)
MEDIAN_COLS, P90_COLS = 12, 23


def mm(offsets):
    o = np.array(offsets, float)
    return o[:, 1] * DX_MM, o[:, 0] * DY_MM          # x along a row, y across rows


for name, nb, nb2 in (("k-NN", KNN, KNN2), ("stencil", STENCIL, STENCIL2)):
    x, y = mm(nb)
    x2, y2 = mm(nb2)
    print(f"{name}: {len(nb)} neighbours, one hop +-{abs(x).max():.3f} mm along / "
          f"+-{abs(y).max():.3f} mm across; two rounds +-{max(abs(c) for _, c in nb2)} cols "
          f"(+-{abs(x2).max():.3f} mm) / +-{max(abs(r) for r, _ in nb2)} rows (+-{abs(y2).max():.3f} mm)")
print(f"front advance: median {MEDIAN_COLS} cols = {MEDIAN_COLS * DX_MM:.3f} mm, "
      f"p90 {P90_COLS} cols = {P90_COLS * DX_MM:.3f} mm")

# ---------------------------------------------------------------- figure
LIM = 0.31                                           # mm, half-width of each panel
fig, axes = plt.subplots(1, 2, figsize=pal.fig_size(1.0, 0.63), sharey=True,
                         gridspec_kw=dict(wspace=0.06, left=0.1, right=0.975, top=0.94, bottom=0.215))

for ax, (label, nb, nb2, col) in zip(axes, [
        ("Index-space $k$-NN graph ($k = 12$)", KNN, KNN2, ARM["knn"]),
        ("Dilated stencil (20 neighbours)", STENCIL, STENCIL2, ARM["stencil"])]):
    ax.set_title(label, loc="left", fontsize=8, fontweight="semibold", pad=4)
    ax.grid(False)
    # rows of the lattice: nodes along a row are 0.0057 mm apart and read as a line
    for k in range(-3, 4):
        ax.axhline(k * DY_MM, color=PAL["line"], lw=0.6, zorder=0)
    # per-visit front advance along the row, both directions
    for c, ls in ((MEDIAN_COLS, (0, (3, 2))), (P90_COLS, (0, (1, 1.5)))):
        for s in (-1, 1):
            ax.axvline(s * c * DX_MM, color=PAL["muted"], lw=0.8, ls=ls, zorder=1)
    x2, y2 = mm(nb2)
    ax.scatter(x2, y2, s=9, facecolor="white", edgecolor=col, lw=0.6, zorder=2,
               clip_on=True)
    x1, y1 = mm(nb)
    ax.scatter(x1, y1, s=11, color=col, edgecolor=PAL["ink"], lw=0.3, zorder=3)
    ax.scatter([0], [0], s=16, color=PAL["ink"], zorder=4)
    ax.set_xlim(-LIM, LIM)
    ax.set_ylim(-LIM, LIM)
    ax.set_aspect("equal")
    ax.set_xticks([-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3])
    ax.set_yticks([-0.24, -0.12, 0, 0.12, 0.24])
    ax.set_xlabel("along a row (mm)")
    ax.spines[["top", "right"]].set_visible(True)
axes[0].set_ylabel("across rows (mm)")

# the k-NN graph's two-round region leaves the panel vertically: say how far it goes
ax = axes[0]
for s in (-1, 1):
    ax.annotate("", xy=(0.0, s * (LIM - 0.005)), xytext=(0.0, s * (LIM - 0.055)),
                arrowprops=dict(arrowstyle="-|>", lw=0.6, color=ARM["knn"]))
ax.text(-LIM + 0.012, LIM - 0.012, "two rounds continue\nto $\\pm$4 rows ($\\pm$0.48 mm)",
        fontsize=6.5, color=PAL["ink_2"], va="top", ha="left",
        bbox=dict(fc="white", ec="none", pad=0.6))

# inset: the same k-NN neighbourhood in grid indices, where it is a diamond
ins = ax.inset_axes([0.60, 0.04, 0.37, 0.37])
o1, o2 = np.array(KNN), np.array(KNN2)
ins.scatter(o2[:, 1], o2[:, 0], s=7, facecolor="white", edgecolor=ARM["knn"], lw=0.5)
ins.scatter(o1[:, 1], o1[:, 0], s=9, color=ARM["knn"], edgecolor=PAL["ink"], lw=0.3)
ins.scatter([0], [0], s=12, color=PAL["ink"])
ins.set_xlim(-4.8, 4.8)
ins.set_ylim(-4.8, 4.8)
ins.set_aspect("equal")
ins.set_xticks([])
ins.set_yticks([])
ins.grid(False)
for sp in ins.spines.values():
    sp.set_visible(True)
    sp.set_color(PAL["line"])
ins.set_facecolor("white")
ins.text(0.5, 1.03, "in grid indices", transform=ins.transAxes, ha="center",
         va="bottom", fontsize=6.5, color=PAL["ink_2"])

# shared legend
h = [plt.Line2D([], [], ls="", marker="o", ms=4, color=PAL["ink"], label="node"),
     plt.Line2D([], [], ls="", marker="o", ms=3.5, mfc=ARM["stencil"], mec=PAL["ink"],
                mew=0.3, label="one hop"),
     plt.Line2D([], [], ls="", marker="o", ms=3.2, mfc="white", mec=ARM["stencil"],
                mew=0.6, label="two rounds"),
     plt.Line2D([], [], color=PAL["muted"], lw=0.8, ls=(0, (3, 2)),
                label="median front advance (12 columns)"),
     plt.Line2D([], [], color=PAL["muted"], lw=0.8, ls=(0, (1, 1.5)),
                label="90th percentile (23 columns)")]
h = [h[0], h[3], h[1], h[4], h[2]]   # two rows: markers above, reference lines below
fig.legend(handles=h, loc="lower center", ncol=3, bbox_to_anchor=(0.5, 0.0),
           frameon=False, fontsize=7, handletextpad=0.4, columnspacing=1.0, handlelength=1.6)

save(fig, "fig_method_stencils")
