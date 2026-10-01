# Micro feedback 2b: Ch. 2 Background, §2.2-§2.4 PDEs, neural solvers, related work

[← Overview](00-overview.md)

46 findings: 2 high, 22 medium, 22 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

The range is structurally sound. §2.2 runs in a clear order: notation, stencils, time stepping, strengths and limits, neural solvers that keep the mechanisms, and the fit to GA. Most of its paragraphs are short and concrete, and they share the plain declarative register of the sentences GPTZero judged human (e.g. "Classical solvers are well understood.", "The two parts are independent: ..."). The weak points are local. The rate function f is defined twice in nearly the same words (l.571 and l.622). The two-step solver description repeats the roadmap of the opening paragraph. "Reach" is a paragraph title but is never defined, although later chapters build on it. The opening sentence calls the update rule "local", which does not fit §2.2.5 ("not assumed here") or the global operators in the survey. §2.3 is the weakest part. It reopens neural solvers without linking back to §2.2.4, re-introduces error accumulation as if it were new, introduces the Fourier Neural Operator twice, jumps from zero stability to "Beyond graph networks", and uses "inductive bias" as a key term without a plain definition. Its register also drifts into stock rhetoric ("fundamentally" four times in the range, "Furthermore ... Finally", "It must be stated plainly that"). Related Work has a sensible four-part structure, but it has three problems. Its first paragraph announces two categories and discusses only the first. The positioning paragraph ("By contrast ... Consequently, this thesis sits at the intersection") follows Mai and Salvi, so it seems to set the thesis apart from those per-eye spatial models as well. The last paragraph repeats the origin of the U-Net from §2.3. None of these needs a content change: back-references, two bridging sentences and sentence-level tightening fix them.

### Transitions

- §2.2 intro (l.507-513) -> next paragraph (l.532-538): the two-step solver description repeats the roadmap and cites the same two \S\ref targets twice in consecutive paragraphs. Merge l.532-538 into one sentence (see the finding at l.532). Optionally, the first two items of the roadmap could be dropped.
- §2.2.1 FDM paragraph (l.571-572) -> §2.2.2 opening (l.622-625): the function f is defined twice in nearly the same words ('maps the grid values u^k to a rate of change for every cell'). Open §2.2.2 by referring back to f instead of defining it again (see the finding at l.622).
- §2.2.1 'Locality and reach' (l.611-617): the paragraph title introduces 'reach', but the text never names it, and the anisotropy that §2.2.5 relies on is not linked here. Define the term (see the finding at l.614). Optionally, add after l.615: 'On the en-face grid, whose two spacings differ by a factor of about twenty, the same stencil therefore reaches very different physical distances along the two axes.'
- §2.2.4 last paragraph (l.749-753) -> §2.3 paragraph 4 (l.834-839): error accumulation is explained twice. §2.2.4 says that §2.3 'discusses this problem', but §2.3 then introduces it as if it were new. Open the §2.3 paragraph with a back-reference (see the finding at l.834).
- §2.2.5 end (l.791-793) -> §2.3 opening (l.799): §2.2.5 promises 'the operator families that are candidates for this role', but §2.3 opens with the split between neural operators and autoregressive solvers, and the families only appear in paragraph 7. Insert a bridging first sentence before l.799: '\S\ref{sec:background:pde-solvers:neural} introduced neural solvers that keep the classical mechanisms; this section places them in the wider neural-PDE literature and introduces the architecture families compared in Chapter~\ref{ch:experiments}.'
- §2.3 paragraph 6 -> paragraph 7 (l.861 -> l.864): the jump from zero stability to 'Beyond graph networks' is abrupt, because graph networks were last named in §2.2.4. Write 'Beyond graph networks such as MP-PDE, several distinct architecture families are used as PDE surrogates.'
- §2.3 paragraphs 2 and 7: the Fourier Neural Operator is introduced at l.815 and then again at l.872-873 as if it were new. In paragraph 7, refer back to it ('Global spectral operators such as the Fourier Neural Operator introduced above ...'). Alternatively, move paragraph 7 (architecture families) directly after paragraph 2 (neural operators), so that all architecture descriptions come before the argument for the autoregressive framing.
- Related Work P1 -> P2 (l.904 -> l.919): P1 announces 'cohort-level risk models and spatial-progression models' but discusses only the first. Open P2 with the second category: 'Among spatial-progression models, the closest prior work on the prediction task addressed here is by \citet{Mai2024}, ...'. Keep the % TODO comment that sits inside this sentence.
- Related Work P3 (l.934-944): the contrast with cohort-level time-to-conversion models comes after the Mai and Salvi paragraph, so 'By contrast' reads as if the thesis also differed from those per-eye spatial models. Move the first two sentences of P3 to the end of P1, where the cohort-level models are discussed. Keep the positioning sentence and the 'remains sparse' sentence as a short closing paragraph before the paragraph on architecture origins.
- Related Work P4 (l.946-958) repeats §2.3: the origin of the U-Net in biomedical image segmentation is stated both in l.868 and in l.951-952. Cut the repeated phrase in P4 and keep only the attributions (see the finding at l.950).

