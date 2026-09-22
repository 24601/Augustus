# Existing-listing positioning audit — 2026-09-22

## Decision

**Yes: prepare targeted updates to existing accepted listings.** Augustus's
current find/build/evaluate/improve mission is materially broader than the
placement-advice descriptions still displayed. Amend the existing Hellogumbo
PR, then propose five small description-only PRs to confirmed accepted source
entries. Do not resubmit Augustus indiscriminately, reopen runtime-only
catalog rejections, or separately patch every generated copy.

This audit authorizes no external action. All PR creation, existing-PR edits,
issue filing, correction forms, and maintainer contact require the user's
subsequent authorization. Nothing was submitted, posted, paid for, or changed
outside this report.

## Scope and provenance

- Reviewed current README, CHANGELOG, SKILL, AGENTS, CONTRIBUTING, research
  protocol and fold instructions. Local candidate was
  `9b4d86d96c92656a97af521c9ed5a5ccad905034` (0.7.0). The
  [latest-release endpoint](https://api.github.com/repos/24601/Augustus/releases/latest)
  still returned v0.6.0 during this audit: use newly published 0.7.0 evidence
  only after the coordinator verifies publication. The
  [public repository metadata](https://api.github.com/repos/24601/Augustus)
  already described building, evaluating, improving, composition, eval harnesses,
  bounded hill climbing, and Jev as the default hosted exemplar.
- Earlier discoverability notes supplied leads only. Current external source
  files, PR/issue states, contribution documents, and directory pages were read
  afresh using GitHub's read-only API and public HTTP/web retrieval.
- GitHub code search for the exact repository identity returned five indexed
  files. Author-scoped external PR search returned 45 results with
  `incomplete_results=false`; seven were relevant awesome-list submissions or
  updates. Issue searches, two public web queries, ten candidate repository
  READMEs, and the directory pages below supplemented that search. This is a
  bounded audit, not a census of GitHub, forks, translations, private catalogs,
  or all historical mentions. Search matches on unrelated issue number 24601
  were discarded.
- Eight repository listings were confirmed directly. That is not eight
  independent endorsements or eight user-acquisition channels: some are
  generated/copied. Jevusers displays eleven source-list mentions, which does
  not establish that this audit inspected all eleven.
- Requested execution identity: GPT-6 Astra, xhigh. The task configuration
  requests that identity; no tool response in this audit independently attests
  the backend model or effective reasoning setting. No agents were delegated.

## Confirmed repository entries

Quoted wording below is an exact short excerpt; the linked source contains
the complete current entry. Surrounding descriptions are paraphrases. Source
links pin the revision observed at review, not a claim that it will remain HEAD.

| Repository and exact source | Current positioning | Registration / current state | Recommendation |
| --- | --- | --- | --- |
| [yibie/awesome-jev: categories/agent-decisions.md:24](https://github.com/yibie/awesome-jev/blob/ba176b4d62a720ce4e8616014b6ff8f4ad2c88dc/categories/agent-decisions.md#L24); generated README:242 | “agent skill that maps Choice, Score, and Noul onto classical methods”; placement, composition, question diagnosis, falsification | [PR #4](https://github.com/yibie/awesome-jev/pull/4) merged September 18; entry present | P1: description-only source-category PR and regenerate README |
| [AnotiaWang/awesome-jev: README.md:174](https://github.com/AnotiaWang/awesome-jev/blob/06c6f5422b215d4fcefb94c31f598a3939ac5dc7/README.md#L174) and [README_zh.md:174](https://github.com/AnotiaWang/awesome-jev/blob/06c6f5422b215d4fcefb94c31f598a3939ac5dc7/README_zh.md#L174) | “Design-judgment skill”; both languages emphasize mapping typed judgments onto classical methods | [PR #7](https://github.com/AnotiaWang/awesome-jev/pull/7) merged September 18; both entries present | P1: one bilingual description-update PR |
| [AbdelStark/awesome-typesafe-jev: README.md:332](https://github.com/AbdelStark/awesome-typesafe-jev/blob/1b3687c533ed321bf47e6e94746c57a658101d0a/README.md#L332) | “Agent skill for choosing where typed judgments fit beside code, policy, and generation”; includes offline threshold evaluator | [PR #82](https://github.com/AbdelStark/awesome-typesafe-jev/pull/82) merged September 21; entry present | P1: README-only description update; maintainers regenerate derived resources |
| [cobanov/awesome-jev: README.md:305](https://github.com/cobanov/awesome-jev/blob/96cac8896a74638c2bb6cb299b58f931c454d449/README.md#L305) | “Design-judgment skill for the decision-model class”; calls Jev “the dominant exemplar” | [PR #59](https://github.com/cobanov/awesome-jev/pull/59) merged September 21; currently in Guides and cookbooks | P1: correct mission and change dominant to default hosted exemplar; retain current shelf |
| [Anil-matcha/awesome-jev-by-typesafe: README.md:395](https://github.com/Anil-matcha/awesome-jev-by-typesafe/blob/057b898aae7b7fadf67263ff44f423326184dc77/README.md#L395) | “takes the desired software behavior as state”; design decomposition, exact effects and falsification; explicitly independent | [PR #9](https://github.com/Anil-matcha/awesome-jev-by-typesafe/pull/9) closed/unmerged by GitHub status, but **accepted by manual application**, confirmed by [maintainer comment](https://github.com/Anil-matcha/awesome-jev-by-typesafe/pull/9#issuecomment-5726739775) and current source | P1: focused replacement paragraph; do not misclassify the closed PR as rejection |
| [v-modal/awesome-jev-tools: README.md:178](https://github.com/v-modal/awesome-jev-tools/blob/f117e0c368d6e293bf5fdf99244a1173a6dc2ae0/README.md#L178) | “Coding agents: agent skill”; same placement-oriented description as yibie | Confirmed current entry; no registration PR established | P2: update candidate, but reconcile conflicting editing guidance before submitting |
| [hellogumbo/awesome-jev: data/projects.json:7234](https://github.com/hellogumbo/awesome-jev/blob/e2014cdb35d7d699795c8ca28904e8f42568bf45/data/projects.json#L7234); generated README:775 and [awesomejev.com](https://awesomejev.com/) | “Agent skill: design judgment-assisted systems with TypeSafe Jev (System One)”; category `research` | Confirmed listing; [PR #76](https://github.com/hellogumbo/awesome-jev/pull/76) **open**, already proposes category `agents` and revised copy | P1 first: amend that PR's description/body, preserve its category correction; no duplicate PR |
| [mabodx/awesome-jev: README.md:102](https://github.com/mabodx/awesome-jev/blob/badcdf7f86e1b8b7e56f5d396876f0e76d24a0a1/README.md#L102) | “Agent skill: design judgment-assisted systems with TypeSafe Jev (System One)”; generated popularity/list-count suffix | Confirmed generated entry; no independent registration established | P3: correct upstream Jevusers data and await regeneration; avoid fragile README-only PR |

### Contribution constraints checked

- **Yibie:** [CONTRIBUTING](https://github.com/yibie/awesome-jev/blob/ba176b4d62a720ce4e8616014b6ff8f4ad2c88dc/CONTRIBUTING.md)
  makes category files authoritative and requires `scripts/build-readme.py`.
  Use one factual sentence with an industry prefix, one project per PR, and
  disclose affiliation and substantial AI assistance. Keep the entry explicitly
  a skill; do not manufacture runtime integration evidence to meet tool criteria.
- **AnotiaWang:** [CONTRIBUTING](https://github.com/AnotiaWang/awesome-jev/blob/06c6f5422b215d4fcefb94c31f598a3939ac5dc7/CONTRIBUTING.md)
  requires matching English and simplified-Chinese entries in the same position,
  concise copy, and explicit unofficial status. Single-sentence entries have no
  trailing period.
- **AbdelStark:** [CONTRIBUTING](https://github.com/AbdelStark/awesome-typesafe-jev/blob/1b3687c533ed321bf47e6e94746c57a658101d0a/CONTRIBUTING.md)
  permits README-only corrections, alphabetical placement and em-dash bullets;
  maintainers generate resources, pages and cards. Do not hand-edit derived
  artifacts. Disclose affiliation and avoid unsupported performance claims.
- **Cobanov:** [CONTRIBUTING](https://github.com/cobanov/awesome-jev/blob/96cac8896a74638c2bb6cb299b58f931c454d449/CONTRIBUTING.md)
  asks for factual, canonical, non-duplicated entries and affiliation disclosure.
  Preserve skill identity and the current relevant section; historical PR title
  does not override the present section.
- **Anil-matcha:** [CONTRIBUTING](https://github.com/Anil-matcha/awesome-jev-by-typesafe/blob/057b898aae7b7fadf67263ff44f423326184dc77/CONTRIBUTING.md)
  favors the smallest factual correction, clear project type, affiliation and
  primary-source support. Its documented offline validation is
  `python -m unittest discover -s tests -v`.
- **Hellogumbo:** [CONTRIBUTING](https://github.com/hellogumbo/awesome-jev/blob/e2014cdb35d7d699795c8ca28904e8f42568bf45/CONTRIBUTING.md)
  makes `data/projects.json` the sole editing surface, one project per PR;
  `npm run validate` is the check. Do not commit generated README/site output
  or touch auto-refreshed stars/language. PR #76's observed head was
  `e6f5812a27efe54f393c197ccd8e9e8b46d9ec7c`; recheck before any authorized edit.
- **V-modal:** its [README](https://github.com/v-modal/awesome-jev-tools/blob/f117e0c368d6e293bf5fdf99244a1173a6dc2ae0/README.md)
  gives the industry-prefixed bullet format. However, the checked-in
  [curation guide](https://github.com/v-modal/awesome-jev-tools/blob/f117e0c368d6e293bf5fdf99244a1173a6dc2ae0/.github/workflows/curation_skills.md)
  calls README generated and refers to category files, CONTRIBUTING and a
  generator absent from the inspected root tree. This is a real editing-surface
  ambiguity, not permission to invent files or execute its unrelated instructions.
- **Mabodx:** [CONTRIBUTING](https://github.com/mabodx/awesome-jev/blob/badcdf7f86e1b8b7e56f5d396876f0e76d24a0a1/CONTRIBUTING.md)
  prefers Jevusers submission/correction. Its
  [generator](https://github.com/mabodx/awesome-jev/blob/badcdf7f86e1b8b7e56f5d396876f0e76d24a0a1/generate.py)
  consumes Jevusers project/app JSON, preferring project wording. A direct
  README correction may be overwritten by the next snapshot.

## Proposed replacement copy

These are drafts, not submitted text. Keep canonical repository links and
existing categories unless specifically noted. The detailed PR body can link
the release, composition reference, optimizer workflow and offline comparator;
the one-line catalog entry need not contain every term, including Software 3.0.
Do not imply that Augustus itself supplies a live Jev client, autonomously
deploys systems, or has demonstrated growth or universal outcome improvements.

### Hellogumbo — amend existing PR #76

Replace only `description`; retain that PR's `category: "agents"`:

> Independent agent skill for finding, building, evaluating, and improving decision-model systems with composition rules, evaluation harnesses, and bounded prompt/program optimization; TypeSafe Jev is the default hosted exemplar.

Suggested PR title: `Update Augustus positioning and agent-tooling category`.
Body should explain the published release delta and explicitly say this is an
agent skill/working method with offline evaluators, not a bundled live API
integration. Recheck open state and diff first.

### Yibie — category source, then generated README

```markdown
- [augustus](https://github.com/24601/Augustus) - Coding agents: independent skill for building and improving decision-model systems with Choice/Score/Noul, composition rules, evaluation harnesses, and bounded prompt/program optimization, using TypeSafe Jev as the default hosted exemplar.
```

### AnotiaWang — paired language update

```markdown
- [augustus](https://github.com/24601/Augustus) - Independent agent skill for finding, building, evaluating, and improving decision-model systems with composition rules, evaluation harnesses, and bounded prompt/program optimization; TypeSafe Jev is the default hosted exemplar
- [augustus](https://github.com/24601/Augustus) - 独立的智能体技能，用于发现、构建、评估和改进决策模型系统，提供组合规则、评估框架和有界的提示词／程序优化方法；默认以 TypeSafe Jev 为托管模型示例
```

Place each line in its corresponding language file, not together in one file.

### AbdelStark — README only

```markdown
- [Augustus](https://github.com/24601/Augustus) — Independent agent skill for building and improving decision-model systems, with composition rules, evaluation workflows, bounded prompt/program optimization, and an offline paired-outcome evaluator; TypeSafe Jev is the default hosted exemplar.
```

### Cobanov — existing Guides and cookbooks entry

```markdown
- [Augustus](https://github.com/24601/Augustus) - Independent agent skill for finding, building, evaluating, and improving decision-model systems through composition rules, evaluation harnesses, and bounded prompt/program optimization; TypeSafe Jev is the default hosted exemplar.
```

### Anil-matcha — existing implementation paragraph

> Community implementation: [Augustus](https://github.com/24601/Augustus) equips agents to find, build, evaluate, and improve decision-model systems, including Software 3.0 workflows, using composition rules, evaluation harnesses, and bounded prompt/program optimization. TypeSafe Jev is the default hosted exemplar; exact constraints, authorization, and effects remain in code or explicit human policy. Independent agent skill with offline evaluators, not an official TypeSafe product or a bundled live Jev client.

### V-modal — after editing-surface clarification

Use the Yibie draft's industry-prefixed sentence, adapted only to its existing
name capitalization. Do not add another entry, switch provider shape names to
match a stale guide, or describe a live integration that does not exist.

## Registries and downstream pages

| Page / exact record | Confirmed current state and wording | Appropriate next action |
| --- | --- | --- |
| [Jevusers tracked project](https://jevusers.com/p/24601-augustus), [project API](https://jevusers.com/api/projects) | Exact `full_name: 24601/Augustus`, rank 198 in snapshot generated `2026-09-22T17:09:10.989Z`; summary still says “TypeSafe Jev is the dominant exemplar” and describes model-family/design coverage | P2: let corrected public metadata/source lists refresh; if summary persists, request correction of this existing record, not a new registration |
| [Jevusers apps](https://jevusers.com/apps) | Exact repository link present under Coding Agent; placement-oriented skill copy, with eleven list mentions | P2: same correction, supplying the existing project and app identities; verify both surfaces after refresh |
| [Skills directory](https://www.skills.sh/24601/augustus/augustus) | Exact owner/repo/skill page present, with install command, but preview says “No SKILL.md available for this skill”; displays 5 installs at observation | P2: reproducible preview/indexing bug report, after verifying published skill path and reproducibility; not another skill registration or a claim of native activation |
| [Made with Jev tools](https://madewithjev.com/tools) | Exact GitHub link; full short description: “An agent skill for designing systems around Jev’s judgments.” | P3: existing-card correction once a suitable free author-edit/contact route is confirmed; do not buy another listing |
| [Shipwithjev detail](https://www.shipwithjev.com/builds/augustus) | HTTP 200, matching canonical, title and repository; same short design-only description as the preceding row | P3: correct existing card after identifying its edit/contact mechanism; common ownership or a shared update pipeline was not verified |

For Jevusers, the [about page](https://jevusers.com/about) describes GitHub-based
discovery/refresh and manual corrections via [the submission form](https://jevusers.com/submit).
That documents a route; it does not prove the next run will refresh all fields.
Use the Hellogumbo description draft as replacement copy and explicitly mark a
request as an **existing-record correction**. The same upstream correction may
flow to Mabodx, but verify rather than promise propagation.

For Skills, [contact guidance](https://www.skills.sh/contact) directs bugs to
[vercel-labs/skills issues](https://github.com/vercel-labs/skills/issues). A useful
draft title is `Directory preview missing for 24601/augustus/augustus`; include
the exact directory URL, published SKILL path and revision, observed message,
date, and expected rendered content. The cause is **unknown**; do not claim an
unsupported root-path bug or promise a crawler fix. No install command was run
to inflate counts or trigger tracking.

For the two short-card sites, suggested replacement:

> Agent skill for building and improving decision-model systems with composition, evals, and bounded prompt/program optimization; Jev is the default hosted exemplar.

Made with Jev exposes a paid new-listing path; that is not proof that correcting
an existing card requires payment. Its [sponsor rules](https://madewithjev.com/sponsors/rules)
name an owner contact for questions, but a free ordinary-card editing procedure
was not established. No payment or outreach is recommended without a separate
decision and authority.

## Closed submissions and search-only mentions: do not resubmit by default

- **Fatwang2:** [PR #151](https://github.com/fatwang2/awesome-jev/pull/151) is
  closed, unmerged, as of `2026-09-22T08:33:07Z`; no entry appeared in the
  inspected current README, and proposed `entries/24601--augustus.json`
  returned 404. Its discussion distinguishes this skill from runtime Jev
  integrations. Classification: closed submission, no accepted listing
  established. Maintainer intent beyond the retrieved discussion is not
  inferred from an automated score. No description-update PR is appropriate.
- **Logicrw:** [issue #57](https://github.com/logicrw/awesome-jev-projects/issues/57)
  is closed; the [maintainer's response](https://github.com/logicrw/awesome-jev-projects/issues/57#issuecomment-5772339803)
  explicitly applies a runtime-integration boundary. The repository's
  [README](https://github.com/logicrw/awesome-jev-projects#readme) uses issues,
  not PRs, for submissions/updates. Classification: rejected for catalog
  scope, no current README listing found. Broader positioning alone does not
  resolve that mismatch. Do not reopen.
- **Search hits are not registrations:**
  [QingshungLI discovery JSON](https://github.com/qingshungLI/everything-about-jev/blob/014723d5b52db5f194d0d094103eaaf3475f1cab/data/discovery.json)
  explicitly marks this record `discovery_only`;
  [YZFly hot data](https://github.com/yzfly/awesome-jev-zh/blob/cdb8a78cb3ac4cec36ebe305b73a4e0b4f5cba21/data/hot.json#L1120)
  contains popularity/first-seen data;
  [Open-Jev's dated report](https://github.com/Zefan-Cai/Open-Jev/blob/ed45657bf726c3b77408942830e5578f99df904e/reports/community-research-20260921-broadening/github-search-2.json#L49)
  preserves a historical search description;
  [Firehorse research data](https://github.com/cinjoff/firehorse/blob/a22c83c0d4a9256d1e40491cecea4bddcaa6b89a/docs/research/jev/data/implementations.json#L33)
  is a research inventory; and
  [what-is-jev's test](https://github.com/g0runmezadam/what-is-jev/blob/45b23e98676d0ea399995db90ef46fc13b358122/tests/test_update.py#L81)
  uses the name as a repository-name fixture. Do not rewrite historical
  evidence or tests as a marketing refresh. No editorial-registration status
  was established for these hits. A closed automated discovery
  [MrJev issue #2](https://github.com/MrJev/awesome-jev/issues/2) was a search lead
  only; its entry-level disposition was not examined.

## Recommended authorized queue

1. **Publication prerequisite:** coordinator verifies 0.7.0 release, public
   README/SKILL and canonical site. Link reproducible capability evidence in
   proposed PR bodies, not unpublished local files.
2. **First wave:** amend Hellogumbo #76; submit five focused description updates
   to Yibie, AnotiaWang, AbdelStark, Cobanov and Anil-matcha. Disclose affiliation
   and AI assistance where required. No new registrations or bundled unrelated
   projects. Recheck current entry, open PRs, and rules immediately before each
   authorized mutation.
3. **Second wave:** observe Jevusers project/app refresh, then request one
   existing-record correction if needed. File a separately scoped Skills
   preview bug if still reproducible. Clarify V-modal's authoritative editing
   surface before its update.
4. **Derived / lower priority:** verify Mabodx regeneration; identify free edit
   routes for Made with Jev and Shipwithjev before requesting card corrections.
   Do not treat copied descriptions as separate high-priority PR targets.
5. **No action:** leave closed runtime-only submissions, historical snapshots,
   search inventories and fixtures unchanged.

Success means accepted source updates and verified rendered/indexed read-back.
It does **not** establish native skill discovery, installation, successful agent
activation, retention, or actual user growth. Those need separate observation.

## Verification of this audit artifact

Only this research report was added by the listing-positioning task. External
operations were read-only. Local `make check` passed, including all 88 tests,
both self-tests and shell syntax checks; the complete report diff was reviewed.
These checks validate repository integration, not
the completeness of external discovery or any future maintainer acceptance.
