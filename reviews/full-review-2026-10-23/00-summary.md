# Full review of the thesis: summary

> **Status: incomplete run (2026-10-23).** The review stopped at the weekly usage limit before it finished. All six reviewers ran on all 15 units and all 15 whole-thesis passes ran. Only the findings of the whole-thesis passes went through the three-lens verification (text, rule, sceptic); every finding marked "verification incomplete" (2,085 of 2,346) is a raw reviewer finding: not checked by the verifiers, not merged across reviewers within its unit (except Front matter), and its severity is the reviewer's own. The completeness rounds (except Front matter), the prerequisite ledger, the terminology table, severity calibration, the fix-first list, the cross-cutting themes and the reviewer paragraphs did not run. Expect duplicates (the same problem reported by several reviewers) and some false positives among the unverified findings. **Update:** the S1 and S2 findings were verified afterwards in the main session: see [03-verification-S1-S2.md](03-verification-S1-S2.md) (246 confirmed problems: 13 S1, 122 S2, 111 downgraded to S3; 1 dropped).


Review of 2026-10-23. 2346 findings (S1 53 · S2 573 · S3 923 · S4 797); the full list is in [01-findings.md](01-findings.md). Page numbers refer to review-build.pdf (build complete).

## 1. The six reviewers

**Supervisor.** U01 Front matter: The front matter is complete. The English abstract, rewritten on 2026-10-22, now follows the three-part structure I asked for (SV-A1): variability of progression comes first among the difficulties (SV-A3), the aim is stated formally (SV-A4), my GA definition is used (SV-A2), there… U02 Chapter 1 Introduction: Chapter 1 now implements most of what the supervisor asked for in review 1. Both US-approved drugs are named with their EU status, the variable growth rate motivates the forecast, "operator" and "framework" are defined at first use and used consistently, the contribution… U03 Chapter 2 opener and Section 2.1 Medical Background: From the supervisor's view, §2.1 now follows the order he asked for (anatomy, then imaging, then GA). Most medical terms that Chapter 1 left open are glossed where they first appear, and the three figures have self-contained captions with the… U04 Chapter 2, Sections 2.2-2.3: From the supervisor's point of view, §2.2 mostly does what was asked. It is a compact primer that never mentions GA. Its opening paragraph says why the reader needs it. It defines reach, the residual form, consistency, the CFL condition and the rollout before later … U05 Chapter 2, Sections 2.4-2.5: Section 2.4 now has the topic subsections the supervisor asked for (SV-2.7). Its sources are current and relevant (Lindner, Gigon, Lachinov, Mai, Yoshida, ImageFlowNet, the PDE tumour models). Section 2.5 follows the requested order of motivation first, then a forma… U06 Chapter 3 Data: From the supervisor's side, Chapter 3 carries out most of what was asked in review 1. The pixel spacings are in micrometres, the Iowa segmentation is cited and the ten boundaries are named, patients and eyes per fold are given, the mask provenance is stated plainly, the crop cen… U07 Chapter 4 opener, Sections 4.1-4.2: The unit applies most of my review-2 points: the first paragraph now says what the framework defines (SV-4.1), the Δt → 0 limit states its Lipschitz assumption (SV-4.3), §4.2.2 uses the C × H × W notation of §2.5.2 (SV-4.4), and conditioning and training now … U08 Chapter 4, Sections 4.3-4.4: Sections 4.3-4.4 carry out most of what was asked in review 2. The original MP-PDE is summarised before the adaptation, under the requested headings. Distances are given in micrometres, the distance used by each graph is named, and dilated convolutions and dilated g… U09 Chapter 5 opener, Sections 5.1-5.2: From the supervisor's perspective, Sections 5.1 to 5.3 largely implement review 2. The evaluation challenges are motivated plainly, the z-test with an empirical sigma is in place, §5.1.4 follows intro, body and conclusion with its own figure, and §5.2 opens w… U10 Chapter 5, Sections 5.3-5.4: From the supervisor's perspective, §5.4 mostly follows the agreed shape. Each subsection now goes from the question to the result to a closing paragraph. Table 5.3 carries the reach ablation with its reference rows, and effects that are not established are labelled … U11 Chapter 5, Section 5.5: From the supervisor's side, the unit mostly does what reviews 1 and 2 asked for. Each subsection runs from goal to results to conclusion. The objective and capacity studies now have their own tables, each with the reference row next to the ablation (SV-5.13), the tables … U12 Chapter 5, Sections 5.6-5.9: From the supervisor's side this unit is in good shape. The step-size test now covers all five folds, states its criteria before the results and ends on an explicit reading. The prior-work section names its caveats once and closes with a clear two-sided statement. Ev… U13 Chapters 6 and 7: From the supervisor's side, Chapters 6 and 7 now carry most of what review 2 asked for. §6.1 can be read without the rest of the thesis: it restates the task, the data and the measure and gives every result with its number. Subsections replace the run-in headings, the front ad… U14 Bibliography and Appendices A-F: From the supervisor's side the unit does most of what he asked for. Appendices A, B and D are short. Every figure and table in them is referenced and has a caption that mostly stands alone. Appendix C carries the z-test he requested (SV-5.2), with stated σ value… U15 Appendix G: Appendix E (source: Appendix G) mostly does what the supervisor asked for. The chapter opener has a section map and a thesis statement. E.3 states its purpose and closes with a conclusion. E.4 reports results in the words of Chapter 5, with z values and fold/eye counts, and limits t…

**External reviewer.** U01 Front matter: Every number in the English abstract matches Chapters 3-5: the cohort, the pixel spacings, 0.54/0.53/0.50, +0.064, +0.062, 0.5-0.65 and r = 0.40. The headline metric and its persistence zero are defined, the cross-validation is described as patient-level, and the weaker growth-spe… U02 Chapter 1 Introduction: From an external reviewer's view, Chapter 1 is well built: the clinical motivation is sourced number by number, the research question and its two parts are stated plainly, the confounder argument for fixing the framework (architecture, size or setup could explain a succe… U03 Chapter 2 opener and Section 2.1 Medical Background: From an external reviewer's view, the medical background is mostly well sourced and hedged where it needs to be. The cRORA/iRORA definitions are accurate, the Pilotto equivalence is limited to "a small cohort", the figure captions give source… U04 Chapter 2, Sections 2.2-2.3: Sections 2.2-2.3 work as a compact primer. Stencil, reach, residual form, rollout, CFL, temporal bundling and the pushforward trick are all defined before Chapters 4-5 use them, every mechanism cites a primary source, and Figure 2.5 shows the path from field to step… U05 Chapter 2, Sections 2.4-2.5: From the external reviewer's side, Related Work is now broad and well sourced. It gives concrete numbers (Lindner border speeds, Gigon Dice ranges, Yoshida r^2) and draws a clear line between rate prediction and spatial forecasting. §2.5.1 is honest that its four po… U06 Chapter 3 Data: Chapter 3 is unusually candid for a data chapter: the crop census and its censoring cost, the empty test split, the FAF provenance of the mask and the per-fold counts are all stated. The counts in Tables 3.1 and 3.2 add up (478 windows, 75 eyes, 51 patients on every fold). From … U07 Chapter 4 opener, Sections 4.1-4.2: From an operator-learning reviewer's view, §4.1–4.2 does what it is for. It names what is held fixed and why (confounding). It states the Δt → 0 limit with its Lipschitz assumption and admits that the limit says nothing about the rate. It explains why the sof… U08 Chapter 4, Sections 4.3-4.4: Sections 4.3-4.4 describe each operator on the same terms. Each original is summarised before its adaptation, and the parameter counts follow from the stated architecture: the graph network's 67 147, the one-hop and per-pixel floors and the FNO and hybrid counts all… U09 Chapter 5 opener, Sections 5.1-5.2: From the external reviewer's side, §5.1 is a careful protocol: the change-region Dice with a persistence score of zero, the late-epoch mean with its stated reasons, a comparison rule built on measured retraining noise, and the honest call that the T-FEN's lea… U10 Chapter 5, Sections 5.3-5.4: The unit reports its comparisons against stated criteria. It names nulls as nulls (second message-passing round, k = 20, the FNO's local path). It gives the parameter gap of the transport control where the result appears and answers it with the width-48 T-FEN. The ±… U11 Chapter 5, Section 5.5: From a reviewer's chair, §5.6 is mostly honest. Nulls are reported as nulls, the opener scopes them to operator, folds and seed, the objective test has its own table with fold and eye counts, and the capacity study states a design and decision rule fixed in advance. Appe… U12 Chapter 5, Sections 5.6-5.9: From an external reviewer's view, §5.7–§5.10 are mostly transparent. The step-size test re-evaluates the trained weights without retraining. Its control reproduces the recorded Dice, every setting is listed for all five folds in Table C.6, and the T-FEN stability cr… U13 Chapters 6 and 7: From a reviewer's side, Chapters 6 and 7 are mostly careful. Nulls are reported as nulls, most numbers agree with Chapter 5, the scope of the framework tests is stated in §6.1.1, and the grader scale and the clinical gaps are framed honestly. The weak points are the central in… U14 Bibliography and Appendices A-F: Appendix C holds the statistical machinery behind every "established" claim of Chapter 5. Its tables are complete, and the numbers I spot-checked agree with Chapter 5: T-FEN vs stencil, reach, the FNO comparisons, capacity, the objective rows and the step-size s… U15 Appendix G: From an external reviewer's perspective the appendix is honest and well controlled. The parameter-matched bypass control is used to withdraw the pre-registered "α → 0 means mesh adaptation does not help" reading. The mesh mover is scored separately and flagged as in-sample. Nulls ar…

