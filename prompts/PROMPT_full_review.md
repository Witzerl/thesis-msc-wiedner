# Prompt: full multi-perspective review of the thesis

**How to start it.** Open a Claude Code session in `D:\Schule\MasterThesis\thesis` with Opus and
ultracode, and type:

> ultracode: run the full review described in prompts/PROMPT_full_review.md

The session then follows "Instructions for the session" below. The review runs as a workflow of
roughly 450–600 agents and takes several hours. Every agent starts with about 100k tokens of
project context that Claude Code loads automatically (CLAUDE.md and the files it imports), so the
run consumes tens of millions of input tokens, much of it cached. The agents read this file
themselves, so change the rules here, not in the chat.

For an external LLM without file access, see the note at the end.

---

## Instructions for the session

1. Do **not** review the thesis in your own context. Copy the script in "Workflow script" below
   (without the surrounding code fence) verbatim into a file in your scratchpad directory, e.g.
   `<scratchpad>/thesis-full-review.workflow.js`, and start it with
   `Workflow({ scriptPath: "<that file>", args: { date: "<today, YYYY-MM-DD>", outDir: "reviews/full-review-<today>", feedbackLog: "reviews/feedback-log-2026-10-22.md" } })`.
   Use a newer feedback log if the author names one.
2. While it runs, answer questions from the author, nothing else. If the run stops or is
   interrupted, resume it with `Workflow({ scriptPath: "<the same file>", resumeFromRunId: "<run id>" })`
   and the same args; finished agents are reused.
3. When it returns, check that `<outDir>/00-summary.md` and `<outDir>/01-findings.md` exist. Report
   in the chat: findings per severity, the five most serious items of the fix-first list (ID,
   location, one line), everything listed under `coverage` in the return value (failed units,
   passes, batches, writes), and the paths of the files.
4. Commit only the two Markdown files, staged by path
   (`git add <outDir>/00-summary.md <outDir>/01-findings.md`). Leave `review-build.pdf`,
   `review-build.log` and every other working-tree change uncommitted, and do not edit `NOTES.md`.

---

## Task

Review the **complete current version** of my master thesis from six reader perspectives and
produce **one list of findings, ordered by position in the thesis**, each with a severity. This is a
review only: **no agent edits any `.tex`, `.bib`, figure, `NOTES.md` or `CLAUDE.md` file.** The
results go to `reviews/full-review-<YYYY-MM-DD>/`.

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

Cite the rule behind every finding as `Guide §x.y`, `CLAUDE.md: <rule>` or `Feedback log <ID>`. A
finding that no rule covers is allowed only for a factual error, a contradiction, or something a
real examiner would clearly object to; mark its rule as `judgement` and say why.

## Material to review

Front matter: title page and keywords (`main-thesis.tex`), `00-abstract.tex` (English abstract and
German Kurzfassung), `acknowledgements.tex`, `acronyms.tex`, the table of contents. Then
`01-introduction.tex` … `07-conclusion.tex`, the bibliography as rendered (printed before the
appendices), then `91-appendix.tex` (Appendices A–G).

What counts as text:
- Only what appears in the PDF. Skip lines that start with `%`, text after an unescaped `%`, and
  anything inside `\iffalse … \fi`. Inline `% TODO` comments are not findings, **but** anything
  unfinished that is *visible* in the PDF (placeholder boxes, "[TODO]", "??", "xxx", empty table
  cells) is.
- The printed version is available to every agent: the review build and its text, page by page,
  with the printed page labels.
- Context files (`THESIS_STRUCTURE.md`, `NOTES.md`, `PROJECT_CONTEXT.md`, `THESIS_FRAMEWORK.md`,
  the feedback log) are read for decisions and history, not reviewed, and they are not ground truth.
  A mismatch between the thesis and one of them is not a finding, and neither is an open TODO from
  `NOTES.md`. Consistency is checked only between places in the printed thesis.

## The six reviewers

Every unit of the thesis goes through all six. Each has its own question; the checklists name the
guide sections it applies most. A reviewer with little to say about a unit (e.g. the clinical
reader on Chapter 5) says so in its verdict and returns few or no findings.

**1. Supervisor** (Dmitrii Lachinov, ML for retinal imaging, co-author of Mai et al. 2024).
*"Does this follow what I asked for?"*
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
- Every technical or medical term is explained at or before its first use (Guide §11.2); before
  calling a term undefined, grep the earlier chapters.
- Jumps in the argument, forward references a reader cannot yet follow, paragraphs with two themes,
  sentences too long to read in one pass (Guide §2.3, §2.4), missing links between paragraphs and
  sections (§3).

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
- A mechanical issue that recurs within a unit is reported **once**, with the count in the problem
  and up to five other locations in "also at". (The thesis-wide sweep lists all locations.)
## Thesis-wide checks

The six reviewers see one unit each, so they cannot judge what only shows across chapters. Separate
passes read the whole thesis for that. Each reports its findings in the same format, at the place to
change, with the other places in "also at".

- **Structure and argument**: chapter and section order (THESIS_STRUCTURE.md, Guide §11.3), the two
  sub-questions stated in Chapter 1 and answered in Chapter 7, abstract, contributions, §5.9, §6.1
  and Chapter 7 saying the same thing, page budgets, every float and appendix referred to.
- **Flow** (four passes, each reading one stretch of the thesis front to back, overlapping at the
  chapter boundaries): every chapter and section opening connects to what came before and says
  what follows, every closing hands over; the paragraphs of a section build its argument in order
  (Guide §2.1, §5); links between paragraphs (§3); no topic introduced and dropped; forward
  references the reader cannot follow yet; places where the reader loses the thread; the
  hour-glass shape of the whole.
- **Repetition**: the same fact, caveat, argument, definition or explanation stated in full in more
  than one place (the author's rule: state it once, elsewhere a short pointer; summaries the
  structure requires, i.e. the abstract, §5.9, Chapter 7 and the short purpose statement at the
  start of a results section (Guide §11.4), are allowed but stay shorter than the original); and
  the same wording reused (sentences or stock phrases that recur across chapters), found with a
  script.
- **Consistency**:
  - *facts and definitions*: every definition and every claim about the data and the setting
    agrees wherever it is stated;
  - *numbers*: every number that appears more than once has the same value, rounding and
    comparison everywhere (four passes);
  - *terminology*: one concept, one name (the ledger step, CLAUDE.md Terminology);
  - *format*: chapter openings and closings, section intros and conclusions, headings,
    cross-reference forms, citations, numbers and units, captions, tables, figures and equations
    follow one convention throughout (two passes, which also report the convention and its
    deviations);
  - *mechanics*: recurring language patterns, with all locations.

## Severity

| Level | Meaning | Typical examples |
|---|---|---|
| **S1 Critical** | must be fixed before submission; an examiner would hold it against the thesis | a factual error; two places that contradict each other (numbers, claims, definitions); a claim the reported results do not support; a sub-question not answered; anything unfinished visible in the PDF; a broken reference or citation; a term the argument depends on that is never defined; a missing formal element |
| **S2 Major** | a careful examiner or reviewer would notice and mark down | a section without intro / thesis statement / conclusion; an abstract weakness; a results subsection without its table or plot; a missing caveat or limitation; structure out of the agreed order; a caption that does not stand alone; a figure or table not referred to; an LLM sentence pattern (§11.5); a medical term used wrongly |
| **S3 Moderate** | hurts readability, but the content is right | a long or nested sentence; negative or padded phrasing; a weak link between paragraphs; repetition across chapters; drifting terminology; inconsistent tense |
| **S4 Minor** | polish | sentence-initial *Because*; an article; a comma; *data is*; a hyphen; spelling variety |

Every agent judges the level the problem deserves on its own. The workflow sets the level as the
median of the reviewer's level and two verifiers' levels, calibrates it across the thesis, and
then raises supervisor repeats (see "Using the feedback log").

## Settled decisions: do not raise these again

These were decided by the author or the supervisor; a finding may only point out that the text does
not *implement* them correctly.
- Passive voice, no *we/I* (impersonal active subjects such as "Table 5.1 shows" are fine).
- Introduction and Background stay separate chapters (accepted by the supervisor); drugs and patient
  management stay in §1.1.
- Everything MM-PDE (mesh mover, dual branch, α gate, mesh quality) is in Appendix G; the main text
  keeps only pointer sentences.
- MP-PDE is described in Chapter 4 with the other operators, not in the Background.
- The term *operator* is kept and defined in §1.2 / §2.5.2; *anchor* is kept and defined in §5.1.2;
  *framework* is kept (not "methodology").
- Chapter 5 reports seed 42 in the text and states results in words; the second seed, SE, t and
  leave-one-fold-out statistics are in Appendix E. Tables keep "mean ± sd over the five folds".
- The graph U-Net arm and the width-32 U-Net are not reported anywhere; the provenance of the two
  graph frameworks (suggested by the clinical partner) is not written anywhere; the chronology
  (the stencil network was fixed before the T-FEN existed) is not given as a reason for the
  canonical model.
- The abstract mentions neither the moving mesh nor a comparison with another model; the keywords
  contain neither MP-PDE nor MM-PDE.
- The run-in paragraph headings were removed from §5.5, §5.6, §6.2, §6.3 and Chapter 7 on purpose;
  the run-in headings of §6.4 stay.
- Appendix D shows no "lowest Dice" panel.
- British spelling; the JKU template's layout.
- Figures 2.1–2.3 are AI-generated drawings with a note in the caption.
- The abstract is rewritten last (deferred on purpose).

Everything marked *Decided* in the feedback log is settled as well, and so are the author decisions
recorded in `NOTES.md` (tablet reviews v1–v6, "Author decision", "author:"). A reviewer who believes
a settled decision hurts the thesis returns it under "reconsider"; it appears once in the summary,
not as a finding.

## Using the feedback log

The log (`reviews/feedback-log-2026-10-22.md`, or the newer file the session names) records each
piece of feedback with its ID, the problem, the fix, and a status: *Done*, *Decided*, *Deferred*,
*Open*, or superseded. The workflow gives the AI-review items an `AI-` prefix (e.g. `AI-S4`,
`AI-1.1`) so that every ID is unique. The log is used in four ways:

1. **Decided items extend the settled-decisions list.** Do not raise them again.
2. **Done items are checked for regressions.** For every item resolved by a change to the text,
   check that the current text still implements it, since later edits may have undone it. A
   regression is a finding: severity at least the level the original problem would have today,
   rule `Feedback log <ID>`, the quote showing what the thesis says now.
3. **Recurrences are marked.** When a new finding is the same kind of problem as an earlier item
   (e.g. an LLM pattern the supervisor already objected to, a term again used before its
   definition), it carries `Recurs: <ID>`. After calibration the workflow raises a finding that
   recurs a supervisor item (IDs SV-, M, E, X) by one level, at most to S2.
4. **Deferred items are known.** They are planned for later (e.g. the abstract rewrite), so a
   problem a deferred item already covers is not a finding; the summary lists the deferred items
   that are still visible. Open items are not findings in themselves: if the current text still
   shows the problem, report it normally with `Recurs: <ID>`.

## Rules for findings

- One finding per problem. Quote the text verbatim from the source, at most two lines.
- A finding about something missing (a conclusion, a table, a definition, a reference) quotes the
  nearest printed anchor, usually the section heading or the `\ref`/`\cite` command. A finding in a
  figure file pulled in with `\input` or `\includegraphics` is located at that line of the chapter
  file. A bibliography finding is located at the `@entry` line in `references.bib`.
- Every fix is concrete: for a sentence, a rewrite; for structure, what moves where. A rewrite
  follows the guide itself (passive or impersonal active, no LLM patterns, numbers, hedges,
  citations and `\ref`s unchanged).
- Never invent numbers, citations or results. If a fix needs a fact the thesis does not contain,
  write "needs: <what>" instead of supplying it.
- Do not re-verify citations against their source PDFs (`literature/_ledger.md` covers that) and do
  not re-check numbers against the run records; do check that each number is the same everywhere
  it appears.
- Undefined references and citations of a complete build are reported by the build step; do not
  report them again.
- Report findings only for lines inside your unit; you may read anything else to check them.
- No praise in the findings. Positive observations go in the verdict.

## What the workflow does

1. **Prepare.** Build the PDF into `_work/build` (timeout handling, `-f`), save its text page by
   page with the printed page labels (PyMuPDF) and a page-search helper, and list undefined
   references, citations and overfull boxes. In parallel, cut the feedback log at its headings and
   parse each part into items with unique IDs.
