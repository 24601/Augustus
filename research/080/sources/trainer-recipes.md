# Trainer recipes for your own classifier or decision head

Lane: 0.8.0 trainer skill (confidential, local only). Prepared 2026-09-23.
Retrieval window: 2026-09-23T17:02Z to 17:13Z, plus reuse of today's patrol
packets and the archive (`research/notes.md` §18–§165). Nothing third-party
was installed or run, and no weights were downloaded. Every third-party number
below is **Reported** (the source's own measurement). The only local work was
arithmetic on reported counts (`research/080/tmp/trainer/calc/calc.py`). No
recipe here is **Reproduced**. Evidence labels follow `research/protocol.md`:
Contract, Reported, Reproduced, Hypothesis, Unknown.

This is research evidence for a skill that does not exist yet. It is not
runtime guidance and it is not legal advice.

---

## 1. Bottom line

1. **TypeSafe contractually bars training on Jev.** The Master Customer
   Agreement §2.3(b) forbids using "the Services or any Output ... to perform
   model distillation, train a model to imitate the output of the Services, or
   develop (or to facilitate the development of) a similar or competing product
   or service" (quoted in full in §2). The clause was also in the Aug 27, 2026
   version. So the trainer skill must never use Jev outputs as labels, soft
   targets, features, filters, or active-learning signals.
   **This conflicts with current doctrine.**
   `optimizer-integration.md:262-263` says training "may use provider or
   teacher distributions as features, weak labels, or distillation targets."
   For Jev, that route is closed by contract.
2. **Generalist fine-tunes do not transfer; workload-local training can.**
   Three independent projects each report this (all Reported):
   - reflex rejected every adapter it trained, including a 27B-teacher distill.
     Each won on data shaped like its training mix and lost general judgement.
   - Hopper's adapter scored 37/56 on the untouched half of the public hard
     items. The frozen base scored 36/56.
   - Open-Jev-27B reports 96% on its own "OOD" split. Its 9B sibling scores
     0.299 on JevBench v1.4's sealed set, where chance is 0.293.

   Training on the workload's own labels is where gains appear:
   - reflex lora-mix: 62.7% → 76.8% in-distribution.
   - Kev `--init_from`, one user's test on 836 support-tool decisions: 0.88 on
     the new domain, and 0.83 kept on Kev's own evaluation set (the released
     model scores 0.84 there). The same data trained from the base fell to
     0.33 on Kev's set.
3. **Leaderboard rank cannot pick a recipe.** On the 308 sealed JevBench v1.4
   items (chance 0.293), every one-pass system sits between 0.22 and 0.37.
   The Wilson 95% intervals of ranks 1–5 overlap (§4, local arithmetic).
   Systems that generate or think before answering score 0.60–0.95. Two
   consequences:
   - Rank is set by the composite formula (speed, cost, calibration), not by
     separable accuracy.
   - "Don't train; route hard multi-step items to a reasoning model or a
     person" is a real, first-class exit.
4. **Default ladder, cheapest adequate first** (details in §6):
   - R0: don't train.
   - R1: frozen open-model readout plus a per-workload temperature.
   - R2: linear or logistic head on frozen features (embeddings or mid-layer
     hidden states).
   - R3: small encoder fine-tune. DeBERTa-v3-large is the best-supported
     choice; ModernBERT-base is the cheap choice. SetFit or GLiClass fit when
     labels are few.
   - R4: LoRA plus a head on a small open decision model, warm-started, with
     workload labels.

   Stay at the lowest rung that passes a prespecified incumbent-challenger
   gate on untouched workload data. R0 through R2, and SetFit, are plausibly
   MacBook-Air feasible (Hypothesis, see §5). R3 and above realistically need
   CUDA rental for anything past small encoders.
5. **Minimum reproduction** (§7). Use two tasks we control:
   - a code-labelled synthetic policy task with minimal pairs and
     missing-evidence twins;
   - one human-labelled public set.

   Run R0/R1/R2 (and SetFit) on the Mac first, with group-disjoint splits,
   about 470 paired confirmation items per task, and Kev's non-inferiority
   acceptance rule. Run R3/R4 only if R1/R2 fail the gate, and only with GPU
   spend authorized.

---

## 2. TypeSafe terms on training with API outputs

**Documents located.** docs.typesafe.ai links its legal index at
`https://docs.typesafe.ai/legal.md` (HTTP 200, 2026-09-23T17:02:54Z, sha256
`4141ec2e…afcf5c`). The index lists the DPA, the Master Customer Agreement, and
the Privacy Policy. Website Terms of Use are at `https://typesafe.ai/legal/terms`
(`/terms` redirects there). No separate "usage policy" or "acceptable use"
page exists: `/legal/acceptable-use`, `/legal/aup`, and `/legal/usage-policy`
all returned 404.

**The clause (Contract).** Source:
[Master Customer Agreement](https://typesafe.ai/legal/mca), "Last updated
Sep 19, 2026". Retrieved 2026-09-23T17:03:00Z. HTML sha256 of this
retrieval: `b07b91d9…4edbc0`. Local copy:
`research/080/tmp/trainer/legal/typesafe.ai_legal_mca`.

> 2.3. License Restrictions. Customer will not do (and will not attempt to do),
> and will not allow Customer Applications, or any of Customer's directors,
> officers, employees, agents or contractors to do, any of the following: …
> (b) use the Services or any Output (defined below) to perform model
> distillation, train a model to imitate the output of the Services, or develop
> (or to facilitate the development of) a similar or competing product or
> service; (c) reverse engineer, decompile, disassemble, or attempt to access or
> derive the source code or underlying data with respect to the Services,
> including the underlying ideas, algorithms, structure, or organization with
> respect to any of the foregoing; …

**Related terms in the same document (Contract):**

- **Scope.** §1 defines the Services as the console plus the API.
- **Acceptance.** The agreement binds anyone who accepts it, including by
  "USING (OR MAKING ANY PAYMENT FOR) ANY SERVICES".
- **"Output"** is defined in §4.1 as outputs "generated … from the Services that
  are delivered to Customer".
- **Ownership.** §4.2 assigns Output ownership to the Customer. Owning the
  Output does not lift the §2.3 use restriction.
- **Survival.** §2.3 survives termination (§10.4).
- **Suspension and indemnity.** Breach of §2.3 allows immediate suspension (§6)
  and is an Excluded Claim with indemnity exposure (§§12–13).
- **Inbound promise.** §4.1 says TypeSafe will not "include Customer Data in a
  dataset used to train … any artificial intelligence or machine learning
  models without Customer's prior consent". The Privacy Policy (last updated
  Nov 19, 2025) repeats this: "We will not train or fine tune any artificial
  intelligence or machine learning models on your prompts or other Input."
  This promise covers TypeSafe's use of our data, not our use of theirs.

**History (Contract, via Wayback).**
- Capture `20260916215503` ("Last updated Aug 27, 2026", decompressed sha256
  `77d65b57…c6983b`) already contains the same (b) clause.
- That version also contained "(f) publish benchmarks or performance
  information about the Services". The clause is absent from capture
  `20260921155004` ("Sep 19, 2026") and from today's page.
- So between Aug 27 and Sep 19 even publishing a Jev comparison was barred.
  The current version drops that bar.
- A Wayback digest is not a capture of every intermediate version.

**Website Terms of Use (Contract, relevant to the autoscience lane).** Source:
<https://typesafe.ai/legal/terms>, "Last updated Sep 19, 2026", sha256
`69efcc6b…0ddfd09c`. "Site" includes "subdomains of that website", which
covers docs.typesafe.ai. §3(b)(vi) forbids using the Site "by automated
electronic processes, 'robots,' 'spiders,' 'scrapers,' … that monitor, copy, or
download data or other content". The license is "solely for your personal use".
The docs publish `llms.txt` ("Use this file to discover all available pages"),
which invites agents, so the two are in tension. How TypeSafe reads this is
**Unknown**. This lane's own curl fetches of the legal pages were automated.
They are disclosed here, and the question is listed in §9.

**Design rules for the trainer skill (Hypothesis until counsel reviews):**

