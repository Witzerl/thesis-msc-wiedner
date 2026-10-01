# Micro feedback 6-7: Ch. 6 Discussion + Ch. 7 Conclusion

[← Overview](00-overview.md)

56 findings: 0 high, 31 medium, 25 low. Listed in source order. Each item gives the location, the GPTZero label of the passage, the criteria (flow, clarity, tone, ai-tone), the text as it stands in the `.tex`, the problem and a suggested rewrite. A second reviewer checked every rewrite against the original for meaning, hedges, numbers, citations, references and the passive-voice rule; *(added in verification)* marks items found in that second pass.

## Flow of this part

At section level, Chapter 6 follows the hour-glass: interpretation, then clinical implications, then limitations, then future work. Chapter 7 is organised around the two sub-questions, which suits a conclusion. Inside §6.1 the argument moves logically from the framework to the operator, but some paragraphs are badly placed. 'Predictions between visits' continues the time-integration topic of 'The framework', and six paragraphs separate the two. 'A missing counterpart to the equation features' relies on the growth-speed gap before §6.2 introduces it, and it ends with candidate descriptors that §6.4 repeats. The reasons for the weak growth-speed prediction (one visit in, no memory, conditioning without eye-specific information) are given in four places (§6.1, §6.2, §6.3, §6.4). This makes the chapter feel circular; one full statement with back-references would be enough. Within paragraphs, an inference sometimes sits two sentences away from its evidence (the operator paragraph, L52-62). A closing 'therefore' does not follow from the sentence just before it (L148-151). Some terms are used before the Discussion explains them ('reach deficit', 'growth-speed gap', 'trajectory memory'). The register is mostly objective and impersonal, but it slips into slogans and idioms ('ingredients, not classes', 'Good at where, weaker at how fast', 'lever', 'paid off', 'bought nothing', 'Take-away'). Chapter 7 also repeats several §6.1 sentences almost word for word. GPTZero left some sentences unflagged ('The comparison is not like-for-like.', 'If the class decided the outcome, such a result would be unlikely.', 'All comparisons in this thesis are made at the one-year anchor.'). They show the author's own plain declarative and conditional voice. The flagged passages rarely differ from them in vocabulary. They differ in structure: colon reveals, em-dash asides, cleft sentences and aphoristic paragraph closers.

### Transitions

- §6.1 'The framework' (06-discussion.tex L33-49): there is no blank line before L40 ('The objective is part of the framework...'), so time integration and the objective share one paragraph. Start a new paragraph at L40. The closing summary at L47 then ends the objective paragraph and still covers both points.
- §6.1 'The operator' paragraph (L52-62): the inference 'If the class decided the outcome, such a result would be unlikely' comes two sentences after the evidence it refers to (three classes within 0.04). The FEN ranking and an unexplained 'reach deficit' sit in between. Move the inference directly after the first sentence. Replace 'the reach deficit discussed below' with 'the limited reach of a single update, discussed in the next paragraph'.
- §6.1 paragraph order (optional): 'Predictions between visits' (L126-138) deals with time integration and the continuous-time reading, which belong next to the time part of 'The framework' (L33-39). It could follow 'The framework' directly. 'The operator', reach/transport, global/local and 'Capacity' would then form one uninterrupted block before 'Where modelling effort pays'. Note that the moved paragraph would then mention the energy-conserving T-FEN before the operator paragraphs do; Chapters 4-5 have already introduced it.
- §6.1 'A missing counterpart to the equation features' (L102-124) uses the 'growth-speed gap' of §6.2 before the reader has met it. Its last sentence (candidate descriptors) anticipates §6.4 'An eye-level descriptor'. Either move the paragraph so that it follows the growth-speed discussion in §6.2, or write 'the weaker prediction of growth speed (§6.2)' and move the candidates sentence (L120-124) into §6.4.
- Repetition across sections: the reasons why growth speed is predicted poorly (one visit in, no memory, conditioning without eye-specific information, covariates shared by every grid position) appear in §6.1 (L109-119), §6.2 (L181-184), §6.3 (L287-292) and §6.4 (L320-322). State them once in full (§6.2 is the natural place) and refer back from the other sections.
- §6.1 'Where modelling effort pays' (L148-151): the closing recommendation ('the first question ... is therefore how far one update reaches') follows the sentence on the objective, but it is drawn from the reach and transport results of the paragraph's first sentences. Name that basis explicitly in the last sentence (see finding at L148), or move the objective sentence before the list of nulls and drop 'by contrast'.
- §6.2 'Good at where...' -> 'Reliable horizon' (L157-202): the metric changes from change-region Dice to growth-region Dice without a reminder of the difference. Add a short defining clause at L196. The heading 'Reliable horizon' also promises an answer that the paragraph declines to give ('cannot be judged from the data'). 'Forecast horizon' matches the content.
- §6.3 'Data and labels' (L259-272): one paragraph carries three unrelated limitations (pixel spacing, label provenance, shrinking reference masks). The 'also' at L266 makes the shrinkage read as another point about spacing. Start a new paragraph at 'The reference masks also shrink between visits.'
- §6.3 after 'Model scope' (L296-303): the paragraph on PINNs and the uniform grid has no heading and no link to the preceding paragraph, which is about what the operators receive. Add a heading such as '\paragraph{Scope of the survey.}' or an opening sentence such as 'Two directions lie outside the main survey.'
- §6.4 'Clinical use' (L348-350): the sentence on joint training across diseases concerns the data limitation, not uncertainty or clinical use. Give it its own short paragraph, or attach it to 'From raw OCT, in 3-D.'
- Ch. 7 'The operator' (07-conclusion.tex L57-64): the two FNO sentences sit between the reach/transport bullets and the sentence that interprets them ('Reach and transport are two unrelated ways...'). Put the interpretation directly after \end{itemize} and the FNO observation after it.
- Ch. 7 'The framework' vs 'What did not matter' (L27-28 and L68-69): the Runge-Kutta null is stated twice; keep it in one place. The sentence on the validity diagnostics (L72-76) is a limit on interpretation, not a negative result on accuracy. It fits better at the end of 'The framework' (as a statement about what the update is); otherwise widen the heading.
- Ch. 7 'Clinical position' (L86-87): the sentence on the limits of every conclusion is general, but it closes a paragraph about growth speed. Move it into the final paragraph, before the closing claim, so that the limits frame the take-away.
- Ch. 6 -> Ch. 7: several Chapter 7 sentences repeat §6.1 almost verbatim: the em-dash list of the three strongest operators (§6.1 L52-53 / Ch. 7 L34-35), 'How time enters the update mattered less than that it enters' (L33 / L27), and 'learned no change at all' (L42 / L25). A conclusion may restate findings, but rephrasing them avoids the impression of copied text.

