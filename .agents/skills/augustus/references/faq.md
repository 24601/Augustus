# FAQ (design judgment, not an API)

Load this when the request is skepticism, stack replacement, or "isn't
Augustus just another Jev skill?" Integration contracts still live in
`typesafe-ai` and the live docs. Typed judgment provider = TypeSafe Jev
by default, or an open Choice/Score/Noul head you self-eval.

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
calibrated decision primitive inside software that already has a generator
and a control loop. Full placement: `mixed-architecture.md`.

## Should we replace the LLM / the stack?

No. Default is mixed architecture: code owns control, the judgment provider
estimates, the LLM writes. Replace *classifier steps*, not the agent. A
loop with no LLM is still mixed architecture when nothing needs writing
(candidates from code; answers located, not composed). The day the task
needs a paragraph, the generator re-enters.

## Jev or Laya (or some other open head)?

TypeSafe Jev is the documented default (live docs, 64k/32k envelope). An
open head with the same Choice/Score/Noul shape is a **provider
substitute**, not a different methodology. Open weights buy self-hosting
and transfer calibration/eval duty to you. Laya is text-only, 512 tokens
per question; vendor vs-Jev tables are claims. Their own zero-shot ECE
jump is the warning that matters (`research/notes.md` §18). Name the
provider on the decision-design card and falsify on *your* labels.

## Is Augustus another Jev how-to?

No. `typesafe-ai` owns API contracts. `tenbin` owns design-time
lint/measure. `decision-first` owns try-a-typed-decision-first habit.
Augustus owns **where judgment belongs**, which classical method maps, and
what would prove the design wrong. If the request is a curl body, stop and
load `typesafe-ai`.
