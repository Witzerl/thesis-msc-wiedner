"""Chapter 2, Figure fig:bg:solver-path -- the computational path of a PDE solver.

    cd images/scripts && python fig_bg_solver_path.py

Six panels, read row by row; each title starts with the step that leads to it.
  1 continuous field u(t_k, x)
  2 discretise: the field sampled at the cell centres, u_i^k
  3 classical stencil at cell i: u_{i-1}, u_i, u_{i+1} a distance dx apart, weights
    alpha_{i-1}, alpha_i, alpha_{i+1} in the bars, f_i = 1/dx^2 sum_j alpha_j u_j;
    the weights are fixed (by the derivative the stencil approximates)
  4 learned stencil: the same sum, but the weights are computed from the three values
    by a network with parameters theta, alpha_j(u; theta) (the learned-coefficient idea
    of Bar-Sinai et al. 2019; message-passing networks go further, see 2.3)
  5 slide the stencil: top strip u^k with the stencil window at three positions (the one
    at cell i solid), each linked to the rate it produces in the bottom strip, f_i
  6 time step: one explicit Euler step u^{k+1} = u^k + dt f; old values dashed, the
    change dt * f_i as an arrow per cell; RK4 or any scheme that evaluates f could
    replace it.

The bars are one real step, not drawn by hand: nine cells sampled from a smooth bump,
the second-difference stencil (+1, -2, +1) / dx^2 with dx = 1, dt = 0.3; the two end
cells are held fixed. Illustrative values, not data.
"""
from __future__ import annotations

import numpy as np

from _common import setup, save

