# Decision jobs and how bounded models are applied

Date: 2026-09-23. This note answers a placement question: which decision jobs a
bounded model can help with, how those models are wired, and when a classical
method, a simple baseline, or no model should win. It is not a directory of
repositories and not a median of published practice.

TypeSafe Jev remains the default hosted exemplar for a typed decision head.
The jobs below are properties of the decision, not of that product. No
occupancy id is assigned here.

## Acceptance brief

**Problem.** An agent using Augustus needs a map of decision jobs, wiring
patterns, and no-model wins, without a literature or popularity catalog.

**Baseline relied on.** Installed guidance at `cad6335` (published skill
0.7.0), quoted by path and section below. v0.7.0 release notes describe the
engine as find/build/evaluate/improve, and they explicitly refuse a consensus
survey.

**Proposed improvement.** Keep the job-and-wiring map in this note. Promote
only the non-equivalence of entropy, top-option mass, and handler-specific
deferral, because that changes which policy an agent writes down before it
places a model.

**Counterexamples that would reject this note.** A table of projects. A
"best practice" with no falsifier. A new row that does not change place,
refuse, or baseline. A soft score treated as permission.

## What the skill already decides

These sections are the baseline. The job table does not replace them.

| Baseline | What it already owns |
| --- | --- |
| `SKILL.md`, Working protocol and Boundaries | Evidence, then bounded judgment, then explicit policy, then checked action. A typed output is not truth, calibration, authority, or execution. Near 0.5 does not diagnose why a model is uncertain. A score cannot grant permission. |
| `references/applied-mappings.md` §§1–9 | Nine placements: context sieve, exact keep/drop, harness triage, rank versus moderation, skill routing, expensive observation, human-confirmed gate, generator leftover, closed-vote computer use. Each names the owner of the act and the failure fallback. |
| `references/mixed-architecture.md`, Cost-sensitive prefilter and Dual orchestration | Per-action fallback table. "Fail open" is undefined until the action is named. The second stage sees the selected residual. Judgment-as-tool versus judgment-as-outer-controller. |
| `references/composition-algebra.md`, The positions | Eleven positions, including gate, post-judge, selector, and comparator. Evidence is not authority. |
| `references/mappings.md` §2 and §7 | Elkan/Bayes threshold is theory only with calibration and an adequate loss. Signal detection separates the criterion from accuracy. |
| `references/validation.md`, Costs, abstention | Abstention is an action. Constant review cost does not make the human perfect. Report selective error and total population cost. Always-positive, always-negative, and defer-all are baselines. Selective ranking does not universally require calibration (`tests/skill_cases.json` `selective_margin`). |
| `references/methods-catalog.md`, Information theory | Entropy is uncertainty inside the offered distribution. Low entropy can be confidently wrong or can omit the right option. |
| `references/judgment-class.md`, Entropy as allocator (before this pass) | Uncertainty routing is a hypothesis. 0.5 is not a universal boundary. It did not say that entropy and top-option mass can reverse, or that accepted-slice risk omits the handler. |

v0.7.0 release notes (`docs/release-notes-v0.7.0.md`, "The important shift"):
research is input, not a finished survey. That constraint is why most of this
note stays in `research/`.

## Decision jobs

Each job is a hole a bounded model might fill. Output type is the model's
product. The act owner is never the model. The baseline must be allowed to
win.

