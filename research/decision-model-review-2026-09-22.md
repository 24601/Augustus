# Full research refresh — 2026-09-22

This refresh follows the broad [September 21 review](decision-model-review-2026-09-21.md)
and the last archived hourly scan at **2026-09-22T04:44Z**. It supports
**0.7.0**, following the user's later mission clarification and the
[decision-engine extension](decision-engine-2026-09-22.md). The original 0.6.1
patch plan was not published. This is not a new provider integration,
model implementation, or measured application improvement. Primary inspection
occurred September 22, approximately 15:30–16:05 UTC. Source-specific retrieval
times and full revisions are in the [source packet](archive/2026-09-22-refresh/source-snapshots.json).
Independent Astra re-derivation and integration followed that window; their
separate times, scope, and findings are linked in the [acceptance ledger](audits/2026-09-22-refresh-acceptance.md).

## Coverage and limits

| Surface | Work completed | What that establishes |
| --- | --- | --- |
| GitHub ecosystem | Four paginated query partitions across Jev, System One and decision-model searches; split the over-1,000-result Jev query; 1,772 unique node IDs | Metadata discovery, not 1,772 code audits |
| GitHub methods | Nine additional query families: calibration, conformal, decision-focused learning, routing, prompt optimization, GLiNER, GLiClass, TabPFN, policy learning; 993 returned rows, 985 unique node IDs | Broad class/method discovery; stemming also returns unrelated projects |
| Hugging Face | `jev`, `gliclass`, `gliner`, `tabpfn`, newest-modified first; 350 metadata rows, each query reached older-than-cutoff entries on page one; 16 Jev entries newer than cutoff | Model discovery, not weight execution or a complete Hub census |
| Jevusers main list | Homepage plus its linked JSON API: all 400 tracked entries, not just the visible top 100 | Complete traversal of the observed tracked list |
| Jevusers apps | All 1,299 rows across 12 categories; combined with tracked list, 1,519 distinct repository names | Complete observed directory traversal; selected primary sources inspected below |
| Provider | Official model, confidence, jaggedness and Python changelog pages; official SDK/adapter revisions | Current documented contracts and bounded release changes |
| Papers/web | Primary arXiv abstracts and relevant full-text methods for selective certification, strategic DFL, and drift-aware routing | Research watch and a classical finite-support correction, not reproduced SOTA |

Receipts: [GitHub](archive/2026-09-22-refresh/github-discovery.json),
[method search](archive/2026-09-22-refresh/method-discovery.json),
[Hub](archive/2026-09-22-refresh/huggingface-discovery.json),
[directory](archive/2026-09-22-refresh/jevusers-inventory.json).
The GitHub Jev interval was 04:44–15:35 UTC, split at 10:00; broader queries
cover September 21–22. Live GitHub totals moved during pagination; these are
completed page traversals, not immutable point-in-time censuses. Directory
descriptions and evaluation-category leads were triaged for design relevance,
not ranked by stars. All 127 Eval/Align app descriptions were considered;
primary-artifact depth is stated below. No claim of reviewing every linked repo.

No paid search, provider inference, third-party code execution, model-weight
download, private receipt access, or directory submission occurred. Web-tool
fetches of some TypeSafe/Hugging Face pages failed; direct public HTTP retrieval
succeeded. Directory retrieval with Python's default client returned 403;
ordinary curl succeeded. Missing evidence is not evidence of nonexistent models.

## Requested sources: completed dispositions

### Jev-Omni — revisit of notes §156

