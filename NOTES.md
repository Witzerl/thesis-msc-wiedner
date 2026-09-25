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
  moving the drafted `02-background.tex` §2.5 text into `91-appendix.tex`.
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
- [ ] §1.2 "three properties" paragraph (not marked by the author): the covariate
  requirement ("should enter the dynamics on equal footing") contradicts the measured
  covariate null, and the claim that both mask and layers are *required* is not shown
  by the results. Revisit.
- [x] §1.3: "Two recent neural PDE solver families…" — too much focus on MP-PDE/MM-PDE.
  Rewritten 2026-09-25.
- [ ] §1.4 Contributions — "might remove"; decide between rewriting and removing.
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
- [ ] ⚠️ FACT CHECK (2026-09-25, Mai et al. 2024, PMC11000109): in the Mai study of the MUW
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
- [ ] The **T-FEN transport term has no matched-capacity control** (a width-≈139 control
  has never been run); the 45-day T-FEN is **not a valid long-horizon integrator** as
  trained (5/10 runs diverge free-running, 9/10 final checkpoints exceed the Courant
  bound) — the learned velocity map is **not quotable**, though the Dice contribution
  stands.
- [ ] **Mai et al. 2024** (Ophthalmology Science) remains the direct comparison paper —
  same MUW cohort, same task. Our growth-region Dice is higher, **with the mandatory
  caveat that this model takes pre-segmented masks as input whereas Mai works from raw
  OCT**. Needs a `references.bib` entry.
- [ ] Ground-truth GA **retraction/shrinkage** between visits should be quantified before
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
- [ ] TODO: §2.3--§2.6 came in shorter than planned (§2.3 ~1.5 pages against a ~2.5-page
  target, §2.4 ~1.5 against ~2). The prose is correct but terse in places; consider a
  depth pass on §2.3 (operator-vs-autoregressive contrast) and §2.4 (message passing as a
  learned stencil) once Chapters 4--5 are drafted and it is clear how much background
  they actually lean on.
- [ ] TODO: produce Figure `fig:bg:eye-anatomy` placed in `02-background.tex` §2.1.1 -- two-panel anatomy reference for ML readers without clinical background: (left) sagittal cross-section of the human eye labelling cornea, lens, vitreous body, retina, fovea, optic-nerve head (ONH) / optic disc, optic nerve, choroid, sclera, with the macular region highlighted on the retina near the posterior pole; (right) en-face fundus view of the posterior pole labelling macula (~6 mm-wide central region), fovea (central pit), foveola (innermost ~0.35 mm of the fovea), parafovea (~0.5--1.5 mm eccentric ring), perifovea (~1.5--3 mm eccentric ring), and ONH / optic disc (~4 mm nasal to the fovea). Overlay the 6 x 6 mm OCT scanning window used by the thesis cohort as a dashed square centred on the fovea. Currently rendered as an `\fbox` placeholder pending a real graphic.
- [ ] TODO: produce Figure `fig:bg:retinal-anatomy` placed in `02-background.tex` §2.1.2 (formerly §2.1.1) -- two-panel schematic for readers without a clinical background: (left) labelled cross-section through a healthy macula showing the principal retinal layers from ILM through RNFL, GCL+IPL, INL+OPL, ONL, photoreceptor IS/OS bands (including the ellipsoid zone), RPE, and Bruch's membrane, with the choriocapillaris immediately beneath; (right) a representative OCT B-scan through a GA-affected macula highlighting the dropout of the outer-retinal layers within the lesion and the corresponding choroidal hypertransmission signature beneath. Mirror the channel ordering of the eleven-channel state tensor used in the thesis. Currently rendered as an `\fbox` placeholder pending a real graphic.
- [ ] TODO: produce Figure `fig:bg:oct-acquisition` placed in `02-background.tex` §2.1.3 -- four-panel schematic of OCT acquisition geometry intended to anchor the geometric vocabulary (A-scan, B-scan, volume, en-face) for ML readers without imaging background: (a) eye + single probe beam + inset depth-vs-reflectivity profile of one A-scan; (b) the same with the beam scanned laterally along one axis to form a B-scan; (c) the beam scanned in both lateral directions to form a 3D volume with the 6 x 6 mm physical footprint annotated (do NOT annotate a fixed voxel count -- native shapes vary per eye: 38-66 B-scans x 961-1719 A-scans, 67 distinct shapes); (d) the volume projected axially onto the fundus plane to yield the 49 x 1024 en-face image used by the model, with a representative GA lesion visible as a region of altered signal. Currently rendered as an `\fbox` placeholder pending a real graphic.
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
- [ ] TODO: produce Figure `fig:data:example-state` in §3.1 -- (a) SLO fundus image with
  the OCT field of view as a rectangle and the SLO-frame GA mask overlaid; (b) channel 0 on
  the 49 x 1024 grid at the physical aspect ratio (~5.94 x 5.82 mm), so the ~21:1 pixel
  anisotropy is visible; (c) one or two layer depth maps as heatmaps with the mask outline
  overlaid. Mark padded regions. A B-scan panel would need raw data from MUW.
