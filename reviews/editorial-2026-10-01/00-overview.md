# Editorial review of the thesis (build of 2026-10-01)

Scope: the English abstract, Chapters 1–7 and Appendices A–G, as they render in `main-thesis.pdf` of 2026-10-01 (21:46). The German Kurzfassung was not reviewed; changes to the abstract need to be mirrored there. Following the brief, citations, references, formatting and the accuracy of numbers were **not** checked; every suggested rewrite keeps them unchanged. The review is advisory: rewrites are given for single sentences, and structural points are given as suggestions, not as rewritten sections.

**How it was made.** The text was split into 14 slices. Each slice was reviewed by one editor against the four criteria of the brief (flow, clarity, tone, AI tone), with the GPTZero scan of that chapter alongside, so that every flagged sentence could be read in context. A second, adversarial reviewer then checked every finding. It confirmed that the quoted text exists and is rendered, compared each rewrite with the original for meaning, hedges and scope, numbers, citations, `\ref`s and the passive-voice rule, dropped taste-only edits, and added clear misses. Of 545 findings, 35 were dropped and 34 were added, leaving **544**. Three further reviewers read the whole thesis: one for structure and narrative, one as a first-time examiner marking where a reader gets lost, and one analysing the recurring patterns behind the GPTZero flags. A final mechanical check confirmed three things. Every quoted passage exists verbatim at the stated line, outside `%` comments and `\iffalse` blocks. No rewrite adds "we", "our" or an em-dash. No rewrite drops a citation, `\ref` or number, except where the item is explicitly a move or a cut.

**Reading the items.** IDs such as `5d.4` refer to the micro files listed in the index below; `S`, `T`, `R`, `L` and `P` refer to the structure, transition, repetition, reader and pattern items further down this page. Severity: **high** = a reader is likely to misread or get lost, or the text is broken; *medium* = clearly clunky, over-long, or a flagged sentence with a concrete tell; *low* = polish. Of the 544 micro items, 15 are high, 277 medium and 252 low. 460 of them sit in passages GPTZero flagged, 71 in passages it judged human.

---

# Fix first (before any wording pass)

These are not style questions. Each one breaks the text for a reader or contradicts another part of the thesis.

1. **Two sentences are lost in the PDF.** Prose was appended to the end of a `%` comment line, so LaTeX drops it:
   - `05-experiments.tex:163` (§5.1.3) — the PDF reads "… is mostly the luckiest one. eyes on which it would be reported." The second of the two announced reasons is missing. → **5a.19**
   - `05-experiments.tex:903` (§5.4.2) — the PDF reads "… and a higher score. in §4.5.1: the raw mask error …". → **5c.17**

   A scan of all chapters for this pattern found no other instance. The fix is a line break after each comment.
2. **Contradictions between chapters** that an examiner will notice:
   - Mask provenance. §2.1.2 says the OCT signatures "define the lesion mask used as channel 0", and §2.1.3 argues for OCT over FAF. §3.1 says the mask was annotated on FAF. → **2a.17**, **S5**
   - Covariates. §1.2 promises that the covariates are "tested in this thesis", but that subsection is commented out of Chapter 5, and §6.3 says their value "is not settled". → **1.27**, **S4**
   - Layer channels. §2.1.5 calls them "not auxiliary context", while §3.2, §4.2.2 and §4.5.1 call them "auxiliary targets". The Figure 2.2 caption maps anatomical strata onto the ten channels, whereas §6.3 says the boundary names are unknown. → **S9**
   - Two pointers lead nowhere. §2.1.1 refers to §1.2 for subfoveal significance, but the point is made in §1.1. §3.7 promises that fold heterogeneity is "revisited in §5.1", which does not happen. → **S22**
3. **Wording that changes what a result says:**
   - The C2 criterion of the solver-swap test can be read so that the RK4-trained network fails it. → **5d.4**
   - "Its accuracy" in §5.5.2 points at the seed-7 run, but the numbers are the seed-42 comparison. → **5d.16**
   - Pearson *r* is described as checking whether the model "scales" growth speeds correctly, which *r* does not measure. → **5d.23**
   - The seven interleaved transport meshes of the T-FEN read as one subsampled mesh. → **4b.25**
   - The opener of the objective test says each run changes one part, but the first run changes two. → **5c.11**
4. **Core terms used before they are defined, or with several meanings:**
   - *arm*: never defined; first used at `04-method.tex:46`.
   - *canonical*: names a fold, a normalisation, an age mode and the model.
   - *the same deficit*: used in the abstract and §1.3, defined only in §5.3.5. → **1.8**, **1.41**
   - *window*: the crop in §3.3, a pair of visits in §3.5–§3.6. → **3.25**
   - *floor*, *anchor*, *late epochs* and *instrument* are also affected.

   One short definitions paragraph at the end of §4.1, plus a definition of "canonical fold" at its first use in §3.4, would remove most of this. See the terminology table and **S19**.

---

# Part 1 — Macro feedback

## Overall flow and structural integrity

The thesis reads as one argument, and its large-scale path is sound: research question, background, data, framework and operators, experiments, discussion, conclusion. The end answers the beginning: §6.1 and Chapter 7 are organised by the two sub-questions of §1.3. The strongest stretch is the technical middle. Chapter 3, the graph-construction argument of §4.3.3 (physical *k*-NN fails, index-space *k*-NN fixes connectivity but not reach, the dilated stencil follows from the front-advance scale) and the step-by-step build-up of §5.3 all read well. §5.5.1 is a model for the other result sections: it states its criteria before its results. Claims are scoped consistently, and a claim is withdrawn wherever the second seed does not replicate it.

The structure weakens in five places:

- **The research-question mapping does not match the text.** §1.3 says Chapter 4 answers sub-question (1) and Chapter 5 answers (2). Chapter 4, however, never names sub-question (1), and it spreads the framework over §4.2, §4.4 and §4.5 with the 13-page operator section in between. The evidence for the framework answer is in Chapter 5 (§5.4.1, §5.4.2), filed under "Negative Results", although §5.4.2 holds the clearest *positive* framework result of the thesis. → **S2**, **S3**, **S7**
- **Material is repeated across chapters.** The cohort facts and the crop census appear in §2.1.6, §3.1/§3.3, §6.3 and Appendix A. The continuous-time caution appears four times, the Mai et al. caveats about seven times, and the batch-statistics argument four times within Chapter 4. Every seed-7 number sits inline in Chapter 5 although Table E.3 repeats them, and that table is never referenced. The repetition makes the longest chapters dense, and it makes the headline read as restated rather than built. → **R1–R17**
- **The method/results boundary is blurred.** Chapter 4 announces outcomes: "turns out to be the most consequential design decision", "The Galerkin form turned out to be unstable", the solver-swap verdict. It also justifies a design choice with a data fact (ground-truth shrinkage) that is first quantified in §6.3. → **S8**, **S13**
- **Chapter 2 introduces learned solvers twice.** They appear in §2.2.4, then the GA argument (§2.2.5), then again with a different taxonomy in §2.3. §2.1 (about 8 pages) duplicates Chapter 3, while §2.3 is short. → **S17**, **S25**, **T8**
- **Chapter 5 ends on cost.** Its last sentence is that inference time was not measured. The answer to sub-question (2) sits eight pages earlier, in §5.3.5. §5.6 is titled "Qualitative Analysis and Clinical Comparison" but contains only the Mai et al. comparison. → **S12**, **T6**, **T12**

Almost all of this can be fixed by moving, cutting, relabelling or adding a signpost; none of it needs new content.

## Reader flow and logical path

Within chapters, the transitions are mostly explicit, and §5.3 shows how well that works: §5.3.1 ends with "This motivates the next comparison". The places where a reader gets lost are mostly about vocabulary, not argument (see the terminology table). The project's working terms arrive before their definitions, and several carry two to four meanings. The reader is also asked to accept results on credit. "The same deficit" appears in the abstract, §1.3 and §5.2, but is explained only in §5.3.5. §1.2 announces that the next section "motivates such a framework", yet §1.3 first argues about the operator. Chapters 2, 3 and 4 open without saying what they contribute to the research question, whereas Chapters 5, 6 and 7 do (**S15**). Where the micro files mark a missing bridge, they give the sentence to insert.

## Clarity and sentence structure

The most common micro finding is clarity: 375 of the 544 items. Four patterns account for most of it:

