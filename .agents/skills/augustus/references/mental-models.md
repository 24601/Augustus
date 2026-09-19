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
| Application control flow | `if` / `case` on a judgment | `chance`/`pick`/`rate` as language primitives (**Empirical**: hunch; English-as-config) | Fail polarity per action; stub backend |
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
| schema-safe ≠ correct | can it still be wrong? | Cannot invent out of schema; can pick the wrong valid option (**Empirical as article**: Akshay; safer *theirs*: schema holds, judgment can fail) | Cousin of type-safe ≠ correct / jaggedness |
| Questions-as-code / shadow rollout | may this branch go live? | Rubric first; shadow beside current; plot accuracy vs confidence; pin questions (**Empirical as article**: Akshay) | Do not rebuild the agent first. 200×/400× are TypeSafe ceiling |
| Sentence-as-rule | does this named artifact contradict itself | Structural matcher × one sentence scored (**Empirical**: mizchi/jevlint 13/15 1.00/1.00 *theirs*) | Mechanical defects stay with the compiler; qualify vs huntedman/JevLint |
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
| Dual-channel ECE / claim-audit | is this NAR "better calibrated"? | Like-for-like channels; n and CI before SOTA (**Hypothesis until independent run**; openJev-verdict-2.0 + PR #1) | Throughput ≠ latency; correctness-head ≠ distribution ECE; ≠ IamBusy/OpenJev |
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