- [ ] TODO: fill Table `tab:data:norm-stats` (§3.4) -- per-channel mean/std of the ten layer
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
- [ ] TODO: confirm which persistence-baseline quantities are bit-identical across arms,
  and cite the runs (§4.1 inline TODO). `THESIS_FRAMEWORK.md` §0.2 asserts the
  "bit-identical persistence fingerprints across arms" without defining them.
- [ ] TODO: verify the temporal-bundle sizes of the original MP-PDE. The set {20, 25, 50}
  (from code-side notes) could not be found in the paper text; §2.4 carries an inline
  TODO, and the §4.3.3 table states only "K steps".
- [ ] TODO: produce Figure `fig:method:pipeline` (§4.1) -- the shared pipeline with the
  operator slot as the one varying box and the moving-mesh branch dashed.
- [ ] TODO: produce Figure `fig:method:stencils` (§4.3.2) -- index-space diamond vs dilated
  stencil at physical aspect ratio, 0.1 mm scale bar, median (12 col) and p90 (23 col)
  per-visit front advance marked.
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
- [ ] TODO: the RK4 stability limit for the T-FEN transport stencil is recorded two ways
  (2.8 as implemented vs ~2.4 derived from a spectral radius of 1.1-1.2). §4.4.4 carries an
  inline TODO. Also confirm "monitored, not enforced during training" against the code;
  it is inferred from the out-of-bound final checkpoints and the parked bounded-velocity
  head.
- [ ] TODO: a parameter-matched free-form FEN control (width ~139, ~5 GPU-h at 5 folds) has
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
- [ ] TODO: 4.5 Moving-mesh extension as a tested hypothesis (DMM, dual branch, alpha gate).
- [ ] TODO: 4.6 Conditioning (covariates, LayerEncoder).
- [ ] TODO: 4.7 Training.
- [ ] TODO: 4.8 Implementation details.

### Chapter 5 - Experiments (`05-experiments.tex`)

- [ ] TODO: 5.1 Evaluation protocol (MSE caveat first, then Dice/IoU@360d, persistence floor).
- [ ] TODO: 5.2 Baselines.
- [ ] TODO: 5.3 Main results table + rollout figure.
- [ ] TODO: 5.4 Ablations sweep.
- [ ] TODO: 5.5 Moving mesh quality.
- [ ] TODO: 5.6 Qualitative analysis (success + failure modes).
- [ ] TODO: 5.7 Computational cost.

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

- [ ] TODO: cite **Gupta2023** -- Gupta & Brandstetter, *TMLR* 2023, "Towards
  Multi-spatiotemporal-scale Generalized PDE Modeling" (PDEArena). Used in §2.3 as the
  evidence that a U-Net is a standard strong surrogate baseline in the neural-PDE
  literature.
