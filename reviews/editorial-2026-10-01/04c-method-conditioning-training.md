# Micro feedback 4c: Ch. 4 Method, §4.4 Conditioning, §4.5 Training, §4.6 Implementation

[← Overview](00-overview.md)

26 findings: 0 high, 9 medium, 17 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

The three sections follow a sensible order: the conditioning inputs, then the shared training recipe (objective, curriculum, optimisation), then implementation. The register matches the author's plain, declarative voice and contains almost no buzzwords. §4.4 is the weakest part. Its opening announcement ("how they enter the operators") is followed by what the covariates are and what they cannot do. Its second paragraph largely repeats §4.3.2 (the θ_PDE substitute and the three injection points) and §4.3.1, and the section ends on a one-sentence orphan paragraph. §4.5 reads well overall, but two terms are used before they are introduced. "Training pass" is defined only in §4.5.3, and $U$ appears in a formula before the text fixes it implicitly through "U = 2, so the largest budget is 360 days". Two scope phrases clash with later statements: "off in every reported run" sits next to "§5.4.2 tests the penalty", and "Every reported run uses the seed 42" sits in the same sentence as the seed-7 replications. Table 4.3 also still says "after epochs 5 and 20", which does not match the text's "from epoch 5 on, counting from 0". That the settings are shared across arms is stated three times within a page (§4.5 intro twice, Table 4.3 caption). The AI tone here comes mostly from teaser sentences ("It addresses a property of the data.", "One side effect is accepted."), self-restating pairs and "which is why / This is also why" constructions, not from vocabulary. §4.6 is concise. Its only real flow problem is that "Even so" follows the data-loader sentences instead of the seeding sentence it refers to.

### Transitions

- §4.3.8 / Table 4.2 -> §4.4: the second paragraph of §4.4 (l. 966-982) restates §4.3.2 l. 333-341 almost verbatim (θ_PDE substitute, injection at encoder input, every message, every node update) and the dense-operator input planes of §4.3.1. Either mark it as a summary ('As described for each operator in §4.3, ...') or shorten it to what §4.3 does not already say in one place (floors, FEN, RK wrapper).
- §4.4, paragraph 1: 'This section describes how they enter the operators.' (l. 956) announces the mechanism, but the paragraph continues with the properties of the covariates, and the mechanism follows only in paragraph 2, which has its own announcement ('How they enter the forward pass depends on the operator.'). Delete the first announcement. Optionally move the motivation sentence (l. 965-966) up so that it follows the pointer to §3.5.
- §4.4 ends with the one-sentence paragraph 'The covariates are enabled in the canonical configuration of every operator.' Append it to the preceding paragraph.
- §4.5 intro + Table 4.3 caption: 'shared by every operator' / 'do not change between arms' / 'None of these settings changes between arms' says the same thing three times within a page (and §4.3.1 says it too). State it once in the intro and keep the caption to one short sentence.
- §4.5.1: 'The same loss is used in training and in validation.' (l. 1089) closes the paragraph on optional switches, where it does not belong. Move it to the end of the first paragraph of §4.5.1, after the weights are defined.
- §4.5.1, third paragraph: per-eye scoring and the sigmoid side effect are two separate topics. Start a new paragraph at the side effect (l. 1074).
- §4.5.2 -> §4.5.3: 'Each training pass draws a time budget' (l. 1104) uses 'pass' before §4.5.3 (l. 1149-1151) defines it. Introduce the pass at the start of the second paragraph of §4.5.2 (see the finding at l. 1149). Do not move the §4.5.3 sentence verbatim, because it would duplicate 'a new time budget is drawn'.
- §4.5.2: the 180-day base is justified in two places, as the modal interval (paragraph 2) and through the undershoot rule (end of paragraph 3). Either join them, or add a forward pointer in paragraph 2 ('a second reason follows from the undershoot rule below').
- §4.5.3, last paragraph (seed and validation schedule): this is not about optimisation. Optionally move the seed sentence into the §4.6 paragraph that seeds the random number generators, which currently does not name the seed.
- §4.6, last paragraph: 'Even so, repeated runs ... do not give identical results' refers back to the seeding and the deterministic cuDNN algorithms, but the sentence just before it is about the data loader. Put the data-loader sentences first and the seeding sentence immediately before 'Even so'.

