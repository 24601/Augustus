# JEV research archive — refresh hourly

All research on TypeSafe AI's Jev / System One models lives here so hourly
refreshes diff against a known baseline instead of re-discovering the world.

- `sources.json` — every source pulled, with type + retrieval date + note.
- `notes.md` — distilled findings (contracts, recipes, ecosystem, gaps).
- `refresh-log.md` — dated log of each refresh pass and what changed.

Method (2026-09-18, UTC): built-in web search + direct docs reads
(docs.typesafe.ai via llms.txt, GitHub READMEs, launch coverage, X posts via
web index). Direct `research_api` calls to Tavily/Exa failed with a plugin
body-serialization bug (providers received a JSON string instead of an object;
Tavily HTTP 422, Exa HTTP 400 `INVALID_REQUEST_BODY`), and X/XAI credentials
are not configured — so X coverage comes from the web index, not the X API.
Retry the provider APIs from `scripts/refresh-jev-research.sh` once fixed.

Freshness rule: Jev launched 2026-09-15/16. Anything about Jev older than
~2026-09-11 is a miss. Re-verify prices, limits, model aliases, and star
counts every pass — they move without notice while GPU capacity lands.

Method fix (2026-09-18): the first census sorted `gh search repos` by stars
with --limit 40, which silently cut the 1-star tail — including two MCTS+Jev
implementations with "jev" in the name. Rule going forward: paginate all
result pages, sort by updated/created, never by stars alone.