| Job | Inputs the model may see | Output type | Who owns the act | No-model / classical baseline | Failure if the model is wired wrong |
| --- | --- | --- | --- | --- | --- |
| **Route** | Live eligible menu plus the case. Exact grants already applied. | Label in the menu, plus `none`/`other` when coverage is open. A rank is only a shortlist. | Host dispatch after argument, authority, and state checks. | Explicit user choice, exact schema match, lexical/BM25 shortlist, or a declared default handler. | A selected tool is treated as permission. Missing `none` forces an unsubscribe request into billing. |
| **Triage** | Case features and queue state the policy is allowed to use. | Ordinal priority or a small priority label. Not a permit. | Queue policy: eligibility, SLA, ownership, starvation limits. A person does the work. | FIFO, deadline rules, severity keywords, SLA buckets. | A soft priority starves a protected class, or a low score closes the case. |
| **Admit / reject** | Evidence sufficient for one binary act, with costs. | Probability of the stated event, or a label only if policy does not need the probability. | Policy applies the cost matrix. Irreversible admits need an exact allow and, where required, a person. | Always-admit, always-reject, or a rule on exact fields. Elkan: if one row of the cost matrix dominates, label-all is optimal. | An uncalibrated 0.9 from a generator, or a ranker's 0.92, is used as `P(permit)`. |
| **Rank within a menu** | Query plus candidates the retriever already returned. | Order or a within-list score. | Presentation or a later decision stage. On model failure, keep the source order. | Retrieval order, recency, exact features, BM25. | The listwise score is thresholded as a calibrated permit. Omitted candidates cannot be rescued. |
| **Selective accept** | A score that ranks "more confident" on the same population. | Accept versus abstain. The reported risk is error among accepted cases, divided by coverage. | The abstention handler must be named. Until the handler's own loss is in the objective, this job is not deferral. | Always-accept and always-abstain. A margin or top-mass ranking is a legal score. It does not have to be a calibrated probability. | Selective error is quoted as the error of the whole population, including cases a person or second model handled badly. A guarantee is claimed after the threshold was chosen on the same cases. |
| **Defer to a named handler** | The case, and samples or a model of that handler's decisions. | Predict versus defer. Under 0-1 loss, the Bayes rule defers when top class probability is at most `P(handler correct \| x)`, plus any query cost in the loss. | The handler (person, stronger model, or exact procedure) produces the deferred decision. Policy still checks authority before effects. | Always-defer, always-act, and constant-cost reject. Constant cost is valid only when the handler's loss really does not depend on the case. | A frozen head's entropy band is described as adapted to the handler's strengths. The classifier was trained on the whole population and never saw where the handler is already reliable. |
| **Detect, then escalate** | A evidence score plus base rate. | A detection score. The criterion is a policy choice on the ROC/PR curve. | Escalation owner: a person, an interlock, or a second procedure. The detector does not clear the hazard. | Exact monitor, control chart, checklist, or a single threshold on a measured physical variable. | Accuracy at 0.5 is the operating point. Rare harms disappear into accuracy. A post-action monitor is treated as prevention. |

Route, triage, and rank are already placements in `applied-mappings.md` §§4–5
and `mixed-architecture.md`. Admit/reject is mappings §2 plus validation.
Selective accept versus deferral was the missing split. Detect-then-escalate
is mappings §7 plus the runtime-assurance card: a monitor after an
irreversible effect is detection, not prevention.

## Wiring patterns

| Wiring | When it helps | When it lies | No-model alternative |
| --- | --- | --- | --- |
| **Pre-gate** | Most cases are easy and exact filters already ran. The gate only buys a more expensive observation, generator, or review. On gate failure, take the safe direction for that action: keep evidence, run the observation, or withhold the mutation. | The residual is harder than the traffic the gate was measured on, and the budget still uses the old error rate. Or the gate drops evidence that cannot be recalled. | Rules, types, and allowlists first. Skip the gate when the unfiltered path already meets the quality, recall, latency, and cost targets. |
| **Post-judge** | The thing to be judged now exists: a diff, a draft, a solver trace. The judge sees that artifact and returns a named quality. Policy chooses warn, review, or block. | The judge is the only veto on an irreversible act, or it scores a vague "is this good?" instead of one atomic question. | Linters, schemas, tests, and proof checkers own machine-checkable defects. Shadow the soft score before it can block. |
| **Option menu in code** | The host enumerated the legal actions, spans, or tools from live state. The model points at an id. Code copies bytes or calls the existing handler and re-checks state. | The menu is incomplete and there is no `none`. The model is allowed to invent a selector, a quote, or a permission. | If the menu has one legal element, or an exact match already selects it, do not call the model. |
| **Dual-loop entropy routing** | Only as a measured hypothesis: entropy on this provider orders errors well enough that the expensive arm's gain exceeds its cost on the cases it actually receives. | K>2 and the team thinks entropy is top-mass. See the arithmetic below. Or low entropy is confidently wrong because the true option was never offered. | Route with rules, a top-mass or margin score evaluated as selective classification, or always use the cheaper or the stronger procedure. |
| **Human floor** | Irreversible, high-cost, or legally dual-control acts. The model may order the queue. It does not replace either approver. | The score is treated as the second signature, or abstention cost assumes a perfect, instant reviewer. | Two-person rule, allowlist, and exact authorization with no model in the approval path. |
| **Fail-open vs fail-closed** | Useful only after the action is named. Preserve source order on a ranker failure. Keep context on a sieve failure. Do not execute a mutating tool on timeout. | A family-wide slogan. Provider timeout is neither approval nor rejection until mapped. | The declared default for that action, including "do not call a model." |
| **Classical operations research or rules first** | Schemas, counts, dates, capacity, permissions, and settlement are decidable exactly. Judgment estimates one semantic feature inside a solver or labels only the unresolved remainder. | The model replaces the solver, or "unresolved" is stored as "safe." | The solver, the decision table, or the checklist alone, when the semantic hole is empty. |

