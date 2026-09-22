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

Keep the entry point short and task-routed. The enforced limits are
16,000 UTF-8 bytes/220 lines for SKILL.md, 18,000 bytes/400 lines per
reference, and 180,000 bytes across references. These are ceilings, not
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
parity, content budgets, reference reachability, supported Markdown links,
duplicate anchors/long paragraphs, unit tests, numerical smoke tests, and
shell syntax. `uniqueness_gate.py` is a compatibility entry point for the
structural checker. CI runs Python 3.11 and 3.12; Pages has a separate build.
The link scanner's supported Markdown subset and limits are documented in
`scripts/check_repo.py`; passing it is not proof every renderer/link works.

Use shellcheck when changing shell scripts. Check the rendered site when
changing its structure. Repository checks need no API keys, model calls,
or network research. Record anything not run.

### Site and installation smoke checks

The Pages workflow builds with GitHub Pages' Jekyll toolchain. To reproduce
locally, use an isolated Ruby environment with `github-pages` 232 (Jekyll
3.10.0), then run:

```bash
JEKYLL_ENV=production jekyll build --source docs --destination _site
python3 scripts/check_site.py _site
```

This checks actual rendered links, fragments, canonical URLs, metadata,
social assets, sitemap entries, and robots metadata. It does not certify
search indexing or layout. Preview the built site at its `/Augustus/`
base path and inspect the homepage, install cards, and examples at desktop
and 390-pixel mobile widths. Check that document scroll width does not
exceed the viewport; long commands may scroll inside their own boxes.
Check keyboard focus and the skip link. Record browser and viewport;
browser emulation is not a physical-device test.

For Claude packaging changes, run `claude plugin validate .`, then use a
temporary `CLAUDE_CONFIG_DIR` to add this repository as a local marketplace,
install `augustus@augustus`, and inspect `claude plugin details`. Expect one
skill and no hooks, agents, MCP servers, or LSP servers. Do not change the
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

## Versions and releases

Installed behavior changes use an unreleased development version until a
release is authorized. Keep skill and marketplace versions aligned, update
the Unreleased changelog, and distinguish last published from development
state in the README. Research-only evidence updates need no package bump.
Releases require the complete checks, behavioral review, an exact tag, and
an install smoke test. Never amend a published tag to replace its contents.

## Scope and secrets

No credentials, private input dumps, or `.env` files in the tree. Follow
[SECURITY.md](SECURITY.md). Use ordinary scoped branches/PRs; no force-push
or automatic staging of unrelated work. Scripts do not publish. Default
branch protection and external account settings remain separately managed.