- **Sentences built on a semicolon or a colon** that join two separate claims: about 190 of each in running prose. The sentences GPTZero judged human have 16 words on average, the flagged ones 21, and 18.5 % of the flagged sentences run to 30 words or more. Split at the semicolon when the second clause makes a new claim.
- **Em-dash asides** that separate subject and verb or carry a list: 63 dashes, most of them in Chapter 2. Use parentheses for definitions and lists, and a new sentence for a claim.
- **The statistics template in Chapter 5**: "X against Y gives Δ = … SE (k/5) and per eye … (m/75, t = …)", often three or four times in a row. The verdict arrives at the end of a number chain. This coincides with the reporting-scheme pass already planned in NOTES.md (#23): give the outcome in words first, then the numbers once. → **S6**, **P14**
- **Pronouns without a clear referent** ("It", "This", "these two") at the start of a sentence after a sentence that names two things. Several high items are of this kind.

## Academic tone and style

Chapters 3–7 are written in a plain, objective register that fits the house style. Three passages read like a different author: §2.1, §2.3 with the related work, and Appendix G.1. All three are older drafts, and they carry explanatory asides ("can be thought of as a biological camera", "takes some getting used to", "Put differently"), intensifiers ("fundamentally" five times, "crucially", "entirely", "precisely", "inevitably") and survey phrases ("sits at the intersection of", "broadly separate into two paradigms"). Revising them as units gains the most for the least effort. Appendix G.1 matters especially, because it is the first page an examiner reads in the moving-mesh appendix. → **S18**, **P9**, **P13**

Elsewhere the tone problems are idioms and abstractions that act: "buys", "bought nothing", "earns", "lever", "pays off", "luckiest", "two tests ask this", "two arguments speak against", "the objective decides". The same holds for slogan-style run-in headings in Chapters 6–7: "The operator: ingredients, not classes.", "Where modelling effort pays.", "Good at where, weaker at how fast.", "Take-away." → **P10**, **P12**

## AI tone (GPTZero flags)

GPTZero rates every chapter "AI Generated" and flags 67 % (Ch. 1) to 89 % (Ch. 7) of the words. It also flags 82 % of the plain, procedural Chapter 3, and it labels the same construction "human" in one place and "AI" in another. The flags are therefore not evidence on their own; they were used here as a pointer to passages worth reading closely. Classic AI vocabulary (delve, multifaceted, testament, pivotal, leverage, moreover) is essentially absent from the thesis. What the flagged passages share is rhetoric and structure, and the most frequent devices are:

1. **Contrast frames used as the claim** ("not X but Y", "X, not Y", "rather than"): about 90 in total, about 25 of them evaluative or paragraph-closing. → **P1**
2. **Paragraph-final verdicts that restate the paragraph**, usually with "therefore" (about 40). → **P2**
3. **Clefts and pseudo-clefts** ("What the framework needs, in short, is …", "This is what made … possible at all"): about 30. → **P3**
4. **Mirrored verdict pairs and parallel catalogues** ("The framework transferred. The operator class did not decide the outcome; a small number of properties … did."): about 25. → **P4**
5. **Chains of consequence connectives**: 71 "therefore" and about 108 ", so". Flagged sentences carry "therefore" or "thus" three times as often as human-judged ones. → **P6**

The sentences GPTZero judged human differ less in vocabulary than in what they *do*. They report something specific: what a source found, what was done to a file, what a probe measured, or a dated correction. They also state limitations flatly ("The comparison is not like-for-like."). The flagged sentences interpret, generalise, announce or summarise. Under the passive-voice rule, the most effective lever is a concrete grammatical subject: a table, a fold, a run, a source, a date. Such a subject replaces the abstract "The X is Y" frame and makes "we" unnecessary. The rules of thumb at the end of this page turn this into a checklist. The aim is clearer, more grounded prose. A lower detector score may follow, but chasing it is not a useful test, because precise technical prose with fixed terms and numbers is predictable by nature.

## Suggested order of work

1. The four "Fix first" groups above (an hour or two).
2. The structural decisions that change where text lives: **S2/S3** (the research-question mapping and the §5.4 heading), **S7** (the framework spread over Chapter 4), **R1–R17** (decide one home for each repeated block) and the planned reporting-scheme pass for Chapter 5 (**S6**). Sentence edits in passages that will be moved or cut can then be skipped.
3. A definitions paragraph in §4.1 and one fixed name per arm (terminology table).
4. The three older-draft passages as units: §2.1, §2.3 plus related work, and Appendix G.1.
5. The micro files in source order, high and medium items first. The low items are polish.


## Index of the micro-feedback files

| Part | File | Findings | high / medium / low |
|---|---|---:|---|
| 1 | [Abstract (English) + Ch. 1 Introduction](01-abstract-introduction.md) | 43 | 3 / 26 / 14 |
| 2a | [Ch. 2 Background, §2.1 GA and OCT imaging](02a-background-ga-oct.md) | 38 | 2 / 23 / 13 |
| 2b | [Ch. 2 Background, §2.2-§2.4 PDEs, neural solvers, related work](02b-background-solvers-related-work.md) | 46 | 2 / 22 / 22 |
| 3 | [Ch. 3 Data and Preprocessing](03-data.md) | 36 | 1 / 15 / 20 |
| 4a | [Ch. 4 Method, §4.1 Overview, §4.2 Fixed Framework, §4.3.1-4.3.2 (contract, GNN)](04a-method-framework-gnn.md) | 37 | 0 / 21 / 16 |
| 4b | [Ch. 4 Method, §4.3.3-4.3.8 (graph construction, dense operators, floors, FEN, RK, parameter matching)](04b-method-operators.md) | 48 | 1 / 23 / 24 |
| 4c | [Ch. 4 Method, §4.4 Conditioning, §4.5 Training, §4.6 Implementation](04c-method-conditioning-training.md) | 26 | 0 / 9 / 17 |
| 5a | [Ch. 5 Experiments, §5.1 Evaluation Protocol, §5.2 Arm Table](05a-experiments-protocol-arm-table.md) | 40 | 1 / 17 / 22 |
| 5b | [Ch. 5 Experiments, §5.3 Ingredient Study](05b-experiments-ingredients.md) | 34 | 0 / 15 / 19 |
| 5c | [Ch. 5 Experiments, §5.4 Negative Results](05c-experiments-negative-results.md) | 30 | 2 / 16 / 12 |
| 5d | [Ch. 5 Experiments, §5.5 Validity Diagnostics, §5.6 Qualitative/Mai comparison, §5.7 Computational Cost](05d-experiments-validity-mai-cost.md) | 45 | 3 / 18 / 24 |
| 6-7 | [Ch. 6 Discussion + Ch. 7 Conclusion](06-07-discussion-conclusion.md) | 56 | 0 / 31 / 25 |
| A | [Appendices A-F (dataset details, derivations, hyperparameters, rollouts, ablation details, code structure)](09a-appendices-A-F.md) | 14 | 0 / 8 / 6 |
| G | [Appendix G The Moving-Mesh Extension (MM-PDE)](09b-appendix-G.md) | 51 | 0 / 33 / 18 |
| | **Total** | **544** | 15 / 277 / 252 |


---

# Part 1 (detail) — Structure and narrative

The thesis reads as one argument: a fixed, Δt-conditioned framework with one operator slot, a controlled survey through that slot, and an ingredient reading of the results. The Discussion and Conclusion return explicitly to the two sub-questions of §1.3. The middle of the thesis is its strongest part (Ch. 3, §4.3.3, §5.3, §5.5.1): short declarative sentences, explicit bridges between subsections, and every claim scoped. Readability drops in three kinds of place. (1) The research-question mapping does not match what the text does. Chapter 4 never names sub-question (1). The framework is defined across §4.2, §4.4 and §4.5 with the 13-page operator section in between. The evidence for the framework answer comes from Chapter 5 (§5.4.1 and §5.4.2), and it is filed under "Negative Results" although §5.4.2 holds the clearest positive framework finding. (2) The same explanations and caveats recur across chapters: the crop census four times, the continuous-time caution four times, the Mai caveats about seven times, and the cohort facts both in §2.1.6 and in Ch. 3. Chapter 5 also carries every seed-7 number inline, while Table E.3 repeats them and is never referenced. As a result the longest chapter is dense, and the headline claim reads as restated rather than built. (3) The logical path breaks in a few places. Two sentences are lost to LaTeX comments in the rendered PDF (§5.1.3 and §5.4.2). Results are announced in the Method chapter. A data fact (ground-truth shrinkage) is first quantified in the Discussion, although Ch. 4 and Ch. 5 rely on it. Two promises are not kept (covariates "tested in this thesis"; fold heterogeneity "revisited in §5.1"). Background and Data contradict each other twice (an OCT-defined mask vs the FAF annotation; layer channels "not auxiliary" vs "auxiliary targets"). The register is plain and consistent in Ch. 3–7 but shifts in §2.1 (analogies, explanatory asides), in §2.3–§2.4 and in Appendix G.1 (intensifiers such as "fundamentally", "crucially", "entirely"); these passages read most like a different author. Almost all of this can be fixed by moving, cutting, relabelling or signposting, without new content.

**Hourglass shape.** The hourglass is mostly respected, but material leaks at both ends of the narrow part. Ch. 1 narrows correctly from epidemiology (§1.1) to the problem (§1.2) to the research question. The narrowest statement, however, sits mid-section after an equation, under a heading ("Why Neural PDE Solvers?") that does not announce it. Ch. 2 widens again (eye anatomy), as a background chapter should. It also carries narrow, cohort-specific material (§2.1.6: native grids, spacing, crop census) and design arguments (§2.2.5) that belong to the technical middle and are repeated there. Ch. 3–5 have the intended depth, but the boundary between method and results is blurred. Ch. 4 announces outcomes ("turns out to be the most consequential design decision", 04-method.tex:470; "The Galerkin form turned out to be unstable", :788; the solver-swap verdict, :876–885), and it justifies a design choice with a data fact that is first quantified in §6.3. The narrow part ends weakly: Chapter 5 closes on computational cost (§5.7, last sentence on unmeasured inference time) rather than on the answer to sub-question (2), which sits in §5.3.5 eight pages earlier. Ch. 6 broadens back out. It sets the results against the CFL expectation of §2.2 and the low-data argument of §1.3, and it closes the clinical loop with §1.1 (growth speed and treatment decisions). It reaches the wider field only in its last sentence ("a new disease-forecasting task of this kind"). The findings are not set against the neural-PDE literature that §2.3 introduced (the U-Net as a standard strong surrogate, the over-smoothing claim for spectral operators, solver invariance after Ott et al.); one paragraph in §6.1 would complete the upper half of the hourglass. Ch. 7 ends on the broadest take-away, as it should. One loop stays open: §1.2, §2.1.5 and §3.2 argue at length that the ten layer channels are needed, but no later chapter tests this or says that it was not tested.

**What already works.**

- The research question is stated once, with two sub-questions (01-introduction.tex:176-195), and restated at the openings of Ch. 5, Ch. 6 and Ch. 7. §6.1 and Ch. 7 are organised by the two sub-questions, so the end of the thesis visibly answers its beginning.
- §4.3.3 (graph construction) is a complete logical chain: the physical k-NN graph fails, the index-space k-NN graph fixes connectivity but not reach, and the dilated stencil is derived from the front-advance scale. Figure 4.2 shows the chain, and §5.3.2 then tests exactly that design choice. This is the best-argued passage of the thesis.
- §5.3 builds step by step with explicit bridges: §5.3.1 ends with 'This motivates the next comparison', and §5.3.2 explains the earlier U-Net result. §5.3.5 then synthesises instead of listing.
- §5.5.1 states its criteria before its results (What is tested / Principle and criteria / Setup / Results / What follows). The other result sections could follow this pattern.
- Claims are scoped consistently and withdrawn when the second seed does not replicate. The global+local result is treated the same way in §5.3.3, §5.3.5, §6.1, Ch. 7 and the abstract.
- MM-PDE is cleanly contained in Appendix G, with at most one pointer per chapter. Appendix G has its own complete arc (background → design → mesh quality → result → outlook).
- Ch. 3–5 use a plain, declarative register with short sentences and concrete subjects, which matches the house style and is markedly easier to read than §2.1 or Appendix G.1.
- The clinical loop closes: §1.1 motivates identifying fast progressors for complement-inhibitor treatment, and §6.2 returns to it and states plainly that growth speed is the weaker capability.

## Structural issues

**S1** [**HIGH**] **§5.1.3 Rollout and Reporting, 05-experiments.tex:161-164; §5.4.2 The Objective, 05-experiments.tex:901-904.** In both places, prose was appended to the end of a % comment line, so it is missing from the PDF. The rendered text reads '... so the highest epoch is mostly the luckiest one. eyes on which it would be reported.' (the second of the 'two reasons' is lost) and '... adds an immediate escape and a higher score. in §4.5.1: the raw mask error ...'. A reader loses the argument at exactly the point where the reporting rule and the calibration cost are justified.  
*Suggestion:* Move 'Second, the highest epoch is chosen on the same validation' (end of 05:163) and 'Its cost is the stretch of the raw mask regression described' (end of 05:903) onto their own lines after the comments. A scan of all chapters found no other instance (02-background.tex:920-922 is harmless).

**S2** [**HIGH**] **Research-question mapping: 01-introduction.tex:192-195 and 219-222; 05-experiments.tex:18-21; 04-method.tex (no mention); 06-discussion.tex:22-49.** The text says Chapter 4 answers sub-question (1) and Chapter 5 answers (2). In fact, Chapter 4 constructs the framework without naming the question, Chapter 5 tests the framework (§5.4.1 time handling, §5.4.2 objective), and §6.1 draws its answer to (1) from those Chapter 5 results. A reader looking for the answer to (1) in Chapter 4 does not find it.  
*Suggestion:* Reword the mapping in §1.3 and §1.4: 'Chapter 4 develops a framework for the first part and leaves the operator as its only free component. Chapter 5 tests which parts of that framework are needed and answers the second part by comparing operators within it.' Open §4.1 with one sentence that names sub-question (1). Reword the opening of §5.1 accordingly (see chapter transitions).

**S3** [**HIGH**] **§5.4 Negative Results, 05-experiments.tex:784-797, and §5.4.2.** The section defines a negative result as 'a comparison whose difference stays under the floor', yet §5.4.2 contains the clearest positive framework result of the thesis: plain MSE never learns change, and removing the soft-Dice term costs 0.050 on all five folds (t = -5.1). The heading and the definition misfile the result that the abstract, §6.1 and Ch. 7 present as part of the answer to (1).  
*Suggestion:* Retitle §5.4 (e.g. 'The Framework Under Test and Capacity') and rewrite its opening so that it covers both outcomes: 'This section tests three choices that every arm shares or that could confound the comparison: the time handling (§5.4.1), the objective (§5.4.2) and the size of the operators (§5.4.3). The first and third are nulls in the sense of §5.1.4; the objective is not.' Alternatively, split it into 'What the Framework Needs' (§5.4.1–§5.4.2) and 'Capacity'.

**S4** [**HIGH**] **§1.2 Problem Statement, 01-introduction.tex:100-102.** The Introduction promises that whether age and sex help the forecast 'is tested in this thesis'. No covariate result is reported: the subsection was removed from Chapter 5, §4.4 only describes the inputs, and §6.3 says their value 'is not settled'. An examiner checks such promises.  
*Suggestion:* Replace the clause with '... is not established; both are included as inputs to every operator (§4.4), and their value is discussed in §6.3.'

**S5** [**HIGH**] **Mask provenance: §2.1.2, 02-background.tex:240-243; §2.1.3, 02:343-350; §3.1, 03-data.tex:50-58.** §2.1.2 says the two OCT signatures 'define the lesion mask used as channel 0', and §2.1.3 argues for OCT over FAF and concludes 'The thesis therefore works on the OCT en-face grid'. §3.1 then states that the mask was not segmented on the OCT but annotated on FAF and registered onto the OCT grid. A clinical reader will see a contradiction between Background and Data.  
*Suggestion:* In §2.1.2, replace 02:240-243 with 'On OCT, the first two signatures are what identifies the lesion; the third ... How the mask of the MUW cohort was produced is stated in §3.1.' In §3.1, add after 'The GA mask was not segmented on the OCT.' a bridging sentence: 'The OCT en-face grid is therefore the grid on which the state is held (§2.1.3), while the lesion outline itself comes from fundus autofluorescence.'

**S6** [**HIGH**] **Chapter 5 statistics density, §5.2 (05:367-382) and §5.3 throughout.** Strings such as 'Δ = +0.0170 ± 0.0085 SE (4/5) and per eye +0.0136 ± 0.0062 (46/75, t = 2.2)' at two seeds fill whole paragraphs. They duplicate Table E.3, which is never referenced. This is the main readability barrier of the longest chapter: the reading ('a tie', 'established') arrives only at the end of each statistics chain.  
*Suggestion:* This coincides with the reporting pass already planned in NOTES.md. Put the reading first and in words ('higher on all five folds and on 70 of 75 eyes'), move SE, t and seed-7 values to Table E.3, and reference that table in §5.1.4.

**S7** [medium] **Ch. 4 structure: §4.2 (04:92-200), §4.4 (04:951-985), §4.5 (04:1018-1195).** The framework, which is the answer to sub-question (1), is defined in three non-adjacent sections, separated by the operator section §4.3. §4.4 (conditioning) is shared by all arms but sits after the operators. The framework is never summarised as one object.  
*Suggestion:* Either reorder (4.2 framework: time handling, state, conditioning, training; 4.3 operators; 4.4 implementation), or at minimum add a signposting sentence at the end of the §4.2 opening and a short closing paragraph after §4.5 that lists the framework components and states which of them Chapter 5 tests.

**S8** [medium] **Results previewed in Chapter 4: 04-method.tex:470, 788-800, 876-885.** §4.3.3 opens with 'turns out to be the most consequential design decision', §4.3.6 states 'The Galerkin form turned out to be unstable' and defines the stability criterion, and §4.3.7 reports the solver-swap outcome. This blurs the method/results boundary of the hourglass and anticipates Chapter 5.  
*Suggestion:* Use neutral method statements with pointers: 04:470 → 'The graph on which messages travel sets how far one round reaches, which on this anisotropic grid needs care.'; 04:788 → 'Chapter 5 reports both forms (§5.5.2); the main comparison uses the energy-conserving form.' (move the stability definition to §5.5.2 or §5.1); 04:876-885 → keep only 'Its outcome is reported in §5.5.1.'

**S9** [medium] **Layer channels: 02-background.tex:440-442 ('not auxiliary context') vs 03-data.tex:146, 04-method.tex:193 and 1044 ('auxiliary targets'); Figure 2.2 caption, 02:168-171.** The Background calls the layer channels 'not auxiliary', the Data and Method chapters call them 'auxiliary targets'. The two uses mean different things (clinical relevance vs weight in the loss), but the reader sees a contradiction. The Figure 2.2 caption maps the anatomical strata onto the ten channels, whereas §6.3 states that the boundary names are not recorded.  
*Suggestion:* In §2.1.5, avoid the word: 'The layer channels therefore do not merely surround the mask; they carry ...'. In §3.2, write 'auxiliary prediction targets (weighted lower than the mask in the loss, §4.5.1)'. In the Figure 2.2 caption, replace the mapping sentence with 'The ten layer-boundary channels of §2.1.5 are surfaces between such strata; which boundaries they are is not recorded (§6.3).'

**S10** [medium] **Open loop on the layer channels: §1.2 (01:93-99), §2.1.5 (02:425-444), §3.2 (03:166-173); nothing in Ch. 5–6.** Three chapters argue that the ten layer channels are needed, but no experiment isolates their contribution, and neither the Discussion nor the Limitations says so. The Introduction's motivation is left without a closing statement.  
*Suggestion:* Add one sentence to §6.3 'Model scope', e.g. 'The contribution of the ten layer channels was not isolated: no operator was trained on the mask alone.'

**S11** [medium] **§5.2 The Arm Table, paragraph order (05:263-458).** The section gives dense pairwise statistics for the top three (05:367) and its conclusion (05:384-390) before the information needed to read the table: the per-pixel floor fixes the zero (05:409), fold variance exceeds most row differences (05:415), the table is not a leaderboard (05:440), the best-fold column reflects fold 2 (05:444). The 'not a leaderboard' sentence comes after a paragraph that reads the table as one.  
*Suggestion:* Reorder: (1) what the table holds and what fixes the scale (persistence, per-pixel floor); (2) how to read it (fold variance, Figure 5.3, best-fold column, not a leaderboard); (3) the top three in words; (4) caveats (T-FEN form, border/interior); (5) Figure 5.2; (6) pointers to §5.3–§5.7.

**S12** [medium] **§5.6 Qualitative Analysis and Clinical Comparison (05:1459-1466).** The section has no opening text and a single subsection. Its title promises a qualitative analysis that it does not contain; the qualitative material is in §5.2 (Figure 5.2) and Appendix D.  
*Suggestion:* Retitle the section 'Comparison with Mai et al. (2024)' and drop the subsection level, or move the Figure 5.2 paragraph (05:449-453) and the failure-mode summary of Appendix D into it.

**S13** [medium] **Ground-truth shrinkage: 04-method.tex:150-153, 05-experiments.tex:932-935 → 06-discussion.tex:266-274.** A design decision (no monotonic constraint) and an ablation argument rest on a data fact that is first quantified in the Limitations. The Method chapter points forward to the Discussion for evidence.  
*Suggestion:* Move the quantification to Ch. 3 (§3.6 or §3.1) and point to it from §4.2.1, §5.4.2 and §6.3.

**S14** [medium] **§6.1 'The framework', 06-discussion.tex:22-49.** Two different answers to sub-question (1) follow each other: 'The framework transferred ... it is the answer to the first part' (06:29-31, close to circular, since the framework was built to accept every operator) and 'What the framework needs, in short, is a loss that puts weight on the lesion mask, an interval length that reaches the operator ...' (06:47). The paragraph does not separate the components that were tested from those fixed by design (zero-initialised start, one-visit input, time budget of the curriculum).  
*Suggestion:* Merge the two into one answer that rests on evidence: identical persistence values across arms, every operator with spatial context learned, and §5.4.1–§5.4.2 show which parts matter. Add one sentence: 'The zero-initialised start, the one-visit input and the time budget of the curriculum were fixed by design and were not varied in the reported experiments.'

**S15** [medium] **Chapter openers: Ch. 2 (02:8-25), Ch. 3 (03:8), Ch. 4 (04:11).** Ch. 5, 6 and 7 open by naming their role in the research question; Ch. 2, 3 and 4 do not. Ch. 2 opens with a statement about the audience, Ch. 3 directly with the dataset, Ch. 4 with project provenance.  
*Suggestion:* Give each a one- to three-sentence opener that states what the chapter contributes to the question (see the chapter transitions for wording).

**S16** [medium] **§1.3 and §6.1: reach framed by direction of growth; 01-introduction.tex:140-150, 06-discussion.tex:142-143.** The Introduction motivates the reach requirement through biological anisotropy (faster growth towards the periphery), and §6.1 speaks of 'reach along the direction in which the front moves'. The measured reach result, however, concerns the 21:1 pixel-spacing anisotropy of the grid: a stencil that is symmetric in pixels is lopsided in millimetres. The two kinds of anisotropy are easily conflated.  
*Suggestion:* In §1.3, keep the clinical directional finding as context, but introduce the grid anisotropy as the reason the reach question is non-trivial. In §6.1, write 'its physical reach along the finely sampled axis of the grid' instead of 'along the direction in which the front moves'.

**S17** [medium] **§2.2.4 vs §2.3 (02:712-900).** Learned solvers are introduced twice, in two sections separated by the GA argument of §2.2.5.  
*Suggestion:* Move §2.2.4 to open §2.3, or move §2.2.5 to the end of §2.3 (see chapter transitions).

**S18** [medium] **Register shifts: §2.1 (e.g. 'can be thought of as a biological camera', 'The terminology in this list takes some getting used to', 'Put differently', 'In other words', 'essentially'); §2.3–§2.4 ('fundamentally irregular', 'It must be stated plainly', 'reliably poor', 'dictates'); Appendix G.1 ('fundamentally inefficient', 'entirely supervised', 'Crucially', 'inevitably', 'critical', 'precisely').** These passages (older drafts) are explanatory, use analogies or intensifiers, and read like a different author from the plain register of Ch. 3–7. They are also among the most strongly flagged passages in the GPTZero scans.  
*Suggestion:* Bring them into the register of Ch. 3–5 in the sentence-level pass: remove analogies and asides addressed to the reader, delete intensifiers, and let concrete subjects carry the sentences. Appendix G.1 needs this most, because it is the first page an examiner reads in the MM-PDE appendix.

**S19** [medium] **Terminology across chapters.** 'Arm' is used from 04:46 on without definition. 'Canonical fold' and 'canonical setting' appear in Ch. 3 (03:252-286) before 'canonical' is defined. The central concept is called 'built-in assumptions' (Ch. 1), 'inductive-bias ingredients' (§2.3), 'ingredients' (Ch. 5) and 'properties' (abstract, §4.3, §6.1, Ch. 7). The operator is variously 'operator', 'backbone', 'arm' and 'model'; the graph network is 'graph network', 'GNN', 'graph solver' and 'message-passing network'.  
*Suggestion:* Add a short terminology paragraph to §4.1: an arm is one operator configuration run over the five folds; 'canonical' denotes the dilated-stencil graph network; and one of 'ingredient' or 'property' is chosen. Define 'canonical fold' (fold 2) at its first use in §3.4, and use the chosen term from §1.3 on.

**S20** [low] **§6.1 'Predictions between visits', 06-discussion.tex:126-138.** The intermediate-time-point regulariser is mentioned here for the first time in the thesis. A result appears in the Discussion that the Results chapter never reports.  
*Suggestion:* Either add one sentence to §5.4.1 ('An intermediate-time-point regulariser ... was evaluated early in the project and removed; no number is reported because those runs predate the current pipeline.') and refer to it from §6.1, or mark it in §6.1 as project history without a reported result.

**S21** [low] **Front matter: main-thesis.tex:190 (title) and :242 (keywords).** The keywords foreground 'MP-PDE, MM-PDE, moving mesh', and the title foregrounds 'Neural PDE Solvers'. Under the current framing MM-PDE lives in Appendix G and the operator family is found not to decide the outcome; a reader of the title and keywords expects a different thesis.  
*Suggestion:* The title is pending with the supervisor. Align the keywords with the framing now, e.g. 'Geographic Atrophy, OCT, longitudinal prediction, autoregressive forecasting, neural PDE solvers, graph neural networks, operator comparison, medical imaging'.

**S22** [low] **§3.7, 03-data.tex:408-411; §2.1.1, 02-background.tex:107-110.** Two internal pointers lead nowhere. §3.7 promises that fold heterogeneity is 'revisited in the evaluation protocol (§5.1)', which does not happen; fold 4 recurs as an outlier in §5.2, §5.4.2 and §5.3.4 without this link. §2.1.1 says subfoveal significance was 'discussed in §1.2'; it is discussed in §1.1.  
*Suggestion:* Point §3.7 to §5.2 (where fold variance is discussed) or drop the promise. Change the §2.1.1 pointer to §1.1.

**S23** [low] **§1.3 Why Neural PDE Solvers? (01:115-209).** The section holds the PDE motivation, the research question and the contributions under a heading that announces only the first. The contributions paragraph (01:197-209) omits the objective finding (the mask weighting decides learning), which the abstract, §6.1 and Ch. 7 present as part of the answer.  
*Suggestion:* Give the contributions a run-in heading like the research question (e.g. '\paragraph{Contributions.}'), and add a clause on the objective so that the Introduction's list matches the Conclusion's.

**S24** [low] **Implementation history in the prose: 03-data.tex:292 (footnote, 365 vs 365.25), 04-method.tex:835-838 (unit-check convergence orders), 05-experiments.tex:1630-1633 (refuted GPU-sharing explanation).** Project history and code checks interrupt the argument and read as lab-notebook material.  
*Suggestion:* Move them to Appendix C or F. In §5.7, keep only the measured causes of the spread between folds.

**S25** [low] **Depth balance: §2.1 (~8 pages incl. §2.1.6) vs §2.3 (~1.5 pages); §4.2.2 (half a page on tensor layout); §4.3.4 (textbook account of the original U-Net).** The clinical primer is long and partly duplicated, the learned-solver background is short, §4.2.2 is a thin implementation subsection inside the framework definition, and the original U-Net is described in more detail than the comparison needs.  
*Suggestion:* Shorten §2.1 by the duplications listed under redundancy instead of expanding §2.3. Fold §4.2.2 into §4.3.1 or §4.6. Reduce the original U-Net description to what the four departures need.

## Transitions between chapters and major sections

**T1** **Ch. 1 (§1.4 Thesis Outline) → Ch. 2 (§2.1 opening, 02-background.tex:8-25).** Ch. 1 ends with a clean roadmap. Ch. 2 has no chapter-level opening: it begins with a §2.1 paragraph about the audience ('The clinical framing established in Chapter 1 is taken as read ... written for a primarily machine-learning audience'). The reader is not told why the chapter has four disparate parts (clinical imaging, classical solvers, learned solvers, related work) or what Chapters 3–5 need from each. A second roadmap of §2.1 then follows at the end of §2.1.1 (02:131-136).  
*Suggestion:* Add a two- or three-sentence chapter opener before §2.1, e.g. 'This chapter provides the background for the rest of the thesis. §2.1 describes GA and the OCT data from which each visit's state is formed; §2.2 and §2.3 introduce the solver mechanisms and the learned operators on which the framework of Chapter 4 and the comparison of Chapter 5 build; §2.4 places the work among prior forecasts of GA progression.' Then cut the audience sentence (02:18-24) and the duplicate roadmap at 02:131-136.

**T2** **§1.2 Problem Statement (end, 01-introduction.tex:105-113) → §1.3 Why Neural PDE Solvers? (opening, 01:115-150).** §1.2 closes by announcing that the next section 'motivates such a framework' (Δt-conditioning and visit-to-visit rollout) and that the model is a separate question. §1.3 instead opens with an operator argument (local boundary dynamics, reach). The reach argument is also motivated by the biological directional anisotropy of growth (01:140), whereas the reach result of Chapters 4–5 rests on the 21:1 pixel-spacing anisotropy of the grid. The reader expects framework motivation, receives operator motivation, and links reach to the wrong kind of anisotropy.  
*Suggestion:* Either reorder §1.3: first why the structure of a numerical solver (state on a grid, a step of length Δt, residual update, rollout) suits irregular visits, then the locality and reach argument as the reason why the operator question stays open. Or change the end of §1.2 to: 'The next section argues why the structure of a numerical PDE solver suits this task, and why it leaves open which operator should sit inside it.' In either case, add one sentence in §1.3 that the en-face grid is about 21 times coarser across B-scans than along them (§3.3), so a neighbourhood that looks symmetric in pixels reaches very different physical distances. That is the form of the reach question that Chapter 5 answers.

**T3** **Ch. 2 (end of §2.4 Related Work, 02:944-962) → Ch. 3 (§3.1 Dataset).** Ch. 2 ends by listing the origins of the operators, with a pointer to §4.3. Ch. 3 starts without an opener and re-presents the cohort already given in §2.1.6: 553 scans, 75 eyes, native shapes, spacing, the 21:1 ratio and the full crop census. The reader meets the cohort twice and cannot tell which version is authoritative.  
*Suggestion:* Reduce §2.1.6 to two or three sentences that name the cohort and point to Ch. 3, or remove it. Move the literature paragraph on the 6 mm window (02:470-475) into §3.3, which already points back to it (03:189). Open Ch. 3 with one bridging sentence: 'This chapter describes the MUW cohort and how each visit is turned into the eleven-channel state, on one common grid, that the framework of Chapter 4 receives.'

**T4** **Ch. 3 (end of §3.7, 03-data.tex:408-411) → Ch. 4 (§4.1 opening, 04-method.tex:11-14).** Ch. 3 ends on a promise that fold heterogeneity 'is revisited in the evaluation protocol (§5.1)'; §5.1 does not revisit it. Ch. 4 then opens with project provenance that names MP-PDE and MM-PDE. This is the first mention of MM-PDE in the main text since the Introduction's pointer, and it is unrelated to the data chapter. Chapter 4 never states that it answers sub-question (1); the phrase 'research question' does not occur in 04-method.tex.  
*Suggestion:* Open §4.1 with the question, e.g. 'This chapter addresses the first part of the research question: what kind of framework the forecast needs. The framework fixes everything except the update operator, so that operators can be compared on equal terms.' Move the provenance sentence (04:11-14) to the end of §4.1 or to the start of §4.3.2. Either connect the §3.7 fold-4 sentence to §5.2, where fold variance is discussed, or delete the forward promise.

**T5** **Ch. 4 (§4.6, end) → Ch. 5 (§5.1 opening, 05-experiments.tex:18-21).** This link works: §4.6 ends with GPU nondeterminism and 'Chapter 5 quantifies this run-to-run variation', and §5.1.4 picks it up. The opening sentence of Ch. 5, however, says the chapter answers only the second part of the question, whereas §5.4.1 and §5.4.2 test the framework, and §6.1 uses them as its answer to part (1).  
*Suggestion:* Replace 05:18-21 with e.g. 'This chapter tests the framework of Chapter 4 and answers the second part of the research question. §5.2 and §5.3 compare operators within the framework, §5.4 tests which parts of the framework matter and whether operator size matters, and §5.5 states what may be said about the trained operators. This section defines how they are scored and how two scores are compared.'

**T6** **Ch. 5 (end of §5.7 Computational Cost, 05:1660-1664) → Ch. 6 (§6.1 opening).** Ch. 5 ends on the cost section, with the last sentence 'Inference time per rollout step and memory footprint were not measured.' There is no closing synthesis; the answer to sub-question (2) is in §5.3.5, eight pages earlier. The summary at the opening of Ch. 6 compensates only partly, and the reader leaves the results chapter on a logistical point.  
*Suggestion:* Move the cost convention (first paragraph of §5.7) into §5.1.3 and the cost comparison directly after §5.2 (Table 5.1 already has the cost column and points to §5.7), so that Ch. 5 ends with the clinical comparison. Alternatively, keep the order and close Ch. 5 with a four- to five-sentence summary: what the framework needs (§5.4.1–§5.4.2), what the operator needs (§5.3), what did not matter (§5.4.3) and what may be said (§5.5).

**T7** **Ch. 6 (§6.4 Future Work) → Ch. 7 (Conclusion).** This works structurally: Ch. 7 restates the question and answers it in the same two parts. However, Ch. 7 re-runs §6.1 almost paragraph by paragraph with the same numbers and caveats (framework, operator, ingredients, what did not matter, the Mai comparison). Read in sequence, it feels like a second discussion rather than a conclusion.  
*Suggestion:* Keep the structure of Ch. 7 but drop second-level detail: the matched-control fold story in the transport bullet (07-conclusion.tex:56-60) and the cohort details of the Mai comparison (07:78-87). Each paragraph then gives the finding and at most one number.

**T8** **§2.2.4–§2.2.5 (Neural solvers that keep the mechanisms; Why this structure suits GA) → §2.3 Neural PDE Solvers and Surrogate Architectures.** Learned solvers are introduced in §2.2.4, the GA argument follows in §2.2.5, and §2.3 then restarts the learned-solver topic with a taxonomy (neural operators vs autoregressive). The reader meets 'neural solvers' twice, in two sections, with an application argument in between.  
*Suggestion:* Move §2.2.4 to the start of §2.3, so that §2.2 covers the classical mechanisms and why they suit GA, and §2.3 covers the learned versions and their families. Alternatively, move §2.2.5 to the end of §2.3, so that the GA argument closes the whole technical background and leads directly to Related Work.

**T9** **§4.2 The Fixed Framework → §4.3 The Operators → §4.4 Conditioning → §4.5 Training.** The framework, which is the answer to sub-question (1), is split: the time handling and tensor layout are in §4.2, the conditioning inputs in §4.4 and the loss, curriculum and optimisation in §4.5, with the 13-page operator section in between. After §4.3 the reader has to reassemble the framework.  
*Suggestion:* Preferred: place §4.4 and §4.5 directly after §4.2, as parts of the framework, so that Ch. 4 reads framework → operators → implementation. Minimum, if the order stays: end the §4.2 opening (04:95-117) with 'The framework consists of this section, the conditioning inputs (§4.4) and the shared training setup (§4.5); §4.3 describes the operators placed in its slot.' Repeat that sentence in the caption of Figure 4.1.

**T10** **§5.2 The Arm Table → §5.3 The Ingredient Study.** §5.2 already states the conclusion that §5.3 is meant to establish ('What separates the arms is therefore not their class but the ingredients they carry', 05:389-390), and §5.3 opens by restating the 0.04 spread (05:463). The ingredient reading is asserted before its evidence and then asserted again in §5.3.5.  
*Suggestion:* End §5.2 with the reading instruction that is already there (05:440-443: 'Adjacent rows mostly lie within the floor of each other, so the table is not a leaderboard ... §5.3 examines one at a time'), delete 05:388-390, and keep the ingredient conclusion for §5.3.5.

**T11** **§5.3.5 Two Routes to One Deficit (end, 05:776-781) → §5.4 Negative Results.** §5.3.5 hands over with '§5.4 reports what was measured and did not matter', but §5.4.2 reports what did matter: the mask weighting decides whether anything is learned, and removing the soft-Dice term costs about 0.05 on all five folds.  
*Suggestion:* Change the handover to '§5.4 tests the shared parts of the framework and the size of the operators.' and retitle §5.4 accordingly (see the structure issue on §5.4).

**T12** **§5.5.2 Numerical Stability of the T-FEN → §5.6 Qualitative Analysis and Clinical Comparison.** §5.5.2 ends on Courant numbers. §5.6 opens without any text and goes straight into a single subsection (§5.6.1). Its title promises a qualitative analysis that it does not contain: the qualitative material is in §5.2 (Figure 5.2) and Appendix D.  
*Suggestion:* Retitle §5.6 'Comparison with Mai et al. (2024)', remove the subsection level, and add one opening sentence that links it to §1.1, e.g. 'The change-region Dice measures where a lesion changes; the treatment decision of §1.1 depends on how fast it grows. This section compares both with the closest prior work on the same clinic's data.' Alternatively, keep the title and move the paragraph on Figure 5.2 (05:449-453) and the failure-mode summary of Appendix D (91-appendix.tex:95-100) into §5.6.

**T13** **Main text → Appendices.** Appendices B and C are empty chapters (91-appendix.tex:75-89). Appendix E is titled 'Ablation Details' but holds additional results (border vs interior split, growth speed for all arms, both seeds). Table E.3 (tab:appendix:seeds) is never referenced from the main text, although Chapter 5 quotes all of its numbers inline.  
*Suggestion:* Fill or drop Appendices B and C; rename Appendix E 'Additional Results'; reference Table E.3 from §5.1.4 ('the second seed is reported for every main comparison in Table E.3') and from §5.2 and §5.3.

## Repetition across chapters

**R1** **Crop census (27.3 % of visits lose lesion area, more than 5 % in 6.0 %, worst case 25.7 %, 31.1 % touch the edge, plus the 35 % padding and 1.9× trade-off).** Appears in: 02-background.tex:476-484 (§2.1.6); 03-data.tex:215-235 (§3.3); 06-discussion.tex:246-256 (§6.3); 91-appendix.tex:48-52 (App. A.2); 06-discussion.tex:313-317 (§6.4, paraphrased).  
*Suggestion:* Keep the full census in §3.3 and the figure in Appendix A.2. Remove it from §2.1.6. In §6.3, replace the restated numbers by one sentence: 'The fixed 49×1024 window is a deliberate trade-off with a measured cost (§3.3): growth across the window edge is censored, in the training targets and in the metrics, without a flag.'

**R2** **Cohort facts (553 scans, 75 eyes, 38–66 × 961–1719 native grids, 67 shapes, spacing, 5.94 × 5.82 mm window, 21:1 ratio).** Appears in: 02-background.tex:445-498 (§2.1.6); 03-data.tex:8-90 (§3.1); 03-data.tex:178-200 (§3.3).  
*Suggestion:* These are data facts and belong to Ch. 3. Reduce §2.1.6 to a short pointer, and move its literature paragraph on the 6 mm window to §3.3, which refers back to it (03:189).

**R3** **Definition of the layer channels as depth maps ('fixing a pixel of the en-face grid selects a single A-scan ...') and the two kinds of en-face maps.** Appears in: 02-background.tex:374-380 (§2.1.4); 02-background.tex:410-422 (§2.1.5); 03-data.tex:155-160 (§3.2); 04-method.tex:175-180 (§4.2.2).  
*Suggestion:* Keep the definition in §3.2. In §2.1.5 keep only the clinical motivation (the biomarkers) with a pointer to §3.2 for the definition; §4.2.2 already points back.

**R4** **Description of the retina and the subsection roadmap within §2.1.** Appears in: 02-background.tex:26-40 (§2.1.1, retina defined); 02-background.tex:181-183 (§2.1.2 opens by defining the retina again); 02-background.tex:112-125 and the Figure 2.2 caption (layer list twice); 02-background.tex:8-25 and 131-136 (two roadmaps of §2.1).  
*Suggestion:* Drop the first sentence of §2.1.2 (the retina is already defined in §2.1.1). Keep the full layer list in the Figure 2.2 caption only. Keep one roadmap, either at the start of §2.1 or at the end of §2.1.1, not both; the 02:134 roadmap item 'the projection from 3D OCT volume to the 2D en-face grid' also no longer matches §2.1.4, which states that no projection is computed.

**R5** **Continuous-time / Neural-ODE caution (f is not a rate; solver invariance must be tested; Ott et al., Krishnapriyan et al.).** Appears in: 02-background.tex:880-890 (§2.3); 04-method.tex:158-170 (§4.2.1); 04-method.tex:863-885 (§4.3.7 'Jump and continuous time', including the outcome); 05-experiments.tex:1174-1210 (§5.5.1 'What is tested' and 'Principle'); 05-experiments.tex:845-848 (§5.4.1).  
*Suggestion:* Give the full argument once, in §5.5.1. Keep the concept in one sentence in §2.3. In §4.2.1 keep one sentence plus the pointer. In §4.3.7 keep only the mechanism (jump vs continuous time) and remove the Ott/Krishnapriyan argument and the test outcome (04:876-885).

**R6** **The batch-statistics argument (rollout in training mode, so no batch normalisation).** Appears in: 04-method.tex:240-250 (§4.3.1); 04-method.tex:381-390 (§4.3.2 normalisation paragraph); 04-method.tex:575-580 (§4.3.4 group normalisation); 04-method.tex:1136-1138 (§4.5.2 end).  
*Suggestion:* Keep the argument in §4.3.1 (the contract) and replace the other three with short pointers ('as the contract requires, §4.3.1').

**R7** **Justification that differences can be attributed to the operator because everything else is shared.** Appears in: 04-method.tex:15-37 (§4.1, twice); 04-method.tex:213-216 (§4.3 intro); 04-method.tex:255-257 (§4.3.1, identical inputs); 04-method.tex:890-893 (§4.3.8); 04-method.tex:1021-1025 (§4.5 intro).  
*Suggestion:* State the design contract once, in §4.1. Elsewhere, name only the specific shared element (identical input planes in §4.3.1, matched size in §4.3.8) without repeating the attribution argument.

**R8** **Decoder of the original MP-PDE (1-D convolution along the hidden vector, emitting K steps).** Appears in: 04-method.tex:306-312 ('The original MP-PDE'); 04-method.tex:399-408 ('The architecture used here'); Table 4.1, row 'Decoder'.  
*Suggestion:* Describe the original decoder once, in 'The original MP-PDE', and in 'The architecture used here' write only 'Because the framework predicts one step (K = 1), the convolutional head was replaced by ...'.

**R9** **Free-form FEN controls (34,785 parameters, factor 1.97, width 139 with 68,282).** Appears in: 04-method.tex:805-811 (§4.3.6); 04-method.tex:905-910 (§4.3.8); 04-method.tex:920-923 (Table 4.2 caption); 05-experiments.tex:675-680 (§5.3.4).  
*Suggestion:* Keep the parameter bookkeeping in §4.3.8 and Table 4.2. In §4.3.6 point to §4.3.8; in §5.3.4 keep one clause ('not parameter-matched, factor 1.97, §4.3.8').

**R10** **Galerkin vs energy-conserving T-FEN (forms, the stability verdict, the stability criterion).** Appears in: 04-method.tex:768-800 (§4.3.6: both forms, 'turned out to be unstable', the definition of unstable); 05-experiments.tex:404-407 (§5.2); 05-experiments.tex:668-671 (§5.3.4, Galerkin numbers); 05-experiments.tex:1060-1075 (§5.4.3 caveat); 05-experiments.tex:1341-1420 (§5.5.2).  
*Suggestion:* In §4.3.6, describe both forms neutrally ('Two forms were trained; Chapter 5 reports both (§5.5.2), and the main comparison uses the energy-conserving form'). Move the definition of 'unstable' to §5.5.2 or to §5.1, since it is an evaluation criterion. Keep the verdict and the diagnosis in §5.5.2 only.

**R11** **Covariates are graph-level and cannot localise anything.** Appears in: 04-method.tex:956-963 (§4.4); 06-discussion.tex:109-113 (§6.1); 06-discussion.tex:290-292 (§6.3).  
*Suggestion:* Keep the mechanism in §4.4. In §6.1 refer to it ('as noted in §4.4, the covariates shift a prediction only as a whole') and drop the repeat in §6.3.

**R12** **Caveats of the Mai et al. (2024) comparison (raw OCT vs segmented masks, cohort size, crop, different visits).** Appears in: 02-background.tex:925-930 (§2.4); 05-experiments.tex:1505 and 1597 (captions of Table 5.6 and Table 5.7); 05-experiments.tex:744 (Figure 5.5 caption); 05-experiments.tex:1562-1570 and 1579-1586 (§5.6.1, twice); 06-discussion.tex:169-176 (§6.2); 07-conclusion.tex:78-87 (Ch. 7).  
*Suggestion:* Give the full caveat once in §5.6.1 (merge the two paragraphs). Captions: 'not a head-to-head comparison (§5.6.1)'. §2.4: one sentence on the input regime. §6.2: replace the 'not like-for-like' paragraph by one clause with the pointer. Ch. 7: half a sentence.

**R13** **The headline antithesis ('the architecture class does not decide; the ingredients do') and similar 'X, not Y' section closers.** Appears in: 05-experiments.tex:384-390 (§5.2); 05-experiments.tex:463-465 (§5.3 intro); 05-experiments.tex:776-778 (§5.3.5); 05-experiments.tex:599 (§5.3.2 '... and not in its operator class'); 05-experiments.tex:856-857 (§5.4.1); 05-experiments.tex:883 (§5.4.2); 05-experiments.tex:1262 (§5.5.1); 06-discussion.tex:17-20 and the heading at 06:51 (§6.1); 07-conclusion.tex:33; 00-abstract.tex:62-64.  
*Suggestion:* Make the claim where it is established (§5.3.5) and where it is interpreted (§6.1, Ch. 7, abstract). Elsewhere, end the section on its concrete finding (e.g. §5.4.1: 'Neither the multiplication by Δt nor the integration scheme changes the result.'). This repeated mirror structure at section ends is one of the main drivers of the machine-like impression at the macro level.

**R14** **Seed-7 replication numbers.** Appears in: 05-experiments.tex:373-382 (§5.2); 05-experiments.tex:480-483 (§5.3.1); 05-experiments.tex:503-507, 592-597 (§5.3.2); 05-experiments.tex:638-650 (§5.3.3); 05-experiments.tex:665-691 (§5.3.4); 91-appendix.tex:231-300 (Table E.3, not referenced).  
*Suggestion:* Report the seed-7 values in Table E.3 only, reference it from §5.1.4, and in the text say per comparison whether the second seed agrees (e.g. 'replicated at the second seed, Table E.3'). The two disagreements (local path, and T-FEN vs U-Net strength) keep one sentence each.

**R15** **Ground-truth lesion shrinkage between visits.** Appears in: 04-method.tex:150-153 (§4.2.1, as a design justification, pointing to §6.3); 05-experiments.tex:932-935 (§5.4.2); 06-discussion.tex:266-274 (§6.3, the only quantification).  
*Suggestion:* State the quantification (5 % of pairs shrink in total area; 96 % lose some border pixels) once, as a data fact in Ch. 3 (§3.6 or §3.1). Point to it from §4.2.1 and §5.4.2, and keep only the interpretation (noise vs regression) in §6.3.

**R16** **No test split / every result is a validation result; anchor without upper bound.** Appears in: 03-data.tex:395-404 (§3.7); 05-experiments.tex:164-166 and 207-208 (§5.1.3, twice); 06-discussion.tex:240-241 (§6.3); 03-data.tex:351-358, 05-experiments.tex:145-149, 06-discussion.tex:279-281 (anchor).  
*Suggestion:* State each once in Ch. 3, once in the protocol and once in the Limitations; remove the second statement within §5.1.3 (05:207-208).

**R17** **Operator origins.** Appears in: 02-background.tex:870-890 (§2.3); 02-background.tex:944-962 (§2.4, last paragraph); 04-method.tex:273-325, 560-650, 693-720 (each original summarised again in §4.3).  
*Suggestion:* Because §4.3 summarises every original, the origins paragraph of §2.4 adds a third pass. Either cut it to one sentence pointing to §4.3, or drop the citations of origins from §2.3 and keep them in §2.4.


---

# Part 1 (detail) — Where a first-time reader gets lost

Read front to back as an external examiner, the thesis has a sound large-scale path: research question, then background, data, framework and operators, experiments, discussion. Each chapter opens with a usable roadmap, and the hedging is careful. A first-time reader is held up mainly by vocabulary, not by the argument. The project's working terms are used well before they are defined, and some are never defined in the compiled text: arm, canonical, floor, deficit, one-year anchor, instrument and graduate, late epochs, survey, backbone, and the moving-mesh terms dual or correction branch and layer encoder. Several of these words also carry two to four meanings. 'Canonical' names a fold, a normalisation scheme, an age mode and the reference model. 'Floor' names two truncated models, a statistical threshold and the persistence score. 'Hybrid' names classical-learned solvers, the FEN and the FNO with a local path. 'Window' names the crop, a training transition and the epochs 10-29. 'Anchor' names the evaluation time and, in §5.6.1, a point of reference. The reader is also asked several times to accept results on credit: 'the same deficit' in the abstract, §1.3 and §5.2 is explained only in §5.3.5, and §4.3.3 says the graph 'turns out' to be the most consequential choice. Two places read as contradictions. Chapter 2 says the OCT signatures define the channel-0 mask, but Chapter 3 says the mask was outlined on FAF. §5.1.4 defines the fold and eye counts k and m as 'same sign as the mean', but the chapter uses them as 'first arm higher'. Structurally, the cohort facts and the crop census are repeated in §2.1.6, §3.1/§3.3, §6.3 and Appendix A. §5.2 packs about twenty numbers into one paragraph, and the same pair is called both 'a tie' and 'a small but consistent lead'. The section titled 'Qualitative Analysis' contains only the Mai comparison. The register is consistent and academic, apart from a few epigrams ('How time enters the update turned out to matter less than that it enters', 'The framework transferred') and some project-history phrasing ('an earlier result', 'Before this change', 'An earlier explanation'). These refer to a chronology the reader never saw. One short definitions paragraph at the end of §4.1 would remove most of the friction: operator vs arm, the canonical model and why it was chosen, the locality floors, the deficit. So would one fixed name per arm, used the same way in text and tables.

## Points where the reader gets lost

**L1** [**HIGH**] Abstract, 00-abstract.tex:52 [GPTZero: not scanned]

> A learned transport term raises it by 0.062 over the same network without one, a second route to the same deficit; these two are the two highest operators.

*Problem:* 'The same deficit' refers to a deficit the abstract never names. 'These two are the two highest operators' is ambiguous: the reader must work out that it means the stencil graph network and the transport FEN, not the two terms. It also sits awkwardly after the earlier ranking sentence (FEN, graph network, U-Net).  
*Fix:* A learned transport term raises it by 0.062 over the same network without one. Both changes remedy the same deficit, an update that sees less far than the lesion front moves between visits, and the two operators that carry them, the Finite Element Network and the dilated-stencil graph network, are the two highest.

**L2** [**HIGH**] §1.3 (contributions paragraph), 01-introduction.tex:201 [GPTZero: AI]

> It identifies physical reach at the scale of the lesion front and an explicit transport term as two independent routes to the same deficit, and it reports what did not help --- larger models, a higher integration order, a monotonic-growth penalty and a moving-mesh extension --- as results in their own right.

*Problem:* 'The same deficit' is used as if already known, but it is defined only in §5.3.5. The transport term, the monotonic-growth penalty and the moving-mesh extension also appear here for the first time, unexplained. The contribution statement therefore cannot be understood on a first reading.  
*Fix:* It identifies two independent ways of correcting the same deficit, an update that cannot see as far as the lesion front moves between two visits: physical reach at the scale of the front, and an explicit transport term that moves the state along a learned velocity. It reports what did not help --- larger models, a higher-order time integrator, a penalty against lesion shrinkage and a moving-mesh extension (Appendix~\ref{app:mm-pde}) --- as results in their own right.

**L3** [**HIGH**] §2.1.2 Geographic Atrophy on OCT, 02-background.tex:240 (also :352-359; conflicts with 03-data.tex:50) [GPTZero: AI]

> The first two signatures define the lesion mask used as channel~0 of the state tensor; the third is a boundary-localised predictive biomarker that motivates encoding the surrounding layer geometry rather than the mask alone.

*Problem:* Chapter 2 tells the reader that the OCT signatures define the channel-0 mask. It adds that 'a single OCT volume shows both the lesion and the retinal layers' and that 'No cross-modality fusion is required'. Chapter 3 then opens with 'The GA mask was not segmented on the OCT' and describes an FAF annotation registered to the OCT grid. A first-time reader takes this as a contradiction and must decide which chapter is right.  
*Fix:* The first two signatures are how the lesion is recognised on OCT; how the mask of channel~0 was obtained for this cohort is stated in~\S\ref{sec:data:dataset}. The third is a boundary-localised predictive biomarker that motivates encoding the surrounding layer geometry rather than the mask alone. (Also cut 'No cross-modality fusion is required.' at line 359.)

**L4** [**HIGH**] §3.4 Normalisation, 03-data.tex:260 (also :252, :281, :286) [GPTZero: AI; :281 HUMAN]

> The binary mask is z-scored in the same way as the layer channels. On the canonical fold, the background value 0 maps to $-0.602$ and the foreground value 1 maps to $+1.660$.

*Problem:* 'The canonical fold' is never defined. §3.7 later mentions fold 2, but the rendered text never states that the canonical fold is fold 2. In the same pages, 'canonical' also labels the z-score (:252) and the per-visit age mode (:281), and from Chapter 4 on it names the reference model. One word carries four meanings before any of them is explained.  
*Fix:* The binary mask is z-scored in the same way as the layer channels. On fold~2 (\S\ref{sec:data:splits}), the background value 0 maps to $-0.602$ and the foreground value 1 maps to $+1.660$. (Also: line 252 'Each channel is z-scored,'; line 281 'which every reported run uses'; line 286 'On fold~2'.)

**L5** [**HIGH**] §4.1, 04-method.tex:39 [GPTZero: HUMAN]

> The operators run through this pipeline are a message-passing graph neural network (GNN) on two different neighbourhood graphs (\S\ref{sec:method:graph}), one of which is the canonical model of this thesis; a U-Net; a Fourier Neural Operator (FNO); and a hybrid Finite Element Network (FEN).

*Problem:* The reader learns that one of the two graphs gives 'the canonical model' but not which one. The dilated stencil is identified only in Table 4.2 and justified only in §5.3.2. Even so, 'canonical model/configuration' is used about 40 times before that justification, once for the round count of the other graph (04-method.tex:500).  
*Fix:* The operators run through this pipeline are a message-passing graph neural network (GNN) on two different neighbourhood graphs (\S\ref{sec:method:graph}), of which the network on the dilated stencil serves as the reference, called the \emph{canonical model} below (the reason is given in~\S\ref{sec:experiments:ingredients:reach}); a U-Net; a Fourier Neural Operator (FNO); and a Finite Element Network (FEN).

**L6** [**HIGH**] §4.1, 04-method.tex:44 [GPTZero: AI]

> A fixed-step Runge--Kutta wrapper can be placed around any of these operators, and a per-pixel model with no spatial context marks the lower floor. The arms are parameter-matched to the canonical configuration's 67\,147 parameters within a narrow band;

*Problem:* 'Arm' is used here for the first time in its experimental sense and is never defined; the only earlier 'arm' is the sample/reference arm of the OCT interferometer (§2.1.3). 'The lower floor' is undefined and implies an upper floor. Both terms carry most of Chapters 4-5.  
*Fix:* A fixed-step Runge--Kutta wrapper can be placed around any of these operators, and a per-pixel model shows what a model without spatial context achieves (a \emph{locality floor}). Each setting of the slot, trained and evaluated on all five folds, is called an \emph{arm}. The arms are parameter-matched to the canonical configuration's 67\,147 parameters within a narrow band;

**L7** [**HIGH**] §5.1.4, 05-experiments.tex:235 (also :245-246 for m; Table 5.2 caption :538) [GPTZero: AI]

> where $k$ is the number of folds on which the difference has the same sign as the mean.

*Problem:* The definition does not match the usage. The chapter reports negative means with small k (FNO − U-Net −0.0215 '(1/5)'; reach ladder '0/5'), and Table E.3 counts 'folds on which the first arm is higher'. A reader who applies the definition reads 'established below the U-Net (1/5)' as 'negative on only one fold'.  
*Fix:* where $k$ is the number of folds on which the first arm is higher. (Use the same wording for $m$ at line 245 and in the caption of Table~\ref{tab:experiments:reach}.)

**L8** [**HIGH**] §5.2 The Arm Table, 05-experiments.tex:367-382 [GPTZero: HUMAN/AI]

> The T-FEN against the dilated-stencil graph network gives $\Delta = +0.0170 \pm 0.0085$~SE (4/5) and per eye $+0.0136 \pm 0.0062$ (46/75, $t = 2.2$): at the floor on one instrument and under it on the other, a tie.

*Problem:* The paragraph gives about twenty numbers for three pairs at two seeds, with the pairs interleaved. The same pair (T-FEN vs dilated stencil) is called 'a tie' here and 'a small but consistent lead, at the noise level' six lines later; the abstract says 'only slightly above', §5.3.5 'within about 0.017', §6.1 'indistinguishable'. A first-time reader cannot extract the verdicts on which the headline rests.  
*Fix:* Lead with the verdicts and leave the numbers to Table~\ref{tab:appendix:seeds}: 'Table~\ref{tab:appendix:seeds} lists the three pairwise comparisons at both seeds. The T-FEN lies above the U-Net on every fold at both seeds. Against the dilated-stencil network it is higher by about 0.017 at both seeds, a small lead at the noise level: at seed 42 the difference sits at the floor on one instrument and under it on the other, at seed 7 it holds on every fold. The dilated-stencil network and the U-Net cannot be told apart at either seed.' Use one verdict phrase for the T-FEN/stencil pair in the abstract, §5.2, §5.3.5, §6.1 and Chapter 7.

**L9** [**HIGH**] §5.2, 05-experiments.tex:386 [GPTZero: unknown (sentence not in the scanned version)]

> The two highest arms are the two that carry a remedy for the reach deficit taken up in~\S\ref{sec:experiments:ingredients:convergence}: the transport term and the dilated stencil. What separates the arms is therefore not their class but the ingredients they carry.

*Problem:* 'The reach deficit' is used before it is explained (§5.3.5). The chapter's conclusion is drawn before the ingredient study that supports it, so the reader must accept both on credit.  
*Fix:* The two highest arms are the two that carry a remedy for one deficit, a single update that sees less far than the lesion front moves between visits (\S\ref{sec:experiments:ingredients:convergence}): the transport term and the dilated stencil. What separates the arms is therefore not their class but the ingredients they carry, as \S\ref{sec:experiments:ingredients} shows one ingredient at a time.

**L10** [medium] Abstract, 00-abstract.tex:29 [GPTZero: abstract not scanned]

> A zero-initialised output starts every operator at exact persistence, and all operators are trained with one pushforward curriculum measured in elapsed days and one loss.

*Problem:* Two pieces of jargon arrive in one sentence. 'Exact persistence' is decoded only implicitly, fifteen lines later ('a model that predicts no change'). 'Pushforward curriculum' presupposes knowledge of the MP-PDE training trick. A reader of the abstract alone cannot tell what the operators start from or how they are trained.  
*Fix:* A zero-initialised output makes every operator start as exact persistence, a forecast of no change, and all operators are trained with one loss and one curriculum in which the model is fed its own predictions over a horizon measured in elapsed days.

**L11** [medium] Abstract, 00-abstract.tex:49 [GPTZero: not scanned]

> Replacing the index-space neighbour graph by a dilated stencil that reaches about 0.12\,mm, roughly as far as the lesion front moves between visits, raises the Dice by 0.064 at an identical parameter count, on all five folds.

*Problem:* 'Index-space neighbour graph' is not explained, so the reader cannot see why a 0.12 mm stencil should help. The key point is missing: on the anisotropic grid the index graph reaches far less along one axis.  
*Fix:* Replacing a neighbour graph built on pixel indices, which on this anisotropic grid reaches far less along one axis than along the other, by a dilated stencil that reaches about 0.12\,mm in both directions, roughly as far as the lesion front moves between visits, raises the Dice by 0.064 at an identical parameter count, on all five folds.

**L12** [medium] §1.3 Why Neural PDE Solvers?, 01-introduction.tex:145 [GPTZero: AI]

> The forward operator that maps the present state to the future state is therefore \emph{local}, but its reach must match the distance the front moves between two visits, which differs between directions --- properties that classical solvers build in explicitly through the size and shape of their stencils.

*Problem:* 'Therefore' rests on the previous paragraph (dynamics concentrated at the boundary), not on the anisotropy evidence just given, so the inference reads as a jump. 'Forward operator', 'reach' and 'stencils' appear here for the first time without explanation. The em-dash tail adds a third idea to a sentence that is already long.  
*Fix:* The forward operator that maps the present state to the future state is therefore \emph{local}. Its reach, the distance from which one prediction step draws information, must still match the distance the front moves between two visits, and that distance differs between directions. Classical solvers build such properties in explicitly through the size and shape of their stencils (\S\ref{sec:background:pde-solvers:stencils}).

**L13** [medium] §1.3, 01-introduction.tex:165 (also :164; 04-method.tex:14) [GPTZero: AI]

> The setup --- how elapsed time enters the prediction, how models are trained and how they are evaluated --- is fixed once, and the operator is the only part that changes.

*Problem:* The same object is called 'the setup' here and 'the framework' four lines later, in the research question. In §4.1 (04-method.tex:14), 'the setup' means framework plus operators. A reader cannot tell whether setup and framework are different things.  
*Fix:* The framework --- how elapsed time enters the prediction, how models are trained and how they are evaluated --- is fixed once, and the operator is the only part that changes. (Also change 'the setup around it' at line 164 to 'the framework around it'.)

**L14** [medium] §2.1.1 A short anatomy primer, 02-background.tex:107 [GPTZero: AI]

> As discussed in~\S\ref{sec:introduction:problem}, whether a lesion is subfoveal or extrafoveal materially changes its clinical significance even if its total area is the same.

*Problem:* The back-reference points to §1.2 (Problem Statement), which says nothing about foveal involvement. A reader who flips back finds nothing. The argument is in §1.1.  
*Fix:* As noted in~\S\ref{sec:introduction:motivation}, whether a lesion is subfoveal or extrafoveal changes its clinical significance even if its total area is the same.

**L15** [medium] Figure 2.2 caption, 02-background.tex:170 [GPTZero: AI]

> The same set of anatomical strata corresponds to the ten layer-boundary channels of the eleven-channel state tensor introduced in \S\ref{sec:background:ga-oct:state-rep}.

*Problem:* The caption asserts a known correspondence, so the reader tries to map the roughly nine labelled strata onto ten boundaries. §6.3 later states that the anatomical names of the ten boundaries are not recorded. The two statements read as a contradiction.  
*Fix:* The ten layer-boundary channels of the state tensor (\S\ref{sec:background:ga-oct:state-rep}) trace boundaries within this stack; which anatomical boundary each channel follows is not recorded (\S\ref{sec:discussion:limitations}).

**L16** [medium] §2.1.6 The MUW longitudinal GA cohort, 02-background.tex:458 [GPTZero: AI]

> Pixel spacing is treated as constant across the cohort at approximately $[0.12118,\, 0.003867,\, 0.00568]$\,mm in the $(x, z, y)$ directions, because the scans were resampled upstream to one gold-standard spacing. The resulting fixed physical window is approximately $5.94 \times 5.82$\,mm. This is an assumption whose limits are stated in~\S\ref{sec:discussion:limitations}.

*Problem:* 'This is an assumption' follows the window sentence, so 'this' reads as the window size rather than the constant spacing. The $(x, z, y)$ labels are never tied to the rows/columns vocabulary used from Chapter 3 on, or to $x_i, y_i, L_x, L_y$ in §4.3.2. The reader has to work out which axis is the coarse one.  
*Fix:* Pixel spacing is treated as constant across the cohort at approximately $[0.12118,\, 0.003867,\, 0.00568]$\,mm in the $(x, z, y)$ directions, that is, between B-scans (the rows of the en-face grid), in depth, and between A-scans (the columns), because the scans were resampled upstream to one gold-standard spacing; this is an assumption whose limits are stated in~\S\ref{sec:discussion:limitations}. The resulting fixed physical window is approximately $5.94 \times 5.82$\,mm.

**L17** [medium] §2.1.6, 02-background.tex:476 (repeated in 03-data.tex:65-74, :215-233, 06-discussion.tex:246-257, Appendix A) [GPTZero: AI]

> However, measured on the present cohort, this window is not lossless. It cuts real lesion area in 27.3 per cent of visits.

*Problem:* The cohort facts (553 scans, 75 eyes, 67 native shapes, the 49 × 1024 crop) and the crop census (27.3 / 6.0 / 25.7 / 31.1 %) appear here, again in §3.1/§3.3, again in §6.3 and once more in Appendix A. The reader meets the same numbers three to four times and checks each time whether they differ. The Background also pre-empts the Data chapter.  
*Fix:* In §2.1.6, keep only the literature argument for the 6 mm window and replace the census with one pointer: 'Measured on the present cohort, this window is not lossless; the cost is quantified in~\S\ref{sec:data:spatial}.' Reduce the native-shape sentences to a pointer to §3.1 in the same way.

**L18** [medium] §2.3 Neural PDE Solvers and Surrogate Architectures, 02-background.tex:799 [GPTZero: AI]

> Neural PDE solvers broadly separate into two paradigms.

*Problem:* Two paragraphs earlier (§2.2.4), neural solvers were divided into hybrid and end-to-end solvers. §2.3 now opens with a different two-way division (neural operators vs autoregressive solvers) without relating the two. The reader wonders whether this is the same split under new names.  
*Fix:* Neural PDE solvers can also be divided by what the network predicts.

**L19** [medium] §3.3 Spatial Standardisation, 03-data.tex:222 [GPTZero: AI]

> The models are therefore trained on censored targets, and the change-region metrics at the one-year anchor under-measure progression for roughly one visit in five.

*Problem:* 'Change-region metrics' and 'one-year anchor' are used two chapters before §5.1 defines them, so the reader cannot judge what is being under-measured.  
*Fix:* The models are therefore trained on censored targets, and the evaluation at one year (\S\ref{sec:experiments:protocol}) under-measures progression for roughly one visit in five.

**L20** [medium] §3.5 Patient-Level Covariates, 03-data.tex:272 [GPTZero: AI]

> Each window is accompanied by two patient-level covariates, age and sex.

*Problem:* 'Window' is defined only in §3.6 (03-data.tex:301-306). Until now the word has meant the 49 × 1024 crop window ('The window was nevertheless kept on purpose', §3.3), so the reader first reads 'each window' as 'each crop'. The whole covariate section then depends on the undefined 'window-start ages'.  
*Fix:* Swap §3.5 and §3.6, or define the term here: 'Each training window, a pair of consecutive visits with the interval between them (\S\ref{sec:data:temporal}), is accompanied by two patient-level covariates, age and sex.'

**L21** [medium] §3.6, 03-data.tex:346 [GPTZero: AI]

> With a budget of 90 days, none of the 75 eyes can chain two visits. With 360 days, 74 of the 75 eyes reach at least one autoregressive step. With 540 days, 68 eyes reach at least two steps, and with 720 days, 73 eyes do.

*Problem:* Three expressions describe one quantity ('chain two visits', 'autoregressive step', 'steps'), and 'budget' is used before it is defined. The 90-day statement looks contradictory next to Table 3.1, which lists 67 intervals of exactly 90 days. The reader cannot see that a fed-back step needs two intervals inside the budget; §4.5.2 explains the rule only later.  
*Fix:* During training the model is rolled forward on its own predictions within a time budget (\S\ref{sec:method:training}); each step fed with its own prediction is an \emph{unrolled step}. With a budget of 90 days, none of the 75 eyes can make an unrolled step. With 360 days, 74 of the 75 eyes reach at least one unrolled step. With 540 days, 68 eyes reach at least two, and with 720 days, 73 eyes do.

**L22** [medium] §3.6, 03-data.tex:351 [GPTZero: AI]

> The same schedule also shapes the evaluation. The one-year anchor has no upper bound: the metric is taken at the first rollout step whose cumulative time reaches about 347 days.

*Problem:* Neither 'the one-year anchor' nor 'the metric' has been introduced. 'About 347 days' next to 'exactly 360 days' leaves the reader wondering why the threshold is not one year. The same rule appears elsewhere as 'first rollout step past 0.95 years' (Table E.3) and 'at or beyond 360 days' (§6.3): three phrasings of one rule.  
*Fix:* The same schedule also shapes the evaluation. Models are scored one year after the baseline visit, at the \emph{one-year anchor} (\S\ref{sec:experiments:protocol}). The anchor has no upper bound: it is the first rollout step whose cumulative time reaches 0.95 years, about 347 days. (Use the same wording in §5.1.3 and §6.3.)

**L23** [medium] §4.1, 04-method.tex:32 (also :816, :911; 05-experiments.tex:791) [GPTZero: AI]

> A backbone placed in the slot contains architecture only.

*Problem:* 'Backbone' is a fifth name for the content of the slot, next to operator, model, architecture and arm, and is never distinguished from 'operator'. It recurs in §4.3.7 ('The Runge--Kutta wrapper is not a backbone') and §5.4.  
*Fix:* An operator placed in the slot contains architecture only. (Use 'operator' wherever 'backbone' appears.)

**L24** [medium] §4.1, 04-method.tex:42 (also :210, :633; 02-background.tex:719, :874; 05-experiments.tex:628-646) [GPTZero: HUMAN/AI]

> and a hybrid Finite Element Network (FEN).

*Problem:* 'Hybrid' names three different things: classical-plus-learned solvers (§2.2.4), the FEN (here) and the FNO with a 3 × 3 local path (§4.3, §4.3.4, and 'the hybrid' throughout §5.3.3). In 'the hybrid against the FNO' a reader can mistake the hybrid for the FEN, which was introduced as 'hybrid' first.  
*Fix:* Drop 'hybrid' for the FEN ('and a Finite Element Network (FEN).') and use one fixed name for the FNO variant throughout, e.g. 'the FNO with a local path', as in Table 5.1. Keep 'hybrid' only for the hybrid solvers of §2.2.4.

**L25** [medium] §4.2 The Fixed Framework, 04-method.tex:102 [GPTZero: AI]

> Two reasons support this design. First, the clinical sequences are short, with five to thirteen visits per eye (\S\ref{sec:data:dataset}). Using several past visits as input would leave fewer visits available as prediction targets. Second, the framework predicts strictly one step at a time.

*Problem:* The paragraph announces two reasons for 'one visit in, no memory', but the second reason is about the output (one step per pass, no temporal bundling), which is a different design decision. The closing 'In addition, as noted above, the sequences are so short ...' repeats the first reason. The reader loses track of which decision is being justified.  
*Fix:* Keep the first reason here and give bundling its own paragraph: 'The output is likewise a single step. Some neural PDE solvers, such as MP-PDE, predict several future steps in one forward pass (temporal bundling, \S\ref{sec:background:neural-pde}), but not all of the operators compared here support this, so bundling is removed and every operator makes the same kind of prediction.' Cut the 'In addition, as noted above, ...' sentence.

**L26** [medium] §4.3.3 Graph Construction, 04-method.tex:470 [GPTZero: HUMAN]

> The graph on which messages travel turns out to be the most consequential design decision of the graph solver.

*Problem:* A Method subsection opens with a result the reader cannot yet assess, with no reference to where it is shown; 'turns out' is a narrative tell.  
*Fix:* The graph on which messages travel is the design decision of the graph solver that the experiments find most consequential (\S\ref{sec:experiments:ingredients:reach}).

**L27** [medium] §4.3.3, 04-method.tex:499 [GPTZero: AI]

> After the two message-passing rounds of the canonical configuration, a node has received information from at most four columns away, about $\pm 0.023$\,mm along the row.

*Problem:* In a paragraph about the index-space k-NN graph, 'the canonical configuration' refers to the round count, while elsewhere it means the dilated-stencil model. The reader may conclude that the canonical model uses the k-NN graph.  
*Fix:* After two message-passing rounds, the number used with both graphs, a node has received information from at most four columns away, about $\pm 0.023$\,mm along the row.

**L28** [medium] §4.3.6 The Finite Element Network, 04-method.tex:794 [GPTZero: AI]

> A run is called stable if, in this free-running rollout, the root mean squared error of the mask channel and of the layer channels, both in normalised units, stays at or below 5 on at least 19 of its 20 late epochs.

*Problem:* 'Late epochs' is used before §5.1.3 defines it (epochs 10 to 29), so the reader cannot tell which 20 epochs are meant.  
*Fix:* A run is called stable if, in this free-running rollout, the root mean squared error of the mask channel and of the layer channels, both in normalised units, stays at or below 5 on at least 19 of the 20 late epochs (epochs 10 to 29, over which every reported value is averaged, \S\ref{sec:experiments:protocol:rollout}).

**L29** [medium] §4.3.8 Parameter Matching, 04-method.tex:894 (also :899-900) [GPTZero: AI]

> All architecture arms lie within a factor of 1.25 of the reference. The one-hop floor lies below this band because it is a rung of the locality ladder of~\S\ref{sec:method:family:floors}, not an architecture arm.

*Problem:* Within six lines the reader meets 'architecture arm', 'rung', 'control' and 'reference' as kinds of arm, none of them defined. The per-pixel floor is a 'control', the one-hop floor a 'rung', and the free-form FEN a 'control' of another arm. It is hard to see which arms are meant to be compared with which.  
*Fix:* Open §4.3.8 with the categories: 'The arms fall into three groups: architecture arms, which compare operator classes and are matched in size to the canonical model; the two locality floors, truncations of the graph network that fix how much spatial context is needed; and the free-form FEN controls of the transport term.' The exceptions can then be stated without new labels.

**L30** [medium] §4.5.3 Optimisation, 04-method.tex:1163 [GPTZero: AI]

> Every reported run uses the seed 42; replication runs with the seed 7 are reported in Chapter~\ref{ch:experiments}.

*Problem:* The two clauses of the same sentence contradict each other: every reported run uses seed 42, yet seed-7 runs are also reported.  
*Fix:* All runs of the main comparison use seed 42; replication runs with seed 7 are reported in Chapter~\ref{ch:experiments} and marked as such.

**L31** [medium] §5.1.1 Why Not Per-Pixel Error, 05-experiments.tex:38 [GPTZero: AI]

> The dense operators, such as the U-Net and the Fourier Neural Operator, decalibrate their raw mask regression under autoregressive rollout much more than the graph network does:

*Problem:* 'Decalibrate' and 'calibration' are used in a non-standard sense: the unthresholded mask values drift away from the two target levels. An ML examiner reads them as probabilistic calibration, which a regression output does not have.  
*Fix:* Under autoregressive rollout, the raw (unthresholded) mask values of the dense operators, such as the U-Net and the Fourier Neural Operator, drift much further from the two target levels than those of the graph network: (and at line 43: '... would therefore measure this drift, not the prediction.')

**L32** [medium] §5.1.2 Metrics, 05-experiments.tex:51 [GPTZero: AI]

> The headline metric is the change-region Dice at the one-year anchor.

*Problem:* The headline metric depends on 'the one-year anchor', which has been used since §3.3 but is defined in this chapter only by a back-reference in §5.1.3. The reader never gets one plain sentence saying when the anchor is.  
*Fix:* The headline metric is the change-region Dice at the one-year anchor, the first rollout step at which at least 0.95 years (about 347 days) have passed since the baseline visit (\S\ref{sec:data:temporal}).

**L33** [medium] §5.1.2, 05-experiments.tex:78 [GPTZero: AI]

> Both have a persistence floor of 0 and are easy to confuse: Table~\ref{tab:experiments:arms} and all fold-paired values use the change-region Dice, while the per-eye instrument uses the growth-region Dice (\S\ref{sec:experiments:protocol:stats}).

*Problem:* 'Fold-paired values' and 'the per-eye instrument' are used before §5.1.4 introduces them. 'Persistence floor' adds a third meaning of 'floor', next to the locality floors and the noise floor.  
*Fix:* Both are 0 for persistence and are easy to confuse. The arm table and the fold-paired comparisons use the change-region Dice; the per-eye comparison introduced in~\S\ref{sec:experiments:protocol:stats} uses the growth-region Dice.

**L34** [medium] §5.1.2, 05-experiments.tex:116 [GPTZero: AI]

> For the split reported in~\S\ref{sec:experiments:main-results}, an eye counts as border-touching when its true lesion at the anchor touches the edge of the imaged field:

*Problem:* 'The split' has not been introduced, and elsewhere in the thesis 'split' means the cross-validation split. The reader does not know that a border/interior comparison is coming.  
*Fix:* For the comparison of border-touching and interior eyes in~\S\ref{sec:experiments:main-results}, an eye counts as border-touching when its true lesion at the anchor touches the edge of the imaged field:

**L35** [medium] §5.1.4 Two Statistical Instruments, 05-experiments.tex:217 [GPTZero: AI]

> Two thresholds follow from it. A difference measured on a single fold must exceed 0.036 to count as an effect, and a difference of five-fold paired means must exceed 0.016.

*Problem:* The reader is not shown how 0.0127 becomes 0.036 and 0.016. The two thresholds that govern every verdict in Chapter 5 must be taken on trust.  
*Fix:* If this is the derivation used: Two thresholds follow from it, each about twice the standard deviation of the quantity compared: a difference between two runs on a single fold must exceed 0.036 ($2\sqrt{2} \times 0.0127$) to count as an effect, and a mean of five fold-paired differences must exceed 0.016 (the same divided by $\sqrt{5}$).

**L36** [medium] §5.1.4, 05-experiments.tex:227 [GPTZero: AI]

> Noise affects nulls and effects differently: it can only widen a null.

*Problem:* An aphorism whose claim the reader cannot reconstruct: does a noisier arm make nulls more likely, make effects harder to establish, or widen the interval around a null? The relevance of the mixed floor remains unclear.  
*Fix:* State the point plainly. If this is the intended meaning: 'A wider spread makes an effect harder to establish; it cannot by itself produce one.'

**L37** [medium] §5.3.2 Physical Reach at Lesion Scale, 05-experiments.tex:589 [GPTZero: AI]

> This also explains an earlier result. Before the dilated stencil, the parameter-matched U-Net was higher than the $k$-NN graph network:

*Problem:* 'An earlier result' and 'Before the dilated stencil' refer to the project's chronology, not to anything earlier in the thesis. The reader searches back for a result that was never reported.  
*Fix:* The same comparison explains why the parameter-matched U-Net is higher than the $k$-NN graph network:

**L38** [medium] §5.3.3 Global and Local Context Together, 05-experiments.tex:631 (definition at :253-254) [GPTZero: AI]

> The effect of the local path itself is the hybrid against the FNO: $\Delta = +0.0153 \pm 0.0110$~SE, which is under the paired floor, but per eye $+0.0190 \pm 0.0070$ (48/75), which graduates on that instrument.

*Problem:* §5.1.4 defines 'graduates' as 'established, only when both instruments agree'. 'Graduates on that instrument' uses the word for a single instrument. 'The hybrid' is also ambiguous (see the hybrid finding).  
*Fix:* The effect of the local path itself is the FNO with a local path against the FNO: $\Delta = +0.0153 \pm 0.0110$~SE, which is under the paired floor, but per eye $+0.0190 \pm 0.0070$ (48/75), which clears the per-eye threshold. (At line 254, drop the metaphor: 'A result counts as established only when both agree.')

**L39** [medium] §5.6 Qualitative Analysis and Clinical Comparison, 05-experiments.tex:1459

> \section{Qualitative Analysis and Clinical Comparison}

*Problem:* The title promises a qualitative analysis, but the section contains only the comparison with Mai et al.; the qualitative material is Figure 5.2 (§5.2) and Appendix D. A reader looking for success and failure cases does not find them, and §6.2's 'where the method is known to be weak' has nothing in Chapter 5 to point back to.  
*Fix:* Until the qualitative subsection exists, title the section 'Clinical Comparison' and open it with one sentence pointing to Figure~\ref{fig:experiments:rollout} and Appendix~\ref{app:rollouts} for individual eyes, including the two failure cases described there.

**L40** [medium] §5.6.1 Comparison with Mai et al., 05-experiments.tex:1557 (same wording at 06-discussion.tex:166) [GPTZero: AI]

> The other arms of the survey do not differ from the canonical model on these measures ($r$ between 0.30 and 0.47, fast-progressor AUCs between 0.66 and 0.78; Table~\ref{tab:appendix:growth-speed}), so the gap belongs to the approach, not to one operator.

*Problem:* 'The approach' is ambiguous. It could mean the framework, the mask-based input, the one-visit design or the comparison itself. §6.2 later lists several candidate causes, so the reader does not know which one is meant here.  
*Fix:* The other arms of the survey do not differ from the canonical model on these measures ($r$ between 0.30 and 0.47, fast-progressor AUCs between 0.66 and 0.78; Table~\ref{tab:appendix:growth-speed}), so the gap is shared by every operator of the framework and cannot be attributed to one of them.

**L41** [medium] §5.6.1, 05-experiments.tex:1569 [GPTZero: HUMAN]

> The paper defines the growth rate as the difference between the square roots of the baseline and the respective follow-up area.

*Problem:* The caveat paragraph ends on this sentence without saying why it matters. The reader cannot tell whether this definition differs from the one used here (whole follow-up, per year) or agrees with it.  
*Fix:* State the consequence. If this is the intended caveat: 'The paper defines the growth rate as the difference between the square roots of the baseline and the respective follow-up area; whether it is taken to the last visit, as here, or fitted over all follow-up visits is not stated.'

**L42** [medium] §5.7, 05-experiments.tex:1651 (also :1659-1660) [GPTZero: AI]

> The dual-branch moving-mesh extension costs about $10\times$ its single-branch counterpart (Appendix~\ref{app:mm-pde}).

*Problem:* 'Dual-branch' and 'single-branch' are never defined in the main text, only in Appendix G. The same applies to 'the dual branch is a null' four lines later.  
*Fix:* The moving-mesh extension of Appendix~\ref{app:mm-pde}, which adds a second graph network on an adapted mesh, costs about $10\times$ the single graph network it extends.

**L43** [medium] §6.1 Interpretation of Results, 06-discussion.tex:17 [GPTZero: AI]

> The framework transferred: one setup served operators from unrelated literatures without change. The operator class did not decide the outcome; a small number of properties of the operator did.

*Problem:* 'Transferred' is not defined: from PDE benchmarks to GA, or between operators? 'Setup' is used again as a second name for the framework. The mirrored pair of short sentences reads as a slogan rather than a summary the reader can check.  
*Fix:* The framework served operators from unrelated literatures without change. The outcome was decided not by the operator class but by a small number of properties of the operator.

**L44** [medium] §6.1, 06-discussion.tex:33 (same at 07-conclusion.tex:27) [GPTZero: AI]

> How time enters the update turned out to matter less than that it enters.

*Problem:* An epigram that has to be decoded. It merges a measured point (the scheme made no difference) and an argued point (the interval must reach the operator), which §5.4.1 keeps apart.  
*Fix:* The way the interval enters the update made no measurable difference, provided it reaches the operator: (and the same in Chapter 7, line 27).

**L45** [medium] §6.1, 06-discussion.tex:111 (and §6.4 :328-333) [GPTZero: AI; :328 HUMAN]

> The learned stand-in that the code provides, a layer encoder that summarises the retinal structure into one vector, was tested in an earlier configuration and in one design only, without a detectable benefit.

*Problem:* This is the first appearance of the layer encoder in the compiled thesis; its Chapter 4 description and Chapter 5 results are inside \iffalse. 'The code provides' and 'an earlier configuration' are undefined. §6.4 then criticises design details (predicted layers, 2× anisotropy correction, global conditioning) that the reader has never seen.  
*Fix:* A learned stand-in, a layer encoder that compresses the ten layer maps of a visit into one vector, was tested only on the index-space $k$-nearest-neighbour graph network and in one design, without a detectable benefit; that test is not reported in Chapter~\ref{ch:experiments}.

**L46** [medium] §6.1, 06-discussion.tex:144 (and 07-conclusion.tex:70) [GPTZero: AI]

> Larger models, a higher integration order, a penalty against lesion shrinkage and the moving-mesh extension of Appendix~\ref{app:mm-pde}, whose correction branch never engaged, did not improve accuracy at the available precision.

*Problem:* 'Correction branch' and 'engaged' are Appendix G terms never introduced in the main text. Chapter 7 repeats them as the cause ('did not improve accuracy, because its correction branch never engaged').  
*Fix:* Larger models, a higher integration order, a penalty against lesion shrinkage and the moving-mesh extension of Appendix~\ref{app:mm-pde}, in which the learned weight of the mesh-based correction stayed near zero, did not improve accuracy at the available precision. (Chapter 7: '... did not improve accuracy, because the learned weight of its mesh-based correction stayed near zero.')

**L47** [low] §1.3, Eq. (1.1), 01-introduction.tex:122 [GPTZero: HUMAN]

> writing $A(t)$ for the lesion area and $r(t)$ for an effective radius,

*Problem:* The equation introduces $r_0$ and $v$, but the sentence defines only $A$ and $r$.  
*Fix:* writing $A(t)$ for the lesion area, $r(t)$ for an effective radius with initial value $r_0$, and $v$ for its constant growth speed,

**L48** [low] §2.1 opening, 02-background.tex:18 (and second roadmap at :131) [GPTZero: AI]

> Because the rest of this thesis is written for a primarily machine-learning audience, the present section is deliberately self-contained and aims to remain accessible to readers without prior clinical training:

*Problem:* §2.1 has two roadmaps (the opening paragraph and 02-background.tex:131-138), plus a meta-statement about the audience. The reader spends half a page on navigation before any content.  
*Fix:* Keep the roadmap at line 131 and cut the audience sentence. The opening paragraph can be reduced to its first sentence.

**L49** [low] §2.1.1, 02-background.tex:122 [GPTZero: AI]

> The terminology in this list takes some getting used to, but for the purposes of this thesis it is sufficient to remember the structural fact that the retina is layered, that GA destroys a specific \emph{outer}-retinal stack of three of those layers (\S\ref{sec:background:ga-oct:disease}),

*Problem:* The reader is asked to remember 'three of those layers'. The three named in §2.1.2 include the choriocapillaris, which is not in the retinal list just given (it was introduced as part of the choroid), so the reader cannot match them. The opening clause is conversational.  
*Fix:* For this thesis it is sufficient to remember that the retina is layered, that GA destroys three tightly coupled tissues at its outer side, the RPE, the photoreceptor outer segments and the choriocapillaris beneath them (\S\ref{sec:background:ga-oct:disease}), and that ten boundary depth maps describing the surrounding layer geometry feed the model alongside the lesion mask (\S\ref{sec:background:ga-oct:state-rep}).

**L50** [low] §2.2.1 Adaptive stencils, 02-background.tex:599 [GPTZero: AI]

> The stencil thereby becomes a non-linear function of its input. This is the mechanism closest to what a learned operator does.

*Problem:* The comparison is asserted without the reason; the link only becomes clear in §2.2.4.  
*Fix:* The stencil thereby becomes a non-linear function of its input. This is the mechanism closest to what a learned operator does, whose stencil is likewise a non-linear function of its input (\S\ref{sec:background:pde-solvers:neural}).

**L51** [low] §2.3, 02-background.tex:836 [GPTZero: AI]

> The input distribution at test time therefore differs systematically from the distribution seen during training.

*Problem:* 'At test time' clashes with the repeated statement that the thesis has no test split (§3.7, §5.1). A careful reader wonders whether a test set is meant.  
*Fix:* The input distribution during a rollout therefore differs systematically from the distribution seen during training.

**L52** [low] §2.3, 02-background.tex:849 [GPTZero: AI]

> Two steps are unrolled, and gradients are propagated only through the last. Backpropagating through the first step as well would teach the model to make its errors small rather than to correct them.

*Problem:* 'Make its errors small' and 'correct them' sound like the same goal, so the rationale for stopping the gradient cannot be decoded.  
*Fix:* If this is the intended reading: Two steps are unrolled, and gradients are propagated only through the last. With gradients through the first step as well, the model could lower the loss by changing the perturbation it produces rather than by learning to handle it.

**L53** [low] §3.1 Dataset, 03-data.tex:24 [GPTZero: AI]

> The vendor is logged as Heidelberg Engineering and the protocol as a volume scan in ART mode.

*Problem:* 'ART mode' is never expanded, and nothing later uses it. A reader with little ophthalmology stops at it.  
*Fix:* Expand ART on first use (Heidelberg's automatic real-time tracking, if that is the recorded mode) or drop the mode.

**L54** [low] §3.3, 03-data.tex:235 [GPTZero: HUMAN]

> The training loss can optionally exclude pad positions.

*Problem:* A dangling sentence after the earlier statement that no reported run excludes pad positions. The reader wonders whether the option was used after all.  
*Fix:* Cut it, or merge it into the earlier sentence: 'No reported run excludes the pad positions from the loss, although the option exists (\S\ref{sec:method:training}), so the models are trained to reproduce this value at full weight.'

**L55** [low] §3.6 Temporal Structure, 03-data.tex:340 [GPTZero: AI]

> A training scheme restricted to intervals shorter than the modal 180 days would therefore learn from this densely imaged subgroup alone.

*Problem:* The reader does not know why anyone would restrict training to intervals under 180 days. The link to the 180-day base of the curriculum appears only in §4.5.2.  
*Fix:* This matters for the time unit of the training curriculum (\S\ref{sec:method:training:curriculum}): a curriculum built on intervals shorter than the modal 180 days would learn from this densely imaged subgroup alone.

**L56** [low] §3.7 Splits and Cross-Validation, 03-data.tex:399 [GPTZero: AI]

> The test split is structurally empty. An eye whose patient appeared in neither the training nor the validation list would be assigned to a test partition.

*Problem:* The reader is never told that a test split was planned, so this explanation of why it is empty raises more questions than it answers.  
*Fix:* There is no test split: every patient is assigned to training or validation in every fold, so every result reported in this thesis is a validation result of the five-fold cross-validation.

**L57** [low] §4.1 Overview, 04-method.tex:11 [GPTZero: AI]

> The work began as an adaptation of two graph-based neural PDE solvers, MP-PDE and MM-PDE, which the clinical partner had suggested; the case for their local inductive bias was built and tested only afterwards.

*Problem:* MM-PDE appears here for the first time, unexpanded and undescribed, and then leaves the main text. The reader does not know that it is the moving-mesh extension reported in Appendix G.  
*Fix:* The work began as an adaptation of two graph-based neural PDE solvers suggested by the clinical partner, MP-PDE \citep{Brandstetter2022} and its moving-mesh extension MM-PDE \citep{Hu2024}; the case for their local inductive bias was built and tested only afterwards.

**L58** [low] §4.3.2 Message-Passing GNN, 04-method.tex:384 [GPTZero: AI]

> Before this change, when batch normalisation was used, training and evaluation measurably behaved as two different operators.

*Problem:* 'This change' refers to a project history the reader never saw; the sentence reads like a changelog entry.  
*Fix:* In an earlier version that used batch normalisation, training and evaluation measurably behaved as two different operators.

**L59** [low] §4.3.2, 04-method.tex:399 (after :390-397) [GPTZero: HUMAN]

> In the original, the output head is a one-dimensional convolution.

*Problem:* The decoder is described in two consecutive paragraphs (lines 390-397 and 399-408), and the second repeats the full-rank output layer and the zero-initialised final layer. The reader re-reads to find what is new.  
*Fix:* Merge the two paragraphs. Open with the reason ('The original decodes with a one-dimensional convolution that emits the $K$ bundled steps; with $K = 1$ this head is removed.'), give the MLP description once, and drop the repeated sentences.

**L60** [low] §4.3.4 Dense Operators, 04-method.tex:589 [GPTZero: AI]

> The schedule was deliberately not tuned further, because a comparison model whose geometry has been optimised against this dataset would be a weaker control, not a stronger one.

*Problem:* Calling the U-Net a 'comparison model' and a 'control' casts the graph network as the subject and the U-Net as its check. This contradicts §4.1 ('all operators on the same terms') and §5.2 ('none is a baseline to be beaten'), so the reader is unsure whether the comparison is symmetric. The sentence also ends in an antithesis ('weaker ..., not a stronger one').  
*Fix:* The schedule was deliberately not tuned further: an operator whose geometry has been optimised against this dataset would make the comparison less controlled.

**L61** [low] §4.3.7 Fixed-Step Runge--Kutta Integration, 04-method.tex:845 (and :849-852) [GPTZero: AI]

> The update itself is not zero: the state still changes by the integrated rate.

*Problem:* The sentence answers a confusion it never states. The next sentences introduce a 'learned Runge--Kutta integrator' variant without saying whether any reported result uses it.  
*Fix:* Setting the $\Delta t$ input to zero does not set the update to zero: the state still changes by the integrated rate. (Also state whether the learned-integrator variant enters any reported result; if it does not, say so or cut the sentence.)

**L62** [low] §4.5.2 Time-Budgeted Pushforward Curriculum, 04-method.tex:1104 [GPTZero: AI]

> Each training pass draws a time budget $B$ uniformly from $\{0, 1, \dots, \min(e, U)\} \times 180$ days, where $e$ is the current epoch.

*Problem:* $U$ appears in the formula without a meaning; it is only set ('$U = 2$') two sentences later.  
*Fix:* Each training pass draws a time budget $B$ uniformly from $\{0, 1, \dots, \min(e, U)\} \times 180$ days, where $e$ is the current epoch and $U$ the largest number of 180-day units.

**L63** [low] §5.1.3 Rollout and Reporting, 05-experiments.tex:206 [GPTZero: HUMAN]

> All experiments use the patient-level five-fold cross-validation of~\S\ref{sec:data:splits}, which has no test split; every result is a validation result.

*Problem:* A one-sentence paragraph after the figure that repeats §3.7 and interrupts the step from reporting to statistics. It reads as a leftover.  
*Fix:* Move it into the opening paragraph of §5.1, or cut it.

**L64** [low] §5.4.2 The Objective, 05-experiments.tex:931 [GPTZero: AI]

> The penalty therefore enforces different priors on teacher-forced and on unrolled steps.

*Problem:* 'Teacher-forced' appears only here. Elsewhere the thesis says 'a plain one-step pass on observed inputs' (§4.5.2).  
*Fix:* The penalty therefore enforces different priors on steps that start from an observed state and on unrolled steps.

**L65** [low] §5.6.1, 05-experiments.tex:1562 (also Table 5.6 caption :1504) [GPTZero: AI]

> The comparison is an anchor, not a head-to-head result.

*Problem:* 'Anchor' already means the one-year evaluation time. Here and in the Table 5.6 caption it means a reference value, so the same section uses the word in two senses.  
*Fix:* The comparison is a point of reference, not a head-to-head result.

**L66** [low] §5.7 Computational Cost, 05-experiments.tex:1630 [GPTZero: AI]

> An earlier explanation of the spread by several runs sharing one GPU was checked and does not hold: no two runs ever shared a GPU.

*Problem:* It refutes an explanation the reader never encountered, which belongs to the project's history. It raises a question instead of answering one.  
*Fix:* Cut it, or: 'Runs sharing a GPU are not a cause: no two runs ever shared one.'

**L67** [low] §6.4 Future Work, 06-discussion.tex:314 [GPTZero: HUMAN]

> The fixed centre crop censors growth for about a third of the cropped lesions.

*Problem:* §3.3 and §6.3 state the same fact as '31.1 % of the visits'. 'A third of the cropped lesions' changes the denominator, so the reader wonders whether a different statistic is meant.  
*Fix:* The fixed centre crop censors growth in about a third of the visits.

**L68** [low] Appendix G.2.2 Dual-Branch Composition, 91-appendix.tex:709 [GPTZero: AI]

> Gradients are clipped to a norm of 1.0 separately in five groups: the uniform branch, the correction branch, the ItpNet weights, the gate $\alpha$ and the layer encoder; the mesh mover is frozen.

*Problem:* The layer encoder is not part of the dual-branch model as described and is not introduced anywhere in the compiled thesis, so the reader wonders whether it was active in these runs.  
*Fix:* If it was off in these runs, add '(when enabled; off in the reported runs)' after 'the layer encoder', or drop it from the list.

**L69** [low] List of Abbreviations, acronyms.tex:24

> \acro{SWE}{Shallow Water Equation}

*Problem:* A reader who turns to the list to decode an abbreviation finds SWE (not used in the text) and DMM/ItpNet (appendix only). FEN, T-FEN, RK4, FAF, SLO, RPE, CFL, WENO, cRORA/iRORA, k-NN, SE and AUC, which carry Chapters 2-5, are missing.  
*Fix:* Add the abbreviations used in the main text (FEN, T-FEN, RK4, FAF, SLO, RPE, CFL, FDM, FVM, FEM, WENO, cRORA, iRORA, CAM, ONH, k-NN, SE, AUC) and remove SWE.

## Terminology and first definitions

| Term | First use | Defined at | Problem | Fix |
|---|---|---|---|---|
| arm | 04-method.tex:46 ('The arms are parameter-matched ...'); earlier, in another sense, 02-background.tex:319 ('sample arm' of the OCT interferometer) | never defined | This is the basic experimental unit of Chapters 4-5 and Appendix E, yet the reader has to infer what it means. The earlier optical sense is a different object. | Define it in §4.1: 'Each setting of the operator slot, trained and evaluated on all five folds, is called an arm.' Use 'arm' only for experimental settings. |
| operator / model / backbone / architecture / network | 01-introduction.tex:152 (operator); 04-method.tex:32 (backbone) | operator: 01-introduction.tex:152-154; backbone: never | Five words are used for the content of the slot. 'Backbone' is never distinguished from 'operator' (§4.1, §4.3.7 'The Runge--Kutta wrapper is not a backbone', §5.4), and 'model' sometimes means operator plus framework. | Use 'operator' for $f_\theta$ and 'arm' for an experimental configuration, and drop 'backbone'. |
| canonical (model / configuration / fold / scheme / setting / update) | 03-data.tex:252 ('The canonical scheme is a z-score') | The model is identified only in Table 4.2 (04-method.tex:930) and justified in §5.3.2 (05-experiments.tex:506-508). 'Canonical fold' (= fold 2) is never defined. | The word is overloaded and used before it is defined. At 04-method.tex:41 the reader is told 'one of which is the canonical model' without being told which one. At 04-method.tex:500 it labels the round count of the k-NN graph, and at :821 the Euler update. | Reserve 'canonical' for the dilated-stencil graph network and define it at 04-method.tex:41 with a pointer to §5.3.2. Write 'fold 2' instead of 'canonical fold', and drop 'canonical' for the z-score, the age mode and the Euler update. |
| floor (locality floor / noise floor / persistence floor / paired, mixed, single-fold floor) | 04-method.tex:46 ('marks the lower floor') | locality floors: 04-method.tex:651-691; noise floor: 05-experiments.tex:213-228; 'persistence floor of 0' (05-experiments.tex:78): not defined | Three meanings, sometimes in one sentence. The Table 5.1 caption reads: 'with the two locality floors and persistence at the bottom; adjacent arms mostly differ by less than the noise floor.' | Keep 'floor' for the two truncated models and call the statistical quantity a 'noise threshold' (paired, single-fold, mixed). Write 'is 0 for persistence' instead of 'persistence floor'. |
| persistence | 00-abstract.tex:30 ('exact persistence'); main text 04-method.tex:52 | 04-method.tex:52 ('The persistence baseline, which predicts no change'); 05-experiments.tex:27 | In the abstract it is decoded only implicitly, fifteen lines later. The definition in §4.1 is fine. | Gloss it at first use in the abstract: 'persistence, a forecast of no change'. |
| deficit / reach deficit | 00-abstract.tex:53; 01-introduction.tex:202 | 05-experiments.tex:757-761 (§5.3.5 Two Routes to One Deficit) | Used in the abstract, the contribution paragraph of §1.3, §5.2 and §5.3.2 before it is defined. Until §5.3.5 the reader cannot know which deficit is meant. | At each first use (abstract, §1.3, §5.2), add: 'an update that sees less far than the lesion front moves between two visits'. |
| one-year anchor / anchor | 03-data.tex:223 | Only partially: 03-data.tex:351-355 ('about 347 days'), 05-experiments.tex:145-146 (back-reference), Table E.3 caption ('past 0.95 years'), 06-discussion.tex:279 ('at or beyond 360 days') | There is no single plain definition, and the same rule is phrased three different ways. 'Anchor' also means 'reference value' in §5.6.1 (05-experiments.tex:1504, :1562). | Define it once in §5.1.2 ('the first rollout step at which at least 0.95 years have passed since the baseline visit') and repeat that wording in §3.6 and §6.3. Replace the second sense by 'point of reference'. |
| hybrid | 02-background.tex:719 ('Hybrid solvers') | 02-background.tex:719-724 (classical + learned); 02-background.tex:874 (global + local architectures); 04-method.tex:42 (the FEN); 04-method.tex:633 (FNO + 3×3) | Four uses for three different objects. 'The hybrid' in §5.3.3 can be read as the FEN, which was introduced as 'hybrid' first. | Name the FNO variant consistently 'FNO with a local path' (as in Table 5.1), drop 'hybrid' for the FEN, and keep 'hybrid' only for the solvers of §2.2.4. |
| window (crop window / transition window / late-epoch window) | 02-background.tex:69 (OCT scanning window) | transition window: 03-data.tex:301-306; late-epoch window: 05-experiments.tex:168 | 'Each window is accompanied by two covariates' (03-data.tex:272) comes before the transition window is defined and right after §3.3's 'The window was nevertheless kept', which refers to the crop. | Use 'crop' for the spatial window. Use 'transition window' only after §3.6 defines it (or move §3.6 before §3.5), and write 'epochs 10 to 29' or 'late-epoch range' for the reporting range. |
| setup vs framework | 01-introduction.tex:164 | framework: 01-introduction.tex:189-192; setup: never | 'Setup' means the framework in §1.3, framework plus operators in §4.1 (04-method.tex:14), and appears again in §6.1 and Chapter 7. | Use 'framework' only. |
| late epochs / late-epoch mean | 04-method.tex:796 ('20 late epochs') | 05-experiments.tex:166-167 | The T-FEN stability criterion in §4.3.6 relies on 'late epochs' one chapter before their definition. | Add '(epochs 10 to 29, \S\ref{sec:experiments:protocol:rollout})' at 04-method.tex:796. |
| instrument / fold-paired / per eye (k, m) | 05-experiments.tex:79-80 | 05-experiments.tex:230-251 | Used before the definition. 'Instrument' is a metaphor for a statistical test. The counts k and m are defined as 'same sign as the mean' but used as 'first arm higher'. | Avoid the forward uses at :79-80 or point to §5.1.4. Redefine k and m as 'the number of folds (eyes) on which the first arm is higher'. |
| graduate / established | 05-experiments.tex:254 | 05-experiments.tex:253-254 ('established --- it graduates --- only when both agree') | Two words for one concept, and 'graduates on that instrument' (05-experiments.tex:633) contradicts the definition. | Use 'established' only. |
| null / negative result | 05-experiments.tex:455 ('are nulls against their single-step counterparts') | 05-experiments.tex:787-789 | Used as a noun before it is defined. | At 05-experiments.tex:455 write 'show no measurable difference from their single-step counterparts'. |
| survey vs comparison | 04-method.tex:265 ('arm of the survey') | never; Chapter 1 calls it 'a controlled comparison' (01-introduction.tex:200) | The reader is not told that 'the survey' is the controlled comparison of operators in the slot. | Introduce it once ('this controlled comparison, referred to as the survey') or use 'comparison' throughout. |
| ingredient vs property | 02-background.tex:897 ('inductive-bias ingredients') | 02-background.tex:892-897 | The abstract, §6.1 and Chapter 7 speak of 'properties', Chapter 5 of 'ingredients'. The four-item list in §2.3 differs from the three ingredients established in §5.3, which the reader has to reconcile. | Pick one word, or keep the §2.3 link explicit: 'properties, here called ingredients'. |
| change-region Dice / change-region metrics | 00-abstract.tex:37/43; 03-data.tex:223 | 05-experiments.tex:51-67 | Chapter 3 uses 'change-region metrics' two chapters before the definition. | In Chapter 3, write 'the evaluation metrics (\S\ref{sec:experiments:protocol})'. |
| unrolled step / chain two visits / autoregressive step / pushforward | 02-background.tex:849; 03-data.tex:345-349 | 04-method.tex:1120-1127 (undershoot rule) | Three phrasings describe the same count in §3.6, and the 90-day statement looks contradictory without the undershoot rule. | Define 'unrolled step' once ('a step whose input is the model's own previous prediction') and use only that term. |
| dual branch / single branch / correction branch / gate / bypass control | 05-experiments.tex:1651; 06-discussion.tex:146; 07-conclusion.tex:71 | only in Appendix G (91-appendix.tex:529-534, 651-675) | The main-text conclusions use vocabulary that exists only in the appendix. | In the main text, write 'the moving-mesh extension, a second graph network on an adapted mesh whose contribution is weighted by a learned gate'. |
| layer encoder | 06-discussion.tex:112 | never in the compiled text (04-method.tex:994-1009 is inside \iffalse) | Discussed and criticised in §6.1 and §6.4, and listed among the clipping groups in Appendix G, without any description. | Add one sentence of description at 06-discussion.tex:112: what it is, where it was tested, and that the test is not reported. |
| graph solver / graph network / GNN / stencil GNN / dilated-stencil network / k-NN arm | 04-method.tex:39 | 04-method.tex:262 | Chapter 4 says 'graph solver', Chapter 5 'graph network', and the tables use 'Stencil GNN', 'Dilated-stencil GNN' and 'Graph network, dilated stencil'. The reader has to check whether these are different models. | Fix one name per arm (e.g. 'stencil graph network', 'k-NN graph network') and use it identically in text and tables. |
| decalibrate / calibration | 05-experiments.tex:39 | never | Non-standard sense (drift of the raw mask values from the two target levels), which an ML reader reads as probabilistic calibration. | Write 'drift of the raw (unthresholded) mask values'. |
| teacher-forced | 05-experiments.tex:932 | never | This is the only use; elsewhere the thesis says 'one-step pass on observed inputs'. | Write 'steps that start from an observed state'. |
| MM-PDE | 04-method.tex:12 | 91-appendix.tex:401 (Appendix G); acronym list only | Unexpanded and undescribed in the main text. | Write 'its moving-mesh extension MM-PDE \citep{Hu2024}' at first use. |
| lift | 05-experiments.tex:70 | never | Jargon that appears only once. | Write 'every positive value is an improvement over "no progression"'. |
| project (as in 'the largest effect in the project') | 05-experiments.tex:506 | n/a | 'Project' and 'thesis' alternate (also 07-conclusion.tex:50 and 91-appendix.tex:857), so the reader may wonder whether results outside the thesis are included. | Write 'in this thesis'. |


---

# Part 1 (detail) — AI tone: what drives the GPTZero flags

GPTZero rates every chapter "AI Generated" at the document level and flags between 67 % (Ch. 1) and 89 % (Ch. 7) of the words. The flags are not reliable. Chapter 3 is mostly plain, procedural description of files, counts and thresholds, and 82 % of it is still flagged. Constructions GPTZero flags in one place are judged human in another: "turns out" (04:470), "What matters is where the neighbours are placed, not how many there are" (05:586) and "fundamentally" (02:826). The flags are therefore best used as a pointer to passages worth reading closely.

Read that way, they do point at real habits. Classic AI vocabulary (delve, multifaceted, testament, pivotal, leverage, moreover) is essentially absent. The machine-like tone comes from rhetoric and structure. The most frequent sources, roughly in order of how much they affect the reading, are:
- contrast frames used as the main claim ("not X but Y", "X, not Y", "rather than"; about 90 in total, about 25 of them evaluative);
- paragraph-final verdicts that restate the paragraph, usually with "therefore" (about 40);
- cleft and pseudo-cleft sentences (about 30);
- mirrored verdict pairs and parallel catalogues (about 25);
- announce-then-enumerate sentences (about 14);
- a dense chain of consequence connectives (71 "therefore", about 108 ", so");
- em-dash asides (63 dashes);
- two-part sentences built on semicolons and colons (about 190 of each);
- stock intensifiers, concentrated in §2.1, §2.3, the related work and Appendix G.1 (about 30);
- idioms and abstractions acting as agents (about 40);
- roadmap paragraphs (about 30);
- slogan-style run-in headings (about 10);
- over-explaining glosses in §2.1 (about 10);
- statistical sentences in Ch. 5 that repeat one template (about 40).

The interpretive passages carry most of these: Ch. 6, Ch. 7, the closers of §5.2–§5.5, and the openings of sections. The two sections that read most like a generic survey are §2.3 (and the related work) and Appendix G.1. Fixing them gains the most for the least editing. The aim is clearer, more grounded prose. A lower detector score may follow, but it should not be the target, because technical prose with fixed terms and numbers is predictable by nature.

## What the sentences judged human do differently

Basis: 367 complete sentences judged [HUMAN] and 1,489 flagged [AI], taken from all eight tagged scans. Headings, tables, page-header fragments and unfinished sentences were removed first.

1) Length and rhythm. The human-judged sentences are shorter.
- Mean length is 16.4 words (median 14), against 20.7 words (median 19) for flagged sentences.
- 41 % of human-judged sentences have 12 words or fewer, against 27 % of flagged ones.
- Only 9.5 % of human-judged sentences reach 30 words or more, against 18.5 % of flagged ones.
- Within a paragraph, the variation in sentence length is about the same in both groups (coefficient of variation 0.44 against 0.46).
- So the difference is not "bursty" versus even paragraphs. It lies in how many sentences are long two-clause constructions.

2) Connectives and punctuation. Flagged sentences carry the reasoning markers much more often.
- "therefore" or "thus": 4.8 % of flagged sentences against 1.6 % of human-judged ones, three times as often.
- Contrast frames ("rather than", "not … but", ", not"): 4.4 % against 1.6 %.
- Semicolons: 10 % against 6.5 %.
- Colons: 12.4 % against 8.7 %.
- "X, Y and Z" lists of three: 3.2 % against 1.6 %.
- Sentences opening "This/These/It is/means/shows…": 2.6 % against 1.4 %.

3) Concreteness and attribution.
- Human-judged sentences carry an author-year citation about twice as often (16 % against 9 %).
- Numbers do not protect a sentence: 39 % of human-judged and 46 % of flagged sentences contain a digit, because the templated statistical strings of Ch. 5 are flagged.