- [ ] TODO: cite **LiuSchiaffini2024** -- Liu-Schiaffini, Berner, Bonev, Kurth,
  Azizzadenesheli & Anandkumar, *ICML* 2024, "Neural Operators with Localized Integral and
  Differential Kernels". Used in §2.3 for the local-kernel bypass over a global operator.
- [ ] TODO: cite **Gao2019** -- Gao & Ji, *ICML* 2019, "Graph U-Nets". Used in §2.3 as the
  multi-scale counterpart on graphs. Note for §4.4: the repository's own `GAGraphUNet` is
  an image pyramid with a graph operator per block, **not** this work's learned node-score
  pooling — cite it as a disambiguation there, not as the method used.
- [ ] TODO: cite **Lienen2022** -- Lienen & Günnemann, *ICLR* 2022, "Learning the Dynamics
  of Physical Systems from Sparse Observations with Finite Element Networks". Used in §2.3
  and needed again in §4.4 for the FEN / T-FEN arm.
- [ ] TODO: cite **Chen2018** -- Chen, Rubanova, Bettencourt & Duvenaud, *NeurIPS* 2018,
  "Neural Ordinary Differential Equations". Used in §2.3 for the Neural-ODE reading of a
  residual update, and in §4.2.1 for the caution that the Euler form does not make
  f_theta a rate; needed again in §4.4 for the Runge--Kutta wrapper.
- [ ] TODO: cite **Ott2021** -- Ott, Katiyar, Hennig & Tiemann, *ICLR* 2021, "ResNet After
  All: Neural ODEs and Their Numerical Solution". Used in §2.3 for the solver-invariance
  requirement; needed again in §5.6 for the solver-swap diagnostic.
- [ ] TODO: cite **Krishnapriyan2023** -- Krishnapriyan, Queiruga, Erichson & Mahoney,
  *Communications Physics* 6:319, 2023, "Learning continuous models for continuous
  physics". Used with Ott2021 in §2.3 and §5.6. Cite the 2023 journal year, not the 2022
  preprint.
- [ ] TODO: cite **HuangRussell2011** -- Huang & Russell, *Adaptive Moving Mesh Methods*,
  Springer, Applied Mathematical Sciences vol. 174, 2011. Used in §2.5 as the classical
  background for moving meshes; also the source of the equidistribution-CoV mesh-quality
  measure needed in §5.5.
- [ ] TODO: cite **Liu2018** -- Liu, Lehman, Molino, Petroski Such, Frank, Sergeev & Yosinski,
  *NeurIPS* 2018, "An Intriguing Failing of Convolutional Neural Networks and the CoordConv
  Solution", arXiv:1807.03247. Used in §4.4.1 for the coordinate input channels.
- [ ] TODO: cite **Wu2018** -- Wu & He, *ECCV* 2018, "Group Normalization", arXiv:1803.08494.
  Used in §4.4.2 for the U-Net / graph U-Net normalisation.
- [ ] TODO: cite **Gilmer2017** -- Gilmer, Schoenholz, Riley, Vinyals & Dahl, *ICML* 2017,
  "Neural Message Passing for Quantum Chemistry", arXiv:1704.01212. Used in §4.4.3.
- [ ] TODO: cite **Courant1928** -- Courant, Friedrichs & Lewy, "Über die partiellen
  Differenzengleichungen der mathematischen Physik", *Mathematische Annalen* 100(1):32-74,
  1928, doi:10.1007/BF01448839. Used in §4.4.4 for the stability condition.
- [ ] TODO: cite **Butcher1987** -- Butcher, *The Numerical Analysis of Ordinary Differential
  Equations: Runge-Kutta and General Linear Methods*, Wiley 1987. Used in §4.4.5.
- [ ] TODO: cite **Hairer1993** -- Hairer, Nørsett & Wanner, *Solving Ordinary Differential
  Equations I: Nonstiff Problems*, Springer, 2nd rev. ed. 1993,
  doi:10.1007/978-3-540-78862-1. Used in §4.4.5.
