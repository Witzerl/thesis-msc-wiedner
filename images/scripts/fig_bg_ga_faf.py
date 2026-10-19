"""Chapter 2, Figure fig:bg:ga-faf -- geographic atrophy on fundus autofluorescence (FAF).

    cd images/scripts && python fig_bg_ga_faf.py --candidates   # rank eyes, preview the top 3
    cd images/scripts && python fig_bg_ga_faf.py                # final figure for EYE below

Panels: (a) FAF of one eye at baseline, (b) FAF of the same eye about three years later.
Grey, no colour map; each image is contrast-stretched on its own (1st-99th percentile of
the displayed crop, black acquisition border excluded), because FAF brightness is in
arbitrary units per acquisition. Dashed square: the 49 x 1024 modelling window
(centre crop / zero pad of the native OCT grid, as in fig_appendix_cohort.py), drawn on
the FAF image through the visit's T_mask, labelled with its size (about 6 x 6 mm).

Source (read-only): data/MUW_GA/scans/<EYE>/<day>/faf_global.png, oct.transform.json,
mask_oct.png. Frame checks (2026-10-19, 26 visits of 13 eyes):
  * T_mask maps (native OCT row, column) to (global row, column): mask_global sampled
    through it reproduces mask_oct at IoU 1.000 (0.30 with the axes swapped);
  * mask_global lies on the FAF lesion edge: the FAF gradient along the mask boundary
    peaks at zero shift (within 2 px), and the FAF inside the lesion is about half as
    bright as a 30 px ring around it -- so faf_global is in the frame of T_mask.
Global pixel size from T_mask: 0.12118 / T[0,0] mm per row, 0.00568 / T[1,1] mm per
column (about 6.0 and 5.9 um).

Eye rule (fixed before looking at the images; the author confirms the eye):
  1. follow-up of at least three years; the later visit is the one closest to 1095 days
     after baseline;
  2. the lesion lies inside the modelling window without touching its edge at both shown
     visits (touch_valid False, pad-aware, as in Section 3.3);
  3. among those, the eye whose square-root-area growth rate over its whole follow-up is
     closest to the cohort median (0.234 mm/yr).
"""
from __future__ import annotations

import argparse
import json

import numpy as np
import pandas as pd
from PIL import Image

from _common import setup, save, panel_label, SCANS, NROWS, NCOLS, DY_MM, DX_MM, PREVIEW
from fig_appendix_cohort import visit_table, eye_table

EYE = "PEAT0021_OD"   # rank 1 by the rule; confirmed by the author 2026-10-19
MARGIN_MM = 1.2       # FAF shown around the window on each side
TARGET_DAYS = 1095
MEDIAN_GROWTH = 0.234


def pick_visits(days: list[int]) -> tuple[int, int]:
    d0 = days[0]
    later = min((d for d in days[1:] if d - d0 >= 1080), key=lambda d: abs(d - d0 - TARGET_DAYS))
    return d0, later


def ranking() -> pd.DataFrame:
    v = visit_table()
    e = eye_table(v).set_index("eye")
    rows = []
    for eye, g in v.groupby("eye"):
        days = sorted(g.day)
        if days[-1] - days[0] < 1080:
            continue
        d0, d1 = pick_visits(days)
        touch = g.set_index("day").touch_valid
        if touch[d0] or touch[d1]:
            continue
        rows.append(dict(eye=eye, day0=d0, day1=d1, growth=e.loc[eye, "growth_mm_yr"],
                         area0=e.loc[eye, "base_area_mm2"]))
    r = pd.DataFrame(rows)
    r["dist"] = (r.growth - MEDIAN_GROWTH).abs()
    return r.sort_values("dist").reset_index(drop=True)


def window_global(vd) -> tuple[np.ndarray, float, float]:
    """Corners of the 49 x 1024 window in global (row, col) pixels, and the global
    pixel size (mm per row, mm per column)."""
    T = np.array(json.loads((vd / "oct.transform.json").read_text())["T_mask"])
    H, W = np.asarray(Image.open(vd / "mask_oct.png")).shape

    def start(n, t):
        return (n - t) // 2 if n >= t else -((t - n) // 2)

    r0, c0 = start(H, NROWS) - 0.5, start(W, NCOLS) - 0.5
    rr = T[0, 0] * np.array([r0, r0 + NROWS]) + T[0, 2]
    cc = T[1, 1] * np.array([c0, c0 + NCOLS]) + T[1, 2]
    return np.array([rr, cc]), DY_MM / T[0, 0], DX_MM / T[1, 1]


