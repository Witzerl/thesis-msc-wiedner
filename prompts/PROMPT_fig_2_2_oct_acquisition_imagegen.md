# Prompt: Figure 2.2 (OCT acquisition) for ChatGPT image generation

Written 2026-10-16, same route as Figures 2.1 and 2.3: ChatGPT draws, no text in the image;
labels, axis names and the A-scan profile curve are added in `images/scripts/` afterwards.

## Plan (changed from the old four-panel TODO in the .tex)

Two drawn panels instead of four:
- **(a) How one depth profile is measured:** a Michelson interferometer -- light source, beam
  splitter, reference mirror (reference arm), the eye (sample arm), detector. The A-scan itself
  (reflectivity against depth) is added here as a small plot drawn in code, so it is exact.
- **(b) The scan geometry in one picture:** a 3D block of retina with one vertical line (A-scan),
  one vertical slice (B-scan), the whole block (volume) and its top face (en-face). This replaces
  the old panels (b)-(d) and shows how the four terms relate.
The old panel (d) "projection of the volume" goes: the MUW data arrive as en-face maps, no
projection is computed in the thesis (§2.1.2). Real en-face maps of a cohort eye are planned for
§3.1 (`fig:data:example-state`), so they are not repeated here.

Sources behind the drawing (do not paste): Michelson interferometer with sample arm and
reference mirror, longitudinal scans plus lateral translation give a 2D section (Huang et al.
1991, pp. 2-3; `literature/OCT_Acquisition_Principle.md`). A-scan, B-scan, volume and en-face are
the terms of §2.1.2. The detector is drawn generically (no spectrometer details), because the
text's spectral-domain sentence has no source yet.

## How to use it

- New ChatGPT chat. Attach as style reference the healthy layer strip of Figure 2.3
  (`Schematische Querschnittsdarstellung der Fovea.png`) and the eye cross-section of Figure 2.1
  (`eye_cross_section_left_panel.png`).
- One prompt per panel; ask for PNG, white background, at least 2048 px wide.

---

## Prompt A: the measuring principle (attach both style images)

```
I am making a figure for a master thesis in medical image analysis. Please draw it in exactly the same style as the two attached illustrations: flat colour fills, thin uniform dark grey-blue outlines, no shading gradients, no photorealism, no 3D effects, no shadows, pure white background, same colours.

Draw a simple schematic of how optical coherence tomography (OCT) measures one depth profile of the retina, as a clean optical diagram seen from above, on a wide canvas (about 16:9, at least 2048 px wide). Leave generous empty white space around everything, because labels will be added later.

Components, connected by thin straight light beams drawn as narrow pale-red lines with small arrowheads showing the direction of the light:
1. On the left, a small rectangular box: the light source. Its beam goes to the right.
2. In the middle, a small glass cube with a diagonal line through it: the beam splitter. It splits the beam in two:
   - one beam continues straight to the right, into an eye;
   - one beam goes straight up to a flat mirror (the reference mirror), drawn as a short thick bar with hatching on its back side.
3. On the right, the eye: a horizontal cross-section of an eye seen from above, front of the eye facing left towards the beam splitter, in the same style as the attached eye illustration but simplified (cornea, lens, the eye wall with its thin blue and rose layers at the back). The beam enters through the cornea and the lens and ends on the retina at the back of the eye.
4. Both reflected beams travel back to the beam splitter, are combined there, and a combined beam goes straight down to a small rectangular box at the bottom: the detector.
Draw the outgoing and returning beams as two thin parallel lines with opposite arrowheads where they share a path, so the direction is clear.

Leave an empty white area to the right of the detector box (about the size of the detector box, three times as wide) where a small graph will be added later.

Absolutely no text, letters, numbers, labels, symbols, scale bars, legends or watermarks anywhere in the image.
```

## Prompt B: the scan geometry (attach the layer strip of Figure 2.3)

