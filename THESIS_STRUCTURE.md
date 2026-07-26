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

**Narrative Constraint:** This thesis must strictly follow the "Hour-Glass" model:
1. **Introduction:** Start broad (general context) -> narrow down to the specific research gap and question.
2. **Methods & Results:** Maximum technical depth and specificity.
3. **Discussion:** Broaden back out -> interpret results, admit weaknesses, and discuss broader implications for the field.

## Front Matter

- **Title page** — Thesis title, your name, supervisor(s), institution (Johannes Kepler University), date.
- **Abstract** — One paragraph each on: problem (GA progression prediction), approach (adapt MM-PDE/MP-PDE to medical imaging), key contributions ($\Delta t$-conditioning, multi-channel, surrogate encoder), headline results.
- **Acknowledgments** — Medical University of Vienna, specifically Supervisor Hrvoje Bogunović and Co-supervisor Dmitrii Lachinov.
- **Table of contents / List of figures / List of tables / List of abbreviations** — Auto-generated.

## 1. Introduction (~6-8 pages)

### 1.1 Clinical motivation
Brief explanation of Geographic Atrophy as an advanced form of age-related macular degeneration, its prevalence, and why predicting lesion progression matters for patient management and treatment planning.

### 1.2 Problem statement
Frame GA progression as a spatiotemporal prediction task on OCT en-face grids: given a baseline state and elapsed time, predict the future lesion configuration. State the irregular-visit-interval challenge clinical data imposes.

### 1.3 Why neural PDE solvers?
Argue that GA progression has the structural properties of a PDE system (spatial state evolving over time with local dynamics) and that neural PDE solvers offer a principled inductive bias compared to generic segmentation-style baselines.

### 1.4 Contributions
Bulleted list: first application of moving-mesh neural PDE solvers to medical imaging, $\Delta t$-conditioned residual formulation for irregular visit schedules, multi-channel generalization of the MM-PDE pipeline, patient covariate conditioning, learnable layer-geometry encoder as a surrogate for PDE coefficients.

### 1.5 Thesis outline
One-paragraph roadmap of the remaining chapters.

## 2. Background (~12-15 pages)

### 2.1 Geographic Atrophy and OCT imaging
Clinical background: what GA is, how it's imaged (OCT volumes, en-face projections), what the 10 retinal layer boundaries represent, how masks are annotated. Reference the MUW dataset structure.

### 2.2 Partial differential equations and numerical solvers
Short primer on temporal PDEs, the method of lines, finite differences/volumes, and mesh-based discretization. Just enough to motivate what neural solvers replace. **Constraint: Do not detail historical PDE origins or generic equations (e.g., heat/wave equation). Focus strictly on spatial grids and time-stepping as they relate to discrete, autoregressive state updates. When an example is needed for explanations, always use the Shallow Water Equation (SWE) as we have relevant examples and potential visualizations.**

### 2.3 Neural PDE solvers
Two-subsection overview: neural operators (FNO, DeepONet — briefly, as context) versus autoregressive solvers (MP-PDE). Explain why autoregressive is the right framing for clinical longitudinal data.

### 2.4 MP-PDE: Message-Passing Neural PDE Solvers
Focused summary of Brandstetter et al. (2022): encode-process-decode architecture, temporal bundling, the pushforward trick and its zero-stability interpretation.

### 2.5 MM-PDE: Moving Mesh PDE Solvers
Focused summary of Hu et al. (2024): DMM (data-free mesh mover trained on the Monge-Ampère equation), the monitor function and equidistribution principle, the dual-branch architecture with ItpNet, interpolation between uniform and moved meshes.

### 2.6 Related work
Short section on: deep learning for retinal imaging, GA progression models in the clinical literature, other neural solvers applied to biomedical problems (if any).

## 3. Data and Preprocessing (~8-10 pages)

### 3.1 Dataset
MUW GA cohort description: number of patients, eyes, visits per eye, visit interval distribution, demographic breakdown. Include a figure showing an example OCT en-face with mask and layer overlays.

