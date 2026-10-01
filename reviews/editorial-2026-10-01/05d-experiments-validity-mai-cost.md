# Micro feedback 5d: Ch. 5 Experiments, §5.5 Validity Diagnostics, §5.6 Qualitative/Mai comparison, §5.7 Computational Cost

[← Overview](00-overview.md)

45 findings: 3 high, 18 medium, 24 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

The range is well built at section level. §5.5 announces two diagnostics. §5.5.1 runs purpose -> principle -> criteria stated before results -> setup -> results -> implications, which is the strongest argument in the range, and §5.5.2 gives a clear diagnosis-and-fix sequence. Four structural weak points stand out. (1) The 'What is tested' paragraph of §5.5.1 repeats §4.3.7 ('Jump and continuous time') almost point for point, including the Ott/Krishnapriyan argument and even the outcome, with no back-reference. (2) Criterion C2 ('at least as fine ..., by step or by order') can be read in a way under which the RK4-trained network fails: its single Euler step, at -0.0201, would count. A reader who checks Table 5.4 against the criterion meets an apparent contradiction. (3) §5.6 opens straight into its only subsection, with no transition from the Courant-number detail of §5.5.2 and none of the qualitative content its title promises (still a TODO). Inside §5.6.1 the comparability caveats are spread over two captions and two paragraphs, the crop caveat appears three times, and the sentence on Mai's growth-rate definition is stranded in the caveat paragraph. (4) §5.7 splits its measurement facts (hardware, epochs, what was not measured) between the two ends of the section. It also announces 'three ratios' that do not depend on the timing details and then shows with the FNO that the wrapper ratio depends on the fixed part of the epoch. The register is mostly consistent, technical and carefully hedged. The flagged tone comes from colon reveals, personified abstractions ('the gain sits', 'r asks', 'the gap belongs to'), 'X, not Y' closers, teaser sentences and a few idioms ('bought nothing', 'ties', 'is ahead', 'did not help', 'head-to-head'), not from buzzwords. The [HUMAN]-judged passages (e.g. 'The T-FEN passes as well. Refining its step ... changes the Dice by at most 0.0003') show the author's own voice: short declaratives that carry a number. Most rewrites move flagged sentences towards that pattern. The chapter ends on a scope statement ('Inference time ... were not measured') and not on the cost-versus-benefit reading.

### Transitions

- §5.4 -> §5.5 (05-experiments.tex l. 1165-1169): the move from accuracy results to non-accuracy diagnostics is announced, but the opening sentence ('are not accuracy numbers') states what the diagnostics are not, not what they are for. Open with their purpose and name the two subsections by \ref so the reader has a map (finding at l. 1165).
- §5.5.1 'What is tested' (l. 1175-1191) repeats §4.3.7 'Jump and continuous time' (04-method.tex l. 863-881): the jump vs continuous reading, the Ott/Krishnapriyan caution and the solver-swap idea, which §4.3.7 already previews with its outcome. Add a back-reference ('As discussed in \S\ref{sec:method:family:rk}, ...') and keep here only what is new: the link to the Euler form of the update and to the FEN.
- §5.5.1 uses the long noun phrase 'the network trained inside the (autonomous) Runge--Kutta wrapper' four times (l. 1219-1220, 1241, 1254, 1256-1257); Table 5.4 says 'Network trained in the RK4 wrapper'. Introducing one short label in 'Setup' (e.g. 'the RK4-trained network') and using it consistently would make 'Results' and 'What follows' easier to scan.
- §5.5.1 C2 (l. 1204) and the Table 5.4 caption (l. 1279-1280): 'at least as fine ..., by step or by order' must be read as 'in both step and order'. Only that reading makes the RK4-trained network pass, because its single Euler step (-0.0201) exceeds 0.0127. Make the definition and the caption say so (finding at l. 1204).
- §5.5.2 'The energy-conserving form' (l. 1374-1378): the seed-7 stability sentence sits between the seed-42 stability result and the seed-42 accuracy result, so the following 'Its accuracy' reads as if it referred to the seed-7 run. Either move the seed-7 sentence after the accuracy sentence or name the seed at the start of the accuracy sentence (finding at l. 1375).
- §5.5.2 -> §5.6 (l. 1400-1469): the range jumps from a Courant-number detail into a new section with no opening text; §5.6 starts directly with its subsection heading. Insert a bridging sentence under the §5.6 heading. While the qualitative part is a TODO, keep the bridge neutral so that it does not promise per-eye analyses.
- §5.6.1: the comparability caveats are spread across the Table 5.6 caption, the paragraph 'The comparison is an anchor ...' (l. 1562-1571), the paragraph after the bins (l. 1578-1585) and the Table 5.7 caption, and the crop caveat is stated three times. Gather the differences (cohort, input, crop, visit sets, growth-rate definition) in one paragraph before or directly after the two tables, and let the captions say only 'see text'.
- §5.6.1 l. 1569: 'The paper defines the growth rate as ...' ends the caveat paragraph without saying whether it marks a match or a difference with the definition used here (l. 1475-1481). It belongs in the definition paragraph, next to the formula.
- §5.6.1 l. 1557: the sentence on the other arms follows \end{figure} after a blank line (l. 1541), so it renders as a one-sentence paragraph cut off from the interpretation paragraph it completes (ending at l. 1538). Move the figure environment below it or remove the paragraph break.
- §5.7: the scope facts (one RTX A6000, 30 epochs, order-of-magnitude only, inference time and memory not measured) are split between the end of paragraph 1 and the end of paragraph 4. Collect them at the start of the section so that the section can end on the cost-versus-benefit reading.
- §5.7 l. 1645-1653: the paragraph announces 'Three ratios' and then gives four numbers (RK4 over the stencil, RK4 over the FNO, T-FEN, dual branch), with the FNO value showing that the wrapper ratio depends on the operator. The project documents list the three estimator-independent ratios as RK4/Euler (about 4.8x), T-FEN/stencil (about 4x) and dual/single (about 10x). Say what they are independent of (the minimum vs the mean epoch time) and present the FNO value as a contrast, not as a member of the set.

