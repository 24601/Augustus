# FAQ (design judgment, not an API)

Load this when the request is skepticism, stack replacement, family
choice ("Jev vs GLiClass vs CLIP"), "formally verify with Jev", or
"isn't Augustus just another Jev skill?" Integration contracts for
TypeSafe Jev still live in `typesafe-ai` and the live docs. The *class*
of providers is `judgment-class.md`: Jev is the exemplar, not the
monopoly. Proof vs judgment ownership: `formal-methods.md`.

## Isn't this just classification?

Yes. Classification is the oldest AI task. Agree, then answer the design
question: **where does a typed judgment beat ad-hoc LLM-classify, and
where does it lose?**

It wins when software needs a schema-valid enum/bool/level; when you will
threshold, abstain, or re-policy from a distribution; when many independent
questions share one state; when per-line / per-hunk / per-message judgments
were known methods that were too expensive; when policy must be reviewable
in code.

It loses to a regex or lookup that already works; to a trained classical
classifier on a stable labeled taxonomy with enough of *your* data; to
open-ended writing, counting, date math, and multi-hop derivation; to
treating in-distribution ECE as a license to skip a held-out test.

The product is not "we invented classification." The product is placing a
fast, cheap scoring primitive inside software that already has a generator
and a control loop — and matching the model's *objective* to the action's
fail policy. Full placement: `mixed-architecture.md`. Families:
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
in the class — open System-1 heads (Laya), GLiClass-adjacent encoder
classifiers, listwise/pairwise rankers, vision scorers — are substitutes
or cousins. Pick the family from the hole, then the vendor
(`judgment-class.md`). `typesafe-ai` still owns *Jev* contracts; other
families own their own cards/READMEs. This skill does not become their
install guide.

## Jev or Laya (or some other open head)?

TypeSafe Jev is the documented default (live docs, 64k/32k envelope). An
open head with the same Choice/Score/Noul shape is a **provider
substitute**, not a different methodology. Open weights buy self-hosting
and transfer calibration/eval duty to you. Laya is text-only, 512 tokens
per question; vendor vs-Jev tables are claims. Their own zero-shot ECE
jump is the warning that matters (`research/notes.md` §18). Name the
provider on the decision-design card and falsify on *your* labels.

## GLiClass vs Jev vs a cross-encoder?

Hole first, logo last.

- **GLiClass-adjacent**: one forward pass over text + *all* labels;
  sigmoid multi-label or softmax single-label. Use for large or changing
  tag sets. Scores are class affinities, not automatically a gateable
  P(permit). Paper: [GLiClass](https://arxiv.org/abs/2508.07662).
- **Jev / open decision head**: calibrated Choice/Score/Noul when you
  need act/abstain, fan-out, and a documented envelope. Option limits
  (e.g. 255-way Choice) are Jev's, not the class's.
- **Cross-encoder / listwise ranker**: order of a retrieved shortlist.
  Fail **open** (keep retrieval order). Translation-invariant listwise
  losses are not calibrated for thresholds
  ([listwise vs pointwise](https://arxiv.org/abs/2208.06164)).

A listwise reranker *plus* a decision gate is a valid mixed stack. A
listwise reranker *as* the gate is the rejected design.

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
in-distribution. A stale Noul is a TOCTOU-shaped soft check, not an
interlock. An LLM-written spec plus "does this spec look good?" is
double theater ([Hillel Wayne, vibing
specs](https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications/)).
The checker, DST harness, or prover ran, or it did not.

## Is Augustus another Jev how-to?

No. `typesafe-ai` owns Jev API contracts. `tenbin` owns design-time
lint/measure. `decision-first` owns try-a-typed-decision-first habit.
Augustus owns **where judgment belongs**, which *family* and classical
method map, what that does to agent architecture, where proof/DST still
own the claim, and what would prove the design wrong. If the request is
a curl body or an SDK snippet, stop and load the family's own
skill/docs (`typesafe-ai` for Jev). If it is "replace TLA+ with Jev",
load `formal-methods.md`.
