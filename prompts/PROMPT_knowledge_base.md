# Prompt: build the thesis knowledge base and citation ledger

Copy everything below the line into a new Claude Code session (model: Sonnet) opened in
`D:\Schule\MasterThesis\thesis`.

---

You are helping me (Christian, the author) with the literature knowledge base of my master
thesis. The thesis LaTeX lives in this folder. Your job is **only** the knowledge base: a
local copy of every cited paper, searchable full text, notes in my Obsidian format, and a
citation ledger that tells me, for every citation in the thesis, which passage of which
page of the source supports it.

## Goal (what "done" looks like)

For any sentence in the thesis that carries a citation, I can search `literature/` and get:
the thesis location (file, section, line), the claim, the cited paper, the page, and a
short verbatim passage from the paper that supports the claim, or an explicit note that no
supporting passage was found.

## Hard rules

1. **Do not edit** any `.tex` file, `references.bib`, `NOTES.md`, `THESIS_STRUCTURE.md`,
   `CLAUDE.md` or anything under `prompts/` except your own progress file (see Phase 5).
   Another session edits the thesis text in parallel. You only write under `literature/`
   and `pdfs/`.
2. **Do not commit anything.** `literature/`, `pdfs/` and `INBOX/` are in `.gitignore` on
   purpose; the knowledge base stays local. Do not change `.gitignore`.
3. **Downloads need my approval first.** Before downloading anything, show me the complete
   download list (Phase 2) and wait for an explicit "go". Download only from the source URL
   listed for each paper. Allowed sources: arxiv.org, PubMed Central (ncbi.nlm.nih.gov/pmc),
   the publisher's own open-access page, proceedings.mlr.press, proceedings.neurips.cc,
   openreview.net, openaccess.thecvf.com, aclanthology.org, university repositories, and
   the official DOI landing page. No shadow libraries, no random mirrors. If a paper is not
   freely available, mark it "JKU library" and I will download it myself.
4. **Never invent.** No made-up page numbers, quotes or bibliographic data. Every quote is
   copied from the extracted text of the PDF, with its page number. If you cannot find
   support for a claim, write `NOT FOUND` and say what you searched for.
5. **Short quotes only.** Ledger quotes are at most about two sentences (roughly 50 words)
   per entry. These are private research notes; do not paste whole sections.
6. **Existing notes are mine.** Extend existing hub and concept notes; never delete or
   rewrite what is there. Keep their style.
7. Work in batches of about 8 papers and report after each batch. Stop and ask when
   something is ambiguous (two candidate PDFs, a preprint vs a journal version with
   different page numbers, a claim that seems wrong for the cited paper).

## Context: what exists

- `references.bib`: bibliographic data (DOI, arXiv id, venue) for every cited key. It is
  your source for titles, DOIs and arXiv ids.
- `literature/`: my Obsidian vault. **Hub notes** are named after the citation key
  (`Vogl2021.md`) and contain only links to concept notes plus a short header (venue,
  authors, DOI). **Concept notes** (`Square_Root_Transformation_ER.md`, `Pushforward_Trick.md`,
  ...) hold the synthesised content, with inline links back to hubs as `[[Key]]`. Read
  `literature/Vogl2021.md` and `literature/Square_Root_Transformation_ER.md` first to see the
  format, and match it.
- `pdfs/GA/`: PDFs of the 13 clinical papers of the first ingest (`<Key>.pdf`, some with
  `.bib`/`.md` next to them, plus timestamped duplicates like `Boyer2017_260426_214626.pdf`
  that you can ignore).
- `pdfs/2202.03376v3_MPPDE.pdf` is Brandstetter2022; `pdfs/2312.05583v2_MMPDE.pdf` is
  Hu2024. `pdfs/GA/Trincão2024.pdf` is Trincao2024 (accent in the file name).
- Tools available: `pdftotext` (poppler, in Git Bash), Python with PyMuPDF (`import fitz`)
  and `pypdf`, and `curl`.
- Hub notes exist for: Boopathiraj2024, Boyer2017, Brandstetter2022, Chu2022, Ebneter2016,
  Flaxman2020, Hu2024, Lad2023, Pilotto2015, Singh2025, Song2025, Trincao2024, Vallino2024,
  Vogl2021, Yehoshua2011. Everything else below has none.

## The reference list

Keys cited in the thesis (60). Determine the authoritative list yourself in Phase 1. Some
of these appear only in LaTeX comments; flag those.

