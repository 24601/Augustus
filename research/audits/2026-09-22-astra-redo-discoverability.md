# Independent redo: discoverability and rendered site

Reviewed 2026-09-22, approximately 16:07–16:22 UTC. This is a fresh review of
the files, public HTTP responses, directory records, and rendered pages. It
does not adopt the conclusions of the earlier discoverability/site audits.

## Identity, scope, and verdict

- Requested reviewer: GPT-6 Astra, xhigh. This worker was dispatched under
  that requested configuration. The available developer identity says GPT-6;
  no independent serving-model attestation or provider response metadata was
  exposed to this review. Do not turn the requested name into an attestation.
- Working branch: `refresh/2026-09-22`; HEAD and published v0.6.0 target:
  `192faf0d18d511154228af8ac40e1393567d828c`. The shared working tree contains
  other agents' 0.6.1-dev changes. This worker changed only this audit file.
- Scope: README, skill activation metadata/reference, Codex UI metadata,
  Claude marketplace paths, Pages sources/workflow, rendered-site checker
  and tests, live repository metadata/deployment, public directory presence,
  and the distinction between discovery and useful adoption.
- **Verdict: ship for the current discoverability and rendered-site scope.**
  The present site renders correctly, its key paths work, and public identity
  matches the mission. No current site defect requires holding the package.
  The checker has important bounded coverage gaps and one fragment bug;
  correct these before treating it as a broader SEO or asset-quality gate.
  This is a scope verdict, not release approval or semantic skill acceptance.

## What a new user can actually do

The README identifies an agent skill, names the concrete questions it helps
answer, offers software and non-software prompts, and explains the expected
design card. It explicitly permits a formula, checklist, or no new model.
The examples page supplies two worked design cards and a deterministic
date-comparison counterexample, labeling them illustrative rather than tested
integrations. This is enough to understand first value without obtaining a
provider key.

The installation routes are internally coherent:

| Surface | Verified current evidence | Limit |
| --- | --- | --- |
| README Skills CLI | Names repository and `--skill augustus`; explains default-branch drift | Not an exact release pin or a native activation test |
| Exact source | `git clone --branch v0.6.0 --depth 1 ...`; names `.agents/skills/augustus/` and warns that cloning alone does not install it | Agent-specific local installation remains necessary |
| Claude marketplace | Source `./.agents`, skills `./skills/augustus`, `strict: false`; version 0.6.1-dev matches local SKILL.md | This review did not run an install or alter normal plugin settings |
| Explicit invocation | README documents `/augustus:augustus` and `$augustus` | Actual invocation in a fresh native host remains a separate test |
| Skill selection | Frontmatter names classification, routing, ranking, uncertainty, placement/evaluation, and exclusions; activation reference gives examples and non-triggers | Sensible text does not measure implicit trigger recall or false activation |
| Codex UI | `agents/openai.yaml` has display name, short description, and a `$augustus` default prompt | UI metadata does not prove installation, indexing, or use |

The website has prominent installation and example links, no credential
requirement for the skill, and a feedback path. Its installation cards follow
the default branch and say so. Keeping “current release 0.6.0” on the site is
accurate while the local skill develops as 0.6.1-dev.

One improvement is worth testing rather than declaring a conversion win:
the on-page install section begins about 2,968 px down at 1440×1000 and
5,505 px down at 390×844; the first-use prompt begins about 3,333/6,085 px
down. The hero links do provide shortcuts, but the primary CTA goes to the
GitHub README instead of the on-page install cards. A small experiment could
move the first-use prompt above the six recipe cards or link the CTA to
`#install-title`. Compare task completion and time to a useful first card;
page depth alone does not establish abandonment.

## Fresh build and visible behavior

Inspected the existing isolated environment rather than installing software:
Ruby 3.3.6, github-pages 232, Jekyll 3.10.0 were present under
`/tmp/augustus-jekyll.hMqlGZ/`. A fresh destination was created at
`/tmp/augustus-astra-site.qtKizj/`.

The first plain `jekyll build` selected the installed jekyll-seo-tag 2.9.0.
That is not the deployed GitHub Pages dependency resolution, despite
github-pages 232 also being installed. Explicit gem activation selected
jekyll-seo-tag 2.8.0 and reproduced the live homepage byte for byte:

```sh
env GEM_HOME=/tmp/augustus-jekyll.hMqlGZ/gems \
  GEM_PATH=/tmp/augustus-jekyll.hMqlGZ/gems JEKYLL_ENV=production \
  /tmp/augustus-jekyll.hMqlGZ/ruby/bin/ruby \
  -e 'gem "github-pages", "=232"; load Gem.bin_path("jekyll", "jekyll", "3.10.0")' \
  -- build --source docs \
  --destination /tmp/augustus-astra-site.qtKizj/pinned/Augustus
python3 scripts/check_site.py /tmp/augustus-astra-site.qtKizj/pinned/Augustus
```

