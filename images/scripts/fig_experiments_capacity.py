"""Figure fig:experiments:capacity (Section 5.4.3; must match Table tab:experiments:capacity).

Fold-paired difference of the change-region Dice@360d of a scaled operator against the
same operator at its original size (five folds, seed 42, late-epoch means), plotted
against the parameter ratio to that original size (log scale). Width series per class are
lines (filled markers); depth points are open markers. Error bars: between-fold SE. Band:
the paired floor +/-0.016 (0.020 applies to the U-Net). Points below the y-range are drawn
at the lower edge with an arrow and their value.

TFEN_FORM switches the T-FEN rows between the Galerkin form (as in the current table) and
the energy-conserving ('skew') form; in 'skew' mode runs that are not complete on all five
folds are skipped with a warning.

Include at width=0.8\\textwidth.
Run from images/scripts/:  python fig_experiments_capacity.py
"""
import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from _common import setup, save, thesis_numbers, FLOOR_PAIRED

TFEN_FORM = "galerkin"            # 'galerkin' (current table) or 'skew'

FRAC, ASPECT = 0.8, 0.68
FOLDS = list(range(5))
YLIM = (-0.06, 0.03)

TFEN_ARMS = {
    "galerkin": dict(w48="FEN_final_w48ftp7rk4d45", w96="FEN_final_w96ftp7rk4d45",
                     w192="FEN_final_w192ftp7rk4d45", d8="FEN_final_w96d8ftp7rk4d45"),
    "skew": dict(w48="FEN_final_w48ftp7rk4d45skew", w96="FEN_final_w96ftp7rk4d45skew",
                 w192="FEN_final_w192ftp7rk4d45skew", d8="FEN_final_w96d8ftp7rk4d45skew"),
}[TFEN_FORM]

# class key -> (legend label, original-size arm, [(arm, setting, params, kind)], x dodge)
# Parameter counts are those of Table tab:experiments:capacity (checked against the logs).
CLASSES = [
    ("stencil", "Dilated-stencil GNN", "ANISOGNN_final_dilmean", 67147,
     [("ANISOGNN_final_dilmean_h32", "width 32", 18219, "width"),
      ("ANISOGNN_final_dilmean_h128", "width 128", 257163, "width"),
      ("ANISOGNN_final_dilmean_l4", "4 rounds", 119499, "depth")], 1.00),
    ("unet", "U-Net", "UNET_final_w5", 83081,
     [("UNET_final_w2", "width 2", 13637, "width"),
      ("UNET_final_w9", "width 9", 267149, "width")], 0.95),
    ("fno_local", "FNO + 3×3 local", "FNO_final_w5k3", 79960,
     [("FNO_final_w2k3", "width 2", 13189, "width"),
      ("FNO_final_w9k3", "width 9", 257804, "width")], 1.05),
    ("tfen", "T-FEN (Galerkin form)" if TFEN_FORM == "galerkin" else "T-FEN (energy-conserving)",
     TFEN_ARMS["w96"], 68503,
     [(TFEN_ARMS["w48"], "width 48", 20455, "width"),
      (TFEN_ARMS["w192"], "width 192", 247543, "width"),
      (TFEN_ARMS["d8"], "MLP depth 8", 142999, "depth")], 1.00),
]

# Table tab:experiments:capacity (05-experiments.tex ~l. 832-865), Galerkin T-FEN rows:
# arm -> (ratio, mean, fold-paired (m, se, k), per eye (m, se, m_eyes))
TABLE = {
    "ANISOGNN_final_dilmean_h32": (0.27, 0.521, (-0.005, 0.006, 1), (-0.005, 0.003, 30)),
    "ANISOGNN_final_dilmean": (1, 0.526, None, None),
    "ANISOGNN_final_dilmean_h128": (3.83, 0.518, (-0.008, 0.006, 2), (-0.009, 0.004, 22)),
    "ANISOGNN_final_dilmean_l4": (1.78, 0.517, (-0.009, 0.002, 0), (-0.010, 0.004, 20)),
    "UNET_final_w2": (0.16, 0.488, (-0.016, 0.029, 3), (-0.019, 0.016, 40)),
    "UNET_final_w5": (1, 0.505, None, None),
    "UNET_final_w9": (3.22, 0.508, (+0.004, 0.013, 1), (+0.004, 0.008, 38)),
    "FNO_final_w2k3": (0.16, 0.479, (-0.019, 0.018, 2), (-0.021, 0.010, 30)),
    "FNO_final_w5k3": (1, 0.498, None, None),
    "FNO_final_w9k3": (3.22, 0.481, (-0.018, 0.008, 1), (-0.021, 0.007, 26)),
    "FEN_final_w48ftp7rk4d45": (0.30, 0.538, (+0.005, 0.004, 3), (+0.004, 0.004, 40)),
    "FEN_final_w96ftp7rk4d45": (1, 0.534, None, None),
    "FEN_final_w192ftp7rk4d45": (3.61, 0.443, (-0.091, 0.059, 3), (-0.070, 0.014, 30)),
    "FEN_final_w96d8ftp7rk4d45": (2.09, 0.329, (-0.204, 0.067, 0), (-0.220, 0.021, 6)),
}


