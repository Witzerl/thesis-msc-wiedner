"""z-tests for the comparison tables of Appendix E (Section "Statistics of the Comparisons").

Supervisor review 2, SV-5.2: every fold-paired comparison is tested against the variation of
retraining. For a mean difference D over n folds,
    sigma_Delta = sqrt(sigma_A^2 + sigma_B^2) / sqrt(n),   z = D / sigma_Delta,
with sigma = 0.0127 for one run of a graph network (seven replicate pairs, Appendix E.3) and
sigma = 0.0191 for one run of the parameter-matched U-Net (its seed-42/seed-7 pairs on folds 0-4,
NOTES.md "U-Net run-to-run spread", 2026-10-18). |z| > 1.96 means two-sided p < 0.05.

The script reads the fold-paired cells "$<D> \\pm <SE>$ (<k>/<n>)" of the three tables in
91-appendix.tex, decides from the comparison name whether a U-Net is on one or both sides, and
writes "(<k>/<n>, $z = <z>$)". Without --apply it only prints the table of values.

Run (from the thesis repo):  python images/scripts/appendix_ztests.py [--apply]
"""
import math
import re
import sys
from pathlib import Path

SIG_G = 0.0127
SIG_U = 0.0191
APPENDIX = Path(__file__).resolve().parents[2] / "91-appendix.tex"
START = r"\label{app:full-results:seeds}"
END = r"\label{app:code}"
CELL = re.compile(r"(\$([+-]\d+\.\d{4}) \\pm (\d\.\d{4})\$ \((\d)/(\d))\)")
HEAD = re.compile(r"\\multicolumn\{4\}\{l\}\{\\textbf\{(.*)\}\}")


def n_unet(name):
    """Number of comparison sides that are a U-Net (0, 1 or 2)."""
    if re.match(r"\s*U-Net, width", name):
        return 2  # capacity rows: U-Net against U-Net
    return 1 if "U-Net" in name else 0


def z_of(d, n, k_unet):
    sa = SIG_U if k_unet >= 1 else SIG_G
    sb = SIG_U if k_unet == 2 else SIG_G
    return d / (math.sqrt(sa ** 2 + sb ** 2) / math.sqrt(n))


def main(apply):
    text = APPENDIX.read_text(encoding="utf-8")
    i0, i1 = text.index(START), text.index(END)
    lines = text[i0:i1].split("\n")
    current = ""
    out = []
    for line in lines:
        h = HEAD.search(line)
        if h:
            current = h.group(1)
        m = CELL.search(line)
        if m and "$z =" not in line:
            stripped = line.strip()
            name = current if stripped.startswith("&") else stripped.split("&")[0]
            d, n = float(m.group(2)), int(m.group(5))
            z = z_of(d, n, n_unet(name))
            p = math.erfc(abs(z) / math.sqrt(2))
            print(f"{name[:52]:52s} D={d:+.4f} n={n} U={n_unet(name)} z={z:+6.2f} p={p:.3f}")
            line = line[:m.start()] + m.group(1) + f", $z = {z:.1f}$)" + line[m.end():]
        out.append(line)
    if apply:
        with open(APPENDIX, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text[:i0] + "\n".join(out) + text[i1:])
        print("written:", APPENDIX)


if __name__ == "__main__":
    main("--apply" in sys.argv)
