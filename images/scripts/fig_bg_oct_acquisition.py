"""Figure 2.2 (fig:bg:oct-acquisition): how OCT measures a depth profile and builds a volume.

(a) Measuring principle (top). Input: images/raw/fig_bg_oct_acquisition_raw_interferometer.png
    (1672 x 941 px, ChatGPT image generation, no text; read-only backup, never modified):
    light source, beam splitter, reference mirror, eye, detector. Added here: labels and a
    schematic A-scan (reflectivity against depth) in the empty area right of the detector.
    Anchors in raw pixels, read off a gridded render: light source box x 73-248, y 400-490;
    beam splitter x 518-660, y 373-512; mirror x 490-688, y 122-148; detector x 497-680,
    y 732-830; eye wall x ~980-1430, y ~240-650; free area x ~720-1180, y ~660-900.
    The A-scan curve is schematic (a sum of Gaussian peaks), not data.

(b) From A-scan to en-face view (bottom, full width), drawn here: one A-scan (a single column),
    a B-scan (many A-scans side by side), the volume (a stack of B-scans) and the en-face view
    (the volume seen from the front of the eye, one line per B-scan, with a lesion). The B-scans
    are the flat left end of the healthy layer strip of Figure 2.3
    (images/raw/fig_bg_retinal_anatomy_raw_healthy.png, rows 100-658 = ILM to sclera, columns
    0-520), shown at native resolution and stretched 1.6x laterally. The highlighted A-scan,
    B-scan and en-face line correspond across the four drawings.

Output: images/fig_bg_oct_acquisition.pdf (include at width=\\textwidth).
"""
from __future__ import annotations

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle
from PIL import Image

from _common import IMAGES, panel_label, save, setup

pal = setup()
PAL = pal.PAL
RAW = IMAGES / "raw"
FS = 6.5
LEAD = dict(arrowstyle="-", lw=0.4, color=PAL["ink"], shrinkA=1.5, shrinkB=0)
Z_TOP = 30                       # labels and leaders above every drawn element


def label(ax, text, anchor, at, ha="left", va="center", color=None, style="normal", dot=True):
    rel = {("left", "center"): (0, 0.5), ("right", "center"): (1, 0.5),
           ("center", "bottom"): (0.5, 0), ("center", "top"): (0.5, 1),
           ("right", "bottom"): (1, 0), ("left", "bottom"): (0, 0),
           ("right", "top"): (1, 1), ("left", "top"): (0, 1)}[(ha, va)]
    ax.annotate(text, xy=anchor, xytext=at, ha=ha, va=va, fontsize=FS, style=style,
                color=color or PAL["ink"], arrowprops=dict(LEAD, relpos=rel),
                annotation_clip=False, zorder=Z_TOP)
    if dot:
        ax.plot(*anchor, "o", ms=1.4, color=PAL["ink"], mec="white", mew=0.3, zorder=Z_TOP + 1)


def text(ax, x, y, s, **kw):
    kw = {"fontsize": FS, "color": PAL["ink"], "ha": "center", "va": "center", "zorder": Z_TOP,
          **kw}
    ax.text(x, y, s, **kw)


def load_white(path) -> np.ndarray:
    a = np.asarray(Image.open(path).convert("RGB")).astype(np.int16)
    a[(a.min(axis=2) >= 246) & (a.max(axis=2) - a.min(axis=2) <= 6)] = 255
    return a.astype(np.uint8)


def arrow(ax, x0, x1, y, **kw):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>", mutation_scale=7, lw=0.6,
                                 color=PAL["ink_2"], zorder=Z_TOP, **kw))


# --------------------------------------------------------------------------------------
# (a) interferometer + schematic A-scan
# --------------------------------------------------------------------------------------
def draw_interferometer(ax):
    W, H = 1672, 941
    ax.imshow(load_white(RAW / "fig_bg_oct_acquisition_raw_interferometer.png"),
              extent=(0, W, H, 0), interpolation="lanczos")
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
    ax.plot(x0 + 8 + r * (x1 - x0 - 30), y0 + 8 + z * (y1 - y0 - 8), color=PAL["accent"],
            lw=0.8)
    for xy in [(x1, y0), (x0, y1 + 10)]:
        ax.annotate("", xy=xy, xytext=(x0, y0), zorder=Z_TOP,
                    arrowprops=dict(arrowstyle="-|>", lw=0.5, color=PAL["ink"],
                                    mutation_scale=5))
    text(ax, x1 + 12, y0, "reflectivity", ha="left", color=PAL["ink_2"])
    text(ax, x0 - 12, y1, "depth", ha="right", color=PAL["ink_2"])
    text(ax, x1 + 12, (y0 + y1) / 2 + 40, "A-scan\n(schematic)", ha="left")
    ax.annotate("", xy=(x0 - 15, 781), xytext=(690, 781), zorder=Z_TOP,
                arrowprops=dict(arrowstyle="-|>", lw=0.5, color=PAL["ink_2"], mutation_scale=5,
                                ls=(0, (2, 1.5))))
    ax.set_xlim(40, 1620)
    ax.set_ylim(960, 90)
    ax.set_aspect("equal")
    ax.axis("off")


