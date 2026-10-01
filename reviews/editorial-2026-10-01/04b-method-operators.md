# Micro feedback 4b: Ch. 4 Method, §4.3.3-4.3.8 (graph construction, dense operators, floors, FEN, RK, parameter matching)

[← Overview](00-overview.md)

48 findings: 1 high, 23 medium, 24 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

The range is technically dense but well ordered. §4.3.3 builds a clean problem-to-solution argument: a physical k-NN graph leaves the rows unconnected, index space restores connectivity, its reach falls short of the lesion advance, and the dilated stencil closes the gap. The weak points are a doubled conclusion ("solves connectivity but not reach" appears at l. 496 and again at l. 510) and a short closing paragraph that comes after the forward pointer to Chapter 5. §4.3.4 describes each of its three operators the same way, original first and adaptation second, which helps the reader. But it opens without a bridge from the graph discussion: the §4.3 roadmap (l. 221) says "dense grid operators" and §4.3.1 describes "the operators that work on the image grid", yet the subsection never connects these. It also keeps one detail (18 normalised convolution sites) whose only reference in the rendered text was the graph U-Net paragraph, which is now commented out. §4.3.6 is the heaviest part. It runs from the original FEN through the adaptation, a recap of departures, the RK4 rationale, the two transport forms and a stability definition (which uses "late epochs" before Chapter 5 defines them) to the parameter counts, and several of these facts come back in §4.3.7, §4.3.8 and the Table 4.2 caption. §4.3.7 explains the mechanics of the wrapper before saying why it exists. It also re-explains the solver-swap diagnostic from §4.2.1 without referring back, and ends by previewing Chapter 5 results, which §4.2.1 avoids. §4.3.8 has the material it needs, but the two floor exceptions, the capacity pointer and the FEN controls are spread across paragraph breaks, and parts repeat §4.3.6. The register is mostly plain and correctly impersonal. Where the prose reads as machine-like, the cause is structure, not buzzwords: short negation-first sentences, "X, not Y" closers, colon reveals, a few metaphors and personifications, and therefore/thus chains. Terminology also drifts: "backbone" vs "operator", "graph" vs "eye", and "equal-area lattice" vs "uniform mesh".

### Transitions

- §4.3.3 opening (04-method.tex l. 470): the subsection opens with a verdict ('turns out to be the most consequential design decision') before the reader knows what is being decided. Open with what the graph determines (which nodes exchange messages), then give the grid facts.
- §4.3.3, l. 496 vs l. 510: 'This index-space graph solves the connectivity problem, but ...' and 'The index-space graph thus solves the connectivity problem but not the reach problem.' make the same point two paragraphs apart. The second was added as a bridge at the author's request (review v4 #6), so keep it as the summary. Merge it with the following sentence instead of keeping it as a separate aphoristic line (see finding at l. 507), and reword l. 496 so that it does not pre-empt the summary.
- §4.3.3, l. 524-529: the paragraph saying the stencil changes only the edge set comes after the forward pointer 'Chapter~\ref{ch:experiments} tests this choice ...'. Move it before that sentence so the subsection ends on the pointer to the test.
- §4.3.3 -> §4.3.4 (l. 560-563): there is no bridge from graphs to grid operators. The roadmap (l. 221) calls these 'dense grid operators' and §4.3.1 (l. 250) describes 'the operators that work on the image grid', but §4.3.4 itself never connects the term. Insert one sentence before the U-Net paragraph (see finding at l. 563).
- §4.3.4 U-Net, l. 582-584: the count of '18 normalised convolution sites' was referenced only by the graph U-Net paragraph (now commented out, l. 654-680) and by the \iffalse'd §5.4.4. The reader is not told why the number matters. Cut it, or tie it to something still in the text.
- §4.3.4 FNO, l. 625-631: 'The mode count follows from the geometry' is followed by an argument for equal counts on both axes, not for the value 14 (the framework mirror confirms that the geometry argument concerns equality only). State that it is the equality that follows from the geometry.
- §4.3.5, l. 682: the opener repeats the §4.3 introduction almost verbatim ('Two truncated graph networks test how much spatial context is needed at all', l. 211). Vary it. The subsection also never says why these arms are called 'floors'. A short clause would help: they mark the lower reference for what spatial context contributes.
- §4.3.6, l. 746-754: the departures paragraph largely recaps the two preceding paragraphs (lattice instead of Delaunay, triangle-type indicator, covariates) and reads as a second pass. Either put a short departures list straight after the summary of the original, as the U-Net subsection does ('departs from the original in four ways'), or keep only the items not yet stated: autonomous time derivative, fixed-step integration, the energy-conserving form.
- §4.3.6, l. 794-797: the stability criterion uses 'late epochs', which Chapter 4 never defines; they are defined in §5.1.3 (sec:experiments:protocol:rollout). Add '(epochs 10 to 29; \S\ref{sec:experiments:protocol:rollout})'.
- §4.3.6 l. 756-757 vs §4.3.7 l. 855-858: both places argue that the FEN's spatial reach comes from sub-steps, because one evaluation only couples nodes sharing a triangle. Keep the argument in §4.3.6 and point to it from §4.3.7.
- §4.3.6 l. 805-811, §4.3.8 l. 906-911 and the Table 4.2 caption describe the free-form FEN controls (34 785 parameters, factor 1.97, width 139 matched) three times. 'Adds no parameters' is said of the RK wrapper at l. 818, at l. 910-911 and in the table. State each fact fully once (§4.3.6, §4.3.7) and point to it from §4.3.8.
- §4.3.7 order: the 'Why the wrapper exists' paragraph (l. 854) comes after the Euler/RK4 mechanics and the autonomous-field paragraph. Move it to directly after the opening paragraph (l. 816-818), so the reader knows the three uses before the details.
- §4.3.7 'Jump and continuous time' (l. 863-881) re-explains the solver-swap diagnostic and the Ott et al. caution already given in §4.2.1 (l. 159-171), without referring back. Add a back-reference, e.g. 'the solver-swap diagnostic introduced in~\S\ref{sec:method:dt-residual}', and shorten the re-explanation.
- §4.3.7 ending, l. 876-881: the Method chapter previews the solver-swap outcome and the accuracy null, while §4.2.1 names the same diagnostic without previewing its result. Make the two consistent: either keep only pointers here, or let §4.2.1 carry the same one-line preview.
- §4.3.8, l. 894-904: the two floor exceptions are split across a paragraph break, and the capacity-experiment pointer sits inside the per-pixel-floor paragraph although it is unrelated to it. Merge the two floor exceptions into one sentence and end the subsection on the capacity pointer, placed after the matching rationale.
- Terminology across §4.3.6-4.3.8: 'backbone' (about eight times in §4.3.7) vs 'operator' (the rest of §4.3); 'graph' vs 'eye' for the same batch element (l. 829-834); 'equal-area lattice' vs 'uniform mesh' for the same triangulation (l. 722-724). Use one term for each.

