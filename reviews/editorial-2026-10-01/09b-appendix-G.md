# Micro feedback G: Appendix G The Moving-Mesh Extension (MM-PDE)

[← Overview](00-overview.md)

51 findings: 0 high, 33 medium, 18 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

Appendix G has a sound order that mirrors the main text. It gives the original method (G.1), the adaptation (G.2), a check that the mesh itself is valid (G.3), the result with its scope (G.4) and an outlook. The argument moves logically from "the mesh is valid" to "the correction branch never engages" to "the result is about this implementation, not about mesh adaptation".

The opening is the weakest part. The chapter starts straight with the details of Hu et al. and never says why the reader is here. The purpose arrives only at the end of G.1, as a one-sentence paragraph, and the roadmap for the whole appendix sits inside G.2 under "This section".

The register is uneven. G.1 was moved from an earlier Background draft and nearly all of it is GPTZero-flagged. It is full of intensifiers and signposting adverbs ("fundamentally", "Crucially", "Intuitively", "critical", "inevitably ... useless", "exclusively") and runs of same-length "The X ensures/keeps/dictates" sentences. G.2-G.4 are much closer to the author's plain, unflagged voice but are dense with specification, and many sentences end in a semicolon clause on a different topic.

Several overloaded terms are the main source of misreading:
- "branch" means both the DeepONet branch network and the two solver branches;
- $M$, $I$, $f$ and $\alpha$ each carry two meanings within the chapter.

Some information arrives late:
- The backbone of the reported dual runs (k-NN with mean and maximum aggregation) is only hinted at in the parameter paragraph and stated fully only in G.4.
- The gradient-clipping groups are split across two paragraphs.
- The bypass control is defined inside a paragraph about parameter counts.

In G.4, "A probe ... shows why the gate stays shut" reads against the closing "why the correction branch does not engage here is not explained". The pre-registration sentence also comes after the scope statement it motivates.

### Transitions

- Chapter opening (91-appendix.tex l. 391-398): G.1 begins with no orientation. Add two or three sentences directly under the chapter heading, built from l. 512-513 and l. 521-537, e.g.: 'This appendix reports the moving-mesh extension of \citet{Hu2024} as an additional experiment. It tests whether mesh adaptation gives a measurable benefit on slowly evolving clinical data. \S\ref{app:mm-pde:background} summarises the original method, \S\ref{app:mm-pde:extension} its adaptation to GA, \S\ref{app:mm-pde:mesh-quality} the quality of the meshes and \S\ref{app:mm-pde:result} the result.' Then delete the one-sentence paragraph at l. 512-513 and the roadmap at l. 535-537.
- End of G.1 -> start of G.2 (l. 512-527): the question sentence and the G.2 opener ('This section describes how ...') restate the same purpose back to back. Once the question has moved to the chapter opening, G.2 can start directly with the adaptation (see the finding at l. 521).
- G.1, l. 502-503: the sentence on the classical background (\citet{HuangRussell2011}) sits between ItpNet and the ablations, where it interrupts. Move it into the second paragraph, directly after '... the original graph topology.' (l. 413), where $r$-adaptation has just been introduced.
- G.2 intro, l. 535-537: the roadmap covers G.2.1, G.2.2, G.3 and G.4, but it sits inside G.2 under 'This section'. Move it to the chapter opening (see above).
- G.2.1, l. 610: 'Quality improved with the number of epochs' uses mesh quality before its metrics are defined in G.3. Add a forward pointer: 'Mesh quality (\S\ref{app:mm-pde:mesh-quality}) improved ...'.
- G.2.2, l. 661 and l. 677: the reader cannot tell which uniform-branch graph the reported runs use. The k-NN paragraph mentions the dilated stencil, l. 716-719 speak only of 'the configuration of the five-fold runs', and only G.4 (l. 824-826) says that these runs use the earlier k-NN network with mean and maximum aggregation. Disclose this right after l. 662 (see the finding at l. 661).
- G.2.2, l. 670-671 vs l. 709-714: gradient clipping is described in two places. 'and its own gradient-clipping group' for the gate comes several sentences before the five-group clipping paragraph. Delete that clause at l. 671 and keep the information in the clipping paragraph only.
- G.2.2, l. 716-727: one paragraph covers three topics: parameter counts, the definition of the bypass control, and the comparison scope of the single-branch arms. Start a new paragraph at 'The bypass control loads ...' (l. 720). The bypass control is the key instrument of G.4 and deserves its own paragraph.
- G.3, l. 769-782: the results paragraph moves through folding, the in-sample caveat, pool comparability, the ablation values, seed spread and the unverified boundary weight. Split after 'the spread pool is the unbiased one.' (l. 774), so that the second paragraph opens with the ablation comparison and ends with the unverified choice.
- G.4, l. 873 vs l. 909-911: 'A probe ... shows why the gate stays shut' and 'why the correction branch does not engage here is not explained by these experiments' read as a contradiction. Make both scopes explicit: the probe explains why a near-zero gate stays near zero, and the closing sentence concerns why the branch fails to engage in the first place (see the findings at l. 873 and l. 908).
- G.4, l. 899-911: the pre-registered reading (l. 905-908) comes after the statement that it is not valid (l. 903-905). Use this order: the summary, the pre-registered reading, that the bypass control invalidates it, the implementation-scoped statement, then the contrast with Hu et al. (see the finding at l. 903).
- G.4 -> Outlook (l. 899-921): the result says the correction branch does not engage, with or without a mesh. The Outlook then proposes a better monitor without relating it to that result. Optionally add one hedged bridging sentence (see the finding at l. 918); the author should decide whether that inference is wanted.

### Recurring tells in this part

