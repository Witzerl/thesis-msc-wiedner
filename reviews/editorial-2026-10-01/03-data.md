# Micro feedback 3: Ch. 3 Data and Preprocessing

[← Overview](00-overview.md)

36 findings: 1 high, 15 medium, 20 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

Chapter 3 has a sound section order: cohort, state tensor, common grid, normalisation, covariates, transition windows, splits. The prose is mostly plain and procedural and close to the author's unflagged voice, so most GPTZero-flagged sentences need no change. The structural weaknesses are local. (i) Like every other chapter of the thesis (Chapters 1, 2, 4, 5 and 6 also open directly with a section), Chapter 3 has no opening paragraph. Adding one is a decision for the whole thesis, not a defect of this chapter. (ii) §3.1 moves between cohort size, acquisition device, demographics, file inventory, mask provenance, grid geometry and lesion statistics with little signposting, and it ends on a one-sentence figure paragraph that is unrelated to the growth statistics before it. (iii) Some terms are used before they are defined in this chapter: 'window' in the temporal sense in §3.5, which also clashes with the spatial crop 'window' of §3.3; 'canonical fold'; 'change-region metrics' and 'one-year anchor'. ('Modelling grid' is already defined in §2.1.6.) (iv) Facts are repeated: the padded zeros entering the statistics appear in both §3.3 and §3.4, and the optional pad-loss masking appears twice in §3.3. (v) In §3.7 the fold-heterogeneity paragraph is separated from the fold table by the test-split paragraph. The register is consistent and objective. Where the tone reads machine-like, the cause is structure, not vocabulary: colon reveals, 'therefore' conclusions, announced enumerations ('for two reasons', 'Two consequences follow', 'Three properties'), X-not-Y closers, two uses of 'on purpose', and storage-level details ('split files', 'eye suffix', 'keyed per eye') that read like an engineering log.

### Transitions

- Chapter opening (l.4-8): the chapter goes straight from \chapter to \section{Dataset}. No chapter of the thesis has an opening paragraph (Chapters 1, 2, 4, 5 and 6 also start with a section), so an opener here is optional and should be decided for all chapters together. If one is wanted, keep it to one short roadmap sentence.
- §3.1 paragraph order: the demographics paragraph (l.31-35) is separated from the cohort-size paragraph (l.11-21) by the acquisition/device paragraph (l.23-27). Moving l.31-35 directly after l.21 gives the sequence cohort -> acquisition -> files -> mask provenance -> grid sizes -> lesion statistics.
- §3.1 end: the one-sentence paragraph 'Figure~\ref{fig:data:example-state} shows one visit ...' (l.98) follows the growth statistics, which it has nothing to do with. Panel (a) shows the SLO frame and panels (b)-(c) two channels on the modelling grid, so the sentence fits after the mask-provenance paragraph (after l.60) or at the end of the first paragraph of §3.2. See the finding at l.98.
- §3.2 last paragraph (l.166-175): it opens with what is not done (thickness) before stating why all ten channels are kept, so the reader has to work out the link. Give the reason first, then thickness as the derived quantity that is not used.
- §3.3 first two paragraphs: the literature pointer on 6 x 6 mm windows (l.189-191) closes the paragraph on how the grid is reached, but the window size only appears in the next paragraph. Attach the pointer to the 5.938 x 5.816 mm sentence (l.193-195).
- §3.3 padding paragraph (l.202-213): the argument goes raw meaning of zero -> normalised value -> loss -> raw meaning again (the sentinel sentence). Move 'Zero also cannot serve as a sentinel ...' (l.211-213) up to follow the raw-unit sentence ending at l.204.
- §3.3 / §3.4 overlap: 'the padded zeros enter the per-channel mean and standard deviation' is stated in §3.3 (l.205-207) and again in §3.4 (l.247-250), each time with a cross-reference to the other section. The optional pad-loss masking is mentioned at l.209-211 and again at l.234-235. State each fact once and point to it.
- §3.5 before §3.6: §3.5 uses 'window', 'window-start ages' and 'rollout' (l.272-291) before §3.6 defines transition windows (l.301), and §3.3 has just used 'window' for the spatial crop. The lightest fix is a parenthetical definition at l.272. Alternatives are to reserve 'crop' for the spatial sense in §3.3 or to swap §3.5 and §3.6, but the swap is a restructure and the author's decision.
- §3.6 (l.312-358): the table is introduced in a one-sentence paragraph (l.312-313). 'Three properties' are announced, the first is never tied to the pipeline, 'Third' opens a new paragraph, and a further effect follows as 'The same schedule also shapes the evaluation'. Merge l.312-313 into the 'Three properties' paragraph, link the first property to the curriculum budget, and open the evaluation paragraph with 'Beyond training, ...'.
- §3.7 (l.364-411): 'The folds also differ in baseline lesion size' (l.408) refers back to the per-fold eye counts (l.373-375), but the test-split paragraph comes between them. Move it to directly after l.375.
- 'canonical fold' (l.261, l.286) is defined as fold 2 only in Chapter 5 (05-experiments.tex l.101). Define it at its first use in §3.4.

