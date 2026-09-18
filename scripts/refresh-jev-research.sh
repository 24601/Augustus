#!/usr/bin/env bash
# Hourly Jev ecosystem refresh. Appends a dated entry to research/refresh-log.md.
# Checks: awesome-typesafe HEAD, docs index, evals site, pinned model page.
# Deep provider searches (Exa/Tavily/Gemini) run inside the Amp thread; this
# script covers the cheap deterministic checks. Run: scripts/refresh-jev-research.sh
set -u
cd "$(dirname "$0")/.."
LOG=research/refresh-log.md
TS=$(date -u +"%Y-%m-%d %H:%M UTC")
{
  echo ""
  echo "## $TS — scheduled refresh"
  echo "- awesome-typesafe HEAD: $(git ls-remote https://github.com/AbdelStark/awesome-typesafe HEAD 2>/dev/null | cut -c1-12 || echo UNREACHABLE)"
  for u in "https://docs.typesafe.ai/llms.txt" "https://evals.typesafe.ai/" "https://openrouter.ai/typesafe/jev-1.13"; do
    code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 20 "$u" || echo FAIL)
    echo "- $u -> HTTP $code"
  done
  echo "- action: diff index/cookbook list vs research/sources.json; update notes.md + log."
} >> "$LOG"
echo "logged to $LOG"
