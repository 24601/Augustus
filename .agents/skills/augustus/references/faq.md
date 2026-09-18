# FAQ (design judgment, not an API)

Load this when the request is skepticism, stack replacement, family
choice, "is this only for software?", "formally verify with Jev", or
"isn't Augustus just another Jev skill?" Integration contracts for
TypeSafe Jev still live in `typesafe-ai` and the live docs. The *class*
of providers is `judgment-class.md`. Cross-domain frames:
`mental-models.md`. Proof vs judgment: `formal-methods.md`.

## Isn't this just classification?

Yes. Classification is the oldest AI task. Agree, then answer the design
question: **where does a typed judgment beat ad-hoc LLM-classify, and
where does it lose?**

It wins when a practice needs a schema-valid enum/bool/level; when you
will threshold, abstain, or re-policy from a distribution; when many
independent questions share one state; when per-item judgments were
known methods that were too expensive (per email, per paper, per hunk,
per incident); when policy must be reviewable (code, checklist, ledger).

It loses to a regex, lookup, recipe, or law that already works; to a
trained classical classifier on a stable labeled taxonomy with enough
of *your* data; to open-ended writing, counting, date math, and
multi-hop derivation; to treating in-distribution ECE as a license to
skip a held-out test.

The product is not "we invented classification." The product is placing
a fast scoring primitive beside exact work and beside generation —
matching the model's *objective* to the action's fail policy. Frames:
`mental-models.md`. Placement: `mixed-architecture.md`. Families:
`judgment-class.md`.

## Is Jev probabilistic programming?

