# Prompt: Appendix G — the moving-mesh extension (MM-PDE)

*(Self-contained. Copy everything below the line into the other model.)*

---

## 1. Your role and the task

You are drafting one appendix of a Master's thesis in machine learning (Johannes Kepler
University Linz, with the Medical University of Vienna). The main chapters are written and
audited. Your job is to write the missing parts of **Appendix G, "The Moving-Mesh Extension
(MM-PDE)"**, **in LaTeX, ready to paste** into `91-appendix.tex`:

| # | Part | Label (already exists, keep it) | Budget |
|---|---|---|---|
| A | §G.2 intro "The Moving-Mesh Extension for GA" | `app:mm-pde:extension` | ~0.5 page |
| B | §G.2.1 "Data-Free Mesh Mover for GA" | `app:mm-pde:dmm` | ~1.5 pages |
| C | §G.2.2 "Dual-Branch Composition" | `app:mm-pde:dual` | ~1.5 pages |
| D | §G.3 "Moving Mesh Quality" | `app:mm-pde:mesh-quality` | ~1 page + 1 table + 1 figure placeholder |
| E | §G.4 "Result" (new section) | `app:mm-pde:result` (new) | ~1.5 pages + 1 table |

§G.1 "Background: MM-PDE" (`app:mm-pde:background`) and §G.5 "Outlook"
(`app:mm-pde:outlook`) already exist. **Do not rewrite them**; do not repeat what §G.1
already explains (the monitor idea, equidistribution, Monge–Ampère, Brenier, the residual
potential, DeepONet, the dual branch and ItpNet *in the original paper*). §G.2 onwards
describes **what this thesis did differently and what it measured**.

Write the full text to the budget, not a skeleton. Every number must come from the fact
sheet in §4. If you need a number that is not there, **do not invent it**: write a
`% TODO:` comment saying exactly what is missing and continue.

After the LaTeX, give a short **report** (plain text): (1) every sentence where you were
unsure whether a claim is supported, (2) every `% TODO` you left, (3) any place where the
fact sheet seemed contradictory.

---

## 2. Context you need

**Topic.** Geographic Atrophy (GA) is the advanced atrophic form of age-related macular
degeneration: a lesion of dead retinal tissue that grows slowly over years. The thesis
forecasts how the GA lesion of an individual eye changes, from longitudinal OCT.

**The thesis in short.** A fixed framework advances an 11-channel state (channel 0 = binary
GA mask, channels 1–10 = depths of ten retinal layer boundaries) on a 49 × 1024 en-face grid
by one residual step per visit interval, $u_{t+\Delta t} = u_t + \Delta t \cdot
f_\theta(u_t, \Delta t, z)$, with a zero-initialised output head (every operator starts at
exact persistence), a pushforward curriculum measured in elapsed days, a mask-weighted MSE +
soft-Dice loss, 5-fold cross-validation over 75 eyes. Only the operator $f_\theta$ varies.
The main chapters compare operators on a **uniform grid**: graph networks (MP-PDE style) on
an index-space k-NN graph and on a dilated stencil (the canonical model), U-Net, FNO, FEN.
The pixel spacing is ~21:1 anisotropic (0.12118 mm between rows, 0.00568 mm between
columns).

**Why this appendix exists.** The work began as an adaptation of MP-PDE (Brandstetter et
al. 2022) and MM-PDE (Hu et al. 2024). MM-PDE adds a moving mesh: a pretrained, frozen
Data-free Mesh Mover (DMM) moves the grid nodes towards where the state changes sharply,
and a second graph network on the moved mesh adds a correction to the uniform branch. In
this thesis the moving mesh was **built in full, tested, and found to contribute nothing
measurable**. The author decided to report it as an additional experiment in this appendix,
not in the main text. The negative result must be reported **honestly and with its exact
scope** (§3.3).

---

## 3. Rules (binding — the author audits every line against these)