### Recurring tells in this part

- Colon reveals that set up a statement and deliver it after a colon (roughly half of the 28 colons in rendered prose): 'The gain sits where the defect was: on lesions that touch ...'; 'There is no single vector field $g(u)$ to converge to: the canonical network is ...'. Turn most of them into two plain sentences or a semicolon.
- Personified abstractions (~9): 'They decide which statements ... are licensed', 'This invites reading', 'Two criteria make this operational', '$r$ asks whether', 'AUC asks whether', 'The gain sits', 'The comparison mainly shows', 'does not decide the accuracy', 'the gap belongs to the approach'. Use 'measures', 'indicates', 'is concentrated', 'determine', or a concrete subject.
- 'X, not Y' antitheses used as closers (~4-5): 'owes this to its transport term ..., not to the continuous-time property'; 'an anchor, not a head-to-head result' (text and Table 5.6 caption); 'belongs to the approach, not to one operator'. One per section is fine; three within §5.6.1 reads formulaic.
- Aphoristic summary sentences that restate the paragraph (~3): 'The continuous-time property can therefore be obtained on this task, but it does not decide the accuracy.'; 'most of the extra cost bought nothing measurable'; 'so the gap belongs to the approach'.
- Short teaser or staged-reveal sentences (~4): 'The reason is structural.', 'A small residual remains, and it has a different cause.', 'The mean is not used.', '... was not the cause. The cause was ...'. Merge them into the neighbouring sentence.
- Mirrored parallel pairs (~6): 'Over the dilated-stencil network, where ... / Over the FNO, whose ...'; '... start from ..., whereas ... / ... reports no cropping ..., whereas ...'; 'The first is ... The second is ...'; 'later than the one-year anchor and later than the 360 days'; the '$r$ asks ...: 1 is ..., 0 is ...' / 'AUC asks ...: 0.5 is ..., 1 is ...' pair. Break the symmetry by changing the subject or the form of one half.
- Idioms and competitive metaphors (~7): 'bought nothing measurable', 'ties', 'is ahead', 'did not help', 'go further', 'head-to-head' (3x, incl. Table 5.7 caption). Use plain verbs such as 'is level with', 'performs better', 'did not remove'.
- Participial and gerund openers (~3), one of them dangling: 'Reading back the Courant number ..., the layer channels stay ...' (dangling); 'Tracing the rollouts step by step showed ...'; 'Set against the results of this chapter, most of the extra cost ...'. Use passive clauses with the real subject.
- 'anchor' used as a metaphor ('the values are an anchor', 'The comparison is an anchor') in a range where 'anchor' is otherwise the technical name of the one-year evaluation point (8 uses in the range). Use 'point of reference'.
- Appositive stacking: several comma-separated qualifiers in one sentence (~6), e.g. 'at most 26 values per eye and at most 36 in normalised units, starting around day 1\,260 and growing by ...'; 'every setting except the single Euler step, the crudest one, lies within ...'.

## Findings

### 5d.1 [low] §5.5 Validity Diagnostics (introduction)

`05-experiments.tex:1165` · GPTZero: AI · flow, clarity, ai-tone

> The two diagnostics of this section are not accuracy numbers. They decide which statements about the operators are licensed. The first tests whether a trained operator can be read as a continuous-time system; the second shows why the first version of the T-FEN was not a stable free-running model, and how the energy-conserving form fixes it.

**Issue.** The section opens with a category slip (a diagnostic is not a number) and a personified 'They decide'. It then gives a symmetric 'The first ...; the second ...' pair and the informal 'fixes it'. The first two sentences were judged human, the third AI.

**Suggestion.**

> The two diagnostics of this section do not measure accuracy; they determine which statements about the operators are admissible. The first (\S\ref{sec:experiments:validity:swap}) tests whether a trained operator can be read as a continuous-time system. The second (\S\ref{sec:experiments:validity:tfen}) shows why the first version of the T-FEN was not a stable free-running model and how the energy-conserving form corrects it.

### 5d.2 [low] §5.5.1 The Solver-Swap Test, 'What is tested'

`05-experiments.tex:1175` · GPTZero: AI · clarity, ai-tone

> The update of the framework, $u_t + \Delta t \cdot f_\theta$, has the form of one explicit Euler step (\S\ref{sec:method:dt-residual}), and the Runge--Kutta wrapper and the Finite Element Network go further and integrate $f_\theta$ over several sub-steps (\S\ref{sec:method:family:rk}, \S\ref{sec:method:family:fen}). This invites reading $f_\theta$ as the right-hand side of an ordinary differential equation $\mathrm{d}u/\mathrm{d}t = g(u)$, in the sense of a Neural ODE \citep{Chen2018}: a vector field that states how the state changes at every moment.

**Issue.** A long compound sentence with three references is followed by a personified 'This invites reading' and a colon appositive that repeats 'state' ('states how the state changes'). 'Go further' is conversational.

**Suggestion.**

