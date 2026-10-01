# Micro feedback 2a: Ch. 2 Background, §2.1 GA and OCT imaging

[← Overview](00-overview.md)

38 findings: 2 high, 23 medium, 13 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

Section 2.1 follows a sensible order (anatomy, disease, imaging, en-face maps, state channels, cohort), and its problems are local, not structural. There are two roadmaps, one in the section introduction and one at the end of §2.1.1. The retina is defined three times (l. 77, 112 and 181). §2.1.2 uses OCT vocabulary (B-scan, column-summed signal, summed-voxel en-face projection) that §2.1.3 and §2.1.4 only introduce later, and the body text uses 'A-scan' (l. 326) without having defined it. l. 240 says that the first two OCT signatures define the channel-0 mask, which contradicts §3.1 ('The GA mask was not segmented on the OCT'). l. 359 ('No cross-modality fusion is required') sits uneasily with the same paragraph of §3.1. The en-face representation is presented as a motivated choice (l. 350, l. 381), although l. 375 states that the data arrive as en-face maps. The Fig. 2.3 caption and the pointer at l. 335 also still describe a projection step that §2.1.4 says is not performed. §2.1.6 repeats §3.1 and §3.3 almost figure for figure. The register is more tutorial than in later chapters: the camera and fingerprint metaphors, 'takes some getting used to', 'a small piece of optical engineering', and signposts such as 'Concretely', 'In other words' and 'Put differently'. The GPTZero-flagged tone comes mostly from em-dash asides between subject and verb, semicolon lists and aphoristic paragraph closers, not from buzzwords.

### Transitions

- §2.1 intro (l. 11-24) and the last paragraph of §2.1.1 (l. 131-138) both give a roadmap. Put the subsection list into the section introduction in place of the clause 'and the subsequent subsections build the imaging substrate on top of that vocabulary', and delete l. 131-138 (see the finding at l. 11). The roadmap's description of §2.1.4 ('the projection from 3D OCT volume to the 2D en-face grid') should also match what §2.1.4 says: no projection is computed.
- §2.1.2 uses 'B-scan', 'column-summed signal' and 'summed-voxel en-face projections' (l. 221-231) before §2.1.3/§2.1.4 define them. The least invasive fix is a one-line forward gloss at the start of §2.1.2, e.g. 'A B-scan is one cross-sectional OCT image of the retina; its acquisition is described in~\S\ref{sec:background:ga-oct:oct}.' Swapping §2.1.2 and §2.1.3 would also work, but it is a structural change for the author to decide.
- §2.1.1 -> §2.1.2: the first sentence of §2.1.2 (l. 181) repeats the definition of the retina from l. 77-79 and l. 112-114. Start §2.1.2 directly with the figure pointer and the definition of GA (finding at l. 181).
- Channel-0 provenance: l. 240 ('The first two signatures define the lesion mask used as channel~0') states that the mask comes from OCT, which contradicts §3.1 (03-data.tex l. 50, 'The GA mask was not segmented on the OCT'). l. 359 ('No cross-modality fusion is required') reads oddly against the same paragraph. §2.1.5 (l. 410) already uses neutral wording; align the two earlier sentences with it without bringing the FAF provenance into the Background, which the author has decided against.
- §2.1.3 -> §2.1.4: l. 335-339 says §2.1.4 explains how the varying native grids are reduced to the modelling grid. §2.1.4 instead says that no projection is computed, and the crop/pad reduction is in §3.3. Redirect the pointer (finding at l. 335). The Fig. 2.3 caption (l. 280-283 and (d) at l. 296) has the same problem.
- l. 350 ('The thesis therefore works on the OCT en-face grid') and l. 381 ('The choice of en-face rather than B-scan ... is motivated by') present the en-face representation as a decision derived from the literature, although l. 375 says the data arrive as en-face maps. Present the literature as supporting the representation (finding at l. 381). l. 364-365 has the same issue in miniature: 'therefore' gives model tractability as the reason the clinical literature uses en-face images (finding at l. 364).
- The Chu2022 rim-thickening result appears twice: as signature (iii) at l. 233-239 and again at l. 428-430 with its r value. In §2.1.5, refer back to 'the RPE--Bruch's-membrane thickening of signature~(iii)' instead of introducing it again (finding at l. 428).
- §2.1.6 (l. 451-484) repeats §3.1 (grid shapes) and §3.3 (crop/pad, spacing, the 27.3 / 6.0 / 25.7 / 31.1 % census). Keep the literature precedent for the 6 mm window and short pointers to §3.1/§3.3 here, so that the numbers are read once, in Chapter 3 (finding at l. 453).
- The Fig. 2.1 caption (l. 54-70) and the body text (l. 74-103) say much the same thing. The caption lists three macular sub-zones and the text four; make the zone lists identical (finding at l. 64).
- The Fig. 2.2 caption (l. 169) maps the named strata onto the ten channels, while §2.1.5 (l. 422) deliberately says only that the boundaries are 'ordered from the most superficial to the deepest'. The reader meets the stronger mapping first and the weaker statement later (finding at l. 169; the issue is also recorded in NOTES.md, figure plan).
- Optional: §2.1 ends on the patient-level split (l. 486-496), a Chapter 3 detail, just before §2.2 turns to PDE solvers. Moving the split paragraph before the window paragraph (l. 470-484) would end the section on the fixed modelling window and the pointer to §3.3, which is closer to the grid that §2.2.1 picks up. Note that the ~21:1 anisotropy sentence is in the first paragraph of §2.1.6, so this swap does not end the section on it.