### 3.1 Voice and style
- **Passive voice, no "we", "I", "our".** "The DMM was trained …", "This thesis …".
- **Plain, short sentences.** One idea per sentence; paragraphs of 3–7 sentences. Prose,
  not bullet lists.
- **No filler or hype words**: never *strictly, crucially, critical(ly), pivotal, massive,
  rigorous, notably, remarkably, firmly, purely, entirely, fundamentally, inherently,
  robust (as praise), novel, leverage, delve, underscore, showcase, landscape*.
- British spelling: *normalisation, discretisation, parameterisation, behaviour,
  modelling*.
- Every metric needs a plain description of what it measures the first time it appears.
- Frame the result honestly: say what did not work; neither oversell nor apologise.

### 3.2 LaTeX
- natbib only: `\citet{key}` (textual), `\citep{key}` (parenthetical). **Keys you may
  use:** `Hu2024` (MM-PDE), `Brandstetter2022` (MP-PDE), `HuangRussell2011` (*Adaptive
  Moving Mesh Methods*, Springer 2011 — equidistribution, mesh quality), `Lu2021`
  (DeepONet), `Loshchilov2019` (AdamW), `Chen2018` (Neural ODEs). For the ReZero gate
  (Bachlechner, Majumder, Mao, Cottrell & McAuley, "ReZero is All You Need: Fast
  Convergence at Large Depth", UAI 2021) write the author-year in plain text and put
  immediately above the sentence: `% TODO: cite Bachlechner2021 (ReZero, UAI 2021) once
  added to references.bib`.
- Cross-references with `\S\ref{…}`, `Table~\ref{…}`, `Figure~\ref{…}`,
  `Appendix~\ref{…}`, non-breaking `~`. **Only these labels exist** (plus the ones you
  create in §5):
  `app:mm-pde app:mm-pde:background app:mm-pde:extension app:mm-pde:dmm app:mm-pde:dual
  app:mm-pde:mesh-quality app:mm-pde:outlook app:ablations app:code` ·
  `sec:data:spatial sec:data:normalization sec:method:framework sec:method:dt-residual
  sec:method:multichannel sec:method:family:contract sec:method:mppde sec:method:graph
  sec:method:family:rk sec:method:family:params sec:method:training
  sec:method:training:loss sec:method:training:curriculum sec:method:training:optim
  sec:experiments:protocol:stats sec:experiments:main-results
  sec:experiments:ingredients:reach sec:experiments:ablations sec:experiments:cost` ·
  `tab:experiments:arms`.
- New labels you create: `app:mm-pde:result`, `tab:appendix:dmm-config`,
  `tab:appendix:mesh-quality`, `fig:appendix:moved-mesh`, `tab:appendix:dual-result`.
- `\%` in running text (`10\,\%`), thin space before units (`0.12\,mm`), thousands with a
  thin space (`175\,663`), `$\times$` for factors (`$10\times$`), math for $\alpha$,
  $\Delta t$, $\phi$, $\pm$.
- Tables: `booktabs`, `\small`, caption before label, self-contained captions, rows end
  with `\\`. No `\tablefootnote`.
- **Figure:** exactly one placeholder in §G.3, in this form (adapt the caption):
  ```latex
  \begin{figure}[t]
    \centering
    \fbox{\parbox[c][5cm][c]{0.9\textwidth}{\centering Placeholder for
      Figure~\ref{fig:appendix:moved-mesh}. See accompanying \texttt{\% TODO}.}}
    \caption[...]{...}
    \label{fig:appendix:moved-mesh}
  \end{figure}
  ```
  with a `% TODO: produce Figure fig:appendix:moved-mesh -- …` comment above it that says
  what the figure should show.

### 3.3 Hard content rules (violating any of these means the text is rejected)
1. **No invented numbers.** Only fact-sheet numbers, rounded no further than the fact sheet.
2. **Scope the negative result exactly.** The measured statement is: *the gated correction
   branch did not engage — with the moving mesh or with the uniform grid in its place,
   with or without weight decay — and the dual branch gave no measurable gain.* **Never**
   write that "mesh adaptation does not work for GA", "does not transfer to GA", "is
   unsuitable for slow processes" or similar. The bypass control (same machinery, mesh
   replaced by the uniform grid) behaves identically, so the result says nothing about
   mesh adaptation as such.