> The update of the framework, $u_t + \Delta t \cdot f_\theta$, has the form of one explicit Euler step (\S\ref{sec:method:dt-residual}). The Runge--Kutta wrapper and the Finite Element Network integrate $f_\theta$ over several sub-steps instead (\S\ref{sec:method:family:rk}, \S\ref{sec:method:family:fen}). This suggests reading $f_\theta$ as the right-hand side of an ordinary differential equation $\mathrm{d}u/\mathrm{d}t = g(u)$ in the sense of a Neural ODE \citep{Chen2018}, that is, as a vector field that gives the rate of change of the state at every moment.

### 5d.3 [low] §5.5.1 The Solver-Swap Test, 'What is tested'

`05-experiments.tex:1186` · GPTZero: AI · flow, clarity

> A network trained with one fixed discretisation need not have this property. It can fit the observed data while its output depends on the discretisation it was trained with \citep{Ott2021, Krishnapriyan2023}. The solver-swap test determines which of the trained models have the property, and therefore for which models statements about continuous-time behaviour are admissible.

**Issue.** The argument repeats §4.3.7 ('Jump and continuous time', 04-method.tex l. 863-881) without a back-reference, and the last clause ('and therefore for which models statements about ... are admissible') is awkward.

**Suggestion.**

> As discussed in \S\ref{sec:method:family:rk}, a network trained with one fixed discretisation need not have this property. It can fit the observed data while its output depends on the discretisation used in training \citep{Ott2021, Krishnapriyan2023}. The solver-swap test determines which of the trained models have the property, and thus for which of them statements about continuous-time behaviour are admissible.

### 5d.4 [**HIGH**] §5.5.1 The Solver-Swap Test, criterion C2

`05-experiments.tex:1204` · GPTZero: human · clarity

> \textbf{C2, agreement:} all settings at least as fine as the one used in training, by step or by order, agree to within the run-to-run noise, the standard deviation of 0.0127 between repeated runs of one configuration (\S\ref{sec:experiments:protocol:stats}).

**Issue.** 'At least as fine ..., by step or by order' can be read as 'finer in step or in order'. Under that reading, the single Euler step of the RK4-trained network (same step, lower order, -0.0201 in Table 5.4) belongs to the C2 set and exceeds 0.0127, so the network would fail although the text says it passes. Only the 'in both step and order' reading matches the results. The Table 5.4 caption ('for all settings at least as fine as its training setting (C2)') has the same ambiguity.

**Suggestion.**

> \textbf{C2, agreement:} all settings that are at least as fine as the training setting in both step and order agree to within the run-to-run noise, that is, the standard deviation of 0.0127 between repeated runs of one configuration (\S\ref{sec:experiments:protocol:stats}). [Apply the same wording to the Table 5.4 caption: '... for all settings at least as fine as its training setting in both step and order (C2).']

### 5d.5 [low] §5.5.1 The Solver-Swap Test, 'Setup'

`05-experiments.tex:1216` · GPTZero: AI · clarity

> As a control, the setting a model was trained with reproduces exactly the change-region Dice recorded at the end of its training.

**Issue.** The sentence merges the control procedure and its outcome into one subject ('the setting ... reproduces'), which reads oddly and hides that the training setting itself was re-evaluated.

**Suggestion.**

> As a control, each model was also evaluated in its training setting; this reproduces exactly the change-region Dice recorded at the end of its training.

### 5d.6 [low] §5.5.1 The Solver-Swap Test, 'Results'

`05-experiments.tex:1235` · GPTZero: AI · tone, ai-tone

> The reason is structural. The operator receives $\Delta t$ as an input, so a smaller step also changes the input on which the operator is conditioned. There is no single vector field $g(u)$ to converge to: the canonical network is a one-step map conditioned on the length of the step, a single jump in the sense of \S\ref{sec:method:family:rk}.

**Issue.** 'The reason is structural.' is a teaser sentence (judged human). The colon reveal in the last sentence was flagged.

**Suggestion.**

> The failure follows from the conditioning of the operator. It receives $\Delta t$ as an input, so a smaller step also changes the input on which it is conditioned. There is therefore no single vector field $g(u)$ to which the refinements could converge; the canonical network is a one-step map conditioned on the length of the step, a single jump in the sense of \S\ref{sec:method:family:rk}.

### 5d.7 [low] §5.5.1 The Solver-Swap Test, 'Results'

`05-experiments.tex:1242` · GPTZero: AI · clarity

> Its Euler refinements change the Dice by $+0.018$ and then by $+0.004$ (C1), and every setting except the single Euler step, the crudest one, lies within 0.0044 of the others; the three RK4 settings agree to within 0.0005 (C2).

**Issue.** Three findings are packed into one sentence with an appositive ('the crudest one') and a semicolon; 'crudest' is informal.

**Suggestion.**

> Its Euler refinements change the Dice by $+0.018$ and then by $+0.004$ (C1). Apart from the single Euler step, the coarsest setting, all settings lie within 0.0044 of one another, and the three RK4 settings agree to within 0.0005 (C2).

### 5d.8 [low] §5.5.1 The Solver-Swap Test, paragraph labels

`05-experiments.tex:1250` · GPTZero: AI · tone, clarity

> \paragraph{What follows.}

**Issue.** 'What follows' can be read as 'what comes next in the text', and the run-in label is more conversational than 'Setup' or 'Results'.

**Suggestion.**

> \paragraph{Implications.} [Optionally also rename \paragraph{What is tested.} at l. 1174 to \paragraph{Purpose.}]

### 5d.9 [low] §5.5.1 The Solver-Swap Test, 'What follows'

