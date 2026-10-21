# Feedback log: supervisor reviews and AI editorial review (as of 2026-10-22)

All feedback received on the thesis text, in the order it arrived, with the problem behind each
point and what was changed. Compiled from the two annotated PDFs, the supervisor's two e-mails, the
AI editorial review, the worklists built from them and the git history.

| # | Review | Date | Source | Scope | Items |
|---|---|---|---|---|---|
| 1 | AI editorial review (flow, clarity, tone, AI tone) | 2026-10-01 | `reviews/editorial-2026-10-01/` (build of 2026-10-01) | whole thesis | 25 structural (S), 13 transitions (T), 17 repetitions (R), 14 patterns (P), 544 sentence items |
| 2 | Supervisor review 1 (Dmitrii Lachinov) | 2026-10-12 | `main-thesis_dl_rev1.pdf` (build of 2026-10-02) + e-mail | abstract, Ch. 1-3 | 28 PDF marks, 5 e-mail points |
| 3 | Supervisor review 2 | 2026-10-17 | `main-thesis_dl_rev2.pdf` (same build, marks 29-93) + e-mail | Ch. 4-7 (appendices skipped) | 65 PDF marks (grouped into 39 items), 6 e-mail points |

The two supervisor reviews come first below (they set the direction), then the AI review.

**Status words.** *Done* = changed in the text, with date and commit. *Open* = not yet done.
*Decided* = settled without a text change (kept on purpose, or declined). *Deferred* = waits for
something else (e.g. the abstract is rewritten last). Item IDs are those of the worklists
(`reviews/supervisor-rev1-2026-10-12.md`, `reviews/worklist-ch1-3-2026-10-14.md`,
`reviews/worklist-ch4-7-2026-10-17.md`), so each item can be looked up there in full. Section
numbers in "Feedback" refer to the build the reviewer read; "Fix" uses today's numbering.

**Not included:** the author's own tablet reviews v1-v6 (2026-09-25 to 2026-10-02) and the citation
rechecks; both are logged in `NOTES.md`.

## Summary

| Review | Items | Done | Decided (kept / declined) | Deferred / open |
|---|---|---|---|---|
| Supervisor review 1 (Part 1) | 34 | 23 (two of them drafts awaiting the author's review: §2.5.2, Related Work) | 2 (SV-1.2 keep, SV-X1 framework kept) | 7 deferred: the abstract (M1, SV-A1-A6); 2 items only point to others (SV-1.7, SV-2.6) |
| Supervisor review 2 (Part 2) | 53 | 39 | 3 (E6, SV-6.3, X8) | 11 open or partly: SV-4.2, SV-5.5 (§5.4), SV-5.12 (ask him), E1-E3, X1-X4, X7 |
| AI review, structure / transitions / repetition / patterns (Part 3) | 69 | 44 | 2 (S10, S25) | 23 open or partly, most of them thesis-wide patterns (P1-P12) |
| AI review, sentence items (Part 4) | 544 | 437 | 12 | 10 deferred (abstract), 11 open (10 in Appendices A-F); 74 superseded because the passage was rewritten anyway |

**Open points that need someone else:** reply mail to the supervisor (operator definition, framework
vs methodology, drugs kept in §1.1, SV-5.12 step-size ladder, JKU rule on AI-generated figures).

**One inconsistency found while compiling this list (fixed 2026-10-22, caption reworded to match §2.4 and §3.1):** after SV-3.1 the thesis says the data *are*
the Mai et al. (2024) cohort with tighter registration and cleaner segmentations (§2.4, §3.1), but the
caption of the horizon figure was changed back on 2026-10-22 (238a8bc) to "a larger cohort of the
same clinic" (`05-experiments.tex:806`). Both are true; pick one wording.

---

# Part 1. Supervisor review 1 (2026-10-12): abstract and Chapters 1-3

Source: 28 PDF annotations (27 highlights with comments, 1 strike-out) on pp. 2-34, plus his e-mail
("Overall, it looks good."). The first step was a restructure of Chapters 1-3 (commit `8d332fd`,
moves only), then bridges (2026-10-13) and one worklist pass per section (2026-10-14).

## 1.1 E-mail points

**M1 · Abstract is the most important part · Deferred**
- Feedback: most readers read only the abstract; polish it to near perfection.
- Issue: the abstract of 2026-10-02 followed the old framing and his structure (SV-A1) was not met.
- Fix: deliberately postponed until the rest of the thesis is settled, so it is written once (author,
  2026-10-14). His three-part template is recorded in `WRITING_GUIDE.md` §11 (2026-10-22).

**M2 · Prerequisite audit · Done 2026-10-14 (`c35cb71`, `4613118`)**
- Feedback: tick every new term as a prerequisite; the reader knows PDEs but not the medicine. After
  the Introduction the reader had met AMD, GA, fovea, VA, OCT without definitions.
- Issue: medical terms used before they were defined, mainly in Chapter 1.
- Fix: term table `reviews/m2-term-table-2026-10-14.md` (term, first use, where defined); 16 short
  glosses added at first use (AMD stages, macula, fovea, AREDS, complement inhibitors, best-corrected
  visual acuity, sham, intravitreal injections, OCT, biomarkers in §1.1; layer boundaries in §1.2;
  photoreceptors and fundus in §2.1.1; glioblastoma). Rows 17-18 (low-coherence, basal laminar
  deposits) left as they are.

**M3 · Structure of the opening chapter · Done 2026-10-12 to 10-14**
- Feedback: (1) medical background: eye, retina, layers, imaging (OCT, SLO, FAF), GA, drugs,
  patient management, predictive methods; (2) PDEs and solvers without GA; (3) motivation; (4) a
  formal problem statement with notation and equations; (5) outline.
- Issue: anatomy, imaging and pathology were intermixed; GA appeared in the PDE section; motivation
  stood before its context; no formal problem statement.
- Fix: restructure (`8d332fd`): Chapter 2 now runs Medical Background (Eye Anatomy -> Retinal
  Imaging -> Geographic Atrophy) -> PDEs and Numerical Solvers (no GA) -> Neural PDE Solvers ->
  Related Work -> Modelling Approach and Problem Statement. The former §1.2/§1.3/§2.2.5 motivation is
  §2.5.1; SLO and FAF got their own paragraph (`a420cf4`). Introduction and Background stay two chapters
  (author's choice; supervisor in review 2: "It's fine"). Drugs and patient management stay in §1.1
  (author, 2026-10-14; for the reply mail).
- M3.4 problem statement: §2.5.2 written 2026-10-14 (`49db013`): visits and irregular intervals, the
  state tensor on the anisotropic lattice, covariates, the residual update (Eq. `eq:bg:problem-update`),
  the definition of "operator", the rollout, the evaluation target and the research question in that
  notation. *Author review of §2.5.2 still pending.*

**M4 · No questions in headings · Done 2026-10-12/13**
- Feedback: "Why Neural PDE Solvers?" is not a good heading.
- Fix: now §2.5.1 "Choice of the Modelling Approach". Later also "Why Not Per-Pixel Error" ->
  "Evaluation Challenges" (review 2, SV-5.1).

**M5 · Contributions as bullet points · Done 2026-10-13**
- Feedback: what was achieved, what is novel, why it is valuable, as bullets.
- Issue: §1.4 had been merged into §1.3 prose on 2026-10-01.
- Fix: §1.3 Contributions is a bulleted list again; see SV-1.6 for the Δt claim.

## 1.2 Cross-cutting comments

**SV-X1 · p. 13 · "framework" -> "methodology" · Decided (ask in the reply mail)**
- Issue: "framework" for the fixed part around the solver.
- Fix: not renamed. In review 2 he writes "The framework defines ..." himself (SV-4.1), so the term is
  kept and the question goes into the reply mail.

**SV-X2 · p. 13 · "operator" -> "neural solver", "we are not necessarily dealing with operators" · Done 2026-10-13/14**
- Issue: "operator" in the neural-operator sense (FNO, DeepONet) does not cover a U-Net or a GNN.
- Fix: "operator" kept and defined once: at first use in §1.2 ("In this thesis, this map is called the
  operator.") and formally in §2.5.2 (general sense: a map from the state at one time to the state at a
  later time, explicitly not the narrow neural-operator sense). For the reply mail.

**SV-X3 · p. 12 · Background before motivation and problem statement; terms used before defined · Done 2026-10-12 (`8d332fd`)**
- Fix: see M3; the terms part is M2.

**SV-X4 · p. 25 · Merge §2.2.5 "Why this structure suits GA" with §1.3, at the end next to the motivation · Done 2026-10-12/13**
- Fix: both are now §2.5.1, reordered so the four properties come before the neural-solver paragraph,
  with a sentence on the 21:1 pixel spacing.

## 1.3 Abstract (p. 2)

**SV-A1-A6 · Deferred (with M1)**
- SV-A1: structure (intro with problem, difficulty and top-3 contributions; methods with data,
  implementation and measurements; results and conclusions with numbers vs the naive baseline).
- SV-A2: "is a lesion of lost retinal tissue" -> "the advanced form of AMD ... manifested as a gradual
  and irreversible loss of retinal tissue".
- SV-A3: the difficulty is the highly variable progression patterns and rates, not irregular visits.
- SV-A4: "This thesis asks what such a forecast needs" -> more formal ("aims to study ... from the
  computational modelling perspective").
- SV-A5: "49 × 1024" is too much detail.
- SV-A6: the openers "Together, ..." / "For the framework, ..." / "For the operator, ..." feel
  disconnected.
- Fix: none yet; all six go into the final rewrite (EN + German Kurzfassung).

## 1.4 Chapter 1 Introduction

**SV-1.1 · p. 10, §1.1 · Split the "no known, cost-effective means ... Clinical care therefore" sentence; two drugs approved in the US, not in the EU · Done 2026-10-14 (`8bcddcd`)**
- Issue: garden-path sentence; the treatment situation was outdated.
- Fix: two sentences ("Unlike cataract, glaucoma or diabetic retinopathy, AMD is not counted among the
  avoidable causes of vision loss."); §1.1 now says the FDA approved the complement inhibitors
  pegcetacoplan and avacincaptad pegol in 2023, that they are "approved in the United States but not in
  the European Union" (cited to the EMA pages EMA2024Syfovre, EMA2024Izelvay; ledger checked
  2026-10-16), and that they reduced lesion growth by roughly 14-27 % in the phase 3 trials.

**SV-1.2 · p. 11, §1.1 · "Well written" · Decided: kept**
- Fix: paragraph unchanged; the AI items 1.17-1.19 on the same paragraph were dropped.

**SV-1.3 · p. 11, §1.2 · Add that GA's growth rate is highly variable · Done 2026-10-14 (`8bcddcd`)**
- Issue: the need for forecasting tools was not motivated by the variability.
- Fix: §1.1 now says "Progression is also highly variable between patients, with the lesion area
  growing by 0.53 to 2.6 mm² per year" (Mai et al. 2024), followed by the clinical question of how fast
  and where the lesion will grow (also AI 1.14, 1.15).

**SV-1.4 · p. 12, §1.3 · Too much GA information, terms before definition · Done 2026-10-12/14**
- Fix: the GA paragraph moved to the Background (restructure); while moving, the anisotropy sentence was
  tied to the 21:1 pixel spacing rather than to the biological direction of growth (AI S16) and checked
  against Singh et al. 2025 (`85aced8`).

**SV-1.5 · p. 12 · "The setup — how elapsed time enters ... — is fixed once": restructure · Done 2026-10-14 (`8bcddcd`)**
- Fix: now "This thesis therefore separates the model from the setup around it. The setup comprises how
  elapsed time enters the prediction and how models are trained and evaluated. It is fixed once, and only
  the operator changes, ..." (AI 1.37, 1.39, 1.42).

**SV-1.6 · p. 13 · Check the literature before claiming Δt-conditioning as a contribution · Done 2026-10-13**
- Issue: Δt-conditioned / continuous-time models exist for GA (Lachinov et al. 2024, Neural ODE;
  ImageFlowNet 2024).
- Fix: the bullet no longer claims Δt-conditioning as new; it claims the architecture-independent
  framework. Both papers are cited in Related Work (SV-2.7).

**SV-1.7 · p. 13 · Research-question terms** -> SV-X1, SV-X2.

## 1.5 Chapter 2 Background

**SV-2.1 · p. 14 · Heading "A short anatomy primer" -> "Eye anatomy" · Done 2026-10-12**

**SV-2.2 · p. 16 · Order: anatomy -> imaging -> GA · Done 2026-10-12 (`8d332fd`)**

**SV-2.3 · p. 16 · GA section redefines the retina; introduce normal anatomy with a schematic (licensed third-party images allowed) · Done 2026-10-14 and 2026-10-16**
- Fix: the repeated retina definition dropped (`a420cf4`, AI 2a.9). Three figures made: Fig. 2.1 eye
  cross-section and fundus with macular zones and the OCT window (`49a37c3`, `9d76500`; zone sizes from
  Koksaldi 2025 and Nair 2021); Fig. 2.3 healthy and GA retinal layer strips (`4de09fb`); Fig. 2.2 OCT
  principle and scan geometry (`34f09f5`). Drawings are AI-generated (ChatGPT), labels added in code,
  caption says so. *Open: the JKU rule on declaring AI-generated figures (asked).*

**SV-2.4 · p. 16 · "What this end-stage lesion looks like on OCT has been formalised by ... CAM": improve · Done 2026-10-14 (`d2ab95f`)**
- Fix: pseudo-cleft removed; the CAM criteria introduced directly (AI 2a.12).

**SV-2.5 · p. 20 · §2.1.5 (state representation) and §2.1.6 (cohort) belong in the Data chapter · Done 2026-10-12/14**
- Fix: moved to §3.2 and §3.1 (`8d332fd`), then de-duplicated: the moved cohort block deleted except
  the 6 mm literature paragraph (now §3.3) and the bilateral evidence (now §3.7); the moved
  state-representation block merged into §3.2 (2026-10-14). Removes the AI repetitions R1-R3.

**SV-2.6 · p. 25 · Merge §2.2.5 with §1.3** -> SV-X4.

**SV-2.7 · p. 27 · Related Work too compact; dedicated subsections · Done as draft 2026-10-14 (`17f6bcd`), author review pending**
- Fix: five subsections (risk and rate; spatial forecasting of GA; irregular longitudinal data;
  PDE-based models in biomedicine; origins of the operators), 13 new references (Lachinov2024,
  Yoshida2025, Cluceru2024, Gigon2021, Lindner2018, Rubanova2019, ImageFlowNet, Ravi2022,
  Puglisi2024, Lipkova2019, Ezhov2022/2023, Banerjee2025), each with its PDF and a checked quote in the
  ledger. "Remains sparse" replaced by a sourced statement. The fifth subsection was later deleted in the
  repetition pass (2026-10-15). *Open: author review; four library papers without a local copy
  (Anegondi2023, Pfau2019, Niu2016, Zhang2021).*

## 1.6 Chapter 3 Data

**SV-3.1 · p. 29 · "yours is the same cohort with tighter registration bounds and cleaner segmentations" · Done 2026-10-14 (`8f3a860`)**
- Issue: the thesis described Mai et al. (2024) as "a larger cohort of the same clinic".
- Fix: §2.4, §3.1, Fig. 5.5, §6.2 and Ch. 7 reworded; also settles the device (Spectralis). See the
  inconsistency note in the summary (`05-experiments.tex:806`).

**SV-3.2 · p. 30 · Strike-out on "The data agree with this:" · Done 2026-10-14 (`5c54edb`)**
- Fix: the IoU sentence removed (AI 3.7).

**SV-3.3 · p. 30 · Pixel spacings in microns · Done 2026-10-14 (`5c54edb`)**
- Fix: 121.18 µm, 5.68 µm, 3.867 µm; thesis-wide follow-up in review 2 (X4).

**SV-3.4 · p. 31 · Cite the layer segmentation (Iowa Reference Algorithms) · Done 2026-10-14 (`24af4c5`), names 2026-10-19 (`8db7614`)**
- Fix: §3.2 cites Li 2006, Garvin 2009 and Abràmoff 2010 (PDFs filed, quotes checked); the ten
  boundary names (from the supervisor's review-2 e-mail, E5) added to §3.2 after checking that the
  mean depth rises over channels 1-10 in all 553 visits.

**SV-3.5 · p. 34 · Report patients / eyes per fold · Done 2026-10-14 (`c5d95de`)**
- Fix: the fold table gives patients and eyes per fold.

---

# Part 2. Supervisor review 2 (2026-10-17): Chapters 4-7

Source: marks 29-93 of `main-thesis_dl_rev2.pdf` (65 highlights, 47 with a comment; uncommented
highlights read as examples of the sentence patterns his e-mail names) and his e-mail. Worked through
2026-10-17 to 2026-10-19, section by section.

## 2.1 E-mail points

**E1 · Every section = intro (purpose + thesis statement) / body / conclusion · Done for Ch. 4-7 sections, thesis-wide pass open**
- Fix: applied in the rewrites of §4.1-§4.3, §5.2, §5.3, §5.5-§5.8, §6.1-§6.4, Ch. 7 and Appendix G
  (2026-10-17 to 10-19). Chapter 4 reordered so the framework sits in one place: §4.2 now holds
  conditioning and training as subsections (`264aebf`). New §5.9 Summary so Chapter 5 ends on its answer.
  *Open: §5.4 (fold differences, written 2026-10-18, not reviewed) and a check of Ch. 1-3 against the
  rule.*

**E2 · Sentence structure: follow the guidelines book; avoid LLM constructions ("What it does is that ...", "not this but that") · Partly done**
- Fix: the guidelines book (Skern, *Writing Scientific English*) is distilled into `WRITING_GUIDE.md`,
  his instructions in its §11 (2026-10-22, `825e9bd`). The patterns were removed in every section
  rewritten for review 2. *Open: one thesis-wide pass (X3).*

**E3 · One table or plot per results subsection; small excerpts next to each ablation · Partly done**
- Fix: new objective table in §5.5.2 (SV-5.13), step-size ladder table and figures in §5.6.1, fold
  figures in §5.4, learning-speed figure in §5.1.4; the disabled figures restored, redrawn or removed
  (2026-10-17 to 10-21). *Open: a planned table/figure for every remaining subsection (X7).*

**E4 · Figures with LLMs are fine; he uses matplotlib/seaborn scripts and Claude SVG + draw.io · Done**
- Fix: data figures are scripts in `images/scripts/` following `style/`; the pipeline figure (Fig. 4.1)
  is TikZ; the solver-path figure (Fig. 2.5) a script.

**E5 · The ten layer boundaries (ILM ... outer boundary of the RPE) · Done 2026-10-19 (`8db7614`)**
- Fix: names in §3.2 (checked against the depth order of the data); the "names not recorded" clause in
  §6.3 removed.

**E6 · Introduction and Background not merged: "It's fine." · Decided**

## 2.2 Cross-cutting work derived from the comments

| # | Topic | Status | What was done / what is left |
|---|---|---|---|
| X1 | Forward references (SV-4.5: "minimise similar occurrences") | Open | Local fix in §4.3.2 done; no thesis-wide list of forward `\ref`s yet. |
| X2 | Paragraph-opening "This ..." | Partly | Fixed where marked (SV-5.6, SV-5.9) and in the Ch. 5-7 rewrites; no thesis-wide pass. |
| X3 | LLM sentence patterns ("X is not what decides Y", "What separates ... is", "not X but Y") | Partly | Removed in Ch. 4-7 rewrites; two left in the text (abstract, deferred; `05-experiments.tex:1435` "not what separated"). |
| X4 | Micrometres for reaches and front advances | Partly | §2.5.2, §3.1, §4.3.3, Fig. 4.2, §4.3.4, §5.3, §6.1 converted; remaining mm/column distances not checked thesis-wide. |
| X5 | Plain headings, no slogans or questions | Done | All marked headings renamed (SV-4.6, 4.10, 5.1, 5.3, 5.4, 5.10, 6.1, 6.6); run-in headings of §6.4 kept (author, 2026-10-02). |
| X6 | Terms: ingredient, anchor, backbone, arm | Done | "ingredient" -> "property" (only label names keep it); "anchor" kept and defined at first use in §5.1.2 (SV-6.4); "backbone" left twice; "arm" defined in §4.1. |
| X7 | One table/figure per results subsection | Partly | See E3. |
| X8 | "framework" vs "methodology" | Decided | Kept; for the reply mail (SV-X1). |

## 2.3 Chapter 4 Method

**SV-4.1 · #29, p. 36, §4.1 · "The framework separates the training and evaluation setup from the spatial operators": not clear; say what the framework defines and that it removes confounders · Done 2026-10-17 (`e91cde5`)**
- Fix: first paragraph now says what the framework defines (time handling, training, evaluation, shared
  by every operator) and that this removes them as confounding factors; "canonical" defined at first use.

**SV-4.2 · #30, p. 37 · Put the MM-PDE result into the main text: a negative result is also a result · Open (author not convinced)**
- Issue: conflicts with the author decision of 2026-09-25 (all MM-PDE in Appendix G).
- Status: `% TODO` in §4.1. Checked: on the dilated stencil only one fold-2 dual run exists, no bypass
  control, no 5-fold arm; the 5-fold dual and bypass arms ran on the k-NN graph. Appendix G was rewritten
  2026-10-19 so it could move into the main text with little rework (`b495589`).

**SV-4.3 · #31, p. 38 · Δt -> 0 limit "not entirely true as we don't know df/dΔt; put an assumption on the Lipschitz constant" · Done 2026-10-17 (`ff3d1ad`)**
- Fix: §4.2.1 states the assumption (f_θ bounded as Δt -> 0, e.g. Lipschitz in Δt); §5.5.1 points to it.

**SV-4.4 · #32, p. 38 · "(C, N, K) = (11, 50 176, 1)": does not match · Done 2026-10-17 (`610fdf3`)**
- Issue: K meant the number of visits in §2.5.2 but the bundle size here; layout notation differed.
- Fix: tensor layout written in the §2.5.2 notation (C × H × W, flattened to N = HW nodes), K dropped;
  Eq. 4.1 refers back to Eq. `eq:bg:problem-update`.

**SV-4.5 · #33, p. 40 · Avoid forward references; introduce the grid before it is used · Done locally 2026-10-17 (`4ca4d1a`)**
- Fix: forward pointers removed from §4.3.2; thesis-wide part is X1 (open).

**SV-4.6 · #34-#36, pp. 40-42 · "architecture used here" -> "used in this work"; run-ins -> "Proposed modifications", "Summary of the modifications" · Done 2026-10-17 (`4ca4d1a`)**

**SV-4.7 · #37-#38, p. 42 · Define "nearest neighbours" (Euclidean yes, geodesic no); index graph = geodesic distance · Done 2026-10-17 (`43ff0dd`)**
- Fix: the metric named for each graph (Euclidean in mm vs Euclidean in integer indices); the k = 12
  index neighbourhood stated to equal the ball of geodesic radius 2 on the 4-connected lattice.

**SV-4.8 · #39, p. 44 · Check whether the dilated stencil is used in the literature; cite · Done 2026-10-17 (`43ff0dd`)**
- Fix: dilated convolutions (Yu & Koltun 2016) and dilated k-NN graphs (Li et al., DeepGCNs 2019)
  cited. *Ledger batch for these two still to run (Phase 4).*

**SV-4.9 · #40, p. 48 · "The Runge-Kutta wrapper is not a backbone. It is placed around any backbone": rephrase · Done 2026-10-18 (`4499804`)**

**SV-4.10 · #41-#43, p. 49 · Run-ins "Why the wrapper exists.", "Jump and continuous time.", "The autonomous field." · Done 2026-10-18 (`4499804`)**
- Fix: §4.3.7 restructured without run-in headings: what the wrapper computes, why it is used, then
  the autonomous variant; no result preview (also AI S8, R5).

## 2.4 Chapter 5 Experiments

**SV-5.1 · #44, p. 55 · "Why Not Per-Pixel Error" -> "Evaluation Challenges" · Done 2026-10-18 (`85ca6d0`)**

**SV-5.2 · #45, p. 58 · Noise rule: assume normal error, estimate σ empirically, do a z-test · Done 2026-10-18 (`cb212b9`), author to re-read**
- Fix: §5.1.5 states the rule as z = mean paired difference / σ_Δ, σ_Δ = √(σ_A² + σ_B²)/√n, σ_GNN =
  0.0127 from replicate pairs, σ_U-Net = 0.0191 from its seed pairs on all five folds (local fold-2 repeats as a
  check, `c042783`); |z| > 1.96. App. E criteria rewritten, z in every fold-paired cell. Readings that changed:
  T-FEN − stencil and stencil − U-Net "just beyond noise at seed 42, not established".

**SV-5.3 · #46, p. 58 · "The Arm Table": make it the results section · Done 2026-10-19 (`701a374`)**
- Fix: "Main Results"; intro -> reading the table -> three highest arms -> interior eyes -> canonical
  choice -> example eye -> summary; no ingredient claim before §5.3 (AI S11, T10).

**SV-5.4 · #47-#48, p. 61 · "What is ingredient?"; heading "Ablation studies" · Done 2026-10-19 (`92a9443`)**
- Fix: section "Ablation Studies"; "ingredient" -> "property" in §2.3, §5.3, §6.1; opener with a map.

**SV-5.5 · #49, #53 · Each results subsection: Goal -> Results -> Conclusion, take-home message · Done for §5.2, §5.3, §5.5-§5.8; open for §5.4**
- Fix: applied in `701a374`, `92a9443`, `636d1b6`, `e268484`, `267037b`, `f71f1f6`. *Open: §5.4
  "Differences Between Folds" (written 2026-10-18, after his review).*

**SV-5.6 · #50-#51, p. 62 · "This comparison keeps ...": avoid "This"; "This also explains an earlier result": the neighbour placement? · Done 2026-10-19 (`92a9443`)**

**SV-5.7 · #52, p. 63 · Make clear what is compared (FNO vs FNO + local kernel) · Done 2026-10-19 (`636d1b6`)**

**SV-5.8 · #53, p. 63 · FNO paragraph as Goal / Results / Conclusion; separate the within-architecture ablation from the comparison with others · Done 2026-10-19 (`636d1b6`)**

**SV-5.9 · #54-#56, p. 64 · "This comparison pairs the T-FEN": expand; mid-paragraph "This" is fine · Done 2026-10-19 (`636d1b6`)**
- Fix: §5.3.4 opening explains the free-form term, the transport term and the zero-init; fold-4 failure
  of the matched control and the limit of the control stated.

**SV-5.10 · #57-#58, p. 66 · "Two Routes to One Deficit": rephrase; closing "not what separates ... the ingredients are": hard to digest · Done 2026-10-19 (`636d1b6`)**
- Fix: heading "Summary of the Ablation Studies"; closing states the two magnitudes plainly.

**SV-5.11 · #59-#60, p. 66 · "Two tests ask this", "The first test asks" · Done 2026-10-19 (`e268484`)**

**SV-5.12 · #61, p. 67 · Another test on step size: h = 1, 1/2, ..., 1/32 year · Done as post-hoc ladder; open: ask him whether this is what he meant**
- Fix: trained networks re-evaluated with fixed steps (no retraining), three models, folds 0-2
  (`d2e2401`); §5.6.1 rewritten around it with Table 5.4 and an Appendix E table (`267037b`); figures
  `fig:experiments:swap` and `fig:experiments:swap-tfen` (2026-10-21). Readout: the canonical model fails
  the agreement criterion on all three folds; the RK4-trained network converges, its Dice rises by 0.018
  on folds 0-1 with finer steps; the T-FEN passes. *Open: folds 3-4; question to the supervisor whether
  networks trained at different step sizes were meant.*

**SV-5.13 · #62, p. 67 · Use tables or boxplots for ablations · Done 2026-10-19 (`e268484`)**
- Fix: Table `tab:experiments:objective` (full / without soft-Dice / plain MSE / with penalty) next to
  §5.5.2.

**SV-5.14 · #63, p. 67 · "(Figure 5.1b)": figure placed 10 pages earlier · Done 2026-10-18/19**
- Fix: the old combined figure split; the objective figure sits in §5.5.2 next to its discussion.

**SV-5.15 · #64, p. 69 · Section opener "The two diagnostics ... are not accuracy numbers": say what is done · Done 2026-10-19 (`267037b`)**

**SV-5.16 · #65-#66, p. 72 · Table 5.4: give step size in days with the number of steps; "90-day steps" does not match · Done 2026-10-19 (`267037b`)**
- Fix: the step-size ladder table uses fixed steps (365 ... 11.4 d) for every model.

**SV-5.17 · #67-#68, p. 75 · "32 months" vs "3.3 years" · Done 2026-10-19 (`f71f1f6`)**
- Fix: same unit (32 months ≈ 2.7 years); §5.7 now "Comparison with Prior Work", also against Gigon et al.
  2021, Salvi et al. 2025 and Yoshida et al. 2025.

## 2.5 Chapter 6 Discussion

**SV-6.1 · #69-#74, p. 78 · Rewrite §6.1 for a reader who skipped the thesis; "The operator class did not decide ..." rephrase · Done 2026-10-19 (`721759e`)**
- Fix: self-contained (task, data, measure, each result with its number); subsections 6.1.1-6.1.6
  instead of run-in headings; one answer to sub-question 1; why more reach stops helping.

**SV-6.2 · #75, p. 79 · "10 to 25 columns": use microns · Done 2026-10-19 (`721759e`)**
- Fix: 57-142 µm (and 11 / 119 µm per hop).

**SV-6.3 · #76-#77, p. 79 · Capacity paragraph and equation-features paragraph: good, keep · Decided: kept**
- Fix: unchanged apart from one phrase; AI items 6-7.13 to 6-7.19 and 6-7.21 dropped.

**SV-6.4 · #78, p. 80 · "anchor": study evaluation interval? · Done 2026-10-19 (`fe7a1d8`)**
- Fix: "anchor" kept and defined at its first use in §5.1.2; §3.3 points to §3.6; the bare "at the
  anchor" of §6.1 now "at one year". A thesis-wide rename to "the one-year visit" was tried and reverted.

**SV-6.5 · #79, p. 80 · "If predictions between visits are needed clinically ...": rephrase · Done 2026-10-19 (`721759e`)**

**SV-6.6 · #80, p. 80 · Run-in "Where modelling effort pays." · Done 2026-10-19 (`721759e`)**
- Fix: subsection "Implications for Modelling".

**SV-6.7 · #81, p. 82 · "most likely annotated on fundus autofluorescence": it was · Done 2026-10-19 (`8db7614`)**
- Fix: hedge removed in §6.3 and §3.1; closes the mask-provenance fact check of 2026-09-25.

## 2.6 Chapter 7 Conclusion

**SV-7.1 · #82-#84 · "needs" -> "requires", "the same way" -> "equally", "does this" -> "implements the requirements" · Done 2026-10-19 (`5041665`)**

**SV-7.2 · #85 · "Held fixed, it served operators from unrelated literatures ..." · Done 2026-10-19 (`5041665`)**
- Fix: participle opener removed.

**SV-7.3 · #86-#87 · "the architecture class is not what decides the outcome" ("they are all over"); "What separates ..." · Done in Ch. 7 2026-10-19 (`5041665`)**
- Fix: replaced by plain statements of what was measured; thesis-wide part X3.

**SV-7.4 · #88-#91 · "Without it,", "where the neighbours ... lie", "lies below the U-Net" · Done 2026-10-19 (`5041665`)**
- Fix: bullets name their subject and use "scores".

**SV-7.5 · #92-#93 · "The negative results are part of the answer."; "In short, ... what matters is ... rather than ..." · Done 2026-10-19 (`5041665`)**
- Fix: slogan sentence and closing antithesis removed; limits moved into the last paragraph.


---

# Part 3. AI editorial review (2026-10-01): structure, transitions, repetition, patterns

Source: `reviews/editorial-2026-10-01/00-overview.md`, build of 2026-10-01 (before both supervisor
reviews). Advisory only; it changed no `.tex` file. GPTZero scans were used as pointers, not as
evidence. Section numbers in "Issue" are those of that build.

## 3.1 Fix first

| # | Issue | Fix | Status |
|---|---|---|---|
| 1 | Two sentences lost in the PDF: prose appended to a `%` comment line in §5.1.3 and §5.4.2 (= S1, 5a.19, 5c.17) | Line break after each comment, wording unchanged | Done 2026-10-01 |
| 2a | Mask provenance: §2.1.2 says OCT signatures define channel 0, §3.1 says FAF annotation (= S5, 2a.17) | §2.1.2 no longer claims the signatures define the mask; §3.1 states the FAF annotation (confirmed by the supervisor, SV-6.7) | Done 2026-10-01/02, hedge removed 2026-10-19 |
| 2b | Covariates promised as "tested in this thesis" (= S4, 1.27) | Clause removed | Done 2026-10-02 (`f998855`) |
| 2c | Layer channels "not auxiliary" vs "auxiliary targets"; Fig. 2.2 caption maps strata onto channels (= S9) | §2.1.5 reworded; caption no longer maps strata to channels | Done 2026-10-02 and 2026-10-14 (`d2ab95f`) |
| 2d | Dead pointers §2.1.1 -> §1.2 and §3.7 -> §5.1 (= S22) | Pointers corrected / replaced | Done 2026-10-02 and 2026-10-14 |
| 3 | Wording that changes a result: C2 criterion (5d.4), "Its accuracy" (5d.16), Pearson r "scales" (5d.23), T-FEN transport mesh (4b.25), objective opener (5c.11) | Each reworded | Done 2026-10-02 (`05f0541`) |
| 4 | Terms used before definition or with several meanings: arm, canonical, "the same deficit", window, floor, anchor, late epochs, instrument | "arm" and "canonical" defined in §4.1; "transition window" in §3.5; "the same deficit" glossed; "anchor" defined in §5.1.2; "late-epoch mean" got its own §5.1.4 | Done 2026-10-02 to 2026-10-19 |

## 3.2 Structural issues (S1-S25)

| # | Issue (short) | Fix | Status |
|---|---|---|---|
| S1 | Sentences lost after `%` comments (§5.1.3, §5.4.2) | Line breaks | Done 2026-10-01 |
| S2 | Research-question mapping: Ch. 4 never names sub-question 1; Ch. 5 also tests the framework | §4.1 opens with sub-question 1; Chapter 5 opener names the framework tests of §5.5 | Done 2026-10-02 / 2026-10-19 |
| S3 | §5.4 "Negative Results" holds the clearest positive framework result (objective) | Heading kept; opener names the two objective effects as exceptions | Done 2026-10-19 (`e268484`) |
| S4 | Covariates "tested in this thesis" | Clause removed | Done 2026-10-02 |
| S5 | Mask provenance Background vs Data | See Fix first 2a | Done |
| S6 | Statistics density in Ch. 5 ("Δ = ... SE (k/5) ... t = ...") | Reporting pass: results in words, statistics in App. E | Done 2026-10-02 (`2318a0f`) |
| S7 | Framework spread over §4.2, §4.4, §4.5 | Chapter 4 reordered: conditioning and training are subsections of §4.2 | Done 2026-10-18 (`264aebf`) |
| S8 | Results previewed in Ch. 4 ("turns out ...", Galerkin "turned out to be unstable", solver-swap outcome) | Previews removed from §4.3.3, §4.3.6, §4.3.7; stability definition moved to Ch. 5 | Done 2026-10-17/18 |
| S9 | Layer channels "not auxiliary" vs "auxiliary targets" | See Fix first 2c | Done |
| S10 | Ch. 1-3 argue the layer channels are needed; no experiment isolates them | Declined by the author (wording stays) | Decided 2026-10-14 |
| S11 | §5.2 paragraph order; conclusion before the information to read the table | §5.2 restructured (SV-5.3) | Done 2026-10-19 |
| S12 | §5.6 "Qualitative Analysis" holds only the Mai comparison | Renamed "Comparison with Prior Work" (§5.7) | Done 2026-10-19 |
| S13 | Ground-truth shrinkage quantified only in §6.3 although §4.2.1 and §5.5.2 rely on it (= R15) | Not moved | Open |
| S14 | §6.1 gives two answers to sub-question 1 | One answer in §6.1.1 | Done 2026-10-19 |
| S15 | Ch. 2, 3, 4 have no chapter openers naming their role | Openers added (Ch. 2 2026-10-13, Ch. 3 2026-10-14, Ch. 4 2026-10-02/17) | Done |
| S16 | Reach motivated by biological anisotropy, result rests on 21:1 pixel spacing | §2.5.1 sentence on the pixel spacing | Done 2026-10-13/14 |
| S17 | Learned solvers introduced twice (§2.2.4 and §2.3) | Former §2.2.4 now opens §2.3 (restructure) | Done 2026-10-12 |
| S18 | Register shifts in §2.1 (analogies, "takes some getting used to", "Put differently") | Removed in the §2.1 worklist pass (2a items) | Done 2026-10-02 / 2026-10-14 |
| S19 | Terminology drift (arm, canonical, ingredient / inductive bias / property, operator / backbone / module) | "arm", "canonical" defined; "ingredient" -> "property"; "operator" defined in §1.2/§2.5.2; "backbone" left twice | Done (two "backbone" left) |
| S20 | Intermediate-time-point regulariser first appears in §6.1 | §6.1.5 places it as an earlier attempt, removed before the experiments of Ch. 5 | Done 2026-10-19 |
| S21 | Keywords foreground MP-PDE, MM-PDE, moving mesh | Keywords changed; title still a working title (open with the supervisor) | Done 2026-10-02 (`803b997`) |
| S22 | Two dead pointers | Fixed | Done |
| S23 | §1.3 holds motivation, research question and contributions under one heading | Restructure: research question in §1.2, contributions as bullets in §1.3, motivation in §2.5.1 | Done 2026-10-12/13 |
| S24 | Implementation history in the prose (365 vs 365.25 footnote, unit-check of convergence orders, GPU-sharing sentence) | GPU sentence and unit-check removed; the 365.25 footnote in §3.6 is still there | Partly |
| S25 | Depth balance: §2.1 long, §2.3 short, §4.2.2 thin | Closed without cuts (supervisor wants more medical background); §4.2.2 folded into §4.2 | Decided 2026-10-15 |

## 3.3 Transitions (T1-T13)

| # | Issue (short) | Fix | Status |
|---|---|---|---|
| T1 | Ch. 1 -> Ch. 2: no chapter opener, audience sentence, two roadmaps of §2.1 | Chapter opener, audience sentence cut, one roadmap | Done 2026-10-12/13 |
| T2 | §1.2 -> §1.3: announces framework motivation, delivers operator motivation | Restructure into §2.5.1 | Done 2026-10-12/13 |
| T3 | Ch. 2 -> Ch. 3: cohort presented twice, no opener | Cohort only in Ch. 3; Ch. 3 opener | Done 2026-10-14 |
| T4 | Ch. 3 -> Ch. 4: dead pointer to §5.1; Ch. 4 opens with project provenance | Pointer fixed; provenance sentence removed, Ch. 4 opens with sub-question 1 | Done 2026-10-02 |
| T5 | Ch. 5 opener says only part 2, but §5.4.1-§5.4.2 test the framework | Opener with a section map naming the framework tests | Done 2026-10-19 |
| T6 | Ch. 5 ends on computational cost, not on its answer | New §5.9 Summary | Done 2026-10-19 |
| T7 | Ch. 7 re-runs §6.1 paragraph by paragraph | Ch. 7 reworded (SV-7.x) but still follows §6.1 | Open |
| T8 | Learned solvers in §2.2.4, GA argument §2.2.5, then §2.3 restarts | Restructure | Done 2026-10-12 |
| T9 | Framework split by the operator section | Chapter 4 reordered | Done 2026-10-18 |
| T10 | §5.2 states the ingredient conclusion before §5.3 shows it | Removed from §5.2 | Done 2026-10-19 |
| T11 | §5.3.5 hands over with "§5.4 reports what ... did not matter", but the objective mattered | §5.3.5 rewritten (SV-5.10); handover sentence gone | Done 2026-10-19 |
| T12 | §5.6 opens without text, title promises qualitative analysis | §5.7 renamed with an opener | Done 2026-10-19 |
| T13 | Appendices B and C empty; App. E titled "Ablation Details" but holds other results; Table E.3 unreferenced | Table E.3 now referenced; B, C still headings only; App. E title unchanged (item A.6) | Open |

## 3.4 Repetition across chapters (R1-R17)

| # | Repeated content | Fix | Status |
|---|---|---|---|
| R1 | Crop census in §2.1.6, §3.3, §6.3, App. A.2, §6.4 | Full census only in §3.3; elsewhere pointers | Done 2026-10-15 (`eddb628`) |
| R2 | Cohort facts in §2.1.6, §3.1, §3.3 | §2.1.6 moved to Ch. 3 and de-duplicated | Done 2026-10-12/14 |
| R3 | Layer channels as depth maps defined four times | Definition in §3.2 | Done 2026-10-12/14 |
| R4 | Retina defined three times; two roadmaps in §2.1 | Restructure and §2.1 pass | Done 2026-10-12/14 |
| R5 | Continuous-time caution in §2.3, §4.2.1, §4.3.7, §5.4.1, §5.5.1 | Reduced in §4.3.7 (no outcome); not consolidated thesis-wide | Partly |
| R6 | Batch-statistics argument four times in Ch. 4 | Curriculum no longer repeats it; still in §4.3.1 and the GNN/U-Net normalisation sentences | Partly |
| R7 | "Differences can be attributed to the operator" six times in Ch. 4 | Some cut in §4.1-§4.3 rewrites | Partly |
| R8 | Original MP-PDE decoder described twice | Described once | Done 2026-10-17 (`4ca4d1a`) |
| R9 | Free-form FEN controls in §4.3.6, §4.3.8, Table 4.2, §5.3.4 | Parameter split moved to §4.3.8 | Done 2026-10-18 (`6c00216`) |
| R10 | Galerkin vs energy-conserving form in five places | Stability definition moved to Ch. 5; form stated in §4.3.6 and §5.6.2 | Partly |
| R11 | Covariates cannot localise anything (§4.4, §6.1, §6.3) | Not consolidated | Open |
| R12 | Mai et al. caveats about seven times | Full caveats only in §5.7 first paragraph | Done 2026-10-15 |
| R13 | Headline antithesis at most section ends | Removed in the Ch. 5-7 rewrites (X3) | Done in Ch. 5-7 |
| R14 | Seed-7 numbers throughout Ch. 5 | Moved to App. E | Done 2026-10-02 |
| R15 | Ground-truth shrinkage (= S13) | | Open |
| R16 | "No test split" twice in §5.1.3; anchor without upper bound in three places | Not consolidated | Open |
| R17 | Operator origins in §2.3, §2.4, §4.3 | §2.4.5 deleted; origins in §2.3 and §4.3 | Done 2026-10-15 |

## 3.5 Recurring sentence patterns (P1-P14)

The review gave each pattern a global fix. They were treated item by item (Part 4) and in the section
rewrites for supervisor review 2; a single thesis-wide pass over Ch. 1-3 and the appendices is still
open (X3, `WRITING_GUIDE.md` §11).

| # | Pattern | Status |
|---|---|---|
| P1 | Contrast frames as the main claim ("not X but Y", "X rather than Y") | Removed in Ch. 4-7 rewrites; 21 "rather than" left thesis-wide (most legitimate); pass open |
| P2 | Restating verdict closers | Removed where flagged; pass open |
| P3 | Cleft and pseudo-cleft sentences ("What X needs is ...") | Removed in Ch. 4-7; one left in the deferred abstract, one in §5.5 |
| P4 | Mirrored verdict pairs, staccato verdicts | Removed where flagged |
| P5 | Announce-then-enumerate ("Two tests ask this.") | Removed where flagged (SV-5.11) |
| P6 | Consequence-connective chains | Removed where flagged |
| P7 | Em-dash asides | Removed where flagged; about a dozen em-dashes left (`WRITING_GUIDE.md` check) |
| P8 | Semicolon and colon hinges | Removed where flagged |
| P9 | Stock intensifiers | 25 removed in the one-word pass (2026-10-02), more in later passes |
| P10 | Idioms and methods as agents ("buys", "pays off", "tests ask") | Removed where flagged (SV-5.11, SV-6.6) |
| P11 | Signposting and roadmap paragraphs | Reduced to one map per chapter/section |
| P12 | Slogan-style run-in headings | Removed in §5.4-§5.5, §6.1-§6.3, Ch. 7 (2026-10-02, 2026-10-19); §6.4 run-ins kept |
| P13 | Over-explaining glosses, conversational register (§2.1) | Done in the §2.1 pass (2026-10-14) |
| P14 | Templated statistical sentences in Ch. 5 | Done in the reporting pass (2026-10-02) |

The overview also lists "points where a first-time reader gets lost" and a terminology table; both
point to the sentence items of Part 4 and to S19, and are not repeated here.

---

# Part 4. AI editorial review: sentence items (544)

Each item: ID, severity, place in the build of 2026-10-01, status; then the issue the review named, the passage as it was, and how it reads today. The status was checked automatically against today's `.tex` (comments stripped): *as suggested* = the suggested wording is in the text; *own wording* = the old passage is gone and the worklist marks the item done; *Now* quotes the closest current sentence where one was found. Items marked *Superseded* were not worked on one by one: the passage they refer to was rewritten for other reasons. Severity *high* items are the ones the review asked to fix first.

| Part of the thesis | Done | Superseded | Decided | Deferred | Open |
|---|---|---|---|---|---|
| Abstract and Chapter 1 | 30 | 0 | 3 | 10 | 0 |
| Chapter 2, medical background (§2.1) | 38 | 0 | 0 | 0 | 0 |
| Chapter 2, solvers, neural solvers, related work (§2.2-§2.5) | 45 | 0 | 1 | 0 | 0 |
| Chapter 3 | 36 | 0 | 0 | 0 | 0 |
| Chapter 4, overview, framework, operator contract, GNN | 36 | 1 | 0 | 0 | 0 |
| Chapter 4, graph construction and the other operators | 47 | 1 | 0 | 0 | 0 |
| Chapter 4, conditioning, training, implementation | 26 | 0 | 0 | 0 | 0 |
| Chapter 5, protocol and main results | 30 | 10 | 0 | 0 | 0 |
| Chapter 5, ablation studies | 26 | 8 | 0 | 0 | 0 |
| Chapter 5, negative results | 28 | 2 | 0 | 0 | 0 |
| Chapter 5, validity, prior work, cost | 41 | 4 | 0 | 0 | 0 |
| Chapters 6 and 7 | 43 | 5 | 8 | 0 | 0 |
| Appendices A-F | 1 | 3 | 0 | 0 | 10 |
| Appendix G (MM-PDE) | 10 | 40 | 0 | 0 | 1 |
| **Total** | **437** | **74** | **12** | **10** | **11** |

**Still open:** A.1, A.3, A.6, A.7, A.8, A.9, A.10, A.11, A.13, A.14, G.40 (mostly Appendices A-F, which neither supervisor review covered).

## Abstract and Chapter 1

Source: `reviews/editorial-2026-10-01/01-abstract-introduction.md`.

- **1.1** [medium] Abstract, paragraph 2 · `00-abstract.tex:29` (today `00-abstract.tex:43`) · **Deferred**: abstract rewritten on 2026-10-02 (review v6); final rewrite with the supervisor's template still to come
  - Issue: 'persistence' is not explained, 'and one loss' dangles at the end, and it is unclear whether 'measured in elapsed days' applies to the curriculum or the loss.
  - Was: "A zero-initialised output starts every operator at exact persistence, and all operators are trained with one pushforward curriculum measured in elapsed days and one loss."
  - Suggested: "A zero-initialised output layer starts every operator at exact persistence (no change), and all operators share one loss and one pushforward curriculum measured in elapsed days."
- **1.2** [medium] Abstract, paragraph 2 · `00-abstract.tex:31` (today `00-abstract.tex:45`) · **Deferred**: abstract rewritten on 2026-10-02 (review v6); final rewrite with the supervisor's template still to come
  - Issue: The 30-word subject list delays the verb to the end, and 'this slot' has no antecedent: the abstract never calls $f_\theta$ a slot.
  - Was: "Only the operator $f_\theta$ varies. Message-passing graph networks on two neighbourhood graphs, a U-Net, Fourier Neural Operators with and without a local path, and Finite Element Networks with and without a learned transport term were placed in this slot at ..."
  - Suggested: "Only the operator $f_\theta$ varies. The operators compared at matched parameter counts were message-passing graph networks on two neighbourhood graphs, a U-Net, Fourier Neural Operators with and without a local path, and Finite Element Networks with and ..."
- **1.3** [medium] Abstract, paragraph 2 · `00-abstract.tex:35` (today `00-abstract.tex:49`) · **Deferred**: abstract rewritten on 2026-10-02 (review v6); final rewrite with the supervisor's template still to come
  - Issue: The headline metric is not explained, and the next paragraph switches to the label 'change-region Dice' without linking the two.
  - Was: "They were compared by five-fold cross-validation on 75 eyes of 51 patients from the Medical University of Vienna, using the Dice of the changed region at one year."
  - Suggested: "They were compared by five-fold cross-validation on 75 eyes of 51 patients from the Medical University of Vienna, using the change-region Dice at one year, the overlap between the pixels predicted to change and those that changed."
- **1.4** [medium] Abstract, paragraph 3 · `00-abstract.tex:39` · **Deferred**: abstract rewritten on 2026-10-02 (review v6); final rewrite with the supervisor's template still to come
  - Issue: The framework is personified ('served'), the sentence ends in a colon reveal, and 'added about 0.05' has no referent. Placed first, this secondary finding comes before the headline result (see flow notes).
  - Was: "The framework served every operator without change, provided its loss weighted the lesion mask: without that weighting no change was learned, and a soft-Dice term added about 0.05."
  - Suggested: "The framework could be used unchanged for every operator, provided the loss gave extra weight to the lesion mask. Without this weighting no change was learned, and an additional soft-Dice term raised the change-region Dice by about 0.05."
- **1.5** [low] Abstract, paragraph 3 · `00-abstract.tex:45` · **Deferred**: abstract rewritten on 2026-10-02 (review v6); final rewrite with the supervisor's template still to come
  - Issue: 'lies above ... at two seeds' is lab jargon that an abstract reader may not decode.
  - Was: "The Finite Element Network lies above the U-Net at two seeds and only slightly above the graph network."
  - Suggested: "The Finite Element Network scores above the U-Net in runs with two different random seeds and only slightly above the graph network."
- **1.6** [low] Abstract, paragraph 3 · `00-abstract.tex:47` · **Deferred**: abstract rewritten on 2026-10-02 (review v6); final rewrite with the supervisor's template still to come
  - Issue: 'on its own' is filler, and the clipped second sentence reads as a reveal. It is also unclear in what sense a property is 'the largest'.
  - Was: "The differences between operators trace back to a few properties, each measured on its own. The largest is physical reach."
  - Suggested: "The differences between operators trace back to a few properties, each measured separately, of which physical reach has the largest effect."
- **1.7** [low] Abstract, paragraph 3 · `00-abstract.tex:49` · **Deferred**: abstract rewritten on 2026-10-02 (review v6); final rewrite with the supervisor's template still to come
  - Issue: 'index-space neighbour graph' is not explained in the abstract, so the contrast with the dilated stencil is hard to grasp.
  - Was: "Replacing the index-space neighbour graph by a dilated stencil that reaches about 0.12\,mm, roughly as far as the lesion front moves between visits, raises the Dice by 0.064 at an identical parameter count, on all five folds."
  - Suggested: "Replacing the graph network's neighbour graph, built from pixel indices, by a dilated stencil that reaches about 0.12\,mm, roughly as far as the lesion front moves between visits, raises the Dice by 0.064 at an identical parameter count, on all five folds."
- **1.8** [HIGH] Abstract, paragraph 3 · `00-abstract.tex:52` · **Done**: 2026-10-02 (high-severity pass)
  - Issue: 'the same deficit' has no antecedent in the abstract, so the reader cannot tell what is being corrected. 'these two' can be read as the transport term and the network without one instead of the two top operators, and 'the two highest operators' is elliptical. It is also not said which network carries the transport term.
  - Was: "A learned transport term raises it by 0.062 over the same network without one, a second route to the same deficit; these two are the two highest operators."
  - Review suggested: "A learned transport term in the Finite Element Network raises it by 0.062 over the same network without one. Both changes address the same deficit, an update that reaches less far than the lesion front moves between visits. The graph network on the dilated ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **1.9** [low] Abstract, paragraph 3 · `00-abstract.tex:54` · **Deferred**: abstract rewritten on 2026-10-02 (review v6); final rewrite with the supervisor's template still to come
  - Issue: The name changes from 'Fourier Neural Operators with and without a local path' (l. 33) to 'a purely spectral operator', and the tense switches from present to past within the sentence.
  - Was: "A purely spectral operator stays below the U-Net; adding a local path closed the gap at one seed only."
  - Suggested: "The Fourier Neural Operator without a local path stays below the U-Net; adding a local path closes the gap at one seed only."
- **1.10** [medium] Abstract, paragraph 4 · `00-abstract.tex:60` · **Deferred**: abstract rewritten on 2026-10-02 (review v6); final rewrite with the supervisor's template still to come
  - Issue: The sentence compares a rate with 'where the lesion changes', and the double 'with ... with' construction is clumsy.
  - Was: "The growth rate of an individual eye over its whole follow-up is predicted less well than where the lesion changes, with a correlation of 0.40 with the true rates."
  - Suggested: "The growth rate of an individual eye over its whole follow-up is predicted less well than the location of change: predicted and true rates correlate at 0.40."
- **1.11** [medium] Abstract, closing sentence · `00-abstract.tex:62` · **Deferred**: abstract rewritten on 2026-10-02 (review v6); final rewrite with the supervisor's template still to come
  - Issue: This aphoristic closer combines a mirror pair ('how far ... how far') with an 'X, not Y' antithesis, which makes it the most slogan-like sentence of the abstract.
  - Was: "For forecasts of this kind, the decisive design question is how far one update reaches compared with how far the disease moves between visits, not which family the operator belongs to."
  - Suggested: "For forecasts of this kind, the decisive design question is how far one update reaches relative to the distance the lesion front moves between visits; the family to which the operator belongs is secondary."
- **1.12** [medium] §1.1 Clinical Motivation · `01-introduction.tex:17` (today `01-introduction.tex:23`) · **Done**: 2026-10-14 (own wording)
  - Issue: 'Among these' refers to the people counted in the previous sentence, but the subject is a disease stage. The em-dash insertion splits subject from verb.
  - Was: "Among these, the late non-neovascular stage --- termed \emph{Geographic Atrophy} (GA) --- is an advanced, irreversible and progressive atrophy of the macula that causes a marked loss of visual acuity once the fovea is involved \citep{Vallino2024}."
  - Now: "GA causes a marked loss of visual acuity once the fovea, the centre of the macula, is involved \citep{Vallino2024}."
- **1.13** [medium] §1.1 Clinical Motivation · `01-introduction.tex:23` (today `01-introduction.tex:28`) · **Done**: 2026-10-14 (own wording)
  - Issue: 'those that known, cost-effective means can prevent or treat' is a garden-path construction, and 'vision loss' appears twice. The sentence also returns from GA to AMD (see flow notes).
  - Was: "Unlike other eye diseases that cause vision loss, such as cataract, glaucoma or diabetic retinopathy, AMD is not counted among the avoidable causes of vision loss, defined as those that known, cost-effective means can prevent or treat \citep{Flaxman2020}."
  - Now: "Unlike cataract, glaucoma or diabetic retinopathy, AMD is not counted among the avoidable causes of vision loss \citep{Flaxman2020}."
- **1.14** [medium] §1.1 Clinical Motivation · `01-introduction.tex:40` · **Done**: 2026-10-14 (own wording)
  - Issue: The tricolon subject is presented as the cause of patient-to-patient variability, which does not follow from it. The high bilateral concordance reported just before even points the other way.
  - Was: "An ageing population, frequent involvement of both eyes and eventual spread to the fovea make GA a long-term disease that progresses differently in every patient."
  - Review suggested: "An ageing population, frequent involvement of both eyes and eventual spread to the fovea make GA a long-term disease, and its course differs from patient to patient." (the passage was cut or rewritten; no single sentence corresponds today)
- **1.15** [medium] §1.1 Clinical Motivation · `01-introduction.tex:43` (today `01-introduction.tex:47`) · **Done**: 2026-10-14 (own wording)
  - Issue: A 'not whether ... but how/where' antithesis with three italicised words closes the paragraph as a punchline, with the section's second 'therefore'.
  - Was: "The clinically relevant question is therefore not \emph{whether} a patient will deteriorate, but \emph{how fast} and \emph{where} in the macula the lesion will grow."
  - Now: "The clinically relevant question is therefore how fast and where in the macula the lesion will grow."
- **1.16** [low] §1.1 Clinical Motivation · `01-introduction.tex:47` (today `01-introduction.tex:50`) · **Done**: 2026-10-14 (own wording)
  - Issue: 'the therapeutic landscape ... was empty' is a figurative set-up followed by a colon reveal; the plain statement after the colon already says it.
  - Was: "Until 2023, the therapeutic landscape for GA was empty: no treatment was approved, and numerous phase 1--3 trials of GA and intermediate AMD, addressing mechanisms such as neuroprotection, visual cycle modulation, antiamyloid pathways and cell replacement, ..."
  - Now: "Until 2023, no treatment for GA was approved \citep{Trincao2024}, and numerous phase 1--3 trials of GA and intermediate AMD, addressing mechanisms such as neuroprotection, visual cycle modulation, antiamyloid pathways and cell replacement, had failed during the preceding decade \citep{Lad2023}."
- **1.17** [medium] §1.1 Clinical Motivation · `01-introduction.tex:58` (today `01-introduction.tex:63`) · **Decided**: dropped: the supervisor asked to keep this paragraph (SV-1.2 / SV-6.3)
  - Issue: The announcement opener 'is twofold' is followed by a colon reveal, both typical of templated prose.
  - Was: "The clinical implication is twofold. First, treatment timing now matters: an intervention that only slows progression is most valuable when administered before foveal involvement, because central vision is largely preserved until the atrophy reaches the fovea ..."
  - Now: "The clinical implication is twofold."
- **1.18** [low] §1.1 Clinical Motivation · `01-introduction.tex:62` (today `01-introduction.tex:68`) · **Decided**: dropped: the supervisor asked to keep this paragraph (SV-1.2 / SV-6.3)
  - Issue: 'the critical decision support task' is an intensifier on a noun stack, placed at the end of the sentence.
  - Was: "Second, intravitreal injections carry both patient burden and procedural risk, so identifying which eyes will progress rapidly enough to justify therapy is the critical decision support task."
  - Now: "Identifying which eyes will progress rapidly enough to justify therapy is therefore the critical decision-support task."
- **1.19** [medium] §1.1 Clinical Motivation (closing) · `01-introduction.tex:64` (today `01-introduction.tex:73`) · **Decided**: dropped: the supervisor asked to keep this paragraph (SV-1.2 / SV-6.3)
  - Issue: The closer 'pursues that avenue' is a metaphorical one-liner, and it ties the thesis to 'predictive probabilities', which §1.2 sets aside one paragraph later in favour of a lesion map.
  - Was: "As \citet{Vallino2024} note in their conclusions, the integration of artificial intelligence with structural OCT biomarkers holds significant promise, and artificial intelligence applied to OCT has the potential to provide predictive probabilities of GA ..."
  - Now: "As \citet{Vallino2024} note in their conclusions, the integration of artificial intelligence with structural OCT biomarkers holds significant promise."
- **1.20** [low] §1.2 Problem Statement · `01-introduction.tex:75` (today `01-introduction.tex:84`) · **Done**: 2026-10-14 (own wording)
  - Issue: 'naturally' is filler, and 'en-face' is not explained in Chapter 1. OCT is spelled out here although it is already used at l. 35 and l. 66.
  - Was: "Predicting GA progression from imaging is naturally framed as a \emph{spatiotemporal forecasting} task on the en-face projection of optical coherence tomography (OCT) volumes."
  - Now: "Predicting GA progression from imaging is framed as a \emph{spatiotemporal forecasting} task on the en-face (frontal, two-dimensional) projection of OCT volumes."
- **1.21** [medium] §1.2 Problem Statement · `01-introduction.tex:77` (today `01-introduction.tex:90`) · **Done**: 2026-10-14 (own wording)
  - Issue: Two separate ideas (the data and the task) are joined by a semicolon into a 55-word sentence, and 'full spatial configuration' is an abstract noun stack.
  - Was: "For each eye, longitudinal imaging yields a sequence of macula-centred grids on which the lesion outline and the underlying retinal layer geometry are traced; given the most recent observed state and a target horizon $\Delta t$, the goal is to predict the ..."
  - Now: "For each eye, longitudinal imaging yields a sequence of macula-centred grids on which the lesion outline and the depths of the boundaries between the retinal layers are traced."
- **1.22** [low] §1.2 Problem Statement · `01-introduction.tex:81` (today `01-introduction.tex:95`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A 'not X but Y' antithesis. 'next visit' also conflicts with 'future visit' and the target horizon of the previous sentence, which may span several visits.
  - Was: "This differs from earlier work on AMD, which predicts or characterises the conversion of an eye to a later disease stage \citep{SchmidtErfurth2018, Vogl2021}. The output here is not a single risk score but a complete map of the lesion at the next visit."
  - Now: "This differs from earlier work on AMD, which predicts or characterises the conversion of an eye to a later disease stage \citep{SchmidtErfurth2018, Vogl2021}. The output here is a complete map of the lesion at the future visit instead of a single risk score."
- **1.23** [low] §1.2 Problem Statement · `01-introduction.tex:86` (today `02-background.tex:896`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A personified abstraction ('clinical reality ... imposes') ending in the colloquial 'has to deal with'.
  - Was: "The clinical reality of OCT follow-up imposes three properties on the data that a model has to deal with."
  - Now: "Clinical OCT follow-up gives the data three properties that a model must handle."
- **1.24** [medium] §1.2 Problem Statement · `01-introduction.tex:89` (today `02-background.tex:900`) · **Done**: 2026-10-14 (as suggested)
  - Issue: Logic slip: the missing temporal origin rules out a common $t = 0$, but a fixed sampling rate is ruled out by the irregular spacing stated in the previous sentence.
  - Was: "There is no shared temporal origin across eyes, which rules out methods that assume a fixed sampling rate or a common $t = 0$."
  - Now: "Irregular spacing rules out methods that assume a fixed sampling rate, and the lack of a shared temporal origin across eyes rules out methods that assume a common $t = 0$."
- **1.25** [medium] §1.2 Problem Statement · `01-introduction.tex:91` (today `02-background.tex:902`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'naturally' is filler, the 'X ..., while Y ...' pair is balanced, and 'surrounding' is misleading because the layer boundaries do not surround the mask.
  - Was: "Second, the underlying disease state is naturally \emph{multi-channel}: the binary lesion mask captures the GA lesion itself, while the surrounding ten retinal layer boundaries describe the retinal structure in which the atrophy is embedded."
  - Now: "Second, the disease state is \emph{multi-channel}: a binary mask marks the GA lesion, and ten retinal layer boundaries describe the retinal structure in which the atrophy lies."
- **1.26** [low] §1.2 Problem Statement · `01-introduction.tex:95` (today `02-background.tex:905`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The reason given justifies the layer channels, not 'both' sources. 'RPE' is used without being spelled out in Chapter 1.
  - Was: "Both information sources are relevant because prognostic biomarkers documented in the clinical literature, such as RPE--Bruch's-membrane thickening \citep{Chu2022} and thinning of the outer retinal layers \citep{Vallino2024}, are not contained in the lesion ..."
  - Now: "The layer channels are relevant because prognostic biomarkers documented in the clinical literature, such as RPE--Bruch's-membrane thickening \citep{Chu2022} and thinning of the outer retinal layers \citep{Vallino2024}, are not contained in the lesion mask alone. (Spell out 'retinal pigment epithelium (RPE)' at this ..."
- **1.27** [HIGH] §1.2 Problem Statement (covariates) · `01-introduction.tex:98` · **Done**: 2026-10-02 (high-severity pass)
  - Issue: The sentence promises a test that the rendered thesis does not report. The covariate subsection of Chapter 5 is inside \iffalse (05-experiments.tex l. 1094-1159), and §6.3 says their value 'is not settled'. A reader will look for the result and not find it. 'carries covariates' is jargon, and the semicolon chain joins separate points.
  - Was: "Third, every patient carries \emph{covariates}, in particular age and sex. Age is strongly associated with the risk of developing the disease (\S\ref{sec:introduction:motivation}), and the evidence on sex is mixed; whether either also helps to forecast where ..."
  - Review suggested: "Third, each patient has \emph{covariates}, in particular age and sex. Age is strongly associated with the risk of developing the disease (\S\ref{sec:introduction:motivation}), and the evidence on sex is mixed. Whether either also helps to forecast where and ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **1.28** [low] §1.2 Problem Statement · `01-introduction.tex:104` (today `02-background.tex:915`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'requirements' re-labels what the previous paragraph called 'properties', which blurs the antecedent.
  - Was: "Meeting these requirements is not only a question of the model itself but also of how the model is used."
  - Now: "Handling these properties depends on the model and on how it is used."
- **1.29** [medium] §1.2 Problem Statement · `01-introduction.tex:107` (today `02-background.tex:917`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'These properties' now means the model's missing abilities (elapsed time, stepping), although the same word meant the data properties one paragraph earlier. The appended 'one that ...' apposition is a recurring tell.
  - Was: "These properties have to come from a framework around the model, one that conditions the prediction on $\Delta t$ and rolls the state forward visit by visit."
  - Now: "Both abilities have to be supplied by a framework around the model that conditions the prediction on $\Delta t$ and advances the state from one visit to the next."
- **1.30** [medium] §1.2 Problem Statement (closing) · `01-introduction.tex:109` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: The announcement does not match §1.3, which first argues that GA growth is local and PDE-like, an argument about the operator. The short closing sentence works as a cliff-hanger.
  - Was: "The next section motivates such a framework, which borrows several of its techniques from neural partial differential equation (PDE) solvers. Which model should sit inside it is a separate question."
  - Review suggested: "The next section motivates such a framework, which borrows several of its techniques from neural partial differential equation (PDE) solvers, and explains why the choice of the model inside it is treated as a separate question." (the passage was cut or rewritten; no single sentence corresponds today)
- **1.31** [medium] §1.3 Why Neural PDE Solvers? · `01-introduction.tex:119` (today `02-background.tex:926`) · **Done**: 2026-10-14 (as suggested)
  - Issue: One sentence carries the finding, its interpretation, the notation and the equation, and continues with two more clauses after the equation (about 100 words). The reader loses the main clause.
  - Was: "\citet{Yehoshua2011} found that the enlargement rate of the square root of the lesion area does not depend on the baseline lesion size, which is what is expected if the radius of a GA lesion grows at a roughly constant rate while its enclosed area scales ..."
  - Now: "\citet{Yehoshua2011} found that the enlargement rate of the square root of the lesion area does not depend on the baseline lesion size. This is what is expected if the radius of a GA lesion grows at a roughly constant rate while its enclosed area scales quadratically. With $A(t)$ the lesion area and $r(t)$ an ..."
- **1.32** [medium] §1.3 Why Neural PDE Solvers? · `01-introduction.tex:135` (today `02-background.tex:942`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'structural fingerprint' is a dramatic metaphor in a paragraph closer, and 'This' is vague. The PDE acronym is already introduced at l. 111.
  - Was: "This is the structural fingerprint of a system governed by a temporal partial differential equation with strong spatial localisation."
  - Now: "Such behaviour is characteristic of a system governed by a temporal PDE with strong spatial localisation."
- **1.33** [medium] §1.3 Why Neural PDE Solvers? · `01-introduction.tex:140` (today `02-background.tex:947`) · **Done**: 2026-10-14 (as suggested)
  - Issue: Three different kinds of finding share one list, with a tense shift. 'peak progression rate occurs ... when the lesion grows foveally' is hard to parse, and the treatment effect is a different kind of fact from natural growth.
  - Was: "GA growth is \emph{anisotropic}: lesions progress faster towards the retinal periphery than towards the fovea, peak progression rate occurs at approximately one millimetre from the foveal centre when the lesion grows foveally, and in eyes treated monthly with ..."
  - Now: "GA growth is \emph{anisotropic}: lesions progress faster towards the retinal periphery than towards the fovea, and growth towards the fovea peaks at approximately one millimetre from the foveal centre \citep{Singh2025}. In eyes treated monthly with pegcetacoplan, progression towards the fovea was slowed more than ..."
- **1.34** [medium] §1.3 Why Neural PDE Solvers? · `01-introduction.tex:145` (today `02-background.tex:951`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The em-dash appendage ('--- properties that ...') tacks a second idea onto an already long sentence, and 'stencil' is used without explanation in Chapter 1.
  - Was: "The forward operator that maps the present state to the future state is therefore \emph{local}, but its reach must match the distance the front moves between two visits, which differs between directions --- properties that classical solvers build in ..."
  - Now: "The forward operator that maps the present state to the future state is therefore \emph{local}, but its reach must match the distance the front moves between two visits, and this distance differs between directions. Classical solvers build such properties in explicitly through the size and shape of their stencils, the ..."
- **1.35** [low] §1.3 Why Neural PDE Solvers? · `01-introduction.tex:152` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: The comma-enclosed 'and the time that elapses' interrupts the main clause.
  - Was: "Instead of discretising a known equation, they learn from data an operator that maps the current state of a system, and the time that elapses, to its next state."
  - Review suggested: "Instead of discretising a known equation, they learn from data an operator that maps the current state of a system and the elapsed time to its next state." (the passage was cut or rewritten; no single sentence corresponds today)
- **1.36** [medium] §1.3 Why Neural PDE Solvers? · `01-introduction.tex:162` (today `01-introduction.tex:106`) · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: 'the two' follows a list of three candidates (operator, size, setup), so it is unclear what is separated. 'actually' is filler.
  - Was: "Which of them GA progression actually requires cannot be decided by testing a single architecture: if one model succeeds, the reason may be its operator, its size, or the setup around it. This thesis therefore separates the two."
  - Now: "Which of them GA progression requires cannot be decided by testing a single architecture: if one model succeeds, the reason may be its operator, its size, or the setup around it."
- **1.37** [medium] §1.3 Why Neural PDE Solvers? · `01-introduction.tex:165` (today `01-introduction.tex:110`) · **Done**: 2026-10-14 (own wording)
  - Issue: An em-dash-enclosed tricolon splits subject and verb, and the closing clause restates the point in mirrored form.
  - Was: "The setup --- how elapsed time enters the prediction, how models are trained and how they are evaluated --- is fixed once, and the operator is the only part that changes."
  - Now: "The setup comprises how elapsed time enters the prediction and how models are trained and evaluated."
- **1.38** [medium] §1.3 Why Neural PDE Solvers? · `01-introduction.tex:168` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: This 55-word sentence repeats the contrast with earlier clinical work from §1.2 (l. 81-84) and interrupts the step from the framework/operator separation to the research question.
  - Was: "In contrast to clinical work based on cohort-level statistical atlases and time-to-conversion survival models \citep{Vogl2021} and on biomarker-based risk analyses \citep{Vallino2024}, every model in this comparison forecasts the lesion of an individual eye ..."
  - Review suggested: "Consider moving the contrast to the end of the first paragraph of §1.2 (after l. 84), where earlier work is first contrasted, with 'every model in this comparison' changed to 'the models of this thesis' and the citations unchanged. Keep in §1.3 only: ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **1.39** [medium] §1.3, research question · `01-introduction.tex:189` · **Done**: 2026-10-14 (own wording)
  - Issue: The two sentences form a mirror pair, and the first repeats almost verbatim the definition of the setup given a few lines earlier (l. 165-166).
  - Was: "The first part concerns everything that surrounds the model: how irregular visit intervals enter the prediction, and how models are trained and evaluated. The second concerns the model itself, the operator that maps one visit to the next."
  - Review suggested: "The first part refers to the setup described above, and the second to the operator that maps one visit to the next." (the passage was cut or rewritten; no single sentence corresponds today)
- **1.40** [medium] §1.3, contributions paragraph · `01-introduction.tex:197` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: A pseudo-cleft announcement in business register ('What the thesis delivers follows from ...') precedes the actual content.
  - Was: "What the thesis delivers follows from this design. It provides a $\Delta t$-conditioned framework for irregular visit schedules in which operators from unrelated literatures can be compared on equal terms, and a controlled comparison of several operator ..."
  - Review suggested: "The thesis contributes a $\Delta t$-conditioned framework for irregular visit schedules, in which operators from unrelated literatures can be compared on equal terms, and a controlled comparison of several operator classes on longitudinal OCT for GA." (the passage was cut or rewritten; no single sentence corresponds today)
- **1.41** [HIGH] §1.3, contributions paragraph · `01-introduction.tex:201` (today `01-introduction.tex:162`) · **Done**: 2026-10-02 (high-severity pass)
  - Issue: 'the same deficit' is never named in the chapter, and the 'moving-mesh extension' appears here without explanation. The em-dash-enclosed list and the idiom 'in their own right' add to the machine-like rhythm.
  - Was: "It identifies physical reach at the scale of the lesion front and an explicit transport term as two independent routes to the same deficit, and it reports what did not help --- larger models, a higher integration order, a monotonic-growth penalty and a ..."
  - Now: "\item Results on what did not help: larger models, a higher integration order, a monotonic-growth penalty and an extension with an adaptive moving mesh."
- **1.42** [low] §1.4 Thesis Outline · `01-introduction.tex:219` (today `01-introduction.tex:182`) · **Done**: 2026-10-14 (as suggested)
  - Issue: This repeats l. 192-195 closely, and 'on equal terms' appears here for the third time in the chapter.
  - Was: "Chapter~\ref{ch:method} addresses the first part of the research question by developing the framework, and describes the models that fill its one free component. Chapter~\ref{ch:experiments} addresses the second part by comparing these models on equal terms."
  - Now: "Chapter~\ref{ch:method} addresses the first part of the research question by developing the framework, and describes the models that fill its one free component. Chapter~\ref{ch:experiments} addresses the second part by comparing these models."
- **1.43** [low] §1.4 Thesis Outline · `01-introduction.tex:225` (today `01-introduction.tex:188`) · **Done**: as suggested
  - Issue: The thesis has several appendices, so 'The appendix' is ambiguous. This sentence is also the reader's first explanation of the 'moving-mesh extension' named in the contributions paragraph.
  - Was: "The appendix reports an additional experiment with an adaptive moving mesh."
  - Now: "Appendix~\ref{app:mm-pde} reports an additional experiment with an adaptive moving mesh."

## Chapter 2, medical background (§2.1)

Source: `reviews/editorial-2026-10-01/02a-background-ga-oct.md`.

- **2a.1** [medium] §2.1 Geographic Atrophy and OCT Imaging (introduction) · `02-background.tex:11` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: A 120-word meta paragraph built on four mirrored emphasised clauses ('on which ..., on how ..., on what ..., on which ...') with filler ('deliberately self-contained', 'imaging substrate'). A second roadmap follows at l. 131-138, where 'actually' is conversational and the description of §2.1.4 ('the projection from 3D OCT volume to the 2D en-face grid') does not match §2.1.4, which says no projection is computed.
  - Was: "This section provides the imaging-side background needed to motivate the state representation used throughout the remainder of the thesis. The clinical framing established in Chapter~\ref{ch:introduction} is taken as read; the focus here is on \emph{which ..."
  - Review suggested: "This section gives the imaging background for the state representation used in the rest of the thesis and builds on the clinical context of Chapter~\ref{ch:introduction}. It describes which part of the eye GA affects, how that part is imaged, what is visible ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.2** [medium] Figure 2.1 caption · `02-background.tex:64` · **Done**: 2026-10-14 (own wording)
  - Issue: The caption names three sub-zones, while the body text (l. 96-100) names four (foveola, fovea, parafovea, perifovea). Most of the rest of the caption repeats the body text.
  - Was: "The fovea sits roughly at the centre of the macula; the macula itself is sub-divided into the foveola (innermost), parafovea, and perifovea, in concentric rings of increasing radius."
  - Review suggested: "The fovea sits roughly at the centre of the macula, which is sub-divided into concentric zones of increasing radius: the foveola, fovea, parafovea and perifovea." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.3** [medium] §2.1.1 A short anatomy primer · `02-background.tex:74` (today `02-background.tex:64`) · **Done**: 2026-10-14 (as suggested)
  - Issue: An informal analogy that the paragraph never uses again; the author's style rules exclude informal analogies.
  - Was: "The eye, sketched in Figure~\ref{fig:bg:eye-anatomy} (left), can be thought of as a biological camera."
  - Now: "Figure~\ref{fig:bg:eye-anatomy} (left) shows the eye in cross-section."
- **2a.4** [medium] §2.1.1 A short anatomy primer · `02-background.tex:82` (today `02-background.tex:74`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A 35-word em-dash aside, containing two nested parentheticals, separates subject and verb.
  - Was: "Behind the retina, two further layers --- the \emph{choroid} (a richly vascularised tissue, of which the \emph{choriocapillaris} is the innermost capillary bed) and the \emph{sclera} (the white, mechanically rigid outer shell) --- support and supply the ..."
  - Now: "Behind the retina lie two further layers that support and supply it from beneath: the \emph{choroid}, a richly vascularised tissue whose innermost capillary bed is the \emph{choriocapillaris}, and the \emph{sclera}, the white, mechanically rigid outer shell."
- **2a.5** [low] §2.1.1 A short anatomy primer · `02-background.tex:91` (today `02-background.tex:84`) · **Done**: 2026-10-14 (as suggested)
  - Issue: Emphatic 'ever', and a long semicolon join of a fact and its consequence.
  - Was: "The macula has a diameter of roughly five to six millimetres and is the only part of the retina that GA ever affects clinically; for that reason, the OCT scanning window used throughout the thesis is centred on the macula and covers a $6 \times 6$\,mm field ..."
  - Now: "The macula has a diameter of roughly five to six millimetres and is the only part of the retina that GA affects clinically. The OCT scanning window used throughout the thesis is therefore centred on the macula and covers a $6 \times 6$\,mm field (\S\ref{sec:background:ga-oct:muw})."
- **2a.6** [low] §2.1.1 A short anatomy primer · `02-background.tex:112` (today `02-background.tex:104`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A colon reveal introduced by an 'X rather than Y' contrast, with the slightly writerly 'piece of anatomy'.
  - Was: "A second piece of anatomy is internal rather than positional: the retina is itself a \emph{layered} tissue, with several distinct strata stacked vertically from the front (closest to the vitreous body) to the back (closest to the choroid)."
  - Now: "The retina is also a \emph{layered} tissue, with several distinct strata stacked vertically from the front (closest to the vitreous body) to the back (closest to the choroid)."
- **2a.7** [HIGH] §2.1.1 A short anatomy primer · `02-background.tex:122` · **Done**: 2026-10-02 (high-severity pass)
  - Issue: 'Takes some getting used to' is a conversational idiom, and 'is what feeds' is a pseudo-cleft. 'Three of those layers' does not match the list just given, because the choriocapillaris (l. 187) is not in it.
  - Was: "The terminology in this list takes some getting used to, but for the purposes of this thesis it is sufficient to remember the structural fact that the retina is layered, that GA destroys a specific \emph{outer}-retinal stack of three of those layers ..."
  - Review suggested: "For the purposes of this thesis, it suffices to note that the retina is layered, that GA destroys a specific \emph{outer}-retinal stack of three layers (\S\ref{sec:background:ga-oct:disease}), and that the surrounding layer geometry, given as ten boundary ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.8** [medium] Figure 2.2 caption · `02-background.tex:169` · **Done**: 2026-10-14 (own wording)
  - Issue: The caption maps the named strata onto the ten channels, while §2.1.5 (l. 422) deliberately says only that the boundaries are ordered from superficial to deep. The roughly eight named strata also do not visibly add up to ten boundaries.
  - Was: "The same set of anatomical strata corresponds to the ten layer-boundary channels of the eleven-channel state tensor introduced in \S\ref{sec:background:ga-oct:state-rep}."
  - Review suggested: "Author to decide; a wording consistent with §2.1.5 would be: 'The ten layer-boundary channels of the state tensor (\S\ref{sec:background:ga-oct:state-rep}) record the depths of boundaries between strata of this kind, ordered from superficial to deep.'" (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.9** [medium] §2.1.2 Geographic Atrophy on OCT · `02-background.tex:181` · **Done**: 2026-10-14 (own wording)
  - Issue: This is the third definition of the retina in the section; it repeats l. 77-79 and l. 112-114, which appear a page earlier.
  - Was: "The retina is a thin, layered tissue at the back of the eye that converts incoming light into neural signals; Figure~\ref{fig:bg:retinal-anatomy} (left) sketches its principal anatomical strata in the macula."
  - Review suggested: "Figure~\ref{fig:bg:retinal-anatomy} (left) sketches the principal anatomical strata of the retina in the macula." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.10** [medium] §2.1.2 Geographic Atrophy on OCT · `02-background.tex:184` (today `02-background.tex:319`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A 40-word em-dash list separates subject and verb, 'RPE' is repeated three times inside it, and 'a stack ... die' is awkward in number.
  - Was: "Geographic atrophy is the disease in which a stack of three tightly coupled \emph{outer}-retinal layers --- the retinal pigment epithelium (RPE), the photoreceptor outer segments that sit just above the RPE, and the choriocapillaris (a dense capillary bed) ..."
  - Now: "Geographic atrophy is the disease in which three tightly coupled \emph{outer}-retinal layers die together in a localised patch of the macula: the retinal pigment epithelium (RPE), the photoreceptor outer segments just above it, and the choriocapillaris, a dense capillary bed immediately below it ..."
- **2a.11** [low] §2.1.2 Geographic Atrophy on OCT · `02-background.tex:191` · **Done**: 2026-10-14 (own wording)
  - Issue: 'In other words' announces a restatement, but the sentence states a consequence of the preceding one.
  - Was: "In other words, atrophy of one layer entrains the degeneration of the others, so the resulting lesion appears on imaging as a sharply delineated patch in which the entire outer-retinal complex is missing rather than as the loss of a single isolated layer."
  - Review suggested: "Atrophy of one layer therefore entrains the degeneration of the others, and the resulting lesion appears on imaging as a sharply delineated patch in which the entire outer-retinal complex is missing rather than as the loss of a single isolated layer." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.12** [low] §2.1.2 Geographic Atrophy on OCT · `02-background.tex:197` (today `02-background.tex:332`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A pseudo-cleft opening with a long clausal subject delays the agent.
  - Was: "What this end-stage lesion looks like on OCT has been formalised by an international consensus group, the Classification of Atrophy Meetings (CAM), under the term \emph{complete RPE and outer retinal atrophy} (cRORA) \citep{Sadda2018, Vallino2024}."
  - Now: "An international consensus group, the Classification of Atrophy Meetings (CAM), has formalised the OCT appearance of this end-stage lesion under the term \emph{complete RPE and outer retinal atrophy} (cRORA) \citep{Sadda2018, Vallino2024}."
- **2a.13** [medium] §2.1.2 Geographic Atrophy on OCT · `02-background.tex:205` (today `02-background.tex:340`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'Put differently' announces a restatement, but the sentence adds new information. 'Precisely' is an intensifier on the author's exclusion list.
  - Was: "Put differently, cRORA is the OCT-readable definition of an established atrophic lesion, which can arise with or without macular neovascularisation (the wet form of AMD), and \emph{GA is precisely the subset of cRORA that arises in eyes without macular ..."
  - Now: "cRORA is thus the OCT-readable definition of an established atrophic lesion, which can arise with or without macular neovascularisation (the wet form of AMD), and \emph{GA is the subset of cRORA that arises in eyes without macular neovascularisation}."
- **2a.14** [medium] §2.1.2 Geographic Atrophy on OCT · `02-background.tex:208` (today `02-background.tex:343`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A 70-word sentence with a double gloss ('essentially ... i.e.'), and a semicolon that joins a definition to a separate study result.
  - Was: "The CAM framework also recognises a precursor stage, \emph{iRORA} (incomplete RPE and outer retinal atrophy), which is essentially the same lesion at a smaller spatial scale, i.e.\ the same OCT pattern below the 250\,\textmu{}m size threshold; in one ..."
  - Now: "The CAM framework also recognises a precursor stage, \emph{iRORA} (incomplete RPE and outer retinal atrophy), which shows the same OCT pattern below the 250\,\textmu{}m size threshold. In one retrospective study of intermediate-AMD eyes, 93\,\% of iRORA lesions progressed to cRORA within twenty-four months, with a ..."
- **2a.15** [medium] §2.1.2 Geographic Atrophy on OCT · `02-background.tex:220` (today `02-background.tex:358`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A metaphor ('visual fingerprints') inside an em-dash aside restates 'signatures', followed by an 'are the following' reveal.
  - Was: "The principal direct OCT signatures of an established GA lesion --- the visual fingerprints by which the disease is identified on a B-scan --- are the following \citep{Boopathiraj2024,Yehoshua2011,Vallino2024}."
  - Now: "An established GA lesion is identified on a B-scan by three principal direct OCT signatures \citep{Boopathiraj2024,Yehoshua2011,Vallino2024}."
- **2a.16** [medium] §2.1.2 Geographic Atrophy on OCT · `02-background.tex:233` (today `02-background.tex:370`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A ~70-word sentence whose em-dash aside ('essentially, ...') restates the main clause in lay terms, which is overly explanatory.
  - Was: "\emph{(iii)} \emph{RPE--Bruch's-membrane (BM) thickening} is concentrated immediately around the lesion margin --- essentially, the narrow ring of tissue just outside the lesion is measurably thicker than tissue further from the lesion --- and is thought to ..."
  - Now: "\emph{(iii)} \emph{RPE--Bruch's-membrane (BM) thickening} is concentrated in a narrow rim just outside the lesion margin and is thought to reflect, at least in part, basal-laminar deposits accumulated in the diseased tissue; the thickness of this rim correlates significantly with the eye's subsequent annual ..."
- **2a.17** [HIGH] §2.1.2 Geographic Atrophy on OCT · `02-background.tex:240` · **Done**: 2026-10-02 (high-severity pass)
  - Issue: The sentence says the channel-0 mask is defined by these OCT signatures, but §3.1 (03-data.tex l. 50) states 'The GA mask was not segmented on the OCT', so a reader meets a contradiction. It is also a symmetric 'first two ...; the third ...' pair that closes on 'rather than'.
  - Was: "The first two signatures define the lesion mask used as channel~0 of the state tensor; the third is a boundary-localised predictive biomarker that motivates encoding the surrounding layer geometry rather than the mask alone."
  - Review suggested: "Author to check against §3.1. A wording that does not state the provenance: 'The first two signatures delineate the lesion itself. The third is a predictive biomarker located at the lesion boundary and motivates encoding the surrounding layer geometry in ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.18** [medium] Figure 2.3 caption · `02-background.tex:296` · **Done**: 2026-10-14 (own wording)
  - Issue: The caption says the pipeline operates on a projected intensity image. §2.1.4 (l. 375-379) states that no projection is computed and that the models receive a mask and depth maps on the en-face grid.
  - Was: "\emph{(d)} Projecting the volume along its axial direction onto the fundus plane yields the two-dimensional en-face image on which the modelling pipeline operates (\S\ref{sec:background:ga-oct:enface}); a GA lesion appears inside the en-face image as a region ..."
  - Review suggested: "\emph{(d)} Projecting the volume along its axial direction onto the fundus plane yields a two-dimensional en-face image, in which a GA lesion appears as a region with a different signal intensity than the surrounding healthy retina. The modelling pipeline ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.19** [low] §2.1.3 Optical Coherence Tomography of the Macula · `02-background.tex:305` (today `02-background.tex:163`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A conversational comparison ('in much the same way') that ends in an em-dash 'except that' twist.
  - Was: "Optical Coherence Tomography (OCT), introduced by \citet{Huang1991}, produces micrometre-resolution cross-sectional images of the retina, in much the same way that ultrasound produces them for soft tissue --- except that low-coherence near-infrared light ..."
  - Now: "Optical Coherence Tomography (OCT), introduced by \citet{Huang1991}, produces micrometre-resolution cross-sectional images of the retina. The principle is analogous to ultrasound imaging of soft tissue, with low-coherence near-infrared light in place of sound."
- **2a.20** [medium] §2.1.3 Optical Coherence Tomography of the Macula · `02-background.tex:308` (today `02-background.tex:166`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The body text never names this profile an A-scan, yet l. 326 ('recovers the A-scan') and l. 328 ('A single A-scan is ...') use the term as if it had been defined. 'Concretely' and 'shines' are conversational.
  - Was: "Concretely, the system shines a weak probe beam into the eye and measures how strongly each \emph{depth} along the path of the beam reflects light back. That depth-versus-reflectivity profile is then displayed as a single column of pixels in the output image, ..."
  - Now: "A weak probe beam is directed into the eye, and the strength of the light reflected back from each \emph{depth} along its path is measured. This depth-versus-reflectivity profile is called an \emph{A-scan}; it is displayed as a single column of pixels, with intensity encoding reflectivity and vertical position ..."
- **2a.21** [low] §2.1.3 Optical Coherence Tomography of the Macula · `02-background.tex:313` (today `02-background.tex:171`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'A small piece of optical engineering' is a conversational understatement.
  - Was: "Resolving the depth dimension requires a small piece of optical engineering, because near-infrared light from a single short pulse cannot be timed precisely enough on a per-layer basis with conventional electronics."
  - Now: "Resolving the depth dimension requires an optical technique, because conventional electronics cannot time near-infrared light from a single short pulse precisely enough to separate individual layers."
- **2a.22** [medium] §2.1.3 Optical Coherence Tomography of the Macula · `02-background.tex:317` (today `02-background.tex:174`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A colon reveal followed by two mirrored em-dash asides ('one of which --- ... --- while the other --- ... ---') in a single sentence.
  - Was: "The standard solution is interferometric: the source light is split into two beams (Figure~\ref{fig:bg:oct-acquisition}(a)), one of which --- the \emph{sample arm} --- is sent into the eye and reflected back from the various retinal layers, while the other ..."
  - Now: "The standard solution is interferometry. The source light is split into two beams (Figure~\ref{fig:bg:oct-acquisition}(a)): the \emph{sample arm} is sent into the eye and reflected back from the various retinal layers, and the \emph{reference arm} is sent to a known mirror and reflected back unchanged."
- **2a.23** [medium] §2.1.3 Optical Coherence Tomography of the Macula · `02-background.tex:335` (today `02-background.tex:191`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The forward pointer says §2.1.4 explains how the native grids are reduced to the modelling grid, but §2.1.4 says no projection is computed and the crop/pad reduction is in §3.3. The heavy subject ('how ... is the subject of') also delays the point.
  - Was: "The MUW cohort uses an acquisition protocol that produces volumes with a physical footprint of approximately $6 \times 6$\,mm laterally; how the varying native voxel grids are reduced to the standard two-dimensional modelling grid used in the rest of the ..."
  - Now: "The MUW cohort uses an acquisition protocol that produces volumes with a lateral footprint of approximately $6 \times 6$\,mm. How such a volume is summarised as a two-dimensional en-face image is described in~\S\ref{sec:background:ga-oct:enface}, and how the varying native grids are brought to one modelling grid ..."
- **2a.24** [low] §2.1.3 Optical Coherence Tomography of the Macula · `02-background.tex:345` (today `02-background.tex:239`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'Struggles' personifies the modality and is colloquial.
  - Was: "and it remains reliable near the fovea, where blue-light FAF struggles."
  - Now: "and it remains reliable near the fovea, where blue-light FAF is less reliable."
- **2a.25** [medium] §2.1.3 Optical Coherence Tomography of the Macula · `02-background.tex:359` · **Done**: 2026-10-14 (own wording)
  - Issue: An aphoristic four-word closer that repeats the paragraph's opening sentence (l. 352) and introduces an undefined notion ('fusion'). It also reads oddly against §3.1, where the mask is an FAF outline registered to the OCT grid.
  - Was: "No cross-modality fusion is required."
  - Review suggested: "Delete the sentence; the opening sentence of the paragraph ('A single OCT volume shows both the lesion and the retinal layers around it.') already makes the point." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.26** [low] §2.1.4 From OCT volumes to en-face projections · `02-background.tex:364` (today `02-background.tex:259`) · **Done**: 2026-10-02 (as suggested)
  - Issue: 'Therefore' presents model tractability as the reason the clinical literature uses en-face images. The cited clinical studies do not model progression, so the causal link reads as an unsupported inference.
  - Was: "The full OCT volume of a GA eye is too large and too redundant to be modelled at native voxel resolution. The clinical literature therefore works with an \emph{en-face} image instead: a two-dimensional map of the retina seen from the front, as in a fundus ..."
  - Now: "The full OCT volume of a GA eye is too large and too redundant to be modelled at native voxel resolution. The clinical literature works with an \emph{en-face} image instead: a two-dimensional map of the retina seen from the front, as in a fundus photograph, in which every pixel corresponds to one A-scan of the volume ..."
- **2a.27** [medium] §2.1.4 From OCT volumes to en-face projections · `02-background.tex:381` (today `02-background.tex:349`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The preceding paragraph says the data arrive as en-face maps and no projection is computed, so calling this a motivated 'choice' reads oddly. 'Methodologically important', 'in fact' and 'substrate' are filler or jargon.
  - Was: "The choice of en-face rather than B-scan as the modelling substrate is motivated by a methodologically important caveat documented by \citet{Vallino2024}: a lesion classified as iRORA on a single horizontal B-scan can in fact be part of a larger cRORA lesion ..."
  - Now: "Working on en-face maps rather than on single B-scans is also supported by a caveat documented by \citet{Vallino2024}: a lesion classified as iRORA on a single horizontal B-scan can be part of a larger cRORA lesion that is fully visible only in the en-face slab."
- **2a.28** [low] §2.1.4 From OCT volumes to en-face projections · `02-background.tex:388` (today `02-background.tex:278`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'By construction' is a stock opener, and 'per-step ... per-step' is repetitive.
  - Was: "By construction, the 2D en-face grid also reduces a per-step three-dimensional forward problem to a per-step two-dimensional one, which matters for the tractability of the models introduced in the subsequent chapters."
  - Now: "The en-face grid also reduces the forward problem of each step from three dimensions to two, which matters for the tractability of the models in the following chapters."
- **2a.29** [low] §2.1.5 The eleven-channel state representation · `02-background.tex:396` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: A paragraph-opening announcement built on an emphasised what/why pair. 'Operational details' recurs at l. 490.
  - Was: "This subsection describes \emph{what} the eleven channels of the state tensor are, in structural terms, and \emph{why} retaining all of them is clinically motivated. The operational details of how the channels were produced in the MUW cohort are deferred ..."
  - Review suggested: "The eleven channels of the state tensor are described here in structural terms, together with the clinical reason for retaining all of them. How the channels were produced in the MUW cohort is stated in~\S\ref{sec:data:dataset}; the rest of this chapter does ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.30** [medium] §2.1.5 The eleven-channel state representation · `02-background.tex:414` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: The same definition is given twice, first via 'the underlying OCT B-scan' and then, after 'Concretely', via the A-scan. The change of reference object is confusing.
  - Was: "The remaining ten channels are \emph{retinal layer boundary depth maps}: at every pixel of the en-face grid, the value of channel $c \in \{1, \dots, 10\}$ is the axial position of one anatomical layer boundary in the underlying OCT B-scan. Concretely, fixing ..."
  - Review suggested: "The remaining ten channels are \emph{retinal layer boundary depth maps}. Each pixel of the en-face grid corresponds to one A-scan of the OCT volume, and the value of channel $c \in \{1, \dots, 10\}$ at that pixel is the depth along this A-scan at which the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.31** [low] §2.1.5 The eleven-channel state representation · `02-background.tex:425` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: A heavy 'The motivation for X is that Y' frame and the personification 'biomarkers ... live'.
  - Was: "The clinical motivation for retaining all ten layer-boundary channels alongside the binary mask is that documented prognostic biomarkers for GA progression live throughout the full vertical retinal column, not only inside the lesion itself."
  - Review suggested: "All ten layer-boundary channels are retained alongside the binary mask because documented prognostic biomarkers for GA progression are found throughout the full vertical retinal column, not only inside the lesion itself." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.32** [medium] §2.1.5 The eleven-channel state representation · `02-background.tex:428` · **Done**: 2026-10-14 (own wording)
  - Issue: An ~80-word semicolon list covering three separate studies. The first clause reintroduces signature (iii) from l. 233 as if it were new.
  - Was: "RPE--Bruch's-membrane thickening at the 0--300\,\textmu{}m rim around the GA boundary correlates with annual square-root enlargement rate at $r = 0.595$ \citep{Chu2022}; outer retinal layer thinning, in particular of the outer nuclear layer and of the ..."
  - Review suggested: "At the 0--300\,\textmu{}m rim around the GA boundary, the RPE--Bruch's-membrane thickening of signature~(iii) correlates with the annual square-root enlargement rate at $r = 0.595$ \citep{Chu2022}. Outer retinal layer thinning, in particular of the outer ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.33** [medium] §2.1.5 The eleven-channel state representation · `02-background.tex:440` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: An aphoristic 'not X; Y' paragraph closer that restates the paragraph as a contrast.
  - Was: "The layer channels are therefore not auxiliary context; they carry rate-of-change information that the mask alone cannot provide."
  - Review suggested: "The layer channels therefore carry rate-of-change information that the mask alone cannot provide." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.34** [low] §2.1.6 The MUW longitudinal GA cohort · `02-background.tex:451` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: The relative clause 'which in the MUW study of ... was' reads as if Mai et al. identified the device used for this cohort. §3.1 (03-data.tex l. 26) says Mai et al. describe 'a larger GA cohort from the same MUW clinic'.
  - Was: "The cohort comprises 553 volume scans over 75 eyes, acquired with a Heidelberg Engineering device, which in the MUW study of \citet{Mai2024} was a Spectralis spectral-domain OCT."
  - Review suggested: "The cohort comprises 553 volume scans over 75 eyes, acquired with a Heidelberg Engineering device; for a larger GA cohort of the same clinic, \citet{Mai2024} report a Spectralis spectral-domain OCT." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.35** [medium] §2.1.6 The MUW longitudinal GA cohort · `02-background.tex:453` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: From here to l. 484, §2.1.6 repeats §3.1 (grid shapes, 03-data.tex l. 65-66) and §3.3 (spacing, crop/pad and the censoring census, l. 193-219) almost figure for figure, so the reader meets the same numbers twice within about fifteen pages.
  - Was: "Lateral pixel counts vary per eye across the 553 visits, ranging from 38 to 66 B-scans by 961 to 1719 A-scans, giving 67 distinct native shapes in total."
  - Review suggested: "Keep only the literature precedent for the 6 mm window and a short pointer in §2.1.6, e.g. 'The native grids differ between eyes and are brought to one $49 \times 1024$ modelling grid by centre-crop or zero-pad (\S\ref{sec:data:spatial}); the pixel spacing, ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.36** [medium] §2.1.6 The MUW longitudinal GA cohort · `02-background.tex:458` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: 'This is an assumption' follows the window sentence, so 'This' appears to refer to the window, not to the constant spacing.
  - Was: "Pixel spacing is treated as constant across the cohort at approximately $[0.12118,\, 0.003867,\, 0.00568]$\,mm in the $(x, z, y)$ directions, because the scans were resampled upstream to one gold-standard spacing. The resulting fixed physical window is ..."
  - Review suggested: "Pixel spacing is treated as constant across the cohort at approximately $[0.12118,\, 0.003867,\, 0.00568]$\,mm in the $(x, z, y)$ directions, because the scans were resampled upstream to one gold-standard spacing; the limits of this assumption are stated ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.37** [medium] §2.1.6 The MUW longitudinal GA cohort · `02-background.tex:476` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: 'This window' points back to the literature's $6 \times 6$ mm acquisition window. What actually cuts lesion area is this thesis's fixed modelling window, obtained by crop or pad.
  - Was: "However, measured on the present cohort, this window is not lossless."
  - Review suggested: "However, measured on the present cohort, the fixed $5.94 \times 5.82$\,mm modelling window of this thesis is not lossless." (the passage was cut or rewritten; no single sentence corresponds today)
- **2a.38** [low] §2.1.6 The MUW longitudinal GA cohort · `02-background.tex:488` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: An unnecessary em-dash aside, and 'the operational details of how ...' (also at l. 398) is wordy.
  - Was: "Patient-level covariates --- in particular age and biological sex --- accompany the imaging sequence; the operational details of how they are extracted and encoded are described in~\S\ref{sec:data:covariates}."
  - Review suggested: "Patient-level covariates, in particular age and biological sex, accompany the imaging sequence; their extraction and encoding are described in~\S\ref{sec:data:covariates}." (the passage was cut or rewritten; no single sentence corresponds today)

## Chapter 2, solvers, neural solvers, related work (§2.2-§2.5)

Source: `reviews/editorial-2026-10-01/02b-background-solvers-related-work.md`.

- **2b.1** [medium] §2.2 Partial Differential Equations and Numerical Solvers (intro) · `02-background.tex:502` (today `02-background.tex:379`) · **Done**: 2026-10-02 (one-word pass)
  - Issue: 'a local update rule' presents locality as a premise of the approach. §2.2.5 (l.789-791), however, states that whether a local stencil, a global operator or both is needed is 'not assumed here', and global operators (FNO) are part of the survey. Pseudospectral solvers (l.603-609) are not local either.
  - Was: "The approach of this thesis treats GA progression the way a numerical solver treats a partial differential equation (PDE): the state is held on a grid and advanced step by step by a local update rule."
  - Now: "The models in this thesis are built like numerical solvers for partial differential equations (PDEs): a state is held on a grid and advanced step by step by an update rule."
- **2b.2** [low] §2.2 Partial Differential Equations and Numerical Solvers (intro) · `02-background.tex:505` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: 'exactly those' is emphatic filler typical of generated announcements, and the gerund subject 'Understanding ... requires' is heavy.
  - Was: "Understanding the framework of Chapter~\ref{ch:method} and the models of Chapter~\ref{ch:experiments} therefore requires only a few solver mechanisms, and this section introduces exactly those."
  - Review suggested: "Only a few solver mechanisms are needed to follow the framework of Chapter~\ref{ch:method} and the models of Chapter~\ref{ch:experiments}; this section introduces them." (the passage was cut or rewritten; no single sentence corresponds today)
- **2b.3** [low] §2.2 Partial Differential Equations and Numerical Solvers (intro) · `02-background.tex:528` (today `02-background.tex:407`) · **Done**: 2026-10-14 (as suggested)
  - Issue: Pseudo-cleft ('This X is what Y exploit'), a construction that recurs in the chapter. The plain subject-verb form is shorter.
  - Was: "This locality is what the stencils of \S\ref{sec:background:pde-solvers:stencils} exploit."
  - Now: "The stencils of \S\ref{sec:background:pde-solvers:stencils} exploit this locality."
- **2b.4** [low] §2.2 Partial Differential Equations and Numerical Solvers (intro) · `02-background.tex:532` (today `02-background.tex:411`) · **Done**: 2026-10-14 (sentence kept; moved or its context changed)
  - Issue: This repeats the roadmap given six lines earlier (l.507-513) with the same two cross-references, so the reader meets the same plan twice in consecutive paragraphs. Merging the two sentences reduces the repetition.
  - Was: "Closed-form solutions exist only in special cases, so the solution is computed numerically. A numerical solver does this in two steps: it replaces the continuous domain by a grid and the spatial derivatives by operations on grid values ..."
  - Now: "Closed-form solutions exist only in special cases, so the solution is computed numerically."
- **2b.5** [low] §2.2.1 Discretising space: stencils · `02-background.tex:548` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: 'with the particularity that' is stiff and non-idiomatic.
  - Was: "The en-face grid of this thesis is of that type, with the particularity that the two spacings differ by a factor of about twenty (\S\ref{sec:data:spatial})."
  - Review suggested: "The en-face grid of this thesis is a uniform grid whose two spacings differ by a factor of about twenty (\S\ref{sec:data:spatial})." (the passage was cut or rewritten; no single sentence corresponds today)
- **2b.6** [low] §2.2.1 Finite differences and finite volumes · `02-background.tex:561` (today `02-background.tex:441`) · **Decided**: declined by the author (2026-10-14)
  - Issue: $n$ is defined at l.524 as the number of components of $u$, but here it denotes the derivative order (also in $\alpha_j^{(n)}$ and in $(i\omega)^n$ at l.605). A careful reader may stumble over the clash.
  - Was: "In general, the $n$-th derivative at cell $i$ is estimated as a weighted sum over a small neighbourhood $\mathcal{N}(i)$,"
  - Now: "In general, the $n$-th derivative at cell $i$ is estimated as a weighted sum over a small neighbourhood $\mathcal{N}(i)$, \left[\partial_x^{(n)} u\right]_i \;\approx\; \sum_{j \in \mathcal{N}(i)} \alpha_j^{(n)} u_j ,"
- **2b.7** [low] §2.2.1 Adaptive stencils · `02-background.tex:595` (today `02-background.tex:477`) · **Done**: 2026-10-14 (as suggested)
  - Issue: One sentence of about 45 words carries three steps (candidate estimates, smoothness weights, the effect at the front). Splitting it makes the mechanism easier to follow.
  - Was: "Weighted essentially non-oscillatory (WENO) schemes avoid this by computing several candidate estimates on shifted sub-stencils and combining them with weights that depend on how smooth the data are in each sub-stencil, so that sub-stencils crossing the front ..."
  - Now: "Weighted essentially non-oscillatory (WENO) schemes avoid this by computing several candidate estimates on shifted sub-stencils. The estimates are combined with weights that depend on how smooth the data are in each sub-stencil, so that sub-stencils crossing the front receive almost no weight \citep{Liu1994, ..."
- **2b.8** [low] §2.2.1 Adaptive stencils · `02-background.tex:599` (today `02-background.tex:481`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The short closing sentence works as an aphoristic paragraph ending, and its subject 'This' has a vague referent. Folding it into the previous sentence names the mechanism.
  - Was: "The stencil thereby becomes a non-linear function of its input. This is the mechanism closest to what a learned operator does."
  - Now: "The stencil thereby becomes a non-linear function of its input, which makes WENO the classical mechanism closest to what a learned operator does."
- **2b.9** [low] §2.2.1 Global methods · `02-background.tex:604` (today `02-background.tex:486`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'instead' has no explicit referent. The preceding paragraph is about WENO, and the intended contrast is with all the neighbourhood-based stencils.
  - Was: "Pseudospectral methods compute derivatives in Fourier space instead: the field is transformed, each mode is multiplied by $(i\omega)^n$, and the result is transformed back."
  - Now: "Pseudospectral methods compute derivatives in Fourier space instead of from a neighbourhood: the field is transformed, each mode is multiplied by $(i\omega)^n$, and the result is transformed back."
- **2b.10** [medium] §2.2.1 Locality and reach · `02-background.tex:614` (today `02-background.tex:496`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The paragraph is titled 'Locality and reach', but 'reach' is never defined. Later chapters build on 'physical reach at lesion scale', and l.663 and l.894 already use the word, so the term should be fixed here on first use.
  - Was: "How far that is in physical units is set by the width of the stencil and by the grid spacing."
  - Now: "This distance, the \emph{reach} of the stencil, is set in physical units by the width of the stencil and by the grid spacing."
- **2b.11** [medium] §2.2.2 Stepping in time · `02-background.tex:622` (today `02-background.tex:505`) · **Done**: 2026-10-14 (as suggested)
  - Issue: This nearly repeats the definition of $f$ at l.571-572 and pads it with a transition sentence ('The spatial part of the problem is then settled, and the remaining task is ...'). The redundancy is noticeable and reads as generated.
  - Was: "Once every spatial derivative is replaced by a stencil, the solver is left with a function $f$ that maps the current grid values to a rate of change for every cell. The spatial part of the problem is then settled, and the remaining task is to advance the grid ..."
  - Now: "The stencils of \S\ref{sec:background:pde-solvers:stencils} reduce the spatial part of the problem to the rate function $f$; the grid then has to be advanced in time with this rate."
- **2b.12** [low] §2.2.2 Stepping in time · `02-background.tex:655` (today `02-background.tex:537`) · **Done**: 2026-10-14 (as suggested)
  - Issue: In the clause after the semicolon, the name 'residual form' can attach to the property instead of to the form of the update. Naming the form first reads more naturally and removes the stock 'by construction'.
  - Was: "An update written as the current state plus $\Delta t$ times a rate, as in~\eqref{eq:bg:euler}, returns the current state at $\Delta t = 0$ by construction; this is called the \emph{residual} form."
  - Now: "An update written as the current state plus $\Delta t$ times a rate, as in~\eqref{eq:bg:euler}, is said to be in \emph{residual} form; it returns the current state at $\Delta t = 0$ whatever the rate."
- **2b.13** [low] §2.2.2 Stepping in time · `02-background.tex:669` (today `02-background.tex:551`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'Seen the other way round' is a conversational idiom, and the sentence is an equivalent restatement of the CFL condition.
  - Was: "Seen the other way round, a stencil used with a given step must be wide enough to cover the distance the solution moves during that step."
  - Now: "Equivalently, a stencil used with a given step must be wide enough to cover the distance the solution moves during that step."
- **2b.14** [medium] §2.2.3 Strengths and limits · `02-background.tex:702` (today `02-background.tex:596`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A colon reveal ending in the punchline 'and nothing else' gives the sentence a rhetorical, aphoristic finish.
  - Was: "Their limits follow from the same design. The equation $F$ must be known, including its coefficients: the solver computes what $F$ prescribes and nothing else."
  - Now: "Their limits follow from the same design. The equation $F$, including its coefficients, must be known, because the solver can only compute what $F$ prescribes."
- **2b.15** [medium] §2.2.3 Strengths and limits · `02-background.tex:708` (today `02-background.tex:602`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The sentence opens with 'And' and continues with a colon reveal, which gives it a conversational, slogan-like rhythm.
  - Was: "And accuracy is expensive: fine features need fine grids, the CFL condition then forces small steps, and the cost grows faster than the resolution."
  - Now: "Accuracy is also expensive. Fine features need fine grids, the CFL condition then forces small time steps, and the cost grows faster than the resolution."
- **2b.16** [low] §2.2.4 Neural solvers that keep the mechanisms · `02-background.tex:727` (today `02-background.tex:627`) · **Done**: 2026-10-14 (as suggested)
  - Issue: Two separate examples are joined into one long sentence of about 45 words. The second carries its own claim and reads better on its own.
  - Was: "Graph neural networks built this way simulate fluids, deformable materials and cloth \citep{SanchezGonzalez2020, Pfaff2021}, and a graph-network weather forecaster trained on decades of reanalysis data outperforms a leading operational numerical model on most ..."
  - Now: "Graph neural networks built this way simulate fluids, deformable materials and cloth \citep{SanchezGonzalez2020, Pfaff2021}. A graph-network weather forecaster trained on decades of reanalysis data outperforms a leading operational numerical model on most of its verification targets \citep{Lam2023}."
- **2b.17** [low] §2.2.4 Neural solvers that keep the mechanisms · `02-background.tex:733` (today `02-background.tex:633`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The antecedent of 'the correspondence' sits two sentences back, before the weather-forecasting example, so on first reading it is unclear what corresponds to what.
  - Was: "The message-passing solver of \citet{Brandstetter2022} (MP-PDE) makes the correspondence explicit."
  - Now: "The message-passing solver of \citet{Brandstetter2022} (MP-PDE) makes the correspondence between message passing and a classical stencil explicit."
- **2b.18** [medium] §2.2.4 Neural solvers that keep the mechanisms · `02-background.tex:736` (today `02-background.tex:637`) · **Done**: 2026-10-14 (own wording)
  - Issue: An em-dash appositive delivers the punchline, one of the clearest structural tells in the range. 'their differences to its own' also leaves 'own' without its noun.
  - Was: "One round of message passing computes, at every node, a learned function of its neighbours' values and their differences to its own --- a learned, non-linear stencil."
  - Now: "One round of message passing computes, at every node, a learned function of its neighbours' values and of their differences to its own value; it thus acts as a learned, non-linear stencil (Figure~\ref{fig:bg:solver-path}, panel~4)."
- **2b.19** [medium] §2.2.4 Neural solvers that keep the mechanisms · `02-background.tex:745` (today `02-background.tex:647`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The mirrored pseudo-cleft pair ('What X gains is ... What it loses are ...') is a typical symmetrical structure of generated text. The first sentence is also overloaded (a colon plus two coordinated clauses).
  - Was: "What the learned version gains is that $f$ no longer has to be written down: it is fitted to data, so the solver can be used where the equation is expensive to solve, known only approximately, or not known at all, and it can often run on coarser grids with ..."
  - Now: "A learned solver does not require $f$ to be written down. Because $f$ is fitted to data, the solver can be used where the equation is expensive to solve, known only approximately, or unknown, and it can often run on coarser grids with larger steps. In exchange, the classical guarantees are lost."
- **2b.20** [medium] §2.2.5 Why this structure suits GA progression · `02-background.tex:758` (today `02-background.tex:959`) · **Done**: 2026-10-14 (as suggested)
  - Issue: Three consecutive sentences contain an antithesis ('not X but Y'), the conversational 'not an option' and a trailing cleft ('which is why the thesis adopts it').
  - Was: "GA progression has no known governing equation. Its data are not a densely simulated trajectory but a few observed states per eye (\S\ref{sec:background:ga-oct:muw}). A classical solver is therefore not an option, but the structure it is built from matches ..."
  - Now: "GA progression has no known governing equation, and its data are a few observed states per eye (\S\ref{sec:background:ga-oct:muw}) instead of a densely simulated trajectory. A classical solver therefore cannot be used. The structure such a solver is built from, however, matches the problem in four respects, and the ..."
- **2b.21** [medium] §2.2.5 Why this structure suits GA progression (bullet: Change driven by the neighbourhood) · `02-background.tex:771` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: The em-dash closes the bullet with a slogan-like fragment.
  - Was: "Whether a pixel becomes atrophic depends on what surrounds it --- the situation a stencil is designed for."
  - Review suggested: "Whether a pixel becomes atrophic depends on what surrounds it, and a stencil is designed for this situation." (the passage was cut or rewritten; no single sentence corresponds today)
- **2b.22** [low] §2.2.5 Why this structure suits GA progression (bullet: Slow change) · `02-background.tex:775` (today `02-background.tex:975`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'starts from the right default' is vague and informal; the reader has to infer that the default is the unchanged state and why it is 'right'.
  - Was: "The residual form, which predicts only the change and returns the current state as $\Delta t \to 0$, starts from the right default."
  - Now: "The residual form predicts only the change and returns the current state as $\Delta t \to 0$; its default, the unchanged state, suits data that change slowly."
- **2b.23** [low] §2.2.5 Why this structure suits GA progression (bullet: Irregular steps) · `02-background.tex:779` (today `02-background.tex:979`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'naturally' is filler, and 'the real interval' is slightly loose.
  - Was: "A solver step is naturally parameterised by $\Delta t$, so the step can be the real interval rather than a fixed one."
  - Now: "A solver step is parameterised by $\Delta t$, so each step can use the actual interval between two visits instead of a fixed one."
- **2b.24** [low] §2.2.5 Why this structure suits GA progression · `02-background.tex:784` (today `02-background.tex:995`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A balanced aphoristic antithesis ('X, not Y') used as a paragraph opener and closer. The hedge itself is correct and must stay.
  - Was: "These are reasons to expect the structure to fit, not evidence that it does."
  - Now: "These four points motivate the structure but are not evidence that it fits."
- **2b.25** [medium] §2.2.5 Why this structure suits GA progression · `02-background.tex:786` (today `02-background.tex:997`) · **Done**: 2026-10-14 (as suggested)
  - Issue: This is a long two-part sentence, and 'that distance is very different when counted in pixels along each axis' is awkward. The key point, that the pixel counts differ between the two axes, needs its own sentence.
  - Was: "The CFL argument suggests that an operator applied once per visit has to see at least as far as the lesion front moves between visits, and on the anisotropic en-face grid that distance is very different when counted in pixels along each axis."
  - Now: "The CFL argument suggests that an operator applied once per visit has to see at least as far as the lesion front moves between visits. On the anisotropic en-face grid, this distance corresponds to very different numbers of pixels along the two axes."
- **2b.26** [low] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:799` (today `02-background.tex:656`) · **Done**: 2026-10-14 (own wording)
  - Issue: 'paradigms' is inflated, 'any arbitrary' is redundant, and the participial tail 'thereby predicting' is a common generated pattern. $\mathcal{F}$ is also used without definition.
  - Was: "Neural PDE solvers broadly separate into two paradigms. Neural operators learn a continuous map $M: [0, T] \times \mathcal{F} \to \mathcal{F}$ such that $M(t, u_0) = u(t)$, thereby predicting the solution at any arbitrary time directly from the initial ..."
  - Now: "Learned solvers also differ in what they predict, and in this respect they separate into two paradigms."
- **2b.27** [medium] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:806` (today `02-background.tex:664`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'Note that' is a meta-instruction to the reader, and 'fundamentally' is an intensifier (one of four in this range).
  - Was: "Note that when the step size $\Delta t$ is fixed by the dataset, the explicit dependence on it is usually suppressed in the notation. This thesis cannot suppress it because clinical observation intervals are fundamentally irregular."
  - Now: "When the step size $\Delta t$ is fixed by the dataset, the dependence on it is usually omitted from the notation. Here it cannot be omitted, because the intervals between clinical visits are irregular."
- **2b.28** [medium] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:811` (today `02-background.tex:668`) · **Done**: 2026-10-14 (as suggested)
  - Issue: Five uniformly short sentences, an empty opening announcement ('take several structural forms'), a mirrored pair ('Finite-dimensional variants ... Infinite-dimensional variants ...') and the intensifier 'altogether' together give a clearly robotic rhythm.
  - Was: "Neural operators take several structural forms. Finite-dimensional variants are bound to the specific grid geometry they were trained on. Infinite-dimensional variants decouple the learned operator from the spatial discretisation altogether. The Fourier ..."
  - Now: "Finite-dimensional neural operators are bound to the grid geometry they were trained on, whereas infinite-dimensional ones are defined independently of the spatial discretisation. The Fourier Neural Operator \citep{Li2021} parameterises a kernel integral operator in the Fourier domain, which gives the network global ..."
- **2b.29** [medium] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:818` (today `02-background.tex:673`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'Alternatively' is a weak connector, and 'A standard limitation applies' sets up a colon reveal. 'inherently' is an intensifier, and 'reliably poor' is an odd collocation, since 'reliably' normally carries a positive sense.
  - Was: "Alternatively, DeepONet \citep{Lu2021} factorises the operator into a branch network that encodes the input function and a trunk network that encodes the continuous query coordinate. A standard limitation applies to both variants: the trained operator is ..."
  - Now: "DeepONet \citep{Lu2021} instead factorises the operator into a branch network that encodes the input function and a trunk network that encodes the continuous query coordinate. Both share a well-known limitation: a trained operator is tied to the equation family it was trained on, and its extrapolation beyond the ..."
- **2b.30** [medium] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:825` (today `02-background.tex:680`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The paragraph is a 'Furthermore ... Finally' enumeration with no 'first', built on inflated verbs ('fundamentally constitutes', 'necessitates', 'dictates'). GPTZero judged the first two sentences human and the enumerated tail AI.
  - Was: "The autoregressive framing is the natural fit for clinical longitudinal data. Each visit-to-visit transition fundamentally constitutes one step. Furthermore, there is no shared temporal origin ($t = 0$) across patients, making a direct time-dependent mapping ..."
  - Now: "The autoregressive framing is the natural fit for clinical longitudinal data. Each visit-to-visit transition constitutes one step. Since there is no shared temporal origin ($t = 0$) across patients, a direct time-dependent mapping is ill-posed. In addition, the prediction horizon is set by the clinic rather than by ..."
- **2b.31** [medium] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:834` (today `02-background.tex:687`) · **Done**: 2026-10-14 (own wording)
  - Issue: The paragraph introduces error accumulation as new, although §2.2.4 (l.749-753) already explained it and pointed here. 'at test time' may also confuse readers in a thesis that states it has no test split; 'during a rollout' is the intended meaning.
  - Was: "The principal cost of the autoregressive framing is error accumulation. After the first step, the solver consumes its own output rather than numerical ground truth. The input distribution at test time therefore differs systematically from the distribution ..."
  - Now: "The principal cost of this framing is the error accumulation noted at the start of this section: after the first step, the solver consumes its own output instead of numerical ground truth, so the inputs it receives during a rollout differ systematically from those seen in training."
- **2b.32** [low] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:841` (today `02-background.tex:694`) · **Done**: 2026-10-14 (own wording)
  - Issue: 'against it' points back across a paragraph break, and 'together with their message-passing solver' sits awkwardly at the end of the sentence.
  - Was: "\citet{Brandstetter2022} propose two mechanisms against it together with their message-passing solver (\S\ref{sec:background:pde-solvers:neural})."
  - Now: "Together with their message-passing solver, introduced above, \citet{Brandstetter2022} propose two mechanisms against this distribution shift."
- **2b.33** [low] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:854` (today `02-background.tex:708`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'pushes the constant down' is informal and produces an unintended echo of 'pushforward'.
  - Was: "An update operator is zero-stable if a small perturbation of its input changes the output only by a bounded multiple, $\lVert \mathcal{A}(u^0 + \epsilon) - u^1 \rVert \leq \kappa \lVert \epsilon \rVert$, and the pushforward loss pushes the constant $\kappa$ ..."
  - Now: "An update operator is zero-stable if a small perturbation of its input changes the output only by a bounded multiple, $\lVert \mathcal{A}(u^0 + \epsilon) - u^1 \rVert \leq \kappa \lVert \epsilon \rVert$, and the pushforward loss reduces the constant $\kappa$."
- **2b.34** [medium] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:861` (today `02-background.tex:715`) · **Done**: 2026-10-14 (as suggested)
  - Issue: After a paragraph on consistency and zero stability, 'the two mechanisms' can be misread as those two properties. 'uses' also implies that both temporal bundling and the pushforward trick are used, but Chapter 4 removes bundling (04-method.tex l.436). A neutral verb avoids the misreading without previewing the decision.
  - Was: "Chapter~\ref{ch:method} describes how the framework of this thesis uses the two mechanisms."
  - Now: "Chapter~\ref{ch:method} describes how the framework of this thesis treats temporal bundling and the pushforward trick."
- **2b.35** [medium] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:871` (today `02-background.tex:725`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'vary fundamentally' and 'contrast directly' are filler. The second sentence names a contrast without saying what it is, so 'combine these properties' is vague.
  - Was: "Surrogate architectures also vary fundamentally in their spatial context. Global spectral operators, such as the Fourier Neural Operator, contrast directly with local convolutional or message-passing operators. Hybrid architectures combine these properties by ..."
  - Now: "The architectures also differ in their spatial context: global spectral operators such as the Fourier Neural Operator couple all grid points within one layer, whereas convolutional and message-passing operators are local. Hybrid architectures add a small local kernel bypass to a global operator to capture ..."
- **2b.36** [medium] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:878` (today `02-background.tex:732`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'adopt a different numerical perspective' is an empty abstract phrase. It is followed by a chain of two participles with an inserted qualifier, a typical generated sentence shape.
  - Was: "Finite Element Networks \citep{Lienen2022} adopt a different numerical perspective, building the neural update directly from a finite-element discretisation with learned dynamics and, in their transport variant, carrying an explicit transport (advection) term."
  - Now: "Finite Element Networks \citep{Lienen2022} build the neural update directly from a finite-element discretisation with learned dynamics, and their transport variant carries an explicit transport (advection) term."
- **2b.37** [HIGH] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:882` (today `02-background.tex:735`) · **Done**: 2026-10-02 (high-severity pass)
  - Issue: 'It must be stated plainly that' is a dramatic meta-statement, and 'must ... must' repeats in consecutive sentences. 'A Neural-ODE reading' is used without saying what it is; the plain explanation only appears in Related Work (l.956-957).
  - Was: "Finally, because a residual step resembles one explicit Euler step, a Neural-ODE reading is sometimes applied \citep{Chen2018}. Under this interpretation, a higher-order integrator such as a Runge--Kutta scheme can in principle replace the residual step. It ..."
  - Now: "Finally, because a residual step resembles one explicit Euler step, the network is sometimes read as the right-hand side of an ordinary differential equation, the Neural-ODE reading \citep{Chen2018}."
- **2b.38** [medium] §2.3 Neural PDE Solvers and Surrogate Architectures · `02-background.tex:892` (today `02-background.tex:745`) · **Done**: 2026-10-14 (as suggested)
  - Issue: An announcement sentence, then 'The primary distinctions lie in', then a four-part 'whether ... whether' list form a symmetrical, generated pattern. 'Inductive bias' first appears here in the rendered text of Chapters 1-2 and is not explained; Chapter 1 (l.155) calls the same idea 'built-in assumptions'.
  - Was: "These architecture families differ in a small number of structural properties. The primary distinctions lie in whether the operator has spatial context at all, how far that context physically reaches, whether it combines global and local information, and ..."
  - Now: "The architecture families differ mainly in four structural properties: whether the operator has spatial context at all, how far that context physically reaches, whether it combines global and local information, and whether it carries an explicit transport term. Such built-in assumptions of a model are called its ..."
- **2b.39** [medium] §2.4 Related Work · `02-background.tex:904` · **Done**: 2026-10-14 (own wording)
  - Issue: The noun stack can be misparsed as 'OCT-based age-related macular degeneration' (the disease is not OCT-based), and the opening sentence of the section is hard to read in one pass.
  - Was: "Learning-based models for OCT-based age-related macular degeneration and geographic atrophy progression divide broadly into cohort-level risk models and spatial-progression models."
  - Review suggested: "Learning-based models of AMD and GA progression on OCT fall broadly into cohort-level risk models and spatial-progression models." (the passage was cut or rewritten; no single sentence corresponds today)
- **2b.40** [low] §2.4 Related Work · `02-background.tex:911` (today `02-background.tex:782`) · **Done**: 2026-10-14 (as suggested)
  - Issue: A long fronted prepositional phrase ends in 'it', which the reader has to resolve back to the start of the sentence.
  - Was: "For the conversion of intermediate AMD to macular atrophy or neovascularisation, \citet{Vogl2021} provided a topographic analysis of the retinal and choroidal layer changes that precede it."
  - Now: "\citet{Vogl2021} provided a topographic analysis of the retinal and choroidal layer changes that precede the conversion of intermediate AMD to macular atrophy or neovascularisation."
- **2b.41** [medium] §2.4 Related Work · `02-background.tex:914` (today `02-background.tex:784`) · **Done**: 2026-10-14 (own wording)
  - Issue: A trailing 'which positions X as Y' clause adds an editorial conclusion in jargon ('candidate predictive substrate for structural endpoints'), a recognisable generated tail.
  - Was: "\citet{Vallino2024} noted that artificial intelligence applied to OCT has the potential to provide predictive probabilities of GA development over time, which positions OCT as a candidate predictive substrate for structural endpoints."
  - Now: "\citet{Vallino2024} noted that artificial intelligence applied to OCT has the potential to provide predictive probabilities of GA development over time."
- **2b.42** [medium] §2.4 Related Work · `02-background.tex:924` (today `02-background.tex:821`) · **Done**: 2026-10-14 (own wording)
  - Issue: 'fundamentally' is an intensifier, 'While ..., the present thesis consumes ...' is a symmetrical contrast, and 'must be kept in mind' reads as an instruction to the reader. The caveat itself has to stay with full weight.
  - Was: "The input regime, however, is fundamentally different. While that prior work operates directly on raw OCT volumes, the present thesis consumes pre-segmented lesion masks and layer surfaces. This difference must be kept in mind whenever the approaches are ..."
  - Now: "The input regime, however, is different."
- **2b.43** [low] §2.4 Related Work · `02-background.tex:929` (today `02-background.tex:824`) · **Done**: 2026-10-14 (own wording)
  - Issue: The trailing appositive 'a multi-scale spatial approach on an alternative modality' is loosely attached and could refer either to the images or to the U-Net.
  - Was: "As a precedent for dense convolutional architectures on this task, \citet{Salvi2025} predicted future GA growth using a two-dimensional U-Net on fundus autofluorescence images, a multi-scale spatial approach on an alternative modality."
  - Now: "As a precedent for dense convolutional architectures on this task, \citet{Salvi2025} predicted future GA growth with a two-dimensional U-Net on fundus autofluorescence images."
- **2b.44** [HIGH] §2.4 Related Work · `02-background.tex:934` (today `02-background.tex:834`) · **Done**: 2026-10-02 (high-severity pass)
  - Issue: This is the most generated-sounding passage in the range: a 'By contrast ... Consequently' connective chain, a stacked three-adjective list, the vague verb 'dictates' and the stock phrase 'sits at the intersection of'. Its placement after the Mai and Salvi paragraph is a separate flow issue (see flow_notes).
  - Was: "The prevailing formulation in the clinical literature rests on cohort-level, categorical, time-to-conversion prediction. By contrast, the formulation used here dictates a per-eye, per-time-step prediction of the full spatial next state. Consequently, this ..."
  - Now: "Most of the clinical literature formulates prediction at cohort level, as a categorical time-to-conversion problem."
- **2b.45** [low] §2.4 Related Work · `02-background.tex:946` · **Done**: 2026-10-14 (own wording)
  - Issue: 'operator slot' first appears here in the rendered text of Chapters 1-3 (grep). Chapter 1 only says that 'the operator is the only part that changes', so the jargon term arrives without introduction.
  - Was: "The architectures that fill the operator slot of Chapter~\ref{ch:method} originate in different lines of work."
  - Review suggested: "The architectures used as the exchangeable operator of the framework in Chapter~\ref{ch:method} originate in different lines of work." (the passage was cut or rewritten; no single sentence corresponds today)
- **2b.46** [low] §2.4 Related Work · `02-background.tex:950` · **Done**: 2026-10-14 (own wording)
  - Issue: This repeats §2.3 (l.866-869, where the U-Net's origin in segmentation is already stated), so the reader meets the same fact twice within two pages.
  - Was: "The U-Net was introduced by \citet{Ronneberger2015} for biomedical image segmentation, the Fourier Neural Operator by \citet{Li2021}, and its extension with local kernels by \citet{LiuSchiaffini2024}."
  - Review suggested: "The U-Net was introduced by \citet{Ronneberger2015}, the Fourier Neural Operator by \citet{Li2021}, and its extension with local kernels by \citet{LiuSchiaffini2024}." (the passage was cut or rewritten; no single sentence corresponds today)

## Chapter 3

Source: `reviews/editorial-2026-10-01/03-data.md`.

- **3.1** [low] §3.1 Dataset · `03-data.tex:11` (today `03-data.tex:26`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'The data ... is a ... cohort' equates the data with the cohort. 'clinical practice at a single clinical site' repeats 'clinical'.
  - Was: "The data used in this thesis is a longitudinal cohort of eyes with Geographic Atrophy, provided by the Medical University of Vienna (MUW). It was acquired in routine clinical practice at a single clinical site in Vienna."
  - Now: "The data used in this thesis comes from a longitudinal cohort of eyes with Geographic Atrophy and was provided by the Medical University of Vienna (MUW). It was acquired in routine clinical practice at a single site in Vienna."
- **3.2** [medium] §3.1 Dataset · `03-data.tex:26` (today `03-data.tex:42`) · **Done**: 2026-10-14 (own wording)
  - Issue: 'it' can be read as the present data instead of Mai's cohort, which would turn an inference (the device TODO at l.28) into a stated fact. The relative clause 'who describe a larger GA cohort from the same ... clinic' recurs almost verbatim at l.51 and reads formulaic.
  - Was: "\citet{Mai2024}, who describe a larger GA cohort from the same MUW clinic, report that it was acquired on a Spectralis device."
  - Now: "For this cohort, \citet{Mai2024} report acquisition on a Spectralis device."
- **3.3** [low] §3.1 Dataset · `03-data.tex:34` (today `03-data.tex:48`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The closing antithesis 'not hand-entered integers' answers a question the reader has not asked and reads like a data-cleaning note. It is one of several X-not-Y closers in the chapter.
  - Was: "Ages are decimal values computed from the date of birth to the baseline visit, not hand-entered integers."
  - Now: "Ages are decimal values, computed from the date of birth to the baseline visit."
- **3.4** [low] §3.1 Dataset · `03-data.tex:37` (today `03-data.tex:51`) · **Done**: 2026-10-14 (as suggested)
  - Issue: Chapter 2 uses 'derivative' throughout for spatial derivatives (FDM, stencils), so 'en-face derivatives' can be misread. The intended meaning is 'maps derived from the volume'.
  - Was: "The data does not contain the raw three-dimensional OCT volumes. Instead, each visit provides a set of registered two-dimensional en-face derivatives."
  - Now: "The data does not contain the raw three-dimensional OCT volumes. Instead, each visit provides a set of registered two-dimensional en-face maps derived from them."
- **3.5** [medium] §3.1 Dataset · `03-data.tex:42` (today `03-data.tex:56`) · **Done**: 2026-10-14 (as suggested)
  - Issue: 'Each visit further provides a GA mask' comes right after the mask was introduced as 'The first' file, so it reads like a duplicate entry. The reader has to work out that this is a second mask in another frame. 'are required' does not say what requires them.
  - Was: "Each visit further provides a GA mask, a scanning laser ophthalmoscopy (SLO) fundus image and a fundus-autofluorescence image, all in the SLO reference frame, together with two files of coordinate transforms between the OCT and the SLO frame. Only the ..."
  - Now: "Each visit further provides a scanning laser ophthalmoscopy (SLO) fundus image, a fundus-autofluorescence image and a second GA mask, all three in the SLO reference frame, together with two files of coordinate transforms between the OCT and the SLO frame. Only the OCT-grid mask and the layer array are required by the ..."
- **3.6** [medium] §3.1 Dataset · `03-data.tex:50` (today `03-data.tex:65`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The reader has just read 'a binary GA mask on the native OCT en-face grid', and the flat opener seems to contradict it without saying so. The next sentence repeats the relative clause from l.26 word for word.
  - Was: "The GA mask was not segmented on the OCT. \citet{Mai2024}, who describe a larger GA cohort from the same clinic, report that GA was outlined manually on the fundus-autofluorescence image by certified graders of the Vienna Reading Center, as well-demarcated ..."
  - Now: "Although it is stored on the OCT grid, the GA mask was not segmented on the OCT. For the larger cohort from the same clinic, \citet{Mai2024} report that GA was outlined manually on the fundus-autofluorescence image by certified graders of the Vienna Reading Center, as well-demarcated areas of markedly decreased or ..."
- **3.7** [low] §3.1 Dataset · `03-data.tex:57` · **Done**: 2026-10-14 (own wording)
  - Issue: 'The data agree' is plural, while the chapter treats 'data' as singular elsewhere ('The data does not contain', 'The data is partitioned'). 'agree with this' is also vague about what is compared.
  - Was: "The data agree with this: the OCT-grid mask coincides with the SLO-frame mask mapped through the recorded transform, with an intersection over union of at least 0.9995 on all 553 visits."
  - Review suggested: "The stored files are consistent with this: the OCT-grid mask coincides with the SLO-frame mask mapped through the recorded transform, with an intersection over union of at least 0.9995 on all 553 visits." (the passage was cut or rewritten; no single sentence corresponds today)
- **3.8** [medium] §3.1 Dataset · `03-data.tex:65` (today `03-data.tex:81`) · **Done**: 2026-10-14 (as suggested)
  - Issue: In this thesis 'uniform grid' has a technical sense (uniform spacing, as opposed to a moved mesh), so 'not uniform' suggests non-uniform pixel spacing. The paragraph then says the opposite: spacing is constant and only the sizes differ.
  - Was: "The native en-face grids are not uniform."
  - Now: "The native en-face grids do not all have the same size."
- **3.9** [low] §3.1 Dataset · `03-data.tex:69` (today `03-data.tex:85`) · **Done**: 2026-10-14 (own wording)
  - Issue: In a clinical thesis 'gold-standard' usually means a ground-truth reference, which is misleading for a resampling target. The last sentence puts a parenthetical ('and with them ...') inside a contrast clause.
  - Was: "Upstream of this work, the stored en-face arrays were resampled onto one gold-standard pixel spacing: 0.12118\,mm between B-scans, 0.00568\,mm between A-scans, and 0.003867\,mm per axial pixel. Pixel spacing is therefore treated as constant across the cohort, ..."
  - Now: "Upstream of this work, the stored en-face arrays were resampled onto one common pixel spacing: 121.18\,\textmu{}m between B-scans, 5.68\,\textmu{}m between A-scans, and 3.867\,\textmu{}m per axial pixel."
- **3.10** [medium] §3.1 Dataset · `03-data.tex:82` (today `03-data.tex:98`) · **Done**: 2026-10-14 (as suggested)
  - Issue: The 'square-root-area growth rate' quoted in the next sentence is never described in plain words, and the author asks for every measure to be explained on first use. 'This transform is used for GA, because' has an unneeded comma and a vague 'is used'.
  - Was: "Lesion growth is summarised on the square-root area scale. This transform is used for GA, because it removes the dependence of growth rates on baseline lesion size \citep{Yehoshua2011,Feuer2013}."
  - Now: "Lesion growth is summarised as the yearly change in the square root of the lesion area, a transform used for GA because it removes the dependence of growth rates on baseline lesion size \citep{Yehoshua2011,Feuer2013}."
- **3.11** [low] §3.1 Dataset · `03-data.tex:98` · **Done**: 2026-10-14 (own wording)
  - Issue: The one-sentence paragraph follows the growth statistics, which it has nothing to do with. 'the views used throughout this chapter' is vague, because the chapter does not refer to 'views'.
  - Was: "Figure~\ref{fig:data:example-state} shows one visit of the cohort in the views used throughout this chapter."
  - Review suggested: "Reword, and move it to the end of the mask-provenance paragraph (after l.60), where the SLO frame and the OCT-grid mask have just been introduced: Figure~\ref{fig:data:example-state} shows one visit as the SLO fundus image with the OCT field of view, the GA ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **3.12** [low] Figure 3.1 caption · `03-data.tex:132` (today `03-data.tex:159`) · **Done**: 2026-10-14 (own wording)
  - Issue: The models receive normalised values of all eleven channels. The panels show two channels in raw units (a binary mask and a map coloured by axial depth), so 'as the models receive it' says more than the figure shows.
  - Was: "Panels (b) and (c) show the state tensor as the models receive it."
  - Now: "Panels (c) and (d) show two of the eleven channels of the state tensor before normalisation.}"
- **3.13** [low] §3.2 State Representation · `03-data.tex:141` (today `03-data.tex:169`) · **Done**: 2026-10-14 (as suggested)
  - Issue: Five short sentences of similar length, two of them opening with 'Channel~0'. The roles are listed after both definitions as a mirrored pair ('Channel~0 is both X and Y. The layer channels supply X and serve as Y.').
  - Was: "The state of an eye at each visit is an eleven-channel tensor, so $C = 11$. Channel~0 holds the binary GA mask. Channels~1--10 hold the ten layer-boundary depth maps, ordered from the most superficial boundary to the deepest. Channel~0 is both the prediction ..."
  - Now: "The state of an eye at a visit is a tensor with $C = 11$ channels. Channel~0 holds the binary GA mask, which is both the prediction target and the clinical deliverable. Channels~1--10 hold the ten layer-boundary depth maps, ordered from the most superficial boundary to the deepest. They supply structural context and ..."
- **3.14** [medium] §3.2 State Representation · `03-data.tex:166` (today `03-data.tex:213`) · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: The paragraph opens with what is not done (thickness) and only then gives the reason for what is done, so the reader has to work out the link. It closes with a 'therefore ... rather than ...' sentence that only restates the sentence before.
  - Was: "Retinal thickness, the distance between the deepest and the shallowest boundary, is not computed anywhere in this pipeline. It could be recovered from the layer channels, but it is neither stored nor used as an input. The reason for keeping all ten layer ..."
  - Now: "Retinal thickness, the distance between the deepest and the shallowest boundary, is not computed anywhere in this pipeline."
- **3.15** [low] §3.3 Spatial Standardisation and its Measured Cost · `03-data.tex:187` (today `03-data.tex:252`) · **Done**: as suggested
  - Issue: An announced enumeration ('for two reasons.') followed by the list, plus the stock phrase 'by construction'.
  - Was: "Cropping and padding are used instead of resampling for two reasons. They introduce no interpolation artefacts, and they keep the stored pixel spacing identical across the cohort by construction."
  - Now: "Cropping and padding are used instead of resampling because they introduce no interpolation artefacts and keep the stored pixel spacing identical across the cohort."
- **3.16** [low] §3.3 Spatial Standardisation and its Measured Cost · `03-data.tex:189` · **Done**: 2026-10-12..14 (restructure of Ch. 1-3 and its bridges)
  - Issue: The literature pointer ends a paragraph about how the common grid is reached, before the window size has been given. It belongs next to the 5.938 x 5.816 mm figure in the next paragraph.
  - Was: "The use of a $6 \times 6$\,mm analysis window in the literature was reviewed in~\S\ref{sec:background:ga-oct:muw}."
  - Review suggested: "Delete it here and insert after the first sentence of the next paragraph (after '... holds 50\,176 grid positions.'): This physical extent is close to the $6 \times 6$\,mm analysis window used in the literature (\S\ref{sec:background:ga-oct:muw})." (the passage was cut or rewritten; no single sentence corresponds today)
- **3.17** [low] §3.3 Spatial Standardisation and its Measured Cost · `03-data.tex:195` (today `03-data.tex:259`) · **Done**: as suggested
  - Issue: 'the spacing along them' requires the reader to remember that A-scans lie along a B-scan. §3.1 (l.71) already names the two spacings 'between B-scans' and 'between A-scans'.
  - Was: "The spacing between B-scans is \textbf{21.335 times larger} than the spacing along them."
  - Now: "The spacing between B-scans is \textbf{21.335 times larger} than the spacing between A-scans."
- **3.18** [low] §3.3 Spatial Standardisation and its Measured Cost · `03-data.tex:211` · **Done**: sentence kept; moved or its context changed
  - Issue: The paragraph goes from the raw meaning of zero to the normalised value and the loss, then back to raw values with this sentence. As the closing sentence it interrupts the conclusion about training at full weight.
  - Was: "Zero also cannot serve as a sentinel that marks padding, because real layer values range from $-14$ to $499$ and so include zero."
  - Review suggested: "Move this sentence up so that it directly follows '... a layer depth of 0 is the top of the volume, above the retina.' (l.204), before 'The models, however, do not see raw values.'" (the passage was cut or rewritten; no single sentence corresponds today)
- **3.19** [medium] §3.3 Spatial Standardisation and its Measured Cost · `03-data.tex:221` (today `03-data.tex:306`) · **Done**: as suggested
  - Issue: 'censored' is a technical term used without a plain explanation. 'change-region metrics' and 'one-year anchor' appear before Chapter 5 defines them, with no pointer. 'missingness flag' is storage jargon.
  - Was: "Growth across that edge is censored, and no missingness flag records it. The models are therefore trained on censored targets, and the change-region metrics at the one-year anchor under-measure progression for roughly one visit in five."
  - Now: "Growth across that edge is not observed (it is censored), and no flag in the data marks it. The models are therefore trained on censored targets, and the change-region metrics at the one-year anchor (\S\ref{sec:experiments:protocol}) under-measure progression for roughly one visit in five."
- **3.20** [low] §3.3 Spatial Standardisation and its Measured Cost · `03-data.tex:228` (today `03-data.tex:314`) · **Done**: as suggested
  - Issue: 'on purpose' is conversational (it recurs at l.356). The bare 'window' also collides with the temporal 'window' of §3.5-§3.6.
  - Was: "The window was nevertheless kept on purpose."
  - Now: "The $49 \times 1024$ window was nevertheless kept deliberately."
- **3.21** [medium] §3.3 Spatial Standardisation and its Measured Cost · `03-data.tex:234` · **Done**: own wording
  - Issue: The sentence dangles at the end of a paragraph about lesion censoring, which is not about pad positions. It also repeats the point already made at l.209-211 ('No reported run excludes the pad positions from the loss').
  - Was: "The training loss can optionally exclude pad positions."
  - Review suggested: "Delete it here and replace l.209-211 ('No reported run excludes ... at full weight.') with: The training loss can optionally exclude the pad positions, but no reported run does so (\S\ref{sec:method:training}). The models are therefore trained to reproduce ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **3.22** [low] §3.4 Normalisation · `03-data.tex:244` (today `03-data.tex:329`) · **Done**: as suggested
  - Issue: 'over the training visits of the current fold only' and 'No validation data enters the statistics' say the same thing. The padded-zeros sentence repeats §3.3 almost verbatim, so the two sections cross-reference each other for one fact.
  - Was: "After spatial standardisation, each channel is normalised. The statistics are computed per channel over the training visits of the current fold only, and are then applied to every visit, including the validation visits. No validation data enters the ..."
  - Now: "After spatial standardisation, each channel is normalised. The statistics are computed per channel over the training visits of the current fold only and are then applied to every visit, including the validation visits. As noted in~\S\ref{sec:data:spatial}, the padded zeros contribute to each channel's mean and ..."
- **3.23** [low] §3.4 Normalisation · `03-data.tex:252` (today `03-data.tex:336`) · **Done**: as suggested
  - Issue: 'canonical scheme' implies that alternative schemes exist, but the text no longer mentions any (the min-max variant was removed in review #1 of 2026-09-27).
  - Was: "The canonical scheme is a z-score,"
  - Now: "The normalisation is a z-score,"
- **3.24** [medium] §3.4 Normalisation · `03-data.tex:260` (today `03-data.tex:344`) · **Done**: own wording
  - Issue: 'the canonical fold' is used here and at l.286 but is defined (as fold 2) only in Chapter 5 (05-experiments.tex l.101). 'Two consequences follow. First ... Second ...' is an announced enumeration.
  - Was: "On the canonical fold, the background value 0 maps to $-0.602$ and the foreground value 1 maps to $+1.660$. The binarisation threshold of 0.5 maps to $+0.529$. Two consequences follow. First, the normalised mask has a hard step at the lesion edge. Second, ..."
  - Now: "On fold~2, the background value 0 maps to $-0.602$, the foreground value 1 maps to $+1.660$, and the binarisation threshold of 0.5 maps to $+0.529$."
- **3.25** [HIGH] §3.5 Patient-Level Covariates · `03-data.tex:272` (today `03-data.tex:351`) · **Done**: 2026-10-02 (high-severity pass)
  - Issue: 'window' has two meanings in this chapter: the spatial 49 x 1024 crop region (§3.3: 'The resulting window', 'the border of the window', 'Larger windows', 'any window') and the temporal pair of visits (§3.5-§3.6). Here it is used in the temporal sense before §3.6 defines it, so a reader coming from §3.3 will take it to mean the crop.
  - Was: "Each window is accompanied by two patient-level covariates, age and sex."
  - Now: "Each transition window, a pair of consecutive visits of one eye (\S\ref{sec:data:temporal}), is accompanied by two patient-level covariates, age and sex."
- **3.26** [low] §3.5 Patient-Level Covariates · `03-data.tex:274` (today `03-data.tex:359`) · **Done**: as suggested
  - Issue: 'keyed per eye' is database vocabulary. It is part of the engineering-log register that recurs in the chapter (split files, eye suffix, missingness flag).
  - Was: "The table is keyed per eye, so a patient who contributes two eyes appears in two rows with the same age and sex."
  - Now: "The table has one row per eye, so a patient who contributes two eyes appears in two rows with the same age and sex."
- **3.27** [low] §3.5 Patient-Level Covariates · `03-data.tex:283` (today `03-data.tex:368`) · **Done**: as suggested
  - Issue: 'training window-start ages' is a dense noun stack, and 'Since there is one start age per window' takes a roundabout route to the point.
  - Was: "The z-score statistics for this mode are computed over all training window-start ages. Since there is one start age per window, the final visit of each training eye does not enter them."
  - Now: "The z-score statistics for this mode are computed over the start-visit ages of all training windows. Because each window contributes only the age at its start visit, the final visit of each training eye does not enter them."
- **3.28** [medium] §3.6 Temporal Structure · `03-data.tex:305` (today `03-data.tex:390`) · **Done**: as suggested
  - Issue: A clause pair joined by a semicolon that ends in an 'X, not Y' antithesis. 'fixed commitment' is a rhetorical way of saying that the setting cannot be changed.
  - Was: "Each window holds exactly one transition; this is a fixed commitment of the framework, not a configuration option."
  - Now: "Each window holds exactly one transition. This is fixed by the framework and cannot be changed by configuration."
- **3.29** [medium] §3.6 Temporal Structure · `03-data.tex:336` (today `03-data.tex:419`) · **Done**: as suggested
  - Issue: The topic sentence promises properties that shape the pipeline, but the first property is never tied to anything. Its link (180 days is the base of the training time budget, 04-method.tex l.1106-1107) is left implicit. '90-day acquisition grid' also overloads 'grid', which everywhere else in the thesis means the spatial grid.
  - Was: "Three properties of this schedule shape the rest of the pipeline. First, every interval is a multiple of the 90-day acquisition grid, and the most common interval is 180 days."
  - Now: "Three properties of this schedule shape the rest of the pipeline. First, every interval is a multiple of 90 days, and the most common interval, 180 days, is the base of the time budget used in training (\S\ref{sec:method:training}). In addition, merge the one-sentence table paragraph (l.312-313) into the start of this ..."
- **3.30** [low] §3.6 Temporal Structure · `03-data.tex:341` (today `03-data.tex:424`) · **Done**: as suggested
  - Issue: 'intervals shorter than the modal 180 days' is a roundabout way to say the 90-day intervals, the only shorter interval in Table~\ref{tab:data:intervals}.
  - Was: "A training scheme restricted to intervals shorter than the modal 180 days would therefore learn from this densely imaged subgroup alone."
  - Now: "A training scheme restricted to the 90-day intervals would therefore learn from this densely imaged subgroup alone."
- **3.31** [medium] §3.6 Temporal Structure · `03-data.tex:344` (today `03-data.tex:427`) · **Done**: as suggested
  - Issue: The 'where' clause is loosely attached. The counts switch from 'chain two visits' to 'reach at least one autoregressive step', so a reader cannot tell whether the 90-day and 360-day statements measure the same quantity.
  - Was: "Third, the schedule limits how far an eye can be rolled forward during training, where several visits are chained within a fixed time budget (\S\ref{sec:method:training}). With a budget of 90 days, none of the 75 eyes can chain two visits. With 360 days, 74 ..."
  - Now: "Third, the schedule limits how far an eye can be rolled forward during training, because the training curriculum chains visits within a fixed time budget (\S\ref{sec:method:training}). With a budget of 90 days, none of the 75 eyes can chain two visits, so no step is unrolled. With 360 days, 74 of the 75 eyes reach at ..."
- **3.32** [medium] §3.6 Temporal Structure · `03-data.tex:351` (today `03-data.tex:434`) · **Done**: as suggested
  - Issue: 'The one-year anchor' and 'the metric' appear without definition. The colon presents the definition of the anchor as if it explained 'no upper bound', so the reader has to work out that the scored step can fall well beyond one year. After 'Three properties', this paragraph also reads as an uncounted fourth item.
  - Was: "The same schedule also shapes the evaluation. The one-year anchor has no upper bound: the metric is taken at the first rollout step whose cumulative time reaches about 347 days. For 68 of the 75 eyes, this is exactly 360 days."
  - Now: "Beyond training, the schedule also affects the evaluation. The change-region metrics are taken at a one-year anchor, the first rollout step whose cumulative time reaches about 347 days. This anchor has no upper bound. For 68 of the 75 eyes, it falls at exactly 360 days."
- **3.33** [low] §3.6 Temporal Structure · `03-data.tex:356` (today `03-data.tex:440`) · **Done**: as suggested
  - Issue: 'on purpose' is conversational and recurs (l.228). The semicolon pair reads more naturally as two sentences.
  - Was: "This is accepted on purpose; \citet{Mai2024} likewise score every follow-up visit by its time since baseline, in yearly bins, and not at a fixed horizon."
  - Now: "This is accepted deliberately. \citet{Mai2024} likewise score every follow-up visit by its time since baseline, in yearly bins, and not at a fixed horizon."
- **3.34** [medium] §3.7 Splits and Cross-Validation · `03-data.tex:364` (today `03-data.tex:448`) · **Done**: as suggested
  - Issue: 'split files' and 'carry no eye suffix' describe the storage format instead of the design. A reader without the repository cannot tell what an eye suffix is.
  - Was: "The data is partitioned by five split files that define a patient-level 5-fold cross-validation. The five validation sets do not overlap, and together they cover all patients. The split identifiers carry no eye suffix, so both eyes of a patient always fall ..."
  - Now: "The data is partitioned into five folds for a patient-level cross-validation. The five validation sets do not overlap, and together they cover all patients. The folds are defined on patient identifiers, so both eyes of a patient always fall into the same partition."
- **3.35** [medium] §3.7 Splits and Cross-Validation · `03-data.tex:399` · **Done**: own wording
  - Issue: 'structurally empty' is unexplained jargon. Five short sentences walk through the assignment logic before reaching the statement the reader needs, and the first and fourth sentences say the same thing.
  - Was: "The test split is structurally empty. An eye whose patient appeared in neither the training nor the validation list would be assigned to a test partition. However, every patient with scans is assigned to training or validation in every fold. No test partition ..."
  - Review suggested: "The test split is empty in every fold. An eye whose patient appeared in neither the training nor the validation list would be assigned to a test partition, but every patient with scans is assigned to training or validation in every fold. The protocol is ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **3.36** [low] §3.7 Splits and Cross-Validation · `03-data.tex:408` · **Done**: sentence kept; moved or its context changed
  - Issue: 'also' refers back to the per-fold eye counts (l.373-375), but the test-split paragraph comes between them, so the chapter ends on a point that has lost its anchor.
  - Was: "The folds also differ in baseline lesion size."
  - Review suggested: "Move the whole paragraph (l.408-411) directly after the per-fold eye-count paragraph (l.373-375), before the test-split paragraph. The opening sentence can then stay as it is." (the passage was cut or rewritten; no single sentence corresponds today)

## Chapter 4, overview, framework, operator contract, GNN

Source: `reviews/editorial-2026-10-01/04a-method-framework-gnn.md`.

- **4a.1** [medium] §4.1 Overview · `04-method.tex:11` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: A pseudo-cleft ('What the adaptation produced is ...') followed by three short stand-alone sentences, a semicolon joining the provenance and its consequence, and the informal phrasal verb 'find out'.
  - Was: "The work began as an adaptation of two graph-based neural PDE solvers, MP-PDE and MM-PDE, which the clinical partner had suggested; the case for their local inductive bias was built and tested only afterwards. What the adaptation produced is the setup ..."
  - Review suggested: "The work began as an adaptation of two graph-based neural PDE solvers, MP-PDE and MM-PDE, which the clinical partner had suggested. The case for their local inductive bias was built and tested only afterwards. The adaptation produced the setup described in ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4a.2** [low] §4.1 Overview · `04-method.tex:21` (today `04-method.tex:24`) · **Done**: 2026-10-17 (own wording)
  - Issue: A mirror pair across the paragraph break: 'the only component that changes' and 'Everything outside the slot is held fixed' state the same point from opposite sides as two short sentences.
  - Was: "A single pipeline is therefore fixed, and it provides one swappable slot for the update operator $f_\theta$. The operator placed in this slot is the only component that changes between experiments. Everything outside the slot is held fixed."
  - Now: "A single pipeline therefore provides one swappable slot for the update operator $f_\theta$, the only component that changes between experiments."
- **4a.3** [low] §4.1 Overview · `04-method.tex:32` (today `04-method.tex:35`) · **Done**: 2026-10-17 (as suggested)
  - Issue: 'Backbone' appears only here in §4.1-4.3, while the surrounding text says 'operator' (and also 'module', 'architecture', 'arm'), so a reader may wonder whether a backbone is something different from the operator.
  - Was: "A backbone placed in the slot contains architecture only."
  - Now: "An operator placed in the slot contains only its architecture."
- **4a.4** [low] §4.1 Overview · `04-method.tex:35` · **Done**: 2026-10-17 (own wording)
  - Issue: A redundant paragraph closer with an intensifier ('exactly'). It repeats the argument of l. 18-21 ('If every candidate architecture came with its own training pipeline ...').
  - Was: "A separate pipeline per architecture would reintroduce exactly the confounds the design is meant to remove."
  - Review suggested: "Cut the sentence. If it is kept: "A separate pipeline per architecture would reintroduce the confounds described above."" (the passage was cut or rewritten; no single sentence corresponds today)
- **4a.5** [low] §4.1 Overview · `04-method.tex:39` (today `04-method.tex:51`) · **Done**: 2026-10-17 (as suggested)
  - Issue: Grammatically, 'one of which' refers to the graphs, but the canonical model is the GNN on one of them. The semicolon list with a nested relative clause is also hard to parse.
  - Was: "The operators run through this pipeline are a message-passing graph neural network (GNN) on two different neighbourhood graphs (\S\ref{sec:method:graph}), one of which is the canonical model of this thesis; a U-Net; a Fourier Neural Operator (FNO); and a ..."
  - Now: "The operators run through this pipeline are a message-passing graph neural network (GNN) on two different neighbourhood graphs (\S\ref{sec:method:graph}), a U-Net, a Fourier Neural Operator (FNO) and a hybrid Finite Element Network (FEN). The GNN on one of the two graphs is the canonical model of this thesis."
- **4a.6** [medium] §4.1 Overview · `04-method.tex:44` (today `04-method.tex:60`) · **Done**: 2026-10-17 (as suggested)
  - Issue: Two unrelated items are joined by 'and'. 'Floor' is used for the first time without explanation, and 'lower floor' implies a second floor (the one-hop floor) that the reader has not met yet.
  - Was: "A fixed-step Runge--Kutta wrapper can be placed around any of these operators, and a per-pixel model with no spatial context marks the lower floor."
  - Now: "A fixed-step Runge--Kutta wrapper can be placed around any of these operators. A per-pixel model with no spatial context sets the lowest reference level, or floor, of the comparison."
- **4a.7** [medium] §4.1 Overview · `04-method.tex:46` (today `04-method.tex:56`) · **Done**: 2026-10-02 (high-severity pass)
  - Issue: 'Arm' appears here for the first time in the comparison sense and is never defined. It is the central unit of Chapters 4-5, and its only earlier use in the thesis is the sample and reference arms of the OCT interferometer (§2.1.3), so the reader has to infer what an arm is (an operator, a variant, a run?).
  - Was: "The arms are parameter-matched to the canonical configuration's 67\,147 parameters within a narrow band; the matching and its exceptions are described in~\S\ref{sec:method:family:params}."
  - Now: "It is the reference configuration: the ablations of the framework in Chapter~\ref{ch:experiments} are run on it, and the other arms are matched to its 67\,147 parameters within a narrow band; the matching and its exceptions are described in~\S\ref{sec:method:family:params}."
- **4a.8** [medium] §4.1 Overview · `04-method.tex:52` · **Done**: 2026-10-17 (own wording)
  - Issue: This evidence that the shared pipeline held sits between the operator list and the roadmap, where it interrupts both. 'Come out identical' is conversational, and three short sentences carry what is one point.
  - Was: "The persistence baseline, which predicts no change, is computed inside every run by the same evaluation code. Its values come out identical across all arms. This indicates that every arm was trained and evaluated on the same data through the same evaluation ..."
  - Review suggested: "Move the paragraph, together with its TODO comment, to directly after the second paragraph (after l. 37), once 'arm' has been defined in the first paragraph (see l. 46), and reword it: "The persistence baseline, which predicts no change, is computed in every ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4a.9** [medium] §4.2 The Fixed Framework · `04-method.tex:95` (today `04-method.tex:108`) · **Done**: 2026-10-17 (own wording)
  - Issue: A meta-announcement is followed by a second one ('A further shared choice concerns ...'). The scope list leaves out the input that the paragraph then discusses, and the last sentence restates 'but no earlier visits' on its own.
  - Was: "This section defines what every arm shares: the time handling and the tensor layout of the state. A further shared choice concerns the input itself. Every operator receives exactly one visit and predicts the state at the next visit. It sees the current state, ..."
  - Now: "This section defines what every arm shares: the input, the time handling (\S\ref{sec:method:dt-residual}), the tensor layout of the state (\S\ref{sec:method:multichannel}), the conditioning inputs (\S\ref{sec:method:covariates}), the objective (\S\ref{sec:method:training:loss}), the training curriculum ..."
- **4a.10** [medium] §4.2 The Fixed Framework · `04-method.tex:102` (today `04-method.tex:126`) · **Done**: 2026-10-17 (as suggested)
  - Issue: The 'second reason' is not presented as a reason for the one-visit input. It is a separate decision about the output (no temporal bundling), so the reader loses track of what is being justified. The paragraph also uses the intensifier 'strictly', the conversational 'anyway', and 'as noted above', which repeats the first reason.
  - Was: "Two reasons support this design. First, the clinical sequences are short, with five to thirteen visits per eye (\S\ref{sec:data:dataset}). Using several past visits as input would leave fewer visits available as prediction targets. Second, the framework ..."
  - Now: "This design follows from the length of the clinical sequences: with five to thirteen visits per eye (\S\ref{sec:data:dataset}), using several past visits as input would leave fewer visits available as prediction targets. On the output side, the framework predicts one step at a time. Some neural PDE solvers, such as ..."
- **4a.11** [low] §4.2 The Fixed Framework · `04-method.tex:115` · **Done**: 2026-10-17 (own wording)
  - Issue: A pointer appended to the bundling paragraph, where it has nothing to do with the topic. It belongs where §4.2 sets out its scope.
  - Was: "The shared loss and curriculum are defined in~\S\ref{sec:method:training}, and the shared evaluation in~\S\ref{sec:experiments:protocol}."
  - Review suggested: "Move the sentence unchanged to directly after the scope sentence of §4.2 (l. 95-96)." (the passage was cut or rewritten; no single sentence corresponds today)
- **4a.12** [low] §4.2.1 $\Delta t$-Conditioned Residual Formulation · `04-method.tex:140` · **Done**: 2026-10-17 (own wording)
  - Issue: A teaser opener ('This form has a useful limit.') followed by two short sentences that make one point.
  - Was: "This form has a useful limit. As $\Delta t$ approaches zero, the predicted change vanishes and the prediction collapses to $u_{t+\Delta t} = u_t$. For two visits very close in time, the model thus predicts no change."
  - Review suggested: "As $\Delta t$ approaches zero, the predicted change vanishes and the prediction collapses to $u_{t+\Delta t} = u_t$, so that for two visits very close in time the model predicts no change." (the passage was cut or rewritten; no single sentence corresponds today)
- **4a.13** [medium] §4.2.1 $\Delta t$-Conditioned Residual Formulation · `04-method.tex:142` (today `04-method.tex:182`) · **Done**: 2026-10-17 (own wording)
  - Issue: The comparison 'relative to the rest of the retinal state' is unclear. It suggests that the layer channels change faster than the lesion, which the persistence argument does not need and which is probably not meant. The argument only needs slow change between visits.
  - Was: "The leading $u_t$ term is also a deliberate prior. Consecutive visits are almost identical, because GA changes slowly relative to the rest of the retinal state."
  - Now: "The leading $u_t$ term is also a deliberate prior: consecutive visits are almost identical, because GA progresses little over a typical interval between visits."
- **4a.14** [medium] §4.2.1 $\Delta t$-Conditioned Residual Formulation · `04-method.tex:147` (today `04-method.tex:189`) · **Done**: 2026-10-17 (own wording)
  - Issue: The first sentence piles up 'so ..., although ... and ...'. The second ends in an aphoristic clause after a semicolon, and 'the prior' does not say which prior is meant. The topic changes here, so a new paragraph would help.
  - Was: "The output of $f_\theta$ is signed and unbounded, so the model can in principle also predict a shrinking lesion, although atrophic tissue does not regenerate and a shrinking lesion is not clinically plausible. No monotonic-growth constraint is imposed, ..."
  - Now: "The output of $f_\theta$ is signed and unbounded, so the model can in principle also predict a shrinking lesion."
- **4a.15** [low] §4.2.1 $\Delta t$-Conditioned Residual Formulation · `04-method.tex:159` (today `04-method.tex:202`) · **Done**: 2026-10-17 (own wording)
  - Issue: 'It is the same ...' is ambiguous (the step size or the form?), and 'This resemblance ... needs a caution' announces the caveat instead of stating it.
  - Was: "Equation~\eqref{eq:method:residual-update} takes the form of one explicit Euler step (\S\ref{sec:background:pde-solvers:time}), with a step size that differs from window to window. It is the same for every operator placed in the slot. This resemblance to a ..."
  - Now: "Equation~\eqref{eq:method:residual-update} has the form of one explicit Euler step (\S\ref{sec:background:pde-solvers:time}) whose step size differs from window to window, and this form is the same for every operator in the slot."
- **4a.16** [low] §4.2.1 $\Delta t$-Conditioned Residual Formulation · `04-method.tex:165` · **Done**: 2026-10-17 (own wording)
  - Issue: In 'Instead, it is tested directly', 'it' could refer to 'this thesis' or to 'such a reading', and 'directly' is filler.
  - Was: "This thesis therefore does not assume such a reading. Instead, it is tested directly with a solver-swap diagnostic, reported in~\S\ref{sec:experiments:validity}: a trained model is re-evaluated, without retraining, under several integration schemes and step ..."
  - Review suggested: "Whether such a reading holds is therefore tested with a solver-swap diagnostic (\S\ref{sec:experiments:validity}): a trained model is re-evaluated, without retraining, under several integration schemes and step counts." (the passage was cut or rewritten; no single sentence corresponds today)
- **4a.17** [low] §4.2.2 Multi-Channel State Propagation · `04-method.tex:175` (today `04-method.tex:210`) · **Done**: 2026-10-17 (own wording)
  - Issue: Three sentences of recap and a scope announcement before the content starts.
  - Was: "The framework carries the full eleven-channel state through every component. As defined in~\S\ref{sec:data:state}, the state consists of one binary mask channel and ten layer-boundary depth channels. This subsection covers only how these channels are laid out ..."
  - Now: "The full eleven-channel state of~\S\ref{sec:data:state} is carried through every component of the framework; this subsection describes only how the channels are laid out as tensors."
- **4a.18** [low] §4.2.2 Multi-Channel State Propagation · `04-method.tex:188` (today `04-method.tex:225`) · **Done**: 2026-10-17 (own wording)
  - Issue: A one-sentence paragraph left over from an earlier cut. 'Convolutional arms' does not match the term used in §4.3.1 ('operators that work on the image grid'), and the FNO is not convolutional in the usual sense.
  - Was: "Operators that work on images, such as the convolutional arms of~\S\ref{sec:method:family}, need the state in the image layout $(B, C, 49, 1024)$."
  - Now: "Operators that work on the image grid (\S\ref{sec:method:family:dense}) use the layout $(B, C, H, W)$ instead."
- **4a.19** [medium] §4.3 The Operators · `04-method.tex:204` · **Done**: 2026-10-17 (own wording)
  - Issue: A run of short sentences with identical 'X tests Y' syntax, the emphatic 'at all', and a closing sentence that repeats §4.1 a third time. The slot is introduced again although §4.1 and §4.2 already did so. Attaching the section references here makes the roadmap paragraph that follows unnecessary.
  - Was: "The framework of~\S\ref{sec:method:framework} provides one slot for the update operator $f_\theta$. This section describes every operator that occupies it. Each was chosen to isolate one property. A message-passing graph neural network, run on two different ..."
  - Review suggested: "This section describes the operators placed in the slot of~\S\ref{sec:method:framework}; each was chosen to isolate one property. The message-passing graph neural network (\S\ref{sec:method:mppde}), run on two different graphs (\S\ref{sec:method:graph}), ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4a.20** [medium] §4.3 The Operators · `04-method.tex:218` (today `04-method.tex:500`) · **Done**: 2026-10-17 (own wording)
  - Issue: A mechanical roadmap that lists the operators a second time in this section (a third time counting §4.1). Every sentence uses the same '\S X describes ...' pattern.
  - Was: "\S\ref{sec:method:family:contract} states the interface every operator satisfies. \S\ref{sec:method:mppde} describes the message-passing network and \S\ref{sec:method:graph} the two graphs it runs on. \S\ref{sec:method:family:dense} describes the three dense ..."
  - Now: ""
- **4a.21** [medium] §4.3.1 The Operator Contract · `04-method.tex:230` (today `04-method.tex:503`) · **Done**: 2026-10-17 (as suggested)
  - Issue: The em-dash triad and the 'same ..., same ..., same ...' rhythm stand out. The residual form and the zero-init are restated from §4.2.1. 'Cannot diverge' can be read as numerical divergence (a topic the chapter later raises for the T-FEN) when 'cannot become inconsistent' is meant. 'Module' is a fifth name for the operator.
  - Was: "Every operator satisfies the same interface. It is built from the same metadata --- one time step, eleven state channels and two covariates --- and it consumes the same batch. It returns the full next state in the residual form of ..."
  - Now: "Every operator satisfies the same interface: it is built from the same metadata (one time step, eleven state channels and two covariates) and consumes the same batch. It returns the full next state in the residual form of Equation~\eqref{eq:method:residual-update}, and its final layer is initialised to zero ..."
- **4a.22** [medium] §4.3.1 The Operator Contract · `04-method.tex:241` (today `04-method.tex:513`) · **Done**: 2026-10-17 (own wording)
  - Issue: 'These drifted states' refers to a drift the previous sentence never mentions, so a reader who has not yet seen the pushforward trick loses the thread. 'The very perturbation' is an intensifier. (GPTZero labels the first sentence human and the second AI.)
  - Was: "The training curriculum of~\S\ref{sec:method:training} rolls the model forward on its own predictions without gradients but in training mode. Batch normalisation \citep{Ioffe2015} would normalise these drifted states with the statistics of the current batch, ..."
  - Now: "The training curriculum of~\S\ref{sec:method:training:curriculum} rolls the model forward on its own predictions, without gradients but in training mode, so the states it produces drift away from the observed ones."
- **4a.23** [medium] §4.3.1 The Operator Contract · `04-method.tex:251` (today `04-method.tex:524`) · **Done**: 2026-10-17 (as suggested)
  - Issue: An em-dash aside and an 'X, not Y' closer that repeats the opening ('identical inputs'). 'The Fourier Neural Operator with its local-kernel hybrid' leaves it unclear whether the hybrid is a separate operator.
  - Was: "The operators that work on the image grid --- the U-Net and the Fourier Neural Operator with its local-kernel hybrid --- receive identical inputs. Each takes sixteen input channels: the eleven state channels, $\Delta t$ broadcast as a constant plane, the two ..."
  - Now: "The operators that work on the image grid (the U-Net, the Fourier Neural Operator and its local-kernel hybrid) receive identical inputs, so that a difference between these arms cannot come from the information they receive. Each takes sixteen input channels: the eleven state channels, $\Delta t$ broadcast as a ..."
- **4a.24** [low] §4.3.2 Message-Passing Graph Neural Network · `04-method.tex:267` (today `04-method.tex:539`) · **Done**: 2026-10-17 (as suggested)
  - Issue: An em-dash aside containing a list of three, plus the intensifier 'strict'.
  - Was: "Several of its design decisions --- the time handling, the output layer and the strict one-step prediction --- also became part of the shared framework."
  - Now: "Several of its design decisions also became part of the shared framework: the time handling, the output layer and the one-step prediction."
- **4a.25** [medium] §4.3.2 Message-Passing Graph Neural Network (The original MP-PDE) · `04-method.tex:283` (today `04-method.tex:556`) · **Done**: 2026-10-17 (as suggested)
  - Issue: The sentence calls $f_i^0$ the encoder's input, although $f_i^0$ is its output and the input is the bracketed list. A careful reader will stumble here.
  - Was: "Its input is $f_i^0 = \epsilon([u_i^{k-K:k}, x_i, t_k, \theta_{\text{PDE}}])$: the last $K$ states of the node, its position, the current time and the equation features."
  - Now: "It computes $f_i^0 = \epsilon([u_i^{k-K:k}, x_i, t_k, \theta_{\text{PDE}}])$ from the last $K$ states of the node, its position, the current time and the equation features."
- **4a.26** [low] §4.3.2 Message-Passing Graph Neural Network (The original MP-PDE) · `04-method.tex:288` (today `04-method.tex:561`) · **Done**: 2026-10-17 (as suggested)
  - Issue: Inside a paragraph headed 'The original MP-PDE', the tacked-on clause '; the original uses six' leaves the reader asking 'original of what?'. It reads like an appended punchline.
  - Was: "The processor applies several rounds of message passing to the latent node states; the original uses six."
  - Now: "The processor applies several rounds of message passing to the latent node states (six in the original paper)."
- **4a.27** [low] §4.3.2 Message-Passing Graph Neural Network (The original MP-PDE) · `04-method.tex:294` (today `04-method.tex:568`) · **Done**: 2026-10-17 (as suggested)
  - Issue: The closing appositive restates the point and repeats 'learned'.
  - Was: "The solution difference $u_i - u_j$ lets each message act as a learned local difference operator, a flexible learned stencil."
  - Now: "The solution difference $u_i - u_j$ lets each message act as a learned local difference operator, that is, a learned stencil."
- **4a.28** [medium] §4.3.2 Message-Passing Graph Neural Network (The original MP-PDE) · `04-method.tex:301` (today `04-method.tex:574`) · **Done**: 2026-10-17 (as suggested)
  - Issue: A pseudo-cleft ('is what lets'), a semicolon-joined pair of clauses, and the informal 'hurts'.
  - Was: "This persistent injection is what lets a single trained solver generalise across a family of equations; removing it hurts most when the equation parameters vary across the dataset."
  - Now: "Injecting it at every layer allows a single trained solver to generalise across a family of equations, and removing it degrades performance most when the equation parameters vary across the dataset."
- **4a.29** [medium] §4.3.2 Message-Passing Graph Neural Network (The architecture used here) · `04-method.tex:336` (today `04-method.tex:609`) · **Done**: 2026-10-17 (as suggested)
  - Issue: 'Slot' is the chapter's key term for the operator slot. Using it here for the $\theta_{\text{PDE}}$ input invites confusion, and Table 4.1 does the same ('in that slot'). The two sentences also say the same thing twice ('fills the slot' / 'take this place'). (GPTZero labels the first sentence AI and the second human.)
  - Was: "The conditioning vector fills the slot that the equation feature vector $\theta_{\text{PDE}}$ occupies in the original. No governing equation or coefficients are known for GA, so the interval and the covariates take this place."
  - Now: "The conditioning vector takes the place of the equation feature vector $\theta_{\text{PDE}}$ of the original: no governing equation or coefficients are known for GA, so the interval and the covariates are used instead. (In Table~\ref{tab:method:mppde-diff}, change 'in that slot' to 'in its place'.)"
- **4a.30** [medium] §4.3.2 Message-Passing Graph Neural Network (The architecture used here) · `04-method.tex:369` (today `04-method.tex:642`) · **Done**: 2026-10-17 (as suggested)
  - Issue: 'As in the original' opens two of three sentences and 'The canonical configuration' two consecutive ones. The relative clause inside the third sentence makes it hard to follow. 'Raw state' could be read as un-normalised, although $u_i$ is the normalised state (l. 329).
  - Was: "As in the original, the state difference $u_i - u_j$ lets the message act as a learned local difference operator. Every round receives the raw state, the positions and the conditioning vector again, so this information is available at every depth. As in the ..."
  - Now: "As in the original, the state difference $u_i - u_j$ lets the message act as a learned local difference operator. Every round receives the state $u_i$, the positions and the conditioning vector again, so this information is available at every depth. Each update ends in a residual connection followed by a normalisation ..."
- **4a.31** [medium] §4.3.2 Message-Passing Graph Neural Network (The architecture used here) · `04-method.tex:384` (today `04-method.tex:656`) · **Done**: 2026-10-17 (as suggested)
  - Issue: 'Before this change' refers to a change in project history that the text never introduces. It reads like a development log, not a method description.
  - Was: "Before this change, when batch normalisation was used, training and evaluation measurably behaved as two different operators."
  - Now: "In earlier runs with batch normalisation, training and evaluation measurably behaved as two different operators."
- **4a.32** [low] §4.3.2 Message-Passing Graph Neural Network (The architecture used here) · `04-method.tex:393` (today `04-method.tex:668`) · **Done**: 2026-10-17 (own wording)
  - Issue: 'Bare' is informal, and the following phrase says the same thing again.
  - Was: "The final layer is bare, without normalisation or activation, because the output is a signed and unbounded residual."
  - Now: "The final layer has no normalisation or activation, because the output is a signed and unbounded residual, and it is initialised to zero, which yields the persistence start of~\S\ref{sec:method:dt-residual}."
- **4a.33** [medium] §4.3.2 Message-Passing Graph Neural Network (The architecture used here) · `04-method.tex:394` (today `04-method.tex:671`) · **Done**: 2026-10-17 (as suggested)
  - Issue: 'Node update' already names the message-passing update $\psi$ (l. 291, l. 342 'every node update', Eq. 4.4). Using it for the residual state update makes the reader wonder which one is meant.
  - Was: "The node update is then $u_i + \Delta t \cdot \delta(f_i^{M})$, where $\delta$ denotes the decoder; this is Equation~\eqref{eq:method:residual-update} at node level."
  - Now: "The predicted next state of node $i$ is then $u_i + \Delta t \cdot \delta(f_i^{M})$, where $\delta$ denotes the decoder; this is Equation~\eqref{eq:method:residual-update} at node level."
- **4a.34** [medium] §4.3.2 Message-Passing Graph Neural Network (The architecture used here) · `04-method.tex:399` (today `04-method.tex:662`) · **Done**: 2026-10-17 (own wording)
  - Issue: The original head is described a second time, almost word for word from l. 306-309, and the reason for replacing it comes after the replacement has already been described. The paragraph also restates the decoder, the zero-init and the 'independent prediction'. (GPTZero labels the first sentence human and the rest AI.)
  - Was: "In the original, the output head is a one-dimensional convolution. It treats the final hidden vector of a node as a temporal signal and convolves along it to emit the $K$ bundled future steps \citep{Brandstetter2022}. This head exists to produce several time ..."
  - Now: "Because the framework predicts one step ($K = 1$, \S\ref{sec:method:framework}), the one-dimensional convolutional head of the original, which exists to emit the $K$ bundled steps, was replaced by an MLP decoder."
- **4a.35** [low] §4.3.2 Message-Passing Graph Neural Network (Differences from the original) · `04-method.tex:412` (today `04-method.tex:676`) · **Done**: 2026-10-17 (own wording)
  - Issue: 'Original' appears three times in two sentences, and 'the original entries' sounds as if the entries themselves were original.
  - Was: "Table~\ref{tab:method:mppde-diff} lists the main departures from the original MP-PDE \citep{Brandstetter2022}. The original entries refer to the published paper; the original was evaluated mainly on one-dimensional equations, with additional two-dimensional ..."
  - Now: "\paragraph{Summary of the modifications.} Table~\ref{tab:method:mppde-diff} summarises the modifications to MP-PDE \citep{Brandstetter2022}."
- **4a.36** [low] Table 4.1 caption · `04-method.tex:425` (today `04-method.tex:690`) · **Done**: 2026-10-17 (as suggested)
  - Issue: The possessive 'the original's aggregation' reads awkwardly, and it is not immediately clear that the sentence explains the 'Sum over neighbours' cell.
  - Was: "The original's aggregation is the sum written in its node-update equation; the paper does not describe the aggregation of its reference implementation."
  - Now: "For MP-PDE, the table gives the sum written in its node-update equation; the paper does not describe the aggregation used in its reference implementation."
- **4a.37** [medium] §4.3.2 Message-Passing Graph Neural Network (Differences from the original) · `04-method.tex:458` · **Done**: 2026-10-17 (own wording)
  - Issue: A recap made of short sentences with the same syntax. The last sentence pairs two changes with two reasons in an implicit 'respectively' construction that the reader has to untangle, and 'behaves identically under the training curriculum' leaves open 'identically to what'.
  - Was: "Each change is motivated where it is introduced. The irregular time handling and the removal of bundling follow from the clinical visit schedule (\S\ref{sec:method:framework}, \S\ref{sec:method:dt-residual}). The conditioning vector replaces the unknown ..."
  - Review suggested: "Each change is motivated where it is introduced: the irregular time handling and the removal of bundling by the clinical visit schedule (\S\ref{sec:method:framework}, \S\ref{sec:method:dt-residual}), the conditioning vector by the unknown equation identity, ..." (the passage was cut or rewritten; no single sentence corresponds today)

## Chapter 4, graph construction and the other operators

Source: `reviews/editorial-2026-10-01/04b-method-operators.md`.

- **4b.1** [low] §4.3.3 Graph Construction on an Anisotropic Grid · `04-method.tex:470` · **Done**: 2026-10-17 (own wording)
  - Issue: 'turns out' is narrative phrasing that presents a Chapter 5 finding as a discovery, and the subsection opens with a verdict before saying what the graph does.
  - Was: "The graph on which messages travel turns out to be the most consequential design decision of the graph solver."
  - Review suggested: "The graph determines which nodes exchange messages, and its construction proved to be the most consequential design decision of the graph solver." (the passage was cut or rewritten; no single sentence corresponds today)
- **4b.2** [low] §4.3.3 Graph Construction on an Anisotropic Grid · `04-method.tex:477` (today `04-method.tex:738`) · **Done**: 2026-10-17 (own wording)
  - Issue: The one-word verdict 'fails' is followed by a colon explanation, a reveal structure. Naming the concrete failure is plainer and more precise.
  - Was: "A $k$-nearest-neighbour graph built on these physical positions fails. The twelve physically nearest neighbours of every node all lie in its own row: measured over the grid, 100\,\% of the edges connect nodes in the same row and none cross rows."
  - Now: "The usual construction on irregular meshes, a $k$-nearest-neighbour graph, connects each node to the $k$ nodes at the smallest Euclidean distance between their physical positions (Figure~\ref{fig:method:stencils}a)."
- **4b.3** [medium] §4.3.3 Graph Construction on an Anisotropic Grid · `04-method.tex:481` (today `04-method.tex:743`) · **Done**: 2026-10-17 (own wording)
  - Issue: 'the retina falls apart into ... strands' is dramatic imagery. The retina does not change; only the graph's connectivity over the grid does.
  - Was: "No information can cross from one row to the next at any network depth, and the two-dimensional retina falls apart into 49 independent one-dimensional strands."
  - Now: "Message passing on such a graph runs along rows only, no information can cross from one row to the next at any network depth, and the grid decomposes into 49 independent one-dimensional rows."
- **4b.4** [low] §4.3.3 Graph Construction on an Anisotropic Grid · `04-method.tex:486` (today `04-method.tex:752`) · **Done**: 2026-10-17 (own wording)
  - Issue: Two geometric descriptions (a disc and a diamond) follow each other without saying why they are the same set.
  - Was: "With $k = 12$, and without self-loops, the neighbourhood of an interior node is exactly the index-space disc of squared radius four, a diamond of radius two."
  - Now: "With $k = 12$ and without self-loops, the neighbourhood of an interior node is exactly the set of nodes at squared index distance at most four."
- **4b.5** [low] §4.3.3 Graph Construction on an Anisotropic Grid · `04-method.tex:496` · **Done**: 2026-10-17 (own wording)
  - Issue: 'lopsided' is colloquial for a method description, and the sentence anticipates the 'connectivity but not reach' summary two paragraphs later.
  - Was: "This index-space graph solves the connectivity problem, but its physical reach is lopsided."
  - Review suggested: "This index-space graph restores two-dimensional connectivity, but its physical reach differs strongly between the two axes." (the passage was cut or rewritten; no single sentence corresponds today)
- **4b.6** [low] §4.3.3 Graph Construction on an Anisotropic Grid · `04-method.tex:504` · **Done**: 2026-10-17 (own wording)
  - Issue: An announcement sentence says that a comparison is coming instead of making it, a paragraph-opening signpost.
  - Was: "This reach can be compared with the scale on which the lesion changes. Between two visits 180 days apart, the GA front advances a median of about 12 columns, or roughly 0.07\,mm."
  - Review suggested: "For comparison, the GA front advances a median of about 12 columns, or roughly 0.07\,mm, between two visits 180 days apart." (the passage was cut or rewritten; no single sentence corresponds today)
- **4b.7** [medium] §4.3.3 Graph Construction on an Anisotropic Grid · `04-method.tex:507` (today `04-method.tex:776`) · **Done**: 2026-10-17 (as suggested)
  - Issue: The middle sentence stands alone as an aphoristic closer that repeats l. 496. The cleft 'This is why ...' and the therefore/thus chain make the rhythm machine-like, and 'even' is emphasis only.
  - Was: "A single hop along a row therefore covers only a small fraction of the distance the front typically moves between two visits, and even the four columns reached after two rounds are about a third of the median advance. The index-space graph thus solves the ..."
  - Now: "A single hop along a row therefore covers only a small fraction of the distance the front typically moves between two visits, and the four columns reached after two rounds are about a third of the median advance. The index-space graph thus restores connectivity but not reach, which motivates a second graph ..."
- **4b.8** [medium] §4.3.3 Graph Construction on an Anisotropic Grid · `04-method.tex:527` (today `04-method.tex:801`) · **Done**: 2026-10-17 (own wording)
  - Issue: 'its weights ... stay unchanged' can be read as reusing trained weights, when the point is that the architecture and the parameter count are the same; the stencil model is trained separately. The paragraph also comes after the forward pointer to Chapter 5, so the subsection ends on an afterthought.
  - Was: "The dilated stencil replaces only the edge set. The network, its weights and every other component stay unchanged, and the stencil adds no parameters."
  - Now: "The dilated stencil changes only the edge set; the network architecture and every other component are the same as on the index-space graph, and the stencil adds no parameters."
- **4b.9** [medium] Figure 4.2 caption · `04-method.tex:550` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: The appositive 'the number of rounds of the canonical configuration' is followed by a colon and two reach values, so it is not clear at first that the values describe the two-round reach.
  - Was: "Filled markers are reached in one message-passing round, open markers in two, the number of rounds of the canonical configuration: about $\pm 4$ columns ($\pm 0.023$\,mm) along a row with the $k$-NN graph, against $\pm 42$ columns ($\pm 0.24$\,mm) with the ..."
  - Review suggested: "Filled markers are reached in one message-passing round and open markers in two, the number of rounds used by the canonical configuration. After two rounds, a node reaches about $\pm 4$ columns ($\pm 0.023$\,mm) along a row with the $k$-NN graph and $\pm 42$ ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4b.10** [medium] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid · `04-method.tex:563` (today `04-method.tex:846`) · **Done**: 2026-10-18 (sentence kept; moved or its context changed)
  - Issue: The subsection moves from graphs to grid operators without a bridge, and it does not connect 'dense' to the roadmap's 'dense grid operators' or to the grid-operator inputs of §4.3.1.
  - Was: "The first dense operator is a U-Net \citep{Ronneberger2015}."
  - Now: "The first dense operator is a U-Net \citep{Ronneberger2015}."
- **4b.11** [low] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid · `04-method.tex:582` · **Done**: 2026-10-18 (own wording)
  - Issue: An em-dash aside sits in the middle of the sentence. The count of normalised sites served only the graph U-Net comparison (now commented out) and the \iffalse'd §5.4.4, so the reader is not told why it matters.
  - Was: "With nine such blocks --- an input stage, four downsampling and four upsampling stages --- the network has 18 normalised convolution sites."
  - Review suggested: "The network has nine such blocks (an input stage, four downsampling and four upsampling stages) and therefore 18 normalised convolutions. If the number serves no later comparison, consider cutting the sentence." (the passage was cut or rewritten; no single sentence corresponds today)
- **4b.12** [medium] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid · `04-method.tex:587` (today `04-method.tex:869`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'pooled four times' reads as four pooling operations, but rows are pooled twice, by a total factor of four (columns, in turn, are pooled four times). 'aspect of the grid' is vague for the ratio of row to column spacing.
  - Was: "Rows are pooled four times and columns sixteen times, which reduces the 21:1 aspect of the grid to about 5:1 without removing it."
  - Now: "Rows are downsampled by a factor of four in total and columns by a factor of sixteen, which reduces the 21:1 ratio of row to column spacing to about 5:1 without removing it."
- **4b.13** [low] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid · `04-method.tex:589` (today `04-method.tex:872`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The 'a weaker control, not a stronger one' antithesis is a rhetorical closer; 'weaker control' alone carries the point.
  - Was: "The schedule was deliberately not tuned further, because a comparison model whose geometry has been optimised against this dataset would be a weaker control, not a stronger one."
  - Now: "The schedule was deliberately not tuned further: a comparison model whose geometry had been optimised on this dataset would make a weaker control."
- **4b.14** [low] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid · `04-method.tex:595` (today `04-method.tex:877`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'base width' is used without explanation; readers outside the U-Net literature may not know it is the channel count of the first stage.
  - Was: "A base width of five gives 83\,081 parameters."
  - Now: "A base width of five, that is, five channels at the input stage, gives 83\,081 parameters."
- **4b.15** [low] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid · `04-method.tex:620` (today `04-method.tex:903`) · **Done**: 2026-10-18 (as suggested)
  - Issue: There is an 'X, not Y' opener, and 'This thesis' acts as an agent, which breaks the passive house style used elsewhere.
  - Was: "The domain here is a crop, not a periodic physical domain (\S\ref{sec:data:spatial}). This thesis therefore zero-pads the field by about one eighth per axis before the transform, from $49 \times 1024$ to $56 \times 1152$, and crops it back after the spectral ..."
  - Now: "Because the domain here is a crop and not a periodic physical domain (\S\ref{sec:data:spatial}), the field is zero-padded by about one eighth per axis before the transform, from $49 \times 1024$ to $56 \times 1152$, and cropped back after the spectral blocks; the original does not pad and relies on the local linear ..."
- **4b.16** [medium] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid · `04-method.tex:625` (today `04-method.tex:908`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The first sentence promises a reason for the mode count, but the explanation only justifies equal counts on both axes, not the value 14. The em-dash callback is a contrast tell.
  - Was: "The mode count follows from the geometry. The physical domain is nearly square ($5.94 \times 5.82$\,mm), so equal mode counts give nearly equal physical bandwidth on both axes --- the property the index-space graph of~\S\ref{sec:method:graph} lacks."
  - Now: "The equal mode count on both axes follows from the geometry: the physical domain is nearly square ($5.94 \times 5.82$\,mm), so equal mode counts give nearly equal physical bandwidth on both axes, a property the index-space graph of~\S\ref{sec:method:graph} does not have."
- **4b.17** [low] §4.3.4 Dense Operators: U-Net, FNO and a Local-Kernel Hybrid · `04-method.tex:643` (today `04-method.tex:926`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The 'without ..., without ... and without ...' triad is a symmetric list that reads as mechanical.
  - Was: "Unlike the original, it operates at a single training resolution, without mean subtraction, without rescaling and without discrete-continuous convolutions; it is therefore not the resolution-consistent operator of that paper."
  - Now: "Unlike the original, it operates at a single training resolution and uses no mean subtraction, rescaling or discrete-continuous convolutions, so it is not the resolution-consistent operator of that paper."
- **4b.18** [medium] §4.3.5 The Locality Floors · `04-method.tex:682` (today `04-method.tex:961`) · **Done**: 2026-10-18 (own wording)
  - Issue: 'at all' is emphasis filler, and the sentence repeats the §4.3 introduction (l. 211, 'Two truncated graph networks test how much spatial context is needed at all') almost word for word.
  - Was: "Two arms test how much spatial context is needed at all."
  - Now: "Two arms are used to measure how much spatial context the prediction needs."
- **4b.19** [low] §4.3.5 The Locality Floors · `04-method.tex:687` (today `04-method.tex:971`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'at all' is emphasis again, and three short clauses state the same consequence one after another.
  - Was: "The per-pixel floor uses no message passing at all. Each node's next state then depends only on its own state and its conditioning inputs, and the model has no spatial context; it has 14\,795 parameters."
  - Now: "The per-pixel floor uses no message passing, so each node's next state depends only on its own state and its conditioning inputs and the model has no spatial context; it has 14\,795 parameters."
- **4b.20** [medium] §4.3.6 The Finite Element Network · `04-method.tex:697` · **Done**: 2026-10-18 (own wording)
  - Issue: The mirrored short pair 'This is X. It is not Y.' and 'by construction rather than' are typical tells, and 'which is tested' grammatically attaches to 'a claim'.
  - Was: "It is the only operator whose output is defined as a time derivative by construction rather than as a next state. This is a property of the architecture. It is not a claim that the trained model behaves as a valid continuous-time system, which is tested in ..."
  - Review suggested: "Its architecture defines the output as a time derivative and not as a next state; it is the only operator in the survey that does so. Whether the trained model behaves as a valid continuous-time system is a separate question, tested in ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4b.21** [low] §4.3.6 The Finite Element Network · `04-method.tex:708` (today `04-method.tex:992`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The appositive 'a network, the free-form term,' equates a network with a term in the middle of a long noun stack, so the sentence has to be read twice.
  - Was: "The inner products are factored so that a network, the free-form term, predicts one coefficient per cell, vertex and feature from the time, the cell centre, the local vertex coordinates and the vertex features."
  - Now: "The inner products are factored so that a network predicts one coefficient per cell, vertex and feature from the time, the cell centre, the local vertex coordinates and the vertex features; this network is the free-form term."
- **4b.22** [low] §4.3.6 The Finite Element Network · `04-method.tex:716` (today `04-method.tex:1001`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'dopri5' is a software name that is not explained at first use.
  - Was: "Both networks are tanh MLPs, and the resulting ODE is solved with the adaptive dopri5 solver."
  - Now: "Both networks are tanh MLPs, and the resulting ODE is solved with the adaptive Dormand--Prince solver (dopri5)."
- **4b.23** [medium] §4.3.6 The Finite Element Network · `04-method.tex:722` (today `04-method.tex:1008`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'equal-area lattice' and 'uniform mesh' name the same object in consecutive sentences, 'machinery ... makes a difference' is informal, and 'hyperedges' is not explained.
  - Was: "On this equal-area lattice the lumped assembly is exactly a mean over the triangles adjacent to a node. On a uniform mesh, the FEN is therefore a message-passing network over triangle hyperedges with mean aggregation, and the finite-element machinery only ..."
  - Now: "On this equal-area lattice, the lumped assembly is exactly a mean over the triangles adjacent to a node. The FEN is therefore a message-passing network with mean aggregation over triangles, each linking three nodes, and its finite-element formulation differs from such a network only at the boundary."
- **4b.24** [low] §4.3.6 The Finite Element Network · `04-method.tex:736` (today `04-method.tex:1022`) · **Done**: 2026-10-18 (as suggested)
  - Issue: This repeats the statement about the original from two paragraphs earlier (l. 715-716), and the 'Neither ... nor ..., so reading it ... rests on' construction is heavy.
  - Was: "Neither the original nor this implementation makes the velocity divergence-free across triangles, so reading it as a physical advection speed rests on an assumption the model does not enforce globally."
  - Now: "As in the original, the velocity is not divergence-free across triangles, so reading it as a physical advection speed rests on an assumption that the model does not enforce globally."
- **4b.25** [HIGH] §4.3.6 The Finite Element Network · `04-method.tex:741` (today `04-method.tex:1026`) · **Done**: 2026-10-02 (high-severity pass)
  - Issue: 'built on every seventh column' makes the reader picture a subsampled mesh over one seventh of the nodes. In fact the mesh consists of seven interleaved triangulations that together use every node, which is why it has almost as many triangles as the full mesh. As written, the mesh structure is likely to be misread.
  - Was: "The transport term runs on its own coarser mesh, built on every seventh column (97\,632 triangles), while the free-form term uses the full-resolution mesh."
  - Now: "The transport term runs on its own coarser mesh, made of seven interleaved triangulations, each of which connects every seventh column (97\,632 triangles in total), while the free-form term uses the full-resolution mesh."
- **4b.26** [low] §4.3.6 The Finite Element Network · `04-method.tex:749` (today `04-method.tex:1035`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'autonomous' is not defined at first use, and 'learned dynamics' is wording the project otherwise avoids.
  - Was: "The time is not an input, so the learned dynamics are autonomous, a variant the original paper explicitly allows."
  - Now: "The time is not an input, so the learned time derivative has no explicit dependence on time (it is autonomous), a variant the original paper explicitly allows."
- **4b.27** [low] §4.3.6 The Finite Element Network, paragraph 'Two forms of the transport operator' · `04-method.tex:768` (today `04-method.tex:1054`) · **Done**: 2026-10-18 (own wording)
  - Issue: The first sentence repeats the run-in paragraph heading almost word for word.
  - Was: "\paragraph{Two forms of the transport operator.} Two forms of the assembled transport operator were trained. The first is the Galerkin form described above, as in the original."
  - Now: "The assembled transport operator was trained in two forms."
- **4b.28** [medium] §4.3.6 The Finite Element Network, paragraph 'Two forms of the transport operator' · `04-method.tex:770` (today `04-method.tex:1055`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'as pure transport should: content is moved, not created' combines a colon reveal with an aphoristic 'X, not Y' antithesis.
  - Was: "At a constant velocity and away from the edge of the domain, it conserves a discrete energy of the state, the mass-weighted sum of squares $u^\top M u$, as pure transport should: content is moved, not created."
  - Now: "At a constant velocity and away from the edge of the domain, it conserves a discrete energy of the state, the mass-weighted sum of squares $u^\top M u$, as expected of pure transport, which moves content without creating it."
- **4b.29** [medium] §4.3.6 The Finite Element Network, paragraph 'Two forms of the transport operator' · `04-method.tex:773` (today `04-method.tex:1058`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'and' reads as if both conditions must hold together, but the previous sentence makes conservation require both a constant velocity and the interior, so either violation breaks it. The elliptical 'it does not' adds to the ambiguity.
  - Was: "At the edge of the crop, and for a velocity that varies from triangle to triangle, it does not. No flux term is assembled at the boundary, so transported content accumulates there, and the operator has modes that grow instead of travelling."
  - Now: "At the edge of the crop, or where the velocity varies from triangle to triangle, it does not conserve this energy. No flux term is assembled at the boundary, so transported content accumulates there, and the operator has modes that grow instead of travelling."
- **4b.30** [low] §4.3.6 The Finite Element Network, paragraph 'Two forms of the transport operator' · `04-method.tex:777` (today `04-method.tex:1063`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The equation introduces $L_{\text{skew}}$, but the text never says what 'skew' refers to, so the subscript appears unexplained.
  - Was: "It keeps only the energy-conserving part of the Galerkin operator $L$,"
  - Now: "It keeps only the part of the Galerkin operator $L$ that is skew-adjoint with respect to the mass matrix $M$, which is its energy-conserving part,"
- **4b.31** [medium] §4.3.6 The Finite Element Network · `04-method.tex:788` · **Done**: 2026-10-18 (own wording)
  - Issue: 'turned out' is narrative phrasing, and 'Unstable has a specific meaning here.' is a signpost sentence that delays the definition.
  - Was: "The Galerkin form turned out to be unstable, and the T-FEN reported in Chapter~\ref{ch:experiments} uses the energy-conserving form; the Galerkin runs are reported in~\S\ref{sec:experiments:validity:tfen}. \emph{Unstable} has a specific meaning here."
  - Review suggested: "The Galerkin form proved unstable in the sense defined below, so the T-FEN reported in Chapter~\ref{ch:experiments} uses the energy-conserving form; the Galerkin runs are reported in~\S\ref{sec:experiments:validity:tfen}. (Then begin the next sentence: ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4b.32** [medium] §4.3.6 The Finite Element Network · `04-method.tex:794` · **Done**: 2026-10-18 (own wording)
  - Issue: 'late epochs' is used here for the first time in the thesis and is defined only in §5.1.3, so the criterion cannot be followed at this point.
  - Was: "A run is called stable if, in this free-running rollout, the root mean squared error of the mask channel and of the layer channels, both in normalised units, stays at or below 5 on at least 19 of its 20 late epochs."
  - Review suggested: "A run is called stable if, in this free-running rollout, the root mean squared error of the mask channel and of the layer channels, both in normalised units, stays at or below 5 on at least 19 of its 20 late epochs (epochs 10 to 29; ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4b.33** [medium] §4.3.7 Fixed-Step Runge–Kutta Integration · `04-method.tex:816` (today `04-method.tex:1111`) · **Done**: 2026-10-18 (own wording)
  - Issue: The subsection opens with a negation followed by three uniformly short declaratives, a robotic rhythm.
  - Was: "The Runge--Kutta wrapper is not a backbone. It is placed around any backbone and changes only how the backbone's output is turned into the next state. It adds no parameters."
  - Now: "The Runge--Kutta wrapper is placed around an operator and changes only how the operator's output is turned into the next state; it adds no parameters."
- **4b.34** [medium] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Euler and RK4' · `04-method.tex:825` (today `04-method.tex:1133`) · **Done**: 2026-10-18 (own wording)
  - Issue: 'used in every reported run' literally says that every run in the thesis uses RK4, right after the statement that the canonical update is one Euler step. The intended scope is every reported model trained with the wrapper. The pronoun 'it' is also distant from 'the operator'.
  - Was: "The classical fourth-order scheme (RK4), used in every reported run, evaluates it four times per step and takes a weighted average \citep{Butcher1987, Hairer1993}."
  - Now: "The classical fourth-order scheme (RK4) \citep{Runge1895,Kutta1901} evaluates the operator four times per step and takes a weighted average \citep{Butcher1987, Hairer1993}; every reported model trained with the wrapper uses it."
- **4b.35** [low] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Euler and RK4' · `04-method.tex:829` (today `04-method.tex:1137`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The text switches between 'graph' and 'eye' for the same batch element, and 'graph' is odd for the dense operators the wrapper also serves.
  - Was: "The sub-step length is set per graph, either as $h = \Delta t / n$ or from a physical step length in days, with the number of sub-steps rounded up from the ratio of the interval to that length. An eye is therefore integrated with the same steps whether it is ..."
  - Now: "The sub-step length is set separately for each eye in a batch, either as $h = \Delta t / n$ or from a physical step length in days, with the number of sub-steps rounded up from the ratio of the interval to that length. An eye is therefore integrated with the same steps whether it is batched with others or evaluated ..."
- **4b.36** [low] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Euler and RK4' · `04-method.tex:835` (today `04-method.tex:1143`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'unit check' is ambiguous: it can mean a check of physical units or a unit test.
  - Was: "As a unit check, the observed convergence orders on the test problem $\mathrm{d}u / \mathrm{d}t = -\lambda u$ are 0.99, 2.04, 2.04 and 4.35 for the Euler, midpoint, Heun and RK4 schemes, close to their nominal orders of one, two, two and four."
  - Now: "As a check of the implementation, the observed convergence orders on the test problem $\mathrm{d}u / \mathrm{d}t = -\lambda u$ are 0.99, 2.04, 2.04 and 4.35 for the Euler, midpoint, Heun and RK4 schemes, close to their nominal orders of one, two, two and four."
- **4b.37** [medium] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'The autonomous field' · `04-method.tex:841` (today `04-method.tex:1151`) · **Done**: 2026-10-18 (own wording)
  - Issue: The passage personifies the operator and the integrator ('no longer knows', 'states', 'decides') and pre-empts a misreading with a colon sentence. The heading term 'autonomous' is not defined in the paragraph.
  - Was: "Inside the wrapper, the $\Delta t$ entry of the operator's conditioning vector is set to zero. The operator then no longer knows how long the interval is. Its output only states how fast the state is changing at the current moment, and the integrator alone ..."
  - Now: "Inside the wrapper, the $\Delta t$ entry of the operator's conditioning vector is therefore set to zero, so the operator receives no information about the length of the interval."
- **4b.38** [medium] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'The autonomous field' · `04-method.tex:848` (today `04-method.tex:1159`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The requirement is stated without its reason, so the link to the preceding explanation of the rate is left to the reader.
  - Was: "The wrapper requires the $\Delta t$-multiplied residual form of Equation~\eqref{eq:method:residual-update}."
  - Now: "The wrapper requires the $\Delta t$-multiplied residual form of Equation~\eqref{eq:method:residual-update}, because without the multiplication by $\Delta t$ the operator's output is not a rate and cannot be integrated."
- **4b.39** [medium] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Why the wrapper exists' · `04-method.tex:854` · **Done**: 2026-10-18 (own wording)
  - Issue: 'It' has no antecedent after the heading, the reach clause repeats §4.3.6 (l. 756-757), and the last sentence buries its verb behind a long clausal subject. The paragraph would also work better directly after the subsection's opening paragraph.
  - Was: "\paragraph{Why the wrapper exists.} It has three uses. First, the finite-element network outputs a rate and needs an integrator (\S\ref{sec:method:family:fen}); since one evaluation couples only nodes that share a triangle, its spatial reach grows with the ..."
  - Review suggested: "\paragraph{Uses of the wrapper.} The wrapper has three uses. First, the finite-element network outputs a rate and needs an integrator (\S\ref{sec:method:family:fen}). Second, it allows the integration order to be tested on its own: the same backbone trained ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4b.40** [medium] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Jump and continuous time' · `04-method.tex:865` (today `04-method.tex:1166`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The rhetorical opener 'Nothing requires', the colon reveal 'must satisfy exactly this:' and the colloquial 'the answer' together read as staged.
  - Was: "Nothing requires that two jumps of length $\Delta t / 2$ lead to the same state as one jump of length $\Delta t$. A continuous-time model must satisfy exactly this: splitting the interval into more or finer steps must not change the answer."
  - Now: "Training does not require two jumps of length $\Delta t / 2$ to lead to the same state as one jump of length $\Delta t$. In a continuous-time model, by contrast, splitting the interval into more or finer steps must not change the prediction."
- **4b.41** [low] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Jump and continuous time' · `04-method.tex:869` (today `04-method.tex:1170`) · **Done**: 2026-10-18 (as suggested)
  - Issue: A 45-word sentence joins a finding and a test procedure with ', and they', which makes it hard to read in one pass.
  - Was: "\citet{Ott2021} show that a model trained with an overly coarse step can reach high accuracy and still lose this property, and they test it by evaluating the trained model with solvers of equal or smaller discretisation error and checking whether its ..."
  - Now: "\citet{Ott2021} show that a model trained with an overly coarse step can reach high accuracy and still lose this property. They test it by evaluating the trained model with solvers of equal or smaller discretisation error and checking whether its predictions stay the same."
- **4b.42** [low] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Jump and continuous time' · `04-method.tex:874` (today `04-method.tex:1175`) · **Done**: 2026-10-18 (own wording)
  - Issue: 'trained ... after training' is redundant, and the wrapper, the actual agent, appears only at the end.
  - Was: "Because any trained backbone can be integrated with different schemes and step counts after training, the wrapper makes this solver-swap test possible."
  - Now: "Because the wrapper can integrate any trained operator with other schemes and step counts, it makes this solver-swap test possible."
- **4b.43** [low] §4.3.7 Fixed-Step Runge–Kutta Integration, paragraph 'Jump and continuous time' · `04-method.tex:876` (today `04-method.tex:1177`) · **Done**: 2026-10-18 (own wording)
  - Issue: The Method chapter previews Chapter 5 results and closes on a verdict, while §4.2.1 names the same diagnostic without previewing its outcome. The colon reveal and the 'therefore ..., but ...' closer add to the machine-like tone.
  - Was: "Its outcome is reported in~\S\ref{sec:experiments:validity:swap}: the canonical model fails it, whereas the same network trained under the RK4 wrapper passes it, as does the finite-element network. A continuous-time model can therefore be obtained by training ..."
  - Now: "Its outcome is reported in~\S\ref{sec:experiments:validity:swap}, and the accuracy of the models trained with the wrapper in~\S\ref{sec:experiments:ablations:time}."
- **4b.44** [medium] §4.3.8 Parameter Matching · `04-method.tex:889` (today `04-method.tex:1184`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'Every operator' is contradicted a few sentences later by the floors, which are not matched, and the doubled 'so that ... so that' makes the second sentence clumsy.
  - Was: "Every operator is matched in size to the canonical graph solver of~\S\ref{sec:method:graph}, which has 67\,147 parameters. The widths are chosen so that each arm comes as close to this count as its width granularity allows, so that differences between arms ..."
  - Now: "Every architecture arm is matched in size to the canonical graph solver of~\S\ref{sec:method:graph}, which has 67\,147 parameters: its width is chosen to come as close to this count as the width granularity allows, so that differences between arms cannot be attributed to extra parameters."
- **4b.45** [medium] §4.3.8 Parameter Matching · `04-method.tex:894` (today `04-method.tex:1193`) · **Done**: 2026-10-18 (as suggested)
  - Issue: '..., not an architecture arm' appears twice in a mirrored pair, the second time with a colon reveal, and the two parallel exceptions are split across a paragraph break.
  - Was: "All architecture arms lie within a factor of 1.25 of the reference. The one-hop floor lies below this band because it is a rung of the locality ladder of~\S\ref{sec:method:family:floors}, not an architecture arm. The per-pixel floor also lies outside the ..."
  - Now: "All architecture arms lie within a factor of 1.25 of the reference. The two floors lie below this band because they are not architecture arms: the one-hop floor is a rung of the locality ladder of~\S\ref{sec:method:family:floors}, and the per-pixel floor, with about a fifth of the parameters, is a control that marks ..."
- **4b.46** [low] §4.3.8 Parameter Matching · `04-method.tex:901` (today `04-method.tex:1189`) · **Done**: 2026-10-18 (own wording)
  - Issue: The sentence has a long clausal subject before its verb, and it sits in the per-pixel-floor paragraph, which it is unrelated to.
  - Was: "Whether the size at which the arms are matched affects the comparison is tested separately, by scaling every architecture class from about a quarter to about four times its size (\S\ref{sec:experiments:ablations:capacity})."
  - Now: "experiment tests whether the size at which the arms are matched affects the comparison, by scaling every architecture class from about a quarter to about four times its size (\S\ref{sec:experiments:ablations:capacity})."
- **4b.47** [low] §4.3.8 Parameter Matching · `04-method.tex:906` (today `04-method.tex:1200`) · **Done**: 2026-10-18 (own wording)
  - Issue: This nearly repeats §4.3.6 (l. 805-811), and the RK sentence repeats l. 818 and the table row. With the Table 4.2 caption, the same facts appear three times.
  - Was: "The free-form FEN control at width 96 has 34\,785 parameters, half the reference and a factor of 1.97 below the T-FEN it controls, because it is the T-FEN with the transport head removed (\S\ref{sec:method:family:fen}). A second free-form control at width 139 ..."
  - Now: "The free-form FEN control at width 96 has 34\,785 parameters, half the reference and a factor of 1.97 below the T-FEN it controls, because it is the T-FEN with the transport head removed (\S\ref{sec:method:family:fen}): of the T-FEN's 68\,503 parameters, 34\,785 belong to the free-form term and 33\,718 to the ..."
- **4b.48** [medium] Table 4.2 caption · `04-method.tex:919` (today `04-method.tex:1214`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The semicolon list ends in the elliptical 'the width-139 control is.', which is hard to parse after three appositive items.
  - Was: "Three arms lie outside this band: the per-pixel floor, a control without spatial context; the one-hop floor, a rung of the locality ladder and a truncation of the index-space arm; and the free-form FEN at width 96, which is not matched to the T-FEN it is ..."
  - Now: "Three arms lie outside this band: the per-pixel floor, a control without spatial context; the one-hop floor, a rung of the locality ladder and a truncation of the index-space arm; and the free-form FEN at width 96, which is smaller than the T-FEN it is compared with by a factor of 1.97. The free-form FEN at width 139 ..."

## Chapter 4, conditioning, training, implementation

Source: `reviews/editorial-2026-10-01/04c-method-conditioning-training.md`.

- **4c.1** [low] §4.4 Conditioning: Patient Covariates · `04-method.tex:956` · **Done**: 2026-10-18 (own wording)
  - Issue: The announcement promises 'how they enter', but the next sentences cover what the covariates are and what they cannot do. The mechanism follows only in the next paragraph, which has its own announcement ('How they enter the forward pass depends on the operator.').
  - Was: "This section describes how they enter the operators."
  - Review suggested: "Delete the sentence. The paragraph then moves directly from the pointer to §3.5 to the properties of the covariates, and l. 969 already introduces the mechanism. Optional: move 'The covariates are included because age and sex are plausible modulators of how ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4c.2** [low] §4.4 Conditioning: Patient Covariates · `04-method.tex:957` (today `04-method.tex:243`) · **Done**: as suggested
  - Issue: 'Graph-level' is GNN vocabulary (§4.3.2 uses it for the conditioning vector), but this section covers every operator, including the dense grid operators, which have no graph.
  - Was: "Both covariates are graph-level quantities: a visit has one value of each, and that value is shared by all $50\,176$ grid positions."
  - Now: "Both covariates are global quantities: a visit has one value of each, and that value is shared by all $50\,176$ grid positions."
- **4c.3** [medium] §4.4 Conditioning: Patient Covariates · `04-method.tex:960` (today `04-method.tex:246`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The second sentence restates the first in negative form, a mirror pair typical of the flagged tone. 'Shift' can also be read as an additive offset, although in the graph network the covariates enter every message and update nonlinearly.
  - Was: "Because the covariates carry no spatial information, they can only shift the prediction of an operator as a whole. They cannot point to a location on the grid or shape the lesion boundary locally."
  - Now: "Because the covariates carry no spatial information, they act on the prediction of an operator only as a whole and cannot point to a location on the grid or shape the lesion boundary locally."
- **4c.4** [low] §4.4 Conditioning: Patient Covariates · `04-method.tex:966` · **Done**: 2026-10-18 (own wording)
  - Issue: In this chapter 'slot' names the swappable operator slot, so reusing it for the θ_PDE input is a small collision. The 'since' clause gives the reason for needing a substitute but hangs off the end. The sentence also repeats §4.3.2 (l. 337-340) almost verbatim.
  - Was: "Together with $\Delta t$, they fill the slot that the equation features $\theta_{\text{PDE}}$ occupy in MP-PDE, since no governing equation with known coefficients exists for GA (\S\ref{sec:method:mppde})."
  - Review suggested: "Since no governing equation with known coefficients exists for GA, $\Delta t$ and the two covariates take the place of the equation features $\theta_{\text{PDE}}$ of MP-PDE (\S\ref{sec:method:mppde}). (Alternatively cut the sentence, since ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4c.5** [low] §4.4 Conditioning: Patient Covariates · `04-method.tex:975` · **Done**: 2026-10-18 (own wording)
  - Issue: The em-dash aside used for an inline list is a recurring flagged pattern. 'The free-form network of the Finite Element Network' repeats 'network', and both names are written out although FNO and FEN were abbreviated earlier (l. 42-43, 600, 696). §4.3.6 calls this part 'the free-form term'.
  - Was: "In the dense grid operators --- the U-Net, the Fourier Neural Operator and the local-kernel hybrid --- each covariate is an extra input channel holding a constant plane (\S\ref{sec:method:family:contract}). The free-form network of the Finite Element Network ..."
  - Review suggested: "In the dense grid operators (the U-Net, the FNO and the local-kernel hybrid), each covariate is an extra input channel holding a constant plane (\S\ref{sec:method:family:contract}). In the FEN, they are additional inputs to the free-form term ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4c.6** [low] §4.4 Conditioning: Patient Covariates · `04-method.tex:984` · **Done**: 2026-10-18 (own wording)
  - Issue: A one-sentence paragraph closes the section and reads as an orphan.
  - Was: "The covariates are enabled in the canonical configuration of every operator."
  - Review suggested: "Append the sentence to the end of the preceding paragraph, after the Runge--Kutta sentence." (the passage was cut or rewritten; no single sentence corresponds today)
- **4c.7** [low] §4.5 Training (introduction) · `04-method.tex:1021` · **Done**: 2026-10-18 (own wording)
  - Issue: The second sentence restates the first ('shared by every operator' / 'do not change between arms'), and the Table 4.3 caption says it a third time.
  - Was: "Everything in this section is shared by every operator of the survey (\S\ref{sec:method:family:contract}), and Table~\ref{tab:method:hparams} lists the settings. The objective, the curriculum and the optimisation settings do not change between arms, so that a ..."
  - Review suggested: "The objective, the curriculum and the optimisation settings are the same for every operator of the survey (\S\ref{sec:method:family:contract}), so that a difference between two arms can be attributed to the operator. Table~\ref{tab:method:hparams} lists the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4c.8** [low] §4.5.1 Objective · `04-method.tex:1041` (today `04-method.tex:308`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The reason for the higher mask weight ('The mask is the clinical target.') is separated from the weight by an unrelated normalisation sentence, which makes the sequence choppy.
  - Was: "The mask channel ($c = 0$) has the weight $w_0 = 5$, and each of the ten layer channels has the weight $w_c = 1$. Dividing by the mean weight keeps the scale of the term comparable to an unweighted MSE. The mask is the clinical target. The layer channels are ..."
  - Now: "The mask channel ($c = 0$), which is the clinical target, has the weight $w_0 = 5$, and each of the ten layer channels has the weight $w_c = 1$. The layer channels are auxiliary targets, but the operator must still predict them, because they are part of the next state that is fed back during a rollout. Dividing by the ..."
- **4c.9** [low] §4.5.1 Objective · `04-method.tex:1048` (today `04-method.tex:316`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'It addresses a property of the data.' is a teaser that names nothing and makes the reader wait for the next sentence.
  - Was: "The second term is a soft-Dice loss on the mask channel \citep{Milletari2016}, with the weight $\lambda_{\text{Dice}} = 5$. It addresses a property of the data. Between two consecutive visits, almost all mask pixels are unchanged, so a plain MSE is dominated ..."
  - Now: "The second term is a soft-Dice loss on the mask channel \citep{Milletari2016}, with the weight $\lambda_{\text{Dice}} = 5$. It counters an imbalance in the data: between two consecutive visits, almost all mask pixels are unchanged, so a plain MSE is dominated by static pixels and gives little gradient at the moving ..."
- **4c.10** [low] §4.5.1 Objective · `04-method.tex:1052` (today `04-method.tex:320`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'Settle on' is conversational and slightly anthropomorphic for an optimisation outcome.
  - Was: "A model trained on it can settle on copying its input."
  - Now: "A model trained on it can learn to copy its input."
- **4c.11** [low] §4.5.1 Objective · `04-method.tex:1054` (today `04-method.tex:323`) · **Done**: 2026-10-18 (as suggested)
  - Issue: Elsewhere in the chapter 'the original' means MP-PDE (or the original FEN). Here it means the soft-Dice loss of Milletari et al., and 'it' is ambiguous between the term and the soft mask.
  - Was: "Unlike the original, which scores a segmentation probability map, it is applied here to a regression output."
  - Now: "Unlike the original soft-Dice loss, which scores a segmentation probability map, the term is applied here to a regression output."
- **4c.12** [medium] §4.5.1 Objective · `04-method.tex:1074` · **Done**: 2026-10-18 (own wording)
  - Issue: 'One side effect is accepted.' is a teaser sentence, and it opens a new topic in the middle of the paragraph on per-eye scoring. 'Stretches the raw mask regression about the threshold' is opaque on first reading.
  - Was: "One side effect is accepted. The sigmoid of Equation~\eqref{eq:method:soft-mask} does not saturate at the physical mask values, so the term stretches the raw mask regression about the threshold."
  - Review suggested: "Start a new paragraph: "The soft-Dice term has one accepted side effect. Because the sigmoid of Equation~\eqref{eq:method:soft-mask} does not saturate at the physical mask values, the term stretches the raw mask predictions away from the threshold." Keep the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4c.13** [medium] §4.5.1 Objective · `04-method.tex:1081` · **Done**: 2026-10-18 (own wording)
  - Issue: 'Off in every reported run' contradicts the closing clause: §5.4.2 reports a run with the penalty at weight 2.0. 'Its weight is zero ...' repeats the opening sentence, and 'from both terms' is stranded after the parenthesis.
  - Was: "Two further options exist in the implementation and are off in every reported run. First, the loss can exclude grid positions whose target equals the fill value of the crop padding (\S\ref{sec:data:spatial}), from both terms. Since this option is off, the ..."
  - Review suggested: "Two further options exist in the implementation and are off for every operator of the comparison. First, the loss can exclude from both terms the grid positions whose target equals the fill value of the crop padding (\S\ref{sec:data:spatial}); since no ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4c.14** [low] §4.5.1 Objective · `04-method.tex:1089` · **Done**: 2026-10-18 (sentence kept; moved or its context changed)
  - Issue: This general statement about the loss is attached to the end of a paragraph about optional switches.
  - Was: "The same loss is used in training and in validation."
  - Review suggested: "Move the sentence to the end of the first paragraph of §4.5.1, directly after the definition of the weights." (the passage was cut or rewritten; no single sentence corresponds today)
- **4c.15** [low] §4.5.2 Time-Budgeted Pushforward Curriculum · `04-method.tex:1104` (today `04-method.tex:389`) · **Done**: 2026-10-18 (as suggested)
  - Issue: $U$ appears in the formula but is introduced only implicitly two sentences later ('Every reported run uses $U = 2$, so the largest budget is 360 days').
  - Was: "Each training pass draws a time budget $B$ uniformly from $\{0, 1, \dots, \min(e, U)\} \times 180$ days, where $e$ is the current epoch."
  - Now: "Each training pass draws a time budget $B$ uniformly from $\{0, 1, \dots, \min(e, U)\} \times 180$ days, where $e$ is the current epoch and $U$ the largest number of 180-day units in a budget."
- **4c.16** [low] §4.5.2 Time-Budgeted Pushforward Curriculum · `04-method.tex:1109` (today `04-method.tex:395`) · **Done**: 2026-10-18 (as suggested)
  - Issue: A bare math expression as the object of 'Because of the' reads awkwardly, and 'ramps in' is informal and vague.
  - Was: "Because of the $\min(e, U)$, the horizon ramps in over the first $U$ epochs; after that, budgets of 0, 180 and 360 days are drawn with equal probability."
  - Now: "Because the upper limit is $\min(e, U)$, the largest budget grows by 180 days per epoch over the first $U$ epochs; after that, budgets of 0, 180 and 360 days are drawn with equal probability."
- **4c.17** [medium] §4.5.2 Time-Budgeted Pushforward Curriculum · `04-method.tex:1124` (today `04-method.tex:410`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The 'This is also why' cleft and the emphatic 'at all' are flagged-tone markers, and 'never ... never' repeats. The second reason for the 180-day base arrives a paragraph after the base was introduced.
  - Was: "This is also why the base is 180 days and not the shortest interval of 90 days. Under the undershoot rule, a 90-day budget can never chain two visits (\S\ref{sec:data:temporal}), and the curriculum would never unroll at all."
  - Now: "The undershoot rule is also the reason for the 180-day base: a budget of 90 days, the shortest interval, can never chain two visits (\S\ref{sec:data:temporal}), so the curriculum would not unroll."
- **4c.18** [low] §4.5.2 Time-Budgeted Pushforward Curriculum · `04-method.tex:1135` (today `04-method.tex:420`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'And combined' trails at the end of the clause, and the 'which is why' construction is a recurring explanatory tell.
  - Was: "The group losses are weighted by the share of the batch each group holds and combined. The rollout runs in training mode, which is why no operator may use batch statistics (\S\ref{sec:method:family:contract})."
  - Now: "The group losses are combined, each weighted by the share of the batch its group holds. Because the rollout runs in training mode, no operator may use batch statistics (\S\ref{sec:method:family:contract})."
- **4c.19** [low] §4.5.3 Optimisation · `04-method.tex:1145` (today `04-method.tex:431`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'From epoch 5 on' is colloquial, and the parenthesis is loosely attached.
  - Was: "The learning rate is multiplied by 0.4 from epoch 5 on and again from epoch 20 on, counting epochs from 0 (the first five epochs run at the initial rate)."
  - Now: "The learning rate is multiplied by 0.4 at the start of epoch 5 and again at the start of epoch 20, counting from 0, so the first five epochs run at the initial rate."
- **4c.20** [medium] §4.5.3 Optimisation · `04-method.tex:1149` · **Done**: 2026-10-18 (own wording)
  - Issue: A 'pass' is defined here, after §4.5.2 has already built the curriculum on 'each training pass' (l. 1104), and four very short sentences in a row read like a list.
  - Was: "Training runs for 30 epochs. One epoch consists of 20 passes. In each pass, a new time budget is drawn, and every training eye contributes one randomly chosen start window that can realise it. The batch size is four eyes."
  - Review suggested: "In §4.5.2, open the second paragraph with: "Training proceeds in passes; in each pass, every training eye contributes one randomly chosen start window." (The budget is then introduced by the existing 'Each training pass draws a time budget ...', and ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4c.21** [medium] §4.5.3 Optimisation · `04-method.tex:1156` (today `04-method.tex:440`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The colon introduces a restatement of the same fact ('separately for each module' / 'each module is clipped by its own norm'), a tautological colon reveal typical of the flagged tone.
  - Was: "Gradients are clipped to a norm of 1.0, separately for each trainable module: each module is clipped by its own gradient norm, so that a large gradient in one module cannot shrink the updates of another."
  - Now: "Gradients are clipped to a norm of 1.0 separately for each trainable module, so that a large gradient in one module cannot shrink the updates of another."
- **4c.22** [medium] §4.5.3 Optimisation · `04-method.tex:1163` · **Done**: 2026-10-18 (own wording)
  - Issue: 'Every reported run uses the seed 42' contradicts the second half of the same sentence (seed-7 runs are reported), and 'the seed 42' is unidiomatic. The inverted clause 'which epochs ..., and why, is set out in' is hard to parse.
  - Was: "Every reported run uses the seed 42; replication runs with the seed 7 are reported in Chapter~\ref{ch:experiments}. The model is validated on the held-out fold after every epoch (\S\ref{sec:data:splits}); which epochs enter the reported numbers, and why, is ..."
  - Review suggested: "Unless stated otherwise, every reported run uses seed 42; replication runs with seed 7 are reported in Chapter~\ref{ch:experiments}. The model is validated on the held-out fold after every epoch (\S\ref{sec:data:splits}); \S\ref{sec:experiments:protocol} sets ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **4c.23** [low] Table 4.3 caption · `04-method.tex:1172` (today `04-method.tex:457`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The second sentence repeats the first.
  - Was: "Training settings shared by every operator of the survey. None of these settings changes between arms."
  - Now: "Training settings, identical for every operator of the survey."
- **4c.24** [medium] Table 4.3 (Learning rate row) · `04-method.tex:1181` (today `04-method.tex:465`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The table says 'after epochs 5 and 20', but the text says 'from epoch 5 on ... counting epochs from 0'. Read literally, the two describe schedules one epoch apart. NOTES records that 'after epoch 5' was corrected in the text, but the table was not updated.
  - Was: "Learning rate & $2 \times 10^{-3}$, multiplied by 0.4 after epochs 5 and 20"
  - Now: "Learning rate & $2 \times 10^{-3}$, multiplied by 0.4 at the start of epochs 5 and 20 (counted from 0)"
- **4c.25** [low] §4.6 Implementation Details · `04-method.tex:1205` (today `04-method.tex:1255`) · **Done**: as suggested
  - Issue: The tense switches from past ('was trained') to present ('are submitted') within one sentence.
  - Was: "Every reported run was trained on a single NVIDIA RTX A6000 GPU on a cluster managed by Slurm, and the five folds of an experiment are submitted together as a job array."
  - Now: "Every reported run was trained on a single NVIDIA RTX A6000 GPU on a cluster managed by Slurm, and the five folds of an experiment were submitted together as a job array."
- **4c.26** [medium] §4.6 Implementation Details · `04-method.tex:1219` (today `04-method.tex:1269`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'Even so' refers to the seeding and the deterministic cuDNN algorithms, but the data-loader sentences sit in between, so it attaches to the wrong statement. 'This is required, because' is stilted, and the em-dash aside is a recurring tell.
  - Was: "All random number generators --- those of Python, NumPy, PyTorch and CUDA --- are seeded, and deterministic cuDNN algorithms are enforced. The data loader runs in the main process. This is required, because the curriculum changes the sampling restriction of ..."
  - Now: "The data loader runs in the main process, because the curriculum changes the sampling restriction of the dataset at every pass and a change made in the main process would not reach separate worker processes. All random number generators (Python, NumPy, PyTorch and CUDA) are seeded, and deterministic cuDNN algorithms ..."

## Chapter 5, protocol and main results

Source: `reviews/editorial-2026-10-01/05a-experiments-protocol-arm-table.md`.

- **5a.1** [low] §5.1 Evaluation Protocol (chapter opening) · `05-experiments.tex:18` · **Done**: 2026-10-18 (own wording)
  - Issue: The chapter introduction sits under the \section{Evaluation Protocol} heading, so the chapter has no opening of its own, and one paragraph mixes chapter scope ('This chapter') with section scope ('This section'). 'Many operators' is vague.
  - Was: "This chapter answers the second part of the research question: what kind of operator the framework of Chapter~\ref{ch:method} needs. Many operators are run through the same slot under identical conditions. This section defines how they are scored and how two ..."
  - Review suggested: "Move the first two sentences above \section{Evaluation Protocol} so that they open the chapter: "This chapter answers the second part of the research question: what kind of operator the framework of Chapter~\ref{ch:method} needs. The operators ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.2** [low] §5.1.1 Why Not Per-Pixel Error · `05-experiments.tex:27` (today `05-experiments.tex:43`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The emphatic 'at all' (on the author's list of fillers) appears twice within two sentences.
  - Was: "Persistence, which predicts no change at all, is therefore a strong per-pixel baseline. A per-pixel mean squared error or root mean squared error (RMSE) is dominated by the static pixels, and a model can reach a low per-pixel error while predicting no ..."
  - Now: "Persistence, the prediction that nothing changes, is therefore a strong per-pixel baseline. A per-pixel mean squared error or root mean squared error (RMSE) is dominated by the static pixels, so a model can reach a low per-pixel error without predicting any progression."
- **5a.3** [medium] §5.1.1 Why Not Per-Pixel Error · `05-experiments.tex:33` (today `05-experiments.tex:49`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The Dice score is used here before it is explained (the plain definition only comes at l. 64-65), against the author's rule that every metric is explained on first use. The closing 'therefore ... almost blind' sentence only restates the previous one, with a metaphor.
  - Was: "The same holds for a Dice score over the whole lesion. The static interior of the lesion dominates it, so persistence already reaches a full-mask Dice of about 0.87. Full-mask Dice is therefore almost blind to progression."
  - Now: "The same holds for a Dice score over the whole lesion. The Dice score measures the overlap of two regions: it is 1 when they coincide and 0 when they share no pixel. Over the whole lesion it is dominated by the static interior, so persistence already reaches a full-mask Dice of about 0.87, and the score barely ..."
- **5a.4** [medium] §5.1.1 Why Not Per-Pixel Error · `05-experiments.tex:37` (today `05-experiments.tex:55`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The second sentence stands alone, and its causal link to the first and third is left for the reader to supply. 'Decalibrate their raw mask regression' is not explained in plain words. 'Late rollout mask RMSE' can be read as RMSE at late rollout steps; if the late-epoch mean is meant (defined only in §5.1.3), 'late-epoch' would remove the ambiguity.
  - Was: "Raw errors are also not compared across architectures. The clinical metrics are computed on the thresholded mask. The dense operators, such as the U-Net and the Fourier Neural Operator, decalibrate their raw mask regression under autoregressive rollout much ..."
  - Now: "Raw errors are also not compared across architectures, because the clinical metrics are computed on the thresholded mask. Under autoregressive rollout, the dense operators, such as the U-Net and the Fourier Neural Operator, decalibrate their raw mask regression much more than the graph network does: the late rollout ..."
- **5a.5** [low] §5.1.1 Why Not Per-Pixel Error · `05-experiments.tex:44` (today `05-experiments.tex:62`) · **Done**: 2026-10-18 (own wording)
  - Issue: 'A separate, known stretch' leaves the reader asking: separate from what, and known from where? §4.5.1 describes the effect as a stretch of the raw mask regression about the threshold.
  - Was: "The soft-Dice loss adds a separate, known stretch to the raw mask values (\S\ref{sec:method:training:loss})."
  - Now: "In addition, the soft-Dice term of the loss stretches the raw mask values away from the threshold (\S\ref{sec:method:training:loss})."
- **5a.6** [medium] §5.1.2 Metrics · `05-experiments.tex:51` (today `05-experiments.tex:76`) · **Done**: as suggested
  - Issue: Dangling participle: grammatically 'mapped' attaches to the masks, but it is the threshold that is mapped into normalised space (§4.5.1: 'the physical threshold of 0.5 mapped into normalised space').
  - Was: "All predicted and ground-truth masks are binarised at the physical threshold of 0.5, mapped into normalised space in the same way as in the loss."
  - Now: "All predicted and ground-truth masks are binarised at the physical threshold of 0.5, which is mapped into normalised space in the same way as in the loss."
- **5a.7** [low] §5.1.2 Metrics · `05-experiments.tex:53` (today `05-experiments.tex:77`) · **Done**: 2026-10-18 (as suggested)
  - Issue: The appositive 'the first visit of the rollout' sits inside a comma-separated list of definitions, so it reads like a further list item.
  - Was: "Let $b$ be the thresholded mask at the baseline visit, the first visit of the rollout, $p$ the thresholded prediction at the anchor and $y$ the thresholded ground truth at the anchor."
  - Now: "Let $b$ be the thresholded mask at the baseline visit (the first visit of the rollout), $p$ the thresholded prediction at the anchor and $y$ the thresholded ground truth at the anchor."
- **5a.8** [low] §5.1.2 Metrics · `05-experiments.tex:65` (today `05-experiments.tex:88`) · **Done**: 2026-10-18 (own wording)
  - Issue: The metric is personified ('it asks') and the sentence contains the filler 'actually'.
  - Was: "Applied to the change regions, it asks whether the model predicts change where change actually happened, and it ignores the large part of the lesion that stays the same."
  - Now: "Applied to the change regions, the Dice score measures how well the predicted change overlaps the change that occurred; the large part of the lesion that stays the same does not enter it."
- **5a.9** [low] §5.1.2 Metrics · `05-experiments.tex:69` (today `05-experiments.tex:92`) · **Done**: 2026-10-18 (as suggested)
  - Issue: 'Lift' is marketing/ML jargon and is not explained.
  - Was: "First, persistence predicts no change, so its score is 0 by construction, and every positive value is lift over "no progression"."
  - Now: "First, persistence predicts no change, so its score is 0 by construction, and every positive value is an improvement over predicting no progression."
- **5a.10** [medium] §5.1.2 Metrics · `05-experiments.tex:74` (today `05-experiments.tex:99`) · **Done**: 2026-10-18 (own wording)
  - Issue: The paragraph announces 'Three consequences follow', but the third item is not a consequence of the definition. It is a distinction from another metric, which brings a second metric into a numbered list.
  - Was: "Third, it is not the growth-region Dice of \citet{Mai2024}, which this chapter also uses."
  - Now: "The change-region Dice differs from the growth-region Dice of~\citet{Mai2024}, which this chapter also uses."
- **5a.11** [low] §5.1.2 Metrics · `05-experiments.tex:78` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: A colon reveal follows the informal 'are easy to confuse', and model selection is added as an afterthought sentence.
  - Was: "Both have a persistence floor of 0 and are easy to confuse: Table~\ref{tab:experiments:arms} and all fold-paired values use the change-region Dice, while the per-eye instrument uses the growth-region Dice (\S\ref{sec:experiments:protocol:stats}). The ..."
  - Now: "Both score 0 for persistence and are easy to confuse: Table~\ref{tab:experiments:arms} and all differences between arms use the change-region Dice, while the eye counts of \S\ref{sec:experiments:protocol:stats} use the growth-region Dice."
- **5a.12** [low] §5.1.2 Metrics · `05-experiments.tex:108` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: This repeats the statement made at the end of the preceding paragraph (l. 80-81).
  - Was: "It is used by the per-eye statistical instrument (\S\ref{sec:experiments:protocol:stats})."
  - Now: "It is used for the eye counts of \S\ref{sec:experiments:protocol:stats}."
- **5a.13** [low] §5.1.2 Metrics · `05-experiments.tex:111` (today `05-experiments.tex:137`) · **Done**: 2026-10-18 (as suggested)
  - Issue: Two unrelated points are joined by 'and', and 'the forecast reaches further' personifies the forecast.
  - Was: "These horizon bins show how the prediction degrades as the forecast reaches further than the one-year anchor, and they are the bins in which \citet{Mai2024} report the same metric."
  - Now: "These horizon bins show how the prediction degrades beyond the one-year anchor. \citet{Mai2024} report the same metric in the same bins."
- **5a.14** [medium] §5.1.2 Metrics · `05-experiments.tex:116` (today `05-experiments.tex:144`) · **Done**: 2026-10-18 (own wording)
  - Issue: The paragraph refers to 'the split' before the reader knows that a split exists or what it is for. A single sentence then carries a colon, an embedded 'or, for padded visits,' and a 'because there' clause.
  - Was: "For the split reported in~\S\ref{sec:experiments:main-results}, an eye counts as border-touching when its true lesion at the anchor touches the edge of the imaged field: the outermost ring of the crop or, for padded visits, the edge of the zero padding, ..."
  - Now: "An eye counts as border-touching when its true lesion at the anchor touches the edge of the imaged field."
- **5a.15** [low] §5.1.3 Rollout and Reporting · `05-experiments.tex:138` (today `05-experiments.tex:168`) · **Done**: 2026-10-18 (own wording)
  - Issue: The second sentence is a pseudo-cleft ending on a preposition; the direct form is shorter.
  - Was: "It isolates the accuracy of a single step from the drift of a rollout. The rollout evaluation is the procedure every reported number comes from."
  - Now: "It isolates the accuracy of a single step from the drift of a rollout."
- **5a.16** [low] §5.1.3 Rollout and Reporting · `05-experiments.tex:146` (today `05-experiments.tex:176`) · **Done**: 2026-10-18 (as suggested)
  - Issue: A semicolon plus 'this is accepted, as' plus 'rather than' packs the observation and its justification into one hard-to-parse sentence.
  - Was: "For a few eyes this step lies beyond one year, where the true change region is larger; this is accepted, as \citet{Mai2024} also score every follow-up visit by its time since baseline rather than at a fixed horizon."
  - Now: "For a few eyes this step lies beyond one year, where the true change region is larger. This is accepted because \citet{Mai2024} also score every follow-up visit by its time since baseline and not at a fixed horizon."
- **5a.17** [low] §5.1.3 Rollout and Reporting · `05-experiments.tex:154` · **Done**: 2026-10-17 (own wording)
  - Issue: A checkpoint is equated with an epoch.
  - Was: "The checkpoint kept as the best one is the epoch with the highest change-region Dice at the anchor."
  - Review suggested: "The checkpoint that is kept is the one from the epoch with the highest change-region Dice at the anchor." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.18** [medium] §5.1.3 Rollout and Reporting · `05-experiments.tex:156` · **Done**: 2026-10-17 (own wording)
  - Issue: One long colon-and-'so' sentence ends on a colloquial phrase ('the luckiest one').
  - Was: "First, the metric is noisy: with 12 to 20 validation eyes per fold, it still fluctuates from epoch to epoch once training has levelled off, with a standard deviation of about 0.01 to 0.05 within one run (Figure~\ref{fig:experiments:curves}a), so the highest ..."
  - Review suggested: "First, the metric is noisy. With 12 to 20 validation eyes per fold, it still fluctuates from epoch to epoch once training has levelled off, with a standard deviation of about 0.01 to 0.05 within one run (Figure~\ref{fig:experiments:curves}a). As a result, the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.19** [HIGH] §5.1.3 Rollout and Reporting · `05-experiments.tex:163` · **Done**: 2026-10-02 (high-severity pass)
  - Issue: The words 'Second, the highest epoch is chosen on the same validation' stand on line 163 after the % of a LaTeX comment and are not rendered. The PDF reads '...the luckiest one. eyes on which it would be reported.', so the second of the two announced reasons is lost. The closing 'and the more so the noisier the metric' is also overly compressed.
  - Was: "Second, the highest epoch is chosen on the same validation eyes on which it would be reported. There is no separate test split (\S\ref{sec:data:splits}), so a best-epoch value is biased upwards, and the more so the noisier the metric."
  - Review suggested: "Put a line break after the % comment (or move the comment below the paragraph) so that the text is rendered: "Second, the highest epoch is chosen on the same validation eyes on which it would be reported. There is no separate test split ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.20** [low] §5.1.3 Rollout and Reporting · `05-experiments.tex:168` · **Done**: 2026-10-17 (own wording)
  - Issue: In the first sentence an 'so ..., and ...' chain joins two separate justifications. The second sentence interrupts itself with 'from epoch 5 on' and then adds a semicolon tail.
  - Was: "The window is fixed in advance and the same for every arm, so no choice is made on the validation data, and averaging twenty epochs damps the epoch-to-epoch noise. The window starts at epoch 10 because by then the learning rate has been reduced once, from ..."
  - Review suggested: "The window is fixed in advance and is the same for every arm, so no choice is made on the validation data. Averaging twenty epochs also damps the epoch-to-epoch noise. The window starts at epoch 10 because by then the learning rate has been reduced once (from ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.21** [low] Figure 5.1 caption · `05-experiments.tex:189` · **Done**: 2026-10-17 (own wording)
  - Issue: 'Ended by the fold markers of Figure 5.3' is cryptic: the reader has to infer that each segment ends in the symbol that identifies its fold.
  - Was: "the dark segments are the late-epoch means of the five folds, ended by the fold markers of Figure~\ref{fig:experiments:arms-folds}."
  - Review suggested: "the dark segments are the late-epoch means of the five folds, each ending in the marker that identifies the fold in Figure~\ref{fig:experiments:arms-folds}." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.22** [low] §5.1.3 Rollout and Reporting · `05-experiments.tex:206` · **Done**: 2026-10-17 (sentence kept; moved or its context changed)
  - Issue: This one-sentence paragraph after Figure 5.1 is cut off from the reporting discussion and repeats the no-test-split point already made at l. 164-165.
  - Was: "All experiments use the patient-level five-fold cross-validation of~\S\ref{sec:data:splits}, which has no test split; every result is a validation result."
  - Review suggested: "Move it to the start of \S\ref{sec:experiments:protocol:rollout} (or to the chapter opening): "All experiments use the patient-level five-fold cross-validation of~\S\ref{sec:data:splits}. It has no test split, so every result is a validation result." The ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.23** [low] §5.1.4 Two Statistical Instruments and the Noise Floor · `05-experiments.tex:214` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: The long subject with an embedded appositive ('two with the same seed and five with different seeds') delays the verb and the result.
  - Was: "Seven pairs of runs with the same configuration on the same fold, two with the same seed and five with different seeds, give a per-run standard deviation of about 0.0127 for the late-epoch mean of the change-region Dice."
  - Review suggested: "The run-to-run spread was measured on seven pairs of runs with the same configuration on the same fold, two pairs with the same seed and five with different seeds. They give a per-run standard deviation of about 0.0127 for the late-epoch mean of the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.24** [medium] §5.1.4 Two Statistical Instruments and the Noise Floor · `05-experiments.tex:217` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: 'Follow from it' asserts a derivation the reader cannot see, so the jump from 0.0127 to 0.036 and 0.016 looks arbitrary.
  - Was: "Two thresholds follow from it. A difference measured on a single fold must exceed 0.036 to count as an effect, and a difference of five-fold paired means must exceed 0.016."
  - Review suggested: "Two thresholds follow from it, each about twice the standard deviation of the difference it applies to: a difference measured on a single fold must exceed 0.036 to count as an effect, and a difference of five-fold paired means must exceed 0.016." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.25** [medium] §5.1.4 Two Statistical Instruments and the Noise Floor · `05-experiments.tex:227` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: An aphoristic paragraph closer (the mirror pair 'nulls and effects' plus a colon reveal) whose meaning is unclear: 'widen a null' is not a defined notion, and a reader cannot tell what follows for the U-Net comparisons.
  - Was: "Noise affects nulls and effects differently: it can only widen a null."
  - Review suggested: "Delete the sentence. If a statement is wanted, give the consequence plainly in the author's own words (for example, that a wider floor makes a null result less informative), after confirming that this is the intended meaning." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.26** [medium] §5.1.4 Two Statistical Instruments and the Noise Floor · `05-experiments.tex:233` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: One sentence carries the notation, a colon, a 'with' phrase and a 'where' clause, and it never says which symbol is which. The second instrument's 'Here $m$ is ...' gives a clearer pattern.
  - Was: "The first is the fold-paired mean, written $\Delta = x \pm y$~SE ($k$/5): the mean over the five folds of the per-fold difference, with its between-fold standard error, where $k$ is the number of folds on which the difference has the same sign as the mean."
  - Review suggested: "The first is the fold-paired mean, written $\Delta = x \pm y$~SE ($k$/5). Here $x$ is the mean over the five folds of the per-fold difference, $y$ its between-fold standard error and $k$ the number of folds on which the difference has the same sign as the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.27** [medium] §5.1.4 Two Statistical Instruments and the Noise Floor · `05-experiments.tex:247` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: The paragraph ends on an 'X, not Y' antithesis closer that restates the preceding sentence.
  - Was: "This instrument uses the growth-region Dice rather than the headline metric, because the change-region Dice was logged per run as a cohort mean only, without per-eye values across epochs. This is a limitation of the logging, not a choice of metric."
  - Review suggested: "This instrument uses the growth-region Dice instead of the headline metric only because of a limitation of the logging: the change-region Dice was recorded per run as a cohort mean, without per-eye values across epochs." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.28** [low] §5.1.4 Two Statistical Instruments and the Noise Floor · `05-experiments.tex:253` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: An em-dash aside introduces a coined term; a parenthesis is the quieter academic form.
  - Was: "A result is established --- it \emph{graduates} --- only when both agree."
  - Review suggested: "A result counts as established (it \emph{graduates}) only when both agree." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.29** [medium] §5.2 The Arm Table · `05-experiments.tex:263` · **Done**: 2026-10-19 (own wording)
  - Issue: A semicolon-joined antithesis ('peer arm; none is a baseline to be beaten'). 'To be beaten' adds a competitive tone the thesis otherwise avoids, and 'fix the scale' is a mild metaphor.
  - Was: "Every architecture in the survey is a peer arm; none is a baseline to be beaten. Only two entries fix the scale: persistence, which scores 0 by construction, and the per-pixel floor."
  - Review suggested: "All architectures in the survey are compared as peers, and none serves as a baseline. Only two entries set the scale: persistence, which scores 0 by construction, and the per-pixel floor." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.30** [low] §5.2 The Arm Table · `05-experiments.tex:265` · **Done**: 2026-10-19 (own wording)
  - Issue: Figure 5.2 (rollouts) is placed before Figure 5.3 but is first referenced at the end of §5.2 (l. 449), after Figure 5.3 (l. 419). The text therefore refers to the figures out of order.
  - Was: "Table~\ref{tab:experiments:arms} lists every arm on the headline metric."
  - Review suggested: "Table~\ref{tab:experiments:arms} lists every arm on the headline metric, and Figure~\ref{fig:experiments:rollout} shows the rollouts of five of them for one validation eye. At l. 449, then begin: "Figure~\ref{fig:experiments:rollout} illustrates what the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.31** [low] Figure 5.2 caption · `05-experiments.tex:354` · **Done**: 2026-10-19 (own wording)
  - Issue: The light grey shows the part of the prediction that coincides with the baseline lesion, not 'the predicted lesion'. 'Code' as a verb is ambiguous.
  - Was: "Model panels show in light grey the predicted lesion that coincides with the baseline lesion and code the change against the baseline: predicted and true in blue, predicted only in orange, true only (missed) in purple; in the baseline column they show the ..."
  - Review suggested: "Model panels show in light grey the part of the predicted lesion that coincides with the baseline lesion and colour the change against the baseline: predicted and true in blue, predicted only in orange, true only (missed) in purple; in the baseline column ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.32** [medium] §5.2 The Arm Table · `05-experiments.tex:368` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: The verdict is appended after a colon as a fragment ('..., a tie'). The seed-7 result for the same pair comes only at the end of the paragraph (l. 380-382), after the U-Net comparisons, and is again closed with a colon fragment ('...: a small but consistent lead, at the noise level'). The reader has to piece the comparison together.
  - Was: "The T-FEN against the dilated-stencil graph network gives $\Delta = +0.0170 \pm 0.0085$~SE (4/5) and per eye $+0.0136 \pm 0.0062$ (46/75, $t = 2.2$): at the floor on one instrument and under it on the other, a tie."
  - Review suggested: ""The T-FEN against the dilated-stencil graph network gives $\Delta = +0.0170 \pm 0.0085$~SE (4/5) and per eye $+0.0136 \pm 0.0062$ (46/75, $t = 2.2$). This lies at the floor on one instrument and under it on the other and is read as a tie. At seed 7 the T-FEN ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.33** [low] §5.2 The Arm Table · `05-experiments.tex:375` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: One sentence carries four statistics, and each seed label comes only at the end of its half. 'At both' is missing its noun.
  - Was: "The T-FEN against the U-Net gives $\Delta = +0.0383 \pm 0.0134$~SE (5/5) and per eye $+0.0383 \pm 0.0075$ (51/75, $t = 5.1$) at seed 42, and $+0.0246 \pm 0.0073$~SE (5/5) and per eye $+0.0255 \pm 0.0074$ (52/75, $t = 3.4$) at seed 7. The lead is smaller at ..."
  - Review suggested: "The T-FEN against the U-Net gives $\Delta = +0.0383 \pm 0.0134$~SE (5/5) and per eye $+0.0383 \pm 0.0075$ (51/75, $t = 5.1$) at seed 42. At seed 7 it gives $+0.0246 \pm 0.0073$~SE (5/5) and per eye $+0.0255 \pm 0.0074$ (52/75, $t = 3.4$). The lead is smaller ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.34** [medium] §5.2 The Arm Table · `05-experiments.tex:386` · **Done**: 2026-10-19 (own wording)
  - Issue: 'The reach deficit' is used as a known term, but §4.3.3 prepared it only as 'the reach problem', and §5.3.5 explains it. The sentence then serves as the premise of the section's verdict.
  - Was: "The two highest arms are the two that carry a remedy for the reach deficit taken up in~\S\ref{sec:experiments:ingredients:convergence}: the transport term and the dilated stencil."
  - Review suggested: "The two highest arms are the two that carry a remedy for the reach deficit, the mismatch between how far one update can see and how far the lesion front moves between two visits (\S\ref{sec:experiments:ingredients:convergence}): the transport term and the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.35** [medium] §5.2 The Arm Table · `05-experiments.tex:389` · **Done**: 2026-10-19 (own wording)
  - Issue: This is a pseudo-cleft with a 'not X but Y' aphoristic close. The same verdict is restated at l. 439-442, in the Table 5.1 caption and in the first sentence of §5.3.
  - Was: "What separates the arms is therefore not their class but the ingredients they carry."
  - Review suggested: "The arms are therefore separated by the ingredients they carry and not by their architecture class; \S\ref{sec:experiments:ingredients} measures these ingredients one at a time. (Then cut the restatement at l. 439-442; see that finding.)" (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.36** [medium] §5.2 The Arm Table · `05-experiments.tex:394` (today `05-experiments.tex:464`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Touches the crop border' does not match the definition in §5.1.2 ('edge of the imaged field', which includes the padding edge), so a reader may think these are two different criteria. The paragraph also interrupts the T-FEN discussion.
  - Was: "The fixed crop censors growth across the window edge (\S\ref{sec:data:spatial}). Of the 75 eyes, 21 have a lesion that touches the crop border at the one-year anchor and 54 do not."
  - Now: "Growth across the edge of the imaged field is censored (\S\ref{sec:data:spatial})."
- **5a.37** [medium] §5.2 The Arm Table · `05-experiments.tex:409` · **Done**: 2026-10-19 (own wording)
  - Issue: The paragraph contains the emphatic 'at all' and a personified, legalistic 'This licenses reading ...'. It also comes five paragraphs after the opening that names the per-pixel floor as one of the two entries that set the scale.
  - Was: "The per-pixel floor reads exactly 0.0000 on all five folds, identical to persistence; its collapse counter flags every validation eye as unchanged from baseline. A model without spatial context predicts no change at all. This licenses reading every point of ..."
  - Review suggested: "Move the paragraph directly after the opening paragraph of §5.2 and write: "The per-pixel floor reads exactly 0.0000 on all five folds, identical to persistence, and its collapse counter flags every validation eye as unchanged from baseline. A model without ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.38** [low] §5.2 The Arm Table · `05-experiments.tex:416` · **Done**: 2026-10-19 (own wording)
  - Issue: '..., which is why ...' is a cleft-like causal tail.
  - Was: "The standard deviations in the table are between-fold deviations and are much larger than the replicate floor, which is why differences are always read fold-paired."
  - Review suggested: "Because the standard deviations in the table are between-fold deviations and much larger than the replicate floor, differences are always read fold-paired." (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.39** [medium] §5.2 The Arm Table · `05-experiments.tex:439` · **Done**: 2026-10-19 (own wording)
  - Issue: 'Leaderboard' is informal, and 'What it provides is ...' is a pseudo-cleft. 'Lie within the floor of each other' is awkward. Both sentences restate the caption and l. 389-390.
  - Was: "Adjacent rows mostly lie within the floor of each other, so the table is not a leaderboard. What it provides is the evidence for which components of an operator move the metric, which \S\ref{sec:experiments:ingredients} examines one at a time."
  - Review suggested: "Adjacent rows mostly differ by less than the noise floor, so the order of the rows should not be read as a ranking. (Drop the second sentence if l. 389 carries the pointer to \S\ref{sec:experiments:ingredients}.)" (the passage was cut or rewritten; no single sentence corresponds today)
- **5a.40** [low] §5.2 The Arm Table · `05-experiments.tex:444` · **Done**: 2026-10-19 (own wording)
  - Issue: This repeats 'fold 2 is the highest fold for almost every arm' from l. 421-422, and 'rather than a separate result' is vague.
  - Was: "The best-fold column shows how far a single fold can lie above the mean. For every arm except the two FNO arms without a local path, the best fold is fold 2, so the column mostly reflects the spread between folds rather than a separate result."
  - Review suggested: "The best-fold column shows how far a single fold can lie above the mean. Since the best fold is fold 2 for every arm except the two FNO arms without a local path, the column adds little beyond the spread between folds. (Then drop 'and fold 2 is the highest ..." (the passage was cut or rewritten; no single sentence corresponds today)

## Chapter 5, ablation studies

Source: `reviews/editorial-2026-10-01/05b-experiments-ingredients.md`.

- **5b.1** [medium] §5.3 The Ingredient Study (intro) · `05-experiments.tex:463` · **Done**: 2026-10-19 (own wording)
  - Issue: The opener repeats the closing figure of §5.2, uses the conversational 'what makes an operator work' and ends on a terse 'Each comparison measures one ingredient' without saying which ingredients follow, so the reader has no map of the five subsections. The blanket 'All comparisons are fold-paired over the same five folds' does not hold for the seed-42 matched transport control, which is paired on folds 0 to 3 only (§5.3.4).
  - Was: "The strongest arms of different classes lie within about 0.04 of each other, so comparing whole architectures says little about what makes an operator work. This section therefore compares operators that differ in one property only, with the rest of the ..."
  - Review suggested: "Since the strongest arms of different classes lie within about 0.04 of each other, a comparison of whole architectures shows little about which properties of an operator matter. This section therefore compares operators that differ in one property only, with ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.2** [low] §5.3.1 Spatial Context · `05-experiments.tex:475` (today `05-experiments.tex:546`) · **Done**: 2026-10-19 (own wording)
  - Issue: Three mirror sentences with identical openings and verbs ('With … rounds, the … reads') form a mechanical tricolon.
  - Was: "With zero rounds, the per-pixel floor reads 0.0000 on every fold, identical to persistence. With one round, the one-hop floor reads $0.4515 \pm 0.0243$. With two rounds, the $k$-NN arm reads $0.4623 \pm 0.0361$."
  - Now: "With zero rounds, each pixel sees only itself."
- **5b.3** [low] §5.3.1 Spatial Context · `05-experiments.tex:478` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: The fold-paired value gets a verdict ('under the paired floor') but the per-eye value does not. §5.1.4 gives no per-eye criterion, so the reader cannot tell what t = -2.4 means until the paragraph's last sentence, after the seed-7 values.
  - Was: "One round against two gives $\Delta = -0.0108 \pm 0.0061$~SE (1/5), under the paired floor, and per eye $-0.0122 \pm 0.0051$ (33/75, $t = -2.4$)."
  - Review suggested: "One round against two gives $\Delta = -0.0108 \pm 0.0061$~SE (1/5), under the paired floor, and per eye $-0.0122 \pm 0.0051$ (33/75, $t = -2.4$), in the same direction; the difference is not established." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.4** [low] §5.3.1 Spatial Context · `05-experiments.tex:485` · **Done**: 2026-10-19 (own wording)
  - Issue: 'Buys' is a colloquial economic metaphor. 'The second ring adds little or nothing' repeats the previous paragraph's last sentence (l.483). The free-standing 'Every point …' repeats the §5.2 conclusion without saying so.
  - Was: "A single ring of neighbours therefore buys almost everything the graph network on this graph achieves, and the second ring adds little or nothing. Every point of change-region Dice comes from spatial context."
  - Review suggested: "One ring of neighbours therefore accounts for almost all of the score that the graph network reaches on this graph. As in~\S\ref{sec:experiments:main-results}, every point of change-region Dice comes from spatial context." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.5** [low] §5.3.2 Physical Reach at Lesion Scale · `05-experiments.tex:505` · **Done**: 2026-10-19 (own wording)
  - Issue: 'In the project' is an informal register for a thesis. The second sentence is a summary closer that restates the paragraph's opening (only the edge set changed; 67\,147 parameters on both sides).
  - Was: "This is the largest effect in the project. It was obtained by changing only the edge set, at the same parameter count, and it is the reason the dilated stencil is the canonical configuration."
  - Review suggested: "This is the largest effect measured in this work, obtained by changing only the edge set at the same parameter count, and the reason the dilated stencil is the canonical configuration." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.6** [medium] §5.3.2 Physical Reach at Lesion Scale · `05-experiments.tex:515` (today `05-experiments.tex:578`) · **Done**: 2026-10-19 (own wording)
  - Issue: The passage checks a confound (at ±42 reach and sparsity change together), but it never says so. The reader has to work out why the ±35 geometry is introduced, and the last sentence chains 'therefore … so'.
  - Was: "The $\pm 42$ geometry keeps the 20 neighbours of the default by doubling the column spacing from 7 to 14, so its neighbours are sparser. The geometry reaching $\pm 35$ columns keeps the default spacing of 7 columns instead, with 32 neighbours; it is also ..."
  - Now: "The $\pm 42$ geometry keeps the 20 neighbours of the default by doubling the column spacing from 7 to 14, so reach and spacing change together."
- **5b.7** [low] §5.3.2 Physical Reach at Lesion Scale · `05-experiments.tex:521` (today `05-experiments.tex:584`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Costs the most' is colloquial. In a chapter with a cost column (training time per epoch), it can be misread as computational cost rather than as loss of Dice.
  - Was: "Widening the stencil across rows, to $\pm 2$ rows, costs the most of all geometries."
  - Now: "Widening the stencil across rows, to $\pm 2$ rows, lowers the score most of all geometries, by 0.039."
- **5b.8** [low] §5.3.2 Physical Reach at Lesion Scale · `05-experiments.tex:580` · **Done**: 2026-10-19 (own wording)
  - Issue: 'Buys nothing' is colloquial. The graph-theory term 'degree' is used before the next sentence explains it as the number of neighbours.
  - Was: "A higher degree at the same reach buys nothing."
  - Review suggested: "More neighbours at the same reach do not raise the score." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.9** [low] §5.3.2 Physical Reach at Lesion Scale · `05-experiments.tex:586` · **Done**: 2026-10-19 (own wording)
  - Issue: A pseudo-cleft ('What matters is …') combined with an 'X, not Y' antithesis, used as an aphoristic paragraph closer.
  - Was: "What matters is where the neighbours are placed, not how many there are."
  - Review suggested: "The gain of the dilated stencil is thus attributable to the placement of its neighbours and not to their number." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.10** [medium] §5.3.2 Physical Reach at Lesion Scale · `05-experiments.tex:589` · **Done**: 2026-10-19 (own wording)
  - Issue: The opening 'This' points back two paragraphs (to the reach result), while the paragraph just before it is about k = 20. 'An earlier result' and 'Before the dilated stencil' narrate project history, although the U-Net/k-NN comparison is a current measurement.
  - Was: "This also explains an earlier result. Before the dilated stencil, the parameter-matched U-Net was higher than the $k$-NN graph network:"
  - Review suggested: "The reach result also explains a second difference. The parameter-matched U-Net is higher than the $k$-NN graph network:" (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.11** [low] §5.3.2 Physical Reach at Lesion Scale · `05-experiments.tex:594` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: The seed-42 caveat comes after the seed-7 values, so the reader has to jump back a seed.
  - Was: "At seed 42, fold 3 reads $-0.042$, so the effect is fold-heterogeneous."
  - Review suggested: "Move it directly after the seed-42 values: '… and per eye $+0.0399 \pm 0.0102$ (53/75, $t = 3.93$); at this seed, fold 3 reads $-0.042$, so the effect is fold-heterogeneous. At seed 7, with the same seed on both sides, the difference is $+0.0548 \pm 0.0181$ ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.12** [medium] §5.3.2 Physical Reach at Lesion Scale · `05-experiments.tex:597` · **Done**: 2026-10-19 (own wording)
  - Issue: An em-dash aside combined with an 'and not' antithesis as a summary closer; 'located in … in where' is awkward.
  - Was: "The deficit of the graph network was therefore located in its graph --- in where its neighbours lie physically --- and not in its operator class."
  - Review suggested: "The deficit of the graph network therefore lay in the physical placement of its neighbours and not in its operator class." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.13** [medium] §5.3.3 Global and Local Context Together · `05-experiments.tex:604` (today `05-experiments.tex:655`) · **Done**: 2026-10-19 (own wording)
  - Issue: The subsection goes from the two operators straight into five pairwise comparisons at two seeds without saying which comparison answers which question, so the reader has to sort them out alone.
  - Was: "The Fourier Neural Operator has global spectral support but no local path (\S\ref{sec:method:family:dense}). The local-kernel hybrid adds a $3 \times 3$ local path to the same operator, at a cost of 800 parameters."
  - Now: "The Fourier Neural Operator sees the whole grid in every layer through its Fourier modes but has no local path (\S\ref{sec:method:family:dense})."
- **5b.14** [low] §5.3.3 Global and Local Context Together · `05-experiments.tex:610` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: A personified, colloquial 'carries all of it' with a colon reveal, followed by three clauses chained with 'and … so'.
  - Was: "Fold 4 carries all of it: without fold 4 the fold-paired difference is $-0.001$, and on both instruments it does not survive leaving one fold out, so this difference is not established."
  - Review suggested: "The whole difference comes from fold 4; without it, the fold-paired difference is $-0.001$. On neither instrument does the difference survive leaving one fold out, so it is not established." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.15** [medium] §5.3.3 Global and Local Context Together · `05-experiments.tex:614` (today `05-experiments.tex:666`) · **Done**: 2026-10-19 (own wording)
  - Issue: A subject-clause opener ('That X … is established'), then two parallel number triplets that the reader has to pair up before the colon gives the reading, then a closing tricolon.
  - Was: "That the FNO lies below the U-Net at the one-year anchor is established. Beyond one year the order changes. In the growth-region Dice by horizon, the FNO reads 0.546, 0.583 and 0.594 for one to two, two to three and more than three years, and the U-Net 0.563, ..."
  - Now: "Against the other operators, the plain FNO lies below the U-Net at the one-year anchor: lower by 0.022 on average, higher on only one of the five folds and on 30 of the 75 eyes."
- **5b.16** [medium] §5.3.3 Global and Local Context Together · `05-experiments.tex:631` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: An effect is equated with a comparison ('The effect … is the hybrid against the FNO'), and there are three 'which' clauses in two sentences. 'Graduates on that instrument' contradicts §5.1.4, where a result graduates only when both instruments agree. The last sentence re-justifies the method of §5.1.4.
  - Was: "The effect of the local path itself is the hybrid against the FNO: $\Delta = +0.0153 \pm 0.0110$~SE, which is under the paired floor, but per eye $+0.0190 \pm 0.0070$ (48/75), which graduates on that instrument. The two instruments disagree here, which is why ..."
  - Review suggested: "The local path itself is isolated by the hybrid against the FNO. The fold-paired difference, $\Delta = +0.0153 \pm 0.0110$~SE, is under the paired floor, while the per-eye difference, $+0.0190 \pm 0.0070$ (48/75), counts as an effect on that instrument. This ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.17** [low] §5.3.3 Global and Local Context Together · `05-experiments.tex:640` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: 'No longer' implies a change over time, although only the seed differs. The sentence-initial 'And' is conversational.
  - Was: "The local path no longer helps: the hybrid against the FNO gives $-0.0057 \pm 0.0105$~SE (3/5) and per eye $-0.0054$ (35/75). And the hybrid lies below the U-Net, by $-0.0193 \pm 0.0051$~SE on all five folds and per eye $-0.0227 \pm 0.0091$ (26/75, $t = ..."
  - Review suggested: "At this seed the local path does not help: the hybrid against the FNO gives $-0.0057 \pm 0.0105$~SE (3/5) and per eye $-0.0054$ (35/75). The hybrid also lies below the U-Net, by $-0.0193 \pm 0.0051$~SE on all five folds and per eye $-0.0227 \pm 0.0091$ ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.18** [medium] §5.3.3 Global and Local Context Together · `05-experiments.tex:648` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: Two consecutive cleft or subject-clause constructions ('What holds … is that', 'That X rests on'), with 'alone' used twice, give a recognisably machine-like rhythm.
  - Was: "What holds at both seeds is therefore that global spectral support alone does not reach the U-Net at the one-year anchor. That a minimal local path closes this gap rests on seed 42 alone; at seed 7 it does not, and the claim is not established."
  - Now: "Global context alone therefore does not reach the U-Net at the one-year anchor."
- **5b.19** [medium] §5.3.4 An Explicit Transport Term · `05-experiments.tex:661` · **Done**: 2026-10-19 (own wording)
  - Issue: 'Purely' is an intensifier of the kind the author removes elsewhere. 'Both heads' is ambiguous, because the control has only one head and the reader does not know which two are meant.
  - Was: "The ablation is purely additive: both heads are zero-initialised, so both arms start as the same function."
  - Review suggested: "The T-FEN differs from this control only by the added transport head. Its free-form and transport heads are both zero-initialised, so the two arms start as the same function." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.20** [low] §5.3.4 An Explicit Transport Term · `05-experiments.tex:670` (today `05-experiments.tex:714`) · **Done**: 2026-10-02 (one-word pass)
  - Issue: In this thesis 'operator' denotes the whole $f_\theta$ in the slot; here only the transport operator is meant.
  - Was: "so the effect does not depend on the form of the operator."
  - Now: "That form becomes unstable in long free-running rollouts, but only well after the one-year anchor (\S\ref{sec:experiments:validity:tfen}), so its score at the anchor is valid, and the effect does not depend on the form of the transport operator."
- **5b.21** [low] §5.3.4 An Explicit Transport Term · `05-experiments.tex:677` (today `05-experiments.tex:726`) · **Done**: 2026-10-19 (own wording)
  - Issue: In this section 'gap' also stands for score differences (l.650, l.706); here it means the difference in parameter count, which invites a misreading.
  - Was: "Part of the gain could therefore come from the extra parameters. A second control closes this gap."
  - Now: "It has 34\,785 parameters against 68\,503 for the T-FEN, so part of the gain could come from the extra parameters."
- **5b.22** [medium] §5.3.4 An Explicit Transport Term · `05-experiments.tex:680` (today `05-experiments.tex:729`) · **Done**: 2026-10-19 (own wording)
  - Issue: Four clauses in one sentence. 'In two separate attempts' sits where it appears to modify only the anchor reading, not the failure to train.
  - Was: "At seed 42, this control does not train on fold 4: its training error rises from the first epoch instead of falling, and it reads 0.047 at the anchor, in two separate attempts, while the width-96 control trains normally on the same fold (0.501)."
  - Now: "This matched control does not train on fold 4: its training error rises from the first epoch, and it reads 0.047 at the anchor."
- **5b.23** [low] §5.3.4 An Explicit Transport Term · `05-experiments.tex:689` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: 'Moves … by little' is unidiomatic.
  - Was: "The extra width moves the free-form network by little at either seed ($-0.0084$ on folds 0 to 3 at seed 42, $+0.0135$ at seed 7, both under the floor). The transport effect is therefore not a matter of parameter count."
  - Review suggested: "Widening the free-form network changes its score little at either seed ($-0.0084$ on folds 0 to 3 at seed 42, $+0.0135$ at seed 7, both under the floor). The transport effect is therefore not a matter of parameter count." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.24** [medium] §5.3.4 An Explicit Transport Term · `05-experiments.tex:699` (today `05-experiments.tex:758`) · **Done**: 2026-10-19 (own wording)
  - Issue: A pseudo-cleft opener with an abstract subject clause ('Where … acts can be seen').
  - Was: "Where the transport term acts can be seen in the first year."
  - Now: "The first-year values show where the transport term acts."
- **5b.25** [medium] §5.3.4 An Explicit Transport Term · `05-experiments.tex:699` (today `05-experiments.tex:762`) · **Done**: 2026-10-19 (own wording)
  - Issue: The trailing appositive can be read as describing only the last two operators, although the argument and Figure 5.5b put the free-form FEN in the same group.
  - Was: "In the growth-region Dice between baseline and one year, the free-form FEN reads 0.388, close to the one-hop floor (0.395) and the $k$-NN graph network (0.397), the operators whose reach falls short of the per-visit front advance (\S\ref{sec:method:graph})."
  - Now: "In the growth-region Dice up to one year, the free-form FEN reads 0.388, close to the one-hop floor (0.395) and the $k$-NN graph network (0.397)."
- **5b.26** [low] §5.3.4 An Explicit Transport Term · `05-experiments.tex:706` · **Done**: 2026-10-19 (own wording)
  - Issue: A one-line aphoristic closer. It restates the preceding sentence (the T-FEN reaches the level of the dilated stencil), anticipates §5.3.5 and uses the overloaded 'gap' again.
  - Was: "The two constructions close the same near-term gap."
  - Review suggested: "Cut the sentence; the preceding sentence states the result and §5.3.5 draws the conclusion." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.27** [low] §5.3.4 An Explicit Transport Term · `05-experiments.tex:715` · **Done**: 2026-10-19 (own wording)
  - Issue: Two parallel number triplets that the reader has to pair up, as at l.616-618. The point of the sentence (the two profiles are close) is easier to see when the values are paired per year.
  - Was: "In the growth-region Dice by horizon, the T-FEN reads 0.519, 0.602 and 0.633 in the first three years and the dilated stencil 0.503, 0.600 and 0.634; only beyond three years does the stencil lie higher (0.655 against 0.611; ..."
  - Review suggested: "In the growth-region Dice by horizon, the T-FEN and the dilated stencil read 0.519 and 0.503 in the first year, 0.602 and 0.600 in the second and 0.633 and 0.634 in the third; only beyond three years does the stencil lie higher (0.655 against 0.611; ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.28** [low] Figure 5.5 caption · `05-experiments.tex:739` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: After the semicolon, the list subject 'inputs, the area … and the evaluated visits' starts without an article and at first reads as a continuation of the preceding clause.
  - Was: "The dashed line gives the values reported by \citet{Mai2024} on a larger cohort of the same clinic; inputs, the area over which lesions are measured (a fixed crop here) and the evaluated visits differ, so the line is a reference, not a head-to-head comparison ..."
  - Now: "The dashed line gives the values reported by \citet{Mai2024} on a larger cohort of the same clinic; it is a reference, not a head-to-head comparison (\S\ref{sec:experiments:qualitative:mai})."
- **5b.29** [low] §5.3.5 Two Routes to One Deficit · `05-experiments.tex:760` · **Done**: 2026-10-19 (own wording)
  - Issue: The anthropomorphic 'see' is an informal analogy. The sentence also leaves implicit that the limit applies to one step, which the Figure 5.5b caption states explicitly.
  - Was: "An operator of that kind cannot see as far as the lesion front moves between two visits."
  - Review suggested: "The single step of such an operator reaches less far than the lesion front moves between two visits." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.30** [medium] §5.3.5 Two Routes to One Deficit · `05-experiments.tex:763` (today `05-experiments.tex:832`) · **Done**: 2026-10-19 (own wording)
  - Issue: A mirror enumeration ('The first is X: … The second is Y: …') with paired colon reveals, a symmetric template.
  - Was: "Two unrelated constructions correct this deficit. The first is physical reach: the dilated stencil, whose single hop spans 21 columns. The second is an explicit transport term: the T-FEN, established against a parameter-matched control at both seeds (on the ..."
  - Now: "Two different constructions remove this limit."
- **5b.31** [low] §5.3.5 Two Routes to One Deficit · `05-experiments.tex:767` (today `05-experiments.tex:836`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'End up' is conversational, and 'the two' changes its referent from constructions to arms in mid-sentence. The semicolon adds a third clause.
  - Was: "Each is established against its own control, and the two end up within about 0.017 of each other, at the noise level; they are the two highest arms of Table~\ref{tab:experiments:arms} (\S\ref{sec:experiments:main-results})."
  - Now: "Each is established against its own control, and the two arms lie within about 0.017 of each other as the two highest arms of Table~\ref{tab:experiments:arms} (\S\ref{sec:experiments:main-results})."
- **5b.32** [medium] §5.3.5 Two Routes to One Deficit · `05-experiments.tex:771` · **Done**: 2026-10-19 (own wording)
  - Issue: 'Coincidence' usually implies chance, which can invert the intended meaning (agreement of two independent constructions) in the section's central claim. The passage also stacks an em-dash aside and two 'rather than' in two sentences.
  - Was: "The central architectural result of the survey is this coincidence --- two independent routes to the same deficit --- rather than the score of any single arm. It is suggestive rather than a proof of mechanism."
  - Review suggested: "The central architectural result of the survey is this convergence of two independent routes on the same deficit, rather than the score of any single arm. The convergence is suggestive but does not prove a mechanism." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.33** [medium] §5.3.5 Two Routes to One Deficit · `05-experiments.tex:776` · **Done**: 2026-10-19 (own wording)
  - Issue: A pseudo-cleft with the antithetical answer delayed until after the semicolon. It also repeats the §5.2 sentence 'What separates the arms is therefore not their class but the ingredients they carry' in the same rhetorical form.
  - Was: "The architecture class therefore is not what separates the strongest operators; the ingredients they carry are."
  - Review suggested: "Among the strongest operators, the differences therefore follow the ingredients they carry and not the architecture class." (the passage was cut or rewritten; no single sentence corresponds today)
- **5b.34** [low] §5.3.5 Two Routes to One Deficit · `05-experiments.tex:777` · **Done**: 2026-10-19 (own wording)
  - Issue: 'Seen' is vague. 'What was measured and did not matter' is informal and stronger than the null definition of §5.4. The sentence opens with a section symbol.
  - Was: "A third candidate, global and local context together, was seen at one seed only (\S\ref{sec:experiments:ingredients:global}) and is not counted among them. \S\ref{sec:experiments:ablations} reports what was measured and did not matter."
  - Review suggested: "A third candidate, global and local context together, was observed at seed 42 only (\S\ref{sec:experiments:ingredients:global}) and is not counted among them. The comparisons without a measurable effect are reported in~\S\ref{sec:experiments:ablations}." (the passage was cut or rewritten; no single sentence corresponds today)

## Chapter 5, negative results

Source: `reviews/editorial-2026-10-01/05c-experiments-negative-results.md`.

- **5c.1** [low] §5.4 Negative Results (introduction) · `05-experiments.tex:789` (today `05-experiments.tex:1003`) · **Done**: 2026-10-19 (own wording)
  - Issue: Three consecutive sentences open with 'A ... / It ... / It ...', and the third joins two unrelated points (what a null does not show; the scope of each finding) with ', and'.
  - Was: "It is a null at the available precision. It does not show that the tested alternative is equivalent, or that the mechanism behind it has no effect, and each finding is scoped to the backbone, the folds and the seed on which it was measured."
  - Now: "Such a result is a null at the available precision only."
- **5c.2** [medium] §5.4 Negative Results (introduction) · `05-experiments.tex:792` (today `05-experiments.tex:994`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Such results' tells the reader that everything below is a null, but §5.4.2 also reports two effects well above the floor: plain MSE never learns change, and removing the soft-Dice term lowers the score on all five folds. A reader expecting only nulls will be surprised by them under this heading.
  - Was: "This section reports three groups of such results: the time handling of the update (\S\ref{sec:experiments:ablations:time}), the composition of the training objective (\S\ref{sec:experiments:ablations:loss}) and the capacity of the operators ..."
  - Now: "This section tests the settings that every operator shares, namely the time handling of the update (\S\ref{sec:experiments:ablations:time}) and the training objective (\S\ref{sec:experiments:ablations:loss}), and the size of the operators (\S\ref{sec:experiments:ablations:capacity})."
- **5c.3** [medium] §5.4.1 Time Handling (introduction) · `05-experiments.tex:805` · **Done**: 2026-10-19 (own wording)
  - Issue: This opener is the template that the §5.4.2 opener repeats, and 'two tests ask this' personifies the tests. 'Both on the canonical dilated-stencil network' is incomplete, because the second test is also reported for the FNO, which then appears without introduction.
  - Was: "This design is part of the framework that every operator shares, so it matters whether its details carry any of the accuracy. Two tests ask this, both on the canonical dilated-stencil network."
  - Review suggested: "Because every operator shares this update, two tests check whether its details contribute to the accuracy. Both use the canonical dilated-stencil network; the second is repeated with the FNO." (the passage was cut or rewritten; no single sentence corresponds today)
- **5c.4** [medium] §5.4.1 Time Handling: Is the multiplication by Δt needed? · `05-experiments.tex:813` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: The colon presents a difference as if it were the Dice value. 'Does not change' is also blunter than the section's own definition of a null (a difference under the floor).
  - Was: "The change-region Dice does not change: $-0.0006$ on average ($\pm 0.0061$~SE, higher on 2 of 5 folds) and per eye $-0.0028 \pm 0.0037$ (30/75)."
  - Now: "The change-region Dice does not change: $-0.0006$ on average, higher on two of the five folds and on 30 of the 75 eyes."
- **5c.5** [medium] §5.4.1 Time Handling: Is the multiplication by Δt needed? · `05-experiments.tex:821` (today `05-experiments.tex:1034`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'The scaled update' is imprecise. The scaled update $\Delta t \cdot f_\theta$ produces the distance itself; it is $f_\theta$ that must output the distance divided by $\Delta t$. A careful reader stumbles over the algebra. 'Simply' is conversational filler.
  - Was: "At a pixel that changes between two visits, the scaled update therefore has to produce exactly that distance divided by $\Delta t$, whatever the interval, and the operator simply learns to divide by $\Delta t$ internally."
  - Now: "At a pixel that changes between two visits, the update must add this distance whatever the interval."
- **5c.6** [medium] §5.4.1 Time Handling: Is the multiplication by Δt needed? · `05-experiments.tex:824` · **Done**: 2026-10-19 (own wording)
  - Issue: This is an aphoristic 'X, not Y' closer, and 'knowledge' gives the operator a human quality. It reads like a slogan, not a technical statement.
  - Was: "The multiplication is a change of parameterisation, not additional knowledge."
  - Review suggested: "The multiplication is thus a reparameterisation that adds no information beyond the $\Delta t$ input." (the passage was cut or rewritten; no single sentence corresponds today)
- **5c.7** [low] §5.4.1 Time Handling: Is the multiplication by Δt needed? · `05-experiments.tex:828` (today `05-experiments.tex:1042`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'It' is ambiguous. The sentence directly before ('It is kept because ...') is about why the multiplication is retained, but this 'It' refers back to the internal division two sentences earlier. 'Read off' and 'read as' repeat the same verb, 'at all' adds emphasis, and the semicolon joins two separate points.
  - Was: "It also means that $f_\theta$ is not a growth rate that could be read off; whether the operator can be read as a continuous-time model at all is tested in~\S\ref{sec:experiments:validity:swap}."
  - Now: "As a consequence, $f_\theta$ cannot be read as a growth rate; whether the operator can be read as a continuous-time model is tested in~\S\ref{sec:experiments:validity:swap}."
- **5c.8** [medium] §5.4.1 Time Handling: Does the time-stepping scheme matter? · `05-experiments.tex:840` (today `05-experiments.tex:1051`) · **Done**: 2026-10-19 (own wording)
  - Issue: The cost clause comes right after the FNO result, so the 4.8 factor reads as if it applied to both operators. §5.6 gives it for the dilated-stencil network only (about 2x for the FNO). It is also unclear what it is relative to.
  - Was: "Over the dilated-stencil network, the change-region Dice is 0.012 lower than with the single step, on 4 of 5 folds; over the FNO it is 0.006 higher. Both differences lie within the noise level, and the Runge--Kutta step costs about 4.8 times the training time ..."
  - Now: "Over the dilated-stencil network, the change-region Dice is 0.012 lower than with the single step, on four of the five folds; over the FNO it is 0.006 higher."
- **5c.9** [medium] §5.4.1 Time Handling: What this means · `05-experiments.tex:852` (today `05-experiments.tex:1073`) · **Done**: 2026-10-19 (own wording)
  - Issue: A pseudo-cleft ('What the update needs is'), an emphatic 'at all' and a mirrored semicolon pair make this read as machine-written.
  - Was: "What the update needs is that the length of the interval reaches the operator at all, either as an input to a single step or through an integrator that steps over the interval; how it arrives makes no measurable difference."
  - Now: "In every tested variant the length of the interval reaches the operator, either as an input to a single step or through an integrator, and the way it arrives makes no measurable difference."
- **5c.10** [low] §5.4.1 Time Handling: What this means · `05-experiments.tex:855` (today `05-experiments.tex:1075`) · **Done**: 2026-10-19 (own wording)
  - Issue: This closer is a 'therefore' verdict plus a 'not by ...' antithesis that restates what the previous sentence just said ('makes no measurable difference').
  - Was: "The simple update of the framework is therefore sufficient, and the accuracy is decided by the spatial operator (\S\ref{sec:experiments:ingredients}), not by the way time is stepped."
  - Now: "The simple update of the framework is therefore sufficient."
- **5c.11** [HIGH] §5.4.2 The Objective (introduction) · `05-experiments.tex:868` (today `05-experiments.tex:1091`) · **Done**: 2026-10-02 (high-severity pass)
  - Issue: 'Each with one part changed' does not hold for the first run, which removes both the mask weighting and the soft-Dice term (l. 878-879). That is why the verdict on the weighting later has to be pieced together from two runs. The sentence also mirrors the §5.4.1 opener almost word for word ('part of the framework ..., so it matters whether ...'; tests that 'ask'), a template-like tell.
  - Was: "Like the time handling, this objective is part of the shared framework, so it matters which of its parts carry the result. Three runs on the canonical dilated-stencil network, each with one part changed, ask this."
  - Now: "Because the objective is shared, three runs on the canonical dilated-stencil network test which of its parts carry the result (Table~\ref{tab:experiments:objective})."
- **5c.12** [low] §5.4.2 The Objective: Is the weighting of the mask channel needed? · `05-experiments.tex:877` · **Done**: 2026-10-19 (own wording)
  - Issue: The second sentence runs about 55 words, with a colon reveal and two facts joined by 'and'. 'Detects this' has a vague antecedent.
  - Was: "The collapse counter of~\S\ref{sec:experiments:protocol:metrics} detects this. Trained with a plain, unweighted mean squared error and no soft-Dice term, the network falls into this collapse and never leaves it within the 30 epochs: its change-region Dice is ..."
  - Review suggested: "The collapse counter of~\S\ref{sec:experiments:protocol:metrics} detects this copying. Trained with a plain, unweighted mean squared error and no soft-Dice term, the network falls into this collapse and never leaves it within the 30 epochs. Its change-region ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5c.13** [medium] §5.4.2 The Objective: Is the weighting of the mask channel needed? · `05-experiments.tex:882` · **Done**: 2026-10-19 (own wording)
  - Issue: This aphoristic 'X, not Y' closer with an emphatic 'at all' is a typical machine pattern. It also leaves the paragraph's own question (is the weighting needed?) unanswered, because this run removed two parts; the answer appears only a paragraph later.
  - Was: "The objective, not the operator, decides whether the model learns any change at all."
  - Review suggested: "For the same operator, the objective decides whether the network learns any change. Because this run also lacks the soft-Dice term, the next run separates the two parts." (the passage was cut or rewritten; no single sentence corresponds today)
- **5c.14** [low] §5.4.2 The Objective: What does the soft-Dice term add? · `05-experiments.tex:886` (today `05-experiments.tex:1144`) · **Done**: 2026-10-19 (own wording)
  - Issue: An emphatic auxiliary ('does leave') plus a colon reveal ('but late:') make this a typical flagged construction; the editor lists both as tells but gave no finding.
  - Was: "With the mask weighting kept and only the soft-Dice term removed, the network does leave the collapse, but late: on the five folds, its change-region Dice first rises above 0 at epochs 2, 8, 3, 7 and 12, against epoch 0 with the full objective ..."
  - Now: "On the five folds, its change-region Dice first rises above 0 at epochs 2, 8, 3, 7 and 12, against epoch 0 with the full objective (Figure~\ref{fig:experiments:objective})."
- **5c.15** [medium] §5.4.2 The Objective: What does the soft-Dice term add? · `05-experiments.tex:894` · **Done**: 2026-10-19 (own wording)
  - Issue: The fold is personified ('makes the run less steady'), and 'It leaves the collapse' could refer to the fold or to the run.
  - Was: "The same fold makes the run less steady. It leaves the collapse only at epoch 12, inside the late-epoch window, so averaged over the folds the epoch-to-epoch standard deviation of the late-epoch Dice is 0.043 against 0.015 with the full objective, but only ..."
  - Review suggested: "The run is also less steady, mainly because of fold 4. On that fold the network leaves the collapse only at epoch 12, inside the late-epoch window, so averaged over the five folds the epoch-to-epoch standard deviation of the late-epoch Dice is 0.043 against ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5c.16** [medium] §5.4.2 The Objective: What does the soft-Dice term add? · `05-experiments.tex:898` · **Done**: 2026-10-19 (own wording)
  - Issue: This is a pseudo-cleft ('is what lets') followed by a balanced two-part verdict, with 'escape ... escape' repeated. The conclusion about the weighting depends on the first run, but the sentence does not say so.
  - Was: "The weighting is therefore what lets the model escape the collapse, and the soft-Dice term adds an immediate escape and a higher score."
  - Review suggested: "Read together with the first run, the mask weighting therefore lets the model leave the collapse; the soft-Dice term makes it leave at once and raises the score." (the passage was cut or rewritten; no single sentence corresponds today)
- **5c.17** [HIGH] §5.4.2 The Objective (soft-Dice paragraph) · `05-experiments.tex:903` · **Done**: 2026-10-02 (high-severity pass)
  - Issue: The clause 'Its cost is the stretch of the raw mask regression described' sits at the end of a comment line, so the PDF prints the fragment '... and a higher score. in §4.5.1: the raw mask error ...' (confirmed in the GPTZero scan). Even once restored, 'Its' is ambiguous, because the preceding sentence names both the weighting and the soft-Dice term.
  - Was: "% 0.013/0.147 vs full 0.011/0.019/0.010/0.012/0.022 (fold 4 carries it). Its cost is the stretch of the raw mask regression described in~\S\ref{sec:method:training:loss}: the raw mask error of the free-running rollout is about twice as large with the term as ..."
  - Review suggested: "Break the line after '(fold 4 carries it).' and put the sentence on its own uncommented line (ideally as the start of a new short paragraph), naming the term: The cost of the soft-Dice term is the stretch of the raw mask regression described ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5c.18** [medium] §5.4.2 The Objective: Would a monotonic-growth penalty help? · `05-experiments.tex:917` (today `05-experiments.tex:1192`) · **Done**: 2026-10-19 (own wording)
  - Issue: A difference is stated as if it were the Dice itself, and the colon-plus-fragment verdict ': no measurable effect, so ...' is a recurring tell.
  - Was: "With the penalty at weight 2.0, the change-region Dice is $-0.0036$ on average ($\pm 0.0037$~SE, higher on 2 of 5 folds) and per eye $-0.0042 \pm 0.0034$ (34/75): no measurable effect, so the simpler objective is kept."
  - Now: "At weight 2.0, the change-region Dice changes by $-0.004$ on average, higher on two of the five folds and on 34 of the 75 eyes."
- **5c.19** [low] §5.4.2 The Objective: Would a monotonic-growth penalty help? · `05-experiments.tex:924` (today `05-experiments.tex:1199`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Locks in' and 'paying the penalty' are idioms, and 'own ... own' repeats within one clause.
  - Was: "Under the pushforward curriculum (\S\ref{sec:method:training:curriculum}), the previous state on an unrolled step is the model's own earlier prediction, so the penalty locks in the model's own false positives: a pixel wrongly marked as atrophic can no longer ..."
  - Now: "Under the pushforward curriculum (\S\ref{sec:method:training:curriculum}), the previous state on an unrolled step is the model's own earlier prediction."
- **5c.20** [medium] §5.4.2 The Objective: Would a monotonic-growth penalty help? · `05-experiments.tex:931` (today `05-experiments.tex:1205`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Teacher-forced' appears nowhere else in the thesis; §4.5.2 speaks of 'a plain one-step pass on observed inputs'. The project rules ask that every term be explained on first use.
  - Was: "The penalty therefore enforces different priors on teacher-forced and on unrolled steps."
  - Now: "The penalty therefore acts differently on steps that start from an observed state and on unrolled steps."
- **5c.21** [low] §5.4.1 Time Handling: Is the multiplication by Δt needed? · `05-experiments.tex:954` (today `05-experiments.tex:1269`) · **Done**: 2026-10-19 (own wording)
  - Issue: Two consecutive 'Each ...' openers, a tense shift (was scaled / changes), and a slightly garbled list ending 'and five folds, seed 42'.
  - Was: "Each architecture class was scaled while everything else was held fixed: the same loss, curriculum, epoch budget and five folds, seed 42. Each run changes one size setting only."
  - Now: "Each class was scaled in one size setting at a time, with the loss, curriculum, epoch budget and the five folds at seed 42 unchanged."
- **5c.22** [low] §5.4.3 Capacity (introduction) · `05-experiments.tex:959` (today `05-experiments.tex:1273`) · **Done**: 2026-10-19 (own wording)
  - Issue: The emphatic 'does change' adds stress the sentence does not need, 'it' could refer to depth or to the reach, and 'is read' is lab jargon for 'is analysed'.
  - Was: "Depth does change the reach of the graph network, so it is read for each class on its own; the U-Net and the FNO have no depth setting."
  - Now: "Depth changes the reach of the graph network, so it is read for each class separately; the U-Net and the FNO have no depth setting."
- **5c.23** [medium] §5.4.3 Capacity (introduction) · `05-experiments.tex:961` (today `05-experiments.tex:1274`) · **Done**: 2026-10-19 (own wording)
  - Issue: The width step is personified ('earns') in a mirrored pair of clauses ('a width step that ... earns ...; a width step without ... earns ...'), a clear template tell.
  - Was: "The design and a decision rule were fixed before the first run: a width step that clears the floor on both instruments earns a further step up, and a width step without a gain earns a step down instead, to between about a sixth and a third of the original ..."
  - Now: "The design and a decision rule were fixed before the first run."
- **5c.24** [low] Table 5.3 caption (capacity study) · `05-experiments.tex:970` (today `05-experiments.tex:1286`) · **Done**: 2026-10-19 (own wording)
  - Issue: The bare '(1)' can be read as a footnote or an equation reference rather than as 'the original size has ratio 1', and 'against' is loose for a ratio.
  - Was: "The ratio is the parameter count against the arm's own original size (1)."
  - Now: "The ratio is the parameter count divided by that of the arm at its original size."
- **5c.25** [low] Figure 5.6 caption (capacity study) · `05-experiments.tex:1040` · **Done**: 2026-10-19 (own wording)
  - Issue: This single sentence of about 50 words chains four appended modifiers ('over ..., with ..., plotted against ...').
  - Was: "Each point is the fold-paired difference of the change-region Dice at the one-year anchor between an operator scaled in size and the same operator at its original size, over five folds at seed 42, with the between-fold standard error, plotted against the ..."
  - Review suggested: "Each point is the fold-paired difference in change-region Dice at the one-year anchor between an operator scaled in size and the same operator at its original size (five folds, seed 42; bars: between-fold standard error). The horizontal axis gives the ratio ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5c.26** [medium] §5.4.3 Capacity (results) · `05-experiments.tex:1057` (today `05-experiments.tex:1339`) · **Done**: 2026-10-19 (own wording)
  - Issue: The paragraph opens with an announcement and never closes the pre-registered rule just stated. The reader is not told that, because no step up was earned, every class was run at a smaller width, which is why the table has those rows.
  - Was: "Table~\ref{tab:experiments:capacity} gives the result. No width step raises any class above the floor on either instrument."
  - Now: "No width step raises any class beyond the noise level (Table~\ref{tab:experiments:capacity})."
- **5c.27** [low] §5.4.3 Capacity (depth paragraph) · `05-experiments.tex:1066` (today `05-experiments.tex:1358`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Lower the graph network' is elliptical: it is the network's change-region Dice that is lowered, not the network.
  - Was: "Four message-passing rounds instead of two, which also double the reach of the dilated stencil, lower the graph network on every fold ($-0.009 \pm 0.002$~SE, 0/5), a small difference under the floor."
  - Now: "Four message-passing rounds instead of two, which also double the reach of the dilated stencil, lower the graph network on every fold, by 0.009 on average, within the noise level."
- **5c.28** [medium] §5.4.3 Capacity (results) · `05-experiments.tex:1070` · **Done**: 2026-10-19 (sentence kept; moved or its context changed)
  - Issue: This is a width result placed at the end of the paragraph that opens 'Depth does not help where it was tested.' The reader of the width paragraph above is never told that one width step made a model diverge.
  - Was: "At width 192, the T-FEN diverges during training on folds 1 and 4 and ties width 96 on the other three."
  - Review suggested: "Move it to the end of the preceding paragraph, after '... level with width 96.', as: Scaled up to width 192, by contrast, the T-FEN diverges during training on folds 1 and 4 and ties width 96 on the other three. The depth paragraph then covers only the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5c.29** [medium] §5.4.3 Capacity (conclusion) · `05-experiments.tex:1074` (today `05-experiments.tex:1364`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Not a lever' is a metaphor. The sentence is a sweeping 'therefore' verdict with two negations, followed by a caveat that reads as an afterthought.
  - Was: "Capacity is therefore not a lever on this task in any of the four classes, and the comparisons at matched size in~\S\ref{sec:experiments:main-results} and~\S\ref{sec:experiments:ingredients} are not an artefact of the size at which they were made. The finding ..."
  - Now: "More parameters therefore improve none of the four classes, and the comparisons at matched size in~\S\ref{sec:experiments:main-results} and~\S\ref{sec:experiments:ingredients} do not depend on the size at which they were made."
- **5c.30** [low] §5.4.3 Capacity (Galerkin caveat) · `05-experiments.tex:1079` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: 'Is open:' followed by evidence that points one way reads as self-contradictory without a contrastive link. The sentence is long and ends on a 'rather than' contrast.
  - Was: "Whether the divergence at width 192 comes from the defect at the crop edge described in~\S\ref{sec:experiments:validity:tfen} is open: in the runs with the energy-conserving form completed so far, width 192 fails on the same two folds, which points to an ..."
  - Review suggested: "Whether the divergence at width 192 comes from the defect at the crop edge described in~\S\ref{sec:experiments:validity:tfen} is not settled. In the runs with the energy-conserving form completed so far, however, width 192 fails on the same two folds, which ..." (the passage was cut or rewritten; no single sentence corresponds today)

## Chapter 5, validity, prior work, cost

Source: `reviews/editorial-2026-10-01/05d-experiments-validity-mai-cost.md`.

- **5d.1** [low] §5.5 Validity Diagnostics (introduction) · `05-experiments.tex:1165` (today `05-experiments.tex:1451`) · **Done**: 2026-10-19 (own wording)
  - Issue: The section opens with a category slip (a diagnostic is not a number) and a personified 'They decide'. It then gives a symmetric 'The first ...; the second ...' pair and the informal 'fixes it'. The first two sentences were judged human, the third AI.
  - Was: "The two diagnostics of this section are not accuracy numbers. They decide which statements about the operators are licensed. The first tests whether a trained operator can be read as a continuous-time system; the second shows why the first version of the ..."
  - Now: "This section examines two properties of the trained operators that the accuracy numbers do not show: whether an operator can be read as a continuous-time model, and whether the T-FEN stays stable when it predicts far beyond the training horizon."
- **5d.2** [low] §5.5.1 The Solver-Swap Test, 'What is tested' · `05-experiments.tex:1175` (today `05-experiments.tex:1469`) · **Done**: 2026-10-19 (as suggested)
  - Issue: A long compound sentence with three references is followed by a personified 'This invites reading' and a colon appositive that repeats 'state' ('states how the state changes'). 'Go further' is conversational.
  - Was: "The update of the framework, $u_t + \Delta t \cdot f_\theta$, has the form of one explicit Euler step (\S\ref{sec:method:dt-residual}), and the Runge--Kutta wrapper and the Finite Element Network go further and integrate $f_\theta$ over several sub-steps ..."
  - Now: "The update of the framework, $u_t + \Delta t \cdot f_\theta$, has the form of one explicit Euler step (\S\ref{sec:method:dt-residual}). The Runge--Kutta wrapper and the Finite Element Network integrate $f_\theta$ over several sub-steps instead (\S\ref{sec:method:family:rk}, \S\ref{sec:method:family:fen}). This ..."
- **5d.3** [low] §5.5.1 The Solver-Swap Test, 'What is tested' · `05-experiments.tex:1186` (today `05-experiments.tex:1480`) · **Done**: 2026-10-19 (own wording)
  - Issue: The argument repeats §4.3.7 ('Jump and continuous time', 04-method.tex l. 863-881) without a back-reference, and the last clause ('and therefore for which models statements about ... are admissible') is awkward.
  - Was: "A network trained with one fixed discretisation need not have this property. It can fit the observed data while its output depends on the discretisation it was trained with \citep{Ott2021, Krishnapriyan2023}. The solver-swap test determines which of the ..."
  - Now: "A network trained with one fixed discretisation need not have this property."
- **5d.4** [HIGH] §5.5.1 The Solver-Swap Test, criterion C2 · `05-experiments.tex:1204` (today `05-experiments.tex:1493`) · **Done**: 2026-10-02 (high-severity pass)
  - Issue: 'At least as fine ..., by step or by order' can be read as 'finer in step or in order'. Under that reading, the single Euler step of the RK4-trained network (same step, lower order, -0.0201 in Table 5.4) belongs to the C2 set and exceeds 0.0127, so the network would fail although the text says it passes. Only the 'in both step and order' reading matches the results. The Table 5.4 caption ('for all settings at least as fine as its training setting (C2)') has the same ambiguity.
  - Was: "\textbf{C2, agreement:} all settings at least as fine as the one used in training, by step or by order, agree to within the run-to-run noise, the standard deviation of 0.0127 between repeated runs of one configuration (\S\ref{sec:experiments:protocol:stats})."
  - Now: "Two criteria make this operational: \item \textbf{C1, convergence:} when the step is refined, the change in the prediction becomes smaller; \item \textbf{C2, agreement:} all settings that are at least as fine as the one used in training in both step and order agree to within the run-to-run noise, the standard ..."
- **5d.5** [low] §5.5.1 The Solver-Swap Test, 'Setup' · `05-experiments.tex:1216` (today `05-experiments.tex:1511`) · **Done**: 2026-10-19 (own wording)
  - Issue: The sentence merges the control procedure and its outcome into one subject ('the setting ... reproduces'), which reads oddly and hides that the training setting itself was re-evaluated.
  - Was: "As a control, the setting a model was trained with reproduces exactly the change-region Dice recorded at the end of its training."
  - Now: "As a control, each model was evaluated with the setting it was trained with, which reproduces its recorded change-region Dice exactly."
- **5d.6** [low] §5.5.1 The Solver-Swap Test, 'Results' · `05-experiments.tex:1235` · **Done**: 2026-10-19 (own wording)
  - Issue: 'The reason is structural.' is a teaser sentence (judged human). The colon reveal in the last sentence was flagged.
  - Was: "The reason is structural. The operator receives $\Delta t$ as an input, so a smaller step also changes the input on which the operator is conditioned. There is no single vector field $g(u)$ to converge to: the canonical network is a one-step map conditioned ..."
  - Review suggested: "The failure follows from the conditioning of the operator. It receives $\Delta t$ as an input, so a smaller step also changes the input on which it is conditioned. There is therefore no single vector field $g(u)$ to which the refinements could converge; the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.7** [low] §5.5.1 The Solver-Swap Test, 'Results' · `05-experiments.tex:1242` · **Done**: 2026-10-19 (own wording)
  - Issue: Three findings are packed into one sentence with an appositive ('the crudest one') and a semicolon; 'crudest' is informal.
  - Was: "Its Euler refinements change the Dice by $+0.018$ and then by $+0.004$ (C1), and every setting except the single Euler step, the crudest one, lies within 0.0044 of the others; the three RK4 settings agree to within 0.0005 (C2)."
  - Review suggested: "Its Euler refinements change the Dice by $+0.018$ and then by $+0.004$ (C1). Apart from the single Euler step, the coarsest setting, all settings lie within 0.0044 of one another, and the three RK4 settings agree to within 0.0005 (C2)." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.8** [low] §5.5.1 The Solver-Swap Test, paragraph labels · `05-experiments.tex:1250` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: 'What follows' can be read as 'what comes next in the text', and the run-in label is more conversational than 'Setup' or 'Results'.
  - Was: "\paragraph{What follows.}"
  - Review suggested: "\paragraph{Implications.} [Optionally also rename \paragraph{What is tested.} at l. 1174 to \paragraph{Purpose.}]" (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.9** [low] §5.5.1 The Solver-Swap Test, 'What follows' · `05-experiments.tex:1251` (today `05-experiments.tex:1592`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Every headline result' is made the subject of 'described as a continuous-time model' (a result is not a model), and the singular 'for it' then leaves the results out. The colon reveal is a recurring tell.
  - Was: "The canonical network, and with it every headline result, may not be described as a continuous-time model: no statement about an ordinary differential equation, a learned rate of growth or learned dynamics is made for it."
  - Now: "Steps coarser than training (shaded) lie outside the test: at 91 days the forecast still agrees with the trained one, at 183 and 365 days it drops by 0.07 to 0.20.} The canonical network, and with it every headline result, may therefore not be described as a continuous-time model: no statement about an ordinary ..."
- **5d.10** [medium] §5.5.1 The Solver-Swap Test, 'What follows' · `05-experiments.tex:1256` (today `05-experiments.tex:1605`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Above it' is ambiguous: the preceding sentence names both the RK4-trained network (subject) and the canonical network. 'Owes this to ..., not to ...' is a personified antithesis, and the closing sentence is an aphoristic restatement with a personified 'decide'.
  - Was: "The network trained inside the Runge--Kutta wrapper is not more accurate than the canonical network (\S\ref{sec:experiments:ablations:time}). The T-FEN lies slightly above it, at the noise level (\S\ref{sec:experiments:main-results}), and owes this to its ..."
  - Now: "The Runge--Kutta network is not more accurate than the canonical network (\S\ref{sec:experiments:ablations:time}), and the score of the T-FEN comes from its transport term (\S\ref{sec:experiments:ingredients:transport})."
- **5d.11** [low] Table 5.4 caption (solver-swap test) · `05-experiments.tex:1275` (today `05-experiments.tex:1632`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Difference to' is a Germanism ('difference from'), and 'the setting the model was trained with' is wordy next to the column header 'vs. trained'.
  - Was: "the values are the change-region Dice at the one-year anchor and its difference to the setting the model was trained with."
  - Now: "The table gives the change of the change-region Dice at the one-year anchor at the finest step against the setting the model was trained with, the span over all settings at least as fine as the training setting in both step and order, and the two criteria: convergence at the finest steps (C1) and agreement of those ..."
- **5d.12** [low] Figure 5.7 caption (solver-swap test against the step size) · `05-experiments.tex:1323` · **Done**: 2026-10-02 (one-word pass)
  - Issue: Garden path: 'without retraining with explicit Euler' first reads as 'without retraining-with-Euler'. The Table 5.4 caption sets the same phrase off with commas.
  - Was: "Each trained model is re-evaluated without retraining with explicit Euler (solid, filled circles) or classical RK4 (dotted, open squares) at a changed step."
  - Review suggested: "Each trained model is re-evaluated, without retraining, with explicit Euler (solid, filled circles) or classical RK4 (dotted, open squares) at a changed step." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.13** [low] Figure 5.7 caption (solver-swap test against the step size) · `05-experiments.tex:1327` (today `05-experiments.tex:1683`) · **Done**: 2026-10-19 (own wording)
  - Issue: The bare '(ring)' at the end of a long clause does not say that it names a marker.
  - Was: "the vertical axis gives the change of the change-region Dice at the one-year anchor against the trained setting (ring)."
  - Now: "The vertical axis gives the change of the change-region Dice at the one-year anchor against the trained setting (ring), one line per fold (folds 0 to 2, seed 42); the shaded band marks $\pm 0.0127$, the run-to-run standard deviation."
- **5d.14** [medium] §5.5.2 Numerical Stability of the T-FEN, 'The first version' · `05-experiments.tex:1349` (today `05-experiments.tex:1720`) · **Done**: 2026-10-19 (sentence kept; moved or its context changed)
  - Issue: The second sentence stacks four qualifiers before a colon reveal and ends in a mirrored 'later than ... and later than ...' pair.
  - Was: "Tracing the rollouts step by step showed where the divergence comes from. It starts at the edge of the crop, in a layer channel, driven by the transport term, and only after about 1.6 to 2 years: later than the one-year anchor and later than the 360 days that ..."
  - Now: "Tracing the rollouts step by step showed where the divergence comes from."
- **5d.15** [medium] §5.5.2 Numerical Stability of the T-FEN, 'The first version' · `05-experiments.tex:1352` (today `05-experiments.tex:1733`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Did not help' is conversational. '... was not the cause. The cause was ...' is a staged anadiplosis.
  - Was: "A smaller step did not help, and the velocities at the onset were within the stability limit of RK4, so the step size was not the cause. The cause was the defect of the Galerkin operator at the domain edge described in~\S\ref{sec:method:family:fen}."
  - Now: "A smaller step left the divergence in place, and the velocities at the onset were within the stability limit of RK4."
- **5d.16** [HIGH] §5.5.2 Numerical Stability of the T-FEN, 'The energy-conserving form' · `05-experiments.tex:1375` (today `05-experiments.tex:1754`) · **Done**: 2026-10-02 (high-severity pass)
  - Issue: The sentence directly follows the seed-7 replication, so 'Its accuracy' reads as the accuracy of the seed-7 run, although the numbers are the seed-42 comparison (0.5428 is the seed-42 value of Table 5.1).
  - Was: "Its accuracy is at least as good: $0.5428 \pm 0.0401$ against $0.5337 \pm 0.0453$ for the Galerkin form, higher on all five folds, by $+0.009$, which is under the noise level."
  - Now: "The energy-conserving form is also at least as accurate as the Galerkin form: $0.5428 \pm 0.0401$ against $0.5337 \pm 0.0453$, higher on all five folds, by $+0.009$, which is under the noise level."
- **5d.17** [medium] §5.5.2 Numerical Stability of the T-FEN, 'The energy-conserving form' · `05-experiments.tex:1378` (today `05-experiments.tex:1761`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'The gain sits where the defect was:' is a personified, slightly literary colon reveal. It is followed by a three-part sentence that mixes a contrast and an addition.
  - Was: "The gain sits where the defect was: on lesions that touch the crop border the change-region Dice rises from 0.516 to 0.544, while interior lesions are unchanged (0.535 and 0.536), and the growth-region Dice beyond three years rises from 0.537 to 0.611."
  - Now: "The growth-region Dice beyond three years rises from 0.537 to 0.611."
- **5d.18** [medium] §5.5.2 Numerical Stability of the T-FEN, residual · `05-experiments.tex:1386` (today `05-experiments.tex:1766`) · **Done**: 2026-10-19 (own wording)
  - Issue: The opener is a teaser sentence, and 'a small residual' does not say of what. The second sentence has a dangling participle: the layer channels do not 'read back' anything. A pointer to where the Courant number is defined (§4.3.6) would help.
  - Was: "A small residual remains, and it has a different cause. Reading back the Courant number over every sub-step of the free-running rollout on fold 0, the layer channels stay at or below 1.36, inside the RK4 limit of about 2.4, but the mask channel lies slightly ..."
  - Now: "The energy-conserving form leaves a small residual with a different cause."
- **5d.19** [medium] §5.5.2 Numerical Stability of the T-FEN, residual · `05-experiments.tex:1390` (today `05-experiments.tex:1771`) · **Done**: 2026-10-19 (own wording)
  - Issue: Four trailing qualifiers hang off one clause. 'At most 26 values per eye and at most 36 in normalised units' puts a count and a magnitude in one mirrored phrase, so it is unclear what the 36 refers to.
  - Was: "In 9 of the 20 validation eyes a few mask values on the top or bottom row of the grid eventually leave the plausible range, at most 26 values per eye and at most 36 in normalised units, starting around day 1\,260 and growing by a factor of about 1.04 per ..."
  - Now: "In 9 of the 20 validation eyes a few mask values on the top or bottom row of the grid eventually leave the plausible range: at most 26 mask values per eye, each at most 36 in normalised units."
- **5d.20** [medium] §5.5.2 Numerical Stability of the T-FEN, residual · `05-experiments.tex:1394` (today `05-experiments.tex:1775`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'This is the step-size limit' equates an observed excursion with a limit. The second sentence joins two unrelated statements with 'and' and nests a relative clause, so 'it' has several possible referents.
  - Was: "This is the step-size limit of RK4, now a minor effect compared with the defect of the Galerkin form, which produced growth by a factor of about 1.3 per sub-step from around day 585. It does not affect the stability criterion, which the run passes, and an ..."
  - Now: "It is a minor effect compared with the defect of the Galerkin form, which produced growth by a factor of about 1.3 per sub-step from around day 585."
- **5d.21** [low] Table 5.5 caption (stability of the T-FEN) · `05-experiments.tex:1412` (today `05-experiments.tex:1795`) · **Done**: 2026-10-19 (own wording)
  - Issue: The caption does not say which error is meant (Figure 5.8 and §4.3.6 specify root mean squared error), so the table is not self-contained.
  - Was: "For each fold: the number of late epochs (10 to 29) on which the free-running mask and layer errors stay at or below 5, and the largest late-epoch mask and layer error, in normalised units."
  - Now: "For each fold: the number of late epochs (10 to 29) on which the root mean squared errors of the mask and of the layer channels in the free-running rollout stay at or below 5, and the largest late-epoch value of each, in normalised units."
- **5d.22** [medium] §5.6 Qualitative Analysis and Clinical Comparison (heading) · `05-experiments.tex:1459` · **Done**: 2026-10-19 (own wording)
  - Issue: The section follows a Courant-number detail of §5.5.2 with no transition and opens directly with its only subsection. The qualitative half of the title has no content yet (TODO), so the reader finds only the Mai comparison.
  - Was: "\section{Qualitative Analysis and Clinical Comparison}"
  - Review suggested: "Insert under the section heading, before \subsection: 'The preceding sections compare the operators within the framework. This section compares the results with a published study of GA progression from OCT.' Until the qualitative part is written, keep this ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.23** [HIGH] §5.6.1 Comparison with Mai et al. (2024), definition of r · `05-experiments.tex:1482` (today `05-experiments.tex:1953`) · **Done**: 2026-10-02 (high-severity pass)
  - Issue: Pearson $r$ does not depend on scale: a model that predicts half of every true rate still reaches $r = 1$. 'Scales ... correctly' therefore misdescribes the metric, and 'orders' fits a rank correlation better. This matters a few lines later, where the fastest eyes are predicted at about half their true rate. '$r = 0$ no relation' should read 'no linear relation'.
  - Was: "The Pearson correlation $r$ asks whether the model orders and scales the growth speeds of the eyes correctly: $r = 1$ is a perfect linear relation and $r = 0$ no relation."
  - Now: "The Pearson correlation $r$ measures how closely the predicted rates follow a linear relation with the true rates across eyes: $r = 1$ is a perfect linear relation and $r = 0$ no linear relation."
- **5d.24** [low] §5.6.1 Comparison with Mai et al. (2024), definition of the AUC · `05-experiments.tex:1485` (today `05-experiments.tex:1957`) · **Done**: 2026-10-19 (own wording)
  - Issue: The sentence mirrors the $r$ sentence exactly ('... asks whether ...: a is ..., b is ...'), and the embedded appositive splits 'separates ... from the rest'.
  - Was: "The fast-progressor area under the receiver operating characteristic curve (AUC) asks whether the predicted rate separates the fastest-growing eyes, the top 10, 15 or 20\,\% of true growth rates, from the rest: 0.5 is chance and 1 is perfect separation."
  - Now: "The fast-progressor area under the receiver operating characteristic curve (AUC) measures how well the predicted rate separates the fastest-growing eyes, the top 10, 15 or 20\,\% of true growth rates, from the rest; 0.5 is chance and 1 is perfect separation."
- **5d.25** [medium] Table 5.6 caption (growth-speed measures against Mai et al.) · `05-experiments.tex:1503` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: 'Anchor' is the technical name of the one-year evaluation point throughout the chapter, so 'the values are an anchor' is ambiguous. 'Head-to-head' is a sports idiom, and 'X, not Y' is a recurring closer.
  - Was: "The two studies differ in cohort size, input and the area over which lesions are measured (see text), so the values are an anchor, not a head-to-head comparison."
  - Review suggested: "The two studies differ in cohort size, input and the area over which lesions are measured (see text), so the values serve as a point of reference and not as a direct comparison." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.26** [medium] §5.6.1 Comparison with Mai et al. (2024), interpretation · `05-experiments.tex:1530` (today `05-experiments.tex:2002`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Captures growth-speed information' is vague, 'clearly' is an intensifier, and the colon reveal is a recurring tell. The basis for 'above zero' (the bootstrap interval in Table 5.6) is not named.
  - Was: "The canonical model captures growth-speed information (Figure~\ref{fig:experiments:growth-rate}): its correlation is clearly above zero, whereas the baseline lesion size alone is not correlated with the growth rate in this cohort ($r = -0.10$)."
  - Now: "The baseline lesion size alone is not correlated with the growth rate in this cohort ($r = -0.10$)."
- **5d.27** [low] §5.6.1 Comparison with Mai et al. (2024), interpretation · `05-experiments.tex:1536` (today `05-experiments.tex:2007`) · **Done**: 2026-10-19 (as suggested)
  - Issue: 'About half the true rate in the median' is a clumsy trailing phrase; it is not clear that it is the median ratio of predicted to true rate.
  - Was: "The fastest eyes are under-predicted: of the 15 eyes with the highest true rates, 14 receive a lower predicted rate, about half the true rate in the median."
  - Now: "The fastest eyes are under-predicted: of the 15 eyes with the highest true rates, 14 receive a lower predicted rate, with a median ratio of predicted to true rate of about one half."
- **5d.28** [medium] §5.6.1 Comparison with Mai et al. (2024), other arms · `05-experiments.tex:1557` · **Done**: 2026-10-19 (own wording)
  - Issue: The closer 'belongs to the approach, not to one operator' is a personified 'X, not Y' aphorism, and 'the approach' is not defined. Because of the blank line before the figure (l. 1541), the sentence renders as a one-sentence paragraph, separated from the interpretation paragraph it completes.
  - Was: "The other arms of the survey do not differ from the canonical model on these measures ($r$ between 0.30 and 0.47, fast-progressor AUCs between 0.66 and 0.78; Table~\ref{tab:appendix:growth-speed}), so the gap belongs to the approach, not to one operator."
  - Review suggested: "Join it to the paragraph ending at l. 1538 (move the figure environment below it) and write: The other arms of the survey do not differ from the canonical model on these measures ($r$ between 0.30 and 0.47, fast-progressor AUCs between 0.66 and 0.78; ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.29** [medium] §5.6.1 Comparison with Mai et al. (2024), caveats · `05-experiments.tex:1562` · **Done**: 2026-10-19 (own wording)
  - Issue: This repeats the caption metaphor almost word for word: it again collides with the technical 'one-year anchor' and uses a sports idiom in a short antithetical topic sentence.
  - Was: "The comparison is an anchor, not a head-to-head result."
  - Review suggested: "The values of \citet{Mai2024} serve only as a point of reference, since the two studies differ in several respects." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.30** [low] §5.6.1 Comparison with Mai et al. (2024), caveats · `05-experiments.tex:1565` · **Done**: 2026-10-19 (own wording)
  - Issue: Two consecutive sentences use the same '..., whereas this thesis/here ...' template, a mirrored pair.
  - Was: "\citet{Mai2024} start from the raw OCT volume, whereas this thesis starts from segmented masks and layer depths. Their paper reports no cropping of the areas, whereas the areas here are measured inside the $49 \times 1024$ crop, which censors growth at its ..."
  - Review suggested: "\citet{Mai2024} start from the raw OCT volume; this thesis starts from segmented masks and layer depths. Their paper reports no cropping of the areas, while the areas here are measured inside the $49 \times 1024$ crop, which censors growth at its border ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.31** [medium] §5.6.1 Comparison with Mai et al. (2024), caveats · `05-experiments.tex:1569` · **Done**: 2026-10-19 (own wording)
  - Issue: The sentence ends a list of differences between the studies but does not say whether it marks a difference from or a match with the definition used here (l. 1475-1481), so the reader cannot tell why it is there.
  - Was: "The paper defines the growth rate as the difference between the square roots of the baseline and the respective follow-up area."
  - Review suggested: "Move it into the definition paragraph, directly after the formula, as '\citet{Mai2024} define the growth rate as the difference between the square roots of the baseline and the respective follow-up area.' If it is meant as a difference (each follow-up visit ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.32** [low] §5.6.1 Comparison with Mai et al. (2024), growth-region Dice · `05-experiments.tex:1577` · **Done**: 2026-10-19 (own wording)
  - Issue: 'All three operators' appears without antecedent; the preceding paragraphs speak of 'the canonical model' and 'the other arms', and the three are named only in the column headers of Table 5.7.
  - Was: "All three operators lie above the values of \citet{Mai2024} in every bin, by 0.18 to 0.29."
  - Review suggested: "The dilated-stencil network, the U-Net and the T-FEN all lie above the values of \citet{Mai2024} in every bin, by 0.18 to 0.29." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.33** [low] §5.6.1 Comparison with Mai et al. (2024), growth-region Dice · `05-experiments.tex:1579` (today `05-experiments.tex:2057`) · **Done**: 2026-10-19 (own wording)
  - Issue: '\citet{Mai2024} must first find the lesion' makes the authors, not their model, the agent. The crop caveat is stated here for the third time (Table 5.6 caption, l. 1566-1569).
  - Was: "The models of this thesis receive the segmented baseline lesion as input, so its outline is given exactly, whereas \citet{Mai2024} must first find the lesion in the raw OCT volume. The areas here are measured inside the crop, and the two studies evaluate ..."
  - Now: "The models of this thesis receive the segmented baseline lesion as input, so its outline is given exactly, whereas the model of~\citet{Mai2024} first has to find the lesion in the raw OCT volume."
- **5d.34** [medium] §5.6.1 Comparison with Mai et al. (2024), growth-region Dice · `05-experiments.tex:1583` (today `05-experiments.tex:2059`) · **Done**: 2026-10-19 (own wording)
  - Issue: This is a personified summary closer ('the comparison shows', 'the mask carries', 'the mask helps') joined by a semicolon and ending on the race idiom 'is ahead'.
  - Was: "The comparison mainly shows how much of the spatial forecast the segmented mask already carries; on growth speed, where the mask helps less, the model of \citet{Mai2024} is ahead."
  - Now: "Together with the differences listed above, this means that the comparison mainly shows how much of the spatial forecast the segmented mask already carries."
- **5d.35** [low] Table 5.7 caption (growth-region Dice against Mai et al.) · `05-experiments.tex:1596` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: This is the third use of the sports idiom 'head-to-head' in §5.6.1 (with the Table 5.6 caption and l. 1562).
  - Was: "so the values are not a head-to-head comparison."
  - Review suggested: "so the values do not form a direct comparison." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.36** [low] §5.7 Computational Cost · `05-experiments.tex:1622` (today `05-experiments.tex:2070`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'The mean is not used.' is a choppy standalone sentence whose reason only follows in the next sentence.
  - Was: "The cost of an arm is reported as its minimum epoch time over the five folds. The mean is not used. The epoch times of a run carry a nearly constant additive overhead of 17 to 64~s, which would penalise cheap operators far more than expensive ones."
  - Now: "Cost is reported as the minimum epoch time over the five folds, not as the mean."
- **5d.37** [low] §5.7 Computational Cost · `05-experiments.tex:1625` · **Done**: 2026-10-19 (own wording)
  - Issue: 'The spread' does not say of what (epoch times). The 'The first is ... The second is ...:' enumeration is mechanical.
  - Was: "The spread between folds has two measured causes. The first is this overhead. The second is that the work per epoch differs between folds: an epoch is twenty passes over the fold's training eyes in batches of four, which gives 280, 320, 300, 300 and 320 ..."
  - Review suggested: "The epoch times differ between folds for two measured reasons: this overhead and a different amount of work per epoch. An epoch consists of twenty passes over the fold's training eyes in batches of four, which gives 280, 320, 300, 300 and 320 optimiser steps ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.38** [medium] §5.7 Computational Cost · `05-experiments.tex:1630` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: 'An earlier explanation' refers to project history the reader never saw, which tells the story of the project and does not report a result. The hardware sentence is setup information placed after the analysis.
  - Was: "An earlier explanation of the spread by several runs sharing one GPU was checked and does not hold: no two runs ever shared a GPU. All runs used one NVIDIA RTX A6000 GPU and 30 epochs."
  - Review suggested: "Runs sharing a GPU can be excluded as a further cause, since no two runs ever shared a GPU. [Move 'All runs used one NVIDIA RTX A6000 GPU and 30 epochs.' to the first sentence of the section.]" (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.39** [low] §5.7 Computational Cost · `05-experiments.tex:1636` (today `05-experiments.tex:2082`) · **Done**: 2026-10-02 (one-word pass)
  - Issue: 'On this scale' could refer to the time scale or to the order-of-magnitude precision just stated.
  - Was: "On this scale, the U-Net is the cheapest spatial operator at 21~s per epoch, about $0.23\times$ the 91~s of the canonical dilated-stencil graph network."
  - Now: "Within this precision, the U-Net is the cheapest spatial operator, at 21~s per epoch, about $0.23\times$ the 91~s of the canonical dilated-stencil graph network."
- **5d.40** [medium] §5.7 Computational Cost · `05-experiments.tex:1640` · **Done**: 2026-10-19 (own wording)
  - Issue: 'Single-step' conflicts with §4.3.6/§5.5.1, where the FENs are always integrated with RK4 in 45-day sub-steps; elsewhere (l. 455, 1657) 'single-step' means one Euler step. The intended exclusion appears to be the RK4-wrapped graph network (439 s).
  - Was: "The Finite Element Networks are the most expensive single-step family: 180~s for the free-form network and 367~s for the T-FEN (Table~\ref{tab:experiments:arms})."
  - Review suggested: "Apart from the graph network inside the RK4 wrapper, the Finite Element Networks are the most expensive arms: 180~s for the free-form network and 367~s for the T-FEN (Table~\ref{tab:experiments:arms}). [If 'single-step' was meant differently, name the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.41** [medium] §5.7 Computational Cost · `05-experiments.tex:1645` · **Done**: 2026-10-19 (own wording)
  - Issue: The topic sentence promises three timing-independent ratios. The paragraph then gives four numbers and shows with the FNO that the wrapper ratio changes with the operator because of the fixed overhead, which reads as a contradiction. It does not say which 'details' are meant.
  - Was: "Three ratios do not depend on the fine details of the timing."
  - Review suggested: "Replace with: 'Three cost ratios hardly change whether the minimum or the mean epoch time is used.' Then let the three ratios be the RK4 wrapper over the dilated-stencil network (about $4.8\times$), the T-FEN against that network (about $4\times$) and the ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **5d.42** [low] §5.7 Computational Cost · `05-experiments.tex:1649` (today `05-experiments.tex:2096`) · **Done**: 2026-10-19 (own wording)
  - Issue: In 'it raises it' the two pronouns refer to different things. The sentence also mirrors the preceding 'Over the dilated-stencil network, where ...' sentence clause for clause.
  - Was: "Over the FNO, whose forward pass is cheap, it raises it only from 23 to 45~s, about $2\times$, because the fixed part of the epoch weighs more."
  - Now: "Over the FNO, whose forward pass is cheap, the epoch time rises only from 23 to 45~s, about $2\times$, because the fixed part of the epoch weighs more."
- **5d.43** [medium] §5.7 Computational Cost · `05-experiments.tex:1655` (today `05-experiments.tex:2102`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Bought nothing measurable' is a conversational, slightly dramatic idiom used as a verdict-style topic sentence.
  - Was: "Set against the results of this chapter, most of the extra cost bought nothing measurable."
  - Now: "Set against the results of this chapter, most of the extra cost brings no measurable gain."
- **5d.44** [low] §5.7 Computational Cost · `05-experiments.tex:1660` (today `05-experiments.tex:2107`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'The one ... arm' (for 'the only') and the sports verb 'ties' are informal, and the appositive 'its transport term' makes the term itself the 'effect'.
  - Was: "The T-FEN is the one expensive arm with an established effect, its transport term, but at the anchor it ties the dilated-stencil network, which reaches the same level at about a quarter of the cost."
  - Now: "The T-FEN is the only expensive arm with an established effect, its transport term."
- **5d.45** [low] §5.7 Computational Cost · `05-experiments.tex:1663` · **Done**: 2026-10-19 (sentence kept; moved or its context changed)
  - Issue: This scope statement closes the chapter after the cost-versus-benefit reading, so the chapter ends on a limitation that belongs with the definition of what was measured.
  - Was: "Inference time per rollout step and memory footprint were not measured."
  - Review suggested: "Move it to the first paragraph after the hardware sentence, e.g. 'All runs used one NVIDIA RTX A6000 GPU and 30 epochs; inference time per rollout step and memory footprint were not measured.' The section then ends on the T-FEN sentence." (the passage was cut or rewritten; no single sentence corresponds today)

## Chapters 6 and 7

Source: `reviews/editorial-2026-10-01/06-07-discussion-conclusion.md`.

- **6-7.1** [medium] §6.1 Interpretation of Results (opening) · `06-discussion.tex:16` · **Done**: 2026-10-19 (own wording)
  - Issue: A colon reveal and a semicolon antithesis form a mirror pair of short verdicts. 'Transferred' has no object, so the reader has to infer across what the framework transferred.
  - Was: "The results answer the two parts differently. The framework transferred: one setup served operators from unrelated literatures without change. The operator class did not decide the outcome; a small number of properties of the operator did."
  - Review suggested: "The results answer the two parts differently. The framework transferred, since one setup served operators from unrelated literatures without modification. The architecture class of the operator did not decide the outcome, whereas a small number of its ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.2** [medium] §6.1 'The framework.' · `06-discussion.tex:27` · **Done**: 2026-10-19 (own wording)
  - Issue: 'Learned' has no object, and 'every ... every one' repeats. The cleft 'This is what made ... possible at all' has an unclear 'This' (the setup, or the fact that every operator learned?) and adds an intensifier.
  - Was: "Under these conditions, every operator with any spatial context learned, and every one of them lies far above persistence. This is what made the comparison of Chapter~\ref{ch:experiments} possible at all, and it is the answer to the first part of the question."
  - Review suggested: "Under these conditions, every operator with any spatial context learned to predict change and lies far above persistence. This common setup made the comparison of Chapter~\ref{ch:experiments} possible, and it is the answer to the first part of the question." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.3** [medium] §6.1 'The framework.' (time) · `06-discussion.tex:33` · **Done**: 2026-10-19 (own wording)
  - Issue: 'Turned out' is narrative. The compressed 'less than that it enters' is hard to parse on first reading, and Ch. 7 reuses the same aphorism. 'over a local and over a global operator' reads awkwardly.
  - Was: "How time enters the update turned out to matter less than that it enters. A fourth-order Runge--Kutta step in place of one Euler step changed nothing measurable, over a local and over a global operator (\S\ref{sec:experiments:ablations:time})."
  - Review suggested: "The form in which $\Delta t$ enters the update mattered less than the fact that it enters. Replacing one Euler step by a fourth-order Runge--Kutta step made no measurable difference for either a local or a global operator ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.4** [low] §6.1 'The framework.' (time) · `06-discussion.tex:36` · **Done**: 2026-10-19 (own wording)
  - Issue: The interjection 'on the mask channel' splits the subject from its complement, and 'rather than additional knowledge' is a vague antithesis.
  - Was: "The multiplication of the operator output by $\Delta t$ is, on the mask channel, a change of parameterisation rather than additional knowledge, and removing it does not change the result."
  - Review suggested: "On the mask channel, multiplying the operator output by $\Delta t$ only changes the parameterisation and adds no prior knowledge; removing the multiplication does not change the result." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.5** [medium] §6.1 'The framework.' (objective) · `06-discussion.tex:40` · **Done**: 2026-10-19 (own wording)
  - Issue: No blank line precedes this sentence, so the objective is discussed in the same paragraph as time integration. 'part ... parts' repeats, and three ablations follow, so the reader has to work out which two components are meant.
  - Was: "The objective is part of the framework, and two of its parts are needed (\S\ref{sec:experiments:ablations:loss})."
  - Review suggested: "Start a new paragraph here: "The objective belongs to the framework as well, and two of its components are needed (\S\ref{sec:experiments:ablations:loss}): the weighting of the mask channel and the soft-Dice term."" (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.6** [low] §6.1 'The framework.' (closing sentence) · `06-discussion.tex:47` · **Done**: 2026-10-19 (own wording)
  - Issue: A pseudo-cleft with 'in short' turns the sentence into an aphoristic closer that restates the paragraph.
  - Was: "What the framework needs, in short, is a loss that puts weight on the lesion mask, an interval length that reaches the operator, and everything else held fixed."
  - Review suggested: "In summary, the framework needs a loss that weights the lesion mask, an interval length that reaches the operator, and all other components held fixed. (Alternatively, cut the sentence; the paragraph already says this.)" (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.7** [low] §6.1 heading 'The operator: ingredients, not classes.' · `06-discussion.tex:51` · **Done**: 2026-10-19 (own wording)
  - Issue: The heading is a slogan-like antithesis. It also breaks the parallel with the plain heading 'The framework.' above it, and the paragraph itself speaks of 'properties'.
  - Was: "\paragraph{The operator: ingredients, not classes.}"
  - Review suggested: "\paragraph{The operator.}" (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.8** [medium] §6.1 'The operator' (L52-62) · `06-discussion.tex:54` · **Done**: 2026-10-19 (own wording)
  - Issue: 'Such a result' most naturally refers to the first sentence (three unrelated classes within 0.04), but two sentences intervene, so the referent is unclear. The 'reach deficit' is used before the reader knows what it is.
  - Was: "The finite-element network is highest: it lies above the U-Net at both seeds and only slightly above the graph network. The two highest are the two that carry a remedy for the reach deficit discussed below. If the class decided the outcome, such a result ..."
  - Review suggested: "Move "If the class decided the outcome, such a result would be unlikely." directly after the sentence ending "(\S\ref{sec:experiments:main-results}).", then continue: "The finite-element network is highest: it lies above the U-Net at both seeds and only ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.9** [medium] §6.1 'The operator' (properties list) · `06-discussion.tex:58` · **Done**: 2026-10-19 (own wording)
  - Issue: A pseudo-cleft opens the sentence, and 'spatial context at all' is an ungrammatical list item that uses 'at all' as an intensifier.
  - Was: "What separates operators is instead a set of properties that can be switched on and off one at a time (\S\ref{sec:experiments:ingredients}): spatial context at all, physical reach at the scale of the lesion front, and an explicit transport term."
  - Review suggested: "Instead, the operators are separated by a set of properties that can be switched on and off one at a time (\S\ref{sec:experiments:ingredients}): the presence of any spatial context, physical reach at the scale of the lesion front, and an explicit transport ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.10** [low] §6.1 reach and transport paragraph · `06-discussion.tex:69` · **Done**: 2026-10-02 (one-word pass)
  - Issue: 'End up' is a narrative idiom.
  - Was: "Each is established against its own control, and the two end up indistinguishable from each other."
  - Review suggested: "Each is established against its own control, and the two are indistinguishable from each other." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.11** [low] §6.1 reach and transport paragraph (closing) · `06-discussion.tex:77` · **Done**: 2026-10-19 (own wording)
  - Issue: This is an aphoristic closer built on 'rather than ... but'. 'Coincidence' also suggests chance, which is not what is meant.
  - Was: "The coincidence of two routes is suggestive rather than a proof of mechanism, but it is a more specific statement than any ranking of architectures."
  - Review suggested: "The agreement of the two routes is suggestive but does not prove a mechanism; it is nevertheless more specific than any ranking of architectures." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.12** [low] §6.1 global and local context · `06-discussion.tex:89` · **Done**: 2026-10-19 (own wording)
  - Issue: 'Were not tested' could be read as 'not measured'. What is meant is that no statistical test was applied.
  - Was: "These horizon values are descriptive and were not tested, but they suggest that global support matters more for long forecasts than for the one-year anchor."
  - Review suggested: "These horizon values are descriptive and were not tested statistically, but they suggest that global support matters more for long forecasts than at the one-year anchor." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.13** [low] §6.1 'Capacity.' · `06-discussion.tex:94` (today `06-discussion.tex:131`) · **Decided**: dropped: the supervisor asked to keep this paragraph (SV-1.2 / SV-6.3)
  - Issue: 'Lever' is a metaphor, and 'raised a class above the noise level' confuses the class with the size of its gain.
  - Was: "Capacity was not a lever in any of the four classes tested (\S\ref{sec:experiments:ablations:capacity}): no width step raised a class above the noise level, and the smaller versions lost little."
  - Now: "Capacity was not a lever in any of the four classes tested (\S\ref{sec:experiments:ablations:capacity}): no width step raised a class above the noise level, and the smaller versions lost little."
- **6-7.14** [low] §6.1 'Capacity.' · `06-discussion.tex:96` (today `06-discussion.tex:136`) · **Decided**: dropped: the supervisor asked to keep this paragraph (SV-1.2 / SV-6.3)
  - Issue: The clause after the semicolon has a nominal 'that'-clause as its subject and is hard to parse. 'Weigh more' is a mild metaphor.
  - Was: "With 75 eyes, this is what the low-data argument of Chapter~\ref{ch:introduction} leads one to expect: the assumptions built into an operator weigh more than its size. The capacity study shows that size did not help; that the built-in assumptions are the ..."
  - Now: "With 75 eyes, this is what the low-data argument of \S\ref{sec:introduction:why-pde} leads one to expect: the assumptions built into an operator weigh more than its size."
- **6-7.15** [medium] §6.1 'A missing counterpart to the equation features.' · `06-discussion.tex:103` (today `06-discussion.tex:142`) · **Decided**: dropped: the supervisor asked to keep this paragraph (SV-1.2 / SV-6.3)
  - Issue: An em-dash aside splits subject and verb, and a cleft ('it is what lets') follows. The sentence is long for a definition.
  - Was: "In MP-PDE, a vector of equation features $\theta_{\text{PDE}}$ --- the coefficients and boundary conditions of the equation being solved --- is passed to every layer, and it is what lets one trained solver handle a whole family of equations ..."
  - Now: "In MP-PDE, a vector of equation features $\theta_{\text{PDE}}$ --- the coefficients and boundary conditions of the equation being solved --- is passed to every layer, and it is what lets one trained solver handle a whole family of equations \citep{Brandstetter2022}."
- **6-7.16** [low] §6.1 'A missing counterpart to the equation features.' · `06-discussion.tex:106` (today `06-discussion.tex:148`) · **Decided**: dropped: the supervisor asked to keep this paragraph (SV-1.2 / SV-6.3)
  - Issue: Every other place in the thesis says the equation is unknown (§1.3 L158, §2 L758 'no known governing equation', §4 L339, §6.3 L297). 'Has no governing equation' is a different, ontological claim.
  - Was: "GA has no governing equation, and so no such vector exists."
  - Now: "GA has no governing equation, and so no such vector exists."
- **6-7.17** [low] §6.1 'A missing counterpart to the equation features.' · `06-discussion.tex:109` (today `06-discussion.tex:151`) · **Decided**: dropped: the supervisor asked to keep this paragraph (SV-1.2 / SV-6.3)
  - Issue: 'Cannot say anything' personifies the covariates and is conversational.
  - Was: "The covariates are two numbers per visit, shared by every grid position and nearly constant along a trajectory, so they can shift a prediction as a whole but cannot say anything about a particular eye's lesion."
  - Now: "The covariates are two numbers per visit, shared by every grid position and nearly constant along a trajectory, so they can shift a prediction as a whole but cannot say anything about a particular eye's lesion."
- **6-7.18** [low] §6.1 'A missing counterpart to the equation features.' · `06-discussion.tex:111` (today `06-discussion.tex:153`) · **Decided**: dropped: the supervisor asked to keep this paragraph (SV-1.2 / SV-6.3)
  - Issue: 'That the code provides' points to an implementation the reader has not seen. A long appositive and a trailing 'without a detectable benefit' make the sentence hard to follow.
  - Was: "The learned stand-in that the code provides, a layer encoder that summarises the retinal structure into one vector, was tested in an earlier configuration and in one design only, without a detectable benefit."
  - Now: "The learned stand-in that the code provides, a layer encoder that summarises the retinal structure into one vector, was tested in an earlier configuration and in one design only, without a detectable benefit."
- **6-7.19** [medium] §6.1 'A missing counterpart to the equation features.' · `06-discussion.tex:116` (today `06-discussion.tex:158`) · **Decided**: dropped: the supervisor asked to keep this paragraph (SV-1.2 / SV-6.3)
  - Issue: A pseudo-cleft opens the paragraph, and 'eye-specific ... this eye' is redundant.
  - Was: "What is lost is an eye-specific description of how this eye progresses."
  - Now: "What is lost is an eye-specific description of how this eye progresses."
- **6-7.20** [low] §6.1 'A missing counterpart to the equation features.' · `06-discussion.tex:119` (today `06-discussion.tex:161`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Growth-speed gap' is used as a known term, but §6.2 introduces it only later.
  - Was: "This is a plausible contributor to the growth-speed gap discussed in \S\ref{sec:discussion:clinical}, but it was not tested."
  - Now: "This is a plausible contributor to the weaker prediction of growth speed discussed in~\S\ref{sec:discussion:clinical}, but it was not tested."
- **6-7.21** [medium] §6.1 'A missing counterpart to the equation features.' · `06-discussion.tex:120` (today `06-discussion.tex:163`) · **Decided**: dropped: the supervisor asked to keep this paragraph (SV-1.2 / SV-6.3)
  - Issue: This is future-work content inside the interpretation, and §6.4 'An eye-level descriptor' largely repeats it. The em-dash aside uses 'trajectory memory' before §6.3/§6.4 introduce the term.
  - Was: "Candidates for the slot are descriptors that do vary between eyes: lesion-level quantities such as size, shape or focality, a learned summary of the observed layers, or --- with trajectory memory --- the eye's own past growth."
  - Now: "Candidates for the slot are descriptors that do vary between eyes: lesion-level quantities such as size, shape or focality, a learned summary of the observed layers, or --- with trajectory memory --- the eye's own past growth."
- **6-7.22** [medium] §6.1 'Predictions between visits.' · `06-discussion.tex:130` · **Done**: 2026-10-19 (own wording)
  - Issue: The paragraph announces 'two attempts' (the regulariser and the RK wrapper), but this sentence adds a third model that was not built for this purpose, so the count no longer matches. The parenthetical also makes the subject hard to read.
  - Was: "The network trained inside the Runge--Kutta wrapper, and the T-FEN in its energy-conserving form, pass the solver-swap test and can therefore be read as continuous-time models (\S\ref{sec:experiments:validity:swap})."
  - Review suggested: "The second attempt, training the network inside the Runge--Kutta wrapper, gives a model that passes the solver-swap test and can therefore be read as a continuous-time model; the T-FEN in its energy-conserving form passes the test as well ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.23** [medium] §6.1 'Where modelling effort pays.' · `06-discussion.tex:141` · **Done**: 2026-10-19 (own wording)
  - Issue: The opener only restates the heading, using the idiom 'paid off'. The next sentence splits a long subject with an em-dash aside, and 'where an operator looks' personifies the operator.
  - Was: "Taken together, the positive results and the nulls indicate where effort paid off in this survey. Changing where an operator looks --- its reach along the direction in which the front moves --- or adding a mechanism that transports the state produced the ..."
  - Review suggested: "Across the survey, the largest effects came from changing the reach of an operator along the direction in which the front moves and from adding a mechanism that transports the state." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.24** [medium] §6.1 'Where modelling effort pays.' (closing) · `06-discussion.tex:148` · **Done**: 2026-10-19 (own wording)
  - Issue: The closing 'therefore' follows the sentence on the objective, but the recommendation does not follow from it; it follows from the reach and transport results earlier in the paragraph. The emphatic 'did matter' and 'at all' add to the effect.
  - Was: "The objective, by contrast, did matter: the weighting of the mask channel decided whether anything was learned at all. For a new disease-forecasting task of this kind, the first question to ask of an operator is therefore how far one update reaches compared ..."
  - Review suggested: "The objective, by contrast, affected the result: without the weighting of the mask channel, no change was learned. Given the effects of reach and transport, the first question to ask of an operator in a new disease-forecasting task of this kind is how far one ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.25** [low] §6.2 heading 'Good at where, weaker at how fast.' · `06-discussion.tex:157` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: The heading is conversational and slogan-like, out of register with the other paragraph headings.
  - Was: "\paragraph{Good at where, weaker at how fast.}"
  - Review suggested: "\paragraph{Location versus speed of growth.}" (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.26** [low] §6.2 location versus speed · `06-discussion.tex:162` (today `06-discussion.tex:215`) · **Done**: 2026-10-19 (own wording)
  - Issue: One sentence carries two separate comparisons, and 'fast-progressor AUCs' appears without a reminder of what it measures.
  - Was: "The correlation between predicted and true growth rates is 0.40 for the canonical model, against 0.61 reported by \citet{Mai2024} on a larger cohort from the same clinic, and the fast-progressor AUCs are 0.70 to 0.74 against 0.77 to 0.81 ..."
  - Now: "The correlation between predicted and true growth rates is 0.40 for the canonical model, against 0.52 to 0.61 for the comparable models of~\S\ref{sec:experiments:qualitative}, and its fast-progressor AUCs are 0.70 to 0.74 against 0.77 to 0.81 reported by \citet{Mai2024} on the full cohort from which the data here are ..."
- **6-7.27** [low] §6.2 location versus speed · `06-discussion.tex:165` · **Done**: 2026-10-19 (own wording)
  - Issue: 'The gap belongs to the approach' personifies the gap, and the sentence closes on a 'rather than' antithesis.
  - Was: "The other arms do not differ from the canonical model on these measures, so the gap belongs to the approach rather than to one operator."
  - Review suggested: "The other arms do not differ from the canonical model on these measures, so the gap lies in the shared approach and is not specific to one operator." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.28** [medium] §6.2 comparison with Mai et al. · `06-discussion.tex:169` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: Two mirrored 'whereas' clauses joined by a semicolon give a symmetrical, mechanical rhythm. 'It is still notable that' is evaluative filler.
  - Was: "\citet{Mai2024} start from the raw OCT volume, whereas every model here starts from segmented masks and layer depths; they evaluate 184 eyes with no reported cropping of the lesion area, whereas this thesis evaluates 75 eyes inside a crop that censors growth ..."
  - Review suggested: "\citet{Mai2024} start from the raw OCT volume and evaluate 184 eyes with no reported cropping of the lesion area. Every model here starts from segmented masks and layer depths and is evaluated on 75 eyes inside a crop that censors growth at its border. Even ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.29** [low] §6.2 growth speed (explanations) · `06-discussion.tex:182` · **Done**: 2026-10-19 (own wording)
  - Issue: The sentence opens with a conversational 'And', and 'nothing ... tells the operator' personifies the conditioning.
  - Was: "And, as argued in \S\ref{sec:discussion:interpretation}, nothing in the conditioning tells the operator how fast this particular eye progresses."
  - Review suggested: "Finally, as argued in \S\ref{sec:discussion:interpretation}, the conditioning carries no information on how fast this particular eye progresses." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.30** [medium] §6.2 clinical relevance of growth speed · `06-discussion.tex:186` (today `06-discussion.tex:261`) · **Done**: 2026-10-19 (as suggested)
  - Issue: The paragraph opens with an announcement and uses the idiom 'most worth its burden'. 'That decision' then refers to a decision that has not been named.
  - Was: "The distinction matters clinically. Complement inhibitors slow GA growth but do not stop it (\S\ref{sec:introduction:motivation}), so the eyes that grow fastest are the ones for which treatment is most worth its burden. That decision depends on growth speed, ..."
  - Now: "The distinction is clinically relevant. Complement inhibitors slow GA growth but do not stop it (\S\ref{sec:introduction:motivation}), so the benefit of treatment relative to its burden is largest in the eyes that grow fastest. The decision to treat therefore depends on growth speed, the weaker of the two capabilities."
- **6-7.31** [medium] §6.2 'Reliable horizon.' · `06-discussion.tex:195` (today `06-discussion.tex:271`) · **Done**: 2026-10-19 (as suggested)
  - Issue: The section switches from the change-region Dice (L158) to the growth-region Dice without a reminder of the difference. The heading 'Reliable horizon' promises a verdict that the paragraph declines to give.
  - Was: "Beyond one year, the growth-region Dice of the canonical model does not fall; it lies at about 0.60 to 0.66 in the second, third and later years (\S\ref{sec:experiments:ingredients:transport})."
  - Now: "Beyond one year, the growth-region Dice of the canonical model, which scores only new atrophy, does not fall; it lies at about 0.60 to 0.66 in the second, third and later years (\S\ref{sec:experiments:ingredients:transport}). (Also consider renaming the heading to \paragraph{Forecast horizon.})"
- **6-7.32** [medium] §6.2 grader agreement as scale · `06-discussion.tex:209` (today `06-discussion.tex:286`) · **Done**: 2026-10-19 (as suggested)
  - Issue: 'Less far from what is attainable than it would appear' is a convoluted double comparison that is hard to parse.
  - Was: "A forecast with a growth-region Dice of about 0.5 in the first year, as here (Table~\ref{tab:experiments:mai-bins}), is accordingly less far from what is attainable than it would appear on a scale from 0 to 1."
  - Now: "On this scale, the first-year growth-region Dice of about 0.5 obtained here (Table~\ref{tab:experiments:mai-bins}) lies closer to the attainable level than its distance from 1 suggests."
- **6-7.33** [medium] §6.2 grader agreement as scale · `06-discussion.tex:212` (today `06-discussion.tex:290`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Orientation point' is a Germanism (Orientierungspunkt). The sentence stacks three devices: an 'X, not Y' antithesis, a colon reveal and 'rather than'.
  - Was: "The grader value is an orientation point, not a target or an upper limit for the models of this thesis: it was measured on a different imaging modality and a different cohort, and the graders outlined existing images rather than predicting a future one."
  - Now: "It was measured on a different imaging modality and a different cohort, and the graders outlined existing images rather than predicting a future one."
- **6-7.34** [low] §6.2 'Position in a clinical pipeline.' · `06-discussion.tex:227` (today `06-discussion.tex:302`) · **Done**: 2026-10-19 (own wording)
  - Issue: After a sentence on segmentation errors, 'Failures' could mean segmentation or forecast failures. 'Matter most' also mixes how often failures occur with how much they cost.
  - Was: "Failures would matter most where the method is known to be weak: lesions that touch the border of the crop, where growth is censored; fast progressors; and eyes with sparse visit schedules, where each step must bridge a long interval."
  - Now: "Forecast failures are most likely where the method is known to be weak: lesions that touch the border of the crop, where growth is censored (\S\ref{sec:experiments:folds}); fast progressors, whose growth is under-predicted (\S\ref{sec:experiments:qualitative}); and eyes with sparse visit schedules, where each step ..."
- **6-7.35** [medium] §6.3 'Data and labels.' (crop) · `06-discussion.tex:247` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: The elliptical list ('more than 5 % of the lesion in 6.0 %') makes the reader reconstruct what each percentage refers to.
  - Was: "It cuts real lesion area in 27.3\,\% of the visits, more than 5\,\% of the lesion in 6.0\,\%, and up to 25.7\,\% in the worst case."
  - Review suggested: "It cuts away part of the lesion in 27.3\,\% of the visits; in 6.0\,\% the loss exceeds 5\,\% of the lesion, and in the worst case it reaches 25.7\,\%." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.36** [low] §6.3 'Data and labels.' (crop) · `06-discussion.tex:249` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: A comma-heavy chain of four clauses ends in jargon ('without any flag').
  - Was: "In 31.1\,\% of the visits, the lesion touches the edge of the imaged field inside the window, so its growth across that edge is censored, in the training targets and in the metrics, without any flag."
  - Now: "The fixed $49 \times 1024$ window censors growth at its border, in the training targets and in the metrics, without any flag (\S\ref{sec:data:spatial})."
- **6-7.37** [low] §6.3 'Data and labels.' (crop) · `06-discussion.tex:252` · **Done**: 2026-10-02 (one-word pass)
  - Issue: 'Anyway' is conversational.
  - Was: "Larger windows would trade this for up to 35\,\% zero padding and about $1.9\times$ as many grid positions, and about 19\,\% of lesions would touch the border anyway because they reach the edge of the scan itself."
  - Review suggested: "Larger windows would trade this for up to 35\,\% zero padding and about $1.9\times$ as many grid positions, and about 19\,\% of lesions would still touch the border because they reach the edge of the scan itself." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.38** [medium] §6.3 'Data and labels.' (reference masks) · `06-discussion.tex:266` (today `06-discussion.tex:335`) · **Done**: 2026-10-19 (sentence kept; moved or its context changed)
  - Issue: The paragraph already covers pixel spacing and label provenance. Starting the shrinkage point mid-paragraph with 'also' makes it read as another remark about spacing.
  - Was: "The reference masks also shrink between visits."
  - Now: "The reference masks also shrink between visits."
- **6-7.39** [medium] §6.3 'Data and labels.' (reference masks) · `06-discussion.tex:269` (today `06-discussion.tex:338`) · **Done**: 2026-10-19 (as suggested)
  - Issue: For an ML readership, 'regression' could be read as statistical regression rather than regression of the lesion. 'It' in the next sentence has no clear referent.
  - Was: "This pattern is more consistent with annotation and registration noise at the boundary than with regression, although the masks alone cannot separate the two. It is one reason why no monotonic-growth constraint was imposed."
  - Now: "This pattern is more consistent with annotation and registration noise at the boundary than with regression of the atrophy, although the masks alone cannot separate the two. The observed shrinkage is one reason why no monotonic-growth constraint was imposed."
- **6-7.40** [medium] §6.3 'Model scope.' (PINNs and grid) · `06-discussion.tex:296` (today `06-discussion.tex:366`) · **Done**: 2026-10-19 (own wording)
  - Issue: After 'Model scope' the paragraph starts abruptly, with no link to the paragraph before it, and then jumps from PINNs to the grid. 'The residual' is not specified.
  - Was: "Physics-informed neural networks were deliberately not run, because the governing equation is unknown and the residual would have to be taken on a binary mask. All operators work on the uniform $49 \times 1024$ grid."
  - Now: "Physics-informed neural networks were deliberately not run, because the governing equation is unknown and the equation residual would have to be taken on a binary mask."
- **6-7.41** [low] §6.4 'Spatial pre-processing.' · `06-discussion.tex:314` · **Superseded**: passage rewritten (mostly the Chapter 5 reporting pass of 2026-10-02)
  - Issue: §6.3 (L249) states the proportion per visit ('In 31.1 % of the visits ...'), but here the reference set is 'the cropped lesions'. Readers may take these for two different statistics.
  - Was: "The fixed centre crop censors growth for about a third of the cropped lesions."
  - Review suggested: "The fixed centre crop censors growth in about a third of the visits." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.42** [low] §6.4 'Trajectory memory.' · `06-discussion.tex:321` (today `06-discussion.tex:408`) · **Done**: 2026-10-19 (as suggested)
  - Issue: The present tense presents an untested remedy as fact, out of step with the conditional 'would let it' just before. 'Apply' is vague.
  - Was: "This addresses the growth-speed gap of \S\ref{sec:discussion:clinical} directly. It is also the setting in which sequence models such as recurrent networks and transformers apply."
  - Now: "This would address the growth-speed gap of \S\ref{sec:discussion:clinical} directly. It is also the setting in which sequence models such as recurrent networks and transformers become applicable."
- **6-7.43** [medium] §6.4 'A valid transport model.' · `06-discussion.tex:337` (today `06-discussion.tex:424`) · **Done**: 2026-10-19 (as suggested)
  - Issue: The sentence is long, with a dangling participle phrase ('starting from ...') and two coordinated relative clauses.
  - Was: "A velocity parameterisation that is bounded by construction, starting from the energy-conserving form, would give a model that stays numerically valid over multi-year horizons and whose velocity field could be read as a direction and speed of growth."
  - Now: "A next step is a velocity parameterisation that is bounded by construction and builds on the energy-conserving form. A model with such a parameterisation would stay numerically valid over multi-year horizons, and its velocity field could be read as a direction and speed of growth."
- **6-7.44** [medium] Ch. 7 'The framework.' · `07-conclusion.tex:16` (today `07-conclusion.tex:15`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Absorbs the irregularity' is a metaphor that leaves the reader to guess what is irregular.
  - Was: "The forecast needs a setup that absorbs the irregularity of clinical data and treats every candidate model the same way."
  - Now: "For the first part, the forecast requires a setup that accommodates the irregular visit schedules of clinical data and treats every candidate model equally."
- **6-7.45** [low] Ch. 7 'The framework.' · `07-conclusion.tex:21` (today `07-conclusion.tex:21`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Held fixed' and 'without change' say the same thing, and 'change' is repeated. 'Learned to predict change far above persistence' attaches the comparison to the wrong element.
  - Was: "Held fixed, it served operators from unrelated literatures without change, and every operator with spatial context learned to predict change far above persistence."
  - Now: "The same framework served operators from unrelated literatures without modification, and every operator with spatial context learned to predict change and scored far above persistence."
- **6-7.46** [medium] Ch. 7 'The framework.' · `07-conclusion.tex:24` (today `07-conclusion.tex:26`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'This' lacks a clear antecedent, and the colon places the soft-Dice gain under 'required', although it is an improvement rather than a requirement. 'Added about 0.05' does not say to what.
  - Was: "This required a loss that puts weight on the lesion mask: without the weighting the canonical operator learned no change at all, and a soft-Dice term added about 0.05."
  - Now: "A soft-Dice term on the mask added about 0.05 to the change-region Dice."
- **6-7.47** [medium] Ch. 7 'The framework.' · `07-conclusion.tex:27` (today `07-conclusion.tex:27`) · **Done**: 2026-10-19 (own wording)
  - Issue: This is a near-verbatim repeat of the §6.1 aphorism, with the idiom 'bought nothing'. 'What did not matter' (L68-69) states the Runge-Kutta null again.
  - Was: "How time enters the update mattered less than that it enters: a higher-order Runge--Kutta step bought nothing over a single Euler step."
  - Now: "The interval length has to reach the operator, but the form in which it does so mattered little: a fourth-order Runge--Kutta step gave no measurable gain over a single Euler step."
- **6-7.48** [medium] Ch. 7 'The operator.' · `07-conclusion.tex:33` · **Done**: 2026-10-19 (own wording)
  - Issue: A cleft opener ('is not what decides') is followed by an em-dash list copied verbatim from §6.1 L52, and the sentence ends in three trailing prepositional phrases.
  - Was: "The architecture class is not what decides the outcome. The three strongest operators come from three unrelated classes --- a finite-element network, a graph network and a U-Net --- and lie within about 0.04 of each other, at a change-region Dice of about ..."
  - Review suggested: "The architecture class does not decide the outcome. The three strongest operators (a finite-element network, a graph network and a U-Net) come from unrelated classes. At one year they reach a change-region Dice of about 0.50 to 0.54, against zero for ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **6-7.49** [medium] Ch. 7 'The operator.' · `07-conclusion.tex:37` (today `07-conclusion.tex:35`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'The two that carry the reach and transport properties below' leaves the reader to work out which operator carries which property. 'What separates operators are ...' is a pseudo-cleft with awkward agreement.
  - Was: "The finite-element network is highest, above the U-Net at both seeds and slightly above the graph network; these two highest operators are the two that carry the reach and transport properties below. What separates operators are a few properties that were ..."
  - Now: "The finite-element network scores highest: above the U-Net at both seeds, and slightly above the graph network, a lead that is not established."
- **6-7.50** [low] Ch. 7 'The operator.' (spatial context bullet) · `07-conclusion.tex:43` (today `07-conclusion.tex:39`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'At all' is used as an intensifier.
  - Was: "Without it, a model predicts no change at all; one ring of neighbours raises the change-region Dice from 0 to about 0.45."
  - Now: "A few properties, each measured one at a time, separate the operators: \item \textbf{Spatial context.} A model without spatial context predicts no change; one ring of neighbours raises the change-region Dice from 0 to about 0.45."
- **6-7.51** [medium] Ch. 7 'The operator.' (transport bullet) · `07-conclusion.tex:51` (today `07-conclusion.tex:49`) · **Done**: 2026-10-19 (as suggested)
  - Issue: The first 'it' refers to the change-region Dice of the previous bullet, across a bullet boundary, and the second 'it' refers to the term. Three results are packed into one semicolon chain.
  - Was: "Adding a learned transport term to a Finite Element Network raised it by 0.062 over the same network without it, and by 0.072 over a parameter-matched control on the four folds on which that control trained; at a second seed the control trained on all five ..."
  - Now: "Adding a learned transport term to a Finite Element Network raised the change-region Dice by 0.062 over the same network without the term. Against a parameter-matched control, the margin was 0.072 on the four folds on which that control trained, and 0.076 at a second seed, where the control trained on all five folds."
- **6-7.52** [medium] Ch. 7 'The operator.' (synthesis) · `07-conclusion.tex:60` (today `07-conclusion.tex:55`) · **Done**: 2026-10-19 (own wording)
  - Issue: The FNO sentences separate this interpretation from the bullets it interprets. The closing appositive ('more informative than the score of any single model') is an aphoristic tag.
  - Was: "Reach and transport are two unrelated ways to correct the same deficit: a single update that cannot see as far as the disease moves between two visits. That two independent routes lead to the same level is the central architectural result of this thesis, more ..."
  - Now: "Reach and transport are two unrelated ways to correct the same deficit: a single update that cannot see as far as the disease moves between two visits."
- **6-7.53** [low] Ch. 7 'What did not matter.' · `07-conclusion.tex:72` (today `07-conclusion.tex:69`) · **Done**: 2026-10-19 (as suggested)
  - Issue: The subject is personified ('diagnostics ... limit what may be said') and the sentence ends in an 'X, not Y' antithesis. It states a limit on interpretation rather than a negative result, so it does not fit the heading.
  - Was: "The validity diagnostics also limit what may be said: the canonical model is a one-step map conditioned on the length of the step, not a continuous-time model."
  - Now: "The validity diagnostics also restrict how the canonical model may be described: it is a one-step map conditioned on the step length and does not behave as a continuous-time model."
- **6-7.54** [medium] Ch. 7 'Clinical position.' · `07-conclusion.tex:80` (today `07-conclusion.tex:78`) · **Done**: 2026-10-19 (own wording)
  - Issue: 'Which' could attach to the clinic, the cohort or the model, and the sentence chains four qualifications.
  - Was: "On growth speed, the canonical model reaches a correlation of 0.40 with the true growth rates, against 0.61 for the model of \citet{Mai2024} on a larger cohort from the same clinic, which starts from the raw OCT volume where this thesis starts from segmented ..."
  - Now: "On how fast, the model reaches a correlation of 0.40 with the true growth rates, against 0.52 to 0.61 for comparable models, including the model of \citet{Mai2024}, which starts from the raw OCT volume instead of segmented masks."
- **6-7.55** [low] Ch. 7 'Clinical position.' · `07-conclusion.tex:86` (today `07-conclusion.tex:83`) · **Done**: 2026-10-19 (as suggested)
  - Issue: A tricolon with a metaphorical verb ('bound'). The sentence applies to every conclusion but closes a paragraph about growth speed.
  - Was: "The small cohort, the censoring of the fixed crop and the missing memory of past visits bound every conclusion drawn here."
  - Now: "Every conclusion drawn here is limited by the small cohort, the censoring by the fixed crop and the lack of memory of past visits. (Consider moving it into the final paragraph, before the closing claim.)"
- **6-7.56** [medium] Ch. 7 'Take-away.' · `07-conclusion.tex:89` (today `07-conclusion.tex:88`) · **Done**: 2026-10-19 (own wording)
  - Issue: The final sentence of the thesis combines several tells: an informal heading, a pseudo-cleft ('what matters is'), an em-dash aside with 'above all' and a closing 'rather than' antithesis. Together they read as a formulaic closer.
  - Was: "\paragraph{Take-away.} For forecasts from longitudinal medical imaging in a low-data clinical setting, what matters is the framework around the model and the properties of the operator placed in it --- above all, whether one update can see as far as the ..."
  - Now: "Of these properties, the most important was whether one update can see as far as the disease moves between two visits."

## Appendices A-F

Source: `reviews/editorial-2026-10-01/09a-appendices-A-F.md`.

- **A.1** [medium] Appendix A.1 Visit Schedule and Lesion Scale · `91-appendix.tex:16` (today `91-appendix.tex:13`) · **Open**: text unchanged
  - Issue: The first sentence repeats almost word for word the chapter opener two lines above ("summarises the visit schedule, the lesion scale ...") and adds nothing new. This announce-then-repeat pattern is the flagged part; the unflagged second sentence carries the content.
  - Was: "The visit schedule and the lesion scale of the cohort are summarised in Figure~\ref{fig:appendix:cohort}. Most eyes were seen six or seven times, three in four intervals between visits are 180 days long, and the baseline lesion area ranges from 0.11 to ..."
  - Suggested: "As Figure~\ref{fig:appendix:cohort} shows, most eyes were seen six or seven times, three in four intervals between visits are 180 days long, and the baseline lesion area ranges from 0.11 to 20.8\,mm$^2$, with a median of 6.7\,mm$^2$."
- **A.2** [medium] Appendix A.2 Native Grids and the Crop · `91-appendix.tex:48` · **Superseded**: passage rewritten since the review (appendix figure and table work)
  - Issue: The list after the colon is elliptical. "more than 5 % of it" leaves "it" ambiguous, and "at most 25.7 %" can be misread as a share of visits, when it is the worst-case share of one lesion (cf. \S3.3).
  - Was: "Figure~\ref{fig:appendix:crop} relates the native grids of the eyes to the modelling window of~\S\ref{sec:data:spatial} and shows how much lesion area the window removes: some lesion area in 27.3\,\% of the visits, more than 5\,\% of it in 6.0\,\%, and at ..."
  - Now: "Figure~\ref{fig:appendix:crop} relates the native grids of the eyes to the modelling window of~\S\ref{sec:data:spatial}; how much lesion area the window removes is given there."
- **A.3** [low] Figure A.2 caption · `91-appendix.tex:63` (today `91-appendix.tex:61`) · **Open**: text unchanged
  - Issue: "eyes ... overlap" names the eyes where the plotted markers are meant. Saying that the markers coincide states directly why fewer than 75 points are visible.
  - Was: "The grid is the same at every visit of an eye, and eyes with identical grids overlap (67 distinct grids)."
  - Suggested: "The grid is the same at every visit of an eye, and the markers of eyes with identical grids coincide (67 distinct grids)."
- **A.4** [medium] Appendix D Additional Rollout Figures · `91-appendix.tex:98` (today `91-appendix.tex:89`) · **Done**: as suggested
  - Issue: One 60-word sentence carries the figure reference, the eye pool and four selection rules after a colon, and it repeats the caption almost verbatim. "border of the crop" also differs from the caption's "border of the imaged field" and from the \S5.1.2 term "edge of the imaged field". The selection actually uses the pad-aware edge.
  - Was: "Figure~\ref{fig:appendix:rollouts} shows rollouts of the canonical dilated-stencil graph network for four further eyes, chosen by fixed rules from the 48 validation eyes of folds 0, 1 and 2: the eyes with the highest and the lowest growth-region Dice at the ..."
  - Now: "Figure~\ref{fig:appendix:rollouts} shows rollouts of the canonical dilated-stencil graph network for four further eyes. They were chosen by fixed rules from the 48 validation eyes of folds 0, 1 and 2: the eyes with the highest and the lowest growth-region Dice at the one-year anchor, the eye with the most true-lesion ..."
- **A.5** [medium] Appendix D Additional Rollout Figures · `91-appendix.tex:103` · **Superseded**: passage rewritten since the review (appendix figure and table work)
  - Issue: "The two failure cases" is never defined. Four eyes are shown, and the reader must work out which two are meant. The colon reveal ("share one pattern:") is the flagged rhetorical tell.
  - Was: "The two failure cases share one pattern: the true lesion expands far beyond its baseline outline, and the predicted change stays a narrow band along that outline, so most of the true change is missed."
  - Review suggested: "In the two failure cases, panels~(b) and~(d), the true lesion expands far beyond its baseline outline while the predicted change stays a narrow band along that outline, so most of the true change is missed." (the passage was cut or rewritten; no single sentence corresponds today)
- **A.6** [medium] Appendix E (chapter heading) · `91-appendix.tex:139` (today `91-appendix.tex:133`) · **Open**: text unchanged
  - Issue: The heading promises ablation sweeps, but the chapter contains a border/interior split, growth-speed measures and a two-seed replication table, none of which is an ablation. The chapter also opens with no text, so the reader is not told what the three tables are for. The section labels (app:full-results:*) already point to the intended title.
  - Was: "\chapter{Ablation Details}"
  - Suggested: "Retitle to \chapter{Additional Result Tables} and add under it: "This appendix gives three tables that support Chapter~\ref{ch:experiments}: the headline metric on border-touching and interior eyes (Table~\ref{tab:appendix:border-interior}), the growth-speed measures of the arms ..."
- **A.7** [low] Table E.1 caption · `91-appendix.tex:150` (today `91-appendix.tex:144`) · **Open**: text unchanged
  - Issue: \S5.1.2 defines the split as the true lesion at the anchor touching the pad-aware edge of the imaged field. "border of the fixed crop" suggests a crop-only criterion that excludes the padded visits.
  - Was: "Change-region Dice at the one-year anchor, seed 42, split by whether the eye's lesion touches the border of the fixed crop (\S\ref{sec:data:spatial})."
  - Suggested: "Change-region Dice at the one-year anchor, seed 42, split by whether the eye's true lesion at the anchor touches the edge of the imaged field (\S\ref{sec:data:spatial})."
- **A.8** [low] Table E.1 caption · `91-appendix.tex:154` (today `91-appendix.tex:151`) · **Open**: text unchanged
  - Issue: The nested "mean over ... of the ... mean" chain makes the reader parse the order of the two averages.
  - Was: "Each value is the mean over the five folds of the late-epoch mean within that group."
  - Suggested: "Each value is the late-epoch mean within the group, averaged over the five folds."
- **A.9** [low] Tables E.1 and E.2, row labels · `91-appendix.tex:166` (today `91-appendix.tex:160`) · **Open**: text unchanged
  - Issue: Tables E.1 and E.2 use labels ("Dilated-stencil GNN", "k-NN GNN") that differ from Table 5.1 and Table F.2 ("Graph network, dilated stencil", "Graph network, $k$-NN, $k = 12$"). A reader matching rows across tables has to translate, and "k-NN GNN" does not state k.
  - Was: "Dilated-stencil GNN"
  - Suggested: "Use the row labels of Table~\ref{tab:experiments:arms} in Tables E.1 and E.2, as Table F.2 already does, e.g. "Graph network, dilated stencil" and "Graph network, $k$-NN, $k = 12$"."
- **A.10** [medium] Table E.2 caption · `91-appendix.tex:188` (today `91-appendix.tex:182`) · **Open**: text unchanged
  - Issue: A colon followed by comma-chained fragments replaces sentences, the most machine-like structure in the range. "The AUC separates" attributes the separation to the metric, when it is the predicted rate that separates the groups. "every arm" overstates, because the per-pixel floor of Table 5.1 is not listed.
  - Was: "Eye-level growth-speed measures for every arm of Table~\ref{tab:experiments:arms}, computed as for the canonical model in \S\ref{sec:experiments:qualitative:mai}: growth rate on the square-root area scale over each eye's whole follow-up, predicted rate ..."
  - Suggested: "Eye-level growth-speed measures for the arms of Table~\ref{tab:experiments:arms}, seed 42, computed as for the canonical model in \S\ref{sec:experiments:qualitative:mai}: the growth rate is taken on the square-root area scale over each eye's whole follow-up, the predicted rate is averaged over the late epochs, and the ..."
- **A.11** [low] Table E.2 caption · `91-appendix.tex:194` (today `91-appendix.tex:191`) · **Open**: text unchanged
  - Issue: "about ±0.2 wide" mixes a half-width (±) with a width, so the reader cannot tell whether the intervals span 0.2 or 0.4.
  - Was: "Only point estimates are given; the 95\,\% bootstrap intervals are about $\pm 0.2$ wide for every arm (see Table~\ref{tab:experiments:mai} for the canonical model), so the arms cannot be told apart on these measures."
  - Suggested: "Only point estimates are given; for every arm the 95\,\% bootstrap intervals reach about $\pm 0.2$ around the estimate (see Table~\ref{tab:experiments:mai} for the canonical model), so the arms cannot be told apart on these measures."
- **A.12** [medium] Table E.3 caption · `91-appendix.tex:238` · **Superseded**: passage rewritten since the review (appendix figure and table work)
  - Issue: The stacked "of the differences of the ..." chains are hard to parse. "first rollout step past 0.95 years" is not identified as the one-year anchor used throughout Chapter 5. The "Reading" line of every block is never explained.
  - Was: "Fold-paired: mean $\pm$ SE of the differences of the late-epoch change-region Dice over the five folds, with the number of folds on which the first arm is higher. Per eye: mean $\pm$ SE of the differences of the growth-region Dice at each eye's first rollout ..."
  - Now: "Fold-paired: mean $\pm$ SE of the differences of the late-epoch change-region Dice over the five folds, with the number of folds on which the first arm is higher and the $z$ statistic of \S\ref{app:full-results:criteria} ($|z| > 1.96$ corresponds to $p < 0.05$)."
- **A.13** [medium] Appendix F, Run identity · `91-appendix.tex:345` (today `91-appendix.tex:562`) · **Open**: text unchanged
  - Issue: Five uniform medium-length sentences contain two additive "also"s. The logic is unclear: the directory name already encodes the fold, so the reader cannot see why the fold is recorded again (the missing step is that the shared mount path does not identify the data). "trained in one piece" is an idiom.
  - Was: "Every run writes its complete configuration into its run directory at the start. The name of the directory encodes the key settings, the fold and the data variant. Since 2 September 2026, each run also records the version of the code it ran; earlier runs are ..."
  - Suggested: "At the start, every run writes its complete configuration into its run directory, whose name encodes the key settings, the fold and the data variant. Because every fold is mounted at the same path on the cluster, the path does not identify the data, so each run also records the fold and data variant it loaded. Since 2 ..."
- **A.14** [low] Table F.2 caption · `91-appendix.tex:361` (today `91-appendix.tex:578`) · **Open**: text unchanged
  - Issue: The table also lists "FEN, free-form, matched width 139", which is not a row of Table 5.1. A reader who looks for it there will not find it.
  - Was: "Experiment names of the arms of Table~\ref{tab:experiments:arms}, seed 42."
  - Suggested: "Experiment names of the arms of Table~\ref{tab:experiments:arms} and of the matched free-form control, seed 42."

## Appendix G (MM-PDE)

Source: `reviews/editorial-2026-10-01/09b-appendix-G.md`.

- **G.1** [medium] §G.1 Background: MM-PDE · `91-appendix.tex:401` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: The intensifier 'fundamentally' and the redundant 'while simultaneously' are clear tells. The consequence sits in a separate sentence where a colon would tie it to the claim.
  - Was: "\citet{Hu2024} extend message-passing neural solvers by integrating an adaptive moving mesh. A uniform mesh is fundamentally inefficient for problems that exhibit localised dynamics. It wastes computational resolution in smooth regions while simultaneously ..."
  - Now: "\citet{Hu2024} extend message-passing neural solvers with an adaptive moving mesh."
- **G.2** [low] §G.1 Background: MM-PDE · `91-appendix.tex:409` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'hostile to' personifies a property, and 'Conversely,' is a stock connector. The two sentences mirror each other ('both ... and ...' twice).
  - Was: "This changes both the topology and the total degrees of freedom between steps, a property that is hostile to standard graph-network training. Conversely, $r$-adaptation, or moving-mesh adaptation, moves a fixed set of nodes while maintaining both the node ..."
  - Review suggested: "This changes the topology and the number of degrees of freedom from step to step, which is poorly suited to standard graph-network training. In $r$-adaptation, or moving-mesh adaptation, a fixed set of nodes is moved, and the node count and the original graph ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.3** [low] §G.1 Background: MM-PDE · `91-appendix.tex:413` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'entirely' is filler. The sentence motivates the 'data-free' mesh mover introduced three paragraphs later, but the link is not signalled.
  - Was: "Prior neural $r$-adaptation methods were entirely supervised and required ground-truth optimal meshes generated by an expensive classical solver."
  - Now: "Earlier neural $r$-adaptation methods were supervised: they required optimal meshes from an expensive classical solver as training targets."
- **G.4** [medium] §G.1 Background: MM-PDE · `91-appendix.tex:417` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: There are seven sentences of near-identical shape ('The X ensures/keeps/dictates/is given by ...'). They carry fillers ('precisely', 'specific', 'established', 'corresponding'), and 'dictates' personifies a constant. This uniform rhythm is the clearest machine pattern in G.1.
  - Was: "The moving-mesh framework is governed by a monitor function. The monitor is defined as $M = (1 + \lVert \nabla u \rVert_2 / \alpha) I$, a matrix-valued function that takes large values precisely where the state solution varies sharply. The identity factor $I$ ..."
  - Now: "The mesh is guided by a monitor function."
- **G.5** [medium] §G.1 Background: MM-PDE · `91-appendix.tex:430` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: The definition is spread over two sentences ('is equal' ... 'Specifically, this integral must equal'). It is padded with 'every single', 'total' (twice) and 'identical', and opened with the signposts 'Specifically,' and 'Intuitively,'.
  - Was: "A coordinate map $f$ produces an $M$-uniform mesh if the integral of the density $\rho$ over the image of every single cell is equal. Specifically, this integral must equal $\sigma / N$, where $\sigma$ is the total integral of $\rho$ over the domain and $N$ ..."
  - Review suggested: "A coordinate map $f$ produces an $M$-uniform mesh if the integral of the density $\rho$ over the image of each cell equals $\sigma / N$, where $\sigma$ is the integral of $\rho$ over the domain and $N$ the number of cells. Every cell then carries the same ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.6** [medium] §G.1 Background: MM-PDE · `91-appendix.tex:450` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'Crucially' is on the author's banned list, and 'mathematically equivalent' is padding. The last sentence is a mixed construction: an act of 'enforcing' is not something one 'regularises'.
  - Was: "A scalar potential is learned rather than the full vector map because the convexity of $\phi$ is mathematically equivalent to a non-singular Jacobian of $f$. A non-singular Jacobian guarantees that the resulting mesh does not tangle. Crucially, enforcing ..."
  - Review suggested: "A scalar potential is learned instead of the full vector map because convexity of $\phi$ is equivalent to a non-singular Jacobian of $f$, which guarantees that the mesh does not tangle. Convexity of a scalar potential is far easier to regularise than a global ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.7** [low] §G.1 Background: MM-PDE · `91-appendix.tex:458` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'The network architecture reformulates' and 'is tasked with' are agentive phrasings. $\psi$ is called 'the displacement field', but by the equation just given the displacement is $\nabla\psi$ and $\psi$ is a scalar.
  - Was: "The network architecture reformulates the scalar potential residually as $\phi(x) = 0.5 \|x\|^2 + \psi(x)$. The gradient therefore becomes $\nabla \phi = x + \nabla \psi$. The network is tasked with predicting only the displacement field $\psi$. This ..."
  - Review suggested: "The potential is written in residual form, $\phi(x) = 0.5 \|x\|^2 + \psi(x)$, so that $\nabla \phi = x + \nabla \psi$. The network predicts only $\psi$, whose gradient is the displacement. This removes the trivial identity component from what the network has ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.8** [low] §G.1 Background: MM-PDE · `91-appendix.tex:469` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: A filler cluster ('entirely', 'dedicated', 'In this formulation,'). The two sentences can be one with a 'where' clause.
  - Was: "The DMM is trained entirely without mesh supervision via a dedicated physics loss $L = L_{\text{eq}} + \beta L_{\text{bound}} + \gamma L_{\text{convex}}$. In this formulation, $L_{\text{eq}}$ is the squared residual of the Monge--Amp\`ere equation evaluated ..."
  - Review suggested: "The DMM is trained without mesh supervision on the physics loss $L = L_{\text{eq}} + \beta L_{\text{bound}} + \gamma L_{\text{convex}}$, where $L_{\text{eq}}$ is the squared residual of the Monge--Amp\`ere equation at sampled interior points, ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.9** [medium] §G.1 Background: MM-PDE · `91-appendix.tex:475` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: Dramatic emphasis: 'critical', 'inevitably' and 'useless' are stacked into one clause.
  - Was: "The convexity term is critical; a non-convex potential inevitably yields a tangled and useless mesh, regardless of how small the equation residual becomes."
  - Review suggested: "The convexity term is needed because a non-convex potential yields a tangled, unusable mesh, however small the equation residual becomes." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.10** [low] §G.1 Background: MM-PDE · `91-appendix.tex:478` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: Fillers ('exclusively', 'subsequently', 'identical', 'different') inflate three plain facts.
  - Was: "Training uses the Adam optimiser followed by BFGS fine-tuning applied exclusively to the last layer. The DMM is pretrained and subsequently frozen during solver training. This decouples a well-posed geometric problem from the main solver objective and allows ..."
  - Review suggested: "Training uses Adam, followed by BFGS fine-tuning of the last layer only. The DMM is pretrained and then frozen during solver training. This separates a well-posed geometric problem from the solver objective and allows the same mesh mover to be reused across ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.11** [medium] §G.1 Background: MM-PDE · `91-appendix.tex:485` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: Symbols clash. At l. 418 $M$ is the monitor and $I$ the identity matrix; here $M$ is the update operator and $I$ the interpolation. $\alpha$ is also the monitor constant at l. 418-423 and the gate from G.2.2 on. 'is constructed as ..., defined as' is redundant.
  - Was: "The full moving-mesh update operator is constructed as a dual-branch composition, defined as $M(u_t) = G_1(u_t) + I(G_2, \tilde{f}, u_t)$."
  - Review suggested: "The moving-mesh update operator is the dual-branch composition $M(u_t) = G_1(u_t) + I(G_2, \tilde{f}, u_t)$, in which $M$ and $I$ no longer denote the monitor and the identity matrix. (Optionally add after the definition of $\alpha$ at l. 423-424: '(unrelated ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.12** [low] §G.1 Background: MM-PDE · `91-appendix.tex:495` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: There is a 'rather than relying on' antithesis, the filler 'directly', and a vague, dramatic ending ('destabilising the system').
  - Was: "The interpolation network, ItpNet, learns adaptive interpolation weights directly from the moved-mesh geometry rather than relying on fixed finite-element basis functions. It is pretrained with its own optimiser before joint dual-branch training begins, ..."
  - Review suggested: "The interpolation network, ItpNet, learns adaptive interpolation weights from the moved-mesh geometry instead of using fixed finite-element basis functions. It is pretrained with its own optimiser before the joint training of both branches, because an ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.13** [low] §G.1 Background: MM-PDE · `91-appendix.tex:502` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: This general pointer arrives after the method has been described, between ItpNet and the ablations, where it interrupts. The embedded relative clause 'on which this framework builds' is awkward.
  - Was: "The classical background for adaptive moving meshes on which this framework builds is covered extensively by \citet{HuangRussell2011}."
  - Review suggested: "Move it to the second paragraph, directly after '... the original graph topology.' (l. 413), and reword: 'The classical theory of adaptive moving meshes, on which this framework builds, is treated in detail by \citet{HuangRussell2011}.'" (the passage was cut or rewritten; no single sentence corresponds today)
- **G.14** [medium] §G.1 Background: MM-PDE · `91-appendix.tex:504` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: The subject is four gerund clauses plus a parenthesis, so the reader waits about 40 words for 'each increases'. The tense also shifts: l. 401 and l. 508 use the present, here the past.
  - Was: "\citet{Hu2024} reported several architectural ablations of the dual-branch solver. Removing the uniform-mesh branch, replacing the moved branch by a second branch on the original mesh, removing the residual-cut network of the original model (not used in this ..."
  - Now: "\citet{Hu2024} report four ablations of the dual-branch solver: removing the uniform branch, replacing the moved branch by a second branch on the original mesh, removing the residual-cut network of their model (not used in this thesis), and replacing the DMM mesh by the uniform mesh."
- **G.15** [medium] §G.1 Background: MM-PDE · `91-appendix.tex:512` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: An inverted pseudo-cleft ('Whether X ... is the question this appendix tests') used as a stock closing flourish. It stands alone as a one-sentence paragraph and states the appendix's purpose only after three pages of background, and G.2 then restates it.
  - Was: "Whether mesh adaptation provides a measurable benefit for slowly evolving clinical data is the question this appendix tests."
  - Review suggested: "Move the question to a short opening under the chapter heading (see flow notes) and phrase it directly: 'This appendix tests whether mesh adaptation gives a measurable benefit on slowly evolving clinical data.' Delete it here." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.16** [low] §G.2 The Moving-Mesh Extension for GA · `91-appendix.tex:521` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: The paragraph opens with an announcement ('This section describes') and repeats 'built'. Four short sentences say what two can.
  - Was: "This section describes how the moving-mesh solver of \citet{Hu2024} (\S\ref{app:mm-pde:background}) was adapted to GA forecasting. A data-free mesh mover and a dual-branch graph network were built on top of the fixed framework of \S\ref{sec:method:framework}. ..."
  - Review suggested: "The moving-mesh solver of \citet{Hu2024} (\S\ref{app:mm-pde:background}) was adapted to GA forecasting by adding a data-free mesh mover and a dual-branch graph network to the fixed framework of \S\ref{sec:method:framework}. The complete extension was ..." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.17** [medium] §G.2 The Moving-Mesh Extension for GA · `91-appendix.tex:529` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: The opener is an empty aphorism, since every experiment is a measurement; what is meant is that the design makes the outcome measurable. 'decides' personifies the gate, and 'at all' is emphatic filler.
  - Was: "The experiment was designed as a measurement. A learnable scalar gate, initialised to zero, decides how much of the correction computed on the moved mesh enters the prediction, so its trajectory shows whether the correction is used at all."
  - Now: "Two design choices make the experiment a measurement."
- **G.18** [medium] §G.2.1 Data-Free Mesh Mover for GA · `91-appendix.tex:546` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: From here on 'branch' means two things: the solver branches (here) and the DeepONet branch network of the mesh mover (l. 554, 578, 613). The clause after the semicolon repeats the paragraph's first sentence.
  - Was: "The network branches on the uniform and on the moved mesh still process all eleven channels; only the mesh mover reads the mask alone."
  - Now: "Only the mesh mover reads the mask alone; both solver branches process all eleven channels."
- **G.19** [low] §G.2.1 Data-Free Mesh Mover for GA · `91-appendix.tex:548` (today `91-appendix.tex:750`) · **Done**: as suggested
  - Issue: A trained version is said to be 'replaced by the native grid', which mismatches subject and replacement.
  - Was: "An earlier version was trained on a square $256 \times 256$ mask sampled from the fundus image; it was replaced by the native grid, which removes a resize round trip during the rollout."
  - Now: "An earlier version was trained on a square $256 \times 256$ mask sampled from the fundus image. It was replaced by a version trained on the native grid, which removes a resize round trip during the rollout."
- **G.20** [low] §G.2.1 Data-Free Mesh Mover for GA · `91-appendix.tex:559` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'the base head' is never defined. The reader cannot tell whether it is the head of \citet{Hu2024} or of the starting configuration of the search.
  - Was: "A head maps the concatenated branch and trunk outputs to the scalar potential $\phi$ through widths 1024, 512, 512 and 1, one layer deeper than the base head."
  - Now: "A head maps the concatenated outputs of encoder and trunk to the scalar potential $\phi$ through widths 1024, 512, 512 and 1, one layer deeper than the base head."
- **G.21** [medium] §G.2.1 Data-Free Mesh Mover for GA · `91-appendix.tex:577` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'Two parts' are announced but not named: the blur follows, and the logarithm only three sentences later, after a divergence aside. 'the branch' is ambiguous right after the mention of solver branches at l. 546.
  - Was: "Two parts of this monitor were needed. The blur ($\sigma = 1.0$\,px) is applied for the monitor only; the branch always sees the raw binary mask."
  - Now: "Two parts of this monitor were necessary."
- **G.22** [medium] §G.2.1 Data-Free Mesh Mover for GA · `91-appendix.tex:579` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: The contrast 'the first GA run diverged' vs 'On the native grid ... no longer diverges' implies the first run differed in grid or monitor, but the text does not say how. The reader cannot tell what changed.
  - Was: "A binary mask has a step at the lesion edge, and without the blur the first GA run diverged to NaN. On the native grid, the unblurred monitor no longer diverges but leaves the mesh almost unmoved (\S\ref{app:mm-pde:mesh-quality})."
  - Now: "Without the blur, the step of the binary mask at the lesion edge made the first GA run diverge to NaN."
- **G.23** [low] §G.2.1 Data-Free Mesh Mover for GA · `91-appendix.tex:584` (today `91-appendix.tex:786`) · **Done**: as suggested
  - Issue: A two-item list in which the first item has its own internal 'and' plus a 'which' clause, so it is hard to see where the first item ends.
  - Was: "Two further ideas were tested and left out: a blur kernel stretched along the columns to match the physical spacing, which gave no gain ($p = 0.95$) and folded the mesh intermittently, and a penalty on the Jacobian determinant, which made folding worse."
  - Now: "Two further ideas were tested and left out. A blur kernel stretched along the columns to match the physical spacing gave no gain ($p = 0.95$) and folded the mesh intermittently. A penalty on the Jacobian determinant made folding worse."
- **G.24** [medium] §G.2.1 Data-Free Mesh Mover for GA · `91-appendix.tex:605` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: Three pronouns refer to different things: 'it' is the mesh mover, 'this' is training on all masks, and the second 'it' is the training again.
  - Was: "Because it never sees a future state, this leaks no label, and it makes the same mesh mover in-distribution for every fold."
  - Now: "Because it never sees a future state, this leaks no label, and the same mesh mover is in-distribution for every fold."
- **G.25** [low] §G.2.1 Data-Free Mesh Mover for GA · `91-appendix.tex:609` (today `91-appendix.tex:810`) · **Done**: as suggested
  - Issue: 'Quality' is used before its metrics are defined in G.3, and 'levers' is a business metaphor.
  - Was: "The configuration was selected from a 55-run search on the native grid. Quality improved with the number of epochs up to 500. The two largest levers were the extra head layer and the sharper blur of $\sigma = 1$ instead of 2, and they helped only together."
  - Now: "The configuration was selected from a 55-run search on the native grid. Mesh quality (\S\ref{app:mm-pde:mesh-quality}) improved with the number of epochs up to 500. The two changes with the largest effect were the extra head layer and the sharper blur of $\sigma = 1$ instead of 2, and they helped only together."
- **G.26** [medium] §G.2.2 Dual-Branch Composition · `91-appendix.tex:661` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: G.2 never says which graph the uniform branch uses in the reported runs. The next paragraphs mention the dilated stencil (l. 677) and 'the configuration of the five-fold runs' (l. 717), and only G.4 (l. 824-826) names the earlier k-NN network with mean and maximum aggregation. A reader of G.2 will likely assume the stencil.
  - Was: "Both branches are the graph network of \S\ref{sec:method:mppde}, with two message-passing rounds of width 64."
  - Now: "Both branches are the graph network of~\S\ref{sec:method:mppde}, with two message-passing rounds of width 64."
- **G.27** [medium] §G.2.2 Dual-Branch Composition · `91-appendix.tex:666` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'has to earn its weight' is a conversational idiom that personifies the correction.
  - Was: "At the start the dual model is therefore exactly the uniform branch alone, and the correction has to earn its weight."
  - Now: "At the start, the dual model is therefore identical to the uniform branch alone, and the correction enters the prediction only if training increases $|\alpha|$."
- **G.28** [low] §G.2.2 Dual-Branch Composition · `91-appendix.tex:668` (today `91-appendix.tex:874`) · **Done**: as suggested
  - Issue: 'which' can attach to 'the sum' instead of 'the two branches', and 'otherwise' has no clear anchor.
  - Was: "The gate also fixes the scale of the correction: the loss constrains only the sum of the two branches, which could otherwise grow large and cancel each other."
  - Now: "The gate also fixes the scale of the correction. The loss constrains only the sum of the two branches, so without the gate both branches could grow large and cancel each other."
- **G.29** [medium] §G.2.2 Dual-Branch Composition · `91-appendix.tex:673` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'a deadlock from which the branch could never activate' is dramatic, and 'the gate alone supplies the zero start' is an aphoristic closer appended after a semicolon.
  - Was: "If both the decoder and $\alpha$ started at zero, the gradients of both would be exactly zero, a deadlock from which the branch could never activate; the gate alone supplies the zero start."
  - Now: "If both the decoder and $\alpha$ started at zero, the gradients of both would be exactly zero, and the correction branch could never become active."
- **G.30** [medium] §G.2.2 Dual-Branch Composition · `91-appendix.tex:691` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: Each of the three sentences ends in a tacked-on clause. In the second, the training objective comes after the optimiser. In the third, the clause after the semicolon (clipping, gate) is unrelated to the 'because' clause before it.
  - Was: "The weights of the return direction are renormalised to sum to one at each point, with a sign-preserving floor of 0.1 on the denominator, which bounds the gain at 10; the floor is active at about 12.6\,\% of the points. ItpNet is pretrained at epoch 0 for 25 ..."
  - Now: "The weights of the return direction are renormalised to sum to one at each point, with a sign-preserving floor of 0.1 on the denominator, which bounds the gain at 10."
- **G.31** [medium] §G.2.2 Dual-Branch Composition · `91-appendix.tex:709` (today `91-appendix.tex:914`) · **Done**: as suggested
  - Issue: 'throttled' is an informal metaphor, and the second sentence buries its numbers in a mid-sentence aside. The 'layer encoder' appears without a pointer; in the rendered text it is introduced only briefly in §6.1.
  - Was: "Gradients are clipped to a norm of 1.0 separately in five groups: the uniform branch, the correction branch, the ItpNet weights, the gate $\alpha$ and the layer encoder; the mesh mover is frozen. Under one joint clip, the large gradients of ItpNet, with a ..."
  - Now: "Gradients are clipped to a norm of 1.0 separately in five groups: the uniform branch, the correction branch, the ItpNet weights, the gate $\alpha$ and the layer encoder of \S\ref{sec:discussion:interpretation}; the frozen mesh mover is excluded. The gradients of ItpNet have a median norm of $10^3$ to $10^4$ in the ..."
- **G.32** [low] §G.3 Moving Mesh Quality · `91-appendix.tex:732` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'on its own terms' is an idiom that adds nothing to 'independently of the prediction'. 'the same reference' is not identified.
  - Was: "The mesh mover was judged on its own terms, independently of the prediction. Four metrics were used. All of them depend only on the mask and use the same reference for every run."
  - Now: "The mesh mover was judged on its own terms, independently of the prediction, so that a defective mesh can be told apart from a correction branch that does not use a good one."
- **G.33** [medium] §G.3 Moving Mesh Quality · `91-appendix.tex:735` (today `91-appendix.tex:946`) · **Done**: as suggested
  - Issue: 'The edge gain asks' personifies a metric. In the three-step definition after the colon, the participles lose their subject: it is the band, not the border, that is normalised and then averaged.
  - Was: "The edge gain asks whether nodes move to the lesion border: the border is widened to a band of half-width 0.02 of the domain, normalised to a grid mean of 1, and averaged at the moved node positions."
  - Now: "The edge gain measures whether nodes move to the lesion border. The border is widened to a band of half-width 0.02 of the domain, the band is normalised to a mean of 1 over the grid, and its values are averaged over the moved node positions."
- **G.34** [low] §G.3 Moving Mesh Quality · `91-appendix.tex:740` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'the standard deviation divided by the mean of the cell areas weighted by ...' leaves unclear whether 'of the cell areas' applies to both the standard deviation and the mean. The appositive and the semicolon clause pile up at the end.
  - Was: "The reference coefficient of variation, \texttt{cov\_ref}, is the standard deviation divided by the mean of the cell areas weighted by one fixed reference monitor, the equidistribution measure of \citet{HuangRussell2011}; lower is more even."
  - Now: "The reference coefficient of variation, \texttt{cov\_ref}, is the standard deviation divided by the mean of the cell areas weighted by one fixed reference monitor, the equidistribution measure of~\citet{HuangRussell2011}; lower values mean a more even mesh."
- **G.35** [low] §G.3 Moving Mesh Quality · `91-appendix.tex:769` (today `91-appendix.tex:979`) · **Done**: as suggested
  - Issue: 'values ... say nothing' personifies the numbers.
  - Was: "No mesh folds: the number of tangled cells is zero on every scored mask, at every seed and every scored epoch. The values are in-sample and say nothing about generalisation to unseen lesions."
  - Now: "No mesh folds: the number of tangled cells is zero on every scored mask, at every seed and every scored epoch. The values are in-sample and do not show how the mesh mover generalises to unseen lesions."
- **G.36** [medium] §G.3 Moving Mesh Quality · `91-appendix.tex:774` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: The list is elliptical: verbs and subjects are dropped in items two and three. 'below the unmoved mesh' requires the reader to recall that the unmoved mesh scores 1.
  - Was: "On that pool, the configuration before the head and blur changes reaches an edge gain of 2.24, the same mesh mover without blur 1.34, and without the logarithmic compression 0.94, below the unmoved mesh."
  - Now: "On the spread pool, the configuration before the changes of head and blur reaches an edge gain of 2.24, the same mesh mover without blur 1.34, and the same without the logarithmic compression 0.94, below the unmoved mesh."
- **G.37** [medium] §G.3 Moving Mesh Quality · `91-appendix.tex:779` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'it' after the semicolon can refer to the weight of 1000 or the weight of 100. The 'lesion-specificity check' is not explained.
  - Was: "One choice is unverified. The boundary weight of 1000 was kept although a weight of 100 scored higher on edge gain, by 0.029 on head-16 and 0.105 on spread-16; it was rejected on a lesion-specificity check that was computed only on the biased head-16 pool."
  - Now: "One choice is unverified."
- **G.38** [low] §G.3 Moving Mesh Quality · `91-appendix.tex:785` (today `91-appendix.tex:997`) · **Done**: as suggested
  - Issue: 'drawn' means 'attracted' here, but in the figure caption (l. 806-807) it means 'plotted'.
  - Was: "In all three, nodes are drawn from the surrounding retina towards the lesion, most strongly at its border, and no cell folds."
  - Now: "In all three, nodes move from the surrounding retina towards the lesion, most strongly at its border, and no cell folds."
- **G.39** [medium] §G.3 Moving Mesh Quality · `91-appendix.tex:789` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'without folds that concentrate nodes' attaches the relative clause to 'folds', so on first reading the meshes lack folds that concentrate nodes. The 'thus ... therefore' pair is an aphoristic closer, and 'can therefore not' is unidiomatic.
  - Was: "The mesh mover thus produces valid meshes without folds that concentrate nodes on the lesion border. The null result of \S\ref{app:mm-pde:result} can therefore not be explained by a broken mesh."
  - Now: "The mesh mover thus produces valid meshes that concentrate nodes at the lesion border, and a defective mesh does not explain the result of~\S\ref{app:mm-pde:result}."
- **G.40** [low] §G.4 Result · `91-appendix.tex:857` (today `91-appendix.tex:1067`) · **Open**: text unchanged
  - Issue: 'tightest null' is jargon, and the purpose of the 0.016 threshold (to count as an effect) is left implicit.
  - Was: "This is the tightest null result of the project: its standard error is less than half the difference of 0.016 that a five-fold paired mean must exceed."
  - Suggested: "It is the most precise null result of the project: its standard error is less than half of 0.016, the difference that a five-fold paired mean must exceed to count as an effect."
- **G.41** [medium] §G.4 Result · `91-appendix.tex:864` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'in the first step, one optimiser step from the zero start' says the same thing twice. In 'averages 0.009 to 0.024 and 0.005 to 0.023' the reader must guess which range belongs to which arm. 'opens' is never defined.
  - Was: "The gate $\alpha$ never opens, with or without the moving mesh. In every fold of both arms it moves from zero to exactly $\pm 0.0020$ in the first step, one optimiser step from the zero start, as designed. It then peaks at 0.058 to 0.093 in the dual branch ..."
  - Now: "The gate stays shut, with and without the moving mesh."
- **G.42** [medium] §G.4 Result · `91-appendix.tex:869` (today `91-appendix.tex:1079`) · **Done**: 2026-10-02 (one-word pass)
  - Issue: The previous sentence gives two ranges per arm (peaks and mean absolute values), so 'The range' is ambiguous. For the mean absolute values the statement does not hold (0.005-0.023 does not enclose 0.009-0.024); only the peak range does.
  - Was: "The range of the bypass control encloses that of the dual branch, and the largest peak of either arm, 0.1005, belongs to a bypass fold."
  - Now: "The range of the peaks in the bypass control encloses that of the dual branch, and the largest peak of either arm, 0.1005, belongs to a bypass fold."
- **G.43** [medium] §G.4 Result · `91-appendix.tex:873` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: This reads as a complete explanation, yet the appendix closes with 'why the correction branch does not engage here is not explained by these experiments'. The probe explains why a near-zero gate stays near zero, not why the branch fails to engage in the first place.
  - Was: "A probe on the trained dual model shows why the gate stays shut."
  - Now: "A probe on the trained dual model explains why a gate near zero stays there."
- **G.44** [medium] §G.4 Result · `91-appendix.tex:878` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: A chiasmus ('gate gives the branch ... branch gives the gate') with personification ('no reason to open'). It is a polished, symmetrical closer.
  - Was: "A gate that starts at zero thus gives the branch almost no signal to learn from, and an untrained branch gives the gate no reason to open."
  - Review suggested: "With $\alpha$ near zero, the correction branch therefore receives almost no gradient, and while the branch is untrained, a larger $\alpha$ does not lower the loss." (the passage was cut or rewritten; no single sentence corresponds today)
- **G.45** [medium] §G.4 Result · `91-appendix.tex:882` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'opened the branch' mixes the metaphors: the gate opens, the branch engages, and one of the three runs has no gate. The second sentence runs to about 45 words with an unrelated semicolon clause, and the three runs are not marked as first, second and third.
  - Was: "Three further runs on fold 2 tested this reading, and none of them opened the branch. Without the gate, with the decoder zero-initialised instead, the change-region Dice falls to 0.3148 against 0.4878 for the gated dual model, a loss of 0.173, about five ..."
  - Now: "Three further runs on fold~2 tested this reading, and in none of them did the correction branch engage."
- **G.46** [medium] §G.4 Result · `91-appendix.tex:888` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'its counterpart' is vague. The sentence chains three findings with a semicolon and ends in a 'rather than' antithesis followed by a pseudo-cleft ('is not what keeps').
  - Was: "Without weight decay on the correction branch and ItpNet, the Dice is 0.0092 higher than its counterpart, under the single-fold floor; $\alpha$ peaks lower (0.058 against 0.067), and the parameters of the correction branch grow rather than shrink, so weight ..."
  - Now: "Without weight decay on the correction branch and ItpNet, the Dice is 0.0092 higher than its counterpart, under the single-fold floor."
- **G.47** [medium] §G.4 Result · `91-appendix.tex:892` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'reads' is jargon for 'scores'. 'however strong the uniform branch is' is a rhetorical flourish that generalises beyond the single fold-2 run it summarises.
  - Was: "On the dilated stencil, the dual model reads 0.5754 against 0.6060 for its own single-branch counterpart, a difference of $-0.031$ (per eye $-0.0305 \pm 0.0086$, 3 of 16 eyes), at roughly nine times the cost. The stencil's own gain carries over to the dual ..."
  - Now: "On the dilated stencil, the dual model scores 0.5754 against 0.6060 for its own single-branch counterpart, a difference of $-0.031$ (per eye $-0.0305 \pm 0.0086$, 3 of 16 eyes), at roughly nine times the cost."
- **G.48** [medium] §G.4 Result · `91-appendix.tex:899` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: A pseudo-cleft opener ('The finding is therefore that') with an em-dash aside holding a rhetorical tricolon. It is the most machine-like sentence in G.4.
  - Was: "The finding is therefore that the gated correction branch did not engage --- with the moving mesh or with the uniform grid in its place, with or without weight decay, with or without the gate --- and that the dual-branch model gave no measurable gain at about ..."
  - Now: "The dual-branch model gave no measurable gain at about ten times the cost."
- **G.49** [medium] §G.4 Result · `91-appendix.tex:903` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: The scope conclusion comes before the pre-registered reading it corrects. 'a statement ... says nothing' personifies, and 'that would mean that' doubles 'that'.
  - Was: "This is a statement about this implementation. It says nothing about whether mesh adaptation could help GA forecasting, because the bypass control behaves the same without any mesh. Before the runs, $\alpha \to 0$ had been fixed as a reportable outcome that ..."
  - Now: "This statement concerns this implementation and not mesh adaptation for GA in general."
- **G.50** [medium] §G.4 Result · `91-appendix.tex:908` (today `91-appendix.tex:1118`) · **Done**: as suggested
  - Issue: This reads against the probe paragraph (l. 873), which 'shows why the gate stays shut'. Two unrelated statements are joined by a semicolon.
  - Was: "\citet{Hu2024} report that their dual branch improves on the uniform grid on their benchmarks; why the correction branch does not engage here is not explained by these experiments."
  - Now: "\citet{Hu2024} report that their dual branch improves on the uniform grid on their benchmarks. Why the correction branch fails to engage here in the first place is not explained by these experiments."
- **G.51** [medium] §G.5 Outlook · `91-appendix.tex:918` · **Superseded**: Appendix G rewritten 2026-10-19 (b495589)
  - Issue: 'is the natural continuation' is an evaluative closing cliché, and 'the change happens in the next one' is vague. The paragraph does not connect to G.4.
  - Was: "In the moving-mesh extension, the monitor that guides the mesh is computed from the current state, whereas the change happens in the next one. A monitor built on a surrogate of the next state, the open problem named by \citet{Hu2024}, is the natural ..."
  - Now: "The monitor of the mesh mover is computed from the current state, whereas the change happens in the next one."

