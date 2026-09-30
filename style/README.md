# Thesis colour and figure rules

The thesis uses the same colours as the poster
(`masterthesis-docker/poster/tokens.css`, `design-system.html`): JKU IML blue
`#0082BA` for structure, one warm orange `#E8852B` for emphasis, cool neutrals
for everything else. The hex values are unchanged. Only the chart-series
assignment is new, because the poster compared MP-PDE and MM-PDE and the thesis
compares operator families.

| File | Use |
|---|---|
| `palette.py` | Python figures: `apply_thesis_style()`, `PAL`, `ARM`, `ARM_LABEL`, `MASK`, `SEQ`/`DIV` colormaps, `fig_size()` |
| `thesis-colors.sty` | LaTeX: the same colours as `xcolor` names (`gaPrimary`, `armStencil`, `maskFP`, ...) and `\armkey{...}` |
| `palette_preview.png` | Swatch sheet, regenerate with `python palette.py palette_preview.png` |

If a colour changes, change it in `palette.py` **and** `thesis-colors.sty` on
the same commit.

## Base tokens

| Token | Hex | Role |
|---|---|---|
| primary | `#0082BA` | JKU IML blue: structure, emphasis in figures |
| primary_700 | `#00628C` | blue at text strength |
| primary_300 | `#6FC0DF` | light fills, rules |
| primary_tint | `#E6F3F9` | panel / figure-frame tint |
| secondary | `#0C3C52` | deep petrol: dark end of sequential maps, GT lesion |
| accent | `#E8852B` | orange: the one thing the reader must not miss |
| accent_tint | `#FCEBD8` | highlight fill (dark text on it, never white) |
| ink | `#15242B` | text, axis labels |
| ink_2 | `#56676E` | tick labels, secondary text |
| bg_soft | `#F2F7FA` | panel background |
| line | `#D5E1E8` | hairlines, grid, spines |
| good | `#0E7C86` | teal |
| muted | `#8AA0A9` | de-emphasised elements |

## Operator arms

One hue per operator family. Within a family the main variant takes the full
colour and the plain or smaller variant the light one.

| Arm | Key | Hex |
|---|---|---|
| Dilated-stencil GNN (locked model) | `stencil` | `#0072B2` |
| k-NN GNN | `knn` | `#56B4E9` |
| k-NN GNN, k = 20 | `knn_k20` | `#56B4E9`, dashed / dotted hatch |
| One-hop floor | `onehop` | `#A9D6F0` |
| U-Net | `unet` | `#E8852B` |
| FNO | `fno` | `#7CCBB1` |
| FNO + 3×3 local | `fno_local` | `#009E73` |
| FEN, free-form | `fen` | `#E3B5CF` |
| T-FEN (transport) | `tfen` | `#CC79A7` |
| Any backbone + RK4 | | backbone colour, linestyle `:` / hatch `//` |
| Persistence | `persistence` | `#8A9BA3`, reference line only |
| Per-pixel floor | `pixel` | `#56676E`, reference line only |
| Mai et al. (2024) | `mai2024` | `#15242B`, dashed |

## Masks and error maps

| Element | Hex |
|---|---|
| Ground-truth lesion | `#0C3C52` |
| Predicted lesion | `#0082BA` |
| Baseline lesion | `#8A9BA3` outline |
| True positive | `#0072B2` blue |
| False positive (over-prediction) | `#E8852B` orange |
| False negative (missed growth) | `#CC79A7` purple |
| Zero-padded region | `#D5E1E8`, hatched |

Sequential maps (depth maps, magnitudes): `SEQ` = tint → light blue → primary →
petrol. Signed maps (paired deltas, growth vs shrinkage): `DIV` = petrol/blue ↔
light grey ↔ orange, centred on 0 with a symmetric range.

## Rules

1. **Each arm keeps one colour in every figure.** Take it from `ARM`, never
   from the matplotlib default cycle.
2. **Never red and green together.** Error maps use blue / orange / purple.
3. **Greys are references, not series.** Persistence and the per-pixel floor
   are dashed horizontal lines or table rows, never bars. Under
   deuteranopia the grey is indistinguishable from the T-FEN purple
   (checked: ΔE ≈ 0.6), so a filled grey series would be misread.
4. **Light family variants never carry the difference by colour alone.**
   FNO vs FEN (light variants) are close under deuteranopia (ΔE ≈ 9), so add
   a marker, hatch or direct label whenever both appear.
5. **Orange marks one thing.** In a figure that does not show the U-Net,
   orange may mark the single highlighted result. In a figure that does show it,
   emphasise with the blue of the locked model or a direct label instead.
6. **No colour in the prose.** Figures and tables use colour; body text stays
   ink. Table rules use `gaLine` if tables are coloured at all.
7. **Figures are sized for the page.** The text width is 135 mm (A4, jkureport
   with unequal margins). Make figures with `fig_size(frac, aspect)` and include
   them at the same fraction (`width=frac\textwidth`) so the 7–9 pt fonts are
   their nominal size. Save as PDF (vector) for plots, PNG at 300 dpi for images.
8. **Font:** Public Sans, the template's sans (`fonts/`); call
   `register_fonts()` once if matplotlib does not find it.
9. **Captions carry the legend text** when a legend would crowd the plot; use
   `\armkey{armStencil}` for an inline colour square.
10. **Masks at physical aspect ratio.** En-face panels are drawn at
    ≈ 5.94 × 5.82 mm, not 49 × 1024 pixels.

## Differences from the poster

- Poster type scale (A0, 26 pt body) is replaced by print sizes (8 pt labels,
  7 pt ticks) and Archivo/Inter by the template's Public Sans.
- The poster series (`persistence`, `mppde` sky, `mmpde` deep blue,
  `baseline` orange for Mai 2024) are kept in `POSTER_SERIES` for reuse of
  poster figures only. In the thesis, orange belongs to the U-Net and Mai
  (2024) is an ink dashed line.
- The poster figure notebook (`poster_figures.ipynb`) used an older deck
  palette (navy `#12283A`, teal `#1C6E8C`, amber `#D9772B`, green TP). Figures
  regenerated for the thesis should switch to this palette.