Positions for these wirings already exist: gate, post-judge, selector,
comparator, budget signal (`composition-algebra.md`). This table says when
each wiring is the wrong join.

## Primary findings

Retrieval time for all three artifacts: 2026-09-23. Local entropy arithmetic
was run the same day with Python 3 on the fractions below. No model was
called. ImageNet and CIFAR numbers in the papers were not reproduced.

### Geifman and El-Yaniv, selective classification

Source ID: arXiv:1705.08500v2 (abs page current version, submitted 2017-06-01).
URL: https://arxiv.org/abs/1705.08500v2. Body: ar5iv HTML, full text through
the concluding remarks. Prior card: none in `sources.json`; Chow-style
abstention is notes.md §21 and validation.md, without this paper's
risk-coverage definition.

**Claim (theory, their setting).** A selective classifier is a pair `(f, g)`.
Coverage is `E[g(x)]`. Selective risk is `E[loss · g] / coverage` (their
equation 1). The rejected region is outside that risk. Softmax response,
`max_j f(x|j)`, is a confidence-rate function: it only needs to rank. The
authors write that they do not have a rigorous explanation for it, and that
softmax values are often treated as probabilities but need not be for this
use. Selection with guaranteed risk (their Theorem 3.2) is a binomial
inversion bound over the binary-search thresholds, under i.i.d. draws from
`P`. If the score ranks badly, the bound still holds and can sit far from the
target risk.

**Reported, not ours.** Their VGG/ResNet tables, including about 2% top-5
ImageNet error at high coverage, use their training recipe and a split of the
validation set. They note they did not Bonferroni-correct across the several
target risks in a table. Do not copy those coverages.

**Design implication.** Post-hoc selective classification may threshold a
ranking score, including an uncalibrated margin, and then measure
accepted-slice risk and coverage on data not used to pick the threshold.
That measurement is not the loss of a system whose rejected cases go to a
person. **Disposition:** refine-reference. **Falsifier:** on a held-out
population, the accepted-slice error looks acceptable while population loss
including the handler exceeds always-defer or always-act.

### Mozannar and Sontag, learning to defer

Source ID: arXiv:2006.01862v3 (abs page current version, 2021-01-25).
URL: https://arxiv.org/abs/2006.01862v3. Body: ar5iv HTML through §5.2.
Appendix proofs and the experimental tables were not inspected. Prior card:
none. Validation.md already says a constant review cost does not make the
human perfect; it does not state this Bayes rule.

**Claim (theory).** System loss charges the classifier's loss when it
predicts and the expert's loss when it defers (their equation 3, 0-1 case).
The Bayes classifier is ordinary top-class prediction. The Bayes rejector
defers when `max_y η_y(x) ≤ P(Y = M | X = x)` (their Proposition 2). Constant
deferral cost is the special case that recovers rejection learning, not the
general expert problem. Section 5.1: training the classifier on the whole
population, then comparing confidences, can miss a simple split where the
expert already solves one group and the model should fit only the other.
That example assumes a limited hypothesis class. It is a counterexample to
"threshold a frozen head and call it expert-adapted," not a claim that every
frozen head loses.

**Design implication.** If the fallback is a specific person or second model,
the objective is system loss on both slices. A hosted decision head that
cannot be retrained on that handler's mistakes stays in the post-hoc
selective job unless a separate rejector is trained and evaluated.
**Disposition:** refine-reference. **Falsifier:** the entropy or top-mass
band's system loss, counting handler mistakes and query cost, loses to
always-defer or to a rejector that sees handler outcomes. Their CIFAR and
hate-speech numbers were not inspected and are not evidence here.

### Elkan, cost-sensitive decisions

Source ID: Elkan, IJCAI 2001, https://cseweb.ucsd.edu/~elkan/rescale.pdf.
Local PDF sha256
`46f46ba7aaab3df82aa09643c51549ee327ec1734bdf9829debd6101da35c048`
(96,603 bytes). Prior card: `sources.json` and notes.md §21.

