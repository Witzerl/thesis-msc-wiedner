# Micro feedback 1: Abstract (English) + Ch. 1 Introduction

[← Overview](00-overview.md)

43 findings: 3 high, 26 medium, 14 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

The abstract follows a sound order: problem, question, method, results, take-away. Its third paragraph carries four separate messages (loss weighting, the three strongest operators, the reach and transport effects, the nulls). It opens with the secondary loss-weighting finding before the headline comparison. It also uses terms the abstract never explains: persistence, pushforward curriculum, 'this slot', index-space neighbour graph, seeds and 'the same deficit'. Chapter 1 follows the hour-glass model: clinical burden, then the forecasting task and its data properties, then the PDE-solver argument, the research question, the contributions and the outline. The weak points are the section boundaries. §1.1 closes on Vallino's 'predictive probabilities' and 'This thesis pursues that avenue', and §1.2 then sets the forecast apart from a risk score. §1.2 announces that the next section 'motivates such a framework', but §1.3 first argues about the operator's locality and reach. The last paragraph of §1.3 repeats the §1.2 contrast with earlier clinical work and interrupts the run-up to the research question. The split into setup and operator (Chapters 4 and 5) is stated three times within about a page (l. 165-166, 189-195, 219-222). The contributions paragraph names 'the same deficit', which the chapter never defines under that name, and a 'moving-mesh extension' that is explained only afterwards, in the last sentence of the outline. §1.2 promises that the covariates are 'tested in this thesis', but the compiled Chapter 5 reports no such test. The register is mostly plain and consistent. The machine-like tone comes from structural habits, not vocabulary: em-dash insertions, 'not X but Y' antitheses, short paragraph closers, announcement openers and a 'therefore' at many argument steps. Terminology drifts between model, operator, architecture, family and class, and 'these properties' means two different things in consecutive paragraphs of §1.2.

### Transitions

- Abstract, paragraph 3 (00-abstract.tex l. 39-58): about 200 words carrying four messages. Split it after 'against zero for a model that predicts no change.' (l. 45) and start a new paragraph with 'The Finite Element Network ...' / 'The differences between operators ...'. Move the loss-weighting sentence (l. 39-41) to after the operator results (after l. 58), so the results open with the headline comparison.
- Abstract vs. Chapter 1: the abstract reports the loss-weighting finding (mask weighting required, soft-Dice about +0.05), but the contributions paragraph of §1.3 (l. 197-205) does not mention the objective. The two summaries of the findings therefore diverge. Aligning them in one direction is the author's decision; no new content is implied.
- §1.1, first paragraph (l. 11-28): the topic moves AMD -> GA (l. 17-23) -> AMD again ('Unlike other eye diseases ...', l. 23-28). Consider moving the 'Unlike ...' sentence and 'Clinical care therefore focuses ...' to directly after the Flaxman ranking sentence (l. 15), so the paragraph narrows once, from AMD to GA.
- §1.1 -> §1.2 (l. 64-69 -> l. 75-84): §1.1 ends on AI providing 'predictive probabilities of GA development' and 'This thesis pursues that avenue', and §1.2 then sets the output apart from a 'single risk score'. Let the closing sentence of §1.1 already signal the difference, e.g. 'This thesis follows that direction, but forecasts the lesion map itself.'
- §1.2 -> §1.3 (l. 109-112 -> l. 118): 'The next section motivates such a framework' does not match the opening of §1.3, which argues that GA growth has local, PDE-like structure, an argument about the operator. Merge the two closing sentences so the announcement also covers the operator question (see the finding at l. 109).
- §1.3, last paragraph (l. 168-174): the contrast with cohort-level atlases, survival models and biomarker risk analyses repeats the §1.2 contrast (l. 81-84) and sits between the framework/operator separation and the research question. Consider moving it to §1.2, where earlier work is first contrasted, and keeping only the pointer to Section~\ref{sec:background:related-work} in §1.3 (see the finding at l. 168).
- Research question -> outline: the split 'setup vs operator, Chapter 4 vs Chapter 5' is stated at l. 165-168, again at l. 189-195 and a third time at l. 219-222. Keep the full mapping once, directly after the research question, and shorten the other two (see the findings at l. 189 and l. 219).
- Contributions paragraph (l. 201-205): 'two independent routes to the same deficit' has no antecedent under that name. Tie it back to the earlier statement in §1.3 that the operator's 'reach must match the distance the front moves between two visits' (l. 146-147) by glossing the deficit in place. The 'moving-mesh extension' appears here for the first time and is explained only in the last sentence of the outline (l. 225-226); a short gloss here helps.
- §1.2, covariates (l. 98-102): 'is tested in this thesis' promises a result the compiled Chapter 5 does not contain. The covariate subsection is inside \iffalse, and §6.3 says their value 'is not settled'. A reader who follows the promise will not find the test. Align the sentence with what the thesis reports.
- Edge to Chapter 2: the transition works. Chapter 2 takes the clinical framing of Chapter 1 as read, and the outline (l. 215-217) announces its content accurately. No change needed.

