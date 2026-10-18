"""Numbers for the fold section of Chapter 5 (exploratory analysis, no figure). Parts: fold level
(part0), graph networks vs the other operators (main body, part1_within), dense vs local operators
(part2), predicted / true new atrophy (part3). Original question:
folds 1 and 4?

Deficit per eye = (graph network) - mean(T-FEN, U-Net, FNO), per-eye growth-region Dice at the
one-year anchor, late-epoch mean (thesis_numbers.eye_late), averaged over seeds 42 and 7.

(a) Eye properties, from the raw masks (data/MUW_GA/scans/<eye>/<day>/mask_oct.png), centre-
    cropped / zero-padded to 49 x 1024 like tools/precompute_graphs_ga.py:
      area      baseline lesion area (mm^2)
      pieces    connected components of the baseline lesion >= 0.02 mm^2 (8-connectivity)
      irreg     perimeter / perimeter of a circle of equal area (1 = circle), physical units
      edge      baseline or one-year lesion touches the window edge
      far       fraction of the new atrophy at one year lying > REACH_MM from the baseline lesion
                (two message-passing rounds of the dilated stencil reach about 0.24 mm)
      grow      new atrophy at one year (mm^2)
(b) Training set vs eyes: if the fold-1 and fold-4 models are weaker because of their training
    sets, the deficit should be a shift shared by most validation eyes of those folds; if certain
    eyes carry it, it should be concentrated in a few eyes and follow their properties. Checked by
    the per-fold distribution of the per-eye deficit and by a regression of the deficit on the
    eye properties plus a fold-1/4 indicator.

Eye order: validation eyes are the sorted eye ids of the fold's validation patients
(precompute_graphs_ga.py assign_eyes_to_splits); verified against the baseline area in the
per-eye records of every fold.
Run from images/scripts/:  python _analysis_gnn_folds.py
"""
import json
import os

import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.stats import spearmanr, mannwhitneyu

from _common import thesis_numbers, CODE

DY, DX = 0.12118, 0.00568
H, W = 49, 1024
REACH_MM = 0.24
MIN_PIECE_MM2 = 0.02
SCANS = CODE / "data" / "MUW_GA" / "scans"
SPLITS = CODE / "data" / "MUW_GA" / "splits"
F = list(range(5))
RUNS = {42: dict(tfen="FEN_final_w96ftp7rk4d45skew", stencil="ANISOGNN_final_dilmean",
                 unet="UNET_final_w5", fno="FNO_final_w5", knn="MPPDE_final_aggrmean"),
        7: dict(tfen="FEN_final_w96ftp7rk4d45skews7", stencil="ANISOGNN_final_dilmeans7",
                unet="UNET_final_w5s7", fno="FNO_final_w5s7", knn="MPPDE_final_aggrmeans7")}


