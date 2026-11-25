#!/usr/bin/env bash
# Usage: ./push-to-github.sh https://github.com/YOUR-USER/YOUR-REPO.git
# Create the empty repository on GitHub first (no README, no .gitignore).
set -e
URL="${1:-}"
if [ -z "$URL" ]; then read -r -p "GitHub repository URL: " URL; fi
cd "$(dirname "$0")"
[ -d .git ] || git init -b main
git add -A
git commit -m "ASW Law Advocates LLP website redesign" || echo "Nothing new to commit"
git remote remove origin 2>/dev/null || true
git remote add origin "$URL"
git branch -M main
git push -u origin main
echo "Done. Pushed to $URL"