def stretch(a: np.ndarray) -> np.ndarray:
    valid = a[a > 2]
    lo, hi = np.percentile(valid, [1, 99])
    return np.clip((a - lo) / (hi - lo), 0, 1)


def draw(axes, eye: str, d0: int, d1: int, pal) -> None:
    import matplotlib.patches as mpatches
    for k, (ax, day) in enumerate(zip(axes, (d0, d1))):
        vd = SCANS / eye / str(day)
        faf = np.asarray(Image.open(vd / "faf_global.png")).astype(float)
        (rr, cc), py, px = window_global(vd)
        mr, mc = MARGIN_MM / py, MARGIN_MM / px
        R0, R1 = int(max(rr[0] - mr, 0)), int(min(rr[1] + mr, faf.shape[0]))
        C0, C1 = int(max(cc[0] - mc, 0)), int(min(cc[1] + mc, faf.shape[1]))
        crop = stretch(faf[R0:R1, C0:C1])
        # extent in mm, origin at the window's top-left corner
        ext = ((C0 - cc[0]) * px, (C1 - cc[0]) * px, (R1 - rr[0]) * py, (R0 - rr[0]) * py)
        ax.imshow(crop, cmap="gray", vmin=0, vmax=1, extent=ext, interpolation="lanczos")
        # window: dashed primary blue on a white halo, visible on dark and bright retina
        rect = dict(xy=(0, 0), width=(cc[1] - cc[0]) * px, height=(rr[1] - rr[0]) * py, fill=False)
        ax.add_patch(mpatches.Rectangle(**rect, ec="white", lw=2.6))
        ax.add_patch(mpatches.Rectangle(**rect, ec=pal.PAL["primary"], lw=1.4, ls=(0, (4, 3))))
        # size of the window (5.94 x 5.82 mm), on its top edge, white box with ink text
        ax.text(rect["width"] / 2, 0, "≈ 6 × 6 mm", color=pal.PAL["ink"], ha="center",
                va="center", fontsize=7,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9))
        ax.set_xlim(ext[0], ext[1]); ax.set_ylim(ext[2], ext[3])
        ax.set_axis_off()
        panel_label(ax, "(a)" if k == 0 else "(b)", x=0.0, y=1.01)
        ax.texts[-1].set_ha("left")


def figure(eye: str, d0: int, d1: int, name: str, pal, to_preview: bool = False):
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=pal.fig_size(1.0, 0.5))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.94, bottom=0.01, wspace=0.04)
    draw(axes, eye, d0, d1, pal)
    if to_preview:
        PREVIEW.mkdir(exist_ok=True)
        fig.savefig(PREVIEW / f"{name}.png", dpi=200)
        print(f"wrote {PREVIEW / name}.png")
    else:
        save(fig, name, raster=True)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", action="store_true")
    ap.add_argument("--top", type=int, default=3)
    args = ap.parse_args()
    pal = setup()
    r = ranking()
    v = visit_table()
    print(f"eyes passing rules 1-2: {len(r)} of {v.eye.nunique()}")
    print(r.head(10).to_string(float_format=lambda x: f"{x:.3f}"))
    if args.candidates:
        for i, row in r.head(args.top).iterrows():
            figure(row.eye, row.day0, row.day1, f"fig_bg_ga_faf_cand{i + 1}_{row.eye}", pal, True)
        return
    if EYE is None:
        raise SystemExit("set EYE after the author has confirmed the candidate")
    row = r.set_index("eye").loc[EYE]
    print(f"{EYE}: days {row.day0} -> {row.day1} ({(row.day1 - row.day0) / 365:.2f} years), "
          f"growth {row.growth:.3f} mm/yr, baseline area {row.area0:.2f} mm2 (window)")
    figure(EYE, int(row.day0), int(row.day1), "fig_bg_ga_faf", pal)


if __name__ == "__main__":
    main()
