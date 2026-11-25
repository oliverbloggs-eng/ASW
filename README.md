# ASW Law Advocates LLP: website redesign

Design source for the ASW Law Advocates LLP (Nairobi) website, exported from the Claude Design canvas.

## Contents
- `source/` the pages as `.dc.html` artboards (Desktop 1440, Tablet 768, Phone 390) and `canvas.json` (board layout and notes). Home, About Us, Areas of Practice, Insights, two articles, Contact Us, Frequently Asked Questions.
- `assets/` all photos and logos used by the pages (`team-portrait-current.jpg` is the shared portrait).
- `generators/` the Python scripts and CSS that generate and verify the pages (for reference or regeneration).

## Notes
- `.dc.html` files use the Claude Design runtime (`support.js`), so they open inside the Claude Design canvas, not as plain web pages. Live canvas: https://claude.ai/artifact/R7ENh9F7qRMT3iMiVjizpd
- Image paths point to `../assets/`.
- Brand: navy #1B4584, deep navy #0E1F3D, sky #94BBE4, link blue #0F74B5, off-white #F2F2F0. Marcellus headings, DM Sans body.
- All text is sample copy for review, to be confirmed by the firm.

## Push to GitHub
1. Create an empty repository on GitHub.
2. In this folder run `./push-to-github.sh https://github.com/YOUR-USER/YOUR-REPO.git` (macOS, Linux, Git Bash) or `push-to-github.bat <url>` (Windows).
   You need Git installed and to be signed in to GitHub (browser prompt, token or SSH).