### Recurring tells in this part

- 'X, not Y' / 'rather than' / 'instead of' antitheses used as sentence closers, e.g. 'would be a weaker control, not a stronger one' (l. 591). Others: 'a crop, not a periodic physical domain' (l. 620), 'by construction rather than as a next state' (l. 698), 'content is moved, not created' (l. 773), 'not an architecture arm' twice (l. 896-897, l. 900). About 10 in the range. Keep the ones that carry a real technical contrast (e.g. 'returns a residual rather than class scores', 'sets the reach ... rather than treating it as a free hyperparameter'); drop the rhetorical ones.
- Negation-first or mirrored short declaratives: 'This is a property of the architecture. It is not a claim that ...' (l. 699-700); 'The Runge--Kutta wrapper is not a backbone.' (l. 816); 'The update itself is not zero:' (l. 845); 'It is a control, not an architecture arm:' (l. 900). About 5.
- Colon reveals after a short verdict: 'fails. ... in its own row: measured over the grid' (l. 477-479); 'as pure transport should: content is moved, not created' (l. 773); 'must satisfy exactly this:' (l. 867); 'Its outcome is reported in ...: the canonical model fails it' (l. 876). About 5.
- Narrative 'turns out / turned out', which presents results as discoveries: l. 470 and l. 788.
- Metaphor and personification: 'the two-dimensional retina falls apart into 49 independent one-dimensional strands' (l. 482), 'lopsided' (l. 497), 'the finite-element machinery only makes a difference' (l. 725), 'the 21:1 axis imbalance never reaches the MLPs' (l. 740), 'The operator then no longer knows' (l. 842), 'Its output only states ... the integrator alone decides' (l. 843-844). About 6.
- therefore/thus chains in consecutive sentences, mainly l. 507-523 ('therefore', 'thus', 'This is why', 'thus'). About 10 across the range.
- Emphasis words 'at all', 'even' and emphatic 'exactly': 'needed at all' (l. 682, repeating l. 211), 'no message passing at all' (l. 687), 'even the four columns' (l. 509), 'must satisfy exactly this' (l. 867). About 4. The technical 'exactly' (exact set equality at l. 487, exact reduction at l. 649 and l. 723) is not a tell and should stay.
- Facts repeated across subsections: 'adds no parameters' (l. 529 for the stencil, l. 786 for the skew form, l. 818 and l. 910-911 for the RK wrapper), the FEN control parameter counts (§4.3.6, §4.3.8, Table 4.2 caption), connectivity-vs-reach (l. 496, l. 510), reach from sub-steps (l. 756, l. 857), and the solver-swap test (§4.2.1 and §4.3.7).

## Findings

### 4b.1 [low] §4.3.3 Graph Construction on an Anisotropic Grid

`04-method.tex:470` · GPTZero: human · tone, flow

> The graph on which messages travel turns out to be the most consequential design decision of the graph solver.

**Issue.** 'turns out' is narrative phrasing that presents a Chapter 5 finding as a discovery, and the subsection opens with a verdict before saying what the graph does.

**Suggestion.**

> The graph determines which nodes exchange messages, and its construction proved to be the most consequential design decision of the graph solver.

### 4b.2 [low] §4.3.3 Graph Construction on an Anisotropic Grid

`04-method.tex:477` · GPTZero: AI · ai-tone, clarity

> A $k$-nearest-neighbour graph built on these physical positions fails. The twelve physically nearest neighbours of every node all lie in its own row: measured over the grid, 100\,\% of the edges connect nodes in the same row and none cross rows.

**Issue.** The one-word verdict 'fails' is followed by a colon explanation, a reveal structure. Naming the concrete failure is plainer and more precise.

**Suggestion.**