### Recurring tells in this part

- Em-dash asides that put a definition or restatement between subject and verb: 20 '---' in the rendered range (captions included), about 10 asides. Example: 'Behind the retina, two further layers --- the \emph{choroid} (...) and the \emph{sclera} (...) --- support and supply ...' (l. 82). Also at l. 122, 184, 220, 233, 317 (two in one sentence) and 488. Move the gloss after the main clause or into its own sentence.
- Gloss signposts that announce a restatement: 'Concretely' (l. 308, 417), 'In other words' (l. 191), 'Put differently' (l. 205), 'essentially' (l. 210, 234), sometimes doubled with 'i.e.'. About 6 occurrences. Delete the signpost and say the thing once.
- Metaphors and conversational idioms: 'can be thought of as a biological camera' (l. 75), 'the visual fingerprints' (l. 221), 'takes some getting used to' (l. 122), 'a small piece of optical engineering' (l. 314), 'blue-light FAF struggles' (l. 345), 'biomarkers ... live throughout' (l. 427). About 6, against the author's no-informal-analogy rule. The ultrasound comparison (l. 306) is a standard technical analogy; only its em-dash twist needs smoothing.
- Semicolon-joined pairs and lists, often balanced: 'The first two signatures define ...; the third is ...' (l. 240), 'The layer channels are therefore not auxiliary context; they carry ...' (l. 440), and three-clause semicolon lists at l. 131, 353 and 428. 26 semicolons in the range. Split the lists where each clause has its own citation (l. 428); leave single-citation enumerations (l. 353) alone.
- Antithesis closers ('rather than', 'not X; Y', 'not only'): l. 112, 194, 243, 381, 427, 440, 495. About 7. Several end a paragraph by restating it as a contrast (l. 243, l. 440).
- Paragraph-opening announcements and meta-commentary: 'This section provides the imaging-side background needed to motivate ...' (l. 11), 'The remaining subsections build on this vocabulary.' (l. 131), 'This subsection describes \emph{what} ... and \emph{why} ...' (l. 396). 3 occurrences.
- Pseudo-cleft or heavy-subject constructions: '... is what feeds the model' (l. 127), 'What this end-stage lesion looks like on OCT has been formalised by ...' (l. 197), 'how the varying native voxel grids are reduced ... is the subject of' (l. 337). 3 occurrences.
- Emphatic fillers: 'ever' (l. 93), 'precisely' (l. 207), 'deliberately' (l. 20), 'actually' (l. 133), 'in fact' (l. 384), 'By construction' (l. 388), 'methodologically important' (l. 382). About 7.
- The same definition or phrase repeated across subsections: the retina is defined at l. 77, 112 and 181; the Chu2022 rim result appears at l. 233 and 428; 'operational details' appears at l. 398 and 490.

## Findings

### 2a.1 [medium] §2.1 Geographic Atrophy and OCT Imaging (introduction)

`02-background.tex:11` · GPTZero: AI · flow, clarity, ai-tone

> This section provides the imaging-side background needed to motivate the state representation used throughout the remainder of the thesis. The clinical framing established in Chapter~\ref{ch:introduction} is taken as read; the focus here is on \emph{which part of the eye} GA affects, on \emph{how} that part is imaged, on \emph{what is visible} in an OCT volume of a GA eye, and on \emph{which derived quantities} feed into the eleven-channel state tensor introduced in~\S\ref{sec:data:state}. Because the rest of this thesis is written for a primarily machine-learning audience, the present section is deliberately self-contained and aims to remain accessible to readers without prior clinical training:~\S\ref{sec:background:ga-oct:anatomy} introduces the small set of anatomical terms that recur throughout the work, and the subsequent subsections build the imaging substrate on top of that vocabulary.

**Issue.** A 120-word meta paragraph built on four mirrored emphasised clauses ('on which ..., on how ..., on what ..., on which ...') with filler ('deliberately self-contained', 'imaging substrate'). A second roadmap follows at l. 131-138, where 'actually' is conversational and the description of §2.1.4 ('the projection from 3D OCT volume to the 2D en-face grid') does not match §2.1.4, which says no projection is computed.

**Suggestion.**

