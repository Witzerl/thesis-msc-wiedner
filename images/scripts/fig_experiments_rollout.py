"""Figure fig_experiments_rollout (Chapter 5, section 5.2): one validation eye of fold 2, its
ground truth and the rollouts of five operators (epoch-29 weights), visit by visit.

Data: images/data/rollouts/<EXP>_f2.npz, written and self-checked by rollouts_regen.py
(each cache reproduces the run's logged epoch-29 change-region Dice@360d).

Eye-selection rule (fixed before looking at the panels): among the fold-2 validation eyes
with at least 4 follow-up visits, the eye whose canonical-model per-eye growth-region Dice at
the one-year anchor (late-epoch mean, thesis_numbers.eye_late('ANISOGNN_final_dilmean', [2]))
is closest to the median over those eligible eyes. At most baseline + 5 follow-ups are drawn.

Run from images/scripts/:  python fig_experiments_rollout.py [--eye N]
(--eye only for previews of other eyes; the thesis figure uses the rule.)
"""
from __future__ import annotations

import argparse
import statistics

import matplotlib as mpl
import numpy as np

from _common import setup, save, PREVIEW, thesis_numbers
import rollouts_panels as RP
from rollouts_panels import load_cache

ARMS = [  # (row label, experiment) -- order of the figure
    ("Dilated stencil", "ANISOGNN_final_dilmean"),
    ("U-Net", "UNET_final_w5"),
    ("T-FEN", "FEN_final_w96ftp7rk4d45skew"),
    ("FNO", "FNO_final_w5"),
    ("k-NN graph", "MPPDE_final_aggrmean"),
]
FOLD = 2
MAX_FOLLOW = 5
MIN_FOLLOW = 4


