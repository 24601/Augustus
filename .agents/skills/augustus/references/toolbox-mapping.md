# The toolbox sweep: how to find approaches and applications for a new primitive

Jev is out-of-distribution: no cookbook for most of its uses exists yet, and
prompting an LLM to "be creative with the docs" produces shallow rehashes of
the launch demos. This card is the *meta-method* — the repeatable procedure
for deriving new mappings and applications from tools you already know.
It is methodology-grade (hypothesis): each produced mapping still earns its
status individually (Contract / Empirical recipe / Hypothesis, per
mappings.md).

## Why toolbox substitution instead of brainstorming

A "be creative with the docs" prompt fails the same way for humans and
models: the concept is new, meaning hasn't been built. But every
practitioner owns a deep toolbox of methods that ARE in distribution —
statistics, decision theory, discrete math, operations research, signal
detection, psychology, game theory, logic, safety engineering. Software
is one place those methods live, not the only one (`mental-models.md`).
Jev's three primitives (a calibrated probability for a proposition; a
distribution over a fixed option set; an expectation over an ordered
rubric; all evaluated in parallel over one state) are narrow, so the
productive question is the inverse of "what can Jev do": **"which
component of a method I already trust is exactly a fast semantic
judgment over a fixed answer space, given a state?"** Swap that
component; keep the rest of the method in code.

## The sweep procedure

1. **Pin the primitive facts you're mapping TO** (verify live each pass):
   calibrated P(proposition) with no separate confidence (Noul); winner +
   full distribution + confidence, 1–255 options (Choice); probability-
   weighted expectation over 2–10 levels (Score); every question in one
   request sees the same state and is judged independently; ~70–500ms,
   ~$0.0004/case, output tokens free; 64k combined envelope; no generation,
   no arithmetic, no date math, calibration only in-distribution.
2. **Inventory a toolbox family** — one at a time: statistics, decision
   theory, signal processing, operations research, discrete math, game
   theory, experimental design, physics/measurement, psychometrics,
   behavioral economics. For each family, list its canonical components.
3. **Test each component for a judgment-shaped hole**: a step that (a) a
   knowledgeable person answers in ~a second given the right context, (b)
   has a closed answer space, (c) doesn't require derivation, counting, or
   arithmetic. That hole is substitutable with a Jev call; everything else
   stays deterministic.
4. **Classify the substitution** before writing code:
   - *Direct substitute* — the method was feasible but clunky (LLM judge,
     hand-tuned rule, manual review). Marginal win.
   - *Newly feasible* — the method was KNOWN but economically impossible:
     100–150× cost/latency per judgment is the unlock. These are the
     high-yield applications (MCTS value estimation, per-artifact context
     sieving, per-claim citation checks, 10 Hz-ish game judgment).
   - *Invalid* — violates a boundary (see below). Record it as a rejection,
     not a failure to imagine.
5. **Check the named-methods catalog** (`references/methods-catalog.md`)
   for prior art on the specific operator/theorem/algorithm before assuming
   the mapping is new — including the operators-and-theorems tier with its
   precondition rule (no named precondition = metaphor, not mapping).
6. **Compose and falsify**: build the decision card, define the falsifying
   experiment (mappings.md format), test on labeled data.

## Substitution patterns per family (seeded from launch-week evidence)

