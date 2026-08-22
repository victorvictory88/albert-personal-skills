#!/bin/zsh
set -euo pipefail

repo_root="${0:A:h}"
repo_name="${1:-albert-personal-skills}"
gh_bin="$(command -v gh 2>/dev/null || true)"

if [[ -z "$gh_bin" ]]; then
  print "Downloading GitHub's portable command-line client."
  python3 "$repo_root/tools/install_gh.py" --destination "$repo_root/.local-tools/gh"
  gh_bin="$repo_root/.local-tools/gh"
fi

if ! "$gh_bin" auth status >/dev/null 2>&1; then
  print "GitHub needs browser authorization. Follow the prompts that open next."
  "$gh_bin" auth login --web --git-protocol https
fi

"$repo_root/update.sh"

github_login="$("$gh_bin" api user --jq .login)"
github_name="$("$gh_bin" api user --jq '.name // .login')"
github_id="$("$gh_bin" api user --jq .id)"
repo_slug="${github_login}/${repo_name}"
git -C "$repo_root" config user.name "$github_name"
git -C "$repo_root" config user.email "${github_id}+${github_login}@users.noreply.github.com"
git -C "$repo_root" add --all
if ! git -C "$repo_root" rev-parse --verify HEAD >/dev/null 2>&1; then
  git -C "$repo_root" commit -m "Initial selected skills backup"
elif ! git -C "$repo_root" diff --cached --quiet; then
  git -C "$repo_root" commit -m "Update selected skills $(date +%F)"
fi

if git -C "$repo_root" remote get-url origin >/dev/null 2>&1; then
  print "A GitHub remote already exists. Pushing the current main branch."
  git -C "$repo_root" push -u origin main
elif "$gh_bin" repo view "$repo_slug" >/dev/null 2>&1; then
  print "Connecting the existing private GitHub repository."
  git -C "$repo_root" remote add origin "https://github.com/${repo_slug}.git"
  git -C "$repo_root" push -u origin main
else
  "$gh_bin" repo create "$repo_name" --private --source "$repo_root" --remote origin --push
fi