3. **No mechanism beyond the fact sheet.** The correction branch's gradient is proportional
   to $\alpha$ (measured by a probe); that is the self-reinforcing dead-gate reading. **Do
   not** say the gradient "underflows" or "vanishes numerically" — that earlier reading was
   retracted. Do not claim to know why $\alpha$ stays shut beyond "the gradient of the
   correction branch is proportional to $\alpha$, so a gate that starts at zero gives the
   branch almost no learning signal, and an untrained branch gives the gate no reason to
   open".
4. **The monitor is a scalar monitor on the Gaussian-blurred binary mask, on the native
   49 × 1024 grid.** Do not describe a multi-channel or Frobenius-norm monitor, and do not
   describe the DMM as trained on a 256² SLO grid, except in at most one sentence that says
   an earlier version trained on a square 256² grid and was replaced. Never mention a
   "res_cut" term.
5. **The mesh-quality numbers are in-sample** (the DMM is trained on all 478 masks of the
   cohort, which is allowed because it never sees a future state). Say so; claim nothing
   about generalisation.
6. **Name the era.** The 5-fold dual, bypass and single-branch runs used the **v1 k-NN graph
   network with mean+max neighbour aggregation** (single-branch 0.4515), *not* the
   canonical dilated stencil and *not* the mean-aggregation k-NN arm of
   Table~\ref{tab:experiments:arms} (0.4623). Only one dual run (fold 2) used the stencil.
7. No "ODE", "rate field" or "learned dynamics" language. No "test set" (5-fold
   cross-validation, validation folds only).
8. Report cost as order of magnitude only (~10×), as the minimum epoch time over the folds.

---

## 4. Fact sheet (the only allowed source of numbers)

### 4.1 The DMM for GA (what differs from Hu et al.)
- Input: **channel 0 only** — the binary GA mask on the **native (49, 1024)** OCT grid.
  At the first step this is the observed segmentation; during a rollout it is the model's
  own predicted mask (denormalised and thresholded back to binary), so the deployed input
  is used automatically. The network branches on the uniform and on the moved mesh still
  process **all eleven channels**; only the mesh mover reads the mask alone.
- Architecture: DeepONet-style (Lu et al. 2021) as adapted by Hu et al.: a CNN **branch**
  (`pool`: three stride-2 convolutions 1→16→32→64, adaptive average pooling to 4×4, linear
  to a 512-d latent; it works at any input size) encodes the mask; an MLP **trunk** on the
  continuous coordinate $\xi \in [0,1]^2$ (widths [2, 32, 512], tanh); a **head** maps the
  concatenation of both to the scalar potential $\phi$, with widths [1024, 512, 512, 1] (one
  layer deeper than the base [1024, 512, 1]). The moved mesh is $x(\xi) = \xi + \nabla\phi(\xi)$,
  by automatic differentiation. **1\,394\,273 parameters**, all frozen during solver training
  and excluded from the optimiser.
