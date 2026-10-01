# Micro feedback 5b: Ch. 5 Experiments, §5.3 Ingredient Study

[← Overview](00-overview.md)

34 findings: 0 high, 15 medium, 19 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

§5.3 has a clear plan: one ingredient per subsection, then a synthesis. Most subsections run in the same order (numbers, verdict, interpretation), so the logic is easy to check. Three structural points weaken the flow. First, the section opener gives no roadmap, and it repeats the closing figure of §5.2 ("within about 0.04"). Second, §5.3.3 (global and local context) sits between reach (§5.3.2) and transport (§5.3.4), so it interrupts the reach-to-transport line that §5.3.5 then joins. It is also the one subsection that ends without an established ingredient, and the reader learns this only in its last sentence. Third, the headline ("not the class but the ingredients") appears at the end of §5.2, before any evidence, and again at the end of §5.3.5. The convergence point is stated three times: in §5.2, in the closer of §5.3.4 and in §5.3.5. Inside the paragraphs, the template "X against Y gives Δ = … SE (k/5) and per eye …" recurs about a dozen times, with the verdict at the end, so the reader has to parse two instruments before learning the result. Some per-eye values have no verdict (§5.3.1). Another per-eye value "graduates on that instrument", although §5.1.4 uses "graduates" only for agreement of both instruments and gives no per-eye criterion. The register is mostly plain and objective. The exceptions are a few colloquial verbs ("buys", "carries all of it", "end up", "costs the most") and rhetorical paragraph closers (em-dash asides, "X, not Y" antitheses, pseudo-clefts). These closers cluster at paragraph ends and in §5.3.5 and carry most of the machine-like tone.

### Transitions

- §5.2 → §5.3 (05-experiments.tex l.389-390 and l.463): §5.3 opens by repeating 'within about 0.04 of each other' from the last §5.2 paragraph. §5.2 also already states the conclusion ('What separates the arms is therefore not their class but the ingredients they carry') before any ingredient has been measured, and l.776 repeats it in the same rhetorical form. Keep the full statement in one place only. Either reduce the §5.2 sentence to a forward pointer ('Which ingredients separate the arms is examined in~\S\ref{sec:experiments:ingredients}.') or shorten the §5.3.5 closer. The §5.2 wording was a deliberate scoping decision (a), so the choice of place is the author's.
- §5.3 intro (l.463-468): there is no roadmap. The reader does not know that four ingredients follow, that one of them ends as 'not established', or that §5.3.5 joins two of them. Add one sentence that names the subsections (see the finding at l.463).
- §5.3.1 → §5.3.2 (l.490-491): the bridge 'This motivates the next comparison, which changes where the neighbours lie' works and should stay.
- §5.3.2, l.589: 'This also explains an earlier result' points back two paragraphs, to the reach result, while the paragraph just before it is about k = 20. Name the antecedent ('The reach result also explains …'). Also move the seed-42 fold-3 remark (l.594) so that it directly follows the seed-42 values.
- §5.3.2 → §5.3.3 → §5.3.4: §5.3.5 joins reach (§5.3.2) and transport (§5.3.4), but the not-established global/local subsection sits between them. Consider moving §5.3.3 to after §5.3.4, so that it directly precedes §5.3.5, which mentions it as 'a third candidate'. If the order stays, open §5.3.4 with a sentence that returns to the reach deficit, e.g. 'The next comparison addresses the short reach of~\S\ref{sec:experiments:ingredients:reach} with a different construction.'
- §5.3.3 opening (l.604-606): the subsection goes straight from the two operators into five pairwise comparisons at two seeds, without saying which comparison answers which question. Add a mapping sentence (see the finding at l.604).
- §5.3.4, l.714-720: this paragraph compares the T-FEN and dilated-stencil horizon profiles. It is about the two routes, not about the transport term alone, and it repeats the first-year pair 0.519/0.503 from l.704. It would read more naturally in §5.3.5, after the sentence on their 0.017 difference. Its last sentence (velocity field not interpreted, stability in §5.5.2) is unrelated to the horizon comparison; it could close the first §5.3.4 paragraph instead. If the paragraph stays, drop the repeated first-year values.
- §5.3.4 → §5.3.5 (l.706): the closer 'The two constructions close the same near-term gap.' anticipates the point of §5.3.5 and restates the preceding sentence. Cut it and let §5.3.5 draw the conclusion.
- §5.3.5, l.757-763: the first paragraph describes the short reach but does not call it a deficit; the next paragraph opens with 'correct this deficit'. The subsection heading ('Two Routes to One Deficit') bridges the two, so this is optional. If wanted, end l.760 with '…; this is the deficit addressed below.'
- Per-eye verdicts across §5.3 (l.478, l.633): per-eye results carry a t value but are judged inconsistently. In §5.3.1 the reader gets no verdict for t = -2.4. At l.633 a per-eye result 'graduates on that instrument', although §5.1.4 reserves 'graduates' for agreement of both instruments and states no per-eye criterion. Either state the per-eye criterion once in §5.1.4 or say in words, each time, whether the per-eye difference counts as an effect.
- §5.3.5 → §5.4 (l.780-781): the hand-off '\S\ref{sec:experiments:ablations} reports what was measured and did not matter' is informal and starts the sentence with a section symbol. Rephrase it (see the finding at l.777).

