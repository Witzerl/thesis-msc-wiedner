# Micro feedback A: Appendices A-F (dataset details, derivations, hyperparameters, rollouts, ablation details, code structure)

[← Overview](00-overview.md)

14 findings: 0 high, 8 medium, 6 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

Appendices A-F are mostly figures and tables with little running prose. Where prose exists, it is plain and declarative and largely matches the author's unflagged voice. GPTZero judged one passage human ("Most eyes were seen six or seven times, ...") that reads much like the flagged captions, so most flags here come from the enumerative style of captions, not from real AI-isms. The weak points are structural. Appendices B and C appear as empty chapters (heading only) between A and D. Appendix E is titled "Ablation Details" but holds a border/interior split, growth-speed measures and a two-seed replication table, none of which is an ablation. It also has no lead-in text at all, so the reader meets three tables without being told what they support. Table E.3, Figure A.2 and Appendix F are never referenced from the main text, so a reader of Chapters 3-5 cannot know they exist. Terms also drift for the same concept: "border of the crop", "border of the fixed crop" and "border of the imaged field" all appear, while §5.1.2 defines "edge of the imaged field". The arm names in Tables E.1/E.2 differ from those in Table 5.1 and Table F.2. Appendix A and the Appendix D paragraph read well apart from one repetition and one undefined referent ("the two failure cases"). The register is consistently objective. The few tone problems are small: one idiom ("in one piece") and dense "of the ... of the" noun chains in the captions.

### Transitions

- 91-appendix.tex l. 74-87 (Appendices B and C): both chapters contain only a heading (their content is still a LaTeX TODO), so the reader passes two empty chapters between A and D. Nothing in the main text refers to app:derivations or app:hyperparameters, so either fill them as planned or drop the two headings before submission; dropping them breaks no \ref.
- 91-appendix.tex l. 139-145 (start of Appendix E): the chapter heading is followed directly by a section heading and a table, with no sentence saying what the three tables are for. One lead-in paragraph under the chapter heading is enough (see the Appendix E finding, which also gives Table E.3 its first reference); a one-line orientation under each section is optional.
- Unreferenced appendix material: Table~\ref{tab:appendix:seeds}, Figure~\ref{fig:appendix:crop} and Appendix~\ref{app:code} are not cited anywhere in Chapters 1-7. Add pointers where a reader needs them. In \S5.1.4 (05-experiments.tex l. 255-256), extend the seed sentence: "All numbers are for seed 42 unless they are marked as seed 7 or seed-pooled; Table~\ref{tab:appendix:seeds} collects the main comparisons at both seeds." After the censoring census in \S3.3 (03-data.tex ~l. 219), add "(Figure~\ref{fig:appendix:crop})". In \S4.6 Implementation, add "(Appendix~\ref{app:code})".
- Table E.3 vs \S5.1.4: the caption counts the folds/eyes "on which the first arm is higher", but \S5.1.4 (05-experiments.tex l. 236, 245) defines k and m as the number with "the same sign as the mean". A reader who cross-checks a negative row (e.g. FNO - U-Net, 1/5) will find the two definitions disagree. This is already tracked as a TODO in NOTES.md; resolve it before readers reach this table.
- Appendix D (l. 98-106) and the Figure D.1 caption (l. 119-133) repeat the four selection rules almost word for word. One option is to keep the full rules in the self-contained caption, shorten the paragraph to the selection principle ("chosen by the fixed rules given in its caption"), and let the paragraph carry its one interpretive point, the failure pattern, with explicit panel letters.
- Terminology across A-E: the same concept appears as "border of the crop" (l. 102), "border of the imaged field" (l. 127) and "border of the fixed crop" (l. 151), while \S5.1.2 (05-experiments.tex l. 117-118) defines "edge of the imaged field". The pad-aware definition is the one actually used. Use the \S5.1.2 term throughout, including \S5.2 l. 397 ("touches the crop border"), so the reader knows Table E.1 uses the same split as the main text.

### Recurring tells in this part

