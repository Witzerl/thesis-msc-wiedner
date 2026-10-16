# Prompt: Figure 2.1 (eye anatomy), drawing only

Written 2026-10-16. Paste everything below the line into the external LLM. The labels,
leader lines, panel letters and caption are added afterwards in the thesis repo; the
external model draws the graphics only and reports anchor points for the labels.

---

## Task

Write one self-contained Python script, `fig_bg_eye_anatomy.py`, that draws a two-panel
anatomical schematic of the human eye with **matplotlib** (plus numpy). It is Figure 2.1
of a master thesis on forecasting geographic atrophy (a disease of the macula) from
retinal OCT images. The readers are machine-learning people without a clinical
background, so the drawing must be clear and anatomically correct, not artistic.

**Draw the graphics only. The script must contain no text at all:** no `ax.text`, no
`annotate`, no titles, no legends, no tick labels, no panel letters. All labels and
leader lines are added later by hand. To make that possible, the script exports anchor
points for every structure (see "Anchors").

## Panel (a): horizontal cross-section of a right eye, seen from above

Orientation: the optical axis is horizontal; the **front of the eye (cornea) points to
the left**, light enters from the left. Because this is a right eye seen from above with
the front to the left, the **nasal side is the bottom of the panel and the temporal side
the top**. Work in millimetres, origin at the centre of the globe.

Structures, front to back (approximate adult values; the drawing may simplify):

| Structure | Geometry |
|---|---|
| Globe | near-spherical, axial length ~24 mm |
| Cornea | clear dome at the front, more curved than the globe (radius of curvature ~7.8 mm), diameter ~11.5 mm, ~0.55 mm thick; continuous with the sclera at the limbus |
| Anterior chamber | fluid space between cornea and iris, depth ~3 mm |
| Iris | thin diaphragm in front of the lens, with a central opening (pupil, ~3-4 mm) |
| Ciliary body | small wedge behind the root of the iris on both sides |
| Zonules | a few thin fibres from the ciliary body to the lens equator |
| Lens | biconvex, ~9.5 mm wide, ~4 mm thick, back surface more curved than the front |
| Vitreous body | clear gel filling the large cavity behind the lens |
| Retina | thin inner lining of the back wall, from just behind the ciliary body (ora serrata) to the optic disc |
| Choroid | vascular layer between retina and sclera, same extent as the retina |
| Sclera | white outer shell, ~0.5-1 mm thick, continuous with the cornea and with the sheath of the optic nerve |
| Fovea | small, shallow pit in the retina at the back of the eye, slightly temporal of the optical axis (i.e. slightly above it here); pit ~1.5 mm wide |
| Macula | the retinal region around the fovea, ~5.5 mm across along the wall; show it as a segment of retina in a slightly different tint |
| Optic disc | where the retina ends at the nerve, ~4.5 mm **nasal** of the fovea measured along the wall (i.e. below it here) |
| Optic nerve | leaves the globe backwards from the disc, ~3 mm thick, inside a sheath ~4-5 mm thick; show ~6-8 mm of it |
| Central retinal vessels | optional: a thin artery and vein running in the centre of the nerve into the disc |

Retina and choroid are ~0.25 mm thick each and would be invisible at print size; draw
them thicker (e.g. 0.5-0.7 mm) and keep the factor in a constant `LAYER_EXAGGERATION`
so the caption can say "layer thickness not to scale". Everything else stays in
proportion.

## Panel (b): fundus of a right eye, en-face, as seen by an examiner

This is a flat drawing of the back of the eye as seen through the pupil (like a fundus
photograph, but schematic, not photorealistic). Work in millimetres on the retina,
**origin at the centre of the fovea, x to the right, y up (superior)**. For a right eye
the **optic disc lies to the right of the fovea** (nasal side).

| Element | Geometry |
|---|---|
| Fundus field | a circular field of view, radius ~7.5 mm, centred so that both the optic disc and the 6 x 6 mm window below fit inside with a margin |
| Optic disc | slightly vertical oval, ~1.8 mm wide x ~1.9 mm tall, centre at about (+4.5, +0.5) mm (the fovea sits slightly below the disc centre) |
| Optic cup | paler central area of the disc, ~0.4 of the disc diameter |
| Vessels | the central artery and vein emerge from the disc and split into four main branches each (superotemporal, inferotemporal, superonasal, inferonasal). The **temporal branches arch around the macula** (the vascular arcades), passing roughly 3-4 mm above and below the fovea. Smaller branches run towards the fovea but **stop at the foveal avascular zone** (~0.5 mm diameter, vessel-free). Arteries thinner and lighter than veins (width ratio ~2:3); widths taper with each branching. Smooth curves (Bezier or splines), no jagged random walks. If any randomness is used, fix the seed. |
| Macular zones | concentric circles centred on the fovea, **diameters: foveola 0.35 mm, fovea 1.5 mm, parafovea 2.5 mm, perifovea 5.5 mm** (the outer edge of the perifovea is the edge of the macula). Thin outlines; a faint darker tint towards the centre may suggest the macular pigment. |
| OCT window | a **6 x 6 mm square centred on the fovea, dashed**, in the accent colour. It is the scan field of the OCT data used in the thesis and is the one element the reader must not miss. Note that it is only slightly larger than the 5.5 mm macula circle, so make the two easy to tell apart (square vs circle, dashed vs solid, colour). |

