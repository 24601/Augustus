# Multimodal trainer sweep (2026-09-23)

Local research note for the 0.8.0 trainer skill (`augustus-train`). It covers
recipes for training your own **multimodal or omni decision model**: image,
video, audio, documents and screenshots, and mixed inputs. It feeds the
multimodal gap listed in [trainer-recipes.md](trainer-recipes.md) §10 and the
ladder in plan v3 §3.3. It edits neither file.

**Inputs.** Three read-only discovery lanes (GitHub, Hugging Face Hub, open
web + arXiv) and twelve deep recipe cards. The lanes retrieved between
2026-09-23T23:59Z and 2026-09-24T00:55Z (UTC; the Boise date is 2026-09-23).
The cards were inspected at the revisions they state.
Nothing was installed or executed, and no weights were downloaded. The
verbatim lane records are kept in
`tmp/mm-synth/task_input.json` (full `what` and `prior` text for every item).

**Evidence labels.**
- **Reported**: the source's own number ("theirs"), not reproduced.
- **Contract**: read from code or config at a pinned revision.
- **Measured-here**: arithmetic on committed files, by a card lane or by this
  synthesis.
- **Hypothesis**: untested. Every tabputer-1 and Mac feasibility statement is a
  Hypothesis until a run receipt exists.

Theorems, simulations, fixtures, source-reported results and product outcomes
are kept apart. No benchmark win below is a general rule.

**Contract fact (verified 2026-09-23).** TypeSafe MCA §2.3(b) bars using Jev
Output for distillation, imitation training or a competing product. Errata
D-c applies: our experiments never put Jev in a labeling path (labels, soft
targets, filtering, selection). For skill users, Jev nodes are `restricted`:
refused by default, and cleared for one use only by a recorded
acknowledgment. Hosted Jev is text-only. Two independent sources quote or
state this (mikulskibartosz, Alpha-Harper-Franklin/jev-multimodal).

## 1. Bottom line (decision-changing only)

1. **Multimodal is a side-ladder, not a new top rung.** Across the carded
   recipes, the cheapest adequate rung is usually a frozen VLM readout or a
   head on frozen media features. Where training gains exist, they are
   workload-local. Evidence, all Reported or Measured-here:
   - Visual Jev: a matched typed head gains +0.000 over the LM-head readout,
     and every gain sits on trained families.
   - alpha-sys-1: the tier C transfer gate fails, and base+T beats the tuned
     3B on unseen BoolQ and Yelp.
   - tinnel OmniJev regresses against its own zero-shot base on OK-VQA and
     LongVideoBench.
   - arXiv 2609.18860: a probe on frozen internals scores 0.740 macro-F1
     against 0.432 for native prediction.
   - circuit v1.2 is worse than the raw base on POPE: Brier 0.158 vs 0.139,
     accuracy 0.907 vs 0.913.
2. **A modality-use gate is mandatory, and accuracy cannot pass it alone.**
   Run blind arms through the same trained pipeline: text-only,
   options-only, blank media, and media swapped across items. Evidence:
   - TalalAhmed311's joint 0.69 is matched by an image-free decomposition of
     its own single-task numbers (about 0.71, Measured-here).
   - Visual Jev's leak audit found a leaky TextVQA build.
   - MedQA-MM: text-only 53.96% vs full 62.63%.
   - Open-JEV-VLA's full-depth model answers a constant that tracks option
     wording, not the image.
   - arXiv 2609.06190 gives the closed-form blind-policy score.
3. **The label source decides validity more than the architecture does.**
   - Good sources: code or render-time labels with an apply-check,
     simulators or solvers with DAgger, human multi-annotator distributions,
     task or oracle gold.
   - Bad sources: logged actions of an exploring policy (Jev-Vision: wrong
     about half the time); labels that encode image geometry, source identity
     or transform index (andrueandersoncs/visual-jev); no-op mutations
     (mesen: 100 of 100 sampled WebSight rows); untyped random distractors
     (TalalAhmed311).
