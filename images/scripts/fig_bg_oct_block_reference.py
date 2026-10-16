"""Geometry reference for Fig. 2.2(b), to hand to ChatGPT image generation together with the
healthy layer strip of Fig. 2.3. No text. Writes images/_preview/fig_bg_oct_block_reference.png.

Geometry (cabinet projection): a block of retina, front, top and right faces visible. The layer
order on the faces follows the Fig. 2.3 strip (blue inner layers, photoreceptor bands, brown RPE,
rose choroid, white sclera), as flat colour bands. Inside the block, one B-scan slice parallel to
the front face at 40 % of the depth, semi-transparent; its top edge lies on one of the scan lines
drawn on the top face. The A-scan is an orange line coming from above, entering the top face on
that scan line and running down inside the slice to the bottom of the block.
"""
from __future__ import annotations

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

from _common import PREVIEW, setup

pal = setup()
PAL = pal.PAL

BW, BD, BH = 6.0, 6.0, 1.9
K, ANG = 0.55, np.deg2rad(32)
YS = 0.4 * BD                              # depth of the B-scan slice
XA = 2.2                                   # lateral position of the A-scan
# flat colour bands, top to bottom, fractions of the height (from the Fig. 2.3 strip)
BANDS = [(0.14, "#9FD3EE"), (0.07, "#D5ECF6"), (0.08, "#8CC4E6"), (0.06, "#D5ECF6"),
         (0.15, "#6FA6D8"), (0.08, "#E4EEF3"), (0.09, "#3E8FB8"), (0.05, "#B07A45"),
         (0.05, "#E9A3BC"), (0.15, "#E58FAE"), (0.08, "#F2F2F2")]


def P(x, y, z):
    return (x + y * K * np.cos(ANG), z + y * K * np.sin(ANG))


def face_bands(ax, corner, u, v, z):
    """Fill a face spanned by u (lateral) and v (up) with the bands, top band at the top."""
    top = 1.0
    for frac, col in BANDS:
        b = top - frac
        pts = [corner + u * 0 + v * b, corner + u + v * b, corner + u + v * top, corner + v * top]
        ax.add_patch(Polygon([P(*p) for p in pts], closed=True, fc=col, ec="none", zorder=z))
        top = b


def main():
    fig, ax = plt.subplots(figsize=(8, 5.2))
    o = np.array([0.0, 0.0, 0.0])
    face_bands(ax, o, np.array([BW, 0, 0]), np.array([0, 0, BH]), 2)                 # front
    face_bands(ax, np.array([BW, 0, 0]), np.array([0, BD, 0]), np.array([0, 0, BH]), 1)  # right
    ax.add_patch(Polygon([P(BW, 0, 0), P(BW, BD, 0), P(BW, BD, BH), P(BW, 0, BH)], closed=True,
                         fc=PAL["secondary"], alpha=0.10, ec="none", zorder=3))
    ax.add_patch(Polygon([P(0, 0, BH), P(BW, 0, BH), P(BW, BD, BH), P(0, BD, BH)], closed=True,
                         fc="#DCEAF2", ec="none", zorder=4))
    t = np.linspace(0, 2 * np.pi, 200)
    r = 1.0 + 0.18 * np.sin(3 * t + 1) + 0.12 * np.sin(5 * t + 2) + 0.08 * np.cos(2 * t)
    lx, ly = 3.9 + 1.0 * r * np.cos(t), 3.9 + 0.85 * r * np.sin(t)
    ax.add_patch(Polygon([P(x, y, BH) for x, y in zip(lx, ly)], closed=True,
                         fc=PAL["secondary"], alpha=0.35, ec="none", zorder=5))
    for y in np.linspace(0, BD, 11)[1:-1]:
        (xa, ya), (xb, yb) = P(0, y, BH), P(BW, y, BH)
        ax.plot([xa, xb], [ya, yb], lw=0.5, color=PAL["primary_700"], zorder=6)
    # B-scan slice inside the block (seen through the faces): light fill, hidden edges dashed,
    # the edge where it meets the top face solid
    sl = [P(0, YS, 0), P(BW, YS, 0), P(BW, YS, BH), P(0, YS, BH)]
    ax.add_patch(Polygon(sl, closed=True, fc=PAL["primary_300"], alpha=0.30, ec="none", zorder=7))
    for a, b in [((0, YS, 0), (BW, YS, 0)), ((BW, YS, 0), (BW, YS, BH)), ((0, YS, 0), (0, YS, BH))]:
        (x0, y0), (x1, y1) = P(*a), P(*b)
        ax.plot([x0, x1], [y0, y1], lw=0.8, color=PAL["primary_700"], ls=(0, (4, 3)), zorder=8)
    (xa, ya), (xb, yb) = P(0, YS, BH), P(BW, YS, BH)
    ax.plot([xa, xb], [ya, yb], lw=1.2, color=PAL["primary_700"], zorder=8)
    # A-scan: solid above the top face, dashed inside the block, down to the bottom of the slice
    top_pt, bot_pt, air_pt = P(XA, YS, BH), P(XA, YS, 0), P(XA, YS, BH + 1.2)
    ax.annotate("", xy=top_pt, xytext=air_pt, zorder=9,
                arrowprops=dict(arrowstyle="-|>", lw=1.6, color=PAL["accent"], mutation_scale=9,
                                shrinkA=0, shrinkB=0))
    ax.plot([top_pt[0], bot_pt[0]], [top_pt[1], bot_pt[1]], color=PAL["accent"], lw=1.6,
            ls=(0, (3, 2)), zorder=9)
    ax.plot(*top_pt, "o", ms=4, color=PAL["accent"], zorder=10)
    edges = [((0, 0, 0), (BW, 0, 0)), ((BW, 0, 0), (BW, 0, BH)), ((BW, 0, BH), (0, 0, BH)),
             ((0, 0, BH), (0, 0, 0)), ((BW, 0, 0), (BW, BD, 0)), ((BW, BD, 0), (BW, BD, BH)),
             ((BW, BD, BH), (BW, 0, BH)), ((0, 0, BH), (0, BD, BH)), ((0, BD, BH), (BW, BD, BH))]
    for a, b in edges:
        (x0, y0), (x1, y1) = P(*a), P(*b)
        ax.plot([x0, x1], [y0, y1], lw=0.6, color=PAL["ink_2"], zorder=11)
    ax.set_aspect("equal")
    ax.axis("off")
    out = PREVIEW / "fig_bg_oct_block_reference.png"
    PREVIEW.mkdir(exist_ok=True)
    fig.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")
    print("wrote", out)


if __name__ == "__main__":
    main()
