# One-time migration: stage1.pdf -> src/ (HTML source of record)
import pymupdf as fitz, re, os, hashlib, base64, json, shutil
SRC='src'; os.makedirs(SRC+'/assets',exist_ok=True); os.makedirs(SRC+'/fonts',exist_ok=True); os.makedirs(SRC+'/pages',exist_ok=True)
for f in ['Poppins-Regular','Poppins-Bold','Poppins-Italic','Poppins-BoldItalic','Poppins-Medium']:
    shutil.copy(f'/usr/share/fonts/truetype/google-fonts/{f}.ttf',f'{SRC}/fonts/')
for f in ['DejaVuSansMono','DejaVuSansMono-Bold']: shutil.copy(f'/usr/share/fonts/truetype/dejavu/{f}.ttf',f'{SRC}/fonts/')
for f in os.listdir('qr'): shutil.copy('qr/'+f,f'{SRC}/assets/'+f)
d=fitz.open('stage1.pdf')
seen={}
def ext(m):
    kind,data=m.group(2),m.group(3)
    raw=base64.b64decode(data); h=hashlib.md5(raw).hexdigest()[:12]
    fn=f'assets/img_{h}.{ "jpg" if kind=="jpeg" else kind}'
    if h not in seen: open(f'{SRC}/{fn}','wb').write(raw); seen[h]=fn
    return f'{m.group(1)}="{fn}"'
for i,p in enumerate(d):
    s=p.get_svg_image(text_as_path=False)
    s=re.sub(r'(xlink:href|href)="data:image/(png|jpeg|jpg);base64,([^"]+)"',ext,s)
    s=re.sub(r'^<\?xml[^>]*>\s*','',s)
    # make ids unique per page
    s=re.sub(r'id="([^"]+)"',lambda m:f'id="p{i+1}_{m.group(1)}"',s)
    s=re.sub(r'url\(#([^)]+)\)',lambda m:f'url(#p{i+1}_{m.group(1)})',s)
    s=re.sub(r'(xlink:href|href)="#([^"]+)"',lambda m:f'{m.group(1)}="#p{i+1}_{m.group(2)}"',s)
    s=s.replace('<svg ','<svg class="pg" ',1)
    open(f'{SRC}/pages/p{i+1:02d}.svg','w').write(s)
print(len(d),'pages',len(seen),'images', sum(os.path.getsize(f'{SRC}/'+v) for v in seen.values())//1024,'KB')
