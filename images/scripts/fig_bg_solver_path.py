"""Chapter 2, Figure fig:bg:solver-path -- the computational path of a classical PDE solver.

    cd images/scripts && python fig_bg_solver_path.py

Reading order 1-6, row by row. Each panel title starts with the step that leads to it
(discretise, stencil, slide the stencil, time step). The right column (2, 4, 6) shares
one x-axis, so a cell's value, its rate and its new value sit directly above one another;
the left column (1, 3, 5) shows the operation, worked out for cell i:
  1 continuous field u(t_k, x)
  2 discretise: the field sampled at the cell centres, u_i^k
  3 stencil at cell i: u_{i-1}, u_i, u_{i+1} a distance dx apart, weights alpha = +1, -2, +1 in
    the bars, formula f_i = 1/dx^2 * sum_{j=i-1}^{i+1} alpha_j u_j
  4 slide the stencil: top strip u^k with the stencil window at three positions (the one
    at cell i solid), each linked to the rate it produces in the bottom strip, f_i
  5 time step for cell i, one explicit Euler step; RK4 or any scheme that evaluates f
    could replace it
  6 next state: old values dashed, the change dt * f_i drawn as an arrow per cell.

The numbers are one real step, not drawn by hand: nine cells sampled from a smooth bump,
dx = 1, dt = 0.3; the two end cells are held fixed. Illustrative values, not data.
"""
from __future__ import annotations

import numpy as np

from _common import setup, save

N, I = 9, 4                 # cells, highlighted cell
DX, DT = 1.0, 0.3
SLIDE = (1, 4, 7)           # stencil positions drawn in panel 4


def field(x):
    return 0.10 + 0.80 * np.exp(-((x - 4.0) ** 2) / 2.2)