### Recurring tells in this part

- Mid-sentence 'therefore' conclusions, 7 times (l.72, 196, 222, 232, 341, 402, and l.172 'The layer geometry is therefore kept in full rather than reduced to the lesion mask alone.'). Keep the ones that carry a real inference. Cut the ones that only restate the sentence before (l.172, l.402).
- Colon reveals, about 8-10 times, e.g. 'The data agree with this:', 'They also cannot remove the problem:', 'The one-year anchor has no upper bound:'. Most are acceptable. Rewrite the ones where the colon hides the logical link (l.57, l.352).
- X-not-Y / 'rather than' closers, about 6 times, e.g. 'not hand-entered integers', 'a fixed commitment of the framework, not a configuration option', 'rather than reduced to the lesion mask alone', 'and not at a fixed horizon'.
- Announced enumerations, 3 times: 'for two reasons. They ...', 'Two consequences follow. First, ... Second, ...', 'Three properties of this schedule ... First, ... Second, ... Third, ...'.
- Conversational 'on purpose', twice ('The window was nevertheless kept on purpose.', 'This is accepted on purpose;'). Use 'deliberately', which the chapter already uses in its footnote.
- The same relative clause, almost verbatim, twice: '\citet{Mai2024}, who describe a larger GA cohort from the same (MUW) clinic, report that ...' (l.26, l.51).
- Staccato runs of short sentences of the same length, in about 3 paragraphs: §3.2 first paragraph ('Channel~0 holds ... Channels~1--10 hold ... Channel~0 is ... The layer channels supply ...'), §3.4 first paragraph, §3.7 test-split paragraph.
- 'canonical' without a stated alternative or a definition, 4 times ('canonical scheme', 'canonical fold' twice, 'canonical setting').
- Storage-level vocabulary instead of design statements, about 5 times: 'split files', 'carry no eye suffix', 'keyed per eye', 'missingness flag', 'invalidate every precomputed dataset'.

## Findings

### 3.1 [low] §3.1 Dataset

`03-data.tex:11` · GPTZero: human · clarity

> The data used in this thesis is a longitudinal cohort of eyes with Geographic Atrophy, provided by the Medical University of Vienna (MUW). It was acquired in routine clinical practice at a single clinical site in Vienna.

**Issue.** 'The data ... is a ... cohort' equates the data with the cohort. 'clinical practice at a single clinical site' repeats 'clinical'.

**Suggestion.**

> The data used in this thesis comes from a longitudinal cohort of eyes with Geographic Atrophy and was provided by the Medical University of Vienna (MUW). It was acquired in routine clinical practice at a single site in Vienna.

### 3.2 [medium] §3.1 Dataset

`03-data.tex:26` · GPTZero: AI · clarity, ai-tone

> \citet{Mai2024}, who describe a larger GA cohort from the same MUW clinic, report that it was acquired on a Spectralis device.

