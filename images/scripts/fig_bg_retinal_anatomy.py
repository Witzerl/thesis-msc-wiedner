"""Figure 2.3 (fig:bg:retinal-anatomy): retinal layers and the OCT signs of GA, with labels.

Inputs (images/raw/, read-only backups, never modified), both 2172 x 724 px, no text:
  fig_bg_retinal_anatomy_raw_healthy.png  healthy retina around the foveal pit
  fig_bg_retinal_anatomy_raw_ga.png       the same strip with a GA lesion in the middle
Both were generated with ChatGPT image generation from
prompts/PROMPT_fig_2_3_retina_layers_imagegen.md. Everything else is drawn here: the layer
labels of panel (a) and the three OCT signs of GA in panel (b), numbered as in the text
(Section 2.1.3, signatures (i)-(iii)).

Anchors are pixels of the raw images, measured with colour scans down narrow columns
(x = 160 and x = 2000 for the flat parts, x = 1086 for the lesion centre). The layers sit at
the same heights on both sides and in both panels:
  ILM 100-105, RNFL 106-130, GCL 131-169, IPL 170-200, INL 201-241, OPL 242-269,
  ONL 271-346, ELM 347-361, IS 362-406, EZ 408-415, OS 416-462, RPE 463-489,
  BM (seam) 490, CC 492-537, choroid 538-590, sclera 592-657.
Lesion (panel b): RPE absent between x ~833 and ~1343 (row 476); heaped RPE at x ~780-860;
at x = 1086 the remnant cell row lies at y 446-459 on Bruch's membrane (y 462-468),
washed-out choroid y 470-590.

Output: images/fig_bg_retinal_anatomy.pdf (include at width=\\textwidth).
"""
from __future__ import annotations

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

from _common import IMAGES, panel_label, save, setup

pal = setup()
PAL = pal.PAL
RAW = IMAGES / "raw"
FS = 6.5
LEAD = dict(arrowstyle="-", lw=0.4, color=PAL["ink"], shrinkA=1.5, shrinkB=0)
DOWNSAMPLE = 1600
W, H = 2172, 724
XL, XR = -330, W + 400            # gutters for the labels


def load(name: str) -> np.ndarray:
    im = Image.open(RAW / name).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    grey_white = (a.min(axis=2) >= 246) & (a.max(axis=2) - a.min(axis=2) <= 6)
    a[grey_white] = 255
    im = Image.fromarray(a.astype(np.uint8))
    s = DOWNSAMPLE / im.size[0]
    return np.asarray(im.resize((DOWNSAMPLE, round(im.size[1] * s)), Image.LANCZOS))


def label(ax, text, anchor, at, ha="left", va="center", color=None):
    # leader starts at the middle of the label's near edge, so each line clearly belongs
    # to one label
    rel = {("left", "center"): (0, 0.5), ("right", "center"): (1, 0.5),
           ("center", "bottom"): (0.5, 0), ("right", "bottom"): (1, 0),
           ("left", "bottom"): (0, 0), ("right", "top"): (1, 1), ("left", "top"): (0, 1),
           ("center", "top"): (0.5, 1)}[(ha, va)]
    ax.annotate(text, xy=anchor, xytext=at, ha=ha, va=va, fontsize=FS,
                color=color or PAL["ink"], arrowprops=dict(LEAD, relpos=rel),
                annotation_clip=False)
    ax.plot(*anchor, "o", ms=1.4, color=PAL["ink"], mec="white", mew=0.3, zorder=5)


def fan(top, bottom, n):
    return np.linspace(top, bottom, n)


def draw_healthy(ax):
    ax.imshow(load("fig_bg_retinal_anatomy_raw_healthy.png"), extent=(0, W, H, 0),
              interpolation="none")
    inner = [("ILM", 102), ("RNFL", 118), ("GCL", 150), ("IPL", 185), ("INL", 221),
             ("OPL", 256), ("ONL", 308)]
    for (name, y), yl in zip(inner, fan(30, 420, len(inner))):
        label(ax, name, (150, y), (-40, yl), ha="right")
    outer = [("ELM", 356), ("IS", 384), ("EZ", 411), ("OS", 440), ("RPE", 476), ("BM", 490),
             ("CC", 514), ("Choroid", 560), ("Sclera", 622)]
    for (name, y), yl in zip(outer, fan(250, 740, len(outer))):
        label(ax, name, (2040, y), (W + 40, yl))
    label(ax, "Foveal pit", (1086, 227), (1086, -45), ha="center", va="bottom")
    ax.text(330, 55, "Vitreous", fontsize=FS, color=PAL["ink_2"], style="italic",
            ha="center", va="center")
    ax.set_xlim(XL, XR)
    ax.set_ylim(770, -90)
    ax.set_aspect("equal")
    ax.axis("off")


def draw_ga(ax):
    ax.imshow(load("fig_bg_retinal_anatomy_raw_ga.png"), extent=(0, W, H, 0),
              interpolation="none")
    label(ax, "(i) photoreceptors and RPE lost,\nlayers above collapsed", (1000, 452),
          (930, -40), ha="right", va="bottom")
    label(ax, "Bruch's membrane intact", (1250, 465), (1330, -40), ha="left", va="bottom")
    label(ax, "(iii) RPE–BM thickening at the margin", (812, 448), (760, 790), ha="right",
          va="top")
    label(ax, "(ii) choroidal hypertransmission", (1086, 545), (1150, 790), ha="left",
          va="top")
    ax.set_xlim(XL, XR)
    ax.set_ylim(870, -150)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    fig = plt.figure(figsize=(131.5 / 25.4, 98 / 25.4))
    ax_a = fig.add_axes([0.0, 0.52, 1.0, 0.48])
    ax_b = fig.add_axes([0.0, 0.0, 1.0, 0.52])
    draw_healthy(ax_a)
    draw_ga(ax_b)
    panel_label(ax_a, "(a)", x=0.03, y=0.95)
    panel_label(ax_b, "(b)", x=0.03, y=0.95)
    save(fig, "fig_bg_retinal_anatomy")


if __name__ == "__main__":
    main()
