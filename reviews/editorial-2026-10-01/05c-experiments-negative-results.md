# Micro feedback 5c: Ch. 5 Experiments, §5.4 Negative Results

[← Overview](00-overview.md)

30 findings: 2 high, 16 medium, 12 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

§5.4 has a clear skeleton. A definition of what counts as a negative result comes first. Three subsections follow (time handling, objective, capacity); each opens with what the framework fixes and closes with a short verdict. The question-style run-in headings guide the reader well, and GPTZero marks two of them ('Is the weighting of the mask channel needed?', 'Would a monotonic-growth penalty help?') and 'What this means.' as human. The main structural weakness is a mismatch between frame and content. The section title, the opening definition and the last sentence of §5.3.5 all announce nulls, but §5.4.2 reports two effects well above the floor: the plain-MSE run never learns change, and removing the soft-Dice term lowers the score on every fold. Inside §5.4.2 the design is also misdescribed ('each with one part changed', although the first run removes two parts), so the verdict on the mask weighting arrives one paragraph late and only by combining two runs without saying so. In §5.4.3 the pre-registered decision rule is stated, but the results never say what it produced; the width-192 result sits in the depth paragraph; and the subsection ends on the Galerkin side question instead of its scoped conclusion. One source defect breaks a rendered sentence: in the soft-Dice paragraph, part of a sentence sits on a comment line, and the PDF prints '... a higher score. in §4.5.1: ...'. The register is consistently passive and objective. The machine-like tone comes from structure, not vocabulary: antithesis closers ('X, not Y'), colon reveals after a result, emphatic 'at all', 'therefore' verdicts, and two mirrored subsection openers.

### Transitions

