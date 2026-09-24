# Independent adversarial review of Augustus 0.8.0 plan v4

NOT ACCEPTED - 0 P0, 6 P1, 5 P2

Review date: 2026-09-24. This is a review of the frozen plan, not acceptance
of an implementation or authorization to operate the maintainer's host.
All six P1 findings need correction before their affected experiments run.
No P0 is established. The protocol is repairable without changing the
maintainer's settled GPU, Jev, PAW or publication decisions.

## Provenance, inputs and execution

**Requested routing:** the assignment requests this artifact as
`research/080/reviews/astra-max-v4.md`, but contains no executable model ID
or effort-setting string for this session. I cannot recover a routing
setting from the filename. The prior v3 review's request for `gpt-6-astra`
at `max` is historical, not evidence of this session's routing.

**Observed identity, verbatim from my environment:**
"You are an AI assistant accessed via an API."
No serving-model name, model ID, provider
attestation or reasoning-effort value is exposed to me. In particular, I
cannot certify that this is Astra or that its effort is max. I performed
the review directly; no reviewer, subagent or new thread was delegated it.

Repository: [24601/Augustus](https://github.com/24601/Augustus). I ran the
requested fetch and checkout. The checked-out branch is
`research/080-exopo-trainer`; HEAD is
[`58be8b4e1bd0608029291f2cf711c7984084fcee`](https://github.com/24601/Augustus/commit/58be8b4e1bd0608029291f2cf711c7984084fcee),
"Add plan v4, its dispositions, and the v4 arithmetic". The worktree was
clean before this review file was created.

**SHA-256 of [plan-v4.md](../plan/plan-v4.md):**

```text
6102f850cbf94bb3da1f372127f660efcbea00d5a1e0ccf8400023d349483e50
```

Read in full: the plan; [v4 dispositions](../plan/plan-v4-dispositions.md);
[v3](../plan/plan-v3.md); [binding v3 errata](../plan/plan-v3-errata.md);
[Fable v3](fable-5.1-xhigh-v3.md); [Astra v3](astra-max-v3.md);
[M0 receipt](../receipts/m0-tabputer-1-2026-09-23.md);
[v4 arithmetic](../calc/calc_v4.py) and [saved output](../calc/calc_v4.out.txt);
[AGENTS.md](../../../AGENTS.md) and [CONTRIBUTING.md](../../../CONTRIBUTING.md).
Also read the relevant research protocol/fold prompt, the PAW/RAP source
card, the current confirmation helper, the acquisition-window wrapper,
the batched vLLM smoke, and the relevant nftables rules. Loaded the
Augustus and explaining-code guidance. A mistaken read of
`research/fold-prompt.md` failed; the actual
[research fold prompt](../../prompts/research-fold.md) was then read.

Primary external checks, all read-only:

- [Maurer–Pontil, arXiv:0907.3740v1](https://arxiv.org/pdf/0907.3740),
  full paper, especially Theorems 4 and 11 and the definition of sample
  variance. This is the theorem v4 names, not an inference from its title.
- [PyTorch 2.12 allocator-limit documentation](https://docs.pytorch.org/docs/2.12/generated/torch.cuda.memory.set_per_process_memory_fraction.html)
  and [vLLM 0.29.0 engine arguments](https://docs.vllm.ai/en/v0.29.0/configuration/engine_args/),
  read in full and checked at their memory-limit passages. Separate HTML
  captures for provenance resolved to those exact URLs at
  `2026-09-24T04:42:38Z`; SHA-256 respectively
  `7e1b0425408b3900b9dc5675e0548cfafdcb4e1f7ab5d0a2130236837f4f3cbe`
  and `c74e9018ba3922014af415fc1ff3f91eb96ce4c72f0702a7ff54cded3f6291b4`.
- The RAP Git tree and three frozen prediction files at
  [`901acfbbde65d56dc7808b39a2a530f93b33cf4c`](https://github.com/programasweights/rules-as-programs/commit/901acfbbde65d56dc7808b39a2a530f93b33cf4c).
  Also read the two saved summaries and the pinned summarizer to resolve
  the metric definition: its macro-F1 averages binary positive-class F1
  across rules, not across severity labels.
  The appendix recomputes their metrics from predictions, not from saved
  summary metrics. No upstream code or model was executed.

Executed in this orb, with Python 3.11.6:

```bash
git fetch origin research/080-exopo-trainer
git checkout research/080-exopo-trainer
git rev-parse HEAD
git show -s --format=%s HEAD
sha256sum research/080/plan/plan-v4.md
python3 research/080/calc/calc_v4.py > /tmp/astra-v4-calc-rerun.txt
diff -u research/080/calc/calc_v4.out.txt /tmp/astra-v4-calc-rerun.txt
```

The arithmetic rerun exited successfully and the diff was empty: the
saved output is **byte-identical**. Script SHA-256:
`4a2d2308f5f56533c056864f63342ebe2cb1f7dfda9b2a01c90bd2f88b4e8b80`;
output SHA-256:
`5d7e26442b0ef8f7c3ce1a2e4c04cfc70e5743c23c46e3b532d683d1a8050b7a`.
Reproducibility of those bytes does not validate the assumptions producing
them. The independent appendix does not import or execute that script.

The appendix was executed directly from this Markdown's Python block.
Its initial RAP calculation used severity-label macro-F1, which did not
match the source's metric; source inspection established the rule-macro
definition, and the script was corrected and rerun. This was a reviewer
calculation correction, not evidence of an upstream numerical defect.

`make check` initially stopped at `ModuleNotFoundError: No module named
'yaml'`. After reading the pinned development requirements, the check
was run in an ephemeral uv environment, without changing the manifest:

```bash
uv run --no-project --with-requirements requirements-dev.txt make check PYTHON=python
```

Result: `repository quality checks passed`; `Ran 123 tests` / `OK`;
`self-test ok`; `revisit-fingerprints self-test ok`; shell syntax checks
passed. These check the existing repository, not the future plan's
correctness. The delivery is this uncommitted review file only: no
commit, push, host activation or release.

## P1 findings

### F1 — E3 uses the range of one utility, not the paired difference

**Severity: P1. Quote:** §2.7 E3, L279:
"**clipped to [−0.2, 1] at the design lock, so R = 1.2**".
This conflicts with §2.4, L169–170, which correctly defines R as the range
of the **paired differences**.

**Failure path.** Two utilities in that interval can differ by either
−1.2 or +1.2. The guaranteed paired-difference width is therefore 2.4,
not 1.2. Negating utilities to obtain losses does not change that width.
No tighter joint-support constraint is proved in the plan. Using 1.2
halves the range term, so the cited theorem no longer establishes the
advertised coverage. It also makes the narrowing look feasible when it
is not at the stated variance.

Independent normal/fixed-variance planning calculation, retaining v4's
two-tail levels and 80% central equivalence power:

| E3 family | SD | v4 n, R = 1.2 | Corrected n, R = 2.4 | Fits 6,405? |
|---|---:|---:|---:|---|
| Two readers, m = 6 | 0.25 | 5,178 | 6,598 | No |
| Two readers, m = 6 | 0.30 | 6,794 | 8,271 | No |
| One reader, m = 3 | 0.25 | 4,705 | 5,971 | Yes |
| One reader, m = 3 | 0.30 | 6,185 | 7,501 | No |

At 6,405 rows the corresponding maximum planning SDs are approximately
0.24368 and 0.26502, not the claimed two-reader threshold near 0.29 and
one-reader feasibility at 0.30. More compute cannot create additional
questions in this locked validation population.

**Minimum correction.** Use R = 2.4 in the E3 protocol, arithmetic,
dispositions and lock, unless a smaller paired-support bound is actually
proved. Recompute the powered set and narrowing. Keep the 0.02 margin;
when the available population is insufficient, use the already permitted
inconclusive outcome. Do not enlarge the dataset after looking at
confirmation outcomes.

### F2 — B16 tests current local files, not the full proposer-to-artifact label path

**Severity: P1. Quotes:** §2.4, L187–188:
"The evaluator, splits and confirmation labels are outside the proposer's read
and write set, as tested by E4c and B16."
§4.3 B16, L655: "As `augexp`, inside a run container, try to recover confirmation labels".
§4.2, L587–589: "Downloads land in `/srv/aug/quarantine`, owned
by `augexp` during the window, together with the HF cache."

**Failure path.** The plan confines candidate *execution* on tabputer-1
but explicitly allows the proposer to run off-host (§2.7 E4d). It does
not give that proposer an enforced read/network boundary. A proposer
that acquires the public labeled benchmark before producing A1 can
embed a normalized-text-hash-to-label table in the frozen artifact.
It need not know the confirmation partition: the complete benchmark
mapping covers every eventual partition. The resulting artifact needs
neither quarantine access nor network access during confirmation. Hashing
it before confirmation freezes the leakage; it does not remove it.

A synthetic canary added only to the private confirmation partition is
absent from the original public corpus. Failing to recover that canary
does not demonstrate that ordinary confirmation labels are unavailable.
This is a concrete permitted information path missing from the test,
not an allegation that any current candidate has taken it.

The acquisition transition has a related gap: re-owning the pathname
does not revoke bytes already copied, open descriptors or mappings held
by the downloading uid. The prohibition on experiment containers during
windows is useful, but is not a specified teardown of all acquisition
processes, writable caches and surviving copies. B16 starts after that
transition and inside a restricted mount view.

**Minimum correction.** Define and enforce the proposer's input boundary,
not only the candidate's runtime mounts. Use a separate clean acquisition
principal or a verified clean acquisition lifecycle with no surviving
processes/copies, and test that transition. Challenge the entire proposal
path with a pre-existing labeled corpus and an embedded lookup artifact,
not only a newly planted private canary. Public-benchmark memorization
cannot be ruled out by local ACLs: either use genuinely unseen independent
confirmation for that stronger claim, or explicitly limit the claim to
local-file isolation and record contamination as unresolved. Keep the
new label-free staging; it closes the original direct `/stage` leak.

### F3 — The GPU budget and launch floor do not bound host memory consumption

**Severity: P1. Quotes:** §4.2, L615–618:
"M5 PAW-ft
38 GiB (0.306)" and "the wrapper samples `/proc/meminfo` every 5 s, refuses to launch below 24 GiB and kills the
container below 6 GiB".
§4.3 B18, L657: "The budget aborts the allocation".

**Failure path.** At the permitted launch floor, a compliant PAW-ft job
may request 38 GiB of GPU memory, independently of up to 16 GiB of CPU
memory. Both consume this UMA host's RAM, but M0 measured GPU memory
outside the CPU cgroup. Their combined allowance is 54 GiB, greater than
24 GiB before retaining any reserve. A burst can cross the abort floor
and exhaust memory before the next five-second sample. A watchdog is
detection and recovery, not prevention of that allocation.

The proposed APIs are also narrower than B18's wording. PyTorch documents
a per-process **caching allocator** limit; vLLM documents a **per-instance**
limit, and an explicit KV-cache size can override its utilization-based
calculation. These are not an aggregate, adversary-resistant GPU cgroup.
Multiple processes/instances, allocations outside that allocator, or
candidate-controlled settings are not bounded by one declared fraction.
This matters especially when F4 restores the required candidate GPU path.
No kernel or driver exploit is needed for this failure mode.

**Minimum correction.** Admit a run against its aggregate CPU, GPU,
teacher/service and overhead allowance plus a host reserve, not a fixed
24 GiB floor. With the currently stated maximum CPU/GPU allowances and
the existing 6 GiB reserve, PAW-ft alone needs at least 60 GiB plus
unbudgeted overhead, or smaller demonstrably enforced allowances.
Specify which trusted component enforces the aggregate GPU budget and
test multi-process and non-default-allocator paths safely. If the local
GPU boundary cannot enforce the promised protection, use the authorized
per-experiment Colab route or a controlled GPU service; never CPU.
Retain the watchdog as a secondary control and do not deliberately OOM
the shared host to validate this correction.

### F4 — Candidate GPU denial contradicts binding D-b

**Severity: P1. Quotes:** §4.2, L608–609: "Candidate code never
gets GPU devices." §4.6, L708–709: "candidate code runs without devices anyway."

**Failure path.** D-b explicitly includes candidate and hill-climb code
in the GPU requirement. The plan repeats GPU-for-everything in §0, then
denies its execution capability in the actual container profile.
Implementing that profile either runs those candidates on CPU, contrary
to the binding decision, or makes GPU-dependent candidates fail before
the experiment. The denial cannot be used to justify the GPU safety
claim while the experiments require the opposite behavior.

**Minimum correction.** Specify the actual GPU-capable candidate path
and its device/budget isolation, incorporating F3. A mediated GPU service
is an option only if the required candidate work really executes on GPU.
Where tabputer-1 cannot support the job safely, use Colab and label its
different containment scope. This is not a request to reconsider D-b.

### F5 — The power calculator tests equivalence for NI and mixes true effects with boundary gaps

**Severity: P1. Quotes:** §3.3 M5, L398:
"At true Δ = 0 with 80% power, EB at K = 5 needs 6,671 rows (σ = 0.10), 14,035 (0.20) or 25,535 (0.30)."
§2.7, L243–244: "g = 0 for equivalence and non-inferiority
(true Δ = 0 is the planning point) and the prespecified planning effect for superiority".

**Failure path A.** M5 declares one-sided NI, UCB < +0.01. The arithmetic
instead calls `n_equiv_eb`, requiring both endpoints inside ±0.01.
Using a two-sided CI does **not** make the NI event two-sided. Under the
script's fixed-SD normal approximation, 80% equivalence power corresponds
to 90% one-sided NI power at equality. The minimum 80% NI sample sizes
at K = 5 are **6,180 / 12,368 / 21,902**, not
6,671 / 14,035 / 25,535. For example, T2b's 12,850 rows at SD 0.20 are
powered for the declared NI test, but v4 calls them unpowered and bars
them from either outcome row. This is conservative for false positives
but wrong for the registered selection/recommendation rule.

**Failure path B.** `n_super_eb` takes the positive distance **beyond the
superiority margin**. The common rule and arithmetic section 7 instead
call g the true planning effect; arithmetic section 3 even prints
"true 0.04 gain beyond 0". E3's margin is 0.02. A true gain of 0.04
therefore supplies a gap of 0.02, not 0.04. With corrected E3 R = 2.4 and
SD 0.30, n is **7,318** at m = 6, or **6,592** at m = 3, rather than
2,498 / 2,243 for a gap of 0.04. The latter gap means a true gain of
0.06. The ambiguity can turn an unreachable contrast into a powered one.
M5's analogous true gain 0.02 with margin 0.01 needs gap 0.01: at SD
0.20, K = 5, the approximation gives 12,368 rather than 4,181.

**Minimum correction.** Register separate names for `true_delta`, the
test boundary and the derived distance to that boundary. Give NI its
one-sided power calculation; keep equivalence's central calculation.
Recompute all powered sets and scenarios, and test both interpretations
on inputs where they differ. Label these n values **normal/fixed-SD
planning approximations**, not finite-sample power guarantees: the
acceptance theorem is distribution-free under its sampling assumptions,
but the power approximation substitutes pilot SD for a random sample SD
and assumes an approximately normal sample mean. That approximation is
not made distribution-free by using an EB radius.

### F6 — M5 can escalate past a successful tested PAW-standard arm

**Severity: P1. Quotes:** §3.3, L395 includes "**A2a** PAW-standard via the local single-GPU compiler";
L397 restricts the family to "**K = 5** low rungs (R1, R2a, R2b, A1, A2b)";
L401 says "R3a superior to every low rung by more than 0.01 on a powered task".

**Failure path.** A2a is a tested lower artifact form, not declared
descriptive-only, but it appears in neither side of the decision family.
Consider a powered task where each of the five listed contrasts has
interval [0.026, 0.034] and A2a has [−0.004, 0.004]. V4's enumerated
family triggers escalation, although PAW-standard meets the very same
NI gate. It can also fail to stop at A2a when that arm is adequate on
every task. The inference would be about five selected arms, not about
the cheapest adequate artifact form or "every low rung".

**Minimum correction.** Include A2a in the eligible confirmatory family
and recalculate K, n and both verdict directions. Alternatively, explicitly
register it as descriptive-only and restrict the recommendation so that
its success cannot be reported as lower-form failure. State R0's role
too: a separate G0 acceptance exit or a member of the decision family.
Do not select the included forms after seeing results.

## P2 specification gaps

### F7 — Equal inclusion probability is not the theorem's sampling assumption

**Severity: P2. Quotes:** §2.4, L172: "EB's coverage holds for any bounded distribution";
§3.5: "a required `sampling_design`, which must be `equal_probability` for confirmation in 0.8.0".

**Failure path.** The cited theorem requires independent observations
(Theorem 4 is iid; Theorem 11 permits independent non-identical
variables). Equal inclusion probability does not ensure that. Sample
one of two equal-size clusters uniformly, where all 3,000 differences
in one cluster are zero and all in the other are one. Every row has
equal inclusion probability. Treating rows as independent gives SD zero
and, at m = 1, R = 1, an EB radius 0.00340938 around either zero or one;
coverage of the population mean 0.5 is exactly zero. There was only one
independent sampled cluster.

The existing helper already warns about independent representative
units, and G0 mentions independent gold. This is not evidence that all
planned benchmarks are dependent; it is a gap in the proposed universal
contract and its validation. E1's prior resampling also needs a declared
unit and sampling law rather than interpreting repeated original rows
as new independent real-world evidence. A finite benchmark census and
inference to future traffic are different estimands.

**Minimum correction.** Carry the independence/fixed-sample assumptions
into the acceptance contract and derive n and variance from the stated
unit. Specify group aggregation or the applicable finite-population bound
where relevant, and refuse unsupported cluster/weighted designs. Add a
correlated equal-probability countercase. Do not demand another model,
calibration stage or a universal cross-task correction to fix sampling.

### F8 — S12b still prescribes certification without an observed mean

**Severity: P2. Quote:** §3.7, L547:
"**S12b: the same at σ̂ = 0.02**" → "Non-inferiority **certified** at 3,000 rows; the skill must not refuse a feasible low-variance case".

**Failure path.** At K = 3, R = 2, n = 3,000, SD 0.02, the radius is
0.00973721. A paired fixture with mean zero passes NI. A fixture with
the **same n and SD** but mean +0.005 has UCB 0.01473721 and fails.
Thus the expected answer is not determined by the scenario's inputs.
A planning assumption of true mean zero cannot replace the observed
mean at certification. Moreover, even the corrected one-sided normal
power approximation needs 3,015 rows at equality here; 3,000 gives about
0.76414 power, so it does not meet the common 80% powered-set rule.

**Minimum correction.** Split planning from observed certification.
Supply actual paired losses or both observed mean and sample SD for a
certification fixture, and include the matched-SD failing fixture. If
this is a planning scenario, choose a genuinely powered low-SD example
or expect the stated underpowered result. Correct S12a's NI n via F5.

### F9 — E3's joint determinism probability and remedy are not established by M0

**Severity: P2. Quote:** §2.7 E3, L281:
"over 9 calls a whole question replays identically with probability 0.0098 [Rep calc §6]".

**Failure path.** This is 0.598 to the ninth power, which assumes nine
independent events with the same marginal probability. M0 measured
neither their joint law nor HotpotQA's per-call marginals. Even if every
marginal really were 0.598, the possible all-nine intersection ranges
from zero to 0.598. Only the conditional arithmetic was reproduced.

The smoke source submits the **same prompt list** twice using the same
sampling configuration. Those passes already disagreed. A fixed input
batch therefore is not an established cure; a fixed internal execution
schedule might help, but has not been demonstrated. The proposed
50-question check only reports disagreement and specifies no failure
threshold or consequence. P6's finite-population truth must not silently
change across resplits or disagree with the answers the policies saw.

**Minimum correction.** Label 0.0098 as hypothetical iid arithmetic, not
measured replay probability. Define immutable once-generated replay
tables shared by all policies/resplits, with claims conditional on those
tables, or define and validate the stochastic replay estimand. If
deterministic re-execution is needed, register its tolerance and failure
path before measuring it; retain GPU/Colab, not a CPU fallback.

### F10 — P10 mixes metrics and upgrades synthetic rule checks to a real-text conclusion

**Severity: P2. Quote:** §2.6 P10, L220:
"programs lose on fuzzy real text" and
"0.771 recall where lexical matching cannot see the distinction, where fine-tuned PAW reaches 0.961".

**Failure path.** Independent recomputation of RAP's frozen predictions
confirms that 0.961 is **macro-F1**, not recall; fine-tuned PAW's controlled
recall is 1.000. Here macro-F1 means the mean of per-rule binary
positive-class F1. The comparable controlled macro-F1 values are 0.863
for lexical code and 0.961 for PAW-ft. The external lexical macro-F1 is
0.993. These are different metrics/slices unless labeled explicitly.
More importantly, the controlled records say `synthetic`, with labels
fixed by construction; the external records also identify synthetic
contrastive inputs. Recomputing predictions on those cases does not
establish what arbitrary programs do on independent fuzzy real text.
The circularity warning in §3.3 correctly withholds that claim for T1,
but P10's evidence cell does not preserve the same boundary.

**Minimum correction.** Name metric, split and synthetic provenance
beside each number. Keep the reproduced-table label narrowly attached
to the arithmetic on frozen predictions; mark the real-text program
comparison [H] pending M5. Do not delete the useful PAW arm or assume
program failure is required for a successful reproduction.

### F11 — E4a's declared positive-control outcomes are false for some named cells

**Severity: P2. Quote:** §2.7 E4a, L296:
"radius removed → every cell (size 0.50)".

**Failure path.** `sign_exact` has no radius to remove, so this mutation
cannot make every cell fail. For a rare-large, mean-zero difference
0.98 × (Bernoulli(0.0001) − 0.0001), n = 300 and strict acceptance below
zero, a removed radius adopts whenever no rare event occurs: probability
0.970444, not 0.50. Even in a symmetric continuous case with per-contrast
size 0.50, the specified any-of-five event has size 0.96875 if the five
contrasts are independent, not 0.50. Joint dependence must be specified.
Likewise, a sign flip in NI is not automatically detectable for every
margin/radius configuration merely because the mode is NI.

**Minimum correction.** Pre-register individual detecting cells with
complete distributions, margins, joint candidate dependence and exact
or justified expected events. Test radius mutations only on methods
that use a radius; give `sign_exact` its own mutation. Keep the
simultaneous CP diagnostic and its stated tolerance. Do not make a
correct implementation fail because an impossible positive-control
expectation was mistaken for an acceptance condition.

## Statistical conclusions that should not be over-corrected

For fixed policies, prespecified bounds and independent confirmation
units, §2.4's **formula and two-tail composition are correct**. Map a
difference in [a,b] to [0,1], use the unbiased sample variance with
denominator n−1, apply Maurer–Pontil to the variable and its reflection,
and assign each tail δ = α/(2m). A union bound over the 2m tail events
gives simultaneous coverage at least 1−α; independence **between
contrasts** is not required. Conditional on a separate pilot/search
sample, this reasoning still works for policies and sample sizes frozen
before confirmation. Repeated adaptive confirmation peeks would not be
covered.

Reading superiority, NI and equivalence from that **same valid
simultaneous interval** requires no extra penalty for the number of
claim labels. A false interval-based assertion implies a coverage failure.
The error in F5 is power-event calculation, not a requirement to replace
the common interval with three tests. `sign_exact` is the explicitly
separate binary, zero-margin direction test and should remain separate.

E1's R_r = 2 max(C_FP,C_FN) is a safe paired-difference bound; its stated
cost normalization gives 1.00 at 1:1 and 1.96 at 1:49. M5's R = 2 is
also safe. E3 alone substitutes the one-policy width. The rare-large
v3 counterexample really is repaired by an EB radius: at n = 12,850,
m = 19, R = 1.96 and observed SD zero the radius is 0.00260770, greater
than 0.00005. The no-event probabilities 0.2766328082 and 0.2049315506
also independently reproduce. This is a theorem/constructed-distribution
check, not a product outcome.

**M5's intersection-union idea is valid for its conjunctive claim.**
For a fixed low rung to pass on *every* task in its preselected powered
set, any false all-task NI claim entails passing at least one false
task-level NI test. A union bound over K possible selected rungs then
controls the existential choice. One must not automatically multiply
alpha by the task count for that conjunction.

The reverse row is a different logical expression: some task on which
*all* low rungs are inferior. With the present K = 5, at most three
tasks, and per-tail δ = 0.005, the global false all-task-NI declaration
is bounded by 5δ = 0.025 and the global false any-task-escalation
declaration by 3δ = 0.015; their union is at most 0.04. This argument
conditions on frozen powered sets and covers those global declarations,
not simultaneous accuracy of every individual task/rung statement.
It does not repair the omitted A2a in F6. The pre-registered NI and
inferiority thresholds are symmetric about the **same +0.01 boundary**;
workload-local and inconclusive outcomes are legitimate, not failed
experiments. Scope the reported recommendation to its powered tasks.

**The window ordering is now reachable.** W1 contains infrastructure
and acceptance models, with synthetic acceptance inputs; M2 can lock
the design without reading experiment text; W2 depends on both M2 and
M0b; W3 names the separate site-build dependency window. A synthetic
B16 custody test at M0b need not download the real experiment corpus.
Retain dated window receipts and closed-egress retests. I found no
remaining design-lock-before-download cycle in that specification.

## Verification of all prior v3 findings

"Closed" below means closed in v4's **specification**, unless a supplied
M0 receipt is explicitly cited. I did not re-execute host acceptance.
"Partial" means the original correction helps but the claimed closure
is not complete. Counts: 11 Fable findings and 7 Astra findings.

| Prior finding | Status in v4 | Verification and residual |
|---|---|---|
| Fable P1-1 — download/lock cycle | Closed | W1/M2/W2/M2b/W3 order, synthetic acceptance, and window receipts are explicit (§2.7, §4.2, §7). |
| Fable P2-1 — proxy DNS | Closed; M0-reported pass | Local resolver exception is named and present in nft rules; the supplied B9 receipt records success. |
| Fable P2-2 — site staging scope | Closed by binding decision | The record and site source are public under D-c/D-d; §4.1 states the changed premise. |
| Fable P2-3 — superiority margins and g | Partial | Margins and lock timing are explicit, but true-effect versus boundary-gap semantics disagree with the calculator (F5). |
| Fable P2-4 — fit-B partition | Closed | Separate 200k fit-B is allocated; planned CivilComments remainder is 1.4M. |
| Fable P2-5 — disk exhaustion | Closed in specification | Size-bounded run/prediction storage plus ENOSPC test B17; execution is still an M0b obligation. |
| Fable P2-6 — hosted review disclosure | Closed | Header explicitly acknowledges hosted review; public-record decision is not reopened. |
| Fable P2-7 — E4a detecting cells | Partial | Cells, planning-effect lock and any-of-five event are named, but some promised control outcomes cannot hold (F11). GPU conversion removes the old CPU-parallelism issue. |
| Fable P2-8 — profile/calibration nits | Closed as originally raised | Prediction group, B10 counters, test-container ordering, B5 receipt, text-versus-label release and no-intercept temperature are specified. F2–F4 concern residual/new boundaries, not a demand to undo these fixes. |
| Fable P2-9 — M5 levels/expansion and CLINC decision | Closed as originally raised | Matching tails, analysis-lock expansion and route-versus-abstain costs are explicit. F5/F6 are distinct quantitative/family defects. |
| Fable P2-10 — provenance/percentages/token estimate | Closed | Obsolete Mac-isolation wording is removed; the synthetic cost regrets independently round to +95%/+216%/+553%; the earlier token-runtime estimate is replaced by measurements/pilots. These are not deployment wins. |
| Astra 1 — original labeled corpus readable | Partial | Label-free per-run staging addresses the direct mount leak. Off-host proposer acquisition and acquisition lifecycle remain outside B16's proof (F2). |
| Astra 2 — unjustified family CI | Partial | EB fixes the stated rare-large counterexample and the Bonferroni argument is valid under its assumptions. E3's range breaks the claimed implementation of that guarantee (F1); the sampling contract needs F7. |
| Astra 3 — contradictory download prerequisites | Closed | Same verified ordering as Fable P1-1. |
| Astra 4 — P6 replay workload | Closed as originally raised | Full replay is now budgeted: 133,290/66,645 calls; the held-out P6 population takes 115,290/57,645. The independent arithmetic agrees. F9 concerns stochastic replay identity, not missing calls. |
| Astra 5 — disputed lineage and substring identity | Closed in specification | Declared identity, missing-parent `unknown`, revision-bound `disputed`, and preservation of the allegation are explicit. No ancestry or legal determination is inferred. |
| Astra 6 — S12 row-count-only answer | Partial | Mode/method/SD are supplied, but certification still lacks an observed mean and the NI power arithmetic is wrong (F5/F8). |
| Astra 7 — stale memory blocker | Closed as originally raised | Dated MemAvailable replaces the stale k3s attribution; blocked state is measured at launch. F3 is a new insufficiency of the proposed protection, not a claim that the host is currently blocked. |

## What v4 gets right

- Bounded EB rather than a normal/bootstrap interval that can collapse is
  the correct response to sparse rare losses. Keep the theorem/diagnostic
  distinction and the unchanged substantive margins.
- The explicit inconclusive rows allow an honest result when a dataset
  cannot resolve a small margin. Do not manufacture power by moving the
  margin or call an underpowered run evidence for either side.
- The artifact-form ladder, independent real-text tasks, frozen A1 and
  fixture-only T1 expose the circularity trap instead of hiding it.
  Programs, PAW and models deserve the same workload-specific gate.
- Detection after an irreversible effect is correctly distinguished from
  pre-effect enforcement. Operational failure is not `OK`.
- Quarantine, label-free confirmation inputs, quotas, tested egress,
  measured rather than imagined GPU behavior and honest Colab non-claims
  are improvements. M0b explicitly marks the new mechanisms as work
  still to be implemented; their absence from the old window wrapper
  is not by itself a plan defect.
- Jev's permitted comparator/routing/selection/inference roles, the
  exclusion from our training data and the local PAW preference remain
  binding. None of this review's corrections requires reopening them.

## Not covered

No tabputer-1 access, sudo, host mutations, GPU workload, boundary test,
Colab experiment, training run, attack against real confirmation data or
model inference was performed. M0 measurements are supplied evidence,
not measurements made by this reviewer. I did not validate all dataset
cards/licenses, all bibliography entries, every swept repository, future
kernel parity, throughput at E3's actual context lengths, or a rendered
paper/site/skill activation. No legal issue or publication-risk gate is
raised. I did not attempt to recover hidden serving-model identity.

The independent calculation below validates arithmetic and constructed
counterexamples. It is not a Monte Carlo proof of finite-sample power,
an experimental replication of RAP's models, or an end-to-end trainer
result. No runtime guidance was changed. This review does not authorize
a release; an explicit maintainer go is still required.

## Appendix — independent calculation script

This script uses only the standard library. Its n search inverts the
normal-quantile inequality rather than calling the plan's power function;
E1 loss means/variances use integer weighted-error counts. It deliberately
reconstructs the *same seeded synthetic input population* for checking
the quoted planning figures, not a different dataset. RAP is fetched
only from the pinned public revision, with a response-size bound; its
prediction data are parsed, never executed. Everything else is offline.

Run from the repository root by extracting the following Python block
from this review and executing it. It writes no files.

```python
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from hashlib import sha256
from math import comb, fsum, log, sqrt
from random import Random
from statistics import NormalDist, mean, stdev
from urllib.request import urlopen
import json

ND = NormalDist()
ALPHA = 0.05

def rad(sd, n, k, width):
    ell = log(4 * k / ALPHA)
    return sqrt(2 * ell / n) * sd + 7 * width * ell / (3 * (n - 1))

def need(sd, distance, k, width, quantile):
    # One-sided 80% uses q=.8; central 80% uses q=.9.
    # The inequality is monotone in n. This is planning, not a power theorem.
    z = ND.inv_cdf(quantile)
    def enough(n):
        return rad(sd, n, k, width) + z * sd / sqrt(n) <= distance
    lo, hi = 2, 200_000_000
    if distance <= 0 or not enough(hi):
        return None
    while lo < hi:
        mid = (lo + hi) // 2
        if enough(mid):
            hi = mid
        else:
            lo = mid + 1
    assert enough(lo) and (lo == 2 or not enough(lo - 1))
    return lo

def max_sd(n, distance, k, width, quantile):
    return ((distance - rad(0, n, k, width)) * sqrt(n)
            / (sqrt(2 * log(4 * k / ALPHA)) + ND.inv_cdf(quantile)))

print('RARE')
with localcontext() as ctx:
    ctx.prec = 40
    for n in (12850, 15850):
        print(n, f'{Decimal("0.9999") ** n:.10f}')
print('EB zero-sd radius', f'{rad(0, 12850, 19, 1.96):.10f}')
print('E1 R endpoints', 2 * max(1 / 2, 1 / 2), 2 * max(1 / 50, 49 / 50))

print('E3 equivalence: k sd old-n corrected-n')
for k in (6, 3):
    for sd in (.25, .30):
        print(k, sd, need(sd, .02, k, 1.2, .9), need(sd, .02, k, 2.4, .9))
    print('max-sd at 6405', k, f'{max_sd(6405, .02, k, 2.4, .9):.8f}')
    print('superiority, gap .04 versus .02', k,
          need(.30, .04, k, 2.4, .8), need(.30, .02, k, 2.4, .8))
for readers in (2, 1):
    print('replay', readers, 7405 * 9 * readers, 6405 * 9 * readers,
          f'{7405 * 9 * readers * 64 / 2004 / 3600:.6f}', 'decode-hours')

print('M5: k sd central-80-n NI-80-n')
for k in (5, 3):
    for sd in (.10, .20, .30):
        print(k, sd, need(sd, .01, k, 2, .9), need(sd, .01, k, 2, .8))
for n in (6000, 12850, 60000):
    print('M5 NI max-sd', n, f'{max_sd(n, .01, 5, 2, .8):.8f}')
print('M5 superiority gap .02 versus .01',
      need(.20, .02, 5, 2, .8), need(.20, .01, 5, 2, .8))

print('S12 matched-sd fixtures')
for mu in (0, .005):
    a = .02 * sqrt(2999 / 3000)
    rows = [mu + a * (1 if i % 2 else -1) for i in range(3000)]
    upper = mean(rows) + rad(stdev(rows), len(rows), 3, 2)
    print(f'mean={mean(rows):.6f} sd={stdev(rows):.6f} UCB={upper:.10f}', upper < .01)
print('S12 equality NI need / approximate power at 3000',
      need(.02, .01, 3, 2, .8),
      f'{ND.cdf((.01 - rad(.02, 3000, 3, 2)) * sqrt(3000) / .02):.8f}')

print('OTHER COUNTEREXAMPLES')
r = rad(0, 3000, 1, 1)
coverage = sum(.5 for b in (0, 1) if b - r <= .5 <= b + r)
print('two clusters: radius / actual coverage', f'{r:.10f}', coverage)
print('iid nine / Frechet bounds', f'{.598 ** 9:.10f}', max(0, 9 * .598 - 8), .598)
print('radius removed, rare / independent any-of-five', f'{.9999 ** 300:.8f}', 1 - .5 ** 5)
print('PAW memory: allowance / floor / reserve-inclusive', 38 + 16, 24, 38 + 16 + 6)
print('M5 global declaration bounds', 5 * .005, 3 * .005, (5 + 3) * .005)
listed = {name: (.026, .034) for name in ('R1', 'R2a', 'R2b', 'A1', 'A2b')}
paw_standard = (-.004, .004)
print('omitted A2a: escalation / adequate A2a',
      all(lo > .01 for lo, hi in listed.values()), paw_standard[1] < .01)

print('E4 cutoff independently inverted from the binomial CDF')
def cp_upper(x, n, tail):
    # Exact integer combination, Decimal probability recurrence; no lgamma CDF.
    with localcontext() as ctx:
        ctx.prec = 40
        choose = Decimal(comb(n, x))
        lo, hi = Decimal(0), Decimal(1)
        target = Decimal(str(tail))
        for _ in range(65):
            p = (lo + hi) / 2
            mass = choose * p ** x * (1 - p) ** (n - x)
            total = mass
            for j in range(x, 0, -1):
                mass *= Decimal(j) * (1 - p) / (Decimal(n - j + 1) * p)
                total += mass
            if total > target:
                lo = p
            else:
                hi = p
        return float(hi)

cells = 2 * 2 * 3 * 2 * 4 + 2 * 3 * 2
for x in (2049, 2050):
    upper = cp_upper(x, 40000, .05 / cells)
    print(x, f'{upper:.10f}', upper <= .055)
print('cells / repetitions / quoted max-element envelope / chunk MiB / batches',
      cells, cells * 40000, cells * 40000 * 2500,
      2000 * 2500 * 4 / 2 ** 20, cells * (40000 // 2000))

print('E1 same seeded inputs; independent integer-cost moments and quantile inversion')
N = 300_000
generator = Random(80003)
populations = []
for concentration in (1.0, 1.5, 2.0, 3.0):
    ps = [generator.betavariate(.08 * concentration, .92 * concentration) for _ in range(N)]
    ys = [int(generator.random() < p) for p in ps]
    negative_seen = concordant = 0
    for p, y in sorted(zip(ps, ys)):
        if y:
            concordant += negative_seen
        else:
            negative_seen += 1
    auc = concordant / (sum(ys) * (N - sum(ys)))
    populations.append((abs(auc - .9), concentration, auc, ps, ys))
_, concentration, auc, ps, ys = min(populations, key=lambda p: p[0])
print('population', concentration, f'{auc:.6f}', f'{sum(ys) / N:.6f}')
noise = Random(80004)
errors = {t: [noise.gauss(0, t) for _ in range(N)] for t in (.1, .3)}
logits = [log(min(max(p, 1e-12), 1 - 1e-12) /
              (1 - min(max(p, 1e-12), 1 - 1e-12))) for p in ps]

def integer_errors(flags, ys, fp, fn):
    return [fp * int(flag and not y) + fn * int(y and not flag)
            for flag, y in zip(flags, ys)]

def integer_moments(values, denominator):
    count, total, squares = len(values), sum(values), sum(v * v for v in values)
    mu = total / (count * denominator)
    var = (count * squares - total * total) / (count * (count - 1) * denominator ** 2)
    return mu, sqrt(var)

for fp, fn in ((4, 1), (1, 1), (1, 4), (1, 9), (1, 19), (1, 49)):
    den = fp + fn
    a = integer_errors((p >= fp / den for p in ps), ys, fp, fn)
    b = integer_errors((p >= .5 for p in ps), ys, fp, fn)
    cost = sum(a) / (den * N)
    margin, width = .02 * cost, 2 * max(fp, fn) / den
    delta, sd = integer_moments([x - y for x, y in zip(a, b)], den)
    ns = need(sd, -delta - margin, 19, width, .8)
    equivalence = []
    for tau in (.1, .3):
        c = integer_errors((l + e >= log(fp / fn) for l, e in zip(logits, errors[tau])), ys, fp, fn)
        _, sigma = integer_moments([x - y for x, y in zip(c, a)], den)
        equivalence.append(need(sigma, margin, 19, width, .9))
    regret = sum(b) / sum(a) - 1
    print(f'{fp}:{fn}', 'super', ns, 'equiv', *equivalence, 'stale-regret', f'{regret:+.6%}')
print('partitions', 2_000_000 - 200_000 - 200_000 - 100_000 - 100_000,
      23850 - 8000 - 3000)

print('RAP METRICS: recomputed from pinned prediction rows, not model reruns')
revision = '901acfbbde65d56dc7808b39a2a530f93b33cf4c'
base = ('https://raw.githubusercontent.com/programasweights/rules-as-programs/'
        + revision + '/experiments/eacl2027/outputs/frozen/')
for name in ('lexical.jsonl', 'paw-finetuned.jsonl', 'external-lexical.jsonl'):
    with urlopen(base + name, timeout=30) as response:
        blob = response.read(2_000_001)
        assert len(blob) <= 2_000_000
    rows = [json.loads(line) for line in blob.splitlines() if line.strip()]
    truth = [r['expected'] for r in rows]
    pred = [r['prediction'] for r in rows]
    assert all(not r['error'] for r in rows)
    positive = {'INFO', 'WARNING', 'CRITICAL'}
    assert set(truth) <= positive | {'OK'}
    assert set(pred) <= positive | {'OK', 'INVALID'}
    tp = sum(t in positive and p in positive for t, p in zip(truth, pred))
    pos = sum(t in positive for t in truth)
    f1 = []
    for rule in sorted({r['rule_id'] for r in rows}):
        counts = Counter((r['expected'] in positive, r['prediction'] in positive)
                         for r in rows if r['rule_id'] == rule)
        hits = counts[True, True]
        denominator = 2 * hits + counts[True, False] + counts[False, True]
        f1.append(2 * hits / denominator if denominator else 0)
    print(name, 'rows', len(rows), 'binary-recall', f'{tp / pos:.6f}',
          'rule-macro-F1', f'{fsum(f1) / len(f1):.6f}')
    print('provenance', dict(Counter(r['provenance'] for r in rows)))
    print('source-sha256', sha256(blob).hexdigest(),
          'retrieved', datetime.now(timezone.utc).isoformat())
```

### Execution record

The final script exited 0. The command was:

```bash
python3 -u - <<'PY'
from pathlib import Path
p = Path('research/080/reviews/astra-max-v4.md')
text = p.read_text()
code = text.split('```python\n')[1].split('\n```', 1)[0]
exec(compile(code, str(p) + ':independent-appendix', 'exec'))
PY
```

Selected decisive output (2026-09-24; n searches also asserted that the
immediately preceding integer n fails the planning inequality):

```text
EB zero-sd radius 0.0026077025
E3 equivalence: k sd old-n corrected-n
6 0.25 5178 6598
6 0.3 6794 8271
3 0.25 4705 5971
3 0.3 6185 7501
M5: k sd central-80-n NI-80-n
5 0.1 6671 6180
5 0.2 14035 12368
5 0.3 25535 21902
mean=0.000000 sd=0.020000 UCB=0.0097372078 True
mean=0.005000 sd=0.020000 UCB=0.0147372078 False
S12 equality NI need / approximate power at 3000 3015 0.76414088
2049 0.0549748563 True
2050 0.0550006938 False
lexical.jsonl rows 192 binary-recall 0.770833 rule-macro-F1 0.862718
paw-finetuned.jsonl rows 192 binary-recall 1.000000 rule-macro-F1 0.960961
external-lexical.jsonl rows 160 binary-recall 0.987500 rule-macro-F1 0.993421
```

The three pinned RAP bodies, fetched at `2026-09-24T04:53:55Z`, had these
SHA-256 digests in the same order:

```text
6577297215dbb2dfac3e120a5460332ff0204e94d8dec9d9f94b7d38b9ac2462
249c427ac65d531f2db390a2c1f957fdf2b7df15e49b15cf776eab582d4d24f2
e5c7e8dfa7598ebd4dee7c596dc545f97f3aa087d21849f08cdcf1c213d7425b
```

A separate local check confirmed all finding quotations against v4
(normalizing line-wrap whitespace only), six P1/five P2 entries, all 18
prior findings in the closure table, and resolving relative file links.
The plan hash and HEAD remained unchanged. Only this review was added;
it was not staged, committed or pushed.