Ba2016 BarSinai2019 Bartels2016 Battaglia2018 Bogunovic2017 Boopathiraj2024 Boyer2017
Brandstetter2022 Butcher1987 Chen2018 Chu2022 Courant1928 Courant1943 Ebneter2016
Feuer2013 Flaxman2020 Gao2019 Gilmer2017 GottliebOrszag1977 Gupta2023 Hairer1993 Hu2024
Huang1991 HuangRussell2011 Ioffe2015 JiangShu1996 Kochkov2021 Krishnapriyan2023 Kutta1901
Lad2023 Lam2023 LangtangenMardal2019 LeVeque2002 LeVeque2007 Li2021 Lienen2022 Liu1994
Liu2018 LiuSchiaffini2024 Lu2021 Mai2024 Ott2021 Pfaff2021 Pilotto2015 Ronneberger2015
Runge1895 Sadda2018 Salvi2025 SanchezGonzalez2020 Scarselli2009 SchmidtErfurth2018
Singh2025 Song2025 Trefethen2000 Trincao2024 Vallino2024 Vogl2021 Wong2014 Wu2018
Yehoshua2011

Four more are mentioned in `04-method.tex` as plain text with a `% TODO: cite` marker and
are not yet in `references.bib`. Include them in the PDF collection: Milletari2016 (V-Net,
3DV 2016, arXiv:1606.04797), Loshchilov2019 (AdamW, ICLR 2019, arXiv:1711.05101),
Paszke2019 (PyTorch, NeurIPS 2019, arXiv:1912.01703), Fey2019 (PyTorch Geometric, ICLR
2019 RLGM workshop, arXiv:1903.02428).

Gao2019 is no longer cited in the running text (its arm was dropped). Skip it unless it
turns up uncommented in Phase 1.

## Phase 1: citation index (no downloads)

Write a Python script `literature/_tools/build_citation_index.py` and run it. It must:

1. Read `00-abstract.tex`, `01-introduction.tex` ... `07-conclusion.tex` and
   `91-appendix.tex` in that order.
2. Ignore LaTeX comments (text after an unescaped `%`) and everything between `\iffalse`
   and `\fi`. Record citations found **only** in comments separately as "comment-only".
3. Find every `\cite`, `\citep`, `\citet`, `\citeauthor` and `\citeyear`, including
   optional arguments (`\citep[p.~5]{Key}`, `\citep[see][]{A,B}`) and multi-key
   citations.
4. For each occurrence, record: a stable ID (`C001`, `C002`, ... in document order), the
   file, the line number, the current `\chapter`/`\section`/`\subsection` titles, the
   key(s), and the full sentence that contains the citation (from the previous sentence end
   to the next one; strip LaTeX markup to readable text but keep math as written).
   Also record plain-text author-year mentions that have a `% TODO: cite <Key>` marker just
   above them (the four pending references), with the key from the marker.
5. Write `literature/_citation_index.md`. It starts with a summary (number of occurrences,
   number of distinct keys, comment-only keys), followed by one table per chapter:
   `| ID | Location | Key(s) | Sentence |` with Location as `03-data.tex:44 (§3.1 Dataset)`.
6. Write `literature/_citation_index.json` with the same data, for the later phases.

The script must be re-runnable: the thesis text will keep changing. Sort IDs by document
order and note the date of the run at the top of both files.

**Report to me:** the number of occurrences, the keys per chapter, the comment-only keys,
and any key that is cited but missing from `references.bib`.

## Phase 2: download list (no downloads yet)

For each key (cited keys + the four pending ones), check whether a local PDF already
exists (see Context). For each missing one, find the best freely available full text and
write `literature/_download_list.md` as a table:

`| Key | Title (short) | Version | Source URL | Est. size | Target file | Note |`

- Prefer the published version when it is open access (PMC, publisher OA, PMLR, NeurIPS,
  OpenReview, CVF). Otherwise use the arXiv version and say "arXiv v<N>, page numbers may
  differ from the published version" in Note.
- Get the size with `curl -sIL <url>` (Content-Length). If none is reported, write "?".
- Books and paywalled papers: Source URL = DOI landing page, Note = "JKU library".
  Expected: LeVeque2007, LeVeque2002, Bartels2016, Butcher1987, Hairer1993, Trefethen2000,
  GottliebOrszag1977, HuangRussell2011, Liu1994, Sadda2018, Feuer2013 (verify each, as some
  may have legal free copies, e.g. LangtangenMardal2019 is Springer open access; JiangShu1996
  has a NASA/ICASE report version; Scarselli2009 has university repository copies; Runge1895
  and Kutta1901 are public domain, e.g. via the Göttingen digitisation centre).
- Target layout: clinical and ophthalmology papers -> `pdfs/GA/<Key>.pdf`; all methods,
  machine-learning and numerics papers -> `pdfs/Methods/<Key>.pdf`.
- Misnamed existing files: propose **copies** (not moves) to the key name:
  `pdfs/2202.03376v3_MPPDE.pdf` -> `pdfs/Methods/Brandstetter2022.pdf`,
  `pdfs/2312.05583v2_MMPDE.pdf` -> `pdfs/Methods/Hu2024.pdf`,
  `pdfs/GA/Trincão2024.pdf` -> `pdfs/GA/Trincao2024.pdf`.

**Then stop and show me the table.** Wait for "go".