No. It is a cool typed-decision API, not a probabilistic programming
language, and Kleisli-arrow qualifications are an exaggeration
([Erik Meijer, 2026-09-18](https://x.com/headinthebox/status/2100984170004824221)).
The gloss he endorses: **Jev gives you the marginals; a decoder gives
you the joint.** One call is factorized marginals over isolated
questions on shared state — the same isolation as the architecture
reconstruction (`notes.md` §31), not a second essay. The joint lives
in application code, sequential TypeAR, or a generative decoder. Teach
decision theory, calibration, and value of information
(`mental-models.md`), not category theory. Joints and invariants:
TLA+ / Alloy / contracts (`formal-methods.md`). Fast calibrated
factors: System One. A Noul is still not a proof.
`judgment-class.md`.

## Should we replace the LLM / the stack?

No. Default is mixed architecture: code owns control, the judgment provider
estimates, the LLM writes. Replace *classifier steps*, not the agent. A
loop with no LLM is still mixed architecture when nothing needs writing
(candidates from code; answers located, not composed). The day the task
needs a paragraph, the generator re-enters.

## Is Jev the only model this skill covers?

No. Augustus designs for the whole class of fast/cheap
categorization-classification-scoring models. TypeSafe Jev is the
documented exemplar (typed Choice / Score / Noul, live docs). Neighbors
in the class — open System-1 / decision-model heads (Laya, kev,
blackwood-rlcd, openjev-lm, encoder DeBERTa, LoRA distill; Hume's 27B drop is Watch),
constrained-AR (TypeAR), GLiNER/GLiClass encoder family (locate vs
categorize vs local multi-head), listwise/pairwise rankers, vision
scorers — are substitutes
or cousins. Pick the family from the hole, then the vendor
(`judgment-class.md` species map and when-to-use table).
`typesafe-ai` still owns *Jev* contracts; other families own their own
cards/READMEs. This skill does not become their install guide.

## Jev or Laya (or some other open head)?

TypeSafe Jev is the documented default (live docs, 64k/32k envelope). An
open head with the same Choice/Score/Noul shape is a **provider
substitute**, not a different methodology. Open weights buy self-hosting
and transfer calibration/eval duty to you. Laya is text-only, 512 tokens
per question; vendor vs-Jev tables are claims. Their own zero-shot ECE
jump is the warning that matters (`research/notes.md` §18). Name the
provider on the decision-design card and falsify on *your* labels.
A CPU-distilled clone trained on Jev's *answers* (openjev-lm) is still a
teacher-copy. Read its two numbers separately: 92.9% is against 70
hand-labelled rows (one annotator, one domain, one seed), while the 98.1%
on fresh rows measures *agreement with the teacher*, not gold. Self-eval
on your own independent labels before you treat it as a decision API
(`notes.md` §25).

[jaredpalmer/kev](https://github.com/jaredpalmer/kev) is the laptop-local
System One **API drop-in** on that same open path: Qwen2.5-0.5B LoRA +
pointer, public gold not a Jev teacher, official SDK with a `base_url`
change. Hub weights: [`jaredpalmer/kev-0.5b`](https://huggingface.co/jaredpalmer/kev-0.5b)
(`notes.md` §45 delta). Use it for development and eval. Do not use 0.5B ID ECE as a
knowledge or frontier substitute (`notes.md` §45).

## Open weights vs Jev vs constrained decoding vs encoder vs LoRA?

Five surfaces, not one family (`judgment-class.md` when-to-use table).
Three *open* paths sit beside proprietary Jev: **encoder** open-jev
(DeBERTa, public gold), **AR constrained decode** (TypeAR; native
[pcdServer](https://github.com/stephanj/pcdServer) GGUF serving),
**trained decision-only** (Laya / Nimble / **kev** / **blackwood-rlcd** /
Archer Watch). Proprietary Jev is the documented decision API; you do not hold the
weights, so checks around the boundary stay black-box
(`formal-methods.md`). A trained decision-only open head (Laya, kev,
openjev-lm, encoder DeBERTa, a LoRA student, **blackwood-rlcd**) copies the Choice / Score /
Noul *shape* and moves eval onto you. Distills trained on Jev's
*answers* (openjev-lm, jev-gate-student-b) are teacher-copies — read
agreement separately from gold. **kev** is not that distill: CE on
public labelled outcomes, pointer readout, isolation probes, ID ECE
0.065 (0.031 after temperature scaling) on 1,350 questions — still
self-eval, still not OOD (`notes.md` §45). Encoder open-jev
([DeBERTa-v3-large](https://huggingface.co/com-kotobalabs/open-jev-deberta-v3-large))
was trained on public gold, not Jev; in-domain ECE 0.022, OOD acc
0.854→0.690. Constrained autoregressive decoding (TypeAR; README names
SGLang; pcdServer is the native llama.cpp server for the same
objective) masks a pretrained generator so the next token stays in a
declared set — a different objective, so do not threshold that
distribution as a Noul. A short enum and a missing abstain option are
brittleness; compose with abstention and an allowlist gate
(`mappings.md` §2, §17, §18). Hume's announced open **decision-model**
(27B dense, multimodal, AU healthcare residency — not anti-TypeSafe)
is **WATCH** until weights, license, and evals exist (`notes.md` §31,
§33). Open multimodal *decide* that already shipped:
[blackwood-rlcd](https://huggingface.co/BlackwoodAI/blackwood-rlcd)
(CC BY-NC; not that drop; `notes.md` §46). Constrained decoding is §32; native serving is §42. Decision-token QLoRA on that graph:
[Foodoo1/Qwen3-14B-RLCD-Decision-LoRA](https://huggingface.co/Foodoo1/Qwen3-14B-RLCD-Decision-LoRA)
(train the decision token, not prose; synthetic fraud receipt). Public logit dump for the
read-the-letter graph: mini-jev-runs. "Smarter than Jev" is a claim.
He prefers "decision models" over "system one"; this skill still quotes
TypeSafe's name for the exemplar. Before you pick any of those paths,
ask whether the decision needs a model at all (`mappings.md` §6).

## GLiNER vs GLiClass vs Jev vs a cross-encoder?

Hole first, logo last. These are **species**, not aliases
(`judgment-class.md`).

- **GLiNER (locate):** span/entity extraction. Answers "what's *in* the
  text?" Output is spans + types. Keep/drop over those candidates in
  code. Paper: [GLiNER](https://arxiv.org/abs/2311.08526). Local
  multi-head GLiNER2.5 (fastino-ai) can also classify and extract
  relations on a laptop — discourse, not a measured 36× (`notes.md` §25).
- **GLiClass (categorize):** one forward pass over text + *all* labels;
  sigmoid multi-label or softmax single-label. Use for large or changing
  tag sets. Scores are class affinities, not automatically a gateable
  P(permit). Paper: [GLiClass](https://arxiv.org/abs/2508.07662).
- **Jev / open decision head (decide):** calibrated Choice/Score/Noul
  when you need act/abstain, fan-out, and a documented envelope. Option
  limits (e.g. 255-way Choice) are Jev's, not the class's. Distilled
  open heads (openjev-lm, jev-gate-student-b) copy the *teacher*, not
  independent gold. Encoder open-jev (DeBERTa) is the same *shape* on
  public gold — still self-eval, especially OOD. **kev** is the
  causal-decoder + pointer productization of Archer's reconstruction on
  public gold (API-compatible; not a teacher-copy). **blackwood-rlcd** is
  the open multimodal decide head (CC BY-NC; not Archer Watch). Hume's 27B drop is
  Watch. When-to-use axes: `judgment-class.md`.
- **Cross-encoder / listwise ranker:** order of a retrieved shortlist.
  Fail **open** (keep retrieval order). Translation-invariant listwise
  losses are not calibrated for thresholds
  ([listwise vs pointwise](https://arxiv.org/abs/2208.06164)).

A listwise reranker *plus* a decision gate is a valid mixed stack. A
listwise reranker *as* the gate is the rejected design. A GLiNER span
that *authorizes* an irreversible act is the same rejected design.
Discourse this hour ("classifiers are cheap — jump on GLiNER") is the
species map, not a stack replacement and not "discard Jev"
(`notes.md` §42).

**Trolley test (Empirical, Han Xiao 2026-09-18):** a Jev-shaped API on
jina-reranker-v3.5 always pulls the lever, 1 death or 1B
([tweet](https://x.com/hxiao/status/2100973209114075330)). Retrieval
relevance is not decision rationality. Do not ship that as System One.

## Is GLiGuard Jev?

No. One forward pass over a safety schema is the same *interface shape*
as batched System One questions and a different objective (moderation
labels on a GLiNER2 encoder, not Choice / Score / Noul). Empirical open
encoder next to GLiClass; not a weight clone. "like jev" is discourse.
A GLiGuard score is not a proof. LLM I/O safety is not a coding-agent
tool gate (rh-guard for reward-hacking; jevgate shape for allowlist
∩ remainder; Abide for project soft rules on diffs). `judgment-class.md`.

## Can I threshold CLIP / SigLIP as a safety gate?

Not without calibration on *your* labels. CLIP-family softmax is
competition inside the offered prompt set; SigLIP's pairwise sigmoid is
an affinity, not class-conditional p
([SigLIP](https://huggingface.co/docs/transformers/v4.39.2/en/model_doc/siglip)).
A VLM asked "is this safe?" is *generation* — verbal scores are not
calibrated. Prefer pixel-free state (AX tree / detector boxes) and a
closed region/label Choice, or treat vision as the vision-scorer family on
`judgment-class.md`. Do not caption the world and then "run Laya on the
caption."

## Is this skill only for software engineering?

No. The placement question is the same in AI, SWE, business, knowledge
work, and life: what is exact, what is a narrow judgment, what is
generation, what is a proof-shaped constraint. Formal methods are one
pillar. Expected utility, abstention, VOI, MCDA, signal detection,
search/control, and Leveson org/safety are the others
(`mental-models.md`). Policy (checklist, ledger, two-person rule) is
the code of a practice that has no repository. Hypothesis cards for
VOI, ROC, Leveson, search/control outside SWE, spec pipelines, Alloy
loops, RV sandwiches, DST triage, durable agents, assignment hybrids,
situated density, paraphrase stability, allowlist ∩ remainder, and
effect-oriented loops: `mappings.md` §6–§19 — promote only with an
acceptance test that ran.

## Alloy Analyzer or Apalache?

Different languages, different claims, same harm if you launder a bound.
Alloy's Analyzer is a **model finder** (SAT, finite *scope*, relational
structure). Apalache is a **symbolic model checker** for TLA+ (SMT;
modes: some traces ≤ k, all traces ≤ k, or inductiveness for unbounded
safety *if* the invariant holds). TLC enumerates TLA+ states explicitly.
A System One Noul does not sit in any of those seats. It may triage
counterexamples. Full split: `formal-methods.md` §2.

## Is PufferLib "real DST"?

It is the third member of the DST *trio on this card*, not a fourth
owner and not Antithesis. Antithesis wraps existing software in a
deterministic hypervisor. Resonate HQ is **durable async execution**
(Distributed Async Await) with Lean spec + oracle + DST of an SDK —
not an unrelated "Resonate AI" brand; promises settle in protocol.
PufferLib's world is already a simulator: seeded serial
vectorization and Ocean sanity envs test the *trainer contract*; a seed
does not make GPU training bitwise deterministic; Ocean scores are not
a comparative baseline (authors). Judgment may cluster failing
episodes. It may not vote that the policy is correct.
`formal-methods.md` §4. One-screen: `formal-semi-formal.md`.

## Can a System One model replace TLA+ / Dafny / DST?

No. Model-checkers and provers exhaust a *model* or a *fragment*.
DST searches executions under a deterministic scheduler. A
judgment-class model estimates a *state*. Those are three owners
(`formal-methods.md`). Valid mixed stacks: TLA+ on the protocol + DST
on the SDK + judgment triaging failing seeds. Invalid: "formally verify
this agent with Jev." If removing the judgment call would change what
the system is allowed to do, the design is wrong.

## Isn't a high-confidence Noul basically a proof?

No. That is soundness theater. Calibration describes groups,
in-distribution. A stale Noul is **TOCTOU-of-Noul**, not an interlock
(judge at t0, act at t1; the check was never atomic because it was
never a check). An LLM-written spec plus "does this spec look good?" is
double theater; an MCP that "ran the checker" on a tautology is receipt
theater ([Hillel Wayne, vibing
specs](https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications/)).
The checker, DST harness, or prover ran *a non-vacuous property*, or it
did not.

## Is Augustus another Jev how-to?

No. `typesafe-ai` owns Jev API contracts. `tenbin` owns design-time
lint/measure. `decision-first` owns try-a-typed-decision-first habit.
Augustus owns **where judgment belongs** — in software *and* outside it —
which *pillar* and *family* map, what that does to a control loop, where
proof/DST still own the claim, and what would prove the design wrong. If
the request is a curl body or an SDK snippet, stop and load the family's
own skill/docs (`typesafe-ai` for Jev). If it is "replace TLA+ with Jev",
load `formal-methods.md` (one-screen: `formal-semi-formal.md`). If it is
hiring, inbox, reading list, or org safety, load `mental-models.md`.

## Is Jev a drop-in for LLM-as-judge (Langfuse etc.)?

When the eval output is a **typed decision** (Choice / Score / Noul), a
judgment-class model is the right *species* of judge — it cannot write
sentences, and that is the point
([Langfuse framing, 2026-09-18](https://x.com/langfuse/status/2100980004678971491)).
When you need a paragraph rationale, a trace UI, or an annotation
workflow, generation and the eval platform still own those seats.
Verbal LLM scores are uncalibrated. The Harbor/jevals-adjacent
practice is: shadow mode + fixtures that assert on the **action**,
not on prose (`jev-harness`, `validation.md`; `notes.md` §44). Shared
bake-off this hour scores **ECE / NLL / Brier**, not an LLM paragraph
([open-jev-laya-bench](https://huggingface.co/datasets/pngwn/open-jev-laya-bench);
`notes.md` §46). Do not
thin this skill into a Langfuse how-to. Mixed architecture: traces stay; the judge step can
be a System One model.

## Allowlist first, then Jev?

Yes, when code (or a recipe, a law, a text layer) can *prove* the easy
cases. jevgate's Proven / Refused / Unknown sandwich is the SWE shape;
OCR page-routing is the same composition with dollars attached
(`mappings.md` §18). The model judges leftovers. Putting the model
first so a comment can talk it into a write is the rejected design.
The same three-way test, one hour later: if a regex, a DNS lookup, or a
database query already answers, **do not call a model**
(`wotai-dev/typesafe-jev-tools`, `notes.md` §42). That is meta-VOI, not
a hook tutorial. This hour's wording of the same sandwich: the allowlist
**proves** read-only verbs; Jev judges only unlisted leftovers;
fail-open (cannot block) (`notes.md` §46). Same family, different
remainder: a **linter proves** lintable rules; [Abide](https://github.com/coldteadotai/abide)
Scores residual soft AGENTS.md / CLAUDE.md rules; fail-open, banded
(`notes.md` §47). Soft judgment is never the sole hard veto.

## Soft project rules — Jev or the linter?

The linter owns what it can prove. Soft instruction-file rules
("no helper with one caller", "don't add what wasn't asked") are
residual judgment. Same layering as jevgate: structure first, typed
Score only on the remainder; **fail-open**. Name the observation
window (edit vs turn). Fix false positives in the rubric, not the
model. Productized path: [Abide](https://github.com/coldteadotai/abide);
earlier contract pointer: jev-pref. Complementary, not the same
product: [rh-guard](https://github.com/24601/rh-guard) (reward-hacking /
eval integrity). Request-shape lint still sits upstream (wellposed /
`tenbin`). `mixed-architecture.md`; `question-design.md`; `notes.md`
§47.

## Can confidence gating catch a forced wrong Choice?

No. Choice probabilities are conditional on the offered set. If coverage
is open and you omit `other`, the model must pick a listed option — and
the distribution can peak at **1.00 on the wrong label**. Downstream
confidence gates see a healthy answer. Lint the *request* (missing
escape hatch, broken state paths) before you trust the number. Recipe:
[wellposed](https://github.com/suraj-phanindra/wellposed) (unsubscribe
email → `"support issue"` at 1.00 without `other`; overlapping options
collapse to 0.19 — that failure is loud). `tenbin` still owns the
design-time lint *skill*; Augustus owns the placement.
`question-design.md`; `notes.md` §46. Putting `"other"` on the request
is necessary and not sufficient for an open head you train: the
residual option must also appear as a **wrong** alternative, with
varied wording, or the hatch becomes a shortcut
([kev](https://github.com/jaredpalmer/kev) first-run lesson;
`none_of_the_above` eval; `notes.md` §45 delta).

## Should Jev live inside the database?

The *hole* is a semantic index over a structured store: cheap exact
predicates first, typed questions on the remainder. Two serving
choices, same hole (`mappings.md` §4; `notes.md` §44):

- **In-engine extension** (`sqlite-jev`; cousin `pg-jev`): SQL sees
  `jev()` / `jev_rows`. Convenient. The database process now has an
  API key, a spend guard, and a residency problem.
- **Out-of-process CLI** (`jevql`): vanilla Postgres never sees
  `jev()`. The rewrite layer owns the call.

Neither is an index. Full-scan the post-filter remainder. Row contents
leave the store. zoxide/`joxide` is the same hole over paths. Do not
copy SQL.

## Can Jev pick the bitrate, the join order, the model?

Yes as a **proposal inside a hard envelope**, no as the actuator.
bitrate-advisor: Jev may only match the deterministic cap or be more
conservative; missing the model returns the policy's answer.
mmalisper's JOB planner: Postgres plans first; Jev overrides only when
confident (+12% geomean author-reported; join-order Choice alone was
2× slower). routeKit / jev-claw / Higgsfield: classify requirements;
code picks the generator. The envelope is load-bearing
(`mappings.md` §12, §15, §18).

## Wait for Archer to ship omni System One?

No. Archer's 27B dense drop is still **Watch** (no Hub weights this
pass; user watch ~2026-09-19). Omni perception→decision already has an
open model: [`BlackwoodAI/blackwood-rlcd`](https://huggingface.co/BlackwoodAI/blackwood-rlcd)
(CC BY-NC; Jev-compatible shim; screenshot + marked candidates →
Choice). Soft judgment over pixel candidates inside deterministic
code. Jev still leads general *text* (0.850 vs 0.786 on their 8,456-item
table). Specialist composition (SAM / OCR → text → Jev) remains valid.
Do not wait, and do not treat screenshot-vs-Jev-text as the same input.
`judgment-class.md`; `notes.md` §46.

## Is confidence a trained score?

No — not on Hume's reconstruction, and not as a new contract. Re-read
live TypeSafe confidence docs before you code a threshold. Training
(published name: RLCD) is aimed at the predictive distribution; which
proper scoring rule he did not observe. The Choice `confidence` field, in
the adapter revision he cites, is then ordinary arithmetic: how far the
leading probability sits above a uniform `1/K`. It is not a second learned
estimate that the answer is correct. A peaked distribution can be
confidently wrong. Threshold a p you have checked on your labels.
[Essay](https://archerhume.com/posts/jevs-architecture-unmasked/),
`notes.md` §31, `mental-models.md` calibration.
