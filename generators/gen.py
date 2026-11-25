import os,re
OUT="/home/claude/hero/project"
STATUE="/_blob/7bffb6afabcfcbc44b6f7d89a6f80b82"
LOGO="/_blob/0f1b700fd0305212cb9b04b1c9d788d5"

P={
"clock":'<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
"mail":'<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
"phone":'<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/>',
"arrow":'<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
"scale":'<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
"briefcase":'<rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
"file":'<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
"home":'<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
"user":'<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
"users":'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
"checks":'<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/>',
"calendar":'<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
"pin":'<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
"shield":'<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
"compass":'<circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z"/>',
}
def ic(n,s=20,sw=1.8,extra=''):
    return '<svg aria-hidden="true" width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"%s>%s</svg>'%(s,s,sw,extra,P[n])

AREAS=[("Dispute Resolution","scale"),("Commercial and Corporate","briefcase"),("Public Procurement and Tax","file"),("Property &amp; Real Estate","home"),("Private Client","user"),("Employment and Pensions","users")]
PILLARS=[("Competence","checks"),("Integrity","shield"),("Pragmatism","compass")]

IDS=["dispute","commercial","procurement","property","private","employment"]
rows=""
for i,(t,k) in enumerate(AREAS):
    rows+='          <li><a class="h-row%s" href="Areas.dc.html#%s"><span class="h-ric">%s</span><span>%s</span></a></li>\n'%(" on" if i==0 else "",IDS[i],ic(k,20),t)
IDS=["dispute","commercial","procurement","property","private","employment"]
chips=""
for j,(t,k) in enumerate(AREAS):
    chips+='        <li><a class="h-chip" href="Areas.dc.html#%s"><span class="h-ric">%s</span><span>%s</span></a></li>\n'%(IDS[j],ic(k,18),t)
pd=""; pm=""
for t,k in PILLARS:
    pd+='        <li class="h-pill-i"><span class="h-pic">%s</span><span class="h-pl">%s</span></li>\n'%(ic(k,22,1.6),t)
    pm+='        <li class="h-pm-i"><span class="h-pic">%s</span><span class="h-pl">%s</span></li>\n'%(ic(k,22,1.6),t)

JS_RET = '''      ai,
      dots: [0,1,2,3,4,5].map((i) => ({
        cls: i === ai ? 'ar-dot on' : 'ar-dot',
        cur: i === ai ? 'true' : 'false',
        label: 'Show area ' + (i + 1) + ' of 6',
        go: () => {
          const t = document.getElementById('ar-track');
          if (t && t.children[i]) t.scrollTo({ left: t.children[i].offsetLeft - t.children[0].offsetLeft, behavior: 'smooth' });
        }
      })),
      onTrack: (e) => {
        const t = e.currentTarget || e.target;
        if (!t || !t.children || t.children.length < 2) return;
        const step = t.children[1].offsetLeft - t.children[0].offsetLeft;
        const i = Math.max(0, Math.min(5, Math.round(t.scrollLeft / step)));
        if (i !== this.state.ai) this.setState({ ai: i });
      }'''