### Recurring tells in this part

- Formulaic comparison template 'X against Y gives $\Delta = … \pm …$~SE (k/5) and per eye … (m/75, t = …)', with the verdict last: about a dozen times in §5.3 (e.g. l.478, 501, 608, 613, 628, 635, 684, 688). The verdict is left to the end, often in a separate clause. Where the comparison carries a claim, state the verdict first in some places.
- Paragraph closers that restate the paragraph, often with 'therefore'/'thus' (9 'therefore', 1 'thus' in the range), e.g. 'A single ring of neighbours therefore buys almost everything …' (l.485, restating l.483), 'The transport effect is therefore not a matter of parameter count.' (l.691) and 'The two constructions close the same near-term gap.' (l.706). About 6 cases. Cut the closer where the preceding sentence already makes the point.
- Antithesis 'X, not Y' / 'rather than' / '… is not what …; … are' as a punchline: 'What matters is where the neighbours are placed, not how many there are.' (l.586), plus l.597-599, l.771-774 (two 'rather than' in two sentences) and l.776-777. About 4-5 cases, all at paragraph ends.
- Pseudo-cleft and subject-clause openers: 'That the FNO lies below the U-Net … is established' (l.614), 'What holds at both seeds is therefore that …' (l.648), 'That a minimal local path closes this gap rests on …' (l.649), 'Where the transport term acts can be seen in the first year' (l.699), 'is not what separates' (l.776), 'One possible reason … is where its extra reach lies' (l.487). About 6 cases.
- Colon reveals: 'Fold 4 carries all of it:' (l.610), '…: a tie.' (l.636), 'The local path no longer helps:' (l.640), 'The first is physical reach:' / 'The second is an explicit transport term:' (l.763-765). About 5 cases.
- Colloquial or economic verbs: 'buys almost everything' (l.485), 'buys nothing' (l.580), 'costs the most of all geometries' (l.522, which can also be misread as compute cost), 'carries all of it' (l.610), 'end up' (l.768). About 5 cases. Replace them with neutral verbs (accounts for, does not raise, lowers the score, comes from, lie).
- Em-dash asides in the most-quoted conclusions: 'located in its graph --- in where its neighbours lie physically --- and not in its operator class' (l.598) and 'this coincidence --- two independent routes to the same deficit ---' (l.772). Two pairs in the range.
- Mirror-symmetric enumerations: 'With zero rounds … With one round … With two rounds …' (l.475-478) and 'The first is … The second is …' (l.763-765). 2 cases.
- Parallel number triplets that the reader must pair up: 'the FNO reads 0.546, 0.583 and 0.594 …, and the U-Net 0.563, 0.581 and 0.555' (l.616-618) and the T-FEN/stencil triplets (l.716-717). Give the values in pairs, bin by bin.
- Overloaded 'gap' for three different things: a score difference (l.650), a parameter difference (l.678) and a near-term growth difference (l.706).

