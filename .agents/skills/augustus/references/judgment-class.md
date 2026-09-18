# The judgment-model class (Jev is exemplar, not monopoly)

Augustus designs for the whole class of **fast, cheap
categorization / classification / scoring models** that return a bounded
answer software can act on — not only TypeSafe Jev. Jev is the documented
exemplar (typed Choice / Score / Noul, calibrated decision objective, live
docs). Neighbors in the class are substitutes or cousins, not a reason to
fork this skill into an install guide.

Integration contracts for Jev stay in `typesafe-ai` + live docs. Other
families own their own cards/READMEs. This file is **which family fits the
hole**, what the objective implies, and what that does to agent
architecture.

Status: **Contract** only for TypeSafe docs you re-read live; everything
else here is **Empirical recipe** (named paper/repo) or **Hypothesis**.

## The class

A model is in-class when most of these hold:

- Input is language, structured text, or (for vision scorers) an image plus
  a closed label/region set.
- Output is a score, a distribution, or a label — not a paragraph.
- Latency/cost is in the "run per chunk / per hunk / per frame" band, not
  "one call per user turn."
- Code, not the model, owns side effects.

Out of class: generative LLMs used as classifiers (prompt → JSON);
regexes/lookups that already work; trained heads on a frozen labeled
taxonomy with enough of *your* data (XGBoost still wins there —
`faq.md`).

## Families

