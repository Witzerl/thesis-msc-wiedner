# Prompt: Figure 2.1 (eye anatomy) for an image-generating model

Written 2026-10-16. Replaces the matplotlib route (`PROMPT_fig_2_1_eye_anatomy.md`), whose
two returned scripts drew the anatomy wrong.

## How to use it

- The colours are thesis palette tokens (`style/palette.py`) or tints of them: the rose
  and plum tones are `jku_magenta` blended with white or ink, the nerve grey a blend of
  `primary_tint` and `muted`. The model will only approximate them.

- **Generate the two panels separately** (Prompt A, Prompt B). Image models get one
  object right far more often than two side by side. The panels are combined in LaTeX.
- Generate several candidates per panel and pick one; then ask for corrections in plain
  words ("move the optic nerve lower", "remove all text").
- **Labels, leader lines, the dashed 6 x 6 mm OCT window and the N/T orientation marks
  are added here afterwards** (TikZ overlay), because image models place text and exact
  sizes unreliably. The prompts therefore forbid all text and do not ask for the window.
- Ask for the largest output (at least 2048 px on the long side) and PNG.
- Before using a result, go through the checklist at the end. Image models often get the
  side of the optic nerve, the position of the lens or the fovea wrong.
- **Disclosure:** the caption must say the drawing is AI-generated (e.g. "schematic,
  generated with <model> and checked by the author"). JKU rules on AI-generated figures
  still need to be confirmed with the supervisor (NOTES.md, illustrations item, rule 5).
  Also check the image tool's terms on using its outputs in a publication.

---

## Prompt A: cross-section of the eye

> A clean, flat, scientific textbook illustration of a **horizontal cross-section through
> a human right eye, seen from above**. Medical schematic style: flat colour fills, thin
> uniform dark grey-blue outlines, no shading gradients, no photorealism, no 3D effects,
> no shadows. Pure white background, generous empty white margin around the eye on all
> sides (the eye takes up about 60 % of the width), because labels will be added later.
>
> Orientation: the front of the eye points to the **left**, the optic nerve leaves at the
> **right**. Because it is a right eye seen from above, the optic nerve attaches slightly
> **below** the centre of the back wall (nasal side), and the fovea sits at the back wall
> slightly **above** the centre line (temporal side).
>
> Show, from front (left) to back (right): the transparent **cornea** as a thin dome that
> bulges out at the front; the fluid-filled **anterior chamber** behind it; the **iris** as
> two thin dark bands in front of the lens with a gap between them (the pupil); a small
> wedge-shaped **ciliary body** behind each iris root, with a few very thin **zonular
> fibres** running to the edge of the lens; the clear biconvex **lens**, more curved at the
> back than at the front, sitting just behind the iris; the large clear **vitreous body**
> filling the rest of the globe. The wall of the globe has three thin layers, from inside
> to outside: the **retina** (light blue), the **choroid** (muted rose), and the white
> **sclera** (white with a grey-blue outline), which continues into the cornea at the
> front. Retina and choroid line the back two thirds of the globe and end behind the
> ciliary body. At the back wall, slightly above the centre line, the retina shows a small
> shallow **pit (the fovea)**, and the retina around it (the **macula**, a stretch about a
> quarter of the back wall long) is a slightly darker blue. Slightly below the centre line
> the retina stops at the **optic disc**, where the **optic nerve** (pale grey-blue, with a
> white sheath continuous with the sclera) leaves the eye towards the right; show a short
> piece of the nerve, about a third of the eye's diameter long. A thin rose and a thin
> dark-rose line (the central retinal artery and vein) may run inside the nerve into the
> disc.
>
> Proportions: the globe is nearly spherical, about 24 mm across; cornea about half the
> eye's height; lens about 9.5 mm wide and 4 mm thick; the optic nerve about 3 mm thick.
> Retina and choroid may be drawn thicker than real so they are visible.
>
> Colours (flat): retina #6FC0DF, macula #0082BA, choroid a muted rose (#E480A5), sclera
> white #FFFFFF, outlines #56676E, iris and ciliary body #0C3C52, cornea and lens very
> light blue #E6F3F9, vitreous near-white #F2F7FA, optic nerve #C6D6DD. No green, no red,
> no orange.
>
> **Absolutely no text, letters, numbers, labels, arrows, leader lines, scale bars,
> legends or watermarks anywhere in the image.**

## Prompt B: the fundus (back of the eye seen through the pupil)

> A clean, flat, scientific textbook illustration of the **fundus of a human right eye**,
> i.e. the back of the eye as an examiner sees it through the pupil, drawn as a
> schematic, not as a photograph. Flat colour fills, thin clean lines, no photographic
> texture, no glare, no vignetting. The fundus is a **circle** on a pure white background,
> with a generous empty white margin around it (labels will be added later).
>
> Layout: the **fovea** (a small darker spot) lies at the **exact centre of the circle**.
> The **optic disc** lies to the **right** of the fovea (nasal side of a right eye), at a
> distance of about 2.5 disc diameters, centre-to-centre, and slightly higher than the
> fovea. The disc is a pale, slightly vertically oval disc with a paler central cup.
>
> Around the fovea draw **four thin concentric circles**, all centred on the fovea, with
> diameters in the ratio 0.35 : 1.5 : 2.5 : 5.5 (the largest circle is about 3 disc
> diameters across; the smallest is a tiny ring at the very centre). They are thin
> grey-blue outlines, not filled; the area inside the largest circle (the macula) is a
> slightly darker, faint tint of the background.
>
> Blood vessels: a central artery (thinner, lighter rose) and vein (wider, darker
> plum-red) emerge from the optic disc and each split into four main branches going up
> and down. The branches towards the left form two broad **arcs above and below the
> macula** (the vascular arcades) that curve around the largest circle **without crossing
> it**. Thinner side branches reach in towards the fovea but **stop short of the centre**,
> leaving a small vessel-free zone at the fovea. Branches taper and fork smoothly; arteries
> and veins run side by side.
>
> Colours (flat): fundus background a very pale warm rose (#FBEDF2), macula tint slightly
> darker (#F5D1DF), optic disc pale (#F8E0E9) with a lighter cup (#FFFFFF), arteries
> #E480A5, veins #890D40, zone circles and the fundus outline #56676E. No green, no
> orange.
>
> **Absolutely no text, letters, numbers, labels, arrows, leader lines, scale bars,
> squares, legends or watermarks anywhere in the image.**

---

## Checklist before using a result (author)

Panel A
- [ ] No text or text-like scribbles anywhere.
- [ ] Front (cornea) on the left, optic nerve on the right.
- [ ] Optic nerve attaches **below** the centre line; fovea pit slightly **above** it.
- [ ] Order front to back: cornea, anterior chamber, iris, lens, vitreous. The lens is
      **behind** the iris, not in front of it.
- [ ] Wall layers inside to outside: retina, choroid, sclera; retina ends at the optic
      disc; sclera continues into the cornea and into the nerve sheath.
- [ ] Macula is a stretch of the back wall around the fovea, not a shape in the vitreous.

Panel B
- [ ] No text, no squares or boxes.
- [ ] Fovea at the centre of the circle; optic disc to the **right**, ~2.5 disc diameters
      away, slightly higher.
- [ ] Four concentric circles centred on the fovea, roughly in the ratio 0.35 : 1.5 :
      2.5 : 5.5.
- [ ] Arcades curve around the macula; no vessel reaches the foveal centre.
- [ ] Veins darker and wider than arteries.

Both
- [ ] White background, flat style, similar line weights in the two panels.
- [ ] At least 2048 px on the long side.

Afterwards (here): place both PNGs in `images/`, add the 6 x 6 mm OCT window at the
correct scale (the 5.5 mm circle gives the scale), labels, leader lines and N/T marks in
TikZ, and rewrite the caption (AI-generated schematic, layer thickness not to scale,
no Commons credits).
