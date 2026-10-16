"""Figure 2.2 (fig:bg:oct-acquisition): how OCT measures a depth profile and builds a volume.

(a) Measuring principle. Input: images/raw/fig_bg_oct_acquisition_raw_interferometer.png
    (1672 x 941 px, ChatGPT image generation, no text; read-only backup, never modified):
    light source, beam splitter, reference mirror, eye, detector. Added here: labels and a
    schematic A-scan (reflectivity against depth) in the empty area right of the detector.
    Anchors in raw pixels, read off a gridded render: light source box x 73-248, y 400-490;
    beam splitter x 518-660, y 373-512; mirror x 490-688, y 122-148; detector x 497-680,
    y 732-830; eye wall x ~980-1430, y ~240-650; free area x ~720-1180, y ~660-900.
    The A-scan curve is schematic (a sum of Gaussian peaks), not data.

(b) Scan geometry, drawn here in cabinet projection: a block of retina whose front and right
    faces carry the flat ends of the healthy layer strip of Figure 2.3
    (images/raw/fig_bg_retinal_anatomy_raw_healthy.png, rows 108-658 = RNFL to sclera, columns
    0-650 and 1522-2172). Top face = en-face view with scan lines parallel to the front edge (one
    line per B-scan) and a lesion; front face = one B-scan; orange line = one A-scan; the block =
    the volume. Footprint ~6 x 6 mm as stated for the MUW cohort in Section 2.1.2; heights are
    not to scale.

Output: images/fig_bg_oct_acquisition.pdf (include at width=\\textwidth).
"""
from __future__ import annotations

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.transforms import Affine2D
from PIL import Image

from _common import IMAGES, panel_label, save, setup

pal = setup()
PAL = pal.PAL
RAW = IMAGES / "raw"
FS = 6.5
LEAD = dict(arrowstyle="-", lw=0.4, color=PAL["ink"], shrinkA=1.5, shrinkB=0)


def label(ax, text, anchor, at, ha="left", va="center", color=None, style="normal", dot=True):
    rel = {("left", "center"): (0, 0.5), ("right", "center"): (1, 0.5),
           ("center", "bottom"): (0.5, 0), ("center", "top"): (0.5, 1),
           ("right", "bottom"): (1, 0), ("left", "bottom"): (0, 0),
           ("right", "top"): (1, 1), ("left", "top"): (0, 1)}[(ha, va)]
    ax.annotate(text, xy=anchor, xytext=at, ha=ha, va=va, fontsize=FS, style=style,
                color=color or PAL["ink"], arrowprops=dict(LEAD, relpos=rel),
                annotation_clip=False)
    if dot:
        ax.plot(*anchor, "o", ms=1.4, color=PAL["ink"], mec="white", mew=0.3, zorder=9)


def text(ax, x, y, s, **kw):
    kw = {"fontsize": FS, "color": PAL["ink"], "ha": "center", "va": "center", **kw}
    ax.text(x, y, s, **kw)


def load_white(path, size=None) -> np.ndarray:
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    a[(a.min(axis=2) >= 246) & (a.max(axis=2) - a.min(axis=2) <= 6)] = 255
    im = Image.fromarray(a.astype(np.uint8))
    return np.asarray(im.resize(size, Image.LANCZOS) if size else im)


