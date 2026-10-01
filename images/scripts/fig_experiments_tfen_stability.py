"""Figure fig:experiments:tfen-stability (Section 5.5.2, Table tab:experiments:tfen-stability):
free-running rollout error of the T-FEN per epoch, Galerkin against energy-conserving form.

rollout_mask_rmse and rollout_layer_rmse from metrics.jsonl (normalised units), every epoch
0-29, five folds, seed 42: FEN_final_w96ftp7rk4d45 (Galerkin form) and
FEN_final_w96ftp7rk4d45skew (energy-conserving form); latest run directory per fold, as in
thesis_numbers.py. The stability criterion (thesis_numbers.py `stability`): mask and layer
error <= 5 on at least 19 of the 20 late epochs (10-29).

    python fig_experiments_tfen_stability.py
"""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

from _common import LATE_FROM, panel_label, save, setup, thesis_numbers

pal = setup()
ARM, PAL = pal.ARM, pal.PAL
tn = thesis_numbers()

FORMS = {"galerkin": "FEN_final_w96ftp7rk4d45", "skew": "FEN_final_w96ftp7rk4d45skew"}
CH = {"mask": "rollout_mask_rmse", "layer": "rollout_layer_rmse"}
THR = 5.0

data = {}  # (form, fold) -> {"epoch": [...], "mask": [...], "layer": [...]}
for form, arm in FORMS.items():
    for f in tn.FOLDS:
        rd = tn.run_dir(arm, f)
        assert tn.complete(rd), (arm, f)
        ep = tn.epochs(rd)
        assert [m["epoch"] for m in ep] == list(range(30)), (arm, f)
        data[(form, f)] = {"epoch": np.array([m["epoch"] for m in ep]),
                           **{c: np.array([m.get(k, float("nan")) for m in ep], float)
                              for c, k in CH.items()}}

# ---------------------------------------------------------------- values and checks
nonfinite = []
print("per fold: late epochs <= 5 (mask / layer), largest late-epoch error (mask / layer)")
summary = {}
for form in FORMS:
    for f in tn.FOLDS:
        d = data[(form, f)]
        late = d["epoch"] >= LATE_FROM
        cnt, mx = {}, {}
        for c in CH:
            v = d[c]
            bad = ~np.isfinite(v)
            for e in d["epoch"][bad]:
                nonfinite.append((form, f, c, int(e), v[d["epoch"] == e][0]))
            cnt[c] = int(np.sum(v[late] <= THR))                  # NaN/inf count as > 5
            mx[c] = float(np.max(v[late])) if np.all(np.isfinite(v[late])) else float("inf")
        summary[(form, f)] = (cnt, mx)
        ok = cnt["mask"] >= 19 and cnt["layer"] >= 19
        print(f"  {form:8s} f{f}: {cnt['mask']:2d} / {cnt['layer']:2d}   max {mx['mask']:.4g} / {mx['layer']:.4g}"
              f"   {'stable' if ok else 'UNSTABLE'}   (all epochs: max {np.nanmax(d['mask']):.4g} / "
              f"{np.nanmax(d['layer']):.4g})")
print(f"non-finite epoch values: {len(nonfinite)}" + "".join(f"\n  {x}" for x in nonfinite))

TABLE = {  # Table tab:experiments:tfen-stability: (mask count, layer count, mask max, layer max)
    ("galerkin", 0): (1, 2, "24418", "456"), ("galerkin", 1): (12, 19, "196", "14.9"),
    ("galerkin", 2): (18, 19, "6.97", "33.5"), ("galerkin", 3): (20, 20, "1.49", "3.33"),
    ("galerkin", 4): (19, 6, "11.9", "174"),
    ("skew", 0): (20, 20, "2.00", "1.13"), ("skew", 1): (20, 20, "2.32", "0.89"),
    ("skew", 2): (20, 20, "1.82", "1.08"), ("skew", 3): (20, 20, "1.73", "0.82"),
    ("skew", 4): (20, 20, "2.00", "0.99"),
}


def fmt_like(x, ref):
    """Round x the way the table rounds `ref` (3 significant figures, or as many decimals)."""
    if "." in ref:
        return f"{x:.{len(ref.split('.')[1])}f}"
    return f"{x:.0f}"


print("\ncheck: Table tab:experiments:tfen-stability (text) vs computed")
nbad = 0
for key, (tm, tl, xm, xl) in TABLE.items():
    cnt, mx = summary[key]
    cm, cl = fmt_like(mx["mask"], xm), fmt_like(mx["layer"], xl)
    ok = (cnt["mask"], cnt["layer"], cm, cl) == (tm, tl, xm, xl)
    nbad += not ok
    print(f"  {key[0]:8s} f{key[1]}: text {tm}/{tl}, {xm}/{xl}   computed {cnt['mask']}/{cnt['layer']}, "
          f"{cm}/{cl}  {'ok' if ok else 'MISMATCH'}")
print(f"  {'all values match' if not nbad else f'{nbad} MISMATCHES'}")

# ---------------------------------------------------------------- figure
fig, axes = plt.subplots(1, 2, figsize=pal.fig_size(1.146, 0.349), sharey=True,
                         gridspec_kw=dict(wspace=0.08))
YLIM = (0.3, 1e5)
for ax, (c, head) in zip(axes, [("mask", "Mask channel"), ("layer", "Layer channels")]):
    ax.axvspan(LATE_FROM - 0.5, 29.5, color=PAL["bg_soft"], lw=0, zorder=0)
    ax.axhline(THR, color=PAL["muted"], ls="--", lw=0.9, zorder=1)
    for form in ("galerkin", "skew"):
        for f in tn.FOLDS:
            d = data[(form, f)]
            v = d[c].copy()
            fin = np.isfinite(v)
            kw = (dict(ls=(0, (3, 1.5)), lw=0.9, alpha=0.9) if form == "galerkin"
                  else dict(ls="-", lw=1.1, alpha=0.9))
            ax.plot(d["epoch"][fin], v[fin], color=ARM["tfen"], zorder=3, **kw)
            if (~fin).any():                                       # non-finite: mark at the top edge
                ax.plot(d["epoch"][~fin], np.full((~fin).sum(), YLIM[1]), ls="none", marker="^",
                        ms=4, color=ARM["tfen"], clip_on=False, zorder=4)
    ax.set_yscale("log")
    ax.set_ylim(*YLIM)
    ax.set_xlim(-0.5, 29.5)
    ax.set_xticks([0, 5, 10, 15, 20, 25, 29])
    ax.set_xlabel("Epoch")
    ax.set_title(head, fontsize=7.5, loc="left", pad=3)
axes[0].set_ylabel("Free-running rollout error\n(RMSE, normalised units)")
axes[1].text(29.2, YLIM[1] * 0.7, "late epochs", fontsize=6.5, color=PAL["ink_2"], va="top", ha="right")

h = [Line2D([], [], color=ARM["tfen"], ls=(0, (3, 1.5)), lw=0.9, label="Galerkin form"),
     Line2D([], [], color=ARM["tfen"], ls="-", lw=1.1, label="energy-conserving form"),
     Line2D([], [], color=PAL["muted"], ls="--", lw=0.9, label="stability threshold (5)")]
axes[1].legend(handles=h, loc="upper left", handlelength=2.4, borderaxespad=0.3)
for ax, l in zip(axes, ("(a)", "(b)")):
    panel_label(ax, l, x=-0.03, y=1.04)
save(fig, "fig_experiments_tfen_stability")