**Issue.** 'it' can be read as the present data instead of Mai's cohort, which would turn an inference (the device TODO at l.28) into a stated fact. The relative clause 'who describe a larger GA cohort from the same ... clinic' recurs almost verbatim at l.51 and reads formulaic.

**Suggestion.**

> \citet{Mai2024} report that a larger GA cohort from the same MUW clinic was acquired on a Spectralis device.

### 3.3 [low] §3.1 Dataset

`03-data.tex:34` · GPTZero: AI · tone, ai-tone

> Ages are decimal values computed from the date of birth to the baseline visit, not hand-entered integers.

**Issue.** The closing antithesis 'not hand-entered integers' answers a question the reader has not asked and reads like a data-cleaning note. It is one of several X-not-Y closers in the chapter.

**Suggestion.**

> Ages are decimal values, computed from the date of birth to the baseline visit.

### 3.4 [low] §3.1 Dataset

`03-data.tex:37` · GPTZero: AI · clarity

> The data does not contain the raw three-dimensional OCT volumes. Instead, each visit provides a set of registered two-dimensional en-face derivatives.

**Issue.** Chapter 2 uses 'derivative' throughout for spatial derivatives (FDM, stencils), so 'en-face derivatives' can be misread. The intended meaning is 'maps derived from the volume'.

**Suggestion.**

> The data does not contain the raw three-dimensional OCT volumes. Instead, each visit provides a set of registered two-dimensional en-face maps derived from them.

### 3.5 [medium] §3.1 Dataset

`03-data.tex:42` · GPTZero: AI · clarity

> Each visit further provides a GA mask, a scanning laser ophthalmoscopy (SLO) fundus image and a fundus-autofluorescence image, all in the SLO reference frame, together with two files of coordinate transforms between the OCT and the SLO frame. Only the OCT-grid mask and the layer array are required.

**Issue.** 'Each visit further provides a GA mask' comes right after the mask was introduced as 'The first' file, so it reads like a duplicate entry. The reader has to work out that this is a second mask in another frame. 'are required' does not say what requires them.

**Suggestion.**

> Each visit further provides a scanning laser ophthalmoscopy (SLO) fundus image, a fundus-autofluorescence image and a second GA mask, all three in the SLO reference frame, together with two files of coordinate transforms between the OCT and the SLO frame. Only the OCT-grid mask and the layer array are required by the pipeline.

### 3.6 [medium] §3.1 Dataset

`03-data.tex:50` · GPTZero: AI · flow, clarity, ai-tone

> The GA mask was not segmented on the OCT. \citet{Mai2024}, who describe a larger GA cohort from the same clinic, report that GA was outlined manually on the fundus-autofluorescence image by certified graders of the Vienna Reading Center, as well-demarcated areas of markedly decreased or absent autofluorescence.

**Issue.** The reader has just read 'a binary GA mask on the native OCT en-face grid', and the flat opener seems to contradict it without saying so. The next sentence repeats the relative clause from l.26 word for word.

**Suggestion.**

> Although it is stored on the OCT grid, the GA mask was not segmented on the OCT. For the larger cohort from the same clinic, \citet{Mai2024} report that GA was outlined manually on the fundus-autofluorescence image by certified graders of the Vienna Reading Center, as well-demarcated areas of markedly decreased or absent autofluorescence.

### 3.7 [low] §3.1 Dataset

`03-data.tex:57` · GPTZero: AI · clarity

> The data agree with this: the OCT-grid mask coincides with the SLO-frame mask mapped through the recorded transform, with an intersection over union of at least 0.9995 on all 553 visits.

**Issue.** 'The data agree' is plural, while the chapter treats 'data' as singular elsewhere ('The data does not contain', 'The data is partitioned'). 'agree with this' is also vague about what is compared.

**Suggestion.**

> The stored files are consistent with this: the OCT-grid mask coincides with the SLO-frame mask mapped through the recorded transform, with an intersection over union of at least 0.9995 on all 553 visits.

### 3.8 [medium] §3.1 Dataset

`03-data.tex:65` · GPTZero: human · clarity

> The native en-face grids are not uniform.