# --------------------------------------------------------------------------------------
# (b) A-scan -> B-scan -> volume -> en-face view
# --------------------------------------------------------------------------------------
def draw_sequence(ax):
    raw = load_white(RAW / "fig_bg_retinal_anatomy_raw_healthy.png")
    strip = raw[100:658, 0:520]                    # flat left end, ILM ... sclera
    H = 1.0
    W = H * strip.shape[1] / strip.shape[0] * 1.6
    xa = 0.42                                      # A-scan position, fraction of the width
    aw = 0.09                                      # drawn width of the A-scan column
    gap = 0.46
    n, dx, dy = 6, 0.13, 0.09                      # B-scans in the stack and their offset

    def caption(xc, title, sub):
        text(ax, xc, -0.12, title, va="top")
        text(ax, xc, -0.27, sub, va="top", fontsize=FS - 0.5, color=PAL["ink_2"])

    x = 0.0
    # 1. A-scan: one column of the B-scan
    c = int(xa * strip.shape[1])
    ax.imshow(strip[:, c - 5:c + 5], extent=(x, x + aw, 0, H), aspect="auto",
              interpolation="lanczos", zorder=2)
    ax.add_patch(Rectangle((x, 0), aw, H, fill=False, ec=PAL["accent"], lw=0.8, zorder=3))
    caption(x + aw / 2, "A-scan", "depth profile")
    arrow(ax, x + aw + 0.08, x + aw + gap - 0.08, H / 2)
    x += aw + gap
    # 2. B-scan: many A-scans side by side
    ax.imshow(strip, extent=(x, x + W, 0, H), aspect="auto", interpolation="lanczos", zorder=2)
    ax.add_patch(Rectangle((x, 0), W, H, fill=False, ec=PAL["primary"], lw=0.6, zorder=3))
    ax.add_patch(Rectangle((x + xa * W - aw / 2, 0), aw, H, fill=False, ec=PAL["accent"],
                           lw=0.8, zorder=4))
    caption(x + W / 2, "B-scan", "A-scans side by side")
    arrow(ax, x + W + 0.08, x + W + gap - 0.08, H / 2)
    x += W + gap
    # 3. Volume: a stack of B-scans, offset back and to the right
    for i in reversed(range(n)):
        ox, oy = x + i * dx, i * dy
        ax.imshow(strip, extent=(ox, ox + W, oy, oy + H), aspect="auto",
                  interpolation="lanczos", zorder=10 - i)
        ax.add_patch(Rectangle((ox, oy), W, H, fill=False,
                               ec=PAL["primary"] if i == 0 else PAL["ink_2"],
                               lw=0.6 if i == 0 else 0.35, zorder=10.5 - i))
    caption(x + (W + (n - 1) * dx) / 2, "Volume", "stack of B-scans")
    x += W + (n - 1) * dx
    arrow(ax, x + 0.08, x + gap - 0.08, H / 2)
    x += gap
    # 4. En-face view: the volume seen from the front of the eye, one line per B-scan
    s = 1.0
    ax.add_patch(Rectangle((x, 0), s, s, fc="#DCEAF2", ec=PAL["ink_2"], lw=0.5, zorder=2))
    t = np.linspace(0, 2 * np.pi, 200)
    r = 1.0 + 0.18 * np.sin(3 * t + 1) + 0.12 * np.sin(5 * t + 2)
    ax.add_patch(Polygon(np.c_[x + 0.55 + 0.2 * r * np.cos(t), 0.55 + 0.17 * r * np.sin(t)],
                         closed=True, fc=PAL["secondary"], alpha=0.45, ec="none", zorder=3))
    for i, yy in enumerate(np.linspace(0.08, 0.92, n)):
        ax.plot([x, x + s], [yy, yy], lw=1.0 if i == 0 else 0.4,
                color=PAL["primary"] if i == 0 else PAL["primary_700"], zorder=4)
    label(ax, "lesion", (x + 0.62, 0.62), (x + s + 0.12, 0.85))
    caption(x + s / 2, "En-face view", "volume seen from the front")
    x += s
    ax.set_xlim(-0.05, x + 0.55)
    ax.set_ylim(-0.42, H + (n - 1) * dy + 0.05)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    fig = plt.figure(figsize=(126 / 25.4, 95 / 25.4))
    ax_a = fig.add_axes([0.09, 0.42, 0.82, 0.58])
    ax_b = fig.add_axes([0.0, 0.0, 1.0, 0.38])
    draw_interferometer(ax_a)
    draw_sequence(ax_b)
    fig.text(0.0, 0.98, "(a)", fontsize=9, fontweight="bold", va="top")
    fig.text(0.0, 0.38, "(b)", fontsize=9, fontweight="bold", va="top")
    save(fig, "fig_bg_oct_acquisition")


if __name__ == "__main__":
    main()
