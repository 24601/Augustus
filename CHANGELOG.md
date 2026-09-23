# Changelog

All notable changes to Augustus are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versioning
follows [SemVer](https://semver.org/spec/v2.0.0.html).

Each release notes the [`typesafe-ai/skills`](https://github.com/typesafe-ai/skills)
revision it was written against. That skill owns integration contracts;
Augustus owns design judgment. Re-read live TypeSafe docs before treating a
pin as current API behavior.

Hourly uniqueness locks from folds after v0.3.0 were moved out of this
file so release notes stay scannable. Archive:
[`research/changelog-hourly.md`](research/changelog-hourly.md). Canonical
folds: `research/notes.md`.

## [Unreleased]

### Changed

- Added "The story of Jev and Augustus", a 2:38 explainer film, to the homepage
  and README. The site uses a click-to-load, privacy-enhanced YouTube player
  with an on-page transcript and `VideoObject` metadata. The MP4, captions and
  poster are hosted on the `film-jev-and-augustus` pre-release, so the
  repository gains only a small poster image. This is a website and README
  change; the skill package is unchanged.
- Skill development version **0.7.1-dev** (not a release). Uncertainty routing
  in the judgment-class reference now separates two-act expected cost, post-hoc
  selective ranking, and deferral to a named handler. Entropy and top-option
  mass rank the same binary menu and can reverse once a choice has three or
  more options. Published **0.7.0** is unchanged until a release.
- Consolidated duplicated runtime guidance. Removed
  `references/formal-semi-formal.md`, a one-screen alias whose rules all live
  in `formal-methods.md`, `mappings.md` §12, and `mental-models.md`. Repeated
  exemplar disclaimers, formal-methods crossover metaphors, duplicated red
  flags, a second invalid-substitution list, and a generic design card now
  appear only in their owning file. References drop from 179,929 to 172,348
  bytes; no design decision is removed.
- Reworked the website as a technical publication centered on an annotated
  decision example. Kept the agent build/evaluate/improve mission visible,
  brought installation into the page, and moved the six detailed placements
  into a linked guide. Removed decorative skeletons, glass panels, gradient
  backgrounds, and reveal-animation JavaScript. This is a website-only change;
  the published 0.7.0 skill package is unchanged.
- Aligned the favicon and social share image with the new site, improved
  mobile command reading, and added parsed accessibility regression checks
  plus a design contract and screenshot/reviewer evidence for future updates.
- Reskinned the website after user feedback to a Geist × stripe.dev-inspired
  developer reference: self-hosted Geist Sans/Mono, a neutral light/dark palette,
  larger typography, ruled grids, and monochrome controls. This supersedes the
  initial mineral/green serif direction without changing the skill package.
  Kept the mobile family comparison readable in a keyboard-scrollable region,
  with parsed regression checks for its name and focusability.

## [0.7.0] - 2026-09-22

### Why this release matters

Augustus is an **agent skill and working method for discovering, building,
evaluating, and iteratively improving decision-model systems**—including
Software 3.0 programs, evaluation harnesses, and prompt/program hill climbing.
It is not a vendor catalog or a median survey of what others have built.
Research supplies good/bad patterns and hypotheses; mathematical composition
rules and independently observed outcomes determine which methods to retain.

This mission is now explicit in the README, skill activation metadata, Codex UI,
Claude marketplace description, and website for discoverability. The new
composition calculus and executable paired-outcome evaluator make the workflow
more actionable. This is not a claim of universal optimality, measured user
growth, or a demonstrated deployment gain from the skill itself.

### Added

- A typed composition calculus: branch and selected-cascade accounting,
  dependence-safe risk budgets, bounded-loss decision regret, joint-information
  substitution limits, and closed-loop outcome contracts.
- An executable paired-workflow outcome comparator with fixed-sample bounded-loss
  confirmation, explicit provenance/unknowns, and no deployment side effects.
- An agent build/evaluate/improve loop for decision-driven and Software 3.0
  systems, with bounded search, protected confirmation, regression and rollback.

### Changed

- Refined wrapper score semantics, permutation averaging, multimodal observation
  limits, and full-pipeline cost/latency accounting from a new primary-source refresh.
- Added finite-sample support planning and controlled injection-evaluation guidance.
- Re-derived the session's prior delegated work with requested GPT-6 Astra/xhigh
  reviews and fresh behavioral answers; scenario coverage grows from 12 to 31.
- Required explicit discovery-versus-inspection coverage, requested-source
  dispositions, and publication/metadata read-back in maintainer checklists.
- Defined recurring changed-source, aged-card, and whole-skill reassessment;
  left the unverified external scheduler explicitly open rather than claiming
  that a collector script establishes unattended research.

### Fixed

- Removed unnecessary specialist-training, RAG-filter, calibration, and
  all-metrics-win requirements. Distinguished detection from preventive
  enforcement, Alloy object bounds from temporal horizons, and distillation
  targets from independently established truth.
- Rejected duplicate JSON keys and normalized malformed-input failures;
  prevented finite mean-cost overflow and conflicting repository identities.
- Adversarial review caught maximum-float overflow, subnormal mean/cost loss,
  early-normalization delta loss, and near-zero log-loss cancellation missed
  by the initial tests. Exact-ratio aggregation and stable logarithms now have
  boundary and randomized regressions. Fable follow-up notes also led to
  consistent strict-bound rounding, order-stable Brier/calibration aggregation,
  explicit attrition metadata, provenance-preserving violation labels and
  build/improve activation examples.
- Enforced installed-skill link containment and recursive reference budgets;
  corrected fence parsing, SemVer validation, encoded site fragments, and
  accidental `noindex` detection. The suite now has 106 regression tests, including
  executable composition counterexamples and workflow comparisons.
- Corrected GitHub About wording and documented explicit Pages toolchain
  activation. Directory preview/activation and user-growth gaps remain visible.
- Audited existing awesome-list registrations and prepared targeted positioning
  updates; external PRs/corrections remain unsubmitted. Release and maintenance
  checklists now revisit accepted, open, rejected, and crawler-managed listings.

Minor-release scope: new outcome-evaluation capability and operational agent
workflow, plus corrected guidance/helpers; no new provider integration or
breaking valid-input API. The planned 0.6.1 patch was not published. Historical TypeSafe skill provenance
remains [`v0.5.7`](https://github.com/typesafe-ai/skills/tree/65a39f393687675ce170e6094757de20370365b9).
See [release notes](docs/release-notes-v0.7.0.md) and the
[full refresh](research/decision-model-review-2026-09-22.md).

## [0.6.0] - 2026-09-22

### Changed

- Rebuilt the skill as a concise entry point and focused references;
  preserved historical source revisions in the research archive manifest.
- Clarified probability, confidence, ranking, calibration, authority,
  abstention, causal action effects, and scoped conformal guarantees.
- Replaced repeated-prose uniqueness checks with structural lint, budgets,
  metadata parity, link/reachability checks, regression tests, and CI.
- Removed tautological evaluator assertions; added real selective-policy
  metrics and strict input validation, including undefined all-abstain risk.
- Added maintainer guidance, research promotion and review prompts, and
  independent behavioral scenarios. Refresh collection no longer publishes.
- Fixed Claude marketplace packaging and verified an isolated local install;
  added Codex skill UI metadata and clearer activation exclusions.
- Rebuilt onboarding around six placements and two worked examples; added
  social-preview assets, sitemap, rendered-site checks, a feedback template,
  and a discoverability audit. Corrected mobile install-card overflow.

### Migration

- Evaluator cost reports now require explicit `--cost-fp` and `--cost-fn`;
  selective-policy cost also needs `--cost-abstain`. Threshold search is
  labeled in-sample and must not substitute for held-out policy evaluation.
- Complete binary predictions report `action_rate`, not selective coverage.
  Log loss is infinite for an impossible observed event; malformed inputs
  and duplicate IDs are rejected. Partial baselines are accepted but
  excluded from comparison; comparative reports require a complete baseline.
- Refresh scripts emit JSON review receipts instead of appending logs,
  cloning discoveries, or committing/pushing changes. Scheduler owners
  should explicitly choose receipt storage and perform separate review.
- `uniqueness_gate.py` is a repository-maintainer compatibility entry point
  to the structural checker, not a tool for an installed standalone skill.
  Use `make check` for the complete check suite.

Catalog observations remain in [research](research/README.md); they need
not change the installed skill. See [release notes](docs/release-notes-v0.6.0.md).

## [0.5.1] - 2026-09-21

Patch on the 0.5.0 package surface. v0.5.0 (2026-09-20) already shipped
class-wide recipes and Pages. Hourly folds since then stayed pinned at
0.5.0. This cut is the human-facing pin, not a research dump.

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12). Live HEAD of that repo is still this commit.
Checked 2026-09-21. Do not treat a later untagged commit as a new pin
until it is tagged.

Framing lock (merged #68): decision-model class first. TypeSafe Jev
(Choice, Score, Noul) is the dominant exemplar most users will call.
Peers are in the class. They are not equal in adoption.

README ends at License. `uniqueness_gate.py` fails if a uniqueness dump
wall returns after that heading.

### Added

- **GEPA domain-adapt (class recipe).** Praneeth ADE on Jev. Without
  Augustus: treat a schema-valid Choice as correct, API confidence as
  P(correct), or F1 as a review-queue policy. With Augustus: schema-valid
  is not the same as correct; confidence is not P(correct); GEPA revises
  Choice instructions and criteria with weights fixed; Brier and F1 stay
  *theirs*; a review queue is not an F1; a soft score is not a gate.
  Full card: [`docs/release-notes-v0.5.1.md`](docs/release-notes-v0.5.1.md).

### Changed

- Package pin 0.5.0 to 0.5.1: SKILL metadata, marketplace, README, Pages
  kicker, CITATION.cff. SECURITY supported line stays 0.5.x.
- Skill YAML `description` is a short class-first blurb (under 1024
  characters). The trigger-keyword wall and the full mapping-index rows
  live in `references/activation-triggers.md`. SKILL.md keeps a short
  row plus the hourly uniqueness locks.
- Pages nav and recipe links point at the v0.5.1 notes. Earlier class
  recipes remain on the v0.5.0 notes.

### Notes

Catalog densifies since 0.5.0 (hourly folds through 1019 / `notes.md`
§145) stay in `research/notes.md` and the hourly archive
`research/changelog-hourly.md`. They are not release-note walls.

## [0.5.0] - 2026-09-20

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12). Live HEAD of that repo is still this commit,
the only tagged official-skill revision.

Nine commits on `main` after the v0.4.0 tag (merged #33 README map,
#31 Harbor-jevals, #34 Pages layout, #35 hysteresis/ECE, #36 NanoJev,
#38 jcr, #37 SemIf, #40 llm-to-jev, #39 0843 hygiene). Open #41
(0947 fold) is in flight on another branch and is not part of this
release. Verbose hourly locks stay in
[`research/changelog-hourly.md`](research/changelog-hourly.md).

### Added

- **Pages / onboarding.** Custom site layout (nav, comparison, install,
  pillars). With vs without Augustus on the homepage and README
  (`docs/assets/with-without-augustus.svg`): call-then-act vs
  place-then-judge. Jev is the exemplar, not the monopoly.

- **README.** Scannable skill map (one line per file). The living catalog
  stays in the reference cards and `research/notes.md`, not a README wall.

- **Recipes (class, not Jev-only).** Same with/without split for any
  Choice/Score/Noul-style or typed probabilistic judgment tool. Full
  cards: [`docs/release-notes-v0.5.0.md`](docs/release-notes-v0.5.0.md).
  Shape, not invented scores:
  - **Encoder (GLiNER / GLiClass):** without — swap locate/categorize for
    a decision head and hard-gate spans. With — species map; remainder
    after extractive spans. Measure span quality separately from ECE.
  - **Open heads (Laya, SemIf, kev, Jeff-1):** without — treat wire-compat
    or argmax agree as a replica. With — softmax over options ≠ calibrated
    Noul; systems timing ≠ semantic equivalence. Measure ECE/Brier on
    held-out, not only speed or top-1.
  - **NanoJev:** without — game wins as calibration. With — specialist
    gameplay S1; local boolean ≠ TypeSafe noul. Measure held-out game
    success separately from ECE.
  - **llm-to-jev:** without — ship converted prompts as equivalent
    behavior. With — heuristic on-ramp; review Score rubric; prose stays
    with the LLM. heuristic conversion ≠ calibrated Noul.
  - **jcr:** without — run what the capability tree found. With — lookup
    returns context and **does not execute**. Routing ≠ permission;
    docs ≠ authority to run.
  - **localjev / prompted JSON:** without — parse generated JSON as a
    Noul. With — schema-valid ≠ picked-right; prompted JSON ≠ structured
    logit read.

- **Class / migration.** llm-to-jev conversion on-ramp (`notes.md` §118).
  SemIf rename + MLX densify (`§117`; formerly OpenJev, independent).
  NanoJev unified-games densify (`§115`). jcr capability resolver
  (`§116`; docs ≠ execute).

- **Measurement honesty.** 0843: hysteresis `{enter, exit}` is policy
  attached to a probability, not a model property; instruct-tuning can
  wreck ECE while accuracy stays flat; equal-width ECE ≠ quantile ECE;
  hop-ECE is permutation-invariant (trajectory soundness theater);
  ranking ≠ calibration. 0743: Harbor-jevals practice (schema-pass ≠
  joint fields; skip-and-call-a-tool); Verdict linear ECE floor ≠
  TypeSafe replica; DecisionOps ACT / REVIEW / FALLBACK (a provider
  failure is **not** a policy outcome). Evaluator reports both ECEs,
  AUC, accuracy@0.5, cost-optimal threshold, hysteresis, and hop-ECE
  invariance.

### Changed

- Marketplace plugin version and SKILL YAML pin: 0.4.0 → 0.5.0.
- Homepage / README / CITATION.cff / SECURITY supported line follow 0.5.0.
- CHANGELOG Unreleased dump folded into this cut. Verbose hourly locks
  remain in `research/changelog-hourly.md`.
- Evaluator hop-ECE self-test covers reverse and even/odd interleave
  (permutation invariance is not reverse-only). uniqueness_gate checks
  Pages strings (`LICENSE` in the #34 layout) and refuses CHANGELOG/README
  dump walls. `docs/ecosystem.md` 0843 blurb cites `notes.md` §114.

### Security

- `SECURITY.md`: supported line is 0.5.x. Report via GitHub Security
  Advisories. No invented Scorecard number.

## [0.4.0] - 2026-09-20

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12). Live HEAD of that repo is still this commit,
the only tagged official-skill revision.

Twenty-eight commits on `main` after the v0.3.0 tag (merged #2–#30,
through Merve §112). Open #31 (0743 fold) is in flight on another
branch and is not part of this release.

### Added

- **Class breadth.** TypeSafe Jev remains the documented exemplar, not
  the monopoly. Folded class peers and cousins: Laya (open head), kev
  family (Archer-arch fidelity; replica honesty), OpenJev `/v1/decide`
  (not a TypeSafe drop-in), TypeAR / constrained-AR, GLiNER species
  (locate vs categorize vs safety-schema vs local multi-head), Decision
  Graph Protocol (frame→assess→commit; app retains permissions/effects),
  encoder zero-shot classifiers.
- **Encoder / ZS lineage (Merve Noyan, `notes.md` §112).** Institutional
  HF voice: BERTForXYZ → DeBERTa → ModernBERT. Many problems solved with
  LLMs could have been solved with zero-shot classifiers. It was a
  skill issue. Prefer DeBERTa and ModernBERT heads. Jev vs GPT-5.6
  bakeoffs are a category error. Softmax / ZS scores still ≠ calibrated
  Noul; soft scores ≠ hard gates. Multimodal image↔text ZS is a
  perception front-end, not a decision model. Quote *theirs*; no
  invented accuracy numbers.
- **Measurement honesty.** Harbor / jevals practice: ranking ≠ calibration;
  Score is a 0..n−1 expectation, not 0–1; Noul has no confidence field;
  ECE ≠ an edge; treating 0.85 / minProbability as a hard Harbor gate is
  theater; soft Noul ≠ hard gate; VERIFY must acquire discriminating
  evidence, never same-pool confidence-only rescoring. Calibration is
  not alpha. Compaction default 0.5 is not safety.
- **Composition / placement.** Decision Graph Protocol envelope;
  meaning-grep (proposition ≠ embedding; AND/OR/NOT after threshold;
  not a gate); gut cost-of-error overlay (thresholds from costs, not
  hard-coded); fail-open vs fail-closed per action; prune ≠ deny;
  hard-gating DGP as safety theater.
- **Pages landing** at https://24601.github.io/Augustus/ (`docs/`) plus
  community-health stubs (`SECURITY.md`, `CONTRIBUTING.md`, brief
  `CODE_OF_CONDUCT.md`), `CITATION.cff`, and
  `.github/workflows/scorecard.yml` so an OpenSSF Scorecard can appear.
  No invented Scorecard number.
- Formal methods pillar unchanged in spirit: a Noul is a SENSOR; never
  launder it as a proof (soundness theater).

### Changed

- Marketplace plugin version and SKILL YAML pin: 0.3.0 → 0.4.0.
- README / Pages SEO: one-liner, homepage, install paths, "not a
  TypeSafe product" clarity, [`rh-guard`](https://github.com/24601/rh-guard)
  companion pointer.
- CHANGELOG restored to Keep a Changelog. The hourly uniqueness dump
  lives in `research/changelog-hourly.md`.

### Security

- `SECURITY.md`: supported line is 0.4.x; report via GitHub Security
  Advisories / private vulnerability reporting. Dependabot security
  updates, secret scanning, and push protection stay enabled.
- `.gitignore` covers common secret filenames.

## [0.3.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12).

### Added

- Mixed-architecture card: default placement is judgment-class model +
  generator + code, not stack replacement. Covers cost-sensitive prefilter
  (fail-open vs fail-closed per action), tool/skill routing, AGENTS.md
  preference lint, a placement gallery from the 2026-09-18 X+GH hour, and
  an explicit answer to "Jev is just classification"
- Protocol branch and mapping-index rows for those four placements
- Non-negotiable: classification is not the product; typed judgment is a
  software primitive placed beside generation
- Hourly research archive for this pass (X theme digest + `topic:jev` movers)
  under `research/archive/hourly/2026-09-18T14/`
- Research note on Laya (`convaiinnovations/laya`): open Choice/Score/Noul
  head as a self-hosted *typed judgment provider*; vendor benches labeled
  claims; TypeSafe remains the default path
- Applied-mapping cards: context sieve, exact-text keep/drop, env/harness
  triage, moderation/ranking, skill/tool routing (`applied-mappings.md`)
- FAQ card for "it's just classification", stack replacement, Jev vs open
  head, and Augustus vs neighbor how-to skills
- Judgment-class card: Augustus covers the whole class of fast/cheap
  categorization-classification-scoring models (Jev is exemplar, not
  monopoly). Families: closed decision API, open System-1 heads (Laya),
  GLiNER/GLiClass encoder family (locate vs categorize vs local
  multi-head), listwise/pairwise rankers, vision scorers.
  Species map in `judgment-class.md`; GLiNER is a peer, not a footnote.
  Fork of listwise discriminative vs decision/proper-scoring objectives;
  four vision scoring patterns; seven portents for agent architecture.
  FAQ rows for family choice, GLiNER vs GLiClass vs Jev vs cross-encoder, and
  CLIP/SigLIP gating. No invented APIs.
- Formal-methods card: judgment vs proof ownership (sensor / constraint /
  searchlight); Alloy Analyzer vs Apalache (model finder ≠ SMT BMC ≠
  inductiveness); TLA+/Quint/P/NuSMV/PRISM/Event-B; Dafny/JML/
  Frama-C/SPARK; DST trio (Antithesis hypervisor, Resonate Lean+oracle+
  SDK, PufferLib env+seed / Ocean trainer contracts); harms
  (TOCTOU-of-Noul, soundness theater, AI×FM / Hillel vibing specs);
  crossover metaphors (NATM, snap-fit, Norman gulfs, Leveson STAMP/STPA).
  Curriculum archived at `research/archive/curriculum/FORMAL-METHODS-SYSTEM-ONE.md`;
  named rows folded here. One-screen alias: `formal-semi-formal.md`.
  Non-negotiable: never launder a Noul as a proof.
- One-screen `references/formal-semi-formal.md` (curriculum 1-pager)
- Hypothesis mapping cards (do not promote without an acceptance test):
  VOI / gather; SDT/ROC; Leveson sensor≠constraint; search/control
  outside SWE; spec property pipeline; Alloy instance loop; runtime
  assurance sandwich; DST multiverse triage; durable agent control;
  assignment hybrid; situated density (`mappings.md` §6–§16)
- Input-brittleness and structural-prove ∩ remainder cards
  (`mappings.md` §17–§18): paraphrase pairs → Chow abstain; allowlist /
  text-layer first, judge leftovers (jevgate / doc-router *shapes*
  Empirical; domain-general reading Hypothesis). FAQ: GLiNER vs Jev,
  LLM-as-judge (Langfuse framing), allowlist-then-judge
- GLiGuard as an Empirical encoder peer (`judgment-class.md`,
  `notes.md` §30): one-pass safety-schema classify on GLiNER2, not a
  Jev weight clone; FAQ "is GLiGuard Jev?"; README OR/refusal
  aggregation left as existing policy-in-code. LLM I/O safety is not
  a coding-agent tool gate
- Hourly 10:07 Boise fold (`research/notes.md` §25–§26): GLiNER2.5 local
  peer; openjev-lm 92.9% / 6 vCPU teacher-distill; jevgate; doc-router
  1.74× $; pi-jev-context; jevscope next to jevals; Han Xiao trolley
  (listwise ≠ decide); James Ward dual orchestration; JevLint
- Constrained-AR surface, not a sixth species (`judgment-class.md`):
  TypeAR puts a typed interface on a pretrained generator (next-token
  constraint ≠ proper-scoring head). Archer Hume's open-weight drop
  stays **Watch** (`research/notes.md` §31, §32)
- Hourly ~11:02 Boise fold (`research/notes.md` §33): Archer
  clarifications still Watch (27B dense one-forward-pass, multimodal
  generalization report, AU healthcare residency not anti-TypeSafe,
  prefers "decision models"); when-to-use table (proprietary Jev vs
  Archer vs TypeAR vs encoder DeBERTa vs LoRA distill); HF novel
  (jev-gate-student-b 148k corpus, jp-sns-jev7 ONNX, open-jev-deberta,
  mini-jev-runs 27.9k logits, jev-tree-choice-cap); device/harness
  (jev-mobile MCP, jev-macos-loop, jev-harness, routeKit); HacksonClark
  SREGym-Lite 20/50→24/50: rank tests, do not diagnose
- Hourly ~11:59 Boise fold (`research/notes.md` §42): Archer still
  Watch. Three open paths (encoder / AR constrained decode / trained
  decision-only). Native constrained serving
  ([pcdServer](https://github.com/stephanj/pcdServer), TypeAR-class,
  2–256 enums, Apple+Linux GGUF). Meta-VOI hook
  (typesafe-jev-tools 149-row: Haiku more accurate, Jev confidence
  monotonic). jev-mode latency-class split (token ratio durable;
  accuracy is parity). OpenSmoke env-break vs policy-break +
  pre-mortem. jevql store-as-decision-surface. jot topology B with a
  closed catalog. openevals online full-traffic. hermes north-star
  two-layer finish gate. pi-jev (not pi-jev-context). jev-plays-games
  option-order probe. joxide jump-by-description. laya-typed-decisions
  companion packaging. No wrapper.
- Effect-oriented loops (`notes.md` §28, `mappings.md` §19): Ward's
  ZIO client keeps Jev as the outer Choice and the handler as the
  effect. Not Effect.ts. GLiNER author: GLiNER2 "like jev" is GLiGuard
  schema-conditioned categorize, not a Noul.
- Boundary-audit stop conditions for TOCTOU-of-Noul and vacuous specs;
  FAQ rows for Alloy vs Apalache and PufferLib-as-DST-trio
- Research pointer to [dayhaysoos/jevals](https://github.com/dayhaysoos/jevals):
  local MIT workbench for Jev questions vs labeled Noul/Choice/Score cases
  (compare runs, WebMCP + agent skill). Empirical acceptance-test surface
  for Hypothesis mapping cards; complements `evaluate_decisions.py`. Not a
  jevals how-to (`research/notes.md` §24; one sentence in `validation.md`)
- Mental-models card: Augustus is design judgment across AI, SWE,
  business, knowledge work, and life, not SWE-only. Pillars: expected
  utility / selective classification, calibration and cost-sensitive
  thresholds, VOI, MCDA, search/control substitutions, signal detection,
  Leveson org/safety, NATM/snap-fit/Norman/Kent/Shirky as general
  intuition. Domain gallery labeled Hypothesis except launch-week
  Empirical SWE rows.
- Archer Hume architecture reconstruction (17 Sep 2026 essay, ~10k
  probes of `jev-1.13.0`): direct readout vs generated confidence,
  isolated questions, listwise IIA and order sensitivity, confidence as
  arithmetic on the distribution. Independent envelope probe; does not
  override live TypeSafe docs. Announced open-weight drop is **WATCH**
  (27B dense, AU healthcare residency, prefers "decision models"; still
  no Hub weights). `research/notes.md` §31, §33; `judgment-class.md`
  when-to-use table; FAQ confidence / surfaces questions.
- Entropy as allocator (**Hypothesis**, `judgment-class.md`): Atallah's
  low / medium / high buckets place System One on typed decisions and a
  frontier decoder on high-entropy synthesis, same axis as marginals
  vs joint and as VOI. "Review this PR" as medium is still partly
  generative; "first model ever" is a claim. `research/notes.md` §38
- Marginals, not a probabilistic program (`judgment-class.md`, FAQ):
  Erik Meijer: Jev is a cool API and not a PPL; Kleisli qualifications
  exaggerate; "Jev gives you the marginals; a decoder gives you the
  joint." Joints and invariants stay with TLA+ / Alloy / contracts.
  `research/notes.md` §34
- Bespoke Nimble: open contrastive recipe, not a Jev distill. Model
  card Apache-2.0 LoRA on Qwen3.5-9B (repo license absent). Their
  324-example holdout is a named receipt (Nimble 90.12%, Jev 1.13.0
  93.21%), not a ranking. 9B-vs-Jev on your labels stays Hypothesis.
  `research/notes.md` §35; one sentence in `validation.md`
- djev-spark: third compute graph (diffusion structured reads,
  Jev-shaped I/O, image-in). Empirical as the public interface;
  Hypothesis that it beats a decision head on your task. Archer's
  multimodal drop stays WATCH. `research/notes.md` §36
- Perception specialist then judgment specialist vs shared multimodal
  System One (**Hypothesis**): SAM 3.1 (masks and tracks) or an ASR
  transcript, then typed decisions on that state, is an application
  pattern, not native omni. Information dies at the interface. Prefer
  a shared multimodal decision model when the joint matters (Archer
  Watch, not Empirical; djev-spark images; future audio). Basit ask,
  primary post not retrieved. `research/notes.md` §39
- Perception→decision pipeline, measure, and hill-climb
  (**Hypothesis**, `validation.md`): stages with a versioned state
  contract; stage metrics plus a frozen taskset; HoH changes one stage
  or one interface. DSPy/Ax only on LM-program knobs; jevals and
  calibration for the decision slice; Harbor names product
  end-to-end, not a tutorial. `research/notes.md` §41
- Eval & hill-climb (`validation.md`): jevals decision-stage hygiene
  (independent keys, correctness is not confidence, held-out, immutable
  runs) and Harbor as the product taskset substrate; one composition
  table. `research/notes.md` §40

### Changed

- Skill description rewritten as trigger conditions (mixed architecture,
  prefilter, routing, preference lint, classification skepticism, family
  choice including GLiNER/GLiClass/listwise/vision) plus an explicit `not_for`
  against the official `typesafe-ai` skill
- Identity lock vs neighbor skills (`typesafe-ai`, `tenbin`, `decision-first`)
  so Augustus stays the design-judgment layer, class-wide, not TypeSafe-only
- Design cards name hole, family, and typed judgment provider (Jev default;
  other family only with self-eval)
- Protocol fan-out step is family-aware (Jev batch, GLiClass one-pass,
  dual-encoder prompt scoring); ranking vs decision fail policy is a
  non-negotiable
- Protocol and FAQ branch for "formally verify with Jev"; methods-catalog
  and composition-algebra verifier position point at the ownership split
- Skill mission and description are domain-general (AI / SWE / business /
  knowledge work / life); FAQ "is this only for software?"; mappings.md
  beyond-SWE examples labeled Hypothesis; boundary-audit red flags for
  TOCTOU-of-Noul and vacuous specs; formal-methods expanded with Alloy vs
  Apalache and the DST trio including PufferLib; GLiNER promoted from
  cousin footnote to species-map peer

### Fixed

Adversarial review of the whole skill against its own non-negotiables
(findings in `research/notes.md` §27).

- Gate fail policy is per action, not universally open
  (`composition-algebra.md` position 3, `agent-self-assessment.md`):
  advisory guards fail open *because* an interlock sits underneath;
  selection and authorization gates fail closed
- Dual-orchestration topology A selects from a closed catalog instead of
  "planning" MCP calls, which contradicted the standing planner rejection
- Species map applied to the skill's own advice: GLiClass (categorize) is
  the large-catalog substitute for a 255-option Choice; GLiNER spans are
  not (`SKILL.md`, `judgment-class.md`, `applied-mappings.md`)
- Han Xiao trolley relabeled an Empirical **rejection** (one tweet, no
  repo), not a recipe
- openjev-lm caveat moved to the figure it belongs to: 92.9% is against 70
  hand-labelled gold, 98.1% is teacher *agreement*
- Contract surface removed from design cards: the Ax constructor call and
  the `instructions` key enumeration point at live docs instead
  (`optimizer-integration.md`, `question-design.md`)
- `mappings.md` preamble no longer claims uniform Hypothesis where card
  bodies say Contract/Empirical; §17 forbids reusing jevgate's ≤0.18 as a
  constant; all Hypothesis-range references aligned to §6–§19
- Ownership split labeled Contract in `toolbox-mapping.md`, matching
  `mappings.md` §8; done-check splits structure from the Noul

Second pass on `7b3a0c3` (`research/notes.md` §43). Zero blockers.
Dropped the unpublished `npx jevals` line; SAM and ASR are upstream
producers, not the perceive species; removed two call shapes from
`optimizer-integration.md`; tagged the $0.042/MTok cell as a vendor
figure; marked GodsBoy 94.4% exploratory.
- Skill description gained trigger terms for boundary audit, question
  diagnosis, agent self-supervision, and optimizer placement

## [0.2.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12).

### Added

- Boundary-audit card for existing systems: three-way split (exact /
  bounded judgment / generation), code-smell catalog, fit test, opportunity
  map, smallest-viable-boundary rule, Jev-around-LLM sandwich, centralized
  policy + raw-judgment retention, red flags, completion questions
- Protocol branch: audit a codebase/PR before inventing mappings; per-action
  risk gates; keep questions/thresholds in one reviewable module
- Skill description trigger terms for brittle parsers, prompt-to-JSON
  classifiers, and agent loops that are really bounded decisions

## [0.1.0] - 2026-09-18

Pegged against [`typesafe-ai/skills` v0.5.7](https://github.com/typesafe-ai/skills/tree/v0.5.7)
(`65a39f3`, 2026-09-12), the only tagged revision of the official skill at
Augustus launch.

### Added

- Skill protocol, decision-design card, and evidence labels (Contract /
  Empirical recipe / Hypothesis)
- Classical-method mappings: features/utility, selective decisions, decision
  circuits, bounded rerank, hierarchy/beam search
- Agent self-assessment, optimizer coupling (Ax, DSPy, ProgramAsWeights)
- Toolbox sweep, named-methods catalog, 11-position composition algebra,
  question-design diagnosis
- Validation gates and `scripts/evaluate_decisions.py`
- Launch-week evidence archive (187 repos) and public ecosystem index
- Claude Code marketplace manifest; public GitHub mirror at
  [`24601/Augustus`](https://github.com/24601/Augustus)

### Research log (pre-tag)

The dated passes below are how 0.1.0 was assembled.

### 2026-09-18 (refresh pass 2)
- Research: Gemini Deep Research report retrieved and archived (interaction ID
  saved in jev-archive/state); GitHub census doubled to ~60 Jev repos +
  framework integrations (LiteLLM, LangChain, Vercel AI, Mastra, Eliza, Ax,
  Composio); all 87 repos cloned to /home/user/workspace/jev-archive for
  hourly refresh.
- New measured recipes added to notes.md: foreman supervision loop, pi-jev
  gate thresholds, pi-warden 6→0 paired-run result, winnow relevance sieve,
  fast-jev-compaction two-noul rule, skill-router gates (0.30/0.40, shortlist
  3, 94.4% vs 70.8%), calibration ECE 0.0313 vs 32% OOD collapse (Archer
  Hume), Every 777-judgment eval, Near Here moderation numbers.
- Skill: added references/agent-self-assessment.md (agent self-supervision
  lifecycle, grounding/citation checks, skill callability testing) and two
  mapping-index rows; validation.md dogfooding section still canonical.

### 2026-09-17/18 (initial)
- Baseline research archive (sources.json, notes.md), augustus skill with
  mappings + validation references, evaluator script, hourly refresh script,
  Claude plugin marketplace manifest.

### 2026-09-18 (topic-index pass 3)
- Fixed census method: exact GitHub search paginated (700 repos created since
  09-14 captured; 700-result cap noted) + topics/jev crawl → ~80 additional
  repos; archive now 184 clones. Miss-cause documented: earlier star-sorted
  limit-40 search cut the low-star tail (incl. both MCTS repos).
- Skill: MCTS mapping promoted experimental → empirical recipe (grounded vs
  speculative fidelity in types; probes-only concession; measured 24/24 vs
  1/24 greedy); agent-self-assessment.md gains the judge-variance recipe
  (Jev judge 224-279x more consistent than LLM judge over 100 reps).

### 2026-09-18 (pass 4 — optimizers + official skills + clone audit)
- ax Jev support documented from source (native adapter details, trueThreshold
  semantics, fail-closed mapping validation); new reference
  optimizer-integration.md covering Ax + DSPy typesafeify + jev-dspy-lab.
- typesafeainate/dspy-typesafeify cloned; official typesafe-ai/skills already
  archived and layered-on (never duplicated).
- Clone audit: repos.txt deduped (185 unique), 0 missing on disk, no failures.

### 2026-09-18 (pass 5 — toolbox sweep meta-method)
- New references/toolbox-mapping.md: the how-to-find-approaches-and-
  applications procedure (judgment-shaped-hole substitution, newly-feasible
  classification via economics inversion, standing rejections list); wired
  into SKILL.md central model + index row.

### 2026-09-18 (pass 6 — named-methods + operators/theorems tier)
- references/methods-catalog.md: ~20 named algorithms (CatBoost row is
  Empirical via autoresearch cookbook) + operators/theorems tier with
  precondition-carrying rule; wired into SKILL.md index and toolbox sweep.

### 2026-09-18 (pass 7 — composition algebra as application generator)
- references/composition-algebra.md: 11-position grammar of Jev-vs-construct
  relations, logical-operator combination rules, and the position×construct
  traversal as the systematic application generator; wired into SKILL.md
  index + toolbox sweep.