### Recurring tells in this part

- A colon reveal delivers a verdict or explanation ('X: Y') about 15 times outside lists, e.g. 'The framework transferred: one setup served operators from unrelated literatures without change.' (L17). Keep the colon where it introduces a list; elsewhere use a full stop, 'because' or 'so'.
- Em-dash asides: 6 pairs in the range (4 in Ch. 6, 2 in Ch. 7). Examples: '--- a finite-element network, a graph network and a U-Net ---' (verbatim in §6.1 L52 and Ch. 7 L34) and '--- its reach along the direction in which the front moves ---' (L142). Replace them with commas, parentheses or a relative clause.
- Cleft and pseudo-cleft sentences, about 8, e.g. 'What the framework needs, in short, is ...' (L47), 'What separates operators is instead ...' (L58), 'What is lost is ...' (L116), 'This is what made ... possible at all' (L29), 'it is what lets' (L105), 'is not what decides' (Ch. 7 L33), 'what matters is' (Ch. 7 L91). Use the plain subject-verb form.
- 'at all' as an intensifier, about 6-7 times, e.g. 'possible at all' (L30), 'no change at all' (L42; Ch. 7 L25, L44), 'spatial context at all' (L60), 'whether anything was learned at all' (L149). Drop it, or write 'any' where the meaning is 'even minimal'.
- Antithesis 'X, not Y' / 'rather than', about 8-10, e.g. the heading 'ingredients, not classes' (L51), 'an orientation point, not a target' (L213), 'not a continuous-time model' (Ch. 7 L74), 'rather than additional knowledge' (L38), 'rather than to one operator' (L167), 'rather than the choice of operator family' (Ch. 7 L94). Keep the ones that carry a scoped claim and rephrase the rest positively.
- Aphoristic paragraph closers that restate the paragraph, about 5, e.g. 'it is a more specific statement than any ranking of architectures' (L79), 'What the framework needs, in short, ...' (L47), 'more informative than the score of any single model' (Ch. 7 L64), and the 'Take-away' sentence. Cut them or fold them into the preceding sentence.
- Mirror pairs and symmetric clauses, about 4, e.g. 'The framework transferred: ... The operator class did not decide the outcome; a small number of properties of the operator did.' (L17-20), the double 'whereas ...; ... whereas' (L169-173), and 'neither benefits from nor accounts for' (L293).
- Personified abstractions, about 8, e.g. 'the gap belongs to the approach' (L167), 'nothing in the conditioning tells the operator' (L183), the covariates 'cannot say anything' (L111), 'The validity diagnostics also limit what may be said' (Ch. 7 L72), 'bound every conclusion drawn here' (Ch. 7 L87). 'How far one update can see' and 'where an operator looks' recur about 5 times; as shorthand for receptive field they are acceptable if used sparingly.
- Idioms and metaphors, about 10, e.g. 'turned out' (L33), 'not a lever' (L94), 'weigh more' (L98), 'paid off' (L141), 'most worth its burden' (L188), 'end up' (L70), 'catches up' (L88), 'anyway' (L254), 'bought nothing' (Ch. 7 L28), 'absorbs the irregularity' (Ch. 7 L16), plus the headings 'Good at where, weaker at how fast', 'Where modelling effort pays' and 'Take-away'.
- Short announcement openers, about 4-5, e.g. 'The results answer the two parts differently.' (L17), 'Taken together, the positive results and the nulls indicate where effort paid off' (L141), 'The distinction matters clinically.' (L186). Most are harmless topic sentences; trim only the ones that just restate the heading.
- Vocabulary alternates in the closing chapters: 'arms', 'operators', 'models' and 'networks' all name the compared models (e.g. 'The three highest arms', L52, vs 'The three strongest operators', Ch. 7 L34), and 'ingredients' (L51, L82) alternates with 'properties' (L19, L59, Ch. 7 L40). Within Chapters 6-7, consider one term for each, unless 'arm' is meant in its narrower Chapter 5 sense of a configured run.
- Terms appear in the Discussion before it explains them, or without a reminder of their Chapter 5 definition: 'reach deficit' (L57), 'growth-speed gap' (L119), 'trajectory memory' (L123), 'fast-progressor AUCs' (L164), 'per-eye instrument' (L282).

## Findings

### 6-7.1 [medium] §6.1 Interpretation of Results (opening)

`06-discussion.tex:16` · GPTZero: AI · clarity, ai-tone

> The results answer the two parts differently. The framework transferred: one setup served operators from unrelated literatures without change. The operator class did not decide the outcome; a small number of properties of the operator did.

**Issue.** A colon reveal and a semicolon antithesis form a mirror pair of short verdicts. 'Transferred' has no object, so the reader has to infer across what the framework transferred.

**Suggestion.**

> The results answer the two parts differently. The framework transferred, since one setup served operators from unrelated literatures without modification. The architecture class of the operator did not decide the outcome, whereas a small number of its properties did.

### 6-7.2 [medium] §6.1 'The framework.'

`06-discussion.tex:27` · GPTZero: AI · clarity, ai-tone

> Under these conditions, every operator with any spatial context learned, and every one of them lies far above persistence. This is what made the comparison of Chapter~\ref{ch:experiments} possible at all, and it is the answer to the first part of the question.