## Phase 3: download, verify, extract

After my "go":

1. Download each approved file with `curl -L --fail -o <target> <url>`. Do them one at a
   time and handle failures (HTML returned instead of a PDF, 403, redirect to a login page):
   mark the row FAILED with the reason and continue.
2. Verify each PDF: it opens with PyMuPDF, and the first two pages contain the title (fuzzy
   match) and the first author's surname. If not, delete that file and mark it MISMATCH.
3. Extract text **per page** to `pdfs/<subdir>/<Key>.txt`, with a marker line
   `===== page <n> =====` before each page. Use the printed page number when the PDF has
   page labels (`page.get_label()` in PyMuPDF), else the PDF page index starting at 1, and
   say which one was used in a header line at the top of the `.txt`.
4. Do the same text extraction for the PDFs that already exist.
5. Update `literature/_download_list.md` with a Status column (OK / FAILED / MISMATCH /
   JKU library / already present), and give me the list of what I must get from the JKU
   library, with DOI links.

## Phase 4: hub notes and citation ledger (batches of ~8 papers)

Order: the papers with the most citation occurrences first (from Phase 1).

For each paper with a local PDF:

1. **Hub note** `literature/<Key>.md`. If it does not exist, create it in the format of
   the existing hubs: title line, Venue, Authors, DOI or arXiv id, local PDF path, then
   "This is a **Hub Note** — links only." and sections of links to concept notes. If it
   exists, leave the existing content and only append.
2. **Concept notes:** if the paper introduces a concept the thesis relies on that has no
   concept note yet (e.g. `Fourier_Neural_Operator.md`, `Finite_Element_Network.md`,
   `Neural_ODE.md`, `CFL_Condition.md`, `Layer_Normalization.md`), create one with the key
   facts, equations and numbers, with inline `[[Key]]` links and page references like
   `[[Li2021]] p. 4`. If one exists, append a short section. Keep notes atomic: one concept
   per note. Do not create concept notes for things the thesis does not use.
3. **Ledger:** append to the hub note a section

   ```markdown
   ## Cited in thesis
   <!-- generated from _citation_index.json on YYYY-MM-DD; do not edit IDs by hand -->

   ### C017 · 02-background.tex:216 · §2.1.2 Geographic Atrophy on OCT   (format example only)
   **Thesis sentence:** "… iRORA progresses to cRORA in approximately 93 % of cases within
   twenty-four months …"
   **Claim checked:** iRORA → cRORA conversion rate and median time.
   **Source:** p. 6 (PDF page 6, printed page 1214)
   > "verbatim supporting passage, at most about two sentences"
   **Verdict:** SUPPORTED | PARTLY (say what differs) | NOT FOUND (say what was searched) |
   CONTRADICTED (quote the contradicting passage)
   ```

   Find the passage by searching the extracted `.txt` for the claim's numbers and key
   terms, then read the surrounding page to confirm. For numbers, the number in the
   thesis must appear in the quote or follow from it in an obvious way; say so if it is
   rounded or converted.
4. For a multi-key citation `\citep{A,B}`, check each key separately; each hub gets its
   own entry with the same ID.
5. For textbooks (JKU library, not yet local), create the hub note with bibliographic
   data and the "Cited in thesis" entries, with Source = `PENDING (no local copy)`.

After each batch, report: the papers done, the number of entries per verdict, and **every
PARTLY, NOT FOUND and CONTRADICTED entry with its ID and location**. Those are what I need
to fix in the thesis. Do not fix the thesis yourself.

## Phase 5: master index and search

1. Write `literature/_ledger.md`: one row per citation occurrence,
   `| ID | Location | Key | Page | Verdict | Hub |`, with Hub as an Obsidian link
   `[[Key#C017 · …]]` (or plain `[[Key]]` if heading links don't resolve), grouped by
   chapter, with a verdict summary at the top.
2. Write `literature/_tools/find_source.py`: given a phrase from the thesis (or an ID, or
   a key), print the matching ledger entries (location, key, page, quote, verdict). Accept
   approximate matches (case-insensitive, whitespace-normalised, LaTeX stripped). Usage
   example in its docstring.
3. Write `literature/_tools/update_ledger.py` (or a documented procedure in
   `literature/_tools/README.md`) for when the thesis changes: re-run Phase 1, report new
   occurrences without an entry, occurrences whose sentence text changed (the stored
   sentence no longer matches), and entries whose citation no longer exists. Moved
   citations keep their verified quote if the sentence text is unchanged.
4. Keep a progress file `prompts/KB_PROGRESS.md` (the only file you write outside
   `literature/` and `pdfs/`): the phase, the batches done, open questions for me, and the
   JKU library list. Update it after every batch so a later session can resume.

## How to report

Keep the reports short: a table or a list, counts, and the items that need my attention.
Ask me before anything irreversible, before every download round, and whenever a source
cannot be found or does not support the claim.