P["building"]='<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4"/><path d="M10 10h4"/><path d="M10 14h4"/><path d="M10 18h4"/>'
P["checkc"]='<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>'
P["arrowur"]='<path d="M7 7h10v10"/><path d="M7 17 17 7"/>'
from home3 import areas_phone_html, PV_CSS, trust_html, who_html, how_html, team_html, faq_html, about_html, areas_html, blog_html
from about import FOOT_CSS, foot_html
PHONE_CSS=r"""
/* phone hero refinement (390 only) */
.h-top{position:relative;z-index:60}
.h-top .h-wrap{min-height:36px;padding:0 24px}
.h-top a.h-ti{min-height:44px;margin:-4px 0;font-size:14px;font-weight:600}
.h-nav .h-wrap{min-height:64px;padding:0 24px}
.h-logo img{height:40px}
.h-burger{width:44px;height:44px}
.h-inner{padding:28px 24px 0;min-height:0}
.h-copy{padding-bottom:0;max-width:none}
.h-eyebrow{font-size:13px;line-height:16px}
.h-h1{margin:12px 0 0;font-size:34px;line-height:1.15;max-width:none;text-wrap:nowrap}
.h-h1 span:not(.h-nb){display:block}
.h-actions{margin-top:20px;gap:8px}
.h-btn{min-height:56px;padding:6px 6px 6px 26px}
.h-link{min-height:44px}
.h-art{min-height:0;height:348px;margin-top:8px;overflow:hidden}
.h-arch2{width:316px;height:348px;margin-left:-158px;border-radius:158px 158px 0 0}
.h-arch{width:281px;height:334px;margin-left:-140px;border-radius:140px 140px 0 0}
.h-statue{height:544px;top:-3px;bottom:auto}
.h-panel{margin-top:-24px;border-radius:24px 24px 0 0}
.h-panel .h-wrap{padding:20px 20px 16px}
.h-ah{font-size:22px;line-height:28px;margin:0}
.h-root .h-chips{display:flex;flex-wrap:nowrap;gap:8px;margin:12px -20px 0;padding:0 44px 0 20px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:20px;scrollbar-width:none;-webkit-overflow-scrolling:touch;-webkit-mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 40px),transparent 100%);mask-image:linear-gradient(90deg,#000 0,#000 calc(100% - 40px),transparent 100%)}
.h-chips::-webkit-scrollbar{display:none}
.h-chips>li{flex:none;scroll-snap-align:start}
.h-root .h-chip{min-height:48px;padding:4px 18px 4px 4px;white-space:nowrap;font-size:15px}
.h-root .h-chip .h-ric{width:40px;height:40px}
.h-root a.h-all{display:inline-flex;align-items:center;gap:8px;min-height:44px;margin-top:4px;font-size:16px;font-weight:600;color:#0B66A0}

/* phone section rhythm */
.pv{padding:48px 0}
.pv-wrap,.tb2-in{padding-left:24px;padding-right:24px}
.pv-eyebrow + .pv-h2{margin-top:10px}
.pv-h2{font-size:30px;line-height:1.15;text-wrap:balance}
.pv-bar{margin-top:12px}
.pv-head{gap:2px}
.h-root .wo-grid,.h-root .il,.h-root .fp-list{margin-top:16px}
.h-root .at-grid{margin:16px -24px 0;padding:4px 24px 12px;scroll-padding-left:24px}
.h-root .hw3{margin-top:16px}
.h-root .ta-grid{margin:16px -24px 0;padding:4px 24px 12px;scroll-padding-left:24px}
/* trust bar */
.tb2-in{flex-direction:column;align-items:flex-start;flex-wrap:nowrap;gap:12px;min-height:0;padding-top:24px;padding-bottom:24px}
.h-root .tb2-ul{flex-direction:column;align-items:stretch;gap:0;width:100%}
.h-root .tb2-b{width:100%;min-height:40px;padding:0;border:0;border-radius:0;background:transparent;font-size:16px;gap:12px}
.h-root .tb2-b + .tb2-b{border-top:1px solid #E1E8F2}
.tb2 .pv-link{margin:0}
/* about preview + pillars */
.ap3-top{gap:16px}
.ap3-p{font-size:16px;line-height:1.6}
.h-root a.ap3-lk{margin-top:12px}
.ap3-lead{margin:14px 0 0;font-size:15px;line-height:22px;font-weight:600;gap:12px}
.h-root .ap3-row{grid-template-columns:repeat(3,minmax(0,1fr));margin-top:12px;border-radius:16px}
.h-root .ap3-i{flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:6px;padding:11px 4px;min-width:0}
.ap3-i > span:not(.ap3-ic){display:contents}
.ap3-i br{display:none}
.ap3-n{order:0;font-size:14px;line-height:16px}
.ap3-ic{order:1;width:40px;height:40px}
.ap3-ic svg{width:20px;height:20px}
.ap3-t{order:2;font-size:16px;line-height:20px;white-space:nowrap}
.h-root .ap3-i + .ap3-i{border-left:1px solid #E6ECF4;border-top:0}

/* link below content; who we serve; how we work */
.h-root h2#wo-t{max-width:260px}
.h-root a.pv-top{display:none}
.h-root a.pv-bot{display:inline-flex;margin-top:20px}
.h-root .wo-grid{gap:12px}
.h-root .wo-c{height:72px;min-height:72px;padding:0 16px 0 16px;gap:14px}
.wo-ic{width:40px;height:40px}
.wo-ic svg{width:20px;height:20px}
.wo-t{font-size:22px;line-height:1.15}
.wo-go{width:40px;height:40px}
.wo-go svg{width:18px;height:18px}
.h-root .hw3{gap:0;margin-top:16px}
.h-root .hw3-s{position:relative;display:grid;grid-template-columns:40px minmax(0,1fr);column-gap:16px;align-items:center;box-sizing:border-box;height:68px;min-height:68px;padding:0;background:linear-gradient(#E1E8F2,#E1E8F2) 56px 100%/calc(100% - 56px) 1px no-repeat}
.h-root .hw3-s:last-child{background:none}
.hw3-c{width:40px;height:40px;font-size:15px;font-weight:600;border-width:2px;background:#0E1F3D;border-color:#0E1F3D;color:#ffffff}
.h-root .hw3-c .hw3-nm{display:block;line-height:1}
.h-root .hw3-s:last-child .hw3-nm{display:none}
.h-root .hw3-s:last-child .hw3-ck{display:block}
.hw3-s::after{display:block;content:"";position:absolute;top:54px;left:19px;right:auto;width:2px;height:28px;background:#94BBE4}
.hw3-s::before{content:"";position:absolute;top:54px;left:19px;width:2px;height:28px;background:#0E1F3D;z-index:1;transform-origin:top}
.hw3-s:last-child::after,.hw3-s:last-child::before{display:none}
.h-root h3.hw3-t{margin:0;font-size:22px !important;line-height:1.2 !important}
.h-root .hw3-g{display:block;position:absolute;right:0;top:50%;transform:translateY(-50%);font-family:'DM Sans',system-ui,sans-serif !important;font-size:44px;line-height:1;font-weight:600;font-variant-numeric:lining-nums;color:rgba(14,31,61,.06);pointer-events:none;user-select:none}
.pv[aria-labelledby=hw-t]{position:relative;overflow:clip;border-top:1px solid #E1E8F2}
.pv[aria-labelledby=hw-t] .pv-wrap{position:relative;z-index:1}
.pv[aria-labelledby=hw-t]::before{content:"";position:absolute;top:0;right:24px;width:29px;height:150px;pointer-events:none;background:repeating-linear-gradient(90deg,rgba(14,31,61,.05) 0 1px,transparent 1px 14px);-webkit-mask-image:linear-gradient(#000 40%,transparent);mask-image:linear-gradient(#000 40%,transparent)}
@keyframes hw-circ{from{background:#ffffff;border-color:#94BBE4;color:#0E1F3D}to{background:#0E1F3D;border-color:#0E1F3D;color:#ffffff}}
@keyframes hw-seg{from{transform:scaleY(0)}to{transform:scaleY(1)}}
@supports (animation-timeline:view()){@media (prefers-reduced-motion:no-preference){
.hw3-s{view-timeline:none}
.hw3-s:not(:first-child) .hw3-c{animation:hw-circ linear both;animation-timeline:view(block);animation-range:cover calc(40svh) cover calc(40svh + 24px)}
.hw3-s::before{animation:hw-seg linear both;animation-timeline:view(block);animation-range:cover calc(40svh + 24px) cover calc(40svh + 68px)}
}}

/* phone v3: no areas sheet in hero, new order, areas carousel */
.h-hero .h-inner{padding-bottom:0}
.h-art{height:352px}
.h-arch2{height:352px}
.h-arch{height:338px}
.pv[aria-labelledby=atp-h],.pv[aria-labelledby=hw-t],.pv[aria-labelledby=fp-t]{background:#F2F2F0}
.pv[aria-labelledby=wo-t],.pv[aria-labelledby=ta-t],.pv[aria-labelledby=il-h]{background:#ffffff}

/* real mobile layout: hero without areas sheet, order, number, areas carousel */
.h-panel{display:none}
.h-pd{display:none}
.h-pm{display:inline}
.at-dk{display:none}
.pv.at-ph{display:block}
.h-root{display:flex;flex-direction:column}
.h-top{order:0}
.h-nav{order:1}
.h-hero{order:2}
.pv[aria-labelledby=ap3-t]{order:3}
.tb2{order:4}
.pv[aria-labelledby=wo-t]{order:5}
.pv[aria-labelledby=atp-h]{order:6}
.pv[aria-labelledby=hw-t]{order:7}
.pv[aria-labelledby=ta-t]{order:8}
.pv[aria-labelledby=fp-t]{order:9}
.pv[aria-labelledby=il-h]{order:10}
.ft{order:11}

/* areas carousel */
.pv[aria-labelledby=wo-t]{border-top:1px solid #E6ECF4}
.at-reg{margin:0 -24px}
.h-root .at-grid{display:flex;gap:12px;margin:16px 0 0;padding:4px 10vw 12px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-inline:10vw;scrollbar-width:none;-webkit-overflow-scrolling:touch;overscroll-behavior-x:contain}
.at-grid::-webkit-scrollbar{display:none}
.at-grid>li{flex:0 0 80vw;min-width:0;scroll-snap-align:center;scroll-snap-stop:always}
@keyframes at-depth{0%{transform:scale(.96);opacity:.85}50%{transform:scale(1);opacity:1}100%{transform:scale(.96);opacity:.85}}
@supports (animation-timeline:view(inline)){@media (prefers-reduced-motion:no-preference){.at-grid>li{animation:at-depth linear both;animation-timeline:view(inline);animation-range:cover 0% cover 100%}}}
.at-ph .at-t{border-radius:20px;box-shadow:0 10px 28px rgba(14,31,61,.14);transition:transform .2s ease}
.at-ph .at-t:hover{transform:none}
.at-ph .at-t:active{transform:scale(.98)}
.at-ph .at-m::after{content:"";position:absolute;inset:0;z-index:1;background:#0E1F3D;opacity:.14;mix-blend-mode:multiply;pointer-events:none}
.at-ph .at-i{object-position:center}
.at-ph .at-p{z-index:2}
.at-ph .at-b,.at-ph .at-t:hover .at-b,.at-ph .at-t:active .at-b{box-sizing:border-box;height:60px;min-height:60px;background:#0E1F3D;border-top:1px solid #94BBE4}
.at-ph .at-n{min-width:0;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:19px;line-height:1.2;color:#ffffff}
.at-ph .at-go{width:40px;height:40px;justify-content:center;border-radius:50%;background:#ffffff;color:#0E1F3D;transition:background .2s ease}
.at-ph .at-b svg{color:#0E1F3D}
.at-ph .at-t:active .at-go{background:#94BBE4}
.at-ph .at-t:hover .at-i{transform:none}
@media (prefers-reduced-motion:reduce){.at-ph .at-t{transition:none}}
.at-foot{view-timeline:--ctl block}
.at-ctl{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-top:4px}
.at-cnt{display:flex;flex-direction:column;gap:8px}
.h-root p.at-num{margin:0;font-family:'DM Sans',system-ui,sans-serif !important;font-size:14px !important;line-height:20px !important;font-weight:600;font-variant-numeric:lining-nums;color:#5B6B88 !important}
.at-cur{color:#0E1F3D}
.at-track{position:relative;display:block;width:180px;height:2px;background:#94BBE4;border-radius:2px;overflow:hidden}
.at-fill{position:absolute;left:0;top:0;width:100px;height:2px;background:#0E1F3D;border-radius:2px;transition:transform .3s ease}
.at-fill.s1{transform:translateX(16px)}.at-fill.s2{transform:translateX(32px)}.at-fill.s3{transform:translateX(48px)}.at-fill.s4{transform:translateX(64px)}.at-fill.s5{transform:translateX(80px)}
.at-btns{display:flex;gap:10px}
.at-btn{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;padding:0;border-radius:50%;border:1.5px solid #8FB0D6;background:#ffffff;color:#0E1F3D;cursor:pointer;transition:background .2s ease,opacity .2s ease}
.at-btn:active{background:#E4ECF8}
.at-btn:focus-visible{outline:3px solid #0F74B5;outline-offset:3px}
.at-btn.dis{opacity:.4;cursor:default}
.at-foot a.pv-bot{margin-top:20px}
/* team carousel */
.h-root .ta-grid{display:flex;gap:16px;margin:16px -24px 0;padding:4px 26vw 12px 24px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-inline:24px;scrollbar-width:none;-webkit-overflow-scrolling:touch;overscroll-behavior-x:contain}
.ta-grid>li{flex:0 0 74vw;display:block;min-width:0;scroll-snap-align:start;scroll-snap-stop:always}
.h-root .ta-c{display:flex;flex-direction:column;align-items:flex-start;text-align:left;min-height:44px}
.h-root .ta-fr{position:relative;width:calc(100% - 16px);height:auto;aspect-ratio:4/5;margin:8px;transition:none}
.h-root .ta-fr::before{inset:-8px;transform:none;border:1.5px solid #94BBE4;border-radius:999px 999px 0 0;box-sizing:border-box}
.ta-ph{border-radius:999px 999px 0 0}
.ta-ph::after{content:"";position:absolute;left:0;right:0;bottom:0;height:25%;background:linear-gradient(to top,rgba(14,31,61,.55),rgba(14,31,61,0));pointer-events:none}
.ta-c:hover .ta-fr,.ta-c:focus-visible .ta-fr{transform:none}
.h-root .ta-l.on .ta-fr::before,.ta-c:hover .ta-fr::before,.ta-c:focus-visible .ta-fr::before{border-color:#0E1F3D}
.ta-c:focus-visible{outline:3px solid #0F74B5;outline-offset:2px;border-radius:8px}
.h-root .ta-n{margin:16px 0 0;font-size:22px;line-height:1.2}
.h-root .ta-r{margin:4px 0 0;font-size:16px;line-height:1.5;color:#5B6B88}
@keyframes ta-depth{0%,20%{transform:scale(.96);opacity:.85}54%{transform:scale(1);opacity:1}88%,100%{transform:scale(.96);opacity:.85}}
@keyframes ta-ring{0%,30%{border-color:#94BBE4}54%{border-color:#0E1F3D}78%,100%{border-color:#94BBE4}}
@supports (animation-timeline:view(inline)){@media (prefers-reduced-motion:no-preference){
.ta-grid>li{animation:ta-depth linear both;animation-timeline:view(inline);animation-range:cover 0% cover 100%}
.h-root .ta-fr::before{animation:ta-ring linear both;animation-timeline:view(inline);animation-range:cover 0% cover 100%}
}}
.h-root .ta-foot{display:block;view-timeline:--tctl block}
.at-fill.t1{transform:translateX(40px)}.at-fill.t2{transform:translateX(80px)}
.h-root .ta-foot .ta-ctl{margin-top:4px}

.h-root .at-grid + .at-foot{margin-top:0}
@media (prefers-reduced-motion:reduce){.at-fill{transition:none}}
"""
AREAS_PH=areas_phone_html(ic)
TEMPLATE = open('/home/claude/hero/template.html',encoding='utf-8').read()
for name,title,w,h in (("HeroDesktop","Hero + About: Desktop 1440",1440,5364),("HeroTablet","Hero + About: Tablet 768",768,5701),("HeroPhone","Hero + About: Phone 390",390,5865)):
    html=(TEMPLATE.replace("@@TITLE@@",title).replace("@@W@@",str(w)).replace("@@H@@",str(h))
          .replace("@@STATUE@@",STATUE).replace("@@LOGO@@",LOGO)
          .replace("@@ROWS@@",rows).replace("@@CHIPS@@",chips).replace("@@TRUST@@",trust_html(ic)).replace("@@WHO@@",who_html(ic)).replace("@@HOW@@",how_html(ic)).replace("@@ABOUT@@",about_html(ic)).replace("@@AREAS@@",areas_html(ic)).replace("@@AREAS_CSS@@",FOOT_CSS+PV_CSS).replace("@@TEAM@@",team_html(ic)).replace("@@FAQ@@",faq_html(ic)).replace("@@FOOT@@",foot_html(ic)).replace("@@BLOG@@",blog_html(ic)).replace("@@ABOUT_CSS@@","")
          .replace("@@I_CLOCK@@",ic("clock",15)).replace("@@I_MAIL@@",ic("mail",15)).replace("@@I_PHONE@@",ic("phone",15))
          .replace("@@I_ARROW18@@",ic("arrow",20,2)).replace("@@I_ARROW16@@",ic("arrow",18,2)).replace("@@I_SHIELD@@",ic("shield",18,1.7)))
    if name=="HeroPhone":
        html=re.sub(r'<div class="h-panel">.*?</a>\n      </div>\n    </div>\n','',html,flags=re.S)
        html=re.sub(r'      <nav class="h-areas-d".*?</nav>\n','',html,flags=re.S)
        a0=html.index('  <!-- Trust bar -->'); a1=html.index('  <!-- About preview -->'); a2=html.index('  <!-- Who we serve -->')
        html=html[:a0]+html[a1:a2]+html[a0:a1]+html[a2:]
        b0=html.index('  <!-- Areas preview -->'); b1=html.index('  <!-- How we work -->')
        html=html[:b0]+areas_phone_html(ic)+html[b1:]
        html=html.replace("+254 788685911","+254 788 685 911").replace("</style>\n</helmet>","@media (max-width:640px){"+PHONE_CSS+"}</style>\n</helmet>",1)
    open(os.path.join(OUT,name+".dc.html"),"w",encoding="utf-8").write(html)
