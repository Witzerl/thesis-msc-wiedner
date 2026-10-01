"""Figure fig:experiments:growth-rate (Section 5.5.1, Table tab:experiments:mai): predicted
against true growth rate per eye for the canonical dilated-stencil graph network.

Growth rate = (sqrt(A_last) - sqrt(A_base)) / T over the eye's whole rollout, in mm/yr, as
logged in mai/epoch_*.json -> per_eye (growth_rate_pred_mm_per_year,
growth_rate_true_mm_per_year). Predicted rate per (fold, eye) = mean over the late epochs
10-29; the true rate is the same in every epoch (checked). 75 validation eyes of folds 0-4
pooled (latest run directory per fold, as in thesis_numbers.py). Pearson r with a 95 %
percentile bootstrap over eyes (2000 resamples, seed 0); fast progressors = the top
round(0.2 * 75) = 15 eyes by true rate, as for the AUC in Table tab:appendix:growth-speed.

    python fig_experiments_growth_rate.py
"""
import json
import os

import matplotlib.pyplot as plt
import numpy as np

from _common import LATE_FROM, save, setup, thesis_numbers

pal = setup()
ARM, PAL = pal.ARM, pal.PAL
tn = thesis_numbers()
ARMNAME = "ANISOGNN_final_dilmean"

pred, true, base_sqrt, base_area, keys = [], [], [], [], []
for f in tn.FOLDS:
    rd = tn.run_dir(ARMNAME, f)
    assert tn.complete(rd), f
    acc, tr, bs, ba = {}, {}, {}, {}
    for fn in sorted(os.listdir(os.path.join(rd, "mai"))):
        j = json.load(open(os.path.join(rd, "mai", fn)))
        if j["epoch"] < LATE_FROM:
            continue
        for e in j["per_eye"]:
            k = e["eye_idx"]
            acc.setdefault(k, []).append(e["growth_rate_pred_mm_per_year"])
            t = e["growth_rate_true_mm_per_year"]
            assert k not in tr or abs(tr[k] - t) < 1e-12, "true rate differs between epochs"
            tr[k] = t
            bs[k], ba[k] = e["sqrt_baseline_area_mm"], e["baseline_area_mm2"]
    for k in sorted(acc):
        assert len(acc[k]) == 30 - LATE_FROM, (f, k, len(acc[k]))
        keys.append((f, k))
        pred.append(np.mean(acc[k]))
        true.append(tr[k])
        base_sqrt.append(bs[k])
        base_area.append(ba[k])
pred, true = np.array(pred), np.array(true)
base_sqrt, base_area = np.array(base_sqrt), np.array(base_area)
n = len(true)
print(f"{ARMNAME}: {n} eyes ({', '.join(str(sum(1 for f, _ in keys if f == g)) for g in tn.FOLDS)} per fold)")
assert n == 75


def pearson(a, b):
    return float(np.corrcoef(a, b)[0, 1])


r = pearson(pred, true)
rng = np.random.default_rng(0)
boot, boot_idx = [], []
for _ in range(2000):
    i = rng.integers(0, n, n)
    boot_idx.append(i)
    boot.append(pearson(pred[i], true[i]))
lo, hi = np.percentile(boot, [2.5, 97.5])
# the legacy NumPy generator, for comparison (the original computation's generator is not recorded)
rs = np.random.RandomState(0)
boot2 = [pearson(pred[i], true[i]) for i in (rs.randint(0, n, n) for _ in range(2000))]
lo2, hi2 = np.percentile(boot2, [2.5, 97.5])


def auc(score, pos):
    """Mann-Whitney AUC with ties counted one half."""
    p, q = score[pos], score[~pos]
    return float(((p[:, None] > q[None, :]).sum() + 0.5 * (p[:, None] == q[None, :]).sum())
                 / (len(p) * len(q)))


order = np.argsort(-true)
aucs = {}
for qq in (10, 15, 20):
    m = int(round(qq / 100 * n))
    pos = np.zeros(n, bool)
    pos[order[:m]] = True
    aucs[qq] = (auc(pred, pos), m)
# AUC intervals on the same resamples, positives fixed to the original top-q eyes
auc_ci = {}
for qq, (a, m) in aucs.items():
    pos = np.zeros(n, bool)
    pos[order[:m]] = True
    b = [auc(pred[i], pos[i]) if 0 < pos[i].sum() < n else np.nan for i in boot_idx]
    auc_ci[qq] = tuple(np.nanpercentile(b, [2.5, 97.5]))
