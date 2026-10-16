# Prompt: Figure 2.3 (retinal layers and the OCT signs of GA) for ChatGPT image generation

Written 2026-10-16, same route as Figure 2.1: ChatGPT draws, no text in the image; labels,
leader lines and the three GA signs are added in `images/scripts/` afterwards.

## How to use it

- Best in the **same ChatGPT conversation** as Figure 2.1, so the style matches; otherwise
  attach the final eye cross-section as a style reference.
- Generate **Panel A first**. When it passes the checklist, send Prompt B **with Panel A
  attached**, so the layer colours and thicknesses are identical in both panels.
- Ask for PNG, white background, at least 2400 px wide.

## Anatomy behind the prompts (do not paste)

- Layer order, inner to outer: internal limiting membrane, nerve fibre layer, ganglion cell
  layer, inner plexiform layer, inner nuclear layer, outer plexiform layer, outer nuclear
  layer, external limiting membrane, pigment epithelium, Bruch's membrane, capillary choroid,
  choroid (Abràmoff et al. 2010, IEEE Rev Biomed Eng 3:169, author manuscript p. 2-3,
  `pdfs/Methods/Abramoff2010.txt`). Photoreceptor inner and outer segments with the
  ellipsoid zone and interdigitation zone lie between the external limiting membrane and
  the pigment epithelium (Sadda et al. 2018, p. 8 and Fig. 2 legend).
- GA (cRORA): hypertransmission and RPE loss of at least 250 µm, with overlying photoreceptor
  degeneration, i.e. loss of the interdigitation zone, ellipsoid zone and external limiting
  membrane and thinning of the outer nuclear layer (Sadda et al. 2018, p. 8). In the
  incomplete stage the INL and OPL subside and the ELM descends in curved lines
  (Sadda et al. 2018, Fig. 2 legend B). Thickened RPE-Bruch's complex in a rim just outside
  the lesion (Chu et al. 2022; thesis §2.1.3, signature iii). The choriocapillaris is lost
  with the RPE (thesis §2.1.3, Boopathiraj 2024, Boyer 2017).
- Thicknesses in the prompt are only relative, for a readable schematic; none is quoted in
  the thesis.

---

## Prompt A: healthy retina around the fovea