> A $k$-nearest-neighbour graph built on these physical positions does not connect the rows. The twelve physically nearest neighbours of every node all lie in its own row: measured over the grid, 100\,\% of the edges connect nodes in the same row and none cross rows.

### 4b.3 [medium] §4.3.3 Graph Construction on an Anisotropic Grid

`04-method.tex:481` · GPTZero: AI · tone, ai-tone

> No information can cross from one row to the next at any network depth, and the two-dimensional retina falls apart into 49 independent one-dimensional strands.

**Issue.** 'the retina falls apart into ... strands' is dramatic imagery. The retina does not change; only the graph's connectivity over the grid does.

**Suggestion.**

> No information can cross from one row to the next at any network depth, and the grid decomposes into 49 independent one-dimensional rows.

### 4b.4 [low] §4.3.3 Graph Construction on an Anisotropic Grid

`04-method.tex:486` · GPTZero: AI · clarity

> With $k = 12$, and without self-loops, the neighbourhood of an interior node is exactly the index-space disc of squared radius four, a diamond of radius two.

**Issue.** Two geometric descriptions (a disc and a diamond) follow each other without saying why they are the same set.

**Suggestion.**

> With $k = 12$ and without self-loops, the neighbourhood of an interior node is exactly the index-space disc of squared radius four, which on the integer grid coincides with a diamond of radius two.

### 4b.5 [low] §4.3.3 Graph Construction on an Anisotropic Grid

`04-method.tex:496` · GPTZero: AI · tone, flow

> This index-space graph solves the connectivity problem, but its physical reach is lopsided.

**Issue.** 'lopsided' is colloquial for a method description, and the sentence anticipates the 'connectivity but not reach' summary two paragraphs later.

**Suggestion.**

> This index-space graph restores two-dimensional connectivity, but its physical reach differs strongly between the two axes.

### 4b.6 [low] §4.3.3 Graph Construction on an Anisotropic Grid

`04-method.tex:504` · GPTZero: AI · flow, ai-tone

> This reach can be compared with the scale on which the lesion changes. Between two visits 180 days apart, the GA front advances a median of about 12 columns, or roughly 0.07\,mm.

**Issue.** An announcement sentence says that a comparison is coming instead of making it, a paragraph-opening signpost.

**Suggestion.**

> For comparison, the GA front advances a median of about 12 columns, or roughly 0.07\,mm, between two visits 180 days apart.

### 4b.7 [medium] §4.3.3 Graph Construction on an Anisotropic Grid

`04-method.tex:507` · GPTZero: AI · flow, ai-tone

> A single hop along a row therefore covers only a small fraction of the distance the front typically moves between two visits, and even the four columns reached after two rounds are about a third of the median advance. The index-space graph thus solves the connectivity problem but not the reach problem. This is why a second graph construction was needed, one whose reach along a row matches the scale of the lesion change.

**Issue.** The middle sentence stands alone as an aphoristic closer that repeats l. 496. The cleft 'This is why ...' and the therefore/thus chain make the rhythm machine-like, and 'even' is emphasis only.

**Suggestion.**

> A single hop along a row therefore covers only a small fraction of the distance the front typically moves between two visits, and the four columns reached after two rounds are about a third of the median advance. The index-space graph thus restores connectivity but not reach, which motivates a second graph construction whose reach along a row matches the scale of the lesion change.

### 4b.8 [medium] §4.3.3 Graph Construction on an Anisotropic Grid

`04-method.tex:527` · GPTZero: AI · clarity, flow

> The dilated stencil replaces only the edge set. The network, its weights and every other component stay unchanged, and the stencil adds no parameters.

**Issue.** 'its weights ... stay unchanged' can be read as reusing trained weights, when the point is that the architecture and the parameter count are the same; the stencil model is trained separately. The paragraph also comes after the forward pointer to Chapter 5, so the subsection ends on an afterthought.

**Suggestion.**

> Move this before 'Chapter~\ref{ch:experiments} tests this choice ...' and write: The dilated stencil changes only the edge set; the network architecture and every other component are the same as on the index-space graph, and the stencil adds no parameters.

### 4b.9 [medium] Figure 4.2 caption

`04-method.tex:550` · GPTZero: AI · clarity

> Filled markers are reached in one message-passing round, open markers in two, the number of rounds of the canonical configuration: about $\pm 4$ columns ($\pm 0.023$\,mm) along a row with the $k$-NN graph, against $\pm 42$ columns ($\pm 0.24$\,mm) with the dilated stencil.

**Issue.** The appositive 'the number of rounds of the canonical configuration' is followed by a colon and two reach values, so it is not clear at first that the values describe the two-round reach.

**Suggestion.**

> Filled markers are reached in one message-passing round and open markers in two, the number of rounds used by the canonical configuration. After two rounds, a node reaches about $\pm 4$ columns ($\pm 0.023$\,mm) along a row with the $k$-NN graph and $\pm 42$ columns ($\pm 0.24$\,mm) with the dilated stencil.

### 4b.10 [medium] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid

`04-method.tex:563` · GPTZero: human · flow

> The first dense operator is a U-Net \citep{Ronneberger2015}.

**Issue.** The subsection moves from graphs to grid operators without a bridge, and it does not connect 'dense' to the roadmap's 'dense grid operators' or to the grid-operator inputs of §4.3.1.

**Suggestion.**

> Insert before this sentence: The three operators of this subsection are dense grid operators: they act on the state as an image on the full $49 \times 1024$ grid and receive the sixteen input channels of~\S\ref{sec:method:family:contract}.

