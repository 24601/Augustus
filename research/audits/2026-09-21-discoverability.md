# Discoverability and growth audit

Audit started 2026-09-21; live surfaces and current documentation were
rechecked 2026-09-22 (America/Boise). The repository was at
`0b43a8d3b8d2d389b59415747f566dcbaa3f3ec8` on `main`; the local working tree
contained unreleased `0.6.0-dev` work. This report separates public state from
local remediation. It does not claim exhaustive indexing, search rank, or
conversion.

Evidence labels follow the project protocol:

- **Contract**: a current official interface or submission rule.
- **Reproduced**: an identified local command or live HTTP/API observation.
- **Hypothesis**: a channel or design recommendation that needs measurement.
- **Unknown**: evidence was unavailable or the end-to-end check was not run.

## Decision

The product has a credible core and usable direct install paths. The local
release candidate closes the original packaging, activation-copy, onboarding,
and rendered-site defects. The remaining acceptance boundaries are a remote
install from the released revision, host-level implicit-activation evidence,
the final integrated check, and public deployment. The existing skills.sh
listing and direct Claude marketplace are current discovery paths. Native
Claude/OpenAI directory submissions are post-release experiments, not
guaranteed first channels; generic SEO and broad directories come later.

At audit start the highest-severity defect was a Claude marketplace catalog
without the required root `name`. That made the README's
`augustus@augustus` install claim invalid. The local working tree now fixes the
catalog and passes an isolated install smoke test, but this remains unreleased.

## Findings ordered by severity