**Issue.** 'Learned' has no object, and 'every ... every one' repeats. The cleft 'This is what made ... possible at all' has an unclear 'This' (the setup, or the fact that every operator learned?) and adds an intensifier.

**Suggestion.**

> Under these conditions, every operator with any spatial context learned to predict change and lies far above persistence. This common setup made the comparison of Chapter~\ref{ch:experiments} possible, and it is the answer to the first part of the question.

### 6-7.3 [medium] §6.1 'The framework.' (time)

`06-discussion.tex:33` · GPTZero: AI · clarity, ai-tone

> How time enters the update turned out to matter less than that it enters. A fourth-order Runge--Kutta step in place of one Euler step changed nothing measurable, over a local and over a global operator (\S\ref{sec:experiments:ablations:time}).

**Issue.** 'Turned out' is narrative. The compressed 'less than that it enters' is hard to parse on first reading, and Ch. 7 reuses the same aphorism. 'over a local and over a global operator' reads awkwardly.

**Suggestion.**

> The form in which $\Delta t$ enters the update mattered less than the fact that it enters. Replacing one Euler step by a fourth-order Runge--Kutta step made no measurable difference for either a local or a global operator (\S\ref{sec:experiments:ablations:time}).

### 6-7.4 [low] §6.1 'The framework.' (time)

`06-discussion.tex:36` · GPTZero: AI · clarity, ai-tone

> The multiplication of the operator output by $\Delta t$ is, on the mask channel, a change of parameterisation rather than additional knowledge, and removing it does not change the result.

**Issue.** The interjection 'on the mask channel' splits the subject from its complement, and 'rather than additional knowledge' is a vague antithesis.

**Suggestion.**

> On the mask channel, multiplying the operator output by $\Delta t$ only changes the parameterisation and adds no prior knowledge; removing the multiplication does not change the result.

### 6-7.5 [medium] §6.1 'The framework.' (objective)

`06-discussion.tex:40` · GPTZero: AI · flow, clarity

> The objective is part of the framework, and two of its parts are needed (\S\ref{sec:experiments:ablations:loss}).

**Issue.** No blank line precedes this sentence, so the objective is discussed in the same paragraph as time integration. 'part ... parts' repeats, and three ablations follow, so the reader has to work out which two components are meant.

**Suggestion.**

> Start a new paragraph here: "The objective belongs to the framework as well, and two of its components are needed (\S\ref{sec:experiments:ablations:loss}): the weighting of the mask channel and the soft-Dice term."

### 6-7.6 [low] §6.1 'The framework.' (closing sentence)

`06-discussion.tex:47` · GPTZero: AI · ai-tone, tone

> What the framework needs, in short, is a loss that puts weight on the lesion mask, an interval length that reaches the operator, and everything else held fixed.

**Issue.** A pseudo-cleft with 'in short' turns the sentence into an aphoristic closer that restates the paragraph.

**Suggestion.**

> In summary, the framework needs a loss that weights the lesion mask, an interval length that reaches the operator, and all other components held fixed. (Alternatively, cut the sentence; the paragraph already says this.)

### 6-7.7 [low] §6.1 heading 'The operator: ingredients, not classes.'

`06-discussion.tex:51` · GPTZero: AI · tone

> \paragraph{The operator: ingredients, not classes.}

**Issue.** The heading is a slogan-like antithesis. It also breaks the parallel with the plain heading 'The framework.' above it, and the paragraph itself speaks of 'properties'.

**Suggestion.**

> \paragraph{The operator.}

### 6-7.8 [medium] §6.1 'The operator' (L52-62)

`06-discussion.tex:54` · GPTZero: AI · flow, clarity

> The finite-element network is highest: it lies above the U-Net at both seeds and only slightly above the graph network. The two highest are the two that carry a remedy for the reach deficit discussed below. If the class decided the outcome, such a result would be unlikely.

**Issue.** 'Such a result' most naturally refers to the first sentence (three unrelated classes within 0.04), but two sentences intervene, so the referent is unclear. The 'reach deficit' is used before the reader knows what it is.

**Suggestion.**

> Move "If the class decided the outcome, such a result would be unlikely." directly after the sentence ending "(\S\ref{sec:experiments:main-results}).", then continue: "The finite-element network is highest: it lies above the U-Net at both seeds and only slightly above the graph network. These two are also the arms that compensate for the limited reach of a single update, discussed in the next paragraph."

### 6-7.9 [medium] §6.1 'The operator' (properties list)

`06-discussion.tex:58` · GPTZero: AI · ai-tone, clarity *(added in verification)*

> What separates operators is instead a set of properties that can be switched on and off one at a time (\S\ref{sec:experiments:ingredients}): spatial context at all, physical reach at the scale of the lesion front, and an explicit transport term.

**Issue.** A pseudo-cleft opens the sentence, and 'spatial context at all' is an ungrammatical list item that uses 'at all' as an intensifier.

**Suggestion.**

> Instead, the operators are separated by a set of properties that can be switched on and off one at a time (\S\ref{sec:experiments:ingredients}): the presence of any spatial context, physical reach at the scale of the lesion front, and an explicit transport term.

### 6-7.10 [low] §6.1 reach and transport paragraph

`06-discussion.tex:69` · GPTZero: AI · tone *(added in verification)*

> Each is established against its own control, and the two end up indistinguishable from each other.

**Issue.** 'End up' is a narrative idiom.

**Suggestion.**

> Each is established against its own control, and the two are indistinguishable from each other.

### 6-7.11 [low] §6.1 reach and transport paragraph (closing)

`06-discussion.tex:77` · GPTZero: AI · ai-tone, clarity

> The coincidence of two routes is suggestive rather than a proof of mechanism, but it is a more specific statement than any ranking of architectures.

**Issue.** This is an aphoristic closer built on 'rather than ... but'. 'Coincidence' also suggests chance, which is not what is meant.

**Suggestion.**