### 4b.11 [low] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid

`04-method.tex:582` · GPTZero: AI · ai-tone, flow

> With nine such blocks --- an input stage, four downsampling and four upsampling stages --- the network has 18 normalised convolution sites.

**Issue.** An em-dash aside sits in the middle of the sentence. The count of normalised sites served only the graph U-Net comparison (now commented out) and the \iffalse'd §5.4.4, so the reader is not told why it matters.

**Suggestion.**

> The network has nine such blocks (an input stage, four downsampling and four upsampling stages) and therefore 18 normalised convolutions. If the number serves no later comparison, consider cutting the sentence.

### 4b.12 [medium] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid

`04-method.tex:587` · GPTZero: AI · clarity

> Rows are pooled four times and columns sixteen times, which reduces the 21:1 aspect of the grid to about 5:1 without removing it.

**Issue.** 'pooled four times' reads as four pooling operations, but rows are pooled twice, by a total factor of four (columns, in turn, are pooled four times). 'aspect of the grid' is vague for the ratio of row to column spacing.

**Suggestion.**

> Rows are downsampled by a factor of four in total and columns by a factor of sixteen, which reduces the 21:1 ratio of row to column spacing to about 5:1 without removing it.

### 4b.13 [low] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid

`04-method.tex:589` · GPTZero: AI · ai-tone

> The schedule was deliberately not tuned further, because a comparison model whose geometry has been optimised against this dataset would be a weaker control, not a stronger one.

**Issue.** The 'a weaker control, not a stronger one' antithesis is a rhetorical closer; 'weaker control' alone carries the point.

**Suggestion.**

> The schedule was deliberately not tuned further: a comparison model whose geometry had been optimised on this dataset would make a weaker control.

### 4b.14 [low] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid

`04-method.tex:595` · GPTZero: AI · clarity

> A base width of five gives 83\,081 parameters.

**Issue.** 'base width' is used without explanation; readers outside the U-Net literature may not know it is the channel count of the first stage.

**Suggestion.**

> A base width of five, that is, five channels at the input stage, gives 83\,081 parameters.

### 4b.15 [low] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid

`04-method.tex:620` · GPTZero: AI · tone, ai-tone

> The domain here is a crop, not a periodic physical domain (\S\ref{sec:data:spatial}). This thesis therefore zero-pads the field by about one eighth per axis before the transform, from $49 \times 1024$ to $56 \times 1152$, and crops it back after the spectral blocks; the original relies on the local linear term instead and does not pad.

**Issue.** There is an 'X, not Y' opener, and 'This thesis' acts as an agent, which breaks the passive house style used elsewhere.

**Suggestion.**

> Because the domain here is a crop and not a periodic physical domain (\S\ref{sec:data:spatial}), the field is zero-padded by about one eighth per axis before the transform, from $49 \times 1024$ to $56 \times 1152$, and cropped back after the spectral blocks; the original does not pad and relies on the local linear term instead.

### 4b.16 [medium] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid

`04-method.tex:625` · GPTZero: AI · clarity, ai-tone

> The mode count follows from the geometry. The physical domain is nearly square ($5.94 \times 5.82$\,mm), so equal mode counts give nearly equal physical bandwidth on both axes --- the property the index-space graph of~\S\ref{sec:method:graph} lacks.

**Issue.** The first sentence promises a reason for the mode count, but the explanation only justifies equal counts on both axes, not the value 14. The em-dash callback is a contrast tell.

**Suggestion.**

> The equal mode count on both axes follows from the geometry: the physical domain is nearly square ($5.94 \times 5.82$\,mm), so equal mode counts give nearly equal physical bandwidth on both axes, a property the index-space graph of~\S\ref{sec:method:graph} does not have.

### 4b.17 [low] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid

`04-method.tex:643` · GPTZero: AI · ai-tone

> Unlike the original, it operates at a single training resolution, without mean subtraction, without rescaling and without discrete-continuous convolutions; it is therefore not the resolution-consistent operator of that paper.

**Issue.** The 'without ..., without ... and without ...' triad is a symmetric list that reads as mechanical.

**Suggestion.**

> Unlike the original, it operates at a single training resolution and uses no mean subtraction, rescaling or discrete-continuous convolutions, so it is not the resolution-consistent operator of that paper.

### 4b.18 [medium] §4.3.5 The Locality Floors

`04-method.tex:682` · GPTZero: AI · ai-tone, flow

> Two arms test how much spatial context is needed at all.

**Issue.** 'at all' is emphasis filler, and the sentence repeats the §4.3 introduction (l. 211, 'Two truncated graph networks test how much spatial context is needed at all') almost word for word.

**Suggestion.**

> Two arms test how much spatial context the prediction needs.

### 4b.19 [low] §4.3.5 The Locality Floors

`04-method.tex:687` · GPTZero: AI · clarity, ai-tone

> The per-pixel floor uses no message passing at all. Each node's next state then depends only on its own state and its conditioning inputs, and the model has no spatial context; it has 14\,795 parameters.

**Issue.** 'at all' is emphasis again, and three short clauses state the same consequence one after another.

**Suggestion.**

> The per-pixel floor uses no message passing, so each node's next state depends only on its own state and its conditioning inputs and the model has no spatial context; it has 14\,795 parameters.

