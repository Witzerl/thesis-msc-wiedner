"""Figure fig_appendix_rollouts (Appendix D): additional rollouts of the canonical model
(dilated-stencil graph network, epoch-29 weights), ground truth and prediction per eye,
for four eyes chosen by stated rules from the regenerated validation eyes of folds 0, 1, 2.

Data: images/data/rollouts/ANISOGNN_final_dilmean_f{0,1,2}.npz, written and self-checked by
rollouts_regen.py (each reproduces its run's logged epoch-29 change-region Dice@360d).

Selection (author, 2026-10-21): the figure shows different kinds of lesion on which the model
works, not failure cases (those are discussed in the text). Pool: the 48 eyes, minus the eye of
fig_experiments_rollout (fold 0, eye 10), minus eyes whose change-region Dice at the one-year
anchor (epoch 29) is below the median of the 48 (0.544), minus eyes whose true lesion at the
anchor touches the border of the imaged field (train.py's border definition, as in
fig_experiments_rollout). From the pool, in this order, each rule skipping eyes already chosen:
  (a) small lesion: smallest baseline lesion area,
  (b) large lesion: largest baseline lesion area,
  (c) several lesions: most connected components of the baseline lesion,
  (d) faster growth: largest square-root-area growth rate of the true lesion over the eye's
      whole follow-up, (sqrt(A_last) - sqrt(A_baseline)) / years.
History: until 2026-10-02 the rules were highest Dice / lowest Dice / border lesion / fastest
growth; "lowest Dice" was removed in author review v6 #21, the others on 2026-10-21 (the
highest-Dice eye became the eye of fig_experiments_rollout on 2026-10-18).

Columns (2026-10-21, so the panels print large enough): the baseline and the follow-up visits
closest to each full year (360, 720, ... days), plus the last visit if it is not among them.
Each eye is cropped to the bounding box of its baseline, true and predicted lesions over the
shown visits plus a margin, and gets its own 1 mm scale bar in the left margin (eyes are drawn at different
zoom). Physical aspect ratio throughout.

Run from images/scripts/:  python fig_appendix_rollouts.py
"""
from __future__ import annotations

import matplotlib as mpl
import numpy as np
from matplotlib.lines import Line2D
from scipy.ndimage import label

from _common import setup, save, DY_MM, DX_MM
import rollouts_panels as RP
from rollouts_panels import load_cache

ARM = "ANISOGNN_final_dilmean"
FOLDS = (0, 1, 2)
MAIN_FIG_EYE = (0, 10)    # eye of fig_experiments_rollout (fold 0, PEAT0013_OD), since 2026-10-18
MARGIN_MM = 0.35


def border_pixels(gt, valid):
    inv = ~valid
    adj = np.zeros_like(inv)
    adj[1:] |= inv[:-1]; adj[:-1] |= inv[1:]; adj[:, 1:] |= inv[:, :-1]; adj[:, :-1] |= inv[:, 1:]
    ring = np.zeros_like(gt)
    ring[0] = ring[-1] = True
    ring[:, 0] = ring[:, -1] = True
    return int((gt & (ring | adj)).sum())


