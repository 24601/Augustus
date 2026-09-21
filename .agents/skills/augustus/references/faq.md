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
is a **late-catch rewrite** of that same repo (`notes.md` §99):
GitHub description still says sub-15ms NAR local drop-in (**43★**
live REST); README this pass claims Von-1.0 **395M / 1.5 GB**,
~**62 ms** MPS / ~**300 ms** CPU on **n=78**, Hub
[`wfzyx/von-1.0`](https://huggingface.co/wfzyx/von-1.0) ModernBERT-large
finetune. Do **not** merge the §49 Needle 52.6% table with the
78-case 93.0% table. Competing NAR claims / replica honesty.
"Guaranteeing" calibration is theater. Wire-compat ≠ Noul.
Do not copy its vs-Jev table. Do not dump weights.
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


## Is JCR a skill loader?

No. [NiazMorshed2007/jcr](https://github.com/NiazMorshed2007/jcr)
is a **capability resolver**. Skills = workflow+judgment;
capabilities = individual operations; format independent of
Jev (*theirs*). One tool finds documented deterministic
commands in a nested capability tree and **returns context**.
It **does not execute**. Distinct from skill-broker (grants),
skillranker (advisory VOI over skills), jev-sift (classify
path/url/text), jev-lens (pre-send views), jevusher
(token admission), and Codex `jev_select_capability`.
`notes.md` §116.

## Does a 0.6 band authorize the returned command?

No. Soft scores ≠ hard gates. `JCR_BAND_RATIO` 0.6 is
application policy: keep up to 3 paths ≥60% of the best
geometric-mean routing score. Routing ≠ permission. Docs ≠
authority to run. A match can still be wrong (*theirs*).
The harness still supplies values, credentials, order, and
checks. `notes.md` §116.

## Did JCR win a Harbor task-execution bench?

No. `sol-vs-opus5-20` *theirs* is lookup+explain only, 20
scenarios × 4 variants = 80 runs, n=1 per cell. Token and
cost fell in both harnesses; wall time mixed (Sol slower
with JCR in 19/20; one 372.6s / 193 Jev-call outlier).
Not Harbor task-execution. Do not steal −85% as a class
constant. `validation.md`; `notes.md` §116.

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

No. **Always qualify the owner.** Canonical GitHub name
is now [mizchi/jev-lint](https://github.com/mizchi/jev-lint)
(rename of [mizchi/jevlint](https://github.com/mizchi/jevlint);
same SHA; `jevlint` redirects — not a second product).
ast-grep subjects × sentence `ask:` (matcher silent, Jev
loud; 13/15 1.00/1.00 older corpus *theirs*; ~1 in 5
findings wrong *this README*).
[huntedman/JevLint](https://github.com/huntedman/JevLint)
is file-level convention Nouls (§26). Independent of
eslint-plugin-jev. `notes.md` §26, §70, §100.

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
**PR #1 now closed unmerged** (was Open at §71): throughput misread as
latency; Laya gap inside the 95% CI (parity, not SOTA);
correctness-head ECE is not distribution ECE (Jev 14.40%
slightly lower like-for-like). 107★ densify; GH 151M vs README 149.6M.
do not re-fold §71 claim-audit as a beat. Distinct from
IamBusy/OpenJev `/v1/decide`. `notes.md` §71 / §107.

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

No, no, and no. can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep. jegrep calibrated path+range Nouls. no embeddings/index/daemon. ~$0.01–0.03 typical. agent --json. Rust MIT; **13★** this pass (watch ★12). No published Harbor needle/noise table. Ranking fail-open. OpenRouter/TypeSafe auto-failover is silent FALLBACK, not the same Noul. **≠** JevFind **≠** quarry **≠** jevex. `notes.md` §98.

## Hard-gate 0.4/0.2 as “the concept is absent”? Paste $0.01–0.03 as a class ceiling? Copy cargo install / OpenRouter keys?

No, no, and no. Thresholds are sensors. Auto-τ-lowering across rounds is ranking fail-open, not a 0.4 proof. Live tree means no stale index; it also means you pay per search. Soft Noul ≠ hard safety. Do not copy `cargo install` / `OPENROUTER_API_KEY` / `TYPESAFE_API_KEY` / `~/.env`. `notes.md` §98.

## Treat OpenRouter/TypeSafe auto-failover as the same calibrated Noul? Treat a later-round hit as a 0.4 proof?

No, and no. README *theirs*: with both keys set, 401/402/403/408/429/5xx, transport failures, and invalid responses automatically fail over. That swap still emits path+range Nouls — silent FALLBACK (classifier-dev cousin). Pin `--endpoint`. Mixing providers as one Noul is soundness theater. rh-guard owns the silent-FALLBACK cousin. `notes.md` §98.

## Is kev OOD 0.76 Jev-equivalent? Does isolation 4e-6 prove kev = Jev? Is `/v1/systemone` wire a calibrated Noul? Did Archer land?

No, no, no, and no. Archer-arch fidelity. kev family OOD 0.76–0.77 vs Jev 0.86. block-causal isolation. pointer/readout CE-trained. /v1/systemone drop-in. replica honesty. Mechanism tests falsify “questions leak”; they do not prove identity. Score confidence is a stand-in (*theirs*); TypeSafe has not published theirs. Do not rewrite §45. Jev-omni owns the replica/code fold. Archer still **NOT landed** (tracker likes **51**; lastModified UNCHANGED 2026-09-19T18:37:18Z; Hub `archerhume/4rcherhume` HTTP **401**). Do not treat kev-8b or Qwen3.8-27B as the 27B drop. Apache-2.0; **507★**. `notes.md` §98.

Unique fragments (consecutive): cost-sensitive decision theory × System One probabilities → control flow; thresholds derived from costs not hard-coded; YES / NO / UNSURE from cost_false_yes / cost_false_no / cost_human; auto-batching same-object questions; Kungie/gut ≠ tpellet/hunch ≠ carldaws/hunch; judgment vs generation; deterministic execution after probabilistic judgment; exactly one app-owned callback; explicit uncertain branch; Illusion47586/judge ≠ lexingtonhibiki/judgekit ≠ Ascurse/typed-judge-kit; variable-N option scoring as the trainable object; dynamic candidate bags not fixed label sets; zwliJay/jev-forge ≠ NanoJev; open replica economics / latency vs closed Jev; NAR local drop-in; wfzyx/von late-catch HIGH; competing NAR claims / replica honesty; typed judgments vs chat judges on guardrailing; ishaannk/llm-vs-jev cross-note only; deeper integrity fold is rh-guard; nothing wins outright; can be argued out of guarding

## Are gut / Judge new class-table species? Hard-gate cost-derived 0.038 as a proof? Let UNSURE silently become False?

No, no, and no. Overlays on EU / Chow / Elkan and on typed control flow. cost-sensitive decision theory × System One probabilities → control flow. thresholds derived from costs not hard-coded. YES / NO / UNSURE from cost_false_yes / cost_false_no / cost_human. auto-batching same-object questions. Default `on_unsure="raise"` *theirs* is **application policy** (truthiness / exception), **not** a System One hard gate. `min_confidence` is a spread filter, not P(correct) (DECISIONS *theirs*). Kungie/gut ≠ tpellet/hunch ≠ carldaws/hunch. GitHub Apache-2.0 / LICENSE MIT / pyproject Apache-2.0 *theirs*; **0★**; pre-alpha target design. Soft Noul ≠ hard safety. `notes.md` §99.

## Is Illusion47586/judge lexingtonhibiki/judgekit? Does it generate or execute code? Is the uncertain branch optional theater?

No, no, and no. judgment vs generation. deterministic execution after probabilistic judgment. exactly one app-owned callback. explicit uncertain branch. Provider-neutral core; Jev default. Never executes provider-generated code; never evaluates multiple callbacks speculatively (*theirs*). Illusion47586/judge ≠ lexingtonhibiki/judgekit ≠ Ascurse/typed-judge-kit ≠ 2389-research/judgement ≠ Kungie/gut. TypeScript MIT; **0★**; `@brkn-labs/judge` 0.1.0 pre-release. `notes.md` §99.

## Is jev-forge a sixth species? Clone the Hub weights / Mind2Web corpora? Paste 0.579/0.637 as Harbor?

No, no, and no. variable-N option scoring as the trainable object. dynamic candidate bags not fixed label sets. Class-architecture note on the decide family, not GLiClass categorize, not TypeAR decode. zwliJay/jev-forge ≠ NanoJev. GitHub license NOASSERTION; LICENSE file MIT *theirs*; **1★**. MODEL_CARD *theirs*: candidate discovery is the caller’s; not a browser-agent leaderboard. Do not clone weights. `notes.md` §99.

## Is wfzyx/von still the 14 MB Needle? Is sub-15ms the 62 ms table? Does it guarantee calibration? Dump von-1.0 weights?

No, no, no, and no. wfzyx/von late-catch HIGH. NAR local drop-in. open replica economics / latency vs closed Jev. competing NAR claims / replica honesty. GitHub description still sub-15ms (**43★**); README this pass 395M / ~62 ms MPS / n=78 93.0% *theirs*; Hub `wfzyx/von-1.0` ModernBERT-large. Do not merge §49 Needle 52.6% with this table. “Guaranteeing” calibration is theater (two temperatures T=1.0367 / T=1.1692 in one README). Wire ≠ Noul. Do not dump weights. `notes.md` §99.

## Did Jev win LLM guardrailing? Is ishaannk/llm-vs-jev a Harbor taskset? Does Augustus own the steerability fold?

No, no, and no. typed judgments vs chat judges on guardrailing. nothing wins outright. Pareto *theirs*: jev / opus / astra. Jev is the cheap end (77.9% / ECE 0.053 / 679 ms / $0.0444). can be argued out of guarding (opus 14.3% / jev 10.7% *theirs*). ishaannk/llm-vs-jev cross-note only. deeper integrity fold is rh-guard. Apache-2.0; **0★**. Do not copy `uv` / keys. `notes.md` §99.

## Did Archer land this hour? Treat Qwen/Qwen3.8-27B as Archer? Invent tweets?

No, no, and no. Hub `archerhume/4rcherhume` HTTP **401**. `Qwen/Qwen3.8-27B` HTTP **200** likes **15762** lastModified **2026-08-14T15:00:01Z**, author Qwen — ≠ Archer. Tracker likes **51** flat; lastModified UNCHANGED `2026-09-19T18:37:18.000Z`. X MCP flap: since_id held `2100958005663568282`; pages_archived 0; invented_signal: false. Live REST: SemIf **1936★**; jevlike **983★** (watch claimed 984); TypeAR-AI/TypeAR **11★** flat. Awesomejev 561/27007 user-provided. `notes.md` §99.

Unique fragments (consecutive): Jev IS the if-statement; judgments/probabilities drive branches; text model only writes prose; interpreter owns variables/loops/budgets/replay; otherwise maybe / confidence gate; chaos samples after the gate; southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠ Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably; 133★ / forks 10 live; build calibrated classifiers from human feedback; retrieve by relevance not resemblance; one calibrated yes/no per memory in one request; pointer mode 17/18 19/20 *theirs*; embedding resemblance misses the allergy; samdotmak/jev-recall ≠ jev-search ≠ jev-sift ≠ carryforward ≠ chopratejas/invalidate; memory leases ended by new evidence; six Nouls then fixed rules in code; 0 of 157 false invalidations; questions/plans/directives are not evidence; unsure → review queue; host keeps the store; name↔body / comment truth / test-claims; mizchi/jev-lint is mizchi/jevlint rename; no shipped rule has severity error; ~1 in 5 findings wrong *theirs*; mizchi/jev-lint ≠ huntedman/JevLint ≠ MichitoSugawara/jev-lint; JSON Schema → typed JSON via Jev; noul_threshold 0.5 decoder not a proof; IncompatibleSchemaError lists every bad property; on-device Laya CoreML ANE; ~5 ms P50 short decisions; 189/189 FP16 checkpoint parity; 10× not achieved; mizorewww/laya-coreml ≠ gliner-native-runtime ≠ jevmlx ≠ NandhaKishorM/laya; softmax over allowed tokens ≠ Noul; question-first cache; Micha0827/snapjudge ≠ githubnext/localjev ≠ jevmlx ≠ cendress/SnapJudge; Jev-first Pi agent loop; slow-LLM fallback; explicit action menu / CandidateSource unimplemented; 62 tests wiring not quality; direwolfiy/JevPi ≠ standardagents/jevpilot ≠ pi-jev-control

## Is southpolesteve/probably a hunch / feelings / gut / Judge overlay? Is it tidymodels/probably? Does the hosted playground run live Jev?

No, no, and no. Jev IS the if-statement. judgments/probabilities drive branches. text model only writes prose. interpreter owns variables/loops/budgets/replay. otherwise maybe / confidence gate. chaos samples after the gate. Language, not a library overlay. Hosted playground streams **recorded** runs of bundled examples. TypeScript MIT; **3★**; HEAD `6bf671a4`; README SHA `c28570a9`; package `probably-lang` 0.1.0. southpolesteve/probably ≠ carldaws/hunch ≠ feelings ≠ Kungie/gut ≠ Illusion47586/judge ≠ tidymodels/probably. Soft Noul ≠ hard safety. `notes.md` §100.

## Hard-gate `feels` 80% as a safety proof? Treat chaos as a calibrated sample of the posterior? Copy bun / Cloudflare / JEV_API_KEY?

No, no, and no. 80% / default 50% loop gate / five-iteration cap / 12-effect budget are sensors + interpreter limits. Chaos samples **after** the confidence gate. Do not copy `bun` / `.env` / Cloudflare tokens. `notes.md` §100.

## Re-dump sutro-sh/jev-align? Did the mechanism change? Collapse it into caiovicentino/jev-align?

No, no, and no. 133★ / forks 10 live. build calibrated classifiers from human feedback. HEAD `49753df9` / README SHA `363fccb7` **unchanged** vs §93. human labels only. score never auto-accepts. production capture flywheel. sutro-sh/jev-align ≠ caiovicentino/jev-align (**4★** verifier). Do not copy `uv` / keys. `notes.md` §100.

## Retrieve by embedding resemblance? Paste pointer 17/18 as Harbor? Treat a miss as “the fact is absent”?

No, no, and no. retrieve by relevance not resemblance. one calibrated yes/no per memory in one request. pointer mode 17/18 19/20 *theirs*. embedding resemblance misses the allergy. The H-1B miss needs outside knowledge. samdotmak/jev-recall ≠ jev-search ≠ jev-sift ≠ carryforward ≠ chopratejas/invalidate. Python + TypeScript MIT; **6★**; HEAD `d3e4acfb`; README SHA `ea774519`. `notes.md` §100.

## Hard-gate 0 of 157 false invalidations as a proof on *your* data? Treat questions/plans/directives as evidence? Let the adapter own the store?

No, no, and no. memory leases ended by new evidence. six Nouls then fixed rules in code. 0 of 157 false invalidations. questions/plans/directives are not evidence. unsure → review queue. host keeps the store. Thresholds tuned on that same 157 — treat as optimistic. Apache-2.0; **11★** (HIGH upgrade of §66 MED ★5); HEAD `d6ade601`; README SHA `8cccad5f`. chopratejas/invalidate ≠ jev-recall ≠ CloudFront `invalidate-*`. `notes.md` §100.

## Is mizchi/jev-lint a second product from jevlint? Fail CI on a shipped warning? Collapse into huntedman/JevLint?

No, no, and no. name↔body / comment truth / test-claims. mizchi/jev-lint is mizchi/jevlint rename (same created_at, HEAD `62d73f8e`, README SHA `4c0e37cd` byte-identical; `mizchi/jevlint` redirects). no shipped rule has severity error. ~1 in 5 findings wrong *theirs*. Fail open: no-verdict ≠ clean. TypeScript MIT; **13★**. mizchi/jev-lint ≠ huntedman/JevLint ≠ MichitoSugawara/jev-lint. `notes.md` §100.

## Is JSON Schema boolean @ 0.5 a safety proof? Does IncompatibleSchemaError hide remaining bad properties? Is this TypeSafe official?

No, no, and no. JSON Schema → typed JSON via Jev. noul_threshold 0.5 decoder not a proof. IncompatibleSchemaError lists every bad property. HIGH upgrade of §96 MEDIUM; HEAD `fccea8c2` / README SHA `f3c94957` **unchanged**. Python MIT; **5★**. **≠** TypeSafe official SDK **≠** TypeAR **≠** jevmlx. `notes.md` §100.

## Paste ANE 4.98 ms as “beats Jev”? Claim 10×? Select `cpu_ne` on the ordinary export? Collapse into gliner-native-runtime?

No, no, no, and no. on-device Laya CoreML ANE. ~5 ms P50 short decisions. 189/189 FP16 checkpoint parity. 10× not achieved. Ordinary `cpu_ne` does **not** reproduce. Apache-2.0; **0★**; HEAD `47f4baf0`; README SHA `2068c661`. mizorewww/laya-coreml ≠ gliner-native-runtime ≠ jevmlx ≠ NandhaKishorM/laya ≠ mizorewww/laya-mlx. `notes.md` §100.

## Is snapjudge softmax a Noul? Is it githubnext/localjev? Paste 87.7 vs 81.2 as identity? Is it Archer?

No, no, no, and no. softmax over allowed tokens ≠ Noul. question-first cache. Independent project, not affiliated with TypeSafe (*theirs*). Probabilities are **not proven to be calibrated**. Python MIT; **3★**; HEAD `2df5ce27`; README SHA `64a91458`. Micha0827/snapjudge ≠ githubnext/localjev ≠ jevmlx ≠ cendress/SnapJudge ≠ Qwen3.8-27B-as-Archer. `notes.md` §100.

## Is JevPi jevpilot? Are 62 tests a quality headline? Is CandidateSource implemented?

No, no, and no. Jev-first Pi agent loop. slow-LLM fallback. explicit action menu / CandidateSource unimplemented. 62 tests wiring not quality. GitHub license **null**; **0★**; HEAD `980f8895`; README SHA `88ec1a55`; GitHub `size` **0** with contents present. direwolfiy/JevPi ≠ standardagents/jevpilot ≠ pi-jev-control. `notes.md` §100.

## Did Archer land this hour? Treat Qwen3.8-27B as Archer? Invent tweets?

No, no, and no. Last pin from §99: Hub `archerhume/4rcherhume` HTTP **401**. Tracker likes **51** flat; lastModified UNCHANGED `2026-09-19T18:37:18.000Z`. Not re-fetched as a rewrite. Live REST pulse: SemIf **1954★** (+18 vs §99 **1936**); jevlike **989★** (+6 vs §99 **983**); TypeAR **11★** flat. AnotiaWang/awesome-jev **83★** ≠ Awesomejev 561/27007. `invented_signal: false`. `notes.md` §100.

Unique fragments (consecutive): resume-screening bias audit methodology; name×resume factorial independent Nouls; callback determined by resume quality; mean-probability name gaps operationally negligible; natemoo-re/bias-bench ≠ BBQ; Plan/PRD panel → code-owned pass|review|block; cheerleading out of scope; austindixson/planalyzer ≠ single-goodness Noul; cost-aware multi-model routing/escalation; decide vs do; successful-task cost; cannacre8ive/switchboard-ai ≠ ha-switchboard ≠ hermes-switchyard; frozen-protocol zero-shot bench; TypeSafe Jev vs PrismNLI vs Laya; contamination caveat; elcronos/jev-vs-open-decision-models ≠ JevBench ≠ DMB; context-window admission control; VOI gate which tokens are worth the expensive model; fail polarity per lens; on small inputs lenses lose money; cvsgireesh/jevusher ≠ jev-sift ≠ winnow; typed decision control plane; receipt ≠ authorization; historical-v0 zero retained cases; MokiMeow/jev-fabric ≠ jev-forge ≠ dgp; live 15-dim typed rubric re-score per pause; scoring economics exemplar; OpenJev/Codiv ≠ TypeSafe hosted; jose-troche/live-rubric ~$0.000004 desc / ~$0.000006 README; adversarial pre-registered Jev eval; 28 predictions before data; 123,805 requests; confidence does not track ignorance; polite injection 65% / crude 0%; willkelly/jev-evaluation ≠ jevals ≠ jev-baselines-eval; provider-neutral Elixir/BEAM Noul/Choice/Score SDK; class infrastructure; nshkrdotcom/system_one_sdk ≠ typesafe_sdk ≠ dannote/jev

## Is bias-bench BBQ? Treat a zero binary name gap as a fairness certificate? Hard-gate callback @ 0.5 as hiring policy?

No, no, and no. resume-screening bias audit methodology. name×resume factorial independent Nouls. callback determined by resume quality. mean-probability name gaps operationally negligible. 1,824 independent Nouls; callback perfectly determined by resume quality; mean-p gaps ~0.4–0.6pp *theirs*, opposite the human audit, operationally negligible. Permutation p-values are function properties — read the magnitudes. JavaScript; license **null**; **0★**; HEAD `fe2f2535`; README SHA `a1c3e604`; GitHub size **0** with contents. natemoo-re/bias-bench ≠ BBQ. Soft Noul ≠ hard safety. `notes.md` §101.

## Does planalyzer let Jev emit pass|review|block? Is it a single-goodness Noul? Hard-gate 0.72 as a merge seal?

No, no, and no. Plan/PRD panel → code-owned pass|review|block. cheerleading out of scope. One batched System One call; **code** owns the verdict from `panel.json` (`noul_block_threshold` 0.72 / `noul_review_threshold` 0.4 / `severity_block_at` 2.0; invert literalist/scope). Choice `recommended_next_step` is advisory. Python MIT; **0★**; HEAD `39fc161f`; README SHA `6e4d8da3`. austindixson/planalyzer ≠ single-goodness Noul. `notes.md` §101.

## Is switchboard-ai ha-switchboard? Is the routing smoke a Harbor? Are M4 provider adapters done?

No, no, and no. cost-aware multi-model routing/escalation. decide vs do. successful-task cost. README V0.4 / package **0.4.0** match this pass; ARCHITECTURE M1–M5 functional (M4 least-privilege logical tool plans; M5 supervisor + workflow DAG); provider-specific MCP adapters and learned economics **not** done. JavaScript MIT; **1★**; HEAD `5cae9d1c`; README SHA `872de837`. cannacre8ive/switchboard-ai ≠ ha-switchboard ≠ hermes-switchyard. `notes.md` §101.

## Did PrismNLI win the decision-model class? Is this JevBench / DMB? Treat remote 349 ms as local 31 ms?

No, no, and no. frozen-protocol zero-shot bench. TypeSafe Jev vs PrismNLI vs Laya. contamination caveat. Jev 0.587 Brier 0.667 ECE 0.281 p50 349 ms remote $0.0284; PrismNLI 0.725 Brier 0.441 ECE 0.174 p50 58 ms local; Laya 0.587 Brier 0.707 ECE 0.307 p50 31 ms; Jev≈Laya McNemar p=1.000 *theirs*. All three overconfident. PrismNLI init from deberta-v3-large-zeroshot-v2.0 trained on emotion train/val. Python; license **null**; **0★**; HEAD `b61e6cfc`; README SHA `b7256888`. elcronos/jev-vs-open-decision-models ≠ JevBench ≠ DMB. `notes.md` §101.

## Is jevusher jev-sift / winnow? Treat J7 pass as safe to obey? Paste 261/118 as Harbor?

No, no, and no. context-window admission control. VOI gate which tokens are worth the expensive model. fail polarity per lens. on small inputs lenses lose money (offered 261 / sent 118 / jev read 6,866 to keep out 143 *theirs*). J7 pass = nothing detected, never safe to obey. TypeScript MIT; **0★**; HEAD `d830d344`; README SHA `428a4a59`; package 0.1.0. cvsgireesh/jevusher ≠ jev-sift ≠ winnow. `notes.md` §101.

## Does a jev-fabric receipt authorize an effect? Is historical-v0 ECE usable? Is it jev-forge or DGP?

No, no, and no. typed decision control plane. receipt ≠ authorization. historical-v0 zero retained cases (old ECE invalid: used TypeSafe confidence not max p). Tool-env **NOT_RUN**. Alpha 0.1.0-alpha.1. TypeScript Apache-2.0; **0★**; HEAD `95b9a4f3`; README SHA `f485dbdd`. MokiMeow/jev-fabric ≠ jev-forge ≠ dgp. `notes.md` §101.

## Is live-rubric TypeSafe hosted? Is the price $0.000004 or $0.000006? Copy CODIV_API_KEY into the browser?

No, no, and no. live 15-dim typed rubric re-score per pause. scoring economics exemplar. OpenJev/Codiv ≠ TypeSafe hosted. jose-troche/live-rubric ~$0.000004 desc / ~$0.000006 README (quote **both**). Key never in the browser. TypeScript; license **null**; **0★**; HEAD `db8da8db`; README SHA `4a0be084`. `notes.md` §101.

## Is jev-evaluation jevals? Hard-gate confidence ≥0.95? Does Augustus own the injection fold?

No, no, and no. adversarial pre-registered Jev eval. 28 predictions before data. 123,805 requests. confidence does not track ignorance (≥0.95 still admits 47% unanswerable *theirs*). polite injection 65% / crude 0%. 12/25 testable held; 13 wrong. ECE 0.075 on support-ticket; fails on 3-SAT. Python MIT; **0★**; HEAD `c168c093`; README SHA `2d66ac22`. willkelly/jev-evaluation ≠ jevals ≠ jev-baselines-eval. rh-guard owns injection/steer; Augustus owns pre-registration/calibration science. `notes.md` §101.

## Is system_one_sdk typesafe_sdk? Is it dannote/jev? Is it TypeSafe official?

No, no, and no. provider-neutral Elixir/BEAM Noul/Choice/Score SDK. class infrastructure. GitHub desc provider-neutral; README opening TypeSafe-first. First provider via `typesafe_api_sdk` path dep. mix **0.5.0**. Elixir MIT; **0★**; HEAD `c2a522ee`; README SHA `c117b4c4`; GitHub size **0** with contents. nshkrdotcom/system_one_sdk ≠ typesafe_sdk (**3★**) ≠ dannote/jev (**16★**). `notes.md` §101.

## Did Archer land this hour? Treat Qwen3.8-27B as Archer? Invent tweets?

No, no, and no. Hub `archerhume/4rcherhume` HTTP **401**. Tracker likes **54** (+3 vs §100 pin **51**); lastModified **CHANGED** `2026-09-20T02:59:13Z` (was §100 `2026-09-19T18:37:18Z`). Not re-fetched as a rewrite. Live REST pulse: SemIf **1984★** (+30 vs §100 **1954**); jevlike **1002★** (+13 vs §100 **989**); TypeAR-AI/TypeAR **11★** flat. AnotiaWang/awesome-jev **84★** ≠ Awesomejev 561/27007. `invented_signal: false`. `notes.md` §101.

Unique fragments (consecutive): question-linting of Jev questions themselves; nine jaggedness rules, no API key, no labelled data; static lint ≠ measured separation; yodablocks/jevq ≠ tenbin ≠ JevLint ≠ commitjev; open-weights Laya as class exemplar (binding); Nx/Bumblebee runtime; host chooses backend; ChristianAlexander/laya_ex ≠ system_one_sdk ≠ dannote/jev ≠ NandhaKishorM/laya; on-chain/edge Laya deploy; parity_verified stays false; model output never grants Tx; humandebri/IC-Laya ≠ laya_ex; auditable weekend replica; Jev outputs never used for training; soft human-vote distributions; unpaired 0.577 vs 0.727; agilabs-ai/jev48 ≠ JevBench ≠ Mapika/decider; adversarial dual-judge / framing attack surface; comparative framing is the usable judgment; prior injection crowds out evidence; copyleftdev/ember ≠ ember.js; Laya specialist fine-tune pipeline; training still GPU-pending; PIXELZX0/XERON ≠ convaiinnovations/laya; Hub Laya replica drop; daliborsb/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya; System One student distillation corpus; gold is programmatic; teacher is closed-API clone; do not distill Jev as teacher of record; MagaBitmex/jev-4b-distill-data ≠ missing student checkpoint; non-LLM VIN System One; planning depth not chat; lewislululu/jevon ≠ douglance/jevon; source-bound evidence checks; local quote mismatch needs no API; exit 0 ≠ claim truth; WaynezProg/jev-kit ≠ jonathanavis96/jev-kit (Airlock) ≠ jev-use ≠ jev-mcp

## Is jevq tenbin or JevLint? Treat a clean run as measured separation? Fail CI on a warn?

No, no, and no. question-linting of Jev questions themselves. nine jaggedness rules, no API key, no labelled data. static lint ≠ measured separation. Motivating receipt: commitjev "without" scored 0.75 on real deletions and **0.81 on commits that deleted nothing** *theirs*. Exit 0 clean / 1 warn / 2 run-failed. Python MIT; **0★**; HEAD `40b2dd90`; README SHA `3198dde0`; GitHub size **0** with contents. yodablocks/jevq ≠ tenbin ≠ huntedman/JevLint ≠ commitjev. Soft Noul ≠ hard safety. `notes.md` §102.

## Is laya_ex system_one_sdk? Is it TypeSafe official? Copy mix backends as recipes?

No, no, and no. open-weights Laya as class exemplar (binding). Nx/Bumblebee runtime. host chooses backend. Downloads convaiinnovations/laya. mix `:laya` **0.1.0**; elixir `~> 1.17`. Elixir Apache-2.0; **0★**; HEAD `99f9ce73`; README SHA `6361c920`; GitHub size **0** with contents. ChristianAlexander/laya_ex ≠ system_one_sdk ≠ dannote/jev ≠ NandhaKishorM/laya. `notes.md` §102.

## Do 62 IC-Laya tests prove Laya parity? Can a Score grant Tx? Is parity_verified true?

No, no, and no. on-chain/edge Laya deploy. parity_verified stays false. model output never grants Tx. `cargo test --workspace` **62 PASS**; Candle Wasm **4.8 MiB**; Python **45 PASS**; `LiveDisabled`. Fixture MASK 50283 is upstream PAD; real MASK 50284 *theirs*. Rust MIT; **0★**; HEAD `055ef42f`; README SHA `85431606`; GitHub size **0** with contents. humandebri/IC-Laya ≠ laya_ex. Soft Noul ≠ hard safety. `notes.md` §102.

## Did jev48 beat Jev on phishing? Is unpaired 0.577 identity? Were Jev outputs used for training?

No, no, and no. auditable weekend replica. Jev outputs never used for training. unpaired 0.577 vs 0.727 (teacher-agreement gold, not real-world correctness). Phish AUROC **0.769** vs 0.689 but 0.5-threshold acc **50.1%** vs **62.6%** *theirs*. JevBench 69.7 vs 86.6; CLASH **0.0** vs 98.6. Python MIT; **0★**; HEAD `aa697005`; README SHA `3f667dd4`; size **1439**. agilabs-ai/jev48 ≠ JevBench ≠ Mapika/decider. `notes.md` §102.

## Is ember ember.js? Is v4 a pharmacy controller? Should we inject class priors as help?

No, no, and no. adversarial dual-judge / framing attack surface. comparative framing is the usable judgment. prior injection crowds out evidence (paired worse; correlation with the prior **+0.815**). first-look **+0.199**; **0 of 2,816** crossed 0.5 on v1; v4 **+26,744** doses *theirs* on 120 nodes. SCALING.md red **7/24→1/24→0/24** at locked HEAD `c02f622b` (SPECTRAL 11/40 is later). TypeScript MIT; **0★**; HEAD `c02f622b`; README SHA `6db00b56`; size **479**. copyleftdev/ember ≠ ember.js. Do not copy attacks. `notes.md` §102.

## Are XERON sequence counts trained quality? Did training finish? Never hallucinates?

No, no, and no. Laya specialist fine-tune pipeline. training still GPU-pending. ALL-v2 **131,967** sequences *theirs*. Python; license **null** (README Apache-2.0); **0★**; HEAD `5e870a4d`; README SHA `8733e01f`; size **52**. PIXELZX0/XERON ≠ convaiinnovations/laya. `notes.md` §102.

## Is daliborsb/laya a new species? Re-paste the copied vs-Jev table as a 2145 bake-off?

No and no. Hub Laya replica drop. layout matches convaiinnovations/laya (encoder/multilingual/typed-decisions; 842.6MB safetensors). Copied 0.766 / post-T ECE 0.081 remain §76 receipts. HF Apache-2.0; 421.3M. daliborsb/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya. `notes.md` §102.

## Distill Jev as teacher of record? Is MagaBitmex/jev-4b-distill shipped? Is gold a teacher label?

No, no, and no. System One student distillation corpus. gold is programmatic. teacher is closed-API clone. Hub model MagaBitmex/jev-4b-distill **not found** this pass. 1.5k train / 100 eval / 120 hard; ~$0.03/1k *theirs*. MagaBitmex/jev-4b-distill-data ≠ missing student checkpoint. Contrast jev48: Jev outputs never used for training. `notes.md` §102.

## Is jevon douglance/jevon? Is maze 1.00 a general System One? Is Qwen3.8-27B Archer here?

No, no, and no. non-LLM VIN System One. planning depth not chat. 20,105,047 params; maze/choice **1.0000** n=141; snake **0.9674** n=92 *theirs*; research artefact. HF AGPL; likes **3**. lewislululu/jevon ≠ douglance/jevon ≠ NanoJev. Qwen3.8-27B ≠ Archer. `notes.md` §102.

## Is jev-kit exit 0 claim truth? Is "multi" extra repos? Copy curl|sh as a skill?

No, no, and no. source-bound evidence checks. local quote mismatch needs no API. exit 0 ≠ claim truth (3 review / 2 invalid). "multi" = nine-host installer, not extra GitHub repos. TypeScript + Python MIT; **0★**; HEAD `4558554f`; README SHA `a7f14838`; GitHub size **0** with contents. WaynezProg/jev-kit ≠ jonathanavis96/jev-kit (Airlock) ≠ jev-use ≠ jev-mcp. `notes.md` §102.

## Did Archer land this hour? Treat Qwen3.8-27B as Archer? Invent tweets?

No, no, and no. Hub `archerhume/4rcherhume` HTTP **401** (last pin §101; not re-fetched as a rewrite). Tracker likes **54**; lastModified `2026-09-20T02:59:13Z`. Live REST pulse (review relock): SemIf **2000★** (+16 vs §101 **1984**); jevlike **1002★** **flat**; TypeAR-AI/TypeAR **12★** (+1 vs §101 **11**). AnotiaWang/awesome-jev **86★** (+2 vs §101 **84**) ≠ Awesomejev 561/27007. `invented_signal: false`. `notes.md` §102.

independent System One evidence catalog; 19 reviewed records; scores not one leaderboard; no external record currently reproduced; TokenTrim no-Jev matched hybrid 62.4%; reachjalil/system-one-bench ≠ mallahyari/system-one-benchmark; 21 tasks · 134 items · 208 questions; scenes from public GitHub contracts, not production logs; SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv/jev-eval ≠ xxkuboxx/jev-eval ≠ onlyoneaman/jev-eval ≠ dayhaysoos/jevals; option isolation (sibling-blind); permutation-equivariant; Hub OWNER not published; nafisazizir/hev ≠ jaredpalmer/kev; frozen local LLM logits, no trained decision head; residual-head 9,222-param decreased 73/96→67/96; confidence = 1−normalized entropy, not P(correct); yuki-oshio/mini-jev ≠ r-ms/mini-jev; Jev classifier as autoregressive next-token predictor; ChatJev-style soundness theater; erik-dunteman/ChatJev ≠ dannote/jev ≠ jev-gpt; calibrated decision head × AlphaProof value head; implementation-layer isomorphism, semantic difference; timeout = censoring; do not launder Noul as proof; parallel rank-prediction vs serial selection; independent questions can conflict; zzzzzec/jevsort ≠ keltokhy/jsort; curated open System One ecosystem catalog; rupeshpoojary9/awesome-open-system-one ≠ AnotiaWang/awesome-jev; arXiv paper radar with Jev relevance scoring; ranking ≠ calibration / 0.5 still soft; fail-open failed evals not marked seen

## Is system-one-bench mallahyari/system-one-benchmark? Treat 19 records as one leaderboard? Promote reported to reproduced?

No, no, and no. independent System One evidence catalog. 19 reviewed records. scores not one leaderboard. no external record currently reproduced. TokenTrim no-Jev matched hybrid 62.4% vs best fixed 60.3% (cached answers). `npm test` checks catalog without model calls. JavaScript MIT; **0★**; HEAD `ceb17269`; README SHA `d9e0c7b7`; GitHub size **90**. reachjalil/system-one-bench ≠ mallahyari/system-one-benchmark. Soft Noul ≠ hard safety. `notes.md` §103.

## Is SivletLabs/jev-eval willkelly or 4esv? Are the scenes production logs? Is this Harbor?

No, no, and no. 21 tasks · 134 items · 208 questions. scenes from public GitHub contracts, not production logs. choice/noul accuracy/Brier/NLL; score exact-level/MAE/Brier/NLL. HTTP `POST /api/evaluate`. Python MIT; **0★**; HEAD `3f9d976f`; README SHA `df16766c`; GitHub size **0** with contents. SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv/jev-eval ≠ xxkuboxx/jev-eval ≠ onlyoneaman/jev-eval ≠ dayhaysoos/jevals. `notes.md` §103.

## Is hev kev? Paste 80.00% as Jev identity? Is Hub OWNER published?

No, no, and no. option isolation (sibling-blind). permutation-equivariant. Hub OWNER not published; weights not in git. Dev-split PointerHead 80.00% / transfer 60.71% / ECE 0.020 *theirs*; 0/696 flips (protocols differ from kev/Jev). Development-only. Python Apache-2.0; **0★**; HEAD `79a486f9`; README SHA `b995dce3`; GitHub size **2318**. nafisazizir/hev ≠ jaredpalmer/kev. `notes.md` §103.

## Is yuki-oshio/mini-jev r-ms/mini-jev? Is 93.25% family-disjoint? Is confidence P(correct)? Did the residual head help?

No, no, no, and no. frozen local LLM logits, no trained decision head. residual-head 9,222-param decreased 73/96→67/96. confidence = 1−normalized entropy, not P(correct). Self-authored 2,400 JP suite 93.25% *theirs*. Python MIT; **0★**; HEAD `dff5b323`; README SHA `363441b6`; GitHub size **38370** with contents. yuki-oshio/mini-jev ≠ r-ms/mini-jev. `notes.md` §103.

## Is ChatJev jev-gpt? Is it dannote/jev? Treat "kinda works" as a product?

No, no, and no. Jev classifier as autoregressive next-token predictor. ChatJev-style soundness theater. pyproject name `"jev"` v0.1.0 collides with dannote/jev. Contrast jev-gpt: generation as a tree of Choices, never free-generates. Python; license **null**; **1★**; HEAD `ea33ab8d`; README SHA `c763be19`; `main.py` 6171 bytes — do not dump. erik-dunteman/ChatJev ≠ dannote/jev ≠ jev-gpt. `notes.md` §103.

## Does a softmax-head isomorphism make Jev a proof? Treat timeout-dropped samples as a full distribution? Launder a Noul as Lean?

No, no, and no. calibrated decision head × AlphaProof value head. implementation-layer isomorphism, semantic difference. timeout = censoring. do not launder Noul as proof. Proposals labeled (S). Markdown; license **null**; **0★**; HEAD `afd9bb6f`; README SHA `1810d7f6`; overview SHA `919b922a`. `notes.md` §103.

## Is jevsort jsort? Are parallel rank questions a sort proof?

No and no. parallel rank-prediction vs serial selection. independent questions can conflict. Integers −1e6..1e6. HTML; license **null**; **1★**; HEAD `57067b90`; README SHA `85044740`; GitHub size **70**. zzzzzec/jevsort ≠ keltokhy/jsort. `notes.md` §103.

## Is awesome-open-system-one AnotiaWang/awesome-jev? Paste von sub-15ms as an Augustus fact?

No and no. curated open System One ecosystem catalog (open models/evals/calibration/constrained-decoding), not closed-Jev apps. CC0 1.0 LICENSE SHA `36848c0b`; GitHub SPDX NOASSERTION; **0★**; HEAD `637ee3d3`; README SHA `0007e343`; GitHub size **4** with contents. rupeshpoojary9/awesome-open-system-one ≠ AnotiaWang/awesome-jev. Do not paste listed 4esv/jev-eval or von sub-15ms as Augustus receipts. `notes.md` §103.

## Is paper-radar 0.5 a frequency? Mark failed evals seen? Copy .env?

No, no, and no. arXiv paper radar with Jev relevance scoring. ranking ≠ calibration / 0.5 still soft (high_priority 0.8). fail-open failed evals not marked seen. Tests use doubles. Python MIT; **0★**; HEAD `fbadf01c`; README SHA `1cb8a9c3`; size **73**; default **master**. Do not copy `uv` / keys. `notes.md` §103.

## Did Archer land this hour? Treat Qwen3.8-27B as Archer? Invent tweets?

No, no, and no. Hub `archerhume/4rcherhume` HTTP **401** (last pin §101; not re-fetched as a rewrite). Tracker likes **54**; lastModified `2026-09-20T02:59:13Z`. Live REST pulse (review relock): SemIf **2019★** (+19 vs §102 **2000**); jevlike **1006★** (+4 vs §102 **1002**); TypeAR-AI/TypeAR **12★** **flat**. AnotiaWang/awesome-jev **87★** (+1 vs §102 **86**) ≠ Awesomejev 561/27007. `invented_signal: false`. `notes.md` §103.

train calibrated ~27M from scratch; typed Q→prob dist / one forward pass / no LLM decode; hyusi2003/MiniSystemOne ≠ Colvin0315/MiniSystemOne; description-only stub / size 5; ESCI hard probe fails four of six; jev_bool ECE 0.242 inversion 0.255; do not re-fold §60 six-gates as new; jobbyjev one-request-per-company from batch-size result; find/design/evaluate TypeSafe Jev decision loops; karanb192/jev-architect ≠ samtay32/jev-system-architect; Jairik/jev-distiller size 1; distill-Jev UI stub / do not distill Jev as teacher of record; post-launch scored use-case map / Jev self-scores then human curation; licensedsaucer9-web/jev-opportunities; Jev-inize a use case into classifier/router; gavinHuang/jevinize → simple-jev not TypeSafe; featherless-ai/simple-jev; compare saved decisions / same label can still change the branch; VihaanAgarwal/jev-diff ≠ Saik0s/diffusiongemma-jev-macos; not tested with a live Jev API key; constrained logprob + temp/Platt ≠ Noul; OpenJevPro pastes openjev-sglang JevBench as own; zhangcy122/OpenJevPro ≠ IamBusy/OpenJev ≠ ekzhang/openjev-sglang; PolyForm Noncommercial; SmolLM-135M / sub-70ms / 0 output tokens; demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055; README claims MIT / GitHub license null / no LICENSE file; patelvishwa112/jev-system-one-rlcd ≠ arnabgho/rlcd-lite ≠ blackwood-rlcd; source-backed Awesome Jev radar / 306+ commit-pinned; logicrw/awesome-jev-projects ≠ AnotiaWang/awesome-jev ≠ yibie/awesome-jev ≠ cobanov/awesome-jev ≠ rupeshpoojary9/awesome-open-system-one; auto GitHub sync / Issue-only submissions; hashed n-gram encoder / rival-aware attention; olanotolu/jevbetter vs jevlike starter; synthetic hard menus top-1 0.916 vs 0.873 / ECE 0.0182 vs 0.0367 / 40 vs 4608 menus/sec; shuffled-context control 0.335

## Is hyusi MiniSystemOne a trained checkpoint? Paste Colvin 26.89M as hyusi? Is it mini-jev or kev?

No, no, and no. train calibrated ~27M from scratch. typed Q→prob dist / one forward pass / no LLM decode. hyusi2003/MiniSystemOne ≠ Colvin0315/MiniSystemOne. description-only stub / size 5. Apache-2.0; **0★**; HEAD `4385335b`; README SHA `83016bf8`. Namesake Colvin holds the recipe; do not paste Colvin numbers as hyusi. ≠ mini-jev (frozen logits) ≠ kev (LoRA pointer). `notes.md` §104.

## Did ESCI pass the six gates? Re-fold §60 as new? Treat 20NG as graded-IR safety?

No, no, and no. ESCI hard probe fails four of six. jev_bool ECE 0.242 inversion 0.255. do not re-fold §60 six-gates as new. jobbyjev one-request-per-company from batch-size result. Python MIT; **0★**; HEAD `52397954`; README SHA `7bd075c3`; size **309**. Calibration ≠ sortable is now an empirical fail on graded product relevance. `notes.md` §104.

## Is jev-architect a second Augustus? Is it samtay32/jev-system-architect? Copy npx skills add?

No, no, and no. find/design/evaluate TypeSafe Jev decision loops. karanb192/jev-architect ≠ samtay32/jev-system-architect. HTML MIT; **0★**; HEAD `35ea6d93`; README SHA `68c2b5f9`; size **5199**. Workflow inspection before the API. Do not copy `npx skills add`. `notes.md` §104.

## Distill Jev as teacher of record? Is Jairik/jev-distiller a student checkpoint?

No and no. Jairik/jev-distiller size 1. distill-Jev UI stub / do not distill Jev as teacher of record. MIT; **0★**; HEAD `0589d44c`; README SHA `aa408c5e`. Thin HIGH still gets a real card. `notes.md` §104.

## Are Jev self-scores a product roadmap? Is jev-opportunities licensed?

No and no (license **null**). post-launch scored use-case map / Jev self-scores then human curation. licensedsaucer9-web/jev-opportunities. **0★**; HEAD `a47fa414`; README SHA `aa33f901`; size **27**. Human TOP curation is the exact work. `notes.md` §104.

## Is jevinize TypeSafe hosted? Copy Featherless demo keys?

No and no. Jev-inize a use case into classifier/router. gavinHuang/jevinize → simple-jev not TypeSafe. featherless-ai/simple-jev. MIT; **0★**; HEAD `6d080632`; README SHA `5f48e622`; size **6**. Scaffolding ≠ Augustus design judgment. `notes.md` §104.

## Is a fixture exit 1 a class regression? Is jev-diff diffusiongemma? Tested with a live Jev API key?

No, no, and no. compare saved decisions / same label can still change the branch. VihaanAgarwal/jev-diff ≠ Saik0s/diffusiongemma-jev-macos. not tested with a live Jev API key. Python MIT; **0★**; HEAD `a3c98807`; README SHA `3b0ce75c`; size **120**. 0.81→0.79 at a 0.8 gate still changes the branch. `notes.md` §104.

## Is constrained logprob a Noul? Did OpenJevPro measure 95.5%? Is it IamBusy/OpenJev?

No, no, and no. constrained logprob + temp/Platt ≠ Noul. OpenJevPro pastes openjev-sglang JevBench as own. zhangcy122/OpenJevPro ≠ IamBusy/OpenJev ≠ ekzhang/openjev-sglang. PolyForm Noncommercial. HTML; SPDX NOASSERTION; **0★**; HEAD `94d77bcb`; README SHA `50c77ace`; size **64**. `notes.md` §104.

## Quote SmolLM 67 ms / 2.1% ECE as Jev identity? Is the demo calibrated? Is it MIT on GitHub?

No, no, and no. SmolLM-135M / sub-70ms / 0 output tokens. demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055. README claims MIT / GitHub license null / no LICENSE file. patelvishwa112/jev-system-one-rlcd ≠ arnabgho/rlcd-lite ≠ blackwood-rlcd. Python; **0★**; HEAD `62b103b3`; README SHA `55994d69`; GitHub size **1513** (relock; was **0** with contents). `notes.md` §104.

## Is awesome-jev-projects AnotiaWang or yibie? Paste listed von/cua numbers? Is 306+ a bake-off?

No, no, and no. source-backed Awesome Jev radar / 306+ commit-pinned. logicrw/awesome-jev-projects ≠ AnotiaWang/awesome-jev ≠ yibie/awesome-jev ≠ cobanov/awesome-jev ≠ rupeshpoojary9/awesome-open-system-one. auto GitHub sync / Issue-only submissions. JavaScript MIT; **136★**; HEAD `97057cc1`; README SHA `25a19b31`; size **7677** (relock; was **7136**). `notes.md` §104.

## Quote jevbetter 0.916 as a class ceiling? Is rival-aware the same as hev isolation?

No and no (opposite of option isolation). hashed n-gram encoder / rival-aware attention. olanotolu/jevbetter vs jevlike starter. synthetic hard menus top-1 0.916 vs 0.873 / ECE 0.0182 vs 0.0367 / 40 vs 4608 menus/sec. shuffled-context control 0.335. Python MIT; **12★**; HEAD `bb0ebc82`; README SHA `5cbe01d4`; size **324**. `notes.md` §104.

## Did Archer land this hour? Treat Qwen3.8-27B as Archer? Invent tweets?

No, no, and no. Hub `archerhume/4rcherhume` HTTP **401** (not re-fetched as a rewrite). Tracker `multimodalart/jev-reproductions-tracker` likes **56**; lastModified `2026-09-20T04:29:16.000Z`. `Tonic/4rcher-tracker` HTTP **401**. Live REST pulse: SemIf **2047★** (+28 vs §103 **2019**); jevlike **1018★** (+12 vs §103 **1006**); TypeAR-AI/TypeAR **12★** **flat**. AnotiaWang/awesome-jev **91★** (+4 vs §103 **87**) ≠ Awesomejev 561/27007 ≠ logicrw/awesome-jev-projects **136★**. Qwen/Qwen3.8-27B HTTP **200** likes **15787** lastModified `2026-08-14T15:00:01.000Z` — ≠ Archer. `invented_signal: false`. `notes.md` §104.

structured probability readouts; distribution > argmax; Noul 0.5 midpoint; score is expectation not integer; bare HTTP not SDK; Arohtea/jev-readout; Jev-style Choice/Score/Noul from ordinary models; optional DSH plugin; schema-valid ≠ calibrated; gulagala001/jevify ≠ Mintzs/jevify; Laya RLCD benchmark; 40.3% below constant-answer; open-weight measurement; mourad-ghafiri/laya-rlcd-benchmark ≠ yibie/laya-jev-lab; cheap fail-open semantic edge; second signal not sole; FastLoopError catch; SupremeDreamZ/jev-fastloop ≠ jev-ultrafast; asking more questions in one call; 0.980 at every N; nearly not fully deterministic; TheWebDevel/jev-fanout; Qwen3-VL perception + Jev decisions train RL; 0 model calls at deployment; VLM alone 1.7 vs +Jev 4.4; harneet2512/reflexrl ≠ khordoo/jev-reflex-autonomy-lab; independent Jev API vs Laya; cascade 0.60 matches 78% at 1.8×; noul facts not judgements; yibie/laya-jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab; GLiNER vs GLiFormer vs Laya vs Jev; extractors ≠ decision engines; Laya dict-instructions collapse 58.3%; umstek/zero-shot-ie-bench; decisions-per-minute & cost; 204 moves vs 73; throughput not intelligence; angelgalvisc/snake-arena-jev-vs-llms ≠ vtrivedy/jev-plays-games; behavioral contracts; pin expectations eval upgrades; raw 0.94 is not a release; sathariels/jevcheck ≠ dayhaysoos/jevals ≠ SivletLabs/jev-eval; evidence-linked dependency upgrade; Jev never generates filenames; no_direct_evidence ≠ safe to merge; GaneshVG18/upgrade-radar ≠ LYchoon/paper-radar-jev; discography theme/mood/complexity; five atomic questions one call; lirantal/discoprint

## Is jev-readout an SDK tutorial? Treat displayed p as proof? Round Score to an integer?

No, no, and no. structured probability readouts. distribution > argmax. Noul 0.5 midpoint. score is expectation not integer. bare HTTP not SDK. CORS so the key stays server-side. JavaScript; license **null** (README MIT); **0★**; HEAD `6f1e5900`; README SHA `67ee1e96`; GitHub size **44** (relock; was **0** with contents). Arohtea/jev-readout. Soft Noul ≠ hard safety. `notes.md` §105.

## Is gulagala001/jevify Mintzs/jevify? Is schema-valid JSON a calibrated Noul? Are questions independent parallel?

No, no, and no. Jev-style Choice/Score/Noul from ordinary models. optional DSH plugin. schema-valid ≠ calibrated. Questions merged into one ordinary-model call. Confidence from the TypeSafe ordinary-model adapter, not P(correct), not bit-identical to Jev. JavaScript MIT; **0★**; HEAD `3d3e904a`; README SHA `0e2f8536`; LICENSE SHA `66869720`; GitHub size **145** (relock; was **0** with contents). gulagala001/jevify ≠ Mintzs/jevify. `notes.md` §105.

## Is 40.3% a class ceiling? Collapse mourad into yibie/laya-jev-lab? Skip the constant-answer baseline?

No, no, and no. Laya RLCD benchmark. 40.3% below constant-answer (12.8 points below a constant answer that reads no text). open-weight measurement. Routing/choice +10; booleans −26; ordinals −15. README title `laya-decision-bench`. Python; license **null**; **0★**; HEAD `3401ff26`; README SHA `d8d4859e`; GitHub size **164** (relock; was **0** with contents). mourad-ghafiri/laya-rlcd-benchmark ≠ yibie/laya-jev-lab ≠ pngwn/open-jev-laya-bench. `notes.md` §105.

## Is jev-fastloop jev-ultrafast? Hard-gate fused confidence as safety? Is Jev the only signal?

No, no, and no. cheap fail-open semantic edge. second signal not sole. FastLoopError catch (do the expensive thing). 4/5, 8/8, 2.00→0.18 fused *theirs* on jev-1.13-free $0. Python MIT; **0★**; HEAD `1157841a`; README SHA `053a0885`; GitHub size **12** (relock; was **0** with contents). SupremeDreamZ/jev-fastloop ≠ jev-ultrafast. `notes.md` §105.

## Does asking more questions in one call change answers? Is 0.0000 sd universal determinism? Extrapolate to Score?

Question count did not move the refund probe (0.980 at every N); no, and no. asking more questions in one call. nearly not fully deterministic (22 of 24 identical across 40 calls; two moved at conf 0.107/0.312). Two documents, one afternoon; Score untested. Python MIT; **0★**; HEAD `b30aaadc`; README SHA `394b2e1e`; GitHub size **206** (relock; was **0** with contents). TheWebDevel/jev-fanout. `notes.md` §105.

## Is reflexrl khordoo? Ship VLM+Jev as the runtime? Quote 2.95× as Harbor?

No, no, and no. Qwen3-VL perception + Jev decisions train RL. 0 model calls at deployment. VLM alone 1.7 vs +Jev 4.4. Pixels-only 0.75M policy; teacher influence anneals. Python MIT; **0★**; HEAD `aa36be84`; README SHA `e6ff13cd`; GitHub size **749** (relock; was **0** with contents); default **master**. harneet2512/reflexrl ≠ khordoo/jev-reflex-autonomy-lab. `notes.md` §105.

## Is yibie/laya-jev-lab dairui1 or BrendanH18? Hard-gate cascade 0.60? Cite “choice is order-biased”?

No, no, and no. independent Jev API vs Laya. cascade 0.60 matches 78% at 1.8× (45% local). noul facts not judgements. Retracted: “choice order-biased” (n=4) and “Laya confidence trustworthy above 0.7”. Confidence-to-accuracy not monotonic past 0.70. Python MIT; **0★**; HEAD `30ba64dc`; README SHA `57bd1832`; GitHub size **49** (relock; was **0** with contents). yibie/laya-jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab. `notes.md` §105.

## Are GLiNER/GLiFormer decision engines? Quote 100% sentiment as a class win? Collapse locate into decide?

No, no, and no. GLiNER vs GLiFormer vs Laya vs Jev. extractors ≠ decision engines. Laya dict-instructions collapse 58.3% (strings 95.8%). Easy sentiment set. NER F1 GLiFormer-base 1.00 *theirs*. Python MIT; **0★**; HEAD `8770b16b`; README SHA `d69dc96a`; size **50** (relock; was **33**). umstek/zero-shot-ie-bench. `notes.md` §105.

## Is 21 snake points intelligence? Collapse into jev-plays-games? Ignore 36% of moves <0.90?

No, no, and no. decisions-per-minute & cost. 204 moves vs 73. throughput not intelligence. One seed, one run. 45 output tokens sd 0.00. Python MIT; **0★**; HEAD `985a1c70`; README SHA `0db6f528`; size **194**. angelgalvisc/snake-arena-jev-vs-llms ≠ vtrivedy/jev-plays-games ≠ lewislululu/jevon. `notes.md` §105.

## Is jevcheck jevals or SivletLabs/jev-eval? Is raw 0.94 a release? Is `jev-1.14` a verified live ID?

No, no, and no. behavioral contracts. pin expectations eval upgrades. raw 0.94 is not a release. `jev-1.13`/`jev-1.14` are unverified example pin labels; documented pin `jev-1.13.0`. Gate helper optional, not the product. Python MIT; **0★**; HEAD `fc49c795`; README SHA `5c832f81`; size **117**. sathariels/jevcheck ≠ dayhaysoos/jevals ≠ SivletLabs/jev-eval. `notes.md` §105.

## Is `no_direct_evidence` safe to merge? Does Jev generate filenames? Is the screenshot live Jev? Collapse into paper-radar?

No, no, no, and no. evidence-linked dependency upgrade. Jev never generates filenames. no_direct_evidence ≠ safe to merge. ILLUSTRATIVE FIXTURE is not live Jev. Exit 0 advisory. TypeScript MIT; **0★**; HEAD `e438f9bd`; README SHA `c32f7d18`; GitHub size **908** (relock; was **0** with contents). GaneshVG18/upgrade-radar ≠ LYchoon/paper-radar-jev. `notes.md` §105.

## Is theme Choice a music-theory certificate? Copy npx/.env as a skill?

No and no. discography theme/mood/complexity. five atomic questions one call. Code owns MusicBrainz/lrclib; Jev scores lyrics. TypeScript Apache-2.0; **0★**; HEAD `a9d3294f`; README SHA `9a64f473`; GitHub size **239** (relock; was **0** with contents). lirantal/discoprint. Do not copy `npx` / keys. `notes.md` §105.

## Did Archer land this hour? Treat Qwen3.8-27B as Archer? Invent tweets?

No, no, and no. Hub `archerhume/4rcherhume` HTTP **401**. Tracker likes **59** (+3 vs §104 **56**); lastModified `2026-09-20T04:29:16Z` **UNCHANGED** vs §104. Laya Hub HTTP **200** likes **705**. Blackwood Hub HTTP **200** likes **2** gated manual — user census **absent** from the tracker; do not rewrite as landed. Live REST pulse (independent review relock after `0558f7d`): SemIf **2069★** (+22 vs §104 **2047**); jevlike **1022★** (+4 vs §104 **1018**); TypeAR-AI/TypeAR **12★** **flat**. AnotiaWang/awesome-jev **92★** (+1 vs §104 **91**) ≠ Awesomejev 561/27007 ≠ yibie/awesome-jev **450★**. Qwen3.8-27B ≠ Archer (likes **15796**). `invented_signal: false`. `notes.md` §105.

Turn any open LLM into System-One Jev; uspraveen/Jevify ≠ Mintzs/jevify ≠ gulagala001/jevify; Jevify-any-LLM architecture probe; description-only stub / size 0; Train encoder-only calibrated decision models from a task sentence; Exu is a toolkit, not a method; strictly proper scoring rule; Pre-alpha; Ruivalim/exu-base; scratch-trained calibrated decision model; typed Q → probability dists; Colvin0315/MiniSystemOne ≠ hyusi2003/MiniSystemOne; no published weights download URL; 90.5 seconds / 29.2% pipeline evidence; p_i/p_j independent of other candidates; Recipe for calibrated decision models — small model out; init → synth → train → eval → serve; 91.1 % / ECE 0.022 *theirs*; Jev zero-shot 75.1; scienthoon/luce; Put Jev's three headline claims on trial; 0.5B local GPU; 46x speedup / accuracy identical; ECE 0.624 sentiment catastrophe; bigger model worse calibration; RichardoMrMu/jev-mini ≠ yuki-oshio/mini-jev ≠ r-ms/mini-jev; System-1 decision engine for local LLMs; structured choices only; JSON parse of generated text ≠ Noul; TypefAI JEV / Journal Entry Voucher; tapsin/jev-local ≠ us/jev-local ≠ Argos1111/jev_local; Jev 1.13 reward-model eval across 8 benchmark tracks; 40,940 examples / 0 API errors; RewardBench v1 92.58%; Precise IF 50.63%; goya4140/jev-reward-model-evaluation; Scaffolding in progress; Jev vs LLM support-ticket routing; static + live decision bench; TypeSafe's own published benchmark; illustrative simulations, not live API calls; JevBench v1 — smart/cheap/fast/reliable; I/C/S/K 25% geometric mean; classifier.dev fast tier 84.8 is Jev behind its own API; do not re-fold §78 v1.2 board as new; Laya (421M) 70.1 now on board; Zero-shot/few-shot LLM routing; hard budget filter before Jev; Jev never asked to perform budget arithmetic; Jev judges the next state, XState enforces transitions; simulation uses synthetic keyword fixtures; catalog gravity; v-modal/awesome-jev-tools; ★339 live REST; curation is not endorsement; crawler-maintained directory; Daily GitHub + npm sweep, human-merged; RadRebelSam/awesome-jev ≠ AnotiaWang ≠ yibie ≠ cobanov ≠ logicrw ≠ v-modal; HF peft SPLADE/BGE reranker; rdxtremity/jev-reranking ≠ carlaiau/jev-reranking; query-side encoders, not a Jev replica; ONNX System One Qwen3.5-4B scorer; source:pngwn/system-one-qwen3.5-4b-scorer; CC-BY-NC-4.0; temperature 1.75; transformers.js AutoModel cannot load this graph; Consistency benchmark Space; This Space contains no benchmark result yet; 12-case plumbing fixture; do not reopen or amend PR #23

## Is uspraveen/Jevify a checkpoint? Collapse into Mintzs or gulagala001? Amend PR #23?

No, no, and no. Turn any open LLM into System-One Jev. uspraveen/Jevify ≠ Mintzs/jevify ≠ gulagala001/jevify. Jevify-any-LLM architecture probe. description-only stub / size 0. license **null**; **0★**; HEAD `0f29d783`; README SHA `32608473`. do not reopen or amend PR #23. `notes.md` §106.

## Is Exu a method? Skip `--mode baseline`? Treat Pre-alpha ECE as a proof?

No, no, and no. Train encoder-only calibrated decision models from a task sentence. Exu is a toolkit, not a method. strictly proper scoring rule. Pre-alpha. Ruivalim/exu-base. Python MIT; **1★**; HEAD `7288cdca`; README SHA `45244838`; size **180**. `notes.md` §106.

## Paste Colvin 90.5s / 29.2% as hyusi? Are published weights a download URL? Is p_i/p_j hev isolation?

No, no, and no. scratch-trained calibrated decision model. typed Q → probability dists. Colvin0315/MiniSystemOne ≠ hyusi2003/MiniSystemOne. no published weights download URL. 90.5 seconds / 29.2% pipeline evidence. p_i/p_j independent of other candidates. Apache-2.0; **0★**; HEAD `d7f9f803`; README SHA `a5b0d2fd`; size **814**. hyusi remains description-only stub / size 5. `notes.md` §106.

## Distill Jev as luce's teacher? Quote 91.1% as a class ceiling? Is `/v1/ask` TypeSafe?

No, no, and no. Recipe for calibrated decision models — small model out. init → synth → train → eval → serve. 91.1 % / ECE 0.022 *theirs*. Jev zero-shot 75.1. Teacher is GPT-4o-mini, not Jev. scienthoon/luce. Apache-2.0; **1★**; HEAD `8072b97d`; README SHA `5fbe226d`; size **10833**. `notes.md` §106.

## Quote 46x as Jev identity? Is ECE 0.624 calibrated? Is jev-mini mini-jev?

No, no, and no. Put Jev's three headline claims on trial. 0.5B local GPU. 46x speedup / accuracy identical. ECE 0.624 sentiment catastrophe. bigger model worse calibration. n=18 tiny. RichardoMrMu/jev-mini ≠ yuki-oshio/mini-jev ≠ r-ms/mini-jev. Python MIT; **0★**; HEAD `5adef5dc`; README SHA `154ae8b0`; size **0** with contents. `notes.md` §106.

## Is JSON parse a Noul? Is JEV a Journal Entry Voucher? Collapse tapsin into us/jev-local?

No, no, and no. System-1 decision engine for local LLMs. structured choices only. JSON parse of generated text ≠ Noul. TypefAI JEV / Journal Entry Voucher. tapsin/jev-local ≠ us/jev-local ≠ Argos1111/jev_local. Python; license **null**; **0★**; HEAD `96aac2a1`; README SHA `4d728cbf`; default **master**. `notes.md` §106.

## Quote RewardBench 92.58% as a class ceiling? Is Precise IF Harbor? Is this Harbor?

No, no, and no. Jev 1.13 reward-model eval across 8 benchmark tracks. 40,940 examples / 0 API errors. RewardBench v1 92.58%. Precise IF 50.63%. goya4140/jev-reward-model-evaluation. Python MIT; **0★**; HEAD `f16a06d1`; README SHA `603587fd`. **Not Harbor**. `notes.md` §106.

## Invent ticket-router numbers? Is the README a result?

No and no. Jev vs LLM support-ticket routing. Scaffolding in progress. license **null**; **0★**; HEAD `0318ad72`; README SHA `8223dd6f`. Thin HIGH still gets a real card. `notes.md` §106.

## Paste $0.042 as an Augustus fact? Are the live pages live API calls?

No and no. static + live decision bench. TypeSafe's own published benchmark. illustrative simulations, not live API calls. HTML; license **null**; **0★**; HEAD `2d4bd6a9`; README SHA `f4e98bbf`. `notes.md` §106.

## Is classifier.dev #1 a better model? Re-fold §78 as new? Quote 84.8 as a class ceiling?

No, no, and no. JevBench v1 — smart/cheap/fast/reliable. I/C/S/K 25% geometric mean. classifier.dev fast tier 84.8 is Jev behind its own API. do not re-fold §78 v1.2 board as new. Laya (421M) 70.1 now on board. Python MIT; **6★**; HEAD `c7ab99f5`; README SHA `8fe07c41`; size **8907**. `notes.md` §106.

## Let Jev do budget arithmetic? Treat bundled costs as a ledger? Is ReflexRoute production?

No, no, and no. Zero-shot/few-shot LLM routing. hard budget filter before Jev. Jev never asked to perform budget arithmetic. AIGNLAI/ReflexRoute. Python MIT; **1★**; HEAD `5f475d80`; README SHA `6a1ae694`. Early-stage; bundled costs illustrative. `notes.md` §106.

## Is XState Jev? Are synthetic keyword fixtures live calibration? Copy .env?

No, no, and no. Jev judges the next state, XState enforces transitions. simulation uses synthetic keyword fixtures. TypeScript MIT; **0★**; HEAD `c73aef65`; README SHA `15410dbe`. Do not copy `.env`. `notes.md` §106.

## Is the empty consistency Space a win? Collapse it into jev-lab safety eval?

No and no. Consistency benchmark Space. This Space contains no benchmark result yet. 12-case plumbing fixture. apache-2.0; likes **0**. Companion to mjyoke1111/jev-lab HEAD `5c51bf93`. `notes.md` §106.

## Paste v-modal listed as a bake-off? Is ★339 eval? Is it AnotiaWang?

No, no, and no. catalog gravity. v-modal/awesome-jev-tools. ★339 live REST. curation is not endorsement. license **null**; **339★**; HEAD `f117e0c3`; README SHA `8ea9a669`. `notes.md` §106.

## Is RadRebelSam AnotiaWang or yibie or logicrw? Paste crawler stars as eval?

No and no. crawler-maintained directory. Daily GitHub + npm sweep, human-merged. RadRebelSam/awesome-jev ≠ AnotiaWang ≠ yibie ≠ cobanov ≠ logicrw ≠ v-modal. SPDX NOASSERTION; **0★**; HEAD `27629954`; README SHA `21ec8d51`; LICENSE SHA `2aa7fe23`. `notes.md` §106.

## Is rdxtremity TypeSafe Jev? Collapse into carlaiau/jev-reranking?

No and no. HF peft SPLADE/BGE reranker. rdxtremity/jev-reranking ≠ carlaiau/jev-reranking. query-side encoders, not a Jev replica. apache-2.0; likes **0**; sha `cae796ea`. `notes.md` §106.

## Is the ONNX port Apache? Does transformers.js AutoModel load it? Re-card pngwn as new?

No, no, and no. ONNX System One Qwen3.5-4B scorer. source:pngwn/system-one-qwen3.5-4b-scorer. CC-BY-NC-4.0. temperature 1.75. transformers.js AutoModel cannot load this graph. likes **0**; sha `fa0bed22`. `notes.md` §106.

## Did Archer land this hour? Treat Qwen3.8-27B as Archer? Invent tweets?

No, no, and no. Hub `archerhume/4rcherhume` HTTP **401** (not re-fetched as a rewrite). Tracker `multimodalart/jev-reproductions-tracker` likes **59**; lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED**. `Tonic/4rcher-tracker` HTTP **401**. Live REST pulse: SemIf **2074★** (+27 vs §104 **2047**); jevlike **1022★** (+4 vs §104 **1018**); TypeAR-AI/TypeAR **12★** **flat**. AnotiaWang/awesome-jev **92★** ≠ Awesomejev 561/27007 ≠ logicrw **146★** ≠ v-modal **339★**. Qwen/Qwen3.8-27B HTTP **200** likes **15796** lastModified `2026-08-14T15:00:01.000Z` — ≠ Archer. `invented_signal: false`. `notes.md` §106.

Benchmark-driven Jev router and judge; cheap alone is not success; Jev does not write, sum prices, or claim accuracy %; Sol 94.2 / Luna 83.9 / Jev path 89.7; 19.2% Sol / 62.3% cost save / 4.5pp miss of 2pp non-inferiority; p50 latency worse than Sol due to routing overhead; erendikmenn/jev-llm-router-benchmark ≠ jev-rag-benchmark ≠ ryantsai/jev-llm-router; Express + node:sqlite; mock and Jev decision engines; previous_ticket_count >= 3 is code; MIN_CONFIDENCE 0.6 still soft; substring false positives; aesaganda/jev-ticket-router ≠ SarathChandraBellam/jev-vs-llm-ticket-router; Universal Figure & Diagram Router; confidence ≥ 0.85 hard-gate is theater; generative AI banned from scientific plots; six visual branches; hoangngochuong24947-gif/jev-figure-router; human-labeled (state, question, label); 166,054 rows / 22 configs; soft_label for human uncertainty; Praveenrajus/jev-bench ≠ fstandhartinger/jevbench; ternary bonsai System One GGUF; openjev's mechanism, Bonsai's weights; Hub does not ship weights; 100/100 easy T/F is not Harbor; label_mass ≠ correctness; stock llama.cpp Q2_0 silently gibberish; NicolaiMTLassen/open-bonzi-jev ≠ NicolaiLassen; transformers.js DeBERTa ONNX; source:com-kotobalabs/open-jev-deberta-v3-large; temperature 1.05; AutoModel from_pretrained works; onnx-community/open-jev-deberta-v3-large-ONNX ≠ system-one-qwen3.5-4b-scorer-ONNX; 107★ densify; GH 151M vs README 149.6M; PR #1 now closed unmerged; do not re-fold §71 claim-audit as a beat; typed decisions, RLCD, confidence-gated routing; structured ≠ correct; mock not live API; 26 tests; wjdjdakf17/jev-study ≠ baekenough/jev-study; do not reopen or amend PR #23 or #24

## Quote 62.3% cost save without the 4.5pp miss? Did Jev write the code? Is cheap success?

No, no, and no. Benchmark-driven Jev router and judge. cheap alone is not success. Jev does not write, sum prices, or claim accuracy %. Sol 94.2 / Luna 83.9 / Jev path 89.7. 19.2% Sol / 62.3% cost save / 4.5pp miss of 2pp non-inferiority. p50 latency worse than Sol due to routing overhead. Python MIT; **0★**; HEAD `f44ef450`; README SHA `df3687e5`; size **0** with contents. erendikmenn/jev-llm-router-benchmark ≠ jev-rag-benchmark ≠ ryantsai/jev-llm-router. Do not copy `uv` / `OPENROUTER_API_KEY`. `notes.md` §107.

## Collapse aesaganda into Sarath? Invent ticket-router numbers? Hard-gate 0.6 as safety?

No, no, and no. Express + node:sqlite. mock and Jev decision engines. previous_ticket_count >= 3 is code. MIN_CONFIDENCE 0.6 still soft. substring false positives. JS; license **null**; **0★**; HEAD `ecf00046`; README SHA `41c0b50f`; size **0** with contents. aesaganda/jev-ticket-router ≠ SarathChandraBellam/jev-vs-llm-ticket-router. Mock is for `npm test`, not production. `notes.md` §107.

## Hard-gate figure confidence ≥ 0.85 as FAST_PATH? Let generative AI author scientific plots?

No and no. Universal Figure & Diagram Router. confidence ≥ 0.85 hard-gate is theater. generative AI banned from scientific plots. six visual branches. Python MIT; **1★**; HEAD `4c51b1af`; README SHA `11d5302b`; size **340**. hoangngochuong24947-gif/jev-figure-router. The ban is a CONSTRAINT in policy; Jev only routes. `notes.md` §107.

## Collapse Praveenrajus/jev-bench into fstandhartinger/jevbench? Quote unpublished jevify-run as Harbor?

No and no. human-labeled (state, question, label). 166,054 rows / 22 configs. soft_label for human uncertainty. license **other**; likes **0**; sha `c9c3032c`. Praveenrajus/jev-bench ≠ fstandhartinger/jevbench. Do not collapse “Jevify” tag into uspraveen/Jevify. `notes.md` §107.

## Did Hub ship Bonsai weights? Is 100/100 easy T/F Harbor? Is label_mass correctness? Collapse Nicolai spellings?

No, no, no, and no. ternary bonsai System One GGUF. openjev's mechanism, Bonsai's weights. Hub does not ship weights. 100/100 easy T/F is not Harbor. label_mass ≠ correctness. stock llama.cpp Q2_0 silently gibberish. NicolaiMTLassen/open-bonzi-jev ≠ NicolaiLassen. Hub MIT likes **0** sha `09240156`. GH companion NicolaiLassen/open-bonzi-jev Python MIT; **0★**; HEAD `1c2508fd`; size **0** with contents. `notes.md` §107.

## Collapse DeBERTa ONNX into the Qwen scorer ONNX? Re-card com-kotobalabs as new? Does AutoModel fail?

No, no, and no. transformers.js DeBERTa ONNX. source:com-kotobalabs/open-jev-deberta-v3-large. temperature 1.05. AutoModel from_pretrained works (contrast 0145 T=1.75 AutoModel cannot load). apache-2.0; likes **0**; sha `3bc2553b`. onnx-community/open-jev-deberta-v3-large-ONNX ≠ system-one-qwen3.5-4b-scorer-ONNX. Source metrics stay *theirs* on the original. `notes.md` §107.

## Did openJev-verdict-2.0 beat Jev this hour? Are 151M and 149.6M two models? Is PR #1 still open?

No, no, and no. 107★ densify. GH 151M vs README 149.6M. PR #1 now closed unmerged. do not re-fold §71 claim-audit as a beat. Claims still *theirs* N=2000: 77.10% / Brier 0.0636 / ECE corr 0.0144 / dist ECE 0.1513. Dual-channel ECE design fork. Still Hypothesis until independent run. ≠ IamBusy/OpenJev `/v1/decide`. Python; README Apache-2.0 / GitHub SPDX NOASSERTION; **107★**; HEAD `a458733c`; README SHA `05ca75af`; size **14728**. `notes.md` §107 (densify of §71).

## Is wjdjdakf17/jev-study a live API? Collapse into baekenough/jev-study? Is structured correct?

No, no, and no. typed decisions, RLCD, confidence-gated routing. structured ≠ correct. mock not live API. 26 tests. TypeScript MIT; **0★**; HEAD `24b5d7d7`; README SHA `4ca30c93`; size **34**; default **master**. wjdjdakf17/jev-study ≠ baekenough/jev-study. Code consumes probability. `notes.md` §107.

## Did Archer land this hour? Treat Qwen3.8-27B as Archer? Invent tweets? Reopen PR #23 or #24?

No, no, no, and no. Hub `archerhume/4rcherhume` HTTP **401** (not re-fetched as a rewrite). Tracker `multimodalart/jev-reproductions-tracker` likes **59**; lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED** vs §106. Live REST pulse: SemIf **2094★** (+20 vs §106 **2074**); jevlike **1023★** (+1 vs §106 **1022**); TypeAR-AI/TypeAR **12★** **flat**. AnotiaWang/awesome-jev **93★** (+1 vs §106 **92**) ≠ Awesomejev 561/27007. Hub Laya likes **729**. Qwen3.8-27B ≠ Archer. do not reopen or amend PR #23 or #24. `invented_signal: false`. `notes.md` §107.

## Did Hub ship Bonsai family weights this hour? Is WANLI-256 Harbor? Collapse stock Q1_0 into §107 Q2_0 gibberish?

No, no, and no. bonzi-27b-v2 / ternary-8b / 27b-v1 GGUF family densify. Hub still does not ship weights. WANLI-256 74.6% / 65.2% / 71.1% *theirs*. ternary still needs PrismML fork. Bonsai 1 27B Q1_0 runs on stock llama.cpp. label_mass ≠ correctness. 100/100 easy T/F ≠ Harbor. Hub MIT likes **0** shas `c4d21b74` / `47b66187` / `2fb8061a`. Do **not** re-card NicolaiMTLassen/open-bonzi-jev as a new species. `notes.md` §108.

## Treat the HF verdict twin as a weights drop? Are Hub likes 5 the same as GH 107★? Re-fold §71 as a beat?

No, no, and no. hf:heman10x/openJev-verdict-2.0 twin tokenizer-only. tokenizer + config + README; **no 149.6M weights**. apache-2.0; likes **5**; sha `794d5e0d`. Still Hypothesis until independent run. ≠ IamBusy/OpenJev `/v1/decide`. `notes.md` §108 (twin of §71 / §107).

## Does OpenJev Vision work on CLEVR joint? Is Pets 93.24% the official full-dataset number? Is it TypeSafe Jev?

No, no, and no. OpenJev Vision image classification + uncertainty. CLEVR-4 held-out joint 0% / independent 63.75% / binding 56.25% *theirs*. Pets 740-subset **93.24%** ≠ official full-dataset. Not TypeSafe Jev; not a VLM. license **other**; likes **0**; sha `8cf6cbd3`. `notes.md` §108.

## Are 294,912 derived targets independent samples?

No. hfdataset:IamBusy/OpenJev-Vision-Research-v0.1 12,832. 36 Boolean questions per synthetic image yield **294,912** derived targets, **not** independent samples. likes **0**; sha `43e49184`. `notes.md` §108.

## Is Laya ONNX 63/63 ECE? Collapse mizchi into gqgs or Mattepiu? Does it ship weights?

No, no, and it does ship model.onnx **646.9 MB**. Laya multilingual ONNX WebGPU typed-decisions port. 63/63 selected answers / 5.1e-4 CPU / 1.2e-2 WebGPU *theirs*. Independent port, not official Convai. 63/63 argmax ≠ ECE. apache-2.0; likes **0**; sha `b6314ec9`. ≠ gqgs ≠ Mattepiu. `notes.md` §108.

## Is UpHash-Network/mini-jev a new species? Quote 93.25% as Harbor?

No and no. UpHash-Network/mini-jev is yuki-oshio transfer. README SHA `363441b6` unchanged. residual-head 9,222-param decreased 73/96→67/96. Python MIT; **0★**; HEAD `52fbae12`. ≠ r-ms/mini-jev (**26★**). Do **not** re-fold 93.25% as Harbor. `notes.md` §108.

## Is Jev the best *calibrated* injection detector? Should we hard-gate ECE 0.058? Route on 0.5–0.9 as a frequency?

No, no, and no. jev-injection-bench 11,900 labelled prompts. Jev best ranking / Haiku better ECE 0.021 vs 0.058. 0.5–0.9 band is where Jev's numbers do not mean what they say. Prompt wording moves panic 28%. Python MIT; **0★**; HEAD `c0d0f25d`; size **107**. rh-guard owns injection integrity. `notes.md` §108.

## Is jev-dspy-bench a quality grade / merge gate? Collapse into dspachos or jmanhype?

No and no. manojlds/jev-dspy-bench ≠ dspachos/jev-dspy ≠ jmanhype/jev-dspy-lab. Jev agreement is similarity, never ground truth. no aggregate quality grade or merge gate. Python Apache-2.0; **0★**; HEAD `d8c68d72`. `notes.md` §108.

## Quote AbstentionBench rank 1 as current SOTA? Skip question-asymmetry? Is forward-looking 0.465 extreme?

No, no, and no. AbstentionBench-on-Jev rank 1 of 20 vs 2025 field. question-asymmetry. forward-looking 0.465 never extreme. Python; README MIT / SPDX NOASSERTION; **0★**; HEAD `f5c0c068`; size **0** WITH CONTENTS. `notes.md` §108.

## Is openkev a decision runtime? Is select_threshold inf a bug? Does T transfer? Collapse into jaredpalmer/kev?

No, no, no, and no. openkev calibration layer not a runtime. ECE vs coverage independent. select_threshold returns inf. escalation catches uncertainty not ignorance. misakaikato/openkev ≠ jaredpalmer/kev. Python MIT; **0★**; HEAD `babcab1c`. `notes.md` §108.

## Did Docling→Jev beat Gemini? Do titles get generated? Who owns the wall clock?

A tie on 12 documents is a tie. titles selected not generated. parser owns the wall clock (~24 s of 24.5 s is Docling). pdf-race Docling→Jev vs Gemini. JS MIT; **0★**; HEAD `1c687fc6`; size **0** WITH CONTENTS. `notes.md` §108.

## Is jev-atlas a bake-off? Collapse into Zaious or gorock007? Are listed counts eval?

No, no, and no. ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas. catalog not endorsement. JS; license **null**; **0★**; HEAD `bc94bf50`. `notes.md` §108.

## Is flopcheck composite a proof? Can Jev count em dashes?

No and no. flopcheck 16 calibrated tweet judgments. mechanical tells in code. Confidence = peaked distribution, not correctness. TS; license **null**; **0★**; HEAD `eb0de0ba`. Knowledge work / life: hold-before-publish. `notes.md` §108.

## Ship the Space T? Does temperature change argmax? Is Laya confidence top-label p?

No, no, and no. Laya calibration lab Gradio MCP. T never changes argmax. confidence ≠ top-label p. easy probe set refused. 40–48 rows too small to ship T. apache-2.0; likes **0**; sha `a3fc13ba`. `notes.md` §108.

## Did Archer land this hour? Treat Qwen3.8-27B as Archer? Invent tweets? Reopen PR #23 or #24 or #25?

No, no, no, and no. Hub `archerhume/4rcherhume` HTTP **401** (not re-fetched as a rewrite). Tracker `multimodalart/jev-reproductions-tracker` likes **60**; lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED** vs §107. Live REST pulse: SemIf **2128★** (+34 vs §107 **2094**); jevlike **1026★** (+3 vs §107 **1023**); TypeAR-AI/TypeAR **12★** **flat**. AnotiaWang/awesome-jev **94★** (+1 vs §107 **93**) ≠ Awesomejev 561/27007. Hub Laya likes **765**. Qwen3.8-27B ≠ Archer. do not reopen or amend PR #23 or #24 or #25. `invented_signal: false`. `notes.md` §108.

## Collapse kushalpatil/jevify-gemma4 into Mintzs / gulagala001 / uspraveen? Treat LoRA stubs as independent eval? Hard-gate n=307 ECE 0.061?

No, no, and no. Gemma-4 26B-A4B jevify classification+calibration. Gemma-4 E4B jevify. Hub jevify merged LoRA ships weights. PAWS 0.580/ece 0.288 is the weak cell. smaller E4B slightly better OOD ECE than 26B-A4B. LoRA adapter twin not independent eval. E4B LoRA stub card. GH kushalpatil07/jevify 404. kushalpatil/jevify-gemma4 ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify. license **gemma** / LoRA license **null**; likes **0**; shas `d4c0d1d4` / `ec4a3d22` / `a6b5a716` / `cca1f55e`. `notes.md` §109.

## Re-card open-bonzi-jev or §108 27B/ternary as new? Did Hub ship the 1.7/4/8 v1 GGUF? Is WANLI-256 64.5/60.2/52.0 Harbor?

No, no, and no. bonzi Bonsai-8B v1 GGUF densify. Bonsai-1.7B v1. Bonsai-4B v1. WANLI-256 64.5% / 60.2% / 52.0% *theirs*. rank #4 / #5 / #6 of 6. Hub still does not ship weights. label_mass ≠ correctness. MIT; likes **0**; shas `588bc44e` / `48148bf9` / `d5545084`. Do **not** re-card NicolaiMTLassen/open-bonzi-jev. `notes.md` §109.

## Is JulesHuisman/jev-eval a Harbor harness? Collapse into SivletLabs / 4esv / dayhaysoos/jevals?

No and no. JulesHuisman/jev-eval scaffolding / README SHA c356a584 (was empty e69de29b). Python; license **null**; **0★**; HEAD `96c2a110`; size **0** WITH CONTENTS; default **master**. JulesHuisman/jev-eval ≠ SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv ≠ xxkuboxx ≠ onlyoneaman ≠ dayhaysoos/jevals. Do not copy example.env keys. `notes.md` §109.

## Quote 40-band 0/10 without 7-band? Does Jev run the physics?

No and no. 7 bands 6/10 vs 40 bands 0/10. Option label IS the pixel; physics/collisions/scoring local. Python MIT; **1★**; HEAD `0224c21c`; size **0** WITH CONTENTS. LiuHao-1443/jev-table-tennis. `notes.md` §109.

## Is 32/32 synthetic production? Hard-gate 0.8 evidence as proof?

No and no. source receipts + confidence slider re-policy without re-inference. 32/32 synthetic is smoke not production. 0.8 still soft. Python MIT; **0★**; HEAD `a9669e94`. laguagu/jev-evidence-lab. `notes.md` §109.

## Invent hfjev accuracy? Collapse ultra_laya into NandhaKishorM/laya? Use the watch spelling roadus2?

No, no, and no. classify HF datasets across typed semantic dimensions. **no numbers**. hemanth/hfjev Python MIT; **1★**; HEAD `6f2aa501`. roadus2 watch misspelling; lock roadius2/ultra_laya. ultra_laya REVIEW defects. default branch claude/laya-jev-review-gg5ppo. Do **not** paste vs-Jev table as this-fork win. Apache-2.0; **0★**; HEAD `0dff5bd2`. `notes.md` §109.

## Did MASSIVE prove RU = EN? Is confidence independent of p_max? Hard-gate Δ −11.0 pp as “Jev cannot do Russian”?

No, no, and no. XNLI EN 88.3% ECE 0.032 → RU 77.3% ECE 0.096. Δ −11.0 pp [−14.2,−7.8]; ECE +0.063. MASSIVE no detectable difference at n=600. confidence is function of p_max (r=1.000). Pre-registered; n=600; 4,800 calls. Python MIT; **0★**; HEAD `7167894a`; size **1302**. AHTOOOXA/jev-cyrillic-audit. PRIMARY. `notes.md` §109.

## Is jev-llm a generator? Treat “zero hallucination” without the bank constraint?

No and no. pointer-not-generator 400 human-authored responses. Zero hallucination = bank constraint. JS; README ISC / GitHub license **null**; **0★**; HEAD `194db1a6`; size **54**; default **master**. akash-kamat/jev-llm. `notes.md` §109.

## Is proposed authorized? Treat gated 100% (95/95) as a production guarantee?

No and no. proposed ≠ authorized. FewRel 160: Jev 85.0% vs lexical 13.125%. gated 100% (95/95) coverage 59.375%. Track 2 episodic 85.6% *theirs* ≠ Track 1 FewRel 85.0%. Python Apache-2.0; **0★**; HEAD `7a6f7d05`. chenmingtang830/jevgraph. `notes.md` §109.

## Is J++ Visual J++? Collapse into southpolesteve/probably?

No and no. J++ composable semantic computation language. Python MIT; **3★**; HEAD `14d77789`. Towow-ai/jpp ≠ Microsoft Visual J++ ≠ southpolesteve/probably. `notes.md` §109.

## Treat /judge 0.5 as truth? Do unit tests call a model?

No and no. judge-jev 0.5 still soft. Worker owns parse/thresholds/labels/formatting. Unit tests never call a model. TS; license **null**; **0★**; HEAD `1bf495d3`. Mishkun/judge-jev. `notes.md` §109.

## Are A/B/C Harbor ranks? Do stars affect the score?

No and no. 947 repos scored; A 273 / B 302 / C 372. LLM rubric ≠ benches. Star counts never affect score. Python; README MIT+CC-BY-4.0 / SPDX NOASSERTION; **0★**; HEAD `71d53be2`; size **6277**. tunahansahin897/what-is-jev. `notes.md` §109.

## Did whyashthakker crown a GPT winner? Collapse into walidboulanouar?

No and no. No benchmark winner is claimed. HTML MIT; **3★**; HEAD `74583663`. whyashthakker/awesome-jev-use-cases ≠ walidboulanouar/awesome-jev-use-cases. GH desc vs README honesty. `notes.md` §109.

## Collapse dog-last into AnotiaWang / Frank-ZY-Dou / awesomejev.com? Skip the regex baseline?

No and no. Guide not directory. phishing: naive 62.6% vs regex 91.8%; 5-atomic + LR 95.0% *theirs*. Python MIT; **1★**; HEAD `206fdcab`. dog-last/awesome-jev ≠ AnotiaWang ≠ Frank-ZY-Dou ≠ RadRebelSam ≠ yibie ≠ cobanov ≠ logicrw ≠ v-modal ≠ awesomejev.com. `notes.md` §109.

## Copy npm install for shinpr/jev-reranker? Collapse into 1441 Jev-Reranker?

No and no. README npm global; repo is Rust. Rust MIT; **1★**; HEAD `731deba3`. shinpr/jev-reranker ≠ 1441 Jev-Reranker ≠ carlaiau/jev-reranking ≠ rdxtremity. Filter 0.5 still soft. `notes.md` §109.

## Is git-confess 11% a person verdict? Does Jev own the ratio?

No and no. git-confess code owns counting/blame/ratio. httpx exhibit 11% (13/119) *theirs*. Python MIT; **0★**; HEAD `54cd2849`; size **3**. AHTOOOXA/git-confess ≠ commitjev. squash-merge caveat. `notes.md` §109.

## Treat paper-trader +12.40% as edge? Are fills a strategy win?

No and no. 90d trend +12.40% vs random +12.75% vs BH +41.71%. 5m win rate 25%. Default switched to trend so UI shows fills — do not treat fills as edge. Paper trading not live. JS; license **null**; **0★**; HEAD `73662f79`. waterme7on/jev-paper-trader. `notes.md` §109.

## Did Archer land this hour? Treat tracker likes 64 as a landing? Treat Awesomejev 656/38160 as eval? Reopen PR #23–#26?

No, no, no, and no. Hub `archerhume/4rcherhume` HTTP **401** (not re-fetched as a rewrite). tracker likes 64 (+4) lastModified UNCHANGED. Tracker likes **64** (+4 vs §108 **60**); lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED**. Laya present; Blackwood ABSENT; Archer still promised_not_landed. Laya present (likes **783**); Blackwood ABSENT from tracker ITEMS; Archer still promised_not_landed. Live REST pulse: SemIf **2166★** (+38 vs §108 **2128**); jevlike **1031★** (+5 vs §108 **1026**); TypeAR-AI/TypeAR **14★** (+2 vs §108 **12**). AnotiaWang/awesome-jev **95★** (+1 vs §108 **94**) ≠ Awesomejev 656 entries / 38,160 stars (was 561/27007). Qwen3.8-27B ≠ Archer. AITuber tension ±15. do not reopen or amend PR #23 or #24 or #25 or #26. do not reopen or amend PR #23/#24/#25/#26. `invented_signal: false`. `notes.md` §109.

## Treat Blackwood tracker-absent as landed? Treat Hub Meanblock as a new species vs leesk212?

No and no. Blackwood tracker ABSENT; likes 2 gated manual. Census densify only. GH Meanblock 404; lock leesk212/JEV-CPU. softmax over letter slots ≠ Noul. Hub `archerhume/4rcherhume` HTTP **401**. `notes.md` §110.

## Treat ECE 0.021 as a hard gate of honest probabilities? Treat Independent `{cat,dog}` as Choice?

No and no. r = c - p_a. ECE 0.021; acc 0.807 vs warmup 0.746. calibration beyond ~500 tokens unmeasured. Independent primitive. 11.57s vs 54.10s · 4.67× · 120/128 *theirs*. default path is pretrained Gemma probs not trained RLCD head. Independent is a fourth primitive beside Choice/Score/Noul. `notes.md` §110.

## Distill Jev as teacher of record? Treat priority 0.464 without the majority floor? Treat 3-way NLI as a Noul?

No, no, and no. do not distill Jev as teacher of record (they distilled Haiku). priority 0.464 = majority floor. banking77 contaminated. raw margins not probabilities. GH jev-haiku-benchmarking 404. WANLI 0.741 vs openjev v2 0.77 *theirs*. 3-way NLI ≠ Noul. Teacher-copy vs gold vs zeroshot is three supervision regimes, one schema. `notes.md` §110.

## Treat 0.9 as one number? Collapse Running-Dolphins/jev-bench into Praveenrajus/jevbench?

No and no. “0.9 is not one number”. ranking ≠ calibration. banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*. ≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench. Python MIT; **0★**; HEAD `67d2ee42`; size **1070**. Running-Dolphins/jev-bench. PRIMARY. `notes.md` §110.

## Treat circulating $0.0004 as measured? Treat Score as 0–1? Treat Noul.confidence as existing? Treat json_schema gap as a typed-model win?

No, no, no, and no. $0.0000153–$0.0000226 vs circulating $0.0004 (~20×). Score is 0..n-1 expectation not 0–1. Noul has no confidence field. TCP floor 198.8 ms. type reliability is not a reason to choose Jev (json_schema 5/5). gateway tax not one number. WallerChen/jev-measured Python MIT; **0★**; HEAD `4a12dfb3`. PRIMARY. `notes.md` §110.

## Treat 8/8 as conversion lift? Collapse RadRebelSam/jev-decision-lab into RadRebelSam/awesome-jev?

No and no. Function-only 5/8 vs hybrid 8/8. 4/8 without Jev. 8 designed cases not conversion lift. ≠ RadRebelSam/awesome-jev. TypeScript MIT; **0★**; HEAD `e6d6d42d`; size **128**. `notes.md` §110.

## Treat a 200-row BigQuery pilot as a ranking? Treat Tetris play as a bake-off?

No and no. 200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*. not a ranking. NLI Tetris argmax P(entail)−P(contradict). Jupyter MIT; **0★**; HEAD `cb9ef56b`; size **307**. jackojacko05/compare-jev-bigquery-ai-functions. Trecto34/openjev-fighting-ring Python; license **null**; **0★**; HEAD `ac544f1e`. `notes.md` §110.

## Collapse joshhu/jevtest into realZachi/jevtest? Treat 64× Space as Harbor / JevBench v1.2?

No and no. 情緒測謊器. 1q 396ms / 30q 567ms. ±0.03. 33q $0.000045 vs Gemini ~5× slower ~60× cost *theirs*. ≠ realZachi/jevtest. 8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*. synthetic; no inference. ≠ JevBench v1.2 §78. joshhu size **34**. `notes.md` §110.

## Treat awesome listed counts as eval? Paste APA “microsecond policy / zero hallucination”?

No and no. Judged 3317 / listed 2560. Jev judges, code applies policy. catalog ≠ endorsement. APA “microsecond policy / zero hallucination” overclaim. rhc98/awesome-jev TypeScript; **1★**; HEAD `82898f25`. AiPersonacademy/Awesome-jev-use CC0-1.0; **2★**; HEAD `29246f12`. `notes.md` §110.

## Copy keys / cargo for questionator / grill-jev / jev-lsp? Treat selecting an option as permission? Treat LSP diagnostics as a proof?

No, no, and no. Client-side quiz; pointer from held docs; scanned-PDF warn. CSP only api.typesafe.ai. Jev judges / agent reasons / user decides. selecting an option is not permission to implement. degraded fallback. pattern exact, judgement must clear floor. no matching pattern → no model call. not a correctness oracle. $0.00022 vs chat $0.00306 *theirs*. Do not copy keys / `uv` / `npm` / `pip` / `cargo`. `notes.md` §110.

## Treat 0.85 as 85% / minProbability as Harbor? Treat :max as a mandatory search size? VERIFY by rescoring the same pool?

No, no, and no. Spec vs artifact remainder. treating 0.85 as 85% / minProbability hard-gate as Harbor. VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring. fast/full/max are ceilings not sizes. Solar writes, Jev chooses NEXT ACTION. Hard-gating minProbability 0.85 as a CI proof is soundness theater. nozomi-koborinai/jev-spec TypeScript MIT; **1★**; HEAD `86f14198`. 202620325-spec/Jev-LLM Python MIT; **0★**; HEAD `da06b6d1`. `notes.md` §110.

## Did Archer land this hour? Treat tracker likes 64 as a landing? Reopen PR #23–#27?

No, no, and no. Hub `archerhume/4rcherhume` HTTP **401** (not re-fetched as a rewrite). tracker likes 64 flat, lastModified UNCHANGED. Tracker likes **64** **flat** vs §109; lastModified `2026-09-20T04:29:16.000Z` **UNCHANGED**. Laya likes 802 (was 783). Blackwood tracker ABSENT; likes 2 gated manual. Archer still promised_not_landed. Live REST pulse: SemIf 2186★ (+20 vs §109 2166); jevlike 1038★ (+7 vs 1031); TypeAR 14★ flat. AnotiaWang 96★ (+1 vs 95) ≠ yibie/awesome-jev 490★. Qwen3.8-27B ≠ Archer. do not reopen or amend PR #23/#24/#25/#26/#27. `invented_signal: false`. `notes.md` §110.


## Treat ECE as alpha? Treat paper-trader +12.40% as this hour?

No and no. Calibration is not alpha. NO CURRENT ALPHA CANDIDATE. ΔR² approximately +0.00084. Brier 0.2131387. ECE 0.0421875. Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05. alakise/calibration-is-not-alpha Python MIT; **0★**; HEAD `064b75f5`; size **268**. PRIMARY. `notes.md` §111.

## Treat default 0.5 compaction as safety? Treat keep p as a frequency?

No and no. default 0.5 keeps zero non pinned. keepResult median 0.14 to 0.17. keepCall median 0.28 to 0.35. usable range is about 0.10 to 0.25. 7.8% to 57.9%. judges results it never sees. task-finish eval not built yet. $0.002 per compaction. OrMizL/jev-compaction-bench JavaScript MIT; **0★**; HEAD `92fd33e6`. PRIMARY. `notes.md` §111.

## Collapse sgr-judge-bench into jev-judge-bench? Treat 114/120 as Harbor / intervals-including-zero as equivalence?

No, no, and no. slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench. Jev 108/120 $0.083 0.34 s. Luna SGR 114/120. paired Jev accuracy-difference intervals include zero. not evidence of equivalence. GLM SGR 26/120 93 format failures. Terra-planned Jev hybrid 55/120. Python; SPDX NOASSERTION; **0★**; HEAD `5e142707`. PRIMARY. `notes.md` §111.

## Treat 90.53% BBQ as calibrated? Treat softmax over A/B/C as a Noul?

No and no. prefill plus exactly one decode. softmax over A/B/C ≠ Noul. BBQ 9,053/10,000 (90.53%). ECE 0.0890. Mean confidence 0.9943. overconfident. score and noul not implemented. siren2345/jev-single-decode Python MIT; **0★**; HEAD `65df86a3`. `notes.md` §111.

## Collapse jasonkneen into pngwn? Treat 0.740 as TypeSafe vs Laya?

No and no. encode the state once, decide everything in parallel. 0.740 accuracy against a 0.508 majority. ECE 0.047. fine-tune's advantage ends where its 384-token training data does. jasonkneen/open-jev ≠ pngwn/open-jev. same sha d41dc3cd. pngwn likes **25**. `notes.md` §111.

## Treat DGUI 12 rows as a corpus? Re-fold INSTRUCT 119 as new? Treat jevlogs explorer as a live call?

No, no, and no. DGUI 12 rows (was 6). INSTRUCT 119 rows likes 2. Space does not call Jev. recomputes routing from saved probabilities. `notes.md` §111.

## Treat 97.0% mailordinal as Harbor? Treat 0.8 nlgrep as 80% correctness? Treat contract_passed as truth / Wilson 0.85 as a proof?

No, no, and no. 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22. synthetic repository benchmark. YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep. default threshold 0.8 still soft. 40-line windows cannot prove whole function. token-native sequential start/end Choice. Gemini/Haiku stubs not configured yet. Jev evaluations are advisory. laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills. contract_passed is not a claim of guaranteed factual truth. Wilson lower bound 0.85 floor. fixture mode no savings claim. handful of hand-written examples, not a benchmark. Jev judged exactly what it was given. rule-based by default, optionally Jev-backed. empty README. missing key cannot break the experience. `notes.md` §111.

## Did Archer land this hour? Treat tracker likes 64 as a landing? Reopen PR #23–#28?

No, no, and no. Hub `archerhume/4rcherhume` HTTP **401**. tracker likes 64 flat, lastModified UNCHANGED. Laya likes 822 (was 802). Blackwood tracker ABSENT. Archer still promised_not_landed. Live REST pulse: SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14). AnotiaWang 97★ (+1 vs 96) ≠ yibie/awesome-jev 506★ (+16 vs 490). do not reopen or amend PR #23/#24/#25/#26/#27/#28. `invented_signal: false`. `notes.md` §111.



## Collapse NanoJev into TypeSafe Jev / jev-forge / arena forks? Treat 128/128 as Harbor / a Noul?

No, no, and no. TianyuCodings/NanoJev unified-games-v1 densify. A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding. One model, four games. ViZDoom Basic 128/128 vs Jev 56/128. Predict Position 27/128 vs Jev 11/128. Maze 225 attempts vs Jev 2738. Snake 30 food / 256 steps. held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128. Untuned Qwen3-0.6B baseline. not TypeSafe Jev; open replica / specialist gameplay S1. caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev. Game success ≠ calibrated Noul. Python MIT; **1289★** / **158** forks / size **64035**; HEAD `618cea6d906d54e128360786d12f703fff2b1245`. `notes.md` §115.

## Treat local `boolean` as TypeSafe noul? Treat a normalized Choice bag as calibrated? Copy `pip` / serve recipes? Reopen #31–#35?

No, no, no, and no. local type boolean ≠ TypeSafe noul. A normalized distribution alone does not establish empirical probability calibration. soft scores ≠ hard gates. Demo HTTP 401 gated; recordings local. 18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6. Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58; dataset C-Tianyu/NanoJev-Data likes 5. do not reopen or amend PR #31/#32/#33/#35. `invented_signal: false`. `notes.md` §115.

User-provided 0915 uniqueness lock: TianyuCodings/NanoJev unified-games-v1 densify; A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; 18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58; dataset C-Tianyu/NanoJev-Data likes 5; HEAD 618cea6d906d54e128360786d12f703fff2b1245; 1289★ / 158 forks / size 64035; README SHA 4190093c64ee75b26e9726daa3b00cbcf6d3157a; MIT; caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; not TypeSafe Jev; open replica / specialist gameplay S1; soft scores ≠ hard gates; Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; invented_signal false; do not reopen or amend PR #31/#32/#33/#35; notes.md §115

## Collapse ywchiu into Running-Dolphins/jev-bench or Praveenrajus/jev-bench? Treat 77.0% as Harbor / 100% schema as correctness?

No, no, and no. ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench. Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%. restriction state 95.0% against 84.4%. None of the systems are particularly good at knowing when to stop and ask. They skip the question and call a tool directly. 100% schema pass. six-field joint 48.8% vs 72.8%. GitHub license null; **1★**; HEAD `4322c350`; README SHA `75e6a338`; size **173**. PRIMARY. `notes.md` §113.

## Collapse jev-single-decode-transformers into jev-single-decode? Treat softmax over A/B/C as a Noul / 90.53% as calibrated?

No, no, and no. siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode. Split Transformers experiment from llama.cpp runtime. BBQ 9,053/10,000 (90.53%). ECE 0.0890. Mean confidence 0.9943. overconfident. score and noul not implemented. Python MIT; **0★**; HEAD `2aa5fea7`; size **0** WITH CONTENTS. `notes.md` §113.

## Collapse tanayvasishtha/jev-lab into dairui1 / BrendanH18 / yibie/laya-jev-lab? Treat the scaffold as a bake-off?

No and no. tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab. Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling. second pass must be $0.00 from cache. The pages never call Jev. **0★**; HEAD `96c90cdd`. `notes.md` §113.

## Treat TF-IDF ECE 0.0207 as beating Jev? Collapse Verdict-open-jev into openJev-verdict-2.0? Treat 0.85 as 85%?

No, no, and no. Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0. TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440. Verdict-open-jev 48.07% vs Jev 90.80%. abstention combined recall 10.00%. p50 35.58 ms. K=25 (maximum capacity) 72.00%. 0.85 coverage 84.60% selective risk 1.18%. Python; **33★**; HEAD `30f15564`; size **6709**. `notes.md` §113.

## Treat Mintzs 90.0% as calibrated? Collapse altryne/jevify into Mintzs/jevify? Invent tweets?

No, no, and no. 26.1× faster than standard Qwen JSON generation. Jevify 90.0% / 167 ms CUDA graphs disabled. Uncalibrated. altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify. Find where Jev belongs. Design the questions. Measure the difference. Do not invent X/Twitter discourse. `notes.md` §113.

## Treat Brier on stated confidence as RLCD? Treat Student B 86.0% as independent gold?

No and no. Finding 1: Brier on stated confidence alone is a trap. grpo_rlcr 0.78 / ECE 0.084. reliability 0.007 but resolution 0.000. Student B MAE 0.148 / Pearson 0.836 / 86.0%. do not distill Jev as teacher of record. `notes.md` §113.

## Treat HDFS 0.9933 as Harbor? Treat 40–48-row T as production? Re-fold pngwn RESULTS as new?

No, no, and no. HDFS 0.9933 (745/750) / retain 0.0084. BGL ERROR/FATAL protection 1.0000. 2,479 / 2,500 HDFS uncertain. cache hit 0.9648 (2412/2500). $0.153936 estimated. E2 recomputes from saved probabilities. Space sha eda59e0a. MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133. 40–48 rows too small to ship T. T never changes argmax. pngwn/open-jev-laya-bench README 404. sha 9f69c742 likes 2. 22 configs · 166,054 rows · 4 calibration-gold. sha a39eba3f. 27 900 schema-driven decisions. 13 600 / 13 600 questions. candidate mass min 0.99999624. `notes.md` §113.

## Treat ACT as a provider proof? Collapse Jev-Skill into simplosophy/jev-skill? Treat current-llm as a Jev replica?

No, no, and no. ACT / REVIEW / FALLBACK. A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome. confidence is descriptive provider output, not a substitute for probability. Quality denominators include only valid scored answers. an exact halfway tie chooses the lower level. aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills. The local path does not claim to turn a smaller checkpoint into Jev. Low support becomes decision: "review". MIT-0 SPDX NOASSERTION. current-llm. 结构兼容，不是 Jev 模型能力. `notes.md` §113.

## Did Archer land this hour? Treat TypeAR-AI/TypeAR as the live name? Reopen PR #23–#30?

No, no, and no. Hub `archerhume/4rcherhume` HTTP **401**. TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM. TypeLLM/TypeLLM 16★. tracker likes 67 (+3 vs 64). lastModified UNCHANGED `2026-09-20T04:29:16.000Z`. Laya likes 864 (was 822). Blackwood tracker ABSENT. Archer still promised_not_landed. Live REST pulse: SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043). AnotiaWang 98★ (+1 vs 97) ≠ yibie/awesome-jev 525★ (+19 vs 506). Qwen3.8-27B ≠ Archer. do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33. `invented_signal: false`. `notes.md` §113.

Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

## Compare Jev against GPT-5.6? Is that the right bakeoff?

No. Jev vs GPT-5.6 bakeoffs are a category error. [@mervenoyann](https://x.com/mervenoyann/status/2101463303734067592)
*theirs*: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows. Right lineage = encoder / ZS classifiers (BERTForXYZ → DeBERTa → ModernBERT), same class as System One / categorization / scoring. Jev is exemplar not the mandate. Institutional HF voice — quote *theirs*; do not invent accuracy numbers. Do **not** collapse into §110 aahf 64× Space. likes 421 / 189; impressions 35498 / 9613 (ephemeral). `notes.md` §112.

## Many LLM apps were a skill issue — skip the classifier?

Often yes as a *placement*, never as a stack replacement. Parent *theirs*: many problems solved with LLMs could have been solved with them, it was a skill issue. Mixed architecture: replace-one-classifier-step; generation stays where something must be written. Cousin of Akshay’s LLM hammer (§85), from an institutional HF voice. `notes.md` §112.

## Opt for DeBERTa and ModernBERT? Copy the Hub `pipeline()`?

Prefer the family; do not copy the recipe. Follow-up *theirs*: opt for DeBERTa and ModernBERT ones. Hub pointers: [trending ZS](https://huggingface.co/models?pipeline_tag=zero-shot-classification&sort=trending), [task page](https://huggingface.co/tasks/zero-shot-classification), [image<>text](https://huggingface.co/docs/transformers/en/tasks/zero_shot_image_classification). Live likes this pass: hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72. Hub widget default `facebook/bart-large-mnli` likes 1616 is **not** Merve’s pick. Do not copy `pip` / `pipeline()`. softmax/ZS scores still ≠ calibrated Noul. Hub example 0.504/0.479 *theirs*. soft scores ≠ hard gates. Maziyar quoted: Bart, bert, deberta, modernbert, these are all LLMs — that umbrella does not license a GPT-5.6 bakeoff. `notes.md` §112.

## Multimodal ZS image classification — is that the decision? Wait for Archer?

No and no. multimodal image<>text ZS as perception front-end: candidates/labels in, scores out, then a typed Choice/Noul. Skip Archer. `notes.md` §112.

## Reopen PR #23–#29 for this thread?

No. do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29. Fresh PR off main after merged #29 (`a9c8b61`, §111). `invented_signal: false`. `notes.md` §112.


## Treat huncho as Kungie/gut or carldaws/hunch? Treat `{enter:0.8}` as a model property?

No and no. A hunch is a probability with a policy attached. { enter: 0.8, exit: 0.6 } is hysteresis. replay a policy change without inference. Decision models are providers, not the product. huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch. The latch is exact work. `notes.md` §114.

## Treat Qwen2.5 instruct ECE 0.302 as Archer / as a Jev measurement / as a ranking win?

No, no, and no. pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%. temperature scaling still matches it in-distribution. No Jev API was called. Qwen2.5 ≠ Archer. Qwen/Qwen3.8-27B ≠ Archer. Accuracy can stay flat while honesty dies. `notes.md` §114.

## Treat equal-width ECE as the ECE? Treat jeval drift output as a captured run? Collapse jeval into jevals?

No, no, and no. pd.cut bins by equal width while jeval bins by quantile. ECE 0.113 and ECE 0.076 *theirs*. Which number you ship is a real decision, not a detail. jeval drift is not implemented yet. rlaope/jeval ≠ dayhaysoos/jevals. Cost-optimal threshold is policy arithmetic, not a Harbor score. `notes.md` §114.

## Treat hop-ECE as a trajectory audit? Quote 25–60×? Treat Qwen 3.8 as Archer?

No, no, and no. calibration does not compose. ECE has exactly zero statistical power to detect the failure mode that kills trajectories. 25–60× headline withdrawn. P(all-correct): 0.0071 vs 0.0001. TCE / AMS. Deferred Crispification. Qwen 3.8 sparring ≠ Archer. Soft Noul ≠ hard safety: composing calibrated hops then thresholding is cliff cascade, not a proof. `notes.md` §114.

## Is g0runmezadam/what-is-jev a new 947-repo census? Treat A/B/C as Harbor?

No and no. g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307). Densify §109. 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56. catalog ≠ endorsement. `notes.md` §114.

## Treat ask-jev probabilities as calibrated? Collapse into mcp_jev? Treat 0.5 screening cutoff as 100% sensitivity? Treat BERT-Base 93.02 as zero-shot? Treat circuit-vl-4b as Archer? Treat xiaohuaxi as a benchmark?

No across the board. 13 focused checks and one mutually exclusive outcome. Probabilities are advisory, not calibrated guarantees. omni-/ask-jev ≠ pedroknigge/mcp_jev. light_cutoff_applied_to_combination 0. BANKING77 Accuracy BERT-Base 93.02 Jev 79.90 — BERT figures are published supervised references, not zero-shot. Analyse jev calibration (NLL, ECE) backlog. ranking ≠ calibration. AND: product (independence assumed and recorded in the trace). chat model's stated confidence is not calibrated. circuit-vl-4b ≠ Archer. 不是 benchmark; 概率没做 calibration; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study. Bring your own API key. vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases. recorded run, kinematic animation. 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません. `notes.md` §114.


## Treat llm-to-jev as Jev? Treat the export as equivalent behavior? Collapse it into altryne/jevify?

No, no, and no. Turn decision-shaped LLM prompts into proposed Jev primitives. This is a conversion assistant, not an automatic guarantee of equivalent behavior. The compiler uses deterministic heuristics, not an LLM or evaluation model. alexwestco/llm-to-jev ≠ altryne/jevify ≠ ryana/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify. `notes.md` §118.

## Treat a 0–1 Score prompt as a Noul? Treat `full` compatibility as a production gate? Treat welcome-email as a Choice?

No, no, and no. Score ranges such as 0 to 1 are translated into ordered Jev criteria. Review the generated Score rubric; Jev scores ordered criteria, not an arbitrary 0-to-1 range. Generated instructions and criteria must be reviewed before production use. Prompts requiring open-ended prose are not a fit. Writing new text stays with an LLM. suitability strong/partial/not_a_fit; compatibility full/partial/none. Heuristic conversion ≠ calibrated Noul. Soft scores ≠ hard gates. `notes.md` §118.

## Copy `npm run dev` / store `TYPESAFE_API_KEY` / treat Pages as a live Jev call?

No. Everything runs locally in the browser. There is no framework, database, account, API, or server-side prompt processing. The key is read from the process environment and is never stored or printed. connect-src 'none'. Pages https://alexwestco.github.io/llm-to-jev/ is the static demo. Do not copy `npm`. `notes.md` §118.

## Did Archer land this hour? Reopen PR #23–#32? Push onto #31?

No, no, and no. Hub archerhume/4rcherhume HTTP 401. Archer still promised_not_landed. tracker likes 66 (+2 vs 64) lastModified UNCHANGED. Laya likes 861 (was 822). Blackwood likes 2 gated manual. SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506). do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35. Fresh PR off main. Open #31 is a separate 0743 fold. `invented_signal: false`. `notes.md` §113.

User-provided 0806 uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.


Hourly 0646 uniqueness lock: Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.


Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; 25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; AND: product (independence assumed and recorded in the trace); chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §114


## Collapse SemIf into a new OpenJev census? Is the rename a second species?

No. SemIf was formerly OpenJev. rename is densify not a second census. independent; not affiliated with Jev or TypeSafe. homepage openjev.com. default master. MIT. live REST 2282★ / 140 forks. HEAD ca3ba65f1429. `notes.md` §117.

## Copy the SemIf / MLX installer? Treat `--backend mlx` as a new class?

No. Docs/skill only. MLX backend for Apple Silicon (`--backend mlx`) is a backend, not a species. Tolerate float roundoff in MLX evidence verification. typed output does not guarantee semantic correctness. Do not copy `pip` / `venv`. `notes.md` §117.

## Quote 5.21× as beating Jev? Treat 18/21 as semantic equivalence?

No. Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**). argmax agree 18/21. systems comparison ≠ semantic equivalence. Parallel suffixes 20.03 dec/s on 777 decisions. Direct option logits; 0 output tokens; shared-state parallel. `notes.md` §117.

## Treat 0.813 / 0.845 as Harbor? Merge the ladder with JevBench 74.6?

No. authored BA 0.813, pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases). Softmax over options ≠ calibrated Noul. wire/agreement ≠ replica of TypeSafe. JevBench 74.6 is §78 not this ladder. `notes.md` §117.

## Collapse SemIf into kw2828 / zhihz / semif-rs / semif-serve? Reopen #23–#38? Push onto #39/#40?

No. SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve. interface pattern reproduction with open models; does not reproduce Jev undisclosed model/training. do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38. do not push onto open #39/#40. `invented_signal: false`. `notes.md` §117.


User-provided 0920 jcr uniqueness lock: NiazMorshed2007/jcr MIT; site https://jcr.niazmorshed.dev; topics ai-agents,jev,mcp; **4★**; HEAD `138b3832`; README SHA `2a49dbc1`; LICENSE SHA `46231303`; size **14850**; Jev Capability Resolver; one tool to find documented deterministic commands in a nested capability tree; returns context; **does not execute**; skills = workflow+judgment; capabilities = individual operations; format independent of Jev; proposed open standard exploration; classify (Jev) → optional OpenAI decompose compound → beam search geometric mean of routing probs; keep up to 3 paths ≥60% of best (JCR_BAND_RATIO 0.6); ambiguity / no-match / depth-limit explicit; soft scores ≠ hard gates; 0.6 band is application policy; routing ≠ permission; docs ≠ authority to run; sol-vs-opus5-20 *theirs*: 20 scenarios × 4 variants = 80 runs; lookup+explain only, no execution; Claude Opus 5: agent input 108,585→15,819 (−85%), cost $0.3700→$0.1222 (−67%), wall 105.5s→77.7s; Codex GPT-5.6-Sol: 61,952→47,669 (−23%), $0.1377→$0.1151 (−16%), wall 25.3s→62.4s (Sol slower with JCR in 19/20); One Sol outlier 372.6s / 193 Jev calls; n=1 per cell; Not Harbor task-execution; Claude/Codex harnesses; compare mode; 50 scenarios bundled; 11 groups, 960 nodes, 11,360 items; 16 routing rounds per step; NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34; notes.md §116
User-provided 0922 uniqueness lock: SemIf was formerly OpenJev; independent; not affiliated with Jev or TypeSafe; homepage openjev.com; default master; MIT; HEAD ca3ba65f1429; Tolerate float roundoff in MLX evidence verification; pushed 2026-09-19; live REST 2282★ / 140 forks; size 9177; README SHA 74ab7f7f; LICENSE SHA ca562883; interface pattern reproduction with open models; does not reproduce Jev undisclosed model/training; Direct option logits; 0 output tokens; shared-state parallel; MLX backend for Apple Silicon (`--backend mlx`); Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**); argmax agree 18/21; systems comparison ≠ semantic equivalence; Parallel suffixes 20.03 dec/s on 777 decisions; Browser ladder Qwen3.5-4B authored BA 0.813, pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases); Softmax over options ≠ calibrated Noul; typed output does not guarantee semantic correctness; wire/agreement ≠ replica of TypeSafe; SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve; rename is densify not a second census; JevBench 74.6 is §78 not this ladder; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38; do not push onto open #39/#40; notes.md §117
User-provided 0940 uniqueness lock: Turn decision-shaped LLM prompts into proposed Jev primitives; This is a conversion assistant, not an automatic guarantee of equivalent behavior; The compiler uses deterministic heuristics, not an LLM or evaluation model; It understands a deliberately small set of common prompt patterns; Generated instructions and criteria must be reviewed before production use; Score ranges such as 0 to 1 are translated into ordered Jev criteria; Prompts requiring open-ended prose are not a fit; suitability strong/partial/not_a_fit; compatibility full/partial/none; Writing new text stays with an LLM; Review the generated Score rubric; Jev scores ordered criteria, not an arbitrary 0-to-1 range; Everything runs locally in the browser; There is no framework, database, account, API, or server-side prompt processing; The key is read from the process environment and is never stored or printed; connect-src 'none'; alexwestco/llm-to-jev ≠ altryne/jevify ≠ ryana/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; HEAD 234058ab372d; README SHA 43cd94fb; LICENSE SHA 5f334006; compiler SHA fdf235d0; 2★; MIT; JavaScript; size 29; Pages https://alexwestco.github.io/llm-to-jev/; invented_signal false; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §118