2. **Review** (15 units, in parallel). Six reviewer agents per unit, plus a prerequisite-inventory
   agent; then up to two completeness rounds (a fresh agent reports what the six missed, until a
   round finds fewer than three new problems); then a merge of duplicates.
3. **Whole thesis** (in parallel with 2). The passes of "Thesis-wide checks" (structure, four flow
   passes, two repetition passes, facts, four number passes, two format passes, mechanics); the
   regression check over all *Done* feedback items in batches of 20; after the units, the
   prerequisite ledger, the terminology table and the acronym list.
4. **Verify.** Every finding is judged by three independent lenses: *text* (quote exists and is
   printed, correct line, printed page, fix preserves facts), *rule* (rule real and applicable, not
   a settled or decided item), *sceptic* (tries to refute it). A finding is dropped if the text lens
   cannot find the quote or the rule lens finds a settled item, and kept only if at least two
   lenses judge it valid.
5. **Synthesize.** Calibration agents (one per chapter group if there are many findings) align
   severities and merge duplicates; one agent groups cross-cutting themes and picks the 15 to fix
   first. The script raises supervisor repeats, sorts by position, numbers the findings and renders
   both files; writer agents save them in chunks of at most 25,000 characters, each checked
   against its expected size; a last agent joins the chunks, keeps the review build as
   `review-build.pdf` and `.log`, and removes the working files.

## Output

In `reviews/full-review-<YYYY-MM-DD>/`: `00-summary.md`, `01-findings.md`, and the review build
`review-build.pdf` / `review-build.log` that the page numbers refer to.

**`00-summary.md`**
1. One paragraph per reviewer (supervisor, external reviewer, examiner, colleague, clinical reader,
   copy editor): overall verdict and the three things that reviewer would fix first (by ID). The
   examiner's paragraph ends with the main risk to the grade. Then the verdicts of the
   whole-thesis passes.
2. Counts by severity and by chapter (table).
3. **Fix first**: the 15 most important findings by ID, one line each.
4. Cross-cutting issues (structure, terminology, recurring language patterns, consistency), each
   with the IDs it covers.
5. The prerequisite ledger: every medical and imaging term, and every term explained late or never
   (term | first use | explained | status); a count for the rest.
6. The terminology table: concept | names used | locations | proposed single name.
7. **Format conventions**: for each aspect (chapter openings and closings, headings,
   cross-references, numbers and units, captions, tables, figures, equations, …) the convention the
   thesis follows in most places, the number of deviations and where they are.
8. **Repetition across chapters**: each topic stated in full more than once, where it appears and
   where it should be stated in full.
9. Build log: undefined references, undefined citations, overfull boxes above 5 pt, with pages.
10. **Feedback log check**: items checked and their outcome, regressions (log ID → finding ID), items
   whose resolution could not be confirmed (with the reason), deferred items still visible.
11. Decisions worth reconsidering (if any), each with one sentence of reasoning.
12. Coverage: units, passes, verification batches or writes that failed, and how many findings
    could not be fully verified.

**`01-findings.md`**, the full sequential list: an index table
`ID | Location | Sev. | Reviewers | Finding`, then every finding as

```
### R-0045 · S2 · §5.3.2 Physical Reach — 05-experiments.tex:412 (p. 52)

~~~text
…verbatim source text, at most two lines…
~~~

- **Reviewers:** Supervisor, Examiner
- **Rule:** Guide §11.4 (intro paragraph with thesis statement)
- **Problem:** what is wrong and why it matters to this reader.
- **Fix:** the concrete change or rewrite.
- **Also at:** other locations (only for recurring issues)
- **Recurs:** feedback-log ID (if any)
- **Status:** open
```

IDs run continuously in thesis order (R-0001, R-0002, …). "p." is the printed page number (the page
label) of `review-build.pdf`. The author works down the list and changes `Status`.

## Workflow script

