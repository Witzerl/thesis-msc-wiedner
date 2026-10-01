"""Appendix G, Figure fig:appendix:moved-mesh -- the canonical mesh mover on real GA lesions.

    cd images/scripts && python fig_appendix_moved_mesh.py

Loads the canonical data-free mesh mover (GA_NAT_O512x2_S1, seed 42, checkpoint_latest =
epoch 500, the one every dual-branch run loads) from the code repo, read-only, and evaluates
it on the baseline masks of three validation eyes of fold 2. Top row: the uniform
49 x 1024 lattice over the lesion; bottom row: the moved mesh over the same lesion. Both are
drawn at the physical aspect ratio (5.94 mm tall x 5.82 mm wide).

Ported from masterthesis-docker/practical/scripts/fig_mesh.py (same model loading, same
dmm_metrics functions), restyled to the thesis palette.

Drawn lines: every row of the lattice and every 21st column (0, 21, ..., 1008) plus the last
column (1023), so every drawn node is a lattice node and a drawn cell is about
0.12 x 0.12 mm (21 x 0.00568 mm = 0.119 mm across, 0.121 mm down).

Eye-selection rule (fixed before looking at any mesh): the 16 validation eyes of fold 2,
ordered by baseline lesion area on the 49 x 1024 grid; the nearest-rank lower quartile,
median and upper quartile, i.e. the 4th, 8th and 12th smallest.

Quality numbers per eye are computed with the code repo's dmm_metrics (edge band and
reference monitor with their default settings, the ones the in-training scorer uses).
The mesh mover was trained on all 478 masks of the cohort, so these meshes are in-sample.
Meshes and metrics are cached in images/data/moved_mesh_<eye>.npz.
"""
from __future__ import annotations

import gc
import math
import sys

import numpy as np

from _common import (setup, save, CODE, CACHE, PRECOMP, NROWS, NCOLS, DY_MM, DX_MM,
                     LX_MM, LY_MM)

MESH_DIR = CODE / "GraphPDE" / "mesh"
CKPT_GLOB = "experiments/GA_NAT_O512x2_S1/s42_*/ckpt/checkpoint_latest.pt"
FOLD = 2
STRIDE = int(round(NCOLS / NROWS))            # 21 columns ~ one row in mm
PIX_MM2 = DY_MM * DX_MM


def baseline_masks():
    """(eye_id, baseline binary mask (49, 1024)) for every validation eye of FOLD, exactly
    as dmm_dataloading._load_oct_masks_split builds a mask: channel 0 of x, denormalised
    with the precompute's z-score parameters and thresholded at 0.5."""
    import torch
    pre = PRECOMP[FOLD]
    meta = torch.load(pre / "meta_global.pt", weights_only=False)
    mu, sd = float(meta["norm_params"]["mean"][0]), float(meta["norm_params"]["std"][0])
    out = []
    for f in sorted((pre / "val").glob("sample_*.pt")):
        ws = torch.load(f, map_location="cpu", weights_only=False)
        ws = ws if isinstance(ws, list) else [ws]
        w0 = min(ws, key=lambda w: int(w["t0_steps"]))
        ch0 = w0["x"][0, :, 0].float().reshape(NROWS, NCOLS)
        out.append((str(w0["eye_id"]), ((ch0 * sd + mu) > 0.5).numpy()))
        del ws
    return out


def select(masks):
    """Nearest-rank lower quartile, median, upper quartile of baseline area."""
    ranked = sorted(masks, key=lambda t: t[1].sum())
    n = len(ranked)
    idx = [math.ceil(p * n) - 1 for p in (0.25, 0.5, 0.75)]
    print(f"fold-{FOLD} validation eyes by baseline area (mm2):")
    for i, (eye, m) in enumerate(ranked):
        tag = "  <- selected" if i in idx else ""
        print(f"  {i + 1:2d}. {eye:<14s} {m.sum() * PIX_MM2:6.2f}{tag}")
    return [ranked[i] for i in idx]


def load_dmm():
    import torch
    for p in (str(MESH_DIR), str(CODE)):        # CODE: the pickled args reference utils.*
        if p not in sys.path:
            sys.path.insert(0, p)
    from dmm_model import DMM
    hits = sorted(MESH_DIR.glob(CKPT_GLOB))
    if len(hits) != 1:
        raise SystemExit(f"expected one checkpoint for {CKPT_GLOB}, found {len(hits)}")
    ck = torch.load(hits[0], map_location="cpu", weights_only=False)
    a = ck["args"] if isinstance(ck["args"], dict) else vars(ck["args"])
    model = DMM(branch_layer=a["branch_layers"], trunk_layer=[2] + list(a["trunk_layers"]),
                out_layer=list(a["out_layers"]), Nx=NROWS, Ny=NCOLS, in_channels=1)
    model.load_state_dict({k: v for k, v in ck["model_state_dict"].items()
                           if ".fc0." not in k}, strict=True)
    model.eval()
    info = dict(path=hits[0], epoch=ck["epoch"], branch=a["branch_layers"],
                out_layers=a["out_layers"], sigma=a["monitor_mask_sigma"],
                n_params=sum(p.numel() for p in model.parameters()),
                stored=ck["metrics"]["mesh"])
    del ck
    gc.collect()
    return model, info


