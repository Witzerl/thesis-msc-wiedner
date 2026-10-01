"""Appendix A, Figure fig:appendix:cohort -- the visit schedule and lesion scale of the cohort.

    cd images/scripts && python fig_appendix_cohort.py

Panels: (a) visits per eye, (b) intervals between consecutive visits, (c) baseline
lesion area per eye, (d) square-root-area growth rate per eye.

Everything is read from the raw cohort folder of the code repo (read-only):
data/MUW_GA/scans/<EYE>/<day>/mask_oct.png (native OCT-grid mask, 0/255), the folder
name being the visit day. Definitions follow the code repo:
  * centre crop / zero pad to 49 x 1024 = tools/precompute_graphs_ga.py:center_crop_or_pad
    (re-implemented below, identical index arithmetic);
  * mask threshold > 127 = precompute load_visit;
  * pixel area 0.12118 x 0.00568 mm^2 (constant-spacing assumption, Section 3.1);
  * growth rate = (sqrt(A_last) - sqrt(A_base)) / (span_days / 365), areas on the 49 x 1024
    grid = GraphPDE/train.py per-eye record (growth_rate_true_mm_per_year);
  * visit gaps = tools/cohort_visit_stats.py (dt * 365 of the precomputed windows), which is
    cross-checked here against the raw folder days.
The per-visit table is cached in images/data/cohort_visits.csv; delete it to recompute.
Every statistic the thesis text quotes is printed next to the text value (check table).
"""
from __future__ import annotations

import json
from collections import Counter

import numpy as np
import pandas as pd
from PIL import Image

from _common import setup, save, panel_label, SCANS, CODE, CACHE, NROWS, NCOLS, DY_MM, DX_MM

PIX_MM2 = DY_MM * DX_MM
CACHE_CSV = CACHE / "cohort_visits.csv"


# --------------------------------------------------------------------------- data
def _crop_slices(n: int, t: int):
    """(source slice, destination slice) of a symmetric centre crop / zero pad of length n
    to t; same arithmetic as tools/precompute_graphs_ga.py:center_crop_or_pad."""
    if n >= t:
        o = (n - t) // 2
        return slice(o, o + t), slice(0, t)
    o = (t - n) // 2
    return slice(0, n), slice(o, o + n)


def _ring(a: np.ndarray) -> bool:
    """True if any pixel of the 2-D boolean array lies on its outermost ring."""
    return bool(a[0].any() or a[-1].any() or a[:, 0].any() or a[:, -1].any())


def visit_table(recompute: bool = False) -> pd.DataFrame:
    """One row per visit: native shape, native and in-window lesion pixels, crop flags."""
    if CACHE_CSV.exists() and not recompute:
        return pd.read_csv(CACHE_CSV)
    rows = []
    for eye_dir in sorted(p for p in SCANS.iterdir() if p.is_dir()):
        days = sorted(int(d.name) for d in eye_dir.iterdir() if d.is_dir())
        for day in days:
            vd = eye_dir / str(day)
            if not (vd / "mask_oct.png").exists() or not (vd / "layers_oct.npz.npy").exists():
                continue
            m = np.array(Image.open(vd / "mask_oct.png")) > 127
            H, W = m.shape
            (sh, dh), (sw, dw) = _crop_slices(H, NROWS), _crop_slices(W, NCOLS)
            win = np.zeros((NROWS, NCOLS), bool)
            win[dh, dw] = m[sh, sw]
            valid = win[dh, dw]                     # the non-pad part of the window
            n_nat, n_win = int(m.sum()), int(win.sum())
            rows.append(dict(
                eye=eye_dir.name, patient=eye_dir.name.split("_")[0], day=day,
                H=H, W=W, n_native=n_nat, n_window=n_win,
                row_pad=H < NROWS, col_pad=W < NCOLS,
                pad_frac=1.0 - (min(H, NROWS) * min(W, NCOLS)) / (NROWS * NCOLS),
                # lesion on the outer ring of the window's non-pad region (crop edge or the
                # scan's own edge) -- pad-aware; and on the ring of the 49x1024 window itself
                touch_valid=_ring(valid) if n_win else False,
                touch_window=_ring(win) if n_win else False,
                touch_native=_ring(m) if n_nat else False,
            ))
    df = pd.DataFrame(rows)
    CACHE.mkdir(exist_ok=True)
    df.to_csv(CACHE_CSV, index=False)
    return df