- Intensifiers and filler adverbs, concentrated almost entirely in G.1 (~17 occurrences). Examples: 'fundamentally inefficient', 'while simultaneously', 'entirely supervised' / 'collapsing entirely' / 'trained entirely without', 'precisely where', 'every single cell', 'the identical amount', 'Crucially', 'critical', 'inevitably yields a tangled and useless mesh', 'applied exclusively', 'subsequently frozen', 'dedicated physics loss', 'covered extensively'. One more in G.2: 'used at all' (l. 532). Fix: delete them; no claim depends on them.
- Sentence-opening signpost adverbs, a typical machine rhythm (6, all in G.1): 'Conversely,', 'Specifically,', 'Intuitively,', 'Crucially,', 'In this formulation,', 'Here,'. Fix: drop them or merge the sentence with its neighbour.
- Personified abstractions and agentive verbs for things that do not act (~10). Examples: 'a property that is hostile to ... training', '$\alpha$ dictates the trade-off', 'The network architecture reformulates', 'The network is tasked with', 'A learnable scalar gate ... decides', 'the correction has to earn its weight', 'The edge gain asks whether', 'The values ... say nothing about', 'This is a statement ... It says nothing', 'gives the gate no reason to open'. Fix: use 'sets', 'measures', 'do not show', or the passive.
- Gate and branch metaphors plus informal mechanical images (roughly a dozen). Examples: 'opens', 'stays shut', 'opened the branch', 'earn its weight', 'deadlock', 'throttled', 'levers'. 'opens' is never defined. Keep 'engage' and the gate image as established vocabulary and define 'opens' once. Replace 'throttled', 'levers' and 'earn its weight' with literal wording.
- Balanced mirror pairs and chiasmus (3). Examples: 'The uniform branch supplies a stable global view ..., while the moved branch supplies a locally refined correction'; 'A gate that starts at zero thus gives the branch almost no signal ..., and an untrained branch gives the gate no reason to open'; the em-dash tricolon 'with the moving mesh or ..., with or without weight decay, with or without the gate'.
- Pseudo-cleft and inverted framing (3). Examples: 'Whether mesh adaptation provides a measurable benefit ... is the question this appendix tests'; 'The finding is therefore that ...'; 'weight decay is not what keeps the gate shut'. Fix: state the subject first.
- Aphoristic paragraph closers that restate the paragraph (4). Examples: 'the gate alone supplies the zero start', 'however strong the uniform branch is', 'can therefore not be explained by a broken mesh', 'is the natural continuation'.
- Long specification sentences that end in a semicolon clause on a different topic (~10 in G.2). Examples: '... the identity it is meant to learn; the gradients are clipped and the gate is disabled', '... which bounds the gain at 10; the floor is active at about 12.6 % of the points'. Fix: split into two sentences.
- Overloaded terms and symbols within the chapter (5): - 'branch' means both the DeepONet branch network and the two solver branches; - $M$ is both the monitor and the update operator; - $I$ is both the identity and the interpolation; - $f$ is both the coordinate map and, as $f_\theta$, the operator; - $\alpha$ is both the monitor constant and the gate. G.1 says 'DMM' where G.2-G.4 say 'mesh mover'.
- 'rather than' antitheses (4: l. 451, 496, 526, 891) and 'thus/therefore' chains (~9, sometimes two in one closing pair, as in l. 789-791).
- 'reads' for a score (2: l. 828 'reads 0.4623', l. 893 'the dual model reads 0.5754'). Fix: 'scores' or 'reaches'.

## Findings

### G.1 [medium] §G.1 Background: MM-PDE

`91-appendix.tex:401` · GPTZero: AI · tone, ai-tone

> \citet{Hu2024} extend message-passing neural solvers by integrating an adaptive moving mesh. A uniform mesh is fundamentally inefficient for problems that exhibit localised dynamics. It wastes computational resolution in smooth regions while simultaneously under-resolving sharp gradients, such as wave fronts.

**Issue.** The intensifier 'fundamentally' and the redundant 'while simultaneously' are clear tells. The consequence sits in a separate sentence where a colon would tie it to the claim.

**Suggestion.**

> \citet{Hu2024} add an adaptive moving mesh to message-passing neural solvers. A uniform mesh is inefficient for problems with localised dynamics: it wastes resolution in smooth regions and under-resolves sharp gradients such as wave fronts.

### G.2 [low] §G.1 Background: MM-PDE

`91-appendix.tex:409` · GPTZero: AI · tone, ai-tone

> This changes both the topology and the total degrees of freedom between steps, a property that is hostile to standard graph-network training. Conversely, $r$-adaptation, or moving-mesh adaptation, moves a fixed set of nodes while maintaining both the node count and the original graph topology.

**Issue.** 'hostile to' personifies a property, and 'Conversely,' is a stock connector. The two sentences mirror each other ('both ... and ...' twice).

**Suggestion.**

> This changes the topology and the number of degrees of freedom from step to step, which is poorly suited to standard graph-network training. In $r$-adaptation, or moving-mesh adaptation, a fixed set of nodes is moved, and the node count and the original graph topology are kept.

### G.3 [low] §G.1 Background: MM-PDE

`91-appendix.tex:413` · GPTZero: AI · flow, tone

> Prior neural $r$-adaptation methods were entirely supervised and required ground-truth optimal meshes generated by an expensive classical solver.

**Issue.** 'entirely' is filler. The sentence motivates the 'data-free' mesh mover introduced three paragraphs later, but the link is not signalled.

**Suggestion.**

> Earlier neural $r$-adaptation methods were supervised and required ground-truth optimal meshes from an expensive classical solver; the mesh mover described below needs no such meshes.

### G.4 [medium] §G.1 Background: MM-PDE

`91-appendix.tex:417` · GPTZero: AI · clarity, ai-tone

> The moving-mesh framework is governed by a monitor function. The monitor is defined as $M = (1 + \lVert \nabla u \rVert_2 / \alpha) I$, a matrix-valued function that takes large values precisely where the state solution varies sharply. The identity factor $I$ ensures that the refinement is isotropic. The addition of a constant $+1$ keeps $M$ bounded away from zero, which prevents nodes from collapsing entirely in smooth regions. The global scaling constant $\alpha$ dictates the trade-off between mesh adaptivity and numerical stability. The corresponding mesh density is given by $\rho(x) = \sqrt{\det M(x)}$. This specific functional form is derived from an established upper bound on finite-element interpolation error.

**Issue.** There are seven sentences of near-identical shape ('The X ensures/keeps/dictates/is given by ...'). They carry fillers ('precisely', 'specific', 'established', 'corresponding'), and 'dictates' personifies a constant. This uniform rhythm is the clearest machine pattern in G.1.

**Suggestion.**