## Layout and size

- Use the interface below: `fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=pal.fig_size(1.0, 0.52))`.
  The figure is printed at the full text width of **135 mm**, so the whole figure is
  ~135 x 70 mm. Line widths in points must look right at that size (outlines ~0.6-0.8 pt,
  vessels 0.3-1.2 pt, the OCT window ~1.0 pt).
- `ax.set_aspect("equal")`, axes off, white background.
- **Leave empty space for labels** around each drawing: set the axis limits so that the
  drawing occupies about the central 60 % of each axes horizontally, with free gutters
  left and right (and some room above and below in panel a). Put the gutter widths in
  module-level constants so they can be adjusted.
- Vector output only: no raster images, no `imshow`, no embedded bitmaps. Flat fills with
  alpha are fine; avoid hundreds of thousands of path segments.

## Colours

Use only colours from the thesis palette below, or tints and shades of them computed in
code by blending with white or with `ink` (write a small `blend(c1, c2, t)` helper).
**No other hand-picked hex values.** Put every colour the script uses in one `COLORS`
dict at the top, built from `PAL`, so it can be changed in one place. Rules: never red
and green together; the orange `accent` is reserved for the OCT window (do not use it for
anything else); greys only for outlines and reference lines. Suggested mapping (change it
if something works clearly better, and say so): sclera white with `ink_2` outline; cornea
and lens light blue tints of `primary_tint`; vitreous a very light `bg_soft`; iris and
ciliary body `secondary`; choroid a mid tint of `jku_magenta` (blood-rich layer); retina
`primary_300`, macula segment a darker tint of `primary`; optic nerve a pale grey-blue
tint; fundus background a pale warm tint of `jku_magenta` blended strongly with white;
arteries a light tint of `jku_magenta`, veins a darker shade of it.

```python
PAL = dict(
    primary="#0082BA", primary_700="#00628C", primary_300="#6FC0DF",
    primary_tint="#E6F3F9", secondary="#0C3C52", accent="#E8852B",
    accent_tint="#FCEBD8", ink="#15242B", ink_2="#56676E", bg="#FFFFFF",
    bg_soft="#F2F7FA", line="#D5E1E8", good="#0E7C86", muted="#8AA0A9",
    jku_magenta="#C8004B",
)
```

## Interface (the script runs inside the thesis repository)

The repository provides `images/scripts/_common.py`. Use it exactly like this:

```python
from _common import setup, save
pal = setup()            # applies the thesis matplotlib style, returns the palette module
PAL = pal.PAL            # the dict above
fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=pal.fig_size(1.0, 0.52))
...
save(fig, "fig_bg_eye_anatomy")   # writes images/fig_bg_eye_anatomy.pdf
```

To test outside the repository, write yourself a stub `_common.py` with the same names:
`setup()` returning a namespace with `PAL` and `fig_size(width_frac, aspect)` =
`(135/25.4*width_frac, 135/25.4*width_frac*aspect)`, and `save(fig, name)` calling
`fig.savefig(name + ".pdf")`. Do not ship the stub.

Structure the script as `draw_eye(ax) -> dict` and `draw_fundus(ax) -> dict`, each
returning its anchors, plus `main()`.

## Anchors (required)

Each drawing function returns a dict `name -> {"xy": (x, y), "side": "left"|"right"|"top"|"bottom"}`
in that panel's data coordinates (mm). `xy` is a point **on** the structure where a leader
line should end (inside a filled region, or on a thin line); `side` is the gutter where
the label would best go without crossing other structures. The script also writes both
dicts to `fig_bg_eye_anatomy_anchors.json` next to the PDF.

- Panel (a): `cornea, anterior_chamber, iris, pupil, lens, ciliary_body, zonules,
  vitreous, retina, choroid, sclera, macula, fovea, optic_disc, optic_nerve`, plus
  `nasal` and `temporal` (a point in the gutter on each side, for orientation marks).
- Panel (b): `fovea, foveola, parafovea, perifovea, macula, foveal_avascular_zone,
  optic_disc, optic_cup, artery, vein, temporal_arcade, oct_window`, plus `nasal`,
  `temporal`, `superior`, `inferior`.

## Correctness and originality

- Draw it from the anatomy described here. **Do not trace or reproduce the shapes or the
  layout of any particular published figure** (textbook, Wikipedia, journal). For a sanity
  check of proportions only, the following openly licensed images show the same views:
  Wikimedia Commons `File:Schematic_diagram_of_the_human_eye_en.svg` (horizontal section)
  and `File:Macula.svg` (fundus with macular zones).
- Add a function `check_geometry()` that asserts the key numbers in the drawn geometry:
  fovea-to-disc distance (b) 4.5 +/- 0.3 mm; zone diameters exactly as listed; OCT window
  6.0 mm wide and centred on the fovea; no vessel segment inside the foveal avascular
  zone; panel (a) axial length 24 +/- 1 mm and the optic disc on the nasal (lower) side.
  `main()` calls it.
- The script must be deterministic, run in under ~10 s, and need nothing beyond
  matplotlib, numpy and the standard library.

## What to return

1. The complete script in one code block.
2. A short list of every simplification or exaggeration relative to real anatomy (for
   the caption), and any change you made to the suggested colour mapping and why.
3. A rendered preview (PNG) if your environment can produce one.