```js
export const meta = {
  name: 'thesis-full-review',
  description: 'Six-perspective review of the whole thesis against WRITING_GUIDE.md, verified and ordered by position',
  whenToUse: 'Full review of the master thesis before submission',
  phases: [
    { title: 'Prepare', detail: 'build the PDF and page text, parse the feedback log' },
    { title: 'Review', detail: 'six reviewers, an inventory and completeness rounds per unit, merge' },
    { title: 'Whole thesis', detail: 'structure, facts, numbers, mechanical sweep, feedback-log regressions, ledger' },
    { title: 'Verify', detail: 'three lenses per finding: text, rule, sceptic' },
    { title: 'Synthesize', detail: 'calibrate, order, number, write the files' },
  ],
}

// ---------- configuration ----------
const A = args || {}
if (!A.date) throw new Error('Pass args.date as YYYY-MM-DD.')
const DATE = A.date
const OUT = A.outDir || `reviews/full-review-${DATE}`
const WORK = `${OUT}/_work`
const FEEDBACK = A.feedbackLog || 'reviews/feedback-log-2026-10-22.md'
const PROMPT_FILE = 'prompts/PROMPT_full_review.md'
const PY = '"/c/Program Files/anaconda3/python.exe" -X utf8'
const VERIFY_BATCH = 25
const REGR_BATCH = 20
const MAX_COMPLETENESS_ROUNDS = 2
const CAL_SPLIT = 300
const CHUNK_CHARS = 25000

const UNITS = [
  { id: 'U01', name: 'Front matter', scope: 'main-thesis.tex up to \\mainmatter (title page, keywords, table of contents), 00-abstract.tex (English abstract and German Kurzfassung), acknowledgements.tex, acronyms.tex' },
  { id: 'U02', name: 'Chapter 1 Introduction', scope: '01-introduction.tex, the whole file' },
  { id: 'U03', name: 'Chapter 2 opener and Section 2.1 Medical Background', scope: '02-background.tex from the start up to, not including, \\section{Partial Differential Equations and Numerical Solvers}' },
  { id: 'U04', name: 'Chapter 2, Sections 2.2-2.3', scope: '02-background.tex from \\section{Partial Differential Equations and Numerical Solvers} up to, not including, \\section{Related Work}' },
  { id: 'U05', name: 'Chapter 2, Sections 2.4-2.5', scope: '02-background.tex from \\section{Related Work} to the end' },
  { id: 'U06', name: 'Chapter 3 Data', scope: '03-data.tex, the whole file' },
  { id: 'U07', name: 'Chapter 4 opener, Sections 4.1-4.2', scope: '04-method.tex from the start up to, not including, \\section{The Operators}, including figure files it pulls in with \\input' },
  { id: 'U08', name: 'Chapter 4, Sections 4.3-4.4', scope: '04-method.tex from \\section{The Operators} to the end' },
  { id: 'U09', name: 'Chapter 5 opener, Sections 5.1-5.2', scope: '05-experiments.tex from the start up to, not including, \\section{Ablation Studies}' },
  { id: 'U10', name: 'Chapter 5, Sections 5.3-5.4', scope: '05-experiments.tex from \\section{Ablation Studies} up to, not including, \\section{Negative Results}' },
  { id: 'U11', name: 'Chapter 5, Section 5.5', scope: '05-experiments.tex from \\section{Negative Results} up to, not including, \\section{Validity Diagnostics}' },
  { id: 'U12', name: 'Chapter 5, Sections 5.6-5.9', scope: '05-experiments.tex from \\section{Validity Diagnostics} to the end' },
  { id: 'U13', name: 'Chapters 6 and 7', scope: '06-discussion.tex and 07-conclusion.tex, the whole files' },
  { id: 'U14', name: 'Bibliography and Appendices A-F', scope: 'the bibliography as printed (formatting consistency and complete fields of the cited entries only, not the content of the sources; locate findings at the @entry line of references.bib), and 91-appendix.tex from the start up to, not including, \\chapter{The Moving-Mesh Extension (MM-PDE)}' },
  { id: 'U15', name: 'Appendix G', scope: '91-appendix.tex from \\chapter{The Moving-Mesh Extension (MM-PDE)} to the end' },
]
const NOTATION_UNITS = ['U07', 'U08', 'U09', 'U10', 'U11', 'U12']

const PERSONAS = [
  { key: 'supervisor', name: 'Supervisor', question: 'Does the text follow what I asked for (Guide §11)?' },
  { key: 'reviewer', name: 'External reviewer', question: 'Are the claims supported, fairly compared and reproducible?' },
  { key: 'examiner', name: 'Examiner', question: 'Is the research question answered, is the work honest, are the formal requirements met?' },
  { key: 'colleague', name: 'Colleague', question: 'Where do I, an ML master student without medical or numerical-PDE background, get lost?' },
  { key: 'clinician', name: 'Clinical reader', question: 'Is the medicine right and is the clinical framing careful?' },
  { key: 'copyeditor', name: 'Copy editor', question: 'Does every sentence follow the mechanical rules of the guide?' },
]
const PERSONA_NAMES = PERSONAS.map(p => p.name)

// Thesis order. main-thesis.tex below line 300 is front matter; from \mainmatter on it prints the bibliography.
const FILE_ORDER = ['main-thesis.tex', '00-abstract.tex', 'acknowledgements.tex', 'acronyms.tex', '01-introduction.tex', '02-background.tex', '03-data.tex', '04-method.tex', '05-experiments.tex', '06-discussion.tex', '07-conclusion.tex', 'references.bib', '91-appendix.tex']
const MAINMATTER_LINE = 300
const CHAPTER_OF = { '00-abstract.tex': 'Front matter', 'acknowledgements.tex': 'Front matter', 'acronyms.tex': 'Front matter', '01-introduction.tex': 'Ch. 1', '02-background.tex': 'Ch. 2', '03-data.tex': 'Ch. 3', '04-method.tex': 'Ch. 4', '05-experiments.tex': 'Ch. 5', '06-discussion.tex': 'Ch. 6', '07-conclusion.tex': 'Ch. 7', 'references.bib': 'Bibliography', '91-appendix.tex': 'Appendices' }
const CHAPTERS = ['Front matter', 'Ch. 1', 'Ch. 2', 'Ch. 3', 'Ch. 4', 'Ch. 5', 'Ch. 6', 'Ch. 7', 'Bibliography', 'Appendices', 'Other']
const CAL_GROUPS = [['Front matter', 'Ch. 1', 'Ch. 2', 'Ch. 3'], ['Ch. 4'], ['Ch. 5'], ['Ch. 6', 'Ch. 7', 'Bibliography', 'Appendices', 'Other']]

// ---------- shared instructions ----------
const BASE = `You are one agent in a multi-agent review of the master thesis in this repository. This is a review only: do not edit any .tex, .bib, figure, NOTES.md or CLAUDE.md file, do not commit, and run no git command that changes anything. Write files only where your task says. For this task, ignore CLAUDE.md's "Per Request Execution", "NOTES.md Workflow" and "Git Workflow" instructions and any memory rule about verifying citations against source PDFs, updating NOTES.md, building or committing; CLAUDE.md's writing and terminology rules still apply.
NOTES.md, PROJECT_CONTEXT.md, THESIS_STRUCTURE.md and THESIS_FRAMEWORK.md may be in your context automatically. They are history and context, not ground truth: never report a mismatch between the thesis and one of them, and never turn an open TODO from NOTES.md into a finding. Consistency is checked only between places in the printed thesis.
Shell: use the Bash tool (Git Bash), not PowerShell. Run Python as ${PY} (full path; a bare "python" in PowerShell is a Microsoft Store stub). Open text files with encoding="utf-8".`

const FINDPAGE = String.raw`import json, re, sys
pages = json.load(open(sys.argv[1], encoding="utf-8"))
tr = str.maketrans({"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"', "\u2013": "-", "\u2014": "-", "\ufb01": "fi", "\ufb02": "fl", "\u00a0": " "})
def norm(s):
    return re.sub(r"[\s\-]+", "", s.translate(tr)).lower()
q = norm(" ".join(sys.argv[2:]))
print([p["label"] for p in pages if q and q in norm(p["text"])])`

let RULES = ''         // full rules; set after the build
let RULES_VERIFY = ''  // short rules for the text and sceptic lenses
function setRules(buildNote) {
  const textDef = `What counts as text: only what is printed in the PDF. Skip lines that start with %, text after an unescaped %, and \\iffalse ... \\fi blocks. Inline % TODO comments are not findings; anything unfinished that is visible in the PDF (placeholder boxes, [TODO], ??, xxx, empty table cells) is.
The printed version: the review build is ${WORK}/build/main-thesis.pdf; its text, page by page with the printed page labels, is in ${WORK}/thesis-pages.json (a JSON list of {"label", "text"}). Use it to check what is actually printed (rendered references and citations, the bibliography, the table of contents, placeholders, "??"). ${buildNote}
Locations: the file name as in the repository root (e.g. 05-experiments.tex) and the 1-based line number in the file as it is now. A finding about something missing quotes the nearest printed anchor (usually the section heading or the \\ref/\\cite command); a finding in a figure file is located at its \\input/\\includegraphics line in the chapter file; a bibliography finding at the @entry line of references.bib. Quotes are copied verbatim from the source (LaTeX markup may stay), at most two lines. Use "" for empty text fields; "persona" is one of: ${PERSONA_NAMES.join(', ')}.`
  RULES = `Before you start, read WRITING_GUIDE.md in full, and read these sections of ${PROMPT_FILE}: "The baseline you check against", "Material to review", "The six reviewers", "Severity", "Settled decisions: do not raise these again", "Using the feedback log" and "Rules for findings". They define the rules, the reviewers, the severity levels and what must not be raised again. Judge each severity on its own merits; the workflow raises supervisor repeats itself.\n${textDef}`
  RULES_VERIFY = `Read these sections of ${PROMPT_FILE}: "Severity" and "Rules for findings". Look up a cited section of WRITING_GUIDE.md only if you need it.\n${textDef}`
}

// ---------- schemas ----------
const SEV = { type: 'string', enum: ['S1', 'S2', 'S3', 'S4'] }
const FINDING = {
  type: 'object',
  properties: {
    file: { type: 'string' }, line: { type: 'integer' },
    section: { type: 'string', description: 'section number and title, e.g. "§5.3.2 Physical Reach"' },
    quote: { type: 'string' }, rule: { type: 'string' }, severity: SEV,
    problem: { type: 'string' }, fix: { type: 'string' },
    recurs: { type: 'string', description: 'feedback-log ID, exactly as given, or ""' },
    alsoAt: { type: 'string', description: 'other locations of the same issue as file:line; ..., or ""' },
    persona: { type: 'string', description: 'which of the six reviewers this finding belongs to' },
  },
  required: ['file', 'line', 'section', 'quote', 'rule', 'severity', 'problem', 'fix', 'recurs', 'alsoAt', 'persona'],
}
const FIND_RESULT = {
  type: 'object',
  properties: { verdict: { type: 'string' }, findings: { type: 'array', items: FINDING }, reconsider: { type: 'array', items: { type: 'string' } } },
  required: ['verdict', 'findings', 'reconsider'],
}
const TERMS = {
  type: 'object',
  properties: { terms: { type: 'array', items: { type: 'object', properties: {
    term: { type: 'string' }, kind: { type: 'string', enum: ['medical', 'imaging', 'math', 'ml', 'project', 'other'] },
    file: { type: 'string' }, firstLine: { type: 'integer' },
    explainedAt: { type: 'string', description: 'here, <file>:<line> | earlier, <file>:<line> | later, <file>:<line> | never' },
    variants: { type: 'array', items: { type: 'string' } },
  }, required: ['term', 'kind', 'file', 'firstLine', 'explainedAt', 'variants'] } } },
  required: ['terms'],
}
const MERGE = {
  type: 'object',
  properties: { groups: { type: 'array', items: { type: 'object', properties: { keep: { type: 'integer' }, drop: { type: 'array', items: { type: 'integer' } }, alsoAt: { type: 'string' } }, required: ['keep', 'drop', 'alsoAt'] } } },
  required: ['groups'],
}
const VOTES = {
  type: 'object',
  properties: { votes: { type: 'array', items: { type: 'object', properties: {
    i: { type: 'integer' }, valid: { type: 'boolean' }, hardFail: { type: 'boolean' }, reason: { type: 'string' },
    line: { type: 'integer', description: 'corrected line, 0 if unchanged' },
    page: { type: 'string', description: 'printed page label, "" if unknown' },
    severity: SEV, fix: { type: 'string', description: 'corrected fix, "" if the fix is fine' },
  }, required: ['i', 'valid', 'hardFail', 'reason', 'line', 'page', 'severity', 'fix'] } } },
  required: ['votes'],
}
const BUILD = {
  type: 'object',
  properties: {
    ok: { type: 'boolean', description: 'a PDF was produced' },
    complete: { type: 'boolean', description: 'the last pass left no rerun warnings (labels, biber)' },
    pdfPages: { type: 'integer' }, minutes: { type: 'number' },
    chapterStartPages: { type: 'array', items: { type: 'object', properties: { chapter: { type: 'string' }, page: { type: 'string' } }, required: ['chapter', 'page'] } },
    problems: { type: 'array', items: { type: 'object', properties: {
      kind: { type: 'string', enum: ['undefined reference', 'undefined citation', 'multiply defined label', 'overfull box', 'build error', 'other'] },
      detail: { type: 'string' }, file: { type: 'string' }, line: { type: 'integer' }, page: { type: 'string' },
      quote: { type: 'string', description: 'the \\ref/\\cite command or source text at file:line' },
    }, required: ['kind', 'detail', 'file', 'line', 'page', 'quote'] } },
  },
  required: ['ok', 'complete', 'pdfPages', 'minutes', 'chapterStartPages', 'problems'],
}
const FB_SCOUT = {
  type: 'object',
  properties: { exists: { type: 'boolean' }, sections: { type: 'array', items: { type: 'object', properties: { title: { type: 'string' }, startLine: { type: 'integer' }, endLine: { type: 'integer' } }, required: ['title', 'startLine', 'endLine'] } } },
  required: ['exists', 'sections'],
}
const FB_ITEMS = {
  type: 'object',
  properties: { items: { type: 'array', items: { type: 'object', properties: {
    id: { type: 'string' }, logLine: { type: 'integer' }, source: { type: 'string' }, locationThen: { type: 'string' },
    feedback: { type: 'string' }, resolution: { type: 'string' },
    status: { type: 'string', enum: ['fixed', 'decided', 'deferred', 'open', 'other'] },
    unit: { type: 'string', enum: [...UNITS.map(u => u.id), 'none'] },
  }, required: ['id', 'logLine', 'source', 'locationThen', 'feedback', 'resolution', 'status', 'unit'] } } },
  required: ['items'],
}
const REGR = {
  type: 'object',
  properties: {
    checks: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, status: { type: 'string', enum: ['holds', 'regressed', 'no longer applies', 'unclear'] }, note: { type: 'string' } }, required: ['id', 'status', 'note'] } },
    findings: { type: 'array', items: FINDING },
  },
  required: ['checks', 'findings'],
}
const LEDGER = {
  type: 'object',
  properties: {
    corrections: { type: 'array', items: { type: 'object', properties: { term: { type: 'string' }, status: { type: 'string', enum: ['ok', 'late', 'missing'] }, explained: { type: 'string' } }, required: ['term', 'status', 'explained'] } },
    terminology: { type: 'array', items: { type: 'object', properties: { concept: { type: 'string' }, names: { type: 'array', items: { type: 'string' } }, locations: { type: 'string' }, proposed: { type: 'string' } }, required: ['concept', 'names', 'locations', 'proposed'] } },
    findings: { type: 'array', items: FINDING },
  },
  required: ['corrections', 'terminology', 'findings'],
}
const CAL_GROUP = {
  type: 'object',
  properties: {
    changes: { type: 'array', items: { type: 'object', properties: { tid: { type: 'string' }, severity: SEV, reason: { type: 'string' } }, required: ['tid', 'severity', 'reason'] } },
    merges: { type: 'array', items: { type: 'object', properties: { keep: { type: 'string' }, drop: { type: 'array', items: { type: 'string' } } }, required: ['keep', 'drop'] } },
  },
  required: ['changes', 'merges'],
}
const THEMES = {
  type: 'object',
  properties: {
    merges: { type: 'array', items: { type: 'object', properties: { keep: { type: 'string' }, drop: { type: 'array', items: { type: 'string' } } }, required: ['keep', 'drop'] } },
    crossCutting: { type: 'array', items: { type: 'object', properties: { title: { type: 'string' }, description: { type: 'string' }, tids: { type: 'array', items: { type: 'string' } } }, required: ['title', 'description', 'tids'] } },
    fixFirst: { type: 'array', items: { type: 'string' } },
    reconsider: { type: 'array', items: { type: 'object', properties: { decision: { type: 'string' }, reason: { type: 'string' } }, required: ['decision', 'reason'] } },
  },
  required: ['merges', 'crossCutting', 'fixFirst', 'reconsider'],
}
const FORMAT_RESULT = {
  type: 'object',
  properties: {
    verdict: { type: 'string' }, findings: { type: 'array', items: FINDING }, reconsider: { type: 'array', items: { type: 'string' } },
    conventions: { type: 'array', items: { type: 'object', properties: {
      aspect: { type: 'string' }, convention: { type: 'string', description: 'the form used in most places, or the form the rules require' },
      deviations: { type: 'integer' }, where: { type: 'string', description: 'chapters or file:line of the deviations, "" if none' },
    }, required: ['aspect', 'convention', 'deviations', 'where'] } },
  },
  required: ['verdict', 'findings', 'reconsider', 'conventions'],
}
const REPEAT_RESULT = {
  type: 'object',
  properties: {
    verdict: { type: 'string' }, findings: { type: 'array', items: FINDING }, reconsider: { type: 'array', items: { type: 'string' } },
    repeats: { type: 'array', items: { type: 'object', properties: {
      topic: { type: 'string' }, places: { type: 'string', description: 'every place it is stated, as file:line; ...' },
      keep: { type: 'string', description: 'the place where it should be stated in full' },
    }, required: ['topic', 'places', 'keep'] } },
  },
  required: ['verdict', 'findings', 'reconsider', 'repeats'],
}
const PARAS = {
  type: 'object',
  properties: { paragraphs: { type: 'array', items: { type: 'object', properties: { reviewer: { type: 'string' }, text: { type: 'string' } }, required: ['reviewer', 'text'] } } },
  required: ['paragraphs'],
}
const WROTE = {
  type: 'object',
  properties: { chars: { type: 'integer' }, newlines: { type: 'integer' } },
  required: ['chars', 'newlines'],
}
const ASSEMBLED = {
  type: 'object',
  properties: { ok: { type: 'boolean' }, findingsHeadings: { type: 'integer' }, indexRows: { type: 'integer' }, problems: { type: 'string' }, deleted: { type: 'string' } },
  required: ['ok', 'findingsHeadings', 'indexRows', 'problems', 'deleted'],
}

// ---------- helpers ----------
const SEV_N = { S1: 1, S2: 2, S3: 3, S4: 4 }
const N_SEV = ['', 'S1', 'S2', 'S3', 'S4']
const FAILS = []  // everything that did not complete, for the coverage report
let UNVERIFIED = 0
let DROPPED = 0
function sevOf(s) { return SEV_N[s] ? s : 'S3' }
function medianSev(list) {
  const v = list.filter(s => SEV_N[s]).map(s => SEV_N[s]).sort((a, b) => a - b)
  return v.length ? N_SEV[v[Math.floor((v.length - 1) / 2)]] : 'S3'
}
function chunk(arr, n) { const out = []; for (let i = 0; i < arr.length; i += n) out.push(arr.slice(i, i + n)); return out }
function normFile(f) { const m = String(f || '').replace(/\\/g, '/').match(/([A-Za-z0-9_.-]+\.(?:tex|bib|md|py))/); return m ? m[1] : String(f || '') }
function rankOf(file, line) {
  const f = normFile(file)
  if (f === 'main-thesis.tex') return (line || 0) >= MAINMATTER_LINE ? FILE_ORDER.indexOf('references.bib') - 0.5 : 0
  const i = FILE_ORDER.indexOf(f)
  return i < 0 ? FILE_ORDER.length : i
}
function posKey(file, line) { return rankOf(file, line) * 1e6 + (line || 0) }
function chapterOf(file, line) {
  const f = normFile(file)
  if (f === 'main-thesis.tex') return (line || 0) >= MAINMATTER_LINE ? 'Bibliography' : 'Front matter'
  return CHAPTER_OF[f] || 'Other'
}
function oneLine(s, n) { const t = String(s || '').replace(/\s+/g, ' ').trim(); return t.length > n ? t.slice(0, n - 1) + '…' : t }
function cell(s) { return String(s || '').replace(/\|/g, '\\|') }
function tokens(s) { return String(s || '').split(/[\s,;:()]+/).filter(Boolean) }
const SUP_ID = /^(SV-|M\d|E\d|X\d)/
function personaOf(f, fallback) { return PERSONA_NAMES.includes(f.persona) ? f.persona : fallback }
function fmtItem(it, n) { return `${it.id} [${it.status}] ${oneLine(it.feedback, n)} -> ${oneLine(it.resolution, Math.round(n * 0.8))}` }

// Merge duplicates. groups: [{keep, drop: [...], alsoAt}] with indices into list. Returns the kept list and the redirect map.
function applyMerges(list, groups, mostSevere) {
  const out = list.map(f => ({ ...f, reviewers: [...(f.reviewers || [])] }))
  const into = new Map()
  const root = i => { const seen = new Set(); while (into.has(i) && !seen.has(i)) { seen.add(i); i = into.get(i) } return i }
  for (const g of groups) {
    if (g.keep === undefined || g.keep === null || !out[g.keep]) continue
    const ki = root(g.keep)
    const k = out[ki]
    for (const d0 of g.drop || []) {
      if (d0 === undefined || d0 === null || !out[d0]) continue
      const d = root(d0)
      if (d === ki) continue
      const x = out[d]
      into.set(d, ki)
      for (const r of x.reviewers) if (!k.reviewers.includes(r)) k.reviewers.push(r)
      if (mostSevere && SEV_N[sevOf(x.severity)] < SEV_N[sevOf(k.severity)]) k.severity = x.severity
      const extra = [x.alsoAt, (normFile(x.file) !== normFile(k.file) || Math.abs((x.line || 0) - (k.line || 0)) > 3) ? `${normFile(x.file)}:${x.line}` : ''].filter(Boolean)
      if (extra.length) k.alsoAt = [k.alsoAt, ...extra].filter(Boolean).join('; ')
      if (!k.recurs && x.recurs) k.recurs = x.recurs
      if (!k.page && x.page) k.page = x.page
    }
    if (g.alsoAt) k.alsoAt = [k.alsoAt, g.alsoAt].filter(Boolean).join('; ')
  }
  return { list: out.filter((_, i) => !into.has(i)), into, root }
}

// Split text at line ends into chunks of at most `max` characters; no chunk ends on an empty line.
function splitText(text, max) {
  const lines = text.split('\n')
  const pieces = lines.map((l, i) => l + (i < lines.length - 1 ? '\n' : ''))
  const parts = []
  let cur = ''
  for (const p of pieces) {
    if (cur.length + p.length > max && cur.length && !cur.endsWith('\n\n')) { parts.push(cur); cur = '' }
    cur += p
  }
  if (cur.length) parts.push(cur)
  return parts
}

// ---------- verification (three lenses) ----------
const LENSES = [
  { key: 'text', full: false, prompt: `TEXT FIDELITY. For each finding: (a) open the file and check that the quote occurs verbatim at the stated line or near it, and that it is printed (not in a comment or an \\iffalse block); give the correct line in "line" (0 if the stated line is right). For references.bib, check the source entry. hardFail = true only if the quote is not empty and occurs nowhere near the stated place in the printed source. (b) Find its printed page: run ${PY} ${WORK}/findpage.py ${WORK}/thesis-pages.json followed by 4-8 plain words of the passage as printed (no math, symbols, citations or LaTeX); try another run of words if there is no hit; it prints page labels; "" if not found. (c) Check that the fix keeps the meaning, hedges, numbers, citations, \\ref commands and the passive-voice rule, and follows WRITING_GUIDE.md itself; if not, give a corrected fix in "fix", else "". valid = false if the problem statement misreads the text. Give your severity per the scale.` },
  { key: 'rule', full: true, prompt: `RULE FIDELITY. For each finding: is the cited rule real (look it up in WRITING_GUIDE.md, CLAUDE.md or the feedback log ${FEEDBACK}) and does it say what the finding claims? Does the finding re-raise a settled decision (section "Settled decisions" of ${PROMPT_FILE}), an item the feedback log marks as Decided (grep the log for the topic; AI- IDs appear there without the prefix), or an author decision in NOTES.md (grep for the topic together with "author" or "tablet review")? Does it report a problem a Deferred log item already covers? hardFail = true if it re-raises a settled, decided or deferred item. valid = false if neither the cited rule nor a factual error, a contradiction or a clear examiner objection supports it. Give your severity per the scale; line 0, page "", fix "".` },
  { key: 'sceptic', full: false, prompt: `SCEPTIC. Try to refute each finding. Read the passage and its surroundings: is this a real problem for the named reader, or a matter of taste, a false positive, a misreading of the thesis, or already handled in the next sentence or in a nearby footnote, caption or section? Default to valid = false when you are unsure. Set hardFail = false. Give the severity you think is right per the scale; line 0, page "", fix "".` },
]

async function verifyBatch(label, scope, batch, bi) {
  const listing = JSON.stringify(batch.map((f, i) => ({ i, file: f.file, line: f.line, section: f.section, quote: f.quote, rule: f.rule, severity: f.severity, reviewers: f.reviewers, problem: f.problem, fix: f.fix, recurs: f.recurs, alsoAt: f.alsoAt })), null, 1)
  const res = await parallel(LENSES.map(l => () => agent(
    `${BASE}\n\n${l.full ? RULES : RULES_VERIFY}\n\nTask: verify review findings (${label}, batch ${bi + 1}). The reviewed text: ${scope}.\nYour lens: ${l.prompt}\n\nReturn exactly one vote per finding, identified by its index i.\nFindings (JSON):\n${listing}`,
    { label: `verify:${label}:${l.key}:${bi + 1}`, phase: 'Verify', schema: VOTES })))
  res.forEach((r, k) => { if (!r) FAILS.push(`verification lens ${LENSES[k].key} for ${label} batch ${bi + 1} (${batch.length} findings)`) })
  const byLens = res.map(r => { const m = new Map(); for (const v of (r && r.votes) || []) m.set(v.i, v); return m })
  const kept = []
  batch.forEach((f, i) => {
    const vs = byLens.map(m => m.get(i) || null)
    const [text, rule, sceptic] = vs
    if ((text && text.hardFail) || (rule && rule.hardFail)) { DROPPED++; return }
    const present = vs.filter(Boolean)
    const validCount = present.filter(v => v.valid).length
    let unverified = false
    if (present.length === 0) { unverified = true; UNVERIFIED++ }
    else if (present.length === 1) { if (!present[0].valid) { DROPPED++; return } unverified = true; UNVERIFIED++ }
    else if (validCount < 2) { DROPPED++; return }
    kept.push({
      ...f,
      severity: medianSev([f.severity, rule && rule.severity, sceptic && sceptic.severity]),
      line: text && text.line > 0 ? text.line : f.line,
      page: text && text.page ? String(text.page) : (f.page || ''),
      fix: text && text.fix ? text.fix : f.fix,
      unverified,
    })
  })
  return kept
}

async function verify(label, scope, findings) {
  if (!findings.length) return []
  const res = await parallel(chunk(findings, VERIFY_BATCH).map((b, bi) => () => verifyBatch(label, scope, b, bi)))
  res.forEach((r, bi) => { if (r === null) FAILS.push(`verification batch ${label} ${bi + 1}: findings lost`) })
  return res.filter(Boolean).flat()
}

// ---------- phase 1: prepare ----------
phase('Prepare')
const unitsList = UNITS.map(u => `${u.id}: ${u.name} (${u.scope})`).join('\n')

const buildPrompt = `${BASE}

Task: prepare the shared working files for the review.
1. Create the directories ${OUT} and ${WORK}.
2. Build the thesis into an isolated directory, so it does not collide with the editor's auto-build:
   latexmk -xelatex -f -interaction=nonstopmode -outdir=${WORK}/build main-thesis.tex
   Run it with the Bash tool and the maximum timeout (600000 ms). If it has not finished by then, start the same command with run_in_background and wait for its completion notice; do not poll with sleep. Before any re-run, check with  tasklist | grep -i -E "xelatex|latexmk|perl|biber"  that no earlier run is still active, and wait until none is. Note the build time in minutes.
3. Save the text of every page with its printed page label:
   ${PY} -c "import fitz, json; d = fitz.open(r'${WORK}/build/main-thesis.pdf'); json.dump([{'label': p.get_label() or str(p.number + 1), 'text': p.get_text()} for p in d], open(r'${WORK}/thesis-pages.json', 'w', encoding='utf-8'), ensure_ascii=False)"
   If PyMuPDF (fitz) is missing, use "/c/Program Files/texlive/2026/bin/windows/pdftotext" -enc UTF-8 -layout, split at form feeds and use the physical page numbers as labels.
4. Write this helper to ${WORK}/findpage.py exactly as given:
${FINDPAGE}
   Test it: ${PY} ${WORK}/findpage.py ${WORK}/thesis-pages.json <three words from the abstract> must print a non-empty list of labels. If it does not, fix the page file and report the problem.
5. From ${WORK}/build/main-thesis.log list undefined references, undefined citations, multiply defined labels and overfull boxes above 5 pt. For each, give file and line in the sources (grep for the \\ref/\\cite key or use the lines the log gives), the page label if you can find it, and the source text at that line as quote. complete = true only if the last pass in the log has no "Label(s) may have changed", "Please (re)run Biber" or "There were undefined references" caused by a missing pass. Find the page label on which each chapter, the bibliography and each appendix start.
Return ok, complete, pdfPages, minutes, chapterStartPages and problems.`

const fbScoutPrompt = `${BASE}

Task: if the file ${FEEDBACK} does not exist, return exists = false and sections = []. Otherwise cut it into consecutive parts along its headings (lines starting with #), each part at most about 250 lines, without splitting an item; the parts must cover every line from the first item to the end, without gaps or overlaps. Return each part with its first heading as title and its line range (1-based, inclusive).`

const [build, fbScout] = await parallel([
  () => agent(buildPrompt, { label: 'build', phase: 'Prepare', schema: BUILD }),
  () => agent(fbScoutPrompt, { label: 'feedback-log:scout', phase: 'Prepare', schema: FB_SCOUT }),
])
let buildNote = ''
if (!build || !build.ok) { buildNote = 'The review build FAILED: work from the sources only; page labels are unavailable; do not report "??" or missing citations.'; FAILS.push('PDF build failed: no page numbers'); log('PDF build failed') }
else if (!build.complete) { buildNote = 'The review build is INCOMPLETE (a pass is missing): do not report "??" or missing citations; the build step lists them.'; log('PDF build incomplete') }
else { buildNote = 'The review build is complete; its undefined references and citations are reported by the build step, so do not report them again.' }
setRules(buildNote)

let FB = []
if (fbScout && fbScout.exists && fbScout.sections.length) {
  const parts = await parallel(fbScout.sections.map((s, k) => () => agent(
    `${BASE}

Task: parse lines ${s.startLine}-${s.endLine} ("${s.title}") of the feedback log ${FEEDBACK}. Read the log's header (its first 25 lines) for the status words and ID conventions. Return every feedback item in these lines:
- id: unique across the whole log. Keep the IDs of Parts 1 and 2 (supervisor reviews) exactly as written (SV-..., M1, E1, X1, ...). Prefix every item of the AI editorial review (Parts 3 and 4) with "AI-": the "Fix first" rows as AI-FF<n>, the structural, transition, repetition and pattern items as AI-S<n>, AI-T<n>, AI-R<n>, AI-P<n>, the sentence items as AI-<their id> (e.g. AI-1.1, AI-5d.4).
- logLine: the line of the item in the log; source: the review and its date; locationThen: its location at the time; feedback and resolution: each shortened to at most 300 characters without changing the meaning.
- status: Done -> fixed; Decided -> decided; Deferred -> deferred; Open or partly done -> open; superseded or anything else -> other.
- unit: the unit of the current thesis the item concerns (grep the current sources if its section has moved), one of:
${unitsList}
  or "none" if it concerns no single unit (e.g. an e-mail point about the whole thesis).`,
    { label: `feedback-log:parse:${k + 1}`, phase: 'Prepare', schema: FB_ITEMS })))
  parts.forEach((p, k) => { if (!p) FAILS.push(`feedback-log part ${k + 1} (lines ${fbScout.sections[k].startLine}-${fbScout.sections[k].endLine}) not parsed`) })
  FB = parts.filter(Boolean).flatMap(p => p.items)
  const perUnit = UNITS.map(u => `${u.id} ${FB.filter(i => i.unit === u.id).length}`).join(', ')
  log(`feedback log: ${FB.length} items (${FB.filter(i => i.status === 'fixed').length} done, ${FB.filter(i => i.status === 'decided').length} decided, ${FB.filter(i => i.status === 'deferred').length} deferred); per unit: ${perUnit}`)
} else {
  log('no feedback log found: the review uses the settled-decisions list only')
}

const FB_SUP = FB.filter(it => it.status !== 'other' && (SUP_ID.test(it.id) || /^AI-(FF|S|T|R|P)\d/.test(it.id)))
const supText = FB_SUP.length ? FB_SUP.map(it => fmtItem(it, 140)).join('\n') : '(none)'
function fbFor(unitId) {
  const its = FB.filter(it => it.unit === unitId && it.status !== 'other' && !FB_SUP.includes(it))
  return its.length ? its.map(it => fmtItem(it, 150)).join('\n') : '(none)'
}
const fbBlock = u => `Feedback-log items (use their IDs in "recurs"; items marked decided must not be raised again; a problem a deferred item covers is not a finding):
Supervisor items and the AI review's thesis-wide items:
${supText}
Items for this unit:
${fbFor(u.id)}`

// ---------- phase 2: review per unit ----------
function finderPrompt(u, p) {
  const notation = NOTATION_UNITS.includes(u.id) && (p.key === 'supervisor' || p.key === 'reviewer')
    ? '\nFirst read §2.5.2 (02-background.tex, \\subsection{Problem Statement} under \\section{Modelling Approach and Problem Statement}) and check every symbol in your unit against its notation.' : ''
  return `${BASE}\n\n${RULES}

Your role: reviewer "${p.name}" as described in section "The six reviewers" of ${PROMPT_FILE}. Your question: ${p.question} Set "persona" to "${p.name}".
Your unit: ${u.id} ${u.name}. Scope: ${u.scope}. Find the exact line range with grep before reading, then read the unit in full. Report findings only for lines inside your unit; you may read any other file to check them (grep earlier chapters before calling a term undefined). Where the unit includes figures (\\includegraphics), you may open the image files to judge them together with their captions.${notation}
${fbBlock(u)}

Report every problem you find from your perspective, following "Rules for findings": one finding per problem, the verbatim quote, the rule, a severity per the scale, the problem for your reader, a concrete fix. A mechanical issue that recurs within the unit is one finding, with the count in "problem" and up to five other locations in "alsoAt". Be thorough and do not stop at the first few problems, but report nothing you cannot tie to a rule or a clear problem for a reader.
Also return: verdict = 2-4 sentences on this unit from your perspective, including what works; reconsider = settled decisions you think hurt the thesis (usually empty).`
}

function termsPrompt(u) {
  return `${BASE}

Task: prerequisite inventory for unit ${u.id} ${u.name} (scope: ${u.scope}; find the line range with grep). List every technical, medical, imaging, mathematical or project-specific term, symbol and abbreviation in the printed text of this unit (skip comments): where it is first used in this unit (file, line), and where it is explained: "here, <file>:<line>" if explained in this unit at or before first use, "earlier, <file>:<line>" if explained in an earlier chapter (grep the earlier files to check), "later, <file>:<line>" if the explanation only comes after this first use, or "never". An acronym counts as explained only where it is spelled out. Also give the other names the same concept goes by in this unit (variants), e.g. "model / operator / architecture". Be complete; the ledger for the whole thesis is assembled from these lists.`
}

function completenessPrompt(u, listing) {
  return `${BASE}\n\n${RULES}

Task: completeness check for unit ${u.id} ${u.name} (scope: ${u.scope}). Six reviewers (supervisor, external reviewer, examiner, colleague, clinical reader, copy editor) and possibly an earlier completeness check reported the findings listed below. Read the unit yourself and report only problems they MISSED, not rephrasings of listed ones, from any of the six perspectives (set "persona" to the reviewer whose perspective it is), in the same format. Check in particular: each section's intro paragraph, thesis statement and conclusion (Guide §11.4); each results subsection's table or plot (§11.6); each caption (§5.2); each term's first use (§11.2); the LLM patterns (§11.5); tenses (§6); internal consistency of numbers inside the unit.
${fbBlock(u)}
verdict: one sentence on what the earlier reviewers covered least. reconsider: [].
Already reported (file:line - problem):
${listing}`
}

function mergePrompt(u, listing) {
  return `${BASE}

Task: find duplicates among the findings of unit ${u.id} ${u.name}. Below are all findings, indexed by i, each with its reviewers. Group findings that describe the same problem at the same place, or the same recurring pattern (which becomes one finding listing the other places). For each group return keep = the index of the clearest finding, drop = the other indices, alsoAt = locations of the dropped ones that the kept one does not list yet (or ""). Findings that are not duplicates are simply not mentioned; never group distinct problems, and do not drop anything for being minor.
Findings (JSON):
${listing}`
}

async function reviewUnit(u) {
  const calls = PERSONAS.map(p => () => agent(finderPrompt(u, p), { label: `${u.id}:${p.key}`, phase: 'Review', schema: FIND_RESULT }).then(r => (r ? { persona: p.name, ...r } : null)))
  calls.push(() => agent(termsPrompt(u), { label: `${u.id}:terms`, phase: 'Review', schema: TERMS }))
  const res = await parallel(calls)
  const personaRes = res.slice(0, PERSONAS.length)
  const termsRes = res[PERSONAS.length]
  const missing = PERSONAS.filter((p, i) => !personaRes[i]).map(p => p.name)
  if (missing.length) FAILS.push(`${u.id}: no result from ${missing.join(', ')}`)
  if (!termsRes) FAILS.push(`${u.id}: prerequisite inventory failed`)

  const all = []
  for (const r of personaRes.filter(Boolean)) for (const f of r.findings) all.push({ ...f, reviewers: [r.persona] })
  let completenessNote = ''
  for (let round = 1; round <= MAX_COMPLETENESS_ROUNDS; round++) {
    const listing = all.map(f => `${normFile(f.file)}:${f.line} - ${oneLine(f.problem, 120)}`).join('\n') || '(none)'
    const c = await agent(completenessPrompt(u, listing), { label: `${u.id}:completeness:${round}`, phase: 'Review', schema: FIND_RESULT })
    if (!c) { FAILS.push(`${u.id}: completeness round ${round} failed`); break }
    if (round === 1) completenessNote = c.verdict
    for (const f of c.findings) all.push({ ...f, reviewers: [personaOf(f, 'Completeness check')] })
    if (c.findings.length < 3) break
  }

  let merged = all
  if (all.length > 1) {
    const listing = JSON.stringify(all.map((f, i) => ({ i, file: normFile(f.file), line: f.line, reviewers: f.reviewers, rule: f.rule, quote: oneLine(f.quote, 160), problem: oneLine(f.problem, 220), alsoAt: f.alsoAt })))
    const m = await agent(mergePrompt(u, listing), { label: `${u.id}:merge`, phase: 'Review', schema: MERGE })
    if (!m) FAILS.push(`${u.id}: merge failed, duplicates may remain`)
    merged = applyMerges(all, (m && m.groups) || [], true).list
  }
  const verified = await verify(u.id, `${u.id} ${u.name}: ${u.scope}`, merged)
  log(`${u.id}: ${all.length} raw, ${merged.length} after merge, ${verified.length} verified`)
  return {
    unit: u,
    verdicts: personaRes.filter(Boolean).map(r => ({ persona: r.persona, verdict: r.verdict })),
    completenessNote,
    reconsider: personaRes.filter(Boolean).flatMap(r => r.reconsider || []),
    terms: (termsRes && termsRes.terms) || [],
    findings: verified.map(f => ({ ...f, unit: u.id })),
  }
}

// ---------- phase 3: whole-thesis passes ----------
const supBlock = `Feedback-log items (use their IDs in "recurs"; decided items must not be raised; a problem a deferred item covers is not a finding):\n${supText}`
const FLOW_STRETCHES = [
  { key: 'a', scope: 'the English abstract (00-abstract.tex), Chapter 1 (01-introduction.tex) and Chapter 2 (02-background.tex), up to the opening of Chapter 3 (03-data.tex)' },
  { key: 'b', scope: 'from the last section of Chapter 2 (02-background.tex, \\section{Modelling Approach and Problem Statement}) through Chapter 3 (03-data.tex) and Chapter 4 (04-method.tex), up to the opening of Chapter 5 (05-experiments.tex)' },
  { key: 'c', scope: 'from the last section of Chapter 4 (04-method.tex) through Chapter 5 (05-experiments.tex), Chapter 6 (06-discussion.tex) and Chapter 7 (07-conclusion.tex)' },
  { key: 'd', scope: 'the appendices (91-appendix.tex): each appendix and its link to the place in the main text that points to it' },
]
const flowPrompt = st => `Task: FLOW of one stretch of the thesis: ${st.scope}. Read this stretch front to back in order, as a reader would, without skimming (skip comment lines). Check: (1) every chapter and section opening connects to what came before and says what follows; every closing hands over to the next part; (2) within each section the paragraphs build its argument in a sensible order (Guide §2.1, §5); (3) the link from paragraph to paragraph (§3): no abrupt jump, no topic introduced and then dropped, no paragraph that belongs elsewhere; (4) forward references that ask the reader to accept something not yet explained, and backward references that repeat instead of pointing; (5) places where a reader loses the thread or cannot tell why the passage is there; (6) the hour-glass shape of the thesis (THESIS_STRUCTURE.md, Narrative Constraint) as far as this stretch shows it. Do not report single-sentence wording, mechanics or terminology (other passes cover them). Report each problem at the place to change: for a transition, at the opening of the later part, with the earlier place in alsoAt; the fix is a concrete bridge sentence or a concrete move. Set "persona" to "Colleague" or "Supervisor". verdict: 3-5 sentences on the flow of this stretch, naming its weakest transition.`
const numbersPrompt = part => `Task: internal consistency of numbers, part: ${part}. Collect every quantitative result stated in this part (scores, differences, counts of folds and eyes, parameter counts, ratios, cohort statistics). For each, find all other places in the thesis where it appears: grep -F the exact printed form (e.g. 0.064) with --include="*.tex" and skip lines that start with %, including tables, captions and appendices. Check that value, rounding and the stated comparison (which arm minus which, which seed, which measure) agree. Report every mismatch as a finding, located in this part, with the other place in alsoAt: S1 for a different value or comparison, S3 for inconsistent rounding. Do not check numbers against run records or sources. Set "persona" to "External reviewer". verdict: "<checked> numbers checked, <n> disagree".`
const MACRO = [
  { key: 'structure', reviewers: ['Examiner', 'Supervisor'], prompt: () => `Task: whole-thesis structure and argument (examiner and supervisor perspectives; set "persona" to "Examiner" or "Supervisor"). Read in full the abstract (English and German), Chapter 1 and Chapter 7; read the opening and the closing paragraph of every chapter and section; read THESIS_STRUCTURE.md (Framing and the revisions of 2026-09-25, 2026-10-12 and 2026-10-18; the agreed structure and page budgets, not ground truth for facts). Check: the chapter and section order against THESIS_STRUCTURE.md and Guide §11.3; both sub-questions stated in Chapter 1 and answered explicitly in Chapter 7; the abstract, the contributions (§1.3), the results summary (§5.9), the interpretation (§6.1) and the conclusion say the same thing; chapter lengths against the page budgets (chapter start pages: ${JSON.stringify((build && build.chapterStartPages) || [])}); every figure, table and appendix referred to in the text; nothing called a test-set result; English abstract and Kurzfassung agree in content. Report each problem at the location you would change (for a mismatch, the other place in alsoAt). verdict: 4-6 sentences on the thesis as a whole, ending with the main risk to the grade.` },
  { key: 'facts', reviewers: ['External reviewer', 'Clinical reader'], prompt: () => `Task: consistency of facts and definitions across the whole thesis (external reviewer and clinical reader perspectives; set "persona" accordingly). Collect every definition (change-region Dice, growth-region Dice, the anchor, the late-epoch mean, canonical model, persistence, arm, fold, operator, framework) and every factual claim about the data and the setting (cohort size and its relation to Mai et al. 2024, mask provenance, device, pixel spacing, the crop and its census, visit intervals, the layer boundaries) at all places where they are stated, in every chapter, caption and appendix. Report each pair of statements that disagree or could be read as disagreeing, located at the later place, with the other in alsoAt (S1 for a contradiction, S2 for wording that a reader could take as one). Not numbers in general (another pass checks those), only facts and definitions. verdict: what was checked and how consistent it is.` },
  { key: 'numbers-a', reviewers: ['External reviewer', 'Examiner'], prompt: () => numbersPrompt('the English abstract, the German Kurzfassung (00-abstract.tex) and Chapter 1') },
  { key: 'numbers-b', reviewers: ['External reviewer', 'Examiner'], prompt: () => numbersPrompt('§5.9 Summary and the result statements of §5.2 (05-experiments.tex)') },
  { key: 'numbers-c', reviewers: ['External reviewer', 'Examiner'], prompt: () => numbersPrompt('Chapter 6 (06-discussion.tex)') },
  { key: 'numbers-d', reviewers: ['External reviewer', 'Examiner'], prompt: () => numbersPrompt('Chapter 7 (07-conclusion.tex)') },
  { key: 'format-text', reviewers: ['Copy editor', 'Examiner'], schema: FORMAT_RESULT, prompt: () => `Task: consistency of format ACROSS chapters (the per-unit reviewers only see one unit). Compare all chapters, the front matter and the appendices, with grep and by reading the chapter openings and closings, for these aspects: (1) chapter openings (does every chapter open with the same kind of paragraph, e.g. purpose plus a map of its sections?) and closings (summary or bridge to the next chapter: the same pattern everywhere?); (2) section intros and conclusions (Guide §11.4) as a pattern across chapters, not per section; (3) headings: capitalisation style, length, depth of nesting, numbering, no question marks, run-in \\paragraph headings; (4) cross-references: Section~\\ref vs \\S\\ref vs "Sec.", Chapter/Figure/Table/Equation vs "Fig."/"Tab."/"Eq.", non-breaking spaces before \\ref and \\cite, capitalised "Table 5.1"; (5) citations: \\citet/\\citep use (CLAUDE.md), placement before or after punctuation; (6) numbers and units: decimal places for the same kind of quantity (e.g. Dice to three decimals), thousands separators (67,147), ± and spacing, percentages, µm vs mm, \\times, en-dash ranges, numerals vs words for small numbers; (7) quotation marks, emphasis (\\emph vs \\textbf), lists (itemize vs enumerate, punctuation at item ends), abbreviations (defined once, then always used), British spelling, hyphenation of compounds. For each aspect return the convention (the form used in most places, unless a rule in WRITING_GUIDE.md or CLAUDE.md requires another) and the number of deviations. Report each group of deviations from one convention as ONE finding at its first location, with ALL other locations in "alsoAt" (file:line list). Set "persona" to "Copy editor" or "Examiner". verdict: 2-3 sentences on how uniform the format is.` },
  { key: 'format-floats', reviewers: ['Copy editor', 'Supervisor'], schema: FORMAT_RESULT, prompt: () => `Task: consistency of figures, tables and equations ACROSS the whole thesis. Read every \\begin{figure}, \\begin{table} and displayed equation in all chapter files, and look at the rendered pages of ${WORK}/build/main-thesis.pdf where the look matters (you may open PDF pages with the Read tool). Aspects: (1) captions: same structure everywhere (a short title, then the details needed to read the float, Guide §5.2), self-contained (CLAUDE.md), ending punctuation, what "±" means stated where it is used ("mean ± sd over the five folds"), caption length; (2) caption position (table captions above, figure captions below, or whatever the majority does) and label placement; (3) tables: rule style (booktabs or not), alignment of numeric columns, decimal places, units in the header, bold or marking of best values, notes and footnotes, width within the text block; (4) figures: consistent sizes for figures of the same kind, fonts and colours following style/ (palette of style/README.md; one colour per arm everywhere), panel labels (a)/(b) and how captions refer to them; (5) every float referred to in the text before or near where it appears, and in the order of numbering; (6) equations: punctuation after displayed equations, numbering only where referred to later (CLAUDE.md), notation consistent with §2.5.2; (7) placeholder or disabled figures still printed. For each aspect return the convention and the number of deviations. Report each group of deviations as ONE finding at its first location, with ALL other locations in "alsoAt". Set "persona" to "Copy editor" or "Supervisor". verdict: 2-3 sentences on how uniform the floats are.` },
  ...FLOW_STRETCHES.map(st => ({ key: `flow-${st.key}`, reviewers: ['Colleague', 'Supervisor'], prompt: () => flowPrompt(st) })),
  { key: 'repetition-content', reviewers: ['Supervisor', 'Examiner'], schema: REPEAT_RESULT, prompt: () => `Task: repetition of CONTENT across the whole thesis. Find every fact, caveat, argument, definition, explanation of a method or result summary that is stated in full in more than one place (typical candidates: the crop census, the cohort description, the caveats of the comparison with Mai et al. 2024, the continuous-time caution, the reach argument, the research question and its answer, descriptions of the framework). The author's rule: state a thing in full once, elsewhere a short pointer. Summaries the structure requires are allowed (the abstract, §5.9 Summary, Chapter 7, and the short purpose statement at the start of a results section, Guide §11.4), but they must stay shorter than the original and must not repeat its detail; a number quoted again in such a summary is not a repetition. Method: collect candidate topics from the chapter openings and closings and by grepping key numbers and terms; then read every occurrence in context (skip comment lines). For each repeated topic return a "repeats" entry (topic, every place, where it should be stated in full) and ONE finding located at the first redundant place, with the other redundant places in alsoAt; rule "Guide §4" or the feedback-log item that set the rule; the fix names the pointer that replaces the copy. Set "persona" to "Supervisor" or "Examiner". verdict: 2-3 sentences on how much the thesis repeats itself.` },
  { key: 'repetition-wording', reviewers: ['Copy editor'], prompt: () => `Task: repetition of WORDING across the whole thesis. Write and run a short script (${PY}) over the chapter files 00-abstract.tex (English part), 01-introduction.tex ... 07-conclusion.tex and 91-appendix.tex that drops comment lines and \iffalse blocks, strips LaTeX commands, math and citations, normalises case and whitespace, and lists (a) every sequence of 7 or more words that occurs in more than one place, and (b) every phrase of 3-5 words, other than technical terms and ordinary function-word combinations, that occurs 4 or more times. Read each hit in context. Report as findings those that read as repetition: the same sentence or half-sentence reused, a stock phrase that recurs ("on equal terms" and the like), the same sentence opening used again and again. Group each phrase into ONE finding at its first occurrence with ALL other places in alsoAt (rule Guide §4, or Guide §11.5 for LLM-like stock phrases). Skip defined terms, headings, labels and captions that repeat a table title, and phrases fixed by the terminology rules. Set "persona" to "Copy editor". verdict: the number of repeated phrases found and reported.` },
  { key: 'mechanics', reviewers: ['Copy editor'], prompt: () => `Task: thesis-wide sweep for recurring mechanical issues (Guide §1, §2.7, §3, §4, §6, §11.5) over the printed text of all chapter files, with grep (skip comment lines). For each pattern that occurs more than twice in the thesis, report ONE cross-cutting finding: the count in "problem", the first occurrence as file, line and quote, and ALL other locations in "alsoAt" as a list of file:line without quotes. Patterns at least: sentences starting with And/But/So/Because; contractions; get; vague quantities; prove/disprove for results; "it can be seen", "it is shown that"; "the fact that"; "in order to"; e.g./i.e. outside brackets; em-dash asides (---); "data is"; sentence-final too/also/though/yet; emphatic adverbs (crucially, fundamentally, entirely, clearly, simply, actually, naturally, notably); the LLM patterns of Guide §11.5 ("not X but Y", "X, not Y", "What ... is that ...", "is not what decides"); American spellings (-ize, -yze, color, behavior, modeling); mixed µm/mm for the same kind of quantity; inconsistent hyphenation of one compound (e.g. change-region / change region); \\cite instead of \\citet/\\citep. Set "persona" to "Copy editor". verdict: the counts in one or two sentences.` },
]

async function runMacro(m) {
  const r = await agent(`${BASE}\n\n${RULES}\n\n${supBlock}\n\n${m.prompt()}`, { label: `whole:${m.key}`, phase: 'Whole thesis', schema: m.schema || FIND_RESULT })
  if (!r) { FAILS.push(`whole-thesis pass "${m.key}" failed`); return null }
  const fs = r.findings.map(f => ({ ...f, reviewers: [personaOf(f, m.reviewers[0])] }))
  const v = await verify(`whole:${m.key}`, 'the whole thesis', fs)
  return { key: m.key, verdict: r.verdict, reconsider: r.reconsider || [], conventions: r.conventions || [], repeats: r.repeats || [], findings: v.map(f => ({ ...f, unit: 'whole' })) }
}

const REG_ITEMS = FB.filter(it => it.status === 'fixed')
const regChunks = chunk(REG_ITEMS, REGR_BATCH)

async function runRegression(items, i) {
  const r = await agent(`${BASE}\n\n${RULES}

Task: feedback-log regression check, batch ${i + 1}. Each item below was resolved by a change to the text (status Done in ${FEEDBACK}; its full text is at the given log line; AI- IDs appear in the log without the prefix). For each item, find the place in the current text it concerns and decide: holds (the resolution is still in the text), regressed (the text again shows the original problem, or the change was undone), no longer applies (the passage was removed or rewritten so the point is moot), unclear. Return one check per item, with the ID exactly as given. For every regressed item also return a finding at its current location: rule "Feedback log <ID>", recurs "<ID>" (exactly as given), severity what the original problem deserves today, persona the reviewer whose perspective it is.
Items (ID [status] log line: feedback -> resolution):
${items.map(it => `${it.id} [${it.status}] line ${it.logLine}: ${oneLine(it.feedback, 220)} -> ${oneLine(it.resolution, 180)}`).join('\n')}`, { label: `feedback:regressions:${i + 1}`, phase: 'Whole thesis', schema: REGR })
  if (!r) { FAILS.push(`regression batch ${i + 1}: ${items.length} items unchecked`); return { checks: items.map(it => ({ id: it.id, status: 'unclear', note: 'batch failed' })), findings: [] } }
  const returned = new Set(r.checks.map(c => c.id))
  const checks = [...r.checks, ...items.filter(it => !returned.has(it.id)).map(it => ({ id: it.id, status: 'unclear', note: 'not returned by the checking agent' }))]
  return { checks, findings: r.findings.map(f => ({ ...f, reviewers: [personaOf(f, 'Feedback-log check')], unit: 'feedback', regressionOf: tokens(f.recurs)[0] || '' })) }
}

phase('Review')
log(`${UNITS.length} units x ${PERSONAS.length} reviewers; ${MACRO.length} whole-thesis passes; ${REG_ITEMS.length} done feedback items in ${regChunks.length} batches`)
const [unitRes, macroRes, regrRes] = await parallel([
  () => pipeline(UNITS, u => reviewUnit(u)),
  () => pipeline(MACRO, m => runMacro(m)),
  () => pipeline(regChunks, (c, _, i) => runRegression(c, i)),
])
const unitsOk = (unitRes || []).filter(Boolean)
const macroOk = (macroRes || []).filter(Boolean)
const regrOk = (regrRes || []).filter(Boolean)
const failedUnits = UNITS.filter(u => !unitsOk.some(r => r.unit.id === u.id)).map(u => `${u.id} ${u.name}`)
failedUnits.forEach(u => FAILS.push(`unit ${u} not reviewed`))
if (!unitRes) FAILS.push('the unit pipeline failed as a whole')
if (!macroRes) FAILS.push('the whole-thesis passes failed as a whole')
if (!regrRes && regChunks.length) FAILS.push('the regression check failed as a whole')

phase('Whole thesis')
const regrFindings = (await verify('feedback', 'the whole thesis', regrOk.flatMap(r => r.findings))).map(f => ({ ...f, unit: 'feedback' }))

// prerequisite ledger: deduplicate in code
const prefixOf = s => { const m = String(s || '').trim().toLowerCase().match(/^(here|earlier|later|never)/); return m ? m[1] : 'never' }
const locIn = s => { const m = String(s || '').match(/([A-Za-z0-9_.-]+\.(?:tex|bib))\s*:\s*(\d+)/); return m ? { file: m[1], line: +m[2] } : null }
const termMap = new Map()
for (const r of unitsOk) for (const t of r.terms) {
  const key = String(t.term || '').toLowerCase().trim()
  if (!key) continue
  const first = { file: normFile(t.file), line: t.firstLine }
  const pre = prefixOf(t.explainedAt)
  const exp = pre === 'never' ? null : (locIn(t.explainedAt) || (pre === 'here' ? first : null))
  const e = termMap.get(key) || { term: t.term, kind: t.kind, first, explained: null, variants: new Set(), units: new Set() }
  if (posKey(first.file, first.line) < posKey(e.first.file, e.first.line)) e.first = first
  if (exp && (!e.explained || posKey(exp.file, exp.line) < posKey(e.explained.file, e.explained.line))) e.explained = exp
  for (const v of t.variants || []) e.variants.add(v)
  e.units.add(r.unit.id)
  termMap.set(key, e)
}
const LEDGER_ROWS = [...termMap.values()].map(e => ({
  term: e.term, kind: e.kind, firstUse: `${e.first.file}:${e.first.line}`,
  explained: e.explained ? `${e.explained.file}:${e.explained.line}` : 'never',
  status: !e.explained ? 'missing' : (posKey(e.explained.file, e.explained.line) <= posKey(e.first.file, e.first.line) + 2 ? 'ok' : 'late'),
  variants: [...e.variants],
})).sort((a, b) => { const x = locIn(a.firstUse), y = locIn(b.firstUse); return posKey(x.file, x.line) - posKey(y.file, y.line) })
const toAdjudicate = LEDGER_ROWS.filter(r => r.status !== 'ok' || r.kind === 'medical' || r.kind === 'imaging')
const variantRows = LEDGER_ROWS.filter(r => r.variants.length)
let led = null
if (LEDGER_ROWS.length) {
  led = await agent(`${BASE}\n\n${RULES}\n\n${supBlock}

Task: prerequisite ledger, terminology and acronym list for the whole thesis. The script has merged the per-unit inventories. Below are (a) the terms whose status is late or missing, plus every medical and imaging term, and (b) every term that goes by more than one name. Audience (Guide §11.2): mathematics and ML may be assumed (PDE, boundary value problem, neural network, CNN, gradient); the medical and imaging part may not.
1. Spot-check doubtful entries of (a) in the files and return corrections (term, status, explained as file:line or "never") for entries that are wrong.
2. Terminology table: concepts that go by more than one name, with the names, where each is used, and a proposed single name (CLAUDE.md Terminology first).
3. Findings: one per late or missing term a reader needs (rule Guide §11.2; S1 if the argument depends on it, S2 for a medical or imaging term, S3 otherwise; persona "Colleague"), one per terminology drift that could confuse (rule Guide §4), and, after comparing every abbreviation used in the thesis with the entries of acronyms.tex, one per abbreviation used but missing from the list and one per listed abbreviation never used (located in acronyms.tex; persona "Examiner"). Each finding at the place to change.
(a) term [kind] | first use | explained | status:
${toAdjudicate.map(r => `${r.term} [${r.kind}] | ${r.firstUse} | ${r.explained} | ${r.status}`).join('\n') || '(none)'}
(b) term | names:
${variantRows.map(r => `${r.term} | ${r.variants.join(' / ')}`).join('\n') || '(none)'}`, { label: 'ledger', phase: 'Whole thesis', schema: LEDGER })
  if (!led) FAILS.push('ledger step failed: no terminology table, no ledger findings')
}
if (led) for (const c of led.corrections) {
  const row = LEDGER_ROWS.find(r => r.term.toLowerCase() === String(c.term).toLowerCase())
  if (row) { row.status = c.status; row.explained = c.explained }
}
const ledgerFindings = led ? (await verify('ledger', 'the whole thesis', led.findings.map(f => ({ ...f, reviewers: [personaOf(f, 'Colleague')] })))).map(f => ({ ...f, unit: 'ledger' })) : []

// build-log problems of a complete build become findings directly
const buildFindings = (build && build.ok && build.complete ? build.problems : [])
  .filter(p => p.kind === 'undefined reference' || p.kind === 'undefined citation' || p.kind === 'multiply defined label')
  .map(p => ({ file: normFile(p.file), line: p.line, section: '', quote: p.quote, rule: `judgement: ${p.kind} in the build log`, severity: 'S1', problem: `${p.kind}: ${p.detail}`, fix: 'Correct the key or add the missing label or bibliography entry.', recurs: '', alsoAt: '', persona: 'Examiner', reviewers: ['Build log'], page: p.page || '', unverified: false, unit: 'build' }))

// ---------- phase 5: synthesize ----------
phase('Synthesize')
let ALL = []
for (const r of unitsOk) ALL.push(...r.findings)
for (const r of macroOk) ALL.push(...r.findings)
ALL.push(...regrFindings, ...ledgerFindings, ...buildFindings)
ALL = ALL.map((f, i) => ({ ...f, severity: sevOf(f.severity), file: normFile(f.file), tid: `T${i + 1}` }))
log(`${ALL.length} verified findings before calibration; ${DROPPED} dropped by verification; ${UNVERIFIED} kept with incomplete verification`)
const tidIndex = new Map(ALL.map((f, i) => [f.tid, i]))
const calLine = f => `${f.tid} | ${f.file}:${f.line} | ${f.severity} | ${oneLine(f.rule, 30)} | ${oneLine(f.problem, 110)}`
const calHead = `${BASE}\n\nRead the sections "Severity" and "Settled decisions: do not raise these again" of ${PROMPT_FILE}.`

// (1) severity calibration and merges, per chapter group when there are many findings
const groupsToCal = ALL.length > CAL_SPLIT ? CAL_GROUPS.map(g => ALL.filter(f => g.includes(chapterOf(f.file, f.line)))) : [ALL]
const calRes = await parallel(groupsToCal.filter(g => g.length).map((g, k) => () => agent(`${calHead}

Task: calibrate the verified findings below (id | location | severity | rule | problem). Return (1) changes: findings whose severity should change so that the same kind of problem has the same level everywhere, with a short reason (only the changes); (2) merges: findings that describe the same problem (keep = the one with more locations or the clearer text, drop = the others). Open a source file only when a line is ambiguous.
${g.map(calLine).join('\n')}`, { label: `calibrate:${k + 1}`, phase: 'Synthesize', schema: CAL_GROUP })))
calRes.forEach((r, k) => { if (!r) FAILS.push(`calibration group ${k + 1} failed: its severities are uncalibrated`) })
const CHANGES = calRes.filter(Boolean).flatMap(r => r.changes)
const MERGES = calRes.filter(Boolean).flatMap(r => r.merges)

// (2) themes, fix-first and cross-group merges over all findings
const reconsiderNotes = [...unitsOk.flatMap(r => r.reconsider), ...macroOk.flatMap(r => r.reconsider)].filter(Boolean)
const themes = await agent(`${calHead}

Task: overview of the verified findings of the whole review (one short line each: id | location | severity | rule | problem). Return: (1) merges: findings in different chapters or passes that describe the same problem (e.g. a thesis-wide pattern finding and per-unit findings of the same pattern: keep the thesis-wide one); (2) crossCutting: at most 12 themes (structure, terminology, a recurring language pattern, consistency, ...), each with a title, one sentence and its ids; (3) fixFirst: the 15 most important ids, most important first; (4) reconsider: from the reviewers' notes on settled decisions below, the ones worth listing for the author, each with one sentence.
Findings:
${ALL.map(f => `${f.tid} | ${f.file}:${f.line} | ${f.severity} | ${oneLine(f.rule, 25)} | ${oneLine(f.problem, 80)}`).join('\n')}
Reviewers' notes on settled decisions:
${reconsiderNotes.join('\n') || '(none)'}`, { label: 'themes', phase: 'Synthesize', schema: THEMES })
if (!themes) FAILS.push('themes step failed: no fix-first list and no cross-cutting themes')
const TH = themes || { merges: [], crossCutting: [], fixFirst: [], reconsider: [] }

const groups = [...MERGES, ...TH.merges].map(g => ({ keep: tidIndex.get(g.keep), drop: (g.drop || []).map(t => tidIndex.get(t)).filter(x => x !== undefined), alsoAt: '' })).filter(g => g.keep !== undefined)
const merged = applyMerges(ALL, groups, false)
const rootTid = t => { const i = tidIndex.get(t); return i === undefined ? null : ALL[merged.root(i)].tid }
let FINAL = merged.list
const finalByTid = new Map(FINAL.map(f => [f.tid, f]))
for (const ch of CHANGES) { const t = rootTid(ch.tid); const f = t && finalByTid.get(t); if (f) f.severity = sevOf(ch.severity) }
for (const f of FINAL) {  // supervisor repeats: one level up, at most to S2
  if (tokens(f.recurs).some(id => SUP_ID.test(id)) && SEV_N[f.severity] >= 3) { f.severity = N_SEV[SEV_N[f.severity] - 1]; f.raised = true }
}
FINAL.sort((a, b) => posKey(a.file, a.line) - posKey(b.file, b.line))
FINAL = FINAL.map((f, i) => ({ ...f, id: `R-${String(i + 1).padStart(4, '0')}` }))
const ridOfTid = new Map(FINAL.map(f => [f.tid, f.id]))
const rid = t => { const r = rootTid(t); return (r && ridOfTid.get(r)) || null }
const byId = new Map(FINAL.map(f => [f.id, f]))
const N = FINAL.length

// ---------- render ----------
const loc = f => `${f.file}:${f.line}${f.page ? ` (p. ${f.page})` : ''}`
const sevCount = { S1: 0, S2: 0, S3: 0, S4: 0 }
const byCh = {}
for (const c of CHAPTERS) byCh[c] = { S1: 0, S2: 0, S3: 0, S4: 0 }
for (const f of FINAL) { sevCount[f.severity]++; byCh[chapterOf(f.file, f.line)][f.severity]++ }
const countsTable = ['| Part | S1 | S2 | S3 | S4 | Total |', '|---|---|---|---|---|---|']
  .concat(CHAPTERS.filter(c => Object.values(byCh[c]).some(x => x)).map(c => `| ${c} | ${byCh[c].S1} | ${byCh[c].S2} | ${byCh[c].S3} | ${byCh[c].S4} | ${byCh[c].S1 + byCh[c].S2 + byCh[c].S3 + byCh[c].S4} |`))
  .concat([`| **All** | ${sevCount.S1} | ${sevCount.S2} | ${sevCount.S3} | ${sevCount.S4} | ${N} |`]).join('\n')

const block = f => [
  `### ${f.id} · ${f.severity} · ${oneLine(f.section, 80) || chapterOf(f.file, f.line)} — ${loc(f)}`,
  '',
  '~~~text',
  ...String(f.quote || '').replace(/~~~/g, '~ ~ ~').trim().split('\n').slice(0, 4),
  '~~~',
  '',
  `- **Reviewers:** ${(f.reviewers || []).join(', ')}`,
  `- **Rule:** ${oneLine(f.rule, 300)}`,
  `- **Problem:** ${oneLine(f.problem, 3000)}`,
  `- **Fix:** ${oneLine(f.fix, 3000)}`,
  ...(f.alsoAt ? [`- **Also at:** ${oneLine(f.alsoAt, 3000)}`] : []),
  ...(f.recurs ? [`- **Recurs:** ${f.recurs}${f.raised ? ' (supervisor repeat: raised one level)' : ''}`] : []),
  ...(f.unverified ? ['- **Note:** verification incomplete (a verifier failed)'] : []),
  '- **Status:** open',
].join('\n')

const findingsText = [
  '# Full review of the thesis: findings',
  '',
  `Review of ${DATE}. ${N} findings in thesis order (S1 ${sevCount.S1} · S2 ${sevCount.S2} · S3 ${sevCount.S3} · S4 ${sevCount.S4}). "p." is the printed page number in review-build.pdf. Summary: [00-summary.md](00-summary.md).`,
  '',
  '## Index',
  '',
  '| ID | Location | Sev. | Reviewers | Finding |',
  '|---|---|---|---|---|',
  ...FINAL.map(f => `| ${f.id} | ${cell(loc(f))} | ${f.severity} | ${cell((f.reviewers || []).join(', '))} | ${cell(oneLine(f.problem, 110))} |`),
  '',
  '## Findings',
  '',
  FINAL.map(block).join('\n\n'),
  '',
].join('\n')

// reviewer paragraphs (the only prose the summary needs from an agent)
const perPersona = PERSONAS.map(p => {
  const mine = FINAL.filter(f => (f.reviewers || []).includes(p.name)).sort((a, b) => SEV_N[a.severity] - SEV_N[b.severity] || posKey(a.file, a.line) - posKey(b.file, b.line))
  return {
    reviewer: p.name,
    unitVerdicts: unitsOk.map(r => { const v = r.verdicts.find(x => x.persona === p.name); return v ? `${r.unit.id} ${r.unit.name}: ${v.verdict}` : null }).filter(Boolean),
    topFindings: mine.slice(0, 30).map(f => `${f.id} ${f.severity} ${oneLine(f.section, 40)}: ${oneLine(f.problem, 120)}`),
  }
})
const structureVerdict = (macroOk.find(m => m.key === 'structure') || {}).verdict || ''
const paras = await agent(`${BASE}

Task: write one paragraph per reviewer for a review summary (80-150 words each), in plain, factual English that follows WRITING_GUIDE.md (no LLM patterns, Guide §11.5). Each paragraph: the reviewer's overall verdict on the thesis, synthesised from its unit verdicts, and the three findings (by ID, from its topFindings) that this reviewer would fix first. The examiner's paragraph ends with the main risk to the grade, using the whole-thesis verdict. Return them in the given reviewer order.
Whole-thesis verdict: ${structureVerdict}
Data (JSON):
${JSON.stringify(perPersona)}`, { label: 'summary:paragraphs', phase: 'Synthesize', schema: PARAS })
if (!paras) FAILS.push('summary paragraphs failed: section 1 lists the unit verdicts instead')

const checks = regrOk.flatMap(r => r.checks)
const tally = ['holds', 'regressed', 'no longer applies', 'unclear'].map(s => `${s} ${checks.filter(c => c.status === s).length}`).join(' · ')
const regressedRows = checks.filter(c => c.status === 'regressed').map(c => {
  const ids = FINAL.filter(f => f.regressionOf === c.id).map(f => f.id)
  return `| ${cell(c.id)} | ${ids.join(', ') || 'regression claimed, finding failed verification'} | ${cell(oneLine(c.note, 160))} |`
})
const deferred = FB.filter(it => it.status === 'deferred')
const ledgerShown = LEDGER_ROWS.filter(r => r.status !== 'ok' || r.kind === 'medical' || r.kind === 'imaging')
const coverage = {
  failures: FAILS,
  droppedByVerification: DROPPED,
  keptWithIncompleteVerification: UNVERIFIED,
  units: `${unitsOk.length} of ${UNITS.length} reviewed`,
  wholeThesisPasses: `${macroOk.length} of ${MACRO.length}`,
  feedbackItems: `${FB.length} parsed, ${REG_ITEMS.length} done items checked`,
}
const summaryText = [
  '# Full review of the thesis: summary',
  '',
  `Review of ${DATE}. ${N} findings (S1 ${sevCount.S1} · S2 ${sevCount.S2} · S3 ${sevCount.S3} · S4 ${sevCount.S4}); the full list is in [01-findings.md](01-findings.md). Page numbers refer to review-build.pdf (build ${build && build.ok ? (build.complete ? 'complete' : 'incomplete') : 'failed'}).`,
  '',
  '## 1. The six reviewers',
  '',
  ...(paras ? paras.paragraphs.map(p => `**${p.reviewer}.** ${oneLine(p.text, 2000)}\n`) : perPersona.map(p => `**${p.reviewer}.** ${p.unitVerdicts.map(v => oneLine(v, 300)).join(' ')}\n`)),
  '**Whole-thesis passes.**',
  ...macroOk.map(m => `- ${m.key}: ${oneLine(m.verdict, 600)}`),
  '',
  '## 2. Counts',
  '',
  countsTable,
  '',
  '## 3. Fix first',
  '',
  ...[...new Set((TH.fixFirst || []).map(rid).filter(Boolean))].map((id, k) => { const f = byId.get(id); return `${k + 1}. ${id} · ${f.severity} · ${loc(f)}: ${oneLine(f.problem, 160)}` }),
  '',
  '## 4. Cross-cutting issues',
  '',
  ...(TH.crossCutting || []).map(t => `- **${oneLine(t.title, 80)}.** ${oneLine(t.description, 300)} (${[...new Set((t.tids || []).map(rid).filter(Boolean))].join(', ')})`),
  '',
  '## 5. Prerequisite ledger',
  '',
  `${LEDGER_ROWS.length} terms in the inventories: ${LEDGER_ROWS.filter(r => r.status === 'ok').length} ok, ${LEDGER_ROWS.filter(r => r.status === 'late').length} late, ${LEDGER_ROWS.filter(r => r.status === 'missing').length} missing. Listed: every medical and imaging term and every term explained late or never.`,
  '',
  '| Term | Kind | First use | Explained | Status |',
  '|---|---|---|---|---|',
  ...ledgerShown.map(r => `| ${cell(r.term)} | ${r.kind} | ${r.firstUse} | ${r.explained} | ${r.status} |`),
  '',
  '## 6. Terminology',
  '',
  '| Concept | Names used | Where | Proposed |',
  '|---|---|---|---|',
  ...((led && led.terminology) || []).map(t => `| ${cell(t.concept)} | ${cell(t.names.join(' / '))} | ${cell(oneLine(t.locations, 200))} | ${cell(t.proposed)} |`),
  '',
  '## 7. Format conventions',
  '',
  'The conventions the thesis follows in most places (or that the rules require), and how often a chapter departs from them. Each group of deviations is one finding in 01-findings.md.',
  '',
  '| Aspect | Convention | Deviations | Where |',
  '|---|---|---|---|',
  ...macroOk.filter(m => m.key.startsWith('format')).flatMap(m => m.conventions).map(c => `| ${cell(oneLine(c.aspect, 80))} | ${cell(oneLine(c.convention, 200))} | ${c.deviations} | ${cell(oneLine(c.where, 200))} |`),
  ...(macroOk.some(m => m.key.startsWith('format')) ? [] : ['| (the format passes failed) | | | |']),
  '',
  '## 8. Repetition across chapters',
  '',
  'Topics stated in full in more than one place, and where they should be stated in full (elsewhere a short pointer). Each is one finding in 01-findings.md.',
  '',
  '| Topic | Stated at | State in full at |',
  '|---|---|---|',
  ...macroOk.filter(m => m.key === 'repetition-content').flatMap(m => m.repeats).map(r => `| ${cell(oneLine(r.topic, 100))} | ${cell(oneLine(r.places, 300))} | ${cell(oneLine(r.keep, 80))} |`),
  ...(macroOk.some(m => m.key === 'repetition-content') ? [] : ['| (the repetition pass failed) | | |']),
  '',
  '## 9. Build log',
  '',
  build ? `PDF ${build.ok ? 'built' : 'not built'}, ${build.complete ? 'complete' : 'incomplete'}, ${build.pdfPages} pages, ${build.minutes} min.` : 'The build step failed.',
  '',
  '| Kind | Location | Page | Detail |',
  '|---|---|---|---|',
  ...((build && build.problems) || []).map(p => `| ${p.kind} | ${normFile(p.file)}:${p.line} | ${cell(p.page)} | ${cell(oneLine(p.detail, 200))} |`),
  '',
  '## 10. Feedback log check',
  '',
  `${FEEDBACK}: ${FB.length} items parsed; ${REG_ITEMS.length} done items checked: ${tally}.`,
  '',
  '| Log ID | Finding | Note |',
  '|---|---|---|',
  ...regressedRows,
  '',
  'Resolution could not be confirmed (unclear):',
  '',
  ...checks.filter(c => c.status === 'unclear').map(c => `- ${c.id}: ${oneLine(c.note, 200)}`),
  '',
  `No longer applies (passage removed or rewritten): ${checks.filter(c => c.status === 'no longer applies').map(c => c.id).join(', ') || 'none'}.`,
  '',
  'Deferred items still open:',
  '',
  ...deferred.map(it => `- ${it.id}: ${oneLine(it.feedback, 200)}`),
  '',
  '## 11. Decisions worth reconsidering',
  '',
  ...((TH.reconsider || []).length ? TH.reconsider.map(r => `- **${oneLine(r.decision, 150)}.** ${oneLine(r.reason, 300)}`) : ['None.']),
  '',
  '## 12. Coverage',
  '',
  `${coverage.units}; whole-thesis passes ${coverage.wholeThesisPasses}; feedback log ${coverage.feedbackItems}. ${DROPPED} findings were dropped by verification; ${UNVERIFIED} were kept although a verifier failed.`,
  '',
  ...(FAILS.length ? FAILS.map(x => `- ${x}`) : ['Nothing failed.']),
  '',
].join('\n')

// ---------- write: chunked, size-checked ----------
const FILES = [{ name: '00-summary.md', text: summaryText, tag: 's' }, { name: '01-findings.md', text: findingsText, tag: 'f' }]
const PARTS = FILES.flatMap(F => splitText(F.text, CHUNK_CHARS).map((content, k) => ({
  file: F.name, path: `${OUT}/_parts/${F.tag}${String(k).padStart(3, '0')}.md`, content,
  chars: [...content].length, newlines: (content.match(/\n/g) || []).length,
})))
log(`writing ${PARTS.length} parts; largest ${Math.max(...PARTS.map(p => p.chars))} characters`)
const writePrompt = p => `${BASE}

Task: create the file ${p.path} with the Write tool (create the directory first if needed; if the file already exists, delete it first with rm). Its content is every line between the two marker lines below, each line ending with a line break, including any empty lines at the start. It is final Markdown: copy it exactly; do not reformat, correct, shorten or add anything. Then measure the file:
${PY} -c "t = open(r'${p.path}', encoding='utf-8', newline='').read().replace('\\r\\n', '\\n'); print(len(t), t.count('\\n'))"
and return the two numbers as chars and newlines.
<<<BEGIN>>>
${p.content}<<<END>>>`
const okPart = (p, w) => w && Math.abs(w.chars - p.chars) <= 2 && w.newlines === p.newlines
const writes = await parallel(PARTS.map((p, k) => async () => {
  let w = await agent(writePrompt(p), { label: `write:${p.file}:${k}`, phase: 'Synthesize', schema: WROTE })
  if (!okPart(p, w)) w = await agent(writePrompt(p), { label: `write:${p.file}:${k}:retry`, phase: 'Synthesize', schema: WROTE })
  if (!okPart(p, w)) FAILS.push(`part ${p.path} does not match (expected ${p.chars} chars, ${p.newlines} line breaks; got ${w ? `${w.chars}, ${w.newlines}` : 'nothing'})`)
  return okPart(p, w)
}))
const allPartsOk = writes.every(Boolean)

const assembled = await agent(`${BASE}

Task: assemble the review files from their parts with a short Python script (UTF-8; do not retype any content):
${FILES.map(F => `- ${OUT}/${F.name} = concatenation, with no separator, of ${PARTS.filter(p => p.file === F.name).map(p => p.path).join(', ')}`).join('\n')}
Read parts with open(p, encoding='utf-8', newline='') and replace "\\r\\n" by "\\n" before joining; write with newline='\\n'. Then check that ${OUT}/01-findings.md has exactly ${N} lines starting with "### R-" and exactly ${N} lines starting with "| R-". Return those two counts.
Then copy ${WORK}/build/main-thesis.pdf to ${OUT}/review-build.pdf and ${WORK}/build/main-thesis.log to ${OUT}/review-build.log (if they exist).
${allPartsOk ? `If both counts are right, delete the directories ${OUT}/_parts and ${WORK}; if a deletion fails (e.g. a file is locked by a PDF viewer), report it and continue.` : `Some parts failed their size check: delete nothing, so the parts can be inspected.`} Return ok (both counts right), problems ("" if none) and what you deleted.`, { label: 'assemble', phase: 'Synthesize', schema: ASSEMBLED })
if (!assembled || !assembled.ok) FAILS.push(`assembly: ${assembled ? assembled.problems : 'agent failed'}`)

return {
  outDir: OUT,
  total: N,
  bySeverity: sevCount,
  fixFirst: [...new Set((TH.fixFirst || []).map(rid).filter(Boolean))].map(id => { const f = byId.get(id); return `${id} ${f.severity} ${loc(f)}: ${oneLine(f.problem, 140)}` }),
  coverage: { ...coverage, failures: FAILS },
  assembly: assembled,
}
```

---

**Note for use outside this repository.** An external LLM cannot run the workflow. Attach the PDF,
`WRITING_GUIDE.md` and the feedback log; give it the sections from "Task" to "Output" of this file;
replace "file:line" with "page, paragraph n"; ask it to work chapter by chapter in separate
messages and to collect the findings at the end.