## Treat ggmlc GGUF as llama.cpp? Treat ONNX / Docker / C++ serving as a calibrated replica?

No and no. ggmlc GGUF is not llama.cpp. Loading them in llama.cpp will fail. one encoder pass. serving substrate ≠ calibrated replica. Softmax over options ≠ calibrated Noul. tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx. `notes.md` §120.

## Treat option-order flips as a Noul? Treat Minesweeper ρ as "the model cannot play"? Treat pick_second as pick_by_id?

No, no, and no. jev-position-test n=6. jevmlx slots 5 of 6. hosted Jev 0 of 6. prior_correction made it worse. jevSweeper mean Spearman ρ −0.274. picked exact-optimal 1/25 (4%). 31 of 36 still logically decidable. 86% of the time we should not have been asking. game success ≠ calibrated Noul. pick_by_id vs pick_second. `notes.md` §120.

## Treat LLM2Jev / OpenSourceJev / JEV-MLX / RLCD LoRA as TypeSafe Jev? Treat Qwen3.5-9B as Archer?

No and no. not affiliated with or endorsed by Jev or TypeSafe. No answer tokens are generated. OpenSourceJev llama.cpp Qwen3-1.7B. JEV-MLX Qwen3.5-9B. decision-head-rlcd Qwen3.5-4B 4.9M LoRA. Qwen3.5-4B ≠ Archer. Qwen3.5-9B ≠ Archer. `notes.md` §120.

