import pymupdf as fitz, json
SRC='/mnt/user-data/uploads/1c6bb138-Class3_CT_ThinkBook_Sample_Ch1_v6.pdf'
v6=fitz.open(SRC)
out=fitz.open()
order=list(range(19))+[21]   # p1-19 + back cover (Discover and Notes dropped)
for i in order: out.insert_pdf(v6,from_page=i,to_page=i)
# 1) swap QR images by xref (positions unchanged)
XMAP={355:'CGN000008',357:'CGN000009',359:'CGN000010',361:'CGN000011',363:'CGN000012',365:'CGN000013',367:'CGN000014',368:'CGN000015',369:'CGN000017',370:'CGN000002',226:'CGN000002',548:'CGN000002'}
# find xrefs in new doc by matching image digests
import hashlib
def dig(doc,x): return hashlib.md5(doc.extract_image(x)['image']).hexdigest()
old={dig(v6,x):k for x,k in XMAP.items()}
done=set()
for pi,p in enumerate(out):
    for img in p.get_images(full=True):
        x=img[0]
        if x in done: continue
        try: h=dig(out,x)
        except Exception: continue
        if h in old:
            p.replace_image(x,filename=f'qr/{old[h]}.png'); done.add(x); print('page',pi+1,'xref',x,'->',old[h])
# 2) fallback glyphs: remove text, remember for overlay
glyphs=[]
for pi,p in enumerate(out):
    if pi>=19: break
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines',[]):
            for sp in l['spans']:
                if sp['font'].startswith(('Type3','Liberation')):
                    for ch in sp['text']:
                        pass
                    r=fitz.Rect(sp['bbox']); glyphs.append({'page':pi+1,'text':sp['text'],'bbox':list(r),'color':'#%06x'%sp['color'],'size':sp['size']})
                    p.add_redact_annot(r)
    p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE,graphics=fitz.PDF_REDACT_LINE_ART_NONE)
json.dump(glyphs,open('glyphs.json','w'),indent=0)
# 4) back cover (index 21): blank lower half above the wave
p=out[19]
p.add_redact_annot(fitz.Rect(0,538,613.3,768.5))
p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_REMOVE,graphics=fitz.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED)
out.save('stage1.pdf',garbage=4,deflate=True)
print(len(out),'pages;',len(glyphs),'glyphs')
