# Structure proposal for Chapters 1–3 (2026-10-12, for discussion)

Goal: follow the supervisor's ordering (medical context → PDEs/solvers without GA → motivation →
formal problem statement → outline; every term defined before use; contributions as bullets;
no question in headings) and the AI review's structure items, while **keeping Introduction and
Background as separate chapters** and **moving existing text instead of rewriting it**.

## Overview

| New | Content | Comes from | New writing |
|---|---|---|---|
| **Ch. 1 Introduction** | | | |
| 1.1 Clinical Motivation | AMD/GA burden, ageing, bilaterality, drugs, why timing matters | §1.1 as is | Half-sentence definitions of AMD, GA, fovea, visual acuity, OCT (prerequisite audit); drug sentence: both drugs approved in the US, not in the EU, only slow progression; one sentence on highly variable growth rates (SV-1.1, SV-1.3) |
| 1.2 Aim of the Thesis | Forecast a lesion map, not a risk score; separate the setup from the operator; research question | §1.2 first paragraph; §1.3 paragraph "Which of them … equal terms" (l. 162–168); research-question block (l. 176–195) | Heading (was "Problem Statement"); 1–2 bridge sentences |
| 1.3 Contributions | Bullet list | the contributions paragraph (l. 197–206), split into bullets | "Why it matters" half-sentence per bullet; Δt claim after the literature check (SV-1.6) |
| 1.4 Thesis Outline | | §1.4 | Update the chapter descriptions |
| **Ch. 2 Background** | | | |
| *(opener)* | What the chapter covers and why Ch. 3–5 need it | — | 3–4 sentences (AI T1, S15) |
| 2.1 Medical Background | | §2.1 | Section opener replaces the "machine-learning audience" paragraph (2a.1) |
| 2.1.1 Eye Anatomy | Eye, macula, fovea, retinal layers, photoreceptors, RPE, Fig. 2.1/2.2 | §2.1.1 "A short anatomy primer" | Heading only (SV-2.1) |
| 2.1.2 Retinal Imaging | OCT principle, A-/B-scan, volume; OCT vs FAF; en-face maps | §2.1.3 + §2.1.4 | 2–3 sentences on SLO and FAF as modalities (now only mentioned in passing) |
| 2.1.3 Geographic Atrophy | Pathophysiology, CAM/cRORA, OCT signatures | §2.1.2 | Drop the opening sentence that defines the retina again (R4, 2a.9); CAM sentence reworded (SV-2.4) |
| 2.2 Partial Differential Equations and Numerical Solvers | PDE notation, stencils, time stepping, CFL, strengths and limits | §2.2 intro, §2.2.1–§2.2.3 | Opener without "the approach of this thesis treats GA …"; remove the few thesis/GA sentences (e.g. "The en-face grid of this thesis is of that type") |
| 2.3 Neural PDE Solvers and Surrogate Architectures | Learned solvers once: hybrid/end-to-end, MP-PDE as learned stencil, then operators vs autoregressive, pushforward, U-Net/FNO/FEN, inductive biases | §2.2.4 moved to the start of §2.3 | One bridge sentence (fixes AI T8/S17: learned solvers introduced twice) |
| 2.4 Related Work | | §2.4 | Later: expand into subsections (SV-2.7), the only larger writing task |
| 2.5 Modelling Approach and Problem Statement *(title open, no question)* | | | |
| 2.5.1 Choice of the Modelling Approach | Data properties (irregular visits, multi-channel state, covariates); framework needed around the model; GA as local boundary growth (Yehoshua, Eq. 1.1); anisotropy; why the solver structure fits (four bullets); CFL → reach question | §1.2 paragraphs 2–3; §1.3 paragraphs 1–3; §2.2.5 | Merge the overlap between §1.3 ¶1 and the §2.2.5 "neighbourhood" bullet; add one sentence on the 21:1 pixel spacing as the form of the reach question (AI S16/T2) |
| 2.5.2 Problem Statement | Formal: visits $u_{t_k}$ at irregular $t_k$ on the anisotropic lattice, $C=11$ channels, learn $f_\theta$ with $u_{t+\Delta t}=u_t+\Delta t\,f_\theta(u_t,\Delta t)$, rollout, evaluation target; the research question restated in this notation | — | **New, about one page** (supervisor M3.4). Notation now spread over §2.2.2, §3.2, §4.2.1 is defined here once; later sections refer back |
| **Ch. 3 Data** | | | |
| 3.1 Dataset | | §3.1 + §2.1.6 | De-duplicate; the 6 mm window literature paragraph goes to §3.3 (AI R2, T3) |
| 3.2 State Representation | | §3.2 + §2.1.5 | De-duplicate the layer definition (R3); the biomarker paragraph (§2.1.5) is the clinical justification of the channels |
| 3.3–3.7 | unchanged | | SV-3.x fixes only |

## What this covers

- **Supervisor:** medical background in his order (SV-2.2, SV-2.3), PDEs without GA (M3.2),
  motivation after the context (SV-X3, M3.3), a formal problem statement with notation (M3.4),
  no question heading (M4), contributions as bullets (M5), §2.1.5–2.1.6 into Data (SV-2.5),
  §2.2.5 merged with the "Why neural PDE solvers" text (SV-X4). The only deviation: two chapters,
  with motivation and problem statement at the end of the Background instead of the end of a
  combined Introduction.
- **AI review:** T1/S15 (Ch. 2 opener), R4/2a.9 (retina defined three times), T8/S17 (learned
  solvers twice), T2/S16 (framework vs operator motivation; grid vs biological anisotropy),
  S23 (one heading holding motivation, research question and contributions), R2/R3/T3
  (cohort facts and layer definition duplicated), the AI hourglass note that §2.1.6 and §2.2.5
  belong in the technical middle.

## Rough amount of new text

Moves: almost everything. New writing: chapter/section openers and bridges (about 10–15
sentences in total), the SLO/FAF sentences, the contribution bullets (from the existing
paragraph), §2.5.2 problem statement (about one page), the term definitions from the
prerequisite audit. Related Work expansion is a separate task.

## Open choices

1. Problem statement as the last section of Ch. 2 (proposed) or as a short chapter of its own
   ("Problem Formulation") between Background and Data.
2. Drugs and patient management: stay in §1.1 (proposed, no rewrite) or move into §2.1 as the
   supervisor's list puts them.
3. Research question: stays in Ch. 1 in words (proposed) and is restated formally in §2.5.2.
4. Related Work before the problem statement (proposed, so §2.5 leads straight into Data) or
   after it.

Labels stay unchanged, so the existing `\ref`s keep resolving; prose that names "Chapter 1" or
"the Background" needs a check.