> The agreement of the two routes is suggestive but does not prove a mechanism; it is nevertheless more specific than any ranking of architectures.

### 6-7.12 [low] §6.1 global and local context

`06-discussion.tex:89` · GPTZero: AI · clarity

> These horizon values are descriptive and were not tested, but they suggest that global support matters more for long forecasts than for the one-year anchor.

**Issue.** 'Were not tested' could be read as 'not measured'. What is meant is that no statistical test was applied.

**Suggestion.**

> These horizon values are descriptive and were not tested statistically, but they suggest that global support matters more for long forecasts than at the one-year anchor.

### 6-7.13 [low] §6.1 'Capacity.'

`06-discussion.tex:94` · GPTZero: AI · tone, clarity

> Capacity was not a lever in any of the four classes tested (\S\ref{sec:experiments:ablations:capacity}): no width step raised a class above the noise level, and the smaller versions lost little.

**Issue.** 'Lever' is a metaphor, and 'raised a class above the noise level' confuses the class with the size of its gain.

**Suggestion.**

> Larger capacity did not help in any of the four classes tested (\S\ref{sec:experiments:ablations:capacity}): no increase in width improved a class by more than the noise level, and the smaller versions lost little.

### 6-7.14 [low] §6.1 'Capacity.'

`06-discussion.tex:96` · GPTZero: human · clarity

> With 75 eyes, this is what the low-data argument of Chapter~\ref{ch:introduction} leads one to expect: the assumptions built into an operator weigh more than its size. The capacity study shows that size did not help; that the built-in assumptions are the reason is an interpretation, supported by the ingredient study.

**Issue.** The clause after the semicolon has a nominal 'that'-clause as its subject and is hard to parse. 'Weigh more' is a mild metaphor.

**Suggestion.**

> With 75 eyes, this is what the low-data argument of Chapter~\ref{ch:introduction} leads one to expect: the assumptions built into an operator matter more than its size. The capacity study shows that size did not help; attributing this to the built-in assumptions is an interpretation, supported by the ingredient study.

### 6-7.15 [medium] §6.1 'A missing counterpart to the equation features.'

`06-discussion.tex:103` · GPTZero: AI · ai-tone, clarity

> In MP-PDE, a vector of equation features $\theta_{\text{PDE}}$ --- the coefficients and boundary conditions of the equation being solved --- is passed to every layer, and it is what lets one trained solver handle a whole family of equations \citep{Brandstetter2022}.

**Issue.** An em-dash aside splits subject and verb, and a cleft ('it is what lets') follows. The sentence is long for a definition.

**Suggestion.**

> In MP-PDE, every layer receives a vector of equation features $\theta_{\text{PDE}}$, which holds the coefficients and boundary conditions of the equation being solved; this vector allows one trained solver to handle a whole family of equations \citep{Brandstetter2022}.

### 6-7.16 [low] §6.1 'A missing counterpart to the equation features.'

`06-discussion.tex:106` · GPTZero: AI · clarity

> GA has no governing equation, and so no such vector exists.

**Issue.** Every other place in the thesis says the equation is unknown (§1.3 L158, §2 L758 'no known governing equation', §4 L339, §6.3 L297). 'Has no governing equation' is a different, ontological claim.

**Suggestion.**

> No governing equation is known for GA, so no such vector is available.

### 6-7.17 [low] §6.1 'A missing counterpart to the equation features.'

`06-discussion.tex:109` · GPTZero: AI · tone *(added in verification)*

> The covariates are two numbers per visit, shared by every grid position and nearly constant along a trajectory, so they can shift a prediction as a whole but cannot say anything about a particular eye's lesion.

**Issue.** 'Cannot say anything' personifies the covariates and is conversational.

**Suggestion.**

> The covariates are two numbers per visit, shared by every grid position and nearly constant along a trajectory, so they can shift a prediction as a whole but carry no information about the lesion of a particular eye.

### 6-7.18 [low] §6.1 'A missing counterpart to the equation features.'

`06-discussion.tex:111` · GPTZero: AI · clarity, tone

> The learned stand-in that the code provides, a layer encoder that summarises the retinal structure into one vector, was tested in an earlier configuration and in one design only, without a detectable benefit.

**Issue.** 'That the code provides' points to an implementation the reader has not seen. A long appositive and a trailing 'without a detectable benefit' make the sentence hard to follow.

**Suggestion.**

> A learned stand-in, a layer encoder that summarises the retinal structure in one vector, was tested only in an earlier configuration and in one design; it showed no detectable benefit.

### 6-7.19 [medium] §6.1 'A missing counterpart to the equation features.'

`06-discussion.tex:116` · GPTZero: AI · ai-tone, clarity

> What is lost is an eye-specific description of how this eye progresses.

**Issue.** A pseudo-cleft opens the paragraph, and 'eye-specific ... this eye' is redundant.

**Suggestion.**

> The conditioning therefore lacks a description of how the individual eye progresses.

### 6-7.20 [low] §6.1 'A missing counterpart to the equation features.'

`06-discussion.tex:119` · GPTZero: AI · flow, clarity

> This is a plausible contributor to the growth-speed gap discussed in \S\ref{sec:discussion:clinical}, but it was not tested.

**Issue.** 'Growth-speed gap' is used as a known term, but §6.2 introduces it only later.

**Suggestion.**

> This is a plausible contributor to the weaker prediction of growth speed discussed in \S\ref{sec:discussion:clinical}, but it was not tested.

### 6-7.21 [medium] §6.1 'A missing counterpart to the equation features.'

`06-discussion.tex:120` · GPTZero: AI · flow, clarity

> Candidates for the slot are descriptors that do vary between eyes: lesion-level quantities such as size, shape or focality, a learned summary of the observed layers, or --- with trajectory memory --- the eye's own past growth.

**Issue.** This is future-work content inside the interpretation, and §6.4 'An eye-level descriptor' largely repeats it. The em-dash aside uses 'trajectory memory' before §6.3/§6.4 introduce the term.

**Suggestion.**