```
Same style as before (flat colour fills, thin dark grey-blue outlines, no shading gradients, no photorealism, pure white background). Draw a schematic 3D block of retinal tissue that explains how an OCT scan is built up, on a canvas of about 4:3, at least 2048 px wide, with generous empty white space around it for labels.

1. The block: a flat rectangular block (cuboid) seen from the front-left and slightly above (simple isometric view), much wider and deeper than tall, like a thick slice of tissue. Its front face and left face show the retinal layers as horizontal bands, with exactly the same colours and order as the attached layer strip (blue bands with cells on top, the rows of photoreceptor rods, the brown pigment layer, the rose band with blood vessels, white at the bottom). Keep the layers flat (no pit).
2. The top face of the block is a pale blue-grey surface. On it, draw a faint darker irregular patch (a lesion seen from above) somewhere near the middle, and a set of about ten thin, evenly spaced parallel lines running from left to right across the whole top face (the scan lines).
3. One A-scan: a single thin vertical probe beam, drawn as a bright orange line, coming down from above the block, entering the top face at one point and running straight down through all layers to the bottom of the block. Make it clearly stand out.
4. One B-scan: a single vertical slice through the block along one of the scan lines (the one the orange beam lies in), drawn as a semi-transparent pale blue plane with a slightly darker outline, so that the layers are visible through it. The orange beam lies inside this plane.
5. Small arrows are not needed; do not draw axes.

Absolutely no text, letters, numbers, labels, symbols, scale bars, legends or watermarks anywhere in the image.
```

---

## Checklist (author, before using a result)

Panel A
- [ ] No text or symbols.
- [ ] Light source -> beam splitter; splitter sends one beam to the mirror and one into the eye.
- [ ] The eye beam passes cornea and lens and ends on the retina at the back.
- [ ] Both reflections return to the splitter; one combined beam goes to the detector.
- [ ] Empty space next to the detector for the A-scan plot.

Panel B
- [ ] No text, no axes.
- [ ] Layer order on the front face as in Figure 2.3 (blue bands on top, photoreceptor rods, brown
      pigment layer, rose vessel band, white at the bottom).
- [ ] Orange beam vertical from the top face through all layers.
- [ ] The vertical slice lies along one scan line and contains the orange beam.
- [ ] Top face shows the scan lines and a darker patch.

Afterwards (here): raws to `images/raw/`, labels (light source, beam splitter, reference mirror,
eye / sample arm, detector; A-scan, B-scan, volume, en-face, lateral and axial directions, ~6 mm
footprint), the A-scan profile plotted in code, caption and text rewritten for two panels (the
text now refers to panels (a)-(c)), AI note and the Huang1991 citation.

---

## Standalone prompts for a new chat (2026-10-16, second attempt)

First attempt (one image with both panels): detector arrow pointed up, and the B-scan slice ran
front-to-back while the scan lines ran left-to-right. The new prompts ask for two separate
images and put the B-scan slice parallel to the front face, which is easier to draw correctly.
Attach in the new chat: `Schematische Querschnittsdarstellung der Fovea.png` and
`eye_cross_section_left_panel.png` (style references). Send Prompt A, then Prompt B.

### Prompt A (new chat)

```
I am making a figure for a master thesis in medical image analysis. The two attached images are finished figures of the same thesis; please draw in exactly their style: flat colour fills, thin uniform dark grey-blue outlines, no shading gradients, no photorealism, no 3D effects, no shadows, pure white background, the same blues, rose and brown.

Draw a simple optical diagram of how optical coherence tomography (OCT) measures one depth profile of the retina. Seen from above, wide canvas (16:9, at least 2400 px wide), generous empty white margins all around because labels will be added later.

Layout (a plus-shaped arrangement around a beam splitter in the middle-left of the canvas):
1. Left: a small rectangular box, the light source.
2. Centre-left: a small transparent glass cube with one diagonal line from its bottom-left to its top-right corner, the beam splitter.
3. Above the cube: a flat mirror, drawn as a short thick horizontal bar with short hatching lines on its top side (the back of the mirror).
4. Right of the cube: an eye, drawn as a horizontal cross-section seen from above, like the attached eye but simpler: front of the eye (cornea, then lens) facing left towards the cube, the optic nerve leaving at the back slightly below the middle, the eye wall with thin blue and rose layers.
5. Below the cube: a small rectangular box, the detector.

Light beams: thin pale-red straight lines with small arrowheads.
- Source to cube: arrowhead pointing right.
- Cube to mirror: one line going up (arrowhead up) and next to it one line coming back down (arrowhead down).
- Cube to eye: one line going right (arrowhead right) through the cornea and lens to the retina at the back of the eye, and next to it one line coming back left (arrowhead left).
- Cube to detector: one or two lines going DOWN only, every arrowhead on this stretch points down into the detector. Nothing comes out of the detector.
- Do not draw any line returning from the cube to the light source.

Leave an empty white rectangle to the right of the detector, about three times as wide as the detector box, where a small graph will be added later.

Absolutely no text, letters, numbers, labels, symbols, scale bars, legends or watermarks anywhere in the image.
```

