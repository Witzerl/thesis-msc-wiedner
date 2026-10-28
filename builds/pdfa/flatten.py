"""Remove PDF/A-1-forbidden transparency without changing the rendered result over white.
Usage: python flatten.py in.pdf out.pdf"""
import sys, pikepdf
from pikepdf import Name, Operator, Array, Dictionary
src, dst = sys.argv[1:3]
pdf = pikepdf.open(src)

def num(x): return float(x)
def gs_alpha(gsd):
    return (num(gsd.get('/CA', 1)), num(gsd.get('/ca', 1)))
def blend(col, a):            # col: tuple in DeviceRGB or DeviceGray, over white
    return tuple(a * c + (1 - a) for c in col)
def colop(col, stroke):
    if len(col) == 1: return ([col[0]], Operator('G' if stroke else 'g'))
    return (list(col), Operator('RG' if stroke else 'rg'))

PAINT_STROKE = {'S', 's'}
PAINT_FILL = {'f', 'F', 'f*'}
PAINT_BOTH = {'B', 'B*', 'b', 'b*'}
TEXT = {'Tj', 'TJ', "'", '"'}
variant_cache = {}

def transform(stream_obj, resources, state_in):
    """Rewrite one content stream. state_in = (fill, stroke, CA, ca) inherited."""
    ops = pikepdf.parse_content_stream(stream_obj)
    gsdict = (resources.get('/ExtGState') or {}) if resources is not None else {}
    xobjs = (resources.get('/XObject') or {}) if resources is not None else {}
    st = list(state_in); stack = []
    emitted = [None, None]; estack = []          # colours currently in force in the output stream
    out = []
    def ensure_colours(need_fill, need_stroke):
        fill, stroke, CA, ca = st
        if need_fill and fill is not None:
            eff = blend(fill, ca) if ca < 1 else fill
            if emitted[0] != eff: out.append(colop(eff, False)); emitted[0] = eff
        if need_stroke and stroke is not None:
            eff = blend(stroke, CA) if CA < 1 else stroke
            if emitted[1] != eff: out.append(colop(eff, True)); emitted[1] = eff
    changed = False
    for operands, op in ops:
        o = str(op)
        if o == 'q': stack.append(list(st)); estack.append(list(emitted)); out.append((operands, op)); continue
        if o == 'Q': st = stack.pop(); emitted[:] = estack.pop(); out.append((operands, op)); continue
        if o == 'gs':
            g = gsdict[operands[0]]
            if '/CA' in g: st[2] = num(g.CA)
            if '/ca' in g: st[3] = num(g.ca)
            out.append((operands, op)); continue
        if o in ('rg', 'g'):
            st[0] = tuple(num(v) for v in operands); emitted[0] = st[0]; out.append((operands, op)); continue
        if o in ('RG', 'G'):
            st[1] = tuple(num(v) for v in operands); emitted[1] = st[1]; out.append((operands, op)); continue
        if o in ('cs', 'CS', 'sc', 'SC', 'scn', 'SCN', 'k', 'K'):
            if o in ('sc', 'scn', 'SC', 'SCN', 'k', 'K'): raise SystemExit(f'unsupported colour op {o}')
            # cs/CS /DeviceRGB resets colour to black
            cs = str(operands[0]); assert cs in ('/DeviceRGB', '/DeviceGray'), cs
            black = (0.0, 0.0, 0.0) if cs == '/DeviceRGB' else (0.0,)
            if o == 'cs': st[0] = black; emitted[0] = black
            else: st[1] = black; emitted[1] = black
            out.append((operands, op)); continue
        if o == 'Tr': raise SystemExit('text render mode in use')
        CA, ca = st[2], st[3]
        if o in PAINT_STROKE | PAINT_FILL | PAINT_BOTH:
            strokes = o in PAINT_STROKE | PAINT_BOTH and CA > 0
            fills = o in PAINT_FILL | PAINT_BOTH and ca > 0
            if (CA < 1 or ca < 1): changed = True
            if o in PAINT_BOTH:
                closes = o in ('b', 'b*'); even = o.endswith('*')
                if strokes and fills: newop = o
                elif fills: newop = ('f*' if even else 'f'); 
                elif strokes: newop = 's' if closes else 'S'
                else: newop = 'n'
                if closes and newop in ('f', 'f*'): out.append(([], Operator('h')))
            elif o in PAINT_STROKE: newop = o if strokes else 'n'
            else: newop = o if fills else 'n'
            ensure_colours(fills, strokes)
            out.append(([], Operator(newop))); continue
        if o in TEXT:
            if ca < 1: changed = True
            if ca == 0: raise SystemExit('invisible text')
            ensure_colours(True, False); out.append((operands, op)); continue
        if o == 'Do':
            x = xobjs[operands[0]]
            if x.get('/Subtype') == Name.Form and (CA < 1 or ca < 1):
                changed = True
                ensure_colours(True, True)
                key = (x.objgen, st[2], st[3], st[0], st[1])
                if key not in variant_cache:
                    nx = pikepdf.Stream(pdf, b'')
                    for k, v in x.items():
                        if k not in ('/Length', '/Filter', '/DecodeParms'): nx[k] = v
                    body = transform(x, x.get('/Resources'), tuple(st))
                    nx.write(body)
                    name = Name('/' + 'Flat%d' % len(variant_cache))
                    variant_cache[key] = (name, nx)
                name, nx = variant_cache[key]
                resources.XObject[name] = nx
                out.append(([name], op)); continue
            if x.get('/Subtype') == Name.Image and (ca < 1): raise SystemExit('image under alpha')
            out.append((operands, op)); continue
        if o in ('sh', 'BI', 'EI', 'ID'): 
            if CA < 1 or ca < 1: raise SystemExit(f'{o} under alpha')
        out.append((operands, op))
    return pikepdf.unparse_content_stream(out)