> Preferably move this sentence into §6.4 'An eye-level descriptor' and end the §6.1 paragraph at '... but it was not tested.' If it stays here: "Possible candidates for the slot are descriptors that vary between eyes, such as lesion size, shape or focality, a learned summary of the observed layers or, if the operator receives past visits, the eye's own past growth."

### 6-7.22 [medium] §6.1 'Predictions between visits.'

`06-discussion.tex:130` · GPTZero: AI · flow, clarity

> The network trained inside the Runge--Kutta wrapper, and the T-FEN in its energy-conserving form, pass the solver-swap test and can therefore be read as continuous-time models (\S\ref{sec:experiments:validity:swap}).

**Issue.** The paragraph announces 'two attempts' (the regulariser and the RK wrapper), but this sentence adds a third model that was not built for this purpose, so the count no longer matches. The parenthetical also makes the subject hard to read.

**Suggestion.**

> The second attempt, training the network inside the Runge--Kutta wrapper, gives a model that passes the solver-swap test and can therefore be read as a continuous-time model; the T-FEN in its energy-conserving form passes the test as well (\S\ref{sec:experiments:validity:swap}).

### 6-7.23 [medium] §6.1 'Where modelling effort pays.'

`06-discussion.tex:141` · GPTZero: AI · ai-tone, tone

> Taken together, the positive results and the nulls indicate where effort paid off in this survey. Changing where an operator looks --- its reach along the direction in which the front moves --- or adding a mechanism that transports the state produced the largest effects.

**Issue.** The opener only restates the heading, using the idiom 'paid off'. The next sentence splits a long subject with an em-dash aside, and 'where an operator looks' personifies the operator.

**Suggestion.**

> Across the survey, the largest effects came from changing the reach of an operator along the direction in which the front moves and from adding a mechanism that transports the state.

### 6-7.24 [medium] §6.1 'Where modelling effort pays.' (closing)

`06-discussion.tex:148` · GPTZero: AI · flow, ai-tone

> The objective, by contrast, did matter: the weighting of the mask channel decided whether anything was learned at all. For a new disease-forecasting task of this kind, the first question to ask of an operator is therefore how far one update reaches compared with how far the disease moves between visits.

**Issue.** The closing 'therefore' follows the sentence on the objective, but the recommendation does not follow from it; it follows from the reach and transport results earlier in the paragraph. The emphatic 'did matter' and 'at all' add to the effect.

**Suggestion.**

> The objective, by contrast, affected the result: without the weighting of the mask channel, no change was learned. Given the effects of reach and transport, the first question to ask of an operator in a new disease-forecasting task of this kind is how far one update reaches compared with how far the disease moves between visits.

### 6-7.25 [low] §6.2 heading 'Good at where, weaker at how fast.'

`06-discussion.tex:157` · GPTZero: human · tone

> \paragraph{Good at where, weaker at how fast.}

**Issue.** The heading is conversational and slogan-like, out of register with the other paragraph headings.

**Suggestion.**

> \paragraph{Location versus speed of growth.}

### 6-7.26 [low] §6.2 location versus speed

`06-discussion.tex:162` · GPTZero: AI · clarity

> The correlation between predicted and true growth rates is 0.40 for the canonical model, against 0.61 reported by \citet{Mai2024} on a larger cohort from the same clinic, and the fast-progressor AUCs are 0.70 to 0.74 against 0.77 to 0.81 (\S\ref{sec:experiments:qualitative:mai}).

**Issue.** One sentence carries two separate comparisons, and 'fast-progressor AUCs' appears without a reminder of what it measures.

**Suggestion.**

> The correlation between predicted and true growth rates is 0.40 for the canonical model, against 0.61 reported by \citet{Mai2024} on a larger cohort from the same clinic. For identifying the fastest-growing eyes, the AUCs are 0.70 to 0.74, against 0.77 to 0.81 (\S\ref{sec:experiments:qualitative:mai}).

### 6-7.27 [low] §6.2 location versus speed

`06-discussion.tex:165` · GPTZero: AI · tone, ai-tone *(added in verification)*

> The other arms do not differ from the canonical model on these measures, so the gap belongs to the approach rather than to one operator.

**Issue.** 'The gap belongs to the approach' personifies the gap, and the sentence closes on a 'rather than' antithesis.

**Suggestion.**

> The other arms do not differ from the canonical model on these measures, so the gap lies in the shared approach and is not specific to one operator.

### 6-7.28 [medium] §6.2 comparison with Mai et al.

`06-discussion.tex:169` · GPTZero: AI · ai-tone, clarity

> \citet{Mai2024} start from the raw OCT volume, whereas every model here starts from segmented masks and layer depths; they evaluate 184 eyes with no reported cropping of the lesion area, whereas this thesis evaluates 75 eyes inside a crop that censors growth at its border. It is still notable that a model given the segmented lesion as input is weaker on growth speed than one that must find the lesion itself.

**Issue.** Two mirrored 'whereas' clauses joined by a semicolon give a symmetrical, mechanical rhythm. 'It is still notable that' is evaluative filler.

**Suggestion.**

> \citet{Mai2024} start from the raw OCT volume and evaluate 184 eyes with no reported cropping of the lesion area. Every model here starts from segmented masks and layer depths and is evaluated on 75 eyes inside a crop that censors growth at its border. Even so, a model given the segmented lesion as input is weaker on growth speed than one that must find the lesion itself.

### 6-7.29 [low] §6.2 growth speed (explanations)

`06-discussion.tex:182` · GPTZero: human · tone *(added in verification)*

> And, as argued in \S\ref{sec:discussion:interpretation}, nothing in the conditioning tells the operator how fast this particular eye progresses.

**Issue.** The sentence opens with a conversational 'And', and 'nothing ... tells the operator' personifies the conditioning.

**Suggestion.**

> Finally, as argued in \S\ref{sec:discussion:interpretation}, the conditioning carries no information on how fast this particular eye progresses.

### 6-7.30 [medium] §6.2 clinical relevance of growth speed

