# Micro feedback 4a: Ch. 4 Method, §4.1 Overview, §4.2 Fixed Framework, §4.3.1-4.3.2 (contract, GNN)

[← Overview](00-overview.md)

37 findings: 0 high, 21 medium, 16 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

The first half of Chapter 4 is logically sound and its order works. §4.1 motivates a controlled comparison, §4.2 sets out the shared parts, and §4.3.1-4.3.2 give the operator contract and the GNN. The GNN part follows a clear "original, then adaptation, then differences" pattern. The main structural weakness is repetition, not missing links. Several facts are restated in two to four places across §4.1, §4.2.1, the §4.3 intro, §4.3.1 and §4.3.2: the single shared pipeline, the zero-initialised head that gives a persistence start, the absence of batch statistics, the original's convolutional decoder and the per-channel prediction. The operators are also listed three times within about three pages. Together these restatements slow the reader and give the prose the even, self-summarising rhythm that GPTZero picks up. Two places are more likely to confuse. The first is the "Two reasons support this design" paragraph in §4.2: its second reason is a separate decision about the output (no temporal bundling), not a reason for the one-visit input. The second is the central term "arm", which is used from §4.1 onwards without a definition; its only earlier use in the thesis is the sample and reference arms of the OCT interferometer in §2.1.3. "Backbone", "module", "architecture" and "operator" also name the thing in the slot, and "backbone" returns throughout §4.3.7. In §4.1, the persistence-fingerprint paragraph sits between the operator list and the roadmap. The register is formal and impersonal throughout. The AI tone comes from structure, not vocabulary: announcements, summary closers, sameness words, em-dash triads and runs of short parallel sentences. The passages GPTZero judged human (e.g. the summary of the original MP-PDE, or "No operator uses a normalisation that keeps batch statistics.") show the author's plain declarative voice, and most fixes below reach it by merging and cutting.

### Transitions

