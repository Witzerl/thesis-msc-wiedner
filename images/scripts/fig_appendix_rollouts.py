"""Figure fig_appendix_rollouts (Appendix D): additional rollouts of the canonical model
(dilated-stencil graph network, epoch-29 weights), ground truth and prediction per eye,
for four eyes chosen by stated rules from the regenerated validation eyes of folds 0, 1, 2.

Data: images/data/rollouts/ANISOGNN_final_dilmean_f{0,1,2}.npz, written and self-checked by
rollouts_regen.py (each reproduces its run's logged epoch-29 change-region Dice@360d).

Selection rules (over the 48 regenerated eyes; each rule skips eyes already chosen and the
eye shown in fig_experiments_rollout):
  (a) highest per-eye growth-region Dice at the one-year anchor (late-epoch mean,
      thesis_numbers.eye_late),
  (b) lowest per-eye growth-region Dice at the anchor (same instrument),
  (c) border-censored: most true-lesion pixels on the crop border at the anchor (outermost
      pixel ring of the window or 4-adjacent to zero padding -- train.py's border definition),
  (d) fastest true progression: largest square-root-area growth rate of the true lesion over
      the eye's whole follow-up, (sqrt(A_last) - sqrt(A_baseline)) / years.
Every follow-up visit is drawn (no truncation); shorter schedules leave cells empty.

Run from images/scripts/:  python fig_appendix_rollouts.py
"""
from __future__ import annotations

import matplotlib as mpl
import numpy as np

from _common import setup, save, thesis_numbers, DY_MM, DX_MM
import rollouts_panels as RP
from rollouts_panels import load_cache

ARM = "ANISOGNN_final_dilmean"
FOLDS = (0, 1, 2)
MAIN_FIG_EYE = (2, 8)     # eye of fig_experiments_rollout (fold 2, PEA01840_OS)


def border_pixels(gt, valid):
    inv = ~valid
    adj = np.zeros_like(inv)
    adj[1:] |= inv[:-1]; adj[:-1] |= inv[1:]; adj[:, 1:] |= inv[:, :-1]; adj[:, :-1] |= inv[:, 1:]
    ring = np.zeros_like(gt)
    ring[0] = ring[-1] = True
    ring[:, 0] = ring[:, -1] = True
    return int((gt & (ring | adj)).sum())