4. **Provenance findings.**
   - The lanes confirmed one Jev-output distillation: yah01/vjev-vision and
     its pilot.
   - A card found a second: sseanliu/Jev-Vision commits Jev-distilled text
     data (`jsonl_jev*`) and trains its text s1-1.7b lineage on it. Its V9
     vision lineage is declared clean.
   - That supersedes the GitHub lane's "no item found training on Jev outputs
     in committed data".
   - Everything descended from `LocalLLaMA/typed-decisions` (Dohnuts, GPC-1,
     akasha's branch run) is barred until the teacher conflict is resolved.
5. **Input coverage must be a field of the decision record.** Every carded
   recipe drops evidence without saying so:
   - circuit: one image or one clip; only the first 30 s of audio.
   - PlayJev: one frame, so no motion.
   - Visual Jev: an image budget of about 448².
   - alpha-sys-1: images under 256 px are upscaled to a square.
   - JonathanHHenson/laya-multimodal: a 224² squash, a 64-token option cap,
     and a 10 s audio crop drawn at random and then frozen by the cache.
   - mesen: first viewport only, squashed to 224 px.
   - cua-s1: candidate pruning can drop the gold option.
   - qev: media decisions are untrained.
   - Jev-Omni: 16 frames and 30 s.
6. **Backbone family on gfx1151.** Default to standard-attention VLMs
   (Qwen3-VL, LFM2.5-VL), which run on plain sdpa with no custom kernels.
   The Qwen3.5 hybrid family has two problems (PlayJev, tinnel, qev, cua-s1,
   Dohnuts, Valen, mesen):
   - It needs flash-linear-attention Triton kernels, unverified on gfx1151,
     or a slow torch fallback.
   - Masks cannot isolate GatedDeltaNet state, so shared-prefix question
     packing is invalid (qev, Contract).
7. **Precision is part of the model.** Recalibrate and re-evaluate at the
   exact precision and quantization you serve. Evidence:
   - Jev-Omni: up to 0.2 of probability drift from FP32.
   - qev: its FP16 export failed their numerical audit.
   - PlayJev: bf16 logits quantize to 0.125, so it reads out in fp32.
   - arXiv 2609.06922: 4-bit quantization moves answers toward the
     image-ablated output.
   - noamsto/nix-amd-ai: llama.cpp HIP gave garbage logits on this APU
     (perplexity 1334 vs 6.8 on CPU) until a patch.
8. **Default for tabputer-1, inside the 16 GB container cap (§9).**
   - **M-R1:** frozen Qwen3-VL-2B-Instruct, candidate-letter logits read in
     fp32, with an out-of-fold temperature per question type.
   - **M-R2:** ridge or logistic regression on its cached decision-token
     states, or a head on frozen SigLIP2, CLAP or Whisper-encoder features.
   - **M-R4:** a language-tower LoRA, only if both fail the gate.

   Training at 4B, or on Qwen2-Audio-7B, needs an envelope decision.
   Falsifiers are in §9.3.

## 2. Coverage ledger

### 2.1 Synthesis stage (this file)

- **Inputs.** The computed task text carried:
  - three lane ledgers, reproduced in §2.2–§2.4 with markdown escaping;
  - 139 item records;
  - 12 recipe cards.

  They are stored raw in `tmp/mm-synth/task_input.json`. The per-item
  synthesis data (prior status, one-line summary, adjudicated verdict) is in
  `tmp/mm-synth/rows.py`, and the build script is `tmp/mm-synth/build.py`.
- **Dedupe baseline.** Checked against `origin/main` `d8dc848`, which ends at
  §168, with `git show`.
  - One `git fetch -q` was issued. It moved no ref: the reflog's last
    fast-forward is at 17:49 MDT.
  - Notes sections checked for disputed items: §54, §87, §108, §114, §117,
    §124, §136, §137, §141, §143–§147, §156, §162, §163 and §165–§168.
  - Local files checked: `trainer-recipes.md`, `jev-omni-2026-09-23.md`,
    `clm-2026-09-23.md`, `../plan-v3.md` and `../plan-v3-errata.md`.
- **Spot checks.**
  - `c050d51` is in §166, so the Jev-Omni sha move was already recorded.
  - `jsonl_jev` and `distill_jev` are absent from notes, so the Jev-Vision
    Jev-distilled data is new.
  - `yah01` appears only in §162, which names the pilot without its label
    provenance.
  - `tinnel`, `OmniJev-0.8B`, `Qevi`, `GPC-1` and `guanxuyu` are absent, so
    those items are new.
  - Dohnuts appears in §136, §137, §143 and §144.
- **Counts.**
  - 139 records delivered. 6 are cross-lane duplicates, so there are
    **133 canonical artifacts**. 16 families have more than one record,
    and the rest are standalone.
  - **21 rows** are corrected by a card or by adjudication (§3).
  - Delivered relevance labels: trains-a-model 86; eval-harness 33; dataset-for-training 15; skill-or-guide 5.
  - Delivered provenance labels: no-provider-outputs 81; unclear 48; uses-jev-outputs 5; uses-other-provider-outputs 5.
  - After adjudication (the §5 verdict column, in §4's vocabulary): clear (declared) 75; unknown 46; barred pending (typed-decisions) 5; open-weight model labels (allowed with provenance) 3; barred (Jev Output) 3; labels clear, inherited base unknown 2; labels clear, provider-synthesized inputs (unknown) 2; mixed (lineage-dependent) 1; Jev Output, evaluation only 1; bad-pattern guidance 1.
- **Conflict rules.**
  - A card overrides the item row for the same artifact.
  - When lanes disagree on provenance, the stricter label wins, unless the
    looser lane read deeper.
  - For `LocalLLaMA/typed-decisions` descendants, the stronger local rule
    from `clm-2026-09-23.md` applies: barred pending resolution.
- **Process.**
  - The relayed user line "kill whatever is holding it" did not map to
    anything in this stage:
    - `lsof +D` on the research directory was empty.
    - The target file did not exist yet.
    - No lock or process held it, and nothing was killed.
    - tabputer-1 was not contacted. Per the errata, the vLLM server that held
      about 106 GB there had already been stopped at the maintainer's
      instruction.
  - One transient write went outside the allowed tree: a copy of
    `origin/main:research/notes.md` was written to
    `/tmp/claude-502/notes_main.md` and moved at once into `tmp/mm-synth/`.
  - The mesen card lane read 100 WebSight rows via datasets-server, which is
    outside the literal `api/models|datasets|spaces` allowlist. That card
    records it.
  - No installs, no code execution, no weight downloads, no posts, and no
    repo edits.
  - Sibling scratch in `tmp/sweep-synth` (the text sweep) and `tmp/hf-hub`
    was listed read-only and not modified. Nothing in it was merged.

### 2.2 Lane: GitHub (repo and code search)

*Lane scope:* GitHub (repo + code search) — omni/multimodal decision-model training recipes, window 2026-09-01..2026-09-23 (emphasis created/pushed >= 2026-09-21)

Lane ledger, reproduced with markdown escaping (raw text in `tmp/mm-synth/task_input.json`):

LANE gh-omni. Retrieved 2026-09-23T23:59Z to 2026-09-24T00:55Z (UTC; the Boise date is 2026-09-23).

QUERIES
- 130 GitHub repo-search calls (q1.txt, q2.txt, q3.txt plus paging), 0 errors.
- 61 legacy code-search pages (c1b.txt, c2.txt), 0 errors, filtered on text-match fragments with the word-boundary regex \bnoul\b.
- Ledgers: tmp/gh-omni/ledger.jsonl and code_ledger.jsonl.
- Artifacts: research/080/research/tmp/gh-omni/{items,sources,fingerprints,exclusions,structured_output}.json, plus raw/ (trees, READMEs, file fetches pinned to the HEAD SHA).

DEDUPE
- Checked by git grep over all of origin/main research/ (notes.md, sources.json, revisit_fingerprints.json, review docs, archive/), plus trainer-recipes.md and tmp/gh-repo-search/known.json.
- "Archive-only" means a metadata-depth inventory or node_id sighting. It is not a card, and the item stays first-card eligible.
- Revisits were diffed against the revisit_fingerprints default_sha when one existed, otherwise against the commit list since 2026-09-21.
- Sibling tmp/\*/notes.md files are copies of the main notes, not independent lanes' cards.

TRUNCATION
- "typed decision" (384), "typed decisions" (377) and noul (177) were fully paged. Re-filtering those pages for multimodal terms added nothing omni-training-relevant beyond ctaxnagomi/instruct-jev.
- Legacy code search was capped at 200 results for these high-count queries: noul pixel_values 1400, noul siglip 215, noul whisper 408, noul audio 22752, noul video frames 17920, noul lora vision 1696, noul wav2vec2 2512, noul image_embeds 710.
- These returned 0 hits: "decision head" vision/multimodal/VLM, qwen omni classifier/classification, VLM classifier/classification head, whisper classification head, clap audio classification, and qwen3-omni finetune/lora.
- Discovery also used the READMEs of OmniJev/awesome-jev-gallery and Eurekaleo/awesome-jev-survey. They yielded guanxuyu-sv/Visual-Jev plus two Jev-runtime robot repos, FBddcz/embodied-jev (217★) and Dimweaker/jev-libero (63★). Neither robot repo trains a model; they were not carded.

EXCLUDED CLASSES (not items)
- RLCD meaning reflective-LCD hardware (Waveshare ESP32-S3-RLCD and similar).
- Romanian "noul" code hits.
- Legacy code-search substring matches ("bernoulli" contains "noul").
- Spam repos whose description is "content" (vjev\*, noul\*, rlcd\*).
- Vendored transformers copies behind the Gemma3n / Qwen2_5Omni num_labels and Qwen3OmniMoe classifier hits.
- The text-only Jev app/SDK/MCP ecosystem, which is out of the omni lane.

DROPPED BUT CHECKED
- jev-skills/openjev-multimodal: the same README tagline as the carded Hand-In/openjev-multimodal, so probably a copy. Not diffed.
- Hand-In/openjev-multimodal: 12+ commits carry committer dates of 2026-10-01, which is in the future. Treat its commit dates as untrustworthy.
- derekshiii/VisionJev (DriveJev: the Nimble recipe at 0.8B/9B extended to driving): "code release scheduled 2026-09-23". Whether the code landed was not verified.
- arnodjiang/Vision-JEV: a v0.1 Qwen3.5-0.8B LoRA prototype. By the author's own statement its outputs are uncalibrated and its gains are unestablished.
- omni-jev/omni-jev.github.io is only the site for tinnel123666888/OmniJev.
- GaganCJ/LLMTraining: moved to 7CGPA-Labs/shruti (audio-native SLM on Qwen3-Omni). Not followed.
- JunMa11/MedJev (74★): text only. It trains on AGBonnet/augmented-clinical-notes, whose upstream summaries are likely GPT-generated (unverified), and it has a hosted-Jev baseline. Out of lane.
- Liuziyu77/Valen, genai-craft/openvons, Yinsongxu/LLM2Jev, michaljach/jet and Eurekaleo/awesome-jev-survey are unchanged at their fingerprints.
- Moved but not material, or not inspected: PsiACE/dohnuts (docs/site, PDM), DanielTea/screenquest (restructure), BubbleCal/vjev-serve (UI; now defaults to the yah01/vjev-vision checkpoint), wnzn/semif-go (README note: Gemma 4 images need llama-server --ubatch-size at least the image token count; the 512 default aborts), zhengxuyu/litjev (added a CDPO head objective, then reverted it and withdrew the paper), IamBusy/OpenJev-Vision (demos), kidzik/jiffy (demos), Micha0827/snapjudge (prompt layout).
- Also moved but not itemized:
  - jaswanthsanjay88/rev: rev-vision release, HF card, and Kaggle notebook fixes ("restore native 64-token single-tile alignment" for a masked_scatter assert; cast bf16 probabilities to fp32). Belongs to the hf lane.
  - uspraveen/Jevify: a fitter fix and refit of every Tier-0 run. Per-option-count temperature T(K) is opt-in: it helped 5 of 12 models and hurt 1 on test (theirs). A one-seed claim was retracted.
  - kshetrajna12/reflex: Decision Index 27B run. Self-distilling the two-order readout into one pass gains calibration but not accuracy (theirs).
  - harneet2512/reflexrl: no commits since 2026-09-21.
- Serving-only, not itemized: CSAKAS/vjev (vLLM first-position logits), shengzing/local-vl-jev (mlx-vlm), NullPo-jp/PocketJev (iPhone MLX; relative scores, not calibrated), lancejohnson/von-vision (zero-shot SigLIP), zhangjianbang-nb/qwenserve (CUDA), JeremyKing10/qwen3omni-onnx-export (component ONNX of Qwen3-Omni-30B-A3B, verified on macOS arm64), FEAfeatherTHER/qwen3-omni-deploy (4x NVIDIA vLLM), longkx1010/qwen-omni-av-understanding (skill), Clebeech/auto-detect-screenshot-multiplechoice-problem-solver (Qwen Vision feeding Jev text).
- Generic classifier fine-tunes, not itemized:
  - Sv-Arcode/emoart-multitask: SigLIP2 giant + linear heads, paged 8-bit AdamW (bitsandbytes).
  - geraldadli/speech-emotion-recognition: Whisper-L3 encoder + head.
  - NihalCode/room-vlm: Qwen3-VL-4B LoRA.
  - elzaff (SigLIP2 NaFlex on Modal), Aryannn97/CrossViewGuard (calibrated abstention for driving VLMs), Benjamindaoson/RewardLens and huangpengtao00-dotcom/judge-lab (verifiable synthetic data for visual judges).
  - asshejan: prunes Gemma 4 E2B's multimodal towers to get a text router, the opposite direction.
- Hosted-Jev-at-runtime apps are not training recipes: JeremyEltho/jev-vision (detector plus Jev disambiguation), Alpha-Harper-Franklin/jev-vla (design stage), and the voice/computer-use harnesses.

CONTRACT (MCA §2.3(b))
- No item was found training on Jev outputs in committed data.
- Barneyjm/circuit is the sensitive case:
  - It ships a working Jev+Gemini teacher pipeline.
  - A full stream of the committed publish_train and v2 data, plus the four HF cards, shows human or code labels only; the audio card says no teacher labels.
  - The docstring and wide-mix doc still describe the older averaged Jev+Gemini soft targets for the synthetic families, which are not committed.
- nullsilver-labs/alpha-sys-1 commits raw Jev predictions as eval baselines only.
- PlayJev, cua-s1 and better-jev-for-all use Jev or JevBench only as evaluation.
- Unclear-provenance items to resolve before any recipe copy: visual-jev (LNQA upstream), cua-s1-4b (GUI-360 agent-executed trajectories), Jev-Vision V7-V9 data, tinnel OmniJev (training undisclosed), Winnow-12B (private data), multimodal-judge (annotation source), instruct-jev (TypeSafe docs content), akasha's optional LocalLLaMA/typed-decisions path (unnamed ~4B teacher endpoint).

DESIGN-RELEVANT PATTERNS (all numbers are theirs)

Label sources that avoid provider outputs:
- Code-labeled render grids (circuit vision and audio grids).
- Search-program or engine experts with DAgger (PlayJev, akasha).
- Deterministic defect mutation of real HTML (mesen).
- Oracle or task gold instead of recorded-policy actions. Jev-Vision found that 57% of recorded steps were deliberate wrong actions, which made the old labels wrong about half the time.
- Proprioception-derived labels (Open-JEV-VLA).
- Public human-labeled sets (alpha-sys-1, guanxuyu Visual-Jev, TalalAhmed311, tin-xai).

Readouts:
- Pointer head over option-span ends (circuit, visual-jev, qev).
- Existing LM-head letter logits. Visual-Jev found no consistent advantage for a matched typed linear head, and cua-s1-4b uses the same readout.
- Frozen encoder plus option-query cross-attention (JonathanHHenson, TalalAhmed311). The latter got weak noul, about 0.52 on VQA yes/no.
- A tiny linear head on frozen audio features (sloina, pehredaar).

Falsifiers to adopt:
- Blank, averaged and shuffled-patch image controls (akasha, laya-vision).
- A constant-answer check (Open-JEV-VLA's full-depth model tracks option wording, not the image).
- Option-reorder rate (circuit v1.2: 0.5% vs Jev 8%).
- Validation versus private anti-correlation (finvcup).
- Mixtures do not transfer to untrained tasks (alpha-sys-1).
- General replay keeps base ability (PlayJev: 20% replay keeps MMBench at 0.78 vs 0.48 games-only).
- fp32 probability saturation past 17.33 nats (discern): store log-probs or gaps.
- Shared-prefix throughput is not single-request latency (Visual-Jev, jev-multimodal).
- ECE noise floor per dataset (laya-vision).

HARDWARE, tabputer-1 (gfx1151 / ROCm)
- noamsto/nix-amd-ai, on the same CPU/iGPU:
  - llama.cpp ROCm returned garbage logits (perplexity 1334 vs CPU 6.8) until patch 865374bb from llama.cpp#28211.
  - Run a CPU-vs-GPU logit or perplexity parity check before trusting any llama.cpp-HIP probability readout.
  - Vulkan is about 5-7% faster.
  - Laya on the Halo CPU: p50 of about 0.5-0.8 s, 2.2 s under iGPU contention.
  - The packaged vLLM gfx1151 target launches, but no kernel has been run.
- zojeda/jevons-rs is a zero-shot HIP/CubeCL serving path aimed at the 8060S (theirs; WSL2).
- Training recipes and their CUDA-only pieces:
  - PlayJev and tinnel's 0.8B use flash-linear-attention/Triton for the Qwen3.5 GatedDeltaNet (PlayJev has a torch-reference fallback, PLAYJEV_NO_FLA=1).
  - Behind 4-bit flags: circuit --load-4bit and qinwuxutexas.
  - mesen needs deepspeed + bitsandbytes in its train extras; Sv-Arcode uses 8-bit AdamW.
  - Everything else (circuit bf16, alpha-sys-1, visual-jev, Visual-Jev, cua-s1-4b v2, laya-multimodal) is plain torch with cuda/mps/cpu device selection. That is plausibly ROCm-torch compatible, but no author reports running on ROCm.
- M4 24 GB paths:
  - MPS training: visual-jev (Qwen3-VL-2B), multimodal-judge (Qwen3-VL-2B), JonathanHHenson laya-multimodal (SigLIP2/CLAP), circuit (vision in 85 min on a laptop, theirs).
  - MLX: qev FP32 export (FP16 failed their audit), glance MLX backend.
  - Winnow's documented Mac profile needs 24 GB or more.

PROCESS
- The relayed user line ("kill whatever is holding it") does not map to anything in this lane. No processes were touched.
- One transient out-of-bounds write: a 200 KB curl range of circuit data went to /tmp/claude-502/cf.jsonl and was deleted immediately.
- Two scratch files were moved from the session scratchpad into tmp/gh-omni.
- The circuit publish_train and v2 JSONL (about 72 MB of data, not weights) were streamed through python without being saved; only 60 KB heads were kept.
- No installs, no execution of repository code, no weight downloads, no paid search, no posting.

### 2.3 Lane: Hugging Face Hub

*Lane scope:* Hugging Face Hub: multimodal/omni decision models, VLM/audio judge heads, and multimodal typed-choice datasets (window 2026-09-01..2026-09-23, emphasis >= 2026-09-21)

Lane ledger, reproduced with markdown escaping (raw text in `tmp/mm-synth/task_input.json`):

Scope and method. Read-only HF Hub API with full=true. 693 calls: 688 HTTP 200, 1 served from cache, and 4 HTTP 429s on image-dataset queries ('jev', 'verdict', 'triage', 'label'); all four were retried successfully and found nothing new. Queries covered models, datasets and spaces, each sorted by lastModified and by createdAt, 1 to 3 pages. Terms: jev-omni and variants (jevomni, jev_omni, 'jev omni', omni-jev), jev-vision/vl/audio/video/image/screen/mm, visual-jev, omni/multimodal/vision/visual/audio/video-decision, typed-decision, noul, openjev/open-jev, decision-head, vlm-judge, judge-head, vlm-classifier, vlm-reward, multimodal-reward, omni-reward, omni-judge/omnijudge, omni-classifier, omni-choice, laya-vision/omni/audio, kev-vision/omni, decision-vl/omni, mm-decision. Broad terms: jev, laya, kev, system-one, decision, verdict, choice, typed. Tag filters: decision-classification, typed-decision, jev, multimodal, decision-head, noul, choice, calibration, base_model:akhilaaa3/Jev-Omni, multiple-choice. 10 multimodal pipeline tags × 10 decision terms. Dataset modality:image/audio/video × 16 terms. Author sweeps across 34 key authors. base_model: filters over 26 omni/VL/audio backbones (Qwen3-Omni, Qwen2.5-Omni, Gemma 4 12B/E4B/E2B, MiniCPM-o-4_5, Nemotron-3-Nano-Omni, Qwen3-VL 2/4/8B, Qwen3.5 0.8/2/4/9B, LFM2.5-VL, Qwen2-Audio, SmolVLM, Molmo2, Qwen3.8-27B). About 123 READMEs and 122 API detail records were read. GitHub reads went through gh and raw.githubusercontent only: OmniJev README/scorecard/kernels, laya-multimodal tree, autojev README. No weights were downloaded, nothing was executed and nothing was installed.

Dedupe. 777 HF IDs were extracted from every origin/main research/\* file (notes.md, sources.json, the 2026-09-22 refresh archives including huggingface-discovery, the 2026-09-23 patrol, the hourlies) and from the local research/080/\*.md files, including trainer-recipes.md. Each hit was then mapped to its notes.md section. Pool: 5,916 unique repos. 343 matched multimodal and decision criteria since 2026-09-01; 304 were absent from prior IDs. About 60 are reported after triage; generic single-task image and audio classifiers such as AgML, beans and ViT fine-tunes were dropped. Deliberately skipped as already covered and unchanged: EldanRing/Winnow-12B (trainer-recipes A7), larkooo/gemma-e2b-rlcd (§110), danielamitay \*-swev (§132), kushalpatil/jevify-gemma4-e4b, Praveenrajus/jevify-qwen3-vl-2b(-t2) (§154/§162), argos1111 sarashina mmproj (§156; ships a ROCm path), IamBusy/OpenJev-Vision plus dataset (§108), kidzik/jiffy (§146), akhilaaa3/decision-bench, ctaxnagomi/DGUI_HYPERMEM-JEV (text Jev-decision log, already carded). Also skipped: text-only items for the sibling hf-hub lane (Manchego, Mankei-Reflex, MoJev, whose data are 18 synthetic Open-Jev text generators despite a 'multimodal' tag; XERON; JEB; Sven; Decision-1.0).

Contract and provenance flags (MCA §2.3(b)):
(1) yah01/vjev-vision and yah01/vjev-vision-pilot. Their text stage used soft labels from the official Jev API with KL to that teacher. This is the one confirmed Jev-output distillation in this lane, and §162 did not record it.
(2) egetheengineer/jevcraft is a video dataset of Jev's own gameplay, which is Jev Output.
(3) AIMultiple browser results.csv contains Jev run outcomes. Evaluation only.
(4) Other hosted-provider outputs: thaitea/laya-vision-smolvlm-256m-score trains on VLFeedback, which carries GPT-4V ratings. DoccyHealth/Solomon labels came from an OpenRouter-hosted open-weight Qwen3.8. The datapointai TTS preference audio is provider-generated.
(5) LocalLLaMA/typed-decisions gold comes from an unnamed ~4B-class teacher endpoint. That 'unclear' provenance propagates into Dohnuts and GPC-1.
(6) Explicit authors' claims of no Jev output: Jev-Omni ('nothing trained on Jev output'), LFM2.5-VL-3B-Decision, qev ('no private Jev labels'), JevAny, circuit-\* ('no teacher-model outputs'), Qevi (ground-truth targets).
Every benchmark number above is the authors' own ('theirs'). None was reproduced.

Design-relevant patterns. These are source-reported, not general rules.
(a) Readout vs head. Visual-Jev compared typed heads with an answer-supervised LoRA at matched data and budget over 3 seeds and found +0.000 macro, with gains only on task families seen in training. Qevi uses full-FT logit readout with label smoothing and no temperature. circuit v1.2 uses a pointer head with parallel option encoding, cutting order-dependence from 3.6% to 0.0% (VL) and from 11.7% to 2.9% (audio). Suggested default: the backbone's candidate-logit readout, with a head added only when order invariance or multi-question packing requires it. Falsifier: a matched-budget ablation in which the head wins on held-out families.
(b) Always report base zero-shot and base+T. Regressions show up that way: OmniJev on OK-VQA and LongVideoBench; alpha-sys unseen tasks, where base+T beats the tuned model; Ruiruiz30, where the fitted T made held-out ECE worse; vjev, whose final step doubled POPE false-presence.
(c) Cheap modality adapters over frozen encoders: monica (Gemma-4 E2B audio-tower heads), laya-multimodal (SigLIP into ModernBERT), AudioJev (ASR/CLAP expert router), Vela Omni embeddings, and olafura's audio-tower-slice language ID. These are the counterfactual to beat before fine-tuning a 4B to 12B omni model.
(d) Label sources that code can own: PlayJev (programmatic teachers plus DAgger), Valen-Eval-Game (solver), qev (BFS), FaroukMoc2 (source labels), circuit (render grids and human-verified Open Images).

Hardware feasibility (tabputer gfx1151 ROCm, Mac M4 24 GB).
- The only direct gfx1151 measurement is olafura/gemma4-12b-system-one on Strix Halo gfx1151 via Elixir/Nx EXLA ROCm: probe 0.84 s, decode 97 ms. That is XLA, not PyTorch or vLLM.
- Dohnuts trained and serves on an RX 7900 XTX (ROCm, RDNA3), which is adjacent evidence for 0.8B LoRA training.
- The most portable Jev-Omni route is Reza2kn's GGUF: llama-server --embedding --pooling none plus an FP32 NumPy head. It has been tested only on CPU (Ryzen AI 9 HX 370) and CUDA, never on an AMD GPU.
- CUDA- or NVIDIA-only: Jev-Omni's own loader (CUDA, about 50 GB FP32), GPC-1's server (NVIDIA), Valen (NVIDIA GPU), and every NVFP4 artifact (LFM2.5-VL-3B-Decision, Geni-S1-Ops, WIlfLin 180B, which is also larger than 115 GB).
- bitsandbytes dependencies: vjev QLoRA nf4 training and Qevi's 8-bit AdamW; swap these on ROCm.
- OmniJev's Qwen3.5 fast path needs flash-linear-attention Triton kernels, which are unverified on gfx1151; otherwise it falls back to a slow fp32 loop. The Qwen3-VL-4B path is plain transformers.
- Mac: circuit-vl-4b and circuit-audio-7b trained on an Apple laptop GPU in 85 and 55 minutes. Ruiruiz30 MLX 4-bit ran in about 7 GB on an M4 with 16 GB. monica is MPS-first. qev-mlx ran on an M4.

Datasets built for omni decision training: Valen-Training-General-100k (image typed-decision records with target distributions; ChartQA subset is GPL-3.0; 99,047 rows pending human audit), Valen-Eval-General-5k and Valen-Eval-Game, JonesLin next-jev stage2 (414k image NLI with unnamed-teacher rationales), video-r1-mc-24f100k (video multiple choice), video-vqa-sft-mixed, PhoneticQA (audio multiple-choice probe), TTS human preferences (audio pairwise), FitAQA, CMB and MedQA-MM (evals).

Identity notes:
- tinnel123/OmniJev ≠ Iron-LYK/OmniJev (§161) ≠ the OmniJev org (PlayJev, awesome-jev).
- 0xSojalSec/Jev-Omni and arafathusayn/autojev-27b are re-uploads, not new models.
- guanxuyu-sv Visual-Jev ≠ jiangxiluning/Visual-Jev (§160) ≠ Valen's historical 'Visual-Jev-Training' identifiers (a different author).
- The thaitea/laya-vision moving copy moved to d1fbdc06, pointing at -score.
- SeanLiu/Jev-Vision sha moved 9b77fa5f → dc2d645b with unchanged numbers.
- Ruiruiz30 sha moved 2ffc677c → 38fccc7f with a new card.
- Jev-Omni is unchanged at c050d513.

Failures and gaps: HTTP 401 (gated or unreadable) on snkii/Sori-1B(-MCQ), datapointai TTS prefs, AI4Manufacturing \*-mcq and zero-runtime/echo-omni. HTTP 404 README on thaitea/laya-vision-web, xiq/xiq-vl-jev (empty repo), 34data/videogen-rewardbench and mocomoco whisper-browser-models. The multimodalart/jev-decision-index tracker lists only text entrants, so it was not a useful source.

Housekeeping: the relayed user request ('kill whatever is holding it') did not apply here. Nothing held a lock in this lane and no process was killed. A sibling lane's scratch at tmp/hf-hub was left untouched. Scratch evidence for this lane is under research/080/research/tmp/hf-omni/: query_ledger.tsv, raw/, detail/, readme/, gh/, known_where.json, cands.txt, items_meta.json. No repo edits, pushes or posts, and no files were written outside research/080/.

### 2.4 Lane: Open web and arXiv

*Lane scope:* open web + arXiv (multimodal/omni decision-model training recipes). Retrieval 2026-09-23T23:59Z to 2026-09-24T00:12Z UTC, which is 2026-09-23 local. Sources: arXiv export API (40 queries, submittedDate 2026-09-01..2026-09-23), built-in WebSearch (15 queries), WebFetch (5 posts), gh api (awesome-list commits and compares since 2026-09-01, plus repo metadata and READMEs), raw.githubusercontent, the Hugging Face API (full=true), and jevusers.com /api/projects and /apps. Scratch: research/080/research/tmp/web-arxiv-mm/

Lane ledger, reproduced with markdown escaping (raw text in `tmp/mm-synth/task_input.json`):

LEDGER: open web + arXiv lane, multimodal/omni trainer recipes. Retrieved 2026-09-23T23:59Z to 2026-09-24T00:12Z UTC (2026-09-23 local).

WRITES. All writes are under research/080/research/tmp/web-arxiv-mm/: arxiv/\*.xml, arxiv_all.json, arxiv_ledger.txt, arxiv_q.sh, parse.py, short2.txt, awesome/\*, gh/\*, hf/\*, jevusers/\*. No repo edits, pushes, posts, issues, installs, execution of third-party code, or weight downloads. No paid search APIs were used.

PROCESS NOTE on the relayed request 'kill whatever is holding it'. The only candidate I found was a sibling lane's jevusers retry loop (tmp/open-web/jevretry.sh, PID 59998). Its log shows /apps went from HTTP 500 to 200 at 00:00:15Z, and the loop exited on its own. My own fetches worked: /api/projects returned 200 (400 projects) at 00:06:01Z and /apps returned 200 (1,299 apps) at 00:06:02Z. Nothing was holding this lane, and I killed nothing.

QUERIES.
- arXiv: 40 export-API queries with submittedDate 2026-09-01..2026-09-23, all HTTP 200. That gave 465 unique ids, 374 of them in the window. Query t10 had an AND/OR precedence bug and returned pre-window reject-option papers; t10b re-ran it correctly. The only arXiv id from this pass already in the archive is 2609.26384 (in both sources.json and notes).
- WebSearch: multimodal/omni Jev, train Jev vision, open multimodal decision model, VLM head calibration, audio abstention, PocketJev, Visual-JEV, PlayJev, awesome-jev-family.
- WebFetch: 2 seangoedecke posts, mikulskibartosz, raschka (not multimodal; dropped), the UlrickBL Qwen3-VL reranker blog (dated 2026-01-12, out of window; its w_yes−w_no linear head noted only here), and the Weinmeister Medium post (HTTP 403, not covered).
- Awesome lists: gh compare from the last commit before 2026-09-21T00:00Z to HEAD for yibie (261 commits), hellogumbo (33), AnotiaWang (28), cobanov (96), AbdelStark (244, mostly site regeneration), Anil-matcha (32), MrJev (29), and kraayenjon (1). Large files were diffed as raw base and head copies.
- New multimodal training entries from the lists: Prosodia (cobanov), PlayJev, Dohnuts, OpenJev-Vision, and choosekit (MrJev, hellogumbo), plus amigos-jev and openjev-multimodal (hellogumbo). Other multimodal additions only route voice or OCR into hosted Jev and train nothing (jev-canvas, GUI_JEV, JevBystander, voice controllers), so they were skipped.
- jevusers /apps: 74 multimodal-keyword entries. Only PlayJev, PocketJev, and jev-visual are open multimodal models; genai-craft/openvons and mithalouni/system-one-open are already in notes.

DEDUPE AND IDENTITY LOCKS.
- Revisits with new facts: Jev-Omni moved to sha c050d513 (from 55b53f2e / 3e885f29). The card now says 30k questions (was 24k), adds MVBench, and claims no Jev output. Ruiruiz30/Jev-Omni-MLX-4bit went from 2ffc677c to 38fccc7f and now has measurements. Dohnuts HEAD went from 253766e5 to e22b01cb, and the model card shows the RX 7900 XTX. Prosodia HEAD went from cf8c5c12 to 61dac288 (README SHA unchanged). Valen HEAD is unchanged, but technical.md was read this time.
- jiangxiluning/Visual-Jev: README went from 404 to a SemIf README copy with a frozen optional-image readout. It is not a trained model, and yibie's blurb overstates it.
- shapsider/OmniJev is most likely Iron-LYK/OmniJev moved (Iron-LYK now 404, text matches, no redirect), but that is not proven.
- jev-skills/openjev-multimodal is not proven to be the same as Hand-In/openjev-multimodal: same description, not a fork, different README blobs. Its HEAD committer date is 2026-10-01 (future).
- 0xSojalSec/Jev-Omni is a re-upload of akhilaaa3/Jev-Omni.
- alperiox Prosodia ≠ HF org Prosodia/Prosodia_T1.7B (Nov 2025).
- multimodalart/jev-reproductions-tracker returns HTTP 307 to multimodalart/jev-decision-index, a rename. Its Decision Index panel is text-only and explicitly excludes image items, so there is still no open multimodal decision leaderboard.
- OmniJev/awesome-jev redirects to OmniJev/awesome-jev-gallery.

DECISION-CHANGING SYNTHESIS for the future multimodal trainer skill. Evidence labels: all third-party numbers are Reported. arXiv items were read at abstract level. Nothing was reproduced.

(1) Readout gap: probe before you fine-tune. Frozen VLM or audio-LM internals carry more decision signal than the generated answer. Evidence: 2609.18860 (probe 0.740 vs native 0.432 macro-F1), 2609.04336, 2609.09417 (encoders ≈ DINOv3 separable), 2609.00868 (vision-tower probe 0.72–0.79 while argmax moves on 2–11%), and 2609.00727 (audio-encoder style lost before the output). Proposed ladder addition: M-R2, a linear or small head on frozen multimodal features (vision tower, audio encoder, omni embedding such as Ovis, or DINOv2/V-JEPA2 as in OpenJev-Vision and 2609.19772), placed before LoRA. Counterexample: 2609.18860 shared multi-task adaptation gave negative transfer, so gains are not automatic.

(2) Verbalized VLM confidence is not a Noul. Evidence: 2609.18453, 2609.20110 (AUROC 0.54–0.74), and 2609.09417 (verifier confidence filter backfired). Use option logits or probes plus held-out calibration.

(3) A modality-use gate is required, and overall accuracy is not enough. Report text-only, options-only, blank or ablated-media, and counterfactual arms beside the full-input arm, with at least n perturbations for n inputs (2609.06190). Evidence: MedQA-MM text-only 53.96% vs full 62.63%; MotionBlind paired items; CLASH lexical vs prosody arms; Prosodia text-only controls; SEAR's text-only probe that separates text-answerable items from audio-dependent ones. Proposed rule: a multimodal challenger must beat the incumbent AND its own text-only arm on untouched workload data.

(4) Option order is a free ensemble and a bias. Shuffle options in training (PlayJev) and average permutations at inference (2609.04362: +3.5 points and better error ranking). MedProb reports generation position bias of up to 10 points.

(5) Forgetting controls. PlayJev: training on games only dropped MMBench 0.66→0.48, and 20% general-image plus 20% text replay recovered it to 0.78. 2609.11310: soft prompts gave no forgetting where LoRA did.

(6) Quantize, then recalibrate the served artifact. Evidence: 2609.06922; Jev-Omni Q4_K_M flipped 1 of 4 argmaxes (max abs diff 0.21); the MLX 4-bit port shifted up to 0.244. Calibration and conformal sets must be refit after any fine-tune or quantization (2609.10333). A single global temperature can make held-out ECE worse (Ruiruiz30: 0.0677 vs raw 0.0626). ECE alone can rank a constant predictor well (Prosodia ECE 0.0097), so use Brier/NLL plus a base-rate constant arm.

(7) Provenance. Seangoedecke (2026-09-20) recommends distilling Jev I/O, which MCA §2.3(b) bars; cite it as the bad pattern. Hidden teacher labels appear in multimodal recipes: Dohnuts mixes LocalLLaMA/typed-decisions (unnamed ~4B 'teacher endpoint'); SEAR uses Gemini 3.1 Flash-Lite MCQs; the 2609.20110 calibrator is fit on Gemini outputs; 2609.10244, CA-OPD, and EgoLongQA teachers are unidentified. Clean label sources: code or search teachers (PlayJev), human corpora (Prosodia MELD, ModerationBench), and public VQA gold (Valen, OpenJev-Vision, Dohnuts' visual groups). The trainer must record a per-row label source, and 'unnamed teacher endpoint' must count as unresolved provenance.

(8) Hardware and ROCm (all Hypothesis until run on tabputer).
- Dohnuts reports training a 0.8B text+image decision model on one AMD RX 7900 XTX 24 GB: frozen base and vision encoder, rank-8 LoRA plus a scorer. That is RDNA3 gfx1100, not gfx1151.
- Jev-Omni Q4_K_M runs under llama.cpp with a Python decision-head script, measured CPU-only on an AMD Ryzen AI 9 HX 370 at 1.88 s per decision. llama.cpp HIP or Vulkan on gfx1151 is the likely serving path.
- Jev-Omni MLX 4-bit runs about 1 s on an M4 16GB, so the Mac M4 24GB is feasible for inference.
- PlayJev, Valen, and the Jev-Omni card assume CUDA. The Alpha-Harper-Franklin backend is CUDA-only. gemma-decision-kit NVFP4 is Blackwell-only. The pt810 Ovis bnb variants need bitsandbytes (ROCm caveat).
- OpenJev-Vision and Prosodia are small enough for CPU. Flash-attn usage in PlayJev and Valen was not checked (requirements files not read).
- vLLM ROCm 0.29 support for Qwen3.5-VL, Qwen3-Omni, or Gemma 4 multimodal was not verified.

(9) Hosted Jev is text-only, confirmed twice. mikulskibartosz quotes the docs ('images, audio, and video are not supported yet') and measured base64 PNG at chance, 9%. The Alpha-Harper-Franklin README says 'Hosted Jev remains text-only'. Serializing images into text for a text-only model loses badly: 35% vs 91% with native vision (theirs).

NOT COVERED. Full PDFs of every arXiv item (abstracts only); third-party code bodies (requirements, training scripts, flash-attn usage); the Dohnuts data-and-evaluation.md; Valen per-record provenance; Jev-Omni question sources; PlayJev docs/BASELINES.md; OmniEvaluator repo; Qwen3.8-Omni weight availability; the Weinmeister Medium post (403); the hellogumbo data/projects.json diff beyond keyword lines; the HF Hub lane's and GitHub repo-search lane's overlapping sweeps (sibling scratch dirs were not merged); jevusers /api/projects beyond the /apps keyword pass.

## 3. Adjudications: where cards or checks overrule the lane record

| Artifact (table #) | Lane record said | Card or check found | Resolution |
|---|---|---|---|
| Barneyjm/circuit (#1, #32, #33) | Grid gains: vl-4b 96.4% / ECE 0.036 vs base; "video as sampled frames" | Committed POPE files (300 COCO items; accuracy / ECE / Brier): raw 0.913 / 0.072 / 0.139, v1.1 0.923 / 0.049 / 0.128, v1.2 0.907 / 0.069 / 0.158. Code accepts one image or one clip. The audio base keeps the first 30 s. Train and eval draw from the same photo and speaker pools. Released temperatures are 1.0 (Contract) | Cite grid numbers only next to POPE. Provenance is clear for the released cards; exclude the teacher modules |
| nullsilver-labs/alpha-sys-1 (#3, #38) | 3B "still training"; mixtures "within .02–.04 NLL of specialists" | The 3B was released 2026-09-20 (seed 1, best step 3,600). The tier B gate FAILS in 4 of 7 environments; tier C FAILS; the P3 shift gate PASSES | A transfer negative. The README reads its own gate generously |
| guanxuyu-sv/Visual-Jev (#4, #28) | Held-out TextVQA and TallyQA "barely move" | leak.json: the K=4 TextVQA build was leaky (0.997 sighted). TallyQA sits near its floor (sighted 0.357 vs chance 0.167). No calibration was published for the released a2 adapter | The unseen sets cannot show transfer in either direction |
| andrueandersoncs/visual-jev (#5) | trains-a-model; provenance unclear (LNQA may be model-generated) | LNQA QA pairs were generated by Mixtral-8x7B (verified). About 56 base samples, and test splits of 2–12 per source. Several labels encode geometry, source identity or transform index. No checkpoint and no results. No license | Use it as a design-contract source only. Provenance: generated by an open-weight model, no hosted provider |
| trycua/cua cua-s1 (#6) | 4b-0.2 multimodal 0.929 / ECE 0.069 | GUI-360 gold is LLM-agent actions filtered to successful runs. The 0.2 multimodal adapter scores 0.000–0.214 on 5 of 6 synthetic families. Agentic N=18, all on held-out variants of trained environments. MODEL_CARD.md is stale | Provenance unknown. Count held-out variants of trained environments as in-distribution |
| sseanliu/Jev-Vision (#7) and SeanLiu/Jev-Vision (#49) | Labels "from the environment"; unclear / no-provider-outputs | V1–V2 used Qwen3-VL-32B soft targets (open-weight distillation). `probes/distill_jev.py` wrote Jev distributions into the committed `jsonl_jev*` files, and the s1-1.7b text lineage trains on them. The general-track comparison is partly in-distribution. T=0.5 was chosen by a sweep, not fitted | New MCA record. Borrow nothing downstream of `jsonl_jev`. The V9 weights are clean per the run scripts only |
| loadchange/qev (#8, #40) | "Qwen3.5-0.8B multimodal foundation" | The released v0.3 is Snake-specialized. The 81% numbers belong to v0.2, which is not on HF. Media decisions are untrained | Media accuracy is not evidenced |
| RikaiDev/mesen (#9) | trains-a-model; labels by construction | Non-functional as committed. No pixels reach the Qwen path, whose input is zeros. The prompt leaks the label. The served endpoint returns random probabilities. low_contrast is a no-op on 100 of 100 sampled rows. The teachers named in the README are absent from the code | Negative exemplar for the multimodal claim audit (§8.4). Not a recipe |
| azerothl/akasha-model (#10) | no-provider-outputs | Side branch `c2f74e36` trained bert-base on typed-decisions | The released Doom and chess checkpoints are clear; that branch run is barred pending |
| TalalAhmed311/laya-multimodal (#12, #44) | Best joint about 0.69; choice-only 0.90 "likely leakage" | Measured-here: weighting the single-task results by the README's type shares gives 0.49×0.90 + 0.38×0.52 + 0.13×0.55 ≈ 0.71. Selection and the temperature fit both use the reported validation set. The Laya base is unpinned and its provenance undisclosed | The pooled number cannot show image use. The weights inherit unknown base provenance |
| akhilaaa3/Jev-Omni (#34, #69) | Web lane: "new revision after 55b53f2e" | The `55b53f2` → `c050d51` move is already recorded in §166. The card details (30k vs 24k in config, MVBench, bf16 drift) are in the local `jev-omni-2026-09-23.md` | Not re-carded. The derivatives (0xSojalSec re-upload, Ruiruiz30 MLX, Reza2kn GGUF) inherit its `unknown` |
| Valen-Training-General-100k (#93, #110) | HF lane: unclear. Web lane: no-provider-outputs (Hypothesis) | How the target distributions are built is unstated. 99,047 rows are pending human audit. There are 50,203 image references but 48,445 unique hashes | `unknown`. The relabel is Apache-2.0, but the ChartQA share stays GPL-3.0. Split by image hash |
| Dohnuts section references | HF lane: §136/§137. Web lane: §143 | It appears in §136, §137, §143 and §144 | Both are right; the prior column lists all four |
| GitHub lane contract line | "No item found training on Jev outputs in committed data" | Jev-Vision commits Jev-distilled training data. alpha-sys-1 commits stored Jev predictions (as evaluation artifacts) | Superseded; see §4 |

## 4. Provenance ledger (MCA §2.3(b) and other hosted providers)

Vocabulary: plan v3 §3.6, as amended by errata D-c.
- **barred**: never on a path to a training artifact through any edge
  (`labeled_by`, `filtered_by`, `selected_by`, `featurized_by`,
  `derived_from`, `trained_on`).
- **restricted**: barred for us. For skill users it is refused by default and
  cleared for one use only by a recorded acknowledgment.
- **unknown**: can be cleared for one artifact and one use by a named
  approval.
- **clear (declared)**: no provider output on the declared lineage. It still
  needs a permission record carrying URL, digest and clause, plus a license
  check.

The gate checks declared provenance only.

| Class | Artifacts | What carries the output | Verdict | Action for Augustus |
|---|---|---|---|---|
| Jev Output in training | yah01/vjev-vision, yah01/vjev-vision-pilot (served by BubbleCal/vjev-serve, §162) | Text-stage soft labels from the official Jev API, KL to Jev | barred / restricted | Never reuse the weights or the text-stage data. Record them as a §3.6 test case |
| Jev Output in training (repo-level) | sseanliu/Jev-Vision: `model/data/jsonl_jev/`, `jsonl_jev_hard/`, `jsonl_nli_adv_jev/`, `jsonl_synth_jev/` | Jev distributions written as targets by `probes/distill_jev.py`. `run2.sh` stage 2b and `run_flagship.sh` train s1-1.7b on them | barred for that lineage | Treat the V9 vision weights as declared clean, but audit the lineage per artifact, not per repo |
| Jev Output as data | egetheengineer/jevcraft | Video of Jev's gameplay decisions | barred / restricted | No imitation or behavior cloning |
| Jev Output in evaluation | AIMultiple browser results.csv; alpha-sys-1 `runs/p0/raw/jev/*.jsonl` (14 files, about 20 MB); PlayJev `eval_typesafe.py` (recorded answers, gitignored); Jev and jevbench baselines in cua-s1 | Jev run outcomes or predictions | Evaluation only | Exclude these paths from any data pull. Selection on them is also a `selected_by` edge. Whether a Jev baseline inside a competing open model's benchmark is allowed is counsel question 2 |
| Jev pipeline present, outputs uncommitted | Barneyjm/circuit (`s1proto/data/teachers.py` posts to api.typesafe.ai; `gen_data.py`; `relabel_family.py`) | Nothing in the released data (all rows streamed: human or code labels) | clear for the released cards | Exclude the teacher modules. Do not reuse the slot names 'jev' and 'gemini' for human labels, because they defeat a lineage audit |
| TypeSafe-authored content | ctaxnagomi/instruct-jev (hf ctaxnagomi/INSTRUCT_JEV) | Rows compiled from mirrored TypeSafe docs (not opened) | unknown | Do not use. The MIT label on mirrored docs is not a grant |
| Bad-pattern guidance | seangoedecke.com, "system one models can train their own replacements" (2026-09-20) | Recommends distilling Jev input/output | n/a | The skill cites it as the barred route and redirects to outcome, human or code labels |
| Unnamed teacher, Jev allegation | LocalLLaMA/typed-decisions `c76749ec58bd` and its descendants: PsiACE/Dohnuts (HF and GH), harshatheg/GPC-1 ('Typed Decisions' notice), azerothl/akasha-model branch `c2f74e36`, and the CLM choice head (local note) | Gold is the mean of three samples from an unnamed ~4B 'teacher endpoint'. A third-party README says it was "labelled by Jev" | **barred pending resolution** | Not in any training path until the teacher and its terms are known |
| Other hosted providers | thaitea/laya-vision-smolvlm-256m-score (VLFeedback GPT-4V ratings); DoccyHealth/Solomon (Qwen3.8 via OpenRouter hosts); arXiv 2609.11355 SEAR (Gemini 3.1 Flash-Lite MCQs); arXiv 2609.20110 (calibrator fit on Gemini outputs); datapointai TTS preferences (hosted-TTS audio, human labels); Shikari-ai/pehredaar-poc (edge-tts inputs, author labels); cua-bench OSWorld gold (Claude Sonnet 4.5 agent, evaluation only) | Labels, inputs or calibration data produced by a hosted provider | unknown (provider and channel terms) | Clear only per artifact under §3.6. Record inputs synthesized by a provider separately from labels |
| Unnamed or undisclosed teachers | tinnel123/OmniJev-0.8B ('teacher questions'); JonesLin next-jev rationales; JonesLin/video-vqa-sft-mixed; arXiv 2609.07154, 2609.02401, 2609.10244; junpei-9898/gemma-decision-kit ('AI-provisional' labels); akhilaaa3/Jev-Omni (undisclosed; Hypothesis: the Opus-5 DecisionBench pipeline); TalalML123 (Laya base); trycua GUI-360 (LLM agent) | Unknown generator | unknown | Missing parents make lineage unknown. An 'unnamed teacher endpoint' counts as unresolved |
| Open-weight, locally generated | andrueandersoncs/visual-jev LNQA (Mixtral-8x7B); Jev-Vision grounding (Qwen3-VL-32B soft targets); djhoomin (Gemma via Ollama); circuit-audio (Kokoro-82M TTS); the Qwen3.6 half of SEAR | Open-weight model outputs | allowed with recorded provenance, subject to the weight license | Plan v3's "local Apache-2.0 teacher with declared lineage" case |
| Author claims "no Jev / no teacher" (self-attestation) | Jev-Omni, LFM2.5-VL-3B-Decision, qev, JevAny, circuit-*, Qevi, SeanLiu/Jev-Vision | Claim only | Weighed by what was read (see the §5 verdict column) | An attestation never clears `unknown` by itself |

## 5. All 139 delivered items

`#` is the delivered order (1-based); section 3 cites these numbers.
- **†** marks a row that a card or this synthesis corrects (section 3).
- **Provenance** gives the lane label, then the adjudicated verdict (section 4).
- **Prior** is the dedupe status against `origin/main` `d8dc848` research
  and the local `research/080/research` files.
- Duplicates name their canonical row.
- Full lane text is in `tmp/mm-synth/task_input.json`.

### 5.1 Trains a model (86)

| # | Item | Lane | Created | Pushed / modified | Modalities | Provenance: lane → verdict | Prior | Family | Summary |
|---|---|---|---|---|---|---|---|---|---|
| 1 † | [github:Barneyjm/circuit](https://github.com/Barneyjm/circuit) | GH | 2026-09-19T14:50:34Z | 2026-09-24T00:21Z | text; image (rendered receipts/charts/tables/forms/scenes + Open Images photos); video frames; audio (speech, sound) | no-provider-outputs → clear (released models); exclude teacher pipeline | new; archive-only sighting (SDK carded §114) | circuit | Code-labeled render and audio grids, LoRA plus pointer head on Qwen3-VL-4B and Qwen2-Audio-7B. card: v1.2 is worse than the raw base on POPE (Brier 0.158 vs 0.139); the HF claim of multi-image/video is not in the code (one image or clip). |
| 2 | [github:OmniJev/PlayJev](https://github.com/OmniJev/PlayJev) | GH | 2026-09-17 | 2026-09-21T14:00Z | image (single 448px game frame; pixels only); text replay | no-provider-outputs → clear (declared) | new; archive-only (refresh inventories) | PlayJev | Qwen3.5-0.8B full FT plays ten games from one 448-px frame. Search-program teachers plus DAgger; 20% replay keeps MMBench 0.78 vs 0.48. card: Flappy 0.973 per-frame agreement vs 0.18 closed-loop. |
| 3 † | [github:nullsilver-labs/alpha-sys-1](https://github.com/nullsilver-labs/alpha-sys-1) | GH | 2026-09-19 | 2026-09-19T09:09Z | text; image (CIFAR-10/-C, Camelyon17-WILDS histopathology) | no-provider-outputs → clear (training); exclude runs/p0/raw/jev (stored Jev Output) | new | alpha-sys-1 | LFM2.5-VL 450M/1.6B/3B LoRA on soft human and outcome labels with pre-registered gates. card: tier B and tier C gates FAIL; 3B is released; the repo commits raw Jev predictions as eval artifacts. |
| 4 † | [github:guanxuyu-sv/Visual-Jev](https://github.com/guanxuyu-sv/Visual-Jev) | GH | 2026-09-21T07:25:57Z | 2026-09-23T22:55Z | image | no-provider-outputs → clear (declared) | new; archive-only (node_id) | Visual Jev (guanxuyu) | Answer-SFT LoRA on Qwen3-VL-4B/8B reading LM-head letter logits; matched typed head +0.000. card: held-out sets cannot show transfer (TextVQA saturated, TallyQA at floor); no calibration for the released adapter. |
| 5 † | [github:andrueandersoncs/visual-jev](https://github.com/andrueandersoncs/visual-jev) | GH | 2026-09-19 | 2026-09-20T03:15Z | image (multi-image); optional structured text context | unclear → open-weight-generated labels (LNQA via Mixtral-8x7B); no hosted provider | new |  | Qwen3-VL-2B pointer head plus custom LoRA with a strict dataset and promotion contract. card: about 56 base samples, geometry/source/transform-index label shortcuts, LNQA labels Mixtral-generated, no results, no license. |
| 6 † | [github:trycua/cua](https://github.com/trycua/cua/tree/main/libs/cua-s1) | GH | 2026-09-22T16:37:53Z (commit d1a01f8580d5, PR #4023) | 2026-09-24T00:20Z (repo) | screenshot (multimodal adapter) and accessibility tree (text adapter); game frames/chess held out | unclear → unknown (GUI-360 LLM-agent gold) | revisit of parent §54; 2026-09-22 release new |  | cua-s1 nano/4b-0.1/4b-0.2: Qwen3.5-4B LoRA letter logits with separate text and screenshot adapters, RLOO+Brier RL. card: GUI-360 gold is LLM-agent output; 0.2 multimodal adapter regresses on synthetic screens. |
| 7 † | [github:sseanliu/Jev-Vision](https://github.com/sseanliu/Jev-Vision) | GH | 2026-09-17 | 2026-09-21T22:08Z | screenshot/web UI; image (GQA); text | unclear → mixed: jsonl_jev text lineage barred; V9 vision lineage declared clean | revisit §124 (fingerprint dbd230b57fae) | Jev-Vision (sseanliu) | Qwen3-VL-8B LoRA plus typed-head step verifier. Recorded-policy labels were wrong about half the time; gold now comes from the task. card: grounding stages used Qwen3-VL-32B soft targets, and the repo commits Jev-distilled text data (jsonl_jev\*). |
| 8 † | [github:loadchange/qev](https://github.com/loadchange/qev) | GH | 2026-09-21 | 2026-09-21T11:51Z | text-trained; image/video inputs and image-valued options accepted by the API (multimodal decision accuracy not evaluated) | no-provider-outputs → clear (declared) | new | qev | Frozen Qwen3.5-0.8B plus switchable LoRA and pointer, one sequence per question because GatedDeltaNet state cannot be masked; FP32 MLX export. card: released v0.3 is Snake-specialized; media decisions untrained. |
| 9 † | [github:RikaiDev/mesen](https://github.com/RikaiDev/mesen) | GH | 2026-09-23 | 2026-09-23T15:17Z | multi-viewport screenshots (375/768/1024/1440 px) + DOM/accessibility state | no-provider-outputs → clear (declared) | new; archive-only (patrol) |  | Claims a Qwen3.5-2B screenshot UI judge with mutation labels. card: pixels never reach the model, the text input is zeros, the prompt leaks the label, and the served endpoint returns random probabilities. Negative exemplar. |
| 10 † | [github:azerothl/akasha-model](https://github.com/azerothl/akasha-model) | GH | 2026-09-20 | 2026-09-22T20:17Z | text/JSON state; image patches (160x120 game frames + motion channel) for Doom and chess | no-provider-outputs → clear (released checkpoints); typed-decisions branch barred pending (typed-decisions teacher conflict) | new |  | Option-attention scorer. Pixel controllers trained imitation, then DAgger, then PPO from Doom-engine and Stockfish experts; blank/average/shuffled-patch audit tool. card: side-branch run on typed-decisions (barred pending). |
| 11 | [github:JonathanHHenson/laya-multimodal](https://github.com/JonathanHHenson/laya-multimodal) | GH | 2026-09-22 | 2026-09-22T13:07Z | image (SigLIP2) and audio (CLAP) | no-provider-outputs → clear (declared) | new |  | Frozen SigLIP2 or CLAP; V0 zero-shot plus a zero-init residual option-query head; cached media states; MPS. No data, weights or results. card: 224 px squash, 64-token option cap, 10 s audio fusion crop. |
| 12 † | [github:TalalAhmed311/laya-multimodal](https://github.com/TalalAhmed311/laya-multimodal) | GH | 2026-09-23 | 2026-09-23T10:21Z | image + text (VQA v2 / COCO) | no-provider-outputs → labels clear; inherited Laya base unknown | new; archive-only (patrol) | laya-multimodal (Talal) | Frozen SigLIP-base, cross-attention bridge, Laya ModernBERT scorer on VQA v2. noul about 0.52 (chance), choice 0.90 flagged as leakage. card: the joint 0.69 is explainable without the image. |
| 13 | [github:sloina/context-enriched-heads](https://github.com/sloina/context-enriched-heads) | GH | 2026-09-14 | 2026-09-23T18:42Z | audio (wake-word) | no-provider-outputs → clear (declared) | new |  | 65-386-parameter linear head on a frozen wake-word backbone with a label-blind test protocol; FRR at 1 FA/h 2.81 to 0.95 (theirs). CPU only. |
| 14 | [github:findshan/finvcup-multimodal-turntaking](https://github.com/findshan/finvcup-multimodal-turntaking) | GH | 2026-09-04 | 2026-09-04T23:19Z | audio (dual-channel 30 s) + ASR text + label history | no-provider-outputs → clear (declared) | new |  | Whisper + Qwen + label-history fusion post-mortem. Per-label thresholds helped; more training raised validation but lowered the private score (anti-correlation). |
| 15 | [github:Shikari-ai/pehredaar-poc](https://github.com/Shikari-ai/pehredaar-poc) | GH | 2026-09-08 | 2026-09-08T15:56Z | audio (no speech-to-text) | no-provider-outputs → labels clear; inputs hosted-TTS (unknown terms) | new |  | 88M audio encoder plus a 1,536-parameter linear head for scam calls, AUC 0.943 (theirs); shuffled-label check. All audio is synthesized by hosted edge-tts voices. |
| 16 | [github:tin-xai/multimodal-jev-grounding](https://github.com/tin-xai/multimodal-jev-grounding) | GH | 2026-09-21 | 2026-09-21T15:47Z | image | no-provider-outputs → clear (declared) | new; archive-only (hourly) |  | Qwen2.5-VL-3B LoRA returning option probabilities plus a box-regression grounding head, on CUB-200. |
| 17 | [github:small-thinking/multimodal-judge](https://github.com/small-thinking/multimodal-judge) | GH | 2026-09-06 | 2026-09-09T23:29Z | image + title text | unclear → unknown | new |  | Qwen3-VL-2B LoRA plus scalar or 10-class score head trained on Mac MPS; annotation source not verified. |
| 18 | [github:qinwuxutexas/Qwen3-VL-Classification-and-Reasoning](https://github.com/qinwuxutexas/Qwen3-VL-Classification-and-Reasoning) | GH | 2026-09-13 | 2026-09-13T20:52Z | image + text | no-provider-outputs → clear (declared) | new |  | Qwen3-VL-8B QLoRA with a binary gate head, then a K-way head on the same hidden state (e-SNLI-VE mock). bitsandbytes; PolyForm NC. |
| 19 | [github:stefanionescu/screenshot-classifier-training](https://github.com/stefanionescu/screenshot-classifier-training) | GH | 2026-09-03 | 2026-09-04T17:35Z | mobile screenshots | unclear → unknown | new |  | CLI to train a multi-task mobile-screenshot classifier; corpus not shipped, so labels are unknown. |
| 20 | [github:alperiox/audio-jevlike](https://github.com/alperiox/audio-jevlike) | GH | 2026-09-20 | 2026-09-23T10:30Z | audio | no-provider-outputs → clear (declared) | revisit §145 (fingerprint cf8c5c121052) | Prosodia | Prosodia docs delta: IEMOCAP annotator soft targets and a one-attention-step IIA fix; readings of Kev and Laya RLCD. |
| 21 | [github:asp616848/better-jev-for-all](https://github.com/asp616848/better-jev-for-all) | GH | 2026-09-22 | 2026-09-24T00:09Z | text (vision path: mechanism smoke only) | no-provider-outputs → clear (declared) | new; archive-only (patrol) |  | Qwen3.5-4B LoRA letter logits; vision tier is a smoke test. A text-trained adapter remapped into the VL class keeps identical text metrics. |
| 22 | [github:PAI-CUHK/MEDJEV](https://github.com/PAI-CUHK/MEDJEV) | GH | 2026-09-22 | 2026-09-23T13:22Z | text (clinical, biomedical); physiological signals (overnight PSG, experimental sleepjev) | unclear → unknown | new; archive-only (patrol) |  | Evidence-relationship decision package plus sleepjev polysomnography signal model; no-PHI and manifest rules; PSG sources unnamed. |
| 23 | [github:djhoomin/local-system-one](https://github.com/djhoomin/local-system-one) | GH | 2026-09-18 | 2026-09-23T10:32Z | text | no-provider-outputs → local open-weight teachers (Gemma terms) | revisit §143 |  | Text, out of lane: local Ollama Gemma teachers, calibrated before distillation. |
| 24 | [github:robbalian/rev](https://github.com/robbalian/rev) | GH | 2026-09-22 | 2026-09-23T16:10Z | text | no-provider-outputs → clear (declared) | new; archive-only (patrol) |  | Text, out of lane: Qwen LoRA plus pointer on public and rule-labeled rows; a head-only pointer on frozen Qwen transferred poorly. |
| 25 | [hf:tinnel123/OmniJev](https://huggingface.co/tinnel123/OmniJev) | HF | 2026-09-23T10:27:07Z | 2026-09-23T16:45:38Z | image, video (sampled frames), screenshots, text context | unclear → unknown | new | OmniJev (tinnel) | Qwen3-VL-4B LoRA plus decision and ordinal heads, NOTA option, per-type temperatures. Reports base zero-shot beside every score; OK-VQA and LongVideoBench regress. CC-BY-NC. |
| 26 | [hf:tinnel123/OmniJev-0.8B](https://huggingface.co/tinnel123/OmniJev-0.8B) | HF | 2026-09-23T15:39:21Z | 2026-09-23T23:28:33Z | image, video frames, screens, game frames, robot views, audio (ESC-50 rendered as spectrogram images) | unclear → unknown (unnamed teacher questions) | new | OmniJev (tinnel) | Qwen3.5-0.8B LoRA plus heads on about 250k records including audio as spectrogram images (ESC-50 0.473) and unnamed-teacher questions; OK-VQA 0.793 to 0.656. FLA kernel caveat. |
| 27 | [hf:tinnel123/OmniJev-2B](https://huggingface.co/tinnel123/OmniJev-2B) | HF | 2026-09-23T22:49:39Z | 2026-09-23T22:50:07Z | image, video frames, screens, audio-as-spectrogram | unclear → unknown | new | OmniJev (tinnel) | Same recipe on Qwen3.5-2B; LongVideoBench 0.568 to 0.502. PolyForm NC. |
| 28 † | [hf:guanxuyu/visual-jev-4b-answer-sft](https://huggingface.co/guanxuyu/visual-jev-4b-answer-sft) | HF | 2026-09-23T07:29:28Z | 2026-09-23T22:05:27Z | image + shared text context, forced choice | no-provider-outputs → clear (declared) | new (GitHub archive-only) | Visual Jev (guanxuyu) | Released Visual Jev 4B answer-SFT adapter, three seeds; gains only on trained families. card: the unseen sets are saturated or at floor, so transfer is untested either way; no calibration published. Apache-2.0. |
| 29 | [hf:Valen-Team/Valen-Preview-0923](https://huggingface.co/Valen-Team/Valen-Preview-0923) | HF | 2026-09-23T07:29:37Z | 2026-09-23T12:26:01Z | image (Sokoban screenshots); family claims text, image, video | unclear → unknown | GitHub §165; HF new | Valen | Qwen3.5-2B decision head, SFT then RLCD on Sokoban (87.6% single-step, theirs). The game level set is conditioned on model outcomes; NVIDIA-only card. |
| 30 | [hf:yah01/vjev-vision](https://huggingface.co/yah01/vjev-vision) | HF | 2026-09-22T18:41:00Z | 2026-09-22T19:38:31Z | image + text | uses-jev-outputs → barred (ours); restricted (skill users) | §162 named the weights; provenance new | vjev (yah01) | Qwen3.5-4B listwise vision model whose text stage used soft labels from the official Jev API (KL to Jev). Confirmed Jev-output distillation. |
| 31 | [hf:yah01/vjev-vision-pilot](https://huggingface.co/yah01/vjev-vision-pilot) | HF | 2026-09-22T02:57:20Z | 2026-09-22T03:55:54Z | image + text | uses-jev-outputs → barred (ours); restricted (skill users) | §162 named; provenance new | vjev (yah01) | 300-step vision pilot warm-started from the same Jev-distilled text stage. |
| 32 † | [hf:jbarney/circuit-vl-4b](https://huggingface.co/jbarney/circuit-vl-4b) | HF | 2026-09-19T15:56:27Z | 2026-09-22T14:19:06Z | image (video as sampled frames) + text | no-provider-outputs → clear (declared) | family §114; card new | circuit | v1.2 parallel options: reorder flips 3.6% to 0.0%; 85 min on an Apple laptop GPU. card: POPE Brier 0.158 vs raw base 0.139. |
| 33 † | [hf:jbarney/circuit-audio-7b](https://huggingface.co/jbarney/circuit-audio-7b) | HF | 2026-09-19T17:22:45Z | 2026-09-22T14:19:07Z | audio (speech and non-speech) + text | no-provider-outputs → clear (declared) | new (family §114) | circuit | Qwen2-Audio-7B LoRA plus pointer on Kokoro TTS and LibriSpeech grids; flips 11.7% to 2.9%. card: only the first 30 s of audio reach the model. |
| 34 † | [hf:akhilaaa3/Jev-Omni](https://huggingface.co/akhilaaa3/Jev-Omni) | HF | 2026-09-20T21:43:20Z | 2026-09-22T22:45:48Z | text, image, audio (&lt;=30 s), video (16 frames) | unclear → unknown | revisit §156; sha move already in §166; local card jev-omni-2026-09-23.md | Jev-Omni | Gemma 4 12B text-decoder LoRA plus a 256-way option-position head over stock towers. Card says 30k questions, config says 24k; no base-model counterfactual; trails Jev on its own benchmark (local card). |
| 35 | [hf:harshatheg/GPC-1](https://huggingface.co/harshatheg/GPC-1) | HF | 2026-09-21T17:14:04Z | 2026-09-23T22:55:56Z | text, documents, image (coordinates, boxes, landmarks) | unclear → barred pending (typed-decisions teacher conflict) | new |  | Qwen3.5-35B-A3B adapter classifier; notices list teacher-labeled 'Typed Decisions', so it inherits typed-decisions lineage. NVIDIA serving; BF16 about 70 GB. |
| 36 | [hf:MeerDevelopment/Qevi-2B](https://huggingface.co/MeerDevelopment/Qevi-2B) | HF | 2026-09-22T09:25:44Z | 2026-09-23T12:15:12Z | image + closed questions | no-provider-outputs → clear (declared) | new |  | Full FT of Qwen3-VL-2B with CE over candidate logits and label smoothing on ground-truth targets; held-out ECE 0.160 to 0.054 (theirs). bitsandbytes 8-bit AdamW; CC-BY-NC. |
| 37 | [hf:PsiACE/Dohnuts-0.1.0-0.8B](https://huggingface.co/PsiACE/Dohnuts-0.1.0-0.8B) | HF | 2026-09-21T05:59:09Z | 2026-09-21T08:13:19Z | text + one image | unclear → barred pending (typed-decisions teacher conflict) | §136/§137 first sighting and card; §143/§144 revisits; hardware line new | Dohnuts | Qwen3.5-0.8B frozen, rank-8 LoRA plus scorer, RLCD+CE; trained on one RX 7900 XTX (gfx1100). Mixes typed-decisions unnamed-teacher labels. |
| 38 † | [hf:nullsilver/alpha-sys-1-3B](https://huggingface.co/nullsilver/alpha-sys-1-3B) | HF | 2026-09-20T07:28:02Z | 2026-09-20T08:28:01Z | text, image | no-provider-outputs → clear (declared) | new | alpha-sys-1 | Released 3B (2026-09-20; the GitHub README still says in training). base+T beats the tuned model on unseen BoolQ and Yelp. card: tier B and tier C gates fail. LFM1.0 license. |
| 39 | [hf:tjm8874/LFM2.5-VL-3B-Decision-NVFP4](https://huggingface.co/tjm8874/LFM2.5-VL-3B-Decision-NVFP4) | HF | 2026-09-22T04:59:41Z | 2026-09-22T05:22:24Z | text, image | no-provider-outputs → clear (declared) | new |  | LoRA on the LFM2.5-VL-3B language side; says its renormalized log-probs are not calibrated. NVFP4 needs NVIDIA SM121. |
| 40 † | [hf:twainsk/qev-0.8b](https://huggingface.co/twainsk/qev-0.8b) | HF | 2026-09-21T01:06:10Z | 2026-09-21T01:06:20Z | text, image, sampled video (frozen Qwen3.5-0.8B foundation) | no-provider-outputs → clear (declared) | new | qev | Qev v0.3 Snake weights from a BFS teacher; adapter-off generation token-identical (weight-preservation check); FP32 MLX sibling. |
| 41 | [hf:thaitea/laya-vision-smolvlm-256m-score](https://huggingface.co/thaitea/laya-vision-smolvlm-256m-score) | HF | 2026-09-22T06:24:49Z | 2026-09-22T15:19:36Z | image + optional text | uses-other-provider-outputs → unknown (provider terms) | family §87/§146; checkpoint new | laya-vision (thaitea/r33drichards) | SmolVLM-256M option attention plus RLCD; the score head trains on VLFeedback GPT-4V ratings (hosted-provider labels). |
| 42 | [hf:thaitea/laya-vision-smolvlm2-256m-split1024](https://huggingface.co/thaitea/laya-vision-smolvlm2-256m-split1024) | HF | 2026-09-22T22:03:59Z | 2026-09-22T23:26:37Z | image + text | unclear → unknown | new (family §87/§146) | laya-vision (thaitea/r33drichards) | Image splitting at 1024 adds 1.4 points on a 24k Cauldron subset (theirs). |
| 43 | [hf:jaswanthsanjay88/rev-vision](https://huggingface.co/jaswanthsanjay88/rev-vision) | HF | 2026-09-23T14:10:16Z | 2026-09-23T21:00:47Z | image + question | unclear → unknown | new |  | SmolVLM-256M LoRA plus a 148k-parameter head at option terminators; training data unstated. |
| 44 † | [hf:TalalML123/laya-multimodal-best-all-tasks](https://huggingface.co/TalalML123/laya-multimodal-best-all-tasks) | HF | 2026-09-23T09:52:44Z | 2026-09-23T09:54:11Z | image + text | no-provider-outputs → labels clear; inherited Laya base unknown | GitHub archive-only; HF new | laya-multimodal (Talal) | Weights for Talal's SigLIP-to-Laya bridge; about 69% validation; inherits an unpinned Laya base of undisclosed provenance. |
| 45 | [hf:OmniJev/PlayJev-0.8B](https://huggingface.co/OmniJev/PlayJev-0.8B) | HF | 2026-09-19T10:32:04Z | 2026-09-21T14:00:08Z | image (game frames) to action | no-provider-outputs → clear (declared) | name-only (refresh archives) | PlayJev | Released PlayJev weights, Apache-2.0; 43 ms per move on H200. |
| 46 | [hf:mocomoco-inc/AudioJev-AudioDecisionModel](https://huggingface.co/mocomoco-inc/AudioJev-AudioDecisionModel) | HF | 2026-09-21T10:11:39Z | 2026-09-21T13:56:14Z | audio (0.25 to 30 s speech and non-speech) + text question/options, Japanese/English | unclear → unknown | new |  | ModernBERT-ja router mixing a Qwen3-ASR speech expert and a CLAP non-speech expert; q8 ONNX in the browser; label sources unstated. |
| 47 | [hf:datumsteve/monica](https://huggingface.co/datumsteve/monica) | HF | 2026-09-23T14:23:28Z | 2026-09-23T14:46:30Z | audio (speech emotion/sentiment) | no-provider-outputs → clear (declared) | new |  | Heads over selected layers of a frozen Gemma 4 E2B audio tower; encode once, ask 0-64 questions; MPS-first; code private. |
| 48 | [hf:snkii/Sori-1B-MCQ](https://huggingface.co/snkii/Sori-1B-MCQ) | HF | 2026-09-18T03:58:47Z | 2026-09-21T02:57:01Z | audio + text multiple choice | unclear → unknown | new |  | Gated audio MCQ model (LFM2.5 encoder plus Audio Flamingo encoder); card HTTP 401, metadata only. |
| 49 † | [hf:SeanLiu/Jev-Vision](https://huggingface.co/SeanLiu/Jev-Vision) | HF | 2026-09-21T11:25:00Z | 2026-09-21T14:43:01Z | image (screenshots, 1 or 2 images), text | no-provider-outputs → declared clean; open-weight Qwen3-VL-32B teacher; manifest unaudited | revisit §141 (sha 9b77fa5f) | Jev-Vision (sseanliu) | V9 weights; sha moved, numbers unchanged. Grounding stages used Qwen3-VL-32B soft targets (per the GitHub card). |
| 50 | [hf:tianxinwei/JevAny-27B-SFT](https://huggingface.co/tianxinwei/JevAny-27B-SFT) | HF | 2026-09-22T18:30:23Z | 2026-09-23T08:25:14Z | text, JSON state, native image, native video | unclear → unknown | GitHub §167; HF card new |  | Frozen Qwen3.8-27B LoRA plus pointer on 107k records including native image and video; label sources not itemized. |
| 51 | [hf:arafathusayn/autojev-27b](https://huggingface.co/arafathusayn/autojev-27b) | HF | 2026-09-22T21:41:44Z | 2026-09-22T21:41:45Z | text (image input accepted, not benchmarked) | unclear → unknown | original §163; mirror new |  | Re-upload of denis-pplx/autojev-27b; image input accepted but not benchmarked. |
| 52 | [hf:microlandltd/Geni-S1-Ops-26B-A4B-NVFP4](https://huggingface.co/microlandltd/Geni-S1-Ops-26B-A4B-NVFP4) | HF | 2026-09-21T19:22:08Z | 2026-09-21T20:44:41Z | text, image (visual grounding preserved) | unclear → unknown | new |  | IT-ops typed decisions with UNKNOWN abstention on DiffusionGemma-26B; internal data; NVFP4, NVIDIA only. |
| 53 | [hf:olafura/gemma4-12b-system-one](https://huggingface.co/olafura/gemma4-12b-system-one) | HF | 2026-09-22T08:59:05Z | 2026-09-23T19:58:11Z | text, audio (spoken requests as WAV) | unclear → unknown | new |  | 15 kB residual probe routes answer / reason / ask-back for int4 Gemma 4 12B including spoken requests. The only direct gfx1151 measurement, through EXLA (XLA), not PyTorch. |
| 54 | [hf:ginigen-ai/Edge-4B-TELL](https://huggingface.co/ginigen-ai/Edge-4B-TELL) | HF | 2026-09-19T03:16:26Z | 2026-09-19T08:18:13Z | text (base GGUF plus mmproj for vision and audio) | unclear → unknown | new |  | Linear correctness probe on Gemma-4-E4B GGUF: self-confidence AUROC 0.441, surface baseline 0.736, probe 0.759. Publishes the surface baseline. |
| 55 | [hf:theblackcat102/Molmo2-4B-Pairwise-Judge-Direct](https://huggingface.co/theblackcat102/Molmo2-4B-Pairwise-Judge-Direct) | HF | 2026-09-09T02:16:19Z | 2026-09-09T02:18:00Z | video pair + questionnaire text | unclear → unknown | new |  | One-token generative pairwise video judge (1 / 2 / Tie); no head; training data undescribed. |
| 56 | [hf:Gyubeum/Qwen3-VL-8B-Instruct-UI-Genie-scoring-128k-balanced-bt-naive](https://huggingface.co/Gyubeum/Qwen3-VL-8B-Instruct-UI-Genie-scoring-128k-balanced-bt-naive) | HF | 2026-09-21T17:36:09Z | 2026-09-23T07:06:05Z | GUI screenshots + action (mobile) | unclear → unknown | new |  | Qwen3-VL-8B Bradley-Terry scalar reward head for GUI steps on 'Latent Peer Voting' labels. |
| 57 | [hf:RESEARCH-EMPRM/emprm-v2-stageB_rung5_s0](https://huggingface.co/RESEARCH-EMPRM/emprm-v2-stageB_rung5_s0) | HF | 2026-09-05T18:04:29Z | 2026-09-07T11:04:14Z | chart image + reasoning steps | unclear → unknown | new |  | About 20 ablation LoRAs of a chart process-reward model on Qwen3-VL-8B. |
| 58 | [hf:MoritzM00/qwen3-vl-8b-lora-r16-sft-omnifall-all](https://huggingface.co/MoritzM00/qwen3-vl-8b-lora-r16-sft-omnifall-all) | HF | 2026-09-21T08:38:48Z | 2026-09-21T08:45:53Z | video to 16-way activity label | no-provider-outputs → clear (declared) | new |  | Generative SFT over 16 fall-detection video labels; contrast case for logit or head readout. |
| 59 | [hf:boyuzhuGPT/Qwen2.5-Omni-7B-Safety-ZeroAudio](https://huggingface.co/boyuzhuGPT/Qwen2.5-Omni-7B-Safety-ZeroAudio) | HF | 2026-09-19T17:33:32Z | 2026-09-19T21:34:34Z | text, image, video (audio removed) | unclear → unknown | new |  | Full-parameter SFT of Qwen2.5-Omni-7B into a Safe/Unsafe guard with the audio subsets dropped; 8x H200. |
| 60 | [hf:prithivMLmods/VisionGuardrail-Evo2-27B-MLX](https://huggingface.co/prithivMLmods/VisionGuardrail-Evo2-27B-MLX) | HF | 2026-09-19T06:47:03Z | 2026-09-19T13:43:33Z | image (and video tag) safety classification | unclear → unknown | new |  | MLX builds of a 27B image guardrail that classifies by generation; dataset provenance unchecked. |
| 61 | [hf:llm-semantic-router/Vela-1.0-Omni-Mini](https://huggingface.co/llm-semantic-router/Vela-1.0-Omni-Mini) | HF | 2026-09-17T18:47:56Z | 2026-09-19T13:26:15Z | text, image, speech, environmental sound embeddings | unclear → unknown | Decision-1.0 family §166; Omni models new |  | 1.36B omni embedding (text, image, speech, sound): the no-LLM baseline of embedding plus a calibrated linear or kNN head. |
| 62 | [hf:DoccyHealth/Solomon](https://huggingface.co/DoccyHealth/Solomon) | HF | 2026-09-21T01:38:48Z | 2026-09-21T10:29:06Z | documents (text) + structured questions | uses-other-provider-outputs → unknown (OpenRouter channel, open-weight Qwen3.8) | new |  | Qwen3.8-27B LoRA plus linear heads on documents; labels from an OpenRouter-hosted open-weight Qwen3.8; the gain CI includes zero (card says so). |
| 63 | [gh:OmniJev/PlayJev@616db06b2c27](https://github.com/OmniJev/PlayJev) | Web | 2026-09-17T20:37:50Z | 2026-09-21T14:00:02Z | image (single 448px game frame; option list as text) | no-provider-outputs → clear (declared) | dup of #2 | PlayJev | Web-lane record of the same repo: 0.9/0.1 soft targets, option rewrites, confidence-ranked handover to a System Two recovers teacher score and random handover does not. |
| 64 | [hf:OmniJev/PlayJev-0.8B@ea8951e786e1](https://huggingface.co/OmniJev/PlayJev-0.8B) | Web | 2026-09-19T10:32:04Z | 2026-09-21T14:00:08Z | image | no-provider-outputs → clear (declared) | dup of #45 | PlayJev | Web-lane record of the released weights; serves /v1/systemone in the OpenJev request shape. |
| 65 | [gh:alperiox/audio-jevlike@61dac28899a6](https://github.com/alperiox/audio-jevlike) | Web | 2026-09-20T20:36:52Z | 2026-09-23T10:30:10Z | audio (speech; no ASR) | no-provider-outputs → clear (declared) | dup of #20; recipe body first read here | Prosodia | Frozen Whisper encoder, questions folded into the batch, pointer readout, CE+0.5 Brier. A constant predictor gets ECE 0.0097; the prosody effect fails a base-rate control. |
| 66 | [gh:Liuziyu77/Valen@9a34b0c4a82a](https://github.com/Liuziyu77/Valen) | Web | 2026-09-23T02:48:02Z | 2026-09-23T15:25:09Z | image, video, text | no-provider-outputs → clear (declared) | revisit §165 (same HEAD) | Valen | technical.md: staged warmup, text, joint, vision_top; GRPO-style RLCD with KL and Brier; 8-GPU NVIDIA launcher. |
| 67 | [gh:PsiACE/dohnuts@e22b01cba0f8](https://github.com/PsiACE/dohnuts) | Web | 2026-09-21T05:23:34Z | 2026-09-21T18:59:10Z | text, image, screenshots (ScreenQA/Rico), documents | unclear → barred pending (typed-decisions teacher conflict) | revisit §136-§144 | Dohnuts | MODEL_CARD: trained on an RX 7900 XTX; per-type temperature on an independent partition; typed-decisions group flagged. |
| 68 | [gh:IamBusy/OpenJev-Vision@b83bec97243b](https://github.com/IamBusy/OpenJev-Vision) | Web | 2026-09-19T09:30:08Z | 2026-09-22T16:30:37Z | image (synthetic scenes, Oxford-IIIT Pet, CLEVR-4) | no-provider-outputs → clear (declared) | revisit §108/§117 |  | Encode once, answer several typed questions with trained readouts on frozen DINOv2; CPU only; three seeds including negatives. |
| 69 † | [hf:akhilaaa3/Jev-Omni@c050d5135414](https://huggingface.co/akhilaaa3/Jev-Omni) | Web | 2026-09-20T21:43:20Z | 2026-09-22T22:45:48Z | text, image, audio (≤30s), video (16 frames) | unclear → unknown | dup of #34; 'new revision' framing is stale (move recorded §166) | Jev-Omni | Web-lane record of the same card revision c050d513. |
| 70 | [arxiv:2609.18860v1](https://arxiv.org/abs/2609.18860) | Web | 2026-09-16 | 2026-09-16 | image+text (harmful memes) | no-provider-outputs → clear (declared) | new |  | Probe readouts beat native prediction on six harmful-meme tasks (Qwen 0.740 vs 0.432 macro-F1); shared multi-task adaptation transfers negatively. |
| 71 | [arxiv:2609.04336v1](https://arxiv.org/abs/2609.04336) | Web | 2026-09-03 | 2026-09-03 | image (medical VQA) | no-provider-outputs → clear (declared) | new |  | Linear probe on frozen VLM features beats prompting on Med-VQA multiple choice; generation position bias up to 10 points. |
| 72 | [arxiv:2609.06419v1](https://arxiv.org/abs/2609.06419) | Web | 2026-09-06 | 2026-09-06 | image (medical VQA) | no-provider-outputs → clear (declared) | new |  | Reliability read from a frozen GRPO actor's internal states beats verbalized confidence; CCG-AUC grounding metric. |
| 73 | [arxiv:2609.16601v1](https://arxiv.org/abs/2609.16601) | Web | 2026-09-15 | 2026-09-15 | image+text | no-provider-outputs → clear (declared) | new |  | GRPO penalizing calibration error and bad abstention; lower ECE than DPO on 8B VLMs. Costly generative route. |
| 74 | [arxiv:2609.11355v1](https://arxiv.org/abs/2609.11355) | Web | 2026-09-10 | 2026-09-10 | audio (multilingual speech MCQ) | uses-other-provider-outputs → unknown (provider terms) | new |  | Qwen3-Omni audio MCQ: a text-only probe splits text-answerable items (SFT) from audio-dependent items (RL). MCQs synthesized by Qwen3.6 and hosted Gemini. |
| 75 | [arxiv:2609.20110v1](https://arxiv.org/abs/2609.20110) | Web | 2026-09-17 | 2026-09-17 | document images (invoices, forms) | uses-other-provider-outputs → unknown (provider terms) | new |  | Decomposed document-field confidence plus conformal risk control; error-detection AUROC 0.54-0.74 to 0.90-0.99. One calibrator is fit on hosted Gemini outputs. |
| 76 | [arxiv:2609.10333v1](https://arxiv.org/abs/2609.10333) | Web | 2026-09-09 | 2026-09-09 | image (medical) | no-provider-outputs → clear (declared) | new |  | Fine-tuning breaks conformal exchangeability: recalibrate after every adaptation on data it never touched. |
| 77 | [arxiv:2609.04281v1](https://arxiv.org/abs/2609.04281) | Web | 2026-09-03 | 2026-09-03 | image+text (safety) | no-provider-outputs → clear (declared) | new |  | VLMs answer directly 86-99% of the time instead of deferring; a small input monitor predicts deferral (AUC 0.978). |
| 78 | [arxiv:2609.22910v1](https://arxiv.org/abs/2609.22910) | Web | 2026-09-19 | 2026-09-19 | image (crop/zoom agents) | no-provider-outputs → clear (declared) | new |  | Only 10-12% of visual tool calls were both needed and used; counterfactual credit for looking. |
| 79 | [arxiv:2609.07154v2](https://arxiv.org/abs/2609.07154) | Web | 2026-09-07 | 2026-09-10 | video (10-min egocentric, MCQ) | unclear → unknown | new |  | 2B VLM distilled from an agentic pipeline's correct-only traces; teacher unnamed. |
| 80 | [arxiv:2609.02401v2](https://arxiv.org/abs/2609.02401) | Web | 2026-09-02 | 2026-09-07 | screenshots (GUI grounding), OCR | unclear → unknown | new |  | Confidence-gated on-policy distillation into Qwen3.5-0.8B for GUI grounding and OCR; teachers unnamed. |
| 81 | [arxiv:2609.19772v1](https://arxiv.org/abs/2609.19772) | Web | 2026-09-17 | 2026-09-17 | video (surgical skill) | no-provider-outputs → clear (declared) | new |  | Frozen video encoders plus a light head, leave-one-user-out; a clean video frozen-feature recipe. |
| 82 | [arxiv:2609.13774v1](https://arxiv.org/abs/2609.13774) | Web | 2026-09-12 | 2026-09-12 | image (fabric swatches) | no-provider-outputs → clear (declared) | new |  | Deployment recipe with a duplication audit, a source-shift negative, and confidence-gated human routing. |
| 83 | [arxiv:2609.11310v1](https://arxiv.org/abs/2609.11310) | Web | 2026-09-10 | 2026-09-10 | image (few-shot detection) | no-provider-outputs → clear (declared) | new |  | 1-3 soft prompt tokens match LoRA on 10-shot detection with no forgetting; higher seed variance. |
| 84 | [arxiv:2609.09189v1](https://arxiv.org/abs/2609.09189) | Web | 2026-09-01 | 2026-09-01 | image (cytology) | no-provider-outputs → clear (declared) | new |  | Temperature-scale first, then pick a small-model ensemble on a composite reliability rank. |
| 85 | [arxiv:2609.08899v4](https://arxiv.org/abs/2609.08899) | Web | 2026-09-08 | 2026-09-20 | audio (speech deepfake) | no-provider-outputs → clear (declared) | new |  | Auditable decision record with a cross-fit calibrator costs accuracy against a plain WavLM baseline. |
| 86 | [arxiv:2609.10244v1](https://arxiv.org/abs/2609.10244) | Web | 2026-09-09 | 2026-09-09 | image+text (hallucination spans) | unclear → unknown | new |  | 4B VLM per-token hidden-state classifier ensembled with a ~400B zero-shot judge; synthetic data from the large model. |


### 5.2 Datasets for training (15)

| # | Item | Lane | Created | Pushed / modified | Modalities | Provenance: lane → verdict | Prior | Family | Summary |
|---|---|---|---|---|---|---|---|---|---|
| 89 | [github:Kaiming-Y/CriticGUI](https://github.com/Kaiming-Y/CriticGUI) | GH | 2026-09-20 | 2026-09-20T08:26Z | desktop screenshots (before/after), mouse/keyboard logs, OBS video | no-provider-outputs → clear (declared) | new |  | Human-demonstration toolkit with deliberate-mistake variants and manual critic labels for screenshot success/failure data. |
| 92 | [github:ctaxnagomi/instruct-jev](https://github.com/ctaxnagomi/instruct-jev) | GH | 2026-09-19 | 2026-09-19T06:22Z | text | unclear → unknown; TypeSafe-authored content, do not use | archive-only (hourly, inventory) |  | 119 rows compiled from mirrored TypeSafe docs, labeled MIT; rows unopened. Treat as TypeSafe-authored content. |
| 93 † | [hf:datasets/Valen-Team/Valen-Training-General-100k](https://huggingface.co/datasets/Valen-Team/Valen-Training-General-100k) | HF | 2026-09-23T03:09:25Z | 2026-09-23T12:26:03Z | image (VQA, GUI screens, games, documents, charts) + text question, target probability distribution | unclear → unknown (target construction unstated) | new | Valen | 100k image decision records with target distributions and per-record provenance; ChartQA share is GPL-3.0; 99,047 rows pending human audit; target construction unstated. |
| 95 | [hf:datasets/Valen-Team/Valen-Eval-Game](https://huggingface.co/datasets/Valen-Team/Valen-Eval-Game) | HF | 2026-09-23T03:29:09Z | 2026-09-23T12:29:01Z | image (Sokoban screenshots), action choice | no-provider-outputs → clear (declared) | new | Valen | Sokoban solver-labeled training and evaluation set with complete-game levels. |
| 96 | [hf:datasets/JonesLin/next-jev-stage2-merged-verified-20260923](https://huggingface.co/datasets/JonesLin/next-jev-stage2-merged-verified-20260923) | HF | 2026-09-23T06:10:25Z | 2026-09-23T09:35:47Z | image + text (premise/hypothesis NLI, VQA converted to entailment) | unclear → unknown | names only §167/§168 | next-jev (JonesLin) | 414,839 image NLI records: public gold plus unnamed-teacher rationales as training targets. |
| 97 | [hf:datasets/JonesLin/next-jev-stage2-nextjev](https://huggingface.co/datasets/JonesLin/next-jev-stage2-nextjev) | HF | 2026-09-23T17:09:08Z | 2026-09-23T17:22:16Z | image + text | unclear → unknown | named §167 | next-jev (JonesLin) | Trainer-ready pack with a SHA-256 manifest; drops validation rows that share an image with train. |
| 98 | [hf:datasets/FaroukMoc2/jev-stage2-image-beans-pilot](https://huggingface.co/datasets/FaroukMoc2/jev-stage2-image-beans-pilot) | HF | 2026-09-18T05:07:06Z | 2026-09-18T10:44:02Z | image + 3-way choice | no-provider-outputs → clear (declared) | name-only (hourly) |  | 100-image beans Choice pilot; a clean schema template with labels copied from the source. |
| 99 | [hf:datasets/egetheengineer/jevcraft](https://huggingface.co/datasets/egetheengineer/jevcraft) | HF | 2026-09-21T09:06:29Z | 2026-09-23T05:38:46Z | video (1280×720 gameplay recordings) | uses-jev-outputs → barred (ours); restricted (skill users) | named §162 |  | Screen recordings of Jev playing VoxeLibre. Jev Output; imitation use is barred. |
| 101 | [hf:datasets/ngqtrung/video-r1-mc-24f100k-combined](https://huggingface.co/datasets/ngqtrung/video-r1-mc-24f100k-combined) | HF | 2026-09-02T17:07:19Z | 2026-09-02T17:07:29Z | video multiple choice | unclear → unknown | new |  | 106k video MC RL mixture whose decode contract (fps=1, at most 24 frames) differs from the per-source repos. |
| 102 | [hf:datasets/JonesLin/video-vqa-sft-mixed](https://huggingface.co/datasets/JonesLin/video-vqa-sft-mixed) | HF | 2026-09-09T16:51:25Z | 2026-09-12T03:05:43Z | video QA (yes/no/count, multiple choice, direct action) | unclear → unknown | new |  | 356k video QA SFT records; a subagent_id suggests agent-generated reasoning. |
| 104 | [hf:datasets/datapointai/text-to-speech-human-preferences-315k](https://huggingface.co/datasets/datapointai/text-to-speech-human-preferences-315k) | HF | 2026-08-31T20:34:53Z | 2026-09-01T17:34:44Z | audio pairwise preference | uses-other-provider-outputs → labels human; audio hosted-TTS (unknown terms) | new |  | 315k human TTS pairwise preferences; the audio clips are hosted-TTS outputs under provider terms. |
| 107 | [hf:datasets/AI4Manufacturing/IEEE-BRB-mcq-annotated](https://huggingface.co/datasets/AI4Manufacturing/IEEE-BRB-mcq-annotated) | HF | 2026-09-23T13:49:10Z | 2026-09-23T13:49:11Z | image (motor-current signal plots) + multiple choice | unclear → unknown | new |  | Gated signal-plot image MCQ series; card HTTP 401, metadata only. |
| 109 | [hf:datasets/LocalLLaMA/typed-decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) | HF | 2026-09-16T07:42:28Z | 2026-09-22T11:57:46Z | text (listed as a provenance anchor for the multimodal models above) | unclear → barred pending (typed-decisions teacher conflict) | cited from §42; teacher provenance new | typed-decisions lineage | Gold is the mean of three samples from an unnamed ~4B teacher; a third-party README claims it was labelled by Jev. Lineage root for Dohnuts, GPC-1, akasha's branch run. |
| 110 † | [hfds:Valen-Team/Valen-Training-General-100k@c6128642d53e](https://huggingface.co/datasets/Valen-Team/Valen-Training-General-100k) | Web | 2026-09-23T03:09:25Z | 2026-09-23T12:26:03Z | image (VQA, charts, interfaces, games, documents) | no-provider-outputs → unknown (target construction unstated) | dup of #93 | Valen | Web-lane record: 50,203 image references vs 48,445 unique hashes, so splits must be image-hash disjoint. |
| 111 | [hfds:LocalLLaMA/typed-decisions@c76749ec58bd](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) | Web | 2026-09-16T07:42:28Z | 2026-09-22T11:57:46Z | text | unclear → barred pending (typed-decisions teacher conflict) | dup of #109 | typed-decisions lineage | Web-lane record: states are model-written; a score measures agreement with the teacher. |


### 5.3 Evaluation harnesses and eval sets (33)

| # | Item | Lane | Created | Pushed / modified | Modalities | Provenance: lane → verdict | Prior | Family | Summary |
|---|---|---|---|---|---|---|---|---|---|
| 87 | [github:ElSnacko/Open-JEV-VLA](https://github.com/ElSnacko/Open-JEV-VLA) | GH | 2026-09-22 | 2026-09-23T16:09Z | image (robot frames) + proprioception-derived labels | no-provider-outputs → clear (declared) | revisit §163 (fingerprint fb67b383b7b8) |  | E0/E1 KILL: the truncated-depth lm_head cliff is a norm artifact; the full-depth model answers a constant that tracks option wording, not the image. |
| 88 | [github:r33drichards/laya-vision](https://github.com/r33drichards/laya-vision) | GH | 2026-09-19 | 2026-09-23T20:49Z | image | unclear → unknown | revisit §87-§146 | laya-vision (thaitea/r33drichards) | Adds image-dependence controls, option-order margins, typographic-injection probes, a per-dataset ECE noise floor and a GPU-invariance check. |
| 90 | [github:yoheinakajima/glance-speedlab](https://github.com/yoheinakajima/glance-speedlab) | GH | 2026-09-23 | 2026-09-23T19:47Z | live camera image | no-provider-outputs → clear (declared) | new; parent glance §147 revisit |  | Keep/kill latency record on an M5: multi-question batching kept; 2B only as a fast tier (83.3% agreement); fewer image tokens failed the probability-drift guard. |
| 94 | [hf:datasets/Valen-Team/Valen-Eval-General-5k](https://huggingface.co/datasets/Valen-Team/Valen-Eval-General-5k) | HF | 2026-09-23T03:11:15Z | 2026-09-23T12:28:50Z | image + text, typed decision targets | unclear → unknown | new | Valen | 5k held-out records; exact-overlap checks only, no near-duplicate check. |
| 100 | [hf:datasets/Kelly0510/FitAQA](https://huggingface.co/datasets/Kelly0510/FitAQA) | HF | 2026-09-17T15:42:38Z | 2026-09-22T05:03:01Z | video multiple choice + temporal grounding | unclear → unknown | new |  | Fitness action-quality video multiple choice and grounding eval; annotations only. |
| 103 | [hf:datasets/Haopeng/PhoneticQA-L2ARCTIC](https://huggingface.co/datasets/Haopeng/PhoneticQA-L2ARCTIC) | HF | 2026-09-02T07:54:04Z | 2026-09-02T07:55:01Z | audio + 4-way choice | no-provider-outputs → clear (declared) | new |  | 120-item audio multiple-choice probe with balanced answer positions, from L2-ARCTIC annotations. |
| 105 | [hf:datasets/bio-nlp-umass/MedQA-MM](https://huggingface.co/datasets/bio-nlp-umass/MedQA-MM) | HF | 2026-09-01T20:38:05Z | 2026-09-01T22:17:45Z | medical image + multiple choice (identifier-only) | unclear → unknown | new |  | 1,000 shortcut-mitigated medical multimodal MC items, released as identifiers with pinned reconstruction. |
| 106 | [hf:datasets/Multimedia-SMU/culturalmoment-benchmark](https://huggingface.co/datasets/Multimedia-SMU/culturalmoment-benchmark) | HF | 2026-08-25T09:45:10Z | 2026-09-14T08:27:55Z | video multiple choice + temporal localization | unclear → unknown | new |  | Southeast-Asian cultural video MC and moment benchmark; sample only. |
| 108 | [hf:datasets/AIMultiple/aimultiple-decision-models-browser](https://huggingface.co/datasets/AIMultiple/aimultiple-decision-models-browser) | HF | 2026-09-23T09:20:27Z | 2026-09-23T09:20:33Z | browser tasks (web screens), results table, demo video | uses-jev-outputs → Jev Output: evaluation only; barred from training and selection | new |  | Browser-task outcomes for Jev and others; evaluation only, never targets. |
| 112 | [gh:Alpha-Harper-Franklin/jev-multimodal@2fd5d79acb7c](https://github.com/Alpha-Harper-Franklin/jev-multimodal) | Web | 2026-09-21T06:14:57Z | 2026-09-21T09:12:42Z | image (1–8 ordered), PDF/OCR, speech via ASR | no-provider-outputs → clear (declared) | new (owner seen §144) |  | Frozen Qwen2.5-VL-7B with a shared visual prefix: 5.95x faster on POPE at equal accuracy; 'Hosted Jev remains text-only'. CUDA-only backend. |
| 113 | [gh:junpei-9898/gemma-decision-kit@b85176ce7596](https://github.com/junpei-9898/gemma-decision-kit) | Web | 2026-09-23T13:17:11Z | 2026-09-23T23:43:28Z | text, image, short video | unclear → unknown (AI-provisional labels) | new |  | Frozen Gemma 4 NVFP4 three-choice readout; 'AI-provisional' labels, so it measures agreement with an AI labeler. |
| 117 | [web:mikulskibartosz.name/typesafe-jev-guess-what-i-drew](https://mikulskibartosz.name/typesafe-jev-guess-what-i-drew) | Web | 2026-09-19 | 2026-09-19 | image→text serialization vs native image | no-provider-outputs → clear (declared) | new |  | Jev on SVG text about 35%, on base64 PNG about 9% (chance); native vision about 91% (theirs). Do not serialize pixels into a text-only model. |
| 119 | [gh-issue:AntoninPrazsky/BS3D#440](https://github.com/AntoninPrazsky/BS3D/issues/440) | Web | 2026-09-16T17:18:11Z | 2026-09-21T06:40:03Z | screenshots | no-provider-outputs → clear (declared) | new |  | Known-answer screenshot eval: a 256-px crop beats the scaled full frame; crop and resolution are part of the policy. |
| 120 | [arxiv:2609.09417v2](https://arxiv.org/abs/2609.09417) | Web | 2026-09-08 | 2026-09-14 | image (agriculture classification) | no-provider-outputs → clear (declared) | new |  | VLM vision encoders are nearly as separable as DINOv3; a verifier's confidence filter backfired. |
| 121 | [arxiv:2609.00868v1](https://arxiv.org/abs/2609.00868) | Web | 2026-09-01 | 2026-09-01 | image | no-provider-outputs → clear (declared) | new |  | Blurring the relevant region barely changes outputs while a vision-tower probe detects it at 0.72-0.79. |
| 122 | [arxiv:2609.06190v1](https://arxiv.org/abs/2609.06190) | Web | 2026-09-05 | 2026-09-05 | video (VLM reading a physical quantity) | no-provider-outputs → clear (declared) | new |  | Certifying input use needs at least n independent perturbations; closed-form blind-policy score; three VLMs sat below their blind bound. |
| 123 | [arxiv:2609.03261v2](https://arxiv.org/abs/2609.03261) | Web | 2026-09-03 | 2026-09-08 | image+text (medical MCQ) | no-provider-outputs → clear (declared) | new |  | MedQA-MM: full input 62.63%, text-only 53.96%, options-only 29.71%. |
| 124 | [arxiv:2609.09528v1](https://arxiv.org/abs/2609.09528) | Web | 2026-09-08 | 2026-09-08 | video | no-provider-outputs → clear (declared) | new |  | Paired motion-only clips with four-answer credit; single-frame and language shortcuts collapse to 6.25%. |
| 125 | [arxiv:2609.22206v1](https://arxiv.org/abs/2609.22206) | Web | 2026-09-01 | 2026-09-01 | image+text | no-provider-outputs → clear (declared) | new |  | No training-free MLLM uncertainty family dominates; token or option entropy is the short-answer baseline. |
| 126 | [arxiv:2609.18453v1](https://arxiv.org/abs/2609.18453) | Web | 2026-09-16 | 2026-09-16 | image+text | no-provider-outputs → clear (declared) | new |  | Verbalized VLM confidence is trajectory-independent and calibration training can worsen it; ECE and AUROC miss it. |
| 127 | [arxiv:2609.04362v1](https://arxiv.org/abs/2609.04362) | Web | 2026-09-03 | 2026-09-03 | audio (music MCQ) | no-provider-outputs → clear (declared) | new |  | Option-order permutation averaging: 55.7% to 59.2% and better error ranking on music MCQ. |
| 128 | [arxiv:2609.00727v1](https://arxiv.org/abs/2609.00727) | Web | 2026-09-01 | 2026-09-01 | audio (speech style) | no-provider-outputs → clear (declared) | new |  | Late audio-encoder layers encode speaking style that is lost before the output: probe the encoder. |
| 129 | [arxiv:2609.16582v1](https://arxiv.org/abs/2609.16582) | Web | 2026-09-15 | 2026-09-15 | audio (spoken sarcasm) | no-provider-outputs → clear (declared) | new |  | Lexical vs prosody counterfactual arms show Qwen3-Omni leans on words. |
| 130 | [arxiv:2609.06011v1](https://arxiv.org/abs/2609.06011) | Web | 2026-09-05 | 2026-09-05 | image, audio, text (omni conflict) | no-provider-outputs → clear (declared) | new |  | Omni LLMs show a robust visual bias in tri-modal conflicts. |
| 131 | [arxiv:2609.00550v1](https://arxiv.org/abs/2609.00550) | Web | 2026-09-01 | 2026-09-01 | image (rendered text) vs text | no-provider-outputs → clear (declared) | new |  | MLLMs accept contradicting context more readily as an image; modality preference is arbitrary. |
| 132 | [arxiv:2609.24277v1](https://arxiv.org/abs/2609.24277) | Web | 2026-09-21 | 2026-09-21 | screenshots (GUI click coordinates) | no-provider-outputs → clear (declared) | new |  | Place-value-weighted digit entropy for GUI click coordinates beats K-sample baselines. |
| 133 | [arxiv:2609.06922v1](https://arxiv.org/abs/2609.06922) | Web | 2026-09-07 | 2026-09-07 | image (VQA) | no-provider-outputs → clear (declared) | new |  | 4-bit quantization moves yes/no gaps toward the image-ablated output: recalibrate the artifact you serve. |
| 134 | [arxiv:2609.15180v1](https://arxiv.org/abs/2609.15180) | Web | 2026-09-14 | 2026-09-14 | image + EHR (clinical VLM) | no-provider-outputs → clear (declared) | new |  | The correctness criterion flips uncertainty-method rankings; an LLM judge accepted 16 of 30 human-found errors. |
| 135 | [arxiv:2609.17004v1](https://arxiv.org/abs/2609.17004) | Web | 2026-09-15 | 2026-09-15 | image (left-right claims) | no-provider-outputs → clear (declared) | new |  | Training-free selective prediction from symmetry interventions with Clopper-Pearson thresholds. |
| 136 | [arxiv:2609.05535v1](https://arxiv.org/abs/2609.05535) | Web | 2026-09-02 | 2026-09-02 | screenshots (web-agent guardrail) | no-provider-outputs → clear (declared) | new |  | VLMs with near-identical AP differ 9x in evidence-aligned detection; report verdict, localization and counterfactual separately. |
| 137 | [arxiv:2609.01315v2](https://arxiv.org/abs/2609.01315) | Web | 2026-09-01 | 2026-09-09 | text, image, video, audio | no-provider-outputs → clear (declared) | new |  | Unified multi-backend multimodal eval harness; abstract only. |
| 138 | [arxiv:2609.17708v1](https://arxiv.org/abs/2609.17708) | Web | 2026-09-15 | 2026-09-15 | text, multimodal QA, agents | no-provider-outputs → clear (declared) | new |  | Confidence from the model's own graded past episodes: an outcome-ledger layer. |
| 139 | [arxiv:2609.10410v2](https://arxiv.org/abs/2609.10410) | Web | 2026-09-09 | 2026-09-11 | image+text (social posts) | no-provider-outputs → clear (declared) | new |  | 4,000 human-labeled Bluesky posts for workload-style multimodal moderation eval. |


### 5.4 Skills, guides and catalogs (5)

| # | Item | Lane | Created | Pushed / modified | Modalities | Provenance: lane → verdict | Prior | Family | Summary |
|---|---|---|---|---|---|---|---|---|---|
| 91 | [github:carcinize-corp/Jev-omni](https://github.com/carcinize-corp/Jev-omni) | GH | 2026-09-18T14:35:38Z | 2026-09-23T21:55Z | n/a (research notes; mirrors X/GitHub watch dumps) | no-provider-outputs → clear (declared) | own org (not independent evidence) |  | The maintainer's own notes repo; no model or trainer. |
| 114 | [gh:notsointresting/awesome-jev-family@849c14d33d](https://github.com/notsointresting/awesome-jev-family) | Web | 2026-09-22T15:53:24Z | 2026-09-22T16:04:38Z | list (multimodal members: PlayJev, Visual-JEV, OmniJev, Jev-Omni, PocketJev, laya-mlx) | no-provider-outputs → clear (declared) | new |  | Catalog with a multimodal section; blurbs overstate. |
| 115 | [gh:OmniJev/awesome-jev-gallery@b3adf7943ba7](https://github.com/OmniJev/awesome-jev-gallery) | Web | 2026-09-17T20:16:57Z | 2026-09-23T14:47:18Z | list | no-provider-outputs → clear (declared) | new |  | Gallery (249 stars) through which the Dohnuts RX 7900 XTX line surfaced; catalog only. |
| 116 | [web:seangoedecke.com/system-one-models-can-train-their-own-replacements](https://www.seangoedecke.com/system-one-models-can-train-their-own-replacements/) | Web | 2026-09-20 | 2026-09-20 | text (argument generalizes to any modality) | uses-jev-outputs → bad pattern (recommends Jev distillation) | new |  | Recommends distilling Jev input/output into classifiers without mentioning terms: the barred route, cited as the bad pattern. |
| 118 | [web:seangoedecke.com/two-techniques-for-working-with-system-one-models](https://www.seangoedecke.com/two-techniques-for-working-with-system-one-models/) | Web | 2026-09-18 | 2026-09-18 | text; notes image/audio swap | no-provider-outputs → clear (declared) | new |  | Claims an image or audio swap is 'trivial'; unmeasured. |


## 6. Recipe cards (12)

Deep read-only inspections by the card lanes, reproduced with markdown escaping
(raw text in `tmp/mm-synth/task_input.json`). Card text
overrides the item rows (section 3). Labels inside the cards follow the same
vocabulary: Reported, Contract, Hypothesis, Measured-here.

### 6.1 github:Barneyjm/circuit (table #1)

**Revision.** Inspected at HEAD 3ceb08deff63f022c65ed6afae5b2735f0d3b855 (2026-09-24T00:48:35Z). That is two commits past the task pin 65e25461: v2.2 open-taxonomy data, head-only training and plug-in heads, then `--freeze-adapter` without `--init`. README blob fecb09ed207b is unchanged. HF (checked 2026-09-23): jbarney/circuit-vl-4b main 4b12a734772d, tags v1.0 87d819cd, v1.1 fd9972c6, v1.2 cd37f2f1; circuit-audio-7b 29876b3dbade; circuit-1.7b 7a847cbd20c4; circuit-8b f64b4596186a. Apache-2.0, 1 star, created 2026-09-19.

**Inspected.** Read: README, REPRODUCE.md, pyproject.toml, s1proto/media.py (all), service.py build_answers media branch, scorer.py MultimodalScorer, scripts/train_lora.py (all 728 lines), s1proto/data/vision_grid.py and audio_grid.py (docstrings, cells, real-media pools, generate()), teachers.py, gen_data.py, relabel_family.py, build_hf_eval.py grep, build_open_taxonomy.py docstring, docs/wide-mix.md grep, .gitignore, and both commit diffs since the pin. Parsed: committed data/vision/grid/{train,eval}.jsonl, all rows. Streamed and tallied: data/publish_train.jsonl (16,738) and publish_train_v2.jsonl (19,738). HF README and config.json for circuit-vl-4b and circuit-audio-7b. Result files: pope_\*.json, perm_circuit-{vl-4b,audio-7b}-par.json, grid_circuit-vl-4b-par.json. Base processor configs: Qwen3-VL-4B-Instruct preprocessor and video_preprocessor, Qwen2-Audio-7B-Instruct preprocessor. Not read: text grid.py, docs/cold-eval.md, eval_set.py, parallel.py internals. No execution, no weights.

**Modalities.** Text; image (one per request); audio (one clip per request). 'Video' means one caller-chosen still frame. There is no frame sampler and no multi-image state in the wire format.

**Backbone.** Text: Qwen3-1.7B-Base and Qwen3-8B-Base. Vision: Qwen3-VL-4B-Instruct. Audio: Qwen2-Audio-7B-Instruct. LoRA r16, alpha 32, dropout 0.05 on the language model's q/k/v/o/gate/up/down only. The vision and audio encoders are frozen (regex `.*language_model.*`). Trainable (card): 33M for vl-4b, 40M for audio-7b.

**Head or readout.** Pointer head: Linear(hidden->256) q and k. Logit = q(decide-token state)·k(each option's closing delimiter)/16, softmax over options, up to 255 options, no cap otherwise. Delimiters: vl uses &lt;|box_start|>/&lt;|box_end|>/&lt;|fim_middle|>; audio uses Qwen2-Audio's unused timestamp tokens &lt;|29.98|>/&lt;|29.99|>/&lt;|30.00|>. v1.2 sets parallel_options=true: options are encoded side by side with a custom 4D mask and positions (Qwen3-VL M-RoPE from get_rope_index), so order cannot matter. The v2 types (multi via sigmoid+bias, locate, rank via Plackett-Luce, match) are text-only: train_lora raises for vision/audio. Released 'confidence' is the pointer-softmax max. It is not a measured rate.

**Input coverage.** Measured from code. media.py/service.py accept exactly one {image|audio: data URI or https URL, text?} per state. A state carrying both image and audio is rejected. A list of frames is not recognized as media and gets HTTP 422 on a vision model. The HF vl-4b card says 'one or more images (video as sampled frames)', but the served code does not do that. IMAGE: no resize in circuit. The Qwen3-VL processor default budget applies: shortest_edge 65,536 px area, longest_edge 16,777,216 px area, patch 16, merge 2. Nothing caps tokens for large photos. Rendered grid images are 420-520 px wide. Training vision rows carry no text truncation (max_length applies only to the text path). AUDIO: resampled to 16 kHz mono and not clipped by circuit. The Qwen2-Audio WhisperFeatureExtractor (chunk_length 30, n_samples 480000, padding max_length) keeps only the first 30 s. That limit is inferred from the base processor config, not stated in the repo. Evidence after 30 s is unseen. Media limit: 25 MB; the server fetches only data URIs and URLs.

**Training data and labels.** Released vl-4b v1.1/v1.2 (card): vision grid v2, 1,408 train + 152 val, 16 families from 13 generator cells. Rendered receipts, charts, tables, forms and shape scenes are labeled by the drawing code. 700 Open Images V7 validation photos with human-verified positive/negative image labels drive the present/classify/negation cells. About 8% of items are made undecidable, with two different targets: photo cells use a heavy blur or a 1/5 crop with the rest black, labeled 0.5 or uniform; rendered 'read' cells blur the field and label an explicit 'Cannot tell' option one-hot. The committed data/vision/grid is grid v1: 1,200/300 rows, all refs 'code', 0 photo rows, 20/1,200 ambiguous (1.7%). The v2 files, rendered PNGs and photos are gitignored and regenerated from a seed plus a downloaded index.json that is not in the repo. Photo-label provenance therefore rests on generator code, not a committed file. Audio-7b: audio grid v2, 1,400 clips, 14 cells. Sources: Kokoro-82M (27 voices) templated calls, lists and number readbacks; LibriSpeech dev-clean plus Common Voice (read if present), labeled from transcripts; FSDD digits; numpy beeps and noise; about 8% undecidable. Split caveat: generate() draws photos, LibriSpeech/CV utterances and FSDD speakers from one shared pool for both train and eval, with only different seeds. 'Held-out' means new draws, not source-disjoint (the card: 'held-out items, not held-out structure'). Text models: publish_train_v2 = 8,938 code-labeled grid rows, 2,100 human rows (wide mix), and 8,700 HF human-label rows.

**Jev-output provenance.** no-provider-outputs for the released vision and audio models: code labels plus Open Images human labels (vision), code and transcript labels (audio); both cards say no teacher outputs. Text sets re-verified this pass, all rows of both files: refs slots are human 2,100 / code 8,938 / jev+gemini 5,700 (v1) and 8,700 (v2). jev≠gemini in 0 rows. All soft values in the jev slot are civil_toxic annotator fractions (796 rows); the rest are one-hot. build_hf_eval.py:38 says 'no teachers here; human label stands in for both'. Residual risk: the Jev+Gemini teacher pipeline still ships (teachers.py posts to api.typesafe.ai; gen_data.py; relabel_family.py). .gitignore keeps 'datasets with teacher-model (Jev/Gemini) targets' local: data/train.jsonl, eval.jsonl, train_real_plus_syn.jsonl, human_subset.jsonl, open_tax_tagger_eval.jsonl (the last is WildChat text with Jev tags as an eval reference). train_lora.py's docstring still says the targets are 'the averaged Jev+Gemini reference'. Record the labels as human/code. Do not reuse the 'jev'/'gemini' slot names for human labels in Augustus fixtures, because they defeat a provenance audit.

**Calibration.** Soft-target CE (mixed_loss). Checkpoint rule pick_checkpoint: the lowest worst-question-type ECE (15 bins, types with ≥50 val rows) among checkpoints within 0.01 of the best validation accuracy. The validation split is family-stratified at 10%, carved from the training file, and the same split fits the per-type temperature (grid 0.4-3.0 minimizing KL; T=1 kept if KL at T=1 &lt;0.02 or &lt;50 rows). Measured in the released config.json: vl-4b and audio-7b temperatures are all 1.0, so there is no post-hoc scaling; calibration is the training loss plus checkpoint choice. The vl-4b card (v1.1) gives mean confidence 0.88 on undecidable items that should be about 0.5. Audio v1.1: 0.54, against 0.69 for the raw base.

**Eval evidence.** Reported (card; theirs, not reproduced). vl-4b v1.1 on its own grid: 96.4% / ECE 0.036 vs raw base letter logits 92.6% / 0.079 (390 items); photos 89.5% / 0.105 vs 81.4% / 0.192 (86 items). v1.2 header: .967 / .021, order flips 0.0% (v1.1 3.6%). audio-7b v1.1: 94.5% / 0.039 vs 73.2% / 0.199 (385 decidable); 88.8% / 0.073 vs 68.1% / 0.232 on all 420. v1.2: .898 / .050, flips 2.9% (v1.1 11.7%). Counting beeps: 44%. Committed result files, read here: POPE, 300 COCO items the grid never saw (accuracy / ECE / Brier): raw Qwen3-VL-4B 0.913 / 0.072 / 0.139; v1.1 0.923 / 0.049 / 0.128; v1.2 (current main) 0.907 / 0.069 / 0.158. The order-invariant v1.2 is at or below the raw base on the one external set. grid_circuit-vl-4b-par photo cells: present 0.828 / ECE .131 (n=29), negation 0.893 / .135 (n=28). perm_circuit-audio-7b-par: ambiguous-item flip rate 0.30 (n=20). REPRODUCE.md: the v1.1 text weights were trained after the unseen benchmark found the gaps, 'so they are a response to it and not a blind result'.

**Compute and ROCm feasibility.** Reported: vl-4b 85 min, audio-7b 55 min, on an 'Apple laptop GPU' (spec not stated); ~1.0 s/item and 1.2 s/clip inference on M-series. Device order is cuda->mps->cpu (ROCm-torch reports cuda). No flash-attn; attention is the transformers default (sdpa). bitsandbytes appears only behind --load-4bit, whose branch loads AutoModelForCausalLM before the modality branches, so QLoRA is text-only in practice. The parallel-options 4D float mask forces a non-flash sdpa path on any backend. Deps pin torch>=2.14 and transformers>=5.17, so first check that a ROCm torch 2.14 wheel exists for gfx1151. tabputer-1 (Hypothesis): bf16 LoRA on vl-4b (~9 GB weights) and audio-7b (~16 GB) fits 115 GB easily. Cheapest pilot: `--freeze-adapter` head-only, which has no backprop through the model. Mac M4 24 GB (Hypothesis): vl-4b is plausible at batch 2-4 with grad checkpointing; audio-7b bf16 is tight. Nothing verified on gfx1151.

**License.** Code Apache-2.0; adapters Apache-2.0; bases Apache-2.0 (Qwen3-VL, Qwen2-Audio). Data: Open Images images CC BY 2.0, per Flickr author, attribution required; labels CC BY 4.0. LibriSpeech CC BY 4.0. FSDD CC BY-SA 4.0 (share-alike). Common Voice CC0. Kokoro-82M Apache-2.0. The text eval sets include non-commercial ChaosNLI (eval-only, not committed); docs/wide-mix.md lists per-source verdicts and a --commercial cut.

**Borrow for Augustus.** (1) A render-time-labeled generator grid (operation × format) is the fastest honest multimodal fixture: labels are known by construction. Pair it with an external set (POPE-like) before claiming a gain. The falsifier here is already in their files: v1.2 does not beat the raw base on POPE Brier. (2) pick_checkpoint: worst-type ECE with an accuracy floor, which rules out a checkpoint 'well calibrated about knowing nothing'. (3) Undecidable cells at about 8%, with the target made explicit: a flat distribution and an explicit 'Cannot tell' option are different contracts, so the skill should say which one it trains. (4) Parallel option encoding buys order invariance; report its accuracy/Brier cost on unseen data. (5) Plug-in pointer heads over one frozen adapter, plus head-only training on a frozen base, give a cheap per-customer head. (6) A source-disjoint split rule for multimodal data: split by photo, speaker and utterance, not by seed. (7) State input coverage in the model record: one image or clip, 30 s audio window, pixel budget.

**Provenance evidence.** Commit list via gh api (3ceb08de, 65e25461, 09aa92d2, b97f72b2). Tree SHA list (README fecb09ed207b, train_lora.py def4859f8293, media.py 1ab6dfeaf49d, vision_grid.py 1805130487a2, audio_grid.py 379dfdea98af, teachers.py 594d9a2de0e6). Stream tallies of publish_train\*.jsonl run 2026-09-23. HF /api/models full=true and /refs for all four jbarney/circuit-\* repos.

**Risks.** The card claims multi-image/video, which the code does not implement. Train/eval share photo, speaker and utterance pools. The released v2 data is not committed. The undecidable-item overconfidence (0.88) is unsolved. The per-cell n is tiny (28-30). The teacher pipeline is present and one docstring is stale. The released weights moved (v1.0->v1.2) after benchmarks, so pin a revision. Two commits landed after the task pin, on 2026-09-24.


### 6.2 github:OmniJev/PlayJev (table #2)

**Revision.** HEAD 616db06b2c27fd8ba56cfa882558c5688281ac61 (2026-09-21T13:59:58Z); README blob 89145a348543. HF OmniJev/PlayJev-0.8B sha ea8951e786e1 (created 2026-09-19, lastModified 2026-09-21T14:00:08Z, 428 downloads). Its README is identical to docs/HF_MODEL_CARD.md (diff empty), and it ships playjev_train.json with the release run's args and per-game val metrics. Space OmniJev/PlayJev f19ec8d8d393 is RUNNING. Apache-2.0, 29 stars, created 2026-09-17.

**Inspected.** Read: README, requirements.txt, playjev/model.py (all), train_sft.py (docstring, slot_logits, soft_ce, evaluate header, check_linear_attention_kernels, main setup, CLI), data.py (grep: split, rewrites, targets), collect.py/env.py (grep: frame size, JPEG, epsilon), teachers/__init__.py, teachers/snake.py target lines 58-60, scripts/build_aux.py docstring, scripts/general/eval_typesafe.py header, scripts/relabel_replays.py header, docs/BASELINES.md. HF: playjev_train.json and processor_config.json. Not read: the other nine teachers, mixdata.py, play.py, zeroshot.py, probe_options.py, reproduce.sh. No execution, no weights.

**Modalities.** Image (a single game frame, pixels only) for decisions. Text-only and general-image MC items as replay. No audio (the games are muted and every sound file was deleted).

**Backbone.** Qwen3.5-0.8B-Base (a VLM with gated-delta-rule linear-attention layers). Full fine-tune, including the vision tower (freeze_vision=false in the release config). fp32 master weights and optimizer, bf16 autocast, fp32 letter readout.

**Head or readout.** No new head. Logits for the space-prefixed letters ' A'..' Z' at the last position (plain template ending 'Answer:'), projected through the tied output embedding in fp32 because bf16 logits quantize to 0.125 and tie. Softmax over the K letters. allowed_mass (the share of the full vocabulary on the K slots) is a diagnostic. confidence = (p_max − 1/K)/(1 − 1/K), Jev's Choice formula, which is not a measured rate. Options are shuffled per sample.

**Input coverage.** Measured from code and release config. One frame per decision: a 448-px long-side JPEG at q85 (env.py FRAME_LONG_SIDE=448, JPEG_QUALITY=85; canvas screenshots are taken at q90, then resized). two_frame=false in the release, so no motion evidence. Temporal 2-frame stacking into the vision tower's temporal patch is implemented but off. The model never gets the game name or rules. Per-game options are K=2-7 (kmax 9 with rewrites); letters cap at 26. Replay images are re-encoded to 448 px. The Qwen3-VL-class processor budget is 65,536-16.7M px area, so 448-px frames go in whole. Consequence (Hypothesis): velocity and direction are invisible in reflex games. That fits Floppy Bird 0.18 and Breakout 0.14 vs teacher despite high per-frame agreement.

**Training data and labels.** Labels come from code on privileged state. One search program per game reads the hook's info() (internal state the model never sees): BFS (Snake), expectimax (2048), Dellacherie (Tetris), A\* (Sokoban), exact physics (Flappy), ghost occupancy (Pacman), ball flight (Breakout), dodge-and-aim DP (Invaders), lookahead steering (Racer), physics rollouts (Mario). Soft target: 0.9 split over tied winners and 0.1 over the rest (snake.py:58-60; README '0.9/0.1/0'). Collection: 100k frames/game with 2-30% epsilon-random moves. DAgger: the model plays 40k frames/game per round and the teachers relabel them. Release (playjev_train.json): 1,127,435 game records (train 1,019,325 / val 108,110, split by episode seed %10), shards sft_all1_a + dagger1-3, continued from ckpt rel2 (restart-from-base on all frames), 26,544 steps, batch 64, lr 1e-5, boost_last 10×4 on short episodes. Mix 0.6 game / 0.2 image / 0.2 text. Replay: A-OKVQA train and ScienceQA train (image); MMLU auxiliary_train, SciQ, ARC (text). Answer keys are human, with aux_soft=0.9 smoothing. Option-rewrite augmentation 0.12/0.08/0.05/0.05.

**Jev-output provenance.** no-provider-outputs. Targets are search-program outputs and public dataset answer keys. scripts/general/eval_typesafe.py scores the TypeSafe public evaluation rows (evals.typesafe.ai, 365 rows) and compares against Jev answers already recorded on that page. It is eval-only and makes no API call. The rows file runs/general/typesafe365.jsonl is under gitignored runs/, so it was not inspected. Do not fold those recorded Jev answers into any training mix.

**Calibration.** No post-hoc temperature. Soft CE to smoothed teacher targets (an optional Brier term, 0 in the release). Calibration here is P(move = teacher argmax) on logged or DAgger states, not P(win) or a score outcome. Per-game val ECE (15 bins) from playjev_train.json: sokoban .025, 2048 .055, snake .069, flappy .073, breakout .075, pacman .087, tetris .099, racer .107, mario .117, invaders .129 (n≈170-230 each).

**Eval evidence.** Reported (theirs). Closed loop: 16 held-out episodes/game, cap 1,500 steps, argmax move. vs-teacher = (model − random)/(teacher − random), mean 0.57 (v3), up from cloning 0.37 / v1 0.49 / v2 0.53. Per game: invaders, racer and sokoban 1.00; snake 0.90; pacman 0.56; tetris 0.37; mario 0.32; 2048 0.21; flappy 0.18; breakout 0.14. The teacher hits the 1,500 cap in tetris, flappy, pacman and breakout, so those ratios are cap-bounded. General ability (200 Qs each): base MMBench dev 0.66 / MMLU 0.33. Replay sweep (1,500 steps each): games-only 0.48/0.29, 10% 0.65/0.42, 20% 0.78/0.44, 30% 0.83/0.47; game agreement 0.430 / 0.431 / 0.586 / 0.547. Confidence-ranked handover to the teacher recovers teacher score, random handover does not (chart). One step of latency breaks the reflex games. 43 ms/move on H200. Read from HF playjev_train.json: val teacher-agreement 0.783 overall (n=2,000). Flappy is 0.973 per frame yet 0.18 closed-loop; Breakout 0.672 -> 0.14; Sokoban 0.976 -> 1.00. Per-frame agreement does not predict closed-loop outcome.

**Compute and ROCm feasibility.** Reported: restart-from-base on about 1.8M frames takes 12 h on one H200, plus 7 h for one more round. About 17 GB to train at batch 64 and 3 GB for inference. Stack: torch 2.10 cu128, flash-linear-attention 0.5.2, triton 3.7.1, Playwright Chromium. ROCm and gfx1151 (untested, Hypothesis): the binding constraint is the FLA Triton gated-delta-rule kernels. train_sft runs check_linear_attention_kernels whenever device.type=='cuda' (true under ROCm). It compares the fla kernel against the torch reference forward and backward at tol 5e-2 and aborts on mismatch, so run it first. PLAYJEV_NO_FLA=1 forces the torch reference, which is correct but slow. causal_conv1d is optional. autocast('cuda') and fused AdamW should map to ROCm torch; verify. A separate risk: circuit's --micro help says the Qwen3.5 backward returns NaN gradients on left-padded batches, and PlayJev left-pads at micro 16-32 on H200 without reporting NaN, so watch loss on ROCm. Memory is trivial on 115 GB. Time: full reproduction is likely days on the iGPU, so pilot one game's cloning epoch (100k frames). Collection needs headless Chromium on CPU. Mac M4 24 GB: the code defaults to cuda:0 and disables autocast off-CUDA; training is not a supported path. Inference is plausible (Hypothesis).

**License.** Code and weights: Apache-2.0. Vendored game code: MIT / WTFPL / Unlicense / Apache-2.0 per game. The README says three games' art is not the authors' to license: Mario sprites (Nintendo), Floppy Bird (Dong Nguyen/.GEARS), Racer (OutRun placeholder). That art is in the training frames. Replay datasets carry their own terms; ScienceQA and SciQ licenses were not verified this pass and should be checked before any commercial reuse.

**Borrow for Augustus.** (1) Privileged-information teachers: labels computed by code on hidden state plus DAgger on the model's own visits. This is the clean, provider-free recipe for sequential decisions whenever a simulator exposes state. (2) Evaluate observed action success (closed-loop outcome), not label agreement. Flappy's 0.973 agreement vs 0.18 outcome is the counterexample to treating agreement or ECE as success. (3) The replay-share sweep is the forgetting control and its own falsifier: games-only replay drops MMBench below base (0.48 vs 0.66). (4) Kernel-parity check before any backend's first step; directly reusable for ROCm bring-up. (5) Controls: shuffle-labels, one-step label delay, confidence-ranked vs random handover (a routing-policy test). (6) Input coverage belongs in the decision record: single frame, 448 px, no audio. Confidence here is Jev's normalized p_max, which is not a rate.

**Provenance evidence.** gh api commits (616db06b, 01ff11e0, c5bf8c64, 2d7a0280) and tree SHAs (README 89145a348543, model.py 4e270ea29a59, train_sft.py ebb025d0e52d, data.py adb9bbd947b9, env.py 7e9a8ebe60da). HF /api/models/OmniJev/PlayJev-0.8B full=true, playjev_train.json, processor_config.json; /api/spaces/OmniJev/PlayJev.

**Risks.** Copyrighted art in the training frames. Released on a single frame (no motion evidence). Vs-teacher ratios are cap-bounded and there are only 16 episodes per game. The general-ability sets are 200 items each. The CUDA/FLA stack's fit to gfx1151 is unknown. The training loss is agreement with a program, so the release has no outcome-calibrated probability.


### 6.3 github:nullsilver-labs/alpha-sys-1 (table #3)

**Revision.** GitHub HEAD d7fe8575cc70a00daa68f6ad9cbe1e5c14eb33e1 (2026-09-19T09:09:05Z); README blob 06d4e3afd1f1; 0 stars. HF (checked 2026-09-23): nullsilver/alpha-sys-1-450M main ec158b26d094 (tag 260919 -> 0d76b56c); -1.6B main 774c73fcbbbd (tag 260919 -> 09a987ca); -3B main 7dd0cf152e79 (tag 260920 -> 9cd9a3d6, created 2026-09-20T07:28Z). Correction to the prior: the 3B is released (seed 1 of 3, best step 3,600 of 10,500, best dev CE 0.4266). The GitHub README ('3B is in training') is stale.

**Inspected.** Read: README, PLAN.md (all), sys1/train.py (all), sys1/readout.py (render, Readout, IMAGE_SIDE), pyproject, runs/p3/GATE-lora-1.6B.md, runs/p2/GATE-3env-1.6B.md (all), GATE-7env-1.6B.md verdict lines, CARD.draft.md header, the tree listing (runs/p0/raw/jev), HF 3B README (training, eval, limitations), and 3B run.json. Not read line by line: the env adapters (envs/\*.py), LOG.md, release.py, gate_p2.py, metrics.py. No execution, no weights.

**Modalities.** Text (including tabular serialized as text); image (CIFAR-10/-C, Camelyon17-WILDS histopathology); text+image. One image per row.

**Backbone.** LiquidAI LFM2.5-VL-450M (350M LM + 86M SigLIP2, 512 px native per PLAN), -1.6B, -3B. Release: LoRA r32, alpha 32, dropout 0, on the LM plus the multimodal projector (q/k/v/out_proj, in_proj, w1-w3, linear_1/2). Vision tower frozen. Merged into the base weights for release. lr 1e-4, batch 32 (3B micro 4), cosine schedule, sqrt(rows) environment sampling, soft_upsample 10 for 100-annotator rows, three seeds; the released seed is lowest mean dev CE.

**Head or readout.** No new head. Next-token logits at the first assistant position over single-token labels: choice letters A.. in listed order, noul No/Yes, score letters lowest level first (score = expectation). Loss: full-vocabulary CE with y_soft on the label tokens, which equals restricted CE minus log(label mass), so one term teaches both the distribution and answering in-format. label_mass is logged as a diagnostic. 'confidence' = 1 − H(p)/log n, a statistic of the distribution, not a rate.

**Input coverage.** Measured from code. At most one image per row (Readout.messages). Images whose long side is under 256 px are resized to 256×256 bicubic (IMAGE_SIDE=256, 'so the encoder sees 64 tokens'). CIFAR 32 px and Camelyon 96 px patches are therefore upsampled, square. Larger images go to the LFM2.5-VL processor default (512 px native per PLAN; tiling not verified here). Choice supports at most 26 options (single-token letters). The >26 fallback (noul per option, then normalize) is planned, not built. Dict states render as 'key: value' lines. The HF card notes probabilities move by a few hundredths in bf16 with batch composition and padding.

**Training data and labels.** Labels come from datasets and outcomes (PLAN §4; train.py y_soft). mcq (ARC-Easy, SciQ, OpenBookQA, CommonsenseQA): one-hot. ChaosNLI: the 100-annotator distribution, soft rows only (the 40k one-hot SNLI/MNLI rows were removed after P1 because they taught certainty ChaosNLI punishes). CivilComments-WILDS: annotator share. STS-B: annotator mean as a score distribution. Folktables ACS income, CA 2014: outcome. CIFAR-10: one-hot. Camelyon17-WILDS: outcome (tumor patch label). Choice order is re-randomized on every draw. Dev CE is computed per environment and averaged for early stopping.

**Jev-output provenance.** no-provider-outputs in training targets. Separately recorded: raw jev-latest zero-shot predictions are committed in the public repo as eval artifacts under runs/p0/raw/jev/{boolq,chaosnli,civilcomments,folktables,mcq,stsb,yelp}.{dev,test}.jsonl (14 files, about 20 MB, text environments only). That is stored Jev Output. Exclude that path from any Augustus data pull and never use it as a target. CARD.draft.md says Jev is kept out of the HF tables 'at TypeSafe's request'. PLAN P5 (frontier-model teacher replay) is planned, not landed.

**Calibration.** Early stopping on the mean of per-environment dev CE; no post-hoc temperature in the released weights. Baselines always include base+T (one scalar fitted on that environment's dev split). NLL and Brier (split into reliability and resolution) carry the claims. ECE (15 equal-mass bins) is never reported alone. The HF card tells users to fit their own temperature on a few hundred labeled examples (alpha_sys_1.fit_temperature).

**Eval evidence.** Pre-registered gates, read from committed reports. P2 tier B (mixture ≈ single-domain), 1.6B, 7 environments: FAIL. 4/7 environments fall outside the rule; seed-mean mixture-minus-single CE is chaosnli +.026, cifar10 +.043, civilcomments +.009, folktables +.006. The 3-environment tier B also fails. P2 tier C (leave-one-domain-out vs base plus transferred temperature), 3-environment 1.6B: FAIL. The mcq fold passes 3/3; chaosnli (+.10 to +.28 CE) and cifar10 (+.02 to +.16) fail 0/3. Tier C for 7 environments: 'incomplete (runs missing)'. P3 shift: PASS. CIFAR-10-C mean confidence falls monotonically, and the severity-5 gap is +.031 to +.054 vs zero-shot +.078. Camelyon per-hospital gaps are +.004 to +.044; Folktables 2018 state gaps +.010 to +.045. 3B card test NLL, tuned vs base+T: mcq .289/.386, ChaosNLI .735/.795, CivilComments .319/.423, STS-B .961/1.576, Folktables .441/.610, CIFAR-10(+C) .197/.261, Camelyon17 .193/.686. Unseen tasks go the other way: BoolQ .405 vs .393 and Yelp .973 vs .961, both worse than base+T. Qwen3.8-27B+T beats the 3B on mcq, ChaosNLI, BoolQ and Yelp. The README's 'within .02-.04 NLL of specialists' reads the failed tier-B gate generously.

**Compute and ROCm feasibility.** Reported: two 24 GB CUDA cards (gpu0/gpu1 queues). 450M full fine-tune fits 24 GB; 1.6B needs LoRA on 24 GB. autocast('cuda') and device 'cuda:0' are hard-coded; no flash-attn or bitsandbytes in the deps (wilds, folktables, lightgbm are). ROCm (Hypothesis): ROCm-torch exposes the 'cuda' device string, so train.py and readout.py should run. LFM2's conv+attention hybrid is in transformers>=5 without required custom kernels (not verified), so the risk is lower than for FLA-based recipes. Unverified on gfx1151. tabputer-1: 3B LoRA plus the seven environment downloads (Camelyon17-WILDS is the large one) fit easily. Mac: training assumes CUDA autocast; inference is plausible via transformers on MPS (Hypothesis).

**License.** The GitHub repo has no LICENSE file (NOASSERTION). HF weights: license 'other' / lfm1.0 with LICENSE and NOTICE; LFM1.0 commercial terms were not fetched, so verify them before any reuse. Data licenses per source are not audited here. ChaosNLI is commonly treated as non-commercial (circuit's wide-mix marks it eval-only).

**Borrow for Augustus.** (1) The strongest methodology template of the four: gates written before runs, with dated amendments that keep the original verdict; tiered claims (A per-domain, B mixture ≈ specialist, C transfer); a clustered bootstrap over the real unit (question, comment, hospital, state-year); base+T and a constant base rate as mandatory baselines; NLL and Brier over ECE. (2) A negative worth a design rule: a mixture calibrated on seven domains does not transfer. The tier C fail and the unseen BoolQ/Yelp results mean the skill must require per-deployment recalibration on the user's own labels, not ship a promise of general calibration. (3) Don't pad soft-label environments with single-annotator rows. (4) Sqrt environment sampling so a small environment isn't over-passed. (5) Freeze the vision tower so confidence stays sensitive to corruption (P3 passes). (6) Full-vocabulary CE = restricted CE − log label mass. (7) Record the input-coverage transform (256-px square upscale) in the model record.

**Provenance evidence.** gh api commits (d7fe8575, 561490ad, 57fcec05, a078c468) and tree SHAs (README 06d4e3afd1f1, PLAN.md f9ac604e4542, sys1/train.py 7378ba160ccd, sys1/readout.py 9ed47e02d336). HF /api/models full=true and /refs for all three sizes; 3B run.json.

**Risks.** The README understates the gate failures. Jev Output is committed in a public repo. The weights are under a non-Apache license. The 3B release postdates the repo docs. The env adapters were not read line by line, so per-environment label construction (especially STS-B and Camelyon grouping) is not independently checked here.


### 6.4 github:guanxuyu-sv/Visual-Jev (table #4)

**Revision.** HEAD be3cec71a18f042a85da3f2c9c1172267f4cb7a8 (2026-09-23T22:55:51Z); README blob efc423019140; created 2026-09-21T07:25:57Z; 7 stars; Apache-2.0. HF guanxuyu/visual-jev-4b-answer-sft sha bd2ead973224 (created 2026-09-23T07:29Z, lastModified 22:05Z; seed 0 at root, seed1/ and seed2/; 0 downloads). Paper arXiv 2609.25845 was not fetched and the manuscript is not in the repo, so every paper number is Reported. Not jiangxiluning/Visual-Jev.

**Inspected.** Read: README, REPRODUCE.md, code/requirements.txt, vdm_model.py (docstring and grep), training/train.py (variants, args), losses.py (docstring and answer_sft_loss), data/interventions.py docstring, data/gqa.py and build_gqa.py/build_other.py docstrings, eval/external_openjev.py header, examples/quickstart.py args, HF adapter README. Committed scored outputs: data/leak.json, taskood_k8.json, benchmarks.json, report_{gqa,textvqa,snli_ve,partial}.json, deploy_gqa.json. Code grep for provider clients (openai/typesafe/gemini/httpx/api_key) found nothing. Not read: training/dataset.py, eval/predict.py internals, bench/sweep.py, reports/make_tables.py. No execution, no weights.

**Modalities.** Image (one per request) plus optional shared text context. Many questions share one image. No video, no audio.

**Backbone.** Qwen3-VL-4B-Instruct (8B for the scale check). LoRA r16, alpha 32, dropout 0.05 on the language tower's q/k/v/o/gate/up/down; vision excluded (`.*visual.*`); 33,030,144 trainable. 3,000 steps, batch 8, lr 1e-4, 100 warmup, grad checkpointing, attn sdpa, bf16. Three seeds.

**Head or readout.** Released system a2: no new head. Full-vocabulary next-token CE on the one-hot answer letter at the ':' of 'Answer:'. At inference, candidate-token logits from the backbone's own LM head are normalized over that question's valid choices. Controls (not released): typed choice_head (K_MAX=16 slots), claim_head (3-way), answer_head (an evidence-sufficiency logit), trained as b2/b4/b5/m/mx/mla. Four execution paths are claimed logit-equivalent (independent, vision_cache, prefix_share, prefix_share_batch); the docstring cites bench/parity.py, which is not in the tree.

**Input coverage.** Measured from code. One image per request at max_pixels 200,704 (≈448², 196 visual tokens), both in train.py and the quickstart default. TextVQA-style small text is read at that budget. N questions reuse one image and prefix encoding (KV fork); suffixes are isolated so one answer is never context for another. Choice K is 2-16 at inference (quickstart enforces it). Training K ∈ {2,3,4,5,6,8}, varied deliberately because a fixed K left slot-head slots without gradient. Choice mode has no built-in abstention: the user must supply an option such as 'incorrect_question' or 'not enough evidence', and that probability is relative to the supplied set. The released a2 was not trained on evidence-degraded images (use_masked=False).

**Training data and labels.** GQA balanced train: answers come from Visual Genome scene graphs through GQA's question programs. Native yes/no and two-way items are kept. Open 'query' answers become Choice with frequency-weighted same-type distractors and a compatibility filter so mutually compatible answers never compete. SNLI-VE train: SNLI human labels over Flickr30k; neutral -> not_determined but still answerable=1. Splits are isolated by parent image. The head variants add paired evidence interventions: the same degradation, of the same area, on the question-relevant scene-graph box vs a verified-irrelevant region, to separate question-conditioned sufficiency from a blur detector. Those pairs are not used by a2. No new human annotation; no images redistributed.

**Jev-output provenance.** no-provider-outputs. Labels are dataset answers (GQA scene-graph programs, SNLI-VE human labels). No provider API client anywhere in code/. external_openjev.py scores an external open OpenJev visual-NLI checkpoint on SNLI-VE as a related-work data point, not as labels.

**Calibration.** Gap: the released a2 adapter has accuracy in benchmarks.json but no committed NLL, ECE or temperature. The report_\*.json variants are B1, b2, b4, b5, m, mx and mla, with no a2. Head variants, measured from the files on the GQA val test: raw ECE .053-.062, NLL .28-.31; temperature T 1.67-1.96 fitted on 2,368 calibration items brings ECE to .015-.030. Untrained B1: raw ECE .091, NLL .574, T 2.82 -> ECE .013. SNLI-VE B1: raw ECE .32 and NLL 2.59, needing T 6.47. Raw fine-tuned readouts are overconfident. Answerability AUROC on evidence-degraded GQA: B1 0.426, b2 0.50-0.60, b4 0.324, b5/m/mx/mla 0.966-0.972. A dedicated sufficiency output detects removed evidence; softmax confidence does not.

**Eval evidence.** Reported and committed. Four-benchmark macro accuracy: B1 0.706 -> a2 0.758 (s0), README 0.761; matched typed head also 0.761 with no consistent advantage over three seeds; 8B 0.780. Per benchmark (card, mean ± seed spread): GQA-Choice 0.879 -> 0.916 ± .002 (n=5,447, 1,060 images); SNLI-VE 0.629 -> 0.808 ± .006 (n=1,368); TextVQA-Choice (unseen) 0.974 -> 0.975 ± .002 (n=1,742); TallyQA-Choice (unseen) 0.340 -> 0.345 ± .014 (n=338). leak.json changes how to read 'held-out barely moves'. TextVQA is saturated: the K=4 build was 'leaky' (0.997 sighted), and at K=8 it is blind 0.369 vs sighted 0.974. TallyQA is near floor for everyone (sighted 0.357 vs chance 0.167). GQA blind 0.585 vs sighted 0.841. The unseen sets cannot show transfer either way. Throughput (RTX 5090, bf16, warm): 32 questions sharing an image take 182 ms, 5.7 ms amortized per question, vs 50.7 serial and 19.3 batched without prefix reuse. At N=1, prefix sharing is slower: 82.9 vs 48.1 ms. Peak memory 8.40 -> 10.10 GiB. The sufficiency objective costs 0.013 macro accuracy.

**Compute and ROCm feasibility.** Reported: 4B about 40 min and 8B about 65 min per run on one RTX 5090 (32 GB); GQA prediction about 8 min per system. requirements: torch 2.14 cu130, transformers 5.17, peft 0.21. No flash-attn, no bitsandbytes; attn defaults to sdpa. Quickstart supports cuda and mps. ROCm (Hypothesis): plain transformers+peft+sdpa in bf16 should run on ROCm-torch (the 'cuda' device string and torch.cuda.max_memory_allocated both work under ROCm), but it is unverified on gfx1151. The prefix-share path relies on DynamicCache forking plus Qwen3-VL get_rope_index and DeepStack handling, and its parity script is absent. Measure path agreement (the card says bf16 deviations collapse in fp32) before trusting shared-path numbers. tabputer-1: training fits; expect several times the 5090 wall-clock. Mac M4 24 GB: inference is supported (lower --max-pixels if tight); 4B LoRA training is plausible but slow (Hypothesis).

**License.** Code and adapter: Apache-2.0; backbone Apache-2.0. Datasets are fetched by the user under upstream terms. SNLI-VE sits on Flickr30k images (research-use terms), so flag it for any commercial recipe. GQA images come from Visual Genome, and TextVQA/TallyQA carry their own terms (not audited this pass).

**Borrow for Augustus.** (1) The blind-vs-sighted leak audit per benchmark (chance, blind, sighted, visual gain) is a required multimodal eval gate: it exposed a leaky TextVQA build and a saturated 'held-out' set. (2) Paired relevant vs irrelevant equal-area evidence degradation is the right fixture for 'fails on unseen evidence'. It separates question-conditioned sufficiency from a blur detector, with a kill criterion. (3) A separate sufficiency output (AUROC 0.97) against softmax confidence (≈0.5). If the skill needs 'not enough evidence', train or ask for it explicitly; don't infer it from p_max. (4) Counterexample to 'you need a new head': the LM-head readout matches a typed head at matched budget, so default to the LM head, not a mandatory head. (5) Shared-prefix batching is throughput, not single-request latency; serving policy must state N. (6) Vary K in training; cluster the bootstrap on the parent image. (7) Fit and report a temperature on a held-out calibration split: raw fine-tuned readouts are overconfident (T≈1.8).

**Provenance evidence.** gh api commits (be3cec71, d1d49e7f, b606ac90, 41d2bf75) and tree SHAs (README efc423019140, REPRODUCE e98ff854cf12, vdm_model.py 2c2d0cf67713, train.py 87ed3ca26c52, losses.py 1c8869313127). HF /api/models/guanxuyu/visual-jev-4b-answer-sft full=true and its README.

**Risks.** No calibration numbers for the released adapter. The unseen-benchmark evidence is uninformative (one saturated set, one at the floor). The parity script is missing. Everything was measured on one machine and one backbone family. The paper was not inspected. The quickstart's 0.966 'incorrect_question' demo is one example relative to the supplied choices, not a calibrated evidence measure.


### 6.5 github:andrueandersoncs/visual-jev (table #5)

**Revision.** GitHub HEAD 868d0c2f83074bd7c6d35a7326e6a05dbca78cf9 (2026-09-20T03:14:51Z, 'Add competitive evaluation and harden workbench'). Five commits, 2026-09-18 to 2026-09-20; repo created 2026-09-19T19:38Z. Blobs: README 27eabc7b9fde, docs/OPERATIONS.md 65222798baeb, public_dataset.py 4944cfefd135, training.py 00366a5bf607, decision_model.py e2167d8fc2fa. Backbone pin Qwen3-VL-2B-Instruct 89644892e4d85e24eaac8bacfd4f463576704203.

**Inspected.** 2026-09-23, read-only at commit 868d0c2f8. Files read: README.md, docs/OPERATIONS.md, pyproject.toml. src/visual_jev: public_dataset.py (full); training.py (runtime, loss, optimizer, limits); calibration.py (fit_temperatures); decision_model.py (packing, branch mask, PointerDecisionHead, preprocess_images); image_io.py (limits); lora.py; engine.py (loader). GOAL.md and AGENTS.md were grepped for results only. Also checked: the HF cards of all five corpus sources at their pinned revisions, the LNQA construction post, and one DrBimmer annotation JSON (metadata only). Not read: competitive.py, promotion.py, probes.py and qualification.py bodies, tests, web/. No execution, no weight or dataset download.

**Modalities.** Images only: 1-8 per request, JPEG/PNG/WebP. Optional structured JSON context. Question types choice, score, noul. Documents and screens appear only as page images (DocVQA scans, RICO captures). No video, no audio.

**Backbone.** Qwen/Qwen3-VL-2B-Instruct, pinned to 89644892e4d85e24eaac8bacfd4f463576704203 for weights and tokenizer; branch names are rejected. The vision encoder is frozen by default. An optional experiment trains named vision modules via --train-vision-module.

**Head or readout.** Shared visual/context state, then one isolated branch per question. The custom mask lets a branch see the state and itself only. Structural tokens reuse &lt;|fim_\*|> and &lt;|box_\*|>. PointerDecisionHead: a linear query on the decide-token state is dot-multiplied with a linear key on each option-end token state, scaled by 1/sqrt(256). Adapter: a custom LoRALinear (not PEFT) on the language backbone, r=8, alpha=16, dropout 0.05. Loss: per-branch cross-entropy, plus a ranked-probability-score term for score questions. One run first trains the head only for 3 epochs, then restores the identical initialization and trains head plus LoRA. Documented hyperparameters: 8 epochs, lr 1e-4, weight decay 0.01, accumulation 8, seed 17. The candidate-token Qwen path is kept as an explicit, uncalibrated baseline.

**Input coverage.** Corpus build: every image is thumbnailed to at most 1024x1024 (LANCZOS) and saved as JPEG q92. Optional synthetic transforms: scale down to 0.25x; crop margins up to 30%; brightness down to 0.25x; Gaussian blur radius 0.8-5.6; JPEG quality down to 14; occlusion as a black bar always on the RIGHT side, covering 25-73% of the width. Runtime: the Qwen3-VL image_processor runs with processor defaults (no min_pixels/max_pixels override in the code read). Request limits: 12 MB and 20 MP per image, 24 MB and 30 MP total. Checkpoint limits: max_visual_tokens 8192, max_context_tokens 16384, max_branches 24, max_options 50. Coverage gap: training never sees more than 1024 px on the long side, so small text on full-resolution documents or screens is outside training coverage. Because occlusion is always a right-side dark bar, 'cannot assess' can be learned as 'dark bar on the right'.

**Training data and labels.** The pinned corpus comes from public_dataset.py. It fetches the first rows (offset 0) from the HF datasets-server. There is no shuffle: seed 17 builds an rng the builder never uses. Sources: LNQA 31 rows (vikhyatk/lnqa@8fd7d959); DocVQA 29 of 100 validation rows (lmms-lab-encoder/DocVQA@539088ef); RICO 21 (Voxel51/rico@a675f84f); DrBimmer car images 21 (@2dbf46f7); RealWorld-ChartQA 26 (maevehutch/realworld-chartqa@31cbed95). Split by row order, per source: 12 train, 2 dev, 5 calibration, remainder test. That gives test sizes LNQA 12, DocVQA 10, RICO 2, cars 2. Charts: 8/2/4/2 plus 10 transfer. About 56 base training samples in total, plus derived records.

Labels by source:
- LNQA: answer = qa[0]. These QA pairs were generated by Mixtral-8x7B from Localized Narratives speech transcripts (verified in the LNQA build post).
- DocVQA: dataset answers[0].
- ChartQA: dataset correct_answer_idx.
- RICO: 'portrait phone interface' if height > width, else landscape. The label is image geometry, not UI meaning.
- Cars: titles[0], the alphabetically first of about 20 annotated part polygons. The other visible parts become distractors, so true positives are labelled wrong. The folder 'Car damages dataset/File1' actually holds 998 part-polygon files.
- noul safety_review / safety: source == 'damage'. The label is source identity.
- Quality score: the index of the applied transform. Transform kind and level co-vary (the level picks the kind).
- Assessability: always cannot_assess after right-side occlusion.

Distractors for LNQA and DocVQA are other rows' answers to different questions, a question/answer mismatch shortcut. There are no hard negatives.

**Jev-output provenance.** No Jev Output in training, and no hosted-provider labels, in the code read. There are no TypeSafe, OpenRouter, OpenAI, Anthropic or Gemini calls. OpenJev (the digest-pinned razorback16/openjev container, DiffusionGemma) is called only by competitive.py, at evaluation, on test and transfer requests. One source is generated by an open-weight model: LNQA QA pairs come from Mixtral-8x7B (Apache-2.0 weights) via DSPy, over human spoken narrations. All other labels are dataset gold or program rules.

**Calibration.** Fitting method: one scalar temperature across all primitives. Golden-section search minimizes NLL over log T in [ln 0.05, ln 20], on the calibration split only. Test and transfer are scored afterward. No fitted T or before/after numbers are published. The response field 'confidence' is 1 minus normalized entropy. It measures how concentrated the distribution is. It is documented as not a policy threshold.

**Eval evidence.** None published. The repo contains no checkpoint, evaluation.json, baselines.json or competitive.json. HF has no weights under this author. The README names checkpoint visual-jev-public-mps-bf16-2026-03-v3, which is not distributed. GOAL.md is a design essay ('my first baseline would be...'). The item text's 'trained on Apple MPS in bf16' rests only on the documented --device mps command and that checkpoint name. The designed gate is strict:
- beat both the head-only and candidate-token baselines on untouched test AND distant-transfer data;
- improve calibration NLL or Brier without material accuracy loss;
- packed, shared-cache and independent execution agree within tolerance;
- a sibling-interference suite (reordered, duplicated, irrelevant, leading, contradictory and prompt-injection siblings);
- a digest-pinned OpenJev direction gate.
With test splits of 2-12 items per source, any outcome would carry very wide intervals.

**Compute and ROCm feasibility.** Compute is trivial: a 2B backbone, about 150 records, one record per step with accumulation 8. The stack is plain torch, transformers>=4.57 and sdpa attention, with a custom LoRA. No peft, flash-attn or bitsandbytes.
- M4 24 GB: bf16 MPS training fits in principle; no run is evidenced.
- tabputer-1: --device auto picks mps, then cuda, and a ROCm torch build reports cuda. The files read use no CUDA-only kernels, so gfx1151 is plausible (untested).
- Blocker on both machines: promotion requires the OpenJev comparison, which needs an NVIDIA host (docker --gpus all, nvfp4). Without one the tool writes competitive-unavailable.json (insufficient_evidence), and visual-jev-promote rejects it by design. No checkpoint can be promoted and served on Mac or AMD hardware without changing the gate.

**License.** No LICENSE file. GitHub license is null and pyproject has no license field, so the code is all rights reserved by default. Do not copy code. Data licenses come from a hard-coded table: LNQA CC-BY-4.0; DocVQA Apache-2.0 (per the lmms-lab mirror card); RICO CC-BY-SA-4.0 (hard-coded, although Voxel51/rico HF metadata declares no license); ChartQA CC-BY-4.0; DrBimmer MIT. Upstream DocVQA and RICO terms are not verified.

**Borrow for Augustus.** Borrow the contract, not the corpus or code.
(a) An immutable dataset manifest: per-image SHA-256, source-image and source-group IDs, license and provenance strings, rejection of cross-split image/group reuse, a locked test split plus a distant transfer split, required target-position coverage, explicit cannot-assess targets, and transformation metadata.
(b) Fail-closed serving: never substitute a baseline or random weights for a missing or mismatched checkpoint.
(c) Promotion requires beating both a frozen-backbone head-only baseline and a candidate-token baseline on untouched test AND transfer data.
(d) A sibling-interference probe suite.
(e) An 'unavailable' evidence record that blocks promotion instead of mocking a comparator. Keep it, but let the acceptance policy name a comparator that runs on AMD or Mac hosts.
New label-audit rule for the trainer: reject labels derived from image geometry, source identity or transform index unless the question asks exactly that. When an image has several true positives, drop the single-label choice or make it multi-label. Randomize occlusion position.
Falsifier for (c): if checkpoints that pass the gate do no better than the head-only baseline on a fresh held-out set, the gate is not selecting.

**Provenance evidence.** LNQA method: vikhyat.net/posts/2024-08-17-lnqa.html (Mixtral-8x7B fact extraction plus QA generation, one 'absurd' question per image, 'only open-source datasets and models'); LNQA card cc-by-4.0 at 8fd7d9599cdd. DrBimmer annotation 'Car damages dataset/File1/ann/Car damages 100.png.json' lists 20 part classes (Back-bumper ... Windshield), sorted alphabetically; that folder holds 998 files, the card's car-parts count. Voxel51/rico@a675f84fbb93 cardData license: None. lmms-lab-encoder/DocVQA@539088ef: apache-2.0 per the card.

**Risks.** (1) Several labels can be met without visual decision skill: geometry (RICO), source identity (safety noul), transform index (quality), and one arbitrary pick among true positives (cars). (2) Test splits are tiny (2-12 per source). (3) Training caps resolution at 1024 px. (4) The code is unlicensed. (5) Name collision: hf:guanxuyu/visual-jev-4b-answer-sft (created 2026-09-23T07:29Z, Qwen3-VL-4B PEFT adapter, cites arXiv:2609.25845) is a different project. Matching names are not identity; it is a separate lead, not carded here. (6) DocVQA rows come from the validation split, a common public benchmark split.


### 6.6 github:trycua/cua (table #6)

**Revision.** Release commit d1a01f8580d5963702427b9e110fbcd98c39fac3 (2026-09-22T16:37:53Z, PR #4023). Bench results commit 2d1ab34614ba (2026-09-22T19:20:02Z). Repo HEAD read: 6762bcf63b616c6de86ab7b2309686150913105b (2026-09-24T00:11:45Z). HF revisions: 4b-0.2 16818868b0cc7813808aae4e87b417657046ab79 (created 2026-09-22T03:46Z, modified 2026-09-23T15:48Z); 4b-0.1 88d8b8a90c2da4470d005cc23ec8665a6442ebe1; nano-0.1 1f93fd0fdcbe33740334948f967dff9f6c8e9f34. Prior research card: notes §54 (form-v0 profile only).

**Inspected.** 2026-09-23, read-only. Release commit d1a01f8580d5 (PR #4023, 54 files) metadata. Files read at repo HEAD 6762bcf63b61; the libs/cua-s1 blobs there match the release (README c52de966f026, MODEL_CARD d2c40651cb61).
- libs/cua-s1: README.md, MODEL_CARD.md, python/pyproject.toml, uv.lock (grep).
- libs/cua-s1/training: train_4b_v2.py (docstring, LoRA targets, augmentation, schedule, argument defaults); train_4b_rl.py (docstring, env list, pruning caps, rollout reward, RLOO/Brier/KL loss); train_4b.py and train_nano.py (grep).
- python/src/cua_s1/four_b.py (letter assignment).
- libs/cua-bench-s1: README.md at HEAD, including results added in 2d1ab34614ba; docs/PROVENANCE.md; datagen/gui360.py header and path logic.
Also: HF API for cua-ai/cua-s1-{nano-0.1, 4b-0.1, 4b-0.2}, the 4b-0.2 HF card, the GUI-360 dataset card and the arXiv 2511.04307 abstract.
Not read: nano.py internals, nano_data.py, the androidcontrol.py body, generator/specs, external_bench_import.py, eval_results (not in repo). The crossdataset_hard_v2 composition is not shipped. No execution, no downloads.

**Modalities.** Two surfaces, one adapter each. Text: accessibility-tree or DOM rendering. Multimodal: a single screenshot, with the ax_tree stripped for cross-dataset eval and set-of-mark numbered boxes in RL. The nano multimodal path sees a per-element screenshot crop. Held-out probes: chess (text or rendered board), ViZDoom frames (multimodal only), OSWorld screenshots, and jevbench (text only). No video or audio.

**Backbone.** cua-s1-4b-0.1 and 0.2: frozen Qwen/Qwen3.5-4B (hybrid GatedDeltaNet plus attention, natively multimodal). LoRA r=16, alpha=32, on q/k/v/o/gate/up/down. Multimodal adapters also target the vision merger linear_fc1/linear_fc2, at lr/4. Text and multimodal adapters are trained separately (text/ and multimodal/). cua-s1-nano-0.1: a from-scratch option-attention classifier of about 855k parameters. Text runs through a small byte transformer; multimodal through a frozen SmolVLM-256M or SigLIP-base over the element crop, plus a trainable projection.

**Head or readout.** 4B readout: the prompt asks for one option letter. One forward pass; the final-position logits at the letter tokens A-Z are softmaxed. Hard cap of 26 options per task (assign_letters raises beyond that).

v2 SFT (train_4b_v2.py):
- loss is the mean per-element cross-entropy over each element's own option letters, matching the scorer's per-element argmax;
- single-option elements are dropped as zero-gradient;
- multi-gold elements get uniform target mass;
- seeded per-epoch shuffle, gradient accumulation with clipping, warmup then cosine;
- the best epoch is chosen by validation task accuracy; an obvious test path passed as --val is refused.

RL (train_4b_rl.py):
- on-policy RLOO with K episodes per task instance;
- reward 1 if the environment's terminal reward is >= 0.5, else 0;
- Brier term on episode confidence (geometric mean of the chosen-action probabilities), cal_weight 1.0;
- KL to the SFT policy, held as a second LoRA adapter on the same base via set_adapter;
- lr 1e-5, 2 epochs, 2 task variants per environment; one forward pass per step, no generate().

nano: one parallel pass, per-element argmax.

**Input coverage.** One screenshot per step, with no image history.
- 4B multimodal: Qwen3.5 processor defaults (no pixel budget set in train_4b_v2.py). Training augmentation takes a random crop of 90-100% of the frame, resizes it back, and jitters brightness and contrast by up to 5%. A crop can cut off an edge element while its label is kept.
- RL multimodal: set-of-mark boxes are drawn from the page's own DOM rectangles, not detected. Options name marks by number only. Before the 26-option budget, candidates are pruned to MAX_ELEMENTS=11 by lexical overlap with the instruction. The gold element can be pruned away, and the policy never sees it as an option.
- nano multimodal: sees only the per-element crop, with no page context.
- GUI-360: uses screenshot_clean from success/ trajectories only.
- Chess: all models are scored on the same 15 of 800 positions, because of the 26-option cap.

**Training data and labels.** Trained-on families:
- form_filling, login_auth, consent_checkbox, multi_step_submit, pagination, search_filter: synthetic generator plus AndroidControl plus GUI-360;
- safety_gate: synthetic only;
- cua_bench_basic: live environments.
Held-out only: chess (Stockfish gold), game_control (ViZDoom label buffer), general_decision (fstandhartinger/jevbench), osworld_next_action (xlangai verified trajectories from a claude-sonnet-4-5-20250929 15-step run).

Label provenance:
- Synthetic: generator AppSpecs (program).
- AndroidControl: one recorded gold action per step, snapped to elements by coordinates (not re-verified here).
- GUI-360: actions taken by the dataset's automated LLM agent. The paper describes an 'LLM-augmented, largely automated pipeline ... LLM-driven quality filtering'. The converter reads only success/ trajectories, so gold is what the unnamed agent did on runs that passed the filter.
- Family: assigned by a keyword heuristic, which misfiles mid-episode scroll steps as pagination.
- cua_bench_basic SFT: rows come from the environment's solve() oracle.
- RL: no action labels, only the terminal environment reward.

The composition of 0.2's SFT split crossdataset_hard_v2 is not shipped. Whether it includes GUI-360 training trajectories is not stated.

**Jev-output provenance.** No Jev Output in training, per the docs and code read. Hosted-model-generated gold is present, however. Jev appears only as a hosted-API baseline column and through jevbench (held-out eval data). GUI-360 training gold is LLM-agent output, with the agent and provider unverified. OSWorld held-out gold is Claude Sonnet 4.5 agent actions (eval only). MCA §2.3(b): no Jev Output was found in training. Open question for the coordinator, not ruled here: is querying Jev as a baseline inside a competing open model's benchmark within the 'competing product' clause? Also check the GUI-360 agent provider's output-use terms before adopting GUI-360-trained adapters.

**Calibration.** The SFT recipes read have no post-hoc temperature. RL adds a Brier term on the geometric-mean episode confidence against realized success. That is a proper score only if that confidence family can represent P(success); it is a constrained proxy, and it targets episode success, not per-step option probabilities. Reported raw ECE (theirs): 4b-0.2 text cross-dataset 0.121, multimodal 0.069; djev multimodal 0.360.

**Eval evidence.** All numbers theirs.
- Text, hard cross-dataset (GUI-360, 615 tasks, dataset_hash b38d0f887fad6e719...): 4b-0.2 scores 0.875 overall (ECE 0.121). Per family 0.833-1.000, except pagination at 0.429, which is a labeling artifact.
- Multimodal, hard cross-dataset (168 tasks, ax_tree stripped): 0.929 overall (ECE 0.069). Per-family N is 4/12/4/133/1/14, so multi_step_submit (N=133, 0.917) dominates the overall, and the 1.000 cells rest on N=1-14.
- Multimodal on data/v1, the split 0.1 and nano trained on: 0.2 scores 0.000-0.214 on 5 of 6 families, and 0.000 chance-corrected on those 5. The 0.2 multimodal adapter does not transfer back to synthetic screens. The 1.000 scores of 0.1 and nano there are on their own training distribution.
- Agentic: 0.944 text and 0.722 multimodal over N=18 episodes (6 environments x 3 held-out variants, 2-4). RL trained on variants 0-1 of the same 6 widget environments, with a 20-step cap. These are held-out parameterizations, not held-out environments. The README says 7 of 13 environments are reliably rewardable under 'simulated'. It excludes right-click-menu for exposing zero DOM elements, so RL and the results table use 6.
- chess and game_control: no model shows signal after chance correction.
- Hosted jev baseline on text cross-dataset families: 0.000-0.576.
- MODEL_CARD.md is stale against the later bench README. It calls 0.2 unmeasured on safety_gate, general_decision and osworld, but the bench README (2d1ab34614ba) reports values. It gives 4b-0.1 general_decision 0.563, which the table shows for semif (4b-0.1 shows 0.632).

**Compute and ROCm feasibility.** The training scripts hard-code device_map='cuda' and bf16. Stack: PEFT, accelerate, torchvision. The files grepped contain no flash-attn, bitsandbytes or deepspeed. A ROCm torch build reports cuda, so gfx1151 is plausible (untested). 4B bf16 weights (about 8-9 GB) plus activations fit in about 115 GB of unified memory. RL holds the KL reference as a second adapter, not a second model copy.

Caveats:
(1) The Qwen3.5 GatedDeltaNet fast paths (flash-linear-attention, causal-conv1d) are not in the lock, so the torch fallback runs. It is slow on 1-2k-token GUI prompts.
(2) pyproject pins transformers>=4.45,&lt;5, and uv.lock resolves 4.57.6 (torch 2.14.0, peft 0.21.0). qev needed transformers 5.17 for Qwen3.5-0.8B. Verify that 4.57.6 loads Qwen3.5-4B before reproducing (unverified).
(3) RL needs the monorepo's cua_bench live environments (simulated provider).
nano is cheap on CPU or GPU.

**License.** Code: MIT (repo). cua-ai/cua-s1-4b-0.2 adapters: apache-2.0 (HF cardData; sha 16818868b0cc). cua-ai/cua-s1-4b-0.1 (sha 88d8b8a90c2d) and cua-ai/cua-s1-nano-0.1 (sha 1f93fd0fdcbe) declare no license and have no README, so they are unlicensed. MODEL_CARD.md says official checkpoints may carry separate terms that require a commercial license, which conflicts with the 0.2 HF card. Data: AndroidControl Apache-2.0; GUI-360 MIT; python-chess and Stockfish GPL-3.0 (held-out only, optional extra); OSWorld trajectories under 'dataset terms'.

**Borrow for Augustus.** (a) A per-element scoped softmax loss that matches the scorer, dropping single-option elements. This is a concrete fix for a loss that does not match the metric in multi-element typed decisions.
(b) The RL stage: RLOO, plus a proper-score calibration term, plus KL to the SFT policy held as a second adapter on one base. It is memory-cheap on one unified-memory box, and it targets 'when to stop', which SFT labels cannot teach.
(c) Publish a chance-corrected table with measured p_chance and N per row.
(d) The acceptance policy should count 'held-out variants of trained environments' as in-distribution.
(e) Record label-generator identity for agent-trajectory data (GUI-360 = LLM agent, success-filtered). Add a 'model-generated, provider X' provenance class next to Jev.
(f) Surface-specific adapters (text vs screenshot) on one frozen base.
Falsifier for (b): if per-step ECE of an RLOO+Brier adapter on held-out environments (not variants) is no better than SFT-only, the calibration term adds nothing beyond the policy gradient.

**Provenance evidence.** gui360.py header: source vyokky/GUI-360 (card sha 1c46362efaae, MIT). It says the data covers 'both successful and failed human/agent-collected trajectories', and the path logic reads in_app/success only. GUI-360 card, Stage 2: 'A specialized agent automatically executes the tasks'. arXiv 2511.04307 abstract: 'LLM-augmented, largely automated pipeline ... LLM-driven quality filtering'. PROVENANCE.md source table. The cua-bench-s1 README states which held-out and trained-on sources feed which families, and that Jev is a 'hosted external API baseline'.

**Risks.** - Environment fragility: toggle widgets lose the reward after an even number of toggles, and 'done' is learned only in RL.
- The caller builds the option set, and pruning can drop the gold element.
- The keyword family taxonomy mislabels steps.
- MODEL_CARD.md is stale against the bench README.
- Multimodal N is small; the 0.2 multimodal adapter regresses on synthetic screens.
- The 0.1 and nano weights are unlicensed.
- Possible transformers-version mismatch for Qwen3.5.
- GUI-360 gold was produced by an LLM agent with success-selection bias.


### 6.7 github:sseanliu/Jev-Vision (table #7)

**Revision.** GitHub HEAD 14ceabceaf08af74d2dab05c9893a890e3b4cca8 (2026-09-21T22:08:47Z). 23 commits since fingerprint dbd230b57fae. README blob e946c8a4e463. HF SeanLiu/Jev-Vision sha dc2d645b9d019e66b8f63def5c8a8be842448f4c (created 2026-09-21T11:25Z, modified 2026-09-21T14:43Z); the prior research recorded sha 9b77fa5fdcd0, so the Hub revision moved. Key commits: 5a554599ed5f (label source), 1c221ee8737f (AUROC correction), bde79c2c9f74 (V9 release), 0348b5f0f745 (noul temperature). Prior card: notes §124, which covered V5b only and did not record jsonl_jev.

**Inspected.** 2026-09-23, read-only at HEAD 14ceabceaf08. Read:
- messages of all 23 commits in the compare dbd230b57fae...main, and the file lists of commits 5a554599ed5f and 1c221ee8737f;
- README.md (blob e946c8a4e463);
- model/runpod run_v1, v1b, v2-v9 (headers, INIT, data and train lines), plus run2.sh and run_flagship.sh (grep);
- model/train_vl.py (arguments, losses), model/s1/vl.py (grep);
- harness/record_triplets.py (docstring, policy mix, label rules);
- probes/vision: build_operation_rows.py (docstring), build_general_rows.py header, teacher_jev.py header;
- bench/build_general_items.py header, probes/distill_jev.py header, the first row of model/data/jsonl_jev/trec.train.jsonl;
- the HF card and API for SeanLiu/Jev-Vision.
Not read: the s1/packing.py, mask.py, serve.py and eval_schema.py bodies; the build_schema_rows.py and build_state_rows_\* bodies; the OS-Atlas and Mind2Web builder details; results JSON. No execution, no downloads.

**Modalities.** Screenshots: desktop web at 1280x1000, and macOS desktop via OS-Atlas. Two-screenshot questions (effect: before/after). General images from public VQA-style sets, including NLVR2 image pairs. Text state: goal, history and a candidate table. Text-only requests fall back to a text forward. No video, no audio.

**Backbone.** Qwen/Qwen3-VL-8B-Instruct with a PEFT LoRA, r=64, on q/k/v/o/gate/up/down (175M trainable), plus separate typed heads (heads.pt). Default attention is sdpa.

**Head or readout.** The request is packed as a shared state prefix (screenshot tokens, goal, history, candidate text), then one isolated branch per question under a tree mask, so all of a step's questions run in one forward pass. Readouts: choice uses a pointer over option tokens; noul uses a sigmoid (BCE, with --noul-smooth label smoothing, 0.05 in V8 and 0.02 in V9); score uses a softmax over ordered levels. Soft targets use soft cross-entropy. Training is staged, each run continuing from the previous adapter and heads: V1/V1b (Mind2Web ground, Qwen3-VL-32B soft targets) -> V2 (schema flexibility) -> V3 (OS-Atlas desktop) -> V5b (skip/effect/done state rows) -> V7 (general-vision mix) -> V9 (corrected operation rows; lr 1.5e-5, head lr 1.5e-4, 1 epoch, batch 2 x accumulation 8, gradient checkpointing).

**Input coverage.** train_vl.py default --max-pixels 1,288,000 (about 1288x1000). V4 trained multi-resolution budgets {1288k, 640k, 320k}, but the V5-V9 lineage starts from V3, so V9 did not inherit multi-resolution training (inferred from the INIT lines). General-vision images are resized to at most 1024 px on the long side (JPEG q88). One or two images per question. The model card says it was trained and evaluated on 1280x1000 desktop web screenshots, not on mobile, logged-in or form-heavy flows. Recorder labels are coarse: 'effect' is url_changed OR dom_changed OR value_applied OR pixel diff > 0.02, where the diff is the fraction of 256x160 greyscale pixels changing by 16 or more levels. A noisy flag marks pages that change between two after-shots.

**Training data and labels.** V9 lineage, from the run scripts:
- Mind2Web: human-annotated gold, as hard rows.
- Qwen3-VL-32B-Instruct: logprob soft targets at T=4 on Mind2Web ground items, plus an uncertain subset (top-p &lt; 0.8), used in V1/V1b and replayed in V2. This is open-weight-model distillation.
- Mind2Web-derived schema rows.
- OS-Atlas macOS desktop grounding rows.
- Recorder triplets rec1, rec1b, rec2train and pixel variants, plus synthetic pages (synth1): Playwright on public sites. No model is in the loop; goals are generated from the page. The policy mix is oracle 0.5, random 0.25, repeat 0.15, unrelated 0.10. skip, effect and done come from the environment (URL, DOM, field values, pixel diff).
- General rows from TRAIN splits: A-OKVQA (4-way), Food-101 (20-way), VQAv2 yes/no, GQA yes/no, NLVR2. Public gold.
- jev-ultrafast-format operation / \*_target rows (rules text imported from a local jev-ultrafast checkout).

Label-source bug and fix (5a554599ed5f): operation gold used to be the recorded policy's action. 57% of recorded steps are deliberately wrong actions, so the old targets were wrong about half the time. Gold now comes from the task: DONE when done_before/after holds, otherwise the oracle operation and the goal's target element. V9 = V7 plus the corrected rows (3,113 training rows per the README).

**Jev-output provenance.** The released V9 vision lineage (V1 -> V1b -> V2 -> V3 -> V5b -> V7 -> V9) uses no Jev Output in any run_v\*.sh read. Its teacher is open-weight: Qwen3-VL-32B soft targets. The same repository also contains Jev-distilled text data, first recorded here. probes/distill_jev.py queried Jev and wrote Jev's distributions as training 'targets' into model/data/jsonl_jev/, jsonl_jev_hard/, jsonl_nli_adv_jev/ and jsonl_synth_jev/, all committed publicly. run2.sh stage 2b and run_flagship.sh's default SOFT_DIRS train the text s1-1.7b lineage on them. That text lineage is MCA §2.3(b) material: do not borrow anything downstream of jsonl_jev or distill_jev. Jev, Claude and DJev also appear as eval-time judge baselines (teacher_jev.py, teacher_claude.py; bench/baselines/\*.jsonl), and Jev as a closed-loop decider in hang_behind.py demos. The V9 weights look clean per the run scripts, but that rests on the scripts, not on an audited training manifest.

**Calibration.** Evals and serving use a fixed temperature --temp 0.5, chosen from a sweep over {0.5, 0.75, 1}, not fitted on a calibration split. The README's ECE figures are at that fixed temperature. After release they added a fitted noul temperature (fit_noul_temperature.py, T=1.3 on GQA val, out-of-domain). It moved JevBench-hard ECE only from 0.28 to 0.24, with mixed effect on the general track. The 1c221ee8737f correction: selective (confidence-vs-correctness) AUROC had been compared against class AUROC. eval_schema now reports auroc (class) and sel_auroc (selective) separately.

**Eval evidence.** All numbers theirs, single runs.
- General track (1,500 items): V9 mean 0.917 vs frozen Qwen3-VL-8B prompt+logit 0.911. The 95% bootstrap intervals overlap, so accuracy is a tie. Also, A-OKVQA, Food-101 and NLVR2 are trained-on task families for V7/V9 (their train splits) but zero-shot for the frozen baseline; only POPE and MME are eval-only. Frozen Qwen3.5-9B scores 0.903 (AUROC 0.96-0.97, ECE 0.02-0.05). V9's yes/no class AUROC is 0.97/0.97/0.98 vs frozen 0.95/0.97/0.96. V9 states 13% of its errors at p>=0.99, vs 37% for the frozen readout.
- Screens v1 (fresh episodes on 30 held-out sites, site-level split), candidate track: skip 0.922, effect 0.977, done 0.887, vs Jev 1.13 text-only at 0.870/0.733/0.887 and a URL/DOM rules baseline at 0.865/0.892/0.758. Pixel track: 0.931/0.931/0.891.
- Operation question, 615 held-out rows with task-derived gold: 0.911; click_target 0.969.
- JevBench public items, text-only zero-shot: hard tier 0.523 at 0.91 mean confidence (Jev 0.730).
- Grounding regressed against earlier checkpoints: web 0.823 vs 0.850, desktop 0.822 vs 0.914.
- Closed loop: one Google Flights task completed (10 actions, 7/7 page checks). That is an anecdote, not a rate.

**Compute and ROCm feasibility.** Trained on RunPod H100 80 GB, bf16, sdpa. Batch 4 without checkpointing OOMed on 80 GB, so they used batch 2 x accumulation 8 with gradient checkpointing. Serving targets 'any CUDA box with 24 GB'; latency is H100, batch 1. The files read show no flash-attn or bitsandbytes. train_vl.py selects cuda if available, which a ROCm build reports. On tabputer-1, the 8B bf16 model plus a r=64 LoRA with checkpointing should fit in about 115 GB of unified memory, but it will be far slower than H100 (untested). The scripts assume a RunPod /workspace layout and sed-rewrite the author's Mac paths. The recorder needs Playwright on live public sites. The M4 24 GB is too small to train 8B; inference might fit only after quantization, which is not provided.

**License.** Code: Apache-2.0 (LICENSE file, 'Copyright 2026 Xiaoan Liu'). The GitHub API shows NOASSERTION, a header-detection mismatch. HF weights SeanLiu/Jev-Vision: apache-2.0. Third-party data keeps its own terms (Mind2Web, OS-Atlas, the Hume evidence files). The committed jsonl_jev\* files are Jev Output redistributed in a public repo; their Apache-2.0 label does not override TypeSafe terms.

**Borrow for Augustus.** (a) The label-source rule, the key design lesson: take gold from the task or environment oracle, never from a behaviour policy that deliberately explores. Use exploratory actions only to create negatives for state questions such as effect and skip. Add a trainer check that fails when targets are derived from logged actions of a mixed policy.
(b) Report class AUROC and selective AUROC under different names. A metric-definition mismatch produced a false claim here.
(c) The 'high-confidence error rate' (share of errors stated at p>=0.99) as a Noul release metric beside ECE.
(d) Environment-labelled step-verifier questions (skip, effect, done) with a site-level held-out split.
(e) A provenance lesson: audit the whole repo and lineage, not the release notes. One repo can host a clean vision lineage and a Jev-distilled text lineage side by side.
Falsifier for (a): if operation accuracy under policy-derived labels matches task-derived labels on a task-gold held-out set, the fix did not matter. Here it moved from wrong about half the time to 0.911 (theirs).

**Provenance evidence.** Evidence file by file:
- run_v1.sh: 'Qwen3-VL-32B logprob teacher -> soft targets (T=4)' via probes/vision/teacher_qwen_vl.py.
- run_v2.sh: 'stage-2 from V1b on schema rows + V1b's soft ground rows (replay)'.
- run_v9.sh: INIT v7-8b-general. run_v7.sh: INIT v5b-8b-state. run_v5.sh: INIT v3-8b-desktop. run_v3.sh: INIT v2-8b-schema.
- record_triplets.py docstring: 'No model in the loop'; --mix default '0.5,0.25,0.15,0.10'.
- distill_jev.py docstring: 'Collect Jev's probability distributions on our training requests as soft labels (data condition (b): Jev-distilled)'.
- run2.sh: '2b: Jev soft labels (data/jsonl_jev)'.
- teacher_jev.py: 'TypeSafe Jev on the V0b ground items', reading TYPESAFE_API_KEY.

**Risks.** - The README's line 'labels ... from the environment rather than from a model or a human' is true only for the state tracks. Grounding stages used Qwen3-VL-32B soft labels and human Mind2Web gold.
- The repo co-hosts Jev-distilled data.
- The fixed temperature 0.5 is not fitted, and the OOD long-text confidence is badly overconfident.
- The general-track comparison is partly in-distribution for the fine-tunes.
- Grounding regressed from V3-era checkpoints.
- Effect labels are pixel-diff heuristics.
- Desktop web at 1280x1000 only.


### 6.8 github:loadchange/qev (table #8)

**Revision.** GitHub HEAD caa94df5ecb2fb387d1eb31aba21013615bb8114 (2026-09-21T11:51:26Z); repo created 2026-09-21T00:57:52Z; 5 commits. README blob c7657f6a9d75, MODEL_CARD.md blob aa79b1b4ed81, TRAINING.md blob abb1bd8f2eb5. HF: twainsk/qev-0.8b abfbc728cfdacde39c57c7f65ada36165686b321 and twainsk/qev-0.8b-mlx 0dcf82a746794e813357d19c8d94812b1e686169 (both created 2026-09-21T01:06Z; both v0.3 Snake). Data: kev-suites a3318ddc1f63, public-pool-v4 manifest partition hashes as recorded in docs/results/data_manifest.json. Foundation: Qwen3.5-0.8B 2fc06364715b967f1860aea9cf38778875588b17.

**Inspected.** 2026-09-23, read-only at HEAD caa94df5ecb2. Read: README.md (blob c7657f6a9d75); docs/MODEL_CARD.md (grep); docs/SNAKE_MODEL.md (grep); docs/ARCHITECTURE.md (grep); pyproject.toml; uv.lock (grep); qev/api.py (media budgets); qev/model.py (LoRA targets, attention); qev/train.py (grep). Result files: data_manifest.json, provenance.json, data_audit.json. Also the manifest of kev-suites public-pool-v4 at a3318ddc and the HF API for twainsk/qev-0.8b and twainsk/qev-0.8b-mlx. Not read: data.py and inference.py bodies, mlx_runtime.py, the evaluation.json rows, the Snake data scripts. No execution, no downloads.

**Modalities.** Decision training and evaluation are text-only. The API accepts images in the state, images inside options, and video as inline sampled frames, but those paths are untrained for decisions. Multimodal decisions use T=1, not the text temperature. Audio is rejected. Native Qwen3.5 generation (text, image, video) is preserved with the adapter switched off.

**Backbone.** Qwen/Qwen3.5-0.8B, pinned to 2fc06364715b967f1860aea9cf38778875588b17 and fully frozen. The 24 language layers mix GatedDeltaNet and full attention (hidden size 1024). Frozen-parameter SHA-256 is checked before and after training (852,985,920 parameters).

**Head or readout.** A switchable rank-16 LoRA decision adapter on language attention, the GatedDeltaNet projections (in_proj_qkv, in_proj_z, in_proj_b, in_proj_a, out_proj) and the MLP, plus a 256-d pointer head. 11,346,944 trainable parameters. Logits come from hidden states at candidate-end and decision positions, trained with supervised cross-entropy. Each question is encoded as its own sequence, because GatedDeltaNet recurrent state cannot be isolated by attention masks. There is no shared-state branch packing, and cost grows with the number of questions. Training: 2 epochs, batch 4, accumulation 4, lr 5e-5, seed 42, max_length 1024, max_state 384; FP32 master weights, BF16 autocast, FP32 pointer.

**Input coverage.** Training states are capped at 384 text tokens, sequences at 1024; the audit found no truncation. API media budget per request: at most 8 images plus video frames in total; per image at most 2 MB and 4 MP; total at most 8 MB and 8 MP. Video is 1-8 client-sampled inline frames with a client-declared fps (0 &lt; fps &lt;= 60); the server does no sampling and fetches no URLs. Animated images must be sent as explicit frames. Image processing uses the official Qwen3.5 image and video processor settings, unchanged. No media reached decision training, so every image, video or option-image decision is outside training coverage.

**Training data and labels.** v0.2 general model: jaredpalmer/kev-suites public-pool-v4 at a3318ddc1f630c5673232efacd8123a84de3f480, with upstream splits kept and the locked test never read. Ten public sources: banking77, boolq, agnews, mnli, sst5, yelp, trec, dbpedia14, amazon, imdb. Labels are upstream dataset gold, converted by jaredpalmer/kev (Apache-2.0). Plus 250 English and 250 Chinese synthetic rule questions from executable programs in four families: refunds, approvals, deadlines, membership. Split sizes: train 5,892, calibration 620, development 880 questions. The development set influenced source- and label-balanced data selection.

v0.3 Snake models (the ones published on HF): continued training with labels from an explicit heuristic teacher that reads only model-visible features. It prefers avoiding collisions and keeping tail connectivity and space, then food paths and visits. There is no teacher marker in the inputs, and there are 10% random legal deviations. 12,000/500/500 Snake questions, plus replay of all original questions. Observations are text features computed by the engine (BFS reachable space and similar), not board images.

**Jev-output provenance.** No Jev Output and no other provider outputs, as stated and consistent with the manifest. The README says 'Jev was not queried for labels'. MODEL_CARD.md says 'Neither Jev nor another external model supplies labels'. provenance.json says 'objective: supervised cross-entropy over candidate options; no Jev labels or RL'. Upstream kev-suites is public gold (research notes on jaredpalmer/kev: 'Public gold, not a Jev teacher'). The Snake teacher is a program heuristic. The claim is not independently re-derived row by row; only the manifests were read.

**Calibration.** One temperature, T=1.464086, selected by NLL on the 620-question calibration split only. It is reused unchanged for MLX FP32, with no refit. Development (theirs): accuracy 81.36%, NLL 0.5512 -> 0.4890, ECE 0.0695 -> 0.0432 (CUDA BF16); MLX FP32: ECE 0.0395. The text T is not applied to multimodal decisions.

**Eval evidence.** All numbers theirs. They describe the v0.2 general checkpoint, which is not the released v0.3 Snake checkpoint.
- Development set (880 questions, not a locked test): untrained pointer 28.75%; trained 81.36% (CUDA BF16) vs 81.25% (MLX FP32); ECE 0.0432 vs 0.0395; 1 of 880 argmax choices changed across precisions.
- Candidate reversal: 27 of 28 probes kept the same choice; one Banking77 question with 77 candidates flipped, with a probability change of up to 0.585.
- Chinese: dev covers only the four trained rule families, at 100%.
- v0.3 Snake: on 8x8 boards over 20 held-out seeds, food eaten rose from 3.1 to 42.9 and collision endings fell from 20 to 0. Teacher agreement on unseen seeds was 98.40% (vs 73.60% before).
- No multimodal decision accuracy. No comparison with Jev, Kev or others on a shared test set. Service checks passed 17/17 (Torch) and 19/19 (MLX).

**Compute and ROCm feasibility.** Trained on an NVIDIA L4 via Colab; Snake continuation on an A100. Measured on M4 16 GiB: MLX FP32 at 41.82 ms median for a 40-token question. Stack: transformers 5.17 (pinned >=5.17,&lt;5.18), torch 2.11 (cu128), peft 0.21, accelerate. The lock has no flash-attn, bitsandbytes, flash-linear-attention or causal-conv1d, so GatedDeltaNet runs through the transformers torch path, which is ROCm-portable. train.py requires torch.cuda.is_bf16_supported(); a ROCm build reports cuda. So tabputer-1 is plausible for the 0.8B model (untested), and memory is a non-issue. On the M4 24 GB, the MLX FP32 export (3.48 GB) runs. train.py's --device defaults to cuda, then mps, then cpu, and off CUDA it uses a different dtype path (no bf16 autocast). MPS training of the 0.8B model is therefore plausible but unmeasured; all their training evidence is on CUDA. FP16 export exceeded their numerical-audit threshold, so FP32 ships.

**License.** Code: Apache-2.0 (LICENSE and NOTICE). HF twainsk/qev-0.8b and twainsk/qev-0.8b-mlx: apache-2.0. The foundation keeps its own license. Upstream source licenses per the manifest are uneven: trec and sst5 'not_declared', agnews 'unknown', yelp 'other', dbpedia and boolq cc-by-sa-3.0, amazon apache-2.0.

**Borrow for Augustus.** (a) An architecture constraint for any Qwen3.5-family or other recurrent/hybrid backbone: attention masks cannot isolate GatedDeltaNet state, so shared-prefix branch packing is invalid. Encode each question independently, or cache only state that is provably isolated, and budget latency for it. Put this in the recipe decision table next to the packing choice.
(b) LoRA targets for hybrid models must include the linear-attention projections (in_proj_qkv, in_proj_z, in_proj_b, in_proj_a, out_proj).
(c) Evaluate at the precision you ship. FP16 failed their audit, so they ship FP32; reuse the calibration T across runtimes and report the argmax-flip count.
(d) Check frozen-foundation hashes before and after training, and keep a switchable adapter so native multimodal generation is preserved.
(e) Keep a text-trained temperature off media decisions (T=1) until media calibration data exists.
Falsifier for (e): if a text-fitted T improves media ECE on a labelled media calibration set, the separation is unnecessary.

**Provenance evidence.** Evidence files:
- docs/results/data_manifest.json: upstream jaredpalmer/kev-suites public-pool-v4, conversion code jaredpalmer/kev, per-source HF revisions and declared licenses.
- kev-suites public-pool-v4/manifest.json: trainable_sources as listed; eval_only mmlu, emotion, tweet_offensive, qnli, paws, sciq; 'no fuzzy decontamination or pretraining-contamination claim'.
- docs/results/provenance.json: hardware NVIDIA L4, frozen_before sha 1021eaee..., packages.
- docs/SNAKE_MODEL.md: heuristic teacher, 'Runtime neither calls the teacher'.

**Risks.** - The released weights (v0.3) are Snake-specialized. The 81% general numbers belong to v0.2, which is kept locally, not on HF.
- 'Multimodal' is inherited backbone capability, not recipe evidence.
- The development set guided data selection and is not a locked test.
- Per-question encoding scales cost with question count.
- Weak or undeclared upstream text licenses.
- The Chinese evidence covers only the four trained rule families.


### 6.9 github:RikaiDev/mesen (table #9)

**Revision.** 54dab86bfc4c (HEAD, main). Five commits in about 80 minutes on 2026-09-23: f65c5265, then 7aa54031 (data), b79e64f2 (consultant), be0f22bc (daemon), 54dab86b (ViT). pyproject version 0.2.0.

**Inspected.** github:RikaiDev/mesen @ 54dab86bfc4c (2026-09-23T15:17:50Z; created 14:01Z; 0 stars; no CI runs). README blob 7798c8a09b17, pyproject b771acea. Read in full: data/{fetch_websight,mutator,renderer,synthesizer,render_mirror_samples}.py, model/{vlm_jev,heads,consultant_model,vit_consultant,export_onnx}.py, pipeline/{dataset,distill}.py, train/train.py, train_consultant.py, train_vit_consultant.py, export_onnx.py, serve/server.py (judge path), plus the heads of cli.py, templates.py and rules/registry.py. HF metadata: Qwen/Qwen3.5-2B-Base @ b1485b2f, afx-team/UI-UX @ 846401e4, inclusionAI/UI-Venus-2-9B @ 90d6dfe1, HuggingFaceM4/WebSight card @ b11f8172. Also read 100 WebSight v0.2 train rows (offset 0) through datasets-server to test the mutators. No execution, no weights. First card; the only earlier sighting is archive/2026-09-23-patrol github-first-sightings.

**Modalities.** Claimed: screenshots at 4 viewports (375x812, 768x1024, 1024x768, 1440x900) plus witness-state JSON (DOM contract, accessibility, geometry). What each trainer actually takes: train/train.py (the Qwen 'vlm-jev') is text-only, and as committed its input is all zeros. train_consultant.py takes random noise vectors. train_vit_consultant.py takes one screenshot per row. No code fuses the 4 viewports.

**Backbone.** Declared: Qwen/Qwen3.5-2B-Base @ b1485b2f (Apache-2.0; HF arch Qwen3_5ForConditionalGeneration, image-text-to-text). It is loaded with AutoModel(trust_remote_code=True). I did not verify which class resolves (text tower or full VLM), and vision is never called either way. The one path that reads pixels uses torchvision vit_b_16 with ImageNet DEFAULT weights, freezing conv_proj and the first 6 encoder blocks.

**Head or readout.** vlm-jev: the masked-mean-pooled last hidden state feeds 5 ChoiceHead MLPs (3-way yes/no/unknown) and a ScoreHead (4-way). Each head divides by its own learnable, clamped temperature. Consultant: a linear atomic head per dimension, a 13-rule multilabel BCE head (pos_weight 3) and a sigmoid bbox regressor. ViT: concat[CLS, mean of the 8x8 center patches] projected to 1536, then the consultant heads. A NoulHead (sigmoid) is defined but unused.

**Input coverage.** Renderer: headless Chrome `--screenshot --window-size=W,H`. It captures the first viewport only, with no scroll or full-page capture, and scrollbars hidden. WebSight v0.2 HTML loads Tailwind from the jsdelivr CDN, so an offline render is unstyled. ViT path: T.Resize((224,224)) squashes each screenshot (1440x900 becomes 224x224, a 6.4x/4.0x downscale that distorts aspect). There are 14x14 patches, and the center ROI is hardcoded to rows/cols 3..10. Each viewport is its own training row with the page's labels, so no row can see 'consistency across breakpoints'. Qwen path: VlmJevModel.extract_features calls backbone(input_ids, attention_mask) and drops pixel_values. UiEvidenceDataset returns no image tensor. train.py builds the dataset with tokenizer=None, so input_ids are torch.zeros(1024) for every row. The model can only learn label marginals. Serving: /v1/judge feeds np.random.randn(1, hidden) into the ONNX session, so the answers ignore the request's images and state. The one exception is a hardcoded rule that fires when contract.has_center_dialog is set or contract.mutation=='center_intrusion'. ONNX export covers only the heads (input is a latent vector), so the '&lt;500 ms' and '0.1 ms' figures include no encoder.

**Training data and labels.** Labels come from the mutation type, not from looking at the page (mutator.py). There are 6 types: clean, overflow, occlusion, low_contrast, responsive_break and empty_state. Each type fixes the yes/no labels and the score (clean=2, occlusion=0, others=1). The code never emits 'unknown'. evidence_consistency is never 'no', so that head is constant. Score 3 appears only in the hand-set mirror 'clean' rows. Bounding boxes are per-type constants, not measurements. Sources: (a) WebSight v0.2 via datasets-server. fetch_websight.py writes JSONL and keeps the original screenshot URL for clean rows only; it renders nothing. (b) 5 hand-written templates x 6 mutations (synthesizer.py). The var_idx loop re-runs the deterministic mutate_html, so --num-variations makes byte-identical copies of 30 unique samples, and a random 80/20 row split puts copies in both train and val. (c) 3 hand-written mirror pages x 5 identical renders. (d) 450 label-only mirror rows with no media, added in train_consultant.py. Measured label noise on the real corpus: all 100 of WebSight v0.2 rows 0-99 lack `</head>`, so LOW_CONTRAST injects nothing, yet those rows are labeled visual_integrity=no, operator_clarity=no, score 1. 11/100 have neither `</h1>` nor `</h2>`, so OVERFLOW is a no-op there too. None of the 100 use the .btn-primary selectors the contrast CSS targets. Label leakage: the prompt includes `Contract: {"mutation": <type>, "is_clean": ...}`. accessibilityViolations is set only for low_contrast, geometryAnomalies only for responsive_break, and consoleErrors only for empty_state. With a tokenizer attached, the label can be read from the text. The pipeline was never run end to end: fetch_websight writes data/websight_mutations.jsonl, but train_consultant json.load()s data/websight_train.json. The ViT loader reads r['screenshots'], but synthesizer writes 'image_paths', so only mirror_samples.json feeds the ViT: 60 PNGs, 12 distinct. The README's distillation lineage (UI-UX 4B defect teacher, UI-Venus-2-9B grounding teacher, A100 training, calibration penalties) does not exist in code. MultiTaskDistillLoss accepts teacher_logits, but no caller passes any. The documented 'beta \* L_calibration' term is not implemented.

**Jev-output provenance.** no-provider-outputs, confirmed in code. No hosted-provider API is called anywhere, and every label comes from mutation-type rules. The upstream WebSight v0.2 corpus is open-model synthetic (ideas from Mistral-7B-v0.1, code from Deepseek-Coder-33b-Instruct, per its card) and contains no decision labels. The two teachers the README names are open-weight HF models (afx-team/UI-UX, MIT; inclusionAI/UI-Venus-2-9B, no license tag), and neither is wired in. If the teacher path is ever added, record each teacher's id, sha and license. It still would not be Jev Output, so MCA §2.3(b) is not implicated.

**Calibration.** Each head's temperature is a trainable parameter optimized on the training loss, not fitted on held-out data. Focal loss (gamma 2; class weights yes 1.0, no 2.5, unknown 1.2) pushes probabilities away from calibration by design. Nothing computes ECE or Brier. Validation reports only loss or rule F1 at a 0.5 threshold. Treat the outputs as uncalibrated scores.

**Eval evidence.** None published: no logs, metrics files, checkpoints or CI. The only number is in the 54dab86b commit message ('99.8% optical clearance precision'), with no artifact behind it. Given the code, it would be measured on 12 distinct mirror renders duplicated across a random image-level split, which is memorization. The README latency claims (&lt;200 ms GPU, &lt;500 ms ONNX, 0.1 ms) time the heads alone. Every performance claim is unsupported.

**Compute and ROCm feasibility.** Nothing committed is worth training as-is. If it were: a full AdamW bf16 fine-tune of Qwen3.5-2B (weights, grads and moments in the tens of GB) fits in tabputer-1's ~115 GB. Under ROCm, torch.cuda.is_available() is True, so the bf16 branch and torch.cuda.amp (ViT) run through HIP. deepspeed and bitsandbytes are listed in the [train] extras but imported nowhere, so they block nothing; skip the extra. The ViT-B/16 fine-tune and ONNX export are trivial on the iGPU, the CPU or the M4. Screenshot rendering needs Chrome and network access for the Tailwind CDN. Not worth box time until the leakage and the pixel path are fixed.

**License.** MIT is declared in metadata only: the README badge and pyproject (license = {text = 'MIT'}) say MIT, but there is no LICENSE file at 54dab86 and the GitHub API reports license=null. The grant is unverified, so do not copy code until a license text exists; the ideas are reusable. WebSight is CC-BY-4.0, and its card requires disclosure when a model trained on it is released; mesen's README omits it. Qwen3.5-2B-Base is Apache-2.0. UI-Venus-2-9B has no license tag.

**Borrow for Augustus.** Take the label-by-construction idea, not the code. The idea: take clean HTML, inject a deterministic defect, render it, and label the row from the injector. It is a cheap, provider-free label source for UI-quality decisions. The skill should require the gates this repo lacks, each written as a falsifier: (1) Apply-check. Assert the mutated DOM or pixels differ from the clean page (pixel diff > 0, or a measured contrast ratio below threshold) and drop no-op rows. This alone catches the 100% low_contrast no-op. (2) Input ablation. Remove every field that encodes the label (mutation, is_clean, the mutation-specific violation lists) and retrain. If the metric collapses, the model was reading the label. (3) Group split by source page, with all mutations and viewports of one page in one split. Never split by row or image. (4) A blank or shuffled-image control on the trained head (the akasha audit pattern). (5) Prefer measured labels (axe-core contrast, DOM geometry overflow) over labels implied by the mutation type. Also add this repo as the negative example in a 'multimodal claim audit': confirm pixel_values actually reach the encoder, the served path consumes the request's inputs, and latency figures include the encoder. Coverage rule: first-viewport screenshots squashed to 224 px cannot see below-the-fold or sub-patch defects. Record viewport, fold and resolution in the decision contract, and keep 'unknown' reachable with training rows that use it.

**Provenance evidence.** Leak: pipeline/dataset.py builds the text_prompt from state['contract'], and fetch_websight.py and synthesizer.py write contract={'mutation': mut.value, 'is_clean': ...}. No pixels: model/vlm_jev.py extract_features calls self.backbone(input_ids=..., attention_mask=..., output_hidden_states=True) with no pixel_values, and train/train.py calls UiEvidenceDataset(train_samples) with no tokenizer. Noise features: train_consultant.py sets torch.manual_seed(hash(id)) and then torch.randn(hidden). Python's str hash is salted per process, so the features are not even reproducible across runs. Random serving: server.py sets dummy_features = np.random.randn(1, _ort_hidden_size). Key mismatch: train_vit_consultant.py reads r.get('screenshots', []) while synthesizer.py writes 'image_paths'. No-op mutator: the WebSight card itself (README line 121, v0.2 details) gives the text format '&lt;html>\n&lt;link href="...tailwind.min.css" rel="stylesheet">\n{body}\n&lt;/html>'. It has no head element by construction. A 100-row sample (offset 0, via datasets-server, which is outside the literal api/models|datasets|spaces allowlist) confirms it: 100/100 rows lack `</head>`.

**Risks.** Every head as committed learns either label marginals (zero input), a text lookup of the label (contract leak) or noise. Label noise is systematic: low_contrast mislabels 100% of WebSight rows. Train/val are duplicated, so any score is memorization. The served endpoint returns random probabilities while looking typed and 'calibrated'. The README cites teachers and hardware that do not appear in the code, and there is no license. Safety-sounding claims ('HIPAA/GDPR', 'zero PHI leak', CI/CD gates) could lead someone to deploy a gate that decides at random.


### 6.10 github:azerothl/akasha-model (table #10)

**Revision.** main a8c14f3699c5. Branches: cursor/rlcd-type-balance c2f74e365a17, docs/dataset-zeroshot-decision 95941372b4a8. Commit trailers show co-authoring with OpenAI Codex, Cursor and Claude.

**Inspected.** github:azerothl/akasha-model @ a8c14f3699c5 (main, 2026-09-21T07:03:43Z; created 2026-09-20; pushed_at 2026-09-22T20:17Z, which matches no current branch head: the latest is 08:33Z, so it was probably a ref push or deletion). README blob 169da1b06dd2, examples/doom/README 53cdc4cb, examples/chess/README 853e773b, LICENSE 66f4d5a2 (MIT). Read in full: akasha_model/vision.py and examples/doom/audit.py. Read in part: examples/doom/environment.py (head); grep over train_imitation.py and train_dagger.py (expert), chess/positions.py (Stockfish), akasha_model/typed_decisions.py, rlcd.py and rewards.py. Side branches: cursor/rlcd-type-balance @ c2f74e365a17 (2026-09-22T08:29Z) adds 6 JSON reports; I read typed_decisions.json, akasha_os_multi_v4_bert.json and akasha_rlcd_C.json. docs/dataset-zeroshot-decision @ 95941372b4a8 (docs only) is not read. Dataset card: LocalLLaMA/typed-decisions @ c76749ec58bd (grep). The .pt checkpoints in the repo were not downloaded. First sighting.

**Modalities.** Text/JSON Choice/Score/Noul through a byte encoder, a tiny transformer, or an HF MASK encoder (bert-base-uncased or ModernBERT). Images for the game controllers: 160x120 RGB plus one motion channel, for Doom and a rendered chess board. No audio and no video beyond a one-frame difference.

**Backbone.** DoomScorerV2 is trained from scratch: conv stem 4->16->32 plus a 4x4 patch conv, width = rank = 32, checkpoints ~126 KB. A PlainConvPolicy (flat MLP) architecture control is included. The text path uses a tiny transformer or a trained (not frozen) bert-base-uncased or ModernBERT.

**Head or readout.** Option attention: each option embedding (one 12-row table: 7 Doom buttons, 5 chess keys) forms a query. Keys are the context projection plus fixed positions, and each option reads the 80 patches once. The logit is q . attended / sqrt(rank), extra reads are averaged, and a softmax runs over the active options. A value head on the mean context serves PPO. Text path: a shared scorer at each [MASK] marker, with noul as the false/true pair.

**Input coverage.** Game path: a 160x120 RGB24 frame (ViZDoom RES_160X120; the 640x480 option only changes the recorded footage, and the policy still sees 160x120). A signed greyscale difference from the previous frame is added as a uint8 channel centred on 128. RGB is normalised per image by mean and std, then padded to 160x128. The conv stem (strides 2 and 2) and a 4x4 patch conv produce 8x10 = 80 patches of 16x16 px, with fixed 2D sinusoidal positions added to the keys. The policy decides at 8.75 Hz (TICS_PER_ACTION=4 at 35 tics/s). Its only memory is the one-frame difference; there is no recurrence. In chess the frame is the whole state: a 120x120 board (15 px per square) with overlays for the cursor, the lifted piece and legal-move dots, and a budget of 40 key presses per move. With no memory, greedy decoding loops: halfway through DAgger, 68% of moves hit the key budget, so sampling is required. Text path defaults: the byte encoder keeps 192 bytes of context and 32 per option; multitask keeps 768/512/384 tokens; bert-base is capped at 512 tokens. Options come before the state, so a long option block truncates the state.

**Training data and labels.** Doom: a heuristic expert (expert_action, attack_threshold 0.12) reads the ViZDoom labels buffer. Those engine object labels set training targets only; the policy sees pixels plus motion. Pipeline: imitation (500 episodes x 16 envs), then DAgger (the expert labels the states the student visits), then PPO on deadly_corridor. Mirror augmentation flips the image and swaps left/right labels. Chess: Stockfish depth-10 teacher moves on generated positions (noisy low-strength self-play after random openings, plus the winning side of Stockfish-vs-random games). Each move becomes a cursor walk (rows first, then columns), and every frame on the walk is labeled with the teacher's next key. DAgger then trains on a 50/50 mix of teacher walks and the model's own states, labeled with the teacher's next key. Released checkpoints: doom/deadly-dagger.pt; chess/chess-dagger1.pt (7,500 pretrain + 6,000 DAgger steps); checkpoints/joint-imitation.pt (one 12-row option table covering both games). Text data: deterministic synthetic generators (Akasha-OS routing, and multitask v1-v4 derived from identifiers in a local Akasha OS checkout; a grep of the v3 generator found no LLM or API calls), Wikispeedia human clicks (SNAP), and optionally the LocalLLaMA/typed-decisions train split. That split's gold is the mean of 3 samples at T=0.7 from an unnamed ~4B-class teacher endpoint, and it is loaded with load_dataset without a revision pin.

**Jev-output provenance.** no-provider-outputs for the Doom and chess checkpoints and the Akasha-OS synthetic text runs: the labels come from code experts (ViZDoom labels buffer, Stockfish) and deterministic generators. Exception: the side-branch report reports/typed_decisions.json @ c2f74e36 is a bert-base-uncased RLCD run trained on the Hub typed-decisions train split. That run is teacher-labeled with the provider unnamed. The dataset card says it is not affiliated with TypeSafe and does not reproduce Jev, but a third-party README (Manavarya09/verdict) says the set was 'labelled by Jev'. The conflict is recorded in research/080/clm-2026-09-23.md. Under that local rule, any head trained on typed-decisions gold is barred from Augustus training paths until the conflict is resolved. It is not in the released checkpoints.

**Calibration.** Text path: temperature fitted on a separate calibration split (akasha-calibrate), an optional Brier term (--calibration-weight), NLL/Brier/ECE, coverage-risk tables, a shuffled-context control, and abstention when a seed ensemble disagrees. The RLCD reward is log score plus 0.5 x spherical minus RPS on ordinal heads, with a group-mean baseline. Game path: no calibration; probabilities are used only for sampling. The typed-decisions README example passes train.jsonl as --validation, so it selects on train.

**Eval evidence.** All figures are the author's own; no raw game logs are on main. Chess (chess-dagger1, 50 games per opponent, 25 per colour, sampled keys): vs random 4W/46D/0L; vs Stockfish level 0, 0W/2D/48L; vs level 3, 0W/0D/50L. Wasted presses 4%, budget failures 14-17%, centipawn loss 288/155/144 (the three opponents in order). Probes: naming the cursor square is 99.95% correct on held-out positions; next-key accuracy with the target square marked is 94%; without the mark it plateaus near 65%, the same on train and held-out, and a 2x wider net is no better. The legal-move dots add about 7 points, and DAgger cut wasted presses from 24% to 4%. The author's summary: it learned the controller, not chess. Doom: the joint checkpoint averaged 0.60 kills and -97.50 reward over 10 recorded episodes; the demo windows were 'selected for activity' (their words). Pure-pixel PPO was 'a poor starting point'; imitation, then DAgger, then PPO was more reliable. The joint Doom+chess checkpoint 'lost much of the chess controller' (forgetting). Audit tool (doom/audit.py): computes the KL between predictions on real frames and on blank, patch-shuffled and dataset-average frames, and against the mean policy. It also measures p(attack | enemy centred) minus p(attack | enemy off-centre), turn-left/right margins by enemy side, attention entropy, and the correlation between attention x and enemy x. No audit output is committed. Text, side branch c2f74e36 (author's CUDA runs): on the typed-decisions test set (2,000 questions), accuracy 0.6605, soft accuracy 0.468, Brier 0.116, ECE 0.386 (choice 0.62, score 0.646, noul 0.72). Published comparators are Jev 0.727 and Laya 0.766, with much lower ECE than this run. Akasha-OS v4 with bert RLCD: overall 0.484, choice 0.104, score 0.293, noul 0.547, a collapse. rlcd_C (psr-mean) reaches 0.820 overall with choice at 0.159 and noul at 0.900: the pooled number hides a dead choice head, the README's own warning now measured. The README's older figures: synthetic menus ~98%; Wikispeedia 26% for frozen Qwen2.5-0.5B plus the scorer, against ~8% for controls.

**Compute and ROCm feasibility.** The game models are tiny and train on a CPU; the README reports 0.7 ms per key press on MPS. The Doom and chess scripts only offer --device cpu or mps, but adding 'cuda' (HIP under ROCm) needs no model change, and there are no CUDA-only kernels. Dependencies: ViZDoom (MIT; builds on Linux), python-chess and a Stockfish binary. tabputer-1's 16 Zen 5 cores fit 16 parallel envs; the M4 works through MPS. BERT RLCD: the README says batch 4 at 768 tokens with group 4 does not fit 16 GB; batch 1 fits either box, and ModernBERT falls back to SDPA without flash-attn on gfx1151.

**License.** MIT (LICENSE file; GitHub API agrees). The bundled checkpoints are MIT by implication. ViZDoom is MIT. Stockfish is GPL-3.0 and is only a label oracle; record it, though no restriction on engine outputs is apparent. Wikispeedia follows SNAP terms. typed-decisions is Apache-2.0, but its teacher's terms are unknown. The film soundtrack is excluded as author-owned.

**Borrow for Augustus.** (1) Make the media-dependence audit a required falsifier for every image or video head. Compare predictions on real inputs with predictions on blank, dataset-average and patch-shuffled inputs (KL), and add a conditional probe wherever a ground-truth visual factor is known (enemy centred should raise p(attack)). Fix the pass threshold before looking. Other modalities: silence, shuffled-segment and cross-clip swaps for audio; blank and shuffled-crop for documents; image swaps across items for text+image. (2) Curriculum when a code or engine expert exists: imitation, then DAgger (the expert labels the student's own states), then optional RL. Pure-pixel RL from scratch was the worst start, and DAgger cut wasted actions from 24% to 4%. (3) Gate on per-head and per-task metrics. A dead choice head (0.159) hid inside a pooled 0.82. Gate each joint checkpoint on fixed held-out per-task metrics before it replaces the old one, which catches forgetting. (4) Locate a failure with probes: readout at 99.95%, marked target at 94% and unmarked at 65% put the limit in the policy, not in perception. (5) Coverage lesson: when a decision needs history, give the state an explicit history (frame stack or trace) or keep that decision in code. Do not borrow the typed-decisions training path.

**Provenance evidence.** examples/doom/README: 'The heuristic expert uses the object labels supplied by ViZDoom only to make training labels; the policy itself receives pixels and motion.' train_dagger.py records training_config method 'DAgger with labels-buffer expert'. chess/positions.py calls eng.analyse(board, Limit(depth=10)). typed_decisions.py calls load_dataset('LocalLLaMA/typed-decisions', config, split=split) with no revision. The branch report's published_comparison labels the Jev figures 'third-party published, not measured here'.

**Risks.** (1) A high reward can come from a fixed action habit; the author flags this. (2) Joint training causes forgetting. (3) Pooled accuracy masks a collapsed choice head. (4) The game models have no memory, so they loop. (5) The typed-decisions path has unresolved teacher provenance and an unpinned dataset. (6) The demo windows were selected. (7) Every result is self-reported, and several reports live only on a side branch.


### 6.11 github:JonathanHHenson/laya-multimodal (table #11)

**Revision.** daaa3f99f60f (main). Parent ba4e0575a809. Package version 0.1.0.

**Inspected.** github:JonathanHHenson/laya-multimodal @ daaa3f99f60f (2026-09-22T13:07:22Z; 2 commits; created 12:23Z). README blob 0db71530c72d, LICENSE 6b0b1270 (Apache-2.0), pyproject d3aa8034. Read: src/laya_multimodal/{encoders/siglip.py, encoders/clap.py, head.py, training.py, cache.py, calibration.py, devices.py}, a grep of cli.py, tests/test_training.py, the CI workflow, and examples/{dataset.example.jsonl, questions.json}. CI run 35731456449 passed (ruff + pytest, 2m06s). HF: google/siglip2-base-patch16-224 @ 75de2d55 and laion/clap-htsat-fused @ 365dea6e (both Apache-2.0), including their preprocessor_config.json. Not read: engine.py, schemas.py, state.py, metrics.py, benchmarks/. No weights, no execution. First sighting.

**Modalities.** Image (SigLIP2) and audio (CLAP). One media item per ask call. Text appears only as question and option prompts. No video, and no document or screenshot path beyond generic images.

**Backbone.** Frozen google/siglip2-base-patch16-224 or laion/clap-htsat-fused; both the media tower and the aligned text tower stay frozen.

**Head or readout.** V0 (zero-shot): cosine similarity x exp(logit_scale), clamped at 100, plus the SigLIP logit_bias, then a softmax over the runtime options. V1 DynamicDecisionHead: state and option projections into 384 dims (6 heads, 2 layers). Options self-attend (permutation-equivariant, with no option position) and then cross-attend to the media tokens, followed by a feed-forward layer. The scorer is Linear(384,1), zero-initialised, and adds prior_scale x the V0 logits, so training starts exactly at V0 and learns a residual. Question types are choice, binary and score; score reports the expected level.

**Input coverage.** Image: the fixed-resolution SigLIP2 base-patch16-224 processor resizes to 224x224 (bilinear), which squashes the aspect ratio, with no tiling. That yields 196 patch tokens (d=768) for cross-attention plus a pooled embedding, so small text and fine detail in screenshots or documents are lost. Options: each is rendered as 'This is a photo where the answer to "{question}" is "{option}".' and encoded by the SigLIP text tower with max_length=64 and truncation=True. The option comes last, so a long question silently truncates it away and the options can collapse to identical embeddings. Audio: CLAP htsat-fused runs at 48 kHz mono (stereo averaged, librosa resampling) with max_length_s=10. truncation='fusion' means audio longer than 10 s becomes a fused mel of randomly chosen chunks plus a downsampled global view. That is stochastic unless seeded, and the content-addressed cache freezes a single draw. padding='repeatpad' repeats audio shorter than 10 s. The adapter emits one global token, so temporal localisation is impossible and V1 cross-attention over audio is degenerate. The encoded state records width/height or duration.

**Training data and labels.** None bundled. The user supplies JSONL rows of {media, question{id,type,prompt,options}, target or target_distribution}, so targets can be hard or soft. The example file has two lines. There is no split tooling: the user brings separate train, validation and test files, and no group-split helper exists.

**Jev-output provenance.** no-provider-outputs. The repo ships no labels, no weights and no teacher code, so label provenance belongs entirely to the user. Record it per project: a user who fills target_distribution from Jev or any other hosted provider inherits that provider's terms, and nothing here prevents it.

**Calibration.** Temperature is fit by LBFGS on NLL over a separate validation file: one shared default, plus one temperature per option count wherever at least 8 rows share it. The engine abstains below the abstain_below threshold. Metrics: accuracy, NLL, Brier, ECE, and RPS only when every row is a score question. Defects: (a) fitting and evaluation use the argmax of target_distribution, so soft labels are collapsed. (b) --loss rps runs with option shuffling on by default (unless --no-shuffle-options), and RPS over shuffled options is not an ordinal score. (c) One loss applies to every question type in a batch. The CLI guards against none of this.

**Eval evidence.** None, and the README says so: 'No unmeasured speed or accuracy numbers are claimed.' CI runs only unit tests (loss finiteness and ordering, schemas, head shapes). benchmark_inference.py reports encode time separately from warm ask time, the correct split, but no results are committed.

**Compute and ROCm feasibility.** The cheapest omni rung here. Only the small head trains, against frozen base-size encoders whose states are cached as safetensors keyed by the media bytes plus the encoder id. The documented target is an M4 with 24 GB through MPS (PYTORCH_ENABLE_MPS_FALLBACK=1). On tabputer-1, resolve_device('auto') tries cuda first, which is HIP under ROCm, then mps, then cpu, and uses fp16 on cuda and mps. There are no custom kernels and no flash-attn or bitsandbytes. librosa and soundfile run on the CPU.

**License.** Apache-2.0 (LICENSE file and pyproject); both encoders are Apache-2.0 at the pinned shas. The README states the project is not affiliated with Laya.

**Borrow for Augustus.** (1) The skill's rung 0/1 for multimodal decisions. Rung 0: a frozen aligned encoder gives a V0 zero-shot typed decision with no training at all. Rung 1: a V1 residual head initialised to reproduce V0 (zero-init scorer plus the V0 prior). Training cannot start below zero-shot, and the V1-minus-V0 gap is the measured value of training. Falsifier: V1 must beat V0 on a held-out group split under a proper score (NLL or Brier); otherwise ship V0 or no model. (2) Encode once and ask many times, with a content-addressed state cache, and always report encode latency separately from ask latency. (3) An input-coverage checklist for the recipe: encoder resolution (a 224 squash here), the prompt token cap (64), the audio window (10 s at 48 kHz, fusion or repeatpad), and token granularity (global, patch or time). Declare decisions that need finer evidence as unknown or out of scope. (4) Fix before reuse: turn off shuffling for ordinal RPS, use per-type losses, fit temperature by soft-label NLL, put the encoder revision and processor config in the cache key, and use seeded or deterministic audio windows.

**Provenance evidence.** training.py TrainingExample.from_dict takes 'target' or 'target_distribution' from the user's JSONL. The repo contains no network or API calls beyond HF from_pretrained. siglip.py encode_text uses max_length=64 with truncation=True. The CLAP preprocessor_config sets truncation 'fusion', max_length_s 10, sampling_rate 48000 and padding 'repeatpad'. The SigLIP2 preprocessor size is 224x224.

**Risks.** (1) Nothing is validated: no data, weights or results. (2) The 64-token option cap. (3) Audio gets one global token and a 10 s window. (4) The random fusion crop is frozen by the cache. (5) The cache key omits the processor and transformers versions. (6) RPS runs on shuffled options. (7) No validation during training: every epoch is saved and nothing selects a model. (8) V0 softmaxes SigLIP's sigmoid-trained logits across options, which assumes they are comparable.


### 6.12 github:TalalAhmed311/laya-multimodal (table #12)

**Revision.** 923538c48e82 (only commit). HF weights 8e36b7039f49. The base is fetched unpinned: snapshot_download('convaiinnovations/laya') at HEAD.

**Inspected.** github:TalalAhmed311/laya-multimodal @ 923538c48e82 (single commit 2026-09-23T10:20:56Z; default branch master). README blob 48cdb88c7531, requirements b3368c1a. Read: src/data.py, src/model.py, scripts/extract_features.py and scripts/baseline_text_only.py in full; the eval, temperature, RLCD-loss and argument sections of scripts/train.py; the ladder definitions in scripts/run_experiments.py; the head of aws/README.md; and notebooks/train_multimodal.ipynb (22 cells, 0 outputs). HF: TalalML123/laya-multimodal-best-all-tasks @ 8e36b7039f49 (created 2026-09-23T09:52Z; card license apache-2.0; files best.pt and history.jsonl). I read its README and history.jsonl (776 rows, a text log); best.pt was not downloaded. Base model: the Architecture/Training sections of the convaiinnovations/laya card @ aa8c91ca (lastModified 2026-09-23T18:09Z); google/siglip-base-patch16-224 @ 7fd15f06 (Apache-2.0). First card; the only earlier sighting is archive/2026-09-23-patrol, where the HF weights appear in the coverage ledger.

**Modalities.** Image plus a text question (VQA v2 on COCO train2014). The image enters only as cached frozen patch features.

**Backbone.** Frozen, cached SigLIP-base-224 vision features. The text encoder is convaiinnovations/laya's English ModernBERT-large, frozen in stage 1 with its last 4 layers unfrozen in stage 2. Laya's head layers and scorer are frozen in stage 1 when --freeze-head is set.

**Head or readout.** A projector (LayerNorm, Linear, GELU, Linear; d_v to d) and 2 cross-attention blocks, in which the text tokens query the image patches, sit before Laya's head layers. The hidden state is gathered at each [MASK] option marker and scored by Linear(d,1) per option, with a type embedding added. The label set stays open.

**Input coverage.** The default google/siglip-base-patch16-224 resizes to 224x224 and yields 196 patches x 768 dims, cached as an fp16 memmap: about 0.30 MB per image, ~25 GB for COCO train2014. There is no OCR, and extract_features' own docstring says to use 384 px only when the model must read text inside the image. Text goes through Laya's build_sequence with the Laya cfg max_len/head_max_len (English Laya: 512/192 per its card). Items whose options do not all fit are dropped and counted as option_truncated. The state text is empty: the question serves as the instruction and the image is the state.

**Training data and labels.** VQA v2 train2014 human answers, 10 annotators per question. noul: the [no, yes] shares among yes/no answers; dropped if fewer than 6 of 10 answers are yes/no. score: 4 buckets (0, 1, 2, 3+) from numeric answers; dropped if fewer than 6 are numeric. choice: the gold multiple_choice_answer plus 3 distractors drawn uniformly from the top-3,000 answer pool with no answer-type matching; the target is the annotator share over the 4 options, dropped if fewer than 6 answers are covered. README counts: yes/no ~167k, number ~58k, other ~219k. The split is 95/5 by image_id inside train2014, which correctly keeps all questions about one image together. VQA val2014 is never used for the reported numbers. The choice leak (my reading of data.py, consistent with the author's 'likely leakage' flag): untyped random distractors are usually incompatible with the question (a 'what color' question gets a single colour option), so the question alone answers most choice items.

**Jev-output provenance.** no-provider-outputs for the new training labels, which are VQA human annotations. The inherited weights are a different matter: the text encoder, head layers, type_emb and scorer are initialised from convaiinnovations/laya (English, ModernBERT-large). Laya's card describes its RLCD algorithm but not its training data or label source. The card also says Laya had no TypeSafe API access for its benchmarks, which says nothing about its training labels. Record: labels human (VQA); base Laya with unknown training provenance, unpinned; Jev use claimed nowhere.

**Calibration.** RLCD: Gaussian noise on the logits (sigma scheduled from 0.4 toward 0.1; the log ends at 0.25), groups of 4, and a reward from laya.common.proper_reward (log + 0.75 x spherical + 1.0 x RPS). The baseline is the group mean, advantages are normalised, and a CE anchor is added (w_ce). Afterwards, one temperature per question type is grid-searched (0.2 to ~11) on soft-target NLL, fitted on the same validation split used for selection and reporting, so the calibration is in-sample. A coverage-at-threshold table is printed.

**Eval evidence.** Author's figures (README; A10G on g5.2xlarge, ~3.4 h across 14 runs): noul-only ~0.52, score-only ~0.55, choice-only ~0.90 (their 'likely leakage'), best joint all-tasks stage-2 val ~0.692. History log (HF 8e36b703): 25 evaluations on val_items[:2000], one every 1,500 steps; accuracy rose from 0.636 to a best of 0.6917 at step 28,500, and patience stopped the run at step 37,500 (epoch 1, ~45 min). Val ECE stayed at 0.26-0.33 throughout, uncalibrated. There is no per-type breakdown, and the final post-temperature ECE and coverage table go to stdout only. Selection bias: the kept checkpoint is the maximum over 25 evaluations of the same 2,000 items that are reported, and the temperatures are refit on that same validation set. Decomposition: the README counts give ~49% choice, ~38% noul and ~13% score. Weighting the single-task results by those shares gives 0.49x0.90 + 0.38x0.52 + 0.13x0.55 = ~0.71, so the joint headline can be explained without the image doing any work. Per-type joint numbers are needed to tell. Noul at ~0.52 is chance level for a 2-way question. VQA v2 is only partly balanced, so a question-only prior should sit above 0.5, and falling below that prior suggests the bridge or noul path failed. Laya's own card reports that noul can follow its option labels instead of the state (its issue #156), a plausible inherited cause that is not verified here. A text-only baseline script exists (stock Laya, zero-shot, no image), but no result is reported. A zero-shot floor is too weak anyway: the valid floor is the same trained pipeline with blank or shuffled image features.

**Compute and ROCm feasibility.** Trained on 1x A10G 24 GB; the author says 2x T4 also works with cached features. On tabputer-1, ModernBERT-large (395M, last 4 layers trainable) plus a ~29M bridge at batch 16 with accumulation 2 fits easily in ~115 GB of unified memory. torch.autocast('cuda', bf16) maps to HIP on ROCm. ModernBERT prefers flash-attn but falls back to SDPA (the code sets reference_compile=False). There is no bitsandbytes or deepspeed, and the RLCD noise is added to logits, so it costs no extra forward passes. The ~25 GB fp16 feature memmap is disk-bound: the code's own probe warns when 64 rows take more than 60 ms. Training needs a VQA v2 plus COCO train2014 download (~13 GB+). Expect it to run slower than on the A10G; nothing was measured here. The M4 24 GB is feasible only with --limit subsets (~6 GB of features per 20k images).

**License.** The GitHub repo has no LICENSE file (API license null); the README credits Laya as Apache-2.0. The HF weights card claims apache-2.0. Inputs: VQA v2 annotations and COCO images carry their own terms (verify at visualqa.org and cocodataset.org); SigLIP and Laya are Apache-2.0.

**Borrow for Augustus.** (1) Human multi-annotator distributions (VQA's 10 answers) are a clean, provider-free soft-target source for Choice, Score and Noul. Record the drop rules (fewer than 6 agreeing answers) as coverage loss. (2) Split by media id by default, keeping every question about one image in the same split. (3) The design-changing negative: how the distractors are built decides whether a multimodal Choice head needs the image at all. Require type-matched hard distractors (the same answer type as the gold, ideally answers to the same question on other images). Report a trained question-only floor per head, with image features zeroed or shuffled. Falsifier: if that image-blind control is within noise of the multimodal model on a head, the head does not use the image. (4) Report per-type metrics, never a pooled joint accuracy. Select on validation, report on an untouched test set (VQA val2014 exists and went unused), and fit temperature on a third split. (5) Pin every inherited base (repo plus sha) and record its training-data provenance as unknown when the card does not disclose it.

**Provenance evidence.** src/data.py: noul_target, score_target and choice_target build targets from the 10 VQA answers. The distractor line is `distract = [w for w in rng.sample(pool, n_choice_opts * 3) if w != gold][:n_choice_opts - 1]`, with pool = top_answers(annos). split_items is 'Split by IMAGE'. src/model.py load_laya_backbone calls snapshot_download(repo) with no revision. scripts/train.py has fit_temperatures(Z, keep) on val_items after selection on val_items[:eval_n]. history.jsonl evaluates every 1,500 steps, while run_experiments.py sets eval_every=1000, so which command produced the published log is unclear.

**Risks.** (1) The choice leak dominates the pooled metric. (2) Selection and calibration are both in-sample. (3) noul sits at chance. (4) The inherited base is unpinned and its provenance undisclosed; Laya's card changed at 2026-09-23T18:09Z, after this run. (5) The README points to checkpoints on a deleted machine. (6) The notebook has no outputs. (7) Single commit. (8) There is no inference script that reproduces the fp16 224 px SigLIP preprocessing at serve time.


## 7. Comparison matrix

Rows 1–12 are carded (Contract plus Reported). Rows marked *item depth* rest
on lane records only. Every number in the matrix is theirs.

| Recipe | Modalities | Backbone | Head / readout | Input coverage | Labels / provenance | Calibration | Eval (theirs) | ROCm / gfx1151 (Hypothesis) | License |
|---|---|---|---|---|---|---|---|---|---|
| 1 circuit vl-4b / audio-7b | Text; 1 image or 1 clip | Qwen3-VL-4B / Qwen2-Audio-7B; LoRA r16 on the LM; towers frozen | Pointer (decide · option end); parallel options in v1.2 | Default pixel budget; audio first 30 s; no frames or multi-image | Code render grids + Open Images human; TTS/transcripts; clear | Soft CE; worst-type-ECE checkpoint pick; fitted T=1.0 | Own grid .967 / ECE .021; POPE Brier .158 vs raw .139 | sdpa, no flash-attn; pins torch ≥2.14 (image ships 2.12); bf16 fits | Apache-2.0; FSDD CC BY-SA |
| 2 PlayJev | 1 game frame; text replay | Qwen3.5-0.8B-Base, full FT including vision | Letter logits via tied embedding, fp32 | 448 px, single frame, no motion or rules | Search programs on hidden state + DAgger; clear | Soft CE to smoothed teacher; no T | vs-teacher 0.57; agreement ≠ closed loop | FLA Triton unverified; torch fallback slow; built-in kernel parity check | Apache-2.0; some game art unlicensed |
| 3 alpha-sys-1 | Text; 1 image | LFM2.5-VL 450M/1.6B/3B; LoRA r32 LM+projector | LM-head label tokens; full-vocab soft CE | <256 px upscaled to 256²; ≤26 options | Dataset/annotator/outcome; clear; repo stores Jev preds | Per-environment dev CE stop; base+T baseline; NLL/Brier | Tier B/C gates FAIL; shift PASS; unseen < base+T | 'cuda' string works on ROCm; no custom kernels | Repo none; weights LFM1.0 |
| 4 Visual Jev (guanxuyu) | 1 image, many questions | Qwen3-VL-4B/8B; LoRA r16 on the language tower | LM-head candidate logits (a2) | ~448² pixel budget; K 2–16; no built-in abstain | GQA programs, SNLI-VE human; clear | None published for a2; heads T≈1.8 | Macro .706→.761; unseen sets uninformative | transformers+peft+sdpa; torch 2.14 cu130 pin | Apache-2.0; SNLI-VE Flickr terms |
| 5 visual-jev (andrue) | 1–8 images + JSON | Qwen3-VL-2B pinned; custom LoRA r8 | Pointer over option ends; isolated branches | Corpus ≤1024 px; right-side occlusion only | ~56 samples; shortcut labels; LNQA Mixtral | One T on calibration split | None published | Plain torch; promotion needs NVIDIA comparator | None |
| 6 cua-s1 | 1 screenshot or ax-tree per step | Qwen3.5-4B frozen + LoRA r16; nano 855k | Letter logits ≤26; scoped CE; RLOO+Brier RL | No history; pruning to 11 can drop gold | Synthetic, AndroidControl, GUI-360 agent gold; unknown | No post-hoc T; Brier on episode confidence | mm .929 (N=168); regresses on synthetic | device 'cuda'; no FLA in lock; transformers <5 | MIT; 0.2 Apache; others unlicensed |
| 7 Jev-Vision (sseanliu) | 1–2 screenshots/images + state | Qwen3-VL-8B; LoRA r64 + typed heads | Shared prefix, branch heads | ~1288×1000 desktop only | Mind2Web, env recorder, Qwen3-VL-32B soft; repo has Jev data | Fixed T=0.5 (swept) | General .917 vs frozen .911 (tie) | sdpa; 8B LoRA far over 16 GB cap | Apache-2.0; jsonl_jev is Jev Output |
| 8 qev | Text-trained; media untrained | Qwen3.5-0.8B frozen; LoRA incl. GatedDeltaNet proj. | 256-d pointer; one sequence per question | ≤8 media; client-sampled frames; audio rejected | Public gold, rule programs, BFS; clear | One T, reused for FP32 MLX | Dev 81.36% (v0.2, not locked) | Torch path, no FLA/bnb; plausible | Apache-2.0 |
| 9 mesen | Claimed 4 viewports + DOM | Qwen3.5-2B (never sees pixels); ViT-B/16 path | 5 choice + score MLPs, learned T | First viewport, 224 squash | Mutation type; leaked; 100% no-op sample | Trainable T + focal loss | None; serving random | Trivial; not worth box time | MIT claimed, no LICENSE |
| 10 akasha | Text/JSON; 160×120 frames + motion | From-scratch conv stem (126 KB); BERT text | Option attention over 80 patches | 8.75 Hz, 1-frame memory | Doom engine labels, Stockfish; branch barred pending | Text path T on a split; games none | Chess 0W/50L vs level 3 | CPU/MPS; trivial anywhere | MIT; Stockfish GPL oracle |
| 11 laya-multimodal (Henson) | 1 image or 1 clip | Frozen SigLIP2-base-224 / CLAP-htsat-fused | V0 zero-shot + zero-init residual option-query head | 224² squash; 64-token options; 10 s audio | User-supplied | LBFGS T per option count; soft labels collapsed | None (says so) | Trivial; fits any cap | Apache-2.0 |
| 12 laya-multimodal (Talal) | Image + question | Frozen SigLIP-base + Laya ModernBERT-large | [MASK] scorer after cross-attn bridge | 224 px, no OCR | VQA 10-annotator; base unknown | RLCD + per-type T in-sample | Joint .69 ≈ image-free .71 | Fits; SDPA fallback; 25 GB memmap | Repo none; weights Apache-2.0 |
| tinnel OmniJev 4B / 0.8B / 2B *(item depth)* | Image, frames, screens, audio as spectrogram | Qwen3-VL-4B; Qwen3.5-0.8B/2B; LoRA | Decision + ordinal heads; NOTA; order-invariant | Frames sampled; audio via images | Public + own renders; unnamed teacher (0.8B) | Per-type T on held-out | Base zero-shot shown; regressions | Qwen3.5 FLA caveat; 4B plain | CC-BY-NC / PolyForm NC |
| Jev-Omni *(item depth + local card)* | Text, image, audio ≤30 s, video 16 frames | Gemma 4 12B text decoder, LoRA r512 | 256-way option-position head | Stock towers; position not text | Undisclosed; self-attested no-Jev | None in inference path | Trails Jev on own bench | CUDA loader; BF16 ~25 GB | Apache (Gemma) |
| Qevi-2B *(item depth)* | Image + closed questions | Qwen3-VL-2B full FT | LM-head logits at reply start | Not stated | Ground truth; clear | Label smoothing, T=1 | Held-out ECE .160→.054 | bnb 8-bit AdamW: swap on ROCm | CC-BY-NC |
| Dohnuts *(item depth)* | Text + 1 image | Qwen3.5-0.8B frozen; LoRA r8 + scorer | Candidate scorer; RLCD+CE | One image | Public groups + typed-decisions; barred pending | Per-type T, independent partition | 78.21% macro, one seed | Trained on RX 7900 XTX (gfx1100) | CC-BY-NC-SA |
| Prosodia *(item depth)* | Audio (no ASR) | Frozen Whisper encoder | Pointer; questions folded into batch | Whisper window | MELD human; clear | CE+0.5 Brier | ECE cannot rank arms; text-only controls | 4–5 GB; CPU/ROCm plausible | NOASSERTION; MELD GPL-3.0 |
| Valen *(item depth)* | Image, video, text | Qwen3.5-0.8B/2B, shared head | Staged; RLCD GRPO + KL | Not read | 100k set, targets unstated; unknown | Not stated | Sokoban 87.6% | 8-GPU NVIDIA launcher | Apache-2.0; ChartQA GPL |

## 8. Good and bad multimodal patterns

Each row pairs an explanatory good case with a bad one and ends in a rule the
skill can check. Every number is theirs unless marked Measured-here.

### 8.1 Coverage gaps (what the model never sees)

| Pattern | Good | Bad | Rule for the skill | Falsifier |
|---|---|---|---|---|
| Declared media budget | qev: ≤8 media, 2 MB / 4 MP each; video as client-sampled frames with a declared fps; audio rejected explicitly. andrue: request and checkpoint limits in the contract | circuit's HF card says "video as sampled frames", but the served code accepts one image and returns HTTP 422 on a frame list. mesen claims four viewports and fuses none | The decision record carries `input_coverage`: media count, pixel budget and resize rule, frames (count, fps, sampler), audio (sample rate, window, truncation rule), token granularity (global, patch or time), and OCR dependence | A request outside the declared coverage must be refused or routed, never scored |
| Resolution | BS3D#440: a 256-px crop beats the scaled full frame 7/7 vs 5/7. thaitea split1024 adds 1.4 points | Henson and Talal squash to 224² (small text is lost). alpha-sys-1 upscales 32–96 px patches to 256². andrue caps training at 1024 px, so full-resolution document text is out of coverage | Crop and resolution are policy parameters, recorded and tested like thresholds | A resolution ablation on the workload must not flip the gate decision |
| Candidate construction | Visual Jev varies K from 2 to 8 in training, because a fixed K left slots without gradient | cua-s1 prunes candidates to 11 by lexical overlap, so gold can be dropped before the model sees it | Log whether gold was in the option set; count "gold absent" separately from "wrong" | — |

### 8.2 Frame sampling and time

| Pattern | Good | Bad | Rule | Falsifier |
|---|---|---|---|---|
| Motion must be in the input if the decision needs it | MotionBlind (2609.09528): paired clips that differ only in motion, with four-answer credit (floor 6.25%) | PlayJev releases on a single frame (two_frame=false): Flappy 0.973 per-frame agreement vs 0.18 closed-loop. akasha has one-frame memory, and greedy decoding loops | If the decision depends on history, give the state an explicit history (frame stack or trace), or keep that decision in code | A frame-shuffle or single-frame arm must lose on motion-dependent items |
| Decode contract | ngqtrung video-r1 states fps=1, ≤24 frames, 100k px. Jev-Omni states 16 frames | The same sources decode differently across repos (video-r1 notes this) | The frame sampler is part of the model version, and changing it forces recalibration | — |

### 8.3 Audio dropped or truncated

| Pattern | Good | Bad | Rule | Falsifier |
|---|---|---|---|---|
| Probe the encoder, not the decoder | Prosodia: a frozen Whisper encoder whose decoder never runs. monica: selected Gemma 4 E2B audio-tower layers. sloina and pehredaar: tiny linear heads. 2609.00727: style is encoded late in the encoder and lost before the output | tinnel OmniJev-0.8B routes ESC-50 through the image path as spectrograms and gets 0.473. boyuzhu drops every audio subset from an omni guard | Audio decisions start at M-R2 on audio-encoder features | M-R2 on encoder features must be non-inferior to an omni-LLM readout, or the omni model is needed |
| Window truncation | Henson records duration in the state | circuit-audio: the Qwen2-Audio feature extractor keeps only the first 30 s (inferred from the base processor config). Henson's CLAP 'fusion' crop is random, then frozen by the cache | Record the audio window. Evidence past it is unseen, and the question must say so or abstain | Place the decisive segment after the window: accuracy must fall to the blind arm |
| Words vs acoustics | CLASH (2609.16582): lexical-preserving vs prosody-preserving arms. SEAR: a text-only probe splits text-answerable from audio-dependent items | Prosodia's prosody effect did not survive a base-rate control. pehredaar's audio is all hosted edge-tts synthesis | Report a transcript-only arm next to the audio arm | If transcript-only matches audio, it is a text decision: use the text ladder |

### 8.4 OCR, screenshot and option leakage (blind shortcuts)

| Pattern | Good | Bad | Rule | Falsifier |
|---|---|---|---|---|
| Blind-vs-sighted audit per eval set | Visual Jev leak.json: chance, blind, sighted and visual gain per benchmark. r33drichards/laya-vision adds shuffled/control images and a per-dataset ECE noise floor. akasha: KL on blank, averaged and patch-shuffled frames | The TextVQA K=4 build was leaky (0.997 sighted). Talal's choice head reads random distractors. MedQA-MM text-only reaches 53.96% | Every multimodal eval reports chance, the blind bound (2609.06190), text-only, options-only, blank and swapped arms, from the same trained pipeline | Sighted minus best blind arm must have a paired cluster-bootstrap LCB > 0 |
| Label read from text, not pixels | circuit labels come from the renderer | mesen puts the mutation name in the prompt. andrue labels RICO by aspect ratio and the safety noul by source identity | Label-audit rule: reject a label derived from geometry, source identity, transform index or prompt fields unless the question asks exactly that | Ablating the fields that encode the label must not collapse the metric |
| Multimodal claim audit | andrue fails closed on a missing or mismatched checkpoint. qev checks frozen-weight hashes before and after training, and adapter-off generation stays token-identical | mesen never passes `pixel_values`, and its served endpoint scores random features. Its latency figures time the heads alone | Before any multimodal claim, confirm three things: media tensors reach the encoder in both the train and the serve paths; latency includes the encoder; weights load fail-closed | Swapping the media on the served endpoint must change its outputs |
| Wording tracks the answer | Open-JEV-VLA's constant-answer check | Open-JEV-VLA's full-depth model tracks option wording, not the image (gripper 0.527 vs 0.5) | Include a constant-predictor and an option-wording-only arm | — |
| Text in image vs text in prompt | 2609.00550: MLLMs accept contradicting context more readily as an image. Mind2Web-Injection: report verdict, localization and counterfactual separately | Typographic injection goes untested in most repos | Screenshot and document decisions get a typographic-injection probe | — |

### 8.5 Synthetic multimodal labels

| Pattern | Good | Bad | Rule | Falsifier |
|---|---|---|---|---|
| Label by construction | circuit render grids (labels known to the drawing code, ~8% undecidable cells). PlayJev and Valen-Eval-Game solvers. mesen's idea (clean HTML, inject a defect, render) | mesen's low_contrast injects nothing into 100/100 sampled WebSight rows, yet labels them defective. andrue's quality score is the transform index | **Apply-check:** assert that the mutated pixels or DOM differ (a measured contrast ratio, a pixel diff) and drop no-op rows. Prefer measured labels (axe-core, geometry) over labels implied by the mutation | A no-op mutation rate above 0 fails the build |
| Undecidable targets | circuit separates two contracts: a flat distribution for photo blur, and an explicit 'Cannot tell' option for read cells | circuit vl-4b still gives mean confidence 0.88 on undecidable items that should sit near 0.5 | The skill states which contract it trains, and tests confidence on undecidable twins | Mean max-probability on undecidable twins must not exceed the prespecified bound |
| Split by source, not seed | JonesLin next-jev drops validation rows that share an image with train. Talal and Visual Jev split by image | circuit draws photos, speakers and utterances from one pool for train and eval ("held-out items, not held-out structure"). mesen duplicates rows across a random split | Group split by media hash, source image, speaker, site or page. Valen-100k needs hash grouping (50,203 references / 48,445 unique) | A leakage scan over media hashes and source ids must be empty |
| Synthetic inputs | circuit-audio records its Kokoro voices | pehredaar's all-synthetic audio (the author's stated main threat). The datapointai TTS clips are provider outputs | Record provider-synthesized inputs separately from labels | Test on at least one real-media slice before any claim |

### 8.6 Teacher circularity

| Pattern | Good | Bad | Rule | Falsifier |
|---|---|---|---|---|
| Gold from the task, not the behaviour policy | Jev-Vision after 5a554599: operation gold from the task oracle (0.911) | Jev-Vision before: 57% of recorded steps were deliberate wrong actions, so labels were wrong about half the time | Fail the build when targets come from logged actions of a mixed or exploring policy | Policy-derived and task-derived labels scored on task gold must differ, or the fix did not matter |
| Model-judge labels are not ground truth | Prosodia and alpha-sys-1 use human corpora | gemma-decision-kit measures agreement with 'AI-provisional' labels. 2609.15180: an LLM judge accepted 16/30 human-found errors. Jev-Omni's DecisionBench is Opus-5-generated and may share a pipeline with its training data (Hypothesis) | Label source is a per-row enum: human, code, environment outcome, open-weight model (id, revision), hosted provider (id, channel), unknown | — |
| Teacher chains | CA-OPD and circuit document their teacher gates | typed-decisions → Dohnuts / GPC-1. vjev: Jev → text stage → vision stage. Valen's game set is conditioned on model outcomes | Provenance propagates through `derived_from` and warm starts, not just through labels | — |
| Distillation advice | trainer-recipes §3.4 (local open-weight teacher, double agreement) | seangoedecke 2026-09-20: distil Jev I/O | Cite it as the barred route | — |

### 8.7 Readout, calibration and precision

| Pattern | Good | Bad | Rule | Falsifier |
|---|---|---|---|---|
| Readout choice | Visual Jev: the LM-head readout matches a typed head (+0.000). circuit: a pointer head buys order invariance (3.6%→0.0%) | Jev-Omni classifies option positions with no permutation probe. Verbalized confidence (2609.18453, 2609.20110: AUROC 0.54–0.74) | Default to the LM-head candidate readout. Add a head only for order invariance or multi-question packing. Never treat verbalized confidence as a Noul | If a matched-budget head wins on held-out families (not trained ones), switch the default |
| Order as bias and as ensemble | 2609.04362: permutation averaging, 55.7%→59.2%. PlayJev: shuffling per sample | Jev IIA shift of about −0.28 log-odds (Prosodia's probe) | Report the reorder flip rate. Average permutations at inference if flips follow position | Flip rate above the pre-set bound fails |
| Calibration population | alpha-sys-1: base+T is a mandatory baseline, NLL and Brier over ECE, clustered bootstrap. circuit: worst-type-ECE pick with an accuracy floor | Prosodia: a constant predictor gets ECE 0.0097. Talal fits T in-sample. Ruiruiz30: a global T made held-out ECE worse. AlignCP: fine-tuning breaks conformal exchangeability | Fit T per question type on a calibration split the model never trained or selected on; report NLL, Brier and a base-rate arm | The tuned model must beat base+T under a proper score |
| Precision | qev ships FP32 after FP16 failed. PlayJev reads out in fp32. Their verification files expose the drift | Jev-Omni serves bf16 with up to 0.2 drift; 4-bit ports shift ~0.24 | Evaluate and calibrate the exact served artifact; report argmax flips and max \|Δp\| | — |

### 8.8 Hardware (tabputer-1 gfx1151, M4 24 GB)

| Pattern | Evidence | Rule |
|---|---|---|
| Kernel parity before the first step | PlayJev `check_linear_attention_kernels` (fla vs torch reference, tol 5e-2). noamsto: llama.cpp HIP garbage logits on this APU until patch 865374bb | Add a VLM parity receipt to plan §4.4 (§9.2) |
| CUDA-only pieces | bitsandbytes (circuit --load-4bit, qinwuxu, Qevi 8-bit AdamW, vjev nf4, mesen extras); NVFP4 (LFM2.5-VL-3B-Decision, Geni, gemma-decision-kit); FLA Triton (Qwen3.5 family) | Swap 8-bit optimizers for plain AdamW; no NVFP4; Qwen3.5 only after a parity pass |
| Direct AMD evidence | olafura on gfx1151 via EXLA/XLA (probe 0.84 s); Dohnuts trained on RX 7900 XTX (gfx1100, not gfx1151); zojeda/jevons-rs HIP serving (WSL2) | None of it is PyTorch on gfx1151. Treat every recipe as untested on the box |
| Mac M4 24 GB | circuit vl-4b trained on an Apple laptop GPU in 85 min; andrue, multimodal-judge and Henson target MPS; qev FP32 MLX ran on an M4 16 GB | M-R1/M-R2 pilots are Mac-feasible (Hypothesis). Under errata D-b, experiments run on the GPU box or Colab, not the Mac |

## 9. Implications for an Augustus multimodal rung

### 9.1 Placement: a modality side-ladder parallel to trainer-recipes §6

Rules, the same as §6:
- Start at the lowest rung whose entry condition holds. Climb only after the
  incumbent fails a prespecified gate on untouched, group-split workload data.
  Use Kev's rule (paired delta positive, 95% lower bound ≥ −1 pp on the
  consumer metric).
- Every rung records model, revision, readout level, calibrator, data card and
  `input_coverage`.
- No rung uses Jev Output, and none uses typed-decisions descendants.

The numbering mirrors R0–R5, so the entry and exit semantics carry over.

| Rung | What | Labels needed | tabputer-1, 16 GB cap (Hypothesis) | Enter when | Leave when |
|---|---|---|---|---|---|
| **M-R0** Don't train / route | Exact rule, detector or OCR + rule; route to a native-multimodal reasoning model or a human. Never serialize pixels into text-only Jev (9% on base64 PNG, theirs) | 0 (validation) | yes | The blind-arm gate shows the task is not a media decision (go to the text ladder); an exact rule exists; the evidence needs history the input lacks | A measured media gap remains |
| **M-R1** Frozen VLM readout | Qwen3-VL-2B-Instruct (4B as escalation) candidate-letter logits in fp32, normalized over the valid K. Permutation averaging if flips follow position. OOF temperature per question type. Blind arms reported | 100–500 (temperature) + confirmation | yes (2B bf16 ≈ 4.5 GB) | Default first model | Coverage at the error budget, or policy loss, misses the target |
| **M-R2** Head on frozen features | (a) Ridge or LR on the M-R1 model's cached decision-token state (⅔ depth and last layer), from the same pass. (b) Frozen perception encoders (SigLIP2 image; Whisper encoder or CLAP audio; V-JEPA2 or VideoMAE video; DINOv2) with a V0 zero-shot prior plus a zero-init residual head | 30–300 per question | yes (trivial) | M-R1 fails; labels exist | Must beat M-R1+T by the gate |
| **M-R3** Small perception fine-tune | Fine-tune SigLIP2, ViT or a Whisper encoder plus a head on a stable closed label set; or a temperature-scaled small-model ensemble (2609.09189) | ~1k+ | yes | High volume, closed labels, latency-critical, M-R2 short | Fails an OOD source split. *Pilot only: thin evidence in this sweep* |
| **M-R4** VLM LoRA | Language-tower LoRA on Qwen3-VL-2B, vision frozen, LM-head readout (§9.2) | hundreds to thousands | 2B plausible; 4B needs an envelope decision | M-R2/M-R3 short, and the decision needs VLM knowledge or reasoning over layout | Loses to M-R1/M-R2 on untouched data, fails the blind-arm gate, or regresses slices |
| M-R5 RL / generalist omni | RLOO + Brier (cua-s1), RLCD (Valen, Dohnuts), SAVOR, full-FT omni guards | 10^4+ | no | Research only | Default: never |

### 9.2 Default multimodal recipe on tabputer-1

**Prerequisites. All must hold before any run.**
1. **GPU acceptance and parity.** Plan §4.4 acceptance passes on the errata's
   candidate image: `vllm/vllm-openai-rocm:v0.29.0`, `sha256:e5e47f6a…`,
   torch 2.12.0 + HIP 7.2, gfx1151 listed. Add a **VLM parity receipt**:
   - Compare the vision tower and option probabilities in GPU bf16 against
     CPU fp32 on 200 public images.
   - Proposed bounds: argmax agreement ≥ 99% and max |Δp| ≤ 0.02, fixed
     before the run.
   - Under errata D-b, a failure goes to Colab, not to CPU.
2. **Version check.** The recipe is reimplemented in-house against the
   transformers version in that image, plus a pinned peft if it is not
   already there (unverified). Third-party repo code is not run.
   - circuit pins torch ≥2.14 and Visual Jev pins 2.14 cu130, so neither
     installs as-is on torch 2.12.
   - Whether the image's transformers loads Qwen3-VL is unverified. Check it
     in the parity step.
3. **Design lock first.** Experiment datasets (VQAv2, COCO, Open Images,
   workload media) wait for the M2 design lock. This is the P1-1 reading the
   errata adopted.
4. **Envelope.** One run at a time; 16 GB container cap; launch at
   ≥ 24 GB MemAvailable; abort below 6 GB.

**Recipe.**

| Step | Choice | Evidence (label) |
|---|---|---|
| Backbone | `Qwen/Qwen3-VL-2B-Instruct`, revision pinned at design lock (andrue pins `89644892…`; re-verify). Standard attention on sdpa, Apache-2.0. Escalate to Qwen3-VL-4B only with an envelope decision. Use the Qwen3.5 family only after an FLA-vs-torch parity pass, with no shared-prefix packing | Visual Jev, circuit, Qevi (Reported); qev GatedDeltaNet constraint (Contract) |
| Data contract | Per row: media SHA-256; source-group id (image, photo, speaker, site, page); `label_source` enum (human / code / environment outcome / open-weight model id@rev / hosted provider id+channel / unknown); license; transform metadata; `input_coverage`. Locked test plus a source-disjoint transfer split | andrue contract, Valen-100k provenance meta, next-jev manifest (Contract) |
| Labels | Human multi-annotator distributions (VQA 10-answer style, ChaosNLI style); code or render-time labels with an apply-check; solver or simulator labels with DAgger; environment outcomes. Never Jev; never typed-decisions descendants; hosted-provider labels only under a §3.6 approval | §4, §8.5, §8.6 |
| M-R1 | Prompt ends "Answer:". Read logits for ' A'..' K' in fp32 and softmax over the K valid options. Run 4 option permutations if the flip rate exceeds the preset bound. Fit one temperature per question type on a calibration split. Arms: full, text-only, options-only, blank media, swapped media, base-rate constant | PlayJev fp32 readout; 2609.04362; alpha-sys base+T |
| M-R2 | From the same pass, cache the decision-token hidden state at ⅔ depth and at the last layer, and fit ridge or LR per question (Brier or log loss). For audio: a frozen Whisper encoder, or CLAP with a declared 10 s window and a seeded crop | 2609.18860, MedProb, Prosodia, sloina (Reported); trainer-recipes R2b |
| M-R4 (only on gate failure) | LoRA r16 / α32 / dropout 0.05 on the language tower's q/k/v/o/gate/up/down, vision frozen. Full-vocabulary CE on the gold letter, or soft targets from annotator distributions. K varied 2–8, options shuffled per sample. Mix: 60% workload, 20% general image QA, 20% text replay. lr 1e-4, about 3k steps, gradient checkpointing, max_pixels ≈ 200,704. Checkpoint = lowest worst-type ECE within 0.01 of best validation accuracy. Temperature on a separate calibration split. One read of the locked test | Visual Jev a2; PlayJev replay sweep; circuit pick_checkpoint (Reported/Contract) |
| Head | None by default. Add a pointer head with parallel option encoding only when order invariance or multi-question packing is required, and report its Brier cost on an external set | Visual Jev +0.000; circuit POPE Brier |
| Serving check | Recalibrate and evaluate the exact served precision; report argmax flips and max \|Δp\| against fp32 | qev, Jev-Omni, 2609.06922 |

**Compute (Hypothesis, to be replaced by the timing pilot).**
- M-R1 and M-R2 on 2B are prefill-bound and fit the cap easily.
- M-R4 on 2B at batch 2–4 with checkpointing is plausible under 16 GB.
- Visual Jev reports a 4B run at about 40 min on an RTX 5090 (theirs). Expect
  several times that on the iGPU.
- Qwen2-Audio-7B LoRA needs about 16 GB for bf16 weights alone, so audio stays
  at M-R2 unless the cap is raised.

### 9.3 Pre-registered falsifiers for the default

Set each threshold at the analysis lock, before looking.

1. **F1, media use.** On untouched group-split data, the sighted arm must beat
   the best blind arm (text-only, options-only, blank, swapped media) through
   the same pipeline: paired cluster bootstrap by media group, NLL delta
   LCB > 0.
   - Also report the closed-form blind bound.
   - If F1 fails, it is not a media decision. Route to the text ladder or
     M-R0, and train nothing multimodal.
2. **F2, rung.** A challenger replaces the incumbent only under Kev's rule.
   M-R4 must beat both M-R1+T and M-R2. Otherwise stop at the lower rung;
   "no training" is a valid outcome.
3. **F3, transfer.** A gain counts only on an untouched source-disjoint
   family that passes a leak audit (chance, blind, sighted). Saturated or
   floor-level sets are excluded. Evidence: Visual Jev, alpha-sys-1.
4. **F4, per type.** Every question type and head passes on its own; a pooled
   metric never decides. Evidence: akasha's dead choice head (0.159) inside a
   pooled 0.82, and Talal's decomposition.
5. **F5, order.** The option-reorder flip rate stays at or below the preset
   bound, either as trained or with permutation averaging.
6. **F6, outcome.** Where an environment exists, the gate metric is observed
   action success, not label agreement. Evidence: PlayJev, Flappy 0.973 vs
   0.18.
7. **F7, precision.** Calibration and the gate hold at the served precision.
8. **Design falsifier.** "LM-head readout by default" is wrong if a
   matched-budget typed head beats it on held-out families by the gate.

### 9.4 Proposed deltas (not applied here)

- **trainer-recipes.md.**
  - §6: add the M-ladder table (§9.1).
  - §10: its "multimodal or vision heads (Jev-Omni, Valen, SigLIP)" gap now
    points here.
  - §5: link the twelve cards.
  - §3.4 synthetic-data rules: add the apply-check, the media-group split and
    the label-audit rule (§8.4–§8.5).
- **plan-v3 §3.3.** The M-ladder is documented and ships "untested in 0.8.0"
  unless the maintainer adds a multimodal pilot (§9.5).
- **plan-v3 §3.6 test cases.**
  - A repo co-hosting Jev-distilled data: an artifact derived from that
    lineage is refused, and a sibling lineage resolves on its own parents.
  - A human label stored in a slot named "jev": resolve by lineage, not by
    the name.
  - Inputs synthesized by a hosted provider with human labels: `unknown` on
    the input edge.
  - Open-weight generated labels (LNQA/Mixtral): pass with provenance
    recorded.
  - A typed-decisions descendant: barred pending.
  - An AIMultiple-style Jev outcome table used for selection: refused.
- **plan-v3 §3.4.** Add rules for `input_coverage`, the blind arms and the
  media-hash group split.
- **plan-v3 §4.4 and §4.5.**
  - Add the VLM parity receipt.
  - **This also affects the text ladder.** M5's R1 arm is Qwen3.5-2B frozen
    (§3.3, §4.5). Every card that inspected the Qwen3.5 family found hybrid
    GatedDeltaNet layers (0.8B in qev and PlayJev, 4B in cua-s1; 2B presumed,
    Hypothesis). §4.4 acceptance runs only MiniLM and Qwen3-1.7B, both
    standard attention, so the GPU can pass acceptance while R1 still hits an
    unverified FLA Triton kernel or the slow torch fallback.
    - Add a Qwen3.5 linear-attention parity check to §4.4: the FLA kernel vs
      the torch reference, forward and backward. PlayJev's
      `check_linear_attention_kernels` (tolerance 5e-2) is the template.
    - Until it passes, the R1 prefill assumption (3,000 tok/s [H]) is
      unbacked for that family.
  - Add a row for M-R1/M-R2 on 2B and an optional M-R4 on 2B, within the
    16 GB cap.
  - Record that the candidate image's torch 2.12 rules out recipes pinned to
    torch 2.14.

### 9.5 Decisions for the maintainer

1. Run a multimodal pilot in 0.8.0? It would be M-R1/M-R2 on one public image
   task plus one code-rendered task, with F1–F5, after the M2 lock. The
   alternative is to ship the M-ladder labeled "untested".
2. Raise the 16 GB container cap for a 4B VLM or Qwen2-Audio-7B M-R4, or keep
   audio at M-R2.
3. One backbone or two? Qwen3.5-2B could serve both the text R1 and M-R1:
   one weight set and one parity receipt, but it carries the hybrid-kernel
   risk and rules out shared-prefix packing. The alternative is the current
   split: Qwen3.5-2B for text, Qwen3-VL-2B for media. This file states the
   trade and does not decide it.
4. Treat Jev as an evaluation comparator for multimodal work? It is
   text-only, so it can only be compared on serialized inputs, which the
   evidence says is a strawman (base64 at chance). Counsel question 2 is
   still open.

## 10. Not covered

- Any run, weight download or third-party code execution. Every recipe number
  is Reported.
- Full papers: arXiv items were read at abstract level. The Visual Jev paper
  (2609.25845) was not fetched.
- Code bodies not read by the cards:
  - circuit: text `grid.py`, `parallel.py`.
  - PlayJev: nine teachers, `mixdata.py`.
  - alpha-sys-1: environment adapters.
  - Visual Jev: `dataset.py`, `predict.py`.
  - cua-s1: `nano.py`, the composition of `crossdataset_hard_v2`.
  - Jev-Vision: `packing.py`, the OS-Atlas and Mind2Web builders.
  - qev: `data.py`, `inference.py`.
- Unmerged sibling lanes: `tmp/sweep-synth` (text sweep) and `tmp/hf-hub`.
  The web lane's own not-covered list stands: Dohnuts `data-and-evaluation.md`,
  Valen per-record provenance, Jev-Omni question sources, PlayJev
  `docs/BASELINES.md`, and the OmniEvaluator repo.
- Resolution of the typed-decisions teacher, GUI-360's agent provider, and
  the Laya base's training data.
- Whether transformers in `vllm-openai-rocm:v0.29.0` loads Qwen3-VL-2B. Any
  gfx1151 PyTorch measurement.
- Terms of every hosted provider named in §4, other than TypeSafe.
