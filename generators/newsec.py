NEW_CSS = r"""
/* new home sections */
@keyframes nv-rise{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
@supports (animation-timeline:view()){.nv{animation:nv-rise linear both;animation-timeline:view();animation-range:entry 0% entry 55%}}
@media (prefers-reduced-motion:reduce){.nv{animation:none !important}}
.tb{background:#ffffff;border-bottom:1px solid #E6ECF4}
.tb-in{max-width:1280px;margin:0 auto;padding:0 40px;min-height:96px;display:flex;align-items:center;gap:20px 40px;flex-wrap:wrap}
.tb-l{font-size:12.5px;line-height:16px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#0B66A0}
.h-root .tb-ul{display:flex;flex-wrap:wrap;gap:14px 20px;margin:0;padding:0;list-style:none}
.tb-b{display:inline-flex;align-items:center;gap:14px;padding:12px 22px 12px 14px;border:1px solid #D5DFEC;border-radius:14px;background:#ffffff}
.tb-ic{display:inline-flex;align-items:center;justify-content:center;flex:none;width:40px;height:40px;border-radius:50%;background:#1B4584;color:#ffffff}
.tb-t{font-family:'Marcellus',Georgia,serif;font-size:19px;line-height:1.2;color:#0E1F3D}
.ws{background:#F2F2F0;padding:96px 0 80px}
.ws + .ar{border-top:1px solid #DDE5F0}
.ws-wrap{max-width:1280px;margin:0 auto;padding:0 40px}
.ws-eyebrow{display:flex;align-items:center;gap:14px;font-size:13px;line-height:16px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#0B66A0}
.ws-eyebrow::before{content:"";width:36px;height:2px;background:#0B66A0}
.ws-h2{margin:20px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:44px;line-height:1.12;letter-spacing:-.01em;color:#0E1F3D}
.ws-bar{display:block;width:64px;height:4px;margin-top:26px;border-radius:4px;background:#94BBE4}
.h-root .ws-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px;margin:48px 0 0;padding:0;list-style:none}
.ws-p{position:relative;overflow:hidden;isolation:isolate;display:flex;flex-direction:column;align-items:flex-start;height:100%;box-sizing:border-box;min-height:360px;padding:48px 44px;border-radius:20px}
.ws-w{background:#ffffff;border:1px solid #E6ECF4;box-shadow:0 14px 40px rgba(14,31,61,.08);color:#0E1F3D}
.ws-n{background:#0E1F3D;color:#ffffff;box-shadow:0 18px 44px rgba(14,31,61,.22)}
.ws-n::before{content:"";position:absolute;inset:0;z-index:-1;background:repeating-linear-gradient(90deg,rgba(255,255,255,.05) 0,rgba(255,255,255,.05) 1px,transparent 1px,transparent 84px);background-position:42px 0}
.ws-ic{display:inline-flex;align-items:center;justify-content:center;width:64px;height:64px;border-radius:50%;border:1.5px solid #C9DBF0;color:#1B4584}
.ws-n .ws-ic{border-color:rgba(148,187,228,.5);color:#ffffff}
.ws-t{margin:28px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:36px;line-height:1.15;color:inherit}
.ws-ph{margin:16px 0 0;font-size:17px;line-height:1.6;font-style:italic;color:#6B7C99;text-decoration:underline dashed;text-decoration-thickness:1px;text-underline-offset:4px;text-decoration-color:rgba(107,124,153,.7)}
.ws-n .ws-ph{color:#A9BCD8;text-decoration-color:rgba(169,188,216,.6)}
.h-root .ws-lk{display:inline-flex;align-items:center;gap:10px;min-height:44px;margin-top:auto;padding-top:28px;font-size:16px;font-weight:600;color:#0B66A0;text-decoration:none;border-bottom:2px solid transparent}
.h-root .ws-n .ws-lk{color:#94BBE4}
.ws-lk svg{transition:transform .2s ease}
.h-root .ws-lk:hover{border-bottom-color:currentColor}
.ws-lk:hover svg{transform:translateX(4px)}
.hw{background:#ffffff;padding:96px 0 16px}
.hw-wrap{max-width:1280px;margin:0 auto;padding:0 40px}
.hw-h2{margin:20px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:44px;line-height:1.12;letter-spacing:-.01em;color:#0E1F3D}
.h-root .hw-list{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:32px;margin:64px 0 0;padding:0;list-style:none}
.hw-s{position:relative}
.hw-s::after{content:"";position:absolute;top:27px;left:68px;width:calc(100% - 68px + 32px - 12px);height:1.5px;background:#94BBE4}
.hw-s:last-child::after{display:none}
.hw-c{display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border-radius:50%;background:#ffffff;border:2px solid #94BBE4;font-family:'DM Sans',sans-serif;font-size:20px;font-weight:600;font-variant-numeric:lining-nums;color:#0E1F3D}
.hw-t{margin:26px 0 0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:26px;line-height:1.2;color:#0E1F3D}
.hw-ph{margin:12px 0 0;font-size:16px;line-height:1.6;font-style:italic;color:#6B7C99;text-decoration:underline dashed;text-decoration-thickness:1px;text-underline-offset:4px;text-decoration-color:rgba(107,124,153,.7)}
.ar-txt{display:flex;flex-direction:column;gap:6px;min-width:0}
.ar-li{display:block;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;font-size:14px;line-height:20px;color:#C9DBF0}
.ar-li:first-of-type{margin-top:4px}
@media (max-width:1023px){
  .tb-in{padding:20px 32px}
  .ws{padding:80px 0 64px}
  .ws-wrap,.hw-wrap{padding:0 32px}
  .ws-h2,.hw-h2{font-size:40px}
  .h-root .ws-grid{gap:20px;margin-top:36px}
  .ws-p{padding:36px 30px;min-height:340px}
  .hw{padding:80px 0 8px}
  .h-root .hw-list{gap:24px;margin-top:48px}
  .hw-s::after{width:calc(100% - 68px + 24px - 12px)}
  .hw-t{font-size:22px}
}
@media (max-width:640px){
  .tb-in{padding:24px 20px;gap:16px}
  .h-root .tb-ul{flex-direction:column;width:100%;gap:12px}
  .tb-b{width:100%;box-sizing:border-box}
  .ws{padding:64px 0 56px}
  .ws-wrap,.hw-wrap{padding:0 20px}
  .ws-h2,.hw-h2{font-size:32px}
  .ws-bar{margin-top:22px}
  .h-root .ws-grid{grid-template-columns:minmax(0,1fr);gap:16px;margin-top:28px}
  .ws-p{padding:32px 24px;min-height:0}
  .ws-t{font-size:30px;margin-top:22px}
  .hw{padding:64px 0 0}
  .h-root .hw-list{grid-template-columns:minmax(0,1fr);gap:0;margin-top:36px}
  .hw-s{display:grid;grid-template-columns:56px minmax(0,1fr);column-gap:20px;align-items:start;padding-bottom:36px}
  .hw-s:last-child{padding-bottom:0}
  .hw-s::after{top:64px;left:27px;width:1.5px;height:calc(100% - 64px - 8px)}
  .hw-t{margin:12px 0 0;font-size:26px}
  .hw-ph{grid-column:2;margin-top:8px}
}
"""
def trust_html(ic):
    b=''.join('<li class="tb-b"><span class="tb-ic">%s</span><span class="tb-t">%s</span></li>'%(ic("shield",20,1.7),t) for t in ("Law Society of Kenya","East Africa Law Society"))
    return '''  <!-- Trust bar -->
  <section class="tb nv" aria-label="Professional memberships">
    <div class="tb-in">
      <div class="tb-l">Professional Memberships</div>
      <ul class="tb-ul">%s</ul>
    </div>
  </section>
''' % b
def who_html(ic):
    arrow=ic("arrow",20,2)
    return '''  <!-- Who we serve -->
  <section class="ws" aria-labelledby="ws-title">
    <div class="ws-wrap">
      <div class="nv">
        <div class="ws-eyebrow">WHO WE SERVE</div>
        <h2 class="ws-h2" id="ws-title">Individuals and Corporations</h2>
      </div>
      <ul class="ws-grid">
        <li class="nv"><div class="ws-p ws-w"><span class="ws-ic">%s</span><h3 class="ws-t">Individuals</h3><p class="ws-ph">[Short description to come from the firm]</p><a class="ws-lk" href="Areas.dc.html"><span>View Areas of Practice</span>%s</a></div></li>
        <li class="nv"><div class="ws-p ws-n"><span class="ws-ic">%s</span><h3 class="ws-t">Corporations</h3><p class="ws-ph">[Short description to come from the firm]</p><a class="ws-lk" href="Areas.dc.html"><span>View Areas of Practice</span>%s</a></div></li>
      </ul>
    </div>
  </section>
''' % (ic("user",30,1.5),arrow,ic("building",30,1.5),arrow)
def how_html(ic):
    steps=''.join('<li class="hw-s nv"><span class="hw-c" aria-hidden="true">%d</span><h3 class="hw-t">%s</h3><p class="hw-ph">[Step description to be confirmed by the firm]</p></li>\n        '%(n,t) for n,t in enumerate(("Consultation","Advice","Representation","Resolution"),1))
    return '''  <!-- How we work -->
  <section class="hw" aria-labelledby="hw-title">
    <div class="hw-wrap">
      <div class="nv">
        <div class="ws-eyebrow">HOW WE WORK</div>
        <h2 class="hw-h2" id="hw-title">Our Approach</h2>
      </div>
      <ol class="hw-list" aria-label="Our approach in four steps">
        %s</ol>
    </div>
  </section>
''' % steps
