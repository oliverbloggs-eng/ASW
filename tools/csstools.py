import re
def strip_comments(s): return re.sub(r'/\*.*?\*/','',s,flags=re.S)
def split_blocks(s):
    out=[];i=0;n=len(s)
    while i<n:
        j=s.find('{',i)
        if j<0: break
        sel=s[i:j].strip(); depth=1;k=j+1
        while depth and k<n:
            c=s[k]
            depth+=(c=='{')-(c=='}'); k+=1
        out.append((sel,s[j+1:k-1])); i=k
    return out
def flatten(s,ctx=()):
    res=[]
    for sel,body in split_blocks(strip_comments(s)):
        if sel.startswith('@media') or sel.startswith('@supports'):
            res+=flatten(body,ctx+(sel,))
        else:
            res.append((ctx,sel,body.strip()))
    return res
def emit(rules):
    out=[];cur=None;buf=[]
    def flush():
        if not buf: return
        txt=''.join('%s{%s}\n'%(s,b) for _,s,b in buf)
        for c in reversed(cur): txt='%s{\n%s}\n'%(c,txt)
        out.append(txt)
    for r in rules:
        if cur is None or r[0]!=cur:
            flush(); buf.clear(); cur=r[0]
        buf.append(r)
    flush(); return ''.join(out)
