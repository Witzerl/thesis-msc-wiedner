# Master Thesis: Neural PDE Solvers for Geographic Atrophy Progression Prediction

LaTeX source for a Master's thesis at the [Johannes Kepler University Linz](https://www.jku.at/) in collaboration with the [Medical University of Vienna](https://www.meduniwien.ac.at/).

**Topic:** Adapting two neural PDE solver frameworks — MP-PDE (Brandstetter et al., ICLR 2022) and MM-PDE (Hu et al., ICLR 2024) — to Geographic Atrophy (GA) progression prediction from longitudinal OCT imaging.

**Supervisor:** Hrvoje Bogunović (Medical University of Vienna)
**Co-supervisor:** Dmitrii Lachinov (Medical University of Vienna)


## Compilation

The JKU template requires XeLaTeX for full font support:

```
latexmk -xelatex main-thesis.tex
```


## Repository Layout

- `main-thesis.tex` — Root document.
- `00-abstract.tex` … `07-conclusion.tex` — Chapter sources (see `THESIS_STRUCTURE.md`).
- `91-appendix.tex` — Appendices.
- `acknowledgements.tex`, `acronyms.tex` — Front matter.
- `references.bib` — Bibliography (natbib).
- `jkureport.sty`, `fonts/`, `logos/` — JKU template assets.
- `images/` — Figures.
- `CLAUDE.md`, `THESIS_STRUCTURE.md`, `PROJECT_CONTEXT.md`, `NOTES.md` — Writing guidance, chapter outline, technical context, and open TODOs.


## Template Attribution

Built on the JKU LaTeX thesis and technical report template by Michael Roland
(<https://github.com/michaelroland/jku-templates-report-latex>),
licensed under the [Mozilla Public License v2.0](https://mozilla.org/MPL/2.0/).

- Copyright (c) 2021-2025 Michael Roland <<michael.roland@ins.jku.at>>
