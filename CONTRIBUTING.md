# Contributing

Contributions should make Augustus better at placing and evaluating
judgment. Keep the domain-general mission and Jev's role as the default
hosted exemplar. A reproducible result showing that a simpler baseline
wins is valuable.

## Product guidance

Explain the user problem, the current failure, and the smallest correction.
A new reference card needs a placement, assumptions, counterexample,
failure policy, and experiment that could reject it. Link evidence and
label it Contract, Reported, Reproduced, Hypothesis, or Unknown. Avoid
unsupported market-share claims, copied thresholds, and repeated slogans.

Keep the entry point short and task-routed. The enforced limits apply per skill:
16,000 UTF-8 bytes/220 lines for SKILL.md, 18,000 bytes/400 lines per
reference, and 180,000 bytes across that skill's references. Every skill
under `.agents/skills/` is checked, skills share one version, and the
marketplace must list all of them. These are ceilings, not
targets. If a useful addition exceeds them, consolidate or split by a
real user task; don't increase the limit to accommodate a feed.

## Research evidence

Use [the research protocol](research/protocol.md). Treat **revisit HIGH
like novel HIGH** when behavior or evidence materially changes. Update the
existing source card and retain prior claims. Popularity-only movement is
an observation, not a reason to change the skill. Read only the relevant
research sections. No uniqueness passage must be copied into runtime files.

## Local checks

Python 3.11 or later and the pinned development dependency are sufficient:

```bash
python3 -m pip install -r requirements-dev.txt
make check
```

Checks run offline after dependency installation: parsed metadata, version
and release-surface parity, portable frontmatter keys, content budgets,
reference reachability, supported Markdown links, duplicate anchors/long
paragraphs, unit tests, numerical smoke tests, and shell syntax. `uniqueness_gate.py` is a compatibility entry point for the
structural checker. CI runs Python 3.11 and 3.12; Pages has a separate build.
The link scanner's supported Markdown subset and limits are documented in
`scripts/check_repo.py`; passing it is not proof every renderer/link works.

Use shellcheck when changing shell scripts. Check the rendered site when
changing its structure. Repository checks need no API keys, model calls,
or network research. Record anything not run.

For numerical changes, exercise the declared input range, not only typical
values: largest finite values, subnormals, cancellation, ties and boundaries.
Use an independent exact-rational or high-precision oracle where possible.
Check constant-mean preservation, finite bounded results and permutation
invariance. A named “overflow test” at `1e308` does not cover float maximum;
an algebraically equivalent rearrangement can introduce another failure.
Check relationships between outputs too: a strict-support flag must not
contradict its reported bound, and evidence labels must survive failure paths.

### Site and installation smoke checks

The Pages workflow builds with GitHub Pages' Jekyll toolchain. To reproduce
locally, use an isolated Ruby environment with `github-pages` 232 (Jekyll
3.10.0), then run:

```bash
JEKYLL_ENV=production ruby -e 'gem "github-pages", "=232"; load Gem.bin_path("jekyll", "jekyll", "3.10.0")' -- build --source docs --destination _site
python3 scripts/check_site.py _site
```

Explicit gem activation selects Pages' dependency versions; a bare `jekyll`
executable can select newer installed plugins. The checker covers rendered
HTML links/fragments, canonical URLs, metadata (including common `noindex`
directives), asset existence, sitemap entries, and the project robots file's
sitemap declaration. It does not decode images, scan CSS asset URLs, inspect
HTTP indexing headers, or certify indexing/layout. Project-path `robots.txt`
is not origin-wide crawler policy. Preview the built site at its `/Augustus/`
base path and inspect the homepage, install cards, and examples at desktop
and 390-pixel mobile widths. Check that document scroll width does not
exceed the viewport; long commands may scroll inside their own boxes.
Check keyboard focus and the skip link. Record browser and viewport;
browser emulation is not a physical-device test.

### Website design review

Follow [the website design contract](.stitch/DESIGN.md). Start with what the
reader needs to understand and do. Keep an actual, annotated decision study
as the focal artifact, not a fictional dashboard. A monochrome palette alone
does not make a design distinctive. Preserve the skill-and-method-engine
positioning, install path, and distinction between illustrations and outcomes.

Before accepting a redesign, inspect the complete page and shared reading
pages at 320, 390, 768, and 1440 CSS pixels, in both themes. Exercise the
installation anchor, keyboard-only skip link and command scrolling, zoom,
and JavaScript-disabled reading. Keep representative screenshots and exact
build/reviewer provenance in a dated audit. Recheck after substantive fixes.
Record requested and observed viewport dimensions and theme for each case;
assert that they agree and count unique observed configurations. With multiple
tabs, a browser-wide viewport command may resize the wrong tab. A loop count
alone is not evidence of responsive coverage.