### Recurring tells in this part

- Intensifiers and filler adverbs, about 12 occurrences in the range. Examples: 'fundamentally' (l.809, 826, 871, 925), 'inherently' (l.822), 'altogether' (l.814), 'exactly' (l.507, 719), 'naturally' (l.779), 'directly' (l.873), 'reliably' (l.823). Most can be deleted without changing the meaning. 'exactly' at l.582 and l.766 is technical and can stay.
- Antitheses and 'rather than' contrasts. Examples: 'not a densely simulated trajectory but a few observed states' (l.758-759) and 'reasons to expect the structure to fit, not evidence that it does' (l.784). 'rather than' occurs about 8 times (e.g. l.575, 588, 707, 781, 830, 836, 851, 888). Keep the ones that carry a real technical contrast (FVM vs FDM, l.851) and rephrase the rhetorical ones.
- Pseudo-cleft and cleft constructions, about 3 occurrences: 'This locality is what the stencils ... exploit' (l.528), 'What the learned version gains is ... What it loses are the guarantees' (l.745-749), '..., which is why the thesis adopts it' (l.762). Replace each with a direct subject-verb sentence.
- Aphoristic paragraph closers, about 3-4 occurrences: 'This is the mechanism closest to what a learned operator does.' (l.600-601), '... and nothing else' (l.703-704), 'These are reasons to expect the structure to fit, not evidence that it does.' (l.784).
- Connective chains that list reasons, 2 occurrences, both flagged by GPTZero: 'Each ... Furthermore ... Finally' (l.825-832) and 'The prevailing formulation ... By contrast ... Consequently' (l.934-939).
- Meta-announcements and instructions to the reader, about 4 occurrences: 'this section introduces exactly those' (l.507), 'Note that' (l.806), 'It must be stated plainly that' (l.885-886), 'This difference must be kept in mind' (l.927-928).
- Colon reveals and em-dash appositives that deliver a punchline, about 4-5 occurrences: 'the solver computes what F prescribes and nothing else' (l.703), 'And accuracy is expensive: ...' (l.708), '--- a learned, non-linear stencil' (l.737), '--- the situation a stencil is designed for' (l.772). Only these two em-dashes occur in the range.
- Vague abstract verbs and noun stacks, about 7 occurrences, mostly in §2.3 and Related Work: 'dictates' (l.832, 936), 'necessitates' (l.830), 'positions OCT as a candidate predictive substrate' (l.916-917), 'adopt a different numerical perspective' (l.878-879), 'sits at the intersection of' (l.937-938), 'OCT-based age-related macular degeneration and geographic atrophy progression' (l.904-905).

## Findings

### 2b.1 [medium] §2.2 Partial Differential Equations and Numerical Solvers (intro)

`02-background.tex:502` · GPTZero: AI · flow, clarity

> The approach of this thesis treats GA progression the way a numerical solver treats a partial differential equation (PDE): the state is held on a grid and advanced step by step by a local update rule.

**Issue.** 'a local update rule' presents locality as a premise of the approach. §2.2.5 (l.789-791), however, states that whether a local stencil, a global operator or both is needed is 'not assumed here', and global operators (FNO) are part of the survey. Pseudospectral solvers (l.603-609) are not local either.

**Suggestion.**

> The approach of this thesis treats GA progression the way a numerical solver treats a partial differential equation (PDE): the state is held on a grid and advanced step by step by an update rule.

### 2b.2 [low] §2.2 Partial Differential Equations and Numerical Solvers (intro)

`02-background.tex:505` · GPTZero: AI · tone, ai-tone

> Understanding the framework of Chapter~\ref{ch:method} and the models of Chapter~\ref{ch:experiments} therefore requires only a few solver mechanisms, and this section introduces exactly those.

**Issue.** 'exactly those' is emphatic filler typical of generated announcements, and the gerund subject 'Understanding ... requires' is heavy.

**Suggestion.**

> Only a few solver mechanisms are needed to follow the framework of Chapter~\ref{ch:method} and the models of Chapter~\ref{ch:experiments}; this section introduces them.

### 2b.3 [low] §2.2 Partial Differential Equations and Numerical Solvers (intro)

`02-background.tex:528` · GPTZero: AI · ai-tone

> This locality is what the stencils of \S\ref{sec:background:pde-solvers:stencils} exploit.

**Issue.** Pseudo-cleft ('This X is what Y exploit'), a construction that recurs in the chapter. The plain subject-verb form is shorter.

**Suggestion.**

> The stencils of \S\ref{sec:background:pde-solvers:stencils} exploit this locality.

### 2b.4 [low] §2.2 Partial Differential Equations and Numerical Solvers (intro)

`02-background.tex:532` · GPTZero: AI · flow

> Closed-form solutions exist only in special cases, so the solution is computed numerically. A numerical solver does this in two steps: it replaces the continuous domain by a grid and the spatial derivatives by operations on grid values (\S\ref{sec:background:pde-solvers:stencils}), and it then advances the grid values in discrete time steps (\S\ref{sec:background:pde-solvers:time}).