`05-experiments.tex:1251` · GPTZero: AI · clarity, ai-tone

> The canonical network, and with it every headline result, may not be described as a continuous-time model: no statement about an ordinary differential equation, a learned rate of growth or learned dynamics is made for it.

**Issue.** 'Every headline result' is made the subject of 'described as a continuous-time model' (a result is not a model), and the singular 'for it' then leaves the results out. The colon reveal is a recurring tell.

**Suggestion.**

> The canonical network may therefore not be described as a continuous-time model, and no statement about an ordinary differential equation, a learned rate of growth or learned dynamics is made for it or for any headline result.

### 5d.10 [medium] §5.5.1 The Solver-Swap Test, 'What follows'

`05-experiments.tex:1256` · GPTZero: AI · clarity, ai-tone

> The network trained inside the Runge--Kutta wrapper is not more accurate than the canonical network (\S\ref{sec:experiments:ablations:time}). The T-FEN lies slightly above it, at the noise level (\S\ref{sec:experiments:main-results}), and owes this to its transport term (\S\ref{sec:experiments:ingredients:transport}), not to the continuous-time property. The continuous-time property can therefore be obtained on this task, but it does not decide the accuracy.

**Issue.** 'Above it' is ambiguous: the preceding sentence names both the RK4-trained network (subject) and the canonical network. 'Owes this to ..., not to ...' is a personified antithesis, and the closing sentence is an aphoristic restatement with a personified 'decide'.

**Suggestion.**

> The network trained inside the Runge--Kutta wrapper is not more accurate than the canonical network (\S\ref{sec:experiments:ablations:time}). The T-FEN lies slightly above the canonical network, at the noise level (\S\ref{sec:experiments:main-results}); this margin comes from its transport term (\S\ref{sec:experiments:ingredients:transport}) and not from the continuous-time property. On this task, the continuous-time property can thus be obtained, but it does not determine the accuracy.

### 5d.11 [low] Table 5.4 caption (solver-swap test)

`05-experiments.tex:1275` · GPTZero: AI · clarity

> the values are the change-region Dice at the one-year anchor and its difference to the setting the model was trained with.

**Issue.** 'Difference to' is a Germanism ('difference from'), and 'the setting the model was trained with' is wordy next to the column header 'vs. trained'.

**Suggestion.**

> the values are the change-region Dice at the one-year anchor and its difference from the training setting.

### 5d.12 [low] Figure 5.7 caption (solver-swap test against the step size)

`05-experiments.tex:1323` · GPTZero: AI · clarity *(added in verification)*

> Each trained model is re-evaluated without retraining with explicit Euler (solid, filled circles) or classical RK4 (dotted, open squares) at a changed step.

**Issue.** Garden path: 'without retraining with explicit Euler' first reads as 'without retraining-with-Euler'. The Table 5.4 caption sets the same phrase off with commas.

**Suggestion.**

> Each trained model is re-evaluated, without retraining, with explicit Euler (solid, filled circles) or classical RK4 (dotted, open squares) at a changed step.

### 5d.13 [low] Figure 5.7 caption (solver-swap test against the step size)

`05-experiments.tex:1327` · GPTZero: AI · clarity

> the vertical axis gives the change of the change-region Dice at the one-year anchor against the trained setting (ring).

**Issue.** The bare '(ring)' at the end of a long clause does not say that it names a marker.

**Suggestion.**

> the vertical axis gives the change of the change-region Dice at the one-year anchor against the trained setting, which is marked by a ring.

### 5d.14 [medium] §5.5.2 Numerical Stability of the T-FEN, 'The first version'

`05-experiments.tex:1349` · GPTZero: AI · clarity, ai-tone

> Tracing the rollouts step by step showed where the divergence comes from. It starts at the edge of the crop, in a layer channel, driven by the transport term, and only after about 1.6 to 2 years: later than the one-year anchor and later than the 360 days that training unrolls.

**Issue.** The second sentence stacks four qualifiers before a colon reveal and ends in a mirrored 'later than ... and later than ...' pair.

**Suggestion.**

> Step-by-step tracing of the rollouts located the onset of the divergence. It starts at the edge of the crop, in a layer channel, is driven by the transport term, and appears only after about 1.6 to 2 years, beyond both the one-year anchor and the 360 days unrolled in training.

### 5d.15 [medium] §5.5.2 Numerical Stability of the T-FEN, 'The first version'

`05-experiments.tex:1352` · GPTZero: AI · tone, ai-tone

> A smaller step did not help, and the velocities at the onset were within the stability limit of RK4, so the step size was not the cause. The cause was the defect of the Galerkin operator at the domain edge described in~\S\ref{sec:method:family:fen}.

**Issue.** 'Did not help' is conversational. '... was not the cause. The cause was ...' is a staged anadiplosis.

**Suggestion.**

> A smaller step did not remove the divergence, and the velocities at the onset were within the stability limit of RK4, which rules out the step size as the cause. The divergence arises instead from the defect of the Galerkin operator at the domain edge described in~\S\ref{sec:method:family:fen}.

### 5d.16 [**HIGH**] §5.5.2 Numerical Stability of the T-FEN, 'The energy-conserving form'

`05-experiments.tex:1375` · GPTZero: AI · clarity, flow

> Its accuracy is at least as good: $0.5428 \pm 0.0401$ against $0.5337 \pm 0.0453$ for the Galerkin form, higher on all five folds, by $+0.009$, which is under the noise level.

