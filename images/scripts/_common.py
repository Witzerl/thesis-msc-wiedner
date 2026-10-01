"""Shared set-up for every thesis figure script in images/scripts/.

Each figure script does

    from _common import setup, save, P
    pal = setup()                      # thesis style (style/palette.py), Public Sans
    fig, ax = plt.subplots(figsize=pal.fig_size(1.0, 0.5))
    ...
    save(fig, "fig_experiments_xyz")   # -> images/fig_experiments_xyz.pdf (+ preview PNG)

Rules (style/README.md): colours only from pal.ARM / pal.MASK / pal.PAL, size with
pal.fig_size(frac, aspect) and include the figure at width=frac\\textwidth; plots as
PDF, image-like figures (masks, meshes) as PNG at 300 dpi; masks at the physical
aspect ratio. Numbers come from the run records in masterthesis-docker, read here
(read-only) through the code repo's own thesis_numbers.py where possible, so a figure
and the text quote the same values.

The code repository is read-only: nothing here writes into it.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

THESIS = Path(__file__).resolve().parents[2]
IMAGES = THESIS / "images"
PREVIEW = IMAGES / "_preview"          # PNG previews for checking (git-ignored)
CACHE = IMAGES / "data"                # derived data caches, e.g. rollouts (git-ignored)
STYLE = THESIS / "style"

CODE = THESIS.parent / "masterthesis-docker"
RESULTS = CODE / "GraphPDE" / "results"
DEMOS = CODE / "GraphPDE" / "demos & explanations"
SCANS = CODE / "data" / "MUW_GA" / "scans"
PRECOMP = {f: CODE / "data" / "GA" / f"split{f}_n12_zscore_slo256_agevisit" / "precomp"
           for f in (0, 1, 2)}         # only splits 0-2 are present locally

# Grid geometry (THESIS_FRAMEWORK.md section 1): 49 rows (B-scans) x 1024 columns (A-scans)
NROWS, NCOLS = 49, 1024
DY_MM, DX_MM = 0.12118, 0.00568        # row pitch, column pitch
LY_MM, LX_MM = NROWS * DY_MM, NCOLS * DX_MM   # 5.938 mm tall, 5.816 mm wide
EXTENT = (0.0, LX_MM, LY_MM, 0.0)      # imshow extent (left, right, bottom, top), mm

LATE_FROM = 10                         # late-epoch window: epochs 10-29
FLOOR_REPLICATE = 0.0127               # run-to-run sd
FLOOR_PAIRED = 0.016                   # five-fold paired floor (0.020 with a U-Net)
FLOOR_SINGLE = 0.036                   # single-fold floor


class P:
    """Paths, for scripts that prefer one namespace."""
    thesis, images, preview, cache, style = THESIS, IMAGES, PREVIEW, CACHE, STYLE
    code, results, demos, scans, precomp = CODE, RESULTS, DEMOS, SCANS, PRECOMP


def setup():
    """Apply the thesis matplotlib style and return the palette module."""
    import matplotlib
    matplotlib.use("Agg")
    if str(STYLE) not in sys.path:
        sys.path.insert(0, str(STYLE))
    import palette
    palette.register_fonts(str(THESIS / "fonts"))
    palette.apply_thesis_style()
    return palette


def thesis_numbers():
    """The code repo's thesis_numbers module (paired tests, horizon bins, stability)."""
    if str(DEMOS) not in sys.path:
        sys.path.insert(0, str(DEMOS))
    import thesis_numbers as tn
    return tn


def save(fig, name: str, raster: bool = False, dpi: int = 300) -> Path:
    """Write images/<name>.pdf (or .png when raster=True) and a preview PNG."""
    IMAGES.mkdir(exist_ok=True)
    PREVIEW.mkdir(exist_ok=True)
    out = IMAGES / f"{name}.{'png' if raster else 'pdf'}"
    fig.savefig(out, dpi=dpi)
    fig.savefig(PREVIEW / f"{name}.png", dpi=200)
    print(f"wrote {out}")
    return out


def panel_label(ax, s: str, x: float = -0.02, y: float = 1.02) -> None:
    """Bold panel letter (a), (b), ... at the top left of an axes."""
    ax.text(x, y, s, transform=ax.transAxes, ha="right", va="bottom",
            fontsize=9, fontweight="bold")