def yearly_steps(cum_days):
    """Indices of the follow-up visits closest to each full year, plus the last visit."""
    cum = np.asarray(cum_days)
    steps = []
    for y in range(1, int(cum[-1] // 360) + 1):
        s = int(np.argmin(np.abs(cum - 360 * y)))
        if s not in steps:
            steps.append(s)
    if len(cum) - 1 not in steps:
        steps.append(len(cum) - 1)
    return steps


def crop_box(masks):
    """(x0, x1, y_bottom, y_top) in mm around the union of the masks, plus a margin."""
    m = np.any(masks, axis=0)
    rows, cols = np.nonzero(m)
    x0 = max(cols.min() * DX_MM - MARGIN_MM, 0.0)
    x1 = min((cols.max() + 1) * DX_MM + MARGIN_MM, RP.EXTENT[1])
    y0 = max(rows.min() * DY_MM - MARGIN_MM, 0.0)
    y1 = min((rows.max() + 1) * DY_MM + MARGIN_MM, RP.EXTENT[2])
    return x0, x1, y1, y0


def main():
    pal = setup()
    import matplotlib.pyplot as plt
    mpl.rcParams["hatch.color"] = pal.PAL["muted"]
    mpl.rcParams["hatch.linewidth"] = 0.4
    # exact physical size (no tight bbox): the PNG is then exactly the text width, so the
    # 7-8 pt labels print at their nominal size when included at width = text width
    mpl.rcParams["savefig.bbox"] = "standard"

    px_mm2 = DY_MM * DX_MM
    eyes = {}
    for f in FOLDS:
        es, meta = load_cache(f"{ARM}_f{f}")
        print(f"{ARM}_f{f}: logged e29 {meta['chg_logged']:.6f}  regenerated {meta['chg_cache']:.6f}")
        assert abs(meta["chg_cache"] - meta["chg_logged"]) < 1e-3, "unverified rollout"
        for e in es:
            a = RP.anchor_step(e["cum_days"])
            b, g, p = e["base"], e["gt"][a], e["pred"][a]
            tc, pc = g ^ b, p ^ b
            e["fold"], e["anchor"] = f, a
            e["chg"] = 2 * (tc & pc).sum() / max(tc.sum() + pc.sum(), 1)
            e["border_px"] = border_pixels(g, e["valid"][a])
            e["area"] = b.sum() * px_mm2
            e["comp"] = label(b)[1]
            yrs = e["cum_days"][-1] / 365.0
            e["rate"] = (np.sqrt(e["gt"][-1].sum() * px_mm2) - np.sqrt(b.sum() * px_mm2)) / yrs
            eyes[(f, e["eye_idx"])] = e
    med = float(np.median([e["chg"] for e in eyes.values()]))
    print(f"{len(eyes)} eyes, median change-region Dice at the anchor {med:.3f}")
    assert abs(eyes[MAIN_FIG_EYE]["chg"] - 0.761) < 5e-4, "Fig. 5.2 eye moved"

    taken = {MAIN_FIG_EYE} | {k for k, e in eyes.items() if e["chg"] < med or e["border_px"] > 0}
    print(f"pool: {len(eyes) - len(taken)} eyes")
    rules = [("(a) Small lesion", lambda e: e["area"]),
             ("(b) Large lesion", lambda e: -e["area"]),
             ("(c) Several lesions", lambda e: -e["comp"]),
             ("(d) Faster growth", lambda e: -e["rate"])]
    picks = []
    for title, key in rules:
        k = min((k for k in eyes if k not in taken), key=lambda k: key(eyes[k]))
        taken.add(k)
        e = eyes[k]
        e["steps"] = yearly_steps(e["cum_days"])
        shown = [e["base"]] + [e["gt"][s] for s in e["steps"]] + [e["pred"][s] for s in e["steps"]]
        e["box"] = crop_box(shown)
        picks.append((title, e))
        print(f"{title:<20s} fold {e['fold']} eye {e['eye_idx']:2d} {e['eye_id']:<12s} "
              f"chg Dice {e['chg']:.3f} | area {e['area']:.2f} mm2 | lesions {e['comp']} | "
              f"rate {e['rate']:.3f} mm/yr | days {np.rint(e['cum_days']).astype(int).tolist()} | "
              f"shown {[int(round(e['cum_days'][s])) for s in e['steps']]} | "
              f"crop {e['box'][1] - e['box'][0]:.2f} x {e['box'][2] - e['box'][3]:.2f} mm")

    # ---------------- layout (inches) ----------------
    W = pal.fig_size(1.0)[0]
    ncol = 1 + max(len(e["steps"]) for _, e in picks)
    lm, rm, gap = 0.85, 0.04, 0.04
    pw = (W - lm - rm - (ncol - 1) * gap) / ncol
    head, block_gap, leg_h = 0.17, 0.08, 0.40
    phs = [pw * (e["box"][2] - e["box"][3]) / (e["box"][1] - e["box"][0]) for _, e in picks]
    H = sum(head + 2 * ph + gap for ph in phs) + (len(picks) - 1) * block_gap + leg_h + 0.04
    fig = plt.figure(figsize=(W, H))
    print(f"{ncol} columns, panel width {pw:.3f} in, figure {W:.2f} x {H:.2f} in")

    any_pad = False
    y = 0.0
    for (title, e), ph in zip(picks, phs):
        cum = np.rint(e["cum_days"]).astype(int)
        x0, x1, yb, yt = e["box"]
        base_pad, eid = RP.baseline_pad(e["fold"], e["eye_idx"])
        assert eid == e["eye_id"]
        cols = [None] + e["steps"]
        y_head = y + head
        for r in range(2):
            y_top = y_head + r * (ph + gap)
            for c, s in enumerate(cols):
                ax = fig.add_axes([(lm + c * (pw + gap)) / W, 1 - (y_top + ph) / H, pw / W, ph / H])
                pad = base_pad if s is None else ~e["valid"][s]
                if r == 0:
                    codes = RP.gt_codes(e["base"] if s is None else e["gt"][s])
                elif s is None:
                    codes = np.where(e["base"], RP.UNCH, RP.BG).astype(np.uint8)
                else:
                    codes = RP.model_codes(e["pred"][s], e["gt"][s], e["base"])
                RP.draw_panel(ax, codes, e["base"], pal, pad=pad, outline_lw=0.55)
                ax.set_xlim(x0, x1)
                ax.set_ylim(yb, yt)
                pad_in_view = pad[int(yt / DY_MM):int(np.ceil(yb / DY_MM)),
                                  int(x0 / DX_MM):int(np.ceil(x1 / DX_MM))]
                any_pad |= bool(pad_in_view.any())
                if r == 0:
                    lab = "Baseline" if s is None else f"{cum[s]} d"
                    ax.set_title(lab, fontsize=7, loc="center", pad=2, color=pal.PAL["ink"],
                                 fontweight="bold" if (s is not None and s == e["anchor"]) else "normal")
                if c == 0:
                    ax.text(-0.08, 0.5, "Truth" if r == 0 else "Prediction",
                            transform=ax.transAxes, ha="right", va="center", fontsize=7,
                            color=pal.PAL["ink"])
        y_title = 1 - (y + head * 0.5) / H
        fig.text(0.0, y_title, title, ha="left", va="center", fontsize=7.5,
                 fontweight="semibold", color=pal.PAL["ink"])
        # 1 mm scale bar at this eye's zoom, in the left margin below the "Prediction" label
        L = pw / (x1 - x0)
        y_bar = 1 - (y_head + 2 * ph + gap - 0.06) / H
        xl = 0.12
        fig.add_artist(Line2D([xl / W, (xl + L) / W], [y_bar] * 2, transform=fig.transFigure,
                              color=pal.PAL["ink"], lw=1.0, solid_capstyle="butt"))
        fig.text((xl + L / 2) / W, y_bar + 0.035 / H, "1 mm", ha="center", va="bottom",
                 fontsize=6.5, color=pal.PAL["ink"])
        y = y_head + 2 * ph + gap + block_gap

    fig.legend(handles=RP.legend_handles(pal, with_pad=any_pad), loc="lower center", ncol=4,
               frameon=False, fontsize=7, handlelength=1.3, handleheight=0.9, columnspacing=1.0,
               handletextpad=0.5, bbox_to_anchor=(0.5, 0.0))
    save(fig, "fig_appendix_rollouts", raster=True)


if __name__ == "__main__":
    main()