- **Monitor** (scalar): $M = 1 + \log(1 + \lVert \nabla u \rVert / (\alpha_{\text{scale}}\,\bar g + \epsilon))$,
  where $u$ is the mask after a Gaussian blur, $\bar g$ the field mean of the gradient
  magnitude, $\alpha_{\text{scale}} = 0.1$, $\epsilon = 10^{-10}$. The gradient is taken in
  the unit-square computational coordinate, which gives the two axes their correct relative
  weight on the anisotropic grid.
  - **Blur** (σ = 1.0 px, monitor only — the branch CNN always sees the raw binary mask):
    a binary mask has a step at the lesion edge; without the blur the first GA run diverged
    to NaN (monitor peak ~1800). Without blur on the native grid the mesh barely moves:
    boundary concentration (`edge_gain`, §4.3) 1.24 against 1.62 at σ = 2 on an otherwise
    identical configuration (head-16 pool; on the spread pool the no-blur value is 1.34).
  - **log compression** (the `log(1 + ·)`): bounds the peak-to-bulk ratio of the monitor at
    the sharp lesion ring, so the equidistribution target stays reachable. Without it the
    mesh scores below an unadapted mesh (`edge_gain` 0.94 vs 2.24 on the spread pool).
  - A physically matched anisotropic blur kernel (≈21.8× wider along the columns) was tried
    and gave no gain (p = 0.95) while folding the mesh intermittently; a
    Jacobian-determinant barrier made tangling worse. Both are kept out of the design.
- **Loss** (weights 1 / 1000 / 1): (i) Monge–Ampère equidistribution residual at sampled
  interior points, $\text{MSE}\big(M(\xi + \nabla\phi)\,\det(I + \nabla^2\phi) / \bar M,\ 1\big)$ —
  monitor at the moved point times the cell-volume change should be constant; (ii) a soft
  boundary term penalising the normal derivative of $\phi$ on the four edges, so boundary
  nodes stay on the boundary; (iii) a convexity term penalising negative diagonal entries of
  the Hessian (a fold-over precursor). The convexity term is measured to be ≈0 throughout
  training; validity is enforced at checkpoint selection (zero folded cells, §4.3).
- **Sampling:** per iteration 5 masks and 1000 points per mask, drawn 90 % in proportion to
  the monitor (importance sampling) and 10 % uniformly.
- **Training:** on **all 478 masks** of the cohort (every window's start mask, all 75 eyes,
  ≈6.4 per eye) — the DMM never sees a future state, so this leaks no label, and it makes
  the same mesh mover in-distribution for every fold. Adam, learning rate 2e-4, weight decay
  1e-5, 500 epochs, learning rate × 0.2 at epochs 333 and 467. Selected from a **55-run
  hyperparameter search** on the native grid; three seeds of the winner. Epochs improved
  quality up to 500 and converged there. The two largest levers were one extra head layer
  (+0.18 `edge_gain`) and the sharper blur σ = 1 instead of 2 (+0.19), which only help
  together (σ = 1 is worth +0.003 with the shallow head). The branch architecture was a
  null across five variants (spread 0.047 over a 25× range of branch parameters); the
  `pool` branch is kept because it works at any grid size, not for a measured edge.
- **History (at most one sentence):** an earlier version trained on a square 256² mask
  sampled from the fundus image; it was replaced by the native grid, which removes a resize
  round-trip during rollout.

### 4.2 The dual-branch composition (as implemented)
- $\text{pred} = u + \Delta t\, f_\theta(\text{uniform}) + \alpha \cdot \tilde I\big[\Delta t\, g_\theta(\text{moved})\big]$.
  The uniform branch returns the full next state; the correction branch on the moved mesh
  returns a pure $\Delta t$-scaled increment; $\tilde I$ carries it back to the uniform grid.
- Both branches are the graph network of the main text (\S\ref{sec:method:mppde}), two
  message-passing rounds, width 64.
- **Gate $\alpha$**: a learnable scalar, initialised to **0** (the ReZero construction,
  Bachlechner et al. 2021), so the dual model starts exactly as the uniform branch alone and
  the correction has to earn its weight. It also fixes the scale of the correction: the loss
  only constrains the sum of the two branches, which could otherwise grow large and cancel.
  $\alpha$ has its own optimiser group with **no weight decay** and its own gradient-clipping
  group.
- **No zero-init on the correction branch's decoder** (unlike every operator of the main
  text, whose output head is zero-initialised): zero-initialising both the decoder and
  $\alpha$ makes the gradients of both exactly zero at the start, a deadlock from which the
  branch could never activate. The gate alone supplies the zero start.
