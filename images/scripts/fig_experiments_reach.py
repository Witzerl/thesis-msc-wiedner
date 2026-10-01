"""Figure fig:experiments:reach (Section 5.3.2, the reach ladder; Table tab:experiments:reach).

Fold-paired difference of the change-region Dice@360d against the default dilated stencil
(rows +/-1, columns {0, +/-7, +/-14, +/-21}; 20 neighbours), seed 42, five folds, plotted
against the column reach of one hop. Error bars: between-fold SE. Shaded band: the paired
noise floor +/-0.016. Geometries (GraphPDE/baselines/anisognn.py: columns
{0, +/-p, ..., +/-t*p}, rows +/-r, neighbours = (2r+1)(2t+1) - 1):
  meanp4   p=4,  t=3, r=1: columns up to +/-12, 20 neighbours (spacing 4)
  dilmean  p=7,  t=3, r=1: columns up to +/-21, 20 neighbours (default)
  meant5   p=7,  t=5, r=1: columns up to +/-35, 32 neighbours (same spacing, more taps)
  meanp14  p=14, t=3, r=1: columns up to +/-42, 20 neighbours (spacing 14, sparser)
  meanr2   p=7,  t=3, r=2: columns up to +/-21, rows +/-2, 34 neighbours
and the index-space k-NN graph (k=12), whose hop reaches +/-2 columns (and +/-2 rows).
Vertical dashed lines: median (12 columns) and 90th-percentile (23 columns) per-visit
front advance (Section 4.3.3).

Include at width=0.8\\textwidth.
Run from images/scripts/:  python fig_experiments_reach.py
"""
import json
import os

import numpy as np
import matplotlib.pyplot as plt

from _common import setup, save, thesis_numbers, FLOOR_PAIRED, DX_MM

FRAC, ASPECT = 0.8, 0.62
FOLDS = list(range(5))
DEFAULT = "ANISOGNN_final_dilmean"
MEDIAN_ADV, P90_ADV = 12, 23          # columns per 180-day visit (04-method.tex, Section 4.3.3)

# experiment -> (column reach, expected (pitch, taps, rows), label, marker, quoted (mean, se, k))
GEOMS = {
    "ANISOGNN_final_meanp4": (12, (4, 3, 1), "spacing 4\n20 neighbours", "o", (-0.019, 0.008, 1)),
    "ANISOGNN_final_meant5": (35, (7, 5, 1), "spacing 7\n32 neighbours", "s", (-0.010, 0.003, 1)),
    "ANISOGNN_final_meanp14": (42, (14, 3, 1), "spacing 14\n20 neighbours", "^", (-0.026, 0.004, 0)),
    "ANISOGNN_final_meanr2": (21, (7, 3, 2), "rows ±2\n34 neighbours", "D", (-0.039, 0.005, 0)),
}
KNN = "MPPDE_final_aggrmean"
KNN_QUOTED = (-0.0635, 0.0106, 0)     # Section 5.3.2: stencil - k-NN = +0.0635 +/- 0.0106 (5/5)
KNN_EYE_QUOTED = (-0.0647, 0.0062)    # per eye +0.0647 +/- 0.0062 (70/75) with the sign flipped


def geometry(exp):
    """(pitch, taps, rows, neighbours) from the fold-0 args.json."""
    a = json.load(open(os.path.join(thesis_numbers().run_dir(exp, 0), "args.json")))
    p, t, r = a.get("aniso_pitch", 7), a.get("aniso_taps", 3), a.get("aniso_rows", 1)
    return p, t, r, (2 * r + 1) * (2 * t + 1) - 1