def mesh_for(model, eye, mask):
    """Moved mesh X1 (rows), X2 (columns) in xi in [0, 1] and quality numbers; cached."""
    import torch
    cache = CACHE / f"moved_mesh_{eye}.npz"
    if cache.exists():
        z = np.load(cache)
        if np.array_equal(z["mask"], mask):
            return z["X1"], z["X2"], {k: float(z[k]) for k in
                                      ("edge_gain", "tangled", "cov_ref", "det_min", "min_area_rel")}
    from dmm_metrics import (moved_mesh_grid, signed_cell_areas, edge_band_field, edge_gain,
                             reference_monitor, cov_against, min_det_sample)
    u1 = torch.from_numpy(mask.astype(np.float32))[None]          # (1, 49, 1024)
    X1, X2 = moved_mesh_grid(model, u1, NROWS, NCOLS, "cpu")
    A = signed_cell_areas(X1, X2)
    A0 = 1.0 / ((NROWS - 1) * (NCOLS - 1))
    gen = torch.Generator().manual_seed(12345)                     # MeshScorer's det seed
    det_min, _ = min_det_sample(model, u1, 5000, "cpu", generator=gen)
    q = dict(edge_gain=edge_gain(edge_band_field(u1), X1, X2),
             tangled=float((A <= 0).sum()),
             cov_ref=cov_against(reference_monitor(u1), X1, X2),
             det_min=float(det_min), min_area_rel=float(A.min() / A0))
    X1, X2 = X1.numpy(), X2.numpy()
    CACHE.mkdir(exist_ok=True)
    np.savez_compressed(cache, X1=X1, X2=X2, mask=mask, **q)
    return X1, X2, q


def to_mm(X1, X2):
    """xi -> mm, lattice node (i, j) at the centre of pixel (i, j) of the en-face image."""
    return (0.5 + X2 * (NCOLS - 1)) * DX_MM, (0.5 + X1 * (NROWS - 1)) * DY_MM


def mesh_segments(x, y):
    cols = list(range(0, NCOLS, STRIDE))
    if cols[-1] != NCOLS - 1:
        cols.append(NCOLS - 1)
    segs = [np.column_stack([x[i, cols], y[i, cols]]) for i in range(NROWS)]
    segs += [np.column_stack([x[:, j], y[:, j]]) for j in cols]
    return segs, len(cols)


def pad_extent(eye):
    """Zero-padded rows / columns of this eye in the 49 x 1024 window (from the raw shape)."""
    from fig_appendix_cohort import visit_table
    v = visit_table()
    H, W = (int(v[v.eye == eye].H.iloc[0]), int(v[v.eye == eye].W.iloc[0]))
    pads = []
    if H < NROWS:
        o = (NROWS - H) // 2
        pads += [("rows", 0, o), ("rows", o + H, NROWS)]
    if W < NCOLS:
        o = (NCOLS - W) // 2
        pads += [("cols", 0, o), ("cols", o + W, NCOLS)]
    return (H, W), [p for p in pads if p[2] > p[1]]