### Recurring tells in this part

- Em-dash insertions or appendages that interrupt the clause: e.g. 'the late non-neovascular stage --- termed \emph{Geographic Atrophy} (GA) --- is ...' (l. 17), '--- properties that classical solvers build in ...' (l. 148), 'The setup --- how elapsed time ... --- is fixed once' (l. 165), '--- larger models, ... ---' (l. 203). 4 in Chapter 1. Replace with commas, parentheses or a sentence split.
- 'not X but Y' / 'X, not Y' antitheses: 'not \emph{whether} ... but \emph{how fast} and \emph{where}' (l. 43), 'not a single risk score but a complete map' (l. 83), 'not only a question of the model itself but also' (l. 104), and the abstract closer '..., not which family the operator belongs to' (l. 62-64). About 4. Keep at most one, stated plainly.
- Short sentence closing a paragraph that restates or teases: 'This thesis pursues that avenue.' (l. 68), 'Which model should sit inside it is a separate question.' (l. 111-112), 'This is the structural fingerprint of ...' (l. 135). 3. The abstract's 'The largest is physical reach.' (l. 48) works the same way inside a paragraph.
- Announcement openers: 'The clinical implication is twofold.' (l. 58), 'What the thesis delivers follows from this design.' (l. 197). 2. Start directly with the content. ('The remainder of this thesis is organised as follows.', l. 214, is the conventional outline opener and can stay.)
- 'therefore' as the connective at most argument steps: l. 27, 43, 146, 164. Each is fine alone, but together they form a mechanical chain. Drop it where the logical link is already obvious.
- Filler adverbs: 'naturally' (l. 75, 92), 'actually' (l. 162), 'on its own' (abstract l. 48). About 4. Delete them. ('on its own' at l. 106 carries meaning, 'without a framework', and can stay.)
- Colon reveals with a rhetorical set-up: 'the therapeutic landscape for GA was empty:' (l. 47), 'treatment timing now matters:' (l. 59), abstract 'provided its loss weighted the lesion mask:' (l. 39). 3. The informative colons (l. 92, 140, 155) are fine.
- Terminology drift for the same objects: model / operator / architecture / family / class / setup / framework, with frequent switches in §1.3 and the research-question paragraph. 'these properties' means data properties at l. 86 and missing model abilities at l. 107, and 'requirements' (l. 104) re-labels the 'properties' of l. 86.
- Repeated stock phrase 'on equal terms' (l. 168, 199, 222): 3 occurrences within one and a half pages.
- Terms used before they are explained: OCT (l. 35, 66; spelled out only at l. 77), en-face (l. 76), RPE (l. 96), stencil (l. 149), 'the same deficit' and 'moving-mesh extension' (l. 202-204). In the abstract: persistence, pushforward curriculum, 'this slot', index-space neighbour graph, seeds.
- Personified abstractions: 'The clinical reality of OCT follow-up imposes ...' (l. 86), 'The literature offers many such operators' (l. 154), abstract 'The framework served every operator' (l. 39). About 3.

## Findings

### 1.1 [medium] Abstract, paragraph 2

`00-abstract.tex:29` · GPTZero: not scanned / not matched · clarity

> A zero-initialised output starts every operator at exact persistence, and all operators are trained with one pushforward curriculum measured in elapsed days and one loss.

**Issue.** 'persistence' is not explained, 'and one loss' dangles at the end, and it is unclear whether 'measured in elapsed days' applies to the curriculum or the loss.

**Suggestion.**

> A zero-initialised output layer starts every operator at exact persistence (no change), and all operators share one loss and one pushforward curriculum measured in elapsed days.

### 1.2 [medium] Abstract, paragraph 2

`00-abstract.tex:31` · GPTZero: not scanned / not matched · clarity

> Only the operator $f_\theta$ varies. Message-passing graph networks on two neighbourhood graphs, a U-Net, Fourier Neural Operators with and without a local path, and Finite Element Networks with and without a learned transport term were placed in this slot at matched parameter counts.

**Issue.** The 30-word subject list delays the verb to the end, and 'this slot' has no antecedent: the abstract never calls $f_\theta$ a slot.

**Suggestion.**

