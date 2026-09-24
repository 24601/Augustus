# Trainer sweep: train-your-own-Jev recipes, 2026-09-14 to 2026-09-24

Lane: 0.8.0 trainer skill research (confidential, local only). Synthesis
written 2026-09-24 ~01:20Z from four retrieval lanes run 2026-09-23 ~17:50Z to
2026-09-24 ~00:55Z, plus 16 deep-inspection recipe cards. Nothing third-party
was installed or run, and no weights were downloaded. Every third-party number
is **Reported** (the source's own measurement); nothing here is
**Reproduced**. Evidence labels follow `research/protocol.md`: Contract,
Reported, Reproduced, Hypothesis, Unknown. Provenance verdicts are readings of
repository text against MCA §2.3(b), not legal advice.

**Legal fact carried through every row (Contract, verified 2026-09-23 in
`trainer-recipes.md` §2).** TypeSafe Master Customer Agreement §2.3(b) bars
using "the Services or any Output ... to perform model distillation, train a
model to imitate the output of the Services, or develop (or to facilitate the
development of) a similar or competing product or service". Each item below
records whether its training data, labels, targets, rewards, features or
selection came from Jev output.

---

## 0. Headline

- **298 training-relevant artifact ids, about 268 distinct projects**:
  collapsing 25 known sibling groups (a GitHub repo and its HF checkpoint or
  dataset, for example) removes 30 ids. All were created or pushed on or after
  2026-09-14.
  - **78 were created on 2026-09-23 or later** ("the last day"; one,
    `ivanviragine/jev-vs-llms`, was created 2026-09-24T00:19Z, just past the
    nominal window). 200 more were created or pushed 2026-09-21 onward; 20
    fall only in 2026-09-14..20.
  - Relevance: 218 train a model (one of them, `beratcmn/qwen3.5-0.8b-systemone`,
    turned out on inspection to train nothing), 22 datasets for training, 32
    eval harnesses, 26 skills or guides.
- **Jev-output provenance: 43 use Jev outputs, 101 unclear, 154 no.**
  - 21 **trained on** Jev output: 17 as labels or soft targets (imitation or
    distillation), 2 as RL reward, 2 as input features only.
  - 6 **ship a runnable Jev-teacher path** in an otherwise non-Jev project
    (whether the shipped weights used it is unverified for most).
  - 3 let **Jev select or filter** training rows.
  - 4 are **published corpora** of Jev output labelled as training data.
  - 5 **hold Jev outputs** as evaluation records (safe only if never joined
    into training).
  - 4 are **guides recommending** it, including TypeSafe's own cookbook
    (features for a CatBoost model).
  - Of the 7 last-day uses, 5 trained on Jev output (`fireworks-jev-reward-rl`,
    `autotrust/JEV`, `StevenJPx2/jev-distill`, `Adamya05/jev-echo`,
    `Holy-Coders/doorman`).
- **Prior status, re-checked against origin/main `d8dc848` (notes through
  §168):** 94 first sightings (27 of them created in the last day), 142 archive
  metadata rows only (listed in a discovery packet, never inspected), 5 in
  sources/fingerprints only, 57 named in `notes.md` (carded or mentioned).
  The HF lane's "first-sighting" label was downgraded for 44 ids that sit in
  archive discovery packets (§1.5).
- **Top 3 to borrow** (Jev-free mechanism, cheap to run, honest evaluation):
  1. `adimyth/compass`: the promotion scaffold (pre-registered rule, disjoint
     selection/calibration/release/shadow splits, a rejected-variants table,
     committed per-item records) plus training through the serving readout
     with permutation-consistency and opaque-label losses.
  2. `StevenJPx2/jev-distill`'s harness **with the teacher swapped out**:
     CPU-only, deterministic, union-find leakage components, hash-only label
     ledger, budget and approval gate, "a failure is never a label", and
     separate agreement-with-teacher vs accuracy-vs-gold reports with Wilson
     intervals and a majority baseline.
  3. `integrallis/models`: a Noul head fit on the hidden states of the
     project's own Granite 4.1 3B with digest-pinned labels, where the
     no-Jev-output rule is enforced in types and tests (a feature-free
     `ExternalVerdict` type, `LogisticHeadTrainer.fit` accepting only `int[]`
     labels, and a bytecode-scan `ExternalArmIsolationTest`). Item-level
     evidence only; not deep-carded.

  Runners-up: `mateolafalce/system-one-model` (human gold plus a weak local
  teacher on an 8 GB GPU, with a disclosed missed gate) and `bandr-ai/bandits`
  #73 (the closest outside analog to the planned skill).
- **Doctrine gaps the sweep exposes** (§6): RL reward and preference use are
  missing from the barred-use list; the barred-corpus list names one corpus
  where at least six exist; the vendor's own cookbook trains on Jev answers as
  features; and seven recurring evaluation defects need hard gates.

---

## 1. Coverage ledger

### 1.1 GitHub repository search (lane R)

- **Method.** `gh api search/repositories` only; no code search, no paid
  APIs. Retrieval 2026-09-23 ~17:50Z to 2026-09-24 ~00:30Z. Scratch:
  `tmp/gh-repo-search/`.
- **Batch 1: 114 queries, 0 errors.** Every required term was run with both
  `created:>=2026-09-21` and `pushed:>=2026-09-21`. Pushed totals:

  | Query | Pushed | Query | Pushed |
  |---|---:|---|---:|
  | jev train | 29 (created 23) | "decision head" | 7 |
  | "train your own" jev | 1 | "typed decision" train | 7 |
  | open jev | 264 | noul train | 2 |
  | openjev | 56 | "choice score noul" | 32 |
  | jev replica | 2 | "system one" model | 270 |
  | jev distill / distill jev | 8 / 8 | typesafe jev fine-tune | 2 |
  | jev-like | 57 | jev lora | 11 |
  | jev alternative | 23 | jev encoder | 8 |
  | jev classifier | 124 | jev benchmark train | 4 |
  | noul | 106 | jev fine-tune | 16 |
  | jev dataset | 18 | jev teacher | 3 |
  | jev local | 296 | | |

- **Bare "jev" exceeded the 1,000-result cap** (3,704 created / 4,929 pushed
  since 09-21), so it was fully enumerated by recursive time slicing: created
  09-21..24 fetched 3,705 of 3,706; created 09-14..20 with pushed ≥ 09-21,
  1,121; created before 09-14 with pushed ≥ 09-21, 105. The sum, 4,930,
  matches the pushed total.
- **Batch 3: 112 queries, 0 errors.** Fused tokens (openjev, jevk5, jevlike,
  anyjev, nanojev, llm2jev and others; 23 returned 0); non-jev terms
  (systemone 68, rlcd 56, semif 70, laya fine-tune 18, laya train 6); 8 core
  terms for created 09-14..20; 16 `in:readme` variants. **Three `in:readme`
  queries were truncated at 1,000 and not sliced:** "jev train" 1,151, "jev
  encoder" 1,053, "jev labels" 3,163.
- **Funnel.** Union 7,183 unique repos → dedupe against origin/main
  (sources.json, revisit_fingerprints.json with 1,211 GitHub ids, all of
  notes.md, every `research/archive` file including the patrol's 5,094
  first-sighting node rows, plus trainer-recipes.md; joined by slug and
  node_id): 5,386 known at some depth, 1,792 with no trace → training-keyword
  filter: 1,683 candidates read by hand → README and HEAD fetched for about
  290 → static grep (no execution) of up to 8 teacher/label/data files per repo
  for `api.typesafe.ai`, `typesafe/jev`, `jev-1.1x`, `TYPESAFE_API_KEY`,
  `/v1/systemone` → **210 items** (138 train, 34 serving-only, 18 eval, 11
  data, 9 guides; uses 22, no 87, unclear 101).
- **Excluded.** About 1,470 filter candidates (hosted-Jev integrations: MCP
  servers, routers, hooks, SDKs, browser agents, games, trading bots, awesome
  lists) and name collisions (ESP32 RLCD displays, "semifinal" student repos);
  `kazu5150/jev-train` (a speed race; trains nothing);
  `g0runmezadam/jev-architecture-research` (probing). Aliases folded:
  lawrence3699/* mirrors; musubi-labs/musubi-jev and asdfjep/kev (Kev README
  copies); LeanFly/NanoJev and bigqiao/NanoJev-MLX; wayfind/metask-jev.
- **Limits.** Default repository search covers name, description and topics
  only. The index shifted during pagination. Sibling-lane rate-limit
  contention caused ~15 s backoffs. Items without a SHA were not fetched. One
  stray scratch write to `/tmp/x_md_list` (archive file names only) was
  deleted immediately.

### 1.2 Hugging Face Hub (lane H)

- **Method.** 72 list calls, all HTTP 200:
  `huggingface.co/api/{models,datasets,spaces}?search=<term>&sort={lastModified,createdAt}&direction=-1&limit=100&full=true`
  for 12 terms. Scratch: `tmp/hf-hub/`.
- **Unique repos per term (models / datasets / spaces):** jev 179 (paged to
  end) / 70 / 96; openjev 45/8/14; open-jev 45/8/15; noul 2/0/3 (unrelated,
  pre-2026); typed-decision 32/13/9; decision-head 6/0/0; system-one 27/17/11;
  jevlike 0/0/0; jev-distill 1/2/0; kev 100/100/100 (capped); laya 200 (paged,
  cap still hit) / 23 / 100; decision 100/100/100 (capped).
- **Caps.** Models "jev" and "laya" were paged with the Link cursor ("jev"
  reached the end; "laya" stopped at 200 with oldest createdAt 2026-08-10,
  which covers the window). For every other capped set, the oldest createdAt
  on the createdAt-sorted page predates 2026-09-14, so the window is covered.
- **Funnel.** 1,407 unique repos. Window A (created or modified ≥ 09-21):
  334 models / 63 datasets / 93 spaces; window B (09-14..20): 104 / 44 / 47;
  older 722. Of 643 in-window non-noise rows, 256 were already in the archive
  and 387 (+2 restored) were candidates; 42 name collisions dropped (kevin*,
  Keval*, Layan*, Layase). README fetched via `/raw/main` for 389 candidates
  (30 returned 404/401, e.g. gated `Mapika/surogate`, `winrisef/codecpilot`).
  106 model rows classified as format ports (about 50 Laya ports, about 20
  Kev ports, 11 APUS, openjev FP8/MLX, Jev-Omni GGUF) and marked
  serving-only. Mirrors verified by hash (e.g. `gionebeats/Open-Jev-2B` and
  `junetask/Open-Jev-9B` adapters identical to `ZefanCai/Open-Jev-2B/9B`) →
  **87 items**.
- **Revisits.** 33 archived HF repos whose SHA moved since the last
  fingerprint look (e.g. `AXERA-TECH/Laya` §140, `DKNTZMN/gan8-vs-jev` §167,
  `WIlfLin/JEV-Qwen3.5-*` §162, `apus-ailab` 4B/9B/35B-A3B §162,
  `chaoliangUNSW` v2 §167, `lostargon/Tiny-Jev` §153/§167,
  `wayfind/metask-jev-4b-policy-mix` §134). These are revisit candidates, not
  new items.
- **Failures and limits.** HF `search=` matches repo ids, not card text. Near
  the end HF rate-limited the IP on `/api/datasets/{id}/tree`, so per-row file
  listings for bonzi-vs-jev-wanli256, SamuelChien821, code-holes,
  laya-formatting-fragility, AIMultiple and dylantom2012 were not verified
  (cards only); no HF calls after that. **The lane's dedupe base did not
  include `research/archive/*.json`** (see §1.5).

### 1.3 Open web and directories (lane W)

- **Method.** Retrieval 2026-09-23T23:50Z to 2026-09-24T00:12Z, compared with
  the latest archive retrievals (hourly §168 at 21:44Z; patrol jevusers at
  16:18Z). Scratch: `tmp/open-web/` (evidence packet `lane_packet.json`,
  sources in `src/`, awesome-list diffs in `awesome/`).
- **Built-in web search: 31 queries**, about 8–10 results each, covering
  "train your own Jev", distill/replica/alternative/clone phrasings, Noul and
  decision-head training, RLCD, typed-decisions datasets, MLX/Unsloth/Colab,
  Show HN / LocalLLaMA, Together tev1, "no Jev outputs", and Jev distillation
  terms of service.
- **Web fetch: 10 attempted, 9 read** (together.ai, seangoedecke, distillabs,
  anth.us fine-tuning-jev, orcarouter, rohitraj, wunderlandmedia, jevaiguide,
  redlinesoft). The wonderwhy-er Medium post returned 403 and was not read.
- **Directories.** jevusers `/api/projects`: first 200 went to /dev/null,
  then HTTP 500 (Cloudflare 1101); saved at 23:55:39Z, 0 added and 0 removed
  against the patrol set. jevusers `/apps`: 19 × 500, then 200 at 00:00:15Z,
  sha256 identical to the patrol's. `/new`: 200. madewithjev.com
  `/open-source-jev`, all 35 `/builds` pages, and `/github-repos` (263 cards,
  text scan). **jev.magicteams.ai (1,362 builds, client-rendered) was not
  enumerated**, and its MCP endpoint was not called (third-party tool).
  notsointresting/awesome-jev-family: 62 links, 2 not in the archive, neither
  trains.
- **Awesome lists.** Base = last commit before 09-21T00:00Z. Added URLs since:
  yibie 123, hellogumbo 343 (projects.json 997 entries, 304 added),
  AnotiaWang 25, cobanov 39, AbdelStark 118, Anil-matcha 31, MrJev 137,
  logicrw 295. Training-keyword union 148 URLs: 135 already known (about 55
  metadata-only), 10 new, none of which trains. The AbdelStark compare API
  truncates at 300 files, so its diff used raw README.md and llms.txt.
- **Limits.** `doofz/systemone-rlcd` returned an error (unavailable evidence,
  not absence). Laya fork compares (debjyotikm, hemanthrayuduu,
  maxfield-allison) returned 404 and were treated as fork noise.
  systemonemodels.org, scriptbyai, llmgateway and iapp.co.th were seen in
  search results only.

### 1.4 GitHub code search and agent skills (lane C)

- **Method.** Retrieval 2026-09-23 ~22:30Z to 2026-09-24T00:14Z. Legacy REST
  `search/code`, first page only, per_page=100, best-match order, no date
  filter, default branch only. Scratch: `tmp/gh-code-skills/` (148 raw search
  JSONs).
- **Code queries: 40, with total counts.** 1 'Noul train' 366,592; 2 'jev
  fine-tune filename:README.md' 686; 3 'choice score noul language:Python
  train' 25,984 (language:Python because path:*.py is unsupported); 4 'jev
  train filename:SKILL.md' 1,136; 5 'kev-finetune' 29; 6 'openjev in:file'
  13,120; 7 'Noul lora' 158,720; 8 'jev distill' 50,432; 9 'systemone train
  language:Python' 634; 10 'Noul filename:SKILL.md' 1,656; 11 'jev
  filename:SKILL.md fine-tune' 17; 12 '… distill' 38; 13 '… lora' 115; 14
  'noul filename:train.py' 2,032; 15 'jev path:train language:Python' 32; 16
  'jev teacher labels language:Python' 406; 17 'systemone filename:SKILL.md
  train' 77; 18 '"decision head" filename:SKILL.md' 112; 19 'kev
  filename:SKILL.md train' 6,880 (mostly substring noise); 20 'laya
  filename:SKILL.md finetune' 42; 21 'jev distill filename:README.md' 729; 22
  'jev "soft targets"' 386; 23 'typesafe teacher language:Python' 161; 24
  '"/v1/systemone" train' 3,264; 25 'jev classifier filename:train.py' 10; 26
  '"Master Customer Agreement" jev' 73; 27 'typesafe distillation terms' 335;
  28 'setfit jev' 563; 29 'noul brier train' 26,368; 30 'jev "training data"
  filename:SKILL.md' 10; 31 '"2.3(b)" typesafe' 32; 32 '"2.3(b)" jev
  distillation' 19; 33 'filename:SKILL.md classifier train calibrate' 2,708;
  34 'filename:SKILL.md setfit' 46; 35 'filename:SKILL.md "decision model"
  fine-tune' 7; 36 'filename:SKILL.md "soft targets"' 563; 37
  'filename:SKILL.md typesafe distill' 32; 38 'noul cross_entropy
  language:Python' 14,048; 39 '"jev-distill-corpus"' 41; 40
  'filename:SKILL.md laya train' 6,080. Hits from queries 1–30 merged to
  1,247 unique repos; GraphQL metadata put 640 in the window, 82 with
  training-type paths. **Queries 33, 34, 36, 38 and 40 were
  fetched but not triaged** (coverage gap); 31, 32, 35, 37 and 39 were
  triaged by eye.
- **Repo queries: 34** (sort=updated, pushed ≥ 09-14 unless noted), union
  460 repos: jev skill train 1; jev finetune 4; jev fine-tune 21; jev lora 14;
  jev distill 10; jev distillation 8; jev trainer 36; jev head 29; train jev
  39; jev student 1; jev teacher 4; kev finetune 0; laya finetune 3; laya
  fine-tune 20; laya train 7; "system one" train 11; systemone train 1; claude
  skill classifier train 0; codex skill train classifier 0; skill fine-tune
  classifier 0; decision model train skill 1; typed decision train 21; jev
  clone 6; jev skill created ≥ 09-21 148; noul 177; jev calibrate head 2; jev
  probe 17; openjev train 3; jev dataset 26; jev labels 92; jev-like train 3;
  open jev lora 8; agent skill train classifier 0; skill finetune small model
  0. Many "jev labels" hits are Gmail/issue labelers and were not carded.
- **Deep reads.** GraphQL README plus root tree for 90 candidates; about 120
  specific files (training scripts, SKILL.md, DATA_SOURCES, THIRD_PARTY) in 5
  batches; REST compares for kev and von; HF API plus raw cards for SargeDev
  v3, LocalLLaMA/typed-decisions, dwidlee phase2, Praveenrajus/jev-bench.
- **Failures.** Repo searches 11–19 first hit the shared 30/min search limit
  (403) and succeeded on retry. **Result: 57 items** (uses 15, unclear 8, no
  34); 55 of 57 created or pushed ≥ 09-21.

### 1.5 Synthesis step (this file)

- **Merge.** Lane items minus 37 serving-only and 2 unrelated rows = 280
  unique ids, plus 18 open-web-only items = **298** (no id was serving-only
  or unrelated in one lane and training-relevant in another, checked). Where two lanes carried
  one id, text came from the first of R > H > C > W; lane membership is the
  union. Merged file: `tmp/sweep-synth/items_298.json`.
- **Card verdicts replace lane verdicts** for the 16 deep-inspected items: 9
  moved unclear → no (compass, JevNext, hotdog, mtlm-router, nagi,
  laya-session-guard, MoJev, SnapJudge, beratcmn), and beratcmn's relevance
  moved to "readout only". Carded "no" verdicts keep their caveats in the
  table (hosted-drafter labels, sealed Jev predictions visible during
  selection, private lineage).
- **Cross-lane adjudications** (the lanes disagreed; the stricter reading
  with file-level evidence wins):

  | # | Item | Lanes said | Adopted | Evidence |
  |---:|---|---|---|---|
  | 1 | `wfzyx/von` | R unclear, C uses | **uses** (path) | `training/prepare_distill_dataset.py` (commit `ac9f3da996`, 2026-09-22T20:48Z) harvests SargeDev v3 `yuri_v3` (Jev 1.13 soft targets); shipped weights unverified |
  | 2 | `chukfinley/gavel` | R no, C uses | **uses** (path) | `scripts/label_with_jev.py` asks `typesafe/jev-1.13` via OpenRouter; `src/gavel/teacher.py` attaches soft targets; README claims public human labels |
  | 3 | `Barneyjm/circuit` | R uses, C no | **uses** | R read code (`train_lora.py` docstring "averaged Jev+Gemini reference", `teachers.py` → api.typesafe.ai, `refs.jev` in 60/180 sampled `publish_train.jsonl` rows); C read the README banner |
  | 4 | `TianyuCodings/NanoJev` | R uses, C no | **uses** (path) | Shipped `label_decision_dataset.mjs` calls teacher `jev`; C's design doc gates Jev supervision behind authorization and defaults to Qwen3 teachers. Both readings hold; the path exists |
  | 5 | `theolivenbaum/llm-shield` | W no | **unclear** | Trains on LocalLLaMA/typed-decisions, whose gold is an unnamed ~4B teacher; the shared lane rule makes every typed-decisions derivative unclear |
  | 6–10 | `OmniJev/PlayJev`, `Caho1/Jev`, `uzuw/laya-cli-gate`, `janmejai2002/gutcheck`, `ArturL6/specialist-factory` | R unclear, C no | **no** | C read training files: scripted per-game teachers; explicit compliance note; hand-written command lists; no Jev in the training path (gutcheck's benchmark is Gemini-synthetic); BART-MNLI/CLIP/OpenRouter-VLM teachers with per-signal provenance |

  Net: the lane items as delivered implied 41 uses / 115 unclear / 142 no;
  after card verdicts and adjudication, **43 / 101 / 154**.
- **Dedupe re-check.** origin/main was re-fetched (still `d8dc848`, notes
  through §168) and `research/` extracted to `tmp/sweep-synth/research/`
  (18 MB). Each id's slug was matched with boundaries against notes.md (with
  section numbers), sources.json, revisit_fingerprints.json, every archive
  file, the other research/*.md, and local `research/080/*.md`
  (`tmp/sweep-synth/dedupe.py`). "First-sighting" means no trace anywhere.
  **44 HF ids labelled first-sighting by lane H are archive metadata rows**
  (mostly `2026-09-23-patrol/coverage-ledger.json` and
  `2026-09-22-refresh/huggingface-discovery.json`): lane H's dedupe base was
  sources, fingerprints, notes and local files, not archive packets. They are
  still first *cards*. A notes hit means the slug is named, not necessarily
  carded. Slug matches do not distinguish hosts, so a GitHub archive row can
  mark its same-slug HF sibling as known.
- **Scratch.** `tmp/sweep-synth/` holds `openweb_items.json` (transcribed
  from the lane W payload), `merge.py`, `adjudicate.py`, `dedupe.py`,
  `table.py`, `items_298.json`, `table.md`, and the origin/main extract. No
  tracked files were modified; nothing was pushed, posted or contacted.

---

## 2. Training-relevant items (298)

**Legend.**
- **▣** = deep-inspected; a recipe card is in §3 and its verdict replaces the
  lane's (the lane's value is shown as "(lane: …)").
- **Win** (from created/pushed): **D** = created 2026-09-23T00:00Z or later
  (the last day); **A** = created or pushed 2026-09-21 onward; **B** = only
  2026-09-14..20.
- **Rel.**: train = trains a model; data = dataset for training; eval = eval
  harness; guide = skill or guide.
- **Provenance**: *uses* names the use; *unclear* = training exists but the
  label source is unnamed or conflicting (every LocalLLaMA/typed-decisions
  derivative is unclear, because its gold is the mean of 3 samples from an
  unnamed ~4B-class teacher, card sha `c76749ec`); *no* = the source says so
  outright or names only non-Jev label sources. An empty grep never counted as
  evidence of "no".
- **Prior**: "notes §N" = slug named in origin/main `research/notes.md` at
  that section; "archive meta (…)" = only in an archive discovery packet
  (patrol-gfs = `2026-09-23-patrol/github-first-sightings.json`; refresh-ghd /
  refresh-hfd / refresh-jevusers = `2026-09-22-refresh/{github,huggingface}-discovery.json`
  / `jevusers-inventory.json`; patrol-ledger = `2026-09-23-patrol/coverage-ledger.json`);
  "sources/fp only" = in sources.json or revisit_fingerprints.json but not
  notes; **first-sighting** = no trace anywhere; "TR" = also named in local
  `trainer-recipes.md`; "(lane: first)" = the lane said first-sighting and the
  re-check disagrees.
- **Lanes**: R = GitHub repo search, H = Hugging Face, C = code search and
  skills, W = open web and directories.
- "What" is truncated at about 105 characters; the full text and signal are
  in `tmp/sweep-synth/items_298.json`. Row order: use class, then created
  date descending; within unclear and no, training items first.

### 2a. Uses Jev outputs (43)

**T. trained on Jev output (21)**

| # | ID | Created / pushed (UTC; 2026 unless shown) | Win | What | Rel. | Jev-output provenance | Prior (re-checked on origin/main d8dc848) | Lanes |
|---:|---|---|:-:|---|---|---|---|:-:|
| 1 | [github:sophiamyang/fireworks-jev-reward-rl](https://github.com/sophiamyang/fireworks-jev-reward-rl) ▣ | 09-23 18:02 / 09-23 20:31 | D | RL cookbook on Fireworks: Qwen3.8-27B rank-8 LoRA writer trained with Jev scores as the reward | train | uses — RL REWARD | **first-sighting** | R |
| 2 | [hf:autotrust/JEV](https://huggingface.co/autotrust/JEV) | 09-23 12:08 / 09-23 14:20 | D | Qwen3.5-9B + 40.2M-param LoRA and linear fp32 head (24 slots, per-kind temperature); self-described … | train | uses — SOFT TARGETS via SargeDev v3 (self-described Jev student) | archive meta (patrol-ledger) (lane: first) | H |
| 3 | [github:StevenJPx2/jev-distill](https://github.com/StevenJPx2/jev-distill) ▣ | 09-23 05:05 / 09-23 05:05 | D | TypeScript CLI that distills Jev typed decisions into small task-specific student classifiers | train | uses — LABELS + SOFT TARGETS + confidence FILTER (sole teacher) | archive meta (patrol-gfs) | RC |
| 4 | [github:Adamya05/jev-echo](https://github.com/Adamya05/jev-echo) ▣ | 09-23 04:03 / 09-23 20:14 | D | Echo: 22,212-param Snake policy trained on Jev answers, with DAgger rounds relabelled by Jev | train | uses — SOFT LABELS + DAgger relabel + Jev-derived driver | archive meta (patrol-gfs) | RC |
| 5 | [github:Holy-Coders/doorman](https://github.com/Holy-Coders/doorman/blob/1b62ccaf50d64b1e5e8e12cdf921df5a72c6e603/tools/classifier/train.py) | 09-23 03:30 / 09-23 22:52 | D | Offline LR + LR calibrator over session telemetry with optional 'jev_' enrichment features; labels are … | train | uses — FEATURES (optional jev_ enrichment) | **first-sighting** | C |
| 6 | [hf:mpuig/system-one-minicpm5-2b-q8](https://huggingface.co/mpuig/system-one-minicpm5-2b-q8) | 09-22 15:46 / 09-23 06:39 | A | MiniCPM5-2B-Base LoRA fused and 8-bit MLX quantized with the same frozen recipe (public recasts + … | train | uses — SOFT TARGETS (pinned jev-1.13.0) | archive meta (patrol-ledger) (lane: first) | H |
| 7 | [hf:mpuig/system-one-qwen3-0.6b](https://huggingface.co/mpuig/system-one-qwen3-0.6b) | 09-22 15:46 / 09-23 06:39 | A | MLX rank-16 attention LoRA on Qwen3-0.6B; 8.7k recast public questions + ~1.6k synthetic scenarios whose … | train | uses — SOFT TARGETS (pinned jev-1.13.0) | archive meta (patrol-ledger) (lane: first) | H |
| 8 | [github:mpuig/system-one](https://github.com/mpuig/system-one) | 09-22 15:15 / 09-23 06:39 | A | Open System One model + runtime; gold-label LoRA and a distilled adapter on small bases | train | uses — SOFT TARGETS (distilled adapter) | notes §165 | RC |
| 9 | [github:ljwwwiop/JEV-mini](https://github.com/ljwwwiop/JEV-mini) | 09-22 13:13 / 09-22 16:22 | A | Minimal Qwen3-0.6B decision-model training project (Kev-style) trained on a third-party distillation … | train | uses — LABELS via SargeDev v3 corpus | archive meta (refresh-ghd) | RC |
| 10 | [github:timbrinded/fly-lint](https://github.com/timbrinded/fly-lint) | 09-22 10:39 / 09-22 11:14 | A | PR review: hosted Jev signals feed a fixed FlyWire reservoir; a ridge readout is trained for four lint … | train | uses — FEATURES (labels ESLint) | archive meta (refresh-ghd) | RC |
| 11 | [hf:sshalimov04/open-jev-base](https://huggingface.co/sshalimov04/open-jev-base) | 09-22 07:38 / 09-22 07:39 | A | mmBERT-small (~140M) cross-encoder, BCE against teacher probability per option; pooled soft labels of 40 … | train | uses — SOFT LABELS (29 of 40 tasks Jev-labelled) | archive meta (refresh-hfd) (lane: first) | H |
| 12 | [github:aibengineering/minecraft-jev-distillation](https://github.com/aibengineering/minecraft-jev-distillation) | 09-22 03:56 / 09-22 14:59 | A | LightGBM Minecraft-combat policy trained to imitate Jev decisions, with interactive demo | train | uses — LABELS (imitation) | archive meta (refresh-ghd) | RC |
| 13 | [github:Bring-AI/jev-rl](https://github.com/Bring-AI/jev-rl) | 09-21 16:00 / 09-21 16:55 | A | JevRL: DQN agents on CartPole/MountainCar/Acrobot/FrozenLake trained with JEV-powered rewards | train | uses — RL REWARD | notes §145 | R |
| 14 | [github:slatinwine/jevy](https://github.com/slatinwine/jevy) | 09-21 11:32 / 09-23 02:31 | A | jevy: 118M EN+CN Jev-style typed-decision model distilled from official Jev (trains on 4GB GPU) | train | uses — SOFT TARGETS (KL) | notes §141 | RW |
| 15 | [github:AnthusAI/Jev-Flywheel](https://github.com/AnthusAI/Jev-Flywheel) | 09-20 23:30 / 09-23 00:25 | A | Jev plus a feedback-trained decision head; `make student` fine-tunes a local DistilBERT on the teacher's … | train | uses — FEATURES -> head, then LABELS for BERT student | notes §128 | RW |
| 16 | [hf:gopalanj/jevons-lfm25-1.2b-systemone](https://huggingface.co/gopalanj/jevons-lfm25-1.2b-systemone) | 09-20 15:45 / 09-20 15:45 | B | MLX QLoRA seed adapter on LFM2.5-1.2B-Instruct for the jevons local System One server; logits over … | train | uses — SEED LABELS (official-Jev aliases) | archive meta (refresh-hfd) (lane: first) | H |
| 17 | [github:mcftira/jev-route](https://github.com/mcftira/jev-route/blob/8e1e1d9a377d953d0cab4d4c64abe6de6d3aa5d1/docs/graduation.md) | 09-20 10:37 / 09-23 22:01 | A | 'Run it. Log it. Distill it. Own it.' Routing on Jev logs full distributions; export -> train … | train | uses — SOFT TARGETS (KL; productized log-to-student) | archive meta (refresh-ghd) | C |
| 18 | [github:Barneyjm/circuit](https://github.com/Barneyjm/circuit) | 09-19 14:50 / 09-23 20:22 | A | Open-weights System One models (circuit-1.7b/8b/vl-4b/audio-7b): LoRA + pointer readout head on Qwen3 … | train | uses — SOFT TARGETS (Jev+Gemini avg; README banner contradicts code) | archive meta (refresh-ghd) | RC |
| 19 | [github:lavallee/mk-jev-fly-brain](https://github.com/lavallee/mk-jev-fly-brain/blob/8217937e6e725b0ce3160c6e1ab0183db8b8aa30/scripts/train_local_policy.py) | 09-18 16:04 / 09-18 17:50 | B | 'Distil Jev into a local policy': softmax regression (168 weights) on logged per-move Jev probabilities … | train | uses — SOFT TARGETS | archive meta (refresh-jevusers) | C |
| 20 | [github:kanta13jp1/my_web_app](https://github.com/kanta13jp1/my_web_app/blob/34ff1b9669e18cbe1a7dc9e88cf903ccf3aabccd/scripts/jev_distillation/train.py) | 2025-10-17 / 09-23 22:41 | A | scripts/jev_distillation/: LightGBM regressors fit separately on Jev teacher probabilities and on a … | train | uses — TARGETS (Jev arm of Jev-vs-rule A/B) | **first-sighting** | C |
| 21 | [github:AnthusAI/Anth.us](https://github.com/AnthusAI/Anth.us/blob/bce5f665c6dc281cb120553053fdd19de8184963/scripts/generate-distilling-jev-into-a-classifier-charts.py) | 2023-11-01 / 09-23 20:56 | A | Charts for blog post 'Distilling an Aligned Jev System into a Classifier You Own': students trained on a … | train | uses — LABELS (hybrid Jev+Laya teacher; records off-repo) | **first-sighting** | C |

**P. ships a runnable Jev-teacher path (6)**

| # | ID | Created / pushed (UTC; 2026 unless shown) | Win | What | Rel. | Jev-output provenance | Prior (re-checked on origin/main d8dc848) | Lanes |
|---:|---|---|:-:|---|---|---|---|:-:|
| 22 | [github:omkarghugarkar007/system-one-model-finetuning](https://github.com/omkarghugarkar007/system-one-model-finetuning) | 09-23 05:55 / 09-23 06:13 | D | Measured fine-tuning recipe for Laya-class decision models, plus a teacher-distillation example | guide | uses — SOFT TARGETS, example 03 (measured arm used Jev) | archive meta (patrol-gfs) | RC |
| 23 | [github:bladedevoff/stuntd](https://github.com/bladedevoff/stuntd) | 09-23 00:46 / 09-23 17:05 | D | Local Jev/OpenAI-compatible proxy that records typed LLM decisions and distils them into a Laya head | train | uses — LABELS when upstream is Jev (proxy) | notes §165 | R |
| 24 | [github:Shalimov04/open-jev](https://github.com/Shalimov04/open-jev) | 09-20 09:22 / 09-22 15:06 | A | Distil-a-prompt pipeline: teacher labels -> ~140M mmBERT-small student (KL) -> calibration -> … | train | uses — SOFT TARGETS, optional backend=jev | notes §125,127,128,129 | R |
| 25 | [github:chukfinley/gavel](https://github.com/chukfinley/gavel) | 09-18 07:01 / 09-22 22:04 | A | gavel: decision model on public human-labelled data (MNLI, WANLI train, ANLI-R3, BoolQ...) | train | uses — SOFT TARGETS, label_with_jev.py (lane: no); shipped weights unverified | archive meta (refresh-ghd) | RC |
| 26 | [github:wfzyx/von](https://github.com/wfzyx/von) | 09-18 05:03 / 09-23 22:28 | A | Von: ModernBERT-Large (395M) non-autoregressive decision model, 250k class-balanced examples | train | uses — SOFT TARGETS, prepare_distill_dataset.py (SargeDev v3) (lane: unclear); shipped weights unverified | notes §49,60,99,123… | RC |
| 27 | [github:TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) | 09-17 16:08 / 09-21 09:58 | A | NanoJev: 0.6B parallel decision model (Maze/Snake/ViZDoom) with end-to-end training pipeline and … | train | uses — LABELS, shipped labeling scripts (gated in design doc) | notes §115,139,140 | RC |

**F. Jev selects/filters training rows (3)**

| # | ID | Created / pushed (UTC; 2026 unless shown) | Win | What | Rel. | Jev-output provenance | Prior (re-checked on origin/main d8dc848) | Lanes |
|---:|---|---|:-:|---|---|---|---|:-:|
| 28 | [github:RenaGao/jev-dataops](https://github.com/RenaGao/jev-dataops) | 09-21 02:15 / 09-23 14:08 | A | JEV-powered workbench: streaming data selection/quality evaluation -> automatic LoRA training -> … | data | uses — SELECTION FILTER (live mode) | sources/fp only | RW |
| 29 | [github:AkashPriyadarshii/jev-curate](https://github.com/AkashPriyadarshii/jev-curate) | 09-18 06:36 / 09-23 06:21 | A | Rust/Python high-throughput synthetic/pretraining dataset sifter using Jev Choice/Score/Noul judgments | data | uses — SELECTION FILTER | notes §134,163 | R |
| 30 | [hf:ds:adampippert/granite-decisions-synthetic](https://huggingface.co/datasets/adampippert/granite-decisions-synthetic) | 09-18 02:31 / 09-18 14:20 | B | MIT deterministic template fixtures for Granite decision fine-tunes; config weekend-it-business-v3 has … | data | uses — QUARANTINE FILTER + jev-audit outputs | **first-sighting** | H |

**C. published corpus of Jev output (4)**

| # | ID | Created / pushed (UTC; 2026 unless shown) | Win | What | Rel. | Jev-output provenance | Prior (re-checked on origin/main d8dc848) | Lanes |
|---:|---|---|:-:|---|---|---|---|:-:|
| 31 | [hf:ds:SargeDev/jev-distill-corpus-v3](https://huggingface.co/datasets/SargeDev/jev-distill-corpus-v3) | 09-21 13:50 / 09-21 14:10 | A | 740,957-row typed-decision corpus (System One schema) for training small local judges | data | uses — LABELS corpus (498,010/740,957 rows Jev 1.13) | notes §143 | RHC |
| 32 | [hf:ds:SargeDev/jev-distill-corpus](https://huggingface.co/datasets/SargeDev/jev-distill-corpus) | 09-21 03:30 / 09-21 04:25 | A | Query/passage relevance rows with Jev teacher judgments: graded 0-7 with a probability per grade. sha … | data | uses — LABELS corpus (graded Jev judgments) | notes §33,55,113; TR | W |
| 33 | [github:ctaxnagomi/dgui-hypermem](https://github.com/ctaxnagomi/dgui-hypermem) | 09-19 06:16 / 09-23 19:16 | A | Self-hosted memory MCP server on Cloudflare Workers with a JEV reasoning layer that logs decisions to an … | data | uses — CORPUS of logged Jev decisions | archive meta (refresh-jevusers) | R |
| 34 | [hf:ds:ctaxnagomi/DGUI_HYPERMEM-JEV](https://huggingface.co/datasets/ctaxnagomi/DGUI_HYPERMEM-JEV) | 09-19 05:45 / 09-23 23:17 | A | HF dataset that github:ctaxnagomi/dgui-hypermem (HEAD f5064a74) fills by logging every Jev decision as … | data | uses — CORPUS of logged Jev decisions | notes §69,111,127 | W |

**E. holds Jev outputs (eval) (5)**

| # | ID | Created / pushed (UTC; 2026 unless shown) | Win | What | Rel. | Jev-output provenance | Prior (re-checked on origin/main d8dc848) | Lanes |
|---:|---|---|:-:|---|---|---|---|:-:|
| 35 | [hf:space:Vineethsain/defenseclaw-system-one](https://huggingface.co/spaces/Vineethsain/defenseclaw-system-one) | 09-22 14:25 / 09-23 17:27 | A | Tool-call-safety board: small models incl. Jev 1.13.0 (hosted), OpenJev, nimble, jevify, open-jev-qwen … | eval | uses — hosted-Jev results (training forbidden by card) | **first-sighting** | H |
| 36 | [hf:ds:dylantom2012/open-system-one-bench](https://huggingface.co/datasets/dylantom2012/open-system-one-bench) | 09-21 08:45 / 09-21 15:56 | A | Per-example predictions for 10,000 classification/routing decisions from six stacks, including … | eval | uses — per-row Jev predictions | archive meta (hourly 2026-09-21T09) (lane: first) | H |
| 37 | [github:2nd1st/Jevsus](https://github.com/2nd1st/Jevsus) | 09-20 21:36 / 09-21 12:07 | A | Open dataset + runner: 3,539+ true/false statements put to jev-1.13.0 (about 210,000 calls), … | eval | uses — DATASET is Jev answers (eval) | archive meta (refresh-ghd) | R |
| 38 | [hf:ds:com-kotobalabs/typed-decisions-repo-governance](https://huggingface.co/datasets/com-kotobalabs/typed-decisions-repo-governance) | 09-19 08:27 / 09-19 08:30 | B | Seed (n=1) family of unresolved repo-governance findings run through typesafe/jev-1.13; gold is null and … | eval | uses — stored Jev predictions (null gold) | archive meta (hourly 2026-09-21T09) (lane: first) | H |
| 39 | [github:Jevals/jevals-data](https://github.com/Jevals/jevals-data) | 09-18 21:36 / 09-21 20:47 | A | Independent benchmark data: per-decision logs of Jev vs LLMs (accuracy, calibration, cost), CC-BY-4.0 | eval | uses — per-decision Jev logs (eval) | notes §49,153 | R |

**G. guide recommending it (4)**

| # | ID | Created / pushed (UTC; 2026 unless shown) | Win | What | Rel. | Jev-output provenance | Prior (re-checked on origin/main d8dc848) | Lanes |
|---:|---|---|:-:|---|---|---|---|:-:|
| 40 | [url:https://anth.us/blog/fine-tuning-jev/](https://anth.us/blog/fine-tuning-jev/) | 09-21 / 09-21 | A | Anthus blog 'Fine-Tuning Jev: You Can't' (2026-09-21): reweight a head fitted over Jev's answers; add … | guide | uses — advises head over Jev answers (FEATURES) | **first-sighting** | W |
| 41 | [url:https://www.seangoedecke.com/system-one-models-can-train-their-own-replacements/](https://www.seangoedecke.com/system-one-models-can-train-their-own-replacements/) | 09-20 / 09-20 | B | Sean Goedecke blog (2026-09-20): prompt a System One model, log inputs and outputs, train a … | guide | uses — advises distilling Jev logs (LABELS) | **first-sighting** | W |
| 42 | [url:https://jevaiguide.com/faq/can-you-fine-tune-jev/](https://jevaiguide.com/faq/can-you-fine-tune-jev/) | 09-19 / 09-19 | B | Unofficial FAQ (last checked 2026-09-19): Jev cannot be fine-tuned; use Jev probabilities as features … | guide | uses — advises Jev probabilities as FEATURES | **first-sighting** | W |
| 43 | [url:https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery.md](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery.md) | — / 09-24 00:05 | A | Official TypeSafe cookbook: an autoresearch loop proposes Score/Noul questions, Jev answers them for … | guide | uses — vendor cookbook: Jev answers as FEATURES for CatBoost | sources/fp only | W |

### 2b. Unclear provenance (101)

| # | ID | Created / pushed (UTC; 2026 unless shown) | Win | What | Rel. | Jev-output provenance | Prior (re-checked on origin/main d8dc848) | Lanes |
|---:|---|---|:-:|---|---|---|---|:-:|
| 44 | [github:Jwuthri/SelfJev](https://github.com/Jwuthri/SelfJev) | 09-23 19:38 / 09-23 19:38 | D | personal-jev: Qwen3-Reranker-0.6B frozen + 4.6M-param LoRA for instruction-conditioned classification | train | unclear | **first-sighting** | R |
| 45 | [github:divyanshudhruv/oev](https://github.com/divyanshudhruv/oev) | 09-23 17:36 / 09-23 21:11 | D | oev: 184M decision engine scoring every option in one 22 ms pass; per-benchmark fine-tunes | train | unclear | archive meta (patrol-gfs) | R |
| 46 | [hf:chaoliangUNSW/Jev-Style-Qwen3.5-2B-Decision-v2](https://huggingface.co/chaoliangUNSW/Jev-Style-Qwen3.5-2B-Decision-v2) | 09-23 16:16 / 09-23 22:16 | D | Jev-Style Qwen3.5-2B decision v2 (+GGUF/MLX); SHA moved after the §167 look (22:16Z); new sibling … | train | unclear | notes §167 | H |
| 47 | [github:0xSarnavo/laya-coding-router](https://github.com/0xSarnavo/laya-coding-router) | 09-23 14:43 / 09-23 14:48 | D | Laya fine-tuned to route coding-agent prompts (skills, tools, MCP servers, model, effort) | train | unclear | archive meta (patrol-gfs) | RC |
| 48 | [github:Manavarya09/verdict](https://github.com/Manavarya09/verdict) ▣ | 09-23 13:19 / 09-23 20:14 | D | Verdict: small decision models; zero-shot, fit heads on your labels in seconds, and a `distill` command … | train | unclear | archive meta (patrol-gfs) | RC |
| 49 | [github:tensor-goat/ModernBERT-systemone](https://github.com/tensor-goat/ModernBERT-systemone) | 09-23 12:40 / 09-23 12:40 | D | ModernBERT-systemone (22-byte README) | train | unclear | **first-sighting** | R |
| 50 | [github:xuxufei12/gui-verifier](https://github.com/xuxufei12/gui-verifier) | 09-23 10:55 / 09-23 11:17 | D | Screenshot-to-decision GUI verifier: Qwen3.5-0.8B decision LoRA, direct logits, JSON SFT baselines | train | unclear | **first-sighting** | R |
| 51 | [github:Readyaddy/open_system_one](https://github.com/Readyaddy/open_system_one) | 09-23 10:13 / 09-23 10:44 | D | Open System-1 (OpenJev): experiments creating a Jev-like System One model | train | unclear | archive meta (patrol-gfs) | R |
| 52 | [hf:space:luispoveda93/pcap-kev-triage](https://huggingface.co/spaces/luispoveda93/pcap-kev-triage) | 09-23 10:05 / 09-23 22:53 | D | sharky-0.5B, a Kev-style LoRA r16 + pointer head for pcap flow triage, trained on … | train | unclear | **first-sighting** | H |
| 53 | [github:tamnd/kime](https://github.com/tamnd/kime/blob/c8a9afa2eccc294b23442d6596b2d6fc07307649/spec/12-training.md) | 09-23 10:05 / 09-23 22:52 | D | Rust engine spec: teacher cross-encoders (ModernBERT-large / mmBERT) trained on public human-labeled … | train | unclear | notes §165 | C |
| 54 | [hf:abedinia/laya-web-agent](https://huggingface.co/abedinia/laya-web-agent) | 09-23 09:42 / 09-23 15:37 | D | Laya fine-tune picking the next browser step; 26,234 decisions from generated pages played in headless … | train | unclear | archive meta (patrol-ledger) (lane: first) | H |
| 55 | [hf:2nugu/laya-ko](https://huggingface.co/2nugu/laya-ko) | 09-23 08:02 / 09-23 08:52 | D | Korean Laya fine-tune with RLCD + soft CE on 102,665 KLUE/AI-Hub decisions + 6,000 English … | train | unclear | archive meta (patrol-ledger) (lane: first) | H |
| 56 | [github:shaunthebuilder/laya-snake-lab](https://github.com/shaunthebuilder/laya-snake-lab) | 09-23 07:59 / 09-23 08:01 | D | Local Laya MLX Snake with reproducible training, report and paper | train | unclear | archive meta (patrol-gfs) | R |
| 57 | [hf:lokinfey/Qwen3_5_0.8B_jev](https://huggingface.co/lokinfey/Qwen3_5_0.8B_jev) | 09-23 07:50 / 09-23 07:50 | D | Qwen3.5-0.8B fine-tune answering typed noul/choice/score questions, trained on … | train | unclear | archive meta (patrol-ledger) | W |
| 58 | [github:2nugu/laya-ko-decision-onnx](https://github.com/2nugu/laya-ko-decision-onnx) | 09-23 07:49 / 09-23 08:06 | D | Korean fine-tuned Laya decision model with PyTorch training pipeline and ONNX/Rust export | train | unclear | sources/fp only | R |
| 59 | [github:theolivenbaum/llm-shield](https://github.com/theolivenbaum/llm-shield/pull/1) | 09-23 07:15 / 09-23 10:07 | D | Merged PR #1 'Jevstral' in a fork of curiosity-ai/llm-shield: .NET CPU decider reading a Shieldstral 3B … | train | unclear (lane: no) | **first-sighting** | W |
| 60 | [github:Nomothings/Jetau](https://github.com/Nomothings/Jetau) | 09-23 05:49 / 09-23 10:01 | D | Jeτ: System One model for long-horizon decision-making (WebShop, Snake, Pokémon) vs NanoJev baselines | train | unclear | archive meta (patrol-gfs) | R |
| 61 | [github:anyforge/ruhui](https://github.com/anyforge/ruhui) ▣ | 09-23 02:53 / 09-23 10:00 | D | Ruhui: bilingual mmBERT-base Laya-architecture decision model; soft-label RLCD + soft distillation | train | unclear | archive meta (patrol-gfs) | R |
| 62 | [github:Liuziyu77/Valen](https://github.com/Liuziyu77/Valen) | 09-23 02:48 / 09-23 15:25 | D | Valen: train-it-yourself Jev-like multimodal model (Preview-0923) | train | unclear | notes §165 | R |
| 63 | [hf:asjson/jevson-4b-01](https://huggingface.co/asjson/jevson-4b-01) | 09-23 01:06 / 09-23 01:11 | D | Qwen3-4B LoRA + readout heads + fitted temperatures; JSON-Schema extraction mode plus System One … | train | unclear | archive meta (patrol-ledger) (lane: first) | H |
| 64 | [hf:flymy-ai/decision-fast-preview](https://huggingface.co/flymy-ai/decision-fast-preview) | 09-23 00:02 / 09-23 00:02 | D | Qwen3-0.6B-Base "headfirst" pointer-head checkpoint (v53), same packaging and provenance caveats as … | train | unclear | archive meta (patrol-ledger) (lane: first) | H |
| 65 | [hf:flymy-ai/decision-2b-preview](https://huggingface.co/flymy-ai/decision-2b-preview) | 09-23 00:01 / 09-23 00:02 | D | MiniCPM5-2B + LoRA + pointer head (frozen checkpoint v59, 26.2M trained params), Kev-derived trainer and … | train | unclear | archive meta (patrol-ledger) (lane: first) | H |
| 66 | [github:HeartY1ng/qwen-decision-lab](https://github.com/HeartY1ng/qwen-decision-lab) | 09-22 19:51 / 09-22 19:53 | A | Qwen2.5-0.5B frozen + shared candidate-scoring head trainer with Gradio/TensorBoard | train | unclear | archive meta (patrol-gfs) | R |
| 67 | [github:sshah03/shrewd](https://github.com/sshah03/shrewd) | 09-22 18:49 / 09-22 19:37 | A | shrewd: turn LLM judgments into a small fast local text model for one fixed task | train | unclear | archive meta (patrol-gfs) | R |
| 68 | [hf:tianxinwei/JevAny-27B-SFT](https://huggingface.co/tianxinwei/JevAny-27B-SFT) | 09-22 18:30 / 09-23 08:25 | A | Qwen3.8-27B rank-16 LoRA + pointer head on 107,278 records incl. native image/video evidence; sibling … | train | unclear | archive meta (patrol-ledger) (lane: first) | H |
| 69 | [github:weitianxin/JevAny](https://github.com/weitianxin/JevAny) | 09-22 18:28 / 09-23 18:21 | A | JevAny: two rank-16 LoRAs on Qwen3.8-27B (SFT, experimental RLCR), multimodal harness | train | unclear | notes §167 | R |
| 70 | [github:Ahtsham0715/ondevice-system1](https://github.com/Ahtsham0715/ondevice-system1) | 09-22 18:12 / 09-22 18:12 | A | OnDevice-System1: community on-device typed-decision family derived from Laya, with teacher/student … | train | unclear | archive meta (patrol-gfs) | R |
| 71 | [github:Artid1994/JEV_Concept-hermes-agent-router](https://github.com/Artid1994/JEV_Concept-hermes-agent-router) ▣ | 09-22 17:28 / 09-22 18:23 | A | Qwen2.5-1.5B-Instruct fine-tuned with Unsloth LoRA -> GGUF q4_k_m decision router for Hermes Agent | train | unclear | archive meta (patrol-gfs) | R |
| 72 | [github:bet0x/decision-jef](https://github.com/bet0x/decision-jef) ▣ | 09-22 16:03 / 09-23 20:58 | A | Decision-Jef-0.1 typed-decisions checkpoint with slot-bias/permutation analysis | train | unclear | archive meta (patrol-gfs) | R |
| 73 | [github:mourad-ghafiri/qwen3.5_0.8B_decision_model](https://github.com/mourad-ghafiri/qwen3.5_0.8B_decision_model) | 09-22 13:51 / 09-22 15:15 | A | Qwen3.5-0.8B decision model with soft labels; head-to-head vs jev-1.13.0 on unseen scenarios | train | unclear | archive meta (refresh-ghd) | R |
| 74 | [github:sshh12/nanojev](https://github.com/sshh12/nanojev) | 09-22 13:10 / 09-22 15:55 | A | nanojev: nanoGPT-style hypothetical reconstruction of Jev with /v1/systemone server | train | unclear | archive meta (patrol-gfs) | R |
| 75 | [github:vindahi/Medical-OpenJev](https://github.com/vindahi/Medical-OpenJev) | 09-22 12:59 / 09-23 06:20 | A | Medical-OpenJev: frozen backbone, heads trained with RLCD composite proper-scoring rewards | train | unclear | archive meta (refresh-ghd) | R |
| 76 | [github:Haswell119/jev-on-promise](https://github.com/Haswell119/jev-on-promise) | 09-22 12:28 / 09-23 19:24 | A | Sextant: local JEV reproduction with trained weights.json/calibration.json via scripts/train.sh | train | unclear | archive meta (refresh-ghd) | R |
| 77 | [github:JonathanHHenson/laya-multimodal](https://github.com/JonathanHHenson/laya-multimodal) | 09-22 12:23 / 09-22 13:07 | A | Experiment creating a multimodal version of Laya (JSONL training data with media paths) | train | unclear | **first-sighting** | R |
| 78 | [github:KNambiarDJsc/second-thought](https://github.com/KNambiarDJsc/second-thought) | 09-22 10:59 / 09-23 06:16 | A | Learning infrastructure: capture typed decisions, review the most uncertain, export a leak-free … | train | unclear | archive meta (refresh-ghd) | R |
| 79 | [hf:marcmagn1/kev-4b-typed-v1](https://huggingface.co/marcmagn1/kev-4b-typed-v1) | 09-22 10:57 / 09-22 12:23 | A | Kev recipe (LoRA r16, pointer head) trained on LocalLLaMA/typed-decisions annotator soft distributions + … | train | unclear | **first-sighting** | H |
| 80 | [github:Petofi-romance/Openjev-Med](https://github.com/Petofi-romance/Openjev-Med) | 09-22 09:10 / 09-22 14:19 | A | Openjev-Med: frozen ModernBERT + two pluggable heads trained with proper-scoring RL (student project) | train | unclear | **first-sighting** | R |
| 81 | [hf:jsaurabh/qwen3.5-9b-jev-data-mix-v2](https://huggingface.co/jsaurabh/qwen3.5-9b-jev-data-mix-v2) | 09-22 08:46 / 09-22 17:05 | A | Qwen3.5-9B LoRA: 2,676 Nimble rows + 764 synthetic gap rows + 382 hard replay; the curriculum was … | train | unclear | archive meta (refresh-hfd) (lane: first) | H |
| 82 | [github:AntonioGr7/Jeff](https://github.com/AntonioGr7/Jeff) | 09-22 07:34 / 09-23 10:50 | A | Jeff: local System One model inspired by Jev with permutation-disagreement diagnostics | train | unclear | archive meta (refresh-ghd) | R |
| 83 | [github:AISidesKicks/selectia](https://github.com/AISidesKicks/selectia) | 09-22 07:27 / 09-23 12:13 | A | Selectia: System One-style models fine-tuned from LFM 2.5 (1.2B); teacher_data + 695,795-example core … | train | unclear | archive meta (refresh-ghd) | RC |
| 84 | [github:asp616848/better-jev-for-all](https://github.com/asp616848/better-jev-for-all) | 09-22 06:25 / 09-23 20:26 | A | better-jev-for-all: Qwen3.5-4B + LoRA restricted-letter decoder arm (primary) vs encoder arm | train | unclear | archive meta (refresh-ghd) | RC |
| 85 | [github:HITsz-TMG/JevEmbed](https://github.com/HITsz-TMG/JevEmbed/blob/bf41f0daacaa088401dd4b9bfb4a545fdcd2c884/docs/training.md) | 09-22 05:57 / 09-23 10:03 | A | LoRA fine-tuning of embedding encoders for Choice/Score/Noul; data adapter pulls ZefanCai/Open-Jev … | train | unclear | archive meta (patrol-gfs) | C |
| 86 | [github:kortexa-ai/shingi](https://github.com/kortexa-ai/shingi) | 09-22 05:35 / 09-23 07:32 | A | Shingi: general-purpose decision models (choices, scores, probabilities in one pass) | train | unclear | archive meta (patrol-gfs) | R |
| 87 | [hf:cainai/OpenJev-Qwen3.5-0.8b](https://huggingface.co/cainai/OpenJev-Qwen3.5-0.8b) | 09-22 05:22 / 09-22 06:54 | A | Chinese full fine-tune of Qwen3.5-0.8B (3 epochs, 1,800 steps, no LoRA) with a shared decision head; … | train | unclear | **first-sighting** | H |
| 88 | [github:azalio/doomLaya](https://github.com/azalio/doomLaya) | 09-22 05:13 / 09-22 05:21 | A | Laya and Jev play FreeDoom; Laya adapted (v3) and published to HF | train | unclear | archive meta (refresh-ghd) | R |
| 89 | [github:Viratvishnu13/SystemOne-ONNX](https://github.com/Viratvishnu13/SystemOne-ONNX) | 09-22 03:58 / 09-22 04:14 | A | ~22M-param local decision model: confidence-weighted soft-label CE training, ONNX export, RLCD comparison | train | unclear | notes §163 | R |
| 90 | [hf:BarraHome/Decision-Jef-0.1](https://huggingface.co/BarraHome/Decision-Jef-0.1) | 09-21 21:42 / 09-23 20:59 | A | mmBERT-base decision encoder (heavy calibration and option-slot-bias analysis); part of the training … | train | unclear; same project as github:bet0x/decision-jef | archive meta (patrol-ledger) (lane: first) | H |
| 91 | [github:distil-labs/invoice-processing-pipeline](https://github.com/distil-labs/invoice-processing-pipeline) | 09-21 18:14 / 09-22 05:29 | A | AP pipeline: Jev for triage vs Qwen3.5-0.8B/4B fine-tuned on the distil labs platform (HF weights + GGUF) | train | unclear | archive meta (refresh-ghd) | RW |
| 92 | [github:malevrigns/agent-jev](https://github.com/malevrigns/agent-jev) | 09-21 16:24 / 09-23 09:16 | A | AgentJev-0.6B trained on LocalLLaMA/typed-decisions train split | train | unclear | notes §146,148,160 | R |
| 93 | [hf:llm-semantic-router/Decision-1.0-Lex-0.6B](https://huggingface.co/llm-semantic-router/Decision-1.0-Lex-0.6B) | 09-21 13:53 / 09-22 12:54 | A | New Decision-1.0 members: Kai-0.6B (on Vela-1.0-Encoder-307M), Lex-0.6B (specialist from Kai), Eos-0.8B … | train | unclear | **first-sighting** | H |
| 94 | [github:crownpku/FunctionGemma-Jev](https://github.com/crownpku/FunctionGemma-Jev) | 09-21 13:33 / 09-21 13:33 | A | FunctionGemma-270M with ToolRouterHead/ToolSafetyHead trained on Brier + soft-KL | train | unclear | **first-sighting** | R |
| 95 | [hf:alfred361/laya-multilingual-typed-decisions](https://huggingface.co/alfred361/laya-multilingual-typed-decisions) | 09-21 12:47 / 09-21 12:52 | A | laya-multilingual (mmBERT-base 322M) fine-tuned on LocalLLaMA/typed-decisions; one of about seven … | train | unclear | archive meta (hourly 2026-09-21T13) (lane: first) | H |
| 96 | [github:peterzhoufuliao/jev-like-transformer](https://github.com/peterzhoufuliao/jev-like-transformer) | 09-21 12:46 / 09-22 13:09 | A | Parallel decision model on shared state and dynamic candidate sets | train | unclear | archive meta (refresh-ghd) | R |
| 97 | [hf:apus-ailab/APUS-OpenJev-v1](https://huggingface.co/apus-ailab/APUS-OpenJev-v1) | 09-21 12:01 / 09-23 10:26 | A | Umbrella card for APUS-OpenJev 4B/9B/35B-A3B (Qwen3.5) decision runtime with effort=low/high early-exit … | train | unclear | archive meta (hourly 2026-09-21T13) (lane: first) | H |
| 98 | [github:KT19/looped-decision-ja](https://github.com/KT19/looped-decision-ja) | 09-21 11:43 / 09-21 11:57 | A | Japanese option-scoring decision model (JAX/Flax) with generic option head | train | unclear | archive meta (refresh-ghd) | R |
| 99 | [github:meijustory123/OpenJev-Kit](https://github.com/meijustory123/OpenJev-Kit) | 09-21 06:16 / 09-22 07:13 | A | OpenJev-Kit: open decision model reference implementation 'with the full training process public' | train | unclear | notes §139 | R |
| 100 | [github:MercatorProj/MyJev](https://github.com/MercatorProj/MyJev) | 09-21 03:12 / 09-21 07:18 | A | MyJev: adapt language models to Jev-style structured questions | train | unclear | archive meta (hourly 2026-09-21T08) | R |
| 101 | [github:metask-ai/metask-jev](https://github.com/metask-ai/metask-jev) | 09-21 02:34 / 09-22 14:54 | A | Metask-Jev: candidate-logit Jev-class models (metask-jev-4b on HF 'policy-mix') | train | unclear | notes §132,133,134,142 | R |
| 102 | [github:ajaman190/lumen](https://github.com/ajaman190/lumen) | 09-21 00:18 / 09-21 03:19 | A | Lumen: Qwen3.5 mixture-of-LoRA decision model; focal PSR + symmetric KL + ordinal + optional teacher … | train | unclear | notes §133 | R |
| 103 | [github:kyegomez/open-jev](https://github.com/kyegomez/open-jev) | 09-21 00:13 / 09-21 01:47 | A | Open Jev: from-first-principles PyTorch reconstruction (RLCDLoss: soft NLL, Brier, consistency, ECE … | train | unclear | notes §125,128,129,131 | R |
| 104 | [github:Zefan-Cai/Open-Jev](https://github.com/Zefan-Cai/Open-Jev) | 09-20 20:12 / 09-23 09:27 | A | Open-Jev 2B/9B/27B-v1.1: rank-8 LoRA + scalar per-candidate head on Qwen bases; community-hard training … | train | unclear | notes §125,127,128,129…; TR | R |
| 105 | [github:isHeSatoshi/smalljev](https://github.com/isHeSatoshi/smalljev) | 09-20 17:50 / 09-21 08:51 | A | smalljev v9: MiniCPM5-2B-Base + LoRA adapter + heads ('a few thousand decision examples') | train | unclear | archive meta (hourly 2026-09-20T18) | R |
| 106 | [github:S1LV3RJ1NX/openjev](https://github.com/S1LV3RJ1NX/openjev) | 09-20 15:08 / 09-23 17:36 | A | OpenJev: open System One models trainable on your own data; 279-task, 323,466-row training mixture on HF | train | unclear | notes §119 | R |
| 107 | [github:iapp-technology/openthai-systemone](https://github.com/iapp-technology/openthai-systemone) | 09-20 14:42 / 09-21 17:22 | A | OpenThai-SystemOne: Qwen3.5-0.8B text tower with 256-way slot head; CPT -> SFT -> calibration on 1xH100 | train | unclear | archive meta (refresh-ghd) | R |
| 108 | [github:azerothl/akasha-model](https://github.com/azerothl/akasha-model) | 09-20 08:35 / 09-22 20:17 | A | Akasha: one-pass choice model with option-attention head (text + image patches), trained encoder | train | unclear | **first-sighting** | R |
| 109 | [github:FogMoe/necro](https://github.com/FogMoe/necro) | 09-20 06:39 / 09-21 03:08 | A | Abandoned Qwen3.5-0.8B LoRA fine-tuning experiments for Jev-like typed judgments, with datasets, … | train | unclear | notes §134 | R |
| 110 | [github:Ruivalim/exu-base](https://github.com/Ruivalim/exu-base) | 09-20 05:46 / 09-22 17:57 | A | Exu: train encoder-only decision models with proper-scoring-rule RLCD; soft targets from annotators or a … | train | unclear | notes §106 | R |
| 111 | [github:AltSlate-Labs/certo](https://github.com/AltSlate-Labs/certo) | 09-20 05:42 / 09-21 17:20 | A | certo: toolkit for narrow calibrated decision models; separates exact-world soft targets, gold labels … | train | unclear | notes §136,137 | R |
| 112 | [github:PIXELZX0/XERON](https://github.com/PIXELZX0/XERON) | 09-20 01:03 / 09-23 23:40 | A | XERON: fine-tuned Laya models (English track on LocalLLaMA/typed-decisions; Korean + browser tracks) | train | unclear | notes §102,109 | R |
| 113 | [github:intikhab49/open-jev-typed-decision-engine](https://github.com/intikhab49/open-jev-typed-decision-engine) | 09-19 14:26 / 09-21 16:05 | A | 150M encoder typed-decision engine trained on LocalLLaMA/typed-decisions soft distributions; Colab T4 … | train | unclear | archive meta (refresh-jevusers) | RW |
| 114 | [hf:dwidlee/systemone-lite-0.5b](https://huggingface.co/dwidlee/systemone-lite-0.5b) | 09-19 08:28 / 09-22 15:48 | A | Qwen2.5-0.5B-Instruct option-restricted next-token scorer trained on ds dwidlee/systemone-lite-phase2 … | train | unclear | archive meta (patrol-ledger) (lane: first) | H |
| 115 | [github:zeredy879/minojev](https://github.com/zeredy879/minojev) | 09-18 06:25 / 09-21 16:43 | A | minojev: typed distributions read from cached hidden states; small head trained with distribution losses | train | unclear | archive meta (refresh-jevusers) | R |
| 116 | [hf:convaiinnovations/laya](https://huggingface.co/convaiinnovations/laya) | 09-18 05:05 / 09-23 18:09 | A | Laya ModernBERT-large 421M / mmBERT 322M RLCD decision head; modified 2026-09-23. This window: about 60 … | train | unclear | notes §18,42,46,48…; TR | H |
| 117 | [github:NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 09-18 04:46 / 09-23 18:05 | A | Laya: ModernBERT/mmBERT encoder + RLCD-trained decision head (English, multilingual, typed-decisions … | train | unclear | notes §76,77,78,79…; TR | R |
| 118 | [github:steph4n-gh/system1](https://github.com/steph4n-gh/system1/blob/68ed82af5aa22b110b33a2fc1ebe2b1b309adb00/README.md) | 09-18 01:20 / 09-22 14:48 | A | 'Teach bounded decision skills from examples or observed APIs': teacher callback (colleague, rules, … | train | unclear | **first-sighting** | C |
| 119 | [github:anthony-maio/eve-rlcd](https://github.com/anthony-maio/eve-rlcd) | 09-18 00:24 / 09-21 02:20 | A | eve-rlcd: Qwen3-0.6B decision model trained with RLCD bandit REINFORCE (Brier-derived reward), with RLVR … | train | unclear | notes §110 | R |
| 120 | [hf:heman10x/rlcd-modernbert-151m](https://huggingface.co/heman10x/rlcd-modernbert-151m) | 09-17 16:25 / 09-20 14:35 | B | Hub weights for OpenJev Verdict: GLiClass-modern-base (151M) trained with CE + 1.0 x Brier, then L-BFGS … | train | unclear | **first-sighting** | W |
| 121 | [github:ziyacivan/s1decide](https://github.com/ziyacivan/s1decide) | 09-17 09:17 / 09-23 23:49 | A | s1decide: open decision model with published calibration and negative controls; Qwen3.8-27B 4-bit … | train | unclear | archive meta (refresh-ghd) | R |
| 122 | [github:rhizomatous/qwenrlcd](https://github.com/rhizomatous/qwenrlcd) | 09-17 01:49 / 09-23 15:28 | A | qwenrlcd: Qwen RLCD with soft targets, tree-attention isolation and deterministic fixtures | train | unclear | archive meta (patrol-gfs) | R |
| 123 | [github:shubhamjoshipromail-svg/opspilot-ai](https://github.com/shubhamjoshipromail-svg/opspilot-ai) | 05-04 01:33 / 09-22 19:50 | A | OpsPilot: fine-tuned ModernBERT support-ticket router, 74.0% held-out (redesigned taxonomy) vs Jev 0.5458 | train | unclear | archive meta (patrol-gfs) | R |
| 124 | [github:earlyaidopters/away-together-starter](https://github.com/earlyaidopters/away-together-starter) | 09-23 20:52 / 09-23 21:08 | D | Build your own Jev-style specialist: visual guide + small training recipe (travel demo) | guide | unclear | sources/fp only | R |
| 125 | [github:fabiobraganet/laya-dataset-manager](https://github.com/fabiobraganet/laya-dataset-manager) | 09-23 14:18 / 09-23 14:53 | D | Laya dataset management and training support (Docker/WSL2) | data | unclear | **first-sighting** | R |
| 126 | [hf:ds:AIMultiple/aimultiple-decision-models-browser](https://huggingface.co/datasets/AIMultiple/aimultiple-decision-models-browser) | 09-23 09:20 / 09-23 09:20 | D | 10 of 50 browser tasks comparing Jev 1.13, Kev-9B, Laya typed-decisions, Gemini 3.8 Flash, GPT-6 Astra; … | eval | unclear | **first-sighting** | H |
| 127 | [hf:ds:JonesLin/next-jev-stage2-merged-verified-20260923](https://huggingface.co/datasets/JonesLin/next-jev-stage2-merged-verified-20260923) | 09-23 06:10 / 09-23 09:35 | D | 414,839 verified NLI/VQA-as-entailment records (378,903 train) with teacher_rationale targets and gold … | data | unclear | archive meta (patrol-ledger) (lane: first) | H |
| 128 | [github:manishhnnegi/laya-decision-engine-tutorial](https://github.com/manishhnnegi/laya-decision-engine-tutorial) | 09-23 04:45 / 09-23 06:03 | D | Hands-on Laya multilingual decision-engine tutorial (RLCD-trained model) | guide | unclear | archive meta (patrol-gfs) | R |
| 129 | [github:tehtommeh/laya-finetuning](https://github.com/tehtommeh/laya-finetuning) | 09-23 04:06 / 09-23 21:14 | D | Laya local fine-tuning kit: JSONL state/gold, DATA_PREP for exports, votes or LLM-teacher labels | guide | unclear | archive meta (patrol-gfs) | R |
| 130 | [github:hyprstream/hyprstream-synthesis](https://github.com/hyprstream/hyprstream-synthesis) | 09-23 01:55 / 09-23 19:10 | D | Teacher-agnostic synthetic corpus pipeline for System One training (procedural question specs, pluggable … | data | unclear | archive meta (patrol-gfs) | R |
| 131 | [hf:ds:limberc/this-that-complex-decisions](https://huggingface.co/datasets/limberc/this-that-complex-decisions) | 09-22 17:01 / 09-22 18:22 | A | 1,710 policy-applied-to-state decisions; LLM baselines (claude-opus-5 0.834, gpt-5.6 0.816, glm-5.3 … | eval | unclear | **first-sighting** | H |
| 132 | [github:daemonchen/jev-system-one-tutorial](https://github.com/daemonchen/jev-system-one-tutorial) | 09-22 15:39 / 09-22 16:34 | A | Chinese tutorial: hand-build a jevlike ticket-triage system from scratch | guide | unclear | archive meta (patrol-gfs) | R |
| 133 | [hf:ds:telepatia-ai/typed-decisions-pt-es](https://huggingface.co/datasets/telepatia-ai/typed-decisions-pt-es) | 09-22 14:42 / 09-22 14:49 | A | Unofficial pt-BR/es translations of LocalLLaMA/typed-decisions with pinned source and translator … | data | unclear | **first-sighting** | H |
| 134 | [github:XFlexDev/kev-corpus](https://github.com/XFlexDev/kev-corpus) | 09-22 13:34 / 09-22 13:59 | A | KEV decision-model training corpus (463K MCQ samples) for a Qwen2.5-0.5B discriminative model | data | unclear | archive meta (refresh-ghd) | R |
| 135 | [github:manojlds/classifier-bench](https://github.com/manojlds/classifier-bench) | 09-22 12:44 / 09-23 10:09 | A | Benchmark of TF-IDF, MiniLM linear head, DSPy and Jev on BANKING77 | eval | unclear | archive meta (refresh-ghd) | R |
| 136 | [hf:ds:tasksource/tasksource-jev-typed-decisions](https://huggingface.co/datasets/tasksource/tasksource-jev-typed-decisions) | 09-22 09:02 / 09-23 22:30 | A | tasksource typed-decision mixture (571 upstream sources) with a "Jev-native" share; modified again … | data | unclear | notes §167,168; TR | H |
| 137 | [hf:ds:mkzero/agent-decision-30k](https://huggingface.co/datasets/mkzero/agent-decision-30k) | 09-22 08:30 / 09-22 08:32 | A | 30,456 operational decisions (browser DOM, API dispatch, e-commerce brand/specs/category, legal clause) … | data | unclear | **first-sighting** | H |
| 138 | [hf:ds:annelo/laya-marker-corpus](https://huggingface.co/datasets/annelo/laya-marker-corpus) | 09-22 08:19 / 09-22 08:27 | A | 95,817 rows over 368 tasks (choice/noul/multi) for training an instruction-reading typed-decision head; … | data | unclear | **first-sighting** | H |
| 139 | [github:cexll/train-your-first-jev](https://github.com/cexll/train-your-first-jev) | 09-21 03:19 / 09-21 03:53 | A | Chinese interactive course: train your own Jev-style decision model (Qwen LoRA on Mac) | guide | unclear | notes §133 | R |
| 140 | [hf:ds:Hanno-Labs/decision-bench](https://huggingface.co/datasets/Hanno-Labs/decision-bench) | 09-20 18:54 / 09-23 21:04 | A | DecisionBench typed-decision benchmark (Noul/Choice/Score) with reviewed results dataset and a Docker … | eval | unclear | archive meta (patrol-gfs) (lane: first) | H |
| 141 | [github:WiredMind2/jev](https://github.com/WiredMind2/jev) | 09-20 00:59 / 09-22 02:27 | A | Independent research notes toward an open Jev-like model: API contract, datasets catalog, frozen-head … | guide | unclear | archive meta (refresh-ghd) | R |
| 142 | [hf:ds:LocalLLaMA/typed-decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) | 09-16 07:42 / 09-22 11:57 | A | Typed-decisions benchmark/training set (4 workflows; gold = mean of 3 teacher samples) | data | unclear | notes §42,71,87,102… | RH |
| 143 | [github:whilehq/whileai-sdk](https://github.com/whilehq/whileai-sdk/blob/4edde3ef3d302f89fd04ec12cc6153f4ada49a40/skills/whileai-simulations/SKILL.md) | 08-16 19:38 / 09-23 23:34 | A | Agent skill for SFT/GRPO/DPO post-training with evals, simulations, judge validation vs people; accepts … | guide | unclear | **first-sighting** | C |
| 144 | [github:sileod/tasksource](https://github.com/sileod/tasksource) | 2022-12-06 / 09-23 21:36 | A | tasksource: dataset collection/preprocessing framework for extreme multitask NLP | data | unclear | **first-sighting** | R |

### 2c. No Jev outputs (154)

| # | ID | Created / pushed (UTC; 2026 unless shown) | Win | What | Rel. | Jev-output provenance | Prior (re-checked on origin/main d8dc848) | Lanes |
|---:|---|---|:-:|---|---|---|---|:-:|
| 145 | [github:caiovicentino/eikos](https://github.com/caiovicentino/eikos) | 09-23 23:48 / 09-24 00:04 | D | Eikos: open single-pass typed-decision models (4B & 27B) for finance/trading; data on HF … | train | no | **first-sighting** | R |
| 146 | [github:janmejai2002/gutcheck](https://github.com/janmejai2002/gutcheck) | 09-23 22:44 / 09-23 22:46 | D | gutcheck: OpenVINO Laya runtime (Intel NPU/GPU, parity-tested) plus a 25-minute laptop fine-tune path | train | no (lane: unclear) | **first-sighting** | RC |
| 147 | [github:danil31219as/jev-as-a-judge](https://github.com/danil31219as/jev-as-a-judge) | 09-23 21:46 / 09-23 23:53 | D | Score-scale judge on Qwen/Halo: soft-target CE on POLLUX annotation vote distributions (+ optional Laya … | train | no | **first-sighting** | R |
| 148 | [github:devjothish/laya-forge](https://github.com/devjothish/laya-forge) | 09-23 18:40 / 09-23 20:59 | D | laya-forge: fine-tune, calibrate and gate Laya on your own decisions; CI regenerates data | train | no | notes §168 | R |
| 149 | [github:togethercomputer/tev1](https://github.com/togethercomputer/tev1) | 09-23 17:39 / 09-23 23:01 | D | tev1-4B-experimental: LoRA SFT of Qwen3.5-4B on Together AI, 37,840 examples, Qwen LM-head readout | train | no | **first-sighting** | RCW |
| 150 | [github:MoLeMo-Lab/mojev](https://github.com/MoLeMo-Lab/mojev) ▣ | 09-23 16:02 / 09-23 21:16 | D | MoJev: typed calibrated decisions in one forward pass; /v1/systemone server | train | no (lane: unclear); Open-Jev generator revision unpinned | **first-sighting** | R |
| 151 | [hf:OwaisAli10/laya-snake](https://huggingface.co/OwaisAli10/laya-snake) | 09-23 14:44 / 09-23 14:47 | D | laya-multilingual fine-tuned to play Snake from a BFS teacher: soft targets 0.85 on the teacher move, … | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 152 | [github:Okbatti/SnakeGame_Laya](https://github.com/Okbatti/SnakeGame_Laya) | 09-23 14:35 / 09-23 14:48 | D | Snake where each move is decided by a fine-tuned copy of Laya | train | no | archive meta (patrol-gfs) | RC |
| 153 | [hf:xuhaodev/Qwen3-1.7B-Jev](https://huggingface.co/xuhaodev/Qwen3-1.7B-Jev) | 09-23 13:34 / 09-23 13:34 | D | Qwen3-1.7B LoRA; 3,600 synthetic contrasts + 2,000 historical replay questions with targets derived from … | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 154 | [hf:XAILab-CyberSpark/OAK-Decision-parallel-decision-qwen3.5-0.8b](https://huggingface.co/XAILab-CyberSpark/OAK-Decision-parallel-decision-qwen3.5-0.8b) | 09-23 13:23 / 09-23 14:50 | D | Shared state prefix with isolated question branches and a 256-d pointer head on Qwen3.5-0.8B LoRA; … | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 155 | [github:greyaperez/openjeff](https://github.com/greyaperez/openjeff) | 09-23 11:50 / 09-23 12:50 | D | OpenJeff: self-hosted judgments with a trained Gemma adapter; candidate-order disagreement 22.00% -> … | train | no | archive meta (patrol-gfs) | R |
| 156 | [github:nagisanzenin/nagi](https://github.com/nagisanzenin/nagi) ▣ | 09-23 11:43 / 09-23 18:56 | D | Nagi: Smol 421M (ModernBERT-large dual encoder + option tower) and Big 4B (Qwen3.5-4B mixed-rank LoRA … | train | no (lane: unclear); documented lineage only: v0 soft-distilled from DeepSeek+GPT-5.6-Luna, G-clean data private | archive meta (patrol-gfs) | RC |
| 157 | [github:NasirSultan/CalibRoute-Calibrated-Intent-Router](https://github.com/NasirSultan/CalibRoute-Calibrated-Intent-Router) | 09-23 10:40 / 09-23 11:02 | D | CalibRoute: ModernBERT on CLINC150 + typo/short-query augmentation; template data taught shortcuts | train | no | archive meta (patrol-gfs) | R |
| 158 | [github:chemany/jeva](https://github.com/chemany/jeva) | 09-23 09:59 / 09-23 18:30 | D | jeva: 2B browser-agent decision model you can train and run yourself | train | no | archive meta (patrol-gfs) | RC |
| 159 | [github:Priyanshu-5257/laya-medical-finetune](https://github.com/Priyanshu-5257/laya-medical-finetune) | 09-23 09:39 / 09-23 12:11 | D | Laya medical RLCD fine-tune (smoke + torchrun DDP on Kaggle T4x2) | train | no | **first-sighting** | RC |
| 160 | [github:uzuw/laya-cli-gate](https://github.com/uzuw/laya-cli-gate) | 09-23 07:49 / 09-23 12:33 | D | Head-only fine-tune of convaiinnovations/laya as a pre-execution safety gate + tool router for terminal … | train | no (lane: unclear) | archive meta (patrol-ledger) | RC |
| 161 | [hf:guanxuyu/visual-jev-4b-answer-sft](https://huggingface.co/guanxuyu/visual-jev-4b-answer-sft) | 09-23 07:29 / 09-23 22:05 | D | Qwen3-VL-4B-Instruct LoRA (language tower r16) for forced-choice visual answers; records derived from … | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 162 | [github:bandr-ai/bandits](https://github.com/bandr-ai/bandits/issues/73) | 09-23 07:25 / 09-23 14:35 | D | Tracking issue #73 'Decision Models: train your own Jev-style model in Bandits' + plan/learnings docs on … | train | no | **first-sighting** | W |
| 163 | [github:wdlctc/jev-recommend](https://github.com/wdlctc/jev-recommend) | 09-23 06:53 / 09-23 15:23 | D | Jev-style typed decision recommenders: pointwise vs isolated-mask vs listwise LoRA scoring on MovieLens | train | no | archive meta (patrol-gfs) | R |
| 164 | [github:zty2004/jev-xiangqi-lab](https://github.com/zty2004/jev-xiangqi-lab) | 09-23 06:14 / 09-23 13:53 | D | Self-trained Xiangqi CNN decision model: legal-move probabilities, temperature on calibration split | train | no | archive meta (patrol-gfs) | RC |
| 165 | [github:agentculture/nvsh](https://github.com/agentculture/nvsh/issues/51) | 09-23 05:56 / 09-23 22:13 | D | Issues #46 (two-track 'Tool-Jev' fine-tune of Qwen3.5-0.8B on DGX Sparks, 2026-09-23T05:56Z) and #51 … | train | no | **first-sighting** | W |
| 166 | [hf:tindang/laya-code](https://huggingface.co/tindang/laya-code) | 09-23 05:48 / 09-23 05:49 | D | Laya code-relevance re-ranker for Claude Code context selection; weak supervision from git history, … | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 167 | [hf:mazenDDr/laya-crisis-triage](https://huggingface.co/mazenDDr/laya-crisis-triage) | 09-23 04:32 / 09-23 11:38 | D | Laya fine-tune for disaster-message triage on HumAID and CrisisBench (CC BY-NC-SA) vs e5+LR baselines. | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 168 | [hf:altslate/certo-decision-v2.2](https://huggingface.co/altslate/certo-decision-v2.2) | 09-23 03:55 / 09-23 03:55 | D | Ettin-encoder-1B generic decision model trained on real gold + synthetic worlds with exact known … | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 169 | [hf:Quantum08/laya-browser-mind2web](https://huggingface.co/Quantum08/laya-browser-mind2web) | 09-23 03:04 / 09-23 03:07 | D | Laya (421M) fine-tuned on Mind2Web target-element choice; labels from DOM attributes; ~33 min. | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 170 | [github:DejaAI2/JevNext](https://github.com/DejaAI2/JevNext) ▣ | 09-23 02:55 / 09-23 03:00 | D | JevNext: Qwen3-0.6B + rank-16 LoRA decision mode fused with an OpenAI-compatible generation server | train | no (lane: unclear); seeded rule generator (MiniJev) | archive meta (patrol-gfs) | RC |
| 171 | [github:clawdreyhepburn/identity-jev](https://github.com/clawdreyhepburn/identity-jev) | 09-23 01:41 / 09-23 02:21 | D | Fine-tuned Laya for identity-standards retrieval: zero-shot 40% -> 87% (Mac mini M4 Pro, ~25 min) | train | no | archive meta (patrol-gfs) | RC |
| 172 | [github:robbalian/rev](https://github.com/robbalian/rev/blob/7ee8732aad2b21a5c304e76b108cf831943fb877/train/train.py) | 09-22 22:43 / 09-23 16:10 | A | Pointer heads on Qwen3.5-4B/9B and Qwen3.8-27B over 19,792 public decisions (RACE, CosmosQA, MultiRC, … | train | no | archive meta (patrol-gfs) | C |
| 173 | [hf:vigneshlabs/ballot-jev-0.5b](https://huggingface.co/vigneshlabs/ballot-jev-0.5b) | 09-22 20:44 / 09-22 21:52 | A | Qwen2.5-0.5B LoRA r16 with a permutation-invariant readout (0/32 option-order flips by construction); … | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 174 | [github:javimosch/mtlm-router](https://github.com/javimosch/mtlm-router) ▣ | 09-22 19:57 / 09-22 22:15 | A | 7M-param typed decision layer in pure MFL (routing, calibration, abstention); model on HF | train | no (lane: unclear); noul/score head labels unpublished | archive meta (patrol-gfs) | R |
| 175 | [github:michaljach/jet](https://github.com/michaljach/jet) | 09-22 19:34 / 09-23 19:33 | A | jet: train and serve a small typed calibrated decision model on Apple Silicon (Qwen3-0.6B) | train | no | sources/fp only | R |
| 176 | [hf:bdauzats/minicpm5-2b-decision](https://huggingface.co/bdauzats/minicpm5-2b-decision) | 09-22 19:04 / 09-22 19:29 | A | MiniCPM5-2B merged LoRA r16 + pointer head from scratch; Kev decision-v7 (12,576) + 2,800 public rows … | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 177 | [github:biplovgautam/LayaStudio](https://github.com/biplovgautam/LayaStudio/blob/acf9c10820906e9be48c9f1dab667cb00cfce4b5/README.md) | 09-22 18:59 / 09-22 21:42 | A | Mac/MLX studio to fine-tune Laya on your own data and 'prove the result is better': token-budget check, … | train | no | archive meta (patrol-gfs) | C |
| 178 | [hf:InfinimindCreations/laya-news-decisions](https://huggingface.co/InfinimindCreations/laya-news-decisions) | 09-22 18:35 / 09-22 18:35 | A | Laya multilingual full fine-tune on ~92,000 2026 news articles labelled on full text by DeepSeek v4.1 … | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 179 | [github:arbazsiddiqui/kev-browser-use](https://github.com/arbazsiddiqui/kev-browser-use) | 09-22 18:19 / 09-23 16:50 | A | 0.6B Kev fine-tune for browser use (32.2% Mind2Web step success, WebGPU) | train | no | notes §167 | R |
| 180 | [hf:arbazsiddiqui/kev-0.6b-browser-use](https://huggingface.co/arbazsiddiqui/kev-0.6b-browser-use) | 09-22 18:16 / 09-23 10:42 | A | Fine-tune of Kev-0.6B (Qwen3-0.6B LoRA + pointer head) for browser element/operation choice; 32.2% step … | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 181 | [github:mrmps/hotdog](https://github.com/mrmps/hotdog) ▣ | 09-22 17:54 / 09-22 19:13 | A | hotdog-27B: Qwen3.8-27B dense binary classifier, rank-16 LoRA trained with Tinker; paired Jev benchmark | train | no (lane: unclear); OpenAI gpt-4.1-mini generator+auditor filter; sealed Jev dev preds loaded during selection | archive meta (patrol-gfs) | RC |
| 182 | [github:adimyth/compass](https://github.com/adimyth/compass) ▣ | 09-22 17:10 / 09-23 12:47 | A | Compass 0.2.0: Qwen3.5-4B + rank-16 LoRA trained through direct/verify readouts (listwise CE), … | train | no (lane: unclear); 270 train rows + shadow suite drafted by hosted Claude, terms Unknown | archive meta (patrol-gfs) | R |
| 183 | [hf:ait-hf/certus-jev-like-v0007](https://huggingface.co/ait-hf/certus-jev-like-v0007) | 09-22 15:57 / 09-23 09:24 | A | Qwen2.5-1.5B family: trunk LoRA r16 on 61 public datasets (<=3k each) with NLL + Brier, yes/no balancing … | train | no | archive meta (patrol-ledger) (lane: first) | H |
| 184 | [github:allebee/jevk5](https://github.com/allebee/jevk5) | 09-22 14:58 / 09-23 19:06 | A | JevK5: Qwen3.5-4B + distilled LoRA (Apache-2.0); SemIf option-letter readout | train | no | notes §165,167,168; TR | R |
| 185 | [github:10086ggqq/laya-t-rex-runner](https://github.com/10086ggqq/laya-t-rex-runner) | 09-22 14:52 / 09-22 14:54 | A | 7.5k-param System 1 T-Rex runner policy in Laya typed-decision style, distilled from a rollout planner … | train | no | **first-sighting** | R |
| 186 | [hf:shreyanbr/nev-lite-systemone](https://huggingface.co/shreyanbr/nev-lite-systemone) | 09-22 13:47 / 09-22 15:29 | A | Static no-attention model2vec decision head (from all-MiniLM-L6-v2) trained on eight public benchmarks' … | train | no | **first-sighting** | H |
| 187 | [hf:harikarthikmanyam/laya-issue-triage](https://huggingface.co/harikarthikmanyam/laya-issue-triage) | 09-22 13:46 / 09-22 13:57 | A | Laya fine-tune for GitHub issue triage; labels from the maintainers who triaged each issue, "not from a … | train | no | **first-sighting** | H |
| 188 | [hf:AnkitAI/tinyjev-0.6b](https://huggingface.co/AnkitAI/tinyjev-0.6b) | 09-22 13:15 / 09-23 10:43 | A | Qwen3-0.6B-Base + pointer head; LoRA r16 lr 5e-5, merged; T=1.46; trained on jaredpalmer/kev-suites … | train | no | **first-sighting** | W |
| 189 | [hf:mghafiri/qwen3.5-0.8B-decision-model](https://huggingface.co/mghafiri/qwen3.5-0.8B-decision-model) | 09-22 12:57 / 09-22 15:14 | A | Qwen3.5-0.8B-Base trained on a MacBook Pro M2 Max using ds mghafiri/decision-model-scenarios (2,000 … | train | no | **first-sighting** | H |
| 190 | [github:ankit-aglawe/tinyjev](https://github.com/ankit-aglawe/tinyjev) | 09-22 12:49 / 09-22 21:12 | A | TinyJev 0.6B on Qwen3-0.6B-Base with Kev's pointer head and training data; MLX/PyTorch | train | no | archive meta (refresh-ghd) | R |
| 191 | [hf:lewisdog/aoa-course-decision-0.6b](https://huggingface.co/lewisdog/aoa-course-decision-0.6b) | 09-22 12:38 / 09-22 13:59 | A | Kev LoRA/pointer head on Qwen3-0.6B for a course planner; hand-written + gpt-oss:20b paraphrases, … | train | no | **first-sighting** | H |
| 192 | [github:Worthify-AI/worthify-open-jev](https://github.com/Worthify-AI/worthify-open-jev/blob/715ecd820e6743687f5459af3786d6ff0653cc76/THIRD_PARTY_WORTHIFY.md) | 09-22 11:16 / 09-22 16:01 | A | Gemma 4 option-logit LoRA recipes on attributed CLINC150/WANLI; 'Company records and Jev-generated … | train | no | archive meta (refresh-ghd) | C |
| 193 | [github:aryanthegamedev3465-collab/Fragment](https://github.com/aryanthegamedev3465-collab/Fragment) | 09-22 11:13 / 09-22 22:26 | A | Fragment-1: tiny typed-decision model trained from scratch on a 2-thread CPU (SST-2, BoolQ, AG News, … | train | no | archive meta (refresh-ghd) | R |
| 194 | [hf:guzus/jev-nyotti](https://huggingface.co/guzus/jev-nyotti) | 09-22 09:46 / 09-22 10:25 | A | Qwen3.5-4B LoRA imitating user-supplied historical BTC execution records attributed to one trader (4,096 … | train | no | archive meta (refresh-ghd) (lane: first) | H |
| 195 | [hf:IJyad/jeb-typed-decisions](https://huggingface.co/IJyad/jeb-typed-decisions) | 09-22 09:22 / 09-22 09:33 | A | Arabic (Saudi/Gulf) typed-decision specialisation of IJyad/jeb on programmatically generated synthetic … | train | no | **first-sighting** | H |
| 196 | [github:jinlio/mjbrain](https://github.com/jinlio/mjbrain) | 09-22 09:20 / 09-23 10:32 | A | Riichi mahjong decision recommender: LAYA fine-tuned with Mortal-teacher soft labels (human x teacher … | train | no | **first-sighting** | R |
| 197 | [github:Xiao-AI-Lab/xiaojev](https://github.com/Xiao-AI-Lab/xiaojev) | 09-22 08:38 / 09-23 02:12 | A | xiaojev: 0.6B model with calibrated distributions from programmatic ground truth (no LLM in the loop) | train | no | archive meta (patrol-gfs) | R |
| 198 | [github:Astroshreyas1/Society-Harness-](https://github.com/Astroshreyas1/Society-Harness-/blob/b54eafc7d0fb0f2a9fe0acddcbbd78fd9d8c5d56/agentsim/train.py) | 09-22 08:21 / 09-22 11:02 | A | Gateway harness: 'train-jev' converts OTel-shaped traces to typed (state, answers) examples and fits a … | train | no | **first-sighting** | C |
| 199 | [hf:hxrikp/laya-session-guard-pilot](https://huggingface.co/hxrikp/laya-session-guard-pilot) | 09-22 07:20 / 09-22 08:05 | A | Full fine-tune of Laya for coding-session guard decisions (480 synthetic sessions, T4, 302 s); missed … | train | no | **first-sighting** | H |
| 200 | [github:Mr-Neutr0n/laya-session-guard](https://github.com/Mr-Neutr0n/laya-session-guard) ▣ | 09-22 07:17 / 09-22 08:22 | A | Session-aware Laya fine-tuning with prompt-injection/action-authorization evals (Kaggle T4, 301.7 s) | train | no (lane: unclear); Jev comparator outputs ship beside training data | **first-sighting** | RC |
| 201 | [github:Caho1/Jev](https://github.com/Caho1/Jev) | 09-22 07:12 / 09-22 07:24 | A | Jev/Laya experiment monorepo: distill-lab (Laya fine-tune BANKING77 85.55%, CrossWOZ, browser choice) + … | train | no (lane: unclear) | archive meta (refresh-ghd) | RC |
| 202 | [hf:thaitea/laya-vision-smolvlm-256m-score](https://huggingface.co/thaitea/laya-vision-smolvlm-256m-score) | 09-22 06:24 / 09-22 15:19 | A | SmolVLM-256M Laya-vision variant whose options attend to each other; trained on 19 Cauldron subsets + … | train | no | **first-sighting** | H |
| 203 | [github:aungthuhein2005/laya-burmese](https://github.com/aungthuhein2005/laya-burmese) | 09-22 06:23 / 09-22 13:38 | A | Zero-shot, calibration and fine-tuning study of Laya on Burmese SIB-200 topic classification | train | no | archive meta (2026-09-22-refresh/method-discovery.json) | R |
| 204 | [github:manyamkarthik/laya-issue-triage](https://github.com/manyamkarthik/laya-issue-triage) | 09-22 05:07 / 09-22 14:12 | A | Fine-tuned Laya GitHub-issue triager (single CPU pass) with training data, held-out benches, GitHub … | train | no | **first-sighting** | RC |
| 205 | [github:guzus/jev-nyotti](https://github.com/guzus/jev-nyotti) | 09-22 05:07 / 09-23 09:05 | A | Jev-compatible market-research API with Qwen3.5-4B LoRA pilot trained on user trading history | train | no | archive meta (refresh-ghd) | R |
| 206 | [github:themaker00001/JevFlash](https://github.com/themaker00001/JevFlash) | 09-22 05:02 / 09-23 19:12 | A | MPS replication of NanoJev's non-generative architecture; Qwen3-0.6B vs 1.7B; DAgger from heuristic | train | no | archive meta (refresh-ghd) | R |
| 207 | [hf:tjm8874/LFM2.5-VL-3B-Decision-NVFP4](https://huggingface.co/tjm8874/LFM2.5-VL-3B-Decision-NVFP4) | 09-22 04:59 / 09-22 05:22 | A | LFM2.5-VL-3B fine-tune (vision encoder, projector and head frozen) for text candidate selection and … | train | no | **first-sighting** | H |
| 208 | [github:sqliteai/blink](https://github.com/sqliteai/blink) | 09-22 04:17 / 09-23 06:05 | A | Blink: high-performance System One model with embeddable C runtime and WebGPU (ViZDoom Basic/Predict … | train | no | archive meta (refresh-ghd) | R |
| 209 | [github:Addisonmeng/NanoJev](https://github.com/Addisonmeng/NanoJev) | 09-22 03:02 / 09-23 13:40 | A | NanoJev MuJoCo policy derivative | train | no | archive meta (patrol-gfs) | R |
| 210 | [github:xiaol/Gut-RWKV-Jev-laya](https://github.com/xiaol/Gut-RWKV-Jev-laya) | 09-22 00:46 / 09-22 16:24 | A | Gut-RWKV: RWKV state-tuning decision engine on Kev decision-v7 (44.3% on 1,468 held-out) | train | no | archive meta (patrol-gfs) | R |
| 211 | [github:Akicou/system-one-270m](https://github.com/Akicou/system-one-270m) | 09-21 23:15 / 09-21 23:15 | A | system-one-270m: gemma-3-270m-it with calibrated typed decisions, soft targets via log score | train | no | notes §157 | R |
| 212 | [github:ArturL6/specialist-factory](https://github.com/ArturL6/specialist-factory) | 09-21 20:03 / 09-22 07:56 | A | Teacher-to-specialist POC: cached teacher signals (BART-MNLI, CLIP, OpenRouter VLM) aggregated -> small … | train | no (lane: unclear) | **first-sighting** | RC |
| 213 | [hf:mogita/jev-decider-qwen3-4b](https://huggingface.co/mogita/jev-decider-qwen3-4b) | 09-21 19:26 / 09-22 09:20 | A | Qwen3-4B LoRA over letter logits for bank-transaction categories: 20k public rows, then 8k synthetic … | train | no | archive meta (refresh-hfd) (lane: first) | H |
| 214 | [hf:distil-labs/distil-qwen3.5-4b-invoice-decision](https://huggingface.co/distil-labs/distil-qwen3.5-4b-invoice-decision) | 09-21 18:52 / 09-22 05:30 | A | Qwen3.5-4B fine-tuned on distil labs from 40 seed examples; teacher GLM 5.3 (reasoning) generated 4,156 … | train | no | **first-sighting** | H |
| 215 | [hf:saivamshiatukuri/qwen3.5-4b-decision-mind2web](https://huggingface.co/saivamshiatukuri/qwen3.5-4b-decision-mind2web) | 09-21 18:06 / 09-21 18:20 | A | Qwen3.5-4B LoRA reading answers from slot logprobs ("Arm 3"), best of four designs in a study; element … | train | no | **first-sighting** | H |
| 216 | [github:Alexander-Ollman/laya-ft](https://github.com/Alexander-Ollman/laya-ft) | 09-21 17:28 / 09-21 22:27 | A | Jev vs fine-tuned Laya: Banking77 51.3% -> 79.4% (Jev 80.0%), chat moderation | train | no | notes §148,156 | R |
| 217 | [github:mb-mal/multisorter](https://github.com/mb-mal/multisorter) | 09-21 16:33 / 09-21 16:58 | A | multisorter: one 1.8M-param trunk answering tetris, snake, text classification and CIFAR-10 typed … | train | no | **first-sighting** | R |
| 218 | [github:beratcmn/qwen3.5-0.8b-systemone](https://github.com/beratcmn/qwen3.5-0.8b-systemone) ▣ | 09-21 15:07 / 09-21 21:14 | A | qwen3.5-0.8b-systemone (README is a name only) | readout only | no (lane: unclear); trains nothing | **first-sighting** | R |
| 219 | [github:codedpro/reflex-mlx](https://github.com/codedpro/reflex-mlx) | 09-21 14:16 / 09-22 05:55 | A | Reflex MLX: learn a hashed ridge classifier from verified outcomes, gate on calibration set, defer to … | train | no | **first-sighting** | R |
| 220 | [hf:s1lv3rj1nx/openjev-encoder-general](https://huggingface.co/s1lv3rj1nx/openjev-encoder-general) | 09-21 08:21 / 09-22 10:43 | A | ModernBERT-base general typed-decision encoder with fitted per-question temperatures; siblings … | train | no | archive meta (hourly 2026-09-21T09) (lane: first) | H |
| 221 | [github:RelativeDB/rt-doom](https://github.com/RelativeDB/rt-doom) | 09-21 07:03 / 09-21 07:03 | A | Relational Transformers fine-tuned to play Doom; scripted teacher labels observations | train | no | **first-sighting** | R |
| 222 | [github:samdoom-coder/Snapjudge](https://github.com/samdoom-coder/Snapjudge) ▣ | 09-21 03:06 / 09-23 23:27 | A | SnapJudge: open 165M System One model that judges game states in one pass | train | no (lane: unclear); exact-solver labels | **first-sighting** | R |
| 223 | [github:hamakyo/open-jev-mahjong](https://github.com/hamakyo/open-jev-mahjong) | 09-21 01:24 / 09-21 01:29 | A | Distill Mortal's riichi-mahjong decisions into a ModernBERT Open Jev model; eval via jev-mahjong-bench | train | no | **first-sighting** | R |
| 224 | [hf:telepatia-ai/laya-pt-es-nli](https://huggingface.co/telepatia-ai/laya-pt-es-nli) | 09-21 00:14 / 09-21 00:18 | A | Full fine-tune (no LoRA) of laya-multilingual for pt/es 3-way NLI with RLCD + CE (4 perturbations, log + … | train | no | **first-sighting** | H |
| 225 | [github:mizorewww/pastewhat-ranker-v1](https://github.com/mizorewww/pastewhat-ranker-v1) | 09-20 23:54 / 09-23 21:13 | A | Candidate-aware clipboard ranker distilled into Laya-multilingual encoder | train | no | archive meta (patrol-gfs) | R |
| 226 | [hf:jaredpalmer/kev-9b](https://huggingface.co/jaredpalmer/kev-9b) | 09-20 22:42 / 09-21 14:15 | A | HF weights for Kev Qwen3.5-9B-Base (LoRA + pointer head); siblings jaredpalmer/kev-0.8b; card: "No Jev … | train | no | archive meta (hourly 2026-09-21T12) (lane: first) | H |
| 227 | [github:abhishek085/open-spark-jev](https://github.com/abhishek085/open-spark-jev) | 09-20 19:39 / 09-22 19:33 | A | spark-s1-4b-v6: Qwen3 decision models for DGX Spark; 11,792 code/LLM-labelled rows across 49 task packs | train | no | archive meta (refresh-ghd) | R |
| 228 | [github:day253/microjev](https://github.com/day253/microjev) | 09-20 15:35 / 09-21 15:29 | A | GPT-2 124M with Jev-style typed decisions on MLX, plus a pure-Python teaching model | train | no | archive meta (hourly 2026-09-20T18) | R |
| 229 | [hf:iapp/OpenThai-SystemOne](https://huggingface.co/iapp/OpenThai-SystemOne) | 09-20 14:15 / 09-21 17:38 | A | Qwen3.5-0.8B-Base text tower, Thai continued pretraining (~5B tokens), LM head replaced by a 256-way … | train | no | archive meta (hourly 2026-09-21T17) (lane: first) | H |
| 230 | [github:scienthoon/luce](https://github.com/scienthoon/luce) | 09-20 04:27 / 09-22 08:39 | A | Luce: init -> synth -> train (LoRA + decision head on Qwen) -> calibrate recipe | train | no | notes §106 | R |
| 231 | [github:hiroki-abe-58/sokudan](https://github.com/hiroki-abe-58/sokudan) | 09-20 02:56 / 09-22 05:06 | A | sokudan: Japanese System One decision model with bench_ja/bench_en and Laya position-bias study | train | no | notes §114 | R |
| 232 | [github:edgelabs-ai/jev48](https://github.com/edgelabs-ai/jev48) | 09-20 00:30 / 09-21 06:29 | A | Jev48: 48-hour agent-built open reproduction; Decider-2B checkpoint, soft-label selection on locked … | train | no | archive meta (refresh-ghd) | R |
| 233 | [hf:vagmi/jev-lite](https://huggingface.co/vagmi/jev-lite) | 09-19 23:46 / 09-20 00:01 | B | Gemma 4 E4B QLoRA (r16, 1 epoch, one RTX 4090, 1h40m); 23,632 rows over 301 tasks; soft labels from … | train | no | archive meta (refresh-hfd) (lane: first) | H |
| 234 | [github:weiyangzen/zenjev](https://github.com/weiyangzen/zenjev/blob/406569d251d063ef8137506efc92347f264a9291/jev/distill.py) | 09-19 20:12 / 09-22 07:29 | A | LoRA 'distillation pairs' (143,869) from 208,814 records of a GPT-5.6-sol capture corpus, served on an … | train | no | **first-sighting** | C |
| 235 | [hf:lafalce/system-one-model](https://huggingface.co/lafalce/system-one-model) | 09-19 16:41 / 09-19 16:41 | B | ModernBERT-base + LoRA r16 + 2-layer fp32 scoring head, distilled from a frozen Qwen2.5-7B-Instruct-AWQ … | train | no | **first-sighting** | H |
| 236 | [github:mateolafalce/system-one-model](https://github.com/mateolafalce/system-one-model) | 09-19 16:25 / 09-19 16:44 | B | 'Domain System One' for an 8 GB GPU: ModernBERT-base + LoRA r16 + 2-layer head; phase 1 human gold, … | train | no | **first-sighting** | W |
| 237 | [github:r33drichards/laya-vision](https://github.com/r33drichards/laya-vision) | 09-19 15:12 / 09-23 23:54 | A | Laya Vision: SmolVLM-256M image+text typed decisions | train | no | notes §87,146 | R |
| 238 | [hf:noscienthoon/ouro-2.6b-decision-lora](https://huggingface.co/noscienthoon/ouro-2.6b-decision-lora) | 09-19 14:20 / 09-19 23:59 | B | Ouro-2.6B (looped LM) LoRA r16 + 2-layer head; 2k ARC-Easy + 2k BoolQ, CE + Brier, checkpoint by … | train | no | **first-sighting** | H |
| 239 | [github:NomaDamas/kojev](https://github.com/NomaDamas/kojev) | 09-19 14:16 / 09-21 08:37 | A | KoJev-v0: Korean Jev-style decision model (SFT-only; RLCD attempted NO-GO) | train | no | archive meta (refresh-ghd) | R |
| 240 | [hf:IamBusy/OpenJev-0.6B](https://huggingface.co/IamBusy/OpenJev-0.6B) | 09-19 10:27 / 09-19 10:50 | B | Qwen3-0.6B attention LoRA (1.15M params) + independent scalar head; 725 training judgments where rules … | train | no | **first-sighting** | H |
| 241 | [github:IamBusy/OpenJev-Vision](https://github.com/IamBusy/OpenJev-Vision) | 09-19 09:30 / 09-22 16:30 | A | OpenJev-Vision: encode an image once, answer multiple structured questions; public data + trained weights | train | no | notes §108,117,147 | R |
| 242 | [github:zwliJay/jev-forge](https://github.com/zwliJay/jev-forge) | 09-19 05:44 / 09-23 04:17 | A | JevForge: training/inference stack scoring dynamic candidate branches from a shared prefix (Mind2Web) | train | no | notes §99,101,115 | R |
| 243 | [github:djhoomin/local-system-one](https://github.com/djhoomin/local-system-one) | 09-18 18:23 / 09-23 10:32 | A | Local stand-ins for Jev's interface: small-model routing benchmark + distilled 19 ms 149M encoder | train | no | notes §143 | R |
| 244 | [github:bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) | 09-18 09:07 / 09-23 18:49 | A | Bespoke Nimble: local typed decisions, contrastive data curation with human-labelled public subsets, … | train | no | notes §35,130,141; TR | R |
| 245 | [github:kotoba-lang/typed-decisions](https://github.com/kotoba-lang/typed-decisions) | 09-18 07:03 / 09-22 13:52 | A | Jev-shaped typed-decision models on ModernBERT/DeBERTa/LLaDA-MoE with measured latency | train | no | notes §33,130,131,132; TR | R |
| 246 | [hf:adampippert/granite-decisions](https://huggingface.co/adampippert/granite-decisions) | 09-18 02:31 / 09-18 12:02 | B | IBM granite-4.1-3b decision adapter; bundled smoke artifacts trained on 54-row template-labelled … | train | no | **first-sighting** | H |
| 247 | [github:kshetrajna12/reflex](https://github.com/kshetrajna12/reflex) | 09-17 23:03 / 09-23 01:25 | A | reflex: small open decision model re-creating Jev/System One on Qwen3.5; reflex-distill route | train | no | notes §121; TR | R |
| 248 | [github:jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 09-17 20:49 / 09-23 23:42 | A | Kev: Qwen3.5 0.8B/4B/9B + rank-16 LoRA + pointer head, decision-v7 data (public datasets + generated … | train | no | notes §45,49,60,77…; TR | RC |
| 249 | [github:OmniJev/PlayJev](https://github.com/OmniJev/PlayJev) | 09-17 20:37 / 09-21 14:00 | A | 0.8B JEV-like multimodal model playing 10 GUI games from pixels; cloning from per-game teachers + 3 … | train | no (lane: unclear) | archive meta (refresh-jevusers) | RC |
| 250 | [github:catoenm/first-instinct](https://github.com/catoenm/first-instinct) | 09-17 03:50 / 09-23 23:43 | A | Train and inspect a small decision model on your Mac: public data, full fine-tuning, downloadable weights | train | no | notes §136,137 | R |
| 251 | [hf:andyshu/opensysone](https://huggingface.co/andyshu/opensysone) | 09-17 02:15 / 09-17 12:10 | B | Rank-8 adapters + scalar head (16.5M trainable) on Qwen3-4B-Instruct-2507 scoring explicit candidates; … | train | no | **first-sighting** | W |
| 252 | [hf:DavidHatley/system-one-mini](https://huggingface.co/DavidHatley/system-one-mini) | 09-16 17:02 / 09-16 17:30 | B | DistilBERT 69.3M with five depth-2 heads for fixed typed decisions; 20,000 deterministic synthetic … | train | no | **first-sighting** | H |
| 253 | [hf:pngwn/nanodiff-350m-typed-decisions-lam1](https://huggingface.co/pngwn/nanodiff-350m-typed-decisions-lam1) | 09-16 15:07 / 09-16 16:04 | B | Proper-scoring arm (lambda=1) of a controlled calibration study on a 350M masked-diffusion LM; within L1 … | train | no | archive meta (hourly 2026-09-21T09) (lane: first) | H |
| 254 | [github:Mapika/decider](https://github.com/Mapika/decider) | 09-16 07:15 / 09-23 19:57 | A | decider: Qwen3.5-4B/35B-A3B System One models; public datasets + local Qwen3.5-27B teacher; mixture v2 | train | no | notes §102; TR | R |
| 255 | [github:sloina/context-enriched-heads](https://github.com/sloina/context-enriched-heads) | 09-14 15:07 / 09-23 18:42 | A | Tiny linear context-enriched decision heads (65-386 params) on frozen wake-word detectors (ICASSP 2027 … | train | no | **first-sighting** | R |
| 256 | [github:integrallis/models](https://github.com/integrallis/models/blob/cb041e7948199ccd0ede0d737009c968b8306eda/models-decisions/benchmark-results/2026-09-20-noul-head/THIRD-PARTY-TERMS.md) | 05-02 13:41 / 09-23 22:59 | A | In-JVM Noul head fit on hidden states of their own Granite 4.1 3B (Apache-2.0) with digest-pinned corpus … | train | no | **first-sighting** | C |
| 257 | [github:ivanviragine/jev-vs-llms](https://github.com/ivanviragine/jev-vs-llms) | 09-24 00:19 / 09-24 00:19 | D | Same loaded questions to Jev, GPT-5.6, Claude and Kev/Laya in English and Portuguese | eval | no | **first-sighting** | R |
| 258 | [github:ngallodev-software/typesafe-ai-implementation-skill](https://github.com/ngallodev-software/typesafe-ai-implementation-skill/blob/592f5acdfb406894255c56d76b0dfaf6e2899367/SKILL.md) | 09-23 23:18 / 09-23 23:44 | D | WIP skill for finding and building Jev opportunities: start in shadow/advisory mode, compare against … | guide | no | **first-sighting** | C |
| 259 | [github:MaojieXu/typed-mini-guard](https://github.com/MaojieXu/typed-mini-guard) | 09-23 22:19 / 09-23 22:19 | D | Typed Mini Guard: planned lightweight typed decision model for agent security; 39-family training-data … | data | no | **first-sighting** | R |
| 260 | [github:blacksinisterx/jev-bench](https://github.com/blacksinisterx/jev-bench) | 09-23 21:40 / 09-23 22:20 | D | When does a genuinely trained classifier beat Jev? Accuracy vs training-data size (10-147 examples) on … | eval | no | **first-sighting** | R |
| 261 | [hf:ds:servronix/laya-thai-trainset](https://huggingface.co/datasets/servronix/laya-thai-trainset) | 09-23 13:37 / 09-23 13:39 | D | 29,667 Thai typed-decision rows (Wisesight train + XNLI-th train + 39 handwritten), schema-compatible … | data | no | **first-sighting** | H |
| 262 | [hf:ds:AirsideLabs/notam-typed-decisions](https://huggingface.co/datasets/AirsideLabs/notam-typed-decisions) | 09-23 12:03 / 09-23 12:03 | D | Frozen, hashed eval suites for typed decisions about NOTAMs; labels derived from Q-code/Q-line (not … | eval | no | **first-sighting** | H |
| 263 | [github:gkastanis/d3code-calibration](https://github.com/gkastanis/d3code-calibration) | 09-23 11:50 / 09-23 12:58 | D | Checks Jev and open-weights Laya probabilities against 150,000 human ratings; stdlib recalibration tools | eval | no | archive meta (patrol-gfs) | R |
| 264 | [hf:space:biswapm/jev-tool-model-router](https://huggingface.co/spaces/biswapm/jev-tool-model-router) | 09-23 09:13 / 09-23 09:33 | D | Jev-style router that picks tool and model tier in one batched pass; parameters fit by search to … | guide | no | archive meta (patrol-ledger) (lane: first) | H |
| 265 | [github:sureshbujji/jev-eval-lab](https://github.com/sureshbujji/jev-eval-lab) | 09-23 07:22 / 09-23 07:22 | D | Eval harness for typed decisions: golden-dataset runner, calibration metrics, schema tests (offline … | eval | no | archive meta (patrol-gfs) | R |
| 266 | [github:akiraNuma/claude-plugins](https://github.com/akiraNuma/claude-plugins/blob/ee149096f617124465b7d18f9a12097d32f01acb/plugins/jev-model-router/skills/jev-router-tune/SKILL.md) | 09-23 05:34 / 09-23 06:36 | D | Japanese skill: aggregates jev-model-router decision/outcome logs to check tier usage, whether … | guide | no | **first-sighting** | C |
| 267 | [github:asp616848/better-jev-bench](https://github.com/asp616848/better-jev-bench) | 09-23 03:57 / 09-23 21:34 | D | License-tiered multi-domain corpus + benchmark for training/evaluating typed decision models (8 … | data | no | archive meta (patrol-gfs) | R |
| 268 | [github:MikeyBeez/calibration-table](https://github.com/MikeyBeez/calibration-table) | 09-23 01:54 / 09-23 01:54 | D | Calibrating an open Jev-style classifier (von-1.0) with a lookup table vs one temperature | eval | no | archive meta (patrol-gfs) | R |
| 269 | [url:https://www.together.ai/blog/how-to-train-your-own-jev](https://www.together.ai/blog/how-to-train-your-own-jev) | 09-23 / 09-23 | D | Together AI blog 'How to train your own Jev for $17' (2026-09-23): Qwen3.5-4B fine-tune on 37,840 … | guide | no | **first-sighting** | W |
| 270 | [url:https://www.orcarouter.ai/blog/jev-vs-kev](https://www.orcarouter.ai/blog/jev-vs-kev) | 09-23 / 09-23 | D | OrcaRouter blog 'Jev vs Kev: A $95 Fine-Tune Beats Jev on Support Tickets' (2026-09-23), restating Kev … | guide | no | **first-sighting** | W |
| 271 | [url:https://rohitraj.tech/notes/jev-alternatives-open-weights-decision-models-2026](https://rohitraj.tech/notes/jev-alternatives-open-weights-decision-models-2026) | 09-23 / 09-23 | D | Listicle of open-weight Jev alternatives (2026-09-23): Laya, Kev, open-alternative-jev, … | guide | no | **first-sighting** | W |
| 272 | [github:lemon-tea-ai/qwen35-9b-mlx-decision](https://github.com/lemon-tea-ai/qwen35-9b-mlx-decision) | 09-22 15:57 / 09-22 15:57 | A | Frozen Qwen3.5-9B MLX 4-bit decision baseline: 184/231 public JevBench, raw ECE 8.09% | eval | no | archive meta (patrol-gfs) | R |
| 273 | [hf:ds:pranaysuyash/laya-formatting-fragility](https://huggingface.co/datasets/pranaysuyash/laya-formatting-fragility) | 09-22 15:41 / 09-22 20:26 | A | Hand-labelled formatting-robustness suite for small decision models (Laya 0.3.5, AgentJev-0.6B, hosted … | eval | no | **first-sighting** | H |
| 274 | [github:Serendeep/rl-by-subtraction](https://github.com/Serendeep/rl-by-subtraction) | 09-22 15:04 / 09-23 10:44 | A | Toy numpy RLHF/RLVR/RLCD/GRPO implementations sharing one environment | guide | no | archive meta (patrol-gfs) | R |
| 275 | [github:rssr25/sys1bench](https://github.com/rssr25/sys1bench) | 09-22 14:03 / 09-23 09:57 | A | sys1bench: calibration vs noise floor, framing sensitivity, selective prediction for Jev/Laya/Kev | eval | no | archive meta (patrol-gfs) | R |
| 276 | [github:treadkex1/decision-model-security](https://github.com/treadkex1/decision-model-security) | 09-22 13:39 / 09-22 13:39 | A | Security tests of Kev 0.8B/4B: state injection, confident-wrong, option order, delimiter forgery | eval | no | archive meta (refresh-ghd) | R |
| 277 | [hf:ds:mghafiri/decision-model-scenarios](https://huggingface.co/datasets/mghafiri/decision-model-scenarios) | 09-22 13:36 / 09-22 15:18 | A | 2,000 synthetic English scenarios, 9,716 typed questions with calibrated soft labels (rubric: fraction … | data | no | **first-sighting** | H |
| 278 | [github:NotoriousPOG/trust-router](https://github.com/NotoriousPOG/trust-router) | 09-22 09:12 / 09-22 09:12 | A | Shadow-mode security router: rules vs BERT vs Laya on an external prompt-injection challenge | eval | no | **first-sighting** | R |
| 279 | [github:dhruvmehra/jevbench](https://github.com/dhruvmehra/jevbench) | 09-22 02:11 / 09-22 02:12 | A | Benchmark Jev vs LLMs vs per-dataset fine-tuned DistilBERT vs Laya vs zero-shot NLI | eval | no | notes §161 | R |
| 280 | [github:shivpratapsinghpanwar/edgefront_JEV](https://github.com/shivpratapsinghpanwar/edgefront_JEV) | 09-21 18:00 / 09-22 18:50 | A | Hosted decision model vs small local model on your own task: accuracy, latency, calibration, cost | eval | no | archive meta (patrol-gfs) | R |
| 281 | [hf:space:jaredpalmer/kev](https://huggingface.co/spaces/jaredpalmer/kev) | 09-21 13:38 / 09-23 00:50 | A | Kev demo Space, "tiny Jev-like decision models you can train yourself" (35 likes); modified 2026-09-23. | guide | no | notes §45,49,60,77…; TR | H |
| 282 | [github:cocodedk/jev-bench](https://github.com/cocodedk/jev-bench) | 09-21 11:11 / 09-21 11:53 | A | Configurable classifier workbench: Jev (OpenRouter) vs classifier.dev (jev/laya tiers) on BANKING77 | eval | no | **first-sighting** | R |
| 283 | [github:KacperPilkowski/semif-needle](https://github.com/KacperPilkowski/semif-needle) | 09-21 07:16 / 09-21 07:46 | A | Porting SemIf's typed-logit readout to Cactus Needle 3 (121M): a negative result with controls | eval | no | **first-sighting** | R |
| 284 | [github:Maverick-Ansh/jev-from-scratch](https://github.com/Maverick-Ansh/jev-from-scratch) | 09-21 06:04 / 09-21 07:30 | A | First-principles rebuild of Jev's non-autoregressive decision model (total-correlation, … | guide | no | notes §136 | R |
| 285 | [github:hazemibrahim97/decision-models-css](https://github.com/hazemibrahim97/decision-models-css) | 09-21 05:43 / 09-23 08:18 | A | Replication package: decision models for text annotation in computational social science | eval | no | archive meta (refresh-ghd) | R |
| 286 | [hf:ds:SamuelChien821/typed-decision-bench](https://huggingface.co/datasets/SamuelChien821/typed-decision-bench) | 09-20 19:52 / 09-20 21:21 | B | 5,387 items / 25 tasks from 21 openly licensed datasets + one generator, per-item source/licence … | eval | no | archive meta (hourly 2026-09-21T09) (lane: first) | H |
| 287 | [github:mugenkyou/JEV-VS-ML](https://github.com/mugenkyou/JEV-VS-ML) | 09-20 19:03 / 09-21 14:33 | A | Reproducible benchmark: Jev 1.13.0 vs 11 conventional ML pipelines across eight datasets | eval | no | archive meta (hourly 2026-09-20T19) | R |
| 288 | [hf:ds:altslate/certo-decisions-v2](https://huggingface.co/datasets/altslate/certo-decisions-v2) | 09-20 06:51 / 09-21 17:59 | A | Canonical-schema decision corpus with a per-record provenance column (e.g. MultiNLI 120k gold) plus … | data | no | **first-sighting** | H |
| 289 | [hf:ds:com-kotobalabs/typed-decisions-code-holes](https://huggingface.co/datasets/com-kotobalabs/typed-decisions-code-holes) | 09-19 23:25 / 09-20 02:57 | B | Single-token substitutions mined from git history of 64 public repos; gold = the token the commit used; … | eval | no | archive meta (hourly 2026-09-21T09) (lane: first) | H |
| 290 | [github:clduab11/jev-test](https://github.com/clduab11/jev-test/blob/0fe81072cb9b6dcc191aa9037ba142bd73ff3eb2/scripts/export_corpus.py) | 09-19 17:00 / 09-21 17:54 | A | Pre-registered 2B-vs-Jev benchmark; export keeps 67,312 raw Jev records local and publishes aggregates … | eval | no | notes §89,146 | C |
| 291 | [url:https://wunderlandmedia.com/typesafe-ai-jev-terms-of-service-gdpr](https://wunderlandmedia.com/typesafe-ai-jev-terms-of-service-gdpr) | 09-18 / 09-18 | B | Third-party EU/GDPR reading of TypeSafe's terms (modified 2026-09-18): quotes MCA §2.3(b) distillation … | guide | no | **first-sighting** | W |
| 292 | [hf:space:multimodalart/jev-decision-index](https://huggingface.co/spaces/multimodalart/jev-decision-index) | 09-17 20:05 / 09-23 12:11 | A | Index of open Jev repros with benchmarks and news (161 likes); copied as KingClancy/jev-decision-index. | guide | no | archive meta (patrol-ledger) (lane: first) | H |
| 293 | [github:hideshi/llm-skills](https://github.com/hideshi/llm-skills/blob/2bced6745dfce1f935eef97cc3ce40124258543a/skills/jev-eval-set/SKILL.md) | 09-17 11:33 / 09-21 07:37 | A | Japanese skill chain jev-logic-architect -> jev-eval-set (define gold, sampling/leak prevention, … | eval | no | **first-sighting** | C |
| 294 | [github:Busy-Office/ai-skills](https://github.com/Busy-Office/ai-skills/blob/844ae36ecd2be749dcc0486e244c3fb50146a143/skills/kev-gate/SKILL.md) | 09-07 16:10 / 09-20 09:17 | B | kev-gate skill: put KEV (or hosted Jev) in front of an agent step; labels come from the project's own … | guide | no | **first-sighting** | C |
| 295 | [github:STRML/omp-classifier](https://github.com/STRML/omp-classifier/blob/cb8981d60edc7ab3b26c2f94affc9911a3df751d/.agents/skills/optimizing-jev/SKILL.md) | 08-19 16:09 / 09-23 00:19 | A | Skill for writing/tuning Jev questions, state and thresholds: atomic semantic facts, decision in code, … | guide | no | archive meta (patrol-gfs) | C |
| 296 | [github:magnus919/agent-skills](https://github.com/magnus919/agent-skills/blob/d95e6cfcd192025b16fcf6f57dc79553b6426960/system-one/scripts/jev_teacher_label.py) | 07-11 21:36 / 09-23 23:49 | A | system-one skill script: labels blinded Jev review packets with a separate inference model (prompt … | eval | no | notes §166 | C |
| 297 | [github:CathedralOS/Omega](https://github.com/CathedralOS/Omega/blob/b8aeb99401cf7cee92353e56d795550637cdbb82/.agents/skills/typesafe-experiments/SKILL.md) | 06-20 21:36 / 09-23 23:53 | A | Skill to tune and evaluate TypeSafe/Jev judgments in compiler-agent workflows; synthetic controls kept … | eval | no | **first-sighting** | C |
| 298 | [github:IgorGanapolsky/ThumbGate](https://github.com/IgorGanapolsky/ThumbGate/blob/1e3849239836e11ad516b512b123b4c0011961ff/.agents/skills/typesafe-typed-questions-not-clone/SKILL.md) | 03-03 18:13 / 09-23 21:50 | A | Skill 'TypeSafe typed questions - compare, do not clone': deterministic matchers answer the question … | guide | no | **first-sighting** | C |

---

## 3. Recipe cards (16 deep-inspected items)

Condensed from the deep-inspection cards; every card field is kept. Files
were read at the pinned SHA via raw.githubusercontent, the GitHub API or the
HF API; nothing was executed and no weights were downloaded. All numbers are
the source's own (Reported) except where marked "local arithmetic". Four
cards' key facts are also in `tmp/deep4-hotdog-nagi/cards.json`, four full
cards in `tmp/deep4-sysone/cards.json`, and four key-fact sets in
`tmp/cards-verdict-ruhui-compass-jevnext/cards.json`.

### 3.1 `github:StevenJPx2/jev-distill` — uses Jev outputs (sole teacher)
- **Revision.** HEAD `401eb17f` (2026-09-23T05:05:51Z), node `R_kgDOUmunhw`, v0.1.0, one visible push. First card; only a patrol-gfs metadata row existed. Distinct from Jairik/jev-distiller (§104) and SargeDev corpora.
- **Inspected.** README; `src/teacher/jev.ts`, `question.ts`; `src/train/index.ts`, `select.ts`; `src/student/features.ts`; `src/eval.ts`; routing example task and data; package.json; repo-wide terms grep.
- **Backbone / head.** No neural backbone: multinomial logistic regression over FNV-1a-32 hashed word (≤2) and char (3,4) n-grams, 262,144 buckets, full-batch Adam with L2. Linear softmax over 2–255 labels; abstains below `student_min_confidence` using Jev's (K·p_max−1)/(K−1) transform.
- **Output / calibration.** A fitted imitation of Jev's Choice distribution; "confidence" is a concentration transform, not P(correct). No temperature; fixed abstain threshold with coverage reported per threshold.
- **Data and labels.** User `data.jsonl` rows (examples: 100 routing, 60 permission). **Labels are Jev Choice answers only** (pinned jev-1.13.0): soft target = Jev's full distribution, hard = Jev's top choice, and rows below teacher confidence 0.3 are dropped. Gold is used only for held-out scoring and was written by the building agent.
- **Provenance evidence.** README:12-14 "Jev is the only teacher. Training labels come only from Jev answers"; `src/train/index.ts:167-170` soft target `record.probabilities[label]`; `:124-126` Jev-confidence filter; `select.ts:8` CV objective is "agreement with Jev's top label (not accuracy)". No mention of TypeSafe terms.
- **Eval (Reported).** Routing holdout n=25: agreement with Jev 60.0% (Wilson 40.7–76.6); 92.3% at 52% coverage; student vs gold 60.0%; Jev vs gold 100% (agreement with the building agent, not human truth); majority 12.0%. Permission n=12 flagged "insufficient evidence" by the tool. Labeling cost $0.00206 for 100 requests. Local arithmetic: the Wilson intervals recompute from the reported counts.
- **License / compute / runs on.** MIT. About 2 s to train 75 rows on Apple Silicon; artifact 707 KB; byte-identical retrains. CPU, Node 22+, any OS.
- **Good.** Teacher-agnostic harness: union-find leakage components, content-hash ids, append-only hash-only label ledger keyed on (content, question, model), approval gate and budgets, failures and 403s never become labels, mixed-teacher refusal, trained-overlap exclusion at eval, dual agreement/accuracy report with CIs and a majority baseline.
- **Bad / risks.** The teacher is Jev; model selection optimizes imitation; tiny holdouts; surface-form features. Using it as designed is the case §2.3(b) names (Hypothesis until counsel).
- **Borrow.** The harness with a permitted teacher behind the `Teacher` interface; select L2 by inner CV on gold, not teacher agreement. 75 distilled rows reached 60% where the teacher scored 100%: try R0/R1 before R2 on small data.

### 3.2 `github:Adamya05/jev-echo` — uses Jev outputs (soft labels, DAgger relabel)
- **Revision.** HEAD `d2e9a202` (2026-09-23T20:14:31Z), node `R_kgDOUmqWYA`; moved after the patrol row (04:04Z). First card.
- **Inspected.** README; `collect_raw.py`, `train_board.py`, `train.py`; `sysone/snake/{boardnet,student,collect,search,policy,compare}.py`; `sysone/core.py`; pyproject.
- **Backbone / head.** BoardNet: 3 input planes on 10×10, Conv3×3(3→16), Conv3×3(16→16), 2×2 pool, Linear(400→48→4); 22,212 params (local arithmetic matches). Masked log-softmax over 4 moves; confidence = p1−p2 margin.
- **Output / calibration.** A move distribution imitating Jev's; no calibration fitted or claimed; decisiveness weighting (1−H/Hmax, floor 0.05) at training.
- **Data and labels.** About 13.7k boards labelled by Jev (`typesafe/jev-1.13` via OpenRouter), probabilities renormalized over legal moves, plus two DAgger rounds of 250 Echo-driven games relabelled by Jev. The default driver is an earlier student trained on Jev priors, so even the state distribution is Jev-derived.
- **Provenance evidence.** README:3-4 "trained on the answers of Jev"; `collect_raw.py:49` `jev.decide(...)`; `sysone/core.py:116-125` OpenRouter model `typesafe/jev-1.13`.
- **Eval (Reported).** 10 games per player on the same 10 boards, disjoint collection seeds. Safety net on: Jev 21.5, Echo 17.8, Echo+search 29.1 (won 9/10). Off: 8.9 / 7.7 / 17.2 (9/10). 0.20 ms vs 215 ms per move. "No clear difference" is a failure to distinguish, not equivalence.
- **License / compute / runs on.** MIT. About 30 s training on an M4 CPU; MLX on Apple Silicon required.
- **Good.** DAgger for compounding error; masked normalization; decisiveness-weighted KL; like-for-like raw input; paired per-seed comparison at equal latency.
- **Bad / risks.** Direct Jev imitation (datasets, weights and driver); n=10; search gain depends on an exact cheap simulator. Intermediary (OpenRouter) terms Unknown.
- **Borrow.** DAgger, masked normalization and decisiveness weighting with a permitted teacher (planner, flood-fill oracle, outcomes). The "don't train, search" exit when an exact simulator exists.

### 3.3 `github:sophiamyang/fireworks-jev-reward-rl` — uses Jev outputs (RL reward)
- **Revision.** HEAD `6a75d0d5` (2026-09-23T20:31:47Z), node `R_kgDOUn3JVA`, created 18:02Z. **First sighting** (no trace in origin/main).
- **Inspected.** README; `docs/RESULTS.md`, `LESSONS.md`; `experiments/scale-v1/*` (README, REWARD, manifest, build_dataset, sources, train.jsonl); `raw-base-v1` config and contract; `src/fw_jev/{reward,rl_math,calibration,runner}.py`; model README.
- **Backbone / head.** Qwen3.8-27B on Fireworks, rank-8 LoRA; generative writer, no classifier head.
- **Output / calibration.** Generated text; reward is a Jev-derived scalar in [0,1], "not a probability of human authorship". No calibration of Jev scores against humans; a 16-draft, 21-check preflight (2 checks cannot fail).
- **Data and labels.** 96 train / 24 eval prompt-only fictional inputs, no SFT or preference targets. **Reward from Jev 1.13.0** via api.typesafe.ai: style, quality and, on source-bound prompts, unsupported-claim support; reward = ((style+quality)/2)·support, zeroed if P(unsupported) ≥ 0.90. Group-relative advantages, KL β 0.05, 24 updates.
- **Provenance evidence.** README:5-6 "those scores become the RL reward"; `reward.py:15-16` model `jev-1.13.0`, endpoint `/v1/systemone`; `contract.json`: "Same Jev for training and evaluation".
- **Eval (Reported).** Jev reward 0.583 → 0.759 on 24 prompts × 2; words −39.8%; 20 of 24 prompt means rose. The same Jev scored training and evaluation; the baseline is a separate saved run; the eval suite was already inspected. 896 Jev requests, about $0.061 (local arithmetic matches the request count).
- **License / compute / runs on.** MIT; adapter unpublished. Hosted Fireworks CUDA; 72 minutes.
- **Good.** API failures halt the run rather than becoming zero-reward negatives; fail-closed consistency check; frozen reward version; success contract frozen before sampling; documented length bias.
- **Bad / risks.** Judge = reward = evaluator (Goodhart); length fell 40% while quality slipped. Whether §2.3(b) reaches reward use (not imitation) is Unknown; "facilitate" is the only possible hook.
- **Borrow.** The integrity patterns, and the rule that an optimizer's signal cannot also score the evaluation. **Doctrine gap:** RL reward, preference pairs and reward-model targets are not in trainer-recipes §2 rule 1 (see §6).

### 3.4 `github:bet0x/decision-jef` (= `hf:BarraHome/Decision-Jef-0.1`) — unclear
- **Revision.** GitHub `d3414109` (2026-09-23T20:58:05Z, "0.6.0"), node `R_kgDOUl30DQ`, 14 commits in about 29 h. HF `83aefb4a`. First card (patrol-gfs row only). Upstream `tasksource/tasksource-jev-typed-decisions` is carded (§167/§168, A15) and its sha moved to `01cf47f3`.
- **Inspected.** README; HF_CARD.md; `decision_jef/model.py`; `verify.py`; metrics.json; upstream tasksource cards and builder files (`build_jev_dataset.py`, `recast.py`, `synthetic/annotate.py`, `synthetic/configs/openai_luna.yaml`).
- **Backbone / head.** jhu-clsp/mmBERT-base (307M), fine-tuned. Query from h[DEC] against keys from h[OPT_i], cosine × learned scale; questions isolated by masks and position restarts; score = probability-weighted level.
- **Output / calibration.** Softmax over supplied options only. Raw ECE 0.010 in-distribution; optional per-(type, cardinality) temperatures (off by default).
- **Data and labels.** Part tasksource-jev-typed-decisions (license other; labels inherited from source datasets per its card), part tasksource/procedural-jev (rule-computed), the rest "generated for this project" (20,000 rule-labelled ViZDoom reports described; the support-decision slice undisclosed). No training code released.
- **Provenance evidence.** README:535-537 disclaims third-party "weights, gradients or private data" but not API outputs. tasksource's synthetic config names `annotator: jev` while `annotate.py` is still a heuristic stub, so a latent Jev-annotation path exists upstream.
- **Eval (Reported).** typed-decisions test (2,000; gold = unnamed teacher): 77.30 global; ECE 0.010. Gold slot-position bias: slot 3 holds 39.7% of choice gold vs 23.3% uniform. Accuracy falls from 0.915 at 5 options to 0.625 at 65. ViZDoom 37.4% → 99.4% on a held-out set from the same rule format (rule recovery, not live play). Option-order change rate stated as both 5.5% and 5.7%.
- **License / compute / runs on.** MIT code and weights; upstream `license: other` unreviewed despite a "commercial-use" tag. Training compute undisclosed; H100 fp32 ~12 ms for 1–4 questions; CPU plausible (Hypothesis).
- **Good.** Runtime option space; exact question isolation; permutation harness and slot-bias disclosure; OOD lesson (a confident constant answer on an unseen state format, with in-distribution ECE giving no warning).
- **Bad / risks.** Incomplete provenance and no training code; weights mutated in place under a fixed "0.1" name; a future tasksource release with real Jev annotations would contaminate downstream models.
- **Borrow.** The runtime-options readout as an R3 head candidate; permutation test plus gold-slot histogram as a required eval; a few dozen known-answer cases in the target state format before trusting confidences. Pin the HF sha if ever evaluated.

### 3.5 `github:Manavarya09/verdict` — unclear
- **Revision.** HEAD `39e4a09a` (2026-09-23T20:14:12Z), 34 commits in one day, node `R_kgDOUnZciA`. First card (patrol row only). At least 8 name-similar "verdict" repos are different sources.
- **Inspected.** README; docs (TRAINING, RESEARCH, PLAN, LAUNCH, API); `src/verdict/{distill,heads,core,cli}.py`; calibration modules; `train/{data,train,finetune_typed}.py`; bench and results files; the typed-decisions card.
- **Backbone / head.** intfloat/multilingual-e5-small (118M) bi-encoder; logit = cosine × 20. Heads: none, prototype, or L-BFGS logistic regression initialized at the zero-shot solution; then one temperature and a split-conformal set; abstain = set size > 1.
- **Output / calibration.** Label, temperature-scaled probability, conformal set. Temperature and qhat fitted on the same slice. **Empty LAC sets are replaced by top-1 and counted as commits** (`conformal.py:72`, `core.py:287`), so the lowest-confidence items commit when accuracy exceeds target coverage.
- **Data and labels.** Four paths: user labels (`fit`); `verdict distill traces.jsonl` on any logged (input, answer) rows with no labeler field; a 134,680-row public human-labelled mix for verdict-small-v0 (including research-only XNLI and Amazon reviews); and heads/fine-tunes on LocalLLaMA/typed-decisions gold.
- **Provenance evidence.** The README calls typed-decisions test labels "labelled by Jev"; the dataset card @c76749ec says gold is "the mean of three samples from a teacher endpoint of roughly 4B-class capability" and "does not reproduce their Jev model". Heads were already trained on that gold (the 0.6245 row). `distill` on Jev traces would be a §2.3(b) use.
- **Eval (Reported).** Banking77 zero-shot 0.594, 16-shot 0.860, full 0.920; CLINC150 0.536 / 0.928 / 0.953. typed-decisions heads 0.6245. verdict-small-v0 held-out mean 0.4856 → 0.5935 but Banking77 fell 0.580 → 0.524, so its own gate 1 is unmet. Checkpoints were selected on test rows.
- **License / compute / runs on.** Apache-2.0 code; research-only data inside the "open" encoder. Heads under a second on laptop CPU; encoder about 2–3 h on Apple M5 MPS. CPU, MPS, CUDA, browser (ORT Web).
- **Good.** The cheap R2 rung (frozen encoder, logistic head initialized at zero-shot, temperature, conformal set) with strong 16-per-class intent results; option-order invariance; losing rows published.
- **Bad / risks.** Abstain inversion; test-set checkpoint selection; mean-based gate hides a per-suite regression; random split on time-ordered logs; nominal L2 shrink.
- **Borrow.** R2 recipe, with fixes: an empty set = abstain; temperature and qhat on disjoint slices; selective risk reported separately; selection on validation only; gate on every suite. A `distill` step needs a per-row labeler field that refuses Jev, a time split, and the name "agreement with the logged model".

### 3.6 `github:anyforge/ruhui` — unclear
- **Revision.** HEAD `cdfc526e` (2026-09-23T10:00:22Z), 5 commits; HF `anyforge/ruhui` `9260e9d2`. First card; parent Laya is A17.
- **Inspected.** README, NOTICE, pyproject, `scripts/{prepare_train_data,train,predict}.py`, `ruhui/{common,agent}.py`, tests grep, HF card and configs, ModelScope API.
- **Backbone / head.** jhu-clsp/mmBERT-base (322M with head), not initialized from Laya weights; Laya type injection, 2-layer decision head, [MASK] option slots, act head.
- **Output / calibration.** Jev-shaped answers; confidence = 1 − H/log k. Per-type temperatures fitted on `all_items[::15][:400]`, a sample of **training** items; runtime clamp [0.5, 5.0].
- **Data and labels.** `datas/soft_*.jsonl` from "30+ domain datasets"; datasets, licenses and the producer of the soft probabilities are unpublished. Loss: soft cross-entropy plus REINFORCE over Gaussian logit perturbations with a proper-score reward.
- **Provenance evidence.** README:95 "RLCD + soft distillation"; the row schema carries source_dataset/index/hash but no teacher field; no Jev, TypeSafe or hosted-API mention; the HF author has no datasets and ModelScope declares none.
- **Eval.** None reported; the card's `scripts/evaluate.py` is absent from GitHub. 5,121 ModelScope downloads (observation).
- **License / compute / runs on.** Apache-2.0 (Laya fork); teacher terms Unknown. 4.97 h on one device per the config; CUDA, MPS or CPU.
- **Good.** Per-row source fields; temperature clamp; one bilingual checkpoint.
- **Bad / risks.** The "RL" term injects self-noise against a differentiable reward and adds no outcome information; in-sample calibration; a config `training` block the shipped script never writes, so the script is not shown to have produced the weights.
- **Borrow.** The row schema, extended with required labeler identity, a terms field and a Jev-exclusion check; the clamp as a guard. Do not use as a base until the teacher is identified.

### 3.7 `github:adimyth/compass` — no Jev outputs (hosted-drafter caveat)
- **Revision.** HEAD `2cd378d9` (2026-09-23T12:47:27Z), 67 commits; release compass-0.2.0 = Qwen3.5-4B @`851bf6e8` + `hf:adimyth/compass-lora-v2` @`bfa8af07`. First card (patrol row only).
- **Inspected.** README, CLAUDE.md, EXPERIMENTS, bench-request, stage-b-v2 specs, `train_lora.py`, `data/v2.py`, release cards, per-row provenance tallies of every train/split/shadow file, per-item public-check records.
- **Backbone / head.** Frozen bf16 Qwen3.5-4B + rank-16 LoRA on attention, linear-attention and MLP projections (116 MB). No new head: a verification readout (yes/no log-odds per candidate) fused in log space with a direct letter readout; KV cache prefilled once and forked.
- **Output / calibration.** /v1/systemone wire format, deterministic. One temperature per type (2.0/2.0/2.25) fitted after design freeze on a "hard-like" split introduced after the public hard-tier ECE was seen (mild adaptive risk).
- **Data and labels.** 2,150 training items: 1,900 code-generated with code-computed gold (300 with count-derived soft targets), 250 drafted. Loss: listwise CE through both readouts, ordinal term, symmetric-KL permutation consistency, opaque-label substitution.
- **Provenance evidence.** `train_lora.py:28-33` targets come only from item provenance or `expected`; no api.typesafe.ai call; README:82 no JevBench item used; JevBench is reached only through its own adapter pointed at the local server. **Caveat:** 270 training items and all 280 shadow items are `claude-drafter-*` outputs (hosted-provider terms Unknown), and the shadow suite breaks its own "human-authored, never committed" protocol.
- **Eval (Reported).** JevBench public hard 63/111 → 67/111 (ECE 0.107 → 0.069). Local paired arithmetic on committed records: 21 gained / 12 lost overall, exact McNemar p = 0.163; hard p = 0.54; Wilson 95% for 60.4% is [0.511, 0.690]. Shadow 66.4% → 76.4%, but adequacy regressed.
- **License / compute / runs on.** Apache-2.0. RTX 4090 (RunPod) CUDA; MPS works through reference kernels (1.6–3.5 s p50 frozen).
- **Good.** Train through the serving readout (no train/serve skew); order- and label-name-robust losses; code gold; disjoint splits by template, domain and language; pre-registered promotion; all non-promoted variants reported; n-gram overlap check.
- **Bad / risks.** Generator-evaluator coupling through the drafted shadow suite; missing data/PROVENANCE.md; non-significant public deltas; the adequacy regression was promoted anyway.
- **Borrow.** The promotion scaffold and the readout-level losses; make the shadow set really independent and record drafter identity and terms per item; report paired tests.

### 3.8 `github:DejaAI2/JevNext` (data: `DejaAI2/MiniJev`) — no Jev outputs
- **Revision.** JevNext `fabcd2e1` (2026-09-23T02:54Z, imported history); MiniJev `be718a5d`. First cards for both.
- **Inspected.** JevNext README, train.py, calibrate.py, checkpoint config and logs, reports; MiniJev README, `minijev/data.py`, holdout_eval.py, split tallies over all 8,700 rows.
- **Backbone / head.** Qwen3-0.6B (Instruct or Base), frozen bf16, rank-16 LoRA on 196 projections (10.3M trainable); last-token LayerNorm+Linear scalar per candidate, then a set-attention head across candidates.
- **Output / calibration.** /v1/systemone plus OpenAI-compatible generation on the same weights (LoRA toggled off). One global temperature fitted on the OOD split, which is also reported as an evaluation number; T ≈ 0.95.
- **Data and labels.** MiniJev's seeded, stdlib-only rule generator (8,700 states, ~18.6k questions); gold from the rules; 45 hand-written holdout cases (102 questions).
- **Provenance evidence.** `minijev/data.py:1-4` "Gold labels are derived deterministically"; imports only argparse/json/random/pathlib; no API calls in `jevnext/*.py`. The patrol's "generator unnamed" is corrected.
- **Eval (Reported).** Holdout: MiniJev 58.8%; Base+LoRA 91.2%; the shipped Instruct adapter 86.3% (Wilson local [0.783, 0.916]); McNemar Base vs Instruct p ≈ 0.27; seeds disagree on 11 questions; some per-task n of 5–7. In-distribution 0.997 (saturated).
- **License / compute / runs on.** MIT. About 50 min on an M4 32 GB (MPS); CPU and CUDA via device pick.
- **Good.** Controlled "swap only the model" comparison with McNemar and seed noise; `selected_on` recorded.
- **Bad / risks.** Saturated synthetic metrics; tiny author-written holdout; calibration split doubles as an eval split; headline is not the shipped checkpoint.
- **Borrow.** A seeded rule generator as a Jev-free smoke test; the controlled comparison; never quote rule-generated accuracy as real-text evidence.

### 3.9 `github:mrmps/hotdog` (HF `opensporks/hotdog-27B`) — no Jev outputs (OpenAI-teacher caveat)
- **Revision.** GitHub `5a75c7e2` (formerly mrmps/tinker-binary, same node); HF `0a49cd7e`. First card (patrol row only).
- **Inspected.** README, NOTICE, train.py, binary_model.py, data pipeline (build, audit, compositional, import_kev), protocol and candidate configs, evaluation scripts, reproducibility and results JSONs, HF card.
- **Backbone / head.** Qwen3.8-27B dense, rank-16 LoRA, LM-token readout: logprob("B") − logprob("A"), p_yes = sigmoid; inputs over 8,192 tokens rejected.
- **Output / calibration.** Scalar P(yes), binary only. No post-hoc calibration; selection by lowest dev Brier within 1 pp of best dev accuracy. ECE 0.58% in-family vs 11.95% on 74 public JevBench items.
- **Data and labels.** 13,017 unique rows: ~9,280 Kev decision-v7 public rows kept only if a blinded gpt-4.1-mini auditor agreed; 1,854 gpt-4.1-mini generated-and-audited rows; 1,881 code-computed procedural rows. Group-disjoint splits, 5-gram near-dup quarantine.
- **Provenance evidence.** README:100-101 JevBench evaluation-only; `train.py:18-19` refuses paths outside `data/` or under `evaluation`; every TypeSafe call is in evaluation/serve code. **Caveat:** `evaluation/development.py:52-60` loads sealed Jev predictions on the DEV split and emits paired comparisons per candidate, so Jev outputs were visible during selection (not labels, but a "facilitate" question). OpenAI output terms Unknown.
- **Eval (Reported).** In-family holdout 1,631: 98.28% vs Jev 97.30%, +0.98 pp [+0.19, +1.79], concentrated in mnli/agnews/banking77. Public JevBench 74: 81.08% vs 83.78%, −2.70 pp [−12.20, +5.63]. "It does not establish a JevBench win."
- **License / compute / runs on.** Apache-2.0; mixed dataset licenses including "unknown". Hosted Tinker training (16 runs, 661 steps); H200 CUDA inference; not a Mac recipe.
- **Good.** Trainer path allowlist; preregistered protocol and failure-mode list; blinded auditor as filter; AST minimal-pair oracles; paired cluster bootstrap with "lower CI bound > 0" as the criterion; one frozen candidate scored once.
- **Bad / risks.** Generator and auditor from one model family, so the holdout is "rows gpt-4.1-mini is sure about"; in-family win does not transfer; comparator predictions on the selection split.
- **Borrow.** The allowlist, selection rule, blinded-auditor pattern (with a teacher of known terms, never Jev) and paired bootstrap. Rung R4.

### 3.10 `github:javimosch/mtlm-router` (HF `javimosch/mtlm-7m-router3s384`) — no Jev outputs (noul/score heads unknown)
- **Revision.** GitHub `fc4756f6` (2026-09-22T22:15Z), 8 commits; HF `7521ebd7`. First card.
- **Inspected.** README, MODEL-CARD, PRODUCT, `tools/{synth_tools,train_head,gen_routespec,head_studio,calibrate}.py`, hosted-API grep of all tools, HF siblings.
- **Backbone / head.** A 7.2M-param Llama-compatible decoder trained from scratch in MFL (int8 8.06 MB); three linear heads (route softmax, noul escalate, score 1–4) on the last hidden state, fit by numpy logistic regression; a generative JSON path; delegation on low confidence, escalate, or head/generation disagreement.
- **Output / calibration.** A distribution over a fixed trained route set; noul/score answer fixed questions only. Temperature grid-searched on a 20% validation slice, then the head refit on train+val with that T. ECE 0.012 on the synthetic holdout; `calibrate.py` can bucket real traffic from logs.
- **Data and labels.** 30,000 seeded template conversations; the route label is the generator that produced the text; hand-listed escalate and garbage classes; TinyStoriesV2-GPT4 used only as chat filler. Noul/score head label spec unpublished (Unknown).
- **Provenance evidence.** `synth_tools.py:194` generator list; `train_head.py:20` label = `expect_tool`; demos call a localhost server; no typesafe.ai reference.
- **Eval (Reported).** Route 97.6%, noul 98.9%, score 97.9% on the same generator with a different seed; head-generation agreement 100% (self-consistency); ~15 ms on a 6-core LXC.
- **License / compute / runs on.** Apache-2.0 (machin-anvil license Unknown). CPU serving (linux-amd64 static binary); head training plausibly minutes on CPU (Hypothesis).
- **Good.** Phrase-config → labelled spec → ~7 KB linear head on a frozen trunk; duplicate-stem refusal across routes; explicit OOD class; two-channel disagreement gate; calibration from production logs.
- **Bad / risks.** Template-recall holdout; exact-string-only leakage filter; a 7M classifier plus a short hand list as the guard on shell and email tools (detection, not authorization).
- **Borrow.** An R1/R2 phrase-config head with validation and a trained escalate class. Require a different generator or real traffic for holdouts.

### 3.11 `github:Artid1994/JEV_Concept-hermes-agent-router` — unclear (anti-pattern)
- **Revision.** HEAD `f1f27946` (2026-09-22T18:23Z); one file, README only; no license; no HF artifacts. First card.
- **Inspected.** README, repo API, tree, commits, author repos, HF search.
- **Backbone / head.** Qwen2.5-1.5B-Instruct, Unsloth LoRA, GGUF q4_k_m through Ollama; generative JSON, no head.
- **Output / calibration.** `{"action": execute_tool | reject, ...}`; no probabilities; no calibration.
- **Data and labels.** Not stated anywhere; no dataset, notebook, adapter or GGUF published.
- **Provenance evidence.** README:3 says only that Qwen was fine-tuned with Unsloth; "JEV" appears only in the name. No evidence either way.
- **Eval.** None measured; "~0.22 s" and "Strict JSON 100%" claims.
- **License / compute / runs on.** None (all rights reserved). Nothing published to run.
- **Good.** The pre-filter-plus-fallback idea only.
- **Bad / risks.** A generated "reject" presented as a security gate; tells users to bind Ollama to 0.0.0.0 without auth; nothing reproducible.
- **Borrow.** Nothing; cite in the skill's "what a decision head is not" section.

### 3.12 `github:nagisanzenin/nagi` — no Jev outputs (documented lineage only)
- **Revision.** HEAD `838eae07` (2026-09-23T18:56Z), 8 commits in 7 h; SDK 0.2.1; HF nagi-big-v3 `0357e819`, big-v0 `04e0b881`, smol-v0 `6d842eed`. The research repo `nagisanzenin/nagi-research` returns 404. First card.
- **Inspected.** README, CHANGELOG, RECIPES, CALIBRATION, VALIDATION, bench docs V0–V5 and receipts, `modal_bench5.py`, `model.py`, `render.py`; four HF cards and small config files.
- **Backbone / head.** Smol: ModernBERT-large state encoder + per-option tower + MLP score head (421M, variable K). Big v3: Qwen3.5-4B mixed-rank LoRA (r64 attention from the private G-clean, r16 linear-attention/MLP), letter-logit readout; K > 26 rejected.
- **Output / calibration.** Choice distribution, expected Score level, Noul P(true). Big v3 temperature 0.849 fitted by NLL on 537 separate calibration examples; docs require raw and calibrated ECE/Brier/NLL and say there is "no universal safe threshold".
- **Data and labels.** Big v3: 5,999 public labels + 6,000 executable-oracle examples, initialized from private G-clean. Big v0: "Soft-distilled from teacher ensemble (DeepSeek flash + GPT-5.6-Luna)". Smol v0 teacher unnamed.
- **Provenance evidence.** v3 `selection.json`: "All final JEV predictions remain sealed. No final scoring has informed this selection"; Jev is only a benchmark arm (`modal_bench5.py:206-250`). Gaps: G-clean data, hail-C generation, Smol KD teacher.
- **Eval (Reported).** V3 sealed finals vs jev-1.13.0: public 75.80% vs 91.40% (−15.6 pp), executable policy 68.19% vs 84.51%. V2: fine-tuning bought about +1 pp on language tasks and +18 pp on executable rules over the frozen base. V5 matched ablation: +4.25 pp [+0.58, +7.83], one seed, failed its transfer gates. The v0 gold_ltout table is withdrawn (QQP mislabels, demo leakage) but still shown on stale HF cards.
- **License / compute / runs on.** README says Apache-2.0 but no LICENSE file; v3 weights inherit Qwen's license. Modal H100 training; Smol CPU inference verified on macOS; Big CUDA only.
- **Good.** Withdrew its own headline; preregistered gates with a noninferiority margin; sealed finals; research gate separate from release decision; clean matched ablation; frozen-base arm; failures counted as wrong.
- **Bad / risks.** Private lineage; v0 soft-distilled from hosted LLMs with Unknown terms; single seed; post-hoc v3 release choice.
- **Borrow.** The V5 matched-ablation template, the noninferiority gate, the `final_predictions_opened` selection record, and the frozen-base baseline arm.

### 3.13 `github:Mr-Neutr0n/laya-session-guard` (HF `hxrikp/laya-session-guard-pilot`) — no Jev outputs
- **Revision.** HEAD `963269db` (2026-09-22T08:22Z), 3 commits; HF `d8f65c3c`, weights sha256 `4b37300e…` match the run manifest. **First sighting.**
- **Inspected.** README, MODEL_CARD, all `src/*.py`, Kaggle notebook sources (byte-compared to src), data metadata, reports, label counts, GitHub compare, HF commits and tree, Laya base card.
- **Backbone / head.** convaiinnovations/laya English (ModernBERT-large + Laya head, ~421M), full fine-tune; two Choice questions (content, action) plus a fail-closed wrapper returning review on incomplete or oversized input.
- **Output / calibration.** Two distributions plus a wrapper decision; "not suitable for automatic tool authorization". Per-question temperature grid [0.5, 5.0] on 96 calibration sessions: **the fine-tune chose T = 0.5 for both, the grid floor.**
- **Data and labels.** 480/96/144 template sessions with labels hard-coded per case; a 24-session agent-authored challenge set (eval only).
- **Provenance evidence.** `session_data.py:88-109` hard-coded labels; `train.py:99` only data source; HF server timestamps put weights (07:21:41Z) before the first Jev call (07:37:34Z); data files unchanged after the Jev commit. **But** `reports/jev_template_results.jsonl` holds Jev probabilities for the whole template test split beside the training data.
- **Eval (Reported).** Template test 100%/100% (uninformative). Challenge: fine-tune 70.8% / 54.2% vs Jev 95.8% / 95.8%; suspicious recall 4/11 vs 11/11; action ECE 0.457; paired bootstrap Jev − fine-tune +41.7 pp action [20.8, 62.5]. Single seed.
- **License / compute / runs on.** Apache-2.0. One Kaggle T4, 301.7 s; training CUDA-only, inference CPU.
- **Good.** Separate content and authorization questions; fail-closed wrapper that refuses truncation; hash-cached comparator calls with request_sha256 and returned-model check; template and challenge results reported together.
- **Bad / risks.** Shared generator logic across splits; grid-floor temperature; the action gain is mostly deferral; Jev outputs co-located where a future retrain could glob them.
- **Borrow.** The provenance receipt (commit data and weights, then call any comparator, record hashes, store outputs on a path the trainer never reads); falsifiers for same-generator holdouts, grid-boundary temperatures and deferral-driven gains.

### 3.14 `github:MoLeMo-Lab/mojev` — no Jev outputs (Open-Jev revision unpinned)
- **Revision.** HEAD `a74d58cd` (2026-09-23T21:15:51Z, one squashed commit); HF model `0c8695b6`, dataset MoJev-Mix `424bc3ea`. **First sighting.** Upstream Open-Jev (A3) inspected at `3308a15c`.
- **Inspected.** README, ROADMAP, CHANGELOG, `mojev/{openjev,balance,wikiqa,full,calibrate,evaluate,serve,apitest}.py`, tests, preprint text, HF cards, datasets-server statistics, 2,996 OOD rows, Open-Jev generator files.
- **Backbone / head.** Qwen3.5-0.8B fully trained; TreePacked attention (state, questions and candidates in one sequence under a tree mask); rank-512 projection, one scalar utility per candidate; grouped Plackett-Luce over graded candidates plus Brier.
- **Output / calibration.** Per-field softmax over request-time candidates; /v1/systemone wire-compatible. Brier at training; no temperature in the serve path.
- **Data and labels.** MoJev-Mix: 507,974 rows from 18 deterministic Open-Jev generators (labels = generator argmax; grades from graph distance, RGB bands, ordinal gaps or a rule-priority table), capped per source by supervision depth.
- **Provenance evidence.** Dataset card "derived from 18 synthetic Open-Jev generators"; Open-Jev label bases are deterministic rules, exact geometry, BFS/minimax teachers and SQL equivalence; its only HTTP callers are eval policies. Verified against Open-Jev HEAD, not the unpinned revision MoJev ran.
- **Eval (Reported).** 93.23% top-1, ECE 0.79% on 12,000 decisions **pooled** from test and OOD. Per split (400-item test subset vs OOD): accuracy at 100% coverage 94.50 vs 82.50; error-detection AUROC 0.975 vs 0.682. **The "held-out generators" OOD claim is false:** all 13 source names in the first 2,996 OOD rows are training sources. 4-way visual P(cat) reported inconsistently across README and project page.
- **License / compute / runs on.** MIT (Qwen license applies to the checkpoint). One epoch on 8 GPUs of about 180 GB class, 47 min. MPS/CPU code-possible; browser ONNX export.
- **Good.** Grades from recoverable structure; reduces exactly to CE without grades; per-source caps; shuffled-context null; invariance checks; served-vs-in-process probability test.
- **Bad / risks.** The priority grading ranks opposite verdicts as nearest misses; pooled headline; synthetic, in-family data; `trust_remote_code`; squashed histories.
- **Borrow.** The graded-preference schema with PL+Brier; supervision-depth caps; served-vs-in-process check. Add semantic review of every grading rule, per-split metrics only, and a source-id listing per split before any "held-out generator" claim.

### 3.15 `github:samdoom-coder/Snapjudge` (HF `Brutalsky111/Snapjudge`) — no Jev outputs
- **Revision.** HEAD `34ac0694` (2026-09-23T23:27Z); HF `e64838fc`; HF source files byte-identical to GitHub. **First sighting.** Different from Micha0827/snapjudge and cendress/SnapJudge (§100).
- **Inspected.** README, run_train, `snapjudge/{data_gen,train,common,router,agent}.py`, bench.py, Space README, HF card, metrics, config.
- **Backbone / head.** answerdotai/ModernBERT-base (149M) fully fine-tuned + a from-scratch 2-layer decision head, option-marker scorer, act head (~165M).
- **Output / calibration.** Typed per-game outputs; confidence = 1 − normalized entropy. Temperatures per (type, K-bucket) fitted on the val pool (all chose 1.5), **and the reported "held-out" ECE 0.049 is computed on the same pool**; it doubles to 0.096 on fresh seeds.
- **Data and labels.** 6,000 synthetic games; labels from exact rules (minimax, collision check with greedy food distance, a 72-state obstacle table); tied optima share mass; trapped Snake states get random labels.
- **Provenance evidence.** `data_gen.py:3` "All labels are computed by exact rules ... no LLM teacher needed"; no hosted-API calls.
- **Eval (Reported).** Val pool: strict 0.905, ECE 0.049 (temple-run 1.000, snake 0.939, tic-tac-toe 0.772). Fresh-seed re-check: tie-aware 0.949, ECE 0.096; choice strict 0.79. Temple-run's 72-state space is split randomly by example, so 1.000 is memorization.
- **License / compute / runs on.** Apache-2.0. About 1 h on a T4; CPU inference.
- **Good.** Exact-solver labels; uniform targets over tied optima; tie-aware and strict accuracy reported.
- **Bad / risks.** In-sample calibration; entropy "confidence" used for ECE; duplicate states across splits; the "RLCD" policy-gradient term is multiplied by 0.0.
- **Borrow.** As a counterexample fixture for eval gates (same split for temperature and reported ECE; entropy-based ECE; no state dedup before a random split); plus exact-solver labels for game-like domains.

### 3.16 `github:beratcmn/qwen3.5-0.8b-systemone` — no Jev outputs (trains nothing)
- **Revision.** HEAD `1568b321` (2026-09-21T21:14Z), 6 commits; base Qwen3.5-0.8B pinned `2fc06364`. **First sighting.** The README is a 3.5 KB API document, not "a name only".
- **Inspected.** README, BENCHMARKS, pyproject, engine.py, scoring.py, training-term grep across src/scripts/tests.
- **Backbone / head.** Frozen Qwen3.5-0.8B (with vision path); no trained head. Criteria rendered as a label table; next-token logits after "Answer:" restricted to verified single-token labels (255 verified at startup); shared-prefix KV cache with batched question branches.
- **Output / calibration.** Softmax over label-token logits; Noul "true" is always label A; confidence = 1 − normalized entropy. No calibration and no order debiasing.
- **Data and labels.** None: no optimizer or backward call anywhere.
- **Provenance evidence.** `engine.py:28-29, 101-117` load and `eval()` only; no typesafe/jev/openai/anthropic references.
- **Eval (Reported).** Latency only: RTX 3060, 4 questions 1393.7 → 359.1 ms with shared prefill and batched branches; 50 questions 1003 ms.
- **License / compute / runs on.** No license. CUDA only (raises without a GPU).
- **Good.** Single-token label verification; prefix KV sharing.
- **Bad / risks.** Uncalibrated letter readout with unmeasured position bias; no accuracy evaluation; no license.
- **Borrow.** As an R0/R1 frozen-readout baseline; require permuted averaging and a held-out temperature before comparing it with a trained head.

---

## 4. Comparison matrix (the 16 carded recipes)

Rungs follow `trainer-recipes.md` §6 (R0 don't train … R5 generalist). "Not
stated" in the ROCm column means no card reports a ROCm run or claim; nothing
here supports a ROCm "yes". Apple entries cite only what the source says or
measured.

| Recipe | Rung | Backbone | Head / readout | Labels · Jev provenance | Calibration (split) | Eval evidence (Reported) | Train compute | CUDA / Apple / CPU / ROCm | License |
|---|---|---|---|---|---|---|---|---|---|
| StevenJPx2/jev-distill | R2 | none (hashed n-grams) | multinomial LR + abstain | Jev answers only · **uses** | none; fixed abstain threshold | n=25: 60% agreement, 60% vs agent-written gold | ~2 s, 75 rows | – / measured on Apple Silicon / yes / not stated | MIT |
| Adamya05/jev-echo | tiny policy | 22k-param CNN | masked log-softmax | Jev soft labels + DAgger · **uses** | none | 10 games: ties Jev; +search wins 9/10 | ~30 s | – / MLX required (M4) / MLX CPU / not stated | MIT |
| sophiamyang/fireworks-jev-reward-rl | n/a (writer) | Qwen3.8-27B | LM + LoRA r8 | Jev scores as RL reward · **uses** | none vs humans | Jev reward 0.583→0.759 (Jev also the evaluator) | 72 min hosted | hosted / no / orchestration only / not stated | MIT |
| bet0x/decision-jef | R3 | mmBERT-base 307M | DEC-query × OPT-key cosine | tasksource mix + undisclosed slice · unclear | optional per-(type,K) T; off | 77.30 typed-decisions (teacher-agreement gold) | not disclosed | H100 / not stated / plausible (H) / not stated | MIT; upstream `other` |
| Manavarya09/verdict | R2 (+R3 encoder) | multilingual-e5-small 118M | cosine or LR head + T + conformal | user / public / typed-decisions gold · unclear | T and qhat on the same slice; empty set commits | Banking77 16-shot 0.860; own gate 1 unmet | heads <1 s; encoder ~2–3 h | yes / MPS measured (M5) / yes / not stated | Apache-2.0 (research-only data inside) |
| anyforge/ruhui | R3 | mmBERT-base 322M | Laya option slots | 30+ unnamed soft-label sets · unclear | per-type T on **training** items | none | 4.97 h, 1 device | yes / MPS code path / yes / not stated | Apache-2.0 |
| adimyth/compass | R4 | Qwen3.5-4B frozen + LoRA r16 | fused verify + direct LM readout | code gold + Claude-drafted items · no (drafter terms Unknown) | per-type T on a hard-like split | public hard 63→67/111, McNemar p=0.54 (local) | RTX 4090 | yes / MPS eval via reference kernels / – / not stated | Apache-2.0 |
| DejaAI2/JevNext | R4 | Qwen3-0.6B + LoRA r16 | scalar + set-attention head | seeded rule generator · no | global T on OOD split (also reported) | 102-q author holdout 86.3% (shipped) | ~50 min | yes / MPS measured (M4) / yes / not stated | MIT |
| mrmps/hotdog | R4 | Qwen3.8-27B + LoRA r16 | A/B logit difference | Kev public + gpt-4.1-mini gen/audit + code · no (OpenAI terms Unknown) | none; Brier-based selection | in-family +0.98 pp; JevBench-74 −2.70 pp | hosted Tinker, 16 runs | H200 / no / – / not stated | Apache-2.0 |
| javimosch/mtlm-router | R2 | 7.2M decoder from scratch | 3 linear heads on last state | template generator · no (noul/score heads Unknown) | T on 20% val, then refit | 97.6% same-generator holdout | not stated | – / untested (H) / yes (serving) / not stated | Apache-2.0 |
| Artid1994/JEV_Concept-hermes | – (anti-pattern) | Qwen2.5-1.5B + LoRA | generated JSON | not stated · unclear | none | none | not stated | – / – / – / not stated (nothing published) | none |
| nagisanzenin/nagi | R3 (Smol) / R4 (Big) | ModernBERT-large 421M; Qwen3.5-4B | option tower; letter logits | public + oracle (v3); v0 DeepSeek/GPT soft targets · no (documented lineage) | T=0.849 on 537 separate items | v3 public 75.8% vs Jev 91.4% | Modal H100 | yes / Smol CPU inference on macOS / Smol / not stated | Apache-2.0 claimed, no LICENSE |
| Mr-Neutr0n/laya-session-guard | R3 | Laya (ModernBERT-large) | Laya option markers ×2 + fail-closed wrapper | template constants · no | T at grid floor 0.5 | challenge 70.8/54.2% vs Jev 95.8/95.8% | T4, 302 s | yes / not stated / inference / not stated | Apache-2.0 |
| MoLeMo-Lab/mojev | R4/R5 | Qwen3.5-0.8B full | tree-packed candidate utility | 18 Open-Jev rule generators · no (revision unpinned) | Brier at train; no T | pooled 93.23% / ECE 0.79%; OOD 82.5% | 8×~180 GB GPUs, 47 min | yes / code-possible / code-possible / not stated | MIT |
| samdoom-coder/Snapjudge | R3 | ModernBERT-base 149M | Laya-style option markers | exact solvers · no | T fitted on the reported split | 0.905 in-sample; ECE 0.049 → 0.096 fresh | T4, ~1 h | yes / not stated / inference / not stated | Apache-2.0 |
| beratcmn/qwen3.5-0.8b-systemone | R0/R1 baseline | Qwen3.5-0.8B frozen | restricted label-token softmax | none · no | none | latency only | none | yes / no / no / not stated | none |

**Read-across.** Few carded recipes fit calibration on a split separate
from both training and the reported evaluation: nagi (537 items), compass (a
hard-like split chosen after the benchmark was seen), laya-session-guard
(which then hit its grid floor) and mtlm-router (a validation slice, after
which the head is refit on train+val). Only 4 report training on Apple
hardware (jev-distill, jev-echo, verdict, JevNext), all small models. None
reports ROCm.

---

## 5. Mechanisms: good and bad patterns across the field

**M-a. Label circularity is the dominant defect.** It takes three forms.
- *Teacher = evaluator*: `fireworks-jev-reward-rl` (the same Jev rewards and
  scores); `StevenJPx2/jev-distill` (selection maximizes agreement with the
  teacher; "gold" written by the building agent).
- *Generator = evaluator*: `hotdog` (gpt-4.1-mini generates and filters both
  train and test, so 98% means "rows that model is sure about"); `compass`
  (the same drafter family writes training items and the shadow suite);
  `JevNext`, `mtlm-router`, `laya-session-guard`, `MoJev` (holdouts from the
  same generator or rules; MoJev's "held-out generator" OOD is false).
- *Unnamed-teacher gold presented as truth*: at least ten ids in this window
  train on LocalLLaMA/typed-decisions, and about seven near-identical Laya
  fine-tunes on its train split report beating the 0.735 "teacher ceiling",
  which is agreement with an unnamed ~4B endpoint; `verdict` calls the same
  gold "labelled by Jev".

Good counter-patterns: labels from code (Nimble-style rules, AST minimal
pairs in hotdog, exact posteriors in certo and `Maverick-Ansh/jev-from-scratch`),
exact solvers (Pikafish, Mortal, BFS, minimax), live environments
(`abedinia/laya-web-agent` checks the live page; `chemany/jeva` drives real
Chrome), maintainers' own triage (`laya-issue-triage`), git history
(`tindang/laya-code`, kotoba code-holes), and realized outcomes
(`Society-Harness-`, `reflex-mlx`). All Reported.

**M-b. Jev-output use has more shapes than "distillation".** In this window
(Reported instances; contract effect Hypothesis until counsel):
- labels or soft targets, 17 trained models, including transitive use
  through a corpus (`JEV-mini`, `autotrust/JEV`, and the `von` path all
  inherit SargeDev v3's 498,010 Jev-labelled rows);
- **RL reward** (`fireworks-jev-reward-rl`, `Bring-AI/jev-rl`), which the
  current barred-use list does not name;
- features (`fly-lint`, `doorman`, `Jev-Flywheel`, and TypeSafe's own
  autoresearch cookbook, which trains CatBoost on Jev answers: **Contract**
  that the vendor documents this pattern);
- selection and quarantine (`jev-curate`, `jev-dataops`,
  `adampippert/granite-decisions-synthetic`, where Jev decided which
  rule-labelled rows were excluded);
- optional teacher paths hidden in otherwise clean projects (`gavel`'s
  `label_with_jev.py` against a "public human labels" README; `circuit`'s
  "never by another model" banner against a Jev+Gemini soft-target trainer);
- the access channel is often OpenRouter's `typesafe/jev-1.13` alias
  (jev-echo, gavel, Shalimov04, omkarghugarkar, SargeDev v3, RenaGao), so a
  gate keyed on `api.typesafe.ai` alone would miss them.

Contract-aware patterns worth copying: `integrallis/models` (the rule in
types and a bytecode test), `hyprstream-synthesis` (rows from any
"api-prohibited" teacher marked non-distributable), `s1decide` (a data-licence
gate ADR), `sokudan` (did not measure Jev, citing §2.3(b)), `clduab11/jev-test`
(67,312 raw Jev records kept local, aggregates only), `Worthify-AI` (a
per-component license table that excludes Jev labels), and cards that forbid
training on stored predictions (`Vineethsain`, com-kotobalabs).

**M-c. "Not Jev" is not "clean".** At least ten recipes train on other hosted
models' outputs: gpt-4.1-mini (hotdog), Claude drafters (compass,
`mghafiri`, `michaljach/jet`), DeepSeek and GPT-5.6-Luna (nagi v0), GLM
(eikos, distil-labs), Gemini (circuit's other half, gutcheck's benchmark),
OpenRouter-hosted gpt-oss and Qwen (Akicou, KoJev), and a GPT-5.6-sol capture
corpus (zenjev). Their output terms are Unknown here. Plan-v3 §3.6 already
routes hosted teachers through the gate; the field shows how often that gate
will fire.

**M-d. Synthetic data works as a smoke test, not as confirmation.**
Rule-generated in-distribution scores saturate (JevNext 0.997); a model
trained on templates can hit 100% on the template test and fail authorization
on a hand-written challenge (laya-session-guard 4/11 suspicious sources);
MiniJev reports 42% UNK on human phrasing. `dwidlee/systemone-lite` found
37–91% train/eval state overlap and rebuilt; `Snapjudge`'s 72-state space
cannot be split randomly. An LLM filter can be badly wrong: `agentculture/nvsh`
found its reviewer wrong on 10 of 13 checked rejections.

**M-e. Calibration claims are the weakest numbers in the field.** Observed
defects: temperatures fitted on training items (ruhui) or on the reported
split (Snapjudge; JevNext's OOD split); a temperature at the grid floor
(laya-session-guard, T = 0.5); ECE computed on entropy "confidence" rather
than P(correct) (Snapjudge; beratcmn's readout); pooled test+OOD ECE (MoJev
0.79%); in-distribution ECE that misses OOD failure (hotdog 0.58% vs 11.95%;
decision-jef's confident constant answer); temperature and conformal
threshold on one slice, with empty sets committed (verdict); a calibration
split chosen after seeing the benchmark (compass). Good practice: separate
calibration sets (nagi 537, andyshu 510), `mogita` needing about 500 labelled
rows per task to move ECE from 21.4% to 6.5%, and `bdauzats` warning that
MLX 4-bit shifts probabilities by up to ~0.3, so a calibrator is bound to
precision as well as model. All Reported.

**M-f. Benchmark overfitting is common and mostly disclosed by the careful.**
Checkpoints selected on test rows (verdict); curricula designed after
inspecting public JevBench (`jsaurabh`; llm-shield calls itself
"public-benchmark-directed"); a JevBench split leak fixed in `bandr-ai`.
Counter-patterns: one frozen candidate scored once (hotdog), sealed finals
with a `final_predictions_opened` flag (nagi), per-item contamination flags
(`SamuelChien821/typed-decision-bench`), a withheld 40-task split
(AIMultiple), and the family holdout (`andyshu/opensysone`: +8.42 pp on known
families, +2.60 pp [0.13, 5.34] on a held-out family).

**M-g. Transfer evidence keeps pointing the same way as M3/M4.** Fine-tuning
bought about +18 pp on executable rules and +1 pp on language tasks over the
frozen base (nagi V2); at 0.6B, full fine-tuning, 4B-teacher distillation and
a 149M encoder "all tried and all lost" (tinyjev); a generic typed-decision
mix lowered unseen Banking77 (verdict); an in-family win did not carry to
JevBench (hotdog). Teacher quality matters less than gold: `lafalce` reached
Banking77 88.5% with human gold plus a teacher that tops out at 56%;
`marcmagn1` found that blending a weaker LLM judge into soft targets cut
coverage (35.5% → 28.8% at 5%); `vagmi/jev-lite` found teacher entropy 0.000
with thinking on vs 0.211 off, so soft-label teachers need reasoning off;
`sshah03/shrewd` found better teacher labels did not always improve the
student. All Reported.

---

## 6. Implications for the trainer skill

Targets: `research/080/trainer-recipes.md` (TR) and
`research/080/plan-v3.md` (P3). Nothing here edits either file. Labels:
**Contract** (text of the MCA or the vendor's docs), **Reported** (a
third-party source's own claim), **Hypothesis** (a design rule not yet
tested or reviewed by counsel).

### 6.1 Add

| # | Change | Where | Label | Evidence |
|---:|---|---|---|---|
| 1 | Add **RL reward, preference pairs, reward-model targets, and teacher relabels of student-visited states (DAgger)** to the barred Jev uses | TR §2 rule 1; P3 §3.6 edges (add `rewarded_by`, `preferred_by`, `relabeled_by`) and test table | Hypothesis (counsel: does §2.3(b) reach non-imitation reward use?) | fireworks-jev-reward-rl, Bring-AI/jev-rl, jev-echo DAgger (Reported); `whilehq/whileai-sdk` skill accepts `typesafe:<model>` as a judge with no warning that judge verdicts used as rewards or SFT filters are training use |
| 2 | Extend the **barred-corpus list** and add a field-level screen | TR §2 rule 4; P3 §3.6 "barred" list | Reported | SargeDev v3 (498,010 of 740,957 rows Jev 1.13, Apache-2.0 card), DGUI_HYPERMEM-JEV (still growing), Jevsus (~210,000 calls), jevals-data (CC-BY logs), dylantom2012 bench, Vineethsain board, com-kotobalabs repo-governance `prediction` field, adampippert `jev-audit/`. Transitive consumers: JEV-mini, autotrust/JEV, von's distill path. A card license never clears MCA use |
| 3 | New **gate test fixtures from real items** | P3 §3.6 test table | Hypothesis | Row quarantined by a Jev confidence gate → refused (granite-decisions-synthetic); Jev via the OpenRouter alias `typesafe/jev-1.13` → refused (gavel, jev-echo, Shalimov04); corpus row with a Jev `prediction` field → field stripped or row refused; trace log with no labeler field → `unknown` (verdict `distill`); upstream corpus with a configured-but-stubbed Jev annotator → `unknown` until the release is checked (tasksource `openai_luna.yaml`) |
| 4 | **Comparator isolation in code**, not prose: comparator outputs live on a path the trainer cannot read, are never loaded on the selection split, and are recorded with request hash, pinned model and timestamp after data and weights are committed | TR §2 rule 2; P3 §3.4 table and §3.5 hard gates | Hypothesis | hotdog `train.py:18` allowlist (good) but `development.py:52-60` loads sealed Jev dev predictions per candidate (bad); integrallis `ExternalArmIsolationTest`; laya-session-guard receipt (good) with Jev outputs shipped beside training data (bad); clduab11 keeps raw rows local (Reported) |
| 5 | **Evaluation-hygiene hard gates** in the climb ledger, each with a scenario | P3 §3.5 "probes and floors are hard gates"; §3.7 as S16–S22 | Hypothesis | S16 calibration split = reported split → fail (Snapjudge, JevNext); S17 temperature at a grid bound → flag (laya-session-guard 0.5); S18 ECE computed on entropy "confidence" → metric rejected (Snapjudge, beratcmn); S19 pooled test+OOD headline → per-split required (MoJev); S20 "OOD"/"held-out generator" claim without per-split source ids → fail (MoJev, mtlm-router, JevNext); S21 checkpoint chosen on test rows → fail (verdict); S22 empty conformal set counted as a commit → abstain (verdict) |
| 6 | **Data-protocol rows**: semantic review of any grading rule (no opposite verdict as a near miss); state-space dedup before any random split; calibrate a judge or filter on known-good and known-bad probes before a full pass; time-ordered split for logged traces; labeler identity and terms required per row | P3 §3.4; TR §6 synthetic-data rules 8–12 | Hypothesis | MoJev rule-priority grades; Snapjudge 72 states, dwidlee 37–91% overlap; nvsh reviewer wrong on 10 of 13; verdict random split on logs; ruhui/verdict rows lack a labeler field (Reported) |
| 7 | **Soft-label teacher rules**: reasoning off when reading a teacher distribution; teacher cross-entropy only where the teacher is stronger or agrees with gold; the student can beat a weak teacher when gold is present | TR §6 rule 5; TR §3 M8 | Reported | vagmi/jev-lite (entropy 0.000 vs 0.211); marcmagn1 blend hurt coverage; lafalce 88.5% vs teacher 56% |
| 8 | **Precision binds the calibrator**: record precision and quantization with the temperature and refit after any change | TR §3 M2; P3 §3.5 calibrator identity | Reported | bdauzats: MLX 4-bit moves probabilities up to ~0.3; decision-jef ±0.15 bf16 noise |
| 9 | **"Search with an exact simulator"** as an R0 exit next to the reasoning exit | TR §6 R0 row | Hypothesis (Reported n=10) | jev-echo: Echo+search beat the teacher 9/10 at equal latency, because Snake rules predict the next board exactly |
| 10 | **R2 variants** worth naming in the runtime `recipes` reference: frozen multilingual encoder + LR head initialized at the zero-shot solution + temperature + conformal set (with the S21/S22 fixes); phrase-config linear head on a frozen trunk with a trained escalate class | TR §6 R2 row; P3 §3.3 | Reported | verdict (Banking77 16-shot 0.860); mtlm-router (~7 KB heads, CPU) |
| 11 | Cite **bandr-ai/bandits #73** as the closest outside analog, and note where it differs: optional Jev column (P3 keeps comparators a maintainer decision), a "95% CI excludes zero" gate (P3 uses EB non-inferiority), and label-source plus license gating of datasets | P3 §3 intro; TR §5 | Reported | issue #73 and the feat/jev docs at `e6bf6524` |
| 12 | **ROCm acceptance check for Qwen3.5 linear attention**: the M5 R1 arm uses Qwen3.5-2B, whose DeltaNet layers needed flash-linear-attention on CUDA (compass) and reference kernels on MPS (compass, Kev); add a linear-attention parity and speed probe to the §4.4 tests, with Qwen3-1.7B (attention-only) as the fallback R1 model | P3 §4.4; §4.5 M5 row | Hypothesis | No carded recipe reports ROCm; compass's MPS path is 1.6–3.5 s p50 on reference kernels (Reported) |

### 6.2 Sharpen (decisions for the maintainer or counsel)

- **Features vs replacement.** TypeSafe's own cookbook trains a CatBoost model
  on Jev answers used as features against dataset labels (**Contract**: the
  vendor documents the pattern; sha `00ee0cff…`, unchanged at
  2026-09-24T00:05Z). TR §2 rule 1 bars features. Add to P3 decision 11 and
  TR §9 Q1: does §2.3(b) distinguish a feature model that keeps Jev in the
  loop from a model built to replace it? Default stays **exclude** until
  answered (Hypothesis). doorman, fly-lint, Jev-Flywheel, jevaiguide and the
  anth.us post all use or recommend the feature shape.
- **"Similar or competing product."** Many recipes ship a `/v1/systemone`
  drop-in server (decision-jef-serve, compass, MoJev, jevons, JevNext). An
  Augustus skill that emits Jev-shaped servers sharpens TR §9 Q1c; record
  whether the skill's outputs should avoid the Jev wire format by default.
- **Refusal wording.** The most repeated public advice is "log your Jev calls
  and distill them" (seangoedecke, mcftira/jev-route's "Run it. Log it.
  Distill it. Own it.", verdict `distill`, anth.us). P3 S7 should quote that
  request shape and redirect to outcome labels, human adjudication, code
  labels or a local permissive teacher. `IgorGanapolsky/ThumbGate`'s
  "compare, do not clone" skill is a working example of the redirect.
- **Hosted non-Jev teachers.** M-c shows the §3.6 hosted-teacher gate will
  fire on most community recipes. Decide whether 0.8.0 checks any provider
  terms beyond TypeSafe, or ships every hosted teacher as `unknown` with a
  named-approval path.

### 6.3 Replace or reject

- **Reject as sources of labels:** LocalLLaMA/typed-decisions gold (unnamed
  teacher; at least ten derivatives in this window) and the
  tasksource Jev-native share, both `unknown` in the gate until the teacher is
  identified (Reported).
- **Reject as recipes:** every item in §2a class T and P as a data source;
  ruhui (unknown teacher, in-sample calibration); MoJev and compass as
  generalist defaults (in-family evidence; M3 holds); Artid1994 (no data, no
  eval). Keep jev-echo and jev-distill only for their teacher-agnostic
  mechanisms.
- **Do not cite:** `wunderlandmedia` for current terms (it quotes the Aug 27
  MCA's §2.3(f), absent from the Sep 19 version); stale HF cards of nagi v0
  (withdrawn benchmark); pooled or in-sample calibration numbers.
- **Replace** TR §6 R1's evidence note "reflex, SemIf, AnyJev" with the same
  plus a warning that an unaveraged letter readout (beratcmn) is only an R0
  floor until order averaging and an out-of-fold temperature are applied.

### 6.4 What the sweep does not change

The ladder order (R0 → R4, R5 never default), the M5 pre-registered rule,
EB non-inferiority at 1 pp, and "no Jev output in any training path" all
stand. Nothing in 298 items supplies a controlled comparison that would move
a rung; the new evidence is about gates, provenance shapes and evaluation
defects.

---

## 7. Limits

- Lane R's default repository search covers name, description and topics;
  three `in:readme` queries were truncated at 1,000. Lane H searches repo ids,
  not card text. Lane C searched first pages only and left five queries
  untriaged. jev.magicteams.ai (1,362 builds) was not enumerated. Projects
  that never use "jev", "laya", "kev", "system one" or similar tokens are
  under-sampled.
- About 70% of items were read at README or card depth only; only 16 were
  deep-inspected. Most "unclear" verdicts mean the label source was not
  stated in what was read, not that it is hidden.
- "Uses" for the six runnable-path items (class P) means the path exists;
  whether shipped weights used it was not verified.
- Dedupe matches slugs, not hosts, and "notes §N" means named, not
  necessarily carded.
- All third-party metrics are Reported and unreproduced. Stars, likes and
  downloads were observed and not used.
- Provenance verdicts are readings of repository text, not legal advice.
