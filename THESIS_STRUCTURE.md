# Master Thesis Structure

## Status

- [ ] Front Matter (title page, abstract, acknowledgements)
- [ ] 1. Introduction
- [ ] 2. Background
- [ ] 3. Data and Preprocessing
- [ ] 4. Method
- [ ] 5. Experiments
- [ ] 6. Discussion
- [ ] 7. Conclusion
- [ ] Bibliography
- [ ] Appendices

---

## Framing (revised 2026-09-17)

**The thesis question is "what does a model need in order to predict GA progression, and what framework does it need to sit in?" — not "can MP-PDE/MM-PDE be adapted to GA?".** The adaptation of the two solver frameworks is still the largest single block of engineering and keeps its full technical chapter, but what it produced is a **fixed experimental framework with one swappable operator slot**, and what the thesis reports is a controlled survey through that slot. Chapters 4 and 5 are structured accordingly: §4.3 (the graph solver the project built) and §4.4 (everything else, on identical terms) are two halves of one chapter, not a subject and its appendix.

Several originally-planned contributions are **measured nulls** and must be written up as negative results rather than contributions: mesh adaptation / the dual branch, patient covariates, the learned surrogate encoder, parameter count, time-integration order, and every GNN-internal knob. See `NOTES.md` → "Code-side sync (2026-09-17)" for the binding vocabulary rules, and `THESIS_FRAMEWORK.md` §7.5 for every number with its instrument and caveat.

**Narrative Constraint:** This thesis must strictly follow the "Hour-Glass" model:
1. **Introduction:** Start broad (general context) -> narrow down to the specific research gap and question.
2. **Methods & Results:** Maximum technical depth and specificity.
3. **Discussion:** Broaden back out -> interpret results, admit weaknesses, and discuss broader implications for the field.

## Front Matter

- **Title page** — Thesis title, your name, supervisor(s), institution (Johannes Kepler University), date.
- **Abstract** — One paragraph each on: problem (GA progression prediction), approach (a Δt-conditioned autoregressive framework with a swappable operator, surveyed across six architecture classes), key contributions (the framework itself, physical reach at lesion scale, global+local context, the transport term, and the reported nulls), headline results.
- **Acknowledgments** — Medical University of Vienna, specifically Supervisor Hrvoje Bogunović and Co-supervisor Dmitrii Lachinov.
- **Table of contents / List of figures / List of tables / List of abbreviations** — Auto-generated.

## 1. Introduction (~6-8 pages)

### 1.1 Clinical motivation
Brief explanation of Geographic Atrophy as an advanced form of age-related macular degeneration, its prevalence, and why predicting lesion progression matters for patient management and treatment planning.

### 1.2 Problem statement
Frame GA progression as a spatiotemporal prediction task on OCT en-face grids: given a baseline state and elapsed time, predict the future lesion configuration. State the irregular-visit-interval challenge clinical data imposes.

### 1.3 Why a PDE-solver framing, and why a survey
Argue that GA progression has the structural properties of a locally driven growth process (spatial state evolving over time with local dynamics) and that neural PDE solvers offer a principled inductive bias in a low-data clinical regime. **Then make the turn that defines the thesis:** a single architecture cannot answer whether that prior is the right one, so the work fixes everything except the update operator and surveys the slot. State the research question in its current form — what a model needs, and what framework it needs to sit in. Be honest about provenance: the two frameworks were initially suggested by the clinical partner; the locality/inductive-bias justification was built and tested empirically afterwards.