print("ok")

# ---- build Main from the same template ----
WA = """
<!-- WhatsApp -->
<div style="position:sticky;bottom:24px;height:0;display:flex;justify-content:flex-end;padding-right:24px;z-index:40">
  <a class="wa" href="https://wa.me/254788685911" aria-label="Chat with ASW Law Advocates on WhatsApp" style="display:flex;align-items:center;justify-content:center;width:56px;height:56px;margin-top:-80px;border-radius:9999px;background:#25d366;box-shadow:0 8px 24px rgba(14,31,61,0.28)">
    <svg aria-hidden="true" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21l1.65-4.9A8.5 8.5 0 1 1 8 19.4L3 21z"/><path d="M9 8.6c.2 2.7 2.6 5.4 5.6 5.9l1.2-1.3c.2-.2.5-.3.8-.2l1.5.6c.3.1.5.4.4.7-.4 1.2-1.6 1.9-2.8 1.8-3.8-.4-7-3.5-7.4-7.2-.1-1.2.6-2.3 1.8-2.6.3-.1.6.1.7.4l.6 1.5c.1.3 0 .6-.2.8"/></svg>
  </a>
</div>
"""
old=open('/home/claude/hero/main_pre_about.html',encoding='utf-8').read()
a=old.index('<!-- WhatsApp -->'); b=old.index('</div>\n',old.index('</a>',a))+7
WA_ORIG=old[a:b]
html=(TEMPLATE.replace("@@TITLE@@","ASW Law Advocates LLP: Home").replace("@@W@@","1440").replace("@@H@@","5364")
      .replace("@@STATUE@@",STATUE).replace("@@LOGO@@",LOGO)
      .replace("@@ROWS@@",rows).replace("@@CHIPS@@",chips)
      .replace("@@TRUST@@",trust_html(ic)).replace("@@WHO@@",who_html(ic)).replace("@@HOW@@",how_html(ic)).replace("@@ABOUT@@",about_html(ic)).replace("@@AREAS@@",areas_html(ic)+AREAS_PH).replace("@@AREAS_CSS@@",FOOT_CSS+PV_CSS).replace("@@TEAM@@",team_html(ic)).replace("@@FAQ@@",faq_html(ic)).replace("@@FOOT@@",foot_html(ic)).replace("@@BLOG@@",blog_html(ic))
      .replace("@@ABOUT_CSS@@","")
      .replace("@@I_CLOCK@@",ic("clock",15)).replace("@@I_MAIL@@",ic("mail",15)).replace("@@I_PHONE@@",ic("phone",15))
      .replace("@@I_ARROW18@@",ic("arrow",20,2)).replace("@@I_ARROW16@@",ic("arrow",18,2)).replace("@@I_SHIELD@@",ic("shield",18,1.7)))
