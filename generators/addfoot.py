import glob,re
CSS=r"""
/* ===== mobile footer ===== */
@media (max-width:640px){
  .ft-full .ft-wrap{padding:0 24px}
  .ft-full .ft-arc{width:320px;height:320px;right:-130px;top:-150px}
  .ft-full .ft-cta{display:flex;flex-direction:column;align-items:stretch;text-align:left;gap:20px;padding:48px 0 28px}
  .ft-full .ft-talk{display:flex;align-items:center;justify-content:space-between;gap:16px}
  .h-root .ft-full h2.ft-h2{font-size:34px !important;line-height:1.1 !important;text-wrap:balance}
  .ft-full .ft-go{width:44px;height:44px}
  .ft-full .ft-go svg{width:20px;height:20px}
  .ft-full .ft-book{width:100%;min-height:56px;height:56px;padding:0 24px;box-sizing:border-box;background:#94BBE4;color:#0E1F3D}
  .ft-full .ft-cols{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);grid-template-areas:"contact contact" "r2 r2" "logo logo" "areas menu";gap:0 24px;padding:0 0 28px}
  .ft-full.ft-nocta .ft-cols{padding-top:48px}
  .ft-full .ft-menu{display:block;grid-area:menu}
  .ft-full .ft-r2{display:block;grid-area:r2}
  .ft-full .ft-contact{padding:28px 0}
  .ft-full.ft-nocta .ft-contact{padding-top:0}
  .ft-full .ft-list{display:flex;flex-direction:column;gap:16px;padding-right:72px}
  .ft-full .ft-item:nth-child(2){order:2}
  .ft-full .ft-item:nth-child(3){order:1}
  .ft-full .ft-item:nth-child(4){order:3}
  .ft-full .ft-item{gap:16px;align-items:flex-start}
  .ft-full .ft-ic{width:44px;height:44px;border:1.5px solid #94BBE4}
  .ft-full .ft-txt{padding-top:0;min-width:0}
  .h-root .ft-full .ft-lab{font-size:12px !important;line-height:16px;letter-spacing:.14em !important;color:#C9DBF0}
  .ft-full .ft-val{margin-top:2px;font-size:16px;line-height:1.5;overflow-wrap:anywhere}
  .ft-full a.ft-val{min-height:0;margin-top:2px}
  .ft-full .ft-brand{padding:28px 0 0;align-items:flex-start;text-align:left}
  .ft-full .ft-logo{height:56px}
  .ft-full .ft-tag{margin:12px 0 0;max-width:260px;font-size:15px;line-height:1.5}
  .ft-full .ft-areas,.ft-full .ft-menu{margin-top:28px;min-width:0}
  .h-root .ft-full h2.ft-ah{margin:0 0 8px;font-size:18px !important;line-height:24px !important;color:#94BBE4}
  .ft-full .ft-links{display:flex;flex-direction:column;gap:0;margin:0;padding:0;list-style:none}
  .ft .ft-links a,.ft .ft-nl a,.ft .ft-legal a{color:rgba(255,255,255,.9) !important}
  .ft-full .ft-links a{display:flex;align-items:center;min-height:40px;padding:0;font-size:15px !important;line-height:20px;font-weight:400 !important}
  .ft-full .ft-sub nav{display:none}
  .ft-full .ft-sub,.ft .ft-sub{display:block;padding:24px 0 0}
  .h-root .ft .ft-legal{display:flex;flex-wrap:wrap;gap:0 16px;margin:0;padding:0;list-style:none}
  .ft .ft-legal a{display:inline-flex;align-items:center;min-height:36px;font-size:14px !important;line-height:20px;font-weight:400 !important}
  .ft-full .ft-sub + .ft-rule{display:none}
  .ft-copy,.ft .ft-copy{padding:20px 0 72px;text-align:center;font-size:13px;line-height:20px;color:#C9DBF0}
  .ft-slim-brand{padding:40px 0 28px}
  .ft:not(.ft-full) .ft-sub{padding:24px 0 0}
  .ft:not(.ft-full) .ft-nl{margin-bottom:8px}
  .ft:not(.ft-full) .ft-sub + .ft-rule{display:none}
}
"""
n=0
for f in glob.glob("/home/claude/hero/project/*.dc.html"):
    if re.search(r"/(Book|Footer|Header)\.dc\.html$",f): continue
    s=open(f,encoding="utf-8").read()
    if "/* ===== mobile footer" in s: s=s[:s.index("\n/* ===== mobile footer")]+s[s.index("</style>\n</helmet>"):]
    if "</style>\n</helmet>" not in s or "ft-wrap" not in s: continue
    s=s.replace("</style>\n</helmet>",CSS+"</style>\n</helmet>",1)
    open(f,"w",encoding="utf-8").write(s); n+=1
print("foot",n)
