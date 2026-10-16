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