## Treat AUTO_ACT as a Noul? Treat 0.92 urgency / BLOCK / 40% watermarks as hard gates? Treat 22 to 40% cheaper as Harbor?

No across the board. AUTO_ACT is not a Noul. closed-set fail-open stdlib-only. verified=False. soft scores ≠ hard gates. 22 to 40% cheaper *theirs*. first version 70% more expensive. third-person-audit 40% & 60% watermarks still soft. The included experience uses a handwritten demo provider. `notes.md` §120.

## Treat jev-skill / awesome-jev-live as endorsement? Treat planner writes as JEV writes? Treat ashare-trader as a working edge? Treat typed_evals as official TypeSafe?

No. catalog ≠ endorsement. jev-skill 109★ 90 scenarios. awesome-jev-live 673 entries 4★. planner writes JEV selects. minecraft-agent 214★ 131 JEV decisions 35 Astra calls. nether-final-08 8 minutes 43.300 seconds. RoboJEV structured simulator state not images. 策略未通过自己的回测门槛. 36 组参数全部净期望为负. no positive expectation under real costs. typed_evals NOT an official TypeSafe AI product. jev-as-judge is a sensor. CDC 5,000 Jev 72.2% AUC 0.7725 *theirs*. accuracy is a trap. 9.0% base rate always-no 91.0%. 111-case benchmark *theirs*. Do not reopen or amend PR #23–#42. `invented_signal: false`. `notes.md` §120.