### 1.4 Contributions
Bulleted list, rewritten against the measured results:
- A Δt-conditioned autoregressive framework for irregular clinical visit schedules, with a persistence-exact initialisation, that makes architecture classes comparable under one loss, curriculum, evaluation and parameter budget.
- The first controlled comparison of six architecture classes on longitudinal OCT GA progression, parameter-matched, 5-fold, with two agreeing statistical instruments and a replicate noise floor.
- The identification of **physical reach at lesion scale** as the dominant ingredient — the largest effect in the project, obtained at fewer parameters by changing only the graph's edge set.
- The finding that **global context and local detail are separable and both required**, demonstrated by two architecturally unrelated constructions landing at the same place.
- An explicit **transport term** as a second, independent route to the same deficit (with its parameter-matching caveat stated in the same breath).
- A set of **reportable negative results**: mesh adaptation, patient covariates, the learned coefficient surrogate, capacity, integration order, and every GNN-internal knob.
- The transfer of the MM-PDE/MP-PDE machinery to a multi-channel clinical state on an extremely anisotropic grid, as the engineering that made the above measurable.

### 1.5 Thesis outline
One-paragraph roadmap of the remaining chapters.

## 2. Background (~12-15 pages)

### 2.1 Geographic Atrophy and OCT imaging
Clinical background: what GA is, how it's imaged (OCT volumes, en-face projections), what the 10 retinal layer boundaries represent, how masks are annotated. Reference the MUW dataset structure.

### 2.2 Partial differential equations and numerical solvers
Short primer on temporal PDEs, the method of lines, finite differences/volumes, and mesh-based discretization. Just enough to motivate what neural solvers replace. **Constraint: Do not detail historical PDE origins or generic equations (e.g., heat/wave equation). Focus strictly on spatial grids and time-stepping as they relate to discrete, autoregressive state updates. When an example is needed for explanations, always use the Shallow Water Equation (SWE) as we have relevant examples and potential visualizations.**

### 2.3 Neural PDE solvers and surrogate architectures
Widened from the original "operators vs autoregressive" framing so that every class later surveyed in §4.4 has its background here: neural operators (FNO, DeepONet), autoregressive solvers (MP-PDE), the U-Net as the standard strong surrogate baseline in this literature, finite-element / transport-based networks, and the Neural-ODE reading of a residual update. Explain why autoregressive is the right framing for clinical longitudinal data, and introduce the notion of an *inductive-bias ingredient* that the survey later measures.

### 2.4 MP-PDE: Message-Passing Neural PDE Solvers
Focused summary of Brandstetter et al. (2022): encode-process-decode architecture, temporal bundling, the pushforward trick and its zero-stability interpretation.

### 2.5 MM-PDE: Moving Mesh PDE Solvers
Focused summary of Hu et al. (2024): DMM (data-free mesh mover trained on the Monge-Ampère equation), the monitor function and equidistribution principle, the dual-branch architecture with ItpNet, interpolation between uniform and moved meshes.

### 2.6 Related work
Short section on: deep learning for retinal imaging, GA progression models in the clinical literature (including Mai et al. 2024 as the direct comparison on the same cohort), other neural solvers applied to biomedical problems (if any).

## 3. Data and Preprocessing (~8-10 pages)

### 3.1 Dataset
MUW GA cohort description: patients, eyes, visits, visit-interval distribution, demographic breakdown, and the cohort's lesion-scale statistics (baseline-area distribution, growth-rate distribution). Include a figure showing an example OCT en-face with mask and layer overlays. **Constraint: pixel counts vary per eye (38-66 B-scans x 961-1719 A-scans across 553 visits, 67 distinct shapes); no visit is natively 49x1024. State the constant-spacing assumption as an assumption, not a measurement — it is verified only against the cohort's own transforms, to ~2 %.**

### 3.2 State representation
Define the 11-channel state tensor: channel 0 (binary mask) and channels 1-10 (layer depths). Justify this choice as capturing both the pathology and its structural context. **Constraint: Focus strictly on the clinical/data definition here. Do not discuss how these channels propagate through the network (reserve for 4.2).**

### 3.3 Spatial standardization and its measured cost
Center-crop/pad to the canonical (49, 1024) grid. **Constraint: Explicitly state that we crop/pad instead of resampling to keep the en-face pixel spacing strictly invariant across all patients, giving a fixed physical window of ≈5.94 x 5.82 mm.**

