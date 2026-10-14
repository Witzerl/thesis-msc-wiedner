# M2 prerequisite audit -- medical and imaging terms, Ch. 1-3 (2026-10-14)

Supervisor review 1, M2: every term defined before use, for a reader who knows PDEs but not the
medicine. Scan of `01-introduction.tex`, `02-background.tex`, `03-data.tex` (comments excluded;
abstract deferred). Line numbers refer to the sources of 2026-10-14 after commit db31abe.

Status: **OK** = defined at or before first use; **GAP** = used before its definition or never
defined. Proposed fixes are glosses at first use; author signs off row by row.

## Gaps

| # | Term | First use | Defined | Proposed fix |
|---|---|---|---|---|
| 1 | macula | 01:11 (in "macular"), 01:19 | 02:87 (§2.1.1) | Gloss at 01:19: "progressive atrophy of the macula, the central region of the retina that provides sharp vision" |
| 2 | fovea / foveal involvement | 01:20, 01:57 | 02:96 (§2.1.1) | Gloss at 01:20: "once the fovea, the centre of the macula, is involved" |
| 3 | non-neovascular / AMD stages (early, intermediate, late; dry vs wet) | 01:17, 01:44 ("intermediate AMD") | partly 02:354 ("macular neovascularisation (the wet form of AMD)"); stages never | One sentence in §1.1 after the AMD numbers, sourced to Vogl2021 (p. 1-2: "the stages of early, intermediate to late AMD (ie. macular neovascularization (MNV) or macular atrophy (MA))"; MNV = "abnormal blood vessel formation from the choriocapillaris"): AMD progresses from early and intermediate stages to two late forms, neovascular AMD with abnormal vessel growth beneath the retina, and atrophy. Drusen: Boyer2017 p. 1 ("Early stages of AMD are characterized by the presence and accumulation of drusen, extracellular deposits of cellular debris") |
| 4 | drusen | 02:781 (Related Work) | never | Covered by #3 ("drusen, deposits beneath the RPE") at first mention in §1.1; nothing else needed |
| 5 | AREDS | 01:35 | never (acronym) | "in the Age-Related Eye Disease Study (AREDS) cohort" |
| 6 | complement-pathway inhibitors, anti-C3 / anti-C5 | 01:48-49 | never | "two complement-pathway inhibitors, drugs that block part of the immune system's complement cascade at the C3 or C5 protein" (or drop "(anti-C3)/(anti-C5)") |
| 7 | intravitreal injections | 01:59 | vitreous body only at 02:76 | "injections into the eye (intravitreal)" |
| 8 | best-corrected visual acuity; sham | 01:53-54 | never | "visual acuity (the sharpness of vision with the best spectacle correction) did not differ significantly from a sham procedure (a simulated injection)" |
| 9 | OCT (what it is) | 01:34 (abbreviation only), 01:78 "OCT volumes" | 02:207 (§2.1.2) | Gloss at 01:34: "optical coherence tomography (OCT), a three-dimensional imaging technique for the retina" |
| 10 | retinal layer geometry | 01:80 | "layered tissue" 02:107 | Add pointer: "... traced (Section~\ref{sec:background:ga-oct})" or gloss "the depths of the boundaries between the retina's tissue layers" |
| 11 | (structural OCT) biomarkers | 01:63 | never | "structural OCT biomarkers (measurable image features that indicate the course of the disease)" |
| 12 | fundus | 02:48 (caption), 02:229 (text) | only in the caption (02:61) | Define in §2.1.1 text: "the fundus, the inside of the back of the eye as seen through the pupil" |
| 13 | photoreceptor(s) | 02:58 (caption), 02:94 | never | §2.1.1, at "converts the incoming light pattern": "... by the photoreceptors, the light-sensitive cells of the retina" |
| 14 | posterior pole | 02:57, 02:87 | never | "near the posterior pole, the back of the eye opposite the lens" (or drop "near the posterior pole") |
| 15 | macular atrophy | 02:780 (Related Work) | never | Vogl2021 uses macular atrophy (MA) for the atrophic late stage. With #3 in place, it reads naturally; otherwise gloss "macular atrophy, the atrophic late stage of AMD" |
| 16 | glioblastoma; multiple sclerosis | 02:~855-866 (Related Work) | never | "glioblastoma, an aggressive brain tumour" (MS is common knowledge; leave) |
| 17 | low-coherence (light) | 02:211 | never | Leave; the next sentences explain the interferometry. Optional: drop "low-coherence". |
| 18 | basal-laminar deposits | 02:383 | never | Leave (a hedged mechanism, cited) or gloss "deposits between the RPE and Bruch's membrane" |

## Defined at or before first use (no action)

AMD (01:11), GA (01:18), lesion (plain word), en-face (01:77, glossed "frontal, two-dimensional";
full definition 02:267), A-scan / B-scan / OCT volume (02:213-226), SLO (02:228), FAF and
lipofuscin (02:235), RPE and Bruch's membrane (02:116, roles at 02:333), choroid and
choriocapillaris (02:81-83), subfoveal / extrafoveal (02:103), cRORA / iRORA / CAM (02:346-360),
choroidal hypertransmission (02:376), ellipsoid zone (02:372), intraclass correlation (02:248;
statistics term, known to the reader), square-root enlargement rate (02:388; defined in §3.1),
Spectralis (03:42, a device name), Vienna Reading Center (03:69).
