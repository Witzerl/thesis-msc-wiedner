"""Figure fig:experiments:swap (Section 5.6.1, Table tab:experiments:swap): the step-size ladder
for the dilated-stencil graph network, trained in two ways.

Each trained network (epoch 29) is re-evaluated without retraining with a fixed internal step
h = 1, 1/2, ..., 1/32 year (365 to 11.4 days), using the scheme it was trained with, folds 0-4,
seed 42. Values from the cache of images/scripts/step_ladder.py (images/data/step_ladder/*.json,
git-ignored), the same files that images/scripts/table_step_ladder.py turns into
Table tab:experiments:swap and Table tab:appendix:step-ladder.

(a) canonical network, trained with one Euler step per visit interval and Delta t as input;
(b) the same network trained with one RK4 step per interval inside the autonomous wrapper.
Both are trained with one step per interval, so every step in the plot is at least as fine
as training. The T-FEN (trained in 45-day steps) is not in this figure (author, 2026-10-21).

y = change of the change-region Dice at the one-year anchor against the trained setting.
x = the fixed internal step in days, log scale, finer to the right. One colour and marker
per fold (light to dark blue, FOLD_SEQ; markers so that folds do not rely on colour alone).
Band: run-to-run sd 0.0127. Ring: the trained setting. The 365-day step leaves 97-100 % of the
intervals in one piece and reproduces the trained Dice on folds 0-3 exactly, on fold 4 to within
0.005 (two intervals are split; asserted below).

    python fig_experiments_swap.py
"""
import json

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from _common import CACHE, FLOOR_REPLICATE, save, setup

pal = setup()
PAL, SEQ = pal.PAL, pal.SEQ

LADDER = CACHE / "step_ladder"
H = ["365", "182.5", "91.25", "45.625", "22.8125", "11.4062"]
DAYS = np.array([float(h) for h in H])
MODELS = [  # arm, panel title, trained config
    ("ANISOGNN_final_dilmean", "Trained with one Euler step", "euler:n1"),
    ("ANISOGNN_final_oderk4n1", "Trained with one RK4 step", "rk4:n1"),
]
FOLDS = {f: (pal.FOLD_SEQ[f], m) for f, m in enumerate("os^Dv")}

D = {}
for arm, _, tr in MODELS:
    sch = tr.split(":")[0]
    for fold in FOLDS:
        d = json.loads((LADDER / f"{arm}_f{fold}.json").read_text())
        c = {r["config"]: r["chg_dice"] for r in d["rows"]}
        t = c[tr]
        assert abs(t - d["info"]["chg_dice_logged_epoch"]) < 1e-9, (arm, fold)   # control
        assert abs(c[f"{sch}:d365"] - t) < 5e-3, (arm, fold)                     # ring position
        D[(arm, fold)] = np.array([c[f"{sch}:d{h}"] - t for h in H])
        print(f"{arm[:22]:22s} f{fold} {sch:5s} " + " ".join(f"{x:+.3f}" for x in D[(arm, fold)]))

fig, axes = plt.subplots(1, 2, figsize=pal.fig_size(0.85, 0.42), sharey=True,
                         gridspec_kw=dict(wspace=0.08))
for ax, lab, (arm, title, _) in zip(axes, "ab", MODELS):
    ax.axhspan(-FLOOR_REPLICATE, FLOOR_REPLICATE, color=PAL["bg_soft"], ec="none", zorder=0)
    ax.axhline(0, color=PAL["muted"], lw=0.6, zorder=1)
    for fold, (col, mk) in FOLDS.items():
        ax.plot(DAYS, D[(arm, fold)], color=col, lw=1.3, marker=mk, ms=3.6, mec=col, zorder=3)
    ax.plot([365], [0], ls="none", marker="o", ms=9, mfc="none", mec=PAL["ink"], mew=0.8, zorder=5)
    ax.set_xscale("log")
    ax.set_xlim(500, 8.5)                                   # finer steps to the right
    ax.set_xticks(DAYS, ["365", "183", "91", "46", "23", "11"])
    ax.minorticks_off()
    ax.set_title(f"({lab}) {title}", fontsize=7.5, loc="left", pad=3)
    ax.grid(axis="x", visible=False)
axes[0].set_ylabel("Change in Dice against\nthe trained setting")
axes[0].set_ylim(-0.21, 0.21)
fig.supxlabel("Internal integration step (days, log scale)", fontsize=8, y=-0.07)
axes[1].legend(handles=[Line2D([], [], color=c, marker=m, ms=3.6, lw=1.3, label=f"fold {f}")
                        for f, (c, m) in FOLDS.items()],
               loc="lower left", bbox_to_anchor=(0.02, 0.0), frameon=False, handlelength=1.8, ncol=2)
save(fig, "fig_experiments_swap")