- Colon-introduced lists or reveals closing a sentence, e.g. "shows how much lesion area the window removes: some lesion area in 27.3 % ..." and "The two failure cases share one pattern: ...". About 4-5 times (l. 50, 100, 103, 190). This is acceptable in captions; in running prose it reads better as two sentences.
- Stacked 'of the ... of the' noun chains in captions, e.g. "mean ± SE of the differences of the late-epoch change-region Dice over the five folds" and "the mean over the five folds of the late-epoch mean within that group". About 3 times (Tables E.1, E.3). Rephrase around a verb or with "difference in".
- Comma-chained fragments after a colon in place of sentences: Table E.2 caption, "growth rate on the square-root area scale ..., predicted rate averaged over the late epochs, 75 validation eyes ... pooled, seed 42". Once, and the most machine-like structure in the range.
- Announce-then-repeat: a framing sentence followed by a near-copy, e.g. "This appendix summarises the visit schedule, the lesion scale ..." and then "The visit schedule and the lesion scale of the cohort are summarised in Figure A.1". Once in A, and in effect once more in D (paragraph vs caption).
- Terminology drift for one concept or one arm: border of the crop / fixed crop / imaged field, and "Dilated-stencil GNN" vs "Graph network, dilated stencil". About 4 occurrences across D, E and F.
- Repeated additive 'also' in a short procedural paragraph (Run identity: "each run also records ... each run also records"). Once, but it hides the logic of that paragraph.

## Findings

### A.1 [medium] Appendix A.1 Visit Schedule and Lesion Scale

`91-appendix.tex:16` · GPTZero: AI · flow, ai-tone

> The visit schedule and the lesion scale of the cohort are summarised in Figure~\ref{fig:appendix:cohort}. Most eyes were seen six or seven times, three in four intervals between visits are 180 days long, and the baseline lesion area ranges from 0.11 to 20.8\,mm$^2$, with a median of 6.7\,mm$^2$.

**Issue.** The first sentence repeats almost word for word the chapter opener two lines above ("summarises the visit schedule, the lesion scale ...") and adds nothing new. This announce-then-repeat pattern is the flagged part; the unflagged second sentence carries the content.

**Suggestion.**

> As Figure~\ref{fig:appendix:cohort} shows, most eyes were seen six or seven times, three in four intervals between visits are 180 days long, and the baseline lesion area ranges from 0.11 to 20.8\,mm$^2$, with a median of 6.7\,mm$^2$.

### A.2 [medium] Appendix A.2 Native Grids and the Crop

`91-appendix.tex:48` · GPTZero: human · clarity

> Figure~\ref{fig:appendix:crop} relates the native grids of the eyes to the modelling window of~\S\ref{sec:data:spatial} and shows how much lesion area the window removes: some lesion area in 27.3\,\% of the visits, more than 5\,\% of it in 6.0\,\%, and at most 25.7\,\%.

**Issue.** The list after the colon is elliptical. "more than 5 % of it" leaves "it" ambiguous, and "at most 25.7 %" can be misread as a share of visits, when it is the worst-case share of one lesion (cf. \S3.3).

**Suggestion.**

> Figure~\ref{fig:appendix:crop} relates the native grids of the eyes to the modelling window of~\S\ref{sec:data:spatial} and shows how much lesion area the window removes. Some lesion area is lost in 27.3\,\% of the visits, more than 5\,\% of the lesion in 6.0\,\%, and at most 25.7\,\% of the lesion in a single visit.

### A.3 [low] Figure A.2 caption

`91-appendix.tex:63` · GPTZero: AI · clarity

> The grid is the same at every visit of an eye, and eyes with identical grids overlap (67 distinct grids).

**Issue.** "eyes ... overlap" names the eyes where the plotted markers are meant. Saying that the markers coincide states directly why fewer than 75 points are visible.

**Suggestion.**

> The grid is the same at every visit of an eye, and the markers of eyes with identical grids coincide (67 distinct grids).

### A.4 [medium] Appendix D Additional Rollout Figures

`91-appendix.tex:98` · GPTZero: AI · clarity, flow

> Figure~\ref{fig:appendix:rollouts} shows rollouts of the canonical dilated-stencil graph network for four further eyes, chosen by fixed rules from the 48 validation eyes of folds 0, 1 and 2: the eyes with the highest and the lowest growth-region Dice at the one-year anchor, the eye whose lesion has the most pixels on the border of the crop, and the eye with the fastest true growth.

**Issue.** One 60-word sentence carries the figure reference, the eye pool and four selection rules after a colon, and it repeats the caption almost verbatim. "border of the crop" also differs from the caption's "border of the imaged field" and from the \S5.1.2 term "edge of the imaged field". The selection actually uses the pad-aware edge.