### 4b.20 [medium] §4.3.6 The Finite Element Network

`04-method.tex:697` · GPTZero: AI · ai-tone, clarity

> It is the only operator whose output is defined as a time derivative by construction rather than as a next state. This is a property of the architecture. It is not a claim that the trained model behaves as a valid continuous-time system, which is tested in Chapter~\ref{ch:experiments}.

**Issue.** The mirrored short pair 'This is X. It is not Y.' and 'by construction rather than' are typical tells, and 'which is tested' grammatically attaches to 'a claim'.

**Suggestion.**

> Its architecture defines the output as a time derivative and not as a next state; it is the only operator in the survey that does so. Whether the trained model behaves as a valid continuous-time system is a separate question, tested in Chapter~\ref{ch:experiments}.

### 4b.21 [low] §4.3.6 The Finite Element Network

`04-method.tex:708` · GPTZero: AI · clarity

> The inner products are factored so that a network, the free-form term, predicts one coefficient per cell, vertex and feature from the time, the cell centre, the local vertex coordinates and the vertex features.

**Issue.** The appositive 'a network, the free-form term,' equates a network with a term in the middle of a long noun stack, so the sentence has to be read twice.

**Suggestion.**

> The inner products are factored so that a network predicts one coefficient per cell, vertex and feature from the time, the cell centre, the local vertex coordinates and the vertex features; this network is the free-form term.

### 4b.22 [low] §4.3.6 The Finite Element Network

`04-method.tex:716` · GPTZero: AI · clarity

> Both networks are tanh MLPs, and the resulting ODE is solved with the adaptive dopri5 solver.

**Issue.** 'dopri5' is a software name that is not explained at first use.

**Suggestion.**

> Both networks are tanh MLPs, and the resulting ODE is solved with the adaptive Dormand--Prince solver (dopri5).

### 4b.23 [medium] §4.3.6 The Finite Element Network

`04-method.tex:722` · GPTZero: AI · tone, clarity

> On this equal-area lattice the lumped assembly is exactly a mean over the triangles adjacent to a node. On a uniform mesh, the FEN is therefore a message-passing network over triangle hyperedges with mean aggregation, and the finite-element machinery only makes a difference at the boundary.

**Issue.** 'equal-area lattice' and 'uniform mesh' name the same object in consecutive sentences, 'machinery ... makes a difference' is informal, and 'hyperedges' is not explained.

**Suggestion.**

> On this equal-area lattice, the lumped assembly is exactly a mean over the triangles adjacent to a node. The FEN is therefore a message-passing network with mean aggregation over triangles, each linking three nodes, and its finite-element formulation differs from such a network only at the boundary.

### 4b.24 [low] §4.3.6 The Finite Element Network

`04-method.tex:736` · GPTZero: AI · flow, clarity

> Neither the original nor this implementation makes the velocity divergence-free across triangles, so reading it as a physical advection speed rests on an assumption the model does not enforce globally.

**Issue.** This repeats the statement about the original from two paragraphs earlier (l. 715-716), and the 'Neither ... nor ..., so reading it ... rests on' construction is heavy.

**Suggestion.**

> As in the original, the velocity is not divergence-free across triangles, so reading it as a physical advection speed rests on an assumption that the model does not enforce globally.

### 4b.25 [**HIGH**] §4.3.6 The Finite Element Network

`04-method.tex:741` · GPTZero: AI · clarity

> The transport term runs on its own coarser mesh, built on every seventh column (97\,632 triangles), while the free-form term uses the full-resolution mesh.

**Issue.** 'built on every seventh column' makes the reader picture a subsampled mesh over one seventh of the nodes. In fact the mesh consists of seven interleaved triangulations that together use every node, which is why it has almost as many triangles as the full mesh. As written, the mesh structure is likely to be misread.

**Suggestion.**

> The transport term runs on its own coarser mesh, made of seven interleaved triangulations that each use every seventh column (97\,632 triangles in total), while the free-form term uses the full-resolution mesh.

### 4b.26 [low] §4.3.6 The Finite Element Network

`04-method.tex:749` · GPTZero: AI · clarity, tone

> The time is not an input, so the learned dynamics are autonomous, a variant the original paper explicitly allows.

**Issue.** 'autonomous' is not defined at first use, and 'learned dynamics' is wording the project otherwise avoids.

**Suggestion.**

> The time is not an input, so the learned time derivative has no explicit dependence on time (it is autonomous), a variant the original paper explicitly allows.

### 4b.27 [low] §4.3.6 The Finite Element Network, paragraph 'Two forms of the transport operator'

`04-method.tex:768` · GPTZero: human · flow

> \paragraph{Two forms of the transport operator.} Two forms of the assembled transport operator were trained. The first is the Galerkin form described above, as in the original.

**Issue.** The first sentence repeats the run-in paragraph heading almost word for word.

**Suggestion.**

> \paragraph{Two forms of the transport operator.} Both forms were trained. The first is the Galerkin form described above, as in the original.

### 4b.28 [medium] §4.3.6 The Finite Element Network, paragraph 'Two forms of the transport operator'

`04-method.tex:770` · GPTZero: AI · ai-tone

> At a constant velocity and away from the edge of the domain, it conserves a discrete energy of the state, the mass-weighted sum of squares $u^\top M u$, as pure transport should: content is moved, not created.

**Issue.** 'as pure transport should: content is moved, not created' combines a colon reveal with an aphoristic 'X, not Y' antithesis.