- §5.3.5 -> §5.4 (05-experiments.tex l. 780): the lead-in '\S\ref{sec:experiments:ablations} reports what was measured and did not matter' is contradicted by §5.4.2, where the plain-MSE run and the removal of the soft-Dice term both change the result. Fix: '\S\ref{sec:experiments:ablations} reports the remaining tests, most of which did not change the result.'
- §5.4 opening (l. 787-796): the definition of a negative result covers only nulls. Add one sentence saying that two of the objective tests show effects above the floor (see the finding at l. 792), so the reader is not surprised by them under this heading.
- §5.4.1 opener (l. 805-808) says both tests use the dilated-stencil network, but the Runge-Kutta test also reports the FNO (l. 841), which appears without introduction. Mention the repetition with the FNO in the opener (finding at l. 805).
- §5.4.2, weighting paragraph -> soft-Dice paragraph: the paragraph headed 'Is the weighting of the mask channel needed?' tests a run that removes the weighting and the soft-Dice term together, and the answer to its own question appears only at the end of the next paragraph. Close the first paragraph with a bridge ('Because this run also lacks the soft-Dice term, the next run separates the two parts.') and open the later verdict with 'Read together with the first run, ...' (findings at l. 882 and l. 898).
- §5.4.2 soft-Dice paragraph (l. 885-906): about 200 words covering four topics (escape timing, final score, fold-4 steadiness, calibration cost). After the broken sentence at l. 903 is restored, start a new short paragraph at the cost sentence.
- §5.4.3 results (l. 1060-1064): 'The U-Net and the FNO with a local path do best at or near their original size.' is followed directly by 'Scaling down costs little:', whose examples cover only the graph network and the T-FEN. Read side by side, the two sentences seem to contradict each other. The author should decide whether 'costs little' is meant for all four classes (as §6.1 'the smaller versions lost little' suggests) and make the scope explicit. No rewrite is proposed, because the scope is a content decision.
- §5.4.3 intro -> results (l. 961-1064): the pre-registered rule (step up after a gain, step down otherwise) is never closed in the results. Add a clause saying that no class earned a step up, so each was also run at a smaller width (finding at l. 1057). Also move the width-192 sentence (l. 1070) from the depth paragraph into the width paragraph.
- §5.4.3 end -> §5.5: the subsection, and with it §5.4, ends on the open Galerkin/width-192 question instead of its conclusion. Place the Galerkin caveat (l. 1077-1084) before the 'Capacity is therefore ...' verdict so that the section ends on the scoped conclusion. Optionally add one closing sentence for §5.4 as a whole, worded so that it keeps the scope of each result, e.g. 'Across the three groups, neither the details of the time handling nor a larger operator improves the result; the mask weighting and the soft-Dice term of the objective do.'
- Closing devices are inconsistent: only §5.4.1 has a separate 'What this means.' paragraph, while §5.4.2 and §5.4.3 put their verdicts inside the last paragraph. Use the same device in all three, or fold the §5.4.1 paragraph into the preceding one.
- Count notation changes from sentence to sentence ('higher on 2 of 5 folds', '(30/75)', 'lower on all five folds', 'lower on 56 of 75 eyes, $t = -5.1$', '(34/75)'), so the reader has to decode each form anew. This is already scheduled in the planned Chapter 5 reporting-scheme pass (NOTES #23); harmonise it there.

### Recurring tells in this part

- Colon reveals after a result clause, about 6 times: 'The change-region Dice does not change: $-0.0006$ ...' (l. 813), 'does leave the collapse, but late:' (l. 887), '(34/75): no measurable effect, so ...' (l. 920), 'Scaling down costs little:' (l. 1062), '... is open: in the runs ...' (l. 1081). Fix: state the number in one sentence and the verdict in the next, or join them with a plain verb.
- Antithesis closers 'X, not Y' / 'rather than', about 4 times: 'a change of parameterisation, not additional knowledge' (l. 824); 'The objective, not the operator, decides ...' (l. 882); '..., not by the way time is stepped' (l. 857); '... rather than to the form of the transport operator' (l. 1084). Fix: keep the positive statement and drop the restated contrast where the contrast is already made.
- Paragraph-ending verdicts built on 'therefore' that restate the paragraph: 6 'therefore' in the rendered range, of which about 4 are such closers ('The simple update of the framework is therefore sufficient ...', 'The weighting is therefore what lets ...', 'The penalty therefore enforces ...', 'Capacity is therefore not a lever ...'). The other two (l. 822, l. 875) are ordinary logical connectives and are fine.
- Emphatic 'at all', 4 times: 'continuous-time model at all' (l. 830), 'reaches the operator at all' (l. 853), 'predicts no change at all' (l. 876), 'learns any change at all' (l. 883).
- Pseudo-cleft constructions, 2: 'What the update needs is that ...' (l. 852), 'The weighting is therefore what lets the model escape ...' (l. 898).
- Mirrored subsection openers, 2 pairs: 'This design is part of the framework that every operator shares, so it matters whether ...' / 'Like the time handling, this objective is part of the shared framework, so it matters which ...', and 'Two tests ask this' / 'Three runs ... ask this'.
- Personified abstractions, about 5: tests and runs that 'ask', a width step that 'earns' a step up, 'The same fold makes the run less steady', capacity as 'a lever'.
- Differences written as if they were the metric itself, 3 times: 'the change-region Dice is $-0.0036$ on average' (l. 918), 'does not change: $-0.0006$' (l. 813), 'ends lower, by $-0.050$' (l. 890, a double negative; the number itself should be handled in the reporting-scheme pass).
- Emphatic auxiliaries and mild intensifiers, about 5: 'does leave' (l. 887), 'does change' (l. 959), 'deliberately simple' (l. 801), 'simply learns' (l. 823); 'exactly that distance' (l. 822) is precise and defensible.

## Findings

### 5c.1 [low] §5.4 Negative Results (introduction)

`05-experiments.tex:789` · GPTZero: AI · clarity

> It is a null at the available precision. It does not show that the tested alternative is equivalent, or that the mechanism behind it has no effect, and each finding is scoped to the backbone, the folds and the seed on which it was measured.

**Issue.** Three consecutive sentences open with 'A ... / It ... / It ...', and the third joins two unrelated points (what a null does not show; the scope of each finding) with ', and'.

**Suggestion.**

> Such a result is a null at the available precision: it does not show that the tested alternative is equivalent or that the mechanism behind it has no effect. Each finding is scoped to the backbone, the folds and the seed on which it was measured.

### 5c.2 [medium] §5.4 Negative Results (introduction)

`05-experiments.tex:792` · GPTZero: AI · flow, clarity

> This section reports three groups of such results: the time handling of the update (\S\ref{sec:experiments:ablations:time}), the composition of the training objective (\S\ref{sec:experiments:ablations:loss}) and the capacity of the operators (\S\ref{sec:experiments:ablations:capacity}).

**Issue.** 'Such results' tells the reader that everything below is a null, but §5.4.2 also reports two effects well above the floor: plain MSE never learns change, and removing the soft-Dice term lowers the score on all five folds. A reader expecting only nulls will be surprised by them under this heading.

**Suggestion.**

> This section reports three groups of tests: the time handling of the update (\S\ref{sec:experiments:ablations:time}), the composition of the training objective (\S\ref{sec:experiments:ablations:loss}) and the capacity of the operators (\S\ref{sec:experiments:ablations:capacity}). Most of them give negative results in this sense; two of the tests on the objective show effects above the floor.

### 5c.3 [medium] §5.4.1 Time Handling (introduction)

`05-experiments.tex:805` · GPTZero: AI · flow, ai-tone

> This design is part of the framework that every operator shares, so it matters whether its details carry any of the accuracy. Two tests ask this, both on the canonical dilated-stencil network.

**Issue.** This opener is the template that the §5.4.2 opener repeats, and 'two tests ask this' personifies the tests. 'Both on the canonical dilated-stencil network' is incomplete, because the second test is also reported for the FNO, which then appears without introduction.

**Suggestion.**

> Because every operator shares this update, two tests check whether its details contribute to the accuracy. Both use the canonical dilated-stencil network; the second is repeated with the FNO.

### 5c.4 [medium] §5.4.1 Time Handling: Is the multiplication by Δt needed?

`05-experiments.tex:813` · GPTZero: AI · clarity, tone

> The change-region Dice does not change: $-0.0006$ on average ($\pm 0.0061$~SE, higher on 2 of 5 folds) and per eye $-0.0028 \pm 0.0037$ (30/75).

**Issue.** The colon presents a difference as if it were the Dice value. 'Does not change' is also blunter than the section's own definition of a null (a difference under the floor).

**Suggestion.**

> The change-region Dice does not change measurably. The difference is $-0.0006$ on average ($\pm 0.0061$~SE, higher on 2 of 5 folds) and $-0.0028 \pm 0.0037$ per eye (30/75).

### 5c.5 [medium] §5.4.1 Time Handling: Is the multiplication by Δt needed?

`05-experiments.tex:821` · GPTZero: AI · clarity, tone

> At a pixel that changes between two visits, the scaled update therefore has to produce exactly that distance divided by $\Delta t$, whatever the interval, and the operator simply learns to divide by $\Delta t$ internally.

**Issue.** 'The scaled update' is imprecise. The scaled update $\Delta t \cdot f_\theta$ produces the distance itself; it is $f_\theta$ that must output the distance divided by $\Delta t$. A careful reader stumbles over the algebra. 'Simply' is conversational filler.

**Suggestion.**

> At a pixel that changes between two visits, $f_\theta$ in the scaled form therefore has to output exactly that distance divided by $\Delta t$, whatever the interval; the operator learns to perform this division internally.

### 5c.6 [medium] §5.4.1 Time Handling: Is the multiplication by Δt needed?

`05-experiments.tex:824` · GPTZero: AI · ai-tone, tone

> The multiplication is a change of parameterisation, not additional knowledge.

**Issue.** This is an aphoristic 'X, not Y' closer, and 'knowledge' gives the operator a human quality. It reads like a slogan, not a technical statement.

**Suggestion.**

> The multiplication is thus a reparameterisation that adds no information beyond the $\Delta t$ input.

### 5c.7 [low] §5.4.1 Time Handling: Is the multiplication by Δt needed?

`05-experiments.tex:828` · GPTZero: AI · clarity, ai-tone

> It also means that $f_\theta$ is not a growth rate that could be read off; whether the operator can be read as a continuous-time model at all is tested in~\S\ref{sec:experiments:validity:swap}.

**Issue.** 'It' is ambiguous. The sentence directly before ('It is kept because ...') is about why the multiplication is retained, but this 'It' refers back to the internal division two sentences earlier. 'Read off' and 'read as' repeat the same verb, 'at all' adds emphasis, and the semicolon joins two separate points.

**Suggestion.**

> The internal division also means that $f_\theta$ cannot be read off as a growth rate. Whether the trained operator can be interpreted as a continuous-time model is tested in~\S\ref{sec:experiments:validity:swap}.

### 5c.8 [medium] §5.4.1 Time Handling: Does the time-stepping scheme matter?

`05-experiments.tex:840` · GPTZero: AI · clarity

> Over the dilated-stencil network, the change-region Dice is 0.012 lower than with the single step, on 4 of 5 folds; over the FNO it is 0.006 higher. Both differences lie within the noise level, and the Runge--Kutta step costs about 4.8 times the training time (\S\ref{sec:experiments:cost}).

**Issue.** The cost clause comes right after the FNO result, so the 4.8 factor reads as if it applied to both operators. §5.6 gives it for the dilated-stencil network only (about 2x for the FNO). It is also unclear what it is relative to.

**Suggestion.**

> Over the dilated-stencil network, the change-region Dice is 0.012 lower than with the single step, on 4 of 5 folds; over the FNO it is 0.006 higher. Both differences lie within the noise level. Over the dilated-stencil network, the Runge--Kutta step costs about 4.8 times the training time of the single step (\S\ref{sec:experiments:cost}).

### 5c.9 [medium] §5.4.1 Time Handling: What this means

`05-experiments.tex:852` · GPTZero: AI · ai-tone, clarity

> What the update needs is that the length of the interval reaches the operator at all, either as an input to a single step or through an integrator that steps over the interval; how it arrives makes no measurable difference.

**Issue.** A pseudo-cleft ('What the update needs is'), an emphatic 'at all' and a mirrored semicolon pair make this read as machine-written.

**Suggestion.**

> The length of the interval has to reach the operator, either as an input to a single step or through an integrator that steps over the interval; which of the two routes is used makes no measurable difference.

### 5c.10 [low] §5.4.1 Time Handling: What this means

`05-experiments.tex:855` · GPTZero: AI · ai-tone

> The simple update of the framework is therefore sufficient, and the accuracy is decided by the spatial operator (\S\ref{sec:experiments:ingredients}), not by the way time is stepped.

**Issue.** This closer is a 'therefore' verdict plus a 'not by ...' antithesis that restates what the previous sentence just said ('makes no measurable difference').

**Suggestion.**

> The simple update of the framework is therefore sufficient, and the accuracy is decided by the spatial operator (\S\ref{sec:experiments:ingredients}).

### 5c.11 [**HIGH**] §5.4.2 The Objective (introduction)

`05-experiments.tex:868` · GPTZero: AI · flow, clarity, ai-tone

> Like the time handling, this objective is part of the shared framework, so it matters which of its parts carry the result. Three runs on the canonical dilated-stencil network, each with one part changed, ask this.

**Issue.** 'Each with one part changed' does not hold for the first run, which removes both the mask weighting and the soft-Dice term (l. 878-879). That is why the verdict on the weighting later has to be pieced together from two runs. The sentence also mirrors the §5.4.1 opener almost word for word ('part of the framework ..., so it matters whether ...'; tests that 'ask'), a template-like tell.

**Suggestion.**

> Three runs on the canonical dilated-stencil network test which of its parts the result depends on: the first uses a plain, unweighted mean squared error without the soft-Dice term, the second drops only the soft-Dice term, and the third adds a monotonic-growth penalty.

### 5c.12 [low] §5.4.2 The Objective: Is the weighting of the mask channel needed?

`05-experiments.tex:877` · GPTZero: AI · clarity

> The collapse counter of~\S\ref{sec:experiments:protocol:metrics} detects this. Trained with a plain, unweighted mean squared error and no soft-Dice term, the network falls into this collapse and never leaves it within the 30 epochs: its change-region Dice is 0 on every fold and at every epoch, and at the last epoch 74 of the 75 validation eyes have a prediction identical to their baseline mask.

**Issue.** The second sentence runs about 55 words, with a colon reveal and two facts joined by 'and'. 'Detects this' has a vague antecedent.

**Suggestion.**

> The collapse counter of~\S\ref{sec:experiments:protocol:metrics} detects this copying. Trained with a plain, unweighted mean squared error and no soft-Dice term, the network falls into this collapse and never leaves it within the 30 epochs. Its change-region Dice is 0 on every fold and at every epoch, and at the last epoch 74 of the 75 validation eyes have a prediction identical to their baseline mask.

### 5c.13 [medium] §5.4.2 The Objective: Is the weighting of the mask channel needed?

`05-experiments.tex:882` · GPTZero: AI · ai-tone, flow

> The objective, not the operator, decides whether the model learns any change at all.

**Issue.** This aphoristic 'X, not Y' closer with an emphatic 'at all' is a typical machine pattern. It also leaves the paragraph's own question (is the weighting needed?) unanswered, because this run removed two parts; the answer appears only a paragraph later.

**Suggestion.**

> For the same operator, the objective decides whether the network learns any change. Because this run also lacks the soft-Dice term, the next run separates the two parts.

### 5c.14 [low] §5.4.2 The Objective: What does the soft-Dice term add?

`05-experiments.tex:886` · GPTZero: AI · ai-tone, clarity *(added in verification)*

> With the mask weighting kept and only the soft-Dice term removed, the network does leave the collapse, but late: on the five folds, its change-region Dice first rises above 0 at epochs 2, 8, 3, 7 and 12, against epoch 0 with the full objective (Figure~\ref{fig:experiments:curves}b).

**Issue.** An emphatic auxiliary ('does leave') plus a colon reveal ('but late:') make this a typical flagged construction; the editor lists both as tells but gave no finding.

**Suggestion.**

> With the mask weighting kept and only the soft-Dice term removed, the network leaves the collapse after a delay. On the five folds, its change-region Dice first rises above 0 at epochs 2, 8, 3, 7 and 12, against epoch 0 with the full objective (Figure~\ref{fig:experiments:curves}b).

### 5c.15 [medium] §5.4.2 The Objective: What does the soft-Dice term add?

`05-experiments.tex:894` · GPTZero: AI · clarity, ai-tone

> The same fold makes the run less steady. It leaves the collapse only at epoch 12, inside the late-epoch window, so averaged over the folds the epoch-to-epoch standard deviation of the late-epoch Dice is 0.043 against 0.015 with the full objective, but only 0.017 against 0.013 on folds 0 to 3.

**Issue.** The fold is personified ('makes the run less steady'), and 'It leaves the collapse' could refer to the fold or to the run.

**Suggestion.**

> The run is also less steady, mainly because of fold 4. On that fold the network leaves the collapse only at epoch 12, inside the late-epoch window, so averaged over the five folds the epoch-to-epoch standard deviation of the late-epoch Dice is 0.043 against 0.015 with the full objective, but only 0.017 against 0.013 on folds 0 to 3.

### 5c.16 [medium] §5.4.2 The Objective: What does the soft-Dice term add?

`05-experiments.tex:898` · GPTZero: AI · ai-tone, flow

> The weighting is therefore what lets the model escape the collapse, and the soft-Dice term adds an immediate escape and a higher score.

**Issue.** This is a pseudo-cleft ('is what lets') followed by a balanced two-part verdict, with 'escape ... escape' repeated. The conclusion about the weighting depends on the first run, but the sentence does not say so.

**Suggestion.**

> Read together with the first run, the mask weighting therefore lets the model leave the collapse; the soft-Dice term makes it leave at once and raises the score.

### 5c.17 [**HIGH**] §5.4.2 The Objective (soft-Dice paragraph)

`05-experiments.tex:903` · GPTZero: AI · flow, clarity

> % 0.013/0.147 vs full 0.011/0.019/0.010/0.012/0.022 (fold 4 carries it). Its cost is the stretch of the raw mask regression described in~\S\ref{sec:method:training:loss}: the raw mask error of the free-running rollout is about twice as large with the term as without it (1.10 against 0.51). It does not change any thresholded metric.

**Issue.** The clause 'Its cost is the stretch of the raw mask regression described' sits at the end of a comment line, so the PDF prints the fragment '... and a higher score. in §4.5.1: the raw mask error ...' (confirmed in the GPTZero scan). Even once restored, 'Its' is ambiguous, because the preceding sentence names both the weighting and the soft-Dice term.

**Suggestion.**

> Break the line after '(fold 4 carries it).' and put the sentence on its own uncommented line (ideally as the start of a new short paragraph), naming the term: The cost of the soft-Dice term is the stretch of the raw mask regression described in~\S\ref{sec:method:training:loss}: the raw mask error of the free-running rollout is about twice as large with the term as without it (1.10 against 0.51). This stretch does not change any thresholded metric.

### 5c.18 [medium] §5.4.2 The Objective: Would a monotonic-growth penalty help?

`05-experiments.tex:917` · GPTZero: AI · clarity, ai-tone

> With the penalty at weight 2.0, the change-region Dice is $-0.0036$ on average ($\pm 0.0037$~SE, higher on 2 of 5 folds) and per eye $-0.0042 \pm 0.0034$ (34/75): no measurable effect, so the simpler objective is kept.

**Issue.** A difference is stated as if it were the Dice itself, and the colon-plus-fragment verdict ': no measurable effect, so ...' is a recurring tell.

**Suggestion.**

> With the penalty at weight 2.0, the difference in change-region Dice is $-0.0036$ on average ($\pm 0.0037$~SE, higher on 2 of 5 folds) and $-0.0042 \pm 0.0034$ per eye (34/75). The penalty has no measurable effect, and the simpler objective is kept.

### 5c.19 [low] §5.4.2 The Objective: Would a monotonic-growth penalty help?

`05-experiments.tex:924` · GPTZero: AI · tone

> Under the pushforward curriculum (\S\ref{sec:method:training:curriculum}), the previous state on an unrolled step is the model's own earlier prediction, so the penalty locks in the model's own false positives: a pixel wrongly marked as atrophic can no longer be corrected toward the ground truth without paying the penalty.

**Issue.** 'Locks in' and 'paying the penalty' are idioms, and 'own ... own' repeats within one clause.

**Suggestion.**

> Under the pushforward curriculum (\S\ref{sec:method:training:curriculum}), the previous state on an unrolled step is the model's own earlier prediction, so the penalty preserves the model's false positives: a pixel wrongly marked as atrophic can no longer be corrected toward the ground truth without incurring the penalty.

### 5c.20 [medium] §5.4.2 The Objective: Would a monotonic-growth penalty help?

`05-experiments.tex:931` · GPTZero: AI · clarity

> The penalty therefore enforces different priors on teacher-forced and on unrolled steps.

**Issue.** 'Teacher-forced' appears nowhere else in the thesis; §4.5.2 speaks of 'a plain one-step pass on observed inputs'. The project rules ask that every term be explained on first use.

**Suggestion.**

> The penalty therefore enforces different priors on steps that start from an observed state and on unrolled steps.

### 5c.21 [low] §5.4.1 Time Handling: Is the multiplication by Δt needed?

`05-experiments.tex:954` · GPTZero: AI · clarity

> Each architecture class was scaled while everything else was held fixed: the same loss, curriculum, epoch budget and five folds, seed 42. Each run changes one size setting only.

**Issue.** Two consecutive 'Each ...' openers, a tense shift (was scaled / changes), and a slightly garbled list ending 'and five folds, seed 42'.

**Suggestion.**

> Each architecture class was scaled with everything else held fixed (loss, curriculum, epoch budget, the five folds and seed 42), and each run changed one size setting only.

### 5c.22 [low] §5.4.3 Capacity (introduction)

`05-experiments.tex:959` · GPTZero: AI · clarity, tone

> Depth does change the reach of the graph network, so it is read for each class on its own; the U-Net and the FNO have no depth setting.

**Issue.** The emphatic 'does change' adds stress the sentence does not need, 'it' could refer to depth or to the reach, and 'is read' is lab jargon for 'is analysed'.

**Suggestion.**

> Depth, by contrast, changes the reach of the graph network, so depth results are compared only within a class; the U-Net and the FNO have no depth setting.

### 5c.23 [medium] §5.4.3 Capacity (introduction)

`05-experiments.tex:961` · GPTZero: AI · ai-tone, clarity

> The design and a decision rule were fixed before the first run: a width step that clears the floor on both instruments earns a further step up, and a width step without a gain earns a step down instead, to between about a sixth and a third of the original size.

**Issue.** The width step is personified ('earns') in a mirrored pair of clauses ('a width step that ... earns ...; a width step without ... earns ...'), a clear template tell.

**Suggestion.**

> The design and a decision rule were fixed before the first run: if a width step cleared the floor on both instruments, a larger width was to be run next; otherwise, a smaller width between about a sixth and a third of the original size.

### 5c.24 [low] Table 5.3 caption (capacity study)

`05-experiments.tex:970` · GPTZero: human · clarity *(added in verification)*

> The ratio is the parameter count against the arm's own original size (1).

**Issue.** The bare '(1)' can be read as a footnote or an equation reference rather than as 'the original size has ratio 1', and 'against' is loose for a ratio.

**Suggestion.**

> The ratio is the parameter count relative to the arm's original size, which has ratio 1.

### 5c.25 [low] Figure 5.6 caption (capacity study)

`05-experiments.tex:1040` · GPTZero: AI · clarity

> Each point is the fold-paired difference of the change-region Dice at the one-year anchor between an operator scaled in size and the same operator at its original size, over five folds at seed 42, with the between-fold standard error, plotted against the ratio of their parameter counts on a logarithmic axis.

**Issue.** This single sentence of about 50 words chains four appended modifiers ('over ..., with ..., plotted against ...').

**Suggestion.**

> Each point is the fold-paired difference in change-region Dice at the one-year anchor between an operator scaled in size and the same operator at its original size (five folds, seed 42; bars: between-fold standard error). The horizontal axis gives the ratio of their parameter counts on a logarithmic scale.

### 5c.26 [medium] §5.4.3 Capacity (results)

`05-experiments.tex:1057` · GPTZero: AI · flow

> Table~\ref{tab:experiments:capacity} gives the result. No width step raises any class above the floor on either instrument.

**Issue.** The paragraph opens with an announcement and never closes the pre-registered rule just stated. The reader is not told that, because no step up was earned, every class was run at a smaller width, which is why the table has those rows.

**Suggestion.**

> No width step raises any class above the floor on either instrument (Table~\ref{tab:experiments:capacity}), so, following the rule, each class was also run at a smaller width.

### 5c.27 [low] §5.4.3 Capacity (depth paragraph)

`05-experiments.tex:1066` · GPTZero: AI · clarity *(added in verification)*

> Four message-passing rounds instead of two, which also double the reach of the dilated stencil, lower the graph network on every fold ($-0.009 \pm 0.002$~SE, 0/5), a small difference under the floor.

**Issue.** 'Lower the graph network' is elliptical: it is the network's change-region Dice that is lowered, not the network.

**Suggestion.**

> Four message-passing rounds instead of two, which also double the reach of the dilated stencil, lower the Dice of the graph network on every fold ($-0.009 \pm 0.002$~SE, 0/5), by a small difference under the floor.

### 5c.28 [medium] §5.4.3 Capacity (results)

`05-experiments.tex:1070` · GPTZero: AI · flow

> At width 192, the T-FEN diverges during training on folds 1 and 4 and ties width 96 on the other three.

**Issue.** This is a width result placed at the end of the paragraph that opens 'Depth does not help where it was tested.' The reader of the width paragraph above is never told that one width step made a model diverge.

**Suggestion.**

> Move it to the end of the preceding paragraph, after '... level with width 96.', as: Scaled up to width 192, by contrast, the T-FEN diverges during training on folds 1 and 4 and ties width 96 on the other three. The depth paragraph then covers only the four-round graph network and the eight-layer T-FEN.

### 5c.29 [medium] §5.4.3 Capacity (conclusion)

`05-experiments.tex:1074` · GPTZero: AI · ai-tone, tone

> Capacity is therefore not a lever on this task in any of the four classes, and the comparisons at matched size in~\S\ref{sec:experiments:main-results} and~\S\ref{sec:experiments:ingredients} are not an artefact of the size at which they were made. The finding is scoped to one seed.

**Issue.** 'Not a lever' is a metaphor. The sentence is a sweeping 'therefore' verdict with two negations, followed by a caveat that reads as an afterthought.

**Suggestion.**

> At seed 42, changing the capacity therefore does not improve the result in any of the four classes, and the comparisons at matched size in~\S\ref{sec:experiments:main-results} and~\S\ref{sec:experiments:ingredients} do not depend on the size at which they were made.

### 5c.30 [low] §5.4.3 Capacity (Galerkin caveat)

`05-experiments.tex:1079` · GPTZero: AI · clarity, ai-tone

> Whether the divergence at width 192 comes from the defect at the crop edge described in~\S\ref{sec:experiments:validity:tfen} is open: in the runs with the energy-conserving form completed so far, width 192 fails on the same two folds, which points to an instability of the larger network in training rather than to the form of the transport operator.

**Issue.** 'Is open:' followed by evidence that points one way reads as self-contradictory without a contrastive link. The sentence is long and ends on a 'rather than' contrast.

**Suggestion.**

> Whether the divergence at width 192 comes from the defect at the crop edge described in~\S\ref{sec:experiments:validity:tfen} is not settled. In the runs with the energy-conserving form completed so far, however, width 192 fails on the same two folds, which points to an instability of the larger network in training and not to the form of the transport operator.