## Treat reflex / pngwn / a blueprint as TypeSafe Jev? Treat Qwen3.5-4B as Archer?

No. It is an open re-creation of Jev. less calibrated. open recreation ≠ calibrated replica. pngwn demo accuracy 0.705 ECE 0.046 ~112 ms *theirs*. This dataset and model are independent research artifacts, not reproductions of Jev or RLCD. Qwen3.5-4B ≠ Archer. A blueprint is not a replica. `notes.md` §121.

## Treat perch / oxlint / patdown as a proof? Treat cutoff 0.8 as a hard gate?

No. semantic lint is a sensor not a proof. the plugin reports an error when the yes-probability clears your cutoff. cutoff 0.8 still soft. patdown fuzzy linter. nassim-arifette/jevgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep. PanAchy/jevvy ≠ Atominac/jevvy. soft scores ≠ hard gates. `notes.md` §121.

## Treat paired CIs / BANKING77 / 35x / 430/500 as Harbor? Treat 24 invented tickets as calibration?

No. paired bootstrap CIs *theirs*. +0.82 pts XQuAD-EN 95% CI +0.35 to +1.31. +7.62 pts SciFact CI +4.88 to +10.38. BANKING77 500 Jev 81.0% GPT-OSS 82.8% Mercury 73.2% Gemini 85.4% *theirs*. Same accuracy, 35x faster *theirs*. systems comparison ≠ semantic equivalence. frozen cascade missed its evaluation accuracy target 430/500 vs GPT-5 432/500. This is not demonstrated equal-quality savings. 24 invented tickets. Routing errors caught by the gate 0 of 3. sample too small to establish calibration. This is not TypeSafe Jev. No real API requests were made. No orders, no advice. `notes.md` §121.