**Constraint (corrected 2026-09-17 — the previous justification was false as measured and must not appear):** do **not** claim the discarded periphery is clinically irrelevant. Report the census instead: the window cuts real lesion area in **27.3 %** of visits (more than 5 % of the lesion in 6.0 %, worst case 25.7 %), and **31.1 %** of cropped lesions touch the crop border, so growth across it is censored with no missingness flag. Frame the 49x1024 choice as a deliberate trade-off — larger windows trade truncation for up to 35 % zero-pad and ~1.9x the node count, and ~19 % border-touch is irreducible — and point forward to how the consequences are handled downstream (border-touching vs interior split of the change-region metric, the pad-masked `_anat` variant, optional pad-node loss masking).

### 3.4 Normalization
Per-channel z-score normalization from training-split statistics. Table with the computed mean/std per channel.

### 3.5 Patient-level covariates
Age and sex extraction from the patient index. Training-split z-score for age, binary encoding for sex, mean imputation for missing values. Note the per-visit vs baseline age encoding and that both are later measured (§5.4, negative results).

### 3.6 Temporal structure
Visits ordered per eye, $\Delta t$ computed between consecutive visits in years. Consecutive (state_i, state_{i+1}, $\Delta t$) triples form the training windows.

### 3.7 Splits and cross-validation
Patient-level splitting (not eye-level) to prevent leakage across an individual's two eyes. **Constraint: the protocol is 5-fold train/validation cross-validation and the "test" split is structurally empty — state this plainly here and again in §5.1, and do not describe results as test-set performance anywhere in the thesis.**

## 4. Method (~18-22 pages)

### 4.1 Overview: one framework, one swappable slot
One figure showing the pipeline with the operator slot drawn explicitly as the only thing that varies: state in -> (fixed) encoding and conditioning -> **$f_\theta$** -> (fixed) Δt-scaled residual update -> next state. State the design contract: loss, curriculum, evaluation, model selection and bookkeeping live in one shared pipeline that a backbone is forbidden to duplicate, which is what makes the comparison controlled. Reference every component to its detailed subsection, and note that the bit-identical persistence fingerprints across arms are the evidence the contract held.

### 4.2 What is fixed: the framework
The part that is common to every arm and that demonstrably transfers.
- **$\Delta t$-conditioned residual formulation.** `u_{t+\Delta t} = u_t + \Delta t * f_\theta(u_t, \Delta t)`, replacing the fixed-step rollout of MP-PDE/MM-PDE. Why this replaces absolute time, why the persistence limit at $\Delta t \to 0$ is the right one, and why the head is zero-initialised so every model starts at exact persistence.
- **Multi-channel propagation.** How C=11 channels move through the pipeline at the tensor level: dataset layout, feature construction, per-channel treatment. **Constraint: the clinical meaning of the channels was established in §3.2; this is mathematics and tensors only.**
- **One visit in, no history**, and why (short clinical sequences).
- Pointer forward to the shared loss and curriculum (§4.7) and shared evaluation (§5.1).

### 4.3 Backbone I: the GA-adapted MP-PDE graph solver
The arm the project built rather than imported, in full detail — encoder, message passing, decoder, the Δt-conditioned output head. Explicitly note that the original MP-PDE's temporal bundling is removed entirely (strict K=1) because clinical sequences are short and a moved mesh computed from a single snapshot would be stale for later steps in a window.

**The graph construction is the load-bearing part of this section**, not an implementation detail: the ~21:1 pixel-spacing anisotropy means an index-space k-NN hop reaches ±0.25 mm across B-scans but only ±0.011 mm along them, against a GA front that advances a median ~12 columns per visit. Present the index-space k-NN as the v1 construction and the dilated physical-scale stencil (rows ±1 x columns {0, ±7, ±14, ±21}) as the v2 lock, deriving the offsets from the lesion scale rather than presenting them as a hyperparameter. This is where §5.3's largest effect is set up.

