"""Chapter 2, Figure fig:bg:solver-path -- the computational path of a classical PDE solver.

    cd images/scripts && python fig_bg_solver_path.py

Two rows, read left to right, then the second row:
  1 continuous field u(t_k, x)            2 grid: one value per cell, u_i^k
  3 stencil: f_i = sum_j alpha_j u_j       (cells i-1, i, i+1 with their weights)
  4 rates f_i for every cell               5 time stepper (Euler, RK4, ... -- any scheme
                                             that only calls f)
  6 next state u^{k+1}, old values dashed; dashed arrow back to 2: rollout.

The numbers are one real step, not drawn by hand: nine cells sampled from a smooth bump,
the three-point second-difference stencil alpha = (1, -2, 1) / dx^2 (dx = 1), and one
explicit Euler step with dt = 0.3. The stencil approximates the second derivative, so
the step flattens the peak and raises the flanks. Illustrative values, not data.
"""
from __future__ import annotations

import numpy as np

from _common import setup, save

N, I = 9, 4                 # cells, highlighted cell
DT = 0.3
ALPHA = (1, -2, 1)


def field(x):
    return 0.10 + 0.80 * np.exp(-((x - 4.0) ** 2) / 2.2)


def main():
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
    pal = setup()
    P, A = pal.PAL, pal.ARM
    hi, nb, base = P["accent"], A["stencil"], P["primary_300"]

    x = np.arange(N)
    u = field(x)
    f = np.zeros(N)
    f[1:-1] = ALPHA[0] * u[:-2] + ALPHA[1] * u[1:-1] + ALPHA[2] * u[2:]
    u1 = u + DT * f
    print("u   ", np.round(u, 3)); print("f   ", np.round(f, 3)); print("u+1 ", np.round(u1, 3))

    fig = plt.figure(figsize=pal.fig_size(1.0, 0.60))
    gs = fig.add_gridspec(2, 3, left=0.02, right=0.93, top=0.82, bottom=0.05,
                          wspace=0.42, hspace=0.80)
    ax = [[fig.add_subplot(gs[r, c]) for c in range(3)] for r in range(2)]
    (a1, a2, a3), (a4, a5, a6) = ax

    def colours(stencil=False):
        c = [base] * N
        if stencil:
            c[I - 1] = c[I + 1] = nb
        c[I] = hi
        return c

    def tidy(a, ylim=(0, 1.0), ticks=True):
        a.set_ylim(*ylim); a.set_yticks([]); a.grid(False)
        a.spines["left"].set_visible(False)
        if ticks:
            a.set_xticks([I - 1, I, I + 1]); a.set_xticklabels(["$i\\!-\\!1$", "$i$", "$i\\!+\\!1$"])
            a.tick_params(axis="x", length=2, pad=1, labelsize=7)
        else:
            a.set_xticks([])

    # 1 continuous field
    xs = np.linspace(-0.4, N - 0.6, 300)
    a1.plot(xs, field(xs), color=P["primary"], lw=1.4)
    a1.set_xlim(-0.6, N - 0.4); tidy(a1, ticks=False)
    a1.set_xlabel("$x$", labelpad=1, color=P["ink_2"])
    a1.set_title("1  Continuous field $u(t_k, x)$")

    # 2 grid: one value per cell, sampled at the cell centres
    a2.bar(x, u, width=0.86, color=colours(True))
    a2.plot(xs, field(xs), color=P["ink_2"], lw=0.6, ls=":")
    a2.plot(x, u, "o", ms=2.2, color=P["ink"])
    a2.set_xlim(-0.6, N - 0.4); tidy(a2)
    a2.set_title("2  Grid values $u_i^k$")

    # 3 stencil: the three cells with their weights and the formula
    xi = np.array([I - 1, I, I + 1])
    a3.bar(xi, u[xi], width=0.8, color=[nb, hi, nb])
    for xx, al in zip(xi, ALPHA):
        a3.text(xx, -0.10, f"$\\alpha = {al:+d}$", ha="center", va="top", fontsize=7,
                color=P["ink"])
    a3.text(I, 1.12, "$f_i = \\sum_{j} \\alpha_j\\, u_j \\,/\\, \\Delta x^2$", ha="center",
            va="center", fontsize=8, color=P["ink"])
    a3.set_xlim(I - 1.7, I + 1.7); tidy(a3, ylim=(0, 1.3), ticks=False)
    a3.set_title("3  Stencil")
    a3.set_xticks(xi); a3.set_xticklabels(["$i\\!-\\!1$", "$i$", "$i\\!+\\!1$"])
    a3.tick_params(axis="x", length=0, pad=14, labelsize=7)

    # 4 rates for every cell
    c4 = [base] * N; c4[I] = hi
    a4.bar(x, f, width=0.86, color=c4)
    a4.axhline(0, color=P["ink_2"], lw=0.6)
    a4.set_xlim(-0.6, N - 0.4); tidy(a4, ylim=(-0.7, 0.35))
    a4.spines["bottom"].set_visible(False)
    a4.set_title("4  Rates $f_i$")

    # 5 time stepper: any scheme that only calls f
    a5.set_axis_off(); a5.set_xlim(0, 1); a5.set_ylim(0, 1)
    a5.add_patch(FancyBboxPatch((0.0, 0.05), 1.0, 0.9, boxstyle="round,pad=0.0,rounding_size=0.04",
                                fc=P["primary_tint"], ec=P["primary"], lw=0.8))
    a5.text(0.5, 0.72, "Euler: $u^{k+1} = u^k + \\Delta t\\, f$", ha="center",
            va="center", fontsize=7.5, color=P["ink"])
    a5.text(0.5, 0.48, "RK4: four calls of $f$", ha="center", va="center",
            fontsize=7.5, color=P["ink"])
    a5.text(0.5, 0.24, "any scheme that calls $f$", ha="center", va="center",
            fontsize=7, color=P["ink_2"], style="italic")
    a5.set_title("5  Time step $\\Delta t$")

    # 6 next state, old values dashed
    a6.bar(x, u, width=0.86, color="none", edgecolor=P["muted"], ls=(0, (2, 1.5)), lw=0.7)
    c6 = [base] * N; c6[I] = hi
    a6.bar(x, u1, width=0.86, color=c6, alpha=0.95)
    a6.set_xlim(-0.6, N - 0.4); tidy(a6)
    a6.set_title("6  Next state $u_i^{k+1}$")

    # arrows between the panels (figure coordinates)
    def arrow(p, q, style="-|>", ls="-", colour=None, conn="arc3"):
        fig.add_artist(FancyArrowPatch(p, q, transform=fig.transFigure, arrowstyle=style,
                                       mutation_scale=8, lw=0.8, ls=ls, connectionstyle=conn,
                                       color=colour or P["ink"]))

    def box(a):
        return a.get_position()

    for l, r in ((a1, a2), (a2, a3), (a4, a5), (a5, a6)):
        bl, br = box(l), box(r)
        y = (bl.y0 + bl.y1) / 2
        arrow((bl.x1 + 0.008, y), (br.x0 - 0.008, y))
    # end of row 1 -> start of row 2
    b3, b4 = box(a3), box(a4)
    ymid = (b3.y0 + b4.y1) / 2 + 0.01
    xr = b3.x1 + 0.02
    fig.add_artist(plt.Line2D([b3.x1 + 0.005, xr, xr, b4.x0 - 0.015, b4.x0 - 0.015],
                              [(b3.y0 + b3.y1) / 2, (b3.y0 + b3.y1) / 2, ymid, ymid,
                               (b4.y0 + b4.y1) / 2], transform=fig.transFigure,
                              color=P["ink"], lw=0.8))
    arrow((b4.x0 - 0.015, (b4.y0 + b4.y1) / 2 + 0.001), (b4.x0 - 0.003, (b4.y0 + b4.y1) / 2))
    # rollout: next state -> grid of the next step
    b6, b2 = box(a6), box(a2)
    xo = b6.x1 + 0.035
    yo = 0.965
    fig.add_artist(plt.Line2D([b6.x1 + 0.005, xo, xo, (b2.x0 + b2.x1) / 2],
                              [(b6.y0 + b6.y1) / 2, (b6.y0 + b6.y1) / 2, yo, yo],
                              transform=fig.transFigure, color=P["ink_2"], lw=0.8,
                              ls=(0, (3, 2))))
    arrow(((b2.x0 + b2.x1) / 2, yo), ((b2.x0 + b2.x1) / 2, b2.y1 + 0.075), ls=(0, (3, 2)),
          colour=P["ink_2"])
    fig.text((b2.x1 + box(a3).x0) / 2, yo + 0.008,
             "rollout: $u^{k+1}$ is the input of the next step",
             ha="center", va="bottom", fontsize=7, color=P["ink_2"])

    save(fig, "fig_bg_solver_path")
    plt.close(fig)


if __name__ == "__main__":
    main()
