"""PDF/A-1b finishing: CIDSet streams, Info/XMP date match, sRGB output intent, classic xref, PDF 1.4 header.
Usage: finish.py in.pdf out.pdf icc"""
import sys, io, re, pikepdf
from pikepdf import Name
from fontTools.ttLib import TTFont
src, dst, icc = sys.argv[1:4]
pdf = pikepdf.open(src)
n = 0
for o in pdf.objects:
    if not (isinstance(o, pikepdf.Dictionary) and o.get('/Type') == Name.Font and o.get('/Subtype') in (Name.CIDFontType2, Name.CIDFontType0)):
        continue
    fd = o.FontDescriptor
    if '/CIDSet' in fd: continue
    assert '/FontFile2' in fd, (o.BaseFont, list(fd.keys()))
    tt = TTFont(io.BytesIO(fd.FontFile2.read_bytes()), lazy=False)
    glyf, order = tt['glyf'], tt.getGlyphOrder()
    m = o.get('/CIDToGIDMap', Name.Identity)
    if m == Name.Identity:   # TeX subsets keep empty slots for unused glyphs
        present = [gid for gid, g in enumerate(order) if gid == 0 or glyf[g].numberOfContours != 0]
    else:                    # matplotlib subsets: every glyph in the font is used (spaces have no contours)
        present = list(range(len(order)))
    if m == Name.Identity:
        cids = present
    else:
        raw = m.read_bytes(); g2c = {}
        for cid in range(len(raw) // 2):
            g = raw[2*cid] << 8 | raw[2*cid+1]
            if g or cid == 0: g2c.setdefault(g, []).append(cid)
        cids = sorted(c for g in present for c in g2c.get(g, []))
    bits = bytearray((max(cids) // 8) + 1)
    for c in cids: bits[c // 8] |= 0x80 >> (c % 8)
    fd.CIDSet = pdf.make_stream(bytes(bits)); n += 1
print('CIDSets added:', n)
# dates: make Info CreationDate equal to XMP CreateDate
x = pdf.Root.Metadata.read_bytes().decode()
cd = re.search(r'<xmp:CreateDate>([^<]*)<', x).group(1)
y, mo, d, h, mi, s, tz = re.match(r'(\d{4})-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)([+-]\d\d:\d\d)', cd).groups()
pdf.docinfo[Name.CreationDate] = pikepdf.String(f"D:{y}{mo}{d}{h}{mi}{s}{tz[:3]}'{tz[4:]}'")
print('CreationDate ->', pdf.docinfo.CreationDate)
prof = pdf.make_stream(open(icc, 'rb').read()); prof.N = 3
pdf.Root.OutputIntents = pikepdf.Array([pikepdf.Dictionary(Type=Name.OutputIntent, S=Name.GTS_PDFA1,
    OutputConditionIdentifier=pikepdf.String('sRGB IEC61966-2.1'), Info=pikepdf.String('sRGB IEC61966-2.1'),
    RegistryName=pikepdf.String('http://www.color.org'), DestOutputProfile=prof)])
pdf.save(dst, fix_metadata_version=False, object_stream_mode=pikepdf.ObjectStreamMode.disable,
         force_version='1.4')
