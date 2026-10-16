"""Figure 2.1 (fig:bg:eye-anatomy): eye cross-section and fundus, with labels.

Inputs (images/raw/, read-only backups, never modified):
  fig_bg_eye_anatomy_raw_cross_section.png  horizontal section of a right eye seen from
      above, front to the left (2048 x 2048 px)
  fig_bg_eye_anatomy_raw_fundus.png         fundus of a right eye, optic disc to the right
      (1254 x 1254 px)
Both were generated with ChatGPT image generation from prompts/PROMPT_fig_2_1_eye_anatomy_imagegen.md
and contain no text. Everything else is drawn here: labels and leader lines, the four
macular zone circles, the 6 x 6 mm OCT window and the orientation words.

All anchor coordinates are pixels of the raw images; they were measured on the images
(colour scans across the eye wall, darkest point of the fovea, outline of the optic disc).

Scale of the fundus panel: the fovea-to-optic-disc distance is taken as 4.5 mm (centre to
centre, horizontal), which fixes the zone circles (diameters 0.35 / 1.5 / 2.5 / 5.5 mm)
and the 6 x 6 mm window. The cross-section has no scale.

Output: images/fig_bg_eye_anatomy.pdf (include at width=\\textwidth).
"""
from __future__ import annotations

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Rectangle
from PIL import Image

from _common import IMAGES, save, setup

pal = setup()
PAL = pal.PAL
RAW = IMAGES / "raw"
FS = 7                       # label font size (pt)
LEAD = dict(arrowstyle="-", lw=0.45, color=PAL["ink"], shrinkA=1.5, shrinkB=0)
DOWNSAMPLE = 1300            # px on the long side of each embedded image (~600 dpi in print)


def load(name: str) -> tuple[np.ndarray, int, int]:
    """Raw image as RGB, near-white background set to pure white, downsampled.
    Returns the array and the raw width/height (anchors stay in raw pixels)."""
    im = Image.open(RAW / name).convert("RGB")
    W, H = im.size
    a = np.asarray(im).astype(np.int16)
    grey_white = (a.min(axis=2) >= 246) & (a.max(axis=2) - a.min(axis=2) <= 6)
    a[grey_white] = 255
    im = Image.fromarray(a.astype(np.uint8))
    s = DOWNSAMPLE / max(W, H)
    im = im.resize((round(W * s), round(H * s)), Image.LANCZOS)
    return np.asarray(im), W, H


def label(ax, text, anchor, at, ha="left", va="center", color=None, dot=True):
    ax.annotate(text, xy=anchor, xytext=at, ha=ha, va=va, fontsize=FS,
                color=color or PAL["ink"], arrowprops=LEAD, annotation_clip=False)
    if dot:
        ax.plot(*anchor, "o", ms=1.6, color=PAL["ink"], mec="white", mew=0.3, zorder=5)


def orient(ax, text, at, ha="center"):
    ax.text(*at, text, fontsize=FS - 0.5, color=PAL["ink_2"], style="italic", ha=ha, va="center")


