#!/usr/bin/env python3
"""Check internal links, anchors, assets, dash rule and noindex on every HTML page."""
import re,os,glob,sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pages=sorted(glob.glob('*.html')); ids={p:set(re.findall(r'\bid="([^"]+)"',open(p,encoding='utf-8').read())) for p in pages}
bad=0
for p in pages:
    s=open(p,encoding='utf-8').read()
    for h in re.findall(r'(?:href|src)="([^"]+)"',s):
        if re.match(r'(https?:|mailto:|tel:|data:)',h): continue
        f,_,a=h.partition('#')
        if f=='' : tgt=p
        else:
            tgt=f
            if not os.path.exists(tgt): print('MISSING',p,h); bad+=1; continue
        if a and tgt.endswith('.html') and a not in ids.get(tgt,set()): print('NO ANCHOR',p,h); bad+=1
    for pat,name in ((r'—','em dash'),(r'–','en dash'),(r' - ','spaced hyphen')):
        t=re.sub(r'<(script|style)[^>]*>.*?</\1>','',s,flags=re.S); t=re.sub(r'<[^>]+>','',t)
        if re.search(pat,t): print('DASH',p,name); bad+=1
    if 'name="robots" content="noindex, nofollow"' not in s: print('NO NOINDEX',p); bad+=1
    for im in re.findall(r'<img [^>]*>',s):
        if 'alt=' not in im: print('NO ALT',p,im[:80]); bad+=1
        if 'width=' not in im: print('NO DIMS',p,im[:80]); bad+=1
    if len(re.findall(r'<h1',s))!=1: print('H1 count',p,len(re.findall(r'<h1',s)))
print('pages',len(pages),'problems',bad)
