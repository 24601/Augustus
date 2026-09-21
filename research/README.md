# JEV research archive — refresh hourly

All research on TypeSafe AI's Jev / System One models lives here so hourly
refreshes diff against a known baseline instead of re-discovering the world.

- `sources.json` — every source pulled, with type + retrieval date + note.
- `notes.md` — distilled findings (contracts, recipes, ecosystem, gaps).
- `refresh-log.md` — dated log of each refresh pass and what changed.
- `changelog-hourly.md` — uniqueness-lock dump after v0.3.0 (not release
  notes; see root `CHANGELOG.md`, `docs/release-notes-v0.5.1.md`, and
  `docs/release-notes-v0.5.0.md`).
- `archive/hourly/YYYY-MM-DDTHH/` — raw scan dumps for that UTC hour
  (X theme digest + `topic:jev` JSON when a live scan lands).
- `archive/curriculum/` — attached research briefs folded into the skill
  (formal-methods × System One, mental-models across domains, source
  list). Provenance; the skill cards are the doctrine.
- `revisit-checklist.md` — since-last-look protocol. Treat revisit HIGH
  like novel HIGH. Material change vs star-noise. How densify cards
  update prior notes without inventing equivalence.
- `revisit_fingerprints.json` — last-look snapshots (`default_sha`,
  `pushed_at`, `description_hash`, `release_tag`) so hourly can diff.
- `revisit_fingerprints.py` — offline classifier. `--self-test` does
  not fetch the network. SHA move is not a replica.

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

Hourly dumps (2026-09-18T14): when a live X+GH scan is provided, archive it
verbatim under `archive/hourly/` before distilling into notes.md. Do not
treat X ECE/latency claims as Contract until reproduced.

Revisit / since last look (2026-09-20 standing order): already-catalogued
repos are not done. Hourly diffs fingerprints against the last look.
Material change (README / API / release / calibration claim / serving
port / bench rewrite) is revisit HIGH: densify the prior `notes.md`
section, do not mint a sibling first sighting, do not invent
equivalence. Star-noise (stars / likes / forks alone) is a pulse, not
a fold. Hourly fold prompts must treat revisit HIGH like novel HIGH
for Augustus. `notes.md` §122.

Revisit / since-last-look lock: catalogued repos are not done; store fingerprints default_sha, pushed_at, description_hash, release_tag; material change is README/API/release/calibration claim/serving port/bench rewrite; star-noise is stars/likes/forks alone; densify the prior notes section, do not mint a sibling first sighting; do not invent equivalence; SHA move is not a replica; treat revisit HIGH like novel HIGH for Augustus; notes.md §122