4) What the sentence does. This is the clearest difference.
- Human-judged runs report something specific: what a source found (01:47 "Until 2023, the therapeutic landscape for GA was empty: …"), what was done to a file (Ch. 3: "The stored mask, which has the values 0 and 255, is thresholded above 127"), where a variation comes from (03:68 "The variation stems from the raw acquisitions, whose B-scan spacing ranged from 115 to 258 µm"), what a probe measured (91:873), or a dated correction (Appendix G: "That was the case in the implementation until 6 August 2026; dual-branch results from before that date are not used").
- They also state limitations flatly (06:169 "The comparison is not like-for-like."; 07:67 "The negative results are part of the answer. Larger models did not help …"), list concrete causes (06:177–184), use run-in questions (05:873 "Is the weighting of the mask channel needed?"), and hedge with a reason (01:157 "For GA, where the governing equation is unknown and only a few dozen patients are available for training, these assumptions are likely to matter more than model size.").
- Flagged runs mostly interpret, generalise, announce or summarise. Examples: "This is the structural fingerprint of …", "What separates the arms is therefore not their class but …", "The clinical implication is twofold.", "This section provides …", "What the framework needs, in short, is …".
- Even plain flagged sentences in Ch. 3 and Ch. 4 share one property: they are uniform "The X is Y" descriptions with no source, date or procedural detail attached.

