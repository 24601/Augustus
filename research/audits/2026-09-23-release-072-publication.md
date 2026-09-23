# 0.7.2 publication receipt — 2026-09-23

Read-back after publishing. The pre-release
[acceptance record](2026-09-23-release-072.md) stays as written.

| Surface | Read-back |
| --- | --- |
| Changes | [#104](https://github.com/24601/Augustus/pull/104) guidance fix; [#105](https://github.com/24601/Augustus/pull/105) release surfaces, merge commit `30b60338ee8fc065162969ffeeb707f819173509` |
| Tag | `v0.7.2` is annotated tag object `98f94e58`, pointing at `30b6033`. No tag was moved |
| GitHub release | [v0.7.2](https://github.com/24601/Augustus/releases/tag/v0.7.2), published 2026-09-23T18:22:15Z. Not a draft or prerelease. `releases/latest` returns `v0.7.2` |
| Pages | Build `built` for `30b6033`. The homepage hero, "Current release" and footer link `release-notes-v0.7.2.html` (HTTP 200) |
| Pinned Claude Code install | Fresh `CLAUDE_CONFIG_DIR`: `marketplace add 24601/Augustus@v0.7.2`, then install. `details` reports `augustus 0.7.2` with one skill and no agents, hooks, MCP or LSP servers. The cached `optimizer-integration.md` contains the terms check |
| Pinned Skills CLI discovery | `npx skills add https://github.com/24601/Augustus/tree/v0.7.2/.agents/skills/augustus --list` lists one skill at `v0.7.2`. This is discovery only |

Release notes were written after the final review and match the merged skill
text.