### Recurring tells in this part

- Teaser or announcement sentences that hold back the content until the next sentence: 'This section describes how they enter the operators.', 'It addresses a property of the data.', 'One side effect is accepted.' (3 occurrences). Fold each into the sentence that carries the content.
- Pairs that restate themselves, or the same fact said twice: 'they can only shift the prediction ... as a whole. They cannot point to a location ...'; 'separately for each trainable module: each module is clipped by its own gradient norm'; 'off in every reported run ... Its weight is zero for every operator'; 'shared by every operator ... do not change between arms' (about 4-5 occurrences). Keep one formulation.
- Explanatory cleft and 'which is why' constructions: 'This is also why the base is 180 days', 'which is why no operator may use batch statistics', 'This is required, because ...', 'It is one reason why ...' (about 4 occurrences; the last is unremarkable). Use a plain causal clause ('Because ..., ...').
- Over-broad scope words that clash with a stated exception: 'off in every reported run' (the penalty is run in §5.4.2), 'Every reported run uses the seed 42' (seed-7 runs are reported) (2 occurrences). Use 'unless stated otherwise' or 'for every operator of the comparison'.
- Unclear referent of 'the original': in the soft-Dice paragraph, 'Unlike the original' refers to Milletari et al., while elsewhere in the chapter (including §4.5.2, l. 1098) 'the original' means MP-PDE (1 problematic occurrence in range; the MP-PDE use in §4.5.2 is consistent and fine).
- Em-dash asides used for inline lists: 'the dense grid operators --- the U-Net, ... --- each covariate ...', 'All random number generators --- those of Python, ... --- are seeded' (2 occurrences). Parentheses read more neutrally.
- Runs of very short declaratives that separate a rationale from its fact ('The mask is the clinical target.'; 'Training runs for 30 epochs. One epoch consists of 20 passes.'). This is also the author's human-judged voice, so merge only where a fact is split from its reason (about 2 paragraphs).
- Emphasis words the author's notes discourage: 'would never unroll at all' (1 occurrence).

## Findings

### 4c.1 [low] §4.4 Conditioning: Patient Covariates

`04-method.tex:956` · GPTZero: human · flow, tone

> This section describes how they enter the operators.

**Issue.** The announcement promises 'how they enter', but the next sentences cover what the covariates are and what they cannot do. The mechanism follows only in the next paragraph, which has its own announcement ('How they enter the forward pass depends on the operator.').

**Suggestion.**

> Delete the sentence. The paragraph then moves directly from the pointer to §3.5 to the properties of the covariates, and l. 969 already introduces the mechanism. Optional: move 'The covariates are included because age and sex are plausible modulators of how fast GA progresses.' (l. 965-966) up so that it follows the pointer to §3.5.

### 4c.2 [low] §4.4 Conditioning: Patient Covariates

`04-method.tex:957` · GPTZero: human · clarity

> Both covariates are graph-level quantities: a visit has one value of each, and that value is shared by all $50\,176$ grid positions.

**Issue.** 'Graph-level' is GNN vocabulary (§4.3.2 uses it for the conditioning vector), but this section covers every operator, including the dense grid operators, which have no graph.

**Suggestion.**

> Both covariates are global quantities: a visit has one value of each, and that value is shared by all $50\,176$ grid positions.

### 4c.3 [medium] §4.4 Conditioning: Patient Covariates

`04-method.tex:960` · GPTZero: AI · clarity, ai-tone

> Because the covariates carry no spatial information, they can only shift the prediction of an operator as a whole. They cannot point to a location on the grid or shape the lesion boundary locally.

**Issue.** The second sentence restates the first in negative form, a mirror pair typical of the flagged tone. 'Shift' can also be read as an additive offset, although in the graph network the covariates enter every message and update nonlinearly.

**Suggestion.**

> Because the covariates carry no spatial information, they act on the prediction of an operator only as a whole and cannot point to a location on the grid or shape the lesion boundary locally.

### 4c.4 [low] §4.4 Conditioning: Patient Covariates

`04-method.tex:966` · GPTZero: AI · clarity, flow

