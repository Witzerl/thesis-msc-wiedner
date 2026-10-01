"""Appendix A, Figure fig:appendix:crop -- native grid shapes against the 49 x 1024 window,
and the lesion area the window cuts off.

    cd images/scripts && python fig_appendix_crop.py

(a) native en-face grid of every eye (B-scans x A-scans; constant within an eye), with the
    49 x 1024 modelling window as dashed reference lines;
(b) share of the 553 visits that lose more than a given fraction of their lesion area to
    the centre crop (complementary cumulative distribution).
Data and definitions: fig_appendix_cohort.visit_table() (raw mask_oct.png of every visit,
crop/pad arithmetic of tools/precompute_graphs_ga.py). Every annotated number is printed.
"""
from __future__ import annotations

import numpy as np

from _common import setup, save, NROWS, NCOLS, DY_MM, DX_MM
from fig_appendix_cohort import visit_table


def main() -> None:
    pal = setup()
    import matplotlib.pyplot as plt

    v = visit_table()
    n = len(v)
    eyes = v.groupby("eye").agg(H=("H", "first"), W=("W", "first"), n=("day", "size"))
    lost = (1.0 - v.n_window / v.n_native).to_numpy() * 100.0      # % of the lesion

    # --- printed record of every number in the figure / caption
    print(f"visits {n}, eyes {len(eyes)}, distinct shapes {v[['H', 'W']].drop_duplicates().shape[0]}")
    print(f"rows {v.H.min()}-{v.H.max()}, columns {v.W.min()}-{v.W.max()}")
    print(f"native extent: {v.H.min() * DY_MM:.2f}-{v.H.max() * DY_MM:.2f} mm (rows) x "
          f"{v.W.min() * DX_MM:.2f}-{v.W.max() * DX_MM:.2f} mm (columns)")
    for lab, m in [("rows < 49 (row-padded)", eyes.H < NROWS), ("rows > 49", eyes.H > NROWS),
                   ("rows = 49", eyes.H == NROWS), ("cols < 1024 (col-padded)", eyes.W < NCOLS),
                   ("cols > 1024", eyes.W > NCOLS)]:
        print(f"  eyes {lab}: {int(m.sum())}, visits {int(eyes.n[m].sum())}")
    for t in (0, 1, 5, 10, 20):
        k = int((lost > t).sum())
        print(f"visits losing > {t:>2} % of the lesion: {k}/{n} = {100 * k / n:.1f} %")
    print(f"largest loss {lost.max():.1f} %")
    print(f"lesion touches border of the window's non-pad region: {100 * v.touch_valid.mean():.1f} %;"
          f" touches the native scan edge: {100 * v.touch_native.mean():.1f} %")

    plt.rcParams["savefig.bbox"] = "standard"
    fig, axs = plt.subplots(1, 2, figsize=pal.fig_size(1.0, 0.36), layout="constrained")
    fig.get_layout_engine().set(w_pad=0.04, h_pad=0.03, wspace=0.08)
    blue, ink, ink2 = pal.PAL["primary"], pal.PAL["ink"], pal.PAL["ink_2"]

    # (a) native grid shapes
    ax = axs[0]
    ax.axvline(NCOLS, color=pal.PAL["muted"], lw=0.9, ls="--", zorder=1)
    ax.axhline(NROWS, color=pal.PAL["muted"], lw=0.9, ls="--", zorder=1)
    ax.scatter(eyes.W, eyes.H, s=10, color=blue, edgecolor="white", linewidth=0.4,
               alpha=0.9, zorder=3)
    ax.text(NCOLS + 12, 66.5, "1024 columns", fontsize=6.5, color=ink2, va="top", ha="left")
    ax.text(1725, NROWS + 0.6, "49 rows", fontsize=6.5, color=ink2, va="bottom", ha="right")
    ax.set_xlim(930, 1740)
    ax.set_ylim(35, 68)
    ax.set_xlabel("A-scans per B-scan (columns)")
    ax.set_ylabel("B-scans (rows)")
    ax.grid(axis="both")

    # (b) lesion area lost to the crop
    ax = axs[1]
    xs = np.linspace(0, 30, 601)
    share = np.array([(lost > x).mean() * 100 for x in xs])
    ax.step(xs, share, where="post", color=blue, lw=1.4)
    for t in (1, 5):
        s = (lost > t).mean() * 100
        ax.plot([t], [s], "o", ms=3.2, color=blue, zorder=4)
        ax.annotate(f"{s:.1f} % lose > {t} %", (t, s), xytext=(6, 4),
                    textcoords="offset points", fontsize=6.5, color=ink, va="bottom")
    s0 = (lost > 0).mean() * 100
    ax.plot([0], [s0], "o", ms=3.2, color=blue, zorder=4, clip_on=False)
    ax.annotate(f"{s0:.1f} % lose any area", (0, s0), xytext=(6, 2),
                textcoords="offset points", fontsize=6.5, color=ink, va="bottom")
    ax.annotate(f"largest loss {lost.max():.1f} %", (lost.max(), 100 / n), xytext=(-4, 8),
                textcoords="offset points", fontsize=6.5, color=ink, ha="right", va="bottom",
                arrowprops=dict(arrowstyle="-", color=ink2, lw=0.6))
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 32)
    ax.set_xlabel("Lesion area cut off by the window, $x$ (%)")
    ax.set_ylabel("Visits losing more than $x$ (%)")

    for ax, s in zip(axs, "ab"):
        ax.set_title(f"({s})", loc="left", fontsize=8, fontweight="bold", pad=3)
    save(fig, "fig_appendix_crop")


if __name__ == "__main__":
    main()
