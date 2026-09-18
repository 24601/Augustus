# Mental models: placing typed judgment across domains

Augustus is **design judgment for placing typed probabilistic judgment**
(the Jev-class of System One models: Choice / Score / Noul or a cousin —
`judgment-class.md`) using mathematical, logical, and algorithmic frames.
It is **not** a software-engineering-only skill. The same placement
question appears in AI systems, ordinary programs, businesses, knowledge
work, and personal practice: *what is exact, what is a narrow judgment,
what is generation, and what would prove this split wrong?*

Formal methods are **one pillar** (`formal-methods.md`), not the whole
toolbox. TypeSafe Jev is the documented exemplar, not a monopoly, and
not an API this card will invent.

**Non-negotiable, every domain:**

```text
exact work     →  code, policy, checklist, ledger, law, recipe, arithmetic
narrow judgment →  a System One–class model (or a human answering in a second)
generation     →  an LLM or a person writing
proof / types  →  a checker, a contract, a forcing function — never a Noul
```

Never launder a soft Noul as a proof, a model-check, or a safety case.
Policy *is* the code of a practice that has no repository.

**Master rule (curriculum):** judgment estimates; policy decides; the
world confirms. Irreversible concession belongs to a **probe**
(measurement, receipt, test, signed commit) — not to a Noul. TOCTOU is
the universal name for "checked with a soft estimate, then acted as if
the check were still true."

Status: frames below are **Contract** where they restate a named method's
preconditions; **Empirical recipe** where a launch-week artifact measured
them in software; **Hypothesis** where the domain example is analogical
until you label *your* cases.

## Pillars

| Pillar | What you steal | Detail |
|---|---|---|
| Decision theory & selective classification | Act / abstain / gather; expected loss | This file §decision; `mappings.md` §2 |
| Calibration & cost-sensitive thresholds | Per-action bars from *your* costs | This file §thresholds; Elkan; confidence docs |
| Value of information | Pay for another observation only if EV(info) > cost | This file §VOI |
| MCDA | Named criteria; weights in policy | This file §MCDA; `mappings.md` §1 |
| Search / control | Judgment as heuristic or sensor in a loop you own | This file §search; `methods-catalog.md` |
| Signal detection | Hits, false alarms, criterion — not "accuracy" | This file §SDT |
| Control / hysteresis | Dual thresholds; model never actuates | This file §search; `mappings.md` §9 |
| Mechanism / OR | Soft affinity; hard solver | This file §OR; `mappings.md` §15 |
| Epistemology | Evidence strength ≠ truth | This file §epistemology |
| Org / safety (Leveson) | Sensor ≠ constraint | This file §Leveson; `formal-methods.md` |
| Crossover metaphors | NATM, snap-fit, Norman, Kent, Shirky | This file §crossover |
| Formal / semi-formal | Proof vs DST vs judgment | `formal-methods.md`, `formal-semi-formal.md` |
| Class / family / objective | Decide vs locate vs categorize vs rank vs perceive | `judgment-class.md` species map |
| Boundary map / extractable-from-state | Self-contained in fed state vs needs outside knowledge | This file §boundary; atlas receipts `notes.md` §49 |

Pick the pillar from the hole, then the family, then the vendor.

## Decision theory and selective classification

