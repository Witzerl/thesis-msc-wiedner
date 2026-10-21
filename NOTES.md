# NOTES

Single source of truth for open TODOs, supervisor feedback, pending numbers, and unresolved citations. Mirror every `% TODO:` left in the LaTeX as an entry here.

## Code-side architecture & results sync (2026-09-17) — CURRENT

Re-synced from the code repository (`masterthesis-docker`, `HEAD e3d2df7`) after a gap of
roughly seven weeks in the thesis repo. **This section supersedes the 2026-07-26 sync
below, which is retained only as a record of what was believed at that time.** Most of
the 2026-07-26 items are themselves now out of date — read them as history, not as
instructions.

### What was mirrored on this date

- `PROJECT_CONTEXT.md` — re-mirrored in full (13 KB → ~70 KB). It now opens with a §0
  that states the project's question and how the document is organised, and carries a
  measured-effect table for every ingredient.
- `THESIS_FRAMEWORK.md` — **new mirror** (~280 KB), from
  `masterthesis-docker/GraphPDE/demos & explanations/THESIS_FRAMEWORK.md`. This is the
  technical source of truth for Chapters 3–5: data (§1), preprocessing (§2), DMM (§3),
  the graph backbone (§4), the rest of the backbone family (§4b), the dual-branch
  composition (§5), training (§6), evaluation and the **thesis-bound results table with
  instruments and caveats (§7.5)**, reproducibility (§8), the chronology of load-bearing
  fixes (§9), refuted ideas kept as citable negative results (§9.3), open items the
  thesis must state honestly (§9.4), and the reference list (§10). It is deliberately not
  `@`-auto-loaded; read the relevant `§` on demand.
- `CLAUDE.md` — project framing updated (see next block).
- Not mirrored (too large, and indexed by the two above): the code repo's own `NOTES.md`
  (813 KB), `SOLVER_FINAL_RUNS.md` (435 KB, the dated run readouts), `ARCHITECTURE.md`
  (decision → code map), `EXPERIMENTS.md` (run infrastructure), `DMM_GA_DESIGN.md`,
  `DMM_HPSEARCH_NATIVE.md`, `COHORT_VISITS.md`, `solver_results.csv`. Read them in place
  when a number needs its full provenance.

### The framing changed — this is the big one

The project no longer asks "can MP-PDE / MM-PDE be adapted to GA?". It asks **"what does
a model need in order to predict GA progression, and what framework does it need to sit
in?"**. The adaptation is still the largest block of engineering, but what it produced is
a **fixed experimental framework with one swappable operator slot**, and the thesis
reports a controlled survey through that slot.

- **Fixed for every arm** (this is the framework, and the part that demonstrably
  transfers): one visit in, no history; 11-channel state on the 49×1024 en-face grid; a
  $\Delta t$-conditioned autoregressive residual operator $u_{t+\Delta t} = u_t + \Delta t
  \cdot f_\theta$ on all channels with a **zero-initialised head so every model starts at
  exact persistence**; the time-budgeted pushforward curriculum; the channel-weighted MSE
  + soft-Dice objective; per-module gradient clipping; identical optimiser, epoch budget,
  folds, seeds, evaluation, model selection and replicate floor.
- **Variable**: $f_\theta$ only, via `--backbone` (+ optional `--integrator`). Nine
  settings across six architecture classes: k-NN GNN, dilated-stencil GNN (**the locked
  model**), U-Net at two capacities, FNO, FNO + 3×3 local bypass, graph U-Net, Finite
  Element Network (free-form and with a learned transport term), RK4 wrapper over any of
  them, and a per-pixel floor with no spatial context. Parameter-matched to within
  **1.25×** of the locked model's 67,147, except two deliberate controls (the 44×-capacity
  U-Net and the 0.22× per-pixel floor).
- **Headline**: the framework transfers and **the architecture class does not decide the
  outcome**. Dilated-stencil GNN 0.5258, param-matched U-Net 0.5046, T-FEN 0.5337 are
  statistically indistinguishable at the available precision; a per-pixel model with no
  spatial context is bit-exactly persistence (0.0000). What separates arms is which
  *ingredients* they carry.

### Measured ingredients (all change-region Dice@360d, late-epoch mean, 5-fold)

Established:

- **Spatial context at all** — 0 message-passing layers = 0.0000 (exactly persistence)
  vs 0.4529 for one ring. Required, trivially.
- **Physical reach at lesion scale (~0.12 mm/hop)** — **+0.074 ± 0.008 SE, 5/5 folds,
  74/75 eyes**, replicated at a second seed, at **0.89× the parameters**, by changing only
  `data.edge_index` (dilated stencil: rows ±1 × columns {0, ±7, ±14, ±21}). The largest
  effect in the project (T7i/T7j).
- **Global context *and* local detail together** — a global-only FNO sits *below* the
  U-Net; +800 parameters of 3×3 local bypass bring it level and to **+0.047 ± 0.016 over
  the k-NN GNN on 5/5 folds**, the only arm to win every fold (T7c/T7d).
- **An explicit transport (advection) term** — **+0.053 ± 0.007, 5/5 folds**, at both
  seeds (T8f). ⚠️ The only architecture comparison in the project that is **not
  parameter-matched** (68,503 vs 34,785, 1.97×) — that caveat must travel with the number
  every time it is quoted.

Measured nulls (reportable negative results, **not** contributions):

- **Mesh adaptation / the dual branch (the MM-PDE half)** — dual − parameter-matched
  bypass = **−0.0001 ± 0.0060**, the tightest null in the project, at ~10× the wall-clock.
  ⚠️ **Scope it correctly**: α stays shut in the bypass control as well as in the mesh
  arm, so what the gate measured is *the correction branch's failure to optimise*, not
  "mesh adaptation does not transfer to GA". Weight decay is refuted as the cause (T8g).
- **Patient covariates (age, sex)** — T6 reads *in favour of removing them*
  (+0.0198 ± 0.0140 fold-paired, +0.0190 ± 0.0080 per eye) but graduates on neither
  instrument. Defensible claim: no detectable benefit, residual points against.
- **The learned surrogate encoder (LayerEncoder)** — null at every width over an 8× range
  (T5), at 30–55 % more compute.
- **Parameter count** — a 44× U-Net *loses* to the parameter-matched one (T7b).
- **Time-integration order** — RK4 − Euler null over both a local graph operator and a
  global spectral one, at ~4.8× the cost (T8n/T9/T9b).
- **Every GNN-internal knob** — normalisation, aggregation, edge-direction features
  (T7e–T7g). The geometry mattered; the message function did not.
- **The intermediate-time-point regulariser** — evaluated and removed 2026-06-11.

### Vocabulary rules that now bind the writing

- **No "ODE", "rate field" or "learned dynamics" language for the locked model or any
  headline result.** The solver-swap diagnostic (T10, 2026-09-17) has the locked model
  *failing* (Dice spread 0.0856 under refined inference schemes) and only the
  autonomous-RK4 arm passing (0.0044) — and that arm is a 5-fold null on accuracy at
  ~4.8× the cost. The ODE property is real, obtainable, and worth nothing on this task.
- **Never quote raw RMSE across arms.** The dense arms decalibrate far more under
  autoregression than the GNN does; raw-scale comparisons measure the decalibration.
- **Quote cost as the minimum epoch time of the cheapest fold, and name the fold**
  (`curve_sec_per_epoch_min`); the mean carries a near-constant additive overhead that
  penalises cheap architectures. The GPU co-scheduling explanation for the spread is
  **refuted** (2026-09-17 audit); the procedure stands for other reasons.
- **Compare within an era** — pre-fix runs are not comparable; dual-branch runs before the
  2026-08-06 edge fix are void.
- **Two instruments, always quoted together**: fold-paired 5-fold mean ± between-fold SE
  (threshold 0.016; single fold 0.036) and the pooled per-eye test over 75 eyes. A result
  graduates only when both agree. Replicate noise floor **±0.0127**.
- **The @360d metric has no upper horizon bound** (7/75 eyes scored at 450–720 d), and the
  evaluation protocol is 5-fold train/val CV — **the "test" split is structurally empty**.
  Both must be stated honestly.
