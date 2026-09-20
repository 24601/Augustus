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
| **Closed decision API** (TypeSafe Jev) | Calibrated decision (proper-scoring / RLCD lineage) | Choice / Score / Noul + distributions | Default when you need act/abstain, fan-out, documented envelope. **Productized public HTTP** (classifier.dev): label + calibrated confidence as the contract; batch `{id,text}[]`; LLM chains fallback only (`notes.md` §73) | Cloud, pin version, re-measure on your data. AU health data-residency is a reason *not* to pick this family (`notes.md` §33). Silent fallback is a lie about the instrument — mark `FALLBACK` |
| **Open System-1 / decision-model head** (Laya, openjev, LightJev, openjev-lm, Nimble, **kev**, **blackwood-rlcd**, Hume **Watch**) | Same *shape* as Jev, you host it | Same primitives or logits-as-options | Air-gap, $0/token, inspectable weights, deployment control; **image-in now** (blackwood) without waiting for Archer | Self-eval duty; Laya text-only, 512 tok; vendor vs-Jev tables are claims (`notes.md` §18). A distill learns the *teacher's* answers: openjev-lm and jev-gate-student-b (`notes.md` §25, §33). Nimble is an open LoRA recipe on hard labels, not a Jev distill (`notes.md` §35). **kev** is a shipped Qwen2.5-0.5B LoRA + pointer readout of Archer's reconstruction — public gold, not a Jev teacher; ID ECE only (`notes.md` §45). **blackwood-rlcd** is open multimodal RLCD (CC BY-NC), Jev-compatible shim; Jev still leads general text (`notes.md` §46). Hume's 27B dense drop is **Watch**, not a Hub checkpoint. He prefers the class name **decision models** over "system one" |
| **Encoder open-jev** (DeBERTa-v3-large) | Same *shape*, bidirectional encoder, public gold (not a Jev teacher) | Choice / Score / Noul from one pass | Self-host decide without a decoder; 512 tok | In-domain ECE 0.022; OOD acc 0.854→0.690. English / three public domains. `notes.md` §33 |
| **GLiFormer wire-compat encoder** ([jeff](https://github.com/logan-markewich/jeff) on gliformer-large-v1 400M) | Labels-in-encoder; System One *wire*, not a Jev replica | choice / score / noul via `/v1/systemone`; typesafe-sdk `base_url` | Self-host the envelope when you own the GPU path and accept the accuracy gap | Normalized sigmoids, T=3.2; isolate nouls; DeBERTa tokens ≠ Jev billing. L4 HTTP ~6× cheaper; A10G direct ~24×; AG News 75.5% vs 90.5% *theirs*. CPU is *more* expensive. License null this pass. **≠** GestaltLabs/Jeff-1 Qwen3-4B LoRA replica (`notes.md` §88). `notes.md` §60 |
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
  **≠** pi-jev-compact **≠**
  [zaycruz/fast-jev-compaction-pi](https://github.com/zaycruz/fast-jev-compaction-pi)
  (dedicated Pi port of tamaratran/fast-jev-compaction;
  `notes.md` §87). Augustus stays backend-agnostic. Mutating tools and shell operators
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
  **Native Apple locate runtime (Empirical as README + source
  comments, 2026-09-19 ~17:17 Boise; user-linked SIGNAL):**
  [gliner-native-runtime](https://github.com/shershah1024/gliner-native-runtime)
  (Apache-2.0; **4★**; HEAD `b44f661`) is unofficial
  Swift/Core ML inference for
  `fastino/gliner2.5-small-v1` (rev `cab1bddf…`) on
  Apple silicon ANE. **Not Fastino. Not TypeSafe. Not
  Choice/Score/Noul.** Entity spans + confidence;
  label descriptions as schema; on-device ANE
  economics; Python not needed for inference.
  Extraction path only (flat non-overlap + trained
  null/abstention). Default threshold 0.1 still soft.
  README `0.99` is a fixture, not Harbor. honesty
  locks. **≠** gliner25-compaction **≠**
  gliner2-ultrafast **≠** Eran-BA/Jev_from_GLiNER2
  **≠** NSStudent/JevSwiftSDK **≠** jevmlx
  (`notes.md` §97). Do not copy `swift build` / Git
  LFS / Hub weights.
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
  **OCR+AX desktop product (Empirical as README; MIT
  **427★**; 2026-09-19 ~09:51):**
  [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
  is the same observe→score-among-candidates→code-acts
  hole on a **Mac**, with **hosted TypeSafe Jev**, not
  GLiNER2 and **not** Cua-S1. Vision OCR (crop+tile) +
  AX → numbered items → three/four Choices
  (`kind`/`item`/`site`/`offscreen`) → deterministic
  click/type. **The decision never ships a screenshot
  to frontier.** The one-shot **answer** writer may
  receive the capture because OCR misreads — a reader
  packet, not the Choice. Overlapping options always
  read as doubt. AX is a bonus, never a replacement
  (Spotify 0 *theirs*). $0.0002 vs Opus $0.032 (155×)
  is *theirs* on **one screenshot**, not a Harbor
  taskset. 0.4 / 0.5 still soft. **≠** jev-ultrafast
  **≠** jev-macos-loop OmniParser **≠** camoufox
  **≠** blackwood-rlcd (`notes.md` §81). Do not copy
  `uv` / `.env`. Skip Archer.
  **ASR voice-browser product (Empirical as README; MIT
  **103★**; 2026-09-19 ~10:01):**
  [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
  is the same observe→score-among-candidates→code-acts
  hole with **ASR** as the producer: Web Speech
  transcript + numbered Playwright elements → hosted
  TypeSafe (9–11 questions) → code clicks. **Jev never
  generates.** Partial-speech wait is VOI. Spoken
  confirm is convenience, not auth. Numbered overlays
  disambiguate without another model. 27/27 fixtures
  *theirs*. **≠** jev-voice-control **≠** nikolas-j
  **≠** typesafe-computer-use OCR (`notes.md` §82).
  **Wrap-as-execution product (Empirical as README; MIT
  **2★**; 2026-09-19 ~10:20):**
  [AgentGhost](https://github.com/reddpy/AgentGhost)
  puts ALLOW/ASK/DENY *on the actuator path*. The
  model cannot skip the wrap. Rules first; ASK
  throws; fail-closed. Judge is a slot, not a
  vendor lock. **≠** actiongate (evidence ≠
  authority) **≠** toolgate **≠** jev-use
  fail-open. rh-guard owns the gate cousin
  (`notes.md` §83). Do not copy `npm` / `.env`.
  Skip Archer.
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
   something must be typed. **Receipt (ARCHITECTURE *theirs*):**
   [khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)
   sends **no graphical input** to either provider; sensors emit
   geometry; code never labels safest; planner narrative is
   excluded from Jev input (`notes.md` §80). **Receipt
   (README *theirs*):**
   [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
   never ships a screenshot to frontier for the
   *decision*; OCR+AX text-state → TypeSafe Choices →
   code clicks; writer only for free text; the one-shot
   answer reader may receive the capture (`notes.md`
   §81). Overlapping options = false low confidence.
   155× is one screenshot. **≠** jev-ultrafast **≠**
   cua-s1. **Receipt (README *theirs*):**
   [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
   never ships a waveform to Jev; ASR → transcript →
   Choices → Playwright; pointer spans; spoken confirm
   ≠ auth (`notes.md` §82). Compose with OCR, don't
   collapse. Hosted TypeSafe product APIs and prompted
   LocalJev are **not** a shared-prefix multimodal
   species. Skip Archer.
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
| Laptop-local System One API for development / eval | **kev** — trained decision-only readout; family 0.5B–8B; official SDK with a `base_url` change (`notes.md` §45, §98) | Treat 0.5B ID ECE as a knowledge or frontier substitute; treat kev family OOD 0.76–0.77 vs Jev 0.86 as identity; treat isolation 4e-6 or `/v1/systemone` wire as a Noul |
| Dynamic candidate bags (variable K per question) | Trained decision-only head whose object is `score(state, q, candidate_k)` then softmax over K (jev-forge class-architecture; `notes.md` §99). Not a new species | Treat as GLiClass categorize or TypeAR decode; clone Hub weights; paste 0.579/0.637 as Harbor; treat gut/judge as class-table species |
| Local NAR drop-in vs hosted Jev latency/cost | **von** late-catch (`notes.md` §99) ModernBERT-large `/v1/systemone`; measure ECE on *your* labels | Merge Needle 52.6% with n=78 93%; treat sub-15ms GitHub desc as the 62 ms table; dump weights; treat wire as a Noul |
| Constrained-AR local logits vs trained decision head | **snapjudge** softmax over allowed tokens ≠ Noul (`notes.md` §100); question-first cache; measure ECE on *your* labels | Treat softmax as a Noul; paste 87.7 vs 81.2 as identity; collapse into githubnext/localjev or Archer |
| On-device Laya CoreML vs GLiNER locate | **laya-coreml** ANE replica economics (`notes.md` §100); 189/189 FP16 checkpoint parity | Claim 10×; paste ANE P50 as “beats Jev”; collapse into gliner-native-runtime |
| Language primitive vs library overlay | **probably** (`notes.md` §100): Jev IS the if-statement; not hunch/feelings/gut/Judge | Collapse into tidymodels/probably; hard-gate `feels` 80% |
| Class bake-off on a public labelled set | **jev-vs-open-decision-models** frozen PROTOCOL (`notes.md` §101); Jev vs PrismNLI vs Laya; contamination caveat | Paste PrismNLI 0.725 as “wins the class”; treat remote p50 as local |
| OpenJev wire vs TypeSafe hosted | **live-rubric** OpenJev/Codiv (`notes.md` §101); scoring economics | Treat Codiv as TypeSafe hosted; quote only one of $0.000004 / $0.000006 |
| Unofficial BEAM class SDK | **system_one_sdk** (`notes.md` §101); GitHub desc provider-neutral; README TypeSafe-first | Collapse into typesafe_sdk or dannote/jev; treat as TypeSafe official |
| Lint the *question text* before a labelled run | **jevq** (`notes.md` §102); nine jaggedness rules, no API key, no labelled data; static lint ≠ measured separation | Collapse into tenbin / JevLint / commitjev; treat a clean run as measured separation; fail CI on a warn |
| Run OSS Laya inside Elixir | **laya_ex** (`notes.md` §102); Nx/Bumblebee runtime; host chooses backend | Treat as system_one_sdk or TypeSafe official; copy mix backends as recipes |
| On-chain / edge Laya inference next to a bounded canister | **IC-Laya** (`notes.md` §102); parity_verified stays false; model output never grants Tx | Treat 62 tests as Laya parity; let a Score grant Tx; claim ICP heap proof |
| Measure an open weekend student without teacher-copy | **jev48** (`notes.md` §102); Jev outputs never used for training; unpaired 0.577 vs 0.727 | Paste AUROC as a phishing win; treat 0.577 as identity; treat teacher-agreement gold as truth |
| Two judges, incomplete evidence, frame that separates | **ember** (`notes.md` §102); comparative framing is the usable judgment; prior injection crowds out evidence | Collapse into ember.js; inject class priors as help; treat v4 as a pharmacy controller |
| Non-LLM planning-depth System One | **jevon** VIN (`notes.md` §102); planning depth not chat | Collapse into douglance/jevon or Qwen-as-Archer; paste maze 1.00 as a knowledge-work certificate |
| Source-bound evidence then bounded Choice | **jev-kit** (`notes.md` §102); local quote mismatch needs no API; exit 0 ≠ claim truth | Treat matching quotes as proof; treat exit 0 as task success; copy curl\|sh |
| Keep receipts beside slogans; negative results first-class | **system-one-bench** (`notes.md` §103); scores not one leaderboard; no external record currently reproduced | Collapse into mallahyari; promote reported to reproduced; treat 62.4% as a class win |
| Score a typed-decision backend on a frozen item set | **SivletLabs/jev-eval** (`notes.md` §103); 21 tasks · 134 items · 208 questions | Collapse into willkelly / 4esv; treat constructed scenes as production logs |
| Option order as nuisance, not signal | **hev** (`notes.md` §103); option isolation (sibling-blind); permutation-equivariant | Paste 80.00% as Jev identity; publish Hub OWNER; collapse into kev |
| Typed decisions from frozen local logits | **yuki-oshio/mini-jev** (`notes.md` §103); frozen local LLM logits, no trained decision head | Quote 93.25% as family-disjoint; treat entropy-confidence as P(correct) |
| Do not turn a classifier into an LM | **ChatJev** (`notes.md` §103) is the anti-pattern | Jev classifier as autoregressive next-token predictor; ChatJev-style soundness theater |
| Compose scoring with proof search | **jev-alpha-proof-analysis** (`notes.md` §103); calibrated decision head × AlphaProof value head | do not launder Noul as proof; treat isomorphism as identity |
| Serial selection vs parallel rank-k | **jevsort** (`notes.md` §103); parallel rank-prediction vs serial selection | Treat independent questions as a permutation; collapse into jsort |
| Point at runnable open reproductions | **awesome-open-system-one** (`notes.md` §103); curated open System One ecosystem catalog | Paste listed von/4esv numbers; collapse into AnotiaWang |
| Knowledge-work relevance ranking | **paper-radar-jev** (`notes.md` §103); arXiv paper radar with Jev relevance scoring | ranking ≠ calibration / 0.5 still soft; mark failed evals seen |
| Train a decision head from scratch, not LoRA-on-LLM | **MiniSystemOne** (`notes.md` §104); typed Q→prob dist / one forward pass / no LLM decode; description-only stub / size 5 | Collapse hyusi into Colvin; treat the GitHub description as a checkpoint; paste Colvin 26.89M as hyusi |
| Re-measure ORDER BY on graded IR | **jev-orderby-bench** ESCI (`notes.md` §104); ESCI hard probe fails four of six | Re-fold §60 six-gates as new; treat 20NG pass as graded-IR safety |
| Inspect a workflow before the API | **jev-architect** (`notes.md` §104); find/design/evaluate TypeSafe Jev decision loops | Collapse into Augustus or samtay32/jev-system-architect; copy `npx skills add` |
| Do not distill Jev as teacher of record | **jev-distiller** stub (`notes.md` §104); Jairik/jev-distiller size 1 | Treat a size-1 UI as a student checkpoint |
| Score opportunities, then a human ranks TOP | **jev-opportunities** (`notes.md` §104); Jev self-scores then human curation | Treat self-scores as a product roadmap |
| Scaffold Choice/Score/Noul against an open classifier server | **jevinize** (`notes.md` §104); simple-jev not TypeSafe | Treat the scaffold as TypeSafe hosted; copy Featherless demo keys |
| Diff saved decisions against policy gates | **jev-diff** (`notes.md` §104); same label can still change the branch | Treat fixture exit 1 as a class regression; collapse into diffusiongemma-jev-macos |
| Constrained logprob ≠ trained Noul | **OpenJevPro** (`notes.md` §104); constrained logprob + temp/Platt ≠ Noul | Paste openjev-sglang JevBench as own; collapse into IamBusy/OpenJev |
| NAR heads on a tiny decoder | **jev-system-one-rlcd** (`notes.md` §104); SmolLM-135M / sub-70ms / 0 output tokens | Quote 2.1% ECE / 67 ms as Jev identity; collapse into rlcd-lite / blackwood |
| Source-backed radar, not a bake-off | **awesome-jev-projects** (`notes.md` §104); 306+ commit-pinned; auto GitHub sync | Paste listed numbers; collapse into AnotiaWang / yibie / cobanov |
| Rival-aware option scoring vs sibling-blind | **jevbetter** (`notes.md` §104); hashed n-gram encoder / rival-aware attention | Quote 0.916 as a class ceiling; treat as hev isolation (the opposite) |
| See the distribution, not the argmax | **jev-readout** (`notes.md` §105); structured probability readouts; Noul 0.5 midpoint; score is expectation not integer | Treat displayed p as proof; round Score to an integer |
| Keep Jev-shape on an ordinary model | **gulagala001/jevify** (`notes.md` §105); optional DSH plugin; schema-valid ≠ calibrated | Collapse into Mintzs/jevify; treat schema JSON as a Noul |
| Measure open Laya against a constant-answer | **laya-rlcd-benchmark** (`notes.md` §105); 40.3% below constant-answer | Quote 40.3% as “Laya is bad”; collapse into yibie/laya-jev-lab |
| Second semantic signal, fail-open | **jev-fastloop** (`notes.md` §105); cheap fail-open semantic edge; FastLoopError catch | Hard-gate fused confidence as safety; collapse into jev-ultrafast |
| Test packed fan-out | **jev-fanout** (`notes.md` §105); asking more questions in one call; 0.980 at every N | Treat 0.0000 sd as universal determinism; extrapolate to Score |
| Perceive ≠ decide ≠ deploy | **reflexrl** (`notes.md` §105); Qwen3-VL perception + Jev decisions train RL; 0 model calls at deployment | Ship VLM+Jev as the runtime; quote 2.95× as Harbor |
| Local-first cascade, not a hard gate | **laya-jev-lab** (`notes.md` §105); cascade 0.60 matches 78% at 1.8×; noul facts not judgements | Hard-gate 0.60; cite retracted n=4 order-bias |
| Locate vs decide | **zero-shot-ie-bench** (`notes.md` §105); GLiNER vs GLiFormer vs Laya vs Jev; extractors ≠ decision engines | Collapse locate into decide; quote 100% easy sentiment |
| Throughput, not intelligence | **snake-arena-jev-vs-llms** (`notes.md` §105); decisions-per-minute & cost; 204 moves vs 73 | Treat 21 points as intelligence; collapse into jev-plays-games |
| Pin the instrument, then eval the upgrade | **jevcheck** (`notes.md` §105); behavioral contracts; raw 0.94 is not a release | Treat exit 0 as world quality; collapse into jevals |
| Code owns facts; Jev scores relevance | **upgrade-radar** (`notes.md` §105); Jev never generates filenames; no_direct_evidence ≠ safe to merge | Treat no_direct_evidence as merge-safe; treat the fixture screenshot as live Jev |
| Knowledge-work discography categorization | **discoprint** (`notes.md` §105); discography theme/mood/complexity; five atomic questions one call | Treat theme Choice as a music-theory certificate |
| Probe any-open-LLM → System-One shape | **Jevify** (`notes.md` §106); Turn any open LLM into System-One Jev; description-only stub / size 0 | Treat the two-liner as a checkpoint; collapse into Mintzs or gulagala001; amend PR #23 |
| Train encoder-only from a task sentence | **exu-base** (`notes.md` §106); Exu is a toolkit, not a method; strictly proper scoring rule; Pre-alpha | Skip `--mode baseline`; treat Pre-alpha ECE as a proof |
| Use the from-scratch recipe, not the stub | **Colvin MiniSystemOne** (`notes.md` §106); typed Q → probability dists; 90.5 seconds / 29.2% pipeline evidence | Paste Colvin as hyusi; treat 26.89M tables as quickstart |
| Sentence → small serving head | **luce** (`notes.md` §106); init → synth → train → eval → serve; 91.1 % / ECE 0.022 *theirs* | Distill Jev as teacher of record; quote 91.1% as a class ceiling |
| Trial headline claims on local GPU | **jev-mini** (`notes.md` §106); 46x speedup / accuracy identical; ECE 0.624 sentiment catastrophe | Quote 46x as Jev identity; collapse into mini-jev |
| Local JSON structured choices | **tapsin/jev-local** (`notes.md` §106); JSON parse of generated text ≠ Noul | Treat JSON parse as a Noul; expand JEV as Journal Entry Voucher |
| Reward-model tracks as a class of jobs | **jev-reward-model-evaluation** (`notes.md` §106); RewardBench v1 92.58%; Precise IF 50.63% | Paste 92.58% as a class ceiling; call it Harbor |
| Geometric-mean typed-decision bench densify | **jevbench** v1.2.3 (`notes.md` §106); classifier.dev fast tier 84.8 is Jev behind its own API | Treat #1 as a better model; re-fold §78 as new |
| Code proves budget; Jev selects remainder | **ReflexRoute** (`notes.md` §106); hard budget filter before Jev | Let Jev do budget arithmetic |
| FSM proves transitions; Jev judges next state | **jev-state** (`notes.md` §106); Jev judges the next state, XState enforces transitions | Treat XState as Jev; treat synthetic fixtures as live calibration |
| Catalog gravity, not a bake-off | **awesome-jev-tools** (`notes.md` §106); ★339 live REST; curation is not endorsement | Paste listed as eval |
| Crawler directory, namesake lock | **RadRebelSam/awesome-jev** (`notes.md` §106); Daily GitHub + npm sweep, human-merged | Collapse into AnotiaWang / yibie / cobanov / logicrw / v-modal |
| Retrieval framed as Jev-class | **jev-reranking** HF (`notes.md` §106); query-side encoders, not a Jev replica | Treat SPLADE as TypeSafe Jev |
| Community ONNX scorer port | **system-one-qwen3.5-4b-scorer-ONNX** (`notes.md` §106); CC-BY-NC-4.0; temperature 1.75 | Treat AutoModel-cannot-load as a drop-in; re-card pngwn as new |
| Empty consistency protocol | **jev-consistency-benchmark** Space (`notes.md` §106); This Space contains no benchmark result yet | Treat the empty Space as a win |

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
| **kev** (Qwen2.5-0.5B LoRA + pointer; Apache-2.0) | Public gold, CE. Held-out ECE 0.065 (0.031 after T=1.47); acc 0.799 on 1,350 ID questions. Isolation exact. **Not** a Jev teacher-copy (`notes.md` §45). **Family delta (`notes.md` §98):** Archer-arch fidelity; kev family OOD 0.76–0.77 vs Jev 0.86; block-causal isolation; pointer/readout CE-trained; `/v1/systemone` drop-in; replica honesty | Laptop-local System One drop-in for development/eval; independent questions, one prefill. Family bake-off candidate, not a Jev substitute | ~160 ms / 6 questions; ~1h45m train on M5; 38 MB adapter. Family: kev-4b ~1 s / kev-8b ~2 s bf16 *theirs* | Self-host; official `typesafe-sdk` with `base_url` | Text. Not multimodal. 0.5B knowledge; 4B/8B OOD still a gap | noul / choice 2–255 / score |
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
**Independent open-Jev class (Empirical as their docs;
2026-09-19 ~03:38):**
[openvons](https://github.com/genai-craft/openvons)
(Apache-2.0 LICENSE; GitHub SPDX NOASSERTION; **7★**)
implements finite-choice+prob for LM / vision / voice
with a mandatory none-of-the-above and
execute/confirm/reject policy. Speaks
`POST /v1/systemone` so an SDK `base_url` drop-in works —
**wire-compat, not a TypeSafe replica** (same duty as
jeff / jev-local). JevPick is menu decode (3.2–4.8×
byte-identical *theirs*), not a Noul. Flutter on-device:
audio/image stay on the phone. Unrelated to TypeSafe; no
TypeSafe API output used. Archer still Watch
(`notes.md` §68). Do not copy `uv` / APK.
**Independent local OpenJev `/v1/decide` (Empirical as
their RESULTS.md; not a TypeSafe drop-in; 2026-09-19
~04:39):**
[OpenJev](https://github.com/IamBusy/OpenJev) (Apache-2.0)
is a 0.6B Qwen3 + LoRA + scalar head. Supervised CE +
held-out temperature — **not** RLCD, **not** a TypeSafe
replica. Hub `IamBusy/OpenJev-Branch-v0.3`. *Theirs:*
**45/60** vs v0.2 39/60; reversal 100% vs 68.75%.
`POST /v1/decide` is an OpenJev contract. Distinct from
[hraness/sysone](https://github.com/hraness/sysone)
"OpenJev runners" (loopback gateway). Do not copy `uv`
(`notes.md` §69).
**SemIf as `/v1/systemone` runoff (Empirical as their
latency table; wire-compat ≠ replica; 2026-09-19 ~04:39):**
[semif-serve](https://github.com/dddanielliu/semif-serve)
(pyproject MIT / GitHub SPDX null) serves SemIf behind
the Jev wire. No option ceiling (runoff). RTX 3080 Ti
Qwen3.5-4B **1164 ms** vs hosted Jev median **178 ms**
*theirs*. Confidence inferred for choice; runoff is a
product, not a single softmax; `output_tokens` always 0.
MiniCPM5-2B unusable. `--stub` needs no GPU. Same warning
as jeff / openvons / jev-local. Do not copy CUDA how-to
(`notes.md` §69).
**Competing NAR claims as an audit object, not a
swap (2026-09-19 ~06:43):**
[openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0)
(README Apache-2.0 / GitHub SPDX NOASSERTION) is a
149.6M ModernBERT-base NAR with Choice/Score/Noul and a
WebGPU demo. README *theirs* on
`LocalLLaMA/typed-decisions` N=2000: acc **77.10%** /
Brier **0.0636** / ECE corr **0.0144** / dist
**0.1513**. The TypeSafe Jev table row is a
Laya-catalogued vendor baseline, **not** an independent
run. Dual-channel ECE is a real design fork — and
**like-for-like is the rule**. Open PR #1 already
audits the launch write-up (throughput≠latency; Laya
gap inside CI → parity; Jev 14.40% slightly lower on
distribution ECE). **Do not endorse.** Distinct from
IamBusy/OpenJev `/v1/decide`, openvons, grande, and
openjev-lm. Do not copy train/serve how-to
(`notes.md` §71).
**Competing NAR agent engine — wire-compat vs
agent-routing as separate Harbor axes (2026-09-19
~16:52):**
[Cerebellum-2B](https://github.com/mkeco/Cerebellum-2B)
(Apache LICENSE / GitHub SPDX other; Hub
`mkzero/Cerebellum-2B-*`) is a Qwen3.5-2B NAR pointer
over caller-supplied candidates on `POST /v1/decide`
— **not** TypeSafe `/v1/systemone`. Claimed 94.92% vs
Jev 81.1% *theirs* is **unverified**; treat as an
audit object, not an endorsement (same discipline as
openJev-verdict-2.0). Wire-compat and agent-routing
are **separate** Harbor axes. mkeco GitHub ≠ mkzero
Hub. Do not paste a Cerebellum URL into typesafe-sdk
`base_url` (`notes.md` §87).
**Laya-class vision (SmolVLM; `score` untrained;
2026-09-19 ~16:52):**
[thaitea/laya-vision-smolvlm-256m](https://huggingface.co/thaitea/laya-vision-smolvlm-256m)
(CC-BY-NC-SA) + [r33drichards/laya-vision](https://github.com/r33drichards/laya-vision)
(Apache-2.0). Same `predict(state, questions)` API;
val n=8235 acc 75.2% ECE cal 0.034 *theirs*. `score`
is untrained. **≠** blackwood-rlcd **≠** Archer.
VQAv2 re-split is not published VQAv2 (`notes.md`
§87).
**Laya grounding tradeoffs — not a drop-in
(2026-09-19 ~16:52):**
[Luni/laya-grounded](https://huggingface.co/Luni/laya-grounded)
(CC-BY-NC; GitHub 404). Grounding improved; phishing
and routing-stability **regressed**. Platt, not
temperature. Entropy-confidence ≠ max_prob
(`notes.md` §87).
**1-token logprob local endpoint (constrained-AR
surface, not a trained head; 2026-09-19 ~07:49):**
[chakuho](https://github.com/taku-me/chakuho) (MIT)
serves `POST /v1/systemone` by reading one next-token
logprob over caller-enumerated labels (vLLM / Ollama
instruct). Softmax-over-labels **≠ Noul**. `coverage`
is format-mass, not correctness. GUI 336-case *theirs*:
27B **95%/92%** vs Jev Gateway **89%/82%**; `__none__`
gold 97% vs 8B 10%. Cousin jevify / TypeAR / pcdServer
/ jevmlx. Do not copy `uv run chakuho serve`
(`notes.md` §72).
**Open replica inference engine (argmax-parity
speedup, not ECE; 2026-09-19 ~07:49):**
[jevinf](https://github.com/zerodegress/jevinf) (MIT;
Python ≥3.14) runs NanoJev / decider-2b / Laya with
segmented forwards + prefix reuse, then the Jev wire.
Only `torch-mps` is wired. *Theirs:* **2.57×** /
**2.27×** at **100% argmax agreement**. Wire-compat ≠
TypeSafe replica. Do not copy serve/port
(`notes.md` §72).
**Laya multilingual class expansion (English checkpoint
confident-wrong OOD; 2026-09-19 ~07:49):**
[`laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual)
(Apache-2.0; mmBERT-base **322M**; 9 Hub likes). MASSIVE
51-lang *theirs*: **0.366 / 0.387 / 45 of 51** vs
English `laya` **0.227 / 0.733 / 23 of 51**. Khmer
**0.000 acc at 0.952 confidence**; mean conf never <
0.885 — **gating cannot catch it**. Route by script
before the forward pass. Ships uncalibrated (ECE
**0.314 → 0.106** after T *theirs*). Weaker on English
(0.619 vs 0.684) — route, do not replace. Sibling of
already-folded `laya-typed-decisions`. Do not copy
`pip install laya` (`notes.md` §72).
**Laya GitHub/PyPI packaging (not a new species;
2026-09-19 ~09:07):**
[`NandhaKishorM/laya`](https://github.com/NandhaKishorM/laya)
(Apache-2.0; **710★**). SDK + `Router` over the three
Hub checkpoints already watched. T4 *theirs*: 1q
**32.8 ms**; post-T ECE **0.081** vs Jev **0.246**;
Banking77 **0.425** vs Jev **0.870** (token budget;
72 vs 77 labels). typed-decisions **0.766** is a
fine-tune (base 0.362/0.342 vs majority 0.461). Jev
rows third-party unpublished-here. 0.85 gating is
*theirs*, still soft. **≠** TypeSafe `/v1/systemone`.
**≠** githubnext/localjev. Do not copy pip / preload /
`head_max_len` (`notes.md` §76).
**External openjev census (tweet, not a new species;
2026-09-19 ~09:14):**
[@airesearch12](https://x.com/airesearch12/status/2101259522933186879)
lists ~18 named openjevs including GLiNER2 and
routers. That is a **class-boundary**, not identity.
Incomplete vs Laya / githubnext/localjev / kev /
TypeAR / openvons. **≠** jevbench v1.1. Watch
[jev-models](https://benchmarkheaven.com/jev-models);
do not paste live ranks (`notes.md` §77).
**JevBench v1.2 scored class table (live board;
2026-09-19 ~09:24):**
[jev-models](https://benchmarkheaven.com/jev-models)
+ [`RESULTS-v1.2.md`](https://github.com/fstandhartinger/jevbench/blob/main/RESULTS-v1.2.md)
(SHA `fdfab1a2`). 15 systems × 534 decisions. Geo-mean
I/C/S/K; Jev **75.3** / SemIf **74.6** *theirs*.
Instruction models (Luna/Gemini/DeepSeek/Qwen3.8) sit
in the same table as NAR rebuilds — class-boundary is
the typed task. OpenJev on the board = razorback16
DiffusionGemma **≠** IamBusy `/v1/decide`. Laya
absent (gap). GLiNER2 mapping-excluded. Qwen3.8 27B
**≠** Archer. **≠** v1.1 87.6 (`notes.md` §78).
**Schema-conditioned DeBERTa scorer (Hub; GitHub 404;
2026-09-19 ~07:49):**
[`jev-schema-scorer-deberta-v3-large`](https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large)
(MIT; 4 likes). One scalar head per `(state,
question+candidate)`; **code** groups into
Choice/Noul/Score. v2 Choice **0.841** *theirs*
(chance 0.214). Peaked p = ranking, not calibration.
Distinct from com-kotobalabs/open-jev-deberta-v3-large.
Do not copy `schema_scorer.py` (`notes.md` §72).
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
equivalence; measured 2026-09-19 ~05:46):**
[`kunchenguid/local-jev`](https://github.com/kunchenguid/local-jev)
— ONNX ModernBERT-large-zeroshot-v2.0; "API-compatible
local approximation — **not** behavioral equivalence."
`confidence` omitted. 136 checkpoints *theirs*: done
**30%** / shape **57%** / Pearson r **−0.06** vs live
Jev; gold done 26% vs 87%; 112 min vs 21 s. Distinct from
jev-local's stub and jeff's GLiFormer. MIT (`notes.md`
§64, §70).
**GitHub Next prompted-JSON `/v1/systemone` (Empirical as
README + 1,200-request eval; 2026-09-19 ~08:56):**
[`githubnext/localjev`](https://github.com/githubnext/localjev)
— MIT; **261★**. Bun bridge: DiffusionGemma through
ordinary Chat Completions; TypeSafe SDK drop-in
(`jev-latest` / `jev-preview` aliases). **Wire-compat ≠
logit-equiv:** the model emits a JSON probability vector;
code validates/retries, normalizes, and computes
entropy-based confidence. OpenJev
([razorback16/openjev](https://github.com/razorback16/openjev))
reads logits via structured-read vLLM extensions.
**≠** [kunchenguid/local-jev](https://github.com/kunchenguid/local-jev)
(ONNX hyphenated namesake). **≠** IamBusy/OpenJev
`/v1/decide`. Bake-off *theirs* (prompted pipeline, not
logits): Qwen3.6 short macro **76.7%**; Gemma 4 26B-A4B
**75.0%**; DiffusionGemma **74.2%**; no definitive winner;
do not treat as calibrated. LM Studio cannot load
DiffusionGemma (18 Sep 2026). Do not copy bun / `.env`
(`notes.md` §75).
**Rust/WebGPU System One (Empirical as JGLUE + isolation;
2026-09-19 ~05:46):**
[`bokuweb/grande`](https://github.com/bokuweb/grande) —
Archer/kev-shaped shared-state branches; `POST /v1/systemone`.
JGLUE *theirs*: E2B zshot JNLI 0.614 ECE 0.252→0.088 T=2.81;
JCQA 0.853; trained 270M 0.710/0.710. Isolation sibling
0.098 / state 0.996. Packed Δmax 7e-5. License null. Softmax
≠ Noul until T. Not Archer Watch. Do not copy cargo
(`notes.md` §70).
**Clojure/Jolt Laya (Empirical as golden byte parity;
was empty skip §61):**
[`jlt-commons/laya-jolt`](https://github.com/jlt-commons/laya-jolt)
— Apache-2.0; README quickstart byte-identical to Python
`RLAgent.system_one`. ~1e-7 last-digit drift (f32 vs double).
~1.7 GB f32. Do not copy `jolt` (`notes.md` §70).
**CPU SemIf (Empirical as PoC UI, not a bench):**
[`leesk212/JEV-CPU`](https://github.com/leesk212/JEV-CPU) —
MIT; Qwen3-0.6B float32; option-letter logits, no generate.
Cross-ref semif-serve §69. **Meanblock/JEV-CPU 404.**
Softmax over slots ≠ Noul (`notes.md` §70).
**GLiNER2 decide adapter (spec only):**
[`Eran-BA/Jev_from_GLiNER2`](https://github.com/Eran-BA/Jev_from_GLiNER2)
— `fastino/gliner2-base-v1` → Choice/Score/Noul `/v1/systemone`.
No service, no training, no measurements. Interface ≠ replica.
Distinct from jeff GLiFormer (`notes.md` §70).
**Native Apple locate ≠ that spec (`notes.md` §97):**
[`shershah1024/gliner-native-runtime`](https://github.com/shershah1024/gliner-native-runtime)
runs GLiNER2.5-small spans on Core ML. It does **not**
speak Choice/Score/Noul. Eran-BA remains design-only.
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
**Tiny SAN local surface (extreme speed/econ class, not a replica;
§49 snapshot):**
[`wfzyx/von`](https://github.com/wfzyx/von) — 14 MB Needle; `POST
/v1/systemone`; sub-15 ms CPU *claim* / ~38 ms embed in their table;
authored144 needle **52.6%**. Distinguish from jev-local's **stub**
and kev's trained pointer. **Do not copy the vs-Jev ranking table.**
**Late-catch rewrite (`notes.md` §99; same repo, not a first
discovery):** GitHub description still says sub-15ms NAR local
drop-in (**43★** live REST). README this pass is Von-1.0 **395M
(1.5 GB)** ModernBERT-large; table ~**62 ms** MPS / ~**300 ms**
CPU on **n=78**; Hub
[`wfzyx/von-1.0`](https://huggingface.co/wfzyx/von-1.0) **10**
likes, lastModified 2026-09-19T22:38:37Z. Do **not** merge Needle
52.6% with n=78 93.0%. Two temperatures in one README (T=1.0367 /
T=1.1692); “guaranteeing” calibration is theater. NAR local
drop-in. open replica economics / latency vs closed Jev.
wfzyx/von late-catch HIGH. competing NAR claims / replica honesty.
Wire-compat ≠ Noul. Do not dump weights.
**Variable-N option scoring as the trainable object
(class-architecture note, not a sixth species; `notes.md` §99):**
[`zwliJay/jev-forge`](https://github.com/zwliJay/jev-forge)
(Python; GitHub NOASSERTION / LICENSE MIT; **1★**; HEAD
`eb3e4a2d`; README SHA `359f3f57`). Shared prefix + per-candidate
scalar head; softmax over that question's K. dynamic candidate
bags not fixed label sets. Contrast GLiClass (categorize a
changing *label schema*) and TypeAR (constrained decode at
*inference*, no trained decision head). zwliJay/jev-forge ≠
NanoJev. MODEL_CARD *theirs*: candidate discovery is the caller's;
not a browser-agent leaderboard. Do not clone Hub weights
([AndeyTait/JevForge-0.8B](https://huggingface.co/AndeyTait/JevForge-0.8B)
0 likes). Do not paste test/OOD choice top-1 0.579/0.637 as Harbor.
**GLiFormer encoder serving the System One wire (2026-09-18 ~20:43):**
[`logan-markewich/jeff`](https://github.com/logan-markewich/jeff) —
`knowledgator/gliformer-large-v1` 400M; official SDK `base_url`
drop-in; choice/score/noul. **Not a Jev replica.** Normalized
sigmoids, T=3.2; isolate nouls; DeBERTa tokens ≠ Jev billing.
Their card: L4 HTTP ~$2.6 vs ~$15.6 (~6×); A10G direct ~$0.65
(~24×); AG News 75.5% vs 90.5%; CPU 6–20× *more* expensive.
License null this pass. Do not copy uv / Modal (`notes.md` §60).
**Open LoRA replica, different jeff (2026-09-19 ~17:25):**
[GestaltLabs/Jeff-1](https://huggingface.co/GestaltLabs/Jeff-1)
(Apache-2.0; **4 likes**) +
[Gestalt-Lab/jeff](https://github.com/Gestalt-Lab/jeff)
(**0★**; README SHA `bbf66409`) — Qwen3-4B LoRA on
Qwen3-4B-Instruct-2507; first-token or whole-sequence
label scores; confidence = max label p; optional `POST /v1/systemone`. **Not a Jev replica.** README
*theirs*: API compatibility ≠ identical judgments.
n=9730 fact-check vs Jev 1.13.0: acc **0.8183** ECE
**0.0807** vs **0.8283** / **0.0932**. Acc/Brier lose;
ECE wins; set reused for error analysis. Weak on
`not_enough_info`. **≠** logan-markewich/jeff GLiFormer
(§60). **≠** anima3's jeff backend. Soft Noul ≠ hard
safety (`notes.md` §88).
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
**Productized Apple Silicon one-pass (Empirical as README
library, not a bake-off; 2026-09-19 ~01:47):**
[`bnsd55/jevmlx`](https://github.com/bnsd55/jevmlx) — MIT;
**28★**. Schema of booleans/enums/multi-selects → JSON
valid by construction, probability per field, one batched
MLX forward pass. Not TypeSafe Jev. Softmax ≠ Noul. No
local leaderboard yet (official 67.8% cited). OpenAI-compat
backend is one request per field. Distinct from
system-one-benchmark's n=50 Brier table. Do not copy pip
(`notes.md` §66).

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
§70 (grande / laya-jolt / JEV-CPU / local-jev measured /
GLiNER2 spec),
§75 (githubnext/localjev prompted JSON ≠ structured
logit read; ≠ kunchenguid/local-jev),
§76 (NandhaKishorM/laya packaging ≠ new species;
Router script-before-p; vs-Jev unpublished-here),
§77 (@airesearch12 census ≠ scored bake-off;
GLiNER2+routers class-boundary; incomplete vs watch;
≠ jevbench v1.1),
§78 (JevBench v1.2 geo-mean I/C/S/K; cal ON rank;
Jev 75.3 / SemIf 74.6 *theirs*; instruction models
in the table; Laya absent gap; ≠ v1.1 87.6),
§71 (openJev-verdict-2.0 competing NAR as claim-audit ≠
IamBusy/OpenJev),
§87 (laya-vision SmolVLM `score` untrained ≠ blackwood ≠
Archer; Cerebellum-2B `/v1/decide` ≠ TypeSafe — wire-compat
vs agent-routing as separate Harbor axes, competing NAR
not endorsement; laya-grounded not drop-in / phishing
regress / Platt not temperature; anima3 Qwen logprob
default, jeff confidently flat, do not invent Laya),
§88 (GestaltLabs/Jeff-1 LoRA Qwen3-4B ≠ logan-markewich/jeff GLiFormer; acc/ECE tradeoff n=9730 *theirs*; set reused),
§89 (feelings / apa / grok-bot-jev / Essentiel / enzo-mcp / pigeonhole / playground / jev-reliability / clduab11/jev-test / jev-rag-benchmark / dairui1/jev-lab / jevmail / mailjay — placements, not new species),
§90 (ZHUBoer/ego-jev namesake lock; jsort ranking ≠ calibration; groundedness native vs schema-guided; jev_playground 0 promotions; yuyang2230/jev-agent-skill jev-1.13-free; jev-techstack-classifier stack_config.json; s1_ruby collapse late; 2389-research/judgement license null; confidence ≠ winner p; typesafeai-sdk-community not a new species; tpellet/hunch exit 3; jevbrain AUTO_ACT is not a Noul — placements / unofficial packaging, not new species),
§91 (judgekit YAML classify/score/route/verify; typed-judge-kit verdict-in-code; alsoleg89/decide packing VOI; Jev-Calibration Platt ECE 0.117→0.052; jev-calibration-arena never acts; ctmx/openrouter-jev-mcp Decision-as-Plugin; FrancoisChastel/jev-code ≠ npm jev-code; claudecode-jev-marketplace fail-open not hot path; pedroknigge/mcp_jev packs not ask_jev; cyrusasco/typesafe-mcp noul deadband 0.35–0.65; codaaiteam/jev-skill jevtypesafeai.com ≠ TypeSafe; hermes-switchyard ≠ hermes-jev-router ≠ hermes-plugin-jev; nanoprune 2.8MB ECE 2.58%; smartdio/jev-browser-agent ≠ ZHUBoer/ego-jev; Dakai/omp-jev-web DONE ≠ proof; hari007sh/jev ≠ dannote/jev; 0thernet/system-one-skills deterministic verify; typed-gate band [0.40,0.60] is refusal; pi-jev-gate fail-closed; choice is the verdict — placements / unofficial packaging, not new species),
§92 (Foq ~25ms/2.2GB local; rev prefill-only + HF jev-0.5b; robfrase/jev planning memo; meldltd/meldecision laya-go ONNX; laya-doom never pixels; logixism/laya-api empty README; akpsahan/laya ≠ Archer; Nibir1/typesafe-go ≠ official — packaging / Hub copy, not new species; Qwen3.8 27B ≠ Archer),
§93 (hyperspaceai/jevcache decision ledger / memoization ≠ kushals256/jevcache same-intent admit ≠ Hyperspace KV attention cache; sutro-sh/jev-align GEPA alignment loop ≠ caiovicentino/jev-align verifier — placements, not new species),
§94 (byenzyme/enzyme compile-time System One / catalysts ≠ summaries / guidance ≠ hook / hosted bootstrap ≠ silent TypeSafe; argos1111/modernbert-ja-310m-jev unofficial ≠ TypeSafe / format_version modernbert-jev/1; Argos1111/jev_local ≠ us/jev-local ≠ kunchenguid/local-jev / LFM default ≠ ModernBERT backend; pst2154/Nemotron_Jev ≠ TypeSafe / not a calibrated replacement; Davipar/djev-dev complements djev-spark / images as Choice options; Laya essay ≠ new species / Router/OOD confidence — placements / unofficial packaging, not new species),
§95 (llama-jev llama.cpp replica; numbered-choice softmax ≠ Noul; **≠** TypeSafe **≠** pcdServer **≠** chakuho; 80 ms cold / 40 ms cache *theirs* on minicpm5-2b-q8; packaging / WIP replica, not a new species),
§96 (indiejoseph/opencode-jev-pruner OpenCode host-port of tamaratran/jev-pruner; jev-zen / jev-1.13-free; zen-chat ≠ Noul; **≠** nrdz-labs/fast-jev-opencode; Kiln-AI/jev_jsonschema / NSStudent/JevSwiftSDK unofficial packaging, not new species; jev-webagent-bench empty stub),
§97 (shershah1024/gliner-native-runtime GLiNER2 native Apple path; unofficial Swift/Core ML GLiNER 2.5-small; entity spans + confidence; not Choice/Score/Noul; not TypeSafe; label descriptions as schema; on-device ANE economics; honesty locks; shershah1024/gliner-native-runtime ≠ Fastino; ≠ gliner25-compaction ≠ gliner2-ultrafast ≠ Eran-BA/Jev_from_GLiNER2 ≠ NSStudent/JevSwiftSDK ≠ jevmlx; default threshold 0.1 still soft),
§98 (numerous-com/dgp Decision Graph Protocol frame→assess→commit; app retains permissions/effects; Jev-first assessor-neutral; guarded commit / receipt/next frame; assessment batching; hard-gating DGP as safety theater; numerous-com/dgp ≠ TypeSafe official; can1357/jegrep calibrated path+range Nouls; no embeddings/index/daemon; ~$0.01–0.03 typical; agent --json; can1357/jegrep ≠ Bentlybro/jevgrep ≠ uehaj/jev-semgrep; jaredpalmer/kev family Archer-arch fidelity; kev family OOD 0.76–0.77 vs Jev 0.86; block-causal isolation; pointer/readout CE-trained; /v1/systemone drop-in; replica honesty — do not rewrite §45),
§99 (Kungie/gut cost-derived YES/NO/UNSURE overlay, not a species; Illusion47586/judge typed-callback twin, not a species; zwliJay/jev-forge variable-N option scoring as the trainable object, not a sixth species; wfzyx/von late-catch HIGH — Needle snapshot ≠ 395M table; competing NAR claims / replica honesty; ishaannk/llm-vs-jev cross-note only; deeper integrity fold is rh-guard; gut/judge are control-flow overlays),
§100 (southpolesteve/probably language primitive — Jev IS the if-statement — not an overlay and not tidymodels/probably; sutro-sh/jev-align 133★ live delta of §93, not a new mechanism; samdotmak/jev-recall retrieve by relevance not resemblance, not a new species; chopratejas/invalidate HIGH upgrade, six Nouls then fixed rules in code; mizchi/jev-lint is mizchi/jevlint rename, not a second product; Kiln-AI/jev_jsonschema HIGH upgrade, noul_threshold 0.5 decoder not a proof; mizorewww/laya-coreml on-device Laya CoreML ANE, not a new species; Micha0827/snapjudge softmax over allowed tokens ≠ Noul; direwolfiy/JevPi Jev-first Pi agent loop, not jevpilot),
§101 (natemoo-re/bias-bench resume-screening bias audit methodology, not BBQ; austindixson/planalyzer code-owned panel, not a species; cannacre8ive/switchboard-ai cost-aware routing overlay, not ha-switchboard; elcronos/jev-vs-open-decision-models frozen-protocol bake-off, not JevBench/DMB; cvsgireesh/jevusher VOI admission, not jev-sift/winnow; MokiMeow/jev-fabric typed control plane, not jev-forge/dgp; jose-troche/live-rubric OpenJev/Codiv ≠ TypeSafe hosted; willkelly/jev-evaluation pre-registered science, not jevals; nshkrdotcom/system_one_sdk class infrastructure, not typesafe_sdk/dannote/jev),
§102 (yodablocks/jevq question-linting of Jev questions themselves, not tenbin/JevLint; ChristianAlexander/laya_ex open-weights Laya binding, not system_one_sdk/dannote/jev; humandebri/IC-Laya on-chain/edge deploy, parity_verified stays false, model output never grants Tx; agilabs-ai/jev48 auditable weekend replica, Jev outputs never used for training, unpaired 0.577 vs 0.727; copyleftdev/ember adversarial dual-judge / framing, not ember.js; PIXELZX0/XERON Laya specialist FT, training still GPU-pending; daliborsb/laya Hub replica drop, not a new species; MagaBitmex/jev-4b-distill-data student corpus, gold is programmatic, teacher is closed-API clone, do not distill Jev as teacher of record, student checkpoint missing; lewislululu/jevon non-LLM VIN System One, planning depth not chat, ≠ douglance/jevon; WaynezProg/jev-kit source-bound evidence, local quote mismatch needs no API, exit 0 ≠ claim truth, ≠ jonathanavis96/jev-kit Airlock),
§103 (reachjalil/system-one-bench independent System One evidence catalog, 19 reviewed records, scores not one leaderboard, no external record currently reproduced, TokenTrim no-Jev matched hybrid 62.4%, ≠ mallahyari/system-one-benchmark; SivletLabs/jev-eval 21 tasks · 134 items · 208 questions, scenes from public GitHub contracts, not production logs, ≠ willkelly/jev-evaluation ≠ 4esv/jev-eval; nafisazizir/hev option isolation (sibling-blind), permutation-equivariant, Hub OWNER not published, ≠ jaredpalmer/kev; yuki-oshio/mini-jev frozen local LLM logits, no trained decision head, residual-head 9,222-param decreased 73/96→67/96, confidence = 1−normalized entropy, not P(correct), ≠ r-ms/mini-jev; erik-dunteman/ChatJev Jev classifier as autoregressive next-token predictor, ChatJev-style soundness theater, ≠ dannote/jev ≠ jev-gpt; wufuju2023-cell/jev-alpha-proof-analysis calibrated decision head × AlphaProof value head, implementation-layer isomorphism, semantic difference, timeout = censoring, do not launder Noul as proof; zzzzzec/jevsort parallel rank-prediction vs serial selection, independent questions can conflict, ≠ keltokhy/jsort; rupeshpoojary9/awesome-open-system-one curated open System One ecosystem catalog, ≠ AnotiaWang/awesome-jev; LYchoon/paper-radar-jev arXiv paper radar with Jev relevance scoring, ranking ≠ calibration / 0.5 still soft, fail-open failed evals not marked seen),
§104 (hyusi2003/MiniSystemOne train calibrated ~27M from scratch, typed Q→prob dist / one forward pass / no LLM decode, ≠ Colvin0315/MiniSystemOne, description-only stub / size 5; yodablocks/jev-orderby-bench ESCI hard probe fails four of six, jev_bool ECE 0.242 inversion 0.255, do not re-fold §60 six-gates as new; karanb192/jev-architect find/design/evaluate TypeSafe Jev decision loops ≠ samtay32/jev-system-architect; Jairik/jev-distiller size 1, distill-Jev UI stub / do not distill Jev as teacher of record; licensedsaucer9-web/jev-opportunities post-launch scored use-case map / Jev self-scores then human curation; gavinHuang/jevinize → simple-jev not TypeSafe; VihaanAgarwal/jev-diff compare saved decisions / same label can still change the branch, not tested with a live Jev API key; zhangcy122/OpenJevPro constrained logprob + temp/Platt ≠ Noul, pastes openjev-sglang JevBench as own, PolyForm Noncommercial ≠ IamBusy/OpenJev ≠ ekzhang/openjev-sglang; patelvishwa112/jev-system-one-rlcd SmolLM-135M / sub-70ms / 0 output tokens, demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055, README claims MIT / GitHub license null / no LICENSE file ≠ arnabgho/rlcd-lite ≠ blackwood-rlcd; logicrw/awesome-jev-projects source-backed Awesome Jev radar / 306+ commit-pinned ≠ AnotiaWang/awesome-jev ≠ yibie/awesome-jev ≠ cobanov/awesome-jev ≠ rupeshpoojary9/awesome-open-system-one; olanotolu/jevbetter hashed n-gram encoder / rival-aware attention vs jevlike starter, synthetic hard menus top-1 0.916 vs 0.873 / ECE 0.0182 vs 0.0367 / 40 vs 4608 menus/sec, shuffled-context control 0.335),
§105 (Arohtea/jev-readout structured probability readouts, distribution > argmax, Noul 0.5 midpoint, score is expectation not integer, bare HTTP not SDK; gulagala001/jevify Jev-style Choice/Score/Noul from ordinary models, optional DSH plugin, schema-valid ≠ calibrated, ≠ Mintzs/jevify; mourad-ghafiri/laya-rlcd-benchmark Laya RLCD benchmark, 40.3% below constant-answer, open-weight measurement, ≠ yibie/laya-jev-lab; SupremeDreamZ/jev-fastloop cheap fail-open semantic edge, second signal not sole, FastLoopError catch, ≠ jev-ultrafast; TheWebDevel/jev-fanout asking more questions in one call, 0.980 at every N, nearly not fully deterministic; harneet2512/reflexrl Qwen3-VL perception + Jev decisions train RL, 0 model calls at deployment, VLM alone 1.7 vs +Jev 4.4, ≠ khordoo/jev-reflex-autonomy-lab; yibie/laya-jev-lab independent Jev API vs Laya, cascade 0.60 matches 78% at 1.8×, noul facts not judgements, ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab; umstek/zero-shot-ie-bench GLiNER vs GLiFormer vs Laya vs Jev, extractors ≠ decision engines, Laya dict-instructions collapse 58.3%; angelgalvisc/snake-arena-jev-vs-llms decisions-per-minute & cost, 204 moves vs 73, throughput not intelligence, ≠ vtrivedy/jev-plays-games; sathariels/jevcheck behavioral contracts, pin expectations eval upgrades, raw 0.94 is not a release, ≠ dayhaysoos/jevals ≠ SivletLabs/jev-eval; GaneshVG18/upgrade-radar evidence-linked dependency upgrade, Jev never generates filenames, no_direct_evidence ≠ safe to merge, ≠ LYchoon/paper-radar-jev; lirantal/discoprint discography theme/mood/complexity, five atomic questions one call),
§49 (boundary map; DMB vs constrained LLMs; von Needle snapshot; open-alternative-jev). Before
adopting a surface, the bake-off is a jevals-shaped suite and, for a
product loop, a Harbor taskset (`validation.md`, Eval & hill-climb).
The stage pipeline into that decision is the same file
(**Hypothesis**, `notes.md` §41). FAQ: open weights vs Jev vs TypeAR
vs encoder vs LoRA; is Jev probabilistic programming?
§105 (uspraveen/Jevify Turn any open LLM into System-One Jev, ≠ Mintzs/jevify ≠ gulagala001/jevify, Jevify-any-LLM architecture probe, description-only stub / size 0, do not reopen or amend PR #23; Ruivalim/exu-base Train encoder-only calibrated decision models from a task sentence, Exu is a toolkit, not a method, strictly proper scoring rule, Pre-alpha; Colvin0315/MiniSystemOne scratch-trained calibrated decision model, typed Q → probability dists, ≠ hyusi2003/MiniSystemOne, no published weights download URL, 90.5 seconds / 29.2% pipeline evidence, p_i/p_j independent of other candidates; scienthoon/luce Recipe for calibrated decision models — small model out, init → synth → train → eval → serve, 91.1 % / ECE 0.022 *theirs*, Jev zero-shot 75.1; RichardoMrMu/jev-mini Put Jev's three headline claims on trial, 0.5B local GPU, 46x speedup / accuracy identical, ECE 0.624 sentiment catastrophe, bigger model worse calibration, ≠ yuki-oshio/mini-jev ≠ r-ms/mini-jev; tapsin/jev-local System-1 decision engine for local LLMs, structured choices only, JSON parse of generated text ≠ Noul, TypefAI JEV / Journal Entry Voucher, ≠ us/jev-local ≠ Argos1111/jev_local; goya4140/jev-reward-model-evaluation Jev 1.13 reward-model eval across 8 benchmark tracks, 40,940 examples / 0 API errors, RewardBench v1 92.58%, Precise IF 50.63%; SarathChandraBellam/jev-vs-llm-ticket-router Jev vs LLM support-ticket routing, Scaffolding in progress; Shilin237/jev-vs-llm-cost static + live decision bench, TypeSafe's own published benchmark, illustrative simulations, not live API calls; fstandhartinger/jevbench JevBench v1 — smart/cheap/fast/reliable, I/C/S/K 25% geometric mean, classifier.dev fast tier 84.8 is Jev behind its own API, do not re-fold §78 v1.2 board as new, Laya (421M) 70.1 now on board; AIGNLAI/ReflexRoute Zero-shot/few-shot LLM routing, hard budget filter before Jev, Jev never asked to perform budget arithmetic; priyankark/jev-state Jev judges the next state, XState enforces transitions, simulation uses synthetic keyword fixtures; v-modal/awesome-jev-tools catalog gravity, ★339 live REST, curation is not endorsement; RadRebelSam/awesome-jev crawler-maintained directory, Daily GitHub + npm sweep, human-merged, ≠ AnotiaWang ≠ yibie ≠ cobanov ≠ logicrw ≠ v-modal; rdxtremity/jev-reranking HF peft SPLADE/BGE reranker, ≠ carlaiau/jev-reranking, query-side encoders, not a Jev replica; onnx-community/system-one-qwen3.5-4b-scorer-ONNX ONNX System One Qwen3.5-4B scorer, source:pngwn/system-one-qwen3.5-4b-scorer, CC-BY-NC-4.0, temperature 1.75, transformers.js AutoModel cannot load this graph; mjyoke1111/jev-consistency-benchmark Consistency benchmark Space, This Space contains no benchmark result yet, 12-case plumbing fixture),
§49 (boundary map; DMB vs constrained LLMs; von Needle snapshot; open-alternative-jev). Before
adopting a surface, the bake-off is a jevals-shaped suite and, for a
product loop, a Harbor taskset (`validation.md`, Eval & hill-climb).
The stage pipeline into that decision is the same file
(**Hypothesis**, `notes.md` §41). FAQ: open weights vs Jev vs TypeAR
vs encoder vs LoRA; is Jev probabilistic programming?
§107 (erendikmenn/jev-llm-router-benchmark Benchmark-driven Jev router and judge, cheap alone is not success, Jev does not write, sum prices, or claim accuracy %, Sol 94.2 / Luna 83.9 / Jev path 89.7, 19.2% Sol / 62.3% cost save / 4.5pp miss of 2pp non-inferiority, p50 latency worse than Sol due to routing overhead, ≠ jev-rag-benchmark ≠ ryantsai/jev-llm-router; aesaganda/jev-ticket-router Express + node:sqlite, mock and Jev decision engines, previous_ticket_count >= 3 is code, MIN_CONFIDENCE 0.6 still soft, substring false positives, ≠ SarathChandraBellam/jev-vs-llm-ticket-router; hoangngochuong24947-gif/jev-figure-router Universal Figure & Diagram Router, confidence ≥ 0.85 hard-gate is theater, generative AI banned from scientific plots, six visual branches; Praveenrajus/jev-bench human-labeled (state, question, label), 166,054 rows / 22 configs, soft_label for human uncertainty, ≠ fstandhartinger/jevbench; NicolaiMTLassen/open-bonzi-jev ternary bonsai System One GGUF, openjev's mechanism, Bonsai's weights, Hub does not ship weights, 100/100 easy T/F is not Harbor, label_mass ≠ correctness, stock llama.cpp Q2_0 silently gibberish, ≠ NicolaiLassen; onnx-community/open-jev-deberta-v3-large-ONNX transformers.js DeBERTa ONNX, source:com-kotobalabs/open-jev-deberta-v3-large, temperature 1.05, AutoModel from_pretrained works, ≠ system-one-qwen3.5-4b-scorer-ONNX; Heman10x-NGU/openJev-verdict-2.0 107★ densify, GH 151M vs README 149.6M, PR #1 now closed unmerged, do not re-fold §71 claim-audit as a beat; wjdjdakf17/jev-study typed decisions, RLCD, confidence-gated routing, structured ≠ correct, mock not live API, 26 tests, ≠ baekenough/jev-study, do not reopen or amend PR #23 or #24),
§108 (NicolaiMTLassen/bonzi-27b-v2-jev bonzi-27b-v2 / ternary-8b / 27b-v1 GGUF family densify, WANLI-256 74.6% / 65.2% / 71.1% *theirs*, Bonsai 1 27B Q1_0 runs on stock llama.cpp, ternary still needs PrismML fork, Hub still does not ship weights; mizchi/laya-multilingual-onnx Laya multilingual ONNX WebGPU typed-decisions port, 63/63 selected answers / 5.1e-4 CPU / 1.2e-2 WebGPU; IamBusy/OpenJev-Vision OpenJev Vision image classification + uncertainty, CLEVR-4 held-out joint 0%; heman10x/openJev-verdict-2.0 twin tokenizer-only, likes **5** ≠ GH **107★**; IamBusy/OpenJev-Vision-Research-v0.1 12,832, 294,912 derived targets not independent samples; UpHash-Network/mini-jev is yuki-oshio transfer, residual-head 9,222-param decreased 73/96→67/96; ASEVlad/jev-injection-bench 11,900 labelled prompts, Jev best ranking / Haiku better ECE 0.021 vs 0.058, 0.5–0.9 band is where Jev's numbers do not mean what they say, Prompt wording moves panic 28%; manojlds/jev-dspy-bench ≠ dspachos/jev-dspy ≠ jmanhype/jev-dspy-lab, Jev agreement is similarity, never ground truth, no aggregate quality grade or merge gate; sshariqali/jev-abstentionbench AbstentionBench-on-Jev rank 1 of 20 vs 2025 field, question-asymmetry, forward-looking 0.465 never extreme; misakaikato/openkev calibration layer not a runtime, ECE vs coverage independent, select_threshold returns inf, escalation catches uncertainty not ignorance, ≠ jaredpalmer/kev; goodrahstar/pdf-race Docling→Jev vs Gemini, parser owns the wall clock, 12/12 tie is a tie, titles selected not generated; ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas, catalog not endorsement; samyakjain0606/jev-is-here flopcheck 16 calibrated tweet judgments, mechanical tells in code; BunsDev/laya-calibration-lab Laya calibration lab Gradio MCP, T never changes argmax, confidence ≠ top-label p, easy probe set refused, 40–48 rows too small to ship T, do not reopen or amend PR #23 or #24 or #25),
§109 (kushalpatil/jevify-gemma4-26b-a4b Gemma-4 26B-A4B jevify classification+calibration, Hub jevify merged LoRA ships weights, PAWS 0.580/ece 0.288 is the weak cell, ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify, GH kushalpatil07/jevify 404; LoRA adapter twin not independent eval; Gemma-4 E4B jevify, smaller E4B slightly better OOD ECE than 26B-A4B; E4B LoRA stub card; NicolaiMTLassen/bonzi-8b-v1-jev bonzi Bonsai-8B v1 GGUF densify, Bonsai-1.7B v1, Bonsai-4B v1, WANLI-256 64.5% / 60.2% / 52.0% *theirs*, rank #4 / #5 / #6 of 6; JulesHuisman/jev-eval scaffolding / README SHA c356a584 (was empty e69de29b), ≠ SivletLabs/jev-eval ≠ willkelly/jev-evaluation ≠ 4esv ≠ xxkuboxx ≠ onlyoneaman ≠ dayhaysoos/jevals; LiuHao-1443/jev-table-tennis 7 bands 6/10 vs 40 bands 0/10; laguagu/jev-evidence-lab source receipts + confidence slider re-policy without re-inference, 32/32 synthetic is smoke not production; hemanth/hfjev classify HF datasets across typed semantic dimensions; roadus2 watch misspelling; lock roadius2/ultra_laya, ultra_laya REVIEW defects, default branch claude/laya-jev-review-gg5ppo; AHTOOOXA/jev-cyrillic-audit XNLI EN 88.3% ECE 0.032 → RU 77.3% ECE 0.096, Δ −11.0 pp [−14.2,−7.8]; ECE +0.063, MASSIVE no detectable difference at n=600, confidence is function of p_max (r=1.000); akash-kamat/jev-llm pointer-not-generator 400 human-authored responses; chenmingtang830/jevgraph proposed ≠ authorized, FewRel 160: Jev 85.0% vs lexical 13.125%, gated 100% (95/95) coverage 59.375%; Towow-ai/jpp J++ composable semantic computation language; Mishkun/judge-jev 0.5 still soft; tunahansahin897/what-is-jev 947 repos scored; A 273 / B 302 / C 372, LLM rubric ≠ benches; whyashthakker/awesome-jev-use-cases No benchmark winner is claimed; dog-last/awesome-jev phishing: naive 62.6% vs regex 91.8%; 5-atomic + LR 95.0% *theirs*; shinshin86/jev-aituber-tension-sample AITuber tension ±15; shinpr/jev-reranker README npm global; repo is Rust; AHTOOOXA/git-confess code owns counting/blame/ratio, httpx exhibit 11% (13/119) *theirs*; waterme7on/jev-paper-trader 90d trend +12.40% vs random +12.75% vs BH +41.71%, 5m win rate 25%; Awesomejev 656 entries / 38,160 stars; tracker likes 64 (+4) lastModified UNCHANGED; Laya present; Blackwood ABSENT; Archer still promised_not_landed; do not reopen or amend PR #23/#24/#25/#26),
§110 (BlackwoodAI/blackwood-rlcd Blackwood tracker ABSENT, likes 2 gated manual, census densify not landed; Blackwood tracker ABSENT; likes 2 gated manual; ECE 0.021; acc 0.807 vs warmup 0.746; GH Meanblock 404; lock leesk212/JEV-CPU; GH jev-haiku-benchmarking 404; banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*; TCP floor 198.8 ms; type reliability is not a reason to choose Jev (json_schema 5/5); gateway tax not one number; 4/8 without Jev; ≠ RadRebelSam/awesome-jev; 200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*; NLI Tetris argmax P(entail)−P(contradict); 情緒測謊器; 1q 396ms / 30q 567ms; ±0.03; 33q $0.000045 vs Gemini ~5× slower ~60× cost *theirs*; ≠ realZachi/jevtest; 8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*; synthetic; no inference; ≠ JevBench v1.2 §78; Judged 3317 / listed 2560; Jev judges, code applies policy; catalog ≠ endorsement; APA “microsecond policy / zero hallucination” overclaim; Client-side quiz; pointer from held docs; scanned-PDF warn; CSP only api.typesafe.ai; Jev judges / agent reasons / user decides; selecting an option is not permission to implement; degraded fallback; pattern exact, judgement must clear floor; no matching pattern → no model call; not a correctness oracle; $0.00022 vs chat $0.00306 *theirs*; fast/full/max are ceilings not sizes; SemIf 2186★ (+20 vs §109 2166); jevlike 1038★ (+7 vs 1031); TypeAR 14★ flat; AnotiaWang 96★ (+1 vs 95); yibie/awesome-jev 490★; Laya likes 802 (was 783); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27. anthonym21/qwen3-0.6b-rlcd-decision r = c - p_a, ECE 0.021, acc 0.807 vs warmup 0.746, calibration beyond ~500 tokens unmeasured; larkooo/gemma-e2b-rlcd Independent primitive, 11.57s vs 54.10s · 4.67× · 120/128 *theirs*, default path is pretrained Gemma probs not trained RLCD head; Meanblock/JEV-CPU GH Meanblock 404, lock leesk212/JEV-CPU, softmax over letter slots ≠ Noul; impacte/mimir-lfm-openjev WANLI 0.741 vs openjev v2 0.77 *theirs*, 3-way NLI ≠ Noul; shreyanbr/system-one-distilled/gold/zeroshot priority 0.464 = majority floor, banking77 contaminated, raw margins not probabilities, do not distill Jev as teacher of record (they distilled Haiku); Running-Dolphins/jev-bench “0.9 is not one number”, ranking ≠ calibration, ≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench; WallerChen/jev-measured $0.0000153–$0.0000226 vs circulating $0.0004 (~20×), Score is 0..n-1 expectation not 0–1, Noul has no confidence field; RadRebelSam/jev-decision-lab Function-only 5/8 vs hybrid 8/8, 8 designed cases not conversion lift; nozomi-koborinai/jev-spec Spec vs artifact remainder, treating 0.85 as 85% / minProbability hard-gate as Harbor; 202620325-spec/Jev-LLM VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring, Solar writes, Jev chooses NEXT ACTION; do not reopen or amend PR #23/#24/#25/#26/#27),
§49 (boundary map; DMB vs constrained LLMs; von Needle snapshot; open-alternative-jev). Before
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

**Family delta (judgment / architecture; `notes.md` §98).**
Do **not** rewrite this card as a train/serve how-to.
Primary replica/code fold lives in Jev-omni. README
*theirs* now ships a family (0.5B / 0.6B / 4B / 8B),
not the 0.5B-only note. Archer-arch fidelity.
block-causal isolation. pointer/readout CE-trained.
`/v1/systemone` drop-in. Isolation exact: packed vs
separate agree to **4e-6**. Frozen `transfer-v4` dev
(764 records) *theirs*: kev-4b acc **0.759**, kev-8b
**0.774**, Jev **0.857** — highlights round to
kev family OOD 0.76–0.77 vs Jev 0.86. Brier kev-8b
**0.339** vs Jev **0.211**; confident errors kev-8b
**8.2%** vs Jev **3.7%**; held-out policy both-siblings
kev-4b **0.62** / kev-8b **0.61** vs Jev **0.86**.
Previews fail the ≥70% screen (best **0.67**). Locked-test
OOD: kev-4b **0.794** / kev-8b **0.799** (single read).
ECE OOD ~0.1. replica honesty: a `/v1/systemone`
drop-in is not a Noul; architecture confirmation ≠
Jev identity. Score confidence is a stand-in
(*theirs*); TypeSafe has not published theirs. Hub:
[`jaredpalmer/kev-4b`](https://huggingface.co/jaredpalmer/kev-4b),
[`jaredpalmer/kev-8b`](https://huggingface.co/jaredpalmer/kev-8b),
[`jaredpalmer/kev-0.6b`](https://huggingface.co/jaredpalmer/kev-0.6b).
Collection
[kev](https://huggingface.co/collections/jaredpalmer/kev-6aad9d0ea49f2589665e07cd).
Do not copy `uv run` / ports / Modal / train flags.
Soft Noul ≠ hard safety: 0.76 / 0.77 / 0.86 / ECE ~0.1
/ 0.62 are **sensors**. Pasting OOD acc as “close
enough to ship as Jev” is theater. Archer still
**NOT landed**.

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



**0743 HIGH class ports (`notes.md` §113):** siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; softmax over A/B/C ≠ Noul; Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; current-llm; 结构兼容，不是 Jev 模型能力; The local path does not claim to turn a smaller checkpoint into Jev; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★. Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2240★ (+33 vs §111 2207); jevlike 1050★ (+7 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 522★ (+16 vs 506); Laya likes 862 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2240★ (+33 vs §111 2207); jevlike 1050★ (+7 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 522★ (+16 vs 506); Laya likes 862 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

**0806 HIGH encoder / ZS lineage (`notes.md` §112):** BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; opt for DeBERTa and ModernBERT ones; Jev is exemplar not the mandate; softmax/ZS scores still ≠ calibrated Noul. people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29

**0646 HIGH class ports (`notes.md` §111):** prefill plus exactly one decode; softmax over A/B/C ≠ Noul; encode the state once, decide everything in parallel; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; score and noul not implemented; BBQ 9,053/10,000 (90.53%) overconfident (ECE 0.0890; Mean confidence 0.9943). Wire-compat ≠ replica. Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.
User-provided 0806 uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.