html=html.replace('<span>+254 788685911</span>','<span class="h-pd">+254 788685911</span><span class="h-pm">+254 788 685 911</span>',1)
html=html.replace('<div class="h-root">','<div style="width:100%;background:#ffffff;timeline-scope:--ctl,--tctl">\n<div class="h-root">',1)
WA_NEW='''
<!-- WhatsApp -->
<div class="wa-w">
  <a class="wa-b" href="https://wa.me/254788685911" target="_blank" rel="noopener" aria-label="Chat with ASW Law Advocates on WhatsApp">
    <svg aria-hidden="true" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21l1.65-4.9A8.5 8.5 0 1 1 8 19.4L3 21z"/><path d="M9 8.6c.2 2.7 2.6 5.4 5.6 5.9l1.2-1.3c.2-.2.5-.3.8-.2l1.5.6c.3.1.5.4.4.7-.4 1.2-1.6 1.9-2.8 1.8-3.8-.4-7-3.5-7.4-7.2-.1-1.2.6-2.3 1.8-2.6.3-.1.6.1.7.4l.6 1.5c.1.3 0 .6-.2.8"/></svg>
  </a>
</div>
'''
WA_CSS="""
.wa-w{position:sticky;bottom:24px;height:0;display:flex;justify-content:flex-end;padding-right:24px;z-index:40}
.wa-b{display:flex;align-items:center;justify-content:center;width:56px;height:56px;margin-top:-80px;border-radius:9999px;background:#25d366;box-shadow:0 8px 24px rgba(14,31,61,.28)}
@keyframes wa-in{from{opacity:0;pointer-events:none}to{opacity:1;pointer-events:auto}}
@media (max-width:640px){
  .wa-w{bottom:0;padding-right:16px;z-index:60}
  .wa-b{width:48px;height:48px;margin-top:-68px}
  .wa-b svg{width:26px;height:26px}
  @supports (animation-timeline:scroll()){.wa-w{animation:wa-in linear both;animation-timeline:scroll(root);animation-range:620px 880px}}
  @supports (animation-timeline:--ctl){.wa-b{animation:wa-hide linear,wa-hide linear;animation-timeline:--ctl,--tctl;animation-range:cover 0% cover 100%,cover 0% cover 100%}}
}
@keyframes wa-hide{0%{opacity:1}6%{opacity:0;pointer-events:none}94%{opacity:0;pointer-events:none}100%{opacity:1}}
"""
html=html.replace('</div>\n</x-dc>','</div>\n'+WA_NEW+'\n</div>\n</x-dc>',1)
html=html.replace('</style>\n</helmet>',WA_CSS+'@media (max-width:640px){'+PHONE_CSS+'}</style>\n</helmet>',1)
open('/home/claude/hero/project/Main.dc.html','w',encoding='utf-8').write(html)
print('main ok',html.count('class="ab"'),html.count('class="ft"'),html.count('wa.me'))