- [ ] TODO: cite **Ba2016** -- Ba, Kiros & Hinton, "Layer Normalization", arXiv:1607.06450,
  2016 (preprint, no peer-reviewed venue). Used in §4.3.1 for the per-node normalisation.
- [ ] TODO: cite **Ioffe2015** -- Ioffe & Szegedy, *ICML* 2015, "Batch Normalization:
  Accelerating Deep Network Training by Reducing Internal Covariate Shift",
  arXiv:1502.03167. Used in §4.3.1 for the normalisation that is avoided. (Also cited by
  the MP-PDE paper itself for its 2-D experiments.)
- [ ] TODO: cite **Feuer2013** -- Feuer, Yehoshua, Gregori, Penha, Chew, Ferris, Clemons,
  Lindblad & Rosenfeld, *JAMA Ophthalmology* 131(1):110-111, 2013, "Square Root
  Transformation of Geographic Atrophy Area Measurements to Eliminate Dependence of Growth
  Rates on Baseline Lesion Measurements". Used in §3.1 for the square-root area scale of
  the cohort growth statistics; needed again in §5.1 for √area MAE and growth rates.
- [ ] TODO: cite **Mai2024** -- Mai, Lachinov, Reiter, Riedl, Grechenig, Bogunović &
  Schmidt-Erfurth, *Ophthalmology Science* 4(4):100466, 2024, "Deep Learning-Based
  Prediction of Individual Geographic Atrophy Progression from a Single Baseline OCT".
  Used in §2.6 as the closest prior work (same MUW cohort, same task), in §2.1.6 and §3.1 as the
  source of the device model, and in §3.6 for the one-year-anchor
  comparability choice; needed again in §5.7. **The pre-segmented-masks vs raw-OCT caveat must travel with every comparison.**
- [ ] TODO: cite **Salvi2025** -- Salvi et al., *Ophthalmology Science* 5(2):100635, 2025,
  "Deep Learning to Predict the Future Growth of Geographic Atrophy from Fundus
  Autofluorescence". Used in §2.6 as the dense-CNN precedent on this task (different
  modality, so not a comparable number); also the GA-domain motivation for the U-Net arm
  in §4.4.
- [ ] TODO: literature check -- is there any prior application of neural PDE solvers to
  biomedical disease progression or organ modelling? §2.6 currently states only that the
  application "remains sparse", with an inline `% TODO`. Either find and cite one or two
  examples, or make the absence an explicit, defensible claim.


External references introduced inline in the LaTeX drafts that still need to be added to `references.bib` (one entry per reference; each has a corresponding `% TODO: cite ...` marker in the .tex file). Once an entry is added to the bibliography, replace the placeholder author-year mention with the proper `\citet{}` / `\citep{}` and remove the matching `% TODO:` line.