**Issue.** The sentence directly follows the seed-7 replication, so 'Its accuracy' reads as the accuracy of the seed-7 run, although the numbers are the seed-42 comparison (0.5428 is the seed-42 value of Table 5.1).

**Suggestion.**

> At seed 42, the energy-conserving form is at least as accurate as the Galerkin form: $0.5428 \pm 0.0401$ against $0.5337 \pm 0.0453$, higher on all five folds, by $+0.009$, which is under the noise level. [Alternatively, move the seed-7 sentence after this one.]

### 5d.17 [medium] §5.5.2 Numerical Stability of the T-FEN, 'The energy-conserving form'

`05-experiments.tex:1378` · GPTZero: AI · tone, ai-tone, clarity

> The gain sits where the defect was: on lesions that touch the crop border the change-region Dice rises from 0.516 to 0.544, while interior lesions are unchanged (0.535 and 0.536), and the growth-region Dice beyond three years rises from 0.537 to 0.611.

**Issue.** 'The gain sits where the defect was:' is a personified, slightly literary colon reveal. It is followed by a three-part sentence that mixes a contrast and an addition.

**Suggestion.**

> The difference is concentrated where the defect was located. On lesions that touch the crop border, the change-region Dice rises from 0.516 to 0.544, whereas interior lesions are unchanged (0.535 and 0.536); beyond three years, the growth-region Dice rises from 0.537 to 0.611.

### 5d.18 [medium] §5.5.2 Numerical Stability of the T-FEN, residual

`05-experiments.tex:1386` · GPTZero: AI · clarity, tone, ai-tone

> A small residual remains, and it has a different cause. Reading back the Courant number over every sub-step of the free-running rollout on fold 0, the layer channels stay at or below 1.36, inside the RK4 limit of about 2.4, but the mask channel lies slightly above it at the 45-day training step (median 2.64, maximum 2.85).

**Issue.** The opener is a teaser sentence, and 'a small residual' does not say of what. The second sentence has a dangling participle: the layer channels do not 'read back' anything. A pointer to where the Courant number is defined (§4.3.6) would help.

**Suggestion.**

> A small residual effect remains, with a different cause. The Courant number (\S\ref{sec:method:family:fen}) was read back over every sub-step of the free-running rollout on fold 0. On the layer channels it stays at or below 1.36, inside the RK4 limit of about 2.4, but on the mask channel it lies slightly above this limit at the 45-day training step (median 2.64, maximum 2.85).

### 5d.19 [medium] §5.5.2 Numerical Stability of the T-FEN, residual

`05-experiments.tex:1390` · GPTZero: AI · clarity

> In 9 of the 20 validation eyes a few mask values on the top or bottom row of the grid eventually leave the plausible range, at most 26 values per eye and at most 36 in normalised units, starting around day 1\,260 and growing by a factor of about 1.04 per sub-step.

**Issue.** Four trailing qualifiers hang off one clause. 'At most 26 values per eye and at most 36 in normalised units' puts a count and a magnitude in one mirrored phrase, so it is unclear what the 36 refers to.

**Suggestion.**

> In 9 of the 20 validation eyes, a few mask values on the top or bottom row of the grid eventually leave the plausible range: at most 26 values per eye, reaching at most 36 in normalised units. The excursion starts around day 1\,260 and grows by a factor of about 1.04 per sub-step.

### 5d.20 [medium] §5.5.2 Numerical Stability of the T-FEN, residual

`05-experiments.tex:1394` · GPTZero: AI · clarity

> This is the step-size limit of RK4, now a minor effect compared with the defect of the Galerkin form, which produced growth by a factor of about 1.3 per sub-step from around day 585. It does not affect the stability criterion, which the run passes, and an evaluation step of 30 days, at which the Courant number of the mask channel falls to about 1.8, removes it without changing the Dice (\S\ref{sec:experiments:validity:swap}).

**Issue.** 'This is the step-size limit' equates an observed excursion with a limit. The second sentence joins two unrelated statements with 'and' and nests a relative clause, so 'it' has several possible referents.

**Suggestion.**

> This excursion reflects the step-size limit of RK4 and is minor compared with the defect of the Galerkin form, which produced growth by a factor of about 1.3 per sub-step from around day 585. The run still passes the stability criterion, and an evaluation step of 30 days, at which the Courant number of the mask channel falls to about 1.8, removes the excursion without changing the Dice (\S\ref{sec:experiments:validity:swap}).

### 5d.21 [low] Table 5.5 caption (stability of the T-FEN)

`05-experiments.tex:1412` · GPTZero: AI · clarity

> For each fold: the number of late epochs (10 to 29) on which the free-running mask and layer errors stay at or below 5, and the largest late-epoch mask and layer error, in normalised units.

**Issue.** The caption does not say which error is meant (Figure 5.8 and §4.3.6 specify root mean squared error), so the table is not self-contained.

**Suggestion.**

> For each fold: the number of late epochs (10 to 29) on which the root mean squared errors of the free-running mask and layer predictions stay at or below 5, and the largest late-epoch value of each, in normalised units.

### 5d.22 [medium] §5.6 Qualitative Analysis and Clinical Comparison (heading)

`05-experiments.tex:1459` · GPTZero: unmarked · flow

> \section{Qualitative Analysis and Clinical Comparison}

**Issue.** The section follows a Courant-number detail of §5.5.2 with no transition and opens directly with its only subsection. The qualitative half of the title has no content yet (TODO), so the reader finds only the Mai comparison.

**Suggestion.**