1. **Never train on Jev Output.** Do not use it as hard labels, soft targets,
   distillation targets, features, pseudo-labels, agreement filters ("keep a
   synthetic item only if Jev agrees"), or active-learning selection scores.
   That covers the `jev-triage` pattern cited at `optimizer-integration.md:264`
   when the downstream artifact is a model trained to do Jev's job.
2. **Treat Jev comparisons as a maintainer decision.** Running Jev as a held-out
   comparator is not explicitly barred by the current MCA. But "facilitate the
   development of a similar or competing product" is broad. Keep any Jev
   comparison outputs physically separate from training stores, and never feed
   them back.
3. **Choose teachers whose terms are known.** Preferred sources, in order:
   observed outcomes, human adjudication, labels computed in code from checked
   facts, or a locally run open-weight teacher under a permissive license. For
   example, JevK5 used Qwen3.6-27B, which is Apache-2.0 per the JevK5 README.
   Other hosted providers' output terms were **not checked** here (Unknown).
4. **Screen third-party corpora for Jev outputs.**
   `SargeDev/jev-distill-corpus` states it holds Jev-scored rows ("distilled
   from the Jev typed-judgment API", Jev reached via OpenRouter). The tasksource
   ModernBERT-JEV recipe uses "30% Jev-native" data with unverified provenance.
   Its `tasksource/train_jev` repository returned 404. Whether our reuse of
   outputs someone else generated is bound by their MCA is **Unknown**.
   Default: exclude, and record in the data card.
5. **Record the access channel.** Jev reached through OpenRouter or Vercel AI
   Gateway (Kev's `kev.jev`) may carry intermediary terms. Unknown.

**Archived community projects that trained on Jev outputs are not recipes to
copy.** Examples: openjev-lm (§25: "2,591 rows of Jev's own API answers") and
jev-gate-student-b (SargeDev). Whether they were contract-compliant is outside
this lane.

---

## 3. Mechanisms that decide recipe choice

All claims are cross-source patterns from Reported evidence, not Reproduced
here. Each entry states the design implication.

- **M1. Fix the readout before you train.** Letter or option logits carry a
  position bias and a label prior. Evidence:
  - [PriDe](https://arxiv.org/abs/2309.03882) attributes MCQ "selection bias"
    to token priors on option IDs.
  - [Contextual calibration](https://arxiv.org/abs/2102.09690) divides out a
    content-free prior.
  - AnyJev L0 (cyclic averaging plus prior removal) moved Qwen3-8B BANKING77-20
    order flips from 0.230 to 0.073 and coverage at ≤5% error from 7.7% to 46.3%
    with zero labels.
  - reflex ships two-order averaging and no temperature.
  - The TypeLLM fair-die study (patrol ECO-2): averaging removes position bias
    but not a label-identity prior.

  Implication: R1 needs a label-prior check, not just order averaging.
- **M2. Temperature is rank-preserving and workload-local.**
  - Kev's `calibrate.py` docstring: Kev-9B on WANLI-256 is "served at mean
    confidence 0.82 against accuracy 0.70". It reports raw, shipped,
    in-sample, and group-disjoint out-of-fold arms.
  - JevK5's temperature fitted on the hard tier left the standard tier
    under-confident (ECE 0.141).
  - Hopper replaced a 7-coefficient map with 3 temperatures because the rich
    map "did not transfer".
  - JevK5 rejected per-type temperatures. Hopper adopted them.

  Implication: fit per workload, out of fold, and record calibrator identity.
  This agrees with installed `validation.md`.
- **M3. Generalist fine-tunes overfit their mixture.**
  - reflex: "Fine-tuning, in every form we tried … won on data shaped like
    their training data and lost general judgement on long, ambiguous inputs."
  - Hopper: dev half hard 0.709; reserve half 0.661, level with the frozen base.
  - kotoba typed-decisions: ModernBERT-base scores 0.728 in-domain but 0.485 on
    OOD questions, "memorising the slot".
  - Kev: fine-tuning dropped the base's date arithmetic from 0.82 to 0.72.
  - Open-Jev: internal OOD 96% against sealed JevBench near chance.
- **M4. Workload-local labels are where training pays.**
  - reflex lora-mix on Qwen3.5-4B: 62.7%/ECE 0.120 → 76.8%/0.051 → 0.024 with
    temperature, in-distribution.
  - Kev warm start: `--init_from` reached 0.88 on the new domain and kept 0.83
    on Kev's own set. Training from the base fell to 0.33 on Kev's set (one
    user's test).
  - AnyJev L2 (closed-form head on a hidden state at about ⅔ depth):
    100 labels → 0.740, 300 → 0.772 on Qwen3-8B.

  Implication: train per workload, warm-start, and keep the frozen readout as
  the incumbent.
- **M5. Missing evidence must be designed, not hoped for.**
  - Decision-1.0 DIAGNOSTICS, 110 unknowable items, share of answers with
    P≥0.9 (lower is better):

    | Model | P≥0.9 share |
    | --- | --- |
    | Lux-9B | 20.91% |
    | Sol-2B | 24.55% |
    | Jev | 16.36% |
    | Kev-9B, Kev-4B, Kev-0.8B | 0.00% |

  - Kev trained "cases whose deciding evidence was removed, trained toward a
    uniform answer".
  - Nimble deliberately did not train ablated examples with labels ("missing
    evidence does not mean that the answer is false").

  Two defensible designs, uniform target versus exclusion plus abstention. The
  reproduction should test both.
- **M6. Shortcuts through the answer hatch and through surface form.**
  - Kev: when none-of-the-above appeared only as the correct answer, the model
    learned the wording. Fix: add it as a wrong alternative too.
  - mobarmg randomized option IDs.
  - kotoba: paraphrase, negation, and order augmentation plus a consistency
    loss gave OOD +2.6 pt and negated noul +16 pt.

  Minimal pairs ([counterfactual augmentation](https://arxiv.org/abs/1909.12434);
  Nimble's ≤8-word focus-fact edits) target the same failure.
- **M7. Low ECE is not discrimination.** tasksource ModernBERT-JEV reports
  zero-shot AG News accuracy of 24.07% at K=4 (chance 25%). It reports Banking77
  accuracy of 2.05% at K=77 (chance 1.30%) with ECE 0.0019. A near-uniform
  predictor is well calibrated and useless. Implication: always report accuracy
  or proper scores and coverage at an error budget beside ECE.
- **M8. Teacher labels propagate non-random errors.**
  [LLM annotations → BERT](https://arxiv.org/abs/2504.15432) (2025) reports
  lower accuracy, run-to-run instability, and failures on minority classes.
  Mitigations seen in sources:
  - JevK5 keeps a teacher item only when two independent answers match the
    intended one.
  - Hopper keeps "only where independent LLM solvers agreed".
  - Winnow adds teacher-distribution cross-entropy "only when the teacher
    agreed with the gold label".
  - Nimble and Hopper families compute labels in code from checked facts.

  The best-supported synthetic pattern is: the LLM writes facts and text, code
  computes the label, and the ablation checks prove the evidence is necessary.
- **M9. One-pass ceiling.**
  - Sealed JevBench v1.4: one-pass systems 0.22–0.37. djev-thinking 0.601,
    GPT-6 Luna 0.955, DeepSeek-V4.1-Flash 0.948.
  - TypeLLM: 195/231 without thinking, 228/231 with thinking on public items.
  - Hopper and reflex both list dates, multi-step arithmetic, and multi-hop long
    documents as weak.

  Implication: exact preprocessing (Kev `KEV_DATE_FACTS`: deadline 0.80 → 0.90)
  or a reasoning exit, not more head training.
- **M10. Selection noise and dev-set reuse.**
  - Kev autoresearch: "A one-seed point-estimate lead on ~650 questions is
    mostly noise". The champion changes only if the paired-bootstrap delta is
    positive and the 95% lower bound is ≥ −1 pp.
  - Hopper used its dev half for 26 configurations plus more than 20
    calibration maps, and disclosed it.
  - JevK5's calibration set echoed public items (8-gram scan), and the
    correction was published.
  - JevBench flags operators whose APIs received sealed text.

  Implication: this is the acceptance machinery the skill should reuse.

---

## 4. Leaderboard context (JevBench v1.4, Reported)

Source: `fstandhartinger/jevbench` @ `2fa63fa3`,
`results/v1.4/jevbench-v1.4-results.json` (generated 2026-09-23T10:02:48Z).
Sealed set n = 308, chance 0.293. The Wilson intervals are local arithmetic on
counts reconstructed from the reported accuracies.

| System | Public 231 | Sealed | Sealed 95% Wilson | v1.4 rank |
| --- | ---: | ---: | --- | ---: |
| Jev 1.13.0 (API flag) | 0.866 | 0.367 | 0.315–0.422 | 1 |
| JevK5 v0.2 (Qwen3.5-4B LoRA) | 0.853 | 0.331 | 0.281–0.386 | 2 |
| Hopper (Qwen3.5-4B LoRA) | 0.823 | 0.341 | 0.290–0.396 | 3 |
| Winnow-12B Q8 (Gemma-4-12B LoRA) | 0.857 | 0.331 | 0.281–0.386 | 4 |
| reflex 4B | 0.792 | 0.282 | 0.235–0.335 | 5 |
| SemIf (frozen Qwen3.5-4B) | 0.810 | 0.263 | — | 8 |
| Kev-4B (Qwen3 generation) | 0.662 | 0.224 | 0.181–0.274 | 22 |
| Laya (ModernBERT-large, 421M) | 0.584 | 0.308 | 0.259–0.362 | 32 |
| open-jev-deberta-v3-large | 0.524 | 0.295 | 0.247–0.349 | 56 |
| djev-thinking (generative) | 0.874 | 0.601 | 0.545–0.654 | 52 |
| GPT-6 Luna (API flag) | 0.996 | 0.955 | 0.925–0.973 | 27 |

The benchmark's own caveat: "The sealed set is unusually difficult for one-pass
decision models. Small differences in sealed accuracy should not be read as
proven pairwise superiority." The listed Kev row is the Qwen3-generation
`kev-4b`, not the current Qwen3.5 family. JevK5's reported McNemar p = 0.013
(21 fixed, 7 broken) matches the exact binomial p computed locally (0.0125).

---

## 5. Recipe cards

**Card fields.** Each card has the same fields:

- **Backbone:** base model and size.
- **Head:** head type.
- **Output:** probability of what, and calibrated how.
- **Data:** labels, teacher, or synthetic.
- **Compute:** training compute, with MacBook Air feasibility.
- **Serve:** serving cost and latency.
- **License:** code, weights, and data.
- **Evidence:** what evaluation exists.
- **Failure modes:** known weak spots.
- **Disposition:** what to do with the recipe.

"Mac" means a MacBook-Air-class Apple Silicon laptop, which is fanless.
Its RAM is unknown (§9), so Mac feasibility is **Hypothesis** unless a source
measured it on Apple hardware.

### 5a. Jev-class open decision heads and ports

**A1. Kev** — `github:jaredpalmer/kev` @ `557598fc` (node `R_kgDOUfXmpg`); prior cards §45 and §123–§141.
- **Backbone:** Qwen3.5-0.8B, 4B, or 9B base.
- **Head:** rank-16 LoRA plus a pointer head that scores each option's `</opt>`
  state against `<decide>`, then applies a softmax. Questions are isolated;
  on Qwen3.5, each question is run as its own row.
- **Output:** a distribution over the supplied options. One shipped temperature
  per checkpoint (about 2.1–2.4), fitted in-distribution. Choice confidence is
  `(p_max−1/K)/(1−1/K)`, which is "not a measured accuracy rate".
- **Data:** `decision-v7`: 10,000 examples from ten public datasets, 896
  generated policy examples, and 1,680 generated rule-structure examples. A
  second pass trained on day-count and removed-evidence cases (uniform target).
  "No Jev outputs were used for training."
- **Compute:** 0.8B takes about 20 minutes on one H100. The Mac path "works but
  is slow for Qwen3.5 bases". The earlier Kev-0.5B (Qwen2.5) trained in about
  1h45m on an Apple M5 (§45). Serving on Mac goes through MLX: Kev-0.8B 149 ms
  new state, 28 ms cached.
- **Serve:** a five-question request takes tens of ms on H100/MI300X.
- **License:** Apache-2.0 code and adapters. Qwen bases are Apache-2.0.
  Datasets carry their own licenses.
- **Evidence:** new-source test 0.852 for 9B, 0.837 for 4B, 0.684 for 0.8B.
  Jev scores 0.857 on the new-source dev set, which "isn't a controlled
  comparison". Frozen suites and a claims ledger (`docs/claims.json`) are
  published.
- **Failure modes:**
  - Option order can change the answer.
  - Training covered at most 384 state tokens.
  - Temperature does not transfer across workloads.
  - Date arithmetic regressed after fine-tuning.
  - The v1.4 sealed score of 0.224 is for the Qwen3 generation.
- **Disposition:** **borrow** the autoresearch champion rule, `calibrate.py`'s
  out-of-fold report, the claims ledger, the NOTA-as-distractor data rule, and
  `--init_from` warm start. **Pilot** the fine-tune path at rung R4. The bundled
  `kev-finetune` skill offers any-LLM data generation through OpenAI-compatible
  endpoints. The Jev-output bar in §2 applies to whatever teacher a user picks.

**A2. Decision-1.0 Lux / Nox / Sol** — `hf:llm-semantic-router/Decision-1.0-Lux-9B` @ `bd45a30a`, Nox-4B @ `0bb83350`, Sol-2B @ `0665a411`; first card in today's patrol.
- **Backbone:** Qwen3.5-9B, 4B, or 2B.
- **Head:** a shared bilinear/MLP candidate head (4.2M parameters, FP32) reads
  candidate-endpoint vectors and the final query vector. The backbone is fully
  fine-tuned.
- **Output:** a per-candidate distribution with a single temperature fitted on
  1,814 independent calibration examples.
- **Data:** 24,000 examples: programmatically verified tasks; human labels from
  MultiNLI, BANKING77, and CLINC150; 8,000 human-annotated Cosmos QA, SQuAD 2.0,
  and SNLI examples. "Official Jev outputs are not used as training labels."
  Splits are group-disjoint and near-duplicate aware.
- **Compute:** full-parameter training; hardware not stated. Serving is validated
  only on AMD gfx942. "CPU and MPS inference are unsupported". **Not Mac.**
- **License:** Apache-2.0. Dataset licenses are listed per source, including
  CC BY-SA.
- **Evidence:** weighted accuracy 77.40 (Lux), 73.09 (Nox), and 66.32 (Sol),
  against Jev 81.05. The 30/25/15/15/15 weights were "chosen after observing
  results" (patrol).
- **Failure modes:** missing-evidence P≥0.9 is 20.9% for Lux and 24.6% for Sol.
  Option-order flips are 8.3% for Lux and 38.9% for Sol.
- **Disposition:** **watch.** The attribution and group-split discipline is a
  good model for data cards. The recipe itself is not a laptop recipe.

**A3. Open-Jev-27B-v1.1** — `hf:ZefanCai/Open-Jev-27B-v1.1` @ `28cf7306`; code `github:Zefan-Cai/Open-Jev`; prior cards §125 and §165.
- **Backbone:** Qwen3.8-27B at revision `1d4bf0f2`.
- **Head:** rank-8 LoRA plus a scalar per-candidate head (15.47M trained
  parameters).
- **Output:** a distribution over candidates with a saved temperature of 2.534,
  fitted on 512 calibration rows.
- **Data:** this stage used 82,045 WANLI rows, 30,720 new synthetic community
  rows, and 35,874 replay rows. It warm-started from an earlier checkpoint.
  The public dataset is a projection, not the training set.
- **Compute:** multi-GPU (four-rank FSDP2). **Not Mac.**
- **License:** Apache-2.0 adapter; MIT code. Data licenses depend on the source.
- **Evidence:**
  - Internal Test and OOD accuracy is 96–98% on its own mixture.
  - Public JevBench 197/231, against Jev's 200/231.
  - The 2B and 9B siblings score 0.263 and 0.299 on the v1.4 sealed set.
- **Failure modes:** its own "OOD" is synthetic and in-family. A lexical overlap
  screen "does not prove semantic independence".
- **Disposition:** **reject as a default.** Keep it as the clearest evidence
  that in-family OOD splits overstate generalization.

**A4. Bespoke Nimble** — `github:bespokelabsai/nimble` @ `38edc3b5` (node `R_kgDOUf54AA`); prior card §35 and today's patrol.
- **Backbone:** Qwen3.5-9B with a rank-16 LoRA (lr 5e-5, effective batch 8,
  one epoch, BF16, 2,048-token limit).
- **Head:** cross-entropy over the allowed candidate logits (one token per
  candidate).
- **Output:** a softmax over supplied candidates. The default temperature is
  2.179 for that exact revision. v2 inherits it as a "transferred release
  default".
- **Data:** 2,676 synthetic contrastive examples. Labels are computed in code
  from facts checked by separate model calls, and "no person has reviewed them".
- **Compute:** tuning ran on L40S; the final fit ran on H100. Mac is
  inference-only (MLX `ParallelScorer`, 444 ms median on an M5 Pro).
- **License:** Apache-2.0 on the model card. GitHub LICENSE returns 404, and
  the API license is null.
- **Evidence:** 292/324 synthetic holdout matches, against Jev 302 and the base
  215. The authors call the test "narrow".
- **Failure modes:** "don't expect a lot of generalization". v1.4 sealed 0.289.
  "Saved Jev probabilities are available for future soft-target distillation";
  under §2 that would be a Jev-output use.
- **Disposition:** **borrow the curation recipe**: rule check, a pair differing
  in ≤8 words, ablation checks that each sentence is required, code-computed
  labels, and pairs kept within one split. **Reject** the soft-Jev-target
  extension.

**A5. JevK5** — `github:allebee/jevk5` @ `70855658`; `hf:alibiserikbay/JevK5` @ `3c673298`; first card in §165.
- **Backbone:** Qwen3.5-4B with a merged rank-16 LoRA on attention projections.
- **Head:** SemIf's letter-logit readout.
- **Output:** a softmax over answer letters with one temperature (1.532), fitted
  on teacher questions from three unseen domains.
- **Data:** 3,272 teacher questions written by Qwen3.6-27B with thinking. A
  question is kept only if two independent answers match the intended one.
  Another 3,272 human-labelled items come from MMLU-Pro, WANLI, MultiNLI, BoolQ,
  banking77, ARC, and CommonsenseQA. Two epochs, lr 3e-5.
- **Compute:** CUDA. Inference takes about 9 GB bf16. **Not Mac** as published.
- **Serve:** 13.5 ms p50 on H100 with CUDA graphs.
- **License:** Apache-2.0.
- **Evidence:** public hard tier: untrained 0.613 → v0.1 0.676 → v0.2 0.739.
  v1.4 rank 2 (sealed 0.331).
- **Failure modes:** two standard-tier items regressed. Standard-tier ECE is
  0.141 because the temperature was fitted on hard items. A calibration-set
  echo of public items was found and corrected.
- **Disposition:** **borrow** the double-agreement teacher filter, the
  local permissive teacher, and the published rejected-variant list. **Watch**
  the recipe.

**A6. Hopper** — `hf:HopitAI/hopper` @ `281d393f`; code `github:hopit-ai/hopper` (not inspected); first sighting.
- **Backbone:** Qwen3.5-4B at `851bf6e8` with a rank-16 LoRA.
- **Head:** a letter-logit softmax.
- **Output:** a distribution with per-answer-type temperatures (choice 0.790,
  noul 0.753, score 0.900), fitted on its own held-out items.
- **Data:** three sources: LLM-generated families with code-computed labels;
  a JevBench-style LLM-generated set kept only where independent solvers agree,
  screened by 8-gram and question identity against every public item; and
  training splits of 11 human-labelled datasets.
- **Compute:** CUDA. **Not Mac** as published.
- **License:** Apache-2.0. Dataset licenses include CC BY-SA.
- **Evidence:** dev half hard 0.709; reserve half 37/56, level with the frozen
  base at 36/56. v1.4 sealed 0.341.
- **Failure modes:** dates and multi-step arithmetic; multi-hop long documents;
  English only.
- **Disposition:** **borrow** the disclosure pattern (dev/reserve split,
  pre-registered single read) and the shared-8-gram screen.

**A7. Winnow-12B** — `hf:EldanRing/Winnow-12B` @ `b6ac22b0`; first sighting.
- **Backbone:** `google/gemma-4-12B-it` with a rank-32 LoRA on all projections,
  merged and exported as BF16 and Q8_0 GGUF.
- **Output:** a softmax over options at temperature 1.0 with no fitted map.
  Confidence is entropy-based, "not a guaranteed probability of correctness".
- **Data:** private. 16k initial plus 26k refinement presentations. The loss is
  gold-label cross-entropy plus teacher-distribution cross-entropy, used only
  where the teacher agrees with gold. The teacher's identity is not stated
  (Unknown).
- **Compute:** CUDA training. A llama.cpp GGUF serves on an RTX 4090; Mac
  llama.cpp serving is plausible (Hypothesis).
- **License:** Apache-2.0, under Gemma 4 terms.
- **Evidence:** v1.4 sealed 0.331. The author's contamination scan cannot be
  reproduced because the rows are private.
- **Disposition:** **watch.** Borrow the "teacher CE only when teacher = gold"
  rule.

**A8. reflex** — `github:kshetrajna12/reflex` @ `231f896d` (node `R_kgDOUfc0Dg`); prior card §121.
- **Backbone:** frozen Qwen3.5-4B by default.
- **Head:** a lettered readout averaged over two option orders.
- **Output:** `stable` ships no calibration file. A workload temperature is
  optional, and the README says to refit when the model, prompt, or precision
  changes.
- **Data:** none for `stable`. The optional LoRA fine-tune (`reflex-calibrate
  train`, proper-scoring loss, hard or soft labels) uses mixes built from eight
  public datasets.
- **Compute:** a 16 GB CUDA GPU. The README says the server "also runs on the
  Mac GPU through PyTorch MPS", so **Mac-feasible for R1** (Contract, README;
  not measured here).
- **License:** MIT code and adapter; Apache-2.0 base.
- **Evidence:** public hard 0.685 for 4B and 0.766 for 27B, against Jev 0.730
  (self-run). lora-mix in-distribution: 62.7% → 76.8%. v1.4 sealed 0.282.
- **Failure modes:** "Every adapter trained in this repo was rejected". The
  `reflex-distill` route uses teacher distributions as targets.
- **Disposition:** **adopt as the R1 reference pattern.** The frozen model with
  two orders and a per-workload temperature is the incumbent any training must
  beat. Keep its negative results as falsifier evidence.

**A9. SemIf (formerly OpenJev)** — `github:TheoLeeCJ/SemIf` @ `1f2dea3e`. The API now reports `full_name` TheoLeeCJ/SemIf-OpenJev, same node `R_kgDOUc5tow`. Prior cards §117 and §165.
- **Backbone:** frozen Qwen3.5-4B BF16 (also MiniCPM5-2B, Qwen3-0.6B, and a
  Qwen3.8-27B EXL3 bridge).
- **Head:** none. Native option logits are read in one pass.
- **Output:** probabilities "conditional on the supplied options". Optional
  per-workload temperature with out-of-fold evidence: WANLI ECE 0.208 → 0.069;
  authored decisions 0.068 → 0.038.
- **Data:** none, or labels for temperature only.
- **Compute:** **Mac-feasible** through MLX, PyTorch MPS, and a llama.cpp CPU
  backend (Contract, per the README).
- **License:** MIT code. Weights keep their own licenses.
- **Evidence:** 144 authored decisions, balanced accuracy 0.813 (4B) and 0.958
  (27B). TypeSafe-subset agreement 0.845, against Jev's published 0.883.
- **Failure modes:** BF16 reuse paths changed 5–6 of 777 argmaxes. v1.4 sealed
  0.263.
- **Disposition:** **adopt as an R1 implementation option.** Its MLX path is the
  most direct Mac route.

**A10. AnyJev levels** — `github:nokia-applied-research/AnyJev` @ `73fa8c66` (HEAD moved from `3cd8c6fc`, the §165 look, earlier today); prior cards §151 and §165.
- **Levels:**
  - `raw`: restricted softmax over label tokens.
  - `L0`: cyclic averaging plus label-prior division, zero labels.
  - `L1`: temperature on L0, 100–500 labels.
  - `L2`: closed-form shrunk LDA or ridge head on the hidden state at about ⅔
    depth, 100–300 labels per question. The head is about 100 KB, solves in
    2–8 s on CPU, and label-free recentering follows rewordings.
- **Output:** `decision.level` is part of score identity. L0 "does not make
  uncertainty calibrated".
- **Compute:** the transformers backend. Feature extraction needs a local model
  forward (MPS plausible, Hypothesis); the solve runs on CPU.
- **License:** Apache-2.0.
- **Evidence:**
  - BANKING77-20 on Qwen3-8B, n = 300 (§165).
  - typed-decisions L2 0.730–0.799 across Qwen3 1.7B–32B, pooled ECE 0.03–0.05.
    That gold is teacher-LLM agreement, with self-agreement 0.735 (§165).
  - Reworded questions drop 0.77 → 0.65–0.70; 30 unlabelled requests restore
    0.74–0.75.
- **Failure modes:** heads do not transfer across questions or models. A shift
  in states is invisible to recentering. Maze and Minesweeper rows show no
  readout beating the trivial baseline.
- **Disposition:** **adopt L2 as the R2 reference** (linear probe on frozen
  hidden states). **Borrow** the level-in-output contract.

**A11. dynajev** — `github:strangeloopcanon/dynajev` @ `8afc7ef3` (node `R_kgDOUmfX-A`); first card in today's patrol.
- **What it is:** per-request "compiled" readout heads on a stock model, with
  optional per-class bias or ridge probes kept only if leave-one-out accuracy
  holds. Heads can exit early.
- **Output:** "Probabilities are relative to the allowed answers, not calibrated
  frequencies."
- **Compute:** Qwen3.5-2B on a 4-core CPU: 71 vs 72 of 74 questions against the
  same model writing its answer, 265 ms vs 408 ms. **CPU-feasible**, Reported.
- **Failure modes:** an early-exit head missed 1 of 8 states.
- **Identity note:** the README links "Jev" to `jevtypesafeai.com/docs`, which is
  not the official docs.typesafe.ai.
- **License:** MIT.
- **Disposition:** **borrow** the leave-one-out keep rule for tiny probes and the
  early-exit layer search. It credits contextual calibration and PET as prior
  work.

**A12. TypeLLM** (constrained autoregressive) — `github:TypeLLM/TypeLLM` @ `d592c10c` (node `R_kgDOUev6yQ`, formerly zmtomorrow/TypeAR); prior cards §32 and §113.
- **What it is:** JSON-Schema-typed generation on unchanged weights. Optional
  thinking before the constrained answer. Per-enum permutation averaging.
- **Output:** a token distribution over enum values; not calibrated by
  construction.
- **Evidence:** public JevBench 195/231 without thinking and 228/231 with
  thinking.
- **License:** Apache-2.0.
- **Disposition:** **adopt as the reasoning exit** for items where one-pass
  readouts fail (M9). This is not a trained head.

**A13. jevfire** — `github:kikoncuo/jevfire` @ `5df83b55` (node `R_kgDOUdkiXw`); first card here.
- **Verified: a serving and readout sidecar, not a training recipe.**
  "No retraining. No second model." It scores verified single-token labels with
  the pretrained LM head through vLLM (CUDA). The WebGPU demo uses Qwen3.5-0.8B.
- **Output:** "summing to 100% expresses relative preference … not calibrated".
- **License:** MIT.
- **Disposition:** **archive-only.** Use it as a CUDA serving substrate for R1
  if ever needed.

**A14. GLiClass** — `github:Knowledgator/GLiClass` @ `40baa67c` (node `R_kgDOMD04Zg`); [arXiv 2508.07662v1](https://arxiv.org/abs/2508.07662); models `knowledgator/gliclass-edge-v3.0` (32.7M), `-base-v3.0` (186.5M), and `-instruct-large-v1.0` (438.7M), all Apache-2.0. Prior card §19.
- **What it is:** a GLiNER-style joint encoding of text and all labels in one
  pass. Sigmoid multi-label or softmax scores. Zero-shot, few-shot (examples),
  and fine-tunable (`train.py`).
- **Output:** label affinities with a caller threshold; not calibrated
  probabilities.
- **Compute:** small encoders; CPU and ONNX variants exist. **Mac-feasible for
  inference and plausibly for fine-tuning** (Hypothesis).
- **Evidence:** zero-shot F1 tables on the cards (Reported). JevBench variants
  "openjev-verdict" (GLiClass ModernBERT-base fine-tune) score 0.554–0.576
  public and 0.247–0.279 sealed.
- **Disposition:** **pilot** as an R3 alternative when the label set is large or
  changing, or multi-label. Calibrate before any threshold policy.

**A15. tasksource ModernBERT-JEV** — `hf:tasksource/modernbert-tasksource-jev` @ `790beda6`; first card.
- **Backbone:** ModernBERT-base (149M).
- **Head:** an option-query cross-attention head, permutation-equivariant by
  construction. Its 0% flip rate is structural.
- **Data:** "70% Tasksource / 30% Jev-native" with soft targets. Provenance of
  the Jev-native share is Unknown; the reproduction repository
  `tasksource/train_jev` returned 404.
- **Evidence:** zero-shot AG News 24.07% at K=4 and Banking77 2.05% at K=77,
  near chance. typed-decisions 32.2% macro.
- **License:** Apache-2.0 model. The companion dataset is `license: other`.
- **Disposition:** **reject** as a recipe. **Borrow** only the equivariant head
  idea (a structural fix for position bias) and the M7 lesson.

**A16. open-jev-deberta-v3-large and kotoba typed-decisions** — `hf:com-kotobalabs/open-jev-deberta-v3-large` @ `19bf9a64`; `github:kotoba-lang/typed-decisions` @ `e4ed8076` (license NOASSERTION); prior card §33.
- **Backbone:** DeBERTa-v3-large (435M), fully fine-tuned.
- **Head:** span-pooled option scoring with a softmax per question.
- **Output:** cross-entropy plus Brier, then a post-hoc temperature fitted on a
  validation split.
- **Data:** "Public gold labels only — no synthetic answers, no teacher model"
  (Banking77, SST-5, BoolQ).
- **Compute:** one H100: 229 s and about $0.25 for 18k states, one epoch.
  - ModernBERT-base: $0.16.
  - LLaDA-MoE LoRA: $2.29.
  - M1 Max CPU inference: 1.8 s per 4 questions.
  - The Mac training bench was "not measured" because runs were killed.
- **Evidence:** in-domain 0.854 and OOD questions 0.690 (three seeds:
  0.847 ± 0.005 and 0.678 ± 0.012).
  - ModernBERT-large did not learn under their heads.
  - ModernBERT-base memorized slots (OOD 0.485).
  - Augmentation plus a consistency loss: OOD +2.6 pt.
- **Failure modes:** the 512-token context cuts state to 256 tokens. OOD ECE
  runs about 0.03 over-confident. v1.4 sealed 0.295.
- **License:** Apache-2.0 model; repository NOASSERTION.
- **Disposition:** **adopt DeBERTa-v3-large as the R3 default encoder.** Keep
  ModernBERT-base as the cheap, 8k-context alternative that needs an
  OOD-question test.

**A17. Laya** — `hf:convaiinnovations/laya` (archive §18 and §76; not re-inspected today; GitHub `convaiinnovations/laya` returned 404 in today's patrol; runtime link `NandhaKishorM/laya`).
- **What it is:** ModernBERT-large plus a decision head (421M), RLCD-style
  training.
- **Evidence (older, Reported):** in-task 0.838 accuracy / ECE 0.060 against
  zero-shot 0.651 / 0.207. v1.4 sealed 0.308. In Decision-1.0's
  missing-evidence panel, Laya English has a 0.00% share at P≥0.9 but a
  negative paired confidence drop (−5.58 pp) and 49.09% intact accuracy.
- **Disposition:** **archive-only** for this lane.

**A18. Name-similar and unavailable sources.**
- `jdev/jev-research` returned 404 again at 2026-09-23T17:11:19Z; user `jdev`
  exists with 3 public repos. **Unavailable evidence, not absence.**
- `liuup/jev-research` (node `R_kgDOUgelzw`, HEAD `4a0fcad9`, README only) is a
  different owner and **not joined**. Its content is relevant to the paper lane:
  a Qwen3.5-0.8B head predicts a distribution over outcome events (collision,
  timeout, food) per legal action, and a fixed utility of [−1, 0, +1] chooses
  the action. It trains only on events observed on the executed trajectory.
  That is an exogenous-policy, outcome-trained instrument. Contract-level
  description; no results inspected.

### 5b. Classical and strong baselines

**B1. Logistic regression or linear probe on frozen features.**
- **Sources:**
  - [arXiv 2408.03414v2](https://arxiv.org/abs/2408.03414): penalised LR on
    small-LLM embeddings "equals (and usually betters)" a large LLM on 17 tasks
    in the tens-of-shot regime, using no more labels than validating the large
    LLM needs.
  - [arXiv 2512.22245v1](https://arxiv.org/abs/2512.22245): Brier-loss linear
    probes on judge hidden states, better calibrated at about 10× lower
    compute, but "conservative" on easy data.
  - [arXiv 2606.10487v1](https://arxiv.org/abs/2606.10487) (2026): a mid-layer
    probe recovers most decisions of a guard model.
  - AnyJev L2 (A10).
- **Output:** a calibrated-by-objective probability if trained with log or
  Brier loss. Still verify.
- **Data:** tens to hundreds of labels per question.
- **Compute:** CPU seconds for the solve. Features come from an embedding model
  or a local LLM forward, which needs MPS for ≥1B. **Mac: yes.**
- **License:** depends on the feature model.
- **Failure modes:** a per-question head does not transfer; state shift;
  [probes can detect task format](https://arxiv.org/abs/2606.02907) rather than
  the target (title-level only, not read).
- **Disposition:** **adopt as R2.**

**B2. SetFit** — `github:huggingface/setfit` @ `be332d6d` (latest release v1.2.0, 2026-09-04); [arXiv 2209.11055v1](https://arxiv.org/abs/2209.11055) (2022).
- **What it is:** contrastive Siamese fine-tuning of a sentence transformer,
  then a scikit-learn or differentiable head. Prompt-free; "8 labeled examples
  per class" in its headline example.
- **Mac:** plausible for small bodies (Hypothesis).
- **License:** Apache-2.0.
- **Evidence:** a 2022 paper, older than this cycle.
- **Disposition:** **pilot** as the few-label R3 option. It is not in any
  JevBench row.

**B3. Fine-tuned encoders (DeBERTa-v3, ModernBERT).** See A16. Background:
[ModernBERT, arXiv 2412.13663v2](https://arxiv.org/abs/2412.13663). The
measured evidence here says architecture choice interacts with the head design
(A16). Do not assume "newest encoder wins".

**B4. GLiClass zero-shot or few-shot.** See A14.

**B5. TabPFN (tabular)** — `github:PriorLabs/TabPFN` @ `eeb37a6c`; [TabPFN-3.5 report, arXiv 2609.17895v1](https://arxiv.org/abs/2609.17895) (2026-09-15).
- **What it is:** a pretrained in-context tabular predictor.
- **Limits:** CPU is capped at 5,000 samples for v3 and v3.5 (1,000 for older
  versions). Apple Silicon GPU is supported.
- **License:** code is Apache-2.0. Weights for TabPFN-2.5, 2.6, 3, and 3.5 are
  **non-commercial** and require login to accept. TabPFN-2 weights are Apache-2.0
  plus attribution.
- **Disposition:** **pilot only if the license fits** and after
  logistic-regression and gradient-boosting baselines. Its reported SOTA claims
  are vendor claims.

**B6. Gradient boosting** (LightGBM, XGBoost, CatBoost). No source was fetched
today. It is the standard strong baseline for stable feature tables and is
already the "classical supervised model" row in `judgment-class.md:32`. Mac:
yes. **Adopt as the tabular incumbent**, with no new evidence claimed.

### 5c. LLM fine-tunes: classification head versus constrained generation

**C1. LoRA plus a classification or pointer head on a causal LM.**
- **Sources:**
  - [arXiv 2512.12677v3](https://arxiv.org/abs/2512.12677) (v3 May 2026): the
    final-token-embedding head with 4-bit plus LoRA "matches or exceeds
    fine-tuned BERT baselines on single-label classification while training
    10-30x fewer parameters". Instruction-tuning was competitive only for
    multi-label with ≥100M trainable parameters.
  - [LS-LLaMA, arXiv 2310.01208v1](https://arxiv.org/abs/2310.01208).
  - Kev (pointer head), Open-Jev (scalar head), and Lux (bilinear head).
- **Output:** a softmax over candidates. Calibrate after training.
- **Mac:** small attention-only bases on MPS are plausible. Qwen3.5 DeltaNet
  bases lack PyTorch Apple kernels (Kev README). MLX-LM supports LoRA, DoRA,
  and full fine-tuning with `--mask-prompt` completion loss. Its documented
  example is a 7B model at batch 1 with 4 layers on a 32 GB M1 Max, at about
  250 tokens/s. It has no classification head, so a candidate-restricted loss
  needs custom code (Hypothesis).
- **Disposition:** **pilot at R4** with warm start.

**C2. LoRA on option-letter logits** (next-token cross-entropy restricted to
candidates). Used by JevK5, Hopper, Winnow, Nimble, and reflex. This is the
simplest head: it reuses the LM head. Mechanism risk: it inherits the letter
prior (M1). Same Mac constraints as C1. **Pilot at R4 as an alternative to C1.**
Choose between C1 and C2 by reproduction, not by source preference.

**C3. Constrained generation, optionally with thinking.** TypeLLM (A12) and
[YOFO, arXiv 2511.16600v3](https://arxiv.org/abs/2511.16600), which reads
per-requirement yes/no logits in one forward pass and optionally follows with
chain of thought. Use it as the **reasoning exit**, not a trained head. It costs
more latency and tokens; it does not replace calibration.

---

## 6. Default recipe ladder

**Rule.** Start at the lowest rung whose entry condition holds. A higher rung
is built only after the current incumbent fails a **prespecified** gate on
**untouched, group-split workload data**. A challenger replaces the incumbent
only under Kev's rule: the paired, cluster-bootstrapped delta on the consumer
metric is positive and its 95% lower bound is ≥ −1 pp. That is `kev/autoresearch.py`,
and it is consistent with `optimizer-integration.md` steps 4–5. Every rung
records model, revision, readout level, calibrator, and data-card versions.
No rung may use Jev Output (§2).

| Rung | What | Labels needed | Mac? | Enter when | Leave when |
| --- | --- | --- | --- | --- | --- |
| **R0 Don't train** | Exact rule, lookup, parser, existing classifier; or route to a reasoning model (C3) or a human | 0 (validation only) | yes | An exact rule exists; volume is too low to repay validation; items need multi-step arithmetic or long multi-hop reading (M9); or the label budget is below what validating any model needs | A measured gap remains after exact preprocessing |
| **R1 Frozen readout** | 2–4B open model, restricted option softmax; label-prior check, then two-order or cyclic averaging only if flips follow position; per-workload temperature fitted out of fold (reflex, SemIf, AnyJev L0/L1) | 100–500 (temperature) | yes (MLX, MPS, llama.cpp) | Default first model | Coverage at the error budget, or policy loss, misses the target |
| **R2 Linear head** | LR/ridge/LDA on frozen features: a sentence embedding, or the R1 model's mid-layer state (AnyJev L2); Brier or log loss; per question | 30–300 per question | yes | R1 fails; labels exist | Must beat R1 by the gate |
| **R3 Small encoder** | DeBERTa-v3-large full fine-tune (CE + Brier, then temperature); ModernBERT-base for cost or 8k context; SetFit for 8–64 per class; GLiClass for large or changing or multi-label sets | ~1k–20k (SetFit: tens) | small ones plausibly; large ones CUDA | High volume, stable label set, latency-critical, R2 short | Fails the OOD-question test or the gate |
| **R4 LoRA + head** | Warm-start an open decision model (Kev `--init_from`), or letter-logit LoRA (C2), on workload labels; minimal pairs, NOTA-as-distractor, missing-evidence twins | hundreds to thousands | slow or no; CUDA rental | R3 short, and the task needs LLM knowledge or long context | Loses to R1/R2 on untouched data, or regresses slices |
| R5 Generalist decision model | 9B–27B synthetic-family training (Open-Jev, Nimble, Lux class) | 10^4–10^5 | no | Research only | Default: never, because M3 applies |

Tabular side-ladder: majority or base rate → logistic regression → gradient
boosting → TabPFN, only if the weight license fits.

**Synthetic data rules for R3–R4, best supported first:**

1. Labels are computed in code from facts checked independently. An LLM may
   write the text; it does not decide the label (Nimble, Hopper).
2. Build minimal pairs where one focus fact flips the label. Keep both members,
   and the whole source family, in one split.
3. Add missing-evidence twins. Test uniform targets (Kev) against
   exclusion plus abstention (Nimble).
4. Put NOTA both as the answer and as a distractor. Randomize option IDs.
   Augment paraphrase, negation, and order.
5. If a teacher labels items, it is open-weight and run locally, and double
   agreement is required (JevK5). Teacher cross-entropy is used only where the
   teacher agrees with gold (Winnow).
6. Scan every set, including calibration and dev sets, for shared 8-grams and
   question identity against every evaluation set (JevK5 correction, Hopper). A
   missing reference index must fail the scan, not print CLEAN
   (von, patrol).
7. Keep a per-source license table. CC BY-SA sources may constrain
   redistribution of derived data (Lux, Hopper attribution pages).

**Hill-climb infrastructure to reuse or borrow:**

- Existing: `compare_workflows.py` for paired episode losses and the Hoeffding
  confirmation bound; `evaluate_decisions.py` for Brier, reliability, and
  policy cost.
- Borrow from Kev: the champion ledger with a non-inferiority gate, one
  locked-test read ever, per-trial code and data hashes, the out-of-fold
  calibration report, and a claims ledger that maps printed numbers to
  artifacts.
- Borrow from reflex: an index of every run with its verdict, rejects included.
- Borrow from AnyJev: `level` in the output.

---

## 7. Minimum reproduction to select among recipes

**Goal.** Decide which rungs belong in the skill's default path, using tasks
where we own ground truth. This is a plan; nothing has been run.

**Tasks.** T1 is required, T2 is required, and T3 is optional.

- **T1: synthetic policy decisions with code-computed labels** (we control
  ground truth). Include:
  - 8–12 rule families: deadlines with explicit dates, thresholds, precedence,
    exceptions, routing.
  - Minimal pairs.
  - Missing-evidence twins.
  - Negated questions.
  - Seven-option Choice with NOTA.

  Text comes from templates, or from an open-weight Apache-2.0 generator run
  locally. The generator never sees evaluation items. Split by rule family
  and by pair.
- **T2: one human-labelled public set** for an external check. Candidates are a
  BANKING77 20-way subset (CC BY 4.0, comparable to AnyJev's 300-item table) or
  WANLI (CC BY 4.0, comparable to SemIf and Kev). Record the source revision.
- **T3 (optional, maintainer decision): Augustus research-triage
  dispositions.** Labels are archive-only, refine-reference, investigate, or
  new-placement from past folds. It is a real internal decision, but label
  provenance is agent-drafted and maintainer-accepted, so it is a weaker gold.

**Arms.** Mac first; each arm is a frozen, versioned artifact.

| Arm | Content | Runs on |
| --- | --- | --- |
| R0 | Majority or base rate, plus a hand rule for T1 | Mac |
| R1 | Qwen3.5-2B or 4B frozen: `raw`, then two-order averaging, then L0, then OOF temperature (SemIf MLX or reflex MPS code paths) | Mac |
| R2a | LR on a small sentence-embedding model | Mac |
| R2b | Ridge/LDA on the R1 model's ⅔-depth hidden state | Mac |
| R3a | SetFit | Mac |
| R3b | DeBERTa-v3-large fine-tune | CUDA, about $0.25–0.5 per run on reported H100 figures |
| R4 | Kev-0.8B `--init_from` LoRA | CUDA; only if R1–R3 miss the gate |

GPU rental is spend and needs maintainer authorization.

**Splits and size.** Use dev (selection), calibration, and confirmation
splits, group-disjoint. Confirmation is read once per frozen candidate.
- About 470 paired confirmation items per task detect a 5 pp difference when
  about 15% of items are discordant (α = 0.05, power 0.8, normal-approximation
  McNemar). Local arithmetic:
  `calc.py`: 312 items at 10% discordance, 626 at 20%, 155 for a 10 pp effect
  at 20%.
- Per-slice support follows `validation.md`: zero errors in 100 accepted cases
  still allows a 2.95% error rate at 95% confidence.

**Metrics.** Report each one per task and per slice:

- Accuracy.
- NLL and Brier.
- ECE, with bins and counts.
- Coverage at ≤5% error, and AURC.
- Policy loss at a fixed cost matrix.
- Missing-evidence share at P≥0.9.
- Order-flip rate.
- Negation and NOTA accuracy.
- Wall-clock training time and serving latency on the actual MacBook Air.

**Decision rule, fixed before any run:**

- If R1 or R2 is non-inferior (lower bound ≥ −1 pp on T1 and T2 policy loss)
  to R3 and R4, the skill's default stops at R2, and R3 and R4 remain
  documented escalations.
- If R3 or R4 wins on T1 but not T2, record it as workload-local. The skill
  must then require a per-workload gate before it trains.
- If R1 shows ≥ 5% P≥0.9 on missing-evidence twins and neither uniform-target
  nor abstention training fixes it, the skill must route missing evidence to
  exact checks or R0.

**Falsifiers of this report's recommendations:**

- A frozen readout that loses to a generalist LoRA on T2 untouched data,
  which would contradict M3.
- An L2 or LR head that fails to beat R1 at 300 labels on either task, which
  would contradict M4.

---

## 8. Recommendations (summary)

| Item | Action | Why |
| --- | --- | --- |
| No Jev Output in any training, labeling, filtering, or selection path | adopt | MCA §2.3(b) (Contract); survives termination |
| Refine `optimizer-integration.md:262-263` ("provider or teacher distributions as … distillation targets") to "only where the provider's terms allow; TypeSafe's do not" | decide | Current doctrine conflicts with the contract; a runtime edit is outside this lane |
| Frozen readout + OOF per-workload temperature as incumbent (R1) | adopt | reflex, SemIf, AnyJev; Hopper reserve half; M1–M3 |
| Linear probe / LR on frozen features (R2) | adopt | AnyJev L2; arXiv 2408.03414, 2512.22245; CPU-cheap |
| DeBERTa-v3-large as the R3 encoder; ModernBERT-base as the cheap option with an OOD-question test | pilot | kotoba measured costs and OOD; one author, one seed family |
| SetFit and GLiClass as few-label or large-label R3 options | pilot | Mechanism fit; no controlled comparison in hand |
| LoRA + head warm-started from Kev (R4) | pilot | `--init_from` evidence; CUDA-bound |
| Kev champion rule, OOF calibration report, claims ledger | borrow-pattern | Directly addresses M10 |
| Nimble contrastive curation with code-computed labels; JevK5 double agreement; Winnow agree-only teacher CE; Hopper 8-gram screen | borrow-pattern | M6, M8, M10 |
| Reasoning exit (TypeLLM / C3) as a first-class "don't train" route | adopt | Sealed JevBench one-pass ceiling (M9) |
| Generalist 9B–27B decision-model training (Open-Jev, Lux, Nimble class) as a default | reject | M3; not laptop-feasible |
| tasksource ModernBERT-JEV recipe | reject | Near-chance zero-shot; Jev-native data provenance Unknown |
| JevBench rank as a recipe selector | reject | Overlapping sealed intervals; formula-driven rank |
| Decision-1.0, Winnow, Hopper, JevK5 releases | watch | Recipes partly private or CUDA/ROCm-only |
| TabPFN-3.5 | watch | Non-commercial weights; vendor SOTA claims |
| Website ToS automated-access clause versus the research patrol | decide | Affects the autoscience lane (§9) |

---

## 9. Open questions for the maintainer

1. **Counsel reading of MCA §2.3(b).**
   - Does it cover using Jev as an evaluation comparator for a head we train for
     our own workflow?
   - Does it cover active-learning selection by Jev uncertainty?
   - Does it cover publishing an Augustus skill that helps users build
     Jev-shaped local heads ("facilitate the development of a similar …
     product")?
2. **Channel terms.** Do OpenRouter or Vercel AI Gateway access to Jev carry
   the same restriction?
3. **Website Terms §3(b)(vi).** Automated monitoring and copying of
   typesafe.ai "including subdomains" conflicts with the recurring patrol's
   digest checks of docs.typesafe.ai. Seek written permission, rely on
   `llms.txt` as an invitation, or reduce to manual reads?
4. **The actual MacBook Air.** Chip and unified-memory size decide whether R1
   with a 4B model and R2 hidden-state extraction are local, or whether 2B is
   the ceiling.
5. **GPU spend.** Is CUDA rental (Modal or RunPod) authorized for the R3b and
   R4 arms, and with what cap?
6. **T3.** Should Augustus's own triage dispositions be a reproduction task,
   given their agent-drafted provenance?
7. **Missing-evidence design.** Should the skill's default be uniform-target
   training (Kev) or exclusion plus abstention (Nimble)?

---

## 10. Not covered

- Any local run, weight download, or third-party code execution. Every recipe
  number is Reported.
- Bodies of: Kev `PLAN.md`, `docs/claims.json`, and `kev/metrics.py`; Nimble
  `docs/NIMBLE_TRAINING.md`; reflex `docs/results/*` (frozen-vs-trained,
  DISTILLATION); AnyJev `docs/results_*.md`; Hopper, JevK5, and Open-Jev
  training scripts; kotoba typed-decisions iterations after the third.
- Decision-1.0 `EVALUATION.md` (fetched, not read in full), `TASKS.md`, and
  code. Open-Jev `verification/*.json`.
- Terms of any hosted teacher other than TypeSafe (OpenAI, Anthropic, Google,
  OpenRouter, Vercel). Terms of redistributed Jev-output datasets.
- Full papers. arXiv items were read at abstract level, and
  [2606.02907](https://arxiv.org/abs/2606.02907) at title level only.
  arXiv's export API returned HTTP 429, so abstract pages were used.
- Gradient-boosting sources, conformal methods for heads, and multimodal or
  vision heads (Jev-Omni, Valen, SigLIP).
- Laya re-inspection, `decider` (`Mapika/decider`), `featherless-ai/simple-jev`,
  `typed-gguf`, AlexWortega/openjev, openjev-verdict, and `yuan-phd/jev-rlcd-research`
  (empty README).
- The JevBench sealed items, which are private by design.

---

## 11. Sources

Depth key:
- **L** = legal text read in full for the relevant sections.
- **R** = README or card read.
- **S** = source file read.
- **M** = metadata only.
- **A** = abstract page.
- **D** = data or result file parsed.

All retrievals are 2026-09-23 UTC unless noted. "Patrol" means today's
`wf1-patrol-ecosystem` packet (16:15–16:55Z).

| # | Canonical ID | URL | Revision | Retrieved | Depth | Prior card |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | url:docs.typesafe.ai/legal | https://docs.typesafe.ai/legal.md | sha256 4141ec2e…afcf5c | 17:02:54Z | L | first |
| 2 | url:typesafe.ai/legal/mca | https://typesafe.ai/legal/mca | "Last updated Sep 19, 2026"; sha256 b07b91d9…4edbc0 | 17:03:00Z | L (§§1–4, 10, 12–13) | first |
| 3 | url:typesafe.ai/legal/mca (Wayback) | https://web.archive.org/web/20260916215503id_/https://typesafe.ai/legal/mca | "Aug 27, 2026"; sha256 77d65b57…c6983b | 17:03–17:04Z | L (§2.3) | first |
| 4 | url:typesafe.ai/legal/mca (Wayback) | https://web.archive.org/web/20260921155004id_/https://typesafe.ai/legal/mca | "Sep 19, 2026"; sha256 c41c8c84…ff05d9a | 17:04:21Z | L (§2.3) | first |
| 5 | url:typesafe.ai/legal/terms | https://typesafe.ai/legal/terms | "Sep 19, 2026"; sha256 69efcc6b…0ddfd09c | 17:03:01Z | L (§§1–3) | first |
| 6 | url:typesafe.ai/legal/privacy-policy | https://typesafe.ai/legal/privacy-policy | "Nov 19, 2025"; sha256 41186365…816947f | 17:03:01Z | L (training clause) | first |
| 7 | url:typesafe.ai/legal/data-processing | https://typesafe.ai/legal/data-processing | "Apr 24, 2026"; sha256 877470aa…4faba6f5 | 17:03:01Z | M (grep) | first |
| 8 | github:jaredpalmer/kev | https://github.com/jaredpalmer/kev | 557598fced1dada75dfbf36ed144dce309ac6ceb | 17:05:06Z | R + S (calibrate.py, autoresearch.py, skills/kev-finetune SKILL.md, data-generation.md) | §45 |
| 9 | hf:llm-semantic-router/Decision-1.0-Lux-9B | https://huggingface.co/llm-semantic-router/Decision-1.0-Lux-9B | bd45a30aee8c84032791c245c70f86dee5389cc8 | 17:04:47Z | R (README, METHODS, ATTRIBUTIONS, DIAGNOSTICS, RUNTIME) | patrol first |
| 10 | hf:llm-semantic-router/Decision-1.0-Nox-4B, -Sol-2B | https://huggingface.co/llm-semantic-router | 0bb833504965… / 0665a41108e8… | 17:12:3xZ | M | patrol first |
| 11 | hf:ZefanCai/Open-Jev-27B-v1.1 | https://huggingface.co/ZefanCai/Open-Jev-27B-v1.1 | 28cf73067d5b337860bbef3c85b8b82ba8730956 | 17:08:23Z | R (full card) | §165 |
| 12 | github:bespokelabsai/nimble | https://github.com/bespokelabsai/nimble | 38edc3b576f13179df785d412621d5cb1128d02d | 17:05:52Z | R | §35 |
| 13 | github:allebee/jevk5 | https://github.com/allebee/jevk5 | 708556582fb419e9038e2f7f654f2805daddc4ba | 17:05:54Z | R + S (CHANGELOG) | §165 |
| 14 | hf:alibiserikbay/JevK5 | https://huggingface.co/alibiserikbay/JevK5 | 3c673298eb7f2dc7cb98019262c55b1fac01a0bc | 17:08:23Z | M | §165 |
| 15 | hf:HopitAI/hopper | https://huggingface.co/HopitAI/hopper | 281d393f65ecfaf25c729a60b8f7fff61b49f9b4 | 17:07:24Z | R | first |
| 16 | hf:EldanRing/Winnow-12B | https://huggingface.co/EldanRing/Winnow-12B | b6ac22b0d51b69b18200acacb3fbdd98073fffe8 | 17:07:25Z | R | first |
| 17 | github:kshetrajna12/reflex | https://github.com/kshetrajna12/reflex | 231f896d818a62b94fec305ed553df1088486dcb | 17:07:25Z | R | §121 |
| 18 | github:fstandhartinger/jevbench | https://github.com/fstandhartinger/jevbench | 2fa63fa3226cb369795525ed011800f57dcbd894 | 17:06:36Z | R + D (RELEASE-v1.4.0, METHOD-v1.4, v1.2-additions-winnow, v1.4 results JSON) | §78, patrol |
| 19 | github:TheoLeeCJ/SemIf (API full_name SemIf-OpenJev) | https://github.com/TheoLeeCJ/SemIf | 1f2dea3e25379f9dfc98cb83c324f00ab5deda37 | 17:05:45Z | R | §117 |
| 20 | github:nokia-applied-research/AnyJev | https://github.com/nokia-applied-research/AnyJev | 73fa8c663e5ea27b5312d11fe18a5d9157b10bd2 | 17:05:47Z | R | §151/§165 |
| 21 | github:strangeloopcanon/dynajev | https://github.com/strangeloopcanon/dynajev | 8afc7ef30520fc79c6bb36d4de140cdb7e8411c8 | 17:05:49Z | R | patrol first |
| 22 | github:TypeLLM/TypeLLM | https://github.com/TypeLLM/TypeLLM | d592c10cd527188e5e81c22a2816017a988c6d8f | 17:05:50Z | R (partial) | §32/§113 |
| 23 | github:kikoncuo/jevfire | https://github.com/kikoncuo/jevfire | 5df83b558bf635e006d31f8f2fc2798d0e3ff051 | 17:05:56Z | R | first |
| 24 | github:jdev/jev-research | https://github.com/jdev/jev-research | HTTP 404 (API and web) | 17:05:57Z, 17:11:19Z | — | task-named; unavailable |
| 25 | github:liuup/jev-research | https://github.com/liuup/jev-research | 4a0fcad9d28830e016570dc325f44bf5ac84895e | 17:11:25Z | R (opening) | first; not joined to #24 |
| 26 | github:Knowledgator/GLiClass | https://github.com/Knowledgator/GLiClass | 40baa67cdea577449bc3f6a251646377b2cb0a6c | 17:05:58Z | R | §19 |
| 27 | hf:knowledgator/gliclass-{edge,base}-v3.0, -instruct-large-v1.0 | https://huggingface.co/knowledgator | df03993a… / 77a70e6c… / 825e5478… | ~17:12Z | M + R (grep) | §19 |
| 28 | arxiv:2508.07662v1 (GLiClass) | https://arxiv.org/abs/2508.07662 | v1 | 17:10:27Z | A | §19 |
| 29 | hf:tasksource/modernbert-tasksource-jev | https://huggingface.co/tasksource/modernbert-tasksource-jev | 790beda6257fe1531e50426b60f07d396b1f9663 | 17:08:22Z | R | patrol M |
| 30 | hf:ds:tasksource/tasksource-jev-typed-decisions; hf:ds:tasksource/procedural-jev | https://huggingface.co/datasets/tasksource | 6ec3f6be… / 3c11c134… | 17:08:37–38Z | R (grep) | first |
| 31 | github:tasksource/train_jev | https://github.com/tasksource/train_jev | HTTP 404 | 17:08:45Z | — | unavailable |
| 32 | hf:ds:SargeDev/jev-distill-corpus | https://huggingface.co/datasets/SargeDev/jev-distill-corpus | bd686f32e9b3982b1a46a5f0c436157e293e6c98 | 17:08:38Z | R (grep) | archive (changelog-hourly) |
| 33 | hf:com-kotobalabs/open-jev-deberta-v3-large | https://huggingface.co/com-kotobalabs/open-jev-deberta-v3-large | 19bf9a64815add579fbf6c907bef584d9277a8e4 | 17:08:23Z | R (grep) | §33 |
| 34 | github:kotoba-lang/typed-decisions | https://github.com/kotoba-lang/typed-decisions | e4ed807630c061179a6834d77e18c43227e4f19d | 17:06:00Z | R (grep, iterations 1–3) | §130 |
| 35 | hf:convaiinnovations/laya | https://huggingface.co/convaiinnovations/laya | not re-fetched | archive 2026-09-18 | archive | §18 |
| 36 | github:DECRUX9812/openjev-lm | https://github.com/DECRUX9812/openjev-lm | not re-fetched | archive 2026-09-18 | archive | §25 |
| 37 | github:huggingface/setfit | https://github.com/huggingface/setfit | be332d6d4993e272fd9bca4364e8025880228b48 (release v1.2.0) | 17:06:01Z | R | §19 mention |
| 38 | arxiv:2209.11055v1 (SetFit) | https://arxiv.org/abs/2209.11055 | v1 (2022) | 17:10:39Z | A | first |
| 39 | github:PriorLabs/TabPFN | https://github.com/PriorLabs/TabPFN | eeb37a6c4e4b8803af41faa57c3672c61caa5b44 | 17:06:03Z | R (license, limits) | judgment-class link |
| 40 | arxiv:2609.17895v1 (TabPFN-3.5) | https://arxiv.org/abs/2609.17895 | v1 2026-09-15 | 17:10:40Z | A | first |
| 41 | github:ml-explore/mlx-lm | https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md | 15bcf8b929e5da67aa7f8fe6feda7fb9eda00050 | 17:10:52Z | S (LORA.md) | first |
| 42 | arxiv:2408.03414v2 | https://arxiv.org/abs/2408.03414 | v2 (2024) | 17:10:26Z | A | first |
| 43 | arxiv:2512.22245v1 | https://arxiv.org/abs/2512.22245 | v1 (2025-12-23) | 17:10:25Z | A | first |
| 44 | arxiv:2512.12677v3 | https://arxiv.org/abs/2512.12677 | v3 (2026-05-25) | 17:10:26Z | A | first |
| 45 | arxiv:2606.10487v1 | https://arxiv.org/abs/2606.10487 | v1 (2026-06-09) | 17:10:26Z | A | first |
| 46 | arxiv:2606.02907 | https://arxiv.org/abs/2606.02907 | unknown | search result only | title | first |
| 47 | arxiv:2504.15432v1 | https://arxiv.org/abs/2504.15432 | v1 (2025-04-21) | 17:10:26Z | A | first |
| 48 | arxiv:2511.16600v3 (YOFO) | https://arxiv.org/abs/2511.16600 | v3 (2026-02-02) | 17:10:27Z | A | dynajev citation |
| 49 | arxiv:2309.03882v4 (PriDe) | https://arxiv.org/abs/2309.03882 | v4 | 17:10:39Z | A | first |
| 50 | arxiv:2102.09690v2 (contextual calibration) | https://arxiv.org/abs/2102.09690 | v2 (2021) | 17:10:39Z | A | first |
| 51 | arxiv:1706.04599v2 (temperature scaling) | https://arxiv.org/abs/1706.04599 | v2 (2017) | 17:10:39Z | A | first |
| 52 | arxiv:2412.13663v2 (ModernBERT) | https://arxiv.org/abs/2412.13663 | v2 (2024) | 17:10:40Z | A | first |
| 53 | arxiv:2106.09685v2 (LoRA) | https://arxiv.org/abs/2106.09685 | v2 (2021) | 17:10:40Z | A | first |
| 54 | arxiv:1909.12434v2 (counterfactual augmentation) | https://arxiv.org/abs/1909.12434 | v2 (2020) | 17:10:40Z | A | first |
| 55 | arxiv:2201.05955v5 (WANLI) | https://arxiv.org/abs/2201.05955 | v5 (2022) | 17:10:41Z | A | first |
| 56 | arxiv:2310.01208v1 (LS-LLaMA) | https://arxiv.org/abs/2310.01208 | v1 (2023) | 17:10:41Z | A | first |
| 57 | TypeLLM fair-die blog | https://typellm.ai/blog/fair-die | 2026-09-22 post | patrol 16:15–16:55Z | patrol R | §113, patrol |
| 58 | Augustus runtime doctrine | `.agents/skills/augustus/references/{optimizer-integration,validation,judgment-class,faq}.md` | repo HEAD 4236a60 | local read | S | — |
| 59 | Local arithmetic | `research/080/tmp/trainer/calc/calc.py` → `calc_out.json` | sha256 adc37cf6… / a9e1e60e… | 17:12Z | executed (own code) | — |

Stars, likes, and downloads observed during retrieval, for example Kev 5,624★,
Nimble 1,675★, SemIf 4,049★, open-jev-deberta 61 likes, and Open-Jev-27B 0
downloads, are observations only. They did not affect any disposition.