> Only the operator $f_\theta$ varies. The operators compared at matched parameter counts were message-passing graph networks on two neighbourhood graphs, a U-Net, Fourier Neural Operators with and without a local path, and Finite Element Networks with and without a learned transport term.

### 1.3 [medium] Abstract, paragraph 2

`00-abstract.tex:35` · GPTZero: not scanned / not matched · clarity

> They were compared by five-fold cross-validation on 75 eyes of 51 patients from the Medical University of Vienna, using the Dice of the changed region at one year.

**Issue.** The headline metric is not explained, and the next paragraph switches to the label 'change-region Dice' without linking the two.

**Suggestion.**

> They were compared by five-fold cross-validation on 75 eyes of 51 patients from the Medical University of Vienna, using the change-region Dice at one year, the overlap between the pixels predicted to change and those that changed.

### 1.4 [medium] Abstract, paragraph 3

`00-abstract.tex:39` · GPTZero: not scanned / not matched · clarity, ai-tone, flow

> The framework served every operator without change, provided its loss weighted the lesion mask: without that weighting no change was learned, and a soft-Dice term added about 0.05.

**Issue.** The framework is personified ('served'), the sentence ends in a colon reveal, and 'added about 0.05' has no referent. Placed first, this secondary finding comes before the headline result (see flow notes).

**Suggestion.**

> The framework could be used unchanged for every operator, provided the loss gave extra weight to the lesion mask. Without this weighting no change was learned, and an additional soft-Dice term raised the change-region Dice by about 0.05.

### 1.5 [low] Abstract, paragraph 3

`00-abstract.tex:45` · GPTZero: not scanned / not matched · clarity

> The Finite Element Network lies above the U-Net at two seeds and only slightly above the graph network.

**Issue.** 'lies above ... at two seeds' is lab jargon that an abstract reader may not decode.

**Suggestion.**

> The Finite Element Network scores above the U-Net in runs with two different random seeds and only slightly above the graph network.

### 1.6 [low] Abstract, paragraph 3

`00-abstract.tex:47` · GPTZero: not scanned / not matched · ai-tone, clarity

> The differences between operators trace back to a few properties, each measured on its own. The largest is physical reach.

**Issue.** 'on its own' is filler, and the clipped second sentence reads as a reveal. It is also unclear in what sense a property is 'the largest'.

**Suggestion.**

> The differences between operators trace back to a few properties, each measured separately, of which physical reach has the largest effect.

### 1.7 [low] Abstract, paragraph 3

`00-abstract.tex:49` · GPTZero: not scanned / not matched · clarity

> Replacing the index-space neighbour graph by a dilated stencil that reaches about 0.12\,mm, roughly as far as the lesion front moves between visits, raises the Dice by 0.064 at an identical parameter count, on all five folds.

**Issue.** 'index-space neighbour graph' is not explained in the abstract, so the contrast with the dilated stencil is hard to grasp.

**Suggestion.**

> Replacing the graph network's neighbour graph, built from pixel indices, by a dilated stencil that reaches about 0.12\,mm, roughly as far as the lesion front moves between visits, raises the Dice by 0.064 at an identical parameter count, on all five folds.

### 1.8 [**HIGH**] Abstract, paragraph 3

`00-abstract.tex:52` · GPTZero: not scanned / not matched · clarity, flow

> A learned transport term raises it by 0.062 over the same network without one, a second route to the same deficit; these two are the two highest operators.

**Issue.** 'the same deficit' has no antecedent in the abstract, so the reader cannot tell what is being corrected. 'these two' can be read as the transport term and the network without one instead of the two top operators, and 'the two highest operators' is elliptical. It is also not said which network carries the transport term.

**Suggestion.**

> A learned transport term in the Finite Element Network raises it by 0.062 over the same network without one. Both changes address the same deficit, an update that reaches less far than the lesion front moves between visits. The graph network on the dilated stencil and the Finite Element Network with transport are the two highest-scoring operators.

### 1.9 [low] Abstract, paragraph 3

`00-abstract.tex:54` · GPTZero: not scanned / not matched · clarity

> A purely spectral operator stays below the U-Net; adding a local path closed the gap at one seed only.

**Issue.** The name changes from 'Fourier Neural Operators with and without a local path' (l. 33) to 'a purely spectral operator', and the tense switches from present to past within the sentence.

**Suggestion.**

> The Fourier Neural Operator without a local path stays below the U-Net; adding a local path closes the gap at one seed only.

### 1.10 [medium] Abstract, paragraph 4

`00-abstract.tex:60` · GPTZero: not scanned / not matched · clarity

> The growth rate of an individual eye over its whole follow-up is predicted less well than where the lesion changes, with a correlation of 0.40 with the true rates.