## Findings

### 5b.1 [medium] §5.3 The Ingredient Study (intro)

`05-experiments.tex:463` · GPTZero: AI · flow, clarity, tone

> The strongest arms of different classes lie within about 0.04 of each other, so comparing whole architectures says little about what makes an operator work. This section therefore compares operators that differ in one property only, with the rest of the framework held fixed. Each comparison measures one ingredient. All comparisons are fold-paired over the same five folds.

**Issue.** The opener repeats the closing figure of §5.2, uses the conversational 'what makes an operator work' and ends on a terse 'Each comparison measures one ingredient' without saying which ingredients follow, so the reader has no map of the five subsections. The blanket 'All comparisons are fold-paired over the same five folds' does not hold for the seed-42 matched transport control, which is paired on folds 0 to 3 only (§5.3.4).

**Suggestion.**

> Since the strongest arms of different classes lie within about 0.04 of each other, a comparison of whole architectures shows little about which properties of an operator matter. This section therefore compares operators that differ in one property only, with the rest of the framework held fixed, so that each comparison measures one ingredient: spatial context (\S\ref{sec:experiments:ingredients:context}), physical reach at lesion scale (\S\ref{sec:experiments:ingredients:reach}), global and local context together (\S\ref{sec:experiments:ingredients:global}) and an explicit transport term (\S\ref{sec:experiments:ingredients:transport}). The last subsection relates reach and transport (\S\ref{sec:experiments:ingredients:convergence}). Unless stated otherwise, all comparisons are fold-paired over the same five folds.

### 5b.2 [low] §5.3.1 Spatial Context

`05-experiments.tex:475` · GPTZero: AI · ai-tone

> With zero rounds, the per-pixel floor reads 0.0000 on every fold, identical to persistence. With one round, the one-hop floor reads $0.4515 \pm 0.0243$. With two rounds, the $k$-NN arm reads $0.4623 \pm 0.0361$.

**Issue.** Three mirror sentences with identical openings and verbs ('With … rounds, the … reads') form a mechanical tricolon.

**Suggestion.**

> Without message passing, the per-pixel floor reads 0.0000 on every fold, identical to persistence. One round (the one-hop floor) scores $0.4515 \pm 0.0243$ and two rounds (the $k$-NN arm) $0.4623 \pm 0.0361$.

### 5b.3 [low] §5.3.1 Spatial Context

`05-experiments.tex:478` · GPTZero: AI · clarity

> One round against two gives $\Delta = -0.0108 \pm 0.0061$~SE (1/5), under the paired floor, and per eye $-0.0122 \pm 0.0051$ (33/75, $t = -2.4$).

**Issue.** The fold-paired value gets a verdict ('under the paired floor') but the per-eye value does not. §5.1.4 gives no per-eye criterion, so the reader cannot tell what t = -2.4 means until the paragraph's last sentence, after the seed-7 values.

**Suggestion.**

> One round against two gives $\Delta = -0.0108 \pm 0.0061$~SE (1/5), under the paired floor, and per eye $-0.0122 \pm 0.0051$ (33/75, $t = -2.4$), in the same direction; the difference is not established.

### 5b.4 [low] §5.3.1 Spatial Context

`05-experiments.tex:485` · GPTZero: human · tone, flow

> A single ring of neighbours therefore buys almost everything the graph network on this graph achieves, and the second ring adds little or nothing. Every point of change-region Dice comes from spatial context.

**Issue.** 'Buys' is a colloquial economic metaphor. 'The second ring adds little or nothing' repeats the previous paragraph's last sentence (l.483). The free-standing 'Every point …' repeats the §5.2 conclusion without saying so.

**Suggestion.**

> One ring of neighbours therefore accounts for almost all of the score that the graph network reaches on this graph. As in~\S\ref{sec:experiments:main-results}, every point of change-region Dice comes from spatial context.

### 5b.5 [low] §5.3.2 Physical Reach at Lesion Scale

`05-experiments.tex:505` · GPTZero: AI · tone, ai-tone