- §4.1, paragraph order (l. 39-67): the persistence-fingerprint paragraph (l. 52-55) sits between the operator list and the roadmap and interrupts both. Move it, together with its TODO comment, to the end of the second paragraph (after l. 37), where it serves as evidence that the shared pipeline held. This works only if 'arm' is defined before that point (see the finding at l. 46: define it where the slot is introduced, l. 21-24). 'Figure~\ref{fig:method:pipeline} summarises the pipeline.' (l. 64) can move to the same place, since the pipeline is described in paragraphs 1-2.
- §4.1 -> §4.2: §4.1 lists the loss, curriculum, optimiser, folds, seeds, evaluation and model selection as fixed, but §4.2 then announces only 'the time handling and the tensor layout'. Move the pointer sentence now stranded at l. 115-117 ('The shared loss and curriculum are defined in ...') to directly after the scope sentence of §4.2, so the reader learns at once where the other shared parts are described.
- §4.2, l. 102-112: 'Two reasons support this design' introduces reasons for the one-visit input, but the 'second reason' is a separate design decision on the output side (no temporal bundling). Separate the two (see the finding at l. 102).
- §4.2.1, l. 140-152: one paragraph covers the $\Delta t \to 0$ limit, the persistence prior and the shrinkage/monotonicity question. Start a new paragraph at 'The output of $f_\theta$ is signed and unbounded'.
- Zero-initialisation is stated in full in §4.2.1 (l. 154-157), §4.3.1 (l. 235-236) and §4.3.2 (l. 407-408), and again in Table 4.1. Keep the full statement in §4.2.1 and the table cell. In the two prose restatements, refer back in a clause (e.g. 'its final layer is initialised to zero (\S\ref{sec:method:dt-residual})').
- The batch-statistics argument is made in full in §4.3.1 (l. 241-249). The GNN paragraph (l. 381-388) restates it only briefly and already refers back to the contract, so it can stay; only its 'Before this change' sentence needs rewording (see the finding at l. 384).
- §4.3 intro + roadmap (l. 204-225), together with §4.1 l. 39-48: the operators are listed three times within about three pages. Attach the section references to the property list in l. 206-213, and reduce the roadmap paragraph to one sentence covering the contract (§4.3.1) and the parameter matching (§4.3.8). See the findings at l. 204 and l. 218.
- §4.3.1, third paragraph (l. 251-257): the image-grid input planes concern three operators only, so in a section about the contract for all operators the paragraph can seem out of place. The rewrite at l. 251 names the three operators at the start; alternatively move the paragraph to §4.3.4.
- §4.2.2, l. 188-190: a one-sentence paragraph left over after the view/permute text was removed. Merge it into the preceding layout paragraph.
- §4.3.2 decoder: the original's 1-D convolutional head is described twice (l. 306-309 and l. 399-401), and the new decoder (l. 390-397) is described before the reason it replaced the original head (l. 399-408). Put the reason first and refer back to the earlier description instead of repeating it (see the finding at l. 399).
- §4.3.2 'The architecture used here', l. 369-370: the sentence on $u_i - u_j$ repeats l. 295-297, but it is introduced with 'As in the original' and so works as a deliberate back-reference. It can optionally be shortened.
- Transition §4.3.2 -> §4.3.3 (l. 458-470; l. 470 belongs to the next reviewer's range): the section ends with a recap paragraph, and §4.3.3 opens with 'turns out to be the most consequential design decision', which narrates a result before it is shown. A neutral opener with a forward reference fits the register better, e.g. 'The graph on which messages travel is, as Chapter~\ref{ch:experiments} shows, the most consequential design decision of the graph solver.'
- Terminology across the range: 'backbone' (l. 32), 'module' (l. 236), 'architecture', 'operator' and 'arm' all name the thing in the slot or a setting of it. Define 'arm' once in §4.1 and use 'operator' for $f_\theta$. 'Backbone' is also used throughout §4.3.7 (l. 816-945), so a terminology decision there should be applied consistently.

### Recurring tells in this part

- Restating the same fact in several places: zero-init and the persistence start 3x in prose plus the table; 'one shared pipeline, so differences come from the operator' 3-4x in §4.1, the §4.3 intro and §4.3.1; channels predicted independently 3x; the original's decoder 2x. Fix: state each fact once and refer back elsewhere.
- Paragraph-opening meta-announcements that say what comes next instead of saying it (about 6): 'A further shared choice concerns the input itself.', 'This form has a useful limit.', 'This resemblance to a numerical integrator needs a caution.', 'This subsection covers only how ...', 'This section describes every operator that occupies it.' Fix: drop them or fold them into the next sentence.
- Redundant summary closers that repeat the paragraph's point (about 4): 'A separate pipeline per architecture would reintroduce exactly the confounds the design is meant to remove.', '; the prior rests on slow change alone', 'a difference between these arms reflects the operator, not the information it receives', 'Because all of them run in the same training environment, differences ... can be attributed to the architecture rather than to the training protocol.'
- Repeated sameness words: 'every' 27x, 'same' 12x, 'shared' 11x and 'identical' 5x in about 3,400 words. They give a monotone, insistent rhythm (e.g. 'Every operator satisfies the same interface. It is built from the same metadata ... and it consumes the same batch.').
- Runs of short sentences with identical syntax (3 instances, each 4-8 sentences long): 'A U-Net tests multiscale local detail. A Fourier Neural Operator tests global spectral support ... Two truncated graph networks test ...'; the roadmap '\S X describes ..., \S Y describes ...'; the closing recap 'The X follow from ... The Y replaces ... The Z follow from ...'.
- Em-dash asides wrapping a list of three (all 6 em-dashes in the range): 'It is built from the same metadata --- one time step, eleven state channels and two covariates --- and ...', 'Several of its design decisions --- the time handling, the output layer and the strict one-step prediction --- also became ...'. Fix: parentheses or a colon list at the end of the sentence.
- A semicolon followed by a short comment clause (about 10 of the 42 semicolons): '; the original uses six', '; only the type of normalisation differs', '; removing it hurts most when ...', '; it motivates the moving-mesh extension ...'. Most are acceptable; the ones that end a paragraph read as tacked-on punchlines.
- Cleft and pseudo-cleft constructions (2): 'What the adaptation produced is the setup described in this chapter.', 'This persistent injection is what lets a single trained solver generalise ...'.
- Intensifiers and emphasis markers that the author's style rules exclude (about 6): 'strictly' / 'strict' (l. 105, 269), 'the very perturbation' (l. 245), 'at all' (l. 211), 'tested directly' (l. 166), 'exactly the confounds' (l. 36). 'Exactly one step ($K = 1$)' is precise and can stay.
- Mild agency given to methods: 'A U-Net tests multiscale local detail', 'relieves the network of reproducing the whole state'. These are normal academic usage; only the 'X tests Y' list is conspicuous because of its repetition.

## Findings

### 4a.1 [medium] §4.1 Overview

`04-method.tex:11` · GPTZero: AI · ai-tone, clarity, tone

> The work began as an adaptation of two graph-based neural PDE solvers, MP-PDE and MM-PDE, which the clinical partner had suggested; the case for their local inductive bias was built and tested only afterwards. What the adaptation produced is the setup described in this chapter. It separates the experimental framework from the spatial operators evaluated inside it. The aim is to find out which properties a model needs in order to predict GA progression. Answering that question requires a controlled comparison.

**Issue.** A pseudo-cleft ('What the adaptation produced is ...') followed by three short stand-alone sentences, a semicolon joining the provenance and its consequence, and the informal phrasal verb 'find out'.

**Suggestion.**

> The work began as an adaptation of two graph-based neural PDE solvers, MP-PDE and MM-PDE, which the clinical partner had suggested. The case for their local inductive bias was built and tested only afterwards. The adaptation produced the setup described in this chapter, which separates the experimental framework from the spatial operators evaluated inside it. The aim is to determine which properties a model needs in order to predict GA progression, and answering that question requires a controlled comparison.

### 4a.2 [low] §4.1 Overview

`04-method.tex:21` · GPTZero: AI · ai-tone, flow

> A single pipeline is therefore fixed, and it provides one swappable slot for the update operator $f_\theta$. The operator placed in this slot is the only component that changes between experiments. Everything outside the slot is held fixed.

**Issue.** A mirror pair across the paragraph break: 'the only component that changes' and 'Everything outside the slot is held fixed' state the same point from opposite sides as two short sentences.

**Suggestion.**

> A single pipeline is therefore fixed, and it provides one swappable slot for the update operator $f_\theta$, the only component that changes between experiments. [new paragraph, unchanged] Everything outside the slot is held fixed.

### 4a.3 [low] §4.1 Overview

`04-method.tex:32` · GPTZero: AI · clarity

> A backbone placed in the slot contains architecture only.

**Issue.** 'Backbone' appears only here in §4.1-4.3, while the surrounding text says 'operator' (and also 'module', 'architecture', 'arm'), so a reader may wonder whether a backbone is something different from the operator.

**Suggestion.**

> An operator placed in the slot contains only its architecture.

### 4a.4 [low] §4.1 Overview

`04-method.tex:35` · GPTZero: AI · ai-tone, flow

> A separate pipeline per architecture would reintroduce exactly the confounds the design is meant to remove.

**Issue.** A redundant paragraph closer with an intensifier ('exactly'). It repeats the argument of l. 18-21 ('If every candidate architecture came with its own training pipeline ...').

**Suggestion.**

> Cut the sentence. If it is kept: "A separate pipeline per architecture would reintroduce the confounds described above."

### 4a.5 [low] §4.1 Overview

`04-method.tex:39` · GPTZero: human · clarity

> The operators run through this pipeline are a message-passing graph neural network (GNN) on two different neighbourhood graphs (\S\ref{sec:method:graph}), one of which is the canonical model of this thesis; a U-Net; a Fourier Neural Operator (FNO); and a hybrid Finite Element Network (FEN).

**Issue.** Grammatically, 'one of which' refers to the graphs, but the canonical model is the GNN on one of them. The semicolon list with a nested relative clause is also hard to parse.

**Suggestion.**

> The operators run through this pipeline are a message-passing graph neural network (GNN) on two different neighbourhood graphs (\S\ref{sec:method:graph}), a U-Net, a Fourier Neural Operator (FNO) and a hybrid Finite Element Network (FEN). The GNN on one of the two graphs is the canonical model of this thesis.

### 4a.6 [medium] §4.1 Overview

`04-method.tex:44` · GPTZero: AI · clarity, flow

> A fixed-step Runge--Kutta wrapper can be placed around any of these operators, and a per-pixel model with no spatial context marks the lower floor.

**Issue.** Two unrelated items are joined by 'and'. 'Floor' is used for the first time without explanation, and 'lower floor' implies a second floor (the one-hop floor) that the reader has not met yet.

**Suggestion.**

> A fixed-step Runge--Kutta wrapper can be placed around any of these operators. A per-pixel model with no spatial context sets the lowest reference level, or floor, of the comparison.

### 4a.7 [medium] §4.1 Overview

`04-method.tex:46` · GPTZero: AI · clarity

> The arms are parameter-matched to the canonical configuration's 67\,147 parameters within a narrow band; the matching and its exceptions are described in~\S\ref{sec:method:family:params}.

**Issue.** 'Arm' appears here for the first time in the comparison sense and is never defined. It is the central unit of Chapters 4-5, and its only earlier use in the thesis is the sample and reference arms of the OCT interferometer (§2.1.3), so the reader has to infer what an arm is (an operator, a variant, a run?).

**Suggestion.**

> Define the term where the slot is introduced by adding, after the sentence at l. 21-24: "Each setting of the slot is referred to below as an \emph{arm} of the comparison." Line 46 can then stay as it is.

### 4a.8 [medium] §4.1 Overview

`04-method.tex:52` · GPTZero: AI · flow, tone

> The persistence baseline, which predicts no change, is computed inside every run by the same evaluation code. Its values come out identical across all arms. This indicates that every arm was trained and evaluated on the same data through the same evaluation routine.

**Issue.** This evidence that the shared pipeline held sits between the operator list and the roadmap, where it interrupts both. 'Come out identical' is conversational, and three short sentences carry what is one point.

**Suggestion.**

> Move the paragraph, together with its TODO comment, to directly after the second paragraph (after l. 37), once 'arm' has been defined in the first paragraph (see l. 46), and reword it: "The persistence baseline, which predicts no change, is computed in every run by the same evaluation code, and its values are identical across all arms. This indicates that every arm was trained and evaluated on the same data through the same evaluation routine."

### 4a.9 [medium] §4.2 The Fixed Framework

`04-method.tex:95` · GPTZero: AI · ai-tone, clarity

> This section defines what every arm shares: the time handling and the tensor layout of the state. A further shared choice concerns the input itself. Every operator receives exactly one visit and predicts the state at the next visit. It sees the current state, the interval to the next visit and the patient covariates, but no earlier visits. It has no memory of the trajectory so far.

**Issue.** A meta-announcement is followed by a second one ('A further shared choice concerns ...'). The scope list leaves out the input that the paragraph then discusses, and the last sentence restates 'but no earlier visits' on its own.

**Suggestion.**

> This section defines what every arm shares: the input, the time handling and the tensor layout of the state. Every operator receives exactly one visit and predicts the state at the next visit. It sees the current state, the interval to the next visit and the patient covariates, but no earlier visits, and therefore has no memory of the trajectory so far.

### 4a.10 [medium] §4.2 The Fixed Framework

`04-method.tex:102` · GPTZero: AI · flow, clarity, tone

> Two reasons support this design. First, the clinical sequences are short, with five to thirteen visits per eye (\S\ref{sec:data:dataset}). Using several past visits as input would leave fewer visits available as prediction targets. Second, the framework predicts strictly one step at a time. Some neural PDE solvers, such as MP-PDE, predict several future steps in one forward pass (temporal bundling, \S\ref{sec:background:neural-pde}), but not all of the operators compared here support this. Bundling is therefore removed, so that every operator makes the same kind of prediction. In addition, as noted above, the sequences are so short that splitting them into multi-step windows would not be useful anyway.

**Issue.** The 'second reason' is not presented as a reason for the one-visit input. It is a separate decision about the output (no temporal bundling), so the reader loses track of what is being justified. The paragraph also uses the intensifier 'strictly', the conversational 'anyway', and 'as noted above', which repeats the first reason.

**Suggestion.**

> This design follows from the length of the clinical sequences: with five to thirteen visits per eye (\S\ref{sec:data:dataset}), using several past visits as input would leave fewer visits available as prediction targets. On the output side, the framework predicts one step at a time. Some neural PDE solvers, such as MP-PDE, predict several future steps in one forward pass (temporal bundling, \S\ref{sec:background:neural-pde}), but not all of the operators compared here support this. Bundling is therefore removed, so that every operator makes the same kind of prediction; with sequences this short, splitting them into multi-step windows would not be useful in any case.

### 4a.11 [low] §4.2 The Fixed Framework

`04-method.tex:115` · GPTZero: AI · flow

> The shared loss and curriculum are defined in~\S\ref{sec:method:training}, and the shared evaluation in~\S\ref{sec:experiments:protocol}.

**Issue.** A pointer appended to the bundling paragraph, where it has nothing to do with the topic. It belongs where §4.2 sets out its scope.

**Suggestion.**

> Move the sentence unchanged to directly after the scope sentence of §4.2 (l. 95-96).

### 4a.12 [low] §4.2.1 $\Delta t$-Conditioned Residual Formulation

`04-method.tex:140` · GPTZero: AI · ai-tone

> This form has a useful limit. As $\Delta t$ approaches zero, the predicted change vanishes and the prediction collapses to $u_{t+\Delta t} = u_t$. For two visits very close in time, the model thus predicts no change.

**Issue.** A teaser opener ('This form has a useful limit.') followed by two short sentences that make one point.

**Suggestion.**

> As $\Delta t$ approaches zero, the predicted change vanishes and the prediction collapses to $u_{t+\Delta t} = u_t$, so that for two visits very close in time the model predicts no change.

### 4a.13 [medium] §4.2.1 $\Delta t$-Conditioned Residual Formulation

`04-method.tex:142` · GPTZero: AI · clarity

> The leading $u_t$ term is also a deliberate prior. Consecutive visits are almost identical, because GA changes slowly relative to the rest of the retinal state.

**Issue.** The comparison 'relative to the rest of the retinal state' is unclear. It suggests that the layer channels change faster than the lesion, which the persistence argument does not need and which is probably not meant. The argument only needs slow change between visits.

**Suggestion.**

> Name the reference of the comparison explicitly. If slow change over a visit interval is meant: "The leading $u_t$ term is also a deliberate prior: consecutive visits are almost identical, because GA progresses little over a typical interval between visits." If a comparison with the layer channels is intended, state which part changes faster and why that matters for the prior.

### 4a.14 [medium] §4.2.1 $\Delta t$-Conditioned Residual Formulation

`04-method.tex:147` · GPTZero: AI · clarity, ai-tone, flow

> The output of $f_\theta$ is signed and unbounded, so the model can in principle also predict a shrinking lesion, although atrophic tissue does not regenerate and a shrinking lesion is not clinically plausible. No monotonic-growth constraint is imposed, because the reference segmentations themselves shrink locally between most pairs of visits (\S\ref{sec:discussion:limitations}); the prior rests on slow change alone.

**Issue.** The first sentence piles up 'so ..., although ... and ...'. The second ends in an aphoristic clause after a semicolon, and 'the prior' does not say which prior is meant. The topic changes here, so a new paragraph would help.

**Suggestion.**

> [new paragraph] The output of $f_\theta$ is signed and unbounded, so the model can in principle also predict a shrinking lesion. Atrophic tissue does not regenerate, and a shrinking lesion is not clinically plausible. No monotonic-growth constraint is imposed nonetheless, because the reference segmentations themselves shrink locally between most pairs of visits (\S\ref{sec:discussion:limitations}). The persistence prior therefore rests on slow change alone.

### 4a.15 [low] §4.2.1 $\Delta t$-Conditioned Residual Formulation

`04-method.tex:159` · GPTZero: AI · clarity, ai-tone

> Equation~\eqref{eq:method:residual-update} takes the form of one explicit Euler step (\S\ref{sec:background:pde-solvers:time}), with a step size that differs from window to window. It is the same for every operator placed in the slot. This resemblance to a numerical integrator needs a caution. The Euler form does not by itself make $f_\theta$ a time derivative or a rate of change.

**Issue.** 'It is the same ...' is ambiguous (the step size or the form?), and 'This resemblance ... needs a caution' announces the caveat instead of stating it.

**Suggestion.**

> Equation~\eqref{eq:method:residual-update} has the form of one explicit Euler step (\S\ref{sec:background:pde-solvers:time}) with a step size that differs from window to window, and this form is the same for every operator placed in the slot. The Euler form does not, however, by itself make $f_\theta$ a time derivative or a rate of change.

### 4a.16 [low] §4.2.1 $\Delta t$-Conditioned Residual Formulation

`04-method.tex:165` · GPTZero: AI · clarity, tone

> This thesis therefore does not assume such a reading. Instead, it is tested directly with a solver-swap diagnostic, reported in~\S\ref{sec:experiments:validity}: a trained model is re-evaluated, without retraining, under several integration schemes and step counts.

**Issue.** In 'Instead, it is tested directly', 'it' could refer to 'this thesis' or to 'such a reading', and 'directly' is filler.

**Suggestion.**

> Whether such a reading holds is therefore tested with a solver-swap diagnostic (\S\ref{sec:experiments:validity}): a trained model is re-evaluated, without retraining, under several integration schemes and step counts.

### 4a.17 [low] §4.2.2 Multi-Channel State Propagation

`04-method.tex:175` · GPTZero: AI · ai-tone, clarity

> The framework carries the full eleven-channel state through every component. As defined in~\S\ref{sec:data:state}, the state consists of one binary mask channel and ten layer-boundary depth channels. This subsection covers only how these channels are laid out and moved as tensors.

**Issue.** Three sentences of recap and a scope announcement before the content starts.

**Suggestion.**

> The full eleven-channel state of~\S\ref{sec:data:state} (one binary mask channel and ten layer-boundary depth channels) is carried through every component of the framework. This subsection describes only how these channels are laid out and moved as tensors.

### 4a.18 [low] §4.2.2 Multi-Channel State Propagation

`04-method.tex:188` · GPTZero: human · flow, clarity

> Operators that work on images, such as the convolutional arms of~\S\ref{sec:method:family}, need the state in the image layout $(B, C, 49, 1024)$.

**Issue.** A one-sentence paragraph left over from an earlier cut. 'Convolutional arms' does not match the term used in §4.3.1 ('operators that work on the image grid'), and the FNO is not convolutional in the usual sense.

**Suggestion.**

> Merge into the preceding paragraph: "Operators that work on the image grid (\S\ref{sec:method:family}) use the image layout $(B, C, 49, 1024)$ instead."

### 4a.19 [medium] §4.3 The Operators

`04-method.tex:204` · GPTZero: AI · ai-tone, flow

> The framework of~\S\ref{sec:method:framework} provides one slot for the update operator $f_\theta$. This section describes every operator that occupies it. Each was chosen to isolate one property. A message-passing graph neural network, run on two different graphs, tests how far the spatial context of one step has to reach. A U-Net tests multiscale local detail. A Fourier Neural Operator tests global spectral support without a local path, and a hybrid adds a minimal local path to it. Two truncated graph networks test how much spatial context is needed at all. A Finite Element Network adds an explicit transport term. Finally, a Runge--Kutta wrapper changes the time integration of any of these operators. Because all of them run in the same training environment, differences between them can be attributed to the architecture rather than to the training protocol.

**Issue.** A run of short sentences with identical 'X tests Y' syntax, the emphatic 'at all', and a closing sentence that repeats §4.1 a third time. The slot is introduced again although §4.1 and §4.2 already did so. Attaching the section references here makes the roadmap paragraph that follows unnecessary.

**Suggestion.**

> This section describes the operators placed in the slot of~\S\ref{sec:method:framework}; each was chosen to isolate one property. The message-passing graph neural network (\S\ref{sec:method:mppde}), run on two different graphs (\S\ref{sec:method:graph}), tests how far the spatial context of one step has to reach, and two truncated versions of it (\S\ref{sec:method:family:floors}) test how much spatial context is needed, if any. The U-Net (\S\ref{sec:method:family:dense}) tests multiscale local detail, and the Fourier Neural Operator tests global spectral support without a local path; a hybrid adds a minimal local path to it. The Finite Element Network (\S\ref{sec:method:family:fen}) adds an explicit transport term, and a Runge--Kutta wrapper (\S\ref{sec:method:family:rk}) changes the time integration of any of these operators.

### 4a.20 [medium] §4.3 The Operators

`04-method.tex:218` · GPTZero: AI · flow, ai-tone

> \S\ref{sec:method:family:contract} states the interface every operator satisfies. \S\ref{sec:method:mppde} describes the message-passing network and \S\ref{sec:method:graph} the two graphs it runs on. \S\ref{sec:method:family:dense} describes the three dense grid operators, \S\ref{sec:method:family:floors} the locality floors, and \S\ref{sec:method:family:fen} the Finite Element Network. \S\ref{sec:method:family:rk} describes the integration wrapper, and \S\ref{sec:method:family:params} the parameter matching.

**Issue.** A mechanical roadmap that lists the operators a second time in this section (a third time counting §4.1). Every sentence uses the same '\S X describes ...' pattern.

**Suggestion.**

> Only if the references are attached in the previous paragraph (finding at l. 204), replace this paragraph with: "The interface shared by all operators is stated first (\S\ref{sec:method:family:contract}), and the parameter matching last (\S\ref{sec:method:family:params})."

### 4a.21 [medium] §4.3.1 The Operator Contract

`04-method.tex:230` · GPTZero: AI · clarity, ai-tone

> Every operator satisfies the same interface. It is built from the same metadata --- one time step, eleven state channels and two covariates --- and it consumes the same batch. It returns the full next state in the residual form of Equation~\eqref{eq:method:residual-update}: the predicted residual is scaled by $\Delta t$ and added to the input state. The final layer of every architecture is initialised to zero, so every operator starts training at exact persistence. Each module computes the residual and the next state from one shared internal computation, so the two cannot diverge. The integration wrapper of~\S\ref{sec:method:family:rk} integrates exactly this residual.

**Issue.** The em-dash triad and the 'same ..., same ..., same ...' rhythm stand out. The residual form and the zero-init are restated from §4.2.1. 'Cannot diverge' can be read as numerical divergence (a topic the chapter later raises for the T-FEN) when 'cannot become inconsistent' is meant. 'Module' is a fifth name for the operator.

**Suggestion.**

> Every operator satisfies the same interface: it is built from the same metadata (one time step, eleven state channels and two covariates) and consumes the same batch. It returns the full next state in the residual form of Equation~\eqref{eq:method:residual-update}, and its final layer is initialised to zero (\S\ref{sec:method:dt-residual}), so that every operator starts training at exact persistence. The residual and the next state are computed from one shared internal computation, so the two cannot become inconsistent; the integration wrapper of~\S\ref{sec:method:family:rk} integrates this same residual.

### 4a.22 [medium] §4.3.1 The Operator Contract

`04-method.tex:241` · GPTZero: AI · clarity, tone

> The training curriculum of~\S\ref{sec:method:training} rolls the model forward on its own predictions without gradients but in training mode. Batch normalisation \citep{Ioffe2015} would normalise these drifted states with the statistics of the current batch, which would erase the very perturbation the curriculum is meant to expose the model to.

**Issue.** 'These drifted states' refers to a drift the previous sentence never mentions, so a reader who has not yet seen the pushforward trick loses the thread. 'The very perturbation' is an intensifier. (GPTZero labels the first sentence human and the second AI.)

**Suggestion.**

> The training curriculum of~\S\ref{sec:method:training} rolls the model forward on its own predictions, without gradients but in training mode, so the states it produces drift away from the observed ones. Batch normalisation \citep{Ioffe2015} would normalise these drifted states with the statistics of the current batch and so remove the perturbation the curriculum is meant to expose the model to.

### 4a.23 [medium] §4.3.1 The Operator Contract

`04-method.tex:251` · GPTZero: AI · ai-tone, clarity

> The operators that work on the image grid --- the U-Net and the Fourier Neural Operator with its local-kernel hybrid --- receive identical inputs. Each takes sixteen input channels: the eleven state channels, $\Delta t$ broadcast as a constant plane, the two covariates broadcast as constant planes, and two coordinate ramps running from zero to one along each axis. The coordinate ramps follow the CoordConv construction of \citet{Liu2018}. Because the inputs are identical, a difference between these arms reflects the operator, not the information it receives.

**Issue.** An em-dash aside and an 'X, not Y' closer that repeats the opening ('identical inputs'). 'The Fourier Neural Operator with its local-kernel hybrid' leaves it unclear whether the hybrid is a separate operator.

**Suggestion.**

> The operators that work on the image grid (the U-Net, the Fourier Neural Operator and its local-kernel hybrid) receive identical inputs, so that a difference between these arms cannot come from the information they receive. Each takes sixteen input channels: the eleven state channels, $\Delta t$ broadcast as a constant plane, the two covariates broadcast as constant planes, and two coordinate ramps running from zero to one along each axis, following the CoordConv construction of \citet{Liu2018}.

### 4a.24 [low] §4.3.2 Message-Passing Graph Neural Network

`04-method.tex:267` · GPTZero: AI · ai-tone, tone

> Several of its design decisions --- the time handling, the output layer and the strict one-step prediction --- also became part of the shared framework.

**Issue.** An em-dash aside containing a list of three, plus the intensifier 'strict'.

**Suggestion.**

> Several of its design decisions also became part of the shared framework: the time handling, the output layer and the one-step prediction.

### 4a.25 [medium] §4.3.2 Message-Passing Graph Neural Network (The original MP-PDE)

`04-method.tex:283` · GPTZero: AI · clarity

> Its input is $f_i^0 = \epsilon([u_i^{k-K:k}, x_i, t_k, \theta_{\text{PDE}}])$: the last $K$ states of the node, its position, the current time and the equation features.

**Issue.** The sentence calls $f_i^0$ the encoder's input, although $f_i^0$ is its output and the input is the bracketed list. A careful reader will stumble here.

**Suggestion.**

> It computes $f_i^0 = \epsilon([u_i^{k-K:k}, x_i, t_k, \theta_{\text{PDE}}])$ from the last $K$ states of the node, its position, the current time and the equation features.

### 4a.26 [low] §4.3.2 Message-Passing Graph Neural Network (The original MP-PDE)

`04-method.tex:288` · GPTZero: AI · clarity, ai-tone *(added in verification)*

> The processor applies several rounds of message passing to the latent node states; the original uses six.

**Issue.** Inside a paragraph headed 'The original MP-PDE', the tacked-on clause '; the original uses six' leaves the reader asking 'original of what?'. It reads like an appended punchline.

**Suggestion.**

> The processor applies several rounds of message passing to the latent node states (six in the original paper).

### 4a.27 [low] §4.3.2 Message-Passing Graph Neural Network (The original MP-PDE)

`04-method.tex:294` · GPTZero: AI · ai-tone, clarity

> The solution difference $u_i - u_j$ lets each message act as a learned local difference operator, a flexible learned stencil.

**Issue.** The closing appositive restates the point and repeats 'learned'.

**Suggestion.**

> The solution difference $u_i - u_j$ lets each message act as a learned local difference operator, that is, a learned stencil.

### 4a.28 [medium] §4.3.2 Message-Passing Graph Neural Network (The original MP-PDE)

`04-method.tex:301` · GPTZero: AI · ai-tone, tone

> This persistent injection is what lets a single trained solver generalise across a family of equations; removing it hurts most when the equation parameters vary across the dataset.

**Issue.** A pseudo-cleft ('is what lets'), a semicolon-joined pair of clauses, and the informal 'hurts'.

**Suggestion.**

> Injecting it at every layer allows a single trained solver to generalise across a family of equations, and removing it degrades performance most when the equation parameters vary across the dataset.

### 4a.29 [medium] §4.3.2 Message-Passing Graph Neural Network (The architecture used here)

`04-method.tex:336` · GPTZero: AI · clarity

> The conditioning vector fills the slot that the equation feature vector $\theta_{\text{PDE}}$ occupies in the original. No governing equation or coefficients are known for GA, so the interval and the covariates take this place.

**Issue.** 'Slot' is the chapter's key term for the operator slot. Using it here for the $\theta_{\text{PDE}}$ input invites confusion, and Table 4.1 does the same ('in that slot'). The two sentences also say the same thing twice ('fills the slot' / 'take this place'). (GPTZero labels the first sentence AI and the second human.)

**Suggestion.**

> The conditioning vector takes the place of the equation feature vector $\theta_{\text{PDE}}$ of the original: no governing equation or coefficients are known for GA, so the interval and the covariates are used instead. (In Table~\ref{tab:method:mppde-diff}, change 'in that slot' to 'in its place'.)

### 4a.30 [medium] §4.3.2 Message-Passing Graph Neural Network (The architecture used here)

`04-method.tex:369` · GPTZero: AI · clarity, ai-tone

> As in the original, the state difference $u_i - u_j$ lets the message act as a learned local difference operator. Every round receives the raw state, the positions and the conditioning vector again, so this information is available at every depth. As in the original, which uses skip connections in its message-passing layers, each update ends in a residual connection followed by a normalisation layer; only the type of normalisation differs. The canonical configuration aggregates messages by their mean, as written in Equation~\eqref{eq:method:update}. The canonical configuration uses two message-passing rounds and a hidden width of 64; larger and smaller settings are compared in~\S\ref{sec:experiments:ablations:capacity}.

**Issue.** 'As in the original' opens two of three sentences and 'The canonical configuration' two consecutive ones. The relative clause inside the third sentence makes it hard to follow. 'Raw state' could be read as un-normalised, although $u_i$ is the normalised state (l. 329).

**Suggestion.**

> As in the original, the state difference $u_i - u_j$ lets the message act as a learned local difference operator. Every round receives the state $u_i$, the positions and the conditioning vector again, so this information is available at every depth. Each update ends in a residual connection followed by a normalisation layer; the original also uses skip connections in its message-passing layers, and only the type of normalisation differs. The canonical configuration aggregates messages by their mean, as written in Equation~\eqref{eq:method:update}, and uses two message-passing rounds and a hidden width of 64; larger and smaller settings are compared in~\S\ref{sec:experiments:ablations:capacity}.

### 4a.31 [medium] §4.3.2 Message-Passing Graph Neural Network (The architecture used here)

`04-method.tex:384` · GPTZero: AI · tone, clarity

> Before this change, when batch normalisation was used, training and evaluation measurably behaved as two different operators.

**Issue.** 'Before this change' refers to a change in project history that the text never introduces. It reads like a development log, not a method description.

**Suggestion.**

> In earlier runs with batch normalisation, training and evaluation measurably behaved as two different operators.

### 4a.32 [low] §4.3.2 Message-Passing Graph Neural Network (The architecture used here)

`04-method.tex:393` · GPTZero: AI · tone, clarity *(added in verification)*

> The final layer is bare, without normalisation or activation, because the output is a signed and unbounded residual.

**Issue.** 'Bare' is informal, and the following phrase says the same thing again.

**Suggestion.**

> The final layer has no normalisation or activation, because the output is a signed and unbounded residual.

### 4a.33 [medium] §4.3.2 Message-Passing Graph Neural Network (The architecture used here)

`04-method.tex:394` · GPTZero: AI · clarity

> The node update is then $u_i + \Delta t \cdot \delta(f_i^{M})$, where $\delta$ denotes the decoder; this is Equation~\eqref{eq:method:residual-update} at node level.

**Issue.** 'Node update' already names the message-passing update $\psi$ (l. 291, l. 342 'every node update', Eq. 4.4). Using it for the residual state update makes the reader wonder which one is meant.

**Suggestion.**

> The predicted next state of node $i$ is then $u_i + \Delta t \cdot \delta(f_i^{M})$, where $\delta$ denotes the decoder; this is Equation~\eqref{eq:method:residual-update} at node level.

### 4a.34 [medium] §4.3.2 Message-Passing Graph Neural Network (The architecture used here)

`04-method.tex:399` · GPTZero: AI · flow, clarity

> In the original, the output head is a one-dimensional convolution. It treats the final hidden vector of a node as a temporal signal and convolves along it to emit the $K$ bundled future steps \citep{Brandstetter2022}. This head exists to produce several time steps at once. Because the framework predicts exactly one step ($K = 1$, \S\ref{sec:method:framework}), the convolutional head was removed and replaced by the decoder described above. The decoder maps the hidden vector of each node directly to the eleven channels with a full-rank linear output layer, so every channel receives its own independent prediction. Its final layer is initialised to zero, which yields the persistence start of~\S\ref{sec:method:dt-residual}.

**Issue.** The original head is described a second time, almost word for word from l. 306-309, and the reason for replacing it comes after the replacement has already been described. The paragraph also restates the decoder, the zero-init and the 'independent prediction'. (GPTZero labels the first sentence human and the rest AI.)

**Suggestion.**

> Move this paragraph before 'The decoder maps the final hidden vector ...' (l. 390) and shorten it to: "The one-dimensional convolutional head of the original \citep{Brandstetter2022}, described above, exists to emit the $K$ bundled steps. Because the framework predicts exactly one step ($K = 1$, \S\ref{sec:method:framework}), it was replaced by an MLP decoder whose full-rank linear output layer gives every channel its own independent prediction." Then end the following decoder paragraph (after '... at node level.') with "Its final layer is initialised to zero, which yields the persistence start of~\S\ref{sec:method:dt-residual}."

### 4a.35 [low] §4.3.2 Message-Passing Graph Neural Network (Differences from the original)

`04-method.tex:412` · GPTZero: human · clarity

> Table~\ref{tab:method:mppde-diff} lists the main departures from the original MP-PDE \citep{Brandstetter2022}. The original entries refer to the published paper; the original was evaluated mainly on one-dimensional equations, with additional two-dimensional smoke-inflow experiments, and used different settings for the two.

**Issue.** 'Original' appears three times in two sentences, and 'the original entries' sounds as if the entries themselves were original.

**Suggestion.**

> Table~\ref{tab:method:mppde-diff} lists the main departures from the original MP-PDE \citep{Brandstetter2022}. The entries for MP-PDE refer to the published paper, which evaluates the method mainly on one-dimensional equations, with additional two-dimensional smoke-inflow experiments, and uses different settings for the two.

### 4a.36 [low] Table 4.1 caption

`04-method.tex:425` · GPTZero: AI · clarity

> The original's aggregation is the sum written in its node-update equation; the paper does not describe the aggregation of its reference implementation.

**Issue.** The possessive 'the original's aggregation' reads awkwardly, and it is not immediately clear that the sentence explains the 'Sum over neighbours' cell.

**Suggestion.**

> For MP-PDE, the table gives the sum written in its node-update equation; the paper does not describe the aggregation used in its reference implementation.

### 4a.37 [medium] §4.3.2 Message-Passing Graph Neural Network (Differences from the original)

`04-method.tex:458` · GPTZero: AI · ai-tone, clarity

> Each change is motivated where it is introduced. The irregular time handling and the removal of bundling follow from the clinical visit schedule (\S\ref{sec:method:framework}, \S\ref{sec:method:dt-residual}). The conditioning vector replaces the unknown equation identity. The graph constructions follow from the anisotropy of the grid (\S\ref{sec:method:graph}). The normalisation and the decoder were changed so that the operator behaves identically under the training curriculum and represents all eleven channels independently (see above).

**Issue.** A recap made of short sentences with the same syntax. The last sentence pairs two changes with two reasons in an implicit 'respectively' construction that the reader has to untangle, and 'behaves identically under the training curriculum' leaves open 'identically to what'.

**Suggestion.**

> Each change is motivated where it is introduced: the irregular time handling and the removal of bundling by the clinical visit schedule (\S\ref{sec:method:framework}, \S\ref{sec:method:dt-residual}), the conditioning vector by the unknown equation identity, and the graph constructions by the anisotropy of the grid (\S\ref{sec:method:graph}). The normalisation was changed so that the operator behaves identically in training and in evaluation, and the decoder so that it represents all eleven channels independently.

