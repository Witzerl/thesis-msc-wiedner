# Micro feedback 5a: Ch. 5 Experiments, §5.1 Evaluation Protocol, §5.2 Arm Table

[← Overview](00-overview.md)

40 findings: 1 high, 17 medium, 22 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

§5.1 follows a sound order: why per-pixel error fails, then the metrics, then rollout and reporting, then the statistical instruments. Its register is consistent, with short, plain, impersonal declaratives and almost none of the usual buzzwords. The weaknesses are local. (1) The chapter has no opening of its own, because its two introductory sentences sit under the §5.1 heading and mix chapter scope ('This chapter') with section scope ('This section'). (2) The Dice score is used in §5.1.1 before §5.1.2 explains it. (3) §5.1.2 turns into a run of auxiliary definitions (growth-region Dice, horizon bins, border-touching eyes, collapse counter). The per-eye use of the growth-region Dice is stated twice, and the third item of 'Three consequences follow' is not a consequence. (4) The most serious defect is in §5.1.3: the start of the second of the two announced reasons sits on a LaTeX comment line (l. 163), so the PDF reads '...the luckiest one. eyes on which it would be reported.' A one-sentence orphan paragraph after Figure 5.1 then repeats the no-test-split point. (5) In §5.1.4 the reader cannot see how 0.036 and 0.016 follow from 0.0127, and the closer 'it can only widen a null' is cryptic. §5.2 has the right content but a loose paragraph order. The opening names the per-pixel floor as one of the two entries that set the scale, yet the floor is discussed only in the fifth paragraph after it. The T-FEN-vs-stencil comparison is split by seed across the long results paragraph. Figure 5.2 is referenced after Figure 5.3. The verdict that ingredients, not classes, separate the arms is stated at l. 389, again at l. 439-442, in the Table 5.1 caption, and once more in the first sentence of §5.3. In this range the flagged AI tone comes from structure (colon reveals ending in a verdict fragment, 'X, not Y' closers, pseudo-clefts, repeated restatement of the headline), not from vocabulary.

### Transitions

- Chapter opening (05-experiments.tex l. 18-21): the chapter introduction stands under \section{Evaluation Protocol}. Move the first two sentences above the section heading and keep only 'This section defines ...' under it. If a chapter map is added, it must name all seven sections (5.1-5.7), not only 5.1-5.3.
- §5.1.1 -> §5.1.2: 'a Dice score over the whole lesion' (l. 33) comes before the plain definition of Dice (l. 64-65). Move the definition to its first use and delete it at l. 64-65 (see finding l. 33).
- §5.1.2: the subsection runs through several definitions in a row (change-region Dice, growth-region Dice, horizon bins, border-touching, collapse counter). An orienting sentence after the change-region definition would help, e.g. 'Three auxiliary quantities are used alongside it: the growth-region Dice, a split of the eyes by contact with the edge of the imaged field, and a collapse counter.' Delete the repeated 'It is used by the per-eye statistical instrument' (l. 108).
- §5.1.2, l. 116: the border-touching definition opens with 'For the split reported in §5.2' before the reader knows why such a split exists. Open with its purpose (see finding).
- §5.1.3, l. 154-166: the paragraph announces 'two reasons', but the PDF shows only the first one, followed by the fragment 'eyes on which it would be reported.' The text 'Second, the highest epoch is chosen on the same validation' sits after the % on comment line 163. This is the most serious break in the range.
- §5.1.3, l. 206-208: the one-sentence paragraph after Figure 5.1 ('All experiments use ... every result is a validation result') is cut off from what precedes it and repeats l. 164-165. Move it to the start of §5.1.3 or to the chapter opening.
- §5.1.4, l. 217-228: a reader cannot see how 0.036 and 0.016 follow from 0.0127, and the paragraph ends on a cryptic aphorism ('it can only widen a null'). Add the one-clause rule (each threshold is about twice the standard deviation of the difference it applies to) and cut the closer.
- §5.2 paragraph order. Suggested sequence: (1) opening, then the per-pixel floor paragraph (l. 409-413), because the opening names the floor as one of the two entries that set the scale; (2) Table 5.1 with a first pointer to Figure 5.2; (3) the comparisons of the top three (l. 367-382), with the seed-7 T-FEN-vs-stencil sentence moved up next to its seed-42 counterpart and followed directly by the T-FEN form note (l. 404-407); (4) fold variance, Figure 5.3 and the best-fold column as one block (l. 415-447); (5) the border/interior split (l. 394-399); (6) the Runge-Kutta and cost pointers (l. 455-457); (7) end on the 'not a ranking / ingredients' bridge to §5.3.
- §5.2 -> §5.3: the verdict appears at l. 389-390 ('not their class but the ingredients'), at l. 439-442 ('not a leaderboard ... which components ... move the metric'), in the Table 5.1 caption ('adjacent arms mostly differ by less than the noise floor') and again in the first sentence of §5.3 (l. 463, 'within about 0.04 of each other'). State it once, at the end of §5.2. §5.3 can then open directly with 'This section compares operators that differ in one property only ...'.
- §5.2, l. 386-388: 'the reach deficit' first appears here as a term. §4.3.3 has prepared it only as 'the reach problem', and §5.3.5 explains it. A short gloss in place would help (see finding).
- §5.2, l. 449-453: Figure 5.2 (rollouts) is first referenced at the end of the section, after Figure 5.3. Reference it right after Table 5.1 so that text and figure numbering follow the same order (see added finding at l. 265).
- Figure 5.1(b) shows the objective ablation, which is discussed only in §5.4.2. The caption already points there. One clause in the §5.1.3 text ('panel (b) is discussed in §5.4.2') would stop a reader from looking for its discussion in §5.1.

