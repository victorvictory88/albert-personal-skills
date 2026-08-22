#!/bin/zsh
set -euo pipefail

repo_root="${0:A:h}"
source_root="${ALBERT_SKILLS_SOURCE:-/Users/albertchan/Desktop/AI/Outputs/_workspace-maintenance/Skills}"
days=120
minimum_uses=3
push_changes=false
lock_dir="$repo_root/.update-lock"

if ! mkdir "$lock_dir" 2>/dev/null; then
  print -u2 "Another skill backup update is already running."
  exit 2
fi
trap 'rmdir "$lock_dir" 2>/dev/null || true' EXIT

while (( $# > 0 )); do
  case "$1" in
    --push)
      push_changes=true
      shift
      ;;
    --days)
      days="$2"
      shift 2
      ;;
    --minimum-uses)
      minimum_uses="$2"
      shift 2
      ;;
    *)
      print -u2 "Unknown option: $1"
      exit 2
      ;;
  esac
done

export PYTHONDONTWRITEBYTECODE=1
python3 "$repo_root/tools/audit_usage.py" \
  --source "$source_root" \
  --days "$days" \
  --minimum-uses "$minimum_uses" \
  --json "$repo_root/usage.json" \
  >/dev/null
python3 "$repo_root/tools/sync_selected_skills.py" \
  --source "$source_root" \
  --usage "$repo_root/usage.json" \
  --repo "$repo_root"

if [[ "$push_changes" == true ]]; then
  if ! git -C "$repo_root" remote get-url origin >/dev/null 2>&1; then
    print -u2 "No GitHub remote exists. Run ./publish.sh first."
    exit 2
  fi
  git -C "$repo_root" add --all
  if ! git -C "$repo_root" diff --cached --quiet; then
    git -C "$repo_root" commit -m "Update selected skills $(date +%F)"
  fi
  git -C "$repo_root" push
fi

git -C "$repo_root" status --short
