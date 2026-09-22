# Composition foundations — independent Astra review, 2026-09-22

## Verdict and scope

**Fix-first for the strong claim of an outcome-grounded composition engine.**
The inspected Augustus is a coherent placement/design scaffold, not merely a
vendor survey, but its placement taxonomy does not yet establish that compatible
looking parts compose correctly or improve outcomes. The proposed laws can form
a small useful calculus if each join carries assumptions and a falsifier. They
cannot certify those assumptions, learn a valid loss function, identify missing
counterfactuals, or demonstrate an unrun outcome improvement.

The smallest useful change is a typed decision graph plus seam checks, branch
accounting, and a paired end-to-end rejection experiment—not a grand theory or
a longer catalog. The coordinator owns implementation and acceptance.

Read current `AGENTS.md`, `CONTRIBUTING.md`, `research/protocol.md`, its fold
prompt, complete `.agents/skills/augustus/SKILL.md`, `composition-algebra.md`,
and `mental-models.md`. Initial observed skill version was `0.6.1`, HEAD
`192faf0d18d511154228af8ac40e1393567d828c`; the shared tree is changing.
Only this research report is written by this task. Requested model/effort:
`gpt-6-astra/xhigh`; actual serving route, build, and usage remain unobservable
to this worker. No delegates, paid calls, third-party execution, or Git mutation.

## Recommended law set

### C1. Type the claim, not merely its JSON representation

Recommended contract, a **design discipline**, not a statistical theorem:

```text
quantity kind and support/event:
conditioning evidence, target population and selection policy:
observation time, prediction horizon and deployment regime:
units/utility scale, candidate identities and coverage:
model/rubric/adapter/calibration/policy versions:
assumptions, evidence status, qualification data and uncertainty:
outcome source, observation mechanism, missingness/censoring:
consumer preconditions, permitted effects and fallback owner:
```

Name `P(Y=1 | evidence, population, regime)` differently from a rank score,
ordinal grade, realized measurement, or `P(Y(a)=1)`. Compatibility requires
the consumer's assumptions, not just matching field names. A type checker can
reject missing or contradictory declarations; it cannot establish truth or
calibration from declarations supplied by the same caller.

**Naive-transfer counterexample:** a 30-day purchase probability among contacted
leads is used as 24-hour intervention uplift for all leads. Event, time, selection,
and causal estimand have changed. **Executable falsifier:** mutate one contract
dimension at a time; the join must reject it or require an explicit, independently
qualified adapter. Separately corrupt plausible outcome labels: structural
validation should still pass, demonstrating why semantic qualification remains.

### C2. Account for complete branches by total expectation

For a finite/countable mutually exclusive, exhaustive branch partition `B`,
an integrable loss `L`, and one fixed deployed policy/regime:

```text
E[L] = sum_b P(B=b) E[L | B=b]
```

No independence is needed. Zero-probability branches contribute zero; their
conditional means are not identified by observations. Branch losses must use
the same units and include fallback, human delay, missed opportunities, and
shared overhead exactly once. Use complete terminal paths when stages overlap.
If workload changes review queues, branch costs must reflect that workload.

**Counterexample:** averaging a 90%-traffic branch loss 1 and a 10%-traffic
branch loss 10 gives 5.5 instead of 1.9. Summing losses for overlapping events
can double count. **Executable falsifier:** grouped row-level weighted losses
must equal the ungrouped mean; reject a branch table whose mass is not one.
This identity on observed data does not identify risk for a different policy
with different unobserved counterfactual outcomes.

### C3. Cascade coverage is conditional composition

For upstream acceptance `G` and downstream acceptance `H` on the same population,
with `P(G)>0`:

```text
P(G and H) = P(G) P(H | G)
selective risk = E[L | G and H]
```

With `P(G)=0`, joint coverage is zero and downstream conditional qualification
is undefined, not perfect. General chains condition each stage on all earlier
acceptances. A downstream model's global calibration, coverage, or conformal
guarantee does not automatically apply after selection; establish the selected
population's relevant property, or a theorem whose conditioning covers it.

