"""Thesis figure style -- single source of truth for colours in Python figures.

Derived from the poster design tokens (masterthesis-docker/poster/tokens.css,
JKU IML blue #0082BA + warm orange accent). The hex values are the poster's;
only the *assignment* of chart series changed, because the thesis reports an
operator survey rather than MP-PDE vs MM-PDE. See style/README.md for the rules.

Usage (from a notebook or script anywhere):

    import sys; sys.path.insert(0, r"D:\\Schule\\MasterThesis\\thesis\\style")
    from palette import apply_thesis_style, ARM, PAL, fig_size
    apply_thesis_style()
    fig, ax = plt.subplots(figsize=fig_size(1.0, 0.55))
    ax.plot(x, y, color=ARM["stencil"], label=ARM_LABEL["stencil"])
    fig.savefig("images/fig_xyz.pdf")
"""
from __future__ import annotations

# --------------------------------------------------------------------------
# Base tokens (identical hex values to poster/tokens.css)
# --------------------------------------------------------------------------
PAL = dict(
    primary="#0082BA",       # JKU IML blue -- structure, emphasis
    primary_700="#00628C",   # darker blue -- text-strength blue, table heads
    primary_300="#6FC0DF",   # light blue -- rules, light fills
    primary_tint="#E6F3F9",  # very light blue -- panel / figure background tint
    secondary="#0C3C52",     # deep petrol -- dark end of sequential maps
    accent="#E8852B",        # warm orange -- the one thing not to miss
    accent_tint="#FCEBD8",   # light orange -- highlight fill (ink text on it)
    ink="#15242B",           # body text / axis labels
    ink_2="#56676E",         # captions, tick labels, secondary text
    bg="#FFFFFF",
    bg_soft="#F2F7FA",       # panel background
    line="#D5E1E8",          # hairlines, grid, axis spines
    good="#0E7C86",          # teal
    warn="#E8852B",          # orange (= accent)
    muted="#8AA0A9",         # de-emphasised elements
    jku_magenta="#C8004B",   # optional institutional accent -- off by default
)

# Poster chart series (kept for reference / reuse of poster figures)
POSTER_SERIES = dict(
    persistence="#8A9BA3", mppde="#56B4E9", mmpde="#0072B2", baseline="#E8852B",
)

# --------------------------------------------------------------------------
# Thesis arms -> colours. One hue per operator FAMILY; variants of a family
# share the hue (light = plain / smaller variant, full = main variant) and
# are further separated by linestyle or hatch (see ARM_STYLE).
# All hues are Okabe-Ito based, as the poster series were.
# --------------------------------------------------------------------------
ARM = {
    # graph network family -- blue (the locked model is the full blue)
    "stencil":      "#0072B2",  # dilated-stencil GNN (locked model)
    "knn":          "#56B4E9",  # index-space k-NN GNN
    "knn_k20":      "#56B4E9",  # k = 20 variant (dashed)
    "onehop":       "#A9D6F0",  # one-hop floor
    # dense CNN -- orange
    "unet":         "#E8852B",
    # spectral family -- bluish green
    "fno":          "#7CCBB1",  # FNO, global only (light)
    "fno_local":    "#009E73",  # FNO + 3x3 local bypass (full)
    # finite-element family -- reddish purple
    "fen":          "#E3B5CF",  # free-form FEN (light)
    "tfen":         "#CC79A7",  # FEN with transport term (full)
    # references / floors -- greys
    "persistence":  "#8A9BA3",
    "pixel":        "#56676E",  # per-pixel floor (no spatial context)
    "mai2024":      "#15242B",  # external clinical reference: ink, dashed
}
# RK4-wrapped arms reuse the colour of the wrapped backbone with hatch "//"
# (bars) or linestyle ":" (lines): ARM["stencil"] + RK4 -> blue, dotted.

ARM_LABEL = {
    "stencil": "Dilated-stencil GNN",
    "knn": "k-NN GNN",
    "knn_k20": "k-NN GNN, k = 20",
    "onehop": "One-hop floor",
    "unet": "U-Net",
    "fno": "FNO",
    "fno_local": "FNO + 3×3 local",
    "fen": "FEN, free-form",
    "tfen": "T-FEN (transport)",
    "persistence": "Persistence",
    "pixel": "Per-pixel floor",
    "mai2024": "Mai et al. (2024)",
}

ARM_STYLE = {  # linestyle for line plots; bars use ARM_HATCH
    "knn_k20": "--", "mai2024": "--", "persistence": (0, (1, 2)),
}
ARM_HATCH = {"knn_k20": "..", "onehop": "", "pixel": ""}
RK4_LINESTYLE, RK4_HATCH = ":", "//"

# --------------------------------------------------------------------------
# Image / mask overlays (rollout strips, error maps, meshes)
# --------------------------------------------------------------------------
MASK = dict(
    gt="#0C3C52",          # ground-truth lesion fill (petrol)
    pred="#0082BA",        # predicted lesion fill (primary)
    baseline="#8A9BA3",    # baseline lesion (grey outline)
    outline="#15242B",     # contour lines
    background="#F2F7FA",  # panel background behind masks
    pad="#D5E1E8",         # zero-padded (outside-scan) region, hatched
    tp="#0072B2",          # true positive  -- blue
    fp="#E8852B",          # false positive -- orange (over-prediction)
    fn="#CC79A7",          # false negative -- purple (missed growth)
    tn="#FFFFFF",
)
# never red + green: TP/FP/FN are blue / orange / purple.