## Treat a Laya HTTP/ONNX/MCP server as a calibrated replica? Treat BeatAPI 125 as endorsement? Treat a permission plugin as confidence?

No. wire-compat ≠ replica. KonghaYao/laya-jev 按官方接口写的客户端只改一个 base URL. gqgs/laya-onnx densify 496.8 MiB. serving substrate ≠ calibrated replica. All 125 projects. catalog ≠ endorsement. BeatAPI/awesome-jev ≠ 99hansling/awesome-jev ≠ Vishnurr2k01/awesome-jev ≠ robokrunch/awesome-jev ≠ rudy2steiner/awesome-jev-hub. Independent project. Not affiliated with TypeSafe. permission ≠ confidence. Kevthetech143/super-jev densify experimental V0.2.0. allay-team/openjev ≠ piyush-infocusp/openjev ≠ TheoLeeCJ/openjev. Do not reopen or amend PR #23–#43. `invented_signal: false`. `notes.md` §121.



Hourly 0947 uniqueness lock: Fast and cheap agent evals. jev as judge.; 18,041 skills from the 200 most-starred repos; Not a security scanner; 最简 Jev 调用演示器; confidence 不是正确率; q93304989-bit/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; 75% cheaper and 18% faster withdrawn; jev @0.15 100% recall 87% savings; 33Audits/jev-auto ≠ gargpratyush/jev-router; no Typesafe key, no PI_API_BASE, zero deps; tool-emitted Score/Noul ≠ calibrated Noul; semantic_compatibility: false; candidate_mass; Qwen3.5-2B ≠ Archer; Jev evaluates decisions; it cannot run a coding-agent session; Status: no model yet; S1LV3RJ1NX/openjev ≠ TheoLeeCJ/openjev; 28 accepted decisions; 3 targets; score 800; health 100; arcade game not a flight trainer; A successful live TypeSafe call has not been verified for v0.1.0; abhibansal60/tidy ≠ MANISH007700/tidy; No model, Jev included, predicted which channels its owner keeps; seed 1 selected on a held-out 400-item validation split; Brier 0.342 → 0.378; more accurate and more overconfident; Qwen3.5-4B ≠ Archer; static quants of kushalpatil/jevify-gemma4-26b-a4b; The labels were corrected, and one earlier result was retracted; zero of 23,869 eligible rows; Do not compare cost without checking task success; Exit 1 is not a proof; kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go ≠ official; 38 tests that cannot fail in a 356-model warehouse; if a parser can answer it, Jev is never asked; 359 of them; Games & Simulation 82; Education & Learning 1; Ratings are heuristics; syedabbasshaheer-art/jev-atlas ≠ ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases ≠ walidboulanouar/awesome-jev-use-cases ≠ vamsikrishna2421/jev-usecases; Every headline result above is self-reported; Archer Hume 84.6% MMLU-Pro is a third-party probe not landed Archer; catalog ≠ endorsement; judge ≠ actuator; softmax over A–H ≠ Noul; SemIf 2270★; jevlike 1054★; TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 538★; Laya likes 889; tracker likes 68 lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#35/#36/#37/#38/#40; do not push onto open #39; notes.md §119
Hourly 1049 uniqueness lock: ggmlc GGUF is not llama.cpp; Loading them in llama.cpp will fail; one encoder pass; hf:mys/laya-GGUF sha 713ae6f6e39f likes 0 apache-2.0; hf:mys/laya-multilingual-GGUF sha 3b645ae54281; hf:mys/laya-typed-decisions-GGUF sha 1e9e8ba1f527; hf:tozp/laya-onnx sha 0862aeba1e65 Opset 14 FP32 and INT8; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; docker-laya MIT HEAD 1b8239a51ddd README SHA 9cb7bdc3; laya.cpp RTX ggml CUDA HEAD 8590937c79a2 README SHA cdd429b9; serving substrate ≠ calibrated replica; Softmax over options ≠ calibrated Noul; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; jev-position-test n=6 HEAD 7a56ca1c2698 README SHA 23f194c9; jevmlx slots 5 of 6; hosted Jev 0 of 6; prior_correction made it worse; jevSweeper mean Spearman ρ −0.274; picked exact-optimal 1/25 (4%); 31 of 36 still logically decidable; 86% of the time we should not have been asking; game success ≠ calibrated Noul; LLM2Jev 64★ Apache-2.0 HEAD 924618721277 README SHA da35fe61; not affiliated with or endorsed by Jev or TypeSafe; No answer tokens are generated; OpenSourceJev llama.cpp Qwen3-1.7B HEAD 3c41fba3681d; JEV-MLX Qwen3.5-9B HEAD dec24cd929ea; decision-head-rlcd Qwen3.5-4B 4.9M LoRA; AUTO_ACT is not a Noul; closed-set fail-open stdlib-only; verified=False; soft scores ≠ hard gates; 22 to 40% cheaper *theirs*; first version 70% more expensive; 111-case benchmark *theirs*; CDC 5,000 Jev 72.2% AUC 0.7725 *theirs*; accuracy is a trap; 9.0% base rate always-no 91.0%; catalog ≠ endorsement; jev-skill 109★ 90 scenarios HEAD 4f6e899a24d4; awesome-jev-live 673 entries 4★; minecraft-agent 214★ 131 JEV decisions 35 Astra calls; nether-final-08 8 minutes 43.300 seconds; planner writes JEV selects; RoboJEV structured simulator state not images; ashare-trader 策略未通过自己的回测门槛; 36 组参数全部净期望为负; no positive expectation under real costs; typed_evals NOT an official TypeSafe AI product; jev-as-judge is a sensor; third-person-audit 40% & 60% watermarks still soft; The included experience uses a handwritten demo provider; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42; notes.md §120


