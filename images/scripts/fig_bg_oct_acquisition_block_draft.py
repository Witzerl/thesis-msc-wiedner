"""Prototype for Fig. 2.2(b): OCT scan geometry as a block textured with the Fig. 2.3 layer strip."""
import sys
import numpy as np
from PIL import Image
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.transforms import Affine2D
sys.path.insert(0, r"D:\Schule\MasterThesis\thesis\style")
import palette
palette.register_fonts(r"D:\Schule\MasterThesis\thesis\fonts"); palette.apply_thesis_style()
PAL = palette.PAL

raw = np.asarray(Image.open(r"D:\Schule\MasterThesis\thesis\images\raw\fig_bg_retinal_anatomy_raw_healthy.png").convert("RGB"))
band = raw[108:658]                                  # ILM ... sclera
flat = np.concatenate([band[:, 0:650], band[:, 0:650][:, ::-1]], axis=1)   # both flat ends, no pit
side = band[:, 0:650]

W, D, Hb = 6.0, 6.0, 1.9          # block width, depth, height (height exaggerated)
k, ang = 0.45, np.deg2rad(35)     # cabinet projection: depth drawn at 35 deg, scaled by 0.45
dx, dy = D * k * np.cos(ang), D * k * np.sin(ang)

def P(x, y, z):                   # 3D -> 2D (x right, y into the page, z up)
    return (x + y * k * np.cos(ang), z + y * k * np.sin(ang))

fig, ax = plt.subplots(figsize=(5.3, 3.6))
# front face: texture in its rectangle
ax.imshow(flat, extent=(0, W, 0, Hb), interpolation="bilinear", zorder=2)
# right face: same texture, sheared into the parallelogram
tr = Affine2D().scale(dx / side.shape[1], Hb / side.shape[0]).skew(0, 0).translate(0, 0)
im = ax.imshow(side[::-1], extent=(0, side.shape[1], 0, side.shape[0]), origin="lower",
               interpolation="bilinear", zorder=1)
M = Affine2D(np.array([[dx / side.shape[1], 0, W], [dy / side.shape[1], Hb / side.shape[0], 0], [0, 0, 1]]))
im.set_transform(M + ax.transData)
clip = Polygon([P(W, 0, 0), P(W, D, 0), P(W, D, Hb), P(W, 0, Hb)], closed=True, transform=ax.transData)
im.set_clip_path(clip)
# shade the right face slightly
ax.add_patch(Polygon([P(W, 0, 0), P(W, D, 0), P(W, D, Hb), P(W, 0, Hb)], closed=True,
                     fc=PAL["secondary"], alpha=0.12, ec="none", zorder=3))
# top face
top = [P(0, 0, Hb), P(W, 0, Hb), P(W, D, Hb), P(0, D, Hb)]
ax.add_patch(Polygon(top, closed=True, fc="#DCEAF2", ec="none", zorder=3))
# lesion patch on the top face (smooth seeded blob)
rng = np.random.default_rng(3); t = np.linspace(0, 2 * np.pi, 200)
r = 1.0 + 0.18 * np.sin(3 * t + 1) + 0.12 * np.sin(5 * t + 2) + 0.08 * np.cos(2 * t)
bx, by = 3.6 + 1.1 * r * np.cos(t), 3.6 + 0.9 * r * np.sin(t)
ax.add_patch(Polygon([P(x, y, Hb) for x, y in zip(bx, by)], closed=True, fc=PAL["secondary"],
                     alpha=0.35, ec="none", zorder=4))
# scan lines (B-scan positions), parallel to the front edge
for y in np.linspace(0.0, D, 11):
    (x0, y0), (x1, y1) = P(0, y, Hb), P(W, y, Hb)
    ax.plot([x0, x1], [y0, y1], lw=0.5 if y > 0 else 0, color=PAL["primary_700"], zorder=5)
# outlines
for a, b in [((0,0,0),(W,0,0)), ((W,0,0),(W,0,Hb)), ((W,0,Hb),(0,0,Hb)), ((0,0,Hb),(0,0,0)),
             ((W,0,0),(W,D,0)), ((W,D,0),(W,D,Hb)), ((W,D,Hb),(W,0,Hb)), ((0,0,Hb),(0,D,Hb)), ((0,D,Hb),(W,D,Hb))]:
    (x0, y0), (x1, y1) = P(*a), P(*b)
    ax.plot([x0, x1], [y0, y1], lw=0.7, color=PAL["ink_2"], zorder=6)
# B-scan = the front face, highlighted
ax.add_patch(Polygon([P(0,0,0), P(W,0,0), P(W,0,Hb), P(0,0,Hb)], closed=True, fill=False,
                     ec=PAL["primary"], lw=1.6, zorder=7))
# A-scan: beam from above, on the front edge, through all layers
xa = 2.0
ax.plot([xa, xa], [Hb + dy + 0.7, 0], color=PAL["accent"], lw=1.6, zorder=8, solid_capstyle="butt")
ax.plot(xa, Hb, "o", ms=3, color=PAL["accent"], zorder=9)
ax.set_xlim(-0.3, W + dx + 0.3); ax.set_ylim(-0.3, Hb + dy + 0.9)
ax.set_aspect("equal"); ax.axis("off")
fig.savefig(sys.argv[1], dpi=250, bbox_inches="tight")