### 4.4 Backbone II: the countermodel family
Everything else that occupies the same slot, described on identical terms and at comparable depth — this section carries equal weight with §4.3.
- The shared backbone contract every module satisfies.
- **Dense countermodels:** U-Net (at two capacities), FNO, and the FNO + 3x3 local-kernel hybrid.
- **Graph countermodels and the floors:** the graph U-Net, and the per-pixel model with no spatial context as the lower floor.
- **The Finite Element Network**, free-form and with the learned transport (advection) term.
- **Time integration:** the fixed-step Runge-Kutta wrapper over any backbone, and what a continuous-time reading would require.
- **Parameter matching:** what is matched to what, the 1.25x band, and the two deliberate out-of-band controls (44x U-Net, 0.22x per-pixel floor) and why each exists.

### 4.5 The moving-mesh extension as a tested hypothesis
DMM + dual branch, framed from the outset as a hypothesis the design was built to measure rather than a component assumed to help.
- **DMM for GA:** the physics loss (Monge-Ampère + boundary + convexity), sampling strategy, and the monitor function. **Constraint: the monitor is a plain scalar monitor on the Gaussian-blurred mask, and the DMM trains and is applied on the native anisotropic (49, 1024) grid (since 2026-08-04). The multi-channel Frobenius-norm monitor and the square 256² SLO-mask path are superseded — mention them, if at all, only as documented intermediate steps, and never as the design.** DMM is pretrained separately and frozen.
- **Dual-branch composition:** main branch on the uniform mesh returning the full next state; correction branch on the moved mesh returning a pure Δt-delta; ItpNet interpolation renormalised to a partition of unity; the learnable scalar gate α, zero-initialised, which is the instrument that makes the question measurable. **Constraint: `res_cut` is gone from the framework entirely — do not describe it as a component.**
- State the pre-registration explicitly: α -> 0 was a pre-registered reportable outcome, and §5.4 reports what it actually measured.

### 4.6 Conditioning: covariates and the coefficient surrogate
Age and sex as graph-level attributes broadcast per node into the `variables` vector; the LayerEncoder CNN compressing the 10 layer maps into a global embedding concatenated the same way, framed as a learned stand-in for the PDE coefficients $\theta_{PDE}$ of MP-PDE. Describe both as implementation deltas whose value is an open question at this point in the text; §5.4 reports both as nulls. Note the encoder's stride schedule corrects only ~2x of the image's ~21:1 anisotropy, which bounds what the null covers.

### 4.7 Training
The channel-weighted MSE + soft-Dice objective, the time-budgeted pushforward curriculum (unroll depth measured in elapsed days, not visit count), ItpNet pretraining at epoch 0 for the dual branch, per-module gradient clipping, optimizer and schedule. Note that the explicit monotonic-growth penalty is set to 0.0 and the residual form is signed — what the zero-init biases toward is *persistence*, not monotonicity.

### 4.8 Implementation details
Hardware, framework versions, the run-identity/checkpoint/resume infrastructure, and notable engineering choices (GPU-native k-NN, graph precomputation, anisotropy-corrected edge construction, etc.).

## 5. Experiments (~18-22 pages)

### 5.1 Evaluation protocol
**Crucial Context, in this order:**
1. Why per-pixel MSE is a deceptive metric for slow-moving GA pathology, and why the persistence baseline is the floor any learned model must beat.
2. **Never quote raw RMSE across arms** — the dense arms decalibrate far more under autoregression than the graph arms, so raw-scale comparisons measure the decalibration, not the prediction.
3. The clinical metrics: change-region Dice and IoU on the GA mask at the 360-day anchor, √area MAE, growth-rate agreement. Note that the @360d metric has no upper horizon bound (7/75 eyes scored at 450-720 d).
4. **The two statistical instruments, always quoted together:** the fold-paired 5-fold mean ± between-fold SE (threshold 0.016; single fold 0.036) and the pooled per-eye test over 75 eyes, with leave-one-fold-out robustness. A result graduates only when both agree. State the ±0.0127 replicate noise floor.
5. **The era rule:** comparisons are valid only within an era; pre-fix runs are not comparable.
6. 5-fold CV, no test split (repeat from §3.7).

