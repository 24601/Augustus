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
| Control-plane combinators | Then/Gate/Vote/Cascade/Weighted + Router/Loop/Retry/Fallback/Memory; digital-design metaphor ≠ literal AND/OR | `composition-algebra.md`; `notes.md` §66, §69 |
| Conflict ≠ ignorance | Noul collapses both; named Choice escape separates; binary Choice without escape is lexically biased | `question-design.md`; `notes.md` §69 |
| VOI cache / attention admit | Same-intent skip LLM; worth-your-attention before click; skip the narrating second call | jevcache / ThinkyMiner Winnow / hermes-jev-router; `notes.md` §69 |
| Eval integrity (receipts not leaderboard) | Hold/break map + budget-attached bake-off + OOD ECE with sign | atlas / frontier-100 / ood-calibration; `validation.md`; `notes.md` §66 |

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
component-node placement as lizard-agent / solari-reflex /
gliner2-ultrafast (GLiNER2 encoder backend of the same hole;
`notes.md` §52). Contrast blackwood-rlcd (screenshot + marked
letters). (`applied-mappings.md` §2; `mixed-architecture.md`).

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
**Programming primitive overlay (`notes.md` §99):**
[gut](https://github.com/Kungie/gut) (GitHub Apache-2.0 /
LICENSE MIT / pyproject Apache-2.0 *theirs*; **0★**; pre-alpha
target design *theirs*) makes that table a control-flow
outcome — YES / NO / UNSURE from `cost_false_yes` /
`cost_false_no` / `cost_human`. Thresholds derived from
costs not hard-coded. Worked example *theirs*: 2/52 ≈
0.038. Ties prefer UNSURE, then NO. Default
`on_unsure="raise"` so UNSURE does not silently become
`False` — **application policy**, not a System One hard
gate. Auto-batching same-object questions. Twin:
[Illusion47586/judge](https://github.com/Illusion47586/judge)
maps the belief onto **exactly one** application callback
including an explicit `uncertain` branch (judgment vs
generation; deterministic execution after probabilistic
judgment). Overlays, **not** new class-table species.
Kungie/gut ≠ tpellet/hunch ≠ carldaws/hunch.
Illusion47586/judge ≠ lexingtonhibiki/judgekit ≠
Ascurse/typed-judge-kit. Soft Noul ≠ hard safety: 0.038
/ `minimum: 0.85` are sensors. Hard-gating the derived
threshold as a proof is theater.
**Language primitive (`notes.md` §100):**
[southpolesteve/probably](https://github.com/southpolesteve/probably)
(TypeScript MIT; **3★**; HEAD `6bf671a4`; README SHA `c28570a9`)
— Jev IS the if-statement. judgments/probabilities drive
branches. text model only writes prose. interpreter owns
variables/loops/budgets/replay. otherwise maybe / confidence
gate. chaos samples after the gate.
southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠
Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably.
Language, not a library overlay. Soft Noul ≠ hard safety.
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
conservative (`notes.md` §50). Stdout-prune envelope (Jev):
jev-pruner — ≤10k / JSON-diff-whole-doc prove pass-through; Noul on
the remainder; fail-safe keep original (`notes.md` §53). OpenCode
host-port: [indiejoseph/opencode-jev-pruner](https://github.com/indiejoseph/opencode-jev-pruner)
— same envelope; `tool.execute.after` on `bash`; default
`jev-zen` / `jev-1.13-free`; zen-chat ≠ Noul; keepScore >0.1
floor; hook fail-open (`notes.md` §96).

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

**Capability kernel (Empirical as architecture, `notes.md` §59):**
[interlock](https://github.com/somoore/interlock) — the sensor is a
parallel Noul battery; the constraint is `policy.py` plus a closed
action space and canaries. Type-safe ≠ correct. Distinct from
asking "dangerous?" after the LLM already held the secret.

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
| Agent context | prune Bash stdout before the LLM without inventing prose | Noul per chunk after a hard size/format envelope (**Empirical**: jev-pruner; OpenCode host-port **indiejoseph/opencode-jev-pruner**, `notes.md` §96) | ≤10k / JSON-diff-whole-doc untouched; fail-safe original; archive dropped spans; hook fail-open; zen-chat ≠ Noul |
| Dataframe labeling | classify / score rows | Noul/Choice/Score + full `p__` (**Empirical** as jevframe / jevpandas *shape*) | pandas/Polars, thresholds in code |
| Computer-use speed | one verified act per step | score / Choice among numbered a11y/DOM/OCR+AX/ASR-transcript controls (**Empirical**: solari-reflex Jev; gliner2-ultrafast GLiNER2; laya-mind2web Laya DOM indices; cua-s1 option-attention, source-only, not TypeSafe Jev; Stagehand experimental Jev harness, draft; **closed-vote no planner:** JevOnly; **host-owned:** waymode; **hot-click ego-lite:** ego-jev; **OCR+AX desktop:** typesafe-computer-use hosted Jev, **427★**; **ASR voice-browser:** jev-voice-browser hosted Jev, **103★**) | Guard check; deny-list absence; no screenshots **on the decision**; no waveform to Jev; `DONE` ≠ success; plan ≠ execute; LLM fallback; pick ≠ replacement; type without generation; host handlers/permissions; `--until` beats Jev `done`; exclusive action set; spoken confirm ≠ auth |
| Agent turn | skip memory tour on easy intent | intent Choice (**Empirical**: jev-hermes) | Memory still writes; complex still searches |
| Document / lab routing | which pages need the expensive observation | Noul on remainder after a text layer / recipe | local extract, merge order (**Empirical** as OCR-router *shape*) |
| Shell / tool allowlist | unlisted remainder after a **proof** | five Nouls on unknown verbs | Proven/Refused in code; cannot block (**Empirical**: jevgate) |
| SWE | residual AGENTS.md / CLAUDE.md rules | one Score per named instruction-file rule | linter owns hard rules; bands + fail-open (**Empirical**: Abide replay, `notes.md` §47) |
| Screenshot candidates → act | lettered elements code already marked | Choice over those letters | Click in code (**Empirical** as blackwood-rlcd *shape*; CC BY-NC) |
| Browser / DOM candidates → act | numbered elements from a **text** snapshot | score among those ids (**Empirical**: atlas browser-use / jev-ultrafast / gliner2-ultrafast *shape*: DOM-as-text, not vision; cua-s1 specialist form, source-only; Stagehand a11y + editable-id side channel; **Empirical as README**: typesafe-computer-use OCR+AX macOS, **427★**) | Click / copy in code; no screenshots **on the decision**; hybrid remote TYPE optional; plan ≠ execute; schema/gate else LLM; overlapping options = doubt |
| Extract from a page | values already in element text | pick elements; copy bytes (**Empirical** as Stagehand #2955: 37/75 no-LLM ~0.5s vs 4.37s *their* card) | Schema plan; completion gate; screenshot → LLM; 36/75 LLM-off honesty |
| Knowledge / recall | fact that is not in the document | **Do not ask.** Retrieve the passage first; then a self-contained Choice (**Empirical**: history suite A wrong@0.90 → C right@0.97) | Index, citation, the passage in `state` |
| Dual-process cascade | cheap classify / route vs write | S1 typed decision + τ; S2 generates only on low conf (**Empirical as a productized metaphor**; routing accuracy **unmeasured** — dual-process-ai). **Harbor-shaped cousin:** decide→policy→LLM leftover on labelled emails (**Empirical**: jav-email-cascade; Noul 0.5 never rounded; mock gen-json flat-confidence is *their mock*) | Safety still fail-closed in code |
| Domain specialist vs few-shot | when policy reads p vs when only argmax | Train local LoRA on independent gold if downstream uses the distribution; hosted+examples if argmax (**Empirical**: Domain-jev-maker KL 0.168 vs 0.580; McNemar n.s. on few-shot determinate) | Threshold / EU in code |
| Semantic `ORDER BY` | put rows in a defensible order | Measure pairwise inversion / Score ordinality / ties; do not treat ECE as the sort certificate (**Empirical**: jev-orderby-bench six gates; Score 0.143 weak link; 53-way 0.99 tie) | Secondary key; measure request shape |
| CI merge-gate | ignore infra noise without merging a real bug | cause Choice per cluster (**Empirical**: latch demo PASS vs BLOCK) | Cluster + fingerprint + `--gate` table; reporter never fails the runner |
| Sleeping-agent resume | skip a worthless LLM turn | p(wake) (**Empirical** as safety table; 21/21 smoke — wakegate) | User-message / skip-limit / error always wake |
| Claim integrity at Stop | do not ship hallucinated-done | supports/contradicts vs session evidence (**Empirical**: clear-head) | Keyword retrieve; firm-confidence floor never blocks |
| Code-graph index | cheap S1 extract, S2 only on the tail | GLiNER locate + confidence escalate (**Hypothesis** as 10–50×; **Empirical** as degraded-load / no-invent-edges) | Graph in code; do not dump repo if S1 failed to load |
| Combinatorial puzzle | whole grid / program that must be consistent | **Rejected as extractive.** Cell-wise Choice assembly is not keep/drop (ARC-AGI Direct Jev 4/400) | Search, a program, a simulator |
| Moderation | hold before publish | hazard Nouls (**Empirical** as family) | block/review policy |
| Phishing / fraud screen | hold vs deliver | SDT criterion on a Noul | blocklist, SPF/DKIM exact (**Hypothesis**) |
| Personal ops | cook done / not | "looks done" Noul | thermometer probe |
| Org safety | stop the line | sensor Noul | interlock, two-person rule |
| Knowledge / RAG | reason only over kept evidence | retrieve wide → decide → evidence set (**Empirical** as architecture: decision-native-rag-skills; classify-first MCP cousin: jev-sift; **Hypothesis** as a measured win) | Conflict/temporal/provenance in code; embeddings / file lists generate candidates; errors/truncation ≠ irrelevant |
| Agent I/O | classify first, read selectively | batch path/url/text → relevance or typed questions (**Empirical** as README: jev-sift; topology A MCP) | Hard envelope (50 / 60k / 2MB / public-IP); main LLM opens survivors |
| Spreadsheet / catalog | named semantic columns | heading scores each row (**Empirical** as *shape*: jevpandas / jevframe; jevable intent columns). Snack MCDA clocks are **claims** | Weights, vetoes, exact fields in code |
| Robotics / control | observe → decide → act on a body | Choice on **geometry-as-text**, not pixels (**Empirical** as showcase: MuJoCo / MOSS; cousins jev-drone, Doom JSON; **Empirical as README delta**: khordoo/jev-reflex-autonomy-lab — S1 keeps flying, S2 one-use, no graphical input) | Kinematics / Hz / physics in code; two-call split; do not replace A*. Drawing-pixel claim ≠ Archer. S2 never grants. 20% still soft |
| Draft quality gate | kill drafts that break rules | quality Noul/Score (**Empirical** as fail *mode*: silence treated as safer) | Fail-open / heartbeat on missing verdict; contrast Abide `<0.5` (edit proceeds) |
| Session memory | next task sees last session's facts | scored recall over a verbatim ledger (**Empirical**: carryforward; 9×3 hint; **0/4** recall) | Constraints always-keep; fail-open dump; SessionStart > hoping |
| Application control flow | `if` / `case` on a judgment | `chance`/`pick`/`rate` as language primitives (**Empirical**: hunch; English-as-config). **Cost-derived overlay** (**Empirical as README target design**: Kungie/gut; YES / NO / UNSURE from costs; auto-batch). **Typed-callback overlay** (**Empirical as README**: Illusion47586/judge; exactly one app-owned callback; explicit uncertain branch) | Fail polarity per action; stub backend. Default UNSURE raises. Overlays, not species. Kungie/gut ≠ tpellet/hunch ≠ carldaws/hunch. Illusion47586/judge ≠ judgekit ≠ typed-judge-kit |
| Healthcare huddle / recon / inbox | escalate / hold / route | S1 remainder after NEWS2/code (**Empirical** as synthetic report: explore-typesafe-ai; **not clinically validated**) | NEWS2, recon, routing in code; S2 blinded review |
| Intent cascade vs nano/encoder | escalate when unsure | pre-registered kill/go (**Empirical as practice**: jev-baselines-eval **AMBIGUOUS**; cascade sign-flip; encoder-with-labels wins) | Thresholds, serving-path honesty, ECE if you claim calibration |
| Public primitive / wall | typed answers on a sentence | six parallel questions (**Empirical** as README: ask-jev-ai; cost-to-1M from tokens) | Policy-in-code; no-key allowlist; safety threshold in code |
| Codebase meaning-search | relevant file/chunk without knowing names | packed parallel relevance (**Empirical**: jevgrep 79% top-5 vs BM25 40% / grep 20% on stripped repos). **Line meaning-grep** AND/OR/NOT after threshold (**Empirical**: jev-semgrep 0.94/0.98 *theirs*; proposition ≠ embedding; contrast-set refund; Semgrep.dev collision; not a gate; `notes.md` §86). **Path-then-window pointer** (**Empirical as README**: JevFind; 0.25/0.55 still soft; overlapping windows not AST; `notes.md` §87). **Evidence packets** index-once (**Empirical**: jevex 1/8→6/8 n=8 *theirs*) | Keyword still wins exact strings; packet HitFile 0.233 is diagnostic; Japanese noisier near threshold; do not multiply parallel p |
| PR review attention | where a human should look | P0/P1/P2 (**Empirical** as README: egma-ai/jev-reviewer). **Not** correctness; **not** choxos pointer-not-generator | alwaysReviewPaths P0; incomplete never P2; generator writes deltas |
| Skill-derived lint | remainder after AST/precheck | Noul/Choice on guidance in state (**Empirical** as Phoenix: jev-oxlint) | Parser/precheck in code; not a hard gate; `tenbin` owns lint skill |
| Session model route | which model for this thread | first-prompt Choice, then lock (**Empirical** as README: jev-adaptive-thinking) | Fail-closed declared fallback; never reclassify later turns |
| RAG vs generative rerank | which passages to keep | pointwise relevance (**Empirical** as one-run: Jev-RAG ≥70%/72% vs Spark rerank; full-context Spark still faster) | Embeddings generate candidates; name the no-RAG arm |
| Untrusted agent / secrets | never hold the real key | hazard Nouls as **sensor** (**Empirical** as architecture: interlock) | Closed action space; canaries; `policy.py` BLOCK/ASK/ALLOW; type-safe ≠ correct |
| Live chess coaching | speak only when it matters | severity / interrupt / error-class (**Empirical** as Wave 0 PRD: game-coach) | Stockfish owns eval; templates + capped writing model own words |
| Kill a listening port | stop stale listeners without murdering the wrong PID | Stop/Keep/Review Choice (**Empirical**: port-cleanup) | Human confirm; identity re-check; shields override; mapped explanations |
| Calibration measurement | honesty of native probabilities | Brier/ECE/reliability on analytic worlds (**Empirical**: jev-arena live Brier 0.0059 / ECE 0.0620 *theirs*) | Oracle stub; fan-out batches; not verbalized confidence |
| Ranking vs calibration | does `ORDER BY` put rows right | Pairwise inversion / Score ordinality / two-decimal ties (**Empirical**: jev-orderby-bench) | Secondary key; do not quote ECE as sortable |
| Training-data VOI | which unlabeled rows are worth an expensive label | Confidence routes accept / teacher / human; log full distributions (**Empirical**: jev-triage) | Real outcome labels stay the targets; do **not** distill Jev as teacher (~68% ceiling) |
| Constrained-AR speed vs calibration | O(1) structured decode vs a Noul | Measure Brier/ECE, not only latency (**Empirical**: system-one-benchmark n=50; PCD Brier 0.3884 vs Jev 0.1096) | Schema-valid is not calibrated |
| Closed-vote CU | task with no planner LLM | Code builds options; model only picks (**Empirical**: JevOnly; waymode host-owned) | Type without generation; `completed` ≠ server-state success |
| OMP/pi gate | done-check / subagent topology | Choice, not boolean; fail-open missing Jev (**Empirical**: omp-jev-extensions) | Contrast pi-jev-approver fail-closed |
| Permission vs probability | auto-approve a gated tool call | Operator-owned criterion; plugin never self-tunes the bar (**Empirical**: omp-greenlight 40.9% / 0 of 94 *theirs*) | Not a sandbox; host deny stays above; live traffic unlabelled |
| Judgment ≠ permission | which specialised skills to inject | Jev scores relevance; code owns grants (**Hypothesis / outline**: skill-broker) | Never broaden access on Jev failure; not a production recipe |
| Eval integrity / instrument | is this eval's score trustworthy | Audit data/scorer/runs/claims; test a Jev question like an if (**Empirical**: dinostomp; ECE 0.062 *theirs* on 24) | 99 of 189 findings against itself; not a Harbor taskset |
| Constrained optimizer + S1 features | which backend meets quality + SLO at min cost | Judgment as a *feature*; solver owns floors (**Empirical as shape / negative**: slo-router p95 77.93→490.38 same routes *theirs*) | Never the sole hot-path gate; fail-open local features; eight-row demo is not a benchmark |
| Privilege ≠ verdict | is this shell command safe | Effect semantics + independent risk Nouls (**Empirical**: construct-auto-classifier; Jev 0 dangerous / 975; chat leaked) | Fast-allow/deny prove; landed-script trust; headless ≠ auto-approve; fail-closed |
| Attention filter / human-review VOI | do I need to look at what the agent did | Per-file Nouls; never blocks the agent (**Empirical as README**: rashedInt32/jev-lens; never green unless sure) | Not a permission gate; distinct from dizk/jev-lens pre-send views |
| Measurement owns endorsement | is this question pack shippable | Evidence-gated accuracy/ECE/cost/latency on a pinned version (**Empirical**: jev-packs nine verified *theirs*; **jevassert landed** record/replay CI) | No numbers → `provisional`; `unknown` mandatory; `check` offline |
| Jev supplies evidence, code owns authority | may this tool call run | Deterministic policy ALLOW/REVIEW/BLOCK; Jev is the sensor (**Empirical as slogan**: actiongate-jev) | Positive p never overrides a hard fail; fail-closed on irreversible classes if Jev is down |
| Ranking ≠ calibration | can I threshold raw p as a frequency | AUC vs ECE/Brier vs human rates (**Empirical**: 8,000 judgments; stated ~75% vs human ~10%; ~96% ECE removed) | Recalibrate on *your* labels (`jevcal` ~100 rows); vendor "calibrated" often means rank-correlation |
| Hot-click CU | next click / type from a viewport | Indexed element table → operation+target (**Empirical**: ego-jev; ~2× vs per-step LLM, n=3, not a bench) | Code owns observe/execute/`--until`; generator only for type; Jev `done` ≠ success |
| Compact without paraphrasing | drop irrelevant history, keep bytes | Keep/drop per message; pins + regex floor in code (**Empirical**: jev-compactor later **73%** / 350 ms / 4 of 4 vs shipped summarizers; §65 vs-Sonnet 64.5%/366ms) | Never rewrite; compaction fail-open if Jev down; safety fail-closed |
| Hold-before-show social | collapse junk replies | Local rules prove easy junk; remainder Nouls (**Empirical**: x-reply-filter) | Collapse not delete; never auto-train on the model's own hides |
| Never confidently wrong | protocol verdict under noisy evidence | TLA+ quorum + stability; Jev is the oracle (**Empirical**: jev-labs 1,080 golden 0 wrong *theirs*; escalate 5%→18% under severe) | Escalate is allowed; not a proof of zero; synthetic ≠ clinical |
| Advance / coverage | whether the world may change | Seal + coverage.path ledger (**Empirical as README**: seal; Jev answers questions, SEAL answers advance) | Exception queue visible; mint ≠ product brain; code seals first |
| Sureness of a distribution | act / escalate / abstain | max_prob/margin/entropy/gini (**Empirical**: how-sure-is-jev; Choice confidence = max_prob) | Bands are policy; pair with OOD; max_prob is generous |
| Cheap review triage | auto-approve / human-review / block | Four typed questions before expensive review (**Empirical**: ci-gatekeeper 504–629 ms *theirs*) | Operator owns thresholds; distinct from latch flaky-vs-real |
| Attention redirect (agent Stop) | one more look vs finish | Eight risk Nouls (**Empirical**: jev-preflight; fail-open; 0.85 uncalibrated) | Not a merge blocker; not rashedInt32/jev-lens |
| Pre-send perception | which lines enter the prompt | Code-built views; Jev picks (**Empirical**: dizk/jev-lens 79% fewer tokens / 500 trajectories) | Compress before first send; code full unless confident |
| tools≠use | will the agent call memory? | SessionStart injects; tools sitting there are not VOI (**Empirical**: carryforward 0/4) | Hook > hoping |
| Observational memory | what to keep, what kind | Keep/kind; verbatim ledger; model-free compact (**Empirical as README**: pi-om) | Failed Jev does not drain buffer; not a summary |
| Physical-world S1 | typed house questions | Sensors + automations (**Empirical**: HA-Jev 17★). **Portable cousin:** HA remains execution; Jev typed; one bounded LLM handoff (**Empirical as README**: ha-switchboard; **≠** HA-Jev; `notes.md` §87) | Not for locks/heaters/smoke; arithmetic in templates; allowlist / freshness / idempotency / post-state verify |
| Open-Jev class | finite choice + prob without TypeSafe | LM/vision/voice; JevPick; `/v1/systemone` wire (**Empirical**: openvons) | NOTA; execute/confirm/reject; not a replica |
| Judgment outside the store | semantic SQL over vanilla Postgres | CLI judges; DB sees ordinary SQL (**Empirical**: jevql) | Contrast pg-jev in-engine; cheap SQL first |
| Record/replay eval | can CI gate accuracy+calibration+cost | Record once; replay offline (**Empirical**: jevassert) | Live calls belong in `record`, not in PR CI |
| Failure-finding vs leaderboard | where does the judge fail | Reviewed atlas, not a winner crown (**Empirical as README**: chenmingtang830/jevarena; harness not findings) | Qualify vs meetr1912/jev-arena |
| Stereotype / uncertainty / cost | does missing evidence leak a stereotype | Typed Choice + unknown option; report bias **and** accuracy (**Empirical**: BBQ 97.28% / 0.04 / 0.34 / $0.3429 *theirs*) | Not a general bias cert; 12/13 amb errors stereotype-aligned |
| Decider ≠ executor | who picks the next act vs who writes args | Jev next-tool/progress/risk/done; LLM fills (**Empirical as README**: jeffrey) | Risk≥0.5 pause; stuck ladder; not a planner-writer |
| Decider ≠ executor across timescales | who flies vs who advises | S1 typed action every tick; S2 one-use strategy (**Empirical as README**: khordoo/jev-reflex-autonomy-lab) | S1 never stalls; S2 never grants; jeffrey is the SWE cousin |
| Escalate without stalling | pay S2 only under threshold, keep the loop | Async planner; reflex keeps steering (**Empirical as README**: khordoo; cousin classifier.dev smart *does* wait) | 20% starting gate *theirs* still soft; not Harbor τ |
| Mixed-initiative consumption | was the advice actually used? | Purple confidence = consumed; purple S2 bar = arrival; red = fail (**Contract as telemetry**: khordoo) | Arrival ≠ used. Green = local context |
| Local controller ≠ localjev | which reflex backend? | Rule-based built-in vs hosted `jev-latest` vs prompted-JSON Bun vs ONNX (**Contract**: khordoo Local/Live; **≠** githubnext/localjev **≠** kunchenguid/local-jev) | Same physics/seed; not a scored bake-off |
| Split kind/item/site | one 255-way soup vs three questions | Parallel Choices; used-only-for-matching-kind (**Empirical as README**: typesafe-computer-use) | Off-screen is a fourth question, not mixed into items |
| Exclusive CU actions | overlapping labels as false doubt | Confidence is concentration (**Contract as README**: typesafe-computer-use; wellposed cousin) | Missing `other` is the quiet 1.00 failure |
| Perception rebuild | what frontier reads from pixels for free | OCR crop/tile, AX walk, dates.py, clock, URL (**Empirical as README**: typesafe-computer-use) | AX never sole (Spotify 0). Decision ≠ answer-reader capture |
| ASR as perception | waveform vs transcript | Web Speech producer; Jev on text-state (**Empirical as README**: jev-voice-browser; compose with OCR §81) | Audio never enters the Choice. Skip Archer |
| Partial-speech VOI | act now vs wait for the rest | `complete` Noul + silence; closed-set may fire; free-text waits (**Empirical as README**: jev-voice-browser) | Truncating "search for alan" is the cheap failure |
| Spoken confirm ≠ auth | destructive click | Second Noul path; convenience not guarantee (**Contract as README**: jev-voice-browser) | Control-port reach is the real grant |
| Overlay disambiguate | which of 2–3 targets | Numbered badges; spoken digit; no second model (**Empirical as README**: jev-voice-browser) | The id is already in code |
| Wrap-as-execution | can the model skip the judge? | The wrap *is* the tool function (**Empirical as README**: AgentGhost; ASK throws; fail-closed) | Advisory sidecar is theater. rh-guard owns the gate cousin |
| Rules first then remainder | which verbs skip the model | allow-list proves; Jev on leftovers (**Empirical as README**: AgentGhost `allow` skips judge) | Contrast fail-open allowlist that cannot block |
| ASK throws | can HITL be silently skipped? | Default errors; wire `approveWith` (**Contract as README**: AgentGhost) | `AUTO_APPROVE` is a demo hatch, not a grant |
| Genre atlas ≠ bake-off | is this a rank? | Apps by hole; stars research-time (**Empirical as tweet**: [@studio_yebisu](https://x.com/studio_yebisu/status/2101065176069886152)) | ≠ class census §77 ≠ v1.2 board. Likes ephemeral |
| LLM hammer for bounded decisions | does this call need generation? | Typed answers when code already knows the options (**Empirical as article**: [@akshay_pachaar](https://x.com/akshay_pachaar/status/2101037514945597645)) | Mixed architecture, not stack replacement |
| Jev vs GPT-5.6 bakeoffs are a category error | is this the same class as a decoder-only chat model? | Encoder / ZS classifiers (BERTForXYZ → DeBERTa → ModernBERT) (**Empirical as tweet**: [@mervenoyann](https://x.com/mervenoyann/status/2101463303734067592)) | Jev is exemplar not the mandate. Do not invent accuracy numbers |
| Skill-issue classifier hole | could a ZS/fine-tuned encoder have done this? | many problems solved with LLMs could have been solved with them, it was a skill issue (**Empirical as tweet**: @mervenoyann) | Mixed architecture; replace-one-classifier-step |
| opt for DeBERTa and ModernBERT ones | which encoder family for ZS? | Hub pointers, not a how-to (**Empirical as tweet**: [follow-up](https://x.com/mervenoyann/status/2101592535835529527); hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72) | Do not cite bart-large-mnli likes as her pick. Do not copy `pipeline()` |
| multimodal image<>text ZS as perception front-end | pixels vs candidates? | ZS image classification is perceive; typed Choice/Noul is decide (**Empirical as HF docs**, Merve pointer) | Skip Archer. Soft scores ≠ hard gates |
| softmax/ZS scores still ≠ calibrated Noul | is 0.504 a frequency? | Hub widget `[0.504, 0.479, …]` *theirs* (`facebook/bart-large-mnli`) | quote *theirs*; do not invent accuracy numbers |
| schema-safe ≠ correct | can it still be wrong? | Cannot invent out of schema; can pick the wrong valid option (**Empirical as article**: Akshay; safer *theirs*: schema holds, judgment can fail) | Cousin of type-safe ≠ correct / jaggedness |
| Questions-as-code / shadow rollout | may this branch go live? | Rubric first; shadow beside current; plot accuracy vs confidence; pin questions (**Empirical as article**: Akshay) | Do not rebuild the agent first. 200×/400× are TypeSafe ceiling |
| Sentence-as-rule | does this named artifact contradict itself | Structural matcher × one sentence scored (**Empirical**: mizchi/jev-lint is jevlint rename; ~1 in 5 wrong *this README*; 13/15 older corpus *theirs*) | Mechanical defects stay with the compiler; qualify vs huntedman/JevLint |
| VOI admission (expensive review) | which hunks are worth a generative look | Typed per-hunk probabilities; safety keep-set in code (**Empirical as pilot**: prune-review 1.18% with 305% outlier *theirs*) | Cost ≠ quality; ~20% is a target not a result |
| Whole-repo intent | does unchanged code still violate the ask | VERIFIED/VIOLATION/UNKNOWN (**Empirical as CLI**: jev-intent-review) | Empty search ≠ proof; observation window ≠ the diff |
| Persist constraints | will "don't touch that" survive compaction | Structured policy + replay; Jev classifies meaning (**Empirical**: pi-heed 98.5%/0 false block *theirs*) | Jev never writes policy; fail-open |
| Open replica substrates | same contract, different engine | Isolation / byte-parity / agreement tests (**Empirical**: grande JGLUE; laya-jolt golden; local-jev 30%/57%; JEV-CPU PoC) | Softmax ≠ Noul; spec ≠ product; Meanblock 404; Archer Watch |
| Harbor SGR-judge contract | does evaluation need generation? | Frozen protocol vs schema-guided LLM judges; invalid = FN; cost/latency first-class (**Empirical as contract**: jev-judge-bench; **no quality headline yet**) | Canaries ≠ F1; incomplete cohort ≠ replacement claim; qualify vs jevarena/jevbench |
| Hand no-text steps | which loop steps need no writing | Plugin/control plane; writing stays generated (**Empirical**: jev-use 220 ms p50 / 12/12 gate *theirs*) | Vercel drops confidence → margin ≠ vendor head; fail-open gate never grants |
| Control plane, not a second agent | router / gate / retry / sieve / review / click | Named sensors; fail polarity per act (**Empirical as README**: pi-jev-control) | GUI never force-click; compaction never writes the session |
| Generation as a tree of Choices | next word without free generation | One typed question per choice over a closed lexicon (**Empirical as README**: jev-gpt ~400 calls / 75 s / 2¢ *theirs*) | Architecture demo; not a product writer; still pick ≠ fill |
| Recipe atlas (code prepares) | which narrow questions fit this job | Samples show technique; policy in code (**Empirical as recipes**: jev-cookbook; 16–36 not benches) | Thresholds are a dial; numbers/dates stay exact |
| Personal history without a social graph | what to show next from *your* trail | Rank outbound links; distribution *is* ranking (**Empirical as README**: jevfeed) | Generating the next look converges on a mirror; history never uploaded |
| Ranking ≠ calibration / injection ECE | is catch-rate a frequency? | AUPRC ranking and ECE move independently; 0.5–0.9 is the dangerous band (**Empirical as README 11,900**; Jev v2 AUPRC 0.980 ECE 0.058 vs Haiku ECE 0.021; Prompt wording moves panic 28%; `notes.md` §108) | Jev best ranking; Haiku better calibrated; rh-guard owns injection integrity |
| Temperature never changes argmax | can T fix a wrong pick? | 1-D search; accuracy identical; Laya `confidence` ≠ top-label p (**Empirical as Space + README**; Laya calibration lab Gradio MCP; easy probe set refused; 40–48 rows too small to ship T; `notes.md` §108) | ECE vs coverage independent; select_threshold returns inf |
| Question-asymmetry / abstention F1 | did the model refuse, or was it asked? | Jev is asked whether the question can be answered; published models saw the bare question (**Empirical as cached AbstentionBench**; rank 1 of 20 vs 2025 field; forward-looking 0.465 never extreme; `notes.md` §108) | Rank 1 is not current SOTA; forecasting is ignorance |
| Catalog ≠ endorsement | is listed a bake-off? | Continuously updated public index; auto-ingest marked pending (**Empirical as README index**; ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; `notes.md` §108) | Stars / listed counts are not eval |
| Mechanical tells in code | can Jev count em dashes? | Regex owns countable tells; Jev owns soft judgment (**Empirical as flopcheck**; 16 calibrated tweet judgments; hold-before-publish; `notes.md` §108) | Composite band is not a proof |
| Language OOD / p_max identity | does RU drop track ignorance? | Pre-registered n=600; XNLI Δ −11.0 pp; MASSIVE not detected at this n; confidence is function of p_max (r=1.000) (**Empirical as README 4,800 calls**; AHTOOOXA/jev-cyrillic-audit; `notes.md` §109) | MASSIVE “not detected at this n” not “equal” |
| Option-band resolution | is a finer menu better? | 7 bands 6/10 vs 40 bands 0/10; option label IS the pixel (**Empirical as README table-tennis**; LiuHao-1443/jev-table-tennis; `notes.md` §109) | Physics/collisions/scoring local |
| Proposed ≠ authorized | may a typed relation write? | Blocking O(nk) then Choice; gated 100% (95/95) coverage 59.375% (**Empirical as README FewRel 160**; chenmingtang830/jevgraph; `notes.md` §109) | Graph write is exact authorization |
| Code owns count | is 11% a person verdict? | git blame/ratio exact; Jev 10 questions/commit (**Empirical as README httpx 13/119**; AHTOOOXA/git-confess; `notes.md` §109) | squash-merge caveat |
| Paper PnL vs random | did the criteria make edge? | 90d trend +12.40% vs random +12.75% vs BH +41.71%; 5m win rate 25% (**Empirical as README paper trader**; waterme7on/jev-paper-trader; `notes.md` §109) | Default switched to trend so UI shows fills |
| Catalog jump ≠ eval | is 656/38160 a bake-off? | Awesomejev 656 entries / 38,160 stars (was 561/27007); tracker likes 64 (+4) lastModified UNCHANGED (**Empirical as live REST**; `notes.md` §109) | Laya present; Blackwood ABSENT; Archer still promised_not_landed |

| Ranking ≠ calibration | is 0.9 one number? | Same band over-confident on banking77, under-confident on sms-spam (**Empirical as README PRIMARY**; Running-Dolphins/jev-bench; “0.9 is not one number”; banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*; `notes.md` §110) | ≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench |
| Measured economics | is $0.0004 measured? | $0.0000153–$0.0000226 vs circulating $0.0004 (~20×); TCP floor 198.8 ms (**Empirical as README PRIMARY**; WallerChen/jev-measured; Score is 0..n-1 expectation not 0–1; Noul has no confidence field; `notes.md` §110) | type reliability is not a reason to choose Jev (json_schema 5/5) |
| Proper-scoring-rule RLCD | is ECE a hard gate? | Reward `r = c - p_a`; ECE 0.021; acc 0.807 vs warmup 0.746 (**Empirical as Hub card**; anthonym21/qwen3-0.6b-rlcd-decision; calibration beyond ~500 tokens unmeasured; `notes.md` §110) | In-distribution only |
| Independent primitive | must options be exclusive? | Independent `{cat: 0.9, dog: 0.5}` is valid (**Empirical as Hub demo**; larkooo/gemma-e2b-rlcd; Independent primitive; 11.57s vs 54.10s · 4.67× · 120/128 *theirs*; `notes.md` §110) | default path is pretrained Gemma probs not trained RLCD head |
| Teacher-copy vs gold vs zeroshot | who is the teacher of record? | Distilled = Haiku; gold = labels; zeroshot = base NLI (**Empirical as Hub trio**; shreyanbr/system-one-distilled/gold/zeroshot; priority 0.464 = majority floor; banking77 contaminated; `notes.md` §110) | do not distill Jev as teacher of record (they distilled Haiku) |
| Hybrid designed cases | did 8/8 convert users? | Function-only 5/8 vs hybrid 8/8; 4/8 without Jev (**Empirical as README**; RadRebelSam/jev-decision-lab; 8 designed cases not conversion lift; `notes.md` §110) | ≠ RadRebelSam/awesome-jev |
| VERIFY VOI | may I rescore the same pool? | VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring (**Empirical as README**; 202620325-spec/Jev-LLM; fast/full/max are ceilings not sizes; Solar writes, Jev chooses NEXT ACTION; `notes.md` §110) | Do not treat :max as a mandatory search size |
| 0.85-as-85% theater | is minProbability Harbor? | treating 0.85 as 85% / minProbability hard-gate as Harbor (**Empirical as README anti-pattern**; nozomi-koborinai/jev-spec; Spec vs artifact remainder; `notes.md` §110) | Hard-gating 0.85 as a CI proof is soundness theater |
| User decides | does selecting an option implement? | Jev judges / agent reasons / user decides (**Empirical as README**; grgy078033/grill-jev; selecting an option is not permission to implement; degraded fallback; `notes.md` §110) | User decision is the authorization |
| Dual-channel ECE / claim-audit | is this NAR "better calibrated"? | Like-for-like channels; n and CI before SOTA (**Hypothesis until independent run**; openJev-verdict-2.0; PR #1 now closed unmerged; 107★ densify; GH 151M vs README 149.6M; do not re-fold §71 claim-audit as a beat; `notes.md` §107) | Throughput ≠ latency; correctness-head ≠ distribution ECE; ≠ IamBusy/OpenJev |
| 1-token logprob ≠ Noul | can a generic LLM's next-token mass be the judge? | Constrained decode over caller-enumerated labels; coverage is format-mass (**Empirical as 336-case GUI**: chakuho 27B 95%/92% vs Jev 89%/82% *theirs*) | Softmax ≠ Noul; 8B coverage 1.00 while `__none__` collapses; arithmetic in code |
| Open replica runtime | same wire, faster forwards | Prefix reuse + family adapters; argmax-parity is the honesty check (**Empirical as README**: jevinf 2.57×/2.27× 100% argmax *theirs*) | MPS only; not ECE; not TypeSafe |
| Files-to-read VOI | which ranges change the next Read | Index-once, BM25, Jev packet (**Empirical as n=16**: jevex 160s→69s / $8.74→$3.13 / 16/16 *theirs*; keep n=8 finish 1/8→6/8) | Not a patcher; HitFile diagnostic; rename of jev-semantic-explorer |
| Commit attention ≠ verdict | is this commit worth a human look? | Typed Nouls + middle "review" band; regex proves literals (**Empirical as 13 labelled**: commitjev; 0 false on 5 clean *theirs*) | Small control; never round the middle; Nouls decide, Choice headlines |
| Decision-native queue | where should limited attention go next? | Atomic signals × deterministic policy (**Empirical as README**: mailordinal 100-point; humans own ambiguity) | Do not ask "how urgent"; arrival time is a poor proxy |
| Language OOD / confident-wrong | will p drop when the checkpoint cannot read? | Route by script **before** the forward pass (**Empirical as MASSIVE**: laya-multilingual; Khmer 0.000@0.952 *theirs*) | English checkpoint mean conf never < 0.885; gating cannot catch; ships uncalibrated |
| Schema-conditioned ranking | new labels without retraining | Scalar head per candidate; code softmaxes (**Empirical as Hub eval**: schema-scorer v2 Choice 0.841 *theirs*) | Peaked one-hot training ≠ calibration; GitHub 404 this pass |
| Branding ≠ backend | is this actually System One? | Read the client, not the badge (**Contract**: hermes-plugin-jev is Agnes chat-completions) | Distinct from hermes-jev-router |
| Productized System One HTTP | label + calibrated p as a public contract | Batch `{id,text}[]`; LLM fallback only (**Empirical as README**: classifier-dev **185★**; 400 headlines 650 ms *theirs*) | Distinct from ask-jev-ai wall; policy stays in code; not omni |
| Escalate-under-threshold | pay S2 only where p might change the act | Smart re-asks single-label <0.7; multi-label ignores (**Empirical**: classifier-dev ≥0.9→82% / <0.5→29%; gemini 87.5→90.0 / 61.8→63.7 *theirs*) | 0.7 is *theirs*; re-judge that made it worse is not VOI |
| Silent-fallback honesty | which model actually answered? | Named `FALLBACK` marker; alerts on a quiet chain (**Empirical**: granite F1 **0.546** vs advertised ~**0.800** *theirs*) | rh-guard owns the gate; dinostomp owns the instrument |
| Evidence-synthesis pointer | which line in the paper is the quote? | Jev picks ids; code copies verbatim (**Empirical as README**: choxos/jev-reviewer **12★**; 18-q **4.6 s / $0.0101** *theirs*) | **≠** egma-ai attention. *Not found* is an answer. Spot check ≠ validation |
| Two-pass relative + absolute | which line, and does that line itself answer? | Choice (+ none) then per-line Noul (**Empirical**: choxos; quotes Noul ≥ 0.5 *theirs*) | Multi-row tables need both; 0.5 is *theirs* |
| Human check as productized judgment | may this quote enter the review? | Tick/edit; checked never overwritten (**Empirical as README**: choxos) | Jev SENSOR; reviewer constraint. Not optional chrome |
| Wire-compat ≠ logit-equiv | does `/v1/systemone` mean the same p? | Prompted JSON + entropy-conf vs structured logit read (**Contract**: githubnext/localjev vs razorback16/openjev) | SDK drop-in is the wire. JSON-valid ≠ picked-right. **≠** kunchenguid/local-jev |
| Institutional open-replica | who ships the interchange? | GitHub Next local Bun bridge (**Empirical as product**: githubnext/localjev **261★**) | Legitimacy ≠ quality headline. Softmax / generated JSON ≠ Noul |
| Prompted-JSON bake-off | which local backbone on this *pipeline*? | Frozen AG News/BoolQ/SST-5; 1,200 req; caveats first (**Empirical as eval**: Qwen3.6 76.7% / Gemma 26B 75.0% / DiffusionGemma 74.2% short *theirs*) | No definitive winner (2/120). Not logits. Not calibrated. Not a Harbor taskset |
| Packaging ≠ new species | is this a new head or the same Laya? | GitHub/PyPI + Router over Hub ckpts (**Empirical as README**: NandhaKishorM/laya **710★**) | Weights stay convaiinnovations/*. **≠** TypeSafe drop-in. **≠** localjev |
| Token-budget cardinality | why does Jev win >20 options? | Options share `head_max_len`; ~3–4 tok/label at Banking77 (**Empirical as README**: 0.425 vs Jev 0.870 *theirs*) | Jev 255 options. Hierarchical Choice, not a silent cfg copy |
| Post-T ECE ≠ raw ECE | which ECE is on the badge? | Temperature per (type, K) on held-out (**Empirical**: 0.466→0.081 / 0.314→0.106 *theirs*) | vs-Jev 0.081 is post-T. Raw typed-decisions 0.213 vs Jev 0.144. Multilingual ships uncalibrated |
| Soft 0.85 gate | may I auto-act? | RLCD makes p *meaningful*, not Harbor-calibrated (**Contract**: README snippet) | Khmer 0.000@0.952. 0.85 is *theirs*. Route before p |
| External census ≠ scored bake-off | is this a rank? | Named list + a promised board (**Empirical as tweet**: [@airesearch12](https://x.com/airesearch12/status/2101259522933186879); watch [jev-models](https://benchmarkheaven.com/jev-models)) | ≠ jevbench v1.1 §67. Do not paste live ranks here. Likes ephemeral |
| Class-boundary (what belongs) | is GLiNER2 / a router an openjev? | Locate/categorize encoder + catalog routers counted beside NAR wires (**Contract as their list**) | Same job family ≠ replica. Needle 3 already not Jev-class §67. Qualify namesakes |
| Incomplete census vs watch | are missing names out of class? | Laya / localjev / kev / TypeAR / openvons / chakuho / jevinf / grande / laya-jolt / blackwood / classifier-dev absent | Lag, not a dunk. Completeness is a board watch item |
| Harbor honesty watch | what must a public openjev board disclose? | Calibration on/off the rank; cost/latency assumptions; silent fallback; partial runs (**Empirical as v1.2 board**: `notes.md` §78) | Soft-score-as-hard-rank is a design. Mixed class needs a class column |
| Geometric-mean product | can accuracy buy back a weak axis? | I/C/S/K 25% each; `exp(sum 0.25 ln max(axis,1))` (**Empirical as board**: Jev **75.3** / SemIf **74.6**; Luna I=96.8 rank #7 *theirs*) | Weights are a choice. Do not mix with v1.1 87.6. ≠ tweet census |
| Weight sensitivity | does the rank survive a different product? | Same axes, other views, still geo-mean (**Empirical**: no-cal SemIf #1; cost system-one-open #1 / Jev #5 *theirs*) | Official Score is 25:25:25:25. Other buttons are not the Score |
| Option-order brittleness | does A/B order change the act? | Reverse yes/no labels (**Empirical**: open-alternative-jev 72% → 21% *theirs*) | Cousin of paraphrase-brittleness. Ranked row uses author's order |
| Instruction models in a System One table | is the class the task or the architecture? | JSON-schema instruction models beside NAR rebuilds (**Contract as their legend**) | Luna/Gemini/DeepSeek/Qwen3.8. Needle 3 label-only. OpenJev = razorback16 ≠ IamBusy |

Rejected in every domain: replacing the ledger with a vibe; replacing
the interlock with confidence; replacing the essay with a Noul;
TOCTOU-of-Noul as authorize; tautological spec + "looks good."

Harm patterns that recur (curriculum §14): laundering estimate as
measurement; TOCTOU; Score unit fiction; independence fiction;
threshold cargo-cult; ontology capture (Choice set smuggles the
conclusion); Goodhart on the judge; coverage theater; scale mismatch
(Web metrics on situated problems); vacuous assurance.

## Apply this hour's class (already folded — do not re-card)

When the hourly named HIGHs are already on the branch, extract
**how to apply**, not a dump (`notes.md` §79):

1. **Wire-compat ≠ logit-equiv** — same `/v1/systemone` SDK can
   sit on prompted JSON (entropy-as-confidence) or on structured
   logit read. Calibrate before consequential use.
2. **Productize label + *p*; mark FALLBACK** — escalate-under-
   threshold is policy in code; a silent head-swap is a lie
   about the instrument.
3. **Packaging ≠ new species** — a Router is a face. Route by
   script before *p* when gating cannot catch OOD overconfidence.
   0.85 is still soft.
4. **Pointer-not-generator** — point at ids, copy verbatim,
   *Not found* is an answer, human tick never overwritten.
   Works at Cochrane/PRISMA scale, not only SWE.
5. **External list ≠ scored bake-off** — census VOI is
   completeness/class-boundary; a board VOI is the score
   function, cal on/off, and named cost/latency assumptions.

A Noul may attend or escalate. Hard-gating it as a PR/quality
seal is soundness theater unless an exact envelope already
proved the irreversible act.

## Apply 1047 (mental models, not SWE-only)

Typed judgment is portable EU / abstention / VOI / MCDA /
SDT / search / Leveson. This hour's how-to-apply:

1. **Decision-validated UI** — strings come from data or
   a catalog. Jev never authors. Formal methods own
   Telegram/A2UI envelopes. Valid tree ≠ good screen.
2. **Decision-as-assert** — meaning Noul vs exact
   `toContain`. Ambiguous band never rounded. 0.85 still
   soft; a matcher is not a product proof.
3. **Hybrid S1** — hard safety first (code shrinks the
   menu); S1 picks among remaining verbs; low conf → the
   rule. Perception as text-state / a11y. Logprob ≠ Noul.
4. **Pointer search** — path then window; copy snippets.
   Keyword still wins exact strings.
5. **Harbor three shapes** — vs frontier (economics +
   ECE); product bakeoff ≠ architecture duel; four
   engines + majority floor. Calibration ≠
   discrimination. Uniform can beat a miscalibrated model
   on JS.
6. **Named-escape authorship** — `uncertain` exists
   because conflict ≠ ignorance. Not courtroom evidence.
7. **Non-SWE product** — HA remains execution; n8n Low
   Confidence is abstention. Business/ops, not a coding
   agent.
8. **Verbatim compaction** — keep/drop, never summarize;
   fail-open to the host summarizer. Qualify the three
   Pi namesakes.
9. **Full distribution as a value function** — unused
   mass is signal. Bandits + CEM over operators in code;
   no LLM in the loop. Mock ≠ quality.
10. **Class honesty** — vision `score` untrained;
    Cerebellum wire ≠ TypeSafe; grounding can regress
    phishing. Platt, not temperature.

## Apply queued 1047 follow-ons (`notes.md` §88)

Same pillars, four more placements (plus jevsubrouter,
the remaining deferred 0945 HIGH). laya-vision and
Cerebellum stay §87 — do not re-card.

1. **Replica honesty** — wire `/v1/systemone` ≠ identical
   judgments. Acc can lose while ECE wins. Reused eval
   sets are Harbor honesty, not a holdout. **≠** the
   GLiFormer also named jeff.
2. **Empty ≠ approve** — a bounded workflow that found
   nothing has not proved the change. `notChecked` is
   the coverage ledger. Soft router thresholds are not
   a merge seal. Humans promote; agents draft.
3. **Beam as control** — the search algorithm stays
   yours; S1 only ranks observed FS candidates from an
   NL memory. Life/knowledge, not only SWE.
4. **Cache is the exact envelope** — never swap the
   conversation model to “save” a worker. Bind at
   dispatch; advise at the turn. Fail-open. Low conf
   does not silently downgrade. Do not quote dollars
   the instrument cannot see.

Soft Noul ≠ hard safety on every cluster.

## Apply 1144 (`notes.md` §89)

Same pillars, seven more placements. Do **not** re-fold
1047 / §87 / §88.

1. **Typed if** — `.feels()` is a typed method, not a
   new language. Keep p with `.how()`. Exhaustive
   `match`. Default 0.5 is Noul-0.5-never-rounded.
   **≠** hunch **≠** Probably.
2. **Shadow then honor** — policy + confidence gate +
   shadow, then a skill that honors the action. A
   pasted skill cannot force a bot that ignores it.
   “Mathematically fulfilled” without numbers is
   overclaim. **≠** AntonioCoppe/jev-harness.
3. **Human every action** — Jev SENSOR; LLM drafts;
   the person is the actuator. Never authority.
   0.75 is provisional.
4. **Atom then sense** — independently falsifiable
   claims; deterministic evidence outranks Jev;
   UNKNOWN useful; no sensor-output feedback.
   **≠** jev-sift.
5. **File by Choice** — classify then move.
   `OTHER` skip. 0.6 still soft. **≠** jev-semgrep.
6. **Question preflight** — Nothing about accuracy.
   Preregister bars before runs. “Jev wins” is not
   an assumption.
7. **Inbox read-only vs write** — `gmail.readonly`
   trays vs proposed archive/trash with review.
   **≠** mailordinal.

Soft Noul ≠ hard safety on every cluster.

## Apply 1241 (`notes.md` §90)

Same pillars, twelve more placements. Do **not** re-fold
1144 / §89. Fresh PR; never reopen merged #3.

1. **Observe→score→act (namesake lock)** —
   ZHUBoer/ego-jev reserved `__none__`. `selectedId` or
   null. No universal cutoff. runWorkflow completed ≠
   success. Exact work local. **≠** jiangkoumo/ego-jev.
2. **Decision-as-ranking** — jsort scores are relative.
   Noul not Choice for scale. Ranking ≠ frequency.
3. **Native vs schema-guided Harbor** —
   groundedness-judge-bench native vs schema-guided.
   Fastest/cheapest is not the quality winner.
   implicit_true included in yes.
4. **0 promotions / authored vs real** — jev_playground
   0 promotions. A suite that passes a random judge is
   plumbing. routing-backtest 0.0447%.
5. **Offload + classifier-not-generator** —
   yuyang2230/jev-agent-skill jev-1.13-free.
   jev-techstack-classifier stack_config.json only.
6. **Collapse late** — s1_ruby collapse late.
   `undecided?` abstain. Code asks; code decides.
   **≠** carldaws/hunch **≠** feelings.
7. **Unofficial toolbelt** — 2389-research/judgement
   license null. confidence ≠ winner p.
   typesafeai-sdk-community not a new species.
8. **Pointer shell** — tpellet/hunch exit 3.
   never-execute list. **≠** carldaws/hunch.
9. **Preview-first VOI / rubric rewrite** —
   jev-file-search scores not calibrated accuracy.
   jev-linkmap Jev never sees S2 prose.
10. **Life fail-open covers** — muhammedilyasy/jev-mail
    metadata only. tidy none-of-folders stay.
    tab-bouncer pinned/audio/current never closed.
    lkclean Show fail-open. jev-yt-time-saver Show
    anyway.
11. **S1 decide / S2 plan** — ORIGIN pause-if-no-Jev.
    validResponse sums-to-1. **≠** Essentiel-Jev.
12. **Seed/expand/judge/verify + local daemon ≠ Jev**
    — jev-crawlers risk bands never raw boolean.
    jevbrain AUTO_ACT is not a Noul.

## Apply 1347 (`notes.md` §91)

Same pillars, nine more placements. Do **not** re-fold
1241 / §90. Fresh PR; never reopen merged #3 / #7.

1. **Judge harness as control API** — judgekit YAML classify/score/route/verify.
   typed-judge-kit verdict-in-code. Thresholds from labels, not
   self-confidence. **≠** JudgeBench **≠** DeepEval.
2. **Batch packing VOI** — alsoleg89/decide packing VOI.
   0.8 ≠ 80% accuracy. **≠** jev-sift.
3. **Calibration as product** — Jev-Calibration Platt ECE 0.117→0.052.
   jev-calibration-arena never acts.
   **≠** jev-arena **≠** jevarena.
4. **Decision-as-Plugin** — ctmx/openrouter-jev-mcp Decision-as-Plugin.
   FrancoisChastel/jev-code ≠ npm jev-code.
   claudecode-jev-marketplace fail-open not hot path.
   pedroknigge/mcp_jev packs not ask_jev.
   cyrusasco/typesafe-mcp noul deadband 0.35–0.65.
   codaaiteam/jev-skill jevtypesafeai.com ≠ TypeSafe.
5. **Policy-constrained skill select** —
   hermes-switchyard ≠ hermes-jev-router ≠ hermes-plugin-jev.
   Advisory; never loads skills.
6. **Tiny local econ pruner** — nanoprune 2.8MB ECE 2.58%.
   “0 hallucination guaranteed” is theater.
7. **Observe→score→act cousins** —
   smartdio/jev-browser-agent ≠ ZHUBoer/ego-jev.
   Dakai/omp-jev-web DONE ≠ proof.
   hari007sh/jev ≠ dannote/jev.
8. **Deterministic verify ≠ System One** —
   0thernet/system-one-skills deterministic verify.
9. **Soft-score vs hard-argmax** — typed-gate band [0.40,0.60] is refusal.
   pi-jev-gate fail-closed; choice is the verdict. rh-guard owns the gate
   cousin.

Soft Noul ≠ hard safety on every cluster.

## Apply 1441 (`notes.md` §92)

Same pillars, nine more placements. Do **not** re-fold
1347 / §91. Fresh PR; never reopen merged #3–#8.
rh-guard owns the gate cousins; Augustus owns
placement. Skip Archer.

1. **Self-hosted econ** — Foq ~25ms/2.2GB local.
   rev prefill-only + HF jev-0.5b.
   robfrase/jev planning memo.
   Sample `latency_ms` 32.4 is not a bench.
2. **Soft-judgment gate integrity** —
   typesafe_agent_gates 27/27 / 31/31.
   EpicEric/safe-sh static remainder.
   pastepilot Confirm before act.
3. **Retrieval as calibrated decision space** —
   Jev-Reranker live Jev not yet measured.
   sessionwise opt-in relevance.
   jev-search pointer sieve.
4. **Enterprise reflexes** — 400ms Salesforce WebMCP.
   typesafe-scheduler-diagnostics advisory.
5. **Screenshot-free / CU** — droidjev screenshot-free.
   Tewoto1 jevcu planner still writes.
6. **Hybrid S1/S2** — ha-conversation-jev Jev→Grok.
   dsh-jev can only gate.
7. **Harbor-jevals / SRE** —
   jev-classification-benchmark specified not run.
   jev-luna-pagerduty p≥0.50.
8. **Laya densifies** — meldltd/meldecision laya-go ONNX.
   laya-doom never pixels.
   logixism/laya-api empty README.
   akpsahan/laya ≠ Archer.
9. **Demos / unofficial toolbelt** —
   choxos/jevchess engine owns truth.
   jev-drive sim not AV.
   story-arc Jev never authors.
   jev-hs-assistant HS6.
   golergka/jev-plays-starcraft-2 UI-verified ≠ API Victory.
   awesome-jev-use-cases catalog.
   Nibir1/typesafe-go ≠ official.

Soft Noul ≠ hard safety on every cluster.
soft Noul ≠ hard safety.

## Apply SIGNAL jevcache/jev-align (`notes.md` §93)

Same pillars, two placements. Do **not** re-fold
1441 / §92. Fresh PR; never reopen merged #3–#9.
rh-guard owns HIT-as-truth and training-score
auto-accept as gate cousins; Augustus owns
placement. Skip Archer.

Unique fragments (consecutive): fingerprint after redact; recall vs decide; publish fingerprints+answers; CI replay as Harbor cousin; Cache hit ≠ correctness; hyperspaceai/jevcache ≠ kushals256/jevcache; human labels only; score never auto-accepts; production capture flywheel; sutro-sh/jev-align ≠ caiovicentino/jev-align

1. **Decision ledger / memoization** —
   fingerprint after redact.
   recall vs decide.
   publish fingerprints+answers.
   CI replay as Harbor cousin.
   Cache hit ≠ correctness.
   hyperspaceai/jevcache ≠ kushals256/jevcache.
   memoize typed decisions; VOI of cache hit.
2. **GEPA alignment loop** —
   human labels only.
   score never auto-accepts.
   production capture flywheel.
   sutro-sh/jev-align ≠ caiovicentino/jev-align.
   GEPA + System One.

Soft Noul ≠ hard safety on every cluster.
A HIT is a sensor, not a proof. A training score
is a sensor, not an accept.

## Apply SIGNAL enzyme / JA ModernBERT / Gemma (`notes.md` §94)

Same pillars, three placements. Do **not** re-fold
jevcache/jev-align / §93. Fresh PR; never reopen
merged #3–#10. rh-guard owns guidance-as-hook,
unofficial-local-as-Jev, hosted-bootstrap silent
FALLBACK, LFM-default-as-JA-softmax, Nemotron “not
calibrated replacement”, and Laya
confidence-without-competence as gate cousins;
Augustus owns placement. Skip
Archer.

Unique fragments (consecutive): guidance ≠ hook; catalysts ≠ summaries; compile-time System One; unofficial ≠ TypeSafe; format_version modernbert-jev/1; Argos1111/jev_local ≠ us/jev-local ≠ kunchenguid/local-jev; LFM default ≠ ModernBERT backend; Nemotron ≠ TypeSafe Jev; not a calibrated replacement; djev-dev complements djev-spark; images as Choice options; Laya essay numbers *theirs*; Router/OOD confidence; hosted bootstrap ≠ silent TypeSafe

1. **Compile-time System One / questions-as-index** —
   guidance ≠ hook.
   catalysts ≠ summaries.
   compile-time System One.
   Soft guidance ≠ hard gate. Life/PKM atlas.
2. **Unofficial JA ModernBERT cross-encoder** —
   unofficial ≠ TypeSafe.
   format_version modernbert-jev/1.
   Argos1111/jev_local ≠ us/jev-local ≠ kunchenguid/local-jev.
   Pair scoring → softmax. LFM default ≠ ModernBERT backend.
   The Hub card is text-only; jev_local default is LFM
   (including vision).
3. **NAR class legitimacy / multimodal / Router-OOD** —
   Nemotron ≠ TypeSafe Jev.
   not a calibrated replacement.
   djev-dev complements djev-spark.
   images as Choice options.
   Laya essay numbers *theirs*.
   Router/OOD confidence.

Soft Noul ≠ hard safety on every cluster.
`when asked` is a sensor, not a deny. Unofficial
local p is a sensor, not TypeSafe calibration.
Nemotron p and Laya 0.85 remain sensors.
hosted bootstrap ≠ silent TypeSafe. LFM default ≠
ModernBERT backend.

Formal methods **compose** with scoring. A Noul is a
SENSOR. Hard-gating it as CI pass / HA write / authorship
seal is the same theater as jev-gate §79.

## Apply 1541 (`notes.md` §95)

Same pillars, six more placements. Do **not** re-fold
1441 / §92. Fresh PR; never reopen merged #7–#12. Do **not**
re-fold §93 / §94. rh-guard owns the injection-firewall
/ CI-gate cousins; Augustus owns placement. Skip Archer.
Census not re-derived.

Unique consecutive fragments:
difficulty + policy thresholds + JSONL trace;
jev-codex-pilot model + reasoning depth;
keep/shadow/hybrid/reject;
quarry evidence projection;
Frank-ZY-Dou/awesome-jev robotics/3D/control;
one-dollar-tahoe TypeSafe Jev defense eval;
jevguard calibrator/cache/escape;
jev-ci-selector CI shadow mode;
llama-jev llama.cpp replica.
petercr/jev-orchestrator ≠ FleeexCorp/jev-orchestrator.
seb4ez/jevguard ≠ AseemPrasad/JevGuard ≠ pablozr/JevGuard.
webNeat/llama-jev ≠ WiktorB2004/llama-index-jev.

1. **Decision-as-plugin for SWE** —
   difficulty + policy thresholds + JSONL trace.
   jev-codex-pilot model + reasoning depth.
   keep/shadow/hybrid/reject.
2. **Evidence projection vs LLM summary** —
   quarry evidence projection.
3. **Soft judgment integrity** —
   jevguard calibrator/cache/escape.
   jev-ci-selector CI shadow mode.
4. **Physical/control first-class domain** —
   Frank-ZY-Dou/awesome-jev robotics/3D/control.
5. **Harbor-jevals / injection-firewall** —
   one-dollar-tahoe TypeSafe Jev defense eval.
6. **llama.cpp replica** —
   llama-jev llama.cpp replica.

Soft Noul ≠ hard safety on every cluster.
0.95 FINISH / 0.05 skip_below / 0.40 calibrator
are **sensors**. Keep is a win. Pointer, never
paraphrase. Text-state, not pixels. Static 74-row
demo is not a rate. Softmax ≠ Noul.

Formal methods **compose** with scoring. A Noul is a
SENSOR. Hard-gating it as CI skip / injection firewall
/ physical actuator is the same theater as jev-gate §79.

## Apply 1639 (`notes.md` §96)

Same pillars, one HIGH host-port plus MEDIUM
watch. Do **not** re-fold 1541 / §95. Fresh PR;
never reopen merged #7–#13. Skip Archer. Census
not re-derived.

Unique consecutive fragments:
OpenCode jev-pruner context sieve;
observe→score-candidates→prune;
jev-zen / jev-1.13-free;
zen-chat ≠ Noul;
fail-open original;
keepScore >0.1 floor;
host port of tamaratran/jev-pruner;
indiejoseph/opencode-jev-pruner ≠ nrdz-labs/fast-jev-opencode;
jev-webagent-bench empty stub;
Kiln-AI/jev_jsonschema noul_threshold 0.5;
NSStudent/JevSwiftSDK unofficial.

1. **OpenCode host-port of evidence-preserving
   stdout prune** —
   OpenCode jev-pruner context sieve.
   observe→score-candidates→prune.
   jev-zen / jev-1.13-free.
   zen-chat ≠ Noul.
   fail-open original.
   keepScore >0.1 floor.
   host port of tamaratran/jev-pruner.
2. **MEDIUM watch / tooling** —
   jev-webagent-bench empty stub.
   Kiln-AI/jev_jsonschema noul_threshold 0.5.
   NSStudent/JevSwiftSDK unofficial.

Soft Noul ≠ hard safety. Hook fail-open; reduction
fail-closed to original. zen-chat parsed JSON is
not a Noul. 0.5 boolean decode is a sensor.
Empty stub ≠ Harbor.

Formal methods **compose** with scoring. A Noul is a
SENSOR. Hard-gating prune as proof of irrelevance,
or treating zen-chat as calibrated Jev, is the same
theater as jev-gate §79.

## Apply SIGNAL gliner-native-runtime (`notes.md` §97)

Same pillars, one HIGH on-device locate runtime.
Do **not** re-fold 1639 / §96. Fresh PR; never
reopen merged #7–#14. Skip Archer. Census not
re-derived.

Unique consecutive fragments:
GLiNER2 native Apple path;
unofficial Swift/Core ML GLiNER 2.5-small;
entity spans + confidence;
not Choice/Score/Noul;
not TypeSafe;
label descriptions as schema;
on-device ANE economics;
honesty locks;
shershah1024/gliner-native-runtime ≠ Fastino;
≠ gliner25-compaction ≠ gliner2-ultrafast ≠ Eran-BA/Jev_from_GLiNER2 ≠ NSStudent/JevSwiftSDK ≠ jevmlx;
default threshold 0.1 still soft.

1. **GLiNER2 native Apple path** —
   unofficial Swift/Core ML GLiNER 2.5-small.
   entity spans + confidence.
   not Choice/Score/Noul.
   not TypeSafe.
   label descriptions as schema.
   on-device ANE economics.
   honesty locks.
   Locate species; Fastino owns the checkpoint.
   Code owns policy. Position 10 discretizer/encoder
   (schema+text → labeled spans), **not** position 4
   Selector of F, **not** keep/drop of held candidates.
   Soft Noul ≠ hard safety:
   0.1 / null >0.5 / README 0.99 are sensors.

Soft Noul ≠ hard safety. Spans + confidence are
not a Noul. Hard-gating 0.1 as NER quality, or
treating this as TypeSafe `/v1/systemone`, is the
same theater as jev-gate §79.

Formal methods **compose** with scoring. A span
confidence is a SENSOR. Hard-gating it as a safety
proof is theater.

## Apply 1740 (`notes.md` §98)

Same pillars, three HIGH clusters (protocol envelope,
calibrated meaning-grep, Archer-arch family gap).
Do **not** re-fold 1639 / §96 / gliner-native-runtime
/ §97 / 1541 / §95. Fresh PR; never reopen merged
#7–**#15**. Skip Archer rewrite (still **NOT
landed**; likes 51; lastModified UNCHANGED). Census
not re-derived. Do not rewrite §45.

Unique consecutive fragments:
Decision Graph Protocol frame→assess→commit;
app retains permissions/effects;
Jev-first assessor-neutral;
guarded commit / receipt/next frame;
assessment batching;
hard-gating DGP as safety theater;
numerous-com/dgp ≠ TypeSafe official;
jegrep calibrated path+range Nouls;
no embeddings/index/daemon;
~$0.01–0.03 typical;
agent --json;
can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep;
Archer-arch fidelity;
kev family OOD 0.76–0.77 vs Jev 0.86;
block-causal isolation;
pointer/readout CE-trained;
/v1/systemone drop-in;
replica honesty.

1. **Decision Graph Protocol** —
   Decision Graph Protocol frame→assess→commit.
   app retains permissions/effects.
   Jev-first assessor-neutral.
   guarded commit / receipt/next frame.
   assessment batching.
   Protocol envelope around a judgment-class
   assessor. Pillar: Leveson sensor≠constraint +
   runtime-assurance sandwich + EU (assessment is
   belief; commit is the act). Commit fail-closed
   in the application; assessment is a sensor.
   hard-gating DGP as safety theater.
   numerous-com/dgp ≠ TypeSafe official.
2. **Calibrated meaning-grep (Rust, live tree)** —
   jegrep calibrated path+range Nouls.
   no embeddings/index/daemon.
   ~$0.01–0.03 typical.
   agent --json.
   SDT / cascade IR. Ranking fail-open.
   OpenRouter/TypeSafe auto-failover is silent
   FALLBACK, not the same Noul. Auto-τ-lowering
   is not a 0.4 proof.
   can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep.
3. **Archer-arch fidelity + measured calibration
   gap** (secondary) —
   Archer-arch fidelity.
   block-causal isolation.
   pointer/readout CE-trained.
   /v1/systemone drop-in.
   kev family OOD 0.76–0.77 vs Jev 0.86.
   replica honesty.
   Runnable family ≠ Jev identity. A wire drop-in
   is not a Noul. Score confidence is a stand-in
   (*theirs*). Do not rewrite §45.

Soft Noul ≠ hard safety. Assessment p / mock
outcomes / 106 tests / 0.4/0.2 / $0.01–0.03 /
0.76 / 0.77 / 0.86 / ECE ~0.1 / 0.62 rule-pairs
are **sensors**. A receipt proves the commit
happened under the guards, not that the assessor
was correct. Hard-gating a miss as “the concept
is absent,” treating OpenRouter/TypeSafe
auto-failover as one Noul (silent FALLBACK),
or pasting OOD acc as “close enough to ship as
Jev,” is the same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul
is a SENSOR. Hard-gating DGP as safety theater
is theater.

## Apply 1843 (`notes.md` §99)

Same pillars, five HIGH clusters (cost-derived
control flow, typed-callback twin, variable-N
training object, open NAR replica economics,
typed vs chat judges). Do **not** re-fold 1740
/ §98 / 1639 / §96 / gliner-native-runtime /
§97 / 1541 / §95. Fresh PR; never reopen merged
#7–**#16**. Skip Archer rewrite (still **NOT
landed**; likes 51 **flat**; lastModified
UNCHANGED). Quote live REST over watch claims.
`invented_signal: false`. gut/judge are
**overlays**, not new class-table species.
jev-forge is a class-architecture note, not a
sixth species. llm-vs-jev is a **cross-note**;
deeper integrity fold is rh-guard.

Unique consecutive fragments:
cost-sensitive decision theory × System One probabilities → control flow;
thresholds derived from costs not hard-coded;
YES / NO / UNSURE from cost_false_yes / cost_false_no / cost_human;
auto-batching same-object questions;
Kungie/gut ≠ tpellet/hunch ≠ carldaws/hunch;
judgment vs generation;
deterministic execution after probabilistic judgment;
exactly one app-owned callback;
explicit uncertain branch;
Illusion47586/judge ≠ lexingtonhibiki/judgekit ≠ Ascurse/typed-judge-kit;
variable-N option scoring as the trainable object;
dynamic candidate bags not fixed label sets;
zwliJay/jev-forge ≠ NanoJev;
open replica economics / latency vs closed Jev;
NAR local drop-in;
wfzyx/von late-catch HIGH;
competing NAR claims / replica honesty;
typed judgments vs chat judges on guardrailing;
ishaannk/llm-vs-jev cross-note only;
deeper integrity fold is rh-guard;
nothing wins outright;
can be argued out of guarding.

1. **Cost-derived YES/NO/UNSURE control flow**
   (PRIMARY) —
   cost-sensitive decision theory × System One
   probabilities → control flow.
   thresholds derived from costs not hard-coded.
   YES / NO / UNSURE from cost_false_yes /
   cost_false_no / cost_human.
   auto-batching same-object questions.
   EU / Chow / Elkan as a programming primitive.
   Kungie/gut ≠ tpellet/hunch ≠ carldaws/hunch.
2. **Typed-callback twin** —
   judgment vs generation.
   deterministic execution after probabilistic
   judgment.
   exactly one app-owned callback.
   explicit uncertain branch.
   Illusion47586/judge ≠ lexingtonhibiki/judgekit
   ≠ Ascurse/typed-judge-kit.
3. **Variable-N option scoring as the trainable
   object** (not a new species) —
   dynamic candidate bags not fixed label sets.
   zwliJay/jev-forge ≠ NanoJev.
4. **Open NAR replica economics** (late-catch) —
   NAR local drop-in.
   open replica economics / latency vs closed Jev.
   wfzyx/von late-catch HIGH.
   competing NAR claims / replica honesty.
   Do not merge Needle 52.6% with n=78 93%.
5. **Typed vs chat judges on guardrailing**
   (cross-note) —
   typed judgments vs chat judges on guardrailing.
   ishaannk/llm-vs-jev cross-note only.
   deeper integrity fold is rh-guard.
   nothing wins outright.
   can be argued out of guarding.

Soft Noul ≠ hard safety. 0.038 / 0.85 /
0.579 / 0.637 / 93.0% / 62 ms / 15 ms /
77.9% / ECE 0.053 / 14.3% steer are
**sensors**. Hard-gating a derived threshold
as a proof, pasting von as a Jev replica,
or pasting "Jev wins guardrailing" is the
same theater as jev-gate §79.

Formal methods **compose** with scoring. A
Noul is a SENSOR. The cost table / callback
map / commit guard is policy.


## Apply 1943 (`notes.md` §100)

Same pillars, six HIGH clusters (Jev IS the if-statement
PRIMARY; GEPA live-star delta; memory retrieve vs lease;
contract-of-artifact lint rename; JSON Schema question
compiler; local System One economics). Do **not** re-fold
1843 / §99 / 1740 / §98 / 1639 / §96 /
gliner-native-runtime / §97 / 1541 / §95 / jev-align
*mechanism* / §93. Fresh PR; never reopen merged
#7–**#17**. Skip Archer rewrite (still **NOT landed**;
likes 51 **flat**; lastModified UNCHANGED). Quote live
REST over watch claims. `invented_signal: false`.
probably is a **language**, not a library overlay.
jev-align is a live-star / framing delta of §93, not a
new mechanism. jev-lint **is** jevlint (GitHub rename).
invalidate / jev_jsonschema are HIGH upgrades.
0★ HIGH still gets a real card.

Unique consecutive fragments:
Jev IS the if-statement;
judgments/probabilities drive branches;
text model only writes prose;
interpreter owns variables/loops/budgets/replay;
otherwise maybe / confidence gate;
chaos samples after the gate;
southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠ Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably;
133★ / forks 10 live;
build calibrated classifiers from human feedback;
retrieve by relevance not resemblance;
one calibrated yes/no per memory in one request;
pointer mode 17/18 19/20 *theirs*;
embedding resemblance misses the allergy;
samdotmak/jev-recall ≠ jev-search ≠ jev-sift ≠ carryforward ≠ chopratejas/invalidate;
memory leases ended by new evidence;
six Nouls then fixed rules in code;
0 of 157 false invalidations;
questions/plans/directives are not evidence;
unsure → review queue;
host keeps the store;
name↔body / comment truth / test-claims;
mizchi/jev-lint is mizchi/jevlint rename;
no shipped rule has severity error;
~1 in 5 findings wrong *theirs*;
mizchi/jev-lint ≠ huntedman/JevLint ≠ MichitoSugawara/jev-lint;
JSON Schema → typed JSON via Jev;
noul_threshold 0.5 decoder not a proof;
IncompatibleSchemaError lists every bad property;
on-device Laya CoreML ANE;
~5 ms P50 short decisions;
189/189 FP16 checkpoint parity;
10× not achieved;
mizorewww/laya-coreml ≠ gliner-native-runtime ≠ jevmlx ≠ NandhaKishorM/laya;
softmax over allowed tokens ≠ Noul;
question-first cache;
Micha0827/snapjudge ≠ githubnext/localjev ≠ jevmlx ≠ cendress/SnapJudge;
Jev-first Pi agent loop;
slow-LLM fallback;
explicit action menu / CandidateSource unimplemented;
62 tests wiring not quality;
direwolfiy/JevPi ≠ standardagents/jevpilot ≠ pi-jev-control.

1. **Jev IS the if-statement** (PRIMARY) —
   judgments/probabilities drive branches.
   text model only writes prose.
   interpreter owns variables/loops/budgets/replay.
   otherwise maybe / confidence gate.
   chaos samples after the gate.
   southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠
   Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably.
2. **GEPA alignment loop live delta** —
   133★ / forks 10 live.
   build calibrated classifiers from human feedback.
   HEAD/README SHA unchanged vs §93. Do **not** re-dump
   the loop.
3. **Memory: retrieve vs lease** —
   retrieve by relevance not resemblance.
   one calibrated yes/no per memory in one request.
   pointer mode 17/18 19/20 *theirs*.
   embedding resemblance misses the allergy.
   samdotmak/jev-recall ≠ jev-search ≠ jev-sift ≠
   carryforward ≠ chopratejas/invalidate.
   memory leases ended by new evidence.
   six Nouls then fixed rules in code.
   0 of 157 false invalidations.
   questions/plans/directives are not evidence.
   unsure → review queue.
   host keeps the store.
4. **Contract-of-artifact lint** —
   name↔body / comment truth / test-claims.
   mizchi/jev-lint is mizchi/jevlint rename.
   no shipped rule has severity error.
   ~1 in 5 findings wrong *theirs*.
   mizchi/jev-lint ≠ huntedman/JevLint ≠
   MichitoSugawara/jev-lint.
5. **JSON Schema as question compiler** —
   JSON Schema → typed JSON via Jev.
   noul_threshold 0.5 decoder not a proof.
   IncompatibleSchemaError lists every bad property.
6. **Local System One economics** —
   on-device Laya CoreML ANE.
   ~5 ms P50 short decisions.
   189/189 FP16 checkpoint parity.
   10× not achieved.
   mizorewww/laya-coreml ≠ gliner-native-runtime ≠ jevmlx
   ≠ NandhaKishorM/laya.
   softmax over allowed tokens ≠ Noul.
   question-first cache.
   Micha0827/snapjudge ≠ githubnext/localjev ≠ jevmlx ≠
   cendress/SnapJudge.
   Jev-first Pi agent loop.
   slow-LLM fallback.
   explicit action menu / CandidateSource unimplemented.
   62 tests wiring not quality.
   direwolfiy/JevPi ≠ standardagents/jevpilot ≠
   pi-jev-control.

Soft Noul ≠ hard safety. 80% / 17/18 / 0 of 157 /
4.98 ms / 189/189 / 87.7 vs 81.2 / 62 tests are
**sensors**. Hard-gating `feels`, pasting 17/18 as
Harbor, hard-gating 0 of 157 as a proof, treating
boolean @ 0.5 as safety, claiming 10×, treating
softmax as a Noul, or treating wiring tests as quality
is the same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul is a
SENSOR. The interpreter / lease policy / schema
envelope / AST matcher is exact work.

## Apply 2041 (`notes.md` §101)

Same pillars, nine HIGH clusters (resume-screening
bias audit PRIMARY; MCDA panel + code-owned
pass|review|block; EU cost-aware routing; frozen-protocol
class bake-off; VOI admission; Leveson sensor≠authority
control plane; scoring economics / live MCDA;
pre-registered calibration/safety science; class
infrastructure SDK). Do **not** re-fold 1943 / §100 /
1843 / §99 / 1740 / §98 / 1639 / §96 /
gliner-native-runtime / §97 / 1541 / §95 / jev-align
*mechanism* / §93. Fresh PR; never reopen merged
#7–**#18**. Skip Archer rewrite (still **NOT landed**;
likes **54** vs §100 pin **51**; lastModified
**CHANGED** `2026-09-20T02:59:13Z`). Quote live
REST over watch claims. `invented_signal: false`.
0★ HIGH still gets a real card. rh-guard owns
injection/steer. Augustus owns placement.

Unique consecutive fragments:
resume-screening bias audit methodology; name×resume factorial independent Nouls; callback determined by resume quality; mean-probability name gaps operationally negligible; natemoo-re/bias-bench ≠ BBQ; Plan/PRD panel → code-owned pass|review|block; cheerleading out of scope; austindixson/planalyzer ≠ single-goodness Noul; cost-aware multi-model routing/escalation; decide vs do; successful-task cost; cannacre8ive/switchboard-ai ≠ ha-switchboard ≠ hermes-switchyard; frozen-protocol zero-shot bench; TypeSafe Jev vs PrismNLI vs Laya; contamination caveat; elcronos/jev-vs-open-decision-models ≠ JevBench ≠ DMB; context-window admission control; VOI gate which tokens are worth the expensive model; fail polarity per lens; on small inputs lenses lose money; cvsgireesh/jevusher ≠ jev-sift ≠ winnow; typed decision control plane; receipt ≠ authorization; historical-v0 zero retained cases; MokiMeow/jev-fabric ≠ jev-forge ≠ dgp; live 15-dim typed rubric re-score per pause; scoring economics exemplar; OpenJev/Codiv ≠ TypeSafe hosted; jose-troche/live-rubric ~$0.000004 desc / ~$0.000006 README; adversarial pre-registered Jev eval; 28 predictions before data; 123,805 requests; confidence does not track ignorance; polite injection 65% / crude 0%; willkelly/jev-evaluation ≠ jevals ≠ jev-baselines-eval; provider-neutral Elixir/BEAM Noul/Choice/Score SDK; class infrastructure; nshkrdotcom/system_one_sdk ≠ typesafe_sdk ≠ dannote/jev;

1. **Resume-screening bias audit methodology** (PRIMARY) —
   name×resume factorial independent Nouls.
   callback determined by resume quality.
   mean-probability name gaps operationally negligible.
   natemoo-re/bias-bench ≠ BBQ.
2. **MCDA panel + code-owned aggregation** —
   Plan/PRD panel → code-owned pass|review|block.
   cheerleading out of scope.
   austindixson/planalyzer ≠ single-goodness Noul.
3. **EU cost-aware routing / escalation** —
   cost-aware multi-model routing/escalation.
   decide vs do.
   successful-task cost.
   cannacre8ive/switchboard-ai ≠ ha-switchboard ≠
   hermes-switchyard.
4. **Frozen-protocol class bake-off** —
   frozen-protocol zero-shot bench.
   TypeSafe Jev vs PrismNLI vs Laya.
   contamination caveat.
   elcronos/jev-vs-open-decision-models ≠ JevBench ≠ DMB.
5. **VOI admission control** —
   context-window admission control.
   VOI gate which tokens are worth the expensive model.
   fail polarity per lens.
   on small inputs lenses lose money.
   cvsgireesh/jevusher ≠ jev-sift ≠ winnow.
6. **Leveson sensor ≠ authority** —
   typed decision control plane.
   receipt ≠ authorization.
   historical-v0 zero retained cases.
   MokiMeow/jev-fabric ≠ jev-forge ≠ dgp.
7. **Scoring economics / live MCDA** —
   live 15-dim typed rubric re-score per pause.
   scoring economics exemplar.
   OpenJev/Codiv ≠ TypeSafe hosted.
   jose-troche/live-rubric ~$0.000004 desc /
   ~$0.000006 README.
8. **Pre-registered calibration/safety science** —
   adversarial pre-registered Jev eval.
   28 predictions before data.
   123,805 requests.
   confidence does not track ignorance.
   polite injection 65% / crude 0%.
   willkelly/jev-evaluation ≠ jevals ≠
   jev-baselines-eval. rh-guard owns injection.
9. **Class infrastructure SDK** —
   provider-neutral Elixir/BEAM Noul/Choice/Score SDK.
   class infrastructure.
   nshkrdotcom/system_one_sdk ≠ typesafe_sdk ≠
   dannote/jev.

Soft Noul ≠ hard safety. 25.0% / 0.72 / V0.4 / 0.587 /
0.725 / 6,866-to-keep-out-143 / zero retained cases /
$0.000004 / $0.000006 / ECE 0.075 / 47% / 65% are
**sensors**. Treating a zero binary name gap as a
fairness certificate, letting Jev emit the verdict
string, pasting PrismNLI's lead without the
contamination caveat, treating J7 pass as safe to
obey, treating a receipt as authorization, hard-gating
confidence ≥0.95, or treating an unofficial SDK as
TypeSafe official is the same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul is a
SENSOR. The factorial design / panel aggregation /
routing policy / PROTOCOL / fail polarity / Fabric
packs / rubric compiler / pre-registered plan / OTP
client is exact work.

## Apply 2145 (`notes.md` §102)

Same pillars, nine HIGH clusters (question-linting of
Jev questions themselves PRIMARY; open-weights Laya as
class exemplar (binding); on-chain/edge Laya deploy;
auditable weekend replica; adversarial dual-judge /
framing attack surface; Laya specialist + Hub replica
drop; distillation economics / teacher-of-record;
non-LLM VIN System One; source-bound evidence + bounded
judgments). Do **not** re-fold 2041 / §101 / 1943 /
§100 / 1843 / §99 / 1740 / §98 / 1639 / §96 /
gliner-native-runtime / §97 / 1541 / §95 / jev-align
*mechanism* / §93. Fresh PR; never reopen merged
#7–**#19**. Skip Archer rewrite (still **NOT landed**;
last pin §101: likes **54**; lastModified
`2026-09-20T02:59:13Z`; Hub HTTP **401**). Quote live
REST over watch claims. `invented_signal: false`.
0★ HIGH still gets a real card. Open-weights Laya is
the *class* exemplar this hour, not a TypeSafe drop-in.

Unique consecutive fragments:
question-linting of Jev questions themselves; nine jaggedness rules, no API key, no labelled data; static lint ≠ measured separation; yodablocks/jevq ≠ tenbin ≠ JevLint ≠ commitjev; open-weights Laya as class exemplar (binding); Nx/Bumblebee runtime; host chooses backend; ChristianAlexander/laya_ex ≠ system_one_sdk ≠ dannote/jev ≠ NandhaKishorM/laya; on-chain/edge Laya deploy; parity_verified stays false; model output never grants Tx; humandebri/IC-Laya ≠ laya_ex; auditable weekend replica; Jev outputs never used for training; soft human-vote distributions; unpaired 0.577 vs 0.727; agilabs-ai/jev48 ≠ JevBench ≠ Mapika/decider; adversarial dual-judge / framing attack surface; comparative framing is the usable judgment; prior injection crowds out evidence; copyleftdev/ember ≠ ember.js; Laya specialist fine-tune pipeline; training still GPU-pending; PIXELZX0/XERON ≠ convaiinnovations/laya; Hub Laya replica drop; daliborsb/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya; System One student distillation corpus; gold is programmatic; teacher is closed-API clone; do not distill Jev as teacher of record; MagaBitmex/jev-4b-distill-data ≠ missing student checkpoint; non-LLM VIN System One; planning depth not chat; lewislululu/jevon ≠ douglance/jevon; source-bound evidence checks; local quote mismatch needs no API; exit 0 ≠ claim truth; WaynezProg/jev-kit ≠ jonathanavis96/jev-kit (Airlock) ≠ jev-use ≠ jev-mcp;

1. **Question-linting of Jev questions themselves** (PRIMARY) —
   nine jaggedness rules, no API key, no labelled data.
   static lint ≠ measured separation.
   yodablocks/jevq ≠ tenbin ≠ JevLint ≠ commitjev.
2. **Open-weights Laya as class exemplar (binding)** —
   Nx/Bumblebee runtime.
   host chooses backend.
   ChristianAlexander/laya_ex ≠ system_one_sdk ≠ dannote/jev
   ≠ NandhaKishorM/laya.
3. **On-chain/edge Laya deploy** —
   parity_verified stays false.
   model output never grants Tx.
   humandebri/IC-Laya ≠ laya_ex.
4. **Auditable weekend replica** —
   Jev outputs never used for training.
   unpaired 0.577 vs 0.727.
   agilabs-ai/jev48 ≠ JevBench ≠ Mapika/decider.
5. **Adversarial dual-judge / framing attack surface** —
   comparative framing is the usable judgment.
   prior injection crowds out evidence.
   copyleftdev/ember ≠ ember.js.
6. **Laya specialist + Hub replica drop** —
   Laya specialist fine-tune pipeline.
   training still GPU-pending.
   PIXELZX0/XERON ≠ convaiinnovations/laya.
   daliborsb/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya.
7. **Distillation economics / teacher-of-record** —
   gold is programmatic.
   teacher is closed-API clone.
   do not distill Jev as teacher of record.
   MagaBitmex/jev-4b-distill-data ≠ missing student checkpoint.
8. **Non-LLM VIN System One** —
   planning depth not chat.
   lewislululu/jevon ≠ douglance/jevon.
9. **Source-bound evidence + bounded judgments** —
   local quote mismatch needs no API.
   exit 0 ≠ claim truth.
   WaynezProg/jev-kit ≠ jonathanavis96/jev-kit (Airlock) ≠ jev-use ≠ jev-mcp.

Soft Noul ≠ hard safety. 0.03s / 0.75 vs 0.81 / 62 tests /
4.8 MiB / 0.577 vs 0.727 / AUROC 0.769 vs acc 50.1 /
+0.199 / +26,744 / 0 of 2,816 / 131,967 sequences /
$0.03/1k / maze 1.0000 / snake 0.9674 / exit 0 are
**sensors**. Treating a clean jevq run as measured
separation, treating 62 IC-Laya tests as Laya parity,
letting a Score tail grant Tx, pasting "Jev48 beats Jev
on phishing" from AUROC, injecting class priors as
"help", treating v4 as a pharmacy controller, pasting
sequence counts as trained quality, re-pasting a copied
vs-Jev table, distilling Jev as teacher of record,
pasting maze 1.00 as a general System One, or treating
jev-kit exit 0 as claim truth is the same theater as
jev-gate §79.

Formal methods **compose** with scoring. A Noul is a
SENSOR. The jaggedness regex / Nx backend / canister
schema stamp / weekend freeze / kernel+doctrine /
FT pipeline / Hub layout / programmatic gold / VIN
recurrence / local quote match is exact work.

## Apply 2246 (`notes.md` §103)

Same pillars, nine HIGH clusters (independent System
One evidence catalog PRIMARY; typed eval freeze;
option-isolated tiny replica; frozen-LLM typed
decisions; AR next-token anti-pattern; formal compose
with scoring; parallel rank vs serial selection;
open-side ecosystem catalog; knowledge-work paper
radar). Do **not** re-fold 2145 / §102 / 2041 / §101 /
1943 / §100 / 1843 / §99 / 1740 / §98 / 1639 / §96 /
gliner-native-runtime / §97 / 1541 / §95 / jev-align
*mechanism* / §93. Fresh PR; never reopen merged
#7–**#20**. Skip Archer rewrite (still **NOT landed**;
Hub 401 last pin §101). 0★ HIGH still gets a real
card. Soft Noul ≠ hard safety. Formal methods
**compose** with scoring; a Noul is a SENSOR.

1. **Independent System One evidence catalog** —
   19 reviewed records.
   scores not one leaderboard.
   no external record currently reproduced.
   TokenTrim no-Jev matched hybrid 62.4%.
   reachjalil/system-one-bench ≠ mallahyari/system-one-benchmark.
2. **Typed eval freeze** —
   21 tasks · 134 items · 208 questions.
   scenes from public GitHub contracts, not production logs.
   SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv/jev-eval ≠ xxkuboxx/jev-eval ≠ onlyoneaman/jev-eval ≠ dayhaysoos/jevals.
3. **Option-isolated tiny replica** —
   option isolation (sibling-blind).
   permutation-equivariant.
   Hub OWNER not published.
   nafisazizir/hev ≠ jaredpalmer/kev.
4. **Frozen-LLM typed decisions** —
   frozen local LLM logits, no trained decision head.
   residual-head 9,222-param decreased 73/96→67/96.
   confidence = 1−normalized entropy, not P(correct).
   yuki-oshio/mini-jev ≠ r-ms/mini-jev.
5. **AR next-token anti-pattern** —
   Jev classifier as autoregressive next-token predictor.
   ChatJev-style soundness theater.
   erik-dunteman/ChatJev ≠ dannote/jev ≠ jev-gpt.
6. **Formal compose with scoring** —
   calibrated decision head × AlphaProof value head.
   implementation-layer isomorphism, semantic difference.
   timeout = censoring.
   do not launder Noul as proof.
7. **Parallel rank vs serial selection** —
   parallel rank-prediction vs serial selection.
   independent questions can conflict.
   zzzzzec/jevsort ≠ keltokhy/jsort.
8. **Open-side ecosystem catalog** —
   curated open System One ecosystem catalog.
   rupeshpoojary9/awesome-open-system-one ≠ AnotiaWang/awesome-jev.
9. **Knowledge-work paper radar** —
   arXiv paper radar with Jev relevance scoring.
   ranking ≠ calibration / 0.5 still soft.
   fail-open failed evals not marked seen.

Soft Noul ≠ hard safety. 62.4% / 208 questions /
80.00% / 0/696 / 93.25% / 73/96→67/96 / “kinda works”
/ softmax-head isomorphism / 1★ / 0.5 are
**sensors**. Treating a catalog row as a bake-off
win, treating constructed scenes as production logs,
pasting Hev 80.00% as Jev identity, quoting 93.25% as
family-disjoint, putting Jev in an AR next-token
loop, laundering a Noul as a Lean step, treating
parallel rank-k as a sort proof, pasting a curated
list’s von sub-15ms as an Augustus fact, or
hard-thresholding paper-radar 0.5 as frequency is
the same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul is a
SENSOR. The catalog labels / freeze / option mask /
logit read / Choice tree (jev-gpt) / Lean kernel /
serial selection / open-side list / fetch+persist
are exact work. ChatJev-style soundness theater is
the anti-pattern.

## Apply 2340 (`notes.md` §104)

Same pillars, eleven HIGH clusters (from-scratch
calibrated decision model PRIMARY; ORDER BY ranking
upgrade; find/design/evaluate decision loops;
distill-Jev UI stub anti-pattern; post-launch scored
opportunity map; Jev-inize a use case; saved-decision
regression; constrained-logprob API; SmolLM RLCD
reproduction; source-backed Awesome radar; rival-aware
one-pass scorer). Do **not** re-fold 2246 / §103 /
2145 / §102 / 2041 / §101 / 1943 / §100 / 1843 / §99 /
1740 / §98 / 1639 / §96 / gliner-native-runtime / §97 /
1541 / §95 / jev-align *mechanism* / §93 /
jev-orderby-bench *six-gates* / §60. Fresh PR; never
reopen merged #7–**#21**. Skip Archer rewrite (still
**NOT landed**; Hub 401). 0★ HIGH still gets a real
card. Soft Noul ≠ hard safety. Formal methods
**compose** with scoring; a Noul is a SENSOR.

1. **From-scratch calibrated decision model** —
   train calibrated ~27M from scratch.
   typed Q→prob dist / one forward pass / no LLM decode.
   hyusi2003/MiniSystemOne ≠ Colvin0315/MiniSystemOne.
   description-only stub / size 5.
2. **ORDER BY ranking upgrade** —
   ESCI hard probe fails four of six.
   jev_bool ECE 0.242 inversion 0.255.
   do not re-fold §60 six-gates as new.
   jobbyjev one-request-per-company from batch-size result.
3. **Find/design/evaluate decision loops** —
   find/design/evaluate TypeSafe Jev decision loops.
   karanb192/jev-architect ≠ samtay32/jev-system-architect.
4. **Distill-Jev UI stub** —
   Jairik/jev-distiller size 1.
   distill-Jev UI stub / do not distill Jev as teacher of record.
5. **Post-launch scored opportunity map** —
   post-launch scored use-case map / Jev self-scores then human curation.
   licensedsaucer9-web/jev-opportunities.
6. **Jev-inize a use case** —
   Jev-inize a use case into classifier/router.
   gavinHuang/jevinize → simple-jev not TypeSafe.
   featherless-ai/simple-jev.
7. **Saved-decision regression** —
   compare saved decisions / same label can still change the branch.
   VihaanAgarwal/jev-diff ≠ Saik0s/diffusiongemma-jev-macos.
   not tested with a live Jev API key.
8. **Constrained-logprob API** —
   constrained logprob + temp/Platt ≠ Noul.
   OpenJevPro pastes openjev-sglang JevBench as own.
   zhangcy122/OpenJevPro ≠ IamBusy/OpenJev ≠ ekzhang/openjev-sglang.
   PolyForm Noncommercial.
9. **SmolLM RLCD reproduction** —
   SmolLM-135M / sub-70ms / 0 output tokens.
   demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055.
   README claims MIT / GitHub license null / no LICENSE file.
   patelvishwa112/jev-system-one-rlcd ≠ arnabgho/rlcd-lite ≠ blackwood-rlcd.
10. **Source-backed Awesome radar** —
    source-backed Awesome Jev radar / 306+ commit-pinned.
    logicrw/awesome-jev-projects ≠ AnotiaWang/awesome-jev ≠ yibie/awesome-jev ≠ cobanov/awesome-jev ≠ rupeshpoojary9/awesome-open-system-one.
    auto GitHub sync / Issue-only submissions.
11. **Rival-aware one-pass scorer** —
    hashed n-gram encoder / rival-aware attention.
    olanotolu/jevbetter vs jevlike starter.
    synthetic hard menus top-1 0.916 vs 0.873 / ECE 0.0182 vs 0.0367 / 40 vs 4608 menus/sec.
    shuffled-context control 0.335.

Soft Noul ≠ hard safety. ~27M / 4.7h / 0.242 / 0.255 /
size 1 / 0.81→0.79 / 95.5% pasted / 0.5052 / 136★ /
0.916 are **sensors**. Treating a description-only
stub as a checkpoint, re-folding six-gates as new,
distilling Jev as teacher of record, pasting
openjev-sglang as OpenJevPro, treating constrained
logprob as a Noul, quoting an untrained-looking demo
as Jev identity, pasting a radar's listed numbers,
or quoting 0.916 as a class ceiling is the same
theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul is a
SENSOR. The from-scratch encoder / SQL secondary key /
workflow inspection / independent gold / human TOP
curation / decision map / saved-trace compare /
grammar mask / Brier training / commit-pin / rival
attention are exact work. Distill-Jev UI stub and
constrained-logprob-as-Noul are the anti-patterns.


## Apply 0042 (`notes.md` §105)

Same pillars, twelve HIGH clusters (structured
probability readouts PRIMARY; ordinary-model
Jev-shape; open-weight Laya measurement; cheap
fail-open semantic edge; fan-out measurement;
VLM+Jev RL teacher; independent Jev API vs Laya;
locate vs decide; throughput arena; behavioral
contracts; evidence-linked upgrade review;
knowledge-work discography). Do **not** re-fold
2340 / §104 / 2246 / §103 / 2145 / §102 /
2041 / §101 / 1943 / §100 / 1843 / §99 / 1740 /
§98 / 1639 / §96 / gliner-native-runtime / §97 /
1541 / §95 / jev-align *mechanism* / §93. Fresh
PR; never reopen merged #7–**#22**. Skip Archer
rewrite (still **NOT landed**; Hub 401). 0★ HIGH
still gets a real card. Soft Noul ≠ hard safety.
Formal methods **compose** with scoring; a Noul is
a SENSOR.

1. **Structured probability readouts** —
   structured probability readouts.
   distribution > argmax.
   Noul 0.5 midpoint.
   score is expectation not integer.
   bare HTTP not SDK.
   Arohtea/jev-readout.
2. **Ordinary-model Jev-shape** —
   Jev-style Choice/Score/Noul from ordinary models.
   optional DSH plugin.
   schema-valid ≠ calibrated.
   gulagala001/jevify ≠ Mintzs/jevify.
3. **Open-weight Laya measurement** —
   Laya RLCD benchmark.
   40.3% below constant-answer.
   open-weight measurement.
   mourad-ghafiri/laya-rlcd-benchmark ≠ yibie/laya-jev-lab.
4. **Cheap fail-open semantic edge** —
   cheap fail-open semantic edge.
   second signal not sole.
   FastLoopError catch.
   SupremeDreamZ/jev-fastloop ≠ jev-ultrafast.
5. **Fan-out measurement** —
   asking more questions in one call.
   0.980 at every N.
   nearly not fully deterministic.
   TheWebDevel/jev-fanout.
6. **VLM+Jev RL teacher** —
   Qwen3-VL perception + Jev decisions train RL.
   0 model calls at deployment.
   VLM alone 1.7 vs +Jev 4.4.
   harneet2512/reflexrl ≠ khordoo/jev-reflex-autonomy-lab.
7. **Independent Jev API vs Laya** —
   independent Jev API vs Laya.
   cascade 0.60 matches 78% at 1.8×.
   noul facts not judgements.
   yibie/laya-jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab.
8. **Locate vs decide** —
   GLiNER vs GLiFormer vs Laya vs Jev.
   extractors ≠ decision engines.
   Laya dict-instructions collapse 58.3%.
   umstek/zero-shot-ie-bench.
9. **Throughput arena** —
   decisions-per-minute & cost.
   204 moves vs 73.
   throughput not intelligence.
   angelgalvisc/snake-arena-jev-vs-llms ≠ vtrivedy/jev-plays-games.
10. **Behavioral contracts** —
    behavioral contracts.
    pin expectations eval upgrades.
    raw 0.94 is not a release.
    sathariels/jevcheck ≠ dayhaysoos/jevals ≠ SivletLabs/jev-eval.
11. **Evidence-linked upgrade review** —
    evidence-linked dependency upgrade.
    Jev never generates filenames.
    no_direct_evidence ≠ safe to merge.
    GaneshVG18/upgrade-radar ≠ LYchoon/paper-radar-jev.
12. **Knowledge-work discography** —
    discography theme/mood/complexity.
    five atomic questions one call.
    lirantal/discoprint.

Soft Noul ≠ hard safety. 0.5 / 59/41 / 2.69 /
schema JSON / 40.3% / 4/5 / 0.980 / 0.0000 /
4.40 / 2.95× / 78% / 0.60 / 58.3% / 21 pts /
0.94 / `no_direct_evidence` / theme Choice are
**sensors**. Treating displayed p as proof,
schema-valid JSON as a calibrated Noul,
40.3% without the constant-answer, fused
fastloop p as safety, 0.0000 sd as universal
determinism, 2.95× as Harbor, cascade 0.60 as
a hard gate, locate as decide, snake points as
intelligence, jevcheck as a correctness proof,
`no_direct_evidence` as merge-safe, or a theme
Choice as a music-theory certificate is the
same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul
is a SENSOR. Bare HTTP bytes / adapter
normalization / constant-answer baseline /
keyword first-signal / packed-question
experiment / pixels-only policy / cascade
threshold as a compromise / extractor spans /
fixed output-token shape / pin+replay / code-
owned spans / catalog fetch+cache are exact
work. Hard-gating a soft Noul as safety is the
anti-pattern.


## Apply 0145 (`notes.md` §106)

Same pillars, seventeen HIGH clusters / four themes
(architecture probes PRIMARY; measurement densifies;
catalog gravity; HF class ports). Do **not** re-fold
2340 / §104 / 2246 / §103 / 2145 / §102 / 2041 / §101 /
1943 / §100 / 1843 / §99 / 1740 / §98 / 1639 / §96 /
gliner-native-runtime / §97 / 1541 / §95 / jev-align
*mechanism* / §93 / jev-orderby-bench *six-gates* / §60 /
JevBench v1.2 *board* / §78. Fresh PR; never reopen
merged #7–**#23**. do not reopen or amend PR #23.
Skip Archer rewrite (still **NOT landed**; Hub 401).
0★ HIGH still gets a real card. Soft Noul ≠ hard
safety. Formal methods **compose** with scoring; a
Noul is a SENSOR.

1. **Jevify-any-LLM architecture probe** —
   Turn any open LLM into System-One Jev.
   uspraveen/Jevify ≠ Mintzs/jevify ≠ gulagala001/jevify.
   Jevify-any-LLM architecture probe.
   description-only stub / size 0.
2. **Encoder-only from a task sentence** —
   Train encoder-only calibrated decision models from a task sentence.
   Exu is a toolkit, not a method. strictly proper scoring rule. Pre-alpha.
   Ruivalim/exu-base.
3. **Scratch-trained recipe upgrade** —
   scratch-trained calibrated decision model. typed Q → probability dists.
   Colvin0315/MiniSystemOne ≠ hyusi2003/MiniSystemOne.
   no published weights download URL. 90.5 seconds / 29.2% pipeline evidence.
   p_i/p_j independent of other candidates.
4. **Recipe small model out** —
   Recipe for calibrated decision models — small model out.
   init → synth → train → eval → serve.
   91.1 % / ECE 0.022 *theirs*. Jev zero-shot 75.1. scienthoon/luce.
5. **Headline claims trial** —
   Put Jev's three headline claims on trial. 0.5B local GPU.
   46x speedup / accuracy identical. ECE 0.624 sentiment catastrophe.
   bigger model worse calibration.
   RichardoMrMu/jev-mini ≠ yuki-oshio/mini-jev ≠ r-ms/mini-jev.
6. **Local structured-choice engine** —
   System-1 decision engine for local LLMs. structured choices only.
   JSON parse of generated text ≠ Noul. TypefAI JEV / Journal Entry Voucher.
   tapsin/jev-local ≠ us/jev-local ≠ Argos1111/jev_local.
7. **Reward-model 8-track** —
   Jev 1.13 reward-model eval across 8 benchmark tracks.
   40,940 examples / 0 API errors. RewardBench v1 92.58%. Precise IF 50.63%.
   goya4140/jev-reward-model-evaluation.
8. **Ticket-router scaffold** —
   Jev vs LLM support-ticket routing. Scaffolding in progress.
9. **Cost bench** —
   static + live decision bench. TypeSafe's own published benchmark.
   illustrative simulations, not live API calls.
10. **JevBench v1.2.3 densify** —
    JevBench v1 — smart/cheap/fast/reliable. I/C/S/K 25% geometric mean.
    classifier.dev fast tier 84.8 is Jev behind its own API.
    do not re-fold §78 v1.2 board as new. Laya (421M) 70.1 now on board.
11. **Budget-in-code remainder** —
    Zero-shot/few-shot LLM routing. hard budget filter before Jev.
    Jev never asked to perform budget arithmetic.
12. **XState compose** —
    Jev judges the next state, XState enforces transitions.
    simulation uses synthetic keyword fixtures.
13. **Consistency Space** —
    Consistency benchmark Space. This Space contains no benchmark result yet.
    12-case plumbing fixture.
14. **Catalog gravity** —
    catalog gravity. v-modal/awesome-jev-tools. ★339 live REST.
    curation is not endorsement.
15. **Crawler directory** —
    crawler-maintained directory. Daily GitHub + npm sweep, human-merged.
    RadRebelSam/awesome-jev ≠ AnotiaWang ≠ yibie ≠ cobanov ≠ logicrw ≠ v-modal.
16. **HF peft retrieval port** —
    HF peft SPLADE/BGE reranker. rdxtremity/jev-reranking ≠ carlaiau/jev-reranking.
    query-side encoders, not a Jev replica.
17. **ONNX scorer port** —
    ONNX System One Qwen3.5-4B scorer. source:pngwn/system-one-qwen3.5-4b-scorer.
    CC-BY-NC-4.0. temperature 1.75. transformers.js AutoModel cannot load this graph.

Soft Noul ≠ hard safety: 90.5s / 29.2% / 91.1% / 46x /
0.624 / 92.58% / 84.8 / ★339 / T=1.75 are **sensors**.
Treating a Jevify two-liner as a checkpoint, pasting
Colvin as hyusi, treating JSON parse as a Noul, quoting
46x / 91.1% / 92.58% / 84.8 as class ceilings, treating
classifier.dev #1 as a better model, re-folding §78 as
new, letting Jev do budget arithmetic, treating XState
as Jev, pasting catalog ★ as eval, treating SPLADE as
TypeSafe Jev, or treating an empty consistency Space as
a win is the same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul is a
SENSOR. The any-open-LLM probe / encoder-only toolkit /
from-scratch recipe / LoRA+head recipe / local GPU trial
/ JSON-parse honesty / RM tracks / scaffold hole /
vendor cost infographic / geometric-mean bench / budget
filter in code / XState envelope / catalog map /
crawler sweep / query-side encoders / ONNX port /
empty consistency protocol are exact work. Jevify stub
and JSON-parse-as-Noul are the anti-patterns.


## Apply 0243 (`notes.md` §107)

Same pillars, eight HIGH clusters / three themes
(measurement densifies PRIMARY; open reproduction
class ports; study densification). Do **not** re-fold
0145 / §106 / 0042 / §105 / 2340 / §104 / 2246 / §103 /
2145 / §102 / 2041 / §101 / 1943 / §100 / 1843 / §99 /
1740 / §98 / 1639 / §96 / gliner-native-runtime / §97 /
1541 / §95 / jev-align *mechanism* / §93 /
jev-orderby-bench *six-gates* / §60 / JevBench v1.2
*board* / §78 / openJev-verdict *claim-audit* / §71.
Fresh PR; never reopen merged #7–**#24**. do not
reopen or amend PR #23 or #24. Skip Archer rewrite
(still **NOT landed**; Hub 401). 0★ HIGH still gets a
real card. Soft Noul ≠ hard safety. Formal methods
**compose** with scoring; a Noul is a SENSOR.

1. **Benchmark-driven router + judge** —
   Benchmark-driven Jev router and judge.
   cheap alone is not success.
   Jev does not write, sum prices, or claim accuracy %.
   Sol 94.2 / Luna 83.9 / Jev path 89.7.
   19.2% Sol / 62.3% cost save / 4.5pp miss of 2pp non-inferiority.
   p50 latency worse than Sol due to routing overhead.
   erendikmenn/jev-llm-router-benchmark ≠ jev-rag-benchmark ≠ ryantsai/jev-llm-router.
2. **Support ticket router** —
   Express + node:sqlite. mock and Jev decision engines.
   previous_ticket_count >= 3 is code. MIN_CONFIDENCE 0.6 still soft.
   substring false positives.
   aesaganda/jev-ticket-router ≠ SarathChandraBellam/jev-vs-llm-ticket-router.
3. **Universal figure router** —
   Universal Figure & Diagram Router.
   confidence ≥ 0.85 hard-gate is theater.
   generative AI banned from scientific plots. six visual branches.
   hoangngochuong24947-gif/jev-figure-router.
4. **Human-labeled feedstock** —
   human-labeled (state, question, label).
   166,054 rows / 22 configs. soft_label for human uncertainty.
   Praveenrajus/jev-bench ≠ fstandhartinger/jevbench.
5. **Ternary bonsai GGUF** —
   ternary bonsai System One GGUF.
   openjev's mechanism, Bonsai's weights. Hub does not ship weights.
   100/100 easy T/F is not Harbor. label_mass ≠ correctness.
   stock llama.cpp Q2_0 silently gibberish.
   NicolaiMTLassen/open-bonzi-jev ≠ NicolaiLassen.
6. **DeBERTa ONNX t.js port** —
   transformers.js DeBERTa ONNX.
   source:com-kotobalabs/open-jev-deberta-v3-large.
   temperature 1.05. AutoModel from_pretrained works.
   onnx-community/open-jev-deberta-v3-large-ONNX ≠ system-one-qwen3.5-4b-scorer-ONNX.
7. **verdict NAR densify** —
   107★ densify. GH 151M vs README 149.6M.
   PR #1 now closed unmerged. do not re-fold §71 claim-audit as a beat.
8. **Study notes densify** —
   typed decisions, RLCD, confidence-gated routing.
   structured ≠ correct. mock not live API. 26 tests.
   wjdjdakf17/jev-study ≠ baekenough/jev-study.

Soft Noul ≠ hard safety: 94.2 / 89.7 / 62.3% / 4.5pp /
0.85 / 100/100 / 166,054 / T=1.05 / 77.10% / 107★ are
**sensors**. Treating a 0.85 figure FAST_PATH as a
proof, 100/100 easy T/F as Harbor, label_mass as
correctness, 77.10% as beating Jev, collapsing
ticket-router into Sarath, collapsing jev-bench into
jevbench, collapsing DeBERTa ONNX into the Qwen scorer
ONNX, quoting 62.3% without the 4.5pp miss, or
re-folding §71 as a beat is the same theater as
jev-gate §79.

Formal methods **compose** with scoring. A Noul is a
SENSOR. The router threshold/fallback/budget / ticket
count>=3 / generative-AI-ban-on-plots / Hub recipe
without weights / AutoModel-works contrast / dual-channel
ECE audit / code-consumes-p study notes are exact work.
Figure-router 0.85 hard-gate and 100/100 easy T/F as
Harbor are the anti-patterns.





## Apply 0345 (`notes.md` §108)

Same pillars, sixteen HIGH clusters / two themes
(open reproduction densifies; measurement densifies PRIMARY
for Harbor-jevals). Do **not** re-fold
0243 / §107 / 0145 / §106 / 0042 / §105 / 2340 / §104 / 2246 / §103 /
2145 / §102 / 2041 / §101 / 1943 / §100 / 1843 / §99 /
1740 / §98 / 1639 / §96 / gliner-native-runtime / §97 /
1541 / §95 / jev-align *mechanism* / §93 /
jev-orderby-bench *six-gates* / §60 / JevBench v1.2
*board* / §78 / openJev-verdict *claim-audit* / §71 /
yuki-oshio/mini-jev *93.25%* / §103. Fresh PR; never reopen
merged #7–**#25**. do not reopen or amend PR #23 or #24
or #25. Skip Archer rewrite (still **NOT landed**; Hub 401).
0★ HIGH still gets a real card. Size **0** WITH CONTENTS
still gets a real card. Soft Noul ≠ hard safety. Formal methods
**compose** with scoring; a Noul is a SENSOR. Jev is the hot
exemplar, not the whole mandate. Mathematical / logical /
algorithmic mental models across AI, SWE, business, knowledge
work — not SWE-only.

1. **Bonsai 27B v2 family card** —
   bonzi-27b-v2 / ternary-8b / 27b-v1 GGUF family densify.
   Hub still does not ship weights. WANLI-256 74.6% *theirs*.
   ternary still needs PrismML fork. 100/100 easy T/F ≠ Harbor.
   label_mass ≠ correctness.
2. **Ternary Bonsai 8B family card** —
   WANLI-256 65.2% / 200/min / 281 ms / label_mass 0.999 *theirs*.
   Same PrismML-fork requirement.
3. **Bonsai 1 27B family card** —
   Bonsai 1 27B Q1_0 runs on stock llama.cpp. WANLI-256 71.1%
   *theirs*. Do **not** collapse stock Q1_0 into §107 Q2_0
   gibberish.
4. **Laya multilingual ONNX WebGPU** —
   Laya multilingual ONNX WebGPU typed-decisions port.
   63/63 selected answers / 5.1e-4 CPU / 1.2e-2 WebGPU.
   Independent port; 63/63 argmax ≠ ECE. Script-before-p OOD
   still applies.
5. **OpenJev Vision** —
   OpenJev Vision image classification + uncertainty.
   CLEVR-4 held-out joint 0%. Pets 93.24% 740-subset ≠ official
   full-dataset. Not TypeSafe Jev; not a VLM.
6. **HF verdict twin** —
   hf:heman10x/openJev-verdict-2.0 twin tokenizer-only.
   No 149.6M weights. likes **5** ≠ GH **107★**. Do **not**
   re-fold §71 as a beat.
7. **Vision research dataset** —
   hfdataset:IamBusy/OpenJev-Vision-Research-v0.1 12,832.
   294,912 derived targets not independent samples.
8. **mini-jev residual-head densify** —
   UpHash-Network/mini-jev is yuki-oshio transfer.
   residual-head 9,222-param decreased 73/96→67/96.
   Do **not** re-fold 93.25% as Harbor.
9. **Prompt-injection ranking vs calibration** (PRIMARY) —
   jev-injection-bench 11,900 labelled prompts.
   Jev best ranking / Haiku better ECE 0.021 vs 0.058.
   0.5–0.9 band is where Jev's numbers do not mean what they say.
   Prompt wording moves panic 28%.
10. **Jev vs DSPy quality-evaluator** —
    manojlds/jev-dspy-bench ≠ dspachos/jev-dspy ≠ jmanhype/jev-dspy-lab.
    Jev agreement is similarity, never ground truth.
    no aggregate quality grade or merge gate.
11. **AbstentionBench-on-Jev** —
    AbstentionBench-on-Jev rank 1 of 20 vs 2025 field.
    question-asymmetry. forward-looking 0.465 never extreme.
12. **openkev calibration layer** —
    openkev calibration layer not a runtime.
    ECE vs coverage independent. select_threshold returns inf.
    escalation catches uncertainty not ignorance.
    misakaikato/openkev ≠ jaredpalmer/kev.
13. **Docling→Jev vs Gemini race** —
    pdf-race Docling→Jev vs Gemini. parser owns the wall clock.
    12/12 tie is a tie. titles selected not generated.
14. **Public TypeSafe JEV index** —
    ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas.
    catalog not endorsement.
15. **flopcheck tweet judgments** —
    flopcheck 16 calibrated tweet judgments. mechanical tells in code.
    Knowledge work / life: hold-before-publish.
16. **Laya calibration lab** —
    Laya calibration lab Gradio MCP. T never changes argmax.
    confidence ≠ top-label p. easy probe set refused.
    40–48 rows too small to ship T.

Soft Noul ≠ hard safety: 74.6% / 65.2% / 71.1% / 93.24% /
joint 0% / 0.980 / 0.058 / 0.855 / 12/12 / 0.466→0.081 are
**sensors**. Treating WANLI-256 as Harbor, label_mass as
correctness, Hub family cards as shipping weights, collapsing
stock Q1_0 into §107 Q2_0 gibberish, treating the HF twin as
a weights drop, quoting 93.25% as family-disjoint, hard-gating
injection ECE 0.058 as “Jev is calibrated”, quoting rank 1
without question-asymmetry / 2025 field, treating dspy-bench
as a quality claim, hard-gating pdf-race 12/12 as pipeline
equality, treating atlas listed counts as eval, hard-gating
flopcheck composite as truth, treating calibration-lab 40-row
T as production, treating CLEVR joint 0% as “vision Jev
works”, treating ONNX 63/63 as ECE, treating openkev T as
transferable, or treating select_threshold inf as a bug is
the same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul is a SENSOR.
The parser clock / regex mechanical tells / select_threshold
inf / generative-AI-ban-on-plots cousin (titles selected not
generated) / PrismML-fork vs stock llama.cpp split are exact
work. Injection ECE 0.058 as a hard gate and 40-row T as
production are the anti-patterns.


## Apply 0439 (`notes.md` §109)

Same pillars, twenty-four HIGH clusters / three themes
(open reproduction densifies; measurement densifies PRIMARY
for Harbor-jevals; applied class placements across AI, SWE,
business, knowledge work — not SWE-only). Do **not** re-fold
0345 / §108 / 0243 / §107 / 0145 / §106 / 0042 / §105 / 2340 / §104 / 2246 / §103 /
2145 / §102 / 2041 / §101 / 1943 / §100 / 1843 / §99 /
1740 / §98 / 1639 / §96 / gliner-native-runtime / §97 /
1541 / §95 / jev-align *mechanism* / §93 /
jev-orderby-bench *six-gates* / §60 / JevBench v1.2
*board* / §78 / openJev-verdict *claim-audit* / §71 /
yuki-oshio/mini-jev *93.25%* / §103. Fresh PR; never reopen
merged #7–**#26**. do not reopen or amend PR #23 or #24
or #25 or #26. Skip Archer rewrite (still
**promised_not_landed**; Hub 401). 0★ HIGH still gets a
real card. Size **0** WITH CONTENTS still gets a real card.
Soft Noul ≠ hard safety. Formal methods **compose** with
scoring; a Noul is a SENSOR. Jev is the hot exemplar, not
the whole mandate. Mathematical / logical / algorithmic
mental models across AI, SWE, business, knowledge work —
not SWE-only.

1. **Gemma-4 26B-A4B jevify** —
   Gemma-4 26B-A4B jevify classification+calibration.
   Hub jevify merged LoRA ships weights. PAWS 0.580/ece 0.288
   is the weak cell. kushalpatil/jevify-gemma4 ≠ Mintzs/jevify
   ≠ gulagala001/jevify ≠ uspraveen/Jevify. GH kushalpatil07/jevify
   404. Do **not** hard-gate n=307 ECE 0.061.
2. **26B-A4B LoRA twin** —
   LoRA adapter twin not independent eval. Stub card.
3. **Gemma-4 E4B jevify** —
   Gemma-4 E4B jevify. Smaller E4B slightly better OOD ECE
   than 26B-A4B.
4. **E4B LoRA stub** —
   E4B LoRA stub card. Not independent eval.
5. **Bonsai-8B v1** —
   bonzi Bonsai-8B v1 GGUF densify. WANLI-256 64.5% *theirs*.
   rank #4 of 6. Hub still does not ship weights.
6. **Bonsai-1.7B v1** —
   Bonsai-1.7B v1. WANLI-256 52.0% *theirs*. rank #6 of 6.
7. **Bonsai-4B v1** —
   Bonsai-4B v1. WANLI-256 60.2% *theirs*. rank #5 of 6.
   Do **not** re-card §108 27B/ternary as new.
8. **ultra_laya REVIEW** —
   roadus2 watch misspelling; lock roadius2/ultra_laya.
   ultra_laya REVIEW defects. default branch
   claude/laya-jev-review-gg5ppo. Do **not** paste vs-Jev
   table as this-fork win.
9. **JulesHuisman/jev-eval** (thin; still a card) —
   JulesHuisman/jev-eval scaffolding / README SHA c356a584 (was empty e69de29b).
   JulesHuisman/jev-eval ≠ SivletLabs/jev-eval ≠ willkelly/jev-evaluation
   ≠ 4esv ≠ xxkuboxx ≠ onlyoneaman ≠ dayhaysoos/jevals.
10. **RU accuracy/calibration audit** (PRIMARY) —
    XNLI EN 88.3% ECE 0.032 → RU 77.3% ECE 0.096.
    Δ −11.0 pp [−14.2,−7.8]; ECE +0.063.
    MASSIVE no detectable difference at n=600.
    confidence is function of p_max (r=1.000).
11. **what-is-jev rubric** —
    947 repos scored; A 273 / B 302 / C 372. LLM rubric ≠ benches.
12. **judge-jev** —
    judge-jev 0.5 still soft. Worker owns parse/thresholds.
13. **table-tennis** —
    7 bands 6/10 vs 40 bands 0/10. Physics local; Jev SENSOR.
14. **evidence-lab** —
    source receipts + confidence slider re-policy without re-inference.
    32/32 synthetic is smoke not production. 0.8 still soft.
15. **hfjev** —
    classify HF datasets across typed semantic dimensions. No numbers.
16. **jev-llm** —
    pointer-not-generator 400 human-authored responses.
    Zero hallucination = bank constraint.
17. **jevgraph** —
    proposed ≠ authorized. FewRel 160: Jev 85.0% vs lexical 13.125%.
    gated 100% (95/95) coverage 59.375%.
18. **J++** —
    J++ composable semantic computation language.
19. **whyashthakker gallery** —
    No benchmark winner is claimed. ≠ walidboulanouar.
20. **dog-last guide** —
    phishing: naive 62.6% vs regex 91.8%; 5-atomic + LR 95.0% *theirs*.
21. **AITuber** —
    AITuber tension ±15. Thin demo; still a card.
22. **shinpr reranker** —
    README npm global; repo is Rust. 0.5 still soft.
23. **git-confess** —
    git-confess code owns counting/blame/ratio.
    httpx exhibit 11% (13/119) *theirs*. Not a person verdict.
24. **paper-trader** —
    90d trend +12.40% vs random +12.75% vs BH +41.71%.
    5m win rate 25%. Do **not** treat fills as edge.

Soft Noul ≠ hard safety: 0.834 / 0.844 / 0.061 / 0.043 /
64.5% / 60.2% / 52.0% / 88.3→77.3 / 32/32 / 85.0% /
+12.40% / 11% are **sensors**. Treating WANLI-256 as Harbor,
label_mass as correctness, LoRA stubs as independent eval,
jevify n=307 ECE as a hard gate, 32/32 as production,
0.8 evidence as proof, 40-band 0/10 without 7-band,
/judge 0.5 as truth, git-confess 11% as a person verdict,
paper-trader +12.40% as edge, Awesomejev 656/38160 as eval,
tracker likes as Archer landing, or jevgraph 100% gated as
production is the same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul is a SENSOR.
Physics / git blame / KG authorization / reply bank /
fills/PnL / Worker thresholds are exact work. Hard-gating
jevify ECE 0.061, 0.8 evidence, /judge 0.5, or paper-trader
fills as edge are the anti-patterns.

Unique consecutive fragments (this hour):
kushalpatil/jevify-gemma4 ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify;
GH kushalpatil07/jevify 404;
PAWS 0.580/ece 0.288 is the weak cell;
smaller E4B slightly better OOD ECE than 26B-A4B;
WANLI-256 64.5% / 60.2% / 52.0% *theirs*;
rank #4 / #5 / #6 of 6;
JulesHuisman/jev-eval ≠ SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv ≠ xxkuboxx ≠ onlyoneaman ≠ dayhaysoos/jevals;
default branch claude/laya-jev-review-gg5ppo;
do not reopen or amend PR #23/#24/#25/#26.


## Apply 0541 (`notes.md` §110)

Same pillars, twenty-two HIGH clusters / three themes
(Open-weight / RLCD / Blackwood watch; measurement densifies
PRIMARY for Harbor-jevals; applied/theory class placements across
AI, SWE, business, knowledge work — not SWE-only). Do **not** re-fold
0439 / §109 / 0345 / §108 / 0243 / §107 / 0145 / §106 / 0042 / §105 /
2340 / §104 / 2246 / §103 / 2145 / §102 / 2041 / §101 / 1943 / §100 /
1843 / §99 / 1740 / §98 / 1639 / §96 / gliner-native-runtime / §97 /
1541 / §95 / jev-align *mechanism* / §93 /
jev-orderby-bench *six-gates* / §60 / JevBench v1.2
*board* / §78 / openJev-verdict *claim-audit* / §71 /
yuki-oshio/mini-jev *93.25%* / §103. Fresh PR; never reopen
merged #7–**#27**. do not reopen or amend PR #23 or #24
or #25 or #26 or #27. Skip Archer rewrite (still
**promised_not_landed**; Hub 401). 0★ HIGH still gets a
real card. Size **0** WITH CONTENTS still gets a real card.
Soft Noul ≠ hard safety. Formal methods **compose** with
scoring; a Noul is a SENSOR. Jev is the hot exemplar, not
the whole mandate. Mathematical / logical / algorithmic
mental models across AI, SWE, business, knowledge work —
not SWE-only. Treating 0.85 as 85% / minProbability hard-gate
as Harbor is the anti-pattern.

1. **Blackwood watch densify** —
   Blackwood tracker ABSENT; likes 2 gated manual. Hub HTTP 200;
   sha `3b9e29df`; lastModified UNCHANGED. Do **not** rewrite as
   landed. Census densify only.
2. **Qwen3-0.6B RLCD decision** —
   Reward `r = c - p_a` (Brier identity). ECE 0.021; acc 0.807 vs
   warmup 0.746 *theirs*. Calibration beyond ~500 tokens unmeasured.
   Do **not** treat ECE 0.021 as a hard gate of “honest probabilities.”
3. **Gemma E2B RLCD Independent** —
   Independent primitive. 11.57s vs 54.10s · 4.67× · 120/128 *theirs*.
   Default path is pretrained Gemma probs not trained RLCD head.
   Independent `{cat: 0.9, dog: 0.5}` is valid. Fourth primitive
   beside Choice/Score/Noul — class expansion, not a Jev drop-in.
   Do **not** paste 4.67× as Harbor.
4. **Hub JEV-CPU twin** —
   GH Meanblock 404; lock leesk212/JEV-CPU. softmax over letter slots
   ≠ Noul. Do **not** treat Hub Meanblock as a new species vs leesk212.
5. **Mímir LFM openjev** —
   WANLI 0.741 vs openjev v2 0.77 *theirs*. 3-way NLI ≠ Noul.
   Do **not** hard-gate WANLI 0.741 as “beats openjev.”
6. **System One distilled (Haiku teacher)** —
   priority 0.464 = majority floor. banking77 contaminated. raw
   margins not probabilities. GH jev-haiku-benchmarking 404.
   Do not distill Jev as teacher of record (they distilled Haiku).
7. **System One gold** —
   Gold = dataset labels 4000/task. Teacher-copy vs gold vs zeroshot
   is the class lesson: three supervision regimes, one schema.
8. **System One zeroshot** —
   Zeroshot = base NLI; no extra supervision. Same schema, same floors.
9. **Running-Dolphins/jev-bench** (PRIMARY Harbor-jevals) —
   “0.9 is not one number”. ranking ≠ calibration. banking77 0.8–0.9
   stated 0.86 actual 0.73 over-confident *theirs*. ≠ Praveenrajus/jev-bench
   ≠ fstandhartinger/jevbench. Size **1070**. Do **not**
   treat 0.9 as one number.
10. **WallerChen/jev-measured** (PRIMARY economics) —
    $0.0000153–$0.0000226 vs circulating $0.0004 (~20×). Score is
    0..n-1 expectation not 0–1. Noul has no confidence field. TCP
    floor 198.8 ms. type reliability is not a reason to choose Jev
    (json_schema 5/5). gateway tax not one number. Do **not** treat
    circulating $0.0004 as measured.
11. **RadRebelSam/jev-decision-lab** —
    Function-only 5/8 vs hybrid 8/8; 4/8 without Jev. 8 designed
    cases not conversion lift. ≠ RadRebelSam/awesome-jev. Size **128**
    (was 0 WITH CONTENTS lag). Do **not** treat 8/8 as conversion lift.
12. **jackojacko05 BigQuery pilot** —
    200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0%
    172/200 vs Pro 87.0% 174/200 *theirs*. not a ranking. Size **307**. Do **not** treat a 200-row as a ranking.
13. **openjev fighting ring** —
    NLI Tetris argmax P(entail)−P(contradict). Not Harbor.
14. **joshhu/jevtest 情緒測謊器** —
    情緒測謊器. 1q 396ms / 30q 567ms. ±0.03. 33q $0.000045 vs Gemini
    ~5× slower ~60× cost *theirs*. ≠ realZachi/jevtest. Size **34**.
    Knowledge work / life.
15. **aahf/JevBenchmark Space** —
    8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*.
    synthetic; no inference. ≠ JevBench v1.2 §78. Do **not** treat
    64× Space as Harbor.
16. **rhc98/awesome-jev** —
    Judged 3317 / listed 2560. Jev judges, code applies policy.
    catalog ≠ endorsement. Do **not** treat listed counts as eval.
17. **AiPersonacademy/Awesome-jev-use** —
    Catalog not eval. APA “microsecond policy / zero hallucination”
    overclaim. Catalog ≠ endorsement.
18. **erseco/questionator** —
    Client-side quiz; pointer from held docs; scanned-PDF warn.
    CSP only api.typesafe.ai. Parse/extract exact and local; Jev
    SENSOR on Choice. Knowledge work.
19. **grgy078033/grill-jev** —
    Jev judges / agent reasons / user decides. selecting an option
    is not permission to implement. degraded fallback. User decision
    is the authorization; Jev SENSOR.
20. **makefunstuff/jev-lsp** —
    pattern exact, judgement must clear floor. no matching pattern →
    no model call. not a correctness oracle. $0.00022 vs chat $0.00306
    *theirs*. Regex/pattern is exact; Jev SENSOR on matching lines only.
21. **nozomi-koborinai/jev-spec** —
    Spec vs artifact remainder. **Anti-pattern:** treating 0.85 as 85%
    / minProbability hard-gate as Harbor. Hard-gating minProbability
    0.85 as a CI proof is soundness theater.
22. **202620325-spec/Jev-LLM** —
    VERIFY acquires discriminating evidence, never same-pool
    confidence-only rescoring. fast/full/max are ceilings not sizes.
    Solar writes, Jev chooses NEXT ACTION. Do **not** treat :max as a
    mandatory search size.

Soft Noul ≠ hard safety: 0.807 / 0.021 / 0.9 / 0.86 vs 0.73 /
$0.0000153 / 8/8 / 85.5% / 0.85 / 0.464 are **sensors**. Treating
0.9 as one number, 8/8 as conversion lift, 200-row as ranking,
0.85 as 85%, Score as 0–1, Noul.confidence as existing,
json_schema gap as typed-model win, circulating $0.0004 as
measured, 64× Space as Harbor, WANLI 0.741 as beating openjev,
ECE 0.021 as a hard gate, Independent `{cat,dog}` as Choice,
softmax over letter slots as a Noul, or minProbability 0.85 as
Harbor is the same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul is a SENSOR.
Parse/extract / regex/pattern / VERIFY envelope / user decision /
mdast/root jail / search ceilings are exact work. treating 0.85
as 85% / minProbability hard-gate as Harbor, 0.9 as one number,
and 8/8 as conversion lift are the anti-patterns.

Unique consecutive fragments (this hour):
Blackwood tracker ABSENT; likes 2 gated manual;
r = c - p_a;
ECE 0.021; acc 0.807 vs warmup 0.746;
calibration beyond ~500 tokens unmeasured;
Independent primitive;
11.57s vs 54.10s · 4.67× · 120/128 *theirs*;
default path is pretrained Gemma probs not trained RLCD head;
GH Meanblock 404; lock leesk212/JEV-CPU;
softmax over letter slots ≠ Noul;
WANLI 0.741 vs openjev v2 0.77 *theirs*;
3-way NLI ≠ Noul;
priority 0.464 = majority floor;
banking77 contaminated;
raw margins not probabilities;
GH jev-haiku-benchmarking 404;
do not distill Jev as teacher of record (they distilled Haiku);
“0.9 is not one number”;
ranking ≠ calibration;
banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*;
≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench;
$0.0000153–$0.0000226 vs circulating $0.0004 (~20×);
Score is 0..n-1 expectation not 0–1;
Noul has no confidence field;
TCP floor 198.8 ms;
type reliability is not a reason to choose Jev (json_schema 5/5);
gateway tax not one number;
Function-only 5/8 vs hybrid 8/8;
4/8 without Jev;
8 designed cases not conversion lift;
≠ RadRebelSam/awesome-jev;
200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*;
not a ranking;
NLI Tetris argmax P(entail)−P(contradict);
情緒測謊器;
1q 396ms / 30q 567ms;
±0.03;
33q $0.000045 vs Gemini ~5× slower ~60× cost *theirs*;
≠ realZachi/jevtest;
8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*;
synthetic; no inference;
≠ JevBench v1.2 §78;
Judged 3317 / listed 2560;
Jev judges, code applies policy;
catalog ≠ endorsement;
APA “microsecond policy / zero hallucination” overclaim;
Client-side quiz; pointer from held docs; scanned-PDF warn;
CSP only api.typesafe.ai;
Jev judges / agent reasons / user decides;
selecting an option is not permission to implement;
degraded fallback;
pattern exact, judgement must clear floor;
no matching pattern → no model call;
not a correctness oracle;
$0.00022 vs chat $0.00306 *theirs*;
Spec vs artifact remainder;
treating 0.85 as 85% / minProbability hard-gate as Harbor;
VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring;
fast/full/max are ceilings not sizes;
Solar writes, Jev chooses NEXT ACTION;
SemIf 2186★ (+20 vs §109 2166);
jevlike 1038★ (+7 vs 1031);
TypeAR 14★ flat;
AnotiaWang 96★ (+1 vs 95);
yibie/awesome-jev 490★;
Laya likes 802 (was 783);
tracker likes 64 flat, lastModified UNCHANGED;
do not reopen or amend PR #23/#24/#25/#26/#27.





## Apply 0922 (`notes.md` §117)

Same pillars, user-provided HIGH densify (TheoLeeCJ/SemIf rename +
MLX + accuracy ladder — not a first sighting; AI / SWE / business /
knowledge work, not SWE-only). Do **not** re-fold §78 JevBench 74.6 /
§69 semif-serve / §113 census 2241★ / §114 hourly 2237★ / merged #36
NanoJev §115 / merged #38 jcr §116 as if they were this ladder.
Reconstruct onto main after merged **#34/#35/#36/#38**; never reopen
merged #7–**#36** or **#38**. Do not push onto open **#39** (hygiene)
or **#40** (llm-to-jev §118 / 322–329 / #101). This fold is `notes.md`
§117 / composition **330–336** / batch **#100**. Skip Archer rewrite
(still **promised_not_landed**). Quote *theirs*. Soft Noul ≠ hard
safety. Formal methods **compose** with scoring; a Noul is a SENSOR.
Jev is the hot exemplar, not the whole mandate. Treating 0.813 /
0.845 / 5.21× as Harbor, 18/21 as semantic equivalence, or
softmax-over-options as a Noul is the anti-pattern.

1. **Rename is densify** — SemIf was formerly OpenJev. independent;
   not affiliated with Jev or TypeSafe. homepage openjev.com.
   live REST 2282★ / 140 forks. HEAD ca3ba65f1429.
2. **Interface pattern ≠ replica** — interface pattern reproduction
   with open models; does not reproduce Jev undisclosed model/training.
   wire/agreement ≠ replica of TypeSafe.
3. **Direct logits / MLX** — Direct option logits; 0 output tokens;
   shared-state parallel; MLX backend for Apple Silicon (`--backend mlx`).
   typed output does not guarantee semantic correctness.
4. **Systems comparison ≠ semantic equivalence** — direct 1.023s vs
   AR JSON 5.332s (**5.21×**); argmax agree 18/21. Parallel suffixes
   20.03 dec/s on 777 decisions.
5. **Browser ladder ≠ Harbor; cousins ≠ host** — authored BA 0.813,
   pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883
   (102 across 20 cases). Softmax over options ≠ calibrated Noul.
   JevBench 74.6 is §78 not this ladder. SemIf ≠ kw2828/OpenJev
   playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠
   dddanielliu/semif-serve.

Soft Noul ≠ hard safety: 0.813 / 0.845 / 0.883 / 5.21× / 18/21 are
**sensors**. Treating subset agreement as a replica or 5.21× as
TypeSafe latency is the same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul is a SENSOR.
Option-logit readout / prefix reuse / MLX float roundoff are exact
work. Ranking ≠ calibration theater.

Unique consecutive fragments (this fold):
User-provided 0922 uniqueness lock: SemIf was formerly OpenJev; independent; not affiliated with Jev or TypeSafe; homepage openjev.com; default master; MIT; HEAD ca3ba65f1429; Tolerate float roundoff in MLX evidence verification; pushed 2026-09-19; live REST 2282★ / 140 forks; size 9177; README SHA 74ab7f7f; LICENSE SHA ca562883; interface pattern reproduction with open models; does not reproduce Jev undisclosed model/training; Direct option logits; 0 output tokens; shared-state parallel; MLX backend for Apple Silicon (`--backend mlx`); Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**); argmax agree 18/21; systems comparison ≠ semantic equivalence; Parallel suffixes 20.03 dec/s on 777 decisions; Browser ladder Qwen3.5-4B authored BA 0.813, pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases); Softmax over options ≠ calibrated Noul; typed output does not guarantee semantic correctness; wire/agreement ≠ replica of TypeSafe; SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve; rename is densify not a second census; JevBench 74.6 is §78 not this ladder; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38; do not push onto open #39/#40; notes.md §117

## Apply 0920 jcr (`notes.md` §116)

Same pillars, one productized HIGH (capability-tree
lookup as retrieve-wide → decide → evidence-set;
skills vs capability catalogs; VOI of context
admission; measurement honesty on mixed wall-time)
across AI, SWE, business, knowledge work — not
SWE-only. Do **not** re-fold 0743 / §113 / 0806 /
§112 / 0646 / §111 or cookbook beam §2 as if they
were this product. Fresh PR; never reopen merged
#7–**#33**. do not reopen or amend PR #23 or #24
or #25 or #26 or #27 or #28 or #29 or #30 or #31
or #32 or #33 or #34 or #35 or #36. Do **not** push onto open
#37 (SemIf). Skip Archer rewrite (still
**promised_not_landed**). Soft Noul ≠ hard safety.
Formal methods **compose** with scoring; a Noul
is a SENSOR. Jev is the hot exemplar, not the
whole mandate. Treating 0.6 as a proof, −85% as
Harbor, or returned docs as permission to run is
the anti-pattern.

1. **NiazMorshed2007/jcr** (PRIMARY) —
   NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability.
   Jev Capability Resolver. one tool to find documented deterministic commands in a nested capability tree.
   returns context. **does not execute**.
   skills = workflow+judgment. capabilities = individual operations.
   format independent of Jev. proposed open standard exploration.
   classify (Jev) → optional OpenAI decompose compound → beam search geometric mean of routing probs.
   keep up to 3 paths ≥60% of best (JCR_BAND_RATIO 0.6).
   ambiguity / no-match / depth-limit explicit.
   soft scores ≠ hard gates. 0.6 band is application policy.
   routing ≠ permission. docs ≠ authority to run.
   sol-vs-opus5-20 *theirs*: 20 scenarios × 4 variants = 80 runs.
   lookup+explain only, no execution. n=1 per cell. Not Harbor task-execution.
   Claude Opus 5: agent input 108,585→15,819 (−85%), cost $0.3700→$0.1222 (−67%), wall 105.5s→77.7s.
   Codex GPT-5.6-Sol: 61,952→47,669 (−23%), $0.1377→$0.1151 (−16%), wall 25.3s→62.4s (Sol slower with JCR in 19/20).
   One Sol outlier 372.6s / 193 Jev calls.
   11 groups, 960 nodes, 11,360 items. 16 routing rounds per step.
   **4★**. HEAD `138b3832`. README SHA `2a49dbc1`. site https://jcr.niazmorshed.dev.

Soft Noul ≠ hard safety: 0.6 / −85% / 372.6s are
**sensors**. Treating 0.6 as a fail-closed grant,
−85% as Harbor, or docs as authority to run is
the same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul
is a SENSOR. Catalog audit / beam width / band
ratio / depth budget are exact work. Ranking ≠
calibration theater.


## Apply 0743 (`notes.md` §113)

Same pillars, sixteen HIGH clusters / three themes
(Measurement densifies PRIMARY for Harbor-jevals —
ywchiu routing-across-a-conversation plus Transformers
one-decode sibling, tanay lab scaffold, dataset/Space
densifies; open-weight/RLCD/replicas; skills/DecisionOps
across AI, SWE, business, knowledge work — not SWE-only).
Do **not** re-fold 0646 / §111 / 0541 / §110 / 0439 /
§109 / 0345 / §108 / 0243 / §107 / 0145 / §106 / 0042 /
§105 / 2340 / §104 / 2246 / §103 / 2145 / §102 / 2041 /
§101 / 1943 / §100 / 1843 / §99 / 1740 / §98 / 1639 /
§96 / gliner-native-runtime / §97 / 1541 / §95 /
jev-align *mechanism* / §93 / jev-orderby-bench
*six-gates* / §60 / JevBench v1.2 *board* / §78 /
openJev-verdict *claim-audit* / §71 / jev-judge-bench
SLA-150 *contract* / §71 / yuki-oshio/mini-jev *93.25%*
/ §103 / pngwn RESULTS / §46. Fresh PR; never reopen
merged #7–**#29** / merged **#30**. do not reopen or amend PR #23 or #24
or #25 or #26 or #27 or #28 or #29 or #30. Skip Archer rewrite
(still **promised_not_landed**; Hub 401). 0★ HIGH still
gets a real card. Size **0** WITH CONTENTS still gets a
real card. Soft Noul ≠ hard safety. Formal methods
**compose** with scoring; a Noul is a SENSOR. Jev is
the hot exemplar, not the whole mandate. Mathematical /
logical / algorithmic mental models across AI, SWE,
business, knowledge work — not SWE-only. Treating 77.0%
as Harbor, 0.85 as 85%, TF-IDF ECE as beating Jev,
softmax A/B/C as a Noul, or ACT as a provider proof is
the anti-pattern.

1. **ywchiu/jev_benchmark** (PRIMARY) —
   ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench.
   Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%.
   restriction state 95.0% against 84.4%.
   None of the systems are particularly good at knowing when to stop and ask.
   They skip the question and call a tool directly.
   100% schema pass. six-field joint 48.8% vs 72.8%.
2. **siren2345/jev-single-decode-transformers** —
   siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode.
   Split Transformers experiment from llama.cpp runtime.
   BBQ 9,053/10,000 (90.53%). ECE 0.0890. Mean confidence 0.9943.
   score and noul not implemented. softmax over A/B/C ≠ Noul.
3. **tanayvasishtha/jev-lab** —
   tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab.
   Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling.
   second pass must be $0.00 from cache. The pages never call Jev.
4. **Praveenrajus/jev-bench densify** — 22 configs · 166,054 rows · 4 calibration-gold. sha a39eba3f.
5. **pngwn/open-jev-laya-bench densify** — pngwn/open-jev-laya-bench README 404. sha 9f69c742 likes 2.
6. **jevlogs-log-triage-benchmark** — HDFS 0.9933 (745/750) / retain 0.0084.
   BGL ERROR/FATAL protection 1.0000. 2,479 / 2,500 HDFS uncertain.
   cache hit 0.9648 (2412/2500). $0.153936 estimated. E2 recomputes from saved probabilities.
7. **BunsDev/laya-calibration-lab densify** — Space sha eda59e0a.
   MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133.
   40–48 rows too small to ship T. T never changes argmax.
8. **mini-jev-runs densify** — 27 900 schema-driven decisions.
   13 600 / 13 600 questions. candidate mass min 0.99999624.
9. **Heman10x-NGU/Verdict-open-jev** —
   Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0.
   TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440.
   Verdict-open-jev 48.07% vs Jev 90.80%.
   abstention combined recall 10.00%. p50 35.58 ms.
   K=25 (maximum capacity) 72.00%. 0.85 coverage 84.60% selective risk 1.18%.
10. **Mintzs/jevify densify** — 26.1× faster than standard Qwen JSON generation.
    Jevify 90.0% / 167 ms CUDA graphs disabled. Uncalibrated.
11. **arnabgho/rlcd-lite densify** — Finding 1: Brier on stated confidence alone is a trap.
    grpo_rlcr 0.78 / ECE 0.084. reliability 0.007 but resolution 0.000.
12. **SargeDev/jev-distill-corpus** — Student B MAE 0.148 / Pearson 0.836 / 86.0%.
    do not distill Jev as teacher of record.
13. **altryne/jevify** —
    altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify.
    Find where Jev belongs. Design the questions. Measure the difference.
14. **erayyilmmaz/jev-decisionops** — ACT / REVIEW / FALLBACK.
    A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome.
    confidence is descriptive provider output, not a substitute for probability.
    Quality denominators include only valid scored answers.
    an exact halfway tie chooses the lower level.
15. **aiwithenoch/Jev-Skill** —
    aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills.
    The local path does not claim to turn a smaller checkpoint into Jev.
    Low support becomes decision: "review". MIT-0 SPDX NOASSERTION.
16. **simplosophy/jev-skill** — current-llm. 结构兼容，不是 Jev 模型能力.

Soft Noul ≠ hard safety: 77.0% / 0.85 / 90.53% / 90.0% / 0.0207 / ACT are
**sensors**. Treating 77.0% as Harbor, 0.85 as 85%, TF-IDF ECE as beating
Jev, or ACT as a provider proof is the same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul is a SENSOR.
Contracts / denominators / halfway ties / cache / gold audit / validators
are exact work. Ranking ≠ calibration theater.

Unique consecutive fragments (this hour):
Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113


## Apply 0646 (`notes.md` §111)

Same pillars, twenty HIGH clusters / three themes
(Measurement densifies PRIMARY for Harbor-jevals —
calibration ≠ alpha, compaction 0.5 theater, SGR vs native,
one-decode overconfidence; datasets/Spaces densify the scoring
surface; applied/skills/economics across AI, SWE, business,
knowledge work — not SWE-only). Do **not** re-fold
0541 / §110 / 0439 / §109 / 0345 / §108 / 0243 / §107 / 0145 / §106 / 0042 / §105 /
2340 / §104 / 2246 / §103 / 2145 / §102 / 2041 / §101 / 1943 / §100 /
1843 / §99 / 1740 / §98 / 1639 / §96 / gliner-native-runtime / §97 /
1541 / §95 / jev-align *mechanism* / §93 /
jev-orderby-bench *six-gates* / §60 / JevBench v1.2
*board* / §78 / openJev-verdict *claim-audit* / §71 /
jev-judge-bench SLA-150 *contract* / §71 /
yuki-oshio/mini-jev *93.25%* / §103. Fresh PR; never reopen
merged #7–**#28**. do not reopen or amend PR #23 or #24
or #25 or #26 or #27 or #28. Skip Archer rewrite (still
**promised_not_landed**; Hub 401). 0★ HIGH still gets a
real card. Size **0** WITH CONTENTS still gets a real card.
Soft Noul ≠ hard safety. Formal methods **compose** with
scoring; a Noul is a SENSOR. Jev is the hot exemplar, not
the whole mandate. Mathematical / logical / algorithmic
mental models across AI, SWE, business, knowledge work —
not SWE-only. Treating ECE as alpha, 0.5 compaction as
safety, 0.8 nlgrep as proof, or contract_passed as truth
is the anti-pattern.

1. **alakise/calibration-is-not-alpha** (PRIMARY) —
   Calibration is not alpha. NO CURRENT ALPHA CANDIDATE.
   ΔR² approximately +0.00084. Brier 0.2131387. ECE 0.0421875.
   Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05.
   Do **not** treat ECE as exploitable edge. Business / markets.
2. **OrMizL/jev-compaction-bench** (PRIMARY) —
   default 0.5 keeps zero non pinned. keepResult median 0.14 to 0.17.
   keepCall median 0.28 to 0.35. usable range is about 0.10 to 0.25.
   7.8% to 57.9%. judges results it never sees. task-finish eval not built yet.
   $0.002 per compaction. Hard-gating 0.5 as safety is theater.
3. **slavadubrov/sgr-judge-bench** (PRIMARY) —
   slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench.
   Jev 108/120 $0.083 0.34 s. Luna SGR 114/120.
   paired Jev accuracy-difference intervals include zero.
   not evidence of equivalence. GLM SGR 26/120 93 format failures.
   Terra-planned Jev hybrid 55/120.
4. **elyashium/atlas-replay-lab** —
   rule-based by default, optionally Jev-backed. empty README.
   missing key cannot break the experience.
5. **siren2345/jev-single-decode** —
   prefill plus exactly one decode. softmax over A/B/C ≠ Noul.
   BBQ 9,053/10,000 (90.53%). ECE 0.0890. Mean confidence 0.9943.
   overconfident. score and noul not implemented.
6. **DGUI densify** — DGUI 12 rows (was 6). Schema, not a corpus.
7. **INSTRUCT densify** — INSTRUCT 119 rows likes 2.
8. **pngwn/open-jev Space** —
   encode the state once, decide everything in parallel.
   0.740 accuracy against a 0.508 majority. ECE 0.047.
   fine-tune's advantage ends where its 384-token training data does.
9. **jasonkneen/open-jev** — jasonkneen/open-jev ≠ pngwn/open-jev. same sha d41dc3cd.
10. **IkerMoel Space densify** — packed one-forward Space of §49 GH.
11. **mobarmg Space densify** — peaked ranking ≠ calibration.
12. **jevlogs-triage-explorer** — Space does not call Jev.
    recomputes routing from saved probabilities.
13. **financial recorded lab** — fifty demos; recorded ≠ alpha.
14. **mailordinal densify** — 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22.
    synthetic repository benchmark.
15. **Pleo2/awesome-jev-agent-skills** — Jev evaluations are advisory.
16. **YehuiTang0316/jev-nlgrep** —
    YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep.
    default threshold 0.8 still soft. 40-line windows cannot prove whole function.
17. **dangquan1402/jev-extract** — token-native sequential start/end Choice.
    Gemini/Haiku stubs not configured yet.
18. **jyje/pilot-typesafeai-jev** — handful of hand-written examples, not a benchmark.
    Jev judged exactly what it was given.
19. **laguagu/jev-skills** —
    laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills.
20. **lorensation/llm-cost-optimizer-jev** —
    contract_passed is not a claim of guaranteed factual truth.
    Wilson lower bound 0.85 floor. fixture mode no savings claim.

Soft Noul ≠ hard safety: 0.0421875 / 0.5 / 0.8 / 0.85 / 90.53% / 97.0% are
**sensors**. Treating ECE as alpha, 0.5 compaction as safety, 0.8 as 80%
correctness, Wilson 0.85 as a proof, or contract_passed as truth is the
same theater as jev-gate §79.

Formal methods **compose** with scoring. A Noul is a SENSOR.
Threshold / policy / replay / windows / token spans / Wilson floor /
fees/slippage are exact work. Calibration is not alpha. Ranking ≠
calibration theater.

Unique consecutive fragments (this hour):
Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.


## Apply 0806 (`notes.md` §112)

Same pillars, user-provided HIGH community / mental-model
signal (institutional HF voice — Merve Noyan @mervenoyann).
Do **not** re-fold §85 Akshay / §111 / §110 64× Space /
0541 / §110. Fresh PR; never reopen merged #7–**#29**.
do not reopen or amend PR #23 or #24 or #25 or #26 or
#27 or #28 or #29. Skip Archer rewrite (still
**promised_not_landed**). Quote *theirs*. Do not invent
accuracy numbers. Soft Noul ≠ hard safety. Formal methods
**compose** with scoring; a Noul is a SENSOR. Jev is
exemplar not the mandate. Jev vs GPT-5.6 bakeoffs are a
category error. Treating a ZS softmax as a calibrated
Noul or a hard gate is the anti-pattern.

1. **Category error** — people who compare Jev against GPT-5.6
   has never fine-tuned BERTForXYZ for living and it shows.
   Right lineage = encoder / ZS classifiers (BERTForXYZ →
   DeBERTa → ModernBERT).
2. **Skill-issue thesis** — many problems solved with LLMs
   could have been solved with them, it was a skill issue.
   Mixed architecture, not stack replacement.
3. **opt for DeBERTa and ModernBERT ones** — Hub pointers,
   not a how-to. hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0
   likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0
   likes 72. bart-large-mnli likes 1616 is the widget default,
   **not** Merve’s pick.
4. **multimodal image<>text ZS as perception front-end** —
   perceive, then typed decide. Skip Archer.
5. **softmax/ZS scores still ≠ calibrated Noul** — Hub
   widget 0.504/0.479 *theirs*. soft scores ≠ hard gates.

people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29

Soft Noul ≠ hard safety: 0.504 / 0.479 / likes 421 / 189
are **sensors / engagement**. Treating a ZS softmax as a
Noul or a bakeoff against GPT-5.6 as same-class is theater.


## Apply 0843 (`notes.md` §114)

Same pillars, hourly HIGH measurement / judgment cluster.
Mathematical / logical / algorithmic mental models for
Jev-class categorization/scoring across AI / SWE /
business / knowledge work / life — not SWE-only. Do
**not** re-fold §112 / §111 / §109 tunahan census as a
sibling. Fresh PR off main; never reopen merged #7–**#35**.
do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35.
Do **not** reopen or amend merged #31. Skip Archer rewrite (still
**promised_not_landed**). Quote *theirs*. Soft Noul ≠
hard safety. Formal methods **compose** with scoring; a
Noul is a SENSOR. Calibration does not compose. Ranking ≠
calibration. Measurement theater ≠ a Harbor score.

1. **Hysteresis / policy attached** — A hunch is a probability
   with a policy attached. { enter: 0.8, exit: 0.6 } is hysteresis.
   replay a policy change without inference. Decision models are
   providers, not the product. huncho ≠ Kungie/gut ≠ carldaws/hunch ≠
   tpellet/hunch. Life analogue: do not re-hire / re-page / re-cut
   every time p flaps around 0.7.
2. **Instruct-tuning honesty collapse** — pretrained Qwen2.5 base
   ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269;
   70.9% → 70.0% mean conf 74.1% → 96.7%. temperature scaling still
   matches it in-distribution. No Jev API was called. Qwen2.5 ≠ Archer.
3. **Binning + cost line** — pd.cut bins by equal width while jeval
   bins by quantile; ECE 0.113 and ECE 0.076. jeval drift is not
   implemented yet. Cost-optimal threshold is policy, not a proof.
4. **Calibration does not compose** — ECE has exactly zero statistical
   power to detect the failure mode that kills trajectories.
   Deferred Crispification. TCE / AMS. 25–60× headline withdrawn.
   P(all-correct): 0.0071 vs 0.0001. Qwen 3.8 sparring ≠ Archer.
5. **Catalogs / advisory / screening / ranking theater** —
   g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev
   (same GitHub id 1378007307). 947 repos scored; A 273 · B 302 · C 372;
   LLM rubric ≠ benches. Probabilities are advisory, not calibrated
   guarantees. light_cutoff_applied_to_combination 0. BANKING77
   Accuracy BERT-Base 93.02 Jev 79.90 — BERT figures are published
   supervised references, not zero-shot. AND: product (independence
   assumed and recorded in the trace). circuit-vl-4b ≠ Archer.
   档位措辞效应 分数极差中位 0.50、最大 1.32. 不是 benchmark.

Soft Noul ≠ hard safety: 0.030 / 0.302 / 0.113 / 0.076 / 0.523 /
0.8 / 0.6 / 0.49 / 93.02 / 79.90 are **sensors**. Treating hop-ECE
as a trajectory proof, equal-width as the only ECE, 0.5 cutoff as
100% sensitivity, or Qwen instruct recovery as Archer is theater.
## Apply 0915 (`notes.md` §115)

Same pillars, user-provided HIGH densify (TianyuCodings/NanoJev
unified-games-v1 — open replica / specialist gameplay S1,
not SWE-only). Do **not** re-fold §7 / §72 light NanoJev as
a first sighting. Do **not** re-fold §99 jev-forge / §113 /
§112. Fresh PR; never reopen merged **#31** / **#32** /
**#33** / **#35**. do not reopen or amend PR #31 or
#32 or #33 or #35. Skip Archer rewrite (still
**promised_not_landed**). Quote *theirs*. Do not invent
accuracy numbers. Soft Noul ≠ hard safety. Formal methods
**compose** with scoring; a Noul is a SENSOR. Jev is
exemplar not the mandate. Game success ≠ calibrated Noul.
local type boolean ≠ TypeSafe noul. Treating 128/128 as
Harbor or a normalized bag as a Noul is the anti-pattern.

1. **Open replica / specialist gameplay S1** — A 0.6B
   parallel decision model: states and questions in,
   complete probability distributions out. Zero
   output-token decoding. not TypeSafe Jev.
2. **One model, four games** — ViZDoom Basic 128/128 vs
   Jev 56/128; Predict Position 27/128 vs Jev 11/128;
   Maze 225 attempts vs Jev 2738; Snake 30 food / 256
   steps; held-out Maze 4/10 Snake 8/8 Basic 128/128
   Predict 27/128. Untuned Qwen3-0.6B baseline.
3. **Dataset / mix / hard_lr1e5** — 18,760 questions per
   variant; 16,333 ViZDoom; 896 Predict Position expert
   episodes; mix weights 1/3, 1/3, 1/6, 1/6. Hub
   C-Tianyu/NanoJev revision unified-games-v1 likes 58.
4. **Namesake lock** — caijinchun/nanojev-arena ≠
   liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠
   NanoJev.
5. **boolean ≠ noul / calibration honesty** — local type
   boolean ≠ TypeSafe noul. A normalized distribution
   alone does not establish empirical probability
   calibration. Demo HTTP 401; recordings local. soft
   scores ≠ hard gates.

User-provided 0915 uniqueness lock: TianyuCodings/NanoJev unified-games-v1 densify; A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; 18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58; dataset C-Tianyu/NanoJev-Data likes 5; HEAD 618cea6d906d54e128360786d12f703fff2b1245; 1289★ / 158 forks / size 64035; README SHA 4190093c64ee75b26e9726daa3b00cbcf6d3157a; MIT; caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; not TypeSafe Jev; open replica / specialist gameplay S1; soft scores ≠ hard gates; Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; invented_signal false; do not reopen or amend PR #31/#32/#33/#35; notes.md §115

Soft Noul ≠ hard safety: 128/128 / 4/10 / 8/8 / 27/128
are **gameplay sensors**. Treating them as Harbor or as
calibrated Nouls is theater.


## Apply 0940 (`notes.md` §118)

Same pillars, user-linked HIGH: **migration / question-design
on-ramp**. Mathematical / logical / algorithmic mental models
for Jev-class categorization/scoring across AI / SWE /
business / knowledge work / life — not SWE-only. Fresh PR
off main after merged #35. Do **not** reopen or amend PR
#23–#38. Do **not** push onto open #37/#39. Merged #36 owns §115. Merged #38 owns §116.
Skip Archer rewrite (still **promised_not_landed**). Quote
*theirs*. Soft Noul ≠ hard safety. Formal methods **compose**
with scoring; a heuristic compile is a SENSOR of shape, not
a proof of equivalent behavior.

1. **On-ramp, not a replica** — Turn decision-shaped LLM
   prompts into proposed Jev primitives. Finds where typed
   judgment belongs inside existing LLM prompts. Companion
   to altryne/jevify (find / design / measure) and to the
   Augustus decision-design card. alexwestco/llm-to-jev ≠
   altryne/jevify ≠ Mintzs/jevify.
2. **Soft proposal ≠ production gate** — This is a conversion
   assistant, not an automatic guarantee of equivalent
   behavior. Generated instructions and criteria must be
   reviewed before production use. A falsifying experiment
   is still required.
3. **Partial convertibility** — suitability
   strong/partial/not_a_fit; compatibility full/partial/none.
   Writing new text stays with an LLM. Place only bounded
   decisions; keep generation with the writer.
4. **Category error** — Prompts requiring open-ended prose
   are not a fit. Not every prompt is a Jev candidate.
   Forcing a Choice onto a welcome email is theater.
5. **Heuristic ≠ calibrated Noul** — The compiler uses
   deterministic heuristics, not an LLM or evaluation model.
   Score ranges such as 0 to 1 are translated into ordered
   Jev criteria *theirs*. Review the generated Score rubric;
   Jev scores ordered criteria, not an arbitrary 0-to-1
   range. Soft scores ≠ hard gates.

Soft Noul ≠ hard safety: a proposed Choice/Score/Noul from
this compiler is a **draft**. Treating `full` compatibility
as Harbor, a 0–1 Score as a Noul, or exported SDK as
equivalent behavior is soundness theater.

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

Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; 25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; AND: product (independence assumed and recorded in the trace); chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §114

User-provided 0920 jcr uniqueness lock: NiazMorshed2007/jcr MIT; site https://jcr.niazmorshed.dev; topics ai-agents,jev,mcp; **4★**; HEAD `138b3832`; README SHA `2a49dbc1`; LICENSE SHA `46231303`; size **14850**; Jev Capability Resolver; one tool to find documented deterministic commands in a nested capability tree; returns context; **does not execute**; skills = workflow+judgment; capabilities = individual operations; format independent of Jev; proposed open standard exploration; classify (Jev) → optional OpenAI decompose compound → beam search geometric mean of routing probs; keep up to 3 paths ≥60% of best (JCR_BAND_RATIO 0.6); ambiguity / no-match / depth-limit explicit; soft scores ≠ hard gates; 0.6 band is application policy; routing ≠ permission; docs ≠ authority to run; sol-vs-opus5-20 *theirs*: 20 scenarios × 4 variants = 80 runs; lookup+explain only, no execution; Claude Opus 5: agent input 108,585→15,819 (−85%), cost $0.3700→$0.1222 (−67%), wall 105.5s→77.7s; Codex GPT-5.6-Sol: 61,952→47,669 (−23%), $0.1377→$0.1151 (−16%), wall 25.3s→62.4s (Sol slower with JCR in 19/20); One Sol outlier 372.6s / 193 Jev calls; n=1 per cell; Not Harbor task-execution; Claude/Codex harnesses; compare mode; 50 scenarios bundled; 11 groups, 960 nodes, 11,360 items; 16 routing rounds per step; NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34; notes.md §116
User-provided 0922 uniqueness lock: SemIf was formerly OpenJev; independent; not affiliated with Jev or TypeSafe; homepage openjev.com; default master; MIT; HEAD ca3ba65f1429; Tolerate float roundoff in MLX evidence verification; pushed 2026-09-19; live REST 2282★ / 140 forks; size 9177; README SHA 74ab7f7f; LICENSE SHA ca562883; interface pattern reproduction with open models; does not reproduce Jev undisclosed model/training; Direct option logits; 0 output tokens; shared-state parallel; MLX backend for Apple Silicon (`--backend mlx`); Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**); argmax agree 18/21; systems comparison ≠ semantic equivalence; Parallel suffixes 20.03 dec/s on 777 decisions; Browser ladder Qwen3.5-4B authored BA 0.813, pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases); Softmax over options ≠ calibrated Noul; typed output does not guarantee semantic correctness; wire/agreement ≠ replica of TypeSafe; SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve; rename is densify not a second census; JevBench 74.6 is §78 not this ladder; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38; do not push onto open #39/#40; notes.md §117
User-provided 0940 uniqueness lock: Turn decision-shaped LLM prompts into proposed Jev primitives; This is a conversion assistant, not an automatic guarantee of equivalent behavior; The compiler uses deterministic heuristics, not an LLM or evaluation model; It understands a deliberately small set of common prompt patterns; Generated instructions and criteria must be reviewed before production use; Score ranges such as 0 to 1 are translated into ordered Jev criteria; Prompts requiring open-ended prose are not a fit; suitability strong/partial/not_a_fit; compatibility full/partial/none; Writing new text stays with an LLM; Review the generated Score rubric; Jev scores ordered criteria, not an arbitrary 0-to-1 range; Everything runs locally in the browser; There is no framework, database, account, API, or server-side prompt processing; The key is read from the process environment and is never stored or printed; connect-src 'none'; alexwestco/llm-to-jev ≠ altryne/jevify ≠ ryana/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; HEAD 234058ab372d; README SHA 43cd94fb; LICENSE SHA 5f334006; compiler SHA fdf235d0; 2★; MIT; JavaScript; size 29; Pages https://alexwestco.github.io/llm-to-jev/; invented_signal false; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §118


## Apply 1049 (`notes.md` §120)

Serving substrate ≠ calibrated replica. ggmlc GGUF is not llama.cpp.
Option-order and exact-p games are measurements: pick_by_id vs pick_second.
Adapters / RLCD heads are class members, not TypeSafe drop-ins.
Qwen3.5-9B ≠ Archer. Qwen3.5-4B ≠ Archer.
Soft scores ≠ hard gates. planner writes JEV selects.
catalog ≠ endorsement. Life analogue: shuffle the menu; if dinner
changes, you ranked seats, not dishes. A new bottle does not recertify
the medicine. Negative EV stays negative. Do not copy keys.



## Apply 1143 (`notes.md` §121)

Open recreation ≠ calibrated replica. A cover band is not the studio master.
Semantic lint is a sensor not a proof. cutoff 0.8 still soft.
Third-party benches are *theirs*: paired bootstrap CIs, BANKING77, cascade
parity miss, invented-ticket n=24. Same accuracy, 35x faster is a systems
comparison ≠ semantic equivalence. Local Laya wire-compat is still substrate
≠ replica. permission ≠ confidence. catalog ≠ endorsement.
Qwen3.5-4B ≠ Archer. Do not copy keys.

Hourly 0947 uniqueness lock: Fast and cheap agent evals. jev as judge.; 18,041 skills from the 200 most-starred repos; Not a security scanner; 最简 Jev 调用演示器; confidence 不是正确率; q93304989-bit/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; 75% cheaper and 18% faster withdrawn; jev @0.15 100% recall 87% savings; 33Audits/jev-auto ≠ gargpratyush/jev-router; no Typesafe key, no PI_API_BASE, zero deps; tool-emitted Score/Noul ≠ calibrated Noul; semantic_compatibility: false; candidate_mass; Qwen3.5-2B ≠ Archer; Jev evaluates decisions; it cannot run a coding-agent session; Status: no model yet; S1LV3RJ1NX/openjev ≠ TheoLeeCJ/openjev; 28 accepted decisions; 3 targets; score 800; health 100; arcade game not a flight trainer; A successful live TypeSafe call has not been verified for v0.1.0; abhibansal60/tidy ≠ MANISH007700/tidy; No model, Jev included, predicted which channels its owner keeps; seed 1 selected on a held-out 400-item validation split; Brier 0.342 → 0.378; more accurate and more overconfident; Qwen3.5-4B ≠ Archer; static quants of kushalpatil/jevify-gemma4-26b-a4b; The labels were corrected, and one earlier result was retracted; zero of 23,869 eligible rows; Do not compare cost without checking task success; Exit 1 is not a proof; kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go ≠ official; 38 tests that cannot fail in a 356-model warehouse; if a parser can answer it, Jev is never asked; 359 of them; Games & Simulation 82; Education & Learning 1; Ratings are heuristics; syedabbasshaheer-art/jev-atlas ≠ ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases ≠ walidboulanouar/awesome-jev-use-cases ≠ vamsikrishna2421/jev-usecases; Every headline result above is self-reported; Archer Hume 84.6% MMLU-Pro is a third-party probe not landed Archer; catalog ≠ endorsement; judge ≠ actuator; softmax over A–H ≠ Noul; SemIf 2270★; jevlike 1054★; TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 538★; Laya likes 889; tracker likes 68 lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#35/#36/#37/#38/#40; do not push onto open #39; notes.md §119
Hourly 1049 uniqueness lock: ggmlc GGUF is not llama.cpp; Loading them in llama.cpp will fail; one encoder pass; hf:mys/laya-GGUF sha 713ae6f6e39f likes 0 apache-2.0; hf:mys/laya-multilingual-GGUF sha 3b645ae54281; hf:mys/laya-typed-decisions-GGUF sha 1e9e8ba1f527; hf:tozp/laya-onnx sha 0862aeba1e65 Opset 14 FP32 and INT8; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; docker-laya MIT HEAD 1b8239a51ddd README SHA 9cb7bdc3; laya.cpp RTX ggml CUDA HEAD 8590937c79a2 README SHA cdd429b9; serving substrate ≠ calibrated replica; Softmax over options ≠ calibrated Noul; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; jev-position-test n=6 HEAD 7a56ca1c2698 README SHA 23f194c9; jevmlx slots 5 of 6; hosted Jev 0 of 6; prior_correction made it worse; jevSweeper mean Spearman ρ −0.274; picked exact-optimal 1/25 (4%); 31 of 36 still logically decidable; 86% of the time we should not have been asking; game success ≠ calibrated Noul; LLM2Jev 64★ Apache-2.0 HEAD 924618721277 README SHA da35fe61; not affiliated with or endorsed by Jev or TypeSafe; No answer tokens are generated; OpenSourceJev llama.cpp Qwen3-1.7B HEAD 3c41fba3681d; JEV-MLX Qwen3.5-9B HEAD dec24cd929ea; decision-head-rlcd Qwen3.5-4B 4.9M LoRA; AUTO_ACT is not a Noul; closed-set fail-open stdlib-only; verified=False; soft scores ≠ hard gates; 22 to 40% cheaper *theirs*; first version 70% more expensive; 111-case benchmark *theirs*; CDC 5,000 Jev 72.2% AUC 0.7725 *theirs*; accuracy is a trap; 9.0% base rate always-no 91.0%; catalog ≠ endorsement; jev-skill 109★ 90 scenarios HEAD 4f6e899a24d4; awesome-jev-live 673 entries 4★; minecraft-agent 214★ 131 JEV decisions 35 Astra calls; nether-final-08 8 minutes 43.300 seconds; planner writes JEV selects; RoboJEV structured simulator state not images; ashare-trader 策略未通过自己的回测门槛; 36 组参数全部净期望为负; no positive expectation under real costs; typed_evals NOT an official TypeSafe AI product; jev-as-judge is a sensor; third-person-audit 40% & 60% watermarks still soft; The included experience uses a handwritten demo provider; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42; notes.md §120


**Hourly 1143 HIGH (`notes.md` §121).** open recreation ≠ calibrated replica. semantic lint is a sensor not a proof. cutoff 0.8 still soft. paired bootstrap CIs *theirs*. Same accuracy, 35x faster *theirs*. systems comparison ≠ semantic equivalence. serving substrate ≠ calibrated replica. catalog ≠ endorsement. permission ≠ confidence. Do not reopen or amend PR #23–#43. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1143 uniqueness lock: open recreation ≠ calibrated replica; Qwen3.5-4B ≠ Archer; It is an open re-creation of Jev; less calibrated; perch 164★ MIT HEAD ba775a9940b6 README SHA 7ad0403b; semantic lint is a sensor not a proof; oxlint-plugin-jev cutoff 0.8 still soft; nassim-arifette/jevgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; patdown fuzzy linter; PanAchy/jevvy ≠ Atominac/jevvy; No orders, no advice; SmartMoney-Cub 25★ HEAD d93cf493853d; paired bootstrap CIs *theirs*; emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; +0.82 pts XQuAD-EN 95% CI +0.35 to +1.31; +7.62 pts SciFact CI +4.88 to +10.38; Same accuracy, 35x faster *theirs*; systems comparison ≠ semantic equivalence; BANKING77 500 Jev 81.0% GPT-OSS 82.8% Mercury 73.2% Gemini 85.4% *theirs*; frozen cascade missed its evaluation accuracy target 430/500 vs GPT-5 432/500; This is not demonstrated equal-quality savings; 24 invented tickets; Routing errors caught by the gate 0 of 3; sample too small to establish calibration; This is not TypeSafe Jev; No real API requests were made; wire-compat ≠ replica; KonghaYao/laya-jev 按官方接口写的客户端只改一个 base URL; gqgs/laya-onnx densify 496.8 MiB; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; serving substrate ≠ calibrated replica; BeatAPI/awesome-jev ≠ 99hansling/awesome-jev ≠ Vishnurr2k01/awesome-jev ≠ robokrunch/awesome-jev ≠ rudy2steiner/awesome-jev-hub; All 125 projects; catalog ≠ endorsement; Pasblinn/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab ≠ q93304989-bit/jev-lab; Independent project. Not affiliated with TypeSafe; Kevthetech143/super-jev densify experimental V0.2.0; permission ≠ confidence; allay-team/openjev ≠ piyush-infocusp/openjev ≠ TheoLeeCJ/openjev; 2022 Mineflayer Jevalent collision; kushalpatil/jevify-gemma4-e4b GGUF densify; static quants; This dataset and model are independent research artifacts, not reproductions of Jev or RLCD; pngwn demo accuracy 0.705 ECE 0.046 ~112 ms *theirs*; cutoff 0.8 still soft; soft scores ≠ hard gates; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43; notes.md §121

**Hourly 1248 HIGH (`notes.md` §123).** decide is not generate. tryDecide returns typed calibrated judgments not a token stream. GLiNER/GLiClass ports are class members not Jev replicas. 93.5% *theirs* not Harbor. 74.9 *theirs* not Harbor. 8.7x *theirs* not Harbor. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#45. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1248 uniqueness lock: decide is not generate; tryDecide returns typed calibrated judgments not a token stream; juspay/neurolink 133★ MIT HEAD 268b0fe83130 README SHA e709cadfa6b6 tag v12.19.0; GLiNER/GLiClass ports are class members not Jev replicas; MacPaw/Gliner2Swift ≠ Knowledgator/GLiClass.c ≠ fbilhaut/gliclass-rs ≠ Knowledgator/GLiClass.js ≠ gravitee-io/GLiNER4j ≠ apiplant/gliner-rs ≠ codesoda/gliner2-rs; 8.7x faster 4.4x fewer prompts *theirs*; 153 was a reporting error; corrected 156-case 9.8x faster 4.2x fewer prompts *theirs*; independent v0.2.1 1.24x vs Mini *theirs*; Approvals only; anpicasso/hermes-jev-approvals ≠ hermes-switchyard; scx-router GLiClass ranks candidate LLMs in one non-generative pass; typesafeai-dotnet-sdk Not affiliated with TypeSafe AI; hyperspaceai/jevcache ≠ kushals256/jevcache; ST-jeved measures each reply; 400 plain-text for unaskable question; razorback16/openjev:0.2.1 Docker densify HEAD 794a81b87131; wire-compat ≠ logit-equiv; Option-Marker joint attention 93.5% macro *theirs*; 93.6% micro *theirs*; n=78; T = 1.0367 vs T = 1.1692 two temperatures; guaranteeing is soundness theater; wfzyx/von densify HEAD bed7e7337791; Benchmark Heaven leaderboard #2 74.9 *theirs*; NLL calibration assets; 77.10% still §71 claim-audit; do not re-fold as a beat; Heman10x-NGU/openJev-verdict-2.0 densify HEAD bff28567cff4; kev-family weight tarballs; PLAN_Qwen35 proposal for review; deadline 0.53→0.82 at 9B *theirs*; Qwen3.5-9B ≠ Archer; isolation would fail by construction on DeltaNet; jaredpalmer/kev densify; JevBench v1.2.2 jeff 66.9 (#9) jev 75.3 (#2) *theirs*; logan-markewich/jeff densify HEAD 34b32f99a727; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; TypeLLM/TypeLLM densify HEAD c4b03ba9e792; us/jev-local stub until hf; Eran-BA/Jev_from_GLiNER2 spec ≠ replica; lsu-ub-uu/systemone ≠ TypeSafe System One; Layan/Laya HF spaces name-match; catalog ≠ endorsement; decide ≠ generate ≠ stream; 93.5% *theirs* not Harbor; 74.9 *theirs* not Harbor; 8.7x *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45; notes.md §123

## Apply 1248 (`notes.md` §123)

Decide is not generate. tryDecide returns typed calibrated judgments, not a token stream.
GLiNER locate / GLiClass categorize ports are class members, not Jev replicas.
Third-party benches stay *theirs*: von 93.5% macro n=78, verdict Heaven 74.9,
hermes 8.7x / corrected 9.8x, jeff JevBench 66.9. Wire-compat is still not
logit-equiv. SHA move is not a replica. thinking mode is constrained AR, not a Noul.
Qwen3.5-9B ≠ Archer. Isolation would fail by construction on DeltaNet.
Do not copy keys.

**Hourly 1248 HIGH (`notes.md` §123).** decide is not generate. tryDecide returns typed calibrated judgments not a token stream. GLiNER/GLiClass ports are class members not Jev replicas. 93.5% *theirs* not Harbor. 74.9 *theirs* not Harbor. 8.7x *theirs* not Harbor. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#45. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1248 uniqueness lock: decide is not generate; tryDecide returns typed calibrated judgments not a token stream; juspay/neurolink 133★ MIT HEAD 268b0fe83130 README SHA e709cadfa6b6 tag v12.19.0; GLiNER/GLiClass ports are class members not Jev replicas; MacPaw/Gliner2Swift ≠ Knowledgator/GLiClass.c ≠ fbilhaut/gliclass-rs ≠ Knowledgator/GLiClass.js ≠ gravitee-io/GLiNER4j ≠ apiplant/gliner-rs ≠ codesoda/gliner2-rs; 8.7x faster 4.4x fewer prompts *theirs*; 153 was a reporting error; corrected 156-case 9.8x faster 4.2x fewer prompts *theirs*; independent v0.2.1 1.24x vs Mini *theirs*; Approvals only; anpicasso/hermes-jev-approvals ≠ hermes-switchyard; scx-router GLiClass ranks candidate LLMs in one non-generative pass; typesafeai-dotnet-sdk Not affiliated with TypeSafe AI; hyperspaceai/jevcache ≠ kushals256/jevcache; ST-jeved measures each reply; 400 plain-text for unaskable question; razorback16/openjev:0.2.1 Docker densify HEAD 794a81b87131; wire-compat ≠ logit-equiv; Option-Marker joint attention 93.5% macro *theirs*; 93.6% micro *theirs*; n=78; T = 1.0367 vs T = 1.1692 two temperatures; guaranteeing is soundness theater; wfzyx/von densify HEAD bed7e7337791; Benchmark Heaven leaderboard #2 74.9 *theirs*; NLL calibration assets; 77.10% still §71 claim-audit; do not re-fold as a beat; Heman10x-NGU/openJev-verdict-2.0 densify HEAD bff28567cff4; kev-family weight tarballs; PLAN_Qwen35 proposal for review; deadline 0.53→0.82 at 9B *theirs*; Qwen3.5-9B ≠ Archer; isolation would fail by construction on DeltaNet; jaredpalmer/kev densify; JevBench v1.2.2 jeff 66.9 (#9) jev 75.3 (#2) *theirs*; logan-markewich/jeff densify HEAD 34b32f99a727; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; TypeLLM/TypeLLM densify HEAD c4b03ba9e792; us/jev-local stub until hf; Eran-BA/Jev_from_GLiNER2 spec ≠ replica; lsu-ub-uu/systemone ≠ TypeSafe System One; Layan/Laya HF spaces name-match; catalog ≠ endorsement; decide ≠ generate ≠ stream; 93.5% *theirs* not Harbor; 74.9 *theirs* not Harbor; 8.7x *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45; notes.md §123


## Apply 1746 (`notes.md` §128)

truncated thinking then constrained decode. Constrained AR ≠ calibrated Noul.
0.8B thinking On 0/18 *theirs*. forced closure 20/20 type-valid *theirs*.
type-valid ≠ exact. type safety does not guarantee factual accuracy.
Kev-0.8B completes family. 4B new-source 0.794/0.832 *theirs*.
9B new-source 0.812/0.837 *theirs*. transfer-v9 5%/9%/26% *theirs*.
Qwen3.5 ≠ Archer.
Facts go to code. Judgments go to Jev. Only facts can block. Jev never blocks.
five-lines threshold 0.80 still soft. 155/155 argmax *theirs*.
serving substrate ≠ calibrated replica. SHA move is not a replica. Do not copy keys.

## Apply 1843 (`notes.md` §129)

from-scratch ≠ warm-start. JSONL labels ≠ Harbor.
--init_from warm-start LoRA/head PR #9. Fine-tuning on your own data.
Kev-0.8B 4B 9B Qwen3.5 family. 4B new-source 0.794/0.832 *theirs*.
9B new-source 0.812/0.837 *theirs*. 0.33 vs 0.84 vs 0.83/0.88 *theirs*.
reconstruction ≠ replica. unofficial research implementation with random weights.
assay-001 split verdict. CLINC150 ECE 0.0204 *theirs*.
Banking77 ECE 0.0936 *theirs*. catalog ≠ endorsement.
game success ≠ calibrated Noul. SHA move is not a replica. Do not copy keys.

## Apply 1643 (`notes.md` §127)

restructured vLLM head ≠ logit-equiv. release 0.3.0.
MODEL_VERSION stays openjev-0.1. uv.lock hygiene.
dual serving is not generate. Hosted Codiv ≠ TypeSafe.
typed judgments not opinions. documentation is read not judged.
Models participate. Real tools execute. Thresholds are policy not model.
Jev never generates prose JSX or code. json-render is the only renderer.
game success ≠ calibrated Noul. SHA move is not a replica. Do not copy keys.

## Apply 1542 (`notes.md` §126)

Constrained AR ≠ calibrated Noul. Batch 5.8x *theirs*.
thinking=True/False per-field budget. type safety does not guarantee factual accuracy.
Kev-0.6B 4B 8B family. 4B new-source 0.790/0.806 *theirs*.
8.2% ≥0.9 on wrong *theirs*. option order can change an answer.
Questions share the input text but cannot read each other.
JEV_THRESHOLD 0.65 still soft. routing ≠ permission.
fail closed never auto-allows. fail-open uncertainty means RUN.
classifier ≠ authorizer. estimates not Harbor.
catalog ≠ endorsement. SHA move is not a replica. Do not copy keys.

## Apply 1441 (`notes.md` §125)

dual serving is not generate. Hosted Codiv ≠ TypeSafe.
chat 501 on MLX. vLLM NVIDIA + MLX Apple Silicon.
candidate probabilities are relative not correctness.
37.30s → 2.40s at 64 decisions *theirs*.
Breakout 9 bricks 6 returns 2 lives *theirs*.
recommendation is advisory. the server never blocks on its own.
TypeSafe CLERC 5% to 18% *theirs*.
Probabilities are not calibrated by default. Qwen/Qwen3.8-27B ≠ Archer.
LoRA ≠ RLCD replica. 2B 94.71% 9B 97.54% hard test *theirs*.
2B OOD 86.02% 9B OOD 91.97% *theirs*. 80,816 training rows.
27B still in progress. pass-min 0.8 still soft. JEQ does not own actions.
AndyInQtr/laya-coreai CoreML serving substrate ≠ calibrated replica.
SHA move is not a replica. Do not copy keys.
Since last look 2026-09-21 Open-Jev densify: not merged base models.
customer-service P50 85.03 vs Jev 295.26 *theirs*.
1024/32 slower 1015.90 vs 301.37 *theirs*.
systems latency ≠ semantic equivalence. Open-Jev TREC pending.
hard acc ≠ calibrated Noul. type-valid ≠ exact.
prefix caching experimental/off by default.

## Apply 1340 (`notes.md` §124)

Pydantic response models ≠ logit-equiv. msgspec dropped is not a replica.
The server's output is unchanged and was never wrong.
SchemaError is 400 plain-string detail not 422 list. Error contract is not a Noul.
PLAN_Qwen35 still proposal for review. coverage-at-error-budget *theirs* not Harbor.
GLiNER locate ports are class members not Jev replicas. Locate ≠ decide.
Jev-Vision skip 0.936 / effect 0.967 / done 0.896 / 157 ms stay *theirs*.
~160 ms *theirs* not Harbor. 0.971 F1 *theirs* not Harbor.
hf:fr0stbit3/laya-gguf serving substrate ≠ calibrated replica.
jkcdarunday/SystemOne-Next ≠ TypeSafe System One.
Qwen3.5-9B ≠ Archer. Isolation would fail by construction on DeltaNet.
SHA move is not a replica. Do not copy keys.

**Hourly 1340 HIGH (`notes.md` §124).** typesafe-sdk 0.7 Pydantic response models. msgspec dropped. MLX backend 400 plain-text error contract. Pydantic response models ≠ logit-equiv. msgspec dropped is not a replica. Error contract is not a Noul. PLAN_Qwen35 densify. coverage-at-error-budget *theirs* not Harbor. GLiNER locate ports are class members not Jev replicas. Locate ≠ decide. ~160 ms *theirs* not Harbor. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#46. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1340 uniqueness lock: typesafe-sdk 0.7 Pydantic response models; msgspec dropped; The server's output is unchanged and was never wrong; MLX backend 400 plain-text error contract; SchemaError is 400 plain-string detail not 422 list; razorback16/openjev densify HEAD 6e91dfc031bc README SHA cbdcc8de0304; Pydantic response models ≠ logit-equiv; msgspec dropped is not a replica; Error contract is not a Noul; wire-compat ≠ logit-equiv; PLAN_Qwen35 densify; corrected Qwen3.5 LoRA target names verified; in_proj_qkv in_proj_z in_proj_a in_proj_b out_proj; peft 0.21 existence proof; OOD-calibration study; coverage-at-error-budget metric in Phase 0; PLAN_Qwen35 still proposal for review; deadline 0.53→0.82 at 9B *theirs*; isolation would fail by construction on DeltaNet; Qwen3.5-9B ≠ Archer; jaredpalmer/kev densify HEAD 75cc15ddb8e2 PLAN SHA eca543246f50; GLiNER locate ports are class members not Jev replicas; urchade/GLiNER ≠ fbilhaut/gline-rs ≠ lmoe/gliner-onnx.js ≠ shershah1024/gliner-native-runtime; Locate ≠ decide; Jev-Vision skip 0.936 effect 0.967 done 0.896 157 ms *theirs*; ~160 ms *theirs* not Harbor; 0.971 F1 *theirs* not Harbor; coverage-at-error-budget *theirs* not Harbor; hf:fr0stbit3/laya-gguf serving substrate ≠ calibrated replica; jkcdarunday/SystemOne-Next ≠ TypeSafe System One; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46; notes.md §124

**Hourly 1441 HIGH (`notes.md` §125).** vLLM NVIDIA + MLX Apple Silicon. Codiv hosted free endpoint. dual /v1/systemone + /v1/chat/completions. chat 501 on MLX. dual serving is not generate. Hosted Codiv ≠ TypeSafe. candidate probabilities are relative not correctness. recommendation is advisory. the server never blocks on its own. LoRA ≠ RLCD replica. pass-min 0.8 still soft. 37.30s → 2.40s at 64 decisions *theirs*. 2B 94.71% 9B 97.54% hard test *theirs*. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#47. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1441 uniqueness lock: vLLM NVIDIA + MLX Apple Silicon; Codiv hosted free endpoint; dual /v1/systemone + /v1/chat/completions; razorback16/openjev densify HEAD cddbd962c88a README SHA a5943415cb92; STE README rewrite; serving-port densify; chat 501 on MLX; dual serving is not generate; Hosted Codiv ≠ TypeSafe; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; hr98w/jev-visual 167★ Apple Silicon visual candidate scoring; 37.30s → 2.40s at 64 decisions *theirs*; Breakout 9 bricks 6 returns 2 lives *theirs*; candidate probabilities are relative not correctness; jkudish/jev-mcp 156★ ten MCP tools; recommendation is advisory; the server never blocks on its own; TypeSafe CLERC 5% to 18% *theirs*; jkudish/jev-mcp ≠ burnigtm/jev-mcp; zhengxuyu/litjev off-the-shelf Qwen decision layer; Probabilities are not calibrated by default; Qwen/Qwen3.8-27B ≠ Archer; zhengxuyu/litjev ≠ alexwestco/llm-to-jev; Zefan-Cai/Open-Jev LoRA + scalar head; 2B 94.71% 9B 97.54% hard test *theirs*; 2B OOD 86.02% 9B OOD 91.97% *theirs*; 80,816 training rows; 27B still in progress; LoRA ≠ RLCD replica; Zefan-Cai/Open-Jev ≠ TheoLeeCJ/openjev ≠ razorback16/openjev; cristianoliveira/jeq intelligence you can pipe; pass-min 0.8 still soft; JEQ does not own actions; AndyInQtr/laya-coreai CoreML serving substrate ≠ calibrated replica; AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47; notes.md §125


**Hourly 1542 HIGH (`notes.md` §126).** TypeLLM README densify 3k→12k B. Batch 5.8x *theirs*. Constrained AR ≠ calibrated Noul. kev family densify. 4B new-source 0.790/0.806 *theirs*. 8.2% ≥0.9 on wrong *theirs*. option order can change an answer. fail-closed routing vs fail-open test selection. classifier ≠ authorizer. estimates not Harbor. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#48. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1542 uniqueness lock: TypeLLM/TypeLLM densify HEAD 6a48f9f1e623 README SHA dbdc1f193537; README densify 3k→12k B; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; Batch 5.8x *theirs*; Constrained AR ≠ calibrated Noul; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify HEAD b339f446a0ef README SHA 86b0a19909f3; Kev-0.6B 4B 8B family; 4B new-source 0.790/0.806 *theirs*; 8B new-source 0.796/0.780 *theirs*; Jev hosted 0.857 *theirs*; Questions share the input text but cannot read each other; No Jev outputs were used for training; 8.2% ≥0.9 on wrong *theirs*; option order can change an answer; Qwen3 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; TheoOliveira/pi-jev 21★ fail-closed routing; JEV_THRESHOLD 0.65 still soft; routing ≠ permission; harshwasan/jev-sentinel fail closed never auto-allows; harshwasan/jev-sentinel ≠ leepokai/jev-guard; jackbarunz/jev-tool-router ≠ esinocchi/jev-tool-router; threshold 0.90 still soft; 76/81 vs 77/81 *theirs*; 0.419s vs 2.459s *theirs*; $0.00486 vs $0.03673 *theirs*; does not execute; not a security boundary; baronunread/leanest fail-open uncertainty means RUN; classifier.dev default Jev/Laya pluggable; openlayer-ai/jevals ≠ dayhaysoos/jevals; estimates not Harbor; classifier ≠ authorizer; MrJev/awesome-jev 118 entries catalog ≠ endorsement; MrJev/awesome-jev ≠ yibie/awesome-jev; Koushik890/jev-firewall fail closed ask_below 0.7 still soft; CompleteTech-LLC-AI-Research/jev-codex-approval experimental native not compiled; confidence is not a measured probability; rh-guard owns primary gates; hf:rAVEUK/open-jev-deberta-v3-large encoder class member not Jev replica; hf:p-yan/laya-quanto serving substrate ≠ calibrated replica; hf:Gtrkrsk/laya serving substrate ≠ calibrated replica; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48; notes.md §126
**Hourly 1643 HIGH (`notes.md` §127).** openjev release 0.3.0 densify. re-pin vLLM PR #57250 restructured head. restructured vLLM head ≠ logit-equiv. MODEL_VERSION stays openjev-0.1. dual serving is not generate. Hosted Codiv ≠ TypeSafe. typed judgments not opinions. Thresholds are policy not model. Jev never generates prose JSX or code. game success ≠ calibrated Noul. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#49. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1643 uniqueness lock: razorback16/openjev densify HEAD febf02e88989 README SHA 242a737dba01; release 0.3.0; re-pin vLLM PR #57250 restructured head; VLLM_COMMIT baa8338; pyproject and __init__ agree 0.3.0; MODEL_VERSION stays openjev-0.1; uv.lock hygiene; dual serving is not generate; Hosted Codiv ≠ TypeSafe; restructured vLLM head ≠ logit-equiv; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; frostney/clean-code-review 7★ typed judgments not opinions; documentation is read not judged; Luna writes from Jev findings; morcoan/JMP Joint Model Participation; Models participate. Real tools execute.; Jev routes actions generators supply arguments; not a swarm; zkjoie/jevbus Thresholds are policy not model; Drop < Review < Deliver; FanOut or Exclusive; Kelbie/hunch ≠ carldaws/hunch ≠ tpellet/hunch ≠ huncho; Agent Skills semantic review; SupratikB23/JevCanvas Jev never generates prose JSX or code; Diffusion never decides structure; json-render is the only renderer; skcache/jevtrafficsim Fixed Adaptive Jev; game success ≠ calibrated Noul; Shalimov04/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev; MstyAI/laya-onnx empty repo ≠ tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; SherifAshraf2003/jev-use ≠ shitianfang/jev-use; aniruddh-krovvidi/switchboard ≠ cannacre8ive/switchboard-ai; Visorian/TidyUp ≠ abhibansal60/tidy; isiomaC/jevkit ≠ WaynezProg/jev-kit; lee-lou2/jev-tree ≠ reachjalil/jev-tree; Royhu1/jev-poker-trainer empty repo; JoacoMarc/jev-harness-router ≠ jackbarunz/jev-tool-router; rh-guard owns primary gates; hf:Praveenrajus/jev-bench HTTP 200 was 401; hf:ZefanCai/Open-Jev densify dataset; LoRA ≠ RLCD replica; hf:emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; hf:ctaxnagomi/DGUI_HYPERMEM-JEV densify sha ab3d3529; hf:hugging-apps/open-jev-deberta-v3-large-demo encoder class member not Jev replica; serving substrate ≠ calibrated replica; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49; notes.md §127

**Hourly 1746 HIGH (`notes.md` §128).** TypeLLM truncated thinking densify. 0.8B thinking On 0/18 *theirs*. forced closure 20/20 type-valid *theirs*. Constrained AR ≠ calibrated Noul. Kev-0.8B completes family. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. transfer-v9 5%/9%/26% *theirs*. Facts go to code. Judgments go to Jev. Only facts can block. Jev never blocks. five-lines threshold 0.80 still soft. 155/155 argmax *theirs*. Qwen3.5 ≠ Archer. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#50. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1746 uniqueness lock: TypeLLM/TypeLLM densify HEAD 702e6a287f3c README SHA 08180db0450b; truncated thinking then constrained decode; typellm_runtime.py typellm_sglang.py; evals/qwen35_small; 0.8B thinking On 0/18 *theirs*; forced closure 20/20 type-valid *theirs*; Constrained AR ≠ calibrated Noul; type safety does not guarantee factual accuracy; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify live HEAD 8465c4c4c294 watch 38087aa0301d README SHA 19664b9ae546; Kev-0.8B completes family; Kev-0.8B 4B 9B Qwen3.5; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*; SemIf Kev-9B 0.917 Jev 0.965 *theirs*; scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*; transformers >= 5.17; Qwen3.5 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; notque/vexjoy-agent 421★ /d routes /do fallback; tamaratran/jev-pruner densify HEAD 47d017c34eab; qkal/Canny Facts go to code. Judgments go to Jev. Only facts can block.; Jev never blocks; jqueryscript/awesome-jev 231 entries catalog ≠ endorsement; jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; jamescazzetta/five-lines threshold 0.80 still soft; eugeniughelbur/jev-engineering 371ms $0.0000189 300-call *theirs*; tpellet/jevify ≠ altryne/jevify; seb4ez/jevguard-mcp ≠ seb4ez/jevguard; resumocast/jev-mcp ≠ jkudish/jev-mcp; dtduc-git/jev-table first sighting; Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort; MidasMulli/kev-ane 155/155 argmax *theirs*; MidasMulli/kev-ane ≠ jaredpalmer/kev; serving substrate ≠ calibrated replica; empty repo skip-thin; loktar00/llm-lan-party empty repo; rh-guard owns primary gates; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50; notes.md §128
**Hourly 1843 HIGH (`notes.md` §129).** kev own-data JSONL densify. --init_from warm-start LoRA/head PR #9. from-scratch ≠ warm-start. JSONL labels ≠ Harbor. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. 0.33 vs 0.84 vs 0.83/0.88 *theirs*. reconstruction ≠ replica. assay-001 split verdict. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#51. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1843 uniqueness lock: jaredpalmer/kev densify HEAD bd058057ad0a README SHA 84b872488915; Fine-tuning on your own data; --data JSONL; --init_from warm-start LoRA/head PR #9; Kev-0.8B 4B 9B Qwen3.5 family; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; 0.33 vs 0.84 vs 0.83/0.88 *theirs*; from-scratch ≠ warm-start; JSONL labels ≠ Harbor; Kev-0.5B card Qwen3.5 family pointer; No Jev outputs were used for training; option order can change an answer; 8.2% ≥0.9 on wrong *theirs*; Kev-9B 7.5% ≥0.9 on wrong *theirs*; dabit3/jev-experiments densify 340★; simota/tenbin densify neighbor skill; Promethe-us/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; kyegomez/open-jev reconstruction ≠ replica; unofficial research implementation with random weights; kyegomez/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev ≠ Shalimov04/open-jev; jourdanlabs/assay-001 split verdict; CLINC150 ECE 0.0204 *theirs*; Banking77 ECE 0.0936 *theirs*; 8,576 responses zero type errors *theirs*; brnyxx/jev-ra 3-5x / ~300 ms *theirs*; 8.50× Wikipedia *theirs*; ThePFMind/jev-mcp ≠ jkudish/jev-mcp ≠ burnigtm/jev-mcp; namenu/pi-jev-effort ≠ TheoOliveira/pi-jev; samatv256/mini-Jev ≠ r-ms/mini-jev; comoc/jev-minesweeper ≠ EnesYilmazcode/JevMinesweeper; game success ≠ calibrated Noul; Nutlope/jev-fraud Kimi K3; jeffloo886/jev-notion; hf:akhilaaa3/openjev-v1-allmix-r512-merged ≠ hf:akhilaaa3/openjev-r512-handoff-demo; serving substrate ≠ calibrated replica; catalog ≠ endorsement; SHA move is not a replica; wire-compat ≠ logit-equiv; Qwen3.5 ≠ Archer; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51; notes.md §129


## Apply 1936 (`notes.md` §130)

Same pillars, user-provided HIGH (three aisearchio census gaps plus a
community census pointer; AI / SWE / business / knowledge work, not
SWE-only). Do **not** re-fold §129 1843 / §128 1746 / §77 Benchmark
Heaven / §78 JevBench table / §33 Hub encoder as a second census.
Fresh PR off `d26578f` (merged #52). Never reopen merged #7–**#52**.
Skip Archer rewrite (still **promised_not_landed**). Quote *theirs*.
Soft Noul ≠ hard safety. Formal methods **compose** with scoring; a
Noul is a SENSOR. Treating TypeSafe-compatible as a replica, 76.7% as
Harbor, 0.855 as a hard gate, kotoba as Laya HF, or the 15-link list as
an endorsement is the anti-pattern.

1. **TypeSafe-compatible ≠ TypeSafe replica** — sgoedecke/system-one
   PRIMARY. SystemOne.from_pretrained. Batched single-token choice
   inference. cache_prefix=True. LICENSE absent.
2. **replica ≠ TypeSafe** — mithalouni/system-one-open. 76.7% vs Jev
   86.9% *theirs*. 97 ms H100 *theirs*. 74.8% held-out *theirs*.
3. **Namesake lock vs Laya HF** — kotoba-lang/typed-decisions ≠
   convaiinnovations/laya-typed-decisions. DeBERTa-v3-large 0.855 / 42 ms
   *theirs*. encoder class member not Jev replica. Hub stays §33.
4. **catalog ≠ endorsement** — aisearchio 15-link census. 12 already
   carded 3 gaps this fold.

Soft Noul ≠ hard safety: 76.7% / 86.9% / 0.855 / 42 ms are **sensors**.
SHA move is not a replica. Do not reopen or amend PR #23–#52.

**User-provided 1936 HIGH (`notes.md` §130).** sgoedecke/system-one first-sighting. SystemOne.from_pretrained. TypeSafe-compatible ≠ TypeSafe replica. mithalouni/system-one-open first-sighting. 76.7% vs Jev 86.9% *theirs*. replica ≠ TypeSafe. kotoba-lang/typed-decisions first-sighting. DeBERTa-v3-large 0.855 / 42 ms *theirs*. kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions. aisearchio 15-link census catalog ≠ endorsement. soft scores ≠ hard gates. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided 1936 uniqueness lock: sgoedecke/system-one 20★ HEAD ebde2a2db706 README SHA d331b567e2c3; SystemOne.from_pretrained; Batched single-token choice inference; TypeSafe-compatible; cache_prefix=True; LICENSE absent; sgoedecke/system-one ≠ mithalouni/system-one-open ≠ KathanModh259/system-one ≠ babybear-labs/system-one; TypeSafe-compatible ≠ TypeSafe replica; mithalouni/system-one-open 18★ MIT HEAD 77f1f7cccf8a README SHA 535f33028a68 LICENSE SHA 2f6f2cf1064e; Gemma 4 E2B / Gemma 3 270M Modal; 76.7% vs Jev 86.9% strict common subset *theirs*; 97 ms H100 *theirs*; 74.8% held-out *theirs*; replica ≠ TypeSafe; HF upload pending; kotoba-lang/typed-decisions 1★ Apache-2.0 HEAD 10d7834d3b99 README SHA 4d6bbf4c4e44 LICENSE SHA 513bb5e3cb4c; ModernBERT / DeBERTa / LLaDA-MoE; DeBERTa-v3-large 0.855 / 42 ms *theirs*; ModernBERT-base 0.717 / 68 ms *theirs*; LLaDA-MoE 0.835 / 676 ms *theirs*; kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions; encoder class member not Jev replica; aisearchio 15-link census catalog ≠ endorsement; 12 already carded 3 gaps this fold; soft scores ≠ hard gates; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §130
**Open-Jev densify (`notes.md` §125).** DENSIFY the original 1441 card, not a sibling first sighting. HEAD 4933ee84951f README SHA ce1a587219e4. LoRA + scalar head + calibration temperature. not merged base models. customer-service P50 85.03 vs Jev 295.26 *theirs*. 1024/32 slower 1015.90 vs 301.37 *theirs*. systems latency ≠ semantic equivalence. Open-Jev TREC pending. hard acc ≠ calibrated Noul. type-valid ≠ exact. LoRA ≠ RLCD replica. Qwen/Qwen3.8-27B ≠ Archer. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided Open-Jev densify uniqueness lock: Zefan-Cai/Open-Jev densify HEAD 4933ee84951f README SHA ce1a587219e4; pushed 2026-09-21T01:34Z; Astra TREC commit 1dd56990be7e pushed 2026-09-21T01:17Z; live 3★ (was 0★; star-noise is not the fold); LoRA adapters plus trained scalar decision head and calibration temperature; not merged base models; dataset ZefanCai/Open-Jev rev c67699e13d0a; Open-Jev-2B rev 0c7aa498b162; Open-Jev-9B rev 47e966881e48; 27B still in progress; Independent of TypeSafe; no RLCD/parity claims; LoRA ≠ RLCD replica; customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms *theirs*; 1024 tokens/32 candidates Open-Jev slower 1015.90 vs 301.37 *theirs*; prefix caching experimental/off by default; CUDA prefix caching exceeded tolerance on 9/11 workloads; systems latency ≠ semantic equivalence; GPT Luna P50 918.13 ms Astra 1938.39 ms *theirs*; TREC-DL Jev/Luna/Astra completed; Open-Jev TREC pending; 80,816 training rows; 2B 94.71% / OOD 86.02%; 9B 97.54% / 91.97% *theirs* not Harbor; hard acc ≠ calibrated Noul; type-valid ≠ exact; Qwen/Qwen3.8-27B ≠ Archer; website https://zefan-cai.github.io/open-jev/; launch X thread https://x.com/Zefan_Cai/status/2101782158658695388 https://x.com/Zefan_Cai/status/2101786019607740436 https://x.com/Zefan_Cai/status/2101789698947793231; densify §125 not a sibling first sighting; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §125