- **Moved graph:** the moved nodes lie off the lattice, where the dilated stencil is not
  defined, so the correction branch builds its own k-NN graph (k = 12) on the moved
  positions, searched in index space (coordinates divided by the grid pitch). A search in
  physical millimetres would return only same-row neighbours on this grid (measured:
  100 % before the fix of 2026-08-06; every dual result before that date is void).
- **ItpNet:** a learned interpolation; for each query point an MLP (widths [26, 128, 64, 12],
  tanh, linear output) turns the coordinates of its 12 nearest source points into 12 weights.
  Two independent copies: uniform → moved (builds the correction branch's input, all eleven
  channels) and moved → uniform (returns the correction). The return weights are
  renormalised to sum to one per point, with a sign-preserving floor of 0.1 on the
  denominator, which bounds the gain at 10 (the floor engages on ~12.6 % of points).
- **ItpNet pretraining:** 25 passes at epoch 0 with its own AdamW optimiser, on the
  round-trip identity uniform → moved → uniform, scored by the channel-weighted MSE only
  (soft-Dice would push the operator away from the identity), with gradient clipping and
  the gate disabled.
- **Mesh recomputed at every step** from the current state; therefore the dual branch, like
  every operator here, predicts **one step at a time**: a mesh built at the start of a
  multi-step window would no longer match the lesion at the later steps. (In the main
  text, one-step prediction is motivated by the short visit sequences; this is the second,
  mesh-specific reason.)
- **Per-module gradient clipping** (norm 1.0) over five groups: uniform branch, correction
  branch, ItpNet weights, $\alpha$, and the layer encoder; the DMM is frozen. Under one
  joint clip, ItpNet's large gradients (median $10^3$–$10^4$ in the k-NN-era dual runs,
  against ~1 for the uniform branch) would have throttled the uniform branch.
- The Runge–Kutta wrapper of \S\ref{sec:method:family:rk} applies to single-branch models
  only. The dense operators and the FEN of the main text run as single-branch models, so
  they are compared with the single-branch graph network, not with the dual branch.
- **Parameters** (trainable): dual and bypass **175\,663** vs single **75\,339** in the v1
  k-NN configuration of the 5-fold runs (≈100 k extra = second network + ItpNet); with the
  stencil (v2) 159\,279 vs 67\,147. The frozen DMM (1.39 M) is not counted and is loaded by
  the bypass arm too.
- **Bypass control** (`--bypass_dmm_move`): loads the same DMM, runs the second network and
  the full ItpNet round-trip, but uses the **uniform grid** instead of the moved mesh.
  Parameter-identical to the dual model; the only difference is the mesh geometry.

### 4.3 Mesh quality (canonical DMM, three seeds, epoch 500; in-sample)
Metrics (all depend only on the mask, the same reference for every run):
- **tangled cells**: number of mesh cells with non-positive signed area (fold-overs). **0
  on every scored mask, every seed, every scored epoch.**
- **`edge_gain`**: mean of a fixed lesion-boundary band field (the lesion border widened to
  a band of half-width 0.02 of the domain and normalised to a grid mean of 1), sampled at
  the moved node positions. The identity mesh scores exactly 1; higher means more nodes on
  the lesion border.
- **`cov_ref`**: coefficient of variation (std/mean) of the cell areas weighted by one fixed
  reference monitor — the equidistribution measure of Huang & Russell (2011); lower is
  more even.
- **`det_min`**: minimum of $\det(I + \nabla^2\phi)$ over random points — the continuous
  invertibility margin (> 0 means no fold anywhere, not only at the grid nodes).

| pool (16 masks each) | `edge_gain` mean ± sd (3 seeds) | tangled | `cov_ref` | `det_min` |
|---|---|---|---|---|
| head-16 (first 16 masks; covers few eyes) | 1.9854 ± 0.0580 | 0 | 0.313 | 0.203 |
| spread-16 (spread over eyes) | 2.6307 ± 0.0607 | 0 | 0.311 | 0.115 |