> This is the largest effect in the project. It was obtained by changing only the edge set, at the same parameter count, and it is the reason the dilated stencil is the canonical configuration.

**Issue.** 'In the project' is an informal register for a thesis. The second sentence is a summary closer that restates the paragraph's opening (only the edge set changed; 67\,147 parameters on both sides).

**Suggestion.**

> This is the largest effect measured in this work, obtained by changing only the edge set at the same parameter count, and the reason the dilated stencil is the canonical configuration.

### 5b.6 [medium] §5.3.2 Physical Reach at Lesion Scale

`05-experiments.tex:515` · GPTZero: AI · clarity

> The $\pm 42$ geometry keeps the 20 neighbours of the default by doubling the column spacing from 7 to 14, so its neighbours are sparser. The geometry reaching $\pm 35$ columns keeps the default spacing of 7 columns instead, with 32 neighbours; it is also lower, but under the floor. A longer reach therefore does not help even when the spacing is kept, so the penalty at $\pm 42$ columns is not a matter of sparser neighbours alone.

**Issue.** The passage checks a confound (at ±42 reach and sparsity change together), but it never says so. The reader has to work out why the ±35 geometry is introduced, and the last sentence chains 'therefore … so'.

**Suggestion.**

> The $\pm 42$ geometry keeps the 20 neighbours of the default by doubling the column spacing from 7 to 14, so its reach grows and its neighbours become sparser at the same time. The geometry reaching $\pm 35$ columns keeps the default spacing of 7 columns instead, with 32 neighbours, and is also lower, though under the floor. A longer reach thus does not help even at the default spacing, and the penalty at $\pm 42$ columns is not a matter of sparser neighbours alone.

### 5b.7 [low] §5.3.2 Physical Reach at Lesion Scale

`05-experiments.tex:521` · GPTZero: AI · clarity, tone *(added in verification)*

> Widening the stencil across rows, to $\pm 2$ rows, costs the most of all geometries.

**Issue.** 'Costs the most' is colloquial. In a chapter with a cost column (training time per epoch), it can be misread as computational cost rather than as loss of Dice.

**Suggestion.**

> Widening the stencil across rows, to $\pm 2$ rows, lowers the score most of all geometries.

### 5b.8 [low] §5.3.2 Physical Reach at Lesion Scale

`05-experiments.tex:580` · GPTZero: human · tone, clarity

> A higher degree at the same reach buys nothing.

**Issue.** 'Buys nothing' is colloquial. The graph-theory term 'degree' is used before the next sentence explains it as the number of neighbours.

**Suggestion.**

> More neighbours at the same reach do not raise the score.

### 5b.9 [low] §5.3.2 Physical Reach at Lesion Scale

`05-experiments.tex:586` · GPTZero: human · ai-tone

> What matters is where the neighbours are placed, not how many there are.

**Issue.** A pseudo-cleft ('What matters is …') combined with an 'X, not Y' antithesis, used as an aphoristic paragraph closer.

**Suggestion.**

> The gain of the dilated stencil is thus attributable to the placement of its neighbours and not to their number.

### 5b.10 [medium] §5.3.2 Physical Reach at Lesion Scale

`05-experiments.tex:589` · GPTZero: AI · flow, tone

> This also explains an earlier result. Before the dilated stencil, the parameter-matched U-Net was higher than the $k$-NN graph network:

**Issue.** The opening 'This' points back two paragraphs (to the reach result), while the paragraph just before it is about k = 20. 'An earlier result' and 'Before the dilated stencil' narrate project history, although the U-Net/k-NN comparison is a current measurement.

**Suggestion.**

> The reach result also explains a second difference. The parameter-matched U-Net is higher than the $k$-NN graph network:

### 5b.11 [low] §5.3.2 Physical Reach at Lesion Scale

`05-experiments.tex:594` · GPTZero: AI · flow

> At seed 42, fold 3 reads $-0.042$, so the effect is fold-heterogeneous.

**Issue.** The seed-42 caveat comes after the seed-7 values, so the reader has to jump back a seed.

**Suggestion.**

