"""Figure for Section 5.1.4 (late-epoch mean): the operators reach their level at different epochs.

One panel: change-region Dice at the one-year anchor over the 30 training epochs, mean over the five
folds (seed 42), for two operators that learn fast (dilated-stencil GNN, FNO) and two that learn slowly
(U-Net, free-form FEN). The late-epoch window (epochs 10-29) is shaded; a marker shows the first epoch
at which each fold-mean curve comes within LEVEL_TOL of its late-epoch mean ("reaches its level").

The script also prints every number the text of Section 5.1.4 quotes, computed over all eleven arms of
Table 5.1 from the logged metrics (metrics.jsonl via the code repo's thesis_numbers module):
  - epoch-to-epoch standard deviation over epochs 10-29 (mean over folds), per arm
  - selection bias: mean over folds of (best epoch over 0-29) - (late-epoch mean)
  - epoch at which the fold-mean curve reaches its level
  - largest difference between the means over epochs 10-19 and 20-29
  - range of the stencil - U-Net difference when a single epoch of 10-29 is used

Run (from the thesis repo, MPPDE env):
    python images/scripts/fig_experiments_learning_speed.py
Output: images/fig_experiments_learning_speed.pdf (+ preview PNG in images/_preview/).
"""
import numpy as np
import matplotlib.pyplot as plt

from _common import setup, save, thesis_numbers, LATE_FROM

FRAC, ASPECT = 0.8, 0.55
N_EPOCHS = 30
LEVEL_TOL = 0.01
KEY = "change_region_dice_360d"

# all arms of Table 5.1 (per-pixel floor excluded: it is 0 at every epoch)
ARMS = [
    ("FEN_final_w96ftp7rk4d45skew", "T-FEN"),
    ("ANISOGNN_final_dilmean", "Dilated-stencil GNN"),
    ("ANISOGNN_final_oderk4n1", "Dilated-stencil GNN + RK4"),
    ("UNET_final_w5", "U-Net"),
    ("FNO_final_w5k3", "FNO + 3x3"),
    ("FNO_final_w5rk4", "FNO + RK4"),
    ("FNO_final_w5", "FNO"),
    ("FEN_final_w96Frk4d45", "FEN, free-form"),
    ("MPPDE_final_aggrmean", "k-NN GNN"),
    ("MPPDE_final_k20", "k-NN GNN, k = 20"),
    ("MPPDE_final_l1mean", "One-hop floor"),
]
# late-epoch means of Table 5.1 (05-experiments.tex), checked below
TABLE = {"FEN_final_w96ftp7rk4d45skew": 0.5428, "ANISOGNN_final_dilmean": 0.5258,
         "UNET_final_w5": 0.5046, "FNO_final_w5": 0.4831, "FEN_final_w96Frk4d45": 0.4810,
         "MPPDE_final_aggrmean": 0.4623}

# the four arms drawn: (run, palette key, label, marker)
SHOWN = [
    ("ANISOGNN_final_dilmean", "stencil", "Dilated-stencil GNN", "o"),
    ("FNO_final_w5", "fno", "FNO", "s"),
    ("UNET_final_w5", "unet", "U-Net", "D"),
    ("FEN_final_w96Frk4d45", "fen", "FEN, free-form", "^"),
]


def curves(tn, arm):
    """(5, 30) array of the per-epoch metric, folds in rows."""
    out = []
    for f in range(5):
        ep = tn.epochs(tn.run_dir(arm, f))
        assert len(ep) == N_EPOCHS and [m["epoch"] for m in ep] == list(range(N_EPOCHS)), arm
        out.append([m[KEY] for m in ep])
    return np.array(out, float)


def level_epoch(c):
    """First epoch at which the fold-mean curve comes within LEVEL_TOL of the late-epoch mean."""
    m = c.mean(0)
    late = c[:, LATE_FROM:].mean()
    return int(np.argmax(m >= late - LEVEL_TOL))


def numbers(tn):
    C = {arm: curves(tn, arm) for arm, _ in ARMS}
    for arm, v in TABLE.items():
        got = C[arm][:, LATE_FROM:].mean(1).mean()
        assert abs(got - v) < 5e-5, (arm, got, v)
    print(f"{'arm':28s} {'late':>6s} {'sd10-29':>7s} {'bias':>6s} {'level':>5s} {'halves':>6s}")
    sds, biases, halves = [], [], []
    for arm, name in ARMS:
        c = C[arm]
        late = c[:, LATE_FROM:].mean(1)
        sd = c[:, LATE_FROM:].std(1, ddof=1).mean()
        bias = (c.max(1) - late).mean()
        half = abs(c[:, 10:20].mean() - c[:, 20:30].mean())
        sds.append(sd); biases.append(bias); halves.append(half)
        print(f"{name:28s} {late.mean():6.4f} {sd:7.4f} {bias:+6.4f} {level_epoch(c):5d} {half:6.4f}")
    print(f"\nepoch-to-epoch sd (10-29, mean over folds): {min(sds):.3f} to {max(sds):.3f}")
    print(f"selection bias (best - late): {min(biases):+.3f} to {max(biases):+.3f}")
    print(f"largest |mean 10-19 - mean 20-29|: {max(halves):.3f}")
    d = (C["ANISOGNN_final_dilmean"][:, LATE_FROM:] - C["UNET_final_w5"][:, LATE_FROM:]).mean(0)
    late_d = d.mean()
    print(f"stencil - U-Net: late {late_d:+.3f}, single epochs 10-29 from {d.min():+.3f} to {d.max():+.3f}")
    return C


def main():
    pal = setup()
    tn = thesis_numbers()
    C = numbers(tn)

    fig, ax = plt.subplots(figsize=pal.fig_size(FRAC, ASPECT))
    ep = np.arange(N_EPOCHS)
    ax.axvspan(LATE_FROM - 0.5, N_EPOCHS - 0.5, color=pal.PAL["bg_soft"], zorder=0, lw=0)
    ax.text((LATE_FROM + N_EPOCHS - 1) / 2, 0.02, "averaged: epochs 10–29",
            ha="center", va="bottom", fontsize=7, color=pal.PAL["ink_2"])
    for arm, key, label, mk in SHOWN:
        c = C[arm]
        m = c.mean(0)
        col = pal.ARM[key]
        e = level_epoch(c)
        ax.plot(ep, m, color=col, lw=1.3, zorder=3, marker=mk, markevery=[e], ms=4.5,
                mec="white", mew=0.6, label=f"{label} (level at epoch {e})")
    ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.12), fontsize=7, frameon=False,
              handlelength=1.8)
    ax.set_xlim(-0.5, N_EPOCHS - 0.5)
    ax.set_ylim(0.0, 0.62)
    ax.set_xticks([0, 5, 10, 15, 20, 25, 29])
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Change-region Dice at one year\n(mean over five folds)")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.subplots_adjust(left=0.13, right=0.98, bottom=0.17, top=0.97)
    save(fig, "fig_experiments_learning_speed")


if __name__ == "__main__":
    main()
