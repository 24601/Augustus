# Augustus 0.8.0 publication — 2026-09-26

Authorized by Basit: “Publish and update our listings on awesome lists, etc”.
The [development acceptance](2026-09-26-trainer-journeys/README.md) remains
historical; publication does not change its proxy/fixture evidence limits.

## Published surfaces

| Surface | Read-back |
| --- | --- |
| Release commit | [94a43ad](https://github.com/24601/Augustus/commit/94a43ad065d9580b31c120eea68438756db87858), merged and pushed to main |
| New annotated tag | `v0.8.0`, tag object `622a1327af991b4507ca0d9c3b152d764074fd76`, resolves to the release commit above; no existing tag moved |
| GitHub release | [v0.8.0](https://github.com/24601/Augustus/releases/tag/v0.8.0), published 2026-09-26T19:38:03Z; neither draft nor prerelease; latest-release API returns `v0.8.0` |
| Pages | [Deployment](https://github.com/24601/Augustus/actions/runs/36266560651) succeeded; Pages build API reports `built` for the exact release commit. Homepage, installation and footer name 0.8.0; release notes return successfully |
| Metadata | Both skills, marketplace, citation, changelog and install commands agree on 0.8.0. Historical release notes and audit versions remain historical |

## Verification

- `make check`: **190 tests passed**, both numerical self-tests passed, shell
  syntax passed. [Quality CI](https://github.com/24601/Augustus/actions/runs/36266561727)
  passed on Python 3.11 and 3.12.
- GitHub Pages 232 / Jekyll 3.10.0 local build and `check_site.py` passed.
  [Pages check](https://github.com/24601/Augustus/actions/runs/36266561706)
  and [Scorecard](https://github.com/24601/Augustus/actions/runs/36266561696)
  also passed.
- Claude Code 2.1.283: validated the exported candidate, then installed both
  the local export and remote `24601/Augustus@v0.8.0` in separate scratch
  configurations. Inventory: **two skills, zero agents/hooks/MCP/LSP servers**.
- Skills CLI 1.7.0: remote pinned URL discovery found both skills; an isolated
  Codex-targeted install copied both. Telemetry was disabled for these checks.
- Both remote installation trees contained the same **30 files**, byte-for-byte,
  as the tagged skill export. Normal user plugin settings were not modified.
- Chromium rendered the deployed homepage/install and release notes at 1280px
  and 390px widths, DPR 2. Inspected screenshots; document width equaled viewport
  width. Desktop code blocks scroll internally; narrow commands wrap. The code
  block accepted keyboard focus, and activating the skip link focused `main`.
  These are browser viewport checks, not physical-device testing.

Only version metadata changed in the installed skills after the executed
development acceptance. No new model/paid-provider evaluation was performed for
publication. Implicit activation and benefit versus an unassisted agent remain
unmeasured.

## Permission limit

Updating the repository About description through `gh repo edit` returned
**HTTP 403: Resource not accessible by integration**. Read-back confirmed the
previous description and correct homepage were unchanged. No account/security
settings or alternative credentials were changed. README and Pages do describe
the trainer. The remaining optional About description is:

> Agent skills for designing, training, evaluating and improving application-specific
> decision systems. Primitive/model selection, data assembly, export/reload and
> bounded hill climbing. TypeSafe Jev is the default hosted exemplar; independent
> of TypeSafe.

Third-party listings are a separate operation: maintainer acceptance and crawler
refresh are not implied by this release's publication.
