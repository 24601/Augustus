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
agreement separately from gold. **Domain-jev-maker** is also not that
distill: independent CLINC gold, soft targets; pick it when downstream
*reads* p, few-shot hosted when only argmax (`notes.md` §60). **kev** is not that distill: CE on
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
(CC BY-NC; not that drop; `notes.md` §46). A local `POST /v1/systemone`
drop-in ([jev-local](https://github.com/us/jev-local)) is a **surface**,
not a fourth path — default scorer is a stub until `hf` (`notes.md` §48).
[jeff](https://github.com/logan-markewich/jeff) is a GLiFormer encoder
behind the same wire (not a Jev replica; `notes.md` §60).
[sysone](https://github.com/hraness/sysone) is a loopback **router**,
not a scorer. Distinct name collision:
[sysone-help/sysone](https://github.com/sysone-help/sysone) is an
evaluation-model-first TypeScript SDK (predicate/classifier/rubric
as data; cancellable; never auto-retry; first adapter Jev via
Vercel AI Gateway). Do not merge the two (`notes.md` §60, §63).
Laya ONNX port: [laya-onnx](https://huggingface.co/Mattepiu/laya-onnx)
(do not copy the inherited vs-Jev table). Constrained decoding is §32; native serving is §42. Decision-token QLoRA on that graph:
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
  Compaction receipt: [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
  uses that local multi-head as **categorize** (retention action) plus
  **locate** (character-offset spans); code copies; not a summarizer
  (`notes.md` §50).
  Indexer cousin: [s1-graphify-indexer](https://github.com/GreyssonEnterprises/s1-graphify-indexer)
  uses GLiNER2 on the bulk of a repo graph and escalates an LLM only
  on the ambiguous tail **if the backend loaded**. GitHub one-liner
  10–50× is a **target, not a measured speedup** — table TBD
  (`notes.md` §51). Not a Noul.
  Computer-use receipt:
  [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
  uses GLiNER2 (`fastino/gliner2-multi-v1`, not 2.5) to **score among
  observed** a11y/DOM controls; code acts; not a screenshot model
  (`notes.md` §52). Same observe→score→act hole as Jev Ultrafast.
- **GLiFormer (encoder serving the System One *wire*):**
  [jeff](https://github.com/logan-markewich/jeff) on
  gliformer-large-v1 (400M) answers choice/score/noul at
  `/v1/systemone`. Related Knowledgator encoder lineage, **not**
  GLiNER locate and **not** a Jev replica. Cheaper on GPU,
  less accurate on reasoning-heavy; CPU is *more* expensive.
  `notes.md` §60.
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
  public gold (API-compatible; not a teacher-copy). **Domain-jev-maker**
  is a domain LoRA on independent CLINC gold (not a teacher-copy) —
  train when downstream reads p; few-shot hosted when only argmax.
  **blackwood-rlcd** is
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
∩ remainder; Abide for project soft rules on diffs;
gliner25-compaction for extractive context compaction — Fastino
sibling class, not GLiGuard;
gliner2-ultrafast for scoring observed browser controls — GLiNER2,
not 2.5, not a safety schema). `judgment-class.md`.

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
eval integrity). Plain-English PR check:
[if-ai](https://github.com/Victor-Casado/if-ai) (one condition +
required min-confidence; fail-closed on error). [jev-marshal](https://github.com/LightningK0ala/jev-marshal)
is Watch / empty this pass. Request-shape lint still sits upstream (wellposed /
`tenbin`). `mixed-architecture.md`; `question-design.md`; `notes.md`
§47, §51.

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
code picks the generator. Compaction cousin (encoder, not Jev):
gliner25-compaction — mutating tools / shell operators prove
`keep_full`; the model may only match that or be more conservative;
uncertain fails closed to `keep_full`. The envelope is load-bearing
(`mappings.md` §12, §15, §18; `notes.md` §50).

## Wait for Archer to ship omni System One?

No. Archer's 27B dense drop is still **Watch** (no Hub weights this
pass; user watch ~2026-09-19). Omni perception→decision already has an
open model: [`BlackwoodAI/blackwood-rlcd`](https://huggingface.co/BlackwoodAI/blackwood-rlcd)
(CC BY-NC; Jev-compatible shim; screenshot + marked candidates →
Choice). Soft judgment over pixel candidates inside deterministic
code. Jev still leads general *text* (0.850 vs 0.786 on their 8,456-item
table). Specialist composition (SAM / OCR → text → Jev) remains valid.
Do not wait, and do not treat screenshot-vs-Jev-text as the same input.
Pixel-free computer-use (DOM/a11y candidates → score → code acts) does
not wait either: [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
is that hole with a local encoder (`notes.md` §52).
`judgment-class.md`; `notes.md` §46, §52.

## When does a decision model hold?

When the answer is **extractable from the state you feed it**
(classification, citation/paraphrase/reversed-meaning with claim +
quote both given, sarcasm whose trigger is in the text, DOM-as-text
fan-out). It **fails, often confidently**, on recall without a
supporting passage. Atlas history suite (`notes.md` §49): Case A
wrong @ 0.90 with no context; Case B near-flat 0.07 (correct by luck);
Case C — same item as B — right @ 0.97 once the passage is in
`state`. Retrieve first. Overlapping categories can still be
**dangerous-high** (DAIR Emotion 48% acc / mean conf 0.819). Not a
leaderboard; one axis. `mental-models.md` §boundary.

## Are the internals a state machine?

No. Distributed LM understanding, not hand-written transitions
(paraphrase vs reversed-meaning contrast). **Placement** is a
component node in *your* code — that instinct is right; "it *is* a
state machine" is not. `mappings.md` §3; `mixed-architecture.md`.

## Decision model or a constrained LLM?

Neither class won on quality in DMB v2 (`notes.md` §49). Decision
models win the *axes you actually buy*: p50 ~264–276 ms, ~$0.07/1k
on banking, schema-valid, flat to 255 options — and **fail at 256+**.
Constrained LLMs handle 512 and (most of them) admit ignorance on
no-good items; they are slower and cost more. Spam: two OpenAI models
sat *below* the majority baseline. Re-run on *your* labels. Do not
merge Banking77 87% / 76.3% / 79.67% across protocols.
`judgment-class.md`; `validation.md`.

## Can many cell-wise Choices solve a combinatorial grid?

Not in the Direct Jev ARC-AGI-1 experiment: **4/400 (1%)**, ~$2.32.
Dimensions ~90%; complete grids rarely. Combinatorial assembly ≠
extractive keep/drop. Search or a program stays in code.
`mappings.md` §9; `notes.md` §49.

## Is a local `/v1/systemone` the same as Jev?

No — not until you know **which scorer** is behind the socket.
[jev-local](https://github.com/us/jev-local) is a **contract-compatible**
drop-in (`base_url`). The **default scorer is a deterministic stub**
and carries no intelligence. `JEVLOCAL_SCORER=hf` turns on a frozen-model
logprob scorer. Their README: an interface-compatible baseline, not a
reproduction of Jev's undisclosed model. kev is the other local
drop-in (trained pointer head, public gold). [von](https://github.com/wfzyx/von)
is a **tiny SAN** (14 MB needle; authored144 52.6%) at the extreme of
the speed/econ class — not the stub, not kev, **not a calibrated Jev
replica**. Do not copy its vs-Jev table.
[open-alternative-jev](https://github.com/ikermoel/open-alternative-jev)
packs one-forward logprobs on an open LLM you already have (RACE-H
92.9% @ 4.55 q/s); **not a Jev reproduction**.
[jevify](https://github.com/Mintzs/jevify) is a CUDA/PyTorch cousin
on Qwen2.5-1.5B (`ora_decision_engine`): CUDA graphs, branch kernels,
literal-label scoring. **Uncalibrated model likelihoods, not
measured correctness** — softmax over A/B/C is not a Noul. Independent
of Distillation. No LICENSE this pass. Default refund workflow is
not a validated policy. A green smoke test on
the stub is not a bake-off. `judgment-class.md`; `notes.md` §48, §49, §55.

**Independent `/v1/decide` (not this wire; 2026-09-19 ~04:39):**
[OpenJev](https://github.com/IamBusy/OpenJev) speaks a
**different** contract. 45/60 *theirs*. Not TypeSafe. Distinct
from hraness/sysone OpenJev runners.
[semif-serve](https://github.com/dddanielliu/semif-serve)
is another `/v1/systemone` surface (SemIf runoff; 1164 vs
178 ms *theirs*; wire-compat ≠ replica). `notes.md` §69.

**Wire-compat encoder cousin (2026-09-18 ~20:43):**
[jeff](https://github.com/logan-markewich/jeff) serves
`/v1/systemone` on GLiFormer-400M; `typesafe-sdk` drop-in via
base URL. **Not a Jev replica** — normalized sigmoids, T=3.2,
noul isolation default, DeBERTa token counts. Their card: L4
HTTP ~$2.6 vs jev ~$15.6 per 1M requests (~6×); A10G direct
~$0.65 (~24×); AG News 75.5% vs 90.5%. CPU arm is *more*
expensive. License null this pass. A loopback **router**
([sysone](https://github.com/hraness/sysone)) is not a scorer
either — it routes hosted + local OpenJev/NanoJev/Mini-Jev
and does not run weights. `notes.md` §60.

## Are local CUDA likelihoods a Noul?

No. [jevify](https://github.com/Mintzs/jevify) (and packed-logprob
cousins) return **uncalibrated model likelihoods**. Do not threshold
them as P(permit) or as calibrated abstention. Temperature / ECE on
*your* labels if you use the surface. Softmax over allowed tokens ≠
Noul. `judgment-class.md`; `notes.md` §55.

## Should RAG stop at Top-K / a reranker?

Not if the hole is **evidence**.
[decision-native-rag-skills](https://github.com/emergency-lee/decision-native-rag-skills):
retrieve wide → decide explicitly → evidence set → resolve conflicts
→ reason only over kept evidence. Embeddings stay candidate
generators. Provider-agnostic; no bundled harness; **no universal
benchmark**. Default migration gates are starting targets, not
promises. Do not ship because an LLM judge prefers it.
[jev-sift](https://github.com/kbhuw/jev-sift) is the same sandwich
on **agent I/O**: classify first, read selectively; content to Jev
without entering main agent context first (paths/URLs). Uncertain /
errors / truncation ≠ irrelevant. Transport tests ≠ accuracy.
`mappings.md` §4; `notes.md` §55, §56.

## Dump files into context, or classify first?

Classify first when the items are **not** already in the main agent
context. [jev-sift](https://github.com/kbhuw/jev-sift): batch path /
public URL / inline text → Jev; the main LLM opens survivors.
Uncertain → closer look; errors and truncation ≠ irrelevant. Inline
text the agent already read cannot recover that cost. Hard envelope
in code (50 / 60k / 2MB / public-IP). Transport tests ≠ accuracy.
Same family as decision-native RAG. Topology A MCP — not
jev-routing (host adapter). Do not copy plugin how-to.
`applied-mappings.md` §1; `notes.md` §56.

## Is jevable.com a 342-title census?

No. [jevable.com](https://jevable.com/) is a living **applied-mappings
atlas**: extract class patterns (intent columns, score-among-observed,
VOI gates, generative UI decide, robotics text-state, draft-gate fail
modes). The site claims **342** curated projects this pass; homepage
JSON-LD lists **36** (first page / `pageSize` 36). We did not enumerate
titles. Maker clocks stay **claims** unless already a named receipt.
Cross-link exemplars already in notes; do not dump a hit list. Not a
model. Not multimodal substrate. Archer still Watch.
`applied-mappings.md`; `notes.md` §56.

## Did Jev beat nano as an escalation gate?

Not in the pre-registered independent eval
[jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval)
(2026-09-18). **Both experiments AMBIGUOUS.** Cascade Δ +0.265 at a
1pp-below-frontier target; **at exact parity the sign flips**
(R_jev=1.000 vs nano 0.730) because Jev confidence is exactly 1.0 on
102/200 items including 6 wrong. AUROC error-ranking neither
direction established; **no ECE**. Encoder with labels wins Banking77
(0.933 / 9 ms). Recorded call duration ~2.2×, **serving-path not
model-speed**, not 40–200×. Same-day errata three rounds. This is
the jevals/Harbor practice exemplar this hour (honest negative +
calibration theater). `validation.md`; `notes.md` §55.

## Did Jev pay off for Precision PDF extraction?

Not in
[databricks-jev-pdf-lab](https://github.com/laurentfabre/databricks-jev-pdf-lab).
**No quality-equivalent, end-to-end Jev payoff demonstrated.**
Compact requests cut tokens but changed 26/236 recommendations.
**No OSS license selected.** Typed output is not truth. `notes.md` §55.

## Should the model write the quote / the citation / the click?

No. Extractive keep/drop: code already holds the sentences, line ids,
character offsets, or numbered controls; the model **selects**; code
**copies or clicks**.
[testimonial-miner](https://github.com/AppitStudio/testimonial-miner)
assembles quotes from per-sentence Nouls and `redecide`s without new
calls. **[choxos/jev-reviewer](https://github.com/choxos/jev-reviewer)**
(systematic-review Jev Reviewer; **≠** egma-ai) points at ids; *Not
found* is an answer; human tick never overwritten. [solari-reflex](https://github.com/hitakshiA/solari-reflex)
never lets model output become a selector. Compaction is the same
species: [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
copies exact source spans; a prose summary of the tool result is
generation, not keep/drop (`notes.md` §50). Command-output cousin:
[jev-pruner](https://github.com/tamaratran/jev-pruner) keeps verbatim
chunks of Bash stdout; dropped spans live in an archive, not a
summary (`notes.md` §53). Claim/evidence Stop:
[clear-head](https://github.com/VladyslavHontar/clear-head) judges
against retrieved session lines, not generated prose (`notes.md`
§51). Computer-use encoder
cousin: [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
scores observed controls; code clicks; no generated selectors
(`notes.md` §52). Specialist-form cousin:
[Cua-S1](https://github.com/trycua/cua/tree/main/libs/cua-s1) selects
fill/check/click/skip among observed elements; does not generate
values or selectors (`notes.md` §54). Generation is only for
TYPE/prose when something must be written. `applied-mappings.md` §2;
`notes.md` §48, §50, §52, §53, §54.

## Should compaction summarize?

No. Pointer/extractive compaction and generator summarizers are
different species. The former is auditable (every kept byte occurs in
the input). The latter can invent. Same job as
fast-jev-compaction / pi-jev-compaction (Jev Noul/Score backends);
GLiNER2.5 is an encoder backend. Mutating tools and shell operators
stay `keep_full` in **code**. Low-confidence / invalid evidence fail
**closed to `keep_full`** — the *reduction* is the irreversible act,
unlike Abide / jevgate fail-open. Ship `shadowMode` first (default
true: log, do not replace history). Not Jev. Not multimodal.
Stdout prune is the same *family* (evidence-preserving reduce) on a
**different job**: [jev-pruner](https://github.com/tamaratran/jev-pruner)
Noul-prunes a just-run Bash result before the main LLM sees it;
fast-jev-compaction / gliner25-compaction compact completed tool
pairs already in history. Hard ≤10k / JSON-diff-whole-doc envelope
in code; fail-safe keep original; archive for recovery. Marketplace
id still `fast-jev-output`. Framework-agnostic middleware cousin:
[jev-compactor](https://github.com/edwardyen724-g/jev-compactor)
— **Jev judges relevance. Code decides structure.** Never rewrite.
Regex floor in code. Compaction fails open if Jev is down; safety
gate fails closed on pending destructive/exfil. One-session
*theirs*: later product-arm table **73%** / 350 ms /
$0.0004 / 4 of 4 vs shipped summarizers (30–250× cheaper);
earlier vs-Sonnet card 64.5% / 366 ms (`notes.md` §65).
Claude Code shorter path remains fast-jev-compaction.
`judgment-class.md`; `notes.md` §50, §53, §65, §68.

## Is pruning Bash stdout the same as compacting session memory?

No. Same family (pointer, not summarizer; dropped bytes recoverable).
Different job. [jev-pruner](https://github.com/tamaratran/jev-pruner)
scores chunks of a command that just ran, *before* they enter the
generative turn. [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)
and [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
reduce completed tool pairs already in session history (Jev Noul vs
GLiNER2.5 encoder). Host capability shapes the product: Claude wraps
Bash automatically; Codex is an opt-in wrapper because it cannot
replace native shell output from `PostToolUse`. `applied-mappings.md`
§1; `notes.md` §50, §53.

## Fail-open or fail-closed — which?

Name the **irreversible act**, then pick polarity. Compaction *drop*
fails closed to `keep_full`. Stdout *prune* fails closed to original
output ([jev-pruner](https://github.com/tamaratran/jev-pruner):
archive/Jev/incomplete-score failure keeps the log; Harbor plugin-eval
cannot reach Jev and therefore cannot prune). Wake *skip* fails open (wake on error /
unsure): [wakegate](https://github.com/shitianfang/wakegate) skips
only if Jev answers and p(wake) < 0.2. Merge *PASS* on a red run
fails closed at the gate: [latch](https://github.com/CaseReed/latch)
`--gate` BLOCKs unless infra is confirmed; the Playwright reporter
stays fail-open. [if-ai](https://github.com/Victor-Casado/if-ai)
fails the Action on error / empty / low confidence. jevgate cannot
block; pi-jev-approver fails closed without a key; Abide is fail-open
on diffs. Session-memory *omit* fails open (dump the ledger):
[carryforward](https://github.com/Dharundp6/jev-carryforward).
Tool *execution* fails closed on block/timeout:
[toolgate](https://github.com/fdemir/toolgate) (Jev is not
authorization). OMP/pi
[omp-jev-extensions](https://github.com/luw2007/omp-jev-extensions)
**fail open** (`confidence: 0`) if Jev is missing — contrast
pi-jev-approver fail-closed without a key. Ruby validations in
[hunch](https://github.com/carldaws/hunch) `rescue nil` at save —
spam gates should not. Draft-gate *silence* is the same rule:
missing verdict is not a block and not a pass — fail-open /
heartbeat, do not hold forever ([jevable.com](https://jevable.com/)
class pattern). Contrast Abide `<0.5` silence (the *edit proceeds*).
Same sandwich, opposite authorized act.
`notes.md` §50, §51, §53, §55, §56, §58.

## Type-safe or correct?

Typed answers are not a safety case.
[interlock](https://github.com/somoore/interlock): type-safe ≠
correct; irreversible stays behind a threshold **and** a human.
Secrets never enter the agent. Jev is a SENSOR; `policy.py`
decides BLOCK/ASK/ALLOW. A launch-week firewall that asks
"dangerous?" after the LLM already decided, with real secrets in
scope, is the named anti-pattern. Distinct from
[toolgate](https://github.com/fdemir/toolgate) (pre-exec of a
proposed call). Atlas receipts make the same split a
**measurement** claim: schema-valid (cannot emit off-list)
≠ picked-right (DAIR Emotion 48% at mean conf 0.819).
`mappings.md` §8; `applied-mappings.md` §7;
`notes.md` §59, §49, §66.

## Is Jev the policy?

No. Jev is the sensor. Policy (checklist, ledger, `policy.py`,
two-person rule, human confirm) is the constraint. Interlock:
the model never picks allow/ask/block.
[port-cleanup](https://github.com/epiphany-dynamics/port-cleanup):
the human is the only kill trigger; shields override; displayed
explanations are app-owned mapped text, not raw model prose.
`notes.md` §59. Same split: [omp-greenlight](https://github.com/SemetricLabs/omp-greenlight)
is permission vs probability (operator owns the bar); [skill-broker](https://github.com/adamjralph/skill-broker)
outline is judgment ≠ permission (Jev never grants access).
`notes.md` §62.

## Is Jev authorization?

No. Jev is a probability, not a grant.
[toolgate](https://github.com/fdemir/toolgate): pre-exec
allow/block/review; Jev is not authorization.
[omp-greenlight](https://github.com/SemetricLabs/omp-greenlight):
suppresses an OMP approval prompt when Jev says allow —
**permission vs probability**. Operator owns the bar; the
plugin never self-tunes it. Host `bash.patterns: deny` stays
the floor. Default **40.9%** prompts removed / **0 of 94**
unsafe auto-approvals on the labelled corpus (not live
traffic). Not a sandbox. Composes with waymode and
omp-jev-extensions. `applied-mappings.md` §5, §7;
`notes.md` §62.

## Does Jev grant skill access?

No. Judgment ≠ permission.
[skill-broker](https://github.com/adamjralph/skill-broker)
is a **project-outline** (not a production recipe):
deterministic code owns catalog, policy, limits, and
grants; Jev scores relevance/confidence and **never grants
access**. Candidates ≠ grants. Jev down → foundation-only;
never broaden access. Distinct from shipped routers
(jev-hermes, GodsBoy, omp-jev-extensions).
`applied-mappings.md` §5; `notes.md` §62.

## Is the Jev score the eval?

No. Check the instrument, not just the score.
[dinostomp](https://github.com/collapseindex/dinostomp)
audits data, scorer, runs, numbers, claims, and itself.
`dinostomp jev` tests a Jev question like an if-statement
(accuracy, p(yes) cut, ECE, blank lean, rewording). Demo
*theirs*: 24 examples, ECE **0.062** — not a class ranking.
FINDINGS 189; 99 against itself. Cousin of rh-guard /
egma attention≠correctness / game-coach engine-owns-truth.
Beside jevals, not a Harbor taskset. `validation.md`;
`formal-methods.md`; `notes.md` §62.

## Is Jev the sole hard gate on the hot path?

No. Put System One on the **feature side of a constrained
optimizer**, never as the only gate that must answer before
traffic moves.
[slo-router](https://github.com/zeeshan8281/slo-router):
Jev supplies task / exactness / external-evidence; code
picks the cheapest backend meeting quality + SLO floors.
Fail-open to local features on timeout/invalid. Measured
*theirs*: same routes/accuracy as the local path; p95
**77.93 → 490.38 ms**. Exactness raises the quality floor;
it must not override capability/context. **Hunch:** Harbor-
style measurement of decision-model latency is mandatory
before claiming “Jev routing.” Eight-row demo is not a
benchmark. `mappings.md` §6, §15; `notes.md` §63.

## Is privilege the verdict?

No. Privilege changes blast radius, not whether the act is
benign.
[construct-auto-classifier](https://github.com/godspede/construct-auto-classifier):
`sudo status` can be a safe read. Fast structural rules,
then Jev Choice + independent risk Nouls. Operator owns
`minConfidence` / `riskThreshold`. Fail-closed.
Certification *theirs*: Jev **0** dangerous / 975; every
chat model leaked. **Landed-script trust** (byte-identical
to the remote default branch) is a merge-gate receipt, not
a name. **Headless ≠ auto-approve.** Pair with dinostomp and omp-greenlight.
`applied-mappings.md` §7; `mappings.md` §18; `notes.md` §63.

## Is System One a permission gate for human review?

No. It can be an **attention filter / VOI** that never
blocks the agent and never says green unless sure.
[jev-lens](https://github.com/rashedInt32/jev-lens):
calibrated “do I need to look / which files / strip
debris?” Never edits files. Companion
[jev-lens.nvim](https://github.com/rashedInt32/jev-lens.nvim)
is a popup, no API key. Complements skill-broker (Jev
never grants access) and omp-greenlight (operator owns the
bar). Distinct from
[jev-gates](https://github.com/rashedInt32/jev-gates)
(stops writes). **Hunch:** minimize expected human cost
under false-green risk. `notes.md` §63.

## Are the two `jev-lens` repos the same product?

No. Qualify the owner.
[rashedInt32/jev-lens](https://github.com/rashedInt32/jev-lens)
is a Stop-hook **human** attention filter (never blocks
the agent). [dizk/jev-lens](https://github.com/dizk/jev-lens)
is **pre-send view selection** of tool results (79% fewer
tokens on 500 SWE-rebench trajectories *theirs*).
Compress-before-first-send beat post-send prune (cache
cost +17%). `notes.md` §63, §68.

## Is a Stop-hook risk score a merge blocker?

No. [jev-preflight](https://github.com/muse0509/jev-preflight)
redirects the agent's attention for at most one
reinspect, then finishes. Fail-open. Uncalibrated 0.85.
Not tests, not SAST, not latch / ci-gatekeeper.
`notes.md` §68.

## Does exposing MCP tools mean the agent will recall?

No. **tools≠use.**
[carryforward](https://github.com/Dharundp6/jev-carryforward)
eval: `recall` **0/4** with tools + skill installed.
SessionStart hook injects rules; hoping the model reaches
for memory is not a design. `notes.md` §68.

## Is openvons TypeSafe Jev?

No. [openvons](https://github.com/genai-craft/openvons)
is an independent open-Jev *class* (LM/vision/voice;
NOTA; execute/confirm/reject). Apache-2.0 code; GitHub
SPDX NOASSERTION. Speaks `/v1/systemone` as
**wire-compat**, not a replica (same warning as jeff /
jev-local). JevPick is menu decode (3.2–4.8×
byte-identical *theirs*), not a Noul. Unrelated to
TypeSafe; no TypeSafe API output used. `notes.md` §68.

## Is OpenJev (IamBusy) TypeSafe Jev, or hraness/sysone?

No to both. [OpenJev](https://github.com/IamBusy/OpenJev) is
an independent 0.6B LoRA+scalar head. `/v1/decide` is **not**
a TypeSafe drop-in. Training is supervised CE, not RLCD.
[hraness/sysone](https://github.com/hraness/sysone) "OpenJev
runners" are a **loopback gateway**, not this model.
[semif-serve](https://github.com/dddanielliu/semif-serve)
is another `/v1/systemone` **wire** (SemIf runoff; 1164 vs
178 ms *theirs*); wire-compat ≠ replica. `notes.md` §69.

## Are the two Winnow repos the same product?

No. Always qualify the owner.
[kevinpita/winnow](https://github.com/kevinpita/winnow) is
the launch-week **context sieve** (hide agent artifacts).
[ThinkyMiner/Winnow](https://github.com/ThinkyMiner/Winnow)
is a Chrome **worth-your-attention** VOI filter (read /
skim / save / skip from typed answers; 80%/90% *theirs*).
`notes.md` §69.

## Can I skip the LLM when the intent is the same?

Yes, as a **fail-open** VOI admit — never as a silent
rewrite. [jevcache](https://github.com/kushals256/jevcache)
asks Jev `same_intent` after exact SHA-256; 0 FP / recall
0.38 on n=100 *theirs*. Stream/tools/multimodal bypass.
A cosine cache with Jaccard@0.35 had fpr 0.48 on the same
fixture. `notes.md` §69.

## Does a Noul distinguish conflict from ignorance?

Not by itself. [jev-typed-evaluation-collapse](https://github.com/mleyvaz/jev-typed-evaluation-collapse)
(NCML field note v0.3 *theirs*): the same evidence yields
Noul 0.50–0.57 (conflict) vs 0.46–0.48 (ignorance);
Choice with named `conflicting_evidence` /
`insufficient_evidence` separates at p=1.0; binary Choice
without an escape is lexically biased (red 0.67–0.85).
Schema-as-interface. Same family as missing-`other` →
confident wrong. `notes.md` §69.

## Does a typed baton grant the tool call?

No. [jev-handoff](https://github.com/shitianfang/jev-handoff):
gate `allow` **never grants** — only deny/ask. Control
returns as escalate / continue / abort. Fail-open. Inverted
loop wakes the LLM only on escalate. Vercel drops
confidence. `notes.md` §69.

## Jev WHETHER, Python HOW, LLM WHAT?

Yes as a split, not as a stack replacement.
[hermes-jev-router](https://github.com/rsdkrasen/hermes-jev-router)
(license null; community plugin): Jev decides whether the
next main-model call is worth it; Python keeps original
chunks and suppresses duplicate observational tools; the
LLM still writes when writing is required. Skip-next needs
a Hermes core patch. Fail-open. `notes.md` §69.

## Can I put a Noul on a lock or a heater?

No. [HA-Jev](https://github.com/AboveColin/HA-Jev)
explicitly: a probability with no explanation should not
hold a lock, a heater, or a smoke alarm. Typed answers
as sensors, confidence gating, Jev-gates-LLM cascades —
yes. Safety actuators stay in Home Assistant interlocks.
`notes.md` §68.

## Does measurement own endorsement?

Yes, for question packs (and any cookbook criteria).
[jev-packs](https://github.com/dtduc-git/jev-packs): a pack
is only `verified` after recorded accuracy / ECE / cost /
latency on a **pinned** model version. No numbers, no
endorsement; otherwise `provisional`. Abstention/`unknown`
is mandatory. Named runner
[jevassert](https://github.com/dtduc-git/jevassert)
**LANDED** this pass (Apache-2.0; was 404 in §64):
record once, `check` offline from recordings, exit 0/1/2.
Calibration and cost are first-class gates, not footnotes.
Harbor/jevals pattern for the class — never
cookbook-once-and-forget. Distinct from INSTRUCT_JEV
(docs-derived seed, no evidence gate) and dinostomp
(instrument). `validation.md`; `notes.md` §64, §70.

## Does a positive Jev score authorize the act?

No. **Jev supplies evidence. Code owns authority.**
[actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev):
deterministic policy / RBAC / schemas / limits own
ALLOW | REVIEW | BLOCK. A positive model score never
overrides a deterministic security failure. Six narrow
questions, never one vague "is this safe?" Financial /
destructive / credential fail closed if Jev is down.
500-case eval is label-baseline integrity, not accuracy.
Compose with construct (privilege ≠ verdict) and interlock
(SENSOR ≠ policy). `applied-mappings.md` §7; `notes.md` §64.

## Does "calibrated" mean I can threshold p as a frequency?

No. Ranking ≠ calibration.
[does-jev-confidence-mean-anything](https://github.com/Adilmp/does-jev-confidence-mean-anything):
8,000 human-annotated judgments; AUC **~0.91** while when
Jev said **~75%**, humans flagged **~10%**. Two-parameter
recalibration removes **~96% of ECE** without changing
rank. Vendor "Calibrated: higher confidence means higher
accuracy" is **true as rank-correlation** (0.96 *theirs*)
and **false as probability units**. Companion
[jevcal](https://github.com/Adilmp/jevcal) (~100 labelled
rows). Never `if p > 0.9` without domain recalibration.
One dataset; do not cite `threat`. `mappings.md` §7;
`notes.md` §64.

## Does AUC mean the probabilities are honest?

No. Ranking can be strong while units are wrong — and the
**sign of the error can flip by question type**.
[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration):
on 900 synthetic tickets Jev cannot have seen, Choice/Score
are overconfident (refit T ~3.3) while the boolean on the
**same** tickets is underconfident (T 0.66). The priority
label is an org rule **not in the text** (44.7% acc, mean
stated p 0.74). In-domain OpenBookQA looks almost honest
(ECE 0.024). Do not threshold the TypeSafe `confidence`
field. Complements does-jev-confidence. `notes.md` §66.

## Can I gate on Jev `confidence` alone?

Usually that is the **rosiest** reading of the vector.
[how-sure-is-jev](https://github.com/adarc8/how-sure-is-jev):
Choice `confidence` **is** rescaled max-prob
(`(p_max − 1/n) / (1 − 1/n)`), to 3 decimals on 60 live
answers *theirs*. A 2-option 75/25 is Jev **0.5** and
entropy **0.19**. Use margin / entropy / gini as named
features; bands CERTAIN|…|CLUELESS are **policy**. Pair
with OOD (do not threshold `confidence`) and
does-jev-confidence (ranking ≠ calibration). Zero-dep.
`notes.md` §67.

## Are combinators a new judgment model?

No. They are **control-plane primitives** over typed
judgments. [jev-combinators](https://github.com/voidning/jev-combinators)
is the **rename** of
[decision-combinators](https://github.com/voidning/decision-combinators)
(same repo): Then / Gate / Vote / Cascade / Weighted plus
extended Router / Loop / Retry / Fallback / Memory.
Digital-design slogan (transistors / logic gates / chip)
is a metaphor for *soft* classifiers; AND/OR aggregation of
parallel Nouls still lives in code (do not multiply).
Compose with [skillranker](https://github.com/Dicklesworthstone/skillranker)
(VOI over a skill library; abstention; hook fail-open).
Not chat turns. `composition-algebra.md`; `notes.md` §66,
§69.

## Does TLA+ replace Jev, or the reverse?

Neither. [jev-labs](https://github.com/copyleftdev/jev-labs)
puts TLA+ on the **protocol** (quorum, stability, crash)
and Jev on the **oracle**. The invariant is never
confidently wrong: escalate is allowed. 1,080 golden
rounds 0 wrong *theirs* bounds the violation rate below
0.28% (rule of three) — it does **not** prove zero.
Hard-gating a soft judgment without an escalation path
is soundness theater's inverse. Synthetic pharmacy, not
clinical. `formal-methods.md`; `notes.md` §67.

## Does a typed answer unlock the next step?

No. [seal](https://github.com/Reasonofmoon/seal): **Jev
answers questions; SEAL answers whether the world may
change.** Coverage.path ∈ {auto|code|human|escalate}
must be visible. Mint ≠ product brain. Generation fills
Candidates; only a Seal advances. `notes.md` §67.

## Is JevBench a TypeSafe leaderboard?

No. [jevbench](https://github.com/fstandhartinger/jevbench)
is Benchmark Heaven's unofficial v1.1 bake-off.
Calibration is **reported, not scored**. Native vs
verbalized are labelled. Partial runs are not ranked.
Main Score = 0.6 Capability + 0.2 Speed + 0.2 Cost
*theirs* (Jev 1.13.0 **87.6**). Contrast atlas
(receipts, not a ranking). Harbor/jevals practice, not
a vendor eval. `validation.md`; `notes.md` §67.

## Is Jev weaker than a 4B model?

Only with the **thinking budget** attached, on this set.
[jev-frontier-100](https://github.com/softpudding/jev-frontier-100):
Jev **77.0%**; Qwen3.5 4B with thinking off **56.0%**; at
512 **78.3%**; at 2048 **96.7%** (+12.7 to +26.7 pp).
Exploratory, not preregistered. Similar totals ≠ similar
skills. Not a ceiling. `notes.md` §66.

## Does a local MLX one-pass replica give Nouls?

No. [jevmlx](https://github.com/bnsd55/jevmlx) assembles
schema-valid JSON with a probability per field in one
forward pass on Apple Silicon. Softmax over allowed tokens
≠ a calibrated Noul. No local leaderboard yet. Distinct
from system-one-benchmark's Harbor Brier table
(PCD 0.3884 vs Jev 0.1096). `judgment-class.md`; `notes.md`
§61, §66.

## Does Jev `done` mean the browser task succeeded?

No. Code owns observe / execute / verify / exit.
[ego-jev](https://github.com/jiangkoumo/ego-jev): `--until` (URL
substring or a `check` function) is the deterministic success
condition; Jev self-`done` is weaker. Malformed fill JSON is
`text_model_failed`, not a guessed value. Same lesson as
`DONE` ≠ verified success (gliner2-ultrafast) and waymode
`completed` ≠ server-state success. `applied-mappings.md` §2;
`notes.md` §65.

## Should the model's own hides become training labels?

No. A feedback loop that auto-trains on the judge's own
negatives self-reinforces errors.
[x-reply-filter](https://github.com/zhuyansen/x-reply-filter):
local rules first; remainder Nouls; auto-collapses sit in a
confirm queue until a human says hide or keep. Distinct from
distilling Jev as teacher of record (jev-triage ~68% ceiling)
— here the poison is *self-labeled hides*. `applied-mappings.md`
§4; `notes.md` §65.

## Do Ax / DSPy own the control plane?

No. They climb **LM-program knobs** (prompts, demos, module
graphs). A typed control plane is deterministic code around that
program: ontology validation → security override → confidence →
state machine → tool allow-list.
[jev-dspy-control-plane](https://github.com/manikanda-kumar/jev-dspy-control-plane)
lets DSPy draft **after** route+action are fixed. Offline
heuristic + contract stubs prove plumbing, not quality. Accuracy
alone is not enough; a negative result is valuable.
`optimizer-integration.md`; `notes.md` §59.

## Native probabilities or verbalized confidence?

Measure the native distribution. Verbalized "I'm 80% sure" is a
different object (and usually needs temperature scaling).
[jev-arena](https://github.com/meetr1912/jev-arena) scores Jev's
`noul`/`choice`/`score` on analytically-known worlds. Their live
card (`jev-1.13.0`, 145 noul, 2 requests): Brier **0.0059**, ECE
**0.0620**, overconfident in the low bins. Fan-out is measurement
economics, not a demo flourish. Siblings: sonar (heatmap-as-policy),
vickrey (Jev never bids), bracket (Brier vs Elo; live trailed Elo —
honest). `validation.md`; `notes.md` §59.

## Train a specialist, or few-shot the hosted API?

Depends on **what consumes the output**, not on a vs-hosted
accuracy table.
[Domain-jev-maker](https://github.com/help-er/Domain-jev-maker)
trains a domain LoRA on **independent** CLINC-150 labels (not
a Jev teacher-copy). Their RESULTS.md: local 1.5B KL 0.168 vs
hosted zero-shot 0.580 banking (r +0.933 vs +0.343). Few-shot
hosted (one example per intent in `state`) matches or beats
local determinate accuracy (McNemar p=0.134 / p=1.000);
calibration barely moves. **Argmax routing → hosted +
examples. Threshold / deferral / expected-cost that reads
p → specialist.** Matched-precision KL (both systems rounded
to two decimals, zeros → 0.0025) is the Harbor hygiene.
`mappings.md` §2; `notes.md` §60.

## Is Noul 0.5 "maybe / medium"?

No. Noul 0.5 is **cannot-tell** — uncertainty about a
predicate, never medium intensity, **never rounded** into an
act. [jav-email-cascade](https://github.com/skiingfalcon/jav-email-cascade)
treats the band between mirrored thresholds as review, not
auto. Score confidence 0.0 is a flat distribution and is
never acted on. Same non-negotiable as the skill card.
`applied-mappings.md` §8; `notes.md` §60.

## Does a passing ECE mean `ORDER BY` is safe?

No. **Calibration ≠ sortable.** ECE/Brier ask whether a
stated 0.7 is 70%; pairwise inversion / Score ordinality ask
whether sorting by the number puts rows in a defensible
order. They come apart in both directions.
[jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench):
`jev-1.13.0` passes six pre-registered gates; Score ordinal
inversion 0.143 vs 0.15 is the weak link **and the sort
key**; 53 rows tie at 0.99 so `LIMIT 20` is
engine-dependent; two-decimal quantization. recodelabs
40-row batching fails the ranking gate that one-row-per-
request passes. Vendor 67.8% agreement is not calibration.
`mappings.md` §4; `notes.md` §60.

## Should we distill Jev as the teacher of record?

No. Use Jev to **decide what enters the training set**, not
as the label teacher.
[jev-triage](https://github.com/ThyFriendlyFox/jev-triage)
routes high-conf accept / middling expensive teacher /
low-or-boundary human and logs **full distributions** for a
local student. Author: a ~**68% ceiling compounds errors**.
Real outcome labels remain the training targets. Soft labels
are a bootstrap — cut the cord when the local head wins on
held-out real labels. Distinct from Domain-jev-maker
(independent gold specialist) and openjev-lm (teacher-copy).
`mappings.md` §2, §6; `notes.md` §61.

## Is local PCD a calibrated Noul?

No. **O(1) speed ≠ calibrated probability.**
[system-one-benchmark](https://github.com/mallahyari/system-one-benchmark)
on LMSYS toxic-chat n=50: local MLX PCD (Qwen2.5-1.5B) is 1
forward pass / p50 227.2 ms / 52% acc / Brier **0.3884**;
Jev-1.13.0 is 84.0% / Brier **0.1096** / p50 356.5 ms
HTTPS. AR JSON ~30.8 passes and 98% schema errors. Softmax
over allowed tokens is not a Noul. Same honesty as jevify
(uncalibrated CUDA likelihoods). Productized cousin:
[jevmlx](https://github.com/bnsd55/jevmlx) (28★) — schema→JSON
+ per-field probs in one MLX pass; **no local leaderboard
yet**. Small n — *their* card.
`judgment-class.md`; `notes.md` §61, §66.

## Closed-vote computer-use, or Stagehand pick?

Closed-vote means **code builds every option, the decision
model only picks, no planner LLM**.
[JevOnly](https://github.com/buluoray/JevOnly) is that
harness (Apache-2.0; type without generation; verify/undo).
[waymode](https://github.com/mossburgh/waymode) is the
**product** cousin: the app keeps handlers and permissions;
Jev selects among live typed actions; `completed` is Jev's
reading. Stagehand pick is a **fast path with LLM fallback**,
not this card. `applied-mappings.md` §9; `notes.md` §61.

## Engine eval or coaching verdict?

The engine owns truth; Jev owns judgment.
[game-coach](https://github.com/JoelLewis/game-coach) (Wave 0 PRD;
GPL-3.0): Stockfish WASM eval/lines/swing; Jev severity / error
class / interrupt; templates + a capped writing model own words.
Jev never evaluates positions or picks moves. Same anti-soundness-
theater as PR attention ≠ correctness (egma-ai). Silence is a
feature. `formal-methods.md`; `notes.md` §59.

## Is observe→score→act Jev-only?

No. The hole is backend-agnostic: observe controls, score among those
candidates, code acts. [jev-ultrafast](https://github.com/browser-use/jev-ultrafast)
and [solari-reflex](https://github.com/hitakshiA/solari-reflex) use
TypeSafe Jev; [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
uses local GLiNER2 (`fastino/gliner2-multi-v1`);
[laya-mind2web](https://huggingface.co/ShaunSpark/laya-mind2web-browser-agent)
uses a Laya head over DOM element indices;
[Cua-S1](https://github.com/trycua/cua/tree/main/libs/cua-s1) uses a
byte encoder + option-attention head (fill/check/click/skip) — **not
TypeSafe Jev**, source-only this pass.
[Stagehand #2951–#2955](https://github.com/browserbase/stagehand/pull/2955)
is the same hole **inside a major harness**: Jev picks; code copies
or acts; LLM fallback; extract `"off"`/`"judge"`/`"pick"`. Their
card: 37/75 no-LLM ~0.5 s vs baseline 4.37 s; LLM-off 36/75 — **pick
is a fast path, not a replacement.** Draft stack; do not copy the
opt-in flag. Same lesson as compaction
(Jev Noul/Score vs GLiNER2.5). Screenshot multimodal (blackwood-rlcd:
letters on an image) is a **different input**, not a better version of
this hole. Hybrid local decide + remote fill is mixed-architecture
economics, not dual-process-ai. `DONE` is loop termination, not
verified success. Plan ≠ execute; dry-run default on Cua-S1. Closed-vote
extreme: [JevOnly](https://github.com/buluoray/JevOnly) has **no
planner LLM** (code builds options, Jev only picks).
[waymode](https://github.com/mossburgh/waymode) is host-owned
handlers × System One, not a harness. Not
GLiNER2.5. Not a bake-off against the Flights demo clock.
[ego-jev](https://github.com/jiangkoumo/ego-jev) is the same
hole on ego-lite: indexed viewport table → operation+target;
code owns the loop; text model only for type; `--until` beats
Jev `done`. n=3 medians ~2×, not a bench.
[awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
is the **macOS OCR+AX** product of the same hole (MIT;
**427★**): never ships a screenshot for the *decision*;
writer only for free text; post-type Noul 0.5 *theirs* still
soft; overlapping options = false low confidence; split
kind/item/site. The one-shot answer reader may receive the
capture — that is not the Choice. $0.0002 / 155× is
one-screenshot *theirs*, not a Harbor taskset. **≠**
jev-ultrafast **≠** cua-s1 **≠** jev-macos-loop **≠**
open-typesafe-camoufox. `notes.md` §81.
`judgment-class.md`; `mixed-architecture.md`; `notes.md` §52, §54, §57, §61, §65, §81.

## Should I send the screenshot to Jev for computer use? Is 155× a Harbor score?

No, and no. [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
reads the screen **deterministically** (Vision OCR + AX +
dates.py) and asks TypeSafe a Choice over numbered items.
The decision never ships pixels to a frontier model. The
one-shot **answer** writer may receive the capture — a
reader packet, not the classifier. 155× / $0.0002 is
*theirs* on **one screenshot**, with the honest caveat that
frontier read dates unaided. Re-measure on *your* taskset.
`--min-confidence` 0.4 and post-type Noul 0.5 stay product
copy, not Harbor τ. Overlapping actions read as doubt; keep
the set exclusive. `notes.md` §81.

## Does Stagehand extract replace the LLM?

No. Pick-and-copy is a **fast path**. Schema leftovers, screenshot
extract, failed gates, and abstention still call the LLM. 36/75 with
the LLM disabled is the honesty number. `applied-mappings.md` §2;
`notes.md` §57.

## Is a public yes/no wall the product?

It is a **primitive surface**, not a chatbot. [ask-jev-ai](https://github.com/waynesutton/ask-jev-ai):
one call, six questions, policy in `convex/questions.ts`, code
decides live/blocked. Cost-to-1M from TypeSafe token counts
($32–$41), not estimates. No-key: allowlist, UI says Jev offline.
License null this pass. Do not copy Convex how-to.
`mixed-architecture.md`; `notes.md` §58.

## Meaning-search or grep?

Use grep when you know the string. [jevgrep](https://github.com/Bentlybro/jevgrep)
is for "where is the code that *does* X" with no embeddings: packed
parallel Jev relevance; 79% top-5 vs BM25 40% / grep 20% on
docstring-stripped repos; BM25 still wins exact wording (top-10
96% vs 85%). Line-level AND/OR/NOT over Nouls, including
JP↔EN: [jev-semgrep](https://github.com/uehaj/jev-semgrep)
(name collides with Semgrep SAST). Citable
"where is this *enforced*?" packets, index-once:
[jev-semantic-explorer](https://github.com/jimmyhealer/jev-semantic-explorer)
(jevex; 1/8→6/8 n=8 *theirs*; packet HitFile 0.233 is not
the product number). Distinct from kazuhideoki file+fzf,
superagents-lab web, and jev-sift classify-first.
`mappings.md` §4; `notes.md` §58, §61.

## Attention or correctness on a PR?

Attention. [egma-ai/jev-reviewer](https://github.com/egma-ai/jev-reviewer)
assigns P0/P1/P2 for where to look; OpenAI writes behavior deltas.
Incomplete never becomes P2. That is **not**
[choxos/jev-reviewer](https://github.com/choxos/jev-reviewer)
(pointer-not-generator). A Noul is not a proof the PR is good.
`formal-methods.md`; `notes.md` §48, §58.

## Can oxlint hard-gate on a Noul?

No. [jev-oxlint](https://github.com/cephalization/jev-oxlint) AST /
precheck prove what they can; guidance lives whole-file in state;
Jev scores the remainder. Phoenix fixtures matched the human
answer key; routing was sharp; the coarse hint was not. Experiment;
`tenbin` owns the lint skill. Do not treat remainder Noul as a
discharged proof. `mappings.md` §18; `notes.md` §58.

## Session-sticky routing: fail-open or fail-closed?

Name the irreversible act: *sending a model*.
[jev-adaptive-thinking](https://github.com/jxu-dev-c/jev-adaptive-thinking)
locks a declared standard (`gpt-5.6-sol`) on timeout / no session.
That is fail-closed to fallback, not jev-gateway passthrough.
First prompt classifies; later requests never reclassify. Same
family as routeKit (Jev estimates; code picks). `applied-mappings.md`
§5; `notes.md` §58.

## Did Jev-RAG beat full-context Spark on latency?

No. [Jev-RAG](https://github.com/Max-sm-yc/Jev-RAG) one-run: ≥70%
cost and 72% latency **vs Muse Spark rerank**. Full-context Spark
is still **faster** (10.60 s vs 62.3 s). Costs include embeddings.
Do not overclaim vs no-RAG. `mappings.md` §4; `notes.md` §58.

## Is Cua-S1 TypeSafe Jev?

No. [Cua-S1](https://github.com/trycua/cua/tree/main/libs/cua-s1)
uses "System One" as a computer-use research label for a small
specialist decide head. It does not ship Choice/Score/Noul, a
`/v1/systemone` drop-in, or TypeSafe contracts. Augustus places the
*hole* (observe candidates → select among a closed option set → code
acts under a hard envelope), not the logo. Same lesson as GLiNER2
Ultrafast vs Jev Ultrafast. Source-only; no checkpoint scores.
`judgment-class.md`; `notes.md` §54.

## Is routing the same as memory?

No. A cheap intent gate can skip a memory/tool *tour* on
`calendar` / `mail` / `status` without turning memory off.
[jev-hermes](https://github.com/de-niji/jev-hermes): memory still
**writes**; `complex` still searches. Route ≠ memory.
`applied-mappings.md` §5; `notes.md` §48.

## Is confidence a trained score?

No — not on Hume's reconstruction, and not as a new contract. Re-read
live TypeSafe confidence docs before you code a threshold. Training
(published name: RLCD) is aimed at the predictive distribution; which
proper scoring rule he did not observe. The Choice `confidence` field, in
the adapter revision he cites, is then ordinary arithmetic: how far the
leading probability sits above a uniform `1/K`. It is not a second learned
estimate that the answer is correct. A peaked distribution can be
confidently wrong. Threshold a p you have checked on your labels.
Independent receipt: [how-sure-is-jev](https://github.com/adarc8/how-sure-is-jev)
found Choice `confidence == max_prob` to 3 decimals on 60
answers — the most generous metric in their table.
[Essay](https://archerhume.com/posts/jevs-architecture-unmasked/),
`notes.md` §31, §67, `mental-models.md` calibration.

## Can CI call Jev live on every PR?

Prefer not. [jevassert](https://github.com/dtduc-git/jevassert)
**LANDED**: `record` once, commit `predictions.jsonl`,
`check` **offline** (accuracy + ECE/Brier + cost/latency
gates; exit 0/1/2; McNemar compare). Calibration and cost
are first-class, not footnotes. Pairs with jev-packs SPEC
v0. Do not copy `uvx`. `notes.md` §70.

## Is jevarena the same as jev-arena?

No. **Always qualify the owner.**
[chenmingtang830/jevarena](https://github.com/chenmingtang830/jevarena)
is an open BYOK failure-finding playground (JevJudge-Bench
harness; **not** measured model findings).
[meetr1912/jev-arena](https://github.com/meetr1912/jev-arena)
is a native-probability calibration arena on analytic
worlds (Brier/ECE; §59). Neither is a winner-crowning
leaderboard. `notes.md` §59, §70.

## Does 97% on BBQ mean Jev is unbiased?

No. [jev-bbq-experiment](https://github.com/simonmesmith/jev-bbq-experiment)
*theirs*: 58,492 questions, **97.28%**, amb bias **0.04** /
inf **0.34**, **$0.3429**. 12 of 13 ambiguous errors were
stereotype-aligned. One frozen English/U.S. QA template is
not a hiring/lending/healthcare cert. Pair with the
lustig framing stub, not a substitute. `notes.md` §70.

## Does the LLM plan in jeffrey?

No. **Decider ≠ executor.**
[jeffrey](https://github.com/thomasbrueggemann/jeffrey):
Jev owns next-tool / progress / risk / done; the LLM
**only fills args**. Risk ≥ 0.5 pauses mutating tools.
Stuck ladder withholds the looping tool and re-asks Jev.
Distinct from jev-handoff (baton around an existing host).
`notes.md` §70.

## Is jevlint the same as JevLint?

No. **Always qualify the owner.**
[mizchi/jevlint](https://github.com/mizchi/jevlint):
ast-grep subjects × sentence `ask:` (matcher silent, Jev
loud; 13/15 1.00/1.00 *theirs*).
[huntedman/JevLint](https://github.com/huntedman/JevLint)
is file-level convention Nouls (§26). Independent of
eslint-plugin-jev. `notes.md` §26, §70.

## Can I treat a local `/v1/systemone` as Jev?

Only as a **wire**. grande (Rust/WebGPU), laya-jolt
(Clojure byte-parity Laya), JEV-CPU (SemIf on CPU;
Meanblock 404), kunchenguid/local-jev (ONNX ModernBERT;
done **30%** / shape **57%** vs Jev *theirs*),
**githubnext/localjev** (prompted JSON + entropy
confidence; wire-compat ≠ logit-equiv), OpenJev
`/v1/decide`, semif-serve runoff, jeff GLiFormer, and the
GLiNER2 spec are **class substrates**. Softmax / generated
JSON ≠ Noul until calibrated on your labels. Interface
compatibility ≠ replica. Always qualify
**githubnext/localjev** vs **kunchenguid/local-jev**. The
Eran-BA GLiNER2 document is **spec-only** (no service, no
measurements) and is not jeff. Archer still Watch.
`judgment-class.md`; `notes.md` §70, §75.

## Do user constraints survive compaction?

Not in the model's memory. [pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)
persists them as structured state and checks
side-effecting calls before they run. Jev **never writes
policy**. Fail-open. Distinct from actiongate (RBAC/schema
authority). `notes.md` §70.

## Is jev-judge-bench the same as jevarena or jevbench?

No. **Always qualify the owner.**
[slavadubrov/jev-judge-bench](https://github.com/slavadubrov/jev-judge-bench)
is a frozen SLA-150 Harbor-shaped **contract**: Jev vs
cheap schema-guided LLM judges, human labels, invalid = FN,
cost/latency. **No quality headline yet** (21 offline tests;
canaries are availability).
[chenmingtang830/jevarena](https://github.com/chenmingtang830/jevarena)
is a failure-finding playground (JevJudge-Bench harness;
§70). [fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench)
is Capability/Speed/Cost Main Score (calibration reported,
not scored; §67). `notes.md` §71.

## Is jev-use the same as jev-ultrafast? Does Vercel Jev return confidence?

No, and often no. [jev-use](https://github.com/shitianfang/jev-use)
hands **no-text** steps (did it work / which next / safe) to
Jev and leaves writing with the LLM. Distinct from
browser-use/jev-ultrafast (observe→score-act browser loop).
Through the Vercel gateway there is **no confidence field**
— jev-use reconstructs margin and defaults that backend to
**0.4**. First loop 17/20 escalate, then 0/20. Same author
as jev-handoff. Gate is fail-open. `notes.md` §71.

## What is pi-jev-control?

A System-One **control plane** for Pi (router, tool gate,
failure+retry, context/skill/memory, compaction epoch,
review, GUI), not a second agent.
[pi-jev-control](https://github.com/goodruizhan/pi-jev-control)
compaction never modifies the on-disk session; GUI
confidence below threshold → `unknown`, never force-click.
License null; no live quality numbers in the README.
Distinct from omp-jev-extensions / jevons / pi-heed / pi-om.
`notes.md` §71.

## Can Jev generate text (jev-gpt)?

It never free-generates.
[jev-gpt](https://github.com/florian-hoenicke/jev-gpt)
asks one typed question per choice over a WordNet /
jina-embeddings tree, then ranks candidate texts. README
*theirs*: ~400 calls, 75 s, 2 cents per prompt.
Architecture demo of **decider ≠ executor** taken to the
word. Distinct from jeffrey (pick next-tool, LLM fills
args). License null. `notes.md` §71.

## Are jev-cookbook numbers a benchmark?

No. [jev-cookbook](https://github.com/nexibeo/jev-cookbook)
samples are 16–36 handmade items; the authors say the
scores show technique, not benches. Recipes 01–13: 425
calls / $0.015; browser 5/6 *theirs*. Pattern: code
prepares, Jev answers narrow questions. MIT. `notes.md` §71.

## Is jevfeed a social product?

No. [jevfeed](https://github.com/fengyiqicoder/jevfeed)
ranks links found in **your** last 200 history pages. No
likes, follows, or accounts. History stays local; one Jev
request per batch of ten (the distribution *is* ranking).
Distinct from ThinkyMiner/Winnow (grade an existing feed)
and kevinpita/winnow (context sieve). `notes.md` §71.

## Did openJev-verdict-2.0 beat Jev? Is it OpenJev?

Treat it as a **claim-audit**, not an endorsement, and no
it is not IamBusy/OpenJev.
[openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0)
README *theirs*: 77.10% / Brier 0.0636 / ECE 0.0144 on
LocalLLaMA/typed-decisions. The Jev table row is a
Laya-catalogued vendor baseline, not an independent run.
**Open PR #1** already flags: throughput misread as
latency; Laya gap inside the 95% CI (parity, not SOTA);
correctness-head ECE is not distribution ECE (Jev 14.40%
slightly lower like-for-like). Distinct from
IamBusy/OpenJev `/v1/decide`. `notes.md` §71.

## Is IPECTER/jev-context-pruner a compaction product?

Not this pass. The repo is **empty** (409). Slogan only.
Sibling of fast-jev-compaction / jev-compactor /
dizk/jev-lens. Do not invent files. `notes.md` §71.

## Is chakuho a local Jev? Is coverage a Noul?

No, and no. [chakuho](https://github.com/taku-me/chakuho)
is a 1-token logprob endpoint over a generic instruct
model (`POST /v1/systemone`). Softmax over declared
labels is **not** a calibrated Noul. `coverage` is the
mass that landed on those labels — format-keeping, not
correctness. 8B stays coverage 1.00 while `__none__`
collapses (3/30 vs 27B 29/30 *theirs*). GUI 336-case:
27B 95%/92% vs Jev Gateway 89%/82%. Arithmetic stays in
code. Cousin jevify / TypeAR / pcdServer / jevmlx.
`notes.md` §72.

## Is jevinf TypeSafe Jev?

No. [jevinf](https://github.com/zerodegress/jevinf) is an
open replica **runtime**: segmented forwards + prefix
reuse, then the Jev wire. NanoJev / decider-2b / Laya
families; only `torch-mps` is wired. 2.57× / 2.27× at
**100% argmax agreement** *theirs* is speed, not ECE.
Python ≥3.14. `notes.md` §72.

## Is typesafe-elixir-sdk the same as dannote/jev?

No. [typesafe-elixir-sdk](https://github.com/phiat/typesafe-elixir-sdk)
is an unofficial **HTTP client** (Req; same env/retry as
the Python SDK). [dannote/jev](https://github.com/dannote/jev)
is an OTP **peer GenServer** (answers as messages; clause
order is routing). Code still owns the `cond`. Confidence
is concentration, not P(correct). `notes.md` §72.

## Did jevex replace jev-semantic-explorer? New numbers?

It **is** the rename (same `created_at`; GitHub
redirects). New card *theirs*: SWE-bench Verified
**n=16**, 160s → 69s, $8.74 → $3.13, 16/16 both arms.
90s cap: 1/16 vs 11/16 finished. Keep the older n=8
finish 1/8 → 6/8. Claude Code n=5 6.8 → 2.2 is
unchanged. Packet HitFile stays diagnostic.
`notes.md` §61, §72.

## Does commitjev block a commit? Can I round 0.4?

It blocks only on a **warning**. A failed check is not
a reason to refuse. Anything between 0.35 and 0.65
(their 0.65 bands) is reported as **"review"**, never
rounded. Nouls decide the verdict; the Choice is the
headline. Six regex checks never reach the model.
Same owner as jev-orderby-bench (one commit per call
because batch ranking fails). Five clean commits is a
small control. `notes.md` §72.

## Is hermes-plugin-jev TypeSafe System One?

No. The README brands Choice/Noul/Score as Jev, but
`__init__.py` calls **Agnes 3.0 Flash** via
`system_one_adapter` OpenAI chat-completions
(`AGNES_API_KEY`). Distinct from hermes-jev-router
(TypeSafe WHETHER/HOW/WHAT). `notes.md` §72.

## Is pi-jev-compact the same as pi-jev-compaction?

No. [pi-jev-compact](https://github.com/dev-willbird1936/pi-jev-compact)
replaces Pi's **summarizer** with verbatim keep/drop of
paired tool calls (fail-open to the LLM summary if
<25% saved). [pi-jev-compaction](https://github.com/vava-nessa/pi-jev-compaction)
is the fast-jev-compaction cousin. Pair compact with
pi-jev-control / pi-heed, not as a clone of either.
`notes.md` §72.

## Is IPECTER/jev-runway a Codex proxy?

Not this pass. LICENSE only; created and pushed one
second apart; README 404. Second IPECTER empty slogan
(after jev-context-pruner). `notes.md` §72.

## What is mailordinal? Is it just email classification?

A **decision-native inbox**: nine typed questions, then
a 100-point policy in code (SLA + account tier). It
does not ask "how urgent is this?" Humans own
ambiguity — low confidence never silently lowers
priority. Life/business, not SWE-only. Cousin of
jav-email-cascade. Independent of TypeSafe.
`notes.md` §72.

## Is jev-cli the same as jevql? Can I install it?

No, and not yet. [jev-cli](https://github.com/shaharia-lab/jev-cli)
is an unofficial Rust CLI (exit codes as a semantic
`if`; planned MCP). README: **commands not
implemented**; crate: **not ready**; version 0.0.0.
[jevql](https://github.com/kylemclaren/jevql) is
judgment *outside* the store (vanilla Postgres never
sees `jev()`). Do not copy `claude mcp add jev`.
`notes.md` §72.

## Should I use English Laya on non-English text?

No. [laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual)
exists because the English checkpoint **stays
confident while going to chance** (Khmer 0.000 acc at
0.952 confidence *theirs*; mean conf never < 0.885).
Route by **script before the forward pass**. The
multilingual checkpoint ships uncalibrated (ECE 0.314
→ 0.106 after T *theirs*). Weaker on English — route,
do not replace. `notes.md` §72.

## Is the Hub schema-scorer a Jev replica? GitHub 404?

Hub
[jev-schema-scorer-deberta-v3-large](https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large)
is MIT; the GitHub repo 404s this pass. One DeBERTa
scalar head; **code** groups logits into
Choice/Noul/Score. v2 Choice acc 0.841 *theirs*.
Peaked probabilities are **rankings**, not calibrated
confidences. Distinct from
com-kotobalabs/open-jev-deberta-v3-large. `notes.md`
§72.

## Why are open-jev-laya-bench / jev-tree-choice-cap / INSTRUCT_JEV 401?

Access change this pass (historically 200). Do not
invent new numbers; do not re-fold. jevlogs-log-triage-
benchmark is GitHub 404 **and** HF 401 — skip.
`notes.md` §72.

## Is classifier.dev just another public Jev wall?

No. [classifier-dev](https://github.com/mrmps/classifier-dev)
(MIT; **185★**; https://classifier.dev) is a **zero-shot
classification API**: caller-supplied labels, batch
`{id, text}[]` up to ~1000, multi-label, dimensions.
Primary backend is TypeSafe Jev (`src/jev.ts`); LLM
chains are fallback only. Distinct from
[ask-jev-ai](https://github.com/waynesutton/ask-jev-ai)
(six parallel questions on one sentence). Life/business
(spam / inbox / feedback), not an agent hook. Do not
copy wrangler / `npm i -g`. `notes.md` §73.

## Should every low-confidence answer escalate?

No. `tier: smart` re-asks **single-label** answers
below 0.7. Multi-label **ignores** the tier: re-judging
made it worse (23 s *theirs*). 0.7 is *their* operating
point, not a class constant. Cousin of jev-use
escalate-under-threshold (different product; Vercel
drops `confidence`). `notes.md` §73.

## Can I quote classifier.dev F1 0.887 / 87.7% AG News?

Only with `eval/README`. `/benchmark` is generated from
tracked `src/vs-jev.json`, not hand transcription.
Multi-label n=7 is **train-on-test**, one annotator, no
CIs; ~0.03 is a coin flip. README *theirs*: F1 **0.887**
in **230 ms** vs cascade **0.799** / 1.5 s; eval *theirs*
232 ms, AG News **87.7%** vs ling-3.0-flash **82.0%**,
emotion **60.5%** vs **57.0%**. Calibration anecdote:
≥0.9 → 82% correct; <0.5 → 29%. `notes.md` §73.

## What is the silent-fallback anti-pattern? Does rh-guard own it?

A delisted primary left `granite-4.0-h-micro` serving
F1 **0.546** while docs advertised ~**0.800** for weeks
(*theirs*; eval/README). Nothing in the deployed numbers
said so. Digest now marks `FALLBACK`. That is **eval
integrity / soundness theater** (lying about the
instrument). **rh-guard owns the gate card**; dinostomp
owns instrument-not-score. classifier.dev is the lived
product cousin, not a new hook. `notes.md` §73.

## Is choxos/jev-reviewer the same as egma-ai/jev-reviewer?

No. Always write **[choxos/jev-reviewer](https://github.com/choxos/jev-reviewer)**
or **systematic-review Jev Reviewer**. It is local-first evidence
extraction: Jev points at line ids, code copies verbatim quotes,
human checks every answer (https://jevreviewer.xera.ac; MIT;
**12★**). [egma-ai/jev-reviewer](https://github.com/egma-ai/jev-reviewer)
assigns PR **attention** P0/P1/P2; OpenAI writes behavior deltas.
Attention ≠ correctness. `notes.md` §48, §58, §74.

## Why two passes (Choice then Noul) on a paper?

Relative Choice answers "which line, if any?" Absolute Noul answers
"does this line **itself** answer q?" Multi-row table answers
(Mean (SD) vs Median (IQR) under Age) need both. Quotes = Noul
≥ 0.5 *theirs*, not a class constant. Same species as Stagehand
extract / jev-sift; different domain (Cochrane / PRISMA). `notes.md`
§74.

## Can I skip the human tick if Noul ≥ 0.5?

No. The tick **is** the product. Checked or annotated answers are
never overwritten by a reworded question. Jev is SENSOR; the
reviewer is the constraint. Spot checks on the sample study are
**not** a validation study. `notes.md` §74.

## Is *Not found* a failure of the extractor?

No. When no line passes, the card says *Not found* (or *Unclear*,
with the closest lines) instead of guessing. Paraphrase invent is
the rejected species. *Not applicable* is a checked n/a. `notes.md`
§74.

## Is githubnext/localjev the same as kunchenguid/local-jev?

No. Always write **[githubnext/localjev](https://github.com/githubnext/localjev)**
(MIT; **261★**; GitHub Next). It is a Bun `POST /v1/systemone`
bridge: DiffusionGemma through ordinary Chat Completions; TypeSafe
SDK drop-in. [kunchenguid/local-jev](https://github.com/kunchenguid/local-jev)
is an ONNX ModernBERT approximation (done **30%** / shape **57%**
vs Jev *theirs*; confidence omitted). Hyphen vs no hyphen is
load-bearing. `notes.md` §70, §75.

## Is LocalJev OpenJev? Are the probabilities logits?

No, and no. [razorback16/openjev](https://github.com/razorback16/openjev)
obtains probabilities with a one-step DiffusionGemma **structured
read** (unmerged vLLM `diffusion_seed_canvas` / `diffusion_read_only`
/ token logprobs). githubnext/localjev **prompts** for a JSON
probability vector, validates/retries, then normalizes + entropy
confidence. Wire-compatible, **not mathematically equivalent**.
Distinct from [IamBusy/OpenJev](https://github.com/IamBusy/OpenJev)
`/v1/decide`. Cousin djev-spark is the structured-read Spark
surface already §36. `notes.md` §75.

## Can I threshold LocalJev confidence as a Noul?

Not until you calibrate on *your* labels. README: evaluate before
consequential decisions. The 1,200-request bake-off tests the
prompted-JSON pipeline, **not** direct logits, and says **do not
treat these outputs as calibrated probabilities** (high conf on
wrong BoolQ → large NLL; 40 samples/task). JSON-valid ≠
picked-right. Entropy-as-confidence is a spread statistic on a
generated vector. `notes.md` §75.

## Did Gemma 4 26B-A4B win? Should I use LM Studio instead?

Neither as a class claim. Short-input *theirs*: Qwen3.6 macro
**76.7%**, Gemma 4 26B-A4B **75.0%** (lowest SST-5 MAE **0.533**),
DiffusionGemma **74.2%**. Qwen vs Gemma 26B is two answers of 120 —
not a statistically clear winner. Serving default **unchanged**.
LM Studio still cannot load DiffusionGemma (18 Sep 2026 *theirs*).
Even after Chat Completions support, swapping runners is not
OpenJev parity — the runner must expose structured-read primitives.
Do not copy bun / `.env`. `notes.md` §75.

## Is NandhaKishorM/laya a new System One species?

No. [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
(Apache-2.0; **710★**) is the GitHub/PyPI packaging of
Hub Laya we already watch
([convaiinnovations/laya](https://huggingface.co/convaiinnovations/laya),
[laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual),
[laya-typed-decisions](https://huggingface.co/convaiinnovations/laya-typed-decisions)).
Choice / Score / Noul, RLCD, NAR encoder. The new face
is `Router` (script-before-p) plus an honest vs-Jev
table. Always qualify GitHub vs Hub. `notes.md` §18,
§42, §46, §72, §76.

## Is Laya a TypeSafe `/v1/systemone` drop-in? Same as localjev?

No, and no. Different Python API (`agent.predict` /
`Router.predict`), not the TypeSafe SDK wire.
[githubnext/localjev](https://github.com/githubnext/localjev)
is a prompted-JSON Bun bridge. Do not copy `pip
install laya`. `notes.md` §76.

## Can I hard-act at Laya confidence 0.85?

Not from the README snippet. 0.85 is *their*
illustration because RLCD trains against strictly
proper scoring — it is **not** a Harbor-calibrated
threshold and **not** a class constant. Khmer 0.000
acc at 95.2% confidence already shows gating cannot
catch script OOD; route **before** p. Fit T and pick
τ on *your* labels. `notes.md` §72, §76.

## Did Laya beat Jev?

Not as a class slogan. README: Jev figures are
**third-party published, never measured here**;
Banking77 is 72 vs 77 labels. Where Jev leads *on
that table*: Banking77 **0.870 vs 0.425**, soft-acc
**0.580 vs 0.471**, raw ECE **0.144 vs 0.213**. Where
Laya leads *theirs*: T4 **32.8 ms** vs Jev p50
236–276 ms; post-T ECE **0.081 vs 0.246**; multilingual
router. typed-decisions **0.766** is a fine-tune on
that split (base ckpts below majority 0.461). `notes.md`
§76.

## Is the @airesearch12 tweet JevBench v1.1? Can I quote the live board from it?

No, and no. The tweet is a **named census + a promise**
of a first leaderboard "today"
([status/2101259522933186879](https://x.com/airesearch12/status/2101259522933186879)).
[`fstandhartinger/jevbench`](https://github.com/fstandhartinger/jevbench)
**v1.1** is already §67 (314 decisions; Main 0.6/0.2/0.2;
calibration **reported, not scored**). The watch URL is
[benchmarkheaven.com/jev-models](https://benchmarkheaven.com/jev-models).
Do **not** paste live ranks into the census card — scored
methodology is now §78 (JevBench v1.2 board). Also **≠** jev-judge-bench
**≠** jevarena **≠** jev-arena. `notes.md` §67, §77, §78.

## Does GLiNER2 count as an openjev? Do routers?

As a **class-boundary claim**, not as identity.
GLiNER2 ([fastino-ai/gliner2](https://github.com/fastino-ai/gliner2))
locates/categorizes;
Succinct Router 14M / jev-model-router / Director / Loki
**route**. The tweet lists them beside NAR replicas and
TypeSafe-shaped wires. Same *job family* (fast cheap
bounded judgment) ≠ a Jev replica and ≠ a Noul ECE row.
Needle 3 is already **not Jev-class** in §67
(function-calling / label only). Qualify `open-jev`
Dasein vs JoshuaSP; OpenJev razorback16 vs IamBusy
`/v1/decide`. `notes.md` §77.

## Is the census complete? Are the missing names out of class?

No, and no. Gaps vs our watch include Laya /
[NandhaKishorM/laya](https://github.com/NandhaKishorM/laya),
[githubnext/localjev](https://github.com/githubnext/localjev),
kev, TypeAR, openvons, chakuho, jevinf, grande,
laya-jolt, blackwood, classifier-dev. Incomplete census
is **lag**, not a dunk and not evidence those heads left
the class. Completeness is a board watch item. `notes.md`
§77.

## Can I rank openjevs from the tweet? Are 15 likes a quality signal?

No, and no. A list is not a bake-off. Likes/views/quotes
are **ephemeral** (SIGNAL ~417/9/3; this pass 564/15/5 —
do not quote as quality). The scored sibling is §78
(geometric-mean I/C/S/K; Jev 75.3 / SemIf 74.6 *theirs*).
Harbor/jevals still wants a frozen taskset, calibration
on or honestly off the composite, named cost/latency
assumptions, partial runs not ranked, silent fallback
marked. `notes.md` §77, §78.

## Did Jev win JevBench v1.2? Is 75.3 vs 87.6 a drop?

Jev 1.13.0 is **#1 at 75.3** *theirs* (I 90.4 C 82.7 S 83.3
K 51.7; $0.041 production). SemIf is **#2 at 74.6** (−0.7).
**75.3 is not a drop from v1.1 87.6** — different tiers
(hard 220 new; 534 vs 314) and scoring (geo-mean I/C/S/K
with calibration **on** the rank vs weighted sum with
calibration **off**). Do not mix versions. Unofficial,
not TypeSafe-endorsed. `notes.md` §67, §78.

## Is Luna better than Jev? Can I hard-rank from the geometric mean?

Luna has the highest Intelligence (**96.8**) and ranks
**#7** because Cost is **28.2** ($0.247/1k). DeepSeek
wins Calibration (**96.7**) and ranks **#11**. The
geometric mean does not let a strong axis buy back a
weak one — *theirs*. That formula is a **product
design**. Other views: Balanced no-cal SemIf #1 75.2 /
Jev #3 73.0; Emphasis Cost system-one-open #1 69.4 /
Jev #5 63.6. Limits: "The weights are a choice."
`notes.md` §78.

## Is Qwen3.8 27B Archer? Why is Laya missing?

No, and not as a quality verdict. Qwen3.8 27B is a
**partial** official-Qwen run via Chutes TEE (I 74.6
C 92.1 S 61.3 K **0** ~$2.711 est.; hard 21.4%) — **≠**
Archer Hume (still Watch). Laya is **absent from the
scored table and also not in the named exclusion list**
— a gap vs our watch (§76), never a quoted "excluded."
GLiNER2 is mapping-excluded *theirs* (normalization
would drive calibration). Apps (Director/Loki) out.
OpenJev on the board = razorback16 DiffusionGemma **≠**
IamBusy `/v1/decide`. `notes.md` §78.

## This hour's HIGHs already folded — dump the repos again?

No. Hourly 0842's named HIGHs are already §73–§78
(classifier-dev, choxos/jev-reviewer, githubnext/localjev,
NandhaKishorM/laya, @airesearch12 census, JevBench v1.2).
The product is a **recipe**, not a hit list:

1. Ask how *p* was produced (wire-compat ≠ logit-equiv;
   prompted JSON + entropy ≠ structured logit read).
2. Productize `{id, label, p}`; escalate-under-threshold
   in code; mark `FALLBACK` if the head swaps (granite
   0.546 vs advertised 0.800 *theirs*).
3. Packaging ≠ new species; route by script **before** *p*
   (Khmer 0.000@0.952); 0.85 still soft.
4. Pointer-not-generator: Choice of line ids, copy
   verbatim, *Not found* is an answer, human tick never
   overwritten (choxos ≠ egma-ai).
5. A named census is not a bake-off; a scored board
   needs the score function, cal on/off, and named
   latency/cost assumptions (geo-mean I/C/S/K; ≠ v1.1
   87.6).

Skip thin noise (JEValuate / jevspeak / fable-jev;
jev-semgrep already §61). Hard-gating a Noul as a PR
merge or quality seal is **soundness theater**
([totally-tim/jev-gate](https://github.com/totally-tim/jev-gate)
≠ jev-gateway). Archer still Watch. `notes.md` §79.

## Does System 2 fly the drone? Should S1 wait for it?

No. [khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)
is **S1 keeps control / S2 one-use advisory**. README
*theirs*: “System 2 is advisory. It does not fly the
drone directly, and Jev does not pause while waiting
for it.” Escalate-under-threshold **without stalling**
— cousin of classifier.dev smart tier, different fail
polarity (that path re-asks and waits). S2 never
grants permission. Experimental viz, not a production
flight controller. `notes.md` §46, §80.

## Does purple mean S2 arrived or that Jev used the advice?

Used. Green = local context. **Purple confidence** =
that Jev decision **consumed** returned S2.
**Purple S2 bar** = arrival. Red = fail. Arrival
without a later purple confidence point is unused
advice. Mixed-initiative without a consumption mark
is theater. `notes.md` §80.

## Is Local controller githubnext/localjev? Is the 20% gate Harbor-calibrated?

No, and no. **Local controller** is the lab’s built-in
**rule-based** reflex (no credentials). **Live API**
is hosted TypeSafe `POST /v1/systemone` `jev-latest`.
Selecting Live API sets a 20% starting gate *theirs*
and **does not start a mission**; credentials do not
auto-switch. **≠** [githubnext/localjev](https://github.com/githubnext/localjev)
(prompted JSON) **≠** [kunchenguid/local-jev](https://github.com/kunchenguid/local-jev)
(ONNX). 20% is a UI default, still soft — schema-safe
≠ correct. Seed = repeatable geometry, not a
deterministic async replay. README says OpenRouter /
GLM 5.3; ARCHITECTURE proposed
`meta/muse-spark-1.3-contributor` — quote both
*theirs*; do not invent which is live. No pixels to
either provider. Do not copy npm / `.dev.vars`.
`notes.md` §80.