**Suggestion.**

> At a constant velocity and away from the edge of the domain, it conserves a discrete energy of the state, the mass-weighted sum of squares $u^\top M u$, as expected of pure transport, which moves content without creating it.

### 4b.29 [medium] §4.3.6 The Finite Element Network, paragraph 'Two forms of the transport operator'

`04-method.tex:773` · GPTZero: AI · clarity

> At the edge of the crop, and for a velocity that varies from triangle to triangle, it does not. No flux term is assembled at the boundary, so transported content accumulates there, and the operator has modes that grow instead of travelling.

**Issue.** 'and' reads as if both conditions must hold together, but the previous sentence makes conservation require both a constant velocity and the interior, so either violation breaks it. The elliptical 'it does not' adds to the ambiguity.

**Suggestion.**

> At the edge of the crop, or where the velocity varies from triangle to triangle, it does not conserve this energy. No flux term is assembled at the boundary, so transported content accumulates there, and the operator has modes that grow instead of travelling.

### 4b.30 [low] §4.3.6 The Finite Element Network, paragraph 'Two forms of the transport operator'

`04-method.tex:777` · GPTZero: human · clarity

> It keeps only the energy-conserving part of the Galerkin operator $L$,

**Issue.** The equation introduces $L_{\text{skew}}$, but the text never says what 'skew' refers to, so the subscript appears unexplained.

**Suggestion.**

> It keeps only the part of the Galerkin operator $L$ that is skew-adjoint with respect to the mass matrix $M$, which is its energy-conserving part,

### 4b.31 [medium] §4.3.6 The Finite Element Network

`04-method.tex:788` · GPTZero: AI · ai-tone, flow

> The Galerkin form turned out to be unstable, and the T-FEN reported in Chapter~\ref{ch:experiments} uses the energy-conserving form; the Galerkin runs are reported in~\S\ref{sec:experiments:validity:tfen}. \emph{Unstable} has a specific meaning here.

**Issue.** 'turned out' is narrative phrasing, and 'Unstable has a specific meaning here.' is a signpost sentence that delays the definition.

**Suggestion.**

> The Galerkin form proved unstable in the sense defined below, so the T-FEN reported in Chapter~\ref{ch:experiments} uses the energy-conserving form; the Galerkin runs are reported in~\S\ref{sec:experiments:validity:tfen}. (Then begin the next sentence: Stability is judged during evaluation, where every model is run freely: it predicts ...)

### 4b.32 [medium] §4.3.6 The Finite Element Network

`04-method.tex:794` · GPTZero: AI · clarity, flow

> A run is called stable if, in this free-running rollout, the root mean squared error of the mask channel and of the layer channels, both in normalised units, stays at or below 5 on at least 19 of its 20 late epochs.

**Issue.** 'late epochs' is used here for the first time in the thesis and is defined only in §5.1.3, so the criterion cannot be followed at this point.

**Suggestion.**

> A run is called stable if, in this free-running rollout, the root mean squared error of the mask channel and of the layer channels, both in normalised units, stays at or below 5 on at least 19 of its 20 late epochs (epochs 10 to 29; \S\ref{sec:experiments:protocol:rollout}).

### 4b.33 [medium] §4.3.7 Fixed-Step Runge–Kutta Integration

`04-method.tex:816` · GPTZero: AI · ai-tone

> The Runge--Kutta wrapper is not a backbone. It is placed around any backbone and changes only how the backbone's output is turned into the next state. It adds no parameters.

**Issue.** The subsection opens with a negation followed by three uniformly short declaratives, a robotic rhythm.

**Suggestion.**

> The Runge--Kutta wrapper is placed around any backbone and changes only how the backbone's output is turned into the next state; it is not itself a backbone and adds no parameters.

### 4b.34 [medium] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Euler and RK4'

`04-method.tex:825` · GPTZero: human · clarity

> The classical fourth-order scheme (RK4), used in every reported run, evaluates it four times per step and takes a weighted average \citep{Butcher1987, Hairer1993}.

**Issue.** 'used in every reported run' literally says that every run in the thesis uses RK4, right after the statement that the canonical update is one Euler step. The intended scope is every reported model trained with the wrapper. The pronoun 'it' is also distant from 'the operator'.

**Suggestion.**

> The classical fourth-order scheme (RK4) evaluates the operator four times per step and takes a weighted average \citep{Butcher1987, Hairer1993}; every reported model trained with the wrapper uses it.

### 4b.35 [low] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Euler and RK4'

`04-method.tex:829` · GPTZero: human · clarity

> The sub-step length is set per graph, either as $h = \Delta t / n$ or from a physical step length in days, with the number of sub-steps rounded up from the ratio of the interval to that length. An eye is therefore integrated with the same steps whether it is batched with others or evaluated alone; graphs with shorter intervals take zero-length steps until the longest interval in the batch is complete.

**Issue.** The text switches between 'graph' and 'eye' for the same batch element, and 'graph' is odd for the dense operators the wrapper also serves.

**Suggestion.**

> The sub-step length is set separately for each eye in a batch, either as $h = \Delta t / n$ or from a physical step length in days, with the number of sub-steps rounded up from the ratio of the interval to that length. An eye is therefore integrated with the same steps whether it is batched with others or evaluated alone; eyes with shorter intervals take zero-length steps until the longest interval in the batch is complete.

