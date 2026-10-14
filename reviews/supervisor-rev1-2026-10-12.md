# Supervisor review 1 (Dmitrii Lachinov), received 2026-10-12

Source: `main-thesis_dl_rev1.pdf` (build of 2026-10-02 00:29, 112 pages, i.e. after the
editorial high-severity fixes and the one-word pass, commit b9e2388; no `.tex` change since).
28 PDF annotations by `dlachinov`: 27 highlights with comments, 1 strike-out without comment.
**All comments fall on pp. 2–34: the abstract and Chapters 1–3.** Chapters 4–7 and the
appendices carry no marks. It is not yet known whether he stopped there or found nothing more.

Matched against the AI editorial review of 2026-10-01 (`reviews/editorial-2026-10-01/`,
session "Master's thesis academic review"). Status of each AI item as of 2026-10-02, from that
session's re-check: `open` = text unchanged, `changed` = passage rewritten since the review,
`partly` = adverb removed, rest open, `fixed`.

What the AI-review session already addressed (all before this PDF was built): the 15 high
items (incl. S1 swallowed sentences, S4 covariate promise, S5 mask provenance, 1.41 "same
deficit", 2a.7, 2a.17, 2b.37, 2b.44, 3.25), the three fix-first items (S9 "not auxiliary",
S22 dead pointers, "arm" defined), and a one-word pass (41 edits). Still open in Ch. 1–3:
Ch. 1 27 items (19 medium), §2.1 32 (20 medium), §2.2–2.4 41 (16 medium), Ch. 3 31 (14 medium),
plus structure items S2, S10, S15–S19, S23, S25, T1–T3, R1–R4, R12, R16, R17.

Legend: **SV** = supervisor comment. *Decision* = needs the author's call before editing.

---

## Supervisor's e-mail (2026-10-12)

"Overall, it looks good." Comments cover Ch. 1–3; **the rest follows next week**. Most comments
concern structure. Offers a meeting for questions.

| # | Point | Notes |
|---|---|---|
| M1 | **The abstract is the most important part** (most readers read only it, reviewers read it first): polish to near perfection. | Priority 1. See SV-A1–A6. |
| M2 | **Prerequisite audit:** read start to end and tick every new term (GA, PDE, …) as a prerequisite. The audience knows PDEs and boundary value problems, but not the medicine. After the current Introduction the reader has met AMD, GA, fovea, VA, OCT … without knowing what they are. | Systematic pass: list every term with its first use and its definition; every medical term defined before use. AI review's terms-before-definition lists (01 file, S19) are a starting point. |
| M3 | **Proposed structure of the opening chapter:** (1) **medical background**: eye, retina, retinal structure (schematic), photoreceptors, RPE; imaging (OCT, SLO, FAF); GA and its pathophysiology; novel drugs; needs in patient management and predictive methods; personalised medicine. (2) **PDEs and solvers**: no GA here, only formalism and current methods ("what you have now is already good"). (3) **Motivation**: "now it is well written", but place it here, where the context exists. (4) **Problem statement**: clear, sharp, concise, formal, e.g. "given measurements X (layer thicknesses) sampled at times T on the anisotropic lattice, learn a parametric neural operator 𝒩 (of GA progression) that maps the input to the solution"; introduce the notation used later, with a few equations. (5) **Thesis outline**. | Makes SV-X3/X4/2.2/2.6 concrete: largely decided by the supervisor. Proposed mapping below. Open: where Related Work goes (not in his list), and whether "Introduction" absorbs all of Ch. 2. |
| M4 | Section name "Why Neural PDE Solvers?" is not good: **no questions in headings**. Something like "Choice of the modelling approach", to be improved. | Also check the other headings (§2.2.5 "Why this structure suits …", §5.4.2 run-in questions were already removed). |
| M5 | **Contributions as bullet points**: what was achieved, what is novel, why it is valuable. | §1.4 Contributions was merged into §1.3 prose on 2026-10-01; reinstate as a bulleted list. Tie to SV-1.6 (Δt-conditioning novelty check). |

**Decided 2026-10-13 (author):** "operator" is kept and defined once. Ch. 1.2: "In this thesis,
this map is called the operator." §2.5.2 (to be written): "Throughout this thesis, the learned
function $f_\theta$ is called the *operator*. The term is used in its general sense, a map from the
state at one time to the state at a later time. It is not used in the narrower sense of the
neural-operator literature (§2.3), where it denotes models such as the FNO or DeepONet that learn
maps between function spaces. A U-Net and a graph network are operators in the first sense but not
in the second." Introduction and Background stay separate chapters. **Both points go into the
reply mail.**