def eye_table(v: pd.DataFrame) -> pd.DataFrame:
    """One row per eye: visits, follow-up, baseline area, growth rate, age, sex."""
    cov = pd.read_csv(CODE / "data" / "MUW_GA" / "clinical_covariates.csv").set_index("eye_index")
    out = []
    for eye, g in v.sort_values("day").groupby("eye", sort=True):
        a0 = g.n_window.iloc[0] * PIX_MM2
        a1 = g.n_window.iloc[-1] * PIX_MM2
        span = int(g.day.iloc[-1] - g.day.iloc[0])
        out.append(dict(
            eye=eye, patient=g.patient.iloc[0], n_visits=len(g), span_days=span,
            gaps=list(np.diff(g.day.to_numpy()).astype(int)),
            base_area_mm2=a0, base_area_native_mm2=g.n_native.iloc[0] * PIX_MM2,
            growth_mm_yr=(np.sqrt(a1) - np.sqrt(a0)) / (span / 365.0),
            age=float(cov.loc[eye, "age"]), sex=cov.loc[eye, "sex"],
        ))
    return pd.DataFrame(out)


def fold_of_eye() -> dict[str, int]:
    """Validation fold of every eye, from the patient-level split files."""
    f = {}
    for k in range(5):
        s = json.loads((CODE / "data" / "MUW_GA" / "splits" / f"split_{k}.json").read_text())
        for pid in s["val_ids"]:
            f[pid] = k
    return f


def precomp_gaps() -> dict[str, list[int]]:
    """Visit gaps per eye as tools/cohort_visit_stats.py reads them (precomputed windows)."""
    import sys
    if str(CODE) not in sys.path:
        sys.path.insert(0, str(CODE))
    from tools.cohort_visit_stats import load_eyes   # read-only import
    pre = CODE / "data" / "GA" / "split2_n12_zscore_slo256_agevisit" / "precomp"
    return {e["eye"]: e["gaps"] for e in load_eyes(str(pre))}


# --------------------------------------------------------------------------- checks
def q(x, p, method="inverted_cdf"):
    """Percentile as an order statistic (numpy 'inverted_cdf'), the convention that
    reproduces the code repo's growth-rate quartiles; numpy's default 'linear' gives
    0.157-0.337 / 0.461 instead of 0.153-0.340 / 0.473 on the same 75 values."""
    return float(np.percentile(x, p, method=method))


