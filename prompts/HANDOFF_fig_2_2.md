# Handoff: finish Figure 2.2 (`fig:bg:oct-acquisition`)

Written 2026-10-16 at the end of the session that made Figures 2.1 and 2.3. Paste the block below
into a new Claude Code session in `D:\Schule\MasterThesis\thesis`.

```
Finish Figure 2.2 of my thesis (`fig:bg:oct-acquisition`, §2.1.2 Retinal Imaging, 02-background.tex), following CLAUDE.md, NOTES.md and the memory on citation rules. Figures 2.1 and 2.3 were made the same way today; use them as the template.

## What exists
- Panel (a), DONE as a drawing: ChatGPT-generated Michelson interferometer with the eye, no text:
  `images/raw/fig_bg_oct_acquisition_raw_interferometer.png` (1672 x 941, read-only backup of
  Downloads/"OCT-Interferometer mit Auge.png"). Light source left, beam splitter (diagonal
  bottom-left to top-right) centre-left, reference mirror above, eye right (front facing left,
  beam ends at the fovea, optic nerve below the centre line = nasal, consistent with Fig. 2.1),
  detector below; both arrows into the detector point down; empty space right of the detector
  for a small A-scan plot. Physics checked: a "/" splitter sends the incoming beam up to the
  mirror and on to the eye, and both returns down to the detector.
- Panel (b), DECIDED to be built in code (image models failed twice on its 3D geometry):
  prototype `images/scripts/fig_bg_oct_acquisition_block_draft.py` (writes to argv[1]). Cabinet
  projection of a retina block; front face textured with the flat ends of the Fig. 2.3 healthy
  strip (`images/raw/fig_bg_retinal_anatomy_raw_healthy.png`, rows 108-658), right face the same
  texture sheared and clipped to its parallelogram; top face pale with 10 scan lines parallel to
  the front edge and a lesion blob; front face outlined in blue = the B-scan; orange vertical
  line with an entry dot on the top front edge = the A-scan. Remaining polish: faint mirror seam
  in the middle of the front face, texture slightly overlapping the outline at the top right.
- Prompts and the history of the attempts: `prompts/PROMPT_fig_2_2_oct_acquisition_imagegen.md`.

## To do
1. One script `images/scripts/fig_bg_oct_acquisition.py` (replace the draft) that uses
   `_common.setup()/save()` and the palette, like `fig_bg_eye_anatomy.py` and
   `fig_bg_retinal_anatomy.py` (copy their `label()` helper: leader starts at the label edge
   midpoint via relpos; anchors measured on raw pixels by colour scans and documented in the
   docstring; figure printed at 135 mm text width -- canvas ~131.5 mm because the tight bbox
   adds the label overhang; check the PDF width with PyMuPDF).
   - Panel (a): the raw drawing plus labels: light source, beam splitter, reference mirror
     (reference arm), sample arm / eye, detector. Add a small inset plot in the empty area right
     of the detector: a schematic A-scan, reflectivity against depth (depth on the vertical axis,
     increasing downwards, like an OCT column), a few peaks; no numbers on the axes; it is
     schematic, not data.
   - Panel (b): the finished block plus labels: A-scan (orange line), B-scan (front face), volume
     (block), en-face (top face), lateral and axial directions (small arrows), lesion seen
     en face; optionally "≈ 6 × 6 mm" for the footprint of the MUW scans (§2.1.2 says the
     footprint is approximately 6 × 6 mm).
   - Layout: (a) and (b) side by side or stacked, whatever reads better at 135 mm; panel letters.
2. 02-background.tex: replace the placeholder figure and the old four-panel TODO comment. The text
   of §2.1.2 refers to Figure 2.2(a) for sample and reference arm (fine), and to (b) for the
   B-scan and (c) for the volume -- rewrite those references for the two panels. The old caption
   promised a projection of the volume in panel (d): drop it, the thesis computes no projection
   (the MUW data arrive as en-face maps, see "From OCT volumes to en-face maps").
3. Caption: say "schematic"; describe (a) and (b); AI note in the form used for Figs. 2.1 and 2.3
   ("generated with an image-generation model (ChatGPT, OpenAI) and checked by the author; labels
   added by the author" -- for (b) say it was drawn by the author with the layer drawing of
   Fig. 2.3 as texture); cite Huang1991 for the interferometer (local PDF and knowledge-base note
   `literature/OCT_Acquisition_Principle.md`: Michelson interferometer, sample arm, reference
   mirror, longitudinal scans plus lateral translation give a 2D section, pp. 2-3). Do not cite
   anything for spectral-domain detection (no source yet); keep the detector generic. Keep the
   existing `% TODO` on the JKU declaration of AI figures.
4. Float `[tp]` if `[t]` pushes it far from §2.1.2 (Fig. 2.3 needed that). Compile with
   `latexmk -xelatex -interaction=nonstopmode -outdir=<scratch dir> main-thesis.tex` (VS Code
   autobuild races the default outdir), render the page with PyMuPDF and look at it.
5. NOTES.md: close the Fig. 2.2 items, log what was done; commit to master (no Co-Authored-By).

## Rules that bite here
- Scripted LaTeX edits: never write "\r..." through a Python/bash string (turns into a carriage
  return, e.g. \ref -> CR + "ef"); splice from a file or use the Edit tool, then check for CR.
- Every number or claim in the figure or caption needs a source (citation-rules memory).
- Do not map retinal layers onto the ten layer channels.
- Raw images in images/raw/ are backups: never modify them.
```