The rendered-site checker enforces a language, zoom-safe viewport, focusable
main bypass, distinctly named keyboard-accessible code regions, and named
keyboard-accessible `.table-scroll` containers. A wide comparison table may
scroll inside its own region; test arrow-key access to every column rather
than compressing words into a narrow vertical ribbon. Duplicate
HTML attributes are errors rather than silently using a parser's last value.
These are structural checks, not a WCAG certificate or taste score. The layout
adds numbered code-region attributes to Markdown-generated prose; do not also
add them to raw prose `pre` tags. Homepage command regions declare their specific
names directly.

When changing the share identity, update `docs/assets/social-card.svg` and the
favicon together. Open the SVG directly in a browser at 1200 by 630 CSS pixels,
wait for its local Geist fonts to load, and export a lossless PNG to
`docs/assets/social-card.png`. Inspect the exported bitmap and dimensions, not
only the SVG source. The website references the PNG, so its font rendering does
not depend on a social platform fetching web fonts. Keep the bundled fonts'
upstream license and provenance. Inspect the local font responses and computed
font status: a fallback rendering can look plausible while missing the brief.

Design generators and anti-slop skills supply hypotheses, not authority.
Reject invented metrics, example paths, dependencies, and product claims.
Review the actual screenshots and source, record accepted and rejected
findings, and keep optional style preferences separate from release blockers.
User-selected reviewer models must not be silently substituted. Upload only
public project material, keep credentials and raw provider logs out of the
repository, and do not install design tooling into the skill runtime.
Freeze only intended source and evidence, excluding host metadata and secrets.
Give reviewers absolute paths to that input folder and check actual tool
calls against that scope; a CLI's reported working directory is not proof of
its tools' working directory. A failed read must not trigger filesystem-wide
search. Stop scope-drifting reviews and exclude contaminated verdicts; do not
describe prompt-only read restrictions as an enforced sandbox.

For Claude packaging changes, run `claude plugin validate .`, then export the
candidate commit (`git archive <sha> | tar -x -C <tmp>`) and use a temporary
`CLAUDE_CONFIG_DIR` to add that export as a local marketplace, install
`augustus@augustus`, and inspect `claude plugin details`. A working-tree
marketplace also installs ignored files such as `.DS_Store` and `__pycache__/`.
Expect one skill; no hooks, agents, MCP servers, or LSP servers; and only
tracked `.agents/` files in the installed directory. Do not change the
reviewer's normal plugin settings. Local installation does not verify a
future remote tag; repeat against the exact release candidate before publishing.

## Behavioral review

For substantive skill changes, give a fresh agent the revised skill and
realistic prompts from [the scenario set](tests/skill_cases.json), without
the expected-outcome notes. Have it answer using the skill, then assess
the actual responses against the rubric in
[tests/behavioral-review.md](tests/behavioral-review.md). Include
non-trigger requests and cases where no model should be added.

Keep outputs and reviewer findings in a dated audit artifact. Human or
coordinator judgment owns semantic acceptance. Do not turn matching a
phrase into a “behavioral test.” When a scenario fails, fix the relevant
guidance and rerun affected scenarios plus a fresh check for regressions.

An optional paid activation check needs Claude Code 2.1.269 or later and
maintainer-approved spend. `tests/plugin-evals/` mirrors trigger and
non-trigger scenarios. From the repository root:

```bash
claude plugin eval . --eval-dir tests/plugin-evals --model <id> \
  --judge-model <id> --max-cost-usd <n> --keep-temp --no-publish \
  --json <tmp>/result.json
```

Keep the run only if `suite.plugins` names `.agents` and `suite.ablation` is
`with-without`; otherwise no skill loaded and non-trigger cases pass
vacuously. The JSON does not record models, so keep the requested IDs and the
model in each kept trace's `init` line. `tool_used: Skill` shows activation
with only this plugin installed, not selection among many skills. Judge
verdicts are evidence for this review, not acceptance. A failing trigger case
may be a known recall gap; compare it with the last recorded run in
`research/audits/` before changing guidance. The check is not part of
`make check`.

## Versions and releases

Installed behavior changes use an unreleased development version until a
release is authorized. Keep skill and marketplace versions aligned, update
the Unreleased changelog, and distinguish last published from development
state in the README. Research-only evidence updates need no package bump.
Releases require the complete checks, behavioral review, an exact tag, and
an install smoke test. Never amend a published tag to replace its contents.
Use [the release checklist](research/release-checklist.md), including public
metadata read-back and the distinction between packaged, published, and deployed.

## Scope and secrets

No credentials, private input dumps, or `.env` files in the tree. Follow
[SECURITY.md](SECURITY.md). Use ordinary scoped branches/PRs; no force-push
or automatic staging of unrelated work. Scripts do not publish. Default
branch protection and external account settings remain separately managed.
