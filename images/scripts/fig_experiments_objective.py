"""Figure for Section 5.4.2: what the training objective has to contain.

Canonical dilated-stencil graph network, seed 42, three objectives, change-region Dice at the
one-year anchor after every epoch, one line per objective (mean over the five folds):
  - full objective (mask-weighted MSE + soft-Dice)       ANISOGNN_final_dilmean
  - without the soft-Dice term (mask weighting kept)     ANISOGNN_final_dilmean_nodice
  - plain unweighted MSE (no weighting, no soft-Dice)    ANISOGNN_final_dilmean_plainmse
The plain-MSE run predicts no change on any fold at any epoch (Dice 0 = persistence) and is
drawn as a dashed line at 0. A dot sits on the line without soft-Dice at each epoch at which one
of its folds first predicts change (the steps of that line). All explanation is in the caption.

The script also checks every other number Section 5.4.2 quotes for these runs (taken over from the
retired fig_experiments_curves.py): late epoch-to-epoch sd, raw rollout mask RMSE, and the number
of eyes whose plain-MSE prediction equals the baseline mask at the last epoch.

Include at width=0.8\\textwidth.
Run from images/scripts/:  python fig_experiments_objective.py
"""
import numpy as np
import matplotlib.pyplot as plt

from _common import setup, save, thesis_numbers, LATE_FROM

FRAC, ASPECT = 0.8, 0.55
FOLDS = list(range(5))
N_EPOCHS = 30
FULL = "ANISOGNN_final_dilmean"
NODICE = "ANISOGNN_final_dilmean_nodice"
PLAIN = "ANISOGNN_final_dilmean_plainmse"
QUOTED = dict(full=0.5258, nodice=0.4762, escape=[2, 8, 3, 7, 12],
              late_sd_nodice=0.043, late_sd_full=0.015,
              late_sd_nodice_f03=0.017, late_sd_full_f03=0.013,
              raw_rmse_full=1.10, raw_rmse_nodice=0.51, plain_identical="74/75")


def curves(tn, arm, key="change_region_dice_360d"):
    out = []
    for f in FOLDS:
        ep = tn.epochs(tn.run_dir(arm, f))
        assert [m["epoch"] for m in ep] == list(range(N_EPOCHS)), (arm, f)
        out.append([m[key] for m in ep])
    return np.array(out, float)


def main():
    pal = setup()
    tn = thesis_numbers()
    D = {a: curves(tn, a) for a in (FULL, NODICE, PLAIN)}
    late = {a: D[a][:, LATE_FROM:].mean(1).mean() for a in D}
    esc = [int(np.flatnonzero(D[NODICE][f] > 0)[0]) for f in FOLDS]
    assert (D[PLAIN] == 0).all()
    assert esc == QUOTED["escape"], esc
    print(f"late means: full {late[FULL]:.4f} (text {QUOTED['full']}), "
          f"nodice {late[NODICE]:.4f} (text {QUOTED['nodice']}), plain {late[PLAIN]:.4f}")
    print(f"first epoch with change, nodice: {esc}")

    checks = []
    sd_full = D[FULL][:, LATE_FROM:].std(1, ddof=1)
    sd_nd = D[NODICE][:, LATE_FROM:].std(1, ddof=1)
    checks += [("late sd, full", f"{QUOTED['late_sd_full']:.3f}", f"{sd_full.mean():.3f}"),
               ("late sd, nodice", f"{QUOTED['late_sd_nodice']:.3f}", f"{sd_nd.mean():.3f}"),
               ("late sd, full, folds 0-3", f"{QUOTED['late_sd_full_f03']:.3f}",
                f"{sd_full[:4].mean():.3f}"),
               ("late sd, nodice, folds 0-3", f"{QUOTED['late_sd_nodice_f03']:.3f}",
                f"{sd_nd[:4].mean():.3f}")]
    rm_full = curves(tn, FULL, "rollout_mask_rmse")[:, LATE_FROM:].mean()
    rm_nd = curves(tn, NODICE, "rollout_mask_rmse")[:, LATE_FROM:].mean()
    checks += [("raw mask RMSE, full", f"{QUOTED['raw_rmse_full']:.2f}", f"{rm_full:.2f}"),
               ("raw mask RMSE, nodice", f"{QUOTED['raw_rmse_nodice']:.2f}", f"{rm_nd:.2f}")]
    ident = curves(tn, PLAIN, "n_identical_to_bootstrap")[:, -1].astype(int)
    nseq = curves(tn, PLAIN, "n_sequences_evaluated")[:, -1].astype(int)
    checks.append(("plain MSE: eyes identical to baseline, epoch 29", QUOTED["plain_identical"],
                   f"{ident.sum()}/{nseq.sum()}"))
    for nm, q, g in checks:
        print(f"  {nm:48s} text {q:>6s}  computed {g:>6s}  {'ok' if q == g else 'MISMATCH'}")

    # one panel, one line per objective (mean over the five folds), styled like
    # fig_experiments_learning_speed. All three runs are the dilated-stencil GNN, so colour
    # separates the objective, not the arm: stencil blue = full objective (the canonical run),
    # petrol dashed = without soft-Dice, grey dashed at 0 = plain MSE (= persistence).
    blue, petrol, grey = pal.ARM["stencil"], pal.PAL["secondary"], pal.ARM["persistence"]
    ep = np.arange(N_EPOCHS)
    fig, ax = plt.subplots(figsize=pal.fig_size(FRAC, ASPECT))
    ax.axvspan(LATE_FROM - 0.5, N_EPOCHS - 0.5, color=pal.PAL["bg_soft"], zorder=0, lw=0)
    ax.plot(ep, D[FULL].mean(0), color=blue, lw=1.3, zorder=3,
            label="Full objective")
    ax.plot(ep, D[NODICE].mean(0), color=petrol, lw=1.3, ls=(0, (5, 2)), zorder=3,
            marker="o", markevery=sorted(esc), ms=3.5, mec="white", mew=0.5,
            label="Without soft-Dice")
    ax.plot(ep, D[PLAIN].mean(0), color=grey, lw=1.3, ls=(0, (2, 2)), zorder=2,
            label="Plain MSE")
    ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.12), fontsize=7, frameon=False,
              handlelength=2.2)
    ax.set_xlim(-0.5, N_EPOCHS - 0.5)
    ax.set_ylim(-0.01, 0.62)
    ax.set_xticks([0, 5, 10, 15, 20, 25, 29])
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Change-region Dice at one year\n(mean over five folds)")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.subplots_adjust(left=0.13, right=0.98, bottom=0.17, top=0.97)
    save(fig, "fig_experiments_objective")


if __name__ == "__main__":
    main()
