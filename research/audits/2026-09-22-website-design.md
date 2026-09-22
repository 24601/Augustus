# Website redesign: decision fieldnotes

Coordinator record, 2026-09-22. Website-only work based on released `main`
`ef8e03596ef97a75c7fd8998b93e9473bd891a6c`. The v0.7.0 skill, marketplace,
README, release notes, and published tag are unchanged. This audit is not
evidence of deployment, adoption, conversion improvement, or WCAG conformance.

## Direction and sources

The user approved the private Stitch upload and this direction: pale mineral
`#F3F4EF`, charcoal `#202620`, forest `#315C45`, IBM Plex Serif headings,
IBM Plex Sans body, square edges. The canonical implementation contract is
[DESIGN.md](../../.stitch/DESIGN.md). Approval of a palette is not approval of
every generated layout or claim.

Sources inspected on 2026-09-22:

- [Google Stitch skills](https://github.com/google-labs-code/stitch-skills):
  generation, design-system management, and design-document workflows. The
  required upload confirmation was obtained before creating the project.
- [Deslop UI](https://github.com/kmaida/deslop-skills/tree/main/deslop-ui),
  including its tells reference: intentional, product-specific choices over
  decorative skeletons, stock card grids, and animation-led hierarchy.
- [Anti-slop Design](https://github.com/hu553in/skills/tree/main/anti-slop-design),
  including its three references: use an actual product argument as the focal
  artifact; another cream-and-serif template is not enough.
- [OpenDesign](https://github.com/nexu-io/open-design), commit
  `b40f25a1c89552725f1fc31f8c2fad172f92acfe`, version 0.23.1: the critique skill
  supplied an independent five-dimension review structure. Numeric opinions
  are not acceptance tests.

Google's taste-design skill was inspected but not adopted: its mandatory
motion/imagery prescriptions did not fit this static technical publication.
Other discovered skill listings were discovery leads, not quality endorsements.
No design skill, MCP server, or tool was installed into the Augustus package.

## Stitch and implementation

The existing authorized Stitch API connection created a private project:
`8268640545279014257`, titled “Augustus: decision fieldnotes.” Design-system
asset: `68ed2e893d7b4790819b52a7b2060ba9`. Initial screen:
`c74089b590c3440fa25d4eef043f61b2`. Refined screen:
`4680325396a642cc8d8ca51d2d673f38`. Both requested `GEMINI_3_8_FLASH` through
the API. The actual provider backend/checkpoint and cost were not exposed.
The durable resource receipt is [metadata.json](../../.stitch/metadata.json).

Accepted: a technical-publication hierarchy, an annotated refund decision,
one emphasized judgment region, unboxed task rows, and genuine installation
commands. Rejected: the first proposal's repeated card containers, generated
artifact filenames absent from this repo, blanket probabilistic-output claims,
and generator assertions that links were “verified.” Generated HTML depended
on extra frontend assets and was not deployed or copied wholesale.

The coordinator implemented semantic Jekyll HTML/CSS. The six detailed
placements remain in [a linked guide](../../docs/placements.md); the homepage
now shows a concrete evidence/judgment/policy/action boundary. The illustration
explicitly disclaims measured performance. Installation is an in-page action.
The reveal-animation script was removed; Git retains its history.

Initial visual corrections: the release link moved out of the mobile primary
navigation into installation/footer references, avoiding an orphaned last
navigation item; hidden line-break whitespace in the illustration disclaimer
was corrected. No speculative adoption statistics or outcome gains were added.

## Parent verification

- `make check`: 113 unit tests passed, plus repository structure, numerical
  and revisit smoke tests, and shell syntax. Python 3.12 isolated environment.
- Production build: GitHub Pages 232 / Jekyll 3.10.0; rendered-site checker
  passed, including the new placements page, links/fragments, metadata,
  canonicals, sitemap, and accessibility structure.
- Chrome 144 on macOS, local HTTP server under the real `/Augustus/` base
  path. Five pages (home, placements, examples, ecosystem, v0.7.0 release)
  at 320, 390, 768, and 1440 CSS pixels in both themes: no document-width
  overflow. These are browser-emulated dimensions, not physical devices.
- Visual inspection included whole-page desktop/mobile home, mobile install
  and examples, tablet placements, dark desktop home, and dark mobile release
  notes. Layout metrics across 40 combinations supplement those screenshots;
  they are not 40 separate visual-quality judgments.
- Keyboard: first Tab exposed the skip link with a 3px outline; Return focused
  `main`; next Tab reached the install action. These passed again on the final
  candidate. The initial candidate's code regions supported keyboard scrolling
  (Right moved 0 to 40px), but their clipped mobile commands were not obvious.
  Final mobile commands wrap and retain their exact text; both installation
  regions have equal client/scroll widths of 348px at a 390px viewport.
- Page JavaScript disabled and reduced motion emulated: content stayed visible
  and the native accessibility click on Install reached the command blocks.
  The page ships no executable script; its remaining script is JSON-LD.
- Pinch-scale emulation reached 2.0 and was reset. The 320px layout checks cover
  narrow reflow separately; this is not a claim of native browser text-zoom or
  screen-reader/device testing.
- Computed palette contrast: tested ordinary-text pairs ranged from 5.34:1
  to 15.45:1 across both themes. This checks the specified color combinations,
  not every possible rendered state or all WCAG criteria.
- An injected Chrome-extension storage error appeared during the scripting
  test, with duplicate page-attributed messages. It is recorded rather than
  represented as a clean console or an identified Augustus defect.

Future checks and review rules live in
[CONTRIBUTING.md](../../CONTRIBUTING.md#website-design-review). Parsed tests
guard navigation bypass, named keyboard-accessible code regions, language,
zoom-safe viewport metadata, and the new page's presence. No slogan-matching
test or anti-slop word blacklist claims to certify semantics or taste.

## Independent reviews

OpenDesign was built in an isolated temporary checkout under Node 24.13.1.
The daemon bound only to `127.0.0.1`; metrics, content telemetry and artifact
manifest telemetry were explicitly disabled. Inputs were a frozen copy of
public source, built HTML, and before/after screenshots, not account data.

### Claude Code / OpenDesign

Requested `claude-fable-5-1` / `xhigh`, as selected by the user. OpenDesign run
`4ac0862a-9330-4b88-85af-a8b2148f5bc0`; Claude session
`1ddb83ab-989c-4e92-8b2b-b75b2ce12bde`. OpenDesign's initialization event
confirmed the model ID; the actual running CLI arguments confirmed `--effort
xhigh`, `--permission-mode bypassPermissions`, `--dangerously-skip-permissions`,
safe mode, and strict empty MCP configuration. Backend effort was not separately
reported. Read-only was an instruction, not a filesystem sandbox. The reviewer
was told not to delegate, modify inputs, or launch another browser.

Initial verdict: **SHIP**, with nonblocking findings. The exact review is
[fable-review.html](2026-09-22-website-design/fable-review.html). OpenDesign
artifact version `f80e1803-f425-4349-8600-fcb7b459dd23`; content SHA-256
`796d28e435c6a2cb59b358c1fb1f3a386ec340d0a59f8cd20a0358e12f5dc252`.
The coordinator read the complete review and reproduced the actionable issues:

- Mobile commands were readable only by scrolling without an obvious cue.
  They now wrap without inserting clipboard newlines, and the two Claude
  commands have a blank separator to distinguish visual wrapping.
- The examples table's `Candidate/evidence` label broke midword; spaces around
  the slash now permit natural wrapping.
- Share imagery and the favicon retained the old identity. The SVG and actual
  1200×630 PNG export now match the site; the square favicon uses a serif A.
- A smaller responsive masthead improves reading-page title hierarchy.
- Prose code regions now have distinct numbered names. The parsed checker
  rejects repeated code-region names and duplicate HTML attributes.
- The design contract now includes complete rule/dark-judgment tokens and
  tested code-region behavior; obsolete classes were removed.
- The study's falsification heading has enough desktop width, and a forced
  use-case heading break is suppressed on mobile.

Not adopted: arbitrary hover-color additions or a redesign of the task-index
and installation columns merely because both use a grid. Their different
content and treatments already establish hierarchy. The review's numeric
scores are opinions, not a threshold to optimize. Its claim that the entire
study fits above a 1000px fold was too broad; actual captures show the lower
edge near that fold. The page has no executable script, but retains JSON-LD.

Initial run: 589,944ms; final usage event reported 162 uncached input tokens,
102,540 cache-creation tokens, 318,047 cache-read tokens and 47,412 output tokens
(including 30,314 thinking tokens). CLI-reported API-equivalent estimate:
**$4.50253175**, not a statement of subscription charges. Cumulative usage
snapshots were not summed. A fresh final-byte review follows the corrections.

Fresh final review: **SHIP**, no must-fix findings. Claude Code session
`5715d5bf-8f23-476d-86f8-cbfb87cd8970`, requested and CLI-observed
`claude-fable-5-1` / `xhigh`; final usage identifies the same canonical model.
The running command retained permission bypass, safe mode, and strict empty
MCP configuration. The coordinator inspected all 35 tool calls: reads/searches
and local image/asset inspection, scoped to the snapshot; no edits or delegate
calls. All ten specified images were read. Report:
[fable-final-review.md](2026-09-22-website-design/fable-final-review.md);
[receipt](2026-09-22-website-design/fable-final-receipt.json).

This run reported 338,247ms and **$4.08293325** API-equivalent list cost. The two
Fable design reviews total **$8.585465**, without adding their repeated usage
snapshots or counting thinking tokens twice. This is not the whole-task cost.

Final-review dispositions:

- The 60–70-character guideline was too universal for wide reference tables
  and short comparison annotations. The contract now describes the intended
  exception; the rendered candidate did not change after final review.
- The narrow ecosystem table is dense and can break long words. The parent
  inspected it at 320px and retained its cross-column comparison for this
  website pass. It remains a specific mobile-reading improvement opportunity,
  not a hidden claim of ideal reflow or a new defect invented from a score.
- The review's categorical statement that Safari ignores SVG favicons is
  outdated: [WebKit documents support in Safari 26.0](https://webkit.org/blog/17333/webkit-features-in-safari-26-0/).
  Older-browser fallback remains optional; this is not an actual Safari test.
- Unstyled page classes are harmless identifiers. The old comparison SVG is
  no longer linked from repository content but remains at its public URL;
  deleting it was unnecessary to this redesign. The fractional media-query
  boundary produces no observed breakage. Neither warranted another UI change.

### Gemini / AGY

Requested `gemini-3.8-flash-high` / `high`; initialization confirmed that model
ID. Conversation `c6550acc-517f-4041-9fe0-fef82e80e633`. AGY warned that its
`--mode plan` request was ineffective with slash-command expansion disabled;
runtime permission mode was `request-review`, not an enforced read-only mode.
The first directory-read command was denied by the permission gate. AGY returned
an empty response, so this is **not a completed design review**, despite a
transport-level SUCCESS result. The user subsequently explicitly authorized
a review-only `--dangerously-skip-permissions` retry. That permission was not
inferred from Claude's earlier YOLO authorization.

Observed usage on that failed attempt: 22,981 input tokens, 932 output tokens
(including 861 thinking tokens), 0 cache-read tokens. No cost was reported.

The approved retry requested the same model and high effort. Initialization
confirmed `gemini-3.8-flash-high`, permission mode `always-proceed`, and the
snapshot cwd; conversation `d7cb01a5-7d5b-415d-930a-a2d034a5cd19`. The ineffective
plan flag was removed. However, its tools searched outside the snapshot and
read the live audit and earlier Fable review. The coordinator interrupted it
after inspecting the actual tool log. It is **excluded as an independent
review**. No file edits or external-service calls appeared in its tool log,
but that does not excuse the scope drift. Its final result was ERROR/interrupted,
not acceptance. AGY reported 678,084 input tokens, 17,982 output tokens (including
12,874 thinking tokens), and 2,209,292 cache-read tokens; no cost was exposed.

A fresh task-local project was then requested with `--new-project`, the exact
snapshot as `--add-dir`, `--sandbox`, and the already-approved permission bypass.
The prompt permits only absolute-path `view_file` reads under the snapshot;
failed reads must stop, not trigger filesystem search. Initialization confirms
`gemini-3.8-flash-high`, conversation `88706bb6-a561-4996-82eb-7a681d0c7e75`, and
`always-proceed`. The sandbox flag is recorded as requested, not claimed to
enforce all tool reads. This run completed **SHIP**, with zero must-fix findings.
The coordinator audited every tool call: **27 `view_file` reads, all under the
exact snapshot root**, including all ten specified images. No shell command,
delegation, edit, browser or external-service call appeared. Report:
[gemini-final-review.md](2026-09-22-website-design/gemini-final-review.md);
[receipt](2026-09-22-website-design/gemini-final-receipt.json).

AGY reported 226.174122 seconds, 535,509 input tokens, 15,657 output tokens
(including 10,970 thinking tokens), and 1,968,043 cache-read tokens. No monetary
estimate was exposed. These are provider-reported aggregates, not independently
reconstructed billing. High effort was requested; the separate backend effort
was not observable.

The coordinator did not adopt the proposed command-sequencing hint: copying
two newline-separated shell commands is valid, and the blank separator already
clarifies them. A heavier active-navigation weight is optional; the underline
and `aria-current` already distinguish it. Extra text-zoom table protection is
an untested suggestion, not an observed failure. The report's “strict
accessibility” language overstates the evidence; its breakpoint description
also conflates `.wide-break` (44rem) with `.desktop-break` (62rem). Neither is
used as a parent acceptance claim.

## Evidence and acceptance

The coordinator accepts the website candidate for a normal PR handoff, not
automatic merge or publication. Both independent final reviews recommend ship;
the scope-drifting Gemini attempt is excluded. The parent owns that decision,
the complete diff, live local-browser checks, and final tests.

Artifacts without a `final-` prefix describe the initial candidate.
`final-site-source.sha256` fingerprints the handoff source and structural
checks; `final-review-inputs.sha256` fingerprints the frozen public review
artifacts (excluding an incidental Finder metadata file, which no reviewer
opened). Snapshot hashes were checked after both final reviews: unchanged.
Only audit prose, process guidance, tool receipts and contract clarification
changed afterward, not the site or checker. The raw logs are not committed:
they include provider internals and,
in the excluded Gemini attempt, out-of-scope directory listings.

The parent supplemented the reviewers' screenshots with final 320px homepage,
320px ecosystem table, 390px dark installation, and 768px placements captures.
These additional images were **not** supplied to the reviewers. The narrow
homepage retains its install action in the first 844px screen. Keyboard skip
navigation and the no-JavaScript install anchor passed again. All 40 final DOM
measurements show no document overflow. This does not certify screen-reader,
Safari, physical-device, arbitrary text-zoom, or print behavior.

OpenDesign's task-local daemon was stopped cleanly after its artifacts were
preserved. Its temporary 3.2GB tool checkout was moved to Trash, recoverably;
the pinned upstream commit can also be downloaded again. Review evidence remains
in this repository. No global plugin, agent, authentication or model-routing settings
were changed. The released v0.7.0 package and tag are not modified.

## Cost and acceptance limits

API-equivalent whole-task cost is unavailable: parent and Stitch usage/cost are
not exposed, and supported comparable prices for these external reviewers are
not available in the installed calculator snapshot. Unknown cost is not zero;
no subscription-charge or delegation-savings claim is made. The **$8.585465**
Fable subtotal above excludes parent, Stitch, all Gemini attempts, and earlier
v0.7.0 release reviews.