> Together with $\Delta t$, they fill the slot that the equation features $\theta_{\text{PDE}}$ occupy in MP-PDE, since no governing equation with known coefficients exists for GA (\S\ref{sec:method:mppde}).

**Issue.** In this chapter 'slot' names the swappable operator slot, so reusing it for the θ_PDE input is a small collision. The 'since' clause gives the reason for needing a substitute but hangs off the end. The sentence also repeats §4.3.2 (l. 337-340) almost verbatim.

**Suggestion.**

> Since no governing equation with known coefficients exists for GA, $\Delta t$ and the two covariates take the place of the equation features $\theta_{\text{PDE}}$ of MP-PDE (\S\ref{sec:method:mppde}). (Alternatively cut the sentence, since \S\ref{sec:method:mppde} already states it.)

### 4c.5 [low] §4.4 Conditioning: Patient Covariates

`04-method.tex:975` · GPTZero: AI · ai-tone, clarity

> In the dense grid operators --- the U-Net, the Fourier Neural Operator and the local-kernel hybrid --- each covariate is an extra input channel holding a constant plane (\S\ref{sec:method:family:contract}). The free-form network of the Finite Element Network receives them as additional inputs (\S\ref{sec:method:family:fen}).

**Issue.** The em-dash aside used for an inline list is a recurring flagged pattern. 'The free-form network of the Finite Element Network' repeats 'network', and both names are written out although FNO and FEN were abbreviated earlier (l. 42-43, 600, 696). §4.3.6 calls this part 'the free-form term'.

**Suggestion.**

> In the dense grid operators (the U-Net, the FNO and the local-kernel hybrid), each covariate is an extra input channel holding a constant plane (\S\ref{sec:method:family:contract}). In the FEN, they are additional inputs to the free-form term (\S\ref{sec:method:family:fen}).

### 4c.6 [low] §4.4 Conditioning: Patient Covariates

`04-method.tex:984` · GPTZero: human · flow

> The covariates are enabled in the canonical configuration of every operator.

**Issue.** A one-sentence paragraph closes the section and reads as an orphan.

**Suggestion.**

> Append the sentence to the end of the preceding paragraph, after the Runge--Kutta sentence.

### 4c.7 [low] §4.5 Training (introduction)

`04-method.tex:1021` · GPTZero: human · clarity, flow

> Everything in this section is shared by every operator of the survey (\S\ref{sec:method:family:contract}), and Table~\ref{tab:method:hparams} lists the settings. The objective, the curriculum and the optimisation settings do not change between arms, so that a difference between two arms can be attributed to the operator.

**Issue.** The second sentence restates the first ('shared by every operator' / 'do not change between arms'), and the Table 4.3 caption says it a third time.

**Suggestion.**

> The objective, the curriculum and the optimisation settings are the same for every operator of the survey (\S\ref{sec:method:family:contract}), so that a difference between two arms can be attributed to the operator. Table~\ref{tab:method:hparams} lists the settings.

### 4c.8 [low] §4.5.1 Objective

`04-method.tex:1041` · GPTZero: AI · flow, clarity

> The mask channel ($c = 0$) has the weight $w_0 = 5$, and each of the ten layer channels has the weight $w_c = 1$. Dividing by the mean weight keeps the scale of the term comparable to an unweighted MSE. The mask is the clinical target. The layer channels are auxiliary targets, but the operator must still predict them, because they are part of the next state that is fed back during a rollout.

**Issue.** The reason for the higher mask weight ('The mask is the clinical target.') is separated from the weight by an unrelated normalisation sentence, which makes the sequence choppy.

**Suggestion.**

> The mask channel ($c = 0$), which is the clinical target, has the weight $w_0 = 5$, and each of the ten layer channels has the weight $w_c = 1$. The layer channels are auxiliary targets, but the operator must still predict them, because they are part of the next state that is fed back during a rollout. Dividing by the mean weight keeps the scale of the term comparable to an unweighted MSE.

### 4c.9 [low] §4.5.1 Objective

`04-method.tex:1048` · GPTZero: human · clarity, tone

> The second term is a soft-Dice loss on the mask channel \citep{Milletari2016}, with the weight $\lambda_{\text{Dice}} = 5$. It addresses a property of the data. Between two consecutive visits, almost all mask pixels are unchanged, so a plain MSE is dominated by static pixels and gives little gradient at the moving lesion boundary.