**Issue.** In this thesis 'uniform grid' has a technical sense (uniform spacing, as opposed to a moved mesh), so 'not uniform' suggests non-uniform pixel spacing. The paragraph then says the opposite: spacing is constant and only the sizes differ.

**Suggestion.**

> The native en-face grids do not all have the same size.

### 3.9 [low] §3.1 Dataset

`03-data.tex:69` · GPTZero: AI · clarity

> Upstream of this work, the stored en-face arrays were resampled onto one gold-standard pixel spacing: 0.12118\,mm between B-scans, 0.00568\,mm between A-scans, and 0.003867\,mm per axial pixel. Pixel spacing is therefore treated as constant across the cohort, while pixel counts, and with them the physical extent of each native grid, differ between eyes.

**Issue.** In a clinical thesis 'gold-standard' usually means a ground-truth reference, which is misleading for a resampling target. The last sentence puts a parenthetical ('and with them ...') inside a contrast clause.

**Suggestion.**

> Upstream of this work, the stored en-face arrays were resampled onto one common pixel spacing: 0.12118\,mm between B-scans, 0.00568\,mm between A-scans, and 0.003867\,mm per axial pixel. Pixel spacing is therefore treated as constant across the cohort. Pixel counts differ between eyes, and so does the physical extent of each native grid.

### 3.10 [medium] §3.1 Dataset

`03-data.tex:82` · GPTZero: AI · clarity

> Lesion growth is summarised on the square-root area scale. This transform is used for GA, because it removes the dependence of growth rates on baseline lesion size \citep{Yehoshua2011,Feuer2013}.

**Issue.** The 'square-root-area growth rate' quoted in the next sentence is never described in plain words, and the author asks for every measure to be explained on first use. 'This transform is used for GA, because' has an unneeded comma and a vague 'is used'.

**Suggestion.**

> Lesion growth is summarised as the yearly change in the square root of the lesion area, a transform used for GA because it removes the dependence of growth rates on baseline lesion size \citep{Yehoshua2011,Feuer2013}.

### 3.11 [low] §3.1 Dataset

`03-data.tex:98` · GPTZero: human · flow, clarity

> Figure~\ref{fig:data:example-state} shows one visit of the cohort in the views used throughout this chapter.

**Issue.** The one-sentence paragraph follows the growth statistics, which it has nothing to do with. 'the views used throughout this chapter' is vague, because the chapter does not refer to 'views'.

**Suggestion.**

> Reword, and move it to the end of the mask-provenance paragraph (after l.60), where the SLO frame and the OCT-grid mask have just been introduced: Figure~\ref{fig:data:example-state} shows one visit as the SLO fundus image with the OCT field of view, the GA mask on the modelling grid and a layer-boundary depth map.

### 3.12 [low] Figure 3.1 caption

`03-data.tex:132` · GPTZero: AI · clarity

> Panels (b) and (c) show the state tensor as the models receive it.

**Issue.** The models receive normalised values of all eleven channels. The panels show two channels in raw units (a binary mask and a map coloured by axial depth), so 'as the models receive it' says more than the figure shows.

**Suggestion.**

> Panels (b) and (c) show two of the eleven channels of the state tensor on the modelling grid, before normalisation.

### 3.13 [low] §3.2 State Representation

`03-data.tex:141` · GPTZero: AI · ai-tone, clarity

> The state of an eye at each visit is an eleven-channel tensor, so $C = 11$. Channel~0 holds the binary GA mask. Channels~1--10 hold the ten layer-boundary depth maps, ordered from the most superficial boundary to the deepest. Channel~0 is both the prediction target and the clinical deliverable. The layer channels supply structural context and serve as auxiliary prediction targets.

**Issue.** Five short sentences of similar length, two of them opening with 'Channel~0'. The roles are listed after both definitions as a mirrored pair ('Channel~0 is both X and Y. The layer channels supply X and serve as Y.').

**Suggestion.**

> The state of an eye at a visit is a tensor with $C = 11$ channels. Channel~0 holds the binary GA mask, which is both the prediction target and the clinical deliverable. Channels~1--10 hold the ten layer-boundary depth maps, ordered from the most superficial boundary to the deepest. They supply structural context and serve as auxiliary prediction targets.

