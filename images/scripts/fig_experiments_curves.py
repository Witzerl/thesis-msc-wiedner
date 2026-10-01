"""Figure fig:experiments:curves (Section 5.1.3 late-epoch mean; Section 5.4.2 objective).

(a) Canonical dilated-stencil graph network (ANISOGNN_final_dilmean, seed 42): change-region
    Dice at the one-year anchor after every epoch, one line per fold; the late-epoch window
    (epochs 10-29) shaded; each fold's late-epoch mean as a horizontal segment over the window,
    ended by the fold's marker (same fold shapes as fig_experiments_arms_folds); thin vertical
    lines where the learning rate is multiplied by 0.4. The schedule is read from args.json
    (lr_milestones, lr_decay) of the run: torch MultiStepLR stepped at the end of every
    0-based epoch, so a milestone m means that epoch m is the first one trained at the
    reduced rate; the line is drawn between epochs m-1 and m.
(b) Objective ablation on the same network: mean over the five folds (line) and min-max over
    folds (band) for the full objective, without the soft-Dice term (_nodice), and with plain
    unweighted MSE (_plainmse, flat at 0). The epoch at which each fold of the _nodice run
    first predicts change (Dice > 0) is marked with the fold's marker.

Include at width=1.0\\textwidth.
Run from images/scripts/:  python fig_experiments_curves.py
"""
import json
import os

import numpy as np
import matplotlib.pyplot as plt

from _common import setup, save, thesis_numbers, panel_label, LATE_FROM

FRAC, ASPECT = 1.0, 0.42
FOLDS = list(range(5))
N_EPOCHS = 30
FOLD_MARKER = {0: "o", 1: "s", 2: "^", 3: "D", 4: "v"}   # as in fig_experiments_arms_folds

FULL = "ANISOGNN_final_dilmean"
NODICE = "ANISOGNN_final_dilmean_nodice"
PLAIN = "ANISOGNN_final_dilmean_plainmse"

# values quoted in 05-experiments.tex (Section 5.4.2) and 04-method.tex (Section 4.5)
QUOTED = dict(
    canonical_mean=0.5258,
    nodice_mean=0.4762, nodice_sd=0.0631,
    nodice_escape=[2, 8, 3, 7, 12], full_escape=[0, 0, 0, 0, 0],
    late_sd_nodice=0.043, late_sd_full=0.015,
    raw_rmse_full=1.10, raw_rmse_nodice=0.51,
    plain_identical="74/75",
    lr_milestones=[5, 20], lr_decay=0.4,
)


def curves(tn, arm, key="change_region_dice_360d"):
    """(5, 30) array of the per-epoch metric, folds in rows."""
    out = []
    for f in FOLDS:
        ep = tn.epochs(tn.run_dir(arm, f))
        assert len(ep) == N_EPOCHS and [m["epoch"] for m in ep] == list(range(N_EPOCHS)), arm
        out.append([m[key] for m in ep])
    return np.array(out, float)