| Family | What it optimizes | Typical output | Use when | Watch |
|---|---|---|---|---|
| **Closed decision API** (TypeSafe Jev) | Calibrated decision (proper-scoring / RLCD lineage) | Choice / Score / Noul + distributions | Default when you need act/abstain, fan-out, documented envelope | Cloud, pin version, re-measure on your data. AU health data-residency is a reason *not* to pick this family (`notes.md` §33) |
| **Open System-1 / decision-model head** (Laya, openjev, LightJev, openjev-lm, Nimble, Hume **Watch**) | Same *shape* as Jev, you host it | Same primitives or logits-as-options | Air-gap, $0/token, inspectable weights, deployment control | Self-eval duty; Laya text-only, 512 tok; vendor vs-Jev tables are claims (`notes.md` §18). A distill learns the *teacher's* answers: openjev-lm and jev-gate-student-b (`notes.md` §25, §33). Nimble is an open LoRA recipe on hard labels, not a Jev distill (`notes.md` §35). Hume's 27B dense drop is **Watch**, not a Hub checkpoint. He prefers the class name **decision models** over "system one" |
| **Encoder open-jev** (DeBERTa-v3-large) | Same *shape*, bidirectional encoder, public gold (not a Jev teacher) | Choice / Score / Noul from one pass | Self-host decide without a decoder; 512 tok | In-domain ECE 0.022; OOD acc 0.854→0.690. English / three public domains. `notes.md` §33 |
| **Constrained-AR surface** (TypeAR; not a species) | Next-token constraint on a pretrained generator | Distribution over allowed values | Typed fields without retraining; later fields must see earlier answers | Different objective from a proper-scoring head. Enum cap and no abstention. Compute-graph card below (`notes.md` §31, §32). Public logit dump: mini-jev-runs |
| **GLi\* encoder family** (GLiNER locate / GLiClass categorize / GLiNER2.5 local multi-head / GLiGuard safety schema) | One-pass labels-in-encoder; spans, sequence labels, a safety schema, or both | Spans + types; per-label sigmoid/softmax; optional relations/records | Laptop/local; large or changing label sets; "what's *in* the text" vs "what *is* the text" vs "which safety labels fire" | Affinities are not automatically a gateable P(permit). GLiGuard is not a Jev weight clone. Species map below. Not a Jev how-to and not a GLiNER or GLiGuard install |
| **Listwise / pairwise discriminative ranker** | Order of a list (nDCG, softmax-over-list) | Relevance scores, not P(relevant) | Rerank a retrieved shortlist | Translation-invariant listwise losses are **not** calibrated for thresholds ([listwise vs pointwise](https://doi.org/10.48550/arxiv.2208.06164); [RCR](https://arxiv.org/html/2211.01494v2)). Fail **open** (keep retrieval order) |
| **Vision scorer** | Image–text affinity or region Choice | Cosine/sigmoid affinity, or a closed region/label pick | Perception as classification over *candidates you extracted* | CLIP softmax = competition in the offered set; SigLIP sigmoid = pairwise affinity, not class-conditional p ([SigLIP](https://huggingface.co/docs/transformers/v4.39.2/en/model_doc/siglip)). Not a VLM captioner |

Pick the family from the **hole**, then pick a vendor. Do not start from a
logo.

## Species map (GLiNER is a peer, not a footnote)

The class is several *species* that share "fast cheap bounded answer,
code owns side effects." They are not aliases.

```text
locate      GLiNER (span NER)              what's *in* the text
categorize  GLiClass / GLiGuard            what the text is; which schema labels fire
decide      Jev / Laya / openjev           Choice / Score / Noul over a state
rank        listwise / cross-encoder       order a retrieved shortlist
perceive    CLIP / SigLIP / region Choice  score candidates you extracted
```

- **Locate.** [GLiNER](https://arxiv.org/abs/2311.08526) (Zaratiana et al.,
  NAACL 2024): bidirectional encoder; open entity types in one forward
  pass; output is *spans*. Mental model: keep/drop over candidates the
  encoder proposed (`applied-mappings.md` §2), not a Noul over the
  document. Downstream code still owns policy.
- **Categorize.** [GLiClass](https://arxiv.org/abs/2508.07662)
  (Knowledgator): GLiNER's architecture adapted to sequence
  classification. Labels interact in one pass (not sequential
  cross-encoder pairs). Good for large/changing tag sets. Cousins:
  NLI zero-shot, SetFit, ModernBERT heads.
- **Local multi-head.** [GLiNER2.5](https://github.com/fastino-ai/gliner2)
  (fastino-ai; 74M/194M/287M, CPU-first): entities + classification +
  records + relations in one schema. Discourse (2026-09-18): same
  *agentic decision* jobs as Jev, local / free / laptop; a 36× Browser
  Use cost claim is a tweet, not a re-run (`notes.md` §25).
- **Decide.** Typed Choice/Score/Noul with a decision/proper-scoring
  objective. That is Jev's product claim. Open heads copy the *shape*;
  distillation copies the *teacher* (openjev-lm, jev-gate-student-b).
  Encoder open-jev (DeBERTa) copies the shape on public gold and still
  owes OOD self-eval. A constrained autoregressive decode can emit a
  label and still not be this species — compute-graph card below.
  Hume's announced 27B dense drop is Watch.
- **Categorize (safety schema).** [GLiGuard](https://github.com/fastino-ai/GLiGuard)
  ([arXiv 2605.07982](https://arxiv.org/abs/2605.07982); Zaratiana,
  Newhauser, Hurn-Maloney, Lewis, Fastino): a GLiNER2 encoder that
  scores a safety schema — prompt/response safety, toxicity, jailbreak,
  refusal — in **one bidirectional pass**. Same *interface shape* as
  batched System One questions (text + labels once). **Different
  training objective**: a moderation schema, not general Choice / Score
  / Noul. Released checkpoint `fastino/gliguard-LLMGuardrails-300M`
  (0.3B). Author-reported, not re-run: 23–90× smaller than 7–27B
  decoder guards; README up to 16.2× throughput and 16.6× lower latency
  (paper abstract says up to 16× throughput and 17× lower latency;
  paper body matches the README). **Empirical** as an open encoder
  class, next to Laya and GLiClass. **Not a Jev weight clone** —
  adapted from GLiNER2 and trained on WildGuardTrain (paper), not
  distilled from Jev answers. "like jev" is discourse
  ([@urchadeDS](https://x.com/urchadeDS/status/2100929613857804379)),
  not an objective match. Figure 3's own caption: it jointly encodes a
  linearized task-label schema with the input text, then scores each
  label with a shared MLP (softmax single-label, sigmoid multi-label)
  in one pass. That is categorize beside decide, not a Noul. A GLiGuard
  score is not a proof.

  **Surfaces.** GLiGuard is for LLM input/output safety.
  [rh-guard](https://github.com/24601/rh-guard) is a coding-agent
  reward-hack gate (README fetched this pass); jevgate is the
  allowlist-then-judge shape (`mappings.md` §18). Different holes.
  Do not point one model at both, and do not copy a hook install here.

  **Aggregation is policy-in-code, already taught.** The README's
  benchmark rule ORs unsafe / non-benign prompt labels and lets refusal
  override an unsafe response. That is their eval script, not new
  doctrine — fuse in code
  (`mappings.md` §3; judge-once / re-policy in
  `composition-algebra.md`; explicit policy in `mixed-architecture.md`).
  Not generalized past that script, so not a Hypothesis.

A GLiNER span is not a drop-in Noul. A GLiGuard label is not a Noul and
not a discharged proof. A GLiNER2.5 classification head can *sit in*
the decide hole on a laptop only after *your* ECE and a fail policy.
Spans or safety affinities that authorize an irreversible act are the
rejected design (same as CLIP-as-gate). Do not copy extract or
guardrail install APIs into this skill.

## Listwise discriminative vs decision objectives

This is the fork that decides fail-open vs fail-closed.

**Discriminative / ranking objective.** Pairwise or listwise losses
(RankNet, ListNet softmax-over-list) improve *order*. Logits measure
relative relevance. Many such losses are translation-invariant: adding a
constant does not change the ranking and **destroys** any reading of the
number as P(click) / P(relevant). Cross-encoders (monoBERT, Cohere-style
rerank) are usually this family even when they emit a "score."

**Decision objective.** Pointwise proper scoring rules (log/Brier/
spherical; RLCD) train the model so a number *means* a belief you can
threshold. Abstention, per-action bars, and "permit ≠ confidence" only
make sense here. Jev's product claim lives on this side. Open heads that
copy Choice/Score/Noul without a proper-scoring train loop may *look*
like Jev and still be uncalibrated — measure.

**Contrastive curation sits next to RLCD, not in its place.**
[Bespoke Nimble](https://github.com/bespokelabsai/nimble) builds pairs
that differ by one focus fact so a hard label flips, then trains on
those labels. The README says the published run did not distill from
Jev and did not use teacher soft targets. That is a data pattern for
a decision head, not a replacement for a proper-scoring objective, and
not a measured ECE. `notes.md` §35.

**GLi\* sits beside decide, not inside it by default.** Locate (GLiNER)
proposes spans; categorize (GLiClass) fires document labels; local
multi-head (GLiNER2.5) can do both plus relations. Classification
sigmoid/softmax *can* be a cheap multi-label sieve. It is not, without
your calibration plot, a decision API. Great for "which of these 80
tags fire" or "which spans are the allergy / the amount / the verb";
not a silent fail-closed authorize. The 255-option Choice limit is
Jev's, not the class's — this family is why.

Rule of composition (`applied-mappings.md` §4):

```text
ranking error  → quality  → fail open (keep the retrieved order)
selection/auth → control  → fail closed, needs a decision-shaped number
```

A listwise reranker plus a decision gate is a valid mixed stack. A
listwise reranker *as* the gate is the rejected design.

**Empirical rejection (Han Xiao trolley, 2026-09-18 — one tweet, no
public repo; a rejection to remember, not a recipe to reuse).** Wrapping
[jina-reranker-v3.5](https://x.com/hxiao/status/2100973209114075330) in a
Jev-style API and asking the trolley problem: it **always pulls the
lever**, whether one person dies or one billion. Relevancy ≠ decision
rationality. I/O compatibility ("it returns a Choice") is not an
objective match. Never treat a listwise retrieval scorer as an
ethics/value Choice without a policy that is *not* the ranker.

## Vision scoring patterns

Perception is candidate generation plus scoring — the same keep/drop card
(`applied-mappings.md` §2), with pixels or an accessibility tree as the
parser.

1. **Pixel-free (preferred when the environment is already structured).**
   RAM / AX tree / object JSON → closed action or region set → Choice.
   Prices and dates stay in code. Launch-week recipes: typesafe-mario,
   jev-drone (classical CV → symbols, Jev advisory), lizard-agent
   (visible elements only). The model never sees a screenshot.

2. **Region / label Choice over extracted boxes.** Perception (detector,
   grid, SAM, OCR boxes) proposes candidates; a scorer picks. `hr98w/jev-visual`:
   Breakout only worked after reducing control to "which region holds the
   ball" — decomposition in miniature. Do not ask a vision model to
   *invent* the paddle command.

3. **Dual-encoder affinity (CLIP / SigLIP / cousins).** Argmax over prompt
   templates is zero-shot classification. CLIP-family softmax induces
   competition among the offered labels; SigLIP's pairwise sigmoid is an
   affinity, flatter closed-set margins, weaker as a probability
   ([posture-classification note](https://arxiv.org/html/2510.13364v1)).
   Calibrate or conformalize before a safety gate; class-conditional
   coverage can collapse under shift even when marginal coverage looks
   fine ([VLM conformal audit](https://arxiv.org/html/2608.19376v1)).

4. **VLM-as-judge.** A captioning/chat model asked "is this safe?" is
   *generation*. Verbal scores are not calibrated. Use it to *propose*
   labels or describe, then score with a class model — or don't.

Laya's card is text-only / 512 tok: a vision hole is not "run Laya on a
caption." Either pixel-free the state or pick a vision-family scorer.

## Portents for agent architecture

Cheap judgment as a **control plane** around a generator is the
capability shift, independent of vendor:

1. **Full-traffic, not sampled.** Per-step, per-hunk, per-line, per-frame
   judgments were known and too expensive. They are now the default
   design (OpenSmoke, jevprune, git-jev-stage, firehose). Agents that
   still LLM-judge 2% of traces are leaving the economics on the table.
2. **Skills and tools become a catalog + decision**, not a stuffed
   system prompt. Rank-then-verify, reject-all first-class
   (`applied-mappings.md` §5). Large label sets may prefer a GLiClass
   one-pass (categorize: text + all labels together) over a 255-option
   Choice — that limit is Jev's, not the class's. GLiNER is *not* the
   substitute here: selecting a catalog member locates nothing (species
   map above).
3. **Two numbers, two jobs.** Ranking scores order context. Decision
   scores authorize. Harnesses that collapse them will either stall
   (fail-closed on a listwise number) or leak (fail-open on a gate).
4. **Perception is not narration.** Computer-use and robotics that
   caption the world then plan in prose are on the wrong side of the
   class. Extract candidates, score, act; generate text only when
   something must be typed.
5. **Open heads and GLi\* make the control plane local.** Air-gap /
   on-device / laptop (GLiNER2.5 74M–287M CPU-first; openjev-lm 0.5B
   LoRA overnight on 6 vCPU; encoder open-jev DeBERTa-v3-large 434M;
   jev-gate-student-b 0.5B LoRA memory gate) become newly feasible *if*
   you accept self-eval and envelope limits. They do not make
   calibration optional. Distilling a hosted teacher is not independent
   gold. Hume's 27B dense drop is the large-local Watch, not a third
   how-to.
6. **Cross-modal is still thin.** Discourse, GLiNER/GLiClass, Laya, and
   the encoder open-jev are text-first. Vision is a scoring pattern
   (above), not a shipped omni decision API. Hume reports that a
   multimodal *base* plus text post-training generalizes to images with
   little intentional multimodal training — a Watch claim, not a
   recipe (`notes.md` §33). Treat "Jev but for images" as a hole to fill
   with the vision-scorer family or with that drop *when it ships*.
   Locate (spans on a screenshot OCR) is still locate, not perceive.
   Pixel-free computer-use (jev-macos-loop, jev-mobile) keeps pixels on
   the device and sends text-only decisions.
7. **The agent that only has a generator is incomplete.** The missing
   organ is a judgment-class model plus policy in code — not another
   prompt. The agent that only has a ranker is also incomplete: it can
   sort, it cannot abstain.

None of these portents require TypeSafe. They require picking a family
whose *objective* matches the action's fail policy, then falsifying on
your labels.

## Marginals, not a probabilistic program

Erik Meijer, 2026-09-18
([post](https://x.com/headinthebox/status/2100984170004824221)): Jev is
a cool API, and it is **not** probabilistic programming. Kleisli-arrow
qualifications are an exaggeration. The gloss he endorses: **Jev gives
you the marginals; a decoder gives you the joint.**

System One / Jev-class is factorized **marginals** over typed questions
given shared state — isolated branches. That is the same fact as the
architecture reconstruction: questions on one request do not attend
each other (`notes.md` §31, item 7; compute-graph card below). Do not
restate that essay here. The jointly best tuple need not be the tuple
of marginally best answers.

The joint, and any dependence between answers, lives in application
code, in sequential TypeAR, or in a generative decoder. It does not
live inside one Jev call. Do not market or teach Jev as a probabilistic
programming language or as Kleisli sugar. The frames are decision
theory, calibration, and value of information (`mental-models.md`).

When you need a joint or an invariant, reach for TLA+, Alloy, or
contracts (`formal-methods.md`). When you need a fast calibrated factor
over one typed predicate, reach for System One. That is a placement,
not a new formal-methods doctrine. A Noul is still not a proof.

## Entropy as allocator (Hypothesis)

Alex Atallah (OpenRouter), 2026-09-14
([buckets](https://x.com/alexatallah/status/2099511056989147147))
and 2026-09-18
([quoting that post](https://x.com/alexatallah/status/2100962947711295557)).
He tells customers to split AI work into three buckets — low entropy
(who should review a PR), medium (review the PR), high (write a PR) —
and that today a frontier model is needed only for the third. The later
post claims Jev is the first model to truly optimize for the first two.
Both URLs verified (`notes.md` §38). The priority claim is his, not a
measurement.

**Place the work, then the surface.** A low- or medium-entropy step
that is a *typed decision* belongs on System One / Jev-class:
factorized marginals, the card above. High entropy that must
*synthesize* a joint — a diff, a paragraph, a plan that was not already
a candidate — stays on a generative frontier decoder. Same axis as
Meijer (marginals vs joint; Jev is still not a probabilistic program
and not Kleisli) and as value of information / compute budget
(`mental-models.md`): do not buy the joint when a cheap marginal would
authorize the next act. Then pick a row in the when-to-use table. This
is not a sixth surface and not an entropy meter.

**Agent loop.** Many cheap low-entropy scorers per turn. A
high-entropy write is rare, and it sits downstream of those scores.
Code still fuses the marginals and owns the side effect.

**Caveat (load-bearing).** "Review this PR" as medium entropy is still
partly generative. Treat Atallah's buckets as product rhetoric that
needs a decision-versus-generation cut, not a literal entropy meter.
"First model ever" is a claim, not an Empirical fact.

Contracts, property tests, and gates attach to those low- and
medium-entropy *decisions*; high-entropy writing is where specs stay
soft (one sentence in `formal-methods.md`). **Hypothesis** until a
labeled log shows the cut beats sending every bucket to a frontier
model on your costs. The examples are rhetoric, not a dataset. Attached
OpenRouter charts (deterministic / semi-variable / variable) are the
same rhetoric; they are not a benchmark.

## Compute graph: readout vs constrained AR vs diffusion reads

[Archer Hume, *Jev's Architecture Unmasked*](https://archerhume.com/posts/jevs-architecture-unmasked/)
(17 Sep 2026, `jev-1.13.0`). **Reconstruction from ~10k API probes, not a
TypeSafe contract.** Observed vs inferred: `research/notes.md` §31. The
~32k / ~65k / 255 envelope he re-measured matches the live docs; the
essay does not override them.

Labeled in one line: (1) direct readout, not AR text — published;
`output_tokens` is a billing figure, not a decode trace (**observed**);
(2) shared state, questions isolated — isolation **observed**, prefix KV
**inferred**; (3) causal pretrained decoder — **inferred**; tokenizer
closest to Qwen among publics, not an exact match — **observed**; (4)
options interact before the choice — irrelevant-option odds shift and
order sensitivity **observed**, mechanism not unique; (5) train the
distribution (RLCD name published; which proper scoring rule **inferred**),
confidence is then arithmetic (**observed** in the adapter he cites) —
confidence ≠ learned correctness; (6) sparse MoE — **inferred, not
observed**; (7) batch the branches, not a conversation — no cross-answer
dependency, and duplicates are non-deterministic (**observed**).

[TypeAR](https://github.com/zmtomorrow/TypeAR) is the constrained-AR
alternative to (1) and (7): same typed interface shape, different compute
graph (still emits one constrained token, or numeric steps). Use it, or a
state machine where **code owns transitions**, when a later decision must
see an earlier answer. Questions on one Jev request do not. Not a TypeAR
how-to.

Three compute graphs speak Jev-shaped I/O. A trained decision-only
readout (Jev, or an open head you have measured). Constrained
autoregression (TypeAR, above). Diffusion structured reads (below).
They are not three species, and none of them is a probabilistic
program.

### Holes

| Need | Place | Do not |
|---|---|---|
| Calibrated p(y\|x) over a closed set | Trained decision-only head (Jev, or an open head you have proper-scored and measured on your labels) | Threshold a generated "90%", an affinity you have not calibrated, TypeAR constrained scores, or a LoRA student's agreement with the teacher |
| Dependent sequential decisions | Constrained AR that conditions later steps on earlier answers (TypeAR sequential), or code-owned transitions and a new request per stage | Treat sibling questions on one request as if they attend each other |
| Open multimodal self-host / data-residency | Hume's announced **decision-model** drop **when it ships** (Qwen3.8 27B **dense**, 265k, multimodal, no audio; one forward pass locally once AR is removed; MoE next then shrink). Driver: healthcare AU residency, not anti-TypeSafe | Ship on "smarter than Jev." That is his early claim, against his own order-sensitivity and in-distribution calibration warnings. **WATCH** — no Hub weights this pass. Laya remains text-only. jev-visual is region Choice, not this drop |
| Image-in now, different graph | Diffusion structured reads that already accept images on a Jev-shaped interface ([djev-spark](https://github.com/mmastrac/djev-spark)) | Wait on the row above for image-in, or treat this graph as a proof it beats a decision head |

### When to use which decision surface

Five *surfaces*, not five species — plus an open recipe and a diffusion
graph that are not extra species either. Pick from the hole and these
axes; do not start from a logo. Hume prefers the class name **decision
models** over "system one"
([tweet](https://x.com/4rcherhume/status/2100604161821979134)). This
skill keeps TypeSafe's "System One" when quoting the exemplar.
Bucket the task first (entropy as allocator, above; **Hypothesis**,
`notes.md` §38). These rows are typed decisions. High-entropy synthesis
is the generator, not a sixth surface.

| Surface | Calibration | VOI / gather | Latency / $ | Deployment control | Multimodal | Enum size |
|---|---|---|---|---|---|---|
| **Proprietary Jev** | Decision objective; in-dist ECE 0.0313, OOD collapse (`notes.md` §7). Choice `confidence` is arithmetic on the distribution (§31) | Independent questions cheap; sequential gather is a new request | Cloud envelope; ~$0.042/MTok input | No weights. AU health data cannot ride this API if residency forbids it | Text. jev-visual is region Choice | ≤255 Choice |
| **Archer open decision-model** | **Watch.** No Hub weights this pass. "Smarter than Jev" is a claim against *his* calibration/order warnings | Same *hole* as Jev when it ships | 27B dense for one-forward-pass local speed once AR is removed; MoE next, then shrink. Quant-friendly is a claim | Healthcare AU data-residency / deployment control, **not** anti-TypeSafe | Multimodal, no audio. Text post-training reportedly generalizes to images with little intentional multimodal training | Unknown until the drop |
| **TypeAR** (constrained AR; README names SGLang) | Next-token constraint ≠ Noul. No abstention primitive. Public logit dump: [`Mikhail/mini-jev-runs`](https://huggingface.co/datasets/Mikhail/mini-jev-runs) (27.9k; scores "deliberately *not* calibrated") | Sequential mode conditions later fields; that is not gather-as-act | 5.8× is *their* K=16 boolean example | Self-host the generator | Whatever the base model has | Enums ≤16 |
| **Encoder open-jev** (DeBERTa-v3-large 434M) | Public gold, CE+Brier, val temperature. In-domain ECE 0.022 / acc 0.854; OOD acc 0.690 / ECE 0.035. **Not** a Jev teacher-copy | One pass over state + all questions; 512 tok | Author: 28 ms / 10 questions H100; 1.8 s / 4q M1 Max CPU | apache-2.0, self-host | Text | Jev-shaped 255 / Score 2–10 / Noul; 512 ctx |
| **Tiny LoRA distill** (jev-gate-student-b) | Teacher-copy. P(relevant) from yes/no logits. Held-out n=60 vs vanilla 0.5B; 148,160-row corpus | Memory-gating / context sieve; **fail-open** on errors | Qwen2.5-0.5B LoRA; ~59 ms RTX 3060 | Local, apache-2.0 | Text | Binary relevance |
| **Nimble** (open LoRA recipe, not a distill) | Hard synthetic labels. They say temperature was not tuned to correctness rates. 324-row agreement is their receipt, not an ECE (`notes.md` §35) | Not a gather primitive | Their latency table, not re-run | Self-host the adapter. Model card Apache-2.0; repo license absent | Text only | Enum ≤26; 2,048 tokens |
| **Diffusion structured reads** (djev-spark) | Interface claim only. **Hypothesis** it beats a decision head on your labels (`notes.md` §36) | Optional sequential chunks, text-only | Their GX10 tables, not a class benchmark | DGX Spark container. Do not copy the route | Images are an extension; think and sequential reject images | README criteria, not copied here |

Reject: TypeAR scores as fail-closed P(permit); a LoRA student's
agreement with Jev as independent gold; shipping on "smarter than Jev";
thresholding [`jp-sns-jev7-estimator`](https://huggingface.co/kokuren/jp-sns-jev7-estimator)
teacher scores as P(toxic) — the card says they are **not** calibrated,
and `threat` F1@0.5 is 0.0000 on their table (`notes.md` §33). Domain-local
ONNX distill is still categorize / score. Nimble's holdout is not a
universal ranking. Diffusion beating a decision head is Hypothesis.

Detail: `research/notes.md` §33 (surfaces), §34 (marginals), §35
(Nimble), §36 (diffusion), §38 (entropy allocator, Hypothesis). FAQ:
open weights vs Jev vs TypeAR vs encoder vs LoRA; is Jev probabilistic
programming?

**Diffusion structured reads (third graph).**
[djev-spark](https://github.com/mmastrac/djev-spark) serves DiffusionGemma
26B-A4B (NVFP4) on a DGX Spark and speaks a Jev-shaped decision API.
README: structured-reads patches on the engine; images via multipart or
JSON, which stock Jev does not have; optional sequential chunk
conditioning, a think step, and entropy-triggered extra samples. Text
plus images together reject sequential conditioning and the think step.
**Empirical** as that public interface (HTTP 200, 2026-09-18).
**Hypothesis** that diffusion beats a trained decision head on your
task. Archer's audio-less multimodal drop stays **WATCH**. Do not copy
the route or the patches. `notes.md` §36.

### Open recipe (Bespoke Nimble) — not a distill

[bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) and
[Bespoke-Nimble-9B](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B)
(both HTTP 200). Model card: Apache-2.0 LoRA on `Qwen/Qwen3.5-9B`.
The GitHub repo has no license file — do not call the repo Apache-2.0.

- **Open training recipe.** Contrastive curation: change one focus fact
  so the hard label flips; train the decision head on those labels.
  README: not distilled from Jev. `notes.md` §35.
- **Data pattern beside RLCD, not a replacement.** Hard synthetic
  labels, no teacher soft targets in the published objective. RLCD
  remains the named proper-scoring lineage. "Implicit calibration" is
  their claim; they also say temperature was not tuned to correctness
  rates.
- **9B vs proprietary Jev is Hypothesis** until you measure on your
  labels. Their holdout is the existence proof the gap can be small,
  on their set only: Nimble 90.12% (292/324), Jev 1.13.0 93.21%
  (302/324), untuned Qwen3.8-27B 84.88% (275/324), base Qwen3.5-9B
  66.36% (215/324). **Empirical** as that named receipt, not a ranking.
  Synthetic labels, six source families, 162 pairs.
- **Bake-off candidate** beside Laya, openjev-lm, and TypeAR
  (`validation.md`). Not a jevals how-to.

Serving, not copied: candidate logits, then softmax; one path shares
context across fields, another rescores each field; fields are
independent; text only; enum at most 26; prompts over 2,048 tokens
rejected. Probabilities normalize over the candidates you supplied —
the standing Choice-conditional-on-offered-set boundary (`SKILL.md`).
Add "no match" when coverage is open. A high probability is not a
correctness guarantee (their sentence).

### Constrained-AR surface (not `decide`)

[TypeAR](https://github.com/zmtomorrow/TypeAR) ("Type-Safe Decoding for
Autoregressive LLMs"; Python; created 2026-09-17, README updated
2026-09-18) is a **surface** on a pretrained generator. The objective
is a next-token constraint, not a proper-scoring decision head. A
distribution over allowed values is not a Noul. No license file was
present at fetch.

README contract, re-read before relying: finite enums of at most 16
values; string, integer, number, and boolean; open integer and number
by tokenizer-native constrained decoding (added 2026-09-18). Closed
decisions emit one output token. Sequential mode conditions each later
field on earlier values. Batch mode forks independent fields after one
shared prefill. Their one receipt is about 5.8× throughput versus
sequential on Qwen3.8-27B, K=16 booleans — **their** example, not a
portable benchmark. With prefix reuse, new prefill is on the order of
C + D·S unique tokens. Argmax is the default; a sample mode applies
temperature to the constrained scores.

Jev questions on one request do not see each other's answers
(`question-design.md`). TypeAR sequential mode does. That is the
comparison, and it is still not a state machine: `mappings.md` §19
(effect-oriented loops) and §3 keep transitions in code. Batch mode is
the isolation pattern. Enum width and no abstention primitive are
brittleness — compose with cost-sensitive abstention (`mappings.md`
§2), paraphrase abstain (`mappings.md` §17), and a jevgate-shaped gate
(`mappings.md` §18). rh-guard's README (HTTP 200) is a coding-agent
reward-hack gate, a different surface from this one and from GLiGuard.
Do not copy the hook install.

**Hypothesis, not a stack.** TypeAR's example names the same Qwen3.8-27B
family as Hume's announced weights. Running that surface on those
weights versus stock Qwen is a composition to test after the weights
exist. Until then, **Watch** (`notes.md` §31, §32, §33).
[`Mikhail/mini-jev-runs`](https://huggingface.co/datasets/Mikhail/mini-jev-runs)
is the public read-the-letter logit dump (frozen Qwen3-4B, 27.9k
decisions, no token generated) for calibration / gap-abstention /
rotated-option tests — not a TypeAR how-to and not a Noul.

Option order and an irrelevant extra option are properties to test, not
a proof (`formal-methods.md`).

## Decision-design extras for class choice

When the request is "Jev vs GLiNER vs GLiClass vs CLIP vs a cross-encoder":

```text
Hole (sieve / keep-drop / triage / rank / route / gate / perceive):
Family (from the table) and why the objective matches the fail policy:
What the generator is still for:
Envelope (tokens, modality, label-set size, latency budget):
Self-eval duty (closed API vs open weights vs affinity scores):
Smallest experiment that could reject this family, not just this vendor:
```

Propose two families if the hole is mixed (e.g. listwise rerank +
decision gate). Do not invent a hybrid API.
