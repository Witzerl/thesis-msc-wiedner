# Handoff: check the open citation-ledger entries

Written 2026-10-16. Paste the block below into a new Claude Code session in
`D:\Schule\MasterThesis\thesis`.

```
Bring the citation ledger of my thesis up to date: every open entry gets checked against its source. Follow CLAUDE.md, NOTES.md, the memory on citation rules and literature/_tools/README.md. I explicitly allow you to use a workflow (multi-agent) for this; the Phase 4 workflow script is literature/_tools/phase4_workflow.js.

## State (2026-10-16, after `update_ledger.py --apply`)
literature/_ledger.md: 99 SUPPORTED, plus
- 44 "NEW (unchecked)" entries over 35 keys: Abramoff2010 Banerjee2025 Boopathiraj2024 Boyer2017 Brandstetter2022 Chen2018 Chu2022 Cluceru2024 EMA2024Izelvay EMA2024Syfovre Ebneter2016 Ezhov2022 Ezhov2023 Feuer2013 Garvin2009 Gigon2021 Kutta1901 Lachinov2024 Lad2023 Li2006 Lindner2018 Lipkova2019 Liu2025ImageFlowNet Mai2024 Pfaff2021 Puglisi2024 Ravi2022 Rubanova2019 Runge1895 SanchezGonzalez2020 Singh2025 Vallino2024 Vogl2021 Yehoshua2011 Yoshida2025
- 55 "CHANGED SENTENCE (recheck)" entries over 32 keys (old quote still attached, the thesis sentence was reworded on 2026-10-12..14).
- Not part of this job: 11 PENDING entries (books without a local copy) and 3 PARTLY entries that are the author's deliberate decisions (Courant1943, Paszke2019, Vallino2024).
List them with `python literature/_tools/find_source.py --verdict "NEW (unchecked)"` and `--verdict "CHANGED SENTENCE (recheck)"`.

## Before running the workflow
- Many NEW entries were already verified by hand in earlier sessions but could not enter the ledger then: look in literature/_scratch/final/<Key>.json (e.g. the 13 Related Work papers of 2026-10-14, Li2006, Garvin2009, Abramoff2010). Citation IDs have shifted since; match by key and sentence. Reuse a verdict only if the thesis sentence is unchanged and the quote still passes verify_quotes.py; otherwise re-check.
- Hub notes are missing for EMA2024Izelvay, EMA2024Syfovre, Garvin2009, Li2006 (check_links.py reports them); create them in the existing hub format (see literature/Koksaldi2025.md, made today) and register missing keys in literature/_scratch/papers.json, otherwise update_ledger.py will not write their ledger sections.
- The two EMA keys are regulatory web pages (EPAR) -- check whether a local copy exists before treating them as PENDING.

## How (README "After the thesis text changed", steps 3-4)
build_citation_index.py -> prep_phase4.py and prep_ctx.py for the affected keys -> Phase 4 workflow (ledger agent + adversarial reviewer per paper, quotes checked mechanically) -> apply_phase4.py ingest --journal ... && apply_phase4.py write --keys ... -> update_ledger.py --apply -> make_ledger_md.py. Keep the workflow within the session's size guideline by batching keys. Every final quote must PASS verify_quotes.py on its cited page.

## What to report to me, and what not to change on your own
- A table of every entry that ends PARTLY, NOT FOUND or CONTRADICTED: thesis sentence, what the source says (short quote), and the smallest fix (rewording or a different citation).
- Do not edit the thesis text on your own; we go through the problem entries together, one at a time, as in the 2026-10-01 recheck (NOTES.md, "Citation recheck and corrections").
- At the end: NOTES.md updated (close the "Ledger recheck after the 2026-10-12..14 rewording" item), commit to master (no Co-Authored-By; literature/ and pdfs/ are git-ignored, so the commit is mainly NOTES.md and any agreed .tex fixes).
```