def crop(m):
    out = np.zeros((H, W), bool)
    h, w = m.shape
    sh, dh = ((slice((h - H) // 2, (h - H) // 2 + H), slice(0, H)) if h >= H
              else (slice(0, h), slice((H - h) // 2, (H - h) // 2 + h)))
    sw, dw = ((slice((w - W) // 2, (w - W) // 2 + W), slice(0, W)) if w >= W
              else (slice(0, w), slice((W - w) // 2, (W - w) // 2 + w)))
    out[dh, dw] = m[sh, sw]
    return out


def visits(eye):
    d = SCANS / eye
    out = []
    for name in os.listdir(d):
        try:
            t = float(name)
        except ValueError:
            continue
        if (d / name / "mask_oct.png").exists() and (d / name / "layers_oct.npz.npy").exists():
            out.append((t, d / name))
    return sorted(out)


def mask(vdir):
    return crop(np.array(Image.open(vdir / "mask_oct.png")) > 0)


def perimeter(m):
    """Physical boundary length: column-direction boundaries have length DY, row-direction DX."""
    p = np.pad(m, 1)
    return (np.abs(np.diff(p, axis=1)).sum() * DY + np.abs(np.diff(p, axis=0)).sum() * DX)


def features(eye):
    v = visits(eye)
    b = mask(v[0][1])
    one = next(vd for t, vd in v if t >= 0.95 * 365 - 1e-6)
    g = mask(one)
    area = b.sum() * DX * DY
    lab, n = ndimage.label(b, structure=np.ones((3, 3)))
    sizes = ndimage.sum(b, lab, range(1, n + 1)) * DX * DY
    pieces = int((sizes >= MIN_PIECE_MM2).sum())
    irreg = perimeter(b) / (2 * np.sqrt(np.pi * area)) if area > 0 else np.nan
    edge = any(m[0].any() or m[-1].any() or m[:, 0].any() or m[:, -1].any() for m in (b, g))
    new = g & ~b
    dist = ndimage.distance_transform_edt(~b, sampling=(DY, DX))
    far = (dist[new] > REACH_MM).mean() if new.any() else 0.0
    return dict(area=area, pieces=pieces, irreg=irreg, edge=float(edge), far=far,
                grow=new.sum() * DX * DY)


def eye_ids(tn):
    """{(fold, eye_idx): eye id}: sorted eye ids of the fold's validation patients, each
    checked against the baseline area logged in the per-eye records."""
    eye_id = {}
    for f in F:
        sp = json.load(open(SPLITS / f"split_{f}.json"))
        val = sorted(e for e in os.listdir(SCANS)
                     if e.rsplit("_", 1)[0] in set(sp["val_ids"]) and len(visits(e)) >= 2)
        rec = json.load(open(os.path.join(tn.run_dir(RUNS[42]["stencil"], f), "mai",
                                          "epoch_0029.json")))
        logged = {p["eye_idx"]: p["baseline_area_mm2"] for p in rec["per_eye"]}
        assert len(val) == len(logged), (f, len(val), len(logged))
        for i, e in enumerate(val):
            a = mask(visits(e)[0][1]).sum() * DX * DY
            assert abs(a - logged[i]) < 1e-3 * max(1, logged[i]), (f, i, e, a, logged[i])
            eye_id[(f, i)] = e
    return eye_id


def main():
    tn = thesis_numbers()
    # eye ids per fold, checked against the logged baseline areas
    eye_id = {}
    for f in F:
        sp = json.load(open(SPLITS / f"split_{f}.json"))
        val = sorted(e for e in os.listdir(SCANS)
                     if e.rsplit("_", 1)[0] in set(sp["val_ids"]) and len(visits(e)) >= 2)
        rec = json.load(open(os.path.join(tn.run_dir(RUNS[42]["stencil"], f), "mai",
                                          "epoch_0029.json")))
        logged = {p["eye_idx"]: p["baseline_area_mm2"] for p in rec["per_eye"]}
        assert len(val) == len(logged), (f, len(val), len(logged))
        for i, e in enumerate(val):
            a = mask(visits(e)[0][1]).sum() * DX * DY
            assert abs(a - logged[i]) < 1e-3 * max(1, logged[i]), (f, i, e, a, logged[i])
            eye_id[(f, i)] = e
    print(f"eye ids verified against logged baseline areas: {len(eye_id)} eyes")

    E = {s: {k: tn.eye_late(r, F) for k, r in A.items()} for s, A in RUNS.items()}
    keys = sorted(eye_id)
    def deficit(g, k):
        return np.mean([E[s][g][k] - np.mean([E[s][o][k] for o in ("tfen", "unet", "fno")])
                        for s in RUNS])
    X = {k: features(eye_id[k]) for k in keys}
    fo = np.array([k[0] for k in keys])
    in14 = np.isin(fo, [1, 4])
    names = ["area", "pieces", "irreg", "edge", "far", "grow"]

    print("\nEye properties per fold (median; edge = share of eyes; pieces = share with >= 2)")
    print("fold eyes  area   pieces>=2  irreg  edge   far    grow")
    for f in F:
        m = fo == f
        P = [X[k] for k, mm in zip(keys, m) if mm]
        print(f" {f}    {m.sum():2d}  {np.median([p['area'] for p in P]):5.2f}   "
              f"{np.mean([p['pieces'] >= 2 for p in P]):.2f}      "
              f"{np.median([p['irreg'] for p in P]):.2f}   {np.mean([p['edge'] for p in P]):.2f}   "
              f"{np.median([p['far'] for p in P]):.3f}  {np.median([p['grow'] for p in P]):.2f}")
    print("folds 1+4 vs 0,2,3 (Mann-Whitney p): " + ", ".join(
        f"{n} {mannwhitneyu([X[k][n] for k, m in zip(keys, in14) if m], [X[k][n] for k, m in zip(keys, in14) if not m]).pvalue:.2f}"
        for n in names))

    for g in ("stencil", "knn"):
        d = np.array([deficit(g, k) for k in keys])
        print(f"\n=== {g}: deficit to the non-graph operators, per eye (seeds averaged) ===")
        print("(a) Spearman correlation of the deficit with each eye property (n = 75):")
        for n in names:
            x = np.array([X[k][n] for k in keys])
            r = spearmanr(x, d)
            print(f"    {n:7s} rho {r[0]:+.2f}  p {r[1]:.3f}")
        print("(b) per-fold distribution of the deficit:")
        for f in F:
            m = fo == f
            print(f"    fold {f}: mean {d[m].mean():+.3f}  median {np.median(d[m]):+.3f}  "
                  f"eyes below 0: {(d[m] < 0).sum()}/{m.sum()}  "
                  f"lowest three: {', '.join(f'{x:+.2f}' for x in np.sort(d[m])[:3])}")
        # regression: deficit ~ properties + fold-1/4 indicator
        Z = np.column_stack([np.ones(len(keys))] +
                            [(np.array([X[k][n] for k in keys]) - np.mean([X[k][n] for k in keys]))
                             / np.std([X[k][n] for k in keys]) for n in names] +
                            [in14.astype(float)])
        beta, res, *_ = np.linalg.lstsq(Z, d, rcond=None)
        resid = d - Z @ beta
        s2 = resid @ resid / (len(d) - Z.shape[1])
        se = np.sqrt(np.diag(s2 * np.linalg.inv(Z.T @ Z)))
        lab = ["const"] + names + ["fold1or4"]
        print("    regression (properties standardised): " +
              ", ".join(f"{l} {b:+.3f} (t {b / s:+.1f})" for l, b, s in zip(lab, beta, se)))
        m0 = d[in14].mean() - d[~in14].mean()
        print(f"    fold-1/4 gap without properties {m0:+.3f}; with properties {beta[-1]:+.3f}")

    part0(tn, eye_id, X)
    part1_within(tn, eye_id, X)
    part2(tn, eye_id, X)
    part3(tn, eye_id)
    part4(tn, eye_id, X)
    part5(tn, eye_id, X)
    far_terciles(tn, eye_id, X, verbose=True)


def pred_true_ratio(tn, keys, op):
    """Per-eye predicted / true new atrophy at the anchor, late-epoch mean, seeds averaged."""
    v = []
    for s, R in RUNS.items():
        pr = late_anchor(tn, R[op], "A_pred_growth_mm2")
        tr = late_anchor(tn, R[op], "A_true_growth_mm2")
        v.append([pr[k] / tr[k] if tr[k] > 0 else np.nan for k in keys])
    return np.nanmean(v, 0)


def part4(tn, eye_id, X):
    """Fold 4 and the graph networks: relative growth and the predicted amount of new atrophy."""
    keys = sorted(eye_id)
    E = {s: {k: tn.eye_late(r, F) for k, r in A.items()} for s, A in RUNS.items()}
    fo = np.array([k[0] for k in keys])
    rel = np.array([X[k]["grow"] / X[k]["area"] if X[k]["area"] > 0 else np.nan for k in keys])
    ratio = {op: pred_true_ratio(tn, keys, op) for op in RUNS[42]}
    d = np.array([stencil_minus_others(E, k) for k in keys])
    ok = ~np.isnan(rel) & ~np.isnan(ratio["stencil"])
    print("\n=== Part 4: relative growth (new atrophy at the anchor / baseline area) ===")
    print("  median per fold: " + ", ".join(f"{f} {np.nanmedian(rel[fo == f]):.2f}" for f in F))
    print("  median predicted / true per fold (seeds averaged):")
    for op in ratio:
        print(f"    {op:8s} " + " ".join(f"{np.nanmedian(ratio[op][fo == f]):.2f}" for f in F))
    for op in ratio:
        r = spearmanr(rel[ok], ratio[op][ok])
        print(f"  {op:8s} predicted / true vs relative growth: rho {r[0]:+.2f} (p {r[1]:.4f})")
    r = spearmanr(rel[ok], (ratio["stencil"] - ratio["fno"])[ok])
    print(f"  stencil minus FNO (predicted / true) vs relative growth: rho {r[0]:+.2f} (p {r[1]:.3f})")
    q = np.nanpercentile(rel, [100 / 3, 200 / 3])
    grp = np.digitize(rel, q)
    print(f"  thirds of relative growth: <= {q[0]:.2f}, {q[0]:.2f}-{q[1]:.2f}, > {q[1]:.2f}")
    for g, nm in enumerate(("low", "mid", "high")):
        m = (grp == g) & ok
        print(f"    {nm:4s} n {m.sum():2d}: " + ", ".join(
            f"{op} {np.median(ratio[op][m]):.2f}" for op in ratio) + f"; stencil minus others {d[m].mean():+.3f}")
    m = (fo == 4) & ok
    r = spearmanr((ratio["stencil"] - ratio["fno"])[m], d[m])
    print(f"  within fold 4: stencil deficit vs (stencil minus FNO) predicted / true: "
          f"rho {r[0]:+.2f} (p {r[1]:.4f}), n {m.sum()}")


def part5(tn, eye_id, X):
    """Fold 3 and the dense operators: distance of the new atrophy, lesion size."""
    keys = sorted(eye_id)
    E = {s: {k: tn.eye_late(r, F) for k, r in A.items()} for s, A in RUNS.items()}
    fo = np.array([k[0] for k in keys])
    far = np.array([X[k]["far"] for k in keys])
    edge = np.array([X[k]["edge"] for k in keys])
    d = np.array([dense_minus_local(E, k) for k in keys])
    low = far <= np.median(far)
    print("\n=== Part 5: fold 3 and the dense operators ===")
    print(f"  dense minus local, far share at or below the median / above: "
          f"{d[low].mean():+.3f} ({low.sum()}) / {d[~low].mean():+.3f} ({(~low).sum()})")
    print("  share of eyes with low far share per fold: " +
          ", ".join(f"{f} {low[fo == f].mean():.2f}" for f in F))
    m = fo == 3
    ks = [k for k in keys if k[0] == 3]
    for k in sorted(ks, key=lambda k: X[k]["area"])[:2]:
        print(f"  fold 3 smallest lesion {eye_id[k]}: area {X[k]['area']:.2f} mm^2, dense minus local "
              f"seed 42 {dense_minus_local(E, k, (42,)):+.3f}, seed 7 {dense_minus_local(E, k, (7,)):+.3f}")
    order = np.argsort(d[m])
    print("  fold 3 ranks of the deficit (1 = largest): " + ", ".join(
        f"{eye_id[ks[i]]} {r + 1}" for r, i in enumerate(order[:4])))
    Z = np.column_stack([np.ones(len(keys)), (far - far.mean()) / far.std(),
                         (edge - edge.mean()) / edge.std(), m.astype(float)])
    b, *_ = np.linalg.lstsq(Z, d, rcond=None)
    print(f"  fold-3 gap {d[m].mean() - d[~m].mean():+.3f} raw, {b[3]:+.3f} after far share and edge contact")


def far_terciles(tn, eye_id, X, verbose=False):
    """Stencil GNN minus the non-graph operators per third of the far share: mean and SE."""
    keys = sorted(eye_id)
    E = {s: {k: tn.eye_late(r, F) for k, r in A.items()} for s, A in RUNS.items()}
    far = np.array([X[k]["far"] for k in keys])
    d = np.array([stencil_minus_others(E, k) for k in keys])
    q = np.percentile(far, [100 / 3, 200 / 3])
    grp = np.digitize(far, q, right=True)
    out = []
    for g in range(3):
        m = grp == g
        out.append((d[m].mean(), d[m].std(ddof=1) / np.sqrt(m.sum()), m.sum(),
                    far[m].min(), far[m].max()))
    if verbose:
        print("\n=== Far-share thirds (figure): stencil minus non-graph operators ===")
        for (mu, se, n, lo, hi), nm in zip(out, ("low", "mid", "high")):
            print(f"  {nm:4s} n {n:2d}, far share {lo:.2f}-{hi:.2f}: {mu:+.3f} +/- {se:.3f} SE")
        r = spearmanr(far, d)
        print(f"  rho over all eyes {r[0]:+.2f} (p {r[1]:.4f})")
    return out


def stencil_minus_others(E, k, seeds=tuple(RUNS)):
    return np.mean([E[s]["stencil"][k] - np.mean([E[s][o][k] for o in ("tfen", "unet", "fno")])
                    for s in seeds])


def dense_minus_local(E, k, seeds=tuple(RUNS)):
    return np.mean([np.mean([E[s][o][k] for o in ("unet", "fno")]) -
                    np.mean([E[s][o][k] for o in ("stencil", "tfen")]) for s in seeds])


def part0(tn, eye_id, X):
    """Fold level: canonical model (seed 42), per-eye growth-region Dice vs area and rate."""
    keys = sorted(eye_id)
    dg = tn.eye_late(RUNS[42]["stencil"], F)
    d = np.array([dg[k] for k in keys])
    rate = {}
    for f in F:
        r = json.load(open(os.path.join(tn.run_dir(RUNS[42]["stencil"], f), "mai",
                                        "epoch_0029.json")))
        for p in r["per_eye"]:
            rate[(f, p["eye_idx"])] = p["growth_rate_true_mm_per_year"]
    rate = np.array([rate[k] for k in keys])
    area = np.array([X[k]["area"] for k in keys])
    fo = np.array([k[0] for k in keys])
    print("\n=== Part 0: fold level (canonical model, seed 42, per-eye growth-region Dice) ===")
    for f in F:
        m = fo == f
        print(f"  fold {f}: eyes {m.sum():2d}, mean Dice {d[m].mean():.3f}, median area "
              f"{np.median(area[m]):.2f} mm^2, median sqrt growth rate {np.median(rate[m]):.3f} mm/y")
    for nm, x in (("baseline area", area), ("growth rate", rate)):
        r = spearmanr(x, d)
        print(f"  per-eye Dice vs {nm}: rho {r[0]:+.2f} (p {r[1]:.4f}), n {len(d)}")
    for s, A in RUNS.items():
        V = {k: [tn.fold_late(e, F)[f] for f in F] for k, e in A.items()}
        print(f"  seed {s}: highest fold per operator: " +
              ", ".join(f"{k} {int(np.argmax(v))}" for k, v in V.items()))


def part1_within(tn, eye_id, X):
    """Stencil GNN minus the non-graph operators against the far share, within each fold."""
    E = {s: {k: tn.eye_late(r, F) for k, r in A.items()} for s, A in RUNS.items()}
    keys = sorted(eye_id)
    far = np.array([X[k]["far"] for k in keys])
    d = np.array([stencil_minus_others(E, k) for k in keys])
    fo = np.array([k[0] for k in keys])
    hi = far > np.median(far)
    print("\n=== Part 1b: stencil GNN minus non-graph operators vs far share ===")
    print(f"  median far share {np.median(far):.3f}; deficit above / below the median: "
          f"{d[hi].mean():+.3f} ({hi.sum()} eyes) / {d[~hi].mean():+.3f} ({(~hi).sum()} eyes)")
    for f in F:
        m = fo == f
        r = spearmanr(far[m], d[m])
        print(f"  within fold {f}: rho {r[0]:+.2f} (p {r[1]:.2f}), n {m.sum()}, "
              f"median far {np.median(far[m]):.3f}")
    ks = [k for k in keys if k[0] == 1]
    for k in sorted(ks, key=lambda k: stencil_minus_others(E, k))[:3]:
        print(f"    fold 1: {eye_id[k]:<12s} far {X[k]['far']:.2f}  deficit seed 42 "
              f"{stencil_minus_others(E, k, (42,)):+.3f}, seed 7 {stencil_minus_others(E, k, (7,)):+.3f}"
              f"  new atrophy {X[k]['grow']:.2f} mm^2")


def part2(tn, eye_id, X):
    """Dense operators (U-Net, FNO) minus local ones (stencil GNN, T-FEN)."""
    E = {s: {k: tn.eye_late(r, F) for k, r in A.items()} for s, A in RUNS.items()}
    keys = sorted(eye_id)
    d = np.array([dense_minus_local(E, k) for k in keys])
    fo = np.array([k[0] for k in keys])
    print("\n=== Part 2: dense (U-Net, FNO) minus local (stencil GNN, T-FEN), per eye ===")
    for f in F:
        m = fo == f
        ks = [k for k, mm in zip(keys, m) if mm]
        print(f"  fold {f}: mean {d[m].mean():+.3f}  median {np.median(d[m]):+.3f}  "
              f"eyes below 0: {(d[m] < 0).sum()}/{m.sum()}  (seed 42 "
              f"{np.mean([dense_minus_local(E, k, (42,)) for k in ks]):+.3f}, seed 7 "
              f"{np.mean([dense_minus_local(E, k, (7,)) for k in ks]):+.3f})")
    for n in ["area", "pieces", "irreg", "edge", "far", "grow"]:
        x = np.array([X[k][n] for k in keys])
        r = spearmanr(x, d)
        print(f"  vs {n:7s} rho {r[0]:+.2f}  p {r[1]:.3f}")
    e = np.array([X[k]["edge"] for k in keys]) > 0
    print(f"  edge contact: {d[e].mean():+.3f} ({e.sum()} eyes) vs no contact "
          f"{d[~e].mean():+.3f} ({(~e).sum()} eyes)")
    print("  edge share per fold: " + ", ".join(
        f"{f} {np.mean([X[k]['edge'] for k in keys if k[0] == f]):.2f}" for f in F))


def late_anchor(tn, run, key):
    """{(fold, eye): late-epoch mean of a per-step quantity at the one-year anchor step}."""
    out = {}
    for f in F:
        rd = tn.run_dir(run, f)
        acc = {}
        for ep in range(10, 30):
            d = json.load(open(os.path.join(rd, "mai", f"epoch_{ep:04d}.json")))
            by = {}
            for st in d["per_step"]:
                by.setdefault(st["eye_idx"], []).append(st)
            for eye, st in by.items():
                st = sorted(st, key=lambda x: x["step_idx"])
                a = [x for x in st if x["cum_dt_years"] * 365 >= 0.95 * 365 - 1e-6][0]
                acc.setdefault(eye, []).append(a[key])
        for eye, v in acc.items():
            out[(f, eye)] = float(np.mean(v))
    return out


def part3(tn, eye_id):
    keys = sorted(eye_id)
    print("\n=== Part 3: median predicted / true new atrophy at the anchor, per fold ===")
    for s, A in RUNS.items():
        print(f"  seed {s}")
        for op, run in A.items():
            pr = late_anchor(tn, run, "A_pred_growth_mm2")
            tr = late_anchor(tn, run, "A_true_growth_mm2")
            row = [np.median([pr[k] / tr[k] for k in keys if k[0] == f and tr[k] > 0]) for f in F]
            print(f"    {op:8s} " + " ".join(f"{x:.2f}" for x in row))


if __name__ == "__main__":
    main()
