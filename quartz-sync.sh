#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

if [[ "${1:-}" == "--check" ]]; then
  if [[ -n "$(git status --porcelain)" ]]; then
    echo "sync-needed"
    git status --porcelain
    exit 1
  fi
  echo "clean"
  exit 0
fi

if [[ -z "$(git status --porcelain)" ]]; then
  echo "No changes to sync."
  exit 0
fi

msg="${1:-}"
if [[ -z "$msg" ]]; then
  ts="$(date '+%Y-%m-%d %H:%M')"
  msg="Quartz sync: $ts"
fi

npm -s run quartz -- sync -m "$msg"
