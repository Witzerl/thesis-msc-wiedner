"""Figure fig:experiments:swap (Section 5.5.1, Table tab:experiments:swap): the solver-swap
test, drawn as the change in change-region Dice against the integration step.

The trained weights are re-evaluated, without retraining, with another integration scheme
or step (masterthesis-docker GraphPDE/demos & explanations/solver_swap.py). No output files
of those evaluations are stored, so the values are read from their written record,
SOLVER_FINAL_RUNS.md section 9.17 (graph networks, fold 2, seed 42; six decimals) and
section 9.19b (T-FEN in the energy-conserving form, fold 0, seed 42; four decimals), and are
cross-checked against Table tab:experiments:swap in 05-experiments.tex.

x = integration step relative to the training step: Euler or RK4 with n sub-steps over the
interval -> 1/n (training: one step over the interval); T-FEN RK4 at 90 / 45 / 30 / 22.5 /
15 days against its 45-day training step -> 2, 1, 2/3, 1/2, 1/3. Log2 axis, finer steps to
the right.

    python fig_experiments_swap.py
"""
import re

import matplotlib.pyplot as plt
import numpy as np

from _common import DEMOS, FLOOR_REPLICATE, THESIS, panel_label, save, setup

pal = setup()
ARM, PAL = pal.ARM, pal.PAL

md = (DEMOS / "SOLVER_FINAL_RUNS.md").read_text(encoding="utf-8")


def section(head):
    """Text of the section whose header line starts with `head`, up to the next header."""
    i = md.index(head)
    m = re.search(r"\n#{3,4} ", md[i + len(head):])
    return md[i:i + len(head) + (m.start() if m else len(md))]


s917 = section("### 9.17 ")
s919b = section("#### 9.19b ")
ROW_GNN = re.compile(r"^\|\s*\**(euler|rk4) / (\d)( \(= trained\))?\**\s*\|\s*\**([0-9.]+)\**\s*\|",
                     re.M)
ROW_FEN = re.compile(r"^\|\s*\**([0-9.]+) d( \(as trained\))?\**\s*\|\s*\**([0-9.]+)\**\s*\|", re.M)


def gnn_rows(text):
    """{(scheme, n): (dice, trained?)} from one of the 9.17 tables."""
    return {(m[1], int(m[2])): (float(m[4]), bool(m[3])) for m in ROW_GNN.finditer(text)}


a1 = s917.index("**Arm 1")
a2 = s917.index("**Arm 2")
canon = gnn_rows(s917[a1:a2])
rkarm = gnn_rows(s917[a2:])
tfen = {float(m[1]): (float(m[3]), bool(m[2])) for m in ROW_FEN.finditer(s919b)}
assert set(canon) == {("euler", 1), ("euler", 2), ("euler", 4), ("rk4", 1), ("rk4", 2)}, canon
assert set(rkarm) == {(s, k) for s in ("euler", "rk4") for k in (1, 2, 4)}, rkarm
assert set(tfen) == {90.0, 45.0, 30.0, 22.5, 15.0}, tfen

MODELS = [  # name, colour, trained setting, {(scheme, rel. step): dice}
    ("canon", "Canonical network", ARM["stencil"], ("euler", 1.0),
     {(s, 1 / k): v for (s, k), (v, _) in canon.items()}),
    ("rkarm", "Network trained in the RK4 wrapper", ARM["stencil"], ("rk4", 1.0),
     {(s, 1 / k): v for (s, k), (v, _) in rkarm.items()}),
    ("tfen", "T-FEN, energy-conserving", ARM["tfen"], ("rk4", 1.0),
     {("rk4", d / 45.0): v for d, (v, _) in tfen.items()}),
]
assert canon[("euler", 1)][1] and rkarm[("rk4", 1)][1] and tfen[45.0][1]  # trained rows marked

# ---------------------------------------------------------------- values and checks
tex = (THESIS / "05-experiments.tex").read_text(encoding="utf-8")
tab = tex[tex.index(r"\label{tab:experiments:swap}"):]
tab = tab[:tab.index(r"\end{tabular}")]
TEXROW = re.compile(r"^\s*(Euler|RK4), (\d+(?:\.\d+)?)[- ](steps?|day steps)( \(trained\))? & ([0-9.]+) & \$([+-][0-9.]+)\$",
                    re.M)
blocks = re.split(r"\\multicolumn", tab)[1:]
assert len(blocks) == 3
texvals = []
for b in blocks:
    rows = {}
    for m in TEXROW.finditer(b):
        scheme = m[1].lower()
        rel = (1 / int(m[2])) if m[3].startswith("step") else float(m[2]) / 45.0
        rows[(scheme, round(rel, 6))] = (float(m[5]), float(m[6]))
    texvals.append(rows)

print("check: Table tab:experiments:swap (text) vs SOLVER_FINAL_RUNS.md records")
bad = 0
D = {}
for (key, name, col, trained, vals), tv in zip(MODELS, texvals):
    ref = vals[trained]
    D[key] = {}
    print(f"  {name} (trained: {trained[0]}, step 1)")
    for (sch, rel), v in sorted(vals.items(), key=lambda kv: (kv[0][0], -kv[0][1])):
        d = v - ref
        D[key][(sch, rel)] = d
        t = tv.get((sch, round(rel, 6)))
        ok = t is not None and round(v, 4) == t[0] and f"{d:+.4f}" == f"{t[1]:+.4f}"
        bad += not ok
        print(f"    {sch:5s} rel. step {rel:6.4f}: Dice {v:.6f} (text {t[0] if t else '-'}), "
              f"delta {d:+.4f} (text {t[1]:+.4f})  {'ok' if ok else 'MISMATCH'}" if t else
              f"    {sch:5s} rel. step {rel:6.4f}: Dice {v:.6f} -- not in the text table  MISMATCH")
    assert len(tv) == len(vals), (name, len(tv), len(vals))