Both builds passed the checker. The explicitly pinned homepage and the fresh
HTTP response from the deployed homepage have SHA-256
`e52a93c7f07f285d056856ac1fe1fd1d60939310bb9a158f76d1ade73258f30b`.
The only first-build/live HTML differences were SEO-plugin markup. No byte
identity claim is made for un-compared files.

Browser work used the approved Browser skill and its selected Chrome
extension backend. Pages were served at the real `/Augustus/` base path on
loopback. The inspected desktop viewport was 1440×1000 and mobile viewport
390×844; these are browser viewport tests, not physical-device tests.

| Check | Actual result |
| --- | --- |
| Homepage desktop/mobile | Screenshots show legible hero, navigation, and CTAs; document scroll width equals viewport width, 1440/390 |
| Installation cards desktop | Two readable columns; command boxes 476 px wide with no internal overflow |
| Installation cards mobile | One column; page remains 390 px wide; code boxes are 309 px with 353/368 px scroll content and `overflow-x: auto` |
| Examples desktop/mobile | Screenshots show readable tables; page width remains 1440/390; mobile tables are about 314 px wide |
| Ecosystem mobile | Measured document scroll width 390 px |
| First keyboard Tab | Focuses “Skip to content”; visible at top 12 px with a 2 px outline |
| Skip link activation | Enter targets `#main`; next Tab goes to the first main-content link, bypassing site navigation |
| Explicitly pinned rebuild | Homepage desktop/mobile screenshots and width/skip-link checks repeated successfully |

Temporary viewport overrides were reset and agent-created tabs closed. The
temporary build/probe paths are execution evidence, not durable artifacts.
Screenshots were visually inspected in this review's tool output; they are
not committed screenshot fixtures or an accessibility-conformance audit.

## What the checker proves, and does not

Freshly ran all eight `test_check_site.py` tests. All passed. Also ran nine
independent modifications of the actual generated site, each in its own
temporary directory. These exercise parsed behavior rather than slogans:

| Fixture change | Observed checker outcome | Interpretation |
| --- | --- | --- |
| CSS link points to absent local file | `internal-path` failure | Correct |
| Skip link points to absent fragment | `fragment` failure | Correct |
| Canonical loses `/Augustus/` | `canonical` failure | Correct |
| Duplicate `main` ID | `duplicate-id` failure | Correct |
| Insert robots `noindex,nofollow` meta | Pass | Not checked |
| Robots file blocks `/` but keeps correct sitemap declaration | Pass | Only sitemap declaration is checked |
| Replace social PNG with text | Pass | File existence, not image validity |
| Valid encoded fragment `#%6dain` for ID `main` | `fragment` failure | False positive: fragment is not URL-decoded |
| CSS `url("missing.png")` | Pass | CSS references are outside current parser coverage |

Current source HTML contains no noindex directive. The real social image
was separately identified as a valid 1200×630 PNG. The failing/corrupt cases
above are regression fixtures, not claims about today's deployed content.
The existing positive unit fixture deliberately uses non-image bytes for
its `.png`, making the asset-existence boundary especially explicit.

Checker source SHA-256 at review:
`9f3bd95f056eb7fc3c9bf8dc89a45328b7c1c8aa86ad6fe064472166a9982c94`.
Test source SHA-256:
`cffb810fab50be9fd9911adf8766ffb053946042dc9c728d62616e6580fcb370`.

Recommended small corrections, in order:

1. In CONTRIBUTING's reproduction command, activate `github-pages =232`
   explicitly or use a dependency-locked Bundler environment. Merely having
   the gem installed does not select all its pinned dependencies.
2. In `resolve_reference`, URL-decode the fragment before comparing it with
   parsed IDs. Add a positive encoded-fragment fixture alongside the missing
   fragment failure fixture; this fixes an actual resolver bug.
3. For a public-site gate, parse `robots`/`googlebot` meta directives and
   reject `noindex` or `none` on the required public pages. Add a real negative
   fixture. Keep HTTP `X-Robots-Tag` checking in a separate live read-back.
4. Narrow documentation to “local HTML references and social-asset existence,
   canonical metadata, required sitemap entries, and the project's sitemap
   declaration.” State that CSS URLs, JavaScript-created references, external
   reachability, image decoding, and search indexing are outside this check.
   A later decoder test can broaden the asset claim deliberately.