**Issue.** The sentence compares a rate with 'where the lesion changes', and the double 'with ... with' construction is clumsy.

**Suggestion.**

> The growth rate of an individual eye over its whole follow-up is predicted less well than the location of change: predicted and true rates correlate at 0.40.

### 1.11 [medium] Abstract, closing sentence

`00-abstract.tex:62` · GPTZero: not scanned / not matched · ai-tone, tone

> For forecasts of this kind, the decisive design question is how far one update reaches compared with how far the disease moves between visits, not which family the operator belongs to.

**Issue.** This aphoristic closer combines a mirror pair ('how far ... how far') with an 'X, not Y' antithesis, which makes it the most slogan-like sentence of the abstract.

**Suggestion.**

> For forecasts of this kind, the decisive design question is how far one update reaches relative to the distance the lesion front moves between visits; the family to which the operator belongs is secondary.

### 1.12 [medium] §1.1 Clinical Motivation

`01-introduction.tex:17` · GPTZero: AI · clarity, ai-tone

> Among these, the late non-neovascular stage --- termed \emph{Geographic Atrophy} (GA) --- is an advanced, irreversible and progressive atrophy of the macula that causes a marked loss of visual acuity once the fovea is involved \citep{Vallino2024}.

**Issue.** 'Among these' refers to the people counted in the previous sentence, but the subject is a disease stage. The em-dash insertion splits subject from verb.

**Suggestion.**

> The late non-neovascular stage of AMD, termed \emph{Geographic Atrophy} (GA), is an advanced, irreversible and progressive atrophy of the macula that causes a marked loss of visual acuity once the fovea is involved \citep{Vallino2024}.

### 1.13 [medium] §1.1 Clinical Motivation

`01-introduction.tex:23` · GPTZero: AI · clarity, flow

> Unlike other eye diseases that cause vision loss, such as cataract, glaucoma or diabetic retinopathy, AMD is not counted among the avoidable causes of vision loss, defined as those that known, cost-effective means can prevent or treat \citep{Flaxman2020}.

**Issue.** 'those that known, cost-effective means can prevent or treat' is a garden-path construction, and 'vision loss' appears twice. The sentence also returns from GA to AMD (see flow notes).

**Suggestion.**

> Unlike cataract, glaucoma or diabetic retinopathy, AMD is not counted among the avoidable causes of vision loss, that is, causes that can be prevented or treated by known, cost-effective means \citep{Flaxman2020}.

### 1.14 [medium] §1.1 Clinical Motivation

`01-introduction.tex:40` · GPTZero: AI · flow, ai-tone

> An ageing population, frequent involvement of both eyes and eventual spread to the fovea make GA a long-term disease that progresses differently in every patient.

**Issue.** The tricolon subject is presented as the cause of patient-to-patient variability, which does not follow from it. The high bilateral concordance reported just before even points the other way.

**Suggestion.**

> An ageing population, frequent involvement of both eyes and eventual spread to the fovea make GA a long-term disease, and its course differs from patient to patient.

### 1.15 [medium] §1.1 Clinical Motivation

`01-introduction.tex:43` · GPTZero: AI · ai-tone

> The clinically relevant question is therefore not \emph{whether} a patient will deteriorate, but \emph{how fast} and \emph{where} in the macula the lesion will grow.

**Issue.** A 'not whether ... but how/where' antithesis with three italicised words closes the paragraph as a punchline, with the section's second 'therefore'.

**Suggestion.**

> Since further progression is expected, the clinically relevant questions are \emph{how fast} and \emph{where} in the macula the lesion will grow.

### 1.16 [low] §1.1 Clinical Motivation

`01-introduction.tex:47` · GPTZero: human · tone

> Until 2023, the therapeutic landscape for GA was empty: no treatment was approved, and numerous phase 1--3 trials of GA and intermediate AMD, addressing mechanisms such as neuroprotection, visual cycle modulation, antiamyloid pathways and cell replacement, had failed during the preceding decade \citep{Lad2023}.

**Issue.** 'the therapeutic landscape ... was empty' is a figurative set-up followed by a colon reveal; the plain statement after the colon already says it.

**Suggestion.**

> Until 2023, no treatment for GA was approved, and numerous phase 1--3 trials of GA and intermediate AMD, addressing mechanisms such as neuroprotection, visual cycle modulation, antiamyloid pathways and cell replacement, had failed during the preceding decade \citep{Lad2023}.

### 1.17 [medium] §1.1 Clinical Motivation

`01-introduction.tex:58` · GPTZero: AI · ai-tone