The two pools are not comparable with each other (`edge_gain` and `det_min` depend on the
masks scored); the spread pool is the unbiased one. Reference points on the spread pool:
the base configuration before the head and blur changes 2.24; without blur 1.34; without
log compression 0.94 (below an unadapted mesh). The winner's seed spread (sd 0.058–0.061)
is the largest in the search. One recipe choice is unverified: the boundary weight 1000
was kept although a weight of 100 scored higher on raw `edge_gain` (+0.029 head-16, +0.105
spread-16); it was rejected on a lesion-specificity check computed on the biased pool only.

**What this licenses:** the mesh mover produces valid, non-folded meshes that concentrate
nodes on the lesion border. So the null result of §G.4 cannot be explained by a broken
mesh.

### 4.4 The result (change-region Dice at the one-year anchor; same protocol as the main text)
5-fold, seed 42, all three arms on the **v1 k-NN graph network with mean+max
aggregation**; late-epoch mean (epochs 10–29) per fold; paired differences ± between-fold
SE; per-eye instrument = growth-region Dice at each eye's first step past 0.95 years,
75 eyes. Noise floor: a 5-fold paired mean must exceed **0.016**, a single fold **0.036**
(replicate sd 0.0127).

| arm | mean ± sd over folds | params (trainable) | min epoch time |
|---|---|---|---|
| single branch (uniform only) | 0.4515 ± 0.0429 | 75\,339 | 75 s |
| dual branch (moving mesh) | 0.4501 ± 0.0326 | 175\,663 | 759 s (fold 0) |
| bypass control (uniform grid, same machinery) | 0.4503 ± 0.0324 | 175\,663 | 718 s |

- **dual − bypass = −0.0001 ± 0.0060 SE** (3/5 folds higher), per eye **+0.0001 ± 0.0038**
  (33/75): the tightest null in the project; the SE is less than half the 0.016 threshold.
- **dual − single = −0.0013 ± 0.0086 SE** (3/5), per eye −0.0018 ± 0.0064 (32/75).
- **Cost:** about **10×** the single-branch wall-clock per epoch, for no gain.
- **The gate $\alpha$** (all five folds of both arms): starts at exactly ±0.0020 (one
  optimiser step of size learning rate × sign of the gradient from zero — the zero start
  works as designed), peaks at 0.058–0.093 (dual) and 0.031–0.101 (bypass), mean |α|
  0.009–0.024 (dual) and 0.005–0.023 (bypass), and ends ≈ 0 in every fold. The bypass range
  brackets the dual range; the largest peak in either arm belongs to a bypass fold (0.1005).
  **$\alpha$ never opens, with or without the moving mesh.**
- **Mechanism probe** (on the real dual stack): the gradient reaching the correction branch
  is proportional to $\alpha$ — 0 at $\alpha = 0$, 0.0034 at $\alpha = 0.002$, 1.799 at
  $\alpha = 1$, against a uniform-branch gradient norm of ~2.09. At the $|\alpha| \approx
  0.02$ the runs reach, the correction branch's learning signal is about **60× weaker**
  than the uniform branch's: a self-reinforcing dead gate.
- **Three single-fold probes (fold 2), none of which opens the branch:**
  - *No gate* (decoder zero-init instead of $\alpha$): change-region Dice **0.3148 vs 0.4878**
    for the gated dual, **−0.173** (about 5× the single-fold floor). The gate protects the
    prediction from an untrained correction added at full weight; the correction branch's
    gradient is still 0 at the median.
  - *No weight decay on the correction branch and ItpNet* (arm G): **+0.0092** against its
    twin, under the 0.036 single-fold floor; $\alpha$ peaked *lower* (0.058 vs 0.067); the
    correction branch's parameter norm *grew* (×1.114). Weight decay is not the cause.
  - *Dual on the dilated stencil* (the canonical uniform branch): **0.5754** vs its own
    single-branch twin 0.6060, **−0.031** (per eye −0.0305 ± 0.0086, 3/16 eyes, t = −3.53),
    at roughly 9× the wall-clock. The stencil's own gain carries over (+0.088 over the k-NN
    dual), but the correction branch does not engage however strong the uniform branch is.
