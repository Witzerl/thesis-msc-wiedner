# Prompt: full multi-perspective review of the thesis

Use: paste everything below the line into a fresh Claude Code session opened in
`D:\Schule\MasterThesis\thesis`. For an external LLM without file access, attach the compiled PDF
and `WRITING_GUIDE.md`, and read "file:line" as "page, paragraph" (see the note at the end).

---

## Task

Review the **complete current version** of my master thesis from six reader perspectives and
produce **one list of findings, ordered by position in the thesis**, each with a severity. This is a
review only: **do not edit any `.tex`, `.bib` or figure file.** Write the results to
`reviews/full-review-<YYYY-MM-DD>/`.

The thesis: *Neural PDE Solvers for Geographic Atrophy Progression Prediction from Longitudinal OCT
Imaging*, JKU Linz with the Medical University of Vienna. Main question: what is needed to forecast
GA progression from longitudinal OCT, (1) what kind of framework, (2) what kind of operator.

## The baseline you check against

The rule set is **`WRITING_GUIDE.md`** (repository root). Read it in full before anything else. It
has three layers, in this order of precedence:

1. **§11, the supervisor's instructions** (Dmitrii Lachinov, reviews 1 and 2). Highest precedence.
2. **The project's own rules**: `CLAUDE.md` → Writing Style, Terminology, Hard Rules (passive voice,
   no *we/I*, `\citet`/`\citep`, terminology fixed, captions self-contained, no "test set" wording).
   §9 of the guide lists where these override the book.
3. **§0–§10, the rules distilled from Skern, *Writing Scientific English***: formal English,
   punctuation, articles, confusable words, the eight clarity guidelines, linking words,
   document structure, figures and tables, tenses, revision questions.

Cite the rule behind every finding as `Guide §x.y` or `CLAUDE.md: <rule>`. A finding that no rule
covers is allowed only for a factual error, a contradiction, or something a real examiner would
clearly object to; mark its rule as `judgement` and say why.

## Read first (context, not material to review)

- `WRITING_GUIDE.md` (all of it), `CLAUDE.md`.
- `THESIS_STRUCTURE.md`: the Framing block and the revisions of 2026-09-25, 2026-10-12 and
  2026-10-18 (the agreed chapter structure and page budgets).
- `NOTES.md`: skim for **decisions already taken** (see "Settled decisions" below). Do not take its
  open TODO list as findings; you review the text, not the to-do list.