### 3.14 [medium] §3.2 State Representation

`03-data.tex:166` · GPTZero: AI · flow, ai-tone

> Retinal thickness, the distance between the deepest and the shallowest boundary, is not computed anywhere in this pipeline. It could be recovered from the layer channels, but it is neither stored nor used as an input. The reason for keeping all ten layer channels next to the mask was given in~\S\ref{sec:background:ga-oct:state-rep}: documented predictors of GA progression are found throughout the vertical retinal column, not only inside the lesion. The layer geometry is therefore kept in full rather than reduced to the lesion mask alone.

**Issue.** The paragraph opens with what is not done (thickness) and only then gives the reason for what is done, so the reader has to work out the link. It closes with a 'therefore ... rather than ...' sentence that only restates the sentence before.

**Suggestion.**

> All ten layer channels are kept next to the mask because documented predictors of GA progression are found throughout the vertical retinal column, not only inside the lesion (\S\ref{sec:background:ga-oct:state-rep}). Retinal thickness, the distance between the deepest and the shallowest boundary, could be recovered from these channels, but it is not computed anywhere in this pipeline and is neither stored nor used as an input.

### 3.15 [low] §3.3 Spatial Standardisation and its Measured Cost

`03-data.tex:187` · GPTZero: AI · ai-tone

> Cropping and padding are used instead of resampling for two reasons. They introduce no interpolation artefacts, and they keep the stored pixel spacing identical across the cohort by construction.

**Issue.** An announced enumeration ('for two reasons.') followed by the list, plus the stock phrase 'by construction'.

**Suggestion.**

> Cropping and padding are used instead of resampling because they introduce no interpolation artefacts and keep the stored pixel spacing identical across the cohort.

### 3.16 [low] §3.3 Spatial Standardisation and its Measured Cost

`03-data.tex:189` · GPTZero: AI · flow

> The use of a $6 \times 6$\,mm analysis window in the literature was reviewed in~\S\ref{sec:background:ga-oct:muw}.

**Issue.** The literature pointer ends a paragraph about how the common grid is reached, before the window size has been given. It belongs next to the 5.938 x 5.816 mm figure in the next paragraph.

**Suggestion.**

> Delete it here and insert after the first sentence of the next paragraph (after '... holds 50\,176 grid positions.'): This physical extent is close to the $6 \times 6$\,mm analysis window used in the literature (\S\ref{sec:background:ga-oct:muw}).

### 3.17 [low] §3.3 Spatial Standardisation and its Measured Cost

`03-data.tex:195` · GPTZero: AI · clarity

> The spacing between B-scans is \textbf{21.335 times larger} than the spacing along them.

**Issue.** 'the spacing along them' requires the reader to remember that A-scans lie along a B-scan. §3.1 (l.71) already names the two spacings 'between B-scans' and 'between A-scans'.

**Suggestion.**

> The spacing between B-scans is \textbf{21.335 times larger} than the spacing between A-scans.

### 3.18 [low] §3.3 Spatial Standardisation and its Measured Cost

`03-data.tex:211` · GPTZero: AI · flow *(added in verification)*

> Zero also cannot serve as a sentinel that marks padding, because real layer values range from $-14$ to $499$ and so include zero.

**Issue.** The paragraph goes from the raw meaning of zero to the normalised value and the loss, then back to raw values with this sentence. As the closing sentence it interrupts the conclusion about training at full weight.

**Suggestion.**

> Move this sentence up so that it directly follows '... a layer depth of 0 is the top of the volume, above the retina.' (l.204), before 'The models, however, do not see raw values.'

### 3.19 [medium] §3.3 Spatial Standardisation and its Measured Cost

`03-data.tex:221` · GPTZero: AI · clarity, flow

> Growth across that edge is censored, and no missingness flag records it. The models are therefore trained on censored targets, and the change-region metrics at the one-year anchor under-measure progression for roughly one visit in five.

