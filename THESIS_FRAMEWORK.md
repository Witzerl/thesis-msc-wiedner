# THESIS_FRAMEWORK.md — The complete framework, end to end

> **⚠️ MIRROR FILE — copied from the code repository, 2026-09-17** (code repo
> `HEAD e3d2df7`; source path `masterthesis-docker/GraphPDE/demos & explanations/THESIS_FRAMEWORK.md`).
> The code repo is the source of truth; do not edit this copy — edits here do not
> flow back. It is mirrored into the thesis repo because it is the technical
> source of truth for Chapters 3–5 (data, method, experiments) and is needed when
> drafting away from the code machine. **All relative links below are dead on this
> side** — they point into `masterthesis-docker`. This file is deliberately *not*
> `@`-referenced from `CLAUDE.md` (it is ~280 KB); read the relevant `§` on demand.

> **Purpose.** Single source of truth for the *technical* content of the master thesis:
> everything the code does, from raw data to reported metric, in one document. It is
> deliberately mechanism-first and maths-light — formulas appear where they are needed to
> be unambiguous, but the goal is that no component, transformation, or training decision
> is missing. LaTeX-ready mathematics can be layered on top of this later.
>
> Relationship to the other documents: [PROJECT_CONTEXT.md](../../PROJECT_CONTEXT.md) states
> *what and why* per architectural decision; [ARCHITECTURE.md](../../ARCHITECTURE.md) maps each
> decision to *where in code*; [NOTES.md](../../NOTES.md) is the chronological audit trail;
> [EXPERIMENTS.md](../../EXPERIMENTS.md) covers run infrastructure. This document is the
> *narrative synthesis* of all of them plus direct code reading — written 2026-08-14 at
> git HEAD `ecdf2fb` (+ working tree), re-synced 2026-08-15 to HEAD `2fb9485`
> (per-graph Dice + monotonic penalty, `--exclude_pad_nodes`, `--euler_dt_scale`,
> runtime-selectable k, pad-aware endpoint eval + `_anat` column, solver-resume
> disable, scorer `ref_pad`, the crop-censoring census, and the 2026-08-14/15 era
> boundary), and **re-synced again 2026-08-17** for everything that landed after it:
> the Stage-F1 loss lock (monotonic → 0.0), the F1b architecture and k controls, the
> single-branch 5-fold CV and its seed arm (T1), the **±0.0127 replicate noise
> floor**, `euler_dt_scale` re-locked to True, the α/bypass mechanism finding, and
> the repository prune (SLO DMM runs, the n24 precompute and several docs/tools
> removed; results now read from the two committed CSVs, §8). Facts marked
> *(measured)* were established by direct inspection of the data/code.
>
> **⚠️ Currency: last full sync 2026-08-24 (git `d2b821b`, the 5/5-fold dual/bypass
> readout), corrected and extended in place 2026-09-16.** The body below was written
> against that state. Three classes of change have landed since; §0–§9 have been corrected
> for them, and the material they needed that the document did not have was written as two
> new sections — **§4b** (the countermodel family, the Neural-ODE wrapper and the Finite
> Element Network, with the shared backbone contract and the parameter-matching table) and
> **§7.5** (the thesis-bound results, each with its instrument and its caveat). The summary
> stays here because it is what a reader needs before §4 onward:
>
> - **The locked configuration changed (2026-09-03).** The canonical uniform branch no
>   longer runs on the precomputed k-NN graph. It is the **dilated stencil** built at
>   forward time — `--backbone anisognn`, rows ±1 × columns {0, ±7, ±14, ±21},
>   20 neighbours — with `--gnn_aggr mean` (67 147 params). The k = 12 index-space k-NN
>   with `mean_max` (75 339 params) is now the **comparison arm** (`--backbone gnn`), and
>   `edges_global.pt` remains the *data* graph that arm consumes; the moved branch
>   builds its own k-NN on the warped mesh (§2.5, §2.9, §5.2;
>   ARCHITECTURE.md §1; PROJECT_CONTEXT.md §5).
> - **The countermodel and variant arms ran.** External baselines T7–T7d (U-Net at two
>   capacities, the per-pixel floor, FNO, the localized-kernel FNO hybrid) and the
>   GNN-internal variants T7e–T7i (per-graph normalisation, aggregation × normalisation,
>   edge-feature and norm-site arms, the dilated stencil), plus T7j — the locked v2 model
>   at 2 seeds × 5 folds.
> - **Several axes this document calls "planned" are measured.** T5 (the LayerEncoder
>   width sweep — a null at every width), T6 (covariates), T8 (the locality cliff), and
>   T8n/T8f/T8g/T9/T9b — fixed-step Runge–Kutta integration
>   ([GraphPDE/baselines/odeint.py](../baselines/odeint.py)), the Finite Element Network
>   ([GraphPDE/baselines/fen.py](../baselines/fen.py)) and the gate's weight decay.
>
> §7.5 indexes all of these with their instruments and caveats. For the full readouts read
> [SOLVER_FINAL_RUNS.md](SOLVER_FINAL_RUNS.md) §5–§9.15 and the NOTES.md *Thesis-bound
> results* table; the code wins over all three.

## Contents

- §0 — Overview: the problem, the framework and its swappable slot, the pipeline
- §1 — The dataset: raw data, cohort statistics, covariates, splits
- §2 — Preprocessing: graph precomputation and the runtime dataset
- §3 — The DMM (Data-free Mesh Mover): model, physics, training, refinements
- §4 — **Backbone I** — the graph solver: GA-adapted MP-PDE GNN + LayerEncoder surrogate
- §4b — **Backbone II** — the rest of the family: U-Net, FNO and the local-kernel hybrid, graph U-Net, the dilated stencil (the locked model), Runge–Kutta integration, the Finite Element Network
- §5 — The dual-branch MM-PDE composition: moved mesh, ItpNet, α-gate
- §6 — Training: loss regime, pushforward/unrolling, optimization
- §7 — Evaluation: metrics, rollout mechanics, baselines, model selection, results summary
- §8 — Reproducibility infrastructure
- §9 — Chronology of load-bearing fixes (what it took to make it work)
- §10 — References: the published work this document relies on, and what is this repo's own

---

# 0. Overview

## 0.1 The task

Predict the future progression of **Geographic Atrophy (GA)** — an advanced, irreversible
form of age-related macular degeneration in which patches of retinal tissue atrophy and
the lesion area grows over time — from **longitudinal OCT imaging**. Given a patient
eye's current retinal state (GA segmentation + retinal layer geometry) and clinical
covariates, the model predicts the retinal state at a future visit, an arbitrary and
*irregular* time interval Δt later. The clinical deliverable is the predicted GA
segmentation mask; the headline evaluation is segmentation overlap (Dice) of the
*newly atrophied region* at a one-year horizon.

## 0.2 The question, the framework, and the backbone family

**The thesis asks what a model needs in order to do this, and what framework it
needs to sit in — not whether one particular architecture can.** That is worth
stating up front because the project did not start there. It started as an
adaptation of two specific neural-PDE-solver frameworks, and the largest single
block of engineering in this document is still that adaptation (§3, §4, §5).
What the adaptation produced, though, is a **fixed experimental framework with
one swappable slot**, and what the thesis reports is a survey through that slot.

**Fixed for every arm — this is the framework, and it is the part that
demonstrably transfers.** One visit in, no history. An 11-channel state on the
`49×1024` en-face grid. A Δt-conditioned autoregressive residual operator
`u(t+Δt) = u(t) + Δt · f_θ(u(t), Δt)` evaluated on all channels, with a
zero-initialised head so every model starts at exact persistence. The
time-budgeted pushforward curriculum (§6.2), the channel-weighted MSE + soft-Dice
objective (§6.1), per-module gradient clipping, and the same optimiser, epoch
budget, folds, seeds, evaluation, model selection and replicate floor (§7).

**Variable — this is the survey.** `f_θ` itself, selected by `--backbone` and
optionally wrapped by `--integrator`. Nine settings of that slot, spanning six
architecture classes, have run through
the identical pipeline: a message-passing GNN on a k-NN graph (§4), the same GNN
on a dilated physical-scale stencil (§4.3b — the locked model), a U-Net at two
capacities, an FNO, an FNO with a local-kernel bypass, a graph U-Net, a Finite
Element Network with a learned transport term, a fixed-step Runge–Kutta
integration of any of them, and a per-pixel floor (§4b). The comparison is
controlled because **only `f_θ` changes**: loss, curriculum, evaluation and
bookkeeping live in one shared pipeline that a backbone module is forbidden to
duplicate (§4b.1), and the bit-identical persistence fingerprints across arms
prove it held.

**The headline is that the framework transfers and the architecture class does
not decide the outcome.** The three strongest arms — the dilated-stencil GNN
(0.5258), the parameter-matched U-Net (0.5046) and the T-FEN (0.5337) — are
statistically **indistinguishable** from one another at the available precision
(§7.5), while a model with no spatial context at all is bit-exactly persistence
(0.0000). What separates arms is therefore not the operator class but which
*ingredients* they carry, and §7.5 measures those one at a time: spatial context
(required, trivially), **physical reach at lesion scale** (+0.074 over the k-NN
GNN, the largest effect here), **global context and local detail together** (a
global-only FNO is established *below* the U-Net; +800 parameters of local
bypass bring it level, and to +0.047 over the GNN on 5/5 folds), and **an
explicit transport term** (+0.053) all graduate; capacity, mesh adaptation,
integration order, normalisation, aggregation, edge-direction features, patient
covariates and the learned coefficient surrogate are all measured nulls. Reach
and transport are two independent routes to the *same* deficit, and that
coincidence — not any single arm's score — is the project's central
architectural result.

**§4 and §4b are two halves of one chapter, not a subject and its appendix.**
§4 is the graph solver in full detail because it is the arm the project built
rather than imported; §4b is everything else on the same terms, and one of its
modules is the locked model. Read them together.

**Where it started.** Two frameworks from the neural-PDE-solver literature,
which supplied the time-stepping formulation, the mesh mover and the first
backbone:

- **MP-PDE** (Brandstetter et al., *Message Passing Neural PDE Solvers*, ICLR 2022) — an
  encode–process–decode **graph neural network** that learns the update operator of a PDE:
  message passing over a spatial graph plays the role of a learned finite-difference
  stencil, and the network predicts the next K time steps at once (temporal bundling,
  K ∈ {20, 25, 50} upstream) as cumulative-Δt-scaled residuals on top of the most recent
  input frame, rolled out autoregressively.
- **MM-PDE** (Hu et al., *Better Neural PDE Solvers Through Data-Free Mesh Movers*,
  ICLR 2024) — extends MP-PDE-style solvers with a **moving mesh**: a separately
  pretrained, frozen **DMM** (Data-free Mesh Mover) deforms the computational grid so
  node density concentrates where the solution has structure (here: the GA lesion
  boundary), and a second GNN branch operating on the moved mesh contributes a
  correction that is interpolated back to the uniform grid.

**Why a PDE-solver framing for GA?** GA progression is hypothesised to behave like a
*locally driven growth process*: the lesion boundary advances based on the local tissue
state, similar to a reaction–diffusion front. A message-passing GNN encodes exactly this
prior — each node's update depends on its spatial neighbourhood — and high-inductive-bias
models are the principled choice in the low-data regime of a clinical cohort (75 eyes).
The moving-mesh extension tests a sharper hypothesis: that concentrating computational
resolution at the lesion boundary (where all the change happens on the ~21:1 anisotropic
OCT grid) improves boundary prediction. Honest framing for the thesis: the frameworks
were initially *suggested by the clinical partner (MUW)*; the locality/inductive-bias
justification was then built and tested empirically (receptive-field sweeps, capacity
grids — §9), and the moving-mesh contribution is treated as a *measurable question*, not
an assumption — the learnable gate α on the moved branch (§5.4) was designed to make
"does mesh adaptation transfer to slow-progressing GA?" a direct measurement, with the
negative result pre-registered as a reportable outcome. **That design intent was only
partly realised**: α stays shut in the parameter-matched bypass control as well as in
the mesh arm, so what the gate ended up measuring is the correction branch's failure to
optimise rather than the mesh's usefulness (§5.1, §5.5) — the negative result is
reportable, but must be scoped accordingly.

**Measured outcome (2026-08-25 to 2026-09-03), which re-reads the paragraph above.** A
parameter-matched U-Net (Ronneberger et al. 2015 — §4b.3, §10; 83 081 params) beat the
then-locked k = 12 index-space k-NN GNN
by **+0.053 ± 0.023 SE** change-region Dice paired across 5 folds (4/5 folds; per-eye
55/75 eyes), and the seed-7 replicate strengthened it to **+0.068 ± 0.020 SE, 5/5**.
⚠️ **Mind the pairing convention on that second figure, because the two seed replicates
in this document do not use the same one.** The +0.068 pairs the seed-7 U-Net against the
**seed-42** GNN (§9.6e states this and gives both); the *same-seed* pairing, which is the
convention §9.12e later adopts for the stencil's own replicate, reads **+0.0655 ± 0.0209
fold-paired and +0.0618 ± 0.0103 per eye (60/75)**. Either way the effect replicates and
grows (+0.0531 → +0.0655 same-seed), so nothing about the conclusion turns on it — but a
sentence that sets the U-Net's +0.068 beside the stencil's +0.0736 is comparing a
cross-seed number with a same-seed one, and the like-for-like pair is +0.0655 vs +0.0736.
Quote same-seed for both *(re-derived from the runs' `mai/` records, 2026-09-17)*. The
low-data, high-inductive-bias half of the argument survived that result — a
44.5×-parameter U-Net erases its own win (+0.005 ± 0.009 SE, 2/5 folds, per-eye worse) —
but the *graph construction* named above did not. The index-space k-NN is isotropic in
grid steps and therefore ~21× anisotropic in millimetres: at k = 12 a hop reaches
±0.25 mm across B-scans but only ±0.011 mm along them, against a GA front that advances a
median ~12 columns per 180-day visit, and neither depth nor a larger index-space k buys
that reach (both measured null — which is why the receptive-field and capacity sweeps
cited here read flat). Replacing it with a dilated stencil at physical lesion-scale
offsets (rows ±1 × columns {0, ±7, ±14, ±21}, ≈±0.12 mm on both axes) lifts the *same*
network by **+0.074 ± 0.008 SE, 5/5 folds** — 74/75 eyes — to within the available
precision of the U-Net, and is the locked v2 uniform graph. Read the prior accordingly:
locality at physical lesion scale transfers; the index-space k-NN realisation of it did
not (SOLVER_FINAL_RUNS.md §9.6b–d, §9.12b–e). All deltas here are late-epoch
change-region Dice@360d, fold-paired, against the ±0.0127 replicate floor (§7.4: a
5-fold paired mean needs > 0.016, a single fold > 0.036); the per-eye counts are the
separate pooled-eye instrument, and the two must be quoted together rather than
interchangeably.

**What had to change relative to the upstream frameworks** (the applied contribution):

1. **Irregular time steps.** Clinical visits have no shared t=0 and irregular gaps
   (90–720 days). The solver is a **Δt-conditioned Euler residual operator**
   `u(t+Δt) = u(t) + Δt · f_θ(u(t), Δt)` (§4.5) rather than a fixed-step solver.
2. **Multi-channel clinical state.** 11 channels (GA mask + 10 retinal layer boundary
   depth maps) instead of 1–3 physical fields (§1.4, §2.2).
3. **Patient covariates.** Age and sex enter the GNN's conditioning vector (§2.6, §4.1).
4. **A learned surrogate for the PDE coefficients.** MP-PDE assumes known equation
   parameters; here a small CNN (**LayerEncoder**) compresses the 10 layer channels into
   a global embedding that conditions the dynamics (§4.6).
5. **Extreme grid anisotropy.** The en-face OCT grid is 49×1024 over a ≈6×6 mm square
   domain — a ~21:1 pixel-spacing anisotropy that broke, at various points, the k-NN
   graph construction, the physical scaling of the DMM monitor's finite differences
   (×(Nx−1) vs ×(Ny−1), §3.3 — the native-grid DMM failure itself was the binary mask's
   step gradient, not the anisotropy; §3.6, §3.7 item 5, §9.2), the moved-mesh edge
   construction, and the interpolation stencil, and required dedicated fixes throughout
   (§2.5, §3.7, §5.2, §9). Most consequentially for the results, it also governs the
   **physical reach** of the uniform graph — at k = 12 a hop spans ±0.25 mm across
   B-scans but only ±0.011 mm along them — which is what the 2026-09-03 v2 dilated
   stencil fixes (§0.2 above; PROJECT_CONTEXT.md §5, ARCHITECTURE.md §1).
6. **Temporal bundling removed (K=1).** Upstream MP-PDE predicts K future steps at once;
   this framework is committed to strict K=1, because clinical sequences are short and
   the DMM's mesh is computed from a single snapshot — a K>1 window would use a stale
   mesh for the later steps (hard rule; PROJECT_CONTEXT.md §5).

Items 3 and 4 are implementation deltas, not claimed wins. Both ablations have since run:
the covariate arm (T6) reads **+0.020 ± 0.014 SE fold-paired (3/5) and +0.019 ± 0.008
per-eye (43/75) in favour of *removing* age and sex** — the defensible claim is that they
contribute nothing detectable and the residual points against them, not that the two
conditions are equivalent — and the LayerEncoder width sweep (T5) is a null at every
width (§4.6). Item 1 is not a null: the fold-2 arm-N screen reads −0.005 for zeroing the
Δt feature slot, and the separate 5-fold `--euler_dt_scale` test of the ×Δt multiplier
was also under the floor (+0.0134), but the multiplier is kept for the Δt → 0 persistence
limit (§4.5).

## 0.3 The pipeline at a glance

```
raw MUW_GA data (553 Heidelberg OCT volume scans, 75 eyes)
        │
        ▼
[1] tools/precompute_graphs_ga.py           — per-fold graph precompute
        │   11-ch states (49×1024), z-score, k-NN edges (index space),
        │   consecutive-visit windows with Δt (years), covariates
        ▼
data/GA/split{N}_.../precomp/{edges_global.pt, meta_global.pt, train/, val/}
        │
        ├──────────────────────────────────────────────┐
        ▼                                              ▼
[2] GraphPDE/mesh/dmm.py                     [3] GraphPDE/train.py
    DMM pretraining (frozen afterwards)          solver training
    - input: binary GA mask, native              - single-branch (MP-PDE baseline):
      (49, 1024) grid (--mask_source oct)          --moving_mesh False
    - Monge–Ampère loss on a monitor             - dual-branch (MM-PDE):
      built from the blurred mask                  --moving_mesh True
    - output: mesh-moving potential φ              + frozen DMM checkpoint
        │                                          + ItpNet + α-gate
        └────────────── checkpoint ──────────────► (moved branch)
                                                       │
    uniform branch (locked v2, 2026-09-03):            │
      --backbone anisognn --gnn_aggr mean              │
      (dilated stencil built at forward time;          │
       the precompute's k=12 k-NN edges then           │
       serve only --backbone gnn --gnn_aggr            │
       mean_max and the moved branch)                  │
    countermodels: --backbone {unet,fno,gunet,fen}     │
      (GraphPDE/baselines/); optional fixed-step       │
      RK integration via --integrator (odeint.py)      │
                                                       ▼
[4] Evaluation (inside train.py, every epoch)
    per-step losses; per-eye autoregressive rollout;
    change-region Dice/IoU @ 360 d (headline); persistence baseline;
    Mai-2024 cohort metrics; NPZ rollout export
```

Three training pipelines run in order: (1) precompute, (2) DMM pretraining, (3) solver
training; evaluation is built into (3). The DMM is **pretrained separately and frozen**
during solver training — it is an unsupervised, input-side preprocessor (it only ever
sees the GA mask, never future labels), so it can be trained on the whole cohort's masks
without leaking the prediction target (§3.5).

---

# 1. The dataset

All numbers in this section were re-measured directly on the repository data on
2026-08-14 unless a doc source is cited. Raw data lives under `data/MUW_GA/`.

## 1.1 Headline numbers

| Quantity | Value |
|---|---|
| Patients in the 5-fold split universe | 100 (of which 49 have no scans) |
| Patients with usable scans | **51** (24 contribute both eyes, 27 one eye) |
| Eyes (the sample unit) | **75** |
| Visits (OCT acquisitions) | **553** |
| Visit→next-visit windows (training transitions) | **478** (= 553 − 75) |
| Visits per eye | min 5 / median 7 / max 13 |
| Follow-up span per eye | 720–2160 days (median 1080 d ≈ 3 y) |
| Modal visit interval | **180 days** (76.2 % of windows); shortest 90 d |
| Modelling grid (after crop/pad) | **(49, 1024)** = 50 176 nodes ≈ **5.938 × 5.816 mm** |
| En-face pixel spacing | 0.12118 mm (rows, between B-scans) × 0.00568 mm (cols, along B-scans) — **acquisition-spacing ratio 21.335 : 1** |
| Graph node pitch (`build_pos_xy`, `linspace(0, L, N)`) | 0.123705 mm × 0.005686 mm = `L/(N−1)` — **node-pitch ratio 21.758 : 1**, 2.08 % coarser than the acquisition spacing on the row axis. This is the metric `data.pos` carries, so every physical-mm k-NN distance and receptive-field figure is in it (§2.5) |
| State channels | **C = 11** (binary GA mask + 10 layer-boundary depth maps) |
| Temporal bundling | **K = 1** (single transition per window, hard commitment) |
| Time encoding | `delta_adapted`: per-window Δt stored in **years** (days/365) |
| Covariates | 2: `[age_zscore, sex]` (sex 0 = female, 1 = male) |

## 1.2 What one visit physically is

Every visit is a **Heidelberg OCT volume scan** ("Volume scan ART mode", vendor
*Heidelberg Engineering*, study *HRF SPEC*, single Vienna site AT09000 — constant
across all 553 rows of `index_v2.csv` *(measured)*; the device is a **Spectralis**
per Mai et al. 2024's description of the same MUW dataset — Mai, J., Lachinov, D.,
Reiter, G. S., Riedl, S., Grechenig, C., Bogunović, H., Schmidt-Erfurth, U.,
*Deep Learning-Based Prediction of Individual Geographic Atrophy Progression from a
Single Baseline OCT*, Ophthalmology Science 4(4):100466, 2024,
doi:10.1016/j.xops.2024.100466 — so the *device model* is an inference from that paper,
not a field of this repository's data, which records only the vendor; confirm with the
data provider for the thesis). The native volume axes are
(n_B-scans, axial depth, n_A-scans) — e.g. `output_shape: [51, 496, 1077]` in a sample
visit's `oct.transform.json` — i.e. ~38–66 parallel B-scan slices, each 496 px deep and
~961–1719 A-scans wide. The repository stores per visit not the raw volume but
**registered 2-D en-face derivatives** of it:

`data/MUW_GA/scans/<EYE_ID>/<TIME_DAYS>/` (eye IDs are `<PatientID>_<OD|OS>`; visit
directories are named by day-in-study: `0`, `90`, `180`, `360`, …):

| file | content *(measured on samples)* |
|---|---|
| `mask_oct.png` | binary GA mask on the OCT en-face grid (mode `L`, values {0, 255}), e.g. (51, 1077) uint8 |
| `layers_oct.npz.npy` | (rows, cols, **10**) **int16** — 10 retinal layer-boundary depth maps in axial pixels (0–210 in this sample; cohort-wide the values span **−14…499**, i.e. the upstream segmentation occasionally goes slightly negative or beyond the nominal 496-px depth) |
| `mask_global.png` | GA mask in the SLO fundus frame, ~1536² or ~768² |
| `slo_global.png`, `faf_global.png` | SLO fundus image and fundus-autofluorescence image (same SLO frame; not used by the pipeline) |
| `slo.transform.json` | SLO-frame transforms + `transform_oct_fov` = homogeneous corner coordinates of the OCT field of view inside the SLO frame |
| `oct.transform.json` | full OCT↔SLO transform stack; the key entry is **`T_mask`**, a diagonal affine mapping OCT en-face array coordinates → `mask_global.png` array coordinates (verified cohort-wide at native resolution: median IoU 1.000, minimum 0.99957, on all 553 visits) |

Only `mask_oct.png` + `layers_oct.npz.npy` are *required* per visit; an eye is included
if ≥2 visits carry both ([tools/precompute_graphs_ga.py](../../tools/precompute_graphs_ga.py),
`scan_dataset`). All 75 eye directories pass.

**Native shapes vary per eye but not within an eye** *(measured)*: 67 distinct
(rows, cols) shapes across the cohort, rows 38–66, cols 961–1719, constant within each
eye. The reason: raw acquisitions had varying B-scan spacing
(`Visit.Scan.ScanSpacing_mus` 115–258 µm in `index_v2.csv`), and the stored en-face
arrays were **resampled upstream to one constant "gold-standard" pixel spacing**
`[0.12118, 0.003867, 0.00568]` mm = (B-scan spacing, axial, A-scan spacing) — so pixel
*spacing* is treated as constant across the cohort while pixel *counts* differ. (Caveat
worth carrying: that constant's cohort-wide validity is **unverified** — NOTES F10.14
measures a ~2 % deviation against the visits' own transform files and needs DICOM to
settle; every mm² figure inherits it. §9.4.) In the [51, 496, 1077] sample above
(`GX511402_OS`, 1536² SLO) `T_mask`'s row scale is **20.08** and its column scale
**0.960** — a row:column ratio of 20.92, i.e. one OCT en-face row spans ~21 SLO pixels:
the same ~21:1 anisotropy (0.12118/0.00568 ≈ 21.3) that recurs throughout the framework.
Cohort-wide the row scale is bimodal (roughly halved for the ~768² SLO frames: 126 + 61
visits at 10–11 against 9 + 92 + 226 + 39 at 19–22) *(measured, all 553
`oct.transform.json`)*.

**The 10 layer channels** are depth maps: for each en-face position, the axial pixel
index of a segmented retinal boundary surface, ordered superficial → deep (channel
means increase monotonically 137 → 204 px *(measured, split-2 train stats)*; with the
0.003867 mm axial pitch that is ≈0.53–0.79 mm mean depth). Retinal thickness (last minus
first surface) is **not** computed anywhere in this pipeline: the only such computation is
upstream, in `muw_ga_dataset/process_data.py`, where it is resized to 256² uint8 purely to
build the per-eye debug GIF `data/MUW_GA/debug/eye_<ID>_thickness.gif`. It is recoverable
from the layer channels but is neither stored nor consumed. The anatomical names of the ten
surfaces are **not recorded in the repository** (generic `layer_0…layer_9`); they must
be sourced from the MUW segmentation pipeline documentation for the thesis text.

## 1.3 The visit schedule (drives curriculum + evaluation design)

From [COHORT_VISITS.md](COHORT_VISITS.md) (auto-generated by
[tools/cohort_visit_stats.py](../../tools/cohort_visit_stats.py) from the canonical
precompute; interval distribution independently confirmed by the raw
`index_v2.csv` `time_to_next_visit` column *(measured)*):

| interval | windows | share | eyes containing it |
|---|---|---|---|
| 90 d | 67 | 14.0 % | 10 |
| 180 d | 364 | **76.2 %** | 72 |
| 270 d | 2 | 0.4 % | 2 |
| 360 d | 38 | 7.9 % | 28 |
| 540 d | 6 | 1.3 % | 5 |
| 720 d | 1 | 0.2 % | 1 |

Every gap is a multiple of the 90-day acquisition grid. Three structural facts shaped
the pipeline:

1. **All 67 ninety-day intervals belong to 10 eyes from 7 patients** (a densely-imaged
   sub-cohort). Any pushforward budget short enough to exclude the modal 180-day interval
   trains exclusively on that unrepresentative subgroup.
2. **Pushforward reach**: at a 90-day time budget, **0/75 eyes** can chain two visits
   (the shortest gap equals the budget and the step counter undershoots) — the
   arithmetic proof behind the curriculum fix of §6.2. At 360 d, 74/75 eyes reach ≥1
   autoregressive step; 540 d gives ≥2 steps for 68/75; 720 d for 73/75.
3. **The @360d endpoint has no upper bound**: the rollout metric fires at the first step
   with cumulative time ≥ 346.75 days, so 68/75 eyes are scored at exactly 360 d but
   **7/75 (9.3 %) are scored at 450–720 d** (where the ground-truth change region is
   1.3–1.7× larger). Accepted deliberately for comparability with Mai et al. 2024, but
   it must be stated in the thesis.

## 1.4 The state representation

Channel 0 is the **binary GA mask** (the prediction target and clinical deliverable);
channels 1–10 are the **layer-boundary depth maps** (continuous, well-behaved; they act
as context/auxiliary targets and feed the LayerEncoder surrogate, §4.6). Channel order
`[mask, layer_0, …, layer_9]` is a hard invariant — "channel 0 = mask" is hard-coded in
the loss weighting and the LayerEncoder extraction, and the DMM's native-grid loader
asserts it at load time.

## 1.5 Clinical covariates

- `data/MUW_GA/clinical_covariates.csv`: `eye_index, age, sex`; 187 rows (the wider
  study cohort), **100 % coverage of the 75 dataset eyes** *(measured)*. Restricted to
  the 75 eyes: age 60.7–88.0 (mean 76.4), 47 female / 28 male eyes. Ages are decimal
  (computed birthdate→baseline, not hand-typed). The CSV is keyed per *eye*: a
  patient's two eyes appear as separate `_OD`/`_OS` rows carrying duplicated
  age/sex values.
- Source table: `Data_GA_PatriciaBui.xlsx` — a per-eye clinical study table that also
  contains progression rate (mm²/y), pseudodrusen status, predominant FAF pattern, and
  hyperreflective-foci (HRF) concentrations. **Only age and sex are used** by the
  pipeline; the rest exist as unexploited covariates (a possible future-work note).
- Historical trap (fixed 2026-07-05): the covariates CSV used to default to
  `index_v2.csv`, which has an eye-ID column but *no* age/sex — it parsed fine and
  silently produced a constant, information-free covariate channel. The precompute now
  defaults to `clinical_covariates.csv` and hard-fails on a CSV with no usable age.

## 1.6 Splits and the evaluation protocol

`data/MUW_GA/splits/split_{0..4}.json` define a clean **patient-level 5-fold CV** over a
fixed universe of 100 patient IDs: each fold is 80 train + 20 val patients; the five val
sets are pairwise disjoint and their union is the full universe *(measured)*. IDs carry
no `_OD/_OS` suffix, so **both eyes of a patient always land in the same partition** (no
patient-level leakage). Only 51 of the 100 patients have scans, which makes per-fold
*eye* counts uneven despite the balanced patient split:

| fold | train eyes / windows | val eyes / windows |
|---|---|---|
| 0 | 55 | 20 |
| 1 | 63 | 12 |
| 2 (canonical single fold) | 59 / 378 | 16 / 100 |
| 3 | 60 | 15 |
| 4 | 63 | 12 |

**The test split is structurally empty**: the precompute assigns any eye whose patient
is outside both lists to `test`, but every scan-bearing patient is inside the 100-ID
universe, so no precompute has a `test/` directory. The effective protocol is 5-fold
train/val cross-validation; "test = rest" is vacuous and the thesis should describe the
protocol as such.

## 1.7 Precompute inventory (current)

The canonical precompute family is `data/GA/split{N}_n12_zscore_slo256_{variant}/precomp`
(n12 = k-NN k=12, per-channel z-score, `slo_mask_size=256`), with variants
`agevisit` (per-visit age; the canonical), `agebaseline`, `nocov` (covariate ablation),
each for folds 0–4, plus one `split2_n12_minmax_slo256_agevisit` (normalization
ablation) — **16 precomputes total** *(measured 2026-08-17)*. A
`split2_n24_zscore_slo256_agevisit` dir existed briefly, built as the fix for the void
K24 leg and then kept as the bit-identity verification artifact for runtime-selectable
k; it has since been **removed**, because one folder now serves every k (§2.1) and
per-k folders are no longer part of the workflow. The legacy
`data/geographic_atrophy_*` paths named in older docs no longer exist. Note on the
`slo_mask` field: **all 16 remaining dirs predate the 2026-08-09 registration fix** and
carry the mis-registered field (mean IoU 0.588, median 0.64) — uniformly, so the
earlier "the family mixes two SLO registrations" caveat no longer applies. Deliberate:
the SLO field feeds only the deprecated SLO-DMM path, which the solver no longer
consumes (§2.7, §3.6).

# 2. Preprocessing: graph precomputation and the runtime dataset

Preprocessing is a one-shot, per-fold script — [tools/precompute_graphs_ga.py](../../tools/precompute_graphs_ga.py)
— that converts the raw visit files into a graph dataset the trainers load directly.
Normalisation statistics and windowing are baked into the precompute, which is why the
outputs are called *precomputes*, and so is the k-NN graph at the build k. The graph is
not fixed, though: `_2Dataset_preloaded` rebuilds it at dataset-construction time
whenever `--neighbors` differs from the file's k (§2.1), and the locked v2 backbone
(`--backbone anisognn`, the `jobs/train_solver.slurm` default) bypasses the precomputed
`edge_index` altogether, building its dilated stencil once in `GAAnisoGNN.__init__` and
only re-offsetting it per batch at forward time (§2.5).

## 2.1 Invocation and outputs

```bash
python -m tools.precompute_graphs_ga \
  --data_root data/MUW_GA \
  --out_dir   data/GA/split2_n12_zscore_slo256_agevisit/precomp \
  --split_idx 2 --neighbors 12 --normalize zscore \
  --crop_size 49 1024 --dt_unit years --age_mode per_visit --slo_mask_size 256
```

CLI (full): `--data_root`, `--out_dir` (required); `--split_idx` (default 2);
`--neighbors` (12); `--normalize` (`zscore` | `minmax`); `--crop_size` (`49 1024`);
`--dt_unit` (`years`; rationale: keeps Δt ∈ {0.25, 0.5, 1.0, …} so it is O(1) alongside
the other network inputs); `--covariates_csv` (default `<data_root>/clinical_covariates.csv`);
`--no_covariates`; `--age_mode` (`baseline` | `per_visit`); `--slo_mask_size`
(default 0 = off; deprecated, feeds only the SLO-DMM path).

Output layout per fold:

```
<out_dir>/
├── edges_global.pt    # pos_xy (50176, 2) float32 physical mm; edge_index (2, 602112) int64
├── meta_global.pt     # dataset metadata incl. normalisation stats (schema in §2.8)
├── train/sample_000000.pt … (one file per training eye; each = that eye's window list)
└── val/sample_000000.pt …   (one file per validation eye)
```

**Runtime-selectable k (2026-08-14 evening).** The stored `edge_index` is only
the *default* graph: `--neighbors` is live at load time. `_2Dataset_preloaded`
derives the file's k exactly (E/N; in-degree ≡ k for a `knn_graph(loop=False)`
build) and, when the requested k differs, rebuilds the graph with the
precompute's own `build_pos_xy_iso` + `build_edges` (edges are a pure function
of (grid, k) — no data enters), verified bit-identical to the per-k artifacts
at k=12 and k=24. One folder therefore serves every k;
`dataset_provenance.json` records `edges_per_node` + `edges_source`. Prefer
shell-closing k (4, 8, 12, 20, 24, 28, 36, …) — at a shell-splitting k the
tie-break among equidistant index-space neighbours is
torch_cluster-version dependent. **Shell closure holds only for interior nodes**,
though: on 49×1024 at k = 12, 4 276 of the 50 176 nodes (8.5 %) do not carry the
interior stencil *(measured on the shipped `edges_global.pt`)* — half of them the
outermost ring, where the shell is simply truncated, and half the ring one step in,
where it genuinely splits. Node (row 1, col 500) is the demonstration: with (−2, 0)
off-grid its twelfth neighbour is drawn from the equidistant d² = 5 set
{(−1, ±2), (1, ±2), (2, ±1)} and comes out as (−1, +2). So the shipped k = 12 graph
already contains equidistant tie-breaks, and exact edge reproducibility still assumes
the same torch_cluster version.