### 3.2 State representation
Define the 11-channel state tensor: channel 0 (binary mask) and channels 1-10 (layer depths). Justify this choice as capturing both the pathology and its structural context. **Constraint: Focus strictly on the clinical/data definition here. Do not discuss how these channels propagate through the network (reserve for 4.3).**

### 3.3 Spatial standardization
Center-crop/pad to the canonical (49, 1024) grid corresponding to the 6x6 mm macula-centered window. **Constraint: Explicitly state that we crop/pad instead of resampling to keep the en-face pixel spacing strictly invariant at [0.12118, 0.00568] mm across all patients. Justify the 6x6 mm window by citing that 99% of GA pathology occurs within a central 3mm radius from the macula, making the periphery clinically irrelevant for this scope.**

### 3.4 Normalization
Per-channel z-score normalization from training-split statistics. Table with the computed mean/std per channel.

### 3.5 Patient-level covariates
Age and sex extraction from the patient index. Training-split z-score for age, binary encoding for sex, mean imputation for missing values.

### 3.6 Temporal structure
Visits ordered per eye, $\Delta t$ computed between consecutive visits in years. Consecutive (state_i, state_{i+1}, $\Delta t$) triples form the training windows.

### 3.7 Train/validation/test splits
Patient-level splitting (not eye-level) to prevent leakage across an individual's two eyes. Split indices provided with the dataset.

## 4. Method (~15-20 pages)

### 4.1 Overview
One figure showing the full pipeline: input state -> uniform-mesh GNN branch + DMM-moved-mesh GNN branch with interpolation -> combined prediction. Reference every component to its detailed subsection.

### 4.2 $\Delta t$-conditioned residual formulation
Core adaptation from SWE-style fixed-dt to clinical variable-dt. The model learns `u_{t+\Delta t} = u_t + \Delta t * f_\theta(u_t, \Delta t)`. Explain why this replaces absolute time and preserves consistency in the MP-PDE sense.

### 4.3 Multi-channel pipeline
Walk through how C=11 channels propagate through each component: dataset layout `(N, C*K)`, GNN features, DMM with Frobenius-norm monitor function for vector-valued state, per-channel interpolation in ItpNet, multi-channel res_cut Conv2d. **Constraint: Assume the clinical meaning of the 11 channels was already established in 3.2; focus entirely on the mathematical/tensor propagation here.**

<!-- NOTE (2026-07-26, see NOTES.md "Code-side sync"): "Frobenius-norm monitor for vector-valued state" and "multi-channel res_cut Conv2d" are STALE — the DMM now trains on a single-channel SLO mask (scalar monitor) and res_cut was removed. §4.6 dual-branch should also cover the learnable α-gate. -->

### 4.4 Data-free mesh mover (DMM) for GA
How DMM is trained on GA states: the physics loss (Monge-Ampère + boundary + convexity), sampling strategy, monitor function choice. Note that DMM is pretrained separately and frozen during MM-PDE training.

### 4.5 Single-branch MP-PDE architecture
Describe the baseline adaptation: treating the pipeline as a single-branch uniform-mesh GNN. Explicitly note that while the original MP-PDE used temporal bundling, this adaptation removes it entirely due to the short, irregular sequences inherent to clinical data.

### 4.6 Dual-branch MM-PDE architecture
Main GNN branch on the uniform mesh producing the full next state; correction GNN branch on the moved mesh producing a pure $\Delta t$-delta; interpolation back via ItpNet; summation. Explain why the correction-branch formulation is the natural $\Delta t$-conditioned analogue of the original dual-branch sum.

### 4.7 Patient covariate conditioning
Age and sex as graph-level attributes broadcast per-node into the GNN's `variables` vector, entering both the embedding MLP and every message-passing layer.

### 4.8 Surrogate equation encoder
The learnable layer encoder: CNN compressing `(10, 49, 1024)` -> `R^{d_embed}`, concatenated to `variables` the same way as covariates. Framed as a learned stand-in for the PDE coefficients $\theta_{PDE}$ used in MP-PDE.

### 4.9 Training
Pushforward trick with depth-aware sampling, ItpNet pretraining at epoch 0, loss weighting across channels (mask gets higher weight), optimizer setup, learning rate schedule.

