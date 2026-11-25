import glob,re
CSS=r"""
/* ===== type system ===== */
.h-root{font-synthesis:none}
.h-root :is(h1,h2,h3,h4,.h-h1,.pg-h1){font-family:'Marcellus',Georgia,serif !important;font-weight:400 !important;font-synthesis:none !important}
:where(.h-root) :is(h1,h2,h3){text-wrap:balance}
.h-root :is(h1,.h-h1,.pg-h1){font-size:56px !important;line-height:1.15 !important}
.h-root h2:not(.h-ah):not(.ft-ah):not(.in-title){font-size:44px !important;line-height:1.15 !important}
.h-root :is(h3,.h-ah,.ft-ah,.in-title){font-size:28px !important;line-height:1.2 !important}
/* body */
.h-root :is(.ap3-p,.ab-p,.wh-p,.ar-p,p.at-p,.at-lead,.in-ex,.bl-ex){font-family:'DM Sans',system-ui,sans-serif !important;font-size:18px !important;line-height:1.65 !important;color:#2A3A55 !important;max-width:65ch}
/* small text, eyebrows, labels */
.h-top{font-size:14px !important}
.h-root :is(.h-eyebrow,.pv-eyebrow,.sec-eyebrow,.ab-eyebrow,.ws-eyebrow,.tb2-l,.tm-mem-h,.te-mem-h,.h-trust-l){font-family:'DM Sans',system-ui,sans-serif !important;font-size:13px !important;line-height:16px !important;font-weight:600 !important;text-transform:uppercase;letter-spacing:.14em !important}
.h-root :is(.ft-lab,.ct-lab,.vs-lab,.vu-lab){font-size:14px !important;letter-spacing:.14em !important}
.h-root span.at-p{font-size:14px !important;line-height:18px !important}
/* placeholders */
.h-root :is(.fq-a,.fp-q,.ta-r,.hw3-ph,.ct-ph){font-style:normal !important;text-decoration:none !important}
/* numerals */
.h-root :is(.ap3-n,span.at-p,.hw3-c,.hw-c,.pl-num,.pl-z,.ar-num,.ab-num,.ab-z,.fs-n:not(.fs-w)){font-family:'DM Sans',system-ui,sans-serif !important;font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1}
.h-root .fs-w{font-family:'Marcellus',Georgia,serif}
/* buttons and links */
.h-root :is(.h-btn,.h-link,.h-pillbtn,.h-all,.h-links a,.h-row,.h-chip,.pv-link,.ft-book,.ar-btn,.cl-book,.at-submit,.ct-submit,.fq-pill,.ar-all,.bl-all,.bl-more,.in-more,.te-all,.ws-lk,.ab-link,.ct-act,.vs-maps,.mp-btn,.ap-pill,.h-menu a.l,.h-menu .h-pillbtn){font-family:'DM Sans',system-ui,sans-serif !important;font-size:16px !important;font-weight:600 !important}
@media (max-width:1023px){
  .h-root :is(h1,.h-h1,.pg-h1){font-size:44px !important}
  .h-root h2:not(.h-ah):not(.ft-ah):not(.in-title){font-size:36px !important}
  .h-root :is(h3,.h-ah,.ft-ah,.in-title){font-size:24px !important}
  .h-root :is(.ap3-p,.ab-p,.wh-p,.ar-p,p.at-p,.at-lead,.in-ex,.bl-ex){font-size:17px !important}
}
@media (max-width:640px){
  .h-root :is(h1,.h-h1,.pg-h1){font-size:34px !important}
  .h-root h2:not(.h-ah):not(.ft-ah):not(.in-title){font-size:30px !important}
  .h-root :is(h3,.h-ah,.ft-ah,.in-title){font-size:22px !important}
  .h-root :is(.ap3-p,.ab-p,.wh-p,.ar-p,p.at-p,.at-lead,.in-ex,.bl-ex){font-size:16px !important}
  .h-root :is(.h-eyebrow,.pv-eyebrow,.sec-eyebrow,.ab-eyebrow,.ws-eyebrow,.tb2-l,.tm-mem-h,.te-mem-h,.h-trust-l){font-size:12px !important}
}
"""
n=0
for f in glob.glob('/home/claude/hero/project/*.dc.html'):
    if re.search(r'/(Book|Footer|Header)\.dc\.html$',f): continue
    s=open(f,encoding='utf-8').read()
    if '/* ===== type system' in s: s=s[:s.index('\n/* ===== type system')]+s[s.index('</style>\n</helmet>'):]
    if '</style>\n</helmet>' not in s: print('skip',f); continue
    s=s.replace('</style>\n</helmet>',CSS+'</style>\n</helmet>',1)
    open(f,'w',encoding='utf-8').write(s); n+=1
print('typed',n)