**Note on terminology:** in the mail he writes "parametric neural operator 𝒩", while the PDF
comment says "neural solver, we are not necessarily dealing with operators". Ask which term he
wants before the thesis-wide rename (SV-X2).

### Proposed mapping onto M3 (to confirm)

1. **Introduction**
   1. Medical background: eye and retina (§2.1.1, schematic), retinal layers / photoreceptors /
      RPE (§2.1.1, Fig. 2.2), imaging OCT/SLO/FAF and en-face maps (§2.1.3, §2.1.4), GA and its
      pathophysiology incl. CAM/cRORA (§2.1.2), novel drugs and patient management (§1.1),
      predictive methods / personalised medicine (§1.1 end, parts of §2.4).
   2. PDEs and numerical solvers (§2.2.1–§2.2.4 with GA mentions removed; §2.3 neural PDE
      solvers and surrogate architectures).
   3. Motivation (§1.2 data properties, §1.3 GA-as-local-growth argument, §2.2.5; renamed per M4).
   4. Problem statement (new, formal): state $u_t$ on the lattice, irregular $t_k$, $\Delta t$,
      learned update $u_{t+\Delta t} = u_t + \Delta t\, f_\theta(u_t, \Delta t)$, the two-part
      research question. Notation currently spread over §2.2.2, §3.2, §4.2.
   5. Contributions (bullets, M5).
   6. Thesis outline.
2. **Related Work**, expanded into subsections (SV-2.7), as its own short chapter or as 1.x.
3. **Data**, now opening with the cohort and state representation from §2.1.5–§2.1.6 (SV-2.5).
4. onwards unchanged.

---

## 0. Cross-cutting (decide first, they change the whole thesis)

| # | Page | Supervisor | AI match | Notes |
|---|---|---|---|---|
| SV-X1 | p.13 (research question) | "framework" → better term is **methodology** | S19 (terminology drift: framework/setup) | *Decision.* Global rename touches every chapter, §4.2 heading, Ch. 7, abstract. "Methodology" usually means the thesis's method as a whole; check whether it fits "the fixed part around the solver". |
| SV-X2 | p.13 (research question) | "operator" → **neural solver**, "we are not necessarily dealing with operators" | S19 (operator / backbone / arm / model) | *Decision.* Same scope as X1. Note: "neural operator" is a specific class (FNO, DeepONet); the U-Net/GNN are not operators in that sense, so his point is technically right. Keep $f_\theta$ notation. |
| SV-X3 | p.12 | Restructure: make the **Introduction the main chapter, with the background (GA etc.) as its subsections**; end the introduction with motivation and problem statement (problem statement *after* the background). "You sometimes use terms before they are defined." | T1, T2, S15, S23; terms-before-definition list in 01 file (OCT, en-face, RPE, stencil) | *Decision* (CLAUDE.md: no restructuring without explicit instruction). Largest change of the review; X3, SV-2.6, SV-2.2 and SV-2.4 are one combined decision. |
| SV-X4 | p.25 (§2.2.5) | Merge §2.2.5 "Why this structure suits GA" with §1.3 "Why neural PDE solvers" and place it at the end, next to motivation / problem statement | S17 / T8 (learned solvers introduced twice), 2b.20–2b.25 (all open) | Part of the X3 decision. |

## 1. Abstract (p. 2)

The abstract was rewritten in tablet review v6 (2026-10-02), so most AI items 1.1–1.11 are `changed`
and stale. The supervisor's structure supersedes them.

| # | Supervisor | AI match | Notes |
|---|---|---|---|
| SV-A1 | **Structure:** (1) intro: problem, why hard, what this work solves, ending on the contributions (top 3, worded as important), ~1/3 page; (2) methods: MUW-GA data (n eyes, m patients, k visits on average, layer segmentations, anisotropic grids), what was implemented, how measured (metrics, mean ± std, stat tests, 5-fold, 1-year); (3) results + conclusions: strongest model 0.54 ± 0.04 at 1 y vs naive baseline, effect of spatial context, …, closing on realistic estimates of neural-solver performance on clinical data, tailored to the thesis. Smooth transitions. | 1.1–1.11 (mostly changed) | Full rewrite, EN + German Kurzfassung. Numbers only from Table 5.1 / NOTES. |
| SV-A2 | "is a lesion of lost retinal tissue": GA is a disease manifested as a lesion; better "GA is the advanced form of AMD … manifested as a gradual and irreversible loss of retinal tissue" | — | Wording given. |
| SV-A3 | "Forecasting the lesion … is difficult because visits are irregularly spaced, …, cohorts are small": rephrase, e.g. difficulty is the **highly variable progression patterns and rates** in the population | — | Same point as SV-1.3. |
| SV-A4 | "This thesis asks what such a forecast needs": more formal, e.g. "This thesis aims to study GA progression from the computational modelling perspective and determine …" | — | |
| SV-A5 | "49 × 1024": too much detail for an abstract | — | |
| SV-A6 | "Together, …" / "For the framework, …" / "For the operator, …": paragraph openers feel disconnected | — | These openers came from review v6 (author request); now to be replaced. |