**Issue.** This repeats the roadmap given six lines earlier (l.507-513) with the same two cross-references, so the reader meets the same plan twice in consecutive paragraphs. Merging the two sentences reduces the repetition.

**Suggestion.**

> Closed-form solutions exist only in special cases, so the solution is computed numerically, in two steps: the continuous domain is replaced by a grid and the spatial derivatives by operations on grid values (\S\ref{sec:background:pde-solvers:stencils}), and the grid values are then advanced in discrete time steps (\S\ref{sec:background:pde-solvers:time}).

### 2b.5 [low] §2.2.1 Discretising space: stencils

`02-background.tex:548` · GPTZero: AI · clarity, tone

> The en-face grid of this thesis is of that type, with the particularity that the two spacings differ by a factor of about twenty (\S\ref{sec:data:spatial}).

**Issue.** 'with the particularity that' is stiff and non-idiomatic.

**Suggestion.**

> The en-face grid of this thesis is a uniform grid whose two spacings differ by a factor of about twenty (\S\ref{sec:data:spatial}).

### 2b.6 [low] §2.2.1 Finite differences and finite volumes

`02-background.tex:561` · GPTZero: AI · clarity

> In general, the $n$-th derivative at cell $i$ is estimated as a weighted sum over a small neighbourhood $\mathcal{N}(i)$,

**Issue.** $n$ is defined at l.524 as the number of components of $u$, but here it denotes the derivative order (also in $\alpha_j^{(n)}$ and in $(i\omega)^n$ at l.605). A careful reader may stumble over the clash.

**Suggestion.**

> Notation only, optional: use a different symbol for the derivative order (e.g. $m$-th derivative, $\alpha_j^{(m)}$, $(i\omega)^m$), or rename the component count in \eqref{eq:bg:temporal-pde}. The sentence itself needs no other change.

### 2b.7 [low] §2.2.1 Adaptive stencils

`02-background.tex:595` · GPTZero: AI · clarity

> Weighted essentially non-oscillatory (WENO) schemes avoid this by computing several candidate estimates on shifted sub-stencils and combining them with weights that depend on how smooth the data are in each sub-stencil, so that sub-stencils crossing the front receive almost no weight \citep{Liu1994, JiangShu1996}.

**Issue.** One sentence of about 45 words carries three steps (candidate estimates, smoothness weights, the effect at the front). Splitting it makes the mechanism easier to follow.

**Suggestion.**

> Weighted essentially non-oscillatory (WENO) schemes avoid this by computing several candidate estimates on shifted sub-stencils. The estimates are combined with weights that depend on how smooth the data are in each sub-stencil, so that sub-stencils crossing the front receive almost no weight \citep{Liu1994, JiangShu1996}.

### 2b.8 [low] §2.2.1 Adaptive stencils

`02-background.tex:599` · GPTZero: AI · ai-tone

> The stencil thereby becomes a non-linear function of its input. This is the mechanism closest to what a learned operator does.

**Issue.** The short closing sentence works as an aphoristic paragraph ending, and its subject 'This' has a vague referent. Folding it into the previous sentence names the mechanism.

**Suggestion.**

> The stencil thereby becomes a non-linear function of its input, which makes WENO the classical mechanism closest to what a learned operator does.

### 2b.9 [low] §2.2.1 Global methods

`02-background.tex:604` · GPTZero: AI · clarity

> Pseudospectral methods compute derivatives in Fourier space instead: the field is transformed, each mode is multiplied by $(i\omega)^n$, and the result is transformed back.

**Issue.** 'instead' has no explicit referent. The preceding paragraph is about WENO, and the intended contrast is with all the neighbourhood-based stencils.

**Suggestion.**

> Pseudospectral methods compute derivatives in Fourier space instead of from a neighbourhood: the field is transformed, each mode is multiplied by $(i\omega)^n$, and the result is transformed back.

### 2b.10 [medium] §2.2.1 Locality and reach

`02-background.tex:614` · GPTZero: human · clarity, flow

> How far that is in physical units is set by the width of the stencil and by the grid spacing.

**Issue.** The paragraph is titled 'Locality and reach', but 'reach' is never defined. Later chapters build on 'physical reach at lesion scale', and l.663 and l.894 already use the word, so the term should be fixed here on first use.

**Suggestion.**

> This distance, the \emph{reach} of the stencil, is set in physical units by the width of the stencil and by the grid spacing.

### 2b.11 [medium] §2.2.2 Stepping in time

`02-background.tex:622` · GPTZero: AI · flow, ai-tone

> Once every spatial derivative is replaced by a stencil, the solver is left with a function $f$ that maps the current grid values to a rate of change for every cell. The spatial part of the problem is then settled, and the remaining task is to advance the grid in time using this rate.

**Issue.** This nearly repeats the definition of $f$ at l.571-572 and pads it with a transition sentence ('The spatial part of the problem is then settled, and the remaining task is ...'). The redundancy is noticeable and reads as generated.

**Suggestion.**

> The stencils of \S\ref{sec:background:pde-solvers:stencils} reduce the spatial part of the problem to the rate function $f$; the grid then has to be advanced in time with this rate.