**Counterexample:** `G=H` with probability `.5` gives `.5`, not the marginal
product `.25`. A globally calibrated score `.5` can have positive rate 1 in a
selected subgroup and 0 in its complement. **Executable falsifier:** use joint
rows for both examples; selected denominators, accepted-case errors, and no-case
states must be reported. See [selective CRC §4.4](https://arxiv.org/pdf/2512.12844v2):
its practical threshold refinement is explicitly outside its main theorem.

### C4. Union budgets do not require independence, but do require containment

For a finite set of events on a common experiment:

```text
P(union_i F_i) <= min(1, sum_i P(F_i))
```

To bound system failure, justify `F_system` being contained in that union.
Missing common-cause failures invalidate the system argument, not the union
bound. Correlation can make the bound loose; independence is unnecessary.
A conditional-on-reach stage bound is multiplied by its reach probability,
or conservatively uses reach probability at most one. Adaptive reuse still
needs a valid bound for the resulting selection/history, not yesterday's
qualification. Fix the exposure horizon; a per-action budget is not an
indefinite-lifetime budget.

Keep operational failure budgets `epsilon_i` separate from statistical
confidence-error budgets `delta_i`. Simultaneous upper bounds require their
own valid joint statement; a union of individual confidence failures gives
at most `sum(delta_i)`, not an operational-risk estimate.

**Executable falsifiers:** identical events of mass `.1` have union `.1`,
not independence value `.19`; disjoint events of mass `.1` have union `.2`.
Add an unlisted failure and show that the old system guarantee no longer
follows. Fail a purported lifetime certificate that simply reuses one daily
bound forever.

### C5. Bounded-loss plug-in regret is controlled by distribution error

Let `p,q` be distributions on the same finite outcome space; use the same
finite nonempty feasible action set and loss table with `0 <= L(a,y) <= Lmax`.
Let `a_p` minimize expected loss under `p` and `a_q` under `q`. Then:

```text
TV(p,q) = .5 sum_y |p_y-q_y|
E_p L(a_q,Y) - E_p L(a_p,Y) <= 2 Lmax TV(p,q)
```

Proof: for every action, `|E_p L-E_q L| <= Lmax TV`; add and subtract both
`q` risks and use `q`-optimality for the middle term. An `eta`-suboptimal
`q` optimizer adds `eta`. At each context the same bound holds for its true
and estimated conditional outcome laws; averaging gives a bound using mean
conditional TV. Hard feasibility and authorization are not granted by this
loss bound. Unbounded loss, different feasible actions, or a wrong causal
outcome law falls outside it.

**Sharpness fixture:** binary zero-one loss, `p=(.6,.4)`, `q=(.5,.5)`, with
the `q` tie broken toward class 1: regret `.2`, TV `.1`, bound `.2`.
**Executable falsifier:** enumerate finite distributions, bounded loss
matrices, and tie rules; verify the inequality and include this equality case.
Then deliberately use an out-of-range loss or different action set and reject
the invocation. Do not claim ECE, a provider confidence statistic, or agreement
between two models supplies a bound on TV to the true conditional law.
This is a proven sensitivity law, not a measured deployment guarantee.

### C6. Free information cannot hurt an optimal feasible policy

For one decision maker, a common joint probability model, fixed loss/feasible
acts, and policies allowed to ignore an additional observation `Z`:

```text
inf_policy_using(E,Z) E[L] <= inf_policy_using(E) E[L]
```

This follows by policy-set inclusion. Gross value may be zero, not strictly
positive. Buying the observation can have negative net value after latency,
money, privacy, human load, cognitive limits, or state-changing side effects.
If acquiring it changes the game or feasible acts, compare the full systems.
Blackwell domination formalizes universal decision value when a less
informative experiment can be generated by garbling a more informative one.
It does not order arbitrary models from accuracy, entropy, or one benchmark.

**Important substitution limit:** isolated experiment order need not survive
arbitrary background information. Let `Y,C` be independent fair bits,
`A=C`, and `B=Y xor C`. Both A and B alone reveal nothing about Y. Given
background C, A adds nothing but B identifies Y. [Brooks–Frankel–Kamenica,
March 2024, §§1–3](https://benjaminbrooks.net/downloads/bfk_comparisons.pdf)
studies precisely the distinction between isolated experiments and joint
signals. Our four-row XOR fixture makes the seam testable. An optimal policy
with genuinely additional information may ignore it; replacing a component
is a different operation.

**Executable falsifiers:** enumerate Bayes loss with no signal, a free perfect
signal, and an irrelevant signal; require nonincrease, with equality allowed.
Add acquisition cost exceeding gross value and require rejection of purchase.
Evaluate the XOR fixture with background C, not just each signal in isolation.

### C7. Data processing must include learned parameters and other inputs

For finite random variables, suppose output `Z` is generated from `(X,Theta)`
by a channel with no additional information about `Y`, i.e.
`Y` is conditionally independent of `Z` given `(X,Theta)`. Then:

```text
I(Y;Z | Theta) <= I(Y;X | Theta)
I(Y;Z) <= I(Y;X,Theta)
```

The first statement follows from the mutual-information chain rule:
`I(Y;X,Z|Theta) = I(Y;X|Theta)` and also equals
`I(Y;Z|Theta)+I(Y;X|Z,Theta)`. The second is ordinary data processing.
Model parameters, training-derived state, retrieval, tool results, memory,
and informative randomness belong in the input set; do not hide them.
Do not assert `I(Y;Z)<=I(Y;X)` for a model that also uses informative Theta.
The channel/TV definitions are given by [Polyanskiy–Wu v4, §1](https://arxiv.org/pdf/1508.06025v4).

**Counterexample:** a training sample reveals a stable fair-bit world parameter
`Theta=Y`; runtime X is constant and `Z=Theta`. Then `I(Y;X)=0` and
`I(Y;Z)=1` bit. This need not involve runtime observation or leakage: the
training-derived parameter is simply an omitted information source. The
conditional inequality becomes `0<=0` and remains valid.

**Executable falsifier:** enumerate this joint table and a genuine Markov
channel, computing both unconditional and conditional mutual information.
Redacting X while output remains accurate does not alone establish that the
model is invalid; it may expose reliance on prior/training knowledge. Check
whether that knowledge is allowed and sufficiently current for the task.
DPI limits information, not the usefulness of computation to a bounded solver;
processing the same evidence can make a better decision computationally feasible.

### C8. Close the contract around the trajectory

For a fixed finite horizon, evaluate the policy-induced trajectory law and
declared cumulative/terminal loss, including actions, delays, fallbacks,
observation processes, constraints, and authorized effects. A one-stage
score law is not a stability, termination, or safety theorem. A monitor after
an irreversible effect detects; it does not prevent.

[Performative Prediction, ICML 2020, definitions 2.1/2.3 and §3](https://proceedings.mlr.press/v119/perdomo20a/perdomo20a.pdf)
distinguishes risk under the distribution a policy induces from risk on a
fixed historical distribution, and stable retraining from optimality. Its
convergence theorem needs smoothness, strong convexity, and sufficiently small
distributional sensitivity; do not transfer it to an arbitrary agent loop.

A timely concrete example is [Drift-Aware LLM Routing v1, September 1, §§3–5](https://arxiv.org/pdf/2609.00662v1):
its controller combines learned estimates with a separate pre-commit resource
meter, explicit feedback assumptions, and a restricted comparator. Audit costs
are not included in the displayed routing budget. This reinforces a complete
contract; it is not independent evidence that the proposed controller wins.

**Executable falsifiers:** two controllers with the same one-step score
accuracy must remain distinguishable by stale-state violations, queue overload,
chattering, unrecovered failure, terminal-outcome loss, and forbidden effects.
A deterministic fixture `Y_next=1-current_prediction`, starting from binary
prediction 0, makes naive retraining alternate; perfect fit to yesterday's
outcome does not establish convergence.

## Sources and inspection limits

Primary-source web inspection occurred on 2026-09-22; the web tool does not
provide a per-response UTC capture receipt. No cited empirical result was
reproduced. The formulas above were independently derived; the proposed
executable falsifiers are specifications, not claims of tests run by this
worker. The coordinator is implementing independent deterministic checks.

| Source/revision | Inspection and status |
|---|---|
| [Polyanskiy–Wu, arXiv:1508.06025v4](https://arxiv.org/pdf/1508.06025v4), July 28, 2016 | §1 channel, total-variation, mutual-information definitions and Markov interpretation. Theory; no stronger channel-specific contraction asserted here. |
| [Brooks–Frankel–Kamenica, Comparisons of Signals](https://benjaminbrooks.net/downloads/bfk_comparisons.pdf), author PDF marked March 2024 | Introduction, definitions, §3 and relevant theorem statements; not full proof audit. Theory supporting the side-information distinction. First sighting in this bounded review; no existing source-registry entry found. |
| [Perdomo et al., PMLR 119, 2020](https://proceedings.mlr.press/v119/perdomo20a/perdomo20a.pdf) | Definitions 2.1/2.3, example 3.4, assumptions/theorem 3.5. Theory under a modeled distribution map, not arbitrary feedback stability. |
| [Selective CRC, 2512.12844v2](https://arxiv.org/pdf/2512.12844v2), April 2026 revision | Theorem 2 and §4.4 inspected in the preceding independent theory redo; retained here only for its explicit adaptive-threshold caveat. No implementation reproduced. |
| [Drift-Aware LLM Routing, 2609.00662v1](https://arxiv.org/pdf/2609.00662v1), September 1, 2026 | Fresh §3 model/audits and §4 meter plus theorem boundary; existing registry source. Preprint, theory under assumptions and reported experiments only. |

The mutable Brooks author PDF was separately fetched and SHA-256 hashed; receipt
collected at `2026-09-22T16:50:36Z`:
`eaa23f6d31de1c63ce22ca4299b67fbdf14e0480ccca4b06b926d5389324efc8`.
That identifies this later fetch, not the earlier web-rendered response.
No body was archived because this task permits writing only this report.
Blackwell's original DOI `10.1214/aoms/1177729032` was identified, but the
publisher full/PDF paths returned an unavailable page; no claim to have read
that original paper. A Cover Stanford PDF route failed, its alternate was
image-only, and a large author-hosted textbook was consulted at the TV
definition only; none substitutes for an unseen original proof.

## Gaps that matter for this release

1. Replace “compatible outputs” with checked, scoped evidence joins. Keep
   statistical qualification separate from contract declarations.
2. Use C2–C4 as accounting identities/bounds, C5–C7 as conditional mathematical
   results, and C1/C8 as design/evaluation obligations. Do not blur statuses.
3. Preserve no-model answers. These laws also improve deterministic workflows,
   human review funnels, and data collection; they do not require a new model.
4. Run one cross-field worked composition on untouched paired cases: for
   example extraction plus constrained allocation plus optional review. Compare
   to the existing rule/classical baseline, including total cost and fallback
   load. Predictions of unchosen interventions require an identified design,
   not merely replay of observational outcomes.
5. Require actual design responses and measured outcomes before marketing
   this as a validated engine. Arithmetic checks prove neither model quality
   nor that the skill reliably discovers useful compositions.

Existing repository checks passed after the report was written: `make check`
(70 unit tests, repository checks, both numerical self-tests, shell syntax)
and `git diff --check`. The report was read back in full. These checks do not
implement or certify the newly proposed law/falsifier suite.

API-equivalent cost receipt: unavailable—this worker exposes no observed token
usage or inference billing metadata; unknown is not zero. No delegation savings
or empirical quality gains are claimed.
