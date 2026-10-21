"""Figure fig:method:fen-toy (Section 4.3.6): the T-FEN transport operator in its two forms on a toy
grid, run from the same small random start (author 2026-10-21).

The operator is assembled as GraphPDE/baselines/fen.py does (read, not imported): a lattice of
Nx x Ny nodes at pitch 1, two right triangles per quad, per triangle the advective term
-(v_K . grad u_K) with the P1 gradient coefficients of fen.py, assembled to the three vertices
and divided by the number of adjacent triangles (lumped mass M = diag(n_adj)). Galerkin form: L.
Energy-conserving form: 0.5 * (L - M^-1 L^T M) (Equation eq:method:fen-skew).
Velocity per triangle: (0.2, 1.0) grid steps per unit time (mainly along the columns, left to
right) plus Gaussian noise with sd 0.5 per component (seed 0). Start: Gaussian values with
sd 0.1 (seed 1). Both forms are integrated exactly (matrix exponential) to time 10.
No learned part and no data are involved.

    python fig_method_fen_toy.py
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, LogNorm
from scipy.linalg import expm

from _common import save, setup

pal = setup()
PAL, SEQ = pal.PAL, pal.SEQ

NX, NY, T_END = 10, 60, 10.0
G = np.array([[[-1.0, -1.0], [0.0, 1.0], [1.0, 0.0]],          # fen.py grad_coef, type 0
              [[1.0, 1.0], [0.0, -1.0], [-1.0, 0.0]]])         # type 1 (d/drow, d/dcol)


def lattice(nx, ny):
    tris, types = [], []
    for r in range(nx - 1):
        for c in range(ny - 1):
            v00, v01, v10, v11 = r * ny + c, r * ny + c + 1, (r + 1) * ny + c, (r + 1) * ny + c + 1
            tris += [(v00, v01, v10), (v11, v10, v01)]
            types += [0, 1]
    return np.array(tris), np.array(types)


def operators(nx, ny, v):
    tri, typ = lattice(nx, ny)
    n = nx * ny
    n_adj = np.bincount(tri.ravel(), minlength=n).astype(float)
    L = np.zeros((n, n))
    for k, (t, ty) in enumerate(zip(tri, typ)):
        row = -(G[ty] @ v[k])                    # advective term of triangle k on its vertex values
        for i in t:
            L[i, t] += row
    L /= n_adj[:, None]
    M = np.diag(n_adj)
    return L, 0.5 * (L - np.linalg.inv(M) @ L.T @ M)


tri, _ = lattice(NX, NY)
v = np.tile([0.2, 1.0], (len(tri), 1)) + 0.5 * np.random.default_rng(0).standard_normal((len(tri), 2))
L, L_skew = operators(NX, NY, v)
print(f"largest real part of an eigenvalue: Galerkin {np.linalg.eigvals(L).real.max():+.3f}, "
      f"energy-conserving {np.abs(np.linalg.eigvals(L_skew).real).max():.1e}")
u0 = 0.1 * np.random.default_rng(1).standard_normal(NX * NY)
u_skew, u_gal = expm(L_skew * T_END) @ u0, expm(L * T_END) @ u0
for name, u in (("start", u0), ("energy-conserving", u_skew), ("Galerkin", u_gal)):
    a = np.abs(u).reshape(NX, NY)
    print(f"{name:17s} max |u| {a.max():8.3f} (column {int(a.max(0).argmax())}), "
          f"interior (columns 5-54) max {a[:, 5:-5].max():.3f}")

cmap = LinearSegmentedColormap.from_list("seq", SEQ)
norm = LogNorm(1e-3, 1e2)
fig, axes = plt.subplots(3, 1, figsize=pal.fig_size(1.0, 0.44), gridspec_kw=dict(hspace=0.45))
for ax, (u, title) in zip(axes, [(u0, "(a) Start: small random values"),
                                 (u_skew, "(b) Energy-conserving form"),
                                 (u_gal, "(c) Galerkin form")]):
    im = ax.imshow(np.abs(u).reshape(NX, NY), norm=norm, cmap=cmap, aspect="auto",
                   interpolation="nearest")
    ax.set_title(title, fontsize=7.5, loc="left", pad=2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
axes[-1].set_xticks([0, NY - 1], ["left edge", "right edge"])
for lab, ha in zip(axes[-1].get_xticklabels(), ("left", "right")):
    lab.set_ha(ha)
cb = fig.colorbar(im, ax=axes, fraction=0.03, pad=0.02)
cb.set_label("Absolute value (log scale)")
save(fig, "fig_method_fen_toy")