**Issue.** 'censored' is a technical term used without a plain explanation. 'change-region metrics' and 'one-year anchor' appear before Chapter 5 defines them, with no pointer. 'missingness flag' is storage jargon.

**Suggestion.**

> Growth across that edge is not observed (it is censored), and no flag in the data marks it. The models are therefore trained on censored targets, and the change-region metrics at the one-year anchor (\S\ref{sec:experiments:protocol}) under-measure progression for roughly one visit in five.

### 3.20 [low] §3.3 Spatial Standardisation and its Measured Cost

`03-data.tex:228` · GPTZero: AI · tone, clarity

> The window was nevertheless kept on purpose.

**Issue.** 'on purpose' is conversational (it recurs at l.356). The bare 'window' also collides with the temporal 'window' of §3.5-§3.6.

**Suggestion.**

> The $49 \times 1024$ window was nevertheless kept deliberately.

### 3.21 [medium] §3.3 Spatial Standardisation and its Measured Cost

`03-data.tex:234` · GPTZero: human · flow

> The training loss can optionally exclude pad positions.

**Issue.** The sentence dangles at the end of a paragraph about lesion censoring, which is not about pad positions. It also repeats the point already made at l.209-211 ('No reported run excludes the pad positions from the loss').

**Suggestion.**

> Delete it here and replace l.209-211 ('No reported run excludes ... at full weight.') with: The training loss can optionally exclude the pad positions, but no reported run does so (\S\ref{sec:method:training}). The models are therefore trained to reproduce this value at full weight.

### 3.22 [low] §3.4 Normalisation

`03-data.tex:244` · GPTZero: AI · clarity, flow

> After spatial standardisation, each channel is normalised. The statistics are computed per channel over the training visits of the current fold only, and are then applied to every visit, including the validation visits. No validation data enters the statistics. Because they are computed on the cropped and padded states, the padded zeros contribute to each channel's mean and standard deviation (\S\ref{sec:data:spatial}).

**Issue.** 'over the training visits of the current fold only' and 'No validation data enters the statistics' say the same thing. The padded-zeros sentence repeats §3.3 almost verbatim, so the two sections cross-reference each other for one fact.

**Suggestion.**

> After spatial standardisation, each channel is normalised. The statistics are computed per channel over the training visits of the current fold only and are then applied to every visit, including the validation visits. As noted in~\S\ref{sec:data:spatial}, the padded zeros contribute to each channel's mean and standard deviation.

### 3.23 [low] §3.4 Normalisation

`03-data.tex:252` · GPTZero: AI · clarity

> The canonical scheme is a z-score,