**Suggestion.**

> Figure~\ref{fig:appendix:rollouts} shows rollouts of the canonical dilated-stencil graph network for four further eyes. They were chosen by fixed rules from the 48 validation eyes of folds 0, 1 and 2: the eyes with the highest and the lowest growth-region Dice at the one-year anchor, the eye with the most true-lesion pixels on the edge of the imaged field, and the eye with the fastest true growth. (Use "edge of the imaged field" in panel~(c) of the caption as well.)

### A.5 [medium] Appendix D Additional Rollout Figures

`91-appendix.tex:103` · GPTZero: AI · clarity, ai-tone

> The two failure cases share one pattern: the true lesion expands far beyond its baseline outline, and the predicted change stays a narrow band along that outline, so most of the true change is missed.

**Issue.** "The two failure cases" is never defined. Four eyes are shown, and the reader must work out which two are meant. The colon reveal ("share one pattern:") is the flagged rhetorical tell.

**Suggestion.**

> In the two failure cases, panels~(b) and~(d), the true lesion expands far beyond its baseline outline while the predicted change stays a narrow band along that outline, so most of the true change is missed.

### A.6 [medium] Appendix E (chapter heading)

`91-appendix.tex:139` · GPTZero: AI · flow

> \chapter{Ablation Details}

**Issue.** The heading promises ablation sweeps, but the chapter contains a border/interior split, growth-speed measures and a two-seed replication table, none of which is an ablation. The chapter also opens with no text, so the reader is not told what the three tables are for. The section labels (app:full-results:*) already point to the intended title.

**Suggestion.**

> Retitle to \chapter{Additional Result Tables} and add under it: "This appendix gives three tables that support Chapter~\ref{ch:experiments}: the headline metric on border-touching and interior eyes (Table~\ref{tab:appendix:border-interior}), the growth-speed measures of the arms (Table~\ref{tab:appendix:growth-speed}), and the main comparisons at both seeds (Table~\ref{tab:appendix:seeds})."

### A.7 [low] Table E.1 caption

`91-appendix.tex:150` · GPTZero: AI · clarity

> Change-region Dice at the one-year anchor, seed 42, split by whether the eye's lesion touches the border of the fixed crop (\S\ref{sec:data:spatial}).

**Issue.** \S5.1.2 defines the split as the true lesion at the anchor touching the pad-aware edge of the imaged field. "border of the fixed crop" suggests a crop-only criterion that excludes the padded visits.

**Suggestion.**

> Change-region Dice at the one-year anchor, seed 42, split by whether the eye's true lesion at the anchor touches the edge of the imaged field (\S\ref{sec:data:spatial}).

### A.8 [low] Table E.1 caption

`91-appendix.tex:154` · GPTZero: AI · clarity *(added in verification)*

> Each value is the mean over the five folds of the late-epoch mean within that group.

**Issue.** The nested "mean over ... of the ... mean" chain makes the reader parse the order of the two averages.

**Suggestion.**

> Each value is the late-epoch mean within the group, averaged over the five folds.

### A.9 [low] Tables E.1 and E.2, row labels

`91-appendix.tex:166` · GPTZero: AI · clarity

> Dilated-stencil GNN

**Issue.** Tables E.1 and E.2 use labels ("Dilated-stencil GNN", "k-NN GNN") that differ from Table 5.1 and Table F.2 ("Graph network, dilated stencil", "Graph network, $k$-NN, $k = 12$"). A reader matching rows across tables has to translate, and "k-NN GNN" does not state k.

**Suggestion.**

> Use the row labels of Table~\ref{tab:experiments:arms} in Tables E.1 and E.2, as Table F.2 already does, e.g. "Graph network, dilated stencil" and "Graph network, $k$-NN, $k = 12$".

### A.10 [medium] Table E.2 caption

`91-appendix.tex:188` · GPTZero: AI · clarity, ai-tone

> Eye-level growth-speed measures for every arm of Table~\ref{tab:experiments:arms}, computed as for the canonical model in \S\ref{sec:experiments:qualitative:mai}: growth rate on the square-root area scale over each eye's whole follow-up, predicted rate averaged over the late epochs, 75 validation eyes of the five folds pooled, seed 42. The AUC separates the top 10, 15 and 20\,\% of true growth rates (8, 11 and 15 eyes) from the rest.