def needs(res):
    for g in (res.get('/ExtGState') or {}).values():
        if gs_alpha(g) != (1.0, 1.0): return True
    return False

done = set(); log = []
def walk_forms(res, path):
    for n, x in list((res.get('/XObject') or {}).items()):
        if x.objgen in done: continue
        if x.get('/Subtype') == Name.Form:
            done.add(x.objgen)
            if '/Group' in x and str(x.Group.get('/S')) == '/Transparency':
                del x['/Group']; log.append(f'{path}{n}: removed transparency group')
            r = x.get('/Resources') or Dictionary()
            walk_forms(r, path + str(n))
            if needs(r):
                body = transform(x, r, (None, None, 1.0, 1.0))
                x.write(body); log.append(f'{path}{n}: flattened alpha')
                for g in r.ExtGState.values():
                    if '/CA' in g: g.CA = 1
                    if '/ca' in g: g.ca = 1
        elif x.get('/Subtype') == Name.Image and '/SMask' in x:
            import numpy as np, zlib
            from pikepdf import PdfImage
            im = PdfImage(x).as_pil_image().convert('RGB'); m = PdfImage(x.SMask).as_pil_image().convert('L')
            a = np.asarray(m, dtype=np.float64) / 255.0; c = np.asarray(im, dtype=np.float64)
            out = np.round(c * a[..., None] + 255.0 * (1 - a[..., None])).astype(np.uint8)
            done.add(x.objgen)
            x.write(zlib.compress(out.tobytes()), filter=Name.FlateDecode)
            for k in ('/SMask', '/DecodeParms', '/Decode'): 
                if k in x: del x[k]
            x.ColorSpace = Name.DeviceRGB; x.BitsPerComponent = 8
            log.append(f'{path}{n}: image soft mask composited onto white')
for i, p in enumerate(pdf.pages):
    walk_forms(p.obj.get('/Resources') or Dictionary(), f'p{i+1}')
    if needs(p.obj.get('/Resources') or Dictionary()): raise SystemExit(f'page {i+1} content has alpha')
print('\n'.join(log)); print('marker variants:', len(variant_cache))
pdf.save(dst, fix_metadata_version=False)
