# Prompt: Discussion, Conclusion, Abstract and Computational Cost

*(Self-contained. Copy everything below the line into the other model.)*

---

## 1. Your role and the task

You are drafting the last missing parts of a Master's thesis in machine learning (Johannes Kepler University Linz, with the Medical University of Vienna). Chapters 1–5 are written and audited. Your job is to write, **in LaTeX, ready to paste**:

| # | Part | File | Budget |
|---|---|---|---|
| A | §5.6 Computational Cost (the last missing section of Chapter 5) | `05-experiments.tex` | ~0.75–1 page |
| B | Chapter 6, Discussion (four sections) | `06-discussion.tex` | ~6–9 pages |
| C | Chapter 7, Conclusion | `07-conclusion.tex` | ~2–3 pages |
| D | English abstract and German *Kurzfassung* | `00-abstract.tex` | ≤ 1 page each (~300–380 words) |

Write the full text to the budget, not a skeleton. Every number you use must come from the fact sheet in §4 of this prompt. If you need a number that is not there, **do not invent it**: write a `% TODO:` comment in the LaTeX saying exactly what is missing and continue.

After the LaTeX, give a short **report** (plain text): (1) every sentence where you were unsure whether a claim is supported, (2) every `% TODO` you left, (3) any place where the fact sheet seemed contradictory.

---

## 2. The thesis in one page (context you need)

**Topic.** Geographic Atrophy (GA) is the advanced atrophic form of age-related macular degeneration: a lesion of dead retinal tissue that grows slowly and irreversibly over years. The thesis forecasts how the GA lesion of an individual eye changes, from longitudinal OCT imaging.

**Research question (fixed wording, quote it verbatim where you restate it):**
> *What is needed to forecast the progression of Geographic Atrophy from longitudinal OCT?*
> (1) What kind of framework does the forecast need?
> (2) What kind of operator does that framework need?

Chapter 4 answers (1), Chapter 5 answers (2).

**Approach.** The work started as an adaptation of two neural PDE solver frameworks (MP-PDE, Brandstetter et al. 2022; MM-PDE, Hu et al. 2024). What it produced is a **fixed framework with one swappable operator slot**. Everything except the operator $f_\theta$ is fixed and shared: one visit in, no history; an 11-channel state (channel 0 = binary GA mask, channels 1–10 = depths of ten retinal layer boundaries) on a 49 × 1024 en-face grid; the $\Delta t$-conditioned residual update
$$u_{t+\Delta t} = u_t + \Delta t \cdot f_\theta(u_t, \Delta t, z)$$
($z$ = patient covariates age and sex) with a zero-initialised output head so every operator starts at exact persistence; a pushforward training curriculum whose unroll depth is a budget of elapsed days (180-day base, 360-day maximum); a mask-weighted MSE + soft-Dice loss; the same optimiser, epochs, folds, seeds, evaluation and model selection. Then many operators from unrelated literatures are run through the slot under identical conditions: graph networks (MP-PDE style) on two different neighbourhood graphs, U-Net, Fourier Neural Operator (FNO), FNO with a 3×3 local path, a Finite Element Network (FEN) with and without a learned transport (advection) term (T-FEN), a Runge–Kutta (RK4) wrapper, and two locality floors. Parameter counts are matched (67–83 thousand).

**Headline.** The framework transfers across architecture classes, and **the architecture class does not decide the outcome**. The strongest arms come from three unrelated classes and are close together; what separates arms is which *ingredients* they carry — spatial context, physical reach at lesion scale, global and local context together, an explicit transport term — each measured in isolation. Many things were measured and did not matter (negative results).

**Moving mesh (MM-PDE half).** Reported only in Appendix G as an additional experiment. In the main chapters it gets **at most one sentence**, pointing to `Appendix~\ref{app:mm-pde}`.

---

## 3. Rules (binding — the author audits every line against these)