> Move it directly after the seed-42 values: '… and per eye $+0.0399 \pm 0.0102$ (53/75, $t = 3.93$); at this seed, fold 3 reads $-0.042$, so the effect is fold-heterogeneous. At seed 7, with the same seed on both sides, the difference is $+0.0548 \pm 0.0181$ fold-paired (5/5) and $+0.0517 \pm 0.0109$ per eye (59/75).'

### 5b.12 [medium] §5.3.2 Physical Reach at Lesion Scale

`05-experiments.tex:597` · GPTZero: AI · ai-tone, clarity

> The deficit of the graph network was therefore located in its graph --- in where its neighbours lie physically --- and not in its operator class.

**Issue.** An em-dash aside combined with an 'and not' antithesis as a summary closer; 'located in … in where' is awkward.

**Suggestion.**

> The deficit of the graph network therefore lay in the physical placement of its neighbours and not in its operator class.

### 5b.13 [medium] §5.3.3 Global and Local Context Together

`05-experiments.tex:604` · GPTZero: human · flow

> The Fourier Neural Operator has global spectral support but no local path (\S\ref{sec:method:family:dense}). The local-kernel hybrid adds a $3 \times 3$ local path to the same operator, at a cost of 800 parameters.

**Issue.** The subsection goes from the two operators straight into five pairwise comparisons at two seeds without saying which comparison answers which question, so the reader has to sort them out alone.

**Suggestion.**

> Append: 'The FNO is compared with the $k$-NN graph network and the U-Net to test global support alone, the hybrid with the FNO to isolate the local path, and the hybrid with the $k$-NN graph network and the U-Net to test the two together.'

### 5b.14 [low] §5.3.3 Global and Local Context Together

`05-experiments.tex:610` · GPTZero: AI · tone, clarity

> Fold 4 carries all of it: without fold 4 the fold-paired difference is $-0.001$, and on both instruments it does not survive leaving one fold out, so this difference is not established.

**Issue.** A personified, colloquial 'carries all of it' with a colon reveal, followed by three clauses chained with 'and … so'.

**Suggestion.**

> The whole difference comes from fold 4; without it, the fold-paired difference is $-0.001$. On neither instrument does the difference survive leaving one fold out, so it is not established.

### 5b.15 [medium] §5.3.3 Global and Local Context Together

`05-experiments.tex:614` · GPTZero: AI · ai-tone, clarity

> That the FNO lies below the U-Net at the one-year anchor is established. Beyond one year the order changes. In the growth-region Dice by horizon, the FNO reads 0.546, 0.583 and 0.594 for one to two, two to three and more than three years, and the U-Net 0.563, 0.581 and 0.555: the FNO trails the U-Net in the second year, ties it in the third and lies above it beyond three years (Figure~\ref{fig:experiments:horizon}a).

**Issue.** A subject-clause opener ('That X … is established'), then two parallel number triplets that the reader has to pair up before the colon gives the reading, then a closing tricolon.

**Suggestion.**

> The FNO lies below the U-Net at the one-year anchor, and this difference is established. Beyond one year the order changes (Figure~\ref{fig:experiments:horizon}a): in the growth-region Dice by horizon, the FNO trails the U-Net from one to two years (0.546 against 0.563), ties it from two to three years (0.583 against 0.581) and lies above it beyond three years (0.594 against 0.555).

### 5b.16 [medium] §5.3.3 Global and Local Context Together

`05-experiments.tex:631` · GPTZero: AI · clarity, ai-tone

> The effect of the local path itself is the hybrid against the FNO: $\Delta = +0.0153 \pm 0.0110$~SE, which is under the paired floor, but per eye $+0.0190 \pm 0.0070$ (48/75), which graduates on that instrument. The two instruments disagree here, which is why both are always quoted.

**Issue.** An effect is equated with a comparison ('The effect … is the hybrid against the FNO'), and there are three 'which' clauses in two sentences. 'Graduates on that instrument' contradicts §5.1.4, where a result graduates only when both instruments agree. The last sentence re-justifies the method of §5.1.4.

**Suggestion.**