c = {k: v for k, v in MODELS[0][4].items()}
spread_c = max(c.values()) - min(c.values())
r = MODELS[1][4]
refined = [v for k, v in r.items() if k != ("euler", 1.0)]
rk_only = [v for (s, _), v in r.items() if s == "rk4"]
f_ok = [v for (s, rel), v in MODELS[2][4].items() if rel <= 1.0]
print("  derived quantities quoted in the text:")
for label, t, val in [
    ("canonical Euler 1->2", -0.016, c[("euler", 0.5)] - c[("euler", 1.0)]),
    ("canonical Euler 2->4", -0.060, c[("euler", 0.25)] - c[("euler", 0.5)]),
    ("canonical spread of five settings", 0.086, spread_c),
    ("RK4-arm Euler 1->2", 0.018, r[("euler", 0.5)] - r[("euler", 1.0)]),
    ("RK4-arm Euler 2->4", 0.004, r[("euler", 0.25)] - r[("euler", 0.5)]),
    ("RK4-arm spread except Euler/1", 0.0044, max(refined) - min(refined)),
    ("RK4-arm spread of RK4 settings", 0.0005, max(rk_only) - min(rk_only)),
    ("T-FEN spread at <= training step", 0.0003, max(f_ok) - min(f_ok)),
    ("T-FEN 90-day departure", -0.0015, D["tfen"][("rk4", 2.0)]),
]:
    dp = len(str(t).split(".")[1])
    ok = round(val, dp) == t
    bad += not ok
    print(f"    {label:34s} text {t:+.{dp}f}  computed {val:+.6f}  {'ok' if ok else 'MISMATCH'}")
print(f"  spread / run-to-run sd {FLOOR_REPLICATE}: canonical {spread_c / FLOOR_REPLICATE:.2f}x "
      f"(text: 'almost seven times')")
print(f"  {'all values match' if not bad else f'{bad} MISMATCHES'}")

# ---------------------------------------------------------------- figure
fig, axes = plt.subplots(1, 3, figsize=pal.fig_size(1.122, 0.321), sharey=True,
                         gridspec_kw=dict(wspace=0.10))
HEAD = ["Canonical network\nfails C1 and C2", "RK4-trained network\npasses C1 and C2",
        "T-FEN, energy-conserving\npasses C1 and C2"]
STY = {"euler": dict(ls="-", marker="o", ms=3.6, label="Euler"),
       "rk4": dict(ls=":", marker="s", ms=3.4, label="RK4")}
XT = {1: "1", 2 / 3: "2/3", 1 / 2: "1/2", 1 / 3: "1/3", 1 / 4: "1/4", 2: "2"}
for ax, (key, name, col, trained, vals), head in zip(axes, MODELS, HEAD):
    ax.axhspan(-FLOOR_REPLICATE, FLOOR_REPLICATE, color=PAL["bg_soft"], ec=PAL["line"], lw=0.5,
               zorder=0)
    ax.axhline(0, color=PAL["muted"], lw=0.6, zorder=1)
    for sch in ("euler", "rk4"):
        pts = sorted(((rel, D[key][(s, rel)]) for (s, rel) in D[key] if s == sch), reverse=True)
        if not pts:
            continue
        xs, ys = zip(*pts)
        st = STY[sch]
        ax.plot(np.log2(xs), ys, color=col, ls=st["ls"], lw=1.2, marker=st["marker"], ms=st["ms"],
                mfc=col if sch == "euler" else "white", mec=col, mew=0.9, zorder=3,
                label=st["label"])
    ax.plot([np.log2(trained[1])], [0], ls="none", marker="o", ms=8.5, mfc="none",
            mec=PAL["ink"], mew=0.8, zorder=4)
    ax.text(0.16, 0.0035, "trained", fontsize=6.5, color=PAL["ink"], ha="right", va="bottom")
    ticks = sorted({rel for (_, rel) in D[key]} | {1.0}, reverse=True)
    # 2/3 (the 30-day T-FEN step) gets a tick but no label: it would collide with 1/2
    ax.set_xticks(np.log2(ticks), ["" if abs(t - 2 / 3) < 1e-9 else
                                   XT[min(XT, key=lambda q: abs(q - t))] for t in ticks])
    ax.set_xlim(np.log2(2.6), np.log2(0.21))           # finer steps to the right
    ax.set_title(head, fontsize=7.5, loc="left", pad=3)
    ax.grid(axis="x", visible=False)
axes[0].set_ylabel(r"$\Delta$ change-region Dice" "\nvs. training setting")
axes[0].set_ylim(-0.085, 0.024)
axes[1].set_xlabel("Integration step relative to the training step (log scale, finer to the right)")
axes[2].text(np.log2(2.45), -FLOOR_REPLICATE - 0.0025, f"run-to-run sd ±{FLOOR_REPLICATE}",
             fontsize=6.5, color=PAL["ink_2"], va="top", ha="left")
axes[0].legend(loc="lower left", handlelength=2.2, borderaxespad=0.2)
for ax, l in zip(axes, ("(a)", "(b)", "(c)")):
    panel_label(ax, l, x=-0.03, y=1.17)
save(fig, "fig_experiments_swap")
