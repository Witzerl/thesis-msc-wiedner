"""Figure fig:method:stencils (Section 4.3.3): the three uniform-graph constructions of the
graph network, drawn around one interior node in grid indices.

(a) k-NN on physical coordinates (k = 12), (b) k-NN on integer grid indices (k = 12),
(c) the dilated stencil (rows -1..1 x columns 0, +-7, +-14, +-21; baselines/anisognn.py
defaults pitch 7, taps 3, rows 1). The two k-NN neighbourhoods are computed here by brute
force on a lattice patch with the grid pitch (0.12118 mm between rows, 0.00568 mm between
columns), so the figure shows what a k-NN query returns, not a hand-typed offset list.
Geometry only; no run data.

The drawing is in grid indices (one row step = one column step on paper); the physical
distances are written on the figure.

    python fig_method_stencils.py
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

from _common import DX_MM, DY_MM, save, setup

pal = setup()
ARM, PAL = pal.ARM, pal.PAL

# ---------------------------------------------------------------- neighbourhoods
K = 12
R_WIN, C_WIN = 2, 24                       # drawn window: rows +-2, columns +-24


def knn(scale_r, scale_c, k=K, r=6, c=30):
    """k nearest neighbours of the centre of a (2r+1) x (2c+1) patch, no self-loop."""
    dr, dc = np.meshgrid(np.arange(-r, r + 1), np.arange(-c, c + 1), indexing="ij")
    dr, dc = dr.ravel(), dc.ravel()
    d2 = (dr * scale_r) ** 2 + (dc * scale_c) ** 2
    keep = d2 > 0
    dr, dc, d2 = dr[keep], dc[keep], d2[keep]
    order = np.argsort(d2, kind="stable")
    # no tie may straddle the k-th neighbour, otherwise the set is not well defined
    assert d2[order[k - 1]] < d2[order[k]], "tie at the k-th neighbour"
    return sorted(zip(dr[order[:k]].tolist(), dc[order[:k]].tolist()))


PHYS = knn(DY_MM, DX_MM)
INDEX = knn(1.0, 1.0)
STENCIL = sorted((dr, dc) for dr in (-1, 0, 1) for dc in (0, -7, 7, -14, 14, -21, 21)
                 if (dr, dc) != (0, 0))
assert all(dr == 0 for dr, _ in PHYS) and {abs(dc) for _, dc in PHYS} == set(range(1, 7))
assert {(dr, dc) for dr, dc in INDEX} == {(dr, dc) for dr in range(-2, 3)
                                          for dc in range(-2, 3) if 0 < dr * dr + dc * dc <= 4}
assert len(STENCIL) == 20


def reach(nb):
    return (max(abs(c) for _, c in nb) * DX_MM, max(abs(r) for r, _ in nb) * DY_MM)


for name, nb in (("physical k-NN", PHYS), ("index k-NN", INDEX), ("stencil", STENCIL)):
    a, b = reach(nb)
    far = max(np.hypot(r * DY_MM, c * DX_MM) for r, c in nb)
    print(f"{name}: {len(nb)} neighbours, along a row +-{a:.4f} mm, across rows "
          f"+-{b:.4f} mm, farthest neighbour {far:.4f} mm")

# ---------------------------------------------------------------- drawing helpers
FS = 6.5


def um(x_mm):
    """A physical distance in micrometres, as written in Section 4.3.3."""
    x = x_mm * 1000
    return f"{x:.1f} \u00b5m" if x < 10 else f"{x:.0f} \u00b5m"


def edge(ax, nb, r, c, col):
    """Edge from the centre to (r, c). An edge that would run through another neighbour
    on the same line is bent, by more the more neighbours it passes, so every edge stays
    visible as a direct connection."""
    g = np.gcd(abs(r), abs(c))
    between = sum((r // g * m, c // g * m) in nb for m in range(1, g))
    if between == 0:
        ax.plot([0, c], [0, r], color=col, lw=0.8, zorder=2, solid_capstyle="round")
        return
    bulge = 0.16 * between                 # height of the arc, in grid steps
    # arc3 bends a rightward edge downwards for rad > 0: flip so that every bent
    # edge along a row bulges upwards and the dimension lines below stay clear
    sign = -1 if c > 0 else 1
    rad = sign * 2 * bulge / np.hypot(r, c)
    ax.add_patch(FancyArrowPatch((0, 0), (c, r), arrowstyle="-", lw=0.8, color=col,
                                 connectionstyle=f"arc3,rad={rad:.4f}", zorder=2,
                                 shrinkA=0, shrinkB=0))


def hdim(ax, c0, c1, y, text, col=PAL["ink_2"], above=False):
    """Horizontal dimension line from column c0 to c1 at height y, labelled in mm."""
    ax.annotate("", xy=(c1, y), xytext=(c0, y),
                arrowprops=dict(arrowstyle="<->", lw=0.5, color=col,
                                shrinkA=0, shrinkB=0, mutation_scale=5))
    for c in (c0, c1):
        ax.plot([c, c], [y - 0.12, y + 0.12], color=col, lw=0.5)
    ax.text((c0 + c1) / 2, y + (0.18 if above else -0.18), text, fontsize=FS, color=col,
            ha="center", va="bottom" if above else "top")


def vdim(ax, r0, r1, x, text, col=PAL["ink_2"], left=True):
    """Vertical dimension line from row r0 to r1 at column x, labelled in mm."""
    ax.annotate("", xy=(x, r1), xytext=(x, r0),
                arrowprops=dict(arrowstyle="<->", lw=0.5, color=col,
                                shrinkA=0, shrinkB=0, mutation_scale=5))
    for r in (r0, r1):
        ax.plot([x - 0.3, x + 0.3], [r, r], color=col, lw=0.5)
    ax.text(x + (-0.5 if left else 0.5), (r0 + r1) / 2, text, fontsize=FS, color=col,
            ha="right" if left else "left", va="center")


# ---------------------------------------------------------------- figure
PANELS = [
    ("(a) $k$-NN on physical coordinates ($k = 12$)", PHYS, PAL["muted"]),
    ("(b) $k$-NN on grid indices ($k = 12$)", INDEX, ARM["knn"]),
    ("(c) Dilated stencil", STENCIL, ARM["stencil"]),
]

fig, axes = plt.subplots(3, 1, figsize=pal.fig_size(1.0, 0.5),
                         gridspec_kw=dict(hspace=0.3, left=0.01, right=0.99,
                                          top=0.95, bottom=0.02))
rows, cols = np.meshgrid(np.arange(-R_WIN, R_WIN + 1), np.arange(-C_WIN, C_WIN + 1),
                         indexing="ij")

for ax, (title, nb, col) in zip(axes, PANELS):
    ax.set_title(title, loc="left", fontsize=8, fontweight="semibold", pad=3)
    ax.axis("off")
    ax.scatter(cols.ravel(), rows.ravel(), s=5, color=PAL["line"], lw=0, zorder=1)
    for r, c in nb:
        edge(ax, nb, r, c, col)
    o = np.array(nb)
    ax.scatter(o[:, 1], o[:, 0], s=12, color=col, edgecolor=PAL["ink"], lw=0.3, zorder=3)
    ax.scatter([0], [0], s=22, color=PAL["accent"], edgecolor=PAL["ink"], lw=0.4, zorder=4)
    ax.set_xlim(-C_WIN - 4.5, C_WIN + 0.6)
    ax.set_ylim(-R_WIN - 1.4, R_WIN + 0.4)
    ax.set_aspect("equal")

a = axes[0]                                 # lattice pitch, the same in every panel
vdim(a, R_WIN - 1, R_WIN, -C_WIN - 0.6, um(DY_MM))
hdim(a, -C_WIN, -C_WIN + 1, -R_WIN - 0.45, um(DX_MM))
# physical k-NN: six columns either side
hdim(a, 0, 6, -R_WIN - 0.45, um(6 * DX_MM))
hdim(a, -6, 0, -R_WIN - 0.45, um(6 * DX_MM))

b = axes[1]                                 # index k-NN: two steps on both axes
hdim(b, 0, 2, -R_WIN - 0.45, um(2 * DX_MM))
vdim(b, 0, 2, 3.0, um(2 * DY_MM), left=False)

s = axes[2]                                 # stencil: three taps of seven columns
for c0 in (0, 7, 14):
    hdim(s, c0, c0 + 7, -R_WIN - 0.45, um(7 * DX_MM))
hdim(s, -21, 0, -R_WIN - 0.45, um(21 * DX_MM))
vdim(s, 0, 1, 22.2, um(DY_MM), left=False)

save(fig, "fig_method_stencils")