## 2.2 State assembly (`load_visit`)

Per visit ([tools/precompute_graphs_ga.py](../../tools/precompute_graphs_ga.py),
`load_visit`):

```
mask   = (PIL(mask_oct.png) > 127).astype(float32)          # binary {0, 1}
layers = np.load(layers_oct.npz.npy).astype(float32)        # (rows, cols, 10), axial-px depths
state  = concat([mask[..., None], layers], -1).transpose(2, 0, 1)   # (C=11, rows, cols)
```

Channel order `[mask, layer_0 … layer_9]` is fixed here and recorded in
`meta["channel_names"]`; everything downstream depends on it.

## 2.3 Center-crop / zero-pad to (49, 1024) — no resampling

`center_crop_or_pad` ([tools/precompute_graphs_ga.py](../../tools/precompute_graphs_ga.py)):
per axis, symmetric center crop when the native size is ≥ the target, symmetric zero-pad
when it is smaller. Both genuinely occur: 149/553 visits are row-padded (<49 rows) and
115/553 col-padded *(measured)*. Rationales and their honest limits:

- **Crop, never resample**: keeps the *stored* pixel spacing identical by construction —
  a single `SPACING_MM` constant — and introduces no interpolation artefacts. The
  upstream resampling onto that constant is *assumed* exact; NOTES F10.14 flags an
  unverified ~2 % deviation across the cohort's own transform files, pending DICOM
  confirmation, and it would touch every mm² number (§9.4).
- **Zero fill is "no signal" physically** — mask 0 = not atrophic, a layer depth of 0 is
  the top of the volume, above the retina — **but not for the network.** The fill pixels
  are included in the train-split normalisation statistics, because crop/pad runs before
  `compute_norm_params`, so in z-space the layer-channel fill sits at **−2.35 … −2.94 σ**
  *(measured, split-2 stats)*: an extreme value that is regressed at full weight unless
  `--exclude_pad_nodes` is set (§6.1). Nor is 0 out of band as a sentinel — cohort layer
  values span −14 … 499 (§1.2). Open item: NOTES F10.1.
- **The crop is NOT lossless with respect to the lesions** — the historical rationale
  ("the pathology lies within the central ~3 mm, the discarded periphery is clinically
  irrelevant") is **false as measured** (CODE_REVIEW_2026-08-14.md §F3, all 553 visits;
  that file was deleted 2026-08-17 in `294b1d5` — `git show 6e7f9fe:CODE_REVIEW_2026-08-14.md`):
  the window cuts real lesion area in **27.3 %** of visits (>5 % of the lesion in
  6.0 %, max 25.7 %), and **31.1 %** of cropped lesions touch the crop border — growth
  across that border is *censored* with no missingness flag, so training supervises on
  censored truth and the @360d change-region metrics under-measure progression for
  roughly 1 in 5 visits (this also skews comparability with Mai's whole-FOV numbers).
  The 49×1024 window was nevertheless **kept deliberately** (2026-08-14 decision;
  measured trade-off table for 55×1280 / 61×1536 / lesion-centered alternatives was
  recorded in `handoff.md`, removed in the same 2026-08-17 prune and recoverable with
  `git show 6e7f9fe:handoff.md` — larger windows trade truncation for up to 35 % pad and ~1.9× node
  count, and ~19 % border-touch is irreducible because those lesions touch the scan's
  own edge). Mitigations live downstream: the pad-aware border/interior change-region
  Dice split, the pad-masked `_anat` column (§7.1), `ts_layer_rmse_valid`, and the
  `--exclude_pad_nodes` loss option (§6.1). The thesis Methods must state the
  censoring, not the old "clinically irrelevant periphery" premise.

The resulting fixed physical window is Lx × Ly = 49·0.12118 × 1024·0.00568
≈ **5.938 mm × 5.816 mm** (the precompute defines L = N · spacing).

## 2.4 Per-channel normalisation (train-split statistics only)

`compute_norm_params` / `apply_norm` ([tools/precompute_graphs_ga.py](../../tools/precompute_graphs_ga.py)):
statistics are computed **only over the training-split visits** of the fold (no
val→train leakage), per channel, then applied to every visit before windowing. They are
computed over the *already cropped and padded* training states, so the pad zeros enter
the per-channel mean and std (§2.3).

- `zscore` (canonical): `x' = (x − mean_c)/std_c`, std floored at 1e-12→1.0.
- `minmax` (ablation variant): `x' = 2(x − lo_c)/(hi_c − lo_c) − 1` ∈ [−1, 1].

**The binary mask is z-scored like every other channel.** For split 2 that maps
background 0 → −0.602 and foreground 1 → +1.660; the 0.5 binarisation threshold maps to
+0.529 in normalised space. Consequences that shaped the framework: the z-scored mask
has a hard step at the lesion edge (the source of the DMM monitor NaN, §3.7), and every
evaluation threshold must be mapped into normalised space consistently (§7.1). Stats are
stored in `meta["norm_params"]`. The runtime never denormalises through a shared helper:
evaluation maps the 0.5 binarisation threshold into normalised space instead
(`train.py` `_mask_threshold_in_normalised_space`), and the DMM loader
(`dmm_dataloading.py` `_denorm_mask_channel`) and the moved-mesh helper
(`moving_mesh_helper.py` `_state_to_native_mask`) invert the mask channel inline.
`tools/precompute_graphs_ga.py` `denormalize` is an offline convenience that nothing in
the pipeline imports (ARCHITECTURE.md §0, §8).

## 2.5 Graph construction: physical positions, index-space edges

Two coordinate systems coexist deliberately
([tools/precompute_graphs_ga.py](../../tools/precompute_graphs_ga.py): `build_pos_xy`,
`build_pos_xy_iso`, `build_edges`, and the graph-build block of `main`):

- **Node positions** `pos_xy` (50 176 × 2, float32): physical millimetres, from
  `meshgrid(linspace(0, Lx, 49), linspace(0, Ly, 1024))`. These feed the GNN's
  positional features, the DMM/mesh machinery, and ItpNet. (Known nuance: `linspace`
  gives a node pitch of Lx/(Nx−1) = 0.123705 mm, +2.08 % vs the acquisition spacing —
  logged, immaterial.)
- **Edges** `edge_index`: k-nearest-neighbours with k = 12 via `torch_cluster.knn_graph`
  (no self-loops), built **on integer index coordinates** `(row_idx, col_idx)` — i.e. a
  grid where both axes have pitch 1 — *not* on physical mm. Result: 602 112 directed
  edges, ≈33 % to same-row neighbours, ≈50 % one row away, ≈17 % two rows away — a
  proper 2-D stencil. At interior nodes it is exactly the complete d² ≤ 4 index-space
  disc, a radius-2 diamond: the four direct neighbours (±1 row, ±1 column), the four
  diagonals (±1 row × ±1 column), and the four two-step axial neighbours (±2 rows at
  the same column, ±2 columns in the same row) — 12 in total *(measured on the
  shipped `edges_global.pt`)*. So one hop
  reaches ±2 rows **and** ±2 columns — ±0.25 mm × ±0.011 mm in the node pitch
  `data.pos` carries (±0.24 mm × ±0.011 mm at the acquisition spacing; the two
  conventions differ by 2 % on rows and 0.1 % on columns, so no reach argument
  below turns on the choice).

**Why index space (the 2026-05-23 anisotropy fix).** The grid is ≈21:1 anisotropic on either
convention — the acquisition-spacing ratio 0.12118/0.00568 = 21.335:1, and the 21.758:1 node
pitch that `knn_graph` would actually search in physical mm. k-NN in physical mm therefore finds all 12 nearest neighbours
*within a single B-scan row* — measured 100 % in-row, 0 % cross-row — which collapses
message passing to 1-D along the 1024-axis: no information can cross rows at any network
depth. Building edges on index coordinates restores 2-D connectivity while `pos_xy`
keeps honest physical geometry. Every precompute predating this fix was invalidated and
regenerated. (The *same* defect later resurfaced independently inside the moved-mesh
branch, which rebuilds its own edges — §5.2 / §9.)

**Reach, not connectivity (measured 2026-09-02).** Being isotropic in grid steps, that
stencil is ~21× anisotropic in millimetres: along a B-scan it reaches ±2 columns
(±0.011 mm) per hop, ±4 columns over the locked 2 message-passing layers, against a
measured GA front advance of a median ~12 columns per 180-day visit (q3 17, p90 23).
Neither depth nor a larger index-space k closes that gap (both measured null). So the
2026-05-23 fix restored *connectivity* and left *physical reach* untouched. The locked
v2 model therefore **does not use
this `edge_index` for its uniform branch**:
[GraphPDE/baselines/anisognn.py](../baselines/anisognn.py) substitutes the dilated
stencil at forward time (rows ±1 × columns {0, ±7, ±14, ±21}, 20 neighbours, ≈±0.12 mm on
both axes) — §0.2, SOLVER_FINAL_RUNS.md §9.12b–e. `edges_global.pt` remains the graph of
the `--backbone gnn` comparison arm; the moved branch builds its own k-NN on the warped
mesh (§5.2).

## 2.6 Windows, Δt, and covariates

Per eye, visits are sorted by day-in-study and consecutive pairs become windows
([tools/precompute_graphs_ga.py](../../tools/precompute_graphs_ga.py), the per-split
window loop of `main`): window *i* is
(state at visit *i*, state at visit *i+1*, Δt between them). K = 1 is hard-coded — one
window is one transition, not a multi-step tensor. Saved keys per window:

| key | shape | meaning |
|---|---|---|
| `x` | (11, 50176, 1) f32 | state at the start visit, layout (C, N_pts, K) |
| `y` | (11, 50176, 1) f32 | state at the next visit (the target) |
| `dt` | scalar f32 | (t_{i+1} − t_i)/365.0 — Δt in **years** (e.g. 180 d → 0.4932) |
| `dt_days` | float | the raw day gap |
| `t0_steps` | int | window index within the eye |
| `eye_id` | str | e.g. `'GX511402_OS'` |
| `covariates` | (2,) f32 | `[age_z, sex]` |
| `age_raw`, `sex_raw` | float | unnormalised (imputed-if-missing) values |
| `slo_mask` | (256, 256) f32 | binary SLO-registered mask of the *start* state; only when `--slo_mask_size > 0` (deprecated DMM-side field) |

Covariate encoding ([tools/precompute_graphs_ga.py](../../tools/precompute_graphs_ga.py):
`load_patient_covariates`, `build_eye_covariates`, `compute_age_stats`,
`eye_covariate_info`, and the covariate block of `main`):
sex is 0.0 = female / 1.0 = male (missing → the training male fraction); age is z-scored
with **train-eye statistics** (one sample per eye; a patient's two eyes deliberately
both count). `--age_mode baseline` freezes each eye's baseline age across all its
windows; `--age_mode per_visit` (the canonical variant since the `agevisit` precomputes)
gives each window the age at *its own start visit* (baseline + elapsed years), with the
z-stats widened over all training **window-start** (eye, visit) ages — one per window, so
each training eye's final visit is excluded (split 2: n = 378, mean 77.653, std 7.220
*(measured)*) — so the age covariate advances along a rollout. This leaks nothing (future
age is determined by the input Δt). One inconsistency to footnote in Methods: the
elapsed-years conversion uses 365.25 d/y while `dt` uses 365.0 (≤ 0.07 % effect,
deliberately unfixed because changing it would desync every built precompute's baked ages
— NOTES F10.5).

## 2.7 The SLO mask field (deprecated, DMM-side only)

When `--slo_mask_size > 0`, each window additionally carries a square binary mask
sampled from the SLO-frame `mask_global.png`. The **current** implementation
(`load_slo_mask_oct_fov`, corrected 2026-08-09) inverse-warps through the recorded
`T_mask` affine — square target pixel → fractional OCT en-face coordinate → `T_mask` →
nearest-sample `mask_global`. The affine itself was verified cohort-wide, reproducing
`mask_oct` at native resolution with median IoU 1.000 and minimum 0.99957 on all 553
visits; the ported square-resampling implementation was then verified bit-identical to
that reference on 30/30 visits plus native-grid spot checks — it was not itself re-scored
against `mask_oct` on all 553. The **historical** implementation (used to build every `*_slo256` precompute
currently on disk) cropped with the `transform_oct_fov` corners with a swapped axis
binding and without `T_mask`'s shift/rescale terms — mis-registered (mean IoU 0.588,
median 0.64).
The on-disk fields were deliberately not regenerated: this field feeds only the
deprecated SLO-DMM training path (§3.6); the solver reads the GA mask from channel 0 of
the state instead.

## 2.8 `meta_global.pt` schema

`Lx, Ly, grid_size=(1, 49, 1024), Nx, Ny, C=11, in_channels=11, K=1, N_eyes=75,
N_samples, spacing_mm, channel_names, norm_params {method, mean, std | vmin, vmax},
split_idx, dt_unit='years', time_encoding='delta_adapted', n_covariates,
cov_norm_params {age_mean, age_std, sex_mean, names, age_mode}, slo_mask_size`, plus two
keys written by newer builds that **no on-disk precompute carries** *(measured, all 16
dirs)*: `neighbors` — the k that `edges_global.pt` was built with, stamped since
2026-08-14, a dormant cross-check against the artifact's own E/N (§2.1) — and
`slo_mask_registration` — `'T_mask'` when `slo_mask_size > 0` and `None` otherwise,
stamped since 2026-08-13. (The registration *fix* is 2026-08-09; the meta *stamp* is
later.)

## 2.9 The runtime dataset (`_2Dataset_preloaded`, [utils/utils.py](../../utils/utils.py))

The solver ([GraphPDE/train.py](../../GraphPDE/train.py)) loads precomputes through one
Dataset class that holds everything in RAM as tensors, indexed by *sequence* (= eye), not
by window. The DMM loaders (§3.6) do **not**: they read the window files directly into a
flat mask stack with their own split loaders, and construct `_2Dataset_preloaded` only to
borrow its `PDE2DMeta`, whose `grid_size` and `in_channels` they then overwrite.

- **Loading.** For each eye file, every window's `x`/`y` of shape (C, N, K) is flattened
  to **(N, C·K)** by `permute(1, 0, 2).reshape(N, C*K)` — the **channel-major /
  time-minor** layout used throughout the codebase: for one node, features are ordered
  `[c0k0, c0k1, …, c1k0, …]`; at K = 1 this is simply the 11 channel values per node.
  Storage per eye: `X[sid]`, `Y[sid]` (W, N, C·K); `t0s[sid]`, `dts[sid]` (W,);
  `covariates[sid]` (W, n_cov) ([utils/utils.py](../../utils/utils.py), the
  sequence-loading block of `__init__`, which also carries the runtime k-rebuild).
- **Guard**: a precompute with `dt_unit != 'years'` is refused at load — three places in
  the runtime hard-assume years (the day-rounding, the 360-day metric horizon, the
  pushforward budget), so a `days` precompute would silently mis-scale by 365×
  ([utils/utils.py](../../utils/utils.py), the `dt_unit` guard in `__init__`).
- **One sample = one PyG `Data`** (`_make_data_from_idx`,
  [utils/utils.py](../../utils/utils.py)) with:
  - `x`, `y` (N, C·K) — normalised state and target;
  - `pos` (N, 3) = **[Δt, x_mm, y_mm]**: column 0 is the window's Δt broadcast to all
    nodes; columns 1–2 the physical node coordinates;
  - `edge_index` — the shared precomputed index-space k-NN graph (identical for every
    window, since the grid is fixed). This is what the `--backbone gnn` comparison arm
    and the moved branch consume; the locked v2 uniform branch replaces it at forward
    time with the dilated stencil (§2.5, §0.2);
  - `dt` — the Δt as a 1-element tensor, so PyG batching yields shape (B,) and the GNN
    can do per-graph residual scaling `data.dt[batch]`;
  - `covariates` — shape (1, n_cov), batching to (B, n_cov), broadcast per node
    downstream via `data.covariates[data.batch]`;
  - `seq_id`, `t0` — bookkeeping for pushforward chaining.
- **Access API**: `ds[i]` → a *random* window of eye i; `ds[(i, t0)]` → a specific
  window; `get_next_window(sid, t0+K)` → the chronologically next window or `None`
  (drives both the pushforward chain and the evaluation rollout).
- **Time-budget machinery** (the dataset side of unrolling, §6.2):
  `compute_time_table()` precomputes, for every (eye, start-window):
  *reachable_days* (the maximum cumulative Δt-days from chaining consecutive windows to
  the sequence end) and *first_gap* (the Δt-days of the start window itself). Setting
  `ds.min_budget_days = B` then restricts random sampling to start windows with
  `reachable_days ≥ B AND first_gap ≤ B` (windows that can actually realise a B-day
  horizon), with a documented fallback to unrestricted sampling for eyes with no valid
  start. `steps_to_budget(sid, t0, B)` returns the **undershoot** unroll depth: the
  largest number of no-grad unroll steps n such that the cumulative days over the
  n+1 chained windows (the n rolled steps plus the final supervised one) stay ≤ B —
  the chain never overshoots the budget ([utils/utils.py](../../utils/utils.py),
  `compute_time_table` / `steps_to_budget`).
- `PDE2DMeta` is the small metadata holder (Lx/Ly, grid_size, in_channels); it hard-rejects
  any `time_encoding` other than `delta_adapted` — the runtime is GA-only since the
  2026-07-05 purge of the legacy SWE paths ([utils/utils.py](../../utils/utils.py),
  `class PDE2DMeta`).

**What the solver ultimately sees per training sample** (bridging summary): a graph of
50 176 nodes; per node an 11-dimensional normalised state vector (mask + 10 layer
depths) plus its physical (x, y) position; per graph a scalar Δt in years and a 2-vector
`[age_z, sex]`; and as target the same 11 channels at the next visit. The **edge set
depends on the arm**. The precomputed k = 12 index-space k-NN of `edges_global.pt` is
what the v1 comparison arm (`--backbone gnn`) consumes. Since the LOCKED CONFIGURATION v2
decision (2026-09-03) the canonical uniform branch is `--backbone anisognn`, which
replaces that `edge_index` at forward time with the dilated stencil rows ±1 × columns
{0, ±7, ±14, ±21} (20 neighbours, ≈±0.12 mm reach on both axes) under `--gnn_aggr mean`
(67 147 params). The moved branch uses neither: `create_moved_graph` rebuilds its own
k-NN on the warped coordinates, in isotropic index space under `--iso_edges` (§5.2).

# 3. The DMM (Data-free Mesh Mover)

## 3.1 Role and character

The DMM is the mesh-adaptation component inherited from MM-PDE (Hu et al. 2024). Its
job: given the *current GA mask*, produce a smooth deformation of the computational
grid that concentrates nodes where the field has structure — for GA, on the lesion
boundary, which is where all the change happens. It is:

- **Data-free**: it is not trained on data labels at all. It learns to satisfy a
  *Monge–Ampère equidistribution equation* defined by a monitor function of its input —
  a physics/optimisation objective, not supervised regression. Equidistribution is
  classical moving-mesh theory (Huang & Russell 2011 — §3.4, §10); §3.4 gives the loss
  as implemented.
- **Unsupervised with respect to the prediction target**: its only input is the GA
  segmentation of the *current* state (an input available at inference); it never sees
  future masks. This is why it may legitimately be trained on the *whole cohort's*
  masks, including validation eyes, without leaking labels (§3.5).
- **Pretrained separately and frozen** during solver training: loaded from a
  checkpoint, `requires_grad=False`, excluded from the optimizer. The solver treats it
  as a fixed geometric preprocessor.

## 3.2 Architecture: a DeepONet with a CNN branch

The DMM ([GraphPDE/mesh/dmm_model.py](../../GraphPDE/mesh/dmm_model.py)) is a DeepONet-style
operator network (Lu, Jin, Pang, Zhang & Karniadakis, *Learning nonlinear operators via
DeepONet based on the universal approximation theorem of operators*, Nature Machine
Intelligence 3(3):218–229, 2021, arXiv:1910.03193), in the form adapted by Hu, Wang & Ma
(ICLR 2024, arXiv:2312.05583), producing a scalar **mesh potential** φ(ξ₁, ξ₂)
conditioned on the input mask:

- **Branch** (`ConvNet`): encodes the mask image `(B, 1, Nx, Ny)` into a fixed
  **512-d latent**. The architecture is selectable (`--branch_layers`), and *every
  variant emits the same 512-d latent* so the rest of the network is identical across
  a branch sweep (isolating "does branch capacity matter?"):

  The two parameter columns are the **branch alone** and the **whole DMM** at trunk
  `[2, 32, 512]` + base head `[1024, 512, 1]` *(measured by construction)*; the
  whole-DMM figures are the ones older text quoted as if they were branch sizes.

  | name | structure | branch params (256² / 49×1024) | whole DMM @ base head | notes |
  |---|---|---|---|---|
  | `conv7` | Conv2d 1→8 (5×5, s2) → 8→16 (5×5) → 16→8 (5×5) → 8→1 (5×5, s2), residual add of the first 8-ch activation onto the third conv, tanh; flatten → Linear(flat, 1024) → Linear(1024, 512) | 4.73 M / 3.94 M | 5 269 266 @256² | the upstream-git CNN; grid-locked (flatten sized from the training grid) |
  | `conv8` | four 5×5 convs 1→8→16→8→5, no stride, residual add; flatten → Linear(5·Nx·Ny, 1024) → Linear(1024, 512) | 336 M / 257 M | 258 M @49×1024 | paper App. H.1; enormous off small grids — never used for GA |
  | `stride3` | four 5×5 convs 1→8→16→8→1, 3 stride-2 steps; flatten → Linear → 1024 → 512 | 1.58 M / 1.45 M | 2.12 M @256² | compact |
  | `stride4` | as `stride3` with a 4th stride-2 step | 0.79 M (both grids) | 1.34 M | compact |
  | `pool` | Conv 1→16 (s2) → 16→32 (s2) → 32→64 (s2), `AdaptiveAvgPool2d(4)` → Linear(64·16, 512) | 589 312 (both grids) | 1 131 617 | **grid-agnostic** (works at any input size) — the canonical GA branch |
  | `pool_tiny` | as `pool` with last conv → 16 channels | 157 648 (both grids) | 699 953 | |

  The canonical GA DMM is `pool` with the **deepened** head `[1024, 512, 512, 1]`:
  **1 394 273 parameters** in total (§3.9).

- **Trunk** (`DenseNet`): a tanh MLP on the *continuous* query coordinate
  ξ = (ξ₁, ξ₂) ∈ [0, 1]² — canonical widths `[2, 32, 512]` (the native winner keeps this
  trunk unchanged: a second trunk layer is worth +0.10…+0.14 `edge_gain` — but only at
  width ≥ 64, and at the canonical width 32 it *costs* −0.05 — and it adds ≤ 0.014 on top
  of a deepened head, so only one deepening was taken, §3.9). Because the trunk is a continuous function of ξ, the
  mesh can be queried **at any resolution** — this is what lets a mesh trained on one
  grid be evaluated on another.
- **Head** (`out_nn`, also a `DenseNet`): the branch latent (repeated per query point)
  and the trunk features are **concatenated** (so `out_layer[0] = 512 + trunk[-1]`,
  canonically 1024) and mapped through the head to the scalar φ per query point.
  (This concat-head is a departure from the classic DeepONet dot-product; it is the
  upstream MM-PDE design.) Canonical head `[1024, 512, 1]`; the native winner uses the
  deepened `[1024, 512, 512, 1]`.

**From potential to mesh.** The moved mesh is the gradient map of the potential:

```
x(ξ) = ξ + ∇φ(ξ)        (each component via autograd through the trunk)
```

computed everywhere by `torch.autograd.grad(φ, [ξ₁, ξ₂])`. Training constrains φ so
this map equidistributes the monitor (§3.4); a well-behaved φ gives an invertible,
fold-free deformation.

## 3.3 The monitor function (and the binary-mask problem)

The monitor M(x) encodes "where resolution is needed"
([GraphPDE/mesh/dmm_utils.py](../../GraphPDE/mesh/dmm_utils.py): `diff_x`/`diff_y` →
`_blur_mask_channel_for_monitor` → `compute_grad_norm` → `monitor`):

```
M = 1 + log1p( ‖∇u‖ / (α_scale · α + ε) ),      α ≈ the field mean of ‖∇u‖
```

- **‖∇u‖** is the per-pixel gradient magnitude from forward finite differences
  (`diff_x`/`diff_y`, last row/column replicated), scaled by ×(Nx−1) and ×(Ny−1) to
  derivatives in the unit-square **computational** coordinate ξ — that is Lx (resp. Ly)
  times the physical gradient, but the common factor cancels through α and the domain is
  square to 2.1 %, so the two axes' *relative* weighting comes out right. This is what is
  essential on the anisotropic grid, where the two axes have very different
  index-to-physical scales.
- **α** normalises by the field's own mean gradient, making M scale-free;
  `α_scale` (canonical 0.1) sets how aggressively gradient regions are weighted. (In code
  α = Σ‖∇u‖ / ((Nx−1)(Ny−1)) — a unit-square quadrature of ‖∇u‖ rather than an exact
  field mean, so it runs +2.2 % high on 49×1024.)
- **log1p compression** (canonical ON): bounds the peak/bulk ratio of M so that the
  Monge–Ampère target stays *achievable* at the razor-sharp GA lesion ring. The
  linear-ratio ablation (`NOLOG1P`) produced unusable meshes with fold-overs.
- **The Gaussian mask blur — the fix that made GA-DMM training possible at all.**
  A binary mask has a step at the lesion edge; its finite-difference gradient is
  enormous (monitor peaked at ~1800) and drives the second-derivative chain through φ
  to NaN within a few iterations — the failure of the very first GA-DMM run.
  `_blur_mask_channel_for_monitor` convolves the mask with a normalised separable 2-D
  Gaussian (σ = `--monitor_mask_sigma` px, kernel ≈ 6σ wide) **before** the
  derivatives feed the monitor. Crucially, only the monitor sees the blurred field —
  **the branch CNN always trains on the raw binary mask**, so no train/inference
  input skew exists (verified in code, both regimes). σ = 0 (blur off) collapsed the mesh
  to a near-uniform translation on the **SLO** grid (`SLO_NOSIGMA`, 2026-05-12; that run
  tree was deleted 2026-08-17). On the **native** grid σ = 0 trains cleanly for 500 epochs
  but yields a near-identity mesh — `GA_NAT_S0` `edge_gain` **1.2412** against **1.6184**
  at σ = 2 on the otherwise identical config — so the blur is load-bearing, not cosmetic,
  on both grids, though on the native grid it buys adaptation rather than preventing
  divergence. Canonical σ: 4 px on the 256² SLO grid (historical);
  **1 px on the native grid** (§3.9). Padding for the blur is zeros (historical
  default); a flag-gated `replicate` option exists because zero padding manufactures
  a phantom gradient ridge where a lesion touches the crop border (audit C4;
  affects ~33 % of native masks at σ=1) — but it was **never run in training**: all 55
  native runs used `zeros`, and the replicate fix was applied on the scoring side only,
  because flipping the training default would move every logged mesh score. An A/B is one
  run.

## 3.4 The loss: Monge–Ampère equidistribution + boundary + convexity

One training iteration evaluates three terms
([GraphPDE/mesh/dmm_utils.py](../../GraphPDE/mesh/dmm_utils.py): `compute_boundary_loss`
and `compute_interior_loss`, which also returns `loss_convex`), combined inside
`train_MA_res` as `W0·loss_in + W1·loss_bound + W2·loss_convex`
(canonical **W = 1 / 1000 / 1**):

- **Interior (Monge–Ampère) loss** at importance-sampled collocation points ξ:
  compute φ and its full second-derivative stack (φ_ξξ, φ_ξη, φ_ηξ, φ_ηη) by nested
  autograd, then penalise the equidistribution residual

  ```
  LHS = M(ξ + ∇φ) · det(I + Hess φ)          # monitor at the MOVED point × Jacobian determinant
  RHS = Σ M / ((Nx−1)(Ny−1))                  # unit-square quadrature of M; ≈ its field mean
  loss_in = MSE( LHS / RHS , 1 )
  ```

  The monitor at the moved point is obtained by bilinearly interpolating the
  precomputed gradient fields (u_x, u_y) at (ξ + ∇φ) and re-evaluating M there. In
  words: cells should shrink (det < 1) exactly where the monitor is large, such that
  *monitor × cell volume is constant* — the classical equidistribution principle
  (Huang & Russell, *Adaptive Moving Mesh Methods*, Springer 2011, Applied Mathematical
  Sciences vol. 174). Note the denominator sums over all Nx·Ny pixels but divides by
  (Nx−1)(Ny−1), so on 49×1024 the target runs **+2.2 %** above the true field mean: an
  exactly equidistributed mesh leaves a residual of ≈4.6e−4 rather than 0. Identical
  across every run, so it shifts no comparison.
- **Boundary loss (soft)**: at collocation points on the four domain edges, penalise
  the *normal* derivative of φ (∂φ/∂ξ₁ = 0 on the ξ₁-edges, ∂φ/∂ξ₂ = 0 on the
  ξ₂-edges), so boundary points do not move off the boundary. This is the **only**
  boundary mode: the historical `hard` constraint wrapper was removed after audit C2
  found it mis-specified (it double-counted the identity, pinning the boundary to
  2·ξ, and was read four different ways across the tooling); `dmm.py` now rejects
  `bound_constraint != 'soft'` including on resume.
- **Convexity loss**: `mean( min(0, 1+φ_ξξ)² + min(0, 1+φ_ηη)² )` — penalises
  negative diagonal Hessian entries (a fold-over precursor). At the canonical GA
  configuration this term is **essentially dormant** (measured ≈ 0 through training);
  mesh validity is actually enforced at *selection* time by the zero-tangling gate
  (§3.8), not by this penalty.

## 3.5 Training procedure

Entry: [GraphPDE/mesh/dmm.py](../../GraphPDE/mesh/dmm.py) → `train_MA_res`
([GraphPDE/mesh/dmm_utils.py](../../GraphPDE/mesh/dmm_utils.py)).

- **Training pool.** With the canonical `--train_split all`, the loader concatenates
  every split's windows: **478 masks = every window's start-state mask** (≈6.4 per
  eye — deliberately all visits, not one baseline per eye; the wording "baseline
  masks" in older notes was a misnomer). Rationale for full-cohort training: the DMM
  is unsupervised w.r.t. the target, and an earlier train-split-only DMM measurably
  under-generalised (mean mesh displacement 0.16 on seen vs 0.10 on unseen lesions,
  visibly rougher held-out meshes) *and* broke fold comparability, since one fold's
  DMM matched its own training distribution better than the other folds'.
- **Importance sampling** (`sample_train_data`): per iteration, draw
  `batch_size_u_adam` masks (canonical 5) with replacement; per mask, throw 40× the
  needed number of uniform candidate points, evaluate the monitor at each (bilinear
  `grid_sample`), and draw `batch_size_x_adam` points (canonical 1000) *without*
  replacement from `p = (1−f)·p_importance + f·p_uniform` with
  f = `--monitor_uniform_frac` (canonical 0.1). On the square SLO grid the f = 0 leg
  appeared to collapse the mesh toward a global affine map that only equidistributes the
  thin lesion ring. **On the native grid it is a null**: `GA_NAT_NOUNIF` reads
  `edge_gain` 1.6120 head-16 against the 3-seed 500-epoch base 1.6115 (seed sd 0.0133)
  and 2.2595 spread-16 against 2.2403 — +0.001 and +0.019, far inside the search's
  ~0.10 single-leg resolution. The starvation premise was measured and does **not** hold
  here: log1p caps the monitor at M ≈ 9.8 at the canonical σ = 1, so pure importance
  sampling can never be more than ~10× peaked — probing the shipped sampler at f = 0 over
  all 100 val masks, the nonzero-gradient ring is 24.4 % of pixels, takes 51.9 % of the
  sampled points, and the bulk still keeps **48.1 %**. There is little for a uniform mixer
  to repair. f = 0.1 is kept because it is the validated value and costs
  nothing, not because it is load-bearing (§3.9). (Implementation caveat, kept by decision —
  audit B5: the importance step is chunked in `sub_nu = 4` groups sized `⌊nu/4⌋`, so
  at the canonical bu = 5 the remainder field — 1 of 5, 20 % of collocation points —
  always falls through to plain uniform sampling. Identical across all runs and all
  rankings preserved, but it means the `NOUNIF` leg actually compared ≈28 % vs 20 %
  uniform points — **a true importance-only condition has never been run**.)
- **Iterations per epoch**: `train_sample_grid · n_masks / (bx · bu)` (canonical
  5000·478/(1000·5) = 478 iterations).
- **Optimizer**: Adam, lr 2e-4, weight decay 1e-5, `MultiStepLR` γ = 0.2 at
  milestones {333, 467} for the canonical 500-epoch native runs. (Epoch count was
  swept: mesh quality rose monotonically 150 → 250 → 500 epochs and converged at 500.)
- **Per-epoch evaluation**: the legacy `evaluate()` (monitor-weighted cell-area
  spread on both the training and eval pools — with a documented flaw on non-square
  grids, §3.8), plus every 5 epochs the config-independent `MeshScorer` report.
- **Checkpointing**: periodic `checkpoint_epoch*.pt` (every `--save_interval`),
  `checkpoint_latest.pt` refreshed at every save event (periodic cadence, new-best,
  final epoch — so mid-run it can lag up to save_interval − 1 epochs), and
  `checkpoint_best.pt` by `--best_metric`:
  `auto` = the historical rule on square grids (min held-out `test_std`, or min
  interior loss when the eval split is inside the training pool) and **max
  `edge_gain` subject to zero tangled cells on non-square grids** — where the legacy
  area metric is meaningless. Checkpoints carry model + optimizer + scheduler state,
  the full args, data provenance, and the entire loss/metric history; runs are
  resumable at epoch granularity with `args.json` re-used as defaults (only
  explicitly-passed flags override).
- **Optional RF/BFGS refinement** (`--rf`, off in the canonical native recipe): after
  Adam, freeze everything except the *last linear layer* of the head, treat the
  penultimate activations as fixed random features, precompute their derivative
  matrices, and solve for the last-layer weights with torchmin BFGS/Newton-CG on the
  same MA + boundary + convexity objective (plus a `convex_rel·(Σw²)²` regulariser).
  This is the paper's §5.3 refinement; it was explored on SWE/early GA and is not
  part of the canonical GA recipe.
- **Reproducibility**: seeded (`random`/`numpy`/`torch`/CUDA), cuDNN deterministic;
  run directory name encodes the hyperparameters (seed, branch, α_scale, epochs,
  batch sizes, LRs, loss weights, RF settings, source fold `sp<N>`, training scope
  `ts<spec>`, and `ms<source>` for non-SLO mask sources); `args.json` +
  `dataset_provenance.json` (fold, splits, mask counts) are written at run start.

## 3.6 Input regimes: the SLO 256² era and the native-grid path

The DMM consumes a **single-channel binary GA mask**; *which* mask, on *which grid*,
is the `--mask_source` axis ([GraphPDE/mesh/dmm_dataloading.py](../../GraphPDE/mesh/dmm_dataloading.py)):

- **`slo` (historical — the code path is still present and selectable, but as of
  2026-08-17 no SLO run remains in the repository: all 103 SLO-era runs were deleted
  from `mesh/experiments/` and their rows dropped from `dmm_results.csv`, which now
  carries the 55 native runs only; the SLO numbers survive in git history at
  `6e7f9fe`):**
  each window's `slo_mask` — the SLO-frame GA segmentation registered to the OCT
  field of view and sampled to a square 256² grid. This was the path that *first*
  made the GA-DMM train: the square, isotropic grid dissolved a stack of
  asymmetry-specific workarounds. The trunk was then queried at the OCT lateral grid
  (49, 1024) at solver inference — the two-grids-one-continuous-mesh property. Two
  permanent caveats: (a) all on-disk `slo_mask` fields predate the registration fix
  and are mis-registered (mean IoU 0.588, median 0.64 — internally consistent for those runs,
  since training and scoring used the same supplied mask, but thesis DMM claims
  should scope to the native path); (b) at solver rollout steps t > 0 this path
  required upsampling the model's own 49×1024 predicted mask to 256² (a "surrogate"),
  an out-of-distribution round-trip that has since been eliminated.
- **`oct` (CURRENT — the solver path):** channel 0 of each window's `x` on the
  **native (49, 1024) OCT grid**, denormalised (exact inverse of the precompute's
  z-score/minmax) and thresholded > 0.5 back to binary. Works on any GA precompute
  (no `slo_mask` field needed); asserts `channel_names[0] == 'mask'` rather than
  trusting the channel-order invariant silently. The historical belief that "the DMM
  cannot train on the native anisotropic grid" turned out to be a misattribution:
  the original failure was the *unblurred* mask's step gradients (fixed by the
  monitor blur, which landed a week before the 256² pivot), not the anisotropy.
  With a plain isotropic blur the native path trains cleanly, and the 55-run native
  hyperparameter search reaches good, valid meshes (0 tangled cells at every scored
  epoch on all three winner seeds) while removing the 49×1024 → 256² → 49×1024
  round-trip and the rollout surrogate entirely. **Native and SLO mesh scores are not
  comparable** — `edge_gain` is pool-dependent, the two grids have different mask pools,
  `score_dmm_runs.py` keeps them in separate groups, and no common-pool re-score exists —
  so no "native beats SLO" claim is made here; the supported argument for the native path
  is architectural. `train.py` **requires** `mask_source == 'oct'` on the DMM checkpoint it
  loads (checked *before* `load_state_dict`, because a `pool` branch's weights are
  grid-independent and would otherwise load silently onto the wrong field).