### 4b.36 [low] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Euler and RK4'

`04-method.tex:835` · GPTZero: AI · clarity

> As a unit check, the observed convergence orders on the test problem $\mathrm{d}u / \mathrm{d}t = -\lambda u$ are 0.99, 2.04, 2.04 and 4.35 for the Euler, midpoint, Heun and RK4 schemes, close to their nominal orders of one, two, two and four.

**Issue.** 'unit check' is ambiguous: it can mean a check of physical units or a unit test.

**Suggestion.**

> As a check of the implementation, the observed convergence orders on the test problem $\mathrm{d}u / \mathrm{d}t = -\lambda u$ are 0.99, 2.04, 2.04 and 4.35 for the Euler, midpoint, Heun and RK4 schemes, close to their nominal orders of one, two, two and four.

### 4b.37 [medium] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'The autonomous field'

`04-method.tex:841` · GPTZero: AI · ai-tone, clarity

> Inside the wrapper, the $\Delta t$ entry of the operator's conditioning vector is set to zero. The operator then no longer knows how long the interval is. Its output only states how fast the state is changing at the current moment, and the integrator alone decides how long this rate is applied. The update itself is not zero: the state still changes by the integrated rate.

**Issue.** The passage personifies the operator and the integrator ('no longer knows', 'states', 'decides') and pre-empts a misreading with a colon sentence. The heading term 'autonomous' is not defined in the paragraph.

**Suggestion.**

> Inside the wrapper, the $\Delta t$ entry of the operator's conditioning vector is set to zero, so the operator receives no information about the length of the interval. Its output is then a rate of change at the current state with no explicit dependence on time, an \emph{autonomous} field, and the integrator alone determines over which interval this rate is applied. Zeroing the $\Delta t$ entry does not zero the update: the state still changes by the integrated rate.

### 4b.38 [medium] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'The autonomous field'

`04-method.tex:848` · GPTZero: human · clarity, flow *(added in verification)*

> The wrapper requires the $\Delta t$-multiplied residual form of Equation~\eqref{eq:method:residual-update}.

**Issue.** The requirement is stated without its reason, so the link to the preceding explanation of the rate is left to the reader.

**Suggestion.**

> The wrapper requires the $\Delta t$-multiplied residual form of Equation~\eqref{eq:method:residual-update}, because without the multiplication by $\Delta t$ the operator's output is not a rate and cannot be integrated.

### 4b.39 [medium] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Why the wrapper exists'

`04-method.tex:854` · GPTZero: AI · clarity, flow

> \paragraph{Why the wrapper exists.} It has three uses. First, the finite-element network outputs a rate and needs an integrator (\S\ref{sec:method:family:fen}); since one evaluation couples only nodes that share a triangle, its spatial reach grows with the number of evaluations. Second, it allows the integration order to be tested on its own: the same backbone trained with one Euler step and with RK4 (\S\ref{sec:experiments:ablations:time}). Third, it allows the question of whether a model describes a continuous process to be tested.

**Issue.** 'It' has no antecedent after the heading, the reach clause repeats §4.3.6 (l. 756-757), and the last sentence buries its verb behind a long clausal subject. The paragraph would also work better directly after the subsection's opening paragraph.

**Suggestion.**

> \paragraph{Uses of the wrapper.} The wrapper has three uses. First, the finite-element network outputs a rate and needs an integrator (\S\ref{sec:method:family:fen}). Second, it allows the integration order to be tested on its own: the same backbone trained with one Euler step and with RK4 (\S\ref{sec:experiments:ablations:time}). Third, it allows a test of whether a model describes a continuous process. (Consider moving this paragraph to directly after l. 818.)

### 4b.40 [medium] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Jump and continuous time'

`04-method.tex:865` · GPTZero: AI · ai-tone, tone

> Nothing requires that two jumps of length $\Delta t / 2$ lead to the same state as one jump of length $\Delta t$. A continuous-time model must satisfy exactly this: splitting the interval into more or finer steps must not change the answer.

**Issue.** The rhetorical opener 'Nothing requires', the colon reveal 'must satisfy exactly this:' and the colloquial 'the answer' together read as staged.

**Suggestion.**

> Training does not require two jumps of length $\Delta t / 2$ to lead to the same state as one jump of length $\Delta t$. In a continuous-time model, by contrast, splitting the interval into more or finer steps must not change the prediction.

### 4b.41 [low] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Jump and continuous time'

`04-method.tex:869` · GPTZero: AI · clarity *(added in verification)*

> \citet{Ott2021} show that a model trained with an overly coarse step can reach high accuracy and still lose this property, and they test it by evaluating the trained model with solvers of equal or smaller discretisation error and checking whether its predictions stay the same.

**Issue.** A 45-word sentence joins a finding and a test procedure with ', and they', which makes it hard to read in one pass.

**Suggestion.**

> \citet{Ott2021} show that a model trained with an overly coarse step can reach high accuracy and still lose this property. They test it by evaluating the trained model with solvers of equal or smaller discretisation error and checking whether its predictions stay the same.

### 4b.42 [low] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Jump and continuous time'

`04-method.tex:874` · GPTZero: AI · clarity

> Because any trained backbone can be integrated with different schemes and step counts after training, the wrapper makes this solver-swap test possible.

**Issue.** 'trained ... after training' is redundant, and the wrapper, the actual agent, appears only at the end.

**Suggestion.**