### 2b.12 [low] §2.2.2 Stepping in time

`02-background.tex:655` · GPTZero: AI · clarity, ai-tone

> An update written as the current state plus $\Delta t$ times a rate, as in~\eqref{eq:bg:euler}, returns the current state at $\Delta t = 0$ by construction; this is called the \emph{residual} form.

**Issue.** In the clause after the semicolon, the name 'residual form' can attach to the property instead of to the form of the update. Naming the form first reads more naturally and removes the stock 'by construction'.

**Suggestion.**

> An update written as the current state plus $\Delta t$ times a rate, as in~\eqref{eq:bg:euler}, is said to be in \emph{residual} form; it returns the current state at $\Delta t = 0$ whatever the rate.

### 2b.13 [low] §2.2.2 Stepping in time

`02-background.tex:669` · GPTZero: human · tone

> Seen the other way round, a stencil used with a given step must be wide enough to cover the distance the solution moves during that step.

**Issue.** 'Seen the other way round' is a conversational idiom, and the sentence is an equivalent restatement of the CFL condition.

**Suggestion.**

> Equivalently, a stencil used with a given step must be wide enough to cover the distance the solution moves during that step.

### 2b.14 [medium] §2.2.3 Strengths and limits

`02-background.tex:702` · GPTZero: AI · ai-tone, tone

> Their limits follow from the same design. The equation $F$ must be known, including its coefficients: the solver computes what $F$ prescribes and nothing else.

**Issue.** A colon reveal ending in the punchline 'and nothing else' gives the sentence a rhetorical, aphoristic finish.

**Suggestion.**

> Their limits follow from the same design. The equation $F$, including its coefficients, must be known, because the solver can only compute what $F$ prescribes.

### 2b.15 [medium] §2.2.3 Strengths and limits

`02-background.tex:708` · GPTZero: AI · tone, ai-tone

> And accuracy is expensive: fine features need fine grids, the CFL condition then forces small steps, and the cost grows faster than the resolution.

**Issue.** The sentence opens with 'And' and continues with a colon reveal, which gives it a conversational, slogan-like rhythm.

**Suggestion.**

> Accuracy is also expensive. Fine features need fine grids, the CFL condition then forces small time steps, and the cost grows faster than the resolution.

### 2b.16 [low] §2.2.4 Neural solvers that keep the mechanisms

`02-background.tex:727` · GPTZero: AI · clarity

> Graph neural networks built this way simulate fluids, deformable materials and cloth \citep{SanchezGonzalez2020, Pfaff2021}, and a graph-network weather forecaster trained on decades of reanalysis data outperforms a leading operational numerical model on most of its verification targets \citep{Lam2023}.

**Issue.** Two separate examples are joined into one long sentence of about 45 words. The second carries its own claim and reads better on its own.

**Suggestion.**

> Graph neural networks built this way simulate fluids, deformable materials and cloth \citep{SanchezGonzalez2020, Pfaff2021}. A graph-network weather forecaster trained on decades of reanalysis data outperforms a leading operational numerical model on most of its verification targets \citep{Lam2023}.

### 2b.17 [low] §2.2.4 Neural solvers that keep the mechanisms

`02-background.tex:733` · GPTZero: AI · clarity *(added in verification)*

> The message-passing solver of \citet{Brandstetter2022} (MP-PDE) makes the correspondence explicit.

**Issue.** The antecedent of 'the correspondence' sits two sentences back, before the weather-forecasting example, so on first reading it is unclear what corresponds to what.

**Suggestion.**

> The message-passing solver of \citet{Brandstetter2022} (MP-PDE) makes the correspondence between message passing and a classical stencil explicit.

### 2b.18 [medium] §2.2.4 Neural solvers that keep the mechanisms

`02-background.tex:736` · GPTZero: AI · ai-tone, clarity

> One round of message passing computes, at every node, a learned function of its neighbours' values and their differences to its own --- a learned, non-linear stencil.

**Issue.** An em-dash appositive delivers the punchline, one of the clearest structural tells in the range. 'their differences to its own' also leaves 'own' without its noun.

**Suggestion.**

> One round of message passing computes at every node a learned function of its neighbours' values and of their differences to its own value; it thus acts as a learned, non-linear stencil.

### 2b.19 [medium] §2.2.4 Neural solvers that keep the mechanisms

`02-background.tex:745` · GPTZero: AI · ai-tone, clarity

> What the learned version gains is that $f$ no longer has to be written down: it is fitted to data, so the solver can be used where the equation is expensive to solve, known only approximately, or not known at all, and it can often run on coarser grids with larger steps. What it loses are the guarantees.

**Issue.** The mirrored pseudo-cleft pair ('What X gains is ... What it loses are ...') is a typical symmetrical structure of generated text. The first sentence is also overloaded (a colon plus two coordinated clauses).

**Suggestion.**

> A learned solver does not require $f$ to be written down. Because $f$ is fitted to data, the solver can be used where the equation is expensive to solve, known only approximately, or unknown, and it can often run on coarser grids with larger steps. In exchange, the classical guarantees are lost.

### 2b.20 [medium] §2.2.5 Why this structure suits GA progression