### 4.10 Implementation details
Hardware, framework versions, notable engineering choices (GPU-native k-NN replacing sklearn, graph precomputation, mixed-precision or not, etc.).

## 5. Experiments (~15-20 pages)

### 5.1 Evaluation protocol
**Crucial Context:** Explicitly explain why per-pixel MSE is a deceptive metric for slow-moving GA pathology before introducing the other metrics.
Metrics: per-timestep MSE and RMSE in normalized space, Dice and IoU on the GA mask channel at a clinically meaningful horizon (360 days). Persistence baseline (repeat last observed state) as the floor that any learned model must beat.

### 5.2 Baselines
- Persistence (last-state repetition)
- Single-branch GNN (MP-PDE style, no moving mesh)
- Multi-branch GNN, larger parameter budget (to isolate the moving-mesh contribution from capacity)
- Optional: simple CNN baseline (U-Net or similar) to contextualize against standard medical imaging approaches

### 5.3 Main results
Table comparing all methods on MSE, RMSE, Dice@360d, IoU@360d. A figure with example rollouts: ground-truth sequence vs each baseline's predictions over several visits for a representative eye.

### 5.4 Ablations
Each component on/off:
- DMM moving mesh vs uniform mesh
- Correction branch vs full second branch
- ItpNet pretraining vs no pretraining
- Pushforward training vs no pushforward
- Covariates (age, sex) vs no covariates
- Layer encoder (d_embed \in {0, 32, 64, 128, 256})
- Mask channel loss weight sweep

### 5.5 Moving mesh quality
Std/range of cell volumes under the monitor function (following the MM-PDE paper's metric) to verify the DMM generates physically sensible meshes on GA data. Visualize example moved meshes overlaid on sample states.

### 5.6 Qualitative analysis
Per-eye rollout visualizations. Success cases (accurate lesion growth prediction). Failure modes (e.g., what happens with atypical progression patterns, very sparse visit schedules, very short vs long $\Delta t$).

### 5.7 Computational cost
Training time, inference time per rollout step, memory footprint, comparison with baselines.

## 6. Discussion (~5-8 pages)

### 6.1 Interpretation of results
*Broaden back out from the technical results.* Which components contributed most? Did the moving mesh help on slowly-evolving pathology, or was uniform-mesh enough? Did the surrogate encoder improve generalization across patients?

### 6.2 Clinical implications
What prediction horizon is reliable? What RMSE/Dice level would be clinically useful? Where does the model fail, and would those failures matter in practice?

### 6.3 Limitations
Data quantity (sample size, missing visits), normalization of binary mask channel, monitor function chosen by heuristic rather than derived for vector-valued states, fixed grid assumption discards peripheral retina, encoder sees predicted (not observed) layers during pushforward unrolling.

### 6.4 Future work
Incorporating surrogate models of the next state into DMM's monitor function (the future-state problem from MM-PDE's conclusion), extending to 3D volumetric OCT, multi-task joint training across multiple retinal pathologies, uncertainty quantification for clinical deployment.

## 7. Conclusion (~2-3 pages)
Restate contributions, summarize empirical findings, articulate the take-away: neural PDE solvers are a viable framework for longitudinal medical imaging prediction, with specific adaptations needed for the clinical setting ($\Delta t$, multi-channel state, patient covariates).

## Bibliography
BibTeX file. Expect 40-80 references: clinical GA literature, OCT imaging, PDE numerical methods, neural PDE solvers (MM-PDE, MP-PDE, FNO, DeepONet), GNN foundations, retinal deep learning.

## Appendices

- **A. Dataset details** — Full demographic tables, visit-interval histograms, per-channel statistics.
- **B. Extended derivations** — Monge-Ampère equation, monitor function for multi-channel case, pushforward stability argument.
- **C. Full hyperparameters** — Everything not in the main text: all architecture widths, all training schedules, random seeds.
- **D. Additional rollout figures** — Extra qualitative examples, including failure cases.
- **E. Ablation details** — Full tables for every ablation sweep, not just the headline numbers.
- **F. Code structure** — Brief map of the repository, pointer to GitHub, reproducibility instructions.