N, I = 9, 4                 # cells, highlighted cell
DX, DT = 1.0, 0.3
SLIDE = (1, 4, 7)           # stencil positions drawn in panel 5


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

    fig = plt.figure(figsize=pal.fig_size(1.0, 0.66))
    gs = fig.add_gridspec(3, 2, height_ratios=[0.65, 1.55, 1.15], left=0.02, right=0.98,
                          top=0.95, bottom=0.06, wspace=0.16, hspace=0.75)
    a1, a2 = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1])
    a3, a4 = fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])
    sub = gs[2, 0].subgridspec(2, 1, height_ratios=[1, 1], hspace=0.30)
    a5u, a5 = fig.add_subplot(sub[0]), fig.add_subplot(sub[1])
    a6 = fig.add_subplot(gs[2, 1])

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

    # 3 and 4: the same stencil, weights fixed (3) or computed by a network (4)
    xi = np.array([I - 1, I, I + 1])
    uz = 0.58 * u  # zoomed bars, shortened to leave room for the formula (no y-axis here)
    names = ("$u_{i-1}$", "$u_i$", "$u_{i+1}$")

    def stencil(a, weights, formula, note, learned=False):
        a.bar(xi, uz[xi], width=0.55, color=[nb, hi, nb])
        for xx, nm, w in zip(xi, names, weights):
            a.text(xx, uz[xx] + 0.04, nm, ha="center", va="bottom", fontsize=7.5,
                   color=P["ink"])
            box = (dict(boxstyle="round,pad=0.15", fc=P["accent_tint"], ec=hi, lw=0.6)
                   if learned else None)
            a.text(xx, 0.13, w, ha="center", va="center", fontsize=7,
                   color=P["ink"] if learned else "white", bbox=box)
        a.annotate("", xy=(I - 1, -0.10), xytext=(I, -0.10),
                   arrowprops=dict(arrowstyle="<->", color=P["ink_2"], lw=0.7,
                                   mutation_scale=6), annotation_clip=False)
        a.text(I - 0.5, -0.13, "$\\Delta x$", ha="center", va="top", fontsize=7,
               color=P["ink_2"])
        a.text(I, 1.98, formula, ha="center", va="center", fontsize=8, color=P["ink"])
        a.text(I, 1.52, note, ha="center", va="center", fontsize=7, color=P["ink_2"],
               style="italic")
        a.set_xlim(I - 1.9, I + 1.9); a.set_ylim(0, 2.35)
        a.set_xticks(xi); a.set_xticklabels(lab)
        a.tick_params(axis="x", length=0, pad=12, labelsize=7)
        a.set_yticks([]); a.grid(False); a.spines["left"].set_visible(False)

    stencil(a3, ("$\\alpha_{i-1}$", "$\\alpha_i$", "$\\alpha_{i+1}$"),
            "$f_i = \\dfrac{1}{\\Delta x^2} \\sum_{j} \\alpha_j\\, u_j$",
            "the same weights $\\alpha_j$ at every cell")
    a3.set_title("3  Standard stencil at cell $i$")

    stencil(a4, ("$\\alpha_{i-1}$", "$\\alpha_i$", "$\\alpha_{i+1}$"),
            "$f_i = \\dfrac{1}{\\Delta x^2} \\sum_{j} \\alpha_j(u;\\,\\theta)\\, u_j$",
            "weights $\\alpha_j$ computed by a network $\\theta$",
            learned=True)
    # the network theta reads the three values (grey lines from the value labels)
    net = (I, 1.10)
    a4.add_patch(FancyBboxPatch((net[0] - 0.30, net[1] - 0.08), 0.60, 0.16,
                                boxstyle="round,pad=0.0,rounding_size=0.05",
                                fc=P["accent_tint"], ec=hi, lw=0.8, zorder=4))
    a4.text(net[0], net[1], "$\\theta$", ha="center", va="center", fontsize=8,
            color=P["ink"], zorder=5)
    for xx in xi:
        a4.plot([xx, net[0] + 0.18 * (xx - I)], [uz[xx] + 0.24, net[1] - 0.08],
                color=P["ink_2"], lw=0.6, zorder=2)
    a4.set_title("4  Learned stencil at cell $i$")

    # 5 slide the stencil over u^k (top strip) -> rates (bottom strip)
    a5u.bar(x, u, width=0.86, color=P["line"])
    tidy(a5u, (0, 1.45), ticks=False)
    a5u.spines["bottom"].set_visible(False)
    for c in SLIDE:
        top = u[c - 1:c + 2].max() + 0.08
        a5u.add_patch(Rectangle((c - 1.47, 0.0), 2.94, top, fill=False,
                                ec=hi if c == I else nb, lw=1.1,
                                ls="-" if c == I else (0, (3, 2))))
    a5u.annotate("", xy=(N - 1.2, 1.18), xytext=(0.2, 1.18),
                 arrowprops=dict(arrowstyle="-|>", color=P["ink_2"], lw=0.7, mutation_scale=6))
    a5u.text((N - 1) / 2, 1.24, "the stencil slides over every cell", ha="center",
             va="bottom", fontsize=6.5, color=P["ink_2"])
    a5.bar(x, f, width=0.86, color=cols)
    a5.axhline(0, color=P["ink_2"], lw=0.6)
    a5.text(I + 0.55, f[I], "$f_i$", ha="left", va="center", fontsize=7.5, color=P["ink"])
    tidy(a5, (-0.68, 0.36))
    a5.spines["bottom"].set_visible(False)
    for c in SLIDE:
        fig.add_artist(ConnectionPatch((c, 0.0), (c, max(f[c], 0) + 0.02), "data", "data",
                                       axesA=a5u, axesB=a5, color=hi if c == I else nb,
                                       lw=0.7, ls=(0, (1, 1.5)), arrowstyle="-|>",
                                       mutation_scale=6))
    a5u.set_title("5  Slide the stencil: rates $f_i$")

    # 6 time step: formula on top, next state below (old values dashed, change as arrows)
    a6.bar(x, u, width=0.86, color="none", edgecolor=P["muted"], ls=(0, (2, 1.5)), lw=0.7)
    a6.bar(x, u1, width=0.86, color=cols, alpha=0.95)
    for xx in x:
        if abs(u1[xx] - u[xx]) > 0.02:
            a6.annotate("", xy=(xx, u1[xx]), xytext=(xx, u[xx]),
                        arrowprops=dict(arrowstyle="-|>", color=P["ink"], lw=0.7,
                                        mutation_scale=6, shrinkA=0, shrinkB=0))
    a6.text(-0.5, 1.30, "$u_i^{k+1} = u_i^k + \\Delta t\\, f_i$", ha="left", va="center",
            fontsize=8, color=P["ink"])
    a6.text(N - 0.5, 1.00, "RK4 or any scheme\nthat evaluates $f$\ncan replace Euler",
            ha="right", va="top", fontsize=6.5, color=P["ink_2"], style="italic")
    tidy(a6, (0, 1.42))
    a6.set_title("6  Time step: next state $u_i^{k+1}$")

    save(fig, "fig_bg_solver_path")
    plt.close(fig)


if __name__ == "__main__":
    main()
