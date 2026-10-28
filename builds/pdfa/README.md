# PDF/A-1b post-processing of the hand-in PDF (2026-10-28)

The PAS upload rules require PDF/A (ISO 19005-1). The XeTeX build is not PDF/A-1: five figures use
transparency, which PDF/A-1 forbids. The v2 hand-in PDF was made from the v1 build (keywords removed
from the cover) with these scripts, then checked with veraPDF 1.28.2 (PDF/A-1b: PASS):

    python flatten.py   in.pdf flat.pdf                       # transparency -> equivalent solid colours
    python rasterize.py in.pdf flat.pdf flat_r.pdf 1200 87:/Fm19   # page-87 figure as 1200 dpi image + invisible text
    python finish.py    flat_r.pdf out.pdf sRGB.icc           # CIDSets, dates, sRGB output intent, PDF 1.4, classic xref

`in.pdf` is the keyword-free v1 build; `sRGB.icc` from TeX Live (`colorprofiles`). Requires pikepdf,
fonttools, numpy, Pillow and poppler (`pdftoppm`).
