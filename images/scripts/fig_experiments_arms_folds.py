"""Figure fig:experiments:arms-folds (Section 5.2, next to Table tab:experiments:arms).

Dot plot: one row per arm in the order of Table 5.1 (top = T-FEN), the five fold values
(late-epoch mean change-region Dice@360d, epochs 10-29, seed 42) as small markers whose
shape encodes the fold index (the same shape for a fold in every row), and the five-fold
mean as a short vertical bar. RK4-wrapped arms use open markers. The per-pixel floor and
persistence (both 0) lie far outside the plotted range and are left out (caption).

Include at width=0.9\\textwidth.
Run from images/scripts/:  python fig_experiments_arms_folds.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from _common import setup, save, thesis_numbers

FRAC, ASPECT = 0.9, 0.66
FOLDS = range(5)
FOLD_MARKER = {0: "o", 1: "s", 2: "^", 3: "D", 4: "v"}
# small fixed vertical offset per fold (fold 0 on top) so that close values do not hide
# each other; the offset is the same in every row
FOLD_DY = {0: 0.18, 1: 0.09, 2: 0.0, 3: -0.09, 4: -0.18}

# (experiment, palette key, row label, rk4?, value quoted in Table 5.1)
ROWS = [
    ("FEN_final_w96ftp7rk4d45skew", "tfen", "T-FEN", False, 0.5428),
    ("ANISOGNN_final_dilmean", "stencil", "Graph network, dilated stencil", False, 0.5258),
    ("ANISOGNN_final_oderk4n1", "stencil", "Graph network, dilated stencil, RK4", True, 0.5139),
    ("UNET_final_w5", "unet", "U-Net", False, 0.5046),
    ("FNO_final_w5k3", "fno_local", "FNO with 3×3 local path", False, 0.4984),
    ("FNO_final_w5rk4", "fno", "FNO, RK4", True, 0.4893),
    ("FNO_final_w5", "fno", "FNO", False, 0.4831),
    ("FEN_final_w96Frk4d45", "fen", "FEN, free-form only", False, 0.4810),
    ("MPPDE_final_aggrmean", "knn", "Graph network, k-NN, k = 12", False, 0.4623),
    ("MPPDE_final_k20", "knn_k20", "Graph network, k-NN, k = 20", False, 0.4519),
    ("MPPDE_final_l1mean", "onehop", "One-hop floor", False, 0.4515),
]
# left out of the plot (value far outside the range), checked here for the caption
OFF_RANGE = [("MPPDE_final_pxmean", "Per-pixel floor", 0.0000)]

# Table 5.1 also quotes the sd over folds and the best fold
TABLE_SD = {"FEN_final_w96ftp7rk4d45skew": 0.0401, "ANISOGNN_final_dilmean": 0.0497,
            "ANISOGNN_final_oderk4n1": 0.0497, "UNET_final_w5": 0.0632,
            "FNO_final_w5k3": 0.0398, "FNO_final_w5rk4": 0.0398, "FNO_final_w5": 0.0477,
            "FEN_final_w96Frk4d45": 0.0348, "MPPDE_final_aggrmean": 0.0361,
            "MPPDE_final_k20": 0.0436, "MPPDE_final_l1mean": 0.0243}
TABLE_BEST = {"FEN_final_w96ftp7rk4d45skew": (0.6047, 2), "ANISOGNN_final_dilmean": (0.6060, 2),
              "ANISOGNN_final_oderk4n1": (0.5907, 2), "UNET_final_w5": (0.5918, 2),
              "FNO_final_w5k3": (0.5509, 2), "FNO_final_w5rk4": (0.5276, 4),
              "FNO_final_w5": (0.5391, 4), "FEN_final_w96Frk4d45": (0.5323, 2),
              "MPPDE_final_aggrmean": (0.5153, 2), "MPPDE_final_k20": (0.5223, 2),
              "MPPDE_final_l1mean": (0.4856, 2)}


def main():
    pal = setup()
    tn = thesis_numbers()

    data, checks = [], []
    print("arm                                 fold values (f0..f4)                     mean    sd")
    for exp, key, label, rk4, quoted in ROWS:
        fl = tn.fold_late(exp, FOLDS)
        assert sorted(fl) == list(FOLDS), f"{exp}: incomplete ({sorted(fl)})"
        v = np.array([fl[f] for f in FOLDS])
        m, sd = v.mean(), v.std(ddof=1)
        best_f = int(np.argmax(v))
        print(f"{label:36s}" + " ".join(f"{x:.4f}" for x in v) + f"   {m:.4f}  {sd:.4f}")
        data.append((key, label, rk4, v, m))
        checks += [(f"{label}: mean", quoted, m),
                   (f"{label}: sd", TABLE_SD[exp], sd),
                   (f"{label}: best fold", f"{TABLE_BEST[exp][0]:.4f} [{TABLE_BEST[exp][1]}]",
                    f"{v[best_f]:.4f} [{best_f}]")]
    for exp, label, quoted in OFF_RANGE:
        fl = tn.fold_late(exp, FOLDS)
        v = np.array([fl[f] for f in FOLDS])
        print(f"{label:36s}" + " ".join(f"{x:.4f}" for x in v) + "   (not plotted)")
        checks.append((f"{label}: mean (not plotted)", quoted, v.mean()))

    # spread between folds vs differences between arms (the point of the figure)
    sds = [d[3].std(ddof=1) for d in data]
    means = [d[4] for d in data]
    gaps = np.abs(np.diff(means))
    print(f"\nbetween-fold sd per arm: {min(sds):.4f} .. {max(sds):.4f}; "
          f"gaps between adjacent arm means: {gaps.min():.4f} .. {gaps.max():.4f} "
          f"(median {np.median(gaps):.4f})")
    print("best fold per arm:", {d[1]: int(np.argmax(d[3])) for d in data})

    # --- plot ---------------------------------------------------------------
    fig, ax = plt.subplots(figsize=pal.fig_size(FRAC, ASPECT))
    n = len(data)
    for i, (key, label, rk4, v, m) in enumerate(data):
        y = n - 1 - i
        c = pal.ARM[key]
        ax.plot([v.min(), v.max()], [y, y], color=pal.PAL["line"], lw=0.8, zorder=1)
        for f in FOLDS:
            ax.plot(v[f], y + FOLD_DY[f], ls="none", marker=FOLD_MARKER[f], ms=4.2,
                    mfc="white" if rk4 else c, mec=c, mew=0.9, zorder=3)
        ax.plot(m, y, ls="none", marker="|", ms=13, mew=1.4, color=pal.PAL["ink"], zorder=2)
        ax.text(0.632, y, f"{m:.3f}", ha="left", va="center", fontsize=6.5,
                color=pal.PAL["ink_2"])

    ax.set_yticks(range(n))
    ax.set_yticklabels([d[1] for d in data][::-1], fontsize=7)
    ax.tick_params(axis="y", length=0)
    ax.set_ylim(-0.6, n - 0.4)
    ax.set_xlim(0.40, 0.63)
    ax.set_xticks(np.arange(0.40, 0.631, 0.05))
    ax.set_xlabel("Change-region Dice at the one-year anchor (late-epoch mean)")
    ax.grid(axis="x", color=pal.PAL["line"], lw=0.5)
    ax.grid(axis="y", visible=False)
    ax.text(0.632, n - 0.45, "mean", ha="left", va="bottom", fontsize=6.5,
            color=pal.PAL["ink_2"])

    handles = [Line2D([], [], ls="none", marker=FOLD_MARKER[f], ms=4.2, mfc=pal.PAL["ink_2"],
                      mec=pal.PAL["ink_2"], label=f"fold {f}") for f in FOLDS]
    handles += [Line2D([], [], ls="none", marker="|", ms=9, mew=1.6, color=pal.PAL["ink"],
                       label="five-fold mean"),
                Line2D([], [], ls="none", marker="o", ms=4.2, mfc="white",
                       mec=pal.PAL["ink_2"], label="open: RK4")]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=7,
              handletextpad=0.2, columnspacing=0.9, fontsize=6.5)

    save(fig, "fig_experiments_arms_folds")

    print("\nCheck table (value in text / Table 5.1 vs value computed)")
    for name, quoted, got in checks:
        if isinstance(quoted, str):
            ok = quoted == got
            print(f"  {name:48s} {quoted:>12s} {got:>12s}  {'ok' if ok else 'MISMATCH'}")
        else:
            ok = abs(round(got, 4) - quoted) < 1e-9
            print(f"  {name:48s} {quoted:12.4f} {got:12.4f}  {'ok' if ok else 'MISMATCH'}")


if __name__ == "__main__":
    main()