`06-discussion.tex:186` · GPTZero: AI · tone, clarity, ai-tone

> The distinction matters clinically. Complement inhibitors slow GA growth but do not stop it (\S\ref{sec:introduction:motivation}), so the eyes that grow fastest are the ones for which treatment is most worth its burden. That decision depends on growth speed, which is the weaker of the two capabilities.

**Issue.** The paragraph opens with an announcement and uses the idiom 'most worth its burden'. 'That decision' then refers to a decision that has not been named.

**Suggestion.**

> The distinction is clinically relevant. Complement inhibitors slow GA growth but do not stop it (\S\ref{sec:introduction:motivation}), so the benefit of treatment relative to its burden is largest in the eyes that grow fastest. The decision to treat therefore depends on growth speed, the weaker of the two capabilities.

### 6-7.31 [medium] §6.2 'Reliable horizon.'

`06-discussion.tex:195` · GPTZero: AI · clarity, flow

> Beyond one year, the growth-region Dice of the canonical model does not fall; it lies at about 0.60 to 0.66 in the second, third and later years (\S\ref{sec:experiments:ingredients:transport}).

**Issue.** The section switches from the change-region Dice (L158) to the growth-region Dice without a reminder of the difference. The heading 'Reliable horizon' promises a verdict that the paragraph declines to give.

**Suggestion.**

> Beyond one year, the growth-region Dice of the canonical model, which scores only new atrophy, does not fall; it lies at about 0.60 to 0.66 in the second, third and later years (\S\ref{sec:experiments:ingredients:transport}). (Also consider renaming the heading to \paragraph{Forecast horizon.})

### 6-7.32 [medium] §6.2 grader agreement as scale

`06-discussion.tex:209` · GPTZero: AI · clarity

> A forecast with a growth-region Dice of about 0.5 in the first year, as here (Table~\ref{tab:experiments:mai-bins}), is accordingly less far from what is attainable than it would appear on a scale from 0 to 1.

**Issue.** 'Less far from what is attainable than it would appear' is a convoluted double comparison that is hard to parse.

**Suggestion.**

> On this scale, the first-year growth-region Dice of about 0.5 obtained here (Table~\ref{tab:experiments:mai-bins}) lies closer to the attainable level than its distance from 1 suggests.

### 6-7.33 [medium] §6.2 grader agreement as scale

`06-discussion.tex:212` · GPTZero: AI · tone, ai-tone

> The grader value is an orientation point, not a target or an upper limit for the models of this thesis: it was measured on a different imaging modality and a different cohort, and the graders outlined existing images rather than predicting a future one.

**Issue.** 'Orientation point' is a Germanism (Orientierungspunkt). The sentence stacks three devices: an 'X, not Y' antithesis, a colon reveal and 'rather than'.

**Suggestion.**

> The grader value is a reference point and neither a target nor an upper limit for the models of this thesis. It was measured on a different imaging modality and a different cohort, and the graders outlined existing images instead of predicting a future one.

### 6-7.34 [low] §6.2 'Position in a clinical pipeline.'

`06-discussion.tex:227` · GPTZero: AI · clarity

> Failures would matter most where the method is known to be weak: lesions that touch the border of the crop, where growth is censored; fast progressors; and eyes with sparse visit schedules, where each step must bridge a long interval.

**Issue.** After a sentence on segmentation errors, 'Failures' could mean segmentation or forecast failures. 'Matter most' also mixes how often failures occur with how much they cost.

**Suggestion.**

> Decide which is meant. If it is where failures are expected: "Forecast failures are most likely where the method is known to be weak: lesions that touch the border of the crop, where growth is censored; fast progressors; and eyes with sparse visit schedules, where each step must bridge a long interval." If it is their consequences, keep 'would matter most' and only change the subject to 'Forecast failures'.

### 6-7.35 [medium] §6.3 'Data and labels.' (crop)

`06-discussion.tex:247` · GPTZero: AI · clarity

> It cuts real lesion area in 27.3\,\% of the visits, more than 5\,\% of the lesion in 6.0\,\%, and up to 25.7\,\% in the worst case.

**Issue.** The elliptical list ('more than 5 % of the lesion in 6.0 %') makes the reader reconstruct what each percentage refers to.

**Suggestion.**

> It cuts away part of the lesion in 27.3\,\% of the visits; in 6.0\,\% the loss exceeds 5\,\% of the lesion, and in the worst case it reaches 25.7\,\%.

### 6-7.36 [low] §6.3 'Data and labels.' (crop)

`06-discussion.tex:249` · GPTZero: AI · clarity

> In 31.1\,\% of the visits, the lesion touches the edge of the imaged field inside the window, so its growth across that edge is censored, in the training targets and in the metrics, without any flag.

**Issue.** A comma-heavy chain of four clauses ends in jargon ('without any flag').

**Suggestion.**

> In 31.1\,\% of the visits, the lesion touches the edge of the imaged field inside the window. Its growth across that edge is therefore censored, in the training targets and in the metrics, and the censored cases are not marked in the data.

### 6-7.37 [low] §6.3 'Data and labels.' (crop)

`06-discussion.tex:252` · GPTZero: AI · tone *(added in verification)*

> Larger windows would trade this for up to 35\,\% zero padding and about $1.9\times$ as many grid positions, and about 19\,\% of lesions would touch the border anyway because they reach the edge of the scan itself.

**Issue.** 'Anyway' is conversational.

**Suggestion.**

> Larger windows would trade this for up to 35\,\% zero padding and about $1.9\times$ as many grid positions, and about 19\,\% of lesions would still touch the border because they reach the edge of the scan itself.

### 6-7.38 [medium] §6.3 'Data and labels.' (reference masks)

`06-discussion.tex:266` · GPTZero: AI · flow

> The reference masks also shrink between visits.

**Issue.** The paragraph already covers pixel spacing and label provenance. Starting the shrinkage point mid-paragraph with 'also' makes it read as another remark about spacing.

**Suggestion.**