# --------------------------------------------------------------------------------------
# (a) cross-section; raw pixels, x to the right (back of the eye), y down
# --------------------------------------------------------------------------------------
def draw_cross_section(ax):
    img, W, H = load("fig_bg_eye_anatomy_raw_cross_section.png")
    ax.imshow(img, extent=(0, W, H, 0), interpolation="none")
    # left gutter: front of the eye
    label(ax, "Ciliary body", (500, 645), (90, 470), ha="right")
    label(ax, "Iris", (420, 800), (90, 740), ha="right")
    label(ax, "Cornea", (233, 900), (90, 900), ha="right")
    # the lens leader passes through the pupil gap (iris bands end at y ~950 and ~1053)
    label(ax, "Lens", (520, 1000), (90, 1060), ha="right")
    # top: the three wall layers, measured on vertical scans
    label(ax, "Sclera", (700, 404), (520, 215), ha="center", va="bottom")
    label(ax, "Choroid", (1000, 368), (1000, 215), ha="center", va="bottom")
    label(ax, "Retina", (1300, 518), (1480, 215), ha="center", va="bottom")
    # right gutter: back of the eye
    label(ax, "Macula", (1452, 790), (1960, 700))
    label(ax, "Fovea", (1494, 866), (1960, 880))
    label(ax, "Optic disc", (1507, 1182), (1960, 1040))
    label(ax, "Optic nerve", (1760, 1290), (1960, 1450))
    ax.text(1000, 1020, "Vitreous body", fontsize=FS, color=PAL["ink"], ha="center", va="center")
    # right eye seen from above with the front to the left: temporal up, nasal down
    orient(ax, "temporal", (-380, 260), ha="left")
    orient(ax, "nasal", (-380, 1720), ha="left")
    ax.set_xlim(-420, 2470)
    ax.set_ylim(1800, 150)
    ax.set_aspect("equal")
    ax.axis("off")


# --------------------------------------------------------------------------------------
# (b) fundus; raw pixels
# --------------------------------------------------------------------------------------
FOVEA = (575.0, 609.0)        # darkest point of the macular spot
DISC = (871.0, 603.0)         # centre of the cream disc outline (x 805-937, y 522-684)
PX_PER_MM = (DISC[0] - FOVEA[0]) / 4.5
ZONES_MM = {"foveola": 0.35, "fovea": 1.5, "parafovea": 2.5, "perifovea": 5.5}


def polar(r_mm, deg):
    t = np.deg2rad(deg)
    return (FOVEA[0] + r_mm * PX_PER_MM * np.cos(t), FOVEA[1] - r_mm * PX_PER_MM * np.sin(t))


def draw_fundus(ax):
    img, W, H = load("fig_bg_eye_anatomy_raw_fundus.png")
    ax.imshow(img, extent=(0, W, H, 0), interpolation="none")
    for d in ZONES_MM.values():
        ax.add_patch(Circle(FOVEA, d / 2 * PX_PER_MM, fill=False, lw=0.45,
                            ec=PAL["ink_2"], zorder=3))
    half = 3.0 * PX_PER_MM
    ax.add_patch(Rectangle((FOVEA[0] - half, FOVEA[1] - half), 2 * half, 2 * half, fill=False,
                           lw=0.9, ec=PAL["accent"], ls=(0, (3.5, 2.2)), zorder=4))
    # zones: anchors inside each zone at fanned angles, labels in the left gutter
    label(ax, "Macula", polar(2.75, 120), (90, 300), ha="right")
    label(ax, "Perifovea", polar(2.0, 145), (90, 450), ha="right")
    label(ax, "Parafovea", polar(1.0, 165), (90, 580), ha="right")
    label(ax, "Fovea", polar(0.5, 185), (90, 700), ha="right")
    label(ax, "Foveola", FOVEA, (90, 820), ha="right")
    label(ax, "Optic disc", (915, 560), (1090, 330))
    label(ax, "OCT window\n6 × 6 mm", (FOVEA[0] + half, FOVEA[1] + half), (1090, 900),
          color=PAL["accent"], dot=False)
    orient(ax, "temporal", (300, 1100))
    orient(ax, "nasal", (950, 1100))
    ax.set_xlim(-330, 1470)
    ax.set_ylim(1150, 120)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    w_mm = 131.5   # tight bbox adds ~3 mm of label overhang -> ~135 mm in print
    fig = plt.figure(figsize=(w_mm / 25.4, 62 / 25.4))
    ax_a = fig.add_axes([0.0, 0.0, 0.55, 1.0])
    ax_b = fig.add_axes([0.55, 0.0, 0.45, 1.0])
    draw_cross_section(ax_a)
    draw_fundus(ax_b)
    save(fig, "fig_bg_eye_anatomy")


if __name__ == "__main__":
    main()