> Insert under the section heading, before \subsection: 'The preceding sections compare the operators within the framework. This section compares the results with a published study of GA progression from OCT.' Until the qualitative part is written, keep this bridge neutral so that it does not promise per-eye analyses.

### 5d.23 [**HIGH**] §5.6.1 Comparison with Mai et al. (2024), definition of r

`05-experiments.tex:1482` · GPTZero: human · clarity

> The Pearson correlation $r$ asks whether the model orders and scales the growth speeds of the eyes correctly: $r = 1$ is a perfect linear relation and $r = 0$ no relation.

**Issue.** Pearson $r$ does not depend on scale: a model that predicts half of every true rate still reaches $r = 1$. 'Scales ... correctly' therefore misdescribes the metric, and 'orders' fits a rank correlation better. This matters a few lines later, where the fastest eyes are predicted at about half their true rate. '$r = 0$ no relation' should read 'no linear relation'.

**Suggestion.**

> The Pearson correlation $r$ measures how closely the predicted rates follow a linear relation with the true rates across eyes; it does not require the two to agree in scale: $r = 1$ is a perfect linear relation and $r = 0$ no linear relation.

### 5d.24 [low] §5.6.1 Comparison with Mai et al. (2024), definition of the AUC

`05-experiments.tex:1485` · GPTZero: human · ai-tone, clarity

> The fast-progressor area under the receiver operating characteristic curve (AUC) asks whether the predicted rate separates the fastest-growing eyes, the top 10, 15 or 20\,\% of true growth rates, from the rest: 0.5 is chance and 1 is perfect separation.

**Issue.** The sentence mirrors the $r$ sentence exactly ('... asks whether ...: a is ..., b is ...'), and the embedded appositive splits 'separates ... from the rest'.

**Suggestion.**

> The fast-progressor area under the receiver operating characteristic curve (AUC) measures how well the predicted rate separates the fastest-growing eyes (the top 10, 15 or 20\,\% of true growth rates) from the rest: 0.5 is chance and 1 is perfect separation.

### 5d.25 [medium] Table 5.6 caption (growth-speed measures against Mai et al.)

`05-experiments.tex:1503` · GPTZero: AI · clarity, tone, ai-tone

> The two studies differ in cohort size, input and the area over which lesions are measured (see text), so the values are an anchor, not a head-to-head comparison.

**Issue.** 'Anchor' is the technical name of the one-year evaluation point throughout the chapter, so 'the values are an anchor' is ambiguous. 'Head-to-head' is a sports idiom, and 'X, not Y' is a recurring closer.

**Suggestion.**

> The two studies differ in cohort size, input and the area over which lesions are measured (see text), so the values serve as a point of reference and not as a direct comparison.

### 5d.26 [medium] §5.6.1 Comparison with Mai et al. (2024), interpretation

`05-experiments.tex:1530` · GPTZero: AI · clarity, tone, ai-tone

> The canonical model captures growth-speed information (Figure~\ref{fig:experiments:growth-rate}): its correlation is clearly above zero, whereas the baseline lesion size alone is not correlated with the growth rate in this cohort ($r = -0.10$).

**Issue.** 'Captures growth-speed information' is vague, 'clearly' is an intensifier, and the colon reveal is a recurring tell. The basis for 'above zero' (the bootstrap interval in Table 5.6) is not named.

**Suggestion.**

> The predicted growth rates of the canonical model are correlated with the true ones (Figure~\ref{fig:experiments:growth-rate}): $r$ is positive and its bootstrap interval excludes zero, whereas the baseline lesion size alone is not correlated with the growth rate in this cohort ($r = -0.10$).

### 5d.27 [low] §5.6.1 Comparison with Mai et al. (2024), interpretation

`05-experiments.tex:1536` · GPTZero: AI · clarity

> The fastest eyes are under-predicted: of the 15 eyes with the highest true rates, 14 receive a lower predicted rate, about half the true rate in the median.

**Issue.** 'About half the true rate in the median' is a clumsy trailing phrase; it is not clear that it is the median ratio of predicted to true rate.

**Suggestion.**

> The fastest eyes are under-predicted: of the 15 eyes with the highest true rates, 14 receive a lower predicted rate, with a median ratio of predicted to true rate of about one half.

### 5d.28 [medium] §5.6.1 Comparison with Mai et al. (2024), other arms

`05-experiments.tex:1557` · GPTZero: AI · flow, ai-tone

> The other arms of the survey do not differ from the canonical model on these measures ($r$ between 0.30 and 0.47, fast-progressor AUCs between 0.66 and 0.78; Table~\ref{tab:appendix:growth-speed}), so the gap belongs to the approach, not to one operator.

**Issue.** The closer 'belongs to the approach, not to one operator' is a personified 'X, not Y' aphorism, and 'the approach' is not defined. Because of the blank line before the figure (l. 1541), the sentence renders as a one-sentence paragraph, separated from the interpretation paragraph it completes.

**Suggestion.**

> Join it to the paragraph ending at l. 1538 (move the figure environment below it) and write: The other arms of the survey do not differ from the canonical model on these measures ($r$ between 0.30 and 0.47, fast-progressor AUCs between 0.66 and 0.78; Table~\ref{tab:appendix:growth-speed}); the gap to \citet{Mai2024} is therefore common to every operator and lies in the shared approach.

### 5d.29 [medium] §5.6.1 Comparison with Mai et al. (2024), caveats

`05-experiments.tex:1562` · GPTZero: AI · clarity, tone, ai-tone

> The comparison is an anchor, not a head-to-head result.

**Issue.** This repeats the caption metaphor almost word for word: it again collides with the technical 'one-year anchor' and uses a sports idiom in a short antithetical topic sentence.