**Examiner.** U01 Front matter: From the examiner's side the front matter is formally complete. The title page has every JKU field, the sworn declaration is correctly left out (the template deprecates it), and an English abstract and a German Kurzfassung are both present. The rewritten abstract follows the super… U02 Chapter 1 Introduction: Chapter 1 does what an examiner looks for first. The research question and its two parts are stated plainly, and both terms ("operator", "framework") are introduced just before them. The question is mapped to chapters, and Chapter 7 answers both parts explicitly. The cli… U03 Chapter 2 opener and Section 2.1 Medical Background: From the examiner's perspective, §2.1 is a solid, well-cited medical background. It follows the agreed order (anatomy, then imaging, then GA). All four figures are referred to in the text, and the earlier problems with mask provenance and wit… U04 Chapter 2, Sections 2.2-2.3: From the examiner's side, §2.2 does its job. It opens by saying which solver mechanisms the later chapters use (Euler step in residual form, learned and global stencils, finite elements, reach, integrator order, stability) and never mentions GA. It runs in a clean o… U05 Chapter 2, Sections 2.4-2.5: The unit closes Chapter 2 with what an examiner wants to see: a formal problem statement with the residual update, a definition of the central term, the research question restated in that notation, and a Related Work section that now has subsections, numbers and an … U06 Chapter 3 Data: Chapter 3 is within its page budget (pp. 23-30, eight pages), opens with a map of the chapter, and is honest where it matters most: it states the crop census, the censoring at the window edge, the constant-spacing assumption, the FAF origin of the mask and the empty test split. … U07 Chapter 4 opener, Sections 4.1-4.2: From the examiner's side, §4.1–§4.2 are formally sound. The chapter opens with sub-question 1, "arm" and "canonical" are defined, and the persistence check is a good integrity argument. The objective, curriculum and optimisation are given in enough detail to … U08 Chapter 4, Sections 4.3-4.4: Sections 4.3 and 4.4 describe every arm on equal terms. Each original is summarised before its adaptation, and the text is candid in several places: the physical k-NN graph is said to be unused, "the mode count was not ablated" is stated, and the free-form control's… U09 Chapter 5 opener, Sections 5.1-5.2: From the examiner's side the unit is honest and careful. It sets persistence as a floor of 0 and uses the per-pixel floor to calibrate the table. It justifies the late-epoch mean against selection bias, states the z-test with its noise estimate, and says that… U10 Chapter 5, Sections 5.3-5.4: Sections 5.4-5.5 answer the operator sub-question directly and are mostly honest. Nulls are reported as nulls (the local path, k = 20, the second message-passing round, and the FNO's lead over the k-NN network, which fold 4 carries). The transport term's parameter g… U11 Chapter 5, Section 5.5: From the examiner's side, the unit is mostly honest. Nulls are called nulls at the available precision, and the opener scopes them to operator, folds and seed. The capacity study had a decision rule fixed in advance and says it rests on one seed. Each subsection runs fro… U12 Chapter 5, Sections 5.6-5.9: The unit is mostly careful: the stability criterion is defined in full and dated as fixed before the energy-conserving form was trained, the step-size test admits that the canonical network meets Δt values it never saw in training, every comparison with prior work i… U13 Chapters 6 and 7: Both sub-questions are restated verbatim in Chapter 7 and answered explicitly. The Discussion is self-contained for a reader who skipped the thesis, both chapters keep to their page budgets (8 and 2 pages), and the limitations are stated more openly than usual: the empty test … U14 Bibliography and Appendices A-F: From the examiner's side, Appendices A to D do their job. The cohort figures reproduce the Chapter 3 numbers (0.11 to 20.8 mm², 76 % of intervals at 180 days, 67 grids). The statistical rule is stated with its formula, and every z value I recomputed from the tab… U15 Appendix G: From an examiner's point of view, Appendix E (source: Appendix G) is mostly honest. It states the pre-registered reading (α → 0 means mesh adaptation does not help) and then withdraws it because of its own bypass control. It also checks mesh quality separately from accuracy and ends…

**Colleague.** U01 Front matter: From a colleague's seat the front matter is short and mostly readable: the abstract explains persistence ("a forecast of no change scores zero"), says what the change-region Dice measures, and backs the reach argument with concrete micrometre figures. The acknowledgements and the … U02 Chapter 1 Introduction: Chapter 1 is short and keeps the agreed order (clinical motivation, aim, research question, contributions, outline). Most medical terms are glossed where they first appear, and operator and framework are each defined once at first use, so an ML reader can follow §1.1 and… U03 Chapter 2 opener and Section 2.1 Medical Background: For a reader without medical background, §2.1 mostly works: the order anatomy, then imaging, then GA is easy to follow, the A-scan to B-scan to volume to en-face sequence is built up step by step with Fig. 2.2, and photoreceptors, fundus, mac… U04 Chapter 2, Sections 2.2-2.3: For an ML reader without numerical-PDE background, §2.2 works. It goes from PDE to stencil, rate function, Euler step and rollout in a clear order. The CFL condition is tied to the newly defined reach, and Figure 2.5 shows the whole chain. I get lost mainly in §2.3.… U05 Chapter 2, Sections 2.4-2.5: From a non-medical ML reader's point of view, §2.5 works well. The four bullets explain why a solver structure fits, the last paragraph of §2.5.1 (CFL argument plus the 21:1 spacing, 'symmetric in pixels, lopsided in millimetres') is the clearest motivation for reac… U06 Chapter 3 Data: For an ML reader without medical background, Chapter 3 is mostly easy to follow. The opener maps every section, each preprocessing step is concrete and has numbers, the crop cost is reported honestly, and earlier fixes work: "censored" is glossed, "transition window" is defined … U07 Chapter 4 opener, Sections 4.1-4.2: From an ML student's seat, §4.1–4.2 are mostly easy to follow. Figure 4.1 shows the update loop plainly. The Δt → 0 argument names its Lipschitz assumption. Zero initialisation and the pushforward curriculum are explained with concrete numbers (180 vs 720 day… U08 Chapter 4, Sections 4.3-4.4: Read as an ML master student, §4.3-4.4 is mostly followable: every operator is first summarised from its paper and then adapted, the graph-construction argument in §4.3.3 (with Figure 4.2 giving physical distances for the k-NN, index-space and dilated-stencil graphs… U09 Chapter 5 opener, Sections 5.1-5.2: From a colleague's seat, §5.1 is the strongest part of the unit. It builds the evaluation step by step: why per-pixel error and full-mask Dice fail, the change-region Dice with its equation, the rollout, and the late-epoch mean with a figure that shows why th… U10 Chapter 5, Sections 5.3-5.4: From the seat of an ML student without the medical or PDE background, Sections 5.4 and 5.5 are mostly easy to follow. Each ablation subsection opens with its question, reports the comparison in words and closes with a reading. Table 5.3 and Figures 5.4 and 5.5 carry… U11 Chapter 5, Section 5.5: From a colleague's point of view, §5.6 mostly reads well. Each subsection opens by saying what is tested, and the terms it relies on (collapse counter, late-epoch window, pushforward curriculum, autonomous field, energy-conserving form) all point back to where they were … U12 Chapter 5, Sections 5.6-5.9: From the point of view of an ML student, §5.7 to §5.10 are well organised. The step-size test states its principle and both criteria before it shows any results. The stability criterion is defined before it is applied. §5.8 defines r and the AUC where they are used … U13 Chapters 6 and 7: Chapters 6 and 7 are easy to follow for a front-to-back reader. The §6.1 opener restates the task, the data and the measure, the numbers match Chapter 5 (eleven arms 0.45 to 0.54, 0.064, 0.062, 0.050, the step-size results on all five folds), and the subsections each have a cl… U14 Bibliography and Appendices A-F: Read front to back as an ML student, Appendices A, B and D are easy to follow. The figures are clear, the cohort numbers match Chapter 3, and the code map and run names make every arm traceable. Appendix C is where I get lost. C.3 states the criteria differently… U15 Appendix G: Appendix E (source: Appendix G) is organised well for an ML student. The opener maps the sections. E.1 builds the chain monitor → equidistribution → Monge–Ampère → potential → DMM in a sensible order. The α/decoder deadlock explanation, the pre-registered reading and the bypass-cont…

**Clinical reader.** U01 Front matter: From a clinical perspective the front matter is mostly careful. The abstract and the Kurzfassung name the variability of progression as the difficulty, phrase the clinical benefit conditionally ("would support"), limit the findings to "this cohort", and state the weaker growth-spe… U02 Chapter 1 Introduction: Chapter 1 is mostly accurate and well sourced from a clinical point of view. The AMD staging, the GA epidemiology and bilaterality, the 2023 FDA approvals of pegcetacoplan and avacincaptad pegol, their non-approval in the EU, the 14-27 % slowing of growth without a visua… U03 Chapter 2 opener and Section 2.1 Medical Background: From a clinical reader's side, §2.1 is mostly sound and careful. The anatomy, the OCT principle, the FAF physiology and the CAM cRORA/iRORA definitions are correct. The study figures it quotes are hedged ("in one retrospective study", "in a s… U04 Chapter 2, Sections 2.2-2.3: From a clinical reader's view the unit has little medical content. Section 2.2 keeps GA out as the supervisor asked (M3), and no medical term is misused. Figure 2.5 and its caption are purely numerical and clear. The clinical framing comes in only in the paragraphs … U05 Chapter 2, Sections 2.4-2.5: From a clinical point of view the unit is mostly careful. Related Work now has a GA-specific structure (risk and rate, spatial forecasting, irregular data, PDE models). The Mai et al. comparison carries its input-regime caveat. The boundary-growth argument rests on … U06 Chapter 3 Data: From a clinical reader's view, Chapter 3 is mostly correct and carefully hedged. The mask provenance (manual FAF outline by Vienna Reading Center graders, registered through the near-infrared image onto the OCT grid) is stated plainly and matches §6.3. The crop census is reporte… U07 Chapter 4 opener, Sections 4.1-4.2: From the clinical side, §4.1-§4.2 is mostly careful. The methods text makes few medical claims, the mask is called the clinical target and the layer channels auxiliary targets, and the lack of a common time origin and the irregular visit schedule are describe… U08 Chapter 4, Sections 4.3-4.4: Little of this unit is medical. Its one clinical quantity is the per-visit advance of the GA lesion front, and the dilated stencil is built from it. The framing is careful: distances are given in µm and match the spacings of Chapter 3; the text says plainly that no … U09 Chapter 5 opener, Sections 5.1-5.2: From the clinical side this unit says little about medicine, and most of what it says is careful. It explains why persistence is the floor and why a whole-lesion Dice says little about progression. It names the censoring at the edge of the imaged field and sp… U10 Chapter 5, Sections 5.3-5.4: From a clinical reader's perspective this unit is mostly technical. The ablation subsections (§5.4.1-§5.4.4) make no medical claims beyond the scale of the lesion front, they do not interpret the learned transport velocity clinically, and they make no claim of clini… U11 Chapter 5, Section 5.5: From the clinical side, Section 5.6 (Negative Results, 05-experiments.tex 1077-1531) is mostly methodological and gives a clinical reader little to object to. It makes no claim of clinical usefulness. The paragraph on the monotonic penalty states the biology correctly ("… U12 Chapter 5, Sections 5.6-5.9: From the clinical reader's side, Sections 5.7 (Validity Diagnostics), 5.9 (Computational Cost) and 5.10 (Summary) are numerical. They make almost no medical statements and none of those statements is wrong. Section 5.8 (Comparison with Prior Work) is where clinical … U13 Chapters 6 and 7: From a clinical perspective, Chapters 6 and 7 are mostly careful. The FAF provenance of the mask is now stated as a fact, shrinkage of the reference masks is read correctly as annotation and registration noise rather than biological regression, the grader-agreement scale from … U14 Bibliography and Appendices A-F: From a clinical perspective most of this unit is technical. Appendix A presents the visit schedule, the baseline lesion areas and the square-root growth rates correctly, and it states the constant-spacing assumption. Appendix B names three visible weaknesses hon… U15 Appendix G: From a clinical perspective Appendix G is a technical chapter with little medical content, and what there is reads correctly. Channel 0 is called the binary GA mask throughout, in line with Chapter 3. The lesion sizes in Figure E.1 and its caption agree. The closing scope paragraph …

**Copy editor.** U01 Front matter: The front matter is mechanically clean in most places: no contractions, no 'get', no sentence-initial And/But/So/Because, British spelling throughout, thin-spaced units, and a Kurzfassung with correct decimal commas that follows the English closely and is sometimes more careful ('… U02 Chapter 1 Introduction: Chapter 1 follows most mechanical rules of Guide §1. It has no contractions, no sentence opening with And/But/So/Because, no em-dash asides and no e.g./i.e.; spelling is British throughout, medical terms are glossed close to their first use, and the §1.3 bullets are shor… U03 Chapter 2 opener and Section 2.1 Medical Background: Section 2.1 and the chapter opener use consistent British spelling and avoid the hard mechanical faults: no contractions, no "get", no sentence that opens with And/But/So/Because, and no em-dash asides. All the AI-review fixes 2a.1-2a.28 are … U04 Chapter 2, Sections 2.2-2.3: Sections 2.2-2.3 are mechanically clean on the basics. There are no contractions, no "get", no em-dash asides and no American spellings, and the earlier editorial fixes (AI-2b.1 to 2b.38) are still in place. What is left is mostly polish. Three subsection headings a… U05 Chapter 2, Sections 2.4-2.5: Sections 2.4 and 2.5 are mostly clean formal English. British spelling is consistent, and the unit has no contractions, no "get", no em-dash asides and no e.g./i.e. in running text. Every earlier AI-review fix in §2.5.1 is still in place. The remaining problems are … U06 Chapter 3 Data: From the copy editor's side, Chapter 3 is in good shape. The British spelling is consistent, there are no contractions, no em-dash asides and no LLM slogans, the chapter opener gives a clear map, and the numbers carry their units. What remains is mechanical. 'Data' is singular t… U07 Chapter 4 opener, Sections 4.1-4.2: From the copy editor's side the unit is clean on the basic rules. It has no contractions, no "get", no sensational adjectives and no e.g./i.e. outside brackets, and it uses British spelling throughout. Equations are punctuated as sentences, every number carri… U08 Chapter 4, Sections 4.3-4.4: The unit gets the mechanics right. It uses British spelling throughout and keeps the thin-space number format (50\,176, 33\,\%). It has no contractions, no "get", no dash asides and almost no intensifiers, and the earlier AI-review fixes for this unit are all still … U09 Chapter 5 opener, Sections 5.1-5.2: Mechanically the unit is in good shape on the cheap rules: no contractions, no "get", no sentences opening with And/But/So, consistent British spelling (normalisation, favours, neighbour), thin spaces in thousands, units on every number, Title Case headings a… U10 Chapter 5, Sections 5.3-5.4: Mechanically the unit is in good shape. It has no contractions, no sentences opening with And/But/So/Because, no em-dash asides and consistent British spelling. Results are stated in words with their numbers, and §5.4.1-§5.4.4 follow goal, result, conclusion. The se… U11 Chapter 5, Section 5.5: Mechanically the unit is in good shape: British spelling is consistent, there are no contractions, no "get" and no exclamations, results are reported in the present tense with fold and eye counts, and the two tables have captions that state what was measured, over what a… U12 Chapter 5, Sections 5.6-5.9: Read as a copy editor, Sections 5.7 to 5.10 are mostly clean formal English. The spelling is British throughout, and the text has no contractions, no "get" and no vague quantities. Most units are thin-spaced, and every caption is written in full sentences. The step-… U13 Chapters 6 and 7: Chapters 6 and 7 are mostly in clean formal English. Spelling is British throughout, and there are no contractions, no "get" and no sentence opening with And, But, So or Because. Distances are in micrometres, and percentages, cross-references and the run-in headings of §6.4 ar… U14 Bibliography and Appendices A-F: From the copy editor's side, Appendices A-D are mostly clean. British spelling is used throughout, the defined terms (change-region Dice, one-year anchor, late-epoch mean, transition window) keep their meaning, headings are in consistent Title Case and the capti… U15 Appendix G: Appendix E (MM-PDE) reads cleanly at the sentence level: British spelling is consistent, there are no contractions, dashes or "e.g./i.e." problems, most earlier AI items (G.19, G.23, G.28, G.35, G.38, G.42, G.50) still hold, and the result is reported in the plain Chapter-5 wording.…

**Whole-thesis passes.**
- structure: The thesis has a clear research question with two sub-questions. The chapter order follows the agreed structure: medical and numerical background, then motivation and problem statement, then the framework before the operators, and a summary at the end of Chapter 5. Chapter 1 states both sub-questions and Chapter 7 answers each one under its own paragraph. The abstract, §5.10, §6.1 and Chapter 7 give the same central numbers (0.54 / 0.53 / 0.50, +0.064 for reach, +0.062 for transport, r = 0.40), and the English abstract and the Kurzfassung agree in content. The weak points are in how the argum…
- facts: Checked every place in the printed thesis where the following are stated: the definitions (change-region Dice, growth-region Dice, the one-year anchor, the late-epoch mean, the canonical model, persistence, arm, fold, operator, framework, border-touching, stable, established, reach), and the facts about data and setting (cohort size and how it relates to Mai et al. 2024, mask provenance, device, pixel spacing, scan footprint and crop window, crop census, visit intervals, visits per eye, layer boundaries, front advance, seeds). Sources were the abstract and Kurzfassung, Chapters 1-7, all capti…
- numbers-a: 74 numbers checked, 4 disagree
- numbers-b: 101 numbers checked, 5 disagree. Checked: every prose number of §5.2 (0.04, 0.0000, 0.43-0.52, best-fold statement, 0.017 / 4 of 5 / 46 of 75, 0.021 / 3 of 5 / z = 2.1 and 0.8, 0.038 / 5 of 5 / 51 of 75, 54 eyes, z = 2.1 vs 1.96, t = 3.1 / 2.2 vs 2.5, 91 vs 367 s, four times, the Fig. 5.2 caption values, four further eyes), all cells of Table 5.1 (parameters, ratios, mean ± sd, best fold, s/epoch) and the three numerical statements of the printed §5.10 Summary. They were compared against Ch. 4 (parameter table, operator sections), §5.1.5, §5.3-§5.9, Ch. 6, Ch. 7, the abstract and Kurzfassung,…
- numbers-c: 64 numbers checked, 9 disagree. Most of the quantitative content of Chapter 6 matches the rest of the thesis exactly: the cohort facts (75 eyes, 51 patients, 24 bilateral, 12 to 20 validation eyes per fold, 5 to 13 visits, intervals 90 to 720 days), the headline scores (0.543 / 0.526 / 0.505), reach +0.064 and transport +0.062, the T-FEN lead of 0.017 with z = 2.1 and t = 2.2 / 3.1, the reach ladder, the four-round result (-0.009), the cost ratios (about 4x, 4.8x), the growth-speed values (r 0.40 against 0.52 to 0.61, AUCs 0.70 to 0.74 against 0.77 to 0.81), the step-ladder fold counts and th…
- numbers-d: 21 numbers checked, 2 disagree. Every value in Chapter 7 is the same as, and rounded the same way as, Table 5.1, Sections 5.3, 5.5 and 5.7, Section 6.1, the abstract, the Kurzfassung and the Appendix C tables. The checked values: 0.50 to 0.54, at most about 0.04, 0 to about 0.45, 0.064, 0.062, about 0.05 from soft-Dice, the four capacity classes, and r of 0.40 against 0.61, 0.52 and 0.57 to 0.59. The two disagreements are readings of comparisons, not values. (1) The seed-7 FNO and local-path reading is stronger than the appendix allows. (2) The plain-MSE result is credited to the mask weighti…
- format-text: The mechanical format is largely uniform across all chapters and appendices. British spelling, \citet/\citep use and their placement before punctuation, LaTeX quotation marks, percentages (39\,%), Title Case for numbered headings, sentence case for run-in headings, the spelled-out and capitalised Figure/Table/Chapter/Appendix references, thin-space separators in large numbers and ± in math mode are all applied consistently. The deviations cluster in a few places: Chapter 2 (sentence-case subsection headings, bare \eqref and "Eq." references, "(a)" panel references, § at sentence starts); the …
- format-floats: The floats are formally uniform where it is easiest to see: booktabs throughout with no vertical rules, figure captions below and table captions above with the label directly after, every caption ending with a full stop and stating what ± means, arm colours taken from the style/ palette in every data figure, and nothing unfinished printed. The non-uniformity lies in the details. One arm carries up to five different labels across tables and legends. Equations are cited in four forms, and 9 of the 20 numbered equations are never cited. Panel letters are set three ways, numbers in one table row …
- flow-a: The stretch follows the agreed order (medical background, solvers without GA, related work, motivation, formal problem) and has the hour-glass shape it should: Chapter 1 narrows from AMD epidemiology to the two-part research question, and Chapter 2 widens into background and narrows again to the formal problem in §2.5.2. Chapters 2 and 3 open with section maps, and most subsections hand over explicitly. The weak points are the order of paragraphs inside sections, not the order of the sections: - §1.1 goes back from GA to AMD. - §1.1 ends by placing the thesis among GA-development (risk) work,…
- flow-b: The stretch keeps the hour-glass shape. §2.5 narrows from motivation to a formal problem statement, and Chapters 3 and 4 then go into full technical detail. Most sections open with a roadmap, and Chapter 4 ends by handing over cleanly to Chapter 5. The main weakness is order: in several places material appears before the reader has what it depends on. The schedule counts and the anchor come before the curriculum and the evaluation, covariates are described before windows are defined, and padding is explained before normalisation. Results also leak backwards into the Method chapter (the 1/Δt s…
- flow-c: The stretch keeps the hour-glass shape. Chapter 5 is the deep, narrow part, with a section map, subsections that mostly run goal, results, conclusion, and a summary that hands over to Chapter 6. Chapter 6 opens with a recap that stands on its own and widens step by step: implications for modelling, clinical use, limitations, future work. Chapter 7 ends on a broad statement. Most flow problems come from two sections inserted late, §5.3 (Forecasts Beyond One Year) and §5.5 (Differences Between Folds). Their neighbours still hand over past them, their horizon numbers are repeated in §5.4.3, §5.4…
- flow-d: Appendices A, B and D are short. Each points back to its chapter, but two of them have no pointer from the main text: Figure A.2 is never cited in §3.3, and Appendix D is not cited in §4.4. Appendix E works as a self-contained piece with a section map and clear handovers from E.1 to E.4. Inside it, three things break the line of argument. The E.2 opener mixes design choices with a fold-2 result. The single branch of E.4 does not match the k-NN arm that E.2.2 and Table 5.1 point to. The reading of the gate comes after the variant runs instead of after the gate data. The weakest transition is t…
- repetition-content: The thesis repeats itself moderately: the large blocks that earlier reviews flagged (the crop census, the cohort description, the caveats of the Mai et al. comparison) are now stated once, with pointers elsewhere. About two dozen facts and arguments are still restated in full, though. Most of them are in Chapter 5: the horizon values come back in the ablation subsections, the Galerkin versus energy-conserving T-FEN story appears in six places, and §5.4.5 retells the reach argument with all its numbers. The continuous-time caution, the shrinkage of the reference masks and the justification of …
- repetition-wording: 27 repeated phrases reported. A script scanned the English abstract, Chapters 1-7 and Appendices A-E, with comments, \iffalse blocks, tabulars, math, citations and refs removed. It found 360 repeated 7+-word segments, which come to about 180 distinct pairs. Most of these are short-caption/caption pairs, captions that restate the text next to them, the restated research question, or the settled Chapter 5 reporting template. It also found 629 recurring 3-5-word phrases, nearly all of them defined technical terms ("change-region Dice", "one-year anchor", "dilated stencil", "within the noise leve…
- mechanics: The sweep covered the printed text of Chapters 1-7, the appendices and the pipeline figure file, skipping comments, \iffalse blocks and the German Kurzfassung. The English abstract was left out because its rewrite is deferred (M1). Eight patterns occur more than twice and are reported below: colon hinges between two complete clauses (at least 96, a heuristic lower bound), sentences opening with "Because" (28; none open with And, But or So apart from one "So far"), "X, not Y" contrast closers (14), "X (does not) decide(s) Y" verdicts (6), pseudo-clefts (4), vague quantities where the thesis ha…

## 2. Counts

| Part | S1 | S2 | S3 | S4 | Total |
|---|---|---|---|---|---|
| Front matter | 21 | 18 | 29 | 27 | 95 |
| Ch. 1 | 2 | 32 | 37 | 44 | 115 |
| Ch. 2 | 3 | 103 | 136 | 159 | 401 |
| Ch. 3 | 0 | 19 | 73 | 69 | 161 |
| Ch. 4 | 3 | 53 | 122 | 103 | 281 |
| Ch. 5 | 16 | 193 | 296 | 178 | 683 |
| Ch. 6 | 3 | 72 | 83 | 41 | 199 |
| Ch. 7 | 0 | 13 | 19 | 5 | 37 |
| Bibliography | 0 | 6 | 3 | 29 | 38 |
| Appendices | 5 | 64 | 125 | 142 | 336 |
| **All** | 53 | 573 | 923 | 797 | 2346 |

## 3. Fix first


## 4. Cross-cutting issues


## 5. Prerequisite ledger

1472 terms in the inventories: 979 ok, 233 late, 260 missing. Listed: every medical and imaging term and every term explained late or never.

| Term | Kind | First use | Explained | Status |
|---|---|---|---|---|
| Geographic Atrophy | medical | main-thesis.tex:190 | 00-abstract.tex:58 | late |
| PDE | math | main-thesis.tex:190 | acronyms.tex:47 | late |
| partial differential equation | math | main-thesis.tex:190 | 02-background.tex:388 | late |
| neural PDE solver | ml | main-thesis.tex:190 | 02-background.tex:12 | late |
| OCT | imaging | main-thesis.tex:190 | 00-abstract.tex:65 | late |
| optical coherence tomography | imaging | main-thesis.tex:190 | 02-background.tex:159 | late |
| longitudinal (repeated imaging of the same eye over visits) | imaging | main-thesis.tex:190 | 01-introduction.tex:95 | late |
| GA progression forecast | project | main-thesis.tex:190 | 00-abstract.tex:60 | late |
| graph neural network | ml | main-thesis.tex:238 | 02-background.tex:634 | late |
| U-Net | ml | main-thesis.tex:238 | 02-background.tex:720 | late |
| Δt-conditioning (Δt as input of the operator) | project | main-thesis.tex:275 | 04-method.tex:152 | late |
| numerical solver | math | main-thesis.tex:275 | 02-background.tex:406 | late |
| surrogate architecture | ml | main-thesis.tex:275 | 02-background.tex:718 | late |
| spatial standardisation | project | main-thesis.tex:275 | 03-data.tex:239 | late |
| normalisation | ml | main-thesis.tex:275 | 03-data.tex:329 | late |
| patient-level covariates (conditioning) | medical | main-thesis.tex:275 | 02-background.tex:908 | late |
| multi-channel state | project | main-thesis.tex:275 | 02-background.tex:903 | late |
| pushforward (trick) | ml | main-thesis.tex:275 | 02-background.tex:699 | late |
| operator contract | project | main-thesis.tex:275 | 04-method.tex:500 | late |
| message passing | ml | main-thesis.tex:275 | 02-background.tex:632 | late |
| dense operator | project | main-thesis.tex:275 | 04-method.tex:837 | late |
| local-kernel hybrid | ml | main-thesis.tex:275 | 02-background.tex:727 | late |
| locality floor | project | main-thesis.tex:275 | 04-method.tex:959 | late |
| rollout | math | main-thesis.tex:275 | 02-background.tex:527 | late |
| late-epoch mean | project | main-thesis.tex:275 | 05-experiments.tex:204 | late |
| epoch | ml | main-thesis.tex:275 | 04-method.tex:432 | late |
| ablation study | ml | main-thesis.tex:275 | 05-experiments.tex:620 | late |
| global and local context | project | main-thesis.tex:275 | 02-background.tex:724 | late |
| validity diagnostics | project | main-thesis.tex:275 | 05-experiments.tex:1534 | late |
| solver-swap test | project | main-thesis.tex:275 | 05-experiments.tex:1540 | late |
| numerical stability | math | main-thesis.tex:275 | 02-background.tex:539 | late |
| equation features | ml | main-thesis.tex:275 | 04-method.tex:569 | late |
| native grid | imaging | main-thesis.tex:275 | 03-data.tex:81 | late |
| crop | project | main-thesis.tex:275 | 03-data.tex:241 | late |
| border-touching and interior eyes | project | main-thesis.tex:275 | 05-experiments.tex:150 | late |
| arm | project | main-thesis.tex:275 | 04-method.tex:26 | late |
| step-size ladder | project | main-thesis.tex:275 | 05-experiments.tex:1594 | late |
| moving mesh | math | main-thesis.tex:275 | 91-appendix.tex:631 | late |
| data-free mesh mover | ml | main-thesis.tex:275 | 91-appendix.tex:672 | late |
| dual-branch composition | project | main-thesis.tex:275 | 91-appendix.tex:870 | late |
| FNO | ml | main-thesis.tex:275 | acronyms.tex:36 | late |
| T-FEN | ml | main-thesis.tex:275 | acronyms.tex:52 | late |
| MM-PDE | ml | main-thesis.tex:275 | acronyms.tex:41 | late |
| GA | medical | 00-abstract.tex:58 | 00-abstract.tex:58 | ok |
| age-related macular degeneration | medical | 00-abstract.tex:58 | 01-introduction.tex:11 | late |
| retina / retinal tissue | medical | 00-abstract.tex:59 | 02-background.tex:65 | late |
| lesion | medical | 00-abstract.tex:60 | 00-abstract.tex:59 | ok |
| growth rate (speed of lesion growth) | medical | 00-abstract.tex:60 | 03-data.tex:95 | late |
| visit | medical | 00-abstract.tex:62 | 02-background.tex:1018 | late |
| architecture class | ml | 00-abstract.tex:68 | 00-abstract.tex:80 | late |
| residual update (current state plus Δt-scaled update) | project | 00-abstract.tex:71 | 00-abstract.tex:77 | late |
| lesion front | medical | 00-abstract.tex:71 | 02-background.tex:942 | late |
| follow-up | medical | 00-abstract.tex:75 | 03-data.tex:34 | late |
| en-face grid | imaging | 00-abstract.tex:75 | 01-introduction.tex:94 | late |
| binary GA mask | imaging | 00-abstract.tex:76 | 00-abstract.tex:76 | ok |
| graders | medical | 00-abstract.tex:76 | 03-data.tex:68 | late |
| depth map | imaging | 00-abstract.tex:76 | 03-data.tex:198 | late |
| retinal layer boundaries | medical | 00-abstract.tex:77 | 01-introduction.tex:96 | late |
| segmentation (segmented layer boundaries) | imaging | 00-abstract.tex:77 | never | missing |
| loss | ml | 00-abstract.tex:79 | 04-method.tex:289 | late |
| Fourier Neural Operator | ml | 00-abstract.tex:81 | 02-background.tex:669 | late |
| Finite Element Network | ml | 00-abstract.tex:81 | 02-background.tex:731 | late |
| patient-level five-fold cross-validation | ml | 00-abstract.tex:83 | 03-data.tex:441 | late |
| baseline (first visit) | medical | 00-abstract.tex:84 | 03-data.tex:35 | late |
| fold | ml | 00-abstract.tex:85 | 03-data.tex:441 | late |
| seed | ml | 00-abstract.tex:86 | 04-method.tex:34 | late |
| transport term | ml | 00-abstract.tex:89 | 02-background.tex:733 | late |
| spatial context | project | 00-abstract.tex:91 | 02-background.tex:724 | late |
| loss that emphasises the lesion (mask weighting) | project | 00-abstract.tex:91 | 04-method.tex:304 | late |
| fourth-order Runge–Kutta step | math | 00-abstract.tex:93 | 02-background.tex:517 | late |
| anisotropic grid | imaging | 00-abstract.tex:94 | 00-abstract.tex:94 | ok |
| B-scan | imaging | 00-abstract.tex:94 | 02-background.tex:147 | late |
| stencil | math | 00-abstract.tex:98 | 02-background.tex:446 | late |
| AMD | medical | acronyms.tex:32 | acronyms.tex:32 | ok |
| FAF | imaging | acronyms.tex:34 | acronyms.tex:34 | ok |
| RPE | medical | acronyms.tex:50 | acronyms.tex:50 | ok |
| SLO | imaging | acronyms.tex:51 | acronyms.tex:51 | ok |
| AMD (age-related macular degeneration) | medical | 01-introduction.tex:11 | 01-introduction.tex:11 | ok |
| macula | medical | 01-introduction.tex:11 | 01-introduction.tex:23 | late |
| central vision | medical | 01-introduction.tex:12 | 01-introduction.tex:23 | late |
| moderate-to-severe vision impairment | medical | 01-introduction.tex:13 | never | missing |
| early and intermediate AMD stages | medical | 01-introduction.tex:17 | 01-introduction.tex:19 | ok |
| neovascular AMD | medical | 01-introduction.tex:18 | 01-introduction.tex:18 | ok |
| drusen | medical | 01-introduction.tex:19 | 01-introduction.tex:19 | ok |
| atrophy | medical | 01-introduction.tex:19 | 00-abstract.tex:59 | ok |
| GA (Geographic Atrophy) | medical | 01-introduction.tex:21 | 01-introduction.tex:21 | ok |
| retina | medical | 01-introduction.tex:23 | 02-background.tex:65 | late |
| visual acuity | medical | 01-introduction.tex:24 | 01-introduction.tex:61 | late |
| fovea | medical | 01-introduction.tex:24 | 01-introduction.tex:24 | ok |
| cataract | medical | 01-introduction.tex:28 | never | missing |
| glaucoma | medical | 01-introduction.tex:28 | never | missing |
| diabetic retinopathy | medical | 01-introduction.tex:28 | never | missing |
| avoidable causes of vision loss | medical | 01-introduction.tex:29 | 01-introduction.tex:30 | ok |
| GA progression | medical | 01-introduction.tex:32 | 01-introduction.tex:46 | late |
| prevalence | other | 01-introduction.tex:34 | never | missing |
| bilateral GA | medical | 01-introduction.tex:39 | 01-introduction.tex:38 | ok |
| cohort | other | 01-introduction.tex:39 | 03-data.tex:26 | late |
| AREDS (Age-Related Eye Disease Study) | medical | 01-introduction.tex:40 | 01-introduction.tex:40 | ok |
| cumulative probability | math | 01-introduction.tex:41 | never | missing |
| concordance (between the two eyes) | other | 01-introduction.tex:44 | never | missing |
| incidence | other | 01-introduction.tex:44 | never | missing |
| lesion growth rate (area per year) | medical | 01-introduction.tex:46 | 01-introduction.tex:46 | ok |
| phase 1-3 clinical trials | medical | 01-introduction.tex:50 | never | missing |
| neuroprotection | medical | 01-introduction.tex:51 | never | missing |
| visual cycle modulation | medical | 01-introduction.tex:51 | never | missing |
| antiamyloid pathways | medical | 01-introduction.tex:52 | never | missing |
| cell replacement | medical | 01-introduction.tex:52 | never | missing |
| complement inhibitors | medical | 01-introduction.tex:54 | 01-introduction.tex:54 | ok |
| pegcetacoplan | medical | 01-introduction.tex:54 | 01-introduction.tex:54 | ok |
| avacincaptad pegol | medical | 01-introduction.tex:55 | 01-introduction.tex:54 | ok |
| complement cascade | medical | 01-introduction.tex:56 | 01-introduction.tex:56 | ok |
| best-corrected visual acuity | medical | 01-introduction.tex:61 | 01-introduction.tex:62 | ok |
| sham injection | medical | 01-introduction.tex:63 | 01-introduction.tex:63 | ok |
| trial endpoint | medical | 01-introduction.tex:63 | never | missing |
| OCT (optical coherence tomography) | imaging | 01-introduction.tex:73 | 01-introduction.tex:73 | ok |
| biomarkers | medical | 01-introduction.tex:76 | 01-introduction.tex:75 | ok |
| artificial intelligence | ml | 01-introduction.tex:77 | never | missing |
| en-face projection | imaging | 01-introduction.tex:94 | 01-introduction.tex:94 | ok |
| OCT volume | imaging | 01-introduction.tex:95 | 01-introduction.tex:73 | ok |
| longitudinal imaging | imaging | 01-introduction.tex:95 | 01-introduction.tex:96 | ok |
| grid (en-face pixel grid) | imaging | 01-introduction.tex:96 | 02-background.tex:257 | late |
| lesion outline (lesion mask) | imaging | 01-introduction.tex:96 | 02-background.tex:268 | late |
| retinal layers | medical | 01-introduction.tex:97 | 02-background.tex:103 | late |
| layer boundary depths | imaging | 01-introduction.tex:97 | 02-background.tex:268 | late |
| conversion to a later disease stage | medical | 01-introduction.tex:101 | 01-introduction.tex:101 | ok |
| risk score | other | 01-introduction.tex:104 | never | missing |
| neural PDE solvers | ml | 01-introduction.tex:109 | 02-background.tex:12 | late |
| operator size (parameter count) | ml | 01-introduction.tex:113 | 04-method.tex:1178 | late |
| training | ml | 01-introduction.tex:116 | 02-background.tex:1055 | late |
| evaluation | ml | 01-introduction.tex:116 | 02-background.tex:1056 | late |
| irregular visit schedules | project | 01-introduction.tex:154 | 02-background.tex:898 | late |
| \Delta t-scaled residual update | project | 01-introduction.tex:155 | 02-background.tex:538 | late |
| pushforward | ml | 01-introduction.tex:156 | 02-background.tex:699 | late |
| curriculum measured in elapsed days | ml | 01-introduction.tex:156 | 04-method.tex:380 | late |
| accuracy (of a forecast) | ml | 01-introduction.tex:159 | 02-background.tex:1056 | late |
| five-fold cross-validation | ml | 01-introduction.tex:163 | 03-data.tex:441 | late |
| physical reach | project | 01-introduction.tex:164 | 02-background.tex:496 | late |
| integration order | math | 01-introduction.tex:169 | 02-background.tex:517 | late |
| monotonic-growth penalty | project | 01-introduction.tex:170 | 04-method.tex:349 | late |
| adaptive moving mesh | math | 01-introduction.tex:170 | 91-appendix.tex:631 | late |
| Medical University of Vienna GA cohort | project | 01-introduction.tex:188 | 03-data.tex:26 | late |
| eleven-channel state (channel) | project | 01-introduction.tex:189 | 02-background.tex:903 | late |
| partial differential equation (concept) | math | 02-background.tex:10 | 02-background.tex:388 | late |
| neural network | ml | 02-background.tex:13 | never | missing |
| update (of a solver) | math | 02-background.tex:13 | 02-background.tex:522 | late |
| temporal side / nasal side | medical | 02-background.tex:40 | never | missing |
| cornea | medical | 02-background.tex:41 | 02-background.tex:41 | ok |
| lens | medical | 02-background.tex:41 | 02-background.tex:41 | ok |
| vitreous body | medical | 02-background.tex:41 | 02-background.tex:64 | late |
| photoreceptor | medical | 02-background.tex:44 | 02-background.tex:68 | late |
| optic disc | medical | 02-background.tex:44 | 02-background.tex:44 | ok |
| ONH (acronym) | medical | 02-background.tex:45 | 02-background.tex:45 | ok |
| optic nerve | medical | 02-background.tex:45 | 02-background.tex:69 | late |
| choroid | medical | 02-background.tex:46 | 02-background.tex:73 | late |
| fundus | medical | 02-background.tex:47 | 02-background.tex:47 | ok |
| pupil | medical | 02-background.tex:48 | never | missing |
| foveola | medical | 02-background.tex:50 | 02-background.tex:49 | ok |
| parafovea | medical | 02-background.tex:51 | 02-background.tex:51 | ok |
| perifovea | medical | 02-background.tex:51 | 02-background.tex:51 | ok |
| choriocapillaris | medical | 02-background.tex:75 | 02-background.tex:74 | ok |
| sclera | medical | 02-background.tex:75 | 02-background.tex:75 | ok |
| foveal | medical | 02-background.tex:93 | 02-background.tex:93 | ok |
| eccentric (distance from the fovea) | medical | 02-background.tex:95 | never | missing |
| subfoveal | medical | 02-background.tex:97 | 02-background.tex:97 | ok |
| extrafoveal | medical | 02-background.tex:98 | 02-background.tex:98 | ok |
| inner / outer (depth direction in the retina) | medical | 02-background.tex:106 | 02-background.tex:104 | ok |
| inner limiting membrane | medical | 02-background.tex:106 | 02-background.tex:106 | ok |
| retinal nerve fibre layer | medical | 02-background.tex:107 | 02-background.tex:107 | ok |
| ganglion-cell layer | medical | 02-background.tex:107 | 02-background.tex:107 | ok |
| inner-plexiform layer | medical | 02-background.tex:107 | 02-background.tex:107 | ok |
| inner nuclear layer | medical | 02-background.tex:108 | 02-background.tex:108 | ok |
| outer plexiform layer | medical | 02-background.tex:108 | 02-background.tex:108 | ok |
| outer nuclear layer | medical | 02-background.tex:108 | 02-background.tex:108 | ok |
| photoreceptor inner and outer segments | medical | 02-background.tex:109 | never | missing |
| Bruch's membrane | medical | 02-background.tex:110 | 02-background.tex:110 | ok |
| outer-retinal stack of three layers | medical | 02-background.tex:113 | 02-background.tex:314 | late |
| layer-boundary depth map | project | 02-background.tex:115 | 02-background.tex:268 | late |
| retinal layer boundary | medical | 02-background.tex:115 | 01-introduction.tex:96 | ok |
| lesion mask (binary GA mask) | project | 02-background.tex:116 | 03-data.tex:193 | late |
| en-face | imaging | 02-background.tex:120 | 01-introduction.tex:94 | ok |
| 2D (abbreviation) | other | 02-background.tex:120 | never | missing |
| beam splitter | imaging | 02-background.tex:141 | 02-background.tex:141 | ok |
| reference arm | imaging | 02-background.tex:142 | 02-background.tex:142 | ok |
| sample arm | imaging | 02-background.tex:142 | 02-background.tex:142 | ok |
| A-scan | imaging | 02-background.tex:146 | 02-background.tex:145 | ok |
| lateral (direction across the retina) | imaging | 02-background.tex:152 | 02-background.tex:180 | late |
| low-coherence near-infrared light | imaging | 02-background.tex:162 | never | missing |
| probe beam | imaging | 02-background.tex:162 | 02-background.tex:162 | ok |
| interferometry | imaging | 02-background.tex:170 | 02-background.tex:170 | ok |
| interference pattern | imaging | 02-background.tex:175 | never | missing |
| spectral-domain OCT | imaging | 02-background.tex:176 | 02-background.tex:175 | ok |
| voxel | imaging | 02-background.tex:186 | 02-background.tex:186 | ok |
| MUW (acronym) | project | 02-background.tex:187 | 03-data.tex:27 | late |
| modelling grid | project | 02-background.tex:191 | 03-data.tex:239 | late |
| grid | math | 02-background.tex:191 | 02-background.tex:418 | late |
| imaging modality | imaging | 02-background.tex:193 | never | missing |
| lipofuscin | medical | 02-background.tex:201 | 02-background.tex:201 | ok |
| modelling window | project | 02-background.tex:226 | 03-data.tex:249 | late |
| natural history (of a disease) | medical | 02-background.tex:234 | never | missing |
| blue-light FAF vs near-infrared FAF | imaging | 02-background.tex:235 | never | missing |
| inter-reader intraclass correlation coefficient | math | 02-background.tex:237 | never | missing |
| statistically equivalent | math | 02-background.tex:239 | never | missing |
| outer-retinal layer dropout | medical | 02-background.tex:244 | 02-background.tex:354 | late |
| choroidal hypertransmission | imaging | 02-background.tex:245 | 02-background.tex:303 | late |
| segmentation | imaging | 02-background.tex:246 | 03-data.tex:65 | late |
| slab | imaging | 02-background.tex:247 | 02-background.tex:265 | late |
| coronal section | imaging | 02-background.tex:265 | 02-background.tex:265 | ok |
| projection (en-face) | imaging | 02-background.tex:266 | 02-background.tex:263 | ok |
| growth rate | medical | 02-background.tex:273 | 01-introduction.tex:45 | ok |
| layer thickness | imaging | 02-background.tex:273 | 02-background.tex:103 | ok |
| forward problem | math | 02-background.tex:275 | never | missing |
| ELM (acronym) | medical | 02-background.tex:298 | 02-background.tex:290 | ok |
| OCT signatures of GA | imaging | 02-background.tex:300 | 02-background.tex:300 | ok |
| ONL (acronym) | medical | 02-background.tex:301 | 02-background.tex:290 | ok |
| RPE-BM complex thickening | medical | 02-background.tex:304 | 02-background.tex:304 | ok |
| BM (acronym) | medical | 02-background.tex:304 | 02-background.tex:290 | ok |
| lesion margin | medical | 02-background.tex:305 | never | missing |
| CAM | medical | 02-background.tex:326 | 02-background.tex:326 | ok |
| cRORA | medical | 02-background.tex:328 | 02-background.tex:328 | ok |
| RPE band | imaging | 02-background.tex:332 | never | missing |
| RPE tear | medical | 02-background.tex:333 | never | missing |
| macular neovascularisation | medical | 02-background.tex:335 | 01-introduction.tex:18 | ok |
| iRORA | medical | 02-background.tex:338 | 02-background.tex:338 | ok |
| retrospective study | other | 02-background.tex:340 | never | missing |
| intermediate AMD | medical | 02-background.tex:341 | 01-introduction.tex:17 | ok |
| channel (Channel 0) | project | 02-background.tex:347 | 02-background.tex:1026 | late |
| state tensor | project | 02-background.tex:348 | 02-background.tex:1021 | late |
| label (class label) | ml | 02-background.tex:350 | never | missing |
| ellipsoid zone | medical | 02-background.tex:355 | 02-background.tex:354 | ok |
| column-summed signal | imaging | 02-background.tex:361 | 02-background.tex:165 | ok |
| basal-laminar deposits | medical | 02-background.tex:367 | never | missing |
| square-root lesion enlargement rate | medical | 02-background.tex:369 | 03-data.tex:95 | late |
| biomarker | medical | 02-background.tex:371 | 01-introduction.tex:75 | ok |
| state (grid state) | project | 02-background.tex:378 | 02-background.tex:421 | late |
| update operator (A) | math | 02-background.tex:379 | 02-background.tex:522 | late |
| explicit Euler step | math | 02-background.tex:381 | 02-background.tex:510 | late |
| explicit (time-stepping scheme, as opposed to implicit) | math | 02-background.tex:381 | never | missing |
| residual form | math | 02-background.tex:381 | 02-background.tex:536 | late |
| learned stencil | ml | 02-background.tex:382 | 02-background.tex:571 | late |
| global spectral methods (pseudospectral methods) | math | 02-background.tex:383 | 02-background.tex:480 | late |
| finite elements / FEM (finite element method) | math | 02-background.tex:383 | 02-background.tex:454 | late |
| time integrator / time-stepping scheme | math | 02-background.tex:384 | 02-background.tex:507 | late |
| order of an integration scheme (higher-order, fourth-order) | math | 02-background.tex:384 | 05-experiments.tex:1571 | late |
| stability | math | 02-background.tex:385 | 02-background.tex:539 | late |
| D (dimension of the spatial domain, \mathbb{R}^D) | math | 02-background.tex:390 | never | missing |
| F (law of the process, right-hand side of the PDE) | math | 02-background.tex:393 | 02-background.tex:398 | late |
| T (final time of the interval [0, T]) | math | 02-background.tex:394 | never | missing |
| FVM (finite volume method) | math | 02-background.tex:428 | 02-background.tex:449 | late |
| stencil coefficients \alpha_j^{(n)} | math | 02-background.tex:441 | 02-background.tex:444 | late |
| node (vertex of a finite-element mesh) | math | 02-background.tex:457 | never | missing |
| Finite Element Networks | ml | 02-background.tex:466 | 02-background.tex:731 | late |
| sharp front | math | 02-background.tex:470 | never | missing |
| Fourier space / Fourier domain | math | 02-background.tex:480 | never | missing |
| Fourier mode, frequency \omega | math | 02-background.tex:481 | never | missing |
| i (imaginary unit in (i\omega)^n; clashes with the cell index i) | math | 02-background.tex:481 | never | missing |
| periodic domain / smooth and non-smooth solutions | math | 02-background.tex:489 | never | missing |
| norm \lVert\cdot\rVert | math | 02-background.tex:535 | never | missing |
| C_max (scheme-dependent CFL constant) | math | 02-background.tex:546 | 02-background.tex:549 | late |
| surrogate (PDE surrogate) | ml | 02-background.tex:606 | 02-background.tex:867 | late |
| turbulent flow | other | 02-background.tex:623 | never | missing |
| reanalysis data | other | 02-background.tex:629 | never | missing |
| operational numerical model | other | 02-background.tex:629 | never | missing |
| verification targets | other | 02-background.tex:630 | never | missing |
| \mathcal{F} as a function space (clashes with the Fourier transform \mathcal{F} at l. 484) | math | 02-background.tex:658 | never | missing |
| irregular visit intervals | medical | 02-background.tex:665 | 02-background.tex:665 | ok |
| kernel integral operator | ml | 02-background.tex:670 | 04-method.tex:879 | late |
| layer (of a neural network) | ml | 02-background.tex:672 | never | missing |
| equation family | math | 02-background.tex:675 | 04-method.tex:572 | late |
| prediction horizon / temporal horizon | project | 02-background.tex:676 | 02-background.tex:682 | late |
| longitudinal data | medical | 02-background.tex:680 | 01-introduction.tex:95 | ok |
| ill-posed | math | 02-background.tex:682 | never | missing |
| ground truth | ml | 02-background.tex:688 | never | missing |
| forward pass | ml | 02-background.tex:697 | never | missing |
| gradients / backpropagation | ml | 02-background.tex:702 | never | missing |
| encoder-decoder architecture | ml | 02-background.tex:720 | 04-method.tex:840 | late |
| skip connections | ml | 02-background.tex:721 | 04-method.tex:847 | late |
| (multi-scale) receptive field | ml | 02-background.tex:721 | never | missing |
| baseline (reference model) | ml | 02-background.tex:722 | never | missing |
| convolutional operators | ml | 02-background.tex:726 | never | missing |
| high-frequency details | math | 02-background.tex:729 | never | missing |
| transport (advection) term | math | 02-background.tex:733 | 04-method.tex:990 | late |
| inference | ml | 02-background.tex:739 | never | missing |
| irregularly sampled / irregular intervals between visits | other | 02-background.tex:769 | 02-background.tex:897 | late |
| artificial intelligence / machine learning / deep learning | ml | 02-background.tex:779 | never | missing |
| disease conversion / time to conversion | medical | 02-background.tex:779 | 01-introduction.tex:101 | ok |
| topographic analysis | medical | 02-background.tex:782 | never | missing |
| choroid / choroidal layers | medical | 02-background.tex:783 | 02-background.tex:73 | ok |
| macular atrophy | medical | 02-background.tex:784 | 01-introduction.tex:19 | ok |
| neovascularisation | medical | 02-background.tex:784 | 01-introduction.tex:18 | ok |
| growth rate of GA (per eye) | medical | 02-background.tex:788 | 01-introduction.tex:46 | ok |
| squared correlation (r^2) | math | 02-background.tex:790 | 05-experiments.tex:2132 | late |
| holdout set | ml | 02-background.tex:791 | never | missing |
| FAF (fundus autofluorescence) | imaging | 02-background.tex:792 | 02-background.tex:200 | ok |
| occlusion experiments | ml | 02-background.tex:792 | never | missing |
| lesion border / lesion front | medical | 02-background.tex:804 | 02-background.tex:804 | ok |
| lateral spread of GA (micrometres per year) | medical | 02-background.tex:804 | 02-background.tex:804 | ok |
| regular / irregular / splitting borders | medical | 02-background.tex:805 | never | missing |
| RORA | medical | 02-background.tex:809 | never | missing |
| en-face map | imaging | 02-background.tex:810 | 01-introduction.tex:94 | ok |
| mean reflectivity | imaging | 02-background.tex:810 | 02-background.tex:164 | ok |
| en-face pixel | imaging | 02-background.tex:811 | 02-background.tex:257 | ok |
| Dice score | ml | 02-background.tex:813 | 05-experiments.tex:50 | late |
| growth region | project | 02-background.tex:814 | 05-experiments.tex:107 | late |
| feature vector | ml | 02-background.tex:815 | never | missing |
| MRI | imaging | 02-background.tex:819 | never | missing |
| Alzheimer's disease | medical | 02-background.tex:819 | never | missing |
| Runge-Kutta wrapper (Runge-Kutta-integrated operators of this thesis) | project | 02-background.tex:819 | 04-method.tex:1115 | late |
| MUW (Medical University of Vienna) GA cohort | project | 02-background.tex:827 | 03-data.tex:27 | late |
| registration (registration bounds) | imaging | 02-background.tex:829 | 03-data.tex:72 | late |
| dense convolutional architecture | ml | 02-background.tex:833 | 04-method.tex:837 | late |
| RNN | ml | 02-background.tex:843 | never | missing |
| hidden state | ml | 02-background.tex:843 | never | missing |
| latent representation | ml | 02-background.tex:846 | never | missing |
| flow field | math | 02-background.tex:846 | never | missing |
| SDE | math | 02-background.tex:847 | never | missing |
| multiple sclerosis | medical | 02-background.tex:848 | never | missing |
| glioblastoma | medical | 02-background.tex:849 | 02-background.tex:849 | ok |
| 4D-DANI-Net | ml | 02-background.tex:851 | never | missing |
| neurodegeneration | medical | 02-background.tex:852 | never | missing |
| dementia | medical | 02-background.tex:852 | never | missing |
| BrLP | ml | 02-background.tex:852 | never | missing |
| latent diffusion model | ml | 02-background.tex:853 | never | missing |
| conditioning on time (condition on Delta t) | ml | 02-background.tex:855 | never | missing |
| Fisher-Kolmogorov equation | math | 02-background.tex:864 | never | missing |
| Bayesian inference | math | 02-background.tex:865 | never | missing |
| FET-PET | imaging | 02-background.tex:865 | never | missing |
| radiotherapy | medical | 02-background.tex:865 | never | missing |
| inverse problem | math | 02-background.tex:869 | never | missing |
| prognostic biomarkers | medical | 02-background.tex:905 | 01-introduction.tex:76 | ok |
| RPE (retinal pigment epithelium) | medical | 02-background.tex:906 | 02-background.tex:110 | ok |
| RPE-Bruch's-membrane thickening | medical | 02-background.tex:906 | 02-background.tex:364 | ok |
| outer retinal layers (thinning) | medical | 02-background.tex:907 | 02-background.tex:113 | ok |
| square-root enlargement rate | medical | 02-background.tex:926 | 02-background.tex:926 | ok |
| r_0 and v in Eq. (intro:boundary-growth) | math | 02-background.tex:934 | never | missing |
| anisotropic growth (faster towards the periphery) | medical | 02-background.tex:947 | 02-background.tex:947 | ok |
| retinal periphery | medical | 02-background.tex:948 | 02-background.tex:81 | ok |
| transport (explicit transport term) | math | 02-background.tex:989 | 04-method.tex:990 | late |
| anisotropic grid / lattice (~21:1 spacing) | imaging | 02-background.tex:999 | 02-background.tex:424 | ok |
| grid spacing (between B-scans / A-scans) | imaging | 02-background.tex:1000 | 02-background.tex:423 | ok |
| B-scan / A-scan | imaging | 02-background.tex:1001 | 02-background.tex:165 | ok |
| depth maps (channels 1-10) | imaging | 02-background.tex:1027 | 02-background.tex:268 | ok |
| h_y = 121.18 um, h_x = 5.68 um | imaging | 02-background.tex:1029 | 02-background.tex:1029 | ok |
| f_theta | project | 02-background.tex:1037 | 02-background.tex:1040 | late |
| function spaces | math | 02-background.tex:1045 | never | missing |
| training eyes | project | 02-background.tex:1056 | 03-data.tex:441 | late |
| objective (training loss) | ml | 02-background.tex:1064 | 04-method.tex:290 | late |
| MUW (Medical University of Vienna) | project | 03-data.tex:8 | 03-data.tex:27 | late |
| modelling grid (49 x 1024 window) | project | 03-data.tex:13 | 03-data.tex:239 | late |
| transition window | project | 03-data.tex:16 | 03-data.tex:348 | late |
| patient-level cross-validation | ml | 03-data.tex:18 | 03-data.tex:441 | late |
| registration | imaging | 03-data.tex:29 | 03-data.tex:72 | late |
| Heidelberg Engineering / Spectralis device | imaging | 03-data.tex:40 | never | missing |
| ART mode (volume scan protocol) | imaging | 03-data.tex:41 | never | missing |
| depth map (value = axial index of a boundary along an A-scan) | imaging | 03-data.tex:55 | 03-data.tex:198 | late |
| axial pixel | imaging | 03-data.tex:56 | 03-data.tex:200 | late |
| 16-bit integer / floating point | other | 03-data.tex:56 | never | missing |
| SLO (scanning laser ophthalmoscopy) | imaging | 03-data.tex:57 | 03-data.tex:57 | ok |
| SLO reference frame / coordinate transforms | imaging | 03-data.tex:59 | never | missing |
| certified graders of the Vienna Reading Center | medical | 03-data.tex:69 | never | missing |
| near-infrared image | imaging | 03-data.tex:72 | 02-background.tex:198 | ok |
| pixel spacing | imaging | 03-data.tex:84 | 03-data.tex:86 | ok |
| resampling / interpolation artefacts | imaging | 03-data.tex:86 | never | missing |
| square-root-area growth rate | medical | 03-data.tex:95 | 03-data.tex:95 | ok |
| interquartile range | math | 03-data.tex:99 | never | missing |
| 90th percentile | math | 03-data.tex:99 | never | missing |
| baseline lesion area | medical | 03-data.tex:100 | 03-data.tex:100 | ok |
| physical aspect ratio | imaging | 03-data.tex:142 | 03-data.tex:142 | ok |
| foveal pit | medical | 03-data.tex:150 | 02-background.tex:92 | ok |
| loss of the outer retina in GA | medical | 03-data.tex:151 | 02-background.tex:313 | ok |
| auxiliary prediction targets | ml | 03-data.tex:168 | 04-method.tex:307 | late |
| Iowa Reference Algorithms | imaging | 03-data.tex:169 | 03-data.tex:169 | ok |
| ILM (abbreviation) | medical | 03-data.tex:173 | 03-data.tex:173 | ok |
| ganglion cell layer | medical | 03-data.tex:174 | 02-background.tex:107 | ok |
| inner plexiform layer | medical | 03-data.tex:175 | 02-background.tex:107 | ok |
| Henle's fibre layer | medical | 03-data.tex:177 | never | missing |
| junction of the photoreceptor inner and outer segments | medical | 03-data.tex:177 | 02-background.tex:354 | ok |
| outer photoreceptor layer | medical | 03-data.tex:179 | never | missing |
| nominal depth of the scan volume | imaging | 03-data.tex:204 | 03-data.tex:204 | ok |
| retinal thickness | medical | 03-data.tex:209 | 03-data.tex:209 | ok |
| prognostic biomarker | medical | 03-data.tex:215 | 01-introduction.tex:76 | ok |
| rim around the GA boundary | medical | 03-data.tex:217 | 02-background.tex:365 | ok |
| correlation coefficient r | math | 03-data.tex:220 | 05-experiments.tex:2047 | late |
| RPE-photoreceptor complex | medical | 03-data.tex:222 | never | missing |
| macular-atrophy conversion | medical | 03-data.tex:223 | 01-introduction.tex:19 | ok |
| Spearman r | math | 03-data.tex:225 | never | missing |
| outer-retinal-layer thickness | medical | 03-data.tex:227 | 02-background.tex:907 | ok |
| centre crop | imaging | 03-data.tex:241 | 03-data.tex:241 | ok |
| zero-pad | imaging | 03-data.tex:242 | 03-data.tex:242 | ok |
| 6 x 6 mm fovea-centred window | imaging | 03-data.tex:259 | 02-background.tex:56 | ok |
| raster | imaging | 03-data.tex:262 | never | missing |
| swept-source OCT | imaging | 03-data.tex:263 | never | missing |
| A-line | imaging | 03-data.tex:264 | never | missing |
| edge of the imaged field (border contact) | imaging | 03-data.tex:298 | 03-data.tex:298 | ok |
| change-region metrics | project | 03-data.tex:301 | 05-experiments.tex:76 | late |
| one-year anchor | project | 03-data.tex:302 | 03-data.tex:429 | late |
| field of view | imaging | 03-data.tex:304 | never | missing |
| validation (visits, sets, results) | ml | 03-data.tex:325 | 03-data.tex:442 | late |
| imputation | math | 03-data.tex:355 | never | missing |
| run (reported run) | ml | 03-data.tex:359 | never | missing |
| precomputed dataset | ml | 03-data.tex:374 | 04-method.tex:1252 | late |
| day in study | project | 03-data.tex:380 | never | missing |
| time budget | ml | 03-data.tex:414 | 04-method.tex:384 | late |
| training curriculum | ml | 03-data.tex:421 | 04-method.tex:374 | late |
| concordance between fellow eyes | medical | 03-data.tex:448 | 01-introduction.tex:43 | ok |
| arm (of the comparison) | project | 03-data.tex:454 | 04-method.tex:26 | late |
| 49 x 1024 grid | imaging | 04-method.tex:30 | 03-data.tex:240 | ok |
| optimiser | ml | 04-method.tex:33 | 04-method.tex:426 | late |
| epoch / epoch budget | ml | 04-method.tex:33 | 04-method.tex:432 | late |
| random seed | ml | 04-method.tex:34 | never | missing |
| evaluation (shared evaluation protocol) | project | 04-method.tex:34 | 05-experiments.tex:34 | late |
| model selection rule | project | 04-method.tex:34 | 05-experiments.tex:191 | late |
| conditioning inputs | project | 04-method.tex:36 | 04-method.tex:237 | late |
| batch / batch format | ml | 04-method.tex:37 | 04-method.tex:220 | late |
| intersection over union | ml | 04-method.tex:47 | never | missing |
| neighbourhood graph | project | 04-method.tex:52 | 04-method.tex:718 | late |
| ablation | ml | 04-method.tex:57 | never | missing |
| moving-mesh extension | project | 04-method.tex:78 | 91-appendix.tex:608 | late |
| bounded (f_theta stays bounded) | math | 04-method.tex:159 | never | missing |
| norm \|\|.\|\| | math | 04-method.tex:165 | never | missing |
| linear layers / Lipschitz-continuous activations | ml | 04-method.tex:171 | never | missing |
| normalisation layers with a positive stabilising constant | ml | 04-method.tex:172 | never | missing |
| output scaling with 1/Delta t on the mask channel | project | 04-method.tex:175 | 05-experiments.tex:1095 | late |
| atrophic tissue does not regenerate | medical | 04-method.tex:186 | 01-introduction.tex:22 | ok |
| reference segmentations | medical | 04-method.tex:189 | 03-data.tex:64 | ok |
| local shrinkage of the reference segmentations | medical | 04-method.tex:190 | 04-method.tex:190 | ok |
| output head (final layer) | ml | 04-method.tex:194 | never | missing |
| row-major ordering | other | 04-method.tex:219 | never | missing |
| operators that work on the image grid (dense operators) | ml | 04-method.tex:222 | 04-method.tex:834 | late |
| soft-Dice term | ml | 04-method.tex:295 | 04-method.tex:312 | late |
| L, w_c, w-bar, c, L_MSE^(c), lambda_Dice, L_Dice (loss symbols) | math | 04-method.tex:297 | 04-method.tex:302 | late |
| gradient | ml | 04-method.tex:316 | never | missing |
| segmentation probability map | ml | 04-method.tex:320 | never | missing |
| regression output | ml | 04-method.tex:320 | never | missing |
| sigma (logistic sigmoid) | math | 04-method.tex:323 | 04-method.tex:326 | late |
| s (sharpness) | math | 04-method.tex:323 | 04-method.tex:326 | late |
| tau (threshold in normalised space) | math | 04-method.tex:323 | 04-method.tex:326 | late |
| saturation of the sigmoid | ml | 04-method.tex:341 | never | missing |
| raw error / raw mask predictions | project | 04-method.tex:342 | 05-experiments.tex:56 | late |
| multiscale local detail | ml | 04-method.tex:487 | never | missing |
| batch statistics | ml | 04-method.tex:510 | 04-method.tex:514 | late |
| training mode | ml | 04-method.tex:512 | never | missing |
| cut-off radius | ml | 04-method.tex:547 | never | missing |
| latent space | ml | 04-method.tex:553 | never | missing |
| theta_PDE (equation feature vector) | math | 04-method.tex:554 | 04-method.tex:569 | late |
| m (message-passing round index) | math | 04-method.tex:560 | 04-method.tex:624 | late |
| skip connection | ml | 04-method.tex:563 | 04-method.tex:643 | late |
| normalisation layer | ml | 04-method.tex:564 | never | missing |
| translational symmetry | math | 04-method.tex:565 | never | missing |
| convolution | ml | 04-method.tex:576 | never | missing |
| width | ml | 04-method.tex:586 | 04-method.tex:647 | late |
| linear layer | ml | 04-method.tex:620 | never | missing |
| layer normalisation | ml | 04-method.tex:620 | 04-method.tex:650 | late |
| ReLU | ml | 04-method.tex:620 | never | missing |
| activation function | ml | 04-method.tex:621 | never | missing |
| Delta p_ij | math | 04-method.tex:628 | 04-method.tex:635 | late |
| LN | ml | 04-method.tex:630 | 04-method.tex:637 | late |
| N(i) (neighbour set) | math | 04-method.tex:631 | 04-method.tex:636 | late |
| M (index of the final round in f_i^M) | math | 04-method.tex:658 | never | missing |
| smoke-inflow experiments | other | 04-method.tex:673 | never | missing |
| wave equations | math | 04-method.tex:702 | never | missing |
| index-space k-nearest-neighbour graph | project | 04-method.tex:703 | 04-method.tex:743 | late |
| Swish | ml | 04-method.tex:706 | never | missing |
| instance normalisation | ml | 04-method.tex:707 | never | missing |
| anisotropic grid (21:1) | imaging | 04-method.tex:718 | 02-background.tex:424 | ok |
| Euclidean distance | math | 04-method.tex:732 | never | missing |
| self-loops | ml | 04-method.tex:746 | never | missing |
| interior node | math | 04-method.tex:746 | 04-method.tex:754 | late |
| directed edges | ml | 04-method.tex:752 | never | missing |
| GA front | medical | 04-method.tex:766 | 02-background.tex:953 | ok |
| kernel taps | ml | 04-method.tex:781 | never | missing |
| receptive field | ml | 04-method.tex:782 | never | missing |
| feature space | ml | 04-method.tex:786 | never | missing |
| biomedical image segmentation | imaging | 04-method.tex:842 | never | missing |
| max pooling | ml | 04-method.tex:845 | never | missing |
| feature channels | ml | 04-method.tex:845 | never | missing |
| downsampling and upsampling | ml | 04-method.tex:846 | never | missing |
| output classes | ml | 04-method.tex:849 | never | missing |
| fundus autofluorescence | imaging | 04-method.tex:854 | 02-background.tex:200 | ok |
| control | project | 04-method.tex:868 | 04-method.tex:1191 | late |
| GELU | ml | 04-method.tex:893 | never | missing |
| zero-padding | imaging | 04-method.tex:899 | 03-data.tex:242 | ok |
| over-smoothing | ml | 04-method.tex:912 | never | missing |
| discrete-continuous convolutions | ml | 04-method.tex:917 | never | missing |
| one ring of neighbours | ml | 04-method.tex:924 | never | missing |
| locality floors | project | 04-method.tex:928 | 04-method.tex:959 | late |
| Galerkin method | math | 04-method.tex:981 | never | missing |
| Delaunay triangulation | math | 04-method.tex:982 | never | missing |
| conservative form | math | 04-method.tex:991 | never | missing |
| nabla (gradient / divergence) | math | 04-method.tex:991 | never | missing |
| divergence-free velocity | math | 04-method.tex:992 | never | missing |
| tanh | ml | 04-method.tex:995 | never | missing |
| assembled operator | math | 04-method.tex:1003 | never | missing |
| energy-conserving form | project | 04-method.tex:1033 | 04-method.tex:1057 | late |
| sub-step (integration) | math | 04-method.tex:1037 | 04-method.tex:1131 | late |
| purely imaginary spectrum | math | 04-method.tex:1041 | never | missing |
| stability interval on the imaginary axis | math | 04-method.tex:1043 | never | missing |
| flux term | math | 04-method.tex:1054 | never | missing |
| skew-adjoint | math | 04-method.tex:1058 | 04-method.tex:1061 | late |
| free-running rollout | project | 04-method.tex:1090 | 05-experiments.tex:176 | late |
| free-form FEN control | project | 04-method.tex:1103 | 04-method.tex:1194 | late |
| convergence order | math | 04-method.tex:1138 | never | missing |
| lambda (test-problem constant) | math | 04-method.tex:1139 | never | missing |
| midpoint and Heun schemes | math | 04-method.tex:1140 | never | missing |
| discretisation error | math | 04-method.tex:1167 | never | missing |
| CUDA | other | 04-method.tex:1242 | never | missing |
| GPU | other | 04-method.tex:1248 | never | missing |
| data loader | other | 04-method.tex:1261 | never | missing |
| NumPy | other | 04-method.tex:1264 | never | missing |
| deterministic cuDNN algorithms | other | 04-method.tex:1265 | never | missing |
| noise level | project | 04-method.tex:1268 | 05-experiments.tex:249 | late |
| lesion mask | imaging | 05-experiments.tex:44 | 03-data.tex:165 | ok |
| full-mask Dice | imaging | 05-experiments.tex:53 | 05-experiments.tex:52 | ok |
| clinical metrics | project | 05-experiments.tex:58 | 05-experiments.tex:76 | late |
| threshold (binarisation threshold) | imaging | 05-experiments.tex:59 | 03-data.tex:339 | ok |
| i (pixel index in the change-region sets) | math | 05-experiments.tex:89 | never | missing |
| \|.\| (set cardinality) | math | 05-experiments.tex:93 | never | missing |
| shrinkage | medical | 05-experiments.tex:101 | 04-method.tex:186 | ok |
| new atrophy | medical | 05-experiments.tex:107 | 05-experiments.tex:107 | ok |
| eye counts | project | 05-experiments.tex:111 | 05-experiments.tex:308 | late |
| censored growth | imaging | 05-experiments.tex:147 | 03-data.tex:300 | ok |
| edge of the imaged field | imaging | 05-experiments.tex:147 | 03-data.tex:298 | ok |
| padded visits / zero padding | imaging | 05-experiments.tex:152 | 03-data.tex:242 | ok |
| eye-level growth-rate measures | project | 05-experiments.tex:162 | 05-experiments.tex:2040 | late |
| selection bias | ml | 05-experiments.tex:208 | 05-experiments.tex:217 | late |
| standard normal distribution | math | 05-experiments.tex:297 | never | missing |
| two-sided p < 0.05 | math | 05-experiments.tex:300 | never | missing |
| paired t | math | 05-experiments.tex:305 | 91-appendix.tex:236 | late |
| standard errors and test statistics | math | 05-experiments.tex:318 | never | missing |
| k = 20 arm | project | 05-experiments.tex:381 | 05-experiments.tex:733 | late |
| smoothed lesion edges (display) | imaging | 05-experiments.tex:430 | 05-experiments.tex:430 | ok |
| stable (T-FEN rollout) | project | 05-experiments.tex:453 | 05-experiments.tex:1795 | late |
| profile (over horizon bins) | project | 05-experiments.tex:536 | 05-experiments.tex:583 | late |
| lesion front advance | medical | 05-experiments.tex:568 | 04-method.tex:766 | ok |
| pixel | imaging | 05-experiments.tex:642 | 02-background.tex:257 | ok |
| row / column (of the modelling grid) | imaging | 05-experiments.tex:652 | 03-data.tex:240 | ok |
| standard error | math | 05-experiments.tex:700 | never | missing |
| front advance (per-visit, 90th percentile) | medical | 05-experiments.tex:749 | 04-method.tex:766 | ok |
| unstable (numerical stability of a run) | math | 05-experiments.tex:827 | 05-experiments.tex:1795 | late |
| GA front / lesion front | medical | 05-experiments.tex:864 | 02-background.tex:953 | ok |
| five main operators | project | 05-experiments.tex:948 | 05-experiments.tex:983 | late |
| growth rate in square-root area | medical | 05-experiments.tex:958 | 03-data.tex:95 | ok |
| Spearman rho | math | 05-experiments.tex:961 | never | missing |
| window edge (lesion touching the edge of the window) | imaging | 05-experiments.tex:1028 | 05-experiments.tex:150 | ok |
| window (49 x 1024 modelling window) | imaging | 05-experiments.tex:1028 | 03-data.tex:249 | ok |
| relative growth | medical | 05-experiments.tex:1039 | 05-experiments.tex:1039 | ok |
| general tendency to predict too little change | project | 05-experiments.tex:1045 | 06-discussion.tex:273 | late |
| normalised units (mask values -0.602 and +1.660) | imaging | 05-experiments.tex:1115 | 03-data.tex:338 | ok |
| training time (cost convention) | project | 05-experiments.tex:1136 | 05-experiments.tex:2165 | late |
| layer channel | imaging | 05-experiments.tex:1170 | 02-background.tex:1027 | ok |
| atrophic tissue | medical | 05-experiments.tex:1270 | 02-background.tex:313 | ok |
| capacity | ml | 05-experiments.tex:1344 | 05-experiments.tex:1347 | late |
| divergence in training | ml | 05-experiments.tex:1374 | never | missing |
| training error | ml | 05-experiments.tex:1442 | never | missing |
| stability criterion (stable / unstable run) | project | 05-experiments.tex:1541 | 05-experiments.tex:1795 | late |
| checkpoint | ml | 05-experiments.tex:1588 | never | missing |
| mode (of the transport operator) | math | 05-experiments.tex:1654 | never | missing |
| crop (49 × 1024 window) | imaging | 05-experiments.tex:1810 | 03-data.tex:241 | ok |
| geometric mean (with sd of the log error) | math | 05-experiments.tex:1868 | never | missing |
| baseline (visit) | medical | 05-experiments.tex:1954 | 05-experiments.tex:84 | ok |
| growth speed | medical | 05-experiments.tex:1960 | 03-data.tex:95 | ok |
| raw OCT volume | imaging | 05-experiments.tex:1967 | 02-background.tex:185 | ok |
| segmented masks and layer depths (model input) | imaging | 05-experiments.tex:1968 | 03-data.tex:53 | ok |
| growth rate (square-root area per year) | medical | 05-experiments.tex:1974 | 03-data.tex:95 | ok |
| en-face maps | imaging | 05-experiments.tex:1984 | 01-introduction.tex:94 | ok |
| reflectivity | imaging | 05-experiments.tex:1985 | 02-background.tex:164 | ok |
| region of growth (Salvi et al.) | medical | 05-experiments.tex:1990 | 05-experiments.tex:107 | ok |
| fundus autofluorescence (FAF) | imaging | 05-experiments.tex:1990 | 02-background.tex:200 | ok |
| square-root transform | math | 05-experiments.tex:2040 | 05-experiments.tex:2043 | late |
| fast progressor | medical | 05-experiments.tex:2051 | 05-experiments.tex:2053 | ok |
| bootstrap (95 % interval) | math | 05-experiments.tex:2058 | never | missing |
| identity line | math | 05-experiments.tex:2124 | never | missing |
| annual slope of the lesion area | medical | 05-experiments.tex:2134 | 05-experiments.tex:2134 | ok |
| inference time per rollout step | ml | 05-experiments.tex:2174 | never | missing |
| memory footprint | ml | 05-experiments.tex:2174 | never | missing |
| lesion mask (channel 0) | imaging | 06-discussion.tex:23 | 02-background.tex:268 | ok |
| retinal layer boundaries (channels 1-10) | imaging | 06-discussion.tex:23 | 02-background.tex:268 | ok |
| grid rows and columns (anisotropic lattice) | imaging | 06-discussion.tex:96 | 02-background.tex:1028 | ok |
| growth rate / growth speed | medical | 06-discussion.tex:194 | 03-data.tex:95 | ok |
| focality | medical | 06-discussion.tex:197 | never | missing |
| moving-mesh extension / mesh adaptation | project | 06-discussion.tex:230 | 06-discussion.tex:401 | late |
| correction branch | project | 06-discussion.tex:230 | 91-appendix.tex:878 | late |
| engaged (gate opens) | project | 06-discussion.tex:231 | 91-appendix.tex:885 | late |
| crop (fixed 49 x 1024 window) | imaging | 06-discussion.tex:265 | 03-data.tex:241 | ok |
| deterministic model | ml | 06-discussion.tex:277 | never | missing |
| pixel-wise loss | ml | 06-discussion.tex:277 | never | missing |
| image intensity | imaging | 06-discussion.tex:279 | never | missing |
| reflectivity maps | imaging | 06-discussion.tex:280 | 02-background.tex:145 | ok |
| atrophy / atrophic | medical | 06-discussion.tex:303 | 01-introduction.tex:22 | ok |
| segmentation / segmented masks | imaging | 06-discussion.tex:330 | 03-data.tex:68 | ok |
| fast progressors | medical | 06-discussion.tex:337 | 05-experiments.tex:2053 | ok |
| fellow eyes | medical | 06-discussion.tex:351 | 06-discussion.tex:350 | ok |
| transform files | imaging | 06-discussion.tex:362 | 03-data.tex:59 | ok |
| DICOM | imaging | 06-discussion.tex:363 | never | missing |
| GA reference annotated on FAF | imaging | 06-discussion.tex:363 | 03-data.tex:68 | ok |
| regression of the atrophy | medical | 06-discussion.tex:371 | never | missing |
| physics-informed neural networks | ml | 06-discussion.tex:397 | never | missing |
| equation residual | math | 06-discussion.tex:399 | never | missing |
| padded positions | imaging | 06-discussion.tex:418 | 03-data.tex:242 | ok |
| whole-field studies | imaging | 06-discussion.tex:420 | never | missing |
| multi-scale graph (edges at several scales, pyramid of coarsened graphs) | ml | 06-discussion.tex:439 | never | missing |
| recurrent networks / recurrent state | ml | 06-discussion.tex:445 | never | missing |
| sequence models / transformers | ml | 06-discussion.tex:448 | never | missing |
| 21:1 grid anisotropy | imaging | 06-discussion.tex:455 | 02-background.tex:1001 | ok |
| end to end (learning from raw input) | ml | 06-discussion.tex:471 | never | missing |
| predictive uncertainty | ml | 06-discussion.tex:476 | never | missing |
| joint training across retinal diseases | ml | 06-discussion.tex:476 | never | missing |
| complement pathway | medical | references.bib:77 | 01-introduction.tex:56 | ok |
| retinal pigment epithelium | medical | references.bib:88 | 02-background.tex:110 | ok |
| Citation key (printed bibliography note) | other | references.bib:109 | never | missing |
| dry AMD | medical | references.bib:121 | never | missing |
| BMJ | other | references.bib:143 | never | missing |
| OCT angiography | imaging | references.bib:176 | never | missing |
| SIAM | other | references.bib:273 | never | missing |
| CBMS-NSF | other | references.bib:273 | never | missing |
| MATLAB | other | references.bib:284 | never | missing |
| JAMA | other | references.bib:472 | never | missing |
| Age-Related Eye Disease Study | medical | references.bib:472 | 01-introduction.tex:40 | ok |
| square root transformation of GA area | medical | references.bib:472 | 03-data.tex:95 | ok |
| ResNet | ml | references.bib:587 | never | missing |
| arXiv | other | references.bib:615 | never | missing |
| ECCV | other | references.bib:644 | never | missing |
| V-Net | ml | references.bib:687 | never | missing |
| pegcetacoplan / avacincaptad pegol | medical | references.bib:733 | 01-introduction.tex:54 | ok |
| marketing authorisation | medical | references.bib:733 | 01-introduction.tex:57 | ok |
| FAM (FAM-Study Group) | medical | references.bib:793 | never | missing |
| Bayesian inference / calibration | math | references.bib:856 | never | missing |
| ACM | other | references.bib:879 | never | missing |
| PINNs | ml | references.bib:879 | never | missing |
| IEEE | other | references.bib:916 | never | missing |
| fovea centralis | medical | references.bib:938 | 01-introduction.tex:24 | ok |
| CVF | other | references.bib:958 | never | missing |
| GCN / DeepGCNs | ml | references.bib:958 | never | missing |
| CNN | ml | references.bib:958 | never | missing |
| lesion scale (baseline lesion area) | medical | 91-appendix.tex:8 | 91-appendix.tex:15 | late |
| growth rate on the square-root area scale | medical | 91-appendix.tex:34 | 03-data.tex:95 | ok |
| constant pixel spacing | imaging | 91-appendix.tex:37 | 03-data.tex:86 | ok |
| native (en-face) grid | imaging | 91-appendix.tex:42 | 03-data.tex:81 | ok |
| follow-up visit | medical | 91-appendix.tex:105 | 03-data.tex:34 | ok |
| sigma_A, sigma_B | math | 91-appendix.tex:232 | never | missing |
| p-value / significance level | math | 91-appendix.tex:235 | never | missing |
| paired t statistic | math | 91-appendix.tex:241 | never | missing |
| SE | math | 91-appendix.tex:278 | never | missing |
| tie (reading) | project | 91-appendix.tex:300 | never | missing |
| diverged (training divergence) | ml | 91-appendix.tex:413 | never | missing |
| Dockerfile | other | 91-appendix.tex:544 | never | missing |
| mounted (fold mounted at the same path) | other | 91-appendix.tex:553 | never | missing |
| experiment-name codes (w96, ftp7, rk4d45, skew, dilmean, oderk4n1, w5k3, w5rk4, Frk4d45, aggrmean, k20, l1mean, pxmean; ANISOGNN, MPPDE prefixes) | project | 91-appendix.tex:573 | never | missing |
| moving mesh / moved mesh | math | 91-appendix.tex:594 | 91-appendix.tex:631 | late |
| mesh adaptation | math | 91-appendix.tex:609 | 91-appendix.tex:628 | late |
| uniform grid / uniform mesh | math | 91-appendix.tex:616 | 91-appendix.tex:624 | late |
| vertices | math | 91-appendix.tex:629 | never | missing |
| topology (mesh / graph topology) | math | 91-appendix.tex:629 | never | missing |
| degrees of freedom | math | 91-appendix.tex:629 | never | missing |
| alpha_M (monitor constant) | math | 91-appendix.tex:639 | 91-appendix.tex:642 | late |
| det (determinant) | math | 91-appendix.tex:644 | never | missing |
| coordinate map | math | 91-appendix.tex:647 | never | missing |
| convexity / convex | math | 91-appendix.tex:655 | never | missing |
| \|Omega\| (area of the domain) | math | 91-appendix.tex:659 | never | missing |
| Hessian of phi | math | 91-appendix.tex:659 | never | missing |
| Jacobian (non-singular) | math | 91-appendix.tex:663 | never | missing |
| fold (mesh folding) | math | 91-appendix.tex:663 | 91-appendix.tex:959 | late |
| query coordinate xi (unit-square computational coordinate) | math | 91-appendix.tex:673 | 91-appendix.tex:761 | late |
| beta, gamma (DMM loss weights) | math | 91-appendix.tex:676 | never | missing |
| Adam | ml | 91-appendix.tex:681 | never | missing |
| BFGS | math | 91-appendix.tex:681 | never | missing |
| residual-cut network | ml | 91-appendix.tex:700 | never | missing |
| lesion border | medical | 91-appendix.tex:734 | never | missing |
| single-branch model | project | 91-appendix.tex:740 | 91-appendix.tex:877 | late |
| native 49 x 1024 grid (modelling grid) | imaging | 91-appendix.tex:748 | 03-data.tex:249 | ok |
| stride-2 convolutions | ml | 91-appendix.tex:757 | never | missing |
| adaptive average pooling | ml | 91-appendix.tex:757 | never | missing |
| latent vector | ml | 91-appendix.tex:758 | never | missing |
| tanh (activation) | ml | 91-appendix.tex:760 | never | missing |
| base head | project | 91-appendix.tex:763 | never | missing |
| automatic differentiation | ml | 91-appendix.tex:764 | never | missing |
| g-bar (mean gradient magnitude) | math | 91-appendix.tex:772 | 91-appendix.tex:775 | late |
| alpha_scale | math | 91-appendix.tex:772 | 91-appendix.tex:776 | late |
| epsilon (monitor constant) | math | 91-appendix.tex:772 | 91-appendix.tex:777 | late |
| Gaussian blur | imaging | 91-appendix.tex:775 | 91-appendix.tex:783 | late |
| sigma (Gaussian blur width, px) | imaging | 91-appendix.tex:783 | 91-appendix.tex:783 | ok |
| M-bar (mean monitor) | math | 91-appendix.tex:795 | never | missing |
| normal derivative | math | 91-appendix.tex:798 | never | missing |
| checkpoint (selection) | ml | 91-appendix.tex:802 | never | missing |
| learning rate | ml | 91-appendix.tex:808 | never | missing |
| mesh quality | project | 91-appendix.tex:811 | 91-appendix.tex:955 | late |
| edge gain | project | 91-appendix.tex:815 | 91-appendix.tex:960 | late |
| g_theta (correction-branch update) | ml | 91-appendix.tex:873 | 91-appendix.tex:876 | late |
| optimiser group | ml | 91-appendix.tex:890 | never | missing |
| columns (grid columns) | imaging | 91-appendix.tex:902 | 04-method.tex:725 | ok |
| trainable parameters / parameter count | ml | 91-appendix.tex:934 | never | missing |
| signed area | math | 91-appendix.tex:959 | never | missing |
| physical aspect ratio of the 5.94 x 5.82 mm window | imaging | 91-appendix.tex:1031 | 03-data.tex:142 | ok |
| quartile (lower / upper quartile, median) | math | 91-appendix.tex:1036 | never | missing |
| zero-padded row | imaging | 91-appendix.tex:1042 | 03-data.tex:242 | ok |
| GA front advance (columns between visits) | medical | 91-appendix.tex:1139 | 04-method.tex:766 | ok |
| surrogate of the next state (monitor input) | ml | 91-appendix.tex:1159 | never | missing |

## 6. Terminology

| Concept | Names used | Where | Proposed |
|---|---|---|---|

## 7. Format conventions

The conventions the thesis follows in most places (or that the rules require), and how often a chapter departs from them. Each group of deviations is one finding in 01-findings.md.

| Aspect | Convention | Deviations | Where |
|---|---|---|---|
| Chapter openings | A paragraph before the first \section that states the chapter's purpose and lists its sections (Ch. 2, 3, 5; App. A, E). Ch. 1 carries its map in §1.4, which is acceptable. | 3 | 04-method.tex:16; 06-discussion.tex:4; 91-appendix.tex:117 |
| Chapter closings | A closing paragraph that hands over to the next chapter (Ch. 1 outline, Ch. 4 last paragraph, Ch. 5 Summary) | 3 | 02-background.tex:1066; 03-data.tex:489; 06-discussion.tex:477 |
| Section intros | An introductory paragraph before the first subsection, run-in heading or float | 4 | 02-background.tex:20; 06-discussion.tex:413; 91-appendix.tex:120; 91-appendix.tex:165 |
| Section conclusions (Chapter 5) | A concluding paragraph or summary subsection at the end of each results section (§5.2-§5.5, §5.8, §5.9) | 2 | 05-experiments.tex:1077; 05-experiments.tex:1533 |
| Heading capitalisation | Title Case for chapter, section and subsection headings | 4 | 02-background.tex:415; 02-background.tex:501; 02-background.tex:587; 03-data.tex:236 |
| Heading numbering and form | All numbered, plain topic headings, no question marks | 0 |  |
| Run-in \paragraph headings | Sentence case ending in a full stop (Ch. 1, 2, 4, §6.4, App. D) | 0 |  |
| Section references | \S\ref inside a sentence, Section~\ref at a sentence start | 10 | 01-introduction.tex:119; 02-background.tex:12; 03-data.tex:12; 03-data.tex:17; 02-background.tex:119; 02-background.tex:121; 02-background.tex:412; 02-background.tex:1005; 04-method.tex:67; 04-method… |
| Chapter/Appendix/Figure/Table references | Spelled out, capitalised, with a tie (Chapter~\ref, Appendix~\ref, Figure~\ref, Table~\ref); no 'Fig.', 'Tab.', 'Sec.' | 0 |  |
| Figure-panel references | Panel letter attached to the number ('Figure 4.2a') | 8 | 02-background.tex:91; 02-background.tex:111; 02-background.tex:171; 02-background.tex:184; 02-background.tex:186; 02-background.tex:260; 02-background.tex:312; 02-background.tex:639 |
| Equation references | Equation~\eqref → 'Equation (4.1)' | 13 | 02-background.tex:404; 02-background.tex:459; 02-background.tex:537; 02-background.tex:567; 02-background.tex:579; 02-background.tex:621; 02-background.tex:642; 02-background.tex:662; 02-background.t… |
| Tie before \S\ref | word~\S\ref (83 places) | 9 | 02-background.tex:466; 02-background.tex:504; 02-background.tex:1054; 02-background.tex:1061; 05-experiments.tex:28; 06-discussion.tex:447; 91-appendix.tex:276; 91-appendix.tex:281; 91-appendix.tex:6… |
| Citations | \citet for textual and \citep for parenthetical citations, placed before the punctuation; no plain-text author-year in printed text. The tie before \citet varies only in the source and has no printed… | 0 |  |
| Thousands separators | Thin space from five digits (67\,147); none for four digits (1080) | 3 | 01-introduction.tex:27; 04-method.tex:754; 05-experiments.tex:1889 |
| Decimal places of Dice in text | Three decimals in running text and excerpt tables; four only in Table 5.1 and the appendix tables | 8 | 05-experiments.tex:647; 05-experiments.tex:1109; 05-experiments.tex:1844; 91-appendix.tex:1080; 91-appendix.tex:1081; 91-appendix.tex:1110; 91-appendix.tex:1113; 91-appendix.tex:1117 |
| ± notation | Math-mode $a \pm b$, described as 'mean ± sd over the five folds' | 2 | 91-appendix.tex:278; 91-appendix.tex:283 |
| Percentages | Thin space before %, as in '39\,%' | 0 |  |
| Unit spacing | Thin space \, between number and unit | 5 | 05-experiments.tex:422; 05-experiments.tex:2167; 05-experiments.tex:2179; 05-experiments.tex:2218; 05-experiments.tex:2220 |
| Units for reach and front advance | Micrometres (\textmu{}m), with columns in brackets where given | 4 | 05-experiments.tex:992; 05-experiments.tex:993; 05-experiments.tex:1022; 91-appendix.tex:1139 |
| Factors | Words: 'about 4.8 times', 'about ten times' | 6 | 05-experiments.tex:2179; 05-experiments.tex:2219; 05-experiments.tex:2220; 05-experiments.tex:2221; 06-discussion.tex:212; 06-discussion.tex:455 |
| Ranges in running text | 'X to Y' with the unit once; en-dash only in table bins and label ranges | 3 | 01-introduction.tex:60; 02-background.tex:238; 03-data.tex:217 |
| Numerals vs words | Words for one to ten, numerals from 11 upwards (about 80 places); 'five-fold' | 16 | 01-introduction.tex:60; 02-background.tex:342; 02-background.tex:1019; 03-data.tex:34; 03-data.tex:488; 04-method.tex:120; 04-method.tex:524; 04-method.tex:734; 04-method.tex:818; 04-method.tex:839; … |
| Quotation marks | LaTeX ``...'' | 0 |  |
| Emphasis | \emph for new terms; \textbf only for list labels and table group headers | 3 | 02-background.tex:93; 02-background.tex:94; 03-data.tex:252 (author decision, under reconsider) |
| Caption panel labels | \emph{(a)}, \emph{Left:} | 12 | 04-method.tex:817; 04-method.tex:820; 04-method.tex:823; 04-method.tex:1084; 04-method.tex:1086; 05-experiments.tex:423; 05-experiments.tex:424; 05-experiments.tex:425; 05-experiments.tex:427; 91-app… |
| Lists | itemize/enumerate with full-sentence items, capital start, full stop; bold labels end in a full stop | 5 | 05-experiments.tex:1576; 05-experiments.tex:1578; 05-experiments.tex:1602; 05-experiments.tex:1604; 05-experiments.tex:1606 |
| Abbreviations | Defined once in parentheses at first main-text use, then always used | 35 | 02-background.tex:159 and the 34 places listed in its finding |
| Capitalisation of spelled-out names | As in the definition: 'Geographic Atrophy'; the generic arm as 'finite-element network' | 5 | 02-background.tex:222; 02-background.tex:292; 02-background.tex:313; 05-experiments.tex:1552; 07-conclusion.tex:50 |
| Acronym-list expansions | Title Case | 7 | acronyms.tex:8; acronyms.tex:9; acronyms.tex:16; acronyms.tex:17; acronyms.tex:18; acronyms.tex:24; acronyms.tex:28 |
| British spelling | -ise, -our, -re, modelling, labelled | 0 |  |
| Hyphenation of compounds | Hyphenated compound adjectives (change-region Dice, moving-mesh extension, sub-step), closed 'multiscale', 'multilayer', 'preprocessing' | 5 | 02-background.tex:721; acronyms.tex:16; 04-method.tex:581; 06-discussion.tex:416; 91-appendix.tex:952 |
| e.g./i.e. | 'that is,' in running text; i.e. only inside brackets | 1 | 02-background.tex:47 |
| Dashes | En-dash for ranges and names; brackets for asides | 1 | 06-discussion.tex:198 |
| Caption structure (printed title sentence, then details) | The printed caption opens with a title sentence (what is shown or found), then the details needed to read the float | 5 | 05-experiments.tex:260 (Fig. 5.1), 05-experiments.tex:973 (Fig. 5.4), 05-experiments.tex:1018 (Fig. 5.5), 05-experiments.tex:1258 (Fig. 5.6), 91-appendix.tex:1059 (Table E.3) |
| Caption self-containment (seed, columns, no 'see text') | Seed, folds and statistic stated in the caption; caption readable without the text | 6 | 05-experiments.tex:421, 05-experiments.tex:2064, 91-appendix.tex:102 (no seed); 91-appendix.tex:984 (columns undefined); 05-experiments.tex:2016, 05-experiments.tex:2070 ('see text') |
| Meaning of ± stated where used | 'mean ± sd over the five folds' / 'mean ± SE' / band = run-to-run sd stated in every caption that shows ± | 0 |  |
| Caption ending punctuation | Every caption and short caption ends with a full stop | 0 |  |
| Caption length and content | About 50-140 words of reading instructions; no repetition of body text; no results previewed outside Chapter 5 | 2 | 02-background.tex:41 (Fig. 2.1, 225 words, repeats the text); 04-method.tex:1089 (Fig. 4.3 previews §5.7.2) |
| Caption and label position | Figure captions below, table captions above, \label directly after \caption | 0 |  |
| Table rule style | booktabs (\toprule/\midrule/\bottomrule, \cmidrule), no vertical rules, no \hline | 0 |  |
| Table type size | \small | 5 | 03-data.tex:397, 03-data.tex:470 (normal size); 05-experiments.tex:1191, 05-experiments.tex:1377, 05-experiments.tex:2018 (\footnotesize in the main text) |
| Table width and column layout | Within the 135 mm text block; integers right-aligned, decimals centred, columns kept together | 4 | 05-experiments.tex:1732, 91-appendix.tex:462 (last column stretched by group rows); 91-appendix.tex:288, 91-appendix.tex:380 (overfull by 5.0 and 6.6 pt) |
| Numeral font in tables | One mode per table (text or math) for all numeric cells | 7 | 05-experiments.tex:363, 05-experiments.tex:710, 05-experiments.tex:1198, 05-experiments.tex:1384, 05-experiments.tex:1734, 91-appendix.tex:986, 91-appendix.tex:1069 |
| Decimal places | Three decimals for Dice means and sd; four only for paired differences in Appendix C | 3 | 05-experiments.tex:363-387 (Table 5.1), 91-appendix.tex:986 (Table E.2), 91-appendix.tex:1069 (Table E.3) |
| Units and header names in tables | Unit in the column header (s/epoch, years); 'Parameters', 'Folds', 'Eyes'; ratio 1.00 | 5 | 03-data.tex:399 (days in cells), 91-appendix.tex:1067 (s in cells), 05-experiments.tex:360 and 05-experiments.tex:1381 ('Params'), 05-experiments.tex:1385 ('Folds higher', ratio '1') |
| Marking of best values | None in any table (rows ordered instead) | 0 |  |
| Table notes | Note at the end of the caption with a dagger | 1 | 91-appendix.tex:413 (asterisk row under \bottomrule) |
| Group rows inside tables | Italic \multicolumn row | 2 | 91-appendix.tex:292 (Table C.3), 91-appendix.tex:336 (Table C.4) in bold |
| Arm labels in tables and legends | Table 5.1 forms ('Graph network, dilated stencil', 'FNO with 3 × 3 local path', 'U-Net, width 5', 'Graph network, k-NN, k = 12') | 13 | 04-method.tex:1221, 04-method.tex:1222, 04-method.tex:678, 05-experiments.tex:1384, 05-experiments.tex:1395, 05-experiments.tex:1732, 05-experiments.tex:2022, 05-experiments.tex:971, 91-appendix.tex:… |
| Same data in a figure and a table | Each set of numbers shown once (excerpt tables next to ablations allowed) | 2 | 05-experiments.tex:578 vs 05-experiments.tex:550 (Fig. 5.3 / Table 5.2); 91-appendix.tex:25 vs 03-data.tex:397 (Fig. A.1b / Table 3.1) |
| Figure text size | Made with fig_size(frac) and included at the same fraction; 7-8 pt Public Sans in print | 6 | 02-background.tex:138, 02-background.tex:290 (below 7 pt); 04-method.tex:1078, 05-experiments.tex:1864, 05-experiments.tex:1765, 05-experiments.tex:1015 (scaled up 1.07-1.16) |
| Figure font family | Public Sans in every figure | 1 | 04-method.tex:88 (TikZ in the serif body font) |
| Colours | One colour per arm from ARM (followed in every data figure); one colour and name per element | 2 | 02-background.tex:35 (OCT window orange vs blue in Figs 2.3, 3.1); 05-experiments.tex:419 vs 91-appendix.tex:100 (rollout legend names) |
| Panel labels in figures | (a), (b), ... printed in the figure and used in the caption | 3 | 02-background.tex:38 (Left/Right), 05-experiments.tex:975 (left/right), 02-background.tex:563 (1-6 in figure, (1)-(6) in caption) |
| Panel letters in captions | \emph{(a)} | 5 | 04-method.tex:817, 04-method.tex:1083, 05-experiments.tex:423, 91-appendix.tex:1037 (upright); 03-data.tex:132 (mixed) |
| Panel references in running text | Figure~\ref{...}(a) (Chapter 2, matching the captions) | 8 | 03-data.tex:151, 04-method.tex:733, 04-method.tex:745, 04-method.tex:777, 05-experiments.tex:788, 05-experiments.tex:867, 05-experiments.tex:871, 91-appendix.tex:903 |
| Figure and table cross-reference words | 'Figure~\ref', 'Table~\ref', no abbreviations | 0 |  |
| Equation references | 'Equation~\eqref{...}' (renders 'Equation (4.1)') | 13 | 02-background.tex:404, 459, 537, 621, 642, 662, 1048, 1063 (bare); 02-background.tex:567, 579 ('Eq.'); 04-method.tex:95, 04-method.tex:1085, 05-experiments.tex:1837 (\ref without parentheses) |
| Punctuation after displayed equations | Every display ends with a comma or full stop and the sentence continues | 0 |  |
| Equation numbering | Number only equations that are referred to later | 9 | 02-background.tex:435, 02-background.tex:547, 02-background.tex:935, 04-method.tex:300, 04-method.tex:618, 04-method.tex:629, 05-experiments.tex:91, 91-appendix.tex:773, 91-appendix.tex:874 |
| Notation consistent with §2.5.2 | \hat u_{k+1} = u_k + Δt_k f_θ(u_k, Δt_k, \mathbf{z}); one meaning per symbol | 7 | 04-method.tex:147, 06-discussion.tex:40, 91-appendix.tex:872 (update notation); 04-method.tex:330 (t), 04-method.tex:627 (m), 05-experiments.tex:85 / 04-method.tex:616 (y), 02-background.tex:485 (\ha… |
| Order of first reference | Floats numbered in the order they are first cited | 2 | 02-background.tex:111 (Fig. 2.4 before 2.2/2.3), 05-experiments.tex:1612 (Fig. 5.8 before 5.7) |
| Float placement | Float printed within its section, near its first reference; no near-empty pages | 3 | 05-experiments.tex:1909 (Table 5.7 in §5.8); 91-appendix.tex:272, 91-appendix.tex:427 (pp. 102 and 106 nearly empty) |
| Placeholder or disabled figures | None printed | 0 |  |

## 8. Repetition across chapters

Topics stated in full in more than one place, and where they should be stated in full (elsewhere a short pointer). Each is one finding in 01-findings.md.

| Topic | Stated at | State in full at |
|---|---|---|
| Continuous-time / Neural-ODE caution: a network trained with one discretisation need not be a conti… | 02-background.tex:734-742; 04-method.tex:199-205; 04-method.tex:977-979; 04-method.tex:1159-1173; 05-experiments.tex:1124-1126; 05-experiments.tex:1550-1565; 05-experiments.tex:1681-1684; 06-discussion.tex:204-208 | 05-experiments.tex:1550-1565 (§5.7.1); one-sentence mentions with a pointer in … |
| Galerkin versus energy-conserving T-FEN: both trained, Galerkin unstable after the anchor, main com… | 04-method.tex:1048-1056; 04-method.tex:1088-1093; 04-method.tex:1099-1101; 05-experiments.tex:354-355; 05-experiments.tex:450-454; 05-experiments.tex:546-547; 05-experiments.tex:825-830; 05-experiments.tex:1372-1374; 05-experiments.tex:1804-1827; 05-experiments.tex:1851-1853; 05-experiments.tex:189… | 05-experiments.tex:1804-1853 (§5.7.2); the method of the two forms in 04-method… |
| Shrinkage of the reference masks and why no monotonic-growth constraint is imposed | 04-method.tex:185-192; 05-experiments.tex:1270-1272; 05-experiments.tex:1288-1291; 06-discussion.tex:366-375 | 04-method.tex:185-192 (§4.2.1), with the quantification moved there from §6.3 |
| Chapter 7 restates §6.1 (framework answer, property bullets, deficit sentence, FNO local path, null… | 06-discussion.tex:36-68; 07-conclusion.tex:15-29; 06-discussion.tex:73-109; 07-conclusion.tex:31-61; 06-discussion.tex:162-171; 06-discussion.tex:223-236; 07-conclusion.tex:63-71; 07-conclusion.tex:86-88 | 06-discussion.tex:33-236 (§6.1); Chapter 7 only the short answers to the two su… |
| Reach argument: front advance per visit vs hop reach; two constructions remove the same limit | 02-background.tex:952-956; 02-background.tex:995-1003; 04-method.tex:757-774; 04-method.tex:826-830; 05-experiments.tex:651-655; 05-experiments.tex:747-757; 05-experiments.tex:899-918; 06-discussion.tex:95-109; 07-conclusion.tex:54-58; 91-appendix.tex:1134-1145 | numbers in 04-method.tex:757-774 (§4.3.3); interpretation in 06-discussion.tex:… |
| Horizon-bin results (first-year groups, FNO vs U-Net beyond one year, T-FEN vs stencil in later yea… | 05-experiments.tex:566-572; 05-experiments.tex:597-610; 05-experiments.tex:787-791; 05-experiments.tex:797-801; 05-experiments.tex:861-871; 06-discussion.tex:155-159 | 05-experiments.tex:530-610 (§5.3 with Table 5.2) |
| List of operator properties (spatial context, reach, global plus local, transport) | 02-background.tex:744-749; 02-background.tex:986-989; 04-method.tex:481-495; 04-method.tex:1206-1233; 05-experiments.tex:620-630 | 02-background.tex:744-749 (§2.3) |
| Definition of the one-year anchor, its missing upper bound and the justification by Mai et al. (202… | 03-data.tex:427-434; 05-experiments.tex:76-78; 05-experiments.tex:181-185; 06-discussion.tex:381-384 | 03-data.tex:427-434 (§3.6), with the definition at first use in §5.1.2 |
| Within §2.5.1: unknown governing equation (three times) and per-visit reach requirement (twice) | 02-background.tex:959; 02-background.tex:984; 02-background.tex:990; 02-background.tex:952-954; 02-background.tex:997-999 | 02-background.tex:959 (unknown equation); 02-background.tex:997-1003 (reach req… |
| Separation of model and framework / what the framework fixes | 01-introduction.tex:111-118; 02-background.tex:915-922; 02-background.tex:1061-1065; 04-method.tex:16-27 | 01-introduction.tex:111-118 (definition) and 04-method.tex:16-38 (§4.1, full) |
| Irregular visit intervals and no shared temporal origin | 02-background.tex:679-684; 02-background.tex:896-902; 02-background.tex:978-980; 04-method.tex:136-138 | 02-background.tex:896-902 (§2.5.1, first data property) |
| OCT appearance of the GA lesion (layer dropout, choroidal hypertransmission) | 02-background.tex:242-249; 02-background.tex:326-333; 02-background.tex:352-372 | 02-background.tex:326-372 (§2.1.3) |
| The 6 × 6 mm OCT window | 02-background.tex:55-57; 02-background.tex:84-87; 02-background.tex:152-153; 02-background.tex:187-189; 03-data.tex:249-265 | 03-data.tex:249-265 (§3.3) |
| Positioning against risk and conversion models (Vallino 2024 remark; risk score vs full spatial map) | 01-introduction.tex:76-80; 01-introduction.tex:100-104; 02-background.tex:784-786; 02-background.tex:794-798 | 01-introduction.tex:76-80 and 01-introduction.tex:100-104 (§1.1, §1.2) |
| Descriptions and values of prior studies (Yoshida 2025, Gigon 2021, Salvi 2025) | 02-background.tex:789-791; 02-background.tex:809-814; 02-background.tex:833-835; 04-method.tex:853-854; 05-experiments.tex:1984-1988; 05-experiments.tex:1990-1999; 05-experiments.tex:2129-2136 | descriptions in §2.4 (02-background.tex:775-835); values in §5.8 (05-experiment… |
| Relation of the thesis data to the Mai et al. (2024) cohort | 02-background.tex:825-830; 03-data.tex:26-30; 05-experiments.tex:1952-1956; 05-experiments.tex:1963-1966 | 03-data.tex:26-30 (§3.1) |
| Bilateral GA and concordance of fellow eyes | 01-introduction.tex:38-45; 03-data.tex:445-448 | 01-introduction.tex:38-45 (§1.1) |
| Padded zeros enter the normalisation statistics | 03-data.tex:272-274; 03-data.tex:325-327 | 03-data.tex:267-278 (§3.3) |
| Static pixels dominate the mean squared error, so a model can copy its input | 04-method.tex:314-317; 05-experiments.tex:43-48; 05-experiments.tex:1215-1218 | 04-method.tex:314-317 (§4.2.4) |
| Definition of the growth-region Dice and its use for the eye counts | 05-experiments.tex:105-112; 05-experiments.tex:138-145; 05-experiments.tex:309-310 | 05-experiments.tex:105-112 (§5.1.2, merged into one paragraph) |
| Square-root area transform removes the dependence of the growth rate on baseline size | 02-background.tex:925-927; 03-data.tex:95-97; 05-experiments.tex:2043-2044; 05-experiments.tex:2097-2098 | 03-data.tex:95-97 (§3.1) |
| Growth-speed result (r = 0.40 vs 0.52-0.61; shared by every operator) | 05-experiments.tex:2094-2108; 05-experiments.tex:2157-2158; 06-discussion.tex:242-252; 07-conclusion.tex:73-80 | 05-experiments.tex:2094-2108 (§5.8) |
| Covariates are graph-level and cannot localise anything | 04-method.tex:239-245; 04-method.tex:605-607; 06-discussion.tex:184-186; 06-discussion.tex:390-393 | 04-method.tex:239-245 (§4.2.3); §6.1.4 stays (SV-6.3) |
| Set-up of the step-size ladder (fixed step h, Euler/RK4, equal sub-steps, one and half a year leave… | 05-experiments.tex:1588-1599; 05-experiments.tex:1714-1724; 91-appendix.tex:431-439; 91-appendix.tex:443-453 | 05-experiments.tex:1588-1599 (§5.7.1) |

## 9. Build log

PDF built, complete, 127 pages, 0.8 min.

| Kind | Location | Page | Detail |
|---|---|---|---|
| undefined reference | acronyms.tex:8 | ix | Hyper reference `acro:AMD' undefined (2 warnings). The acronym list links each entry to a label acro:<key> that acronym.sty sets only at the first \ac{...} use; the text never uses \ac, so the link t… |
| undefined reference | acronyms.tex:9 | ix | Hyper reference `acro:DMM' undefined (2 warnings); acronym never used via \ac in the text, see the AMD entry. |
| undefined reference | acronyms.tex:10 | ix | Hyper reference `acro:FAF' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:11 | ix | Hyper reference `acro:FEN' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:12 | ix | Hyper reference `acro:FNO' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:13 | ix | Hyper reference `acro:GA' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:14 | ix | Hyper reference `acro:GNN' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:15 | ix | Hyper reference `acro:ItpNet' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:16 | ix | Hyper reference `acro:MLP' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:17 | ix | Hyper reference `acro:MM-PDE' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:18 | ix | Hyper reference `acro:MP-PDE' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:19 | ix | Hyper reference `acro:MSE' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:20 | ix | Hyper reference `acro:MUW' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:21 | ix | Hyper reference `acro:OCT' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:22 | ix | Hyper reference `acro:ODE' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:23 | ix | Hyper reference `acro:PDE' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:24 | ix | Hyper reference `acro:RK4' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:25 | ix | Hyper reference `acro:RMSE' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:26 | ix | Hyper reference `acro:RPE' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:27 | ix | Hyper reference `acro:SLO' undefined (2 warnings); acronym never used via \ac in the text. |
| undefined reference | acronyms.tex:28 | ix | Hyper reference `acro:T-FEN' undefined (2 warnings); acronym never used via \ac in the text. |
| overfull box | 91-appendix.tex:380 | 105 | Overfull \hbox (6.60455pt too wide) in paragraph at lines 380--415: the tabular of Table tab:appendix:seed42 ('Comparisons at seed 42 only', Appendix C) is 6.6 pt wider than the text block. The only … |

## 10. Feedback log check

reviews/feedback-log-2026-10-22.md: 707 items parsed; 552 done items checked: holds 511 · regressed 27 · no longer applies 14 · unclear 0.

| Log ID | Finding | Note |
|---|---|---|
| M2 | R-0103 | Most of the 16 glosses are still in place: AMD stages, drusen, macula, fovea, AREDS, complement cascade, best-corrected visual acuity, sham, injections into th… |
| X6 | R-0763 | Most of it still holds. 'ingredient' survives only in labels, and 'backbone' only inside the \iffalse block (05-experiments.tex:1465-1530), so neither is print… |
| SV-6.1 | R-1767 | The self-contained rewrite holds: task, data and measure are restated, the subsections are 6.1.1-6.1.6, and there is one answer to sub-question 1. The specific… |
| AI-S8 | R-1003 | The main text holds. §4.3.3 has no "turns out", §4.3.6 says only "Both forms were trained; Chapter 5 reports both ..., and the main comparison uses the energy-… |
| AI-S16 | R-1778 | The §2.5.1 fix holds: 02-background.tex:998-1002 states the 21:1 spacing and the lopsided neighbourhood. But the §6.1 passage the item named still frames reach… |
| AI-S19 | R-0764 | Most of the fix holds: 'arm' is defined in §4.1 (04-method.tex:28-29); 'canonical' is defined at 04-method.tex:56; 'ingredient' appears only in labels; 'induct… |
| AI-R13 | R-1723, R-1768 | The 'class does not decide / properties separate' antithesis is back, in the forms the supervisor objected to. 5.10 (05-experiments.tex:2243-2244) has 'What se… |
| AI-R14 | R-1143 | 5.1.5 says 'All numbers in this chapter are for the first seed' (05-experiments.tex:315-316), but second-seed statistics are back in Chapter 5: z = 0.8 at the … |
| AI-1.22 | R-0153 | The tablet-review v7 #4 edit of 2026-10-22 (e2ce11d) changed 'The output here is a complete map ... instead of a single risk score' to 'The forecast of this th… |
| AI-3.6 | R-0631 | The first part of the fix holds: 03-data.tex:65-66 'Although it is stored on the OCT grid, the GA mask was not segmented on the OCT.' The second part was undon… |
| AI-3.14 | R-0664 | The thickness paragraph (l. 209-212) still opens with what is not done and comes before the reason for keeping the layers (l. 214). The biomarker paragraph clo… |
| AI-3.22 | R-0710 | Half fixed: 'No validation data enters the statistics.' is gone. The suggested 'As noted in~\S\ref{sec:data:spatial}, ...' never entered the file (git history … |
| AI-4a.7 | R-0765 | The definition still holds at 04-method.tex:26-27 ("Each setting of the slot is referred to below as an \emph{arm} of the comparison"), and the canonical model… |
| AI-5a.36 | R-1176 | The terminology part holds: l. 467-469 says 'edge of the imaged field', which matches §5.1.2. The placement part has regressed. Since 2026-10-22 the three-high… |
| AI-5a.39 | R-1161 | 'Leaderboard' and the 'What it provides is' cleft are gone. But the awkward 'lie within the floor of each other' is still at 05-experiments.tex:446-448, with o… |
| AI-5b.1 | R-1232 | The opener (05-experiments.tex:620-634) now names the four tested properties and maps the subsections, without the repeated 0.04 and without 'what makes an ope… |
| AI-5c.27 | R-1534 | The recorded fix removed the SE notation but kept the phrase the item flagged. The text still reads '... lower the graph network on every fold, by 0.009 on ave… |
| AI-5d.29 | R-1657 | The replacement sentence written in the same 2026-10-19 commit (f71f1f6), 05-experiments.tex:1963, reads 'The values give an orientation, not a head-to-head re… |
| AI-5d.31 | R-1677 | The fix is present: 05-experiments.tex:1973-1975 states the growth-rate definition as a difference ('One difference remains: their paper computes the growth ra… |
| AI-6-7.5 | R-1750 | Partly holds: the two needed components are now named (06-discussion.tex:53-59: weighting of the mask channel and soft-Dice), and the paragraph has a topic sen… |
| AI-6-7.26 | R-1854 | The recorded change (new comparison values 0.52-0.61, AUCs against Mai) is in the text (06-discussion.tex:246-250), but it did not address the item. The senten… |
| AI-6-7.52 | R-1954 | The interpretation now follows the bullets directly, so that part holds. The aphoristic tag the item objected to is still printed, now as a clause after a semi… |
| AI-6-7.54 | R-1964 | The 2026-10-22 edit that added Gigon2021 and Yoshida2025 undid the resolved structure ('against 0.52 to 0.61 for comparable models, including the model of Mai2… |
| AI-G.25 | R-2241 | The resolved part still holds at 91-appendix.tex:811-813: 'Mesh quality (\S\ref{app:mm-pde:mesh-quality})' with its pointer, and 'settings with the largest eff… |
| AI-G.28 | R-2266 | 91-appendix.tex:888-889. The text now says 'whose outputs', so the attachment ambiguity of 'which' is gone. The unanchored 'otherwise' is still there: its sent… |
| AI-G.31 | R-2276 | 91-appendix.tex:927-932. 'Throttled' is gone, and the ItpNet numbers now have their own sentence. The pointer for 'the layer encoder', which the resolution add… |
| AI-G.33 | R-2286 | 91-appendix.tex:960-963. The first sentence holds ('The edge gain measures whether nodes move to the lesion border.'). The second sentence still hangs 'normali… |

Resolution could not be confirmed (unclear):


No longer applies (passage removed or rewritten): AI-4a.4, AI-4a.31, AI-4c.5, AI-4c.7, AI-5a.19, AI-5b.22, AI-5c.25, AI-5d.7, AI-6-7.10, AI-6-7.37, AI-G.19, AI-G.23, AI-G.35, AI-G.50.

Deferred items still open:

- M1: The abstract is the most important part: most readers (and reviewers) read only the abstract, so polish it to near perfection.
- SV-A1: Abstract structure: intro with problem, difficulty and top-3 contributions; methods with data, implementation and measurements; results and conclusions with numbers vs the naive baseline.
- SV-A2: "is a lesion of lost retinal tissue" -> "the advanced form of AMD ... manifested as a gradual and irreversible loss of retinal tissue".
- SV-A3: The difficulty of the forecast is the highly variable progression patterns and rates in the population, not irregular visits.
- SV-A4: "This thesis asks what such a forecast needs" -> more formal ("aims to study ... from the computational modelling perspective").
- SV-A5: "49 x 1024" is too much detail for the abstract.
- SV-A6: The paragraph openers "Together, ..." / "For the framework, ..." / "For the operator, ..." feel disconnected.
- AI-1.1: [medium] 'persistence' is not explained, 'and one loss' dangles at the end, and it is unclear whether 'measured in elapsed days' applies to the curriculum or the loss.
- AI-1.2: [medium] The 30-word subject list delays the verb to the end, and 'this slot' has no antecedent: the abstract never calls f_theta a slot.
- AI-1.3: [medium] The headline metric is not explained, and the next paragraph switches to the label 'change-region Dice' without linking the two.
- AI-1.4: [medium] The framework is personified ('served'), the sentence ends in a colon reveal, and 'added about 0.05' has no referent; placed first, this secondary finding comes before the headline result.
- AI-1.5: [low] 'lies above ... at two seeds' is lab jargon that an abstract reader may not decode.
- AI-1.6: [low] 'on its own' is filler, and the clipped second sentence ('The largest is physical reach.') reads as a reveal; unclear in what sense a property is 'the largest'.
- AI-1.7: [low] 'index-space neighbour graph' is not explained in the abstract, so the contrast with the dilated stencil is hard to grasp.
- AI-1.9: [low] The name changes from 'Fourier Neural Operators with and without a local path' to 'a purely spectral operator', and the tense switches from present to past within the sentence.
- AI-1.10: [medium] The sentence compares a rate with 'where the lesion changes', and the double 'with ... with' construction is clumsy.
- AI-1.11: [medium] The aphoristic closer combines a mirror pair ('how far ... how far') with an 'X, not Y' antithesis, making it the most slogan-like sentence of the abstract.

## 11. Decisions worth reconsidering

None.

## 12. Coverage

15 of 15 reviewed; whole-thesis passes 15 of 15; feedback log 707 parsed, 552 done items checked. 43 findings were dropped by verification; 2085 were kept although a verifier failed.

- U14: completeness round 1 failed
- verification lens text for U01 batch 1 (25 findings)
- verification lens rule for U01 batch 1 (25 findings)
- verification lens sceptic for U01 batch 1 (25 findings)
- U02: completeness round 1 failed
- U15: completeness round 1 failed
- verification lens text for U01 batch 2 (25 findings)
- verification lens rule for U01 batch 2 (25 findings)
- verification lens sceptic for U01 batch 2 (25 findings)
- verification lens text for U01 batch 3 (16 findings)
- verification lens rule for U01 batch 3 (16 findings)
- verification lens sceptic for U01 batch 3 (16 findings)
- U05: completeness round 1 failed
- U14: merge failed, duplicates may remain
- U02: merge failed, duplicates may remain
- U15: merge failed, duplicates may remain
- U05: merge failed, duplicates may remain
- verification lens text for U14 batch 1 (25 findings)
- verification lens rule for U14 batch 1 (25 findings)
- verification lens sceptic for U14 batch 1 (25 findings)
- verification lens text for U14 batch 2 (25 findings)
- verification lens rule for U14 batch 2 (25 findings)
- verification lens sceptic for U14 batch 2 (25 findings)
- verification lens text for U14 batch 3 (25 findings)
- verification lens rule for U14 batch 3 (25 findings)
- verification lens sceptic for U14 batch 3 (25 findings)
- verification lens rule for whole:mechanics batch 1 (8 findings)
- verification lens text for U14 batch 4 (25 findings)
- verification lens rule for U14 batch 4 (25 findings)
- verification lens sceptic for U14 batch 4 (25 findings)
- verification lens text for U14 batch 5 (25 findings)
- verification lens rule for U14 batch 5 (25 findings)
- verification lens sceptic for U14 batch 5 (25 findings)
- verification lens text for U14 batch 7 (25 findings)
- verification lens rule for U14 batch 7 (25 findings)
- verification lens sceptic for U14 batch 7 (25 findings)
- verification lens text for U14 batch 6 (25 findings)
- verification lens rule for U14 batch 6 (25 findings)
- verification lens sceptic for U14 batch 6 (25 findings)
- verification lens text for U14 batch 8 (14 findings)
- verification lens rule for U14 batch 8 (14 findings)
- verification lens sceptic for U14 batch 8 (14 findings)
- U03: completeness round 1 failed
- verification lens text for U02 batch 1 (25 findings)
- verification lens rule for U02 batch 1 (25 findings)
- verification lens sceptic for U02 batch 1 (25 findings)
- verification lens text for U02 batch 2 (25 findings)
- verification lens rule for U02 batch 2 (25 findings)
- verification lens sceptic for U02 batch 2 (25 findings)
- verification lens text for U02 batch 4 (24 findings)
- verification lens rule for U02 batch 4 (24 findings)
- verification lens sceptic for U02 batch 4 (24 findings)
- U04: completeness round 1 failed
- verification lens text for U15 batch 1 (25 findings)
- verification lens rule for U15 batch 1 (25 findings)
- verification lens sceptic for U15 batch 1 (25 findings)
- verification lens text for U15 batch 2 (25 findings)
- verification lens rule for U15 batch 2 (25 findings)
- verification lens sceptic for U15 batch 2 (25 findings)
- verification lens text for U02 batch 3 (25 findings)
- verification lens rule for U02 batch 3 (25 findings)
- verification lens sceptic for U02 batch 3 (25 findings)
- verification lens text for U15 batch 3 (25 findings)
- verification lens rule for U15 batch 3 (25 findings)
- verification lens sceptic for U15 batch 3 (25 findings)
- verification lens text for U15 batch 4 (25 findings)
- verification lens rule for U15 batch 4 (25 findings)
- verification lens sceptic for U15 batch 4 (25 findings)
- verification lens text for U15 batch 5 (25 findings)
- verification lens rule for U15 batch 5 (25 findings)
- verification lens sceptic for U15 batch 5 (25 findings)
- verification lens text for U15 batch 6 (25 findings)
- verification lens rule for U15 batch 6 (25 findings)
- verification lens sceptic for U15 batch 6 (25 findings)
- verification lens text for U15 batch 7 (8 findings)
- verification lens rule for U15 batch 7 (8 findings)
- verification lens sceptic for U15 batch 7 (8 findings)
- verification lens text for U05 batch 1 (25 findings)
- verification lens rule for U05 batch 1 (25 findings)
- verification lens sceptic for U05 batch 1 (25 findings)
- verification lens text for U05 batch 3 (25 findings)
- verification lens rule for U05 batch 3 (25 findings)
- verification lens sceptic for U05 batch 3 (25 findings)
- verification lens text for U05 batch 4 (25 findings)
- verification lens rule for U05 batch 4 (25 findings)
- verification lens sceptic for U05 batch 4 (25 findings)
- verification lens text for U05 batch 2 (25 findings)
- verification lens rule for U05 batch 2 (25 findings)
- verification lens sceptic for U05 batch 2 (25 findings)
- verification lens text for U05 batch 5 (25 findings)
- verification lens rule for U05 batch 5 (25 findings)
- verification lens sceptic for U05 batch 5 (25 findings)
- verification lens text for U05 batch 6 (8 findings)
- verification lens rule for U05 batch 6 (8 findings)
- verification lens sceptic for U05 batch 6 (8 findings)
- U03: merge failed, duplicates may remain
- U04: merge failed, duplicates may remain
- verification lens text for U03 batch 1 (25 findings)
- verification lens rule for U03 batch 1 (25 findings)
- verification lens sceptic for U03 batch 1 (25 findings)
- verification lens text for U03 batch 2 (25 findings)
- verification lens rule for U03 batch 2 (25 findings)
- verification lens sceptic for U03 batch 2 (25 findings)
- verification lens text for U03 batch 4 (25 findings)
- verification lens rule for U03 batch 4 (25 findings)
- verification lens sceptic for U03 batch 4 (25 findings)
- verification lens text for U03 batch 3 (25 findings)
- verification lens rule for U03 batch 3 (25 findings)
- verification lens sceptic for U03 batch 3 (25 findings)
- verification lens text for U04 batch 2 (25 findings)
- verification lens rule for U04 batch 2 (25 findings)
- verification lens sceptic for U04 batch 2 (25 findings)
- verification lens text for U04 batch 1 (25 findings)
- verification lens rule for U04 batch 1 (25 findings)
- verification lens sceptic for U04 batch 1 (25 findings)
- verification lens text for U03 batch 5 (3 findings)
- verification lens rule for U03 batch 5 (3 findings)
- verification lens sceptic for U03 batch 5 (3 findings)
- verification lens text for U04 batch 3 (25 findings)
- verification lens rule for U04 batch 3 (25 findings)
- verification lens sceptic for U04 batch 3 (25 findings)
- verification lens text for U04 batch 4 (25 findings)
- verification lens rule for U04 batch 4 (25 findings)
- verification lens sceptic for U04 batch 4 (25 findings)
- verification lens text for U04 batch 5 (10 findings)
- verification lens rule for U04 batch 5 (10 findings)
- verification lens sceptic for U04 batch 5 (10 findings)
- U06: completeness round 1 failed
- U06: merge failed, duplicates may remain
- verification lens text for U06 batch 2 (25 findings)
- verification lens rule for U06 batch 2 (25 findings)
- verification lens sceptic for U06 batch 2 (25 findings)
- verification lens text for U06 batch 3 (25 findings)
- verification lens rule for U06 batch 3 (25 findings)
- verification lens sceptic for U06 batch 3 (25 findings)
- verification lens text for U06 batch 1 (25 findings)
- verification lens rule for U06 batch 1 (25 findings)
- verification lens sceptic for U06 batch 1 (25 findings)
- verification lens text for U06 batch 5 (25 findings)
- verification lens rule for U06 batch 5 (25 findings)
- verification lens sceptic for U06 batch 5 (25 findings)
- verification lens text for U06 batch 4 (25 findings)
- verification lens rule for U06 batch 4 (25 findings)
- verification lens sceptic for U06 batch 4 (25 findings)
- verification lens text for U06 batch 6 (13 findings)
- verification lens rule for U06 batch 6 (13 findings)
- verification lens sceptic for U06 batch 6 (13 findings)
- U11: completeness round 1 failed
- U11: merge failed, duplicates may remain
- verification lens text for U11 batch 1 (25 findings)
- verification lens rule for U11 batch 1 (25 findings)
- verification lens sceptic for U11 batch 1 (25 findings)
- verification lens text for U11 batch 2 (25 findings)
- verification lens rule for U11 batch 2 (25 findings)
- verification lens sceptic for U11 batch 2 (25 findings)
- verification lens text for U11 batch 3 (25 findings)
- verification lens rule for U11 batch 3 (25 findings)
- verification lens sceptic for U11 batch 3 (25 findings)
- verification lens text for U11 batch 5 (25 findings)
- verification lens rule for U11 batch 5 (25 findings)
- verification lens sceptic for U11 batch 5 (25 findings)
- verification lens text for U11 batch 4 (25 findings)
- verification lens rule for U11 batch 4 (25 findings)
- verification lens sceptic for U11 batch 4 (25 findings)
- verification lens text for U11 batch 6 (1 findings)
- verification lens rule for U11 batch 6 (1 findings)
- verification lens sceptic for U11 batch 6 (1 findings)
- U08: completeness round 1 failed
- U08: merge failed, duplicates may remain
- verification lens text for U08 batch 1 (25 findings)
- verification lens rule for U08 batch 1 (25 findings)
- verification lens sceptic for U08 batch 1 (25 findings)
- verification lens text for U08 batch 2 (25 findings)
- verification lens rule for U08 batch 2 (25 findings)
- verification lens sceptic for U08 batch 2 (25 findings)
- verification lens text for U08 batch 3 (25 findings)
- verification lens rule for U08 batch 3 (25 findings)
- verification lens sceptic for U08 batch 3 (25 findings)
- verification lens text for U08 batch 5 (25 findings)
- verification lens rule for U08 batch 5 (25 findings)
- verification lens sceptic for U08 batch 5 (25 findings)
- verification lens text for U08 batch 6 (16 findings)
- verification lens rule for U08 batch 6 (16 findings)
- verification lens sceptic for U08 batch 6 (16 findings)
- verification lens text for U08 batch 4 (25 findings)
- verification lens rule for U08 batch 4 (25 findings)
- verification lens sceptic for U08 batch 4 (25 findings)
- U07: completeness round 1 failed
- U07: merge failed, duplicates may remain
- verification lens text for U07 batch 3 (25 findings)
- verification lens rule for U07 batch 3 (25 findings)
- verification lens sceptic for U07 batch 3 (25 findings)
- verification lens text for U07 batch 1 (25 findings)
- verification lens rule for U07 batch 1 (25 findings)
- verification lens sceptic for U07 batch 1 (25 findings)
- verification lens text for U07 batch 2 (25 findings)
- verification lens rule for U07 batch 2 (25 findings)
- verification lens sceptic for U07 batch 2 (25 findings)
- verification lens text for U07 batch 4 (25 findings)
- verification lens rule for U07 batch 4 (25 findings)
- verification lens sceptic for U07 batch 4 (25 findings)
- verification lens text for U07 batch 5 (16 findings)
- verification lens rule for U07 batch 5 (16 findings)
- verification lens sceptic for U07 batch 5 (16 findings)
- U09: completeness round 1 failed
- U09: merge failed, duplicates may remain
- verification lens text for U09 batch 2 (25 findings)
- verification lens rule for U09 batch 2 (25 findings)
- verification lens sceptic for U09 batch 2 (25 findings)
- verification lens text for U09 batch 3 (25 findings)
- verification lens rule for U09 batch 3 (25 findings)
- verification lens sceptic for U09 batch 3 (25 findings)
- verification lens text for U09 batch 4 (25 findings)
- verification lens rule for U09 batch 4 (25 findings)
- verification lens sceptic for U09 batch 4 (25 findings)
- verification lens text for U09 batch 1 (25 findings)
- verification lens rule for U09 batch 1 (25 findings)
- verification lens sceptic for U09 batch 1 (25 findings)
- verification lens text for U09 batch 5 (25 findings)
- verification lens rule for U09 batch 5 (25 findings)
- verification lens sceptic for U09 batch 5 (25 findings)
- verification lens text for U09 batch 6 (22 findings)
- verification lens rule for U09 batch 6 (22 findings)
- verification lens sceptic for U09 batch 6 (22 findings)
- U13: completeness round 1 failed
- U13: merge failed, duplicates may remain
- verification lens text for U13 batch 1 (25 findings)
- verification lens rule for U13 batch 1 (25 findings)
- verification lens sceptic for U13 batch 1 (25 findings)
- verification lens text for U13 batch 3 (25 findings)
- verification lens rule for U13 batch 3 (25 findings)
- verification lens sceptic for U13 batch 3 (25 findings)
- verification lens text for U13 batch 2 (25 findings)
- verification lens rule for U13 batch 2 (25 findings)
- verification lens sceptic for U13 batch 2 (25 findings)
- verification lens text for U13 batch 4 (25 findings)
- verification lens rule for U13 batch 4 (25 findings)
- verification lens sceptic for U13 batch 4 (25 findings)
- verification lens text for U13 batch 5 (25 findings)
- verification lens rule for U13 batch 5 (25 findings)
- verification lens sceptic for U13 batch 5 (25 findings)
- verification lens text for U13 batch 6 (25 findings)
- verification lens rule for U13 batch 6 (25 findings)
- verification lens sceptic for U13 batch 6 (25 findings)
- verification lens text for U13 batch 7 (25 findings)
- verification lens rule for U13 batch 7 (25 findings)
- verification lens sceptic for U13 batch 7 (25 findings)
- verification lens text for U13 batch 8 (22 findings)
- verification lens rule for U13 batch 8 (22 findings)
- verification lens sceptic for U13 batch 8 (22 findings)
- U10: completeness round 1 failed
- U10: merge failed, duplicates may remain
- verification lens text for U10 batch 3 (25 findings)
- verification lens rule for U10 batch 3 (25 findings)
- verification lens sceptic for U10 batch 3 (25 findings)
- verification lens text for U10 batch 5 (25 findings)
- verification lens rule for U10 batch 5 (25 findings)
- verification lens sceptic for U10 batch 5 (25 findings)
- verification lens text for U10 batch 4 (25 findings)
- verification lens rule for U10 batch 4 (25 findings)
- verification lens sceptic for U10 batch 4 (25 findings)
- verification lens text for U10 batch 2 (25 findings)
- verification lens rule for U10 batch 2 (25 findings)
- verification lens sceptic for U10 batch 2 (25 findings)
- verification lens text for U10 batch 1 (25 findings)
- verification lens rule for U10 batch 1 (25 findings)
- verification lens sceptic for U10 batch 1 (25 findings)
- verification lens text for U10 batch 6 (25 findings)
- verification lens rule for U10 batch 6 (25 findings)
- verification lens sceptic for U10 batch 6 (25 findings)
- verification lens text for U10 batch 7 (13 findings)
- verification lens rule for U10 batch 7 (13 findings)
- verification lens sceptic for U10 batch 7 (13 findings)
- U12: completeness round 1 failed
- U12: merge failed, duplicates may remain
- verification lens text for U12 batch 1 (25 findings)
- verification lens rule for U12 batch 1 (25 findings)
- verification lens sceptic for U12 batch 1 (25 findings)
- verification lens text for U12 batch 2 (25 findings)
- verification lens rule for U12 batch 2 (25 findings)
- verification lens sceptic for U12 batch 2 (25 findings)
- verification lens text for U12 batch 4 (25 findings)
- verification lens rule for U12 batch 4 (25 findings)
- verification lens sceptic for U12 batch 4 (25 findings)
- verification lens text for U12 batch 5 (25 findings)
- verification lens rule for U12 batch 5 (25 findings)
- verification lens sceptic for U12 batch 5 (25 findings)
- verification lens text for U12 batch 3 (25 findings)
- verification lens rule for U12 batch 3 (25 findings)
- verification lens sceptic for U12 batch 3 (25 findings)
- verification lens text for U12 batch 6 (25 findings)
- verification lens rule for U12 batch 6 (25 findings)
- verification lens sceptic for U12 batch 6 (25 findings)
- verification lens text for U12 batch 7 (11 findings)
- verification lens rule for U12 batch 7 (11 findings)
- verification lens sceptic for U12 batch 7 (11 findings)
- verification lens text for feedback batch 1 (25 findings)
- verification lens rule for feedback batch 1 (25 findings)
- verification lens sceptic for feedback batch 1 (25 findings)
- verification lens text for feedback batch 2 (13 findings)
- verification lens rule for feedback batch 2 (13 findings)
- verification lens sceptic for feedback batch 2 (13 findings)
- ledger step failed: no terminology table, no ledger findings
- calibration group 1 failed: its severities are uncalibrated
- calibration group 2 failed: its severities are uncalibrated
- calibration group 3 failed: its severities are uncalibrated
- calibration group 4 failed: its severities are uncalibrated
- themes step failed: no fix-first list and no cross-cutting themes
- summary paragraphs failed: section 1 lists the unit verdicts instead
