"""Figure fig:experiments:arms-folds (Section 5.2, next to Table tab:experiments:arms).

One message: the folds move every operator up or down together, and that common shift is larger
than the differences between operators; this is why every comparison is taken fold by fold.

Two panels (2026-10-22, author: both seeds): seed 42 (left) and seed 7 (right); x = fold (0-4),
y = late-epoch mean change-region Dice@360d of that fold (epochs 10-29), one line per operator for the five main operators of Table 5.1 (dilated-stencil
GNN, U-Net, T-FEN, FNO, k-NN GNN) in their thesis colours. Text in the figure is limited to the
axis labels and a legend with the operator names; everything else is in the caption. The script
checks every plotted fold value against thesis_numbers.fold_late and the five-fold means against
Table 5.1, and prints the numbers the caption and text may quote (spread between folds vs spread
between operators).

Include at width=\\textwidth.
Run from images/scripts/:  python fig_experiments_arms_folds.py
"""
import numpy as np
import matplotlib.pyplot as plt

from _common import setup, save, thesis_numbers

FRAC, ASPECT = 1.0, 0.42
FOLDS = list(range(5))

# (experiment, palette key, legend label, five-fold mean quoted in Table 5.1)
ARMS = [
    ("FEN_final_w96ftp7rk4d45skew", "tfen", "T-FEN", 0.5428),
    ("ANISOGNN_final_dilmean", "stencil", "Dilated-stencil GNN", 0.5258),
    ("UNET_final_w5", "unet", "U-Net", 0.5046),
    ("FNO_final_w5", "fno", "FNO", 0.4831),
    ("MPPDE_final_aggrmean", "knn", "k-NN GNN", 0.4623),
]
SEED7 = {"FEN_final_w96ftp7rk4d45skew": "FEN_final_w96ftp7rk4d45skews7",
         "ANISOGNN_final_dilmean": "ANISOGNN_final_dilmeans7",
         "UNET_final_w5": "UNET_final_w5s7", "FNO_final_w5": "FNO_final_w5s7",
         "MPPDE_final_aggrmean": "MPPDE_final_aggrmeans7"}
MARKER = {"tfen": "^", "stencil": "o", "unet": "D", "fno": "s", "knn": "v"}


def main():
    pal = setup()
    tn = thesis_numbers()
    V = {}
    for exp, key, lab, quoted in ARMS:
        fl = tn.fold_late(exp, FOLDS)
        v = np.array([fl[f] for f in FOLDS])
        assert abs(v.mean() - quoted) < 5e-5, (exp, v.mean(), quoted)
        V[exp] = v
        print(f"{lab:22s} " + " ".join(f"{x:.4f}" for x in v) + f" | mean {v.mean():.4f}")

    M = np.array([V[e] for e, *_ in ARMS])            # arms x folds
    fold_mean = M.mean(0)
    print("\nmean over the five operators per fold: " + " ".join(f"{x:.3f}" for x in fold_mean))
    print(f"spread between folds (max - min of these): {fold_mean.max() - fold_mean.min():.3f}")
    arm_mean = M.mean(1)
    print(f"spread between operators (max - min of five-fold means): "
          f"{arm_mean.max() - arm_mean.min():.3f}")
    hi = M.argmax(1)
    lo = M.argmin(1)
    print("highest fold per operator: " + ", ".join(f"{a[2]} {h}" for a, h in zip(ARMS, hi)))
    print("lowest fold per operator:  " + ", ".join(f"{a[2]} {l}" for a, l in zip(ARMS, lo)))

    V7 = {}
    for exp, key, lab, _ in ARMS:
        fl = tn.fold_late(SEED7[exp], FOLDS)
        V7[exp] = np.array([fl[f] for f in FOLDS])
        print(f"seed 7 {lab:15s} " + " ".join(f"{x:.4f}" for x in V7[exp])
              + f" | mean {V7[exp].mean():.4f} | highest fold {V7[exp].argmax()}")

    fig, axes = plt.subplots(1, 2, figsize=pal.fig_size(FRAC, ASPECT), sharey=True)
    for ax, VV, title in ((axes[0], V, "Seed 42"), (axes[1], V7, "Seed 7")):
        for exp, key, lab, _ in ARMS:
            ax.plot(FOLDS, VV[exp], color=pal.ARM[key], lw=1.3, marker=MARKER[key], ms=4.5,
                    mec="white", mew=0.6, label=lab, zorder=3)
        ax.set_xticks(FOLDS, [str(f) for f in FOLDS])
        ax.set_xlim(-0.3, 4.3)
        ax.set_xlabel("Fold")
        ax.set_title(title, fontsize=8)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
    axes[0].set_ylabel("Change-region Dice at one year")
    axes[1].legend(loc="upper left", bbox_to_anchor=(1.0, 1.0), fontsize=7, frameon=False,
                   handlelength=1.8)
    fig.tight_layout()
    save(fig, "fig_experiments_arms_folds")


if __name__ == "__main__":
    main()
