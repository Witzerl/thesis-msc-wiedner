# PROJECT_CONTEXT.md

> **⚠️ MIRROR FILE — maintained in the code repository.** This document
> is a mirror of `masterthesis-docker/PROJECT_CONTEXT.md`, kept here so the
> thesis-writing session can read the current architecture. The **code
> repo is the source of truth**: architectural decisions are edited there
> and copied here to stay byte-identical (this banner excepted). **Do not
> edit this file directly in the thesis repo** — edits made here do not
> flow back and will be overwritten on the next mirror. Cross-references to
> `ARCHITECTURE.md` point at files that live only in the code repo.
> Last mirrored: 2026-07-26.

## 1. Dataset & Clinical Alignment

- **Source:** Medical University of Vienna (MUW) Geographic Atrophy (GA) dataset.
- **Coordinate Systems:** Global (SLO/FAF images) and OCT (rectangle on SLO). Affine transforms map between them.
- **Grid & Spacing:**
  - Standard OCT volume: `49 x 1024 x 496` (6x6 mm macular region).
  - En-face projection shape used for modeling: `49 x 1024`. **Note:** Unlike standard PDE toy datasets (e.g., SWE) which use quadratic/square domains, this framework operates on a highly asymmetrical rectangular domain.
  - Gold standard spacing: `[0.12118, 0.003867, 0.00568]` (in mm).
- **State Representation (11 Channels):**
  - Channel 0: Binary GA Mask (disease segmentation).
  - Channels 1-10: Retinal layer boundaries. Retina thickness is calculated via `layers[...,-1] - layers[...,0]`.
- **Patient Covariates:** Age (continuous) and Sex (categorical) are broadcast per-node and concatenated to the GNN's `variables` vector.

## 2. DMM training on the SLO mask, applied at OCT resolution

The DMM is **trained on the high-resolution Scanning-Laser-Ophthalmoscopy
(SLO) mask cropped to the OCT field-of-view**, not on the OCT volume
directly. This decouples training-time grid (square, isotropic) from
inference-time grid (rectangular, the OCT lateral sampling) and removes
all asymmetry-driven workarounds the OCT-direct path required.

**Two grids, one continuous mesh.** The DMM has two heads:

| Head | What it sees | At training | At MM-PDE inference |
|---|---|---|---|
| Branch CNN | the field $u(x)$ | $(1,\,1,\,256,\,256)$ SLO mask | same — `window["slo_mask"]` |
| Trunk MLP | continuous query $(\xi_1,\xi_2)\in[0,1]^2$ | random samples | OCT lateral grid, $(49,1024)$ flattened to $[0,1]^2$ |

The trunk is grid-agnostic; querying it on $(49,1024)$ at inference is
the same continuous function $\phi(\xi_1,\xi_2)$ that was sampled at
random coordinates during training. The branch is shape-locked to its
training-time input — hence the requirement that the SLO mask field
travels with each window through the MM-PDE pipeline.

**SLO mask construction.** Per visit, the SLO mask is built two-stage in
`tools/precompute_graphs_ga.py:load_slo_mask_oct_fov`:

1. **Crop** `mask_global.png` $(1536\times 1536)$ to the OCT FOV box
   $(1023\times 1024)$ using `transform_oct_fov` from
   `slo.transform.json`. Lossless: only discards SLO pixels outside the
   imaged $6\times 6$ mm rectangle.
2. **Downsample** to $(N\times N)$ via PIL nearest-neighbour resize.
   $N=256$ is the default (4× downsample of the cropped mask). The
   downsample is lossy for sub-4-px boundary detail but keeps lesion
   shape intact.

The resulting mask lives in $[0,1]$ (binary 0/1 float32), is single-
channel by construction, and is stored as a per-window field
`w["slo_mask"]` alongside the existing OCT-side state. The MM-PDE
backbone still consumes the full $(11,49,1024)$ OCT tensor; only the
DMM's branch sees the SLO mask.

**Monitor function on a single channel.** The monitor reduces to the
plain scalar formula
$$M = 1 + \frac{\|\nabla u\|}{\alpha_{\text{scale}}\,\alpha + \epsilon},$$
where $u$ is the (Gaussian-blurred) SLO mask. Multi-channel Frobenius
norm and log-compression workarounds are not used. The blur is still
applied — the binary 0/1 mask has step-function gradients regardless of
grid shape, and a small $\sigma\!\sim\!2$ px keeps the monitor finite.