5) Hedging style.
- Both groups hedge about equally often (about 6.5 % contain may/might/about/roughly/likely).
- The human-judged hedges come with a reason or a scope ("on this grid", "until 6 August 2026", "in a small cohort").
- The flagged hedges are formulaic ("at the noise level", "suggestive rather than a proof of mechanism").

Caveats.
- GPTZero labels runs of text, not single sentences, so the human-judged "islands" are often short and sit next to page breaks.
- No single device decides the label. The pattern is one of density: a paragraph that piles several of the devices above into a summary is flagged, while the same device inside a concrete, attributed report often is not.

## Chapter profiles

| Chapter | Flagged share | Character of the prose |
|---|---|---|
| Abstract (English, 00-abstract.tex l. 16-65) | not scanned | Dense, technical, mostly plain. The tells sit at the turns. Staccato verdicts: "The largest is physical reach." A two-part sentence joined by a semicolon: "a second route to the same deficit; these two are the two highest operators". The abstract also ends on a contrast: "…, not which family the operator belongs to." There are no em-dashes and no intensifiers. It has the highest colon density of any part (6.3 per 1000 words). |
| Ch. 1 Introduction | 66.9 % (1316 of 1966 words) | Least flagged. The clinical facts, each attributed to a source (bilateral GA, failed trials, the FDA approvals), are judged human. The flags fall on the framing rhetoric, in particular: - "The clinically relevant question is therefore not whether … but how fast and where" - "The clinical implication is twofold. First, … Second, …" - "the critical decision support task" - "This is the structural fingerprint of …" - "naturally framed" and "naturally multi-channel" - 7 em-dashes, the highest density outside Ch. 7 - "What the thesis delivers follows from this design." - "The remainder of this thesis is organised as follows." |
| Ch. 2 Background | 84.0 % (6073 of 7230 words) | Textbook exposition with a tutoring register. - It has the most em-dashes (22), the most "rather than" (13) and most of the stock intensifiers (fundamentally ×5, naturally, inherently, reliably, essentially, precisely, materially, plainly). - It uses glosses that restate in a second voice ("In other words", "Put differently", "Concretely", "takes some getting used to", "a small piece of optical engineering"). - Its signposting is heavy (the opening paragraph of §2.1, the roadmap of §2.2). - §2.3 and the related work read as a generic survey: "broadly separate into two paradigms", "Note that", "Furthermore … Finally …", "the principal cost", "the central training difficulty", "Consequently, this thesis sits at the intersection of …". - The human-judged runs are the CAM criteria, the OCT signatures with sources, and short definitional sentences ("A single A-scan is one column of one image."). |
| Ch. 3 Data and Preprocessing | 81.6 % (2442 of 2993 words) | Plain, factual and procedural, with no em-dashes and no intensifiers. Most of the flags therefore reflect how GPTZero treats predictable technical enumeration ("The acquisition setting recorded in the data is the same for all 553 visits." is flagged). The real tells are few: - "Two consequences follow. First, … Second, …" - "The window was nevertheless kept on purpose." - a restating closer: "The layer geometry is therefore kept in full rather than reduced to the lesion mask alone." - 7 "therefore" and a uniform "The X is Y" rhythm The human-judged runs are procedure (thresholding, casting, z-scoring) and grounded judgements ("Zero-padding raises a less obvious problem."). |
| Ch. 4 Method | 79.4 % (7698 of 9698 words) | Dense description of architectures. - It has the highest semicolon density (8.2 per 1000 words), 16 "therefore", about 30 ", so" clauses and 14 em-dashes. - Roadmap chains: "§4.3.1 states …, §4.3.2 describes …". - An anaphoric catalogue: "A U-Net tests … A Fourier Neural Operator tests …". - Mini-verdict sentences: "This form has a useful limit.", "Every arm starts from the same function.", "The Runge–Kutta wrapper is not a backbone." - "turns out" and "turned out". - The human-judged runs summarise the original papers and implementation steps (the encoder layers, the seeding, the autonomous field). |
| Ch. 5 Experiments | 78.6 % (9084 of 11555 words) | Results prose dominated by statistics. - About 40 sentences repeat the template "X against Y gives Δ = … SE (k/5) and per eye … (m/75, t = …)". - It has the most "therefore" (24) and ", so" (37), the most colons (67), and 12 contrast frames of the form ", not". - Verdict closers end most subsections: "What separates the arms is therefore not their class but the ingredients they carry.", "The objective, not the operator, decides …", "Capacity is therefore not a lever …". - It uses idioms (buys, bought, earns, lever, luckiest, blind to) and abstractions that act ("Two tests ask this", "Two arguments speak against"). - The human-judged runs are run-in questions, plain one-line results ("A higher degree at the same reach buys nothing.") and short procedural statements. |
| Ch. 6 Discussion | 82.2 % (2391 of 2910 words) | Synthesis prose. - It has the most run-in heads (18), several of them slogans: "The operator: ingredients, not classes.", "Where modelling effort pays.", "Good at where, weaker at how fast." - It opens with a mirrored verdict pair: "The framework transferred … The operator class did not decide the outcome; a small number of properties … did." - Clefts: "This is what made … possible at all", "What the framework needs, in short, is …". - It has a high contrast density (3.1 per 1000 words). - The human-judged runs are the clinical paragraphs that state limitations and list causes plainly (§6.2: "The comparison is not like-for-like.", "Several explanations are possible …"). |
| Ch. 7 Conclusion | 89.4 % (693 of 775 words) | Highest share. Conclusions restate verdicts by design, so some predictability cannot be avoided. The chapter also has the highest em-dash density (5.3 per 1000 words) and contrast density (3.9 per 1000 words). Examples: - aphoristic closers: "How time enters the update mattered less than that it enters", "more informative than the score of any single model" - a "Take-away." head whose sentence ends on "--- above all, … --- rather than the choice of operator family" The only human-judged run is the plain list of negative results ("The negative results are part of the answer. Larger models did not help …"). |
| Appendices (91-appendix.tex) | 71.2 % (4736 of 6648 words) | Two registers. - G.1 (the MM-PDE background, still unrevised by the author) is the most generic text in the thesis: "fundamentally inefficient", "a property that is hostile to", "entirely supervised", "precisely where", "Crucially", "critical; … inevitably yields a tangled and useless mesh", "Intuitively", "dictates". - G.2–G.4 are concrete and largely judged human (the probe with gradient norms, the dated edge fix, the configuration choices). - G.4 closes with a dash-wrapped verdict: "--- with the moving mesh or with the uniform grid in its place, with or without weight decay, with or without the gate ---". - Captions in A, D and E are flagged mostly because of their enumerative style. |

