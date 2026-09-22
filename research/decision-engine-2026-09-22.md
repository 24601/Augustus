# From research synthesis to an agent's working decision engine

Date: 2026-09-22. This is an extension after the initial full refresh, prompted
by the user's clarification: Augustus should equip agents to discover, apply,
build, evaluate and hill-climb decision-model systems, not become a median
survey of the ecosystem. It changes the planned release from 0.6.1 to **0.7.0**.
The patch candidate was never published.

## Finding and implementation

The existing skill had useful classical methods and a placement grammar, but
the path from a composition to an executable evaluation/improvement loop was
too implicit. A taxonomy of positions is not yet a calculus of valid joins.
An independent [Astra foundations audit](audits/2026-09-22-astra-composition-foundations.md)
challenged the stronger engine claim and derived eight bounded obligations/laws.

Implemented:

- The entry point and public discovery surfaces now name the agent's full job:
  find, build, evaluate and improve; respond with implementation when requested.
- The composition reference adds typed quantity/population/time/regime joins,
  branch loss, selected-cascade risk, union budgets, bounded-loss decision regret,
  joint-information substitution, learned-parameter-aware data processing, and
  closed-loop outcomes. Proof assumptions remain distinct from empirical facts.
- The optimizer reference supplies an incumbent–challenger execution loop:
  runnable baseline, provider/policy seams, outcome capture, bounded search,
  isolated confirmation, authorized promotion, monitoring and rollback.
- `compare_workflows.py` consumes paired bounded episode losses, cost/latency
  observations, constraint violations and provenance. Search is descriptive;
  confirmation uses a conservative fixed-sample Hoeffding bound with a declared
  prespecified comparison family. It never executes or deploys a policy.
- Fourteen new helper tests and four exact finite composition tests increase
  the suite to 88. The latter enumerate 18,225 bounded-loss regret configurations,
  branch/cascade accounting, dependent failure events and the XOR side-information
  counterexample. These are arithmetic/software fixtures, not measured model gains.
- Four additional independent behavioral scenarios cover composition and
  improvement traps. A fresh forward task also builds a local eval from raw
  synthetic cases; its actual output and coordinator assessment are recorded
  separately, not assumed successful here.

## Research that changed the design

This phase searched primary research on compositional risk, information value,
adaptive evaluation and prompt/program optimization. Queries included Blackwell
experiment comparison, time-uniform confidence sequences, 2026 compositional
guarantees, adaptive evaluation/holdout, GEPA and Software 3.0 methods. Search
results were leads, not reviewed evidence. The entries below state inspection
depth; no provider calls, third-party implementation runs or claimed benchmark
reproductions occurred. Older work is catch-up, not newly published today.

| Source | Inspected evidence and disposition |
| --- | --- |
| [Brooks, Frankel, Kamenica: Comparisons of Signals](https://benjaminbrooks.net/downloads/bfk_comparisons.pdf), author PDF March 2024 | Astra inspected definitions and relevant §3 theorem statements, not every proof. Isolated information order does not settle substitutability beside arbitrary background information. Promoted the joint-information seam and an exact four-world XOR counterexample. Later PDF digest receipt is in the foundations audit. |
| [Polyanskiy–Wu, 1508.06025v4](https://arxiv.org/abs/1508.06025v4) | Astra inspected channel/TV/information definitions in §1. Promoted only ordinary conditional data processing with all informative inputs represented; no stronger contraction or deployment guarantee. |
| [Performative Prediction, ICML 2020](https://proceedings.mlr.press/v119/perdomo20a.html) | Astra inspected definitions, counterexample and bounded convergence assumptions. Promoted whole-trajectory evaluation when policy changes its data distribution. Did not transfer a smooth/strongly-convex convergence result to arbitrary agents. |
| [Howard et al., 1810.08240v4](https://arxiv.org/html/1810.08240v4) | Parent read introduction and confidence-sequence scope. Time-uniform inference is a principled alternative to fixed-n peeking under a specified model, not permission for arbitrary adaptive reuse. Runtime points to it; the new helper deliberately implements fixed-sample comparison only. |
| [SHIP, 2608.21748v1](https://arxiv.org/html/2608.21748v1), August 22 | Parent inspected §3.1–3.5, experimental protocol and finite-sample proof boundary. Whole-policy selection changes the estimand. The prespecified-grid guarantee must not be attached to the paper's practical pointwise threshold search; the authors explicitly distinguish them. Target VLM loss is not automatically human truth. Promoted selection-aware trajectory/confirmation discipline, not reported T2I gains. |
| [RECAP, 2606.06698v2](https://arxiv.org/html/2606.06698v2) | Parent inspected methodology, setup and results. Reported proactive constraint updates can regress older constraints; its optimizers receive only the latest constraint and no real eval feedback, unlike our feedback-driven search loop. Retain old-constraint regression checks, but do not generalize its negative result into “GEPA never helps.” No results reproduced. |
| [Combee, 2604.04247v1](https://arxiv.org/html/2604.04247v1), April 6; [official integration guide](https://gepa-ai.github.io/gepa/guides/combee/) | Parent inspected motivation, hierarchical aggregation/shuffling/controller method and integration description. A possible scaling method when reflection aggregation loses specifics; repeated reflections are not independent evidence. Watchlist/equal-budget experiment, not a new default, mandatory parallelism, or universal speed/quality claim. |

GEPA's original paper and implementation were already independently reviewed in
the [theory/frontier redo](audits/2026-09-22-astra-redo-theory.md). Its current
public docs were revisited for the integration lead above. SmartChoices
`2304.13033` was opened only at abstract depth; no implementation or new rule
was promoted. Blackwell's original publisher page was unavailable; do not say
that original proof was read. The simple policy-set inclusion argument and
bounded-regret derivation are given explicitly in the runtime/foundations audit.

## What makes this synthesis instead of a survey

Every retained method must connect an observed failure or opportunity to a
mechanism, assumptions, implementation seam, outcome metric and counterexample.
An elegant derivation does not establish its inputs. A source's popularity or
apparent SOTA status does not establish transport to a user's workload. Negative
results and failed assumptions should remove or narrow advice, not merely grow
the catalog. A physics or biology analogy needs a units/variables/dynamics map;
otherwise it remains a hypothesis, not a new law of decision models.

The useful engine is the agent using this method plus its tools, data and host
framework—not a new autonomous serving service. This release adds practical
instructions and deterministic evaluation tooling. It does **not** demonstrate
that Augustus reliably discovers globally optimal systems, improves measured
customer outcomes, or qualifies any provider. Those require representative
user tasks and independent outcome collection over time.

## Next empirical test, not a fabricated result

Use an authorized real workflow with known outcome ownership. Freeze a simple
baseline; record where a model might improve it; build a paired, outcome-labeled
offline or properly identified trial; compare full loss, constraint violations,
fallback load and serving cost. Keep raw traces and rejected candidates. Separate
task-search results from untouched confirmation and from deployment results.
Where policies change treatment or data collection, ordinary replay may not
identify causal outcomes; use an appropriate experimental/identification design.

The [acceptance ledger](audits/2026-09-22-refresh-acceptance.md) owns actual final
checks/forward answers and the later release receipt owns publication. The
[maintenance contract](maintenance.md) keeps full reassessment separate from
metadata probes and the currently unverified external scheduler.
