"""Chapter 3, Figure fig:data:example-state -- one visit of the MUW cohort.

    cd images/scripts && python fig_data_example_state.py

Panels (one visit, PEAT0058_OD day 360, chosen by the author 2026-10-20 from six candidates:
the visits whose deepest ILM pixels, as many as the lesion has, overlap the lesion best
(Dice 0.87; cohort median 0.64), lesion not touching the window edge):
  (a) FAF image (faf_global.png) and (b) near-infrared SLO image (slo_global.png), each
      contrast-stretched on its own (1st-99th percentile), with the 49 x 1024 modelling
      window drawn through the visit's T_mask (as in fig_bg_ga_faf.py) and the outline of
      the GA mask in the global frame (mask_global.png). Both are shown because the
      lesion looks different on the two: bright on the SLO, dark on FAF, where it was
      annotated; other bright spots on the SLO are not part of the annotation
      (median brightness inside / in a 30 px ring: SLO 88 / 62, FAF 25 / 47);
  (c) channel 0, the binary GA mask on the 49 x 1024 modelling grid (centre crop /
      zero pad of mask_oct.png, same arithmetic as the precompute), at the physical
      aspect ratio, nearest-neighbour, so the tall thin pixels are visible;
  (d) channel 1, the ILM depth map (axial pixel index), on the same grid, with the
      lesion outline of (c).
Hatched: positions without data -- zero padding of the crop (all channels) and, in (d),
positions where the stored layer value is 0 (no segmentation at this visit).

Source (read-only): data/MUW_GA/scans/<EYE>/<DAY>/{slo_global.png, mask_global.png,
mask_oct.png, layers_oct.npz.npy, oct.transform.json}.
Frame checks: T_mask maps native OCT (row, col) to global (row, col) (checked for
fig_bg_ga_faf.py); slo_global and mask_global share the 768 x 768 global frame
(slo.transform.json: transform_reg = identity); mask_global sampled through T_mask
reproduces mask_oct (printed below as IoU).
"""
from __future__ import annotations

import json

import numpy as np
from PIL import Image

from _common import setup, save, panel_label, SCANS, NROWS, NCOLS, LX_MM, LY_MM, EXTENT
from fig_appendix_cohort import _crop_slices
from fig_bg_ga_faf import window_global, stretch

EYE, DAY = "PEAT0058_OD", 360
CHANNEL = 1            # ILM (most superficial boundary)
MARGIN_MM = 0.4


def to_window(a: np.ndarray, fill=0):
    """Centre crop / zero pad a native (H, W, ...) array to the 49 x 1024 window;
    also return the boolean 'inside the native scan' mask."""
    H, W = a.shape[:2]
    (sh, dh), (sw, dw) = _crop_slices(H, NROWS), _crop_slices(W, NCOLS)
    out = np.full((NROWS, NCOLS) + a.shape[2:], fill, dtype=a.dtype)
    out[dh, dw] = a[sh, sw]
    inside = np.zeros((NROWS, NCOLS), bool)
    inside[dh, dw] = True
    return out, inside


def check_iou(vd) -> float:
    T = np.array(json.loads((vd / "oct.transform.json").read_text())["T_mask"])
    m_oct = np.asarray(Image.open(vd / "mask_oct.png")) > 127
    m_glb = np.asarray(Image.open(vd / "mask_global.png")) > 127
    r, c = np.mgrid[0:m_oct.shape[0], 0:m_oct.shape[1]]
    gr = np.clip(np.rint(T[0, 0] * r + T[0, 2]).astype(int), 0, m_glb.shape[0] - 1)
    gc = np.clip(np.rint(T[1, 1] * c + T[1, 2]).astype(int), 0, m_glb.shape[1] - 1)
    s = m_glb[gr, gc]
    return (s & m_oct).sum() / max((s | m_oct).sum(), 1)


def hatch(ax, nodata: np.ndarray, pal) -> None:
    """Grey hatch over the positions where `nodata` is True (window coordinates)."""
    if not nodata.any():
        return
    ax.contourf(np.linspace(0, LX_MM, NCOLS), np.linspace(0, LY_MM, NROWS),
                nodata.astype(float), levels=[0.5, 1.5], colors=[pal.MASK["pad"]],
                hatches=["////"], zorder=3)