def main():
    pal = setup()
    tn = thesis_numbers()
    checks = []
    ep = np.arange(N_EPOCHS)

    a = json.load(open(os.path.join(tn.run_dir(FULL, 0), "args.json")))
    milestones, decay = a["lr_milestones"], a["lr_decay"]
    for f in FOLDS:     # every fold of the three runs uses the same schedule
        for arm in (FULL, NODICE, PLAIN):
            b = json.load(open(os.path.join(tn.run_dir(arm, f), "args.json")))
            assert (b["lr_milestones"], b["lr_decay"], b["lr"]) == (milestones, decay, a["lr"]), (arm, f)
    print(f"learning rate {a['lr']} x {decay} at milestones {milestones} (MultiStepLR, stepped "
          f"after every 0-based epoch): epochs 0-{milestones[0] - 1} at {a['lr']:g}, "
          f"{milestones[0]}-{milestones[1] - 1} at {a['lr'] * decay:g}, "
          f"{milestones[1]}-{N_EPOCHS - 1} at {a['lr'] * decay ** 2:g}")
    checks += [("lr milestones (args.json)", str(QUOTED["lr_milestones"]), str(milestones)),
               ("lr decay factor", f"{QUOTED['lr_decay']}", f"{decay}")]

    D = {arm: curves(tn, arm) for arm in (FULL, NODICE, PLAIN)}
    late = {arm: D[arm][:, LATE_FROM:].mean(1) for arm in D}
    for arm in D:
        print(f"\n{arm}")
        for f in FOLDS:
            print(f"  f{f}: " + " ".join(f"{x:.3f}" for x in D[arm][f]) +
                  f" | late {late[arm][f]:.4f}, late sd {D[arm][f, LATE_FROM:].std(ddof=1):.4f}")
        print(f"  five-fold mean {late[arm].mean():.4f} +/- {late[arm].std(ddof=1):.4f} (sd over folds)")

    # cross-check against thesis_numbers.fold_late
    fl = tn.fold_late(FULL, FOLDS)
    assert np.allclose([fl[f] for f in FOLDS], late[FULL])
    checks.append(("canonical five-fold late mean", f"{QUOTED['canonical_mean']:.4f}",
                   f"{late[FULL].mean():.4f}"))
    checks += [("nodice five-fold late mean", f"{QUOTED['nodice_mean']:.4f}", f"{late[NODICE].mean():.4f}"),
               ("nodice sd over folds", f"{QUOTED['nodice_sd']:.4f}", f"{late[NODICE].std(ddof=1):.4f}")]

    def escape(arm):
        return [int(np.flatnonzero(D[arm][f] > 0)[0]) if (D[arm][f] > 0).any() else None
                for f in FOLDS]
    esc_nd, esc_full = escape(NODICE), escape(FULL)
    checks += [("nodice: first epoch with Dice > 0, folds 0-4", str(QUOTED["nodice_escape"]), str(esc_nd)),
               ("full: first epoch with Dice > 0", str(QUOTED["full_escape"]), str(esc_full)),
               ("plainmse: Dice = 0 at every epoch and fold", "True", str(bool((D[PLAIN] == 0).all())))]

    sd_full = D[FULL][:, LATE_FROM:].std(1, ddof=1)
    sd_nd = D[NODICE][:, LATE_FROM:].std(1, ddof=1)
    print(f"\nlate epoch-to-epoch sd per fold, full:   " + " ".join(f"{x:.4f}" for x in sd_full)
          + f"  mean {sd_full.mean():.4f}")
    print(f"late epoch-to-epoch sd per fold, nodice: " + " ".join(f"{x:.4f}" for x in sd_nd)
          + f"  mean {sd_nd.mean():.4f}")
    print(f"  without fold 4: full {sd_full[:4].mean():.4f}, nodice {sd_nd[:4].mean():.4f} "
          f"(fold 4 of nodice escapes only at epoch {esc_nd[4]}, inside the late window)")
    checks += [("late sd, full (mean of per-fold sd)", f"{QUOTED['late_sd_full']:.3f}", f"{sd_full.mean():.3f}"),
               ("late sd, nodice (mean of per-fold sd)", f"{QUOTED['late_sd_nodice']:.3f}", f"{sd_nd.mean():.3f}")]

    rm_full = curves(tn, FULL, "rollout_mask_rmse")[:, LATE_FROM:].mean()
    rm_nd = curves(tn, NODICE, "rollout_mask_rmse")[:, LATE_FROM:].mean()
    checks += [("raw rollout mask RMSE, full (late mean)", f"{QUOTED['raw_rmse_full']:.2f}", f"{rm_full:.2f}"),
               ("raw rollout mask RMSE, nodice (late mean)", f"{QUOTED['raw_rmse_nodice']:.2f}", f"{rm_nd:.2f}")]

    ident = curves(tn, PLAIN, "n_identical_to_bootstrap")[:, -1].astype(int)
    nseq = curves(tn, PLAIN, "n_sequences_evaluated")[:, -1].astype(int)
    print(f"plainmse identical to baseline at epoch 29: {'/'.join(map(str, ident))} "
          f"of {'/'.join(map(str, nseq))}")
    checks.append(("plainmse: eyes identical to baseline at epoch 29",
                   QUOTED["plain_identical"], f"{ident.sum()}/{nseq.sum()}"))

    # --- plot ---------------------------------------------------------------
    blue, orange, ink2 = pal.ARM["stencil"], pal.PAL["accent"], pal.PAL["ink_2"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=pal.fig_size(FRAC, ASPECT), sharey=True)
    for ax in (ax1, ax2):
        ax.axvspan(LATE_FROM - 0.5, N_EPOCHS - 0.5, color=pal.PAL["primary_tint"], lw=0, zorder=0)
        for m in milestones:
            ax.axvline(m - 0.5, color=pal.PAL["muted"], lw=0.7, ls=(0, (2, 2)), zorder=1)
        ax.set_xlim(-0.8, N_EPOCHS + 1.6)
        ax.set_xticks([0, 5, 10, 15, 20, 25, 29])
        ax.set_xlabel("Epoch")
        ax.set_ylim(-0.02, 0.71)
        ax.text(LATE_FROM - 0.1, 0.70, "late-epoch window", ha="left", va="top",
                fontsize=6.3, color=ink2)
    for m in milestones:
        ax1.text(m - 0.2, 0.01, f"lr × {decay:g}", ha="left", va="bottom", fontsize=6.3,
                 color=ink2)
    ax1.set_ylabel("Change-region Dice at one year")

    # (a) five folds of the canonical run
    for f in FOLDS:
        ax1.plot(ep, D[FULL][f], color=blue, lw=0.8, alpha=0.75, zorder=2)
        ax1.plot([LATE_FROM - 0.5, N_EPOCHS - 0.5], [late[FULL][f]] * 2,
                 color=pal.PAL["secondary"], lw=1.0, zorder=3)
    # fold markers at the end of the late-mean segments, staggered where values are close
    order = np.argsort(late[FULL])
    xs = {f: N_EPOCHS + 0.1 for f in FOLDS}
    for i in range(1, len(order)):
        lo, hi = order[i - 1], order[i]
        if late[FULL][hi] - late[FULL][lo] < 0.016 and xs[lo] < N_EPOCHS + 0.6:
            xs[hi] = xs[lo] + 0.9
    for f in FOLDS:
        ax1.plot(xs[f], late[FULL][f], ls="none", marker=FOLD_MARKER[f], ms=3.8,
                 color=pal.PAL["secondary"], zorder=4, clip_on=False)
    panel_label(ax1, "(a)")

    # (b) objective ablation: mean over folds and min-max band
    series = [(FULL, blue, "-", "full objective"),
              (NODICE, orange, "-", "without soft-Dice"),
              (PLAIN, ink2, "--", "plain MSE")]
    for arm, c, ls, lab in series:
        y = D[arm]
        if arm != PLAIN:
            ax2.fill_between(ep, y.min(0), y.max(0), color=c, alpha=0.15, lw=0, zorder=2)
        ax2.plot(ep, y.mean(0), color=c, lw=1.3, ls=ls, zorder=3)
    for f in FOLDS:
        e = esc_nd[f]
        ax2.plot(e, D[NODICE][f, e], ls="none", marker=FOLD_MARKER[f], ms=3.8, color=orange,
                 mec="white", mew=0.5, zorder=4)
    lab = dict(fontsize=6.5, ha="left", va="center")
    ax2.text(N_EPOCHS - 0.3, D[FULL].mean(0)[-1] + 0.035, "full objective", color=blue, **lab)
    ax2.text(N_EPOCHS - 0.3, D[NODICE].mean(0)[-1] - 0.04, "without\nsoft-Dice", color=orange,
             linespacing=1.0, **lab)
    ax2.text(N_EPOCHS - 0.3, 0.03, "plain\nMSE", color=ink2, linespacing=1.0, **lab)
    ax2.text(12.6, 0.31, "first epoch with\npredicted change\n(one marker per fold)",
             fontsize=6.3, color=ink2, ha="left", va="center", linespacing=1.0)
    panel_label(ax2, "(b)")

    fig.tight_layout(w_pad=1.2)
    save(fig, "fig_experiments_curves")

    print("\nCheck table (value in text vs value computed)")
    for nm, q, g in checks:
        print(f"  {nm:52s} {q:>18s} {g:>18s}  {'ok' if q == g else 'MISMATCH'}")


if __name__ == "__main__":
    main()
