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
  Native Apple locate runtime:
  [gliner-native-runtime](https://github.com/shershah1024/gliner-native-runtime)
  (Apache-2.0; **4★**) is unofficial Swift/Core ML
  `fastino/gliner2.5-small-v1` on ANE. Entity spans +
  confidence; not Choice/Score/Noul; not TypeSafe.
  Label descriptions as schema. `notes.md` §97.
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
replace native shell output from `PostToolUse`. OpenCode host-port:
[indiejoseph/opencode-jev-pruner](https://github.com/indiejoseph/opencode-jev-pruner)
hooks `tool.execute.after` on `bash` (`notes.md` §96). `applied-mappings.md`
§1; `notes.md` §50, §53, §96.

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
[moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
is the **ASR** product of the same hole (MIT;
**103★**): partial transcript → 9–11 questions →
Playwright. Pointer spans. Spoken confirm ≠ auth.
**≠** jev-voice-control **≠** nikolas-j. `notes.md` §82.
`judgment-class.md`; `mixed-architecture.md`; `notes.md` §52, §54, §57, §61, §65, §81, §82.

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

## Is jev-voice-browser omni System One? Is 27/27 a Harbor score?

No, and no. [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
is **ASR → text-state → hosted Jev → Playwright**. Web
Speech (audio to Google) is the producer; Jev never
hears the waveform. Partial transcripts get one
9–11-question request; policy waits longer on
free-text than on closed-set. Pointer-not-generator
for spans. Spoken "confirm" is a convenience, not
auth. Numbered overlays disambiguate without another
model. 27/27 / ~$0.0002/call / ~300 ms are *theirs*
on fixtures, not a Harbor taskset. 0.5 / 0.55 / 0.6
still soft. **≠** chris-wozniczek/jev-voice-control
**≠** nikolas-j/jev-voice-browser **≠**
typesafe-computer-use (OCR). Compose, don't collapse.
Skip Archer. `notes.md` §39, §82.

## Is AgentGhost an advisory sidecar? Can ASK be skipped?

No, and no. [reddpy/AgentGhost](https://github.com/reddpy/AgentGhost)
**is the tool's execution function.** README *theirs*:
the model never decides whether the wrap runs. Rules
(`allow`/`ask`/`deny`, `matchArg`) fire before Jev;
`allow` skips the judge. ASK/DENY throw so HITL
cannot be silently skipped. `failMode: "closed"`
denies on judge error. Judge is a slot (Gateway /
TypeSafe / custom). `AGENTGHOST_AUTO_APPROVE=1` is
a demo hatch, not a grant. Provider-hosted tools
and MCP (planned) are out of reach. **≠**
jwen5419807/agentghost **≠** vventirozos/AgentGhost
**≠** actiongate-jev **≠** toolgate **≠** jev-use
(fail-open). rh-guard owns the gate cousin. Do not
copy `npm` / `.env`. `notes.md` §83.

## Is the @studio_yebisu JP roundup a bake-off? Can I quote its star counts?

No, and no. [@studio_yebisu](https://x.com/studio_yebisu/status/2101065176069886152)
is a **genre atlas** of high-star Jev *apps* plus
open replicas. Tweet *theirs*: stars are
research-time; the post is a docs roundup, not
full eval. Engagement ephemeral (SIGNAL ~120k
views; this pass 131,234 / 1,934 / 192). Star
drift is the point (typesafe-computer-use ★203→
**427**; jev-voice-browser ★40→**103**). **≠**
@airesearch12 class census §77 **≠** JevBench
v1.2 §78. SAM 3.1 already §39. OpenRouter Jev
"no waitlist" is WATCH, not a recipe. Do not dump
the 30 repos. Skip Archer. `notes.md` §84.

## Is Akshay’s “Jev Clearly Explained” a TypeSafe how-to? Can I quote 200× / 400×?

No, and no. [@akshay_pachaar](https://x.com/akshay_pachaar/status/2101037514945597645)
is **independent pedagogy**. Article *theirs*:
LLM hammer for bounded decisions; code owns the
branches; parallel questions; thresholds in
code; schema-safe ≠ correct (“cannot break the
declared output schema, but it can still be
wrong”); placements = routing / tool-risk /
verify with LLM; shadow-mode; questions-as-code.
**200× / 400×** and 70–500 ms / $0.042/MTok sit
at TypeSafe’s favorable end — treat as a
**ceiling, not a promise**. Not Harbor. Text-only;
not looking at the screen. Do not copy the
Python samples. **≠** official docs **≠** Flavio
Copes **≠** LangChain harness **≠** AgentGhost
wrap. Engagement ephemeral (SIGNAL ~183k; this
pass 233,495 / 2,280 / 235). Skip Archer.
`notes.md` §85.

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
JP↔EN and FR/RU/DE/ES/ZH/KO: [jev-semgrep](https://github.com/uehaj/jev-semgrep)
(name collides with [Semgrep.dev](https://semgrep.dev) SAST;
proposition ≠ embedding; AND/OR/NOT after threshold;
not a gate; dedicated `notes.md` §86). Citable
"where is this *enforced*?" packets, index-once:
[jev-semantic-explorer](https://github.com/jimmyhealer/jev-semantic-explorer)
(jevex; 1/8→6/8 n=8 *theirs*; packet HitFile 0.233 is not
the product number). Distinct from kazuhideoki file+fzf,
superagents-lab web, and jev-sift classify-first.
`mappings.md` §4; `notes.md` §58, §61, §86.

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
jev-semgrep dedicated now §86). Hard-gating a Noul as a PR
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

## Is AgentGhost just toolgate with a new name?

No. [AgentGhost](https://github.com/reddpy/AgentGhost)
wraps execution so the LLM cannot skip the judge.
toolgate is pre-exec of a *proposed* call; Jev is
not authorization there. actiongate's slogan is
evidence ≠ authority (policy is the hard gate).
jev-use is fail-open PreToolUse. AgentGhost is
fail-closed wrap-as-execution; ASK throws.
`notes.md` §83.

## Is the JP genre atlas JevBench? Are the ★ live?

No, and no. Application atlas, not a scored board.
Stars were research-time *theirs*. `notes.md` §84.

## Is Akshay a vendor tutorial? Are 200× / 400× measured?

No, and no. Independent pedagogy. Multiples are
TypeSafe ceiling *theirs*. schema-safe ≠ correct.
`notes.md` §85.

## Is jev-semgrep Semgrep.dev? Are AND/OR/NOT embedding tricks? Is it a gate?

No, no, and no. [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep)
is **grep by meaning**: a Noul per line × meaning,
then boolean AND/OR/NOT on *thresholded* bits in
code. Proposition holds, not topical cosine. The
refund contrast-set (all six about a refund; only
customer-*asking* pass) is the pedagogy. Cosine
between angry customer and angry agent is close to
1. Do **not** multiply parallel p. Name collides
with [Semgrep.dev](https://semgrep.dev) SAST —
rename if both installed. Ranking fail-open; not a
gate (rh-guard skip). 0.94/0.98 is LLM-as-judge on
10×51 lines *theirs*, not Harbor. Stars ephemeral
(0 → ★42 SIGNAL → **51** this pass). **≠** jevgrep
**≠** jev-combinators. `notes.md` §86.

## Does Jev write UI text? Is a valid GramSpec / A2UI tree a good screen?

No, and no. Decision-validated UI: derive candidates from
data/quotes, Jev *selects*, a compiler emits.
[gram-render](https://github.com/wei-b0/gram-render) never
authors a word — empty quotes → `unavailable`. Telegram
4096-char / 64-byte `callback_data` prove the tree.
[jev2ui](https://github.com/dglazkov/jev2ui): “Jev decides,
Gemini writes, code assembles, a DESIGN.md paints.” Jobs
11/11 vs Baseline 10/11 valid A2UI *theirs* is **validity**,
not quality. schema-safe ≠ correct. Skip Archer: Jev never
sees photographs. `notes.md` §87.

## Is a meaning matcher a proof the product is right? Round 0.67?

No, and no. [jevtest](https://github.com/realZachi/jevtest)
is a Noul plus a threshold you validate on labelled
outputs. Default 0.85 still soft (“roughly one in ten”).
The band 0.15–0.85 fails *both* polarities on purpose
(anti-round; cousin of commitjev). Exact ticket numbers /
JSON / prices stay in `toContain`. Record/replay is CI
without a key — not a live Noul as a merge seal.
typesafe-ai/jevtest is **404**. **≠** jevassert. `notes.md`
§87.

## Hybrid S1: should I default jeff? Wait for Archer? Invent Laya?

No, no, and no. [anima3](https://github.com/hulryung-uo/anima3)
inverts anima2: closed verb menu + hard safety first (HP
35% shrinks the menu); Qwen logprob default; scene is an
**a11y tree**, not a screenshot. jeff/GLiFormer is
*confidently flat on magnitude*. The user brief named Laya
triage — the README does **not**; do not invent it. Skip
Archer. License null. `notes.md` §87.

## Is JevFind a patcher? Are 0.25 / 0.55 Harbor τ?

No, and no. Path Noul then overlapping windows; code copies
snippets. Thresholds still soft. Keyword still wins exact
strings. **≠** jevex **≠** jev-semgrep. `notes.md` §87.

## Is Jev 72.5% the class ceiling? Use Jev `confidence` as P(answer)?

No, and no. [jev-frontier-bench](https://github.com/manjunathshiva/jev-frontier-bench)
one run, 200 decisions, OpenRouter 19 Sep 2026. Jev 72.5%
ECE 0.161 vs Fable 84% ECE 0.064 *theirs*. Cascade 82.5% at
$4.41/1k is **in-sample** 0.9. ChaosNLI JS: Jev 0.149
**worse than uniform 0.127**. Confidence is the top of
`probabilities`, **not** the `confidence` field. **≠**
jev-frontier-100 **≠** OmarMujahid/jev-decision-bench.
`notes.md` §87.

## GLiClass vs Jev — architecture duel? Skip the majority floor?

No, and no. [jev-gliclass-bench](https://github.com/JoeSlain/jev-gliclass-bench)
is a **product bakeoff**. GLiClass flattened one-question-at-a-time.
Jev 78% vs GLiClass 40% vs majority **49%** n=100 *theirs*.
40% < 49% is the finding. Teacher labels ≠ human GT.
`notes.md` §87.

## Four engines: does zero-shot beat fitted classical? Is ECE ranking?

No, and no. [job-posting-triage](https://github.com/geckguy/job-posting-triage)
majority floor **0.947** (53 fraud / 1000). Jev lands
**exactly on it**. tfidf fitted on 12,725 labels **wins**.
`llm_local` answered fraudulent for all 1000 at conf 1.0
(ECE 0.947) — valid JSON, zero information. Calibration ≠
discrimination. Jev via classifier.dev. `notes.md` §87.

## Authorship check as evidence? Binary “is this AI?”

No, and no. Named Choice escape: `human` /
`ai_generated` / `uncertain`. README *theirs*: “not an AI
detector you should trust as evidence.” A binary Noul
collapses conflict and ignorance. Formal methods: this
sensor must not authorize a disciplinary or legal act.
`notes.md` §87.

## Does ha-switchboard replace HA-Jev? Can Jev write HA YAML?

No, and no. [ha-switchboard](https://github.com/grayslawson/ha-switchboard):
“Home Assistant remains the source of truth and the
execution authority.” Jev typed; one bounded LLM handoff;
proposals re-enter allowlist / freshness / idempotency /
post-state verify. **≠** AboveColin/HA-Jev (gallery still
**17★**). Not for locks/heaters. `notes.md` §87.

## Is n8n-nodes-jev official TypeSafe? Silent-best-route at 0.5?

No, and no. Unofficial helper. Route by Choice + Low
Confidence output (default 0.5 still soft). Arithmetic in
Code/IF. Cost figures are TypeSafe ceiling, not Harbor.
`notes.md` §87.

## Is fast-jev-compaction-pi the same as pi-jev-compact?

No. Three namesakes: **zaycruz/fast-jev-compaction-pi**
(this hour’s dedicated Pi port of tamaratran/fast-jev-compaction;
verbatim; fail-open to built-in LLM summary; ~50× *theirs*)
**≠** pi-jev-compact **≠** pi-jev-compaction. `notes.md`
§87.

## Does jevloop climb Jev? Quote mock-mode quality?

No, and no. Full distributions as a **value function**
inside UCB1+CEM; **no LLM in the loop**. Mock mode is the
Space default — control-loop demo, not a Jev quality
headline. **≠** Ax/DSPy (those climb LM knobs). `notes.md`
§87.

## Is laya-vision Archer? blackwood? Quote `score`?

No, no, and no. First Laya-class vision on SmolVLM.
`score` questions are **untrained**. CC-BY-NC-SA. 75.2% /
ECE cal 0.034 n=8235 *theirs*. VQAv2 yes/no re-split is
**not** published VQAv2. Code:
[r33drichards/laya-vision](https://github.com/r33drichards/laya-vision).
Skip Archer. **≠** blackwood-rlcd. `notes.md` §87.

## Drop Cerebellum into typesafe-sdk `base_url`? Endorse 94.92%?

No, and no. `/v1/decide` is **not** TypeSafe
`/v1/systemone`. mkeco GitHub ≠ mkzero Hub. Treat
**wire-compat** and **agent-routing** (pointer over
candidates) as separate Harbor axes. Competing NAR vs-Jev
table is an **audit object**, not endorsement
(openJev-verdict-2.0 discipline). 0.50 ActEscalate still
soft. `notes.md` §87.

## Is laya-grounded a drop-in Laya? Temperature-scale it?

No, and no. Grounding 2/5→5/5 *theirs* while phishing
**got worse** (0.611→0.512) and routing stability 2/3→1/3.
“Temperature Scaling will not work… Use Platt.”
`confidence` is normalised Shannon entropy, **not** top-p.
CC-BY-NC. GitHub 404. `notes.md` §87.

## Is GestaltLabs/Jeff-1 logan-markewich/jeff? Is better ECE “better than Jev”?

No, and no. [GestaltLabs/Jeff-1](https://huggingface.co/GestaltLabs/Jeff-1)
is a Qwen3-4B LoRA (code
[Gestalt-Lab/jeff](https://github.com/Gestalt-Lab/jeff)).
**≠** [logan-markewich/jeff](https://github.com/logan-markewich/jeff)
GLiFormer encoder. On 9,730 fact-check items *theirs*: Jeff acc
**0.8183** ECE **0.0807** vs Jev **0.8283** / **0.0932**. Acc/Brier
lose; ECE wins. The set was reused for error analysis — not an
untouched holdout. Lower ECE ≠ individual correct. Weak on
`not_enough_info`. Soft Noul ≠ hard safety. `notes.md` §88.

## Empty stanley findings = the change is fine? Auto-promote the agent’s workflow?

No, and no. [stanley-code](https://github.com/devagrawal09/stanley-code)
README *theirs*: empty findings is **not** an approval; read
`notChecked`. There is no `pass`/`approved`. Router 0.6/0.55/0.15
still soft. Only `--promote-candidate` activates a drafted
workflow. Pi fallback is unverified. Soft Noul ≠ hard safety.
`jev-code` 0.0.1 does nothing; 0.1.0 not on npm. `notes.md` §88.

## Is findme JevFind? Does a high beam score prove the file?

No, and no. [findme](https://github.com/marc2332/findme) is NL
memory → beam over listed names+metadata (life/knowledge FS
retrieval). [JevFind](https://github.com/Peu77/JevFind) is repo
path-then-window. Listing / gitignore / symlink skip stay in
code. Ranking ≠ identity. `notes.md` §88.

## Swap the conversation model per turn? Quote jevsubrouter dollars?

No, and no. [jevsubrouter](https://github.com/leftspace89/jevsubrouter)
prices **workers**; the live conversation keeps one model so
the prompt cache is not thrown away. Dispatch binds; the turn
hook is advice. Fail-open. Low conf → balanced, never silent
down. Stats are **counts**, not dollars — worker tokens are
invisible from a hook. **≠** jev-gateway **≠** slo-router.
`notes.md` §88.

## Is `.feels()` a new language? Is default 0.5 a bool if?

No, and no. [BoundaryML/feelings](https://github.com/BoundaryML/feelings)
is BAML methods, not Probably and not
[hunch](https://github.com/carldaws/hunch). README *theirs*:
“Jev makes the decisions, an LLM does the writing, and BAML
ties it together.” `.how()` keeps p. Default `.feels()` 0.5 is
Noul-0.5-never-rounded. License null. `notes.md` §89.

## Is apa-agent-harness jev-harness? Copy `@aipersona` npm?

No, and no. Same hole (shadow + gate), different product.
[apa-agent-harness](https://github.com/AiPersonacademy/apa-agent-harness)
**≠** AntonioCoppe/jev-harness. “Mathematically fulfilled”
has no numbers. npm unpublished this pass. Persona engine
<250 ms ≠ “microsecond.” 0.85 still soft. `notes.md` §89.

## Quote grok-bot-jev 13.0× as token savings? Can the skill force the bot?

No, and no. Proxies, not tokens. README *theirs*: “this is not
a token-savings claim.” 13.0× is a top-five cap by design.
“cannot force a bot that ignores the skill to stop.”
`notes.md` §89.

## Can Essentiel Jev send mail? Is 0.75 calibrated?

No, and no. Human every action. Never authority. 0.75
provisional. Synthetic tests; no live TypeSafe inference.
**≠** jevmail **≠** mailjay **≠** mailordinal. License null.
`notes.md` §89.

## Is enzo-mcp jev-sift? Skip UNKNOWN?

No, and no. Atom then sense: independently falsifiable
claims. Deterministic evidence outranks Jev. UNKNOWN is
useful. Prior sensor output never sent back. **≠** jev-sift.
`notes.md` §89.

## Treat pigeonhole OTHER as a move? Is 0.6 Harbor τ?

No, and no. Named escape skips. 0.6 still soft. autoOnSave
off. **≠** jev-semgrep. `notes.md` §89.

## Is the HF playground live Jev? classifier.dev?

No, and no. Static Space; no network. **≠** classifier.dev.
Sibling jev-decisions is already a toolbelt pointer — do not
re-card. `notes.md` §89.

## Does jev-reliability measure accuracy? Paste 12.5% as a class number?

No, and no. README *theirs*: Nothing about accuracy.
noul-gate flip 0.0%/12.5%/3.6% *theirs* is consistency on
that gate. **≠** dinostomp. `notes.md` §89.

## Is clduab11/jev-test the jevtest matcher? Did D already pass?

No, and no. **≠** realZachi/jevtest. README *theirs*:
“Nothing runs yet.” Bars are commitments, not scores. HTTP
judge smoke ≠ quality. `notes.md` §89.

## Did jev-rag-benchmark show Jev wins?

No. “Jev wins” is not an assumption. Plumbing smoke.
`max_budget_usd` 0 blocks paid calls. **≠** Max-sm-yc/Jev-RAG.
`notes.md` §89.

## Is dairui1/jev-lab BrendanH18/jev-lab? Re-card jev-desktop?

No, and no. 91% vs 79% *theirs* on 120 synthetic tickets.
Fan-out vs `CLICK:3`. 0.65/0.70 still soft. jev-desktop
already MED. `notes.md` §89.

## Is jevmail mailordinal? Is mailjay read-only?

No, and no. jevmail is `gmail.readonly` (~3¢ / ~1 min per 1k
*theirs*). mailjay proposes archive/trash for review.
**≠** Essentiel-Jev. `notes.md` §89.

## Is ZHUBoer/ego-jev jiangkoumo/ego-jev? Is `completed` success?

No, and no. Always write **ZHUBoer/ego-jev**. Ego Lite
observe/act; Jev `choose` over compact page state.
ZHUBoer/ego-jev reserved `__none__`. `choose` does no
browser action and applies no universal cutoff.
runWorkflow completed ≠ success. Exact work local.
**≠** jiangkoumo/ego-jev. `notes.md` §90.

## Are jsort scores frequencies? Use Choice for a scale?

No, and no. jsort scores are relative. Ranking ≠
calibration. Noul not Choice for scale. CommonLit
r=0.824 / ρ=0.841 *theirs*. Fed hawkish ρ=+0.47
(91 statements) vs rate move *theirs*. `notes.md` §90.

## Did groundedness-judge-bench show Jev wins quality? Is it jev-judge-bench?

No, and no. groundedness-judge-bench native vs
schema-guided. Fastest/cheapest ≠ quality. Jev Macro-F1
0.6667 vs GLM 0.7661 *theirs*. implicit_true included
in yes. **≠** jev-judge-bench **≠** jevarena **≠**
jevbench. `notes.md` §90.

## Quote jev_playground 83%? Promote from authored bars?

No, and no. jev_playground 0 promotions — on purpose.
A suite that passes a random judge is plumbing
(254/305=83%). Authored vs real. routing-backtest
0.0447%. **≠** HF playground. `notes.md` §90.

## Copy `jev-latest` on Zen? Is yuyang2230 GodsBoy’s router?

No, and no. yuyang2230/jev-agent-skill jev-1.13-free.
$0 is a Zen-tier claim, not a quality score. **≠**
GodsBoy/jev-agent-skill-router. Do not copy `ZEN_API_KEY`.
`notes.md` §90.

## Does the techstack classifier generate a stack?

No. Classifier not generator. jev-techstack-classifier
stack_config.json only. Worker has no key. License null.
`notes.md` §90.

## Is s1_ruby hunch or feelings? Is `is?` a proof?

No, and no. s1_ruby collapse late. `undecided?` abstain.
Code asks; code decides. **≠** carldaws/hunch **≠**
feelings **≠** tpellet/hunch. `notes.md` §90.

## Is judgement jevql? Is confidence the winner p?

No, and no. 2389-research/judgement license null.
Unofficial Go CLI. confidence ≠ winner p. Pin vs 24h
alias. Live arithmetic ≠ accuracy. **≠** jevql. `notes.md`
§90.

## Is the Rust community SDK official / a new species?

No, and no. typesafeai-sdk-community not a new species.
Independent community port. Bands are caller policy.
**≠** elixir SDK. `notes.md` §90.

## Is tpellet/hunch carldaws/hunch? Skip exit 3?

No, and no. Always write **tpellet/hunch**. Pointer
shell. tpellet/hunch exit 3. never-execute list. NL2Bash
36/120 *theirs* is not a shell-replacement proof.
**≠** carldaws/hunch. `notes.md` §90.

## Quote file-search 15 matches as recall? Is it JevFind?

No, and no. jev-file-search scores not calibrated
accuracy. Recall unmeasured. **≠** findme **≠** JevFind
**≠** jevex. `notes.md` §90.

## Treat linkmap referee as gold? Let Jev see S2 prose?

No, and no. jev-linkmap Jev never sees S2 prose.
Anchors already in copy. v1→v3 45%→65% *theirs* is
rubric rewrite, not ground truth. `notes.md` §90.

## Is jev-mail jevmail? Does tidy OTHER move? Close pinned tabs?

No, no, and no. muhammedilyasy/jev-mail metadata only.
tidy none-of-folders stay. tab-bouncer
pinned/audio/current never closed. lkclean Show
fail-open. jev-yt-time-saver Show anyway. **≠** jevmail
**≠** pigeonhole **≠** x-reply-filter. `notes.md` §90.

## Does ORIGIN’s LLM decide? Continue if Jev is down?

No, and no. ORIGIN pause-if-no-Jev. validResponse
sums-to-1. LLMs plan never decide. **≠** Essentiel-Jev.
`notes.md` §90.

## Gate crawlers on raw `bug_likely`? Skip verify?

No, and no. jev-crawlers risk bands never raw boolean.
Verify grounding, not exec. n=12 fixture. rh-guard owns
the gate cousin. `notes.md` §90.

## Is jevbrain TypeSafe Jev? Paste 95.2% as a class number?

No, and no. Local n-gram/anchor overlap. jevbrain
AUTO_ACT is not a Noul. WHITEPAPER unverified theater.
README MIT vs SPDX null. **≠** classifier.dev. `notes.md`
§90.

## Is judgekit a JudgeBench clone? Quote 97.7% as a class ceiling?

No, and no. judgekit YAML classify/score/route/verify.
n=130 zh mini sets. 0.7 gate *theirs* on 3 errors.
**≠** JudgeBench **≠** DeepEval **≠** promptfoo.
`notes.md` §91.

## Threshold on the model's own confidence? Skip `combine()`?

No. typed-judge-kit verdict-in-code. Gemini 0.88–0.95
does not discriminate. MIN_LABELS=20 / P_MIN=0.95.
Noul rerank made R@5 worse 14/15→13/15. `notes.md` §91.

## Is decide 0.8 equal to 80% accuracy? Dump results into context?

No, and no. alsoleg89/decide packing VOI. 0.8 ≠ 80% accuracy. confidence ≠ max(p). Review rate is an
outcome. **≠** jev-sift. License null. `notes.md` §91.

## Does the calibration arena act? Is it jev-arena?

No, and no. jev-calibration-arena never acts. Spec-first;
scaffold blocked. **≠** jev-arena **≠** jevarena.
`notes.md` §91.

## Does Jev's raw confidence already match frequency?

Not on Anthus's sentiment set. Jev-Calibration Platt ECE 0.117→0.052 (isotonic 0.008). Choice 50–95% sits at
~50–57% accuracy. `confidence` field ≠ top-p. `notes.md`
§91.

## Is openrouter-jev-mcp a TypeSafe first-party MCP? Native TypeSafe keys?

No, and no. ctmx/openrouter-jev-mcp Decision-as-Plugin.
OpenRouter alpha Decisions (`~typesafe/jev-latest`).
Native TypeSafe keys not supported. A judgement can be
wrong and does not grant permission to act. `notes.md`
§91.

## Is FrancoisChastel/jev-code the stanley npm package?

No. FrancoisChastel/jev-code ≠ npm jev-code. auto_accept
0.85 still soft. **1★**. `notes.md` §91.

## Put marketplace Jev on every tool call? Fail-closed without a key?

No, and no. claudecode-jev-marketplace fail-open not hot path. Event boundaries only. Pin jev-1.13.0. `notes.md`
§91.

## Does mcp_jev invent `ask_jev`? Paste the key into host mcp.json?

No, and no. pedroknigge/mcp_jev packs not ask_jev. Key
once in `~/.mcp_jev`. `notes.md` §91.

## Is jevtypesafeai.com TypeSafe? Copy JEV_API_KEY how-to?

No, and no. codaaiteam/jev-skill jevtypesafeai.com ≠ TypeSafe. Independent `/api/v1/decide`. `notes.md` §91.

## Is `ts_safety` a Noul? Skip the deadband?

No, and no. cyrusasco/typesafe-mcp noul deadband 0.35–0.65. `ts_safety` is deterministic patterns.json.
`notes.md` §91.

## Is hermes-switchyard hermes-jev-router? Agnes? Does it load skills?

No, no, and no. hermes-switchyard ≠ hermes-jev-router ≠ hermes-plugin-jev. Advisory; never loads skills; hosted
routing not claimed. `notes.md` §91.

## Is nanoprune hosted Jev? Paste “0 hallucination guaranteed”?

No, and no. nanoprune 2.8MB ECE 2.58%. Laya 421M distill
*theirs*. The badge is soundness theater. `notes.md` §91.

## Is jev-browser-agent ZHUBoer/ego-jev? Is omp-jev-web `DONE` proof?

No, and no. smartdio/jev-browser-agent ≠ ZHUBoer/ego-jev.
Dakai/omp-jev-web DONE ≠ proof. **≠** omp-greenlight.
`notes.md` §91.

## Is hari007sh/jev dannote/jev? Is T-fit 0.9 a Harbor τ?

No, and no. hari007sh/jev ≠ dannote/jev. Teacher is
`systemone generate`. License null. `notes.md` §91.

## Is system-one-skills a judge? Paste 8,026 tokens as a class ceiling?

No, and no. 0thernet/system-one-skills deterministic verify. No model call. Holdout would add 3,612.
`notes.md` §91.

## Hard-argmax typed-gate as safety? Is 0.51 a yes?

No, and no. typed-gate band [0.40,0.60] is refusal.
rh-guard owns the gate cousin. `notes.md` §91.

## Is pi-jev-gate fail-open? Restore the ask band?

No, and no. pi-jev-gate fail-closed; choice is the verdict.
Ask band removed. **≠** pi-jev-approver. `notes.md` §91.

## Paste Foq 100%/ECE 0.2% as a class ceiling? Is 25 ms a Harbor number?

No, and no. Foq ~25ms/2.2GB local. *theirs* on RTX 4080 Super / 150-case exam. Recalibrate on your data. `notes.md` §92.

## Is rev a measured replica? Quote `latency_ms` 32.4?

No. rev prefill-only + HF jev-0.5b. 32.4 is a sample JSON field, not a bench. Card titles itself `rev-0.5b`. GitHub README points at Hub `rev-0.5b` (distinct sha). Do not collapse the two Hub ids. `notes.md` §92.

## Is robfrase/jev a running local Jev? Collapse into dannote/jev?

No, and no. robfrase/jev planning memo. No app code. ECE ≤ 0.10 is a **gate**. **≠** dannote/jev **≠** hari007sh/jev. `notes.md` §92.

## Treat typesafe_agent_gates 27/27 as a Harbor win? Soft Noul as hard deny?

No. typesafe_agent_gates 27/27 / 31/31 *theirs* on labelled probes. 0.5/0.6/0.8 starting points. rh-guard owns the gate cousin. `notes.md` §92.

## Is safe-sh a pre-exec allow/block? Collapse into toolgate?

No. EpicEric/safe-sh static remainder. Not pre-exec authorization. HIGH delta of MED §58. `notes.md` §92.

## Let pastepilot act without Confirm? Watch the clipboard?

No, and no. pastepilot Confirm before act. Fail-open missing key. ≥0.75/&lt;0.45 sensors. No clipboard spyware. rh-guard owns. `notes.md` §92.

## Quote Jev-Reranker r@1 0.1667 as live Jev? Confidence scales value?

No, and no. Jev-Reranker live Jev not yet measured. Offline lexical judge. `confidence_gate` 0.45 never scales value. `notes.md` §92.

## Is sessionwise a required Jev sieve? Fail-closed if Jev is down?

No, and no. sessionwise opt-in relevance. Local first. Fail-open if Jev is down. `notes.md` §92.

## Treat jev-search scores as truth? Dump every page into the LLM? Collapse into kazuhideoki/jev-search?

No, no, and no. jev-search pointer sieve. Score ≠ truth. Counts follow search. Always **savka777/jev-search**. **≠** kazuhideoki/jev-search **≠** superagents-lab/jev-search. `notes.md` §92.

## Is 400 ms a Salesforce SLA? Screen-scrape then stream?

No, and no. 400ms Salesforce WebMCP. Demo 50 ms Jev + 350 ms WebMCP. Timestamps ≠ Harbor. `notes.md` §92.

## Let the scheduler plugin place Pods? Quote demo agreement as accuracy?

No, and no. typesafe-scheduler-diagnostics advisory. Does not place Pods. Demo label agreement ≠ production accuracy. `notes.md` §92.

## Send Android screenshots to the frontier for the decision? Collapse droidjev into jev-ultrafast?

No, and no. droidjev screenshot-free. AX → typed pick → adb. find ~0.6 s/iter *theirs*. **≠** jev-ultrafast **≠** typesafe-computer-use. `notes.md` §92.

## Is jevcu closed-vote? Does Jev write the plan?

No, and no. Tewoto1 jevcu planner still writes. Jev picks op+target. Preview default. Smoke ~12 s / 324–380 ms *theirs*. `notes.md` §92.

## Is ha-conversation-jev HA-Jev? Copy the Grok OAuth client_id? Fire whole-home on `target_area=none`?

No, no, and no. ha-conversation-jev Jev→Grok. Whole-home safety in code. **≠** HA-Jev **≠** ha-switchboard. Do not copy OAuth `client_id`. `notes.md` §92.

## Can dsh-jev widen the tool set? Run live Jev by default?

No, and no. dsh-jev can only gate. Default mock+shadow. HIGH delta of MED §59. `notes.md` §92.

## Paste the classification-benchmark $0.46 as a measured run?

No. jev-classification-benchmark specified not run. Probe $0.0000166 / 13× *theirs*; $0.46 / 20 min **derived**. `notes.md` §92.

## Treat luna-pagerduty 1.000 as production paging? Collapse into Loghub?

No, and no. jev-luna-pagerduty p≥0.50. Synthetic n=3000. ≠ Loghub. rh-guard owns paging. `notes.md` §92.

## Is meldecision a new Laya species? Quote int8 0.938 as Harbor τ?

No, and no. meldltd/meldecision laya-go ONNX. Goldens 4-decimal / byte-identical *theirs*. **≠** NandhaKishorM/laya. `notes.md` §92.

## Does laya-doom see pixels? Is it Archer / blackwood?

No, and no. laya-doom never pixels. ViZDoom keywords + scripted Route. **≠** blackwood **≠** Archer. `notes.md` §92.

## Quote laya-api README numbers? Treat empty README as a drop-in?

No. logixism/laya-api empty README (`e69de29b` 0 bytes). FastAPI wraps `convaiinnovations/laya`. `notes.md` §92.

## Quote akpsahan vs-Jev 0.766 as a new measure? Is it Archer? Is Qwen3.8-27B Archer?

No, no, and no. akpsahan/laya ≠ Archer. Card copies convaiinnovations/laya. Do not re-paste Nandha’s vs-Jev. Qwen3.8-27B ≠ Archer. `notes.md` §92.

## Does Jev own chess truth? Collapse jevchess into chess-coach?

No, and no. choxos/jevchess engine owns truth. ~300 ms / ~3k tok / game &lt;1¢ *theirs*. `notes.md` §92.

## Treat jev-drive as AV? Continue if Jev fails?

No, and no. jev-drive sim not AV. Jev fail pauses; no scripted substitute. Smoke 2026-09-19 not a bench. `notes.md` §92.

## Let Jev author the story-arc chart?

No. story-arc Jev never authors. Compose 0.7/0.5/0.6 sensors. `notes.md` §92.

## Auto-file customs from HS6? Invent HS strings?

No, and no. jev-hs-assistant HS6. Choice over legal 2022.0 children. Post always blocked. Mock if no key. `notes.md` §92.

## Treat SC2 API Victory as a UI win? Quote Zero Hour as completed?

No, and no. golergka/jev-plays-starcraft-2 UI-verified ≠ API Victory. Liberation Day 3:44 / Outlaws 27:57 *theirs*; Zero Hour uncompleted. `notes.md` §92.

## Treat awesome-jev-use-cases likes as eval? Collapse into awesomejev.com?

No, and no. awesome-jev-use-cases catalog. Unofficial. **≠** awesomejev.com census. `notes.md` §92.

## Is typesafe-go official TypeSafe? A new species?

No, and no. Nibir1/typesafe-go ≠ official. Analyzers catch bad questions at build time. **≠** rust community SDK. soft Noul ≠ hard safety. `notes.md` §92.

## Treat a ledger HIT as correctness?

No. Cache hit ≠ correctness. A HIT is a sensor
(same schema+state saw this answer), not a proof
the answer is right. Sharing foreign fingerprints
as calibrated truth is trust theater. rh-guard
owns the HIT-as-truth gate cousin; Augustus owns
placement. Unique fragments (consecutive): fingerprint after redact; recall vs decide; publish fingerprints+answers; CI replay as Harbor cousin; Cache hit ≠ correctness; hyperspaceai/jevcache ≠ kushals256/jevcache; human labels only; score never auto-accepts; production capture flywheel; sutro-sh/jev-align ≠ caiovicentino/jev-align
`notes.md` §93.

## Collapse hyperspaceai/jevcache into kushals256/jevcache?

No. hyperspaceai/jevcache ≠ kushals256/jevcache.
Hyperspace is decision-space memoization
(fingerprint after redact; recall vs decide;
publish fingerprints+answers; CI replay as Harbor
cousin). kushals256 is same-intent LLM-completion
admit (0 FP/100 *theirs*). Not Hyperspace KV
attention cache. Do not copy `curl | sh`.
`notes.md` §93.

## Auto-accept a GEPA proposal because the training score rose?

No. score never auto-accepts. human labels only.
A higher training score is a sensor, not an
accept. Soft Noul ≠ hard safety. rh-guard owns
the training-score auto-accept gate cousin
(Sutro already refuses). `notes.md` §93.

## Is sutro-sh/jev-align caiovicentino/jev-align?

No. sutro-sh/jev-align ≠ caiovicentino/jev-align.
Sutro is a GEPA definition-optimizer with a human
taste gate and a production capture flywheel.
caiovicentino (MIT JS) is a calibrated alignment
*verifier* (pass/flag/block heads). Not Archer.
Not a PreToolUse hard gate. Do not copy `uv` /
keys. `notes.md` §93.

Unique fragments (consecutive): guidance ≠ hook; catalysts ≠ summaries; compile-time System One; unofficial ≠ TypeSafe; format_version modernbert-jev/1; Argos1111/jev_local ≠ us/jev-local ≠ kunchenguid/local-jev; LFM default ≠ ModernBERT backend; Nemotron ≠ TypeSafe Jev; not a calibrated replacement; djev-dev complements djev-spark; images as Choice options; Laya essay numbers *theirs*; Router/OOD confidence; hosted bootstrap ≠ silent TypeSafe

## Hard-gate enzyme `when asked` / catalyst similarity as PreToolUse deny?

No. guidance ≠ hook. Compiled `when asked` is
attention, not a deny. catalysts ≠ summaries.
compile-time System One: Jev shapes the question
program at compile; runtime retrieval is catalyst
handles. Soft Noul ≠ hard safety. rh-guard owns
the PreToolUse cousin. Do not copy `curl | bash`.
hosted bootstrap ≠ silent TypeSafe.
`notes.md` §94.

## Are enzyme catalysts summaries? Collapse into jev-sift / findme?

No, and no. catalysts ≠ summaries. They are
questions the corpus is good at answering. Kinship
with jev-sift / findme / jev-semgrep is VOI /
search-control, not identity. Always write
**byenzyme/enzyme**. **≠** enzymejs/enzyme.
`notes.md` §94.

## Is unofficial JA ModernBERT TypeSafe Jev? Skip format_version?

No, and no. unofficial ≠ TypeSafe. format_version
modernbert-jev/1. Card *theirs*: does not
reproduce Jev training/accuracy. JNLI 92.62% /
JComQA 92.40% are *theirs*. `notes.md` §94.

## Is Argos1111/jev_local us/jev-local or kunchenguid/local-jev?

No. Argos1111/jev_local ≠ us/jev-local ≠
kunchenguid/local-jev. Underscore runtime.
us/jev-local is stub-until-hf. kunchenguid is
ONNX English measured not equivalent. **≠**
githubnext/localjev. LFM default ≠ ModernBERT
backend: default is LFM2.5 text/vision logprob;
the unofficial JA checkpoint is the optional
ModernBERT backend (text/JSON; images 422).
Do not collapse the runtime into the Hub card.
`notes.md` §94.

## Is Nemotron_Jev a calibrated TypeSafe Jev replacement?

No. Nemotron ≠ TypeSafe Jev. not a calibrated
replacement. Dense Nemotron-Labs-Diffusion-14B
adapter; name is the interface. 72/72 synthetic
*theirs* is not Harbor. rh-guard owns.
Do not copy docker. `notes.md` §94.

## Treat enzyme hosted bootstrap as TypeSafe Jev? Silent FALLBACK?

No. hosted bootstrap ≠ silent TypeSafe. README
*theirs*: explicit key → local model → anonymous
brokered free config. Name which backend answered.
rh-guard owns the silent-FALLBACK cousin.
`notes.md` §94.

## Is djev-dev djev-spark or githubnext/localjev? Does it ship pixels as TypeSafe CU?

No, and no. djev-dev complements djev-spark.
images as Choice options (native image input;
live camera). Complements mmastrac; no new
weights. **≠** typesafe-computer-use (that never
ships a screenshot for the *decision*). **≠**
githubnext/localjev prompted JSON. `notes.md` §94.

## Paste the Laya essay vs-Jev table as a new bake-off? Treat Khmer 0.952 conf as competence?

No, and no. Laya essay numbers *theirs*. Already
§76 via NandhaKishorM/laya. Router/OOD
confidence: Khmer 0.000 @ 0.952 is
confidence-without-competence; route before the
forward pass. Not a new species. Do not copy
`pip install laya`. `notes.md` §94.

Unique fragments (consecutive): difficulty + policy thresholds + JSONL trace; jev-codex-pilot model + reasoning depth; keep/shadow/hybrid/reject; quarry evidence projection; Frank-ZY-Dou/awesome-jev robotics/3D/control; one-dollar-tahoe TypeSafe Jev defense eval; jevguard calibrator/cache/escape; jev-ci-selector CI shadow mode; llama-jev llama.cpp replica; petercr/jev-orchestrator ≠ FleeexCorp/jev-orchestrator; seb4ez/jevguard ≠ AseemPrasad/JevGuard ≠ pablozr/JevGuard; webNeat/llama-jev ≠ WiktorB2004/llama-index-jev

## Does jev-orchestrator pick an LLM by difficulty? Paste 0.95 as Harbor τ?

No, and no. difficulty + policy thresholds + JSONL trace. GitHub description says LLM routing; live code is next-action Choice. FINISH blocked until validation. Mock without a key. petercr/jev-orchestrator ≠ FleeexCorp/jev-orchestrator. `notes.md` §95.

## Is jev-codex-pilot a measured bake-off? Collapse into the orchestrator?

No, and no. jev-codex-pilot model + reasoning depth. Thin marketing overlay + Kanban. Config is gateway key + provider. `notes.md` §95.

## Is keep a failed migration? Force BERT/RAG onto Jev?

No, and no. keep/shadow/hybrid/reject. 20-case *theirs* failed the **cost** gate; LLM remains fallback. Round 2 kept BERT/RAG. License null. `notes.md` §95.

## Summarize quarry pages? Fail-closed if Jev is down? Collapse into savka777/jev-search?

No, no, and no. quarry evidence projection. Pointer, never paraphrase. 5 s fail-open. p&lt;0.5 dropped; top 3 ranges. **≠** savka777/jev-search. `notes.md` §95.

## Is Frank-ZY-Dou/awesome-jev walidboulanouar/awesome-jev-use-cases? Paste OpenRoboto $ as a success-rate? Send pixels?

No, no, and no. Frank-ZY-Dou/awesome-jev robotics/3D/control. Text-state, not pixels. One seed-0 trial *theirs*. Do not re-card jev-drone / khordoo / HA-Jev. `notes.md` §95.

## Quote one-dollar-tahoe ASR/FPR? Copy the attack list? Treat 74 rows as Harbor?

No, no, and no. one-dollar-tahoe TypeSafe Jev defense eval. README has **no ASR/FPR**. Static ~74 demo, not a powered bench. Do not copy `attacks.json`. rh-guard owns the gate cousin. `notes.md` §95.

## Is jevguard hyperspaceai/jevcache? Skip the escape? Treat 0.40 as Harbor τ?

No, no, and no. jevguard calibrator/cache/escape. `UNRESOLVED_OR_OTHER`; `AMBIGUOUS_STATE` top p&lt;0.40 or margin&lt;0.15. Volatile fields masked. **≠** jevcache. seb4ez/jevguard ≠ AseemPrasad/JevGuard ≠ pablozr/JevGuard. `notes.md` §95.

## Skip CI from skip_below 0.05? Is shadow the same as enforce?

No, and no. jev-ci-selector CI shadow mode. Shadow default; enforce opt-in. 0.05 is an experiment, not a guarantee. Timeout/no-key → keep all. Mandatory/path rules beat Jev. rh-guard owns. `notes.md` §95.

## Is llama-jev TypeSafe / a Noul? Paste 80 ms as a class ceiling?

No, and no. llama-jev llama.cpp replica. Numbered-choice softmax ≠ Noul. 80 ms cold / 40 ms cache *theirs* on minicpm5-2b-q8. **≠** TypeSafe **≠** pcdServer **≠** chakuho. webNeat/llama-jev ≠ WiktorB2004/llama-index-jev. License null. `notes.md` §95.

Unique fragments (consecutive): OpenCode jev-pruner context sieve; observe→score-candidates→prune; jev-zen / jev-1.13-free; zen-chat ≠ Noul; fail-open original; keepScore >0.1 floor; host port of tamaratran/jev-pruner; indiejoseph/opencode-jev-pruner ≠ nrdz-labs/fast-jev-opencode; jev-webagent-bench empty stub; Kiln-AI/jev_jsonschema noul_threshold 0.5; NSStudent/JevSwiftSDK unofficial

## Is indiejoseph/opencode-jev-pruner tamaratran/jev-pruner? Is it fast-jev-opencode session compaction?

No, and no. OpenCode jev-pruner context sieve. host port of tamaratran/jev-pruner. Same stdout job (`tool.execute.after` on `bash`); different host. **≠** nrdz-labs/fast-jev-opencode (session compaction, §62). GitHub license **null**; `package.json` MIT; **0★**. `notes.md` §96.

## Is zen-chat a Noul? Paste tamaratran 24/24 / 83% as this product’s Harbor?

No, and no. zen-chat ≠ Noul. Default is jev-zen / jev-1.13-free (native System One, keyless). Chat scorer is an approximation; unparseable scores keep. Tests are mapper/retry/zen-scorer/auth, not a prune-quality bench. Do not copy upstream 24/24. `notes.md` §96.

## Fail-closed the OpenCode turn if Jev is down? Treat keepThreshold 0.5 as proof of irrelevance?

No, and no. fail-open original. keepScore >0.1 floor. Hook catch leaves stdout. Hard-gating 0.5 as drop is soundness theater. `notes.md` §96.

## Quote jev-webagent-bench scores? Treat JSON Schema boolean @ 0.5 as a safety proof? Is JevSwiftSDK official?

No, no, and no. jev-webagent-bench empty stub (size 0; 409 empty repo). Kiln-AI/jev_jsonschema noul_threshold 0.5 is a decoder; probabilities are returned. NSStudent/JevSwiftSDK unofficial. Packaging ≠ new species. `notes.md` §96.

Unique fragments (consecutive): GLiNER2 native Apple path; unofficial Swift/Core ML GLiNER 2.5-small; entity spans + confidence; not Choice/Score/Noul; not TypeSafe; label descriptions as schema; on-device ANE economics; honesty locks; shershah1024/gliner-native-runtime ≠ Fastino; ≠ gliner25-compaction ≠ gliner2-ultrafast ≠ Eran-BA/Jev_from_GLiNER2 ≠ NSStudent/JevSwiftSDK ≠ jevmlx; default threshold 0.1 still soft

## Is gliner-native-runtime TypeSafe Jev / Choice/Score/Noul / Fastino official?

No, no, and no. GLiNER2 native Apple path. unofficial Swift/Core ML GLiNER 2.5-small. entity spans + confidence. not Choice/Score/Noul. not TypeSafe. Fastino owns `fastino/gliner2.5-small-v1`. shershah1024/gliner-native-runtime ≠ Fastino. Apache-2.0; **4★**. `notes.md` §97.

## Collapse it into gliner25-compaction / gliner2-ultrafast / Eran-BA / JevSwiftSDK / jevmlx?

No. ≠ gliner25-compaction ≠ gliner2-ultrafast ≠ Eran-BA/Jev_from_GLiNER2 ≠ NSStudent/JevSwiftSDK ≠ jevmlx. Locate on-device, not compaction, not computer-use, not a Choice/Score/Noul spec, not a TypeSafe Swift SDK, not MLX schema→JSON. honesty locks. `notes.md` §97.

## Paste README 0.99 as Harbor? Hard-gate default 0.1 as NER quality? Invent ANE latency?

No, no, and no. default threshold 0.1 still soft. README fixture is a demo. No published Harbor / ECE / ANE ms. Soft Noul ≠ hard safety. label descriptions as schema. on-device ANE economics. `notes.md` §97.

## File it as extractive keep/drop of held candidates? Call it composition position 4 Selector?

No, and no. schema→spans locate. Position 10 discretizer/encoder, not position 4 Selector of F, not keep/drop of offsets code already holds. `notes.md` §97.

Unique fragments (consecutive): Decision Graph Protocol frame→assess→commit; app retains permissions/effects; Jev-first assessor-neutral; guarded commit / receipt/next frame; assessment batching; hard-gating DGP as safety theater; numerous-com/dgp ≠ TypeSafe official; jegrep calibrated path+range Nouls; no embeddings/index/daemon; ~$0.01–0.03 typical; agent --json; can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep; Archer-arch fidelity; kev family OOD 0.76–0.77 vs Jev 0.86; block-causal isolation; pointer/readout CE-trained; /v1/systemone drop-in; replica honesty

## Is numerous-com/dgp an official TypeSafe spec? Does an assessment p grant an effect? Is a receipt proof the decision was right?

No, no, and no. Decision Graph Protocol frame→assess→commit. app retains permissions/effects. Jev-first assessor-neutral. guarded commit / receipt/next frame. assessment batching. A model is neither a security boundary nor the source of execution authority (*theirs*). Speculative assessments cannot authorize effects. numerous-com/dgp ≠ TypeSafe official. **≠** waymode **≠** ctmx/openrouter-jev-mcp Decision-as-Plugin **≠** petercr/jev-orchestrator **≠** AgentGhost. ThreadDesk mocks ≠ live Jev. 106 tests are sensors, not a Harbor quality headline. Python MIT; **0★**. `notes.md` §98.

## Hard-gate DGP as a safety proof / collapse ThreadDesk mocks into live Jev quality / copy mock tokens as a recipe?

No, no, and no. hard-gating DGP as safety theater. Treating a typed assessment p as permission, or the receipt as a proof the decision was *right*, is the same theater as jev-gate §79. Soft Noul ≠ hard safety. Do not copy `DGP_AGENT_TOKEN` / `uv run` / keys. `notes.md` §98.

## Is can1357/jegrep Bentlybro/jevgrep? Is it uehaj/jev-semgrep? Paste jevgrep 79% onto jegrep?

No, no, and no. can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep. jegrep calibrated path+range Nouls. no embeddings/index/daemon. ~$0.01–0.03 typical. agent --json. Rust MIT; **13★** this pass (watch ★12). No published Harbor needle/noise table. Ranking fail-open. **≠** JevFind **≠** quarry **≠** jevex. `notes.md` §98.

## Hard-gate 0.4/0.2 as “the concept is absent”? Paste $0.01–0.03 as a class ceiling? Copy cargo install / OpenRouter keys?

No, no, and no. Thresholds are sensors. Live tree means no stale index; it also means you pay per search. Soft Noul ≠ hard safety. Do not copy `cargo install` / `OPENROUTER_API_KEY` / `TYPESAFE_API_KEY` / `~/.env`. `notes.md` §98.

## Is kev OOD 0.76 Jev-equivalent? Does isolation 4e-6 prove kev = Jev? Is `/v1/systemone` wire a calibrated Noul? Did Archer land?

No, no, no, and no. Archer-arch fidelity. kev family OOD 0.76–0.77 vs Jev 0.86. block-causal isolation. pointer/readout CE-trained. /v1/systemone drop-in. replica honesty. Mechanism tests falsify “questions leak”; they do not prove identity. Do not rewrite §45. Jev-omni owns the replica/code fold. Archer still **NOT landed** (tracker likes **51**; lastModified UNCHANGED 2026-09-19T18:37:18Z; Hub `archerhume/4rcherhume` HTTP **401**). Do not treat kev-8b or Qwen3.8-27B as the 27B drop. Apache-2.0; **507★**. `notes.md` §98.