| Family | Component → Jev shape | Status |
|---|---|---|
| Statistics: ensemble/ variance reduction | Self-consistency: repeat the same judgment N times over one state; use entropy/disagreement across repeats as a review signal (cheap because output tokens are free) | **Empirical recipe** (self-consistency cookbooks, jev-1.13.0) |
| Statistics: judge variance | Repeated judgments over frozen outputs to qualify ANY judge before its numbers are trusted; Jev judge spread 224–279× lower than a GPT judge | **Empirical recipe** (jev-as-a-judge) |
| Decision theory: Neyman–Pearson | One threshold per action scaled to error cost; abstention path | **Contract + empirical** (confidence-routing; pi-jev thresholds) |
| Statistics: point estimation | Score expectation as an estimate — but read the full distribution beside it ([0,1,0] vs [.5,0,.5] both = 1.0) | **Contract** |
| Probabilistic method: priors | Choice distribution as P(s,a) policy prior (MCTS/PUCT); Choice confidences as calibrated gating | **Empirical recipe** (jev-mcts, calibrated vs exact truth) |
| Search: value function | Score rubric as leaf value V(s) — only where a simulator validates outcomes; speculative depth hard-capped at 2 | **Empirical recipe** (jev-mcts fidelity split) |
| Measurement theory: probe vs estimate | Only post-execution probes concede milestones; model estimates never do — "estimation wearing a measurement costume" is the rejection template | **Empirical recipe** (jev-mcts, pi-warden done-check) |
| Experimental design: perturbation | Behavioral tests as the stats layer: candidate removal, option-order shuffle, distractor injection, boundary cases | **Contract-level** (validation.md) |
| Discrete math: width vs depth | Fan out in width (parallel ≈ free), pay depth linearly; two-stage only when next options depend on an earlier answer | **Empirical recipe** (fan-out: 12.2× cheaper, 10× faster) |
| Psychology: Kahneman | System 2 generates/proposes (LLM), System 1 discriminates (Jev); never the reverse | **Empirical recipe** (mcts-agent role split; 2026-09-18 mixed-architecture discourse) |
| IR / cascades | Cheap relevance / irrelevance before an expensive ranker or generator | **Empirical recipe** (RAG cookbook; jevprune; git-jev-stage; LlamaIndex Jev rerank) |
| Spec / lint | Project-defined semantic rules as predicates over a diff | **Empirical recipe** (jev-pref contract; pi-warden; snifftest unsure-band) |
| Formal methods / DST / safety | Judgment triages counterexamples, failing seeds, and named-rule conformance; proof/MC/DST stay with their tools. Noul is a sensor, not a discharged PO | **Hypothesis as product**, **Empirical** as ownership (pi-warden; `formal-methods.md`) |
| Bandits / RL | Value from observed rewards only — Jev provides none; rejected without an environment | **Rejected** (standing boundary) |

Invalid-but-tempting (record these so they don't get rediscovered): treating
parallel Noul answers as independent evidence and multiplying them into a
joint probability (they share the state); Jev as p-value (Noul is a belief,
not a test statistic); cross-question Score comparability without a shared,
versioned rubric; using calibration to certify an individual answer
(calibration describes groups, not cases); treating Jev as a stack
replacement for an LLM (mixed architecture is the default —
`references/mixed-architecture.md`); treating a Noul as a proof, a
model-check, or a DST property (`references/formal-methods.md`).

## The application-finding procedure (top-down, domain-first)

1. **Enumerate decision points** in the workflow: every place a human would
   glance and answer in a second, or where a boolean/enum/rank sits in code
   behind hand-tuned rules, regexes, or "we check it manually."
2. **Apply the economics inversion**: for each, ask "what method would I use
   if this judgment cost ~$0.0004 and ~100ms instead of seconds and cents?"
   The answers you'd previously discard as too expensive (per-block context
   judgments, per-claim citation checks, per-candidate gates) are the
   applications — that is the rethink, not re-running old prompts cheaper.
3. **Classify each decision point**: exact → code; semantic judgment → Jev;
   generation → LLM (after Jev routes/filters/verifies); irreversible or
   uncertain → human. Assign per-action thresholds from error costs.
4. **Shape the state**: one request's questions must be answerable from the
   state as given — filter to what each judgment needs (context rot is
   measured), keep arithmetic/dates in code, name state paths explicitly.
5. **Falsify**: held-out labels, thresholds selected on split A reported on
   split B, judge-variance check if a Jev judge is part of the loop, and the
   behavioral perturbation tests. A use-case passes when its falsifying
   experiment fails to reject it.

## The second generator: the composition algebra
(`references/composition-algebra.md`) crosses positions (operand, gate,
post-judge, selector, comparator, prior, estimator/controller, metric,
verifier, discretizer, terminator) × known constructs — each cell checkable
against a governing rule, filtered by the economics inversion, falsified
before promotion. Use it with the sweep: the sweep asks "is there a
judgment-shaped hole?"; the algebra asks "where could one sit?"

## Escalation for very new problem shapes

When the shape doesn't match any worked mapping (e.g. a 10k-candidate
decomposition, a streaming judgment problem), don't prompt for creativity —
escalate to the closest *classical* method (search, screening, cascades,
importance sampling) and redo step 3 of the sweep on it. The library of
mappings grows one falsified card at a time; a card enters mappings.md only
with an acceptance test that ran.