### 5.2 The arm table and main results
The nine settings of the operator slot presented as one table: change-region Dice@360d (5-fold mean ± SE), the per-eye instrument, parameter count and its ratio to the locked model, and cost. **Constraint: quote cost as the minimum epoch time of the cheapest fold and name the fold; the mean carries a near-constant additive overhead that systematically penalises cheap architectures. The GPU co-scheduling explanation for the spread is refuted — do not repeat it.** Include a figure with example rollouts (ground truth vs a representative subset of arms) for a representative eye.

The headline this table supports: the three strongest arms are statistically indistinguishable, and a model with no spatial context is bit-exactly persistence. Architecture class does not decide the outcome.

### 5.3 The ingredient study
The core of the chapter: what actually separates arms, measured one at a time.
- **Spatial context at all** — the locality cliff (0 / 1 / 2 message-passing layers).
- **Physical reach at lesion scale** — the dilated stencil against the index-space k-NN, with the reach ladder showing ±21 columns as a measured optimum, at fewer parameters, from changing only the edge set.
- **Global context and local detail together** — the FNO's position below the U-Net, and the +800-parameter local bypass that brings it level and makes it the only arm to win every fold.
- **An explicit transport term** — the T-FEN against its free-form control, including the near-term growth bin it recovers. **Constraint: this is the one architecture comparison that is not parameter-matched (1.97x); say so every single time the number is quoted.**
- Close on the convergence argument: reach and transport are two independent routes to the same deficit, and that coincidence — not any single arm's score — is the central architectural result.

### 5.4 Negative results
Reported as findings, not as failures, each with its instrument and its scope.
- **Mesh adaptation / the dual branch.** The tightest null in the project, parameter-matched, at ~10x the cost. **Constraint on scope: α stays shut in the parameter-matched bypass control as well as in the mesh arm, so what the gate measured is the correction branch's failure to optimise — not "mesh adaptation does not transfer to GA". Weight decay is refuted as the cause.**
- **Patient covariates** — both instruments agree, neither graduates, and the residual points against them.
- **The learned coefficient surrogate** — null at every width over an 8x range, at 30-55 % more compute.
- **Capacity** — the 44x U-Net erases its own smaller twin's win.
- **Time-integration order** — RK4 vs Euler null over both a local graph operator and a global spectral one, at ~4.8x the cost.
- **Every GNN-internal knob** — normalisation, aggregation, edge-direction features. The geometry mattered; the message function did not.
- **The intermediate-time-point regulariser** — evaluated and removed.

### 5.5 Moving mesh quality
The DMM judged on its own terms, independent of whether the dual branch helped: equidistribution CoV, tangled-cell counts, geometric quality, capacity/overfitting behaviour across branch architectures and seeds. Visualise example moved meshes overlaid on sample states. This is what licenses the §5.4 null being read as "the correction branch did not engage" rather than "the mesh was bad".

### 5.6 Validity diagnostics
Results that are not accuracy numbers but that determine what may be said.
- **The solver-swap (ODE-validity) diagnostic** — the locked model fails, the autonomous-RK4 arm passes, and that arm is a null on accuracy. **Constraint: this is what forbids "ODE", "rate field" and "learned dynamics" language for the locked model and every headline result.**
- **The T-FEN's numerical validity** — free-running divergence and Courant-bound violations at the longer step. The Dice contribution stands; **the learned velocity map is not quotable.**