def main():
    import matplotlib.pyplot as plt
    from matplotlib.patches import ConnectionPatch, FancyBboxPatch, Rectangle
    pal = setup()
    P, A = pal.PAL, pal.ARM
    hi, nb, base = P["accent"], A["stencil"], P["primary_300"]

    x = np.arange(N)
    u = field(x)
    f = np.zeros(N)
    f[1:-1] = (u[:-2] - 2 * u[1:-1] + u[2:]) / DX ** 2
    u1 = u + DT * f
    print("u   ", np.round(u, 3)); print("f   ", np.round(f, 3)); print("u+1 ", np.round(u1, 3))

    fig = plt.figure(figsize=pal.fig_size(1.0, 0.64))
    gs = fig.add_gridspec(3, 2, width_ratios=[1, 1.25], height_ratios=[1, 1.6, 1],
                          left=0.02, right=0.98, top=0.95, bottom=0.04, wspace=0.22,
                          hspace=0.62)
    a1, a2 = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1])
    sub3 = gs[1, 0].subgridspec(1, 2, wspace=0.10)
    a3, a3g = fig.add_subplot(sub3[0]), fig.add_subplot(sub3[1])
    sub =gs[1, 1].subgridspec(2, 1, height_ratios=[1, 1], hspace=0.30)
    a4u, a4 = fig.add_subplot(sub[0]), fig.add_subplot(sub[1])
    a5, a6 = fig.add_subplot(gs[2, 0]), fig.add_subplot(gs[2, 1])

    cols = [base] * N
    cols[I] = hi
    cols_st = list(cols); cols_st[I - 1] = cols_st[I + 1] = nb
    lab = ["$i\\!-\\!1$", "$i$", "$i\\!+\\!1$"]

    def tidy(a, ylim, ticks=True):
        a.set_ylim(*ylim); a.set_yticks([]); a.grid(False)
        a.spines["left"].set_visible(False)
        a.set_xlim(-0.6, N - 0.4)
        if ticks:
            a.set_xticks([I - 1, I, I + 1]); a.set_xticklabels(lab)
            a.tick_params(axis="x", length=2, pad=1, labelsize=7)
        else:
            a.set_xticks([])
        a.axvline(I, color=hi, lw=0.6, ls=(0, (1, 2)), zorder=0)

    xs = np.linspace(-0.4, N - 0.6, 300)

    # 1 continuous field
    a1.plot(xs, field(xs), color=P["primary"], lw=1.4)
    a1.set_xlim(-0.6, N - 0.4); a1.set_ylim(0, 1.05)
    a1.set_yticks([]); a1.set_xticks([]); a1.grid(False); a1.spines["left"].set_visible(False)
    a1.set_xlabel("$x$", labelpad=1, color=P["ink_2"])
    a1.set_title("1  Continuous field $u(t_k, x)$")

    # 2 discretise
    a2.bar(x, u, width=0.86, color=cols_st)
    a2.plot(xs, field(xs), color=P["ink_2"], lw=0.6, ls=":")
    a2.plot(x, u, "o", ms=2.2, color=P["ink"], zorder=3)
    tidy(a2, (0, 1.05))
    a2.set_title("2  Discretise: grid values $u_i^k$")

    # 3 stencil at cell i: classical (left, weights fixed) and GNN (right, learned)
    xi = np.array([I - 1, I, I + 1])
    uz = 0.72 * u  # zoomed bars, shortened to leave room for the formula (no y-axis here)
    names = ("$u_{i-1}$", "$u_i$", "$u_{i+1}$")
    a3.bar(xi, uz[xi], width=0.62, color=[nb, hi, nb])
    for xx, nm, w in zip(xi, names, ("$\\alpha_{i-1}$", "$\\alpha_i$", "$\\alpha_{i+1}$")):
        a3.text(xx, uz[xx] + 0.05, nm, ha="center", va="bottom", fontsize=7.5, color=P["ink"])
        a3.text(xx, 0.13, w, ha="center", va="center", fontsize=7, color="white")
    a3.annotate("", xy=(I - 1, -0.10), xytext=(I, -0.10),
                arrowprops=dict(arrowstyle="<->", color=P["ink_2"], lw=0.7, mutation_scale=6),
                annotation_clip=False)
    a3.text(I - 0.5, -0.13, "$\\Delta x$", ha="center", va="top", fontsize=7, color=P["ink_2"])
    a3.text(I, 1.40, "$f_i = \\dfrac{1}{\\Delta x^2} \\sum_{j} \\alpha_j\\, u_j$",
            ha="center", va="center", fontsize=8, color=P["ink"])
    a3.text(I, 1.08, "classical: $\\alpha_j$ fixed", ha="center", va="center", fontsize=7,
            color=P["ink_2"], style="italic")
    a3.set_xlim(I - 1.55, I + 1.55); a3.set_ylim(0, 1.75)
    a3.set_xticks(xi); a3.set_xticklabels(lab)
    a3.tick_params(axis="x", length=0, pad=12, labelsize=7)
    a3.set_yticks([]); a3.grid(False); a3.spines["left"].set_visible(False)
    a3.set_title("3  Stencil at cell $i$")

    # GNN version of the same stencil: the cells are graph nodes, the weights become
    # learned messages phi along the edges into node i (intuition only, cf. Eqs. 4.3-4.4)
    a3g.set_xlim(I - 1.55, I + 1.55); a3g.set_ylim(0, 1.75); a3g.set_axis_off()
    yn = 0.40
    xg = np.array([I - 1.15, I, I + 1.15])     # node positions, spread a little for the edges
    a3g.scatter(xg, [yn] * 3, s=260, c=[nb, hi, nb], zorder=3, linewidths=0)
    for xx, nm in zip(xg, names):
        a3g.text(xx, yn, nm, ha="center", va="center", fontsize=6.5, color="white", zorder=4)
    for xx in (xg[0], xg[2]):
        a3g.annotate("", xy=(I, yn), xytext=(xx, yn),
                     arrowprops=dict(arrowstyle="-|>", color=P["ink"], lw=0.9, mutation_scale=8,
                                     shrinkA=8, shrinkB=8))
        a3g.text((xx + I) / 2, yn + 0.20, "$\\varphi_\\theta$", ha="center", va="center",
                 fontsize=7.5, color=P["ink"])
    a3g.text(I, 1.40, "$f_i = \\psi_\\theta\\left(u_i, \\sum_j \\varphi_\\theta(u_i, u_j)\\right)$",
             ha="center", va="center", fontsize=7.5, color=P["ink"])
    a3g.text(I, 1.08, "GNN: $\\varphi_\\theta, \\psi_\\theta$ learned", ha="center",
             va="center", fontsize=7, color=P["ink_2"], style="italic")

    # 4 slide the stencil over u^k (top strip) -> rates (bottom strip)
    a4u.bar(x, u, width=0.86, color=P["line"])
    tidy(a4u, (0, 1.45), ticks=False)
    a4u.spines["bottom"].set_visible(False)
    for c in SLIDE:
        top = u[c - 1:c + 2].max() + 0.08
        a4u.add_patch(Rectangle((c - 1.47, 0.0), 2.94, top, fill=False,
                                ec=hi if c == I else nb, lw=1.1,
                                ls="-" if c == I else (0, (3, 2))))
    a4u.annotate("", xy=(N - 1.2, 1.18), xytext=(0.2, 1.18),
                 arrowprops=dict(arrowstyle="-|>", color=P["ink_2"], lw=0.7, mutation_scale=6))
    a4u.text((N - 1) / 2, 1.24, "the stencil slides over every cell", ha="center",
             va="bottom", fontsize=6.5, color=P["ink_2"])
    a4.bar(x, f, width=0.86, color=cols)
    a4.axhline(0, color=P["ink_2"], lw=0.6)
    a4.text(I + 0.55, f[I], "$f_i$", ha="left", va="center", fontsize=7.5, color=P["ink"])
    tidy(a4, (-0.68, 0.36))
    a4.spines["bottom"].set_visible(False)
    for c in SLIDE:
        fig.add_artist(ConnectionPatch((c, 0.0), (c, max(f[c], 0) + 0.02), "data", "data",
                                       axesA=a4u, axesB=a4, color=hi if c == I else nb,
                                       lw=0.7, ls=(0, (1, 1.5)), arrowstyle="-|>",
                                       mutation_scale=6))
    a4u.set_title("4  Slide the stencil: rates $f_i$")

    # 5 time step for cell i
    a5.set_axis_off(); a5.set_xlim(0, 1); a5.set_ylim(0, 1)
    a5.add_patch(FancyBboxPatch((0.0, 0.08), 1.0, 0.84,
                                boxstyle="round,pad=0.0,rounding_size=0.04",
                                fc=P["primary_tint"], ec=P["primary"], lw=0.8))
    a5.text(0.5, 0.66, "$u_i^{k+1} = u_i^k + \\Delta t\\, f_i$", ha="center", va="center",
            fontsize=8, color=P["ink"])
    a5.text(0.5, 0.32, "explicit Euler; RK4 or any scheme\nthat evaluates $f$ can replace it",
            ha="center", va="center", fontsize=6.5, color=P["ink_2"], style="italic")
    a5.set_title("5  Time step")

    # 6 next state: old values dashed, change dt * f_i as arrows
    a6.bar(x, u, width=0.86, color="none", edgecolor=P["muted"], ls=(0, (2, 1.5)), lw=0.7)
    a6.bar(x, u1, width=0.86, color=cols, alpha=0.95)
    for xx in x:
        if abs(u1[xx] - u[xx]) > 0.02:
            a6.annotate("", xy=(xx, u1[xx]), xytext=(xx, u[xx]),
                        arrowprops=dict(arrowstyle="-|>", color=P["ink"], lw=0.7,
                                        mutation_scale=6, shrinkA=0, shrinkB=0))
    tidy(a6, (0, 1.05))
    a6.set_title("6  Next state $u_i^{k+1}$ (dashed: $u_i^k$)")

    save(fig, "fig_bg_solver_path")
    plt.close(fig)


if __name__ == "__main__":
    main()