> The clinical implication is twofold. First, treatment timing now matters: an intervention that only slows progression is most valuable when administered before foveal involvement, because central vision is largely preserved until the atrophy reaches the fovea \citep{Boyer2017,Vallino2024}.

**Issue.** The announcement opener 'is twofold' is followed by a colon reveal, both typical of templated prose.

**Suggestion.**

> Two clinical consequences follow. First, the timing of treatment now matters. An intervention that only slows progression is most valuable when administered before foveal involvement, because central vision is largely preserved until the atrophy reaches the fovea \citep{Boyer2017,Vallino2024}.

### 1.18 [low] §1.1 Clinical Motivation

`01-introduction.tex:62` · GPTZero: AI · tone, clarity

> Second, intravitreal injections carry both patient burden and procedural risk, so identifying which eyes will progress rapidly enough to justify therapy is the critical decision support task.

**Issue.** 'the critical decision support task' is an intensifier on a noun stack, placed at the end of the sentence.

**Suggestion.**

> Second, intravitreal injections carry both patient burden and procedural risk, so the main decision-support task is to identify the eyes that will progress fast enough to justify therapy.

### 1.19 [medium] §1.1 Clinical Motivation (closing)

`01-introduction.tex:64` · GPTZero: AI · ai-tone, flow

> As \citet{Vallino2024} note in their conclusions, the integration of artificial intelligence with structural OCT biomarkers holds significant promise, and artificial intelligence applied to OCT has the potential to provide predictive probabilities of GA development over time. This thesis pursues that avenue.

**Issue.** The closer 'pursues that avenue' is a metaphorical one-liner, and it ties the thesis to 'predictive probabilities', which §1.2 sets aside one paragraph later in favour of a lesion map.

**Suggestion.**

> Keep the Vallino sentence as it is and replace the closer with: This thesis follows that direction, but forecasts the lesion map itself.

### 1.20 [low] §1.2 Problem Statement

`01-introduction.tex:75` · GPTZero: AI · clarity, tone

> Predicting GA progression from imaging is naturally framed as a \emph{spatiotemporal forecasting} task on the en-face projection of optical coherence tomography (OCT) volumes.

**Issue.** 'naturally' is filler, and 'en-face' is not explained in Chapter 1. OCT is spelled out here although it is already used at l. 35 and l. 66.

**Suggestion.**

> Predicting GA progression from imaging is framed here as a \emph{spatiotemporal forecasting} task on the en-face (frontal, two-dimensional) projection of OCT volumes. (Spell out 'optical coherence tomography (OCT)' at its first use, l. 35.)

### 1.21 [medium] §1.2 Problem Statement

`01-introduction.tex:77` · GPTZero: AI · clarity

> For each eye, longitudinal imaging yields a sequence of macula-centred grids on which the lesion outline and the underlying retinal layer geometry are traced; given the most recent observed state and a target horizon $\Delta t$, the goal is to predict the full spatial configuration of the lesion at the future visit.

**Issue.** Two separate ideas (the data and the task) are joined by a semicolon into a 55-word sentence, and 'full spatial configuration' is an abstract noun stack.

**Suggestion.**

> For each eye, longitudinal imaging yields a sequence of macula-centred grids on which the lesion outline and the underlying retinal layer geometry are traced. Given the most recent observed state and a target horizon $\Delta t$, the task is to predict the extent and shape of the lesion at the later visit.

### 1.22 [low] §1.2 Problem Statement

`01-introduction.tex:81` · GPTZero: AI · ai-tone, clarity

> This differs from earlier work on AMD, which predicts or characterises the conversion of an eye to a later disease stage \citep{SchmidtErfurth2018, Vogl2021}. The output here is not a single risk score but a complete map of the lesion at the next visit.

**Issue.** A 'not X but Y' antithesis. 'next visit' also conflicts with 'future visit' and the target horizon of the previous sentence, which may span several visits.

**Suggestion.**

> This differs from earlier work on AMD, which predicts or characterises the conversion of an eye to a later disease stage \citep{SchmidtErfurth2018, Vogl2021}. The output here is a complete map of the lesion at the future visit instead of a single risk score.

### 1.23 [low] §1.2 Problem Statement

`01-introduction.tex:86` · GPTZero: human · tone

> The clinical reality of OCT follow-up imposes three properties on the data that a model has to deal with.

**Issue.** A personified abstraction ('clinical reality ... imposes') ending in the colloquial 'has to deal with'.

**Suggestion.**

> Clinical OCT follow-up gives the data three properties that a model must handle.

### 1.24 [medium] §1.2 Problem Statement

`01-introduction.tex:89` · GPTZero: AI · clarity