# --------------------------------------------------------------------------------------
# (a) interferometer + schematic A-scan
# --------------------------------------------------------------------------------------
def draw_interferometer(ax):
    W, H = 1672, 941
    ax.imshow(load_white(RAW / "fig_bg_oct_acquisition_raw_interferometer.png", (1300, 732)),
              extent=(0, W, H, 0), interpolation="none")
    text(ax, 160, 515, "Light source", va="top")
    label(ax, "Detector", (497, 781), (450, 781), ha="right", dot=False)
    label(ax, "Beam splitter", (527, 382), (470, 300), ha="right")
    label(ax, "Reference mirror", (688, 135), (730, 135), dot=False)
    text(ax, 625, 255, "reference arm", style="italic", color=PAL["ink_2"], ha="left")
    text(ax, 860, 372, "sample arm", style="italic", color=PAL["ink_2"])
    label(ax, "Eye", (1250, 250), (1250, 190), ha="center", va="bottom")

    # schematic A-scan in the free area: depth downwards, reflectivity to the right
    x0, x1, y0, y1 = 780, 1080, 700, 930          # plot box in image pixels
    z = np.linspace(0, 1, 500)
    peaks = [(0.08, 0.025, 1.00), (0.30, 0.050, 0.30), (0.55, 0.020, 0.55),
             (0.70, 0.030, 0.95), (0.86, 0.070, 0.40)]
    r = 0.05 + sum(a * np.exp(-0.5 * ((z - m) / s) ** 2) for m, s, a in peaks)
    r = r / r.max()
    ax.plot(x0 + 8 + r * (x1 - x0 - 30), y0 + 8 + z * (y1 - y0 - 8), color=PAL["primary"],
            lw=0.8)
    ax.annotate("", xy=(x1, y0), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", lw=0.5, color=PAL["ink"], mutation_scale=5))
    ax.annotate("", xy=(x0, y1 + 10), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", lw=0.5, color=PAL["ink"], mutation_scale=5))
    text(ax, x1 + 12, y0, "reflectivity", ha="left", va="center", color=PAL["ink_2"])
    text(ax, x0 - 12, y1, "depth", ha="right", va="center", color=PAL["ink_2"])
    text(ax, x1 + 12, (y0 + y1) / 2 + 40, "A-scan\n(schematic)", ha="left", va="center")
    # detector -> plot
    ax.annotate("", xy=(x0 - 15, 781), xytext=(690, 781),
                arrowprops=dict(arrowstyle="-|>", lw=0.5, color=PAL["ink_2"], mutation_scale=5,
                                ls=(0, (2, 1.5))))
    ax.set_xlim(40, 1620)
    ax.set_ylim(960, 90)
    ax.set_aspect("equal")
    ax.axis("off")


# --------------------------------------------------------------------------------------
# (b) scan geometry block
# --------------------------------------------------------------------------------------
BW, BD, BH = 6.0, 6.0, 1.9        # width, depth (mm), drawn height (exaggerated)
K, ANG = 0.45, np.deg2rad(35)     # cabinet projection
DX, DY = BD * K * np.cos(ANG), BD * K * np.sin(ANG)


def P(x, y, z):
    return (x + y * K * np.cos(ANG), z + y * K * np.sin(ANG))


def draw_block(ax):
    raw = load_white(RAW / "fig_bg_retinal_anatomy_raw_healthy.png")
    band = raw[108:658]
    front = np.concatenate([band[:, 0:650], band[:, 1522:2172]], axis=1)
    side = band[:, 0:650]
    ax.imshow(front, extent=(0, BW, 0, BH), interpolation="bilinear", zorder=2)
    im = ax.imshow(side[::-1], extent=(0, side.shape[1], 0, side.shape[0]), origin="lower",
                   interpolation="bilinear", zorder=1)
    M = Affine2D(np.array([[DX / side.shape[1], 0, BW],
                           [DY / side.shape[1], BH / side.shape[0], 0], [0, 0, 1]]))
    im.set_transform(M + ax.transData)
    face_r = [P(BW, 0, 0), P(BW, BD, 0), P(BW, BD, BH), P(BW, 0, BH)]
    im.set_clip_path(Polygon(face_r, closed=True, transform=ax.transData))
    ax.add_patch(Polygon(face_r, closed=True, fc=PAL["secondary"], alpha=0.12, ec="none",
                         zorder=3))
    top = [P(0, 0, BH), P(BW, 0, BH), P(BW, BD, BH), P(0, BD, BH)]
    ax.add_patch(Polygon(top, closed=True, fc="#DCEAF2", ec="none", zorder=4))
    # lesion seen en face
    t = np.linspace(0, 2 * np.pi, 200)
    r = 1.0 + 0.18 * np.sin(3 * t + 1) + 0.12 * np.sin(5 * t + 2) + 0.08 * np.cos(2 * t)
    lx, ly = 3.7 + 1.05 * r * np.cos(t), 3.6 + 0.9 * r * np.sin(t)
    ax.add_patch(Polygon([P(x, y, BH) for x, y in zip(lx, ly)], closed=True,
                         fc=PAL["secondary"], alpha=0.35, ec="none", zorder=5))
    # scan lines, one per B-scan, parallel to the front edge
    for y in np.linspace(0, BD, 11)[1:]:
        (xa, ya), (xb, yb) = P(0, y, BH), P(BW, y, BH)
        ax.plot([xa, xb], [ya, yb], lw=0.45, color=PAL["primary_700"], zorder=6)
    edges = [((0, 0, 0), (BW, 0, 0)), ((BW, 0, 0), (BW, 0, BH)), ((BW, 0, BH), (0, 0, BH)),
             ((0, 0, BH), (0, 0, 0)), ((BW, 0, 0), (BW, BD, 0)), ((BW, BD, 0), (BW, BD, BH)),
             ((BW, BD, BH), (BW, 0, BH)), ((0, 0, BH), (0, BD, BH)), ((0, BD, BH), (BW, BD, BH))]
    for a, b in edges:
        (xa, ya), (xb, yb) = P(*a), P(*b)
        ax.plot([xa, xb], [ya, yb], lw=0.6, color=PAL["ink_2"], zorder=7)
    # B-scan = front face
    ax.add_patch(Polygon([P(0, 0, 0), P(BW, 0, 0), P(BW, 0, BH), P(0, 0, BH)], closed=True,
                         fill=False, ec=PAL["primary"], lw=1.3, zorder=8))
    # A-scan
    xa = 1.6
    ax.plot([xa, xa], [BH + DY + 0.55, 0], color=PAL["accent"], lw=1.3, zorder=9,
            solid_capstyle="butt")
    ax.plot(xa, BH, "o", ms=2.6, color=PAL["accent"], zorder=10)

    # labels
    label(ax, "A-scan", (xa, BH + DY + 0.35), (xa - 0.5, BH + DY + 0.45), ha="right",
          dot=False)
    label(ax, "B-scan", (0.0, BH * 0.45), (-0.45, BH * 0.45), ha="right")
    label(ax, "en-face view", P(5.4, 5.0, BH), (BW + DX + 0.3, BH + DY + 0.25))
    label(ax, "lesion", P(3.9, 3.7, BH), (P(3.9, BD, BH)[0], BH + DY + 0.45), ha="center",
          va="bottom")
    label(ax, "volume", P(BW, BD * 0.55, BH * 0.35), (BW + DX + 0.3, BH + DY * 0.35))
    # footprint
    text(ax, BW / 2, -0.28, "≈ 6 mm", va="top", color=PAL["ink_2"])
    mx, my = P(BW, BD / 2, 0)
    text(ax, mx + 0.3, my - 0.15, "≈ 6 mm", ha="left", va="top", color=PAL["ink_2"])
    ax.set_xlim(-1.1, BW + DX + 1.6)
    ax.set_ylim(-0.75, BH + DY + 0.85)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    fig = plt.figure(figsize=(126 / 25.4, 56 / 25.4))
    ax_a = fig.add_axes([0.0, 0.0, 0.52, 1.0])
    ax_b = fig.add_axes([0.52, 0.0, 0.48, 1.0])
    draw_interferometer(ax_a)
    draw_block(ax_b)
    panel_label(ax_a, "(a)", x=0.03, y=0.95)
    panel_label(ax_b, "(b)", x=0.03, y=0.95)
    save(fig, "fig_bg_oct_acquisition")


if __name__ == "__main__":
    main()
