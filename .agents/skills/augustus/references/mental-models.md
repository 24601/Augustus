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
| Org / safety (Leveson) | Sensor ≠ constraint | This file §Leveson; `formal-methods.md` |
| Crossover metaphors | NATM, snap-fit, Norman as *intuition* | This file §crossover |
| Formal / semi-formal | Proof vs DST vs judgment | `formal-methods.md` |
| Class / family / objective | Decision API vs ranker vs vision | `judgment-class.md` |

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
parallel Nouls into a joint.

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

## Calibration and cost-sensitive thresholds

A number you can threshold is a *decision* number only after you check
that it means P(event) on **your** population. In-distribution ECE can
look excellent and collapse OOD (Archer Hume — `notes.md` §7). Open
heads transfer this duty to you (`notes.md` §18).

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
Mapping card: `mappings.md` §6.

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
now default.

Control: hysteresis, continue / stop / retry / verify (foreman shape).
The model estimates named probabilities; the controller is a table with
memory. Estimate ≠ measure — irreversible milestones concede only to a
probe.

| Domain | Search/control loop | Judgment hole | Exact / probe |
|---|---|---|---|
| SWE | MCTS over moves | prune / prior / value | simulator |
| Knowledge work | snowball citations | "is this still on-question?" | you already have the PDF |
| Business | sales stages | "is this still a real opp?" | amount, close date in CRM |
| Life | cook / rest / check | "does this look done?" | thermometer (probe) |
| Org | incident command | "is this still contained?" | head-count, location |

Rejected: bandits without observed rewards; Jev as the planner that
picks its next tool in a loop (`boundary-audit.md`); PufferLib Ocean
scores as a capability claim (`formal-methods.md` DST trio). Mapping
card for the cross-domain loop: `mappings.md` §9.

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

```text
NATM      instrument often; adapt the support you actually control
snap-fit  designed slop only where a miss is reversible
Norman    evaluate candidates; force the irreversible acts
Leveson   sense with judgment; constrain with policy
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
| Moderation | hold before publish | hazard Nouls (**Empirical** as family) | block/review policy |
| Phishing / fraud screen | hold vs deliver | SDT criterion on a Noul | blocklist, SPF/DKIM exact (**Hypothesis**) |
| Personal ops | cook done / not | "looks done" Noul | thermometer probe |
| Org safety | stop the line | sensor Noul | interlock, two-person rule |

Rejected in every domain: replacing the ledger with a vibe; replacing
the interlock with confidence; replacing the essay with a Noul;
TOCTOU-of-Noul as authorize; tautological spec + "looks good."

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

Related: `mappings.md`, `methods-catalog.md`, `toolbox-mapping.md`,
`composition-algebra.md`, `formal-methods.md`, `faq.md`.