> Because the wrapper can integrate any trained backbone with other schemes and step counts, it makes this solver-swap test possible.

### 4b.43 [low] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Jump and continuous time'

`04-method.tex:876` · GPTZero: AI · flow, ai-tone

> Its outcome is reported in~\S\ref{sec:experiments:validity:swap}: the canonical model fails it, whereas the same network trained under the RK4 wrapper passes it, as does the finite-element network. A continuous-time model can therefore be obtained by training with the integrator, but in this survey it is not more accurate than the single jump (\S\ref{sec:experiments:ablations:time}).

**Issue.** The Method chapter previews Chapter 5 results and closes on a verdict, while §4.2.1 names the same diagnostic without previewing its outcome. The colon reveal and the 'therefore ..., but ...' closer add to the machine-like tone.

**Suggestion.**

> Its outcome is reported in~\S\ref{sec:experiments:validity:swap}, and the accuracy of the models trained with the integrator in~\S\ref{sec:experiments:ablations:time}. (If the preview is kept on purpose, align §4.2.1 with it.)

### 4b.44 [medium] §4.3.8 Parameter Matching

`04-method.tex:889` · GPTZero: AI · clarity

> Every operator is matched in size to the canonical graph solver of~\S\ref{sec:method:graph}, which has 67\,147 parameters. The widths are chosen so that each arm comes as close to this count as its width granularity allows, so that differences between arms cannot be attributed to extra parameters.

**Issue.** 'Every operator' is contradicted a few sentences later by the floors, which are not matched, and the doubled 'so that ... so that' makes the second sentence clumsy.

**Suggestion.**

> Every architecture arm is matched in size to the canonical graph solver of~\S\ref{sec:method:graph}, which has 67\,147 parameters: its width is chosen to come as close to this count as the width granularity allows, so that differences between arms cannot be attributed to extra parameters.

### 4b.45 [medium] §4.3.8 Parameter Matching

`04-method.tex:894` · GPTZero: AI · ai-tone, flow

> All architecture arms lie within a factor of 1.25 of the reference. The one-hop floor lies below this band because it is a rung of the locality ladder of~\S\ref{sec:method:family:floors}, not an architecture arm. The per-pixel floor also lies outside the band, with about a fifth of the parameters. It is a control, not an architecture arm: it marks what a model without spatial context can do.

**Issue.** '..., not an architecture arm' appears twice in a mirrored pair, the second time with a colon reveal, and the two parallel exceptions are split across a paragraph break.

**Suggestion.**

> All architecture arms lie within a factor of 1.25 of the reference. The two floors lie below this band because they are not architecture arms: the one-hop floor is a rung of the locality ladder of~\S\ref{sec:method:family:floors}, and the per-pixel floor, with about a fifth of the parameters, is a control that marks what a model without spatial context can do.

### 4b.46 [low] §4.3.8 Parameter Matching

`04-method.tex:901` · GPTZero: AI · flow, clarity

> Whether the size at which the arms are matched affects the comparison is tested separately, by scaling every architecture class from about a quarter to about four times its size (\S\ref{sec:experiments:ablations:capacity}).

**Issue.** The sentence has a long clausal subject before its verb, and it sits in the per-pixel-floor paragraph, which it is unrelated to.

**Suggestion.**

> Move it to the end of the first paragraph (after the matching rationale) and write: A separate experiment tests whether the size at which the arms are matched affects the comparison, by scaling every architecture class from about a quarter to about four times its size (\S\ref{sec:experiments:ablations:capacity}).

### 4b.47 [low] §4.3.8 Parameter Matching

`04-method.tex:906` · GPTZero: AI · flow

> The free-form FEN control at width 96 has 34\,785 parameters, half the reference and a factor of 1.97 below the T-FEN it controls, because it is the T-FEN with the transport head removed (\S\ref{sec:method:family:fen}). A second free-form control at width 139 has 68\,282 parameters and is matched to the T-FEN. The Runge--Kutta wrapper adds no parameters to any backbone.

**Issue.** This nearly repeats §4.3.6 (l. 805-811), and the RK sentence repeats l. 818 and the table row. With the Table 4.2 caption, the same facts appear three times.

**Suggestion.**

> Of the two free-form FEN controls of~\S\ref{sec:method:family:fen}, the one at width 96 has 34\,785 parameters, half the reference and a factor of 1.97 below the T-FEN, and the one at width 139 (68\,282 parameters) is matched to the T-FEN. (Drop the Runge--Kutta sentence; it is stated in~\S\ref{sec:method:family:rk} and in the table.)

### 4b.48 [medium] Table 4.2 caption

`04-method.tex:919` · GPTZero: AI · clarity

> Three arms lie outside this band: the per-pixel floor, a control without spatial context; the one-hop floor, a rung of the locality ladder and a truncation of the index-space arm; and the free-form FEN at width 96, which is not matched to the T-FEN it is compared with (factor 1.97); the width-139 control is.

**Issue.** The semicolon list ends in the elliptical 'the width-139 control is.', which is hard to parse after three appositive items.

**Suggestion.**

> Three arms lie outside this band: the per-pixel floor, a control without spatial context; the one-hop floor, a rung of the locality ladder and a truncation of the index-space arm; and the free-form FEN at width 96, which is smaller than the T-FEN it is compared with by a factor of 1.97. The free-form FEN at width 139 is matched to the T-FEN.

