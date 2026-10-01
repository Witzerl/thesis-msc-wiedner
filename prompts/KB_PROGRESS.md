# Knowledge-base progress

Prompt: `prompts/PROMPT_knowledge_base.md`. Only this file is written outside `literature/` and `pdfs/`.
Last updated: 2026-10-01. **All five phases are done** for everything obtainable; nothing was committed (literature/, pdfs/ are git-ignored; this file is untracked).

## State

| Phase | State |
|---|---|
| 1. Citation index | DONE. 145 live citation commands, 63 keys, 176 (occurrence, key) pairs. `literature/_citation_index.md/.json` |
| 2. Download list | DONE. `literature/_download_list.md/.json` |
| 3. Download, verify, extract | DONE. 54 of 63 keys have a verified PDF + per-page text (`pdfs/GA`, `pdfs/Methods`). 9 library items stay PENDING (Bartels2016, Butcher1987, GottliebOrszag1977, Hairer1993, HuangRussell2011, LeVeque2002, LeVeque2007, Scarselli2009, Trefethen2000). |
| 4. Hub notes and ledger | DONE for the 54 papers with a copy: 63 hub notes carry a "Cited in thesis" section (9 with PENDING entries); 27 new concept notes; sections appended to 11 existing concept notes. Ledger: 176 entries = 98 SUPPORTED, 59 PARTLY, 4 NOT FOUND, 2 CONTRADICTED, 13 PENDING. |
| 5. Master index and search | DONE. `literature/_ledger.md`, `_tools/find_source.py`, `_tools/update_ledger.py`, `_tools/README.md`. |

## Checks that were run (2026-10-01)

- Every quote of the 154 text-based entries occurs verbatim on the cited page of the paper's text (`verify_quotes.py`; the agents ran it on their own drafts, again on the reviewers' versions, and I ran it over the whole store at the end). The 5 quotes from image-only scans (Courant1928 x3, Kutta1901, Liu1994) cannot be matched mechanically; they were read from page images by two agents each; I re-checked Kutta1901 (printed p. 435) and Liu1994 (printed p. 4) myself.
- Every ledger entry was written by one agent and independently re-judged by a second adversarial reviewer; 2 verdicts were changed by reviewers (both SUPPORTED -> PARTLY). Every concept-note contribution was fact-checked against the paper by a second agent.
- `check_links.py`: 150 notes, 0 new broken links against the vault backup taken before Phase 4.
- Coverage: 176 of 176 (occurrence, key) pairs have an entry.

## What the author has to look at

Open `literature/_ledger.md`, section "Needs your attention" (78 rows: 65 judged not-fully-supported + 13 PENDING). The hard ones:
- CONTRADICTED: C003 (Boopathiraj2024: the 288 million projection is for 2040, not 2050), C072 (Vogl2021 studies intermediate AMD before conversion, not "established GA").
- NOT FOUND: C091 and C122 (Mai2024: no one-year anchor, no "comparability" basis), C093 (Chen2018 does not support the consistency claim; Ott2021 only partly), C073 (Lad2023 contains no deep-learning review).
- Recurring PARTLY themes: "same / exact MUW cohort" as Mai2024 (they have 184 eyes / 100 patients, the thesis 75 / 51); the intro clinical numbers that sit in the secondary source but not in the cited one (160,000 per year, 5 million, 39-50 % bilateral, 14-27 % slowing); papers cited for B-scan / en-face statements that they do not make (Yehoshua2011, Pilotto2015, Vallino2024, Vogl2021, Chu2022); "deep learning" attributed to Vogl2021 and SchmidtErfurth2018 (both are Cox / mixed-effects models); "99 % within 3 mm" attributed to Pilotto2015 (not in the paper).
- Found in existing notes but NOT edited: `DMM.md` says "L-BFGS" (Hu2024 says BFGS); `Hu2024.md` still mentions a "thesis Frobenius extension"; `Geographic_Atrophy`, `CAM_Atrophy_Terminology`, `iRORA_cRORA_Progression` equated channel 0 with the cRORA region (a correction section from Mai2024 was appended to each).

## How to continue / maintain

- Thesis text changed: `python literature/_tools/update_ledger.py` (report), `--apply`; then re-check `NEW (unchecked)` / `CHANGED SENTENCE (recheck)` entries with the workflow below. See `_tools/README.md`.
- Re-run the Phase 4 workflow for chosen keys: `prep_phase4.py`, `prep_ctx.py`, then Workflow with `literature/_tools/phase4_workflow.js` and args `{keys: [...], notes_keys: <literature/_scratch/phase4_args.json>}`; then `apply_phase4.py ingest --journal <journal.jsonl> --keys ...`, `apply_phase4.py write`, `make_ledger_md.py`.
- The 9 library papers: if you ever get a PDF, save it under `pdfs/Methods/<Key>.pdf`, run `extract_text.py <Key>` and the workflow for that key; its PENDING entries become real entries.
- A backup of the vault from before Phase 4 is in the session scratchpad (`literature_backup_before_phase4`), not in the repo.
- Run ad-hoc Python from files, not from Bash heredocs (they lose `\\`); edit scripts with the Edit tool.