## Recurring patterns, each with a global fix

The examples below are real sentences from the thesis; several of them also appear as items in the micro files.

### P1. Contrast frames that carry the main claim ("not X but Y", "X, not Y", "rather than" used as the point of the sentence or the paragraph closer)

*Frequency:* About 90 contrast frames in running prose: 38 "rather than", 27 ", not …" in apposition, 14 "instead of", 9 "not … but". About 25 of them are evaluative and carry the claim or close a paragraph. Densest in Ch. 7 (3.9 per 1000 words) and Ch. 6 (3.1 per 1000 words).  
*Why it reads as generated:* Generated prose habitually defines a thing by what it is not: it sets up a reading nobody proposed and then knocks it down. When the excluded alternative was never a live option, the contrast is rhetoric rather than information. Ending a paragraph on a negation also gives it the cadence of a slogan. Contrasts that record a design choice ("centre crop rather than resampling", "index space instead of physical coordinates") are not the problem.  
*Global fix:* Keep a contrast only where the alternative was actually tested or is a likely misreading. Otherwise state the positive claim alone. If the rejected reading has to be named, put it first and end the sentence on the positive claim. Never close a paragraph on "…, not X".

- `01-introduction.tex:43 (§1.1; GPTZero: AI)`
  - Original: The clinically relevant question is therefore not \emph{whether} a patient will deteriorate, but \emph{how fast} and \emph{where} in the macula the lesion will grow.
  - Rewrite: Deterioration itself is expected. The clinically relevant questions are \emph{how fast} and \emph{where} in the macula the lesion will grow.
