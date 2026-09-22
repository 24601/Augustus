# The judgment-model class (Jev is exemplar, not monopoly)

> **Framing.** Augustus designs for the **decision-model class**. TypeSafe Jev (Choice / Score / Noul) is the dominant product most users will call. "System One" is TypeSafe's name for part of this class, not a synonym that erases the rest.

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
| **Open System-1 / decision-model head** (Laya, openjev, LightJev, openjev-lm, Nimble, **kev**, **blackwood-rlcd**, Hume **Watch**) | Same *shape* as Jev, you host it | Same primitives or logits-as-options | Air-gap, $0/token, inspectable weights, deployment control; **image-in now** (blackwood) without waiting for Archer | Self-eval duty; Laya text-only, 512 tok; vendor vs-Jev tables are claims (`notes.md` §18). A distill learns the *teacher's* answers: openjev-lm and jev-gate-student-b (`notes.md` §25, §33). Nimble is an open LoRA recipe on hard labels, not a Jev distill (`notes.md` §35). **kev** is a shipped Qwen2.5-0.5B LoRA + pointer readout of Archer's reconstruction — public gold, not a Jev teacher; ID ECE only (`notes.md` §45). **blackwood-rlcd** is open multimodal RLCD (CC BY-NC), Jev-compatible shim; Jev still leads general text (`notes.md` §46). Hume's 27B dense drop is **Watch**, not a Hub checkpoint. He prefers the class name **decision models** over "system one". Hourly 2146 class members (`notes.md` §133): Open-Jev provider pipeline ≠ completed quality; CPU tests ≠ GPU scores; metask-jev-4b 80.1% *theirs*; lumen MoLoRA conformal; bonsai ECE 0.037 *theirs*; fine-tuned Kev ≠ TypeSafe Jev; cutoff 95% still soft |
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

Hourly 1851 (`notes.md` §158) separates three decide shapes that share
a label and do not share a measurement. An MLX port of von is a serving
substrate, not the §49 PyTorch table. A logprob or early-exit readout
over a causal LM (fooSynaptic/jev-any-llm, neilbauman21-hub/verdict) is
not a trained decision head. A residual head plus LoRA
(hf:Praveenrajus/jevify-qwen3.5-4b-t2) is a trained head, and one seed
is not a species win. Qwen3.5 is not Archer. TypeSafe Jev stays the
default path. These peers are in the class. They are not equal in
adoption.

User-provided jimothy (`notes.md` §159) is a distill and local-serving
path in the decide class. TypeSafe Jev stays the default path. A linear
head on frozen MiniLM or TF-IDF is not a calibrated replica of hosted
Jev. Teacher labels, when configured, come from typesafe-ai/jev.
Training is local. A null threshold is no recommendation. The
application owns the cutoff. MiniLM probabilities can differ across
Node, WASM, and WebGPU, so validate the cutoff in the runtime that
will serve it.


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
   *invent* the paddle command. Hourly 1441 densify: **167★**; HEAD
   `19af545f096e`; candidate probabilities are relative not correctness;
   37.30s → 2.40s at 64 decisions *theirs*; Breakout 9 bricks 6 returns
   2 lives *theirs*. hr98w/jev-visual ≠ sseanliu/Jev-Vision.

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