> The mesh is controlled by a monitor function, $M = (1 + \lVert \nabla u \rVert_2 / \alpha) I$, a matrix-valued function that is large where the solution varies sharply. The identity factor $I$ makes the refinement isotropic, and the constant $+1$ keeps $M$ bounded away from zero, so that nodes do not collapse in smooth regions. The global scaling constant $\alpha$ sets the trade-off between mesh adaptivity and numerical stability. The mesh density is $\rho(x) = \sqrt{\det M(x)}$; this form follows from an upper bound on the finite-element interpolation error.

### G.5 [medium] §G.1 Background: MM-PDE

`91-appendix.tex:430` · GPTZero: AI · clarity, ai-tone

> A coordinate map $f$ produces an $M$-uniform mesh if the integral of the density $\rho$ over the image of every single cell is equal. Specifically, this integral must equal $\sigma / N$, where $\sigma$ is the total integral of $\rho$ over the domain and $N$ is the total number of cells. Intuitively, every cell must carry the identical amount of monitor-weighted information, which forces cells to shrink in regions where $M$ is large.

**Issue.** The definition is spread over two sentences ('is equal' ... 'Specifically, this integral must equal'). It is padded with 'every single', 'total' (twice) and 'identical', and opened with the signposts 'Specifically,' and 'Intuitively,'.

**Suggestion.**

> A coordinate map $f$ produces an $M$-uniform mesh if the integral of the density $\rho$ over the image of each cell equals $\sigma / N$, where $\sigma$ is the integral of $\rho$ over the domain and $N$ the number of cells. Every cell then carries the same amount of monitor-weighted information, so cells shrink where $M$ is large.

### G.6 [medium] §G.1 Background: MM-PDE

`91-appendix.tex:450` · GPTZero: AI · clarity, tone, ai-tone

> A scalar potential is learned rather than the full vector map because the convexity of $\phi$ is mathematically equivalent to a non-singular Jacobian of $f$. A non-singular Jacobian guarantees that the resulting mesh does not tangle. Crucially, enforcing convexity on a scalar potential is far easier to regularise than imposing a global non-tangling constraint on a vector field.

**Issue.** 'Crucially' is on the author's banned list, and 'mathematically equivalent' is padding. The last sentence is a mixed construction: an act of 'enforcing' is not something one 'regularises'.

**Suggestion.**

> A scalar potential is learned instead of the full vector map because convexity of $\phi$ is equivalent to a non-singular Jacobian of $f$, which guarantees that the mesh does not tangle. Convexity of a scalar potential is far easier to regularise than a global non-tangling constraint on a vector field.

### G.7 [low] §G.1 Background: MM-PDE

`91-appendix.tex:458` · GPTZero: AI · clarity, tone

> The network architecture reformulates the scalar potential residually as $\phi(x) = 0.5 \|x\|^2 + \psi(x)$. The gradient therefore becomes $\nabla \phi = x + \nabla \psi$. The network is tasked with predicting only the displacement field $\psi$. This formulation removes the trivial identity component from the network's objective and ensures that the coordinate map is approximately the identity mapping at initialisation.

**Issue.** 'The network architecture reformulates' and 'is tasked with' are agentive phrasings. $\psi$ is called 'the displacement field', but by the equation just given the displacement is $\nabla\psi$ and $\psi$ is a scalar.

**Suggestion.**

> The potential is written in residual form, $\phi(x) = 0.5 \|x\|^2 + \psi(x)$, so that $\nabla \phi = x + \nabla \psi$. The network predicts only $\psi$, whose gradient is the displacement. This removes the trivial identity component from what the network has to learn and makes the coordinate map approximately the identity at initialisation.

### G.8 [low] §G.1 Background: MM-PDE

`91-appendix.tex:469` · GPTZero: AI · ai-tone