**Issue.** 'It addresses a property of the data.' is a teaser that names nothing and makes the reader wait for the next sentence.

**Suggestion.**

> The second term is a soft-Dice loss on the mask channel \citep{Milletari2016}, with the weight $\lambda_{\text{Dice}} = 5$. It counters an imbalance in the data: between two consecutive visits, almost all mask pixels are unchanged, so a plain MSE is dominated by static pixels and gives little gradient at the moving lesion boundary.

### 4c.10 [low] §4.5.1 Objective

`04-method.tex:1052` · GPTZero: AI · tone

> A model trained on it can settle on copying its input.

**Issue.** 'Settle on' is conversational and slightly anthropomorphic for an optimisation outcome.

**Suggestion.**

> A model trained on it can learn to copy its input.

### 4c.11 [low] §4.5.1 Objective

`04-method.tex:1054` · GPTZero: AI · clarity

> Unlike the original, which scores a segmentation probability map, it is applied here to a regression output.

**Issue.** Elsewhere in the chapter 'the original' means MP-PDE (or the original FEN). Here it means the soft-Dice loss of Milletari et al., and 'it' is ambiguous between the term and the soft mask.

**Suggestion.**

> Unlike the original soft-Dice loss, which scores a segmentation probability map, the term is applied here to a regression output.

### 4c.12 [medium] §4.5.1 Objective

`04-method.tex:1074` · GPTZero: AI · ai-tone, clarity, flow

> One side effect is accepted. The sigmoid of Equation~\eqref{eq:method:soft-mask} does not saturate at the physical mask values, so the term stretches the raw mask regression about the threshold.

**Issue.** 'One side effect is accepted.' is a teaser sentence, and it opens a new topic in the middle of the paragraph on per-eye scoring. 'Stretches the raw mask regression about the threshold' is opaque on first reading.

**Suggestion.**

> Start a new paragraph: "The soft-Dice term has one accepted side effect. Because the sigmoid of Equation~\eqref{eq:method:soft-mask} does not saturate at the physical mask values, the term stretches the raw mask predictions away from the threshold." Keep the following two sentences unchanged.

### 4c.13 [medium] §4.5.1 Objective

`04-method.tex:1081` · GPTZero: AI · clarity, flow

> Two further options exist in the implementation and are off in every reported run. First, the loss can exclude grid positions whose target equals the fill value of the crop padding (\S\ref{sec:data:spatial}), from both terms. Since this option is off, the padded positions are regressed at full weight. Second, a monotonic-growth penalty can be added, which penalises a decrease of the mask where the previous state is atrophic. Its weight is zero for every operator of the comparison; \S\ref{sec:method:dt-residual} explains why no monotonic constraint is imposed, and~\S\ref{sec:experiments:ablations:loss} tests the penalty.

**Issue.** 'Off in every reported run' contradicts the closing clause: §5.4.2 reports a run with the penalty at weight 2.0. 'Its weight is zero ...' repeats the opening sentence, and 'from both terms' is stranded after the parenthesis.

**Suggestion.**

> Two further options exist in the implementation and are off for every operator of the comparison. First, the loss can exclude from both terms the grid positions whose target equals the fill value of the crop padding (\S\ref{sec:data:spatial}); since no reported run uses this option, the padded positions are regressed at full weight. Second, a monotonic-growth penalty can be added, which penalises a decrease of the mask where the previous state is atrophic; \S\ref{sec:method:dt-residual} explains why no monotonic constraint is imposed, and~\S\ref{sec:experiments:ablations:loss} tests the penalty.

### 4c.14 [low] §4.5.1 Objective

`04-method.tex:1089` · GPTZero: human · flow

> The same loss is used in training and in validation.

**Issue.** This general statement about the loss is attached to the end of a paragraph about optional switches.

**Suggestion.**

> Move the sentence to the end of the first paragraph of §4.5.1, directly after the definition of the weights.

### 4c.15 [low] §4.5.2 Time-Budgeted Pushforward Curriculum

`04-method.tex:1104` · GPTZero: AI · clarity

