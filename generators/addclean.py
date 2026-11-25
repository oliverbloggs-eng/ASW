import glob,re
CSS=r"""
/* ===== clean accents: no dash ornaments ===== */
:is(.h-eyebrow,.pv-eyebrow,.sec-eyebrow,.ab-eyebrow,.ws-eyebrow){gap:8px !important;align-items:center !important}
:is(.h-eyebrow,.pv-eyebrow,.sec-eyebrow,.ab-eyebrow,.ws-eyebrow)::before{content:"" !important;display:block !important;flex:none !important;width:6px !important;height:6px !important;border-radius:50% !important;background:#94BBE4 !important;margin:0 !important}
:is(.h-eyebrow,.pv-eyebrow,.sec-eyebrow,.ab-eyebrow,.ws-eyebrow) + :is(h1,h2){margin-top:10px !important}
:is(.pv-bar,.sec-bar,.ws-bar,.ar-bar,.bl-bar,.pg-hair){display:none !important}
:is(.h-eyebrow,.pv-eyebrow,.sec-eyebrow,.ab-eyebrow,.ws-eyebrow)::after{content:none !important}
.h-root .pv-head + :not(.at-reg){margin-top:16px !important}
@media (max-width:640px){.ap3-lead::after{display:none !important}}
"""
n=0
for f in glob.glob("/home/claude/hero/project/*.dc.html"):
    if re.search(r"/(Book|Footer|Header)\.dc\.html$",f): continue
    s=open(f,encoding="utf-8").read()
    if "/* ===== clean accents" in s: s=s[:s.index("\n/* ===== clean accents")]+s[s.index("</style>\n</helmet>"):]
    if "</style>\n</helmet>" not in s: continue
    s=s.replace("</style>\n</helmet>",CSS+"</style>\n</helmet>",1)
    open(f,"w",encoding="utf-8").write(s); n+=1
print("clean",n)