**Hourly 1143 HIGH (`notes.md` §121).** open recreation ≠ calibrated replica. semantic lint is a sensor not a proof. cutoff 0.8 still soft. paired bootstrap CIs *theirs*. Same accuracy, 35x faster *theirs*. systems comparison ≠ semantic equivalence. serving substrate ≠ calibrated replica. catalog ≠ endorsement. permission ≠ confidence. Do not reopen or amend PR #23–#43. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1143 uniqueness lock: open recreation ≠ calibrated replica; Qwen3.5-4B ≠ Archer; It is an open re-creation of Jev; less calibrated; perch 164★ MIT HEAD ba775a9940b6 README SHA 7ad0403b; semantic lint is a sensor not a proof; oxlint-plugin-jev cutoff 0.8 still soft; nassim-arifette/jevgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; patdown fuzzy linter; PanAchy/jevvy ≠ Atominac/jevvy; No orders, no advice; SmartMoney-Cub 25★ HEAD d93cf493853d; paired bootstrap CIs *theirs*; emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; +0.82 pts XQuAD-EN 95% CI +0.35 to +1.31; +7.62 pts SciFact CI +4.88 to +10.38; Same accuracy, 35x faster *theirs*; systems comparison ≠ semantic equivalence; BANKING77 500 Jev 81.0% GPT-OSS 82.8% Mercury 73.2% Gemini 85.4% *theirs*; frozen cascade missed its evaluation accuracy target 430/500 vs GPT-5 432/500; This is not demonstrated equal-quality savings; 24 invented tickets; Routing errors caught by the gate 0 of 3; sample too small to establish calibration; This is not TypeSafe Jev; No real API requests were made; wire-compat ≠ replica; KonghaYao/laya-jev 按官方接口写的客户端只改一个 base URL; gqgs/laya-onnx densify 496.8 MiB; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; serving substrate ≠ calibrated replica; BeatAPI/awesome-jev ≠ 99hansling/awesome-jev ≠ Vishnurr2k01/awesome-jev ≠ robokrunch/awesome-jev ≠ rudy2steiner/awesome-jev-hub; All 125 projects; catalog ≠ endorsement; Pasblinn/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab ≠ q93304989-bit/jev-lab; Independent project. Not affiliated with TypeSafe; Kevthetech143/super-jev densify experimental V0.2.0; permission ≠ confidence; allay-team/openjev ≠ piyush-infocusp/openjev ≠ TheoLeeCJ/openjev; 2022 Mineflayer Jevalent collision; kushalpatil/jevify-gemma4-e4b GGUF densify; static quants; This dataset and model are independent research artifacts, not reproductions of Jev or RLCD; pngwn demo accuracy 0.705 ECE 0.046 ~112 ms *theirs*; cutoff 0.8 still soft; soft scores ≠ hard gates; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43; notes.md §121

**Hourly 1248 HIGH (`notes.md` §123).** decide is not generate. tryDecide returns typed calibrated judgments not a token stream. GLiNER/GLiClass ports are class members not Jev replicas. 93.5% *theirs* not Harbor. 74.9 *theirs* not Harbor. 8.7x *theirs* not Harbor. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#45. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1248 uniqueness lock: decide is not generate; tryDecide returns typed calibrated judgments not a token stream; juspay/neurolink 133★ MIT HEAD 268b0fe83130 README SHA e709cadfa6b6 tag v12.19.0; GLiNER/GLiClass ports are class members not Jev replicas; MacPaw/Gliner2Swift ≠ Knowledgator/GLiClass.c ≠ fbilhaut/gliclass-rs ≠ Knowledgator/GLiClass.js ≠ gravitee-io/GLiNER4j ≠ apiplant/gliner-rs ≠ codesoda/gliner2-rs; 8.7x faster 4.4x fewer prompts *theirs*; 153 was a reporting error; corrected 156-case 9.8x faster 4.2x fewer prompts *theirs*; independent v0.2.1 1.24x vs Mini *theirs*; Approvals only; anpicasso/hermes-jev-approvals ≠ hermes-switchyard; scx-router GLiClass ranks candidate LLMs in one non-generative pass; typesafeai-dotnet-sdk Not affiliated with TypeSafe AI; hyperspaceai/jevcache ≠ kushals256/jevcache; ST-jeved measures each reply; 400 plain-text for unaskable question; razorback16/openjev:0.2.1 Docker densify HEAD 794a81b87131; wire-compat ≠ logit-equiv; Option-Marker joint attention 93.5% macro *theirs*; 93.6% micro *theirs*; n=78; T = 1.0367 vs T = 1.1692 two temperatures; guaranteeing is soundness theater; wfzyx/von densify HEAD bed7e7337791; Benchmark Heaven leaderboard #2 74.9 *theirs*; NLL calibration assets; 77.10% still §71 claim-audit; do not re-fold as a beat; Heman10x-NGU/openJev-verdict-2.0 densify HEAD bff28567cff4; kev-family weight tarballs; PLAN_Qwen35 proposal for review; deadline 0.53→0.82 at 9B *theirs*; Qwen3.5-9B ≠ Archer; isolation would fail by construction on DeltaNet; jaredpalmer/kev densify; JevBench v1.2.2 jeff 66.9 (#9) jev 75.3 (#2) *theirs*; logan-markewich/jeff densify HEAD 34b32f99a727; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; TypeLLM/TypeLLM densify HEAD c4b03ba9e792; us/jev-local stub until hf; Eran-BA/Jev_from_GLiNER2 spec ≠ replica; lsu-ub-uu/systemone ≠ TypeSafe System One; Layan/Laya HF spaces name-match; catalog ≠ endorsement; decide ≠ generate ≠ stream; 93.5% *theirs* not Harbor; 74.9 *theirs* not Harbor; 8.7x *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45; notes.md §123

**Hourly 1340 HIGH (`notes.md` §124).** typesafe-sdk 0.7 Pydantic response models. msgspec dropped. MLX backend 400 plain-text error contract. Pydantic response models ≠ logit-equiv. msgspec dropped is not a replica. Error contract is not a Noul. PLAN_Qwen35 densify. coverage-at-error-budget *theirs* not Harbor. GLiNER locate ports are class members not Jev replicas. Locate ≠ decide. ~160 ms *theirs* not Harbor. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#46. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1340 uniqueness lock: typesafe-sdk 0.7 Pydantic response models; msgspec dropped; The server's output is unchanged and was never wrong; MLX backend 400 plain-text error contract; SchemaError is 400 plain-string detail not 422 list; razorback16/openjev densify HEAD 6e91dfc031bc README SHA cbdcc8de0304; Pydantic response models ≠ logit-equiv; msgspec dropped is not a replica; Error contract is not a Noul; wire-compat ≠ logit-equiv; PLAN_Qwen35 densify; corrected Qwen3.5 LoRA target names verified; in_proj_qkv in_proj_z in_proj_a in_proj_b out_proj; peft 0.21 existence proof; OOD-calibration study; coverage-at-error-budget metric in Phase 0; PLAN_Qwen35 still proposal for review; deadline 0.53→0.82 at 9B *theirs*; isolation would fail by construction on DeltaNet; Qwen3.5-9B ≠ Archer; jaredpalmer/kev densify HEAD 75cc15ddb8e2 PLAN SHA eca543246f50; GLiNER locate ports are class members not Jev replicas; urchade/GLiNER ≠ fbilhaut/gline-rs ≠ lmoe/gliner-onnx.js ≠ shershah1024/gliner-native-runtime; Locate ≠ decide; Jev-Vision skip 0.936 effect 0.967 done 0.896 157 ms *theirs*; ~160 ms *theirs* not Harbor; 0.971 F1 *theirs* not Harbor; coverage-at-error-budget *theirs* not Harbor; hf:fr0stbit3/laya-gguf serving substrate ≠ calibrated replica; jkcdarunday/SystemOne-Next ≠ TypeSafe System One; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46; notes.md §124