# Sequential (magnitude, depth maps, density): tint -> light -> primary -> petrol
SEQ = ["#E6F3F9", "#6FC0DF", "#0082BA", "#0C3C52"]
# Diverging (signed change, e.g. shrinkage < 0 < growth, paired deltas)
DIV = ["#0C3C52", "#0082BA", "#6FC0DF", "#F7F7F7", "#F3C08F", "#E8852B", "#8A4210"]

# --------------------------------------------------------------------------
# Page geometry (jkureport, A4, equalmargins=false: 210 - 30 - 45 mm)
# --------------------------------------------------------------------------
TEXTWIDTH_MM = 135.0
TEXTWIDTH_IN = TEXTWIDTH_MM / 25.4  # 5.31 in


def fig_size(width_frac: float = 1.0, aspect: float = 0.62) -> tuple[float, float]:
    """(w, h) in inches for a figure that spans `width_frac` of the text width.
    Include it in LaTeX at the same fraction (\\includegraphics[width=frac\\textwidth])
    so fonts come out at their nominal size."""
    w = TEXTWIDTH_IN * width_frac
    return (w, w * aspect)


def cmap_seq():
    from matplotlib.colors import LinearSegmentedColormap
    return LinearSegmentedColormap.from_list("thesis_seq", SEQ)


def cmap_div():
    from matplotlib.colors import LinearSegmentedColormap
    return LinearSegmentedColormap.from_list("thesis_div", DIV)


def apply_thesis_style() -> None:
    """Set matplotlib rcParams to the thesis look (print-sized, not poster-sized)."""
    import matplotlib as mpl
    from cycler import cycler

    mpl.rcParams.update({
        # Public Sans = the template's sans font (fonts/PublicSans-*.ttf)
        "font.family": "sans-serif",
        "font.sans-serif": ["Public Sans", "Inter", "Arial", "DejaVu Sans"],
        "font.size": 8,
        "axes.titlesize": 9, "axes.titleweight": "semibold",
        "axes.titlecolor": PAL["ink"], "axes.titlelocation": "left",
        "axes.labelsize": 8, "axes.labelcolor": PAL["ink"],
        "xtick.labelsize": 7, "ytick.labelsize": 7,
        "xtick.color": PAL["ink_2"], "ytick.color": PAL["ink_2"],
        "axes.edgecolor": PAL["line"], "axes.linewidth": 0.8,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "axes.grid.axis": "y",
        "grid.color": PAL["line"], "grid.linewidth": 0.5,
        "axes.axisbelow": True,
        "axes.prop_cycle": cycler(color=[
            ARM["stencil"], ARM["unet"], ARM["fno_local"], ARM["tfen"],
            ARM["knn"], ARM["persistence"],
        ]),
        "lines.linewidth": 1.4, "lines.markersize": 4,
        "legend.frameon": False, "legend.fontsize": 7,
        "figure.facecolor": "white", "savefig.facecolor": "white",
        "savefig.dpi": 300, "savefig.bbox": "tight", "savefig.pad_inches": 0.02,
        "pdf.fonttype": 42, "ps.fonttype": 42,  # embed TrueType, keep text editable
        "mathtext.default": "regular",
        "image.cmap": "thesis_seq" if _register_cmaps() else "Blues",
    })


def register_fonts(font_dir: str | None = None) -> None:
    """Register the template's Public Sans TTFs with matplotlib (optional)."""
    from pathlib import Path
    from matplotlib import font_manager
    d = Path(font_dir) if font_dir else Path(__file__).resolve().parents[1] / "fonts"
    for f in d.glob("PublicSans-*.ttf"):
        font_manager.fontManager.addfont(str(f))


def _register_cmaps() -> bool:
    try:
        import matplotlib as mpl
        for cm in (cmap_seq(), cmap_div()):
            if cm.name not in mpl.colormaps:
                mpl.colormaps.register(cm)
        return True
    except Exception:
        return False


def preview(path: str | None = None):
    """Render a swatch sheet of every token (for checking / the README)."""
    import matplotlib.pyplot as plt
    groups = [("Base tokens", PAL), ("Arms", ARM), ("Mask overlays", MASK)]
    n = max(len(g[1]) for g in groups)
    fig, axes = plt.subplots(1, 3, figsize=(10, 0.32 * n + 0.8))
    for ax, (title, d) in zip(axes, groups):
        for i, (k, v) in enumerate(d.items()):
            ax.add_patch(plt.Rectangle((0, -i - 0.8), 0.9, 0.7, fc=v, ec="#D5E1E8", lw=0.5))
            ax.text(1.05, -i - 0.45, f"{k}  {v}", va="center", fontsize=7, family="monospace")
        ax.set_xlim(0, 4.2); ax.set_ylim(-n - 0.2, 0.2); ax.axis("off")
        ax.set_title(title, loc="left", fontsize=9)
    fig.tight_layout()
    if path:
        fig.savefig(path, dpi=200)
    return fig


if __name__ == "__main__":
    import sys
    register_fonts()
    apply_thesis_style()
    preview(sys.argv[1] if len(sys.argv) > 1 else "palette_preview.png")