`02-background.tex:758` · GPTZero: AI · ai-tone, tone

> GA progression has no known governing equation. Its data are not a densely simulated trajectory but a few observed states per eye (\S\ref{sec:background:ga-oct:muw}). A classical solver is therefore not an option, but the structure it is built from matches the problem in four respects, which is why the thesis adopts it.

**Issue.** Three consecutive sentences contain an antithesis ('not X but Y'), the conversational 'not an option' and a trailing cleft ('which is why the thesis adopts it').

**Suggestion.**

> GA progression has no known governing equation, and its data are a few observed states per eye (\S\ref{sec:background:ga-oct:muw}) instead of a densely simulated trajectory. A classical solver therefore cannot be used. The structure such a solver is built from, however, matches the problem in four respects, and the thesis adopts it for these reasons.

### 2b.21 [medium] §2.2.5 Why this structure suits GA progression (bullet: Change driven by the neighbourhood)

`02-background.tex:771` · GPTZero: AI · ai-tone

> Whether a pixel becomes atrophic depends on what surrounds it --- the situation a stencil is designed for.

**Issue.** The em-dash closes the bullet with a slogan-like fragment.

**Suggestion.**

> Whether a pixel becomes atrophic depends on what surrounds it, and a stencil is designed for this situation.

### 2b.22 [low] §2.2.5 Why this structure suits GA progression (bullet: Slow change)

`02-background.tex:775` · GPTZero: AI · clarity, tone

> The residual form, which predicts only the change and returns the current state as $\Delta t \to 0$, starts from the right default.

**Issue.** 'starts from the right default' is vague and informal; the reader has to infer that the default is the unchanged state and why it is 'right'.

**Suggestion.**

> The residual form predicts only the change and returns the current state as $\Delta t \to 0$; its default, the unchanged state, suits data that change slowly.

### 2b.23 [low] §2.2.5 Why this structure suits GA progression (bullet: Irregular steps)

`02-background.tex:779` · GPTZero: AI · tone

> A solver step is naturally parameterised by $\Delta t$, so the step can be the real interval rather than a fixed one.

**Issue.** 'naturally' is filler, and 'the real interval' is slightly loose.

**Suggestion.**

> A solver step is parameterised by $\Delta t$, so each step can use the actual interval between two visits instead of a fixed one.

### 2b.24 [low] §2.2.5 Why this structure suits GA progression

`02-background.tex:784` · GPTZero: AI · ai-tone

> These are reasons to expect the structure to fit, not evidence that it does.

**Issue.** A balanced aphoristic antithesis ('X, not Y') used as a paragraph opener and closer. The hedge itself is correct and must stay.

**Suggestion.**

> These four points motivate the structure but are not evidence that it fits.

### 2b.25 [medium] §2.2.5 Why this structure suits GA progression

`02-background.tex:786` · GPTZero: AI · clarity

> The CFL argument suggests that an operator applied once per visit has to see at least as far as the lesion front moves between visits, and on the anisotropic en-face grid that distance is very different when counted in pixels along each axis.

**Issue.** This is a long two-part sentence, and 'that distance is very different when counted in pixels along each axis' is awkward. The key point, that the pixel counts differ between the two axes, needs its own sentence.

**Suggestion.**

> The CFL argument suggests that an operator applied once per visit has to see at least as far as the lesion front moves between visits. On the anisotropic en-face grid, this distance corresponds to very different numbers of pixels along the two axes.

### 2b.26 [low] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:799` · GPTZero: AI · ai-tone, clarity

> Neural PDE solvers broadly separate into two paradigms. Neural operators learn a continuous map $M: [0, T] \times \mathcal{F} \to \mathcal{F}$ such that $M(t, u_0) = u(t)$, thereby predicting the solution at any arbitrary time directly from the initial condition.

**Issue.** 'paradigms' is inflated, 'any arbitrary' is redundant, and the participial tail 'thereby predicting' is a common generated pattern. $\mathcal{F}$ is also used without definition.

**Suggestion.**

> Neural PDE solvers fall broadly into two groups. Neural operators learn a continuous map $M: [0, T] \times \mathcal{F} \to \mathcal{F}$ such that $M(t, u_0) = u(t)$, and so predict the solution at any time directly from the initial condition. [Optional: a short 'where $\mathcal{F}$ is a space of functions on $\mathcal{X}$' would define the symbol, and $u_0$ here vs $u^{0}$ in \S\ref{sec:background:pde-solvers} could become one symbol.]

### 2b.27 [medium] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:806` · GPTZero: AI · ai-tone, tone

> Note that when the step size $\Delta t$ is fixed by the dataset, the explicit dependence on it is usually suppressed in the notation. This thesis cannot suppress it because clinical observation intervals are fundamentally irregular.

**Issue.** 'Note that' is a meta-instruction to the reader, and 'fundamentally' is an intensifier (one of four in this range).

**Suggestion.**

> When the step size $\Delta t$ is fixed by the dataset, the dependence on it is usually omitted from the notation. Here it cannot be omitted, because the intervals between clinical visits are irregular.