5. **Frozen-VLM logit readout (harness, not weights).**
   [`yoheinakajima/glance`](https://github.com/yoheinakajima/glance)
   (`notes.md` §147; PyPI `glance-vlm`; site
   [glance.yohei.me](https://glance.yohei.me)): default Qwen3-VL-4B.
   Yes/no, pick-one, and the default unfitted rating (`jsondigits`,
   exact 0.669) are answer-token logits in one forward pass. Labeled
   `glance fit` uses `ens4d` (4 passes). Soft probabilities are for
   threshold, abstain, or rank. They are not a safety gate. Shares the
   inference object with simple-jev, jev-visual, and LitJev. Shapes
   follow TypeSafe Jev (hosted text). Trains no weights, unlike
   hf:thaitea/laya-vision (§146), unlike OpenJev v2 (Hub
   AlexWortega/openjev, trained 4B multimodal claim scorer, census
   §77, no sibling card), and unlike IamBusy/OpenJev-Vision (trained).
   OpenJev v2 ≠ Zefan-Cai/Open-Jev (§125, separate trained-head
   namesake) ≠ razorback16/openjev ≠ IamBusy/OpenJev-Vision.
   Author numbers are *theirs*. Raw yes/no ECE is 0.111 and 0.179. The
   measured remedy is a pooled two-number Platt map on those suites
   (ECE 0.061 and 0.053). Transfer to a new yes/no task is untested.
   `glance fit` stays on the rating bullets: it is a per-rubric rating
   map, not that Platt map.

6. **Educational Kev pointer, text choice only.**
   [`peterpme/lev`](https://github.com/peterpme/lev) (`notes.md` §149):
   Qwen2.5-0.5B plus LoRA plus a pointer head over caller-supplied
   options. Softmax probabilities are for rank or threshold. They are
   not a safety gate. `POST /v1/systemone` is choice only; noul and
   score are later. Not production. Distinct from trained Laya, from
   OpenJev scalar heads, and from glance (this vision logit harness).
   Does not erase jaredpalmer/kev (`notes.md` §45). Author Banking77
   figures are *theirs*. License file absent.

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
| Scaffold Choice/Score/Noul against an open classifier server | **jevinize** (`notes.md` §104); **simple-jev** first card (`notes.md` §134); logits are not calibrated probabilities of correctness; does not reproduce TypeSafe; `/v1/systemone` alias of `/v1/classifier` | Treat the scaffold as TypeSafe hosted; copy Featherless demo keys; treat logits as P(correct); collapse alias into logit-equiv |
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
| **kev** (Qwen3 0.6B/4B/8B family + pointer; Apache-2.0) | Public gold, CE. Held-out ECE 0.065 (0.031 after T=1.47); acc 0.799 on 1,350 ID questions. Isolation exact. **Not** a Jev teacher-copy (`notes.md` §45). **Family delta (`notes.md` §98):** Archer-arch fidelity; kev family OOD 0.76–0.77 vs Jev 0.86; block-causal isolation; pointer/readout CE-trained; `/v1/systemone` drop-in; replica honesty | Laptop-local System One drop-in for development/eval; independent questions, one prefill. Family bake-off candidate, not a Jev substitute | ~160 ms / 6 questions; ~1h45m train on M5; 38 MB adapter. Family: kev-4b ~1 s / kev-8b ~2 s bf16 *theirs* | Self-host; official `typesafe-sdk` with `base_url` | Text. Not multimodal. 0.5B knowledge; 4B/8B OOD still a gap | noul / choice 2–255 / score |
| **lev** ([peterpme/lev](https://github.com/peterpme/lev); Qwen2.5-0.5B LoRA + pointer; license file absent) | Educational Kev-line readout on public Banking77 labels. Checked-in banking77-v1 accuracy 0.88, ECE 0.040830, NLL 0.517905, Brier 0.187623 on 150 records *theirs* (`notes.md` §149). Softmax over supplied options is not a calibrated Noul. Not a hosted Jev teacher-copy. Does not replace kev | Rank or threshold the choice distribution. Not a safety gate | median 117.241 ms *theirs* on that suite | Self-host. Not production. License file absent | Text. Not glance | choice now; noul and score later |
| **Diffusion structured reads** (djev-spark) | Interface claim only. **Hypothesis** it beats a decision head on your labels (`notes.md` §36) | Optional sequential chunks, text-only | Their GX10 tables, not a class benchmark | DGX Spark container. Do not copy the route | Images are an extension; think and sequential reject images | README criteria, not copied here |

 **1542 densify:** Constrained AR ≠ calibrated Noul (TypeLLM Batch 5.8x *theirs*). kev 4B new-source 0.790/0.806 *theirs*; 8.2% ≥0.9 on wrong *theirs*; option order can change an answer (`notes.md` §126).
 **1746 densify:** truncated thinking then constrained decode (TypeLLM 0.8B thinking On 0/18 *theirs*; forced closure 20/20 type-valid *theirs*). Kev-0.8B completes family; 4B 0.794/0.832 *theirs*; 9B 0.812/0.837 *theirs*; Qwen3.5 ≠ Archer (`notes.md` §128).

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
reads logits via structured-read vLLM extensions. **Since last look 1643 (`notes.md` §75 / §127):** HEAD `febf02e88989`; release 0.3.0; re-pin vLLM PR #57250 restructured head; VLLM_COMMIT `baa8338`; MODEL_VERSION stays openjev-0.1; uv.lock hygiene. restructured vLLM head ≠ logit-equiv. dual serving is not generate. Hosted Codiv ≠ TypeSafe.
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
**NanoJev unified-games-v1 densify (open replica / specialist
gameplay S1, not TypeSafe Jev; `notes.md` §115):**
[`TianyuCodings/NanoJev`](https://github.com/TianyuCodings/NanoJev)
(Python MIT; **1289★** / **158** forks / size **64035**; HEAD
`618cea6d906d54e128360786d12f703fff2b1245`; README SHA
`4190093c64ee75b26e9726daa3b00cbcf6d3157a`). README *theirs*:
A 0.6B parallel decision model: states and questions in,
complete probability distributions out. Zero output-token
decoding. One model, four games. Qwen3-0.6B + decision heads;
Choice 2–255 / Boolean / Score 2–10. Hub
[`C-Tianyu/NanoJev`](https://huggingface.co/C-Tianyu/NanoJev)
revision **unified-games-v1** likes **58**; dataset likes **5**.
hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6. Held-out *theirs*:
Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128 vs Jev 7/10
8/8 56/128 11/128 vs Untuned Qwen3-0.6B 2/10 0/8 56/128 11/128.
caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠
zwliJay/jev-forge ≠ NanoJev. local type boolean ≠ TypeSafe noul.
A normalized distribution alone does not establish empirical
probability calibration. Game success ≠ calibrated Noul. Wire-
compat ≠ replica. Do not copy `pip`. Already cited lightly via
jevinf (§72); this is the densify.
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

**Family delta (`notes.md` §126 hourly 1542).** HEAD `b339f446a0ef` README SHA `86b0a19909f3`. Kev-0.6B 4B 8B family. 4B new-source 0.790/0.806 *theirs*. 8B new-source 0.796/0.780 *theirs*. Jev hosted 0.857 *theirs*. Questions share the input text but cannot read each other. No Jev outputs were used for training. 8.2% ≥0.9 on wrong *theirs*. option order can change an answer. isolation ≠ option-order immunity. Qwen3 ≠ Archer. Do not copy `uv run`. Soft Noul ≠ hard safety.

**Family delta (`notes.md` §128 hourly 1746).** live HEAD `8465c4c4c294` (watch `38087aa0301d`) README SHA `19664b9ae546`. Kev-0.8B completes family. Kev-0.8B 4B 9B Qwen3.5. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*. SemIf Kev-9B 0.917 Jev 0.965 *theirs*. scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*. transformers >= 5.17. Qwen3.5 ≠ Archer. Do not copy `uv run`. Soft Noul ≠ hard safety.

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

### Since last look (2026-09-20T21 hourly 1542) — TypeLLM/TypeLLM

Live name [TypeLLM/TypeLLM](https://github.com/TypeLLM/TypeLLM). HEAD `6a48f9f1e623` README SHA `dbdc1f193537`. README densify 3k→12k B. thinking=True/False per-field budget. type safety does not guarantee factual accuracy. Sequential 9.35 s vs batch 1.61 s K=16 Boolean fields, 5.8x *theirs*. Constrained AR ≠ calibrated Noul. Qwen/Qwen3.8-27B ≠ Archer. Do not copy SGLang flags. `notes.md` §126.

### Since last look (2026-09-20T23 hourly 1746) — TypeLLM/TypeLLM

Live name [TypeLLM/TypeLLM](https://github.com/TypeLLM/TypeLLM). HEAD `702e6a287f3c` README SHA `08180db0450b` (was `6a48f9f1e623`). truncated thinking then constrained decode. typellm_runtime.py typellm_sglang.py. evals/qwen35_small. 0.8B thinking On 0/18 *theirs*. forced closure 20/20 type-valid *theirs*. type-valid ≠ exact. Constrained AR ≠ calibrated Noul. Qwen/Qwen3.8-27B ≠ Archer. Do not copy SGLang flags. `notes.md` §128.

### Since last look (2026-09-21T03 hourly 2146): Open-Jev / metask / lumen / bonsai / Kev CartPole

Open-Jev provider quality pipeline HEAD `a00559ea0ab2`. README SHA unchanged. provider pipeline ≠ completed Open-Jev quality. CPU tests ≠ GPU scores. 65/76 72/76 66/76 60/76 71/76 *theirs*. Open-Jev TREC pending. metask-jev-4b 79.6% / 80.1% *theirs*. lumen mixture-of-LoRA conformal. bonsai 192/231 ECE 0.037 *theirs*. fine-tuned Kev ≠ TypeSafe Jev. one record of 64. QMT mock/dry default no orders. cutoff 95% still soft. catalog ≠ endorsement. *theirs* not Harbor. `notes.md` §133.

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



**0920 jcr class port (`notes.md` §116):** decide/rank over a nested catalog of deterministic operations; Jev is the routing sensor, not the executor. Beam geometric mean is control, not a new head. NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability.

**0743 HIGH class ports (`notes.md` §113):** siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; softmax over A/B/C ≠ Noul; Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; current-llm; 结构兼容，不是 Jev 模型能力; The local path does not claim to turn a smaller checkpoint into Jev; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★. Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

**0806 HIGH encoder / ZS lineage (`notes.md` §112):** BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; opt for DeBERTa and ModernBERT ones; Jev is exemplar not the mandate; softmax/ZS scores still ≠ calibrated Noul. people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29

**0646 HIGH class ports (`notes.md` §111):** prefill plus exactly one decode; softmax over A/B/C ≠ Noul; encode the state once, decide everything in parallel; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; score and noul not implemented; BBQ 9,053/10,000 (90.53%) overconfident (ECE 0.0890; Mean confidence 0.9943). Wire-compat ≠ replica. Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.

**Hourly 0843 class / measurement (`notes.md` §114):** Qwen2.5 option-logit ECE is a class property of pretrained bases, not Archer. JA sokudan encoder (weights 準備中). decision-circuits AND-product independence recorded. circuit-vl-4b ≠ Archer. ranking ≠ calibration (BANKING77 BERT-Base is supervised). calibration does not compose.

**0940 HIGH prompt-compiler on-ramp (`notes.md` §118):** alexwestco/llm-to-jev is a deterministic heuristic compiler of LLM prompt *shape* into proposed Choice/Score/Noul — not a Jev replica, not altryne/jevify, not Mintzs/jevify. Heuristic conversion ≠ calibrated Noul. conversion assistant, not an automatic guarantee of equivalent behavior.

User-provided 0806 uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.


Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; 25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; AND: product (independence assumed and recorded in the trace); chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §114
User-provided 0915 uniqueness lock: TianyuCodings/NanoJev unified-games-v1 densify; A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; 18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58; dataset C-Tianyu/NanoJev-Data likes 5; HEAD 618cea6d906d54e128360786d12f703fff2b1245; 1289★ / 158 forks / size 64035; README SHA 4190093c64ee75b26e9726daa3b00cbcf6d3157a; MIT; caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; not TypeSafe Jev; open replica / specialist gameplay S1; soft scores ≠ hard gates; Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; invented_signal false; do not reopen or amend PR #31/#32/#33/#35; notes.md §115


User-provided 0920 jcr uniqueness lock: NiazMorshed2007/jcr MIT; site https://jcr.niazmorshed.dev; topics ai-agents,jev,mcp; **4★**; HEAD `138b3832`; README SHA `2a49dbc1`; LICENSE SHA `46231303`; size **14850**; Jev Capability Resolver; one tool to find documented deterministic commands in a nested capability tree; returns context; **does not execute**; skills = workflow+judgment; capabilities = individual operations; format independent of Jev; proposed open standard exploration; classify (Jev) → optional OpenAI decompose compound → beam search geometric mean of routing probs; keep up to 3 paths ≥60% of best (JCR_BAND_RATIO 0.6); ambiguity / no-match / depth-limit explicit; soft scores ≠ hard gates; 0.6 band is application policy; routing ≠ permission; docs ≠ authority to run; sol-vs-opus5-20 *theirs*: 20 scenarios × 4 variants = 80 runs; lookup+explain only, no execution; Claude Opus 5: agent input 108,585→15,819 (−85%), cost $0.3700→$0.1222 (−67%), wall 105.5s→77.7s; Codex GPT-5.6-Sol: 61,952→47,669 (−23%), $0.1377→$0.1151 (−16%), wall 25.3s→62.4s (Sol slower with JCR in 19/20); One Sol outlier 372.6s / 193 Jev calls; n=1 per cell; Not Harbor task-execution; Claude/Codex harnesses; compare mode; 50 scenarios bundled; 11 groups, 960 nodes, 11,360 items; 16 routing rounds per step; NiazMorshed2007/jcr ≠ skill-broker ≠ skillranker ≠ jev-sift ≠ jev-lens ≠ jevusher ≠ jev_select_capability; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34; notes.md §116

User-provided 0922 (`notes.md` §117 / items 330–336 / batch #100). SemIf was formerly OpenJev; MLX backend; 5.21× systems≠semantic; Softmax over options ≠ calibrated Noul; live REST 2282★. Do not reopen #23–#36/#38; do not push onto open #39/#40.
User-provided 0922 uniqueness lock: SemIf was formerly OpenJev; independent; not affiliated with Jev or TypeSafe; homepage openjev.com; default master; MIT; HEAD ca3ba65f1429; Tolerate float roundoff in MLX evidence verification; pushed 2026-09-19; live REST 2282★ / 140 forks; size 9177; README SHA 74ab7f7f; LICENSE SHA ca562883; interface pattern reproduction with open models; does not reproduce Jev undisclosed model/training; Direct option logits; 0 output tokens; shared-state parallel; MLX backend for Apple Silicon (`--backend mlx`); Qwen3.5-4B 3090 direct 1.023s vs AR JSON 5.332s (**5.21×**); argmax agree 18/21; systems comparison ≠ semantic equivalence; Parallel suffixes 20.03 dec/s on 777 decisions; Browser ladder Qwen3.5-4B authored BA 0.813, pert 0.766, TypeSafe subset agreement 0.845 vs Published Jev 0.883 (102 across 20 cases); Softmax over options ≠ calibrated Noul; typed output does not guarantee semantic correctness; wire/agreement ≠ replica of TypeSafe; SemIf ≠ kw2828/OpenJev playground ≠ zhihz/openjev ≠ apiplant/semif-rs port ≠ dddanielliu/semif-serve; rename is densify not a second census; JevBench 74.6 is §78 not this ladder; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#38; do not push onto open #39/#40; notes.md §117
User-provided 0940 uniqueness lock: Turn decision-shaped LLM prompts into proposed Jev primitives; This is a conversion assistant, not an automatic guarantee of equivalent behavior; The compiler uses deterministic heuristics, not an LLM or evaluation model; It understands a deliberately small set of common prompt patterns; Generated instructions and criteria must be reviewed before production use; Score ranges such as 0 to 1 are translated into ordered Jev criteria; Prompts requiring open-ended prose are not a fit; suitability strong/partial/not_a_fit; compatibility full/partial/none; Writing new text stays with an LLM; Review the generated Score rubric; Jev scores ordered criteria, not an arbitrary 0-to-1 range; Everything runs locally in the browser; There is no framework, database, account, API, or server-side prompt processing; The key is read from the process environment and is never stored or printed; connect-src 'none'; alexwestco/llm-to-jev ≠ altryne/jevify ≠ ryana/jevify ≠ fidecastro/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; HEAD 234058ab372d; README SHA 43cd94fb; LICENSE SHA 5f334006; compiler SHA fdf235d0; 2★; MIT; JavaScript; size 29; Pages https://alexwestco.github.io/llm-to-jev/; invented_signal false; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §118
Hourly 0947 uniqueness lock: Fast and cheap agent evals. jev as judge.; 18,041 skills from the 200 most-starred repos; Not a security scanner; 最简 Jev 调用演示器; confidence 不是正确率; q93304989-bit/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; 75% cheaper and 18% faster withdrawn; jev @0.15 100% recall 87% savings; 33Audits/jev-auto ≠ gargpratyush/jev-router; no Typesafe key, no PI_API_BASE, zero deps; tool-emitted Score/Noul ≠ calibrated Noul; semantic_compatibility: false; candidate_mass; Qwen3.5-2B ≠ Archer; Jev evaluates decisions; it cannot run a coding-agent session; Status: no model yet; S1LV3RJ1NX/openjev ≠ TheoLeeCJ/openjev; 28 accepted decisions; 3 targets; score 800; health 100; arcade game not a flight trainer; A successful live TypeSafe call has not been verified for v0.1.0; abhibansal60/tidy ≠ MANISH007700/tidy; No model, Jev included, predicted which channels its owner keeps; seed 1 selected on a held-out 400-item validation split; Brier 0.342 → 0.378; more accurate and more overconfident; Qwen3.5-4B ≠ Archer; static quants of kushalpatil/jevify-gemma4-26b-a4b; The labels were corrected, and one earlier result was retracted; zero of 23,869 eligible rows; Do not compare cost without checking task success; Exit 1 is not a proof; kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go ≠ official; 38 tests that cannot fail in a 356-model warehouse; if a parser can answer it, Jev is never asked; 359 of them; Games & Simulation 82; Education & Learning 1; Ratings are heuristics; syedabbasshaheer-art/jev-atlas ≠ ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas; anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases ≠ walidboulanouar/awesome-jev-use-cases ≠ vamsikrishna2421/jev-usecases; Every headline result above is self-reported; Archer Hume 84.6% MMLU-Pro is a third-party probe not landed Archer; catalog ≠ endorsement; judge ≠ actuator; softmax over A–H ≠ Noul; SemIf 2270★; jevlike 1054★; TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 538★; Laya likes 889; tracker likes 68 lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#35/#36/#37/#38/#40; do not push onto open #39; notes.md §119


**Hourly 1049 HIGH (`notes.md` §120).** ggmlc GGUF is not llama.cpp. serving substrate ≠ calibrated replica. Qwen3.5-9B ≠ Archer. planner writes JEV selects. pick_by_id vs pick_second. soft scores ≠ hard gates. catalog ≠ endorsement. Do not reopen or amend PR #23–#42. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1049 uniqueness lock: ggmlc GGUF is not llama.cpp; Loading them in llama.cpp will fail; one encoder pass; hf:mys/laya-GGUF sha 713ae6f6e39f likes 0 apache-2.0; hf:mys/laya-multilingual-GGUF sha 3b645ae54281; hf:mys/laya-typed-decisions-GGUF sha 1e9e8ba1f527; hf:tozp/laya-onnx sha 0862aeba1e65 Opset 14 FP32 and INT8; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; docker-laya MIT HEAD 1b8239a51ddd README SHA 9cb7bdc3; laya.cpp RTX ggml CUDA HEAD 8590937c79a2 README SHA cdd429b9; serving substrate ≠ calibrated replica; Softmax over options ≠ calibrated Noul; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; jev-position-test n=6 HEAD 7a56ca1c2698 README SHA 23f194c9; jevmlx slots 5 of 6; hosted Jev 0 of 6; prior_correction made it worse; jevSweeper mean Spearman ρ −0.274; picked exact-optimal 1/25 (4%); 31 of 36 still logically decidable; 86% of the time we should not have been asking; game success ≠ calibrated Noul; LLM2Jev 64★ Apache-2.0 HEAD 924618721277 README SHA da35fe61; not affiliated with or endorsed by Jev or TypeSafe; No answer tokens are generated; OpenSourceJev llama.cpp Qwen3-1.7B HEAD 3c41fba3681d; JEV-MLX Qwen3.5-9B HEAD dec24cd929ea; decision-head-rlcd Qwen3.5-4B 4.9M LoRA; AUTO_ACT is not a Noul; closed-set fail-open stdlib-only; verified=False; soft scores ≠ hard gates; 22 to 40% cheaper *theirs*; first version 70% more expensive; 111-case benchmark *theirs*; CDC 5,000 Jev 72.2% AUC 0.7725 *theirs*; accuracy is a trap; 9.0% base rate always-no 91.0%; catalog ≠ endorsement; jev-skill 109★ 90 scenarios HEAD 4f6e899a24d4; awesome-jev-live 673 entries 4★; minecraft-agent 214★ 131 JEV decisions 35 Astra calls; nether-final-08 8 minutes 43.300 seconds; planner writes JEV selects; RoboJEV structured simulator state not images; ashare-trader 策略未通过自己的回测门槛; 36 组参数全部净期望为负; no positive expectation under real costs; typed_evals NOT an official TypeSafe AI product; jev-as-judge is a sensor; third-person-audit 40% & 60% watermarks still soft; The included experience uses a handwritten demo provider; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42; notes.md §120


**Hourly 1143 HIGH (`notes.md` §121).** open recreation ≠ calibrated replica. semantic lint is a sensor not a proof. cutoff 0.8 still soft. paired bootstrap CIs *theirs*. Same accuracy, 35x faster *theirs*. systems comparison ≠ semantic equivalence. serving substrate ≠ calibrated replica. catalog ≠ endorsement. permission ≠ confidence. Do not reopen or amend PR #23–#43. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1143 uniqueness lock: open recreation ≠ calibrated replica; Qwen3.5-4B ≠ Archer; It is an open re-creation of Jev; less calibrated; perch 164★ MIT HEAD ba775a9940b6 README SHA 7ad0403b; semantic lint is a sensor not a proof; oxlint-plugin-jev cutoff 0.8 still soft; nassim-arifette/jevgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; patdown fuzzy linter; PanAchy/jevvy ≠ Atominac/jevvy; No orders, no advice; SmartMoney-Cub 25★ HEAD d93cf493853d; paired bootstrap CIs *theirs*; emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; +0.82 pts XQuAD-EN 95% CI +0.35 to +1.31; +7.62 pts SciFact CI +4.88 to +10.38; Same accuracy, 35x faster *theirs*; systems comparison ≠ semantic equivalence; BANKING77 500 Jev 81.0% GPT-OSS 82.8% Mercury 73.2% Gemini 85.4% *theirs*; frozen cascade missed its evaluation accuracy target 430/500 vs GPT-5 432/500; This is not demonstrated equal-quality savings; 24 invented tickets; Routing errors caught by the gate 0 of 3; sample too small to establish calibration; This is not TypeSafe Jev; No real API requests were made; wire-compat ≠ replica; KonghaYao/laya-jev 按官方接口写的客户端只改一个 base URL; gqgs/laya-onnx densify 496.8 MiB; tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; serving substrate ≠ calibrated replica; BeatAPI/awesome-jev ≠ 99hansling/awesome-jev ≠ Vishnurr2k01/awesome-jev ≠ robokrunch/awesome-jev ≠ rudy2steiner/awesome-jev-hub; All 125 projects; catalog ≠ endorsement; Pasblinn/jev-lab ≠ tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab ≠ q93304989-bit/jev-lab; Independent project. Not affiliated with TypeSafe; Kevthetech143/super-jev densify experimental V0.2.0; permission ≠ confidence; allay-team/openjev ≠ piyush-infocusp/openjev ≠ TheoLeeCJ/openjev; 2022 Mineflayer Jevalent collision; kushalpatil/jevify-gemma4-e4b GGUF densify; static quants; This dataset and model are independent research artifacts, not reproductions of Jev or RLCD; pngwn demo accuracy 0.705 ECE 0.046 ~112 ms *theirs*; cutoff 0.8 still soft; soft scores ≠ hard gates; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43; notes.md §121

**Hourly 1248 HIGH (`notes.md` §123).** decide is not generate. tryDecide returns typed calibrated judgments not a token stream. GLiNER/GLiClass ports are class members not Jev replicas. 93.5% *theirs* not Harbor. 74.9 *theirs* not Harbor. 8.7x *theirs* not Harbor. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#45. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1248 uniqueness lock: decide is not generate; tryDecide returns typed calibrated judgments not a token stream; juspay/neurolink 133★ MIT HEAD 268b0fe83130 README SHA e709cadfa6b6 tag v12.19.0; GLiNER/GLiClass ports are class members not Jev replicas; MacPaw/Gliner2Swift ≠ Knowledgator/GLiClass.c ≠ fbilhaut/gliclass-rs ≠ Knowledgator/GLiClass.js ≠ gravitee-io/GLiNER4j ≠ apiplant/gliner-rs ≠ codesoda/gliner2-rs; 8.7x faster 4.4x fewer prompts *theirs*; 153 was a reporting error; corrected 156-case 9.8x faster 4.2x fewer prompts *theirs*; independent v0.2.1 1.24x vs Mini *theirs*; Approvals only; anpicasso/hermes-jev-approvals ≠ hermes-switchyard; scx-router GLiClass ranks candidate LLMs in one non-generative pass; typesafeai-dotnet-sdk Not affiliated with TypeSafe AI; hyperspaceai/jevcache ≠ kushals256/jevcache; ST-jeved measures each reply; 400 plain-text for unaskable question; razorback16/openjev:0.2.1 Docker densify HEAD 794a81b87131; wire-compat ≠ logit-equiv; Option-Marker joint attention 93.5% macro *theirs*; 93.6% micro *theirs*; n=78; T = 1.0367 vs T = 1.1692 two temperatures; guaranteeing is soundness theater; wfzyx/von densify HEAD bed7e7337791; Benchmark Heaven leaderboard #2 74.9 *theirs*; NLL calibration assets; 77.10% still §71 claim-audit; do not re-fold as a beat; Heman10x-NGU/openJev-verdict-2.0 densify HEAD bff28567cff4; kev-family weight tarballs; PLAN_Qwen35 proposal for review; deadline 0.53→0.82 at 9B *theirs*; Qwen3.5-9B ≠ Archer; isolation would fail by construction on DeltaNet; jaredpalmer/kev densify; JevBench v1.2.2 jeff 66.9 (#9) jev 75.3 (#2) *theirs*; logan-markewich/jeff densify HEAD 34b32f99a727; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; TypeLLM/TypeLLM densify HEAD c4b03ba9e792; us/jev-local stub until hf; Eran-BA/Jev_from_GLiNER2 spec ≠ replica; lsu-ub-uu/systemone ≠ TypeSafe System One; Layan/Laya HF spaces name-match; catalog ≠ endorsement; decide ≠ generate ≠ stream; 93.5% *theirs* not Harbor; 74.9 *theirs* not Harbor; 8.7x *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45; notes.md §123

**Hourly 1340 HIGH (`notes.md` §124).** typesafe-sdk 0.7 Pydantic response models. msgspec dropped. MLX backend 400 plain-text error contract. Pydantic response models ≠ logit-equiv. msgspec dropped is not a replica. Error contract is not a Noul. PLAN_Qwen35 densify. coverage-at-error-budget *theirs* not Harbor. GLiNER locate ports are class members not Jev replicas. Locate ≠ decide. ~160 ms *theirs* not Harbor. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#46. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1340 uniqueness lock: typesafe-sdk 0.7 Pydantic response models; msgspec dropped; The server's output is unchanged and was never wrong; MLX backend 400 plain-text error contract; SchemaError is 400 plain-string detail not 422 list; razorback16/openjev densify HEAD 6e91dfc031bc README SHA cbdcc8de0304; Pydantic response models ≠ logit-equiv; msgspec dropped is not a replica; Error contract is not a Noul; wire-compat ≠ logit-equiv; PLAN_Qwen35 densify; corrected Qwen3.5 LoRA target names verified; in_proj_qkv in_proj_z in_proj_a in_proj_b out_proj; peft 0.21 existence proof; OOD-calibration study; coverage-at-error-budget metric in Phase 0; PLAN_Qwen35 still proposal for review; deadline 0.53→0.82 at 9B *theirs*; isolation would fail by construction on DeltaNet; Qwen3.5-9B ≠ Archer; jaredpalmer/kev densify HEAD 75cc15ddb8e2 PLAN SHA eca543246f50; GLiNER locate ports are class members not Jev replicas; urchade/GLiNER ≠ fbilhaut/gline-rs ≠ lmoe/gliner-onnx.js ≠ shershah1024/gliner-native-runtime; Locate ≠ decide; Jev-Vision skip 0.936 effect 0.967 done 0.896 157 ms *theirs*; ~160 ms *theirs* not Harbor; 0.971 F1 *theirs* not Harbor; coverage-at-error-budget *theirs* not Harbor; hf:fr0stbit3/laya-gguf serving substrate ≠ calibrated replica; jkcdarunday/SystemOne-Next ≠ TypeSafe System One; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46; notes.md §124

**Hourly 1441 HIGH (`notes.md` §125).** vLLM NVIDIA + MLX Apple Silicon. Codiv hosted free endpoint. dual /v1/systemone + /v1/chat/completions. chat 501 on MLX. dual serving is not generate. Hosted Codiv ≠ TypeSafe. candidate probabilities are relative not correctness. recommendation is advisory. the server never blocks on its own. LoRA ≠ RLCD replica. pass-min 0.8 still soft. 37.30s → 2.40s at 64 decisions *theirs*. 2B 94.71% 9B 97.54% hard test *theirs*. wire-compat ≠ logit-equiv. SHA move is not a replica. catalog ≠ endorsement. Do not reopen or amend PR #23–#47. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1441 uniqueness lock: vLLM NVIDIA + MLX Apple Silicon; Codiv hosted free endpoint; dual /v1/systemone + /v1/chat/completions; razorback16/openjev densify HEAD cddbd962c88a README SHA a5943415cb92; STE README rewrite; serving-port densify; chat 501 on MLX; dual serving is not generate; Hosted Codiv ≠ TypeSafe; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; hr98w/jev-visual 167★ Apple Silicon visual candidate scoring; 37.30s → 2.40s at 64 decisions *theirs*; Breakout 9 bricks 6 returns 2 lives *theirs*; candidate probabilities are relative not correctness; jkudish/jev-mcp 156★ ten MCP tools; recommendation is advisory; the server never blocks on its own; TypeSafe CLERC 5% to 18% *theirs*; jkudish/jev-mcp ≠ burnigtm/jev-mcp; zhengxuyu/litjev off-the-shelf Qwen decision layer; Probabilities are not calibrated by default; Qwen/Qwen3.8-27B ≠ Archer; zhengxuyu/litjev ≠ alexwestco/llm-to-jev; Zefan-Cai/Open-Jev LoRA + scalar head; 2B 94.71% 9B 97.54% hard test *theirs*; 2B OOD 86.02% 9B OOD 91.97% *theirs*; 80,816 training rows; 27B still in progress; LoRA ≠ RLCD replica; Zefan-Cai/Open-Jev ≠ TheoLeeCJ/openjev ≠ razorback16/openjev; cristianoliveira/jeq intelligence you can pipe; pass-min 0.8 still soft; JEQ does not own actions; AndyInQtr/laya-coreai CoreML serving substrate ≠ calibrated replica; AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47; notes.md §125


**Hourly 1542 HIGH (`notes.md` §126).** TypeLLM README densify 3k→12k B. Batch 5.8x *theirs*. Constrained AR ≠ calibrated Noul. kev family densify. 4B new-source 0.790/0.806 *theirs*. 8.2% ≥0.9 on wrong *theirs*. option order can change an answer. fail-closed routing vs fail-open test selection. classifier ≠ authorizer. estimates not Harbor. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#48. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1542 uniqueness lock: TypeLLM/TypeLLM densify HEAD 6a48f9f1e623 README SHA dbdc1f193537; README densify 3k→12k B; thinking=True/False per-field budget; type safety does not guarantee factual accuracy; Batch 5.8x *theirs*; Constrained AR ≠ calibrated Noul; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify HEAD b339f446a0ef README SHA 86b0a19909f3; Kev-0.6B 4B 8B family; 4B new-source 0.790/0.806 *theirs*; 8B new-source 0.796/0.780 *theirs*; Jev hosted 0.857 *theirs*; Questions share the input text but cannot read each other; No Jev outputs were used for training; 8.2% ≥0.9 on wrong *theirs*; option order can change an answer; Qwen3 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; TheoOliveira/pi-jev 21★ fail-closed routing; JEV_THRESHOLD 0.65 still soft; routing ≠ permission; harshwasan/jev-sentinel fail closed never auto-allows; harshwasan/jev-sentinel ≠ leepokai/jev-guard; jackbarunz/jev-tool-router ≠ esinocchi/jev-tool-router; threshold 0.90 still soft; 76/81 vs 77/81 *theirs*; 0.419s vs 2.459s *theirs*; $0.00486 vs $0.03673 *theirs*; does not execute; not a security boundary; baronunread/leanest fail-open uncertainty means RUN; classifier.dev default Jev/Laya pluggable; openlayer-ai/jevals ≠ dayhaysoos/jevals; estimates not Harbor; classifier ≠ authorizer; MrJev/awesome-jev 118 entries catalog ≠ endorsement; MrJev/awesome-jev ≠ yibie/awesome-jev; Koushik890/jev-firewall fail closed ask_below 0.7 still soft; CompleteTech-LLC-AI-Research/jev-codex-approval experimental native not compiled; confidence is not a measured probability; rh-guard owns primary gates; hf:rAVEUK/open-jev-deberta-v3-large encoder class member not Jev replica; hf:p-yan/laya-quanto serving substrate ≠ calibrated replica; hf:Gtrkrsk/laya serving substrate ≠ calibrated replica; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48; notes.md §126
**Hourly 1643 HIGH (`notes.md` §127).** openjev release 0.3.0 densify. re-pin vLLM PR #57250 restructured head. restructured vLLM head ≠ logit-equiv. MODEL_VERSION stays openjev-0.1. dual serving is not generate. Hosted Codiv ≠ TypeSafe. typed judgments not opinions. Thresholds are policy not model. Jev never generates prose JSX or code. game success ≠ calibrated Noul. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#49. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1643 uniqueness lock: razorback16/openjev densify HEAD febf02e88989 README SHA 242a737dba01; release 0.3.0; re-pin vLLM PR #57250 restructured head; VLLM_COMMIT baa8338; pyproject and __init__ agree 0.3.0; MODEL_VERSION stays openjev-0.1; uv.lock hygiene; dual serving is not generate; Hosted Codiv ≠ TypeSafe; restructured vLLM head ≠ logit-equiv; wire-compat ≠ logit-equiv; SHA move is not a replica; Error contract is not a Noul; frostney/clean-code-review 7★ typed judgments not opinions; documentation is read not judged; Luna writes from Jev findings; morcoan/JMP Joint Model Participation; Models participate. Real tools execute.; Jev routes actions generators supply arguments; not a swarm; zkjoie/jevbus Thresholds are policy not model; Drop < Review < Deliver; FanOut or Exclusive; Kelbie/hunch ≠ carldaws/hunch ≠ tpellet/hunch ≠ huncho; Agent Skills semantic review; SupratikB23/JevCanvas Jev never generates prose JSX or code; Diffusion never decides structure; json-render is the only renderer; skcache/jevtrafficsim Fixed Adaptive Jev; game success ≠ calibrated Noul; Shalimov04/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev; MstyAI/laya-onnx empty repo ≠ tozp/laya-onnx ≠ Mattepiu/laya-onnx ≠ gqgs/laya-onnx; SherifAshraf2003/jev-use ≠ shitianfang/jev-use; aniruddh-krovvidi/switchboard ≠ cannacre8ive/switchboard-ai; Visorian/TidyUp ≠ abhibansal60/tidy; isiomaC/jevkit ≠ WaynezProg/jev-kit; lee-lou2/jev-tree ≠ reachjalil/jev-tree; Royhu1/jev-poker-trainer empty repo; JoacoMarc/jev-harness-router ≠ jackbarunz/jev-tool-router; rh-guard owns primary gates; hf:Praveenrajus/jev-bench HTTP 200 was 401; hf:ZefanCai/Open-Jev densify dataset; LoRA ≠ RLCD replica; hf:emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; hf:ctaxnagomi/DGUI_HYPERMEM-JEV densify sha ab3d3529; hf:hugging-apps/open-jev-deberta-v3-large-demo encoder class member not Jev replica; serving substrate ≠ calibrated replica; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49; notes.md §127

**Hourly 1746 HIGH (`notes.md` §128).** TypeLLM truncated thinking densify. 0.8B thinking On 0/18 *theirs*. forced closure 20/20 type-valid *theirs*. Constrained AR ≠ calibrated Noul. Kev-0.8B completes family. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. transfer-v9 5%/9%/26% *theirs*. Facts go to code. Judgments go to Jev. Only facts can block. Jev never blocks. five-lines threshold 0.80 still soft. 155/155 argmax *theirs*. Qwen3.5 ≠ Archer. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#50. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1746 uniqueness lock: TypeLLM/TypeLLM densify HEAD 702e6a287f3c README SHA 08180db0450b; truncated thinking then constrained decode; typellm_runtime.py typellm_sglang.py; evals/qwen35_small; 0.8B thinking On 0/18 *theirs*; forced closure 20/20 type-valid *theirs*; Constrained AR ≠ calibrated Noul; type safety does not guarantee factual accuracy; Qwen/Qwen3.8-27B ≠ Archer; jaredpalmer/kev densify live HEAD 8465c4c4c294 watch 38087aa0301d README SHA 19664b9ae546; Kev-0.8B completes family; Kev-0.8B 4B 9B Qwen3.5; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; transfer-v9 Kev-9B 5% Jev 9% Kev-8B 26% *theirs*; SemIf Kev-9B 0.917 Jev 0.965 *theirs*; scienthoon 0.952/0.911 vs 0.897/0.914 *theirs*; transformers >= 5.17; Qwen3.5 ≠ Archer; wire-compat ≠ logit-equiv; SHA move is not a replica; notque/vexjoy-agent 421★ /d routes /do fallback; tamaratran/jev-pruner densify HEAD 47d017c34eab; qkal/Canny Facts go to code. Judgments go to Jev. Only facts can block.; Jev never blocks; jqueryscript/awesome-jev 231 entries catalog ≠ endorsement; jqueryscript/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; jamescazzetta/five-lines threshold 0.80 still soft; eugeniughelbur/jev-engineering 371ms $0.0000189 300-call *theirs*; tpellet/jevify ≠ altryne/jevify; seb4ez/jevguard-mcp ≠ seb4ez/jevguard; resumocast/jev-mcp ≠ jkudish/jev-mcp; dtduc-git/jev-table first sighting; Adrian-Ernesto/jevsort ≠ zzzzzec/jevsort; MidasMulli/kev-ane 155/155 argmax *theirs*; MidasMulli/kev-ane ≠ jaredpalmer/kev; serving substrate ≠ calibrated replica; empty repo skip-thin; loktar00/llm-lan-party empty repo; rh-guard owns primary gates; catalog ≠ endorsement; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50; notes.md §128
**Hourly 1843 HIGH (`notes.md` §129).** kev own-data JSONL densify. --init_from warm-start LoRA/head PR #9. from-scratch ≠ warm-start. JSONL labels ≠ Harbor. 4B new-source 0.794/0.832 *theirs*. 9B new-source 0.812/0.837 *theirs*. 0.33 vs 0.84 vs 0.83/0.88 *theirs*. reconstruction ≠ replica. assay-001 split verdict. catalog ≠ endorsement. SHA move is not a replica. Do not reopen or amend PR #23–#51. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1843 uniqueness lock: jaredpalmer/kev densify HEAD bd058057ad0a README SHA 84b872488915; Fine-tuning on your own data; --data JSONL; --init_from warm-start LoRA/head PR #9; Kev-0.8B 4B 9B Qwen3.5 family; 4B new-source 0.794/0.832 *theirs*; 9B new-source 0.812/0.837 *theirs*; 0.33 vs 0.84 vs 0.83/0.88 *theirs*; from-scratch ≠ warm-start; JSONL labels ≠ Harbor; Kev-0.5B card Qwen3.5 family pointer; No Jev outputs were used for training; option order can change an answer; 8.2% ≥0.9 on wrong *theirs*; Kev-9B 7.5% ≥0.9 on wrong *theirs*; dabit3/jev-experiments densify 340★; simota/tenbin densify neighbor skill; Promethe-us/awesome-jev ≠ MrJev/awesome-jev ≠ yibie/awesome-jev; kyegomez/open-jev reconstruction ≠ replica; unofficial research implementation with random weights; kyegomez/open-jev ≠ razorback16/openjev ≠ TheoLeeCJ/openjev ≠ Zefan-Cai/Open-Jev ≠ Shalimov04/open-jev; jourdanlabs/assay-001 split verdict; CLINC150 ECE 0.0204 *theirs*; Banking77 ECE 0.0936 *theirs*; 8,576 responses zero type errors *theirs*; brnyxx/jev-ra 3-5x / ~300 ms *theirs*; 8.50× Wikipedia *theirs*; ThePFMind/jev-mcp ≠ jkudish/jev-mcp ≠ burnigtm/jev-mcp; namenu/pi-jev-effort ≠ TheoOliveira/pi-jev; samatv256/mini-Jev ≠ r-ms/mini-jev; comoc/jev-minesweeper ≠ EnesYilmazcode/JevMinesweeper; game success ≠ calibrated Noul; Nutlope/jev-fraud Kimi K3; jeffloo886/jev-notion; hf:akhilaaa3/openjev-v1-allmix-r512-merged ≠ hf:akhilaaa3/openjev-r512-handoff-demo; serving substrate ≠ calibrated replica; catalog ≠ endorsement; SHA move is not a replica; wire-compat ≠ logit-equiv; Qwen3.5 ≠ Archer; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51; notes.md §129


Open LM logit-trick (sgoedecke/system-one) is TypeSafe-compatible ≠ TypeSafe replica. Gemma LoRA replica (mithalouni/system-one-open) is replica ≠ TypeSafe. kotoba-lang/typed-decisions is encoder class member not Jev replica. `notes.md` §130.
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
Hourly 0348 uniqueness lock: JonathanHHenson/open-cricket MIT HEAD d75af22125ed README SHA 7d288a741089; Local structured decisions using causal language models; default Qwen/Qwen2.5-1.5B-Instruct; independent of TypeSafe; API follows Jev's general call shapes but model predictions and confidence calibration differ; wire-compat ≠ logit-equiv; Qwen2.5 ≠ Archer; replica ≠ TypeSafe; virtualman333/jev-decision-arena MIT HEAD cf6ae4ed31e8 README SHA 037f75d9610d; Greedy 0.90 vs Oracle 0.82 *theirs*; Random conf 0.00 still 20.5% *theirs*; ECE 0.180 / 0.106 / 0.205 *theirs*; confidence ≠ P(correct); game success ≠ calibrated Noul; seed 42 n=1 is not Harbor; dopeCape/typesafe-ai-test HEAD ed2adb7740d7 README SHA 183f91c36471; 8,400 calls $0.39 *theirs*; Noul 0.7 true 44% *theirs*; ≥0.9 conf 91.7% AG News *theirs*; versioned model ids rejected; *theirs* not Harbor; pCwOrM/werr 2★ MIT HEAD 2526cae98891 README SHA b29476734a09; JevBench 81.65 *theirs* not Harbor; WindTunnel 49/49 *theirs* not Harbor; 0-byte Mandelbrot is not a replica; meijustory123/OpenJev-Kit HEAD c53125982f80 README SHA a4e72c61a973; training not complete; no accuracy; Qwen3.5-0.8B ≠ Archer; meijustory123/OpenJev-Kit IS meijustory123/openjev (same GitHub id 1379187719); meijustory123/OpenJev-Kit ≠ Zefan-Cai/Open-Jev; microchipgnu/jev-hooks HEAD cbf40e64d7b2 README SHA af25fb0aaf70; Compose meaning like state; rashedInt32/jury.nvim 1★ MIT HEAD bf31e9509e7e README SHA a2b088dd0787; Code enumerates the candidates; evoke-build/evoke 1★ Apache-2.0 HEAD 310840b56f1d README SHA 02b91962cef4; Jev is the first classifier the design is bound to none; moritzkremb/jev-voice-browser densify HEAD 198a0764395a README SHA 816309fc22e6 was fa033303; context is the conversation so far; densify §82 not a sibling first sighting; luantak/is-malicious densify 18★ MIT HEAD faf6ba61d7e1 README SHA 4ae098b4b7ae; A clean report is not proof; does not sandbox; skillseedorg/ChatJEVs MIT HEAD 346e7347cf90 README SHA 6ff81d54040f; ChatJEVs ≠ erik-dunteman/ChatJev; generation from Choice is not a language model replica; chrisns/laya-mac-serve MIT HEAD f294500821b6 README SHA 00e39a7d04e2; serving substrate ≠ calibrated replica; rimusz/localjev-mlx HEAD 297836a0d95e README SHA 2d96d20e0b80; rimusz/localjev-mlx ≠ githubnext/localjev; luhayes/jev-agent-router 1★ MIT HEAD bba795a4dc4e README SHA 17a2f44993d1; does not execute; cutoff 0.8 still soft; gbesse/decision-workbench MIT HEAD 8889cf3750a3 README SHA 14a3bf79da7a; demo scores are not accuracy measurements; zhuyansen/x-reply-filter already carded; kylemclaren/jev-search ≠ kazuhideoki/jev-search; xinwang-nwpu/jev-mobile ≠ Friedjof/jev-mobile; kcd-dev/jev-skill ≠ raphael-liu/jev-skill; yanmad27/ask-jev ≠ kuhung/ask-jev; hf:s1lv3rj1nx/openjev-router-healthcare encoder class member not Jev replica; hf:akhilaaa3/openjev-v1-40705-nimble-r512-merged ≠ hf:akhilaaa3/openjev-v1-allmix-r512-merged; jevai spaces catalog ≠ endorsement; skip-thin Fibonaccirabbit/Jev-GalGame MadhavBahl/jev-guide advance-lion/dsh-jev-hooks amithgc/local-jev hiro1202/jev-review-gate-poc inlight37-design/decision-model_lab kuhung/ask-jev mmiguez314/jev-lab pomodorozhong/exp-jev vanthiet1/JevGuarAgent empty SHA; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62; notes.md §139
Hourly 0445 uniqueness lock: lucasmartins-ai/lcc 7★ MIT HEAD a7e86fb60997 README SHA 877831764be9; keeps essentially every block 0.0%/−0.5% *theirs*; mechanical −70.0% Jev −52.1% *theirs*; mock Laya = Jev −22.6% on XL withdrawn; Token reduction alone is not cost reduction; N=18 pilot not Harbor; David-Lolly/Jev-Compatible 3★ HEAD e52e963d8539 README SHA 6e5ff22d40a6; Chat 1282.3 ms vs gateway 232.1 ms ~1/5.5 *theirs*; 3/3 n=3; Softmax over candidate logprobs; Qwen3.8-27B ≠ Archer; wire-compat ≠ logit-equiv; hwfengcs/any2jev 2★ Apache-2.0 HEAD 719b0eb9eefe README SHA 27e0af212cd5; independent not affiliated; acc 0.796 ECE 0.027 *theirs*; 42 ms vs JSON 778 ms *theirs*; Snake acc 0.953 ECE 0.034 *theirs*; Qwen3-0.6B ≠ Archer; /v1/systemone wire-compat ≠ logit-equiv; TianyuCodings/NanoJev densify HEAD 76fdfc9ecdca README SHA a8f8afeb7e44 was 618cea6d / 4190093c64ee; Add JevHarness project link to READMEs; densify §115 not a sibling first sighting; SHA move is not a replica; jjd-lab/jev-synthetic-survey MIT HEAD 9ca8c4ab94bb README SHA ec1664288d50; How you ask mattered more; Noul TVD 0.1530 vs GPT 0.1789 *theirs*; ECE 0.1472 *theirs* not Harbor; missed 0.05 bar; 67.28% vs 64.78% *theirs*; $4.02 vs ~$136 *theirs*; independent work; CankatSarac/jev-arcade MIT HEAD b2e45ed3c1c6 README SHA 1f06af0f4c74; snake 70/80 *theirs*; tetris 167 vs heuristic 2333 *theirs*; 74% conf <0.5 *theirs*; Calibration is not yet measured; three seeds not Harbor; game success ≠ calibrated Noul; sszxt/rlcd HEAD 66ca01664d6b README SHA 3da08d46758d; ECE 0.490→0.423 Brier 0.487→0.409 *theirs*; Yang 2023 contrastive ≠ TypeSafe RLCD; Qwen2.5 ≠ Archer; still overconfident; hf:AXERA-TECH/Laya sha 51a586cd14e2 apache; AX650 NPU 69.991/27.722/69.990 ms *theirs*; seq 256 up to 4 options; serving substrate ≠ calibrated replica; base convaiinnovations/laya; hf:openjev/openjev-MLX-4bit sha c59bf1eed7d8 cc-by-nc-4.0; ~15 GB 4-bit affine; independent not affiliated; hf:openjev/openjev-MLX-4bit ≠ razorback16/openjev; hf:GeekyAbs/laya sha b65d05b4d9eb; GeekyAbs/laya ≠ convaiinnovations/laya; hf:alfred361/laya-web sha 33f171161da5; 100% argmax *theirs*; multilingual-int8 93.8% / worst shift 16.9 pts *theirs*; 50bbx/laya-needle Apache HEAD 01961bade52f README SHA ecaff4dfd271; threshold 0.58 still soft; local Laya ≠ hosted Jev; yunhai-dev/laya2typesafeapi HEAD 4aeb89be286b README SHA d2e5d114fcd8; TypeSafe-compatible ≠ TypeSafe replica; iamdgarcia/openJev MIT HEAD 62bbc30eece2 README SHA 55614ad8caab; independent educational; not local inference; iamdgarcia/openJev ≠ alongL/openJev ≠ Zefan-Cai/Open-Jev; chrisns/homebrew-laya-mac-serve MIT HEAD 1b3c4c0bdb70 README SHA 5e58082b7e9b; tap for chrisns/laya-mac-serve §139; serving substrate ≠ calibrated replica; nk412/judgements MIT HEAD 6624e53c86cc README SHA 86fe465f7887; pydantic wrapper; threshold 0.5 still soft; JingHao-Leon/awesome-jev-apps MIT HEAD d3ef0254c4b2 README SHA fd38a3c4ff2e; catalog ≠ endorsement; JingHao-Leon/awesome-jev-apps ≠ heyjunpenn/awesome-jev; Manta-Boardgame/jev-chat HEAD 44721bae8c2e README SHA 03272e4b9a9f; unofficial; 98% confidence *theirs*; ximing/jev-snake-game HEAD 1e80283f458e README SHA 0a54b74eb095; 用 TypeSafe Jev 驱动的自动贪吃蛇; hf:dataset:syvai/danish-dynaword-laya gated HTTP 401; size_categories 10K<n<100K; devbackend/jevgo ≠ kisshan13/typesafe-ai-go ≠ peach-zhang/typesafe-go; qiudingkai-crypto/jevai and Strernd/beer-jev share README SHA e215bc4ccf13 template collision; skip-thin Adrian-lzr/jev-spire-brain Dililianxice/jev-robotic-arm-benchmark baltzparra/jev-study lzero07/jev-laya-statement qq150078158-lab/TDM-demo empty SHA; Awesomejev 691→802 (+111) / 38194→52151 stars quote watch not re-derive; tracker likes 81 lastModified UNCHANGED; Softmax over options ≠ calibrated Noul; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63; notes.md §140
Hourly 0551 uniqueness lock: jaredpalmer/kev densify HEAD 4f8110a3f862 README SHA d497d4b89427 was e0bcf50153f1 / 84b872488915; Night-2 sign-off; dates+unknowable deltas promoted for 0.8B/4B/9B; v7-base tags; PLAN SHA 5e6d2fca508e; locked OOD 0.684/0.837/0.852 *theirs*; test Kev-9B 0.837→0.852 *theirs*; Kev-4B 0.832→0.837 *theirs*; Kev-0.8B 0.668→0.684 *theirs*; T≈2.0 Brier 0.291→0.267 ECE 0.105→0.039 *theirs*; 7.5%→3.2% *theirs*; grouped T rejected; date_facts deadline 9B 0.72→0.80 raw→0.90 preprocessor; unknowable ≥0.9 → 0.00; 35B Not shipped MMLU-Pro 0.550 *theirs*; coverage@5% 0.62 from 0.66 at 9B *theirs*; not a controlled architecture comparison; Qwen3.5 ≠ Archer; Qwen3.6 ≠ Archer; temperature scaling ≠ ECE unless measured; Hub --revision is a pin not a replica; densify §45 not a sibling first sighting; SHA move is not a replica; bespokelabsai/nimble densify HEAD f136b3f75721 README SHA b3a04a310f1e; Publish original 2676 training examples and frozen 324 holdout; 90.1% vs Jev 93.2% vs base 66.4% *theirs*; did not distill from Jev; densify §35 not a sibling first sighting; AbdelStark/awesome-typesafe-jev 416★ MIT HEAD a6a68b57888a README SHA e47993484e3a github_id 1374058281; Independent community project; catalog ≠ endorsement; AbdelStark/awesome-typesafe-jev IS AbdelStark/awesome-typesafe (same GitHub id 1374058281); cookiespiggy/agentic-rl 103★ MIT HEAD 072bdd8c69de README SHA f2cc68b4e214; ch.25 Jev vs RL; RL ≠ calibrated Noul; DevMortimer/pi-typesafe 27★ MIT HEAD 8dcaa887e22c README SHA 6a11fb9df8b9; DevMortimer/pi-typesafe ≠ twilwa/pi-typesafe ≠ TheoOliveira/pi-jev; hf:gump2049/APUS-OpenJev-v1 sha e7e3cc0b9c82; APUS-OpenJev 9B 85.0% vs Jev API 82.5% *theirs* not Harbor; Frozen80 n=80; Candidate probabilities are not calibrated confidence; Qwen3.5-4B ≠ Archer; Qwen3.5-9B ≠ Archer; hf:SeanLiu/Jev-Vision sha 9b77fa5fdcd0 apache-2.0; POPE 0.907 MME 0.927 NLVR2 0.930 *theirs*; yes/no ECE 0.034 to 0.047 *theirs*; JevBench hard 52% at 91% mean confidence *theirs*; Qwen3-VL-8B ≠ Archer; LoRA ≠ RLCD replica; wire-compat ≠ logit-equiv; hf:SeanLiu/Jev-Vision ≠ sseanliu/Jev-Vision; evoke-build/evoke densify 6★ HEAD ca8a311743fe README SHA fcce876e2cab was 310840b56f1d / 02b91962cef4; Jev is the first adapter the design is bound to no engine; densify §139 not a sibling first sighting; 47thtechcorner/RayCodes_GLiNER_V1_Multi densify HEAD 485cf8045f73 README SHA 035b339c3789; Zero Hallucinations marketing; Locate ≠ decide; kylemclaren/jevsearch ≠ kylemclaren/jev-search ≠ kazuhideoki/jev-search; stacklok/typesafe-go ≠ kisshan13/typesafe-ai-go ≠ peach-zhang/typesafe-go ≠ Nibir1/typesafe-go; sontakey/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ AbdelStark/awesome-typesafe-jev; Giustino98/system-one-bench ≠ mallahyari/system-one-benchmark; skip-thin eatmoreduck/jev-jarvis githubMJ/Laya4j hawkymisc/typed-decision-bert jayanthbagare/laya_examples mohamedAtoui/Jev-project petrixh/laya-test sidhasadhak/jev-perfume-advisor wendaoheri/jev-browser zohaibtanwir/jev-samsho2 empty SHA; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64; notes.md §141
Hourly 0707 uniqueness lock: Sac-Y/Jev-cu 524★ HEAD e2cc92d731fa README SHA 3deeafbc870f; 只传文字，不传截图; Text only no screenshots; Codex CU executes; local policy gates; kyotofin/tax-doc-classifier 322★ Apache-2.0 HEAD 3e95a77f763c README SHA 72c4f74b542e; 100% of our tax document corpus at $0.001 per page; TaxCalcBench 0 strict errors *theirs*; blank IRS 38 strict errors 5.05% *theirs*; 34× cheaper and 6× faster *theirs*; 261 IRS forms; 100% of corpus *theirs* not Harbor; fhshaik/typesafe-mario 319★ HEAD ca22449ed187 README SHA c489f9350414; The model does not receive screenshots; game success ≠ calibrated Noul; droidrun/mobile-jev 307★ MIT HEAD 395fc222beac README SHA d257fed2c5f7; 21 seconds for 9 actions *theirs*; A completed booking is not demonstrated; droidrun/mobile-jev ≠ Friedjof/jev-mobile; realZachi/pg-jev 269★ HEAD afd11fa856d7 README SHA e8735928b57d; giuliosmall/pg_typesafe ≠ realZachi/pg-jev; kitze/skillbox 220★ MIT HEAD cda64ad3310a README SHA dedcb6be3c39; itsmostafa/typesafe-mcp 181★ MIT HEAD d4c110c7edd8 README SHA 2bd68aff4299; itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ burnigtm/jev-mcp; kitze/unclutter 157★ MIT HEAD 9ef9beccc1e5 README SHA 5ad63c67fd02; standardagents/jevpilot 147★ HEAD e1beeb13b9a9 README SHA ec386a81e12c; AbdelStark/awesome-typesafe-jev densify 417★ MIT HEAD d6ea2a0d6cf4 README SHA 234ae59a0b16 was a6a68b57888a / e47993484e3a; The field guide to typed decisions; Independent community project; densify §141 not a sibling first sighting; SHA move is not a replica; hf:Praveenrajus/jev-bench HTTP 401 was 200; densify §107/§125 remainder; *theirs* not Harbor; hf:wayfind/metask-jev-4b-policy-mix densify sha 5ecdd272ab4a README SHA c534ee82b141; densify §134 not a sibling first sighting; wayfind/metask-jev-4b-policy-mix ≠ metask-ai/metask-jev; patryckalves/jev-no-enem HEAD 7f85f787e3d1 README SHA 237b308df062; ENEM 2025 *theirs* not Harbor; 56.6% (103/182) *theirs*; ECE 0.078 *theirs*; Ying-Kai-Liao/jev-browser ≠ wy-coliney/jev-browser-use; w3cj/jev-chat ≠ Manta-Boardgame/jev-chat; snellingio/system-one ≠ sgoedecke/system-one ≠ Luke458/system-one ≠ developerekene/System-One; stoleas/typesafe-computer-use ≠ awlevin/typesafe-computer-use; holotwist/laya ≠ NandhaKishorM/laya; RafalWilinski/vibecheck ≠ psyb0t/vibecheck; dannote/jev ≠ okooo5km/jev ≠ sebastianbugal/jev; skip-thin developerekene/System-One holotwist/laya wuzhiping/jev-laya empty SHA; hf:s1lv3rj1nx/openjev-healthcare-router HTTP 401 *theirs*; hf:s1lv3rj1nx/openjev-heldout HTTP 401 *theirs*; hf:s1lv3rj1nx/openjev-mixture HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65; notes.md §142

**Hourly 0823 HIGH (`notes.md` §143).** dohnuts densify MODEL_CARD. JevBench 65.80% vs Jev 86.58% / Laya multi 47.62% *theirs*. same-species serving not an 18th scoring row. FluidUse field→value match among supplied options not free text. Screenshots aren't uploaded. Jev is the only model. not fully offline. JSON 0.909 letters 0.907 *theirs*. 13 600 / 13 600 *theirs*. softmax over letters ≠ calibrated Noul. model=jev-auto. AG News 0.910 *theirs*. Banking77 0.870 *theirs*. DAIR Emotion 0.480 *theirs*. Fastest and cheapest web agent *theirs*. densify §137 not a sibling first sighting. densify §142 not a sibling first sighting. densify description rewrite. Cua-S1 ≠ TypeSafe. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#66. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 0823 uniqueness lock: PsiACE/dohnuts densify 11★ Apache-2.0 HEAD 253766e5fcb7 README SHA 4b5b019deba9 was a5049834489c / e1b448c440b5; MODEL_CARD + training dataset refs; JevBench 65.80% vs Jev 86.58% / Laya multi 47.62% *theirs*; 152 / 231 *theirs*; 78.21% macro accuracy *theirs*; 180,031 decisions *theirs*; Qwen3.5-0.8B; Joint RLCD *theirs*; Dohnuts ≠ TypeSafe; densify §137 not a sibling first sighting; same-species serving not an 18th scoring row; SHA move is not a replica; FluidInference/FluidUse 3★ Apache-2.0 Swift HEAD c18071d791eb README SHA f1cba4a244bb; on-device Mac form CU; Accessibility API; CUA-S1-FORMS CoreML ~706K params ~1ms Neural Engine; field→value match among supplied options not free text; Cua-S1 ≠ TypeSafe; FluidInference/FluidUse ≠ FluidInference/laya-coreml ≠ AndyInQtr/laya-coreai ≠ mizorewww/laya-coreml; serving substrate ≠ calibrated replica; shhivv/third-hand 274★ MIT Swift HEAD 430394b35dbb README SHA b615d7c3fd19; Screenshots aren't uploaded; Jev is the only model; not fully offline; typesafe-ai/system-one-adapter-python 226★ MIT HEAD adffc2eab300 README SHA d01afbf0499e; Drop-in TypeSafeClient replacement backed by LLM APIs; wire-compat ≠ logit-equiv; typesafe-ai/typesafe-sdk-js 203★ MIT HEAD 66880ccded6c README SHA 7e834076c14e; typesafe-ai/typesafe-sdk-python 175★ MIT HEAD 2ce5c65f1364 README SHA 361a3bc13e19; catalog ≠ endorsement; r-ms/mini-jev 40★ MIT HEAD ca612198bfb6 README SHA 565b70c4cf4d; read the option letter's logits instead of generating JSON; yuki-oshio/mini-jev ≠ r-ms/mini-jev; JSON 0.909 letters 0.907 *theirs*; 13 600 / 13 600 *theirs*; softmax over letters ≠ calibrated Noul; Das-rebel/a3m-router 16★ MIT HEAD 62caefe59315 README SHA c19e802d5cf2; model=jev-auto; routing ≠ permission; AbdelStark/jev-benchmarks 13★ Apache-2.0 HEAD 0d610cc53e79 README SHA 5fd3627f7de4; AG News 0.910 *theirs*; Banking77 0.870 *theirs*; DAIR Emotion 0.480 *theirs*; *theirs* not Harbor; browser-use/jev-ultrafast densify 14622★ MIT HEAD 1231850a0bf1 README SHA fa7d079f9192; Fastest and cheapest web agent *theirs*; densify description rewrite; pythongiant/laya-drift densify 4★ HEAD 334953e5cb8f README SHA 6662121ba0f3 was fc94b71cf7dd / 55ef2343ee5d; opencode plugin to calculate agentic drift over time *theirs*; densify §142 not a sibling first sighting; BlinkWrite/pii-masker densify 1★ MIT HEAD 6ad202ab4443 README SHA 27931758af6c; On-device reversible PII masking *theirs*; Locate ≠ decide; TypeSafeAI/typesafe-playground ≠ kavehmz/typesafe-playground ≠ nickthompson480/typesafe-ai-playground; siliconkernel/vllm-jev-decison 8★ MIT HEAD a9362d52b9a8; No generative fallback; Stumble/jev-go 3★ MIT HEAD a475dc925ba6; Twister915/typesafe-ai 11★ Apache-2.0 Rust HEAD d4455efb1d06; rorshopping/jev-on-a-laptop 23★ HEAD 5821d9106103; Unofficial research repo. Not affiliated with TypeSafe AI; Qwen2.5 ≠ Archer; skip-thin GokhanCalkap/LayaCode fredzhaozonghui/LAYA1 empty SHA; Abhi895/Laya ≠ convaiinnovations/laya; mjdileep/OpenJev ≠ Zefan-Cai/Open-Jev; Abhi001vj/system-one-open ≠ mithalouni/system-one-open ≠ sgoedecke/system-one; ZulfiFazhar/system-one ≠ sgoedecke/system-one; Futureppo/typesafe_register key-farming skip; soft scores ≠ hard gates; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66; notes.md §143

**Hourly 0923 HIGH (`notes.md` §144).** intellyweave GLiNER OSINT. Locate ≠ decide. openvons finite choices + none. 4B frozen+head 0.916 vs 27B zs 0.875 *theirs*. 8 questions 22.6 ms *theirs*. softmax ≠ calibrated Noul. AgentBeam local security layer. soft scores ≠ hard gates. unofficial not affiliated. wire-compat ≠ logit-equiv. chips virtual. game success ≠ calibrated Noul. densify §121 not a sibling first sighting. densify §139 not a sibling first sighting. densify §141 not a sibling first sighting. Runs every rule against every line in parallel. No skimming. Median 275 ms. trolley 0.99 vs 0.78. 11/11/7 match/differ/undecided of 29 *theirs*. retired name reservation is not a replica. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#67. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 0923 uniqueness lock: vericle/intellyweave 76★ BSD-3-Clause Py HEAD ff4152ce9d20 README SHA 3afa702012e8; GLiNER OSINT; Locate ≠ decide; genai-craft/openvons 13★ NOASSERTION Py HEAD c2683c4539a7 README SHA 85164d409725; finite choices + none; 4B frozen+head 0.916 vs 27B zs 0.875 *theirs*; 8 questions 22.6 ms *theirs*; softmax ≠ calibrated Noul; whyashthakker/beam-cli 11★ AGPL-3.0 TS HEAD 5162ec66179a README SHA d55847ca5681; AgentBeam local security layer; soft scores ≠ hard gates; atharvamhaske/typesafe-sdk-go 8★ MIT Go HEAD 6ea04182d356 README SHA 8d90abda1f58; unofficial not affiliated; wire-compat ≠ logit-equiv; atharvamhaske/typesafe-sdk-go ≠ kisshan13/typesafe-ai-go ≠ stacklok/typesafe-go ≠ Nibir1/typesafe-go ≠ peach-zhang/typesafe-go ≠ draganm/go-jev ≠ kataras/jev ≠ robertjndw/gosys1 ≠ Stumble/jev-go; Prophetlab/JevPokerBench 7★ MIT Py HEAD 9c9816688a3c README SHA 0fcd6807b9c3; chips virtual; game success ≠ calibrated Noul; *theirs* not Harbor; tyler-dot-earth/patdown densify 11★ NOASSERTION TS HEAD 8b2b2b591470 README SHA 1052b6da2c25 was ae0e277fdd64 / 275f4b9c; Block/steer/fuzzy lint; judge swappable; default TypeSafe/Jev; provider-neutral; densify §121 not a sibling first sighting; evoke-build/evoke densify 8★ Apache-2.0 Rust HEAD 50c9637ef11f README SHA 72ec0e65c432 was ca8a311743fe / fcce876e2cab; Jev is the first adapter; the design is bound to no engine; densify §139 not a sibling first sighting; lukstei/slop-grader 5★ MIT TS HEAD b60332684ff8 README SHA bbc1604754d3; Runs every rule against every line in parallel. No skimming; sumleo/prompt2jev densify 2★ MIT Py HEAD f3b6bc763b74 README SHA 3d58e8c10075 was bd9cd8a471a6 / afc36885861e; heuristic conversion ≠ calibrated Noul; densify §141 not a sibling first sighting; Andymulb/jev_the_philosopher 0★ MIT TeX HEAD 334e3f9b83e5 README SHA 8db05448b75f; Median 275 ms; trolley 0.99 vs 0.78; 11/11/7 match/differ/undecided of 29 *theirs*; PerryLink/layacore 0★ Apache HEAD 12afe3af5edc README SHA f78b73d21cf7; retired name reservation; the project is now PerryLink/laya-mcp; retired name reservation is not a replica; PerryLink/layacore-mcp HEAD b006cc7c3f87 README SHA 1177f286f3f8; PerryLink/laya-mcp-npm launcher not implementation HEAD 426e965b4c48 README SHA 98ed0d448b09; PerryLink/laya-mcp ≠ wsargent/laya-mcp; DreamBlooms/dohnuts.cpp ≠ PsiACE/dohnuts; ClemensSchartmueller/jev-guard ≠ leepokai/jev-guard ≠ seb4ez/jevguard; AABBAASS1/jev-router ≠ gargpratyush/jev-router ≠ Akashdb5/jev-router ≠ daviddl9/jev-router; wustep/jev-playground ≠ AbnormalPilot/jev-playground ≠ mizchi/jev-playground; Li-Evan/awesome-jev ≠ Omrigotlieb/awesome-jev ≠ youzizzz1028/Awesome-Jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; sunchojack/jev-cli ≠ gnapse/jev-cli; Alistair77/openjev ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev; jev-jarvis/jev-jarvis ≠ eatmoreduck/jev-jarvis; Renwang-Huang/typesafe-mcp ≠ itsmostafa/typesafe-mcp; inematds/laya ≠ convaiinnovations/laya ≠ NandhaKishorM/laya; kataras/jev ≠ okooo5km/jev ≠ sebastianbugal/jev ≠ dannote/jev; ai-ecoverse/kev.js ≠ jaredpalmer/kev; skip-thin gnapse/jev-cli HTTP 404 fr4j4/system-one-arena nothingmn/Jev.Sdk youniszhang/jev-local Vaibhaav-Tiwari/fly-doom-jev fengliner/jev-tank-battle ngouard5/jeveuxaider-design empty SHA; hf:Skylarcc/Laya-Online HTTP 401 *theirs*; hf:piratehack009/laya-cn-flash-triage HTTP 404 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67; notes.md §144

**Hourly 1019 HIGH (`notes.md` §145).** praneeth16 GEPA ADE Corpus V2. schema-valid is not the same as correct. API confidence is not P(correct). GEPA revises Choice instructions/criteria with weights fixed. jev-1.13.0 weights fixed. Brier 0.1357→0.0747 *theirs*. F1 69.1%→79.7% *theirs*. FN 4→6. review-queue policy is not F1. Soft is not gate. Not an 18th scoring-table species. Every claim is labeled and sourced. catalog ≠ endorsement. 发送永远手动. About 180 ms. routing ≠ permission. $0.00241 *theirs*. Not a screenshot agent. game success ≠ calibrated Noul. pi-follow-through threshold 0.8 still soft. wire-compat ≠ logit-equiv. densify §144 not a sibling first sighting. pi-jev-context densify §134 not a sibling first sighting. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#69. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1019 uniqueness lock: praneeth16/adapting-jev-with-gepa ADE Corpus V2 GEPA; schema-valid is not the same as correct; API confidence is not P(correct); GEPA revises Choice instructions/criteria with weights fixed; jev-1.13.0 weights fixed; Brier 0.1357→0.0747 *theirs*; F1 69.1%→79.7% *theirs*; FN 4→6; review-queue policy is not F1; Soft is not gate; Not an 18th scoring-table species; aliaihub/awesome-jev-usecases 15★ NOASSERTION HEAD 6cbde6bd3569 README SHA 7ea135c6345d; Every claim is labeled and sourced; catalog ≠ endorsement; aliaihub/awesome-jev-usecases ≠ anandi1989/awesome-jev-usecases ≠ whyashthakker/awesome-jev-use-cases; rezoch340/jev-chat-JARVIS-windows 6★ MIT Py HEAD 26b686301437 README SHA 0714736b68c3; 发送永远手动; rezoch340/jev-chat-JARVIS-windows ≠ Finderchangchang/jev-chat-JARVIS; iamvatsalpatel/tiershift 3★ MIT TS HEAD 16a0826b9f62 README SHA 46fcb1cb191b; About 180 ms; routing ≠ permission; Bring-AI/jev-rl 2★ MIT Py HEAD 36f89cec85a2 README SHA 6283da6011b7; $0.00241 *theirs*; daniel4x/JevEmon 2★ GPL-3.0 HEAD 572454c69bf7 README SHA 8fc00d12848d; Not a screenshot agent; game success ≠ calibrated Noul; spoonnotfound/soupbase 2★ MIT TS HEAD 3e874e83e710 README SHA 3106bc96d6ab; Nabsku/pi-follow-through 1★ MIT TS HEAD c62ef28ff4ac README SHA 64000451b79e; pi-follow-through threshold 0.8 still soft; dashbi1/jev-sim 1★ MIT Py HEAD 753c7397d73c README SHA 05fd960799d2; wire-compat ≠ logit-equiv; jev-jarvis/jev-jarvis densify 8★ MIT Py HEAD a94e3b967ef5 README SHA e441335b1df0 was be68dd7993f0 / efe7e47a6fe8; densify §144 not a sibling first sighting; Nyarlathoteppppp/pi-jev-context densify 5★ MIT TS HEAD 96371e2bf144 README SHA d4276222a436 was f0128a86478f; pi-jev-context densify §134 not a sibling first sighting; Nyarlathoteppppp/pi-jev-context ≠ kevinpita/pi-jev-context; fly88oj/jebii 0★ MIT JS HEAD 5cbe527ed791 README SHA b4a76b8aba9d; generallymatthew/factlabel 0★ Apache-2.0 Py HEAD b3d3bceee044 README SHA b1cda6c4646e; aakgna/jevcal ≠ abhixhek/jevcal; 007M7/jev-chat ≠ w3cj/jev-chat ≠ Manta-Boardgame/jev-chat; fstandhartinger/jev-router ≠ gargpratyush/jev-router; prakash7474/Jev_guard ≠ leepokai/jev-guard; rdutra/laya-mcp ≠ PerryLink/laya-mcp ≠ wsargent/laya-mcp; Kourin1996/jev-playground ≠ wustep/jev-playground; ai-ecoverse/cua-s1.js Cua-S1 ≠ TypeSafe; skip-thin Unnati-23/jev-typesafe-guide antoniofaical/digital-twin-classifier-jev leonezhu/agent-kits empty README; skip-thin wjw66/deepseek-harness-jev-pre-compaction ziwon/jev-actor empty SHA HTTP 409; hf:chanoian/openjev-mlx-demo HTTP 401 *theirs*; hf:clduab11/jev-calibration-statistics HTTP 401 *theirs*; hf:yasserrmd/laya-lab HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69; notes.md §145

**Hourly 1110 HIGH (`notes.md` §146).** hf:thaitea/laya-vision SmolVLM typed vision decisions. same-species serving not an 18th scoring row. A-OKVQA 63.1% ECE 0.266 to 0.094 *theirs*. act head untrained do not gate on it. codearia-sieve page to typed fields. 11 of 11 *theirs* not Harbor. gemma-jev JSON chat ≠ calibrated Noul. local-decision-model independent from the public post. musubi-jev README is a kev tree copy. copied kev numbers are not a musubi bench. vllm2jev wire-compat ≠ logit-equiv. pg-laya serving substrate ≠ calibrated replica. jev-rerank ranking ≠ calibration. typesafe-mcp decision is code. act_above 0.8 still soft. densify §142 not a sibling first sighting. densify §145 not a sibling first sighting. densify §143 not a sibling first sighting. densify §139 not a sibling first sighting. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23-#70. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1110 uniqueness lock: hf:thaitea/laya-vision 13 likes sha a2653db2831b cc-by-nc-sa-4.0; SmolVLM-256M vision typed choice/score/noul; same-species serving not an 18th scoring row; independent not affiliated; A-OKVQA 63.1% ECE 0.266 to 0.094 *theirs*; ScienceQA 89.0% ECE 0.080 to 0.034 *theirs*; VQAv2 noul 73.2% ECE 0.085 to 0.042 *theirs*; All n=8235 75.9% ECE 0.035 *theirs* not Harbor; VQAv2 re-split not comparable to published VQAv2; about 71 ms *theirs*; option order varies 1.2 points *theirs*; act head untrained do not gate on it; not a drop-in replacement for Laya text checkpoint; usage loads thaitea/laya-vision-smolvlm-256m already §87; hf:thaitea/laya-vision ≠ thaitea/laya-vision-smolvlm-256m card id; AntonG87/codearia-sieve 1★ MIT TS HEAD 64ecd4151726 README SHA b03a3d29ab22; page to typed fields; 6 of 6 *theirs*; 11 of 11 *theirs* not Harbor; robots-disallowed did not fetch; no model required for the parse; 7Zenox/gemma-jev 0★ NOASSERTION Py HEAD 2eed119e03ff README SHA c3b58d6a15a9; generation-free letter slots; 144 authored decisions *theirs*; Gemma 3 270M 0.293 below chance 0.333 *theirs*; Gemma 4 E2B-it JSON chat 0.807 *theirs*; Qwen3.5-4B JSON chat 0.813 *theirs*; JSON chat ≠ calibrated Noul; softmax over letter slots ≠ calibrated Noul; bf16 vs fp32 argmax-agreement check not run; Gemma ≠ Archer; Qwen3.5 ≠ Archer; Pdbz199/local-decision-model 0★ MIT Py HEAD ddceb5829849 README SHA 80659ec966f5; independent project built only from the public post; one pass no generation; schema-valid is not the same as correct; musubi-labs/musubi-jev 0★ Apache-2.0 HEAD e943f21e4057 README SHA 8ffd43564204; README is a kev tree copy; copied kev numbers are not a musubi bench; musubi-labs/musubi-jev ≠ jaredpalmer/kev; quaeast/vllm2jev 0★ NOASSERTION Py HEAD 8a51f94961ea README SHA be92356f1176; does not reproduce Jev calibration; wire-compat ≠ logit-equiv; IAmJSD/pg-laya 0★ Apache-2.0 Rust HEAD 1bc66a4d6a7f README SHA 03476be41744; SQL choice score noul; serving substrate ≠ calibrated replica; IAmJSD/pg-laya ≠ realZachi/pg-jev ≠ giuliosmall/pg_typesafe; gbesse/jev-rerank-server 0★ MIT JS HEAD b28cef5e34a6 README SHA 91167c66c29c; SciFact n=25 nDCG@10 0.616377 to 0.718260 *theirs*; Recall@10 0.84 unchanged *theirs*; ranking ≠ calibration; MarkChu-git/typesafe-mcp 0★ MIT HEAD a064b14207c0 README SHA ae27210cc5af; decision act/review/abstain is code; act_above 0.8 still soft; MarkChu-git/typesafe-mcp ≠ itsmostafa/typesafe-mcp ≠ cyrusasco/typesafe-mcp ≠ Renwang-Huang/typesafe-mcp; pythongiant/laya-drift densify 4★ TS HEAD d33db6736ed8 README SHA 7af1781c28c5 was 334953e5cb8f / 6662121ba0f3; monitor agent drift; densify §142 not a sibling first sighting; Adkid-Zephyr/chinese-workflow-decision-bench densify 1★ MIT Py HEAD b694dc6dbcba README SHA 9ef2b7d76a37 was 6d0a7c2af303 / 4ed71a36cd51; 64/64 and 63/64 *theirs* not Harbor; synthetic not a group-chat dump; densify §145 not a sibling first sighting; turenlabs/jast densify 1★ MIT Rust HEAD c6588285208f README SHA d9214ca31f92 unchanged; star 0 to 1 is star-noise; densify §145 not a sibling first sighting; JabbaKadabra/SystemOneDotNet densify MIT C# HEAD 5120ffb84cc5 README SHA 0809f98d4c93 was 5bff3394281c / 76a9188c180a; unofficial .NET client; wire-compat ≠ logit-equiv; densify §143 not a sibling first sighting; arnavm-codes/JevFence densify HEAD 7e277474ff5e README SHA 2bbb684757de was 6fe62ca7b10c / 5441aaeaace0; soft scores ≠ hard gates; densify §145 not a sibling first sighting; cloudbtl/JevRAG 0★ Apache-2.0 Py HEAD 307ab19ee9cf README SHA 9b814bb6624b; first card revisit tag no prior notes card; cloudbtl/JevRAG ≠ emretheus/jev-rag-benchmark ≠ erendikmenn/jev-rag-benchmark; gbesse/decision-workbench densify MIT JS HEAD 877d1a9add5b README SHA 24cce8900d67 was 8889cf3750a3 / 14a3bf79da7a; human review separate from model output; demo scores are not accuracy measurements; densify §139 not a sibling first sighting; 0xagentlabs/jev-xiangqi ≠ Zafer-Liu/jev-xiangqi; RyanNg1403/jev-cli ≠ gnapse/jev-cli ≠ sunchojack/jev-cli; KennethAshley/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev; malevrigns/agent-jev ≠ hf:aimeigaoshou/agent-jev; 79.25% 1585/2000 ECE 0.1687 *theirs* not Harbor; kidzik/jiffy probabilities are uncalibrated; s3rli/jevips name collision not a decision model; skip-thin Alpha-Harper-Franklin/astra-jev jonas050210/Laya_Playground pietrushka/jev-youtube-filter empty SHA HTTP 409; skip-thin THANK-YOU-FOR-YOUR-ORDER-ASDF123/repo-laya4qxd Ylr9933/JevForAgent empty README; hf:marcmagn1/jev-alt-systemone-eval dataset sha 95f679e8455b README 404 models HTTP 401 *theirs*; catalog ≠ endorsement; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70; notes.md §146

User-provided glance uniqueness lock: yoheinakajima/glance Apache-2.0 Py HEAD 8f36e063bffb README SHA b57280394bc1 LICENSE SHA d645695673349e; 4★; 1 fork; star-noise is not the fold; size 51490; pushed 2026-09-21T17:37:40Z; created 2026-09-21T06:51:38Z; PyPI glance-vlm 0.3.1; tag v0.3.1; site https://glance.yohei.me; topics calibration, image-classification, vision-language-model, vlm, zero-shot; Ask an open vision-language model typed questions about an image and get probabilities back, on your own machine; frozen open VLM default Qwen3-VL-4B Apache-2.0; yes/no pick-one and default unfitted rating read from answer-token logits in one forward pass; default unfitted rating is jsondigits (1 pass, exact 0.669); labeled glance fit uses ens4d (4 passes); four-pass zero-shot rating 0.570 behind write JSON 0.672; glance fit --unlabeled uses jsondigits; fast2 (2 passes) and digits (1 pass) remain available; Glance is a calibration and measurement harness around that readout. It is not a model; trains no weights; images never leave the machine; local server binds 127.0.0.1; noul yes/no choice pick-one score ordered rating; POST /v1/decide; zero-shot table only yes/no 0.939 pick-one 0.933 rating exact 0.669 *theirs*; Gemini 3.1 Flash-Lite yes/no 0.961 pick-one 0.933 rating 0.763 *theirs*; fitted readout marked fitted do not say zero-shot or no training: unlabeled image-quality 0.67 to 0.76 exact (README; CLAIMS one-pass 0.758 at 16 unlabeled images) *theirs*; labeled about 32 images 0.86 exact ECE about 0.03 per rubric does not transfer *theirs*; Glance is not an image-quality metric; on KADID-10k it misses their own targets; do not quote interim KADID numbers; Q-SiT-mini 0.9B trained for image quality is level under the same 32-label fit; hand-built features beat it on low-level artifacts when labels are plentiful; non-image-quality rubrics 0.55 exact with 300 labels *theirs*; tilt 0.33 *theirs*; geometric probes diagonals 0.30 largest of four shapes 0.52 eight objects 0.56 *theirs*; stripe direction hidden-state linear probe 0.99 *theirs*; raw yes/no ECE 0.111 and 0.179 *theirs*; pooled two-number Platt map on those suites ECE 0.061 and 0.053 *theirs*; transfer to a new yes/no task untested; glance fit is a per-rubric rating map not that Platt map; explicit other held-out breeds 7.7% *theirs*; claims ledger: faster or cheaper than Jev do not claim; shares inference object with featherless-ai/simple-jev hr98w/jev-visual zhengxuyu/litjev; request and response shapes follow TypeSafe Jev hosted text; yoheinakajima/glance ≠ TypeSafe Jev; POST /v1/decide ≠ TypeSafe /v1/systemone ≠ IamBusy/OpenJev /v1/decide is a wire lock not OpenJev v2 identity; OpenJev v2 is Hub AlexWortega/openjev trained 4B multimodal claim scorer census §77 do not mint a sibling card; OpenJev v2 ≠ Zefan-Cai/Open-Jev ≠ razorback16/openjev ≠ IamBusy/OpenJev-Vision; Zefan-Cai/Open-Jev §125 is a separate trained-head namesake; trains no weights unlike YOFO and unlike hf:thaitea/laya-vision §146 and unlike OpenJev v2 and unlike IamBusy/OpenJev-Vision; harness not weights; soft probs for threshold abstain rank; soft scores ≠ hard gates; logits are not calibrated probabilities of correctness; *theirs* not Harbor; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72; notes.md §147

Hourly 1203 uniqueness lock: peterfriese/jev-foundation-models Swift 6 bridge into Apple Foundation Models; peterfriese/jev-foundation-models 1★ Apache-2.0 Swift HEAD 27963995965d README SHA b40b836f4396; 40 to 150 ms *theirs*; zero hallucinations is a README claim *theirs*; Never embed API keys; bridge is not an on-device replica; Apple Foundation Models host the call shape; Jev remains the decision model; Alexander-Ollman/laya-ft signal detection; Alexander-Ollman/laya-ft 0★ NOASSERTION Py HEAD 41f8247c3969 README SHA e97e314c88d5; Aegis prompts F1 60.6% 81.5% 83.7% *theirs*; Aegis responses 37.4% 69.5% 77.0% *theirs*; ToxicChat 36.4% 50.5% 53.3% *theirs*; WildGuard prompts 48.7% 59.4% 65.7% *theirs*; WildGuard responses 20.8% 53.3% 51.6% *theirs*; BeaverTails 6.0% 34.1% 59.4% *theirs*; false alarms 24.8% to 65.2% to 47.2% *theirs*; XSTest 250 harmless prompts *theirs*; 67,890 decisions *theirs* not Harbor; No Jev outputs were used; not a dependable general-purpose safety filter *theirs*; detection gain is not a license to auto-block; Soft judgment never sole veto; Ejokey/lightjev $0.000851 in 23.6s *theirs*; Ejokey/lightjev 0★ MIT Py HEAD 921fffb588b9 README SHA 30fa74b9f711; six pages four hits 3/3 *theirs*; about $0.0001 per decision *theirs*; STOP always available; one crawl is not Harbor; code owns the queue; ruslanlap/jev-gate measured $0.000143 *theirs*; ruslanlap/jev-gate 0★ MIT Py HEAD 300014a1bdea README SHA 96e31d8dc5d8; exit code 2 is code; noul p=0.02 is not a merge; five typed questions; probabilities must sum to 1 within 0.02 *theirs*; ruslanlap/jev-gate ≠ hf:SargeDev/jev-gate-student-b-merged; Renwang-Huang/arbitype independent not an official TypeSafe product; Renwang-Huang/arbitype 0★ MIT Py HEAD 454cf2c4a345 README SHA ffa11f281a52; PyPI 0.6.0 pending; Renwang-Huang/arbitype ≠ Renwang-Huang/typesafe-mcp; Codercise/jev-in-practice key stays in the Node process; Codercise/jev-in-practice 0★ MIT TS HEAD 02be666a30ad README SHA 3f0c47161028; playground is not a bench; fraud sales patent presets; emlama/jev-mcp saved tool is inputs context questions docs; emlama/jev-mcp 0★ MIT Py HEAD 4c7da93a21be README SHA a258eb52829c; emlama/jev-mcp ≠ burnigtm/jev-mcp ≠ jkudish/jev-mcp ≠ resumocast/jev-mcp ≠ tphakala/jev-mcp; single SQLite volume; hf:clduab11/jev-calibration-statistics HTTP 200 was 401; hf:clduab11/jev-calibration-statistics 0 likes sha 9bbe055ee875 mit; sha 9bbe055ee875 was 13f4fa48f2f2; 0.612 against 0.740 *theirs*; missed its main pre-registered bar *theirs*; AUROC 0.899 *theirs*; 9,075 passages 349 questions *theirs*; jev-1.13.0; Gemma 4 ≠ Archer; densify §145 not a sibling first sighting; hf:aimeigaoshou/agent-jev sha 024a68eade83 was 7d433994fbde; hf:aimeigaoshou/agent-jev 0 likes sha 024a68eade83 apache-2.0; verified:false; accuracy 0.7925 ECE 0.1687 Brier 0.0448 *theirs*; same numbers as §146 not a new Harbor; Qwen3-0.6B ≠ Archer; malevrigns/agent-jev ≠ hf:aimeigaoshou/agent-jev; densify §146 not a sibling first sighting; AkashPriyadarshii/jev-seo densify HEAD f42455ac951a was f8cb7c55c356; AkashPriyadarshii/jev-seo 27★ MIT Rust HEAD f42455ac951a README SHA 677171501c8e; README SHA 677171501c8e was e3290fd15add; 27★ was 21★; densify §131 not a sibling first sighting; catalog ≠ endorsement; dtduc-git/jevnav densify HEAD b7a12d2f54ce was 96f5438bea96; dtduc-git/jevnav 1★ Apache-2.0 Py HEAD b7a12d2f54ce README SHA 61ea35cc8f32; page truth not pixels; replay exits 1 with no model call *theirs*; densify §129 not a sibling first sighting; star 0 to 1 is star-noise; dtduc-git/jevnav ≠ pstong216/jevnav-demo; SoundBlaster/SwiftDecision first card revisit tag no prior notes card; SoundBlaster/SwiftDecision 0★ Apache-2.0 Swift HEAD 7af9416e1ac4 README SHA 54ad5d8e4886; Models propose. Application keeps policy; SoundBlaster/SwiftDecision ≠ peterfriese/jev-foundation-models ≠ SoundBlaster/SwiftDecision-Examples; Tongyun1/Jev-in-the-Loop densify HEAD 039c2117f4e3 was a60444c0c268; Tongyun1/Jev-in-the-Loop 0★ MIT Py HEAD 039c2117f4e3 README SHA ffe54ee54576; README SHA ffe54ee54576 was e4ebd224d5f8; Codex prepares inputs Jev picks the next action; operating a browser is not a calibrated Noul; hfnissum-byte/jevmerge code enumerates model picks code gates; hfnissum-byte/jevmerge 1★ NOASSERTION JS HEAD 2b472ca7304b README SHA b32e85e4909c; prakash5284 n=10 is not Harbor; $0.0019 *theirs*; theglitcharchitect/muse-skills shadow mode proceeds anyway; skip-thin Elue-dev/jev_elixir Shoaib-Asghar/jev-probe lvzhaobo/-jev-assayer empty SHA HTTP 409; ravinarayanan89/JevForce HTTP 404; jevonj05/jevonj05 name collision not a decision model; sunmont/pi-jev-dsk-agi acronym expansion is not TypeSafe Jev; hf:opg13/laya about 33 ms *theirs* not Harbor; hf:marcmagn1/jev-alt-systemone-trackio ≠ hf:marcmagn1/jev-alt-systemone-eval; game success ≠ calibrated Noul; does not execute; routing ≠ permission; *theirs* not Harbor; SHA move is not a replica; wire-compat ≠ logit-equiv; serving substrate ≠ calibrated replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72; notes.md §148; peterfriese/jev-foundation-models 1★ Apache-2.0 Swift HEAD 27963995965d README SHA b40b836f4396; AbdelStark/abdelstark.github.io 0★ NOASSERTION HTML HEAD bd54fa76189c README SHA 8f7523bcaf57; Alexander-Ollman/laya-ft 0★ NOASSERTION Py HEAD 41f8247c3969 README SHA e97e314c88d5; AustinDKB/grass-optimizer 0★ NOASSERTION Py HEAD 6a0616ab83e1 README SHA e7ee8271da7e; BipinRajC/Jev-api-experiments 0★ NOASSERTION Py HEAD e57a266df0ea README SHA cee6481e2e5b; Codercise/jev-in-practice 0★ MIT TS HEAD 02be666a30ad README SHA 3f0c47161028; DevvGwardo/ghost-route 0★ MIT TS HEAD ca4e40fd94b4 README SHA b4be5c1f6893; Ejokey/lightjev 0★ MIT Py HEAD 921fffb588b9 README SHA 30fa74b9f711; Elue-dev/jev_elixir empty SHA HTTP 409; Georgy-hook/laya-rimworld-director 0★ GPL-3.0 Py HEAD fb82dbf34562 README SHA f25b95e16247; Jorgediamanto/jev-playground 0★ NOASSERTION Py HEAD b3b3d2d8f8db README SHA 7b9972acca45; Lavenir7/Jev2048 0★ NOASSERTION JS HEAD 9e8785ba82e1 README SHA aabbb986b729; Makia9879/pi-jev-router 0★ NOASSERTION TS HEAD 2f6aed131dc8 README SHA 81b43e3994fd; NikHeck/jev-benchmark 0★ NOASSERTION Py HEAD 4997038a2902 README SHA 9e6d3a30ef4b; Renwang-Huang/arbitype 0★ MIT Py HEAD 454cf2c4a345 README SHA ffa11f281a52; Shoaib-Asghar/jev-probe empty SHA HTTP 409; SoundBlaster/SwiftDecision-Examples 0★ MIT HEAD 378c8bc4564f README SHA 05e313ca7b00; Sy3058/jev-evaluate 0★ NOASSERTION Py HEAD 4e6424305b27 README SHA 9a4f7fc26e43; UtpalJayNadiger/find 0★ ISC TS HEAD 44247083ac90 README SHA 670a74958a92; ahtcfg24/codex-speculator 0★ MIT TS HEAD 8496757f0c86 README SHA 6caece2fcb2e; allebee/jevgrep 0★ MIT Py HEAD e7ec44aa801d README SHA 96102d2f6a22; allebee/pytest-jev 0★ MIT Py HEAD b24310cccf43 README SHA 7ab5e2e57a5a; babanomania/linkedin-bullshit-filter 0★ MIT TS HEAD 2838b3c6dc76 README SHA 408ff8140090; bangxiao0927/decidespeak 0★ Apache-2.0 Py HEAD 6558e1a9b157 README SHA d1b95ca6b74b; bitofant/laya 0★ NOASSERTION HEAD f9335cb99e9b README SHA 1a26983aef62; coreywoo27/Jev-Empowered-Qwen-mlx 0★ MIT Py HEAD a14c9b924351 README SHA 2131d40716fc; cornelflorea/jev-test 0★ NOASSERTION TS HEAD 42cadf15cc79 README SHA 35db91381f38; dannyowelch/jev-abstention-checker 0★ NOASSERTION TS HEAD fb2a0afa6220 README SHA acf5b81da07f; dante01yoon/laya-jev-arena 0★ NOASSERTION JS HEAD 4a723c55d31c README SHA a1280d76ddcd; datamonsterr/jev_auto_select_skills 0★ NOASSERTION TS HEAD ffa748ef2cab README SHA 37cd6e7ca9c4; diluteoxygen/JevName 0★ NOASSERTION JS HEAD 08f239452851 README SHA 4598ba81b321; edrache/jevworms 0★ NOASSERTION JS HEAD e79d677c7714 README SHA 098a1d2d3af3; emerson-buoy/jev-ticket-classifier 0★ NOASSERTION TS HEAD a51bd3faf388 README SHA 6a2f242d2409; emlama/jev-mcp 0★ MIT Py HEAD 4c7da93a21be README SHA a258eb52829c; fblissjr/typesafe-experiments 0★ MIT TS HEAD 0d21b21d3c0e README SHA 81d2df816c34; frahlg/laya-ems-test 0★ Apache-2.0 Py HEAD a7f72577dc0e README SHA 35993b958438; hazlema/jev-connect4 0★ MIT TS HEAD be4f9757a820 README SHA bcef5ccd0859; hf:marcmagn1/jev-alt-systemone-trackio 0 likes sha e8fe2df8f29c NOASSERTION; hf:opg13/laya 0 likes sha 99175af5d679 apache-2.0; hfnissum-byte/jevmerge 1★ NOASSERTION JS HEAD 2b472ca7304b README SHA b32e85e4909c; ishantanu/jevtraces 0★ Apache-2.0 Go HEAD 7053acccc254 README SHA f83ca85d1641; jayozer/jevzero 0★ MIT Py HEAD 601228d24a8a README SHA 1a6c376f01ef; jeonck/clinic-checklist 0★ NOASSERTION Py HEAD b693bfa56d42 README SHA e2bb49fe9f2a; jevonj05/jevonj05 0★ NOASSERTION Py HEAD eaf07387d305 README SHA 3743fe2fb819; jordilopez/pi-smart-router 0★ NOASSERTION TS HEAD 2cd38cc56af1 README SHA 89c03c160a85; karanb192/jev-skill-scout 0★ MIT JS HEAD a10b1a1fe71b README SHA 638dd7042894; ljbuturovic/jevgram 0★ NOASSERTION Py HEAD 73185b0df270 README SHA 2af501753734; luisrapalino/jev-smart-bets 0★ MIT TS HEAD a606f2b45195 README SHA 0f3714226f74; lvzhaobo/-jev-assayer empty SHA HTTP 409; lvzhaobo/jev-assayer 1★ NOASSERTION Py HEAD 795031c93e71 README SHA 7fe614bdf174; makiisthenes/JevAIExperimentation 0★ NOASSERTION Py HEAD dae1c2f867d0 README SHA e69de29bb2d1; moelahmady/shunt-jev 0★ MIT TS HEAD 47285110cf2a README SHA 2332516baf23; naiersaidane/jev-demos 0★ NOASSERTION TS HEAD dd8d6fe03da6 README SHA 6a41ac881196; olivere/systemone 0★ MIT Go HEAD fe90e12af0a0 README SHA ede6fced042e; p2kalita/Building-a-Harness-with-Jev-LangChain 0★ NOASSERTION Py HEAD 7c7318ebe703 README SHA 38bc6d9acddc; pavlealeksic/jev-hermes 0★ NOASSERTION Py HEAD ff858e957322 README SHA 2444a463e79c; perezjohn0/jevpav 0★ NOASSERTION HEAD 3185ac2bc377 README SHA ad253f8dfe83; piyushsonawane07/trueKeep 0★ NOASSERTION TS HEAD a072d99e6034 README SHA a217f090c99d; prakash5284/jev-vs-llm-resume-jd-eval 0★ NOASSERTION Py HEAD d9a80a8a00f4 README SHA 06b2104f5b63; pratik-codechef/jev-model 0★ NOASSERTION TS HEAD 5b3a8fb21b50 no README; punitarani/jeve 0★ NOASSERTION Py HEAD c12c66b809da README SHA 631ba86611e4; ravinarayanan89/JevForce HTTP 404; rishhavv/tabjev 0★ MIT JS HEAD 9b4abd1ee7d6 README SHA 15cbe787df05; ruslanlap/jev-gate 0★ MIT Py HEAD 300014a1bdea README SHA 96e31d8dc5d8; sathwikkuncham/laya-snake-arena 0★ Apache-2.0 Py HEAD e7227d789501 README SHA 6947e635bc72; shivpratapsinghpanwar/edgefront 0★ MIT Py HEAD 3b3771d69949 README SHA 7342f40028e9; singhdevhub-lovepreet/firstlight 0★ NOASSERTION TS HEAD 43378a949bce README SHA 5efe948df249; sliday/jev-chess-algo 0★ MIT TS HEAD 4462ace0895b README SHA 24e42556378c; sunmont/pi-jev-dsk-agi 0★ NOASSERTION TS HEAD 2aa1f06e5da6 README SHA b25ef30d534b; theglitcharchitect/muse-skills 0★ MIT Py HEAD f0cc9cc9cea6 README SHA a14927d3b12f; uibuckets/ai-decision-lab 0★ MIT Py HEAD bd237978608f README SHA bc88b74a1ba6; uibuckets/laya-local-service 0★ MIT Py HEAD 7b340cb7ab25 README SHA fbc8e3ca521a; wuxie888/jev-yaba-wechat 0★ MIT Py HEAD b29bd3c42cec README SHA 0744b3dd6268; AkashPriyadarshii/jev-seo 27★ MIT Rust HEAD f42455ac951a README SHA 677171501c8e; dtduc-git/jevnav 1★ Apache-2.0 Py HEAD b7a12d2f54ce README SHA 61ea35cc8f32; SoundBlaster/SwiftDecision 0★ Apache-2.0 Swift HEAD 7af9416e1ac4 README SHA 54ad5d8e4886; Tongyun1/Jev-in-the-Loop 0★ MIT Py HEAD 039c2117f4e3 README SHA ffe54ee54576; hf:aimeigaoshou/agent-jev 0 likes sha 024a68eade83 apache-2.0; hf:clduab11/jev-calibration-statistics 0 likes sha 9bbe055ee875 mit

Hourly 1256 uniqueness lock: AboveColin/jevclient 2★ MIT Py HEAD a225eadd6eb0 README SHA 5e102cbaa555; typed client is not a replica; wire-compat ≠ logit-equiv; revsmoke/promptrejectormcp 2★ ISC TS HEAD 752217d26fe9 README SHA dab9c144b5f2; screen is a sensor; application must act; soft judgment is not a sole veto; GodModeAI2025/JevCoreML 0★ Apache-2.0 Swift HEAD cb5c261a1412 README SHA f61f018eee8f; CoreML serving substrate ≠ calibrated replica; kev ≠ TypeSafe; Neoo-Blue/vibecheck 0★ Kotlin HEAD cfd6c46899f8 README SHA 718ab09e0442; Jev never writes the reply; RavenValentin/TypeSafe.Jev 0★ MIT C# HEAD 5868475507e5 README SHA 6a4cf10feb67; unofficial .NET client; pin jev-1.13.0; adorosario/jev-rag-claim-verification 0★ MIT Py HEAD 2bdb4d9f3935 README SHA 9b6547d48a39; Jev 1.13.0 balanced acc 73.3 CI [68.5, 77.9] false-verification 23.2% *theirs*; Astra task-optimised 73.8 *theirs*; difference -0.6 points; 187× *theirs* not Harbor; bytelabs-oss/clash-jev 1★ MIT Py HEAD 04d420669966 README SHA 31f93aa3c8d7; no trained policy; fallback never logged as Jev; game success ≠ calibrated Noul; krisitown/jev-router HEAD e2809e09f497 README SHA fa27068d3876; routing ≠ permission; allebee/jevgrep revisit 0★ MIT Py HEAD 5cebf4c046ac README SHA e30654352e5f; first card revisit tag no prior notes card; default threshold 0.5 still soft; meaning-grep is not a gate; allebee/jevgrep ≠ Bentlybro/jevgrep ≠ nassim-arifette/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; harlanljones/jev-roster-shapes densify HEAD 1d94f9e07fe8 README SHA 4653c58a6459; missing data stays missing; geometry never creates value; 8.8 ms is UI latency not a Jev bench; densify §134 not a sibling first sighting; ktaletsk/jevframe densify HEAD 16bd3eae69b7 README SHA 6e0a9ef1ba79; no result thresholded or silently renormalized; densify §48 not a sibling first sighting; hfnissum-byte/Hunkpick 77% *theirs* not Harbor; code enumerates model picks code gates; breejesh/gen1 schema-valid is not the same as correct; 100% schema is not calibrated Noul; hf:Cruzex/laya-typed-decisions-smoketest smoke accuracy 0.460 *theirs* not Harbor; reference 0.727 is not comparable; hf:abidlabs/jev-typed-decisions-causal-0.6b quick_eval acc 0.6234 NLL 1.2755 n=640 *theirs*; unre-run report 0.7518 ECE 0.0154 was not re-run; hf:s1lv3rj1nx/openjev-general-lora Banking77 0.728 vs TypeSafe Jev 0.820 *theirs*; hf:libingzheren/Jev-Mem 0.777 LLM-as-a-Judge *theirs* not Harbor; LLM-as-a-Judge ≠ gold; not the §134 11.0% figure; smartaces/jev-plays-streetfighter-2 6★ text state not video; catalog ≠ endorsement; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56/#57/#58/#59/#60/#61/#62/#63/#64/#65/#66/#67/#68/#69/#70/#71/#72/#73/#74; notes.md §150