> This section gives the imaging background for the state representation used in the rest of the thesis and builds on the clinical context of Chapter~\ref{ch:introduction}. It describes which part of the eye GA affects, how that part is imaged, what is visible in an OCT volume of a GA eye, and which derived quantities enter the eleven-channel state tensor of~\S\ref{sec:data:state}. Because the thesis is written mainly for a machine-learning audience, no clinical training is assumed. \S\ref{sec:background:ga-oct:anatomy} introduces the anatomical terms that recur throughout the work, \S\ref{sec:background:ga-oct:disease} describes how GA appears on OCT, \S\ref{sec:background:ga-oct:oct} explains what an OCT volume is and how it is acquired, \S\ref{sec:background:ga-oct:enface} describes en-face images and the en-face maps the models receive, \S\ref{sec:background:ga-oct:state-rep} defines the eleven channels of the state tensor, and \S\ref{sec:background:ga-oct:muw} describes the MUW longitudinal cohort. [Then delete the roadmap paragraph at l. 131-138.]

### 2a.2 [medium] Figure 2.1 caption

`02-background.tex:64` · GPTZero: AI · clarity, flow

> The fovea sits roughly at the centre of the macula; the macula itself is sub-divided into the foveola (innermost), parafovea, and perifovea, in concentric rings of increasing radius.

**Issue.** The caption names three sub-zones, while the body text (l. 96-100) names four (foveola, fovea, parafovea, perifovea). Most of the rest of the caption repeats the body text.

**Suggestion.**

> The fovea sits roughly at the centre of the macula, which is sub-divided into concentric zones of increasing radius: the foveola, fovea, parafovea and perifovea.

### 2a.3 [medium] §2.1.1 A short anatomy primer

`02-background.tex:74` · GPTZero: human · tone

> The eye, sketched in Figure~\ref{fig:bg:eye-anatomy} (left), can be thought of as a biological camera.

**Issue.** An informal analogy that the paragraph never uses again; the author's style rules exclude informal analogies.

**Suggestion.**

> Figure~\ref{fig:bg:eye-anatomy} (left) shows the eye in cross-section.

### 2a.4 [medium] §2.1.1 A short anatomy primer

`02-background.tex:82` · GPTZero: AI · clarity, ai-tone

> Behind the retina, two further layers --- the \emph{choroid} (a richly vascularised tissue, of which the \emph{choriocapillaris} is the innermost capillary bed) and the \emph{sclera} (the white, mechanically rigid outer shell) --- support and supply the retina from beneath.

**Issue.** A 35-word em-dash aside, containing two nested parentheticals, separates subject and verb.

**Suggestion.**

> Behind the retina lie two further layers that support and supply it from beneath: the \emph{choroid}, a richly vascularised tissue whose innermost capillary bed is the \emph{choriocapillaris}, and the \emph{sclera}, the white, mechanically rigid outer shell.

### 2a.5 [low] §2.1.1 A short anatomy primer

`02-background.tex:91` · GPTZero: AI · tone, clarity

> The macula has a diameter of roughly five to six millimetres and is the only part of the retina that GA ever affects clinically; for that reason, the OCT scanning window used throughout the thesis is centred on the macula and covers a $6 \times 6$\,mm field (\S\ref{sec:background:ga-oct:muw}).

**Issue.** Emphatic 'ever', and a long semicolon join of a fact and its consequence.

**Suggestion.**

> The macula has a diameter of roughly five to six millimetres and is the only part of the retina that GA affects clinically. The OCT scanning window used throughout the thesis is therefore centred on the macula and covers a $6 \times 6$\,mm field (\S\ref{sec:background:ga-oct:muw}).

### 2a.6 [low] §2.1.1 A short anatomy primer

`02-background.tex:112` · GPTZero: AI · ai-tone, tone

> A second piece of anatomy is internal rather than positional: the retina is itself a \emph{layered} tissue, with several distinct strata stacked vertically from the front (closest to the vitreous body) to the back (closest to the choroid).

**Issue.** A colon reveal introduced by an 'X rather than Y' contrast, with the slightly writerly 'piece of anatomy'.

**Suggestion.**

> The retina is also a \emph{layered} tissue, with several distinct strata stacked vertically from the front (closest to the vitreous body) to the back (closest to the choroid).

### 2a.7 [**HIGH**] §2.1.1 A short anatomy primer

`02-background.tex:122` · GPTZero: AI · tone, clarity, ai-tone

> The terminology in this list takes some getting used to, but for the purposes of this thesis it is sufficient to remember the structural fact that the retina is layered, that GA destroys a specific \emph{outer}-retinal stack of three of those layers (\S\ref{sec:background:ga-oct:disease}), and that the surrounding layer geometry --- ten boundary depth maps in total --- is what feeds the model alongside the lesion mask (\S\ref{sec:background:ga-oct:state-rep}).

**Issue.** 'Takes some getting used to' is a conversational idiom, and 'is what feeds' is a pseudo-cleft. 'Three of those layers' does not match the list just given, because the choriocapillaris (l. 187) is not in it.

**Suggestion.**

> For the purposes of this thesis, it suffices to note that the retina is layered, that GA destroys a specific \emph{outer}-retinal stack of three layers (\S\ref{sec:background:ga-oct:disease}), and that the surrounding layer geometry, given as ten boundary depth maps, is passed to the model together with the lesion mask (\S\ref{sec:background:ga-oct:state-rep}).

### 2a.8 [medium] Figure 2.2 caption