> The local path itself is isolated by the hybrid against the FNO. The fold-paired difference, $\Delta = +0.0153 \pm 0.0110$~SE, is under the paired floor, while the per-eye difference, $+0.0190 \pm 0.0070$ (48/75), counts as an effect on that instrument. This is the disagreement between the two instruments referred to in~\S\ref{sec:experiments:protocol:stats}.

### 5b.17 [low] §5.3.3 Global and Local Context Together

`05-experiments.tex:640` · GPTZero: AI · tone

> The local path no longer helps: the hybrid against the FNO gives $-0.0057 \pm 0.0105$~SE (3/5) and per eye $-0.0054$ (35/75). And the hybrid lies below the U-Net, by $-0.0193 \pm 0.0051$~SE on all five folds and per eye $-0.0227 \pm 0.0091$ (26/75, $t = -2.5$).

**Issue.** 'No longer' implies a change over time, although only the seed differs. The sentence-initial 'And' is conversational.

**Suggestion.**

> At this seed the local path does not help: the hybrid against the FNO gives $-0.0057 \pm 0.0105$~SE (3/5) and per eye $-0.0054$ (35/75). The hybrid also lies below the U-Net, by $-0.0193 \pm 0.0051$~SE on all five folds and per eye $-0.0227 \pm 0.0091$ (26/75, $t = -2.5$).

### 5b.18 [medium] §5.3.3 Global and Local Context Together

`05-experiments.tex:648` · GPTZero: AI · ai-tone, clarity

> What holds at both seeds is therefore that global spectral support alone does not reach the U-Net at the one-year anchor. That a minimal local path closes this gap rests on seed 42 alone; at seed 7 it does not, and the claim is not established.

**Issue.** Two consecutive cleft or subject-clause constructions ('What holds … is that', 'That X rests on'), with 'alone' used twice, give a recognisably machine-like rhythm.

**Suggestion.**

> At both seeds, therefore, global spectral support alone does not reach the U-Net at the one-year anchor. A minimal local path closes this gap at seed 42 but not at seed 7, so the claim is not established.

### 5b.19 [medium] §5.3.4 An Explicit Transport Term

`05-experiments.tex:661` · GPTZero: AI · clarity, tone

> The ablation is purely additive: both heads are zero-initialised, so both arms start as the same function.

**Issue.** 'Purely' is an intensifier of the kind the author removes elsewhere. 'Both heads' is ambiguous, because the control has only one head and the reader does not know which two are meant.

**Suggestion.**

> The T-FEN differs from this control only by the added transport head. Its free-form and transport heads are both zero-initialised, so the two arms start as the same function.

### 5b.20 [low] §5.3.4 An Explicit Transport Term

`05-experiments.tex:670` · GPTZero: AI · clarity

> so the effect does not depend on the form of the operator.

**Issue.** In this thesis 'operator' denotes the whole $f_\theta$ in the slot; here only the transport operator is meant.

**Suggestion.**

> so the effect does not depend on the form of the transport operator.

### 5b.21 [low] §5.3.4 An Explicit Transport Term

`05-experiments.tex:677` · GPTZero: human · clarity

> Part of the gain could therefore come from the extra parameters. A second control closes this gap.

**Issue.** In this section 'gap' also stands for score differences (l.650, l.706); here it means the difference in parameter count, which invites a misreading.

**Suggestion.**

> Part of the gain could therefore come from the extra parameters. A second control removes this difference in parameter count.

### 5b.22 [medium] §5.3.4 An Explicit Transport Term

`05-experiments.tex:680` · GPTZero: AI · clarity

> At seed 42, this control does not train on fold 4: its training error rises from the first epoch instead of falling, and it reads 0.047 at the anchor, in two separate attempts, while the width-96 control trains normally on the same fold (0.501).

**Issue.** Four clauses in one sentence. 'In two separate attempts' sits where it appears to modify only the anchor reading, not the failure to train.

**Suggestion.**

> At seed 42, this control does not train on fold 4. In two separate attempts, its training error rises from the first epoch instead of falling, and it reads 0.047 at the anchor; the width-96 control trains normally on the same fold (0.501).