**Hourly 1441 HIGH (`notes.md` §125).** vLLM NVIDIA + MLX Apple Silicon. Codiv hosted free endpoint. dual /v1/systemone + /v1/chat/completions. chat 501 on MLX. dual serving is not generate. Hosted Codiv ≠ TypeSafe. candidate probabilities are relative not correctness. recommendation is advisory. the server never blocks on its own. LoRA ≠ RLCD replica. pass-min 0.8 still soft. 37.30s → 2.40s at 64 decisions *theirs*. 2B 94.71% 9B 97.54% hard test *theirs*. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#47. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1441 uniqueness lock: vLLM NVIDIA + MLX Apple Silicon; Codiv hosted free endpoint; dual /v1/systemone + /v1/chat/completions; razorback16/openjev densify HEAD cddbd962c88a README SHA a5943415cb92; STE README rewrite; serving-port densify; chat 501 on MLX; dual serving is not generate; Hosted Codiv ≠ TypeSafe; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; hr98w/jev-visual 167★ Apple Silicon visual candidate scoring; 37.30s → 2.40s at 64 decisions *theirs*; Breakout 9 bricks 6 returns 2 lives *theirs*; candidate probabilities are relative not correctness; jkudish/jev-mcp 156★ ten MCP tools; recommendation is advisory; the server never blocks on its own; TypeSafe CLERC 5% to 18% *theirs*; jkudish/jev-mcp ≠ burnigtm/jev-mcp; zhengxuyu/litjev off-the-shelf Qwen decision layer; Probabilities are not calibrated by default; Qwen/Qwen3.8-27B ≠ Archer; zhengxuyu/litjev ≠ alexwestco/llm-to-jev; Zefan-Cai/Open-Jev LoRA + scalar head; 2B 94.71% 9B 97.54% hard test *theirs*; 2B OOD 86.02% 9B OOD 91.97% *theirs*; 80,816 training rows; 27B still in progress; LoRA ≠ RLCD replica; Zefan-Cai/Open-Jev ≠ TheoLeeCJ/openjev ≠ razorback16/openjev; cristianoliveira/jeq intelligence you can pipe; pass-min 0.8 still soft; JEQ does not own actions; AndyInQtr/laya-coreai CoreML serving substrate ≠ calibrated replica; AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47; notes.md §125



## Treat openjev 0.3.0 as logit-equiv? Treat JMP as one model? Treat jevbus thresholds as the judge?

No. restructured vLLM head ≠ logit-equiv. MODEL_VERSION stays openjev-0.1.
dual serving is not generate. Hosted Codiv ≠ TypeSafe. Models participate.
Real tools execute. decide is not generate. Thresholds are policy not model.
documentation is read not judged. json-render is the only renderer.
game success ≠ calibrated Noul. catalog ≠ endorsement.
Do not reopen or amend PR #23–#49. `invented_signal: false`. `notes.md` §127.

## Treat TypeLLM thinking / 5.8x as a Noul? Treat kev 0.790 as Harbor? Treat 0.65 as a hard gate?

No. Constrained AR ≠ calibrated Noul. Batch 5.8x *theirs*. type safety does not guarantee factual accuracy. 4B new-source 0.790/0.806 *theirs*. 8.2% ≥0.9 on wrong *theirs*. option order can change an answer. JEV_THRESHOLD 0.65 still soft. routing ≠ permission. fail closed never auto-allows. fail-open uncertainty means RUN. classifier ≠ authorizer. estimates not Harbor. catalog ≠ endorsement. Do not reopen or amend PR #23–#48. `invented_signal: false`. `notes.md` §126.

**Hourly 1542 HIGH (`notes.md` §126).** TypeLLM README densify 3k→12k B. Batch 5.8x *theirs*. Constrained AR ≠ calibrated Noul. kev family densify. 4B new-source 0.790/0.806 *theirs*. 8.2% ≥0.9 on wrong *theirs*. option order can change an answer. fail-closed routing vs fail-open test selection. classifier ≠ authorizer. estimates not Harbor. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#48. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1542 uniqueness lock: TypeLLM/TypeLLM densify HEAD 6a48f9f1e623 README SHA dbdc1f193537; README densify 3k→12k B; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; Batch 5.8x *theirs*; Constrained AR ≠ calibrated Noul; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify HEAD b339f446a0ef README SHA 86b0a19909f3; Kev-0.6B 4B 8B family; 4B new-source 0.790/0.806 *theirs*; 8B new-source 0.796/0.780 *theirs*; Jev hosted 0.857 *theirs*; Questions share the input text but cannot read each other; No Jev outputs were used for training; 8.2% ≥0.9 on wrong *theirs*; option order can change an answer; Qwen3 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; TheoOliveira/pi-jev 21★ fail-closed routing; JEV_THRESHOLD 0.65 still soft; routing ≠ permission; harshwasan/jev-sentinel fail closed never auto-allows; harshwasan/jev-sentinel ≠ leepokai/jev-guard; jackbarunz/jev-tool-router ≠ esinocchi/jev-tool-router; threshold 0.90 still soft; 76/81 vs 77/81 *theirs*; 0.419s vs 2.459s *theirs*; $0.00486 vs $0.03673 *theirs*; does not execute; not a security boundary; baronunread/leanest fail-open uncertainty means RUN; classifier.dev default Jev/Laya pluggable; openlayer-ai/jevals ≠ dayhaysoos/jevals; estimates not Harbor; classifier ≠ authorizer; MrJev/awesome-jev 118 entries catalog ≠ endorsement; MrJev/awesome-jev ≠ yibie/awesome-jev; Koushik890/jev-firewall fail closed ask_below 0.7 still soft; CompleteTech-LLC-AI-Research/jev-codex-approval experimental native not compiled; confidence is not a measured probability; rh-guard owns primary gates; hf:rAVEUK/open-jev-deberta-v3-large encoder class member not Jev replica; hf:p-yan/laya-quanto serving substrate ≠ calibrated replica; hf:Gtrkrsk/laya serving substrate ≠ calibrated replica; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48; notes.md §126
**Hourly 1643 HIGH (`notes.md` §127).** openjev release 0.3.0 densify. re-pin vLLM PR #57250 restructured head. restructured vLLM head ≠ logit-equiv. MODEL_VERSION stays openjev-0.1. dual serving is not generate. Hosted Codiv ≠ TypeSafe. typed judgments not opinions. Thresholds are policy not model. Jev never generates prose JSX or code. game success ≠ calibrated Noul. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#49. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1643 uniqueness lock: razorback16/openjev densify HEAD febf02e88989 README SHA 242a737dba01; release 0.3.0; re-pin vLLM PR #57250 restructured head; VLLM_COMMIT baa8338; pyproject and __init__ agree 0.3.0; MODEL_VERSION stays openjev-0.1; uv.lock hygiene; dual serving is not generate; Hosted Codiv ≠ TypeSafe; restructured vLLM head ≠ logit-equiv; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; frostney/clean-code-review 7★ typed judgments not opinions; documentation is read not judged; Luna writes from Jev findings; morcoan/JMP Joint Model Participation; Models participate. Real tools execute.; Jev routes actions generators supply arguments; not a swarm; zkjoie/jevbus Thresholds are policy not model; Drop < Review < Deliver; FanOut or Exclusive; Kelbie/hunch ≠ carldaws/hunch ≠ tpellet/hunch ≠ huncho; Agent Skills semantic review; SupratikB23/JevCanvas Jev never generates prose JSX or code; Diffusion never decides structure; json-render is the only renderer; skcache/jevtrafficsim Fixed Adaptive Jev; game success ≠ calibrated Noul; Shalimov04/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev; MstyAI/laya-onnx empty repo ≠ tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; SherifAshraf2003/jev-use ≠ shitianfang/jev-use; aniruddh-krovvidi/switchboard ≠ cannacre8ive/switchboard-ai; Visorian/TidyUp ≠ abhibansal60/tidy; isiomaC/jevkit ≠ WaynezProg/jev-kit; lee-lou2/jev-tree ≠ reachjalil/jev-tree; Royhu1/jev-poker-trainer empty repo; JoacoMarc/jev-harness-router ≠ jackbarunz/jev-tool-router; rh-guard owns primary gates; hf:Praveenrajus/jev-bench HTTP 200 was 401; hf:ZefanCai/Open-Jev densify dataset; LoRA ≠ RLCD replica; hf:emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; hf:ctaxnagomi/DGUI_HYPERMEM-JEV densify sha ab3d3529; hf:hugging-apps/open-jev-deberta-v3-large-demo encoder class member not Jev replica; serving substrate ≠ calibrated replica; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49; notes.md §127

## Treat truncated thinking as a Noul? Treat 0.812 as Harbor? Treat Jev as a done-block?

No. truncated thinking then constrained decode. Constrained AR ≠ calibrated Noul.
type-valid ≠ exact. 0.8B thinking On 0/18 *theirs*. forced closure 20/20 type-valid *theirs*.
Kev-0.8B completes family. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*.
Qwen3.5 ≠ Archer. Facts go to code. Judgments go to Jev. Only facts can block.
Jev never blocks. five-lines threshold 0.80 still soft. 155/155 argmax *theirs*.
serving substrate ≠ calibrated replica. catalog ≠ endorsement.
jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev.
tpellet/jevify ≠ altryne/jevify. seb4ez/jevguard-mcp ≠ seb4ez/jevguard.
resumocast/jev-mcp ≠ jkudish/jev-mcp. Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort.
MidasMulli/kev-ane ≠ jaredpalmer/kev. routing ≠ permission.
Do not reopen or amend PR #23–#50. `invented_signal: false`. `notes.md` §128.

**Hourly 1746 HIGH (`notes.md` §128).** TypeLLM truncated thinking densify. 0.8B thinking On 0/18 *theirs*. forced closure 20/20 type-valid *theirs*. Constrained AR ≠ calibrated Noul. Kev-0.8B completes family. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. transfer-v9 5%/9%/26% *theirs*. Facts go to code. Judgments go to Jev. Only facts can block. Jev never blocks. five-lines threshold 0.80 still soft. 155/155 argmax *theirs*. Qwen3.5 ≠ Archer. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#50. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1746 uniqueness lock: TypeLLM/TypeLLM densify HEAD 702e6a287f3c README SHA 08180db0450b; truncated thinking then constrained decode; typellm_runtime.py typellm_sglang.py; evals/qwen35_small; 0.8B thinking On 0/18 *theirs*; forced closure 20/20 type-valid *theirs*; Constrained AR ≠ calibrated Noul; type safety does not guarantee factual accuracy; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify live HEAD 8465c4c4c294 watch 38087aa0301d README SHA 19664b9ae546; Kev-0.8B completes family; Kev-0.8B 4B 9B Qwen3.5; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*; SemIf Kev-9B 0.917 Jev 0.965 *theirs*; scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*; transformers >= 5.17; Qwen3.5 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; notque/vexjoy-agent 421★ /d routes /do fallback; tamaratran/jev-pruner densify HEAD 47d017c34eab; qkal/Canny Facts go to code. Judgments go to Jev. Only facts can block.; Jev never blocks; jqueryscript/awesome-jev 231 entries catalog ≠ endorsement; jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; jamescazzetta/five-lines threshold 0.80 still soft; eugeniughelbur/jev-engineering 371ms $0.0000189 300-call *theirs*; tpellet/jevify ≠ altryne/jevify; seb4ez/jevguard-mcp ≠ seb4ez/jevguard; resumocast/jev-mcp ≠ jkudish/jev-mcp; dtduc-git/jev-table first sighting; Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort; MidasMulli/kev-ane 155/155 argmax *theirs*; MidasMulli/kev-ane ≠ jaredpalmer/kev; serving substrate ≠ calibrated replica; empty repo skip-thin; loktar00/llm-lan-party empty repo; rh-guard owns primary gates; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50; notes.md §128

## Treat kev --init_from as from-scratch? Treat JSONL as Harbor? Treat kyegomez as a replica?

No. from-scratch ≠ warm-start. JSONL labels ≠ Harbor. reconstruction ≠ replica.
unofficial research implementation with random weights. assay-001 split verdict.
catalog ≠ endorsement. game success ≠ calibrated Noul.
Do not reopen or amend PR #23–#51.
`invented_signal: false`. `notes.md` §129.



## Treat MLX text gen as a Noul? Treat Release v0.1.1 as calibration? Treat n=8 as Harbor?

No. dual serving is not generate. Hosted Codiv ≠ TypeSafe.
wire-compat ≠ logit-equiv. Constrained AR ≠ calibrated Noul.
PyPI packaging ≠ calibrated Noul. GitHub Release v0.1.1 is distribution.
n=8 is not Harbor. option order can change an answer.
WANLI-256 74.6% *theirs*. jevtok 0 mismatches *theirs* not Harbor.
ockev 35ms 95.8% TomatoEggBench *theirs* not Harbor.
Cua-S1 ≠ TypeSafe. catalog ≠ endorsement.
Do not reopen or amend PR #23–#58.
`invented_signal: false`. `notes.md` §135.

## Treat TREC prep as completed nDCG? Treat a PyPI wheel as a Noul? Treat logits as P(correct)?

No. TREC prep ≠ completed Open-Jev TREC. context proof ≠ nDCG.
CPU tests ≠ GPU scores. PyPI packaging ≠ calibrated Noul.
Constrained AR ≠ calibrated Noul.
logits are not calibrated probabilities of correctness.
wire-compat ≠ logit-equiv. catalog ≠ endorsement.
Do not reopen or amend PR #23–#57.
`invented_signal: false`. `notes.md` §134.

## Treat a CPU-passing provider eval as GPU scores? Treat CartPole as hosted Jev? Treat QMT as live orders?

No. provider pipeline ≠ completed Open-Jev quality. CPU tests ≠ GPU scores.
fine-tuned Kev ≠ TypeSafe Jev. one record of 64. softmax ≠ calibrated Noul.
QMT mock/dry default no orders. does not execute. cutoff 95% still soft.
option order can change an answer. catalog ≠ endorsement.
3.69ms *theirs* not Harbor. 80.1% *theirs* not gold.
Do not reopen or amend PR #23–#56.
`invented_signal: false`. `notes.md` §133.

## Treat Open-Jev 85 ms as Jev parity? Treat 94.71% as a Noul? Treat LoRA as RLCD?

No. systems latency ≠ semantic equivalence. hard acc ≠ calibrated Noul.
not merged base models. LoRA ≠ RLCD replica. type-valid ≠ exact.
customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms *theirs*.
1024 tokens/32 candidates Open-Jev slower 1015.90 vs 301.37 *theirs*.
prefix caching experimental/off by default. TREC-DL Jev/Luna/Astra completed.
Open-Jev TREC pending. Qwen/Qwen3.8-27B ≠ Archer.
Zefan-Cai/Open-Jev ≠ TheoLeeCJ/openjev ≠ razorback16/openjev.
Do not reopen or amend PR #23–#52.
`invented_signal: false`. `notes.md` §125.

**Hourly 1843 HIGH (`notes.md` §129).** kev own-data JSONL densify. --init_from warm-start LoRA/head PR #9. from-scratch ≠ warm-start. JSONL labels ≠ Harbor. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. 0.33 vs 0.84 vs 0.83/0.88 *theirs*. reconstruction ≠ replica. assay-001 split verdict. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#51. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1843 uniqueness lock: jaredpalmer/kev densify HEAD bd058057ad0a README SHA 84b872488915; Fine-tuning on your own data; --data JSONL; --init_from warm-start LoRA/head PR #9; Kev-0.8B 4B 9B Qwen3.5 family; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; 0.33 vs 0.84 vs 0.83/0.88 *theirs*; from-scratch ≠ warm-start; JSONL labels ≠ Harbor; Kev-0.5B card Qwen3.5 family pointer; No Jev outputs were used for training; option order can change an answer; 8.2% ≥0.9 on wrong *theirs*; Kev-9B 7.5% ≥0.9 on wrong *theirs*; dabit3/jev-experiments densify 340★; simota/tenbin densify neighbor skill; Promethe-us/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; kyegomez/open-jev reconstruction ≠ replica; unofficial research implementation with random weights; kyegomez/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev ≠ Shalimov04/open-jev; jourdanlabs/assay-001 split verdict; CLINC150 ECE 0.0204 *theirs*; Banking77 ECE 0.0936 *theirs*; 8,576 responses zero type errors *theirs*; brnyxx/jev-ra 3-5x / ~300 ms *theirs*; 8.50× Wikipedia *theirs*; ThePFMind/jev-mcp ≠ jkudish/jev-mcp ≠ burnigtm/jev-mcp; namenu/pi-jev-effort ≠ TheoOliveira/pi-jev; samatv256/mini-Jev ≠ r-ms/mini-jev; comoc/jev-minesweeper ≠ EnesYilmazcode/JevMinesweeper; game success ≠ calibrated Noul; Nutlope/jev-fraud Kimi K3; jeffloo886/jev-notion; hf:akhilaaa3/openjev-v1-allmix-r512-merged ≠ hf:akhilaaa3/openjev-r512-handoff-demo; serving substrate ≠ calibrated replica; catalog ≠ endorsement; SHA move is not a replica; wire-compat ≠ logit-equiv; Qwen3.5 ≠ Archer; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51; notes.md §129


## Treat TypeSafe-compatible as a replica? Treat 76.7% as Harbor? Treat kotoba as Laya HF?

No. TypeSafe-compatible ≠ TypeSafe replica. replica ≠ TypeSafe.
76.7% vs Jev 86.9% *theirs*. DeBERTa-v3-large 0.855 / 42 ms *theirs*.
kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions.
aisearchio 15-link census catalog ≠ endorsement. soft scores ≠ hard gates.
Do not reopen or amend PR #23–#52.
`invented_signal: false`. `notes.md` §130.

**User-provided 1936 HIGH (`notes.md` §130).** sgoedecke/system-one first-sighting. SystemOne.from_pretrained. TypeSafe-compatible ≠ TypeSafe replica. mithalouni/system-one-open first-sighting. 76.7% vs Jev 86.9% *theirs*. replica ≠ TypeSafe. kotoba-lang/typed-decisions first-sighting. DeBERTa-v3-large 0.855 / 42 ms *theirs*. kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions. aisearchio 15-link census catalog ≠ endorsement. soft scores ≠ hard gates. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided 1936 uniqueness lock: sgoedecke/system-one 20★ HEAD ebde2a2db706 README SHA d331b567e2c3; SystemOne.from_pretrained; Batched single-token choice inference; TypeSafe-compatible; cache_prefix=True; LICENSE absent; sgoedecke/system-one ≠ mithalouni/system-one-open ≠ KathanModh259/system-one ≠ babybear-labs/system-one; TypeSafe-compatible ≠ TypeSafe replica; mithalouni/system-one-open 18★ MIT HEAD 77f1f7cccf8a README SHA 535f33028a68 LICENSE SHA 2f6f2cf1064e; Gemma 4 E2B / Gemma 3 270M Modal; 76.7% vs Jev 86.9% strict common subset *theirs*; 97 ms H100 *theirs*; 74.8% held-out *theirs*; replica ≠ TypeSafe; HF upload pending; kotoba-lang/typed-decisions 1★ Apache-2.0 HEAD 10d7834d3b99 README SHA 4d6bbf4c4e44 LICENSE SHA 513bb5e3cb4c; ModernBERT / DeBERTa / LLaDA-MoE; DeBERTa-v3-large 0.855 / 42 ms *theirs*; ModernBERT-base 0.717 / 68 ms *theirs*; LLaDA-MoE 0.835 / 676 ms *theirs*; kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions; encoder class member not Jev replica; aisearchio 15-link census catalog ≠ endorsement; 12 already carded 3 gaps this fold; soft scores ≠ hard gates; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §130
**Open-Jev densify (`notes.md` §125).** DENSIFY the original 1441 card, not a sibling first sighting. HEAD 4933ee84951f README SHA ce1a587219e4. LoRA + scalar head + calibration temperature. not merged base models. customer-service P50 85.03 vs Jev 295.26 *theirs*. 1024/32 slower 1015.90 vs 301.37 *theirs*. systems latency ≠ semantic equivalence. Open-Jev TREC pending. hard acc ≠ calibrated Noul. type-valid ≠ exact. LoRA ≠ RLCD replica. Qwen/Qwen3.8-27B ≠ Archer. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided Open-Jev densify uniqueness lock: Zefan-Cai/Open-Jev densify HEAD 4933ee84951f README SHA ce1a587219e4; pushed 2026-09-21T01:34Z; Astra TREC commit 1dd56990be7e pushed 2026-09-21T01:17Z; live 3★ (was 0★; star-noise is not the fold); LoRA adapters plus trained scalar decision head and calibration temperature; not merged base models; dataset ZefanCai/Open-Jev rev c67699e13d0a; Open-Jev-2B rev 0c7aa498b162; Open-Jev-9B rev 47e966881e48; 27B still in progress; Independent of TypeSafe; no RLCD/parity claims; LoRA ≠ RLCD replica; customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms *theirs*; 1024 tokens/32 candidates Open-Jev slower 1015.90 vs 301.37 *theirs*; prefix caching experimental/off by default; CUDA prefix caching exceeded tolerance on 9/11 workloads; systems latency ≠ semantic equivalence; GPT Luna P50 918.13 ms Astra 1938.39 ms *theirs*; TREC-DL Jev/Luna/Astra completed; Open-Jev TREC pending; 80,816 training rows; 2B 94.71% / OOD 86.02%; 9B 97.54% / 91.97% *theirs* not Harbor; hard acc ≠ calibrated Noul; type-valid ≠ exact; Qwen/Qwen3.8-27B ≠ Archer; website https://zefan-cai.github.io/open-jev/; launch X thread https://x.com/Zefan_Cai/status/2101782158658695388 https://x.com/Zefan_Cai/status/2101786019607740436 https://x.com/Zefan_Cai/status/2101789698947793231; densify §125 not a sibling first sighting; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §125
**Hourly 1946 HIGH (`notes.md` §131).** X-sentiment does not execute trades. heyjunpenn/awesome-jev 485 catalog ≠ endorsement. jev-arena 62.69% vs 67.26% *theirs* not gold. 203.2s $0.84 vs 823.5s $1.50 *theirs*. one seed-0 trial *theirs*. Jev $0.018825 vs Astra $5.93 *theirs*. 10.59× *theirs*. 6 class flips. agreement ≠ accuracy. probabilities uncalibrated. Qwen3.8 ≠ Archer. Spanish −6.4 pp XNLI *theirs*. ECE 0.057→0.101 *theirs*. 72.2% vs 63.4% p_max≥0.9 coverage *theirs*. llm-to-jev description rewrite Convert LLM prompts to Jev prompts. SHA unchanged 234058ab372d. 3★. heuristic conversion ≠ calibrated Noul. skip Zefan-Cai/Open-Jev densify open #53. skip #54 three. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1946 uniqueness lock: brainstormity/Jev-X-Sentiment-Analysis 136★ HEAD 5c932f941a92 README SHA bf4134b44cda; platform does not execute trades; heyjunpenn/awesome-jev 485 catalog ≠ endorsement; heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev ≠ ckaraca/awesome-jev ≠ yzfly/awesome-jev-zh ≠ shirenchuang/awsomejev ≠ andyrewlee/awesome-system-one; NanmiCoder/jev-arena 10k comments 62.69% vs 67.26% *theirs* not gold; 203.2s $0.84 vs 823.5s $1.50 *theirs*; AI-reviewed labels ≠ gold; openroboto-ai/jev-robot-control one seed-0 trial *theirs*; Jev $0.018825 vs Astra $5.93 *theirs*; one-trial robot ≠ Harbor; endman100/research-Qwen3.8-JevLike 10.59× *theirs*; 6 class flips; agreement ≠ accuracy; probabilities uncalibrated; Qwen3.8 ≠ Archer; 10.59× systems ≠ ECE; marcosmartinez/jev-acento Spanish −6.4 pp XNLI *theirs*; ECE 0.057→0.101 *theirs*; 72.2% vs 63.4% p_max≥0.9 coverage *theirs*; alexwestco/llm-to-jev description rewrite Convert LLM prompts to Jev prompts; SHA unchanged 234058ab372d; 3★; heuristic conversion ≠ calibrated Noul; desc rewrite ≠ SHA/behavior change; skip Zefan-Cai/Open-Jev densify open #53; skip sgoedecke/system-one mithalouni/system-one-open kotoba-lang/typed-decisions open #54; ikermoel/open-alternative-jev already §49; nrdz-labs/fast-jev-opencode already §62; mallahyari/system-one-benchmark already §61; does not execute; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; local_only ≠ Jev; rule-table ≠ model; replica ≠ TypeSafe; arunav25/jev-mcp ≠ jkudish/jev-mcp ≠ ThePFMind/jev-mcp ≠ burnigtm/jev-mcp; luckberonne/mini-jev ≠ r-ms/mini-jev ≠ samatv256/mini-Jev; Kwwwww74/OpenJev ≠ razorback16/openjev ≠ kyegomez/open-jev ≠ Zefan-Cai/Open-Jev; peach-zhang/typesafe-go ≠ kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go; laidick/system-one-benchmark ≠ mallahyari/system-one-benchmark; sahasrarjn/system-one ≠ sgoedecke/system-one; aboisvert/jevvy ≠ PanAchy/jevvy; andrest04/jev-lab ≠ javsanesq/jevlab; twilwa/pi-typesafe ≠ TheoOliveira/pi-jev; RuipuCui/jev-harness ≠ ismaelsoilet/jev-harness ≠ AntonioCoppe/jev-harness; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §131
Hourly 2049 uniqueness lock: jaredpalmer/kev densify HEAD c096660c8da2 PLAN SHA 8d77dd271c66 README SHA unchanged 84b872488915; night-2 dates/unknowable/assertion; KEV_TEMPERATURE T≈2.0; Brier 0.291→0.267 ECE 0.105→0.039 *theirs*; 7.5%→3.2% *theirs*; grouped T rejected; Qwen3.6-35B-A3B smoke 0.812 *theirs*; 21M LoRA experts frozen; Hub --revision night2-du; MMLU-Pro 1000 Kev-9B 0.511 Jev 0.829 *theirs*; Qwen3.6 ≠ Archer; temperature scaling ≠ ECE unless measured; kotoba-lang/typed-decisions densify HEAD ff7f84e74d04 README SHA unchanged 4d6bbf4c4e44; feat expose trained OpenJev decision runtime; open_jev.py; tests/test_open_jev.py; generated_text: False; trained runtime ≠ TypeSafe; OpenJev.from_pretrained; decide_request kind typed-decisions/open-jev-v1; daftAI2026/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev; danielamitay/swev CoreML; serving substrate ≠ calibrated replica; smlayero/jev-debtgate CI gate cutoff still soft; Octalab-Inc/jqv stock Qwen3 decision API; franckverrot/lev ≠ jaredpalmer/kev; neko233-com/laya-go ≠ convaiinnovations/laya; tryAGI/TypeSafeAI ≠ official; abgregs/jev-experiments ≠ nak1b/jev-experiments ≠ dabit3/jev-experiments; jaanavit/gliner2-skill Locate ≠ decide; prasanthj/duckdb-jev SQL predicates; hf:Nebulaw1 legal LoRA ≠ RLCD replica; Qwen3.5 ≠ Archer; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; skip-thin KadePrice123/jev-state-tracking hideri777/jev-application-sample; Hub --revision is a pin not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55; notes.md §132

