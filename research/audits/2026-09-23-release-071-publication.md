# 0.7.1 publication receipt — 2026-09-23

Read-back after publishing. The pre-release
[acceptance record](2026-09-23-release-071.md) stays as written.

| Surface | Read-back |
| --- | --- |
| Release PR | [#101](https://github.com/24601/Augustus/pull/101), squash-merged at head `74244292`; merge commit `3c96a61d09a40facd08a4c68879d1cbe67008baa` |
| Tag | `v0.7.1` is annotated tag object `737078f3`, pointing at `3c96a61`. No existing tag was moved |
| GitHub release | [v0.7.1](https://github.com/24601/Augustus/releases/tag/v0.7.1), published 2026-09-23T17:45:19Z. Not a draft or prerelease. `releases/latest` returns `v0.7.1` |
| Pages | Build `built` for `3c96a61`. Homepage hero, "Current release" and footer link `release-notes-v0.7.1.html`, and the notes page returns 200. The `/06` label is live. Font pages are absent from the sitemap |
| Pinned Claude Code install | Fresh `CLAUDE_CONFIG_DIR`: `claude plugin marketplace add 24601/Augustus@v0.7.1` then `install`. `details` reports `augustus 0.7.1` with one skill and no agents, hooks, MCP or LSP servers. The cached `SKILL.md` has `version: 0.7.1` |
| Pinned Skills CLI discovery | `npx skills add https://github.com/24601/Augustus/tree/v0.7.1/.agents/skills/augustus --list`, with HOME and the npm cache in scratch and telemetry off, lists one skill. This is discovery only, not an activation test |
| About metadata | The description and homepage are unchanged and on-mission. With maintainer authorization, topics now drop `system-one-models` and `structured-output` and add `llm-evaluation` and `prompt-optimization` (20 total) |

## Correction after tagging

The release-notes page tagged in `v0.7.1` summarized four rules in their
pre-review wording:

- deferral "under calibrated mass" using 1 − top mass;
- audit sampling without inverse weights;
- an unconditional router bound;
- weight-only one-off sensitivity.

The tagged skill already contained the corrected rules from `9c543f0`. The
GitHub release body was corrected before publication. The Pages copy of the
notes is corrected on `main` in this change, with a visible note. The tag was
not moved.

## Not claimed

Published availability is not indexing, implicit activation in crowded
listings, or user benefit. The skills.sh audits and third-party listing
corrections are tracked separately.