- Guard rails: resuming across mask sources is refused (read from the checkpoint's
  own saved args, not the run dir); grid-locked branches (`conv7`/`conv8`/`stride*`)
  on an `oct` run trigger a loud warning (only `pool`/`pool_tiny` are grid-agnostic);
  non-square grids trigger a warning that the legacy `Train/Test std` numbers are
  not reportable (§3.8).

## 3.7 Refinements that made the DMM work (summary)

In the order they were needed; details and dates in §9:

1. **Monitor Gaussian blur** (σ px on the mask channel, monitor-side only) — fixed
   the NaN blow-up of the first, unblurred run. σ = 0 today does not diverge; it gives a
   near-identity mesh (`GA_NAT_S0` `edge_gain` 1.2412, against 1.6184 at σ = 2 on the
   otherwise identical config and 2.0317 for the canonical winner).
2. **log1p monitor compression** — bounds the peak/bulk monitor ratio; the linear
   ablation is unusable.
3. **Uniform sampling admixture** (f = 0.1) — on the square SLO grid, reducing it to
   f = 0 appeared to collapse the mesh toward a near-affine map. On the native grid
   `GA_NAT_NOUNIF` is a **null** (+0.001 head-16, +0.019 spread-16), and the starvation
   premise behind it does not hold there (§3.5), so f = 0.1 is kept as the validated,
   free default rather than as a load-bearing fix. (Due to the sampler's chunk remainder
   that leg still drew ~20 % uniform points, so a true importance-only condition has
   never been run — §3.5.)
4. **Memory chunking** of the bilinear interpolation and batched `grid_sample`
   rewrites — the GA grid's 50 176 points OOM'd the original per-point code.
5. **The square-SLO pivot, then the native return** — the 256² SLO representation
   made the first working GA-DMM; the native path later proved the anisotropy was
   never the blocker and is now canonical (it removes the surrogate round-trip).
6. **Full-cohort training** (`--train_split all`) — a train-split-only DMM
   under-generalised to unseen lesions and confounded the cross-fold comparison.
7. **Branch compaction** — on the square **SLO** grid the `conv7` DMM overfit (largest
   train→val equidistribution gap, +73.9 % against `pool`'s +31.9 %, and ≈4.8× `pool`'s
   seed sd: ±0.041 vs ±0.0085). On the **native** grid held-out quality is never
   measured — every run is `--train_split all`, so all scoring is in-sample — and the
   five-branch sweep is a **null**: spread 0.047 across a 25× branch-parameter range at a
   seed sd of 0.0133, i.e. the range of five single-seed draws, with the ranking unstable
   across scoring pools. `pool` is therefore canonical for grid-agnosticism and size, not
   for a measured quality edge (§3.2 here; DMM_GA_DESIGN.md §3.2 "Reason 3").
