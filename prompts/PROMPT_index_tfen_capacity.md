# Prompt: index the last two T-FEN capacity runs (code repo)

Copy everything below the line into a new Claude Code session opened in
`D:\Schule\MasterThesis\masterthesis-docker`.

---

Two runs are currently running on the cluster. **Do not start yet.** Read this
prompt, check that you have everything you need (the files and scripts named
below), tell me in a few lines what you will do, and then **wait for my "go"**.
I will say go once both runs have finished.

## The runs

| Job | Experiment (five folds, `_f0` ... `_f4`) | What it is |
|---|---|---|
| 7875529 | `FEN_final_w192ftp7rk4d45skew` | T-FEN, skew-form transport, width 192 (4x capacity) |
| 7875530 | `FEN_final_w96d8ftp7rk4d45skew` | T-FEN, skew-form transport, MLP depth 8 |

Twin (reference) for both: `FEN_final_w96ftp7rk4d45skew` (0.5428 +/- 0.0401).
The width-48 skew point `FEN_final_w48ftp7rk4d45skew` (0.5434) is already in.

## Tasks after my "go"

1. **Pull** the runs: `MODE=pull bash jobs/sync_solver.sh` (in WSL; it asks for my
   password). Check with `MODE=status` first that both arrays are finished.
2. **Integrity check**, per run: 30/30 epochs on all five folds; one run directory per
   fold (if a fold has two, the earlier is superseded -- say so); `args.json` differs from
   its twin's only in the experiment name and the intended knob (`hidden_dim` 192, or the
   FEN depth 8) plus presence-only keys at their defaults; the logged parameter count
   (expected 247,543 for w192 and 142,999 for depth 8 -- report if different).
3. **Results table:** regenerate `GraphPDE/demos & explanations/solver_results.csv` with
   `collect_solver_results.py --include_archive --carry_deleted`. It has not been
   regenerated since 2026-09-30, so the 2026-10-01 batch (section 9.22) enters it too.
   Check that the anchor rows did not change (e.g. `ANISOGNN_final_dilmean` 0.5258).
4. **Numbers**, with `GraphPDE/demos & explanations/thesis_numbers.py` (it checks its own
   anchor first):
   ```
   python "GraphPDE/demos & explanations/thesis_numbers.py" pair FEN_final_w48ftp7rk4d45skew FEN_final_w96ftp7rk4d45skew  FEN_final_w192ftp7rk4d45skew FEN_final_w96ftp7rk4d45skew  FEN_final_w96d8ftp7rk4d45skew FEN_final_w96ftp7rk4d45skew --latex
   python "GraphPDE/demos & explanations/thesis_numbers.py" stability FEN_final_w48ftp7rk4d45skew FEN_final_w192ftp7rk4d45skew FEN_final_w96d8ftp7rk4d45skew
   python "GraphPDE/demos & explanations/thesis_numbers.py" capacity --style D:/Schule/MasterThesis/thesis/style
   ```
   Also record the minimum epoch time over the folds and its fold
   (`curve_sec_per_epoch_min`).
5. **Readout** in `GraphPDE/demos & explanations/SOLVER_FINAL_RUNS.md` as a new section
   **9.23**, in the style of 9.21/9.22: what was run and why (the T-FEN rows of the
   capacity table, redone in the skew form because the Galerkin form was unstable), the
   integrity check, a table with the three skew capacity points against the width-96 twin
   (mean +/- sd, fold-paired mean +/- SE (k/5), per eye mean +/- SE (m/75, t), stability
   5/5 or not, cost), and a short reading: is capacity a lever for the T-FEN in the skew
   form or not? Compare with the Galerkin capacity rows (w192 -0.090, depth 8 -0.204),
   which were dominated by instability. Include the `--latex` lines so the thesis table
   can be filled directly.
6. **Commit** in the code repo: section 9.22 is already in `SOLVER_FINAL_RUNS.md` but
   uncommitted -- commit it first as its own commit ("SOLVER_FINAL_RUNS 9.22: the
   2026-10-01 batch readout"), then the CSV + 9.23 as a second commit. Do not commit the
   Office lock file `presentation/~$GA_state_of_project_filled.pptx`.
7. **Push** to `origin main` (the branch is already several commits ahead; push them all).

## Rules

- Do not change any training code, any run directory or any earlier section of
  `SOLVER_FINAL_RUNS.md`.
- Do not touch the thesis repository (`D:\Schule\MasterThesis\thesis`); the thesis
  session fills the table there from your 9.23.
- Never invent a number: every value comes from the scripts above or from the run files.
  If a check fails, stop and tell me.
- At the end, give me a short summary: the three rows, whether capacity matters for the
  skew T-FEN, and the commit hashes.