> There is no shared temporal origin across eyes, which rules out methods that assume a fixed sampling rate or a common $t = 0$.

**Issue.** Logic slip: the missing temporal origin rules out a common $t = 0$, but a fixed sampling rate is ruled out by the irregular spacing stated in the previous sentence.

**Suggestion.**

> Irregular spacing rules out methods that assume a fixed sampling rate, and the lack of a shared temporal origin across eyes rules out methods that assume a common $t = 0$.

### 1.25 [medium] §1.2 Problem Statement

`01-introduction.tex:91` · GPTZero: AI · ai-tone, clarity

> Second, the underlying disease state is naturally \emph{multi-channel}: the binary lesion mask captures the GA lesion itself, while the surrounding ten retinal layer boundaries describe the retinal structure in which the atrophy is embedded.

**Issue.** 'naturally' is filler, the 'X ..., while Y ...' pair is balanced, and 'surrounding' is misleading because the layer boundaries do not surround the mask.

**Suggestion.**

> Second, the disease state is \emph{multi-channel}: a binary mask marks the GA lesion, and ten retinal layer boundaries describe the retinal structure in which the atrophy lies.

### 1.26 [low] §1.2 Problem Statement

`01-introduction.tex:95` · GPTZero: AI · clarity

> Both information sources are relevant because prognostic biomarkers documented in the clinical literature, such as RPE--Bruch's-membrane thickening \citep{Chu2022} and thinning of the outer retinal layers \citep{Vallino2024}, are not contained in the lesion mask alone.

**Issue.** The reason given justifies the layer channels, not 'both' sources. 'RPE' is used without being spelled out in Chapter 1.

**Suggestion.**

> The layer channels are relevant because prognostic biomarkers documented in the clinical literature, such as RPE--Bruch's-membrane thickening \citep{Chu2022} and thinning of the outer retinal layers \citep{Vallino2024}, are not contained in the lesion mask alone. (Spell out 'retinal pigment epithelium (RPE)' at this first use.)

### 1.27 [**HIGH**] §1.2 Problem Statement (covariates)

`01-introduction.tex:98` · GPTZero: AI · flow, clarity

> Third, every patient carries \emph{covariates}, in particular age and sex. Age is strongly associated with the risk of developing the disease (\S\ref{sec:introduction:motivation}), and the evidence on sex is mixed; whether either also helps to forecast where and how fast a lesion grows is not established, and is tested in this thesis.

**Issue.** The sentence promises a test that the rendered thesis does not report. The covariate subsection of Chapter 5 is inside \iffalse (05-experiments.tex l. 1094-1159), and §6.3 says their value 'is not settled'. A reader will look for the result and not find it. 'carries covariates' is jargon, and the semicolon chain joins separate points.

**Suggestion.**

> Third, each patient has \emph{covariates}, in particular age and sex. Age is strongly associated with the risk of developing the disease (\S\ref{sec:introduction:motivation}), and the evidence on sex is mixed. Whether either also helps to forecast where and how fast a lesion grows is not established. Both are given to every model as inputs, but their value is not settled in this thesis (\S\ref{sec:discussion:limitations}).

### 1.28 [low] §1.2 Problem Statement

`01-introduction.tex:104` · GPTZero: human · clarity

> Meeting these requirements is not only a question of the model itself but also of how the model is used.

**Issue.** 'requirements' re-labels what the previous paragraph called 'properties', which blurs the antecedent.

**Suggestion.**

> Handling these properties depends on the model and on how it is used.

### 1.29 [medium] §1.2 Problem Statement

`01-introduction.tex:107` · GPTZero: AI · clarity, ai-tone

> These properties have to come from a framework around the model, one that conditions the prediction on $\Delta t$ and rolls the state forward visit by visit.

**Issue.** 'These properties' now means the model's missing abilities (elapsed time, stepping), although the same word meant the data properties one paragraph earlier. The appended 'one that ...' apposition is a recurring tell.

**Suggestion.**

> Both abilities have to be supplied by a framework around the model that conditions the prediction on $\Delta t$ and advances the state from one visit to the next.

### 1.30 [medium] §1.2 Problem Statement (closing)

`01-introduction.tex:109` · GPTZero: AI · flow, ai-tone

> The next section motivates such a framework, which borrows several of its techniques from neural partial differential equation (PDE) solvers. Which model should sit inside it is a separate question.

**Issue.** The announcement does not match §1.3, which first argues that GA growth is local and PDE-like, an argument about the operator. The short closing sentence works as a cliff-hanger.

**Suggestion.**

> The next section motivates such a framework, which borrows several of its techniques from neural partial differential equation (PDE) solvers, and explains why the choice of the model inside it is treated as a separate question.

