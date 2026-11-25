@echo off
REM Usage: push-to-github.bat https://github.com/YOUR-USER/YOUR-REPO.git
REM Create the empty repository on GitHub first (no README, no .gitignore).
set URL=%1
if "%URL%"=="" set /p URL=GitHub repository URL: 
cd /d "%~dp0"
if not exist .git git init -b main
git add -A
git commit -m "ASW Law Advocates LLP website redesign"
git remote remove origin 2>nul
git remote add origin %URL%
git branch -M main
git push -u origin main
echo Done.