> Start a new paragraph at "The reference masks also shrink between visits." and leave the sentence as it is.

### 6-7.39 [medium] §6.3 'Data and labels.' (reference masks)

`06-discussion.tex:269` · GPTZero: AI · clarity

> This pattern is more consistent with annotation and registration noise at the boundary than with regression, although the masks alone cannot separate the two. It is one reason why no monotonic-growth constraint was imposed.

**Issue.** For an ML readership, 'regression' could be read as statistical regression rather than regression of the lesion. 'It' in the next sentence has no clear referent.

**Suggestion.**

> This pattern is more consistent with annotation and registration noise at the boundary than with regression of the atrophy, although the masks alone cannot separate the two. The observed shrinkage is one reason why no monotonic-growth constraint was imposed.

### 6-7.40 [medium] §6.3 'Model scope.' (PINNs and grid)

`06-discussion.tex:296` · GPTZero: AI · flow, clarity

> Physics-informed neural networks were deliberately not run, because the governing equation is unknown and the residual would have to be taken on a binary mask. All operators work on the uniform $49 \times 1024$ grid.

**Issue.** After 'Model scope' the paragraph starts abruptly, with no link to the paragraph before it, and then jumps from PINNs to the grid. 'The residual' is not specified.

**Suggestion.**

> Two directions lie outside the main survey. Physics-informed neural networks were deliberately not run, because the governing equation is unknown and the equation residual would have to be taken on a binary mask. The second is mesh adaptation; all operators work on the uniform $49 \times 1024$ grid.

### 6-7.41 [low] §6.4 'Spatial pre-processing.'

`06-discussion.tex:314` · GPTZero: human · clarity

> The fixed centre crop censors growth for about a third of the cropped lesions.

**Issue.** §6.3 (L249) states the proportion per visit ('In 31.1 % of the visits ...'), but here the reference set is 'the cropped lesions'. Readers may take these for two different statistics.

**Suggestion.**

> The fixed centre crop censors growth in about a third of the visits.

### 6-7.42 [low] §6.4 'Trajectory memory.'

`06-discussion.tex:321` · GPTZero: AI · tone, clarity

> This addresses the growth-speed gap of \S\ref{sec:discussion:clinical} directly. It is also the setting in which sequence models such as recurrent networks and transformers apply.

**Issue.** The present tense presents an untested remedy as fact, out of step with the conditional 'would let it' just before. 'Apply' is vague.

**Suggestion.**

> This would address the growth-speed gap of \S\ref{sec:discussion:clinical} directly. It is also the setting in which sequence models such as recurrent networks and transformers become applicable.

### 6-7.43 [medium] §6.4 'A valid transport model.'

`06-discussion.tex:337` · GPTZero: AI · clarity

> A velocity parameterisation that is bounded by construction, starting from the energy-conserving form, would give a model that stays numerically valid over multi-year horizons and whose velocity field could be read as a direction and speed of growth.

**Issue.** The sentence is long, with a dangling participle phrase ('starting from ...') and two coordinated relative clauses.

**Suggestion.**

> A next step is a velocity parameterisation that is bounded by construction and builds on the energy-conserving form. A model with such a parameterisation would stay numerically valid over multi-year horizons, and its velocity field could be read as a direction and speed of growth.

### 6-7.44 [medium] Ch. 7 'The framework.'

`07-conclusion.tex:16` · GPTZero: AI · tone, clarity

> The forecast needs a setup that absorbs the irregularity of clinical data and treats every candidate model the same way.

**Issue.** 'Absorbs the irregularity' is a metaphor that leaves the reader to guess what is irregular.

**Suggestion.**

> The forecast needs a setup that accommodates the irregular visit schedules of clinical data and treats every candidate model in the same way.

### 6-7.45 [low] Ch. 7 'The framework.'

`07-conclusion.tex:21` · GPTZero: AI · clarity

> Held fixed, it served operators from unrelated literatures without change, and every operator with spatial context learned to predict change far above persistence.

**Issue.** 'Held fixed' and 'without change' say the same thing, and 'change' is repeated. 'Learned to predict change far above persistence' attaches the comparison to the wrong element.

**Suggestion.**

> Unchanged, it served operators from unrelated literatures, and every operator with spatial context learned to predict change and scored far above persistence.

### 6-7.46 [medium] Ch. 7 'The framework.'

`07-conclusion.tex:24` · GPTZero: AI · clarity

> This required a loss that puts weight on the lesion mask: without the weighting the canonical operator learned no change at all, and a soft-Dice term added about 0.05.

**Issue.** 'This' lacks a clear antecedent, and the colon places the soft-Dice gain under 'required', although it is an improvement rather than a requirement. 'Added about 0.05' does not say to what.

**Suggestion.**

> Learning depended on a loss that weights the lesion mask: without this weighting, the canonical operator learned no change. A soft-Dice term on the mask added about 0.05 to the change-region Dice.

### 6-7.47 [medium] Ch. 7 'The framework.'

`07-conclusion.tex:27` · GPTZero: AI · ai-tone, flow

> How time enters the update mattered less than that it enters: a higher-order Runge--Kutta step bought nothing over a single Euler step.

**Issue.** This is a near-verbatim repeat of the §6.1 aphorism, with the idiom 'bought nothing'. 'What did not matter' (L68-69) states the Runge-Kutta null again.

**Suggestion.**

> The interval length has to reach the operator, but the form in which it does so mattered little: a higher-order Runge--Kutta step gave no measurable gain over a single Euler step. (Then delete the Runge--Kutta sentence at L68-69, or keep it there and drop this one.)

### 6-7.48 [medium] Ch. 7 'The operator.'

`07-conclusion.tex:33` · GPTZero: AI · ai-tone, clarity

> The architecture class is not what decides the outcome. The three strongest operators come from three unrelated classes --- a finite-element network, a graph network and a U-Net --- and lie within about 0.04 of each other, at a change-region Dice of about 0.50 to 0.54 at one year, against zero for persistence.