### 1.31 [medium] §1.3 Why Neural PDE Solvers?

`01-introduction.tex:119` · GPTZero: human · clarity

> \citet{Yehoshua2011} found that the enlargement rate of the square root of the lesion area does not depend on the baseline lesion size, which is what is expected if the radius of a GA lesion grows at a roughly constant rate while its enclosed area scales quadratically: writing $A(t)$ for the lesion area and $r(t)$ for an effective radius,

**Issue.** One sentence carries the finding, its interpretation, the notation and the equation, and continues with two more clauses after the equation (about 100 words). The reader loses the main clause.

**Suggestion.**

> \citet{Yehoshua2011} found that the enlargement rate of the square root of the lesion area does not depend on the baseline lesion size. This is what is expected if the radius of a GA lesion grows at a roughly constant rate while its enclosed area scales quadratically. With $A(t)$ the lesion area and $r(t)$ an effective radius, [equation and the following 'which is consistent ...' clause unchanged]

### 1.32 [medium] §1.3 Why Neural PDE Solvers?

`01-introduction.tex:135` · GPTZero: AI · ai-tone, tone

> This is the structural fingerprint of a system governed by a temporal partial differential equation with strong spatial localisation.

**Issue.** 'structural fingerprint' is a dramatic metaphor in a paragraph closer, and 'This' is vague. The PDE acronym is already introduced at l. 111.

**Suggestion.**

> Such behaviour is characteristic of a system governed by a temporal PDE with strong spatial localisation.

### 1.33 [medium] §1.3 Why Neural PDE Solvers?

`01-introduction.tex:140` · GPTZero: human · clarity

> GA growth is \emph{anisotropic}: lesions progress faster towards the retinal periphery than towards the fovea, peak progression rate occurs at approximately one millimetre from the foveal centre when the lesion grows foveally, and in eyes treated monthly with pegcetacoplan progression towards the fovea was slowed more than progression towards the periphery \citep{Singh2025}.

**Issue.** Three different kinds of finding share one list, with a tense shift. 'peak progression rate occurs ... when the lesion grows foveally' is hard to parse, and the treatment effect is a different kind of fact from natural growth.

**Suggestion.**

> GA growth is \emph{anisotropic}: lesions progress faster towards the retinal periphery than towards the fovea, and growth towards the fovea peaks at approximately one millimetre from the foveal centre \citep{Singh2025}. In eyes treated monthly with pegcetacoplan, progression towards the fovea was slowed more than progression towards the periphery \citep{Singh2025}.

### 1.34 [medium] §1.3 Why Neural PDE Solvers?

`01-introduction.tex:145` · GPTZero: AI · ai-tone, clarity

> The forward operator that maps the present state to the future state is therefore \emph{local}, but its reach must match the distance the front moves between two visits, which differs between directions --- properties that classical solvers build in explicitly through the size and shape of their stencils.

**Issue.** The em-dash appendage ('--- properties that ...') tacks a second idea onto an already long sentence, and 'stencil' is used without explanation in Chapter 1.

**Suggestion.**

> The forward operator that maps the present state to the future state is therefore \emph{local}, but its reach must match the distance the front moves between two visits, and this distance differs between directions. Classical solvers build such properties in explicitly through the size and shape of their stencils, the sets of neighbouring grid points that enter one update.

### 1.35 [low] §1.3 Why Neural PDE Solvers?

`01-introduction.tex:152` · GPTZero: AI · clarity

> Instead of discretising a known equation, they learn from data an operator that maps the current state of a system, and the time that elapses, to its next state.

**Issue.** The comma-enclosed 'and the time that elapses' interrupts the main clause.

**Suggestion.**

> Instead of discretising a known equation, they learn from data an operator that maps the current state of a system and the elapsed time to its next state.

### 1.36 [medium] §1.3 Why Neural PDE Solvers?

`01-introduction.tex:162` · GPTZero: AI · clarity, tone

> Which of them GA progression actually requires cannot be decided by testing a single architecture: if one model succeeds, the reason may be its operator, its size, or the setup around it. This thesis therefore separates the two.

**Issue.** 'the two' follows a list of three candidates (operator, size, setup), so it is unclear what is separated. 'actually' is filler.

**Suggestion.**

> Testing a single architecture cannot show which of these assumptions GA progression requires: if one model succeeds, the reason may be its operator, its size or the setup around it. This thesis therefore separates the operator from the setup.

### 1.37 [medium] §1.3 Why Neural PDE Solvers?

`01-introduction.tex:165` · GPTZero: AI · ai-tone