Expected-utility placement
([expected utility](https://en.wikipedia.org/wiki/Expected_utility_hypothesis)):
the model returns a *belief about the state*; policy computes expected
loss of each **act** and picks. Abstention is an act with its own cost
(Chow's reject option: refuse to label when the posterior mass is too
flat — classical statement in Chow 1957/1970; modern cost-based reject
in [Bartlett & Wegkamp / NIPS 2008 lineage](https://papers.nips.cc/paper_files/paper/2008/file/3df1d4b96d8976ff5986393e8767f5b2-Paper.pdf)).

```text
belief  = Noul / Choice distribution / Score distribution   # model
acts    = {do A, do B, abstain, gather more, escalate}      # you enumerate
loss    = table you wrote                                    # policy
pick    = argmin_act  E[loss | belief]                       # arithmetic in code
```

**Transfers:** act / decline / gather / escalate from the distribution;
one threshold per *action*, not per model. **Does not:** a universal 0.8;
treating top-Choice mass as P(the world will cooperate); multiplying
parallel Nouls into a joint. A Jev-class call is factorized **marginals**
over isolated questions, not a probabilistic program: the joint lives in
code, a sequential decode, or a generative decoder, and Kleisli talk is
the exaggeration ([Meijer, 2026-09-18](https://x.com/headinthebox/status/2100984170004824221);
`judgment-class.md`). The same split allocates models: typed low- and
medium-entropy decisions are those marginals, and high-entropy
synthesis is the joint you pay a decoder to write — Atallah's buckets,
a **Hypothesis**, not a meter (`judgment-class.md`).

Specialist perception then judgment — masks, tracks, or a transcript,
then System One on that state — is composition, not a shared
multimodal model: information dies at the interface
(`judgment-class.md`). Taskset first → stage contracts → stage metrics
+ e2e → HoH hill-climb; DSPy/Ax only on the LM-program slice;
jevals/calibration for the decision slice; Harbor for product e2e
(`validation.md`, **Hypothesis**).

| Domain | Belief | Acts policy owns | Exact work |
|---|---|---|---|
| SWE | "this hunk matches the request" | stage / skip / ask | `git diff`, apply patch |
| Business | "this lead is worth a call" | call / nurture / drop | CRM, prices, quotas |
| Knowledge work | "this paper is on-question" | read now / stub / skip | citation, PDF you already have |
| Life | "this email needs a reply today" | reply / snooze / archive | calendar, send button |
| AI harness | "this step failed silently" | flag / ignore | trace you already parsed |

SWE examples are **Empirical** (git-jev-stage, OpenSmoke). The others are
**Hypothesis** until you keep a labeled log. Same card, same test: cost
curve on held-out *your* cases; score the fallback (escalation is not
automatically correct). `mappings.md` §2.

## Boundary map: extractable from state (placement judgment)

Primary mental model this hour
([jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas);
independent unofficial receipts, not a leaderboard; `notes.md` §49).
Before picking a family or a vendor, place the *task*:

> Is the correct answer fully recoverable from the `state` you hand
> the model, or does it require outside knowledge that is not in
> `state`?

| Self-contained (in the state) | Not self-contained (needs outside knowledge) |
|---|---|
| Classify / route / gate over text you already hold | Trivia / recall with no supporting passage |
| Citation / paraphrase / reversed-meaning given claim + quote | Score that needs comparison against a whole field |
| Sarcasm / entailment whose trigger is in the given text | Overlapping blurred categories (dangerous-high ECE) |
| DOM snapshot / numbered candidates → Choice | Combinatorial assembly (grid cells that must agree) |

**Empirical as that named axis, not as a knowledge-breadth estimate.**
History suite (N=3, single annotator, Chinese history; Case A ground
truth itself contested): common-knowledge item **wrong @ 0.90** with
no context (Yongzheng; Kangxi by popular convention); obscure item
near-flat **0.07** without a passage (correct by luck; informal rerun
wrong @ 0.08) → **right @ 0.97** with the passage in `state`
(Xianfeng, 0.98 mass). Teaching: **bare memory is unreliable; reading
comprehension over supplied text is reliable.** Retrieve first; put
the passage in `state`. Do not treat the atlas 30-second slogan as
the table.

**Placement, not internals.** The model is not a state machine under
the hood (distributed LM understanding: `paraphrase_support` and
`reversed_meaning_high_overlap` both judged correctly). It *is*
correctly used as a **component node** in *your* program — code owns
transitions (`mappings.md` §3). Confidence is a **statistic from the
distribution** (RLCD trains the distribution; Choice `confidence` is
how peaked it is), not a second trained correctness score.
Calibration is **population-level** and can fail **dangerous-high**:
DAIR Emotion via jev-benchmarks — 48% acc, mean conf **0.819**, 16%
of items p(correct)=0. Overlapping categories, overconfident. Plot
reliability on *your* labels before you threshold.

**Browser-use is this axis, not vision.** Strength = DOM-as-text +
speculative fan-out over candidates code already numbered — a visual
task translated into extractive text. Not screenshots. Same
component-node placement as lizard-agent / solari-reflex
(`applied-mappings.md` §2; `mixed-architecture.md`).

**Does not:** merge Banking77 87% (atlas/jev-benchmarks) with DMB
76.3% or jevals.com 79.67% into one ranking — protocol / n / split
(`validation.md`, `notes.md` §49). Combinatorial grids are not
extractive keep/drop (ARC-AGI Direct Jev 4/400). FAQ: when-it-holds;
state-machine; retrieve-first.

## Calibration and cost-sensitive thresholds

A number you can threshold is a *decision* number only after you check
that it means P(event) on **your** population. In-distribution ECE can
look excellent and collapse OOD (Archer Hume — `notes.md` §7). Open
heads transfer this duty to you (`notes.md` §18). Encoder open-jev
reports in-domain ECE 0.022 and an OOD accuracy drop 0.854→0.690;
LoRA students report agreement with the teacher (`notes.md` §33). Hume
prefers the class name **decision models** over "system one"
(`notes.md` §33); this file still says System One when quoting TypeSafe.
Three open paths, not three species: encoder open-jev, AR constrained
decode (TypeAR + pcdServer; decision-token LoRA), trained decision-only (Laya / Nimble /
kev / **blackwood-rlcd** / Archer Watch). kev is the runnable Archer reconstruction on that
third path (text-only); blackwood-rlcd is that path with **image-in now** (CC BY-NC);
Watch stays Watch. A constrained softmax is still not a Noul (`notes.md` §42, §45, §46).

**Readout versus a token; IIA is a property.** A direct probability and a
generated "91%" are different objects; the format calibrates neither
(Hume reconstruction, `notes.md` §31 — not a TypeSafe contract). On his
reading of the official adapter, Choice `confidence` is arithmetic on the
distribution (how far the leader sits above uniform), not a second trained
correctness score. Choice probabilities are already conditional on the
offered set. His probes: an irrelevant extra option moved log-odds between
two existing options in every block, and reversing order moved a
probability across a ~0.9 threshold. Property-test both (`validation.md`).
Correctness is not that confidence field: report both, on held-out
cases (`validation.md`, Eval & hill-climb). Stimulus design, not a proof.
Atlas receipt of the same arithmetic: DAIR Emotion mean conf 0.819 at
48% acc (`notes.md` §49) — population calibration can fail
dangerous-high on overlapping labels. DMB S5: jev admits-ignorance
49.7% vs most constrained LLMs 97.3–100% (ECE 0.246). Do not skip
the honesty suite because in-distribution ECE looked fine.

For a calibrated binary p and unequal error costs, the Bayes threshold
is `t = C_FP / (C_FP + C_FN)` when you act vs not
([Elkan, *Foundations of Cost-Sensitive Learning*](https://cseweb.ucsd.edu/~elkan/rescale.pdf);
worked walkthrough:
[scikit-learn cost-sensitive threshold](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)).
Rebalancing the training set is not a substitute for computing the
decision from probabilities. Reject/abstain adds a second pair of
thresholds (Chow), still in policy.

**Per-action, not per-model.** The same Noul can clear "snooze the
email" and must not clear "submit the filing." Fail-open vs fail-closed
still follows the action (`judgment-class.md`): ranking error is
quality; selection/auth is control.

Life/business reading of the same math: write the two costs in dollars,
hours, or harm, *then* pick t. Do not copy 0.7 from a blog.
**Satisficing vs optimizing:** Choice for "good enough" menus; Score for
graded quality. Do not run MCTS theater when satisficing is the real
goal (leave-or-stay, send-or-edit, hire / more-interviews).

**Wording is part of the stimulus.** Semantically equivalent paraphrases
can swing p ("Is this the same person as X?" vs "Same person as X?" —
`notes.md` §25). That is Chow fuel: abstain or rewrite when
paraphrase-disagreement is large; set threshold width ≥ observed jitter.
Do not average ten wordings and call the mean Contract. Mapping:
`mappings.md` §17.

**Base-rate neglect:** force priors in code for rare incidents/fraud.
Soft models amplify vividness. **Conformal prediction** (distribution-free
sets around System One outputs) is the statistical sibling of "the
model checker didn't explore that; don't claim it" — say the
exchangeability assumption. Mapping sandwich: `mappings.md` §12.

## Value of information

[Value of information](https://en.wikipedia.org/wiki/Value_of_information)
(Raiffa-line decision analysis): the worth of another observation is
the expected improvement in the *decision*, not the expected improvement
in the *probability*. Gather-evidence is an act whose cost you know
(another test, another search, another human, another batch of Nouls).

```text
EVPI  = value of *perfect* information (clairvoyant) — an upper bound
EVSI  = value of *sample* information (the test you can actually buy)
both ≈  E[loss | current belief] − E[loss | belief after paying]
pay iff that difference > cost of the observation
```

Do not compute a numeric EVPI from uncalibrated scores and call it
Contract. The *placement* (gather as an enumerated act) is the method;
the calculator is **Hypothesis** until you log act/outcome pairs.
Mapping card: `mappings.md` §6. Paying *zero* because a regex already
answers is also VOI — abstain from calling any model
(`typesafe-jev-tools`, `notes.md` §42). A harness that *picks which
primitive to run* (JevML's claim: PCA / MCMC / diffusion / NCA) is the
same gate one layer down: maybe none of them (`notes.md` §44).
Hypothesis until that picker has a labeled log.

**Transfers:** "ask a second question" / "retrieve one more candidate" /
"run the expensive LLM" only when VOI clears the cost. Cheap fan-out
of independent Nouls is often +VOI because the second question is nearly
free (`composition-algebra.md`: width is cheap). **Does not:** infinite
clarifying questions; paying for a paragraph when a Noul would do;
treating another LLM call as free information.

| Domain | Observation you might buy | When not to |
|---|---|---|
| Knowledge work | Full PDF vs abstract | Abstract already rejects |
| Business | Customer call vs CRM fields | Fields already fail a hard rule (credit limit = exact) |
| Life | Blood test vs wait | Base rate + cost says wait |
| SWE | LLM autopsy vs OpenSmoke flag | Flag is negative — no VOI in the autopsy |
| Search | Deep rerank vs BM25 | Shortlist already size 1 |

## MCDA

[Multiple-criteria decision analysis](https://en.wikipedia.org/wiki/Multiple-criteria_decision_analysis):
name the criteria, score each, **weights live in policy**. Judge once;
re-weight without re-inference (`mappings.md` §1). Hard exclusions are
rules, not weights (a veto is not a −∞ slider you forgot to set).

Score has no natural units. `[0,1,0]` and `[0.5,0,0.5]` both score 1.0
with different tail risk — read the distribution.

| Domain | Criteria (each a Noul/Score) | Policy owns |
|---|---|---|
| Knowledge work | on-question, methods-ok, citation-quality | which paper to read tonight |
| Business | fit, urgency, expansion, risk | which RFP to bid |
| Life | commute, light, noise, price | which apartment — price is **exact** |
| Hiring | evidence-of-skill, miss-flag, culture-add | interview / reject; legal constraints stay exact |
| SWE | relevant, test-touching, unsafe | which hunks to stage |

**Counterexample:** one Score "how good is this candidate?" — that is
nine judgments pretending to be one, and it hides the vetoes.

## Search and control (where judgment substitutes)

Search: the *algorithm* stays yours (beam, A*, MCTS, a hiring funnel, a
literature snowball). The judgment-shaped hole is a prior, a prune, a
leaf value, or a "does this branch still look live?" Noul
(`methods-catalog.md` search rows; `mappings.md` §5). Economics
inversion: per-node judgments were known and too expensive; they are
now default. **A\***: a Score heuristic is *inadmissible* unless you
prove it — treat it as informal guidance, not an optimality certificate.

Control: hysteresis, continue / stop / retry / verify (foreman shape).
The model estimates named probabilities; the controller is a table with
memory. **Setpoint vs estimate:** Jev estimates the process variable;
policy owns the actuator. **Deadbands / dual thresholds:** separate
enter vs exit bars so alarms do not flap (ops *and* relationships).
Estimate ≠ measure — irreversible milestones concede only to a
probe.

| Domain | Search/control loop | Judgment hole | Exact / probe |
|---|---|---|---|
| SWE | MCTS over moves | prune / prior / value | simulator |
| Knowledge work | snowball citations | "is this still on-question?" | you already have the PDF |
| Business | sales stages | "is this still a real opp?" | amount, close date in CRM |
| Life | cook / rest / check | "does this look done?" | thermometer (probe) |
| Org | incident command | "is this still contained?" | head-count, location |
| Infra | Postgres query planner | override join/card when confident | the stock planner (fail-open) |
| Live media | ABR rung / resolution | "which ladder step?" | probe × headroom, thermal, battery |

Rejected: bandits without observed rewards; Jev as the planner that
picks its next tool in a loop (`boundary-audit.md`); PufferLib Ocean
scores as a capability claim (`formal-methods.md` DST trio). Mapping
card for the cross-domain loop: `mappings.md` §9. Soft judgment
inside a hard envelope: bitrate-advisor (ABR) and mmalisper's JOB
hybrid (Postgres plans first) — `notes.md` §44. Compaction envelope
(encoder, not Jev): gliner25-compaction — mutating tools / shell
operators prove `keep_full`; the model may only match that or be more
conservative (`notes.md` §50).

## Signal detection

[Detection theory](https://en.wikipedia.org/wiki/Detection_theory)
(Green & Swets): every yes/no judgment is a hit, miss, false alarm, or
correct rejection. **d′** is separability; the **criterion** is where
you place the bar given base rates and costs. Accuracy is the wrong
summary when classes are rare.

This is not the same as calibration (reliability of p) and not the same
as MCDA (many criteria). It *is* the same as content moderation,
radiology, hiring screens, "is this phishing?", "is this a real
deadline?"

```text
Noul ≈ evidence variable (noisy)
criterion t from costs and base rate   # policy
ROC curve  = hit rate vs false-alarm rate as t moves
PR curve   = precision vs recall — prefer this when the class is rare
you owe the plot on YOUR labeled cases
report the operating point you ship, not "accuracy"
```

Shift the criterion when the base rate shifts (flu season, incident
week, inbox after a launch). Do not retrain to "be more careful" when
you meant "raise t." Fail-open vs fail-closed is a criterion choice.
A listwise or CLIP affinity is not automatically this evidence
variable (`judgment-class.md`).

**Hypothesis** for non-SWE plots; **Empirical** for firehose/moderation
families in the archive (Near Here / jev-experiments) as a *shape*, not
as a number to copy. Mapping card: `mappings.md` §7.
**Alert fatigue:** Score severity, then rate-limit in code. Pure Noul
gates without a budget destroy recall. Leadership often moves the
*criterion* while blaming the model — name which one changed.

## Org and safety (Leveson)

Safety is a **control** problem, not a component-accuracy problem
([Leveson STAMP intro](https://psas.scripts.mit.edu/home/wp-content/uploads/2016/04/STAMP-Intro-2016.pdf)).
Hazards = missing enforcement of constraints. A 99% Noul is a sensor.
Unsafe control action: the person or agent proceeds *because the model
was confident*. STPA asks what happens when the sensor is wrong,
delayed, spoofed, or TOCTOU.

This is hospital, aviation, kitchen, boardroom, and agent harness alike:

- The constraint ("do not give the drug without the allergy list") lives
  in policy / code / physical interlock.
- The sensor ("does this note mention an allergy?") may be a Noul.
- Confidence does not waive the constraint.

Org placement: cheap judgment over every incident step (OpenSmoke
shape) so humans only autopsy flags. That is NATM instrumentation of
the control structure, not a safety case. Mapping card: `mappings.md`
§8. TOCTOU-of-Noul: `formal-methods.md` §5.

## Mechanism design and operations research

**Lite mechanism design:** Score as a reported belief; without
incentives, expect gaming. Allocation Choice assigns scarce resources
(GPU, reviewer time, seats) — strategy-proofness is not free. Separate
the *value estimate* (judgment) from the *payment/assignment rule*
(code). Don't let the estimator set both.

**OR:** soft affinity Score + hard feasibility (ILP/heuristic). Soft
costs cannot violate capacity or legality. Do not replace a VRP solver
with a Choice. Priority queues: Score urgency; FIFO/fairness in code;
starvation is a policy bug. Mapping: `mappings.md` §15.

## Epistemology and evidence

Score strength-of-evidence; Noul "is this an RCT?" — ontology errors
(Kent) dominate. Soft denial ≠ disproof. Citation Nouls check
*support*, not truth. An empty Choice shortlist is not "no good
option" (retrieval recall ≠ rerank). Amazon's split still applies
outside SWE: write "what must go right?" as positive invariants; soft
brainstorming of failures is incomplete by construction.

## Crossover metaphors (general design intuition)

Not substitutions until a precondition survives (`methods-catalog.md`).
Not SWE-only. Full FM-flavored reading stays on `formal-methods.md`;
this is the portable intuition.

**NATM / observational method.**
You do not prove the mountain. You excavate a round, instrument,
adapt support, stop if the readings demand it
([NATM](https://en.wikipedia.org/wiki/New_Austrian_tunnelling_method)).
Judgment = frequent, cheap, noisy instrument. Support and stop-criteria
= policy. A weekly LLM summary of "how the project feels" is the
rejected opposite (sampled, generated, not instrumented).

**Snap-fit.** Designed give on reversible joints; fasteners/welds on
pressure vessels. Snooze is a snap-fit. Wire transfer is a weld.
Hiring "maybe later" is a snap-fit; signed offer is not.

**Norman — gulfs of execution and evaluation.**
[Two UX gulfs](https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/).
Judgment shrinks evaluation over candidates you already hold ("is this
the right apartment listing / the right paper / the right hunk?").
Forcing functions (checklists, types, confirms, two-person rules)
shrink execution for irreversible acts. Knowledge in the world (the
diff, the CRM row, the labeled bins) beats knowledge in the head
(a paragraph you asked an LLM to "summarize how I should feel").

**Kent — naming is the ontology.** Choice sets and Score rubrics *are*
the model of the world. Wrong names → proof of the wrong world, in
business scorecards as in Alloy signatures.

**Shirky — situated.** Dense judgment inside a named group (30 people,
one product). Do not fake public scale. Mapping: `mappings.md` §16.

**Agans — debugging.** See → stabilize → find evidence → fix → verify.
Judgment classifies; probes verify. Incidents and personal stuckness
use the same sequence.

```text
NATM      instrument often; adapt the support you actually control
snap-fit  designed slop only where a miss is reversible
Norman    evaluate candidates; force the irreversible acts
Leveson   sense with judgment; constrain with policy
Kent      naming is the ontology
Shirky    dense loops only inside a named community
```

## Domain gallery (exposure, not a product catalog)

Use these as *existence proofs of a position*. Write your own card.
**Hypothesis** unless noted.

| Domain | Desired behavior | Judgment | Exact / generate |
|---|---|---|---|
| AI | agent that does not silently fail | step-level Nouls (**Empirical**: OpenSmoke) | sandbox; LLM autopsy on flags |
| SWE | stage the right hunks | include/exclude/mixed (**Empirical**: git-jev-stage) | `git diff` |
| Business | bid / no-bid | MCDA Nouls + risk Score | price, deadline, legal |
| Knowledge work | what to read next | on-question Noul + quality Score | library you hold |
| Hiring | interview / reject / hold | evidence Nouls; veto rules in policy | labor law, scorecards you wrote |
| Inbox | reply / snooze / archive | urgency Noul + aboutness Choice | send, calendar |
| Knowledge work | extract a quote / a cited fact | per-sentence or per-line-id Noul/Choice (**Empirical**: testimonial-miner, jev-reviewer) | verbatim join; place; human publish permission |
| Agent context | compact completed tool results without inventing prose | retention Choice + char-offset locate (**Empirical**: gliner25-compaction; same *job* as fast-jev-compaction / pi-jev-compaction) | mutation/shell envelope → keep_full; fail-closed keep_full; shadowMode before replace; copy exact bytes |
| Dataframe labeling | classify / score rows | Noul/Choice/Score + full `p__` (**Empirical** as jevframe / jevpandas *shape*) | pandas/Polars, thresholds in code |
| Computer-use speed | one verified act per step | operation + target Choice on numbered controls (**Empirical**: solari-reflex) | Guard check; deny-list absence; no screenshots |
| Agent turn | skip memory tour on easy intent | intent Choice (**Empirical**: jev-hermes) | Memory still writes; complex still searches |
| Document / lab routing | which pages need the expensive observation | Noul on remainder after a text layer / recipe | local extract, merge order (**Empirical** as OCR-router *shape*) |
| Shell / tool allowlist | unlisted remainder after a **proof** | five Nouls on unknown verbs | Proven/Refused in code; cannot block (**Empirical**: jevgate) |
| SWE | residual AGENTS.md / CLAUDE.md rules | one Score per named instruction-file rule | linter owns hard rules; bands + fail-open (**Empirical**: Abide replay, `notes.md` §47) |
| Screenshot candidates → act | lettered elements code already marked | Choice over those letters | Click in code (**Empirical** as blackwood-rlcd *shape*; CC BY-NC) |
| Browser / DOM candidates → act | numbered elements from a **text** snapshot | Choice / Nouls over those ids (**Empirical** as atlas browser-use *shape*: DOM-as-text + fan-out, not vision) | Click in code; no screenshots |
| Knowledge / recall | fact that is not in the document | **Do not ask.** Retrieve the passage first; then a self-contained Choice (**Empirical**: history suite A wrong@0.90 → C right@0.97) | Index, citation, the passage in `state` |
| Dual-process cascade | cheap classify / route vs write | S1 typed decision + τ; S2 generates only on low conf (**Empirical as a productized metaphor**; routing accuracy **unmeasured** — dual-process-ai) | Safety still fail-closed in code |
| CI merge-gate | ignore infra noise without merging a real bug | cause Choice per cluster (**Empirical**: latch demo PASS vs BLOCK) | Cluster + fingerprint + `--gate` table; reporter never fails the runner |
| Sleeping-agent resume | skip a worthless LLM turn | p(wake) (**Empirical** as safety table; 21/21 smoke — wakegate) | User-message / skip-limit / error always wake |
| Claim integrity at Stop | do not ship hallucinated-done | supports/contradicts vs session evidence (**Empirical**: clear-head) | Keyword retrieve; firm-confidence floor never blocks |
| Code-graph index | cheap S1 extract, S2 only on the tail | GLiNER locate + confidence escalate (**Hypothesis** as 10–50×; **Empirical** as degraded-load / no-invent-edges) | Graph in code; do not dump repo if S1 failed to load |
| Combinatorial puzzle | whole grid / program that must be consistent | **Rejected as extractive.** Cell-wise Choice assembly is not keep/drop (ARC-AGI Direct Jev 4/400) | Search, a program, a simulator |
| Moderation | hold before publish | hazard Nouls (**Empirical** as family) | block/review policy |
| Phishing / fraud screen | hold vs deliver | SDT criterion on a Noul | blocklist, SPF/DKIM exact (**Hypothesis**) |
| Personal ops | cook done / not | "looks done" Noul | thermometer probe |
| Org safety | stop the line | sensor Noul | interlock, two-person rule |

Rejected in every domain: replacing the ledger with a vibe; replacing
the interlock with confidence; replacing the essay with a Noul;
TOCTOU-of-Noul as authorize; tautological spec + "looks good."

Harm patterns that recur (curriculum §14): laundering estimate as
measurement; TOCTOU; Score unit fiction; independence fiction;
threshold cargo-cult; ontology capture (Choice set smuggles the
conclusion); Goodhart on the judge; coverage theater; scale mismatch
(Web metrics on situated problems); vacuous assurance.

## Decision-design extras (any domain)

```text
Domain (AI / SWE / business / knowledge work / life / org):
Desired behavior and non-judgment baseline (checklist, policy, habit):
Exact work (who/what owns arithmetic, law, money, side effects):
Semantic judgment(s) and pillar (EU / VOI / MCDA / SDT / search / safety):
Family (judgment-class.md) and fail policy:
Gather-evidence act and its cost (VOI):
Constraint that remains even if the sensor is wrong (Leveson):
Smallest labeled log that could reject this placement:
```

For open-ended requests propose three *placements* (not three vendors).
If the asker is not writing software, still name the exact work — a
spreadsheet, a checklist, a two-person rule. Do not invent an API.

Related: `mappings.md` §1–§18, `methods-catalog.md`, `toolbox-mapping.md`,
`composition-algebra.md`, `formal-methods.md`, `formal-semi-formal.md`,
`faq.md`.
