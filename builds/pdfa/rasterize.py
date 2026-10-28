"""Replace selected figure form XObjects by a high-res raster of their ORIGINAL (transparent) appearance
+ an invisible copy of their text. Usage: rasterize.py orig.pdf flat.pdf out.pdf dpi page:Form ..."""
import sys, subprocess, tempfile, os, zlib, pikepdf, numpy as np
from pikepdf import Name, Operator
from PIL import Image
orig_p, flat_p, out_p, dpi = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
targets = [(int(a.split(':')[0]), a.split(':')[1]) for a in sys.argv[5:]]
orig = pikepdf.open(orig_p); flat = pikepdf.open(flat_p)
tmp = tempfile.mkdtemp()
for pg, fm in targets:
    ox = orig.pages[pg-1].obj.Resources.XObject[fm]
    fx = flat.pages[pg-1].obj.Resources.XObject[fm]
    assert '/Matrix' not in ox or list(map(float, ox.Matrix)) == [1,0,0,1,0,0]
    x0, y0, x1, y1 = map(float, ox.BBox)
    # 1) render the original form alone on a white page of its bbox
    t = pikepdf.new(); page = t.add_blank_page(page_size=(x1-x0, y1-y0))
    page.Resources = pikepdf.Dictionary(XObject=pikepdf.Dictionary(F=t.copy_foreign(ox)))
    page.Contents = t.make_stream(f'q 1 0 0 1 {-x0} {-y0} cm /F Do Q'.encode())
    tp = os.path.join(tmp, f'p{pg}.pdf'); t.save(tp)
    subprocess.run(['pdftoppm', '-r', str(dpi), '-png', '-singlefile', tp, tp[:-4]], check=True)
    img = Image.open(tp[:-4] + '.png').convert('RGB'); w, h = img.size
    # 2) invisible text copy from the flattened stream (same graphics state, nothing painted)
    keep = []
    for operands, op in pikepdf.parse_content_stream(fx):
        o = str(op)
        if o in ('S','s','f','F','f*','B','B*','b','b*'): keep.append(([], Operator('n')))
        elif o in ('Do', 'sh'): continue
        elif o == 'BT': keep.append((operands, op)); keep.append(([3], Operator('Tr')))
        else: keep.append((operands, op))
    im = pikepdf.Stream(flat, zlib.compress(np.asarray(img).tobytes(), 9))
    im.Type = Name.XObject; im.Subtype = Name.Image; im.Width = w; im.Height = h
    im.ColorSpace = Name.DeviceRGB; im.BitsPerComponent = 8; im.Filter = Name.FlateDecode
    fx.Resources.XObject[Name('/FigRaster')] = im
    body = f'q {x1-x0} 0 0 {y1-y0} {x0} {y0} cm /FigRaster Do Q\n'.encode() + pikepdf.unparse_content_stream(keep)
    fx.write(body)
    print(f'p{pg}{fm}: {w}x{h} px')
flat.save(out_p, fix_metadata_version=False)