- **The 49×1024 crop is not lossless and the old justification is false as measured.** It
  cuts real lesion area in 27.3 % of visits and 31.1 % of cropped lesions touch the crop
  border, with growth across it censored and unflagged. The earlier rationale ("99 % of GA
  is central, the periphery is clinically irrelevant") **must not reach the thesis text**.
  ⚠️ This contradicts the constraint currently written into `THESIS_STRUCTURE.md` §3.3.
- **GA is *not* monotonic growth.** The explicit monotonic penalty is 0.0 since the
  2026-08-15 loss lock and the residual form is signed. Ground-truth shrinkage should be
  quantified and discussed (segmentation noise vs biology).
- The cohort-wide validity of the single `SPACING_MM` constant is **unverified** (~2 %
  deviation, needs DICOM). Every mm² figure inherits it — state it as an assumption.
- The **anatomical names of the 10 layer boundaries are still not recorded** in the code
  repo; they must come from the MUW segmentation pipeline.

### Committed thesis prose that is now WRONG

- [ ] TODO (⚠️): `01-introduction.tex` §1.4 Contributions — **three of the six bullets are
  now measured nulls** (multi-channel Frobenius monitor: superseded design *and* the mesh
  itself is a null; patient covariate conditioning: null; surrogate equation encoder:
  null), and the sixth bullet describes an experimental plan (persistence vs single-branch
  vs dual-branch) that has been overtaken by the nine-arm survey. The whole list needs
  rewriting against the new framing: the framework, the reach/transport findings, and the
  nulls reported as negative results.
- [ ] TODO (⚠️): `01-introduction.tex` §1.3 "Why neural PDE solvers" and the locked-in
  research-question blockquote at its end — the question has changed (see above). Re-read
  and re-frame.
  - [x] 2026-09-25: research question rewritten (user-approved wording): "What is needed
    to forecast the progression of GA from longitudinal OCT?" with two sub-questions —
    (1) what kind of framework, (2) what kind of operator — plus a short follow-up that
    maps them to Chapters 4 and 5.
  - [x] 2026-09-25: the paragraph leading into it ("Two recent neural PDE solver
    families…") replaced by two general paragraphs (user-approved): neural PDE solvers
    as learned operators that differ in their built-in assumptions, then the turn to a
    fixed setup with the operator as the only varying part. No architecture is named.
    The provenance sentence (the work began as an adaptation of the two graph solvers,
    suggested by the clinical partner) was deliberately left out here; place it in §1.4
    or at the start of Chapter 4.

### Author's tablet review of Chapters 1–2 (2026-09-25)

Handwritten review of thesis pp. 1–14 (build of 2026-09-22), decoded from the Samsung
Notes export. Legend: blue highlight = "do not like the sentence", red pen = "something
wrong / to change". The author asked for no shortening yet; cuts wait for a later pass.

- [ ] Author decision (2026-09-25): **everything MM-PDE moves to the appendix** as an
  additional experiment — the mesh mover (DMM), the dual branch, the α-gate result and the
  mesh-quality study. Affects §2.5, §4.5, §5.4 (mesh null) and §5.5.
  2026-09-25: `THESIS_STRUCTURE.md` updated (Framing revision, §2.5/§4.5/§5.5 marked as moved,
  new Appendix G), plus short notes in `CLAUDE.md` and `README.md`. The mirrors
  (`PROJECT_CONTEXT.md`, `THESIS_FRAMEWORK.md`) are code-side and untouched. **Still open:**
  moving the drafted `02-background.tex` §2.5 text into `91-appendix.tex`. (Done 2026-09-26,
  review #22; §4.5 and §5.5 still to move.)
- [x] §1.1: split the first sentence after "industrialised countries". Done 2026-09-25.
- [x] §1.1: "Crucially, AMD is not classified as avoidable…" — author clarified: keep the
  content, fix the construction. Rewritten 2026-09-25 (avoidable-cause list checked against
  the Flaxman PDF: cataract, refractive error, trachoma, glaucoma, diabetic retinopathy,
  corneal opacity).
- [x] §1.1: "The combination of an aging population…" — too long, too complicated. Rewritten 2026-09-25 as two sentences.
- [x] §1.2: "This per-eye, spatially resolved framing…" — simplify. Rewritten 2026-09-25.
- [x] §1.2: "A standard U-Net or similar dense predictor…" — marked, no comment; it
  conflicts with the result that a U-Net inside the framework matches the locked GNN.
  Rewritten 2026-09-25: the paragraph now argues that elapsed time and visit-to-visit
  rollout must come from a framework around the model (which borrows techniques from
  neural PDE solvers); the model choice is left as a separate question. The Ronneberger2015
  cite marker went with the removed U-Net sentence.
- [x] (2026-09-25: covariates reframed as an open question tested in the thesis; opening now
  "properties … that a model has to deal with"; mask says "GA lesion", not cRORA) §1.2 "three properties" paragraph (not marked by the author): the covariate
  requirement ("should enter the dynamics on equal footing") contradicts the measured
  covariate null, and the claim that both mask and layers are *required* is not shown
  by the results. Revisit.
- [x] §1.3: "Two recent neural PDE solver families…" — too much focus on MP-PDE/MM-PDE.
  Rewritten 2026-09-25.
- [x] (2026-10-01: merged into §1.3) §1.4 Contributions — "might remove"; decide between rewriting and removing.
  2026-09-25: headline now reads "Contributions (TODO: maybe remove)" as a visible marker;
  the bullets themselves are still the stale pre-survey list.
- [x] §1.5 Outline — "the two specific architectures (MP-PDE, MM-PDE)" marked; rewrite.
  Rewritten 2026-09-25: no framework names, no mesh content; Chapters 4 and 5 are tied to
  the two parts of the research question; the moving mesh is pointed to the appendix.
- [x] §2.1.3 "Two acquisition platforms…" — drop the SD/SS-OCT description; reword the
  OCT-vs-FAF argument.
  Done 2026-09-25. With the SD-OCT/SS-OCT definitions gone, "SD-OCT volume" in §2.1.4
  became "OCT volume" and "SS-OCT" in §2.1.6 was spelled out.
- [x] §2.1.4 "Two construction strategies…" — not needed (data come as en-face derivatives). Replaced 2026-09-25 by a two-sentence version.
- [x] End of §2.1.4 — add a short summary of what OCT is, what en-face is, what is used.
  Done 2026-09-25 in place, not as a separate paragraph: en-face defined where introduced
  (§2.1.4 opening), "what the thesis receives" stated after the projection sentence, and the
  last paragraph of §2.1.3 opens with the two pieces of information used. "graph-neural-network
  architectures" -> "models".
- [x] (2026-10-19: confirmed by the supervisor, review 2 SV-6.7) ⚠️ FACT CHECK (2026-09-25, Mai et al. 2024, PMC11000109): in the Mai study of the MUW
  cohort the GA reference was annotated **on FAF** by certified Vienna Reading Center readers
  ("well-demarcated areas with a significantly decreased or extinguished degree of
  autofluorescence"), then registered automatically to the near-infrared image aligned with
  the OCT, giving 2-D en-face OCT annotations. The repo is consistent with this: `mask_oct`
  equals the SLO/FAF-frame `mask_global` sampled through `T_mask` (IoU ~1.0 on all 553 visits).
  So channel 0 is most likely a FAF-based annotation transferred to the OCT grid, NOT an
  OCT/cRORA segmentation. Wrong as written: §1.2 "binary lesion mask captures the cRORA region",
  §2.1.3 "Both pieces of information … can be read from a single OCT acquisition" and "The data
  … are therefore OCT-derived", §2.1.5 mask defined via CAM cRORA criteria. Mai confirms
  Spectralis SD-OCT; Mai says nothing about layer segmentation (provenance still open).
  Caveat: that the repo data are exactly Mai's annotations is an inference, not a record.
  2026-09-25: §2.1.3 fixed neutrally (author: keep the FAF provenance out of the Background):
  "The thesis therefore works on the OCT en-face grid." and "A single OCT volume shows both the
  lesion and the retinal layers around it." §1.2 cRORA claim fixed 2026-09-25 ("captures the GA
  lesion itself"). Still to fix: §2.1.5 CAM/cRORA
  mask definition; add the provenance as a plain dataset fact in §3.1.
  2026-10-01 (later): §3.1 provenance paragraph added (hedged, TODO to confirm) and the §2.1.2
  "cRORA endpoint" sentence fixed; 2.1.5 comment reduced to the layer provenance. Item done
  apart from the supervisor confirmation.
  2026-10-01 status: §2.1.5 done (2026-09-25). Still open: §3.1 provenance sentence; and a
  further instance found while merging prompts/open.txt -- §2.1.2 "The thesis state tensor
  encodes only the cRORA endpoint, as channel~0" (02-background l. ~215). Overview of this
  session's leftovers: prompts/open.txt section 12 [r25].
- [x] §2.1.5 "Two technical caveats…" — not needed (cut, later pass); also removes an
  SD-OCT claim. The preceding sentence naming the layer strata claims more than is known.
  Done 2026-09-25 (author approved the cut): caveats paragraph deleted; mask defined neutrally
  (binary, one inside the GA lesion, aligned with the layer grid — no CAM/cRORA claim); the
  layer-strata list replaced by "ordered from the most superficial to the deepest (§3.2)",
  since the boundary names are not recorded. The "again in §6.3" promise went with it.
- [x] §2.1.6 "SD-OCT" (twice) — only the vendor is recorded; state the device once with
  the Mai et al. (2024) caveat. Done 2026-09-25: device stated once, sourced to Mai et al. (2024)
  (plain-text citation + `% TODO: cite Mai2024` marker).
  Update: Mai et al. (2024) state "Spectral-domain (SD)-OCT … (Spectralis, Heidelberg
  Engineering)" for the MUW cohort, so SD-OCT is supported by a citable source.
- [x] (done 2026-09-25) TODO (⚠️): `01-introduction.tex` §1.5 outline — describes a Method chapter built
  around MP-PDE vs MM-PDE; will need to follow whatever restructure is agreed.
- [x] 2026-09-17: `THESIS_STRUCTURE.md` §3.3 corrected. The old constraint told the writer to
  "justify the 6×6 mm window by citing that 99 % of GA pathology occurs within a central 3 mm
  radius" — **false as measured**. It now carries the censoring census (27.3 % of visits lose
  real lesion area, 31.1 % of cropped lesions touch the border) and the deliberate-trade-off
  framing, with an explicit instruction that the old rationale must not appear.
- [ ] TODO (⚠️): `04-method.tex` placeholders (THESIS_STRUCTURE.md corrected 2026-09-17)
  still name the "Frobenius-norm monitor function for vector-valued state" and the
  "multi-channel res_cut Conv2d". Both are gone from the framework (the monitor is a plain
  scalar monitor on the blurred mask, trained on the **native OCT grid** since 2026-08-04
  — the SLO-256² path is itself now historical; `res_cut` was cut entirely).
- [x] 2026-09-17: `THESIS_STRUCTURE.md` Chapters 4 and 5 **restructured** (user-approved). They
  had assumed a two-architecture thesis (4.5 single-branch MP-PDE, 4.6 dual-branch MM-PDE;
  5.2 three baselines). Ch 4 is now 4.1 overview / 4.2 the fixed framework / 4.3 Backbone I
  (the graph solver, with graph construction as the load-bearing part) / 4.4 Backbone II (the
  countermodel family + parameter matching) / 4.5 the moving mesh as a tested hypothesis /
  4.6 conditioning / 4.7 training / 4.8 implementation. Ch 5 is now 5.1 protocol / 5.2 arm
  table / 5.3 ingredient study / 5.4 negative results / 5.5 mesh quality / 5.6 validity
  diagnostics / 5.7 qualitative + Mai comparison / 5.8 cost. A Framing block was added at the
  top of the document, and §1.4, §2.3, §3.1, §3.7, Ch 6, Ch 7 and the appendices were updated
  to match. The chapter .tex files have **not** been touched.
- [x] 2026-09-17: `02-background.tex` §2.1–§2.2 (drafted 2026-05-02, uncommitted since)
  committed together with the new §2.1.6 corrections and the §2.3–§2.6 drafts.

### Author's tablet review of §2.2–§3.4 (2026-09-26)

- [x] 2026-09-26 bibliography pass: every reference cited in Chapters 1–4 and Appendix G is now
  in `references.bib` (63 entries) and cited with `\citep`/`\citet`; each entry was checked
  against the publisher record or the verified list in THESIS_FRAMEWORK.md §10.1. Corrections
  made on the way: §1.2 "predicts when an eye will convert" now cites Schmidt-Erfurth (2018)
  next to Vogl (2021) — Bogunović (2017) predicts drusen regression, so it is cited only in
  §2.5; the cRORA criteria in §2.1.2 now cite the primary source Sadda (2018) next to Vallino;
  the opening sentence of §1.1 now cites Wong (2014). Only Huang1991 remains uncited.
- [x] (author 2026-09-26: "it's fine", Vogl2021 stays) TODO: §1.2 cites Vogl (2021) for "earlier deep-learning work on AMD, which predicts when
  an eye will convert to a later disease stage". Vogl (2021) is a topographic GA progression
  analysis, not a conversion model; check whether it belongs in that sentence.
- [x] 2026-09-26: repaired six broken `\ref` commands in the §1.5 outline (committed in
  1280281): the backslash had been turned into a carriage return, so the PDF read "Chapter
  efch:background". Cause: a scripted edit whose "\\r" collapsed to a carriage return. All
  .tex files were scanned; no other occurrence.


Second handwritten review (build of 2026-09-26, thesis pp. 13–27), decoded from
`main-thesis_v2_260926_163353.sdocx`: 33 marks. Blue = rewrite, red = wrong/remove.
Being worked through one item at a time.

- [x] #1–#3 §2.2 intro: needs more introduction ("this section feels lost"); first sentence
  disliked; "The notation follows Brandstetter" to be removed. Done 2026-09-26: new opening
  (author's choice of three drafts) states that the approach treats GA progression as a solver
  treats a PDE and that Chapters 4–5 need only these mechanisms, then a per-subsection roadmap.
- [x] #4 §2.2 "Because F depends only on u and its spatial derivatives at x…" — "Is this the
  traditional approach to formulating a PDE?" Done 2026-09-26: the form is standard; the
  sentence now states locality as a property of derivatives and links it to the stencils.
- [x] #5 §2.2.1 line break after the ";" of the grid notation. Done 2026-09-26 (`\newline`;
  a first attempt as a display equation was reverted at the author's request).
- [x] #6 §2.2.1 Brandstetter citation after the grid notation removed (2026-09-26).
- [x] #7 heading → "Finite differences and finite volumes." (2026-09-26).
- [x] #8 FVM sentence: Brandstetter replaced by LeVeque (2002); FDM sentence gets LeVeque (2007)
  (2026-09-26, placeholder + `% TODO: cite`).
- [x] #10 WENO: Brandstetter → Liu et al. (1994) + Jiang & Shu (1996) (2026-09-26).
- [x] #11 the general "this chapter always quotes Brandstetter" comment — addressed item by
  item (#6, #8, #10, #12, #13, #14).
- [x] #12 pseudospectral: Brandstetter → Gottlieb & Orszag (1977) + Trefethen (2000)
  (2026-09-26).
- [x] #13 consistency limit "certainly not in this paper" — checked: it IS in MP-PDE p.5
  (citing Arnold 2015). Author: keep the Brandstetter citation (2026-09-26).
- [x] #14 "splitter" quote — checked against MP-PDE p.1: the paper says "field of numerical
  methods", attributed to Bartels (2016). Sentence rewritten with the correct wording and
  "Following Bartels (2016), Brandstetter et al. (2022)…" (2026-09-26).
- [x] (original entry for #6, #8, #10–#14) Brandstetter over-citation across §2.2 ("the methods
  are not described in that paper, some don't need a citation"); #13 the consistency limit is
  "certainly not in this paper"; #14 look up the exact "splitter field" quote. All resolved
  2026-09-26, see the items above.
- [x] #7 "Finite differences" heading → "Finite differences and FVM" (done, see above).
- [x] #9 add a short FEM paragraph (part of the hybrid / FEN arm). Done 2026-09-26: new
  "Finite elements." paragraph in §2.2.1 (weak form, local coupling via shared elements,
  pointer to the FENs of §2.3); cites Courant (1943) and Langtangen & Mardal (2019).
- [x] #15 §2.3 remove "in the graph-network literature". Done 2026-09-26.
- [x] #16 §2.3 remove the Graph U-Nets (Gao & Ji) sentence — "not used, no?" Done 2026-09-26
  (sentence and its Gao2019 marker removed from §2.3). Author: the graph U-Net arm "was more
  of a test than serious" and showed nothing significant.
- [x] (2026-09-26: author decided the arm stays in Chapter 4 for now) TODO (follow-up to #16, decision needed): the graph U-Net arm is still a full arm in
  `04-method.tex` (overview list l.41, l.492/502/530, own subsection §4.4.3 "The Graph U-Net
  and the Locality Floors" with the Gao & Ji disambiguation, parameter table l.911) and in the
  project framing ("nine settings, six architecture classes"). Decide whether to keep it as
  a reported arm, demote it (e.g. to an appendix row), or drop it; the counts in CLAUDE.md /
  THESIS_STRUCTURE.md / Ch. 1 would change with it. Gao2019 is now needed only in §4.4.3.
- [x] #17 §2.4 remove "original"; #18 WENO5 layer mapping — quote the methods. Done
  2026-09-26: "original" removed; claim verified against MP-PDE p.6 ("1 layer for FDM, 2 layers
  for FVM, and 3 layers for WENO"), sentence otherwise kept as is at the author's request.
- [x] #19 §2.4 "In this paper, two distinct mechanisms…"; #20 "detailed in the next section"
  → appendix; #21 "variable Δt rather than t". Done 2026-09-26: "In MP-PDE, two distinct
  mechanisms…"; "…treated as an additional experiment in Appendix~G" (plain text);
  "…on a variable Δt rather than on the absolute time t".
- [x] TODO: §2.4 refers to "Appendix~G" in plain text (inline `% TODO`); switch to `\ref` once
  the MM-PDE appendix and its label exist (together with #22). Done: `\ref{app:mm-pde}`.
- [x] #22 §2.5 MM-PDE → Appendix G. Done 2026-09-26: the whole former §2.5 moved verbatim to
  `91-appendix.tex` as Appendix G "The Moving-Mesh Extension (MM-PDE)" (`app:mm-pde`),
  section G.1 "Background: MM-PDE" (`app:mm-pde:background`); Related Work is now §2.5. The
  closing sentence about "how a monitor function should be defined over a multi-channel
  state tensor … deferred to Chapter 4" was dropped (superseded design: the monitor is a
  scalar on the blurred mask) and replaced by "…is the question this appendix tests."
- [x] 2026-10-01: Appendix G G.2-G.4 written (external draft from prompts/PROMPT_appendix_G.md,
  audited against THESIS_FRAMEWORK.md §3, §5, §6.3, §7.5 and DMM_HPSEARCH_NATIVE.md). Corrections:
  build-breaking paste damage (row ends, lost \, before units, unescaped _ and % in 	exttt);
  "Adam \citep{Loshchilov2019}" (the DMM used plain Adam; AdamW cite kept for ItpNet only);
  "the lower boundary weight failed a lesion-specificity check" (it was a tie on the biased pool);
  ItpNet pretraining described as an identity "on the uniform grid" (it is the round trip).
  Added from the fact sheet: the era sentence (mean+max k-NN 0.4515, not the 0.4623 arm), per-eye
  values, "tightest null", ReZero author-year, the 2026-08-06 edge fix, v2 parameter counts,
  pool definitions, the probe explanation and the fold-2 probe details. Added from the sources:
  the L-BFGS refinement was not used; the GA monitor is scalar and log-compressed (unlike G.1).
- [ ] TODO (Appendix G): cite **Bachlechner2021** (ReZero, UAI 2021) -- `% TODO: cite` marker in G.2.2.
- [ ] TODO (Appendix G): produce Figure `fig:appendix:moved-mesh` (moved mesh over the GA mask,
  2-3 eyes, physical aspect ratio, uniform grid alongside).
- [x] (superseded 2026-10-19 by the rewrite below) Author to review Appendix G (G.1 was not
  touched; it still contains "Crucially" and "entirely", and describes the original paper's
  matrix monitor).
- [x] 2026-10-19 **Appendix G rewritten in the style of the revised main chapters** (author: so that
  it can move into the main text with little rework, cf. SV-4.2). Chapter opener with a map of the
  sections; every section opens with its purpose and closes with what follows; G.1 uses the thesis
  notation (update operator, interpolation, monitor constant written alpha_M so it does not clash with
  the gate alpha); "encoder" named as the DeepONet branch network; "the gate opens / stays shut"
  defined at first use; G.3 results split into mesh validity and mesh quality; G.4 reordered
  (pre-registered reading -> the bypass control removes it -> the narrower statement -> contrast with
  Hu et al.) with the fold-2 probe scope stated. No LLM patterns ("not X but Y", "Crucially",
  "entirely"). All tables, figures, labels and numbers unchanged (checked number by number against
  the previous version); builds clean. Remaining AI-review items of Appendix G (G.1-G.9 partly
  addressed) are covered by the rewrite.
  Ledger: Hu2024 C181, C182, C184, C185 checked by hand (quotes pass verify_quotes on their pages),
  C192, C193 re-checked (same claim); HuangRussell2011 C183, C191 stay PENDING (book not on disk).
- [ ] Author to review the rewritten Appendix G (inline `% TODO (author review)` at its start).
- [x] (superseded by the entry above) TODO: Appendix G still needs the rest of its content (inline `% TODO` at its end): DMM
  for GA, dual branch + α gate, the null result with its scope, mesh-quality study, ~10×
  cost. Chapters 4 and 5 still contain the MM-PDE sections to be moved ("The Moving-Mesh
  Extension as a Tested Hypothesis" §4.5, "Moving Mesh Quality" §5.5).
- [x] #23 §2.5 related work: add related work for all other surveyed methods. Done 2026-09-26
  (after first being postponed): one paragraph naming the original source of every method in
  the operator slot, pointing to §4.4. Previously postponed
  2026-09-26; inline `% TODO` placed at the end of Related Work (U-Net, FNO + hybrid, FENs,
  RK / Neural-ODE). Needs a literature search first.
- [x] #24–#26 §3.1 remove "HRF SPEC"/device-model sentences, the Spectralis-inference sentence
  ("useless information"), and the 100-identifier / 49-without-data sentences. Done
  2026-09-26: the Mai et al. (2024) Spectralis sentence and the device-model TODO are kept;
  the patient paragraph now opens "The 75 eyes come from 51 patients: …".
- [x] (2026-09-26: author wants no more than "75 eyes from 51 patients"; §3.7 text, Table 3.3
  caption and the test-split paragraph no longer mention the 100-identifier universe) TODO (follow-up to #26): §3.7 still explains the split over "the universe of 100 patient
  identifiers", 80/20 per fold, and "Only 51 of the 100 patients have scans". That is where
  the uneven per-fold eye counts come from, so it may be needed there; author to decide
  whether it stays in §3.7.
- [x] #27 §3.1 remove the constant-spacing-assumption paragraph. Done 2026-09-26; the DICOM
  TODO comment is kept. §3.1 still says spacing is "treated as" constant; the ~2 % check is
  still stated in §2.1.6 (02-background.tex ~l.484) and belongs in §6.3 Limitations.
- [x] #28 §3.2 channel-order paragraph removed (2026-09-26).
- [x] #29 §3.2 replace the 496-pixel explanation with a plain statement of the −14…499 range.
  Done 2026-09-26 (option B): "…range from −14 to 499 axial pixels, where 0 is the top of the
  scan volume and 496 its nominal depth."
- [x] #31 §3.3 "21.335 times larger" set in bold (2026-09-26).
- [x] #30 §3.2 mean-depth / anatomical-names paragraph removed (2026-09-26); the TODO comment
  on the boundary names is kept.
- [x] #31 §3.3 bold "21.335 times larger"; #32 forward reference for pad positions excluded
  from the loss; #33 add an outlook TODO: find better cropping pre-processing. All done
  2026-09-26: #32 points to §4.7 (`sec:method:training`), #33 is a `% TODO` in §6.4.
- [x] (2026-09-27: §4.5.1 describes the option and states it is off in every reported run) TODO (from #32): §4.7 Training (still unwritten) must describe the optional pad-position
  loss masking (`--exclude_pad_nodes`) and state whether any reported run uses it, since
  §3.3 now points there (inline `% TODO` in 03-data.tex).
- [x] (resolved in ce6bf3e: §6.4 "Spatial pre-processing"; the author check of its wording is in prompts/open.txt section 5) TODO (from #33): §6.4 Future Work — find a better cropping / spatial pre-processing than
  the fixed 49×1024 centre crop (inline `% TODO` in 06-discussion.tex).

### Author's tablet review of §3.4–§4.3 (2026-09-27)

Third handwritten review (build of 2026-09-26, thesis pp. 25–32), decoded from
`main-thesis_v3_260927_145104.sdocx`: 19 marks. Blue = rewrite, red = wrong/remove.
Being worked through one item at a time.

- [x] #1 §3.4 min-max scaling to [−1, 1] "kept as an ablation variant" removed (no run uses
  it, nothing was tested with it). Done 2026-09-27.
- [x] #2 §3.4 Table 3.1 (`tab:data:norm-stats`) removed with its reference and fill-in TODO:
  the mask row is already given in the text as mapped values, and the layer rows (raw
  depths in axial px) give the reader nothing. Done 2026-09-27.
- [x] #3 Table 3.1 "is this relevant?" — resolved by #2 (table removed).
- [x] #4 §3.5 clinical-table variables paragraph removed in full, including the pointers to
  §6.4 and §5.4 ("I think this can go"). Done 2026-09-27.
- [x] #5 §4.1 heading "Overview: One Framework, One Swappable Slot" -> "Overview" (2026-09-27).
- [x] #6 §4.1 GNN clause rewritten: "a message-passing graph neural network (GNN) on two
  different neighbourhood graphs (§4.3.2), one of which is the canonical model of this thesis"
  (2026-09-27).
- [x] #7 §4.1 variant explanations (U-Net, FNO, FEN) removed; one sentence "Several of these
  are run in more than one variant (§4.4)" added (2026-09-27).
- [x] #8 §4.1 graph U-Net removed from the list of arms (author: not used). The count
  "Nine settings of the slot, spanning six architecture classes" was dropped rather than
  re-counted: the list itself gave ten settings, and the six classes are never defined in the
  sources (2026-09-27). Follow-up below.
- [x] #9 §4.1 "a hybrid Finite Element Network (FEN)" (2026-09-27).
- [x] Follow-up to #8 (2026-09-27, author: comment out, remove elsewhere): graph U-Net removed from
  the §4.4 intro, the roadmap, the grid-operator input paragraph, the parameter table (row
  commented out) and the §2.5 related-work sentence; its paragraphs in §4.4.3 are commented out
  and the subsection renamed "The Locality Floors" (label unchanged). Gao2019 is now uncited
  (bib entry kept). Counts "nine settings, six classes" removed from CLAUDE.md and
  THESIS_STRUCTURE.md; the code-side mirrors (PROJECT_CONTEXT.md, THESIS_FRAMEWORK.md) still
  carry them and were not touched.
- [x] 2026-09-27: repaired another broken `\ref` in §4.4.6 ("locality ladder of~\S" + line break
  + "ef{…}"), same scripted-edit fault as in §1.5. All .tex files scanned; no other occurrence.
- [x] #10 §4.1 "built rather than imported" replaced: "All operators are described on the same
  terms. Each was taken from the literature and adapted to the same framework: §4.3 describes
  the graph solver adapted from MP-PDE, and §4.4 the remaining architectures." (2026-09-27).
  Author: the graph solver must not be highlighted above the other arms.
- [x] TODO (from #10): §4.3 intro still says the graph solver "is described in more depth than
  the others because this project built it rather than imported it"; to be fixed when §4.3 is
  reviewed (author: later sections deal with this extra highlighting). Resolved 2026-09-27 by
  the restructure below; the sentence is gone.

### Restructure: MP-PDE out of the Background, one Operators section (2026-09-27)

Author decision: the Background holds no method descriptions; all methods are explained in
Chapter 4, and the MP-PDE graph network sits next to the other operators on equal terms (it may
be longer, since it supplies two arms and the floors).
- [x] `02-background.tex`: §2.4 "MP-PDE" deleted. Temporal bundling, the pushforward trick and
  zero stability are now two short paragraphs in §2.3 (after the distribution-shift paragraph;
  author: keep them brief). §2.2.4 keeps MP-PDE only as the learned-stencil example and now
  points to §4.3.2. Related Work is §2.4. Dropped with the section: the unverified bundle
  sizes {20, 25, 50}, the "This thesis keeps …" paragraph (covered by the differences table).
- [x] `04-method.tex`: "Backbone I" and "Backbone II" merged into §4.3 "The Operators"
  (label `sec:method:family`). Order: 4.3.1 Operator Contract (now carries the full
  batch-statistics argument, moved from the GNN normalisation paragraph) → 4.3.2
  Message-Passing Graph Neural Network (`sec:method:mppde`; paragraphs "The original MP-PDE"
  = the former §2.4 text, "The architecture used here" = former §4.3.1, "Differences from the
  original" = former §4.3.3 with its table) → 4.3.3 Graph Construction → 4.3.4 Dense → 4.3.5
  Floors → 4.3.6 FEN → 4.3.7 RK → 4.3.8 Parameter Matching. Removed labels:
  `sec:background:mp-pde`, `sec:method:mppde:arch`, `sec:method:mppde:diff` (no references
  left). "member of the family" / "countermodel" wording replaced by "operator".
- [x] (read back in tablet review v6, 2026-10-02) Author to review Chapter 4 after this restructure (planned).
- [x] 2026-09-27: moving-mesh section (former §4.4, placeholders only) moved to Appendix G as
  G.2 "The Moving-Mesh Extension for GA" with G.2.1 DMM (`app:mm-pde:dmm`) and G.2.2 Dual-Branch
  Composition (`app:mm-pde:dual`). Removed from Chapter 4: the dashed mesh path in the pipeline
  figure, the correction-branch zero-init exception, the moved-mesh k-NN sentence, the
  "Branches" row of the MP-PDE difference table, "single-branch" wording in the contract and the
  RK wrapper, and ItpNet from the §4.5 Training TODO; each is kept as a TODO in Appendix G.
  Chapter 4 now mentions the mesh twice: one pointer sentence in §4.1 and a parenthetical
  Appendix G reference in the MP-PDE limitations paragraph (§4.3.2). Chapter 4 renumbers:
  4.4 Conditioning, 4.5 Training, 4.6 Implementation.
- [x] 2026-09-27: §5.5 "Moving Mesh Quality" (placeholder) moved to Appendix G as G.3
  (`app:mm-pde:mesh-quality`); Chapter 5 renumbers (5.5 Qualitative, 5.6 Cost). The mesh items
  of the §5.4 ablation TODO list were removed.
- [x] 2026-09-27: §4.4 retitled "Conditioning: Patient Covariates"; the "Surrogate Equation
  Encoder" subsection is commented out (author: off in every reported arm, only the T5 ablation,
  a null). It is to become one short paragraph in §4.4. The two references to it (operator
  contract, GNN conditioning vector) now point to §4.4.
- [x] 2026-09-27: §4.4 Conditioning, §4.5 Training and §4.6 Implementation to be drafted by an
  external LLM from a fact-sheet prompt (same format as the §4.4-family prompt of 2026-09-18),
  then audited line by line here. Pending external citations proposed in that prompt:
  **Milletari2016** (soft-Dice, V-Net, 3DV 2016, arXiv:1606.04797) and **Loshchilov2019**
  (AdamW, ICLR 2019, arXiv:1711.05101).
- [x] 2026-09-27: §4.4-§4.6 drafted externally, audited line by line against THESIS_FRAMEWORK.md
  §2.6, §4.6, §6, §8 and PROJECT_CONTEXT.md, spliced in (pages 40-45). Corrections made:
  - **Wrong:** the dilated stencil was attributed to "the local-kernel hybrid (§4.2.2)" -- it is
    the graph network's (§4.3.3). The cost convention read "minimum epoch time during a run on a
    named fold"; it is the minimum over folds, with that fold named.
  - **Invented, removed:** "the network quickly learns to reproduce [the fill values]"; "data
    processing is front-loaded to ensure high throughput"; the additive epoch overhead attributed
    to "validation and checkpointing routines" (the source gives no cause); cost reported
    "conservatively" (the minimum is not conservative); "operators are trained without them"
    (the covariate ablation trains *a* model, not every operator); the gradient-clip grouping
    called "architecturally required" for the mesh extension.
  - **Broken by the paste:** the loss equation's subscripts (`*{...}`) and the table row ends
    (`\` collapsed to `\`); channel index changed to c = 0..10 so the mask is channel 0 as in
    Ch. 3.
  - **Trimmed repeats** of the pushforward trick and the batch-statistics argument; filler
    removed ("strictly", "massive", "inadvertently", "rigorous", "pivotal", "monolithic").
- [ ] TODO (§4.5.1 inline): decide whether the pad-masked loss ablation (fold 2, L5nopad leg) is
  reported in Chapter 5; if not, the text stays "off in every reported run".
- [x] (confirmed 2026-10-01, utils/utils.py _rebuild_valid_t0s) TODO (§4.5.2 inline): confirm in the code that the feasible-window restriction applies only
  for B > 0 (for B = 0 the first-interval condition could never hold).
- [x] (2026-10-01: 2.6.1, PyTorch 2.4.1+cu121, read from the .sif) TODO (§4.6 inline): record the PyTorch Geometric version of the container.
- [x] (added to references.bib and cited 2026-10-01) Pending external citations from §4.5-§4.6: **Milletari2016**, **Loshchilov2019**,
  **Paszke2019** (PyTorch, NeurIPS 2019, arXiv:1912.01703), **Fey2019** (PyTorch Geometric,
  ICLR 2019 RLGM workshop, arXiv:1903.02428); each has a `% TODO: cite` marker.
- [x] #11 §4.2 "no memory of the trajectory": TODO added in 04-method.tex and a matching one in
  06-discussion.tex §6.3 (2026-09-27).
- [ ] TODO (from #11): §6.3/§6.4 — discuss the missing trajectory memory (one visit in, no
  history): what it excludes, and whether a model with history (past visits as input or a
  recurrent state) is worth testing at 5-13 visits per eye.
- [x] #12 §4.2 temporal bundling rewritten: some solvers (MP-PDE) predict several steps, not all
  operators compared here support it, so bundling is removed; "as noted above, the sequences are
  so short that splitting them into multi-step windows would not be useful anyway" (2026-09-27).
- [x] #13 §4.2 moving-mesh staleness sentence removed from the main text; TODO added at the end
  of Appendix G to state it there (2026-09-27).
- [x] #14 §4.2.1 option B applied (2026-09-27): the model can in principle predict shrinkage,
  although atrophic tissue does not regenerate; no monotonic constraint "because the reference
  segmentations themselves shrink locally between some visits (§6.3)". Inline TODO added; the
  quantification is the existing open item "Ground-truth GA retraction/shrinkage … should be
  quantified" (2026-09-17 sync section).
- [x] #15 §4.2.1 Euler-step sentence rewritten without MP-PDE: "takes the form of one explicit
  Euler step (§2.2.2), with a step size that differs from window to window. It is the same for
  every operator placed in the slot." (2026-09-27).
- [x] #16 §4.2.1 "where and how?" — the test exists (solver-swap diagnostic, T10, 2026-09-17,
  fold 2, one seed per model). Sentence rewritten to name the diagnostic and explain it: a
  trained model is re-evaluated, without retraining, under several integration schemes and step
  counts (2026-09-27). Result not previewed.
- [x] (done 2026-10-17: §4.2.1 now points to sec:experiments:validity:swap) TODO (from #16): replace "Chapter 5" in §4.2.1 by a \ref to the validity-diagnostics
  section (planned §5.6) once it exists; that section must state the fold-2 / one-seed scope.
- [x] #17 §4.2.2 view/permute tensor-layout explanation removed (2026-09-27).
- [x] #18 §4.2.2 "for the graph solver, this is guaranteed by the full-rank decoder" removed
  (2026-09-27).
- [x] #19 §4.2.2 mesh-mover channel sentences removed from the main text; TODO added in
  Appendix G (2026-09-27). All 19 items of this review are now worked through.

### Author's tablet review of §4.3–§5.5 (2026-09-29)

Fourth handwritten review (thesis pp. 30–57), decoded from
`main-thesis_v4_260929_230116.sdocx`: 38 marks. Blue = rewrite, red = wrong/remove.
Being worked through one item at a time.

- [x] #1 §4.3.1 "The loss, the curriculum, … differ in their architecture only." removed
  (already said in §4.1 and the §4.3 intro) (2026-09-29).
- [x] #2 §4.3.1 layer-encoder / TF32-precision paragraph removed (2026-09-29).
- [x] #3 §4.3.2 θ_PDE: TODO added above the paragraph and in 06-discussion.tex §6.1
  (2026-09-29).
- [ ] TODO (from #3, author: must be included): §6.1 — θ_PDE conditioning is a key
  ingredient of MP-PDE; GA has no counterpart, and the stand-ins tried here (covariates,
  layer encoder) were nulls. Discuss what is lost and what could fill the slot.
- [x] #4/#7/#29 mean+max aggregation (author: mean is the default and the only aggregation
  the thesis refers to). Removed: §4.3.2 sentence, §4.3.3 parameter-bookkeeping paragraph,
  §5.3.2 "(mean and maximum)" and the matched mean+max comparison (+0.0691), the Table 4.1
  "mean and maximum for the index-space arm" entry. The reported k-NN arm (k = 12) is now the
  existing mean-aggregation run `MPPDE_final_aggrmean` (seed 42, 5 folds) instead of the
  mean+max run `MPPDE_final_dts`. Answer to #7: mean+max is not better (mean − mean+max =
  +0.0108 ± 0.0039 SE, 4/5; per eye +0.0105 ± 0.0052, 43/75) (2026-09-29).
  - **Factual error fixed:** the k = 20 arm (`MPPDE_final_k20`) was always mean aggregation;
    Table 5.1 had 75,339 params / 1.12, now 67,147 / 1.00.
  - Numbers changed (seed 42, fold-paired from `solver_results.csv`
    `late_change_region_dice_360d_mean`; per eye with the SOLVER_FINAL_RUNS §9.8b instrument,
    which reproduced U-Net − dts +0.0504/55/75/t 5.36 and dilmean − aggrmean +0.0647/70/75
    exactly before use):
    k-NN arm 0.4515 ± 0.0429 → **0.4623 ± 0.0361**, best fold 0.5178 → 0.5153 (f2), cost
    75 → 76 s (f3), params 75,339 → 67,147 (Tables 4.2, 5.1);
    stencil − k-NN +0.0743 ± 0.0083 / +0.0752 (74/75) → **+0.0635 ± 0.0106 (5/5) / +0.0647 ±
    0.0062 (70/75, t 10.4)**, now at equal parameters;
    U-Net − k-NN +0.0531 ± 0.0226 / +0.0504 (55/75) → **+0.0423 ± 0.0246 (4/5) / +0.0399 ±
    0.0102 (53/75, t 3.93)**, fold 3 −0.022 → −0.042;
    FNO − k-NN +0.0316 ± 0.0259 / +0.0225 (40/75) → **+0.0208 ± 0.0258 (3/5) / +0.0120 ±
    0.0135 (41/75)**, without fold 4 −0.001;
    hybrid − k-NN +0.0470 ± 0.0160 (5/5) / +0.0414 (47/75) → **+0.0361 ± 0.0166 (4/5) /
    +0.0310 ± 0.0111 (49/75, t 2.79)**, LOFO min +0.024 / +0.020 — still established, but no
    longer higher on every fold (sentence removed);
    k = 20 − k = 12 (mean twin, unchanged −0.010 ± 0.005, 1/5) now also per eye **−0.011 ±
    0.003 (20/75, t −4.1)** — instruments disagree, not established;
    k-NN fold range 0.41–0.52 → 0.43–0.52.
- [x] (done 2026-10-01: all recomputed with thesis_numbers.py and matched; only x.xxx5 rounding differences) TODO (verify, author 2026-09-29): **re-check every number changed on 2026-09-29 for
  #4/#7/#29** (listed above) against `solver_results.csv` and the per-eye records, including
  that the CSV row used per fold is the right run where a fold has two rows (e.g. `dts` f2
  has two; the table values match the later row).
- [x] 2026-10-01: the four mean-aggregation twins are in (seed 42 / 7, 5 folds each, all
  30/30 epochs, one run dir per fold). Integrity: args diff vs each twin = experiment + the
  intended knob (`gnn_aggr` / `hidden_layers` / `euler_dt_scale`) + presence-only keys added
  later, at their defaults; logged params 67,147 / 40,971 (one-hop, as predicted) / 14,795.
  Not yet read out in SOLVER_FINAL_RUNS.md (code repo) — numbers computed here with the same
  instruments (fold-paired from `solver_results.csv`, superseded rows skipped; per eye §9.8b).
  Changes made:
  - **Seed-7 reach** (§5.3.2): dilmeans7 − aggrmeans7 **+0.0629 ± 0.0131 SE (5/5) / +0.0620 ±
    0.0071 (66/75, t 8.7)**; seed-pooled per eye **+0.0633 ± 0.0047 (136/150)** (was +0.0736,
    144/150 against mean+max).
  - **Seed-7 U-Net − k-NN** (§5.3.2): **+0.0548 ± 0.0181 (5/5) / +0.0517 ± 0.0109 (59/75)** (was
    +0.0655 / +0.0618); "fold 3 reads −0.042" now marked "at seed 42".
  - **One-hop floor** (Tables 4.2, 5.1, §4.3.5, §5.3.1): 40,971 params (0.61), **0.4515 ±
    0.0243**, best 0.4856 (f2), 37 s (f0) (was 45,067, 0.4529 ± 0.0403, 0.5092, 59 s).
    One − two rounds: **−0.0108 ± 0.0061 SE (1/5) / −0.0122 ± 0.0051 (33/75, t −2.4)** (was
    a null, +0.0014 / 39/75). §5.3.1 now reads "the second round adds about 0.01, consistent in
    direction but not established; a single ring buys almost everything, the second adds
    little" (was "buys nothing measurable").
  - **Per-pixel floor** (Table 5.1): pxmean, still 0.0000 on every fold; cost 28 → 16 s (f0).
  - **Δt-scaling ablation** (§5.4.1): **+0.0019 ± 0.0071 SE (3/5) / +0.0004 ± 0.0042 (40/75)**
    (was +0.0134 ± 0.0059, 4/5, mean+max) — now a clear null on both instruments.
  - For reference: aggrmeans7 0.4651 ± 0.0267 (mean − mean+max at seed 7 +0.0107 ± 0.0062).
- [x] 2026-10-01 **Matched free-form FEN control** (`FEN_final_w139Frk4d45`, 68,282 params) in
  §5.3.4 (review v4 #32): fold 4 does not train, reproducibly (0.0469, rerun 0.0467; training
  error rises from epoch 0; w96 control trains on f4, 0.501) → excluded. Folds 0–3: T-FEN −
  matched **+0.0617 ± 0.0127 SE (4/4) / +0.0648 ± 0.0064 (58/63, t 10.1)**; unmatched on the
  same folds +0.0532; w139 − w96 −0.0084 ± 0.0053 (0/4); with the failed fold +0.150. The 1.97×
  caveat is dropped (§5.3.4, §5.3.5); §4.3.6/§4.3.8/Table 4.2 "pending" TODOs removed. Verified
  against the CSV (superseded f4 attempt skipped) and SOLVER_FINAL_RUNS §9.18.
- [x] (2026-10-01: in -- fold 4 trains at seed 7; §5.3.4 filled) TODO (#32 follow-up): seed-7 matched control `FEN_final_w139Frk4d45s7` (5 folds) to be
  queued 2026-10-01 — tests whether the fold-4 failure is seed-specific; add the seed-7
  comparison against `FEN_final_w96ftp7rk4d45s7` and revise the fold-4 sentence (inline TODO).
- [x] 2026-10-01 **Capacity study written up** as new §5.4.3 "Capacity" (`sec:experiments:
  ablations:capacity`) with Table `tab:experiments:capacity` (stencil GNN w32/64/128 + 4
  rounds; U-Net w2/5/9/32; FNO+3×3 w2/5/9; T-FEN w48/96/192 + depth 8), both instruments. All
  values re-computed from the CSV and per-eye records; they match SOLVER_FINAL_RUNS §9.18
  except the width-32 U-Net per eye (−0.0453 ± 0.0113 here vs −0.0469 ± 0.0090 there; one run
  dir per fold — check the §9.18/§9.6d source). The width-32 U-Net is back as a capacity point
  (not in Table 5.1). §5.4 intro, §4.3.2 and §4.3.8 now point to §5.4.3; the §4.3.2/§4.3.8
  capacity TODOs are closed. **Author to review §5.4.3** (written directly, not via the
  external-draft + audit workflow).
- [x] (2026-10-01, resolved below) TODO: **T-FEN instability re-diagnosed** (SOLVER_FINAL_RUNS §9.19):
  crop-edge discretisation of the Galerkin transport operator, not step size (Courant at onset
  below the RK4 limit). Supersedes the CFL reading in §4.3.6 and §5.5.2 (inline TODOs in both).
  Skew-form retrain `FEN_final_w96ftp7rk4d45skew` running; re-discuss once in.
- [x] 2026-10-01 **Skew-form T-FEN in (§9.19a, outcome A) — the reported T-FEN is now the
  energy-conserving form** (author: describe both forms, say the Galerkin one became unstable,
  define instability). Verified here: 0.5428 ± 0.0401, best 0.6047 (f2), 367 s (f0); skew −
  Galerkin +0.0091 ± 0.0029 (5/5) / +0.0085 (45/75); skew − free-form w96 **+0.0618 ± 0.0040
  (5/5) / +0.0640 ± 0.0058 (68/75, t 11.0)**; skew − matched w139 folds 0–3 **+0.0716 ± 0.0094
  (4/4) / +0.0737 ± 0.0063 (59/63, t 11.7)** (unmatched same folds +0.0631; incl. failed f4
  +0.159); skew − stencil +0.0170 ± 0.0085 (4/5) / +0.0136 ± 0.0062 (46/75, t 2.2) = tie;
  skew − U-Net +0.0383 ± 0.0134 (5/5) / +0.0383 ± 0.0075 (51/75, t 5.1) — above the mixed
  floor at seed 42, **not established before seed 7**; skew − k-NN (mean) +0.0805 (5/5) /
  +0.0782 (66/75). Growth-rate r (Mai measure) 0.32 → 0.40 [0.22, 0.55]; AUC10 0.72, AUC20 0.74.
  Changes: §4.3.6 new paragraph "Two forms of the transport operator" (Galerkin conserves
  u^T M u only in the interior at constant velocity; no boundary flux → growing modes at the
  crop edge; L_skew = ½(L − M⁻¹LᵀM), Eq. `eq:method:fen-skew`, closed wall, same in the interior,
  no parameters) + **definition of "unstable"** (free-running rollout; mask and layer RMSE in
  normalised units ≤ 5 on ≥ 19/20 late epochs; criterion fixed 2026-09-11, before the skew form);
  long Courant/2.8-vs-2.4 paragraph replaced by one sentence (RK4 limit ≈ 2.4); the "natural
  no-flux boundary" sentence removed. §5.5.2 rewritten: Galerkin 7/10 unstable, where/why
  (edge onset 79–93 % of eyes, layer channel 33/34, transport 13–290× free-form, onset day
  ≈585–720 > 360-d training horizon, ×1.3 per substep, Courant at onset 1.9–2.3 < 2.4, 30-day
  step still diverges), **why Dice at 1 y stays valid** (onset after the anchor, at the edge, in
  the layers), skew form stable 5/5, border 0.516 → 0.544, >3 y growth Dice 0.537 → 0.611; new
  Table `tab:experiments:tfen-stability` (Galerkin vs skew per fold); the old Courant table
  removed. Table 5.1 T-FEN row = skew, dagger removed; §5.2 T-FEN paragraphs rewritten (tie with
  stencil; U-Net lead pending seed 7); §5.3.4 transport numbers = skew (Galerkin values kept as
  "the effect does not depend on the form"); horizon profiles inserted (§9.19a); §5.3.5 no longer
  claims "indistinguishable from the U-Net"; capacity table T-FEN points marked Galerkin;
  §5.5 intro reworded; Mai section r range 0.33–0.47. **Resolves review #26, #28, #38.**
- [x] (2026-10-01: in -- §5.2, §5.3.4, §5.5.2 filled; headline decision open, see below) TODO (T-FEN, pending): seed-7 skew run `FEN_final_w96ftp7rk4d45skews7` (5 folds, command
  given 2026-10-01) → T-FEN vs U-Net (established or tie), §5.2, §5.3.5, headline wording,
  seed-7 transport value (§5.3.4). Courant read-back of the skew checkpoints (needs `last.pt`)
  before the velocity map is quotable. Verify the §9.19a horizon values against the mai/ records.
- [ ] Code-side discrepancy (not editable here): SOLVER_FINAL_RUNS §9.19a says the Galerkin form
  "failed on 3/5" folds at seed 42, but its own table (and the old §5.5.2 table) give 4/5
  (folds 0, 1, 2, 4). Thesis uses 4/5 at seed 42, 7/10 overall.
- [ ] Removed with the old §5.5.2 (not in the text any more): the free-form FEN's long-horizon
  deficit (0.507 vs 0.641 beyond 3 y, older per-step computation) — conflicts with §9.19a's
  stencil value 0.655; re-derive before reinstating.
- [x] (fixed 2026-10-01 with #27: first column narrowed to 0.28\textwidth) TODO: Table 5.1 is
  ~10 pt wider than the text block (overfull hbox since the best-fold column was added
  2026-09-28).
- [x] #24 §5.2 "The moving-mesh arms are reported in Appendix G." removed (2026-10-01).
- [x] #25 folded into the Chapter 5 reporting scheme (#23).
- [x] #27 Table 5.1: best-fold values carry their fold index in brackets ("0.6047 [2]"); caption
  says so; per-pixel floor without index (every fold 0). §5.2 sentence now "every arm except the
  two FNO arms without a local path" (both fold 4) (2026-10-01).
- [x] 2026-10-01 §5.5.2 Galerkin part shortened (author: short — what was tried, why it failed,
  then the working version): one paragraph "The first version"; diagnostic details kept as a
  LaTeX comment (possible appendix material). A scripted edit turned two `\S\ref` into
  `\S<CR>ef` again; fixed at byte level, all chapter files checked (no stray CR).
- [x] #30 §5.3.2 now points to Figure 4.2 (`fig:method:stencils`); figure spec in §4.3.3 extended
  (two-round reach: ±4 columns ≈ 0.023 mm k-NN vs ±42 ≈ 0.24 mm stencil; render by script from
  grid spacing + offsets) (2026-10-01).
- [x] #31 folded into the Chapter 5 reporting scheme (#23).
- [x] #33/#34 §5.4.1 "Time Handling" rewritten around its purpose (author: explain what the
  section must achieve): the framework's time handling is simple (one step, Δt as input and
  multiplier); two tests ask whether its details carry accuracy, both on the canonical stencil;
  (1) Δt multiplication — result pending on the stencil (inline TODO); the k-NN run of this
  ablation is deliberately not reported (author 2026-10-01: "pretend it never happened");
  reparameterisation explanation kept; (2) Euler vs RK4 — stencil −0.012
  (4/5 lower), FNO +0.006, both within noise, ~4.8× cost; conclusion: the interval must reach
  the operator (as input or via the integrator), how does not matter; accuracy is decided by
  the spatial operator. Dropped: the fold-2 decomposition (#33). Cost details moved to a §5.7
  TODO (#34). Corrected my own draft: the RK4 arm is autonomous (no Δt input) and still ties,
  so the text says "the interval must reach the operator", not "Δt as an input is necessary"
  (2026-10-01).
- [x] (2026-10-01: null, §5.4.1 + §6.1 filled) TODO (#33 follow-up): `ANISOGNN_final_dilmean_nodts` queued 2026-10-01 (author) — fill the
  §5.4.1 Δt-multiplication result on the canonical stencil (both instruments); if not a null,
  rewrite the paragraph and the subsection's conclusion.
- [x] #35/#36 §5.4.2 "The Objective" rewritten like §5.4.1 (2026-10-01): purpose (the objective
  is part of the shared framework; which parts carry the result?), three questions answered by
  three new runs on the canonical stencil (author queued them 2026-10-01): mask weighting
  (`ANISOGNN_final_dilmean_plainmse`), soft-Dice (`…_nodice`), monotonic penalty (`…_mono2`),
  each with an inline TODO placeholder listing what to fill in (both instruments, collapse
  counter / escape epoch, epoch-to-epoch sd, raw mask RMSE for the calibration stretch). The
  pushforward/31.8× and shrinkage arguments against the penalty are kept (TODO: confirm the
  31.8× measurement setting). Removed: fold-2 loss ladder, sharpness sweep, old fold-2 penalty
  comparison, pad-exclusion leg, and the intermediate-time-point regulariser paragraph (#36;
  its point stays as the §6.1 TODO). §4.5.1: pad-exclusion TODO closed ("off in every reported
  run"); monotonic penalty "zero for every operator of the comparison … §5.4.2 tests it".
- [x] #37 §5.5.1 solver-swap test rewritten formally (author: keep it, but explain what is shown
  and the criteria; no informal analogies) (2026-10-01): what is tested and why (Neural-ODE
  reading of f_θ; Ott/Krishnapriyan) → principle (every convergent scheme approaches the ODE
  solution, error ∝ h^p, Hairer1993) → **criteria stated before results: C1 convergence
  (changes shrink under refinement), C2 agreement (settings at least as fine as training agree
  within the 0.0127 run-to-run sd)** → setup (no retraining, control reproduces the recorded
  Dice exactly) → results for three models → what follows. New: the **skew T-FEN passes**
  (fold 0, RK4 at 45/30/22.5/15 d within 0.0003; 90 d −0.0015; SOLVER_FINAL_RUNS §9.19b).
  Canonical fails (Euler refinements −0.016 then −0.060; span 0.086 ≈ 6.7× noise); RK4-stencil
  passes (+0.018 then +0.004; within 0.0044, RK4 settings within 0.0005). Table
  `tab:experiments:swap` now has three blocks with the verdict in each header; raw mask RMSE
  column dropped. Note in the .tex: C1/C2 make the §9.17 reading explicit; they were not fixed as
  numbers before §9.17 ran.
- [x] 2026-10-01 §5.5.2: Courant read-back and residual added (§9.19b, fold 0): layers ≤ 1.36,
  mask median 2.64 / max 2.85 at 45 d (slightly over ≈ 2.4); residual in 9/20 eyes, ≤ 26
  values, ≤ 36, from ~day 1,260, ×1.04 per sub-step, mask channel, top/bottom row → the step-size
  limit, minor vs the Galerkin defect (×1.3 from ~day 585); criterion still passes; a 30-day
  evaluation step (mask Courant ≈ 1.8) removes it at unchanged Dice. Velocity map quotable at a
  30-day evaluation step (not interpreted in the thesis).
- [x] (done 2026-10-02: skew rows from SOLVER_FINAL_RUNS 9.23; w192 quoted on folds 0, 2, 3) TODO (pending, T-FEN capacity in skew form queued 2026-10-01): replace the four Galerkin
  T-FEN rows of Table `tab:experiments:capacity` by `w48…skew`, `w192…skew`, `w96d8…skew`
  against the skew 1× (0.5428); drop the Galerkin footnote/sentence (inline TODO).
- [x] 2026-10-01 filled from SOLVER_FINAL_RUNS §9.20 (`thesis_numbers.py`, self-checked against
  the §9.8b anchor and our matched-transport numbers): §5.3.3 FNO vs U-Net beyond one year
  (growth-region Dice 1–2 / 2–3 / 3+ y: FNO 0.546 / 0.583 / 0.594, U-Net 0.563 / 0.581 / 0.555;
  FNO trails, ties, leads — stated as descriptive, not tested); §5.3.4 near-term (0–1 y) bin
  (free-form 0.388, one-hop 0.395, k-NN 0.393 vs T-FEN skew 0.519, stencil 0.503 — "the two
  constructions close the same near-term gap"); §5.3.4 horizon values marked verified. Pooled
  per-step aggregation; §9.8a per-eye-bin values must not be mixed with these.
- [x] 2026-10-01 SOLVER_FINAL_RUNS.md exists only once (code repo). THESIS_FRAMEWORK.md: code copy
  and thesis mirror identical apart from the mirror banner — both still at 2026-09-17, i.e. they
  contain none of: mean twins, capacity study, skew T-FEN, §9.19b/§9.20. Re-mirror once the code
  side updates it.
- [ ] Code-side §9.20 is out of date on the queue: it says "no seed-7 free-form FEN" and that
  `dilmean_plainmse/_nodice/_mono2` are "not known to be queued" — all four were queued by the
  author on 2026-10-01 (plus `dilmean_nodts`, FNO/hybrid/one-hop seed 7). When the seed-7
  free-form run is in, read the seed-7 transport effect against it, not against the seed-42
  control.
- [ ] TODO (optional): solver-swap on the skew T-FEN at fold 2 (common fold with the graph
  networks) and on the seed-7 skew T-FEN.
- [x] (2026-10-01: filled) TODO (#35 follow-up): fill §5.4.2 once `dilmean_plainmse`, `dilmean_nodice`,
  `dilmean_mono2` are in (queued 2026-10-01).
- [x] (2026-10-01: all in, read out in SOLVER_FINAL_RUNS §9.22) 2026-10-01 seed-7 runs queued (author): `FEN_final_w96Frk4d45s7` (free-form, fixes the
  mixed-seed seed-7 transport value +0.0495, which used the seed-42 free-form control),
  `FNO_final_w5s7`, `FNO_final_w5k3s7` (global+local ingredient has no replication),
  `MPPDE_final_l1means7` (optional, locality ladder); plus earlier: skew T-FEN s7 and
  T-FEN capacity points in skew form (w48, w192, d8). Read out with the usual integrity checks
  and fill the Appendix E seed-7 table of the reporting scheme.
- [x] 2026-10-01 **Batch readout** (11 of 13 arrays; `thesis_numbers.py`, anchor reproduced;
  written to the code repo as SOLVER_FINAL_RUNS **§9.22**, not committed there). Filled into
  Chapter 5: §5.2 (skew T-FEN s7 vs U-Net +0.0246 ± 0.0073 (5/5) / +0.0255 (52/75, t 3.4); vs
  stencil +0.0165 ± 0.0021 (5/5) / +0.0152 (49/75, t 3.1)); §5.3.1 (one-hop s7 level with two
  rounds, +0.0036 -> "adds at most ~0.01, not reproducibly"); §5.3.3 (seed-7 FNO / hybrid: hybrid −
  FNO −0.0057, hybrid − U-Net −0.0193 (0/5), FNO − U-Net −0.0136 -> the local-path claim rests on
  seed 42 only, "not established"); §5.3.4 (transport at seed 7 vs same-seed free-form +0.0897
  (5/5) / +0.0878 (71/75); Galerkin s7 +0.0758 replaces the mixed-seed +0.0495; w139 s7 trains on
  every fold incl. f4 (0.4418), T-FEN − matched +0.0762 (5/5) / +0.0750 (73/75)); §5.4.1 (nodts
  −0.0006 ± 0.0061, per eye −0.0028: null); §5.4.2 (plainmse 0.0000, never escapes, 74/75 eyes
  identical to baseline; nodice −0.0496 ± 0.0172 (0/5) / −0.0460 (19/75, t −5.1), escape epochs
  2/8/3/7/12, late sd 0.043 vs 0.015, raw mask RMSE 0.51 vs 1.10; mono2 −0.0036 / −0.0042: null);
  §5.5.2 (skew s7 stable 5/5, max mask 2.63, layer 1.11). §6.1 l. 40 TODO closed (Δt null).
  Capacity: w48 skew 0.5434 (= w96 skew, +0.0006), stable 5/5 -- rows replaced only once w192 /
  depth-8 skew are complete.
- [x] (decided 2026-10-01, later session: (a) scope the headline, (b) demote global+local to an
  observation, (c) objective into 6.1 + Ch. 7; also 1.4 merged into 1.3, border split reported,
  Huang1991 cited, spacing check in 6.3 only, Gao2019 kept -- full wording in prompts/open.txt
  section 2; APPLIED 2026-10-01: abstracts, 5.2, 5.3, 6.1, 6.3, Ch. 7, 1.3 (1.4 merged), 4.1
  provenance sentence, 2.1.3 Huang1991, 2.1.6 spacing -> 6.3, App. E border/interior table) **Author decisions from the batch (2026-10-01)** -- inline TODOs in 5.2, 5.3.3, 6.1, Ch. 7,
  abstract: (a) the skew T-FEN lies above the U-Net at both seeds and +0.016/+0.017 above the
  stencil at both -- "the strongest arms of different classes are indistinguishable" / "lie close
  together" / "architecture class does not decide" need rewording or scoping; (b) the global +
  local ingredient does not replicate at seed 7 -- it is named in 5.3 intro, 5.3.5, 6.1, Ch. 7,
  abstracts (and possibly 1.4); (c) the soft-Dice term raises the score and plain MSE never
  learns change -- 6.1 "Where modelling effort pays" / Ch. 7 are silent on the objective.
- [x] (in 2026-10-02, SOLVER_FINAL_RUNS 9.23) Still running: `FEN_final_w192ftp7rk4d45skew` (f3, f4 at 29/30), `FEN_final_w96d8ftp7rk4d45skew`
  (f2-f4) -> capacity table T-FEN rows (all four together).
- [x] Code-side request "SOLVER_FINAL_RUNS readout for the four mean twins" done there (§9.21).
- [ ] TODO (code repo, not editable from here): add a SOLVER_FINAL_RUNS.md readout for the
  four mean twins (aggrmeans7, l1mean, nodtsmean, pxmean), so the numbers above have a source
  entry there; re-mirror THESIS_FRAMEWORK.md afterwards.
- [x] (superseded 2026-10-01, see above) TODO (pending runs queued 2026-09-29, mean-aggregation
  twins; review and confirm when finished): `MPPDE_final_aggrmeans7` (k-NN, seed 7) → seed-7 reach replication vs
  `ANISOGNN_final_dilmeans7` and seed-7 U-Net vs k-NN (§5.3.2, both removed and marked
  inline); `MPPDE_final_l1mean` (one-hop floor) → Tables 4.2/5.1, §4.3.5 parameter count,
  §5.3.1 ladder (note: against the mean two-round arm the old one-hop floor reads −0.0094 ±
  0.0026 fold-paired, 5/5 — "the second ring buys nothing" must be re-checked);
  `MPPDE_final_nodtsmean` → §5.4.1 Δt-scaling ablation (currently mean+max, marked inline);
  optional `MPPDE_final_pxmean` (per-pixel floor; aggregation inert).
- [x] #5 §4.3.2 decoder paragraph rewritten: the original's 1-D convolutional head emits K
  bundled steps; with K = 1 it was removed and replaced by the MLP decoder with a full-rank
  linear output layer; no rank-1 / width-113 wording (2026-09-29).
- [x] #6 §4.3.3 bridge added: two-round reach ≈ a third of the median advance; the index-space
  graph solves connectivity but not reach, hence a second construction (2026-09-29).
- [x] #8 p. 37 red wavy line: a divider, no action (author, 2026-09-29).
- [x] #9 §4.3.6 "A matched free-form control … was not run" replaced: the width-139 control
  (68,282 params) is compared in §5.3.4; inline TODO pending the run (2026-09-29).
- [ ] TODO (from #9, with #11/#32): once `FEN_final_w139Frk4d45` is in — fill §5.3.4, add a
  Table 4.2 row (FEN free-form w139, 68,282, 1.02, transport term (matched)), reword the
  Table 4.2 caption and §4.3.8 "One comparison is not matched"; decide whether the 1.97×
  caveat can be dropped (pre-registered decision rule, 2026-09-28).
- [x] #10 §4.3.8 Hu et al. (2023) sentence removed; kept "so that differences between arms
  cannot be attributed to extra parameters" (2026-09-30).
- [x] #11 §4.3.8 unmatched-control paragraph rewritten (w96 half-size, w139 matched, TODO
  pending the run); Table 4.2 row for the w139 control added, caption reworded (2026-09-30).
- [x] #12 §4.4 "Whether they carry useful information … not settled" removed (2026-09-30).
- [x] #13 §4.4 layer-encoder paragraph moved to Future Work: wrapped in \iffalse in §4.4 (source
  text kept), the §4.3.2 pointer to it removed, a detailed TODO added in §6.4 (2026-09-30).
- [x] #14 + #21 late-epoch mean explained in §5.1.3: noise (sd 0.02–0.10 at 12–20 eyes) and
  upward bias of a best-epoch value chosen on the validation eyes (no test split); window
  fixed in advance and identical for every arm; starts at epoch 10 because the learning rate
  has been reduced once (after epoch 5) and the fast early phase is over (author's reason).
  §4.5 keeps a one-clause pointer; the Table 4.3 reference moved to the §4.5 intro
  (2026-09-30).
- [x] #15 §4.6 TF32/FP32 precision sentence removed (kept as a LaTeX comment). With #2, the
  precision mismatch is no longer stated in the text (2026-09-30).
- [x] #16/#17 §4.6 run-identity and results-table/cost paragraphs removed; run identity →
  TODO in Appendix F, cost convention → TODO in §5.7 (2026-09-30).
- [x] #18 §5.1.2 "Third, the metric differs …" rewritten: growth-region Dice = new atrophy
  only, change-region Dice = every changed pixel; Table 5.1 / fold-paired values use the
  change-region Dice, the per-eye instrument the growth-region Dice (2026-09-30).
- [x] #19 §5.1.2 crop-variant paragraph (border/interior split, pad-masked metric) commented
  out — neither enters a reported number. §3.3 now points to §6.3 instead, §4.5.1 pointer
  removed, §6.3 crop-censoring TODO added (2026-09-30).
- [ ] TODO (from #19, later): decide whether to report the border vs interior split once
  (sentence in §5.2 or Appendix E table). 5-fold late means (all / border / interior):
  stencil 0.526/0.516/0.522, U-Net 0.505/0.483/0.511, T-FEN 0.534/0.516/0.535, hybrid
  0.498/0.479/0.506, FNO 0.483/0.452/0.495, k-NN mean 0.462/0.464/0.455; ranking unchanged
  on interior eyes; descriptive only (small subgroups). Pad-masked (`_anat`) differs by
  ≤ 0.002 everywhere — drop it.
- [x] #20 §5.1.2 metrics trimmed and explained (2026-10-01, author: every metric that is
  mentioned needs a plain description). Kept with descriptions: change-region Dice (plain
  meaning of Dice added), growth-region Dice with horizon bins, collapse counter. Removed from
  §5.1.2: √area MAE, full-mask Dice per bin, change-region IoU / full-mask Dice/IoU sentence
  (never reported). Growth rate, Pearson r and fast-progressor AUC moved to a new §5.5.1
  "Comparison with Mai et al. (2024)" (`sec:experiments:qualitative:mai`) with Table
  `tab:experiments:mai`.
  - Checked against Mai et al. 2024 (PMC11000109, Statistical Analysis + Results): growth rate
    = √-transform difference baseline → follow-up per year, r "calculated over the entire
    follow-up period", AUC for top 10/15/20 % of growth rates — the same definitions as our
    code (`train.py` per-eye record: (√A_last − √A_base)/cum_dt over the whole rollout). Open:
    two-point vs fit (paper does not say), "patients" vs eyes in the top-x % cut-off.
  - Canonical model, pooled 75 eyes, late-epoch mean of predicted rates, bootstrap 2000:
    r 0.40 [0.22, 0.56] (Mai 0.61); AUC top 10 % 0.74 [0.52, 0.91] (8 eyes, Mai 0.81); top
    15 % 0.70 [0.53, 0.86] (11, Mai 0.79); top 20 % 0.70 [0.53, 0.84] (15, Mai 0.77).
    Baseline √area alone r −0.10. Mean follow-up 3.3 y (median 3.0, 2.0–5.9); Mai 32 months.
  - (Superseded 2026-10-01 by Appendix E tab:appendix:growth-speed, skew T-FEN r 0.40, RK4 arms
    0.30 / 0.31 -> range 0.30-0.47.) All arms (r; AUC10; AUC20): stencil 0.40/0.74/0.70, U-Net 0.43/0.68/0.76, T-FEN
    0.32/0.70/0.67, FNO+3×3 0.33/0.75/0.78, FNO 0.33/0.72/0.70, k-NN mean 0.41/0.74/0.73,
    one-hop 0.47/0.76/0.71 — all intervals overlap; the arms do not differ on these measures.
  - The per-fold r/AUC logged by the code (16 eyes, 2 positives) are not usable; only the
    pooled values are.
- [x] (done 2026-10-01: all three arms above Mai in every bin by 0.2-0.3; stated as not head-to-head) TODO (from #20): §5.5.1 — compare growth-region Dice per horizon bin with Mai Table 2
  (inline TODO); optional appendix table of r/AUC for all arms.
- [x] (2026-10-19: §6.2 states it, now with the §5.7 comparison and three untested explanations) TODO (from #20): §6.2 — "good at where, weaker at how fast" (inline TODO).
- [x] (checked 2026-10-01: Ch. 5-7 all defined; border-touching definition added to §5.1.2) TODO (from #20, author 2026-10-01): **every metric mentioned anywhere must have a plain
  description** of what it measures — check Chapters 5–6 for metrics used without one.
- [x] #22 §5.1.3 "Runs are compared only when … same version of the pipeline" removed
  (2026-10-01).
- [x] **#23 / #25 / #31 — Chapter 5 reporting scheme (agreed 2026-10-01, author to review once
  more on 2026-10-02; apply as ONE dedicated pass after the remaining review items):**
  APPLIED 2026-10-02. §5.1.4 rewritten as "Noise Level and Comparisons" (~2/3 page): training
  noise and folds, "differences of about 0.02 or less are within the noise level", the rule in
  words, eye counts on growth-region Dice, one sentence on the second seed ("the conclusions
  drawn in this chapter hold at both"; author: do NOT single out the local-path result there).
  Chapter 5 text now seed 42 only, results in words ("higher by X on average, on k of the five
  folds and on m of the 75 eyes"; counts are "first arm higher" everywhere), no SE / t / Δ
  notation; the reach and capacity tables show the mean difference and folds/eyes higher only.
  §5.3.3 seed-7 paragraph removed (local path "not established", with the hybrid/FNO
  instrument disagreement as one sentence; k = 20 likewise); §5.3.4 keeps one qualitative
  sentence that the matched control trains on all folds at the second seed (explains the
  fold-4 failure); §5.5.2 Galerkin count now seed 42 (4/5) + "most of the runs repeated with the
  second seed". Appendix E: new section "Statistical Criteria" (`app:full-results:criteria`:
  0.0127 replicate sd, √2/√5 derivation -> 0.036 / 0.016, U-Net 1.9x -> 0.020, both
  instruments, LOFO, |t| about 2.5 -- not fixed in advance, the earlier note said 2.7 but the
  readings made correspond to 2.5 (FNO - U-Net t -2.51 counted, T-FEN - stencil 2.17 not) --
  second-seed requirement, fellow-eye caveat); "Statistics of the Comparisons" now three tables
  (`tab:appendix:seeds`, `tab:appendix:seeds-b`, `tab:appendix:seed42`) covering every
  comparison quoted in Ch. 5, all recomputed with thesis_numbers.py pair (every Ch. 5 number
  reproduced). The old "Float too large" warning in Appendix E is gone (table split).
  Still to decide (author): §6.1 and Ch. 7 still mention seeds ("at both seeds", local path
  "level at one seed but not at the second", Ch. 7 transport bullet "at a second seed ... 0.076").
  1. **One seed in the text** (seed 42). One sentence in §5.1: the main comparisons were
     repeated with a second seed and every conclusion held (Appendix E). All seed-7 numbers
     move to an appendix table (reach, U-Net vs k-NN, T-FEN, transport term, stencil / U-Net /
     T-FEN ties — all replicated).
  2. **One noise level as an intuition** instead of the 0.036 / 0.016 / 0.020 thresholds:
     "retraining the same model already changes its score by up to about 0.02; smaller
     differences are not interpreted". The √2/√5 derivation and the U-Net 1.9× spread go to
     the appendix.
  3. **Results in words, statistics in the appendix**: e.g. "the dilated stencil is higher by
     0.064 on average, on all five folds and on 70 of the 75 eyes". SE, t, LOFO in one
     Appendix E table (one row per comparison). The notations "Δ = x ± y SE (k/5)" and "per
     eye x ± y (m/75, t)" disappear from the chapter (this also dissolves the §5.1.4
     same-sign-vs-higher counting TODO — "higher on k folds" everywhere).
  4. **Detail only where there is a claim**: established effects one sentence; nulls "no
     difference beyond the noise level"; the two instrument disagreements (hybrid vs FNO,
     k = 20) one honest sentence each.
  5. **§5.1.4 shrinks to ~½ page**: what varies (training noise, folds), the noise level, "a
     difference is real when it exceeds the noise level and holds on most folds and most
     eyes", pointer to the appendix. The precise rule (fold-paired above the floor; per eye
     |t| ≳ 2.7 — fixed after the fact, say so; both robust to leaving out a fold) and the
     fellow-eye caveat (75 eyes from 51 patients, t optimistic) go to the appendix.
  Keep "mean ± sd" over the five folds in tables (author: understandable).
- [x] (2026-10-19: stated in §5.8, first paragraph) TODO (from #17): §5.7 must state the cost convention (min epoch time over folds, why
  not the mean, 280–320 steps per epoch) — Table 5.1's caption points to §5.7.
- [ ] TODO (from #13): §6.4 — a learned summary of the retinal structure as a θ_PDE stand-in;
  first version (layer encoder) tried only at four widths on one backbone, null (inline TODO).
- [ ] TODO (from #12): §6.3 — covariates are enabled but their value is unsettled; the
  ablation (k-NN, mean+max era) is not reported in Ch. 5 (inline TODO in 06-discussion.tex).
- [x] (done 2026-10-01: 4.3.7 rewritten; 5.4.1 / 5.5.1 aligned) TODO (author, 2026-09-30): **explain the RK4 setting much more plainly** in §4.3.7,
  §5.4.1 and §5.5.1 (inline TODO in §4.3.7 lists what to cover: Euler vs RK4, "autonomous"
  = Δt input zeroed, why the wrapper exists — FEN integrator, integration-order null,
  continuous-time question — and jump model vs continuous-time model). Decide the fate of
  the RK paragraphs together with #33, #34, #37.
- [ ] TODO (§6.1/§6.4, from the RK discussion 2026-09-30): two attempts to make the model
  behave sensibly between visits — the intermediate-time-point regulariser (supervision
  against the linear interpolant) and the autonomous-RK4 arm (continuous-time by
  construction) — neither improves Dice at the anchor. The RK4 arm is time-consistent (fold 2,
  one seed) at ~4.8× cost; if intermediate-time predictions are needed clinically it is the
  principled variant, but its in-between predictions are unverified (no ground truth between
  visits).
- [ ] TODO: the commented-out §5.4.3 (covariates) and §5.4.4 (GNN-internal settings) were run
  on the mean+max k-NN arm; if either is reinstated, it needs mean twins or an explicit note.
- [x] (resolved 2026-10-02 by the reporting pass: counts are "first arm higher" everywhere, in the
  text and in Appendix E) TODO: fold/eye-count convention. §5.1.4 defines k (and m) as the number of folds (eyes)
  on which the difference has **the same sign as the mean**, but Chapter 5 counts the folds
  where the first arm is **higher** (e.g. FNO − U-Net −0.0215 "(1/5)", per eye "(30/75)";
  Table 5.2 "0/5" for negative means). Fix the definition in §5.1.4 (and the Table 5.2
  caption) to match the usage, or recount everything.

- [ ] 2026-09-30: external-LLM prompt for the remaining parts written:
  `prompts/PROMPT_final_chapters.md` (§5.6 Computational Cost, Ch. 6 Discussion, Ch. 7
  Conclusion, English abstract + Kurzfassung). Fact sheet taken from the audited Chapters 3-5
  as of commit 7f93ab9; pending runs (seed-7 skew T-FEN, Δt-multiplication and objective
  ablations on the stencil, T-FEN capacity in skew form, seed-7 matched transport control)
  are to be left as `% TODO`. Audit the returned draft line by line before splicing.
- [x] 2026-09-30: external draft of §5.6, Ch. 6, Ch. 7 and both abstracts returned, audited
  line by line against the prompt's fact sheet and rules, rewritten where needed, spliced in;
  builds clean. Corrections made:
  - **Wrong:** "31.1 % of these cropped *visits*" (it is 31.1 % of cropped *lesions*); the
    transport effect given as "+0.062 over a matched control on four folds" (+0.062 is against
    the same-width control on 5 folds; the matched control is +0.072 on folds 0-3); "the 4.8x
    factor holds generally ... as seen with the FNO" (the FNO, ~2x, is the counterexample);
    "none buy accuracy beyond the noise floor of 0.0127, except the T-FEN, which ties"
    (self-contradictory; the paired floor is 0.016); "the FNO + local path bridged the gap to
    the strongest models" (it ties the U-Net); Mai et al. called a "clinical baseline" /
    "competing model trained on the same cohort".
  - **Unsupported, removed or turned into hypotheses:** "the objective's details did not yield
    measurable benefits" and "the Delta t multiplication is a reparameterisation" stated as
    results (runs pending); "reach and transport yield equivalent improvements" (different
    controls; now "each established against its own control, indistinguishable from each
    other"); "without an eye-level descriptor the operators struggle to capture speed" (now an
    untested contributor); "learning from raw OCT is required to close the gap to Mai";
    "the models reliably locate areas of change"; "segmented masks limit the available
    context"; "a detailed qualitative analysis is outlined in §5.5" (unwritten, TODO).
  - **Missing, added:** the between-visit paragraph (regulariser vs RK4 arm, author TODO);
    what could fill the theta_PDE slot; the full crop census and trade-off; the PINN reason;
    Mai caveats beyond the input (cohort size, crop); CFL cited to Courant1928 and framed as
    "consistent with", not proof; moving-mesh null scoped and pointed to Appendix G.
  - Banned words removed ("strictly"); placeholder `% TODO: cite <ProposedKey>` for UQ removed
    (no claim needs it); banners restored; abstract no longer says "best canonical model".
- [ ] TODO (Ch. 6/7/abstract): revise once the queued runs are in -- seed-7 skew T-FEN
  (headline wording, §6.3 "Unfinished replications"), Delta t-multiplication ablation (§6.1
  inline TODO), objective ablations, T-FEN capacity in skew form, seed-7 matched control.
- [x] (2026-10-01: none found; Salvi2025 inter-grader growth-region Dice 0.71-0.73 added as orientation) TODO (§6.2 inline): literature check for a clinically meaningful threshold for spatial
  GA progression forecasts.
- [ ] TODO (§6.2 inline): link to the failure cases once §5.5 qualitative is written.
- [x] (read back in tablet review v6, 2026-10-02) Author to review §5.6, Ch. 6, Ch. 7 and both abstracts (German text in particular).

### Author's tablet review of the abstract, Ch. 6 and Ch. 7 (2026-10-01)

Fifth handwritten review (build of 2026-10-01), decoded from
`main-thesis_v5_261001_095557.sdocx`: 12 marks on 7 pages (abstract, pp. 63-65, 67,
68, 70); no marks in Chapters 4-5. Blue = rewrite, red = wrong/remove. Being worked
through one item at a time.

- [x] #1/#2 Abstract (blue: moving-mesh sentence; last paragraph "don't like this").
  Author: no moving mesh (not the main part), no comparison with another model, too
  simple, needs technical aspects and results. Rewritten in full 2026-10-01 (English and
  German): state (11 channels, 49 x 1024), update u + Δt f_θ, zero-init, curriculum, the
  operators; results 0.54 ± 0.04 / 0.53 ± 0.05 / 0.50 ± 0.06 (mean ± sd over folds,
  Table 5.1), reach +0.064 at equal parameters (5/5), transport +0.062 (same-width
  control), FNO below U-Net and the 3 x 3 path bringing it level, capacity 1/4x-4x and
  RK4 nulls, growth-rate r 0.40 without the Mai comparison.
- [x] (author 2026-10-01: "it's fine", keep as is) Abstract length: English ~470 words fits one page; the German Kurzfassung now runs
  onto a second page (pp. iii-iv).
- [ ] TODO (abstract inline): T-FEN value and the ordering of the three strongest
  operators after the seed-7 skew T-FEN run.
- [x] #3 §6.1 "which scores zero on the headline metric (Table 5.1)" removed.
- [x] #4/#12 huge U-Net (width 32, 3.35 M, ~40x): author wants **no mention anywhere**
  ("makes no sense to report"). Removed from §6.1 Capacity (now "no width step raised a
  class above the noise level, and the smaller versions lost little"), §5.4.3 (table row
  commented out, sentence removed), Ch. 7 "What did not matter"; THESIS_STRUCTURE.md and
  CLAUDE.md updated so it does not come back. Ch. 4 had it commented out since 09-28.
- [x] #5 §6.1 sentence on the earlier GNN-internal ablation removed (the moving-mesh
  clause of the preceding sentence kept, author).
- [x] #6 §6.2 ", and none was tested" removed.
- [x] #7 §6.3 ": an ablation on an earlier configuration found no detectable benefit,"
  removed (joined with a semicolon).
- [x] #8 §6.3 "The survey leaves out two classes …" removed; §6.4 Trajectory memory now
  "It is also the setting in which sequence models such as recurrent networks and
  transformers apply." (author: not "we didn't bother").
- [x] #9 + #11 §6.3: moving-mesh scope sentence replaced by: all operators on the uniform
  grid; mesh adaptation might help but excludes regular-grid operators (U-Net, FNO); one
  extension tested in Appendix G, no conclusion drawn. §6.4 "The moving mesh" paragraph
  removed; its next-state-monitor sentence moved to a new Appendix G section "Outlook"
  (`app:mm-pde:outlook`).
- [x] #10 §6.3 "Unfinished replications" removed; the pending-run list is kept as a
  `% TODO` comment there (runs in progress, results expected within hours).
- All 12 items of review v5 worked through.

### Citation recheck and corrections (2026-10-01)

Second, independent pass over all 176 entries of `literature/_ledger.md`: 11 agents
re-judged every citation against the PDF text without seeing the earlier verdicts, plus
one pass over the 16 citations that were new or reworded after the ledger was built.
Per-citation evidence: `literature/_recheck_2026-10-01.md` (git-ignored). 138 of the 163
re-judged entries agree with the ledger. The 13 citations of books without a local copy
(LeVeque 2002/2007, Gottlieb & Orszag, Trefethen, Bartels, Hairer, Butcher, Scarselli,
Huang & Russell) were judged from general knowledge only; the Bartels "splitter"
attribution was checked through the MP-PDE text.

- [x] Corrections applied step by step with the author, each as the smallest change to
  wording or citation: §1.1 (AMD numbers: 288 million is 2040 not 2050, cited to Wong;
  bilateral GA, trial results, treatment timing, Vallino wording), §1.2/§1.3 (no "deep
  learning" for Schmidt-Erfurth/Vogl, Yehoshua "found" not "demonstrated", Singh
  pegcetacoplan clause, prior-work claim), §2.1 (cRORA is not restricted to eyes without
  MNV, iRORA 93 % is one study, Chu rim wording, Pilotto ICC 0.97-0.98 and sections, en-face
  list, Ebneter/Vallino numbers, Pilotto 99 % clause deleted, bilateral GA), §2.2-§2.4
  (Yehoshua margin growth, FEN transport variant, related work: Schmidt-Erfurth,
  Bogunovic, Vogl, Lad/Singh sentence deleted, Vallino, Mai, Salvi, MP-PDE credit), §3.1/§3.6
  and §5.1.3 (Mai cohort and anchor wording, Feuer/Yehoshua), §4 (Ott only for the
  consistency caution, MP-PDE limitations, "main departures", Gupta, Courant, table row
  "State"), §5.6.1/§6.2/Ch. 7 (Mai: larger cohort of the same clinic, no cropping reported,
  growth-rate definition, gap 0.18 to 0.29), Appendix G (BFGS not L-BFGS, Hu et al.
  ablations as in their Table 9).
- [x] `references.bib`: Yehoshua2011 given name Manuel (not Maria) Falcao; Singh2025
  Quilantan is Jaclyn; middle initials of Dorairaj (K.) and Worrall (E.).
- Left unchanged on purpose (a gloss or origin citation the source does not contradict):
  Boyer2017/Boopathiraj2024 "outer segments", the three-signature list (union of
  Vallino/Yehoshua/Boopathiraj), en-face definition, Courant1943, Runge1895, Kutta1901,
  Paszke2019/Fey2019 version numbers, SanchezGonzalez2020/Pfaff2021 (cloth rests on Pfaff).
- [ ] TODO (inline in `02-background.tex` §2.4): confirm with the supervisor how the 75-eye
  cohort relates to the 184-eye cohort of Mai et al. (2024); the thesis now says "a larger
  cohort of the same clinic" everywhere. The device and mask provenance TODOs in 03-data.tex
  stay open.
- [x] Verification pass over the 76 reworded sentences that have a local source (4 agents):
  66 fully supported, 10 leftovers, 9 of them fixed in a last round (Wong "projected" instead
  of "lived", Vallino "largely relied" dropped, "segmentation" not "automatic segmentation"
  for Chu, INL "thickness", FEN "finite-element discretisation with learned dynamics",
  Bogunovic predicts drusen regression, Mai device hedged as in Ch. 3, "field of view" in the
  three Mai captions, "definitions of Mai as far as specified"). The corrected wording of
  these 9 follows the agents' own suggested fixes and was not run through the check again.
  Not changed: Vallino "largely preserved" (Boyer, co-cited, has the exact wording) and Lad
  "Until 2023" (the year comes from the approvals in the next sentence).
- [x] Ledger and hub notes updated (`update_ledger.py --apply`, then the verified verdicts of
  this pass written into the 91 changed or new entries): 165 SUPPORTED, 10 PARTLY (the
  decisions above to leave a gloss or origin citation as it is), 14 PENDING (sources not on
  disk). Backup of the previous ledger state in the session scratchpad only.
- [ ] Optional primary sources, not in `references.bib`, that now stand behind a secondary
  statement: Corradetti et al. 2021 (iRORA 93 %), Zhang et al. 2022 (RPE-BM distance plus
  ORL thickness, 62 %), Vogl et al. 2023 Ophthalmol Retina 7:4-13 (topographic GA
  progression), Lindner et al. 2015 (faster growth towards the periphery), Bui et al. 2022
  (description of the Mai cohort).

### Editorial review: flow, clarity, tone, AI tone (2026-10-01)

Whole-thesis editorial review against the author's brief (reader flow, clarity, academic tone,
AI-tone mitigation; citations, references, formatting and numbers excluded). The GPTZero scans of
2026-10-01 (every chapter "AI Generated", 67-89 % of words flagged, including 82 % of the plain
Ch. 3) were used as pointers, not as evidence. Advisory only: no `.tex` file was changed.
English abstract, Ch. 1-7 and App. A-G were reviewed; the German Kurzfassung was not.
- [ ] Author to work through `reviews/editorial-2026-10-01/`: `00-overview.md` (macro feedback,
  fix-first list, structure S1-S25, transitions T1-T13, repetition R1-R17, reader-lost points,
  terminology table, AI-tone patterns P1-P14, rules of thumb) and 14 micro files with 544 verified
  items (15 high, 277 medium, 252 low), each with `file:line`, GPTZero label and a suggested
  rewrite. Line numbers refer to the sources of 2026-10-01, 21:43.
- [x] Fix first: two sentences are missing from the PDF because the prose sits at the end of a
  `%` comment line: `05-experiments.tex:163` (§5.1.3, the second of the "two reasons") and
  `05-experiments.tex:903` (§5.4.2, the cost of the soft-Dice term). Review items 5a.19, 5c.17.
  Fixed 2026-10-01 by a line break after each comment (wording unchanged), verified in the PDF
  text. Review line numbers in `05-experiments.tex` after l. 163 are now +1, after l. 904 +2.
- [x] 2026-10-02: **all 15 high-severity review items closed.** Six were already resolved by the
  review-v6 pass and the Chapter 5 reporting pass (1.8 abstract rewritten, 1.27 covariate claim
  removed, 5c.11 objective opener now "without any emphasis on the mask", 5d.16 "Its accuracy"
  now explicit) or by the comment fix (5a.19, 5c.17). The other nine fixed by wording only:
  1.41 §1.3 "the same deficit" glossed in place (Ch. 7 wording), em-dash list removed; 2a.7 §2.1.1
  "takes some getting used to" and "three of those layers" removed; 2a.17 §2.1.2 the OCT
  signatures now "delineate the lesion itself" (no claim that they define channel 0); 2b.37 §2.3
  "It must be stated plainly" removed, Neural-ODE reading explained; 2b.44 §2.4 "sits at the
  intersection of" paragraph rewritten; 3.25 §3.5 "transition window, a pair of consecutive
  visits" at first use; 4b.25 §4.3.6 transport mesh "seven interleaved triangulations" (checked
  against `fen.py` `_lattice_triangulation`, offsets 0-6, 2*48*1017 = 97,632); 5d.4 §5.5.1 C2 and
  the Table 5.4 caption "in both step and order" (with "by step or by order" the RK4 network's
  Euler one-step setting, -0.020, would fail it); 5d.23 §5.6.1 Pearson r no longer said to check
  scale. Build clean, all nine passages verified in the PDF text.
- [x] 2026-10-02: three more fix-first items closed: §2.1.5 "not auxiliary context" -> "carry
  information on the growth rate" (no clash with "auxiliary targets" in §3.2/§4.5.1 any more);
  §2.1.1 pointer to §1.2 -> §1.1; "arm" defined in §4.1 ("Each setting of the slot is referred to
  below as an arm of the comparison."). §3.7 "revisited in §5.1" was already gone (c6b9d48).
  Still open from this list: the Fig. 2.2 caption mapping strata onto the ten channels (figure is
  a placeholder), "canonical" with several meanings, "canonical fold" undefined.
- [x] (superseded by the entry below) Status of all 544 review items on 2026-10-02, before the
  one-word pass: 465 unchanged, 49 partly changed, 28 gone, 2 fixed by the comment fix.
- [x] 2026-10-02 one-word pass (41 edits, wording only, build clean, verified in the PDF text):
  16 review items whose suggestion differs by one or two words (1.43, 2a.26, 2b.1, 3.17, 3.23,
  3.33, 4c.2, 4c.25, 5a.6, 5b.20, 5d.12, 5d.39, 6-7.10, 6-7.37, G.38, G.42), plus 25 emphatic
  adverbs removed (naturally, actually, materially, precisely, essentially, fundamentally x7,
  inherently, reliably, strictly, purely, simply, entirely x3, Intuitively, Crucially,
  inevitably). Kept on purpose: WENO ("essentially non-oscillatory"), "purely imaginary",
  "timed precisely enough", "essentially the same lesion" (a hedge), "change actually
  happened" (true vs predicted), "purely global" (= global only), "clearly exceeds" (the
  criterion) and "clearly above zero" (interval excludes zero). The two "cut the sentence"
  items (4a.4, 5b.26) are left for the author.
- [ ] Status of all 544 review items after the one-word pass: **fixed 32** (15 high, 4 medium,
  13 low; incl. 4a.7 "arm" now defined); **partly addressed 21** (adverb removed, rest of the
  rewrite still open: 1.20, 1.25, 1.36, 2a.13, 2a.16, 2b.23, 2b.27, 2b.29, 2b.30, 2b.35, 2b.42,
  4a.10, 5b.19, 5c.5, G.1, G.3, G.4, G.5, G.6, G.8, G.9); **changed since the review, mostly by
  the author's own passes, 64** (37 medium, 27 low; check whether still needed); **open 427**
  (219 medium, 208 low). Open medium by kind: 81 flow, 59 clarity+tone, 48 clarity, 31 tone
  only. Status per item: session scratchpad `category_final.json` (not in the repo).
- [ ] Contradictions and dead pointers found (review S4, S5, S9, S22): §1.2 promises the
  covariates are "tested in this thesis" (the test is commented out, §6.3 says unsettled);
  layer channels "not auxiliary" (§2.1.5) vs "auxiliary targets" (§3.2, §4.2.2, §4.5.1); the Fig.
  2.2 caption maps strata onto the ten channels although the boundary names are unknown; §2.1.1
  points to §1.2 for subfoveal significance (it is §1.1); §3.7 promises fold heterogeneity is
  "revisited in §5.1" (it is not). The mask-provenance contradiction §2.1.2 vs §3.1 is the open
  FACT CHECK item of 2026-09-25 (review 2a.17).
- [ ] Wording that changes a result's reading (review 5d.4, 5d.16, 5d.23, 4b.25, 5c.11): C2
  criterion "by step or by order" lets the RK4 arm fail; "Its accuracy" in §5.5.2 reads as seed 7;
  Pearson r described as checking scale; T-FEN transport mesh reads as one subsampled mesh; the
  objective-test opener says each run changes one part (the first changes two).
- [ ] Terms used before definition or with several meanings: arm (never defined), canonical
  (fold / normalisation / age mode / model), "the same deficit" (abstract, §1.3; defined §5.3.5),
  window (crop vs visit pair), floor, anchor, late epochs. Review suggests one definitions
  paragraph at the end of §4.1.
- [ ] Structural suggestions to decide (review S2, S3, S7, S12): research-question mapping (Ch. 4
  never names sub-question 1; the framework evidence is in §5.4); §5.4 "Negative Results" holds
  the clearest positive framework result (§5.4.2); framework spread over §4.2/§4.4/§4.5; §5.6
  "Qualitative Analysis" contains only the Mai comparison. Repetition across chapters R1-R17
  (crop census four times, Mai caveats about seven times, continuous-time caution four times).

### Figure plan (2026-10-01)

Author: work the figures back to front (appendix and Chapter 5 first, medical illustrations
last), not sequentially. Every figure and its script go into the thesis repo (`images/`,
`images/scripts/`) and follow `style/`; code-repo scripts (practical, poster, presentation)
are ported, not edited. The per-figure TODOs further down in this file stay the content specs.

Local resources checked: raw scans for all 75 eyes (`masterthesis-docker/data/MUW_GA/scans`:
SLO, FAF, mask_global, mask_oct, layers, transforms), precomputes for splits 0-2 only, `last.pt`
for every fold-2 arm, `metrics.jsonl` + per-eye `mai/` records for every run, the native DMM
checkpoint `GA_NAT_O512x2_S1`, the `MPPDE` conda env (torch 2.7, PyG 2.6.1) and an RTX 3080.
Rollout NPZs exist only for two superseded runs (k-NN mean+max, dual branch), so rollout
figures need regenerated rollouts.

Planned in the text (9 placeholders + 2 appendix chapters), in working order:
- [x] App. G `fig:appendix:moved-mesh` -- done 2026-10-01 (`fig_appendix_moved_mesh.py`; eyes =
  lower quartile / median / upper quartile of baseline area among fold-2 validation eyes).
- [x] App. D additional rollouts incl. failure cases -- done 2026-10-01 (`fig:appendix:rollouts`,
  canonical model, folds 0-2; rules: highest / lowest per-eye Dice 0.775 / 0.246, most border
  pixels (833), fastest true growth 0.594 mm/yr). Short intro paragraph added. The failure-mode
  discussion for §5.6 (qualitative) is still open.
- [x] App. A cohort plots -- done 2026-10-01: `fig:appendix:cohort` (visits, intervals, baseline
  area, growth rate) and `fig:appendix:crop` (native grids, lesion area lost); every cohort
  number of Ch. 3 reproduced. Appendix A now has two short sections around them.
- [x] §5.2 `fig:experiments:rollout` -- done 2026-10-01. Rollouts regenerated from the epoch-29
  `last.pt` with the unmodified `train.test_rollout_losses` (`rollouts_regen.py`, cache in the
  git-ignored `images/data/rollouts/`); every arm reproduces its logged epoch-29 change-region
  Dice (U-Net +1.1e-5, all others exact; per-pixel floor identical to baseline at every step).
  Rows: ground truth, stencil, U-Net, T-FEN, FNO, k-NN (per-pixel floor dropped). Eye: fold-2
  index 8, median rule; the two middle eyes tie, the lower was taken (the other has a lesion of
  ~0.36 mm^2 and is barely visible) -- author may want to confirm. 5 of 8 follow-ups shown.
  - Finding: what the code calls "pad nodes" (all 11 channels at the normalised value of 0) is
    not only the crop's zero padding. Example eye: native grid 54 x 1356 at every visit, but
    20k-35k of 73k positions have all-zero layers, varying by visit (triangular areas). The
    figure therefore hatches "no data at this visit". Worth one sentence in §3.3 or §6.3: the
    "pad-aware" border definition and `--exclude_pad_nodes` act on these positions too.
  - Rollouts ran on the CPU: the GPU path ran out of host memory while another process held
    most of the RAM.
- [x] §4.3.3 `fig:method:stencils` -- done 2026-10-01 (`fig_method_stencils.py`).
- [x] (done 2026-10-18: TikZ `images/fig_method_pipeline.tex`, update loop only; author accepted) §4.1 `fig:method:pipeline` -- schematic (TikZ draft), needs author review.
- [x] (done 2026-10-20, see below) §3.1 `fig:data:example-state` -- Python from raw data; needs the author's decision whether
  a patient's SLO image may be printed.
- [x] (done 2026-10-20, see below) §2.2.2 `fig:bg:solver-path` -- schematic (TikZ draft), needs author review.
- [x] 2026-10-16 §2.1.1 `fig:bg:eye-anatomy` (Fig. 2.1) done with two openly licensed Wikimedia
  Commons images instead of an LLM drawing (author's choice): left Schematic_diagram_of_the_human_eye_en.svg
  (Rhcastilhos, Jmarchn; CC BY-SA 3.0; background made white), right Macula.svg (photo Danny Hope,
  diagram Zyxwv99; CC BY 2.0; unchanged). Credits with URLs in the caption; sources in
  `images/third_party/SOURCES.md`; script `images/scripts/fig_bg_eye_anatomy.py`. Caption corrected:
  the left panel is a *horizontal* section of a right eye, not a sagittal one. A 6 x 6 mm OCT-window
  overlay on the fundus was left out (its edges would cross the "macula" and "0.65 mm" labels); the
  caption says the window is slightly larger than the 5.5 mm macula drawn there.
- [x] (superseded 2026-10-16: Commons version replaced) Author to check Fig. 2.1 (page 18): the small labels of the right panel (distances, inset) are
  hard to read at 0.48	extwidth; the image also uses its own zone diameters (fovea 1.5 mm, parafovea
  2.5 mm, macula 5.5 mm), which the text does not quote. The style/ palette does not apply to
  third-party images.
- [x] (done 2026-10-16, see below) 2026-10-16 (author): Fig. 2.1 is to be redrawn as an own schematic after all (the Commons
  images stay in the text until then). Prompt for the external LLM, drawing only, no text, with
  label anchors exported as JSON: `prompts/PROMPT_fig_2_1_eye_anatomy.md`. Afterwards here: audit the
  anatomy against the prompt's table, add labels / leader lines / N-T marks from the anchors, rewrite
  the caption ("schematic", layer thickness not to scale, no Commons credits), and remove
  `images/third_party/` and the two `fig_bg_eye_anatomy_[ab].png` if no longer used. Open choice:
  the prompt suggests `jku_magenta` tints for choroid and vessels, which style/README calls "off by
  default".
- [x] (done 2026-10-16, see below) 2026-10-16 (author): the matplotlib route for Fig. 2.1 is dropped -- both returned scripts
  drew the cross-section wrong (layers missing at the back wall, macula as an arc in the vitreous,
  no fovea pit; vessels crossing the macula in one fundus); renders were only in the scratchpad.
  New route: image-generating model, one prompt per panel, no text, labels + 6 x 6 mm window +
  N/T marks added here in TikZ: `prompts/PROMPT_fig_2_1_eye_anatomy_imagegen.md` (with an anatomy
  checklist). Caption must state "AI-generated"; JKU rules and the tool's terms to be checked.
- [x] 2026-10-16 Fig. 2.1 done with two ChatGPT-generated drawings (cross-section: Downloads
  `eye_cross_section_left_panel.png`; fundus: `Detaillierte Netzhaut mit sichtbarer Papille (5).png`),
  kept unchanged and read-only in `images/raw/`. `images/scripts/fig_bg_eye_anatomy.py` adds the
  labels (anchors measured on the raw pixels), the macular zone circles (0.35 / 1.5 / 2.5 / 5.5 mm),
  the dashed 6 x 6 mm OCT window and the temporal/nasal marks, with the fundus scaled by a 4.5 mm
  fovea-to-disc distance (disc then ~2.0 x 2.5 mm). Output `images/fig_bg_eye_anatomy.pdf`, printed at
  135 mm. Caption rewritten (schematic, AI-generated, labels added by the author); the Commons
  images, their SOURCES.md and the two old panel PNGs were removed.
- [ ] TODO (Fig. 2.1 inline): JKU declaration of AI-generated figures -- supervisor asked, answer
  pending; check the image tool's terms. Both drawings confirmed as ChatGPT (author, 2026-10-16).
- [x] 2026-10-16 Fig. 2.1 sources added and cited in the caption: **Koksaldi2025** (Koksaldi, Kayabasi,
  Karti & Saatci, "Clinical anatomy of the macula", Med Hypothesis Discov Innov Ophthalmol 14(2):17-27,
  doi 10.51329/mehdiophthal1520, PMC12330045, CC BY-NC 4.0): macula lutea ~5.5 mm, fovea ~1.5 mm,
  parafovea ~2.3 mm, foveola ~350 um, perifovea "the outermost anatomical region of the macula".
  **Nair2021** (TVST 10(2):25, doi 10.1167/tvst.10.2.25, PMC7900853, CC BY 4.0): horizontal distance
  fovea to disc centre 4359 um in right eyes (4248 left), healthy subjects, Spectralis/Cirrus OCT.
  Bib entries checked against PubMed/Crossref; quotes checked in the Europe PMC full text. The figure
  now follows these values: parafovea circle 2.3 mm (was 2.5, the Polyak/Wikipedia convention) and
  scale 4.36 mm (was 4.5). Sources disagree on the zones (Tschulakow et al. 2018, PeerJ, citing Hogan
  1971: fovea 1.8 mm, parafovea 2.3 mm), hence "approximate" in the caption.
- [x] (done 2026-10-16, see below) Ledger for Koksaldi2025 / Nair2021: no local PDFs yet (PMC blocks scripted downloads). Download in
  a browser: PMC12330045 -> `pdfs/GA/Koksaldi2025.pdf`, PMC7900853 -> `pdfs/GA/Nair2021.pdf`; then
  `extract_text.py`, hub notes and the Phase 4 check (literature/_tools/README.md, step 4).
- [x] 2026-10-16 JKU rules on AI use checked (web + repo): no university-wide JKU rule found. Two
  institute-level policies, both business faculty: Institute of Strategic Management (27 May 2026) --
  tool and purpose disclosed in the methods chapter, by activity (literature, data analysis,
  arguments, writing support); Corporate Finance -- an AI-made figure or table gets a note in its
  caption/footnote, AI chatbots are "documentation-required", the sworn declaration for master
  theses follows the examinations office (the template notes it is now part of the submission
  process). Fig. 2.1 already carries the note in the caption. Supervisor asked (author, 2026-10-16).
- [ ] Decide (after the supervisor's answer) whether the thesis needs a general statement on AI tools
  used (image generation for Figs. 2.1-2.3, writing and coding assistants), e.g. in the front matter
  or the methods chapter.
- [ ] Author to review Fig. 2.1 on page 5 (label choice: ciliary body, iris, cornea, lens, sclera,
  choroid, retina, vitreous body, macula, fovea, optic disc, optic nerve; foveola to perifovea,
  OCT window). The vessels leave the disc slightly nasal of its centre, which is anatomically normal.
- [x] (done 2026-10-16, see below) 2026-10-16 Fig. 2.3 (`fig:bg:retinal-anatomy`) started, same route as Fig. 2.1: prompt
  `prompts/PROMPT_fig_2_3_retina_layers_imagegen.md` (panel A healthy layers around the foveal pit,
  panel B the same strip with a GA lesion: RPE, photoreceptors, ELM/EZ and choriocapillaris lost,
  INL/OPL subsidence, hypertransmission column, thickened RPE rim at the margin), with a checklist.
  Layer order after Abramoff2010 (local, p. 2-3) plus EZ/IZ/ELM and the cRORA features after
  Sadda2018 (p. 8, Fig. 2 legend); rim thickening after Chu2022. When the images are in: raw files
  to `images/raw/`, labels from measured anchors, caption with the AI note and these citations; the
  current caption sentence on the ten layer channels must not map strata onto channels.
- [x] 2026-10-16 Fig. 2.3 done (page 9, `[tp]` so it stays next to §2.1.3): panel (a) healthy strip
  (Downloads `Schematische Querschnittsdarstellung der Fovea.png`), panel (b) GA strip (`Retina mit
  zentraler Atrophie.png`, from a fresh ChatGPT chat after five rounds in the old one kept extra
  bands inside the lesion), both read-only in `images/raw/`. `images/scripts/fig_bg_retinal_anatomy.py`
  adds the 16 layer labels (anchors from colour scans, see the script docstring) and the signs
  (i)-(iii) of §2.1.3 plus "Bruch's membrane intact". Caption rewritten (abbreviations expanded, AI
  note) and cites Abramoff2010, Sadda2018, Chu2022, Boopathiraj2024; text references now say "(a)".
- [x] 2026-10-16 Figure-caption citations verified: PDFs filed as `pdfs/GA/Koksaldi2025.pdf` and
  `pdfs/GA/Nair2021.pdf` (from the author's Downloads), text extracted; hub notes `literature/Koksaldi2025.md`,
  `literature/Nair2021.md` and concept note `Macular_Zones_and_Landmarks.md` written; both registered in
  `_scratch/papers.json`. `update_ledger.py --apply` run (this also applied the pending re-indexing of
  the 2026-10-12..14 rewording). The 8 caption entries C023 (Koksaldi2025), C024 (Nair2021), C025
  (Huang1991), C036 (Abramoff2010, Sadda2018), C037 (Sadda2018, Chu2022), C038 (Boopathiraj2024) are
  SUPPORTED with quotes that pass verify_quotes on the cited page. Fig. 2.3 caption reworded: "the
  layers above it sink towards Bruch's membrane" -> "so the layers above it lie closer to Bruch's
  membrane" (Sadda describes subsidence for iRORA only; ONL thinning is the cRORA criterion).
  Ledger now 99 SUPPORTED, 44 NEW (unchecked), 55 CHANGED SENTENCE (recheck): those are the older
  pending batch (Phase 4 check still to run).
- [x] (done 2026-10-16, see below) Ledger: the new caption citations of Figs. 2.1 and 2.3 (Koksaldi2025, Nair2021, Abramoff2010,
  Sadda2018, Chu2022, Boopathiraj2024) enter with the next `update_ledger.py --apply` run; Koksaldi2025
  and Nair2021 need their PDFs first.
- [x] (2026-10-16, author) Author to review Fig. 2.3 (label choice; whether "CC"/"BM" abbreviations are fine).
  Outcome: short labels on the drawing plus an abbreviation key beside it; RPE/BM/CC dots moved onto
  their measured bands. Caption panel (a) shortened to point to the key; C036 (Abramoff2010,
  Sadda2018) re-verified, SUPPORTED.
- [x] 2026-10-16 Fig. 2.2 revised after author review (blurry block texture, leaders hidden under the
  block faces, thick outline, A-scan/B-scan in the block not readable): panel (a) now full size on top
  (native-resolution raw, labels drawn above everything, A-scan curve orange like the A-scan in (b));
  panel (b) full width below is the sequence A-scan -> B-scan -> volume (stack of B-scans) -> en-face
  view with one line per B-scan and a lesion, highlighted A-scan/B-scan/line corresponding, B-scans =
  the Fig. 2.3 strip at native resolution. Caption (b) and the §2.1.2 references rewritten; float
  `[tp]`, now page 7 (section starts page 6).
- [x] 2026-10-16 Fig. 2.2 done (page 6): `images/scripts/fig_bg_oct_acquisition.py`. Panel (a) =
  ChatGPT interferometer (`images/raw/fig_bg_oct_acquisition_raw_interferometer.png`) with labels
  (light source, beam splitter, reference mirror, reference/sample arm, eye, detector) and a
  schematic A-scan curve drawn in code; panel (b) = block in cabinet projection drawn in code,
  textured with the Fig. 2.3 healthy strip: front face = B-scan, top face = en-face view with scan
  lines and a lesion, orange line = A-scan, block = volume, footprint ~6 x 6 mm. Caption cites
  Huang1991 and states which parts are AI-generated; §2.1.2 now refers to (b) front face / (b) /
  (b) top face. The draft script and `prompts/HANDOFF_fig_2_2.md` are obsolete (handoff not needed,
  done in the same session); the draft was removed.
- [x] (done 2026-10-16, see below) 2026-10-16 Fig. 2.2 status: panel (a) interferometer accepted (ChatGPT, backed up as
  `images/raw/fig_bg_oct_acquisition_raw_interferometer.png`); panel (b) to be built in code
  (image models failed twice on the 3D geometry), prototype
  `images/scripts/fig_bg_oct_acquisition_block_draft.py`. Remaining work and context:
  `prompts/HANDOFF_fig_2_2.md`.
- [x] (done 2026-10-16) 2026-10-16 Fig. 2.2 (`fig:bg:oct-acquisition`) started: prompt
  `prompts/PROMPT_fig_2_2_oct_acquisition_imagegen.md`. Plan changed to two drawn panels: (a) Michelson
  interferometer with the eye (A-scan plot added in code), (b) 3D retina block with A-scan line,
  B-scan slice, volume and en-face top face. The old panel (d) "projection" is dropped (no projection
  is computed; real en-face maps belong to §3.1). When done: text references to panels (b)/(c) in
  §2.1.2 and the caption must be rewritten for two panels; cite Huang1991.
- [x] (done 2026-10-16; the retinal-anatomy remark below is also resolved) §2.1.3 `fig:bg:oct-acquisition` -- illustration, generated
  with the author. The retinal-anatomy caption
  names layer strata and maps them to the ten channels, which the 2026-09-25 decision forbids
  (boundary names unknown); a real B-scan is not in the repository.
- [x] (2026-10-16: Figs. 2.1-2.3 done with ChatGPT image generation, not LLM-written code; AI note in each caption; JKU rule still open, see the Fig. 2.1 TODO) **Illustrations via LLM (author, 2026-10-14; check when the illustrations are made):**
  Figs. 2.1-2.3 (eye anatomy, retinal layers, OCT acquisition) to be drawn by an LLM for a uniform
  look, with the author checking the anatomy. Rules: (1) the LLM writes figure *code* (TikZ / SVG /
  matplotlib with `style/` colours), no image generator; script in `images/scripts/`; (2) check
  against one named reference figure and say "schematic, after X" in the caption; (3) a close copy of
  one published figure is an adaptation: "adapted from X" + licence check; (4) Fig. 2.2 must not map
  layers onto the ten channels, and a drawn B-scan is labelled as a schematic, not shown as data;
  (5) check JKU rules on declaring AI-generated figures (ask the supervisor). Supervisor SV-2.3
  allows licensed third-party images as an alternative. 2026-10-16: Fig. 2.1 took that route (Commons images, see above);
  the LLM rules now concern Figs. 2.2-2.3 only.
- [x] (2026-10-19: superseded by the real FAF figure below; author: no schematic needed for now)
  Not yet in the text: GA progression stages from the poster (`poster/figs/eye_stage_1-4.png`),
  e.g. in §1.1 or §2.1.2 -- placement to be decided.
- [x] 2026-10-19 **Fig. `fig:bg:ga-faf` done** (`images/fig_bg_ga_faf.png`, script
  `images/scripts/fig_bg_ga_faf.py`): PEAT0021_OD, days 0 and 1080, rank 1 of 26 eyes passing the
  rule, chosen by the author over rank 3 (PEA00039_OD, textbook large lesion) and rank 2
  (PEA01821_OD, rejected: dark artefact over the later image). Frame checked (T_mask IoU 1.000; mask
  on the FAF lesion edge within 2 px, 26 visits). Window = 49 x 1024 modelling window, dashed blue
  on a white halo, labelled "≈ 6 × 6 mm" (no scale bar, author). Simple caption; referenced in §2.1.2 (FAF), §2.1.3
  opener, §2.5.1 (growth at the margin), §3.1 (FAF annotation) and §3.3 (window). The spec entry
  below is kept as history.
- [x] 2026-10-19 (author): **§2.1.2 `fig:bg:ga-faf`** -- what GA looks like on a real eye, from the
  MUW FAF images (`data/MUW_GA/scans/<eye>/<day>/faf_global.png`). Placeholder + spec in
  02-background.tex after the FAF paragraph; referenced there and in the §2.1.3 opener. (a) baseline,
  (b) same eye ~3 years later, grey, each image stretched on its own (1st-99th percentile; a
  common window would mislead, since FAF brightness differs per acquisition: median grey 82 vs 110
  in the scratch candidate), caption says brightness is not comparable between panels, dashed OCT
  field of view, scale bar, no mask overlay. Before drawing: check that `faf_global.png` shares the frame of `slo_global.png` /
  `mask_global.png`; fix an eye rule in the script (lesion inside the window, median growth,
  follow-up >= 3 y; scratch candidate GX511402_OS days 0 / 1080), author confirms the eye; then fill
  the caption's interval and describe only what that eye shows. Script
  `images/scripts/fig_bg_ga_faf.py`. Earlier there was no figure showing GA on a real eye (only the
  schematic Fig. 2.3(b) and the still unbuilt `fig:data:example-state`).
- [x] 2026-10-20 **Chapters 1-4 have no figure placeholders left.** (i) `fig:bg:solver-path` (Fig. 2.5,
  p. 15): TikZ `images/fig_bg_solver_path.tex`, one dimension -- field u(t_k, x) with the cell centres
  as dots -> seven cells u^k, cell i orange, its stencil framed blue -> f_i -> time-step box (Euler) ->
  u^{k+1}, dashed loop "rollout"; cell values illustrative (caption says so); caption names stencil and
  time step as independent choices. (ii) `fig:data:example-state` (Fig. 3.1, p. 25):
  `images/scripts/fig_data_example_state.py`, PEAT0021_OD day 0 (= first visit of `fig:bg:ga-faf`):
  (a) SLO with the 49 x 1024 window (via T_mask) and the mask_global outline, (b) channel 0 on the
  window at physical aspect (native 38 x 1059 -> 22.4 % zero pad, hatched), (c) channel 1 (ILM) depth
  map with the lesion outline; IoU mask_global vs mask_oct 1.000. Caption: ILM deeper inside the
  lesion (median 114 vs 83 axial px), retina thinner there (channel 10 - 1: 66 vs 83).
- [x] 2026-10-20 (author): Fig. 3.1 now shows the visit on both fundus images, captioned by modality:
  (a) near-infrared SLO (lesion bright; the other bright spots are not dark on FAF and not part of the
  annotation), (b) FAF (lesion dark, the image it was annotated on), (c) mask, (d) ILM depth. Reason:
  with Fig. 2.3 a reader could take every white spot on the SLO for GA. Brightness inside / ring:
  SLO 124 / 93, FAF 63 / 90. §3.1 sentence reworded.
  Later the same day (author): order swapped to (a) FAF, (b) SLO; each panel now carries its title
  (FAF / Near-infrared SLO / Binary GA mask / ILM depth map).
  Eye changed (author, "this maybe"): PEAT0058_OD day 360 instead of PEAT0021_OD day 0, because
  the dark area of the ILM map did not follow the lesion well. Ranking: overlap (Dice) of the N deepest
  ILM pixels with the lesion (N = lesion size), visits whose lesion does not touch the window edge:
  chosen 0.87, old 0.62, cohort median 0.64; six candidates rendered. No zero padding at this visit;
  the caption no longer links the figure to Fig. 2.3. Caption numbers recomputed (SLO 88 / 62, FAF
  25 / 47; ILM 132 vs 102 axial px; thickness 56 vs 74).
- [x] 2026-10-20 Fig. 2.5 redrawn (author: the TikZ version was unclear; asked for continuous field ->
  discretised grid -> stencil with its formula -> how the rate is used by the solver, with a hint that
  any time-stepping wrapper can use it). Now `images/scripts/fig_bg_solver_path.py` -> PDF, six
  panels in two rows: (1) continuous field, (2) grid values at the cell centres, (3) stencil
  f_i = sum alpha_j u_j / dx^2 with weights +1/-2/+1, (4) rates f_i for every cell, (5) time stepper
  box (Euler / RK4 / any scheme that calls f), (6) next state with the old values dashed; dashed
  rollout arrow back to (2). One real step, illustrative values (9 cells, dx = 1, dt = 0.3). The TikZ
  file `images/fig_bg_solver_path.tex` was removed. Author to review.
  Second redesign the same day (author: no rollout arrow; explain where the weights and dx come from;
  link the rates, the time step and the next state visibly): zig-zag 3 x 2 layout, right column
  (grid / rates / next state) on one shared x-axis, left column works out cell i -- (3) parabola
  through the three values, dx marked, weights +1/-2/+1 in the bars, neighbours' mean as a line,
  formula with the numbers (0.61 - 2 * 0.90 + 0.61 = -0.58); (5) Euler with the numbers
  (0.90 + 0.3 * (-0.58) = 0.73, from the rounded values shown); (6) arrows dt * f_i per cell. A 2-D
  draft (five-point stencil) was tried and rejected by the author (harder to read).
  Third pass (author): connector arrows removed; transitions named in the panel titles (Discretise /
  Stencil at cell i / Slide the stencil / Time step); no numbers in the stencil or time-step panels;
  stencil panel labels u_{i-1}, u_i, u_{i+1}, weights in the bars, dx, formula with explicit weights;
  panel 4 shows u^k with the stencil window at cells 1, 4, 7 linked to their rates. Rest still to
  discuss with the author.
  Fourth pass (author): parabola removed; formula 1/dx^2 sum_j alpha_j u_j with a real fraction; bars
  carry alpha_{i-1}, alpha_i, alpha_{i+1} instead of numbers; panel 3 split: left classical stencil
  ("alpha_j fixed"), right the GNN intuition (nodes, messages phi_theta along the edges, update psi_theta,
  f_i = psi(u_i, sum_j phi(u_i, u_j)), simplified from Eqs. 4.3-4.4; "learned"). The MP-PDE paragraph
  of 2.3 now points to panel 3. Float set to [!t] to keep it on p. 15 next to its text.
  Fifth pass (author: learned stencil as its own panel, general concept rather than GNN notation):
  six panels row by row -- 1 field, 2 discretise, 3 classical stencil (f_i = 1/dx^2 sum alpha_j u_j,
  "weights fixed"), 4 learned stencil (same sum, alpha_j(u; theta), weights in orange-tinted boxes,
  grey lines from the three values into a theta box; caption: message-passing networks go further),
  5 slide the stencil -> rates, 6 time step with next state (Euler formula; RK4 note). 2.3 points to
  panel 4. Shared-x-axis column given up (panel 5 carries its own u^k strip).
  Fact check and fixes (author asked whether it is still correct): learned stencil checked against
  Bar-Sinai et al. (2019, p. 3: coefficients output by the network, depending on the field values in
  the neighbouring cells; a generalisation of ENO/WENO); caption now says (i) the stencil output is the
  rate only for the diffusion equation du/dt = d2u/dx2, in general F turns the derivative into the rate;
  (ii) a standard stencil uses the same weights at every cell, WENO already varies them (panel 3 title
  "Standard stencil"); (iii) panel 5 applies the same rule (fixed weights or the same network), the
  learned weights differ per cell; (iv) 1/dx^2 is written outside the sum, unlike Eq. 2.3. Also more
  space between bars, note and formula in panels 3-4, and one orange arrow "learn the weights" from
  panel 3's weights to panel 4's. Simplification left as is: panel 4 draws the network reading only
  the three stencil values (Bar-Sinai: 6-point stencils, wider input).
  Final (author 2026-10-20: "good like this"): orange arrow removed; caption panel (4) now cites
  BarSinai2019 (ledger C054 SUPPORTED, p. 3, quote checked by hand, PASS). Mai2024 C101 rechecked
  (only the figure pointer was added; SUPPORTED).
- [x] (2026-10-20, author: fine; nothing in either repo restricts printing dataset images) Author to
  review Fig. 3.1 -- image permission part. The layer choice for panel (d) is the next item.
- [x] **Fig. 3.1 panel (d): ILM probably shows the foveal pit, not the lesion (checked 2026-10-20,
  scratchpad scripts `layer_contrast.py`, `fovea_split.py`, render `images/data/layer_candidates_PEAT0058_OD_360.png`,
  git-ignored).** Candidates: all ten channels plus the thicknesses named in §3.2 (total retina ch10-ch1;
  inner retina ch5-ch1; INL ch5-ch4, Ebneter; ONL+HFL ch7-ch6, Vogl; photoreceptor OS ch9-ch7; RPE-PR
  complex ch10-ch7, Vogl; outer retina ch10-ch6; RPE ch10-ch9, Chu). Scores over 553 visits (AUC lesion
  vs rest / vs a ring of rows +-2 x cols +-50; Dice of the N most extreme positions): every boundary lies
  deeper inside the lesion, the outer RPE too (global AUC 0.79), so absolute depths partly reflect scan
  curvature/position; best channel ILM (0.83 / 0.79, Dice-N 0.64); best overall RPE-PR complex ch10-ch7
  (0.84 / 0.76, Dice-N 0.68). At PEAT0058_OD/360 the INL thickness is ~0 inside the lesion and the
  total thickness shows a thin centre with a thicker ring, i.e. the lesion sits on the fovea and the deep
  ILM is largely the foveal pit; the visit was itself picked by the ILM rule. With a crude fovea proxy,
  on the 64 visits whose lesion is off the fovea the ring AUC falls to 0.68 (ILM), 0.53 (total), 0.50
  (INL) but stays 0.73 for the RPE-PR complex. The caption sentence "The membrane lies deeper inside
  the lesion, where the retina is thinner" is misleading as it stands. Options to decide: (i) panel (d) =
  RPE-PR complex thickness (derived from channels 7 and 10, caption changed accordingly; matches the
  definition of GA as RPE + photoreceptor loss) with a new eye rule; (ii) keep the ILM and reword the
  caption (foveal pit).
  Follow-up (author asked whether total thickness works and whether its ring is RPE-BM thickening;
  `rim_decomp.py`): at PEAT0058_OD/360 total thickness by distance from the lesion is 56 (inside) /
  71 / 76 / 79 / 80 / 77 / 72 / 68 px at 0-150 / 150-300 / 300-600 / 600-1000 / 1000-1500 /
  1500-2500 / >2500 um. The ring (peak 300-1000 um, +12 px over far) is entirely inner retina
  (ch1-5: 39 vs 27 px); RPE ch9-10 is 6 px (~23 um) at every distance, ONL flat at 23-24 px. So the
  ring is the normal parafoveal thickness peak, not RPE-BM thickening (Chu R1 mean ~11 um, ~3 px).
  Cohort, rim 0-300 um minus 600-1500 um: RPE ch9-10 change > 0 in 2 % of the 64 off-fovea visits.
  Total thickness has no lesion contrast off the fovea (ring AUC 0.53).
  **Decided 2026-10-20 (author):** keep the ILM; the caption of (d) now names both causes of the dip,
  each pointing to existing text (subfoveal §2.1.1; foveal pit Fig. 2.4a; outer-retinal loss §2.1.3).
  The sentence "most of the dip comes from the pit" was left out (author). Item closed.

- [x] Chapter 5 data figures (author approved all eight, 2026-10-01), all in the text with a
  referencing sentence, every plotted value checked against the text: `fig:experiments:curves`
  (§5.1.3 + §5.4.2), `:arms-folds` (§5.2), `:reach` (§5.3.2), `:horizon` (§5.3.3/§5.3.4, with
  Mai), `:capacity` (§5.4.3), `:swap` and `:tfen-stability` (§5.5), `:growth-rate` (§5.6.1).
- [x] (done 2026-10-02; figure still disabled) TODO: switch `fig_experiments_capacity.py` to `TFEN_FORM = 'skew'` together with the
  table rows once width-192 and depth-8 skew are complete.

Text corrections made while building the figures (2026-10-01), each verified against the run
records and documented in a LaTeX comment at the place:
- Reach table/text: the ±35 geometry keeps the spacing (pitch 7, 32 neighbours); the ±42 one
  keeps 20 neighbours (pitch 14). The text had "same number of neighbours" for ±35.
- "31.1 % of the cropped lesions touch the crop border" (§2.1.6, §3.3, §6.3) -> in 31.1 % of
  the visits (172/553) the lesion touches the edge of the imaged field inside the window
  (window border or, for padded visits, the scan edge). True crop-edge contact alone: 28.4 %.
- §5.1.3: epoch-to-epoch sd "0.02 to 0.10" -> "about 0.01 to 0.05" (late epochs, per fold,
  Table 5.1 arms 0.005-0.047). Learning-rate reductions take effect from epochs 5 and 20
  (0-based), not "after epoch 5" (also fixed in §4.5).
- §5.3.4: k-NN first-year growth-region Dice 0.393 -> 0.397 (0.393 was the retired mean+max
  arm). Also stale in the 2026-10-01 entry above and in SOLVER_FINAL_RUNS §9.20 (code repo).
- §5.3.4: removed "whether its velocities stay within the stability limit has not been read
  back" (the read-back exists, §5.5.2).
- §5.4.2: the soft-Dice steadiness claim ("about three times") is carried by fold 4 (escape at
  epoch 12); folds 0-3: 0.017 vs 0.013. Rewritten.
- §5.4.3: four double-rounded cells fixed (0.520, 0.015, -0.020, -0.090; text 0.520);
  "does not train on any fold" -> "trains poorly"; "about a quarter" -> "between about a sixth
  and a third"; the width-192 divergence is no longer attributed to the Galerkin crop-edge
  defect, because the skew form fails on the same folds 1 and 4 (Dice 0.054 / 0.028, NaN
  training loss; folds 3-4 at 29 of 30 epochs).
- §5.6.1 Table 5.6: bootstrap intervals r [0.22, 0.56] -> [0.20, 0.57], AUC10 [0.52, 0.91] ->
  [0.53, 0.91], AUC15 [0.53, 0.86] -> [0.53, 0.85] (no percentile bootstrap reproduced the old
  ones). Also stale in the "#20" entry above. Added: 14 of the 15 fastest eyes are
  under-predicted (median predicted/true 0.50).
- §3.1: baseline-area range/median/IQR added with a pointer to Appendix A; quantiles are
  nearest-rank (linear interpolation gives 0.157-0.337 / 0.461 for the growth rate).
- Not changed, for the reporting-scheme pass: the reach table caption counts folds "with the
  sign of the mean" but its numbers count folds where the variant is higher (known TODO);
  ±35 per eye is t = -2.8 (19/75), "under the floor" holds for the fold-paired instrument only.
- Pre-existing, not from this work: "Float too large for page by 79.7pt" in Appendix E.

### Author's tablet review of the whole thesis (2026-10-02)

Sixth handwritten review (build of 2026-10-01), decoded from
`main-thesis_v6_261001_235732.sdocx`: 21 marks on 18 pages (title page, abstract, Ch. 1-5, 7,
App. D). Blue = rewrite, red = wrong/remove. Overlay PDF in the session scratchpad only. Being
worked through one item at a time.

- [x] Author decision (2026-10-02, not from a mark): **all 14 generated figures are disabled**
  (Fig. 4.2, 5.1-5.9, A.1, A.2, D.1, G.1): each `\includegraphics` line is commented out with a
  `% TODO: figure not final (2026-10-02); restore the line above when ready.` marker and replaced
  by a placeholder box; captions and labels unchanged. Scripts and image files are untouched.
- [x] (2026-10-21: all handled -- restored, redrawn or removed) TODO (14 inline markers above): restore each figure once it is final.
  2026-10-17: Fig. 4.2 (`fig:method:stencils`) restored (redrawn); Fig. A.1
  (`fig:appendix:cohort`) restored unchanged (author: fine); 12 left. Fig. A.2 (crop) and
  Fig. 5.3 (reach) need more work and discussion (author).
  2026-10-19: Fig. G.1 (`fig:appendix:moved-mesh`) restored unchanged (author: fine; caption
  checked against the PNG of 2026-10-01). Still disabled (8): reach, horizon, capacity, swap,
  T-FEN stability, growth rate (author: later; only the in-plot text needs moving to the
  caption), App. A crop, App. D rollouts.
  2026-10-21: `fig:experiments:swap` restored (redrawn). Still disabled (7).
  2026-10-21: `fig:appendix:rollouts` restored (redrawn, see below). Still disabled (6): reach, horizon,
  capacity, T-FEN stability, growth rate, App. A crop.
  2026-10-21: `fig:experiments:tfen-stability` restored (author): one line per form, geometric mean over the
  five folds with one SD of the log error shaded; caption says the criterion is applied per fold (Table 5.6).
  Drawn and not chosen: median + range, worst fold per epoch (the mean puts the Galerkin line near the
  threshold, although 4 of 5 folds fail). Still disabled (5): reach, horizon, capacity, growth rate, App. A crop.
- [x] 2026-10-21 (author) **New Fig. `fig:method:fen-toy` in §4.3.6** (`images/scripts/fig_method_fen_toy.py`): the T-FEN
  transport operator assembled as in fen.py on a 10 x 60 toy grid, velocity (0.2, 1.0) + noise per triangle, both forms
  integrated exactly from the same random start (sd 0.1) to time 10. Galerkin grows to 145 at the left (inflow) edge,
  interior <= 11.8, largest eigenvalue real part +0.595; energy-conserving stays <= 0.39, real parts < 1e-15. Robustness
  (scratch, five velocity seeds): 61-80 % (median) of the 10 fastest Galerkin modes lie in the outer 5 columns each side
  (17 % of the grid). Caption relates it to the trained Galerkin T-FEN (§5.6.2); §5.6.2 points to it. Not used: an
  eigenvalue/mode-profile figure (author: hard to read) and an error-vs-distance plot on real data
  (`images/scripts/tfen_edge_error.py`, cache `images/data/tfen_edge/`, fold 0, both forms reproduce their logged Dice).
- [x] (2026-10-21, author: yes; added to §5.6.2 after the onset sentence) Open (author): add the onset sentence to §5.6.2? From `tfen_edge_error.py`, fold 0, epoch 29: the Galerkin form
  exceeds a per-pixel layer error of 5 in all 20 eyes (first at visits 539-1079 d); in 14 of 20 the worst pixel at that
  visit lies within 7 columns (40 um) of the left/right field edge, a band holding 1.4 % of the grid; the
  energy-conserving form never exceeds 5. Proposed wording: "In 14 of the 20 eyes of fold 0, the first error above 5
  lies within 40 um of the left or right edge, a band that holds 1.4 % of the grid."
- [x] 2026-10-21 `fig:experiments:growth-rate` restored unchanged (author: "as it was", in-plot r and identity
  labels kept). Checked on the way, not in the thesis (author: include nothing): r without the 15 fastest eyes 0.32
  [0.10, 0.52] (mean true 0.204 vs predicted 0.205); r among the 15 fastest 0.18 [-0.26, 0.61], median predicted/true
  0.50. Largest over-prediction fold 4 eye 8 (1.24 mm^2, true 0.27 vs predicted 0.58 mm/yr). Still disabled (4):
  reach, horizon, capacity, App. A crop.
- [x] 2026-10-21 `fig:experiments:capacity` **removed** (author): every version (old delta + SE plot, absolute
  lines, zero-centred with noise band, dot strip) either suggested trends the numbers do not support (U-Net
  0.488 -> 0.505 -> 0.508 is within noise; the width-192 T-FEN 0.552 is a 3-fold mean, +0.001 paired) or needed
  much explanation. §5.5.3 now points to Table tab:experiments:capacity only. Script kept. Still disabled (3):
  reach, horizon, App. A crop.
- [x] 2026-10-21 `fig:experiments:horizon` restored unchanged (author: "it looks fine"); caption unchanged. Script
  check list updated (k-NN 0-1 y 0.393 -> 0.397, the reported mean-aggregation arm). Not in the text, for reference:
  first-year growth-region Dice FNO 0.446, U-Net 0.458, FNO + 3x3 0.464. Still disabled (2): reach, App. A crop.
- [x] 2026-10-21 `fig:experiments:reach` **removed** (author: looks bad, no clear purpose): Table tab:experiments:reach
  gives the numbers, Fig. fig:method:stencils the geometry, the text the +0.064 over k-NN. The §5.3.2 pointer sentence
  was removed with it. Script kept. Still disabled (1): App. A crop.
- [x] 2026-10-21 `fig:appendix:crop` restored with panel (a) only (author: (a) fine, (b) not good); the lesion-loss
  curve and its in-plot numbers (incl. "19.2 % lose > 1 %", not in the text) dropped; caption and the App. A.2
  sentence rewritten for one panel. **All disabled figures are now handled** (restored, redrawn or removed); the
  14-marker TODO of 2026-10-02 is closed.
- [x] 2026-10-21 **App. D rollouts redrawn and restored** (author): the figure now shows kinds of lesion on which the
  model works instead of failure cases. Pool: folds 0-2 minus the Fig. 5.2 eye, change-region Dice at the anchor
  >= median (0.544), lesion not touching the border (15 eyes); rules smallest area / largest area / most lesions /
  fastest growth -> PEAT0062_OS (1.3 mm^2, 0.649), GX511418_OD (13.2 mm^2, 0.659), GX511414_OD (7 lesions, 0.640),
  PEA01810_OS (0.42 mm/yr, 0.552). Yearly columns only, each eye cropped to its lesion with its own scale bar (panels
  about twice as large; full page, D.1). The selection rule is stated in the Appendix D text, not in the caption
  (author). Text names three visible weaknesses (late over-prediction in (a), missed new satellite lesions in (c),
  under-predicted fast growth in (d)) and points to §5.4 and §5.7. Fig. 5.2 caption no longer promises "typical and
  difficult" eyes. Fixes the stale MAIN_FIG_EYE (panel (a) had become the Fig. 5.2 eye).
- [x] #1 title page keywords: MP-PDE, MM-PDE and moving mesh removed, U-Net added
  (2026-10-02). Now: Geographic Atrophy, OCT, neural PDE solvers, graph neural networks, U-Net,
  medical imaging, longitudinal prediction.
- [x] #2-#4 abstract: "Only the operator f_θ varies … matched parameter counts" marked
  "different"; bar along the results paragraph; "This whole thing reads terribly ?!".
  Done 2026-10-02 (English and German): the slot sentence now starts from the slot ("It was
  filled in turn, at matched parameter counts, with operators from four families: …"); the
  results paragraph is split into a framework paragraph (spatial context needed, per-pixel
  model = persistence, loss must emphasise the mask, RK4 and model size no gain) and an
  operator paragraph (three strongest from three families; reach explained by the 21:1
  spacing, ±0.011 mm k-NN hop vs ~0.07 mm front advance; stencil +0.064; transport +0.062;
  the two carrying these properties are the two highest). Dropped: the spectral / local-path
  sentence, "the largest effect", "the same deficit". English fits on one page again.
  Follow-up (author, 2026-10-02): a headline paragraph now comes before the two answers --
  the framework and its operators forecast individual lesions; strongest operator 0.54 ± 0.04
  at one year (persistence 0); its growth-region Dice above 0.5 in every year since baseline,
  also beyond 3 y (Table 5.7: 0.519 / 0.602 / 0.633 / 0.611); growth speed weaker (r 0.40).
  The next two paragraphs open "For the framework, …" / "For the operator, …"; the separate
  closing take-away was folded into "What separates operators is reach". FNO "with and
  without a local path" dropped from the operator list. German mirrored.
- [x] #5 §1.2 "and is tested in this thesis" (covariates) -- "is it though". Clause removed
  2026-10-02 (the covariate ablation is commented out; §6.3 calls their value unsettled).
- [x] Abstract (EN/DE): growth-speed sentence (r 0.40) removed at the author's request
  (2026-10-02); the author accepts the abstract as it now stands.
- [x] #6 §1.3 "organised around a single question" -- "a single" circled, "?". Now "This thesis
  addresses one question, divided into two parts:" (2026-10-02, author chose option A; matches
  Ch. 7 "It was split into two parts").
- [x] #7 §2.2.2 "which holds the rate constant over the step" -- "is this not why we have a
  linear line, [?] speed?" Author's question: could the constant rate of one Euler step explain
  the weak growth-speed prediction? Answered 2026-10-02, no change: the operator also receives
  Δt (removing the ×Δt multiplication changed nothing, §5.4.1), and the RK4-integrated arms,
  which do not hold the rate constant, reach r 0.30 / 0.31 against 0.40 (Appendix E, Table
  tab:appendix:growth-speed). Author: fine, move on.
- [x] #8 end of §2.2.3 -- "few sentences! what does understanding these yield / is this
  already somewhere?" Author: meant for §2.2 as a whole -- the reader should be told why they
  need the numerical-solver section. Done 2026-10-02: the §2.2 opening now names where the
  mechanisms are used (Euler step in residual form = the framework's update; learned stencils,
  global spectral methods and finite elements = the operators; reach, higher-order integrator
  and stability = what Chapter 5 asks), without previewing results.
- [x] #9 §3.4 "a hard step at the lesion edge" -- "future: the continuous distance from lesion
  experiment". Done 2026-10-02: new §6.4 paragraph "A continuous representation of the lesion"
  (signed distance to the boundary instead of the binary step; untested).
- [x] #10 §3.7 empty test split -- "no test because lack of data". Done 2026-10-02: the split-file
  mechanics replaced by the reason (75 eyes / 51 patients: a held-out test set would leave too few
  eyes for training and for a reliable test; every eye is a validation eye in exactly one fold).
- [x] #11 §4.1 provenance sentence (MP-PDE/MM-PDE suggested by the clinical partner) -- "we can
  absolutely not write this". Done 2026-10-02: removed; Chapter 4 now opens "This chapter answers
  the first part of the research question: what kind of framework the forecast needs." (also
  closes the editorial point that Ch. 4 never names sub-question 1). THESIS_STRUCTURE.md §1.3
  updated so the note does not come back.
- [x] #12 Fig. 4.2 -- "here I was thinking more like this" + sketch, "just the stencil" (the
  two neighbourhoods in grid indices, like the inset). Done 2026-10-02 (author: caption only, the
  figure is not displayed): caption rewritten for two plain grid-index panels (k = 12 diamond;
  dilated stencil rows -1/0/+1 x columns 0, ±7, ±14, ±21; mm reach in the caption); the redraw
  spec is a TODO above the figure. The existing PDF must be redrawn before re-enabling.
- [x] #13 Ch. 5 opener -- "Behaviour beyond 1 year analysis / yearly bins → when we do this →
  show that TFEN becomes really bad after some time, therefore the graph canonical". The data
  show a milder picture (T-FEN = stencil over 0-3 y, 0.611 vs 0.655 beyond 3 y, descriptive;
  energy-conserving T-FEN stable 10/10 with a small mask residual from ~day 1 260). Done
  2026-10-02 (option A): new §5.2 paragraph giving three reasons why the stencil network is the
  canonical model despite the T-FEN's higher anchor score -- small lead (+0.017 at both seeds)
  that does not persist beyond three years; ~4x training time (367 vs 91 s); long free-running
  rollouts numerically delicate. Author: the chronology (stencil fixed before the T-FEN existed)
  must NOT be given as a reason.
- [ ] Optional (from #13, option B, not chosen for now): a subsection "Behaviour beyond one year"
  with yearly bins for every main operator (hybrid, k-NN, free-form FEN still to compute from the
  mai/ records) and a per-eye test of the > 3 y difference.
- [x] #14 §5.1.4/§5.2 -- "I thought it was agreed only to report one seed and have the second
  in appendix E" (= the reporting-scheme pass #23/#25/#31 above). Done 2026-10-02, see there.
- [x] #15 §5.4.2 heading "Is the weighting of the mask channel needed?", #16 §5.5.2 "The
  energy-conserving form.", #20 Ch. 7 "The framework." -- the author dislikes the run-in
  paragraph headings. Done 2026-10-02 (author: remove them in §5.4, §5.5, §6.2, §6.3, Ch. 7 and
  smooth the transitions): all 24 `\paragraph{}` headings there removed; each paragraph now opens
  with a sentence that carries the topic ("The first test asks whether …", "For the first part,
  …", "The evaluation has limits of its own.", …). Fixed on the way: §5.4.2 intro no longer says
  each run changes one part (the first removes weighting and soft-Dice; editorial 5c.11); §5.5.2
  "Its accuracy" now explicitly the energy-conserving form at seed 42 (editorial 5d.16); Ch. 7
  "without the weighting" -> "trained with a plain mean squared error", and "It is the largest
  effect in the project" removed from the reach bullet (the transport bullet below gives +0.072);
  §6.4 "about a third of the cropped lesions" -> "almost a third of the visits" (31.1 % of visits,
  correction of 2026-10-01 missed there). §6.1 and §6.4 keep their headings (not on the list).
- [x] (2026-10-20, dropped by the author) #18/#19 "Figure 5.7:" / "Figure 5.8:" -- highlighted without
  comment. In the build of 2026-10-01 these were the old solver-swap figure (since replaced by the
  step-size ladder, to be redrawn) and the T-FEN stability figure; both disabled, both reviewed afresh
  when they come back.
- [x] #17 §5.7 GPU-sharing sentence -- red, "remove". Removed 2026-10-02.
- [x] #21 Fig. D.1 panel (b) "Lowest Dice" -- red cross, "absolutely not". Done 2026-10-02:
  rule removed from `images/scripts/fig_appendix_rollouts.py` (three eyes now; the other picks
  are unchanged: fold 0 eyes 10, 19, 14), PNG re-rendered in the MPPDE env (figure still
  disabled), Appendix D text and caption updated ("three further eyes"; the failure-pattern
  sentence now describes the fastest-growing eye only). The legend still lists "No data at this
  visit", which no remaining panel shows -- drop it when the figure is re-enabled.
- [x] 2026-10-02 (author): "the largest effect in the project" removed from §5.3.2 as well (abstract
  and Ch. 7 already); the transport term against its matched control (+0.072) is larger. §6.1
  "the weighting of the mask channel decided" -> "whether the loss emphasised the mask decided"
  (the plain-MSE run removed weighting and soft-Dice).

### Supervisor review 1 (Dmitrii Lachinov, 2026-10-12)

First official review, `main-thesis_dl_rev1.pdf` (build of 2026-10-02): 28 PDF comments, all on
the abstract and Chapters 1–3 (pp. 2–34). Consolidated list, matched against the AI editorial
review: `reviews/supervisor-rev1-2026-10-12.md`. To be worked through chapter by chapter.
His e-mail of the same day: the rest of the review follows next week; the abstract must be
polished to near perfection; do a prerequisite audit (every medical term defined before use);
opening chapter = medical background → PDEs and solvers (no GA) → motivation → formal problem
statement with notation and equations → outline; no question in headings ("Why Neural PDE
Solvers?"); contributions back as bullet points. He offers a meeting.
- [ ] Ask the supervisor: "neural solver" (PDF) vs "parametric neural operator" (e-mail).
- [ ] **Reply mail to the supervisor -- points to mention:** (1) "operator" is kept but now defined
  once (first use in 1.2: "In this thesis, this map is called the operator"; formal definition in
  2.5.2: general sense, a map from one state to a later one, not the narrow neural-operator sense of
  FNO/DeepONet); ask whether that resolves his "neural solver" comment. (2) Introduction and
  Background were deliberately kept as separate chapters (author's preference); his ordering is
  followed inside them: medical background (anatomy -> imaging -> GA) -> PDEs without GA -> neural
  solvers -> related work -> motivation and formal problem statement at the end of Ch. 2.
  (3) Drugs, patient management and the need for predictive methods stay in §1.1 (Clinical
  Motivation) rather than in the medical background of §2.1, as his outline suggested (author,
  2026-10-14); ask whether that is fine. (4) Ask about JKU rules for declaring AI-generated
  figures (the anatomy schematics are planned as LLM-drawn code figures). (5) Layer segmentation:
  the Iowa Reference Algorithms segment eleven surfaces, the data hold ten boundary maps -- which
  ten, and their names? (§3.2 now cites the Iowa software as he suggested.)
- [x] (done 2026-10-14) 2.5.2: include the formal definition of "operator" (wording agreed 2026-10-13, see
  `reviews/supervisor-rev1-2026-10-12.md`).
- [x] 2026-10-12 restructure of Ch. 1-3 (author approved; plan and figure in
  `reviews/structure-proposal-2026-10-12.md`), moves only, no wording changed, verified by a
  line-multiset check (only headings differ) and a clean build (112 pages, no new warnings).
  Introduction and Background stay separate chapters. Ch. 1: Clinical Motivation / Aim of the
  Thesis / Contributions / Outline. Ch. 2: Medical Background (Eye Anatomy, Retinal Imaging with
  the en-face paragraph, Geographic Atrophy) / PDEs and Numerical Solvers / Neural PDE Solvers
  (former 2.2.4 now opens it) / Related Work / Modelling Approach and Problem Statement (2.5.1 =
  former 1.2 data properties + 1.3 PDE argument + 2.2.5; 2.5.2 placeholder). Former 2.1.5 and
  2.1.6 appended to 3.2 and 3.1. All labels kept. Defaults taken for the open choices: problem
  statement at the end of Ch. 2, drugs stay in 1.1, research question in Ch. 1, Related Work
  before the problem statement.
- [x] (done 2026-10-13/14, every change signed off by the author; see the next entries) Wording pass after the restructure (inline `% TODO (restructure 2026-10-12)` markers):
  Ch. 2 opener and the 2.1 roadmaps (02 l. 16, 130-138) still describe the old order; 2.2 opener
  still about GA; bridge into 2.3; 2.5 opener; 2.5.1 "The next section motivates ..." and a
  self-reference to its own section; de-duplicate the moved blocks in 3.1/3.2 (Ch. 3 now refers to
  itself in l. 225, 300, 482); Aim/Contributions bridges and bullets; 06-discussion l. 97
  ("Chapter 1 leads one to expect") now points at an argument that sits in 2.5.1.
- [x] 2026-10-14 2.5.2 Problem Statement written (supervisor M3.4; author approved the draft in chat):
  visits and intervals, state tensor on the anisotropic lattice, covariates, the residual update
  (Eq. `eq:bg:problem-update`), the agreed definition of "operator", the rollout, the evaluation
  target, and the research question in this notation.
- [ ] **Author review of 2.5.2** (inline `% TODO (author review)`).
- [x] (done 2026-10-17: §4.2.1 now introduces Eq. 4.1 as the update of Eq. bg:problem-update) Follow-up (Ch. 4): 4.2.1 still defines the same update (Eq. `eq:method:residual-update`);
  make it refer back to `eq:bg:problem-update` when Chapter 4 is revised.
- [x] 2026-10-13 bridges after the restructure (author sign-off per change): Ch. 2 opener, 2.1.1
  roadmap, 2.2 opener without GA, en-face sentence generalised, 2.3 bridges, 2.5 opener, 2.5.1
  reordered (bullets before the neural-solver paragraph) with the 21:1 sentence, Aim of the Thesis
  bridge, contributions as bullets.
- [x] 2026-10-14 Ch. 3 de-duplication (author sign-off): the moved 2.1.6 block deleted from 3.1
  except the 6 mm literature paragraph (now in 3.3, replacing its pointer) and the bilateral
  evidence (now in 3.7); the moved 2.1.5 block deleted from 3.2 except the biomarker paragraph
  (merged into the end of 3.2, opening reworded). Labels `sec:background:ga-oct:muw` and
  `...:state-rep` now sit on 3.1 and 3.2. 6.1 pointers to Ch. 1/Ch. 2 now point to 2.5.1.
  "Operator" glossed at first use in 1.2. Build clean.
- [x] SV-1.6 literature check: Delta t-conditioning is not new for GA. Contribution bullet now
  claims the architecture-independent framework instead.
- [ ] **Related Work rewritten 2026-10-14 (SV-2.7) -- author review pending** (inline `% TODO
  (author review)` at the top of §2.4). Five subsections: risk and rate / spatial forecasting of GA /
  irregular longitudinal data / PDE-based models in biomedicine / origins of the operators. 13 new
  references (Lachinov2024, Yoshida2025, Cluceru2024, Gigon2021, Lindner2018, Rubanova2019,
  Liu2025ImageFlowNet, Ravi2022, Puglisi2024, Lipkova2019, Ezhov2022, Ezhov2023, Banerjee2025);
  PDFs in `pdfs/GA` and `pdfs/Methods` (8 are arXiv preprints, page numbers refer to those), text
  extracted, hub notes written, every citation SUPPORTED in the ledger with a mechanically checked
  quote. Found on the way: Cluceru2024 and the GA data of ImageFlowNet are FAF, not OCT; author
  given names Kenta Yoshida and Anthony Gigon (the search agent's BibTeX had them wrong). "Remains
  sparse" replaced by a sourced statement (PDE models and neural surrogates exist where the equation
  is known; no learned solver on clinical images without a known equation for GA).
- [ ] TODO (author, 2026-10-14, inline in §3.3): rethink the pad positions in the loss. Every
  reported run trains on them at full weight (`exclude_pad_nodes` False; only the unreported fold-2
  ladder runs MPPDE_L5_nopad_f2 / MPPDE_L7_combo_f2 used it). Options: drop the mention of the
  option in §3.3 and §4.5.1, or run the exclusion on the canonical stencil (5 folds) and report it.
  Note: "pad nodes" also include within-scan positions with all-zero layers (figure-plan finding).
- [ ] TODO (author, 2026-10-14): the few single-fold analyses may need more folds: the
  solver-swap test (§5.5.1; fold 2 for the graph networks, fold 0 for the T-FEN), the T-FEN
  Courant read-back (§5.5.2, fold 0) and the three probe runs of Appendix G (fold 2). The first
  two are post-hoc evaluations of existing checkpoints (no training); the probes are training runs.
- [x] 2026-10-15 Repetition (AI R1, R12, R17), author rule "state it once, elsewhere a pointer":
  crop census only in §3.3 (§6.3, §6.4, App. A.2 now pointers without numbers; the larger-window
  trade-off only in §3.3); Mai et al. caveats (input, cohort, follow-up, crop, visits) in full only in
  §5.6.1 first paragraph (visits added there; second paragraph, three captions, §6.2 and Ch. 7 now
  pointers or nothing; §2.4 keeps the description of their raw-OCT input); §2.4.5 "Origins of the
  Operators" deleted (§2.4 intro now points to §2.3 and §4.3); Scarselli2009 + Gilmer2017 moved to the
  §4.3.2 opening, Runge1895 + Kutta1901 to the RK4 sentence of §4.3.7 (ledger: these four citations
  move with the pending recheck).
- [x] 2026-10-14 M2 prerequisite audit (supervisor): term table `reviews/m2-term-table-2026-10-14.md`;
  16 glosses applied in short sentences (AMD stages sourced to Vogl2021 + Boyer2017 drusen; macula,
  fovea, AREDS, complement inhibitors, best-corrected visual acuity, sham, injections into the eye, OCT
  and biomarkers defined in §1.1; layer boundaries in §1.2; photoreceptors and fundus in §2.1.1;
  "posterior pole" dropped; glioblastoma glossed). §1.1 Yehoshua sentence now "one imaging cohort"
  (OCT is defined later in §1.1). Rows 17-18 (low-coherence, basal-laminar deposits) left as they
  are. New citations Vogl2021 / Boyer2017 in §1.1 enter the pending ledger recheck.
- [x] 2026-10-14 §3.7 worklist pass (SV-3.5 patients per fold, 3.34-3.36); dead pointer to §5.1
  replaced ("one reason why arms are compared fold by fold"). Chapter 3 worklist complete.
- [x] 2026-10-14 §3.6 worklist pass (3.28-3.33).
- [x] 2026-10-14 §3.5 worklist pass (3.26, 3.27; "canonical setting" -> "which every reported run
  uses").
- [x] 2026-10-14 §3.3 worklist pass (3.15, 3.18-3.21) and §3.4 (3.22, 3.24): "canonical fold" in
  §3.4/§3.5 replaced by "fold~2" (it is the fold whose statistics are quoted as the example).
- [ ] Library papers for Related Work (no local copy, not cited yet): **Anegondi2023** (Ophthalmol
  Retina 7:243, doi 10.1016/j.oret.2022.08.018), **Pfau2019** (Retina 39:1527), **Niu2016**
  (Ophthalmology 123:1737), **Zhang2021** (Med Image Anal 68:101893, time factors in GA forecasting).
- [x] (2026-10-14: filed, text extracted, quotes in `literature/_scratch/final/`, all PASS;
  enters the ledger with the pending `update_ledger.py --apply` batch) Manual downloads for SV-3.4 (PMC blocks scripts; NIH author manuscripts, free in a browser):
  Li2006 PMC2646122 -> `pdfs/Methods/Li2006.pdf`, Garvin2009 PMC2911837 -> `pdfs/Methods/Garvin2009.pdf`,
  Abramoff2010 PMC3131209 -> `pdfs/Methods/Abramoff2010.pdf`. Then extract text and ledger entries
  for the §3.2 Iowa sentence (currently PENDING).
- [x] (done 2026-10-16, see the next entry) **Ledger recheck after the 2026-10-12..14 rewording:** 45 `CHANGED SENTENCE (recheck)` and 16
  `NEW (unchecked)` entries (existing keys whose sentences changed in Ch. 1-3, plus the EMA pages and
  Mai2024 in §1.1/§2.1.2/§3.1). Needs the Phase 4 check (`literature/_tools/README.md`, step 3).
- [x] 2026-10-16 Ledger recheck done: all 44 NEW + 55 CHANGED entries checked. 78 entries over 34 keys went
  through the Phase 4 workflow (9 batches, ledger agent + adversarial reviewer per paper, only the open
  occurrences given to the agents; unchanged verified entries kept); 16 entries of the 2026-10-14 hand pass
  carried over (same claim, quote passes verify_quotes; ImageFlowNet re-quoted); the two EMA pages checked by
  hand (local copies of the EPAR pages saved as `pdfs/GA/EMA2024*.txt`, page of 2026-10-16). Hub notes created
  for Abramoff2010, Garvin2009, Li2006, EMA2024Syfovre, EMA2024Izelvay; the three Iowa papers and the EMA pages
  registered (page notes in `prep_phase4.py`). Three edited entries without a local copy (Scarselli2009 C117,
  Butcher1987/Hairer1993 C134) are back to PENDING with their preliminary assessment, flagged for re-check.
  Ledger now: 184 SUPPORTED, 14 PARTLY (3 deliberate: Courant1943, Paszke2019, Vallino2024 C020), 14 PENDING,
  no NOT FOUND / CONTRADICTED / UNVERIFIED. Every quote passes verify_quotes on its page except the
  transcriptions from scans without text layer (Kutta1901 C133, Liu1994 C048, Courant1928: NO-TEXT).
- [ ] **Go through the 11 new PARTLY entries with the author, one at a time** (no thesis text changed yet):
  C018 EMA pages ("approved only in the United States": the pages show only "not in the EU");
  C016 Lad2023 ("Until 2023" not in Lad; kept on purpose on 2026-10-01, re-raised);
  C039 Boopathiraj2024 + Boyer2017 ("tightly coupled ... die together", "outer segments": both say photoreceptors);
  C043 Boopathiraj2024 + Yehoshua2011 + Vallino2024 (no source lists "three principal" signatures; sign (iii)
  rests on Chu2022); C032 Pilotto2015 + Vallino2024 ("instead": both use en face alongside B-scans; the
  pixel = A-scan definition rests on Yehoshua2011/Chu2022); C133 Runge1895 (RK4 is Kutta's; Runge's scheme is
  third order). Also worth a look (SUPPORTED with a caveat): Mai2024 C015 is a secondary citation (range from
  Fleckenstein et al. 2018); Feuer2013 C100/C153 limit "removes the dependence" to the AREDS lesion-size range;
  SanchezGonzalez2020 C058 is particle-based while the sentence before speaks of "a grid or mesh".
- [x] (superseded by the rewrite above) TODO (Related Work, SV-2.7): cite **Lachinov2024** -- Lachinov, Chakravarty, Grechenig,
  Schmidt-Erfurth & Bogunovic, "Learning Spatio-Temporal Model of Disease Progression with
  NeuralODEs from Longitudinal Volumetric Data", IEEE TMI 43(3):1165-1179, 2024, arXiv:2211.04234
  (supervisor's own paper; the model behind Mai et al. 2024; GA, continuous time, RK4). And
  **ImageFlowNet** -- arXiv:2406.14794, 2024 (neural ODE/SDE image-level forecasting from
  irregularly sampled scans, incl. GA). One sentence relating the RK4 arm to their Neural ODE
  (2.4 or 6.1).
- [ ] Decisions first: "framework" → "methodology", "operator" → "neural solver" (thesis-wide);
  restructure Introduction + Background (background as subsections of the introduction, problem
  statement and motivation after it, §2.2.5 merged with §1.3); §2.1 order anatomy → imaging → GA;
  §2.1.5–§2.1.6 into Chapter 3.
- [ ] **Abstract: deferred (author, 2026-10-14) until the rest of the thesis is settled**, so it is
  written once. Then rewrite to the supervisor's three-part structure (EN + DE); he calls it the most
  important part.
- [ ] **Worklist for Ch. 1-3** (2026-10-14): `reviews/worklist-ch1-3-2026-10-14.md` -- supervisor
  items and the still-open AI-review items in one list, by current section (15 supervisor points,
  119 AI items: 65 medium, 54 low; 23 AI items resolved by the restructure and bridges).
- [ ] Ch. 1: two-sentence split + both US-approved drugs (pegcetacoplan, avacincaptad pegol, not
  EU); variable growth rate as the motivation; simplify the setup sentence; literature check before
  claiming Δt-conditioning as a contribution. §1.1 closing paragraph: "well written", keep.
- [ ] Ch. 2: heading "Eye anatomy"; GA section wording; Related Work expanded into subsections.
- [ ] Ch. 3: microns for spacings; cite the Iowa layer segmentation; patients per fold; strike-out
  on "The data agree with this:"; supervisor confirms the cohort is Mai's cohort with tighter
  registration and cleaner segmentations (resolves the §2.4 cohort TODO, update every "larger
  cohort" mention).

### Supervisor review 2 (Dmitrii Lachinov, 2026-10-17)

Second part of the review, `main-thesis_dl_rev2.pdf` (Downloads): the same build of 2026-10-02 as
review 1, annotated further. Marks 1-28 are the review-1 comments; marks 29-93 (pp. 36-85) are new and
cover Chapters 4-7 (65 highlights, 47 with a comment). Appendices skipped. Matched against the AI
editorial review (`reviews/editorial-2026-10-01/`, statuses of 2026-10-02 re-checked against today's
sources) in one list: **`reviews/worklist-ch4-7-2026-10-17.md`** (39 supervisor items SV-4.1-SV-7.5,
e-mail points E1-E6, cross-cutting X1-X8, the open AI structure items, 263 open AI items by section,
55 of them on sentences he marked). To be worked through chapter by chapter, like Ch. 1-3.
- [ ] Work through `reviews/worklist-ch4-7-2026-10-17.md`, chapter by chapter.
  - [x] 2026-10-17 §4.1 done: SV-4.1 (first paragraph: what the framework defines, confounders), AI 4a.2-4a.6,
    4a.8 (persistence paragraph moved and now backed by the check above). "Canonical" now defined at its first
    use (the reference configuration on which the framework ablations run and to which the arms are
    parameter-matched).
  - [x] 2026-10-17 §4.2 (SV-4.3 Lipschitz assumption for the Delta t -> 0 limit, SV-4.4 tensor layout in the
    2.5.2 notation), §4.3 opener + §4.3.1, §4.3.2 (SV-4.5 forward references, SV-4.6 headings) and §4.3.3
    (SV-4.7 distances named, index-space k = 12 neighbourhood = geodesic ball of radius 2; SV-4.8 dilated
    convolutions cited; X4 micrometres) done, with the AI items of these sections.
- [ ] (2026-10-19: add Courant1928 C137, §4.3.6, "in the sense of the stability condition of", previous verdict PARTLY) **Ledger batch to check (Phase 4), from the 2026-10-17 wording pass:** NEW Yu2016 (C125) and Li2019
  (C126) in §4.3.3, Liu2018 (C116, sentence moved); CHANGED Brandstetter2022 C123 (§4.3.2) and C149 (§5.4.1),
  Ott2021 C114 (§4.2.1), Ioffe2015 C115 (§4.3.1). Also CHANGED by the author's uncommitted §1.1 edit: Lad2023
  C017, EMA2024Syfovre/Izelvay C019, Trincao2024 C016 (NEW). PDFs of Yu2016 / Li2019 filed in `pdfs/Methods/`
  (arXiv versions; page numbers refer to them), text extracted; hub notes still to be written by the workflow.
  Quotes found by hand: Yu2016 p. 2 "The dilated convolution operator can apply the same filter at different
  ranges using different dilation factors."; p. 3 (Fig. 1 caption) "The number of parameters associated with
  each layer is identical." Li2019 p. 4 "the Dilated k-NN returns the k nearest neighbors within the k × d
  neighborhood region by skipping every d neighbors" and "we use the ℓ2 distance in the feature space of the
  current layer". Bib metadata: Li2019 checked on Crossref (ICCV 2019, pp. 9266-9275, doi
  10.1109/ICCV.2019.00936); Yu2016 ICLR 2016 (no DOI).
- [x] 2026-10-17 **§5.1.3 split; new §5.1.4 "Late-Epoch Mean"** (`sec:experiments:protocol:late`), worked out
  with the author: why no single epoch (noise: sd 0.007-0.025 over epochs 10-29; selection bias of the best
  epoch +0.025 to +0.050, larger for arms that fluctuate more, not removable without a test split) and why
  epochs 10-29 (operators learn at different speeds: level reached at epoch <= 3 except free-form FEN 8 and
  U-Net 9; halves of the window differ <= 0.014). Arguments dropped at the author's request: curriculum (full
  from epoch 2), learning-rate schedule (drops at 5 and 20), best-checkpoint use, 5-29 robustness check. New
  Fig. 5.1 `fig:experiments:learning-speed` (`images/scripts/fig_experiments_learning_speed.py`, which also
  prints every quoted number over all eleven arms). The old combined curves figure is split: its objective
  panel is now a placeholder in §5.4.2 under the old label `fig:experiments:curves` (draft script
  `fig_experiments_objective.py` from another session, not reviewed). Old §5.1.4 is now §5.1.5. AI items
  5a.17, 5a.18, 5a.20-5a.22 done; 5a.15, 5a.16 (wording in the rollout paragraphs) still open.
- [x] 2026-10-18 **Objective figure in §5.4.2** (Fig. 5.6, label renamed `fig:experiments:curves` ->
  `fig:experiments:objective`), reviewed with the author: one panel, one line per objective (mean over the
  five folds of the dilated-stencil GNN, seed 42), legend names only, everything else in the caption.
  `images/scripts/fig_experiments_objective.py` now also checks the other §5.4.2 numbers (late sd
  0.015/0.043 and 0.013/0.017 on folds 0-3, raw mask RMSE 1.10/0.51, 74/75 eyes identical): all match.
  Old combined `fig_experiments_curves.py` / `.pdf` removed. Dropped after review: a best-epoch-vs-late-mean
  plot (a maximum always lies above a mean) and an eleven-arm scatter of epoch-to-epoch sd vs best-epoch
  gain (Pearson r = 0.42; the FNO has sd 0.008 but gain +0.045 because it peaks early). Consequently the
  §5.1.4 sentence "larger for arms whose scores fluctuate more" now reads "larger both for arms whose
  scores fluctuate more and for arms whose score peaks early ..., such as the FNO".
- [ ] SV-5.13: small table next to the §5.4.2 objective test (full / without soft-Dice / plain MSE).
- [x] 2026-10-18 **Rollout figure in §5.2** (Fig. 5.2, `fig:experiments:rollout`, now a vector PDF), reworked
  with the author: one row of four panels (baseline / truth / prediction / agreement), canonical model only,
  epoch-29 weights, cropped to the lesion, edges smoothed for display as in the poster (drawn areas within 3 %
  of the native ones; Dice on the unsmoothed masks). Eye rule: among the validation eyes of folds 0-2 whose
  lesion does not touch the window edge, the highest change-region Dice: fold 0, eye 10 (PEAT0013_OD), 0.761,
  best of 48 (median 0.544); the caption calls it an eye on which the model does well. Rejected on the way:
  the old fold-2 median eye (best fold, edge contact, large no-data area, 10 % shrinkage) and a folds 0-2
  median eye (fold 2 eye 6, 0.552: correct places but 40 % of the true change). §5.2 sentence changed to
  match. Old PNG removed.
- [x] (superseded 2026-10-21: App. D shows kinds of lesion on which the model works; Fig. 5.2 caption adjusted) Appendix D (`fig_appendix_rollouts`, still disabled) must show typical and difficult eyes: the Fig. 5.2
  caption now points there for them. Most eyes receive less predicted change than occurs (35 of 48, median
  ratio predicted/true 0.73, folds 0-2, epoch 29).
- [x] 2026-10-18 **New §5.4 "Differences Between Folds"** (`sec:experiments:folds`, after the ingredient study;
  Negative Results onwards renumber to §5.5-§5.8), worked out with the author. Fig. 5.5 `fig:experiments:arms-folds`
  is now one line per operator over the five folds (five main operators, seed 42, `fig_experiments_arms_folds.py`);
  new Fig. 5.6 `fig:experiments:far-atrophy` (`fig_experiments_far_atrophy.py`). §5.2 keeps a short fold paragraph
  with a pointer. Content: fold 2 highest because it holds the largest, slowest lesions (per-eye Dice vs area
  rho 0.45, vs growth rate -0.35); folds come from MUW split files without a recorded criterion; the stencil GNN
  scores lower relative to the other operators the more new atrophy appears > 0.24 mm from the lesion (rho -0.32;
  explains fold 1, two of three cases are the eyes of one patient); dense operators lose most at the window edge
  (rho -0.39; zero padding named as untested reason, checked in unet.py / fno.py: FNO zero-pads 1/8 per axis
  before the FFT, not periodic); fold 4: all operators under-predict when relative growth is large, the stencil
  falls shorter than the FNO (49 % vs 83 %), not explained by relative growth; fold 3: growth closest to the
  lesion and two tiny lesions, about a quarter of the gap explained. Every number from
  `images/scripts/analysis_folds.py` (per-eye growth-region Dice; eye ids checked against logged areas).
  Checked on the way and dropped: the T-FEN's lead over the stencil concentrated on folds 1 and 4 at seed 42 does
  not repeat at seed 7 (training noise); per-fold box plots did not carry the message.
- [ ] Fold section, open: (i) whether the fold-3/fold-4 dips come from the validation eyes or the training sets
  needs retraining on a reshuffled patient split (stencil GNN and U-Net, 5 folds each); (ii) ask the supervisor
  how MUW's split files (`split5_hrf_spec_aligned`, 100 patient ids, 80/20) were assigned; (iii) the stencil
  GNN's larger lead over the k-NN GNN on folds 2 and 4 (about 0.09 against 0.04, both seeds) is unexplained.
- [ ] Edge-advance analysis for §6.2 ("good at where, weaker at how fast"), exploratory 2026-10-18, not yet a
  script: per row, outward shift of the left/right lesion edge (columns, fine axis) from baseline to one year.
  Predicted advance correlates with the true one in 47 of 48 eyes (median r 0.53; 0.70 for the Fig. 5.2 eye),
  but varies about half as much between places (median sd 25 vs 51 columns) and is smaller (23 vs 39). Caveats:
  horizontal axis only; outermost edge per row, so lobe merging inflates the largest values. Write as a script
  in images/scripts/ before quoting.
- [ ] Figure rule (author, 2026-10-18): one message per figure, one line per condition, text only as axis
  labels and short legend names, everything else in the caption. Apply to the remaining disabled figures.
- [x] 2026-10-18 **Chapter 4 reordered** (author, option (a) of AI S7/T9 and supervisor E1): conditioning and
  training are now subsections 4.2.3-4.2.6 of the framework section; 4.3 Operators unchanged; Implementation is
  4.4. Pure move checked line by line (only headings changed), then: §4.1 roadmap and §4.2 opener rewritten for
  the new order; per-operator covariate details dropped from 4.2.3 (each operator subsection states them); the
  curriculum no longer repeats the batch-statistics rule (4.3.1 states it); references meaning the curriculum
  now point to `sec:method:training:curriculum` (03-data.tex x2, 4.3.1); App. F row points to 4.2 and 5.1.
  Also done: all Chapter 4 AI items except 4c.13 (waits for the local pad-exclusion run) and SV-4.2 (author's
  TODO). Table 4.3 is now Table 4.1 (it comes before the parameter table).
- [x] 2026-10-18 **SV-5.2 z-test applied** (author sign-off): §5.1.5 states the rule as a z-test
  (z = mean fold-paired difference / sigma_Delta, sigma_Delta = sqrt(sigma_A^2 + sigma_B^2)/sqrt(n),
  sigma_GNN = 0.0127 from seven replicate pairs, sigma_UNet = 0.0191 from its seed pairs on all five folds;
  |z| > 1.96); "established" still also needs the per-eye check, leave-one-fold-out and the second seed. App.
  E.3 criteria rewritten with the formula and three caveats (sigma itself estimated; ~50 tests; fellow eyes);
  the unreproducible "1.9x" for the U-Net replaced by the measured 1.5x. App. E tables: z in every fold-paired
  cell, written by `images/scripts/appendix_ztests.py` (rerun it if a table value changes; it skips cells that
  already carry z). Readings changed: T-FEN - stencil "just beyond retraining noise at both seeds (z = 2.1), not
  established" (§5.2 twice + App. E); stencil - U-Net "beyond noise at seed 42 (z = 2.1), not at seed 7 (0.8)";
  FNO+3x3 - U-Net at seed 7 now "within retraining noise" (z = -1.9). All other readings unchanged.
- [x] 2026-10-19 **§5.2 restructured** (SV-5.3, author sign-off): heading "The Arm Table" -> "Main
  Results" (label kept); order intro -> reading the table (per-pixel floor, between-fold sd, best fold,
  adjacent rows) -> the three highest arms (T-FEN form folded in) -> interior eyes -> canonical choice ->
  example eye -> summary. The summary no longer claims "not their class but the ingredients" (AI S11/T10,
  5a.34, 5a.35); it states that the two highest arms extend the reach of a local operator and hands the
  test to §5.3. Per-pixel sentence now "its thresholded prediction at the anchor is identical to the
  baseline mask" (author: no "collapse counter flags", no colon). AI 5a.29-5a.40 done or obsolete.
  Numbers unchanged.
- [x] (done 2026-10-19, see below) TODO (inline at the §5.3 opener, AI 5b.1): the opener repeats "within about 0.04" from the new §5.2
  summary and gives no map of the subsections; rewrite when §5.3 is reviewed.
- [x] 2026-10-19 **§5.3 first round** (SV-5.4, SV-5.6, author sign-off): heading "The Ingredient Study" ->
  "Ablation Studies" (supervisor's wording, label kept); "ingredient" dropped in favour of "property" in
  §2.3, the §5.3 opener and §6.1 (heading "The operator: its properties."); §5.3.5 still uses it (next
  round). New opener with a map of the subsections. §5.3.1 and §5.3.2 as goal -> results -> conclusion;
  §5.3.1 ends on the reach limit of the k-NN graph (author: the depth question belongs to §5.3.2), §5.3.2
  ends with the four-round pointer to §5.5.3; distances in µm (11 / 119 µm). "Negative Results" keeps its
  heading (supervisor did not flag it). AI 5b.1, 5b.2, 5b.4-5b.12 done.
- [x] 2026-10-19 **§5.3 second round** (SV-5.7-SV-5.10, author sign-off): §5.3.3 goal -> FNO vs FNO+3x3 ->
  comparison with the other operators -> horizon (paired per year) -> conclusion; §5.3.4 opening expanded
  (free-form term, transport term, zero-init), Galerkin result scoped (unstable only well after the anchor),
  fold-4 failure of the matched control interpreted as an optimisation failure (training error rises; cause
  not diagnosed; larger FENs in §5.5.3 fail similarly), the matched control's limit stated (author: a wider
  free-form term is not a useful use of the parameters; it rules out that use, not every use) and the
  width-48 T-FEN (20 455 params, fewer than the width-96 control, same score) added; §5.3.5 heading
  "Summary of the Ablation Studies", closing now the two magnitudes (one property within a class 0.06-0.07,
  the three highest classes within 0.04). AI 5b.13-5b.34 done. Numbers unchanged.
- [x] 2026-10-19 **§5.5 Negative Results** (SV-5.11, SV-5.13, SV-5.14, author sign-off; heading kept): opener
  names the two objective effects as exceptions to the nulls; §5.5.1 without "the tests ask", FNO named in the
  opener, f_theta algebra corrected (f_theta outputs the distance divided by Delta t), 4.8x scoped to the
  stencil network, pointer to §5.6.1 for refining the step; §5.5.2 new Table `tab:experiments:objective` (full /
  without soft-Dice / plain MSE / with penalty, values from SOLVER_FINAL_RUNS §9.22), "teacher-forced" replaced,
  conclusion on the weighting rests on runs 1 and 2; §5.5.3 step-down rows explained, FNO + 3x3 at widths 2 and 9
  now stated as below width 5 (z = -2.4 / -2.2), width-192 divergence in the width paragraph, "not a lever"
  removed. AI 5c.1-5c.29 done. Two overfull boxes (Table 5.1, 4.99 pt; lines 417-452, 6.6 pt) predate this pass.
- [x] 2026-10-19 **§5.6 Validity Diagnostics** (SV-5.15, SV-5.16, author sign-off): opener rewritten; the
  step-size ladder replaces the earlier solver-swap test (fold 2 / fold 0, intervals split into 1, 2, 4
  steps). §5.6.1: setup with fixed steps h = 1 ... 1/32 year, three models on folds 0-2; C1 read at the two
  finest steps (fixed after the ladder ran, stated in a comment); results: canonical fails C2 on all folds
  (C1 passes on folds 0 and 1, fails on fold 2), RK4-trained network converges everywhere but passes C2 on
  fold 2 only (+0.018 between trained and converged value on folds 0 and 1), T-FEN passes everywhere. New
  Table 5.4 = per model and fold summary; new Appendix E section "The Step-Size Ladder"
  (`app:full-results:step-ladder`, Table `tab:appendix:step-ladder`) with every setting; both tables from
  `images/scripts/table_step_ladder.py` (asserts the control setting reproduces the logged Dice). Figure 5.x
  caption respecified for the ladder; figure still disabled, script must be redrawn from the ladder cache.
  §5.6.2 wording fixed (AI 5d.14-5d.21). Follow-ups: §6.1 (only the T-FEN is called a continuous-time model;
  the wrapper network would need a finer training step) and §6.3 ("three of the five folds per model").
- [x] 2026-10-21 `fig:experiments:swap` redrawn from `images/data/step_ladder` and restored, worked out with
  the author: only the two graph networks (canonical Euler, RK4-trained), each with the scheme it was trained
  with, one colour + marker per fold (SEQ blues), signed y-axis around 0, x = internal step 365-11.4 d.
  Rejected on the way: three panels with Euler and RK4 per fold (too crowded); one panel with the largest
  change over folds (hides the sign); mean over folds (hides that the folds move in opposite directions).
  The T-FEN was left out: its coarse steps (365-91 d) are coarser than its 45-day training step, fail for the
  Courant reason, and lie outside the test, but read as "the T-FEN fails"; its fine side is three points at 0.
  Caption rewritten ("The step-size ladder for the graph network"); §5.6.1 pointer now "for the two graph
  networks".
- [x] 2026-10-21 (author) T-FEN step ladder as its own figure `fig:experiments:swap-tfen`
  (`images/scripts/fig_experiments_swap_tfen.py`), in §5.6.1 after the T-FEN paragraph: trained with 45-day RK4
  steps (ring), steps coarser than training shaded and stated as outside C2; 91 d still agrees (0.001-0.012
  lower), 183 and 365 d drop by 0.07-0.20. The paragraph's "Coarser steps lose accuracy" now says the same.
  New palette entry `FOLD_TFEN` (#CC79A7 / #995B7D / #663C54) in `style/palette.py` and `foldTfenA-C` in
  `style/thesis-colors.sty` (darkened T-FEN pink, so no fold shade coincides with ARM["fen"]).
- [x] 2026-10-21 (author): the RK4-trained network's C2 failure comes from an improvement and the text now
  says so plainly: with finer steps its Dice rises by 0.018 on folds 0 and 1 (level with the canonical network
  there) and is unchanged on fold 2. Added in §5.6.1, §5.5.1 (RK4 paragraph), §6.1.5 and the Fig. 5.9 caption;
  Table 5.5 retitled "The step-size ladder" (was "The solver-swap test"). Author: no "not tested" hedges.
- [ ] TODO (author, 2026-10-21): run the step-size ladder on folds 3 and 4 too (`images/scripts/step_ladder.py`;
  these folds have no local precompute, so precompute them or run on the cluster), then update
  `fig:experiments:swap`, Table `tab:experiments:swap`, Table `tab:appendix:step-ladder` and the §5.6.1 text
  (inline TODO above the figure). **Then revise everything quoted from folds 0-2** (author 2026-10-21): every
  fold count and number of §5.6.1 (canonical, RK4 network, T-FEN), the RK4 sentence in §5.5.1 ("0.018 higher
  on folds 0 and 1"), §6.1.5 ("two of the three tested folds", "all three tested folds"), the Fig. 5.9 caption,
  and the T-FEN step-ladder figure if it goes in. Inline TODOs at each place.
- [ ] **TODO (author, 2026-10-19): review the placement of the step-size ladder explicitly** -- now in §5.6.1
  (Table 5.4 summary + Appendix E full table), with one pointer sentence in §5.5.1 (inline TODOs in both).
- [x] 2026-10-19 **§5.7 "Comparison with Prior Work"** (author sign-off; heading was "Qualitative Analysis and
  Clinical Comparison" with one subsection, no paper name in the heading): intro, the Mai et al. differences in one
  paragraph (32 months = about 2.7 years, SV-5.17; growth rate from the respective follow-up vs from the last visit),
  growth-region Dice by horizon now also against Gigon2021 Table 2 (same bins, RORA, en-face thickness + reflectivity
  input: 0.46 / 0.57 / 0.59 / 0.65 / 0.72) and Salvi2025 (test Dice 0.70; two input visits, lesions 2.54-17.78 mm2,
  median 9.03, growth from the 6-month lesion), growth speed also against Gigon2021 (r 0.52) and Yoshida2025 (r2
  0.33-0.35, r about 0.57-0.59; trained on the rate, 1219 eyes, FAF slope in mm2/yr), conclusion: in range on where,
  below every comparable model on how fast (0.40 vs 0.52-0.61). Every claim checked against the local text; 19 new
  or re-checked ledger entries by hand, all quotes PASS in verify_quotes.py (literature/_scratch/final, manual pass
  2026-10-19). Horizon table narrowed (footnotesize, "Stencil GNN"). §6.2: comparison updated; three untested
  explanations added (not trained on the rate; cautious predictions, 35/48 eyes at 0.73, fastest at 0.50; no image
  intensity in the inputs); the failure-case TODO replaced by pointers to §5.4 and §5.7. AI S12/T12, 5d.22-5d.34 done.
- [x] 2026-10-19 **§5.8 Computational Cost, Chapter 5 opener, new §5.9 Summary** (author sign-off): §5.8 opens with
  its purpose and the cost convention (scope: inference time and memory not measured), the FENs are no longer called
  single-step, the ratio paragraph explains why the wrapper ratio depends on the operator, the conclusion says the
  T-FEN's lead over the stencil is not established; Chapter 5 opener with a section map that names the framework tests
  of §5.5 (AI T5); new §5.9 "Summary" (`sec:experiments:summary`) so the chapter ends on its answer (AI T6).
  AI 5d.36-5d.45 done. Chapter 5 worklist done except §5.4 (fold section, written 2026-10-18, not in either review)
  and the open author items (z-test re-read, ladder placement, SV-4.2).
- [ ] Qualitative material without a section (2026-10-19): per-eye rollouts are Fig. 5.2 and Appendix D (figure
  disabled); sparse schedules and short vs long Delta t were never analysed (old §5.7 plan). Decide whether Appendix D
  needs a short text on typical and difficult eyes when its figure is restored.
- [x] 2026-10-19 **"anchor" kept, defined instead (SV-6.4, author decision)**: in the 2026-10-02 version the supervisor read,
  "the one-year anchor" was used from §3.3 on without a definition, and §6.1 had a bare "at the anchor" (the sentence he
  marked). Now: definition in place at the first use of Chapter 5 (§5.1.2, "the first visit of the rollout whose time since
  baseline reaches about one year"), §3.3 points to §3.6, and the §6.1 rewrite says "at one year". A thesis-wide rename to
  "the one-year visit" (57 places, e6c0535 + 43b1955) was reverted the same day (af06ea9, ff8053d); the §6.1 sentence repair
  of e6c0535 was re-applied.
- [x] 2026-10-19 **§6.1 rewritten** (SV-6.1, SV-6.2, SV-6.5, SV-6.6, author sign-off): self-contained for a reader who
  skipped the thesis (task, data, measure, then each result with its number); run-in headings replaced by subsections
  6.1.1 The Framework, 6.1.2 The Operator, 6.1.3 Capacity, 6.1.4 A Missing Counterpart to the Equation Features,
  6.1.5 Predictions Between Visits, 6.1.6 Implications for Modelling; one answer to part 1 (AI S14); distances in µm
  (57-142 / 11 / 119 µm); why more reach stops helping (author TODO) now in 6.1.2; regulariser placed as an earlier
  attempt (S20). The capacity and equation-feature paragraphs are unchanged (SV-6.3) apart from "growth-speed gap".
  AI 6-7.1-6-7.12, 6-7.20, 6-7.22-6-7.24 done; 6-7.19/6-7.21 dropped. Numbers from Table 5.1, §5.3, §5.5 (unchanged).
- [x] 2026-10-19 **§6.2-§6.4** (SV-6.7, E5, author sign-off): §6.2 explanations of the growth-speed gap as one list
  ("none of them was tested"; my earlier wording implied the first four were tested), clinical paragraph reworded,
  "one-year anchor" defined in place, grader scale reworded, "Forecast failures"; §6.3 FAF annotation stated as fact
  (§3.1 TODO closed, device-model TODO kept), layer-provenance/name clause removed (names now in §3.2), shrinkage as its
  own paragraph, anchor time "about one year" (consistent with §3.6/§5.1.2), PINN/mesh paragraph with a bridge; §6.4
  trajectory memory and transport model reworded. AI 6-7.26-6-7.43 done. Run-in headings of §6.4 kept (author 2026-10-02).
- [x] 2026-10-19 **Chapter 7 rewritten in place** (SV-7.1-SV-7.5, author sign-off): "requires", "equally", "implements these
  requirements"; no participle opener, no "is not what decides", no "What separates ... are", no slogan sentence, no closing
  "what matters is ... rather than"; bullets name their subject and use "scores"; the Runge-Kutta null stated once; the
  reach/transport interpretation directly after the list; the limits moved into the last paragraph; the growth-speed
  comparison now against 0.52-0.61 (§5.7). Numbers unchanged. AI 6-7.44-6-7.56 done. Ledger: Mai2024 C180 (new) and
  Courant1928 C175 (§6.1.2, reworded) checked by hand, quote PASS / scan as before; the §6.3 Mai citation was removed
  with the FAF hedge. **Chapters 4-7 worklist: every supervisor item done or decided, except SV-4.2 (author TODO) and
  SV-5.12 (question to the supervisor).**
- [ ] **Reply mail (2026-10-20): ask the supervisor about SV-5.12** -- is the post-hoc step-size ladder (trained
  networks re-evaluated with fixed steps h = 1 ... 1/32 year, no retraining; three networks, folds 0-2) what he
  meant, or did he want networks trained at different step sizes?
- [x] (2026-10-19: in §6.1.2, "More reach does not keep helping") TODO (inline in §6.1, author 2026-10-19): discuss why more message-passing rounds or more reach stop
  helping (second round on the k-NN graph +0.011, not established; four rounds on the stencil -0.009; reaches
  ±35/±42 and rows ±2 lower than ±21), with the untested candidate explanations (mean aggregation diluting
  near neighbours; extra reach bringing in unrelated tissue).
- [ ] **TODO (author, 2026-10-18): re-read the z-test parts when going through the thesis again** -- §5.1.5
  second paragraph (inline TODO there), App. E.3 criteria, the z values in the three App. E tables, and the two
  §5.2 sentences on T-FEN vs stencil and stencil vs U-Net.
- [ ] For §5.4.3 (capacity) when it is reviewed: with the z-test, the FNO+3x3 at width 2 and at width 9 are both
  significantly *below* width 5 (z = -2.4 / -2.2), and the U-Net at width 2 is not (z = -1.4 with sigma_UNet).
  The conclusion "no width step raises a class" holds; check that "the smaller versions lost little" still fits.
- [x] (stale, checked 2026-10-20: the redraw of 2026-10-17 already uses µm in the figure and the caption)
  Fig. 4.2 caption still gives distances in mm, while §4.3.3 now uses µm (X4).
- [ ] TODO (SV-4.2, inline in §4.1): reconsider whether the moving-mesh result goes into the main text as a
  negative result. Author 2026-10-17: not convinced (argumentation still loose; on the dilated stencil only one
  fold-2 dual run exists, no bypass control; the 5-fold dual/bypass arms are on the k-NN graph; it would take
  defence time).
- [ ] E-mail, general: every section = intro (purpose + thesis statement) / body / conclusion; no LLM
  sentence patterns ("What it does is that ...", "not X but Y", "X is not what decides Y"; "they are all
  over"); compare the MM-PDE paper's style; one table or plot per results subsection, small table
  excerpts next to each ablation; boxplots/scatterplots. The **guidelines book** he says he sent is not
  in the repo or Downloads: locate it or ask.
- [x] (2026-10-19: in §3.2 with the ten names; mean depth strictly increasing over channels 1-10 in all 553 visits) **Layer boundaries (answers review-1 SV-3.4):** 001 ILM, 002 RNFL-GCL, 003 GCL-IPL, 004 IPL-INL,
  005 INL-OPL, 006 OPL-HFL, 008 IS/OS junction, 009 inner boundary of the OPR, 010 inner boundary of the
  RPE, 011 outer boundary of the RPE (surface 007 of the Iowa set is not in the data). Write into §3.2 and
  §6.3 and close the "names of the ten boundaries" TODOs; confirm first that channels 1-10 follow this
  order.
- [x] (2026-10-19: §6.3 hedge removed, §3.1 TODO closed) **FAF annotation confirmed** (SV-6.7, "most likely annotated" -> "it was"): remove the hedge in §6.3
  and the "inferred from Mai et al." TODO in §3.1; this is the supervisor confirmation that the FACT
  CHECK item of 2026-09-25 was waiting for.
- [ ] Decisions to take with the author (or ask the supervisor): SV-4.2 MM-PDE into the main text as a
  negative result (conflicts with the 2026-09-25 appendix decision); SV-4.4 what "(C, N, K) does not
  match" refers to; SV-5.2 z-test with an empirical sigma for the noise rule (the 0.016 paired threshold
  already corresponds to z of about 2); SV-5.12 new step-size test h = 1 ... 1/32 years (post-hoc on
  existing checkpoints or new training); SV-6.4 "anchor" -> "study evaluation interval?".
- [ ] Reply mail, new points: introduction/background merge closed ("it's fine"); he uses "framework"
  himself (SV-4.1), so "methodology" may not be needed; ask about SV-4.4, SV-6.4 and the guidelines book;
  JKU rule on AI-generated figures still unanswered (he avoids image generators himself, uses
  matplotlib/seaborn scripts and Claude SVG elements merged in draw.io).
- [ ] **SV-5.12 step-size ladder, post-hoc (2026-10-17; author to decide whether and how it enters
  §5.5.1).** No training: the epoch-29 checkpoints were re-evaluated with fixed steps h = 1, 1/2,
  1/4, 1/8, 1/16, 1/32 year (365 ... 11.4 d) through the unmodified evaluation, `GAIntegrator(step_days
  = h)`, script `images/scripts/step_ladder.py`, cache and readout `images/data/step_ladder/README.md`
  (git-ignored). Folds 0, 1, 2 (folds 3, 4 have no local precompute). Each rollout step is one visit
  interval, split into ceil(interval / h) equal substeps, so the step taken is <= h; no visit skipped.
  Checks: every trained setting reproduces its logged epoch-29 Dice exactly (all 9 network/fold pairs,
  incl. canonical f2 Euler 1 / 4 steps 0.596418 / 0.520589, RK4-wrapper f2 0.566656, T-FEN f0 0.548471).
  **h = 1 and 1/2 year are almost the trained one-step setting**: the median interval is 180 d, and
  only 2/135, 0/65, 3/100 intervals (f0/f1/f2) get two substeps at 365 d, 23/135, 4/65, 9/100 at
  182.5 d; a true one-year step would need visit skipping (different set-up, discuss with the
  supervisor). Runtime: 129 settings in ~51 min on the RTX 5080. Change-region Dice@360d, in brackets
  the difference to the trained setting; folds have 20 / 12 / 16 eyes at the anchor:

  Canonical stencil network `ANISOGNN_final_dilmean` (trained: one Euler step per interval, Delta t as input; evaluated autonomous = False):

  | h (year) | scheme | median substeps | intervals > 1 substep (f0 / f1 / f2) | fold 0 (20 eyes) | fold 1 (12 eyes) | fold 2 (16 eyes) |
  |---|---|---:|---|---:|---:|---:|
  | trained (euler:n1) | euler | 1 | 0/135 / 0/65 / 0/100 | 0.5397 | 0.4534 | 0.5964 |
  | 1 (365 d) | euler | 1 | 2/135 / 0/65 / 3/100 | 0.5397 (+0.0000) | 0.4534 (+0.0000) | 0.5964 (+0.0000) |
  | 1/2 (182.5 d) | euler | 1 | 23/135 / 4/65 / 9/100 | 0.5342 (-0.0055) | 0.4412 (-0.0122) | 0.5973 (+0.0009) |
  | 1/4 (91.25 d) | euler | 2 | 131/135 / 65/65 / 72/100 | 0.5350 (-0.0047) | 0.4740 (+0.0206) | 0.5809 (-0.0155) |
  | 1/8 (45.6 d) | euler | 4 | 135/135 / 65/65 / 100/100 | 0.5196 (-0.0201) | 0.4948 (+0.0414) | 0.5154 (-0.0811) |
  | 1/16 (22.8 d) | euler | 8 | 135/135 / 65/65 / 100/100 | 0.5095 (-0.0302) | 0.4995 (+0.0461) | 0.4389 (-0.1575) |
  | 1/32 (11.4 d) | euler | 16 | 135/135 / 65/65 / 100/100 | 0.5032 (-0.0365) | 0.4961 (+0.0427) | 0.4091 (-0.1873) |
  | 1 (365 d) | rk4 | 1 | 2/135 / 0/65 / 3/100 | 0.5569 (+0.0172) | 0.4800 (+0.0266) | 0.6062 (+0.0097) |
  | 1/2 (182.5 d) | rk4 | 1 | 23/135 / 4/65 / 9/100 | 0.5526 (+0.0129) | 0.4702 (+0.0168) | 0.6077 (+0.0113) |
  | 1/4 (91.25 d) | rk4 | 2 | 131/135 / 65/65 / 72/100 | 0.5513 (+0.0116) | 0.5024 (+0.0490) | 0.5791 (-0.0173) |
  | 1/8 (45.6 d) | rk4 | 4 | 135/135 / 65/65 / 100/100 | 0.5409 (+0.0012) | 0.5184 (+0.0650) | 0.5060 (-0.0905) |
  | 1/16 (22.8 d) | rk4 | 8 | 135/135 / 65/65 / 100/100 | 0.5229 (-0.0168) | 0.5099 (+0.0566) | 0.4341 (-0.1623) |
  | 1/32 (11.4 d) | rk4 | 16 | 135/135 / 65/65 / 100/100 | 0.5122 (-0.0276) | 0.5015 (+0.0481) | 0.4066 (-0.1898) |

  Network trained in the RK4 wrapper `ANISOGNN_final_oderk4n1` (trained: one RK4 step per interval, autonomous):

  | h (year) | scheme | median substeps | intervals > 1 substep (f0 / f1 / f2) | fold 0 (20 eyes) | fold 1 (12 eyes) | fold 2 (16 eyes) |
  |---|---|---:|---|---:|---:|---:|
  | trained (rk4:n1) | rk4 | 1 | 0/135 / 0/65 / 0/100 | 0.5275 | 0.4392 | 0.5667 |
  | 1 (365 d) | rk4 | 1 | 2/135 / 0/65 / 3/100 | 0.5275 (+0.0000) | 0.4392 (+0.0000) | 0.5667 (+0.0000) |
  | 1/2 (182.5 d) | rk4 | 1 | 23/135 / 4/65 / 9/100 | 0.5356 (+0.0081) | 0.4422 (+0.0030) | 0.5668 (+0.0002) |
  | 1/4 (91.25 d) | rk4 | 2 | 131/135 / 65/65 / 72/100 | 0.5472 (+0.0197) | 0.4569 (+0.0177) | 0.5670 (+0.0003) |
  | 1/8 (45.6 d) | rk4 | 4 | 135/135 / 65/65 / 100/100 | 0.5455 (+0.0180) | 0.4565 (+0.0173) | 0.5671 (+0.0004) |
  | 1/16 (22.8 d) | rk4 | 8 | 135/135 / 65/65 / 100/100 | 0.5450 (+0.0175) | 0.4572 (+0.0180) | 0.5668 (+0.0001) |
  | 1/32 (11.4 d) | rk4 | 16 | 135/135 / 65/65 / 100/100 | 0.5451 (+0.0176) | 0.4573 (+0.0181) | 0.5667 (+0.0001) |
  | 1 (365 d) | euler | 1 | 2/135 / 0/65 / 3/100 | 0.4145 (-0.1130) | 0.3963 (-0.0429) | 0.5466 (-0.0201) |
  | 1/2 (182.5 d) | euler | 1 | 23/135 / 4/65 / 9/100 | 0.4644 (-0.0631) | 0.3929 (-0.0463) | 0.5505 (-0.0161) |
  | 1/4 (91.25 d) | euler | 2 | 131/135 / 65/65 / 72/100 | 0.5310 (+0.0035) | 0.4543 (+0.0151) | 0.5711 (+0.0045) |
  | 1/8 (45.6 d) | euler | 4 | 135/135 / 65/65 / 100/100 | 0.5436 (+0.0161) | 0.4669 (+0.0277) | 0.5706 (+0.0039) |
  | 1/16 (22.8 d) | euler | 8 | 135/135 / 65/65 / 100/100 | 0.5451 (+0.0176) | 0.4627 (+0.0235) | 0.5695 (+0.0028) |
  | 1/32 (11.4 d) | euler | 16 | 135/135 / 65/65 / 100/100 | 0.5455 (+0.0180) | 0.4594 (+0.0202) | 0.5680 (+0.0014) |

  Energy-conserving T-FEN `FEN_final_w96ftp7rk4d45skew` (trained: RK4 in 45-day steps, autonomous):

  | h (year) | scheme | median substeps | intervals > 1 substep (f0 / f1 / f2) | fold 0 (20 eyes) | fold 1 (12 eyes) | fold 2 (16 eyes) |
  |---|---|---:|---|---:|---:|---:|
  | trained (rk4:d45) | rk4 | 4 | 135/135 / 65/65 / 100/100 | 0.5485 | 0.5242 | 0.6066 |
  | 1 (365 d) | rk4 | 1 | 2/135 / 0/65 / 3/100 | 0.3476 (-0.2009) | 0.4291 (-0.0950) | 0.4755 (-0.1311) |
  | 1/2 (182.5 d) | rk4 | 1 | 23/135 / 4/65 / 9/100 | 0.3895 (-0.1590) | 0.4557 (-0.0685) | 0.4781 (-0.1285) |
  | 1/4 (91.25 d) | rk4 | 2 | 131/135 / 65/65 / 72/100 | 0.5470 (-0.0015) | 0.5205 (-0.0036) | 0.5943 (-0.0123) |
  | 1/8 (45.6 d) | rk4 | 4 | 135/135 / 65/65 / 100/100 | 0.5485 (+0.0000) | 0.5242 (+0.0000) | 0.6066 (+0.0000) |
  | 1/16 (22.8 d) | rk4 | 8 | 135/135 / 65/65 / 100/100 | 0.5486 (+0.0002) | 0.5254 (+0.0013) | 0.6049 (-0.0017) |
  | 1/32 (11.4 d) | rk4 | 16 | 135/135 / 65/65 / 100/100 | 0.5486 (+0.0001) | 0.5255 (+0.0014) | 0.6045 (-0.0021) |
  | 1 (365 d) | euler | 1 | 2/135 / 0/65 / 3/100 | 0.2909 (-0.2576) | 0.3493 (-0.1749) | 0.4417 (-0.1649) |
  | 1/2 (182.5 d) | euler | 1 | 23/135 / 4/65 / 9/100 | 0.3007 (-0.2477) | 0.3558 (-0.1683) | 0.4484 (-0.1582) |
  | 1/4 (91.25 d) | euler | 2 | 131/135 / 65/65 / 72/100 | 0.4601 (-0.0884) | 0.4567 (-0.0675) | 0.5253 (-0.0813) |
  | 1/8 (45.6 d) | euler | 4 | 135/135 / 65/65 / 100/100 | 0.5344 (-0.0141) | 0.5003 (-0.0239) | 0.5845 (-0.0221) |
  | 1/16 (22.8 d) | euler | 8 | 135/135 / 65/65 / 100/100 | 0.5427 (-0.0058) | 0.5153 (-0.0089) | 0.5997 (-0.0070) |
  | 1/32 (11.4 d) | euler | 16 | 135/135 / 65/65 / 100/100 | 0.5454 (-0.0030) | 0.5203 (-0.0039) | 0.6024 (-0.0042) |

  Reading (criteria of §5.5.1, run-to-run sd 0.0127):
  - Canonical network: **fails on all three folds**, as in Table 5.4. No common limit, and the drift
    has a fold-dependent sign (1/32 year: -0.037 / +0.043 / -0.187); spans over the settings at least
    as fine as training: Euler 0.037 / 0.058 / 0.188, with RK4 0.054 / 0.077 / 0.201.
    **Corrected 2026-10-19** (images/scripts/table_step_ladder.py): "no common limit" was too strong.
    It fails C2 on all three folds, but on folds 0 and 1 Euler and RK4 approach a common value at the
    finest steps (last per-halving changes below 0.0127, Euler - RK4 at 11.4 d -0.009 / -0.005), far
    from the trained value; only fold 2 still moves by ~0.03 per halving (C1 fails there). A fold-
    dependent sign of the drift is not by itself a C1 failure.
  - RK4-wrapper network: **C1 passes on all folds** (RK4 changes < 0.002 from h = 1/4 year on, and
    Euler converges to the same limit, within 0.0021 at 1/32 year); **C2 passes on fold 2 only**. On
    folds 0 and 1 the trained one-RK4-step setting is not yet converged: the limit lies +0.018 above
    it, span 0.020 / 0.018 > 0.0127. Table 5.4 (fold 2 only) therefore reads more favourably than
    folds 0-1.
  - T-FEN: **passes on all three folds** (spans 0.0002 / 0.0014 / 0.0021 at 45.6-11.4 d); coarser steps
    lose 0.002-0.012 at 1/4 year and 0.07-0.20 at 1/2-1 year. Euler converges to the RK4 value with
    first-order error (f0 -0.014, -0.006, -0.003 at 1/8 ... 1/32 year). Note: §5.5.1 says Euler is
    unstable for the T-FEN "at any step"; at the one-year anchor Euler at 11.4 d is within 0.004 of RK4
    on all three folds (says nothing about long free-running stability, the §5.5.2 criterion).
  - Training-based variant (one model per h) still open; needs the cluster.
- [ ] **Pad positions excluded from the loss, one local run (2026-10-18; author to decide whether it
  enters §5.4.2 or goes to the cluster).** Canonical stencil network, fold 2, seed 42, 30 epochs, with
  `--exclude_pad_nodes True` (positions whose target equals the zero-fill vector in all channels are
  dropped from every loss term); command line copied from the reference run `ANISOGNN_final_dilmean_f2`
  (cluster, A6000, 2026-09-02). Args diff: only `exclude_pad_nodes`, experiment name, device, input path,
  save_dir, plus flags added to the code later, all at their defaults (`weight_decay 0.01` = AdamW's old
  implicit default). Local run on the RTX 5080, code repo HEAD dd8d269 (the `code_sha` stamp in args.json
  comes from a stale `.code_sha` file). Launcher, comparison script (`compare.py`, per-eye instrument
  copied from `thesis_numbers.py` eye_late) and run dir: `images/data/pad_exclusion/` (git-ignored).
  Same validation set: persistence Dice@360d identical (0.86748). Late window epochs 10-29:

  | | pad positions in the loss (reference) | pad positions excluded | difference |
  |---|---:|---:|---:|
  | change-region Dice@360d, late mean (sd over epochs) | 0.6060 (0.0101) | 0.5922 (0.0103) | -0.0138 |
  | same, pad-masked (`_anat`) | 0.6098 | 0.5958 | -0.0139 |
  | border-touching / interior eyes | 0.6463 / 0.5818 | 0.6145 / 0.5788 | -0.032 / -0.003 |
  | growth-region Dice at the anchor (16 eyes) | 0.6260 | 0.6117 | -0.0143 (higher on 4/16 eyes, t -1.8) |
  | epoch-paired difference | | | lower on 18/20 late epochs |
  | s/epoch (min / median) | 101 / 117 | 89 / 154 | |

  Reading: no gain. The exclusion is slightly *lower*, mainly on the border-touching eyes, but -0.014 is
  inside the single-fold floor of 0.036 (run-to-run sd 0.0127), so it is not an effect either way. As
  expected, layer RMSE over valid positions falls (0.696 -> 0.628) while RMSE over all positions rises
  (0.729 -> 0.814), because the fill values are no longer trained. Caveats: one fold, one seed, different
  GPU from the reference (GPU nondeterminism dominates seed choice in this project); separating hardware
  from the switch would need a local control run of the unchanged configuration (not run). The old
  k-NN-era ladder read +0.029 (`MPPDE_L5_nopad_f2`, also inside the floor); this run does not repeat it.
  Author decision (2026-10-18): no gain, so the option is not mentioned in the thesis until it has been
  run properly. Commented out: the §3.3 sentence, the §4.5.1 sentence and the "Pad-position masking"
  row of Table `tab:method:hparams` (each with its replacement text in a comment). A fourth objective
  test is prepared, commented out, at the end of §5.4.2: the paragraph with `[TODO]` slots and the
  steps to enable it (no numbers; the local pilot appears only in a comment, marked not for the text).
- [ ] TODO (cluster, as soon as A6000 access is back): run the pad-exclusion ablation on the canonical
  stencil, 5 folds, seed 42:
  `EXCLUDE_PAD_NODES=True EXP_TAG=dilmean_nopad ARM=sb sbatch --array=0-4 --gres=gpu:nva6000:1 ~/jobs/train_solver.slurm`
  (BACKBONE=anisognn and GNN_AGGR=mean are the slurm defaults; before submitting, check that the args
  diff against `ANISOGNN_final_dilmean` is only `exclude_pad_nodes` and the experiment name). Read out with
  `thesis_numbers.py pair ANISOGNN_final_dilmean_nopad ANISOGNN_final_dilmean`, plus the
  border/interior split, then decide whether to enable the prepared §5.4.2 paragraph (steps listed
  in the comment there). ~1 h per fold on an A6000.
- [ ] **U-Net run-to-run spread, local repeats on fold 2 (2026-10-18; for SV-5.2, the z-test with an
  empirical sigma; author to decide which sigma_U enters §5.1.5 / App. E).** Parameter-matched U-Net
  (`UNET_final_w5`, 83,081 params), fold 2, retrained three times on the RTX 5080 (seed 42, seed 42, seed 7),
  30 epochs each. Command line copied from the reference run's `solver-7841338.out`; args diff only
  experiment, device, input path, save_dir, num_epochs (smoke test) and flags added to the code later, all at
  their defaults (`weight_decay 0.01` = AdamW's old implicit default; `gnn_aggr mean_max` kept as in the
  reference, inert for the U-Net). Persistence Dice@360d identical (0.86748). Launcher, analysis scripts
  (`analyse.py`, `seedspread.py`) and runs: `images/data/unet_repeats/` (git-ignored). Late mean of
  `change_region_dice_360d`, epochs 10-29:

  | run | late mean | sd over late epochs | s/epoch min / median | wall-clock |
  |---|---:|---:|---:|---:|
  | cluster A6000, seed 42 (`UNET_final_w5_f2`) | 0.5918 | 0.0106 | 21.0 / 32.7 | |
  | cluster A6000, seed 7 (`UNET_final_w5s7_f2`) | 0.5787 | 0.0213 | 46.2 / 81.4 | |
  | local RTX 5080, seed 42, run 1 | 0.5827 | 0.0126 | 10.7 / 12.2 | 7.0 min |
  | local RTX 5080, seed 42, run 2 | 0.5827 | 0.0126 | 10.7 / 12.4 | 7.0 min |
  | local RTX 5080, seed 7 | 0.5875 | 0.0110 | 10.0 / 12.4 | 7.0 min |

  - **The two local seed-42 runs are bit-identical** (Dice and train RMSE at every epoch): the U-Net trains
    deterministically on this GPU (unlike the graph networks, whose same-seed repeats differ). The same-seed
    repeat therefore adds no information; locally there are two independent runs, not three.
  - Single-run sd on fold 2 (convention of the 0.0127: sd of one run; pair = |d|/sqrt 2): local seed pair
    0.0034; cluster seed pair 0.0092; local three runs (formally) 0.0028, 90 % CI 0.0016-0.0124 (df 2, but
    not valid, see above); all five runs 0.0050, 90 % CI 0.0033-0.0120; the four independent runs 0.0057,
    90 % CI 0.0035-0.0166 (df 3). Pairwise: cluster s42 - s7 +0.0131; cluster - local s42 +0.0091; local s42
    - s7 -0.0049; cluster s7 - local s7 -0.0088. **On fold 2 the U-Net varies less than the graph networks
    (about 0.4-0.45 x 0.0127), and hardware adds at most about 0.009.**
  - **But the "one pair" premise is wrong, and fold 2 is a quiet fold.** The cluster has a seed-42/seed-7
    pair of the U-Net on every fold (late means): f0 +0.0041, f1 -0.0301, f2 +0.0131, f3 -0.0480, f4 -0.0155.
    Pooled single-run sd sqrt(mean(d^2)/2) = **0.0191** (df 5, 90 % CI 0.0128-0.0399), 1.50 x 0.0127; with
    the local fold-2 seed pair added 0.0175 (df 6, CI 0.0121-0.0335). Same estimator on the graph networks'
    own seed pairs: dilated stencil 0.0111, k-NN (mean) 0.0069, so the U-Net spreads 1.7 x the stencil and
    2.8 x the k-NN network. The "1.9 x" in App. E (`app:full-results:criteria`) was not reproduced from these
    runs; check its source. The spread is carried by folds 1 and 3; the fold-2 repeats cannot tell whether
    those two pairs are unlucky. A fold-1 repeat is possible locally (precompute exists, ~7 min per run);
    fold 3 is not (no local precompute).
  - z-tests with a U-Net on one side, sigma_Delta = sqrt(0.0127^2 + sigma_U^2) / sqrt 5 (* = |z| > 1.96;
    other side assumed 0.0127, also for the FNOs), seed 42 / seed 7:

    | comparison | mean s42 / s7 | sigma_U 0.0127 (sD 0.0080) | 0.0191, cluster 5 folds (sD 0.0103) | 0.0241 = 1.9 x (sD 0.0122) | 0.0050, fold 2 only (sD 0.0061) |
    |---|---|---|---|---|---|
    | dilated stencil - U-Net | +0.0212 / +0.0081 | +2.64* / +1.01 | +2.07* / +0.79 | +1.74 / +0.66 | +3.47* / +1.33 |
    | T-FEN - U-Net | +0.0383 / +0.0246 | +4.77* / +3.06* | +3.73* / +2.40* | +3.14* / +2.02* | +6.27* / +4.02* |
    | U-Net - k-NN | +0.0423 / +0.0548 | +5.27* / +6.82* | +4.12* / +5.34* | +3.47* / +4.49* | +6.92* / +8.97* |
    | FNO - U-Net | -0.0215 / -0.0136 | -2.68* / -1.69 | -2.10* / -1.33 | -1.76 / -1.12 | -3.52* / -2.23* |
    | FNO+3x3 - U-Net | -0.0061 / -0.0193 | -0.76 / -2.40* | -0.59 / -1.88 | -0.50 / -1.58 | -1.00 / -3.16* |

    Robust under every sigma_U: T-FEN above the U-Net and U-Net above the k-NN network at both seeds; the
    stencil - U-Net difference never counts at seed 7. Borderline (depend on sigma_U): stencil - U-Net and
    FNO - U-Net at seed 42 (count at 0.0191, not at 1.9 x); FNO+3x3 - U-Net at seed 7. The fold-2 value
    (0.0050) would make the FNO arms count at seed 7 as well; it should not be used, since the U-Net's spread
    differs between folds. Recommendation: use the five-fold cluster estimate 0.0191 (sigma_Delta about 0.010,
    threshold about 0.020, i.e. the 0.020 already in the text).

### Writing guide from Skern (2026-10-22)

- [x] 2026-10-22: `WRITING_GUIDE.md` written from Tim Skern, *Writing Scientific English: A
  Workbook* (2009), read in full: formal-English rules, the eight clarity guidelines, linking
  words, document structure mapped onto the thesis chapters, tenses, summarising without
  plagiarism, revision passes, a list of where the book conflicts with CLAUDE.md / the supervisor
  (active voice and *we* vs the passive rule: resolved as impersonal active subjects), and a
  one-page checklist. Advisory only; no `.tex` file changed.
- [ ] Optional, from the guide's scan of the chapter files (comments excluded): about 28 sentences
  open with *Because* (e.g. `02-background.tex:404`, `04-method.tex:165`, `05-experiments.tex:141`);
  `03-data.tex:448` "The data is partitioned" (-> "are"); 12 em-dashes (`---`) in prose or tables;
  the title-page keywords partly repeat the title (the guide suggests terms that extend it).
- [x] (author 2026-10-22: no) Decide whether CLAUDE.md "Writing Style" should point to `WRITING_GUIDE.md`.
- [ ] 2026-10-22: `prompts/PROMPT_full_review.md` written: full-thesis review from six perspectives
  (supervisor, external reviewer, examiner, colleague, clinical reader, copy editor) against
  `WRITING_GUIDE.md`, with severities S1-S4, a settled-decisions list, a verification step and one
  sequential findings list (`reviews/full-review-<date>/`). Not run yet.
- [x] 2026-10-22: supervisor's writing instructions from the e-mails of reviews 1 and 2 checked
  against the guide; most were missing and are now its §11 (abstract, prerequisite audit,
  opening-chapter order, intro/body/conclusion per section, LLM sentence patterns, one table or
  plot per results subsection, contributions as bullets, figure tools).

### Consolidated feedback log (2026-10-22)

- [x] 2026-10-22: `reviews/feedback-log-2026-10-22.md` collects all feedback in order: supervisor
  review 1 (34 items: 23 done, 2 decided, 7 deferred = abstract), supervisor review 2 (53 items:
  39 done, 3 decided, 11 open or partly), the AI review's structural items (69: 44 done) and all 544
  AI sentence items (437 done, 74 superseded by later rewrites, 12 decided, 10 deferred = abstract,
  11 open, 10 of them in Appendices A-F). Each item gives the feedback, the issue and the fix with date
  and commit. The status of every AI item was checked against today's `.tex` (old passage still
  present? suggested wording present?), and the passage was located by a line diff from the reviewed
  commit `08534e6`.
- [x] (fixed 2026-10-22: caption back to "the full cohort from which the data here are drawn") Cohort wording is inconsistent: after SV-3.1, §2.4 and §3.1 say the data are the Mai et al.
  (2024) cohort with tighter registration and cleaner segmentations, but `238a8bc` (2026-10-22) set the
  horizon-figure caption to "a larger cohort of the same clinic" (`05-experiments.tex:806`). Pick one.
- [ ] Open AI items in Appendices A-F (A.1, A.3, A.6-A.11, A.13, A.14; neither supervisor review
  covered the appendices) and G.40; structural items still open: S13/R15 (shrinkage quantified only in
  §6.3), T7 (Ch. 7 re-runs §6.1), T13 (Appendices B and C empty, App. E titled "Ablation Details"),
  R11, R16, the 365.25 footnote of S24.

### Assets that now exist and should be reused

- **The Practical Work report** (`masterthesis-docker/practical/`) was handed in
  2026-08-27: a complete LaTeX report (abstract → conclusion + appendix) with
  `results.json` as the single source of numbers and `scripts/` that regenerate every
  figure and table (`fig_curves`, `fig_folds`, `fig_growth`, `fig_mechanism`, `fig_mesh`,
  `fig_rollout`, `fig_scatter`, plus `main_results`, `per_fold`, `growth_dice`, `hparams`
  tables). Much of Chapters 3–5 can be built on this rather than from scratch, and the
  figure scripts mean thesis figures can be *generated* rather than left as placeholders.
  ⚠️ It predates the 2026-09-03 v2 lock and the T-FEN / RK4 / solver-swap results —
  check every number against `THESIS_FRAMEWORK.md` §7.5 before reuse.
  `practical/CONTEXT.md` §3 lists claims that must not drift, §5 what is superseded.
- **The supervisor deck** (`masterthesis-docker/presentation/`): a 9-slide "state of the
  project" built from verified numbers, plus `SUPERVISOR_PRACTICAL_FINAL.md` (§0 answers
  "why did a plain U-Net outperform the original GNN?", §7 a suggested storyline). Useful
  as a ready-made narrative spine for the thesis.
- **The poster** (`masterthesis-docker/poster/`) and the 2026-06-30 reviewer feedback that
  asked for external baselines from other architecture classes — **that feedback has now
  been answered in full** (U-Net, FNO, hybrid, graph U-Net, FEN, per-pixel floor), except
  a plain RNN and a transformer, which remain unrun.

### Still open / still pending numbers

- [ ] A plain **RNN** and a **transformer** baseline remain unrun (`--backbone` offers
  `gnn`/`unet`/`fno`/`gunet`/`anisognn`/`fen`). The supervisor asked for the RNN.
- [ ] A **cohort-level baseline-area distribution table** comparable to Mai et al. 2024 is
  still missing for the data chapter; growth-rate statistics exist (median √area growth
  0.234 mm/yr, IQR 0.153–0.340, p90 0.473 over 75 eyes).
- [x] (superseded 2026-10-01: matched control run; reported T-FEN is the stable skew form) The **T-FEN transport term has no matched-capacity control** (a width-≈139 control
  has never been run); the 45-day T-FEN is **not a valid long-horizon integrator** as
  trained (5/10 runs diverge free-running, 9/10 final checkpoints exceed the Courant
  bound) — the learned velocity map is **not quotable**, though the Dice contribution
  stands.
- [ ] **Mai et al. 2024** (Ophthalmology Science) remains the direct comparison paper —
  same MUW cohort, same task. Our growth-region Dice is higher, **with the mandatory
  caveat that this model takes pre-segmented masks as input whereas Mai works from raw
  OCT**. Needs a `references.bib` entry.
  ✔ 2026-10-01 (later): checked -- higher in every bin (0.50-0.66 vs 0.25-0.38), same metric definition,
  different inputs / FOV / visit sets; now in §5.5.1. Earlier note:
  ⚠️ 2026-10-01: "our growth-region Dice is higher" is **unverified** — never checked against
  Mai's Table 2 (growth-region DSC 0.25 / 0.38 / 0.38 / 0.37 for 0–1 / 1–2 / 2–3 / >3 y). On
  growth *speed* the canonical model is clearly **weaker** than Mai (r 0.40 vs 0.61). Do not
  quote the old claim; see §5.5 inline TODO. (Mai2024 is in references.bib since 2026-09-26.)
- [x] (2026-10-01: net decrease in 5 % of 478 pairs, local border loss in 96 %, median 2.2 % of the lesion; in §6.3) Ground-truth GA **retraction/shrinkage** between visits should be quantified before
  it is discussed in Limitations.

---

## Code-side architecture & results sync (2026-07-26) — SUPERSEDED by the 2026-09-17 sync above; retained as history

Pulled from the code repository (`masterthesis-docker/NOTES.md` + `PROJECT_CONTEXT.md`) to bring the thesis context current for writing. `PROJECT_CONTEXT.md` in this repo has been **re-mirrored** on this date (it had been stale since 2026-04-19, predating the SLO-mask DMM redesign, the α-gate divergence fix, and the res_cut removal). The items below post-date the 2026-05-02 chapter drafts and change what several sections must say. **Consult the refreshed `PROJECT_CONTEXT.md` before drafting any technical section.**

### Architecture as it now stands (supersedes earlier drafts)

- **The DMM trains on a single-channel SLO mask, not the multi-channel OCT state.** The mesh mover is trained on the high-resolution SLO segmentation cropped to the OCT field-of-view and downsampled to a square 256² grid; at MM-PDE inference the trunk is queried at the OCT (49×1024) grid. The monitor is therefore a **plain scalar** monitor on the (Gaussian-blurred) binary mask. The **multi-channel Frobenius-norm monitor was a superseded workaround** for the OCT-direct path and is no longer part of the final design. See `PROJECT_CONTEXT.md` §2.
  - [ ] TODO (⚠️ affects committed prose): `01-introduction.tex` §1.4 (Contributions, ~line 228) still claims the multi-channel Frobenius monitor as a contribution ("reformulating the monitor function in terms of the Frobenius norm of the per-channel spatial gradient"), and the §1.5 outline (~line 266) says "data-free mesh mover for vector-valued GA states". Both need reframing to the single-channel SLO-mask design. Decide with supervisor how to frame the DMM contribution (train/inference grid decoupling via the SLO mask, vs. keeping the Frobenius monitor as a documented intermediate step). An inline `% NOTE` marker has been left at the contribution bullet.
  - [ ] TODO (⚠️): `THESIS_STRUCTURE.md` §4.3 and `04-method.tex` §4.3 placeholder still list a "Frobenius-norm monitor function for vector-valued state" — correct when drafting §4.3/§4.4.

- **Dual-branch composition, final form:** $pred = u + \Delta t\,f_\theta + \alpha\,\tilde{I}[\Delta t\,g_\theta]$.
  - $\alpha$ is a **learnable scalar gate** (initialised 0): the moved branch starts inert and must earn its contribution; $\alpha$ also pins the moved term's scale (the loss constrains only the *sum* of the branches).
  - $\tilde{I}$ is ItpNet interpolation **renormalised to a partition of unity** (row-sums = 1).
  - **`res_cut` was removed entirely** (the per-timestep CNN correction term added into the velocity). It compounded over the autoregressive rollout and drove divergence; it was first defaulted off, then cut from the framework. See `PROJECT_CONTEXT.md` §3.
  - [ ] TODO (⚠️): `THESIS_STRUCTURE.md` §4.3 and `04-method.tex` §4.3 still mention "multi-channel res_cut Conv2d" — remove when drafting. §4.6 (dual-branch) should describe the $\alpha$-gate.

- **Intermediate-time-point regulariser: evaluated and removed (negative result).** The supervisor's sub-$\Delta t$ linear-interpolant regulariser (2026-05-21) showed no benefit in the ablations and was removed 2026-06-11. Reportable in the Discussion as a negative result; historical runs remain reproducible from their git SHAs. See `PROJECT_CONTEXT.md` §5.

- **Other adaptations now in the code** (relevant to Method / Experiments, not yet in any draft): soft **monotonic-mask growth penalty** (encodes the clinical "GA does not heal" prior — but note the retraction caveat below); **`mean_max` GNN neighbour aggregation** (default, replacing plain mean); **time-budgeted pushforward** (unroll depth measured in elapsed days / 90-day units, not visit count; `--unrolling` default = 4 = 360 d); **anisotropy-corrected k-NN** (edges built on integer index coords, not physical-mm, so the 49-axis actually carries message passing); a **fixed MLP decoder** replacing the upstream conv1d head (removed a rank-1 output bottleneck and the old `hidden_dim ≥ 113` constraint); optional **per-visit age encoding** (`--age_mode per_visit`, default off = frozen baseline age).
  - Open clinical-modelling question logged code-side: GT segmentations show some GA **retraction** between visits, which contradicts the strict monotonic-growth prior the loss leans on. Worth a sentence in Discussion / Limitations once quantified.

### Results now available (thesis-bound; still verify from a named run before quoting)

- **DMM mesh-mover — the canonical branch is the compact `pool` CNN (~1.13 M params), not the 5.27 M `conv7`.** A full-cohort DMM retrain + capacity/overfitting study (mesh-quality metrics: Huang & Russell equidistribution CoV, non-tangling / tangled-cell count, geometric quality $Q_{geo}$) found the 5.27 M `conv7` branch **overfits** (worst held-out mesh CoV, +75 % train→val gap, seed-unstable), while `pool` generalises best (CoV 0.448 ± 0.006 over seeds, 0 tangled). Both are carried downstream. This is the substance of Methods/Experiments §5.5 (moving-mesh quality) and is a reviewer-requested justification for the smaller architecture. Reproducible via the code repo's `mesh_quality_metrics.py`.

- **α-trajectory — the headline dual-branch finding (PRELIMINARY: split-2, n = 16 val, one fold).** The moved-branch gate $\alpha$ engages **only for a well-generalising mesh**: the canonical `pool` DMM → $\alpha \approx -0.31$ (branch active), change-region Dice ≈ 0.51; single-branch ≈ 0.46; a **parameter-matched uniform-mesh control** (`--bypass_dmm_move`) → $\alpha \approx +0.01$ (inert), ≈ 0.44; the overfitting `conv7` DMM → $\alpha \approx +0.01$ (inert), ≈ 0.44. So the **mesh geometry, not the extra parameters**, is what helps, and the gain is in **stability/variance rather than peak Dice** (peaks are indistinguishable; the full-30-epoch mean gap is smaller, ~+0.015). This directly answers the thesis's central question — *does moving-mesh adaptation transfer to slow-progressing GA?* — and should be a figure ($\alpha$ vs. epoch for the three runs). ⚠️ One fold only; 5-fold CV + seeds pending before it is quotable as final.

- **Mai et al. 2024 (Ophthalmology Science) is the direct comparison paper** — same MUW cohort, same task, same en-face deliverable. Cohort metrics matching their Table 2 / Figs 3–4 are implemented: time-binned total & growth-region Dice, √area MAE, growth-rate Pearson r / R², fast-progressor AUC. Our growth-region Dice is substantially higher than Mai's reported bins — **with the mandatory caveat** that this model takes **pre-segmented masks** as input whereas Mai works from raw OCT (state this explicitly in Experiments/Discussion; it is part of *why* a local model suffices).

- **Reviewer / poster feedback (2026-06-30): external baselines from a different architecture class are needed.** The MP-PDE vs MM-PDE comparison is same-class (both local GNNs) and cannot on its own justify the architecture *class*. Reviewers asked for a baseline of a different inductive bias — U-Net / CNN, a transformer (global attention), plus a plain-RNN / per-pixel-MLP floor (supervisor also asked for the RNN) — **capacity- and FLOP-matched**, framed as a low-data inductive-bias argument (high-bias models win when data is scarce). Not yet built. Affects Experiments §5.2 (baselines) and likely adds an "inductive-bias study" subsection; the fair-comparison point also applies to the current MP-PDE (727 k) vs MM-PDE (2.65 M) param gap.

### Pending numbers (leave `% TODO:` placeholders — do NOT invent)

- Main results table (single vs dual-branch × {`pool`, `conv7`} DMM, 5-fold mean ± SD; Dice@360d, IoU@360d, param count) — solver stage launched on the cluster, CV pending.
- Ablation tables (single-branch, dual-branch, encoder `d_embed` sweep, covariates on/off) — pending runs.
- DMM mesh-quality table — data exists (see above), needs writing up.
- Headline "does the moving mesh help" number — currently only the preliminary single-fold α study above.

## Open TODOs

### Title page / metadata (`main-thesis.tex`)

- [ ] TODO: finalize thesis title with supervisor (current working title: "Neural PDE Solvers for Geographic Atrophy Progression Prediction from Longitudinal OCT Imaging").
- [ ] TODO: fill in author name, academic prefix/suffix, and matriculation number on the title page.
- [ ] TODO: confirm exact JKU degree program name (currently placeholder "Artificial Intelligence").
- [ ] TODO: confirm submitting JKU institute (currently placeholder "Institute for Machine Learning").
- [ ] TODO: set submission date once known.

### Front matter

- [ ] TODO: write English abstract covering problem, approach, contributions, headline results (`00-abstract.tex`).
- [ ] TODO: write German `Kurzfassung` (translation of the English abstract) (`00-abstract.tex`).
- [ ] TODO: write acknowledgements to MUW, Hrvoje Bogunović, and Dmitrii Lachinov (`acknowledgements.tex`).

### Chapter 1 - Introduction (`01-introduction.tex`)

- [x] 2026-05-02: 1.1 Clinical motivation drafted (GA as advanced AMD, epidemiology, age dependence, bilaterality, complement-inhibitor era; cites Flaxman2020, Boopathiraj2024, Trincao2024, Vallino2024, Singh2025, Song2025, Yehoshua2011, Boyer2017, Lad2023).
- [x] 2026-05-02: 1.2 Problem statement drafted (spatiotemporal forecasting on OCT en-face, irregular intervals, multi-channel state, covariates; cites Vogl2021, Vallino2024, Chu2022).
- [x] 2026-05-02: 1.3 Why neural PDE solvers drafted (boundary growth model, anisotropy, MP-PDE/MM-PDE; cites Yehoshua2011, Chu2022, Singh2025, Brandstetter2022, Hu2024, Vogl2021, Vallino2024). Locked-in research question included as a blockquote at the end of 1.3.
- [x] 2026-05-02: 1.4 Contributions bullets drafted (six contributions covering MM-PDE transfer, $\Delta t$-residual, multi-channel monitor, covariates, surrogate encoder, empirical validation).
- [x] 2026-05-02: 1.5 Thesis outline paragraph drafted; uses `\ref{ch:...}` cross-references to chapters 2-7.
- [x] 2026-09-25 (all resolve; stale TODO comment removed from the .tex): confirm `\ref{ch:background}`, `\ref{ch:data}`, `\ref{ch:method}`, `\ref{ch:experiments}`, `\ref{ch:discussion}`, `\ref{ch:conclusion}` resolve once the corresponding `\label{}` commands exist in the chapter source files (currently those chapters are placeholders).
- [ ] TODO: re-read 1.1 prevalence numbers against the latest cohort statistics extracted from MUW data once available; the figures cited (1M US / 5M global, 160k new dx/yr, 14-27% growth-rate reduction) follow Singh2025 / Vallino2024 / Lad2023 verbatim.

### Chapter 2 - Background (`02-background.tex`)

- [x] 2026-05-02: 2.1 GA and OCT imaging drafted (subsections: disease on OCT, OCT principle, en-face projections, eleven-channel state representation, MUW cohort; cites Boopathiraj2024, Boyer2017, Vallino2024, Yehoshua2011, Pilotto2015, Chu2022, Vogl2021, Ebneter2016).
- [x] 2026-05-02: 2.1.1 prose softened for an ML-literate but clinically-non-expert audience (added plain-language opener, "in other words" / "concretely" / "put differently" glosses, and a self-contained explanation of cRORA before the formal three-criterion definition). Inline `% TODO` markers preserved.
- [x] 2026-05-02: 2.1.4 rewritten to drop unsupported claims about the MUW segmentation pipeline (removed: "obtained from a trained segmentation network", "ground-truth annotations produced by clinical graders following Vallino2024", "Chu2022 thresholding rule used as complementary check", "standard output of the Iowa reference layer segmentation algorithm with the drusen-aware modification of Vogl2021"). Replaced with a structural description of channels 0 and 1--10 that is agnostic of the specific provenance, with operational details deferred to `03-data.tex` §3.1. The ONL+HFL non-separability and ORB composite-band caveats were retained but reframed as inherent to SD-OCT rather than to the MUW pipeline. Bogunovic2017 reuse claim in `02-background.tex` was removed accordingly (entry in "Pending external citations" section updated).
- [x] 2026-05-02: 2.1.5 speculative sentence about Vogl2021 as the "institutional precedent for the spatial standardisation pipeline" (with HARBOR-cohort + ONH-rotation details) removed; replaced with a leaner paragraph that defers operational preprocessing details to `03-data.tex` §3.3. The user noted the sentence made an unsupported provenance claim and was hard to follow without the underlying paper.
- [x] 2026-05-02: added new §2.1.1 "A short anatomy primer" at the start of §2.1, before "Geographic Atrophy on OCT". Subsections renumber: anatomy primer = §2.1.1; GA on OCT = §2.1.2; OCT principle = §2.1.3; en-face projections = §2.1.4 (the one the user said was fine, content unchanged); state representation = §2.1.5; MUW cohort = §2.1.6. Subsection labels are topic-named (e.g. `sec:background:ga-oct:disease`), so cross-references continue to resolve.
- [x] 2026-05-02: §2.1.3 OCT-acquisition explanation softened. Replaced the dense "low-coherence interferometry / sample arm / reference arm / spectral interference pattern" sentence with a slower account that uses an ultrasound analogy, motivates why interferometry is needed, and walks through A-scan -> B-scan -> volume step by step with cross-references to the new figure placeholder. The SD-OCT vs SS-OCT paragraph and the FAF comparison remain unchanged.
- [x] 2026-05-02: 2.2 PDEs and numerical solvers drafted using SWE as running example (subsections: temporal PDEs and conservation form, method of lines, FDM/FVM stencils, time integration, uniform vs adaptive meshes; cites Brandstetter2022, Hu2024, Yehoshua2011, Singh2025; no historical detours).
- [x] 2026-09-17: §2.1.6 corrected against the refreshed code-side facts. Removed the false
  native volume shape (`49 x 1024 x 496`) here and at the two other places it appeared
  (the §2.1.3 body and the `fig:bg:oct-acquisition` figure TODO); the cohort is now
  described as 553 Heidelberg SD-OCT scans over 75 eyes with 38--66 B-scans x 961--1719
  A-scans and 67 distinct native shapes, with `49 x 1024` named as the *modelling* grid
  reached by symmetric centre-crop or zero-pad. The constant-spacing assumption is stated
  as an assumption (~2 % tolerance) with an inline `% TODO` pointing at the DICOM fields.
  The `\citet{Pilotto2015}` ninety-nine-per-cent statement is retained as literature
  precedent but no longer carries the justification: the measured censoring census
  (27.3 % of visits lose real lesion area, worst case 25.7 %, 31.1 % of cropped lesions
  touch the border) now follows it directly. The clause that shifted "within-window
  heterogeneity onto the moving-mesh inductive bias" was deleted — the moving mesh is a
  tested hypothesis, not an assumption.
- [x] 2026-09-17: §2.1.1 fixed a pre-existing miscount ("three concentric anatomical
  zones" followed by four items: foveola, fovea, parafovea, perifovea).
- [x] 2026-09-17: 2.3 drafted and retitled "Neural PDE Solvers and Surrogate
  Architectures" (label `sec:background:neural-pde` unchanged). Widened past the original
  operators-vs-autoregressive stub so that every architecture class later surveyed in
  Chapter 4 has its background here: neural operators (FNO, DeepONet) and their
  equation-family limitation; why the autoregressive framing fits irregular clinical
  visits; the distribution-shift cost of autoregression; then the U-Net, global-spectral
  vs local operators and the local-kernel hybrid, graph U-Nets, Finite Element Networks
  with a transport term, and the Neural-ODE reading *with* the solver-invariance caveat
  stated as something that must be tested. Closes by naming the "inductive-bias
  ingredient" vocabulary that Chapter 5 measures, without previewing any outcome.
- [x] 2026-09-17: 2.4 MP-PDE drafted (graph-as-stencil analogy, encode--process--decode,
  encoder/message/update functions, the $\theta_{PDE}$ equation feature vector and why it
  is injected at every layer, the 1-D CNN decoder and residual Euler update, temporal
  bundling, the pushforward trick and its zero-stability reading, model scale, the
  paper's own three limitations). Ends with two sentences of forward reference: the
  residual update and pushforward are kept, $\Delta t$-conditioning is added, temporal
  bundling is removed entirely.
- [x] 2026-09-17: 2.5 MM-PDE drafted (uniform-mesh inefficiency, $h$- vs $r$-adaptation,
  the monitor function, the equidistribution principle, optimal transport and Brenier to
  the Monge--Ampère equation, why a scalar potential is learned, the residual
  reformulation, the DMM's DeepONet architecture and its three-term data-free physics
  loss, freezing, the dual-branch composition, ItpNet and its pretraining, the paper's
  ablations). **Closing paragraph checked against the constraint**: mesh adaptation is
  framed as an open question this thesis tests, not as the thesis's architecture, and the
  multi-channel monitor question is deferred to Chapter 4 without naming any formulation.
- [x] 2026-09-17: 2.6 Related work drafted (cohort-level AI-on-OCT precedents; **Mai et
  al. 2024 named as the closest prior work on the same MUW cohort, with the
  pre-segmented-masks vs raw-OCT input-regime difference stated in the same paragraph**;
  Salvi et al. 2025 as the dense-CNN precedent on FAF; the positioning contrast between
  categorical time-to-conversion prediction and per-eye per-time-step spatial
  prediction). Left an inline `% TODO` asking for a literature check on neural PDE
  solvers applied to other biomedical problems rather than inventing examples.
- [x] 2026-09-17: chapter compiles (`latexmk -xelatex`), zero unresolved `\ref`s. Chapter 2
  now spans pages 6--23 (~18 pages) against the ~12--15 in `THESIS_STRUCTURE.md`; §2.1 is
  ~8 pages of that. Decide whether to trim §2.1 or raise the chapter's budget.
- [x] 2026-09-25: §2.2 reworked in full at the author's request (pages 13--19, ~6 pages).
  Structure now follows the MP-PDE paper's own background (§2.1--§2.3 of Brandstetter
  2022): temporal PDEs + conservation form, now *derived* from the integral balance and
  the divergence theorem so it is clear where it comes from; the computational path
  (grids and cells, the method of lines with the origin of the name, the update operator
  $\mathcal{A}$ and the rollout, new pipeline figure); spatial discretisation (FDM with
  the general stencil equation, FVM, WENO, pseudospectral, locality vs global support);
  time integration (Euler, RK, consistency, CFL); a new strengths-and-limits subsection;
  and a new subsection on the step to learned solvers (hybrid vs end-to-end, why they
  work, weather/fluids as examples, what they cost), closing on GA as the "no known
  equation, sparse irregular snapshots" case. The SWE system and its flux matrix were
  removed (one mention remains as an example of a conservation law); the uniform vs
  adaptive mesh subsection was cut to one sentence pointing to the moving-mesh appendix.
  New labels: `eq:bg:conservation-integral`, `eq:bg:update-operator`, `eq:bg:stencil`,
  `eq:bg:cfl`, `fig:bg:solver-path`, `sec:background:pde-solvers:limits`,
  `sec:background:pde-solvers:neural`. Removed labels (none referenced elsewhere):
  `eq:bg:swe-*`, `sec:background:pde-solvers:mesh`. The label
  `sec:background:pde-solvers:time` (used by §4.2) is kept.
  Note: §2.3 opens by re-defining the autoregressive update $\mathcal{A}(\Delta t, u)$,
  which §2.2.2 now introduces; trim that overlap when §2.3 is revised.
- [x] 2026-09-25 (second pass, author feedback): the conservation form was **removed
  entirely** -- it only served to motivate FVM, which the thesis never uses, and the text
  then had to say it does not apply to GA. §2.2 is now: short PDE notation intro ->
  2.2.1 stencils (FDM, general stencil eq., FVM in one sentence, WENO as adaptive stencil,
  pseudospectral as global, locality and reach) -> 2.2.2 stepping in time (method of lines,
  Euler/RK, update operator + rollout, consistency/residual form, CFL) -> 2.2.3 strengths
  and limits -> 2.2.4 neural solvers that keep the mechanisms (hybrid, end-to-end, MP-PDE
  as the explicit case) -> 2.2.5 why this structure suits GA (fixed grid, neighbourhood-
  driven change, slow change, irregular steps; framed as expectations, not evidence; the
  CFL argument motivates the reach question without previewing results). Pages 13--17.
  Labels removed: `eq:bg:conservation-integral`, `eq:bg:conservation-form`,
  `sec:background:pde-solvers:problem`, `sec:background:pde-solvers:mol`; new:
  `sec:background:pde-solvers:ga`. The LeVeque2002 marker now only backs the convergence
  sentence in §2.2.3; the "moving-mesh appendix" pointer TODO below is obsolete (the
  sentence was cut).
- [x] 2026-09-25 (third pass): "method of lines" name, the Schiesser citation and the ODE
  equation `eq:bg:mol-ode` removed from §2.2.2 (nothing referenced them). Kept the idea in
  plain words: stencils yield a rate function f, and any time-stepping scheme can advance
  it -- the split that the swappable slot, the RK4 arm (§4.4.5) and the solver-swap
  diagnostic (§5.6) rely on. The Schiesser2012 pending citation is therefore obsolete.
  **Author to review §2.2 on 2026-09-26.** (Done: tablet review v2, 2026-09-26, marks #1-#14.)
- [x] (2.3 repeat fixed 2026-10-01; THESIS_STRUCTURE part still open) TODO (from the 2026-09-25 §2.2 rework, still open 2026-10-01): §2.3 opens by defining
  the autoregressive update again as plain $A(\Delta t, u(t))$, although §2.2.2 introduces it
  as $\mathcal{A}$ (`eq:bg:update-operator`); remove the repeat or point back, one symbol.
  Also: THESIS_STRUCTURE.md §2.2 entry still names the method of lines and omits the FEM
  paragraph. Overview of this session's open items: `prompts/open.txt` section 11 [s25].
- [x] (done 2026-10-20) TODO: produce Figure `fig:bg:solver-path` (§2.2.2) -- the classical computational
  path as a pipeline: continuous field -> grid of cell values -> spatial discretisation
  (one cell and its stencil, yielding f_i) -> time integrator (Euler step) -> next state,
  with a loop arrow labelled "rollout"; the two boxes marked as independent choices.
- [x] (obsolete 2026-09-25, sentence cut) §2.2.5 points to "the appendix" for adaptive meshes / MM-PDE; replace with
  `\ref` to Appendix G once its label exists (inline TODO in the .tex).
- [ ] TODO: §2.3--§2.6 came in shorter than planned (§2.3 ~1.5 pages against a ~2.5-page
  target, §2.4 ~1.5 against ~2). The prose is correct but terse in places; consider a
  depth pass on §2.3 (operator-vs-autoregressive contrast) and §2.4 (message passing as a
  learned stencil) once Chapters 4--5 are drafted and it is clear how much background
  they actually lean on.
- [x] (done 2026-10-16 with Wikimedia Commons images, see the Figure plan) TODO: produce Figure `fig:bg:eye-anatomy` placed in `02-background.tex` §2.1.1 -- two-panel anatomy reference for ML readers without clinical background: (left) sagittal cross-section of the human eye labelling cornea, lens, vitreous body, retina, fovea, optic-nerve head (ONH) / optic disc, optic nerve, choroid, sclera, with the macular region highlighted on the retina near the posterior pole; (right) en-face fundus view of the posterior pole labelling macula (~6 mm-wide central region), fovea (central pit), foveola (innermost ~0.35 mm of the fovea), parafovea (~0.5--1.5 mm eccentric ring), perifovea (~1.5--3 mm eccentric ring), and ONH / optic disc (~4 mm nasal to the fovea). Overlay the 6 x 6 mm OCT scanning window used by the thesis cohort as a dashed square centred on the fovea. Currently rendered as an `\fbox` placeholder pending a real graphic.
- [x] (done 2026-10-16, see the Figure plan) TODO: produce Figure `fig:bg:retinal-anatomy` placed in `02-background.tex` §2.1.2 (formerly §2.1.1) -- two-panel schematic for readers without a clinical background: (left) labelled cross-section through a healthy macula showing the principal retinal layers from ILM through RNFL, GCL+IPL, INL+OPL, ONL, photoreceptor IS/OS bands (including the ellipsoid zone), RPE, and Bruch's membrane, with the choriocapillaris immediately beneath; (right) a representative OCT B-scan through a GA-affected macula highlighting the dropout of the outer-retinal layers within the lesion and the corresponding choroidal hypertransmission signature beneath. Mirror the channel ordering of the eleven-channel state tensor used in the thesis. Currently rendered as an `\fbox` placeholder pending a real graphic.
- [x] (done 2026-10-16, two panels instead of four) TODO: produce Figure `fig:bg:oct-acquisition` placed in `02-background.tex` §2.1.3 -- four-panel schematic of OCT acquisition geometry intended to anchor the geometric vocabulary (A-scan, B-scan, volume, en-face) for ML readers without imaging background: (a) eye + single probe beam + inset depth-vs-reflectivity profile of one A-scan; (b) the same with the beam scanned laterally along one axis to form a B-scan; (c) the beam scanned in both lateral directions to form a 3D volume with the 6 x 6 mm physical footprint annotated (do NOT annotate a fixed voxel count -- native shapes vary per eye: 38-66 B-scans x 961-1719 A-scans, 67 distinct shapes); (d) the volume projected axially onto the fundus plane to yield the 49 x 1024 en-face image used by the model, with a representative GA lesion visible as a region of altered signal. Currently rendered as an `\fbox` placeholder pending a real graphic.
- [ ] TODO: confirm with supervisor the exact provenance of the eleven state-tensor channels in the MUW cohort (mask: manual grading vs trained network vs combination; layer boundaries: which segmentation algorithm, which boundary list, which post-processing) before drafting `03-data.tex` §3.1. The §2.1.4 text is currently agnostic of those details so it does not need to be revisited once the answer is in hand.

### Chapter 3 - Data and Preprocessing (`03-data.tex`)

- [x] 2026-09-18: Chapter 3 drafted in full (§3.1--§3.7, pages 24--31, ~8 pages against the
  8--10 budget) from an external-LLM draft built on a fact sheet taken from
  `THESIS_FRAMEWORK.md` §1--§2, then audited line by line against that source. Every
  number in the draft matched the source, including the mask normalisation statistics it
  derived (mean 0.266, std 0.442, which reproduce the +0.529 threshold). The prose around
  the numbers needed these corrections:
  - **Factually wrong, fixed:** the schedule-reach figures (0/75 at 90 d, 74/75 at 360 d,
    68/75 and 73/75 at two or more steps) were attributed to *evaluation/inference*; they
    are the **training pushforward budget**, and "73/75 reach an evaluation point" was
    invented (it is "at least two steps"). "About 19 % of the border-touching lesions" had
    the wrong denominator (it is about 19 % of lesions whose border contact cannot be
    avoided by any window). "Two affine transformation matrices" became two transform
    *files*. 0.003867 mm was called the axial *resolution*; it is the axial pixel spacing.
    "The standard deviation is floored to a small constant" became "a vanishing standard
    deviation is replaced by one". "Mapping the prediction back into a bounded probability
    space" became "back to the original scale" (the output is a regression, not a
    probability). "Demographic information is integrated into the state" was wrong — the
    covariates accompany each window, they are not state channels.
  - **Would have broken the build:** `\citet{Mai2024}` used a key that is not in
    `references.bib`; replaced by plain "Mai et al. (2024)" plus the `% TODO: cite` marker.
  - **Unsupported claims, removed or neutralised:** "the lesions exhibit continuous
    anatomical progression" (unsupported, and in tension with the observed local
    shrinkage); a §3.2 closing sentence naming "superficial layers, photoreceptors and RPE"
    as what the channels capture and asserting a "richer, more precise" context (names the
    unrecorded layers and asserts a benefit); mask value 0 described as "healthy" (it means
    non-atrophic); "due to segmentation artefacts"; "clinically vital" (bilaterality makes
    eye-level splitting a leakage issue); the claim that uneven patient counts *cause* the
    fold-4 lesion-area imbalance; "the literature precedent for a 6 x 6 mm window via
    cropping" (the literature did not crop); "this geometry dictates the receptive field
    requirements for any spatial operator" (previews a Chapter 5 result); "continuous
    longitudinal observation", "hardware and software setting", "estimated progression
    rate", "strict comparability". Filler intensifiers stripped throughout.
  - **Fixed in my own prompt:** the figure spec asked for "layer boundaries overlaid on an
    en-face image", which is physically incoherent (boundaries are surfaces, visible as
    lines only in B-scans), and the raw B-scans are not in the repository at all. The
    figure (`fig:data:example-state`) is re-specified as SLO fundus + OCT field of view,
    the channel-0 mask at physical aspect ratio, and a layer depth map as a heatmap — all
    producible from repository files.
  - §3.3 retitled "Spatial Standardisation and its Measured Cost", §3.4 "Normalisation",
    §3.7 "Splits and Cross-Validation"; all labels unchanged. The false "99 % / periphery
    irrelevant" placeholder TODO was replaced, not preserved; the string appears nowhere in
    the chapter.
- [ ] TODO: confirm the device model (Heidelberg Spectralis) with the MUW data provider.
  §3.1 currently reports it as an inference from Mai et al. (2024); the data records only
  vendor, scan mode and study identifier.
- [ ] TODO: settle the constant-spacing assumption (~2 % deviation against the visits' own
  transform files) from the DICOM spacing fields. Marked inline in §3.1; also mirrored in
  §2.1.6.
- [x] (done 2026-10-20) TODO: produce Figure `fig:data:example-state` in §3.1 -- (a) SLO fundus image with
  the OCT field of view as a rectangle and the SLO-frame GA mask overlaid; (b) channel 0 on
  the 49 x 1024 grid at the physical aspect ratio (~5.94 x 5.82 mm), so the ~21:1 pixel
  anisotropy is visible; (c) one or two layer depth maps as heatmaps with the mask outline
  overlaid. Mark padded regions. A B-scan panel would need raw data from MUW.
- [x] (obsolete 2026-09-27, table removed in review #2 of §3.4-§4.3) TODO: fill Table `tab:data:norm-stats` (§3.4) -- per-channel mean/std of the ten layer
  channels from `meta["norm_params"]` of the canonical fold (split 2) precompute. Means
  should rise monotonically from ~137 to ~204 axial px.
- [ ] TODO: record the training/validation window counts for folds 0, 1, 3 and 4 (§3.7);
  only fold 2 (378 / 100) is known.
- [ ] TODO: keep every later chapter free of "test set" wording -- §3.7 states that the test
  split is structurally empty and every result is a validation result.
- [ ] TODO: the anatomical names of the ten layer boundaries (§3.2 inline TODO) and the
  cohort-level baseline lesion-area table (§3.1 inline TODO) remain open; both are also
  tracked in the 2026-09-17 sync section above.

### Chapter 4 - Method (`04-method.tex`)

- [x] 2026-09-18: `04-method.tex` skeleton rebuilt to the framework-and-survey outline
  (commit a4c2a15). All labels referenced by Chapters 2-3 kept (`dt-residual`,
  `multichannel`, `training`); new labels `framework`, `mppde:arch`, `graph`,
  `mppde:diff`, `family`, `dual`.
- [x] 2026-09-18: Chapter 4 part 1 drafted (§4.1-§4.3, pages 32-39, ~8 pages) from an
  external-LLM draft with a fact sheet from `THESIS_FRAMEWORK.md` §0.2, §2.5, §4-§4.7,
  §4b.1-§4b.2, then audited line by line **and checked against the MP-PDE paper itself**
  (`pdfs/2202.03376v3_MPPDE.pdf`). Findings:
  - **The external model fabricated paper facts.** It claimed the original's 2-D
    experiments were shallow-water runs using GroupNorm "in Appendix E" and denied that
    the paper pairs ReLU with batch normalisation. The paper's appendix says: Swish +
    instance normalisation for the 1-D experiments (E1-E3, WE1-WE3), ReLU + batch
    normalisation for the 2-D **smoke-inflow** experiments. It also cited the sum
    aggregation as "Eq. 7"; it is Eq. (9). The table now states what the paper says.
  - **Conflict 3 (decoder axis) resolved:** the paper feeds each node's final hidden
    vector into a 1-D CNN, "treat[ing] this vector as a temporally contiguous signal".
    Both earlier descriptions were half right. Chapter 2 §2.4 reworded accordingly.
  - **Residual connection is not a departure:** the paper's appendix states skip
    connections are used in its message-passing layers; the draft (and my own first
    fix) listed it as a change. Removed from the difference table.
  - **Build-breaking, fixed:** `\cleardoddpage` typo, `\ref{experiments:protocol}`
    missing its `sec:` prefix, `\tablefootnote` (package not loaded).
  - **Factually wrong, fixed:** layer channels called "thickness" channels (they are
    boundary depths; thickness is never computed); backbones said to return "the
    predicted change" (they return the full next state); the moved branch said to build
    a *physical* k-NN graph (it cannot -- a physical graph is 100 % in-row); batch norm
    said to use "historical" statistics (training mode uses the current batch);
    "the framework implements strict guardrails enforcing the permuted view" (invented);
    "the moving mesh leaves the layer channels undisturbed" (only the mesh mover reads
    the mask; the moved branch processes all 11 channels); splits called "random".
  - **Framing, fixed:** MP-PDE called a "continuous-time method" three times; Backbone I
    called "the primary structural subject" (contradicts the equal-weight framing); the
    "two halves of equal weight" misread as framework vs operators (it is Backbone I vs
    II); the six architecture classes enumerated in an order the source never gives;
    "the model is effectively blind to the movement of the lesion" and "verified against
    alternative scales" (both preview results).
  - Message/update equations rewritten in the §2.4 notation ($f_i^m$, $\phi$, $\psi$) so
    they compare line by line with the original; the update equation now includes the
    layer normalisation the draft had dropped.
  - The draft came in at roughly 60 % of the word budget again; it now fills ~8 pages,
    which is proportionate for the first three of eight sections.
- [x] (checked 2026-10-17: persistence Dice and IoU at 360 d identical to 12 decimals per fold across all 353 non-superseded final runs; §4.1 reworded) TODO: confirm which persistence-baseline quantities are bit-identical across arms,
  and cite the runs (§4.1 inline TODO). `THESIS_FRAMEWORK.md` §0.2 asserts the
  "bit-identical persistence fingerprints across arms" without defining them.
- [x] (obsolete 2026-09-27: the sizes are no longer quoted anywhere, both inline TODOs removed) TODO: verify the temporal-bundle sizes of the original MP-PDE. The set {20, 25, 50}
  (from code-side notes) could not be found in the paper text; §2.4 carries an inline
  TODO, and the §4.3.3 table states only "K steps".
- [x] (done 2026-10-18, see the Figure plan) TODO: produce Figure `fig:method:pipeline` (§4.1) -- the shared pipeline with the
  operator slot as the one varying box and the moving-mesh branch dashed.
- [x] (done 2026-10-17, author's revised brief: three panels -- physical k-NN, index k-NN,
  dilated stencil -- one orange centre node with its edges, physical distances written on the
  figure; k-NN sets computed by brute force in the script; figure re-enabled, caption rewritten,
  text points to panels a/b/c) TODO: redraw Figure `fig:method:stencils` (§4.3.3) per author review v6 #12 (2026-10-02):
  two plain schematic panels in grid indices -- k = 12 diamond and dilated stencil -- no mm axes,
  no two-round markers, no front-advance lines (supersedes the physical-aspect-ratio spec).
- [ ] TODO (code repo, not editable from here): `THESIS_FRAMEWORK.md` §4.5 still justifies
  the persistence prior with "GA evolves ... monotonically (dead tissue does not heal)".
  That contradicts the locked-off monotonic penalty and the observed local shrinkage.
  Fix it in `masterthesis-docker` and re-mirror; the thesis text rests the prior on slow
  change only.
- [x] 2026-09-18: §4.4 Backbone II drafted (pages 38-46, ~9 pages, level with §4.3) from an
  external-LLM draft built on (a) an implementation fact sheet from `THESIS_FRAMEWORK.md`
  §4b and (b) a **paper fact sheet written from the papers themselves** -- U-Net, FNO,
  localized kernels, Graph U-Nets, FEN, Ott et al., MM-PDE -- read from their PDFs, with
  section/equation locations. Audited line by line. The draft's self-report said "no
  unverified claims were introduced"; that was not true. Corrections:
  - **My fact sheet was ambiguous, the draft picked wrong:** the locality floors are
    truncations of the *index-space k-NN* arm (the ladder's two-round rung, 0.4515, is the
    k-NN model), not of the canonical dilated stencil.
  - **Invented or wrong:** "batch sizes vary" as the reason to avoid batch statistics (the
    reason is the no-gradient training-mode rollout); "the solver restricts the Courant
    number to 2.83" (the limit is *checked*, not enforced -- 9/10 final T-FEN checkpoints
    exceed it); "the FEN formulates the update as a physical transport process" (only the
    transport term does); "the autonomous formulation prevents reach beyond one triangle"
    (reach is limited because one derivative evaluation only couples nodes sharing a
    triangle); the graph U-Net's message function called a "multi-layer perceptron" (one
    shared linear layer + ReLU); a 0.5 mm wavelength described as "the size of small
    lesions" (unsupported); Hu et al. said to have "established" parameter matching (they
    ran a bigger-GNN control); "temporal covariates"; FNO discretisation invariance stated
    as fact rather than as the paper's claim.
  - **Missing from the draft, added:** the FEN free-form MLP's tanh/depth-4/width-96/zero-init
    details and inputs; RK4 with a fixed 45-day step; the 97,632-triangle transport mesh
    as the FE analogue of the dilated stencil; "no-flux boundary is a statement about the
    crop"; the U-Net's nine blocks / 18 normalised sites (the graph U-Net paragraph
    referenced them); "the mode count was not ablated"; the 1.97x gap stated in §4.4.4 as
    well as §4.4.6; the hybrid explicitly "not the resolution-consistent operator".
  - **Table caption claimed all non-control arms lie within 1.25x**; the one-hop floor
    (0.67x) and the free-form FEN (0.52x) do not. Caption and text now say why.
  - Two tables (this one and §4.3.3's) were ~5 pt wider than the text block; narrowed.
    The one remaining overfull-box warning predates this session (template, \output).
- [x] (superseded 2026-10-01 by the skew-form rewrite of §4.3.6: one sentence, RK4 limit ~2.4) TODO: the RK4 stability limit for the T-FEN transport stencil is recorded two ways
  (2.8 as implemented vs ~2.4 derived from a spectral radius of 1.1-1.2). §4.4.4 carries an
  inline TODO. Also confirm "monitored, not enforced during training" against the code;
  it is inferred from the out-of-bound final checkpoints and the parked bounded-velocity
  head.
- [x] (run and reported 2026-10-01, folds 0-3) TODO: a parameter-matched free-form FEN control (width ~139, ~5 GPU-h at 5 folds) has
  never been run; §4.4.4 and §4.4.6 state the 1.97x gap. Inline TODO in §4.4.4.
- [ ] TODO (code repo, not editable from here) -- three statements in
  `THESIS_FRAMEWORK.md` §4b found wrong or misleading while checking the papers:
  (1) the 3x3 FNO hybrid is called "the localized-kernel neural operator
  (Liu-Schiaffini et al.)"; it is a simplified relative -- no mean subtraction, no 1/h
  rescaling, no DISCO, one fixed resolution; (2) the FEN transport term is said to depart
  from Lienen & Günnemann by imposing "no divergence constraint", but the paper's velocity
  is also only per-cell constant (Appendix B assumes div v = 0 to reach the same advective
  form); both implementations are the same in this respect; (3) the "44x" U-Net ratio is
  against the k-NN arm (75,339); against the canonical 67,147 it is 50x.
- [x] (2026-09-27: done / moved, see the restructure section) TODO: 4.5 Moving-mesh extension as a tested hypothesis (DMM, dual branch, alpha gate).
- [x] (2026-09-27: done / moved, see the restructure section) TODO: 4.6 Conditioning (covariates, LayerEncoder).
- [x] (2026-09-27: done / moved, see the restructure section) TODO: 4.7 Training.
- [x] (2026-09-27: done / moved, see the restructure section) TODO: 4.8 Implementation details.

### Chapter 5 - Experiments (`05-experiments.tex`)

- [x] 2026-09-27: `05-experiments.tex` skeleton rebuilt to the THESIS_STRUCTURE.md outline:
  5.1 Evaluation Protocol, 5.2 The Arm Table (label `sec:experiments:main-results` kept),
  5.3 The Ingredient Study (`sec:experiments:ingredients`), 5.4 Negative Results (label
  `sec:experiments:ablations` kept), 5.5 Validity Diagnostics (`sec:experiments:validity`),
  5.6 Qualitative Analysis and Clinical Comparison, 5.7 Computational Cost. **"Baselines"
  removed** (author question): it was the pre-survey plan (persistence / single-branch /
  dual-branch / optional U-Net); in the survey every architecture is a peer arm of the one
  table, and only persistence and the per-pixel floor fix the scale. §4.2.1 now points to
  `sec:experiments:validity` (review #16 TODO closed).
- [x] 2026-09-27: §5.1-§5.3 to be drafted by an external LLM from a fact-sheet prompt (numbers
  from THESIS_FRAMEWORK.md §7.1-§7.5 and PROJECT_CONTEXT.md), then audited here. Known gaps the
  prompt leaves as TODOs: the one-hop floor's minimum epoch time; per-horizon growth-region Dice
  (FNO vs U-Net beyond one year; T-FEN / free-form / one-hop / stencil in the 0-1 y bin) --
  needed from SOLVER_FINAL_RUNS.md in the code repo.
- [x] 2026-09-27: §5.1-§5.3 drafted externally, audited against THESIS_FRAMEWORK.md §7.1-§7.5 and
  PROJECT_CONTEXT.md, spliced in (pages 46-54). Every number checked against the fact sheet; none
  was altered or invented. Corrections made:
  - **Wrong:** §5.3 intro said the leading classes "produce identical aggregate metrics" (they
    are indistinguishable, not identical); the floors were referenced to the operator contract
    (now `sec:method:family:floors`); the reach ladder said "the two extremes" exceed the floor
    (it is the ±12 and ±42 rows, one on each side); the mechanism for the null second ring was
    stated as fact (now "one possible reason"); `\citep[the square-root transform of][...]` was a
    malformed natbib call.
  - **Build-breaking:** `	exttt{% TODO}` in the figure placeholder (unescaped %), table row ends
    collapsed to `\`, "3x3" in text mode.
  - **Removed:** the repeat of the 68/75 and 7/75 anchor counts from §3.6; "not create one" (noise
    can mask an effect); "strictly", "entirely", "firmly", "purely", "exactly at".
  - **Added:** the neutral logging-limitation sentence the prompt left to the author; a sentence
    that the T-FEN velocity field is not interpreted (§5.5); the U-Net-vs-k-NN numbers moved
    before the conclusion they support; "per-pixel baseline" renamed to "floor"; `\S
ef` style.
- [x] (filled 2026-09-28: 59 s; 37 s since the mean one-hop floor of 2026-10-01) TODO (§5.2 inline): the one-hop floor's minimum epoch time and fold.
- [x] (filled 2026-10-01 from SOLVER_FINAL_RUNS §9.20) TODO (§5.3.3/§5.3.4 inline): per-horizon growth-region Dice -- FNO vs U-Net beyond one
  year; T-FEN / free-form FEN / one-hop floor / dilated stencil in the 0-1 y bin; horizon
  profiles of the T-FEN and the dilated stencil. From SOLVER_FINAL_RUNS.md (code repo). The
  transport-vs-capacity argument in §5.3.4 rests partly on these.
- [x] 2026-09-28 (author decisions on the §5.4-§5.7 plan):
  - **Capacity question dropped from the thesis as it stands.** A single 50x arm compared
    with parameter-matched models does not answer it. The width-32 U-Net is removed from
    Table 5.1, from §4.3.4, the parameter table and §4.3.8 (commented out); §5.2 no longer
    mentions it; §5.3.4 no longer argues "capacity is a null elsewhere" for the T-FEN (only
    the near-term-bin argument remains, plus "settling it needs the matched control"); the
    §5.3.2 sentence "capacity, normalisation and message function are ruled out in §5.4" is
    removed.
  - Table 5.1: new "Best fold" column (highest of the five late-epoch fold means, from
    solver_results.csv; fold 2 for every arm except FNO and FNO + RK4, fold 4); fold index
    removed from the cost column; one-hop floor cost filled in (59 s, min over folds).
    Author's belief that slow folds were GPU-occupied: the 2026-09-17 audit found 0 runs ever
    sharing a GPU; the spread is the 280-320 steps per fold plus an additive overhead. The
    minimum remains the reported value.
  - §5.2 now flags the T-FEN in the table (dagger) and in the text as not a valid free-running
    integrator, before §5.5 (author: otherwise readers take it for the best model).
  - §5.4: time handling (explain why the Delta t scaling could be dropped) and the objective
    are kept; covariates + layer encoder and GNN-internal settings are drafted and then
    commented out; the encoder result must be scoped to one backbone and one design (only the
    width was varied; 20 runs). No moving-mesh sentence in §5.4 (Appendix G only).
  - §5.7: training cost only; inference time and memory were never measured and are dropped.
- [x] TODO (author, 2026-09-28): design separate **capacity experiments** (the question is open
  again). Include the parameter-matched free-form FEN control (width ~139) for the transport
  term. Discuss right after the §5.4-§5.5 prompt. -> pre-registered below.

### Capacity experiment -- PRE-REGISTRATION (fixed 2026-09-28, Monday evening; deadline Thursday 2026-10-01 evening)

**Question.** With the architecture and the shared training recipe fixed, does adding capacity
move change-region Dice@360d by more than the floor -- and do the three architecture classes
stay indistinguishable when all are scaled to the same parameter count? Plus: is the transport
term still established against a parameter-matched free-form control?

**Rules fixed now.** Training recipe unchanged (author: no learning-rate study; the one
curriculum stays). 5 folds, seed 42, final pipeline, late-epoch mean, both instruments
(fold-paired vs 1x, floor 0.016 / 0.020 with a U-Net; per-eye, LOFO). Width is the *comparable*
capacity axis (it adds parameters without changing reach, receptive field or bandwidth); depth
is *arm-specific* and is never compared across arms (GNN depth = more message-passing hops =
more reach; FEN depth = MLP depth; U-Net and FNO have no depth knob without a code change). For
the T-FEN, the stability criterion of §5.5.2 is read on every new run as well.

**Parameter counts** (computed 2026-09-28 by building each model in the MPPDE env from the
code repo, read-only; they reproduce 67,147 / 83,081 / 79,960 / 68,503 / 34,785 exactly):

| arm | 1/4x | 1x (exists) | ~2x depth | ~4x width | ~16x width |
|---|---|---|---|---|---|
| stencil GNN (L = layers) | h32 L2 18,219 (0.27x) | h64 L2 67,147 | h64 **L4** 119,499 (1.78x) | **h128** L2 257,163 (3.83x) | h256 L2 1,005,835 (14.98x) |
| U-Net | w2 13,637 (0.20x) | w5 83,081 | -- | **w9** 267,149 (3.98x) | w18 1,063,541 (15.84x) |
| FNO + 3x3 | w2 13,189 (0.20x) | w5 79,960 | -- | **w9** 257,804 (3.84x) | w18 1,029,077 (15.33x) |
| T-FEN (d = MLP depth) | w48 20,455 (0.30x) | w96 d4 68,503 | w96 **d8** 142,999 (2.13x) | **w192** d4 247,543 (3.69x) | w400 d4 1,014,855 (15.11x) |
| free-form FEN | -- | w96 34,785 (0.52x) | -- | w266 231,985 (3.45x) | -- |
| **matched transport control** | | **w139 68,282 (1.02x vs T-FEN 68,503)** | | | |

**Stage 1 -- submit Monday night (7 arrays, 35 runs), in this priority order:**
1. free-form FEN w139 (matched transport control) -- closes the 1.97x caveat of §5.3.4.
2. stencil GNN h128 L2 (4x width).
3. U-Net w9 (4x width).
4. FNO + 3x3 w9 (4x width).
5. stencil GNN h64 L4 (depth; note: 4 hops of +/-21 columns = more reach, so this is also a
   reach test).
6. T-FEN w96 d8 (depth).
7. T-FEN w192 d4 (4x width) -- by far the most expensive (see cost).

**Decision rule for Stage 2 (Tuesday evening), fixed now:**
- An arm whose 4x-width run is higher than its 1x twin by more than the floor on *both*
  instruments -> run its 16x width point.
- An arm with no such gain -> no 16x; instead run its 1/4x point, so every arm gets a
  three-point curve (1/4x, 1x, 4x). The 1/4x points are cheap.
- Depth: only if a depth run is higher than its 1x twin on both instruments, try one step
  further (stencil L3 or L6, T-FEN d6); otherwise depth stops at one point.
- If the matched transport control leaves T-FEN minus free-form above the floor on both
  instruments, §5.3.4 drops the 1.97x caveat; if not, the transport result is re-read as
  (partly) capacity. Optional at 4x: free-form FEN w266 vs T-FEN w192.

**Cost (rough, GPU-h per 5-fold array; min-epoch x 30 epochs x ~1.3 for the median epoch;
GNN width scaling from the k-NN runs: per layer ~23 s at width 64, ~42 s at 128):**
U-Net w9 ~3; FNO w9 ~3; stencil h128 ~8; stencil L4 ~8; free-form FEN w139 ~15-20 (MLP time
~ width^2); T-FEN d8 ~35-40; **T-FEN w192 ~60-80 (about 12-16 h per run)**. Stage 1 total
~130-160 GPU-h, i.e. one night only if ~35 GPUs are free at once; with fewer GPUs the T-FEN
arrays are the ones that spill into Tuesday. If the queue is full on Tuesday morning, drop
T-FEN w192 first (keep T-FEN d8 as the T-FEN capacity point) and say so in the write-up.

**Schedule.**
- Mon night: submit Stage 1 in the order above.
- Tue morning: check the queue; harvest the finished cheap arrays (U-Net, FNO, stencil).
- Tue afternoon: harvest the rest, pull the per-eye records, apply the decision rule.
- Tue night: submit Stage 2 (16x or 1/4x points, depth follow-up if earned).
- Wed: harvest Stage 2; figure (Dice vs log parameters, one line per arm, 1x points from
  the existing runs) and the paired table; rerun failures on Wednesday night if needed.
- Thu: write the subsection (prompt -> external draft -> audit), update Table 4.3 / §4.3.8
  and §5.3.4, compile, commit.

**Launch lines** (to be checked against the canonical arms' `args.json` before submitting --
the diff of each new run against its 1x twin must contain only the size knob and the
experiment name):
```
BACKBONE=fen HIDDEN_DIM=139 FEN_TRANSPORT=False INTEGRATOR=rk4 ODE_STEP_DAYS=45 EXP_TAG=w139Frk4d45 ARM=sb sbatch --array=0-4 --gres=gpu:nva6000:1 ~/jobs/train_solver.slurm
HIDDEN_DIM=128 EXP_TAG=dilmean_h128 ARM=sb sbatch --array=0-4 --gres=gpu:nva6000:1 ~/jobs/train_solver.slurm
BACKBONE=unet HIDDEN_DIM=9 EXP_TAG=w9 ARM=sb sbatch --array=0-4 --gres=gpu:nva6000:1 ~/jobs/train_solver.slurm
BACKBONE=fno HIDDEN_DIM=9 FNO_LOCAL_KERNEL=3 EXP_TAG=w9k3 ARM=sb sbatch --array=0-4 --gres=gpu:nva6000:1 ~/jobs/train_solver.slurm
HIDDEN_LAYERS=4 EXP_TAG=dilmean_l4 ARM=sb sbatch --array=0-4 --gres=gpu:nva6000:1 ~/jobs/train_solver.slurm
BACKBONE=fen HIDDEN_DIM=96 FEN_DEPTH=8 FEN_TRANSPORT_PITCH=7 INTEGRATOR=rk4 ODE_STEP_DAYS=45 EXP_TAG=w96d8ftp7rk4d45 ARM=sb sbatch --array=0-4 --gres=gpu:nva6000:1 ~/jobs/train_solver.slurm
BACKBONE=fen HIDDEN_DIM=192 FEN_TRANSPORT_PITCH=7 INTEGRATOR=rk4 ODE_STEP_DAYS=45 EXP_TAG=w192ftp7rk4d45 ARM=sb sbatch --array=0-4 --gres=gpu:nva6000:1 ~/jobs/train_solver.slurm
```
Memory to watch: stencil h128 (the k-NN 6x128 ran at batch 4, so it should fit) and T-FEN w192.

**Existing capacity evidence, for the record (none of it usable as the answer):** the k-NN
depth x width grid (depth 1-12, width 32-256) is fold 3 of an older pipeline version, flat;
6x128 on fold 2 at the old loss setting, under the floor; the 50x U-Net (removed). The stencil
GNN, FNO and FEN have never been run at another size.
- [x] TODO: after §5.4.3 is commented out, §4.4 still says the covariates and the layer encoder
  are "tested in Chapter 5" (two sentences) -- adjust them. Done 2026-09-28: covariates "not
  settled by the experiments of this thesis"; encoder "not examined further". Also removed
  §4.3.2 "this capacity is a configuration choice based on experiments reported in Chapter 5"
  (inline TODO: point to the capacity subsection once it exists).
- [x] 2026-09-28: §5.4-§5.5 drafted externally, audited against the fact sheet (prompt of
  2026-09-28, numbers from THESIS_FRAMEWORK.md §7.5/§9.3 and SOLVER_FINAL_RUNS.md §9.15-§9.17),
  spliced in (pages 54-58). §5.4.3 (covariates + layer encoder) and §5.4.4 (GNN-internal
  settings) are written but wrapped in `\iffalse ... \fi` (author). Corrections made:
  - **Wrong:** "at a 30-day step every channel falls back within the 2.4 bound, peaking at
    2.42" (2.42 > 2.4; it is within the 2.8 bound used during the runs); "a Courant read-back
    identifies the cause" (it is a correlation: "points to"); §5.4 opening called the ablations
    "choices that did not graduate to the final pipeline" (the Delta t scaling *is* in the
    pipeline); the k-NN network referenced as `ch:method` (now `sec:method:graph`); the RK4
    limit 2*sqrt(2) cited to Courant et al. (now "in the sense of the stability condition of");
    "the dilated-stencil network logs zero epochs ... for both models" (garbled); the Courant
    table's columns were labelled as if they were RMSE maxima and the caption did not say they
    are Courant numbers; the swap-table caption "confirming it is a conditioned map" overclaimed.
  - **Added:** the era statement for the intermediate-time-point regulariser ("no number is
    quoted"); "raw values quoted only to show the stretch" for the sharpness RMSE; the ± on the
    reparameterisation target; `\times` for "4.8x", "2x", "14x".
  - The §4.3.6 TODO on the Courant bound (2.8 vs ~2.4) is answered in §5.5.2 ("settles the open
    value"); §4.3.6 itself still carries the TODO -- fix in the Chapter 4 review.
- [x] (superseded 2026-10-01: the k-NN ablation is no longer reported; the stencil run `ANISOGNN_final_dilmean_nodts` is queued) TODO (§5.4.1 inline): per-eye instrument for the Delta t-scaling ablation, if computed
  (SOLVER_FINAL_RUNS.md, the `nodts` / `euler_dt_scale False` arm).
- [ ] ⚠️ Mirror is stale (code repo wins): the T-FEN's free-running rollout is unstable on
  **7 of 10** runs (corrected in SOLVER_FINAL_RUNS.md §9.15 on 2026-09-16), not "5 of 10" as
  PROJECT_CONTEXT.md, THESIS_FRAMEWORK.md and the 2026-09-17 entry above say. The Courant bound
  the runs were judged against is 2.8; the correct bound for the assembled stencil is ~2.4
  (spectral radius ~1.17 |v|) -- this resolves the §4.3.6 TODO; fix §4.3.6 in the Chapter 4
  review. Re-mirror when convenient.
- [ ] 2026-10-01: open items of the 2026-09-27/28 session merged into `prompts/open.txt` (marked [s27], overview in its section 8).
- [ ] TODO: produce Figure `fig:experiments:rollout` (§5.2) -- rollout strip for one eye, from
  masterthesis-docker/practical/scripts/fig_rollout.py and the final-epoch rollout exports.

- [x] (drafted 2026-09-27) TODO: 5.1 Evaluation protocol (MSE caveat first, then Dice/IoU@360d, persistence floor).
- [x] (obsolete 2026-09-27: section removed, see above) TODO: 5.2 Baselines.
- [x] (table drafted 2026-09-27; rollout figure tracked separately) TODO: 5.3 Main results table + rollout figure.
- [x] (drafted 2026-09-28, rewritten 2026-10-01) TODO: 5.4 Ablations sweep.
- [x] (moved to Appendix G.3 2026-09-27) TODO: 5.5 Moving mesh quality.
- [x] (2026-10-19, author: section dropped; §5.7 is now "Comparison with Prior Work"; see the 2026-10-19 entry) TODO: 5.6 Qualitative analysis (success + failure modes).
- [x] (written as §5.6 in ce6bf3e) TODO: 5.7 Computational cost.

### Chapter 6 - Discussion (`06-discussion.tex`)

- [ ] TODO: 6.1 Interpretation of results.
- [ ] TODO: 6.2 Clinical implications (reliable horizon, useful RMSE/Dice levels).
- [ ] TODO: 6.3 Limitations.
- [ ] TODO: 6.4 Future work.

### Chapter 7 - Conclusion (`07-conclusion.tex`)

- [ ] TODO: restate contributions, summarize findings, close on the take-away.

### Appendices (`91-appendix.tex`)

- [ ] TODO: A. Dataset details (demographic tables, visit-interval histograms, per-channel stats).
- [ ] TODO: B. Extended derivations (Monge-Ampère, multi-channel monitor function, pushforward stability).
- [ ] TODO: C. Full hyperparameters.
- [ ] TODO: D. Additional rollout figures (including failure cases).
- [ ] TODO: E. Full ablation tables.
- [ ] TODO: F. Code structure + GitHub pointer + reproducibility.

### Pending external citations

Introduced by the 2026-09-17 Chapter 2 draft (`02-background.tex` §2.3--§2.6). Each has a
matching `% TODO: cite ...` marker in the .tex, with the full bibliographic detail in the
marker itself; `THESIS_FRAMEWORK.md` §10.1 carries verified entries for all of them.

- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Gupta2023** -- Gupta & Brandstetter, *TMLR* 2023, "Towards
  Multi-spatiotemporal-scale Generalized PDE Modeling" (PDEArena). Used in §2.3 as the
  evidence that a U-Net is a standard strong surrogate baseline in the neural-PDE
  literature.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **LiuSchiaffini2024** -- Liu-Schiaffini, Berner, Bonev, Kurth,
  Azizzadenesheli & Anandkumar, *ICML* 2024, "Neural Operators with Localized Integral and
  Differential Kernels". Used in §2.3 for the local-kernel bypass over a global operator.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Gao2019** -- Gao & Ji, *ICML* 2019, "Graph U-Nets". Used in §2.3 as the
  multi-scale counterpart on graphs. Note for §4.4: the repository's own `GAGraphUNet` is
  an image pyramid with a graph operator per block, **not** this work's learned node-score
  pooling — cite it as a disambiguation there, not as the method used.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Lienen2022** -- Lienen & Günnemann, *ICLR* 2022, "Learning the Dynamics
  of Physical Systems from Sparse Observations with Finite Element Networks". Used in §2.3
  and needed again in §4.4 for the FEN / T-FEN arm.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Chen2018** -- Chen, Rubanova, Bettencourt & Duvenaud, *NeurIPS* 2018,
  "Neural Ordinary Differential Equations". Used in §2.3 for the Neural-ODE reading of a
  residual update, and in §4.2.1 for the caution that the Euler form does not make
  f_theta a rate; needed again in §4.4 for the Runge--Kutta wrapper.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Ott2021** -- Ott, Katiyar, Hennig & Tiemann, *ICLR* 2021, "ResNet After
  All: Neural ODEs and Their Numerical Solution". Used in §2.3 for the solver-invariance
  requirement; needed again in §5.6 for the solver-swap diagnostic.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Krishnapriyan2023** -- Krishnapriyan, Queiruga, Erichson & Mahoney,
  *Communications Physics* 6:319, 2023, "Learning continuous models for continuous
  physics". Used with Ott2021 in §2.3 and §5.6. Cite the 2023 journal year, not the 2022
  preprint.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **HuangRussell2011** -- Huang & Russell, *Adaptive Moving Mesh Methods*,
  Springer, Applied Mathematical Sciences vol. 174, 2011. Used in §2.5 as the classical
  background for moving meshes; also the source of the equidistribution-CoV mesh-quality
  measure needed in §5.5.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Liu2018** -- Liu, Lehman, Molino, Petroski Such, Frank, Sergeev & Yosinski,
  *NeurIPS* 2018, "An Intriguing Failing of Convolutional Neural Networks and the CoordConv
  Solution", arXiv:1807.03247. Used in §4.4.1 for the coordinate input channels.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Wu2018** -- Wu & He, *ECCV* 2018, "Group Normalization", arXiv:1803.08494.
  Used in §4.4.2 for the U-Net / graph U-Net normalisation.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Gilmer2017** -- Gilmer, Schoenholz, Riley, Vinyals & Dahl, *ICML* 2017,
  "Neural Message Passing for Quantum Chemistry", arXiv:1704.01212. Used in §4.4.3.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Courant1928** -- Courant, Friedrichs & Lewy, "Über die partiellen
  Differenzengleichungen der mathematischen Physik", *Mathematische Annalen* 100(1):32-74,
  1928, doi:10.1007/BF01448839. Used in §4.4.4 for the stability condition.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Butcher1987** -- Butcher, *The Numerical Analysis of Ordinary Differential
  Equations: Runge-Kutta and General Linear Methods*, Wiley 1987. Used in §4.4.5.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Hairer1993** -- Hairer, Nørsett & Wanner, *Solving Ordinary Differential
  Equations I: Nonstiff Problems*, Springer, 2nd rev. ed. 1993,
  doi:10.1007/978-3-540-78862-1. Used in §4.4.5.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Ba2016** -- Ba, Kiros & Hinton, "Layer Normalization", arXiv:1607.06450,
  2016 (preprint, no peer-reviewed venue). Used in §4.3.1 for the per-node normalisation.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Ioffe2015** -- Ioffe & Szegedy, *ICML* 2015, "Batch Normalization:
  Accelerating Deep Network Training by Reducing Internal Covariate Shift",
  arXiv:1502.03167. Used in §4.3.1 for the normalisation that is avoided. (Also cited by
  the MP-PDE paper itself for its 2-D experiments.)
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Feuer2013** -- Feuer, Yehoshua, Gregori, Penha, Chew, Ferris, Clemons,
  Lindblad & Rosenfeld, *JAMA Ophthalmology* 131(1):110-111, 2013, "Square Root
  Transformation of Geographic Atrophy Area Measurements to Eliminate Dependence of Growth
  Rates on Baseline Lesion Measurements". Used in §3.1 for the square-root area scale of
  the cohort growth statistics; needed again in §5.1 for √area MAE and growth rates.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Mai2024** -- Mai, Lachinov, Reiter, Riedl, Grechenig, Bogunović &
  Schmidt-Erfurth, *Ophthalmology Science* 4(4):100466, 2024, "Deep Learning-Based
  Prediction of Individual Geographic Atrophy Progression from a Single Baseline OCT".
  Used in §2.6 as the closest prior work (same MUW cohort, same task), in §2.1.6 and §3.1 as the
  source of the device model, and in §3.6 for the one-year-anchor
  comparability choice; needed again in §5.7. **The pre-segmented-masks vs raw-OCT caveat must travel with every comparison.**
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Salvi2025** -- Salvi et al., *Ophthalmology Science* 5(2):100635, 2025,
  "Deep Learning to Predict the Future Growth of Geographic Atrophy from Fundus
  Autofluorescence". Used in §2.6 as the dense-CNN precedent on this task (different
  modality, so not a comparable number); also the GA-domain motivation for the U-Net arm
  in §4.4.
- [x] (obsolete 2026-09-25, method-of-lines sentence removed) cite **Schiesser2012** -- Schiesser, *The Numerical Method of Lines:
  Integration of Partial Differential Equations*, Academic Press / Elsevier (cited as
  Schiesser 2012 by Brandstetter2022; check the edition year). Used in §2.2.2.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **BarSinai2019** -- Bar-Sinai, Hoyer, Hickey & Brenner, "Learning
  data-driven discretizations for partial differential equations", *PNAS*
  116(31):15344-15349, 2019. Used in §2.2.6 as the hybrid (learned-stencil) example.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Kochkov2021** -- Kochkov, Smith, Alieva, Wang, Brenner & Hoyer,
  "Machine learning-accelerated computational fluid dynamics", *PNAS* 118(21):e2101784118,
  2021. Used in §2.2.6.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Pfaff2021** -- Pfaff, Fortunato, Sanchez-Gonzalez & Battaglia,
  "Learning Mesh-Based Simulation with Graph Networks", *ICLR* 2021. Used in §2.2.6.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Lam2023** -- Lam et al., "Learning skillful medium-range global weather
  forecasting", *Science* 382(6677):1416-1421, 2023 (GraphCast). Used in §2.2.6 as the
  weather-forecasting example.
- [x] (added to references.bib 2026-09-26) TODO: cite **LeVeque2007** -- LeVeque, *Finite Difference Methods for Ordinary and
  Partial Differential Equations: Steady-State and Time-Dependent Problems*, SIAM 2007,
  doi:10.1137/1.9780898717839. Used in §2.2.1 for the finite difference method (replaces a
  Brandstetter2022 citation, author review #8, 2026-09-26).
- [x] (added to references.bib 2026-09-26) TODO: cite **Courant1943** -- Courant, "Variational methods for the solution of problems
  of equilibrium and vibrations", *Bulletin of the AMS* 49(1):1-23, 1943,
  doi:10.1090/S0002-9904-1943-07818-4. Used in §2.2.1 as the original FEM reference.
- [x] (added to references.bib 2026-09-26) TODO: cite **LangtangenMardal2019** -- Langtangen & Mardal, *Introduction to Numerical
  Methods for Variational Problems*, Springer, Texts in Computational Science and Engineering
  vol. 21, 2019, doi:10.1007/978-3-030-23788-2 (author-supplied; the author's copy is the
  2016 draft of the same book). Used in §2.2.1 as the FEM textbook.
- [x] (added to references.bib 2026-09-26) TODO: cite **Liu1994** -- Liu, Osher & Chan, "Weighted essentially non-oscillatory
  schemes", *J. Comput. Phys.* 115(1):200-212, 1994, doi:10.1006/jcph.1994.1187. §2.2.1 WENO.
- [x] (added to references.bib 2026-09-26) TODO: cite **JiangShu1996** -- Jiang & Shu, "Efficient implementation of weighted ENO
  schemes", *J. Comput. Phys.* 126(1):202-228, 1996, doi:10.1006/jcph.1996.0130. §2.2.1 WENO;
  also a candidate for the WENO5 mention in §2.4 (review #18).
- [x] (added to references.bib 2026-09-26) TODO: cite **GottliebOrszag1977** -- Gottlieb & Orszag, *Numerical Analysis of Spectral
  Methods: Theory and Applications*, SIAM (CBMS-NSF vol. 26), 1977,
  doi:10.1137/1.9781611970425. §2.2.1 pseudospectral methods.
- [x] (added to references.bib 2026-09-26) TODO: cite **Trefethen2000** -- Trefethen, *Spectral Methods in MATLAB*, SIAM 2000,
  doi:10.1137/1.9780898719598. §2.2.1 pseudospectral methods (textbook).
- [x] (added to references.bib 2026-09-26) TODO: cite **Bartels2016** -- Bartels, *Numerical Approximation of Partial Differential
  Equations*, Springer, Texts in Applied Mathematics vol. 64, 2016,
  doi:10.1007/978-3-319-32354-1. §2.2.3, origin of the "splitter field" remark quoted via
  MP-PDE.
- [x] (added to references.bib 2026-09-26) TODO: cite **Scarselli2009** -- Scarselli, Gori, Tsoi, Hagenbuchner & Monfardini, "The
  Graph Neural Network Model", *IEEE Trans. Neural Networks* 20(1):61-80, 2009,
  doi:10.1109/TNN.2008.2005605. §2.5 related work (origin of GNNs).
- [x] (added to references.bib 2026-09-26) TODO: cite **Runge1895** -- Runge, "Ueber die numerische Auflösung von
  Differentialgleichungen", *Mathematische Annalen* 46:167-178, 1895, doi:10.1007/BF01446807.
  §2.5 related work (origin of Runge-Kutta).
- [x] (added to references.bib 2026-09-26) TODO: cite **Kutta1901** -- Kutta, "Beitrag zur näherungsweisen Integration totaler
  Differentialgleichungen", *Zeitschrift für Mathematik und Physik* 46:435-453, 1901 (no DOI).
  §2.5 related work (origin of Runge-Kutta).
- [x] (all six added 2026-09-26) Note (2026-09-26): the §2.5 related-work paragraph also uses the already-pending
  **Gilmer2017, Ronneberger2015, Li2021, LiuSchiaffini2024, Lienen2022, Chen2018**.
- [x] (LeVeque2002 added to references.bib 2026-09-26) Note (2026-09-26): **LeVeque2002** now also backs the FVM sentence in §2.2.1 (replacing
  Brandstetter2022); add doi:10.1017/CBO9780511791253 when the entry is created.
- [x] (all added 2026-09-26) Note (2026-09-25): the §2.2 rework also uses the already-listed markers
  **LeVeque2002** (now for conservation laws / FVM / convergence, no longer as the SWE
  textbook), **SanchezGonzalez2020** (§2.2.6), **Butcher1987** and **Hairer1993**
  (§2.2.4), and **Courant1928** (§2.2.4, CFL).
- [ ] TODO: literature check -- is there any prior application of neural PDE solvers to
  biomedical disease progression or organ modelling? §2.6 currently states only that the
  application "remains sparse", with an inline `% TODO`. Either find and cite one or two
  examples, or make the absence an explicit, defensible claim.


External references introduced inline in the LaTeX drafts that still need to be added to `references.bib` (one entry per reference; each has a corresponding `% TODO: cite ...` marker in the .tex file). Once an entry is added to the bibliography, replace the placeholder author-year mention with the proper `\citet{}` / `\citep{}` and remove the matching `% TODO:` line.

- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Wong2014** -- Wong et al., *Lancet Glob Health* 2014, "Global prevalence of age-related macular degeneration and disease burden projection for 2020 and 2040." Used in `01-introduction.tex` §1.1 opening to support "leading cause of irreversible central vision loss in industrialised countries."
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **SchmidtErfurth2018** -- Schmidt-Erfurth et al., *IOVS* 2018, "Prediction of individual disease conversion in early AMD using artificial intelligence." Used in `01-introduction.tex` §1.2 as an AI-on-OCT precedent for cohort-level conversion prediction.
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Bogunovic2017** -- Bogunović et al., *IOVS* 2017, "Machine learning of the progression of intermediate AMD based on OCT imaging." Used in `01-introduction.tex` §1.2 alongside SchmidtErfurth2018 as the supervisor's institutional AI-on-OCT precedent. (Earlier draft of `02-background.tex` §2.1.4 also cited it for the MUW segmentation pipeline; that usage was removed on 2026-05-02 because the MUW pipeline provenance is not actually established by this reference --- if confirmed, restore that usage in `03-data.tex` §3.1 instead.)
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Ronneberger2015** -- Ronneberger et al., *MICCAI* 2015, "U-Net: Convolutional Networks for Biomedical Image Segmentation." Used in `01-introduction.tex` §1.2 to anchor the "standard U-Net" baseline mention. (2026-09-25: that §1.2 sentence was removed; still needed for §2.3 and §4.4.)
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Battaglia2018** -- Battaglia et al., 2018, "Relational inductive biases, deep learning, and graph networks." Used in `01-introduction.tex` §1.3 to attribute the encode--process--decode GNN pattern. (2026-09-25: that §1.3 sentence was removed; the marker went with it. Still relevant for §2.4.)
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **SanchezGonzalez2020** -- Sanchez-Gonzalez et al., *ICML* 2020, "Learning to simulate complex physics with graph networks." Used in `01-introduction.tex` §1.3 alongside Battaglia2018 for the encode--process--decode pattern. (2026-09-25: that §1.3 sentence was removed; still relevant for §2.4.)
- [x] (Li2021 and Lu2021 added to references.bib 2026-09-26) TODO: cite **Li2021** (FNO) and **Lu2021** (DeepONet) -- needed for `02-background.tex` §2.3 (autoregressive vs operator-style neural solvers). (2026-09-25: the conditional §1.3 acknowledgement is moot; §1.3 names no architecture.)
- [x] (added to references.bib 2026-09-26, details checked) TODO: cite **Sadda2018** -- Sadda et al., *Ophthalmology* 2018, "Consensus Definition for Atrophy Associated with Age-Related Macular Degeneration on OCT: Classification of Atrophy Report 3." Used in `02-background.tex` §2.1.1 as the primary source for the cRORA criteria currently attributed only to Vallino2024.
- [x] (2026-10-01: cited in §2.1.3, bib entry added) (2026-09-26: not cited anywhere in the text; the marker in §2.1.3 stays until the author decides whether the OCT section should cite the origin of the modality) TODO: cite **Huang1991** -- Huang et al., *Science* 254:1178-1181, "Optical Coherence Tomography." Used in `02-background.tex` §2.1.2 to anchor the introduction of OCT as the canonical methodological-origin reference for the modality.
- [x] (obsolete 2026-09-26: the SD-OCT description it supported was cut on 2026-09-25; marker removed) TODO: cite an SD-OCT principle reference (e.g. **Wojtkowski2002** or **Drexler2008**) once added to `references.bib`. Used in `02-background.tex` §2.1.2 to support the spectral-domain OCT principle behind the SD-OCT acquisition platform.
- [x] (LeVeque2002 added to references.bib 2026-09-26; now used for FVM and convergence, not the SWE) TODO: cite a canonical SWE textbook (e.g. **LeVeque2002**, "Finite Volume Methods for Hyperbolic Problems", Cambridge University Press, Chapter 13; or **Vreugdenhil1994**, "Numerical Methods for Shallow-Water Flow", Springer) once added to `references.bib`. Used in `02-background.tex` §2.2.1 where the shallow-water equations are introduced as the running example for the section.

### Bibliography

- [ ] TODO: replace placeholder entries in `references.bib` with actual thesis references (MP-PDE, MM-PDE, FNO, DeepONet, GA/OCT clinical literature, GNN foundations, etc.).
- [x] 2026-04-27: ingested 13 GA/OCT/clinical references (Boopathiraj2024, Boyer2017, Chu2022, Ebneter2016, Flaxman2020, Lad2023, Pilotto2015, Singh2025, Song2025, Trincao2024, Vallino2024, Vogl2021, Yehoshua2011) into `references.bib`; added 13 hub notes + 25 atomic concept spokes to `literature/`. Still pending: FNO, DeepONet, GNN foundations, AMD/OCT references beyond this batch.
- [ ] TODO: confirm citation key choice for Trincão-Marques 2024 — currently `Trincao2024` (ASCII for BibTeX safety); raw note in `pdfs/GA/Trincão2024.md` retains the diacritic.
- [x] (fixed 2026-10-01: @inproceedings ICLR 2024; Brandstetter2022 likewise ICLR 2022) TODO: pre-existing inconsistency — `Hu2024` BibTeX entry has `year = {2023}` while the citation key is `Hu2024`. Untouched in this session; flag for cleanup if biblatex sorting becomes year-sensitive.

### Template / build system

- [ ] TODO (build environment, 2026-09-18): VS Code's LaTeX Workshop auto-builds
  `main-thesis.tex` on every save, and it races any `latexmk` run in the same directory --
  both write `main-thesis.aux`, which twice ended up truncated mid-line ("File ended while
  scanning use of \@writefile", "Undefined control sequence \abx@aux@defaglobal"). Such
  errors are .aux corruption, not source errors. Verification builds therefore use an
  isolated output directory: `latexmk -xelatex -interaction=nonstopmode -outdir=<tmp>
  main-thesis.tex`. Consider disabling `latex-workshop.latex.autoBuild.run` while an agent
  is editing, or pointing LaTeX Workshop at its own `outDir`.
- [x] 2026-05-02: switched the biblatex configuration in `main-thesis.tex` from `style=ACM-Reference-Format,citestyle=numeric` to `style=authoryear,natbib=true` so that the natbib-style commands `\citet` / `\citep` mandated by `CLAUDE.md` produce author-year output. Other biblatex options (`backend=biber`, `sortcites=true`, `maxcitenames=2`) preserved.
- [ ] TODO: confirm with supervisor that the JKU technical-report template tolerates the author-year deviation from the bundled ACM numeric default; if not, a one-line revert restores the original style.