**Issue.** A cleft opener ('is not what decides') is followed by an em-dash list copied verbatim from §6.1 L52, and the sentence ends in three trailing prepositional phrases.

**Suggestion.**

> The architecture class does not decide the outcome. The three strongest operators (a finite-element network, a graph network and a U-Net) come from unrelated classes. At one year they reach a change-region Dice of about 0.50 to 0.54, against zero for persistence, and lie within about 0.04 of each other.

### 6-7.49 [medium] Ch. 7 'The operator.'

`07-conclusion.tex:37` · GPTZero: AI · clarity, ai-tone

> The finite-element network is highest, above the U-Net at both seeds and slightly above the graph network; these two highest operators are the two that carry the reach and transport properties below. What separates operators are a few properties that were measured one at a time.

**Issue.** 'The two that carry the reach and transport properties below' leaves the reader to work out which operator carries which property. 'What separates operators are ...' is a pseudo-cleft with awkward agreement.

**Suggestion.**

> The finite-element network scores highest, above the U-Net at both seeds and slightly above the graph network. Of these two, the finite-element network carries the transport term and the graph network the extended reach described below. A few properties, each measured one at a time, separate the operators.

### 6-7.50 [low] Ch. 7 'The operator.' (spatial context bullet)

`07-conclusion.tex:43` · GPTZero: AI · ai-tone *(added in verification)*

> Without it, a model predicts no change at all; one ring of neighbours raises the change-region Dice from 0 to about 0.45.

**Issue.** 'At all' is used as an intensifier.

**Suggestion.**

> Without it, a model predicts no change; one ring of neighbours raises the change-region Dice from 0 to about 0.45.

### 6-7.51 [medium] Ch. 7 'The operator.' (transport bullet)

`07-conclusion.tex:51` · GPTZero: AI · clarity

> Adding a learned transport term to a Finite Element Network raised it by 0.062 over the same network without it, and by 0.072 over a parameter-matched control on the four folds on which that control trained; at a second seed the control trained on all five folds, and the margin was 0.076.

**Issue.** The first 'it' refers to the change-region Dice of the previous bullet, across a bullet boundary, and the second 'it' refers to the term. Three results are packed into one semicolon chain.

**Suggestion.**

> Adding a learned transport term to a Finite Element Network raised the change-region Dice by 0.062 over the same network without the term. Against a parameter-matched control, the margin was 0.072 on the four folds on which that control trained, and 0.076 at a second seed, where the control trained on all five folds.

### 6-7.52 [medium] Ch. 7 'The operator.' (synthesis)

`07-conclusion.tex:60` · GPTZero: AI · flow, ai-tone

> Reach and transport are two unrelated ways to correct the same deficit: a single update that cannot see as far as the disease moves between two visits. That two independent routes lead to the same level is the central architectural result of this thesis, more informative than the score of any single model.

**Issue.** The FNO sentences separate this interpretation from the bullets it interprets. The closing appositive ('more informative than the score of any single model') is an aphoristic tag.

**Suggestion.**

> Move these two sentences directly after \end{itemize}, before the two FNO sentences. If the closing tag is kept, attach it as a plain clause: "That two independent routes lead to the same level is the central architectural result of this thesis; it is more informative than the score of any single model."

### 6-7.53 [low] Ch. 7 'What did not matter.'

`07-conclusion.tex:72` · GPTZero: AI · tone, ai-tone, flow

> The validity diagnostics also limit what may be said: the canonical model is a one-step map conditioned on the length of the step, not a continuous-time model.

**Issue.** The subject is personified ('diagnostics ... limit what may be said') and the sentence ends in an 'X, not Y' antithesis. It states a limit on interpretation rather than a negative result, so it does not fit the heading.

**Suggestion.**

> The validity diagnostics also restrict how the canonical model may be described: it is a one-step map conditioned on the step length and does not behave as a continuous-time model.

### 6-7.54 [medium] Ch. 7 'Clinical position.'

`07-conclusion.tex:80` · GPTZero: AI · clarity

> On growth speed, the canonical model reaches a correlation of 0.40 with the true growth rates, against 0.61 for the model of \citet{Mai2024} on a larger cohort from the same clinic, which starts from the raw OCT volume where this thesis starts from segmented masks.

**Issue.** 'Which' could attach to the clinic, the cohort or the model, and the sentence chains four qualifications.

**Suggestion.**

> On growth speed, the canonical model reaches a correlation of 0.40 with the true growth rates, against 0.61 for the model of \citet{Mai2024}, which was evaluated on a larger cohort from the same clinic and starts from the raw OCT volume instead of segmented masks.

### 6-7.55 [low] Ch. 7 'Clinical position.'

`07-conclusion.tex:86` · GPTZero: AI · tone, flow

> The small cohort, the censoring of the fixed crop and the missing memory of past visits bound every conclusion drawn here.

**Issue.** A tricolon with a metaphorical verb ('bound'). The sentence applies to every conclusion but closes a paragraph about growth speed.

**Suggestion.**

> Every conclusion drawn here is limited by the small cohort, the censoring by the fixed crop and the lack of memory of past visits. (Consider moving it into the final paragraph, before the closing claim.)

### 6-7.56 [medium] Ch. 7 'Take-away.'

`07-conclusion.tex:89` · GPTZero: AI · ai-tone, tone

> \paragraph{Take-away.} For forecasts from longitudinal medical imaging in a low-data clinical setting, what matters is the framework around the model and the properties of the operator placed in it --- above all, whether one update can see as far as the disease moves between two visits --- rather than the choice of operator family.

**Issue.** The final sentence of the thesis combines several tells: an informal heading, a pseudo-cleft ('what matters is'), an em-dash aside with 'above all' and a closing 'rather than' antithesis. Together they read as a formulaic closer.

**Suggestion.**

> \paragraph{Implications.} For forecasts from longitudinal medical imaging in a low-data clinical setting, the framework around the model and the properties of the operator placed in it matter more than the choice of operator family. Of these properties, the most important is whether one update can see as far as the disease moves between two visits.