def main() -> None:
    pal = setup()
    import matplotlib.pyplot as plt
    from matplotlib.collections import LineCollection
    from matplotlib.colors import ListedColormap
    from matplotlib.patches import Rectangle

    chosen = select(baseline_masks())
    model, info = load_dmm()
    print(f"\nDMM {info['path'].parent.parent.name[:40]}..., epoch {info['epoch']}, branch "
          f"{info['branch']}, head {info['out_layers']}, sigma {info['sigma']}, "
          f"{info['n_params']:,} parameters")
    st = info["stored"]
    print(f"stored in-training scores at epoch {st['epoch'][-1]} (head-16 pool): edge gain "
          f"{st['edge_gain'][-1]:.4f}, tangled {st['tangled'][-1]}, cov_ref {st['cov_ref'][-1]:.4f},"
          f" det_min {st['det_min'][-1]:.4f}; max tangled over all {len(st['tangled'])} scored"
          f" epochs: {max(st['tangled'])}")

    meshes = []
    print(f"\n{'eye':<14s} {'area mm2':>8s} {'native':>10s} {'edge_gain':>9s} {'tangled':>7s} "
          f"{'cov_ref':>7s} {'det_min':>7s} {'min A/A0':>8s}  pads")
    for eye, m in chosen:
        X1, X2, q = mesh_for(model, eye, m)
        shape, pads = pad_extent(eye)
        meshes.append((eye, m, X1, X2, q, pads))
        print(f"{eye:<14s} {m.sum() * PIX_MM2:8.2f} {shape[0]:>4d}x{shape[1]:<5d} "
              f"{q['edge_gain']:9.3f} {int(q['tangled']):7d} {q['cov_ref']:7.3f} "
              f"{q['det_min']:7.3f} {q['min_area_rel']:8.3f}  {pads}")
    # displacement statistics, in mm, for the record
    for eye, m, X1, X2, q, _ in meshes:
        x, y = to_mm(X1, X2)
        x0, y0 = to_mm(*np.meshgrid(np.linspace(0, 1, NROWS), np.linspace(0, 1, NCOLS),
                                    indexing="ij"))
        d = np.hypot(x - x0, y - y0)
        print(f"{eye}: node displacement median {np.median(d):.3f} mm, max {d.max():.3f} mm; "
              f"max row shift {np.abs(y - y0).max() / DY_MM:.2f} rows, "
              f"max column shift {np.abs(x - x0).max() / DX_MM:.1f} columns")

    # ------------------------------------------------------------------ drawing
    plt.rcParams["savefig.bbox"] = "standard"
    fig, axs = plt.subplots(2, 3, figsize=pal.fig_size(1.0, 0.70), layout="constrained",
                            sharex=True, sharey=True)
    fig.get_layout_engine().set(w_pad=0.02, h_pad=0.02, wspace=0.03, hspace=0.03)
    lesion_cmap = ListedColormap([(0, 0, 0, 0), pal.MASK["gt"]])
    ext = (0.0, LX_MM, LY_MM, 0.0)
    gx, gy = to_mm(*np.meshgrid(np.linspace(0, 1, NROWS), np.linspace(0, 1, NCOLS),
                                indexing="ij"))
    for c, (eye, m, X1, X2, q, pads) in enumerate(meshes):
        for r in range(2):
            ax = axs[r, c]
            ax.imshow(m.astype(float), cmap=lesion_cmap, vmin=0, vmax=1, alpha=0.28,
                      extent=ext, interpolation="nearest", aspect="equal", zorder=1)
            ax.contour((np.arange(NCOLS) + 0.5) * DX_MM, (np.arange(NROWS) + 0.5) * DY_MM,
                       m.astype(float), levels=[0.5], colors=[pal.MASK["gt"]],
                       linewidths=0.8, zorder=3)
            for kind, a, b in pads:
                if kind == "rows":
                    rect = Rectangle((0, a * DY_MM), LX_MM, (b - a) * DY_MM)
                else:
                    rect = Rectangle((a * DX_MM, 0), (b - a) * DX_MM, LY_MM)
                rect.set(facecolor=pal.MASK["pad"], edgecolor=pal.PAL["muted"], hatch="////",
                         linewidth=0, zorder=0.5)
                ax.add_patch(rect)
            x, y = (gx, gy) if r == 0 else to_mm(X1, X2)
            segs, ncols_drawn = mesh_segments(x, y)
            ax.add_collection(LineCollection(
                segs, colors=pal.PAL["muted"] if r == 0 else pal.PAL["primary_700"],
                linewidths=0.28 if r == 0 else 0.3, zorder=2))
            ax.set_xlim(0, LX_MM)
            ax.set_ylim(LY_MM, 0)
            ax.set_aspect("equal")
            ax.grid(False)
            for s in ax.spines.values():
                s.set_visible(True)
                s.set_color(pal.PAL["line"])
            ax.set_xticks([0, 1, 2, 3, 4, 5])
            ax.set_yticks([0, 1, 2, 3, 4, 5])
        axs[0, c].set_title(f"({'abc'[c]})", loc="left", fontsize=8, fontweight="bold", pad=3)
        box = dict(boxstyle="square,pad=0.15", facecolor="white", edgecolor="none", alpha=0.85)
        axs[0, c].text(0.97, 0.965, f"lesion {m.sum() * PIX_MM2:.2f} mm²", transform=axs[0, c].transAxes,
                       ha="right", va="top", fontsize=6.5, color=pal.PAL["ink"], bbox=box, zorder=5)
        axs[1, c].text(0.97, 0.965, f"edge gain {q['edge_gain']:.2f}", transform=axs[1, c].transAxes,
                       ha="right", va="top", fontsize=6.5, color=pal.PAL["ink"], bbox=box, zorder=5)
    axs[0, 0].set_ylabel("Uniform grid\n(mm)")
    axs[1, 0].set_ylabel("Moved mesh\n(mm)")
    for c in range(3):
        axs[1, c].set_xlabel("mm")
    print(f"\ndrawn: {NROWS} rows x {ncols_drawn} columns (stride {STRIDE}, plus column {NCOLS - 1})")
    save(fig, "fig_appendix_moved_mesh", raster=True)


if __name__ == "__main__":
    main()