### 5b.23 [low] §5.3.4 An Explicit Transport Term

`05-experiments.tex:689` · GPTZero: AI · clarity

> The extra width moves the free-form network by little at either seed ($-0.0084$ on folds 0 to 3 at seed 42, $+0.0135$ at seed 7, both under the floor). The transport effect is therefore not a matter of parameter count.

**Issue.** 'Moves … by little' is unidiomatic.

**Suggestion.**

> Widening the free-form network changes its score little at either seed ($-0.0084$ on folds 0 to 3 at seed 42, $+0.0135$ at seed 7, both under the floor). The transport effect is therefore not a matter of parameter count.

### 5b.24 [medium] §5.3.4 An Explicit Transport Term

`05-experiments.tex:699` · GPTZero: AI · ai-tone

> Where the transport term acts can be seen in the first year.

**Issue.** A pseudo-cleft opener with an abstract subject clause ('Where … acts can be seen').

**Suggestion.**

> The effect of the transport term is visible in the first year.

### 5b.25 [medium] §5.3.4 An Explicit Transport Term

`05-experiments.tex:699` · GPTZero: AI · clarity

> In the growth-region Dice between baseline and one year, the free-form FEN reads 0.388, close to the one-hop floor (0.395) and the $k$-NN graph network (0.397), the operators whose reach falls short of the per-visit front advance (\S\ref{sec:method:graph}).

**Issue.** The trailing appositive can be read as describing only the last two operators, although the argument and Figure 5.5b put the free-form FEN in the same group.

**Suggestion.**

> In the growth-region Dice between baseline and one year, the free-form FEN reads 0.388, close to the one-hop floor (0.395) and the $k$-NN graph network (0.397); the single step of all three reaches less far than the per-visit front advance (\S\ref{sec:method:graph}).

### 5b.26 [low] §5.3.4 An Explicit Transport Term

`05-experiments.tex:706` · GPTZero: AI · ai-tone, flow

> The two constructions close the same near-term gap.

**Issue.** A one-line aphoristic closer. It restates the preceding sentence (the T-FEN reaches the level of the dilated stencil), anticipates §5.3.5 and uses the overloaded 'gap' again.

**Suggestion.**

> Cut the sentence; the preceding sentence states the result and §5.3.5 draws the conclusion.

### 5b.27 [low] §5.3.4 An Explicit Transport Term

`05-experiments.tex:715` · GPTZero: AI · clarity *(added in verification)*

> In the growth-region Dice by horizon, the T-FEN reads 0.519, 0.602 and 0.633 in the first three years and the dilated stencil 0.503, 0.600 and 0.634; only beyond three years does the stencil lie higher (0.655 against 0.611; Figure~\ref{fig:experiments:horizon}a).

**Issue.** Two parallel number triplets that the reader has to pair up, as at l.616-618. The point of the sentence (the two profiles are close) is easier to see when the values are paired per year.

**Suggestion.**

> In the growth-region Dice by horizon, the T-FEN and the dilated stencil read 0.519 and 0.503 in the first year, 0.602 and 0.600 in the second and 0.633 and 0.634 in the third; only beyond three years does the stencil lie higher (0.655 against 0.611; Figure~\ref{fig:experiments:horizon}a).

### 5b.28 [low] Figure 5.5 caption

`05-experiments.tex:739` · GPTZero: AI · clarity

> The dashed line gives the values reported by \citet{Mai2024} on a larger cohort of the same clinic; inputs, the area over which lesions are measured (a fixed crop here) and the evaluated visits differ, so the line is a reference, not a head-to-head comparison (\S\ref{sec:experiments:qualitative:mai}).

**Issue.** After the semicolon, the list subject 'inputs, the area … and the evaluated visits' starts without an article and at first reads as a continuation of the preceding clause.

**Suggestion.**

> The dashed line gives the values reported by \citet{Mai2024} on a larger cohort of the same clinic. Since the inputs, the area over which lesions are measured (a fixed crop here) and the evaluated visits differ, the line is a reference, not a head-to-head comparison (\S\ref{sec:experiments:qualitative:mai}).

