"""Figure 2.1 (fig:bg:eye-anatomy): two openly licensed Wikimedia Commons images.

Inputs (images/third_party/, see SOURCES.md there for authors, URLs and licences):
  (a) commons_schematic_diagram_of_the_human_eye_en_1920.png -- Wikimedia's own PNG
      render of File:Schematic_diagram_of_the_human_eye_en.svg (Rhcastilhos, Jmarchn;
      CC BY-SA 3.0). Its background is transparent; it is placed on white here, which is
      the only change.
  (b) commons_macula_1920.png -- Wikimedia's PNG render of File:Macula.svg (photograph
      Danny Hope, diagram Zyxwv99; CC BY 2.0). Unchanged apart from resampling.

Both panels are resampled to OUT_WIDTH px, which is ~420 dpi at 0.48\\textwidth.
Outputs: images/fig_bg_eye_anatomy_a.png, images/fig_bg_eye_anatomy_b.png.

A 6 x 6 mm OCT-window overlay on (b) was tried and left out: at the image's own scale
(5.5 mm bar = 763 px) the square's edges run through the "macula" and "0.65 mm" labels.
The caption states the window size instead.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image

THESIS = Path(__file__).resolve().parents[2]
SRC = THESIS / "images" / "third_party"
OUT = THESIS / "images"
OUT_WIDTH = 1200
DPI = 300


def resample(im: Image.Image) -> Image.Image:
    h = round(im.height * OUT_WIDTH / im.width)
    return im.resize((OUT_WIDTH, h), Image.LANCZOS)


def main() -> None:
    eye = Image.open(SRC / "commons_schematic_diagram_of_the_human_eye_en_1920.png").convert("RGBA")
    white = Image.new("RGBA", eye.size, (255, 255, 255, 255))
    eye = Image.alpha_composite(white, eye).convert("RGB")
    resample(eye).save(OUT / "fig_bg_eye_anatomy_a.png", dpi=(DPI, DPI))

    macula = Image.open(SRC / "commons_macula_1920.png").convert("RGB")
    resample(macula).save(OUT / "fig_bg_eye_anatomy_b.png", dpi=(DPI, DPI))


if __name__ == "__main__":
    main()