def select_eye(caches):
    tn = thesis_numbers()
    late = tn.eye_late("ANISOGNN_final_dilmean", [FOLD])
    canon = {e["eye_idx"]: e for e in caches["ANISOGNN_final_dilmean"]}
    elig = {i: late[(FOLD, i)] for i, e in canon.items()
            if len(e["dt"]) >= MIN_FOLLOW and (FOLD, i) in late}
    med = float(np.median(list(elig.values())))
    # With an even number of eligible eyes the two middle eyes are exactly equidistant from
    # the median; the tie is broken by the lower median (statistics.median_low).
    low = statistics.median_low(list(elig.values()))
    ranked = sorted(elig, key=lambda i: (abs(elig[i] - med), elig[i] != low))
    print(f"eligible eyes: {len(elig)} of {len(canon)}; median late growth Dice {med:.6f} "
          f"(lower median {low:.6f})")
    for i in ranked[:4]:
        print(f"  eye {i:2d} {canon[i]['eye_id']:<12s} late Dice {elig[i]:.6f} "
              f"|d| {abs(elig[i] - med):.6f} follow-ups {len(canon[i]['dt'])}")
    pick = next(i for i in elig if elig[i] == low)
    return pick, elig, med


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--eye", type=int, default=None, help="preview another eye (not the rule)")
    args = ap.parse_args()

    pal = setup()
    import matplotlib.pyplot as plt
    mpl.rcParams["hatch.color"] = pal.PAL["muted"]
    mpl.rcParams["hatch.linewidth"] = 0.4
    # exact physical size (no tight bbox): the PNG is then exactly the text width, so the
    # 7-8 pt labels print at their nominal size when included at width = text width
    mpl.rcParams["savefig.bbox"] = "standard"

    caches, metas = {}, {}
    for _, exp in ARMS:
        eyes, meta = load_cache(f"{exp}_f{FOLD}")
        caches[exp], metas[exp] = eyes, meta
        print(f"{exp:<32s} cache: logged e29 {meta['chg_logged']:.6f}  regenerated "
              f"{meta['chg_cache']:.6f}  ({meta['run_dir'][-15:]})")
        assert abs(meta["chg_cache"] - meta["chg_logged"]) < 1e-3, "unverified rollout"

    eye_idx, elig, med = select_eye(caches)
    if args.eye is not None:
        eye_idx = args.eye
    E = {exp: next(e for e in caches[exp] if e["eye_idx"] == eye_idx) for _, exp in ARMS}
    ref = E["ANISOGNN_final_dilmean"]
    n_follow = len(ref["dt"])
    n_show = min(MAX_FOLLOW, n_follow)
    cum = np.rint(ref["cum_days"]).astype(int)
    a_idx = RP.anchor_step(ref["cum_days"])
    for _, exp in ARMS:   # every arm rolled out the same eye on the same schedule
        assert np.array_equal(E[exp]["gt"], ref["gt"]) and np.array_equal(E[exp]["base"], ref["base"])
        assert np.allclose(E[exp]["dt"], ref["dt"])
    base_pad, eye_id = RP.baseline_pad(FOLD, eye_idx)
    assert eye_id == ref["eye_id"], (eye_id, ref["eye_id"])
    pads = [base_pad] + [~ref["valid"][s] for s in range(n_show)]
    any_pad = any(p.any() for p in pads)
    print(f"eye {eye_idx} ({ref['eye_id']}): {n_follow} follow-ups, showing {n_show}; "
          f"cumulative days {cum.tolist()}; anchor step {a_idx} ({cum[a_idx]} d); "
          f"zero padding present: {any_pad}")
    print(f"  baseline lesion {ref['base'].sum()} px; true lesion per step "
          f"{[int(g.sum()) for g in ref['gt'][:n_show]]}")
    for lab, exp in ARMS:
        e = E[exp]
        print(f"  {lab:<16s} growth-region Dice per step (this rollout): "
              + " ".join(f"{v:.3f}" for v in e["dice_growth"][:n_show]))

    # ---------------- layout (inches) ----------------
    W = pal.fig_size(1.0)[0]
    lm, rm, top, gap, gt_gap = 0.80, 0.04, 0.20, 0.035, 0.09
    ncol = n_show + 1
    pw = (W - lm - rm - (ncol - 1) * gap) / ncol
    ph = pw * (RP.EXTENT[2] / RP.EXTENT[1])
    nrow = 1 + len(ARMS)
    leg_h = 0.42
    H = top + nrow * ph + (nrow - 2) * gap + gt_gap + leg_h
    fig = plt.figure(figsize=(W, H))

    def add_ax(r, c):
        y_top = top + r * (ph + gap) + (gt_gap - gap if r >= 1 else 0)
        return fig.add_axes([(lm + c * (pw + gap)) / W, 1 - (y_top + ph) / H, pw / W, ph / H])

    rows = [("Ground truth", None)] + ARMS
    for r, (lab, exp) in enumerate(rows):
        for c in range(ncol):
            ax = add_ax(r, c)
            s = c - 1
            if exp is None:
                codes = RP.gt_codes(ref["base"] if c == 0 else ref["gt"][s])
            else:
                if c == 0:   # the input every model receives: the baseline mask itself
                    codes = np.where(ref["base"], RP.UNCH, RP.BG).astype(np.uint8)
                else:
                    codes = RP.model_codes(E[exp]["pred"][s], ref["gt"][s], ref["base"])
            RP.draw_panel(ax, codes, ref["base"], pal, pad=pads[c])
            if r == 0:
                head = "Baseline" if c == 0 else f"{cum[s]} d"
                ax.set_title(head, fontsize=7, loc="center", pad=3, color=pal.PAL["ink"],
                             fontweight="bold" if (c > 0 and s == a_idx) else "normal")
            if c == 0:
                ax.text(-0.08, 0.5, lab, transform=ax.transAxes, ha="right", va="center",
                        fontsize=7.5, color=pal.PAL["ink"])

    RP.scale_bar_fig(fig, pal, x_right_in=lm - 0.10, y_in=top * 0.45, panel_w_in=pw, W=W, H=H)
    leg = fig.legend(handles=RP.legend_handles(pal, with_pad=any_pad), loc="lower center",
                     ncol=4, frameon=False, fontsize=7, handlelength=1.3, handleheight=0.9,
                     columnspacing=1.0, handletextpad=0.5,
                     bbox_to_anchor=(0.5, 0.0))
    name = "fig_experiments_rollout" if args.eye is None else f"_alt_rollout_eye{args.eye}"
    if args.eye is None:
        save(fig, name, raster=True)
    else:
        PREVIEW.mkdir(exist_ok=True)
        fig.savefig(PREVIEW / f"{name}.png", dpi=200)
        print("wrote preview", PREVIEW / f"{name}.png")
    print(f"{'selected' if args.eye is None else 'preview'} eye {eye_idx} ({ref['eye_id']}), late-epoch growth Dice {elig[eye_idx]:.5f}, "
          f"median {med:.5f}; figure {W:.2f} x {H:.2f} in")


if __name__ == "__main__":
    main()