## 2. Chapter 1 Introduction (pp. 10–13)

| # | Page | Supervisor | AI match (status) | Notes |
|---|---|---|---|---|
| SV-1.1 | p.10, §1.1 | "…no known, cost-effective means can prevent or treat (Flaxman). Clinical care therefore focuses …": make it **two separate sentences**; also **two treatments are now approved in the US, not the EU**, and they only slow progression: **pegcetacoplan and avacincaptad pegol** | 1.13 (open: garden-path, AMD↔GA jump), 1.16 (open: "therapeutic landscape empty") | Check that §1.1 names both drugs and the US-only approval (EMA refused pegcetacoplan); needs a citation for the EU status. |
| SV-1.2 | p.11, §1.1 | Paragraph "…lesions continued to grow … This thesis pursues that avenue": **"Well written"** | 1.17, 1.18, 1.19 (open: flag the same paragraph as templated) | **Conflict:** the supervisor likes it, the AI review wants it rewritten. Proposal: leave it, at most drop "This thesis pursues that avenue." Drop the AI items. |
| SV-1.3 | p.11, §1.2 | "The clinical reality of OCT follow-up imposes three properties …": add that **GA's growth rate is highly variable**, which is why forecasting tools are needed at all | 1.23 (open: personified), 1.14 (open: variability claim does not follow) | Fold into the problem statement (also SV-A3). |
| SV-1.4 | p.12, §1.3 | Long GA paragraph (Yehoshua sqrt-area, quasi-static interior, anisotropic growth, Singh): "a lot of GA information" belongs in the background; terms used before definition | 1.31, 1.32, 1.33, 1.34 (open); S16 (biological vs grid anisotropy) | Moves with SV-X3. While moving, fix S16: the reach result rests on the 21:1 pixel spacing, not on the biological direction of growth. |
| SV-1.5 | p.12, §1.3 | "The setup — how elapsed time enters …, how models are trained and evaluated — is fixed once, and the operator is the only part that changes. Architectures … on equal terms.": restructure, easier to read | 1.37 (open, em-dash tricolon), 1.39, 1.42 (open: same split stated 3×) | AI suggestion available. |
| SV-1.6 | p.13, §1.3 contributions | "Δt-conditioned": check the literature; time conditioning can be listed as a contribution, but double-check | 1.40 (open: "What the thesis delivers …") | Literature check needed: Δt-conditioned residual updates exist (MP-PDE's Δt input, Neural ODEs, time-conditioned operators; GA-specific prior work?). Then decide the claim and its wording. |
| SV-1.7 | p.13 | Research question terms (X1, X2) | | See §0. |

## 3. Chapter 2 Background (pp. 14–28)

| # | Page | Supervisor | AI match (status) | Notes |
|---|---|---|---|---|
| SV-2.1 | p.14, §2.1.1 | Heading "A short anatomy primer" → **"Eye anatomy" / "Eye physiology"** | 2a.3 (open: "biological camera") | Trivial once the X3 structure is fixed. |
| SV-2.2 | p.16, §2.1.2 | **Section order:** 1. eye anatomy, 2. diagnostics and imaging (OCT etc.), 3. GA and its pathophysiology | R4 (retina defined 3×), 2a.9 (open), 2a.1 (open, roadmap), T1 | Swap §2.1.2 and §2.1.3. |
| SV-2.3 | p.16, §2.1.2 | The GA section opens by defining the retina again; anatomy/imaging/pathology are intermixed across the background. Introduce normal anatomy with a schematic (third-party images allowed if the licence permits and they are cited), then imaging, then pathology. | R4, 2a.9, 2a.10 (open), Figure TODOs `fig:bg:eye-anatomy`, `fig:bg:retinal-anatomy` | Licensed third-party figures would close the figure TODOs that need illustrations. |
| SV-2.4 | p.16, §2.1.2 | "What this end-stage lesion looks like on OCT has been formalised by … CAM": wording can be improved | 2a.12 (open, pseudo-cleft) | AI suggestion available. |
| SV-2.5 | p.20, §2.1.5 | §2.1.5 "The eleven-channel state representation" **and §2.1.6 (the cohort) belong in the Data chapter** | R2 (cohort facts twice), R1 (crop census 4×), R3 (layer definition 4×), T3, 2a.29–2a.38 (open) | Move and de-duplicate against §3.1–§3.3; removes R1/R2/R3 repeats at once. |
| SV-2.6 | p.25, §2.2.5 | Merge with §1.3, place at the end next to motivation | S17/T8 | = SV-X4. |
| SV-2.7 | p.27, §2.4 | **Related Work too compact:** expand with dedicated subsections per topic; the reader should see the subject was studied deeply | 2b.39–2b.46 (open); NOTES open TODO "neural PDE solvers in biomedical problems" | Needs literature work: GA progression models (clinical + DL), DL on OCT/FAF, neural PDE solvers / operator learning, (bio)medical applications of neural solvers, U-Net/FNO/FEN origins. |

## 4. Chapter 3 Data (pp. 29–34)

| # | Page | Supervisor | AI match (status) | Notes |
|---|---|---|---|---|
| SV-3.1 | p.29, §3.1 | On "Mai et al. (2024), who describe a larger GA cohort from the same MUW clinic …": **"yours is the same cohort with tighter registration bounds and cleaner segmentations"** | 3.2 (open: "it" ambiguous), 3.6 (open: repeated relative clause) | **Answers the open NOTES TODO** (§2.4 "confirm how the 75-eye cohort relates to the 184-eye cohort of Mai") and the device question: the cohort is a subset of Mai's, so the Spectralis device applies. Update §2.4, §3.1, §5.6.1, §6.2, Ch. 7 ("a larger cohort of the same clinic" everywhere). |
| SV-3.2 | p.30, §3.1 | Strike-out (no comment) on "The data agree with this:" (start of the IoU sentence: OCT mask = SLO mask through the transform, IoU …) | 3.7 (open: "data agree", vague) | Strike covers about one line; unclear whether only the phrase or the whole IoU sentence should go. Ask, or drop the phrase and keep the fact. |
| SV-3.3 | p.30, §3.1 | "0.12118 mm between B-scans …": **use microns** | 3.9 (open: "gold-standard") | 121.18 µm, 5.68 µm, 3.867 µm. Decide whether µm applies thesis-wide (spacings) while lesion sizes stay in mm. |
| SV-3.4 | p.31, §3.2 | Layer channels: cite the **layer segmentation** (Iowa Reference Algorithms, https://iibi.uiowa.edu/oct-reference) | 3.13 (open) | Partly answers the open TODO on layer provenance; boundary names may follow from the Iowa algorithm's surface list (to confirm). Needs bib entries (Iowa reference algorithm papers, e.g. Garvin et al. 2009 / Abràmoff et al. 2010). |
| SV-3.5 | p.34, §3.7 | Fold table: **report patients / eyes** per fold | 3.34, 3.36 (open) | Add patient counts per fold to Table 3.x. Data from the split files (code repo). |

## 5. AI-review items in Ch. 1–3 that the supervisor did not mark

Open after the supervisor's points are done, unless a restructure removes the passage. Medium
items worth doing in the same pass (all `open`): 1.12, 1.15, 1.21, 1.24, 1.29, 1.30, 1.36, 1.38
(Ch. 1); 2a.2, 2a.4, 2a.8 (Fig. 2.2 caption maps strata onto channels), 2a.14, 2a.15, 2a.18
(Fig. 2.3 caption says "projected intensity"), 2a.20 (A-scan undefined), 2a.22, 2a.23 (wrong
pointer), 2a.25, 2a.27, 2a.36, 2a.37 (§2.1); 2b.10 ("reach" never defined), 2b.11, 2b.14, 2b.15,
2b.18, 2b.19, 2b.28, 2b.31, 2b.34, 2b.36, 2b.38 (§2.2–2.4); 3.5, 3.6, 3.8 ("not uniform"),
3.10, 3.14, 3.19 (censored / anchor undefined), 3.21, 3.24 ("canonical fold" undefined),
3.28, 3.29, 3.31, 3.32 (Ch. 3). Low items: polish, take as we pass.

## 6. Chapters 4–7, appendices

No supervisor marks. AI review still open there (219 medium total across the thesis, minus Ch. 1–3).
Ask whether the supervisor's review continues; if not, work through the AI items after Ch. 1–3.