def main():
    pal = setup()
    import matplotlib.pyplot as plt
    mpl.rcParams["hatch.color"] = pal.PAL["muted"]
    mpl.rcParams["hatch.linewidth"] = 0.4
    # exact physical size (no tight bbox): the PNG is then exactly the text width, so the
    # 7-8 pt labels print at their nominal size when included at width = text width
    mpl.rcParams["savefig.bbox"] = "standard"

    tn = thesis_numbers()
    late = tn.eye_late(ARM, list(FOLDS))
    px_mm2 = DY_MM * DX_MM
    eyes = {}
    for f in FOLDS:
        es, meta = load_cache(f"{ARM}_f{f}")
        print(f"{ARM}_f{f}: logged e29 {meta['chg_logged']:.6f}  regenerated {meta['chg_cache']:.6f}")
        assert abs(meta["chg_cache"] - meta["chg_logged"]) < 1e-3, "unverified rollout"
        for e in es:
            a = RP.anchor_step(e["cum_days"])
            e["fold"], e["anchor"] = f, a
            e["late"] = late[(f, e["eye_idx"])]
            e["border_px"] = border_pixels(e["gt"][a], e["valid"][a])
            yrs = e["cum_days"][-1] / 365.0
            e["rate"] = (np.sqrt(e["gt"][-1].sum() * px_mm2) - np.sqrt(e["base"].sum() * px_mm2)) / yrs
            eyes[(f, e["eye_idx"])] = e
    print(f"{len(eyes)} eyes")

    taken = {MAIN_FIG_EYE}
    rules = [("(a) Highest Dice", lambda e: -e["late"]),
             ("(b) Lowest Dice", lambda e: e["late"]),
             ("(c) Border lesion", lambda e: -e["border_px"]),
             ("(d) Fastest growth", lambda e: -e["rate"])]
    picks = []
    for title, key in rules:
        k = min((k for k in eyes if k not in taken), key=lambda k: key(eyes[k]))
        taken.add(k)
        e = eyes[k]
        picks.append((title, e))
        print(f"{title:<32s} fold {e['fold']} eye {e['eye_idx']:2d} {e['eye_id']:<12s} "
              f"late growth Dice {e['late']:.4f} | border px {e['border_px']} | true rate "
              f"{e['rate']:.3f} mm/yr | follow-ups {len(e['dt'])} | days "
              f"{np.rint(e['cum_days']).astype(int).tolist()} | anchor step {e['anchor']} | "
              f"e29 growth Dice per step " + " ".join(f"{v:.3f}" for v in e["dice_growth"]))

    # ---------------- layout (inches) ----------------
    W = pal.fig_size(1.0)[0]
    ncol = 1 + max(len(e["dt"]) for _, e in picks)
    lm, rm, gap = 1.30, 0.04, 0.03
    pw = (W - lm - rm - (ncol - 1) * gap) / ncol
    ph = pw * (RP.EXTENT[2] / RP.EXTENT[1])
    head, block_gap, leg_h = 0.15, 0.06, 0.40
    H = len(picks) * (head + 2 * ph + gap) + (len(picks) - 1) * block_gap + leg_h + 0.04
    fig = plt.figure(figsize=(W, H))
    print(f"{ncol} columns, panel {pw:.3f} x {ph:.3f} in, figure {W:.2f} x {H:.2f} in "
          f"(height/width {H / W:.2f})")

    any_pad = False
    y = 0.0
    for b, (title, e) in enumerate(picks):
        cum = np.rint(e["cum_days"]).astype(int)
        base_pad, eid = RP.baseline_pad(e["fold"], e["eye_idx"])
        assert eid == e["eye_id"]
        pads = [base_pad] + [~v for v in e["valid"]]
        any_pad |= any(p.any() for p in pads)
        y_head = y + head
        for r in range(2):
            y_top = y_head + r * (ph + gap)
            for c in range(1 + len(e["dt"])):
                ax = fig.add_axes([(lm + c * (pw + gap)) / W, 1 - (y_top + ph) / H, pw / W, ph / H])
                s = c - 1
                if r == 0:
                    codes = RP.gt_codes(e["base"] if c == 0 else e["gt"][s])
                elif c == 0:
                    codes = np.where(e["base"], RP.UNCH, RP.BG).astype(np.uint8)
                else:
                    codes = RP.model_codes(e["pred"][s], e["gt"][s], e["base"])
                RP.draw_panel(ax, codes, e["base"], pal, pad=pads[c], outline_lw=0.45)
                if r == 0:
                    lab = "Baseline" if c == 0 else f"{cum[s]} d"
                    ax.set_title(lab, fontsize=6.5, loc="center", pad=2, color=pal.PAL["ink"],
                                 fontweight="bold" if (c > 0 and s == e["anchor"]) else "normal")
                if c == 0:
                    ax.text(-0.08, 0.5, "Ground truth" if r == 0 else "Prediction",
                            transform=ax.transAxes, ha="right", va="center", fontsize=7,
                            color=pal.PAL["ink"])
        fig.text(0.0, 1 - (y + head * 0.55) / H, title, ha="left", va="center", fontsize=7.5,
                 fontweight="semibold", color=pal.PAL["ink"])
        y = y_head + 2 * ph + gap + block_gap

    RP.scale_bar_fig(fig, pal, x_right_in=W - rm - 0.02, y_in=head * 0.55, panel_w_in=pw,
                     W=W, H=H)
    fig.legend(handles=RP.legend_handles(pal, with_pad=any_pad), loc="lower center", ncol=4,
               frameon=False, fontsize=7, handlelength=1.3, handleheight=0.9, columnspacing=1.0,
               handletextpad=0.5, bbox_to_anchor=(0.5, 0.0))
    save(fig, "fig_appendix_rollouts", raster=True)


if __name__ == "__main__":
    main()