**Inspected.** Abstract, §1 reasonableness, §1.2 baseline warning, §1.3
prose, Theorem 1's statement. **Not re-derived:** equation (2). The PDF
text extraction does not yield the glyphs, so this pass does not confirm the
algebra from the file. The zero-correct-cost special case already in
validation.md stays the prior formula.

**Claim (prose).** Predict the class with lower expected cost. That can be
the less probable class. If a cost-matrix row dominates, never predict the
dominated label; the extreme is label-all-positive or label-all-negative.
Example-dependent costs (his credit-card amount) change the threshold per
case. When the learner already returns probabilities, he recommends applying
the decision threshold explicitly rather than only rebalancing training data.

**Design implication.** Admit/reject without a reject option is this job. A
dominated cost matrix is a no-model win, not a prompt to add a classifier.
**Disposition:** archive-only for the formula; the dominated-row no-model
case is part of the job table above and of the judgment-class two-act
bullet, which points at validation.md instead of restating a glyph we could
not read. **Falsifier:** a reasonable cost matrix where label-all has lower
expected cost than the model policy on a held-out set.

### Local arithmetic (reproduced)

Binary entropy at (0.6, 0.4) is 0.970951 bits. For ten outcomes with masses
0.8 and nine times 0.2/9, entropy is 1.355913 bits. On a grid of binary
max-probabilities from 0.51 to 0.99 in steps of 0.01, entropy strictly
decreases as the max increases. So:

- two options: entropy order and top-mass order agree;
- three or more options: they can reverse, as in the pair above.

This is arithmetic on declared distributions, not a measurement of any
provider. **Disposition:** refine-reference. **Falsifier:** a provider whose
Choice support is always binary, or a held-out set where the two scores
induce the same accepts and the same system loss.

## Dispositions that do not move guidance

| Finding | Disposition | Why it does not get its own row |
| --- | --- | --- |
| Restating the nine applied-mapping cards as "use cases" | archive-only | An agent already has those cards. Another list would not change place or refuse. |
| Pre-gate, post-judge, menus, fail-open/closed, rules-first | archive-only | `mixed-architecture.md` and `composition-algebra.md` already name the joins and the per-action fallback. |
| Human floor is not a second approver | archive-only | methods-catalog already rejects the two-person rule as a model substitute. |
| Selective classification requires calibration | rejected | Geifman uses SR as a rank key. `selective_margin` already forbids a universal calibration prerequisite. |
| Copy Geifman ImageNet coverage or Mozannar task numbers into a reference | rejected | Reported on their populations. Not a threshold to install. |
| New SKILL survey section or README use-case wall | rejected | Ceilings and the anti-catalog rule. The entry point only gains a route phrase and the development version. |

## Promotion

**Old rule.** `judgment-class.md` "Entropy as allocator" treated uncertainty
as one hypothesis for sending a middle band to a stronger model or a person.

**Revised rule.** Name two-act expected cost, post-hoc selective ranking, or
deferral to a named handler. Entropy and top-option mass agree on a binary
menu and can reverse otherwise. Accepted-slice risk is not handler-inclusive
system loss. A frozen head is not an expert-adapted rejector. Compare
always-act, always-defer, and the other score. The soft score still does not
own the act.

**Scope.** Choice-like distributions used to accept, abstain, or escalate.
Not a new family. Not a claim that Jev, or any peer, is miscalibrated.

**Target.** `references/judgment-class.md`, that section. SKILL.md routes
"uncertainty routing" to the same reference. Version **0.7.1-dev** because
installed wording changed. Published 0.7.0 is unchanged until a release.

The reference byte ceiling is 180,000. The class-choice checklist in
`judgment-class.md` duplicated the skill's decision-design card, so it became
a pointer plus output species, coverage, and the family-matched metric.
Cascade cost fields remain on the skill card and in `mixed-architecture.md`.

**Falsifier for the promotion.** A binary-only menu, where the distinction
is idle, or a held-out system-loss comparison in which entropy routing wins
and the text is then too conservative. Conservatism is acceptable until that
comparison exists. The reverse failure is an agent requiring calibration
before a measured margin may abstain: the new text explicitly does not
require that.

## Unrun

No provider calls, no threshold sweep on real tickets, no reproduction of
Geifman or Mozannar experiments, no Elkan equation re-derivation from glyphs.
The next useful experiment is a paired holdout with three policies — entropy
band, top-mass band, always-defer — scored by population loss including the
handler, on a menu with more than two options.
