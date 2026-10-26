# Full review of the thesis: verification of the S1 and S2 findings

Done on 2026-10-23 in the main session, without agents, after the workflow stopped at the weekly usage limit. It covers the 549 S1 and S2 findings of [01-findings.md](01-findings.md) that the workflow could not verify (the 240 findings of the whole-thesis passes were already verified there; see [02-shortlist.md](02-shortlist.md)).

## How it was done

1. **Mechanical pre-pass** (script `_work/prepass.py`): for every finding, the quoted text was looked up in the current source near the stated line and checked to be printed (not a comment or `\iffalse` block); the printed page was taken from the review build. All 549 quotes were found and printed (one quote was too short to check). Findings at the same place about the same text were then grouped: 549 findings form 308 groups, 132 of them with several reviewers.
2. **Judgement**: each group was read with its source lines and judged once, by one reader (this session): is it a real problem for the named reader, is it settled by a decision or the feedback log, what severity does it deserve. Facts the judgement depended on were checked in the sources (e.g. §4.3.6 on the transport mesh, §2.5.2 on the operator, the loss equation, the message equations, Table 5.2 aggregation, the code appendix references). Groups describing the same problem in different places were merged into one.
3. **Severity**: set per the severity table of `prompts/PROMPT_full_review.md`. Missing section intros or conclusions are S2 as that table says. The automatic "supervisor repeat: raise one level" was not applied again: the reviewers' S2 grades shown in 01-findings.md already include it, and where an item was downgraded to S3 here, that was a deliberate judgement.

**Limits.** One judgement per group instead of three independent lenses; S3 and S4 findings were not verified; printed pages come from the review build (current sources). A "needs:" in a note means the fix needs a fact the thesis does not contain.

## Result

| | Groups | Findings |
|---|---|---|
| Confirmed problems | 246 | 548 |
| of which S1 | 13 | 67 |
| of which S2 | 122 | 333 |
| of which downgraded to S3 | 111 | 148 |
| Dropped (settled decision) | 1 | 1 |

No group was found to misquote the text; the 61 groups merged into another are listed with the group they joined.

## S1: fix first

### G028 · S1 · §1.3 Contributions — 01-introduction.tex:171 (p. 3)

~~~text
moving mesh. These rule out directions that would otherwise appear
~~~

- **Verdict:** "These rule out directions" contradicts §6.3 ("no conclusion about mesh adaptation") and App. E scope
- **Findings:** R-0201, R-0202, R-0203, R-1923 (groups merged in: G262)
- **Suggested fix (R-0201):** "Measured nulls, each within the noise level: operators from a quarter to four times their size, a fourth-order Runge--Kutta step instead of one Euler step, and a monotonic-growth penalty. An extension with an adaptive moving mesh (Appendix~\ref{app:mm-pde}) did not improve accuracy either, because its correction branch never engaged; it is reported as one tested design, not as a verdict on mesh adaptation."
- **Status:** open

### G063 · S1 · §2.3 Neural PDE Solvers and Surrogate Architectures — 02-background.tex:681

~~~text
shared temporal origin ($t = 0$) across patients, a direct
time-dependent mapping is ill-posed.
~~~