### Prompt B (same new chat)

```
Same style as before. Now draw a separate image (4:3, at least 2400 px wide, generous white margins all around for labels): a schematic 3D block of retinal tissue that explains how an OCT scan is built up.

1. The block: a flat rectangular block (cuboid), wider than deep and much wider than tall, seen from the front and slightly from above and from the right (simple isometric view), so that the FRONT face, the TOP face and the RIGHT face are visible.
2. The front face and the right face show the retinal layers as horizontal bands, in the same colours and order as the attached layer strip: blue bands with round cells at the top, then rows of upright photoreceptor rods, then the brown pigment layer, then a rose band with blood vessels, then white at the bottom. Flat layers, no pit.
3. The top face is a pale blue-grey surface. On it: about ten thin, evenly spaced parallel lines running from LEFT to RIGHT, i.e. parallel to the front edge of the block (the scan lines), and a faint darker irregular patch near the middle (a lesion seen from above).
4. The B-scan: one vertical slice through the whole height of the block, PARALLEL TO THE FRONT FACE, positioned about one third of the way from the front to the back. Its top edge lies exactly on one of the scan lines. Draw it as a semi-transparent pale blue plane with a slightly darker outline, so the layers behind it remain visible.
5. The A-scan: one bright orange vertical line, coming down from above the block, entering the top face at a point on that same scan line, and running straight down inside the slice all the way to the bottom face of the block.
6. No axes, no arrows.

Absolutely no text, letters, numbers, labels, symbols, scale bars, legends or watermarks anywhere in the image.
```

---

## Prompt for redrawing panel (b) from a geometry reference (2026-10-16, third attempt)

The code-drawn block had a blurry texture, thick outlines and leaders hidden under the faces, and the
A-scan line crossing the top face read as wrong. New route: ChatGPT redraws an exact geometry
reference at high quality. Attach, in this order:
1. `images/_preview/fig_bg_oct_block_reference.png` (from `images/scripts/fig_bg_oct_block_reference.py`)
2. `Schematische Querschnittsdarstellung der Fovea.png` (the healthy layer strip of Fig. 2.3)

```
I am making a figure for a master thesis in medical image analysis. The FIRST attached image is an exact geometry sketch drawn by me; the SECOND attached image is a finished illustration of the retinal layers from the same thesis. Please redraw the FIRST image as a clean, high-quality scientific illustration in the style of the SECOND image (flat colour fills, fine detail, thin uniform dark grey-blue outlines, no shading gradients, no photorealism, white background).

Keep the geometry of the FIRST image exactly: the same block, the same viewing angle and tilt, the same proportions, the same position of every element. Output at least 2400 px wide, same aspect ratio as the first image.

1. The block: replace the flat colour bands on the front face and on the right face by the detailed layers of the SECOND image, in exactly the same order and colours from top to bottom: blue bands with round cells, pale textured bands, the thick band of densely packed cells, the thin dark line, the pale photoreceptor rods, the thin bright white line, the darker blue rods, the brown pigment cells, the band of small capillaries, the rose band with large blood vessels, white at the bottom. Use only the flat outer parts of the second image: the layers are completely flat, with NO pit or dip anywhere. On the right face the layers run diagonally exactly as in the sketch and meet the front-face layers at the same heights at the front-right edge.
2. The top face: pale blue-grey, with the same thin parallel lines running from left to right (parallel to the front edge) and the same darker irregular patch.
3. The slice inside the block: a thin, semi-transparent pale blue glass plane, parallel to the front face, exactly where it is in the sketch. Its top edge lies on the top face as a slightly thicker solid blue line (one of the parallel lines); its other edges are inside the block and drawn as thin dashed blue lines, so the slice looks like it is seen through the block.
4. The orange line: exactly as in the sketch, a solid orange arrow coming from above and pointing down onto the top face, ending in a small orange dot on the slice's top edge, continued inside the block as a dashed orange line straight down inside the slice to its bottom edge.
5. All outlines thin (similar to the sketch), nothing thick or heavy.

Absolutely no text, letters, numbers, labels, symbols, scale bars, legends or watermarks anywhere in the image.
```

**Not used (2026-10-16):** the author pointed out that a slice inside a textured block cannot be
read; panel (b) became the sequence A-scan -> B-scan -> volume -> en-face view, drawn in code from
the Fig. 2.3 strip (`images/scripts/fig_bg_oct_acquisition.py`). The reference script was removed.