### 5b.29 [low] §5.3.5 Two Routes to One Deficit

`05-experiments.tex:760` · GPTZero: human · tone *(added in verification)*

> An operator of that kind cannot see as far as the lesion front moves between two visits.

**Issue.** The anthropomorphic 'see' is an informal analogy. The sentence also leaves implicit that the limit applies to one step, which the Figure 5.5b caption states explicitly.

**Suggestion.**

> The single step of such an operator reaches less far than the lesion front moves between two visits.

### 5b.30 [medium] §5.3.5 Two Routes to One Deficit

`05-experiments.tex:763` · GPTZero: AI · ai-tone

> Two unrelated constructions correct this deficit. The first is physical reach: the dilated stencil, whose single hop spans 21 columns. The second is an explicit transport term: the T-FEN, established against a parameter-matched control at both seeds (on the four folds on which that control trained at seed 42, and on all five at seed 7).

**Issue.** A mirror enumeration ('The first is X: … The second is Y: …') with paired colon reveals, a symmetric template.

**Suggestion.**

> Two unrelated constructions correct this deficit. The dilated stencil extends the physical reach of a single hop to 21 columns. The T-FEN adds an explicit transport term, established against a parameter-matched control at both seeds (on the four folds on which that control trained at seed 42, and on all five at seed 7).

### 5b.31 [low] §5.3.5 Two Routes to One Deficit

`05-experiments.tex:767` · GPTZero: AI · tone, clarity

> Each is established against its own control, and the two end up within about 0.017 of each other, at the noise level; they are the two highest arms of Table~\ref{tab:experiments:arms} (\S\ref{sec:experiments:main-results}).

**Issue.** 'End up' is conversational, and 'the two' changes its referent from constructions to arms in mid-sentence. The semicolon adds a third clause.

**Suggestion.**

> Each is established against its own control. The two arms that carry them lie within about 0.017 of each other, at the noise level, and are the two highest in Table~\ref{tab:experiments:arms} (\S\ref{sec:experiments:main-results}).

### 5b.32 [medium] §5.3.5 Two Routes to One Deficit

`05-experiments.tex:771` · GPTZero: AI · ai-tone, clarity

> The central architectural result of the survey is this coincidence --- two independent routes to the same deficit --- rather than the score of any single arm. It is suggestive rather than a proof of mechanism.

**Issue.** 'Coincidence' usually implies chance, which can invert the intended meaning (agreement of two independent constructions) in the section's central claim. The passage also stacks an em-dash aside and two 'rather than' in two sentences.

**Suggestion.**

> The central architectural result of the survey is this convergence of two independent routes on the same deficit, rather than the score of any single arm. The convergence is suggestive but does not prove a mechanism.

### 5b.33 [medium] §5.3.5 Two Routes to One Deficit

`05-experiments.tex:776` · GPTZero: AI · ai-tone, flow

> The architecture class therefore is not what separates the strongest operators; the ingredients they carry are.

**Issue.** A pseudo-cleft with the antithetical answer delayed until after the semicolon. It also repeats the §5.2 sentence 'What separates the arms is therefore not their class but the ingredients they carry' in the same rhetorical form.

**Suggestion.**

> Among the strongest operators, the differences therefore follow the ingredients they carry and not the architecture class.

### 5b.34 [low] §5.3.5 Two Routes to One Deficit

`05-experiments.tex:777` · GPTZero: AI · tone, flow

> A third candidate, global and local context together, was seen at one seed only (\S\ref{sec:experiments:ingredients:global}) and is not counted among them. \S\ref{sec:experiments:ablations} reports what was measured and did not matter.

**Issue.** 'Seen' is vague. 'What was measured and did not matter' is informal and stronger than the null definition of §5.4. The sentence opens with a section symbol.

**Suggestion.**

> A third candidate, global and local context together, was observed at seed 42 only (\S\ref{sec:experiments:ingredients:global}) and is not counted among them. The comparisons without a measurable effect are reported in~\S\ref{sec:experiments:ablations}.