- `05-experiments.tex:882 (§5.4.2; GPTZero: AI)`
  - Original: The objective, not the operator, decides whether the model learns any change at all.
  - Rewrite: Since the operator is the same in both runs, whether any change is learned is determined by the objective.
- `02-background.tex:784 (§2.2.5; GPTZero: AI)`
  - Original: These are reasons to expect the structure to fit, not evidence that it does.
  - Rewrite: These four points motivate the structure but do not show that it fits.
- `00-abstract.tex:62 (Abstract; not scanned)`
  - Original: For forecasts of this kind, the decisive design question is how far one update reaches compared with how far the disease moves between visits, not which family the operator belongs to.
  - Rewrite: For forecasts of this kind, the decisive design question is not the family of the operator but how far one update reaches compared with how far the disease moves between visits.

### P2. Restating verdict closers (a paragraph ends on a sentence that repeats it at a higher level of abstraction, usually "X is therefore Y" or "This is the …")

*Frequency:* About 35–40. Roughly 30 of the 71 "therefore" sit in such closers. Most frequent in §5.2–§5.5, Ch. 6 and Ch. 7.  
*Why it reads as generated:* An LLM draft habitually closes each paragraph with a moral. The reader gets the claim twice, and the abstract nouns these closers rely on ("fingerprint", "lever", "the answer", "artefact") signal rhetoric rather than evidence. Repeated after every paragraph, it gives the text a lecturing rhythm.  
*Global fix:* End a paragraph on its last piece of evidence or on a pointer to where the point continues. Keep one verdict per subsection, at its end (for example §5.3.5 or §6.1). Delete closers that only restate the sentence before them.