**Issue.** A colon followed by comma-chained fragments replaces sentences, the most machine-like structure in the range. "The AUC separates" attributes the separation to the metric, when it is the predicted rate that separates the groups. "every arm" overstates, because the per-pixel floor of Table 5.1 is not listed.

**Suggestion.**

> Eye-level growth-speed measures for the arms of Table~\ref{tab:experiments:arms}, seed 42, computed as for the canonical model in \S\ref{sec:experiments:qualitative:mai}: the growth rate is taken on the square-root area scale over each eye's whole follow-up, the predicted rate is averaged over the late epochs, and the 75 validation eyes of the five folds are pooled. The AUC measures how well the predicted rate separates the top 10, 15 and 20\,\% of true growth rates (8, 11 and 15 eyes) from the rest.

### A.11 [low] Table E.2 caption

`91-appendix.tex:194` · GPTZero: AI · clarity

> Only point estimates are given; the 95\,\% bootstrap intervals are about $\pm 0.2$ wide for every arm (see Table~\ref{tab:experiments:mai} for the canonical model), so the arms cannot be told apart on these measures.

**Issue.** "about ±0.2 wide" mixes a half-width (±) with a width, so the reader cannot tell whether the intervals span 0.2 or 0.4.

**Suggestion.**

> Only point estimates are given; for every arm the 95\,\% bootstrap intervals reach about $\pm 0.2$ around the estimate (see Table~\ref{tab:experiments:mai} for the canonical model), so the arms cannot be told apart on these measures.

### A.12 [medium] Table E.3 caption

`91-appendix.tex:238` · GPTZero: AI · clarity

> Fold-paired: mean $\pm$ SE of the differences of the late-epoch change-region Dice over the five folds, with the number of folds on which the first arm is higher. Per eye: mean $\pm$ SE of the differences of the growth-region Dice at each eye's first rollout step past 0.95 years, with the number of eyes on which the first arm is higher and the $t$ value (\S\ref{sec:experiments:protocol:stats}).

**Issue.** The stacked "of the differences of the ..." chains are hard to parse. "first rollout step past 0.95 years" is not identified as the one-year anchor used throughout Chapter 5. The "Reading" line of every block is never explained.

**Suggestion.**

> Fold-paired: the per-fold difference in late-epoch change-region Dice, as mean $\pm$ SE over the five folds, with the number of folds on which the first arm is higher. Per eye: the per-eye difference in growth-region Dice at the one-year anchor (each eye's first rollout step past 0.95 years), as mean $\pm$ SE, with the number of eyes on which the first arm is higher and the $t$ value (\S\ref{sec:experiments:protocol:stats}). \emph{Reading} gives the verdict from both seeds and both instruments.

### A.13 [medium] Appendix F, Run identity

`91-appendix.tex:345` · GPTZero: AI · clarity, tone, ai-tone

> Every run writes its complete configuration into its run directory at the start. The name of the directory encodes the key settings, the fold and the data variant. Since 2 September 2026, each run also records the version of the code it ran; earlier runs are dated by the timestamp of their directory. Because every fold is mounted at the same path on the cluster, each run also records which fold and data variant it loaded. Resuming an interrupted run is disabled, so every reported run was trained in one piece.

**Issue.** Five uniform medium-length sentences contain two additive "also"s. The logic is unclear: the directory name already encodes the fold, so the reader cannot see why the fold is recorded again (the missing step is that the shared mount path does not identify the data). "trained in one piece" is an idiom.

**Suggestion.**

> At the start, every run writes its complete configuration into its run directory, whose name encodes the key settings, the fold and the data variant. Because every fold is mounted at the same path on the cluster, the path does not identify the data, so each run also records the fold and data variant it loaded. Since 2 September 2026, each run records the version of the code it ran; earlier runs are dated by the timestamp of their directory. Resuming an interrupted run is disabled, so no reported run was resumed from a checkpoint.

### A.14 [low] Table F.2 caption

`91-appendix.tex:361` · GPTZero: human · clarity *(added in verification)*

> Experiment names of the arms of Table~\ref{tab:experiments:arms}, seed 42.

**Issue.** The table also lists "FEN, free-form, matched width 139", which is not a row of Table 5.1. A reader who looks for it there will not find it.

**Suggestion.**

> Experiment names of the arms of Table~\ref{tab:experiments:arms} and of the matched free-form control, seed 42.

