#!/usr/bin/env bash
# Hourly refresh during US business hours (Mon-Fri 13:00-21:00 UTC = 9am-5pm ET).
# Runs the deterministic checks, re-sweeps GitHub for NEW jev repos not yet in the
# archive, clones them, appends refresh-log, and pushes any repo changes to main.
set -u
cd "$(dirname "$0")/.."
scripts/refresh-jev-research.sh

# GitHub re-sweep: repos mentioning jev created in last 3 days, not yet archived.
ARCHIVE=/home/user/workspace/jev-archive
page=1
while :; do
  resp=$(curl -s --max-time 30 "https://api.github.com/search/repositories?q=jev+created:%3E2026-09-15&sort=updated&per_page=100&page=$page")
  names=$(echo "$resp" | jq -r '.items[]?.full_name' 2>/dev/null)
  [ -z "$names" ] && break
  for n in $names; do
    d="$ARCHIVE/$(echo "$n" | tr '/' '_')"
    if [ ! -d "$d" ]; then
      git clone --quiet --depth 1 "https://github.com/$n" "$d" 2>/dev/null \
        && echo "$n" >> "$ARCHIVE/repos.txt" \
        && echo "- NEW CLONE: $n" >> "$ARCHIVE/analysis/new-since-last-pass.md"
    fi
  done
  total=$(echo "$resp" | jq -r '.total_count // 0')
  [ "$page" -ge $(( (total + 99) / 100 )) ] && break
  page=$((page+1))
  [ "$page" -gt 10 ] && break
done

if ! git diff --quiet || [ -n "$(git status --porcelain research)" ]; then
  git add -A && git commit -q -m "hourly refresh $(date -u +%FT%TZ)" && git push -q origin main
fi
