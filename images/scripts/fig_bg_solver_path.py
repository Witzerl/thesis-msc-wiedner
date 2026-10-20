"""Chapter 2, Figure fig:bg:solver-path -- the computational path of a classical PDE solver.

    cd images/scripts && python fig_bg_solver_path.py

Reading order 1-6, zig-zag. The right column (2, 4, 6) shares one x-axis, so a cell's
value, its rate and its new value sit directly above one another; the left column
(1, 3, 5) shows how each right-hand panel is obtained, worked out for cell i:
  1 continuous field u(t_k, x)
  2 grid: the field sampled at the cell centres, u_i^k
  3 stencil for cell i: the parabola through u_{i-1}, u_i, u_{i+1} (dashed); its second
    derivative is f_i = (u_{i-1} - 2 u_i + u_{i+1}) / dx^2 (weights +1, -2, +1; dx the
    cell spacing). Equivalently f_i = 2 (mean of the neighbours - u_i) / dx^2: a cell
    above its neighbours' mean gets a negative rate. Numbers of cell i filled in.
  4 the same stencil at every cell: rates f_i
  5 time step for cell i, one explicit Euler step with numbers filled in; RK4 or any
    scheme that evaluates f could replace it
  6 next state: old values dashed, the change dt * f_i drawn as an arrow per cell.

The numbers are one real step, not drawn by hand: nine cells sampled from a smooth bump,
dx = 1, dt = 0.3; the two end cells are held fixed. Illustrative values, not data.
"""
from __future__ import annotations

import numpy as np

from _common import setup, save