**Issue.** 'canonical scheme' implies that alternative schemes exist, but the text no longer mentions any (the min-max variant was removed in review #1 of 2026-09-27).

**Suggestion.**

> The normalisation is a z-score,

### 3.24 [medium] §3.4 Normalisation

`03-data.tex:260` · GPTZero: AI · clarity, ai-tone

> On the canonical fold, the background value 0 maps to $-0.602$ and the foreground value 1 maps to $+1.660$. The binarisation threshold of 0.5 maps to $+0.529$. Two consequences follow. First, the normalised mask has a hard step at the lesion edge. Second, evaluation maps every threshold into normalised space rather than mapping the prediction back to the original scale, and this mapping must be applied consistently.

**Issue.** 'the canonical fold' is used here and at l.286 but is defined (as fold 2) only in Chapter 5 (05-experiments.tex l.101). 'Two consequences follow. First ... Second ...' is an announced enumeration.

**Suggestion.**

> On the canonical fold (fold~2), the background value 0 maps to $-0.602$, the foreground value 1 maps to $+1.660$, and the binarisation threshold of 0.5 maps to $+0.529$. The normalised mask therefore has a hard step at the lesion edge. Evaluation maps every threshold into normalised space rather than mapping the prediction back to the original scale, and this mapping must be applied consistently.

### 3.25 [**HIGH**] §3.5 Patient-Level Covariates

`03-data.tex:272` · GPTZero: AI · flow, clarity

> Each window is accompanied by two patient-level covariates, age and sex.

**Issue.** 'window' has two meanings in this chapter: the spatial 49 x 1024 crop region (§3.3: 'The resulting window', 'the border of the window', 'Larger windows', 'any window') and the temporal pair of visits (§3.5-§3.6). Here it is used in the temporal sense before §3.6 defines it, so a reader coming from §3.3 will take it to mean the crop.

**Suggestion.**

> Each transition window (a pair of consecutive visits, \S\ref{sec:data:temporal}) is accompanied by two patient-level covariates, age and sex. Optionally, also use 'crop' instead of 'window' for the spatial region in §3.3 (l.193, 216, 220, 228, 229, 231; keep the literature's 'analysis window' at l.190).

### 3.26 [low] §3.5 Patient-Level Covariates

`03-data.tex:274` · GPTZero: AI · clarity, tone *(added in verification)*

> The table is keyed per eye, so a patient who contributes two eyes appears in two rows with the same age and sex.

**Issue.** 'keyed per eye' is database vocabulary. It is part of the engineering-log register that recurs in the chapter (split files, eye suffix, missingness flag).

**Suggestion.**

> The table has one row per eye, so a patient who contributes two eyes appears in two rows with the same age and sex.

### 3.27 [low] §3.5 Patient-Level Covariates

`03-data.tex:283` · GPTZero: AI · clarity

> The z-score statistics for this mode are computed over all training window-start ages. Since there is one start age per window, the final visit of each training eye does not enter them.

**Issue.** 'training window-start ages' is a dense noun stack, and 'Since there is one start age per window' takes a roundabout route to the point.

**Suggestion.**

> The z-score statistics for this mode are computed over the start-visit ages of all training windows. Because each window contributes only the age at its start visit, the final visit of each training eye does not enter them.

### 3.28 [medium] §3.6 Temporal Structure

`03-data.tex:305` · GPTZero: AI · ai-tone, tone

> Each window holds exactly one transition; this is a fixed commitment of the framework, not a configuration option.

**Issue.** A clause pair joined by a semicolon that ends in an 'X, not Y' antithesis. 'fixed commitment' is a rhetorical way of saying that the setting cannot be changed.

**Suggestion.**

> Each window holds exactly one transition. This is fixed by the framework and cannot be changed by configuration.

### 3.29 [medium] §3.6 Temporal Structure

`03-data.tex:336` · GPTZero: AI · flow, clarity

> Three properties of this schedule shape the rest of the pipeline. First, every interval is a multiple of the 90-day acquisition grid, and the most common interval is 180 days.

**Issue.** The topic sentence promises properties that shape the pipeline, but the first property is never tied to anything. Its link (180 days is the base of the training time budget, 04-method.tex l.1106-1107) is left implicit. '90-day acquisition grid' also overloads 'grid', which everywhere else in the thesis means the spatial grid.

**Suggestion.**

> Three properties of this schedule shape the rest of the pipeline. First, every interval is a multiple of 90 days, and the most common interval, 180 days, is the base of the time budget used in training (\S\ref{sec:method:training}). In addition, merge the one-sentence table paragraph (l.312-313) into the start of this paragraph.

### 3.30 [low] §3.6 Temporal Structure

`03-data.tex:341` · GPTZero: AI · clarity *(added in verification)*

> A training scheme restricted to intervals shorter than the modal 180 days would therefore learn from this densely imaged subgroup alone.

**Issue.** 'intervals shorter than the modal 180 days' is a roundabout way to say the 90-day intervals, the only shorter interval in Table~\ref{tab:data:intervals}.

**Suggestion.**

> A training scheme restricted to the 90-day intervals would therefore learn from this densely imaged subgroup alone.

### 3.31 [medium] §3.6 Temporal Structure

`03-data.tex:344` · GPTZero: AI · clarity

> Third, the schedule limits how far an eye can be rolled forward during training, where several visits are chained within a fixed time budget (\S\ref{sec:method:training}). With a budget of 90 days, none of the 75 eyes can chain two visits. With 360 days, 74 of the 75 eyes reach at least one autoregressive step.

**Issue.** The 'where' clause is loosely attached. The counts switch from 'chain two visits' to 'reach at least one autoregressive step', so a reader cannot tell whether the 90-day and 360-day statements measure the same quantity.

**Suggestion.**

> Third, the schedule limits how far an eye can be rolled forward during training, because the training curriculum chains visits within a fixed time budget (\S\ref{sec:method:training}). With a budget of 90 days, none of the 75 eyes can chain two visits, so no step is unrolled. With 360 days, 74 of the 75 eyes reach at least one unrolled step.

### 3.32 [medium] §3.6 Temporal Structure

`03-data.tex:351` · GPTZero: AI · clarity, flow

> The same schedule also shapes the evaluation. The one-year anchor has no upper bound: the metric is taken at the first rollout step whose cumulative time reaches about 347 days. For 68 of the 75 eyes, this is exactly 360 days.

**Issue.** 'The one-year anchor' and 'the metric' appear without definition. The colon presents the definition of the anchor as if it explained 'no upper bound', so the reader has to work out that the scored step can fall well beyond one year. After 'Three properties', this paragraph also reads as an uncounted fourth item.

**Suggestion.**

> Beyond training, the schedule also affects the evaluation. The change-region metrics are taken at a one-year anchor, the first rollout step whose cumulative time reaches about 347 days. This anchor has no upper bound. For 68 of the 75 eyes, it falls at exactly 360 days.

### 3.33 [low] §3.6 Temporal Structure

`03-data.tex:356` · GPTZero: AI · tone

> This is accepted on purpose; \citet{Mai2024} likewise score every follow-up visit by its time since baseline, in yearly bins, and not at a fixed horizon.

**Issue.** 'on purpose' is conversational and recurs (l.228). The semicolon pair reads more naturally as two sentences.

**Suggestion.**

> This is accepted deliberately. \citet{Mai2024} likewise score every follow-up visit by its time since baseline, in yearly bins, and not at a fixed horizon.

### 3.34 [medium] §3.7 Splits and Cross-Validation

`03-data.tex:364` · GPTZero: AI · clarity, tone

> The data is partitioned by five split files that define a patient-level 5-fold cross-validation. The five validation sets do not overlap, and together they cover all patients. The split identifiers carry no eye suffix, so both eyes of a patient always fall into the same partition.

**Issue.** 'split files' and 'carry no eye suffix' describe the storage format instead of the design. A reader without the repository cannot tell what an eye suffix is.

**Suggestion.**

> The data is partitioned into five folds for a patient-level cross-validation. The five validation sets do not overlap, and together they cover all patients. The folds are defined on patient identifiers, so both eyes of a patient always fall into the same partition.

### 3.35 [medium] §3.7 Splits and Cross-Validation

`03-data.tex:399` · GPTZero: AI · clarity, tone, ai-tone

> The test split is structurally empty. An eye whose patient appeared in neither the training nor the validation list would be assigned to a test partition. However, every patient with scans is assigned to training or validation in every fold. No test partition is therefore ever produced. The protocol is 5-fold train/validation cross-validation, and every result reported in this thesis is a validation result.

**Issue.** 'structurally empty' is unexplained jargon. Five short sentences walk through the assignment logic before reaching the statement the reader needs, and the first and fourth sentences say the same thing.

**Suggestion.**

> The test split is empty in every fold. An eye whose patient appeared in neither the training nor the validation list would be assigned to a test partition, but every patient with scans is assigned to training or validation in every fold. The protocol is therefore 5-fold train/validation cross-validation, and every result reported in this thesis is a validation result.

### 3.36 [low] §3.7 Splits and Cross-Validation

`03-data.tex:408` · GPTZero: AI · flow

> The folds also differ in baseline lesion size.

**Issue.** 'also' refers back to the per-fold eye counts (l.373-375), but the test-split paragraph comes between them, so the chapter ends on a point that has lost its anchor.

**Suggestion.**

> Move the whole paragraph (l.408-411) directly after the per-fold eye-count paragraph (l.373-375), before the test-split paragraph. The opening sentence can then stay as it is.