**Why this design.** The OCT direct-training path required several
asymmetry-specific workarounds (axis-asymmetric soft-NN interpolation,
log-compressed monitor to balance the 21:1 y/x gradient mismatch,
replicate-pad to keep blur kernels from bleeding zeros across the 49-px
short axis, mask-only Frobenius restriction to suppress the 89%-mass
contribution of quasi-static layer channels). All of these dissolve
when the DMM trains on a square 256² mask. The trade-off is the
4× downsample's loss of sub-pixel boundary precision — empirically
acceptable; the resulting mesh follows the lesion edge cleanly on all
representative eyes inspected.

## 3. Variable Time-Step ($\Delta t$) Conditioning

Unlike original uniform-grid PDEs, clinical visits have irregular intervals and no shared $t=0$.

- **Residual Formulation:** The solver acts as a proper $\Delta t$-conditioned Euler residual operator: $u_{t+\Delta t} = u_t + \Delta t \cdot f_\theta(u_t, \Delta t)$.
- **Persistence as an Inductive Prior:** The leading $u_t$ term is not just the Euler base needed to make the residual form well-posed — it is a deliberate inductive prior, justified on two independent grounds. *(i) Numerical / Euler-base:* framing the network as a residual operator that predicts only the increment $\Delta t \cdot f_\theta$ on top of the known state $u_t$ is far better-conditioned than regressing the absolute next state $u_{t+\Delta t}$ from scratch — consecutive visits are almost identical, so the base term carries most of the signal and the network is freed to model only the change. *(ii) Clinical:* geographic atrophy evolves **slowly** — the lesion barely changes between visits, so persistence ($u_{t+\Delta t} \approx u_t$) is already a strong baseline — and **monotonically** — atrophic retinal tissue never regenerates, so GA is strictly growing and never shrinks. The model therefore only has to learn a small, growth-only correction on top of the persistence base rather than the entire field. The same monotonic-growth prior is additionally enforced at training time by the soft monotonic-mask penalty (see [ARCHITECTURE.md §7](ARCHITECTURE.md)).
- **Time Encoding Flag:** `delta_adapted` mode uses per-window $\Delta t$ (in years) attached to `data.dt`. The GNN reads `dt_per_node` as the integration step.
- **Dual-Branch Composition** (revised 2026-07-19 — see the divergence note below):
  - Main branch (uniform mesh) returns full next-state: $u + \Delta t \cdot f_\theta$.
  - Correction branch (moving mesh) returns pure delta: $\Delta t \cdot g_\theta$.
  - The interpolated moved-branch correction is scaled by a **learnable scalar gate** $\alpha$ (initialised to 0), so the moved branch starts inert and has to earn its contribution. $\alpha$ also pins the moved term's scale, which the loss alone does not: the loss constrains only the *sum* of the branches, so without $\alpha$ the branches are free to grow large and mutually cancelling.
  - Summation evaluates to: $pred = u + \Delta t \cdot f_\theta + \alpha \cdot \tilde{I}\big[\Delta t \cdot g_\theta\big]$.
  - $\tilde{I}$ denotes ItpNet interpolation whose weights are **renormalised to a partition of unity** (row-sums = 1), so interpolation is a true constant-preserving weighted average and its gain is bounded.
  - At $\Delta t \to 0$ the prediction collapses to persistence $u$, which is the right limit for clinical visits with very short gaps.
  - **Removed: the residual-cut term $\mathrm{res\_cut}(u)$.** A per-timestep CNN ItpNet head compensating for moved↔uniform interpolation error, it was previously added into the *velocity* as $+\,\Delta t \cdot \mathrm{res\_cut}(u)$. Because its input is the state $u$ and the ItpNet round-trip pre-training taught it $\mathrm{res\_cut}(u) \approx u - \tilde{I}[u_{\text{moved}}]$ (the full-state round-trip error, $\approx 0.8\,u$), it is a state-aligned velocity that compounds over an autoregressive rollout, and nothing in the loss penalises its magnitude. Empirically it drove the dual-branch model to diverge (rollout RMSE $3.3\times10^5 \to 1.2\times10^{12}$ across epochs 2–4). It was first made default-off, then cut from the framework entirely — the ItpNet head, the composition term, the epoch-0 pre-training of it, and the CLI switches are all gone.
  - $\alpha$'s trajectory over training is a **reportable measurement**: $\alpha \to 0$ means mesh adaptation does not transfer to slow-progressing GA (the pre-registered negative result), $\alpha$ growing means it does.