### 5.7 Qualitative analysis and clinical comparison
Per-eye rollout visualizations. Success cases and failure modes (atypical progression, sparse schedules, very short vs long $\Delta t$, border-censored lesions). Comparison against Mai et al. 2024 on the same cohort and task, **with the mandatory caveat that this model consumes pre-segmented masks whereas Mai works from raw OCT** — which is part of why a local model suffices here.

### 5.8 Computational cost
Training time, inference time per rollout step, memory footprint, per arm, under the stated cost convention. The three estimator-independent ratios (dual/single ≈ 10x, RK4/Euler ≈ 4.8x, T-FEN/stencil ≈ 4x) and the cheapest-arm comparison.

## 6. Discussion (~6-9 pages)

### 6.1 Interpretation of results
*Broaden back out.* Why the ingredient reading beats the architecture reading. What it means that two unrelated constructions correct the same deficit to the same place. Why capacity was not a factor, and what that says about the low-data inductive-bias argument. What the nulls collectively imply about where modelling effort should go.

### 6.2 Clinical implications
What prediction horizon is reliable, what Dice level would be clinically useful, where the model fails and whether those failures would matter in practice. Be explicit that the pipeline starts from segmented masks.

### 6.3 Limitations
Data quantity; **no test split**; the @360d horizon's upper bound; **crop censoring and its effect on both training supervision and the reported metrics**; the unverified spacing constant behind every mm² figure; the missing anatomical names of the layer boundaries; the T-FEN's unmatched capacity control and its unquotable velocity; **ground-truth GA retraction, which contradicts a strict monotonic-growth reading and needs quantifying (segmentation noise vs biology)**; the scope limits on the mesh null; the fixed grid discarding peripheral retina; the encoder seeing predicted rather than observed layers during unrolling; and the arms still unrun (a plain RNN, a transformer).

### 6.4 Future work
Incorporating surrogate models of the next state into the monitor function (the future-state problem from MM-PDE's conclusion), a matched-capacity transport control and a numerically valid long-horizon transport model, extending to 3D volumetric OCT, learning from raw OCT rather than masks, multi-task joint training across retinal pathologies, and uncertainty quantification for clinical deployment.

## 7. Conclusion (~2-3 pages)
Restate the question and what the survey answered: the framework transfers, the architecture class does not decide the outcome, and the ingredients that do — spatial context, physical reach at lesion scale, global and local context together, and an explicit transport term — are measurable and transferable. Summarise the negative results as part of the contribution. Close on the take-away: for longitudinal medical imaging prediction in a low-data clinical regime, what to get right is the framework and the inductive-bias ingredients, not the choice of operator family.

## Bibliography
BibTeX file. Expect 40-80 references: clinical GA literature, OCT imaging, PDE numerical methods, neural PDE solvers (MM-PDE, MP-PDE, FNO, DeepONet), U-Net and surrogate baselines, finite-element/transport networks, Neural ODEs and Runge-Kutta references, GNN foundations, retinal deep learning. `THESIS_FRAMEWORK.md` §10.1 is a curated works-cited list with full bibliographic detail for everything the framework leans on.

## Appendices

- **A. Dataset details** — Full demographic tables, visit-interval histograms, per-channel statistics, the crop-censoring census, lesion-area and growth-rate distributions.
- **B. Extended derivations** — Monge-Ampère equation, the monitor function, pushforward stability argument, the Courant/CFL bound used to read the transport velocity.
- **C. Full hyperparameters** — Everything not in the main text: all architecture widths per arm, all training schedules, random seeds, the parameter-matching table.
- **D. Additional rollout figures** — Extra qualitative examples, including failure cases.
- **E. Full result tables** — Per-fold and per-eye readouts for every arm and every ablation, not just the headline numbers; both instruments side by side.
- **F. Code structure** — Brief map of the repository, pointer to GitHub, reproducibility instructions, and the run-identity scheme that maps each reported number to its run.