- **Verdict:** "a direct time-dependent mapping is ill-posed" contradicts §2.4.2 (Lachinov 2024, Mai 2024 map from each eye's baseline)
- **Findings:** R-0418, R-0419, R-0420, R-0421, R-0422
- **Suggested fix (R-0418):** Replace the sentence: "Without a shared temporal origin across patients, absolute time cannot index the state. A map $M(t, u_0)$ therefore has to measure $t$ from each eye's own baseline visit, as the Neural-ODE model of \citet{Lachinov2024} does (\S\ref{sec:background:related-work}). An autoregressive update needs only the interval to the next visit." Also drop "the natural fit" in l. 679 (see the placement finding).
- **Status:** open

### G081 · S1 · §2.4.4 PDE-Based Models in Biomedicine — 02-background.tex:874 (p. 19)

~~~text
solvers trained directly on longitudinal clinical images without a known
~~~

- **Verdict:** novelty claim ("not applied to GA") contradicted by Lachinov 2024 (learned CNN vector field + RK4 on GA OCT), ImageFlowNet, Mai 2024 (§5.7); needs a delimiting property
- **Findings:** R-0513, R-0514, R-0515, R-0516
- **Suggested fix (R-0513):** "In all of these, the equation is known and the network learns to solve or invert it. Without a known equation, GA progression has been modelled with learned continuous-time dynamics \citep{Lachinov2024, Liu2025ImageFlowNet}." Then state the distinguishing property and the gap. needs: the property that separates the operators of this thesis from these models (e.g. an update that couples neighbouring points of an explicit state on the en-face grid, §2.3), checked against both sources. End with: "Learned updates of this kind, trained on longitudinal clinical data without a known equation, have, to the author's knowledge, not been applied to GA."
- **Status:** open

### G126 · S1 · §4.3.6 The Finite Element Network — 04-method.tex:1103 (p. 46)

~~~text
The T-FEN has 68\,503 parameters; its two free-form controls are described
in~\S\ref{sec:method:family:params}.
~~~

- **Verdict:** "its two free-form controls are described in §4.3.8": §4.3.8 and Table 4.3 report only the width-96 control (width-139 removed)
- **Findings:** R-1006, R-1007, R-1008, R-1009, R-1012
- **Suggested fix (R-1006):** Replace lines 1099-1104 with one closing paragraph: "Both forms were trained, and Chapter~\ref{ch:experiments} reports both (\S\ref{sec:experiments:validity:tfen}); the main comparison uses the energy-conserving form. The T-FEN has 68\,503 parameters; its free-form control is described in~\S\ref{sec:method:family:params}."
- **Status:** open

### G148 · S1 · §5.2 Main Results — 05-experiments.tex:335 (p. 54)

~~~text
The three highest arms
come from three different architecture classes and lie within about 0.04
~~~

- **Verdict:** "The three highest arms come from three different architecture classes" is false against Table 5.1 (RK4 variant of the stencil GNN is third, U-Net fourth); repeated l.450, l.503 (incl. G149)
- **Findings:** R-1144, R-1145, R-1146, R-1162 (groups merged in: G149)
- **Suggested fix (R-1144):** "The highest arms of the three leading classes, the T-FEN, the dilated-stencil graph network and the U-Net, lie within about 0.04 of each other; the Runge--Kutta variant of the graph network, third in the table, is compared with its single-step counterpart in~\S\ref{sec:experiments:ablations:time}." Adjust lines 450 and 502–503 in the same way.
- **Status:** open

### G159 · S1 · §5.4 Ablation Studies — 05-experiments.tex:633 (p. 58)

~~~text
(\S\ref{sec:experiments:protocol:stats}); one control trains on only four
folds (\S\ref{sec:experiments:ingredients:transport}).
~~~

- **Verdict:** "one control trains on only four folds (§5.4.4)": §5.4.4 now reports only five-fold comparisons (width-139 control removed; regression of AI-5b.1)
- **Findings:** R-1227, R-1228, R-1229, R-1230, R-1231, R-1232 (groups merged in: G158)
- **Suggested fix (R-1227):** Delete the clause: "All comparisons are taken fold by fold (\S\ref{sec:experiments:protocol:stats})."
- **Status:** open

### G173 · S1 · §5.4.4 An Explicit Transport Term — 05-experiments.tex:884 (p. 61)

~~~text
The transport term therefore improves the finite-element network, also
against a control of the same size, and it brings the first-year values to
~~~

- **Verdict:** "also against a control of the same size" contradicts l.837 "not parameter-matched"; no same-size control is reported (width-139 removed)
- **Findings:** R-1312, R-1313, R-1314, R-1315, R-1318, R-1319, R-1320, R-1321
- **Suggested fix (R-1312):** "The transport term therefore improves the finite-element network, also when the T-FEN has fewer parameters than its control, and it brings the first-year values to those of the dilated stencil."
- **Status:** open

### G177 · S1 · §5.4.5 Summary of the Ablation Studies — 05-experiments.tex:915 (p. 61)

~~~text
(\S\ref{sec:experiments:main-results}). That two unrelated constructions
aimed at the same limit reach about the same score is the central
~~~

- **Verdict:** "two unrelated constructions ... the central architectural result" contradicts §4.3.6, which calls the 7-column transport mesh "the finite-element counterpart of the dilated stencil" (also G009, G026)
- **Findings:** R-1336, R-1337, R-1338, R-1793, R-1794 (groups merged in: G237)
- **Suggested fix (R-1336):** Name the shared spacing and scope the claim: "Two constructions remove this limit. The dilated stencil places the neighbours of the graph network at lesion scale, so that one hop spans 21 columns (§5.4.2). The transport term of the T-FEN moves the state along a learned velocity on a mesh that connects every seventh column (§4.3.6). Each is established against its own control, and the two arms lie within about 0.017 of each other as the two highest arms of Table 5.1 (§5.2). That a graph with dilated edges and a transport term on a dilated mesh reach about the same score is consistent with the reach explanation. The transport comparison does not separate the transport mechanism from the coarser mesh on which it runs." Drop "unrelated". If a T-FEN with transport on the full-resolution mesh exists, report it here (needs: that run).
- **Status:** open

### G185 · S1 · §5.5 Differences Between Folds — 05-experiments.tex:1029 (p. 63)

~~~text
operators fall behind the local ones most when the lesion touches the
window edge, by 0.079 on the 18 such eyes against 0.022 on the other 57
~~~

- **Verdict:** border-touching eyes: 21 (§5.1.2 "edge of the imaged field"), 21 in Table C.1 caption "border of the fixed crop", 18 vs 57 in §5.5 "window edge"; one property, two definitions, two counts (incl. G274, G275, R-1177 verified)
- **Findings:** R-1387, R-1388, R-1389, R-1390, R-1391, R-2059, R-2060, R-2061, R-2062 (groups merged in: G274, G275)
- **Suggested fix (R-1387):** Use the definition and the 21/54 split of §5.1.2 ("when the lesion touches the edge of the imaged field (§5.1.2)"), or define the window edge used here and say why it gives 18 eyes instead of 21 [needs: the definition behind the 18 eyes].
- **Status:** open

### G212 · S1 · §5.7.2 Numerical Stability of the T-FEN — 05-experiments.tex:1825 (p. 72)

~~~text
the step size. Because the divergence starts after the
one-year anchor and away from the lesion, it did not affect the change-region Dice
~~~

- **Verdict:** "it did not affect the change-region Dice of the Galerkin T-FEN at one year" vs l.1846: the energy-conserving gain "lies on the lesions that touch the crop border, where the defect acted" (0.516 -> 0.544)
- **Findings:** R-1621, R-1622, R-1623, R-1624
- **Suggested fix (R-1621):** Replace lines 1825-1827 with: "In the traced rollouts the divergence typically starts after the one-year anchor, at the edge of the crop, so most of the change-region Dice at one year is unaffected. On lesions that touch the crop border, however, the energy-conserving form scores higher (see below), which suggests that the defect also lowered the one-year score there." At line 1846 hedge the attribution: "The difference lies mainly on the 21 eyes whose lesion touches the crop border, which is consistent with the location of the defect: ...". In §5.4.4 replace "so its score at the one-year anchor is valid" with "so its score at the one-year anchor is affected mainly on border-touching lesions".
- **Status:** open

### G240 · S1 · §6.1.2 The Operator — 06-discussion.tex:136 (p. 82)

~~~text
repeating these tests without changing what they show, because none of
them depends on which of the two operators fills the slot.
~~~

- **Verdict:** "none of them depends on which of the two operators fills the slot" contradicts §6.1.1 l.66-68 ("not in general") and the step-size test (canonical fails C2, T-FEN passes)
- **Findings:** R-1804, R-1805, R-1806
- **Suggested fix (R-1804):** "Second, it is the reference configuration on which the objective and time-handling tests were run (§5.6.1, §5.6.2). Replacing it would require repeating these tests on the T-FEN, and whether their results carry over is not known. The capacity study and the step-size test already include the T-FEN, and the step-size test gives the two operators different verdicts (§5.7.1)."
- **Status:** open

### G308 · S1 · Bibliography — references.bib:118 (p. 91)

~~~text
note    = {Citation key kept as Flaxman2020 to match the projection horizon used in the paper title; publication year is 2017.}
~~~

- **Verdict:** references.bib Flaxman2020 note field prints in the bibliography ("Citation key kept as ...; publication year is 2017., e1221-e1234")
- **Findings:** R-1973, R-1974, R-1975, R-1976, R-1977, R-1978
- **Suggested fix (R-1973):** Turn the note into a BibTeX comment: delete the note field, or rename it (e.g. to comment), which biblatex does not print.
- **Status:** open

### G299 · S1 · §E.4 Result — 91-appendix.tex:1069

~~~text
Single branch & $0.4515 \pm 0.0429$ & $75\,339$ & 75\,s \\
~~~

- **Verdict:** Table E.3 / §E.2.2: "the k-nearest-neighbour graph network" with 75 339 params, 0.4515 +- 0.0429, 75 s vs Tables 4.3/5.1: 67 147, 0.4623 +- 0.0361, 76 s; the difference (an earlier configuration) is not stated; 0.4515 equals the one-hop floor's mean
- **Findings:** R-2307, R-2308, R-2309, R-2310
- **Suggested fix (R-2307):** State the difference once, at the first mention in §E.2, and drop the two repeats: 'All five-fold runs of the extension use an earlier configuration of the $k$-nearest-neighbour graph network with 75 339 parameters (needs: what differs from the $k$-NN arm of Table~\ref{tab:experiments:arms}). Their scores are therefore compared only with each other, not with Table~\ref{tab:experiments:arms}.' In the Table E.3 caption, replace 'All arms use the k-nearest-neighbour graph network, not the dilated stencil' with 'All arms use the earlier $k$-NN configuration of §E.2'.
- **Status:** open

## S2

### G307 · S2 · Title page — main-thesis.tex:190 (p. i)

~~~text
\title{Neural PDE Solvers for Geographic Atrophy Progression Prediction from Longitudinal OCT Imaging}
~~~

- **Verdict:** title uses PDE/OCT abbreviations and a noun stack, and names "neural PDE solvers", which the abstract never mentions; needs: final title agreed with the supervisor (open TODO)
- **Findings:** R-0001
- **Suggested fix (R-0001):** Spell out the abbreviations, break the noun stack and align the title with the abstract, e.g. "Forecasting the Progression of Geographic Atrophy from Longitudinal Optical Coherence Tomography: Framework and Operators". Needs: the final title agreed with the supervisor.
- **Recurs:** AI-S21
- **Status:** open

### G001 · S2 · Abstract — 00-abstract.tex:58 (p. ii)

~~~text
Geographic Atrophy (GA) is the advanced form of age-related macular
~~~

- **Verdict:** §1.1 says GA is one of two late forms; "the advanced form" is wrong (EN only)
- **Findings:** R-0009
- **Suggested fix (R-0009):** Geographic Atrophy (GA) is the atrophic late form of age-related macular degeneration, manifested as a gradual and irreversible loss of retinal tissue. (Alternatively "an advanced form"; either matches §1.1 and "eine Spätform".)
- **Status:** open

### G002 · S2 · Abstract — 00-abstract.tex:65

~~~text
what a forecast from longitudinal optical coherence tomography (OCT)
requires: a framework around the model, and an operator inside it that maps
~~~

- **Verdict:** "determines what a forecast requires: a framework and an operator" reads as the trivial answer, not the question
- **Findings:** R-0013
- **Suggested fix (R-0013):** "This thesis studies GA progression from the perspective of computational modelling and asks two questions about a forecast from longitudinal optical coherence tomography (OCT): what kind of framework it requires around the model, and what kind of operator, the learned map from one visit to the next, that framework requires." (German l. 129-132 likewise: "... und untersucht, welche Art von Framework ... und welche Art von Operator ... erforderlich ist.")
- **Status:** open

### G003 · S2 · Abstract — 00-abstract.tex:70 (p. ii)

~~~text
models for GA. The comparison identifies the property that separates them:
whether one update can see as far as the lesion front moves between two
~~~

- **Verdict:** "identifies the property that separates them" is unscoped and the "What separates" pattern; l. 93 already scopes it
- **Findings:** R-0017, R-0018
- **Suggested fix (R-0017):** "Among operators with spatial context, the comparison shows that the score depends mainly on whether one update reaches as far as the lesion front moves between two visits." (German, l. 136-138, accordingly: "Unter den Operatoren mit räumlichem Kontext hängt das Ergebnis vor allem davon ab, ob ein einzelner Vorhersageschritt so weit reicht, wie sich der Läsionsrand zwischen zwei Untersuchungen verschiebt.")
- **Recurs:** SV-7.3
- **Status:** open

### G007 · S2 · Abstract — 00-abstract.tex:94

~~~text
is reach. On the anisotropic grid, B-scans lie 121\,\textmu{}m
apart, pixels along a B-scan only 5.7\,\textmu{}m. In a graph
~~~

- **Verdict:** B-scan undefined in the abstract while the reach argument rests on it; much spacing detail (SV-A5)
- **Findings:** R-0040, R-0041
- **Suggested fix (R-0040):** "Among operators with spatial context, the main difference is reach. Because the OCT grid is about 21 times coarser between its cross-sectional scans than along them, a neighbour graph built from pixel indices reaches only about 11 µm along a scan per update, whereas the lesion front typically advances by about 70 µm between visits. A dilated stencil that reaches about 120 µm in both directions raises the change-region Dice by 0.064 at an identical parameter count, on all five folds." German l. 168-178 accordingly.
- **Recurs:** SV-A5 (supervisor repeat: raised one level)
- **Status:** open

### G009 · S2 · Abstract (English) — 00-abstract.tex:100 (p. ii)

~~~text
0.064 at an identical parameter count, on all five folds. The transport term
closes the same gap by another mechanism (+0.062 over the network without
~~~

- **Verdict:** verified: §4.3.6 l.1022-1024 calls the transport mesh (every 7th column) the counterpart of the dilated stencil, so "another mechanism" is not separated; +0.062 control has half the parameters; "the same gap" has no antecedent
- **Findings:** R-0048, R-0049, R-0051
- **Suggested fix (R-0048):** Reword to what the comparison shows: "A learned transport term, which the Finite Element Network evaluates on a mesh that links every seventh column like the stencil, raises its score by a similar amount (+0.062 over the same network without it)." Before the term is called an independent route (here, and in §1.3, §5.4.5, §6.1.2 and Chapter 7), the thesis needs either a T-FEN run with the transport term on the full-resolution mesh or a statement that the mesh spacing was not varied.
- **Status:** open

### G010 · S2 · Abstract — 00-abstract.tex:102 (p. ii)

~~~text
it). In this cohort, the models locate new atrophy better than they predict
its speed: their Dice on the newly atrophic region alone is about 0.5 to
~~~

- **Verdict:** closing compares Dice and r, which are on different scales
- **Findings:** R-0053
- **Suggested fix (R-0053):** State the two results without the unsupported comparison: "In this cohort, the Dice of the strongest operators on the newly atrophic region alone lies between about 0.5 and 0.65 in each year of follow-up, and the predicted and measured growth rates of the 75 eyes correlate moderately (r = 0.40)." If the comparative claim is to stay, needs: a reference value for each measure in the abstract (see reconsider). German l. 179-184 accordingly.
- **Recurs:** AI-1.10
- **Status:** open

### G013 · S2 · §1.1 Clinical Motivation — 01-introduction.tex:24

~~~text
causes a marked loss of visual acuity once the fovea, the centre of the
~~~

- **Verdict:** visual acuity used at l.24, glossed only at l.61 (M2)
- **Findings:** R-0099, R-0100, R-0101, R-0102, R-0103
- **Suggested fix (R-0099):** Line 24: "Once the fovea, the centre of the macula, is involved, GA causes a marked loss of visual acuity, the sharpness of vision \citep{Vallino2024}." Line 61: "Best-corrected visual acuity, measured with spectacles, did not differ ..."
- **Recurs:** M2 (supervisor repeat: raised one level)
- **Status:** open

### G014 · S2 · §1.2 Aim of the Thesis — 01-introduction.tex:94

~~~text
task on the en-face (frontal, two-dimensional) projection of OCT volumes.
~~~

- **Verdict:** verified: "en-face projection of OCT volumes" vs §2.1.2 l.266 "No projection is computed"; "traced" without agent
- **Findings:** R-0136, R-0138
- **Suggested fix (R-0136):** Rewrite lines 93-98: "Predicting GA progression is framed as a spatiotemporal forecasting task on the en-face grid of the OCT scan, the retina seen from the front. For each visit, the state consists of the lesion outline, annotated by graders on fundus autofluorescence and registered to this grid, and the depths of ten retinal layer boundaries segmented in the OCT volume (Chapter~\ref{ch:data}); the models receive these maps, not the OCT images."
- **Recurs:** AI-FF2a
- **Status:** open

### G015 · S2 · §1.2 Aim of the Thesis — 01-introduction.tex:100 (p. 2)

~~~text
This differs from earlier work on AMD, which predicts or characterises the conversion of an eye
~~~

- **Verdict:** §1.2 contrasts only with conversion work; spatial GA forecasts (Gigon, Lachinov, Mai) exist (§2.4.2)
- **Findings:** R-0143, R-0145
- **Suggested fix (R-0143):** Rewrite lines 100-104: "Earlier learning-based work on AMD predicts the conversion of an eye to a later stage \citep{SchmidtErfurth2018, Vogl2021} or a single growth rate per eye. More recent models forecast the lesion itself, among them \citet{Mai2024} on the cohort used here, from raw OCT (Section~\ref{sec:background:related-work}). This thesis also forecasts a complete lesion map, from segmented masks and layer surfaces, and compares several operators for this task inside one framework." Drop the separate pointer sentence at line 118, or keep it short.
- **Status:** open

### G017 · S2 · §1.2 Aim of the Thesis — 01-introduction.tex:107 (p. 2)

~~~text
Such a forecast requires a learned map from the state at one visit to the state at a later one. In this thesis, this map is called the operator.
~~~

- **Verdict:** verified: §2.5.2 l.1041 calls f_theta the operator; §1.2 calls the state-to-state map the operator
- **Findings:** R-0155, R-0156
- **Suggested fix (R-0155):** Rewrite: "Such a forecast is made here by a learned update that maps the state at one visit to the state at a later one. In this thesis, the learned part of this update, which is added to the current state after scaling by the interval, is called the operator (\S\ref{sec:background:problem})." Also align the §2.5.2 sentence "a map from the state at one time to the state at a later time" with its own equation.
- **Recurs:** SV-X2
- **Status:** open

### G023 · S2 · §1.3 Contributions — 01-introduction.tex:161 (p. 3)

~~~text
\item A controlled comparison of operators of several architectures for
    forecasting GA from longitudinal OCT, at matched parameter counts and
~~~

- **Verdict:** contribution bullets give no result (M5); objective result missing (G021); scale and caveats missing (G024)
- **Findings:** R-0178, R-0185, R-0186, R-0189 (groups merged in: G021, G024)
- **Suggested fix (R-0185):** First bullet, add after the first sentence: "Inside it, every operator with spatial context learned to predict change, and the objective decided whether any change was learned: trained with a plain mean squared error, the canonical operator learned none." Second bullet: "A controlled comparison of operators from several architecture families for forecasting GA from longitudinal OCT, at matched parameter counts and with five-fold cross-validation. The three strongest operators, a finite-element network, a graph network and a U-Net, come from unrelated families and score within about 0.04 of each other at one year; the comparison therefore makes the properties that separate operators measurable one at a time."
- **Recurs:** M5 (supervisor repeat: raised one level)
- **Status:** open

### G025 · S2 · §1.3 Contributions — 01-introduction.tex:164 (p. 3)

~~~text
\item The identification of physical reach at the scale of the lesion
    front and an explicit transport term as two independent routes to the
~~~

- **Verdict:** physical reach, transport term, lesion front, "the same deficit" undefined in Ch. 1 (M2, AI-1.41)
- **Findings:** R-0191, R-0192
- **Suggested fix (R-0191):** Gloss each term in a few words, e.g. "a pushforward curriculum (training partly on the model's own earlier predictions, with the unroll depth measured in elapsed days)", "physical reach (how far one update of the operator sees)", "an explicit transport term (a learned velocity that moves the state)", "a fourth-order Runge--Kutta step instead of a single Euler step".
- **Recurs:** M2 (supervisor repeat: raised one level)
- **Status:** open

### G026 · S2 · §1.3 Contributions — 01-introduction.tex:165 (p. 3)

~~~text
front and an explicit transport term as two independent routes to the same deficit: a single update that cannot see as far as the lesion front
~~~

- **Verdict:** "two independent routes": §4.3.6 transport mesh links every 7th column like the stencil, so not independent (same as G009)
- **Findings:** R-0193
- **Suggested fix (R-0193):** Drop "independent" and state the confound: "... and an explicit transport term, which in the T-FEN runs on a mesh with the seven-column spacing of the dilated stencil (\S\ref{sec:method:family:fen}), as two constructions that address the same limit: ...". Either qualify "a single update" for the FEN arms ("one evaluation of the operator"), or needs: a T-FEN whose transport term runs on the full-resolution mesh, to separate mechanism from reach.
- **Status:** open

### G027 · S2 · §1.3 Contributions — 01-introduction.tex:167 (p. 3)

~~~text
front moves between two visits. This identifies the property an operator for forecasting GA has to provide.
~~~

- **Verdict:** "the property an operator ... has to provide" is a necessity claim; §5.4.5 says consistent with, does not prove
- **Findings:** R-0196, R-0197
- **Suggested fix (R-0196):** Replace the last sentence with: "Both constructions raise the change-region Dice by about 0.06 against their own controls, and the two arms built in these ways score highest; this is consistent with, but does not prove, the explanation that one update must reach as far as the lesion front moves between two visits."
- **Status:** open

### G030 · S2 · §2.1 Medical Background — 02-background.tex:20 (p. vi)

~~~text
\section{Medical Background}
~~~

- **Verdict:** §2.1 has no intro; its roadmap sits at the end of §2.1.1 and §2.1 has no closing (E1)
- **Findings:** R-0215, R-0216, R-0217
- **Suggested fix (R-0215):** Move l. 118-125 to directly below \label{sec:background:ga-oct} and rewrite them as the section introduction: 'This section introduces the medical terms on which the data and the forecast of this thesis rely. \S\ref{sec:background:ga-oct:anatomy} describes the anatomy of the eye and of the layered retina, \S\ref{sec:background:ga-oct:oct} how the retina is imaged with OCT, SLO and FAF and how an OCT volume is summarised as en-face maps, and \S\ref{sec:background:ga-oct:disease} what GA is and how it appears on these images.' After l. 372, add a closing paragraph: 'In summary, GA is a localised loss of the outer retina and the choriocapillaris that is visible on en-face OCT and FAF images, and the layer geometry at its margin carries information on its growth \citep{Chu2022}. Chapter~\ref{ch:data} describes how the lesion and the layers enter the data of this thesis.'
- **Recurs:** E1
- **Status:** open

### G031 · S2 · §2.1.1 Eye Anatomy — 02-background.tex:83 (p. 5)

~~~text
roughly five to six millimetres and is the only part of the retina that GA affects clinically (\S\ref{sec:background:ga-oct:disease}). The
~~~

- **Verdict:** "only part of the retina that GA affects clinically" + "therefore" window; §3.3 census shows lesions beyond the window
- **Findings:** R-0228, R-0229, R-0230
- **Suggested fix (R-0228):** Rewrite lines 82-87: "The macula has a diameter of roughly five to six millimetres and is where GA develops (\S\ref{sec:background:ga-oct:disease}). The OCT scans of the cohort cover the macula (\S\ref{sec:background:ga-oct:oct}), but a lesion can extend beyond the modelling window used in this thesis (\S\ref{sec:data:spatial})."
- **Status:** open

### G033 · S2 · §2.1.1 Eye Anatomy — 02-background.tex:110

~~~text
retinal pigment epithelium (RPE), and Bruch's membrane;
~~~

- **Verdict:** Bruch's membrane never explained; RPE role late; state tensor before §3.2 (M2)
- **Findings:** R-0239
- **Suggested fix (R-0239):** After the layer list (l. 110-111), add: 'The RPE is a single layer of pigmented cells that supports the photoreceptors, and Bruch's membrane is the thin sheet that separates it from the choriocapillaris.' At l. 187, write 'The Medical University of Vienna (MUW) cohort uses ...'. At l. 347-350, write 'In the data of this thesis, the GA lesion is a binary mask (\S\ref{sec:background:ga-oct:state-rep}); iRORA is not a separate label.' Replace 'slab' with 'an en-face image of a depth range below Bruch's membrane' at its first use. Gloss 'coronal' as 'parallel to the retinal surface'. Drop '(in spectral-domain OCT)'. Add the excitation light to the FAF definition (needs: the excitation wavelengths of blue-light and near-infrared FAF from the cited sources).
- **Recurs:** M2 (supervisor repeat: raised one level)
- **Status:** open

### G037 · S2 · §2.1.2 Retinal Imaging — 02-background.tex:188 (p. 7)

~~~text
acquisition protocol that produces volumes with a lateral footprint of approximately $6 \times 6$\,mm.
~~~

- **Verdict:** "footprint approximately 6x6 mm": §3.1 native grids 38-66 x 961-1719 at fixed spacing = 4.6-8.0 x 5.5-9.8 mm; 6x6 is the crop of §3.3
- **Findings:** R-0259, R-0260, R-0261
- **Suggested fix (R-0259):** Line 187-189: "The MUW volumes are macular scans whose lateral extent differs between eyes (\S\ref{sec:data:dataset}); all of them are brought to a common window of about $6 \times 6$\,mm (\S\ref{sec:data:spatial})." Fig. 2.1 caption: "The dashed square is the modelling window of about $6 \times 6$\,mm used in this thesis (\S\ref{sec:data:spatial})." Fig. 2.2 caption: "The modelling window of this thesis covers about $6 \times 6$\,mm (\S\ref{sec:data:spatial})." Line 86: point to \S\ref{sec:data:spatial} instead of the muw label. Needs: a source in §3.1 if "fovea-centred" is to stay.
- **Status:** open

### G038 · S2 · §2.1.2 Retinal Imaging (Figure 2.3) — 02-background.tex:220

~~~text
\includegraphics[width=\textwidth]{images/fig_bg_ga_faf.png}
~~~

- **Verdict:** no ethics / data-use / pseudonymisation statement anywhere; needs: approval reference from the data provider
- **Findings:** R-0268, R-2011, R-2155 (groups merged in: G271, G283)
- **Suggested fix (R-0268):** Add one sentence to §3.1 (after the cohort description) stating under which ethics approval and data-use agreement the MUW data were provided and that they were pseudonymised; needs: the approval reference or the statement used by the data provider. No change to the figure itself.
- **Status:** open

### G039 · S2 · §2.1.2 Retinal Imaging — 02-background.tex:240 (p. 9)

~~~text
near-infrared FAF measurements in a small cohort. The thesis therefore works on the OCT en-face grid.
~~~

- **Verdict:** OCT advantages then "therefore works on the OCT grid", while the mask was outlined on FAF (§3.1)
- **Findings:** R-0273, R-0276
- **Suggested fix (R-0273):** Replace the last sentence of the paragraph with: "In this thesis, the lesion mask and the layer maps are both given on the OCT en-face grid (\S\ref{sec:data:dataset} describes how the mask was annotated)." At line 347-350, add the same pointer: "Channel~0 of the state tensor used in this thesis marks the GA lesion as a binary mask (\S\ref{sec:background:ga-oct:state-rep}; its annotation is described in \S\ref{sec:data:dataset}); iRORA is not represented as a separate label."
- **Recurs:** AI-S5
- **Status:** open

### G040 · S2 · §2.1.2 Retinal Imaging — 02-background.tex:243 (p. 9)

~~~text
The lesion itself is
visible on the B-scan as a region of outer-retinal layer dropout with
~~~

- **Verdict:** lesion's OCT appearance described before §2.1.3 introduces GA; hypertransmission and "slab" used before explained (incl. G041)
- **Findings:** R-0278, R-0280, R-0281, R-0283 (groups merged in: G041)
- **Suggested fix (R-0278):** Keep l. 242 ('A single OCT volume shows both the lesion and the retinal layers around it.') and replace l. 243-249 with 'Section~\ref{sec:background:ga-oct:disease} describes how the lesion appears on it.' If the en-face view of the choroid should stay, add it as one sentence to signature (ii) in §2.1.3, keeping its citation \citep{Chu2022,Vallino2024}.
- **Recurs:** SV-2.3 (supervisor repeat: raised one level)
- **Status:** open

### G042 · S2 · §2.1.2 Retinal Imaging — 02-background.tex:255 (p. 9)

~~~text
The full OCT volume of a GA eye is too large and too redundant to be
modelled at native voxel resolution.
~~~

- **Verdict:** "too large ... to be modelled at native resolution" contradicted by Mai 2024 / Lachinov 2024 (§2.4); real reason is the data format
- **Findings:** R-0285, R-0286, R-0287, R-0288
- **Suggested fix (R-0285):** Replace l. 255-256 with: 'Models of GA progression have been trained on full OCT volumes \citep{Mai2024,Lachinov2024}, while the clinical literature on GA area and growth works with an \emph{en-face} image: a two-dimensional map of the retina seen from the front, ...' (keep the rest of the sentence). Replace l. 275-277 with 'On the en-face grid, the forecast operates on two-dimensional maps instead of a three-dimensional volume.' or delete it.
- **Status:** open

### G044 · S2 · §2.1.3 Geographic Atrophy — 02-background.tex:314 (p. 10)

~~~text
disease in which three tightly coupled \emph{outer}-retinal layers die
together in a localised patch of the macula: the retinal pigment
~~~

- **Verdict:** choriocapillaris called an outer-retinal layer; §2.1.1 places it in the choroid; "outer segments" vs photoreceptors (ledger C039 PARTLY)
- **Findings:** R-0294, R-0295, R-0297
- **Suggested fix (R-0294):** Rewrite l. 313-318 as: 'Geographic atrophy is the disease in which three tightly coupled layers die together in a localised patch of the macula: the retinal pigment epithelium (RPE), the photoreceptor outer segments just above it, and the choriocapillaris, the innermost capillary bed of the choroid immediately below it \citep{Boopathiraj2024,Boyer2017}.' At l. 113, write 'that GA destroys the outer retina together with the choriocapillaris beneath it'.
- **Status:** open

### G048 · S2 · §2.1.3 Geographic Atrophy — 02-background.tex:352 (p. 11)

~~~text
An established GA lesion is identified on a B-scan by three principal direct OCT signatures \citep{Boopathiraj2024,Yehoshua2011,Vallino2024}.
~~~

- **Verdict:** "three principal signatures identify" vs l.370 "the third is a predictive biomarker" (ledger C043 PARTLY)
- **Findings:** R-0318, R-0321
- **Suggested fix (R-0318):** "An established GA lesion is identified on a B-scan by two direct OCT signatures, which correspond to the CAM criteria above \citep{Boopathiraj2024,Yehoshua2011,Vallino2024}. \emph{(i)} ... \emph{(ii)} ... A third feature lies outside the lesion: \emph{(iii)} RPE--Bruch's-membrane (BM) thickening ... \citep{Chu2022}." Line 370: "The two signatures delineate the lesion itself; the third feature is a predictive biomarker located at the lesion boundary and motivates ...". Fig. 2.4 caption (b): "marked with the two OCT signatures and the margin feature described in the text".
- **Status:** open

### G051 · S2 · §2.2.2 Stepping in time — 02-background.tex:522 (p. 14)

~~~text
Spatial stencil and time integrator together define an update operator
~~~

- **Verdict:** "update operator" names A in §2.2.2 and f_theta in §4.1 (l.18, 25); §2.5.2 calls f_theta the operator (SV-X2)
- **Findings:** R-0365
- **Suggested fix (R-0365):** Keep "operator" for f_θ only. At l. 522: "Spatial stencil and time integrator together define one update step,"; at l. 661: "solvers learn the update $\mathcal{A}$ of~\eqref{eq:bg:update-operator}". In 04-method.tex:18 and :25 write "the operator" instead of "the update operator". In §2.5.2 (l. 1041-1042) define the operator as the learned map that gives the change of the state over an interval, not as a map to the later state.
- **Recurs:** SV-X2
- **Status:** open

### G052 · S2 · §2.2.2 Stepping in time — 02-background.tex:533 (p. 14)

~~~text
\emph{consistency}: as the step shrinks to zero, the update must
reproduce the exact solution,
~~~

- **Verdict:** consistency defined without /Delta t is satisfied by any update with A(0,u)=u (persistence too), yet used as basis of a convergence argument (l.642, 712); incl. G053, G056
- **Findings:** R-0369, R-0370, R-0393 (groups merged in: G053, G056)
- **Suggested fix (R-0369):** Give the standard definition and drop the automatic reading. At l. 533-536: "The first is \emph{consistency}: the error of one step must vanish faster than the step itself, $\lim_{\Delta t \to 0} \lVert \mathcal{A}(\Delta t, u(t)) - u(t+\Delta t) \rVert / \Delta t = 0$; for an update in residual form this requires the rate to approach the right-hand side $F$." Keep \citep{Brandstetter2022}, or cite the ODE textbook already used for the Euler step. At l. 538-539: "it returns the current state at $\Delta t = 0$ for any bounded rate." At l. 642-643: "…in the residual form of~\eqref{eq:bg:euler}, so the update reduces to the current state as the step shrinks." At l. 712: "Together with consistency (\S\ref{sec:background:pde-solvers:time}), zero stability…".
- **Recurs:** SV-4.3
- **Status:** open

### G054 · S2 · §2.3 Neural PDE Solvers and Surrogate Architectures — 02-background.tex:606 (p. vi)

~~~text
\section{Neural PDE Solvers and Surrogate Architectures}
~~~

- **Verdict:** §2.3 has no intro paragraph for 13 paragraphs on many topics (E1); incl. G055
- **Findings:** R-0381, R-0382 (groups merged in: G055)
- **Suggested fix (R-0381):** Insert before l. 614: "This section introduces the learned counterparts of these mechanisms. It describes how learned solvers keep or replace parts of the classical computation, the two ways of using them (neural operators and autoregressive solvers), the error accumulation of autoregressive rollouts and the training remedies against it, and the architecture families that Chapter~\ref{ch:experiments} compares. It closes with the four structural properties by which these families differ."
- **Recurs:** E1
- **Status:** open

### G059 · S2 · §2.3 Neural PDE Solvers and Surrogate Architectures — 02-background.tex:659 (p. 16)

~~~text
$M(t, u_0) = u(t)$, and so predict the solution at any time directly
~~~

- **Verdict:** neural operators presented as direct maps M(t,u0), but the FNO is used as a one-step update in this thesis and §2.3/§4.3.4 never say so; incl. G067
- **Findings:** R-0403, R-0404, R-0441 (groups merged in: G067)
- **Suggested fix (R-0403):** Rewrite l. 655-662: "Learned solvers also differ in how they use time. Following \citet{Brandstetter2022}, a direct approach learns a map $M: [0, T] \times \mathcal{F} \to \mathcal{F}$ with $M(t, u_0) = u(t)$ and predicts the solution at any time from the initial condition. By contrast, autoregressive solvers learn the update operator $\mathcal{A}$ of~\eqref{eq:bg:update-operator} and apply it repeatedly to unroll a trajectory. The two framings concern the use of a network, not its architecture: a neural operator such as the FNO can serve as a direct map or, applied recurrently, as an update operator \citep{Li2021}, which is how it is used in this thesis (\S\ref{sec:method:family:dense})." Restrict the limitation in l. 674-677 to the direct framing.
- **Status:** open

### G065 · S2 · §2.3 Neural PDE Solvers and Surrogate Architectures — 02-background.tex:696

~~~text
The first is temporal bundling: the model predicts $K$ future steps in
~~~

- **Verdict:** K = bundle size here and in §4.3.2, K = last visit index in §2.5.2; u^k vs u_k (SV-4.4)
- **Findings:** R-0427, R-0428, R-0581 (groups merged in: G086)
- **Suggested fix (R-0427):** Give the bundle size its own symbol, e.g. $K_{\mathrm{b}}$, here and in §4.3.2 (l. 554-581, l. 655, Table 4.x row), or rename the last-visit index in §2.5.2. In §2.5.2, add one clause: "the visit index, a superscript in \S\ref{sec:background:pde-solvers}, is written as a subscript because no cell index is needed".
- **Recurs:** SV-4.4 (supervisor repeat: raised one level)
- **Status:** open

### G068 · S2 · §2.3 Neural PDE Solvers and Surrogate Architectures — 02-background.tex:744 (p. 17)

~~~text
The architecture families differ mainly in four structural properties:
~~~

- **Verdict:** §2.3 lists four distinguishing properties, §2.5.1 l.987 a different three
- **Findings:** R-0450
- **Suggested fix (R-0450):** In §2.3, write: "This thesis compares the families along four structural properties: whether the operator has spatial context at all, how far that context physically reaches, whether it combines global and local information, and whether it carries an explicit transport term." In §2.5.1, l. 986-989, replace the three-item list with a pointer: "These solvers differ in the built-in assumptions named in \S\ref{sec:background:neural-pde}."
- **Status:** open

### G070 · S2 · §2.4 Related Work — 02-background.tex:764 (p. 18)

~~~text
Related work is discussed in four groups.
~~~

- **Verdict:** §2.4 opens with a roadmap only and has no closing gap statement (E1); incl. R-0456 of G069
- **Findings:** R-0457, R-0458
- **Suggested fix (R-0457):** Replace l. 764-770 with: "This section places the thesis among four groups of prior work and identifies what they leave open. Models of AMD and GA progression on OCT either predict a risk or a rate for each eye (Section~\ref{sec:background:related-work:rate}) or predict where the lesion will grow (\S\ref{sec:background:related-work:spatial}); \S\ref{sec:background:related-work:irregular} covers forecasts from irregularly sampled longitudinal data in general and \S\ref{sec:background:related-work:pde} PDE-based models in biomedicine." Delete l. 775-777. After §2.4.4, add a short closing paragraph with the gap statement. needs: a gap statement checked against the cited studies (e.g. that no study compares operators of several architecture classes for GA within one fixed framework, the second contribution of §1.3).
- **Recurs:** E1
- **Status:** open

### G071 · S2 · §2.4.1 Predicting the Risk and Rate of Progression — 02-background.tex:778 (p. 18)

~~~text
\citet{SchmidtErfurth2018} reported on the prediction of individual
~~~

- **Verdict:** §2.4.1 first paragraph lists works without input, target or result (SV-2.7)
- **Findings:** R-0459, R-0460
- **Suggested fix (R-0459):** For Schmidt-Erfurth et al. (2018) and Bogunović et al. (2017), state the input, the predicted quantity and the reported performance (needs: from the sources). Move Vogl et al. (2021) to the layer-biomarker sentence of §2.5.1 (l. 905-908), or describe it as the analysis it is. Drop the Vallino sentence or give its specific content.
- **Recurs:** SV-2.7 (supervisor repeat: raised one level)
- **Status:** open

### G073 · S2 · §2.4.2 Spatial Forecasting of GA Lesions — 02-background.tex:809 (p. 18)

~~~text
models that forecast the lesion itself. \citet{Gigon2021} predicted the progression of RORA from OCT
~~~

- **Verdict:** RORA, MRI, SDE, FET-PET never expanded; RORA not defined though §5.7 compares with Gigon; growth region used before §5.1.2 (incl. G074)
- **Findings:** R-0480, R-0481, R-0484, R-1660, R-1661, R-1669 (groups merged in: G074, G218, G220)
- **Suggested fix (R-0480):** "\citet{Gigon2021} predicted the progression of RPE and outer retinal atrophy (RORA; cf. cRORA, \S\ref{sec:background:ga-oct:disease}) from OCT ...". Write 'magnetic resonance imaging (MRI)', 'stochastic differential equation (SDE)' and 'FET positron emission tomography (FET-PET)' at first use. Add RORA, MRI, SDE, PET and CFL (and cRORA, iRORA) to acronyms.tex.
- **Recurs:** M2 (supervisor repeat: raised one level)
- **Status:** open

### G075 · S2 · §2.4.2 Spatial Forecasting of GA Lesions — 02-background.tex:815

~~~text
\citet{Lachinov2024} encode each pixel of a baseline scan as a feature
~~~

- **Verdict:** verified: §5.7 says Mai et al. use a Neural ODE integrated by RK4; §2.4.2 does not, and gives Lachinov no result
- **Findings:** R-0485, R-0486
- **Suggested fix (R-0485):** "\citet{Lachinov2024} encoded each pixel ... and evolved these vectors ..." needs: the result they report on GA. In the Mai paragraph: "... who predicted individual GA progression from a single baseline OCT volume with a Neural ODE integrated by RK4, on the MUW GA cohort (184 eyes of 100 patients)." needs: whether this is the model of Lachinov et al. (2024). Replace l. 819-821 with a statement of the difference: "Unlike these models, the operators of this thesis advance the explicit eleven-channel state of \S\ref{sec:background:problem} and are exchanged within one framework; the Runge--Kutta-integrated operators (\S\ref{sec:method:family:rk}) are closest to the continuous-time formulation."
- **Recurs:** SV-2.7 (supervisor repeat: raised one level)
- **Status:** open

### G079 · S2 · §2.4.3 Forecasting from Irregularly Sampled Longitudinal Data — 02-background.tex:856 (p. 19)

~~~text
on it; the operators of this thesis take the interval as an input to a
~~~

- **Verdict:** "the operators ... take the interval as an input to a single residual step" is false for the RK-wrapped operators (Delta t entry zeroed, sub-steps; §4.3.7) and clashes with l.819-821
- **Findings:** R-0507, R-0508
- **Suggested fix (R-0507):** "These models treat time continuously or condition on it. The default update of this thesis takes the interval as an input to a single residual step (\S\ref{sec:background:problem}). The Runge--Kutta wrapper of \S\ref{sec:method:family:rk} instead integrates an operator without a $\Delta t$ input over the interval, which is closer to these continuous-time models."
- **Status:** open

### G083 · S2 · §2.5.1 Choice of the Modelling Approach — 02-background.tex:941

~~~text
exterior is healthy; both are quasi-static, and all dynamics are
~~~

- **Verdict:** "exterior is healthy ... all dynamics concentrated at the active boundary" contradicted by §5.4 (new atrophy >0.24 mm away), §2.1.3 rim biomarker
- **Findings:** R-0543, R-0544, R-0546
- **Suggested fix (R-0543):** "The interior of the lesion is already atrophic, and the retina further away changes little. Most of the change between visits occurs at the lesion boundary, although new atrophy can also appear at some distance from it (\S\ref{sec:experiments:folds}). Such behaviour is characteristic of ..."
- **Status:** open

### G084 · S2 · §2.5.1 Choice of the Modelling Approach — 02-background.tex:952 (p. 21)

~~~text
forward operator that maps the present state to the future state is therefore \emph{local}, but its reach must match the distance the front
~~~

- **Verdict:** "operator is therefore local ... reach must match" vs l.1003-1005 "not assumed here"
- **Findings:** R-0553, R-0556
- **Suggested fix (R-0553):** "The forward operator that maps the present state to the future state is therefore expected to act mainly locally, and its reach would have to cover the distance the front moves between two visits, which differs between directions." Drop or reword the last sentence ("Classical solvers build such properties in explicitly through the size and shape of their stencils") so that it does not tie the stencil shape to the fovea-periphery anisotropy.
- **Recurs:** AI-S16
- **Status:** open

### G087 · S2 · §2.5.2 Problem Statement — 02-background.tex:1041

~~~text
thesis, $f_\theta$ is called the \emph{operator}. The term is used in its
~~~

- **Verdict:** the defining place: f_theta called the operator and defined as a state-to-state map, contradicting Eq. 2.8 (also G017, G051)
- **Findings:** R-0592, R-0594, R-0595, R-0596, R-0777, R-0903 (groups merged in: G102, G114)
- **Suggested fix (R-0592):** Rewrite 1040-1043: "where $f_\theta$ is a learned map with parameters $\theta$; multiplied by $\Delta t_k$, its output is the predicted change of the state. Throughout this thesis, $f_\theta$ is called the \emph{operator}. The term is used in a general sense: through Equation~\eqref{eq:bg:problem-update}, $f_\theta$ defines a learned map from the state at one visit to the state at the next. It is not used in the narrower sense of the neural-operator literature ..." In §1.2 write "Its learned component is called the operator." At l. 952 replace "The forward operator that maps the present state to the future state" with "The map from the present state to the future state".
- **Recurs:** SV-X2
- **Status:** open

### G088 · S2 · Ch. 3 Data and Preprocessing — 03-data.tex:4 (p. vi)

~~~text
\chapter{Data and Preprocessing}
~~~

- **Verdict:** Ch. 3 has no closing / hand-over to Ch. 4 (E1; severity table: section without conclusion = S2)
- **Findings:** R-0612
- **Suggested fix (R-0612):** Add a closing paragraph after the test-set paragraph: "In summary, the models receive an eleven-channel state on a $49 \times 1024$ grid whose rows are about 21 times farther apart than its columns. Growth is censored at the window edge in almost a third of the visits, and the 478 transitions have intervals that are multiples of 90 days, most of them 180 days. Chapter~\ref{ch:method} builds the framework on these properties."
- **Recurs:** E1 (supervisor repeat: raised one level)
- **Status:** open

### G089 · S2 · §3.1 Dataset — 03-data.tex:28 (p. 23)

~~~text
(MUW). It is drawn from the GA cohort described by \citet{Mai2024}, with
tighter registration bounds and cleaner segmentations, and was acquired in
~~~

- **Verdict:** 75 of the 184 Mai eyes: selection criteria not stated; needs: selection rule from MUW
- **Findings:** R-0617
- **Suggested fix (R-0617):** Rewrite as: "It is a subset of 75 of the 184 eyes of the GA cohort described by \citet{Mai2024}, selected by <needs: the selection criteria, e.g. the registration-error bound between the FAF annotation and the OCT grid, and what was checked or corrected in the segmentations>." In §5.7, add one clause stating that the 75 eyes are a quality-selected subset of the 184.
- **Status:** open

### G094 · S2 · §3.3 Spatial Standardisation and its Measured Cost — 03-data.tex:302 (p. 27)

~~~text
the one-year anchor (\S\ref{sec:data:temporal}) under-measure
progression for roughly one visit in five. The censoring also limits
~~~

- **Verdict:** "roughly one visit in five" matches no number (27.3 %, 31.1 % of visits; 21/75 eyes at the anchor)
- **Findings:** R-0699, R-0703, R-0704
- **Suggested fix (R-0699):** "The models are therefore trained on censored targets. At the one-year anchor, the lesion of 21 of the 75 eyes touches this edge (\S\ref{sec:experiments:protocol:metrics}). For these eyes, the change-region metrics score only the part of the change inside the window, and lesion areas and growth rates measured on the window are biased low."
- **Status:** open

### G095 · S2 · §3.5 Patient-Level Covariates — 03-data.tex:345 (p. vi)

~~~text
\section{Patient-Level Covariates}
~~~

- **Verdict:** §3.5 states no purpose and no hand-over (severity table)
- **Findings:** R-0714
- **Suggested fix (R-0714):** Open §3.5 with its purpose, using the reason already given in §4.2.3: "Age and sex are included as patient-level covariates because they are plausible modulators of how fast GA progresses." Close it with "How the covariates enter each operator is described in~\S\ref{sec:method:covariates}." Add one closing sentence to §3.1 and §3.4 that states what the section hands to the next (needs: wording by the author).
- **Recurs:** E1 (supervisor repeat: raised one level)
- **Status:** open

### G098 · S2 · §3.6 Temporal Structure — 03-data.tex:433 (p. 29)

~~~text
This is accepted deliberately. \citet{Mai2024} likewise score every follow-up
visit by its time since baseline, in yearly bins, and not at a fixed horizon.
~~~

- **Verdict:** "Mai et al. likewise score ... in yearly bins": their bins would put the 450-720-day visits in year 2, the anchor scores them as one year; "likewise" is wrong
- **Findings:** R-0752
- **Suggested fix (R-0752):** "This is accepted so that every eye contributes one score at the anchor. It departs from the yearly bins of \citet{Mai2024}, which would place these visits in the second year." Optionally report the effect (needs: change-region Dice of the canonical model over the 68 eyes scored at 360 days). Make the same correction in §5.1.3.
- **Status:** open

### G100 · S2 · §3.7 Splits and Cross-Validation — 03-data.tex:489 (p. 29)

~~~text
cross-validation, and every result reported in this thesis is a
validation result.
~~~

- **Verdict:** no caveat that configuration choices (reach ladder, objective, canonical model) were made on the same validation folds; Ch. 3 closing missing (with G088)
- **Findings:** R-0771, R-0772
- **Suggested fix (R-0771):** Add a closing paragraph after l. 490: "In summary, each eye provides a sequence of states $u_k \in \mathbb{R}^{11 \times 49 \times 1024}$, normalised per channel with training statistics, the intervals $\Delta t_k$ between its visits and the covariates $\mathbf{z}$. The 478 transition windows are split into five patient-level folds. Chapter~\ref{ch:method} describes the framework that is trained on these windows."
- **Recurs:** E1 (supervisor repeat: raised one level)
- **Status:** open

### G101 · S2 · Chapter 4 Method, §4.1 Overview — 04-method.tex:16 (p. 31)

~~~text
This chapter answers the first part of the research question: what kind
~~~

- **Verdict:** Ch. 4 claims to answer sub-question 1 but never states the answer and has no closing; framework scope differs between §1.2, §2.5.2, §4.1, §4.2
- **Findings:** R-0773, R-0774, R-0776, R-1051, R-1052 (groups merged in: G129)
- **Suggested fix (R-0773):** After l. 17, add a thesis statement that uses the components Chapter 7 names: "The framework developed here consists of a residual update conditioned on the elapsed time $\Delta t$ (\S\ref{sec:method:dt-residual}), a zero-initialised output so that every operator starts from persistence, one objective that weights the lesion mask (\S\ref{sec:method:training:loss}) and a training curriculum measured in elapsed days (\S\ref{sec:method:training:curriculum}). Which of these parts the results depend on is tested in~\S\ref{sec:experiments:ablations}." Also close the chapter, or §4.2 (see the §4.2 finding), with a short paragraph that restates this as the proposed answer to the first part.
- **Recurs:** E1
- **Status:** open

### G103 · S2 · §4.1 Overview — 04-method.tex:30 (p. 31)

~~~text
state on the $49 \times 1024$ grid of Chapter~\ref{ch:data}. Time is
handled by a single-step residual update conditioned on the interval between
~~~

- **Verdict:** "Everything outside the slot is held fixed ... single-step residual update with Delta t input" vs §4.3.6/§4.3.7: FEN always RK4 in 45-day sub-steps, Delta t entry zeroed (also G019)
- **Findings:** R-0783, R-0784, R-0785, R-1436 (groups merged in: G192)
- **Suggested fix (R-0783):** §4.1: "Time is handled by a residual update conditioned on the interval between visits (§4.2.1). Every operator takes one Euler step, except the FEN, which outputs a time derivative and is integrated with RK4 in 45-day sub-steps without Δt as an input (§4.3.6, §4.3.7)." §4.2 opener: "These parts are the same for every operator of the survey, except that the FEN, like any operator run in the Runge–Kutta wrapper, replaces the single step of Equation (4.1) by an RK4 integration (§4.3.7); whether the integration scheme alone changes the score is tested in §\ref{sec:experiments:ablations:time}." After "Δt therefore enters twice" in §4.2.1: "Inside the Runge–Kutta wrapper, which the FEN always uses, Δt enters only as the integration horizon (§4.3.7)." Caption: "Everything except the operator, and for the FEN the integration scheme (§4.3.7), is the same in every arm".
- **Status:** open

### G106 · S2 · §4.2 The Fixed Framework — 04-method.tex:109 (p. 32)

~~~text
This section defines what every arm shares: the input, the time handling
~~~

- **Verdict:** §4.2 intro is a content list without thesis statement; no closing paragraph saying what the framework is (E1)
- **Findings:** R-0815, R-0816 (groups merged in: G105)
- **Suggested fix (R-0816):** End the first paragraph with a thesis statement, e.g. "With these parts, any operator can be trained on visits with irregular intervals, starts from exact persistence and is optimised under the same loss and curriculum." Move l. 119-129 into a short subsection of its own (e.g. 'Input and Prediction Step'). After §4.2.6, add a closing paragraph: "In summary, the framework fixes one input visit, the residual update of Equation~\eqref{eq:method:residual-update} with a zero-initialised output, the loss of Equation~\eqref{eq:method:loss}, the time-budgeted curriculum and the settings of Table~\ref{tab:method:hparams}; \S\ref{sec:method:family} describes the operators that fill the slot."
- **Recurs:** E1
- **Status:** open

### G108 · S2 · §4.2.1 Δt-Conditioned Residual Formulation — 04-method.tex:147

~~~text
u_{t+\Delta t} \;=\; u_t \;+\; \Delta t \cdot
~~~

- **Verdict:** Eq. 4.1 restates Eq. 2.8 with u_t, u_{t+Delta t} and no hat; Fig. 4.1 and §4.2.2 use u_k, hat u_{k+1} (SV-4.4)
- **Findings:** R-0828, R-0829, R-0830, R-0831, R-1558 (groups merged in: G107, G204)
- **Suggested fix (R-0829):** Restate Eq. 4.1 in the §2.5.2 symbols: "$\hat u_{k+1} = u_k + \Delta t_k \cdot f_\theta(u_k, \Delta t_k, \mathbf{z}_k)$". Write l. 143-144 as "from the current state $u_k$ to the predicted next state $\hat u_{k+1}$" and l. 161 as "collapses to $\hat u_{k+1} = u_k$". Alternatively, drop the restatement and refer to Equation~\eqref{eq:bg:problem-update} directly. Give $\mathbf{z}$ the visit index in §2.5.2 as well.
- **Recurs:** SV-4.4
- **Status:** open

### G110 · S2 · §4.2.4 Objective — 04-method.tex:297

~~~text
\mathcal{L} \;=\; \frac{1}{\bar{w}} \sum_{c=0}^{10} w_c\,
~~~

- **Verdict:** verified on the printed equation: (1/w-bar) sum_c w_c L_c is about 11x the channel-mean MSE, contradicting "comparable to an unweighted MSE"; needs: check the denominator in the training code
- **Findings:** R-0871
- **Suggested fix (R-0871):** Replace \frac{1}{\bar{w}} by \frac{1}{\sum_{c} w_c} and write "... w_c its weight; the sum of the weights is the denominator". Change the sentence to: "Dividing by the sum of the weights keeps the term on the scale of an unweighted MSE; with equal weights it equals the MSE averaged over the eleven channels."
- **Status:** open

### G111 · S2 · §4.2.5 Time-Budgeted Pushforward Curriculum — 04-method.tex:380 (p. 35)

~~~text
and 720 days for another. The framework therefore counts the depth in
elapsed days.
~~~

- **Verdict:** elapsed-day curriculum is never ablated (no run without unrolling), yet listed as a framework contribution; state it (open NOTES TODO, v8 #39)
- **Findings:** R-0881
- **Suggested fix (R-0881):** End §4.2.5 with: "The curriculum is used in every reported run; no run trains without unrolling or with a step-count curriculum, so its effect on the forecast is not measured." Add the same point to the limitations in §6.3.
- **Status:** open

### G112 · S2 · §4.2.6 Optimisation — 04-method.tex:426 (p. 36)

~~~text
schedule. All operators are trained with AdamW \citep{Loshchilov2019}, a
learning rate of $2 \times 10^{-3}$ and a weight decay of
~~~

- **Verdict:** shared recipe (lr, schedule, epochs, batch) not said to be untuned per operator, nor how it was chosen
- **Findings:** R-0890, R-0891
- **Suggested fix (R-0890):** Add at the end of the first paragraph of §4.2.6: "These settings were not tuned per operator. A shared recipe prevents differences in training from being confounded with the architectural differences, but it may suit some architectures better than others." Then state how the settings were chosen (needs: on which model and how learning rate, schedule and weight decay were set). In §4.1, replace "Holding these parts fixed removes them as confounding factors when operators are compared" by "Holding these parts fixed prevents differences in the setup from being confounded with the architectural differences under test".
- **Status:** open

### G115 · S2 · §4.3.2 Message-Passing Graph Neural Network — 04-method.tex:536 (p. 38)

~~~text
Several of its design decisions also
became part of the shared framework: the time handling, the output layer
~~~

- **Verdict:** "design decisions [of MP-PDE] became part of the framework: time handling, output layer, one-step prediction" contradicts Table 4.2 (bundling, conv decoder, fixed step replaced)
- **Findings:** R-0906, R-0908
- **Suggested fix (R-0906):** "Three choices made in adapting it became part of the shared framework: the $\Delta t$-scaled residual update, the zero-initialised output layer and the one-step prediction."
- **Status:** open

### G116 · S2 · §4.3.2 Message-Passing Graph Neural Network — 04-method.tex:641 (p. 39)

~~~text
receives the state $u_i$, the positions and the conditioning vector again,
~~~

- **Verdict:** verified: "Every round receives the state u_i, the positions" but Eqs. 4.5-4.6 use u_i - u_j and Delta p_ij
- **Findings:** R-0917
- **Suggested fix (R-0917):** 'Every round receives the state differences $u_i - u_j$, the position offsets $\Delta\mathbf{p}_{ij}$ and the conditioning vector again, so this information is available at every depth.'
- **Status:** open

### G117 · S2 · §4.3.2 Message-Passing Graph Neural Network — 04-method.tex:655 (p. 39)

~~~text
Because the framework predicts one step ($K = 1$,
\S\ref{sec:method:framework}), the one-dimensional convolutional head of
~~~

- **Verdict:** symbol clashes in §4.3: K (bundle vs last visit), M (rounds vs mass matrix), L, x_i, h (SV-4.4); also G065
- **Findings:** R-0918, R-0919, R-0920, R-0921, R-0924 (groups merged in: G118)
- **Suggested fix (R-0918):** Give the bundle size its own symbol in the MP-PDE summary and in Table 4.2, e.g. "the bundle size $n_{\mathrm{b}}$" (u_i^{k-n_b:k}, d_i^1, \dots, d_i^{n_b}, 1 \le l \le n_b). Rewrite line 655 as: "The one-dimensional convolutional head of the original, which exists to emit several bundled steps, was replaced by an MLP decoder, because the framework predicts one step per pass (\S\ref{sec:method:framework})."
- **Recurs:** SV-4.4 (supervisor repeat: raised one level)
- **Status:** open

### G120 · S2 · §4.3.3 Graph Construction on an Anisotropic Grid — 04-method.tex:766

~~~text
For comparison, the GA front advances a median of about 12 columns (68\,\textmu{}m) between two visits 180 days apart; the upper quartile is
~~~

- **Verdict:** front-advance statistic (12/17/23 columns), on which the stencil design rests, has no measurement procedure; Ch. 5/6 quote "10 to 25 columns"; needs: how it was measured
- **Findings:** R-0940, R-0941, R-0942, R-1329 (groups merged in: G175)
- **Suggested fix (R-0940):** Add one sentence after the statistic. Needs: the measurement procedure (e.g. the outward shift of the lesion edge along each row, over which eyes and visit pairs, whether validation eyes were included, and how other intervals were scaled to 180 days). Then make Chapters 5 and 6 quote the same quantiles (median 12, 90th percentile 23 columns).
- **Status:** open

### G122 · S2 · §4.3.3 Graph Construction on an Anisotropic Grid — 04-method.tex:778

~~~text
nodes at row offsets $\{-1, 0, +1\}$ and column offsets
$\{0, \pm 7, \pm 14, \pm 21\}$, excluding the node itself: 20 neighbours in
~~~

- **Verdict:** all column offsets are multiples of 7, so the stencil splits the lattice into 7 interleaved sub-lattices that never exchange messages; unstated, while §4.3.3 rejects the physical k-NN for decomposing into rows
- **Findings:** R-0947
- **Suggested fix (R-0947):** After 'excluding the node itself: 20 neighbours in total', add: 'Because every column offset is a multiple of seven, a node exchanges messages, at any depth, only with columns whose index differs from its own by a multiple of seven. The lattice therefore splits into seven interleaved sub-lattices, 40 µm apart along a row, which share the network weights and never exchange messages.' Follow this with the reason the split is acceptable (needs: the author's reason or evidence, e.g. that neighbouring columns 5.7 µm apart carry nearly the same state, or that the rollouts show no column-periodic pattern).
- **Status:** open

### G123 · S2 · §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid — 04-method.tex:837 (p. 42)

~~~text
The three operators of this subsection are dense grid operators: they act
~~~

- **Verdict:** dense-operator subsection opens without purpose and has no closing (severity table)
- **Findings:** R-0957
- **Suggested fix (R-0957):** Open with: "The three dense operators provide the properties listed in \S\ref{sec:method:family} that the graph network does not have: multiscale local detail (U-Net), global spectral support (FNO) and global support with a local path (local-kernel hybrid). They act on the state as an image ...". Move the Gupta and Salvi sentences directly after "The first dense operator is a U-Net". Close with one sentence: "All three lie within a factor of 1.25 of the canonical parameter count (\S\ref{sec:method:family:params})."
- **Recurs:** E1 (supervisor repeat: raised one level)
- **Status:** open

### G124 · S2 · §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid — 04-method.tex:866 (p. 43)

~~~text
5:1 without removing it. The schedule was deliberately not tuned further:
a comparison model whose geometry had been optimised on this dataset would
~~~

- **Verdict:** "optimised geometry would make a weaker control" reads backwards; asymmetry: stencil reach chosen from a ladder on the same folds, U-Net pooling / FNO modes never varied
- **Findings:** R-0962, R-0963
- **Suggested fix (R-0962):** Replace the sentence by: 'The schedule was fixed before training and not tuned further, because a setting chosen on the validation folds would carry a selection bias, as there is no test split (\S\ref{sec:data:splits}).' After 'Chapter~\ref{ch:experiments} tests this choice against smaller and larger reaches.' (l. 797) add: 'The dilated stencil was adopted as the canonical configuration after this comparison on the same validation folds, so its score may be slightly optimistic relative to the untuned operators.' Repeat the caveat in \S\ref{sec:discussion:limitations}. needs: whether the offsets ±7, ±14, ±21 were fixed before the reach ladder ran. If they were, say so, which removes most of the concern.
- **Status:** open

### G127 · S2 · §4.4 Implementation Details — 04-method.tex:1239 (p. vii)

~~~text
\section{Implementation Details}
~~~

- **Verdict:** verified: app:code is labelled but never referenced; code availability only there (incl. G128)
- **Findings:** R-1043, R-1044, R-2153 (groups merged in: G128, G282)
- **Suggested fix (R-1043):** Add at the end of the first paragraph of §4.4: "The structure of the code and its availability are described in Appendix~\ref{app:code}."
- **Status:** open

### G130 · S2 · Chapter 5 opener — 05-experiments.tex:15 (p. 50)

~~~text
This chapter answers the second part of the research question: what kind
of operator the framework of Chapter~\ref{ch:method} needs.
~~~

- **Verdict:** Ch. 5 opener and §5.1 opener give no thesis statement (severity table)
- **Findings:** R-1055
- **Suggested fix (R-1055):** After the first sentence of the chapter, add: "Inside the fixed framework, operators of three different classes reach similar scores at the one-year anchor, and what separates them is how far they reach in one step (\S\ref{sec:experiments:ingredients})." (wording of §5.10). Extend the §5.1 opener: "Every operator is scored by the late-epoch mean of the change-region Dice at the one-year anchor, and two operators are compared fold by fold against the variation caused by retraining."
- **Recurs:** E1 (supervisor repeat: raised one level)
- **Status:** open

### G132 · S2 · §5.1.1 Evaluation Challenges — 05-experiments.tex:64 (p. 50)

~~~text
mask values than the graph network: the late-epoch mask RMSE of the rollout
is roughly twice as large for the U-Net as for the graph network, while its
~~~

- **Verdict:** "its thresholded metrics are higher [than the graph network]" is false against the canonical stencil (0.5046 vs 0.5258); true only for k-NN; RMSE ratio has no value anywhere
- **Findings:** R-1063, R-1066, R-1067
- **Suggested fix (R-1063):** Name the network in both places, e.g. "...than the $k$-NN graph network: the late-epoch mask RMSE of the rollout is roughly twice as large for the U-Net as for the $k$-NN graph network, while its thresholded metrics are higher (Table~\ref{tab:experiments:arms})." needs: which graph network the RMSE ratio was measured against.
- **Status:** open

### G136 · S2 · §5.1.2 Metrics — 05-experiments.tex:143 (p. 51)

~~~text
These horizon bins show how
the prediction degrades beyond the one-year anchor.
~~~

- **Verdict:** "bins show how the prediction degrades beyond the one-year anchor" vs §5.3: every operator scores higher after the first year
- **Findings:** R-1086, R-1087, R-1088, R-1089
- **Suggested fix (R-1086):** "These horizon bins show how the growth-region Dice changes beyond the one-year anchor."
- **Status:** open

### G137 · S2 · §5.1.3 Rollout Evaluation — 05-experiments.tex:187 (p. 52)

~~~text
held constant. Per-step metrics are averaged per eye first and then over
the eyes, so every eye counts once, whatever its number of visits.
~~~

- **Verdict:** verified: §5.1.3 "averaged per eye first ... every eye counts once" vs Table 5.2 caption / l.535 "every rollout step in the bin ... pooled"
- **Findings:** R-1104, R-1105, R-1106, R-1107
- **Suggested fix (R-1104):** Limit the rule and state the exception: "Metrics at the one-year anchor are computed once per eye and averaged over the eyes, so every eye counts once. The horizon bins of \S\ref{sec:experiments:horizon} instead pool all follow-up visits in a bin, so an eye with several visits in a bin contributes several values."
- **Status:** open

### G138 · S2 · §5.1.4 Late-Epoch Mean — 05-experiments.tex:246 (p. 53)

~~~text
Because no epoch is
chosen on the validation scores, it carries no selection bias, and
~~~

- **Verdict:** "carries no selection bias": window start and configurations (reach ladder, T-FEN form, canonical model) were chosen on the same folds; no test split (with G100)
- **Findings:** R-1115, R-1116
- **Suggested fix (R-1115):** "Because no epoch is chosen on the validation scores, the late-epoch mean carries no bias from selecting an epoch, and averaging twenty epochs reduces the noise of a single epoch. Choices made on the same validation folds, such as the window itself (Figure~\ref{fig:experiments:learning-speed}) and the settings tested in~\S\ref{sec:experiments:ablations}, are not protected in this way." Add the corresponding limitation to \S\ref{sec:discussion:limitations}.
- **Status:** open

### G139 · S2 · §5.1.5 Noise Level and Comparisons — 05-experiments.tex:292 (p. 53)

~~~text
standard deviation of $\sigma \approx 0.0127$ for the late-epoch
change-region Dice of one graph network
~~~

- **Verdict:** sigma measured only for one graph network and the U-Net; FNO/FEN/T-FEN z-values assume the GNN sigma, unstated; T-FEN vs stencil verdict depends on it
- **Findings:** R-1124, R-1125, R-1525, R-2102, R-2103 (groups merged in: G198, G277)
- **Suggested fix (R-1124):** State the assumption: "This value was measured on one graph network and is assumed for every arm except the U-Net." Better, estimate σ for the arms that have a second seed (T-FEN, FNO, FNO + 3x3; App. C.4) in the same way as for the U-Net, and use those values in z. needs: those σ values. Otherwise read every comparison with a non-graph arm against the U-Net bar of about 0.020.
- **Recurs:** SV-5.2
- **Status:** open

### G142 · S2 · §5.1.5 Noise Level and Comparisons — 05-experiments.tex:303 (p. 54)

~~~text
established only when, in addition, it holds on most folds, the
comparison over the 75 validation eyes points the same way clearly (a
~~~

- **Verdict:** "established" defined differently in §5.1.5 (most folds, second seed always, t about 2.5) and App. C.3 (LOFO sign, second seed only where run); "about 2.5" decides T-FEN vs stencil (incl. G141, G143, G144)
- **Findings:** R-1128, R-1129, R-1130, R-1131, R-1133, R-2108, R-2109, R-2110, R-2112, R-2113 (groups merged in: G141, G143, G144, G280)
- **Suggested fix (R-1129):** Restate the appendix list in one sentence with one fixed bar and its reason: "A difference is called established when |z| > 1.96, the paired t over the 75 eyes reaches [bar] (higher than the 5 % value of about 2.0, because the two eyes of one patient are not independent and about fifty comparisons are tested), its sign does not change when any one fold is left out, and, where the comparison was run at both seeds, it holds at both." Needs: one exact per-eye bar instead of "about 2.5" (Appendix C.3).
- **Status:** open

### G146 · S2 · §5.1.5 Noise Level and Comparisons — 05-experiments.tex:314 (p. 54)

~~~text
The main comparisons were repeated with a second random seed, and the
conclusions drawn in this chapter hold at both. All numbers in this
~~~

- **Verdict:** "the conclusions drawn in this chapter hold at both [seeds]" though capacity, step-size test and other ablations ran with one seed
- **Findings:** R-1137, R-1917 (groups merged in: G261)
- **Suggested fix (R-1137):** "The comparisons listed in Appendix~\ref{app:full-results:seeds} were repeated with a second random seed, and their conclusions hold at both; the other experiments of this chapter use the first seed only, as stated where they are reported."
- **Status:** open

### G147 · S2 · §5.1.5 Noise Level and Comparisons — 05-experiments.tex:315 (p. 54)

~~~text
conclusions drawn in this chapter hold at both. All numbers in this
chapter are for the first seed.
~~~

- **Verdict:** "All numbers in this chapter are for the first seed" but §5.2 quotes second-seed z and t, §5.5 shows a seed-7 panel; "first seed" vs "seed 42" naming
- **Findings:** R-1139, R-1142, R-1143, R-1354, R-1355, R-1357, R-1358 (groups merged in: G180)
- **Suggested fix (R-1139):** "All numbers in this chapter are for seed 42 unless a value is marked as seed 7; Appendix~\ref{app:full-results:seeds} gives every comparison at both seeds." Use "seed 42" and "seed 7" throughout §5.2, e.g. "just beyond the variation of retraining at seed 42 ($z = 2.1$) and within it at seed 7 ($z = 0.8$)".
- **Status:** open

### G151 · S2 · §5.3 Forecasts Beyond One Year — 05-experiments.tex:530 (p. 56)

~~~text
The one-year anchor scores every eye once. The rollout, however, continues
over the whole follow-up of an eye, up to about six years.
~~~

- **Verdict:** §5.3 opener gives method but no thesis statement (SV-5.5; severity table)
- **Findings:** R-1191
- **Suggested fix (R-1191):** After "This section follows the forecast over that time." add: "The dilated-stencil network and the T-FEN are the two highest operators in every bin, and every operator scores higher after the first year than within it."
- **Recurs:** SV-5.5
- **Status:** open

### G153 · S2 · §5.3 Forecasts Beyond One Year — 05-experiments.tex:567 (p. 57)

~~~text
The three whose
single step reaches less far than the lesion front advances between two
~~~

- **Verdict:** free-form FEN grouped with "single step reaches less far than the front", but §4.3.6: reach comes from RK4 sub-steps, ~16 evaluations per 180-day interval; reach per visit not shown (incl. G172, also l.863 and Fig. 5.3b)
- **Findings:** R-1201, R-1202, R-1307, R-1308 (groups merged in: G172)
- **Suggested fix (R-1201):** Either define "single step" for each operator and give the free-form FEN's reach per visit (needs: that value), or group the three descriptively: "The three operators without a long-range construction, the $k$-NN graph network, the one-hop floor and the free-form FEN, score 0.388 to 0.397." Adjust the caption of Figure 5.3(b) the same way.
- **Status:** open

### G155 · S2 · §5.3 Forecasts Beyond One Year — 05-experiments.tex:602 (p. 57)

~~~text
operators with short reach close part of their gap: the $k$-NN graph
network and the one-hop floor lie 0.106 and 0.108 below the dilated stencil
~~~

- **Verdict:** horizon values untested and pooled, yet read as orders and gaps of 0.002-0.02; "operators with short reach close part of their gap" is false for the free-form FEN (0.115 -> 0.135); "keep their lead over the whole follow-up" (incl. G154, G156)
- **Findings:** R-1214, R-1215, R-1216, R-1217, R-1218, R-1219, R-1220 (groups merged in: G154, G156)
- **Suggested fix (R-1215):** Add after the table reference: "The values are descriptive: no comparison between bins or operators is tested, and the later bins hold only the eyes with the longest follow-up." Rephrase l. 607-608: "The dilated stencil and the T-FEN score highest in every bin, although beyond three years the T-FEN lies only 0.017 above the FNO."
- **Status:** open

### G157 · S2 · §5.3 Forecasts Beyond One Year — 05-experiments.tex:609 (p. 57)

~~~text
the order changes with the horizon, and global context appears to matter
more for long forecasts than for the first year.
~~~

- **Verdict:** "global context appears to matter more for long forecasts" rests on the FNO alone; FNO+3x3 (same global context) is level with the U-Net beyond 3 y (incl. G169, l.800)
- **Findings:** R-1223, R-1224, R-1294 (groups merged in: G169)
- **Suggested fix (R-1223):** "Among the other operators, the order changes with the horizon: beyond three years the FNO (0.594) lies above the U-Net (0.555) and the FNO with local path (0.553), which it trailed in the first year." Drop the clause on global context.
- **Status:** open

### G160 · S2 · §5.4.1 Spatial Context — 05-experiments.tex:636

~~~text
\subsection{Spatial Context}
~~~

- **Verdict:** §5.4.1, §5.4.3, §5.4.4 have no table of their own; comparisons only in prose (E3, §11.6) (incl. G166)
- **Findings:** R-1233, R-1278 (groups merged in: G166)
- **Suggested fix (R-1233):** Add a small excerpt table to §5.4.1 (zero, one and two rounds: parameters, mean ± sd, difference, folds and eyes higher; values as in Table 5.1 and the text), to §5.4.3 (FNO, FNO + 3×3, U-Net, k-NN network with the four paired differences quoted in the text) and to §5.4.4 (free-form FEN at width 96, T-FEN at width 96, T-FEN at width 48: parameters, mean, difference, folds, eyes). Alternatively, extend Table 5.3 into one ablation table with a block per property. In either case, add the stencil against k-NN row to Table 5.3.
- **Recurs:** E3
- **Status:** open

### G165 · S2 · §5.4.2 Physical Reach at Lesion Scale — 05-experiments.tex:748

~~~text
The best tested reach, $\pm 21$ columns (about 119\,\textmu{}m), lies close
to the 90th percentile of the per-visit front advance, 23 columns
~~~

- **Verdict:** reach matched per hop (+-21 columns) though the canonical network runs two rounds (+-42 columns, 238 µm per update), while the k-NN reach is counted per update (+-4); inconsistent accounting under the central argument
- **Findings:** R-1275, R-1331, R-1811 (groups merged in: G176, G242)
- **Suggested fix (R-1275):** Count reach per update throughout and rewrite: "No tested geometry scores higher than the default hop of ±21 columns, which was set from the 90th percentile of the per-visit advance (§4.3.3). With two rounds, one update of the default network reaches ±42 columns (about 238 µm), about twice that advance. The ±12 variant, whose update reaches ±24 columns, scores lower." In line 903: "Two rounds on the index-space graph reach only ±4 columns, about 23 µm along a row (§4.3.3), so one update of such an operator covers only a small part of that advance."
- **Status:** open

### G167 · S2 · §5.4.3 Global and Local Context Together — 05-experiments.tex:778 (p. 60)

~~~text
Against the other operators, the plain FNO lies below the U-Net at the
one-year anchor: lower by 0.022 on average, higher on only one of the five
~~~

- **Verdict:** "the plain FNO lies below the U-Net" stated as fact and used for the conclusion, but App. C.4: beyond threshold at seed 42 only (z = -1.3 at seed 7); the local path, with a similar profile, is called "not established" (incl. G168)
- **Findings:** R-1281, R-1282, R-1291 (groups merged in: G168)
- **Suggested fix (R-1281):** "Against the other operators, the plain FNO lies below the U-Net at the one-year anchor at seed 42: lower by 0.022 on average, higher on only one of the five folds and on 30 of the 75 eyes. At the second seed it is also lower, but within the noise level, so the difference is not established (Appendix C.4)." Conclusion: "Global context alone scores below the U-Net at the one-year anchor at both seeds, beyond the noise level at one of them." For the hybrid, add: "at the second seed it lies lower on every fold, within the noise level".
- **Status:** open

### G170 · S2 · §5.4.4 An Explicit Transport Term — 05-experiments.tex:821

~~~text
zero-initialised (\S\ref{sec:method:dt-residual}), so the transport term is
the only difference.
~~~

- **Verdict:** "so the transport term is the only difference": control has half the parameters and lacks the coarser 7-column transport mesh (§4.3.6)
- **Findings:** R-1298, R-1299
- **Suggested fix (R-1298):** "Both arms start at persistence, because their output heads are zero-initialised (§4.2.1). The T-FEN adds the transport term, the velocity network that drives it (33 718 parameters, the difference between 68 503 and 34 785) and the coarser mesh on which it runs (§4.3.6)." In line 622, write "compares operators that differ mainly in one property".
- **Status:** open

### G179 · S2 · §5.5 Differences Between Folds — 05-experiments.tex:943 (p. 62)

~~~text
The scores of the five folds differ by more than most operators differ from
each other (\S\ref{sec:experiments:main-results}). This section asks why
~~~

- **Verdict:** §5.5 opener has no thesis statement (SV-5.5; severity table)
- **Findings:** R-1350
- **Suggested fix (R-1350):** Add after the second sentence: "The folds differ mainly in the eyes they hold; two properties of an eye, the distance at which new atrophy appears and contact with the window edge, also go with differences between the operators." Adjust this wording to the group names chosen for the grouping finding at line 1063.
- **Recurs:** SV-5.5 (supervisor repeat: raised one level)
- **Status:** open

### G181 · S2 · §5.5 Differences Between Folds — 05-experiments.tex:988 (p. 63)

~~~text
fold's 15 eyes. Two properties of the eyes separate the local
from the global operators.
~~~

- **Verdict:** the T-FEN is in the "global" group for distant atrophy but on the "local" side for edge contact and fold 3; §4.3.6 describes it as local (incl. G188)
- **Findings:** R-1370, R-1371, R-1372, R-1411, R-1412, R-1413, R-1414, R-1415 (groups merged in: G188)
- **Suggested fix (R-1370):** Name the groups instead of labelling them: "Two properties of the eyes separate the operators." ... "the dilated-stencil network scores lower relative to the mean of the T-FEN, the U-Net and the FNO". In the closing paragraph: "Where new atrophy appears far from the existing lesion, the T-FEN, the U-Net and the FNO do better than the dilated-stencil network." Reserve "dense" for the U-Net and the FNO.
- **Status:** open

### G184 · S2 · §5.5 Differences Between Folds — 05-experiments.tex:998 (p. 63)

~~~text
$\rho = -0.32$ over the 75 eyes). Eyes with little distant atrophy favour
the graph network, eyes with much of it the other three: on the third of
~~~

- **Verdict:** "eyes with much of it [favour] the other three" though that third reads -0.010 with SE spanning zero; conclusion upgrades rho = -0.32/-0.39 to "decide ... because" (incl. G187)
- **Findings:** R-1382, R-1409, R-1410 (groups merged in: G187)
- **Suggested fix (R-1382):** Lines 998-1001: "On the third of the eyes with the least distant atrophy, the graph network scores 0.035 higher than the mean of the other three operators; its lead shrinks as the share grows, and on the third with the most distant atrophy it is 0.010 lower, within one standard error of zero (Figure~\ref{fig:experiments:far-atrophy})." Conclusion: "Two properties of an eye also go with which kind of operator forecasts it better. Where new atrophy appears far from the existing lesion, the lead of the dilated-stencil network shrinks, which is consistent with its limited reach per step." List-of-figures title: "The lead of the graph network shrinks where new atrophy appears far from the lesion."
- **Status:** open

### G189 · S2 · §5.6 Negative Results — 05-experiments.tex:1077 (p. vii)

~~~text
\section{Negative Results}
~~~

- **Verdict:** §5.6 has no intro thesis statement and no closing on what the framework tests show (E1) (incl. G190)
- **Findings:** R-1419, R-1420, R-1422 (groups merged in: G190)
- **Suggested fix (R-1419):** Add a closing paragraph to §5.6: "Of the settings tested here, only the objective changes the result: the loss must emphasise the mask, and the soft-Dice term raises the score by 0.050. The time handling and the size of the operators can stay as they are."
- **Recurs:** E1 (supervisor repeat: raised one level)
- **Status:** open

### G191 · S2 · §5.6.1 Time Handling — 05-experiments.tex:1094

~~~text
\subsection{Time Handling}
~~~

- **Verdict:** §5.6.1 reports three comparisons without a table; absolute score of the no-multiplication variant printed nowhere (E3)
- **Findings:** R-1429, R-1430
- **Suggested fix (R-1429):** Add a small table in the format of Table 5.4. Rows: dilated-stencil network, one Euler step (0.526, reference); without the multiplication by Δt (needs: its mean ± sd; difference −0.0006, 2/5 folds, 30/75 eyes); RK4, autonomous (0.514, −0.012, 1/5 folds, needs: eye count); FNO, one step (0.483, reference); FNO, RK4 (0.489, +0.006, needs: folds and eyes). Then refer to it from the second paragraph.
- **Recurs:** E3
- **Status:** open

### G197 · S2 · §5.6.3 Capacity — 05-experiments.tex:1347

~~~text
Every architecture arm of Table~\ref{tab:experiments:arms} has 67 to 83
thousand parameters (\S\ref{sec:method:family:params}). The capacity study
~~~

- **Verdict:** "Every architecture arm of Table 5.1 has 67 to 83 thousand parameters" vs free-form FEN 34,785 and the floors in Table 5.1
- **Findings:** R-1508, R-1509, R-1510
- **Suggested fix (R-1508):** "The four architecture classes scaled here (the dilated-stencil graph network, the U-Net, the FNO with a local path and the T-FEN) have 67 to 83 thousand parameters at their original size (§4.3.8)."
- **Status:** open

### G199 · S2 · §5.6.3 Capacity — 05-experiments.tex:1441 (p. 68)

~~~text
level. The T-FEN with an eight-layer free-form network does not train on
any fold: its training error barely falls.
~~~

- **Verdict:** "does not train on any fold" vs mean 0.257 in Table 5.5 (persistence = 0); repeated "fails to train in both forms"
- **Findings:** R-1536, R-1538, R-1539, R-1540
- **Suggested fix (R-1536):** "The T-FEN with eight-layer networks trains poorly on every fold: its training error barely falls, and it ends 0.285 lower than at depth four (0.257 against 0.543)." At line 1451: "and the eight-layer network trains poorly in both forms."
- **Status:** open

### G200 · S2 · §5.6.3 Capacity — 05-experiments.tex:1444 (p. 68)

~~~text
More parameters therefore improve none of the four classes, and the
~~~

- **Verdict:** capacity null is at the shared lr and 30-epoch budget, only one arm per class was scaled, T-FEN width 192 diverged on two folds; "do not depend on the size" overstates
- **Findings:** R-1542, R-1543, R-1545, R-1546 (groups merged in: G201)
- **Suggested fix (R-1542):** In the width paragraph add: "For the T-FEN, the step to width 192 diverged in training on folds 1 and 4 and is read on the other three." Rewrite the closer: "At the shared learning rate and 30-epoch budget (\S\ref{sec:method:training:optim}), more parameters improve none of the four classes. The larger T-FEN networks do not train reliably under these settings, so the study does not show whether larger models with retuned optimisation would score higher. The result is scoped to one seed."
- **Recurs:** AI-5c.28
- **Status:** open

### G205 · S2 · §5.7.1 The Step-Size Test — 05-experiments.tex:1583

~~~text
A model is read as a continuous-time model only if it satisfies both. C1
is read at the two finest steps: from 22.8 to 11.4 days the prediction
~~~

- **Verdict:** operational C1 rule (last halving + Euler/RK4 agreement at 11.4 d) differs from the bullet and was fixed after the test ran (comment); the text does not say so
- **Findings:** R-1566
- **Suggested fix (R-1566):** Replace the C1 bullet with: "C1, convergence: at the two finest steps the prediction has settled; from 22.8 to 11.4 days it changes by less than the run-to-run noise with both schemes, and the two schemes agree to within it at 11.4 days;". Delete the separate sentence at lines 1583-1586 apart from "A model is read as a continuous-time model only if it satisfies both.", and add: "The thresholds of C1 were set after the test had been run."
- **Status:** open

### G207 · S2 · §5.7.1 The Step-Size Test — 05-experiments.tex:1606

~~~text
\item the T-FEN in its energy-conserving form, trained with RK4 in steps
~~~

- **Verdict:** the only model passing C2 is also the only one trained with sub-steps (45 d); operator vs training step not separated, yet stated as a model property (also §5.10)
- **Findings:** R-1577
- **Suggested fix (R-1577):** Add after the conclusion paragraph: 'The T-FEN is also the only model of the three trained with sub-steps. Whether the graph network trained with 45-day RK4 steps would pass as well was not tested, so the difference between the models may come from the training step rather than from the operator.'
- **Recurs:** SV-5.12
- **Status:** open

### G209 · S2 · §5.7.1 The Step-Size Test — 05-experiments.tex:1684

~~~text
for it. The energy-conserving T-FEN can be read as a continuous-time model,
~~~

- **Verdict:** T-FEN read as continuous-time "within one seed" only; the test sees one thresholded Dice at the anchor, and §5.7.2 puts the mask channel above the RK4 limit at 45 d
- **Findings:** R-1597, R-1598
- **Suggested fix (R-1597):** 'Within the scope of one seed and of the change-region Dice at the one-year anchor, the energy-conserving T-FEN behaves as a continuous-time model. Its 45-day training step lies slightly outside the RK4 stability limit on the mask channel (\S\ref{sec:experiments:validity:tfen}), so this reading does not extend to rollouts over several years.' Summary (l. 2251-2252): 'The energy-conserving T-FEN behaves as a continuous-time model up to the one-year anchor; the canonical network does not.'
- **Status:** open

### G210 · S2 · §5.7.1 The Step-Size Test — 05-experiments.tex:1688 (p. 70)

~~~text
finer steps change its Dice by 0.016 to 0.018 in either direction. Neither property decides
~~~

- **Verdict:** "Neither property decides the accuracy" (SV-7.3 pattern), unclear which two properties; repeated in §5.10
- **Findings:** R-1601, R-1602, R-1603, R-1604, R-1605
- **Suggested fix (R-1601):** §5.7.1: "A continuous-time reading does not come with higher accuracy: the Runge--Kutta network scores no higher than the canonical network (\S\ref{sec:experiments:ablations:time}), and the advantage of the T-FEN over the free-form FEN comes from its transport term (\S\ref{sec:experiments:ingredients:transport})." Summary: "... the canonical network cannot; this reading does not come with higher accuracy (\S\ref{sec:experiments:validity})."
- **Recurs:** SV-7.3
- **Status:** open

### G213 · S2 · §5.7.2 Numerical Stability of the T-FEN — 05-experiments.tex:1895

~~~text
without changing the Dice (\S\ref{sec:experiments:validity:swap}). Only the
~~~

- **Verdict:** "An evaluation step of 30 days ... removes the residual without changing the Dice (§5.7.1)": §5.7.1 / Table C.6 have no 30-day setting; needs: the 30-day value and fold
- **Findings:** R-1642
- **Suggested fix (R-1642):** State the evidence in place and drop the pointer: 'On fold 0, a re-evaluation with RK4 in 30-day steps, at which the Courant number of the mask channel falls to about 1.8, removes the residual and changes the change-region Dice by <needs: value>.' Alternatively, if the 22.8-day setting of Table C.6 is the evidence, use it and say so (needs: whether the residual vanishes at 22.8 days).
- **Status:** open

### G216 · S2 · §5.8 Comparison with Prior Work — 05-experiments.tex:1963

~~~text
The values give an orientation, not a head-to-head result. The study
~~~

- **Verdict:** comparison with prior work omits that the values here are validation results with the configuration chosen on the same folds, while Salvi/Yoshida report held-out test sets; "not a head-to-head result" (AI-5d.29)
- **Findings:** R-1655, R-1657
- **Suggested fix (R-1655):** Add to the caveat paragraph: 'The values of this thesis are validation results of a cross-validation without a held-out test set (\S\ref{sec:data:splits}), on the same folds on which the reach of the dilated stencil was chosen; \citet{Salvi2025} and \citet{Yoshida2025} report values on held-out test eyes.'
- **Status:** open

### G217 · S2 · §5.8 Comparison with Prior Work — 05-experiments.tex:1973 (p. 74)

~~~text
these are specified. One difference remains: their paper computes the
growth rate from the baseline and the respective follow-up area, whereas
~~~

- **Verdict:** growth rate: "one difference remains" (l.1973-1975) vs "as in Mai et al." (l.2046) (incl. G221)
- **Findings:** R-1658, R-1675, R-1677 (groups merged in: G221)
- **Suggested fix (R-1658):** At line 2046 drop "as in~\citet{Mai2024}" and state the relation once: "The rate is computed once from the ground truth and once from the model's rollout, over the eye's whole follow-up, not at the one-year anchor; unlike \citet{Mai2024}, one rate per eye is used (see above)." Needs: confirmation of which part of Mai et al.'s definition matches (the follow-up period of the correlation) and which differs (per-visit rates).
- **Recurs:** AI-5d.31
- **Status:** open

### G219 · S2 · §5.8 Comparison with Prior Work — 05-experiments.tex:1986 (p. 75)

~~~text
and report the same quantity in the same bins. Their values, 0.46 in the
~~~

- **Verdict:** "same quantity in the same bins" as Gigon et al., but their last bins are 3-4 and >4 y (caption) and their lesion is RORA on OCT, not FAF GA
- **Findings:** R-1663
- **Suggested fix (R-1663):** "... and report the growth-region Dice of RORA by year since baseline; their bins match those used here up to three years and then split into 3 to 4 and more than 4 years. Their values, 0.46 in the first year rising to 0.65 in the fourth year and 0.72 after four years, lie close to those of the canonical network, 0.50 rising to 0.66 beyond three years."
- **Status:** open

### G222 · S2 · §5.8 Comparison with Prior Work — 05-experiments.tex:2099 (p. 76)

~~~text
model therefore predicts part of the differences in growth speed between
eyes, but less of them than the model of~\citet{Mai2024}, on both measures.
~~~

- **Verdict:** growth-speed ranking on point estimates: Mai's AUCs (0.81/0.79/0.77) lie inside the model's bootstrap intervals; Gigon's r 0.52 inside [0.20, 0.57]
- **Findings:** R-1680, R-1681, R-1850, R-1851 (groups merged in: G252)
- **Suggested fix (R-1680):** Line 2099-2100: "The model therefore predicts part of the differences in growth speed between eyes. Its correlation is lower than that of \citet{Mai2024}, whose value of 0.61 lies outside the bootstrap interval. Its AUCs are also lower, but each value of \citet{Mai2024} lies inside the corresponding interval." Line 2137: "The point estimate of the canonical model, $r = 0.40$, lies below all three; the values of \citet{Gigon2021} and \citet{Yoshida2025} lie inside or at the upper edge of its interval of 0.20 to 0.57." Line 2157: "... the canonical model lies below every comparable model in its point estimate, $r = 0.40$ against 0.52 to 0.61, and outside its interval only against \citet{Mai2024}."
- **Status:** open

### G224 · S2 · §5.10 Summary — 05-experiments.tex:2243 (p. 79)

~~~text
from spatial context (\S\ref{sec:experiments:main-results}). What
separates the operators is how far they reach in one step: placing the
~~~

- **Verdict:** §5.10 "What separates the operators is how far they reach in one step" (SV-7.3 pattern) states reach as established; §5.4.5 says it does not prove the mechanism
- **Findings:** R-1718, R-1719, R-1720, R-1722, R-1723, R-1724, R-1725
- **Suggested fix (R-1718):** Rewrite lines 2240-2248 as: "This chapter answered the second part of the research question: the framework needs an operator with spatial context whose single update reaches about as far as the lesion front advances between two visits (57 to 142\,\textmu{}m, \S\ref{sec:experiments:ingredients:convergence}). Inside the fixed framework, operators of three classes reach similar scores at the one-year anchor (\S\ref{sec:experiments:main-results}). Placing the neighbours of the graph network at lesion scale and adding an explicit transport term each raise the score by 0.06 to 0.07 against their own controls, and the two arms built in these ways are the two highest (\S\ref{sec:experiments:ingredients}). For the first part of the question, the tests of the framework's own settings show that the objective must emphasise the mask ...".
- **Recurs:** SV-7.3
- **Status:** open

### G225 · S2 · §5.10 Summary — 05-experiments.tex:2249 (p. 79)

~~~text
the objective matters: it must emphasise the mask. The time handling, the
integration scheme and the size of the operators do not change the result
~~~

- **Verdict:** "the size of the operators [does] not change the result" vs §5.6.3: FNO+3x3 lower at both other widths, depth-8 T-FEN 0.257, width-192 diverges
- **Findings:** R-1730, R-1732
- **Suggested fix (R-1730):** "The time handling and the integration scheme do not change the result, and larger operators do not improve it (\S\ref{sec:experiments:ablations})."
- **Status:** open

### G226 · S2 · §6.1 Interpretation of Results (chapter opening) — 06-discussion.tex:30 (p. 80)

~~~text
scores 0 by construction. This section interprets the results for each
part of the question and then draws the implications for modelling.
~~~

- **Verdict:** Ch. 6 has no chapter opener with the main outcome and a map (severity table)
- **Findings:** R-1739
- **Suggested fix (R-1739):** Move l.19-31 above \section{Interpretation of Results} so that they open the chapter. After the metric sentence, add: "Inside the shared framework, operators from unrelated classes reached similar scores. The objective decided whether any change was learned, and among operators with spatial context the reach of one update relative to the advance of the front separated them most." Replace the last sentence with: "Section~\ref{sec:discussion:interpretation} interprets these results for each part of the question, \S\ref{sec:discussion:clinical} discusses their clinical implications, \S\ref{sec:discussion:limitations} the limitations and \S\ref{sec:discussion:future} future work."
- **Recurs:** E1
- **Status:** open

### G227 · S2 · §6.1.1 The Framework — 06-discussion.tex:49 (p. 80)

~~~text
no neighbours, stays at 0. One framework thus served operators from
unrelated literatures without change. This is the answer to the first
~~~

- **Verdict:** "This is the answer to the first part" points to "the framework served all operators", near circular; Ch. 7 states the answer differently (AI-S14)
- **Findings:** R-1744
- **Suggested fix (R-1744):** "One framework thus served operators from unrelated literatures without modification. The answer to the first part of the question is therefore a framework that conditions a residual update on the interval $\Delta t$, starts every model at persistence and trains it with a loss that weights the mask channel." Use the same list of elements in Chapter 7, l.15-21.
- **Recurs:** AI-S14
- **Status:** open

### G233 · S2 · §6.1.2 The Operator — 06-discussion.tex:78 (p. 81)

~~~text
established. The class of an operator therefore does not decide its
score. The ablations of~\S\ref{sec:experiments:ingredients} tested three
~~~

- **Verdict:** "The class of an operator therefore does not decide its score" (SV-6.1 / SV-7.3 pattern, does not follow); "tested three properties" vs §5.4 "four"; Ch. 7 "a third candidate"
- **Findings:** R-1761, R-1762, R-1763, R-1764, R-1765, R-1767, R-1768, R-1769, R-1771
- **Suggested fix (R-1761):** "Operators from three unrelated classes thus reach scores within 0.04 of each other."
- **Recurs:** SV-7.3
- **Status:** open

### G235 · S2 · §6.1.2 The Operator — 06-discussion.tex:85

~~~text
front moves is the largest lever. Replacing the index-space
~~~

- **Verdict:** "the largest lever" for reach, though spatial context (0 -> 0.45) and the objective are larger and transport is equal; repeated in §6.1.6 and the last sentence of Ch. 7
- **Findings:** R-1779, R-1780, R-1972 (groups merged in: G270)
- **Suggested fix (R-1779):** Bullet: "The reach of one update along the direction in which the lesion front moves raises the score: replacing the index-space neighbourhood of the graph network by the dilated stencil raises it by 0.064, at the same parameter count." l.226: "Among operators with spatial context, the largest effects came from two changes to the operator: ...". Ch. 7 l.87: "Among the operators with spatial context, the property with the largest effect was whether one update can see as far as the disease moves between two visits."
- **Status:** open

### G244 · S2 · §6.1.2 The Operator — 06-discussion.tex:158 (p. 82)

~~~text
(\S\ref{sec:experiments:ingredients:global}). This suggests that global
context matters more for long forecasts than at one year.
~~~

- **Verdict:** §6.1.2 never states the answer to part 2, ends on the long-horizon remark; global-context reading rests on the FNO alone (see G157)
- **Findings:** R-1814, R-1815
- **Suggested fix (R-1814):** Close §6.1.2 with: "The answer to the second part of the question is therefore an operator with spatial context whose single update reaches about as far as the lesion front moves between two visits, through the placement of its neighbours or through an explicit transport term. Operators of different classes that meet this condition reach similar scores."
- **Recurs:** E1
- **Status:** open

### G247 · S2 · §6.1.5 Predictions Between Visits — 06-discussion.tex:212

~~~text
and the wrapper costs about $4.8\times$ the training time. If predictions
between visits are needed clinically, these two models give predictions
~~~

- **Verdict:** the SV-6.5 sentence still says both models give consistent between-visit predictions, then that the wrapper needs a finer step; "changes its predictions by up to 0.018" (the Dice is meant)
- **Findings:** R-1834, R-1835, R-1836, R-1837
- **Suggested fix (R-1834):** "If predictions between visits are needed clinically, the T-FEN provides them consistently with its predictions at the visits. The wrapper network does so only when it is integrated with a finer step than in training; the finer step changes its change-region Dice at one year by up to 0.018 on single folds and by 0.004 on average (\S\ref{sec:experiments:validity:swap})."
- **Recurs:** SV-6.5 (supervisor repeat: raised one level)
- **Status:** open

### G248 · S2 · §6.1.5 Predictions Between Visits — 06-discussion.tex:220 (p. 83)

~~~text
the two visits, brought no benefit and was removed before the experiments
of Chapter~\ref{ch:experiments}.
~~~

- **Verdict:** §6.1.5 ends on the removed regulariser instead of a conclusion (severity table)
- **Findings:** R-1840
- **Suggested fix (R-1840):** End §6.1.5 with: "Predictions between visits are therefore available from the T-FEN, but their correctness cannot be assessed with these data." End §6.2 with: "The forecasts are therefore most informative about where a lesion grows; on how fast it grows they are weaker than the models of \S\ref{sec:experiments:qualitative}."
- **Recurs:** E1 (supervisor repeat: raised one level)
- **Status:** open

### G250 · S2 · §6.2 Clinical Implications — 06-discussion.tex:239 (p. viii)

~~~text
\section{Clinical Implications}
~~~

- **Verdict:** §6.2 ends on a list of failure cases without a clinical bottom line (E1)
- **Findings:** R-1845
- **Suggested fix (R-1845):** Add a closing paragraph: "In summary, the forecast locates the growth along the lesion border at a level within the range of prior work, but it predicts the growth speed of an individual eye less well than comparable models and was evaluated on one cohort only. It would need external validation and a measure of its own uncertainty (\S\ref{sec:discussion:future}) before it could support treatment decisions."
- **Recurs:** E1 (supervisor repeat: raised one level)
- **Status:** open

### G251 · S2 · §6.2 Clinical Implications — 06-discussion.tex:244 (p. 83)

~~~text
this measure the operators are well above persistence. The speed of
~~~

- **Verdict:** "well above persistence" holds for any model that predicts change (persistence = 0); no non-learned growth baseline (uniform dilation by the median advance) and §6.3 does not name its absence; needs: that baseline's score
- **Findings:** R-1848, R-1849
- **Suggested fix (R-1848):** Needs: the change-region Dice of a uniform-growth baseline (baseline mask dilated by the median front advance per interval, in µm on both axes). Until then, drop "well/far above persistence" and add to §6.3: "No non-learned growth model, such as a uniform dilation of the baseline lesion by the median front advance, was evaluated. The scores are compared with persistence only, which scores 0 by construction, so they do not show how much the operators add beyond the average growth of the cohort."
- **Status:** open

### G254 · S2 · §6.2 Clinical Implications — 06-discussion.tex:273 (p. 84)

~~~text
\item The operators predict less change than occurs in most eyes, 35 of
    48 on folds 0 to 2 at a median of 0.73 of the true change
~~~

- **Verdict:** "35 of 48 on folds 0 to 2 at a median of 0.73" printed nowhere in Ch. 5 (comment only); points to Fig. 5.2 (one eye); attributed to "the operators" (incl. G186)
- **Findings:** R-1864, R-1865, R-1866, R-1867, R-1868
- **Suggested fix (R-1864):** After the Figure 5.2 paragraph in §5.2, add: "Across the 48 validation eyes of folds 0 to 2, the canonical model predicts less change than occurs in 35, at a median of 0.73 of the true change." Point the bullet to \S\ref{sec:experiments:main-results} and begin it with "The canonical model predicts less change ...".
- **Status:** open

### G257 · S2 · §6.2 Clinical Implications — 06-discussion.tex:301 (p. 84)

~~~text
All comparisons in this thesis are made at the one-year anchor, the
~~~

- **Verdict:** "All comparisons in this thesis are made at the one-year anchor" is false (§5.3 bins, §5.8 whole follow-up); 0.60-0.66 cited to §5.4.4 instead of §5.3
- **Findings:** R-1877, R-1878, R-1881
- **Suggested fix (R-1877):** "All tested comparisons between operators (§5.1.5) are made at the one-year anchor, the first visit about one year after baseline; beyond it, only descriptive values exist (§5.3)." Point l. 306 to Table~\ref{tab:experiments:horizon} (§5.3).
- **Status:** open

### G258 · S2 · §6.2 Clinical Implications — 06-discussion.tex:321 (p. 85)

~~~text
neither a target nor an upper limit for the models of this thesis. It was
measured on a different imaging modality and a different cohort, and the
~~~

- **Verdict:** Salvi's grader agreement called "a different imaging modality", but the reference masks here are FAF outlines too (§3.1, §6.3)
- **Findings:** R-1887, R-1888
- **Suggested fix (R-1887):** "It was measured on a different cohort and on outlines drawn directly on the FAF images rather than registered onto an OCT grid, and the graders outlined existing images rather than predicting a future one."
- **Status:** open

### G259 · S2 · §6.2 Clinical Implications — 06-discussion.tex:333 (p. 85)

~~~text
them. Forecast failures are most likely where the method is known to be
weak:
~~~

- **Verdict:** "known weaknesses": border lesions (canonical 0.516 vs 0.522 interior) and sparse schedules are not shown; the documented failure (distant / new lesions, §5.5, App. B) is missing
- **Findings:** R-1891, R-1892, R-1893
- **Suggested fix (R-1891):** "Forecast failures were observed where new atrophy appears far from the existing lesion or as new separate lesions (§5.5, Appendix B), and for fast progressors, whose growth is under-predicted (§5.8). Lesions that touch the edge of the imaged field are censored in the reference itself; the dense operators lose most there (§5.5). Whether long intervals between visits degrade the forecast was not analysed."
- **Status:** open

### G260 · S2 · §6.3 Limitations — 06-discussion.tex:347

~~~text
The cohort is small: 75 eyes of 51 patients, with 12 to 20 validation
~~~

- **Verdict:** §6.3 and §6.4 have no opening sentence; single site, one device, one grading protocol, no external cohort missing from the limitations
- **Findings:** R-1895, R-1897
- **Suggested fix (R-1895):** Open §6.3 with: "The conclusions of this thesis are limited by the data, the evaluation and the scope of the models." Open §6.4 with: "The following directions follow from the results of \S\ref{sec:discussion:interpretation} and the limitations of \S\ref{sec:discussion:limitations}."
- **Recurs:** E1 (supervisor repeat: raised one level)
- **Status:** open

### G263 · S2 · Ch. 7 Conclusion — 07-conclusion.tex:15 (p. 88)

~~~text
For the first part, the forecast requires a setup that accommodates the
irregular visit schedules of clinical data and treats every candidate
~~~

- **Verdict:** Ch. 7 answer to part 1 opens with requirements of the comparison ("treats every candidate model equally"); curriculum and zero-init never ablated; the tested requirement (loss) comes later (AI-S14)
- **Findings:** R-1936, R-1937
- **Suggested fix (R-1936):** Ch. 7: "For the first part, the thesis shows that one framework is sufficient for every operator with spatial context: a residual update conditioned on Δt, a zero-initialised output, a curriculum measured in elapsed days, and one loss and evaluation for all models. Of its parts, the emphasis of the loss on the mask was shown to be necessary ...; the curriculum and the zero initialisation were not ablated." Add the last clause to §6.3.
- **Recurs:** AI-S14
- **Status:** open

### G266 · S2 · Ch. 7 Conclusion — 07-conclusion.tex:56 (p. 89)

~~~text
visits. That two independent routes lead to the same level is the central
architectural result of this thesis; it is more informative than the score
~~~

- **Verdict:** Ch. 7 drops the "does not prove the mechanism" hedge and keeps the tag "more informative than the score of any single model" (AI-6-7.52); "two unrelated ways" (see G177)
- **Findings:** R-1949, R-1950 (groups merged in: G265)
- **Suggested fix (R-1950):** "Both routes lead to about the same score, and this agreement is the central architectural result of this thesis." Delete the clause after the semicolon.
- **Recurs:** AI-6-7.52
- **Status:** open

### G268 · S2 · Ch. 7 Conclusion — 07-conclusion.tex:84 (p. 89)

~~~text
limits, for forecasts from longitudinal medical imaging in a low-data
clinical setting, the framework around the model and the properties of
~~~

- **Verdict:** last sentences generalise from one 75-eye single-site cohort to "longitudinal medical imaging in a low-data clinical setting"; "mattered more than the choice of operator family" antithesis (SV-7.5) (incl. G269)
- **Findings:** R-1966, R-1967, R-1968, R-1971 (groups merged in: G269)
- **Suggested fix (R-1966):** "Within these limits, operators of different families reached similar scores once they shared one framework. Among the operators with spatial context, the property with the largest effect was whether one update can see as far as the disease moves between two visits."
- **Recurs:** SV-7.5
- **Status:** open

### G273 · S2 · App. C.1 Border-Touching and Interior Eyes — 91-appendix.tex:120 (p. viii)

~~~text
\section{Border-Touching and Interior Eyes}
~~~

- **Verdict:** Appendix C has no opening paragraph; C.2 has only a table (severity table)
- **Findings:** R-2058
- **Suggested fix (R-2058):** Add a chapter opener after line 118: "This appendix collects the material behind Chapter~\ref{ch:experiments}: the scores on border-touching and interior eyes (\S\ref{app:full-results:border}), the growth-speed measures of every arm (\S\ref{app:full-results:growth-speed}), the criteria and statistics of all comparisons (\S\ref{app:full-results:criteria}, \S\ref{app:full-results:seeds}) and every setting of the step-size test (\S\ref{app:full-results:step-ladder})." Open C.1 and C.2 with one sentence each that names the question the table answers.
- **Recurs:** E1 (supervisor repeat: raised one level)
- **Status:** open

### G278 · S2 · §C.3 Statistical Criteria — 91-appendix.tex:230 (p. 101)

~~~text
differences of the two arms over the five folds. Without a real
difference, this mean $\bar{\Delta}$ varies only through retraining, with
~~~

- **Verdict:** z tests a difference only against retraining noise; the between-fold SE (2-3x sigma_Delta, e.g. FNO - k-NN +0.0208 +- 0.0258 with z = 2.6) is never explained, so z reads as a generalisation test; caption silent too (incl. G279, G281)
- **Findings:** R-2104, R-2106, R-2124 (groups merged in: G279, G281)
- **Suggested fix (R-2104):** Replace the sentence with: "If the two arms performed identically on every fold, this mean would vary only through retraining, with a standard deviation ... over $n$ folds. The $z$ statistic therefore tests the difference on these five folds against retraining noise. It does not include the variation of the difference between folds, which the SE column of the tables shows to be larger for most comparisons (e.g. 0.0246 for U-Net $-$ $k$-NN at seed 42, against $\sigma_\Delta \approx 0.010$). That variation is covered by the fold count, the per-eye test and the leave-one-fold-out condition."
- **Status:** open

### G287 · S2 · §E.1 Background: MM-PDE — 91-appendix.tex:700 (p. 111)

~~~text
original mesh, removing the residual-cut network of their model (not used
in this thesis), and replacing the DMM mesh by the uniform mesh. Each of
~~~

- **Verdict:** the residual cut, which Hu et al. find needed for accuracy, is dropped "(not used in this thesis)" without reason or scope note; needs: description and reason
- **Findings:** R-2198, R-2199, R-2200
- **Suggested fix (R-2198):** After line 703 add: 'The residual cut, needs: one-line description, was left out of the GA version because needs: reason.' In the scope paragraph of §E.4 write: 'One dual-branch design, without the residual cut of the original and adapted to a slowly growing lesion on an anisotropic grid, …'.
- **Status:** open

### G290 · S2 · §E.2 The Moving-Mesh Extension for GA — 91-appendix.tex:740 (p. 112)

~~~text
graph, trails its own single-branch counterpart by 0.031
~~~

- **Verdict:** the fold-2 dual-stencil difference -0.031 is below the single-fold noise level 0.036 (quoted in §E.4) yet reported as "trails" and used in the reach argument
- **Findings:** R-2213, R-2341 (groups merged in: G305)
- **Suggested fix (R-2213):** Line 738-741: "On fold~2, a dual model whose uniform branch uses the dilated stencil ... scores 0.031 below its own single-branch counterpart, within the single-fold noise level of 0.036; no five-fold run and no bypass control exist for this configuration (\S\ref{app:mm-pde:result})." Line 1119: "a difference of $-0.031$, within the single-fold noise level, although higher on only 3 of the 16 eyes". Line 1144-1145: "With the dilated stencil, the uniform branch reaches the front on its own, and in the one fold-2 run the dual model did not improve on its single-branch counterpart."
- **Status:** open

### G292 · S2 · §E.2.1 Data-Free Mesh Mover for GA — 91-appendix.tex:764 (p. 112)

~~~text
$x(\xi) = \xi + \nabla\phi(\xi)$, computed by automatic differentiation.
~~~

- **Verdict:** phi is the full potential in §E.1 (phi = 1/2|x|^2 + psi) but the displacement potential in §E.2.1/§E.3 (x = xi + grad phi, det(I + Hess phi)); the folding statement depends on which; H, M-bar undefined
- **Findings:** R-2223, R-2224, R-2225, R-2226, R-2227
- **Suggested fix (R-2223):** In §E.2.1 and §E.3, write ψ wherever the displacement potential is meant: 'A head maps … to the scalar potential ψ …. The moved mesh is $x(\xi) = \xi + \nabla\psi(\xi)$'. Use $\det(I + \nabla^2\psi)$ in the loss and in det_min. For the convexity term, needs: whether it acts on ∇²ψ or on I + ∇²ψ (the Hessian of φ). Then write 'penalises negative diagonal entries of the Hessian of φ' or '… of ∇²ψ' accordingly.
- **Status:** open

### G293 · S2 · §E.2.1 Data-Free Mesh Mover for GA — 91-appendix.tex:806 (p. 113)

~~~text
proportion to the monitor and 10\,\% uniformly. The mesh mover was trained
on all 478 masks of the cohort, the start mask of every training window of
~~~

- **Verdict:** "all 478 masks of the cohort": the cohort has 553 visits (masks); 478 are window-start masks; "every training window" includes validation eyes
- **Findings:** R-2237, R-2238
- **Suggested fix (R-2237):** Line 806-808: "on 478 of the 553 masks of the cohort, the start masks of all windows of the 75 eyes (the last visit of an eye starts no window)". Line 820: "Training on masks of every eye, including the validation eyes, ...". Table E.1 "Training data": "478 window-start masks, all 75 eyes". Table E.2 and Fig. E.1 captions: "trained on masks of every eye of the cohort" / "trained on 478 masks of the cohort, these three included".
- **Status:** open

### G295 · S2 · §E.2.1 Data-Free Mesh Mover for GA — 91-appendix.tex:823

~~~text
it is given, a property of that mask alone. It never sees a later visit,
~~~

- **Verdict:** "It never sees a later visit": its training masks include later visits of the validation eyes; "does not leak information" asserted, not argued
- **Findings:** R-2247
- **Suggested fix (R-2247):** Replace the sentence with: 'Its weights were also fitted to masks of later visits of the validation eyes, but only to mesh each mask, never to relate one visit to the next. At use, it receives the current mask only, and it is frozen while the solver is trained. Any advantage from this would favour the dual branch, which still shows no gain (§E.4).' Soften l. 820-821 to 'does not give the forecast access to future observations'.
- **Status:** open

### G302 · S2 · §E.4 Result — 91-appendix.tex:1128 (p. 118)

~~~text
not engage in any tested variant: on the moved mesh and on the uniform
grid, without weight decay, and without the gate. The dual-branch model
~~~

- **Verdict:** "did not engage ... without the gate": without the gate the correction entered at full weight and cost 0.173; contradicts the definition of "engage"
- **Findings:** R-2325, R-2326
- **Suggested fix (R-2325):** Rewrite: 'The correction branch did not improve the forecast in any tested variant. With the gate, the gate stayed shut on the moved mesh and on the uniform grid, and on fold 2 also without weight decay. Without the gate, the correction entered at full weight and lowered the change-region Dice on fold 2 by 0.173.'
- **Status:** open

### G303 · S2 · §E.4 Result — 91-appendix.tex:1134

~~~text
A likely reason lies in reach, the property that separates the operators
~~~

- **Verdict:** reach given as "a likely reason" for the shut gate, but in the bypass control the correction branch has the same reach as the uniform branch and its gate stays shut too; "the property that separates the operators" (SV-7.3)
- **Findings:** R-2331, R-2332
- **Suggested fix (R-2331):** "One possible contributing reason, not tested here, lies in reach ... It does not explain the bypass control, whose correction branch has the same reach as the uniform branch and whose gate also stays shut; a second branch that sees the same information as the first adds little in either case. The short-reach graph that §\ref{app:mm-pde:extension} requires for using the gathered nodes is thus also what limits what the branch can add."
- **Status:** open

## Downgraded to S3

Real, but polish or a minor clarity issue. The suggested fixes are in 01-findings.md under the finding IDs.

| Group | Location | Findings | Verdict |
|---|---|---|---|
| G004 | 00-abstract.tex:76 (p. ii) | R-0019 | "annotated by graders" is not wrong, but FAF origin is missing and DE adds "manuell"; minor |
| G005 | 00-abstract.tex:77 (p. ii) | R-0021 | framework "predicts" and "trains"; terminology drift, minor |
| G006 | 00-abstract.tex:93 (p. ii) | R-0037 | RK4 null measured on stencil + FNO only; T-FEN is always RK4-integrated; scope it |
| G008 | 00-abstract.tex:99 (p. ii) | R-0047 | "the Dice" / unnamed scores; name the change-region Dice once more |
| G011 | 00-abstract.tex:169 | R-0062 | DE "entscheidet" stronger than EN "the main difference is" |
| G012 | 01-introduction.tex:21 (p. 1) | R-0097 | "macular" used before macula defined (l.11, 19); "atrophy" gloss optional |
| G016 | 01-introduction.tex:103 (p. 2) | R-0146, R-0151, R-0154 | "instead ..., not a single risk score": X-not-Y returned (AI-1.22); double contrast |
| G018 | 01-introduction.tex:111 (p. 2) | R-0160 | pseudo-cleft opener; style |
| G019 | 01-introduction.tex:116 (p. 3) | R-0164 | "only the operator changes": FENs always run in 45-day RK4 sub-steps; state the exception |
| G022 | 01-introduction.tex:155 | R-0181, R-0182 | pushforward curriculum undefined in Ch. 1; "Delta t-scaled" vs "Delta t-conditioned" |
| G029 | 02-background.tex:7 (p. 5) | R-0211 | Ch. 2 first sentence is generic; map follows (E1) |
| G032 | 02-background.tex:85 (p. 5) | R-0232 | §2.1.1 carries many forward pointers; model input stated twice (l.114-116, l.122-125) |
| G034 | 02-background.tex:111 | R-0241, R-0242 | Fig. 2.4 cited in §2.1.1 before Figs 2.2/2.3, placed in §2.1.3: numbered out of citation order |
| G035 | 02-background.tex:112 (p. 6) | R-0245 | padded 50-word sentence; depth maps before A-scans are introduced |
| G036 | 02-background.tex:187 (p. 7) | R-0256 | verified: "(MUW)" expanded only in §3.1 (03-data.tex:28); used at 02-background l.187 |
| G043 | 02-background.tex:275 (p. 10) | R-0293 | "forward problem of each step" jargon before §2.2 |
| G045 | 02-background.tex:322 (p. 11) | R-0303, R-0304 | Fig. 2.3 (FAF) cannot show the missing outer-retinal complex; "rather than" contrast |
| G046 | 02-background.tex:346 (p. 11) | R-0316 | slab / coronal section undefined |
| G047 | 02-background.tex:348 (p. 11) | R-0317 | whether iRORA counts as 1 or 0 in the mask is unstated; needs: mask labelling of iRORA |
| G049 | 02-background.tex:368 (p. 11) | R-0331 | square-root enlargement rate used before §2.5.1 explains it |
| G050 | 02-background.tex:383 (p. 12) | R-0337 | "The experiments ask" (SV-5.11 pattern) |
| G057 | 02-background.tex:652 (p. 16) | R-0395 | error accumulation and MP-PDE opened, set aside, resumed later |
| G058 | 02-background.tex:656 | R-0399 | "operator" switches to the narrow neural-operator sense in l.656-677 before §2.5.2 separates the senses |
| G061 | 02-background.tex:676 (p. 16) | R-0413 | "well-known ... consistently poor" without citation; Brandstetter says only "not designed to generalize" |
| G062 | 02-background.tex:679 (p. 16) | R-0406, R-0414, R-0415 | clinical visit-schedule argument in the solver background, repeated in §2.5.1 (M3); incl. G060 |
| G064 | 02-background.tex:683 (p. 16) | R-0423 | "horizon set by the clinic rather than by the model" mixes horizon and visit schedule |
| G066 | 02-background.tex:704 (p. 17) | R-0431 | "make its errors small rather than correct them" is a slogan; needs: Brandstetter's stated reason |
| G069 | 02-background.tex:752 | R-0455, R-0456 | no Related Work group on comparisons of neural PDE surrogates; needs: one or two benchmark studies |
| G072 | 02-background.tex:805 (p. 18) | R-0474, R-0475 | Lindner border classes undefined |
| G076 | 02-background.tex:819 (p. 18) | R-0488 | forward pointer: "RK-integrated operators of this thesis are related" says neither what they are nor how they differ |
| G077 | 02-background.tex:829 | R-0494 | "tighter registration bounds" unexplained (first use of registration); needs: what was registered and the bound |
| G078 | 02-background.tex:833 | R-0497 | §2.4.2 ends on Salvi after the closest-work paragraph; no closing |
| G080 | 02-background.tex:864 (p. 19) | R-0510 | Fisher-Kolmogorov, FET-PET, inverse problem unexplained |
| G082 | 02-background.tex:896 (p. 20) | R-0524 | §2.5.1 claim first appears in paragraph 5; multi-channel and covariate properties introduced and dropped; "these four points" ambiguous |
| G085 | 02-background.tex:975 (p. 21) | R-0562 | Delta t -> 0 limit stated without the boundedness assumption of §4.2.1; default persistence comes from the zero-init (SV-4.3) |
| G090 | 03-data.tex:73 (p. 24) | R-0634 | consequences of the FAF-based mask (not cRORA; FAF near the fovea) not stated |
| G091 | 03-data.tex:177 (p. 25) | R-0654, R-0655, R-0656 | Henle's fibre layer, outer photoreceptor layer unexplained; 80-word list sentence; IS/OS vs EZ not linked |
| G092 | 03-data.tex:201 (p. 25) | R-0657 | what the outer boundary channels hold inside the lesion is unstated; needs: segmentation behaviour inside GA |
| G093 | 03-data.tex:267 | R-0693 | zero-padding paragraph: dramatic opener, "zero means no signal" contradicted by its own examples |
| G096 | 03-data.tex:420 (p. 29) | R-0740 | budget counts depend on §4.2.5 definitions; 540/720-day budgets unused |
| G097 | 03-data.tex:422 | R-0743 | "none can chain two visits" reads against the 90-day intervals of Table 3.1; means two intervals |
| G099 | 03-data.tex:454 (p. 29) | R-0763 | "arms" used in §3.7 before §4.1 defines it (X6) |
| G104 | 04-method.tex:47 (p. 31) | R-0794 | Dice and IoU used in §4.1 before §5.1 defines Dice; IoU never used again |
| G109 | 04-method.tex:220 | R-0854, R-0855 | B = batch size and time budget; t = time and target mask |
| G113 | 04-method.tex:482 (p. 36) | R-0898 | "Each was chosen to isolate one property": cross-class pairs (U-Net vs GNN) differ in many respects (§5.4 says so) |
| G119 | 04-method.tex:703 | R-0930 | Table 4.2 names both graphs before §4.3.3 defines them; N(i) graph unstated in Eq. 4.6 |
| G121 | 04-method.tex:772 (p. 41) | R-0944, R-0945 | slogan closers ("restores connectivity but not reach", "The design thus derives ...") |
| G125 | 04-method.tex:1044 (p. 45) | R-0994 | Courant number given as "velocity times the step" (a length), limit 2.4 is unitless; spacing missing |
| G131 | 05-experiments.tex:58 (p. 50) | R-1059 | metrics/anchor as agents ("the clinical metrics only ask", SV-5.11) |
| G133 | 05-experiments.tex:67 (p. 51) | R-1068, R-1069 | "X, not Y" closers (l.67, l.184, Fig. 5.3 caption) |
| G134 | 05-experiments.tex:89 | R-1075, R-1076 | C reused for the change region (C = 11 channels); b, p, y not tied to §2.5.2 notation; z vs bold z |
| G135 | 05-experiments.tex:138 (p. 51) | R-1081 | growth-region Dice introduced, then defined after an intervening paragraph; "eye counts" stated three times |
| G140 | 05-experiments.tex:301 | R-1127 | main-text sigma_Delta = sqrt2 sigma / sqrt5 gives a U-Net bar of about 0.024, not the stated 0.020 (which needs the App. C.3 formula) |
| G145 | 05-experiments.tex:308 | R-1134 | fold numbers use change-region Dice, eye counts growth-region Dice, joined in one clause |
| G150 | 05-experiments.tex:464 | R-1170 | "this lead is real": undefined verdict word; no z or t given unlike the neighbouring comparisons |
| G152 | 05-experiments.tex:542 (p. 57) | R-1196 | Table 5.2 caption implies nine operators; the k = 20 row is missing; caption does not say so |
| G161 | 05-experiments.tex:639 (p. 58) | R-1234 | "The first/second/third/fourth question is whether" template (SV-5.11) |
| G162 | 05-experiments.tex:668 (p. 59) | R-1249 | §5.4 quotes no z although §5.1.5 uses this very sentence with z = 7.9 as template |
| G163 | 05-experiments.tex:673 (p. 59) | R-1256 | reach-ladder variants get numbers but no verdict; ladder ran at one seed, so none is established by §5.1.5 |
| G164 | 05-experiments.tex:747 (p. 60) | R-1270, R-1271 | "Reach along the rows therefore decides" overstates; rows +-2 gives the largest drop; slogan closer "so it lay in the graph" |
| G171 | 05-experiments.tex:841 (p. 61) | R-1306 | forward pointers to §5.6.3 and §5.7.2 carry part of the argument |
| G174 | 05-experiments.tex:899 (p. 61) | R-1322, R-1324 | "Two of the tested properties improve an operator" omits spatial context (0.0000 -> 0.4515); say that reach and transport add to an operator that already has context |
| G178 | 05-experiments.tex:923 (p. 62) | R-1343, R-1344 | "these properties" grammatically points to spatial context and the local path; 0.06-0.07 meant for reach and transport |
| G183 | 05-experiments.tex:993 | R-1376, R-1380, R-1381 | reach in mm (0.24 mm) in §5.5 and Fig. 5.5, in µm in §5.4; column counts without µm (X4) |
| G186 | 05-experiments.tex:1045 (p. 64) | R-1400, R-1401, R-1403 | under-prediction (35/48 eyes, 0.73) first given in §6.2; Ch. 5 points forward to the Discussion for a result |
| G193 | 05-experiments.tex:1138 | R-1454 | previews the step-size result of §5.7.1 before it is introduced |
| G194 | 05-experiments.tex:1172 (p. 65) | R-1460, R-1461 | "three runs ... test which of its parts carry the result" (SV-5.11); ambiguous "its" |
| G195 | 05-experiments.tex:1229 (p. 54) | R-1474 | text counts "lower on all five folds and on 56 of 75 eyes" while Table 5.4 counts higher (0/5, 19/75); forms vary |
| G196 | 05-experiments.tex:1241 (p. 66) | R-1488, R-1489 | raw mask RMSE (1.10 vs 0.51) used as evidence although §5.1.1 says no RMSE is used as evidence; "No thresholded metric is affected" reads against the +0.050 |
| G202 | 05-experiments.tex:1451 (p. 68) | R-1550, R-1553 | "rather than" closer that names a cause and says it was not tested; capacity conclusion ends on a side issue |
| G203 | 05-experiments.tex:1543 (p. 69) | R-1556 | "Their results decide which statements ... can be made" (personification); section openers without thesis statement |
| G206 | 05-experiments.tex:1588 | R-1571 | step-size test re-evaluates trained weights only; say that no network was trained with a finer step (SV-5.12); needs: author confirmation |
| G208 | 05-experiments.tex:1640 (p. 70) | R-1589, R-1590, R-1591 | "not because the finer steps forecast better" reads against +0.018 on folds 0-1; X-not-Y closer (X3) |
| G211 | 05-experiments.tex:1765 | R-1610, R-1647 | float order in §5.7: Fig. 5.8 cited before 5.7, Tables 5.6/5.7 print pages later (SV-5.14) (incl. G215) |
| G214 | 05-experiments.tex:1896 (p. 73) | R-1643 | energy-conserving form called "stable" while the mask Courant (2.64) is above the RK4 limit (2.4) with slow growth; say "passes the stability criterion" |
| G223 | 05-experiments.tex:2180 (p. 78) | R-1707 | the wrapper arm is said to integrate "over several sub-steps" but takes one RK4 step per interval (four evaluations) |
| G228 | 06-discussion.tex:53 | R-1748 | staccato verdict openers ("Its parts do not matter equally.", "More reach does not keep helping.", "Global context behaves differently.") |
| G229 | 06-discussion.tex:55 (p. 80) | R-1751 | §6.1 meant to stand alone, but "canonical network", z (not bold), "soft-Dice", "arms" unexplained there (SV-6.1) |
| G230 | 06-discussion.tex:65 (p. 81) | R-1755 | "The update needs the length of the interval": no run removed the interval, so necessity was not measured |
| G231 | 06-discussion.tex:67 (p. 81) | R-1757 | "..., not in general" contrast closer (X3) |
| G232 | 06-discussion.tex:70 | R-1759 | discussion does not relate the operator results to Gupta 2023, Liu-Schiaffini 2024 or Lachinov 2024 |
| G234 | 06-discussion.tex:84 (p. 81) | R-1777 | "reach along the direction in which the lesion front moves" suggests directional growth; it is reach along a grid row |
| G236 | 06-discussion.tex:89 (p. 81) | R-1785 | "a T-FEN with fewer parameters than that control scores the same" can be read as "same as the control" |
| G238 | 06-discussion.tex:108 (p. 81) | R-1797 | "suggestive" + "a more specific statement than a ranking of architectures" (slogan closer, SV-7.5) |
| G239 | 06-discussion.tex:113 (p. 81) | R-1800 | "on the verge of being the best operator", "would most likely decide the order": story-like; the z = 2.1 rests on the GNN sigma (see G139) |
| G241 | 06-discussion.tex:142 | R-1808 | reach in columns only, after the paragraph before converted to µm (SV-6.2) |
| G243 | 06-discussion.tex:155 (p. 82) | R-1813 | "lies above/below the U-Net", "catches up" (SV-7.4) |
| G245 | 06-discussion.tex:197 | R-1823 | "focality" undefined |
| G246 | 06-discussion.tex:211 (p. 83) | R-1828, R-1829 | "Neither is more accurate than the canonical network" while §6.1.2 has the T-FEN +0.017 (not established) |
| G249 | 06-discussion.tex:230 (p. 83) | R-1842 | "correction branch never engaged" is appendix jargon in the main text; Ch. 7 adds "because" |
| G253 | 06-discussion.tex:255 | R-1858 | "still notable that a model given the segmented lesion is weaker": omits rate definition and cohort-size differences listed in §5.8 |
| G255 | 06-discussion.tex:293 (p. 84) | R-1874 | treatment status of the cohort during follow-up never stated; needs: whether any eye received a complement inhibitor or was in a trial |
| G256 | 06-discussion.tex:295 (p. 84) | R-1876 | §6.2 reduces the treatment decision to growth speed; §1.1 says both decisions need where and how fast |
| G264 | 07-conclusion.tex:24 | R-1938 | participle opener "trained with a plain MSE, the canonical operator ..." (SV-7.2); canonical operator/model naming |
| G267 | 07-conclusion.tex:75 (p. 77) | R-1960 | Ch. 7 comparison with prior work drops the caveats of §5.8 (input, RORA, FAF, regression target) |
| G272 | 91-appendix.tex:80 (p. 98) | R-2046, R-2047 | pseudo-cleft "Where the model fails more clearly is discussed in" (X3) |
| G276 | 91-appendix.tex:159 (p. 100) | R-2080, R-2081 | "the local operators score about the same on both groups": the one-hop floor differs by 0.024, about as much as the U-Net (-0.028); U-Net called "global" here, "dense" in §5.5 |
| G284 | 91-appendix.tex:529 (p. 108) | R-2158 | "data variant" undefined (App. D) |
| G285 | 91-appendix.tex:609 (p. 110) | R-2175 | App. E opener frames the experiment as a test of mesh adaptation, which §E.4 later withdraws |
| G286 | 91-appendix.tex:618 (p. 110) | R-2181 | placement reason "gave no measurable gain" (SV-4.2 open with the author); "may not suit the present setup" vague |
| G288 | 91-appendix.tex:727 (p. 112) | R-2204 | alpha alone does not measure the size of the correction (alpha*g is invariant to rescaling); "open/shut" without threshold; the bypass comparison is the real evidence |
| G289 | 91-appendix.tex:738 (p. 112) | R-2211 | §E.2 intro mixes design choices, the k-NN reason and a fold-2 result; -0.031 stated three times |
| G291 | 91-appendix.tex:747 | R-2215, R-2217 | "native 49 x 1024 grid" contradicts Ch. 3, where native means each visit's own grid (AI-S19) |
| G294 | 91-appendix.tex:815 | R-2242 | "edge gain" used with values before §E.3 defines it |
| G296 | 91-appendix.tex:825 (p. 113) | R-2249 | "no held-out set needed" is followed by the admission that predicted masks were never scored; subsection ends on an unrelated fact |
| G297 | 91-appendix.tex:999 (p. 115) | R-2297 | Table E.2 has one row; the four ablation values sit in prose; base configuration of the ablations unclear |
| G298 | 91-appendix.tex:1016 (p. 116) | R-2301 | "produces valid meshes ... a defective mesh does not explain the result" covers unscored meshes on predicted masks; the bypass control is the stronger argument |
| G300 | 91-appendix.tex:1094 (p. 117) | R-2315 | the gate trajectory, called the instrument, is reported only as ranges in one sentence; no figure |
| G301 | 91-appendix.tex:1113 | R-2320 | three fold-2 variants against different references; "its counterpart" unnamed for the weight-decay run |
| G304 | 91-appendix.tex:1139 | R-2335, R-2336, R-2337, R-2338, R-2339, R-2340 | "up to about 23 columns" presents the 90th percentile as a maximum; columns without µm (X4) |
| G306 | 91-appendix.tex:1147 (p. 118) | R-2343 | slogan-like closer ("The result therefore concerns this method on this task"); double negation |

## Dropped

- G020 (R-0172, 01-introduction.tex:139 (p. 3)): Ch. 4 = part 1 mapping is the author's decision (review v6 #11; AI-S2 addressed)