def _double_rounded(quoted, exact):
    """True when `quoted` (3 dp) equals `exact` rounded first to 4 dp, then half-up to 3 dp."""
    if isinstance(quoted, int):
        return quoted == exact
    from decimal import Decimal, ROUND_HALF_UP
    four = Decimal(f"{exact:.4f}")
    return float(four.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)) == quoted


def complete_folds(tn, arm):
    """Folds on which the arm has all 30 epochs (a running job may lack metrics.jsonl)."""
    out = []
    for f in FOLDS:
        rd = tn.run_dir(arm, f)
        if rd is None or not os.path.exists(os.path.join(rd, "metrics.jsonl")):
            continue
        if tn.complete(rd):
            out.append(f)
    return out


def main():
    pal = setup()
    tn = thesis_numbers()
    checks, results = [], {}
    print(f"T-FEN form: {TFEN_FORM}")

    for key, label, orig, p0, scaled, dodge in CLASSES:
        fo = complete_folds(tn, orig)
        if fo != FOLDS:
            print(f"WARNING: original {orig} complete only on folds {fo}; class skipped")
            continue
        fl0 = tn.fold_late(orig, FOLDS)
        m0 = np.mean(list(fl0.values()))
        lp = tn.params_of(orig)
        print(f"\n{label}: original {orig}, params {p0} (log {lp}), mean {m0:.4f}")
        if orig in TABLE:
            checks.append((f"{orig}: mean", f"{TABLE[orig][1]:.3f}", f"{m0:.3f}",
                           (TABLE[orig][1],), (m0,)))
        for arm, setting, p, kind in scaled:
            fo = complete_folds(tn, arm)
            if fo != FOLDS:
                print(f"  WARNING: {arm} ({setting}) complete only on folds {fo}; skipped")
                continue
            r = tn.pair(arm, orig, FOLDS)
            m, se, npos, n, t = r["fold"]
            em, ese, epos, en, et = r["eye"]
            ratio = p / p0
            lp = tn.params_of(arm)
            fl = tn.fold_late(arm, FOLDS)
            print(f"  {setting:12s} {arm:30s} params {p} (log {lp}), ratio {ratio:.2f}, "
                  f"mean {r['arm_a']:.4f}; folds " + " ".join(f"{fl[f]:.4f}" for f in FOLDS) +
                  f"\n      fold-paired {m:+.4f} +/- {se:.4f} ({npos}/{n} higher), "
                  f"per eye {em:+.4f} +/- {ese:.4f} ({epos}/{en} higher, t {et:+.2f})")
            if lp is not None and lp != p:
                print(f"      NOTE: logged parameter count {lp} differs from the table's {p}")
            results[arm] = (key, kind, ratio, m, se, dodge, setting)
            if arm in TABLE:
                tr, tm, (fm, fse, fk), (pm, pse, pk) = TABLE[arm]
                checks += [(f"{arm}: ratio", f"{tr:.2f}", f"{ratio:.2f}"),
                           (f"{arm}: mean", f"{tm:.3f}", f"{r['arm_a']:.3f}",
                            (tm,), (r["arm_a"],)),
                           (f"{arm}: fold-paired", f"{fm:+.3f} ± {fse:.3f} ({fk}/5)",
                            f"{m:+.3f} ± {se:.3f} ({npos}/{n})",
                            (fm, fse, fk), (m, se, npos)),
                           (f"{arm}: per eye", f"{pm:+.3f} ± {pse:.3f} ({pk}/75)",
                            f"{em:+.3f} ± {ese:.3f} ({epos}/{en})",
                            (pm, pse, pk), (em, ese, epos))]

    # --- plot ---------------------------------------------------------------
    ink2 = pal.PAL["ink_2"]
    fig, ax = plt.subplots(figsize=pal.fig_size(FRAC, ASPECT))
    ax.axhspan(-FLOOR_PAIRED, FLOOR_PAIRED, color=pal.PAL["primary_tint"], lw=0, zorder=0)
    ax.axhline(0, color=pal.PAL["line"], lw=0.8, zorder=1)
    y_edge = YLIM[0] + 0.004
    offscale = []
    for key, label, orig, p0, scaled, dodge in CLASSES:
        c = pal.ARM[key]
        pts = [(1.0, 0.0, 0.0)]              # the original size, shared by every class
        for arm, setting, p, kind in scaled:
            if arm not in results:
                continue
            _, kd, ratio, m, se, dg, st = results[arm]
            if kd == "width":
                pts.append((ratio * dg, m, se))
        pts.sort()
        x, y, e = map(np.array, zip(*pts))
        on = y > YLIM[0]
        ax.plot(x[on], y[on], color=c, lw=1.2, zorder=2)
        sel = on & (x != 1.0)
        ax.errorbar(x[sel], y[sel], yerr=e[sel], ls="none", marker="o", ms=4.2, color=c,
                    capsize=2, elinewidth=0.9, zorder=3)
        for arm, setting, p, kind in scaled:
            if arm not in results:
                continue
            _, kd, ratio, m, se, dg, st = results[arm]
            xx = ratio * dg
            if m < YLIM[0]:
                offscale.append((xx, m, c, kd, st))
            elif kd == "depth":
                ax.errorbar(xx, m, yerr=se, ls="none", marker="o", ms=4.2, color=c,
                            mfc="white", mew=1.1, capsize=2, elinewidth=0.9, zorder=3)
                ax.annotate(st, (xx, m - se), xytext=(0, -2), textcoords="offset points",
                            ha="center", va="top", fontsize=6.3, color=ink2)
    ax.plot(1.0, 0.0, ls="none", marker="o", ms=5, mfc=pal.PAL["ink"], mec="white",
            mew=0.8, zorder=4)
    ax.annotate("original size", (1.0, 0.0), xytext=(0, 5), textcoords="offset points",
                ha="center", va="bottom", fontsize=6.3, color=ink2)

    # points below the y-range: marker on the lower edge, arrow, value to two decimals
    for xx, m, c, kd, st in offscale:
        ax.plot(xx, y_edge, ls="none", marker="o", ms=4.2, color=c,
                mfc="white" if kd == "depth" else c, mew=1.1, zorder=4, clip_on=False)
        ax.annotate("", xy=(xx, YLIM[0] - 0.0015), xytext=(xx, y_edge - 0.0028),
                    arrowprops=dict(arrowstyle="-|>", color=c, lw=0.9, mutation_scale=6),
                    annotation_clip=False)
        short = st.replace("MLP ", "")
        ax.annotate(f"{short}\n{m:.2f}".replace("-", "−"), (xx, y_edge), xytext=(0, 5),
                    textcoords="offset points", ha="center", va="bottom", fontsize=6.3,
                    color=ink2, linespacing=1.0)

    ax.set_xscale("log")
    ax.set_xlim(0.11, 5.5)
    ax.set_xticks([0.25, 1, 4])
    ax.set_xticklabels(["1/4", "1", "4"])
    ax.xaxis.set_minor_locator(plt.NullLocator())
    ax.set_ylim(*YLIM)
    ax.set_yticks(np.arange(-0.06, 0.031, 0.02))
    ax.set_xlabel("Parameters relative to the original size (log scale)")
    ax.set_ylabel(r"$\Delta$ change-region Dice vs. original size")
    ax.text(0.40, FLOOR_PAIRED - 0.0012, "paired floor ±0.016", fontsize=6.3, color=ink2,
            ha="left", va="top")

    handles = [Line2D([], [], color=pal.ARM[k], marker="o", ms=4.2, lw=1.2, label=lab)
               for k, lab, *_ in CLASSES]
    handles += [Line2D([], [], color=ink2, marker="o", ms=4.2, lw=0, label="width (filled)"),
                Line2D([], [], color=ink2, marker="o", ms=4.2, lw=0, mfc="white", mew=1.1,
                       label="depth (open)")]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=3,
              handletextpad=0.4, columnspacing=1.2, fontsize=6.5)

    save(fig, "fig_experiments_capacity")   # same file in both modes, so it switches with the table

    print("\nCheck table (Table tab:experiments:capacity vs value computed)")
    for nm, q, g, *exact in checks:
        if q == g:
            st = "ok"
        elif exact and all(_double_rounded(a, b) for a, b in zip(exact[0], exact[1])):
            st = "rounding: the table rounded the 4-dp value again (x.xxx5)"
        else:
            st = "MISMATCH"
        print(f"  {nm:44s} {q:>24s} {g:>24s}  {st}")


if __name__ == "__main__":
    main()