- `01-introduction.tex:135 (§1.3; GPTZero: AI)`
  - Original: This is the structural fingerprint of a system governed by a temporal partial differential equation with strong spatial localisation.
  - Rewrite: Dynamics confined to a moving boundary in this way are typical of a temporal partial differential equation with strong spatial localisation.
- `02-background.tex:440 (§2.1.5; GPTZero: AI)`
  - Original: The layer channels are therefore not auxiliary context; they carry rate-of-change information that the mask alone cannot provide.
  - Rewrite: The layer channels thus carry information on the rate of change that the mask alone cannot provide.
- `03-data.tex:172 (§3.2; GPTZero: AI)`
  - Original: The layer geometry is therefore kept in full rather than reduced to the lesion mask alone.
  - Rewrite: (Delete. The preceding sentence already says that all ten layer channels are kept and why.)
- `05-experiments.tex:1074 (§5.4.3; GPTZero: AI)`
  - Original: Capacity is therefore not a lever on this task in any of the four classes, and the comparisons at matched size in~\S\ref{sec:experiments:main-results} and~\S\ref{sec:experiments:ingredients} are not an artefact of the size at which they were made.
  - Rewrite: In none of the four classes did a larger operator improve on its original size by more than the floor, so the matched-size comparisons of~\S\ref{sec:experiments:main-results} and~\S\ref{sec:experiments:ingredients} are not an artefact of the size at which they were made.

### P3. Cleft and pseudo-cleft sentences ("What X needs is …", "This is what/why …", "… is what …")

*Frequency:* About 30: 14 sentences that open with "What …" and 17 with "This is what/why/the …" or "… is what …". Concentrated in Ch. 5 and Ch. 6.  
*Why it reads as generated:* A cleft delays the real subject to create emphasis. It is a staple of persuasive and generated summary prose, and in results writing it sounds staged ("This is what made … possible at all"). The subject is usually already known, so the emphasis adds nothing.  
*Global fix:* Make the real subject the grammatical subject. Use "This is why" only for a genuine causal link, and replace a bare "This" with the noun it stands for.

- `06-discussion.tex:47 (§6.1; GPTZero: AI)`
  - Original: What the framework needs, in short, is a loss that puts weight on the lesion mask, an interval length that reaches the operator, and everything else held fixed.
  - Rewrite: The framework therefore requires a loss that puts weight on the lesion mask and an interval length that reaches the operator, with everything else held fixed.
- `06-discussion.tex:29 (§6.1; GPTZero: AI)`
  - Original: This is what made the comparison of Chapter~\ref{ch:experiments} possible at all, and it is the answer to the first part of the question.
  - Rewrite: The comparison of Chapter~\ref{ch:experiments} rests on this result, which also answers the first part of the question.
- `05-experiments.tex:852 (§5.4.1; GPTZero: AI)`
  - Original: What the update needs is that the length of the interval reaches the operator at all, either as an input to a single step or through an integrator that steps over the interval; how it arrives makes no measurable difference.
  - Rewrite: The update needs the length of the interval to reach the operator, either as an input to a single step or through an integrator that steps over the interval; the route makes no measurable difference.
- `02-background.tex:745 (§2.2.4; GPTZero: AI)`
  - Original: What the learned version gains is that $f$ no longer has to be written down: it is fitted to data, so the solver can be used where the equation is expensive to solve, known only approximately, or not known at all, and it can often run on coarser grids with larger steps. What it loses are the guarantees.
  - Rewrite: A learned $f$ no longer has to be written down. It is fitted to data, so the solver can be used where the equation is expensive to solve, known only approximately, or not known at all, and it can often run on coarser grids with larger steps. The classical guarantees are lost in exchange.

### P4. Mirrored verdict pairs, staccato verdicts and parallel catalogues

*Frequency:* About 25. Mirrored or staccato pairs open Ch. 6, Ch. 7, §4.3.7 and §5.5 and appear in several abstract sentences. Anaphoric catalogues include the six "A X tests Y" sentences at the start of §4.3.  
*Why it reads as generated:* Short, balanced sentences with the same syntax ("The framework transferred. … The operator class did not decide the outcome; a small number of properties … did.") read as composed for effect. Lists in which every item is a sentence with the same subject–verb–object shape are a recognisable generated pattern; human authors vary the shape or merge minor items.  
*Global fix:* Merge a mirrored pair into one sentence and make one clause depend on the other. In catalogues, vary the shape: give one sentence to the main items and a clause to the minor ones.

- `06-discussion.tex:16 (§6.1; GPTZero: AI)`
  - Original: The results answer the two parts differently. The framework transferred: one setup served operators from unrelated literatures without change. The operator class did not decide the outcome; a small number of properties of the operator did.
  - Rewrite: The first part has a positive answer: one setup served operators from unrelated literatures without change. For the second part, the outcome was decided by a small number of properties of the operator rather than by its class.
- `04-method.tex:816 (§4.3.7; GPTZero: AI)`
  - Original: The Runge--Kutta wrapper is not a backbone. It is placed around any backbone and changes only how the backbone's output is turned into the next state. It adds no parameters.
  - Rewrite: Unlike the operators above, the Runge--Kutta wrapper is placed around a backbone; it changes only how the backbone's output is turned into the next state and adds no parameters.
- `04-method.tex:205 (§4.3; GPTZero: AI)`
  - Original: This section describes every operator that occupies it. Each was chosen to isolate one property. A message-passing graph neural network, run on two different graphs, tests how far the spatial context of one step has to reach. A U-Net tests multiscale local detail. A Fourier Neural Operator tests global spectral support without a local path, and a hybrid adds a minimal local path to it. Two truncated graph networks test how much spatial context is needed at all.
  - Rewrite: Each operator was chosen to isolate one property. The message-passing graph network, run on two different graphs, tests how far the spatial context of one step has to reach, and two truncated versions of it show whether and how much spatial context is needed. The U-Net supplies multiscale local detail, the Fourier Neural Operator global spectral support without a local path, and the hybrid adds a minimal local path to it.
- `07-conclusion.tex:27 (Ch. 7; GPTZero: AI)`
  - Original: How time enters the update mattered less than that it enters: a higher-order Runge--Kutta step bought nothing over a single Euler step.
  - Rewrite: Once the interval reached the operator, the way it entered made no measurable difference: a higher-order Runge--Kutta step was no more accurate than a single Euler step.

### P5. Announce-then-enumerate ("The clinical implication is twofold.", "Two consequences follow.", "Two reasons support this design.", "Two tests ask this.", "Three ratios do not depend …")

*Frequency:* About 14 announcement sentences plus about 10 "First, … Second, …" sequences. Spread over Ch. 1, Ch. 3, Ch. 4, Ch. 5 and Appendix G.  
*Why it reads as generated:* Stating the number of points and then listing them is a default template of generated text. In a short paragraph it adds a sentence with no content and makes the prose read like slides.  
*Global fix:* Delete the announcement and start with the first item. Number items only when they are referred back to later (C1 and C2 in §5.5.1 are justified).

- `01-introduction.tex:58 (§1.1; GPTZero: AI)`
  - Original: The clinical implication is twofold. First, treatment timing now matters: an intervention that only slows progression is most valuable when administered before foveal involvement, because central vision is largely preserved until the atrophy reaches the fovea \citep{Boyer2017,Vallino2024}. Second, intravitreal injections carry both patient burden and procedural risk, so identifying which eyes will progress rapidly enough to justify therapy is the critical decision support task.
  - Rewrite: Treatment timing now matters: an intervention that only slows progression is most valuable when administered before foveal involvement, because central vision is largely preserved until the atrophy reaches the fovea \citep{Boyer2017,Vallino2024}. Intravitreal injections also carry patient burden and procedural risk, so the eyes that will progress fast enough to justify therapy have to be identified in advance.
- `03-data.tex:263 (§3.4; GPTZero: AI)`
  - Original: Two consequences follow. First, the normalised mask has a hard step at the lesion edge. Second, evaluation maps every threshold into normalised space rather than mapping the prediction back to the original scale, and this mapping must be applied consistently.
  - Rewrite: The normalised mask thus has a hard step at the lesion edge. Evaluation maps every threshold into normalised space instead of mapping the prediction back to the original scale, and the same mapping has to be used throughout.
- `04-method.tex:102 (§4.2; GPTZero: AI)`
  - Original: Two reasons support this design. First, the clinical sequences are short, with five to thirteen visits per eye (\S\ref{sec:data:dataset}). Using several past visits as input would leave fewer visits available as prediction targets. Second, the framework predicts strictly one step at a time.
  - Rewrite: The clinical sequences are short, with five to thirteen visits per eye (\S\ref{sec:data:dataset}), and using several past visits as input would leave fewer visits as prediction targets. The framework also predicts one step at a time.
- `05-experiments.tex:923 (§5.4.2; GPTZero: AI)`
  - Original: Two arguments speak against the penalty independently of its effect on the score.
  - Rewrite: (Delete. Begin the paragraph with "Under the pushforward curriculum (\S\ref{sec:method:training:curriculum}), the previous state on an unrolled step …" and introduce the second point with "The reference segmentations also shrink locally …".)

### P6. Consequence-connective chains ("therefore", "thus", ", so" in consecutive sentences)

*Frequency:* 71 "therefore", 7 "thus" and about 108 ", so" clauses: one causal connective per roughly 220 words. Ch. 5 alone has 24 "therefore" and 37 ", so"; Ch. 4 has 16 "therefore" and 30 ", so".  
*Why it reads as generated:* When every sentence is presented as a deduction from the one before, the prose takes on an evenly logical, lecturing cadence. Human technical writing leaves obvious inferences implicit. Flagged sentences use "therefore" or "thus" three times as often as human-judged ones (4.8 % against 1.6 %).  
*Global fix:* Keep a connective only where the inference is not obvious from the order of the sentences, and use at most one per paragraph. Otherwise delete it, or fold the reason into a "because" clause.

- `04-method.tex:21 (§4.1; GPTZero: AI)`
  - Original: A single pipeline is therefore fixed, and it provides one swappable slot for the update operator $f_\theta$.
  - Rewrite: A single pipeline is used instead, with one swappable slot for the update operator $f_\theta$.
- `05-experiments.tex:597 (§5.3.2; GPTZero: AI)`
  - Original: The deficit of the graph network was therefore located in its graph --- in where its neighbours lie physically --- and not in its operator class.
  - Rewrite: The earlier deficit of the graph network lay in the physical placement of its neighbours, not in its operator class.
- `05-experiments.tex:648 (§5.3.3; GPTZero: AI)`
  - Original: What holds at both seeds is therefore that global spectral support alone does not reach the U-Net at the one-year anchor.
  - Rewrite: At both seeds, global spectral support alone does not reach the U-Net at the one-year anchor.