> Each training pass draws a time budget $B$ uniformly from $\{0, 1, \dots, \min(e, U)\} \times 180$ days, where $e$ is the current epoch.

**Issue.** $U$ appears in the formula but is introduced only implicitly two sentences later ('Every reported run uses $U = 2$, so the largest budget is 360 days').

**Suggestion.**

> Each training pass draws a time budget $B$ uniformly from $\{0, 1, \dots, \min(e, U)\} \times 180$ days, where $e$ is the current epoch and $U$ the largest number of 180-day units in a budget.

### 4c.16 [low] §4.5.2 Time-Budgeted Pushforward Curriculum

`04-method.tex:1109` · GPTZero: AI · clarity, tone

> Because of the $\min(e, U)$, the horizon ramps in over the first $U$ epochs; after that, budgets of 0, 180 and 360 days are drawn with equal probability.

**Issue.** A bare math expression as the object of 'Because of the' reads awkwardly, and 'ramps in' is informal and vague.

**Suggestion.**

> Because the upper limit is $\min(e, U)$, the largest budget grows by 180 days per epoch over the first $U$ epochs; after that, budgets of 0, 180 and 360 days are drawn with equal probability.

### 4c.17 [medium] §4.5.2 Time-Budgeted Pushforward Curriculum

`04-method.tex:1124` · GPTZero: AI · ai-tone, flow

> This is also why the base is 180 days and not the shortest interval of 90 days. Under the undershoot rule, a 90-day budget can never chain two visits (\S\ref{sec:data:temporal}), and the curriculum would never unroll at all.

**Issue.** The 'This is also why' cleft and the emphatic 'at all' are flagged-tone markers, and 'never ... never' repeats. The second reason for the 180-day base arrives a paragraph after the base was introduced.

**Suggestion.**

> The undershoot rule is also the reason for the 180-day base: a budget of 90 days, the shortest interval, can never chain two visits (\S\ref{sec:data:temporal}), so the curriculum would not unroll.

### 4c.18 [low] §4.5.2 Time-Budgeted Pushforward Curriculum

`04-method.tex:1135` · GPTZero: AI · clarity, ai-tone

> The group losses are weighted by the share of the batch each group holds and combined. The rollout runs in training mode, which is why no operator may use batch statistics (\S\ref{sec:method:family:contract}).

**Issue.** 'And combined' trails at the end of the clause, and the 'which is why' construction is a recurring explanatory tell.

**Suggestion.**

> The group losses are combined, each weighted by the share of the batch its group holds. Because the rollout runs in training mode, no operator may use batch statistics (\S\ref{sec:method:family:contract}).

### 4c.19 [low] §4.5.3 Optimisation

`04-method.tex:1145` · GPTZero: AI · clarity

> The learning rate is multiplied by 0.4 from epoch 5 on and again from epoch 20 on, counting epochs from 0 (the first five epochs run at the initial rate).

**Issue.** 'From epoch 5 on' is colloquial, and the parenthesis is loosely attached.

**Suggestion.**

> The learning rate is multiplied by 0.4 at the start of epoch 5 and again at the start of epoch 20, counting from 0, so the first five epochs run at the initial rate.

### 4c.20 [medium] §4.5.3 Optimisation

`04-method.tex:1149` · GPTZero: AI · flow, clarity

> Training runs for 30 epochs. One epoch consists of 20 passes. In each pass, a new time budget is drawn, and every training eye contributes one randomly chosen start window that can realise it. The batch size is four eyes.

**Issue.** A 'pass' is defined here, after §4.5.2 has already built the curriculum on 'each training pass' (l. 1104), and four very short sentences in a row read like a list.

**Suggestion.**

> In §4.5.2, open the second paragraph with: "Training proceeds in passes; in each pass, every training eye contributes one randomly chosen start window." (The budget is then introduced by the existing 'Each training pass draws a time budget ...', and realisability by l. 1114.) Here, write: "Training runs for 30 epochs of 20 passes each, with a batch size of four eyes."

### 4c.21 [medium] §4.5.3 Optimisation

`04-method.tex:1156` · GPTZero: AI · clarity, ai-tone

