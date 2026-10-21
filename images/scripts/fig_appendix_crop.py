"""Appendix A, Figure fig:appendix:crop -- native grid shapes against the 49 x 1024 window,
and the lesion area the window cuts off.

    cd images/scripts && python fig_appendix_crop.py

(a) native en-face grid of every eye (B-scans x A-scans; constant within an eye), with the
    49 x 1024 modelling window as dashed reference lines;
(the former panel (b), the share of visits losing lesion area to the crop, was dropped on
2026-10-21; its numbers are still printed for Section 3.3).
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
    # 2026-10-21 (author): only the grid panel; the lesion-loss curve (former panel (b)) was dropped,
    # its numbers are in Section 3.3 and are still printed above.
    fig, ax = plt.subplots(figsize=pal.fig_size(0.6, 0.62), layout="constrained")
    blue, ink2 = pal.PAL["primary"], pal.PAL["ink_2"]
    ax.axvline(NCOLS, color=pal.PAL["muted"], lw=0.9, ls="--", zorder=1)
    ax.axhline(NROWS, color=pal.PAL["muted"], lw=0.9, ls="--", zorder=1)
    ax.scatter(eyes.W, eyes.H, s=12, color=blue, edgecolor="white", linewidth=0.4,
               alpha=0.9, zorder=3)
    ax.text(NCOLS + 12, 66.5, "1024 columns", fontsize=6.5, color=ink2, va="top", ha="left")
    ax.text(1725, NROWS + 0.6, "49 rows", fontsize=6.5, color=ink2, va="bottom", ha="right")
    ax.set_xlim(930, 1740)
    ax.set_ylim(35, 68)
    ax.set_xlabel("A-scans per B-scan (columns)")
    ax.set_ylabel("B-scans (rows)")
    ax.grid(axis="both")
    save(fig, "fig_appendix_crop")


if __name__ == "__main__":
    main()