**Suggestion.**

> The values of \citet{Mai2024} serve only as a point of reference, since the two studies differ in several respects.

### 5d.30 [low] §5.6.1 Comparison with Mai et al. (2024), caveats

`05-experiments.tex:1565` · GPTZero: AI · ai-tone

> \citet{Mai2024} start from the raw OCT volume, whereas this thesis starts from segmented masks and layer depths. Their paper reports no cropping of the areas, whereas the areas here are measured inside the $49 \times 1024$ crop, which censors growth at its border (\S\ref{sec:data:spatial}).

**Issue.** Two consecutive sentences use the same '..., whereas this thesis/here ...' template, a mirrored pair.

**Suggestion.**

> \citet{Mai2024} start from the raw OCT volume; this thesis starts from segmented masks and layer depths. Their paper reports no cropping of the areas, while the areas here are measured inside the $49 \times 1024$ crop, which censors growth at its border (\S\ref{sec:data:spatial}).

### 5d.31 [medium] §5.6.1 Comparison with Mai et al. (2024), caveats

`05-experiments.tex:1569` · GPTZero: human · flow, clarity

> The paper defines the growth rate as the difference between the square roots of the baseline and the respective follow-up area.

**Issue.** The sentence ends a list of differences between the studies but does not say whether it marks a difference from or a match with the definition used here (l. 1475-1481), so the reader cannot tell why it is there.

**Suggestion.**

