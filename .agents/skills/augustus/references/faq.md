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
not a scorer.
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
calls. [jev-reviewer](https://github.com/choxos/jev-reviewer) points at
ids; *not found* is an answer. [solari-reflex](https://github.com/hitakshiA/solari-reflex)
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
id still `fast-jev-output`. `judgment-class.md`; `notes.md` §50, §53.

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
proposed call). `mappings.md` §8; `applied-mappings.md` §7;
`notes.md` §59.

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
(uncalibrated CUDA likelihoods). Small n — *their* card.
`judgment-class.md`; `notes.md` §61.

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
`judgment-class.md`; `mixed-architecture.md`; `notes.md` §52, §54, §57, §61.

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
[Essay](https://archerhume.com/posts/jevs-architecture-unmasked/),
`notes.md` §31, `mental-models.md` calibration.