def check_table(v: pd.DataFrame, e: pd.DataFrame) -> list[tuple]:
    gaps = [g for gs in e.gaps for g in gs]
    gc = Counter(gaps)
    n_v = len(v)
    lost = 1.0 - v.n_window / v.n_native.where(v.n_native > 0)
    pat = e.groupby("patient").size()
    folds = fold_of_eye()
    e = e.assign(fold=e.patient.map(folds))
    fold_med = e.groupby("fold").base_area_mm2.median()
    p90 = e[e.gaps.apply(lambda gs: 90 in gs)]
    rows = [
        ("eyes", "75", f"{len(e)}"),
        ("visits", "553", f"{n_v}"),
        ("intervals (windows)", "478", f"{len(gaps)}"),
        ("visits per eye min/median/max", "5 / 7 / 13",
         f"{e.n_visits.min()} / {e.n_visits.median():g} / {e.n_visits.max()}"),
        ("follow-up days min/median/max", "720 / 1080 / 2160",
         f"{e.span_days.min()} / {e.span_days.median():g} / {e.span_days.max()}"),
        ("patients; both eyes; one eye", "51; 24; 27",
         f"{len(pat)}; {(pat == 2).sum()}; {(pat == 1).sum()}"),
        ("eyes female / male", "47 / 28",
         f"{(e.sex == 'female').sum()} / {(e.sex == 'male').sum()}"),
        ("baseline age min-max, mean over eyes", "60.7-88.0, 76.4",
         f"{e.age.min():.1f}-{e.age.max():.1f}, {e.age.mean():.1f}"),
        ("distinct native shapes", "67", f"{v[['H', 'W']].drop_duplicates().shape[0]}"),
        ("native rows min-max", "38-66", f"{v.H.min()}-{v.H.max()}"),
        ("native columns min-max", "961-1719", f"{v.W.min()}-{v.W.max()}"),
        ("shape constant within each eye", "yes",
         "yes" if (v.groupby('eye')[['H', 'W']].nunique() == 1).all().all() else "NO"),
        ("visits row-padded / column-padded", "149 / 115",
         f"{int(v.row_pad.sum())} / {int(v.col_pad.sum())}"),
        ("visits whose lesion the crop cuts", "27.3 %",
         f"{(lost > 0).sum()}/{n_v} = {100 * (lost > 0).mean():.1f} %"),
        ("visits losing > 1 % of the lesion", "19.2 % (code-repo record)",
         f"{100 * (lost > 0.01).mean():.1f} %"),
        ("visits losing > 5 % of the lesion", "6.0 %",
         f"{(lost > 0.05).sum()}/{n_v} = {100 * (lost > 0.05).mean():.1f} %"),
        ("largest lesion fraction lost", "25.7 %", f"{100 * lost.max():.1f} %"),
        ("cropped lesions touching the border (pad-aware)", "31.1 %",
         f"{int(v.touch_valid.sum())}/{n_v} = {100 * v.touch_valid.mean():.1f} %"),
        ("  same, ring of the 49x1024 window (pad-blind)", "-",
         f"{100 * v.touch_window.mean():.1f} %"),
        ("lesions touching the native scan edge", "about 19 %",
         f"{100 * v.touch_native.mean():.1f} %"),
        ("mean pad fraction of the window", "1.4 % (code-repo record)",
         f"{100 * v.pad_frac.mean():.1f} %"),
        ("sqrt-area growth median [mm/yr]", "0.234", f"{e.growth_mm_yr.median():.3f}"),
        ("sqrt-area growth IQR [mm/yr]", "0.153-0.340",
         f"{q(e.growth_mm_yr, 25):.3f}-{q(e.growth_mm_yr, 75):.3f}"),
        ("sqrt-area growth p90 [mm/yr]", "0.473", f"{q(e.growth_mm_yr, 90):.3f}"),
        ("  same IQR / p90 with numpy 'linear' quantiles", "-",
         f"{q(e.growth_mm_yr, 25, 'linear'):.3f}-{q(e.growth_mm_yr, 75, 'linear'):.3f}"
         f" / {q(e.growth_mm_yr, 90, 'linear'):.3f}"),
        ("median baseline area fold 4 [mm2]", "about 4.1", f"{fold_med.loc[4]:.3f}"),
        ("median baseline area folds 0-3 [mm2]", "6.0-7.9",
         " / ".join(f"{fold_med.loc[k]:.2f}" for k in range(4))),
        ("eyes per fold (val)", "20/12/16/15/12",
         "/".join(str(int((e.fold == k).sum())) for k in range(5))),
        ("eyes with a 90-day interval; their patients", "10; 7",
         f"{len(p90)}; {p90.patient.nunique()}"),
    ]
    for d, (n, ne) in {90: (67, 10), 180: (364, 72), 270: (2, 2), 360: (38, 28),
                       540: (6, 5), 720: (1, 1)}.items():
        ne_m = int(e.gaps.apply(lambda gs: d in gs).sum())
        rows.append((f"interval {d} d: windows, share, eyes",
                     f"{n}, {100 * n / 478:.1f} %, {ne}",
                     f"{gc[d]}, {100 * gc[d] / len(gaps):.1f} %, {ne_m}"))
    rows.append(("interval values other than the six above", "none",
                 str(sorted(set(gc) - {90, 180, 270, 360, 540, 720})) or "none"))
    return rows


