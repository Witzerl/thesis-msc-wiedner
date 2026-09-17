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
- [ ] TODO (⚠️): `01-introduction.tex` §1.5 outline — describes a Method chapter built
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
- [ ] TODO: confirm `\ref{ch:background}`, `\ref{ch:data}`, `\ref{ch:method}`, `\ref{ch:experiments}`, `\ref{ch:discussion}`, `\ref{ch:conclusion}` resolve once the corresponding `\label{}` commands exist in the chapter source files (currently those chapters are placeholders).
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

- [ ] TODO: 3.1 MUW dataset description + example figure.
- [ ] TODO: 3.2 11-channel state tensor (clinical/data level only).
- [ ] TODO: 3.3 Spatial standardization (crop/pad justification, 6x6 mm window justification).
- [ ] TODO: 3.4 Per-channel normalization + mean/std table.
- [ ] TODO: 3.5 Age/Sex covariate extraction and encoding.
- [ ] TODO: 3.6 Temporal structure and $\Delta t$ computation.
- [ ] TODO: 3.7 Patient-level train/val/test splits.

### Chapter 4 - Method (`04-method.tex`)

- [ ] TODO: 4.1 Overview figure and component map.
- [ ] TODO: 4.2 $\Delta t$-conditioned residual formulation.
- [ ] TODO: 4.3 Multi-channel pipeline (tensor propagation only).
- [ ] TODO: 4.4 DMM for GA (physics loss, sampling, monitor function).
- [ ] TODO: 4.5 Single-branch MP-PDE architecture (no temporal bundling).
- [ ] TODO: 4.6 Dual-branch MM-PDE architecture (correction branch).
- [ ] TODO: 4.7 Patient covariate conditioning.
- [ ] TODO: 4.8 Surrogate equation encoder (LayerEncoder).
- [ ] TODO: 4.9 Training (pushforward, ItpNet pre-training, loss weighting).
- [ ] TODO: 4.10 Implementation details.

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
  residual update; needed again in §4.4 for the Runge--Kutta wrapper.
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
- [ ] TODO: cite **Mai2024** -- Mai, Lachinov, Reiter, Riedl, Grechenig, Bogunović &
  Schmidt-Erfurth, *Ophthalmology Science* 4(4):100466, 2024, "Deep Learning-Based
  Prediction of Individual Geographic Atrophy Progression from a Single Baseline OCT".
  Used in §2.6 as the closest prior work (same MUW cohort, same task); needed again in
  §5.7. **The pre-segmented-masks vs raw-OCT caveat must travel with every comparison.**
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
- [ ] TODO: cite **Ronneberger2015** -- Ronneberger et al., *MICCAI* 2015, "U-Net: Convolutional Networks for Biomedical Image Segmentation." Used in `01-introduction.tex` §1.2 to anchor the "standard U-Net" baseline mention.
- [ ] TODO: cite **Battaglia2018** -- Battaglia et al., 2018, "Relational inductive biases, deep learning, and graph networks." Used in `01-introduction.tex` §1.3 to attribute the encode--process--decode GNN pattern.
- [ ] TODO: cite **SanchezGonzalez2020** -- Sanchez-Gonzalez et al., *ICML* 2020, "Learning to simulate complex physics with graph networks." Used in `01-introduction.tex` §1.3 alongside Battaglia2018 for the encode--process--decode pattern.
- [ ] TODO: cite **Li2021** (FNO) and **Lu2021** (DeepONet) -- needed for `02-background.tex` §2.3 (autoregressive vs operator-style neural solvers) and conditionally for a one-sentence acknowledgement in `01-introduction.tex` §1.3.
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

- [x] 2026-05-02: switched the biblatex configuration in `main-thesis.tex` from `style=ACM-Reference-Format,citestyle=numeric` to `style=authoryear,natbib=true` so that the natbib-style commands `\citet` / `\citep` mandated by `CLAUDE.md` produce author-year output. Other biblatex options (`backend=biber`, `sortcites=true`, `maxcitenames=2`) preserved.
- [ ] TODO: confirm with supervisor that the JKU technical-report template tolerates the author-year deviation from the bundled ACM numeric default; if not, a one-line revert restores the original style.
