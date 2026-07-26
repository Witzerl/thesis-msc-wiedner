# NOTES

Single source of truth for open TODOs, supervisor feedback, pending numbers, and unresolved citations. Mirror every `% TODO:` left in the LaTeX as an entry here.

## Code-side architecture & results sync (2026-07-26)

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
- [ ] TODO: 2.3 Neural PDE solvers (neural operators vs autoregressive).
- [ ] TODO: 2.4 MP-PDE summary.
- [ ] TODO: 2.5 MM-PDE summary.
- [ ] TODO: 2.6 Related work.
- [ ] TODO: produce Figure `fig:bg:eye-anatomy` placed in `02-background.tex` §2.1.1 -- two-panel anatomy reference for ML readers without clinical background: (left) sagittal cross-section of the human eye labelling cornea, lens, vitreous body, retina, fovea, optic-nerve head (ONH) / optic disc, optic nerve, choroid, sclera, with the macular region highlighted on the retina near the posterior pole; (right) en-face fundus view of the posterior pole labelling macula (~6 mm-wide central region), fovea (central pit), foveola (innermost ~0.35 mm of the fovea), parafovea (~0.5--1.5 mm eccentric ring), perifovea (~1.5--3 mm eccentric ring), and ONH / optic disc (~4 mm nasal to the fovea). Overlay the 6 x 6 mm OCT scanning window used by the thesis cohort as a dashed square centred on the fovea. Currently rendered as an `\fbox` placeholder pending a real graphic.
- [ ] TODO: produce Figure `fig:bg:retinal-anatomy` placed in `02-background.tex` §2.1.2 (formerly §2.1.1) -- two-panel schematic for readers without a clinical background: (left) labelled cross-section through a healthy macula showing the principal retinal layers from ILM through RNFL, GCL+IPL, INL+OPL, ONL, photoreceptor IS/OS bands (including the ellipsoid zone), RPE, and Bruch's membrane, with the choriocapillaris immediately beneath; (right) a representative OCT B-scan through a GA-affected macula highlighting the dropout of the outer-retinal layers within the lesion and the corresponding choroidal hypertransmission signature beneath. Mirror the channel ordering of the eleven-channel state tensor used in the thesis. Currently rendered as an `\fbox` placeholder pending a real graphic.
- [ ] TODO: produce Figure `fig:bg:oct-acquisition` placed in `02-background.tex` §2.1.3 -- four-panel schematic of OCT acquisition geometry intended to anchor the geometric vocabulary (A-scan, B-scan, volume, en-face) for ML readers without imaging background: (a) eye + single probe beam + inset depth-vs-reflectivity profile of one A-scan; (b) the same with the beam scanned laterally along one axis to form a B-scan; (c) the beam scanned in both lateral directions to form a 3D volume of shape 49 x 1024 x 496 with the 6 x 6 mm physical footprint annotated; (d) the volume projected axially onto the fundus plane to yield the 49 x 1024 en-face image used by the model, with a representative GA lesion visible as a region of altered signal. Currently rendered as an `\fbox` placeholder pending a real graphic.
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