`02-background.tex:169` · GPTZero: AI · clarity, flow

> The same set of anatomical strata corresponds to the ten layer-boundary channels of the eleven-channel state tensor introduced in \S\ref{sec:background:ga-oct:state-rep}.

**Issue.** The caption maps the named strata onto the ten channels, while §2.1.5 (l. 422) deliberately says only that the boundaries are ordered from superficial to deep. The roughly eight named strata also do not visibly add up to ten boundaries.

**Suggestion.**

> Author to decide; a wording consistent with §2.1.5 would be: 'The ten layer-boundary channels of the state tensor (\S\ref{sec:background:ga-oct:state-rep}) record the depths of boundaries between strata of this kind, ordered from superficial to deep.'

### 2a.9 [medium] §2.1.2 Geographic Atrophy on OCT

`02-background.tex:181` · GPTZero: AI · flow

> The retina is a thin, layered tissue at the back of the eye that converts incoming light into neural signals; Figure~\ref{fig:bg:retinal-anatomy} (left) sketches its principal anatomical strata in the macula.

**Issue.** This is the third definition of the retina in the section; it repeats l. 77-79 and l. 112-114, which appear a page earlier.

**Suggestion.**

> Figure~\ref{fig:bg:retinal-anatomy} (left) sketches the principal anatomical strata of the retina in the macula.

### 2a.10 [medium] §2.1.2 Geographic Atrophy on OCT

`02-background.tex:184` · GPTZero: AI · clarity, ai-tone

> Geographic atrophy is the disease in which a stack of three tightly coupled \emph{outer}-retinal layers --- the retinal pigment epithelium (RPE), the photoreceptor outer segments that sit just above the RPE, and the choriocapillaris (a dense capillary bed) immediately below the RPE --- die together in a localised patch of the macula \citep{Boopathiraj2024,Boyer2017}.

**Issue.** A 40-word em-dash list separates subject and verb, 'RPE' is repeated three times inside it, and 'a stack ... die' is awkward in number.

**Suggestion.**

> Geographic atrophy is the disease in which three tightly coupled \emph{outer}-retinal layers die together in a localised patch of the macula: the retinal pigment epithelium (RPE), the photoreceptor outer segments just above it, and the choriocapillaris, a dense capillary bed immediately below it \citep{Boopathiraj2024,Boyer2017}.

### 2a.11 [low] §2.1.2 Geographic Atrophy on OCT

`02-background.tex:191` · GPTZero: AI · ai-tone, clarity

> In other words, atrophy of one layer entrains the degeneration of the others, so the resulting lesion appears on imaging as a sharply delineated patch in which the entire outer-retinal complex is missing rather than as the loss of a single isolated layer.

**Issue.** 'In other words' announces a restatement, but the sentence states a consequence of the preceding one.

**Suggestion.**

> Atrophy of one layer therefore entrains the degeneration of the others, and the resulting lesion appears on imaging as a sharply delineated patch in which the entire outer-retinal complex is missing rather than as the loss of a single isolated layer.

### 2a.12 [low] §2.1.2 Geographic Atrophy on OCT

`02-background.tex:197` · GPTZero: human · clarity

> What this end-stage lesion looks like on OCT has been formalised by an international consensus group, the Classification of Atrophy Meetings (CAM), under the term \emph{complete RPE and outer retinal atrophy} (cRORA) \citep{Sadda2018, Vallino2024}.

**Issue.** A pseudo-cleft opening with a long clausal subject delays the agent.

**Suggestion.**

> An international consensus group, the Classification of Atrophy Meetings (CAM), has formalised the OCT appearance of this end-stage lesion under the term \emph{complete RPE and outer retinal atrophy} (cRORA) \citep{Sadda2018, Vallino2024}.

### 2a.13 [medium] §2.1.2 Geographic Atrophy on OCT

`02-background.tex:205` · GPTZero: human · tone

> Put differently, cRORA is the OCT-readable definition of an established atrophic lesion, which can arise with or without macular neovascularisation (the wet form of AMD), and \emph{GA is precisely the subset of cRORA that arises in eyes without macular neovascularisation}.

**Issue.** 'Put differently' announces a restatement, but the sentence adds new information. 'Precisely' is an intensifier on the author's exclusion list.

**Suggestion.**

> cRORA is thus the OCT-readable definition of an established atrophic lesion, which can arise with or without macular neovascularisation (the wet form of AMD), and \emph{GA is the subset of cRORA that arises in eyes without macular neovascularisation}.

### 2a.14 [medium] §2.1.2 Geographic Atrophy on OCT

`02-background.tex:208` · GPTZero: AI · clarity, ai-tone

> The CAM framework also recognises a precursor stage, \emph{iRORA} (incomplete RPE and outer retinal atrophy), which is essentially the same lesion at a smaller spatial scale, i.e.\ the same OCT pattern below the 250\,\textmu{}m size threshold; in one retrospective study of intermediate-AMD eyes, 93\,\% of iRORA lesions progressed to cRORA within twenty-four months, with a median conversion time of fourteen months \citep{Vallino2024}.

