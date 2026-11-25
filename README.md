# ASW Law Advocates LLP website

Production static site for ASW Law Advocates LLP (Nairobi). Plain HTML, CSS and a little vanilla JS. No framework, no bundler, no build step. Deploys on Vercel as it is.

The site is currently **sample copy for client review** and is set to `noindex`. See "Before launch" below.

## Project organisation

```
index.html                          Home
about.html                          About Us
areas-of-practice.html              Areas of Practice (ids: dispute, commercial, procurement, property, private, employment)
insights.html                       Insights
article-know-about-industrial-laws.html
article-flexibility-of-marriage-in-us.html
contact.html                        Contact (form + Google Maps embed)
faq.html                            FAQ with filter pills
privacy.html, terms.html            Minimal legal pages (sample copy)
404.html                            Not found page
css/styles.css                      Shared styles: base, header, footer, type system, interactions
css/pages/*.css                     Page specific styles (home, about, areas, insights, article, contact, faq, legal)
js/main.js                          All behaviour (vanilla JS)
assets/                             Images, logos, favicon (compressed, with width and height in the markup)
robots.txt, vercel.json             Crawler rules and Vercel config
source/                             Original Claude Design artboards (.dc.html) and canvas.json, kept for reference
generators/                         Scripts that produced the design source, kept for reference
tools/                              Converter and checks used to produce this static site from source/
```

## Design rules

- Brand: navy `#1B4584`, deep navy `#0E1F3D`, sky `#94BBE4`, link blue `#0F74B5`, off-white `#F2F2F0`. Marcellus for headings, DM Sans for body (Google Fonts, `display=swap`, preconnect).
- Type scale (desktop / tablet / phone): H1 56/44/34, H2 44/36/30, H3 28/24/22, body 18/17/16, eyebrows 13/12.
- Mobile first. Breakpoints at about 640px and 1024px, fluid in between.
- Never use em dashes, en dashes, spaced hyphens or decorative dash lines in copy.

## What `js/main.js` does

Mobile menu, accordions (buttons with `aria-expanded`), scroll snap carousels with counter and prev/next, FAQ filter pills, sticky anchor bar tracking on Areas of Practice, fade up with IntersectionObserver, the floating WhatsApp button (`https://wa.me/254788685911`, hidden over the Home hero, shown after scrolling past it), and the contact form (validation, honeypot, `fetch` submit). `prefers-reduced-motion` is respected throughout. The carousel depth effect and the Home timeline progress use native scroll driven CSS animation where supported, with a JS fallback for the timeline elsewhere.

## Run locally

```
npx serve .
```

Then open the printed address. Any static server works, for example `python3 -m http.server`.

## Deploy on Vercel

Import the repository in Vercel and use:

- Framework Preset: **Other**
- Build Command: leave empty
- Output Directory: leave empty (the repository root is served)
- Install Command: leave empty

`vercel.json` sets `cleanUrls: true` (so `/about.html` is served as `/about`), `trailingSlash: false`, long cache headers for `/assets`, and short revalidating cache for `/css` and `/js`.

## Before launch

1. **Remove noindex.** Every page has `<meta name="robots" content="noindex, nofollow">` with a comment above it, `robots.txt` disallows everything, and `vercel.json` sends an `X-Robots-Tag: noindex, nofollow` header. Remove all three when the firm approves the copy.
2. **Contact form.** In `contact.html` replace `YOUR_FORM_ID` in the form action (`https://formspree.io/f/YOUR_FORM_ID`) with the real Formspree form id. While the placeholder is in place, the page only previews the success message and sends nothing.
3. Replace the sample copy, the shared placeholder portrait and the sample legal pages with the firm's own content.
4. Add the canonical domain to the Open Graph tags if wanted.

## Regenerating from the design source

`python3 tools/build_static.py && python3 tools/build_extras.py` regenerates the HTML and CSS from `source/` (needs Python and Pillow). `python3 tools/check_links.py` checks internal links, anchors, alt text, the noindex tag and the dash rule. This is optional: the committed files are the site.