> A clean, flat, scientific textbook illustration in the same style as the eye illustrations
> before: flat colour fills, thin uniform dark grey-blue outlines, no shading gradients, no
> photorealism, no 3D, no shadows, pure white background.
>
> Draw a **cross-section through the layers of a healthy human retina around the fovea**, as a
> wide horizontal strip (about three times as wide as tall, canvas at least 2400 px wide).
> The layers run horizontally across the whole width, stacked from top to bottom. In the
> middle of the strip the inner layers dip down into a smooth, shallow pit (the **foveal
> pit**): there the upper layers become thinner and thinner and disappear at the very centre,
> while the deep layers continue unbroken underneath. Leave generous empty white space above
> and below the strip and on both sides, because labels will be added later.
>
> The layers, from top to bottom, each as one clearly separated band with its own flat colour:
>
> 1. Above the retina: the vitreous, a very pale near-white blue area.
> 2. A very thin dark line on the top surface of the retina (inner limiting membrane).
> 3. A thin light-blue band (nerve fibre layer); it vanishes at the pit.
> 4. A medium band in a slightly darker blue with small round cell bodies (ganglion cell
>    layer); it thins towards the pit and vanishes at its centre.
> 5. A medium, finely textured pale band (inner plexiform layer); vanishes at the pit centre.
> 6. A medium band of small round cell bodies in a mid blue (inner nuclear layer); vanishes
>    at the pit centre.
> 7. A thin finely textured pale band (outer plexiform layer); vanishes at the pit centre.
> 8. A **thick** band of small densely packed round cell bodies in a light blue-grey (outer
>    nuclear layer), the thickest layer of all; it becomes even thicker directly under the pit.
> 9. A very thin dark line (external limiting membrane).
> 10. A band of short, upright, rod-like photoreceptor inner segments, pale.
> 11. A thin bright line across the photoreceptors (ellipsoid zone).
> 12. A band of upright photoreceptor outer segments, slightly darker.
> 13. A band of cuboidal pigmented cells in warm brown (retinal pigment epithelium).
> 14. A very thin line directly beneath it (Bruch's membrane).
> 15. A thin band of tiny round capillaries in rose (choriocapillaris).
> 16. A thicker band of larger round and oval blood vessels in rose and plum (choroid).
> 17. At the bottom, white fibrous tissue (sclera).
>
> Bands 9 to 17 run straight and unbroken across the whole width, including under the pit.
> Every band must be clearly distinguishable from its neighbours by colour or texture.
> Colours from this palette: blues #6FC0DF, #0082BA, #E6F3F9, #0C3C52; rose #E480A5;
> plum #890D40; warm brown for the pigment epithelium; outlines #56676E. No green, no orange.
>
> **Absolutely no text, letters, numbers, labels, arrows, leader lines, scale bars, legends or
> watermarks anywhere in the image.**

## Prompt B: the same retina with a geographic atrophy lesion (attach Panel A)

> Using exactly the same style, colours, layer order and layer thicknesses as the attached
> illustration, draw the **same retinal layer strip, but with a patch of geographic atrophy
> in the middle** instead of the foveal pit. Same canvas size, same white margins, no pit.
>
> Outside the lesion, on the left and on the right, all layers look exactly as in the attached
> healthy image.
>
> Inside the lesion (the middle third of the strip):
> 1. The **retinal pigment epithelium is completely missing**; Bruch's membrane is still
>    present. Draw Bruch's membrane across the whole width as a **clearly visible thin dark
>    line** directly under the brown pigment layer (in the attached image it is only a faint
>    light seam), so that it is easy to see that it continues under the lesion.
> 2. The **photoreceptors are gone**: the outer segments, the bright ellipsoid-zone line, the
>    inner segments and the external limiting membrane all end at the lesion edges and are
>    absent in between.
> 3. The **outer nuclear layer is reduced to a very thin remnant**, so the layers above it
>    (outer plexiform and inner nuclear layer) **sink down** towards Bruch's membrane, forming a
>    shallow trough. The inner layers (nerve fibre, ganglion cell, inner plexiform) stay intact
>    but follow the trough.
> 4. The **choriocapillaris is missing** under the lesion.
> 5. **Below the lesion, the choroid is clearly brighter** than elsewhere: a vertical column of
>    light, as wide as the lesion, shines from the lesion down through the choroid, as if light
>    now passes through where the pigment layer used to absorb it.
>
> At both lesion edges:
> 6. The external limiting membrane and the ellipsoid-zone line curve down smoothly towards
>    Bruch's membrane where they end.
> 7. Just outside each edge, over a short stretch, the pigment epithelium band is **noticeably
>    thicker** than further away.
>
> **Absolutely no text, letters, numbers, labels, arrows, leader lines, scale bars, legends or
> watermarks anywhere in the image.**

---

## Checklist (author, before using a result)

Panel A
- [ ] No text or text-like marks.
- [ ] Count the bands top to bottom: thin top line, then 5 inner bands, thick nuclear band,
      thin line, inner segments, bright line, outer segments, brown pigment band, thin line,
      capillary band, vessel band, white sclera.
- [ ] The outer nuclear layer is the thickest band.
- [ ] At the pit only the inner bands thin out and vanish; everything from the external
      limiting membrane down runs straight underneath.

Panel B
- [ ] Same colours and thicknesses as A.
- [ ] Inside the lesion: brown pigment band absent, Bruch's line present; photoreceptor bands
      and both thin lines (ELM, EZ) absent; capillary band absent.
- [ ] Upper layers sag into a trough over the lesion; inner bands intact.
- [ ] A bright column through the choroid exactly below the lesion.
- [ ] Brown pigment band thicker just outside both lesion edges.

Afterwards (here): raw files into `images/raw/`, labels and leader lines from measured anchors
(layer names in panel A; the three signs (i)-(iii) of §2.1.3 in panel B), caption rewritten
with AI-generation note and citations (Abramoff2010, Sadda2018, Chu2022).

---

## Prompt B, standalone for a new chat (2026-10-16)

Written after five rounds in one chat kept the same error inside the lesion: a band of
densely packed cells (outer nuclear layer) stays several rows thick, with an extra pale band
and a separate single row of cells underneath it. Only one version had the lesion right
(`Schematische Netzhaut mit zentraler Atrophie (2).png`), but it lost the capillary circles
outside the lesion. Attach two images to the new chat, in this order:
1. `Schematische Querschnittsdarstellung der Fovea.png` (healthy panel A),
2. `Schematische Netzhaut mit zentraler Atrophie (2).png` (lesion reference).

Text to paste:

```
I am making a figure for a master thesis in medical image analysis. It has two panels drawn as flat, clean scientific textbook illustrations (flat colour fills, thin dark grey-blue outlines, no shading, no photorealism, white background). Panel A, the healthy retina, is finished: it is the FIRST attached image. I now need Panel B: the same retina with a lesion of geographic atrophy, a disease in which the pigment epithelium, the photoreceptors and the capillary layer below them die in a patch.

The SECOND attached image is an earlier attempt at Panel B. Its lesion (the middle part) is anatomically correct and should be reproduced exactly, but its healthy parts left and right are wrong (the small capillary circles under the brown layer are missing). Please produce Panel B as follows:

- Canvas, size, proportions, colours, line style and the position and height of every band: exactly as in the FIRST image.
- Left and right thirds (healthy): identical to the FIRST image, including the thin band of small round capillaries directly under the brown pigment cells.
- Middle third (lesion): as in the SECOND image.

For clarity, these are the bands from top to bottom:

Healthy part (as in the first image): thin dark top line; light-blue plain band; band with scattered round cells; pale finely textured band; band with round cells; pale finely textured band; THICK band of densely packed round cells; thin dark double line; band of pale upright rods; thin bright white line; band of darker blue upright rods; brown pigment cells; thin dark line (Bruch's membrane, please make it clearly visible); thin band of small round capillaries; thick pink band with large vessels; white fibrous tissue at the bottom.

Centre of the lesion, from top to bottom (and nothing else):
1. thin dark top line, light-blue plain band, band with scattered round cells, pale band - all intact, but sunk into a shallow trough;
2. band with round cells (sunk);
3. pale finely textured band (sunk);
4. ONE single row of small round cells - this is all that is left of the thick band of densely packed cells;
5. the thin dark Bruch's membrane line, directly under that single row, continuous with the line under the healthy parts;
6. no capillary circles at all;
7. the pink vessel band, clearly brighter and washed out, like a column of light shining down from the lesion;
8. the white fibrous tissue at the bottom.
Important: inside the lesion there must NOT be a band of several rows of densely packed cells, and there must NOT be any pale band or gap between the single row of cells and Bruch's membrane. The pale rods, the bright white line, the darker blue rods, the dark double line and the brown pigment cells are completely absent inside the lesion.

At the two lesion edges: the thick band of densely packed cells tapers down smoothly into the single row; the rods, the white line and the double line curve down towards Bruch's membrane and end; the brown pigment cells are heaped up a little thicker just outside the edge and stop at the edge.

Absolutely no text, letters, numbers, labels, arrows, leader lines, scale bars or watermarks anywhere in the image.
```

If the new chat still fails: use `Schematische Netzhaut mit zentraler Atrophie (2).png` as Panel B
(lesion correct, capillary circles missing outside; label the plain band as choriocapillaris).
