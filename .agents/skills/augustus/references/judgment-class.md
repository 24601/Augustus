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
| **Open System-1 / decision-model head** (Laya, openjev, LightJev, openjev-lm, Nimble, **kev**, **blackwood-rlcd**, Hume **Watch**) | Same *shape* as Jev, you host it | Same primitives or logits-as-options | Air-gap, $0/token, inspectable weights, deployment control; **image-in now** (blackwood) without waiting for Archer | Self-eval duty; Laya text-only, 512 tok; vendor vs-Jev tables are claims (`notes.md` §18). A distill learns the *teacher's* answers: openjev-lm and jev-gate-student-b (`notes.md` §25, §33). Nimble is an open LoRA recipe on hard labels, not a Jev distill (`notes.md` §35). **kev** is a shipped Qwen2.5-0.5B LoRA + pointer readout of Archer's reconstruction — public gold, not a Jev teacher; ID ECE only (`notes.md` §45). **blackwood-rlcd** is open multimodal RLCD (CC BY-NC), Jev-compatible shim; Jev still leads general text (`notes.md` §46). Hume's 27B dense drop is **Watch**, not a Hub checkpoint. He prefers the class name **decision models** over "system one" |
| **Encoder open-jev** (DeBERTa-v3-large) | Same *shape*, bidirectional encoder, public gold (not a Jev teacher) | Choice / Score / Noul from one pass | Self-host decide without a decoder; 512 tok | In-domain ECE 0.022; OOD acc 0.854→0.690. English / three public domains. `notes.md` §33 |
| **GLiFormer wire-compat encoder** ([jeff](https://github.com/logan-markewich/jeff) on gliformer-large-v1 400M) | Labels-in-encoder; System One *wire*, not a Jev replica | choice / score / noul via `/v1/systemone`; typesafe-sdk `base_url` | Self-host the envelope when you own the GPU path and accept the accuracy gap | Normalized sigmoids, T=3.2; isolate nouls; DeBERTa tokens ≠ Jev billing. L4 HTTP ~6× cheaper; A10G direct ~24×; AG News 75.5% vs 90.5% *theirs*. CPU is *more* expensive. License null this pass. `notes.md` §60 |
| **Constrained-AR surface** (TypeAR, **pcdServer**; decision-token LoRA; not a species) | Next-token constraint on a pretrained generator | Distribution over allowed values | Typed fields without retraining; later fields must see earlier answers; local GGUF serving; train the *decision token* if you LoRA | Different objective from a proper-scoring head. TypeAR README enums ≤16; pcdServer 2–256 / 1–63 parallel fields. No abstention primitive. Decision-token QLoRA: `Foodoo1/Qwen3-14B-RLCD-Decision-LoRA` (`notes.md` §46). Compute-graph card below (`notes.md` §31, §32, §42). Public logit dump: mini-jev-runs |
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
decide      Jev / Laya / openjev / kev / blackwood / Domain-jev-maker LoRA   Choice / Score / Noul over a state (blackwood: image-in)
            jeff (GLiFormer)               same *wire*, encoder backend, not a Jev replica
rank        listwise / cross-encoder       order a retrieved shortlist
perceive    CLIP / SigLIP / region Choice  score candidates you extracted
```

SAM 3.1 (masks and tracks) and an ASR transcript are upstream
perception *producers*. They emit masks or text, not a score over
candidates you already extracted, so they are not the **perceive**
species (CLIP / SigLIP / region Choice). Jev on that serialized state
is **decide**. Stacking them is composition, not one model — card
below, next to the when-to-use table.

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
  **Extractive compaction (Empirical as README behavior, 2026-09-18
  ~16:22):**
  [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
  (Apache-2.0) is the named *job* on this family, not a new species.
  Default checkpoint `fastino/gliner2.5-base-v1`. One encoder does
  **categorize** (retention Choice: `keep_full` / `keep_evidence` /
  `keep_call_only` / `drop`) and **locate** (character-offset spans);
  code copies verbatim. **Not Jev, not a Noul, not a prose
  summarizer, not multimodal.** Same compaction hole as
  fast-jev-compaction / pi-jev-compaction (Jev Noul/Score backends);
  Augustus stays backend-agnostic. Mutating tools and shell operators
  are a hard `keep_full` envelope; low-confidence / invalid evidence
  fail closed to `keep_full` (the *reduction* is the irreversible
  act — contrast many fail-open Jev preference gates). Public default
  `shadowMode: true`. Reduction is measured in characters, not
  tokens; no published retention-quality rates (`notes.md` §50).
  Fastino/GLiGuard sibling *class*, not a GLiGuard safety-schema
  clone. Do not copy the plugin install.
  **Stdout prune (Empirical as README / evals README, 2026-09-18
  ~17:15):**
  [jev-pruner](https://github.com/tamaratran/jev-pruner) (MIT) is the
  same evidence-preserving *family* on a **different job** and the
  **Jev** backend: Noul-prune Bash stdout after a hard ≤10k /
  JSON-diff-whole-doc envelope, before the main LLM sees it. Not a
  summarizer. Fail-safe keep original. Archive for recovery.
  Marketplace id still `fast-jev-output`. Codex is opt-in wrapper.
  Same author as fast-jev-compaction; complementary (`notes.md`
  §53). Do not copy the plugin.
  **Code-graph indexer (Empirical as README behavior; 10–50× is a
  target, 2026-09-18 ~16:48):**
  [s1-graphify-indexer](https://github.com/GreyssonEnterprises/s1-graphify-indexer)
  (+ sibling `s1-indexer`) uses GLiNER2 as the default System-1
  backend to build a semantic code graph and escalates an LLM only
  on the ambiguous tail **and only if the backend loaded**. Jev /
  Needle stubs `available=False` until implemented. If GLiNER2
  cannot load: degraded file-node graph, exit nonzero, do not dump
  the repo to `S1_LLM_CMD`. Query does not invent edges. GitHub
  one-liner 10–50× is **unfilled** — not Empirical (`notes.md` §51).
  Same locate family as compaction; different hole (index vs
  keep/drop). License not on GitHub this pass.
  **Computer-use selection (Empirical as README / architecture
  behavior, 2026-09-18 ~16:56):**
  [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
  (MIT) is a *different named job* on the GLi\* encoder family, not
  a new species and **not GLiNER2.5**. Checkpoint
  `fastino/gliner2-multi-v1`. Adaptation of
  [jev-ultrafast](https://github.com/browser-use/jev-ultrafast):
  local GLiNER2 extracts requirements and **scores observed**
  a11y/DOM controls; code clicks. **No screenshots. No generated
  selectors.** Same observe→score-among-candidates→code-acts hole
  as jev-ultrafast / solari-reflex (Jev backends) and
  [laya-mind2web](https://huggingface.co/ShaunSpark/laya-mind2web-browser-agent)
  (Laya over DOM element indices). Contrast blackwood-rlcd
  (screenshot + marked letters → Choice). Hybrid: local decide;
  remote text helper only for TYPE. `DONE` is loop termination, not
  verified success. Inspector scores are not calibrated P(task
  success). Their Flights demo (12.20 s / 13.785 s / ~$0.0001 API)
  is a demonstration, not a bake-off (`notes.md` §52). Do not copy
  `uv` / `.env`.
  **Specialist computer-use S1 (Empirical as README / MODEL_CARD
  behavior, 2026-09-18 ~17:21; weights Watch):**
  [Cua-S1](https://github.com/trycua/cua/tree/main/libs/cua-s1)
  (`trycua/cua`, MIT source) is a **parallel "System One" name**, not
  TypeSafe Jev and not GLiNER. Reference `tinyx`: byte encoder +
  option-attention head. Per observed element: fill (from extracted
  `Label: value`) / check / click / skip. Does not generate values
  or selectors. Plan ≠ execute; dry-run default; `execute` and
  `submit` independent opt-ins; fail-closed on unknown checkbox
  state. Profile `cua-s1-form-v0` is source-only — no weights, no
  checkpoint scores   (`notes.md` §54). Do not copy `uv` / MCP.
  **Harness productization (Empirical as PR-body architecture +
  their local eval, 2026-09-19 ~00:48; draft Watch):**
  [Stagehand #2955](https://github.com/browserbase/stagehand/pull/2955)
  (5/5 of #2951–#2955, all OPEN draft) puts the same
  observe→score-among-candidates→code-acts hole inside
  Browserbase Stagehand. Jev picks a11y elements; code copies text
  or acts. Extract `"off"` | `"judge"` | `"pick"`. Schema / completion
  gate / screenshot-always-LLM in **code**; LLM fallback. Their
  extract card (gemini-3.8-flash, 25×3): 37/75 no-LLM ~0.5 s vs
  4.37 s; 69/75 vs 23/25 (92% both); LLM-off 36/75 — pick ≠
  replacement. Do not merge with jev-ultrafast / gliner2-ultrafast
  / Cua-S1 clocks. Not multimodal pixels on the pick path
  (`notes.md` §57). Do not copy `experimentalJevAct`.
- **Decide.** Typed Choice/Score/Noul with a decision/proper-scoring
  objective. That is Jev's product claim. Open heads copy the *shape*;
  distillation copies the *teacher* (openjev-lm, jev-gate-student-b).
  **Domain specialist LoRA** ([Domain-jev-maker](https://github.com/help-er/Domain-jev-maker))
  trains on **independent gold** (CLINC-150), not Jev answers — pick
  it when downstream reads p; few-shot hosted when only argmax
  (`notes.md` §60).
  **Do not distill Jev as teacher of record.**
  [jev-triage](https://github.com/ThyFriendlyFox/jev-triage)
  logs full distributions for a *local* student and keeps
  **real outcome labels** as targets. Author ~68% ceiling
  compounds errors. Distinct from Domain-jev-maker
  (independent gold) and openjev-lm (teacher-copy)
  (`notes.md` §61).
  Encoder open-jev (DeBERTa) copies the shape on public gold and still
  owes OOD self-eval. **kev** copies the Archer readout (block-causal
  isolation, pointer head, CE vs labelled public gold) and still owes
  *your* ECE — ID numbers are not OOD. A constrained autoregressive
  decode can emit a label and still not be this species — compute-graph
  card below. Hume's announced 27B dense drop is Watch.
  **blackwood-rlcd** is the open multimodal *decide* head that ships now
  (screenshot + marked candidates → Choice; CC BY-NC; Jev still leads
  general text; `notes.md` §46) — not that drop, and not a vision-scorer
  affinity.
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
  allowlist-then-judge shape (`mappings.md` §18);
  [Abide](https://github.com/coldteadotai/abide) is project-instruction
  soft rules on diffs (`mixed-architecture.md`).
  [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
  is extractive context compaction (locate + categorize on tool
  transcripts; Fastino sibling class, not a GLiGuard clone)
  (`notes.md` §50).
  [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
  is browser computer-use scoring among observed controls (GLiNER2
  `gliner2-multi-v1`, not 2.5; `notes.md` §52). Different holes.
  Do not point one model at every hole, and do not copy a hook install here.

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
not a silent fail-closed authorize. Named compaction job
([gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)):
locate + categorize, then code copies exact offsets; fail-closed
`keep_full` is the *reduction* policy, not a Noul (`notes.md` §50).
The 255-option Choice limit is
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
   (visible elements only). Encoder-backend cousin:
   [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
   scores observed a11y/DOM controls with local GLiNER2; code clicks
   (`notes.md` §52). The model never sees a screenshot.

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
   jev-gate-student-b 0.5B LoRA memory gate; **kev** 0.5B LoRA + pointer,
   ~160 ms / 6 questions on an M5) become newly feasible *if*
   you accept self-eval and envelope limits. They do not make
   calibration optional. Distilling a hosted teacher is not independent
   gold. Hume's 27B dense drop is the large-local Watch, not a third
   how-to.
6. **Cross-modal has an open decide head now; Archer is still Watch.**
   Discourse, GLiNER/GLiClass, Laya, kev, and the encoder open-jev are
   text-first. Vision scorers (CLIP/SigLIP) remain a scoring pattern,
   not a decision API. [`BlackwoodAI/blackwood-rlcd`](https://huggingface.co/BlackwoodAI/blackwood-rlcd)
   is the shipped omni *decide* model: screenshot or text in, typed
   Choice out, Jev-compatible shim (`notes.md` §46). Hume's 27B dense
   drop stays **Watch** (no Hub weights this pass; multimodal, no audio).
   Prefer specialist composition (SAM / ASR / OCR → schema → System One)
   when you already have the producer; prefer a shared multimodal
   decision model when the joint of pixels and options matters. Pixel-free
   computer-use (jev-macos-loop, jev-mobile) still keeps pixels on the
   device and sends text-only decisions. Locate (spans on a screenshot
   OCR) is still locate, not perceive.
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
| Laptop-local System One API for development / eval | **kev** — trained decision-only readout; official SDK with a `base_url` change (`notes.md` §45) | Treat 0.5B ID ECE as a knowledge or frontier substitute, or as OOD calibration |
| Dependent sequential decisions | Constrained AR that conditions later steps on earlier answers (TypeAR sequential), or code-owned transitions and a new request per stage | Treat sibling questions on one request as if they attend each other |
| Open multimodal self-host / data-residency *now* | **blackwood-rlcd** — trained decision-only readout with image-in; Jev-compatible shim; CC BY-NC (`notes.md` §46) | Wait for Archer's 27B. Treat screenshot-vs-Jev-text as the same input. Threshold a commercial workflow on a non-commercial license. Skip self-eval because web-element acc is 0.907 |
| Open multimodal self-host / data-residency *when it ships* | Hume's announced **decision-model** drop **when it ships** (Qwen3.8 27B **dense**, 265k, multimodal, no audio; one forward pass locally once AR is removed; MoE next then shrink). Driver: healthcare AU residency, not anti-TypeSafe | Ship on "smarter than Jev." That is his early claim, against his own order-sensitivity and in-distribution calibration warnings. **WATCH** — no Hub weights this pass. Laya remains text-only. kev is text-only. jev-visual is region Choice, not this drop |
| Image-in now, different graph | Diffusion structured reads that already accept images on a Jev-shaped interface ([djev-spark](https://github.com/mmastrac/djev-spark)) | Wait on the row above for image-in, or treat this graph as a proof it beats a decision head |

### When to use which decision surface

Five *surfaces*, not five species — plus open recipes (Nimble; **kev**
as the runnable Archer reconstruction) and a diffusion graph that are
not extra species either. Pick from the hole and these
axes; do not start from a logo. Hume prefers the class name **decision
models** over "system one"
([tweet](https://x.com/4rcherhume/status/2100604161821979134)). This
skill keeps TypeSafe's "System One" when quoting the exemplar.
Bucket the task first (entropy as allocator, above; **Hypothesis**,
`notes.md` §38). These rows are typed decisions. High-entropy synthesis
is the generator, not a sixth surface.

| Surface | Calibration | VOI / gather | Latency / $ | Deployment control | Multimodal | Enum size |
|---|---|---|---|---|---|---|
| **Proprietary Jev** | Decision objective; in-dist ECE 0.0313, OOD collapse (`notes.md` §7). Choice `confidence` is arithmetic on the distribution (§31) | Independent questions cheap; sequential gather is a new request | Cloud envelope; ~$0.042/MTok input (their figure, unreproduced; `/pricing` 404 on 2026-09-18, `notes.md` §1, §42) | No weights. AU health data cannot ride this API if residency forbids it | Text. jev-visual is region Choice | ≤255 Choice |
| **blackwood-rlcd** (open multimodal RLCD; CC BY-NC) | Decision objective; temp-calibrated. Card ECE **0.037** on 300 web steps; letter-shuffle flip **0.133** vs Jev 1.13 **0.587**. Jev still leads general text **0.850** vs **0.786** (`notes.md` §46) | Screenshot/DOM candidates code already marked → Choice. Not gather-as-act | ~200 ms / decision 1×H100 (their figure) | Self-host; non-commercial license | **Image-in now.** Not Archer Watch. Not CLIP | Lettered candidates; Jev-shaped Choice |
| **Archer open decision-model** | **Watch.** No Hub weights this pass. "Smarter than Jev" is a claim against *his* calibration/order warnings | Same *hole* as Jev when it ships | 27B dense for one-forward-pass local speed once AR is removed; MoE next, then shrink. Quant-friendly is a claim | Healthcare AU data-residency / deployment control, **not** anti-TypeSafe | Multimodal, no audio. Text post-training reportedly generalizes to images with little intentional multimodal training | Unknown until the drop |
| **TypeAR / pcdServer** (constrained AR) | Next-token constraint ≠ Noul. No abstention primitive. Public logit dump: [`Mikhail/mini-jev-runs`](https://huggingface.co/datasets/Mikhail/mini-jev-runs) (27.9k; scores "deliberately *not* calibrated"). Decision-token QLoRA trains *that* token under parallel constrained decode (`Foodoo1/Qwen3-14B-RLCD-Decision-LoRA`; synthetic fraud receipt, not a financial product; `notes.md` §46). **Harbor cousin:** local MLX PCD Qwen2.5-1.5B on toxic-chat n=50: O(1) / p50 227.2 ms / acc 52% / Brier **0.3884** vs Jev 84.0% / Brier **0.1096** (`system-one-benchmark`; `notes.md` §61) | TypeAR sequential conditions later fields; pcdServer batches independent fields after one prefix. Neither is gather-as-act | TypeAR 5.8× is *their* K=16 boolean example. pcdServer: native llama.cpp, Apple+Linux. Foodoo1: ~234 ms / 4-field broadcast on RTX 3090 4-bit (their figure) | Self-host the generator / GGUF / adapter | Whatever the base model has | TypeAR enums ≤16; pcdServer 2–256 strings, 1–63 fields |
| **Encoder open-jev** (DeBERTa-v3-large 434M) | Public gold, CE+Brier, val temperature. In-domain ECE 0.022 / acc 0.854; OOD acc 0.690 / ECE 0.035. **Not** a Jev teacher-copy | One pass over state + all questions; 512 tok | Author: 28 ms / 10 questions H100; 1.8 s / 4q M1 Max CPU | apache-2.0, self-host | Text | Jev-shaped 255 / Score 2–10 / Noul; 512 ctx |
| **Tiny LoRA distill** (jev-gate-student-b) | Teacher-copy. P(relevant) from yes/no logits. Held-out n=60 vs vanilla 0.5B; 148,160-row corpus. HF card **unchanged** ~17:48 vs §33 (MAE 0.187 / Pearson 0.791 / 90%; ~59 ms RTX 3060; fail-open) | Memory-gating / context sieve; **fail-open** on errors | Qwen2.5-0.5B LoRA; ~59 ms RTX 3060 | Local, apache-2.0 | Text | Binary relevance |
| **Domain LoRA specialist** (Domain-jev-maker) | Independent CLINC gold, soft targets, pointer readout. **Not** a Jev teacher-copy. Calibration gap is the product: KL 0.168 vs hosted 0.580 banking; few-shot hosted matches argmax (McNemar n.s.) | Threshold / deferral / EU that *reads* p; skip when only argmax | ~0.5 s / request on 8 GB GPU *theirs*; 1.5B LoRA | Self-host; MIT | Text | Domain K + abstain; one forward pass |
| **Nimble** (open LoRA recipe, not a distill) | Hard synthetic labels. They say temperature was not tuned to correctness rates. 324-row agreement is their receipt, not an ECE (`notes.md` §35) | Not a gather primitive | Their latency table, not re-run | Self-host the adapter. Model card Apache-2.0; repo license absent | Text only | Enum ≤26; 2,048 tokens |
| **kev** (Qwen2.5-0.5B LoRA + pointer; Apache-2.0) | Public gold, CE. Held-out ECE 0.065 (0.031 after T=1.47); acc 0.799 on 1,350 ID questions. Isolation exact. **Not** a Jev teacher-copy (`notes.md` §45) | Laptop-local System One drop-in for development/eval; independent questions, one prefill | ~160 ms / 6 questions; ~1h45m train on M5; 38 MB adapter | Self-host; official `typesafe-sdk` with `base_url` | Text. Not multimodal. 0.5B knowledge | noul / choice 2–255 / score |
| **Diffusion structured reads** (djev-spark) | Interface claim only. **Hypothesis** it beats a decision head on your labels (`notes.md` §36) | Optional sequential chunks, text-only | Their GX10 tables, not a class benchmark | DGX Spark container. Do not copy the route | Images are an extension; think and sequential reject images | README criteria, not copied here |

**Three open paths** (not three species, not extra when-to-use rows):
encoder open-jev (DeBERTa, public gold); AR constrained decode (TypeAR
Python/SGLang, pcdServer native GGUF; decision-token LoRA on that graph);
trained decision-only (Laya / Nimble / **kev** / **blackwood-rlcd** /
Archer **Watch**). **kev** is the cleanest *runnable* productization of
Archer's reconstruction on that third path (API-compatible; text-only;
`notes.md` §45). **blackwood-rlcd** is the third path with **image-in
now** (CC BY-NC; Jev-compatible shim; `notes.md` §46). Watch stays Watch.
Encoder vs decoder **replicas** of that third path: DeBERTa is public gold with an OOD
drop; openjev-lm / jev-gate LoRAs are teacher-copies with named receipts
(overnight 6-vCPU, $0/call — economics, not a new species; `notes.md`
§25, §44). kev is public gold on the same 0.5B backbone as openjev-lm,
not a teacher-copy. Pick from the hole. A constrained softmax
is still not a Noul. Laya companion packaging this hour:
[`laya-typed-decisions`](https://huggingface.co/convaiinnovations/laya-typed-decisions)
(same 421.3M; acc 0.766 / Brier 0.066 on `LocalLLaMA/typed-decisions`,
unverified — do not overwrite `notes.md` §18). Shared bake-off this
hour: [`pngwn/open-jev-laya-bench`](https://huggingface.co/datasets/pngwn/open-jev-laya-bench)
(26 + 9 tasks, 11,959 items; ECE/NLL/Brier; **not** TypeSafe Jev vs
Laya; LLM-as-judge is not the score — `notes.md` §46, `validation.md`).
**Contract-compatible local surface, not a fourth path:**
[`us/jev-local`](https://github.com/us/jev-local) speaks `POST
/v1/systemone` so an SDK `base_url` drop-in works offline. **Default
scorer is a deterministic stub** until `JEVLOCAL_SCORER=hf`. A green
smoke test on the stub is not a local decision model (`notes.md` §48).
**ONNX replica of Laya:**
[`Mattepiu/laya-onnx`](https://huggingface.co/Mattepiu/laya-onnx)
(~15 ms CPU for one Noul, their card). Do not copy the inherited
vs-Jev accuracy table (`notes.md` §18).
**Complete Laya → browser ONNX (distinct replica; 2026-09-19
~00:39):**
[`gqgs/laya-onnx`](https://github.com/gqgs/laya-onnx) — full
Laya heads + option scorer + qtype embeddings + act/escalate
as int8 ONNX (496.8 MiB). Conversion smoke, not
task-accuracy or calibration. License null. Distinct from
Mattepiu/laya-onnx. Primary omni archive stays Jev-omni.
Do not copy npm (`notes.md` §64).
**Local ModernBERT `/v1/systemone` approximation (not
equivalence; 2026-09-19 ~00:39):**
[`kunchenguid/local-jev`](https://github.com/kunchenguid/local-jev)
— README: "API-compatible local approximation — **not**
behavioral equivalence with Jev." Distinct from jev-local's
stub and jeff's GLiFormer. Thin this pass
(`IMPLEMENTATION-PLAN.md`). MIT (`notes.md` §64).
**Packed one-forward on an open LLM (constrained-AR / logprob path,
not a Jev reproduction):**
[`ikermoel/open-alternative-jev`](https://github.com/ikermoel/open-alternative-jev)
(Apache-2.0). RACE-H packed **92.9% @ 4.55 q/s** on Qwen3.6-27B
8-bit; interference 6–9%; temperature scaling on *your* labels.
Space demo. Economics of packing a shared state, not trained
decision-only (`notes.md` §49).
**CUDA/PyTorch local replica (constrained-AR / logprob cousin, not
a Jev reproduction, not Distillation; 2026-09-18 ~17:48):**
[`Mintzs/jevify`](https://github.com/Mintzs/jevify) — Qwen2.5-1.5B,
package `ora_decision_engine` / CLI `ora-decision`. CUDA graphs,
branch kernels, literal-label scoring. Default `--answer-encoding
letters`. **Uncalibrated model likelihoods, not measured
correctness.** Default refund `workflow.json` is not a validated
policy. **No LICENSE file this pass.** Do not copy Windows CUDA/venv
(`notes.md` §55). Independent of Distillation; independent of
open-alternative-jev's RACE-H receipt — same *class*, different
repo.
**Tiny SAN local surface (extreme speed/econ class, not a replica):**
[`wfzyx/von`](https://github.com/wfzyx/von) — 14 MB Needle; `POST
/v1/systemone`; sub-15 ms CPU *claim* / ~38 ms embed in their table;
authored144 needle **52.6%**. Distinguish from jev-local's **stub**
and kev's trained pointer. **Do not copy the vs-Jev ranking table.**
**GLiFormer encoder serving the System One wire (2026-09-18 ~20:43):**
[`logan-markewich/jeff`](https://github.com/logan-markewich/jeff) —
`knowledgator/gliformer-large-v1` 400M; official SDK `base_url`
drop-in; choice/score/noul. **Not a Jev replica.** Normalized
sigmoids, T=3.2; isolate nouls; DeBERTa tokens ≠ Jev billing.
Their card: L4 HTTP ~$2.6 vs ~$15.6 (~6×); A10G direct ~$0.65
(~24×); AG News 75.5% vs 90.5%; CPU 6–20× *more* expensive.
License null this pass. Do not copy uv / Modal (`notes.md` §60).
**Loopback gateway, not a scorer:**
[`hraness/sysone`](https://github.com/hraness/sysone) — MIT;
routes hosted Jev + local OpenJev/NanoJev/Mini-Jev; does not
install weights; credential from env never config. Early; no
auth/streaming/non-loopback.
**Evaluation-model-first TS library (name collision; MED
2026-09-18 ~23:40):**
[`sysone-help/sysone`](https://github.com/sysone-help/sysone) —
MIT. `predicate` / `classifier` / `rubric` as pure data;
`check` / `evaluate` / `filter` / `partition` / `rank`;
cancellable; never auto-retry. First adapter = Jev via Vercel
AI Gateway. Independent of TypeSafe/Vercel. **Not** the
hraness loopback gateway. Do not copy npm (`notes.md` §63).
**Local MLX PCD vs Jev (Empirical as their n=50 table,
2026-09-18 ~21:39):**
[`mallahyari/system-one-benchmark`](https://github.com/mallahyari/system-one-benchmark)
— Qwen2.5-1.5B 4-bit MLX PCD is O(1) and faster on-device
(p50 227.2 ms) than Jev HTTPS (356.5 ms), and **uncalibrated**
(Brier 0.3884 vs Jev 0.1096; acc 52% vs 84.0%). Softmax over
allowed tokens ≠ Noul. License null. Small n. Do not copy
pip (`notes.md` §61).

**When to use a decision model vs a constrained LLM (Harbor-style
bake-off, not a quality ranking).**
[`nibzard/decision-model-benchmark`](https://github.com/nibzard/decision-model-benchmark)
v2 (`notes.md` §49): no class wins on *accuracy*. Pick from axes
you actually need:

| Need | Lean decision-model (Jev-class) | Lean constrained LLM |
|---|---|---|
| Latency / $ at schema-valid enums | p50 ~264–276 ms; S1 ~$0.07/1k; 0% malformed this run | Thinking-mode seconds and $0.19–$2.48/1k; some malformed |
| Choice sets ≤255 | Flat latency 2→255; **fails at 256+** (`400 Too many choices`) | Handles 512 |
| Honesty / abstain on no-good items | S5 admits 49.7%; ECE 0.246 — measure, do not assume | Most 97.3–100% (gpt-5.4-mini 64.7%) |
| Position stability | S4 flip 13% this run | Up to 37% |
| Mid-pack banking accuracy | 76.3% this protocol (atlas/jev-benchmarks 87%; jevals.com 79.67% — **do not merge**) | gpt-oss-120b 81.3%; glm-5.3 80.4% |

Quality is not the reason to skip System One. Speed, cost, schema,
and the Choice cap are. Always re-run on *your* labels. Feedstock
for recomputing named boards: [`Jevals/jevals-data`](https://github.com/Jevals/jevals-data)
(CC-BY-4.0; `validation.md`).

Reject: TypeAR or pcdServer scores as fail-closed P(permit); a LoRA student's
agreement with Jev as independent gold; kev's ID ECE as a license to skip
a held-out test on *your* workflow; shipping on "smarter than Jev";
a green `/v1/systemone` smoke test on jev-local's stub as a bake-off;
copying laya-onnx or von vs-Jev rows as independent gold; treating von's
14 MB needle (52.6% authored144) or open-alternative-jev as a Jev
reproduction;
thresholding [`jp-sns-jev7-estimator`](https://huggingface.co/kokuren/jp-sns-jev7-estimator)
teacher scores as P(toxic) — the card says they are **not** calibrated,
and `threat` F1@0.5 is 0.0000 on their table (`notes.md` §33). Domain-local
ONNX distill is still categorize / score. Nimble's holdout is not a
universal ranking. Diffusion beating a decision head is Hypothesis.

Detail: `research/notes.md` §33 (surfaces), §34 (marginals), §35
(Nimble), §36 (diffusion), §38 (entropy allocator, Hypothesis),
§42 (pcdServer serving, meta-VOI, games), §45 (kev), §46 (blackwood,
laya-bench, decision-token LoRA), §48 (jev-local stub, laya-onnx),
§64 (gqgs complete Laya ONNX; local-jev not equivalence),
§49 (boundary map; DMB vs constrained LLMs; von; open-alternative-jev). Before
adopting a surface, the bake-off is a jevals-shaped suite and, for a
product loop, a Harbor taskset (`validation.md`, Eval & hill-climb).
The stage pipeline into that decision is the same file
(**Hypothesis**, `notes.md` §41). FAQ: open weights vs Jev vs TypeAR
vs encoder vs LoRA; is Jev probabilistic programming?

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

### "Perception specialist then judgment specialist" vs "Shared multimodal System One"

Two placements, not a slogan. Specialist composition stays **Hypothesis**
as a general recipe (Basit ask, primary post not retrieved; `notes.md`
§39). Shared multimodal *decide* now has a named open model:
[`BlackwoodAI/blackwood-rlcd`](https://huggingface.co/BlackwoodAI/blackwood-rlcd)
(**Empirical** as that vendor receipt, not re-run; **Hypothesis** on
*your* labels; `notes.md` §46). Not a SAM tutorial, not an ASR tutorial,
and not Archer's 27B drop (**Watch**).

[SAM 3.1](https://huggingface.co/facebook/sam3.1) is Meta Segment
Anything 3.1 ([release](https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md),
[blog](https://ai.meta.com/blog/segment-anything-model-3/)): promptable
masks and tracks (Object Multiplex). SAM and ASR are upstream
perception producers, not the perceive species: their output is a
mask, a track, or a transcript, not a score over candidates you
extracted. System One on the serialized objects or utterances is
**decide**. Composition ≠ one model. A public instance
of transcript-then-Jev, not the source of this ask:
[Moritz Kremb](https://x.com/moritzkremb/status/2100577979021832365)
(2026-09-17). His latency and price are his receipt, not a class
number.

**Information dies at the act.** Specialist composition: the decision
call sees the schema you serialized, not the pixels or the waveform.
Shared multimodal decide (blackwood): the call sees the screenshot
*and* the candidates **code already marked** (letters on the image);
it still does not invent a click. Prefer specialist composition when
you already have the producer; prefer a shared multimodal decision
model when the joint of pixels and options matters — you no longer
have to wait for Archer to place that hole. Archer Hume's drop stays
**Watch** (no Hub weights as of 2026-09-18; multimodal, no audio).
djev-spark already accepts images (multipart or JSON; think and
sequential reject images) on a *different* compute graph. A future
audio-capable shared model is the same hole, not this stack.

Same cut as a low/medium-entropy allocator: specialist state, then
typed decisions. Buckets are product rhetoric, not a meter, and
"review this PR" is still partly generative. One Jev call is still
factorized **marginals** (Meijer); blackwood's one prefill is still
not a joint over the raw waveform. The handoff is a contract surface
— one sentence in `formal-methods.md`. Code owns the schema and the
act. `notes.md` §39, §46. Measure and hill-climb in `validation.md`
(`notes.md` §41). Jev still leads blackwood on general *text* (0.850
vs 0.786 on their 8,456-item table) — omni is not a text free lunch.

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
- **Bake-off candidate** beside Laya, openjev-lm, TypeAR, and kev.
  Adoption still requires the eval path (`validation.md`, Eval &
  hill-climb). Archer stays Watch. Not a jevals how-to.

Serving, not copied: candidate logits, then softmax; one path shares
context across fields, another rescores each field; fields are
independent; text only; enum at most 26; prompts over 2,048 tokens
rejected. Probabilities normalize over the candidates you supplied —
the standing Choice-conditional-on-offered-set boundary (`SKILL.md`).
Add "no match" when coverage is open. A high probability is not a
correctness guarantee (their sentence).

### kev — runnable Archer reconstruction (not a distill)

[jaredpalmer/kev](https://github.com/jaredpalmer/kev) (Apache-2.0;
README, MODEL_CARD, LICENSE, and release
[v0.1.0](https://github.com/jaredpalmer/kev/releases/tag/v0.1.0) HTTP
200). LoRA + pointer readout on Qwen2.5-0.5B. Shared state, isolated
questions under a block-causal mask, one prefill, no decode.
Architecture follows [Archer Hume's reconstruction](https://archerhume.com/posts/jevs-architecture-unmasked).
Speaks TypeSafe `POST /v1/systemone`; official `typesafe-sdk` works
with a `base_url` change. Weights `kev-0.5b` (38 MB) on that release
**and** on the Hub as [`jaredpalmer/kev-0.5b`](https://huggingface.co/jaredpalmer/kev-0.5b)
(`kev.publish`; `--run` accepts Hub ids; base still downloads on first
load). PEFT `task_type=FEATURE_EXTRACTION`; publish patches legacy
adapters. Not a how-to: do not copy serve flags, ports, or train
commands. **NOTA:** training must confront Choice `"other"` as a wrong
alternative too, with varied wording (`notes.md` §45 delta;
`question-design.md`).

**Place it on the trained decision-only open path** next to Laya /
Nimble / Archer Watch. It is the cleanest *runnable* productization of
that reconstruction (API-compatible). Watch stays Watch: 27B,
multimodal, no Hub weights this pass. Not `Kevthetech143/super-jev`.

**Contrast** (same I/O shape, different graph / objective / duty):

- **vs TypeAR / pcdServer.** Constrained AR decode; softmax over
  allowed tokens is not a Noul. kev does not decode. Use TypeAR when a
  later field must see an earlier answer.
- **vs encoder open-jev (DeBERTa).** Bidirectional encoder, public
  gold, OOD drop measured (acc 0.854→0.690). kev is a causal decoder +
  pointer; OOD is unmeasured for this checkpoint.
- **vs proprietary Jev.** Documented cloud decision API, ~32k envelope,
  in-dist ECE 0.0313 with OOD collapse. kev is laptop-local, 0.5B
  knowledge, ID calibration only.
- **vs openjev-lm / jev-gate.** Those LoRAs copy a Jev *teacher*. kev
  trains CE on public labelled outcomes. Same 0.5B backbone, different
  gold.
- **vs Nimble.** 9B contrastive hard labels, no measured ECE, enum
  ≤26. kev publishes ECE and isolation probes.

**Evidence (README; not re-run).** Isolation exact: packed vs separate
max Δ 3.7e-6; secret-in-sibling p=0.03 vs in-state 0.99. Held-out ECE
0.065 (0.031 after temperature scaling); overall acc 0.799 on 1,350 ID
questions. Permute argmax flips 7.4%; IIA log-odds shift mean 0.13;
boundary forgery held. Honest limits: 0.5B knowledge; ID calibration
only; not multimodal. Model card: research prototype, not production,
not Jev.

**When to use.** Laptop-local System One API drop-in for development
and eval. Not a knowledge or frontier substitute. **Bake-off
candidate** on the jevals/Harbor path (`validation.md`); mechanism
tests (isolation, permute, IIA, boundary forgery) mirror Archer probes
— they falsify the reconstruction, they do not prove kev = Jev.
`notes.md` §45.

### blackwood-rlcd — open multimodal RLCD (not Archer, not CLIP)

[`BlackwoodAI/blackwood-rlcd`](https://huggingface.co/BlackwoodAI/blackwood-rlcd)
(Hub README this pass; CC BY-NC 4.0; `image-text-to-text`). Trained
decision-only readout with **image-in**. One prefill; option-letter
logits; temperature-calibrated; Jev-compatible `/v1/systemone` shim.
Screenshot + candidates **code already marked** → typed Choice; code
clicks. Not Archer's 27B drop. Not a vision-scorer affinity. Not a
commercial drop-in. Do not copy serve flags.

**Evidence (card; paired per item; not re-run).** Web element, 300
held-out: acc **0.907** vs Jev 1.13 text-only **0.480**; letter-shuffle
flip **0.133** vs **0.587**; ECE **0.037** vs **0.091**; ~**200 ms**
1×H100 vs 441 ms OpenRouter. General text, 85 sets / 8,456 items:
**0.786** vs Jev **0.850** — Jev still leads. Screenshot rows compare
screenshot input with Jev's text input on the same steps. Randomized
viewport crop. **Empirical** as that named receipt. **Hypothesis** on
*your* labels. Bake-off candidate beside kev / Laya (`validation.md`).
`notes.md` §46.

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
reward-hack gate, a different surface from this one, from GLiGuard,
and from Abide's project soft-rule Scores (`notes.md` §47).
Do not copy the hook install.

[pcdServer](https://github.com/stephanj/pcdServer) (MIT, C++20, created
2026-09-18T17:06Z) is **native serving for the same surface**: llama.cpp
GGUF on Apple Silicon and Linux; the model never writes JSON; the server
assembles allowed booleans and 2–256-wide string enums across 1–63
parallel fields after one prefix checkpoint. Softmax over allowed values
is still not a Noul. Collision trees resolve shared prefixes. Full
sequence checkpoints exist because Qwen3.5 hybrid recurrent state cannot
be partially rewound — an implementation fact, not a new species. Tetris
in the binary is a game-loop demo of the decode, not a strength claim.
No auth; default bind is loopback. Do not copy OpenAPI, flags, or
install. Same author's earlier `parallelConstraintDecoding` is the
two-forward-pass cousin already in the ecosystem snapshot.
`notes.md` §42.

**Decision-token LoRA (same graph, trained).** If you specialize a
pretrained generator for this surface, train **the single decision
token** under parallel constrained decoding — not generated prose.
[`Foodoo1/Qwen3-14B-RLCD-Decision-LoRA`](https://huggingface.co/Foodoo1/Qwen3-14B-RLCD-Decision-LoRA)
(Apache-2.0 adapter on Qwen3-14B): loss only on that token; one
prefill + KV broadcast across fields. Their held-out 200-case / 4-field
receipt: fraud_risk **64.0% → 95.0%**, overall **85.2% → 98.8%** at
**~234 ms** / broadcast on RTX 3090 4-bit. Synthetic fraud-triage;
do not use for real financial decisions. Softmax over allowed tokens
is still not a Noul. `notes.md` §46.

**Hypothesis, not a stack.** TypeAR's example names the same Qwen3.8-27B
family as Hume's announced weights. Running that surface (TypeAR or
pcdServer) on those weights versus stock Qwen is a composition to test
after the weights exist. Until then, **Watch** (`notes.md` §31, §32, §33,
§42).
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
