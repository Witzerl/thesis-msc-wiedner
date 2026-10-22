"""Figure fig:experiments:swap-tfen (Section 5.6.1, Table tab:experiments:swap): the step-size ladder
for the T-FEN in its energy-conserving form.

The network (FEN_final_w96ftp7rk4d45skew, epoch 29, folds 0-4, seed 42) was trained with RK4 in steps
of 45 days and is re-evaluated without retraining with RK4 at a fixed internal step of 365 to 11.4 days.
Values from the cache of images/scripts/step_ladder.py (images/data/step_ladder/*.json, git-ignored),
the same files as Fig. fig:experiments:swap and the two step-ladder tables.

y = change of the change-region Dice at the one-year anchor against the trained setting (ring at the
45.6-day step, which splits every interval like the 45-day training step; asserted below).
Shaded: steps coarser than training, which C2 does not cover. One shade + marker per fold
(palette FOLD_TFEN). Band: run-to-run sd 0.0127.

    python fig_experiments_swap_tfen.py
"""
import json

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from _common import CACHE, FLOOR_REPLICATE, save, setup

pal = setup()
PAL = pal.PAL

ARM_ID = "FEN_final_w96ftp7rk4d45skew"
H = ["365", "182.5", "91.25", "45.625", "22.8125", "11.4062"]
DAYS = np.array([float(h) for h in H])
TRAINED = 45.625
FOLDS = {f: (pal.FOLD_TFEN[f], m) for f, m in enumerate("os^Dv")}

D = {}
for fold in FOLDS:
    d = json.loads((CACHE / "step_ladder" / f"{ARM_ID}_f{fold}.json").read_text())
    c = {r["config"]: r["chg_dice"] for r in d["rows"]}
    t = c["rk4:d45"]
    assert abs(t - d["info"]["chg_dice_logged_epoch"]) < 1e-9, fold        # control
    assert abs(c["rk4:d45.625"] - t) < 5e-5, fold                          # ring position
    D[fold] = np.array([c[f"rk4:d{h}"] - t for h in H])
    print(f"fold {fold}: " + " ".join(f"{x:+.3f}" for x in D[fold]))

fig, ax = plt.subplots(figsize=pal.fig_size(0.55, 0.72))
ax.axvspan(500, TRAINED, color=PAL["line"], alpha=0.35, lw=0, zorder=0)   # coarser than training
ax.axhspan(-FLOOR_REPLICATE, FLOOR_REPLICATE, color=PAL["bg_soft"], ec="none", zorder=0)
ax.axhline(0, color=PAL["muted"], lw=0.6, zorder=1)
for fold, (col, mk) in FOLDS.items():
    ax.plot(DAYS, D[fold], color=col, lw=1.3, marker=mk, ms=3.6, mec=col, zorder=3)
ax.plot([TRAINED], [0], ls="none", marker="o", ms=9, mfc="none", mec=PAL["ink"], mew=0.8, zorder=5)
ax.set_xscale("log")
ax.set_xlim(500, 8.5)                                                      # finer steps to the right
ax.set_xticks(DAYS, ["365", "183", "91", "46", "23", "11"])
ax.minorticks_off()
ax.grid(axis="x", visible=False)
ax.set_ylim(-0.21, 0.21)
ax.set_ylabel("Change in Dice against\nthe trained setting")
ax.set_xlabel("Internal integration step\n(days, log scale)")
ax.legend(handles=[Line2D([], [], color=c, marker=m, ms=3.6, lw=1.3, label=f"fold {f}")
                   for f, (c, m) in FOLDS.items()],
          loc="upper right", frameon=False, handlelength=1.8)
save(fig, "fig_experiments_swap_tfen")