### 2b.28 [medium] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:811` · GPTZero: AI · ai-tone, clarity

> Neural operators take several structural forms. Finite-dimensional variants are bound to the specific grid geometry they were trained on. Infinite-dimensional variants decouple the learned operator from the spatial discretisation altogether. The Fourier Neural Operator \citep{Li2021} parameterises a kernel integral operator in the Fourier domain. This formulation gives the network global spatial support in a single layer.

**Issue.** Five uniformly short sentences, an empty opening announcement ('take several structural forms'), a mirrored pair ('Finite-dimensional variants ... Infinite-dimensional variants ...') and the intensifier 'altogether' together give a clearly robotic rhythm.

**Suggestion.**

> Finite-dimensional neural operators are bound to the grid geometry they were trained on, whereas infinite-dimensional ones are defined independently of the spatial discretisation. The Fourier Neural Operator \citep{Li2021} parameterises a kernel integral operator in the Fourier domain, which gives the network global spatial support within a single layer.

### 2b.29 [medium] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:818` · GPTZero: AI · ai-tone, clarity

> Alternatively, DeepONet \citep{Lu2021} factorises the operator into a branch network that encodes the input function and a trunk network that encodes the continuous query coordinate. A standard limitation applies to both variants: the trained operator is inherently tied to the equation family it was trained on, and extrapolation beyond the temporal horizon seen during training is reliably poor.

**Issue.** 'Alternatively' is a weak connector, and 'A standard limitation applies' sets up a colon reveal. 'inherently' is an intensifier, and 'reliably poor' is an odd collocation, since 'reliably' normally carries a positive sense.

**Suggestion.**

> DeepONet \citep{Lu2021} instead factorises the operator into a branch network that encodes the input function and a trunk network that encodes the continuous query coordinate. Both share a well-known limitation: a trained operator is tied to the equation family it was trained on, and its extrapolation beyond the temporal horizon seen during training is consistently poor.

### 2b.30 [medium] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:825` · GPTZero: AI · ai-tone, tone

> The autoregressive framing is the natural fit for clinical longitudinal data. Each visit-to-visit transition fundamentally constitutes one step. Furthermore, there is no shared temporal origin ($t = 0$) across patients, making a direct time-dependent mapping ill-posed. Finally, the required prediction horizon is set by the clinic rather than by the model, which necessitates a system that can be stepped forward as many times as a given patient's schedule dictates.

**Issue.** The paragraph is a 'Furthermore ... Finally' enumeration with no 'first', built on inflated verbs ('fundamentally constitutes', 'necessitates', 'dictates'). GPTZero judged the first two sentences human and the enumerated tail AI.

**Suggestion.**

> The autoregressive framing is the natural fit for clinical longitudinal data. Each visit-to-visit transition constitutes one step. Since there is no shared temporal origin ($t = 0$) across patients, a direct time-dependent mapping is ill-posed. In addition, the prediction horizon is set by the clinic rather than by the model, so the model has to support as many steps as a patient's visit schedule requires.

### 2b.31 [medium] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:834` · GPTZero: AI · flow, clarity

> The principal cost of the autoregressive framing is error accumulation. After the first step, the solver consumes its own output rather than numerical ground truth. The input distribution at test time therefore differs systematically from the distribution seen during training. This distribution shift is the central training difficulty for autoregressive rollouts.

**Issue.** The paragraph introduces error accumulation as new, although §2.2.4 (l.749-753) already explained it and pointed here. 'at test time' may also confuse readers in a thesis that states it has no test split; 'during a rollout' is the intended meaning.

**Suggestion.**

> The principal cost of this framing is the error accumulation noted in \S\ref{sec:background:pde-solvers:neural}: after the first step, the solver consumes its own output instead of numerical ground truth, so the inputs it receives during a rollout differ systematically from those seen in training. This distribution shift is the central training difficulty for autoregressive rollouts.

### 2b.32 [low] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:841` · GPTZero: human · clarity

> \citet{Brandstetter2022} propose two mechanisms against it together with their message-passing solver (\S\ref{sec:background:pde-solvers:neural}).

**Issue.** 'against it' points back across a paragraph break, and 'together with their message-passing solver' sits awkwardly at the end of the sentence.

**Suggestion.**

> Together with their message-passing solver (\S\ref{sec:background:pde-solvers:neural}), \citet{Brandstetter2022} propose two mechanisms against this distribution shift.

### 2b.33 [low] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:854` · GPTZero: AI · tone *(added in verification)*

> An update operator is zero-stable if a small perturbation of its input changes the output only by a bounded multiple, $\lVert \mathcal{A}(u^0 + \epsilon) - u^1 \rVert \leq \kappa \lVert \epsilon \rVert$, and the pushforward loss pushes the constant $\kappa$ down.

**Issue.** 'pushes the constant down' is informal and produces an unintended echo of 'pushforward'.

**Suggestion.**

> An update operator is zero-stable if a small perturbation of its input changes the output only by a bounded multiple, $\lVert \mathcal{A}(u^0 + \epsilon) - u^1 \rVert \leq \kappa \lVert \epsilon \rVert$, and the pushforward loss reduces the constant $\kappa$.