fast = np.zeros(n, bool)
fast[order[:aucs[20][1]]] = True
cut = true[order[aucs[20][1] - 1]]

r_base_sqrt = pearson(base_sqrt, true)
r_base_area = pearson(base_area, true)
print(f"Pearson r = {r:.4f}; 95 % bootstrap [{lo:.4f}, {hi:.4f}] (default_rng(0)), "
      f"[{lo2:.4f}, {hi2:.4f}] (RandomState(0))")
for qq, (a, m) in aucs.items():
    print(f"AUC top {qq} % ({m} eyes) = {a:.4f}  [{auc_ci[qq][0]:.4f}, {auc_ci[qq][1]:.4f}]")
print(f"fast-progressor cut-off (15th-highest true rate) = {cut:.4f} mm/yr")
print(f"r(sqrt baseline area, true rate) = {r_base_sqrt:.4f};  r(baseline area, true rate) = {r_base_area:.4f}")
print(f"true rate: mean {true.mean():.4f}, median {np.median(true):.4f}, range [{true.min():.4f}, {true.max():.4f}]")
print(f"predicted rate: mean {pred.mean():.4f}, median {np.median(pred):.4f}, range [{pred.min():.4f}, {pred.max():.4f}]")
print(f"eyes with predicted < true: {(pred < true).sum()}/{n};  "
      f"OLS slope pred on true {np.polyfit(true, pred, 1)[0]:.3f}")

# Known (2026-10-01): Table tab:experiments:mai quotes r 0.40 [0.22, 0.56]; no percentile
# bootstrap over these 75 eyes reproduces that interval (default_rng 0-5, RandomState(0),
# fold-stratified, scipy percentile/BCa all give a lower bound of 0.19-0.21 and an upper bound
# of 0.56-0.58), and the session's own growth_rates.py also prints [0.20, 0.57]. The figure
# shows the recomputed interval.
print("\ncheck: text value vs computed")
CHECK = [("Pearson r", 0.40, r, 2), ("bootstrap lower", 0.22, lo, 2), ("bootstrap upper", 0.56, hi, 2),
         ("AUC top 10 %", 0.74, aucs[10][0], 2), ("AUC top 15 %", 0.70, aucs[15][0], 2),
         ("AUC top 20 %", 0.70, aucs[20][0], 2), ("r baseline size alone", -0.10, r_base_sqrt, 2)]
for name, t, c, d in CHECK:
    print(f"  {name:22s} text {t:+.2f}  computed {c:+.4f}  {'ok' if round(c, d) == t else 'MISMATCH'}")
for qq, m in ((10, 8), (15, 11), (20, 15)):
    assert aucs[qq][1] == m

# ---------------------------------------------------------------- figure
fig, ax = plt.subplots(figsize=pal.fig_size(0.645, 0.92))
lim = (0.0, 0.64)
assert max(true.max(), pred.max()) < lim[1]
ax.plot(lim, lim, color=PAL["muted"], ls="--", lw=0.9, zorder=1)
ax.text(lim[1] * 0.97, lim[1] * 0.97 - 0.035, "identity", color=PAL["ink_2"], fontsize=6.5,
        ha="right", va="top", rotation=45, rotation_mode="anchor")
ax.scatter(true[~fast], pred[~fast], s=13, facecolor="white", edgecolor=ARM["stencil"],
           linewidth=0.8, zorder=3, label=f"other eyes ({(~fast).sum()})")
ax.scatter(true[fast], pred[fast], s=13, facecolor=ARM["stencil"], edgecolor=ARM["stencil"],
           linewidth=0.8, zorder=4, label=f"fastest 20 % ({fast.sum()})")
ax.axvline(cut, color=PAL["line"], lw=0.7, ls=(0, (2, 2)), zorder=0)
ax.set_xlim(*lim)
ax.set_ylim(*lim)
ax.set_aspect("equal")
ax.grid(axis="x", visible=True)
ax.set_xticks(np.arange(0, 0.61, 0.1))
ax.set_yticks(np.arange(0, 0.61, 0.1))
ax.set_xlabel("True growth rate (mm/yr)")
ax.set_ylabel("Predicted growth rate (mm/yr)")
ax.text(0.03, 0.97, f"$r$ = {r:.2f} [{lo:.2f}, {hi:.2f}]\n{n} eyes", transform=ax.transAxes,
        ha="left", va="top", fontsize=7, color=PAL["ink"])
ax.legend(loc="lower right", handletextpad=0.2, borderaxespad=0.3, fontsize=7)
save(fig, "fig_experiments_growth_rate")