- **Reading:** the gated correction branch did not engage — mesh or no mesh, decay or no
  decay, gate or no gate — and the dual branch gave no measurable gain at about ten times
  the cost. The result is a statement about this implementation, not about mesh adaptation
  for GA. It differs from Hu et al.'s own ablations (their dual branch beat the uniform
  baseline on their benchmarks); that difference is not explained here.
- **What was originally expected:** before the runs, $\alpha \to 0$ was pre-registered as a
  reportable outcome meaning "mesh adaptation does not help". The bypass control showed
  that this inference is not valid, because $\alpha$ stays shut without the mesh as well.
  (Say this plainly: the design included the control that overturned its own planned
  reading.)

---

## 5. What to write, section by section

### A. §G.2 intro (`app:mm-pde:extension`) — ~0.5 page
What was built (DMM + dual branch, on top of the framework of Chapter 4), why it is in the
appendix (built in full, measured, no gain), and that it was designed as a measurement: the
zero-initialised gate $\alpha$ and the parameter-matched bypass control are the instruments.
Point to §G.2.1, §G.2.2, §G.3, §G.4.

### B. §G.2.1 DMM for GA (`app:mm-pde:dmm`) — ~1.5 pages + Table `tab:appendix:dmm-config`
Input (mask only, native grid, observed vs predicted mask during rollout), architecture,
monitor (blur and log compression, each with its measured reason), loss (three terms;
convexity dormant; validity at selection), sampling, training on all 478 masks (why it is
allowed), the 55-run search and its two levers, the refuted ideas in one sentence, the
history in at most one sentence. A small table with the canonical configuration (input,
branch, trunk, head, monitor σ / α_scale / log, loss weights, sampling, optimiser and
schedule, parameter count).

### C. §G.2.2 Dual-branch composition (`app:mm-pde:dual`) — ~1.5 pages
The composition equation (labelled `eq:appendix:dual`), the gate and why it exists, why the
correction decoder is not zero-initialised, the moved k-NN graph and the 100 %-same-row
defect, ItpNet and its normalisation, the pretraining, the mesh recomputed at every step and
the resulting one-step rule, which channels each part uses, per-module clipping, parameter
counts, the bypass control, and that the RK wrapper and the grid operators are
single-branch only.

### D. §G.3 Mesh quality (`app:mm-pde:mesh-quality`) — ~1 page + Table `tab:appendix:mesh-quality` + figure placeholder
Define the four metrics plainly, give the table, state in-sample, state the two pools are
not comparable, the reference points (no blur, no log), the seed spread and the unverified
boundary weight. Close with what this licenses (the mesh is valid and adapts, so §G.4's null
is not a broken-mesh artefact). Figure placeholder `fig:appendix:moved-mesh`: the moved mesh
(every k-th grid line) over the GA mask of two or three representative eyes, at the
physical aspect ratio, with the uniform grid for comparison.

### E. §G.4 Result (new section, `\section{Result}` with `\label{app:mm-pde:result}`) — ~1.5 pages + Table `tab:appendix:dual-result`
The three-arm table (mean ± sd, params, min epoch time) with the era stated in the caption;
dual − bypass and dual − single with both instruments; the gate trajectories; the probe;
the three fold-2 probes; the reading with its exact scope; the pre-registered reading and
why the control overturned it; one sentence on the difference to Hu et al.'s own result
being unexplained. Do not repeat the Outlook (§G.5 exists).

---

## 6. Output format

1. One LaTeX block per part (A–E), each starting with its `\section` / `\subsection` line
   and label exactly as listed, ready to paste in order between §G.1 and §G.5.
2. Then the plain-text report (§1).