### 2b.34 [medium] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:861` · GPTZero: human · clarity

> Chapter~\ref{ch:method} describes how the framework of this thesis uses the two mechanisms.

**Issue.** After a paragraph on consistency and zero stability, 'the two mechanisms' can be misread as those two properties. 'uses' also implies that both temporal bundling and the pushforward trick are used, but Chapter 4 removes bundling (04-method.tex l.436). A neutral verb avoids the misreading without previewing the decision.

**Suggestion.**

> Chapter~\ref{ch:method} describes how the framework of this thesis treats temporal bundling and the pushforward trick.

### 2b.35 [medium] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:871` · GPTZero: AI · ai-tone, clarity

> Surrogate architectures also vary fundamentally in their spatial context. Global spectral operators, such as the Fourier Neural Operator, contrast directly with local convolutional or message-passing operators. Hybrid architectures combine these properties by adding a small local kernel bypass to a global operator to capture high-frequency details more effectively \citep{LiuSchiaffini2024}.

**Issue.** 'vary fundamentally' and 'contrast directly' are filler. The second sentence names a contrast without saying what it is, so 'combine these properties' is vague.

**Suggestion.**

> The architectures also differ in their spatial context: global spectral operators such as the Fourier Neural Operator couple all grid points within one layer, whereas convolutional and message-passing operators are local. Hybrid architectures add a small local kernel bypass to a global operator to capture high-frequency details more effectively \citep{LiuSchiaffini2024}.

### 2b.36 [medium] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:878` · GPTZero: AI · ai-tone, clarity

> Finite Element Networks \citep{Lienen2022} adopt a different numerical perspective, building the neural update directly from a finite-element discretisation with learned dynamics and, in their transport variant, carrying an explicit transport (advection) term.

**Issue.** 'adopt a different numerical perspective' is an empty abstract phrase. It is followed by a chain of two participles with an inserted qualifier, a typical generated sentence shape.

**Suggestion.**

> Finite Element Networks \citep{Lienen2022} build the neural update directly from a finite-element discretisation with learned dynamics, and their transport variant carries an explicit transport (advection) term.

### 2b.37 [**HIGH**] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:882` · GPTZero: AI · tone, ai-tone, clarity

> Finally, because a residual step resembles one explicit Euler step, a Neural-ODE reading is sometimes applied \citep{Chen2018}. Under this interpretation, a higher-order integrator such as a Runge--Kutta scheme can in principle replace the residual step. It must be stated plainly that this reading is only legitimate if the trained model is nearly invariant to the solver used at inference. This property must be tested empirically rather than assumed, as classical solver guarantees do not automatically transfer to neural parameterisations \citep{Ott2021, Krishnapriyan2023}.

**Issue.** 'It must be stated plainly that' is a dramatic meta-statement, and 'must ... must' repeats in consecutive sentences. 'A Neural-ODE reading' is used without saying what it is; the plain explanation only appears in Related Work (l.956-957).

**Suggestion.**

> Finally, because a residual step resembles one explicit Euler step, the network is sometimes read as the right-hand side of an ordinary differential equation, which turns the model into a Neural ODE \citep{Chen2018}. A higher-order integrator such as a Runge--Kutta scheme can then in principle replace the residual step. This reading is only legitimate if the trained model is nearly invariant to the solver used at inference. The property has to be tested empirically rather than assumed, because classical solver guarantees do not automatically transfer to neural parameterisations \citep{Ott2021, Krishnapriyan2023}.

### 2b.38 [medium] §2.3 Neural PDE Solvers and Surrogate Architectures

`02-background.tex:892` · GPTZero: AI · ai-tone, clarity

> These architecture families differ in a small number of structural properties. The primary distinctions lie in whether the operator has spatial context at all, how far that context physically reaches, whether it combines global and local information, and whether it carries an explicit transport term. This thesis refers to these structural differences as inductive-bias ingredients.

**Issue.** An announcement sentence, then 'The primary distinctions lie in', then a four-part 'whether ... whether' list form a symmetrical, generated pattern. 'Inductive bias' first appears here in the rendered text of Chapters 1-2 and is not explained; Chapter 1 (l.155) calls the same idea 'built-in assumptions'.

**Suggestion.**

> The architecture families differ mainly in four structural properties: whether the operator has spatial context at all, how far that context physically reaches, whether it combines global and local information, and whether it carries an explicit transport term. Such built-in assumptions of a model are called its inductive biases, and this thesis refers to the four properties as inductive-bias ingredients.

### 2b.39 [medium] §2.4 Related Work

`02-background.tex:904` · GPTZero: AI · clarity

> Learning-based models for OCT-based age-related macular degeneration and geographic atrophy progression divide broadly into cohort-level risk models and spatial-progression models.

**Issue.** The noun stack can be misparsed as 'OCT-based age-related macular degeneration' (the disease is not OCT-based), and the opening sentence of the section is hard to read in one pass.

**Suggestion.**

> Learning-based models of AMD and GA progression on OCT fall broadly into cohort-level risk models and spatial-progression models.

### 2b.40 [low] §2.4 Related Work