- **`reviews/feedback-log.md`, the log of all feedback received and how each item was resolved**
  (supervisor reviews 1 and 2, the author's tablet reviews, the editorial review). Read it in full;
  see "Using the feedback log" below. If the file does not exist, say so in the summary and rely on
  the settled-decisions list alone.

## Material to review, in this order

Front matter: title page and keywords (`main-thesis.tex`), `00-abstract.tex` (English abstract and
German Kurzfassung), `acknowledgements.tex`, `acronyms.tex`. Then `01-introduction.tex` …
`07-conclusion.tex`, then `91-appendix.tex` (Appendices A–G), then `references.bib` as rendered.

Rules for what counts as text:
- Review only what appears in the PDF. Skip lines that start with `%`, text after an unescaped `%`,
  and anything inside `\iffalse … \fi`. Inline `% TODO` comments are not findings, **but** anything
  unfinished that is *visible* in the PDF (placeholder boxes, "[TODO]", "??", "xxx", empty table
  cells) is.
- Build once with `latexmk -xelatex -interaction=nonstopmode -outdir=<scratch dir> main-thesis.tex`
  (isolated output directory, so the editor's auto-build does not collide) to get page numbers and
  to list undefined references, undefined citations and overfull boxes from the log.

## The six reviewers

Run every chapter through all six. Each perspective has its own question; the checklists name the
guide sections it applies most.

**1. Supervisor** (Dmitrii Lachinov, ML for retinal imaging, co-author of the Mai et al. 2024 line of
work). *"Does this follow what I asked for?"*
- Guide §11 in full: abstract quality; every term defined before use (medical terms above all);
  the opening-chapter order; every section with intro paragraph + thesis statement, body,
  conclusion; no LLM sentence patterns (§11.5); one table or plot per results subsection, with a
  small excerpt of the main table next to each ablation; contributions as bullets that say what is
  new and why it matters.
- The notation of §2.5.2 (problem statement) is used consistently in Chapters 4–5.
- The register matches a paper such as MM-PDE (Hu et al., ICLR 2024): fact, number, source.

**2. External reviewer** (expert in neural PDE solvers / operator learning, conference-reviewer
mindset). *"Are the claims supported, fairly compared and reproducible?"*
- Every claim of an effect is backed by the reported numbers and their stated criteria (§5.1.5,
  Appendix E); nothing is stated more strongly than the evidence (Guide §1, "no absolute claims";
  §5.4 speculation).
- Comparisons are fair (parameter matching, same pipeline); caveats travel with the numbers they
  qualify; nulls are reported as nulls, not hidden or inflated.
- Methods carry enough detail to re-run the work (Guide §5.8); figures and tables stand alone
  (§5.2).
- Positioning against related work (Mai et al. 2024, Gigon et al. 2021, Lachinov et al. 2024, the
  operator literature) is accurate and the novelty claims hold.

**3. Examiner** (JKU, grades the thesis). *"Is the research question answered, is the work honest,
are the formal requirements met?"*
- Both sub-questions are stated in Chapter 1 and answered explicitly in Chapter 7; contributions,
  abstract, results and conclusion say the same thing.
- Hour-glass structure (THESIS_STRUCTURE.md); chapters within their page budgets; limitations
  stated honestly; nothing called a test-set result.
- Formal: title page complete, English abstract and Kurzfassung agree in content, lists of
  figures/tables/abbreviations complete, every acronym used is in `acronyms.tex` and defined at
  first use, every figure, table and appendix is referred to from the text, consistent reference
  formatting, no broken `\ref`/`\cite`.

**4. Colleague** (fellow ML master student, no medical or numerical-PDE background, reads front to
back once). *"Where do I get lost?"*
- Keep a **prerequisite ledger**: each technical or medical term, where it first appears, and where
  (or whether) it is explained before that point (Guide §11.2).
- Flag jumps in the argument, forward references that a reader cannot yet follow, paragraphs with
  two themes, sentences too long to read in one pass (Guide §2.3, §2.4), missing links between
  paragraphs and sections (§3).

**5. Clinical reader** (ophthalmologist familiar with GA imaging and trials). *"Is the medicine right
and is the clinical framing careful?"*
- Medical statements in Chapters 1–3 and §6.2 are correct and appropriately hedged; terms (GA,
  cRORA, iRORA, FAF, SLO, en-face, layer names) are used correctly; the mask provenance (FAF-based
  annotation registered onto the OCT grid) is stated consistently; claims of clinical usefulness do
  not outrun the evidence.

**6. Copy editor** (scientific English). *"Does every sentence follow the mechanical rules?"*
- Guide §1 (formal English, punctuation, articles, confusable words), §2.5 positive sentences,
  §2.6 impersonal active instead of weak passive, §2.7 needless words, §3 linking words, §4
  repetition vs fixed terms, §6 tenses; British spelling throughout; units, number formats,
  capitalisation of headings and hyphenation consistent.
- Report mechanical issues that recur many times **once**, as a cross-cutting finding with a count
  and up to five example locations, not one finding per occurrence.

## Severity

| Level | Meaning | Typical examples |
|---|---|---|
| **S1 Critical** | must be fixed before submission; an examiner would hold it against the thesis | a factual error; two places that contradict each other (numbers, claims, definitions); a claim the reported results do not support; a sub-question not answered; anything unfinished visible in the PDF; a broken reference or citation; a term the argument depends on that is never defined; a missing formal element |
| **S2 Major** | a careful examiner or reviewer would notice and mark down | a section without intro / thesis statement / conclusion; an abstract weakness; a results subsection without its table or plot; a missing caveat or limitation; structure out of the agreed order; a caption that does not stand alone; a figure or table not referred to; an LLM sentence pattern (§11.5); a medical term used wrongly |
| **S3 Moderate** | hurts readability, but the content is right | a long or nested sentence; negative or padded phrasing; a weak link between paragraphs; repetition across chapters; drifting terminology; inconsistent tense |
| **S4 Minor** | polish | sentence-initial *Because*; an article; a comma; *data is*; a hyphen; spelling variety |

Calibrate across chapters: the same kind of problem gets the same level everywhere. When reviewers
disagree, use the highest level that at least one reviewer can justify with a rule, and note the
disagreement.

## Settled decisions: do not raise these again

These were decided by the author or the supervisor; a finding may only point out that the text does
not *implement* them correctly.
- Passive voice, no *we/I* (impersonal active subjects such as "Table 5.1 shows" are fine).
- Introduction and Background stay separate chapters (accepted by the supervisor); drugs and patient
  management stay in §1.1.
- Everything MM-PDE (mesh mover, dual branch, α gate, mesh quality) is in Appendix G; the main text
  keeps only pointer sentences.
- MP-PDE is described in Chapter 4 with the other operators, not in the Background.
- The term *operator* is kept and defined in §1.2 / §2.5.2; *anchor* is kept and defined in §5.1.2.
- Chapter 5 reports seed 42 in the text; the second seed and the statistics are in Appendix E.
- The graph U-Net arm and the width-32 U-Net are not reported; the provenance of the two graph
  frameworks (suggested by the clinical partner) is not written anywhere.
- British spelling; the JKU template's layout.
- The run-in headings of §6.4 stay.
- Figures 2.1–2.3 are AI-generated drawings with a note in the caption.
If a decision in `NOTES.md` or the feedback log is marked as decided and you believe it hurts the
thesis, list it once in the summary under "Decisions worth reconsidering", not as a finding.

## Using the feedback log

The log records, for each piece of feedback, who gave it, what it asked for, and what was done
about it. Use it in three ways:

1. **Decided items extend the settled-decisions list.** An item resolved as "keep as is",
   "decided against" or "author's choice" is settled: do not raise it again.
2. **Resolved items are checked for regressions.** For every item resolved by a change to the
   text, check that the current text still implements it, since later edits may have undone it.
   A regression is a finding: severity at least the level the original problem would have today,
   rule `Feedback log <item ID>`, and `Text:` quoting what the thesis says now.
3. **Recurrences are marked.** When a new finding is the same kind of problem as an earlier
   feedback item (e.g. an LLM sentence pattern the supervisor already objected to, a term again
   used before its definition), add `Recurs: <item ID>` to the finding. Repeat feedback from the
   supervisor weighs more: raise such a finding one severity level, at most to S2.

Open items in the log (not yet resolved) are not findings in themselves. If the current text still
shows the problem, report it normally with `Recurs: <item ID>`.

In `00-summary.md`, add a section **"Feedback log check"**: the number of items checked, the list
of regressions (IDs), and the items whose resolution could not be confirmed in the text (with the
reason, e.g. "the section was rewritten and the point no longer applies").

## Procedure

1. **Context.** Read the files under "Read first". Build the PDF and keep the log.
2. **Whole-thesis pass** (one reader, front to back): structure against THESIS_STRUCTURE.md;
   research question → answers; abstract ↔ contributions ↔ results ↔ conclusion; **internal
   consistency of every number** that appears more than once (abstract, chapters, tables, captions,
   appendix); terminology table (one term, one meaning, one name); the prerequisite ledger.
3. **Chapter passes.** For each chapter (front matter, 1, 2, 3, 4, 5, 6–7, appendices), apply all six
   perspectives. If you can run subagents, give each chapter group to its own agent with the full
   guide and this prompt, and keep the whole-thesis pass separate.
4. **Feedback-log check.** Go through the log item by item as described in "Using the feedback
   log"; record regressions as findings at their location.
5. **Verification.** Check every finding before it enters the list (a second agent per chapter, if
   available): the quoted text exists verbatim at the stated line and is not commented out; the
   cited rule says what the finding claims; the item is not a settled decision; the suggested fix
   keeps meaning, hedges, numbers, citations, `\ref`s and the passive-voice rule. Drop what fails;
   merge duplicates (list all reviewers who found it).
6. **Ordering.** Sort strictly by position: front matter → Ch. 1 → … → Ch. 7 → Appendices A–G →
   bibliography; within a section by line. A cross-cutting finding sits at its first occurrence and
   lists the other locations.

## Rules for findings

- One finding per problem. Quote the text verbatim, at most two lines.
- Every suggested fix is concrete: for a sentence, a rewrite; for structure, what moves where. A
  rewrite follows the guide itself (passive or impersonal active, no LLM patterns, numbers and
  citations unchanged).
- Never invent numbers, citations or results. If a fix needs a fact the thesis does not contain,
  say "needs: <what>" instead of supplying it.
- Do not re-verify citations against their source PDFs (`literature/_ledger.md` covers that) and do
  not re-check numbers against the run records; do check that each number is the same everywhere
  it appears.
- No praise items in the list. Positive observations go in the per-chapter verdicts.

## Output

Write two files to `reviews/full-review-<YYYY-MM-DD>/`.

**`00-summary.md`**
1. One paragraph per reviewer: overall verdict, the three things that reviewer would fix first. The
   examiner's paragraph ends with the main risk to the grade.
2. Counts by severity and by chapter (table).
3. **Fix first**: the 15 most important findings by ID, one line each.
4. Cross-cutting issues (structure, terminology, recurring language patterns, consistency), each
   with the IDs it covers.
5. The prerequisite ledger: term | first use (file:line, page) | explained where | OK / late /
   missing.
6. The terminology table: concept | names used | locations | proposed single name.
7. Build log: undefined references, undefined citations, overfull boxes above 5 pt, with pages.
8. Feedback log check (see "Using the feedback log").
9. Decisions worth reconsidering (if any), each with one sentence of reasoning.

**`01-findings.md`**, the full sequential list. Start with an index table
`ID | Location | Severity | Reviewer(s) | One line`, then every finding in this form:

```
### R-0045 · S2 · §5.3.2 Physical Reach — 05-experiments.tex:412 (p. 61)
Reviewers: Supervisor, Examiner
Rule: Guide §11.4 (intro paragraph with thesis statement)
Text: "…verbatim, at most two lines…"
Problem: what is wrong and why it matters to this reader.
Fix: the concrete change or rewrite.
Recurs: (feedback-log item ID, if any)
Status: open
```

IDs run continuously in thesis order (R-0001, R-0002, …), so I can work down the list and tick items
off by changing `Status`.

When done, report in the chat: the number of findings per severity, the five S1 items you consider
most serious, and where the files are.

---

**Note for use outside this repository.** Attach the PDF and `WRITING_GUIDE.md`; replace
"file:line" with "page, paragraph n"; skip the build step and the "Read first" files except the
guide; keep the settled-decisions list in the prompt, since the external model cannot read
`NOTES.md`; attach the feedback log as a file.

---

**Format the review expects for `reviews/feedback-log.md`** (any layout works if these fields are
there; one row or block per item):

| Field | Example |
|---|---|
| ID | SV1-07 (supervisor review 1, comment 7); TAB6-12; ED-5c.11 |
| Source and date | Supervisor review 1, 2026-10-12 |
| Location then | §1.3, p. 4 |
| Feedback | "Why Neural PDE Solvers?" is a poor heading; avoid questions |
| Resolution | renamed to "Choice of the Modelling Approach" (§2.5.1) |
| Status | fixed / decided: keep / decided: rejected / open |
