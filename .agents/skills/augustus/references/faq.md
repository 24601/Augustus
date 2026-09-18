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
in the class — open System-1 heads (Laya, openjev-lm), GLiNER/GLiClass
encoder family (locate vs categorize vs local multi-head), listwise/pairwise
rankers, vision scorers — are substitutes or cousins. Pick the family
from the hole, then the vendor (`judgment-class.md` species map).
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
A CPU-distilled clone of Jev's *answers* (openjev-lm 92.9% on 70 gold)
is still a teacher-copy — self-eval on independent labels before you
treat it as a decision API (`notes.md` §25).

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
  open heads (openjev-lm) copy the *teacher*, not independent gold.
- **Cross-encoder / listwise ranker:** order of a retrieved shortlist.
  Fail **open** (keep retrieval order). Translation-invariant listwise
  losses are not calibrated for thresholds
  ([listwise vs pointwise](https://arxiv.org/abs/2208.06164)).

A listwise reranker *plus* a decision gate is a valid mixed stack. A
listwise reranker *as* the gate is the rejected design. A GLiNER span
that *authorizes* an irreversible act is the same rejected design.

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
and situated density, paraphrase stability, and allowlist ∩ remainder:
`mappings.md` §6–§18 — promote only with an
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
Verbal LLM scores are uncalibrated. Do not thin this skill into a
Langfuse how-to. Mixed architecture: traces stay; the judge step can
be a System One model.

## Allowlist first, then Jev?

Yes, when code (or a recipe, a law, a text layer) can *prove* the easy
cases. jevgate's Proven / Refused / Unknown sandwich is the SWE shape;
OCR page-routing is the same composition with dollars attached
(`mappings.md` §18). The model judges leftovers. Putting the model
first so a comment can talk it into a write is the rejected design.