### Recurring tells in this part

- Colon reveal ending in a verdict fragment or appended appositive, e.g. '...(46/75, $t = 2.2$): at the floor on one instrument and under it on the other, a tie.' and '...close to its seed-42 value: a small but consistent lead, at the noise level.' Also 'are easy to confuse: ...' and 'Noise affects nulls and effects differently: it can only widen a null.' Roughly 5-8 times in the range (about 25 colons in total, most of them legitimate).
- Antithesis closers 'X, not Y' / 'not X but Y' that restate the paragraph, e.g. 'would therefore measure calibration, not prediction', 'This is a limitation of the logging, not a choice of metric.', 'not their class but the ingredients they carry', 'the table is not a leaderboard'. About 5 times.
- Pseudo-cleft or cleft sentences, e.g. 'The rollout evaluation is the procedure every reported number comes from.', 'What separates the arms is therefore ...', 'What it provides is the evidence for ...'. About 3 times.
- Emphatic 'at all' (on the author's own list), e.g. 'predicts no change at all' (l. 27-28, l. 411) and 'predicting no progression at all' (l. 30-31). 3 times.
- Personified abstractions and metaphors, e.g. 'Full-mask Dice is therefore almost blind to progression', 'it asks whether the model predicts change', 'This licenses reading ...', 'the forecast reaches further', 'Only two entries fix the scale'. About 5 times.
- Count announcements stacked in §5.1: 'Three consequences follow. First ... Second ... Third', 'Two thresholds follow from it', 'Two evaluation procedures', 'for two reasons. First ... Second', plus 'Two Statistical Instruments' in the heading. About 5-6 times. Each is acceptable on its own; together they give a template-like rhythm.
- Consequence chains closing sentences with 'therefore' (5 times in the rendered range) or ', so ...' (about 10), e.g. 'is therefore a strong per-pixel baseline', 'Full-mask Dice is therefore ...', 'What separates the arms is therefore ...'.
- Formulaic result sentences 'The X against the Y gives $\Delta = ...$' / 'reads', about 6-7 times in §5.2. Technically correct; varying them with 'is higher by' or 'lies at' would read less mechanically.
- The headline verdict ('within about 0.04', 'ingredients, not class', 'not a leaderboard', 'adjacent arms mostly differ by less than the noise floor') is restated in successive paragraphs, the table caption and the next section's opening. 4 times.

## Findings

### 5a.1 [low] §5.1 Evaluation Protocol (chapter opening)

`05-experiments.tex:18` · GPTZero: human · flow, clarity

> This chapter answers the second part of the research question: what kind of operator the framework of Chapter~\ref{ch:method} needs. Many operators are run through the same slot under identical conditions. This section defines how they are scored and how two scores are compared.

**Issue.** The chapter introduction sits under the \section{Evaluation Protocol} heading, so the chapter has no opening of its own, and one paragraph mixes chapter scope ('This chapter') with section scope ('This section'). 'Many operators' is vague.

**Suggestion.**

> Move the first two sentences above \section{Evaluation Protocol} so that they open the chapter: "This chapter answers the second part of the research question: what kind of operator the framework of Chapter~\ref{ch:method} needs. The operators of~\S\ref{sec:method:family} are run through the same slot under identical conditions." Under the section heading keep: "This section defines how the operators are scored and how two scores are compared."

### 5a.2 [low] §5.1.1 Why Not Per-Pixel Error

`05-experiments.tex:27` · GPTZero: AI · tone, ai-tone

> Persistence, which predicts no change at all, is therefore a strong per-pixel baseline. A per-pixel mean squared error or root mean squared error (RMSE) is dominated by the static pixels, and a model can reach a low per-pixel error while predicting no progression at all.

**Issue.** The emphatic 'at all' (on the author's list of fillers) appears twice within two sentences.

**Suggestion.**

> Persistence, the prediction that nothing changes, is therefore a strong per-pixel baseline. A per-pixel mean squared error or root mean squared error (RMSE) is dominated by the static pixels, so a model can reach a low per-pixel error without predicting any progression.

### 5a.3 [medium] §5.1.1 Why Not Per-Pixel Error

`05-experiments.tex:33` · GPTZero: AI · flow, clarity, tone

> The same holds for a Dice score over the whole lesion. The static interior of the lesion dominates it, so persistence already reaches a full-mask Dice of about 0.87. Full-mask Dice is therefore almost blind to progression.

**Issue.** The Dice score is used here before it is explained (the plain definition only comes at l. 64-65), against the author's rule that every metric is explained on first use. The closing 'therefore ... almost blind' sentence only restates the previous one, with a metaphor.

**Suggestion.**

> The same holds for a Dice score over the whole lesion. The Dice score measures the overlap of two regions: it is 1 when they coincide and 0 when they share no pixel. Over the whole lesion it is dominated by the static interior, so persistence already reaches a full-mask Dice of about 0.87, and the score barely responds to progression. (Then delete the definition sentence at l. 64-65, 'A Dice score measures the overlap ... no pixel.')

### 5a.4 [medium] §5.1.1 Why Not Per-Pixel Error

`05-experiments.tex:37` · GPTZero: AI · flow, clarity

> Raw errors are also not compared across architectures. The clinical metrics are computed on the thresholded mask. The dense operators, such as the U-Net and the Fourier Neural Operator, decalibrate their raw mask regression under autoregressive rollout much more than the graph network does: the late rollout mask RMSE of the U-Net is roughly twice that of the graph network, while its thresholded metrics are higher.

**Issue.** The second sentence stands alone, and its causal link to the first and third is left for the reader to supply. 'Decalibrate their raw mask regression' is not explained in plain words. 'Late rollout mask RMSE' can be read as RMSE at late rollout steps; if the late-epoch mean is meant (defined only in §5.1.3), 'late-epoch' would remove the ambiguity.

**Suggestion.**

> Raw errors are also not compared across architectures, because the clinical metrics are computed on the thresholded mask. Under autoregressive rollout, the dense operators, such as the U-Net and the Fourier Neural Operator, decalibrate their raw mask regression much more than the graph network does: the late rollout mask RMSE of the U-Net is roughly twice that of the graph network, while its thresholded metrics are higher. (Optionally add a short gloss of 'decalibrate' in the author's own words, and write 'late-epoch' if that is what 'late' means.)

### 5a.5 [low] §5.1.1 Why Not Per-Pixel Error

`05-experiments.tex:44` · GPTZero: AI · clarity

> The soft-Dice loss adds a separate, known stretch to the raw mask values (\S\ref{sec:method:training:loss}).

**Issue.** 'A separate, known stretch' leaves the reader asking: separate from what, and known from where? §4.5.1 describes the effect as a stretch of the raw mask regression about the threshold.

**Suggestion.**

> In addition, the soft-Dice term of the loss stretches the raw mask values about the threshold (\S\ref{sec:method:training:loss}).

### 5a.6 [medium] §5.1.2 Metrics

`05-experiments.tex:51` · GPTZero: AI · clarity

> All predicted and ground-truth masks are binarised at the physical threshold of 0.5, mapped into normalised space in the same way as in the loss.

**Issue.** Dangling participle: grammatically 'mapped' attaches to the masks, but it is the threshold that is mapped into normalised space (§4.5.1: 'the physical threshold of 0.5 mapped into normalised space').

**Suggestion.**

> All predicted and ground-truth masks are binarised at the physical threshold of 0.5, which is mapped into normalised space in the same way as in the loss.

### 5a.7 [low] §5.1.2 Metrics

`05-experiments.tex:53` · GPTZero: AI · clarity

> Let $b$ be the thresholded mask at the baseline visit, the first visit of the rollout, $p$ the thresholded prediction at the anchor and $y$ the thresholded ground truth at the anchor.

**Issue.** The appositive 'the first visit of the rollout' sits inside a comma-separated list of definitions, so it reads like a further list item.

**Suggestion.**

> Let $b$ be the thresholded mask at the baseline visit (the first visit of the rollout), $p$ the thresholded prediction at the anchor and $y$ the thresholded ground truth at the anchor.

### 5a.8 [low] §5.1.2 Metrics

`05-experiments.tex:65` · GPTZero: AI · ai-tone, tone

> Applied to the change regions, it asks whether the model predicts change where change actually happened, and it ignores the large part of the lesion that stays the same.

**Issue.** The metric is personified ('it asks') and the sentence contains the filler 'actually'.

**Suggestion.**

> Applied to the change regions, it measures how well the predicted change overlaps the change that occurred; the large part of the lesion that stays the same does not enter it.

### 5a.9 [low] §5.1.2 Metrics

`05-experiments.tex:69` · GPTZero: AI · tone

> First, persistence predicts no change, so its score is 0 by construction, and every positive value is lift over "no progression".

**Issue.** 'Lift' is marketing/ML jargon and is not explained.

**Suggestion.**

> First, persistence predicts no change, so its score is 0 by construction, and every positive value is an improvement over predicting no progression.

### 5a.10 [medium] §5.1.2 Metrics

`05-experiments.tex:74` · GPTZero: human · flow, clarity

> Third, it is not the growth-region Dice of \citet{Mai2024}, which this chapter also uses.

**Issue.** The paragraph announces 'Three consequences follow', but the third item is not a consequence of the definition. It is a distinction from another metric, which brings a second metric into a numbered list.

**Suggestion.**

> Change l. 69 to "Two consequences follow." and start a new paragraph with the third item: "The change-region Dice differs from the growth-region Dice of \citet{Mai2024}, which this chapter also uses."

### 5a.11 [low] §5.1.2 Metrics

`05-experiments.tex:78` · GPTZero: AI · tone, ai-tone, clarity

> Both have a persistence floor of 0 and are easy to confuse: Table~\ref{tab:experiments:arms} and all fold-paired values use the change-region Dice, while the per-eye instrument uses the growth-region Dice (\S\ref{sec:experiments:protocol:stats}). The change-region Dice is also the model-selection metric.

**Issue.** A colon reveal follows the informal 'are easy to confuse', and model selection is added as an afterthought sentence.

**Suggestion.**

> Both have a persistence floor of 0 and are easily confused. Table~\ref{tab:experiments:arms}, all fold-paired values and the model selection use the change-region Dice; the per-eye instrument (\S\ref{sec:experiments:protocol:stats}) uses the growth-region Dice.

### 5a.12 [low] §5.1.2 Metrics

`05-experiments.tex:108` · GPTZero: human · flow

> It is used by the per-eye statistical instrument (\S\ref{sec:experiments:protocol:stats}).

**Issue.** This repeats the statement made at the end of the preceding paragraph (l. 80-81).

**Suggestion.**

> Delete this sentence.

### 5a.13 [low] §5.1.2 Metrics

`05-experiments.tex:111` · GPTZero: AI · clarity, ai-tone

> These horizon bins show how the prediction degrades as the forecast reaches further than the one-year anchor, and they are the bins in which \citet{Mai2024} report the same metric.

**Issue.** Two unrelated points are joined by 'and', and 'the forecast reaches further' personifies the forecast.

**Suggestion.**

> These horizon bins show how the prediction degrades beyond the one-year anchor. \citet{Mai2024} report the same metric in the same bins.

### 5a.14 [medium] §5.1.2 Metrics

`05-experiments.tex:116` · GPTZero: AI · flow, clarity

> For the split reported in~\S\ref{sec:experiments:main-results}, an eye counts as border-touching when its true lesion at the anchor touches the edge of the imaged field: the outermost ring of the crop or, for padded visits, the edge of the zero padding, because there the true edge of the field lies inside the crop (\S\ref{sec:data:spatial}). Of the 75 eyes, 21 touch it.

**Issue.** The paragraph refers to 'the split' before the reader knows that a split exists or what it is for. A single sentence then carries a colon, an embedded 'or, for padded visits,' and a 'because there' clause.

**Suggestion.**

> Because growth across the edge of the imaged field is censored (\S\ref{sec:data:spatial}), the eyes are also split by contact with that edge; the split is reported in~\S\ref{sec:experiments:main-results}. An eye counts as border-touching when its true lesion at the anchor touches the edge of the imaged field. This edge is the outermost ring of the crop or, for padded visits, the edge of the zero padding, since for those visits the true edge of the field lies inside the crop. Of the 75 eyes, 21 are border-touching.

### 5a.15 [low] §5.1.3 Rollout and Reporting

`05-experiments.tex:138` · GPTZero: AI · clarity, ai-tone

> It isolates the accuracy of a single step from the drift of a rollout. The rollout evaluation is the procedure every reported number comes from.

**Issue.** The second sentence is a pseudo-cleft ending on a preposition; the direct form is shorter.

**Suggestion.**

> Keep the first sentence and replace the second with: "Every reported number comes from the rollout evaluation."

### 5a.16 [low] §5.1.3 Rollout and Reporting

`05-experiments.tex:146` · GPTZero: AI · clarity

> For a few eyes this step lies beyond one year, where the true change region is larger; this is accepted, as \citet{Mai2024} also score every follow-up visit by its time since baseline rather than at a fixed horizon.

**Issue.** A semicolon plus 'this is accepted, as' plus 'rather than' packs the observation and its justification into one hard-to-parse sentence.

**Suggestion.**

> For a few eyes this step lies beyond one year, where the true change region is larger. This is accepted because \citet{Mai2024} also score every follow-up visit by its time since baseline and not at a fixed horizon.

### 5a.17 [low] §5.1.3 Rollout and Reporting

`05-experiments.tex:154` · GPTZero: AI · clarity

> The checkpoint kept as the best one is the epoch with the highest change-region Dice at the anchor.

**Issue.** A checkpoint is equated with an epoch.

**Suggestion.**

> The checkpoint that is kept is the one from the epoch with the highest change-region Dice at the anchor.

### 5a.18 [medium] §5.1.3 Rollout and Reporting

`05-experiments.tex:156` · GPTZero: AI · tone, clarity

> First, the metric is noisy: with 12 to 20 validation eyes per fold, it still fluctuates from epoch to epoch once training has levelled off, with a standard deviation of about 0.01 to 0.05 within one run (Figure~\ref{fig:experiments:curves}a), so the highest epoch is mostly the luckiest one.

**Issue.** One long colon-and-'so' sentence ends on a colloquial phrase ('the luckiest one').

**Suggestion.**

> First, the metric is noisy. With 12 to 20 validation eyes per fold, it still fluctuates from epoch to epoch once training has levelled off, with a standard deviation of about 0.01 to 0.05 within one run (Figure~\ref{fig:experiments:curves}a). As a result, the highest epoch is mostly the one with the most favourable noise.

### 5a.19 [**HIGH**] §5.1.3 Rollout and Reporting

`05-experiments.tex:163` · GPTZero: AI · flow, clarity

> Second, the highest epoch is chosen on the same validation eyes on which it would be reported. There is no separate test split (\S\ref{sec:data:splits}), so a best-epoch value is biased upwards, and the more so the noisier the metric.

**Issue.** The words 'Second, the highest epoch is chosen on the same validation' stand on line 163 after the % of a LaTeX comment and are not rendered. The PDF reads '...the luckiest one. eyes on which it would be reported.', so the second of the two announced reasons is lost. The closing 'and the more so the noisier the metric' is also overly compressed.

**Suggestion.**

> Put a line break after the % comment (or move the comment below the paragraph) so that the text is rendered: "Second, the highest epoch is chosen on the same validation eyes on which it would be reported. There is no separate test split (\S\ref{sec:data:splits}), so a best-epoch value is biased upwards, and the bias grows with the noise of the metric."

### 5a.20 [low] §5.1.3 Rollout and Reporting

`05-experiments.tex:168` · GPTZero: AI · clarity

> The window is fixed in advance and the same for every arm, so no choice is made on the validation data, and averaging twenty epochs damps the epoch-to-epoch noise. The window starts at epoch 10 because by then the learning rate has been reduced once, from epoch 5 on (\S\ref{sec:method:training}), and the fast early phase of training is over; a second reduction takes effect from epoch 20, inside the window.

**Issue.** In the first sentence an 'so ..., and ...' chain joins two separate justifications. The second sentence interrupts itself with 'from epoch 5 on' and then adds a semicolon tail.

**Suggestion.**

> The window is fixed in advance and is the same for every arm, so no choice is made on the validation data. Averaging twenty epochs also damps the epoch-to-epoch noise. The window starts at epoch 10 because by then the learning rate has been reduced once (from epoch 5; \S\ref{sec:method:training}) and the fast early phase of training is over. A second reduction takes effect from epoch 20, inside the window.

### 5a.21 [low] Figure 5.1 caption

`05-experiments.tex:189` · GPTZero: AI · clarity

> the dark segments are the late-epoch means of the five folds, ended by the fold markers of Figure~\ref{fig:experiments:arms-folds}.

**Issue.** 'Ended by the fold markers of Figure 5.3' is cryptic: the reader has to infer that each segment ends in the symbol that identifies its fold.

**Suggestion.**

> the dark segments are the late-epoch means of the five folds, each ending in the marker that identifies the fold in Figure~\ref{fig:experiments:arms-folds}.

### 5a.22 [low] §5.1.3 Rollout and Reporting

`05-experiments.tex:206` · GPTZero: human · flow

> All experiments use the patient-level five-fold cross-validation of~\S\ref{sec:data:splits}, which has no test split; every result is a validation result.

**Issue.** This one-sentence paragraph after Figure 5.1 is cut off from the reporting discussion and repeats the no-test-split point already made at l. 164-165.

**Suggestion.**

> Move it to the start of \S\ref{sec:experiments:protocol:rollout} (or to the chapter opening): "All experiments use the patient-level five-fold cross-validation of~\S\ref{sec:data:splits}. It has no test split, so every result is a validation result." The best-epoch paragraph can then refer back to it ('As there is no separate test split, ...').

### 5a.23 [low] §5.1.4 Two Statistical Instruments and the Noise Floor

`05-experiments.tex:214` · GPTZero: AI · clarity

> Seven pairs of runs with the same configuration on the same fold, two with the same seed and five with different seeds, give a per-run standard deviation of about 0.0127 for the late-epoch mean of the change-region Dice.

**Issue.** The long subject with an embedded appositive ('two with the same seed and five with different seeds') delays the verb and the result.

**Suggestion.**

> The run-to-run spread was measured on seven pairs of runs with the same configuration on the same fold, two pairs with the same seed and five with different seeds. They give a per-run standard deviation of about 0.0127 for the late-epoch mean of the change-region Dice.

### 5a.24 [medium] §5.1.4 Two Statistical Instruments and the Noise Floor

`05-experiments.tex:217` · GPTZero: AI · flow, clarity

> Two thresholds follow from it. A difference measured on a single fold must exceed 0.036 to count as an effect, and a difference of five-fold paired means must exceed 0.016.

**Issue.** 'Follow from it' asserts a derivation the reader cannot see, so the jump from 0.0127 to 0.036 and 0.016 looks arbitrary.

**Suggestion.**

> Two thresholds follow from it, each about twice the standard deviation of the difference it applies to: a difference measured on a single fold must exceed 0.036 to count as an effect, and a difference of five-fold paired means must exceed 0.016.

### 5a.25 [medium] §5.1.4 Two Statistical Instruments and the Noise Floor

`05-experiments.tex:227` · GPTZero: AI · clarity, ai-tone

> Noise affects nulls and effects differently: it can only widen a null.

**Issue.** An aphoristic paragraph closer (the mirror pair 'nulls and effects' plus a colon reveal) whose meaning is unclear: 'widen a null' is not a defined notion, and a reader cannot tell what follows for the U-Net comparisons.

**Suggestion.**

> Delete the sentence. If a statement is wanted, give the consequence plainly in the author's own words (for example, that a wider floor makes a null result less informative), after confirming that this is the intended meaning.

### 5a.26 [medium] §5.1.4 Two Statistical Instruments and the Noise Floor

`05-experiments.tex:233` · GPTZero: AI · clarity

> The first is the fold-paired mean, written $\Delta = x \pm y$~SE ($k$/5): the mean over the five folds of the per-fold difference, with its between-fold standard error, where $k$ is the number of folds on which the difference has the same sign as the mean.

**Issue.** One sentence carries the notation, a colon, a 'with' phrase and a 'where' clause, and it never says which symbol is which. The second instrument's 'Here $m$ is ...' gives a clearer pattern.

**Suggestion.**

> The first is the fold-paired mean, written $\Delta = x \pm y$~SE ($k$/5). Here $x$ is the mean over the five folds of the per-fold difference, $y$ its between-fold standard error and $k$ the number of folds on which the difference has the same sign as the mean.

### 5a.27 [medium] §5.1.4 Two Statistical Instruments and the Noise Floor

`05-experiments.tex:247` · GPTZero: AI · ai-tone

> This instrument uses the growth-region Dice rather than the headline metric, because the change-region Dice was logged per run as a cohort mean only, without per-eye values across epochs. This is a limitation of the logging, not a choice of metric.

**Issue.** The paragraph ends on an 'X, not Y' antithesis closer that restates the preceding sentence.

**Suggestion.**

> This instrument uses the growth-region Dice instead of the headline metric only because of a limitation of the logging: the change-region Dice was recorded per run as a cohort mean, without per-eye values across epochs.

### 5a.28 [low] §5.1.4 Two Statistical Instruments and the Noise Floor

`05-experiments.tex:253` · GPTZero: human · ai-tone

> A result is established --- it \emph{graduates} --- only when both agree.

**Issue.** An em-dash aside introduces a coined term; a parenthesis is the quieter academic form.

**Suggestion.**

> A result counts as established (it \emph{graduates}) only when both agree.

### 5a.29 [medium] §5.2 The Arm Table

`05-experiments.tex:263` · GPTZero: AI · ai-tone, tone

> Every architecture in the survey is a peer arm; none is a baseline to be beaten. Only two entries fix the scale: persistence, which scores 0 by construction, and the per-pixel floor.

**Issue.** A semicolon-joined antithesis ('peer arm; none is a baseline to be beaten'). 'To be beaten' adds a competitive tone the thesis otherwise avoids, and 'fix the scale' is a mild metaphor.

**Suggestion.**

> All architectures in the survey are compared as peers, and none serves as a baseline. Only two entries set the scale: persistence, which scores 0 by construction, and the per-pixel floor.

### 5a.30 [low] §5.2 The Arm Table

`05-experiments.tex:265` · GPTZero: AI · flow *(added in verification)*

> Table~\ref{tab:experiments:arms} lists every arm on the headline metric.

**Issue.** Figure 5.2 (rollouts) is placed before Figure 5.3 but is first referenced at the end of §5.2 (l. 449), after Figure 5.3 (l. 419). The text therefore refers to the figures out of order.

**Suggestion.**

> Table~\ref{tab:experiments:arms} lists every arm on the headline metric, and Figure~\ref{fig:experiments:rollout} shows the rollouts of five of them for one validation eye. At l. 449, then begin: "Figure~\ref{fig:experiments:rollout} illustrates what the change-region Dice scores: ..."

### 5a.31 [low] Figure 5.2 caption

`05-experiments.tex:354` · GPTZero: AI · clarity

> Model panels show in light grey the predicted lesion that coincides with the baseline lesion and code the change against the baseline: predicted and true in blue, predicted only in orange, true only (missed) in purple; in the baseline column they show the input mask.

**Issue.** The light grey shows the part of the prediction that coincides with the baseline lesion, not 'the predicted lesion'. 'Code' as a verb is ambiguous.

**Suggestion.**

> Model panels show in light grey the part of the predicted lesion that coincides with the baseline lesion and colour the change against the baseline: predicted and true in blue, predicted only in orange, true only (missed) in purple; in the baseline column they show the input mask.

### 5a.32 [medium] §5.2 The Arm Table

`05-experiments.tex:368` · GPTZero: AI · flow, ai-tone

> The T-FEN against the dilated-stencil graph network gives $\Delta = +0.0170 \pm 0.0085$~SE (4/5) and per eye $+0.0136 \pm 0.0062$ (46/75, $t = 2.2$): at the floor on one instrument and under it on the other, a tie.

**Issue.** The verdict is appended after a colon as a fragment ('..., a tie'). The seed-7 result for the same pair comes only at the end of the paragraph (l. 380-382), after the U-Net comparisons, and is again closed with a colon fragment ('...: a small but consistent lead, at the noise level'). The reader has to piece the comparison together.

**Suggestion.**

> "The T-FEN against the dilated-stencil graph network gives $\Delta = +0.0170 \pm 0.0085$~SE (4/5) and per eye $+0.0136 \pm 0.0062$ (46/75, $t = 2.2$). This lies at the floor on one instrument and under it on the other and is read as a tie. At seed 7 the T-FEN is higher by $+0.0165 \pm 0.0021$~SE (5/5) and per eye $+0.0152 \pm 0.0048$ (49/75, $t = 3.1$), close to its seed-42 value; the lead is small but consistent, and at the noise level." Then delete the sentence at l. 380-382.

### 5a.33 [low] §5.2 The Arm Table

`05-experiments.tex:375` · GPTZero: AI · clarity

> The T-FEN against the U-Net gives $\Delta = +0.0383 \pm 0.0134$~SE (5/5) and per eye $+0.0383 \pm 0.0075$ (51/75, $t = 5.1$) at seed 42, and $+0.0246 \pm 0.0073$~SE (5/5) and per eye $+0.0255 \pm 0.0074$ (52/75, $t = 3.4$) at seed 7. The lead is smaller at the second seed but present on every fold at both, so the T-FEN lies above the U-Net.

**Issue.** One sentence carries four statistics, and each seed label comes only at the end of its half. 'At both' is missing its noun.

**Suggestion.**

> The T-FEN against the U-Net gives $\Delta = +0.0383 \pm 0.0134$~SE (5/5) and per eye $+0.0383 \pm 0.0075$ (51/75, $t = 5.1$) at seed 42. At seed 7 it gives $+0.0246 \pm 0.0073$~SE (5/5) and per eye $+0.0255 \pm 0.0074$ (52/75, $t = 3.4$). The lead is smaller at the second seed but present on every fold at both seeds, so the T-FEN lies above the U-Net.

### 5a.34 [medium] §5.2 The Arm Table

`05-experiments.tex:386` · GPTZero: human · flow, clarity

> The two highest arms are the two that carry a remedy for the reach deficit taken up in~\S\ref{sec:experiments:ingredients:convergence}: the transport term and the dilated stencil.

**Issue.** 'The reach deficit' is used as a known term, but §4.3.3 prepared it only as 'the reach problem', and §5.3.5 explains it. The sentence then serves as the premise of the section's verdict.

**Suggestion.**

> The two highest arms are the two that carry a remedy for the reach deficit, the mismatch between how far one update can see and how far the lesion front moves between two visits (\S\ref{sec:experiments:ingredients:convergence}): the transport term and the dilated stencil.

### 5a.35 [medium] §5.2 The Arm Table

`05-experiments.tex:389` · GPTZero: AI · ai-tone, flow

> What separates the arms is therefore not their class but the ingredients they carry.

**Issue.** This is a pseudo-cleft with a 'not X but Y' aphoristic close. The same verdict is restated at l. 439-442, in the Table 5.1 caption and in the first sentence of §5.3.

**Suggestion.**

> The arms are therefore separated by the ingredients they carry and not by their architecture class; \S\ref{sec:experiments:ingredients} measures these ingredients one at a time. (Then cut the restatement at l. 439-442; see that finding.)

### 5a.36 [medium] §5.2 The Arm Table

`05-experiments.tex:394` · GPTZero: AI · clarity, flow

> The fixed crop censors growth across the window edge (\S\ref{sec:data:spatial}). Of the 75 eyes, 21 have a lesion that touches the crop border at the one-year anchor and 54 do not.

**Issue.** 'Touches the crop border' does not match the definition in §5.1.2 ('edge of the imaged field', which includes the padding edge), so a reader may think these are two different criteria. The paragraph also interrupts the T-FEN discussion.

**Suggestion.**

> The fixed crop censors growth across the window edge (\S\ref{sec:data:spatial}). Of the 75 eyes, 21 are border-touching in the sense of~\S\ref{sec:experiments:protocol:metrics} and 54 are interior. (Move the paragraph after the fold-variance block; see flow notes.)

### 5a.37 [medium] §5.2 The Arm Table

`05-experiments.tex:409` · GPTZero: human · tone, ai-tone, flow

> The per-pixel floor reads exactly 0.0000 on all five folds, identical to persistence; its collapse counter flags every validation eye as unchanged from baseline. A model without spatial context predicts no change at all. This licenses reading every point of change-region Dice in the table as coming from spatial context.

**Issue.** The paragraph contains the emphatic 'at all' and a personified, legalistic 'This licenses reading ...'. It also comes five paragraphs after the opening that names the per-pixel floor as one of the two entries that set the scale.

**Suggestion.**

> Move the paragraph directly after the opening paragraph of §5.2 and write: "The per-pixel floor reads exactly 0.0000 on all five folds, identical to persistence, and its collapse counter flags every validation eye as unchanged from baseline. A model without spatial context predicts no change, so every point of change-region Dice in the table can be attributed to spatial context."

### 5a.38 [low] §5.2 The Arm Table

`05-experiments.tex:416` · GPTZero: AI · ai-tone, clarity

> The standard deviations in the table are between-fold deviations and are much larger than the replicate floor, which is why differences are always read fold-paired.

**Issue.** '..., which is why ...' is a cleft-like causal tail.

**Suggestion.**

> Because the standard deviations in the table are between-fold deviations and much larger than the replicate floor, differences are always read fold-paired.

### 5a.39 [medium] §5.2 The Arm Table

`05-experiments.tex:439` · GPTZero: AI · ai-tone, tone, flow

> Adjacent rows mostly lie within the floor of each other, so the table is not a leaderboard. What it provides is the evidence for which components of an operator move the metric, which \S\ref{sec:experiments:ingredients} examines one at a time.

**Issue.** 'Leaderboard' is informal, and 'What it provides is ...' is a pseudo-cleft. 'Lie within the floor of each other' is awkward. Both sentences restate the caption and l. 389-390.

**Suggestion.**

> Adjacent rows mostly differ by less than the noise floor, so the order of the rows should not be read as a ranking. (Drop the second sentence if l. 389 carries the pointer to \S\ref{sec:experiments:ingredients}.)

### 5a.40 [low] §5.2 The Arm Table

`05-experiments.tex:444` · GPTZero: AI · flow, clarity

> The best-fold column shows how far a single fold can lie above the mean. For every arm except the two FNO arms without a local path, the best fold is fold 2, so the column mostly reflects the spread between folds rather than a separate result.

**Issue.** This repeats 'fold 2 is the highest fold for almost every arm' from l. 421-422, and 'rather than a separate result' is vague.

**Suggestion.**

> The best-fold column shows how far a single fold can lie above the mean. Since the best fold is fold 2 for every arm except the two FNO arms without a local path, the column adds little beyond the spread between folds. (Then drop 'and fold 2 is the highest fold for almost every arm' at l. 421-422.)