# --------------------------------------------------------------------------- figure
def main() -> None:
    pal = setup()
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator

    v = visit_table()
    e = eye_table(v)

    # raw-folder gaps must equal the precomputed gaps that cohort_visit_stats reads
    pg = precomp_gaps()
    mism = [k for k in e.eye if list(map(int, pg[k])) != list(map(int, e.set_index('eye').gaps[k]))]
    print(f"gap cross-check raw folder vs precompute: {len(pg)} eyes, {len(mism)} mismatches {mism[:5]}")

    rows = check_table(v, e)
    w = max(len(r[0]) for r in rows)
    print(f"\n{'statistic':<{w}}  {'text':<28}  computed")
    for r in rows:
        print(f"{r[0]:<{w}}  {r[1]:<28}  {r[2]}")

    gaps = np.array([g for gs in e.gaps for g in gs])
    med_g = float(np.median(e.growth_mm_yr))
    base = e.base_area_mm2.to_numpy()
    print(f"\nbaseline area (49x1024 grid) over 75 eyes: min {base.min():.2f}, "
          f"median {np.median(base):.2f}, IQR {q(base, 25):.2f}-{q(base, 75):.2f}, "
          f"max {base.max():.2f} mm2")
    nat = e.base_area_native_mm2.to_numpy()
    print(f"baseline area (native grid): median {np.median(nat):.2f}, "
          f"max {nat.max():.2f} mm2; window/native median ratio "
          f"{np.median(base / nat):.3f}")
    print(f"growth rate: min {e.growth_mm_yr.min():.3f}, max {e.growth_mm_yr.max():.3f}, "
          f"eyes with negative rate {(e.growth_mm_yr < 0).sum()}")

    blue, ink2, accent = pal.PAL["primary"], pal.PAL["ink_2"], pal.PAL["accent"]
    # exact page width (no tight bbox), so the figure is included at width=	extwidth
    # with 7-8 pt fonts at their nominal size
    plt.rcParams["savefig.bbox"] = "standard"
    fig, axs = plt.subplots(2, 2, figsize=pal.fig_size(1.0, 0.62), layout="constrained")
    fig.get_layout_engine().set(h_pad=0.04, w_pad=0.04, hspace=0.06, wspace=0.06)

    # (a) visits per eye
    ax = axs[0, 0]
    vc = e.n_visits.value_counts().sort_index()
    xs = np.arange(vc.index.min(), vc.index.max() + 1)
    ax.bar(xs, [vc.get(x, 0) for x in xs], width=0.7, color=blue)
    ax.set_xticks(xs)
    ax.set_xlabel("Visits per eye")
    ax.set_ylabel("Eyes")
    ax.set_yticks([0, 10, 20, 30])

    # (b) intervals between consecutive visits
    ax = axs[0, 1]
    gc = Counter(gaps.tolist())
    ds = [90, 180, 270, 360, 450, 540, 630, 720]
    cols = [accent if d == 180 else blue for d in ds]
    ax.bar(range(len(ds)), [gc.get(d, 0) for d in ds], width=0.7, color=cols)
    for i, d in enumerate(ds):
        if gc.get(d, 0):
            ax.text(i, gc[d] + 6, str(gc[d]), ha="center", va="bottom", fontsize=6.5,
                    color=pal.PAL["ink"])
    ax.set_xticks(range(len(ds)), [str(d) for d in ds])
    ax.set_xlabel("Interval between consecutive visits (d)")
    ax.set_ylabel("Intervals")
    ax.set_ylim(0, 410)

    # (c) baseline lesion area
    ax = axs[1, 0]
    bins = np.arange(0, np.ceil(base.max() / 2) * 2 + 2, 2)
    ax.hist(base, bins=bins, color=blue, edgecolor="white", linewidth=0.6)
    mb = float(np.median(base))
    ax.axvline(mb, color=pal.PAL["ink"], lw=0.9, ls="--")
    ax.set_ylim(0, ax.get_ylim()[1] * 1.15)
    ax.text(mb + 0.4, ax.get_ylim()[1] * 0.98, f"median {mb:.1f} mm²", fontsize=6.5,
            va="top", ha="left", color=pal.PAL["ink"])
    ax.set_xlabel("Baseline lesion area (mm²)")
    ax.set_ylabel("Eyes")
    ax.yaxis.set_major_locator(MaxNLocator(nbins=4, integer=True))

    # (d) square-root-area growth rate
    ax = axs[1, 1]
    gr = e.growth_mm_yr.to_numpy()
    lo = np.floor(gr.min() / 0.05) * 0.05
    bins = np.arange(lo, gr.max() + 0.05, 0.05)
    ax.hist(gr, bins=bins, color=blue, edgecolor="white", linewidth=0.6)
    ax.axvline(med_g, color=pal.PAL["ink"], lw=0.9, ls="--")
    ax.set_ylim(0, ax.get_ylim()[1] * 1.15)
    ax.text(med_g + 0.012, ax.get_ylim()[1] * 0.98, f"median {med_g:.3f} mm/yr",
            fontsize=6.5, va="top", ha="left", color=pal.PAL["ink"])
    ax.set_xlabel("Square-root-area growth rate (mm/yr)")
    ax.set_ylabel("Eyes")
    ax.yaxis.set_major_locator(MaxNLocator(nbins=4, integer=True))

    for ax, s in zip(axs.flat, "abcd"):
        ax.set_title(f"({s})", loc="left", fontsize=8, fontweight="bold", pad=3)
    save(fig, "fig_appendix_cohort")


if __name__ == "__main__":
    main()
