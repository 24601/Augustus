# Augustus 0.8.0 listing receipt — 2026-09-26

**Result: two directory correction requests queued; six checked fork branches
pushed, but GitHub PR creation and the skills.sh issue follow-up are blocked by
credential permissions. No new 0.8.0 listing correction is confirmed accepted.**

Basit authorized this work through the release coordinator. Only this receipt
changes in Augustus; release, metadata and site changes belong to the parent.
Evidence was read on September 26, approximately 19:27–19:45 UTC, using GitHub
API/source reads, public pages and browser form read-back. See the
[execution thread](https://ampcode.com/threads/T-01a0df33-6750-7529-b881-6a5cacd94682)
for tool receipts, inspected confirmation screenshots and the browser recording.

The [v0.8.0 release](https://github.com/24601/Augustus/releases/tag/v0.8.0)
was independently verified non-draft, published at 19:38:03 UTC, before it was
linked in attempted PR bodies. Its
[two packaged skills](https://github.com/24601/Augustus/tree/v0.8.0/.agents/skills)
are the primary capability evidence. Copy describes application-specific
primitive/base-model/method selection, data assembly, fitting, export/reload,
bounded improvement and independent evaluation. Jev remains the default hosted
exemplar, not a general model being reproduced; no production-benefit guarantee
or bundled live Jev client is claimed. Rules and no-training outcomes remain valid.

## Repository listings

All six previous corrections were closed and accepted, with their wording
present in current upstream source. There were no open Augustus PRs to amend.
Therefore, one replacement correction branch per accepted entry was prepared.
Existing categories, names and repository links were retained. Current
CONTRIBUTING files were read before editing.

| Listing / earlier accepted correction | New branch commit and exact review comparison | Changed surface / checks | New status |
| --- | --- | --- | --- |
| Hellogumbo [#76](https://github.com/hellogumbo/awesome-jev/pull/76), closed/unmerged but maintainer explicitly applied it to main | [Commit](https://github.com/24601/awesome-jev-hellogumbo/commit/eead6069ae8370794072572c3c3c24c09bf8000c); [compare](https://github.com/hellogumbo/awesome-jev/compare/main...24601:awesome-jev-hellogumbo:update-augustus-080) | Only `data/projects.json` description; category `agents` retained; `npm run validate`: 1102 entries valid | Pushed; PR creation blocked |
| Yibie [#203](https://github.com/yibie/awesome-jev/pull/203), merged September 24 | [Commit](https://github.com/24601/awesome-jev-1/commit/59d9246e5376ab46218f92c6d69998b410fba4d1); [compare](https://github.com/yibie/awesome-jev/compare/main...24601:awesome-jev-1:update-augustus-080) | Category source and generated README; `scripts/build-readme.py`, tag audit and 26 unit tests passed | Pushed; PR creation blocked |
| AnotiaWang [#69](https://github.com/AnotiaWang/awesome-jev/pull/69), merged September 24 | [Commit](https://github.com/24601/awesome-jev/commit/69aa56ce650b499dbc0f81bfc089130f408133b3); [compare](https://github.com/AnotiaWang/awesome-jev/compare/main...24601:awesome-jev:update-augustus-080) | Paired English/Chinese entries, same position, explicit unofficial status, no trailing period; diff check passed | Pushed; PR creation blocked |
| AbdelStark [#128](https://github.com/AbdelStark/awesome-typesafe-jev/pull/128), merged September 24 | [Commit](https://github.com/24601/awesome-typesafe-jev/commit/7b2696559a9bd6187e34d460d72ec502ff99f971); [compare](https://github.com/AbdelStark/awesome-typesafe-jev/compare/main...24601:awesome-typesafe-jev:update-augustus-080) | README only; `scripts/check.py`: 322 external links, 228 community entries, all structural checks passed; generated artifacts left to maintainer | Pushed; PR creation blocked |
| Cobanov [#95](https://github.com/cobanov/awesome-jev/pull/95), merged September 23 | [Commit](https://github.com/24601/awesome-jev-cobanov/commit/09614748665304a9d4da06be484411662607d67c); [compare](https://github.com/cobanov/awesome-jev/compare/main...24601:awesome-jev-cobanov:update-augustus-080) | Only existing Guides and cookbooks bullet; diff check passed | Pushed; PR creation blocked |
| Anil-matcha [#77](https://github.com/Anil-matcha/awesome-jev-by-typesafe/pull/77), merged September 23 | [Commit](https://github.com/24601/awesome-jev-by-typesafe/commit/3dfa0de677666aee0f9fda796354be21f6469a46); [compare](https://github.com/Anil-matcha/awesome-jev-by-typesafe/compare/main...24601:awesome-jev-by-typesafe:update-augustus-080) | Existing community-implementation paragraph only; all 11 unit tests passed | Pushed; PR creation blocked |

All fork branches are named `update-augustus-080`. Each push was read back with
`git ls-remote` and GitHub's commit API, including the complete changed-file
patches. No fork default branch was changed. All six `gh pr create` attempts
returned `Resource not accessible by integration`; Hellogumbo's REST fallback
also returned HTTP 403. Subsequent PR queries returned no matching PRs. The
browser had no signed-in GitHub session, so it could not supply an authenticated
fallback. No permissions, accounts or credentials were changed.

The prepared PR bodies disclosed affiliation, substantial AI assistance and
maintainer authorization without claiming human review. To finish submission,
use an authorized GitHub session with external PR creation permission, recheck
for duplicates, and open each existing comparison above; do not recreate patches
or reopen the old accepted PRs. Suggested title: “Update Augustus entry for two
application-specific skills.” Include the release/skills links, scope/checks
from the table, limitations above and the AI-assistance disclosure.

## Directory requests and blocked surfaces

| Surface / exact URL | Action and read-back | Status |
| --- | --- | --- |
| [Jevusers submission form](https://jevusers.com/submit), existing [apps card](https://jevusers.com/apps) | Submitted once, explicitly “EXISTING-RECORD CORRECTION, not a new registration,” with full two-skill copy, limitations, public source and authorized AI disclosure; optional email blank. Read-back: “Thanks! It's in the review queue and will be checked by hand.” | Open manual review; no correction acceptance established |
| [Jevusers former project page](https://jevusers.com/p/24601-augustus) and [API](https://jevusers.com/api/projects) | Project page returned 404; exact full_name absent from the 252-project API snapshot generated 19:36:27.575 UTC, while `/apps` still displayed the older placement-oriented entry and “in Top 100” badge. Included both identities in the one correction request | Existing apps entry confirmed; tracked-page availability unresolved |
| [Shipwithjev existing card](https://www.shipwithjev.com/builds/augustus), [submission route](https://www.shipwithjev.com/submit) | Maintainer rules say updates go in a new post. Submitted once for the existing canonical repository, title Augustus, type Skills, category Tools & apps, existing author identity, and description explicitly starting “Existing-card correction.” Cost, latency and contact blank. Read-back: “RECEIVED · № 0061”, “Your request is received”, filed in queue | Open request 0061; not a new accepted listing |
| [Skills issue #2286](https://github.com/vercel-labs/skills/issues/2286) | Existing issue open with zero comments. Attempted one follow-up comment; HTTP 403 `Resource not accessible by integration`. Read-back still zero comments. No duplicate issue or install-tracking command | Open old issue; new follow-up blocked |
| [V-modal source](https://github.com/v-modal/awesome-jev-tools), [curation guide](https://github.com/v-modal/awesome-jev-tools/blob/main/.github/workflows/curation_skills.md) | Root still contains README but no categories, CONTRIBUTING or generator; guide still directs source-category edits and generated README. No unambiguous authoritative editing surface established; no correction submitted | Blocked on maintainer clarification |
| [Mabodx generated entry](https://github.com/mabodx/awesome-jev#readme) | Still says “Agent skill: design judgment-assisted systems with TypeSafe Jev (System One).” No generated README edit; Jevusers correction above is the upstream request | Awaiting upstream correction/regeneration, not guaranteed propagation |
| [Made with Jev tools card](https://madewithjev.com/tools), [submit](https://madewithjev.com/submit), [owner contact](https://madewithjev.com/sponsors/rules) | Existing card still says “An agent skill for designing systems around Jev’s judgments.” New-listing form is now free but only accepts a link, not correction text. Owner DM is documented; no existing-card self-edit route was established. Did not submit the same link again or send a DM | Blocked on an appropriate correction route/authenticated contact; no payment made |

Shipwithjev's description field truncated the first long draft. This was caught
by pre-submit value read-back and replaced before submitting with the complete
175-character value:

> Existing-card correction: augustus + augustus-train skills for task-specific model selection, data, fit/export/reload, bounded improvement and independent evals; Jev exemplar.

## Skills indexing: observed state, not claimed success

- [Snyk](https://www.skills.sh/24601/augustus/augustus/security/snyk) now shows
  **Pass, LOW, No issues detected**, analyzed September 24 at 10:02 AM (display
  timezone unspecified). W014 no longer reproduces. This predates 0.8.0 and is
  not evidence that the new release was audited.
- The [augustus page](https://www.skills.sh/24601/augustus/augustus) renders older
  skill text. The [augustus-train page](https://www.skills.sh/24601/augustus/augustus-train)
  displays **404: “augustus-train isn’t available in this repository.”** The
  published [train SKILL.md](https://github.com/24601/Augustus/blob/v0.8.0/.agents/skills/augustus-train/SKILL.md)
  exists. Cause and crawler refresh timing remain unknown.
- The blocked follow-up asked maintainers to re-index the existing repository
  and audit current tagged skills, explicitly distinguishing the resolved old
  Snyk warning from missing new-skill indexing. Post that update to #2286 once
  comment permissions are available; do not create another issue or claim a
  crawler refresh has occurred.

## Boundaries and local verification

[Fatwang2 #151](https://github.com/fatwang2/awesome-jev/pull/151) remains closed
and unmerged; [Logicrw #57](https://github.com/logicrw/awesome-jev-projects/issues/57)
remains closed as not planned. Neither was reopened. No paid outreach, account
changes, historical-data rewrites, duplicate registrations or default-branch
pushes were made. A form receipt means queued review, not acceptance or growth.

`make check` passed: repository quality checks, 190 tests, both self-tests and
shell syntax. Its first invocation found PyYAML missing; installing the pinned
`requirements-dev.txt` dependency resolved that environment failure. External
checks are listed above; they establish patch validity, not maintainer acceptance.