- [ ] TODO: cite **Wong2014** -- Wong et al., *Lancet Glob Health* 2014, "Global prevalence of age-related macular degeneration and disease burden projection for 2020 and 2040." Used in `01-introduction.tex` §1.1 opening to support "leading cause of irreversible central vision loss in industrialised countries."
- [ ] TODO: cite **SchmidtErfurth2018** -- Schmidt-Erfurth et al., *IOVS* 2018, "Prediction of individual disease conversion in early AMD using artificial intelligence." Used in `01-introduction.tex` §1.2 as an AI-on-OCT precedent for cohort-level conversion prediction.
- [ ] TODO: cite **Bogunovic2017** -- Bogunović et al., *IOVS* 2017, "Machine learning of the progression of intermediate AMD based on OCT imaging." Used in `01-introduction.tex` §1.2 alongside SchmidtErfurth2018 as the supervisor's institutional AI-on-OCT precedent. (Earlier draft of `02-background.tex` §2.1.4 also cited it for the MUW segmentation pipeline; that usage was removed on 2026-05-02 because the MUW pipeline provenance is not actually established by this reference --- if confirmed, restore that usage in `03-data.tex` §3.1 instead.)
- [ ] TODO: cite **Ronneberger2015** -- Ronneberger et al., *MICCAI* 2015, "U-Net: Convolutional Networks for Biomedical Image Segmentation." Used in `01-introduction.tex` §1.2 to anchor the "standard U-Net" baseline mention. (2026-09-25: that §1.2 sentence was removed; still needed for §2.3 and §4.4.)
- [ ] TODO: cite **Battaglia2018** -- Battaglia et al., 2018, "Relational inductive biases, deep learning, and graph networks." Used in `01-introduction.tex` §1.3 to attribute the encode--process--decode GNN pattern. (2026-09-25: that §1.3 sentence was removed; the marker went with it. Still relevant for §2.4.)
- [ ] TODO: cite **SanchezGonzalez2020** -- Sanchez-Gonzalez et al., *ICML* 2020, "Learning to simulate complex physics with graph networks." Used in `01-introduction.tex` §1.3 alongside Battaglia2018 for the encode--process--decode pattern. (2026-09-25: that §1.3 sentence was removed; still relevant for §2.4.)
- [ ] TODO: cite **Li2021** (FNO) and **Lu2021** (DeepONet) -- needed for `02-background.tex` §2.3 (autoregressive vs operator-style neural solvers). (2026-09-25: the conditional §1.3 acknowledgement is moot; §1.3 names no architecture.)
- [ ] TODO: cite **Sadda2018** -- Sadda et al., *Ophthalmology* 2018, "Consensus Definition for Atrophy Associated with Age-Related Macular Degeneration on OCT: Classification of Atrophy Report 3." Used in `02-background.tex` §2.1.1 as the primary source for the cRORA criteria currently attributed only to Vallino2024.
- [ ] TODO: cite **Huang1991** -- Huang et al., *Science* 254:1178-1181, "Optical Coherence Tomography." Used in `02-background.tex` §2.1.2 to anchor the introduction of OCT as the canonical methodological-origin reference for the modality.
- [ ] TODO: cite an SD-OCT principle reference (e.g. **Wojtkowski2002** or **Drexler2008**) once added to `references.bib`. Used in `02-background.tex` §2.1.2 to support the spectral-domain OCT principle behind the SD-OCT acquisition platform.
- [ ] TODO: cite a canonical SWE textbook (e.g. **LeVeque2002**, "Finite Volume Methods for Hyperbolic Problems", Cambridge University Press, Chapter 13; or **Vreugdenhil1994**, "Numerical Methods for Shallow-Water Flow", Springer) once added to `references.bib`. Used in `02-background.tex` §2.2.1 where the shallow-water equations are introduced as the running example for the section.

### Bibliography

- [ ] TODO: replace placeholder entries in `references.bib` with actual thesis references (MP-PDE, MM-PDE, FNO, DeepONet, GA/OCT clinical literature, GNN foundations, etc.).
- [x] 2026-04-27: ingested 13 GA/OCT/clinical references (Boopathiraj2024, Boyer2017, Chu2022, Ebneter2016, Flaxman2020, Lad2023, Pilotto2015, Singh2025, Song2025, Trincao2024, Vallino2024, Vogl2021, Yehoshua2011) into `references.bib`; added 13 hub notes + 25 atomic concept spokes to `literature/`. Still pending: FNO, DeepONet, GNN foundations, AMD/OCT references beyond this batch.
- [ ] TODO: confirm citation key choice for Trincão-Marques 2024 — currently `Trincao2024` (ASCII for BibTeX safety); raw note in `pdfs/GA/Trincão2024.md` retains the diacritic.
- [ ] TODO: pre-existing inconsistency — `Hu2024` BibTeX entry has `year = {2023}` while the citation key is `Hu2024`. Untouched in this session; flag for cleanup if biblatex sorting becomes year-sensitive.

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