def main():
    pal = setup()
    tn = thesis_numbers()
    checks = []

    p, t, r, nb = geometry(DEFAULT)
    print(f"default {DEFAULT}: pitch {p}, taps {t}, rows {r}: reach +/-{p * t} columns, {nb} neighbours")
    pts = {}
    for exp, (reach, exp_geom, label, mk, quoted) in GEOMS.items():
        p, t, r, nb = geometry(exp)
        assert (p, t, r) == exp_geom, f"{exp}: geometry {p, t, r} != {exp_geom}"
        assert p * t == reach
        res = tn.pair(exp, DEFAULT, FOLDS)
        m, se, npos, n, tt = res["fold"]
        em, ese, epos, en, et = res["eye"]
        print(f"{exp:26s} pitch {p:2d} taps {t} rows {r}: reach +/-{p * t:2d} col "
              f"({p * t * DX_MM:.3f} mm), {nb} neighbours | arm {res['arm_a']:.4f}\n"
              f"    fold-paired {m:+.4f} +/- {se:.4f} ({npos}/{n} higher), "
              f"LOFO [{res['fold_lofo'][0]:+.4f}, {res['fold_lofo'][1]:+.4f}]\n"
              f"    per eye     {em:+.4f} +/- {ese:.4f} ({epos}/{en} higher, t {et:+.2f}), "
              f"LOFO [{res['eye_lofo'][0]:+.4f}, {res['eye_lofo'][1]:+.4f}]")
        pts[exp] = (reach, m, se)
        checks += [(f"{exp}: fold-paired mean", f"{quoted[0]:+.3f}", f"{m:+.3f}"),
                   (f"{exp}: SE", f"{quoted[1]:.3f}", f"{se:.3f}"),
                   (f"{exp}: folds higher", f"{quoted[2]}/5", f"{npos}/{n}")]
        if exp == "ANISOGNN_final_meant5":
            checks.append(("meant5: neighbours (text/table: 'spacing 7, 32 neighbours')", "32",
                           f"{nb}"))
        checks.append((f"{exp}: neighbours (table)", str({"ANISOGNN_final_meanp4": 20,
                       "ANISOGNN_final_meant5": 32, "ANISOGNN_final_meanp14": 20,
                       "ANISOGNN_final_meanr2": 34}[exp]), f"{nb}"))

    res = tn.pair(KNN, DEFAULT, FOLDS)
    m, se, npos, n, tt = res["fold"]
    em, ese, epos, en, et = res["eye"]
    print(f"{KNN} (index-space k-NN, k=12; hop reaches +/-2 columns) | arm {res['arm_a']:.4f}\n"
          f"    fold-paired {m:+.4f} +/- {se:.4f} ({npos}/{n} higher)\n"
          f"    per eye     {em:+.4f} +/- {ese:.4f} ({epos}/{en} higher, t {et:+.2f})")
    knn = (2, m, se)
    checks += [("k-NN vs stencil: fold-paired", f"{KNN_QUOTED[0]:+.4f}", f"{m:+.4f}"),
               ("k-NN vs stencil: SE", f"{KNN_QUOTED[1]:.4f}", f"{se:.4f}"),
               ("k-NN vs stencil: per eye", f"{KNN_EYE_QUOTED[0]:+.4f}", f"{em:+.4f}"),
               ("k-NN vs stencil: per-eye SE", f"{KNN_EYE_QUOTED[1]:.4f}", f"{ese:.4f}"),
               ("k-NN vs stencil: eyes stencil higher", "70/75", f"{en - epos}/{en}")]

    # --- plot ---------------------------------------------------------------
    blue, sky, ink2 = pal.ARM["stencil"], pal.ARM["knn"], pal.PAL["ink_2"]
    fig, ax = plt.subplots(figsize=pal.fig_size(FRAC, ASPECT))
    ax.axhspan(-FLOOR_PAIRED, FLOOR_PAIRED, color=pal.PAL["primary_tint"], lw=0, zorder=0)
    ax.axhline(0, color=pal.PAL["line"], lw=0.8, zorder=1)
    for xv, lab in ((MEDIAN_ADV, "median"), (P90_ADV, "90th pct.")):
        ax.axvline(xv, color=pal.PAL["muted"], lw=0.8, ls="--", zorder=1)
        ax.text(xv + 0.6, 0.026, f"{lab}\nfront advance", fontsize=6.3, color=ink2,
                ha="left", va="top", linespacing=1.0)

    # rows +/-1 family, connected in order of reach
    xs =[pts["ANISOGNN_final_meanp4"][0], 21, pts["ANISOGNN_final_meant5"][0],
          pts["ANISOGNN_final_meanp14"][0]]
    ys = [pts["ANISOGNN_final_meanp4"][1], 0.0, pts["ANISOGNN_final_meant5"][1],
          pts["ANISOGNN_final_meanp14"][1]]
    ax.plot(xs, ys, color=blue, lw=1.0, zorder=2)
    for exp, (reach, m_, se_) in pts.items():
        mk = GEOMS[exp][3]
        ax.errorbar(reach, m_, yerr=se_, ls="none", marker=mk, ms=4.5, color=blue,
                    mfc=blue if exp != "ANISOGNN_final_meanr2" else "white", mew=1.0,
                    capsize=2, elinewidth=0.9, zorder=3)
    ax.plot(21, 0.0, ls="none", marker="o", ms=6, mfc=blue, mec="white", mew=0.8, zorder=4)
    ax.errorbar(*knn[:2], yerr=knn[2], ls="none", marker="o", ms=4.5, color=sky, mfc=sky,
                capsize=2, elinewidth=0.9, zorder=3)

    # direct labels
    lab = dict(fontsize=6.5, color=ink2, linespacing=1.0)
    ax.annotate("default: rows ±1,\nspacing 7, 20 nbrs", (21, 0.0), xytext=(4, 5),
                textcoords="offset points", ha="left", va="bottom", zorder=5,
                bbox=dict(fc=pal.PAL["primary_tint"], ec="none", pad=0.4), **lab)
    x12, y12 = pts["ANISOGNN_final_meanp4"][:2]
    ax.annotate("spacing 4\n20 nbrs", (x12, y12), xytext=(-5, -3), textcoords="offset points",
                ha="right", va="top", **lab)
    x35, y35 = pts["ANISOGNN_final_meant5"][:2]
    ax.annotate("spacing 7\n32 nbrs", (x35, y35), xytext=(-4, -5), textcoords="offset points",
                ha="right", va="top", **lab)
    x42, y42 = pts["ANISOGNN_final_meanp14"][:2]
    ax.annotate("spacing 14\n20 nbrs", (x42, y42), xytext=(-5, -3), textcoords="offset points",
                ha="right", va="top", **lab)
    xr2, yr2 = pts["ANISOGNN_final_meanr2"][:2]
    ax.annotate("rows ±2, spacing 7\n34 nbrs", (xr2, yr2), xytext=(6, -2),
                textcoords="offset points", ha="left", va="center", zorder=5,
                bbox=dict(fc="white", ec="none", pad=0.4), **lab)
    ax.annotate("index-space\nk-NN, k = 12", knn[:2], xytext=(6, 0), textcoords="offset points",
                ha="left", va="center", **lab)
    ax.text(44.5, FLOOR_PAIRED - 0.002, "paired floor ±0.016", fontsize=6.3, color=ink2,
            ha="right", va="top")

    ax.set_xlim(0, 45)
    ax.set_xticks([0, 7, 14, 21, 28, 35, 42])
    ax.set_ylim(-0.08, 0.028)
    ax.set_yticks(np.arange(-0.08, 0.021, 0.02))
    ax.set_xlabel("Reach of one hop along a row (columns)")
    ax.set_ylabel(r"$\Delta$ change-region Dice vs. default")
    sec = ax.secondary_xaxis("top", functions=(lambda c: c * DX_MM, lambda mm: mm / DX_MM))
    sec.set_xticks([0, 0.05, 0.10, 0.15, 0.20, 0.25])
    sec.set_xlabel("mm", fontsize=7, color=ink2, labelpad=2)
    sec.tick_params(labelsize=7, colors=ink2)
    sec.spines["top"].set_visible(True)
    sec.spines["top"].set_color(pal.PAL["line"])

    save(fig, "fig_experiments_reach")

    print("\nCheck table (value in text / Table tab:experiments:reach vs value computed)")
    for name, q, g in checks:
        print(f"  {name:52s} {q:>8s} {g:>8s}  {'ok' if q == g else 'MISMATCH'}")


if __name__ == "__main__":
    main()