**Issue.** A 70-word sentence with a double gloss ('essentially ... i.e.'), and a semicolon that joins a definition to a separate study result.

**Suggestion.**

> The CAM framework also recognises a precursor stage, \emph{iRORA} (incomplete RPE and outer retinal atrophy), which shows the same OCT pattern below the 250\,\textmu{}m size threshold. In one retrospective study of intermediate-AMD eyes, 93\,\% of iRORA lesions progressed to cRORA within twenty-four months, with a median conversion time of fourteen months \citep{Vallino2024}.

### 2a.15 [medium] §2.1.2 Geographic Atrophy on OCT

`02-background.tex:220` · GPTZero: AI · tone, ai-tone

> The principal direct OCT signatures of an established GA lesion --- the visual fingerprints by which the disease is identified on a B-scan --- are the following \citep{Boopathiraj2024,Yehoshua2011,Vallino2024}.

**Issue.** A metaphor ('visual fingerprints') inside an em-dash aside restates 'signatures', followed by an 'are the following' reveal.

**Suggestion.**

> An established GA lesion is identified on a B-scan by three principal direct OCT signatures \citep{Boopathiraj2024,Yehoshua2011,Vallino2024}.

### 2a.16 [medium] §2.1.2 Geographic Atrophy on OCT

`02-background.tex:233` · GPTZero: human · clarity, tone