There is also a deployment-level robots limitation. A fresh HEAD request to
`https://24601.github.io/robots.txt` returned 404; the project-local
`https://24601.github.io/Augustus/robots.txt` exists and declares its sitemap.
Robots rules belong at the host root, so the subdirectory file is not the
host's operative robots policy. This is not a crawl block: absent robots
rules allow crawling by default. It does mean the checker cannot establish
sitemap discovery by validating that project-local file. Root-site changes
would be a separate scope. [Google's robots documentation](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt)
supports this location/default distinction.

## Live publication and public discovery

Fresh read-only GitHub API calls verified:

- About description covers the domain-general mission, decision methods,
  calibration/routing/policy, Jev as the default hosted exemplar, and project
  independence. Homepage is `https://24601.github.io/Augustus/`.
- Twenty topics include agent skills, Claude/Codex skills, decision theory,
  decision systems, formal methods, reranking, Jev, and TypeSafe. Topics
  provide categorization; they do not prove ranking or adoption.
- Pages is legacy branch deployment from `main:/docs`, status `built`, at
  the v0.6.0 SHA above; build updated `2026-09-22T14:16:02Z`.
- The latest release is v0.6.0, published `2026-09-22T14:16:53Z`, at that SHA.
- The [Pages check](https://github.com/24601/Augustus/actions/runs/35738967984)
  and separate [deployment](https://github.com/24601/Augustus/actions/runs/35738966693)
  both succeeded. `.github/workflows/pages.yml` only builds/checks; it does
  not itself deploy. Legacy Pages deployment accounts for the public site.

The web extraction service initially returned yesterday's old homepage
title. Fresh direct HTTP and the deployment API contradicted that cached
view; the current-content assertions use the direct responses.

Both Jevusers surfaces already contain Augustus:

- The [linked tracked-project API](https://jevusers.com/api/projects),
  generated `2026-09-22T16:16:22.106Z`, contains one exact
  `full_name == "24601/Augustus"` record at rank 198 of 400, with six stars.
  The [project page](https://jevusers.com/p/24601-augustus) links the exact
  GitHub repository. Its summary still calls Jev the “dominant exemplar,”
  so the external description lags the current project positioning.
- [All apps](https://jevusers.com/apps) contains the exact repository link.
  Its “in Top 100” badge links the project page, but the current tracked
  rank is 198 and the actual homepage Top 100 does not contain Augustus.
  Treat that badge as directory wording, not ranking evidence.

No directory submission is needed to establish presence, and none was made.
Presence in correlated catalogs is not independent validation of quality.

The public [Skills directory page](https://www.skills.sh/24601/augustus/augustus)
also returned HTTP 200. Parsed HTML has the correct repository/install
command, reports five installs, and says “No SKILL.md available for this
skill.” That is an actionable external preview gap, not proof the CLI cannot
discover or install the source. No native install was performed in this
review, and the directory's install count is a reported metric, not five
verified active users. The web extraction service could not open this page;
these observations came from direct HTTP plus HTML parsing.

## Measurement and acceptance boundary

GitHub read-only traffic data were available for September 8–21: 195 views
from 97 unique visitors and 3,384 clones from 775 unique cloners. At read-back,
the repository had six stars and one fork. These are historical access
proxies with automation, research collection, maintainer traffic, repeat
requests, and bot effects unseparated. They do not measure installation,
correct activation, useful decisions, retained use, or gains caused by v0.6.0.
Referrers included GitHub, search engines, directory/social sources, and the
Pages site; the small counts do not support channel-effect conclusions.

No analytics instrumentation or writes were added. The existing feedback
form already requests version/environment, reproduction, expected/observed
behavior, and an optional discovery source. It can supply useful evidence,
but complaint-driven feedback has selection bias and no success denominator.

The next useful bounded evaluation is a consented first-use study: give
unfamiliar users the real landing page, record whether they can explain the
skill, install one exact version, invoke it, and obtain a useful or correctly
negative design card from their own sanitized workflow. Record native-host
version, explicit versus implicit invocation, time, failure stage, and
reviewer assessment. Include ordinary non-trigger tasks. Set acceptance
criteria before observing results. Do not infer this study's outcome from
metadata, structural lint, directory counts, or authored example cards.

## Checks and remaining limits

- `make check`: passed, including 53 unit tests, repository checks, evaluator
  and fingerprint self-tests, and shell syntax.
- `git diff --check`: passed before this audit was added; repeated for the
  completed audit in the worker's final check.
- Fresh Jekyll builds and rendered-site validation: passed; explicitly pinned
  homepage matches live deployment bytes.
- Actual desktop/mobile screenshots, width measurements, keyboard focus,
  and skip navigation: passed for the paths described above.
- Read-only deployment/release/About/directory/traffic read-backs: completed.
- No native-host installation/implicit activation experiment, model inference,
  paid search, account change, outreach, directory submission, or publication.
- Search-engine crawl/index status, native-host trigger quality, and actual
  user benefit remain unmeasured. Current successful release/deployment does
  not resolve those separate questions.
