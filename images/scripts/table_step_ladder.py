"""Tables of the step-size ladder (Section 5.6.1, Table tab:experiments:swap, and Appendix E,
Table tab:appendix:step-ladder).

Reads the cache written by images/scripts/step_ladder.py (images/data/step_ladder/*.json, git-ignored):
trained checkpoints (epoch 29) re-evaluated without retraining with a fixed step h = 1, 1/2, ..., 1/32
year, explicit Euler and classical RK4, folds 0-4. Prints the summary rows (Table tab:experiments:swap),
the full ladder rows (Table tab:appendix:step-ladder) and the per-halving changes behind the verdicts.

Criteria (Section 5.6.1), against the run-to-run sd 0.0127:
  C1, convergence: at the two finest steps (22.8 -> 11.4 days) the change stays below the sd for both
      schemes, and Euler and RK4 agree within it at 11.4 days.
  C2, agreement: all settings at least as fine as the training setting in both step and order (for the
      Euler-trained network every setting; for the RK4-trained ones RK4 only; for the T-FEN RK4 at steps
      up to 1/8 year = 45.6 days, which splits every interval like its 45-day training step) span at
      most the sd, the trained setting included.

Run (from the thesis repo):  python images/scripts/table_step_ladder.py
"""
import json
from pathlib import Path

CACHE = Path(__file__).resolve().parents[1] / "data" / "step_ladder"
SD = 0.0127
H = ["365", "182.5", "91.25", "45.625", "22.8125", "11.4062"]
MODELS = [  # arm, name, trained config, schemes in C2, largest step in C2 (index into H)
    ("ANISOGNN_final_dilmean", "Canonical dilated-stencil network (trained: Euler, one step per interval)",
     "euler:n1", ("euler", "rk4"), 0),
    ("ANISOGNN_final_oderk4n1", "Network trained in the RK4 wrapper (trained: RK4, one step per interval)",
     "rk4:n1", ("rk4",), 0),
    ("FEN_final_w96ftp7rk4d45skew", "T-FEN, energy-conserving form (trained: RK4, 45-day steps)",
     "rk4:d45", ("rk4",), 3),
]


def main():
    summary, full = [], []
    for arm, name, tr, c2_schemes, c2_from in MODELS:
        full.append(f"    \\multicolumn{{7}}{{l}}{{\\emph{{{name}}}}} \\\\")
        for fold in (0, 1, 2, 3, 4):
            d = json.loads((CACHE / f"{arm}_f{fold}.json").read_text())
            c = {r["config"]: r["chg_dice"] for r in d["rows"]}
            t = c[tr]
            assert abs(t - d["info"]["chg_dice_logged_epoch"]) < 1e-9, (arm, fold)  # control
            fine = [t] + [c[f"{sc}:d{h}"] for sc in c2_schemes for h in H[c2_from:]]
            span = max(fine) - min(fine)
            e = [c[f"euler:d{h}"] for h in H]
            r = [c[f"rk4:d{h}"] for h in H]
            c1 = abs(e[-1] - e[-2]) < SD and abs(r[-1] - r[-2]) < SD and abs(e[-1] - r[-1]) < SD
            c2 = span <= SD
            summary.append((name.split(" (")[0], fold, e[-1] - t, r[-1] - t, span, c1, c2))
            print(f"{arm[:18]} f{fold} Euler halvings " + " ".join(f"{e[i+1]-e[i]:+.4f}" for i in range(5))
                  + " | RK4 " + " ".join(f"{r[i+1]-r[i]:+.4f}" for i in range(5))
                  + f" | E-R at 11.4 d {e[-1]-r[-1]:+.4f}")
            full.append(f"    Fold {fold}, Euler & " + " & ".join(f"${x - t:+.3f}$" for x in e) + " \\\\")
            full.append(f"    Fold {fold}, RK4 & " + " & ".join(f"${x - t:+.3f}$" for x in r) + " \\\\")
        full.append("    \\midrule")
    print("\nSUMMARY TABLE ROWS (Delta Euler / RK4 at 11.4 d, span, C1, C2)")
    last = None
    for name, fold, de, dr, span, c1, c2 in summary:
        if name != last:
            print(f"    \\multicolumn{{6}}{{l}}{{\\emph{{{name}}}}} \\\\")
            last = name
        print(f"    Fold {fold} & ${de:+.3f}$ & ${dr:+.3f}$ & {span:.3f} & "
              f"{'passes' if c1 else 'fails'} & {'passes' if c2 else 'fails'} \\\\")
    print("\nFULL LADDER ROWS")
    print("\n".join(full))


if __name__ == "__main__":
    main()