- `03-data.tex:196 (§3.3; GPTZero: AI)`
  - Original: The grid is therefore strongly anisotropic: moving by one row covers about the same physical distance as moving by 21 columns.
  - Rewrite: The grid is strongly anisotropic: one row step covers about the same physical distance as 21 column steps.

### P7. Em-dash asides (--- … ---) inserting definitions, lists or the key claim mid-sentence

*Frequency:* 63 em-dashes, about 33 asides: Ch. 2 22, Ch. 4 14, Ch. 6 8, Ch. 1 7, Ch. 5 6, Ch. 7 4, appendices 2, Ch. 3 none. Ch. 7 has the highest density (5.3 per 1000 words).  
*Why it reads as generated:* Paired dashes that insert a definition, a list or a punchline into a sentence are one of the most recognisable generated punctuation habits. In Ch. 5–7 they wrap the central claims ("--- two independent routes to the same deficit ---", "--- above all, … ---"), which makes those claims sound staged.  
*Global fix:* Use parentheses for definitions and short lists, commas for brief appositions, and a separate sentence when the aside carries a claim. Aim for at most one dash pair per page and none in Ch. 6–7.

- `01-introduction.tex:164 (§1.3; GPTZero: AI)`
  - Original: This thesis therefore separates the two. The setup --- how elapsed time enters the prediction, how models are trained and how they are evaluated --- is fixed once, and the operator is the only part that changes.
  - Rewrite: This thesis therefore separates the two. The setup is fixed once: how elapsed time enters the prediction, how models are trained and how they are evaluated. Only the operator changes.
- `02-background.tex:184 (§2.1.2; GPTZero: AI)`
  - Original: Geographic atrophy is the disease in which a stack of three tightly coupled \emph{outer}-retinal layers --- the retinal pigment epithelium (RPE), the photoreceptor outer segments that sit just above the RPE, and the choriocapillaris (a dense capillary bed) immediately below the RPE --- die together in a localised patch of the macula \citep{Boopathiraj2024,Boyer2017}.
  - Rewrite: In geographic atrophy, three tightly coupled \emph{outer}-retinal layers die together in a localised patch of the macula \citep{Boopathiraj2024,Boyer2017}: the retinal pigment epithelium (RPE), the photoreceptor outer segments just above it, and the choriocapillaris, a dense capillary bed immediately below it.
- `05-experiments.tex:771 (§5.3.5; GPTZero: AI)`
  - Original: The central architectural result of the survey is this coincidence --- two independent routes to the same deficit --- rather than the score of any single arm. It is suggestive rather than a proof of mechanism.
  - Rewrite: The central architectural result of the survey is that two independent routes correct the same deficit, not the score of any single arm. The coincidence suggests a common mechanism but does not prove one.
- `07-conclusion.tex:90 (Ch. 7, Take-away; GPTZero: AI)`
  - Original: For forecasts from longitudinal medical imaging in a low-data clinical setting, what matters is the framework around the model and the properties of the operator placed in it --- above all, whether one update can see as far as the disease moves between two visits --- rather than the choice of operator family.
  - Rewrite: For forecasts from longitudinal medical imaging in a low-data clinical setting, the outcome depends on the framework around the model and on the properties of the operator placed in it, not on the choice of operator family. The property that matters most is whether one update can see as far as the disease moves between two visits.

### P8. Semicolon and colon hinges (two-part sentences shaped "claim; elaboration" or "claim: reveal")

*Frequency:* 191 semicolons and about 190 colons in running prose, one of each per roughly 210 words. Densest in Ch. 4 (8.2 semicolons per 1000 words) and Ch. 5 (6.7 colons per 1000 words). Flagged sentences contain a semicolon 1.5 times and a colon 1.4 times as often as human-judged ones.  
*Why it reads as generated:* Every sentence becomes a balanced two-part unit. Repeated across a page, this produces the even, symmetrical cadence that readers and detectors associate with generated text, and it makes sentences long: 18.5 % of flagged sentences have 30 words or more, against 9.5 % of human-judged ones.  
*Global fix:* Use a full stop when the second clause makes a new claim and "because" when it gives a reason. Keep colons for lists, definitions and labels such as C1 and C2, and keep semicolons for lists whose items contain commas.

- `02-background.tex:91 (§2.1.1; GPTZero: AI)`
  - Original: The macula has a diameter of roughly five to six millimetres and is the only part of the retina that GA ever affects clinically; for that reason, the OCT scanning window used throughout the thesis is centred on the macula and covers a $6 \times 6$\,mm field (\S\ref{sec:background:ga-oct:muw}).
  - Rewrite: The macula has a diameter of roughly five to six millimetres and is the only part of the retina that GA affects clinically. The OCT scanning window used throughout the thesis is therefore centred on the macula and covers a $6 \times 6$\,mm field (\S\ref{sec:background:ga-oct:muw}).
- `05-experiments.tex:767 (§5.3.5; GPTZero: AI)`
  - Original: Each is established against its own control, and the two end up within about 0.017 of each other, at the noise level; they are the two highest arms of Table~\ref{tab:experiments:arms} (\S\ref{sec:experiments:main-results}).
  - Rewrite: Each is established against its own control. The two end up within about 0.017 of each other, at the noise level, and are the two highest arms of Table~\ref{tab:experiments:arms} (\S\ref{sec:experiments:main-results}).
- `06-discussion.tex:41 (§6.1; GPTZero: AI)`
  - Original: Without the weighting of the mask channel, the canonical operator learned no change at all: with plain MSE every eye stayed at its baseline.
  - Rewrite: With plain MSE and no weighting of the mask channel, the canonical operator learned no change, and every eye stayed at its baseline.

### P9. Stock intensifiers and generic survey register

*Frequency:* About 30 (not counting the technical "exactly"): fundamentally ×5, naturally ×3, essentially ×3, precisely ×3, entirely ×3, inherently, reliably, crucially, plainly, materially, inevitably, critical ×2, "holds significant promise", "the principal cost", "the central training difficulty", "necessitates", "dictates". About 20 in Ch. 2 (§2.1, §2.3, related work) and 6 in Appendix G.1.  
*Why it reads as generated:* Emphatic adverbs that add no information are the closest thing to classic AI vocabulary in the thesis. §2.3 and G.1 also use generic survey phrasing ("broadly separate into two paradigms", "Note that", "Furthermore … Finally …", "sits at the intersection of") that marks text as summarised rather than written from the material. The author's own rules already ban several of these words.  
*Global fix:* Delete the adverb. Where emphasis matters, give the reason or the number instead. Replace survey stock phrases with a specific statement. Revise §2.3 and G.1 as units, because they carry most of these.

- `02-background.tex:885 (§2.3; GPTZero: AI)`
  - Original: It must be stated plainly that this reading is only legitimate if the trained model is nearly invariant to the solver used at inference.
  - Rewrite: This reading holds only if the trained model is nearly invariant to the solver used at inference.
- `02-background.tex:806 (§2.3; GPTZero: AI)`
  - Original: Note that when the step size $\Delta t$ is fixed by the dataset, the explicit dependence on it is usually suppressed in the notation. This thesis cannot suppress it because clinical observation intervals are fundamentally irregular.
  - Rewrite: When the step size $\Delta t$ is fixed by the dataset, the dependence on it is usually dropped from the notation. Here it has to be kept, because the intervals between clinical visits are irregular.
- `91-appendix.tex:475 (App. G.1; GPTZero: AI)`
  - Original: The convexity term is critical; a non-convex potential inevitably yields a tangled and useless mesh, regardless of how small the equation residual becomes.
  - Rewrite: The convexity term is needed because a non-convex potential yields a tangled mesh, however small the equation residual becomes.
- `02-background.tex:937 (§2.4; GPTZero: AI)`
  - Original: Consequently, this thesis sits at the intersection of applied medical-imaging deep learning and PDE-solver inductive biases.
  - Rewrite: The thesis thus applies inductive biases from PDE solvers to a medical-imaging forecasting task.

### P10. Idioms, metaphors and abstractions treated as agents (buys, bought, earns, lever, pays off, luckiest, blind to, fingerprint; "Two tests ask this", "Two arguments speak against", "the objective decides")

*Frequency:* About 17 idioms (buys/bought ×4, earn ×3, lever ×2, pays/paid off ×2, Take-away, luckiest, blind to, fingerprint, hostile, wasteful) and about 24 abstractions that act (decide/decides/decided ×12; asks/ask this/speak against/says nothing/tells ×12). Mostly in Ch. 5–7.  
*Why it reads as generated:* Conversational metaphors and abstractions that ask, speak or decide give the prose a lively, essay-like voice that is out of register in a results chapter and goes against the author's no-informal-language rule. Several of these sentences were judged human (for example 05:485 and 05:580), so this is a tone problem rather than a detector problem.  
*Global fix:* Use literal verbs: raises, lowers, accounts for, measures, determines, is tested. Give agency only to people, models and procedures.

- `05-experiments.tex:485 (§5.3.1; GPTZero: HUMAN)`
  - Original: A single ring of neighbours therefore buys almost everything the graph network on this graph achieves, and the second ring adds little or nothing.
  - Rewrite: A single ring of neighbours therefore accounts for almost all of what the graph network achieves on this graph; the second ring adds little or nothing.
- `06-discussion.tex:94 (§6.1; GPTZero: AI)`
  - Original: Capacity was not a lever in any of the four classes tested (\S\ref{sec:experiments:ablations:capacity}): no width step raised a class above the noise level, and the smaller versions lost little.
  - Rewrite: Operator size made no measurable difference in any of the four classes tested (\S\ref{sec:experiments:ablations:capacity}): no width step raised a class above the noise level, and the smaller versions lost little.
- `05-experiments.tex:159 (§5.1.3; GPTZero: AI)`
  - Original: so the highest epoch is mostly the luckiest one.
  - Rewrite: so the highest epoch mostly reflects this noise.
- `05-experiments.tex:1655 (§5.7; GPTZero: AI)`
  - Original: Set against the results of this chapter, most of the extra cost bought nothing measurable.
  - Rewrite: Compared with the results of this chapter, most of the extra cost brought no measurable gain in accuracy.

### P11. Signposting and roadmap paragraphs ("This section provides …", "§x describes …, §y states …", "The remainder of this thesis is organised as follows.")

*Frequency:* About 30: 12 openers of the form "This section/chapter/subsection/appendix …", about 14 roadmap sentences listing sections by number (6 in Ch. 2, 7 in Ch. 4, 1 in App. G), and "The remainder of this thesis is organised as follows."  
*Why it reads as generated:* Sentences that announce what the next text will do are a strong template signal, especially in chains of "§x describes …". They slow down a reader who already has the headings and the table of contents.  
*Global fix:* Keep at most one orienting sentence per chapter. Open each section with content, and let the headings carry the order.

- `02-background.tex:11 (§2.1; GPTZero: AI)`
  - Original: This section provides the imaging-side background needed to motivate the state representation used throughout the remainder of the thesis. The clinical framing established in Chapter~\ref{ch:introduction} is taken as read; the focus here is on \emph{which part of the eye} GA affects, on \emph{how} that part is imaged, on \emph{what is visible} in an OCT volume of a GA eye, and on \emph{which derived quantities} feed into the eleven-channel state tensor introduced in~\S\ref{sec:data:state}.
  - Rewrite: (Replace lines 11–24 with:) This section explains, for readers without clinical training, which part of the eye GA affects, how it is imaged, and which derived maps form the eleven-channel state of~\S\ref{sec:data:state}.
- `01-introduction.tex:214 (§1.4; GPTZero: AI)`
  - Original: The remainder of this thesis is organised as follows. Chapter~\ref{ch:background} introduces GA and OCT imaging, the numerical ideas that learned PDE solvers build on, and the families of learned models considered in this work.
  - Rewrite: Chapter~\ref{ch:background} introduces GA and OCT imaging, the numerical ideas that learned PDE solvers build on, and the families of learned models considered in this work.
- `04-method.tex:218 (§4.3; GPTZero: AI)`
  - Original: \S\ref{sec:method:family:contract} states the interface every operator satisfies. \S\ref{sec:method:mppde} describes the message-passing network and \S\ref{sec:method:graph} the two graphs it runs on.
  - Rewrite: (Delete this roadmap through the end of the paragraph; subsections 4.3.1–4.3.8 already show the order.)

### P12. Slogan-style run-in headings

*Frequency:* About 10 of the 51 \paragraph heads, nearly all in Ch. 5–7: "The operator: ingredients, not classes.", "Good at where, weaker at how fast.", "Where modelling effort pays.", "Take-away.", "What follows.", "What this means."  
*Why it reads as generated:* Catchy two-beat labels are slide and blog conventions. Placed above verdict paragraphs, they make Ch. 6–7 read as a pitch, and some of them repeat the contrast-frame tell inside the heading itself.  
*Global fix:* Use descriptive topic labels that name what the paragraph covers.

- `06-discussion.tex:51 (§6.1)`
  - Original: \paragraph{The operator: ingredients, not classes.}
  - Rewrite: \paragraph{The operator.}
- `06-discussion.tex:140 (§6.1; GPTZero: AI)`
  - Original: \paragraph{Where modelling effort pays.}
  - Rewrite: \paragraph{Implications for model design.}
- `06-discussion.tex:157 (§6.2; GPTZero: HUMAN)`
  - Original: \paragraph{Good at where, weaker at how fast.}
  - Rewrite: \paragraph{Location and speed of growth.}
- `07-conclusion.tex:89 (Ch. 7)`
  - Original: \paragraph{Take-away.}
  - Rewrite: \paragraph{Summary.} (or merge the sentence into the preceding paragraph)

### P13. Over-explaining glosses and conversational register (mainly §2.1)

*Frequency:* About 10: "In other words", "Put differently", "Concretely" ×2, "essentially" used as a gloss ×2, "takes some getting used to", "a small piece of optical engineering", "can be thought of as a biological camera", and several "i.e." asides.  
*Why it reads as generated:* Restating the same fact a second time in a simpler voice is a tutoring habit, and the author's rules exclude informal analogies. Two of these (the camera analogy and "Put differently") were judged human, so the case is tone rather than the detector.  
*Global fix:* Define each term once and precisely, and cut the restatement. Drop analogies.

- `02-background.tex:122 (§2.1.1; GPTZero: AI)`
  - Original: The terminology in this list takes some getting used to, but for the purposes of this thesis it is sufficient to remember the structural fact that the retina is layered, that GA destroys a specific \emph{outer}-retinal stack of three of those layers (\S\ref{sec:background:ga-oct:disease}), and that the surrounding layer geometry --- ten boundary depth maps in total --- is what feeds the model alongside the lesion mask (\S\ref{sec:background:ga-oct:state-rep}).
  - Rewrite: Three facts suffice for this thesis: the retina is layered, GA destroys a specific \emph{outer}-retinal stack of three of those layers (\S\ref{sec:background:ga-oct:disease}), and the surrounding layer geometry, ten boundary depth maps in total, is given to the model alongside the lesion mask (\S\ref{sec:background:ga-oct:state-rep}).
- `02-background.tex:191 (§2.1.2; GPTZero: AI)`
  - Original: In other words, atrophy of one layer entrains the degeneration of the others, so the resulting lesion appears on imaging as a sharply delineated patch in which the entire outer-retinal complex is missing rather than as the loss of a single isolated layer.
  - Rewrite: Atrophy of one layer therefore entrains the degeneration of the others, and the lesion appears on imaging as a sharply delineated patch in which the whole outer-retinal complex is missing.
- `02-background.tex:74 (§2.1.1; GPTZero: HUMAN)`
  - Original: The eye, sketched in Figure~\ref{fig:bg:eye-anatomy} (left), can be thought of as a biological camera.
  - Rewrite: Figure~\ref{fig:bg:eye-anatomy} (left) sketches the eye.
- `02-background.tex:313 (§2.1.3; GPTZero: HUMAN)`
  - Original: Resolving the depth dimension requires a small piece of optical engineering, because near-infrared light from a single short pulse cannot be timed precisely enough on a per-layer basis with conventional electronics.
  - Rewrite: Depth cannot be resolved by timing the returning light directly, because the delays between retinal layers are too short for conventional electronics.

### P14. Templated statistical sentences in Ch. 5 ("X against Y gives Δ = … SE (k/5) and per eye … (m/75, t = …)")

*Frequency:* About 40 such sentences, often three or four in a row, in §5.2 and §5.3.  
*Why it reads as generated:* Filling the same syntactic slots with numbers sentence after sentence is what generated reports look like, and the verdict ends up at the tail of the sentence. This is a readability point only: the numbers stay as they are, and NOTES.md (#23) already plans a reporting-scheme pass that moves most of them to Appendix E.  
*Global fix:* State the comparison and its outcome in words first, then give the numbers once in one compact parenthesis. Put both seeds in one sentence instead of two parallel clauses.

- `05-experiments.tex:375 (§5.2; GPTZero: AI)`
  - Original: The T-FEN against the U-Net gives $\Delta = +0.0383 \pm 0.0134$~SE (5/5) and per eye $+0.0383 \pm 0.0075$ (51/75, $t = 5.1$) at seed 42, and $+0.0246 \pm 0.0073$~SE (5/5) and per eye $+0.0255 \pm 0.0074$ (52/75, $t = 3.4$) at seed 7. The lead is smaller at the second seed but present on every fold at both, so the T-FEN lies above the U-Net.
  - Rewrite: The T-FEN lies above the U-Net on every fold at both seeds, with a smaller lead at the second: $\Delta = +0.0383 \pm 0.0134$~SE (5/5; per eye $+0.0383 \pm 0.0075$, 51/75, $t = 5.1$) at seed 42 and $+0.0246 \pm 0.0073$~SE (5/5; per eye $+0.0255 \pm 0.0074$, 52/75, $t = 3.4$) at seed 7.

## Rules of thumb for revising the rest of the text

1. Use at most one "therefore", "thus" or ", so" per paragraph. If the inference is obvious from the order of the sentences, delete the connective; if the reason matters, make it a "because" clause.
2. End a paragraph on its last piece of evidence (a number, a table, a source) or on a pointer forward, not on a sentence that restates it. Keep one verdict per subsection, at its end.
3. State the positive claim. Use "not X but Y", "X, not Y" or "rather than" only when the excluded alternative was tested or is a likely misreading. Then name the alternative first and end on the claim, never on the negation.
4. Avoid clefts. Write "The framework requires …" instead of "What the framework needs is …", and replace a bare "This is what/why …" with the noun that "This" stands for.
5. Replace em-dash asides with parentheses (definitions, lists), commas (short appositions) or a new sentence (claims). Allow at most one dash pair per page and none in Ch. 6–7.
6. Delete announcement sentences ("Two consequences follow.", "The clinical implication is twofold.") and start with the first item. Number items only when they are referred back to later.
7. Split any sentence over about 30 words at its semicolon or colon when the second clause makes a new claim. Keep semicolons for lists whose items contain commas and colons for lists, definitions and labels.
8. Vary the shape of consecutive sentences, not only their length. Do not write three sentences in a row with the same subject–verb–object frame ("A U-Net tests … An FNO tests …"); fold minor items into a clause.
9. Lead with a concrete subject that can be checked: a table, a fold, a run, a source, a date ("On fold 4, …", "Until 6 August 2026, …", "Table 5.3 shows …"). The sentences GPTZero judged human almost always do this.
10. Use literal verbs. Write raises, lowers, accounts for, measures, determines or is tested, not buys, earns, lever, pays off, asks, speaks against or decides. Only people, models and procedures act.
11. Delete intensifiers (fundamentally, naturally, inherently, essentially, precisely, entirely, crucially, plainly, materially, reliably, critical, "at all" used for emphasis). If emphasis is needed, give the number or the reason instead.
12. Define a term once, precisely, and do not restate it in a second voice ("In other words", "Put differently", "Concretely"). Drop analogies ("biological camera", "a small piece of optical engineering").
13. Use one orienting sentence per chapter at most. Cut chains of "§x describes …" where the headings already show the order, and open each section with content.
14. Label run-in headings with their topic ("Growth speed", "Model design"), not with a slogan ("Take-away", "Where modelling effort pays", "ingredients, not classes").
15. In results paragraphs, give the outcome in words first, then the statistics once in a compact parenthesis. Do not repeat the "X against Y gives Δ = … and per eye …" template in consecutive sentences.
16. Judge the revision by clarity, not by GPTZero. It flags 82 % of the plain, procedural Ch. 3 and labels the same device differently in different places. Rerunning it after each edit is not a useful test, because precise technical prose with fixed terms and numbers is predictable by nature.