### 3.1 Voice and style
- **Passive voice, no "we", no "I", no "our"** (solo thesis). "It was shown", "The operator was trained", "This thesis …" is fine.
- **Plain, short sentences.** The author repeatedly rewrote sentences that were too long or too dense. One idea per sentence; paragraphs of 3–7 sentences. Prose, not bullet lists (exception: the Conclusion may use one short enumerated list of findings if it reads better).
- **No filler or hype words**: never use *strictly, crucially, pivotal, massive, rigorous, notably, remarkably, firmly, purely, entirely, robust (as praise), novel, groundbreaking, paradigm, leverage, delve, underscore, showcase, landscape*. No rhetorical questions in the running text (paragraph headings in `\paragraph{…?}` form are fine; Chapter 5 uses them).
- British spelling as in the rest of the thesis: *normalisation, discretisation, parameterisation, generalise, modelling, behaviour*.
- Every metric you mention needs a plain description of what it measures the first time it appears in a chapter (the author's rule). Short, e.g. "the change-region Dice, which scores whether the model predicts change where change actually happened".
- Frame results honestly. Say what did not work. Do not oversell; do not apologise either.
- The Discussion follows the "hour-glass": broaden back out from the technical results to what they mean for the field and the clinic.

### 3.2 LaTeX
- Citations with natbib only: `\citet{key}` for textual ("\citet{Mai2024} predict …"), `\citep{key}` for parenthetical. **Only these keys exist:**
  `Brandstetter2022 Hu2024 Boopathiraj2024 Boyer2017 Chu2022 Ebneter2016 Flaxman2020 Lad2023 Pilotto2015 Singh2025 Song2025 Trincao2024 Vallino2024 Vogl2021 Yehoshua2011 LeVeque2007 LeVeque2002 Courant1943 LangtangenMardal2019 Liu1994 JiangShu1996 GottliebOrszag1977 Trefethen2000 Bartels2016 Scarselli2009 Runge1895 Kutta1901 Gilmer2017 Ronneberger2015 Li2021 LiuSchiaffini2024 Lienen2022 Chen2018 Wong2014 SchmidtErfurth2018 Bogunovic2017 Sadda2018 Mai2024 Salvi2025 Feuer2013 Butcher1987 Hairer1993 Courant1928 BarSinai2019 Kochkov2021 SanchezGonzalez2020 Pfaff2021 Lam2023 Lu2021 Gupta2023 Ott2021 Krishnapriyan2023 Battaglia2018 Ba2016 Ioffe2015 Liu2018 Wu2018 Gao2019 HuangRussell2011`
  What they are, for the ones you are likely to need: Brandstetter2022 = MP-PDE; Hu2024 = MM-PDE; Mai2024 = Mai et al., *Ophthalmology Science* 2024, deep-learning prediction of individual GA progression from a single baseline OCT, **same MUW cohort**, Neural ODE with RK4; Salvi2025 = U-Net-type GA growth prediction from fundus autofluorescence; Vogl2021 = topographic GA progression analysis; Vallino2024 = GA review incl. complement inhibitors; Lad2023, Singh2025 = GA treatment/epidemiology; Feuer2013 = square-root transform of GA area; Chen2018 = Neural ODEs; Ott2021, Krishnapriyan2023 = learned ODE models depend on their training discretisation; Hairer1993, Butcher1987 = ODE numerics; Courant1928 = CFL condition; Ronneberger2015 = U-Net; Li2021 = FNO; LiuSchiaffini2024 = neural operators with local kernels; Lienen2022 = Finite Element Networks; Gupta2023 = U-Net as strong neural-PDE baseline (PDEArena); Lam2023 = GraphCast; Pilotto2015 = GA lesion location in the macula; Yehoshua2011 = GA progression natural history.
- If a citation outside this list would genuinely fill a gap (e.g. uncertainty quantification, 3-D OCT models, recurrent/transformer models for longitudinal imaging), write the author-year in plain text and put **immediately above the sentence**: `% TODO: cite <ProposedKey> (short bibliographic hint) once added to references.bib`. Do not invent bibliographic details you are not sure of — then say "hint uncertain" in the TODO.
- Cross-references: use `\S\ref{…}`, `Chapter~\ref{…}`, `Table~\ref{…}`, `Appendix~\ref{…}`, with a non-breaking `~`. **Only these labels exist** (do not invent new ones except the section labels given in §5 of this prompt):
  - Chapters: `ch:introduction ch:background ch:data ch:method ch:experiments ch:discussion ch:conclusion`
  - Data: `sec:data:dataset sec:data:state sec:data:spatial sec:data:normalization sec:data:covariates sec:data:temporal sec:data:splits`
  - Method: `sec:method:overview sec:method:framework sec:method:dt-residual sec:method:multichannel sec:method:family sec:method:family:contract sec:method:mppde sec:method:graph sec:method:family:dense sec:method:family:floors sec:method:family:fen sec:method:family:rk sec:method:family:params sec:method:covariates sec:method:training sec:method:training:loss sec:method:training:curriculum sec:method:training:optim sec:method:implementation`; `fig:method:stencils tab:method:params tab:method:hparams`
  - Experiments: `sec:experiments:protocol sec:experiments:protocol:metrics sec:experiments:protocol:rollout sec:experiments:protocol:stats sec:experiments:main-results sec:experiments:ingredients sec:experiments:ingredients:context sec:experiments:ingredients:reach sec:experiments:ingredients:global sec:experiments:ingredients:transport sec:experiments:ingredients:convergence sec:experiments:ablations sec:experiments:ablations:time sec:experiments:ablations:loss sec:experiments:ablations:capacity sec:experiments:validity sec:experiments:validity:swap sec:experiments:validity:tfen sec:experiments:qualitative sec:experiments:qualitative:mai sec:experiments:cost`; `tab:experiments:arms tab:experiments:reach tab:experiments:capacity tab:experiments:swap tab:experiments:tfen-stability tab:experiments:mai`
  - Discussion (already in the file skeleton): `sec:discussion:interpretation sec:discussion:clinical sec:discussion:limitations sec:discussion:future`
  - Appendix: `app:mm-pde`
  - Research question paragraph: `par:introduction:research-question`
- Escape `%` in running text as `\%` (e.g. `27.3\,\%`). Thin space before units: `0.12\,mm`, `4.8~times` or `$4.8\times$`. Math for $\Delta t$, $f_\theta$, $\pm$. Thousands with a thin space: `67\,147`.
- Table rows end with `\\`. Use `booktabs` (`\toprule \midrule \bottomrule`), `\small`, caption before label, captions self-contained. No `\tablefootnote`.
- Do not use `\newline`, `\\` inside paragraphs, `\textbf` for emphasis in running text (use `\emph` sparingly).
- Do **not** produce figures. If a figure would help, write a placeholder only if asked below.

### 3.3 Hard content rules (violating any of these means the text is rejected)
1. **No invented numbers.** Only fact-sheet numbers; round only as the fact sheet does.
2. **No "ODE", "rate field", "learned dynamics", "growth rate field", "continuous-time model" language for the canonical model or any headline result.** The canonical model failed the solver-swap test; it is a one-step map conditioned on the step length. A continuous-time reading is admissible only for the RK4-wrapper network and the energy-conserving T-FEN, within one fold and one seed.
3. **Never compare raw RMSE across arms**, and never use RMSE as evidence.
4. **No "test set" wording.** The protocol is 5-fold cross-validation with train/validation splits; the test split is structurally empty. Every result is a validation result.
5. **GA is not modelled as strictly monotonic.** No monotonic constraint; reference segmentations shrink locally between some visits (not yet quantified — whether this is segmentation/registration noise or biology is open).
6. **Do not claim the discarded periphery is clinically irrelevant.** The 49 × 1024 crop is a deliberate trade-off with measured cost (see fact sheet).
7. **Do not say "mesh adaptation does not transfer to GA".** The appendix result is scoped: the gated correction branch never engaged, with or without the mesh; it is an implementation-scoped null.
8. **Do not say the T-FEN is the best model.** Its lead over the U-Net is pending a seed-7 replication; against the canonical graph network it is a tie.
9. **The canonical model starts from pre-segmented masks and layer depths; Mai et al. start from the raw OCT volume.** This caveat travels with every comparison to Mai et al.
10. **Nulls are nulls at the available precision**, not proofs of equivalence, and each is scoped to the backbone/folds/seed on which it was measured.
11. Do not name the ten layer boundaries anatomically (the names are not recorded). Do not define the mask via cRORA/CAM criteria.
12. Patient covariates and the layer encoder: their ablations are **not reported in Chapter 5** (commented out). In the Discussion they may only appear as open questions/limitations/future work, described qualitatively as below — never with the old numbers.
13. The graph U-Net arm was dropped; do not mention it. Do not quote "nine settings / six architecture classes".
14. Do not present the thesis as "adapting MP-PDE/MM-PDE to GA". Speak of the framework and the operators.

---

## 4. Fact sheet (the only allowed source of numbers)

### 4.1 Data (Chapter 3)
- MUW GA cohort: **75 eyes of 51 patients** (24 patients contribute both eyes), **553 visits**, 478 visit-to-visit intervals. 5–13 visits per eye (median 7). Follow-up per eye 720–2160 days (median 1080 days, about three years). Most common interval 180 days (76.2 % of intervals); some 90-day intervals from a densely imaged subgroup.
- Device: Heidelberg Spectralis SD-OCT (sourced to Mai2024; the data record only vendor and scan mode).
- Cohort growth: median square-root-area growth rate 0.234 mm/year (IQR 0.153–0.340).
- Grid: native en-face grids vary (67 distinct shapes, 38–66 B-scans × 961–1719 A-scans); all resampled upstream to one pixel spacing (0.12118 mm between B-scans, 0.00568 mm along them). Pixel spacing is **treated as** constant across the cohort; this was checked only against the cohort's own transform files (~2 % agreement), not against the DICOM spacing fields — an open assumption on which every mm² figure depends.
- Modelling grid 49 × 1024 by centre-crop or zero-pad (never resampling): 5.94 × 5.82 mm, 50,176 positions; spacing between B-scans **21.3× larger** than along them.
- **Crop cost:** the window cuts real lesion area in **27.3 %** of visits (>5 % of the lesion in 6.0 %, worst case 25.7 %); **31.1 %** of cropped lesions touch the crop border, so growth across it is censored in training targets and metrics, with no missingness flag. Larger windows would trade this for up to 35 % zero-padding and ~1.9× the node count; about 19 % border contact is irreducible because those lesions reach the scan's own edge. A border-vs-interior split of the metric exists but is **not reported** (the ranking of arms is unchanged on interior eyes — you may say this is not reported in the thesis; do not quote its numbers).
- Mask provenance (for the Limitations only, stated neutrally): the GA reference in this cohort was most likely annotated on fundus autofluorescence and registered onto the OCT grid (as described by Mai2024 for this cohort); the layer-segmentation provenance and the boundary names are not recorded.
- Splits: patient-level 5-fold cross-validation (both eyes of a patient in the same fold); 12–20 validation eyes per fold; no test split.

### 4.2 Framework (Chapter 4) — what is fixed
- Residual update $u_{t+\Delta t} = u_t + \Delta t \cdot f_\theta(u_t,\Delta t,z)$, zero-initialised head ⇒ every operator starts at exact persistence; persistence is the limit as $\Delta t \to 0$.
- One visit in, no memory of the trajectory; strict one-step prediction (no temporal bundling).
- All 11 channels predicted jointly.
- Loss: MSE with mask weight 5 vs 1 per layer channel + soft-Dice on the mask (weight 5); monotonic penalty implemented but off (weight 0) everywhere.
- Pushforward curriculum in elapsed days (base 180 d, max 360 d, matching the one-year anchor).
- No normalisation with batch statistics in any operator (per-node layer normalisation / group normalisation), so training and evaluation are the same operator.
- Covariates age and sex enabled in every operator; they are graph-level scalars broadcast to all 50,176 positions, constant or near-constant along a trajectory, so they cannot localise anything. Together with $\Delta t$ they fill the slot that the equation-coefficient vector $\theta_{\text{PDE}}$ occupies in MP-PDE (GA has no known governing equation).
- An optional **layer encoder** (a CNN compressing the ten layer channels into one global embedding, meant as a learned stand-in for $\theta_{\text{PDE}}$) exists in the code but is off in every reported operator and not examined in the thesis. It was run only as a width sweep (32–256) on the k-NN graph network with no detectable effect; its strides correct only ~2× of the ~21:1 anisotropy, and during rollout it would encode predicted rather than observed layers.

### 4.3 Evaluation protocol (Chapter 5.1)
- Headline metric: **change-region Dice at the one-year anchor** — Dice between predicted and true sets of pixels that changed relative to the baseline mask; persistence scores exactly 0 by construction; symmetric (shrinkage counts as change). Full-mask Dice is nearly blind to progression (persistence already ≈ 0.87).
- Growth-region Dice (new atrophy only; Mai2024's metric), also reported per horizon bin (0–1, 1–2, 2–3, >3 years).
- The anchor is the first rollout step at or beyond 360 days (no upper bound; for a few eyes it lies beyond one year).
- Reported values are late-epoch means (epochs 10–29), not best-epoch values (noise sd 0.02–0.10 per fold; best epoch would be optimistically biased without a test split).
- **Noise floor:** repeated runs of one configuration differ with sd ≈ **0.0127**; a single-fold difference must exceed 0.036, a five-fold paired mean 0.016 (≈ 0.020 when a U-Net is involved, whose seed spread is ~1.9× wider). Two instruments (fold-paired mean and a per-eye paired test over 75 eyes); a result is "established" only when both agree. Fold variance is large (k-NN arm: 0.43–0.52 across folds). GPU nondeterminism dominates seed choice.
- For the Discussion/Conclusion, report results **in words with the key number**, e.g. "higher by 0.064 on average, on all five folds and on 70 of 75 eyes". Do not reproduce "± SE (k/5)" notation.

### 4.4 The arm table (seed 42, change-region Dice @ 1 y, mean ± sd over 5 folds; params; min epoch time)
| Arm | Params | Mean ± sd | s/epoch (min over folds) |
|---|---:|---|---:|
| T-FEN (energy-conserving transport form) | 68,503 | 0.5428 ± 0.0401 | 367 |
| Graph network, dilated stencil (**canonical model**) | 67,147 | 0.5258 ± 0.0497 | 91 |
| Graph network, dilated stencil, RK4 | 67,147 | 0.5139 ± 0.0497 | 439 |
| U-Net, width 5 | 83,081 | 0.5046 ± 0.0632 | 21 |
| FNO + 3×3 local path | 79,960 | 0.4984 ± 0.0398 | 29 |
| FNO, RK4 | 79,160 | 0.4893 ± 0.0398 | 45 |
| FNO | 79,160 | 0.4831 ± 0.0477 | 23 |
| FEN, free-form only | 34,785 | 0.4810 ± 0.0348 | 180 |
| Graph network, k-NN, k = 12 | 67,147 | 0.4623 ± 0.0361 | 76 |
| Graph network, k-NN, k = 20 | 67,147 | 0.4519 ± 0.0436 | 108 |
| One-hop floor | 40,971 | 0.4515 ± 0.0243 | 37 |
| Per-pixel floor (no spatial context) | 14,795 | 0.0000 ± 0.0000 | 16 |
| Persistence | 0 | 0 | — |

- The best single fold of the canonical model reads 0.6060 (fold 2); the best fold is fold 2 for every arm except the two FNO arms without a local path.
- **The three highest arms come from three unrelated classes** (finite-element network, graph network, U-Net). T-FEN vs canonical graph network: +0.017 fold-paired, +0.014 per eye — a **tie**. Canonical vs U-Net: +0.021 at seed 42, only +0.008 at seed 7 (canonical 0.5279, U-Net 0.5199 at seed 7) — both under the floor, **indistinguishable**. T-FEN vs U-Net: +0.038 at seed 42 on both instruments, above the floor, but **not read as established before its seed-7 replication** (an earlier T-FEN form lost half such a lead at seed 7). → `% TODO` wherever the final wording depends on the pending seed-7 T-FEN run.
- The per-pixel floor is bit-identical to persistence on all five folds; every point of change-region Dice comes from spatial context.

### 4.5 Ingredient study (Chapter 5.3)
1. **Spatial context.** 0 rounds of message passing = 0.0000; one round (one-hop floor) 0.4515; two rounds (k-NN arm) 0.4623 — the second round adds about 0.01, consistent in direction, not established. A single ring buys almost everything on this graph.
2. **Physical reach at lesion scale — the largest effect in the project.** Changing only the edge set from the index-space k-NN graph (one hop reaches only ±2 columns ≈ 0.011 mm along a row, but ±0.25 mm across rows) to the dilated stencil (rows ±1 × columns {0, ±7, ±14, ±21}; ≈ 0.12 mm on both axes), at the same 67,147 parameters: **+0.064**, higher on 5/5 folds and 70/75 eyes; replicated at seed 7 (+0.063, 5/5 folds, 66/75 eyes); seed-pooled 136/150 eye-seed pairs. Reach ladder: ±12 columns and ±42 columns are both worse by more than the floor, so **±21 columns is a measured optimum**, close to the 90th percentile of the per-visit front advance (23 columns; median 12). Two rows instead of one costs most (−0.039). More neighbours at the same reach (k = 20) buy nothing. "Placement, not count." Before the stencil, the U-Net beat the k-NN graph network (+0.042 at seed 42, +0.055 at seed 7); with the stencil the graph network is level with the U-Net ⇒ **the graph network's deficit was its graph, not its operator class**.
3. **Global and local context together.** The FNO (global spectral, no local path) is established **below** the U-Net at the one-year anchor (−0.022 / −0.028 per eye). Adding a 3×3 local path (+800 parameters) brings it level with the U-Net (tie) and above the k-NN graph network on both instruments. The local path itself (hybrid vs FNO): +0.015 fold-paired (under the floor) but graduates per eye — the two instruments disagree. Beyond one year the FNO catches up with and passes the U-Net (growth-region Dice 1–2 / 2–3 / >3 y: FNO 0.546 / 0.583 / 0.594 vs U-Net 0.563 / 0.581 / 0.555) — descriptive, not tested. Reading: global context and local detail are separable, both needed; two unrelated constructions (U-Net pyramid, FNO + local path) arrive at the same level.
4. **Explicit transport term.** T-FEN vs the same FEN without its transport head (same width, additive ablation, both start as the same function): **+0.062, 5/5 folds, 68/75 eyes**. Earlier Galerkin form: +0.053 (seed 42) and +0.050 (seed 7) — the effect does not depend on the form. **Parameter-matched control** (free-form FEN widened to 68,282 parameters): does not train on fold 4 (twice); on folds 0–3 the T-FEN is higher by **+0.072 (4/4 folds, 59/63 eyes)**; the extra width bought the free-form FEN nothing ⇒ the transport effect is not a matter of parameter count (scope: four folds, one seed; a seed-7 matched control is pending). Where it acts: growth-region Dice in the first year — free-form FEN 0.388, one-hop floor 0.395, k-NN 0.393 (operators whose reach falls short of the front advance) vs T-FEN 0.519 and dilated stencil 0.503. Over the horizon T-FEN and stencil are close (0.519/0.602/0.633 vs 0.503/0.600/0.634 for years 1/2/3; beyond three years stencil 0.655 vs T-FEN 0.611).
5. **Two routes to one deficit (the central architectural result).** The GA front moves ~10–25 columns per visit; a one-hop operator on the index-space graph cannot see that far. Two unrelated constructions correct it — physical reach (dilated stencil) and an explicit transport term (T-FEN) — each established against its own control, and they end up indistinguishable. This coincidence, not any single arm's score, is the central architectural result. It is **suggestive, not a proof of mechanism**.

### 4.6 Negative results (Chapter 5.4) and pending runs
- **Time handling.** (a) Removing the multiplication by $\Delta t$ (keeping $\Delta t$ as input): on the canonical network the run is **pending** → write around it conditionally with a `% TODO`; the argument in the text is that on the mask channel the scaled update must produce a fixed jump divided by $\Delta t$, so the multiplication is a reparameterisation, not extra knowledge; it is kept for the persistence limit. (b) RK4 instead of one Euler step: over the stencil network −0.012, over the FNO +0.006, both within noise; RK4 costs ~4.8× the training time on the graph network. Conclusion: the interval must reach the operator, how does not matter; accuracy is decided by the spatial operator, not the time stepping.
- **Objective.** Three runs on the canonical network are **pending** (unweighted MSE; no soft-Dice; monotonic penalty weight 2). Expected but not confirmed reading: the mask weighting prevents the copy-the-input collapse; soft-Dice buys earlier escape and steadier training rather than a higher score. Two arguments against the monotonic penalty independent of its score: under pushforward it locks in the model's own false positives (penalty gradient measured at 31.8× the data gradient on such pixels — measurement setting still to confirm), and the reference masks themselves shrink locally. Do not state the pending results.
- **Capacity.** Width scaled per class (≈ ¼×, 1×, ~4×; seed 42, 5 folds): no width step raises any class above the floor on either instrument. Stencil graph network flat from 18,219 to 257,163 parameters (0.521 / 0.526 / 0.518). U-Net and FNO+3×3 best at or near original size; the widest U-Net (~40× parameters, 3.35 M) falls below its original size (−0.045 per eye). Scaling down costs little. Depth: four rounds instead of two lower the graph network slightly on every fold (under the floor); the T-FEN with an 8-layer free-form MLP does not train; T-FEN width 192 diverges on two folds (these T-FEN points used the older Galerkin form; re-runs in the energy-conserving form are pending). ⇒ **Capacity is not a lever on this task**; the matched-size comparisons are not an artefact of size. One seed.
- Not reported in Chapter 5 but measured (may be mentioned **qualitatively only** in the Discussion as "an earlier ablation on an older configuration found no detectable benefit"): patient covariates (removal gave no detectable loss, residual pointed against them, largely carried by one fold); layer encoder (null over an 8× width range); GNN-internal settings (normalisation type, aggregation, edge-direction features — none mattered). The intermediate-time-point regulariser (penalising predictions at sub-interval times against the linear interpolant between visits) was evaluated early and removed: no benefit.
- **Appendix G (moving mesh).** A data-free mesh mover and a gated dual-branch composition were built; the gate never opened; dual branch minus a parameter-matched control that ignores the mesh = −0.0001 ± 0.0060 (tightest null in the project) at ~10× the training cost. The gate stays shut in the control too, so what was measured is the correction branch's failure to engage, not a verdict on mesh adaptation for GA. **One sentence at most in the Discussion; zero or one in the Conclusion/abstract.**

### 4.7 Validity diagnostics (Chapter 5.5)
- **Solver-swap test** (re-evaluating a trained checkpoint, no retraining, under different integration schemes/steps; criteria: C1 convergence under refinement, C2 agreement within the 0.0127 noise). Canonical network (fold 2): **fails** — refining Euler from 1→2→4 steps changes Dice by −0.016 then −0.060; span 0.086 ≈ 7× noise; it is a one-step map conditioned on the step length. RK4-wrapper network (fold 2): **passes** (RK4 settings within 0.0005). Energy-conserving T-FEN (fold 0): **passes** (45→15-day steps within 0.0003). Neither of the passing models is more accurate than the canonical one ⇒ the continuous-time property is obtainable on this task but does not decide accuracy. Scope: one fold, one seed per model.
- **T-FEN stability.** The first (Galerkin) transport form was unstable in 7/10 free-running runs (5 folds × 2 seeds): divergence started at the crop edge, in a layer channel, after ~1.6–2 years (beyond the 360-day training horizon and beyond the anchor), caused by the Galerkin operator's defect at the domain edge, not by step size; the one-year Dice was unaffected. The energy-conserving (skew) form is stable on 5/5 folds, at least as accurate (+0.009, all five folds, under the noise), with the gain on border-touching lesions (0.516 → 0.544) and beyond three years (growth-region Dice 0.537 → 0.611). A small residual at the grid's top/bottom rows from ~day 1,260 is the RK4 step-size limit on the mask channel; a 30-day evaluation step removes it without changing the Dice. The learned velocity field is **not interpreted** in the thesis. Seed-7 skew run pending.

### 4.8 Clinical comparison with Mai et al. 2024 (Chapter 5.5.1)
- Same MUW cohort, Mai et al. predict from a **single raw baseline OCT volume** with a Neural ODE + RK4; 184 eyes / 100 patients, mean follow-up 32 months. This thesis: 75 eyes / 51 patients, mean follow-up 3.3 years, **starts from segmented masks and layer depths**, areas measured inside the censoring crop.
- Growth-speed measures (canonical model, 75 pooled eyes, 95 % bootstrap CI), growth rate = change in √area per year over the whole follow-up:
  - Pearson r: **0.40 [0.22, 0.56]** vs Mai **0.61**
  - Fast-progressor AUC, top 10 %: 0.74 [0.52, 0.91] (8 eyes) vs 0.81; top 15 %: 0.70 [0.53, 0.86] vs 0.79; top 20 %: 0.70 [0.53, 0.84] vs 0.77.
  - Baseline lesion size alone is not correlated with growth rate here (r = −0.10).
  - All other arms similar (r 0.33–0.47, overlapping intervals) ⇒ the gap belongs to the approach, not to one operator.
- The comparison is an anchor, not a head-to-head result. The claim that this thesis's growth-region Dice is higher than Mai's has **not been verified** — do not make it (Mai's growth-region DSC per bin: 0.25 / 0.38 / 0.38 / 0.37 for 0–1 / 1–2 / 2–3 / >3 y; this thesis's per-bin values are pooled differently — do not compare them numerically; leave a `% TODO`).
- Author's summary for §6.2: **"good at *where*, weaker at *how fast*"** — the survey optimises where the lesion changes at one year, but per-eye growth speed over multi-year follow-up is only moderately captured, for every arm alike, even though the model starts from segmented masks.

### 4.9 Cost facts (for §5.6)
- Convention: cost = **minimum epoch time over the five folds** of an arm, fold named where known. The mean is not used: a run's epoch times carry a near-constant additive overhead (17–64 s) that would penalise cheap operators disproportionately. An earlier explanation of the spread by GPU co-scheduling was checked and **refuted** (no two runs ever shared a GPU) — do not repeat it as an explanation; you may say the spread has two measured causes: per-fold work differs (280 / 320 / 300 / 300 / 320 optimiser steps per epoch for folds 0–4, because an epoch is 20 passes over the fold's training eyes in batches of 4) and the additive overhead. Normalised by steps, the per-fold minimum epoch times are flat to about 3 %. Figures therefore support **order-of-magnitude statements only**.
- All runs on NVIDIA RTX A6000 GPUs, 30 epochs per run.
- Numbers: see the s/epoch column in §4.4. Ratios: RK4 over the stencil network 439 vs 91 s ≈ **4.8×**; RK4 over the FNO 45 vs 23 s ≈ 2× (the factor ≈ 4.8 holds where the backbone's forward pass dominates the epoch); T-FEN vs stencil 367 vs 91 s ≈ **4×**; U-Net 21 s ≈ 0.23× the stencil network (the cheapest spatial operator); dual branch (Appendix G) ~10× its single-branch twin. Capacity: 30–55 % more compute for the layer encoder (qualitative mention only).
- **Not measured:** inference time per rollout step and memory footprint. Say so in one sentence; do not estimate them.

### 4.10 Open items that the Discussion must mention (limitations)
Data quantity (75 eyes, 51 patients, 12–20 validation eyes per fold; no test split); fellow eyes make per-eye statistics somewhat optimistic; the one-year anchor has no upper horizon bound; crop censoring (numbers in §4.1); the unverified spacing constant behind every mm² value; mask provenance and unrecorded layer-boundary names; local shrinkage of the reference masks not yet quantified (noise vs biology); one visit in, no trajectory memory; covariates enabled but their value unsettled; the pipeline starts from segmented masks (errors of an upstream segmentation are not modelled, and the comparison with raw-OCT models is not like-for-like); the change-region Dice was logged only as a cohort mean per run, so the per-eye instrument uses the growth-region Dice; several findings are fold-2 or single-seed (solver-swap, some ladders); pending replications (seed-7 T-FEN in the energy-conserving form, seed-7 matched transport control, objective and Δt ablations on the canonical network, T-FEN capacity in the new form); arms not run (a plain recurrent network, a transformer; PINNs deliberately not run because the governing equation is unknown and the residual would be taken on a binary mask); the moving-mesh null is implementation-scoped.

---

## 5. What to write, section by section

### A. §5.6 Computational Cost (`05-experiments.tex`)
Starts with exactly:
```latex
\section{Computational Cost}
\label{sec:experiments:cost}
```
Content: the cost convention and why (§4.9), what the numbers can and cannot support, the table's cost column read as order of magnitude (cheapest spatial operator U-Net ~21 s; graph networks ~76–108 s; FEN arms 180–367 s; RK4 wrappers), the estimator-independent ratios (RK4/Euler ≈ 4.8×, T-FEN/stencil ≈ 4×, dual branch ≈ 10× → Appendix~\ref{app:mm-pde}), the observation that none of the expensive variants (RK4, T-FEN's extra cost, the dual branch, wider models) bought accuracy beyond the noise except the T-FEN's tie at ~4× the cost of the stencil network, and one sentence that inference time and memory were not measured. You may add one small table (ratios) if it helps; otherwise prose. No new labels except optionally `tab:experiments:cost`.

### B. Chapter 6, Discussion (`06-discussion.tex`)
Keep the chapter header and the four `\section`/`\label` lines exactly:
```latex
\cleardoubleoddpage%  Make sure to start each chapter on a new odd page
\chapter{Discussion}
\label{ch:discussion}
\section{Interpretation of Results}        \label{sec:discussion:interpretation}
\section{Clinical Implications}            \label{sec:discussion:clinical}
\section{Limitations}                      \label{sec:discussion:limitations}
\section{Future Work}                      \label{sec:discussion:future}
```
You may add `\subsection`s or `\paragraph`s inside them (keep them few).

**6.1 Interpretation of Results (~2–3 pages).** Answer the research question at the level of meaning, not by repeating Chapter 5.
- Sub-question (1), the framework: what transferred. The $\Delta t$-conditioned residual update, persistence start, elapsed-time curriculum and shared evaluation made unrelated architecture classes comparable and all of them learn (every spatial arm far above persistence). The details of the time handling did not matter (RK4 null, Δt-multiplication argued as reparameterisation — pending run, TODO). What the framework needs is that elapsed time reaches the operator and that everything else is held fixed.
- Sub-question (2), the operator: why the ingredient reading beats the architecture reading. The operator class did not decide the outcome; the ingredients did. Interpret the "two routes to one deficit": the deficit is a scale mismatch between what one update can see and how far the front moves between visits — which is exactly the CFL-type argument from classical numerics (Chapter 2 made it as an expectation; it can now be discussed as borne out). Physical reach and explicit transport are two ways to meet it. Global+local: why a purely global operator underperforms at one year but not at long horizons (descriptive).
- Why capacity was not a factor, and what that says about the low-data inductive-bias argument (75 eyes: the prior matters more than size; say this as interpretation, not proof).
- The $\theta_{\text{PDE}}$ point (**author: must be included**): in MP-PDE, the equation-coefficient vector lets one solver generalise across a family of equations. GA has no governing equation, so there is no counterpart; $\Delta t$ and the covariates fill the slot, and the learned stand-in (layer encoder) was not effective in its only tested design. Discuss what is lost without it (e.g. eye-specific speed information — link to the growth-speed gap in 6.2) and what could fill it (patient- or lesion-level descriptors that vary across eyes). Qualitative only.
- Time consistency (author TODO): two attempts to make predictions meaningful between visits — the intermediate-time-point regulariser (removed, no benefit) and the autonomous RK4 arm (passes the solver-swap test, same accuracy, ~4.8× cost). If intermediate-time predictions are needed clinically, the RK4 variant (or the energy-conserving T-FEN) is the principled choice, but their in-between predictions are unverified (no ground truth between visits).
- What the nulls collectively imply about where modelling effort should go (geometry/reach and transport, not message functions, capacity, integration order or mesh machinery).

**6.2 Clinical Implications (~1–1.5 pages).**
- "Good at where, weaker at how fast": interpret the Mai comparison with all caveats; triage of fast progressors needs growth speed; possible reasons (drift of local models over multi-year rollouts, crop censoring of large lesions, no trajectory memory, no eye-specific conditioning) — as hypotheses.
- Which horizon is reliable: the one-year anchor is where everything is measured; the horizon bins show growth-region Dice does not collapse beyond one year (descriptive values from §4.5), but no statement about clinical usefulness thresholds can be made — say there is no established clinically meaningful Dice threshold for GA progression forecasts (as an observation, no citation needed; if you want one, TODO-cite).
- The pipeline starts from segmented masks: in practice it would sit behind a segmentation model; what that means.
- Where failures would matter: border-touching lesions (censoring), fast progressors, sparse schedules. Keep it qualitative; per-eye failure analysis (§5.5 qualitative) is not written yet → you may point to `\S\ref{sec:experiments:qualitative}` only generally.
- Complement-inhibitor era: a per-eye spatial forecast is relevant for trial enrichment and treatment decisions — one or two sentences, cite from the allowed list (Lad2023, Vallino2024, Singh2025) only if the claim matches what they are (treatment/epidemiology reviews).

**6.3 Limitations (~1.5–2 pages).** Everything in §4.10, grouped (data and labels; evaluation; model scope; unfinished replications). Honest, no apology. Include the crop-censoring paragraph with its numbers and the statement that the border-vs-interior split is not reported (ranking unchanged on interior eyes). Include the trajectory-memory point (5–13 visits per eye). Include the covariates point as specified in §4.6.

**6.4 Future Work (~1 page).** Include all of the following (author's list): a better spatial pre-processing than the fixed 49 × 1024 crop (e.g. a larger/adaptive window with a pad mask, or registration-aware cropping); a model with trajectory memory (several past visits or a recurrent state), plus the two unrun arms (recurrent network, transformer); a learned eye-level summary as a $\theta_{\text{PDE}}$ stand-in, designed to see observed rather than predicted layers, correct the anisotropy, or condition locally (link to 6.1); a transport model that is numerically valid over long horizons with an interpretable velocity field (bounded velocity parameterisation; the energy-conserving form as the starting point); learning from raw OCT (end to end or jointly with segmentation) to close the gap to Mai et al.; 3-D volumetric OCT; uncertainty quantification for clinical use; multi-task training across retinal pathologies; for the moving mesh, one sentence: a monitor that uses a surrogate of the next state (the future-state problem noted by Hu2024) → Appendix~\ref{app:mm-pde}.

### C. Chapter 7, Conclusion (`07-conclusion.tex`)
Header:
```latex
\cleardoubleoddpage%  Make sure to start each chapter on a new odd page
\chapter{Conclusion}
\label{ch:conclusion}
```
No sections needed (or at most two unnumbered paragraphs groups). ~2–3 pages. Restate the research question verbatim (§2), answer (1) and (2) directly in a few sentences each, summarise the four ingredients with their key number (reach +0.064 at equal parameters, the largest effect; transport +0.062 and against a matched control on four folds; global + local at +800 parameters; spatial context from 0 to ~0.45), the central result (two routes to one deficit; architecture class does not decide), the negative results as part of the contribution (time-integration order, capacity, the objective's details as tested, the moving mesh in the appendix, validity: the canonical model is a one-step map, not an ODE), the honest clinical position (where vs how fast; starts from masks), and close on the take-away: *for longitudinal medical-imaging forecasts in a low-data clinical regime, what matters is the framework around the model and the inductive-bias ingredients of the operator — especially whether one update can see as far as the disease moves between visits — not the choice of operator family.* No new numbers, no new claims, no citations needed beyond Mai2024 / Brandstetter2022 if any.

### D. Abstract and Kurzfassung (`00-abstract.tex`)
Replace only the `% TODO` comments inside the two `abstract*` environments; keep the environments and the `otherlanguage{ngerman}` wrapper exactly as below:
```latex
\cleardoubleoddpage%  Make sure to start abstract on a new odd page
\begin{abstract*}
...English...
\end{abstract*}
...
\cleardoubleoddpage%  Make sure to start abstract on a new odd page
\begin{otherlanguage}{ngerman}
\begin{abstract*}
...Deutsch...
\end{abstract*}
\end{otherlanguage}
```
English: 4 short paragraphs — problem (GA, irregular visits, per-eye spatial forecast from longitudinal OCT, low data); approach (fixed $\Delta t$-conditioned autoregressive framework with one swappable operator slot; parameter-matched survey of graph networks, U-Net, FNO, finite-element networks; 5-fold CV on 75 eyes of 51 patients from the MUW cohort); findings (framework transfers, three unrelated classes close together at the top, 0.50–0.54 change-region Dice at one year vs 0 for persistence; physical reach at lesion scale largest effect; transport term as independent route; global + local; nulls: capacity, integration order, moving mesh in appendix); clinical position (captures where more than how fast; r = 0.40 vs 0.61 for a raw-OCT model on the same cohort, with the input caveat). No citations, no `\ref`, no abbreviations without expansion (write "optical coherence tomography (OCT)" and "Geographic Atrophy (GA)" once). Passive voice.
German: a faithful translation in natural academic German (Passiv/unpersönlich, keine "wir"); use German typographic quotes if any (`\glqq … \grqq{}`) and decimal commas in numbers (0,51 statt 0.51). Keep technical terms where German usage keeps them (U-Net, Fourier Neural Operator, Finite-Elemente-Netzwerk, Graph-Netzwerk, Dice, Autoregression).

---

## 6. Output format

Return four fenced code blocks, in this order, each containing **only** the LaTeX for that file/part:
1. `%% === 05-experiments.tex : replace the \section{Computational Cost} block ===`
2. `%% === 06-discussion.tex : full file ===` (include the `%%%%` banner lines at top and bottom as in the other chapters)
3. `%% === 07-conclusion.tex : full file ===`
4. `%% === 00-abstract.tex : full file ===`

Then the plain-text report (§1). Do not add explanations between the blocks.

Before you answer, check your draft against the 14 hard rules in §3.3 and against the label and citation-key lists in §3.2. Every `\citet`/`\citep` key and every `\ref` label must appear in those lists.