> The DMM is trained entirely without mesh supervision via a dedicated physics loss $L = L_{\text{eq}} + \beta L_{\text{bound}} + \gamma L_{\text{convex}}$. In this formulation, $L_{\text{eq}}$ is the squared residual of the Monge--Amp\`ere equation evaluated at sampled interior points, $L_{\text{bound}}$ enforces the boundary condition, and $L_{\text{convex}}$ penalises violations of convexity.

**Issue.** A filler cluster ('entirely', 'dedicated', 'In this formulation,'). The two sentences can be one with a 'where' clause.

**Suggestion.**

> The DMM is trained without mesh supervision on the physics loss $L = L_{\text{eq}} + \beta L_{\text{bound}} + \gamma L_{\text{convex}}$, where $L_{\text{eq}}$ is the squared residual of the Monge--Amp\`ere equation at sampled interior points, $L_{\text{bound}}$ enforces the boundary condition and $L_{\text{convex}}$ penalises violations of convexity.

### G.9 [medium] §G.1 Background: MM-PDE

`91-appendix.tex:475` · GPTZero: AI · tone, ai-tone

> The convexity term is critical; a non-convex potential inevitably yields a tangled and useless mesh, regardless of how small the equation residual becomes.

**Issue.** Dramatic emphasis: 'critical', 'inevitably' and 'useless' are stacked into one clause.

**Suggestion.**

> The convexity term is needed because a non-convex potential yields a tangled, unusable mesh, however small the equation residual becomes.

### G.10 [low] §G.1 Background: MM-PDE

`91-appendix.tex:478` · GPTZero: AI · tone, ai-tone

> Training uses the Adam optimiser followed by BFGS fine-tuning applied exclusively to the last layer. The DMM is pretrained and subsequently frozen during solver training. This decouples a well-posed geometric problem from the main solver objective and allows the identical mesh mover to be reused across different experiments.

**Issue.** Fillers ('exclusively', 'subsequently', 'identical', 'different') inflate three plain facts.

**Suggestion.**

> Training uses Adam, followed by BFGS fine-tuning of the last layer only. The DMM is pretrained and then frozen during solver training. This separates a well-posed geometric problem from the solver objective and allows the same mesh mover to be reused across experiments.

### G.11 [medium] §G.1 Background: MM-PDE

`91-appendix.tex:485` · GPTZero: not scanned / not matched · clarity

> The full moving-mesh update operator is constructed as a dual-branch composition, defined as $M(u_t) = G_1(u_t) + I(G_2, \tilde{f}, u_t)$.

**Issue.** Symbols clash. At l. 418 $M$ is the monitor and $I$ the identity matrix; here $M$ is the update operator and $I$ the interpolation. $\alpha$ is also the monitor constant at l. 418-423 and the gate from G.2.2 on. 'is constructed as ..., defined as' is redundant.

**Suggestion.**

> The moving-mesh update operator is the dual-branch composition $M(u_t) = G_1(u_t) + I(G_2, \tilde{f}, u_t)$, in which $M$ and $I$ no longer denote the monitor and the identity matrix. (Optionally add after the definition of $\alpha$ at l. 423-424: '(unrelated to the gate $\alpha$ of \S\ref{app:mm-pde:dual})'.)

### G.12 [low] §G.1 Background: MM-PDE

`91-appendix.tex:495` · GPTZero: AI · tone, ai-tone

> The interpolation network, ItpNet, learns adaptive interpolation weights directly from the moved-mesh geometry rather than relying on fixed finite-element basis functions. It is pretrained with its own optimiser before joint dual-branch training begins, because an untrained interpolation would feed unstructured noise into the uniform branch, destabilising the system.

**Issue.** There is a 'rather than relying on' antithesis, the filler 'directly', and a vague, dramatic ending ('destabilising the system').

**Suggestion.**

> The interpolation network, ItpNet, learns adaptive interpolation weights from the moved-mesh geometry instead of using fixed finite-element basis functions. It is pretrained with its own optimiser before the joint training of both branches, because an untrained interpolation would pass unstructured noise to the uniform branch and destabilise the model.

### G.13 [low] §G.1 Background: MM-PDE

`91-appendix.tex:502` · GPTZero: human · flow, clarity

> The classical background for adaptive moving meshes on which this framework builds is covered extensively by \citet{HuangRussell2011}.

**Issue.** This general pointer arrives after the method has been described, between ItpNet and the ablations, where it interrupts. The embedded relative clause 'on which this framework builds' is awkward.

**Suggestion.**

> Move it to the second paragraph, directly after '... the original graph topology.' (l. 413), and reword: 'The classical theory of adaptive moving meshes, on which this framework builds, is treated in detail by \citet{HuangRussell2011}.'

### G.14 [medium] §G.1 Background: MM-PDE

`91-appendix.tex:504` · GPTZero: human · clarity

> \citet{Hu2024} reported several architectural ablations of the dual-branch solver. Removing the uniform-mesh branch, replacing the moved branch by a second branch on the original mesh, removing the residual-cut network of the original model (not used in this thesis), or replacing the DMM mesh by the uniform mesh each increases the error.

**Issue.** The subject is four gerund clauses plus a parenthesis, so the reader waits about 40 words for 'each increases'. The tense also shifts: l. 401 and l. 508 use the present, here the past.

**Suggestion.**

> \citet{Hu2024} report several architectural ablations of the dual-branch solver. The error increases in each of four cases: when the uniform-mesh branch is removed, when the moved branch is replaced by a second branch on the original mesh, when the residual-cut network of the original model (not used in this thesis) is removed, and when the DMM mesh is replaced by the uniform mesh.

### G.15 [medium] §G.1 Background: MM-PDE

`91-appendix.tex:512` · GPTZero: AI · flow, ai-tone

> Whether mesh adaptation provides a measurable benefit for slowly evolving clinical data is the question this appendix tests.

**Issue.** An inverted pseudo-cleft ('Whether X ... is the question this appendix tests') used as a stock closing flourish. It stands alone as a one-sentence paragraph and states the appendix's purpose only after three pages of background, and G.2 then restates it.

**Suggestion.**

> Move the question to a short opening under the chapter heading (see flow notes) and phrase it directly: 'This appendix tests whether mesh adaptation gives a measurable benefit on slowly evolving clinical data.' Delete it here.

### G.16 [low] §G.2 The Moving-Mesh Extension for GA

`91-appendix.tex:521` · GPTZero: AI · flow, clarity, ai-tone

> This section describes how the moving-mesh solver of \citet{Hu2024} (\S\ref{app:mm-pde:background}) was adapted to GA forecasting. A data-free mesh mover and a dual-branch graph network were built on top of the fixed framework of \S\ref{sec:method:framework}. The extension was built in full and evaluated over five folds, and it gave no measurable gain over the uniform grid. For this reason it is reported in this appendix rather than in the main text.

**Issue.** The paragraph opens with an announcement ('This section describes') and repeats 'built'. Four short sentences say what two can.

**Suggestion.**

> The moving-mesh solver of \citet{Hu2024} (\S\ref{app:mm-pde:background}) was adapted to GA forecasting by adding a data-free mesh mover and a dual-branch graph network to the fixed framework of \S\ref{sec:method:framework}. The complete extension was evaluated over five folds and gave no measurable gain over the uniform grid; it is therefore reported here and not in the main text.

### G.17 [medium] §G.2 The Moving-Mesh Extension for GA

`91-appendix.tex:529` · GPTZero: AI · clarity, tone, ai-tone

> The experiment was designed as a measurement. A learnable scalar gate, initialised to zero, decides how much of the correction computed on the moved mesh enters the prediction, so its trajectory shows whether the correction is used at all.

**Issue.** The opener is an empty aphorism, since every experiment is a measurement; what is meant is that the design makes the outcome measurable. 'decides' personifies the gate, and 'at all' is emphatic filler.

**Suggestion.**

> Two elements of the design make the outcome measurable. A learnable scalar gate, initialised to zero, weights the correction computed on the moved mesh before it enters the prediction, so its trajectory shows whether the correction is used.

### G.18 [medium] §G.2.1 Data-Free Mesh Mover for GA

`91-appendix.tex:546` · GPTZero: AI · clarity

> The network branches on the uniform and on the moved mesh still process all eleven channels; only the mesh mover reads the mask alone.

**Issue.** From here on 'branch' means two things: the solver branches (here) and the DeepONet branch network of the mesh mover (l. 554, 578, 613). The clause after the semicolon repeats the paragraph's first sentence.

**Suggestion.**

> The two solver branches, on the uniform and on the moved mesh, still process all eleven channels. Keep 'branch network' for the mesh mover's encoder throughout, e.g. at l. 613: 'The architecture of the branch network made no measurable difference across five variants; the pooled variant is kept because it accepts any grid size.'

### G.19 [low] §G.2.1 Data-Free Mesh Mover for GA

`91-appendix.tex:548` · GPTZero: AI · clarity *(added in verification)*

> An earlier version was trained on a square $256 \times 256$ mask sampled from the fundus image; it was replaced by the native grid, which removes a resize round trip during the rollout.

**Issue.** A trained version is said to be 'replaced by the native grid', which mismatches subject and replacement.

**Suggestion.**

> An earlier version was trained on a square $256 \times 256$ mask sampled from the fundus image. It was replaced by a version trained on the native grid, which removes a resize round trip during the rollout.

### G.20 [low] §G.2.1 Data-Free Mesh Mover for GA

`91-appendix.tex:559` · GPTZero: AI · clarity

> A head maps the concatenated branch and trunk outputs to the scalar potential $\phi$ through widths 1024, 512, 512 and 1, one layer deeper than the base head.

**Issue.** 'the base head' is never defined. The reader cannot tell whether it is the head of \citet{Hu2024} or of the starting configuration of the search.

**Suggestion.**

> A head maps the concatenated branch and trunk outputs to the scalar potential $\phi$ through widths 1024, 512, 512 and 1, one layer deeper than the head of the starting configuration of the search. (Author to confirm which head is meant; l. 775 calls it 'the configuration before the head and blur changes'.)

### G.21 [medium] §G.2.1 Data-Free Mesh Mover for GA

`91-appendix.tex:577` · GPTZero: human · flow, clarity

> Two parts of this monitor were needed. The blur ($\sigma = 1.0$\,px) is applied for the monitor only; the branch always sees the raw binary mask.

**Issue.** 'Two parts' are announced but not named: the blur follows, and the logarithm only three sentences later, after a divergence aside. 'the branch' is ambiguous right after the mention of solver branches at l. 546.

**Suggestion.**

> Two parts of this monitor were needed: the blur and the logarithm. The blur ($\sigma = 1.0$\,px) is applied for the monitor only; the branch network of the mesh mover always sees the raw binary mask.

### G.22 [medium] §G.2.1 Data-Free Mesh Mover for GA

`91-appendix.tex:579` · GPTZero: human · clarity

> A binary mask has a step at the lesion edge, and without the blur the first GA run diverged to NaN. On the native grid, the unblurred monitor no longer diverges but leaves the mesh almost unmoved (\S\ref{app:mm-pde:mesh-quality}).

**Issue.** The contrast 'the first GA run diverged' vs 'On the native grid ... no longer diverges' implies the first run differed in grid or monitor, but the text does not say how. The reader cannot tell what changed.

**Suggestion.**

> A binary mask has a step at the lesion edge, and without the blur the first GA run, [state its setting, e.g. grid and monitor], diverged to NaN. In the final configuration on the native grid, the unblurred monitor no longer diverges but leaves the mesh almost unmoved (\S\ref{app:mm-pde:mesh-quality}).

### G.23 [low] §G.2.1 Data-Free Mesh Mover for GA

`91-appendix.tex:584` · GPTZero: AI · clarity

> Two further ideas were tested and left out: a blur kernel stretched along the columns to match the physical spacing, which gave no gain ($p = 0.95$) and folded the mesh intermittently, and a penalty on the Jacobian determinant, which made folding worse.

**Issue.** A two-item list in which the first item has its own internal 'and' plus a 'which' clause, so it is hard to see where the first item ends.

**Suggestion.**

> Two further ideas were tested and left out. A blur kernel stretched along the columns to match the physical spacing gave no gain ($p = 0.95$) and folded the mesh intermittently. A penalty on the Jacobian determinant made folding worse.

### G.24 [medium] §G.2.1 Data-Free Mesh Mover for GA

`91-appendix.tex:605` · GPTZero: AI · clarity

> Because it never sees a future state, this leaks no label, and it makes the same mesh mover in-distribution for every fold.

**Issue.** Three pronouns refer to different things: 'it' is the mesh mover, 'this' is training on all masks, and the second 'it' is the training again.

**Suggestion.**

> Training on all masks leaks no label, because the mesh mover never sees a future state, and makes the same mesh mover in-distribution for every fold.

### G.25 [low] §G.2.1 Data-Free Mesh Mover for GA

`91-appendix.tex:609` · GPTZero: human · clarity, tone

> The configuration was selected from a 55-run search on the native grid. Quality improved with the number of epochs up to 500. The two largest levers were the extra head layer and the sharper blur of $\sigma = 1$ instead of 2, and they helped only together.

**Issue.** 'Quality' is used before its metrics are defined in G.3, and 'levers' is a business metaphor.

**Suggestion.**

> The configuration was selected from a 55-run search on the native grid. Mesh quality (\S\ref{app:mm-pde:mesh-quality}) improved with the number of epochs up to 500. The two changes with the largest effect were the extra head layer and the sharper blur of $\sigma = 1$ instead of 2, and they helped only together.

### G.26 [medium] §G.2.2 Dual-Branch Composition

`91-appendix.tex:661` · GPTZero: AI · flow, clarity

> Both branches are the graph network of \S\ref{sec:method:mppde}, with two message-passing rounds of width 64.

**Issue.** G.2 never says which graph the uniform branch uses in the reported runs. The next paragraphs mention the dilated stencil (l. 677) and 'the configuration of the five-fold runs' (l. 717), and only G.4 (l. 824-826) names the earlier k-NN network with mean and maximum aggregation. A reader of G.2 will likely assume the stencil.

**Suggestion.**

> Both branches are the graph network of \S\ref{sec:method:mppde}, with two message-passing rounds of width 64. In the five-fold runs of \S\ref{app:mm-pde:result}, the uniform branch is the earlier $k$-nearest-neighbour graph network with mean and maximum aggregation; one further run on fold~2 uses the dilated stencil.

### G.27 [medium] §G.2.2 Dual-Branch Composition

`91-appendix.tex:666` · GPTZero: AI · tone, ai-tone

> At the start the dual model is therefore exactly the uniform branch alone, and the correction has to earn its weight.

**Issue.** 'has to earn its weight' is a conversational idiom that personifies the correction.

**Suggestion.**

> At the start the dual model is therefore exactly the uniform branch alone; the correction contributes only as far as training moves $\alpha$ away from zero.

### G.28 [low] §G.2.2 Dual-Branch Composition

`91-appendix.tex:668` · GPTZero: AI · clarity

> The gate also fixes the scale of the correction: the loss constrains only the sum of the two branches, which could otherwise grow large and cancel each other.

**Issue.** 'which' can attach to 'the sum' instead of 'the two branches', and 'otherwise' has no clear anchor.

**Suggestion.**

> The gate also fixes the scale of the correction. The loss constrains only the sum of the two branches, so without the gate both branches could grow large and cancel each other.

### G.29 [medium] §G.2.2 Dual-Branch Composition

`91-appendix.tex:673` · GPTZero: AI · tone, ai-tone

> If both the decoder and $\alpha$ started at zero, the gradients of both would be exactly zero, a deadlock from which the branch could never activate; the gate alone supplies the zero start.

**Issue.** 'a deadlock from which the branch could never activate' is dramatic, and 'the gate alone supplies the zero start' is an aphoristic closer appended after a semicolon.

**Suggestion.**

> If both the decoder and $\alpha$ started at zero, the gradients of both would be exactly zero, and the branch could never be activated. The zero start is therefore supplied by the gate alone.

### G.30 [medium] §G.2.2 Dual-Branch Composition

`91-appendix.tex:691` · GPTZero: AI · clarity

> The weights of the return direction are renormalised to sum to one at each point, with a sign-preserving floor of 0.1 on the denominator, which bounds the gain at 10; the floor is active at about 12.6\,\% of the points. ItpNet is pretrained at epoch 0 for 25 passes with its own AdamW optimiser \citep{Loshchilov2019}, on the round trip uniform $\to$ moved $\to$ uniform, which should return the input unchanged. The pretraining uses the channel-weighted mean squared error only, because the soft-Dice term would push the operator away from the identity it is meant to learn; the gradients are clipped and the gate is disabled.

**Issue.** Each of the three sentences ends in a tacked-on clause. In the second, the training objective comes after the optimiser. In the third, the clause after the semicolon (clipping, gate) is unrelated to the 'because' clause before it.

**Suggestion.**

> The weights of the return direction are renormalised to sum to one at each point. A sign-preserving floor of 0.1 on the denominator bounds the gain at 10; it is active at about 12.6\,\% of the points. ItpNet is pretrained at epoch 0 for 25 passes, with its own AdamW optimiser \citep{Loshchilov2019}, to return the input unchanged on the round trip uniform $\to$ moved $\to$ uniform. This pretraining uses the channel-weighted mean squared error only, because the soft-Dice term would push the operator away from the identity it is meant to learn. During pretraining, the gradients are clipped and the gate is disabled.

### G.31 [medium] §G.2.2 Dual-Branch Composition

`91-appendix.tex:709` · GPTZero: AI · clarity, tone

> Gradients are clipped to a norm of 1.0 separately in five groups: the uniform branch, the correction branch, the ItpNet weights, the gate $\alpha$ and the layer encoder; the mesh mover is frozen. Under one joint clip, the large gradients of ItpNet, with a median of $10^3$ to $10^4$ in the dual runs against about 1 for the uniform branch, would have throttled the uniform branch.

**Issue.** 'throttled' is an informal metaphor, and the second sentence buries its numbers in a mid-sentence aside. The 'layer encoder' appears without a pointer; in the rendered text it is introduced only briefly in §6.1.

**Suggestion.**

> Gradients are clipped to a norm of 1.0 separately in five groups: the uniform branch, the correction branch, the ItpNet weights, the gate $\alpha$ and the layer encoder of \S\ref{sec:discussion:interpretation}; the frozen mesh mover is excluded. The gradients of ItpNet have a median norm of $10^3$ to $10^4$ in the dual runs, against about 1 for the uniform branch, so a single joint clip would also have scaled down the updates of the uniform branch. (Author: consider stating whether the layer encoder was active in these runs.)

### G.32 [low] §G.3 Moving Mesh Quality

`91-appendix.tex:732` · GPTZero: human · clarity, tone

> The mesh mover was judged on its own terms, independently of the prediction. Four metrics were used. All of them depend only on the mask and use the same reference for every run.

**Issue.** 'on its own terms' is an idiom that adds nothing to 'independently of the prediction'. 'the same reference' is not identified.

**Suggestion.**

> The mesh mover was evaluated independently of the prediction, with four metrics. All four depend only on the mask and use the same [name the reference, e.g. reference monitor] for every run.

### G.33 [medium] §G.3 Moving Mesh Quality

`91-appendix.tex:735` · GPTZero: AI · clarity, ai-tone

> The edge gain asks whether nodes move to the lesion border: the border is widened to a band of half-width 0.02 of the domain, normalised to a grid mean of 1, and averaged at the moved node positions.

**Issue.** 'The edge gain asks' personifies a metric. In the three-step definition after the colon, the participles lose their subject: it is the band, not the border, that is normalised and then averaged.

**Suggestion.**

> The edge gain measures whether nodes move to the lesion border. The border is widened to a band of half-width 0.02 of the domain, the band is normalised to a mean of 1 over the grid, and its values are averaged over the moved node positions.

### G.34 [low] §G.3 Moving Mesh Quality

`91-appendix.tex:740` · GPTZero: AI · clarity *(added in verification)*

> The reference coefficient of variation, \texttt{cov\_ref}, is the standard deviation divided by the mean of the cell areas weighted by one fixed reference monitor, the equidistribution measure of \citet{HuangRussell2011}; lower is more even.

**Issue.** 'the standard deviation divided by the mean of the cell areas weighted by ...' leaves unclear whether 'of the cell areas' applies to both the standard deviation and the mean. The appositive and the semicolon clause pile up at the end.

**Suggestion.**

> The reference coefficient of variation, \texttt{cov\_ref}, is the standard deviation of the cell areas, weighted by one fixed reference monitor, divided by their mean. It is the equidistribution measure of \citet{HuangRussell2011}; lower is more even.

### G.35 [low] §G.3 Moving Mesh Quality

`91-appendix.tex:769` · GPTZero: AI · tone, ai-tone

> No mesh folds: the number of tangled cells is zero on every scored mask, at every seed and every scored epoch. The values are in-sample and say nothing about generalisation to unseen lesions.

**Issue.** 'values ... say nothing' personifies the numbers.

**Suggestion.**

> No mesh folds: the number of tangled cells is zero on every scored mask, at every seed and every scored epoch. The values are in-sample and do not show how the mesh mover generalises to unseen lesions.

### G.36 [medium] §G.3 Moving Mesh Quality

`91-appendix.tex:774` · GPTZero: AI · clarity

> On that pool, the configuration before the head and blur changes reaches an edge gain of 2.24, the same mesh mover without blur 1.34, and without the logarithmic compression 0.94, below the unmoved mesh.

**Issue.** The list is elliptical: verbs and subjects are dropped in items two and three. 'below the unmoved mesh' requires the reader to recall that the unmoved mesh scores 1.

**Suggestion.**

> On that pool, the configuration before the head and blur changes reaches an edge gain of 2.24; the same mesh mover reaches 1.34 without blur and 0.94 without the logarithmic compression, below the value of 1 for the unmoved mesh.

### G.37 [medium] §G.3 Moving Mesh Quality

`91-appendix.tex:779` · GPTZero: AI · clarity

> One choice is unverified. The boundary weight of 1000 was kept although a weight of 100 scored higher on edge gain, by 0.029 on head-16 and 0.105 on spread-16; it was rejected on a lesion-specificity check that was computed only on the biased head-16 pool.

**Issue.** 'it' after the semicolon can refer to the weight of 1000 or the weight of 100. The 'lesion-specificity check' is not explained.

**Suggestion.**

> One choice is unverified: the boundary weight of 1000 was kept although a weight of 100 scored higher on edge gain, by 0.029 on head-16 and 0.105 on spread-16. The weight of 100 was rejected on a lesion-specificity check [one clause on what it measures] that was computed only on the biased head-16 pool.

### G.38 [low] §G.3 Moving Mesh Quality

`91-appendix.tex:785` · GPTZero: AI · clarity

> In all three, nodes are drawn from the surrounding retina towards the lesion, most strongly at its border, and no cell folds.

**Issue.** 'drawn' means 'attracted' here, but in the figure caption (l. 806-807) it means 'plotted'.

**Suggestion.**

> In all three, nodes move from the surrounding retina towards the lesion, most strongly at its border, and no cell folds.

### G.39 [medium] §G.3 Moving Mesh Quality

`91-appendix.tex:789` · GPTZero: AI · clarity, ai-tone

> The mesh mover thus produces valid meshes without folds that concentrate nodes on the lesion border. The null result of \S\ref{app:mm-pde:result} can therefore not be explained by a broken mesh.

**Issue.** 'without folds that concentrate nodes' attaches the relative clause to 'folds', so on first reading the meshes lack folds that concentrate nodes. The 'thus ... therefore' pair is an aphoristic closer, and 'can therefore not' is unidiomatic.

**Suggestion.**

> The mesh mover thus produces valid meshes that have no folds and concentrate nodes on the lesion border, so the null result of \S\ref{app:mm-pde:result} cannot be explained by a broken mesh.

### G.40 [low] §G.4 Result

`91-appendix.tex:857` · GPTZero: AI · clarity

> This is the tightest null result of the project: its standard error is less than half the difference of 0.016 that a five-fold paired mean must exceed.

**Issue.** 'tightest null' is jargon, and the purpose of the 0.016 threshold (to count as an effect) is left implicit.

**Suggestion.**

> It is the most precise null result of the project: its standard error is less than half of 0.016, the difference that a five-fold paired mean must exceed to count as an effect.

### G.41 [medium] §G.4 Result

`91-appendix.tex:864` · GPTZero: AI · clarity

> The gate $\alpha$ never opens, with or without the moving mesh. In every fold of both arms it moves from zero to exactly $\pm 0.0020$ in the first step, one optimiser step from the zero start, as designed. It then peaks at 0.058 to 0.093 in the dual branch and at 0.031 to 0.101 in the bypass control, averages 0.009 to 0.024 and 0.005 to 0.023 in absolute value, and ends near zero in every fold.

**Issue.** 'in the first step, one optimiser step from the zero start' says the same thing twice. In 'averages 0.009 to 0.024 and 0.005 to 0.023' the reader must guess which range belongs to which arm. 'opens' is never defined.

**Suggestion.**

> The gate $\alpha$ never opens, with or without the moving mesh. In every fold of both arms, the first optimiser step moves it from zero to exactly $\pm 0.0020$, as designed. It then peaks at 0.058 to 0.093 in the dual branch and at 0.031 to 0.101 in the bypass control, has a mean absolute value of 0.009 to 0.024 and 0.005 to 0.023, respectively, and ends near zero in every fold. (Optionally define once what value of $\alpha$ counts as open.)

### G.42 [medium] §G.4 Result

`91-appendix.tex:869` · GPTZero: AI · clarity *(added in verification)*

> The range of the bypass control encloses that of the dual branch, and the largest peak of either arm, 0.1005, belongs to a bypass fold.

**Issue.** The previous sentence gives two ranges per arm (peaks and mean absolute values), so 'The range' is ambiguous. For the mean absolute values the statement does not hold (0.005-0.023 does not enclose 0.009-0.024); only the peak range does.

**Suggestion.**

> The peak range of the bypass control encloses that of the dual branch, and the largest peak of either arm, 0.1005, belongs to a bypass fold.

### G.43 [medium] §G.4 Result

`91-appendix.tex:873` · GPTZero: human · flow, clarity

> A probe on the trained dual model shows why the gate stays shut.

**Issue.** This reads as a complete explanation, yet the appendix closes with 'why the correction branch does not engage here is not explained by these experiments'. The probe explains why a near-zero gate stays near zero, not why the branch fails to engage in the first place.

**Suggestion.**

> A probe on the trained dual model shows why the gate, once near zero, stays shut. (Make the closing sentence at l. 908-911 specific as well; see the finding at l. 908.)

### G.44 [medium] §G.4 Result

`91-appendix.tex:878` · GPTZero: AI · tone, ai-tone

> A gate that starts at zero thus gives the branch almost no signal to learn from, and an untrained branch gives the gate no reason to open.

**Issue.** A chiasmus ('gate gives the branch ... branch gives the gate') with personification ('no reason to open'). It is a polished, symmetrical closer.

**Suggestion.**

> With $\alpha$ near zero, the correction branch therefore receives almost no gradient, and while the branch is untrained, a larger $\alpha$ does not lower the loss.

### G.45 [medium] §G.4 Result

`91-appendix.tex:882` · GPTZero: AI · clarity

> Three further runs on fold 2 tested this reading, and none of them opened the branch. Without the gate, with the decoder zero-initialised instead, the change-region Dice falls to 0.3148 against 0.4878 for the gated dual model, a loss of 0.173, about five times the single-fold noise floor of 0.036; the gradient of the correction branch is still zero at the median.

**Issue.** 'opened the branch' mixes the metaphors: the gate opens, the branch engages, and one of the three runs has no gate. The second sentence runs to about 45 words with an unrelated semicolon clause, and the three runs are not marked as first, second and third.

**Suggestion.**

> Three further runs on fold 2 tested this reading; in none of them did the correction branch engage. In the first, the gate is removed and the decoder is zero-initialised instead. The change-region Dice then falls to 0.3148, against 0.4878 for the gated dual model; the loss of 0.173 is about five times the single-fold noise floor of 0.036. The median gradient of the correction branch is still zero.

### G.46 [medium] §G.4 Result

`91-appendix.tex:888` · GPTZero: AI · clarity, ai-tone

> Without weight decay on the correction branch and ItpNet, the Dice is 0.0092 higher than its counterpart, under the single-fold floor; $\alpha$ peaks lower (0.058 against 0.067), and the parameters of the correction branch grow rather than shrink, so weight decay is not what keeps the gate shut.

**Issue.** 'its counterpart' is vague. The sentence chains three findings with a semicolon and ends in a 'rather than' antithesis followed by a pseudo-cleft ('is not what keeps').

**Suggestion.**

> In the second run, weight decay is removed from the correction branch and ItpNet. The Dice is 0.0092 higher than with weight decay, under the single-fold floor, $\alpha$ peaks lower (0.058 against 0.067), and the parameters of the correction branch grow instead of shrinking. Weight decay therefore does not keep the gate shut.

### G.47 [medium] §G.4 Result

`91-appendix.tex:892` · GPTZero: AI · tone, ai-tone

> On the dilated stencil, the dual model reads 0.5754 against 0.6060 for its own single-branch counterpart, a difference of $-0.031$ (per eye $-0.0305 \pm 0.0086$, 3 of 16 eyes), at roughly nine times the cost. The stencil's own gain carries over to the dual model, but the correction branch does not engage, however strong the uniform branch is.

**Issue.** 'reads' is jargon for 'scores'. 'however strong the uniform branch is' is a rhetorical flourish that generalises beyond the single fold-2 run it summarises.

**Suggestion.**

> In the third run, on the dilated stencil, the dual model scores 0.5754 against 0.6060 for its own single-branch counterpart, a difference of $-0.031$ (per eye $-0.0305 \pm 0.0086$, 3 of 16 eyes), at roughly nine times the cost. The gain of the stencil carries over to the dual model, but the correction branch does not engage even with this stronger uniform branch.

### G.48 [medium] §G.4 Result

`91-appendix.tex:899` · GPTZero: AI · ai-tone

> The finding is therefore that the gated correction branch did not engage --- with the moving mesh or with the uniform grid in its place, with or without weight decay, with or without the gate --- and that the dual-branch model gave no measurable gain at about ten times the cost.

**Issue.** A pseudo-cleft opener ('The finding is therefore that') with an em-dash aside holding a rhetorical tricolon. It is the most machine-like sentence in G.4.

**Suggestion.**

> The gated correction branch therefore did not engage in any tested variant (moving mesh or uniform grid in its place, with or without weight decay, with or without the gate), and the dual-branch model gave no measurable gain at about ten times the cost.

### G.49 [medium] §G.4 Result

`91-appendix.tex:903` · GPTZero: human · flow, tone

> This is a statement about this implementation. It says nothing about whether mesh adaptation could help GA forecasting, because the bypass control behaves the same without any mesh. Before the runs, $\alpha \to 0$ had been fixed as a reportable outcome that would mean that mesh adaptation does not help. The bypass control, which was part of the same design, showed that this reading is not valid.

**Issue.** The scope conclusion comes before the pre-registered reading it corrects. 'a statement ... says nothing' personifies, and 'that would mean that' doubles 'that'.

**Suggestion.**

> Before the runs, $\alpha \to 0$ had been fixed as a reportable outcome, to be read as evidence that mesh adaptation does not help. The bypass control, part of the same design, showed that this reading is not valid, because it behaves the same without any mesh. The result is therefore a statement about this implementation; it does not show whether mesh adaptation could help GA forecasting.

### G.50 [medium] §G.4 Result

`91-appendix.tex:908` · GPTZero: human · flow, clarity *(added in verification)*

> \citet{Hu2024} report that their dual branch improves on the uniform grid on their benchmarks; why the correction branch does not engage here is not explained by these experiments.

**Issue.** This reads against the probe paragraph (l. 873), which 'shows why the gate stays shut'. Two unrelated statements are joined by a semicolon.

**Suggestion.**

> \citet{Hu2024} report that their dual branch improves on the uniform grid on their benchmarks. Why the correction branch fails to engage here in the first place is not explained by these experiments.

### G.51 [medium] §G.5 Outlook

`91-appendix.tex:918` · GPTZero: AI · flow, tone, ai-tone

> In the moving-mesh extension, the monitor that guides the mesh is computed from the current state, whereas the change happens in the next one. A monitor built on a surrogate of the next state, the open problem named by \citet{Hu2024}, is the natural continuation.

**Issue.** 'is the natural continuation' is an evaluative closing cliché, and 'the change happens in the next one' is vague. The paragraph does not connect to G.4.

**Suggestion.**

> In the moving-mesh extension, the monitor is computed from the current state, although the change to be resolved appears in the next state. A monitor built on a surrogate of the next state, the open problem named by \citet{Hu2024}, is one possible continuation. (Optionally add a bridge if the author accepts the inference: 'Such a monitor can matter only once the correction branch engages, which it did not in the runs of \S\ref{app:mm-pde:result}.')