> Move it into the definition paragraph, directly after the formula, as '\citet{Mai2024} define the growth rate as the difference between the square roots of the baseline and the respective follow-up area.' If it is meant as a difference (each follow-up visit vs the eye's last visit), state the contrast in the same sentence instead.

### 5d.32 [low] §5.6.1 Comparison with Mai et al. (2024), growth-region Dice

`05-experiments.tex:1577` · GPTZero: AI · clarity, flow *(added in verification)*

> All three operators lie above the values of \citet{Mai2024} in every bin, by 0.18 to 0.29.

**Issue.** 'All three operators' appears without antecedent; the preceding paragraphs speak of 'the canonical model' and 'the other arms', and the three are named only in the column headers of Table 5.7.

**Suggestion.**

> The dilated-stencil network, the U-Net and the T-FEN all lie above the values of \citet{Mai2024} in every bin, by 0.18 to 0.29.

### 5d.33 [low] §5.6.1 Comparison with Mai et al. (2024), growth-region Dice

`05-experiments.tex:1579` · GPTZero: AI · flow, clarity

> The models of this thesis receive the segmented baseline lesion as input, so its outline is given exactly, whereas \citet{Mai2024} must first find the lesion in the raw OCT volume. The areas here are measured inside the crop, and the two studies evaluate different sets of visits.

**Issue.** '\citet{Mai2024} must first find the lesion' makes the authors, not their model, the agent. The crop caveat is stated here for the third time (Table 5.6 caption, l. 1566-1569).

**Suggestion.**

> The models of this thesis receive the segmented baseline lesion as input, so its outline is given exactly, whereas the model of \citet{Mai2024} must first locate the lesion in the raw OCT volume. The areas here are measured inside the crop, and the two studies evaluate different sets of visits. [Drop the crop clause only if the caveats are consolidated as proposed in the flow notes.]

### 5d.34 [medium] §5.6.1 Comparison with Mai et al. (2024), growth-region Dice

`05-experiments.tex:1583` · GPTZero: AI · tone, ai-tone

> The comparison mainly shows how much of the spatial forecast the segmented mask already carries; on growth speed, where the mask helps less, the model of \citet{Mai2024} is ahead.

**Issue.** This is a personified summary closer ('the comparison shows', 'the mask carries', 'the mask helps') joined by a semicolon and ending on the race idiom 'is ahead'.

**Suggestion.**

> The comparison therefore mainly indicates how much of the spatial forecast is already contained in the segmented mask. On growth speed, where the mask is of less help, the model of \citet{Mai2024} performs better.

### 5d.35 [low] Table 5.7 caption (growth-region Dice against Mai et al.)

`05-experiments.tex:1596` · GPTZero: AI · tone *(added in verification)*

> so the values are not a head-to-head comparison.

**Issue.** This is the third use of the sports idiom 'head-to-head' in §5.6.1 (with the Table 5.6 caption and l. 1562).

**Suggestion.**

> so the values do not form a direct comparison.

### 5d.36 [low] §5.7 Computational Cost

`05-experiments.tex:1622` · GPTZero: AI · clarity, flow

> The cost of an arm is reported as its minimum epoch time over the five folds. The mean is not used. The epoch times of a run carry a nearly constant additive overhead of 17 to 64~s, which would penalise cheap operators far more than expensive ones.

**Issue.** 'The mean is not used.' is a choppy standalone sentence whose reason only follows in the next sentence.

**Suggestion.**

> The cost of an arm is reported as its minimum epoch time over the five folds and not as the mean, because the epoch times of a run carry a nearly constant additive overhead of 17 to 64~s, which would penalise cheap operators far more than expensive ones.

### 5d.37 [low] §5.7 Computational Cost

`05-experiments.tex:1625` · GPTZero: AI · clarity, ai-tone

> The spread between folds has two measured causes. The first is this overhead. The second is that the work per epoch differs between folds: an epoch is twenty passes over the fold's training eyes in batches of four, which gives 280, 320, 300, 300 and 320 optimiser steps for folds 0 to 4.

**Issue.** 'The spread' does not say of what (epoch times). The 'The first is ... The second is ...:' enumeration is mechanical.

**Suggestion.**

> The epoch times differ between folds for two measured reasons: this overhead and a different amount of work per epoch. An epoch consists of twenty passes over the fold's training eyes in batches of four, which gives 280, 320, 300, 300 and 320 optimiser steps for folds 0 to 4.

### 5d.38 [medium] §5.7 Computational Cost

`05-experiments.tex:1630` · GPTZero: AI · flow, tone

> An earlier explanation of the spread by several runs sharing one GPU was checked and does not hold: no two runs ever shared a GPU. All runs used one NVIDIA RTX A6000 GPU and 30 epochs.

**Issue.** 'An earlier explanation' refers to project history the reader never saw, which tells the story of the project and does not report a result. The hardware sentence is setup information placed after the analysis.

**Suggestion.**

> Runs sharing a GPU can be excluded as a further cause, since no two runs ever shared a GPU. [Move 'All runs used one NVIDIA RTX A6000 GPU and 30 epochs.' to the first sentence of the section.]

### 5d.39 [low] §5.7 Computational Cost

`05-experiments.tex:1636` · GPTZero: AI · clarity

> On this scale, the U-Net is the cheapest spatial operator at 21~s per epoch, about $0.23\times$ the 91~s of the canonical dilated-stencil graph network.

**Issue.** 'On this scale' could refer to the time scale or to the order-of-magnitude precision just stated.

**Suggestion.**

> Within this precision, the U-Net is the cheapest spatial operator at 21~s per epoch, about $0.23\times$ the 91~s of the canonical dilated-stencil graph network.

### 5d.40 [medium] §5.7 Computational Cost

`05-experiments.tex:1640` · GPTZero: AI · clarity

> The Finite Element Networks are the most expensive single-step family: 180~s for the free-form network and 367~s for the T-FEN (Table~\ref{tab:experiments:arms}).

**Issue.** 'Single-step' conflicts with §4.3.6/§5.5.1, where the FENs are always integrated with RK4 in 45-day sub-steps; elsewhere (l. 455, 1657) 'single-step' means one Euler step. The intended exclusion appears to be the RK4-wrapped graph network (439 s).

**Suggestion.**

> Apart from the graph network inside the RK4 wrapper, the Finite Element Networks are the most expensive arms: 180~s for the free-form network and 367~s for the T-FEN (Table~\ref{tab:experiments:arms}). [If 'single-step' was meant differently, name the intended class explicitly.]

### 5d.41 [medium] §5.7 Computational Cost

`05-experiments.tex:1645` · GPTZero: AI · flow, clarity

> Three ratios do not depend on the fine details of the timing.

**Issue.** The topic sentence promises three timing-independent ratios. The paragraph then gives four numbers and shows with the FNO that the wrapper ratio changes with the operator because of the fixed overhead, which reads as a contradiction. It does not say which 'details' are meant.

**Suggestion.**

> Replace with: 'Three cost ratios hardly change whether the minimum or the mean epoch time is used.' Then let the three ratios be the RK4 wrapper over the dilated-stencil network (about $4.8\times$), the T-FEN against that network (about $4\times$) and the dual branch against its single-branch counterpart (about $10\times$), and introduce the FNO value as a contrast (see the next finding).

### 5d.42 [low] §5.7 Computational Cost

`05-experiments.tex:1649` · GPTZero: AI · clarity, ai-tone

> Over the FNO, whose forward pass is cheap, it raises it only from 23 to 45~s, about $2\times$, because the fixed part of the epoch weighs more.

**Issue.** In 'it raises it' the two pronouns refer to different things. The sentence also mirrors the preceding 'Over the dilated-stencil network, where ...' sentence clause for clause.

**Suggestion.**

> For the FNO, whose forward pass is cheap, the wrapper raises the epoch time only from 23 to 45~s, about $2\times$, because the fixed part of the epoch carries more weight.

### 5d.43 [medium] §5.7 Computational Cost

`05-experiments.tex:1655` · GPTZero: AI · tone, ai-tone

> Set against the results of this chapter, most of the extra cost bought nothing measurable.

**Issue.** 'Bought nothing measurable' is a conversational, slightly dramatic idiom used as a verdict-style topic sentence.

**Suggestion.**

> Measured against the results of this chapter, most of the additional cost brought no measurable improvement.

### 5d.44 [low] §5.7 Computational Cost

`05-experiments.tex:1660` · GPTZero: AI · tone, clarity

> The T-FEN is the one expensive arm with an established effect, its transport term, but at the anchor it ties the dilated-stencil network, which reaches the same level at about a quarter of the cost.

**Issue.** 'The one ... arm' (for 'the only') and the sports verb 'ties' are informal, and the appositive 'its transport term' makes the term itself the 'effect'.

**Suggestion.**

> The T-FEN is the only expensive arm with an established effect, that of its transport term; at the one-year anchor, however, it is level with the dilated-stencil network, which costs about a quarter as much.

### 5d.45 [low] §5.7 Computational Cost

`05-experiments.tex:1663` · GPTZero: AI · flow

> Inference time per rollout step and memory footprint were not measured.

**Issue.** This scope statement closes the chapter after the cost-versus-benefit reading, so the chapter ends on a limitation that belongs with the definition of what was measured.

**Suggestion.**

> Move it to the first paragraph after the hardware sentence, e.g. 'All runs used one NVIDIA RTX A6000 GPU and 30 epochs; inference time per rollout step and memory footprint were not measured.' The section then ends on the T-FEN sentence.