> The setup --- how elapsed time enters the prediction, how models are trained and how they are evaluated --- is fixed once, and the operator is the only part that changes.

**Issue.** An em-dash-enclosed tricolon splits subject and verb, and the closing clause restates the point in mirrored form.

**Suggestion.**

> The setup (how elapsed time enters the prediction, and how models are trained and evaluated) is fixed once, and only the operator changes.

### 1.38 [medium] §1.3 Why Neural PDE Solvers?

`01-introduction.tex:168` · GPTZero: AI · flow, clarity

> In contrast to clinical work based on cohort-level statistical atlases and time-to-conversion survival models \citep{Vogl2021} and on biomarker-based risk analyses \citep{Vallino2024}, every model in this comparison forecasts the lesion of an individual eye directly on the imaging state; the closest forecasts of this kind are discussed in Section~\ref{sec:background:related-work}.

**Issue.** This 55-word sentence repeats the contrast with earlier clinical work from §1.2 (l. 81-84) and interrupts the step from the framework/operator separation to the research question.

**Suggestion.**

> Consider moving the contrast to the end of the first paragraph of §1.2 (after l. 84), where earlier work is first contrasted, with 'every model in this comparison' changed to 'the models of this thesis' and the citations unchanged. Keep in §1.3 only: 'Forecasts of individual lesions closest to this work are discussed in Section~\ref{sec:background:related-work}.'

### 1.39 [medium] §1.3, research question

`01-introduction.tex:189` · GPTZero: AI · flow, ai-tone

> The first part concerns everything that surrounds the model: how irregular visit intervals enter the prediction, and how models are trained and evaluated. The second concerns the model itself, the operator that maps one visit to the next.

**Issue.** The two sentences form a mirror pair, and the first repeats almost verbatim the definition of the setup given a few lines earlier (l. 165-166).

**Suggestion.**

> The first part refers to the setup described above, and the second to the operator that maps one visit to the next.

### 1.40 [medium] §1.3, contributions paragraph

`01-introduction.tex:197` · GPTZero: AI · ai-tone, tone

> What the thesis delivers follows from this design. It provides a $\Delta t$-conditioned framework for irregular visit schedules in which operators from unrelated literatures can be compared on equal terms, and a controlled comparison of several operator classes on longitudinal OCT for GA.

**Issue.** A pseudo-cleft announcement in business register ('What the thesis delivers follows from ...') precedes the actual content.

**Suggestion.**

> The thesis contributes a $\Delta t$-conditioned framework for irregular visit schedules, in which operators from unrelated literatures can be compared on equal terms, and a controlled comparison of several operator classes on longitudinal OCT for GA.

### 1.41 [**HIGH**] §1.3, contributions paragraph

`01-introduction.tex:201` · GPTZero: AI · clarity, ai-tone

> It identifies physical reach at the scale of the lesion front and an explicit transport term as two independent routes to the same deficit, and it reports what did not help --- larger models, a higher integration order, a monotonic-growth penalty and a moving-mesh extension --- as results in their own right.

**Issue.** 'the same deficit' is never named in the chapter, and the 'moving-mesh extension' appears here without explanation. The em-dash-enclosed list and the idiom 'in their own right' add to the machine-like rhythm.

**Suggestion.**

> It identifies physical reach at the scale of the lesion front and an explicit transport term as two independent ways to address the same deficit, an update that reaches less far than the front moves between visits. It also reports as results what did not help: larger models, a higher integration order, a monotonic-growth penalty and an extension with an adaptive moving mesh.

### 1.42 [low] §1.4 Thesis Outline

`01-introduction.tex:219` · GPTZero: human · flow

> Chapter~\ref{ch:method} addresses the first part of the research question by developing the framework, and describes the models that fill its one free component. Chapter~\ref{ch:experiments} addresses the second part by comparing these models on equal terms.

**Issue.** This repeats l. 192-195 closely, and 'on equal terms' appears here for the third time in the chapter.

**Suggestion.**

> Chapter~\ref{ch:method} addresses the first part of the research question by developing the framework, and describes the models that fill its one free component. Chapter~\ref{ch:experiments} addresses the second part by comparing these models.

### 1.43 [low] §1.4 Thesis Outline

`01-introduction.tex:225` · GPTZero: human · clarity

> The appendix reports an additional experiment with an adaptive moving mesh.

**Issue.** The thesis has several appendices, so 'The appendix' is ambiguous. This sentence is also the reader's first explanation of the 'moving-mesh extension' named in the contributions paragraph.

**Suggestion.**

> Appendix~\ref{app:mm-pde} reports an additional experiment with an adaptive moving mesh.

