"""Figure fig:experiments:far-atrophy (Section 5.4, differences between folds).

One message: the further from the existing lesion the new atrophy appears, the more the
dilated-stencil graph network falls behind the non-graph operators.

The 75 validation eyes are split into thirds by the share of their new atrophy at the one-year
anchor that lies more than 0.24 mm from the baseline lesion (about the reach of two
message-passing rounds of the dilated stencil). Per third: mean and standard error over the eyes
of the per-eye growth-region Dice of the dilated-stencil GNN minus the mean of T-FEN, U-Net and
FNO (late-epoch mean, seeds 42 and 7 averaged). All numbers from analysis_folds.far_terciles.
Text in the figure: axis labels only; the share ranges of the thirds are in the caption.

Include at width=0.6\\textwidth.
Run from images/scripts/:  python fig_experiments_far_atrophy.py
"""
import numpy as np
import matplotlib.pyplot as plt

from _common import setup, save
import analysis_folds as A

FRAC, ASPECT = 0.6, 0.72


def main():
    pal = setup()
    tn = A.thesis_numbers()
    eye_id = A.eye_ids(tn)
    X = {k: A.features(eye_id[k]) for k in sorted(eye_id)}
    T = A.far_terciles(tn, eye_id, X, verbose=True)

    fig, ax = plt.subplots(figsize=pal.fig_size(FRAC, ASPECT))
    ax.axhline(0, color=pal.ARM["persistence"], lw=0.9, ls=(0, (4, 2)), zorder=1)
    x = np.arange(3)
    mu = [t[0] for t in T]
    se = [t[1] for t in T]
    ax.errorbar(x, mu, yerr=se, color=pal.ARM["stencil"], lw=1.3, marker="o", ms=5,
                capsize=3, mec="white", mew=0.6, zorder=3)
    ax.set_xticks(x, ["Low", "Medium", "High"])
    ax.set_xlim(-0.4, 2.4)
    ax.set_xlabel("Share of new atrophy far from the lesion")
    ax.set_ylabel("Dilated-stencil GNN minus\nother operators")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.tight_layout()
    save(fig, "fig_experiments_far_atrophy")


if __name__ == "__main__":
    main()
