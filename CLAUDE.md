# CLAUDE.md

## Project

Master thesis at the Johannes Kepler University in collaboration with the Medical University of Vienna: **adapting two neural PDE solver frameworks — MP-PDE (Brandstetter et al., ICLR 2022) and MM-PDE (Hu et al., ICLR 2024) — to Geographic Atrophy (GA) progression prediction from longitudinal OCT imaging.** The contribution is applied, not methodological: irregular visit intervals, multi-channel state (mask + 10 retinal layers), patient covariates (Age, Sex), and a learned surrogate encoder for PDE coefficients. Code lives in a separate repository and is treated as read-only reference — DO NOT modify it.

## Context Files

- See @THESIS_STRUCTURE.md for the fixed chapter outline. Confirm where requested content belongs before writing.
- See @PROJECT_CONTEXT.md for architectural differences (e.g., Frobenius norm, \Delta t-conditioning), dataset spacing, and supervisor constraints. Consult this before writing technical sections.
- See @NOTES.md for the single source of truth for open TODOs, supervisor feedback, pending numbers, and unresolved citations.

## Chapter Files

- 00-abstract.tex → Abstract
- 01-introduction.tex → Chapter 1: Introduction
- 02-background.tex → Chapter 2: Background
- 03-data.tex → Chapter 3: Data and Preprocessing
- 04-method.tex → Chapter 4: Method
- 05-experiments.tex → Chapter 5: Experiments
- 06-discussion.tex → Chapter 6: Discussion
- 07-conclusion.tex → Chapter 7: Conclusion
- 91-appendix.tex → Appendices
- acknowledgements.tex → Acknowledgements
- acronyms.tex → List of Abbreviations
- references.bib → Bibliography

## Literature & Second Brain Workflow (Obsidian)

All research, literature summaries, and raw ideas live in the `literature/` folder as `.md` files. This is my "Second Brain" and operates on an **Atomic Note** system (Hub and Spoke). 
- **Hub Notes:** Named after the citation key (e.g., `Brandstetter2022.md`). These only contain links to the relevant concepts.
- **Spoke/Concept Notes:** Thematic notes (e.g., `Pushforward_Trick.md`, `Delta_T_Conditioning.md`). These contain the actual synthesized bullet points, equations, and thoughts, with inline citations pointing back to the Hub notes.

**Command: `/ingest`**
When I type `/ingest [filename]`, you will execute the following pipeline to process raw paper text or notes from the `INBOX/` folder:

**Phase 1: Analysis & Proposal (DO NOT WRITE FILES YET)**
1. Read the specified file in the `INBOX/` folder.
2. Identify the core concepts, methodologies, and findings. Cross-reference these with my existing notes in `literature/` to see if we should update an existing concept note or create a new one.
3. Print a "Proposed Change Log" to the terminal formatted like this:
   * **Hub Note Creation:** `[CitationKey].md`
   * **Concept Updates:** Outline exactly which existing `.md` files in `literature/` you will append data to, and what that data is (including inline citations).
   * **New Concepts:** Outline any entirely new `.md` files you intend to create.

**Phase 2: Pause**
Stop and ask me: *"Does this plan look correct? Say 'execute' to write these files."*

**Phase 3: Execution**
Once I approve, use your file system tools to strictly create and update the `.md` files in `literature/` exactly as proposed.

## Compile Command

```
latexmk -xelatex main-thesis.tex
```

The JKU template requires XeLaTeX (not pdflatex) for full font support. Always use this command to verify compilation after edits.

## NOTES.md Workflow

- WHEN a writing task needs follow-up (missing number, unverified claim, uncertain citation) → append a new TODO. Format: `- [ ] TODO: …`
- Mirror every `% TODO:` left in the LaTeX as an entry in @NOTES.md.
- NEVER delete entries. Mark resolved as `- [x]`.
- Leave @NOTES.md in a clean, current state at session end.

## Writing Style

- **Voice:** Academic, technical, and strictly **passive voice** (e.g., "The model was adapted," "It is shown that"). Do not use "we" or "I" as this is a solo Master's thesis.
- **Tone:** Prose over bullets, but prioritize clarity. Avoid excessively dense, multi-line text blocks; keep paragraphs focused. Frame results honestly, including what did not work.
- **Formatting:** Equations labeled if referenced later. Figure and table captions must be self-contained. Align with JKU LaTeX templates.
- **Terminology:** GA, OCT, DMM, ItpNet, pushforward trick, monitor function, state tensor, \Delta t-conditioning, Frobenius norm. Use `\Delta t` consistently in LaTeX.

## Hard Rules

- **Citation Standard (natbib):** You MUST use `\citet{key}` for textual citations (e.g., "Einstein (1905) argued...") and `\citep{key}` for parenthetical citations (e.g., "...was discovered (Einstein, 1905)").
- **Knowledge base is a resource, not a constraint.** The `literature/` folder and `references.bib` are the *primary* source of citations, but they are NOT exhaustive. (a) The presence of a note in `literature/` does NOT obligate citing it if the section does not benefit from it — only cite what genuinely strengthens the argument. (b) The absence of a reference from `references.bib` does NOT forbid using it: if an external work would fill a real gap (a foundational method, a canonical clinical citation, an institutional precedent), use it inline with a placeholder author-year mention AND leave a `% TODO: cite <ProposedKey> (short bibliographic hint) once added to references.bib` immediately above the affected sentence. Mirror every such marker in @NOTES.md under the "Pending external citations" section so it is collected when the bibliography is expanded.
- **DO NOT paraphrase long passages:** Summarize, cite, move on. The author remains responsible for all originality.
- **DO NOT invent data:** WHEN results or citations are missing, leave a `% TODO:` and log it in @NOTES.md.
- **DO NOT generate figures:** Leave `\includegraphics` placeholders with descriptive filenames and full captions.
- **DO NOT restructure chapters** without explicit instruction.

## Per Request Execution

1. Review @NOTES.md, @PROJECT_CONTEXT.md, and @THESIS_STRUCTURE.md.
2. **Literature Retrieval:** If the task involves drafting or outlining a section, ALWAYS search the `literature/` folder for relevant concept notes and synthesize them before writing the LaTeX draft. Extract the required citation keys from those notes. Treat the knowledge base as the *primary* — but not exclusive — source per the Hard Rule above: an external citation may be introduced when it fills a genuine gap, provided a `% TODO: cite ...` marker accompanies it and is mirrored in @NOTES.md.
3. Write the full section to the page budget, not a skeleton.
4. Flag uncertainties with mirrored `% TODO:` + @NOTES.md entry.
5. Verify work by running `latexmk -xelatex main-thesis.tex` to fix syntax errors.
6. Update @NOTES.md before finishing.

## Git Workflow

- Work directly on the master branch
- Do NOT create worktrees or separate branches for edits
- Commit directly to master
- Do NOT add Co-Authored-By lines to commit messages
- At the end of each session, automatically commit all changes with a concise summary of what was done as the commit message