## 4. Surrogate Equation Encoder (LayerEncoder)

To provide the GNN with a "surrogate equation identity" (a stand-in for PDE coefficients $\theta_{PDE}$), a lightweight `LayerEncoder` CNN compresses the 10 retinal layer boundaries into a compact global embedding vector $z \in \mathbb{R}^{d_{embed}}$.

- **Rectangular Handling:** Due to the extreme `49 x 1024` asymmetry, the encoder downsamples along the long axis first and uses `AdaptiveAvgPool2d(1)` to remain spatial-size agnostic.
- **Integration:** This global per-graph embedding is broadcast per-node and concatenated to the `variables` input of the GNN alongside $\Delta t$ and patient covariates, telling the dynamics model what kind of retinal structure it is operating on without requiring the GNN to parse raw layer geometry through message passing.

## 5. MP-PDE & MM-PDE Conceptual Modifications

- **Temporal Bundling Removed ($K=1$):** Temporal bundling (used in the original MP-PDE) is redundant due to the short sequences inherent to clinical data. More critically, MM-PDE does not natively support multi-timestep windows because the DMM computes the moved mesh from a single spatial snapshot. If $K>1$ were used, the mesh generated at $t=0$ would become "stale" for later timesteps in the window. The framework therefore defaults to strict $K=1$ autoregressive prediction to ensure the mesh faithfully reflects the current state.
- **Training Separation:** ItpNet is pre-trained separately with its own optimizer to prevent polluting the main scheduler before actual data training.
- **Loss Weighting:** The MSE loss is weighted to emphasize the clinical deliverable, prioritizing the mask channel over the auxiliary layer channels.
- **Intermediate-Time-Point Regularization (evaluated and removed 2026-06-11):** Clinical visits give only sparse observations of a continuous trajectory, so a $\Delta t$-conditioned operator easily overfits the endpoints while behaving arbitrarily in between. To address this, a regulariser was implemented (2026-05-21, supervisor's recipe) that queried the model at $K$ sub-times $\tau_k = \alpha_k\,\Delta t$ with $\alpha_k\sim U(0.1,0.9)$ per graph and penalised the prediction against the linear interpolant $(1-\alpha_k)\,u_t + \alpha_k\,u_{t+\Delta t}$ under the same data criterion. Ablations (REG-weight sweep λ ∈ {1, 3, 10} plus reg-on/off legs of the 2026-05-25 queues) showed no benefit on the change-region Dice metric — the reg=0 configurations matched or beat the regularised ones — so the feature was removed from the codebase on 2026-06-11. Historical regularised runs remain reproducible from their recorded git SHAs; the negative result is reportable in the thesis Discussion.

## 6. Evaluation Metrics & Baselines

- **Primary Clinical Metrics:** Dice and IoU on the denormalized, thresholded Mask (Channel 0) at 360 days. Focus on the *change region* (new GA minus baseline GA).
- **Secondary Metrics:** Rollout MSE/RMSE (Note: Per-pixel MSE is flawed for slow-moving GA due to the persistence baseline).
- **Baselines:** Persistence (predict no change), Single-branch GNN, Multi-branch GNN (larger parameter budget).

## 7. Known Issues & Future Work

- **Monitor Function Masking (Resolved 2026-05-03):** The binary GA mask produces step-function gradients ($\sim 1000\times$ larger than the smooth retinal-layer channels), which drove the Frobenius-norm monitor to $\sim 1800$ and made the second-derivative chain through $\phi$ accumulate to NaN within a few training iterations. A Gaussian blur ($\sigma \approx 2$ px) is now applied to Channel 0 strictly for monitor function computation; the GNN itself still sees the unblurred mask. The blur is configurable via `--monitor_mask_sigma` (default 0 disables it for SWE byte-identity) so the unblurred case remains available as an ablation. Empirically reduces the monitor's maximum value by $\sim 5\times$.
- **Multi-Timestep DMM Integration (Future Work):** To overcome the $K=1$ limitation, future research could explore temporally aggregating the monitor function snapshot (e.g., mean or max gradient across the window) to compute a single compromise mesh. Alternatively, a hybrid architecture could be explored where the uniform branch processes all $K$ timesteps simultaneously while the moved branch runs $K$ internal autoregressive steps.