`02-background.tex:911` · GPTZero: AI · clarity

> For the conversion of intermediate AMD to macular atrophy or neovascularisation, \citet{Vogl2021} provided a topographic analysis of the retinal and choroidal layer changes that precede it.

**Issue.** A long fronted prepositional phrase ends in 'it', which the reader has to resolve back to the start of the sentence.

**Suggestion.**

> \citet{Vogl2021} provided a topographic analysis of the retinal and choroidal layer changes that precede the conversion of intermediate AMD to macular atrophy or neovascularisation.

### 2b.41 [medium] §2.4 Related Work

`02-background.tex:914` · GPTZero: AI · ai-tone, clarity

> \citet{Vallino2024} noted that artificial intelligence applied to OCT has the potential to provide predictive probabilities of GA development over time, which positions OCT as a candidate predictive substrate for structural endpoints.

**Issue.** A trailing 'which positions X as Y' clause adds an editorial conclusion in jargon ('candidate predictive substrate for structural endpoints'), a recognisable generated tail.

**Suggestion.**

> \citet{Vallino2024} noted that artificial intelligence applied to OCT has the potential to provide predictive probabilities of GA development over time, which makes OCT a candidate data source for predicting structural endpoints.

### 2b.42 [medium] §2.4 Related Work

`02-background.tex:924` · GPTZero: AI · ai-tone, tone

> The input regime, however, is fundamentally different. While that prior work operates directly on raw OCT volumes, the present thesis consumes pre-segmented lesion masks and layer surfaces. This difference must be kept in mind whenever the approaches are compared.

**Issue.** 'fundamentally' is an intensifier, 'While ..., the present thesis consumes ...' is a symmetrical contrast, and 'must be kept in mind' reads as an instruction to the reader. The caveat itself has to stay with full weight.

**Suggestion.**

> The inputs, however, differ in kind: that work operates directly on raw OCT volumes, whereas this thesis takes pre-segmented lesion masks and layer surfaces as input. Any comparison between the two approaches has to take this difference into account.

### 2b.43 [low] §2.4 Related Work

`02-background.tex:929` · GPTZero: human · clarity

> As a precedent for dense convolutional architectures on this task, \citet{Salvi2025} predicted future GA growth using a two-dimensional U-Net on fundus autofluorescence images, a multi-scale spatial approach on an alternative modality.

**Issue.** The trailing appositive 'a multi-scale spatial approach on an alternative modality' is loosely attached and could refer either to the images or to the U-Net.

**Suggestion.**

> As a precedent for dense convolutional architectures on this task, \citet{Salvi2025} predicted future GA growth with a two-dimensional U-Net, a multi-scale spatial model, applied to fundus autofluorescence images instead of OCT.

### 2b.44 [**HIGH**] §2.4 Related Work

`02-background.tex:934` · GPTZero: AI · ai-tone, flow, tone

> The prevailing formulation in the clinical literature rests on cohort-level, categorical, time-to-conversion prediction. By contrast, the formulation used here dictates a per-eye, per-time-step prediction of the full spatial next state. Consequently, this thesis sits at the intersection of applied medical-imaging deep learning and PDE-solver inductive biases.

**Issue.** This is the most generated-sounding passage in the range: a 'By contrast ... Consequently' connective chain, a stacked three-adjective list, the vague verb 'dictates' and the stock phrase 'sits at the intersection of'. Its placement after the Mai and Salvi paragraph is a separate flow issue (see flow_notes).

**Suggestion.**

> Most of the clinical literature formulates prediction at cohort level, as a categorical time-to-conversion problem. The formulation used here instead requires a per-eye, per-time-step prediction of the full spatial next state. The thesis therefore combines applied medical-imaging deep learning with the inductive biases of PDE solvers. [Leave the following sentence, 'The application of neural PDE solvers to biomedical problems remains sparse.', and its TODO comment unchanged.]

### 2b.45 [low] §2.4 Related Work

`02-background.tex:946` · GPTZero: AI · clarity *(added in verification)*

> The architectures that fill the operator slot of Chapter~\ref{ch:method} originate in different lines of work.

**Issue.** 'operator slot' first appears here in the rendered text of Chapters 1-3 (grep). Chapter 1 only says that 'the operator is the only part that changes', so the jargon term arrives without introduction.

**Suggestion.**

> The architectures used as the exchangeable operator of the framework in Chapter~\ref{ch:method} originate in different lines of work.

### 2b.46 [low] §2.4 Related Work

`02-background.tex:950` · GPTZero: AI · flow

> The U-Net was introduced by \citet{Ronneberger2015} for biomedical image segmentation, the Fourier Neural Operator by \citet{Li2021}, and its extension with local kernels by \citet{LiuSchiaffini2024}.

**Issue.** This repeats §2.3 (l.866-869, where the U-Net's origin in segmentation is already stated), so the reader meets the same fact twice within two pages.

**Suggestion.**

> The U-Net was introduced by \citet{Ronneberger2015}, the Fourier Neural Operator by \citet{Li2021}, and its extension with local kernels by \citet{LiuSchiaffini2024}.