8. **Deepening φ's head** (native search) — the largest *architectural* lever (head range
   0.23 > trunk 0.19 > branch 0.05): the deeper `out_nn = [1024, 512, 512, 1]` head is
   worth +0.17 at σ = 2 on its own, and a further +0.24 when paired with the sharper
   monitor blur σ = 1 (against +0.003 for that same blur at the shallow head), so σ and
   head depth must be tuned together — neither alone reproduces the winner. Note σ is the
   largest *single-knob* effect in the search overall (the deep-head σ range spans ≈0.60
   against the head axis' ≈0.24); the head is the largest lever among the **architecture**
   axes only.
9. **Refuted ideas (kept as negative results, deliberately not in the code path):**
   a physically-matched *anisotropic* blur kernel (σ_col ≈ 21.8·σ_row — the intuitive
   "correction" for the grid imbalance) gave no adaptation gain (p = 0.95) and folded
   the mesh intermittently; a det-Jacobian barrier penalty made tangling monotonically
   *worse*; the `hard` boundary wrapper was mis-specified and removed.

## 3.8 Mesh-quality evaluation

Two generations of metrics coexist deliberately:

- **Legacy `evaluate()`** (unchanged so every historical number stays valid): renders
  the mesh on the full grid, computes per-cell "areas" as d₁·d₂/2 (the product of
  the two cell diagonals) weighted by the run's own monitor at the cell centre, and
  reports mean/std/min-max of that product. Three structural flaws make it unusable
  for *ranking* meshes: the diagonal-product area is exact only for square cells (on
  49×1024 it overstates area ~10.7× and is ~99.8 % blind to the long axis); it is
  sign-blind, so a folded mesh can score well; and it weights by each run's *own*
  monitor, so cross-config rankings measure the metric, not the mesh.
- **`dmm_metrics.py` (config-independent, the ranking metrics)** — all reference
  fields depend only on the mask, parameterised in computational (ξ) units so the
  same setting means the same physical bandwidth on any grid:
  - `signed_cell_areas`: exact signed shoelace area per mesh quad → **`tangled`** =
    number of cells with area ≤ 0 (fold-overs). The binding validity check.
  - **`edge_gain`**: mean of a fixed lesion-*boundary band field* (boundary indicator
    blurred to a band of half-width 0.02 of the domain, normalised to grid-mean 1)
    sampled at the moved node positions. The identity mesh scores exactly 1.000; a
    mesh that concentrates nodes on the lesion boundary scores > 1. The primary
    ranking metric of the native search.
  - **`cov_ref`**: equidistribution coefficient of variation (std/mean of
    reference-monitor-weighted cell areas) against **one fixed reference monitor**
    (Huang & Russell, *Adaptive Moving Mesh Methods*, Springer 2011), so rows of a sweep
    are comparable.
  - **`min_det_sample`**: continuum min det(I + Hess φ) over random ξ by autograd —
    resolution-free invertibility margin, complementing the discrete `tangled` count.
    Uses a dedicated, per-report-reseeded RNG so that *enabling metrics cannot
    perturb the training trajectory* (the global stream feeds the training sampler).
  - `MeshScorer` caches the reference fields once and spread-selects its mask pool
    across eyes (`linspace`, deterministic — the pool is stacked eye-major, so a
    naive head-slice would score ~4 eyes wearing an n = 16 label; audit B4).
  - **Reference-field padding** (`ref_pad`, F4 fix 2026-08-14): the reference
    band/monitor blurs default to **`replicate`** padding — zero padding
    manufactured a phantom monitor ridge at the crop border ~90 % as strong as a
    true lesion edge, sitting inside the very fields that gate `checkpoint_best`
    and rank sweeps. `zeros` reproduces every pre-fix number bit-identically;
    `ref_pad` is stamped into the scorer cfg, the score_dmm_runs CSV rows, and
    threaded as `--mesh_ref_pad` / `REF_PAD` — **pre- and post-fix mesh scores
    are not comparable; the stamp says which regime a row used.** (Measured
    materiality on the *selection* metric is small — the band's grid-mean-1
    normalisation absorbs most of it, worst single mask 0.023 — the fix is about
    removing a structural bias, not moving rankings.)
  - The **selection rule of the native search**: hard-gate `tangled == 0` (and
    det_min > 0) on every mask, rank survivors by mean `edge_gain`; the interior
    loss is reported but never ranked on (it is σ-confounded and anti-correlated
    with validity).
  - The cross-run ranking itself was produced **post hoc** by
    [score_dmm_runs.py](../../GraphPDE/mesh/demos%20&%20explanations/score_dmm_runs.py):
    one process re-scores every run's checkpoints against **one** fixed mask pool
    and **one** fixed reference — the property that makes cross-run ranking valid
    at all (a per-run reference drifts, which is exactly how the legacy metric
    confounded rankings).

## 3.9 The canonical DMM configuration and checkpoint

The solver-bound checkpoint is the winner of the 55-run native search
(**`GA_NAT_O512x2_S1`**, seed 42; three seeds run; the solver launcher resolves
`.../GA_NAT_O512x2_S1/s42_*/ckpt/checkpoint_latest.pt`). Full recipe — the defaults of
[jobs/train_dmm.slurm](../../jobs/train_dmm.slurm); the run itself was submitted by
[launch_dmm_search.sh](../../jobs/launch_dmm_search.sh) `STAGE=n6` (s42) / `n7` (s7,
s2024), whose *base* export block differs from the winner on two axes (σ 2.0, head
`[1024, 512, 1]`) and is overridden per leg. NB ε 1e-10 and det_pts 20 000 come from that
launcher's base exports: `train_dmm.slurm` forwards but does not default them, and
`dmm.py`'s own defaults are 0.0 and 5000.

| axis | value |
|---|---|
| mask source / grid | `oct` — native (49, 1024), full cohort (`train_split all`, 478 masks) |
| branch | `pool` (grid-agnostic, 589 312 branch params) |
| trunk | `[2, 32, 512]` |
| head | **`[1024, 512, 512, 1]`** (the deepened winner; base was `[1024, 512, 1]`) |
| monitor | **σ = 1.0 px** blur, α_scale 0.1, ε 1e-10, uniform_frac 0.1, log1p ON, zeros pad |
| loss weights | W0/W1/W2 = 1 / 1000 / 1, soft boundary |
| sampling | grid 5000, bx 1000 points × bu 5 masks per iteration |
| schedule | Adam lr 2e-4, wd 1e-5, 500 epochs, γ = 0.2 at {333, 467}; RF off |
| selection | `best_metric auto` → max edge_gain gated on tangled = 0 **and det_min > 0** (the `valid` flag of `dmm_metrics`); scoring fixed at band_ξ 0.02, ref_σ_ξ 0.02, ref α_scale 0.1, det_pts 20 000 |
| total size | **1 394 273 parameters** (`pool` branch + trunk `[2, 32, 512]` + deep head) |

Notable search findings baked into this recipe: epochs 150→500 monotonically improve
adaptation (converged at 500); LR/γ/weight-decay are flat axes; σ interacts strongly with
head depth (σ = 1 was worth +0.003 at the shallow head but +0.24 at the deep head);
uniform_frac does not matter natively but is kept at the validated 0.1. **W1 = 1000 is
kept but unverified** — the W1 = 100 leg actually *wins* on raw `edge_gain` on both
scoring pools against its matched 250-epoch anchor (1.6071 vs 1.5780 head-16, +0.029;
2.3101 vs 2.2048 spread-16, +0.105) and was rejected solely on a lesion-specificity
placebo (self − other 0.3799 vs 0.3798) that was computed on the **biased 4-eye pool**
and has never been re-run on the eye-spread pool. See DMM_HPSEARCH_NATIVE.md §6.2 ("the
weakest link") and the open NOTES TODO of 2026-08-17.

# 4. Backbone I — the graph solver: GA-adapted MP-PDE GNN

> **One of two backbone chapters.** This one is in more depth than the others
> because it is the arm the project *built* rather than imported, and because
> several of its components (the decoder, the Δt conditioning, the K=1 rule) are
> framework-level and bind every other arm. It is not the privileged arm: the
> locked uniform branch is §4.3b's dilated stencil, implemented as a wrapper in
> §4b, and two arms from §4b match it. Read §4 and §4b as peers.

One class, [GraphPDE/gnn.py](../../GraphPDE/gnn.py) `MP_PDE_Solver_2D`, implements *both*
solver branches — the uniform branch and (in dual-branch mode) the moved/correction
branch — distinguished only by the `is_correction_branch` flag (§4.5). It is an
**encode–process–decode** message-passing network in the MP-PDE mould: an embedding
MLP lifts each node's state to a hidden vector, `hidden_layers` rounds of learned
message passing propagate information over the graph it is handed (the learned
analogue of a finite-difference stencil) — the **dilated stencil** under the v2 lock,
the k = 12 index-space k-NN in the v1 comparison arm (§4.3b) — and a decoder maps the
processed hidden state to a per-node residual that is Euler-integrated over Δt.

## 4.1 Inputs and the `variables` conditioning vector

Per forward pass on a PyG batch of B graphs × N = 50 176 nodes:

- **Node state** `u = data.x` — (B·N, C·K) = (B·N, 11) normalised channel values.
- **Positions** — `pos_x = pos[:,1]/Lx`, `pos_y = pos[:,2]/Ly` (normalised physical
  coordinates; `pos[:,0]` is the Δt column and is *not* used as a position).
- **`variables`** — the per-node conditioning vector, width
  `n_variables = 1 + n_covariates + d_embed`, concatenated in this order:
  1. `dt_per_node` = `data.dt[batch]` — the graph's Δt (years) broadcast to its nodes;
  2. `cov_per_node` = `data.covariates[batch]` — `[age_z, sex]` broadcast per node;
  3. `cond_per_node` = `data.layer_embed[batch]` — the LayerEncoder's global embedding
     (only when `d_embed > 0`; a missing embedding raises rather than silently
     degrading).

  Δt, covariates, and the surrogate embedding all enter through this **one channel**,
  and the same vector is injected at *three* places: the encoder input, every message,
  and every node update — so conditioning reaches all depths, not just the input.

## 4.2 Encoder (embedding MLP)

`node_input = cat(u, pos_x, pos_y, variables)` — width `C·K + 2 + n_variables` — through
`Linear(·, H) → norm → ReLU → Linear(H, H) → norm` (no trailing activation), with
H = `hidden_dim`. Upstream MP-PDE's Swish activations are ReLU here; the norm is
`nn.LayerNorm` at the canonical `--norm_type layer` (see §4.3, the Normalisation
bullet, for why that choice is load-bearing).

## 4.3 Message passing (`GNN_Layer_FS_2D`)

`hidden_layers` identical rounds of a `MessagePassing` layer; each round re-receives
the raw state, positions, and `variables`:

- **Message** (per directed edge j → i):
  `message_net_1(cat(x_i, x_j, u_i − u_j, Δpos_x, Δpos_y, variables_i)) → ReLU →
  message_net_2 → ReLU` — i.e. both endpoint *hidden* states, the **raw-state
  difference** `u_i − u_j` (the finite-difference flavour of MP-PDE), the normalised
  position offsets, and the receiver's conditioning. Width of the first Linear:
  `2H + C·K + 2 + n_variables`.

  *The two geometry features are the weakest inputs the message MLP receives, and
  that was diagnosed rather than assumed.* By default Δpos is domain-normalised
  (`pos / (Lx, Ly)` on a linspace grid), so an adjacent-node offset is 1/48 on the
  row axis against 1/1023 on the column axis — a **21× axis imbalance** — and both
  sit ~200–4600× below the LayerNorm'd hidden state at initialisation, leaving each
  layer close to direction-blind. Two zero-parameter probes test this; they are
  mutually exclusive, `gnn`/`anisognn` backbones only, both `_CRITICAL_ARGS` with
  **zero state_dict footprint**, and both refused at warm-start across the boundary:
  `--edge_feat_index` rescales Δpos by `(Nx−1, Ny−1)` to balanced ~integer index
  offsets (arm D1), `--edge_feat_none` zeroes both features while keeping the input
  width and parameter count (arm D1b). Measured at 5 folds against the locked GNN:
  D1 **+0.0023 ± 0.0043 SE (3/5)** — a null, *despite* the trained weights showing
  direction sensitivity 24× (rows) / 308× (columns) higher; D1b **−0.0099 ± 0.0056
  (1/5)**, under the 0.016 five-fold paired floor and therefore not established. So
  direction is *weakly used*, and per-direction discrimination in the message
  function is not the binding constraint on this task.
- **Aggregation** (`--gnn_aggr`, an ablation axis):
  - `mean` — the upstream MP-PDE choice, and the **v2 canonical value** (locked
    2026-09-03 in `jobs/train_solver.slurm`; 67 147 params);
  - `max` — morphological dilation; a travelling-front prior;
  - `mean_max` — the **argparse default** (`train.py`) and the v1 canonical value,
    kept so every pre-2026-09-03 run reproduces flag-for-flag; concatenates both,
    doubling the aggregated message width.

  The pre-2026-09 rationale for `mean_max` — that the update MLP would route locally
  between a diffusion-like and a front-like prior — is **refuted by measurement**.
  `max` alone reads **−0.148** against the locked config on fold 2
  (`MPPDE_aggrmax_f2` 0.3699 vs `MPPDE_final_dts_f2` 0.5178, four times the 0.036
  single-fold floor), and mean-only ties `mean_max` at 5 folds (**+0.0108 ± 0.0039
  SE**, under the 0.016 paired floor) at 11 % fewer parameters: the max stream is
  destructive alone and inert in concatenation, and `mean` carries all of the
  aggregation signal.

  *Checkpoint transfer:* switching to or from `mean_max` doubles the aggregated
  message width, so those checkpoints fail to load. `mean` and `max` share a width
  and load **shape-identically**, and nothing catches the swap at runtime —
  `gnn_aggr` is in `_CRITICAL_ARGS`, but that set is only read on the disabled
  `--resume` path and the `--warm_start_uniform` guards do not cover it, so a
  mean↔max cross-load is silent.
- **Update**: `update_net_1(cat(x, aggregated_message, variables)) → ReLU →
  update_net_2 → ReLU`, then an **unconditional residual** `x ← x + update`, then the
  layer norm.
- **Normalisation — a load-bearing choice.** `--norm_type layer` (default) uses
  `nn.LayerNorm` (Ba, Kiros & Hinton, *Layer Normalization*, arXiv:1607.06450, 2016
  — an arXiv preprint with no peer-reviewed venue; §10): each node normalised over
  its own feature vector, no running
  statistics, no coupling across nodes or graphs → **the operator is identical in
  train() and eval()**. This matters because the pushforward unrolls under `no_grad`
  in train mode (§6.2): BatchNorm there renormalises the drifted state with batch
  statistics — erasing the very perturbation the pushforward exists to teach
  robustness against — while poisoning the running statistics evaluation later uses;
  train and eval were measurably different operators (max output gap ≈ 8.6 on a probe)
  before the 2026-07-19 fix. Deliberately `nn.LayerNorm` and *not* PyG's `LayerNorm`:
  the call site passes no batch vector, and PyG's default `mode='graph'` would
  normalise the whole batch as one graph — reinstating exactly the cross-sample
  coupling the change removes. `--norm_type batch` restores the legacy behaviour for
  the ablation leg.

  A third mode exists as the **global-normalisation test**, built to ask whether the
  param-matched U-Net's advantage (§9) comes from its per-sample global statistic.
  `--norm_type graph` = `PerGraphNorm` ([gnn.py](../../GraphPDE/gnn.py)): mean and
  variance over *all* nodes and features of each individual graph, with a per-feature
  affine — the graph analogue of the U-Net's `GroupNorm(1, C)` (Wu & He 2018 —
  §4b.2, §10). It satisfies both
  invariants above (no running statistics, so `train() == eval()`; strictly
  per-sample, so *not* PyG's cross-sample `mode='graph'`), and its parameter
  footprint is identical to `nn.LayerNorm`'s — which is why the warm-start path
  guards `norm_type` explicitly against the checkpoint's saved args rather than
  relying on a shape check. Separately, `--norm_mlp_sites` inserts a norm between
  every Linear and its ReLU in the message and update MLPs (6 → 14 norm-fed
  nonlinearities at the locked 2 layers), the message-side norms taking a per-edge
  graph context. Both were measured and both are nulls: `graph` vs the locked GNN
  **+0.0146 ± 0.0074 SE (4/5 folds)**, site density on top of it **+0.0081 ± 0.0087
  (3/5)**, and the same swap on the v2 stencil backbone (arm E2n) **−0.0121** on fold
  2 — every one under its floor. `layer` stays canonical and the normalisation axis
  is closed.

Two pieces of robustness code with no upstream counterpart, both added during the
dual-branch bring-up: (a) the node→graph `batch` vector is *reconstructed* as
`arange(B).repeat_interleave(N)` from `data.dt.numel()`, because the cluster
container's PyG silently resets a manually-set `.batch` to zeros on a cross-GPU
`clone().to()` (which mis-indexed per-graph Δt as if there were one graph); (b) the
edge index is filtered to `[0, N)` immediately before propagation, because
`torch_cluster.knn_graph` can emit garbage indices on a degenerate moved mesh.

## 4.3b Uniform-graph construction: the anisotropic stencil (LOCKED v2, 2026-09-03)

Everything in §4.3 is agnostic to *which* graph the messages travel over, and since
2026-09-03 that graph is no longer the k-NN one. **The canonical uniform backbone is
`--backbone anisognn`** ([GraphPDE/baselines/anisognn.py](../../GraphPDE/baselines/anisognn.py)
`GAAnisoGNN`), which owns the unchanged `MP_PDE_Solver_2D` as `inner` and swaps only
`data.edge_index` at forward time on a zero-copy proxy batch. The class of §4.3–§4.5,
its parameters and every other module are untouched; the wrapper adds **no
parameters**.

- **Geometry.** Default `dilated`: rows ±1 × columns {0, ±7, ±14, ±21} — **20
  neighbours** per interior node, reaching **±0.121 mm** across rows and **±0.119 mm**
  along columns (acquisition spacing; ±0.124 mm × ±0.119 mm in the node pitch). On a
  ≈21:1 grid that is near-equal *physical* reach on both axes,
  where the k = 12 index-space k-NN of §2.5 is isotropic in grid steps and therefore
  ~21× anisotropic in millimetres. Knobs: `--aniso_stencil {dilated,multiscale}`,
  `--aniso_pitch 7`, `--aniso_taps 3`, `--aniso_rows 1` — all `_CRITICAL_ARGS`, with
  the geometry always emitted into the run-dir name and into
  `dataset_provenance.json` as `edges_source: aniso_stencil:<label>`.
- **`--neighbors` is inert here** and `train.py` *raises* if it differs from the
  precompute's k, rather than letting the run name claim a receptive field the
  operator never had.
- **Only the uniform branch is wrapped.** The moved branch runs on off-lattice DMM
  nodes where a lattice stencil is undefined, so it keeps its own k-NN on the warped
  mesh (§5.2), rebuilt per forward by `knn_graph` at k = `--neighbors` rather than
  read from `edges_global.pt`. The k = 12 index-space k-NN therefore remains the
  **data** graph, and what consumes it is `--backbone gnn`, the v1 comparison arm.

**Measured basis.** At 5 folds the stencil with mean-only aggregation
(`ANISOGNN_final_dilmean_f0..f4`) reads **0.5258 ± 0.0497** against the k-NN GNN's
**0.4515 ± 0.0429** — paired **+0.0743 ± 0.0083 SE, 5/5 folds** — and the
pre-committed seed-7 gate was discharged the same day (**+0.0736 ± 0.0162, 5/5**).
That is the largest effect in the project, at 0.89× the parameters. It leaves the
model statistically **indistinguishable** from the param-matched U-Net rather than
ahead of it (§9), and the fold-2 reach ladder puts the optimum at the default
±21 columns. The wrapped backbone is still MP-PDE (Brandstetter et al.,
*Message Passing Neural PDE Solvers*, ICLR 2022, arXiv:2202.03376); the stencil
geometry is this repo's own.

## 4.4 Decoder

A fixed 3-layer MLP: `Linear(H, H) → norm → ReLU → Linear(H, H) → norm → ReLU →
Linear(H, C·K)` with a **bare final layer** (the output is an unbounded signed
residual, so no norm/activation after it). Full rank: each of the 11 output channels
gets independent dynamics.

This decoder *replaced* (2026-07-05) the upstream-inherited Conv1d-over-hidden head.
Upstream, that conv head's job is to emit the `time_window` bundled future frames of
a scalar PDE; at this project's K = 1 it degenerated into a **rank-1 bottleneck** —
the conv stack collapsed the 128-d hidden vector to a *single scalar per node*, and a
`Linear(1, 11)` expanded that scalar to all 11 channels, making them perfectly
collinear — and additionally imposed a `hidden_dim ≥ 113` crash constraint. Verified
channel-rank 11 (was 1) after the replacement; all older checkpoints were invalidated.

**Zero-initialised decoder** (`zero_init_decoder`): the final layer's weight and bias
are zeroed so the branch starts at its residual identity — the uniform branch outputs
exactly `u` (persistence) at initialisation. On the **correction branch this must be
disabled whenever the α-gate is active** (train.py passes
`zero_init_decoder = not use_alpha_gate`): a zero decoder makes g ≡ 0 and α = 0 makes
∂L/∂θ_b ∝ α = 0, so the two zero-inits deadlock each other *exactly* — the moved
branch could never activate and "α → 0" would be an initialisation artefact rather
than the intended measurement. α alone supplies the zero-init — the ReZero construction
(Bachlechner, Majumder, Mao, Cottrell & McAuley, *ReZero is All You Need: Fast
Convergence at Large Depth*, UAI 2021, arXiv:2003.04887): a normally-initialised
sublayer scaled by a zero scalar.

## 4.5 Output: the Δt-conditioned Euler step and the branch flag

```
diff = decoder(h)                                  # (B·N, C·K)
--euler_dt_scale True (default, the historical MP-PDE operator):
  uniform branch    (is_correction_branch=False):  out = u + dt_per_node · diff   # full next state
  correction branch (is_correction_branch=True):   out = dt_per_node · diff       # pure delta
--euler_dt_scale False (the L6nodts ablation):
  uniform branch:  out = u + diff                  # Δt stays an INPUT feature only
  correction branch: out = diff
```

The uniform branch is a Δt-conditioned Euler residual operator
`u(t+Δt) = u(t) + Δt·f_θ(u, Δt)`; the moved branch returns only `Δt·g_θ` and is
interpolated + α-gated into the composition (§5.4). The placement of the Δt
multiplication is intentional and documented as an invariant (the composition depends
on which branch sees it). Two properties worth stating in the thesis: at Δt → 0 the
prediction collapses to persistence (the correct limit for arbitrarily close visits),
and the leading `u` term is a deliberate inductive prior, not just numerical
convenience — GA evolves slowly (persistence is strong) and monotonically (dead tissue
does not heal), so the network only has to learn a small growth correction.

**The residual is exposed separately, so the branch can be integrated as an ODE**
(2026-09-05). `forward()` is the Euler composition over a shared `_residual()`, and
`vector_field(data)` returns the residual f *before* that composition, so
`forward == u + Δt·vector_field` bit-exactly (asserted in the module self-test).
`--integrator {midpoint,heun,rk4}` / `--ode_substeps n` / `--ode_step_days D` then
wrap the backbone in [GraphPDE/baselines/odeint.py](../../GraphPDE/baselines/odeint.py)
`GAIntegrator`, a fixed-step explicit Runge–Kutta scheme over each graph's own Δt,
with the field **autonomous by default** (`--ode_autonomous True` feeds the
conditioning vector's Δt slot a zero — the valid-ODE reading). It adds no parameters
and is built *only* when one of those flags is off-default, so a flag-less run is
bit-identical; it is single-branch only and requires `--euler_dt_scale True`, both
refusals enforced in `train.py`. **Measured and null:** rk4 against the locked
one-step operator is **−0.0119 ± 0.0037 SE, 1/5 folds** at ~4.5× the wall-clock (and
a triple null on the fold-2 screens, including a leg with the Δt conditioning removed
entirely); the same wrapper over the FNO is +0.0062, also null. ⚠️ Change-region Dice
at the endpoint is *binarised and blind to the trajectory*, so none of this licenses
an "ODE" claim for the locked model. The solver-swap diagnostic that *would* license
one ran 2026-09-17 (SOLVER_FINAL_RUNS.md §9.17, 0 GPU-h) and confirms the refusal: the locked
model spans 0.0856 in Dice across euler n in {1,2,4} and rk4 n in {1,2}, 2.4x the
single-fold floor, with the Euler refinements growing rather than shrinking. The arm
trained with an autonomous RK4 field converges instead (four refined settings within
0.0044), so a continuous-time reading is licensed for that arm alone -- and it is a
5-fold null on Dice.
References as in the module docstring: Chen, Rubanova, Bettencourt & Duvenaud,
*Neural Ordinary Differential Equations*, NeurIPS 2018 (arXiv:1806.07366); Ott,
Katiyar, Hennig & Tiemann, *ResNet After All? Neural ODEs and Their Numerical
Solution*, ICLR 2021 (arXiv:2007.15386). **§4b.6 is the mechanism section** — Butcher
tableaus, the per-graph substep, the physical-step route, the autonomy flag, what is
held fixed across stages, and the scope guards.

**Why the ×Δt is an ablation axis at all** (`--euler_dt_scale`, added 2026-08-14
after the F6 measurement): on the *mask channel* the Euler form is a measured **pure
reparameterisation, not an inductive bias** — the residual target `(y−x)/Δt` at
flipped pixels is *exactly* ±z_gap/Δt (median = p95 = max at every Δt bucket), so f
must synthesise an internal ÷Δt that the outer ×Δt cancels, and the implied
continuous dynamics cross threshold at τ = 0.5·Δt for every flipping pixel at once
(f is not a queryable rate field). The flag drops **only** the output multiply (Δt
remains in `variables`; the +u persistence prior remains); True is verified
weight- and expression-identical to the historical operator, and False satisfies
`(out_True − u) = Δt·(out_False − u)` to fp32.

> **RESOLVED 2026-08-17 on the 5-fold CV: the ablation is a NULL, and ×Δt is
> re-locked to True.** The L6nodts ladder leg looked like a win on fold 2
> (+0.035), but that was a single-fold over-read — its own same-config replicate
> reads −0.006. Run across all five folds (`MPPDE_final_f*` vs
> `MPPDE_final_dts_f*`), dropping the scaling gives **+0.0134 ± 0.0059 SE, 4/5
> folds, t = 2.27 (df 4), p ≈ 0.09**, below the ~0.016 that the ±0.0127 replicate
> floor demands of a 5-fold paired mean (§7.4). Per the pre-registered rule the leg does
> **not** graduate: the canonical operator stays `u + Δt·f`, the one MP-PDE
> defines, which also preserves the Δt→0 persistence limit. **The "solver learns
> a rate field" framing is therefore dropped as a measured 5-fold negative
> result** — which is the reportable outcome, not a defeat: the ×Δt scaling is
> decoration on this task rather than an inductive bias, exactly as the F6
> reparameterisation measurement predicted.

`_CRITICAL_ARG`; run-dir token `nodts`; a warm-start across
the flag boundary is refused (the state_dict is identical across the two operators,
so only the checkpoint's saved args can catch the mismatch — §6.5).

## 4.6 The LayerEncoder surrogate ([GraphPDE/layer_encoder.py](../../GraphPDE/layer_encoder.py))

MP-PDE assumes the PDE's coefficients are known inputs; for GA no governing equation
is known. The LayerEncoder is the **learned stand-in for the PDE-coefficient
identity**: a small CNN compressing the 10 layer-boundary channels
`(B, 10, 49, 1024)` into a global embedding `z ∈ R^{d_embed}` that conditions the
dynamics through `variables` — telling the operator *what kind of retina* it is
evolving without forcing the GNN to parse layer geometry through message passing.

- **Extraction** (`extract_layers_from_batch`): `(B·N, C·K) → view(B, N, C, K)` →
  pick the latest timestep (k = −1) → **drop channel 0 (the mask)** → permute/reshape
  to `(B, C−1, Nx, Ny)`. The "channel 0 = mask" invariant is runtime-asserted in
  train.py.
- **Architecture**: Conv2d(10→32, 3×3) → Conv2d(32→64, 3×3, stride (1,2)) →
  Conv2d(64→64, 3×3, s2) → Conv2d(64→128, 3×3, s2), all bias-free, each followed by
  `GroupNorm(1, C)` + ReLU; then `AdaptiveAvgPool2d(1)` and `Linear(128, d_embed)`.
  The first stride is (1, 2) — long-axis only — because Nx = 49 is already tiny; the
  adaptive pool keeps the encoder input-size agnostic. `GroupNorm(1, ·)` is exactly
  LayerNorm for a conv tensor (no running stats → train ≡ eval, matching the GNN's
  norm rationale; the pre-2026-07-19 hardcoded BatchNorm2d had a measured train/eval
  output gap of 0.51). (Logged critique, closed as won't-fix 2026-09-16: the stride schedule
  corrects only ~2× of the ≈21:1 anisotropy of the image it consumes (acquisition
  spacing 21.335:1), leaving a ~14× receptive-field skew — 11 rows × 17 columns at the
  final layer, 1.361 mm × 0.0967 mm in the node pitch NOTES 2026-08-06 quoted, or
  1.333 mm × 0.0966 mm at the acquisition spacing. The
  skew stays as a caveat rather than a defect to repair: the width sweep below ran
  with it in place, so it measured the encoder as built and cannot separate "the
  surrogate does not help" from "this encoder geometry does not help" — but T5 is a
  null at every width and `d_embed = 0` stays canonical, so the stride fix was not
  pursued (NOTES 2026-08-06, closed 2026-09-16).)
- **Integration**: instantiated only when `--d_embed > 0` and C > 1; trained
  **jointly** with the GNN(s) in the same AdamW (own param group); **recomputed on
  every forward** from the current `data.x` — so during pushforward and rollout it
  sees the model's own *predicted* layers, a documented limitation; the embedding is
  computed once on the uniform batch and carried to the moved graph **not detached**,
  so gradients flow back to the encoder from both branches (whereas Δt and covariates
  are detached on carry-over — they are conditioning inputs, not learnable).
- **Status**: the canonical recipe runs `--d_embed 0` (encoder off), and that is now
  a **measured decision, not a default**. The width sweep ran at 5 folds on
  2026-08-28 (`MPPDE_final_d{32,64,128,256}_f0..f4`, 20 runs, seed 42, locked loss)
  and is thesis-bound row **T5**: 0.4499 / 0.4521 / 0.4506 / 0.4549 against
  `d_embed 0`'s 0.4515 — paired deltas **−0.0015 / +0.0006 / −0.0008 / +0.0034**,
  every one far under the 0.016 five-fold floor, with no monotonic trend across an
  8× width range and a mildly negative per-eye result at every width, for 30–55 % more
  compute (103 → 132–160 s/epoch). The learned surrogate contributes nothing
  detectable and stays off. Full readout:
  [SOLVER_FINAL_RUNS.md](SOLVER_FINAL_RUNS.md) §8.1. The anisotropy caveat above
  travels with that readout.

## 4.7 Summary of differences from upstream MP-PDE

| aspect | upstream (Brandstetter et al., 1-D) | GA adaptation |
|---|---|---|
| task shape | scalar 1-D PDE, temporal bundling K ∈ {20, 25, 50} | 11-channel 2-D clinical state, **K = 1** |
| time | absolute normalised t as a feature; fixed global grid step; output = last frame + cumulative-dt·diff over K frames | **per-graph irregular Δt (years)** as a feature *and* as the Euler multiplier; no shared t = 0 |
| equation identity | known coefficients (α, β, γ, BCs) appended to `variables` | none known → patient covariates + learned LayerEncoder embedding |
| positions | 1-D `pos_x/L` | 2-D `pos_x/Lx`, `pos_y/Ly` |
| graph | 1-D `radius_graph` / `knn_graph` on `pos` | **v2: dilated stencil** rows ±1 × cols {0, ±7, ±14, ±21}, swapped into `edge_index` at forward time by `--backbone anisognn` (20 neighbours, ≈±0.12 mm reach on both axes, parameters unchanged); v1: k = 12 index-space k-NN, which remains the *data* graph the `--backbone gnn` comparison arm consumes — the moved branch rebuilds its own (§4.3b) |
| aggregation | fixed `mean` | selectable; **v2 canonical `mean`** (locked 2026-09-03 in `jobs/train_solver.slurm`); `mean_max` = the v1 canonical and still the argparse default |
| activation / norm | Swish / `InstanceNorm(x, batch)` | ReLU / `nn.LayerNorm` (train ≡ eval); `--norm_type graph` = `PerGraphNorm` is a measured-null ablation option |
| decoder | per-K Conv1d heads (bundling machinery) | full-rank 3-layer MLP; zero-init option |
| branches | single model | `is_correction_branch` flag → uniform (u + Δt·f) vs correction (Δt·g) |
| robustness | trusts `data.batch` / `edge_index` | batch-vector reconstruction; edge-index validity filter |

**Capacity.** CLI defaults are `hidden_dim 128`; the **locked canonical capacity for
the final run batch is `hidden_layers 2 × hidden_dim 64`** — a hyperparameter
decision, not a code default, resting on a 14-leg old-era capacity grid in which
depth/width were flat down to 1×64 (the receptive-field story in §9) and **confirmed
new-era** by the Stage-F1b control. That control ran on fold 2 at
`euler_dt_scale False`, so its 2×64 comparator is the L6nodts leg — whose own
same-config replicate reads 0.5116, and whose locked euler-True counterpart on that
fold reads 0.5178: 6×128 = 0.5071 ± 0.0225 against 2×64's 0.5315 ± 0.0103, a −0.024
gap *inside* the 0.036 single-fold floor, i.e. no detectable capacity benefit rather
than a win for the smaller model (§9.4). The v2 stencil backbone inherits 2×64 with
no capacity control of its own.

Parameter counts at that capacity, read from the run logs *(measured)*:

| configuration | single-branch | dual-branch |
|---|---:|---:|
| **v2, locked** (`--backbone anisognn --gnn_aggr mean`) | **67 147** | **159 279** |
| v1 comparison arm (k = 12 k-NN, `--gnn_aggr mean_max`) | 75 339 | 175 663 |

The moved branch + ItpNet + α add ~92 k (v2) / ~100 k (v1). The ~8.2 k difference
between the two rows comes from the **aggregation**, not the stencil: mean halves the
update MLP's input width, and the wrapper adds nothing (stencil + `mean_max` also
logs 75 339; k-NN + `mean` also logs 67 147). (The 727 k / 1 777 494 figures quoted in
older notes are the retired 6×128 pilot stack.) Each run's log prints the
authoritative count for its config.

# 4b. Backbone II — the rest of the family

§4 describes one backbone. The same pipeline runs five others plus an integration
wrapper, reached through `train.py --backbone {gnn,unet,fno,gunet,anisognn,fen}` and
`--integrator`, with the model code in [GraphPDE/baselines/](../baselines/) — one module
per architecture. **This is the section that answers the thesis question of §0.2**, and
it carries the same weight as §4 for three concrete reasons:

- **The locked model is in here.** `anisognn` with `--gnn_aggr mean` — the unchanged
  message-passing network with its graph replaced at forward time — became the canonical
  uniform branch on 2026-09-03 (§4.3b). The largest measured effect in the project
  (+0.074 ± 0.008, 5/5 folds) is a change of *graph geometry* implemented in this folder.
- **The central architectural claim rests entirely on these arms.** §7.5 rows T7c–T7d —
  context and local detail are separable ingredients and both are required — is a
  contrast between an FNO, an FNO plus a 3×3 bypass, and a U-Net. No GNN arm can make it.
- **The strongest *mechanism* result is in here too.** The Finite Element Network's
  explicit transport term is worth +0.053 ± 0.007 at 5/5 folds and both seeds (§4b.7),
  and it recovers the near-term growth bin to the dilated stencil's own value — the same
  deficit found twice by unrelated means. (It is also the one comparison here that is
  **not** parameter-matched — the velocity head nearly doubles the model, 68,503 against
  the control's 34,785 — which §4b.7 and §7.5 state in full.)

The parameter matching (§4b.5) is what makes all of that a measurement rather than a
capacity comparison, and it answers the obvious objection in the one direction that
matters: the 44×-capacity U-Net *loses* to the parameter-matched one.

**A note on the word "countermodel".** Several arms here were pre-registered as
countermodels — models built to *fail*, so that a null would be informative — and the
run log keeps that vocabulary because it records what was expected at the time. Two of
them did not fail, one of them is now the thesis model, and a third posts the highest
mean recorded. Read "countermodel" historically, and read the family as the survey it
turned into.

## 4b.1 The dispatch, and what it controls for

`--backbone` is a thin lazy-import dispatch in `train.py`. A `--backbone gnn` run at the
default integrator never imports `baselines/` at all, so the F3/F4 comparison arms are
untouched **by construction**; the canonical v2 recipe does import it, because the stencil
wrapper lives there.

The folder holds **architecture only**. Loss, curriculum, optimiser, budget, evaluation,
model selection, seeds and run bookkeeping all come from the shared pipeline, and a
baseline module must not carry training knobs of its own. The alternative — a second
pipeline per baseline — would un-control the comparison and recreate this repository's
most documented bug class, two copies of one computation drifting apart (§9.2).

**Scoping refusals, and what they mean for the reading** (`train.py`): `unet`, `fno`,
`gunet` and `fen` are refused with `--moving_mesh True`, with `--d_embed > 0`, with
`--norm_type graph`, and with the GNN-only message/norm flags (`--edge_feat_index`,
`--edge_feat_none`, `--norm_mlp_sites`) — in each case because the flag would be inert
and the run-directory name would then claim a knob the operator never had. Two
consequences must travel with any dense-arm result: these four arms are **single-branch
and LayerEncoder-free by construction**, so the U-Net arm is a like-for-like of the
*single-branch* model and not of the dual one; and `anisognn` is refused none of them,
because it wraps the GNN and every GNN flag reaches the wrapped model.

**Identity guards.** `backbone`, the four `aniso_*` geometry knobs, the integration set
(`integrator`, `ode_substeps`, `ode_step_days`, `ode_autonomous`) and the six `fen_*`
knobs are all `_CRITICAL_ARGS`. Most of them — the backbone identity, the stencil
geometry, every integration setting and the two FEN pitches — change the forward operator
while leaving every tensor shape intact, so a strict `state_dict` load **cannot** catch
them; `--warm_start_uniform` therefore compares the checkpoint's *recorded args* and
refuses a mismatch. (`--ode_checkpoint` is deliberately *not* critical: it is a memory
strategy and changes nothing the model computes.) Both wrappers give their
keys an `inner.` prefix, which the warm-start strips one level at a time (an integrator
over the stencil over the GNN nests two). The run-directory name carries the backbone and
its off-default geometry, and `dataset_provenance.json` records the edge source, so an
arm is identifiable from a directory listing (§6.5).

## 4b.2 The contract every backbone satisfies

Verified against the pipeline and restated here because it is what makes the family a
controlled comparison rather than a collection of models:

- **Construction.** A backbone takes the pde meta, `time_window = K = 1`,
  `in_channels = C = 11` and `n_covariates`. The two wrappers are the exception:
  `GAAnisoGNN(inner, …)` and `GAIntegrator(inner, …)` are handed an already-built model.
- **`forward(data)`** consumes the PyG batch and returns the full next state
  `(B·N, C·K)`; `edge_index` may be ignored; `B` is derived as `data.dt.numel()`.
- **The node↔grid map is a silent-failure invariant.** The flat feature axis is
  channel-major/time-minor and the node axis is row-major over (49, 1024), so the *only*
  valid mapping to an image is `x.view(B, N, C, K).permute(…)` → `(B, C, 49, 1024)` and
  its inverse. A plain `.reshape` has the right shape and scrambles the channels without
  raising. §2.9 documents the flat layout; the three dense backbones invert it on every
  forward.
- **Conditioning as input channels.** The dense arms receive **16 channels**: the 11
  state channels, Δt broadcast as a constant plane, the 2 covariates likewise, and two
  normalised coordinate ramps (`linspace(0, 1)` per axis, registered non-persistent so
  they stay out of the `state_dict`). This mirrors §4.1's `variables` vector, and the
  construction is **byte-identical across `GAUNet`, `GAFNO` and `GAGraphUNet`** — which
  is precisely what licenses reading an FNO-vs-U-Net difference as an operator contrast.
  The coordinate planes are the CoordConv device (Liu, Lehman, Molino, Petroski Such,
  Frank, Sergeev & Yosinski, *An Intriguing Failing of Convolutional Neural Networks and
  the CoordConv Solution*, NeurIPS 2018, arXiv:1807.03247).
- **Operator parity.** Every backbone emits `u + Δt·f` with the residual head
  **zero-initialised**, so each starts at exact persistence — the `zero_init_decoder`
  precedent of §4.4 made a family-wide contract. `--euler_dt_scale` has the same meaning
  everywhere (the FEN is the one exception and refuses `False`; see §4b.7).
- **Norm parity.** No normalisation carrying batch statistics: `GroupNorm(1, C)` in
  `unet.py`/`gunet.py` (Wu & He, *Group Normalization*, ECCV 2018, arXiv:1803.08494), no
  norm layer at all in `fno.py` and `fen.py`. This is §4.3's fix-D invariant applied to
  the family — the pushforward unrolls under `no_grad` in `train()` mode, so running
  statistics would make train and eval different operators. `anisognn` is the one module
  that owns no norm of its own: being a wrapper it inherits `--norm_type`, where `layer`
  and `graph` are statistics-free but `batch` — the GNN family's own legacy ablation — is
  reachable and carries the parity caveat.
- **`vector_field(data)`** returns the residual f *before* the Euler composition, such
  that `forward(data) == data.x + Δt·vector_field(data)` bit-exactly (same elementwise
  op order). Each module computes both from one shared body — `_residual` in `gnn.py`,
  `_residual2d` in the dense arms, `_proxy` in `anisognn.py`, `rate` in `fen.py` — so the
  two cannot drift. This is what §4b.6 integrates.
- **torch-only, no new dependencies** (a CLAUDE.md hard rule).

## 4b.3 The dense countermodels: U-Net, FNO, and the localized-kernel hybrid

**`GAUNet`** ([baselines/unet.py](../baselines/unet.py)) — a plain Δt-conditioned 2-D
U-Net (Ronneberger, Fischer & Brox, *U-Net: Convolutional Networks for Biomedical Image
Segmentation*, MICCAI 2015, arXiv:1505.04597, doi:10.1007/978-3-319-24574-4_28). It is
the standard strong surrogate in the PDE-surrogate literature (Gupta & Brandstetter,
*Towards Multi-spatiotemporal-scale Generalized PDE Modeling*, TMLR 2023,
arXiv:2209.15616) and it has a GA-field precedent — a 2-D U-Net predicting future GA
growth, on fundus autofluorescence rather than OCT (Salvi et al., *Deep Learning to
Predict the Future Growth of Geographic Atrophy from Fundus Autofluorescence*,
Ophthalmology Science 2025, 5(2):100635). Both make it the countermodel that matters
most here.

- Each stage is two 3×3 convolutions, each followed by `GroupNorm(1, C)` + ReLU; nine
  such blocks (input stage, four down, four up) give **18 norm-fed conv sites** — the
  density arm D2 of §4.3 exists to ask whether that density, rather than the norm's
  globality, is what the GNN lacks.
- **The pooling schedule is anisotropic on purpose**: `(1,2), (1,2), (2,2), (2,2)`, i.e.
  49×1024 → 49×512 → 49×256 → 24×128 → 12×64. Rows are pooled 4×, columns 16×, so the
  21.3:1 grid aspect (§2.5) is reduced to ≈5:1 and **not** removed. It is deliberately
  not tuned further: a countermodel whose geometry has been optimised against this
  dataset is a weaker control, not a stronger one. (The same reasoning, and the same
  partial correction, appears in the LayerEncoder's stride schedule, §4.6.)
- Zero-initialised 1×1 head. Base width is `--hidden_dim`: **5 → 83,081 params** (arm B2,
  the parameter-matched comparison) and **32 → 3,354,347** (arm B1, the capacity
  control).

**`GAFNO`** ([baselines/fno.py](../baselines/fno.py)) — a canonical FNO2d (Li, Kovachki,
Azizzadenesheli, Liu, Bhattacharya, Stuart & Anandkumar, *Fourier Neural Operator for
Parametric Partial Differential Equations*, ICLR 2021, arXiv:2010.08895). It is in the
family to separate two things the U-Net conflates: *global support* and *multiscale local
detail*.

- A 1×1 lifting convolution, then **four blocks** of `spectral conv + pointwise bypass`
  with GELU between them (not after the last), then `1×1 → 32 channels → GELU →` a
  zero-initialised `1×1` projection to the C output channels.
- The spectral convolution is `rfft2`, a per-mode complex channel mixing on the two
  retained low-frequency row blocks (`[:m1]` and `[-m1:]`) × the retained column block
  (`[:m2]`), then `irfft2`. Weights are stored as real `(cin, cout, m1, m2, 2)` tensors
  viewed as complex.
- **Non-periodicity is handled by padding.** The FFT assumes a periodic domain and this
  domain is a *crop*, not a physical boundary (§2.3) — so the field is zero-padded by
  ~1/8 per axis before the transform (49 → 56 rows, 1024 → 1152 columns) and cropped
  after the spectral blocks.
- **Equal mode counts are the anisotropy argument, not an oversight.** `--fno_modes`
  defaults to `14 14`. The physical domain is near-square (5.938 × 5.816 mm), so equal
  mode counts per axis give near-equal *physical* bandwidth per axis — the property the
  index-space k-NN did not have (§4.3b). Retained indices are 0…13 on each axis, so the
  finest retained wavelength is ≈0.52 mm across rows and ≈0.50 mm along columns, i.e.
  lesion scale. (SOLVER_FINAL_RUNS §9.8 states the same cutoffs under the other
  convention, dividing the padded extent by the mode *count* rather than the highest
  retained index, which gives 0.485/0.467 mm; the convention does not change the
  argument, and the discrepancy is flagged rather than resolved here.) The choice is
  **unablated** — all 15 FNO runs carry `fno_modes = 14 14`.
- Width 5 → **79,160 params**. No norm layers at all, so train/eval parity is trivial.

**The localized-kernel hybrid (arm B4c)** — `--fno_local_kernel 3` widens each block's
pointwise bypass from 1×1 to 3×3 (+800 parameters, **79,960**); the default `1`
reconstructs the plain FNO bit-identically. This is the localized-kernel neural operator
(Liu-Schiaffini, Berner, Bonev, Kurth, Azizzadenesheli & Anandkumar, *Neural Operators
with Localized Integral and Differential Kernels*, ICML 2024, arXiv:2402.16845), and it
is the **minimal** global+local construction: the spectral path keeps global support and
the bypass gains exactly one ring of local detail. That minimality is what makes its
result interpretable (§7.5).

## 4b.4 The graph countermodels and the two floors

**`GAGraphUNet`** ([baselines/gunet.py](../baselines/gunet.py), arm E1) is `GAUNet` with
every 3×3 convolution replaced by one message-passing layer on the 8-connected grid
graph — same pyramid, same channel schedule, same 18 `GroupNorm(1, C)` + ReLU sites, same
nearest-neighbour upsampling and skips, same zero-init 1×1 head, same conditioning
channels. Only the operator inside each block differs, so **E1-vs-U-Net isolates the
operator class at a fixed pyramid, and E1-vs-GNN isolates the pyramid at a fixed operator
class**. Message passing is computed by grid shifts — one shared, offset-conditioned
message layer (a 1×1 convolution + ReLU over `[h_i, h_j, −dr, −dc]`) evaluated at each of
the eight offsets, with out-of-grid neighbours masked out of the mean — which is
numerically `MessagePassing(aggr='mean')` on the in-range 8-neighbour graph, and uses no
scatter atomics. Width 7 → **72,713 params**.

Two things must travel with any E1 statement. First, an offset-conditioned *shared*
message MLP is the standard message-passing construction (Gilmer, Schoenholz, Riley,
Vinyals & Dahl, *Neural Message Passing for Quantum Chemistry*, ICML 2017,
arXiv:1704.01212) and is **not a strict superset of a 3×3 convolution** — per-tap weights
would need one matrix per offset — so the "is a convolution just a one-hop GNN?" question
is probed in the direction the construction allows, not settled. Second, the name is
reused: this is *not* Gao & Ji's Graph U-Nets (*Graph U-Nets*, ICML 2019,
arXiv:1905.05178), which pools a general graph by learned node scoring; here the pyramid
is an ordinary image pyramid and only the operator inside each block is a graph one.

**The two floors need no baseline module** — both are `gnn.py`'s own class with the
message-passing stack shortened:

- **Per-pixel floor (arm B3)**, `--hidden_layers 0`: the layer list is empty and the
  forward skips propagation entirely, so each node's next state is a function of its own
  state and its conditioning only — no spatial context whatsoever. **14,795 params.**
- **One-hop floor**, `--hidden_layers 1` at width 64: exactly one ring of neighbour
  context. **45,067 params.**

Together with the locked 2-layer model they form the locality ladder whose result (§7.5,
row T8) is the sharpest discontinuity in the project.

**A precision caveat that belongs with this family, not with the GNN.** Every convolution
arm (`unet`, `fno` including B4c, `gunet`) runs its convolutions at PyTorch's default
TF32 setting on the cluster's Ampere-class cards, while the GNN's `Linear` path is
fp32. The repo leaves the default in place and records it rather than matching
precision across the classes. The measured consequence is that on a conv arm the same graph's output shifts by
~1.4e-3 relative with the sub-batch size, so the "bit-deterministic" claims for these
modules are CPU / TF32-off claims. §6.4's determinism bullet covers the seeding and the
cuDNN flags; it does not make the arms precision-matched.

## 4b.5 Parameter matching: what is matched to what

The protocol is taken from the two source papers: MM-PDE runs a **parameter-matched
"bigger GNN"** control so that gains cannot be attributed to capacity (Hu, Wang & Ma,
*Better Neural PDE Solvers Through Data-Free Mesh Movers*, ICLR 2024, arXiv:2312.05583),
and MP-PDE trains its baselines with its **own training recipe** (Brandstetter, Worrall &
Welling, *Message Passing Neural PDE Solvers*, ICLR 2022, arXiv:2202.03376). Stage F5
applies both: identical folds, loss, curriculum, optimiser, budget, evaluation and
selection, with capacity matched as closely as each architecture's width granularity
allows.

Counts are read from each run's own log *(measured)*; ratios are against the **locked v2
model**, since that is the thesis model — note that most published ratios in the results
documents are against the v1 comparison arm (75,339) and therefore read ~11 % lower.

| arm | how it is built | params | × 67,147 | what it isolates |
|---|---|---:|---:|---|
| **locked v2 stencil GNN** | `--backbone anisognn --gnn_aggr mean` | **67,147** | 1.00 | — (the reference) |
| v1 k-NN GNN | `--backbone gnn --gnn_aggr mean_max` | 75,339 | 1.12 | edge geometry + aggregation, against the lock |
| T-FEN | `--backbone fen --hidden_dim 96` | 68,503 | 1.02 | a FEM operator with an explicit transport term |
| FEN, free-form only | `… --fen_transport False` | **34,785** | 0.52 | the transport control — **the one row here that is not matched to its own comparison arm**: it is the T-FEN with the 33,718-param velocity head deleted, so the +0.053 transport effect is measured across a 1.97× parameter gap (§4b.7) |
| graph U-Net | `--backbone gunet --hidden_dim 7` | 72,713 | 1.08 | the multiscale pyramid at a graph operator |
| FNO | `--backbone fno --hidden_dim 5` | 79,160 | 1.18 | global spectral support, no local detail |
| FNO + 3×3 bypass (B4c) | `… --fno_local_kernel 3` | 79,960 | 1.19 | global support **plus** minimal local detail |
| U-Net w5 | `--backbone unet --hidden_dim 5` | 83,081 | 1.24 | multiscale local detail (the primary countermodel) |
| U-Net w32 | `--backbone unet --hidden_dim 32` | 3,354,347 | 50.0 | capacity, against w5 (44.5× the v1 arm) |
| one-hop floor | `--hidden_layers 1` | 45,067 | 0.67 | one ring of spatial context |
| per-pixel floor | `--hidden_layers 0` | 14,795 | 0.22 | no spatial context at all |

The integrator wrapper adds **no** parameters, and the stencil wrapper's count is the
wrapped GNN's by construction — which is why the E2 comparison is exactly one changed
tensor (§4.3b).

## 4b.6 Time integration: the Neural-ODE wrapper

[baselines/odeint.py](../baselines/odeint.py) `GAIntegrator` turns the one-step Euler
operator of §4.5 into a fixed-step explicit Runge–Kutta integration of any backbone's
`vector_field` over each graph's own Δt. It is **not** a backbone (it exposes no
`vector_field` of its own) and it is built *only* when `--integrator` differs from
`euler`, or `--ode_substeps` from 1, or `--ode_step_days` exceeds 0 — so a flag-less run
never constructs it and is bit-identical to the pre-2026-09-05 pipeline.

- **Schemes** are stored as explicit Butcher tableaus `(a, b, c)`: `euler`, `midpoint`,
  `heun`, `rk4` (Butcher, *The Numerical Analysis of Ordinary Differential Equations:
  Runge-Kutta and General Linear Methods*, Wiley 1987; Hairer, Nørsett & Wanner, *Solving
  Ordinary Differential Equations I: Nonstiff Problems*, Springer 1993, 2nd revised
  edition, doi:10.1007/978-3-540-78862-1). `midpoint` and `heun` are implemented and
  unit-verified but **were never trained** — no recorded run uses them.
- **The step is per graph**, which is the property that matters for irregular visits:
  `h_g = Δt_g / n`, or `n_g = ceil(Δt_g in days / --ode_step_days)` when a physical step
  is requested, so an eye is integrated with the same h whether it is co-batched or
  evaluated alone (enforced by a batched == per-graph unit check). The day arithmetic is
  written float32-safely — round `Δt·365` to integer days, ceil with a 1e-9 slack, clamp
  to ≥ 1 — which is exact on the cohort's 90-day visit grid (§1.3) and cannot push
  `ceil()` up by one on an exact multiple. Graphs that finish early take identity steps
  (h = 0 exactly) so the batch tensor stays uniform until the longest graph ends.
- **Autonomy is a flag, and it is the interesting one.** `--ode_autonomous True` (default)
  feeds the conditioning vector's Δt slot a **zero**, so the field is a genuine
  autonomous right-hand side and Δt sets only the integration horizon — the reading under
  which "Neural ODE" is the right name for the model. `False` feeds the substep length h
  instead, which is a *learned Runge–Kutta integrator* and equals the locked operator at
  euler/1. §4.5 carries the lineage citations.
- **Graph-level conditioning is held fixed across the stages.** Positions, edges,
  covariates and any LayerEncoder embedding are per-*step* parameters, not stage-varying
  fields; each stage is evaluated on a zero-copy proxy of the batch, so the caller's
  object is never mutated (`train_helper` reuses it across pushforward steps). This is
  dormant for covariates, which are constant within a step anyway, but it becomes
  load-bearing the moment `--d_embed > 0` meets an integrator — a combination **no
  recorded run used**: all 29 integrator runs carry `d_embed = 0`.
- **Memory**: `--ode_checkpoint` (default on) recomputes each stage in the backward via
  `torch.utils.checkpoint`, verified to leave both the forward and the gradients
  identical. Checkpointed discretise-then-optimise is preferred over the continuous
  adjoint here for accuracy rather than convenience (Gholami, Keutzer & Biros, *ANODE:
  Unconditionally Accurate Memory-Efficient Gradients for Neural ODEs*, IJCAI 2019,
  arXiv:1902.10298, doi:10.24963/ijcai.2019/103; Zhuang, Dvornek, Li, Tatikonda,
  Papademetris & Duncan, *Adaptive Checkpoint Adjoint Method for Gradient Estimation in
  Neural ODE*, ICML 2020, arXiv:2006.02493).
- **Scope guards**: the wrapper refuses a correction branch, `--moving_mesh True` and
  `--euler_dt_scale False` (there is no rate to integrate without the ×Δt form), and
  validates `substeps ≥ 1`, `step_days ≥ 0`.
- **Verification**: a 42-check CPU self-test at the bottom of the module
  (`python GraphPDE/baselines/odeint.py`) covers all six backbones — euler/1 with the
  field still fed Δt reproduces `forward` bit-identically, `u + Δt·vector_field == forward`
  bit-exactly, rk4 holds persistence at zero-init and identity at Δt = 0, batched ==
  per-graph, checkpointing changes neither forward nor gradients, and the observed
  convergence orders on `du/dt = −λu` are 0.99 / 2.04 / 2.04 / 4.35.
- **The pipeline control.** Because `train.py` builds no wrapper at euler/1/0, the
  run-level control for "does the new code path perturb anything?" is
  `--integrator euler --ode_step_days 730` (larger than the longest visit gap, so
  `n_g = 1`) with the field still fed Δt. It reads −0.010 against the locked model on
  fold 2 — replicate-scale, i.e. the wrapper is inert as intended — and that leg, not the
  locked run, is the reference the other integrator legs are read against.
- **Coverage caveat**: every one of the 29 integrator runs uses `--ode_substeps 1`, so
  the substep *count* was exercised only through `--ode_step_days`; more than one substep
  per visit interval is unrun.
- **What this arm cannot show, and the diagnostic that can — which has now run.** Every
  verdict on the wrapper is read on a *binarised endpoint* metric (§7.1), which is blind
  to the trajectory between visits, so no accuracy result here licenses an "ODE" claim in
  either direction. The test that does is the **solver-swap check**: take one trained
  checkpoint, evaluate it at inference under several schemes and step counts, and report
  how much the metric moves — a genuine continuous model should be nearly invariant (Ott,
  Katiyar, Hennig & Tiemann, as cited in §4.5; Krishnapriyan, Queiruga, Erichson &
  Mahoney, *Learning continuous models for continuous physics*, Communications Physics
  2023, arXiv:2202.08494, doi:10.1038/s42005-023-01433-4). It costs no training time and
  **it ran on 2026-09-17** (SOLVER_FINAL_RUNS.md §9.17, 11 post-hoc evaluations, 0 GPU-h),
  and it discriminates:
  - **The locked model fails it.** Under euler *n* ∈ {1, 2, 4} and rk4 *n* ∈ {1, 2} its
    change-region Dice spans **0.0856** — 2.4× the single-fold floor, 6.7× the replicate
    sd — and the successive Euler refinements move −0.0162 then −0.0596, i.e. they grow
    instead of converging. A control confirms the harness is the training operator:
    euler/1 with the field still fed Δt reproduces the bare `forward` bit-for-bit.
  - **The arm trained under an autonomous RK4 field passes it.** Its four refined
    settings agree to **0.0044**, below the replicate sd, with Euler converging at ratio
    4.05 and rk4 *n* ∈ {1, 2, 4} within 0.0005.

  So a continuous-time reading is licensed for arm N1 and refused for the locked model
  and every headline result. **The pair is the finding:** training under a fixed-step RK
  scheme really does produce a solver-independent vector field, and that model is a
  5-fold null on accuracy at ≈4.8× the cost — on this task the ODE property is real,
  obtainable, and worth nothing. Scope: fold 2, one seed each; and the locked model's
  failure is not a clean integration-only test, because a step-conditioned field
  necessarily sees a different Δt when the substep count changes — which is itself the
  Ott et al. point rather than a defect in the probe.

## 4b.7 The Finite Element Network (FEN / T-FEN)

[baselines/fen.py](../baselines/fen.py) `GAFEN` is the "FEM with joint learning" arm
(Lienen & Günnemann, *Learning the Dynamics of Physical Systems from Sparse Observations
with Finite Element Networks*, ICLR 2022, arXiv:2203.08852). It is the only backbone in
the family whose output is defined as a **rate field** rather than as a next state.

- **Mesh.** P1 elements on the two-right-triangles-per-pixel triangulation of the
  lattice: **98,208 cells** at the default pitch, with every one of the 50,176 nodes
  belonging to 1, 2, 3 or 6 cells *(measured)*.
- **Lumped mass.** The mass matrix is row-sum lumped, so assembly is a division by each
  node's adjacent-cell count — which on this equal-area lattice makes the assembly
  **exactly a mean over the adjacent cells**. That is worth stating plainly rather than
  hiding: on a uniform mesh the FEN is a cell-hyperedge message-passing network with mean
  aggregation, and the finite-element machinery is only non-trivial at the boundary (or
  on an irregular mesh, which this module does not consume). It is the caveat that keeps
  "a finite element method ties the locked model" honest.
- **Free-form term.** The paper's factored form: a tanh MLP (depth `--fen_depth 4`, width
  `--hidden_dim`, no normalisation layers, zero-initialised head) over the three vertex
  state vectors, the triangle-type one-hot, the graph covariates and optionally the
  normalised cell centre, emitting one coefficient per vertex and channel, assembled as
  above.
- **Transport term (T-FEN, `--fen_transport`, default on).** `−v_K·∇u|_K` with a second
  MLP predicting one velocity per cell and channel in **mm/yr** (`--fen_vel_gain 0.2`),
  converted per axis to pixels/yr only inside the stencil. One deviation from the cited
  paper must be stated where the term is described: Lienen's T-FEN derives `−v·∇u` from
  `−∇·(vu)` under a locally divergence-free velocity, and this implementation imposes
  **no divergence constraint** — the velocity head is an unconstrained MLP — so what is
  assembled is the non-conservative advective form.
- **Index-unit assembly.** The P1 gradient coefficients are ±1 per pixel step (divided by
  the pitch on the column axis), i.e. the geometry is assembled in *index* units and only
  the velocity conversion carries millimetres. This is the D1 lesson (§4.3) applied: the
  21.3:1 axis imbalance never reaches the MLP. One cross-module caveat: `fen.py` uses the
  precompute's `L/N` pitch (0.12118 mm/row) while the node coordinates of §2.5 are built
  with `linspace`, i.e. `L/(N−1)` = 0.123705 mm/row — the logged +2.08 % discrepancy — so
  the FEN's mm/yr velocities and the GNN's position-derived geometry sit on two slightly
  different conventions.
- **Boundary.** No flux term is ever assembled, so the crop edge carries a natural
  (no-flux) boundary condition by construction — for this dataset a statement about the
  *crop*, not about anatomy (§2.3).
- **Sub-lattice meshes.** `--fen_pitch p` builds p interleaved triangulations (columns
  o, o+p, … for o = 0…p−1, every node in exactly one) — the FEM analogue of the dilated
  stencil — and `--fen_transport_pitch` gives the transport term its own coarser mesh
  (pitch 7 → **97,632 cells** *(measured)*). The canonical arm is a fine free-form mesh
  with a pitch-7 transport mesh.
- **Rate-field contract.** `vector_field` is the assembled `du/dt` and is **autonomous**
  (`data.dt` is not read); `forward` is one explicit Euler step; and `GAFEN` refuses
  `--euler_dt_scale False` outright, because `u + f` has no meaning for a rate. One
  right-hand-side evaluation reaches exactly one cell, so reach must come from substeps:
  the arm is FEN + `--integrator rk4 --ode_step_days D`.
- **Width 96, depth 4 → 68,503 params** — 1.02× the locked model. That total splits
  **34,785 free-form + 33,718 transport**, and the free-form term is *bit-identically
  present in both arms* (same tensor names and shapes), so the free-form control
  `--fen_transport False` at the same width 96 is a **34,785**-parameter model. ⚠️ **The
  transport ablation is therefore purely additive but NOT parameter-matched — 1.97× —
  and it is the only architecture comparison in this document that is not.** The
  parameter-matched control is a width-≈139 free-form FEN (w138 → 67,377,
  w140 → 69,193) and has **never been run**; one 5-fold array (~5 GPU-h) would close it.
  Until then, quote the +0.053 as *established against a free-form control at equal
  width*, name the parameter gap, and rest the mechanism reading on the two things that
  do argue for it: capacity is a measured null on every other axis in this project
  (§7.5 rows T7b, T8, T5), and the effect is concentrated in the near-term growth bin
  rather than spread across horizons, which a generic capacity gain would not be.
  (Verified 2026-09-17 by constructing both arms at their recorded configs; the runs'
  own logs print `params=34,785` and `params=68,503`.)

**The CFL limit, and why it is the arm's binding constraint.** On the lattice the
assembled transport operator is a skew-symmetric central-difference stencil (impulse
response ±1/3 along the velocity, ±1/6 on two diagonals, 0 at the node) whose interior
spectrum is purely **imaginary**. Forward Euler therefore amplifies every mode for any
non-zero learned velocity, and `midpoint`/`heun` have no imaginary-axis stability
interval at all — they must never be used with the transport term. RK4 does have one,
`|λ|h ≤ 2√2 ≈ 2.83`, and the repo's stability gate applies that limit **directly to the
Courant number** `C = |v_idx|·h` per substep. That step is exact only if the stencil's
spectral radius is 1 per unit velocity·step, and the same derivation — archived in
[CODE_COMMENT_ARCHIVE.md](../../CODE_COMMENT_ARCHIVE.md), "REACH AND STABILITY (review
2026-09-05)" — records that radius as **≈1.1–1.2**, which would put the true bound nearer
`C ≲ 2.4` and makes the stated ~2.8 gate optimistic by roughly that factor. **The
discrepancy is recorded here and not resolved**: ~2.8 is what `fen.py`, the baselines
README and the results log all state, and correcting it is a code-side change. It is not
cosmetic — the fold-2 pass that first declared the velocity map readable measured **2.28**,
which is comfortable against the stated bound and marginal against the derived one, and
SOLVER_FINAL_RUNS §9.15 subsequently found that same 45-day configuration unstable at
5 folds. The generic
stability condition is Courant, Friedrichs & Lewy (*Über die partiellen
Differenzengleichungen der mathematischen Physik*, Mathematische Annalen 100(1):32–74,
1928, doi:10.1007/BF01448839).

**Read-outs, and why none of them is currently quotable.** `velocity_mm_per_yr(data)`
returns the per-cell learned velocity and `rate(…, split=True)` the free-form/transport
decomposition — the front-speed and term-magnitude figures the arm exists to produce.
Four caveats travel with them, and the fourth is decisive:

1. the velocity is state-dependent and was read on baseline states only;
2. two checkpoints of one run differ by ≈4×, so it is not a calibrated estimate;
3. reading it as an advection speed rests on the divergence-free assumption the code does
   not impose (above);
4. **as of 2026-09-11 the 45-day T-FEN is not a valid long-horizon integrator as
   trained** — its free-running rollout diverges on 5 of 10 runs at 5 folds × 2 seeds, and
   9 of 10 *final* checkpoints exceed the bound on the combined Courant number of at
   least one advected channel. One-step error stays healthy and every binarised metric is
   unaffected, so no reported anchor moves; but the velocity map must not be quoted, and
   the raw fields must not be quoted at all (§7.5 row T9b, §9.4).

Neither read-out is produced by a committed script — the numbers in the run log come from
post-hoc probes. Closing that (a zero-GPU probe beside `probe_alpha.py`) is what would
make those thesis-bound rows reproducible from a named run-id, as CLAUDE.md requires.

**Verification**: a 48-check CPU self-test at the bottom of the module
(`python GraphPDE/baselines/fen.py`) covers the triangulation census, exact persistence at
init, `forward == u + Δt·vector_field`, autonomy, the P1 gradient of a linear field being
exact on every cell of both the fine and the pitch-7 mesh, the transport rate being exact
at every node including the boundary, the skew-symmetric impulse response, batched ==
per-graph, and train/eval parity.

# 5. The dual-branch MM-PDE composition

Dual-branch mode (`--moving_mesh True`) adds three trainable-or-frozen components on
top of the uniform branch: the **frozen DMM** (§3), a second GNN (**model_b**, the
correction branch), and **ItpNet**, a learned interpolation operator that carries
fields between the uniform and moved meshes. Orchestrated by `MovingMeshHelper`
([GraphPDE/moving_mesh_helper.py](../../GraphPDE/moving_mesh_helper.py)) and composed in
`_dual_branch_forward` ([GraphPDE/train_helper.py](../../GraphPDE/train_helper.py)).

## 5.1 The composition

```
pred = u + Δt·f_θ(uniform mesh)  +  α · Ĩ[ Δt·g_θ(moved mesh) ]
```

- `u + Δt·f` — the uniform branch's full next-state (§4.5).
- `Δt·g` — the correction branch's pure delta, computed on the DMM-moved mesh.
- `Ĩ[·]` — ItpNet interpolation moved → uniform, weights renormalised to a
  **partition of unity** (§5.4).
- `α` — a learnable scalar gate (`ItpNet.moved_gate`, initialised 0): the moved
  branch starts exactly inert (`pred = u + Δt·f` at init) and must *earn* its
  contribution. α also pins the moved term's scale — the loss constrains only the
  *sum* of the branches, so without α the two branches can grow large and mutually
  cancelling, stable only on the training manifold. TensorBoard logs it per step
  (`moved_gate/alpha`).

> **⚠️ MEASURED 2026-08-17, completed and corrected through 2026-09-07 — and it
> invalidates the reading this section originally gave.** The text here used to say "α → 0 means mesh adaptation does
> not transfer to slow-progressing GA (the pre-registered negative result)".
> **That inference is wrong**, and the 5-fold runs plus the bypass control are
> what disprove it. Measured on all five dual folds: α starts at exactly ±0.0020
> (= `lr·sign(g)` from the zero init, confirming ReZero behaves), peaks at
> 0.058–0.093, mean |α| 0.009–0.024, ends ≈ 0 — i.e. **α never opens**. But the
> five **bypass** folds, which load the same DMM and then *ignore its warp*
> (uniform mesh), give the same trajectories: init ±0.0020, peaks **0.031–0.101**,
> mean |α| 0.005–0.023, ending ≈ 0. The bypass range *brackets* the dual range
> rather than sitting under it, and the largest peak in either arm belongs to a
> bypass fold (f3, 0.1005) — with the warp ignored. Since the mesh is not involved
> in the control, α → 0 **cannot** be evidence about mesh adaptation. (Complete at
> 5/5 on 2026-08-28; this supersedes the fold-0-only figure "max 0.056, mean
> 0.027" this paragraph carried before.)
>
> **The mechanism must be reported without a cause.** The correction branch's
> logged pre-clip gradient norm is **0 at the median on every dual fold** (zero on
> 78–85 % of steps) against the uniform branch's ~1.0. ⚠️ **Retracted 2026-08-24:**
> that zero was previously read as *underflow*. It is not — `clip_grad_norm_`
> returns 0.0 both for a genuinely zero norm and for an all-`None` gradient list,
> so a logged 0 does not establish underflow, and what produces the zeros is **not
> established**. The |α|-on-zero-versus-non-zero-step comparison (0.0194 vs 0.0195)
> rests on the same ambiguous zeros and is withdrawn with it. What *is* measured is
> a direct probe on the real stack (`probe_alpha.py`): the path is intact and
> ∂L/∂θ_b is **exactly proportional to α** — 0 at α = 0, 0.0034 at α = 0.002,
> 1.799 at α = 1, against a uniform-branch norm stable at ~2.09 — so at the
> |α| ≈ 0.02 the runs actually reach, the correction branch's learning signal is
> about **60× weaker** than the uniform branch's. The failure is therefore a **dead
> ReZero gate**, not a severed branch: α starts at 0, so ∂L/∂θ_b starts at 0; θ_b
> stays useless, so nothing pushes α up. Self-reinforcing — and still not evidence
> about mesh adaptation, since the bypass control does the same.
>
> Correspondingly the failure mode **swaps modules with the operator**: under
> `--euler_dt_scale False` the moved branch runs away (median 2.3e9, 99.1 %
> above the clip) while ItpNet stays healthy (1.35); under the canonical `True`
> the moved branch is ~0 and **ItpNet** explodes (median 3.7e3–3.3e4, 59–67 %
> above the clip). That explosion is specific to the **gate** and to the
> **k-NN-era** graph, not to the mesh. The bypass arm shares the clip rate
> (61–71 %) and the p90 tail (1.5e6–1.87e7) but its medians are 1.7× to 85×
> lower fold-for-fold (43.7 / 544 / 250 / 1.88e3 / 5.07e3), and removing the gate
> drops fold 2's median to **3.25** on the same warp — the same-fold ordering
> gate + warp 1.5e4 > gate, no warp 250 > warp, no gate 3.25 puts most of the
> magnitude on the gate, the rest on the warp. On the **v2 dilated-stencil** duals
> the median is 0.75–1.28 (fold 2, 2026-09-07) with the same heavy tail. What the
> arms genuinely share — and what the claim rests on — is that the moved branch's
> gradient is 0 at the median in both. Neither operator optimises the dual branch
> healthily; the per-module clip (audit A1) is what keeps the uniform branch at
> ~1.0 in the gated runs (removing the gate doubles it to 2.07, 89 % above clip).
>
> **Reporting rule.** The dual-branch result is a valid empirical statement
> about *this implementation* — no benefit over single-branch, at roughly
> **10–11× the wall-clock** (least-contended epochs 1026 vs 96 s; per-epoch
> timings are contaminated by GPU co-scheduling [mechanism refuted 2026-09-17], so this is order-of-magnitude
> only — [solver_results.columns.md](solver_results.columns.md), convention 4).
> **Complete at 5/5 folds in all three arms (dual 2026-08-24, bypass
> 2026-08-28):** arm means single **0.4515 ± 0.0429**, dual **0.4501 ± 0.0326**,
> bypass **0.4503 ± 0.0324**; paired dual − single = **−0.0013 ± 0.0086 SE**
> (3/5 folds, t = −0.15 on 4 df) and — the number the mesh chapter turns on —
> **dual − bypass = −0.0001 ± 0.0060 SE** (3/5 folds, t = −0.02), the tightest
> null in the project, with an SE less than half the 5-fold paired threshold of
> **|d| > 0.016** implied by the ±0.0127 replicate floor (§7.4). Because the two
> arms differ in exactly one thing — whether `moving_mesh()` returns the DMM warp
> or the uniform grid — that is a direct, parameter-matched measurement that the
> warp contributes nothing to the prediction. The per-eye instrument (Mai
> growth-region Dice at the @360 d anchor, 75 eyes) agrees and shows no tilt:
> dual − single −0.0018 ± 0.0064 (32/75), dual − bypass +0.0001 ± 0.0038 (33/75).
> Fold remains the dominant variance source (0.41–0.52), larger than any
> treatment effect measured on *this* axis — though not larger than every effect in
> the project: the 0-layer per-pixel floor is −0.45 and the dilated stencil +0.074
> at 5/5 folds (§9.4). The mechanism is a **failure to
> optimise the correction branch**, not a demonstration that mesh adaptation is
> useless for GA. Scope the claim to "the gated correction branch does not engage,
> mesh or no mesh, decay or no decay" (§5.3, arm G).
> Full tables: [SOLVER_FINAL_RUNS.md](SOLVER_FINAL_RUNS.md) §5–§5d.

(Under `--euler_dt_scale False` the same composition reads
`pred = u + f + α·Ĩ[g]` — the flag lives on the models, so every site composes
consistently, and the startup banner echoes the actual operator form.)

Two structural invariants: (i) *training and evaluation must compose identically* —
all composition switches (`compose_alpha_gate`, `normalize_interp`, `iso_edges`,
`iso_interp`) live on the **helper object**, not on a per-call argument, because
train.py aliases `_predict_dual_branch = _dual_branch_forward` and five eval/rollout
sites share it; a training-only argument would silently make evaluation a different
operator. (ii) The α gate and the decoder zero-init are mutually exclusive on the
correction branch (§4.4's deadlock).

## 5.2 Building the moved graph (`create_moved_graph`), step by step

Per forward pass (the mesh is recomputed from the *current* state — during rollout
that is the model's own prediction, so mesh adaptation follows the predicted lesion):

1. **Reshape** the batch state (B·N, C·K) to image layout (B, C, K, 49, 1024).
2. **Branch input** — `_state_to_native_mask`: take channel 0 at k=0, denormalise
   (inverse z-score/minmax from `norm_params`), threshold > 0.5 → a binary
   (B, 1, 49, 1024) mask. At t₀ this is the real segmentation; at rollout steps
   t > 0 it is the model's own predicted mask — **the deployment-honest input is
   automatic**, with no resize and no surrogate (this is what the native-grid DMM
   bought; the old SLO path needed a 49×1024 → 256² upsampled "surrogate" here). An
   optional blur-then-rethreshold (`--native_mask_smooth_xi`) exists but is **OFF by
   default** — it was meant to de-raggedise predicted masks but fired
   unconditionally, measurably weakening the mesh at t₀ where the input is already
   in-distribution (audit A2); a t>0-gated variant is a parked follow-up.
3. **DMM query** (`moving_mesh`): build the uniform [0,1]² query grid at (49, 1024),
   evaluate φ = DMM(mask, ξ) (under `torch.enable_grad()` — the gradient map needs
   autograd even inside no-grad eval), take **x(ξ) = ξ + ∇φ** by one combined
   `autograd.grad` over (ξ₁, ξ₂), and rescale to physical (Lx, Ly). The mesh is
   **detached** — the DMM is frozen and its input is hard-thresholded, so no
   gradient can reach a trainable leaf through it (an assert enforces this stays
   true if the DMM were ever unfrozen). With `--bypass_dmm_move` the warp is skipped
   and the uniform mesh is returned (the parameter-matched control, §5.5).
4. **Sanitise, mesh-preservingly**: the mesh legitimately overshoots the domain edge
   on ~1–2 % of nodes (real structure — a hard [0, L] clamp measurably degrades
   Dice), so only non-finite values are repaired and coordinates are clamped to the
   generous (−L, 2L) margin.
5. **Edges for the moved graph**: k-NN (k = `--neighbors` = 12) with
   `torch_cluster.knn_graph` on coordinates that are (a) clamped to the strict
   domain (out-of-domain coords can make the grid-accelerated knn emit out-of-range
   indices) and (b) — with `--iso_edges`, **default True** — divided by the per-axis
   grid pitch first, i.e. searched in **isotropic index space**. This is the same
   anisotropy defect as §2.5, rediscovered in its second home: the moved branch
   rebuilds its own edges and never inherited the precompute fix, so until
   2026-08-06 its k-NN in physical mm returned **100.0 % same-row neighbours** —
   the moved branch had *no connectivity across the 49-axis* and its message passing
   was collapsed to 1-D. Every dual-branch result produced before that fix is
   invalid. `graph.pos` keeps the un-scaled physical coordinates. Invalid edge
   indices (degenerate meshes) are filtered. **This is why the two branches run on
   two different graph constructions under the v2 lock**: the dilated stencil of
   §4.3b is defined by lattice offsets and the moved nodes are off-lattice by
   construction, so `--backbone anisognn` wraps the *uniform* branch only and the
   correction branch keeps this k-NN on the warped mesh.
6. **Interpolate the state onto the moved mesh** (ItpNet mode '1', uniform → moved):
   the k-NN search + ItpNet weight computation runs **once** per forward (the
   coordinates are identical for all channels) and the cached (idx, weights) are
   applied to all C·K state channels in one batched gather. (The labels are
   deliberately *not* interpolated — an upstream-MM-PDE fossil did, at ~106 MB
   retained through the moved-branch backward per forward, but nothing ever
   consumed the moved graph's labels: supervision composes on the uniform grid.
   Removed 2026-08-14, F5.)
7. **Assemble the PyG graph**: interpolated state, `pos = [Δt, x, y]` (moved
   coordinates), batch vector, and carried attributes — `dt` and `covariates`
   **detached** (conditioning inputs), `layer_embed` **not detached** (the encoder
   must receive gradients from both branches).

`model_b` then runs on this graph (optionally on a second GPU: `--device_b` puts
only model_b's forward on `cuda:1`, with PyTorch's cross-device autograd carrying
gradients back — the batch is cloned first because PyG's `.to()` mutates in place).

## 5.3 ItpNet ([GraphPDE/interpolate.py](../../GraphPDE/interpolate.py))

A learned interpolation-weight network: for each query point, given its k nearest
source points, emit one weight per neighbour; the helper applies the weighted sum.

- **Input**: the k neighbour coordinates + the query coordinate (physical mm),
  flattened to width `k·2 + 2`. **Output**: k weights.
- **Two independent MLP stacks** (both tanh-activated with a bare final linear —
  the weights must remain unconstrained): mode **'1'** interpolates uniform → moved
  (builds the moved branch's input), mode **'2'** interpolates moved → uniform
  (returns the correction). Default widths `[k·2+2, 128, 64, k]` from
  `--itpnet_node1/2 = [128, 64]`.
- **Stencil size** `--itpnet_neighbors`: the
  **locked canonical is k = 12 with `--iso_interp True`**, and since 2026-08-14
  these are also the argparse defaults (the retired inherited pair False/30 sat
  as the defaults for four days after the decision — a flag-less local dual run
  silently trained the arm the fold-3 study had killed; F7a). The two are coupled by a
  hard guard: under a physical-mm metric this grid needs k > ~44 before a single
  cross-row neighbour appears, so shrinking k below 30 *without* the isotropic
  metric only narrows an already-1-D stencil — train.py raises. The empirical
  resolution (fold-3 study, **old-era stack** — 90-day curriculum and joint gradient
  clip, so within-era only): iso_interp at the inherited k = 30 was *worse* (late
  mean 0.0935, 20/30 collapsed epochs; the index-space disc of radius ≈3 averages
  over ~6 rows ≈ ±0.38 mm — a width problem, not a metric problem), while k = 12 +
  iso recovered to the native arm (late mean 0.3904 ± 0.0553, 1/30 collapsed). The α
  readings from that study (−0.304 at epoch 19 against the native arm's −0.301; the
  epoch-30 endpoint was never read) are old-era and **did not reproduce** — see §5.1
  and §5.5, where α fails to open in the dual and bypass arms alike. `iso_interp`
  changes only the neighbour *selection*; ItpNet still receives physical
  coordinates. Changing k changes the state_dict.
- **`moved_gate`** — the α of §5.1, the ReZero construction of §4.4 — lives on ItpNet
  (the module that already owns the moved→uniform composition and is already in the
  optimizer), as a 0-dim parameter in its **own optimizer group with
  weight_decay = 0**: AdamW's decoupled decay would otherwise multiply α by
  (1 − lr·wd) every step regardless of gradient — about a **7 % mechanical shrink**
  over the canonical schedule (exp(−wd·Σ lr) ≈ 0.93 at 8 400–9 600 optimizer steps
  by fold, i.e. 30 epochs × 20 passes × ⌈N_eyes/4⌉ batches, at lr 2e-3 / 8e-4 /
  3.2e-4 over epochs 0–4 / 5–19 / 20–29). Small, but it is a pure-optimiser effect on
  the headline α measurement, so α is never decayed. (This is the counterfactual
  bound: α's group has had `weight_decay = 0` since 2026-07-19, before every recorded
  dual run. The "~2×" figure this bullet carried earlier assumed a retired ~3.5e4-step
  undecayed schedule and is withdrawn.) It is likewise its **own gradient-clipping
  group** (§6.4), so the ItpNet weight norm cannot crush the gate's update.
- **The gated machinery's decay is a separate knob, and it was tested.**
  `--weight_decay` (default 1e-2 = AdamW's own) sets decay for every group;
  `--moved_weight_decay` (default `None` = inherit) overrides it for **model_b and
  the ItpNet weights**, whose gradient is exactly α-scaled — so while α ≈ 0 decay is
  the dominant update they receive on zero-gradient steps. **Arm G**
  (`MMPDE_final_mwd0_f2`, fold 2, 2026-09-07) set it to 0 and **refuted** the
  hypothesis that decay is what closes the gate: Dice **+0.0092 ± 0.0020 fold-paired
  (17/20) and +0.0092 ± 0.0044 per-eye (10/16)**, both under the 0.036 single-fold
  floor; α peaked *lower* decay-free (0.058 vs 0.067); `grad_norm/moved` stayed 0 at
  the median in both; and `param_norm/moved` **grew 1.114×** rather than shrinking,
  confirming the ~7 % bound above. Decay is neither the cause of α → 0 nor a material
  drag, which is why §5.1's negative result is scoped "mesh or no mesh, **decay or no
  decay**". ⚠️ **Comparator trap:** that run carries no `BACKBONE`/`GNN_AGGR`, so it
  inherited the v2 slurm defaults and is a *stencil* dual — its twin is
  `ANISOGNN_final_dual_dilmean_f2` (0.5754), **not** `MMPDE_final_f2` (0.4878),
  against which it reads +0.0968, i.e. the E2d stencil effect and not the decay.

## 5.4 The return trip (`interpolate_pred_precomp`) and the partition of unity

model_b's prediction (Δt·g on the moved mesh) is interpolated back to the uniform
grid with mode-'2' weights, then multiplied by α. With `--normalize_interp`
(default True) the weights of each query row are renormalised to sum to 1, making
the operator a true constant-preserving weighted average with bounded gain. The
renormalisation is deliberately **not** a naive division: the raw weights are
unconstrained reals, so a row can sum to a *small negative* number (a `clamp_min`
would flip its sign and amplify it ~10⁶×), and near-zero sums are common, not
corner cases. Measured at init at the **retired k = 30 physical-mm stencil**,
mode-'1' row-sums are mean −0.09 / std 0.93, with **7.3 % below 0.1 in magnitude**
and a minimum of 5.2e-4 → unbounded gain up to ~1900×. The floor is therefore
**sign-preserving with |denom| ≥ MIN_ROWSUM = 0.1**, which leaves ~93 % of those
rows exactly normalised and caps the rest at a gain ≤ 10. Scope that measurement:
mode-'2' — the direction actually used here — was well conditioned at k = 30
(min |sum| 0.39, max gain 2.5×, the floor never fired), whereas at the **canonical
k = 12 + `iso_interp`** the floor engages on ~12.6 % of mode-'2' rows. The bounded
gain holds either way.

## 5.5 Controls and supporting modes

- **`--bypass_dmm_move`** — the parameter-matched control: the DMM is loaded, the
  ItpNet round-trip and the second GNN all run, but the mesh is the uniform grid.
  Parameter-identical to the full dual branch, isolating "the mesh *geometry*" from
  the extra parameters. At the locked 2×64 capacity that is **175 663 vs the
  single-branch's 75 339** trainable in the **v1** k-NN + `mean_max` arm — the
  configuration in which the 5-fold single / dual / bypass CV actually ran — and
  **159 279 vs 67 147** under the v2 lock (§4.7), i.e. ~100 k and ~92 k respectively,
  not the ~1 M of the retired 6×128 stack *(measured, from the run logs)*.
  ⚠️ **The pilot three-way result this bullet used to cite is superseded.** That
  old-era reading — a well-generalising mesh opening α to −0.31 while the
  overfitting-DMM and bypass arms kept α ≈ +0.01, i.e. "the gate opens only for mesh
  geometry" — did **not** reproduce: on the new-era runs α fails to open in the dual
  arm *and* in the bypass arm alike (§5.1). What no longer separates the two arms is
  therefore the **α signal**. The control's *prediction-side* measurement does
  separate them, and it completed at 5/5 folds on 2026-08-28: paired
  **dual − bypass = −0.0001 ± 0.0060 SE** (3/5 folds), an SE less than half the 0.016
  five-fold floor and the tightest null in the project — a direct, parameter-matched
  measurement that the DMM warp contributes nothing to the prediction (§5.1).
- **`--use_alpha_gate False`** — the **`nogate` probe** (fold 2, 2026-08-24):
  replaces the ReZero gate with a zero-initialised correction decoder (train.py
  passes `zero_init_decoder = not use_alpha_gate`, §4.4), so the branch starts inert
  by the *other* route. Three results. (i) The moved branch's gradient is still 0 at
  the median, so it fails to engage under **both** zero-init schemes — §5.1's
  negative result is strictly stronger and needs no re-runs. (ii) Removing the gate
  is decisively **worse: 0.3148 vs the gated dual's 0.4878, −0.173**, nearly 5× the
  0.036 single-fold floor — the gate is not inert, it *protects* the prediction from
  an untrained correction branch that would otherwise be added at full weight.
  (iii) ItpNet's runaway gradient is gate-driven rather than mesh-driven — four
  orders lower on the same warp once α is removed (§5.1). `use_alpha_gate=True` stays
  locked. *Naming wart:* the run landed under `MMPDE/MMPDE_final_nogate_f2/` while
  its `args.json` still records `experiment=MMPDE_final_f2`, so group on the run
  directory, not `cfg_experiment`.
- **The stencil dual (arm E2d)** — the one dual run on the locked v2 backbone,
  `ANISOGNN_final_dual_dilmean_f2` (fold 2): **0.5754** against the dual k-NN GNN's
  0.4878 (**+0.0876**, 16/16 eyes, t = 7.39), so the stencil's benefit transfers
  fully to the dual arm — but against its own single twin `ANISOGNN_final_dilmean_f2`
  (0.6060) it reads **−0.0306** (per-eye −0.0305 ± 0.0086, 3/16 eyes, t = −3.53) at
  roughly 9× the wall-clock. The correction branch does not engage **however strong the
  uniform branch is** (⚠️ TB was not pulled for this run, so no α trajectory;
  [SOLVER_FINAL_RUNS.md](SOLVER_FINAL_RUNS.md) §9.12e).
- **`--warm_start_uniform` + `--freeze_uniform_branch`** — initialise the uniform
  branch from a trained single-branch checkpoint and freeze it (including the
  LayerEncoder, which is part of the frozen branch's function): α = 0 then
  *provably* recovers the warm-started baseline, so the dual branch cannot lose for
  optimisation-coupling reasons (f co-adapting to g). Freezing also keeps the
  branch in `eval()` throughout so a BatchNorm ablation cannot drift its stats.
  The load checks strict state_dict shapes — after unwrapping every nested `inner.`
  wrapper on both the module and the state_dict, since `GAIntegrator` over
  `GAAnisoGNN` over the GNN nests two — and then compares the checkpoint's **own
  saved args** for every operator flag that has *no* state_dict footprint and could
  therefore never be caught by a shape check: `euler_dt_scale` (a mismatch silently
  applies Δt-mis-scaled residuals — measured 103 % relative error at the modal
  180-day interval; addendum A6), `norm_type` (`layer` and `graph` have an identical
  parameter footprint, §4.3), `edge_feat_index` and `edge_feat_none`, `backbone`
  (only the `gnn`↔`anisognn` pair may cross-load, since the wrapper owns the same
  GNN as `inner`), the anisognn stencil geometry (`stencil`, `pitch`, `taps`, `rows`
  — a non-persistent buffer, so two geometries share a state_dict), and the four
  integrator flags.
- **DMM loading guards** (train.py): the checkpoint must have
  `mask_source == 'oct'` (an SLO checkpoint would load without any shape error —
  `pool` weights are grid-independent — and then silently be conditioned on a field
  it never saw) and `bound_constraint == 'soft'`; the DMM is reconstructed from the
  checkpoint's *own* `branch_layers`/`trunk_layers`/`out_layers`, set to `eval()`,
  all parameters `requires_grad=False`, excluded from the optimizer; and the
  checkpoint file's **sha256 content hash** (first 16 hex) is recorded in
  `args.json` and printed at startup as DMM provenance — the path string is a
  generic container mount and proves nothing. The resume-time mismatch hard-fail
  exists in source but is **dormant**, since solver `--resume` is disabled and
  raises before the DMM is ever loaded (§6.5).

---

# 6. Training

Entry: [GraphPDE/train.py](../../GraphPDE/train.py) `main()`; inner loop in
[GraphPDE/train_helper.py](../../GraphPDE/train_helper.py). Single-branch
(`--moving_mesh False`, the MP-PDE baseline) and dual-branch training share
everything below except the moved-branch components.

## 6.1 The loss regime

The criterion (`_WeightedChannelMSE`) stacks up to three terms, each independently
togglable. **Since the 2026-08-15 loss lock the canonical GA recipe uses the first
two**; the third (monotonic) is implemented and selectable but set to 0.0:

1. **Channel-weighted MSE** (base term): per-channel weights
   `[mask_channel_weight, 1, …, 1]` with `--mask_channel_weight` **5.0** — the mask
   is the clinical deliverable; the 10 layer channels are auxiliary. The weighted
   sum is divided by the mean weight so the scale stays comparable to plain MSE.
2. **Soft-Dice auxiliary on the mask channel** (`--mask_soft_dice_weight`,
   canonical **5.0**; Milletari, Navab & Ahmadi, *V-Net: Fully Convolutional
   Neural Networks for Volumetric Medical Image Segmentation*, 3DV 2016,
   arXiv:1606.04797 — applied here to a sigmoid-sharpened **z-scored regression
   output**, not to a segmentation probability map, which is the source of the
   decalibration caveat below):
   `1 − 2·Σ(p_soft·t_hard)/(Σp_soft + Σt_hard)` with
   `p_soft = sigmoid((pred − thr_norm)·sharpness)` (canonical sharpness **2.0**)
   and a hard-thresholded target. Why it exists: on slow-moving GA, plain MSE is
   dominated by the ~99 % of static pixels, and the early single-branch runs
   collapsed to *bit-exact copy-input* on the mask channel (predictions within the
   threshold band of the input everywhere); the soft-Dice term restores gradient in
   the binarisation band at the moving boundary. The threshold is the physical 0.5
   mapped into normalised space (`_mask_threshold_in_normalised_space` — the same
   mapping evaluation uses, so loss and metric agree). Scoped **per graph,
   unconditionally** (one Dice per eye, then averaged; since `b973a42` this is
   hard-wired, not a flag): Dice is a ratio of sums, so the scope of the sum is a
   weighting choice — pooling the whole flattened batch made an eye's gradient
   depend on which eyes it happened to be batched with (the objective became a
   function of batch composition, and it disagreed with the per-eye-then-averaged
   evaluation). Train and eval use the same criterion object with `n_graphs`
   threaded at every call site (`_crit_kw`), so the objective is identical in both;
   a B = 1 batch degenerates exactly to the single Dice, and a ragged batch
   (impossible for equal-N GA graphs) raises rather than silently falling back to
   pooled. NB the eval-side weighted `ts_mse`/`ts_rmse` columns changed scale at
   this boundary — weighted eval columns are not comparable across it. Known,
   accepted side effect: the shallow sigmoid does not saturate at the physical
   values, so the term *decalibrates* the raw mask regression (predictions stretch
   ~1.6× about the threshold; ~⅓ of reported mask rollout MSE is this stretch, not
   error) — it cannot flip any binarised metric, but raw-RMSE tables need the
   caveat. **The loss ladder ran (2026-08-15, fold 2, seed 42) and answered it:**
   channel weighting, not soft-Dice, is what escapes the copy-input collapse — L1
   (mask ×5, no Dice) equals L2 within noise (0.4885 vs 0.4963), while raw MSE (L0)
   reads 0.0318 and does not escape until epoch 26. What soft-Dice buys is
   **immediate escape and roughly half the epoch-to-epoch sd** (0.049 → 0.025), not
   a better final score; escape epoch is a clean dose–response in mask-gradient
   strength (s2 → ep 0, s4 → ep 2, s6 → ep 5, mw5 → ep 9, mw1 → ep 26). **The
   sharpness trade is measured on the RMSE side only.** On change-region Dice the
   three legs sit inside the 0.036 single-fold threshold implied by the ±0.0127
   replicate floor (§7.4): s2 0.4963, s6 0.4853 (−0.011, inside noise), s4 0.4642
   — and that −0.032 for s4 is one of the five single-fold deltas **retracted** on
   2026-08-17 (§7.4, §9.3). What *is* measured is the calibration cost: s2 inflates
   `ts_mask_rmse` to 0.880 against L1's 0.336 and s6's 0.362 (2.6×), and s6
   recovers essentially all of it — so any thesis table quoting raw mask RMSE must
   carry this caveat. s2 remains canonical for its immediate escape (ep 0), its
   0/30 collapsed epochs and the lowest epoch-to-epoch sd of the three
   (0.025 vs s4 0.044 / s6 0.048), **not** for a better headline. (The paired
   per-eye instrument does read s4 at −0.032 ± 0.011, 3/16 eyes, sign-test
   p = 0.021; the single-fold floor governs either way.)
3. **Soft monotonic-mask penalty** (`--monotonic_mask_weight`, **locked at 0.0 =
   OFF** by the F1 ladder, 2026-08-15; the argparse default is 0.0 too. The
   `L4mono` leg (L6 + mono 2.0) scored 0.5282 ± 0.0173 against L6's
   0.5315 ± 0.0103 — **−0.0032 ± 0.0033 SE over 7/20 paired epochs**, i.e. no
   effect at the **then-locked L6 configuration**, which ran
   `euler_dt_scale=False`; the pair therefore isolates the penalty at a shared
   `nodts` operator, and −0.0032 is an order of magnitude under the 0.036
   single-fold floor, so the null is robust. Per the
   pre-registered rule the simpler objective won and every later stage runs at
   0.0. Note the penalty was never re-tested after `euler_dt_scale` was re-locked
   to **True** on 2026-08-17 (§4.5, §6.6): no final-era run combines mono > 0
   with the locked operator. Described here because the
   term is still implemented, still flag-selectable, and is the encoding of the
   clinical prior any future leg would re-test):
   `λ · Σ ReLU(u_t − pred) / #atrophied` on the mask channel — atrophied =
   bootstrap > thr_norm; pixels not yet atrophied see zero penalty. Encodes the
   clinical prior that GA never regresses (dead tissue does not heal) as a
   differentiable penalty rather than a hard clamp; the model remains free to
   predict growth anywhere. Requires the bootstrap state, gated via
   `criterion.needs_bootstrap`. Two 2026-08-14 refinements/caveats:
   - **Scoped per graph** (`38b610f`, mirroring the Dice fix and for the same
     reason): the penalty is a ratio — sum of decreases over atrophied count — so
     a batch-pooled denominator diluted a small-lesion eye's penalty by its
     co-batched eyes' lesion sizes (measured 101×; per-graph recovers the
     healed-small-eye's weight ~50×, exactly the analytic factor). B = 1 is
     bit-identical to the old pooled formula; an eye with no atrophied bootstrap
     pixels contributes 0.
   - **The bootstrap is the PREVIOUS FRAME, and that is an open decision (F2a):**
     on teacher-forced passes it is the observed state (the documented prior);
     on *unrolled* passes it is the model's own detached rolled prediction — so
     the penalty there enforces trajectory self-consistency and **ratchets the
     model's own false positives** (a rollout false positive cannot be corrected
     toward healthy GT without paying it; measured: the total gradient flips sign
     on such a pixel, |mono| = 31.8× |data + dice|, term live on 72 % of logged
     steps). Defensible as a deployed-rollout property, but teacher-forced and
     unrolled passes implement two different priors without anyone having chosen
     that — the ladder measured the consequence and found none, which is why the
     penalty is **locked off** rather than merely defaulted off: the F2 ratchet
     mechanism above is a real defect, and the ladder showed nothing is lost by
     removing the term entirely.

**Optional row masking — `--exclude_pad_nodes`** (default **False** = the
historical objective; `_CRITICAL_ARG`, run-dir token `nopad`, the L5nopad ladder
leg): drops nodes whose TARGET equals the zero-fill z-vector (all 11 channels,
`isclose` at 1e-4 in z-space; z-score precomputes only) from **all three terms** —
row-filtered out of the weighted MSE, multiplicatively zeroed out of the per-graph
Dice and mono *before* their (B, ·) reshapes, so uneven pad counts per graph can
never make the per-graph scoping ragged. Motivation: the crop's zero fill sits at
−2.4…−2.9 σ in the layer channels and is otherwise regressed at full weight
(~4.9 % of val nodes). Two measured caveats that scope what the leg can conclude:
the mask is **target-side only**, so nodes whose *input* is fill but whose target
is anatomy (2.0 % of nodes, the noisiest supervision class — 3.6× the clean
residual) stay in the loss (the leg measures supervision-ON-fill, not the larger
supervision-FROM-fill coupling); and pad-row *predictions* become training-free
while the plain change-region Dice still scores them — which is why the leg's
readout column is the pad-masked `change_region_dice_360d_anat` (§7.1).

Per-term values are recorded (`last_components`) and logged
(`loss/term_wmse`, `term_dice_*`, `term_mono_*`) — necessary because the total
"RMSE" mixes units (at weight 5, soft-Dice can be ~43 % of the total) and is not a
prediction error. Historical, removed loss experiments: a change-region per-pixel
MSE boost (no clear win) and the supervisor-suggested intermediate-time-point
regulariser (query at random sub-times τ = a·Δt against the linear interpolant;
swept λ ∈ {1, 3, 10}; **no benefit** — the reg = 0 legs matched or beat it;
removed 2026-06-11 and reportable as a negative result).

## 6.2 Unrolling: the pushforward trick, made time-aware

**What unrolling is and why.** An autoregressive solver is evaluated on *rollouts*
— its own predictions fed back as inputs — but one-step training only ever shows it
ground-truth inputs, a distribution-shift gap that compounds. The **pushforward
trick** (Brandstetter et al. §3.1) closes it: unroll the model for several steps
**without gradient**, then train only the final step, so the network learns to make
a correct step *from its own slightly-drifted state*. Gradient stays cheap (one
step) while the input distribution matches deployment.

**The GA twist: budgets are elapsed time, not step counts.** Visit gaps are
irregular, so "unroll 2 steps" means 180 days for one eye and 720 for another. The
curriculum is therefore denominated in **days**:

- Each training pass draws a budget uniformly from
  `{0, 1, …, min(epoch, unrolling)} × unroll_base_days` — i.e. the horizon ramps in
  over the first `unrolling` epochs. `--unroll_base_days` default **180** = the
  cohort's *modal* interval; the historical 90-day quantum (the *smallest* gap) was
  arithmetically incapable of unrolling — `steps_to_budget` undershoots, so a
  budget of one minimal gap can never chain two visits (measured 0/75 eyes), and
  its level filter silently fell back to unrestricted sampling for 53/59 training
  eyes. `--unrolling` default 4; the **locked canonical is 2** (max 360 d, matching
  the evaluation anchor — the @360d endpoint is realised as a median of one unroll
  step).
- The dataset is told the budget (`min_budget_days`): random sampling is
  restricted to start windows that can actually realise it
  (reachable_days ≥ B and first_gap ≤ B).
- Within a batch, each eye's **undershoot step count** to the budget is computed
  (`steps_to_budget`); samples are **grouped by step count**, and each group is
  rolled `n` steps under `no_grad` (`_advance_chain`: fetch the chronologically
  next window, replace its input with the rolled prediction
  `cat[old_x | pred][:, -CK:]`; ended sequences are dropped, the rest continue)
  and then given one differentiated forward + loss. Group losses are combined with
  batch-mean weights (`len(group)/B`) and backpropagated per group.
- **No mask surrogate is needed anywhere**: the roll replaces channel 0 with the
  model's own predicted mask, which is exactly what the native-grid DMM branch
  reads — the deployment-honest conditioning is automatic (§5.2).
- Budget 0 (always in the pool) is a plain single-step pass. LayerNorm (not
  BatchNorm) is what makes the no-grad unroll faithful (§4.3).

## 6.3 ItpNet pretraining (epoch 0, dual-branch only)

Before real training, ItpNet's interpolation weights are taught the **round-trip
identity**: interpolate the true state uniform → moved → uniform and penalise the
deviation from the original (`training_itp_precomp`). Details that matter:

- Runs `--itp_pretrain_passes` passes (canonical **25**) with its **own AdamW** at
  the main lr and the same decay the main optimizer applies to ItpNet
  (`--moved_weight_decay`, else `--weight_decay`; §5.3, §6.4) — deliberately
  separate so it cannot pollute the main optimizer/scheduler state before real
  training begins.
- The α gate is **disabled** during the pretrain (a zero gate would zero the
  round-trip signal and the weights could never train).
- The objective is a **dedicated identity criterion** — channel-weighted MSE
  *only*, not the full training loss: at the exact identity the MSE term is zero,
  so any auxiliary term with nonzero gradient there (soft-Dice's sigmoid does not
  saturate at the physical values) would become 100 % of the objective and push the
  operator *away* from the identity it is being taught (audit B1).
- Gradients are **clipped** at `--grad_clip` (the first-step ItpNet gradient norm
  was measured spanning 0.87–1872 across (k, iso, seed) — with AdamW the harm of an
  unclipped spike is not a huge first step but a suppression of the *subsequent*
  steps that grows while v remembers g₁: exactly 1.0× at step 1 (AdamW's first
  step is scale-invariant, m̂₁/√v̂₁ = sign(g)), 4.3× by step 10, 19.6× by step 25
  and ~174× by step 50 in the recorded simulation, i.e. **8.8× less cumulative
  movement over the 61-step pretrain** than the clipped run — an effectively inert
  pretrain on exactly the seeds that draw a large g₁). Logged: `itp_pretrain/loss`, the plain unweighted
  round-trip MSE `itp_pretrain/mse_u` (the batch-size- and weight-independent
  fidelity readout), and — wired 2026-08-15, closing a filed code↔NOTES
  divergence where commit `dc52682` claimed tags it never emitted — the pre-clip
  per-batch gradient norms `itp_pretrain/grad_norm` / `grad_norm_max` (TB +
  metrics.jsonl): the attribution telemetry for the Stage-F4 dual-arm seed
  spread.

## 6.4 Optimization

- **AdamW** (Loshchilov & Hutter, *Decoupled Weight Decay Regularization*,
  ICLR 2019, arXiv:1711.05101), lr `--lr` (default 2e-3), one optimizer over all
  trainable modules in separate param groups: uniform GNN, moved GNN, ItpNet
  weights, **α in its own group with weight_decay = 0** (§5.3), LayerEncoder (when
  enabled). Under `--freeze_uniform_branch` **neither the uniform GNN nor the
  LayerEncoder enters the optimizer** — the encoder is frozen with the branch it
  feeds. The frozen DMM is never in the optimizer.
- **Decay**: `--weight_decay` (default **1e-2** = AdamW's own, recorded in
  `args.json`) on every group; α's group is the one exception at 0 (§5.3).
  `--moved_weight_decay` (default `None` = inherit) overrides it for the
  correction branch (`model_b`) and ItpNet's weights — the modules whose gradient
  is exactly α-scaled — and also sets the decay of the epoch-0 ItpNet pretrain
  optimizer (§6.3). `param_norm/<group>` is logged beside `grad_norm/<group>`, so
  a decay-only shrink is directly readable. Measured (arm G,
  `MMPDE_final_mwd0_f2`, fold 2): a decay-free gated machinery is a **null** —
  +0.0092 on both instruments, under the 0.036 single-fold floor; α peaks *lower*
  without decay (0.058 vs 0.067) and `param_norm/moved` **grows 1.114×**, so decay
  was never the cause of α → 0 (§5.3).
- **LR schedule**: `MultiStepLR`, γ = `--lr_decay` (0.4), milestones
  `--lr_milestones` default **[5, 20]** (sorted/deduped defensively). Deliberately
  decoupled from `--unrolling`: the historical schedule fed the unroll horizon in
  as the first milestone (an upstream inheritance from when it really was an epoch
  count), so every pushforward-depth ablation silently swept the LR schedule too,
  and its remaining milestones (30/50/70) never fired within a 30-epoch run.
- **Gradient clipping** (`--grad_clip` 1.0, `--clip_mode per_module` default):
  one `clip_grad_norm_` per module group — uniform / moved / ItpNet weights / α /
  encoder — so each module's clip coefficient depends on *its own* gradient only.
  The legacy single joint clip (kept as the `global` ablation leg) coupled the
  branches: the joint pre-clip norm exceeded the clip on **83–92 % of dual-branch
  steps**, with per-run medians spanning **2.07–4.2e4** (p90 up to 4.9e6, max
  7.5e10), against a single-branch median of 0.82–0.87 that sits *below* the clip
  on ~60 % of steps — so on the high-norm runs the shared coefficient throttled the
  uniform branch by up to ~4 orders of magnitude, and single-vs-dual comparisons
  were comparing two different optimisers. (Those are the legacy-joint-clip runs,
  i.e. everything before 2026-08-08; the joint scalar could not be decomposed at
  the time, and the per-module logging this fix added later attributed the runaway
  to **ItpNet** at the canonical ×Δt operator and to the **moved branch** only at
  `--euler_dt_scale False` — never to the uniform branch, §5.1.) Pre-clip per-group
  norms are logged in both modes (`grad_norm/<group>`, `grad_norm/global`); the
  encoder is its own group because it receives gradients from both branches.
  Single-branch at d_embed = 0 is bitwise identical in both modes.
- **Epoch structure**: `--num_epochs` (canonical 30) × `--passes_per_epoch`
  (canonical 20; argparse default 30) passes; one pass = one budget draw + one full
  DataLoader sweep (one random start-window per eye, batch_size 4). Validation
  (§7) runs every epoch.
- **Determinism**: seeded `random`/NumPy/torch/CUDA, `cudnn.deterministic = True`,
  `benchmark = False`; loader workers seeded; `num_workers = 0` (required — the
  budget mutation on the dataset would not reach forked workers). Two qualifications
  the flags do not cover. **Run-to-run nondeterminism is real and measurable**: the
  replicate floor of §7.4 is estimated from same-config re-runs, and same-seed pairs
  spread as widely as cross-seed ones. And **precision is not matched across backbone
  classes** — the convolution arms run at PyTorch's default TF32 while the GNN's
  `Linear` path is fp32 (§4b.4), so a conv arm's output shifts ~1.4e-3 relative with
  the sub-batch size and its bit-determinism claims are CPU / TF32-off claims.

## 6.5 Run identity, checkpointing, resume

- **Run naming**: `<experiment>_[TxNxxNy]_n<k>_ep<E>_bs<B>_lr..._dim<H>_layers<L>_
  unroll<U><hp_tag><data_tag>_<timestamp>`. `_hp_tag` **always** emits the branch
  (`mm`/`sb`) and, on `--backbone anisognn`, the backbone name and `as<stencil>`;
  every other token fires when its knob differs from `_hp_tag`'s **own reference
  value**. Three of those references are no longer the argparse defaults —
  `iso_interp` is compared against the retired `False`, `itpnet_neighbors` against
  the retired `30`, and `mask_soft_dice_weight` is a bare `> 0` test — so
  `isoI`, `itpk12` and `dice5s2` (and, under the v2 lock, `anisognn`, `aggrmean`
  and `asdilated`) appear on **every** canonical run, e.g.
  `…_unroll2_sb_anisognn_aggrmean_dice5s2_asdilated_isoI_itpk12_sp0_ageper_visit_…`.
  The full, current token table is
  [EXPERIMENTS.md](../../EXPERIMENTS.md) §3.2 — it also covers the backbone and
  stencil geometry, the FNO, FEN, edge-feature, norm-site, Neural-ODE and
  weight-decay tokens added after this section was written. `data_tag` stamps the
  **data identity** (`_sp<fold>`, `_age<mode>`, `_nocov`)
  read from the loaded precompute's meta — the cluster mounts every fold at the
  same generic path, so the run name and `dataset_provenance.json` are what make
  fold/variant identifiable from the artefacts (audit B7).
- **Checkpoints**: `last.pt` every epoch; `best.pt` on validation-metric
  improvement (§7.4); periodic `ckpt/epoch_*.pt` + rollout NPZ on the
  `--save_every` cadence (canonical 1000 = effectively final-epoch only; NPZ at
  every epoch costs ~14 GB/run). Checkpoints carry model (+model_b, ItpNet,
  encoder), optimizer, scheduler, args, and the best-metric bookkeeping. The
  **frozen DMM is deliberately NOT saved** (since 2026-08-15, F10.6): no load
  path ever restored it — it was 1.1–5.3 M dead params per dual checkpoint —
  and a reader trusting an embedded copy would bypass the sha256-checked DMM
  provenance; the DMM's identity lives in `args['dmm_checkpoint']` +
  `args['dmm_checkpoint_sha256']`, its weights in that run's own checkpoint.
- **Resume: DISABLED (2026-08-15, user decision).** `--resume` now raises
  immediately: no completed solver run ever resumed, and the path carried
  known-unsafe semantics not worth fixing for an unused workflow (`last.pt`
  saved before `scheduler.step()` → one epoch at a stale LR; no RNG state
  checkpointed → a "resume" replays the fresh run's sampling streams from
  epoch 0; a critical arg absent from an old `args.json` was silently dropped
  while the WARN claimed the CLI value was in effect — NOTES F8/A7).
  `train_solver.slurm` refuses `RESUME` at job start. The supported
  weight-reuse path is `--warm_start_uniform` (loads the uniform branch +
  encoder from a finished run's checkpoint; guards architecture via strict
  state_dict shapes, and every **zero-state_dict-footprint operator flag** —
  `euler_dt_scale`, `norm_type`, `edge_feat_index`/`edge_feat_none`, `backbone`,
  the anisognn stencil geometry (stencil/pitch/taps/rows) and the integrator
  signature (`integrator`, `ode_substeps`, `ode_step_days`, `ode_autonomous`) —
  against the checkpoint's saved args, since a strict load cannot see any of them.
  Two deliberate exemptions: only the `gnn` ↔ `anisognn` pair may cross-load
  (`GAAnisoGNN` wraps the same GNN as `inner`), and an args-less checkpoint is
  exempt from the `norm_type` check when the local run is `batch`, which
  self-protects via its running-stats keys).
  The two-phase merge machinery, the `dataset_provenance.json` identity gate
  and the DMM content-hash check remain in the source as documentation for a
  future re-enable but are unreachable. (DMM-side resume in `dmm.py` remains
  fully supported.)

## 6.6 The locked canonical solver recipe

Encoded as the defaults of [jobs/train_solver.slurm](../../jobs/train_solver.slurm)
(realigned 2026-08-12, backbone and aggregation re-locked 2026-09-03) rather than
argparse defaults: hidden **2 layers × 64** features; uniform graph = the
**dilated stencil** (`--backbone anisognn`, rows ±1 × columns
{0, ±7, ±14, ±21}, 20 neighbours, ±0.12 mm reach on both axes) with
`--gnn_aggr mean` — **LOCKED CONFIGURATION v2**, 2026-09-03, seed-7 gate
discharged the same day (SOLVER_FINAL_RUNS §9.12e: +0.0736 ± 0.0162 SE
fold-paired, 5/5 folds), **67,147 params**. The v1 values (k = 12 index-space
k-NN + `mean_max`, 75,339 params) are the **comparison arm**, reproduced with
`BACKBONE=gnn GNN_AGGR=mean_max`; the k = 12 k-NN remains the *data* graph that
arm consumes (the moved branch rebuilds its own on the warped mesh), and
`--neighbors` is inert on `anisognn` (`train.py`
refuses a value ≠ the precompute's k rather than let the run name claim a
receptive field the operator never had). Then: batch size 4, 30 epochs ×
20 passes, lr 2e-3 / decay 0.4 at {5, 20}, weighted MSE (mask ×5) + soft-Dice (5,
sharpness 2) + **monotonic 0.0**, `d_embed 0`, unrolling 2 × 180 d, per-module clip
1.0, ItpNet pretrain 25 passes, `iso_edges True`, `iso_interp True` + k = 12,
`native_mask_smooth_xi 0`, `exclude_pad_nodes False`, `euler_dt_scale True`,
seed 42, DMM = `GA_NAT_O512x2_S1` s42 `checkpoint_latest.pt`. The three arms are
`sb` (single-branch), `dual`, `bypass`; the 5-fold CV is a Slurm job array over
this template. **The loss stack is LOCKED** (2026-08-15, by the 9-leg Stage-F1
ladder on fold 2 = the L6 configuration): `mask_channel_weight 5.0` +
`mask_soft_dice_weight 5.0 @ sharpness 2.0` + `monotonic_mask_weight 0.0` +
`exclude_pad_nodes False`. Monotonic went to zero because the `L4mono` leg
(= L6 + mono 2.0) measured **−0.003 ± 0.003 SE, 7/20 epochs** against L6 — no
effect at the then-locked L6 configuration, which ran `euler_dt_scale=False`, so
the simpler objective wins (and F2 had separately measured the term ratcheting the
model's own rollout false positives at 31.8× the data gradient). `euler_dt_scale`
was itself locked back to **True** on 2026-08-17 after the 5-fold ablation returned
a null (§4.5), and mono has not been re-tested against that operator — no
final-era run combines mono > 0 with the locked ×Δt. These defaults are load-bearing: Stage F3
submits this template **directly** (`ARM=… FOLD=… sbatch`), bypassing the launcher,
so the template's defaults *are* the objective of the clean runs. The launcher's
loss knobs remain operator-overridable (`MONOTONIC_MASK_WEIGHT=… STAGE=arch …` —
snapshot-at-top, so a leg's own explicit exports still win per leg). Post-2026-08-14
runs are only comparable with runs at the same objective (per-graph dice + mono).

---

# 7. Evaluation

There is no separate evaluation entry point: `train.py` validates every epoch with
two procedures over the fold's validation eyes, writes everything to
`metrics.jsonl` + TensorBoard + per-epoch JSON, and exports full rollouts as NPZ
for post-hoc visualisation.

## 7.1 Metrics hierarchy and the headline

- **Headline / selection metric: `change_region_dice_360d`** — Dice on the
  **symmetric difference of binarised masks vs baseline** at the ~360-day
  endpoint: `pred_changed = (pred_bin ≠ baseline_bin)` vs
  `true_changed = (true_bin ≠ baseline_bin)`. Persistence predicts no change, so
  its score is **0 by construction** — any positive value is genuine tracking of
  the moving boundary. This replaced full-mask Dice for model selection because
  the full-mask floor is ~0.87 (the static lesion interior dominates; on a
  slow-growing disease, full-mask Dice is nearly signal-free).
  Three additive companions (2026-08-14/15):
  `change_region_dice_360d_border` / `_interior` split the per-eye scores by
  whether the endpoint GT lesion touches the imaging boundary — **pad-aware**:
  border = the crop's outermost ring OR 4-adjacency to the zero-pad band, since
  for the 27 % of visits whose native grid is smaller than the crop the true
  FOV edge lies strictly inside it (split-2 val: 6 border / 10 interior; the
  interior column is the uncensored reference for the F3 crop-censoring
  effect). `change_region_dice_360d_anat` (+ `n_anat_eyes_360d`) is the same
  Dice with pad rows excluded from both sides — the readout column for the
  L5nopad leg, whose pad-row predictions are training-free and would otherwise
  be scored by the plain column. NaN on minmax precomputes (no pad z-vector).
- **Full-mask Dice/IoU @ 360 d** (model, persistence, and their delta) — reported
  for comparability; computed on the denormalised-equivalent threshold
  (**threshold after denormalisation semantics**: the physical 0.5 midpoint mapped
  into normalised space, +0.529 for split 2 — the same mapping the loss uses).
- **Per-step and rollout RMSE** (weighted = training scale, unweighted =
  cross-run-comparable, mask-only, layers-only, plus an anatomy-only layer RMSE
  that excludes **pad-vector nodes**). A pad-vector node is one whose target sits
  at the zero-fill z-vector in all 11 channels — ~6.3 % of split-2 training nodes,
  of which only ~28 % is crop zero-fill and the other ~72 % is upstream all-zero
  segmentation *inside* the real FOV, so the detector is broader than the crop
  (audit C3, 2026-08-07). The ~3 % of nodes whose pad status *flips* between visits
  carry ~31 % of the validation **persistence** layer squared error, inflating that
  baseline's layer RMSE from 0.713 to 0.829 — which is why the anatomy-only column
  exists. All of these are documented as deceptive for GA on their own:
  persistence is a strong per-pixel baseline.
- **Collapse counter** `n_identical_to_bootstrap`: the number of eyes — among
  those that reach the ~360 d endpoint (`n_sequences_at_360d`) — whose thresholded
  endpoint prediction is *bit-for-bit* the thresholded **baseline-visit** mask,
  i.e. the model predicted no change at all over the horizon. Note that is the
  baseline state captured at the *start* of the rollout, not the endpoint step's
  input, which by then is the model's own rolled prediction — the direct detector
  of the copy-input failure mode.
- **Mai-2024 cohort metrics** (Mai, Lachinov, Reiter, Riedl, Grechenig, Bogunović
  & Schmidt-Erfurth, *Deep Learning-Based Prediction of Individual Geographic
  Atrophy Progression from a Single Baseline OCT*, Ophthalmology Science
  4(4):100466, 2024, doi:10.1016/j.xops.2024.100466 — the direct comparison paper:
  same MUW cohort and prediction target. Standing input-regime caveat: this model
  consumes pre-segmented masks + layer depths while Mai consumes raw OCT, so Mai's
  published bins are an **anchor, not a head-to-head** — cf.
  [SOLVER_FINAL_RUNS.md](SOLVER_FINAL_RUNS.md) §9.1 and the crop-comparability
  caveat in §2.3): per-step records binned into (0,1], (1,2], (2,3], (3+] year
  horizons with total-mask and **growth-region** Dice (growth region =
  followup ∩ ¬baseline), lesion areas in mm² and √area in mm (the square-root
  GA-area transform of Feuer et al., JAMA Ophthalmology 131(1):110–111, 2013,
  doi:10.1001/jamaophthalmol.2013.572, which removes the dependence of growth rate
  on baseline lesion size), √area MAE; per-eye growth
  rates (Δ√area / Δt, mm/y) with cohort **Pearson r / R²**; and **fast-progressor
  ROC-AUC** at top-10/15/20 % growth-rate cutoffs (computed through the rank-sum /
  Mann–Whitney-U identity, so no external dependency is needed). All
  Mai scalars land in `metrics.jsonl` (`mai/...`) and the raw per-step/per-eye
  records in `mai/epoch_*.json`.

## 7.2 The two procedures: one-step and rollout

**One-step evaluation** (`test_timestep_losses`) is teacher-forced: at every window
index (the step set is the union over all eyes, so late visits of long sequences
are covered), each validation window gets a single prediction from its *ground-truth*
input, batched across eyes — the standard "one-step vs rollout" split of the
neural-PDE literature, isolating operator accuracy from rollout drift. It reports
the weighted/unweighted/mask/layer RMSE breakdown per step and overall.

**Rollout evaluation** (`test_rollout_losses`) is the deployment-shaped procedure.
Per validation eye: start at the **baseline visit** (GA mode forces
`nr_gt_steps = 0`), predict the next visit; then repeatedly fetch the next window,
overwrite its input with the rolled prediction (same
`cat[x | pred][:, -CK:]` as training), and predict again — a full autoregressive
rollout over the eye's real visit schedule using each window's actual Δt. Along the
way:

- **Cumulative time** `cum_dt` (years) advances with every step; the **@360d
  endpoint** is captured at the *first* step with `cum_dt ≥ 0.95` years
  (= 346.75 d) — no upper bound, so 7/75 eyes are actually scored at 450–720 d
  (accepted for Mai-comparability; must be stated in the thesis). The per-eye
  realised horizon is recoverable from the per-step Mai records (`cum_dt_years`),
  so exactly-360 d subsets of the **growth-region and full-mask** Dice/IoU can be
  recomputed post-hoc from `mai/epoch_*.json`. The change-region *headline* cannot:
  `test_rollout_losses` keeps its per-eye values in local lists and returns only
  the cohort mean, so that subset needs the rollout NPZs — which at the canonical
  `SAVE_EVERY=1000` exist for the final epoch only, and therefore cannot give the
  late-epoch mean ± sd the reporting rule of §7.4 requires.
- **Persistence baseline, teacher-forced**: at each step the baseline predicts
  "no change from the *previous ground-truth* state" — snapshotted before the
  input is overwritten with the rolled prediction (an earlier bug read the model's
  own prediction as the baseline, making persistence look epoch-dependent). For
  the endpoint Dice metrics, persistence is "the baseline visit's mask, held
  constant".
- All per-step metrics are averaged per eye first, then across eyes (each eye
  counts once regardless of visit count); Mai *bin* means are deliberately
  per-prediction records, with `n_eyes` reported alongside.

`save_full_rollouts_npz` runs the identical rollout and writes
`viz/rollouts_e{epoch:04d}.npz` — on the `--save_every` cadence **plus the final
epoch**, so at the locked `SAVE_EVERY=1000` that is the final epoch only:
NaN-padded `pred_full`/`gt_full` arrays (N_eyes × T × C × 49 × 1024),
`valid_length`, and per-eye `dt_per_seq` / `cum_dt_per_seq`. It is the source for
the per-eye **image strips** (`plot_runs.py --mode strip`,
`practical/scripts/fig_rollout.py`). The per-eye rollout-curve and growth-rate
scatter figures read `mai/epoch_*.json` instead, which is why they work on every
run while the strips need an NPZ fetched with `MODE=pull-npz` (the 2026-08-17
prune removed every local NPZ).

## 7.3 Reference points and the arm table

Only two things here are "baselines" in the usual sense — the two that fix the
scale. Everything else is a *peer arm* of the survey (§0.2, §4b), reported on
one instrument so that no arm is privileged by how it is presented.

**The two that fix the scale.**

1. **Persistence** (predict no change) — its floor on the change-region metric
   is **0 by construction**, so every number below *is* the lift over "no
   progression". Built into every evaluation.
2. **The per-pixel floor** (`--hidden_layers 0`, arm B3) — the GNN's own class
   with message passing switched off. It is **measured, not assumed**: exactly
   0.0000 on all five folds, bit-identical to persistence, against 0.4529 ±
   0.0403 for a single ring of neighbours (T8, the locality cliff). This is
   what licenses reading every point of change-region Dice as coming from
   spatial context.

**Two internal controls** that isolate a component rather than an architecture:
the **dual-branch bypass** (`--bypass_dmm_move`), which loads the DMM, runs the
second GNN and the full ItpNet round-trip but replaces the moved mesh with the
uniform grid — separating mesh *geometry* from the ~100 k extra trainable
parameters; and the **44×-capacity U-Net** (w32), which separates the
architecture-class effect from parameter count and resolves it against capacity.

**The arm table** — every architecture through the identical pipeline, 5-fold,
seed 42, late-epoch mean ± sd of `change_region_dice_360d`, ranked. Cost is
`curve_sec_per_epoch_min` with its fold, order-of-magnitude only (§7.5 rule 2).

| arm | `--backbone` | params | 5-fold mean ± sd | s/ep | row |
|---|---|---:|---|---:|---|
| T-FEN, 45-day RK4 steps | `fen` | 68,503 | **0.5337 ± 0.0453** | 364 [f0] | T8f |
| **Dilated-stencil GNN (locked)** | `anisognn` | 67,147 | **0.5258 ± 0.0497** | 91 [f0] | T7j |
| Stencil GNN + RK4 | `anisognn` +`--integrator` | 67,147 | 0.5139 ± 0.0497 | 439 [f0] | T9 |
| U-Net, parameter-matched | `unet` w5 | 83,081 | **0.5046 ± 0.0632** | 21 [f2] | T7 |
| Localized-kernel FNO | `fno` `--fno_local_kernel 3` | 79,960 | 0.4984 ± 0.0398 | 29 [f3] | T7d |
| FNO + RK4 | `fno` +`--integrator` | 79,160 | 0.4893 ± 0.0398 | 45 [f0] | T9b |
| FNO | `fno` w5 | 79,160 | 0.4831 ± 0.0477 | 23 [f4] | T7c |
| FEN, free-form only | `fen` `--fen_transport False` | 34,785 | 0.4810 ± 0.0348 | 180 [f0] | T8f |
| Graph U-Net | `gunet` w7 | 72,713 | 0.4784 ± 0.0478 | 47 [f2] | T9 |
| U-Net, capacity control | `unet` w32 | 3,354,347 | 0.4566 ± 0.0526 | 35 [f2] | T7b |
| k-NN GNN, k=20 | `gnn` `--neighbors 20` | 75,339 | 0.4519 ± 0.0436 | 108 [f2] | T9 |
| **k-NN GNN (v1 comparison arm)** | `gnn` `mean_max` | 75,339 | 0.4515 ± 0.0429 | 75 [f2] | T1 |
| Dual branch (moving mesh) | `gnn` `--moving_mesh True` | 175,663 | 0.4501 ± 0.0326 | 759 [f0] | T4 |
| Bypass control | `gnn` `--bypass_dmm_move` | 175,663 | 0.4503 ± 0.0324 | 718 [f0] | T4 |
| Per-pixel floor | `gnn` `--hidden_layers 0` | 14,795 | **0.0000 ± 0.0000** | 28 [f2] | T7b |
| Persistence | — | 0 | **0.0000** by construction | — | — |

Architectures, contract and parameter matching are in **§4b**; the readings,
instruments and caveats per row in **§7.5**; the full dated readouts in
[SOLVER_FINAL_RUNS.md](SOLVER_FINAL_RUNS.md) §5–§9.17 and the NOTES.md
*Thesis-bound results* table. **Read this as an ingredient measurement, not a
leaderboard:** the top three arms are mutually indistinguishable at the
available precision (§7.5), most adjacent pairs sit inside the floor, and what
the table is evidence for is which *components* move the number (§0.2). The
plain-RNN and transformer rungs of the locality ladder remain unimplemented.

**Measured status.** The single-branch CV of the **v1 k-NN comparison arm** is
complete at 5 folds × 2 seeds and gives the T1 number
**`change_region_dice_360d` = 0.4529 ± 0.0362**, against a persistence floor of 0 by
construction; fold is the dominant variance source (0.41–0.52) and the seed arm moves
the mean by only +0.0028. Since the **2026-09-03 v2 lock** the canonical uniform
branch is the dilated stencil with mean-only aggregation: `ANISOGNN_final_dilmean`
**0.5258 ± 0.0497** at seed 42 and **0.5279 ± 0.0419** at seed 7, i.e.
**+0.0743 ± 0.0083 SE over the k-NN arm on 5/5 folds** (seed-pooled per-eye
+0.0736 ± 0.0044, 144/150 eye-seed pairs) and statistically indistinguishable from
the param-matched U-Net (0.5046 ± 0.0632) at the mixed floor of §7.4 —
SOLVER_FINAL_RUNS §9.12b–e, NOTES row T7j.

All three **mesh** arms are complete at 5/5 folds (dual 2026-08-24, bypass
2026-08-28), all on the v1 backbone: single 0.4515 ± 0.0429, dual 0.4501 ± 0.0326,
bypass 0.4503 ± 0.0324. Paired dual − single = **−0.0013 ± 0.0086 SE** and — the
comparison the mesh chapter turns on, because the two arms differ in exactly one
thing — **dual − bypass = −0.0001 ± 0.0060 SE** (3/5 folds), the tightest null in
the project, with an SE less than half the 0.016 five-fold threshold (NOTES row T4).
No arm-to-arm delta here clears the ±0.0127 replicate floor (§7.4), which is why the
dual-branch finding is carried by that three-way single/dual/bypass null plus the α
trajectories (§5.1) rather than by any single Dice comparison. Tables:
[SOLVER_FINAL_RUNS.md](SOLVER_FINAL_RUNS.md) §5–§5d.

## 7.4 Model selection

`best.pt` is selected by **max `change_region_dice_360d`** (fallback: full-mask
Dice if the change region is empty for an epoch; SWE legacy used −train RMSE).
The fallback is **cross-scale-guarded** (2026-08-15, F10.11): the fallback label's
~0.87 scale and the primary's ~0.5 scale are not comparable, so a fallback epoch
winning once would have set an unbeatable bar — the rule is same-label plain max,
a primary-label candidate always displaces a fallback-label incumbent, and a
fallback candidate never displaces a primary incumbent.
`metrics.jsonl` (one JSON line per epoch, every metric above) is the authoritative
per-epoch record. Selection caveat carried in the results docs: at n = 12–20
validation eyes the epoch-to-epoch sd of the headline metric is 0.02–0.10, so
best-epoch selection is noisy — thesis tables should report **late-epoch mean ± sd**
rather than the peak.

**The replicate noise floor (2026-08-17) — the reporting rule everything else hangs
off.** Seven same-config / same-fold replicate pairs — **two same-seed** pairs on
fold 2 (the ladder-vs-CV overlap) and **five cross-seed** pairs (the seed-42 and
seed-7 CV arms) — give a **per-run sd ≈ 0.0127** on the late-epoch mean of
`change_region_dice_360d` (E|X−Y| = 2σ/√π). The
thresholds that follow: a **single-fold** delta needs |Δ| > **0.036** to clear 2σ, and
a **5-fold paired** mean needs > **0.016**. Anything smaller is run-to-run noise and
must not be reported as an effect — five previously reported single-fold deltas (L3s4,
L5nopad, L7combo, 6×128, and the fold-2 +0.035 for `nodts`) were retracted on exactly
this basis, and the `euler_dt_scale` ablation was declared a null against it (§4.5).

**These floors are measured on GNN replicate pairs.** The param-matched U-Net's own
seed pair spreads ~1.9× wider (fold-paired rms 0.027 vs the GNN's 0.014), so any
comparison involving a U-Net arm is read against a **mixed paired floor of ≈ 0.020**
(single-fold ≈ 0.046–0.05) — which is why the dilated stencil, `dilmean` and the
T-FEN are reported as *indistinguishable from* the U-Net rather than ahead of it
(SOLVER_FINAL_RUNS §9.12a–b and §9.15; NOTES rows T7i / T7j / T9b).

One consequence carries into the thesis unchanged: **nulls are unaffected** — noise
only widens a null, so every null result in this project survives the tighter floor.
A second one was **withdrawn**. On the original two same-seed pairs the cross-seed
spread (mean |Δ| 0.0117 on the `dts`-vs-`s7` arm) looked *smaller* than the same-seed
spread (0.0207), which was read as GPU nondeterminism dominating seed choice. Five
further same-seed pairs (the duplicated `gnormmeans7` array, 2026-09-02, mean |Δ|
**0.0070**) bring the pooled same-seed spread to **0.0109**, against **0.0135** pooled
over the five cross-seed arms now on record — so the two are indistinguishable and the
specific ordering no longer holds; seed choice adds nothing measurable on top of
run-to-run nondeterminism, but neither source can be ranked above the other at this
sample size. The floor itself was deliberately **not** re-estimated over all twelve
pairs (SOLVER_FINAL_RUNS §9.11a). The seed arm still moves the 5-fold CV mean by only
+0.0028 (0.4515 → 0.4543). Epoch-paired SEs are optimistic (epochs within a
run are autocorrelated); the replicate pairs are the honest yardstick. Derivation:
[SOLVER_FINAL_RUNS.md](SOLVER_FINAL_RUNS.md) §5.

**The second instrument: the pooled per-eye paired test.** Verdicts from 2026-08-25
onward are quoted on *two* instruments; the fold-paired mean above is the first, and
this is the second. It is the **Mai growth-region Dice** (followup ∩ ¬baseline, §7.1) taken at
each eye's **first rollout step with `cum_dt ≥ 0.95 y` (= 346.75 d)** — the same @360d
anchor `test_rollout_losses` uses, read from `mai/epoch_*.json` — averaged over late
epochs (≥ 10) per eye, then paired arm-vs-arm and pooled over the five folds'
validation cohorts: **75 unique eyes**, or 150 eye-seed pairs for a two-seed arm, with
a leave-one-fold-out robustness check. Its definition was not recorded when it was
first used and was recovered by reproduction; it was validated against the
U-Net − GNN anchor (**+0.0504 ± 0.0094, 55/75 eyes, t = 5.36**), and two rival
candidate definitions (the eye's *last* rollout step, and the mean over all steps)
were rejected because they do not reproduce that anchor (SOLVER_FINAL_RUNS §9.8b).
Note it is **growth-region** (asymmetric) Dice, not the change-region headline —
the headline is stored only as a cohort mean (§7.2), so it has no per-eye analogue
without the rollout NPZs. **Reporting rule:** quote the fold-paired mean and the
per-eye test together, and treat a result as graduating only when both agree. T7d
is the standing precedent for why: the 3×3 kernel's own effect reads
+0.0153 ± 0.0110 fold-paired — under the 0.016 paired floor — while the per-eye test
reads +0.0190 ± 0.0070 (48/75 eyes) and graduates, so the two instruments genuinely
disagree and only quoting both is honest. T6 (covariates) makes the separate point
that a fold-paired mean can be **fold-heterogeneous**: +0.0198 ± 0.0140 with one
fold carrying ~60 % of it, against a per-eye +0.0190 ± 0.0080 (43/75, t = 2.36)
that does *not* survive leave-one-fold-out (dropping fold 4 leaves +0.0089,
t = 1.11). T6 graduates on neither instrument.

## 7.5 Results summary: the thesis-bound rows, with their instruments

The authoritative record is the *Thesis-bound results* table in
[NOTES.md](../../NOTES.md) — one row per result, with its run ids, config, producing
tree and full caveat list — and the dated readouts in
[SOLVER_FINAL_RUNS.md](SOLVER_FINAL_RUNS.md) §5–§9.15. This section is the index: what
was measured, on which instrument, and what may be said about it. Every figure below is
the late-epoch mean of `change_region_dice_360d` over `epoch ≥ 10` (§7.4), recomputed
from [solver_results.csv](solver_results.csv) and the runs' own `mai/` records for this
summary.

**Read every line against the two instruments and the floors of §7.4**: fold-paired
5-fold mean ± its between-fold SE, judged against **0.016**; the pooled per-eye test over
**75 eyes** (150 eye-seed pairs for a two-seed arm), judged with leave-one-fold-out; and
a **mixed floor of ≈ 0.020** whenever a U-Net arm is one of the two sides. A result
graduates only when both instruments agree.

| row | comparison | fold-paired (5 folds) | per-eye (75 eyes) | reading |
|---|---|---|---|---|
| **T1** | single-branch v1 k-NN GNN, absolute | **0.4529 ± 0.0362** pooled over 2 seeds × 5 folds | — | The reference number for the pre-lock model; persistence is 0 on this metric by construction. Fold (0.41–0.52) is the dominant variance source; the seed arm moves the mean by +0.0028. |
| **T4** | dual − bypass (and dual − single) | **−0.0001 ± 0.0060** (3/5); dual − single −0.0013 ± 0.0086 | null | The mesh-specific measurement, parameter-matched: the tightest null in the project, SE less than half the threshold. Scope it as *the gated correction branch does not engage, mesh or no mesh* — not as "mesh adaptation does not transfer" (§5.1). Cost: ~10× the single-branch wall-clock. |
| **T5** | `--d_embed` 32 / 64 / 128 / 256 − encoder off | **−0.0015 / +0.0006 / −0.0008 / +0.0034** | all four negative, none over noise (32–40/75 eyes) | The learned surrogate encoder buys nothing at any width over an 8× range, with no monotonic trend, at 30–55 % more compute. Caveat: measured on the encoder *as built*, whose stride schedule corrects only ~2× of the image's 21.335:1 acquisition-spacing anisotropy (§4.6). |
| **T6** | covariates removed − covariates on | **+0.0198 ± 0.0140** (3/5, one fold carrying ~60 %) | **+0.0190 ± 0.0080** (43/75) | The two instruments **agree** here (+0.0198 fold-paired vs +0.0190 per-eye) and T6 **graduates on neither**: the fold-paired mean is fold-heterogeneous (one fold carries ~60 %) and the per-eye test does not survive leave-one-fold-out (drop fold 4 → +0.0089, t = 1.11). The defensible claim is that age and sex contribute nothing detectable and the residual points against them — not that the conditions are equivalent. Age encoding (`baseline` vs `per_visit`) is a clean null, +0.0045 ± 0.0042. |
| **T7** | U-Net w5 − v1 GNN | **+0.0531 ± 0.0226** (4/5) | **+0.0504 ± 0.0094** (55/75, t = 5.36) | The param-matched countermodel beats the then-locked GNN, at ~1/3 the wall-clock. **Replicates at seed 7 — but quote the same-seed pairing, +0.0655 ± 0.0209 fold / +0.0618 ± 0.0103 per eye (60/75), not the +0.0684 / +0.0641 that §9.6e's table reports against the *seed-42* GNN**, or this row is not comparable with T7j's stencil replicate, which is same-seed (§0.2). Fold-level t = 2.35 (p ≈ 0.08, df 4) and fold 3 reads −0.022, so the effect is fold-heterogeneous: quote the paired mean with its SE *and* the per-eye test. This per-eye figure is the anchor the instrument itself was validated against (§7.4). |
| **T7b** | U-Net w32 − U-Net w5; per-pixel floor | **−0.0479 ± 0.0303** (1/5); floor **0.0000** on all five folds | w32 − w5 negative (17/75) | **Capacity reverses the win**, which is what makes T7 an architecture-class result rather than a parameter-count one. The 0-layer floor is bit-exactly persistence and flags the whole validation cohort as identical to baseline. ⚠️ w32-vs-GNN is *metric-dependent* (fold-paired +0.0052, null; the per-eye instrument reads it as worse) — both agree it does not beat the GNN, only "level with" vs "below" is instrument-dependent; NOTES row T7b carries the detail. |
| **T7c** | FNO − v1 GNN; FNO − U-Net w5 | **+0.0316 ± 0.0259** (3/5); −0.0215 ± 0.0139 (1/5) | +0.0225 ± 0.0142 (40/75); **−0.0279 ± 0.0111** (30/75) | FNO sits *between* the GNN and the U-Net. Its lead over the GNN does not survive leave-one-fold-out on either instrument (fold 4 carries ~77 %) and is **not established**; "FNO < U-Net" is. Reading: global spectral support alone does not reproduce the U-Net's advantage at the 360-day anchor. |
| **T7d** | B4c (FNO + 3×3 bypass) − v1 GNN; − FNO; − U-Net w5 | **+0.0470 ± 0.0160 (5/5)**; +0.0153 ± 0.0110; −0.0061 ± 0.0108 | **+0.0414 ± 0.0115** (47/75); **+0.0190 ± 0.0070** (48/75); −0.0089 (33/75) | The minimal global+local hybrid is the only arm to beat the GNN on *every* fold, and it **ties** the U-Net. With T7c this is the project's central architectural claim: context and local detail are separable ingredients and both are required — two architecturally unrelated global+local constructions land indistinguishable at matched capacity (SOLVER_FINAL_RUNS §9.8e–f). The kernel's own effect graduates on the per-eye instrument but not on the fold-paired one — quote both. |
| **T7e–T7g** | per-graph norm; mean aggregation; norm-site density; edge-feature arms | gnorm **+0.0146 ± 0.0074**; aggrmean +0.0108 ± 0.0039; D2 − gnorm +0.0081 ± 0.0087; D1 +0.0023 ± 0.0043; D1b −0.0099 ± 0.0056 | gnorm +0.0129 ± 0.0060 (42/75); D1b −0.0080 ± 0.0031 (28/75) | Every GNN-internal knob is under its floor. The normalisation axis is **closed** (including the C2 aggregation × norm pairing, which reached +0.0196 at seed 42 and failed to replicate at seed 7), and so is the direction axis in both directions — making the geometry, not the message function, the thing that mattered (§4.3, §4.3b). |
| **T7i / T7j** | dilated stencil − v1 GNN (the v2 lock) | **+0.0691 ± 0.0116 (5/5)** at matched `mean_max`; **+0.0743 ± 0.0083 (5/5)** with mean-only; seed-7 replicate **+0.0736 ± 0.0162 (5/5)** | **+0.0752 ± 0.0054** (74/75, t = 13.9); seed-pooled +0.0736 ± 0.0044 (144/150) | The largest effect in the project, at **0.89× the parameters**, from changing only `data.edge_index`. It leaves the model **statistically indistinguishable from the param-matched U-Net** at the mixed floor — never "ahead of" it. Reach ladder at 5 folds: ±12 columns −0.0193 ± 0.0083, ±42 columns −0.0256 ± 0.0040, so the ±21-column default is a measured optimum ≈ 0.12 mm. |
| **T8** | 0 / 1 / 2 message-passing layers | **0.0000** · **0.4529 ± 0.0403** · 0.4515 ± 0.0429 | 1-layer − 2-layer null (39/75) | The locality cliff, within-era: one ring of neighbours buys everything, the second buys nothing. Every point of change-region Dice comes from spatial context, and the GNN saturates at one hop — which is why what the dense arms add is multiscale *reach*, not more locality. |
| **T8n / T9 / T9b** | RK4 − one Euler step (stencil GNN); FNO + RK4 − FNO | **−0.0119 ± 0.0037** (1/5); **+0.0062 ± 0.0056** (4/5) | −0.0132 ± 0.0055 (28/75); +0.0064 ± 0.0069 (43/75) | Time-integration order buys nothing on a local graph operator or on a global spectral one, at ~4.8× the wall-clock for the former. ⚠️ Dice at the endpoint is **binarised and blind to the trajectory**, so accuracy alone licenses no "ODE" claim either way — but the Ott/Krishnapriyan solver-swap diagnostic **ran 2026-09-17** (T10, §4b.6, §9.17) and settles it: the locked model **fails** (Dice spread 0.0856 across inference schemes, Euler refinements diverging) and the autonomous-RK4 arm **passes** (0.0044). The continuous-time reading belongs to that arm and to no headline result — and that arm is this row's null, so the ODE property is obtainable and buys nothing. |
| **T8f / T9** | T-FEN − free-form FEN; T-FEN − locked model; T-FEN − U-Net w5 | transport **+0.0527 ± 0.0065 (5/5)** at seed 42, **+0.0495 ± 0.0081 (5/5)** at seed 7; vs locked +0.0079 ± 0.0077 (3/5); vs U-Net seed-pooled +0.0199 ± 0.0085 (8/10) | transport **+0.0555 ± 0.0057** (65/75, t = 9.68); vs locked +0.0050 (43/75, t = 0.79); vs U-Net seed-pooled +0.0218 ± 0.0053 (97/150) | **The transport term is established and is the project's strongest mechanism result**: an explicit advection operator, only ~4–5 % of the rate magnitude, recovers the near-term (0–1 y) growth-region bin from the one-hop level to the dilated stencil's own value — two unrelated constructions reaching the same place, which is §4.3b's reach finding reproduced and sharpened into a *transport* deficit. ⚠️ **This is the one architecture comparison in the table that is NOT parameter-matched, and that must be said whenever the +0.053 is quoted:** the control is the same network with the velocity head deleted — a purely additive ablation, both heads zero-init, so the arms start as the same function — but that head is 33,718 parameters on top of a 34,785-parameter free-form term, i.e. **68,503 vs 34,785, a factor of 1.97×**, and a width-≈139 matched-capacity control has never been run (§4b.7). Against the capacity reading: capacity is a measured null on every other axis here (T7b, T8, T5), and the effect is concentrated in the near-term bin rather than diffuse. T-FEN **ties** the locked model at the anchor; against the U-Net its leave-one-fold-out minimum sits under the mixed floor, so that too is indistinguishable, not a win. The anchor tie hides opposite horizon profiles — the horizon rows must travel with any anchor table. |
| **T8g** | decay-free gated machinery (`--moved_weight_decay 0`) | +0.0092, fold 2 only | +0.0092, fold 2 only | Under the 0.036 single-fold floor. Together with the mechanism read-out (α peaks *lower* without decay; `param_norm/moved` **grows**) this refutes weight decay as the cause of α → 0 and extends T4's scope to *"mesh or no mesh, decay or no decay"* (§5.3, §6.4). |
| **T9b** | the 45-day T-FEN's numerical validity | — | — | **Not a Dice result and not optional.** At 5 folds × 2 seeds the free-running rollout diverges on 5/10 runs and 9/10 *final* checkpoints exceed the explicit scheme's Courant bound on at least one advected channel. One-step error is healthy and every binarised metric is unaffected, so no anchor above changes — but **the learned velocity map is not quotable** and the arm as trained is not a valid long-horizon integrator (§4b.7, §9.4). |
| **T10** | the solver-swap (ODE-validity) diagnostic | — (fold 2, post-hoc, 0 GPU-h) | — | **Not a Dice result either — it is what licenses or refuses the vocabulary.** Re-evaluating a trained checkpoint under euler *n* ∈ {1,2,4} and rk4 *n* ∈ {1,2}: the **locked model fails** (spread **0.0856**, 2.4× the single-fold floor, Euler refinements growing) and the **autonomous-RK4 arm passes** (four refined settings within **0.0044**). So no "ODE", "rate field" or "learned dynamics" sentence is licensed for the locked model or any headline result, and a continuous-time reading belongs to arm N1 alone — which is a 5-fold null on accuracy at ≈4.8× the cost. The ODE property is real, obtainable, and worth nothing on this task (§4b.6, §9.17). |

**Three framing rules that follow from the table.**

1. **Never quote raw RMSE across arms.** The clinical metrics binarise, and the dense arms
   decalibrate far more under autoregression than the GNN does (the U-Net's late rollout
   mask RMSE is roughly twice the GNN's while its binarised metrics are better). Raw-scale
   comparisons across backbone classes measure the decalibration, not the prediction.
2. **Quote cost as `curve_sec_per_epoch_min` — the minimum epoch of the cheapest fold —
   and name the fold.** The *mean* epoch time carries a near-constant additive overhead
   (17–64 s across arms whose base epoch spans 30–480 s), so it systematically penalises
   cheap architectures; and per-fold work is not constant, because an epoch is
   20 × ⌈n_train_eyes / 4⌉ optimizer steps. Current values (fold in brackets): U-Net w5
   **21** s/epoch [f2], FNO **23** [f4], per-pixel floor **28** [f2], B4c **29** [f3],
   U-Net w32 **35** [f2], graph U-Net **47** [f2], v1 k-NN GNN **75** [f2], **locked
   stencil 91** [f0], free-form FEN **180** [f0], T-FEN **364** [f0], RK4 over the
   stencil **439** [f0], dual branch **759** [f0]. Same-config replicates on the same
   fold still differ by up to 1.29×, so these support order-of-magnitude statements only
   — but the three headline ratios are estimator-independent (dual/single ≈ 10×,
   RK4/Euler ≈ 4.8×, T-FEN/stencil ≈ 4×). The one figure that moves materially with the
   estimator is the U-Net's: **0.23×** the locked stencil under the minimum, against
   0.52× under the mean — the mean was *understating* how much cheaper it is.
3. **Compare within an era.** Everything in this table is `final`-era (§9.1); pre-fix runs
   are not comparable with it, and the dual-branch runs from before the 2026-08-06 edge
   fix are void outright.

> **⚠️ CORRECTION 2026-09-17 — the GPU co-scheduling mechanism is REFUTED; the procedure (quote the minimum) stands.** A post-hoc audit of all 227 indexed run directories (slurm `NODELIST` / `CUDA_VISIBLE_DEVICES` / start-time `nvidia-smi` headers, run-dir timestamps, per-epoch `epoch_time`) finds **264 run pairs sharing a node concurrently and 0 pairs ever sharing a GPU index**; the assigned card held another job's memory at launch in 1 run of 227; within a run, epoch time does not track node occupancy (Spearman median +0.02, positive in 105 of 200 runs); and all 227 ran on an RTX A6000, so the node's two Ada cards never entered. The spread has two real causes instead. **(i) Per-fold work is not constant** — `passes_per_epoch` counts loader passes and `len(dataset)` is the fold's eye count, so an epoch is 20 × ceil(n_train_eyes / 4) = 280 / 320 / 300 / 300 / 320 steps for folds 0–4; normalised by that, the per-fold ratio of the minimum epoch time is 1.000 / 1.017 / 0.977 / 0.998 / 0.968, flat to 3 %. **(ii) The per-epoch excess over a run's own floor is additive** (a near-constant 17–64 s across arms whose base epoch spans 30–480 s), so the *mean* penalises cheap architectures. Quote **`curve_sec_per_epoch_min`** and name its fold. The three headline ratios are unchanged; the U-Net moves from 0.52× the stencil GNN (mean) to **0.23×** (minimum, and 0.23× per optimizer step). Full resolution: the 2026-09-10 TODO in [NOTES.md](../../NOTES.md) and `solver_results.columns.md` convention 4.

# 8. Reproducibility infrastructure (brief)

- **No YAML config system.** Configs are CLI arguments, captured into the run
  directory as `args.json` at run start (and, for the DMM, re-used as defaults on
  resume — solver resume is disabled, §6.5); the run directory *name* encodes the
  key hyperparameters (§3.5 for DMM, §6.5 for the solver), so a run is
  identifiable from a directory listing and reproducible from name + `args.json`
  + git SHA. **Since 2026-09-02 (commit `85bb2e0`) the solver stamps that SHA
  itself**, as `code_sha` (plus `code_dirty_files`) in `args.json`:
  `jobs/sync_push.sh` writes `git rev-parse HEAD` — with a `-dirty` suffix and the
  porcelain file list — into the gitignored `GraphPDE/.code_sha` before every
  rsync, because the cluster checkout has no `.git`, and `train.py` reads it back
  at run start (`dmm.py` does not). Runs from before that commit carry no SHA
  (195 of the 262 rows in `solver_results.csv`) and are dated only by their
  run-directory timestamp, bracketed against the commit log — which is why the T1
  thesis-bound row records its SHA as "not recorded in the artifacts" while T7j
  onward quote it directly.
- **Determinism**: `--seed` (canonical 42; reproducibility legs at 7 and 2024)
  drives Python/NumPy/torch/CUDA; `cudnn.deterministic = True`,
  `benchmark = False` in both trainers.
- **Environment**: pinned container `pytorch-2.4.1-cu121-cudnn9-runtime.sif`
  (PyTorch 2.4.1 + CUDA 12.1); local runs use the matching `MPPDE` conda env. New
  dependencies require explicit justification (hard rule).
- **Cluster workflow**: all Slurm scripts live in [jobs/](../../jobs/) in the repo —
  *edit locally, rsync to the cluster, never edit cluster-side*. Two scripts per
  side: `train_solver.slurm` / `launch_solver_search.sh` and `train_dmm.slurm` /
  `launch_dmm_search.sh`; the 5-fold CV is a Slurm job array
  (`ARM=sb|dual|bypass sbatch --array=0-4 train_solver.slurm`). Launchers carry
  preflight checks that refuse to submit against stale templates (a stale template
  silently drops flags).
- **Provenance**: both trainers write `dataset_provenance.json`, but the key sets
  differ. The **solver** records fold, split/window counts, covariate mode, norm
  method and — since 2026-08-15 — the graph's actual `edges_per_node` +
  `edges_source` (`file` vs `runtime_knn`, which distinguishes a runtime-rebuilt
  kNN graph; the canonical v2 stencil backbone instead records
  `aniso_stencil:<label>` plus `aniso_geom`, since it replaces the kNN graph
  entirely, and the Neural-ODE wrapper adds `integrator`). The **DMM** records its
  source fold, mask source, grid, training-split scope + mask counts and
  `eval_in_train`, and carries no covariate, norm or edge fields. Both exist
  because the container mounts every fold at one
  generic path; the solver additionally records the frozen DMM's content hash.
  DMM resume validates its side; the solver-side gates are dormant behind the
  resume disable.
- **The committed results harvest** — results are read from two committed CSVs, not
  from the run trees: [solver_results.csv](solver_results.csv) (262 solver runs as
  of the 2026-09-11 harvest — see
  [solver_results.columns.md](solver_results.columns.md) for the current row count;
  regenerated by `collect_solver_results.py --include_archive --carry_deleted`) and
  [dmm_results.csv](../mesh/demos%20&%20explanations/dmm_results.csv) (55 native DMM
  runs, `collect_dmm_results.py --rescore`). Each ships a `*.columns.md` data
  dictionary carrying the reading conventions — quote `late_*_mean ± sd`, mind the
  replicate floor (§7.4), compare only within an era. This is not merely a
  convenience: `GraphPDE/results/` and `mesh/experiments/` were pruned on 2026-08-17,
  and rows whose run directory is gone are retained and flagged `flag_run_deleted`,
  for which the CSV is the only surviving record. Quick figures come from
  `plot_runs.py` (solver) and `plot_mesh.py` (DMM); both write to a gitignored
  `plots/` beside them.
- **Thesis-bound numbers rule** (hard rule): any metric that reaches the thesis
  must be reproducible from a committed config + recorded run-id + git SHA, logged
  in NOTES.md "Thesis-bound results"; changed numbers are appended, never
  overwritten; missing numbers stay missing (no invention).

---

# 9. Chronology of load-bearing fixes — what it took to make this work

This section exists because the framework's final shape is largely the product of
diagnosed failures. Each entry: problem → fix → what it invalidated. Full audit
trail in [NOTES.md](../../NOTES.md).

## 9.1 Era boundaries (which results survive)

| boundary | cause | consequence |
|---|---|---|
| 2026-05-23 | uniform-graph k-NN anisotropy fix (precompute) | every earlier GA precompute regenerated; every earlier `best.pt` selection invalid (was min-train-RMSE) |
| 2026-07-05 | conv1d decoder → MLP | all earlier solver checkpoints unloadable |
| 2026-07-19 / 07-25 | divergence fix (norm/α/PoU) + res_cut removal | solver checkpoints invalidated again |
| **2026-08-06** | **moved-graph iso_edges fix** | **every dual-branch result ever produced before it is void** — including the first 5-fold CV (dual losing on 4/5 folds) and the α-gate study; the moved branch had been structurally incapable of 2-D message passing |
| 2026-08-07/08 (+08-12) | 180-day curriculum + LR-milestone decoupling + per-module clipping + ItpNet-pretrain identity objective (08-08); the pretrain gradient clip followed on 08-12 | pre-fix solver runs are a separate "era"; single-vs-dual comparisons are valid only within an era; the final thesis batch runs entirely post-fix |
| 2026-08-09 | SLO crop mis-registration (audit C1) | historical SLO-DMM mesh numbers remain *internally* valid but carry an unquantified registration error — thesis DMM claims scope to the native path |
| **2026-08-14/15** | per-graph soft-Dice hard-wired (train AND eval) + per-graph monotonic penalty; pad-aware border/interior eval columns + `_anat`; scorer `ref_pad` → replicate | runs across this boundary are only comparable **at the same objective**; the eval-side weighted `ts_mse`/`ts_rmse` columns and the border/interior columns changed scale/definition (border split: 4/12 → 6/10 on split-2 val); mesh scores compare only within one `ref_pad` (stamped per row). Also discovered: the fold-3 `MPPDE_ARCH_F3_K24` leg never changed k, so its "+0.001" measured nothing but run-to-run noise. **Superseded 2026-08-17 on both counts:** that single pair understated the real spread ~20× — the replicate floor is now **per-run sd ≈ 0.0127** from 7 same-config pairs (§7.4) — and the k-axis itself **has since run** on the new-era stack (Stage F1b `K24`, at the locked loss on a runtime-rebuilt k = 24 graph): **+0.0086 ± 0.0053 SE, 12/20 epochs, a null** |

**Nothing after 2026-08-14/15 is an era boundary.** The 2026-09 changes (§9.2
#30–#32) are either default-preserving additions — the Neural-ODE wrapper is not
built at the default euler/1 substep, the new backbones are opt-in `--backbone`
dispatch — or, in the case of the 2026-09-03 v2 lock, a change of *which
configuration is canonical* rather than of what any earlier run computed. Every
pre-09-03 number stands as measured; it is now the `--backbone gnn` comparison arm
rather than the headline.

## 9.2 The fix log (condensed)

**Making the DMM trainable on GA (2026-05):**
1. *Monitor NaN* — the z-scored binary mask's step gradients spiked the monitor to
   ~1800 and NaN'd the Monge–Ampère second-derivative chain on the first GA run →
   Gaussian mask blur, monitor-side only (§3.3). σ = 0 ablation collapses the mesh:
   load-bearing.
2. *Memory / interpolation kernel* — 50 176-point grids OOM'd the per-point
   interpolation → the interpolation was chunked along the batch dim (2026-05-03,
   verified bit-exact) and later given batched/broadcast call sites (2026-05-10,
   bit-identical). Separately, the soft nearest-neighbour kernel was replaced by
   bilinear `grid_sample` (2026-05-08, `36c2da8`) — a **deliberate behaviour
   change**, not a bit-exact rewrite: the softmax kernel spanned ~1 px along the
   long axis but ~21 px along the short one on 49 × 1024, smearing the
   lesion-boundary signal. It also removed the need for the chunked loop.
3. *Square-SLO pivot* — the first working GA-DMM trained on the 256² SLO mask,
   dissolving a stack of workarounds (replicate-pad, `--curriculum_epochs`, and —
   on a single-channel mask — the mask-only Frobenius selector, which became an
   auto no-op and was removed 2026-06-30). log-compression was reverted here too,
   but that classification was wrong: it was restored after the `NOLOG1P` ablation
   and is **canonical ON** (#4, §3.3). Replicate-pad likewise returned
   flag-gated on 2026-08-09 as `--monitor_mask_pad` (default still `zeros`). The
   pivot was later understood to have been unnecessary as a *grid* change (the blur
   was the real fix), and is superseded by the native path.
4. *Monitor shape ablations* — log1p compression proved required (linear monitor:
   fold-overs), and reducing the uniform sampling fraction to f = 0 collapsed the
   mesh toward a near-affine map (NB per audit B5, that leg still drew ~20 % uniform
   points through the sampler's chunk remainder — a true importance-only condition
   has never been run; §3.5).

**Making the solver learn anything real (2026-05):**
5. *First end-to-end run*: a metadata wrap silently dropped the Δt time-encoding
   (crash), and the inherited conv head required `hidden_dim ≥ 113` (crash).
6. *A broken persistence baseline* made the model look worse than persistence — the
   baseline was accidentally reading the model's own rollout; fixed
   (teacher-forced snapshot).
7. *Copy-input collapse* — the single-branch model produced **bit-exact**
   thresholded copies of its input mask on all 16 validation eyes; on that run the
   residual could not flip a single pixel, so MSE on a z-scored binary mask gave it
   no usable gradient at the saturated values. Audited as loss design, not a bug.
   Fix stack: mask channel weight, **soft-Dice auxiliary** (gradient in the
   binarisation band), later the **monotonic penalty** (clinical prior). The
   collapse counter (§7.1) still guards it. **Re-tested on the repaired stack**
   (F1 ladder, 2026-08-15, fold 2): mask-channel weighting *alone* escapes — L1
   (mask ×5, no Dice) 0.4885 equals L2's 0.4963 within the replicate floor — and
   raw MSE (L0) also escapes, late, at epoch 26. What soft-Dice buys is immediate
   escape and roughly half the epoch-to-epoch sd, not a better final score; it
   stays in the locked loss at 5.0 @ sharpness 2.0. The monotonic penalty has no
   effect (L4mono −0.0032) and is **locked at 0.0** (§6.1, §9.4). The 2026-05
   diagnosis and the ladder differ because that run also predated the rank-1
   decoder removal, the index-space edge fix and the BatchNorm→LayerNorm
   train/eval-parity fix (#12, #8, #16).
8. *k-NN anisotropy #1* — physical-mm k-NN put 100 % of neighbours in the same
   B-scan row → index-space edges (§2.5).
9. *Metric + selection* — full-mask Dice floor ~0.87 hid all signal; introduced
   **change-region Dice** (persistence floor 0) and switched `best.pt` selection to
   it (previously min *training* RMSE — which systematically selected collapsed
   late epochs).
10. *mean_max aggregation* — mean-only message passing was argued to be a diffusion
    prior biased against travelling fronts, so concatenated mean+max was made the
    default to let the update MLP route locally. **Superseded 2026-09-01/03 by
    measurement:** the max stream is strongly harmful *alone*
    (`MPPDE_aggrmax_f2` 0.3699 vs 0.5178 = −0.148, 4× the single-fold floor) and
    adds nothing in concatenation — mean-only ties `mean_max`
    (+0.0108 ± 0.0039 SE over 5 folds, under the 0.016 paired floor) at 11 % fewer
    parameters (67,147 vs 75,339). `--gnn_aggr mean` is the v2 canonical
    (§6.6); `mean_max` survives only as the argparse default so pre-09-03 runs
    reproduce flag-for-flag (ARCHITECTURE §0; NOTES row T7f). The max half is
    filed as a negative result in §9.3.

**Structural honesty fixes (2026-05/07):**
11. *SLO leak* — during pushforward/rollout the DMM was fed the *ground-truth
    future* SLO mask (unavailable at deployment) → replaced by a
    prediction-derived surrogate; the native path (2026-08-04) later dissolved the
    surrogate entirely (the branch reads the predicted mask channel directly).
12. *Rank-1 decoder* — the inherited Conv1d head collapsed the hidden state to one
    scalar per node before expanding to 11 channels → full-rank MLP decoder
    (§4.4).
13. *Time-budget unrolling* — unroll depth counted in visits meant different real
    horizons per eye → curriculum re-denominated in days (§6.2).
14. *res_cut removal* — the third composition term (a per-timestep CNN residual)
    was diagnosed as a compounding, state-aligned velocity (`≈ 0.8·u` added into
    the integrated velocity, nothing penalising its magnitude): it was the
    **primary of three defects** (with the BatchNorm train/eval mismatch and the
    un-normalised interpolation weights, #16) behind a run whose per-epoch
    **training** avg RMSE ran 3.3e5 → 5.4e9 → 1.2e12 once the 180-day budget
    entered at epoch 2. First default-off, then removed entirely.
15. *DMM full-cohort retrain + branch compaction* — train-split-only DMMs
    under-generalised and confounded the CV; conv7 overfits; `pool` canonical.

**The dual-branch divergence fix (2026-07-19, five coordinated changes):**
16. **α gate** (moved branch starts inert, must earn its contribution; α was
    designed as the headline measurement of whether mesh adaptation transfers, but
    the 5/5-fold parameter-matched **bypass** control — complete 2026-08-28 —
    shows α fails to open with the warp *ignored* just as it does with it (bypass
    peaks 0.031–0.101 against the dual arm's 0.058–0.093), and
    dual − bypass = −0.0001 ± 0.0060 SE, so what α measures is the correction
    branch's failure to optimise, not the mesh; §5.1, NOTES row T4);
    **partition-of-unity interpolation** with the
    sign-preserving row-sum floor (raw ItpNet weights had unbounded gain);
    **LayerNorm** replacing BatchNorm (train ≡ eval — BatchNorm was erasing the
    pushforward perturbation and poisoning eval stats; also: PyG's LayerNorm
    default mode would have re-coupled the batch — `nn.LayerNorm` chosen
    deliberately); **a real gradient clip** (the existing clip was a triple no-op);
    and the **zero-init deadlock** guard (α-gate and decoder zero-init multiply
    into exactly-zero gradients both ways — caught before it silently produced a
    fake "α → 0" negative result). Post-hoc additions: α excluded from weight decay
    (decay alone pulls α toward the pre-registered negative result), and the
    row-sum floor recalibrated on the real grid (the initial ε guard never fired).
17. *Dual-branch bring-up on the cluster* — three device-side assert fixes: moved
    meshes legitimately overshoot the domain (edges built on clamped coords), the
    container PyG resets `.batch` on cross-GPU clone (batch vector reconstructed),
    degenerate meshes make knn emit garbage indices (edge filter at point of use).

**The anisotropy again, and the optimizer honesty fixes (2026-08):**
18. **k-NN anisotropy #2** — `create_moved_graph` rebuilds its own edges and never
    inherited fix #8: the moved branch had 100 % same-row neighbours the entire
    time it existed. `iso_edges` fix; every prior dual-branch result void. The same
    defect existed a third time in ItpNet's stencil (54.7 % of query points drew
    all 30 neighbours from one row) → `iso_interp` + the k = 12 study.
19. **Curriculum arithmetic** — the 90-day budget quantum could never chain two
    visits (undershoot + 90-day minimum gap): 0/75 eyes unrolled at its first
    level, and the sampler silently fell back for 53/59 eyes → 180-day quantum.
20. **LR schedule accident** — `--unrolling` doubled as the first LR milestone
    (upstream inheritance), making every pushforward ablation a joint LR sweep;
    decoupled to `--lr_milestones [5, 20]` (the historical schedule was one drop
    at epoch 4 and then flat).
21. **Per-module gradient clipping** — the single joint clip let the *dual stack's*
    10³–10⁴× gradient norms rescale the uniform branch's updates ~1000×, so
    single-vs-dual compared two different optimisers. The joint scalar could not be
    decomposed at the time; the per-module logging this fix added measured **ItpNet**
    as the source at the canonical ×Δt operator, and the moved branch only at
    `--euler_dt_scale False` (§5.1).
22. **ItpNet pretrain** — was optimised with the full solver criterion (whose
    minimiser is not the identity: at the identity, soft-Dice was 100 % of the
    gradient) → dedicated identity objective; and it ran unclipped with a
    seed-dependent 43× first-step gradient spread → clipped.
23. **Native mask smoothing OFF** — the blur-rethreshold on the DMM's branch input
    fired at t₀ too, where it measurably weakened the mesh; A/B confirmed OFF is
    equal-or-better and far more stable.
24. **Resume/identity hardening** — two-phase resume (args merged before
    construction), dataset-identity and DMM-content-hash gates, provenance files,
    run-name data tags. Superseded for the solver by the outright **resume
    disable** (2026-08-15; the gates stay in source, dormant).

**The 2026-08-14/15 batch (review of the reviews' fixes + user-directed follow-up):**
25. **Per-graph objective completion** — soft-Dice per-graph hard-wired in train
    AND eval (`_crit_kw`); the monotonic penalty per-graph'd the same way (its
    pooled denominator diluted a small eye's penalty 101× by co-batched lesion
    sizes); B = 1 bit-identity to the pooled formulas verified. The F2a
    bootstrap-semantics question (previous frame = rolled prediction on unrolled
    passes, a 31.8× ratchet on the model's own false positives) is deliberately
    left to the ladder batch — whose closing `L4mono` leg settled it
    (−0.0032 ± 0.0033 SE, 7/20 epochs) and **locked the monotonic penalty at 0.0**
    (2026-08-15). At weight 0 `needs_bootstrap` is False and no bootstrap is passed,
    so F2a cannot affect the locked recipe; the design question itself stays open in
    NOTES.md.
26. **The K24 void + runtime-selectable k** — `--neighbors` was inert on
    single-branch runs (the uniform graph loads the precompute's edges), which
    silently voided the fold-3 K24 receptive-field leg as a same-config twin of
    its anchor. Fixed at the root: the dataset now derives the edge file's k
    exactly (E/N) and **rebuilds the kNN graph at the requested k at load time**
    with the precompute's own construction — verified bit-identical to the
    independently-built per-k artifacts — so one folder serves every k and the
    whole mismatch class (including a launcher env leak that defeated the interim
    stamp-guard) is closed at the load site. The silver lining — the K24/anchor
    pair as a same-config noise estimate — was **superseded 2026-08-17**: at n = 7
    replicate pairs the per-run sd is ≈ 0.0127, roughly 20× what that single pair
    suggested (§7.4). The k-axis itself re-ran clean in Stage F1b and is a null.
27. **Eval honesty for the crop** — pad-aware border/interior split (the crop
    ring is structurally blind for the 27 % of padded visits whose true FOV edge
    lies inside the crop) + the additive pad-masked `change_region_dice_360d_anat`
    column (pad-row predictions are training-free under `--exclude_pad_nodes` but
    were fully scored by the plain column — a one-sided ~0.05 artifact at 5–10 %
    pad drift, the size of the ladder's decision band; that is a **probe-level
    worst case with injected drift, not an observed one**: the two
    `--exclude_pad_nodes True` ladder legs show an `_anat` − plain gap of
    0.0045/0.0048, identical to the pad-trained L2's 0.0045, and across the five F3
    folds the gap never exceeds 0.005, so audit A3's pad-drift fear is refuted both
    directly and cohort-wide).
28. **`--euler_dt_scale`** — the ×Δt on the residual head made an ablation flag
    after the F6 measurement that it is a pure reparameterisation on the mask
    channel (§4.5); warm-start guards the flag via the checkpoint's saved args.
29. **Solver resume disabled; DMM resume repaired** — solver `--resume` raises
    (unused + three known-unsafe semantics); `train_dmm.slurm`'s canonical
    defaults are skipped on resume (they used to force 27 explicit flags that
    silently flipped a resumed non-canonical run to the canonical recipe).

**The 2026-09 batch (the third anisotropy, and the external method classes):**
30. **k-NN anisotropy #3 — physical reach.** The index-space fix (#8) restored
    cross-row *connectivity* but left neighbour *placement* ~21× anisotropic in
    millimetres: at k = 12 a hop reaches ±0.25 mm across rows and ±0.011 mm along
    columns, against a measured GA front advance of ~12 columns (q3 17, p90 23) per
    180-day visit. Replacing the edge geometry with a **dilated stencil** — rows ±1
    × columns {0, ±7, ±14, ±21}, ±0.12 mm on both axes, built at forward time
    around the *unchanged* GNN — lifts the same network by **+0.0691 ± 0.0116 SE at
    5/5 folds** (+0.0743 ± 0.0083 with mean-only aggregation), on 144/150 eye-seed
    pairs, at 0.89× the parameters. Locked as **LOCKED CONFIGURATION v2** on
    2026-09-03 with `--gnn_aggr mean`, seed-7 gate discharged the same day (§6.6).
    The k = 12 k-NN remains the *data* graph and the comparison arm; the reach
    optimum is a measured knee at ≈ 0.12 mm (§9.3). Depth, width and index-space k
    never bought this, which is why the old capacity grid read flat (§9.3).
31. **Stage F5 external countermodels** — a param-matched U-Net and a 44×-capacity
    control, FNO, the 3×3-bypass localized-kernel FNO hybrid, and a graph U-Net,
    all as 5-fold arms through `train.py --backbone`
    ([GraphPDE/baselines/](../baselines/)). The param-matched U-Net beats the k-NN
    GNN; capacity reverses that; and the stencil GNN, at 0.89× the GNN's
    parameters, is statistically indistinguishable from the U-Net at the mixed
    floor of §7.4 — never "beats" it (§7.3, SOLVER_FINAL_RUNS §9.6–§9.12).
32. **Time integration and a FEM backbone (2026-09-05)** — a fixed-step explicit
    Runge–Kutta wrapper over any backbone's `vector_field`
    ([baselines/odeint.py](../baselines/odeint.py); not built at the default
    euler/1 substep, so a flag-less run is bit-identical) and a **Finite Element
    Network** backbone ([baselines/fen.py](../baselines/fen.py); Lienen &
    Günnemann, *Learning the Dynamics of Physical Systems from Sparse Observations
    with Finite Element Networks*, ICLR 2022, arXiv:2203.08852). Integration order
    is a null on both a local graph operator and a global spectral one; the T-FEN
    ties the locked model at the anchor and its **transport term is established**
    (+0.050–0.053 at 5 folds, two seeds), but the 45-day variant's free-running
    rollout is not numerically stable at 5 folds — see the standing open item in
    §9.4 (arms N/FE/G, T8n/T8f/T8g/T9/T9b).

## 9.3 Refuted ideas (kept as citable negative results)

- **Intermediate-time-point regularisation** (supervisor's recipe): implemented,
  swept, no benefit on change-region Dice; removed.
- **Change-region per-pixel MSE boost**: no clear win; removed.
- **Anisotropic (physically-matched) monitor blur kernel**: no adaptation gain
  (p = 0.95), folded the mesh intermittently; not adopted.
- **det-Jacobian barrier penalty** (replacing the dormant convexity term): made
  tangling monotonically *worse*; not adopted.
- **`hard` DMM boundary constraint**: the wrapper was mis-specified (boundary
  pinned to 2ξ, ~74 % of queries out of domain); removed, historical run kept as
  evidence.
- **Surrogate bilinear resize**: built to smooth the SLO round-trip; the question
  dissolved when the native path removed the round-trip.
- **Receptive-field explanation of single ≈ dual**: an old-era 14-leg fold-3
  capacity grid (depth 1–12, width 32–256) is *flat down to 1×64*, which motivated
  the locked 2×64 capacity and the locality/inductive-bias chapter. Two caveats
  travel with it. Its `K24` leg was **void** (`--neighbors` was inert on
  single-branch runs — §9.1, §9.2 #26), so the grid never varied k at all; the
  k-axis first ran clean in Stage F1b (`K24`, fold 2, at the then-locked
  `euler_dt_scale False` loss: +0.0086 ± 0.0053 SE, a null)
  and again at 5 folds, where `k20` reads −0.0104 ± 0.0051 SE (1/5 folds) against
  its matched k = 12 mean-aggregation twin and −0.0009 ± 0.0058 per-eye (36/75)
  against the k-NN GNN baseline — **degree buys zero** (NOTES row T9). And a flat
  depth/width/index-k response is **not** evidence that the backbone is
  reach-unlimited: the index-space k-NN is ~21× anisotropic in *physical* reach
  (row pitch 0.121 mm vs column pitch 0.006 mm), and arm E2 (2026-09-02/03) lifts
  the *same* network by **+0.0691 ± 0.0116 SE at 5/5 folds** (dilated stencil at
  matched `mean_max`; +0.0743 ± 0.0083 for the v2 `dilmean` lock) purely by
  replacing the edge geometry with a ±0.12 mm dilated stencil. The standing
  narrative was revised to "the index-space k-NN locality prior does not transfer;
  locality at physical lesion scale does" (NOTES T7i/T7j; ARCHITECTURE §1).
  Single ≈ dual nonetheless survives the stronger uniform branch, now on direct
  evidence: E2d on fold 2 leaves the dual arm 0.031 below its own single twin.
- **`res_cut`** (§9.2 #14) — the strongest architectural negative result.

**Post-2026-08 negative results** (each with its NOTES *Thesis-bound results* row;
fold-paired 5-fold deltas against the 0.016 threshold unless stated):

- **The gated correction branch does not engage, mesh or no mesh, decay or no
  decay** — dual − bypass = −0.0001 ± 0.0060 SE (3/5 folds), the tightest null in
  the project; arm G (`--moved_weight_decay 0`, fold 2) adds "decay or no decay"
  at +0.0092, under the 0.036 single-fold floor (T4, T8g; §5.1, §5.3).
- **The Euler ×Δt scaling is not load-bearing** — dropping it reads
  +0.0134 ± 0.0059 SE (4/5 folds), under the paired floor, so the flag was
  re-locked to True (T1 ablation arm; §4.5).
- **The monotonic penalty has no effect** and is locked at 0.0 (F1 ladder L4,
  −0.0032 ± 0.0033 SE; §6.1). *Not* a refutation of soft-Dice, which is retained
  at 5.0: what the ladder showed is that channel weighting, not soft-Dice, is what
  escapes the copy-input collapse (L1 ≈ L2) — soft-Dice buys immediate escape and
  half the variance (§9.2 #7).
- **The LayerEncoder surrogate buys nothing at any width** — d_embed 32/64/128/256
  read −0.0015 / +0.0006 / −0.0008 / +0.0034 against the encoder-off baseline, no
  monotonic trend, at 30–55 % more compute (T5).
- **Age + sex covariates are not detectable, and the residual points against them**
  — quote both instruments: fold-paired +0.0198 ± 0.0140 SE (3/5, one fold
  carrying ~60 %) and per-eye +0.0190 ± 0.0080 (43/75, t = 2.36; **not**
  LOFO-robust — dropping fold 4 leaves +0.0089, t = 1.11) for
  *removing* them. The age encoding (`baseline` vs `per_visit`) is a clean null
  (+0.0045 ± 0.0042) (T6).
- **Capacity reverses the U-Net win** — the 44×-capacity U-Net w32 reads
  −0.0479 ± 0.0303 SE against the param-matched w5 (1/5 folds), so the F5 result
  is an architecture-class effect, not a parameter-count one (T7b).
- **The per-pixel floor is exactly persistence** — `--hidden_layers 0` scores
  0.0000 on all five folds and flags the whole validation cohort as identical to
  baseline, while one message-passing ring reads 0.4529: every point of
  change-region Dice comes from spatial context (T7b/T8).
- **The normalisation axis is closed** — per-graph norm B5 reads
  +0.0146 ± 0.0074 SE, under the floor; its C2 pairing with mean aggregation
  reached +0.0196 ± 0.0088 at seed 42 but **fails to replicate at seed 7**
  (+0.0058 ± 0.0059); U-Net-density norm placement D2 adds only
  +0.0081 ± 0.0087 over its own control; and the graph norm on the stencil (E2n,
  fold 2) reads −0.0121. LayerNorm stays canonical (T7e–T7g, T7j).
- **Direction features are not the binding constraint, in either direction** —
  rescaling Δpos to index units (D1) is +0.0023 ± 0.0043, and zeroing it
  altogether (D1b) costs only −0.0099 ± 0.0056; the trained weights confirm D1
  raised the effective direction sensitivity 24×/308× and the metric did not move
  (T7g).
- **Time-integration order buys nothing** — RK4 over the stencil GNN is
  −0.0119 ± 0.0037 SE (1/5) against one Euler step at 4.5× the wall-clock, and the
  mixed FNO + RK4 arm is +0.0062 ± 0.0056 (T8n, T9, T9b). ⚠️ Dice alone never
  supports an "ODE" claim: the endpoint metric is binarised and blind to the
  trajectory. The solver-swap diagnostic ran 2026-09-17 (SOLVER_FINAL_RUNS.md
  §9.17) and the locked model fails it (Dice spread 0.0856 across solver settings)
  while the autonomous RK4 arm passes it (refined settings within 0.0044), so the
  continuous-time reading belongs to that arm and to no headline result.
- **Reach beyond the knee does not help** — against the locked ±21-column stencil,
  ±12 columns reads −0.0193 ± 0.0083 and ±42 columns −0.0256 ± 0.0040 at 5 folds,
  putting a measured optimum at ≈ 0.12 mm (T7j).

## 9.4 Open items the thesis must state honestly

- The anatomical names of the 10 layer boundaries are not recorded in the repo
  (obtain from the MUW segmentation pipeline).
- The cohort-wide validity of the single `SPACING_MM` constant is **unverified**: NOTES
  F10.14 measures a ~2 % deviation against the visits' own transform files and needs
  DICOM to settle. Every mm² figure inherits it (§1.2, §2.3). Distinct from the +2.08 %
  `linspace` node-pitch nuance in §2.5, which is a separate, logged and immaterial
  discrepancy.
- The @360d metric has no upper horizon bound: 7/75 eyes are scored at 450–720 d.
- The evaluation protocol is 5-fold train/val CV; the "test" split is structurally
  empty.
- **CLOSED 2026-08-15.** The 2×64 capacity lock no longer rests only on the old-era
  grid: the `STAGE=arch` legs ran at the then-locked loss on fold 2, and **6×128
  lands at 0.5071 ± 0.0225 against the 2×64 `L6nodts` leg's 0.5315 ± 0.0103**
  (paired −0.0244 ± 0.0053 SE, winning 4/20 epochs, double the variance). Both sit
  at `euler_dt_scale=False`, the configuration locked at the time and **re-locked to
  True on 2026-08-17** (§4.5); at the currently locked loss the fold-2 2×64 reads
  0.4963 (`L2_dice_f2`) / 0.5178 (`final_dts_f2`, its replicate pair). |Δ| = 0.024 is
  inside both the pre-registered ±0.04–0.05 band and the 0.036 single-fold replicate
  threshold (§7.4), so this is **flat capacity re-established post-fix — a null, not
  a win for the smaller model**: the −0.024 is one of the five single-fold deltas
  retracted on 2026-08-17 and must not be read as "6×128 is worse". What it does buy
  is that the old-era footnote on the 2×64 choice can be dropped, and that the extra
  capacity is not paying for itself. The k-axis ran for the first time in the same
  stage (`K24`: +0.0086 ± 0.0053 SE, also a null; `dataset_provenance.json` confirms
  `edges_per_node = 24`, `edges_source = runtime_knn`). Scope: one fold, one seed.
- The final thesis numbers come from the post-fix batch, and **T1 now exists** — for
  the **k = 12 index-space k-NN backbone with `mean_max` aggregation, 75,339
  params**, i.e. the pre-2026-09-03 canonical model and now the `--backbone gnn`
  comparison arm: single-branch 5-fold CV pooled over seeds 42 and 7 (10 runs),
  **`change_region_dice_360d` = 0.4529 ± 0.0362**, fold range 0.41–0.52, with the
  seed arm moving the CV mean by only +0.0028. **Since the 2026-09-03 LOCKED
  CONFIGURATION v2 the canonical uniform graph is the dilated stencil with
  mean-only aggregation** (`--backbone anisognn --gnn_aggr mean`, 67,147 params,
  the defaults of `jobs/train_solver.slurm`): `ANISOGNN_final_dilmean`
  0.5258 ± 0.0497 and its seed-7 replicate 0.5279 ± 0.0419, i.e.
  **+0.0743 ± 0.0083 SE over T1 at 5/5 folds** (NOTES row T7j). Fold remains a
  dominant variance source (0.41–0.52), comparable to or larger than most measured
  treatment effects — but not all: the 0-layer per-pixel floor is −0.45 and the
  dilated stencil +0.074 at 5/5 folds, both far outside the ±0.0127 replicate
  floor. Every earlier number is era-bounded per §9.1.
- **GA is *not* constrained to monotonic growth.** Since the 2026-08-15 loss lock
  the explicit penalty is 0.0 (§6.1; `MONOTONIC_MASK_WEIGHT:=0.0` in
  `jobs/train_solver.slurm`), and the residual form `u + Δt·f` (the ×Δt re-locked
  True on 2026-08-17) is **signed** — `gnn.py`'s decoder ends in a bare Linear, so
  `f` can shrink the mask. What the zero-init residual biases toward is
  *persistence*, not monotonicity. Observed ground-truth shrinkage should be
  quantified and discussed (segmentation noise vs biology — logged TODO).
- **CLOSED 2026-08-28 / 09-11.** The LayerEncoder surrogate ran (T5,
  `MPPDE_final_d{32,64,128,256}_f0..f4` at the locked 2×64): a null at every width
  — paired against the encoder-off baseline −0.0015 / +0.0006 / −0.0008 / +0.0034,
  all inside the 0.016 five-fold floor, with no monotonic trend
  ([SOLVER_FINAL_RUNS.md](SOLVER_FINAL_RUNS.md) §8.1). The external-baseline ladder
  ran as Stage F5: the param-matched U-Net beats the k-NN GNN by
  +0.0531 ± 0.0226 SE (4/5 folds, T7) and replicates at seed 7; U-Net w32 reverses
  the win (−0.0479 vs w5, T7b); the 0-layer per-pixel floor is bit-exactly
  persistence (0.0000 on all five folds, T7b/T8); plus FNO, the 3×3-bypass FNO
  hybrid, the graph U-Net, the dilated-stencil GNN, the Finite Element Network and
  the Neural-ODE wrapper (T7c–T9b, SOLVER_FINAL_RUNS §9). **Still unrun: a plain
  RNN and a transformer** — `--backbone` offers `gnn`/`unet`/`fno`/`gunet`/
  `anisognn`/`fen` only.
- **The 45-day T-FEN is not a valid long-horizon integrator as trained** (T9b): its
  free-running rollout diverges on 5 of 10 runs at 5 folds × 2 seeds, and the
  all-channel Courant number exceeds the explicit scheme's ~2.8 bound on 9 of 10
  final checkpoints. One-step error is healthy and every binarised metric is
  unaffected, so no reported anchor changes — but **the learned velocity map is not
  quotable**, and the fold-2 CFL pass that preceded it covered one fold and the mask
  channel only. The transport term's contribution (+0.050–0.053 at 5 folds, two
  seeds) stands.
- Cohort **lesion-scale statistics** are now partly compiled, from the runs' own
  `mai/` eval records: the growth-rate distribution in
  [SOLVER_FINAL_RUNS.md](SOLVER_FINAL_RUNS.md) §9.6c (true √area growth: median
  0.234 mm/yr, IQR 0.153–0.340, p90 0.473 over 75 eyes) and per-fold baseline-area
  medians in §9.8c (fold 4's 4.1 mm² against the other folds' 6.0–7.9), with the
  eye → mask mapping validated 75/75 against `baseline_area_mm2`. Still missing for
  the thesis dataset chapter: a **cohort-level baseline-area distribution table**
  comparable to Mai 2024, which is what the "slow-progressing, thin change region"
  claims this document makes qualitatively would rest on.

---

# 10. References

**Scope.** Every published work this document relies on, and nothing else. A work is
listed here only if the body actually leans on it; the body gives the full inline form
at the technical first use of each method and the short author-year form elsewhere, and
this section is the single place the fields can be checked. Conference venues that mint
no publisher DOI (ICLR, NeurIPS, ICML/PMLR, TMLR) are given by venue and arXiv id only —
their arXiv DataCite DOIs are omitted as uninformative. Where the repository's own
notation of a citation differs from the published record (title punctuation, preprint vs
journal year, author-name variants), the difference is stated on the entry rather than
silently resolved.

**Citation map.** [CODE_COMMENT_ARCHIVE.md](../../CODE_COMMENT_ARCHIVE.md) Part 2 is the
repository's designated map from each trained experiment arm and run-name family to the
module that implements it and to the published architecture it is adapted from; the
module docstrings carry the same `Reference:` lines. This section and that map must agree
— if they do not, the map and the code win.

## 10.1 Works cited

- **Ba, Kiros & Hinton 2016** — Jimmy Lei Ba, Jamie Ryan Kiros, Geoffrey E. Hinton.
  *Layer Normalization*. arXiv preprint (stat.ML), 2016. arXiv:1607.06450.
  *(No peer-reviewed venue — this work was never published at a conference or journal.)*
  First cited §4.3: `--norm_type layer`, the canonical normalisation of the GNN backbone.
- **Bachlechner, Majumder, Mao, Cottrell & McAuley 2021** — *ReZero is All You Need: Fast
  Convergence at Large Depth*. Uncertainty in Artificial Intelligence (UAI) 2021,
  PMLR 161:1352–1361. arXiv:2003.04887.
  First cited §4.4 (the zero-init deadlock argument), used again in §5.1: the
  zero-initialised scalar gate α on the moved branch.
- **Brandstetter, Worrall & Welling 2022** — *Message Passing Neural PDE Solvers*.
  ICLR 2022 (Spotlight). arXiv:2202.03376.
  First cited §0.2: **MP-PDE**, the solver backbone this framework adapts (§4, §4.7).
- **Butcher 1987** — J. C. Butcher. *The Numerical Analysis of Ordinary Differential
  Equations: Runge-Kutta and General Linear Methods*. Wiley, Chichester/New York, 1987,
  512 pp. ISBN 0-471-91046-5.
  First cited §4b.6: the explicit Butcher tableaus the integrator stores.
- **Chen, Rubanova, Bettencourt & Duvenaud 2018** — *Neural Ordinary Differential
  Equations*. Advances in Neural Information Processing Systems 31 (NeurIPS 2018).
  arXiv:1806.07366. *(The NeurIPS record is unpaginated.)*
  First cited §4.5: the Neural-ODE reading of the Δt-conditioned residual operator.
- **Courant, Friedrichs & Lewy 1928** — *Über die partiellen Differenzengleichungen der
  mathematischen Physik*. Mathematische Annalen 100(1):32–74, 1928.
  doi:10.1007/BF01448839.
  First cited §4b.7: the CFL condition against which the T-FEN's learned transport
  velocity is read (T9b).
- **Feuer, Yehoshua, Gregori, Penha, Chew, Ferris, Clemons, Lindblad & Rosenfeld 2013**
  — *Square Root Transformation of Geographic Atrophy Area Measurements to Eliminate
  Dependence of Growth Rates on Baseline Lesion Measurements: A Reanalysis of
  Age-Related Eye Disease Study Report No. 26*. JAMA Ophthalmology 131(1):110–111, 2013.
  doi:10.1001/jamaophthalmol.2013.572.
  First cited §7.1: the **square-root area transform** used for lesion areas, √area MAE
  and per-eye growth rates.
- **Gao & Ji 2019** — Hongyang Gao, Shuiwang Ji. *Graph U-Nets*. ICML 2019,
  PMLR 97:2083–2092. arXiv:1905.05178.
  First cited §4b.4 — as a **disambiguation, not a method used here**: the repository's
  `GAGraphUNet` is an image pyramid with a graph operator inside each block, not this
  work's learned node-scoring pooling of a general graph.
- **Gholami, Keutzer & Biros 2019** — *ANODE: Unconditionally Accurate Memory-Efficient
  Gradients for Neural ODEs*. IJCAI 2019, pp. 730–736. arXiv:1902.10298.
  doi:10.24963/ijcai.2019/103. *(The IJCAI proceedings print the first author as
  "Amir Gholaminejad"; arXiv gives "Amir Gholami" — the same person.)*
  First cited §4b.6: why the wrapper uses checkpointed discretise-then-optimise rather
  than the continuous adjoint.
- **Gilmer, Schoenholz, Riley, Vinyals & Dahl 2017** — *Neural Message Passing for
  Quantum Chemistry*. ICML 2017, PMLR 70:1263–1272. arXiv:1704.01212.
  First cited §4b.4: the offset-conditioned *shared* message MLP, which is why the graph
  U-Net is not a strict superset of a 3×3 convolution.
- **Gupta & Brandstetter 2023** — Jayesh K. Gupta, Johannes Brandstetter. *Towards
  Multi-spatiotemporal-scale Generalized PDE Modeling*. Transactions on Machine Learning
  Research (TMLR), 2023; arXiv preprint 2022. arXiv:2209.15616. *(PDEArena. TMLR is a
  continuous-publication venue: no volume or pages.)*
  First cited §4b.3: the evidence that a U-Net is the standard strong surrogate baseline
  in this literature.
- **Hairer, Nørsett & Wanner 1993** — *Solving Ordinary Differential Equations I:
  Nonstiff Problems*. Springer, Springer Series in Computational Mathematics vol. 8,
  2nd revised edition, 1993. doi:10.1007/978-3-540-78862-1.
  First cited §4b.6, with Butcher 1987, for the fixed-step explicit Runge–Kutta schemes.
- **Hu, Wang & Ma 2024** — Peiyan Hu, Yue Wang, Zhi-Ming Ma. *Better Neural PDE Solvers
  Through Data-Free Mesh Movers*. ICLR 2024 (Poster). arXiv:2312.05583.
  First cited §0.2: **MM-PDE**, the moving-mesh extension — the DMM (§3), the dual-branch
  composition (§5) and the "bigger GNN" parameter-matched control protocol (§4b.5).
- **Huang & Russell 2011** — Weizhang Huang, Robert D. Russell. *Adaptive Moving Mesh
  Methods*. Springer New York, Applied Mathematical Sciences vol. 174, 2011.
  doi:10.1007/978-1-4419-7916-2.
  First cited §3.1, in full at §3.4: the classical **equidistribution principle** the
  Monge–Ampère loss discretises, and the equidistribution-CoV mesh-quality measure
  (§3.8).
- **Krishnapriyan, Queiruga, Erichson & Mahoney 2023** — *Learning continuous models for
  continuous physics*. Communications Physics 6:319, 2023.
  doi:10.1038/s42005-023-01433-4. arXiv:2202.08494 (preprint, 2022).
  *(Cite the 2023 journal year: "Krishnapriyan et al. 2022" points at the preprint only.)*
  First cited §4b.6: with Ott et al. 2021, the **solver-swap validity test** — evaluate
  one trained checkpoint under several schemes and step counts and report how much the
  metric moves. That test is **unwritten** here, which is why no result in this document
  licenses an "ODE" claim.
- **Li, Kovachki, Azizzadenesheli, Liu, Bhattacharya, Stuart & Anandkumar 2021** —
  *Fourier Neural Operator for Parametric Partial Differential Equations*. ICLR 2021.
  arXiv:2010.08895. *(Publication year 2021; 2020 is the arXiv v1 submission year and is
  the wrong year to cite. The repository's `li2020fno` bib key encodes the preprint year,
  but the entry's own `year` field correctly reads 2021 — the key is misleading, not the
  entry.)*
  First cited §4b.3: the **FNO** countermodel (arm B4).
- **Lienen & Günnemann 2022** — Marten Lienen, Stephan Günnemann. *Learning the Dynamics
  of Physical Systems from Sparse Observations with Finite Element Networks*. ICLR 2022
  (Spotlight). arXiv:2203.08852. *(Surname spelled Günnemann; the ASCII "Guennemann" on
  two lines of `GraphPDE/train.py` is a transliteration of the same name.)*
  First cited §4b.7: the **Finite Element Network** and its T-FEN transport term.
- **Liu, Lehman, Molino, Petroski Such, Frank, Sergeev & Yosinski 2018** — *An Intriguing
  Failing of Convolutional Neural Networks and the CoordConv Solution*. Advances in
  Neural Information Processing Systems 31 (NeurIPS 2018). arXiv:1807.03247.
  *("Petroski Such" is one compound surname. The NeurIPS record is unpaginated.)*
  First cited §4b.2: the two normalised coordinate ramps in the countermodels' shared
  16-channel conditioning construction (`GAUNet`, `GAFNO`, `GAGraphUNet`).
- **Liu-Schiaffini, Berner, Bonev, Kurth, Azizzadenesheli & Anandkumar 2024** — *Neural
  Operators with Localized Integral and Differential Kernels*. ICML 2024,
  PMLR 235:32576–32594. arXiv:2402.16845.
  First cited §4b.3: the **localized-kernel** neural operator, i.e. the 3×3-bypass FNO
  hybrid (arm B4c).
- **Loshchilov & Hutter 2019** — *Decoupled Weight Decay Regularization*. ICLR 2019.
  arXiv:1711.05101. *(v3 of the preprint is the ICLR version.)*
  First cited §6.4: **AdamW**, the optimizer of every recorded solver run. Its decoupled
  decay is what arm G tests (§5.3) — on `model_b` and the ItpNet weights, since α itself
  has sat in a decay-free group since 2026-07-19.
- **Lu, Jin, Pang, Zhang & Karniadakis 2021** — Lu Lu, Pengzhan Jin, Guofei Pang,
  Zhongqiang Zhang, George Em Karniadakis. *Learning nonlinear operators via DeepONet
  based on the universal approximation theorem of operators*. Nature Machine Intelligence
  3(3):218–229, 2021. doi:10.1038/s42256-021-00302-5. arXiv:1910.03193.
  First cited §3.2: **DeepONet**, the branch/trunk operator architecture of the DMM —
  here with a concat head rather than the classic dot product.
- **Mai, Lachinov, Reiter, Riedl, Grechenig, Bogunović & Schmidt-Erfurth 2024** — *Deep
  Learning-Based Prediction of Individual Geographic Atrophy Progression from a Single
  Baseline OCT*. Ophthalmology Science 4(4):100466, 2024.
  doi:10.1016/j.xops.2024.100466.
  First cited §1.2, in full again at §7.1: the **direct clinical comparison** — same MUW
  cohort, same task — and the source of the reported cohort-metric suite (time bins,
  growth-region Dice, √area MAE, growth-rate r/R², fast-progressor AUC). Read every
  comparison against it with the input-regime caveat of §7.1: this framework consumes
  pre-segmented masks and layer surfaces, that work consumes raw OCT.
- **Milletari, Navab & Ahmadi 2016** — *V-Net: Fully Convolutional Neural Networks for
  Volumetric Medical Image Segmentation*. Fourth International Conference on 3D Vision
  (3DV) 2016, IEEE, pp. 565–571. arXiv:1606.04797. doi:10.1109/3DV.2016.79.
  First cited §6.1: the **soft-Dice** auxiliary loss — applied here to a
  sigmoid-sharpened z-scored regression output rather than to a segmentation probability
  map, the deliberate deviation §6.1 names as the source of its decalibration caveat.
- **Ott, Katiyar, Hennig & Tiemann 2021** — *ResNet After All: Neural ODEs and Their
  Numerical Solution*. ICLR 2021. arXiv:2007.15386. *(The arXiv version titles it
  "ResNet After All? …" with a question mark — the form the module docstrings and §4.5
  quote. Note arXiv:2007.15385 is an unrelated paper.)*
  First cited §4.5: the **ODE-solver-validity argument** — a model that is genuinely a
  continuous ODE should be nearly invariant to the solver used at inference (see
  Krishnapriyan et al. 2023).
- **Ronneberger, Fischer & Brox 2015** — *U-Net: Convolutional Networks for Biomedical
  Image Segmentation*. MICCAI 2015, Lecture Notes in Computer Science, Springer,
  pp. 234–241. arXiv:1505.04597. doi:10.1007/978-3-319-24574-4_28.
  First cited §0.2, in full at §4b.3: the **U-Net** countermodel (arms B1/B2), the arm
  that beat the v1 k-NN GNN and against which the v2 stencil is indistinguishable.
- **Salvi, Cluceru, Gao, Rabe, Schiffman, Yang, Lee, Keane, Sadda, Holz, Ferrara &
  Anegondi 2025** — *Deep Learning to Predict the Future Growth of Geographic Atrophy
  from Fundus Autofluorescence*. Ophthalmology Science 5(2):100635, 2025.
  doi:10.1016/j.xops.2024.100635.
  First cited §4b.3: the GA-field precedent for a 2-D U-Net predicting future GA growth
  — on fundus autofluorescence, not OCT, which is why it motivates the countermodel
  rather than supplying a comparable number.
- **Wu & He 2018** — Yuxin Wu, Kaiming He. *Group Normalization*. ECCV 2018, Lecture
  Notes in Computer Science, Springer, pp. 3–19. arXiv:1803.08494.
  doi:10.1007/978-3-030-01261-8_1.
  First cited §4.3, in full at §4b.2: `GroupNorm(1, C)` in `unet.py` and `gunet.py` —
  the stats-free normalisation that gives those two arms the same `train() == eval()`
  parity the GNN has (`fno.py` and `fen.py` carry no norm layer at all).
- **Zhuang, Dvornek, Li, Tatikonda, Papademetris & Duncan 2020** — *Adaptive Checkpoint
  Adjoint Method for Gradient Estimation in Neural ODE*. ICML 2020,
  PMLR 119:11639–11649. arXiv:2006.02493.
  First cited §4b.6, with Gholami et al. 2019, on checkpointed gradients for the
  integrator.

## 10.2 Constructions with no paper behind them

The following carry **no citation deliberately** — they are this repository's own, and
the thesis must present them as such rather than implying an upstream source. Where one
wraps or ablates a published backbone, that backbone is named beside it (the same
convention [CODE_COMMENT_ARCHIVE.md](../../CODE_COMMENT_ARCHIVE.md) Part 2 uses in its
Reference column).

| Construction | Where | Over |
|---|---|---|
| The **dilated anisotropic stencil geometry** — rows ±1 × columns {0, ±7, ±14, ±21}, and the reach ladder around it | §4.3b | wrapped backbone: Brandstetter et al. 2022 |
| The **LayerEncoder** surrogate for the PDE coefficients | §4.6 | conditioning enters the backbone of Brandstetter et al. 2022 |
| **Patient-covariate conditioning** (age, sex as graph-level scalars) | §1.5, §2.6, §4.1 | — |
| The **per-pixel floor** (0 layers) and the **one-hop floor** (1 layer) | §4b.4 | ablations of Brandstetter et al. 2022 |
| The **parameter-matched bypass control** (DMM loaded, warp ignored) | §5.5 | control for the Hu et al. 2024 composition |
| The **direction-feature** variants (`--edge_feat_index`, `--edge_feat_none`) and the **norm-placement** variants (`PerGraphNorm`, `--norm_mlp_sites`) | §4.3 | over Brandstetter et al. 2022; `PerGraphNorm` is the graph analogue of Wu & He 2018 |
| The **mean+max aggregator** — the specific combination, now refuted by measurement and no longer canonical | §4.3 | the `mean` it returns to is Brandstetter et al. 2022 |
| The **time-budgeted pushforward curriculum** (budget in days, not visit count) | §6.2 | the pushforward trick itself is Brandstetter et al. 2022 §3.1 |
| The **change-region restriction** of Dice/IoU at 360 d, whose persistence floor is exactly 0 | §7.1 | the coefficient itself is standard; the restriction is this repo's |
| The **config-independent mesh-quality set** (`tangled`, `edge_gain`, `cov_ref`, `det_min`) | §3.8 | `cov_ref` scores against the equidistribution theory of Huang & Russell 2011; the rest are this repo's |

Two further conventions the thesis should state rather than cite: the ±0.0127
**replicate floor** and the two instruments it calibrates (§7.4) are this project's own
measurement on same-config replicate pairs, not a literature threshold; and the
**era boundaries** of §9.1 are bookkeeping over this repository's own history.

---

*Document written 2026-08-14 from direct code reading at git `ecdf2fb` (+ working
tree) plus the project's canonical docs; last full sync 2026-08-24 (`d2b821b`),
corrected in place 2026-09-16 for the 2026-09-03 v2 lock and the Stage-F5 /
Neural-ODE / FEN arms, and given its §10 reference list in the same pass — see the
currency block in the header for what that covers.
When code and this document disagree, the code is right and this document must be
updated — flag discrepancies in [NOTES.md](../../NOTES.md).*