> \emph{(iii)} \emph{RPE--Bruch's-membrane (BM) thickening} is concentrated immediately around the lesion margin --- essentially, the narrow ring of tissue just outside the lesion is measurably thicker than tissue further from the lesion --- and is thought to reflect, at least in part, basal-laminar deposits accumulated in the diseased tissue; the thickness of this rim correlates significantly with the eye's subsequent annual square-root lesion enlargement rate \citep{Chu2022}.

**Issue.** A ~70-word sentence whose em-dash aside ('essentially, ...') restates the main clause in lay terms, which is overly explanatory.

**Suggestion.**

> \emph{(iii)} \emph{RPE--Bruch's-membrane (BM) thickening} is concentrated in a narrow rim just outside the lesion margin and is thought to reflect, at least in part, basal-laminar deposits accumulated in the diseased tissue; the thickness of this rim correlates significantly with the eye's subsequent annual square-root lesion enlargement rate \citep{Chu2022}.

### 2a.17 [**HIGH**] §2.1.2 Geographic Atrophy on OCT

`02-background.tex:240` · GPTZero: AI · flow, ai-tone

> The first two signatures define the lesion mask used as channel~0 of the state tensor; the third is a boundary-localised predictive biomarker that motivates encoding the surrounding layer geometry rather than the mask alone.

**Issue.** The sentence says the channel-0 mask is defined by these OCT signatures, but §3.1 (03-data.tex l. 50) states 'The GA mask was not segmented on the OCT', so a reader meets a contradiction. It is also a symmetric 'first two ...; the third ...' pair that closes on 'rather than'.

**Suggestion.**

> Author to check against §3.1. A wording that does not state the provenance: 'The first two signatures delineate the lesion itself. The third is a predictive biomarker located at the lesion boundary and motivates encoding the surrounding layer geometry in addition to the lesion mask.'

### 2a.18 [medium] Figure 2.3 caption

`02-background.tex:296` · GPTZero: AI · clarity

> \emph{(d)} Projecting the volume along its axial direction onto the fundus plane yields the two-dimensional en-face image on which the modelling pipeline operates (\S\ref{sec:background:ga-oct:enface}); a GA lesion appears inside the en-face image as a region with a different signal intensity than the surrounding healthy retina.

**Issue.** The caption says the pipeline operates on a projected intensity image. §2.1.4 (l. 375-379) states that no projection is computed and that the models receive a mask and depth maps on the en-face grid.

**Suggestion.**

> \emph{(d)} Projecting the volume along its axial direction onto the fundus plane yields a two-dimensional en-face image, in which a GA lesion appears as a region with a different signal intensity than the surrounding healthy retina. The modelling pipeline operates on en-face maps on this grid (\S\ref{sec:background:ga-oct:enface}).

### 2a.19 [low] §2.1.3 Optical Coherence Tomography of the Macula

`02-background.tex:305` · GPTZero: AI · tone, ai-tone

> Optical Coherence Tomography (OCT), introduced by \citet{Huang1991}, produces micrometre-resolution cross-sectional images of the retina, in much the same way that ultrasound produces them for soft tissue --- except that low-coherence near-infrared light replaces sound.

**Issue.** A conversational comparison ('in much the same way') that ends in an em-dash 'except that' twist.

**Suggestion.**

> Optical Coherence Tomography (OCT), introduced by \citet{Huang1991}, produces micrometre-resolution cross-sectional images of the retina. The principle is analogous to ultrasound imaging of soft tissue, with low-coherence near-infrared light in place of sound.

### 2a.20 [medium] §2.1.3 Optical Coherence Tomography of the Macula

`02-background.tex:308` · GPTZero: AI · clarity, tone

> Concretely, the system shines a weak probe beam into the eye and measures how strongly each \emph{depth} along the path of the beam reflects light back. That depth-versus-reflectivity profile is then displayed as a single column of pixels in the output image, with intensity encoding reflectivity and the vertical position of each pixel encoding depth.

**Issue.** The body text never names this profile an A-scan, yet l. 326 ('recovers the A-scan') and l. 328 ('A single A-scan is ...') use the term as if it had been defined. 'Concretely' and 'shines' are conversational.

**Suggestion.**

> A weak probe beam is directed into the eye, and the strength of the light reflected back from each \emph{depth} along its path is measured. This depth-versus-reflectivity profile is called an \emph{A-scan}; it is displayed as a single column of pixels, with intensity encoding reflectivity and vertical position encoding depth.

### 2a.21 [low] §2.1.3 Optical Coherence Tomography of the Macula

`02-background.tex:313` · GPTZero: human · tone

> Resolving the depth dimension requires a small piece of optical engineering, because near-infrared light from a single short pulse cannot be timed precisely enough on a per-layer basis with conventional electronics.

**Issue.** 'A small piece of optical engineering' is a conversational understatement.

**Suggestion.**

> Resolving the depth dimension requires an optical technique, because conventional electronics cannot time near-infrared light from a single short pulse precisely enough to separate individual layers.

### 2a.22 [medium] §2.1.3 Optical Coherence Tomography of the Macula

`02-background.tex:317` · GPTZero: AI · clarity, ai-tone

> The standard solution is interferometric: the source light is split into two beams (Figure~\ref{fig:bg:oct-acquisition}(a)), one of which --- the \emph{sample arm} --- is sent into the eye and reflected back from the various retinal layers, while the other --- the \emph{reference arm} --- is sent to a known mirror and reflected back unchanged.

**Issue.** A colon reveal followed by two mirrored em-dash asides ('one of which --- ... --- while the other --- ... ---') in a single sentence.

**Suggestion.**

> The standard solution is interferometry. The source light is split into two beams (Figure~\ref{fig:bg:oct-acquisition}(a)): the \emph{sample arm} is sent into the eye and reflected back from the various retinal layers, and the \emph{reference arm} is sent to a known mirror and reflected back unchanged.

### 2a.23 [medium] §2.1.3 Optical Coherence Tomography of the Macula

`02-background.tex:335` · GPTZero: AI · flow, clarity

> The MUW cohort uses an acquisition protocol that produces volumes with a physical footprint of approximately $6 \times 6$\,mm laterally; how the varying native voxel grids are reduced to the standard two-dimensional modelling grid used in the rest of the thesis is the subject of~\S\ref{sec:background:ga-oct:enface}.

**Issue.** The forward pointer says §2.1.4 explains how the native grids are reduced to the modelling grid, but §2.1.4 says no projection is computed and the crop/pad reduction is in §3.3. The heavy subject ('how ... is the subject of') also delays the point.

**Suggestion.**

> The MUW cohort uses an acquisition protocol that produces volumes with a lateral footprint of approximately $6 \times 6$\,mm. How such a volume is summarised as a two-dimensional en-face image is described in~\S\ref{sec:background:ga-oct:enface}, and how the varying native grids are brought to one modelling grid in~\S\ref{sec:data:spatial}.

### 2a.24 [low] §2.1.3 Optical Coherence Tomography of the Macula

`02-background.tex:345` · GPTZero: AI · tone

> and it remains reliable near the fovea, where blue-light FAF struggles.

**Issue.** 'Struggles' personifies the modality and is colloquial.

**Suggestion.**

> and it remains reliable near the fovea, where blue-light FAF is less reliable.

### 2a.25 [medium] §2.1.3 Optical Coherence Tomography of the Macula

`02-background.tex:359` · GPTZero: AI · flow, ai-tone

> No cross-modality fusion is required.

**Issue.** An aphoristic four-word closer that repeats the paragraph's opening sentence (l. 352) and introduces an undefined notion ('fusion'). It also reads oddly against §3.1, where the mask is an FAF outline registered to the OCT grid.

**Suggestion.**

> Delete the sentence; the opening sentence of the paragraph ('A single OCT volume shows both the lesion and the retinal layers around it.') already makes the point.

### 2a.26 [low] §2.1.4 From OCT volumes to en-face projections

`02-background.tex:364` · GPTZero: AI · flow, clarity *(added in verification)*

> The full OCT volume of a GA eye is too large and too redundant to be modelled at native voxel resolution. The clinical literature therefore works with an \emph{en-face} image instead: a two-dimensional map of the retina seen from the front, as in a fundus photograph, in which every pixel corresponds to one A-scan of the volume and summarises what lies along it \citep{Pilotto2015,Chu2022,Yehoshua2011,Vallino2024}.

**Issue.** 'Therefore' presents model tractability as the reason the clinical literature uses en-face images. The cited clinical studies do not model progression, so the causal link reads as an unsupported inference.

**Suggestion.**

> The full OCT volume of a GA eye is too large and too redundant to be modelled at native voxel resolution. The clinical literature works with an \emph{en-face} image instead: a two-dimensional map of the retina seen from the front, as in a fundus photograph, in which every pixel corresponds to one A-scan of the volume and summarises what lies along it \citep{Pilotto2015,Chu2022,Yehoshua2011,Vallino2024}.

### 2a.27 [medium] §2.1.4 From OCT volumes to en-face projections

`02-background.tex:381` · GPTZero: AI · flow, tone

> The choice of en-face rather than B-scan as the modelling substrate is motivated by a methodologically important caveat documented by \citet{Vallino2024}: a lesion classified as iRORA on a single horizontal B-scan can in fact be part of a larger cRORA lesion that is only fully visible in the en-face slab.

**Issue.** The preceding paragraph says the data arrive as en-face maps and no projection is computed, so calling this a motivated 'choice' reads oddly. 'Methodologically important', 'in fact' and 'substrate' are filler or jargon.

**Suggestion.**

> Working on en-face maps rather than on single B-scans is also supported by a caveat documented by \citet{Vallino2024}: a lesion classified as iRORA on a single horizontal B-scan can be part of a larger cRORA lesion that is fully visible only in the en-face slab.

### 2a.28 [low] §2.1.4 From OCT volumes to en-face projections

`02-background.tex:388` · GPTZero: AI · ai-tone, clarity

> By construction, the 2D en-face grid also reduces a per-step three-dimensional forward problem to a per-step two-dimensional one, which matters for the tractability of the models introduced in the subsequent chapters.

**Issue.** 'By construction' is a stock opener, and 'per-step ... per-step' is repetitive.

**Suggestion.**

> The en-face grid also reduces the forward problem of each step from three dimensions to two, which matters for the tractability of the models in the following chapters.

### 2a.29 [low] §2.1.5 The eleven-channel state representation

`02-background.tex:396` · GPTZero: AI · ai-tone, tone

> This subsection describes \emph{what} the eleven channels of the state tensor are, in structural terms, and \emph{why} retaining all of them is clinically motivated. The operational details of how the channels were produced in the MUW cohort are deferred to~\S\ref{sec:data:dataset} and are not relied upon in the rest of this chapter.

**Issue.** A paragraph-opening announcement built on an emphasised what/why pair. 'Operational details' recurs at l. 490.

**Suggestion.**

> The eleven channels of the state tensor are described here in structural terms, together with the clinical reason for retaining all of them. How the channels were produced in the MUW cohort is stated in~\S\ref{sec:data:dataset}; the rest of this chapter does not rely on it.

### 2a.30 [medium] §2.1.5 The eleven-channel state representation

`02-background.tex:414` · GPTZero: AI · clarity, ai-tone

> The remaining ten channels are \emph{retinal layer boundary depth maps}: at every pixel of the en-face grid, the value of channel $c \in \{1, \dots, 10\}$ is the axial position of one anatomical layer boundary in the underlying OCT B-scan. Concretely, fixing a pixel of the en-face grid selects a single A-scan in the OCT volume, and channel $c$ at that pixel records how deep along that A-scan the $c$-th anatomical layer-boundary surface lies.

**Issue.** The same definition is given twice, first via 'the underlying OCT B-scan' and then, after 'Concretely', via the A-scan. The change of reference object is confusing.

**Suggestion.**

> The remaining ten channels are \emph{retinal layer boundary depth maps}. Each pixel of the en-face grid corresponds to one A-scan of the OCT volume, and the value of channel $c \in \{1, \dots, 10\}$ at that pixel is the depth along this A-scan at which the $c$-th anatomical layer boundary lies.

### 2a.31 [low] §2.1.5 The eleven-channel state representation

`02-background.tex:425` · GPTZero: AI · ai-tone, clarity

> The clinical motivation for retaining all ten layer-boundary channels alongside the binary mask is that documented prognostic biomarkers for GA progression live throughout the full vertical retinal column, not only inside the lesion itself.

**Issue.** A heavy 'The motivation for X is that Y' frame and the personification 'biomarkers ... live'.

**Suggestion.**

> All ten layer-boundary channels are retained alongside the binary mask because documented prognostic biomarkers for GA progression are found throughout the full vertical retinal column, not only inside the lesion itself.

### 2a.32 [medium] §2.1.5 The eleven-channel state representation

`02-background.tex:428` · GPTZero: AI · clarity, flow

> RPE--Bruch's-membrane thickening at the 0--300\,\textmu{}m rim around the GA boundary correlates with annual square-root enlargement rate at $r = 0.595$ \citep{Chu2022}; outer retinal layer thinning, in particular of the outer nuclear layer and of the RPE-photoreceptor complex, accelerates in the months preceding macular-atrophy conversion \citep{Vogl2021}; and the thickness of the inner nuclear layer in the retina immediately adjacent to a GA lesion correlates with the yearly progression rate at Spearman $r = 0.48$ \citep{Ebneter2016}.

**Issue.** An ~80-word semicolon list covering three separate studies. The first clause reintroduces signature (iii) from l. 233 as if it were new.

**Suggestion.**

> At the 0--300\,\textmu{}m rim around the GA boundary, the RPE--Bruch's-membrane thickening of signature~(iii) correlates with the annual square-root enlargement rate at $r = 0.595$ \citep{Chu2022}. Outer retinal layer thinning, in particular of the outer nuclear layer and of the RPE-photoreceptor complex, accelerates in the months preceding macular-atrophy conversion \citep{Vogl2021}. The thickness of the inner nuclear layer in the retina immediately adjacent to a GA lesion correlates with the yearly progression rate at Spearman $r = 0.48$ \citep{Ebneter2016}.

### 2a.33 [medium] §2.1.5 The eleven-channel state representation

`02-background.tex:440` · GPTZero: AI · ai-tone, tone

> The layer channels are therefore not auxiliary context; they carry rate-of-change information that the mask alone cannot provide.

**Issue.** An aphoristic 'not X; Y' paragraph closer that restates the paragraph as a contrast.

**Suggestion.**

> The layer channels therefore carry rate-of-change information that the mask alone cannot provide.

### 2a.34 [low] §2.1.6 The MUW longitudinal GA cohort

`02-background.tex:451` · GPTZero: AI · clarity

> The cohort comprises 553 volume scans over 75 eyes, acquired with a Heidelberg Engineering device, which in the MUW study of \citet{Mai2024} was a Spectralis spectral-domain OCT.

**Issue.** The relative clause 'which in the MUW study of ... was' reads as if Mai et al. identified the device used for this cohort. §3.1 (03-data.tex l. 26) says Mai et al. describe 'a larger GA cohort from the same MUW clinic'.

**Suggestion.**

> The cohort comprises 553 volume scans over 75 eyes, acquired with a Heidelberg Engineering device; for a larger GA cohort of the same clinic, \citet{Mai2024} report a Spectralis spectral-domain OCT.

### 2a.35 [medium] §2.1.6 The MUW longitudinal GA cohort

`02-background.tex:453` · GPTZero: AI · flow

> Lateral pixel counts vary per eye across the 553 visits, ranging from 38 to 66 B-scans by 961 to 1719 A-scans, giving 67 distinct native shapes in total.

**Issue.** From here to l. 484, §2.1.6 repeats §3.1 (grid shapes, 03-data.tex l. 65-66) and §3.3 (spacing, crop/pad and the censoring census, l. 193-219) almost figure for figure, so the reader meets the same numbers twice within about fifteen pages.

**Suggestion.**

> Keep only the literature precedent for the 6 mm window and a short pointer in §2.1.6, e.g. 'The native grids differ between eyes and are brought to one $49 \times 1024$ modelling grid by centre-crop or zero-pad (\S\ref{sec:data:spatial}); the pixel spacing, its roughly 21:1 in-plane anisotropy and the censoring of lesion growth at the window edge are described there.' The numbers then appear once, in Chapter~\ref{ch:data}.

### 2a.36 [medium] §2.1.6 The MUW longitudinal GA cohort

`02-background.tex:458` · GPTZero: AI · clarity

> Pixel spacing is treated as constant across the cohort at approximately $[0.12118,\, 0.003867,\, 0.00568]$\,mm in the $(x, z, y)$ directions, because the scans were resampled upstream to one gold-standard spacing. The resulting fixed physical window is approximately $5.94 \times 5.82$\,mm. This is an assumption whose limits are stated in~\S\ref{sec:discussion:limitations}.

**Issue.** 'This is an assumption' follows the window sentence, so 'This' appears to refer to the window, not to the constant spacing.

**Suggestion.**

> Pixel spacing is treated as constant across the cohort at approximately $[0.12118,\, 0.003867,\, 0.00568]$\,mm in the $(x, z, y)$ directions, because the scans were resampled upstream to one gold-standard spacing; the limits of this assumption are stated in~\S\ref{sec:discussion:limitations}. The resulting fixed physical window is approximately $5.94 \times 5.82$\,mm.

### 2a.37 [medium] §2.1.6 The MUW longitudinal GA cohort

`02-background.tex:476` · GPTZero: AI · clarity

> However, measured on the present cohort, this window is not lossless.

**Issue.** 'This window' points back to the literature's $6 \times 6$ mm acquisition window. What actually cuts lesion area is this thesis's fixed modelling window, obtained by crop or pad.

**Suggestion.**

> However, measured on the present cohort, the fixed $5.94 \times 5.82$\,mm modelling window of this thesis is not lossless.

### 2a.38 [low] §2.1.6 The MUW longitudinal GA cohort

`02-background.tex:488` · GPTZero: AI · clarity, ai-tone

> Patient-level covariates --- in particular age and biological sex --- accompany the imaging sequence; the operational details of how they are extracted and encoded are described in~\S\ref{sec:data:covariates}.

**Issue.** An unnecessary em-dash aside, and 'the operational details of how ...' (also at l. 398) is wordy.

**Suggestion.**

> Patient-level covariates, in particular age and biological sex, accompany the imaging sequence; their extraction and encoding are described in~\S\ref{sec:data:covariates}.