Canonical [model](https://huggingface.co/akhilaaa3/Jev-Omni), prior revision
`3e885f2951a126c41c7599ed719f98cc3088d8ed`, inspected revision
`55b53f2ec1b4c656c8a6172b0c7555ae578a9c3f`, modified 14:17:29 UTC.
Read the pinned card, `decision_config.json`, `verification.json`,
`load_model.py`, and `jev_omni.py`; inspected the file inventory without weights.

**Reported:** finite-option text/image/audio/video classification on a Gemma
backbone. The card adds video evidence and operating details; its text accuracy,
ECE, and warm-H200 timings are author measurements, not ours. The code's audio
path clips at 30 seconds and its video default samples 16 frames. The public
multimodal loader requires CUDA and separately obtains base-model components.
The inspected video path sends sampled images, not the video's audio track;
its example download calls leave base/model revisions unpinned.
Its `confidence` is maximum option probability. A 256-output head does not
establish quality for 256 choices; the card's strongest support is at most 20.
The verification file distinguishes a large approximate-merge probability
difference from the much smaller FP32 comparison; matching argmax is not full
probability equivalence. No local execution validated either path.

The linked [DecisionBench card](https://huggingface.co/datasets/akhilaaa3/decision-bench/blob/19334fec40b54b693a63e1ffd91636651d39e847/README.md)
uses synthetic 80-scenario/293-question subsets and excludes missing answers
and refusals, and counts only the last retry's cost. Its one-question-per-request framing for Jev conflicts with
[TypeSafe's documented shared-state batching](https://docs.typesafe.ai/models).
Jev-Omni's chart uses a different model's token price as a cost proxy. These
are reported protocol-specific results, not measured equal-quality serving
cost comparisons. The model card's training-total description and the config's
24,000-example final-stage recipe are different scopes, not independently
verified training provenance.

**Disposition:** refine multimodal observation-window and cost-boundary guidance.
Counterexample: a decisive fault between sampled frames. Falsifier: measure
event recall and false sign-offs with controlled off-window events; include
preprocessing, hardware, cache and fallback costs. We did not run this experiment.

### decision-model-testing — material revisit of notes §163

Canonical [repository](https://github.com/dorkitude/decision-model-testing),
`7af400ed6c923146b0b03167372839e38b75b4f5` →
`ba6a5e2e9a60161564ead92a932ccbf3f88e4497`.
The prior thin-stub description is historically correct but no longer describes
the inspected tree. It now exports four experiments: judges, Kimi RAG,
Claude RAG, and reranking. Read all four READMEs and the reproduction document;
inspected the tree, both RAG aggregate summaries, cascade JSON and statistical
aggregation source. This is not a full code/security audit.

**Reported:** Kimi's 100 paired questions retain 307/2,020 chunks, with 98/100
DeepSeek-judge acceptance in both arms; Jev judging differs between arms.
Claude's categorical run has 96/100 in both arms but one win and one loss,
with its reported paired interval spanning −3 to +3 percentage points. Equal
totals are not equivalence. The reranker follow-up uses nine prompts on a
reused 97-query sample: useful exploration, not proof that methods are equal.

Judge cascades include both wins and losses. The 513-case Jev→GPT-OSS simulation
reports 80.12% versus 76.41% strict label agreement and a 0.563 accounting-cost
ratio; LLMBar→Qwen loses about 3.52 points. The JSON distinguishes unknown-cost
attempts from known subtotals; the Go aggregator gives invalid required stages
zero strict score and preserves benchmark-specific weighting. Intervals are
not adjusted across the multiple explored comparisons.

**Evidence boundary:** source-bearing answers, historical receipts and the
original history remain private. Public numeric projections include original
hashes but cannot reconstruct a receipt-level audit. Synthetic checks are not
historical replay. Fresh RAG replication requires private index construction,
credentials and paid inference. Cost estimates exclude some infrastructure;
RAG timers exclude initial retrieval/filtering. Claude costs are API-equivalent,
not incremental subscription charges. None of these runs was reproduced here.

**Disposition:** refine complete-workflow accounting, matched comparisons and
reproducibility language. Keep negative cascades. Falsifier: a fresh paired
question set loses evidence recall, exceeds a prespecified quality-loss margin,
or has no savings once all stages and actual cache behavior are included.

### pijev — first canonical card

Canonical [repository](https://github.com/TypeLLM/pijev), revision
`bca3a73d6419b794d63cd780ba4a0254579d7ccc`. Read README, aggregation/request
implementation and mocked-transport tests; inspected tree and example scope.

**Contract from inspected source:** expands Choice questions into distinct
option orders, aligns by label, checks returned support/mass, averages
probabilities and preserves non-Choice answers. Default budget is up to eight
orders; a 720-expanded-question cap does not supersede provider token limits.
Choice `confidence` becomes the winning mean probability, not native Jev
confidence. Canonical sorting plus a fixed seed can stabilize sampled orders
against input dictionary reordering; it does not freeze provider randomness.

**Mathematical implication:** convex loss of an average is at most mean loss
of its members, not loss of the best member. Neither calibration nor action
safety follows. For true-label probabilities 0.8 and 0.4, mean prediction 0.6
has log loss 0.5108 versus best-member 0.2231 and mean-member loss 0.5697.
This arithmetic was checked locally; provider quality was not. Mock transport
tests check mechanics, not real calibration. Example ordering variation alone
does not establish a population benefit.

**Disposition:** refine composition and score-contract guidance. Counterexample:
a correct high-probability member diluted across the action threshold.
Falsifier: frozen paired holdout comparing canonical single-order and bounded
averaging at matched policy costs, including actual added question/token usage.

### Jevusers main and apps — discovery, not endorsement

Read [main](https://jevusers.com/), [apps](https://jevusers.com/apps),
[methodology](https://jevusers.com/about), and the linked public API.
The main directory describes daily keyword/README discovery and star ranking;
apps aggregates curated lists. Correlated inclusion is not independent quality
evidence. Evaluation, routing, runtime and compaction leads informed source
selection; browser/mobile/IoT examples remain architectural leads, not new
model families merely because a port exists.

**Disposition:** archive complete URL/category inventories and inspect selected
primary evidence. `24601/Augustus` is already present in both inventories under
Coding Agent. This verifies listing presence, not search rank, traffic, installs
or user benefit. No duplicate submission or unsolicited outreach was made.

## Other material revisits and evidence checks

Full pins and retrieval dates are in the source packet. “Inspected” below does
not mean reproduced, and code availability does not upgrade Reported numbers.

| Canonical source | Inspected change/evidence | Disposition |
| --- | --- | --- |
| `typesafe-ai/skills` | HEAD still `65a39f3…`, matching existing v0.5.7 pin | Keep historical pin; no invented upstream update |
| Official TypeSafe docs | Models still text-only Jev 1.13.0; aliases, concentration-style confidence, batching and jaggedness checked | Current Contract; example thresholds/performance prose are not validated local policy |
| `typesafe-ai/typesafe-sdk-python` | v0.7.1 changelog: early key validation with exception-value exclusion; v0.7.0 Pydantic transition remains relevant | Archive integration delta; no SDK vendored |
| `typesafe-ai/system-one-adapter-python` | v0.2.1 `e1d4cc9…` adds Gemini; diff distinguishes refusals/incomplete outputs from malformed-output retries, and missing usage from zero | Refine accounting boundary; no equivalence from adapter shape |
| `TheoLeeCJ/SemIf` | `ca3ba65…` → `1f2dea3…`; README diff and calibration method. Adds CPU/Apple/EXL3 paths and group-disjoint out-of-fold temperature scaling; pooled-vs-local control is inconclusive | Calibration is a separate versioned step; argmax preservation does not preserve threshold actions |
| `jaredpalmer/kev` | `90990a5…` → `1c35199…`; commit/README diff changes serving default to BF16 while benchmark path stays FP32; author has small precision timing probes | Requalify serving precision, do not transfer rounded agreement to policy parity |
| `wfzyx/von` | `bed7e73…` → `581b874…`; commit/README changes include v1.1 and input-conditioned temperature fitted to public benchmark tiers | Public-benchmark-informed calibration needs fresh independent evaluation; do not market tuned benchmark as untouched holdout |
| `willkelly/jev-evaluation` | Pinned README: preregistered synthetic/solver-label experiments, semantic controls, referent sensitivity and authority-shaped attacks; external raw-log manifest is a lead, not downloaded | Refine explicit subject references; other lessons already covered. Reported run, not our reproduction |
| `cwhy/decision-injection-bench` | Pinned README: clean/length-matched controls, authored multilingual cases, varying eligible denominators and label-changing adaptive attacks | Refine controls and claim language; neither repeated calls nor valid schemas prove safety |
| `ReallyArtificial/stuntdouble` | Pinned README: policy-level shadow replay; launch used Kev-0.8B/Laya, not Jev; agreement limits explicitly stated | Agreement is not truth; authorization/privacy of shadow destinations must be explicit |

The remaining collected GitHub sources—including GLiClass, GLiNER/GLiNER2,
TabPFN, GEPA, RouteLLM, NanoJev, Nimble, JevBench, OOD calibration, LCC and
other runtime/reranking/compaction leads—received **metadata/fingerprint
triage only in this pass** unless named above. Their baseline conceptual
review remains September 21. No unchanged-capability or freshness claim is
inferred from a metadata fetch, and their last-reviewed timestamps are not
advanced. New Hub ports and weights likewise remain discovery leads.

## Classical and emerging methods

These September papers predate the last hourly scan; they are newly inspected
catch-up literature, not falsely presented as September 22 publications.

- **[Available Guardrails, v1](https://arxiv.org/abs/2609.22048v1), September 18.**
  Read abstract and methods §§3.1–3.4. Separates certificate validity from
  having enough accepted samples per reporting unit; uses exact binomial
  inversion, separate planning/certification data, and partition optimization.
  Its dynamic program optimizes a restricted, approximate planning objective,
  not a universal guaranteed coverage optimum. Promote only classical support
  planning; the proposed optimizer and reported experiments remain research watch.
- **[Strategic Decision Focused Learning, v1](https://arxiv.org/abs/2609.14907v1),
  September 14.** Read abstract and relevant game/accuracy propositions. Other
  agents' best responses can make prediction accuracy and equilibrium payoff
  non-monotone under the stated game assumptions. Investigate for incentives
  and adversarial allocation; do not generalize its existence results into a
  universal claim that accuracy hurts. No new runtime recipe without a concrete
  strategic application and falsifier.
- **[Drift-Aware LLM Routing, v1](https://arxiv.org/abs/2609.00662v1), September 1.**
  Read abstract, architecture and evaluation-scope sections. Rolling sparse
  estimates, audit feedback and a separate hard budget meter; reported numerical
  study is synthetic, with a real-data protocol rather than live acceptance.
  Archive as a concrete research candidate; existing runtime already separates
  rewards, drift, route-conditioned evaluation and exact resource constraints.
- **[Decision-Focused Learning tutorial](https://arxiv.org/abs/2606.21773), June 19.**
  Abstract-level rediscovery only. Prediction distance need not track downstream
  regret. Existing DFL guidance already makes this distinction; no promotion
  based on an abstract alone.

## Promotions, falsifiers and unrun work

The initial refresh refined five references. Astra re-derivation extends the
integrated patch to twelve existing references, with no research feed added to
the entry point. The scenario set grows from 12 to 27. The research design
changes are: version adapter/aggregation semantics; bound ensemble
claims; inspect media observation coverage; measure the complete cascade; plan
accepted-case support and preserve valid injection-test denominators.

The independent redo additionally corrects unnecessary training/filtering and
calibration requirements, all-dimensions-win acceptance, runtime detection versus
prevention, Alloy temporal scope, Jensen equality, and distillation overclaims.
The helper/checker corrections and 70-test suite are tracked in the acceptance
ledger rather than presented as model-research results.

Local arithmetic checked: zero errors in 20 IID accepted cases gives a
one-sided 95% upper error bound of about 13.9%; 299 error-free cases are needed
for a single fixed 1% bound. With 41 simultaneous units and a simple Bonferroni
allocation, the analogous zero-error minimum is 668 per unit. These calculations
do not certify any deployed model. Our helper does not implement certification.

Still unrun: provider permutation comparison, multimodal inference, benchmark
receipt replay, fresh RAG noninferiority/cost experiment, privacy-approved shadow
trial, independent calibration after public-benchmark tuning, and the new
papers' algorithms. No source's benchmark was upgraded to Reproduced.

The [protocol](protocol.md) and [fold prompt](prompts/research-fold.md) now require
coverage depth, requested-source closure and accounting checks. The
[release checklist](release-checklist.md) adds public metadata and deployment
read-back. GitHub's About description was corrected to the class-wide mission
and read back; external listings may refresh on their own schedule.
The mutable official documents also have [fresh digest receipts](archive/2026-09-22-refresh/official-doc-receipts.json)
from 16:28–16:29 UTC. These later captures are explicitly not retrospective
evidence of the earlier response bodies. The [Astra discovery audit](audits/2026-09-22-astra-redo-discoverability.md)
records stale Jevusers wording and a missing Skills-directory preview, separately
from successful listing presence and installation checks.

Repository/behavioral acceptance and release evidence are recorded separately
in the [refresh audit](audits/2026-09-22-refresh-acceptance.md). Publication is
not inferred from this research report.
