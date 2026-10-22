# Tablet review v7 + v8 (2026-10-22)

Decoded from `main-thesis_v7_261019_191032.sdocx` (marks on the thesis build of 2026-10-15, Ch. 1-3) and `main-thesis_v8_261022_121822.sdocx` (build of 2026-10-19, Ch. 2 to App. G). Colour: **B** = blue (rewrite / question), **R** = red (wrong / remove). *Page* is the page of the reviewed build; *Now* is the place in the current `.tex` sources. The numbers match the labels in the margin of `tablet-review-v7-v8-2026-10-22-overlay.pdf` (same folder, not committed).

151 marks: 24 in v7, 127 in v8; 128 blue, 23 red. Handwriting decoded by eye; uncertain readings are marked (?).


## Front matter

| # | Page | Col | Marked | Note | Now | Status |
|---|---|---|---|---|---|---|
| 1 | v7 p.ix | B | highlight: “DMM, IoU, ItpNet, MM-PDE (acronym list); SWE struck …” | might need rework | `acronyms.tex:10-24` | done 2026-10-22: SWE, CNN, IoU removed; FAF, FEN, ODE, RK4, RPE, SLO, T-FEN added (author: not AUC, SE, WENO, CFL) |

## Chapter 1 Introduction

| # | Page | Col | Marked | Note | Now | Status |
|---|---|---|---|---|---|---|
| 2 | v7 p.2 | R | struck: “The clinical implication is twofold” | filler word? ("is" struck) | `01-introduction.tex:63` | done 2026-10-22: "Hence, two things matter for clinical practice." |
| 3 | v7 p.2 | B | highlight: “Optical coherence tomography (OCT) produces three-dimensional images of the retina …” | this part feels very off and thrown in here; needs a smoother transition (whole paragraph up to "This thesis pursues that avenue.") | `01-introduction.tex:70` | done 2026-10-22: own paragraph with a bridge |
| 4 | v7 p.2 | B | highlight: “The output here is a complete map” | "here" -> of this approach / thesis? | `01-introduction.tex:97` | done 2026-10-22 |
| 5 | v7 p.2 | B | highlight: “can serve as this model” | "can serve as this" struck, "model" -> operator? | `01-introduction.tex:104` | done 2026-10-22 (with #7) |
| 6 | v7 p.2 | B | highlight: “operator / model / models / operator (Aim of the Thesis) …” | again? model class? type? | `01-introduction.tex:102-114` | done 2026-10-22 (with #7) |
| 7 | v7 p.2 | R | note: Aim of the Thesis, bottom of page | I think this section needs to rethink operator and model | `01-introduction.tex:102-114` | done 2026-10-22: operator / architecture / framework used consistently in Ch. 1 (Aim, RQ follow-up, contributions, outline) |
| 8 | v7 p.3 | B | highlight: “Chapter 2 introduces” | way too long, needs to be split up (outline sentence up to "formal statement of the problem") | `01-introduction.tex:176` | done 2026-10-22: split into two sentences |
| 9 | v7 p.3 | B | note: Appendix G reports | appendices hold a bunch of other stuff too | `01-introduction.tex:188` | done 2026-10-22: appendices named, App. G last |

## Chapter 2 Background

| # | Page | Col | Marked | Note | Now | Status |
|---|---|---|---|---|---|---|
| 10 | v7 p.4 | B | note: a thin neural-tissue lining | new sentence (split at the dash after "retina") | `02-background.tex:67` | done 2026-10-22 |
| 11 | v7 p.4 | B | highlight: “GA / OCT in the macula paragraph of 2.1.1 …” | not discussed yet | `02-background.tex:86` | done 2026-10-22: pointers to 2.1.3 / 2.1.2 |
| 12 | v7 p.7 | B | highlight: “FAF has become the gold standard for detecting and measuring GA area …” | don't these two conflict? (with "OCT is preferred over fundus autofluorescence (FAF)") | `02-background.tex:209` | done 2026-10-22: "Although FAF is the standard ..., Vallino give three reasons to prefer OCT" |
| 13 | v7 p.7 | B | highlight: “The present work” | -> this thesis | `02-background.tex:264` | done 2026-10-22 |
| 14 | v7 p.11 | B | note: Global methods | maybe a formula of derivatives in Fourier space | `02-background.tex:485` | done 2026-10-22: equation added |
| 15 | v7 p.13 | B | highlight: “does not require f to be written down” | "down. B" -> fuse; "data, t" -> new sentence | `02-background.tex:647` | done 2026-10-22 |
| 16 | v7 p.15 | B | note: 2.4 Related Work heading | section needs review | `02-background.tex:753` | TODO added at the top of 2.4 (author review) |
| 17 | v7 p.15 | B | highlight: “fall into four groups:” | don't really like the colon here | `02-background.tex:764` | done 2026-10-22: no colon, one subsection per group |
| 18 | v7 p.15 | B | highlight: “The original papers of the architectures used as the operator are cited where each is introduced …” | is this needed here? | `02-background.tex:768` | done 2026-10-22: deleted |
| 19 | v7 p.16 | B | bracket: On a finer scale | this paragraph seems kind of random (paragraph incl. "Most of the clinical literature ...") | `02-background.tex:828` | done 2026-10-22: Lindner opens 2.4.2 as motivation; cohort-level sentence closes 2.4.1 |
| 20 | v7 p.19 | B | highlight: “2.5.2 Problem Statement (heading)” | needs review | `02-background.tex:1010` | TODO added at the top of 2.5.2 (author review) |
| 21 | v7 p.19 | B | highlight: “t_0 < t_1 < ... < t_K” | same line | `02-background.tex:1018` | done 2026-10-22: \mbox |

## Chapter 3 Data

| # | Page | Col | Marked | Note | Now | Status |
|---|---|---|---|---|---|---|
| 22 | v7 p.24 | B | highlight: “The training loss can optionally exclude the pad positions …” | tested but didn't make a difference | `03-data.tex:289 (comment)` | already done: sentence commented out 2026-10-18 (pad exclusion not reported) |
| 23 | v7 p.26 | B | highlight: Table 3.1 (caption) | why not put in place? | `03-data.tex:403` | done 2026-10-22: [h] (Table 3.1 now on its page; Table 3.2 one page later, no room) |
| 24 | v7 p.27 | B | highlight: Table 3.2 (caption) | why not put in place? | `03-data.tex:473` | done 2026-10-22 (with #23) |

## Chapter 2 Background

| # | Page | Col | Marked | Note | Now | Status |
|---|---|---|---|---|---|---|
| 25 | v8 p.6 | B | struck: “Both drawings were generated with an image-generation model …” | this necessary? (Fig. 2.1 caption; same sentence highlighted in Figs. 2.2 and 2.4) | `02-background.tex:57; 02-background.tex:312` | done 2026-10-22: Figs 2.1, 2.2, 2.4: "Drawings generated with ChatGPT; labels added and verified by the author." |
| 26 | v8 p.8 | B | highlight: B-scans (label in Fig. 2.2b) | this was specifically made bigger(?); line should come at an angle | `02-background.tex:160` | done 2026-10-22: leader line angled down-right, to the highlighted (thick) B-scan |
| 27 | v8 p.15 | B | note: Fig. 2.5 placeholder | TODO next | `02-background.tex:585` | done (drawn 2026-10-20); author ok |

## Chapter 3 Data

| # | Page | Col | Marked | Note | Now | Status |
|---|---|---|---|---|---|---|
| 28 | v8 p.25 | B | note: Fig. 3.1 placeholder | TODO next | `03-data.tex:161` | done (drawn 2026-10-20); author ok |

## Chapter 4 Method

| # | Page | Col | Marked | Note | Now | Status |
|---|---|---|---|---|---|---|
| 29 | v8 p.30 | B | highlight: “the layout of the state, the conditioning inputs, the objective …” | kind of feels repetitive | `04-method.tex:68` | done 2026-10-22: list removed from the 4.1 roadmap |
| 30 | v8 p.31 | B | highlight: “This section defines what every arm shares …” | here again, 3rd time | `04-method.tex:112` | done 2026-10-22: 4.2 opener kept as the section map |
| 31 | v8 p.31 | R | highlight: “and Table 4.1 lists the training settings …” | kind of random | `04-method.tex:119` | done 2026-10-22: Table 4.1 pointer moved to the start of 4.2.6 |
| 32 | v8 p.31 | B | highlight: “therefore has no memory of the trajectory so far …” | what does this do here? | `04-method.tex:124` | done 2026-10-22: merged with #33 |
| 33 | v8 p.31 | B | bracket: This design follows from the length of the clinical sequences | this also kind of goes against what we argue in the discussion / future work | `04-method.tex:126` | done 2026-10-22: one paragraph, points to future work (6.4) |
| 34 | v8 p.32 | B | highlight: “The original neural PDE solvers” | ? | `04-method.tex:140` | done 2026-10-22 |
| 35 | v8 p.32 | B | note: The update of the problem statement | 2.5.2? | `04-method.tex:146` | done 2026-10-22 |
| 36 | v8 p.32 | B | highlight: “No monotonic-growth constraint is imposed nonetheless …” | write: a constraint to avoid shrinking is not imposed | `04-method.tex:191` | done 2026-10-22 |
| 37 | v8 p.32 | B | highlight: “and this form is the same for every operator in the slot …” | repeat | `04-method.tex:204` | done 2026-10-22: deleted |
| 38 | v8 p.34 | B | highlight: “because the reference segmentations themselves shrink locally between visits …” | we already know this | `04-method.tex:355` | done 2026-10-22: reason dropped, pointer to 4.2.1 |
| 39 | v8 p.35 | B | note: end of 4.2.5 (pushforward curriculum) | pushforward ablation? | `04-method.tex:376-425` | TODO in NOTES (author: probably not run) |
| 40 | v8 p.38 | B | highlight: “No running statistics are kept” | repeat? | `04-method.tex:653` | done 2026-10-22: paragraph shortened (with #41, #42) |
| 41 | v8 p.38 | R | highlight: “In earlier runs with batch normalisation, training and evaluation measurably behaved as two different operators …” | can't write like this | `04-method.tex:656` | done 2026-10-22: deleted |
| 42 | v8 p.38 | B | highlight: “A graph-level variant that normalises a whole batch as one graph was avoided as well …” | don't know if I want this | `04-method.tex:658` | done 2026-10-22: deleted |
| 43 | v8 p.41 | B | struck: “receive the sixteen input channels” | remove "the", and explain why 16 | `04-method.tex:845` | done 2026-10-22: the sixteen channels listed |
| 44 | v8 p.42 | B | highlight: “GELU activations between blocks” | why? | `04-method.tex:899` | checked 2026-10-22: fno.py uses F.gelu; text unchanged (author: fine) |
| 45 | v8 p.46 | B | highlight: “to about four times its size” | really? | `04-method.tex:1190` | done 2026-10-22: "from about a sixth to three to four times" |
| 46 | v8 p.46 | B | highlight: “A second free-form control at width 139” | maybe remove, pointless | `04-method.tex:1205` | done 2026-10-22: width-139 control removed everywhere (4.3.8, Table 4.3, 5.3.4, 6.1, Ch. 7, App. E, App. F); width-48 T-FEN + capacity study argue against parameter count |
| 47 | v8 p.47 | B | highlight: FEN, free-form only, width 139 (row of Table 4.3) | ? | `04-method.tex:1231` | done 2026-10-22 (with #46) |

## Chapter 5 Experiments

| # | Page | Col | Marked | Note | Now | Status |
|---|---|---|---|---|---|---|
| 48 | v8 p.48 | B | note: Chapter 5 title page | Dice scores over time: section | `05-experiments.tex:4` | done 2026-10-22: new section 5.3 "Forecasts Beyond One Year" with Table 5.3 (8 operators x 4 year bins); author TODO to review |
| 49 | v8 p.48 | B | highlight: “which statements about the operators are licensed …” | don't like "licensed" | `05-experiments.tex:25; 05-experiments.tex:1462` | done 2026-10-22: "supports" / "can be made" |
| 50 | v8 p.48 | B | highlight: “spread their raw mask predictions much further from the two mask values …” | what does this mean? | `05-experiments.tex:58` | done 2026-10-22: rewritten with the reasoning (Dice asks the side of the threshold, RMSE the distance; example +3) |
| 51 | v8 p.50 | B | highlight: “Single-epoch values are not reported” | reason for choosing mean over epochs | `05-experiments.tex:201` | done 2026-10-22: paragraph opens with the reason for a mean over epochs |
| 52 | v8 p.50 | B | highlight: “In addition, the operators learn at different speeds …” | reason for 10-29; so why "in addition"? | `05-experiments.tex:225` | done 2026-10-22: "The window starts at epoch 10 because ..." |
| 53 | v8 p.52 | B | highlight: “The eye counts use the growth-region Dice at the anchor, because …” | we don't have the change-region Dice? | `05-experiments.tex:299` | done 2026-10-22: "growth-region Dice ..., which is recorded per eye"; logging remark removed |
| 54 | v8 p.52 | B | highlight: “Two entries set the scale” | repetition | `05-experiments.tex:326` | done 2026-10-22: deleted |
| 55 | v8 p.52 | B | highlight: “the same as persistence” | repetition | `05-experiments.tex:432; 05-experiments.tex:550` | done 2026-10-22: deleted |
| 56 | v8 p.52 | B | highlight: “This lies just beyond the variation of retraining …” | doesn't this go against the rule we established? | `05-experiments.tex:452; 05-experiments.tex:458` | done 2026-10-22: names the failing criterion (per-eye t = 2.2 below the bar of App. E.3); 5.1.5 now states the per-eye bar |
| 57 | v8 p.53 | B | highlight: “the two are level for three years” | what kind of argument is this? | `05-experiments.tex:478` | done 2026-10-22: >3-year argument removed |
| 58 | v8 p.53 | B | bracket: Although the T-FEN scores highest at the anchor | I think this argument is not good (whole paragraph) | `05-experiments.tex:473` | done 2026-10-22: canonical paragraph rewritten (criterion named, 4x cost, reference configuration; pointer to 6.1.2) |
| 59 | v8 p.54 | R | highlight: “An eye on which the model does well” | absolutely not (Fig. 5.2 caption) | `05-experiments.tex:412; 05-experiments.tex:413` | done 2026-10-22: caption starts neutrally (author: no selection statement) |
| 60 | v8 p.54 | R | highlight: “The eye is the one with the highest change-region Dice …” | remove (rest of that sentence) | `05-experiments.tex:421` | done 2026-10-22: selection sentence removed (author) |
| 61 | v8 p.56 | B | note: Table 5.2 header | + add the score we are comparing with here | `05-experiments.tex:604` | done 2026-10-22: Mean column + default reference row in Table 5.2 |
| 62 | v8 p.56 | B | bracket: Reach along the rows therefore decides how well the graph network does | maybe also a table here | `05-experiments.tex:636` | done 2026-10-22: four-round and k = 20 rows added to Table 5.2; 5.3.2 points to it |
| 63 | v8 p.56 | B | note: end of 5.3.2 | multiple graphs stacked with multiple scales? | `05-experiments.tex:645` | done 2026-10-22: 6.4 paragraph "Several scales of reach" |
| 64 | v8 p.56 | B | highlight: “These values are descriptive and were not tested …” | ??? | `05-experiments.tex:679` | done 2026-10-22: all "not tested" phrasings in Ch. 5-6 rephrased (#108, #111 still to check) |
| 65 | v8 p.56 | B | note: end of 5.3.3 text | we should maybe dive further into the performance over long rollouts | `05-experiments.tex:689` | done 2026-10-22 (with #48) |
| 66 | v8 p.57 | B | note: Fig. 5.3 placeholder | TODO | `05-experiments.tex:618` | done (figure removed 2026-10-21); author ok |
| 67 | v8 p.58 | B | struck: “A second control widens the free-form network to a width of 139 …” | pointless: just adding width tells us nothing about network complexity / performance | `05-experiments.tex:727` | done 2026-10-22 (with #46) |
| 68 | v8 p.58 | B | bracket: This matched control does not train on fold 4 | I am not sure about this | `05-experiments.tex:729` | done 2026-10-22 (with #46): fold-4 story removed |
| 69 | v8 p.58 | B | highlight: “The extra width changes the free-form network little …” | ? (arrow to the "pointless" note) | `05-experiments.tex:742` | done 2026-10-22 (with #46) |
| 70 | v8 p.58 | B | note: The GA front advances about 10 to 25 columns | include µm | `05-experiments.tex:825` | done 2026-10-22: µm added |
| 71 | v8 p.59 | B | note: Fig. 5.4 placeholder | TODO | `05-experiments.tex:815` | figure restored since (2026-10-21) |
| 72 | v8 p.60 | B | note: Fig. 5.5 | maybe actually both seed visualisations here | `05-experiments.tex:904` | done 2026-10-22: Fig. 5.x two panels, seed 42 and seed 7 |
| 73 | v8 p.60 | B | highlight: “at both seeds and is exploratory” | ? | `05-experiments.tex:873` | done 2026-10-22: "is exploratory" removed |
| 74 | v8 p.60 | R | struck: “because the change-region Dice is recorded per fold only …” | remove | `05-experiments.tex:875` | done 2026-10-22: reason removed |
| 75 | v8 p.60 | B | highlight: “On the third of the eyes with the least distant atrophy it leads them …” | this sentence reads really bad | `05-experiments.tex:923` | done 2026-10-22: rewritten |
| 76 | v8 p.61 | B | highlight: “whether this difference causes the effect was not tested …” | don't like this (incl. the next sentence, "the mirror image of the graph networks") | `05-experiments.tex:958` | done 2026-10-22: mirror-image sentence removed, edge reason as "a possible reason" |
| 77 | v8 p.61 | B | highlight: “On fold 4 the graph networks predict too little …” | which one? | `05-experiments.tex:963` | done 2026-10-22: both graph networks named |
| 78 | v8 p.61 | B | note: each of them predicts less than half of the true new atrophy | is this maybe a data problem? | `05-experiments.tex:969` | done 2026-10-22: small lesions / imprecise outline + general under-prediction (6.2) |
| 79 | v8 p.62 | B | note: two eye properties consistently separate local from global operators | what is this supposed to mean?? | `05-experiments.tex:983` | done 2026-10-22: closing paragraph rewritten as a plain summary |
| 80 | v8 p.62 | B | struck: “These findings are exploratory” | struck | `05-experiments.tex:986` | done 2026-10-22: removed |
| 81 | v8 p.62 | B | note: end of 5.4 | I feel like the story this section tells needs to be more clear | `05-experiments.tex:991` | done 2026-10-22: opener asks the question, closing answers it |
| 82 | v8 p.62 | B | highlight: “the settings that every operator shares” | don't know if I want to put it like that; remove? | `05-experiments.tex:998` | done 2026-10-22 |
| 83 | v8 p.62 | B | highlight: “Its two values are a fixed distance apart in normalised units …” | explain this to me and code a toy example to understand it better (also HL "f cannot be read as a growth rate") | `05-experiments.tex:1032` | answered 2026-10-22 with a toy example (scratchpad toy_dt.py); text unchanged |
| 84 | v8 p.63 | B | note: Table 5.3 | this needs to go closer to where it's referenced, next page maybe | `05-experiments.tex:1109` | done 2026-10-22: [h] after the referencing paragraph |
| 85 | v8 p.63 | B | note: is tested in §5.6.1. (end of RK4 paragraph) | but RK4 makes it a growth rate? | `05-experiments.tex:1044-1059` | answered 2026-10-22: the RK4 network defines a vector field, a rate of change of the normalised state, not an area growth rate |
| 86 | v8 p.65 | B | highlight: “At width 192, the T-FEN diverges during training …” | same as before | `05-experiments.tex:1353` | done 2026-10-22: stated once (closing paragraph) |
| 87 | v8 p.65 | B | note: Four message-passing rounds instead of two | dilated GNN gets smaller Dice, no? | `05-experiments.tex:1358; 06-discussion.tex:113` | answered: yes, lower on every fold, within noise |
| 88 | v8 p.66 | B | highlight: Stencil GNN (Table 5.4) | has this naming ever been used? should be "dilated", no? | `05-experiments.tex:1303` | done 2026-10-22: "Dilated-stencil GNN" (App. E: "Dilated stencil") |
| 89 | v8 p.68 | B | note: The step is fixed in time: h = 1, 1/2 | line break | `05-experiments.tex:1512` | done 2026-10-22 |
| 90 | v8 p.68 | B | highlight: “each on folds 0 to 2 with one seed” | why not 3 and 4 as well? (also HL "three" in "fails C2 on all three folds") | `05-experiments.tex:1519` | running 2026-10-22: ladder on folds 3 and 4 locally (precomputes exist) |
| 91 | v8 p.68 | B | note: steps of 45 days or less are shorter than any interval between two visits | also meaning the network has never seen anything like that during training, which could explain this | `05-experiments.tex:1542` | done 2026-10-22 (valid: every training interval is a multiple of 90 days) |
| 92 | v8 p.68 | B | highlight: “value lies about 0.018 above the value of the trained setting …” | which setting? is this within noise? | `05-experiments.tex:1551` | done 2026-10-22 |
| 93 | v8 p.69 | B | struck: “defines a vector field as well, but its training step resolves it …” | why though? | `05-experiments.tex:1603` | done 2026-10-22 |
| 94 | v8 p.70 | R | struck: “later than the one-year anchor and later than the 360 days that training unrolls …” | remove (also "only") | `05-experiments.tex:1722` | done 2026-10-22 |
| 95 | v8 p.71 | B | highlight: “The growth-region Dice beyond three years rises from 0.537 to 0.611 …” | worse than stencil GNN, right? | `05-experiments.tex:1761` | done 2026-10-22: still below the stencil (0.655) |
| 96 | v8 p.71 | B | note: end of 5.6.2 | so I don't really read from this that the T-FEN is unstable? particularly not the energy-conserving form | `05-experiments.tex:1779` | done 2026-10-22: closing sentence (only Galerkin unstable); 6.4 transport paragraph reworded |
| 97 | v8 p.72 | B | note: Fig. 5.10 placeholder | can this be placed close to the reference? | `05-experiments.tex:1839` | done 2026-10-22: figure moved after its reference, [h] |
| 98 | v8 p.72 | B | highlight: “report the growth-region Dice by time since baseline: the Dice of the newly atrophic region …” | this I know, it was literally 2 sentences ago | `05-experiments.tex:1885` | done 2026-10-22 |
| 99 | v8 p.72 | B | note: Salvi et al. (2025) report a Dice of 0.70 | maybe every comparison should get a separate paragraph | `05-experiments.tex:1896` | done 2026-10-22: one paragraph each for Mai, Gigon, Salvi |
| 100 | v8 p.72 | B | highlight: “the Dice of a growth region rises with its size …” | as we measured before; not sure if this is true in general | `05-experiments.tex:1902` | done 2026-10-22: tied to the cohort measurement (5.5) |
| 101 | v8 p.74 | B | highlight: “The baseline lesion size alone is not correlated with the growth rate …” | doesn't this contradict something? | `05-experiments.tex:2002` | done 2026-10-22: "as intended by the square-root transform" |
| 102 | v8 p.74 | B | note: lies below all three models on growth speed | partly caused by the setup, no? | `05-experiments.tex:2042` | done 2026-10-22 |
| 103 | v8 p.75 | R | note: wrapper at 439 s (Table 5.1) | maybe another table here? | `05-experiments.tex:2089` | done 2026-10-22: new Table (cost per arm, ratio to the stencil) |
| 104 | v8 p.75 | R | highlight: “and the dual-branch moving-mesh extension about …” | remove | `05-experiments.tex:2099` | done 2026-10-22: removed |
| 105 | v8 p.75 | R | struck: “and the dual branch is a null (Appendix G) …” | remove | `05-experiments.tex:2106` | done 2026-10-22: removed |

## Chapter 6 Discussion

| # | Page | Col | Marked | Note | Now | Status |
|---|---|---|---|---|---|---|
| 106 | v8 p.77 | B | note: Chapter 6 heading | do we put an introduction right below the chapter heading or not? sometimes we do, sometimes we don't | `06-discussion.tex:4` | no change (author 2026-10-22: leave as is) |
| 107 | v8 p.77 | B | note: It predicts the next visit from the current one by a residual update | new line | `06-discussion.tex:37` | done 2026-10-22: displayed equation |
| 108 | v8 p.79 | B | highlight: “but they suggest that global context matters more for long forecasts …” | why always "were not tested"? just write it like it could be | `06-discussion.tex:128` | done 2026-10-22 |
| 109 | v8 p.79 | B | note: a vector of equation features | MP-PDE describes this as one of the most important factors; can we make this a general statement? | `06-discussion.tex:145` | done 2026-10-22: new 6.1.4 opener (MP-PDE ablation) |
| 110 | v8 p.79 | B | struck: “the wrapper network would need a finer training step …” | was this maybe done? | `06-discussion.tex:184` | ignored (author 2026-10-22) |
| 111 | v8 p.80 | B | highlight: “Several explanations are possible; none of them was tested …” | why write "not tested"??? | `06-discussion.tex:228` | done 2026-10-22: "none of them was tested" removed |
| 112 | v8 p.82 | B | note: The total lesion area decreases | mention the labelling disagreement from before? | `06-discussion.tex:335` | done 2026-10-22: grader agreement 0.71-0.73 added (pointer to 6.2) |
| 113 | v8 p.82 | R | highlight: “was logged only as a cohort mean per run” | don't like to mention this | `06-discussion.tex:351` | done 2026-10-22: sentence removed |
| 114 | v8 p.82 | B | highlight: “Several findings rest on one seed, and the solver-swap test on three …” | to be changed | `06-discussion.tex:353` | done 2026-10-22: ladder now on all five folds; clause removed |
| 115 | v8 p.83 | B | highlight: “A further step is to work on the volumetric OCT …” | "is" -> could be | `06-discussion.tex:432` | done 2026-10-22: "could be" |

## Chapter 7 Conclusion

| # | Page | Col | Marked | Note | Now | Status |
|---|---|---|---|---|---|---|
| 116 | v8 p.85 | B | note: the raw OCT volume instead of segmented masks | here Mai + score; other paper + score | `07-conclusion.tex:81` | done 2026-10-22: Mai 0.61, Gigon 0.52, Yoshida 0.57-0.59 |

## Appendices

| # | Page | Col | Marked | Note | Now | Status |
|---|---|---|---|---|---|---|
| 117 | v8 p.92 | B | note: end of A.1 | Fig. A.1 here | `91-appendix.tex:17-42` | done 2026-10-22: figures A.1, A.2 [h] |
| 118 | v8 p.97 | B | bracket: Figure D.1 shows rollouts | this has changed since | `91-appendix.tex:86` | done (text redone 2026-10-21); author ok |
| 119 | v8 p.99 | B | note: Table E.1 | global methods much worse on borders? | `91-appendix.tex:156` | done 2026-10-22: one sentence after Table E.1 |
| 120 | v8 p.99 | B | note: E.2 heading | new page + table, then E.3 | `91-appendix.tex:179` | done 2026-10-22: E.2 on new page, Table E.2 below, then E.3 |
| 121 | v8 p.99 | B | highlight: “for the late-epoch change-region Dice of a single run of a graph network …” | check number (sigma = 0.0127) | `91-appendix.tex:240` | done 2026-10-22: checked, 0.0127 = mean absolute difference of the seven replicate pairs (0.0143) x sqrt(pi)/2 |
| 122 | v8 p.100 | B | highlight: “is about 2.5 or larger in magnitude” | really? | `91-appendix.tex:267` | done 2026-10-22: bar kept at about 2.5, reason given in E.3 (fellow eyes, about 50 tests, set when read); only T-FEN - stencil depends on it |
| 123 | v8 p.101 | B | note: E.5 heading | new page | `91-appendix.tex:456` | done 2026-10-22: \clearpage before E.5 |
| 124 | v8 p.103 | B | note: Table E.4 | this needs to go below Table E.3 | `91-appendix.tex:350` | done 2026-10-22: Tables E.3-E.5 on new pages after the E.4 text |
| 125 | v8 p.104 | B | note: Table E.5 | goes after E.4 | `91-appendix.tex:407` | done 2026-10-22 (with #124) |
| 126 | v8 p.105 | B | note: Table E.6 | section E.5 + Table E.6 (together) | `91-appendix.tex:481` | done 2026-10-22: E.5 with Table E.6 |
| 127 | v8 p.106 | R | highlight: “each run also records the version of the code it ran …” | remove | `91-appendix.tex:567` | done 2026-10-22: sentence deleted |
| 128 | v8 p.108 | B | note: Appendix G title | possibly Appendix A | `91-appendix.tex:611` | deferred (author): move MM-PDE out of the appendix later, existing TODO |
| 129 | v8 p.108 | B | highlight: “It gave no measurable gain over the uniform grid …” | the method is a little suboptimal; the reported performance in the paper was not much; the framework was heavily modified; no counter-examples were done | `91-appendix.tex:632` | done 2026-10-22: intro gives two reasons (modified considerably, may not suit the setup); gains argument dropped (author) |
| 130 | v8 p.108 | B | note: which is large where the solution varies sharply | so where gradients are large | `91-appendix.tex:655` | done 2026-10-22 |
| 131 | v8 p.109 | B | note: end of G.1 | however the numbers they report are not awesome | `91-appendix.tex:721` | dropped 2026-10-22 (author): Hu et al. gains are not modest (cylinder: about half the error of a larger GNN); no paragraph added |
| 132 | v8 p.110 | B | highlight: “All reported five-fold runs of the extension use the earlier …” | are we sure about this, and why? We should have an argument that the dilated stencil / reach does not really work with the adaptive mesh | `91-appendix.tex:738` | done 2026-10-22: author argument (mesh pulls nodes together, dilation would skip them) + fold-2 stencil dual run |
| 133 | v8 p.110 | R | highlight: “An earlier version was trained on a square …” | remove | `91-appendix.tex:750` | done 2026-10-22: deleted |
| 134 | v8 p.110 | R | note: The blur (sigma = 1.0 px) is applied to the monitor only | this blurring is not enough (explanation) | `91-appendix.tex:780` | done 2026-10-22: blur paragraph rewritten; anisotropic-blur and Jacobian sentences removed |
| 135 | v8 p.110 | B | highlight: “Without the blur, the step of the binary mask at the lesion edge …” | this whole section needs to be rewritten; the gradient the monitor checks would be infinite at the lesion edge, which leads to instability and the DMM not working (red HL on "On the native grid, the unblurred monitor no longer diverges ...") | `91-appendix.tex:781` | done 2026-10-22 (with #134) |
| 136 | v8 p.110 | B | highlight: “with weights 1, 1000 and 1” | taken from the original | `91-appendix.tex:792` | done 2026-10-22: weighted as in the original |
| 137 | v8 p.111 | B | highlight: “Because it never sees a future state, this leaks no label …” | more info why this is not a problem | `91-appendix.tex:807` | done 2026-10-22: own paragraph on training on all masks / no held-out set |
| 138 | v8 p.111 | B | highlight: “and they helped only in combination” | surely not the correct wording | `91-appendix.tex:814` | done 2026-10-22 |
| 139 | v8 p.112 | B | note: A search in physical millimetres | ? ("physical millimetres" struck) | `91-appendix.tex:888` | done 2026-10-22 |
| 140 | v8 p.112 | R | highlight: “The implementation did so until 6 August 2026 …” | remove | `91-appendix.tex:889` | done 2026-10-22: deleted |
| 141 | v8 p.112 | R | struck: “This is a second reason for one-step prediction …” | this does not really match what we said before | `91-appendix.tex:911` | done 2026-10-22: dual model is one more operator that cannot predict several steps (pointer to 4.2) |
| 142 | v8 p.113 | B | note: The frozen mesh mover is not counted | why? | `91-appendix.tex:924` | done 2026-10-22: not trained with the solver (bypass clause dropped, author) |
| 143 | v8 p.113 | B | highlight: “The values are in-sample and do not show how the mesh mover generalises …” | however unsupervised, so it shouldn't matter | `91-appendix.tex:981` | done 2026-10-22: "in-sample (G.2.1)" |
| 144 | v8 p.113 | R | highlight: “The two pools cannot be compared with each other …” | what? how did you come up with pools? | `91-appendix.tex:982` | done 2026-10-22: only the 16 masks over 13 eyes; head-16 row and comparability sentence removed |
| 145 | v8 p.114 | B | highlight: “of 100 scored higher on edge gain” | edge gain alone is not the most important; if we weight the boundary with 100, pulling in borders can appear | `91-appendix.tex:991` | done 2026-10-22: weight 1000 from the original; edge gain alone does not judge the mesh (Hu App. C.3) |
| 146 | v8 p.115 | R | highlight: “All arms use the earlier k-nearest-neighbour graph network with mean and maximum aggregation …” | just mention it ran on kNN and not dilated stencil (Table G.3 caption) | `91-appendix.tex:739; 91-appendix.tex:1036; 91-appendix.tex:1045` | done 2026-10-22: "k-NN graph network, not the dilated stencil", no mean/max anywhere |
| 147 | v8 p.115 | R | highlight: “with mean and maximum aggregation. This is neither the canonical …” | remove | `91-appendix.tex:1036` | done 2026-10-22 (with #146) |
| 148 | v8 p.115 | B | bracket: The dual branch gives no measurable gain | this the result conversation we agreed on? | `91-appendix.tex:1065` | done 2026-10-22: G.4 results in Chapter-5 wording with z; "tightest null" removed |
| 149 | v8 p.115 | R | bracket: A probe on the trained dual model explains why | this can't go here | `91-appendix.tex:1083` | done 2026-10-22: probe paragraph removed (author: reads as if the architecture cannot learn) |
| 150 | v8 p.115 | R | highlight: “The gate therefore keeps an untrained correction from being added at full weight …” | wrong reasoning (incl. the weight-decay sentence) | `91-appendix.tex:1097` | done 2026-10-22: "untrained correction at full weight" and "gradient zero at the median" removed |
| 151 | v8 p.116 | R | note: end of G.4 | here we have more reasoning: TODO next | `91-appendix.tex:1121` | done 2026-10-22: reach reasoning + scope paragraph (one design, not a general statement on adaptive meshes) |