N, I = 9, 4                 # cells, highlighted cell
DX, DT = 1.0, 0.3


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
    f[1:-1] = (u[:-2] - 2 * u[1:-1] + u[2:]) / DX ** 2
    u1 = u + DT * f
    ul, ui, ur = u[I - 1], u[I], u[I + 1]
    print("u   ", np.round(u, 3)); print("f   ", np.round(f, 3)); print("u+1 ", np.round(u1, 3))
    print(f"cell i: {ul:.2f} {ui:.2f} {ur:.2f} -> f_i {f[I]:.3f} -> u_i^k+1 {u1[I]:.3f}")

    fig = plt.figure(figsize=pal.fig_size(1.0, 0.64))
    gs = fig.add_gridspec(3, 2, width_ratios=[1, 1.25], left=0.02, right=0.98, top=0.95,
                          bottom=0.04, wspace=0.30, hspace=0.75)
    a1, a2 = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1])
    a3, a4 = fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])
    a5, a6 = fig.add_subplot(gs[2, 0]), fig.add_subplot(gs[2, 1])

    cols = [base] * N
    cols[I] = hi
    cols_st = list(cols); cols_st[I - 1] = cols_st[I + 1] = nb

    def tidy(a, ylim):
        a.set_ylim(*ylim); a.set_yticks([]); a.grid(False)
        a.spines["left"].set_visible(False)
        a.set_xlim(-0.6, N - 0.4)
        a.set_xticks([I - 1, I, I + 1])
        a.set_xticklabels(["$i\\!-\\!1$", "$i$", "$i\\!+\\!1$"])
        a.tick_params(axis="x", length=2, pad=1, labelsize=7)
        a.axvline(I, color=hi, lw=0.6, ls=(0, (1, 2)), zorder=0)

    xs = np.linspace(-0.4, N - 0.6, 300)

    # 1 continuous field
    a1.plot(xs, field(xs), color=P["primary"], lw=1.4)
    a1.set_xlim(-0.6, N - 0.4); a1.set_ylim(0, 1.05)
    a1.set_yticks([]); a1.set_xticks([]); a1.grid(False); a1.spines["left"].set_visible(False)
    a1.set_xlabel("$x$", labelpad=1, color=P["ink_2"])
    a1.set_title("1  Continuous field $u(t_k, x)$")

    # 2 grid values
    a2.bar(x, u, width=0.86, color=cols_st)
    a2.plot(xs, field(xs), color=P["ink_2"], lw=0.6, ls=":")
    a2.plot(x, u, "o", ms=2.2, color=P["ink"], zorder=3)
    tidy(a2, (0, 1.05))
    a2.set_title("2  Grid values $u_i^k$ (one per cell)")

    # 3 stencil for cell i: parabola through the three values, dx, neighbour mean
    xi = np.array([I - 1, I, I + 1])
    a3.bar(xi, u[xi], width=0.55, color=[nb, hi, nb])
    c2, c1, c0 = np.polyfit(xi - I, u[xi], 2)
    xp = np.linspace(-1.35, 1.35, 100)
    a3.plot(xp + I, c2 * xp ** 2 + c1 * xp + c0, color=P["ink"], lw=0.8, ls=(0, (3, 2)))
    for xx in xi:
        a3.text(xx, u[xx] + 0.04, f"{u[xx]:.2f}", ha="center", va="bottom", fontsize=7,
                color=P["ink"])
    mean = (ul + ur) / 2
    a3.plot([I - 0.42, I + 0.42], [mean, mean], color=P["ink"], lw=0.8)
    for xx, w in zip(xi, ("$+1$", "$-2$", "$+1$")):
        a3.text(xx, 0.12, w, ha="center", va="center", fontsize=7.5, color="white")
    a3.annotate("", xy=(I - 1, -0.10), xytext=(I, -0.10),
                arrowprops=dict(arrowstyle="<->", color=P["ink_2"], lw=0.7, mutation_scale=6),
                annotation_clip=False)
    a3.text(I - 0.5, -0.13, "$\\Delta x$", ha="center", va="top", fontsize=7, color=P["ink_2"])
    a3.text(I, 1.78, "$f_i = (u_{i-1} - 2u_i + u_{i+1})\\, /\\, \\Delta x^2$",
            ha="center", va="center", fontsize=7.5, color=P["ink"])
    a3.text(I, 1.45, f"$= ({ul:.2f} - 2 \\cdot {ui:.2f} + {ur:.2f})\\, /\\, 1^2 = {f[I]:.2f}$",
            ha="center", va="center", fontsize=7.5, color=P["ink"])
    a3.set_xlim(I - 1.6, I + 1.6); a3.set_ylim(0, 1.95)
    a3.set_xticks(xi); a3.set_xticklabels(["$i\\!-\\!1$", "$i$", "$i\\!+\\!1$"])
    a3.tick_params(axis="x", length=0, pad=12, labelsize=7)
    a3.set_yticks([]); a3.grid(False); a3.spines["left"].set_visible(False)
    a3.set_title("3  Stencil, here for cell $i$")

    # 4 rates for every cell
    a4.bar(x, f, width=0.86, color=cols)
    a4.axhline(0, color=P["ink_2"], lw=0.6)
    a4.text(I + 0.55, f[I], f"$f_i = {f[I]:.2f}$", ha="left", va="center", fontsize=7,
            color=P["ink"])
    tidy(a4, (-0.68, 0.36))
    a4.spines["bottom"].set_visible(False)
    a4.set_title("4  Rates $f_i$ (the stencil at every cell)")

    # 5 time step for cell i
    a5.set_axis_off(); a5.set_xlim(0, 1); a5.set_ylim(0, 1)
    a5.add_patch(FancyBboxPatch((0.0, 0.08), 1.0, 0.84,
                                boxstyle="round,pad=0.0,rounding_size=0.04",
                                fc=P["primary_tint"], ec=P["primary"], lw=0.8))
    a5.text(0.5, 0.74, "$u_i^{k+1} = u_i^k + \\Delta t\\, f_i$", ha="center", va="center",
            fontsize=8, color=P["ink"])
    # result from the rounded numbers shown, so that the arithmetic on the page adds up
    shown = round(ui, 2) + DT * round(f[I], 2)
    a5.text(0.5, 0.52, f"$= {ui:.2f} + {DT:.1f} \\cdot ({f[I]:.2f}) = {shown:.2f}$",
            ha="center", va="center", fontsize=8, color=P["ink"])
    a5.text(0.5, 0.26, "explicit Euler; RK4 or any scheme\nthat evaluates $f$ can replace it",
            ha="center", va="center", fontsize=6.5, color=P["ink_2"], style="italic")
    a5.set_title("5  Time step, here for cell $i$")

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

    # flow arrows (figure coordinates): 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5, 5 -> 6
    def arrow(p, q, rad=0.0):
        fig.add_artist(FancyArrowPatch(p, q, transform=fig.transFigure, arrowstyle="-|>",
                                       mutation_scale=8, lw=0.8, color=P["ink"],
                                       connectionstyle=f"arc3,rad={rad}"))

    pos = {k: a.get_position() for k, a in enumerate((a1, a2, a3, a4, a5, a6), 1)}
    for l, r in ((1, 2), (3, 4), (5, 6)):
        bl, br = pos[l], pos[r]
        y = (bl.y0 + bl.y1) / 2
        arrow((bl.x1 + 0.01, y), (br.x0 - 0.01, y))
    for top, bot in ((2, 3), (4, 5)):
        bt, bb = pos[top], pos[bot]
        # from below panel 2 / 4 to the right end of the title row of panel 3 / 5
        arrow((bt.x0 + 0.01, bt.y0 - 0.045), (bb.x1 + 0.005, bb.y1 + 0.03))

    save(fig, "fig_bg_solver_path")
    plt.close(fig)


if __name__ == "__main__":
    main()