**Hourly 2146 HIGH (`notes.md` §133).** Open-Jev provider quality densify HEAD a00559ea0ab2. README SHA unchanged ce1a587219e4. provider pipeline ≠ completed Open-Jev quality. CPU tests ≠ GPU scores. 65/76 72/76 66/76 60/76 71/76 *theirs*. Open-Jev TREC pending. cartpole Kev flip HEAD 922cc61490a0. fine-tuned Kev ≠ TypeSafe Jev. one record of 64. 81.25% 52/64 *theirs*. softmax ≠ calibrated Noul. ashare rewrite HEAD 26c7e95e6828. QMT mock/dry default no orders. AUC 0.532 *theirs*. does not execute. kevin Playwright + Onyx first card. 3.69ms *theirs* not Harbor. metask-jev-4b 79.6% / 80.1% *theirs*. cutoff 95% still soft. option order can change an answer. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#56. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2146 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD a00559ea0ab2 README SHA unchanged ce1a587219e4; Publish prepared Open-Jev provider quality evaluation pipeline; 808 requests 1841 labelled decisions per model; Open-Jev GPU inference has not started; 48 CPU tests pass; Open-Jev TREC pending; 65/76 72/76 66/76 60/76 71/76 *theirs*; 117/140 109/140 135/140 *theirs*; JF100 232/300 227/300 300/300 *theirs*; FizzBuzz 299/300 300/300 300/300 *theirs*; mailroom 908/921 900/921 913/921 *theirs*; Jev TREC DL19/DL20 nDCG@10 0.275836/0.190667 strict *theirs*; Luna 0.729911/0.702082 *theirs*; Astra 0.736610/0.714484 *theirs*; provider pipeline ≠ completed Open-Jev quality; CPU tests ≠ GPU scores; tinmanlab/cartpole-jev densify HEAD 922cc61490a0 README SHA 0860958714f3; Active model Kev Not TypeSafe Jev; 81.25% 52/64 *theirs*; one record of 64; fine-tuned Kev ≠ TypeSafe Jev; softmax ≠ calibrated Noul; xuboboo/ashare-trader densify HEAD 26c7e95e6828 README SHA 7a860bdfa97b; premarket + intradaily; local probability model; QMT sidecar mock/dry default no orders; AUC 0.532 *theirs*; 36 组参数全部净期望为负; does not execute; gauravsaini/kevin first card Playwright + Onyx; Laya/Kev friends *theirs*; 3.69ms *theirs* not Harbor; metask-jev-4b 79.6% / 80.1% *theirs*; Bespoke Nimble-9B 74.8% / 63.5; Jev 76.0% / 75.3; lumen mixture-of-LoRA conformal; ardada2468/typedecide ≠ shkumbinhasani/typedecide; 87 of 144 order-unstable *theirs*; bonsai 192/231 ECE 0.037 *theirs*; 8GB; vercel-labs 95% Luna fallback; cutoff 95% still soft; tinmanlab/jev-qwen3.8-27b Qwen3.8 ≠ Archer; train-your-first-jev Qwen2.5-0.5B LoRA; sankaku-tech/jev-kit ≠ WaynezProg/jev-kit ≠ isiomaC/jevkit; jevfish DecisionScore 78.24 *theirs*; Typed Decision Bench 5387; reflex-gate CoT GBNF ≠ Noul; skip-thin IOCArena laya-mirror empty SHA; snsk JP 97.6 vs 36.9 *theirs*; yunhe-dev/awesomejev catalog ≠ endorsement; yunhe-dev/awesomejev ≠ heyjunpenn/awesome-jev ≠ daftAI2026/awesome-jev; wayfind/metask-jev ≠ metask-ai/metask-jev; mjyoke1111/jev-lab already §106; mizchi/jev-playground 19★; KaLM-Jev reranker ≠ Jev replica; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56; notes.md §133
**Hourly 2246 HIGH (`notes.md` §134).** Open-Jev TREC densify HEAD 48346d0630f1. README SHA unchanged ce1a587219e4. TREC prep ≠ completed Open-Jev TREC. context proof ≠ nDCG. CPU tests ≠ GPU scores. 79 CPU tests *theirs*. Open-Jev TREC pending. TypeLLM PyPI densify HEAD 8a8b4aefd443. typellm 0.1.1. PyPI packaging ≠ calibrated Noul. Constrained AR ≠ calibrated Noul. simple-jev 408★ first card. logits are not calibrated probabilities of correctness. wire-compat ≠ logit-equiv. jev-directory catalog ≠ endorsement. Jev-Mem 11.0% 6.6× 36.7% *theirs* not Harbor. FogMoe/necro abandoned LoRA retrospective. serving substrate ≠ calibrated replica. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#57. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2246 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD 48346d0630f1 README SHA unchanged ce1a587219e4; Publish strict Open-Jev TREC evaluation preparation and context proof; Actual Open-Jev TREC model inference is pending; All 79 combined CPU tests pass; 97 queries 43 DL19 54 DL20; at most 873 requests per model; No GPU or model inference was used; TREC prep ≠ completed Open-Jev TREC; context proof ≠ nDCG; CPU tests ≠ GPU scores; Open-Jev TREC pending; TypeLLM/TypeLLM densify HEAD 8a8b4aefd443 README SHA 9f6dea3a4c8c; Add PyPI packaging and publish workflow; typellm 0.1.1; Drop fixed banner height so it scales on PyPI; Constrained AR ≠ calibrated Noul; PyPI packaging ≠ calibrated Noul; type safety does not guarantee factual accuracy; featherless-ai/simple-jev 408★ HEAD b02aa81c915a README SHA 4c5be59e9738; logits are not calibrated probabilities of correctness; does not reproduce TypeSafe; /v1/systemone alias of /v1/classifier; wire-compat ≠ logit-equiv; everyai-com/jev-directory 13★ 50 runnable evals 1300+ builds catalog ≠ endorsement; Jev-Mem 11.0% 6.6× 36.7% *theirs* not Harbor; Nyarlathoteppppp/pi-jev-context ≠ kevinpita/pi-jev-context; FogMoe/necro abandoned LoRA retrospective; LoRA ≠ RLCD replica; Qwen3.5-0.8B ≠ Archer; clarity-judge independent community project; hearim Jev-compatible Go gateway; yijunyu/jev-rs any LLM one prefill; alongL/openJev ≠ Zefan-Cai/Open-Jev; huaizuo2022/jev-ultrafast ≠ browser-use/jev-ultrafast; FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; serving substrate ≠ calibrated replica; wayfind/metask-jev-4b-policy-mix ≠ metask-ai/metask-jev; majiayu000/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; rajasekharponakala/jev-mcp ≠ thedv91/jev-mcp ≠ jkudish/jev-mcp; skip-thin jev-droid 404 mach empty SHA; game success ≠ calibrated Noul; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57; notes.md §134
**Hourly 2347 HIGH (`notes.md` §135).** openjev MLX densify HEAD 2050fdb8280d. README SHA d5322e16e565. MLX backend steps>1/think/text gen + image Qs. dual serving is not generate. Hosted Codiv ≠ TypeSafe. wire-compat ≠ logit-equiv. TypeLLM Release v0.1.1 densify HEAD 8a8b4aefd443. README SHA unchanged 9f6dea3a4c8c. GitHub Release v0.1.1. Constrained AR ≠ calibrated Noul. PyPI packaging ≠ calibrated Noul. JevLoop 6★ independent not affiliated. WANLI-256 74.6% *theirs*. option order 0.188 or 0.542 *theirs*. jevtok 0 mismatches *theirs* not Harbor. ockev 35ms 95.8% TomatoEggBench *theirs* not Harbor. n=8 is not Harbor. serving substrate ≠ calibrated replica. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#58. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2347 uniqueness lock: razorback16/openjev densify HEAD 2050fdb8280d README SHA d5322e16e565; MLX backend steps>1/think/text gen + image Qs; dual serving is not generate; Hosted Codiv ≠ TypeSafe; wire-compat ≠ logit-equiv; SHA move is not a replica; TypeLLM/TypeLLM densify HEAD 8a8b4aefd443 README SHA unchanged 9f6dea3a4c8c; GitHub Release v0.1.1; Drop fixed banner height so it scales on PyPI; Constrained AR ≠ calibrated Noul; PyPI packaging ≠ calibrated Noul; type safety does not guarantee factual accuracy; zjunlp/JevLoop 6★ independent not affiliated; NicolaiLassen/open-bonsai-jev ≠ NicolaiMTLassen/open-bonzi-jev; WANLI-256 74.6% *theirs*; danielhirt/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ mjyoke1111/jev-lab; option order 0.188 or 0.542 *theirs*; novaleolin/jev-evolve; option order can change an answer; LabGuy94/jevtok 0 mismatches *theirs* not Harbor; ockev 35ms 95.8% TomatoEggBench *theirs* not Harbor; structured-decision-bench n=8 *theirs*; n=8 is not Harbor; Yang-SS-stack/jev-computer-use ≠ Mrchen116/jev-computer-use; amoreX/jevvy ≠ PanAchy/jevvy ≠ aboisvert/jevvy; smile-magic/laya-mlx-ddz ≠ smile-magic/laya-mlx-wzq; sriramkasyap/laya-api wire-compat ≠ logit-equiv; hf:space:Yuki131/KaLM-Jev ≠ KaLM-Embedding/KaLM-Jev; KaLM-Jev reranker ≠ Jev replica; hf:soyelmismo/laya-multilingual-onnx serving substrate ≠ calibrated replica; ranking before lossless condensation; llm-routing-jiv does not execute; jev-page-checker advisory does not block; 1deat0r/Jcua Cua-S1 ≠ TypeSafe; Jev-Register-Tool catalog only; nexibeo/jev-cookbook already carded; leesk212/JEV-CPU already carded; kazuhideoki/jev-search already carded; skip-thin layacm empty SHA; game success ≠ calibrated Noul; does not execute; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58; notes.md §135
**Hourly 0049 HIGH (`notes.md` §136).** Open-Jev JevBench public-subset densify HEAD f46ff604f794. README SHA e32c4bbd519c. public-subset ≠ Harbor. 231 ≠ 534. kev night-2 35B densify HEAD e0bcf50153f1. README SHA unchanged 84b872488915. PLAN correct 35B MMLU-Pro (0.550). evaluate.load honour weights_dtype=bf16. 5-10× *theirs* not Harbor. fail-open routing ≠ permission. ordered routing ≠ end-to-end. softmax next-token ≠ calibrated Noul. potential_match ≠ hiring decision. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#59. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 0049 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD f46ff604f794 via afb5226982c7 README SHA e32c4bbd519c was ce1a587219e4; Publish audited JevBench public-subset baselines; community benchmark plan; diverse hard-data pipeline New model gains have not been measured; 231 public tasks 72 original 48 easy 111 hard; full 534 303 private unavailable; do not report full-534; 2B 150/231 64.94% 9B 179/231 77.49% Jev 200/231 86.58% Luna 206/231 89.18% Astra 231/231 100.00% *theirs*; Brier 0.4751 0.3219 0.1811 0.2074 0.0085 *theirs*; ECE 0.1274 0.0858 0.0318 0.0932 0.0149 *theirs*; P50 138.0 189.2 291.3 953.8 2206.4 ms *theirs*; candidate order 119 of 139 Choice; native vs verbalized; public-subset ≠ Harbor; 231 ≠ 534; Open-Jev TREC pending; 27B training not complete; LoRA ≠ RLCD replica; Qwen3.5-2B ≠ Archer; Qwen3.5-9B ≠ Archer; densify §125 not a sibling first sighting; jaredpalmer/kev densify HEAD e0bcf50153f1 README SHA unchanged 84b872488915; PLAN correct 35B MMLU-Pro (0.550); evaluate.load honour weights_dtype=bf16; Kev Qwen3.6-35B-A3B MMLU-Pro 0.550 Kev-9B 0.545 Jev 0.840 *theirs*; Not shipped; Qwen3.6 ≠ Archer; Hub --revision is a pin not a replica; wy-coliney/jev-browser-use 282★ 5-10× *theirs* not Harbor; Jev clicks Codex thinks and verifies; wy-coliney/jev-browser-use ≠ browser-use/jev-ultrafast ≠ Mrlyk/jev-browser ≠ akras14/jevbro; gargpratyush/jev-router 270★ first card fail-open routing ≠ permission; 33Audits/jev-auto ≠ gargpratyush/jev-router; BillionsBobby/JevRouter 124★ 38% 44% vs 24% *theirs* not Harbor; ordered routing ≠ end-to-end; BillionsBobby/JevRouter ≠ gargpratyush/jev-router; daseinlabs/open-jev 75★ Gemma 3 4B MLX; softmax next-token ≠ calibrated Noul; head 0.970 ECE 0.027 *theirs*; shuffled-context 0.258; daseinlabs/open-jev ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev ≠ zhlei07/openjev; skeptrunedev/jev-recruiter potential_match ≠ hiring decision; abhixhek/jevcal threshold on held-out; simulator not a Jev bench; fail-closed without fallback; AntonioCoppe/jev-harness already carded; akash-kamat/system-one-gemma 64.4% ECE 0.047 *theirs*; 200x *theirs* not Harbor; Premo-Cloud/typesafe-sdk-java unofficial; AgentBuff/awesome-jev catalog ≠ endorsement; AgentBuff/awesome-jev ≠ yibie/awesome-jev ≠ heyjunpenn/awesome-jev; Alpha-Harper-Franklin/jev-drive ≠ VennIntelligence/jev-drive; skip-thin zhlei07/openjev empty SHA khmuhtadin/n8n-nodes-jev-classification empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59; notes.md §136
**Hourly 0151 HIGH (`notes.md` §137).** Open-Jev v3 densify HEAD ed45657bf726. README SHA 12e0f581e15d. v3 data prepared ≠ retrained released models. held-out protocol ≠ Harbor. 1,280-row panel ≠ Harbor. finite training loss ≠ quality improvement. website redesign ≠ calibration. jev-wide naive throws away 83% *theirs*. certo KL 0.008 *theirs*. first-instinct 63.3%→78.1% *theirs* not Harbor. Jev is a gate not a generator. community port ≠ TypeSafe. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#60. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 0151 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD ed45657bf726 via 748ae3024294 README SHA 12e0f581e15d was e32c4bbd519c; Publish audited v3 community data and held-out evaluation protocol; Redesign readable project site and consolidate benchmark results; 129,288 decision rows 74,921 training; frozen mixture 96,849 training; 1,280-row / 840-group comparison panel; v3 data prepared ≠ retrained released models; held-out protocol ≠ Harbor; 1,280-row panel ≠ Harbor; finite training loss ≠ quality improvement; website redesign ≠ calibration; 27B step 616 pending; Open-Jev TREC pending; LoRA ≠ RLCD replica; Qwen3.5-2B ≠ Archer; Qwen3.5-9B ≠ Archer; densify §125 not a sibling first sighting; chy4pro/jev-for-chrome 12★ community port ≠ TypeSafe; chy4pro/jev-for-chrome ≠ browser-use/jev-ultrafast; PsiACE/dohnuts 4★ small multimodal direct decisions; joint RLCD *theirs*; Dohnuts ≠ TypeSafe; catoenm/first-instinct 9B 63.3%→78.1% *theirs* not Harbor; 371,278 prepared ≠ consumed; RL did not reliably improve held-out; independent educational not a recovered Jev recipe; 123Satyajeet123/jev-wide naive throws away 83% *theirs*; 255 documented ~32,768 tokens real; two-decimal 95.8% floored *theirs*; IIA fails +0.31 ... +0.50 *theirs*; AltSlate-Labs/certo KL 0.008 acc 0.844 ECE 0.004 *theirs*; research preview independent not affiliated; endomorphosis/JevOps Jev is a gate not a generator; Lake remains admission; Jev never writes Lean; gbesse/question-forge held-out before winner; demo accuracy is synthetic not a Jev benchmark; flyryan/ai-news-aggregator 26★ does not execute; Akashdb5/jev-router ≠ gargpratyush/jev-router ≠ daviddl9/jev-router; kiuckhuang/laya-jev ≠ KonghaYao/laya-jev; tegersdorfer-collab/jevkit ≠ isiomaC/jevkit ≠ WaynezProg/jev-kit; buluoray/JevOnly already carded; yottayoshida/jev-intent-review already carded; skip-thin Iskandeur/system1-system2 zhlei07/open-system-one Hand-In/openjev-multimodal gwxcsny53/jev-watchtower empty SHA; serving substrate ≠ calibrated replica; game success ≠ calibrated Noul; does not execute; catalog ≠ endorsement; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60; notes.md §137
Hourly 0248 uniqueness lock: hf:knowledgator/gliclass-instruct-large-v1.0 43 likes sha 825e5478c1bf apache-2.0; Efficient zero-shot and few-shot multi-task model via sequence classification; GLiClass knowledgator Hub family class-peer catalog not Jev equivalent; Knowledgator/GLiClass.c already §123; Hub models first card as class-peer entries; GLiNER/GLiClass ports are class members not Jev replicas; hf:space:mayafree/typed-decision-leaderboard 33 likes sha f4fc44077818; typed-decision-leaderboard *theirs* not Harbor; JEV 0.7350 ZTC 27B 0.7289 ZTC 397B 0.7272 *theirs* not Harbor; 2,018 items same labels; three-way tie; tacticocc/Jevbridge 33★ MIT HEAD da443ea453ac README SHA 2178333c4c3b; Jevbridge ACP and MCP adapter; does not generate text; Any LLM as System One; wire-compat ≠ logit-equiv; tshmieldev/sharp 29★ MIT HEAD 17cbd8d9cc9e README SHA 783a5cde519c; Cut the slop; Filter your X timeline; kavehmz/typesafe-playground 11★ HEAD 733991a2924a README SHA 04c0b1f6e7da; real API calls not polished benchmarks; himomohi/aside-jev 7★ MIT HEAD e570db43b0e1 README SHA 288e7c91c307; Jev picks the next action from your defined candidates; Not a Cua binding; Jev is the model Aside is the browser runtime; nico-martin/open-jev 6★ MIT HEAD 52667199e8a5 README SHA 81c0485d5833; open reproductions of the shape; Nothing is generated; nico-martin/open-jev ≠ razorback16/openjev ≠ Zefan-Cai/Open-Jev ≠ meijustory123/openjev; hf:chaoliangUNSW/Jev-Style-Qwen3.5-2B-Decision-GGUF 82.3% ECE 0.017 *theirs*; Same decision as bf16 94.4% *theirs*; Qwen3.5-2B ≠ Archer; serving substrate ≠ calibrated replica; hf:pngwn/nanodiff-350m-typed-decisions ECE 0.065 → 0.036 *theirs*; hf:litert-community/laya-LiteRT 144/144 *theirs*; gargpratyush/journey-evals A page that says Success is never accepted as proof; mpnikhil/dev-0.4b Banking77 91.33% BoolQ 85.20% *theirs*; encoder class member not Jev replica; n4ze3m/typed-decisions-synth 7,414 cases 25,859 questions; Nobody checked it; Zaious/jev-capability-atlas already carded; LocalLLaMA/typed-decisions already carded; fengyiqicoder/jevfeed already carded; Zhao-Tian-yi/awesome-jev ≠ Gerry9000/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; kaustav1996/reflex ≠ vuckuola619/reflex; tphakala/jev-mcp ≠ jkudish/jev-mcp; ninthspace/hunch ≠ carldaws/hunch ≠ tpellet/hunch; ruban-24/switchboard ≠ cannacre8ive/switchboard-ai; hf:openjev/openjev ≠ razorback16/openjev; catalog ≠ endorsement; skip-thin Fibonaccirabbit/Jev-VLN imanshu03/jev-browser-use luca-saggese/laya.c empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61; notes.md §138