> Gradients are clipped to a norm of 1.0, separately for each trainable module: each module is clipped by its own gradient norm, so that a large gradient in one module cannot shrink the updates of another.

**Issue.** The colon introduces a restatement of the same fact ('separately for each module' / 'each module is clipped by its own norm'), a tautological colon reveal typical of the flagged tone.

**Suggestion.**

> Gradients are clipped to a norm of 1.0 separately for each trainable module, so that a large gradient in one module cannot shrink the updates of another.

### 4c.22 [medium] §4.5.3 Optimisation

`04-method.tex:1163` · GPTZero: AI · clarity

> Every reported run uses the seed 42; replication runs with the seed 7 are reported in Chapter~\ref{ch:experiments}. The model is validated on the held-out fold after every epoch (\S\ref{sec:data:splits}); which epochs enter the reported numbers, and why, is set out in~\S\ref{sec:experiments:protocol}.

**Issue.** 'Every reported run uses the seed 42' contradicts the second half of the same sentence (seed-7 runs are reported), and 'the seed 42' is unidiomatic. The inverted clause 'which epochs ..., and why, is set out in' is hard to parse.

**Suggestion.**

> Unless stated otherwise, every reported run uses seed 42; replication runs with seed 7 are reported in Chapter~\ref{ch:experiments}. The model is validated on the held-out fold after every epoch (\S\ref{sec:data:splits}); \S\ref{sec:experiments:protocol} sets out which epochs enter the reported numbers and why.

### 4c.23 [low] Table 4.3 caption

`04-method.tex:1172` · GPTZero: human · clarity

> Training settings shared by every operator of the survey. None of these settings changes between arms.

**Issue.** The second sentence repeats the first.

**Suggestion.**

> Training settings, identical for every operator of the survey.

### 4c.24 [medium] Table 4.3 (Learning rate row)

`04-method.tex:1181` · GPTZero: AI · clarity

> Learning rate & $2 \times 10^{-3}$, multiplied by 0.4 after epochs 5 and 20

**Issue.** The table says 'after epochs 5 and 20', but the text says 'from epoch 5 on ... counting epochs from 0'. Read literally, the two describe schedules one epoch apart. NOTES records that 'after epoch 5' was corrected in the text, but the table was not updated.

**Suggestion.**

> Learning rate & $2 \times 10^{-3}$, multiplied by 0.4 at the start of epochs 5 and 20 (counted from 0)

### 4c.25 [low] §4.6 Implementation Details

`04-method.tex:1205` · GPTZero: AI · clarity

> Every reported run was trained on a single NVIDIA RTX A6000 GPU on a cluster managed by Slurm, and the five folds of an experiment are submitted together as a job array.

**Issue.** The tense switches from past ('was trained') to present ('are submitted') within one sentence.

**Suggestion.**

> Every reported run was trained on a single NVIDIA RTX A6000 GPU on a cluster managed by Slurm, and the five folds of an experiment were submitted together as a job array.

### 4c.26 [medium] §4.6 Implementation Details

`04-method.tex:1219` · GPTZero: AI · flow, clarity, ai-tone

> All random number generators --- those of Python, NumPy, PyTorch and CUDA --- are seeded, and deterministic cuDNN algorithms are enforced. The data loader runs in the main process. This is required, because the curriculum changes the sampling restriction of the dataset at every pass, and a change made in the main process would not reach separate worker processes. Even so, repeated runs of the same configuration do not give identical results on the GPU. Chapter~\ref{ch:experiments} quantifies this run-to-run variation, and it defines the noise floor against which every comparison is read.

**Issue.** 'Even so' refers to the seeding and the deterministic cuDNN algorithms, but the data-loader sentences sit in between, so it attaches to the wrong statement. 'This is required, because' is stilted, and the em-dash aside is a recurring tell.

**Suggestion.**

> The data loader runs in the main process, because the curriculum changes the sampling restriction of the dataset at every pass and a change made in the main process would not reach separate worker processes. All random number generators (Python, NumPy, PyTorch and CUDA) are seeded, and deterministic cuDNN algorithms are enforced. Even so, repeated runs of the same configuration do not give identical results on the GPU. Chapter~\ref{ch:experiments} quantifies this run-to-run variation and defines the noise floor against which every comparison is read.