def main():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    pal = setup()
    mpl.rcParams["hatch.color"] = pal.PAL["muted"]
    mpl.rcParams["hatch.linewidth"] = 0.5
    vd = SCANS / EYE / str(DAY)

    slo = np.asarray(Image.open(vd / "slo_global.png").convert("L")).astype(float)
    faf = np.asarray(Image.open(vd / "faf_global.png").convert("L")).astype(float)
    m_glb = np.asarray(Image.open(vd / "mask_global.png")) > 127
    m_oct = np.asarray(Image.open(vd / "mask_oct.png")) > 127
    layers = np.load(vd / "layers_oct.npz.npy").astype(float)
    print(f"{EYE} day {DAY}: native grid {m_oct.shape}, IoU(mask_global via T_mask, "
          f"mask_oct) = {check_iou(vd):.4f}")

    mask_w, inside = to_window(m_oct.astype(np.uint8))
    depth_w, _ = to_window(layers[..., CHANNEL - 1])
    nodata_layer = inside & (depth_w == 0)
    print(f"window: {(~inside).mean():.1%} zero pad, {nodata_layer.mean():.1%} inside the "
          f"scan without a layer value; lesion {mask_w.sum()} px")

    fig = plt.figure(figsize=pal.fig_size(1.0, 0.33))
    gs = fig.add_gridspec(2, 4, height_ratios=[1, 0.05], left=0.005, right=0.995,
                          top=0.92, bottom=0.13, wspace=0.10, hspace=0.12)
    axf, axs, axb, axc = (fig.add_subplot(gs[0, k]) for k in range(4))
    cax = fig.add_subplot(gs[1, 3])
    lesion = pal.PAL["accent"]

    # (a) FAF and (b) SLO with the modelling window and the lesion outline
    (rr, cc), py, px = window_global(vd)
    mr, mc = MARGIN_MM / py, MARGIN_MM / px
    R0, R1 = int(max(rr[0] - mr, 0)), int(min(rr[1] + mr, slo.shape[0]))
    C0, C1 = int(max(cc[0] - mc, 0)), int(min(cc[1] + mc, slo.shape[1]))
    ext = ((C0 - cc[0]) * px, (C1 - cc[0]) * px, (R1 - rr[0]) * py, (R0 - rr[0]) * py)
    gy = (np.arange(R0, R1) - rr[0]) * py
    gx = (np.arange(C0, C1) - cc[0]) * px
    for ax, img in ((axs, slo), (axf, faf)):
        ax.imshow(stretch(img[R0:R1, C0:C1]), cmap="gray", vmin=0, vmax=1, extent=ext,
                  interpolation="lanczos")
        ax.contour(gx, gy, m_glb[R0:R1, C0:C1].astype(float), levels=[0.5],
                   colors=[lesion], linewidths=0.9)
        rect = dict(xy=(0, 0), width=(cc[1] - cc[0]) * px, height=(rr[1] - rr[0]) * py,
                    fill=False)
        ax.add_patch(mpatches.Rectangle(**rect, ec="white", lw=2.2))
        ax.add_patch(mpatches.Rectangle(**rect, ec=pal.PAL["primary"], lw=1.2, ls=(0, (4, 3))))
        ax.set_xlim(ext[0], ext[1]); ax.set_ylim(ext[2], ext[3])
        ax.set_axis_off()

    # (b) channel 0 on the modelling grid, nearest neighbour, physical aspect
    cmap_mask = mpl.colors.ListedColormap(["white", pal.MASK["gt"]])
    axb.imshow(mask_w, cmap=cmap_mask, vmin=0, vmax=1, extent=EXTENT,
               interpolation="nearest", aspect="equal")
    hatch(axb, ~inside, pal)

    # (c) ILM depth map with the lesion outline
    d = np.ma.masked_where(depth_w == 0, depth_w)
    lo, hi = np.percentile(depth_w[depth_w > 0], [1, 99])
    im = axc.imshow(d, cmap=pal.cmap_seq(), vmin=lo, vmax=hi, extent=EXTENT,
                    interpolation="nearest", aspect="equal")
    hatch(axc, depth_w == 0, pal)
    xs = np.linspace(0, LX_MM, NCOLS); ys = np.linspace(0, LY_MM, NROWS)
    axc.contour(xs, ys, mask_w.astype(float), levels=[0.5], colors=["white"], linewidths=2.2)
    axc.contour(xs, ys, mask_w.astype(float), levels=[0.5], colors=[lesion], linewidths=1.0)
    cb = fig.colorbar(im, cax=cax, orientation="horizontal")
    cb.set_label("depth (axial pixels)", fontsize=6.5)
    cb.ax.tick_params(labelsize=6.5, length=2)
    cb.outline.set_edgecolor(pal.PAL["line"])

    for ax in (axb, axc):
        ax.set_xlim(0, LX_MM); ax.set_ylim(LY_MM, 0)
        ax.grid(False)
        for s in ax.spines.values():
            s.set_visible(True); s.set_edgecolor(pal.PAL["line"])
        ax.set_xticks([]); ax.set_yticks([])
    titles = ("FAF", "Near-infrared SLO", "Binary GA mask", "ILM depth map")
    for ax, s, t in zip((axf, axs, axb, axc), "abcd", titles):
        panel_label(ax, f"({s}) {t}", x=0.0, y=1.01)
        ax.texts[-1].set_fontsize(8)
        ax.texts[-1].set_ha("left")

    save(fig, "fig_data_example_state", raster=True)
    plt.close(fig)


if __name__ == "__main__":
    main()