| Severity | Finding | Evidence and consequence | Smallest correction | Status |
| --- | --- | --- | --- | --- |
| P0 | Advertised Claude marketplace was invalid | **Reproduced:** the initial `claude plugin validate .` failed because the catalog lacked its required root `name`. The current marketplace contract requires `name`, `owner`, and `plugins`; that `name` is the public suffix in `plugin@marketplace` ([Claude marketplace schema](https://code.claude.com/docs/en/plugin-marketplaces#marketplace-schema)). | Keep root `name: augustus`; keep the plugin rooted at `./.agents` with explicit `skills: ["./skills/augustus"]` and `strict: false`; validate and install from an isolated configuration before release. | Fixed locally; unreleased. |
| P0 | A manifest validation pass alone did not prove installed inventory | **Reproduced:** Claude Code 2.1.278 validates the revised catalog. An isolated `CLAUDE_CONFIG_DIR` install from the local repository then exposed exactly one skill, `augustus`, and zero agents, hooks, MCP servers, or LSP servers; `claude plugin details` reported `0.6.0-dev`. **Unknown:** installation from the remote GitHub repository at the eventual release revision has not run. | Make the isolated inventory check a release gate, then repeat it against the pushed tag or exact remote revision. Assert component count, skill name, and version—not only exit status. | Local-source smoke passed; remote-release smoke pending. |
| P2 | Native OpenAI universal distribution is a deferred channel, not a release defect | **Contract:** Codex loads standalone skills from `.agents/skills`; `agents/openai.yaml` supplies optional UI/invocation metadata; standalone skills are available in Codex CLI, the IDE extension, and ChatGPT desktop ([OpenAI skill docs](https://developers.openai.com/codex/build-skills)). **Reproduced:** the metadata was absent at audit start and is now present locally; Skills CLI discovers the skill. A public OpenAI plugin would add universal-directory and broader ChatGPT reach, not repair the current standalone path. | Verify the current metadata in the real UI. Defer native packaging until the released skill has activation evidence. If later justified, use the current portable root `plugin.json` plus one authoritative `skills/augustus` package; do not add a `.codex-plugin` compatibility shim or a second independently edited skill. | Standalone metadata fixed locally; UI rendering pending. Native plugin deferred. |
| P1 | Activation metadata is corrected; implicit host selection is unmeasured | **Contract:** Codex initially sees a skill's name, description, and path, and may shorten descriptions when many skills are installed ([OpenAI skill docs](https://developers.openai.com/codex/build-skills)). **Observed:** the `0.6.0-dev` frontmatter now explicitly excludes straightforward arithmetic, prose rewriting, and provider setup while preserving positive placement terms. The separate behavioral responses evaluate answers after the skill is supplied; they do not measure whether a host implicitly selects it. | Measure real implicit selection on positive, negative, and ambiguous prompts before claiming activation quality. Review answer quality separately after selection. | Copy fixed locally; host implicit activation pending. |
| P1 | The public website is stale; local crawl/share and responsive checks now pass | **Reproduced 2026-09-22:** the live homepage returned 200 with canonical, description, Open Graph title/description, and a Twitter summary card; `/Augustus/sitemap.xml` and `/Augustus/robots.txt` were not deployed, and the page had no `og:image`. The local tree now adds `jekyll-sitemap`, a project-path `robots.txt`, a 1200x630 social image, favicon, worked examples, and a rendered-site checker. A real Jekyll 3.10 / `github-pages` 232 build passed the structural link, canonical, social-image, sitemap, and SEO checks. Browser review at 1654px and 390px found an install-card width overflow (428px at the 390px viewport); the fix brought it to 390px, and worked examples fit at 390px. Keyboard review confirmed that the skip link reaches the first main-content link. No physical-device test or deployment has run. | Deploy and recheck public URLs. Treat `/Augustus/robots.txt` only as a project artifact: crawler policy for `24601.github.io` is controlled by origin-root `/robots.txt`, which this project path cannot set. The project sitemap and canonical URLs remain usable; root-level handling is external. | Local structural, responsive, visual, and keyboard checks passed; deployment pending. |
| P2 | A measurement policy now exists; analytics remain intentionally disabled | **Reproduced:** skills.sh showed four installs and “First Seen 3 days ago” on 2026-09-22. GitHub's traffic API reported 195 views/97 unique visitors and 3,384 clones/775 unique cloners for 2026-09-18 through 2026-09-21. These counters have different definitions; clones are not installs, activation, retention, or value. This audit now versions the funnel definitions, and a feedback issue path was added. No site analytics are enabled and no conversion is claimed. | Establish a release-cycle baseline before setting targets. Use the feedback path for opt-in qualitative evidence. Never divide counters with different populations/time windows into a “conversion rate.” | Definitions and feedback path recorded; observation pending. |
| P2 | Exact-name discovery works; problem-query discovery is weak or unproven | **Reproduced:** `npx skills add . --list` and `npx skills add 24601/Augustus --list` each found one skill. No install was performed. `npx skills find augustus` returned `24601/augustus@augustus` with four installs; searches for `decision theory` and `model placement` did not return Augustus in the displayed results. A bounded four-query web search for the exact project and generic problem terms returned no results. Search coverage and indexing remain **Unknown**, not “absent.” | Use the job language already present in the new README/site—model placement, classifier boundary, routing, ranking, abstention, threshold policy—in titles, descriptions, worked examples, and native directory metadata. Re-run the same query basket after release. | Partially addressed locally. |
| P2 | Public GitHub metadata contradicts the new product position | **Reproduced:** the repository homepage URL and 20 relevant topics are set, but the public repository description still calls TypeSafe Jev the “dominant exemplar”; `0.6.0-dev` correctly says “default hosted exemplar.” This can produce conflicting snippets and trust loss. | After release approval, update the GitHub description to the same concise, provider-independent claim as the package. Retain the homepage and focused topics; do not optimize by adding more generic tags. | External, release-gated. |
| P2 | Human onboarding is good but the “first value” path is not yet public | **Observed:** the revised README explains the problem before the implementation, offers realistic prompts, states that no model can be the right answer, and distinguishes `0.6.0-dev` from released `0.5.1`. The locally built site has a worked-example page, first-prompt path, and feedback issue; the 390px browser check showed that the examples fit. The public page does not yet reflect this work. | Ship the example and keep one primary CTA per stage: install on the landing page; try a real workflow after installation; report a confusing recommendation after use. | Local build and responsive check passed; deployment pending. |
| P2 | No native directory submission has been attempted, appropriately | skills.sh is populated/ranked through anonymous CLI install telemetry rather than a manual listing process ([skills.sh docs](https://skills.sh/docs)). Anthropic's community marketplace is a read-only mirror: submissions go through its official form, and direct PRs are closed ([community marketplace](https://github.com/anthropics/claude-plugins-community)). OpenAI public plugins use its submission portal and universal directory shared by ChatGPT and Codex ([OpenAI submission docs](https://developers.openai.com/plugins/deploy/submission)). | Submit only a released, remotely smoke-tested package. Do not manufacture installs, open PRs against the Anthropic mirror, or claim official status before approval. | External, gated. |

## Surface audit

### 1. Agent activation

The current description is substantially better than released `0.5.1`: it
names actual user jobs, retains `Choice/Score/Noul` for Jev users, and now says
that straightforward arithmetic, prose rewriting, and provider setup alone do
not require Augustus. That is the smallest frontmatter correction recommended
by this audit.

Selection precision is still **Unknown**. The behavioral-response artifact
tests answers after Augustus is supplied; it is not evidence that Codex,
Claude, or another host will implicitly select the skill. Measure that
separately on a stable activation set:

| Population | Examples | Expected selection |
| --- | --- | --- |
| Positive, implicit | Audit a refund classifier before payment; set an abstention band; decide where a ranker belongs; test whether “confidence” can drive action | Select Augustus |
| Positive, explicit | “Use Augustus”; “Use Choice/Score/Noul with a falsifying evaluation” | Select Augustus |
| Negative exact work | Compare ISO dates; compute tax from a supplied table; validate a schema | Do not select |
| Negative generation/install | Draft a launch email; install an already-chosen provider SDK; summarize a document | Do not select |
| Ambiguous architecture | Choose a database; prioritize projects; review a safety gate | Select only when bounded semantic judgment, uncertain evidence, costs, or authority are actually at issue |

Measure activation precision and recall separately, then review answer quality
after selection. A trigger hit is not evidence that the skill improved the
decision, and a good explicitly invoked response is not evidence of implicit
activation.

### 2. Skills CLI, skills.sh, and directory layout

The repository's `.agents/skills/augustus` layout is the strongest
cross-agent choice:

- **Contract:** the Skills CLI searches `.agents/skills/` and walks supported
  containers up to three levels; `--list` enumerates without installing
  ([Skills CLI README](https://github.com/vercel-labs/skills#skill-discovery)).
- **Contract:** Codex scans `.agents/skills` from the working directory to the
  repository root ([OpenAI skill docs](https://developers.openai.com/codex/build-skills)).
- **Reproduced:** both local and remote `--list` found exactly `augustus`.
- **Reproduced:** the public skills.sh repository and skill pages exist.

Do not add duplicate `.claude/skills`, `skills/`, and `.agents/skills` copies
solely for visibility; divergent copies would create a release and provenance
problem. Use each platform's manifest/installer to point to the one source.

The skills.sh listing is already the canonical low-friction directory surface.
Its public count is useful as a directional install signal, not an outcome
metric. Add its canonical skill link near the install command after release;
an install-count badge is optional and should not become a quality claim.

### 3. Claude marketplace

Current official docs allow either a standard `skills/<name>/SKILL.md` layout
or a single `SKILL.md` at the plugin root. Root-SKILL fallback is documented,
but the locally installed Claude 2.1.278 validator rejected validating the
skill directory by itself because it expected a plugin or marketplace
manifest. The adopted standard nested layout avoids that version-sensitive
edge:

```json
{
  "name": "augustus",
  "plugins": [
    {
      "name": "augustus",
      "source": "./.agents",
      "strict": false,
      "skills": ["./skills/augustus"]
    }
  ]
}
```

This keeps the cached plugin narrow—only `.agents`—while using an explicit
skill path. The official reference documents both automatic root-SKILL
discovery and standard nested skills ([Claude plugin reference](https://code.claude.com/docs/en/plugins-reference#skills)). The isolated install is stronger evidence than schema validation, but the remote tag remains the release acceptance boundary.

### 4. Codex and ChatGPT presentation

The local `agents/openai.yaml` provides a human display name, short
description, and default prompt. Combined with `.agents/skills/augustus` and
the verified Skills CLI discovery path, this is a complete standalone-skill
route for Codex CLI, the IDE extension, and ChatGPT desktop. Actual UI
rendering remains unverified; optional icons and `brand_color` are polish, not
a release blocker.

Native public distribution would add universal-directory and broader ChatGPT
reach, but it is a separate channel experiment. A `.codex-plugin/plugin.json`
file would not publish the skill and is now only a compatibility fallback.
Current OpenAI guidance prefers a portable root `plugin.json` with a fixed
`skills/` package ([OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)).
Do not add a shim now. If post-release evidence justifies this channel, build a
portable package from one authoritative skill source, validate it in the real
surfaces, and submit it separately.

### 5. Human onboarding and website

The local README now answers, in the right order: what the skill is, what it is
not, a useful first prompt, concrete placements, installation, evidence, and
version status. The local website adds worked examples, a first-value prompt,
and a feedback path. These are stronger discovery assets than a large
vendor/project catalog because they map to user problems.

A real Jekyll 3.10 / `github-pages` 232 build and structural checker verified:

1. Homepage title and description contain `agent skill`, `decision models`,
   and one of `classification`, `routing`, or `calibration` without becoming a
   keyword list.
2. Canonical URLs include `/Augustus/`.
3. Every social image resolves under the Pages base path and is 1200x630.
4. `sitemap.xml` contains homepage, ecosystem, and example URLs.
5. The project-path `robots.txt` links the project sitemap.

Browser checks at a 1654px desktop viewport and a 390px mobile viewport found
one material defect: an install card was 428px wide at the 390px viewport. The
local fix brings it to 390px, both worked examples fit at that width, and a
keyboard check confirmed that the skip link reaches the first main-content
link. No physical-device test has run. Install links on the deployed site,
public URLs, and the released remote package remain unverified.

`/Augustus/robots.txt` cannot set crawler policy for the whole
`24601.github.io` origin: standards-compliant crawlers consult origin-root
`/robots.txt`. The project sitemap and canonical URLs are still useful. Any
origin-root robots policy is external to this repository and should not be
claimed as fixed here.

The bounded search run returned no results for its query basket. That does not
prove a page is unindexed and must not be converted into a ranking promise.
Submit the sitemap to search consoles only after the deployed file is correct;
then observe impressions and queries rather than repeatedly changing copy.

## Growth funnel and measurement policy

This audit records funnel version `discoverability-v1`, and the local product
adds a feedback issue path. No analytics were enabled. Use these definitions
for at least one release cycle before changing them; store only aggregate
counts and avoid user prompts, repository contents, or identifiers.

| Stage | Population and event | Source | Interpretation and failure signal |
| --- | --- | --- | --- |
| Qualified discovery | Search impression or directory view for a fixed problem-query basket | Search Console/Bing Webmaster; skills.sh page; Claude/OpenAI directory when approved | If exact-name appears but problem queries do not, improve positioning/examples—not install plumbing. |
| Landing | Unique repository/site landing by channel | GitHub Traffic; optional privacy-preserving site analytics with UTM source | If impressions rise but qualified landings do not, snippets or channel fit are weak. |
| Install intent | Copy/install click from README/site | Optional first-party event; keep raw IP/user data out | If landings rise but intent does not, onboarding or trust is weak. |
| Successful install | Released-package smoke plus compatible directory install counter | Release CI; skills.sh telemetry; native directories if they expose aggregates | Do not substitute Git clones. If intent rises but installs fail, packaging owns the defect. |
| Activation | Implicit/explicit selection on a versioned prompt set; opt-in aggregate invocation count if a platform exposes it | Behavioral review artifact; platform aggregates | If install works but selection precision/recall fails, frontmatter owns the defect. |
| Useful outcome | Reviewer accepts the placement/policy/falsifier or retains the simpler baseline | Opt-in feedback issue/template or study; never collect private case text by default | If activation works but decisions do not improve, stop promoting and fix the skill. |
| Retention | Same installation uses Augustus on a later distinct decision | Only an opt-in or platform aggregate that can measure this safely | Stars, clones, and repeated page loads are not retention. |

Baseline observations must remain separate:

- `skills.sh installs = 4` as observed 2026-09-22.
- GitHub Traffic for 2026-09-18 through 2026-09-21: 195 views/97 uniques;
  3,384 clones/775 unique cloners.
- Search/referrer samples existed, but their small counts and short window do
  not support channel ranking.

No conversion is claimed. Do not set targets from these numbers. First verify
counter definitions and one full release cycle. A useful falsifier for a new
channel is: after enough qualified observations to be meaningful, it adds
maintenance or support load without producing successful installs and
accepted design outcomes; if so, stop maintaining that channel.

## Ordered channel strategy

### Local implementation and release gates

1. **Preserve the passed local gate.** Keep the verified Claude catalog and
   isolated inventory result, Codex metadata, site crawl/share metadata,
   examples, responsive fix, and rendered-site tests. `make check` passed 53
   tests, both self-tests, and shell syntax; inspect the final complete diff.
2. **Test the released object.** After publication is authorized, repeat
   Skills CLI `--list`, Claude marketplace add/install/details, and Pages checks
   against the exact tag or pushed revision. A local-directory success does not
   prove the remote repository works.
3. **Activation evaluation.** Run the positive/negative/ambiguous set above
   with implicit invocation enabled and review actual answers, not phrase
   matching.
4. **Observe before instrumenting.** The definitions and opt-in feedback path
   now exist; analytics do not. Record release, channel, time window, counter
   definition, and limitations. Prefer a small weekly snapshot to real-time
   vanity metrics.

### External actions requiring maintainer authorization

1. **Correct GitHub metadata and release `0.6.0`.** Align the public repository
   description with “default hosted exemplar,” publish the verified tag, and
   let Pages deploy. Do not imply that local `0.6.0-dev` is available.
2. **Experiment with Anthropic's community directory after release evidence.**
   Only after remote install proof, consider the official submission form. The
   community repository is a read-only mirror and direct PRs are incompatible
   with its process. Approval and useful discovery are not guaranteed
   ([Anthropic community marketplace](https://github.com/anthropics/claude-plugins-community)).
3. **Defer an OpenAI portable plugin.** The standalone Codex path is already
   sound. If later evidence justifies universal-directory reach, build a
   portable root `plugin.json` package from one skill source, verify it in
   local Codex/ChatGPT surfaces, and then consider the public submission
   portal. Do not add a `.codex-plugin` shim. Approval and listing are external
   outcomes, not release promises
   ([OpenAI submission docs](https://developers.openai.com/plugins/deploy/submission)).
4. **Let skills.sh grow organically.** It already lists the skill. Do not run
   installs to manipulate telemetry. Recheck exact and generic query discovery
   on a fixed cadence.
5. **Wait before broad curated-list submissions.** VoltAgent's directory
   explicitly asks for real community usage and rejects brand-new skills; when
   Augustus has durable use evidence, a focused PR under its matching community
   category with a ten-word description is compatible
   ([VoltAgent contribution rules](https://github.com/VoltAgent/awesome-agent-skills/blob/main/CONTRIBUTING.md)).
   The Agent Skills specification repository explicitly does not accept skill
   submissions, so do not send one there
   ([Agent Skills contribution rules](https://github.com/agentskills/agentskills/blob/main/CONTRIBUTING.md)).
6. **Publish evidence, not a content mill.** Add future worked examples only
   when a real decision pattern changes or a useful counterexample emerges.
   Cross-links, announcements, or partner outreach require separate authority;
   this audit performed none.

## Release acceptance checklist

- [x] `make check` passes: 53 tests, both self-tests, and shell syntax.
- [x] Local Skills CLI `--list` finds exactly one skill without installing it.
- [x] `claude plugin validate .` passes on Claude Code 2.1.278.
- [x] Isolated local Claude install exposes exactly one skill and no unintended components.
- [ ] Remote/tag Claude install exposes the same inventory and version.
- [ ] Remote/tag Skills CLI `--list` shows the released description/version intent.
- [ ] Codex renders the `openai.yaml` display name, short description, and default prompt as intended.
- [ ] Positive/negative/ambiguous activation review passes with actual responses.
- [x] Real Jekyll 3.10 / `github-pages` 232 build passes structural, link, sitemap, and SEO checks.
- [x] Desktop 1654px and mobile 390px browser checks pass after the overflow fix; keyboard skip-link behavior passes.
- [ ] Deployed homepage, social image, sitemap, and project-path robots URLs return the expected content.
- [ ] GitHub description, README, marketplace, skill metadata, site, and release notes agree on version and positioning.
- [x] Funnel definitions and privacy boundary are recorded; no analytics are enabled and no conversion is claimed.

## Sources

All sources were retrieved or rechecked 2026-09-22.

- [Claude Code: create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
- [Claude Code: plugins reference](https://code.claude.com/docs/en/plugins-reference)
- [OpenAI: build skills](https://developers.openai.com/codex/build-skills)
- [OpenAI: package your plugin](https://developers.openai.com/plugins/build/plugins)
- [OpenAI: submit plugins](https://developers.openai.com/plugins/deploy/submission)
- [Skills CLI README and discovery paths](https://github.com/vercel-labs/skills)
- [skills.sh documentation](https://skills.sh/docs)
- [Anthropic community plugin marketplace](https://github.com/anthropics/claude-plugins-community)
- [Jekyll sitemap plugin](https://github.com/jekyll/jekyll-sitemap)
- [VoltAgent agent-skills contribution rules](https://github.com/VoltAgent/awesome-agent-skills/blob/main/CONTRIBUTING.md)
- [Agent Skills specification contribution rules](https://github.com/agentskills/agentskills/blob/main/CONTRIBUTING.md)

Search result packets used during this audit were written to
`/tmp/augustus-*.json`; they are ephemeral working evidence, not repository
artifacts or claims of exhaustive coverage.
