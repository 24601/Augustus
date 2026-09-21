# Agent self-assessment with Jev

Pattern class: use Jev as the agent's own supervisor — a narrow, fast loop
watching the wide generative loop. Launch-week implementations converged on
the same lifecycle; the numbers below are their measured recipes (dated
2026-09-16/18, jev-1.13.0). Re-verify against repos in the archive before
relying: foreman, pi-jev, pi-warden, winnow, fast-jev-compaction, jev-judgment.

## Lifecycle gates

1. **Pre-action gate** (before any irreversible call). One request, all in
   parallel, thresholded in code: `destructive` (noul, hold ≥0.90),
   `exfiltrates_secrets` (≥0.70), `beyond_request_scope` (≥0.85),
   `impact_if_unwanted` (Score 4 levels, escalate ≥2.5). Ship shadow mode
   first; enforce only after observing real traffic. Productized pre-exec
   cousin: [toolgate](https://github.com/fdemir/toolgate) — `allow` /
   `block` / `review` before execution; guard error/timeout **stops**.
   Jev is not authorization. 72-case synthetic, not independently
   annotated. Distinct from the ndolinschi *vocabulary* (allow /
   ask_human / deny) below (`notes.md` §55).
   **Capability kernel, different trust model (2026-09-18 ~19:48):**
   [interlock](https://github.com/somoore/interlock) — secrets never
   enter the agent; closed action space; Jev is SENSOR; `policy.py`
   decides BLOCK/ASK/ALLOW. Do not merge with toolgate. Type-safe ≠
   correct (`notes.md` §59).
   **Human-confirmed cousin:**
   [port-cleanup](https://github.com/epiphany-dynamics/port-cleanup)
   — Jev recommends; human is the only kill trigger; identity
   re-check; shields override; mapped explanations (`notes.md` §59).
   **OMP prompt suppression (permission vs probability,
   2026-09-18 ~22:38):**
   [omp-greenlight](https://github.com/SemetricLabs/omp-greenlight)
   — auto-approve is a criterion the **operator** owns; Jev
   is not a grant. Not a sandbox (`notes.md` §62).
   **Effect-based shell pre-gate (2026-09-18 ~23:40):**
   [construct-auto-classifier](https://github.com/godspede/construct-auto-classifier)
   — fast-allow/deny then Jev Choice + independent risk
   Nouls. Privilege ≠ verdict. Fail-closed on missing /
   low-conf / high-risk. Jev 0 dangerous / 975 *theirs*.
   Distinct from toolgate / greenlight / interlock
   (`notes.md` §63). Landed-script trust / headless ≠
   auto-approve (`notes.md` §68).
   **Runtime authorize — evidence ≠ authority
   (2026-09-19 ~00:39):**
   [actiongate-jev](https://github.com/omkarghugarkar007/actiongate-jev)
   — Jev supplies evidence; code owns ALLOW/REVIEW/BLOCK.
   Positive score never overrides a deterministic security
   failure. Fail-closed on financial/destructive/credential
   if Jev is down (`notes.md` §64).
   **Persist constraints across compaction (2026-09-19
   ~05:46):**
   [pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)
   — conversational policy as structured state; replayed
   after compaction without calling Jev again. Jev
   classifies KEEP/LIFT/…; **never writes policy**.
   Side-effecting calls checked before they run. Fail-open.
   Shadow default. *Theirs:* recall 98.5% / false block
   0.0% / $0.000058. Distinct from actiongate (RBAC/schema)
   (`notes.md` §70).
   **jev-use PreToolUse gate (2026-09-19 ~06:43):**
   [jev-use](https://github.com/shitianfang/jev-use)
   — deny/ask; **fail-open**; 12/12 *theirs*; Vercel
   reconstructs confidence as margin (default 0.4). Gate
   never grants (`notes.md` §71).
   **Pi control-plane gates (2026-09-19 ~06:43):**
   [pi-jev-control](https://github.com/goodruizhan/pi-jev-control)
   — deterministic fast-path then Jev; GUI < threshold
   → unknown, never force-click. License null
   (`notes.md` §71).
   **Turnstile clone (2026-09-19 ~01:47):**
   [turnstile](https://github.com/zyphr-labs/turnstile) —
   policy first; Jev remainder; receipts + replay; missing
   Jev → Review. Experimental alpha. Same doctrine as
   actiongate (`notes.md` §66).
   **Never-confidently-wrong consensus (2026-09-19
   ~02:38):**
   [jev-labs](https://github.com/copyleftdev/jev-labs)
   — TLA+ protocol; Jev oracle; escalate when unstable.
   1,080 golden 0 wrong *theirs*; not a proof of zero
   (`notes.md` §67).
   **Advance/coverage (2026-09-19 ~02:38):**
   [seal](https://github.com/Reasonofmoon/seal)
   — generation fills Candidates; only a Seal advances;
   coverage.path visible; mint ≠ product brain
   (`notes.md` §67).
   **Email / ticket leftover cascade (2026-09-18 ~20:43):**
   [jav-email-cascade](https://github.com/skiingfalcon/jav-email-cascade)
   — typed decide, policy auto/review/llm, generator only on
   leftover text. Noul 0.5 never rounded into auto. Distinct
   from dual-process-ai (routing unmeasured). `notes.md` §60.
   **Closed-vote / host-owned CU (2026-09-18 ~21:39):**
   [JevOnly](https://github.com/buluoray/JevOnly) — no planner
   LLM; code builds options; Jev only picks. [waymode](https://github.com/mossburgh/waymode)
   — host retains handlers/permissions; Jev over live typed
   actions; `completed` ≠ server-state success. `notes.md` §61.
2. **Post-action output judge** (after the tool result exists, not before):
   `leaks_secret` (noul ≥0.90) and `failure_class` (Choice ~6 options).
   The gate sees intent; only the output judge sees what the command printed.
3. **Done-check on the final reply**: "done" claimed after code changes
   with no test/build/lint result → block. Structure first: whether a
   test/build/lint result exists in the trace is countable, so code
   answers it — one Noul only for the semantic remainder ("does this
   reply claim the work is finished?"), one threshold. Spending the model
   on the countable half is the `/bin/ls`-as-first-tier pattern
   (`mappings.md` §18). Claim/evidence cousin
   ([clear-head](https://github.com/VladyslavHontar/clear-head),
   ~16:48): check factual claims against **what was actually read this
   session**; keyword retriever, not semantic; below `JEV_FIRM` 0.6
   never blocks; true-but-unread still flags unsupported
   (`notes.md` §51). Anti-hallucinated-done, not a test runner.
   **Attention-filter Stop (never blocks the agent;
   2026-09-18 ~23:40):**
   [jev-lens](https://github.com/rashedInt32/jev-lens) —
   calibrated “do I need to look?” in the background; the
   Stop hook returns at once. Never edits files; never says
   green unless sure. **Hunch:** VOI for human review, not a
   permission gate. Distinct from jev-gates (stops writes)
   (`notes.md` §63). Distinct from
   [dizk/jev-lens](https://github.com/dizk/jev-lens)
   (pre-send views; 79% fewer tokens *theirs*) and from
   [jev-preflight](https://github.com/muse0509/jev-preflight)
   (agent attention redirect; fail-open; not a merge
   blocker) (`notes.md` §68).
   Computer-use cousin of the same honesty:
   [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
   — loop `DONE` is termination, not verified success; apps inspect
   the actual result (`notes.md` §52).
4. **Stuck-detector**: three failures with the same strategy → ask for a
   new hypothesis, not another retry. **Silence is not safer:** a draft
   gate that treats a missing Jev answer as "don't send" holds forever.
   Missing verdict needs a fail-open / heartbeat — not a block and not a
   pass. Contrast Abide `<0.5` silence (the *edit proceeds*). Showcase
   class pattern on [jevable.com](https://jevable.com/) (`notes.md` §56).
   **Stuck ladder cousin (2026-09-19 ~05:46):**
   [jeffrey](https://github.com/thomasbrueggemann/jeffrey) — withhold
   the looping tool, re-ask Jev (2 Jev calls / 0 steps per recovery).
   Jev owns stuck/progress/done; LLM only fills args. `notes.md` §70.
5. **Supervision during long runs** (foreman): separate concurrent loop
   estimates `meaningful_progress`, `implementation_complete`,
   `tests_sufficient`, `worker_stuck`, `work_off_track`,
   `ready_to_finish`; deterministic policy with hysteresis (retry counts,
   verification history) gates continue/stop/retry/verify. The model never
   commands; it estimates named probabilities. Same split as
   [jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab):
   **S1 keeps control**; optional S2 is one-use advice on low confidence
   and does not fly the drone (`notes.md` §46). **Delta (`notes.md`
   §80):** escalate-under-threshold **without stalling**; purple
   confidence = that Jev decision **consumed** returned S2 (purple
   S2 bar = arrival; red = fail); Local controller is rule-based
   **≠** githubnext/localjev; 20% starting gate still soft; no
   pixels to either provider; seed = geometry not async replay.
   Experimental viz, not a production supervisor. Computer-use speed layer of the same split:
   [solari-reflex](https://github.com/hitakshiA/solari-reflex) — one
   structured observation → one typed decision → one verified action;
   **no screenshots**; model output never becomes a selector. Harbor-style
   task score (Stripe API / answer key). Author table vs Codex on Solari:
   60.2 s vs 194.9 s; 66 s vs 460 s; 24.2 s vs 98.4 s (`notes.md` §48).
   Encoder backend of the same hole:
   [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
   — local GLiNER2 scores observed controls; `DONE` ≠ verified success
   (`notes.md` §52).
   Specialist-form cousin, **not TypeSafe Jev:**
   [Cua-S1](https://github.com/trycua/cua/tree/main/libs/cua-s1) —
   option-attention among observed elements; plan ≠ execute; dry-run
   default; source-only (`notes.md` §54).
   Harness cousin (draft stack):
   [Stagehand #2955](https://github.com/browserbase/stagehand/pull/2955)
   — pick-and-copy extract + act tree; LLM fallback; pick ≠
   replacement (`notes.md` §57).
   OCR+AX desktop product (hosted Jev; MIT **427★**):
   [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
   — never ships a screenshot for the *decision*;
   overlapping options = doubt; `done` ≠ verified
   success; 0.4 / 0.5 still soft (`notes.md` §81).
   ASR voice-browser product (hosted Jev; MIT **103★**):
   [jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
   — never ships a waveform; partial-speech wait;
   spoken confirm ≠ auth; numbered overlay, no second
   model (`notes.md` §82).
   Wrap-as-execution product (MIT **2★**):
   [AgentGhost](https://github.com/reddpy/AgentGhost)
   — ALLOW/ASK/DENY *is* the tool function; rules
   first; ASK throws; fail-closed; judge swappable
   (`notes.md` §83). **≠** actiongate **≠** toolgate
   **≠** jev-use. rh-guard owns the gate cousin.
   External pedagogy (not a product):
   [@akshay_pachaar](https://x.com/akshay_pachaar/status/2101037514945597645)
   — LLM hammer; schema-safe ≠ correct; shadow
   first; 200×/400× TypeSafe ceiling (`notes.md`
   §85). **≠** official docs **≠** Flavio.
   Institutional HF ZS pedagogy (not a product):
   [@mervenoyann](https://x.com/mervenoyann/status/2101463303734067592)
   — Jev vs GPT-5.6 bakeoffs are a category error;
   it was a skill issue; opt for DeBERTa and
   ModernBERT ones; softmax/ZS scores still ≠
   calibrated Noul (`notes.md` §112). **≠** Akshay
   §85. Quote *theirs*. Do not invent accuracy.
   Meaning-grep is **not** a self-supervision gate:
   [jev-semgrep](https://github.com/uehaj/jev-semgrep)
   ranks lines; rh-guard skip (`notes.md` §86).
   Decision-as-assert is **not** a merge seal:
   [jevtest](https://github.com/realZachi/jevtest)
   ambiguous band fails both; 0.85 still soft
   (`notes.md` §87).
   Hybrid S1 (hard safety first):
   [anima3](https://github.com/hulryung-uo/anima3)
   closed verb menu; Qwen logprob; jeff confidently
   flat on magnitude; a11y tree (`notes.md` §87).
   Empty findings is **not** a self-supervision pass:
   [stanley-code](https://github.com/devagrawal09/stanley-code)
   `notChecked` first-class; no `pass`/`approved`;
   agent fallback unverified; human promote only
   (`notes.md` §88).
   Shadow then honor (not a merge seal):
   [apa-agent-harness](https://github.com/AiPersonacademy/apa-agent-harness)
   0.85 still soft; “mathematically fulfilled”
   overclaim; **≠** AntonioCoppe/jev-harness
   (`notes.md` §89).
   Observe→score→act namesake (not a merge seal):
   [ZHUBoer/ego-jev](https://github.com/ZHUBoer/ego-jev)
   reserved `__none__`; runWorkflow completed ≠
   success; no universal cutoff (`notes.md` §90).
   Pause-if-no-Jev (S1 decide / S2 plan):
   [ORIGIN-CIVILIZATION](https://github.com/JacquesGariepy/ORIGIN-CIVILIZATION)
   ORIGIN pause-if-no-Jev; validResponse sums-to-1;
   **≠** Essentiel-Jev (`notes.md` §90).
   Local AUTO_ACT is **not** a self-supervision Noul:
   [jevbrain](https://github.com/Synxneuos/jevbrain)
   jevbrain AUTO_ACT is not a Noul (`notes.md` §90).
   Judge harness as control API (not a merge seal):
   [judgekit](https://github.com/lexingtonhibiki/judgekit)
   judgekit YAML classify/score/route/verify
   (`notes.md` §91).
   Arena never acts (instrument under glass):
   [jev-calibration-arena](https://github.com/pmcclelland/jev-calibration-arena)
   jev-calibration-arena never acts (`notes.md` §91).
   Soft-score vs hard-argmax (rh-guard cousin):
   [typed-gate](https://github.com/harshpuri84/typed-gate)
   typed-gate band [0.40,0.60] is refusal
   (`notes.md` §91).
   Fail-closed binary checker:
   [pi-jev-gate](https://github.com/fivethirty/pi-jev-gate)
   pi-jev-gate fail-closed; choice is the verdict
   (`notes.md` §91).
   Self-hosted econ / Confirm-before-act (placement):
   Foq ~25ms/2.2GB local; pastepilot Confirm before act;
   typesafe_agent_gates 27/27 / 31/31; dsh-jev can only gate;
   ha-conversation-jev Jev→Grok (`notes.md` §92).
   Decision-ledger HIT is not a self-check:
   [hyperspaceai/jevcache](https://github.com/hyperspaceai/jevcache)
   Cache hit ≠ correctness (`notes.md` §93).
   Production capture still needs a human accept:
   [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align)
   human labels only; score never auto-accepts;
   production capture flywheel (`notes.md` §93).
   Compile-time guidance is not a self-check:
   [byenzyme/enzyme](https://github.com/byenzyme/enzyme)
   guidance ≠ hook; hosted bootstrap ≠ silent
   TypeSafe (`notes.md` §94).
   Unofficial local p is not TypeSafe calibration:
   unofficial ≠ TypeSafe; LFM default ≠ ModernBERT
   backend (`notes.md` §94).
   Nemotron interface is not a calibrated replacement:
   Nemotron ≠ TypeSafe Jev; not a calibrated
   replacement (`notes.md` §94).
   Soft judgment integrity (shadow / calibrator / fail-open):
   jevguard calibrator/cache/escape; jev-ci-selector CI
   shadow mode; one-dollar-tahoe TypeSafe Jev defense eval
   (`notes.md` §95). rh-guard owns the gate cousins.
   Closed-vote extreme (no planner LLM):
   [JevOnly](https://github.com/buluoray/JevOnly) (`notes.md` §61).
   Host-owned product:
   [waymode](https://github.com/mossburgh/waymode) (`notes.md` §61).
   Productized Kahneman cascade for *any* cheap-decide / expensive-write
   loop (business/life, not only SWE):
   [dual-process-ai](https://github.com/taro1985/dual-process-ai) —
   `conf ≥ τ` S1 decides else S2 generates; routing fails open; safety
   fails closed; **routing accuracy not measured**; keyword fallback is
   not S1 (`notes.md` §49). Tune τ on your escalation log.
   **Distinguish names:** the existing "foreman" *shape* here is the
   Kevthetech143/super-jev loop (named probabilities → hysteresis
   table). [`reification-labs/foreman`](https://github.com/reification-labs/foreman)
   (~16:48) is a **description-only** Elixir/Phoenix scaffold claiming
   parallel S1 specialists + one S2 coordinator with typed
   `{value, probability}` — README is stock Phoenix; `mix.exs` has no
   Jev dep. Do not invent an Elixir API (`notes.md` §51).
   Bounded Pi supervisor of the same lifecycle:
   [jevons](https://github.com/LilDojd/jevons) — not a second agent;
   default recovery **shadow**; steering never generates commands.
   Distinguish from pi-jev-approver (fail-closed remainder) and
   pi-jev-context (sieve).
   **OMP/pi fail-open cousins (2026-09-18 ~21:39):**
   [omp-jev-extensions](https://github.com/luw2007/omp-jev-extensions)
   — `jev_acceptance_gate` before done; `jev_route` topology/tier.
   Missing Jev **fails open** (`confidence: 0`). Contrast
   pi-jev-approver fail-closed without a key (`notes.md` §61).
   **OMP prompt suppression (2026-09-18 ~22:38):**
   [omp-greenlight](https://github.com/SemetricLabs/omp-greenlight)
   — grades gated calls; suppresses the prompt when Jev says
   allow. Operator owns the bar; plugin never self-tunes.
   Default 40.9% / 0 of 94 *theirs*. Not a sandbox. Host deny
   fires first (`notes.md` §62).
   **Skill pack grant (outline only):**
   [skill-broker](https://github.com/adamjralph/skill-broker)
   — Jev scores relevance; code owns grants; never broaden
   access. Not a production recipe (`notes.md` §62).
6. **Context economy**: the context-sieve card
   (`references/applied-mappings.md#1-context-sieve`). Judge every large
   tool result with one relevance Noul before it enters context. Hide
   confident-no blocks behind a stub + recall key; always keep current
   instruction, recent turns, errors, and opaque blocks. [kevinpita/winnow](https://github.com/kevinpita/winnow) hides at
  relevance ≤0.22 (agent context sieve; distinct from [ThinkyMiner/Winnow](https://github.com/ThinkyMiner/Winnow) worth-your-attention VOI, `notes.md` §69); fast-jev-compaction asks two nouls per tool call
  (should the call stay knowing it was made? should the result stay
  verbatim?). Encoder-backend cousin:
  [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
  — GLiNER2.5 retention Choice + exact character-offset copies; mutating
  tools stay `keep_full`; low-confidence fails closed to `keep_full`;
  `shadowMode` default true. Not a summarizer. Not Jev (`notes.md` §50).
  **≠**
  [gliner-native-runtime](https://github.com/shershah1024/gliner-native-runtime)
  — schema→spans locate, not compaction keep/drop of
  held bytes (`notes.md` §97).
  Stdout-prune cousin, same family, different job:
  [jev-pruner](https://github.com/tamaratran/jev-pruner) — Jev Noul on
  Bash chunks after a hard envelope; fail-safe original; archive
  (`notes.md` §53). Marketplace id still `fast-jev-output`.
  OpenCode host-port:
  [indiejoseph/opencode-jev-pruner](https://github.com/indiejoseph/opencode-jev-pruner)
  — `tool.execute.after` on `bash`; jev-zen / jev-1.13-free;
  zen-chat ≠ Noul; hook fail-open (`notes.md` §96).
  **Decision Graph Protocol envelope:**
  [dgp](https://github.com/numerous-com/dgp) —
  Decision Graph Protocol frame→assess→commit.
  app retains permissions/effects.
  Jev-first assessor-neutral.
  guarded commit / receipt/next frame.
  assessment batching.
  Commit fail-closed in the application; assessment
  is a sensor. hard-gating DGP as safety theater.
  numerous-com/dgp ≠ TypeSafe official
  (`notes.md` §98).
  **Cost-derived / typed-callback overlays:**
  [gut](https://github.com/Kungie/gut) —
  YES / NO / UNSURE from costs; default
  `on_unsure="raise"` is app policy, not a
  System One hard gate; auto-batching
  same-object questions.
  [judge](https://github.com/Illusion47586/judge)
  — exactly one app-owned callback; explicit
  uncertain branch (`notes.md` §99).
  **Language primitive:**
  [probably](https://github.com/southpolesteve/probably) —
  Jev IS the if-statement; otherwise maybe / confidence
  gate; chaos samples after the gate (`notes.md` §100).
  **2041:** fail polarity per lens (jevusher ADMISSION
  unsure→let in / SELECTION unsure→surface none / SAFETY
  unsure→flag never pass); planalyzer code-owned
  pass|review|block; Fabric receipt ≠ authorization;
  jev-evaluation confidence does not track ignorance —
  do not hard-gate ≥0.95 (`notes.md` §101).
  **2145:** jevq warn never a merge seal; static lint ≠
  measured separation; IC-Laya model output never grants
  Tx; parity_verified stays false; jev-kit exit 0 ≠ claim
  truth; WaynezProg/jev-kit ≠ jonathanavis96/jev-kit
  (Airlock); ember prior injection crowds out evidence;
  comparative framing is the usable judgment
  (`notes.md` §102).
  **2246:** catalog `reported` never becomes `reproduced`;
  19 reviewed records; scores not one leaderboard; TokenTrim no-Jev matched
  hybrid 62.4%; constructed scenes are not production
  logs; Hub OWNER not published; confidence =
  1−normalized entropy, not P(correct); ChatJev-style
  soundness theater — Jev classifier as autoregressive
  next-token predictor; do not launder Noul as proof;
  timeout = censoring; independent questions can
  conflict; ranking ≠ calibration / 0.5 still soft;
  fail-open failed evals not marked seen
  (`notes.md` §103).
  **2340:** description-only stub / size 5 never a checkpoint;
  ESCI hard probe fails four of six; jev_bool ECE 0.242 inversion 0.255;
  do not re-fold §60 six-gates as new; Jairik/jev-distiller size 1;
  distill-Jev UI stub / do not distill Jev as teacher of record;
  Jev self-scores then human curation; simple-jev not TypeSafe;
  same label can still change the branch; not tested with a live Jev API key;
  constrained logprob + temp/Platt ≠ Noul; OpenJevPro pastes openjev-sglang JevBench as own;
  demo P(True) 0.5052 / Choice conf 0.2872 / Score conf 0.0055;
  do not paste listed radar numbers; do not quote 0.916 as a class ceiling
  (`notes.md` §104).
  **0145:** description-only stub / size 0 never a checkpoint;
  do not reopen or amend PR #23; Colvin0315/MiniSystemOne ≠ hyusi2003/MiniSystemOne;
  no published weights download URL; 90.5 seconds / 29.2% pipeline evidence;
  JSON parse of generated text ≠ Noul; TypefAI JEV / Journal Entry Voucher;
  46x speedup / accuracy identical is not Jev identity; ECE 0.624 sentiment catastrophe;
  do not quote 91.1% / 92.58% / 84.8 as class ceilings;
  classifier.dev fast tier 84.8 is Jev behind its own API;
  do not re-fold §78 v1.2 board as new; hard budget filter before Jev;
  Jev never asked to perform budget arithmetic;
  Jev judges the next state, XState enforces transitions;
  simulation uses synthetic keyword fixtures;
  curation is not endorsement; ★339 live REST is not eval;
  query-side encoders, not a Jev replica;
  transformers.js AutoModel cannot load this graph;
  This Space contains no benchmark result yet
  (`notes.md` §106).
  **0243:** do not reopen or amend PR #23 or #24;
  cheap alone is not success; Jev does not write, sum prices, or claim accuracy %;
  62.3% cost save / 4.5pp miss of 2pp non-inferiority; p50 latency worse than Sol due to routing overhead;
  previous_ticket_count >= 3 is code; MIN_CONFIDENCE 0.6 still soft; substring false positives;
  aesaganda/jev-ticket-router ≠ SarathChandraBellam/jev-vs-llm-ticket-router;
  confidence ≥ 0.85 hard-gate is theater; generative AI banned from scientific plots;
  Praveenrajus/jev-bench ≠ fstandhartinger/jevbench;
  Hub does not ship weights; 100/100 easy T/F is not Harbor; label_mass ≠ correctness;
  stock llama.cpp Q2_0 silently gibberish; NicolaiMTLassen/open-bonzi-jev ≠ NicolaiLassen;
  temperature 1.05; AutoModel from_pretrained works;
  onnx-community/open-jev-deberta-v3-large-ONNX ≠ system-one-qwen3.5-4b-scorer-ONNX;
  107★ densify; GH 151M vs README 149.6M; PR #1 now closed unmerged;
  do not re-fold §71 claim-audit as a beat;
  structured ≠ correct; mock not live API; 26 tests;
  wjdjdakf17/jev-study ≠ baekenough/jev-study
  (`notes.md` §107).
  **0345:** do not reopen or amend PR #23 or #24 or #25;
  bonzi-27b-v2 / ternary-8b / 27b-v1 GGUF family densify;
  WANLI-256 74.6% / 65.2% / 71.1% *theirs*;
  Bonsai 1 27B Q1_0 runs on stock llama.cpp;
  ternary still needs PrismML fork;
  hf:heman10x/openJev-verdict-2.0 twin tokenizer-only;
  OpenJev Vision image classification + uncertainty;
  CLEVR-4 held-out joint 0%;
  hfdataset:IamBusy/OpenJev-Vision-Research-v0.1 12,832;
  294,912 derived targets not independent samples;
  Laya multilingual ONNX WebGPU typed-decisions port;
  63/63 selected answers / 5.1e-4 CPU / 1.2e-2 WebGPU;
  UpHash-Network/mini-jev is yuki-oshio transfer;
  jev-injection-bench 11,900 labelled prompts;
  Jev best ranking / Haiku better ECE 0.021 vs 0.058;
  0.5–0.9 band is where Jev's numbers do not mean what they say;
  Prompt wording moves panic 28%;
  manojlds/jev-dspy-bench ≠ dspachos/jev-dspy ≠ jmanhype/jev-dspy-lab;
  Jev agreement is similarity, never ground truth;
  no aggregate quality grade or merge gate;
  AbstentionBench-on-Jev rank 1 of 20 vs 2025 field;
  question-asymmetry;
  forward-looking 0.465 never extreme;
  openkev calibration layer not a runtime;
  ECE vs coverage independent;
  select_threshold returns inf;
  escalation catches uncertainty not ignorance;
  misakaikato/openkev ≠ jaredpalmer/kev;
  pdf-race Docling→Jev vs Gemini;
  parser owns the wall clock;
  12/12 tie is a tie;
  titles selected not generated;
  flopcheck 16 calibrated tweet judgments;
  mechanical tells in code;
  ZeroX-01/jev-atlas ≠ Zaious/jev-capability-atlas ≠ gorock007/jev-atlas;
  Laya calibration lab Gradio MCP;
  T never changes argmax;
  confidence ≠ top-label p;
  easy probe set refused;
  40–48 rows too small to ship T
  (`notes.md` §108).
  **0439 HIGH:** Gemma-4 26B-A4B jevify classification+calibration;
  LoRA adapter twin not independent eval; Gemma-4 E4B jevify;
  E4B LoRA stub card; Hub jevify merged LoRA ships weights;
  PAWS 0.580/ece 0.288 is the weak cell;
  kushalpatil/jevify-gemma4 ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify;
  GH kushalpatil07/jevify 404;
  bonzi Bonsai-8B v1 GGUF densify; Bonsai-1.7B v1; Bonsai-4B v1;
  WANLI-256 64.5% / 60.2% / 52.0% *theirs*; rank #4 / #5 / #6 of 6;
  JulesHuisman/jev-eval scaffolding / README SHA c356a584 (was empty e69de29b);
  7 bands 6/10 vs 40 bands 0/10;
  source receipts + confidence slider re-policy without re-inference;
  32/32 synthetic is smoke not production;
  roadus2 watch misspelling; lock roadius2/ultra_laya;
  ultra_laya REVIEW defects;
  XNLI EN 88.3% ECE 0.032 → RU 77.3% ECE 0.096;
  Δ −11.0 pp [−14.2,−7.8]; ECE +0.063;
  MASSIVE no detectable difference at n=600;
  confidence is function of p_max (r=1.000);
  pointer-not-generator 400 human-authored responses;
  proposed ≠ authorized;
  FewRel 160: Jev 85.0% vs lexical 13.125%;
  gated 100% (95/95) coverage 59.375%;
  J++ composable semantic computation language;
  judge-jev 0.5 still soft;
  947 repos scored; A 273 / B 302 / C 372;
  LLM rubric ≠ benches;
  No benchmark winner is claimed;
  git-confess code owns counting/blame/ratio;
  httpx exhibit 11% (13/119) *theirs*;
  90d trend +12.40% vs random +12.75% vs BH +41.71%;
  5m win rate 25%;
  Awesomejev 656 entries / 38,160 stars;
  tracker likes 64 (+4) lastModified UNCHANGED;
  Laya present; Blackwood ABSENT; Archer still promised_not_landed
  (`notes.md` §109).
  **0541 HIGH:** Blackwood tracker ABSENT; likes 2 gated manual;
  r = c - p_a; ECE 0.021; acc 0.807 vs warmup 0.746;
  Independent primitive;
  11.57s vs 54.10s · 4.67× · 120/128 *theirs*;
  default path is pretrained Gemma probs not trained RLCD head;
  GH Meanblock 404; lock leesk212/JEV-CPU;
  softmax over letter slots ≠ Noul;
  WANLI 0.741 vs openjev v2 0.77 *theirs*; 3-way NLI ≠ Noul;
  priority 0.464 = majority floor; banking77 contaminated;
  raw margins not probabilities;
  do not distill Jev as teacher of record (they distilled Haiku);
  “0.9 is not one number”; ranking ≠ calibration;
  banking77 0.8–0.9 stated 0.86 actual 0.73 over-confident *theirs*;
  $0.0000153–$0.0000226 vs circulating $0.0004 (~20×);
  Score is 0..n-1 expectation not 0–1; Noul has no confidence field;
  TCP floor 198.8 ms;
  type reliability is not a reason to choose Jev (json_schema 5/5);
  Function-only 5/8 vs hybrid 8/8; 4/8 without Jev;
  8 designed cases not conversion lift;
  200-row pilot Jev 86.5% 173/200 vs Gemini Flash-Lite 86.0% 172/200 vs Pro 87.0% 174/200 *theirs*;
  not a ranking; 情緒測謊器;
  8-example Jev vs GPT-5.6 Sol ~64× cost 5.4× latency *theirs*;
  synthetic; no inference; ≠ JevBench v1.2 §78;
  Judged 3317 / listed 2560; Jev judges, code applies policy;
  catalog ≠ endorsement;
  APA “microsecond policy / zero hallucination” overclaim;
  Client-side quiz; pointer from held docs; scanned-PDF warn;
  Jev judges / agent reasons / user decides;
  selecting an option is not permission to implement;
  pattern exact, judgement must clear floor;
  no matching pattern → no model call; not a correctness oracle;
  Spec vs artifact remainder;
  treating 0.85 as 85% / minProbability hard-gate as Harbor;
  VERIFY acquires discriminating evidence, never same-pool confidence-only rescoring;
  fast/full/max are ceilings not sizes;
  Solar writes, Jev chooses NEXT ACTION;
  tracker likes 64 flat, lastModified UNCHANGED;
  Laya likes 802 (was 783); Blackwood tracker ABSENT;
  Archer still promised_not_landed
  (`notes.md` §110).



  **0743 HIGH:** Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0;
  TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%;
  abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%;
  0.85 coverage 84.60% selective risk 1.18%;
  26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled;
  Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084;
  reliability 0.007 but resolution 0.000;
  27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624;
  22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f;
  Student B MAE 0.148 / Pearson 0.836 / 86.0%;
  pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2;
  HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000;
  2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated;
  E2 recomputes from saved probabilities; Space sha eda59e0a;
  MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T;
  T never changes argmax;
  siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode;
  Split Transformers experiment from llama.cpp runtime;
  tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab;
  Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling;
  second pass must be $0.00 from cache; The pages never call Jev;
  Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%;
  restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask;
  They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%;
  ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench;
  ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome;
  confidence is descriptive provider output, not a substitute for probability;
  Quality denominators include only valid scored answers;
  an exact halfway tie chooses the lower level;
  aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills;
  The local path does not claim to turn a smaller checkpoint into Jev;
  Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm;
  结构兼容，不是 Jev 模型能力;
  altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify;
  Find where Jev belongs. Design the questions. Measure the difference
  (`notes.md` §113).

Hourly 0743 uniqueness lock: Heman10x-NGU/Verdict-open-jev ≠ Heman10x-NGU/openJev-verdict-2.0; TF-IDF + LogReg ECE 0.0207 vs Jev 0.1440; Verdict-open-jev 48.07% vs Jev 90.80%; abstention combined recall 10.00%; p50 35.58 ms; K=25 (maximum capacity) 72.00%; 0.85 coverage 84.60% selective risk 1.18%; 26.1× faster than standard Qwen JSON generation; Jevify 90.0% / 167 ms CUDA graphs disabled; Finding 1: Brier on stated confidence alone is a trap; grpo_rlcr 0.78 / ECE 0.084; reliability 0.007 but resolution 0.000; 27 900 schema-driven decisions; 13 600 / 13 600 questions; candidate mass min 0.99999624; 22 configs · 166,054 rows · 4 calibration-gold; sha a39eba3f; Student B MAE 0.148 / Pearson 0.836 / 86.0%; pngwn/open-jev-laya-bench README 404; sha 9f69c742 likes 2; HDFS 0.9933 (745/750) / retain 0.0084; BGL ERROR/FATAL protection 1.0000; 2,479 / 2,500 HDFS uncertain; cache hit 0.9648 (2412/2500); $0.153936 estimated; E2 recomputes from saved probabilities; Space sha eda59e0a; MASSIVE English 0.783 / Khmer 0.033 / Hindi 0.133; 40–48 rows too small to ship T; T never changes argmax; siren2345/jev-single-decode-transformers ≠ siren2345/jev-single-decode; Split Transformers experiment from llama.cpp runtime; tanayvasishtha/jev-lab ≠ dairui1/jev-lab ≠ BrendanH18/jev-lab ≠ yibie/laya-jev-lab; Four experiments stress-testing TypeSafe's Jev: calibration, bundle bias, label bias, and ensembling; second pass must be $0.00 from cache; The pages never call Jev; Gemma 4 31B 77.0% / Jev 1.13.0 61.4% / Laya 322M 0.0%; restriction state 95.0% against 84.4%; None of the systems are particularly good at knowing when to stop and ask; They skip the question and call a tool directly; 100% schema pass; six-field joint 48.8% vs 72.8%; ywchiu/jev_benchmark ≠ Running-Dolphins/jev-bench ≠ Praveenrajus/jev-bench; ACT / REVIEW / FALLBACK; A provider failure, timeout, malformed output, or missing answer is **not** a policy outcome; confidence is descriptive provider output, not a substitute for probability; Quality denominators include only valid scored answers; an exact halfway tie chooses the lower level; aiwithenoch/Jev-Skill ≠ simplosophy/jev-skill ≠ laguagu/jev-skills; The local path does not claim to turn a smaller checkpoint into Jev; Low support becomes decision: "review"; MIT-0 SPDX NOASSERTION; current-llm; 结构兼容，不是 Jev 模型能力; altryne/jevify ≠ Mintzs/jevify ≠ gulagala001/jevify ≠ uspraveen/Jevify; Find where Jev belongs. Design the questions. Measure the difference; TypeAR-AI/TypeAR 301 → TypeLLM/TypeLLM; TypeLLM/TypeLLM 16★; SemIf 2241★ (+34 vs §111 2207); jevlike 1051★ (+8 vs 1043); AnotiaWang 98★ (+1 vs 97); yibie/awesome-jev 525★ (+19 vs 506); Laya likes 864 (was 822); tracker likes 67 (+3 vs 64); lastModified UNCHANGED `2026-09-20T04:29:16.000Z`; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#32/#33; notes.md §113

  **0646 HIGH:** Calibration is not alpha; NO CURRENT ALPHA CANDIDATE;
  ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875;
  Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05;
  default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17;
  keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25;
  7.8% to 57.9%; judges results it never sees; task-finish eval not built yet;
  $0.002 per compaction;
  slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench;
  Jev 108/120 $0.083 0.34 s; Luna SGR 114/120;
  paired Jev accuracy-difference intervals include zero; not evidence of equivalence;
  GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120;
  rule-based by default, optionally Jev-backed; empty README;
  missing key cannot break the experience;
  prefill plus exactly one decode; softmax over A/B/C ≠ Noul;
  BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident;
  score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2;
  encode the state once, decide everything in parallel;
  0.740 accuracy against a 0.508 majority; ECE 0.047;
  fine-tune's advantage ends where its 384-token training data does;
  jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd;
  Space does not call Jev; recomputes routing from saved probabilities;
  200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark;
  Jev evaluations are advisory;
  YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep;
  default threshold 0.8 still soft; 40-line windows cannot prove whole function;
  token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet;
  handful of hand-written examples, not a benchmark; Jev judged exactly what it was given;
  laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills;
  contract_passed is not a claim of guaranteed factual truth;
  Wilson lower bound 0.85 floor; fixture mode no savings claim
  (`notes.md` §111).

Hourly 0646 uniqueness lock: Calibration is not alpha; NO CURRENT ALPHA CANDIDATE; ΔR² approximately +0.00084; Brier 0.2131387; ECE 0.0421875; Adding Jev probability to deterministic volatility improved Brier by only 1.4058e-05; default 0.5 keeps zero non pinned; keepResult median 0.14 to 0.17; keepCall median 0.28 to 0.35; usable range is about 0.10 to 0.25; 7.8% to 57.9%; judges results it never sees; task-finish eval not built yet; $0.002 per compaction; slavadubrov/sgr-judge-bench ≠ slavadubrov/jev-judge-bench; Jev 108/120 $0.083 0.34 s; Luna SGR 114/120; paired Jev accuracy-difference intervals include zero; not evidence of equivalence; GLM SGR 26/120 93 format failures; Terra-planned Jev hybrid 55/120; rule-based by default, optionally Jev-backed; empty README; missing key cannot break the experience; prefill plus exactly one decode; softmax over A/B/C ≠ Noul; BBQ 9,053/10,000 (90.53%); ECE 0.0890; Mean confidence 0.9943; overconfident; score and noul not implemented; DGUI 12 rows (was 6); INSTRUCT 119 rows likes 2; encode the state once, decide everything in parallel; 0.740 accuracy against a 0.508 majority; ECE 0.047; fine-tune's advantage ends where its 384-token training data does; jasonkneen/open-jev ≠ pngwn/open-jev; same sha d41dc3cd; Space does not call Jev; recomputes routing from saved probabilities; 200-case Jev 97.0% / 100.0% / 95.0% / MAE 9.22; synthetic repository benchmark; Jev evaluations are advisory; YehuiTang0316/jev-nlgrep ≠ Bentlybro/jevgrep ≠ can1357/jegrep ≠ uehaj/jev-semgrep; default threshold 0.8 still soft; 40-line windows cannot prove whole function; token-native sequential start/end Choice; Gemini/Haiku stubs not configured yet; handful of hand-written examples, not a benchmark; Jev judged exactly what it was given; laguagu/jev-skills ≠ laguagu/jev-evidence-lab ≠ Pleo2/awesome-jev-agent-skills; contract_passed is not a claim of guaranteed factual truth; Wilson lower bound 0.85 floor; fixture mode no savings claim; SemIf 2207★ (+21 vs §110 2186); jevlike 1043★ (+5 vs 1038); TypeAR 15★ (+1 vs 14); AnotiaWang 97★ (+1 vs 96); yibie/awesome-jev 506★ (+16 vs 490); Laya likes 822 (was 802); tracker likes 64 flat, lastModified UNCHANGED; do not reopen or amend PR #23/#24/#25/#26/#27/#28.

Hourly 0541 uniqueness lock: calibration beyond ~500 tokens unmeasured; GH jev-haiku-benchmarking 404; ≠ Praveenrajus/jev-bench ≠ fstandhartinger/jevbench; gateway tax not one number; ≠ RadRebelSam/awesome-jev; NLI Tetris argmax P(entail)−P(contradict); 1q 396ms / 30q 567ms; ±0.03; 33q $0.000045 vs Gemini ~5× slower ~60× cost *theirs*; ≠ realZachi/jevtest; CSP only api.typesafe.ai; degraded fallback; $0.00022 vs chat $0.00306 *theirs*; SemIf 2186★ (+20 vs §109 2166); jevlike 1038★ (+7 vs 1031); TypeAR 14★ flat; AnotiaWang 96★ (+1 vs 95); yibie/awesome-jev 490★; do not reopen or amend PR #23/#24/#25/#26/#27.
  **Lease / retrieve:**
  [invalidate](https://github.com/chopratejas/invalidate) —
  memory leases ended by new evidence; unsure → review
  queue; host keeps the store.
  [jev-recall](https://github.com/samdotmak/jev-recall) —
  retrieve by relevance not resemblance.
  **Lint / loop:**
  [jev-lint](https://github.com/mizchi/jev-lint) — name↔body
  / comment truth / test-claims; no shipped rule has
  severity error.
  [JevPi](https://github.com/direwolfiy/JevPi) — Jev-first
  Pi agent loop; slow-LLM fallback; 62 tests wiring not
  quality.
  Session-ledger cousin:
  [carryforward](https://github.com/Dharundp6/jev-carryforward) —
  verbatim JSONL; Jev scores which facts are still live; constraints
  and corrections always return; fail-open dump if the scorer is
  down. Nine entries × three tasks is a hint, not proof
  (`notes.md` §55). Eval: `recall` **0/4** — SessionStart
  hook > hoping (`notes.md` §68). Do not copy mcp add.
  Observational-memory sibling:
  [pi-observational-memory-jev](https://github.com/willfish/pi-observational-memory-jev)
  — keep/kind verbatim; model-free compact (`notes.md`
  §68).
  Pre-send cousin:
  [jev-lens](https://github.com/dizk/jev-lens) — views
  before first send; 79% fewer tokens *theirs*
  (`notes.md` §68).
  Classify-first cousin:
  [jev-sift](https://github.com/kbhuw/jev-sift) — batch path/url/text
  → Jev **before** the main agent reads; uncertain/errors/truncation
  ≠ irrelevant. Transport tests ≠ accuracy. No LICENSE this pass
  (`notes.md` §56). Do not copy plugin how-to.
  Framework-agnostic compact+gate cousin
  (2026-09-19 ~00:39; was empty skip §61):
  [jev-compactor](https://github.com/edwardyen724-g/jev-compactor)
  — Jev judges relevance; code decides structure; never rewrite;
  regex floor independent of Jev. Compaction fail-open if Jev
  down; safety fail-closed on pending destructive. OpenCode
  fail-open port already §62: fast-jev-opencode (`notes.md` §65).
  Later product-arm bench **73%** / 350 ms / 4 of 4
  (`notes.md` §68).
  WHETHER/HOW/WHAT cousin (license null; 2026-09-19
  ~04:39):
  [hermes-jev-router](https://github.com/rsdkrasen/hermes-jev-router)
  — compact original chunks; skip next main-model when
  evidence is enough (needs core patch); fail-open
  (`notes.md` §69).
  Pi summarizer-replacement cousin:
  [pi-jev-compact](https://github.com/dev-willbird1936/pi-jev-compact)
  — verbatim keep/drop of paired tool calls; fail-open to
  LLM summary if <25% saved. **≠**
  vava-nessa/pi-jev-compaction (`notes.md` §72).
  Typed baton cousin:
  [jev-handoff](https://github.com/shitianfang/jev-handoff)
  — escalate/continue/abort; gate never grants; inverted
  loop (`notes.md` §69).
  Advice-only cousin:
  [jev-decisions](https://github.com/bojansandhaus/jev-decisions)
  — 25 prepared reviews; **never stop commands**
  (`notes.md` §69).
  Adversarial-browser cousin:
  [browser-jev](https://github.com/DowLucas/browser-jev)
  — Playwright executes, Jev chooses; sample from the
  distribution (`notes.md` §69).
  Decider≠executor cousin:
  [jeffrey](https://github.com/thomasbrueggemann/jeffrey)
  — Jev→tool→Jev; LLM fills args; risk≥0.5 pause
  (`notes.md` §70).
  Persist-constraints cousin:
  [pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)
  — user constraints survive compaction; Jev never
  writes policy (`notes.md` §70).
  Plugin no-text cousin (2026-09-19 ~06:43):
  [jev-use](https://github.com/shitianfang/jev-use)
  — fail-open PreToolUse gate; Vercel margin fallback
  (`notes.md` §71).
  Pi control-plane cousin:
  [pi-jev-control](https://github.com/goodruizhan/pi-jev-control)
  — named sensors; GUI unknown never force-click
  (`notes.md` §71).

## Non-negotiable boundaries

- A Jev probability is evidence about context, never an action permit.
  Operation+target pairs are validated in code; "confidence high" does not
  authorize.
- Error paths fail **per action**. These supervision gates are advisory,
  so they fail open (missing key, timeout, 429, malformed response → no
  verdict, tool call proceeds, error reported once/minute) — and that is
  only safe because a hard interlock or sandbox sits underneath. A gate
  that *selects* or *authorizes* a side effect fails closed instead
  (`mixed-architecture.md` prefilter table; `mappings.md` §18).
  Compaction *drop* is that second kind:
  [gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction)
  fails closed to `keep_full` (`notes.md` §50). Native locate
  confidence is still a sensor, not a permit, and not
  this compaction-drop job:
  [gliner-native-runtime](https://github.com/shershah1024/gliner-native-runtime)
  (`notes.md` §97). Stdout prune is the
  same polarity:
  [jev-pruner](https://github.com/tamaratran/jev-pruner) fails closed
  to original output (`notes.md` §53). OpenCode host-port same
  polarity, hook fail-open:
  [indiejoseph/opencode-jev-pruner](https://github.com/indiejoseph/opencode-jev-pruner)
  (`notes.md` §96). Protocol envelope: commit
  fail-closed, assessment is a sensor:
  [dgp](https://github.com/numerous-com/dgp)
  Decision Graph Protocol frame→assess→commit;
  app retains permissions/effects; hard-gating DGP
  as safety theater (`notes.md` §98). Cost-derived
  overlay: default UNSURE raises so the middle band
  is refusal, not a silent `False`
  ([gut](https://github.com/Kungie/gut)); typed
  callback: invalid provider output runs **no**
  callback
  ([judge](https://github.com/Illusion47586/judge);
  `notes.md` §99). Tool *execution* is the
([judge](https://github.com/Illusion47586/judge);
  `notes.md` §99). Language-primitive cousin: omitting
  `otherwise maybe` executes **neither** branch
  ([probably](https://github.com/southpolesteve/probably);
  `notes.md` §100). Lease cousin: false invalidation is
  fail-closed; dead-band → review
  ([invalidate](https://github.com/chopratejas/invalidate)).
  Lint cousin: no shipped rule has severity error
  ([jev-lint](https://github.com/mizchi/jev-lint)). Tool *execution* is the
  other polarity: [toolgate](https://github.com/fdemir/toolgate)
  stops on block / review-without-approval / guard error
  (`notes.md` §55). Capability kernel
  ([interlock](https://github.com/somoore/interlock)) never lets
  the secret into the agent in the first place (`notes.md` §59).
  Human-confirmed kill
  ([port-cleanup](https://github.com/epiphany-dynamics/port-cleanup))
  re-checks identity before SIGTERM. Session-memory *omit* fails open (dump the
  ledger): [carryforward](https://github.com/Dharundp6/jev-carryforward).
  Draft-gate *silence* is the opposite mistake: treating no-answer as
  a hold. Missing verdict needs a heartbeat (`notes.md` §56).
- Cache identical judgments (~120s) and deduplicate sibling calls into one
  in-flight request.
- pi-warden measured cost makes continuous guarding viable: ~$0.00004 and
  ~0.3s per judgment on 17,160 guarded calls; 150 paired runs broke project
  rules 6 times with it off, 0 times on. Your numbers will differ — measure.

## Hallucination/grounding/citation checks

- Grounding of a generated claim: one Choice per claim–evidence pair
  (supports / contradicts / unrelated) + a confidence review flag; judge
  against the cited source text, never against another model's prose.
  Pointer-not-generator: the model points at line ids; code copies
  verbatim with place; *not found* is an answer
  ([choxos/jev-reviewer](https://github.com/choxos/jev-reviewer);
  systematic-review Jev Reviewer; **12★**; human tick never
  overwritten; `notes.md` §48, §74).
  Distinct: [egma-ai/jev-reviewer](https://github.com/egma-ai/jev-reviewer)
  assigns **attention** P0/P1/P2, not correctness; OpenAI writes
  deltas (`notes.md` §58).
  Compaction: point at character offsets in the tool result
  ([gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction);
  `notes.md` §50). Session-evidence Stop
  ([clear-head](https://github.com/VladyslavHontar/clear-head)): claims
  vs **what the assistant actually read**; keyword retriever; below
  firm-confidence never blocks (`notes.md` §51).
- Self-report fidelity: compare the agent's claimed action with its actual
  trace via decomposed Nouls (right tool? args match schema? result matches
  call?). Escalate on low confidence; never auto-retry.
- Rubric quality: if scores are the data type, use concrete level
  descriptions (never bare degrees or "worse than previous"), independent
  dimensions as separate Scores, and read probabilities beside every score.

## Preference lint (project rules, not taste)

When the "judge" is really "does this change violate a rule we already
wrote?", do not ask Jev whether the code is good. Load
`references/mixed-architecture.md#preference-lint-and-gates`. The transferable
contract (`doeixd/jev-pref`): the project defines the rule, Jev classifies
visible evidence, code maps the outcome, the agent acts.
[`coldteadotai/abide`](https://github.com/coldteadotai/abide) is the
fuller productized path of that contract (compile / calibrate / tune /
replay; one Score per rule on the diff; bands + fail-open). Soft
rules → soft judgment; the linter owns hard rules. Shadow-mode the
gate first; permit remains a separate axis from confidence.
`notes.md` §47. Plain-English PR-check cousin
([if-ai](https://github.com/Victor-Casado/if-ai)): one condition +
required min-confidence; fail-closed on error / empty / low
confidence. [jev-marshal](https://github.com/LightningK0ala/jev-marshal)
is Watch / empty repo this pass (`notes.md` §51).

  **0042:** displayed p never a proof; distribution >
  argmax; Noul 0.5 midpoint; score is expectation not
  integer; schema-valid ≠ calibrated; gulagala001/jevify ≠
  Mintzs/jevify; 40.3% below constant-answer; FastLoopError
  catch — do the expensive thing; second signal not sole;
  0.980 at every N is not universal determinism; 0 model
  calls at deployment — do not ship VLM+Jev as the
  runtime; cascade 0.60 matches 78% at 1.8× but
  confidence-to-accuracy is not monotonic; noul facts not
  judgements; extractors ≠ decision engines; Laya
  dict-instructions collapse 58.3%; throughput not
  intelligence; raw 0.94 is not a release; Jev never
  generates filenames; no_direct_evidence ≠ safe to merge
  (`notes.md` §105).
  **Lease / retrieve:**
  [invalidate](https://github.com/chopratejas/invalidate) —
  memory leases ended by new evidence; unsure → review
  queue; host keeps the store.
  [jev-recall](https://github.com/samdotmak/jev-recall) —
  retrieve by relevance not resemblance.
  **Lint / loop:**
  [jev-lint](https://github.com/mizchi/jev-lint) — name↔body
  / comment truth / test-claims; no shipped rule has
  severity error.
  [JevPi](https://github.com/direwolfiy/JevPi) — Jev-first
  Pi agent loop; slow-LLM fallback; 62 tests wiring not
  quality.
  Session-ledger cousin:
  [carryforward](https://github.com/Dharundp6/jev-carryforward) —
  verbatim JSONL; Jev scores which facts are still live; constraints
  and corrections always return; fail-open dump if the scorer is
  down. Nine entries × three tasks is a hint, not proof
  (`notes.md` §55). Eval: `recall` **0/4** — SessionStart
  hook > hoping (`notes.md` §68). Do not copy mcp add.
  Observational-memory sibling:
  [pi-observational-memory-jev](https://github.com/willfish/pi-observational-memory-jev)
  — keep/kind verbatim; model-free compact (`notes.md`
  §68).
  Pre-send cousin:
  [jev-lens](https://github.com/dizk/jev-lens) — views
  before first send; 79% fewer tokens *theirs*
  (`notes.md` §68).
  Classify-first cousin:
  [jev-sift](https://github.com/kbhuw/jev-sift) — batch path/url/text
  → Jev **before** the main agent reads; uncertain/errors/truncation
  ≠ irrelevant. Transport tests ≠ accuracy. No LICENSE this pass
  (`notes.md` §56). Do not copy plugin how-to.
  Framework-agnostic compact+gate cousin
  (2026-09-19 ~00:39; was empty skip §61):
  [jev-compactor](https://github.com/edwardyen724-g/jev-compactor)
  — Jev judges relevance; code decides structure; never rewrite;
  regex floor independent of Jev. Compaction fail-open if Jev
  down; safety fail-closed on pending destructive. OpenCode
  fail-open port already §62: fast-jev-opencode (`notes.md` §65).
  Later product-arm bench **73%** / 350 ms / 4 of 4
  (`notes.md` §68).
  WHETHER/HOW/WHAT cousin (license null; 2026-09-19
  ~04:39):
  [hermes-jev-router](https://github.com/rsdkrasen/hermes-jev-router)
  — compact original chunks; skip next main-model when
  evidence is enough (needs core patch); fail-open
  (`notes.md` §69).
  Pi summarizer-replacement cousin:
  [pi-jev-compact](https://github.com/dev-willbird1936/pi-jev-compact)
  — verbatim keep/drop of paired tool calls; fail-open to
  LLM summary if <25% saved. **≠**
  vava-nessa/pi-jev-compaction (`notes.md` §72).
  Typed baton cousin:
  [jev-handoff](https://github.com/shitianfang/jev-handoff)
  — escalate/continue/abort; gate never grants; inverted
  loop (`notes.md` §69).
  Advice-only cousin:
  [jev-decisions](https://github.com/bojansandhaus/jev-decisions)
  — 25 prepared reviews; **never stop commands**
  (`notes.md` §69).
  Adversarial-browser cousin:
  [browser-jev](https://github.com/DowLucas/browser-jev)
  — Playwright executes, Jev chooses; sample from the
  distribution (`notes.md` §69).
  Decider≠executor cousin:
  [jeffrey](https://github.com/thomasbrueggemann/jeffrey)
  — Jev→tool→Jev; LLM fills args; risk≥0.5 pause
  (`notes.md` §70).
  Persist-constraints cousin:
  [pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)
  — user constraints survive compaction; Jev never
  writes policy (`notes.md` §70).
  Plugin no-text cousin (2026-09-19 ~06:43):
  [jev-use](https://github.com/shitianfang/jev-use)
  — fail-open PreToolUse gate; Vercel margin fallback
  (`notes.md` §71).
  Pi control-plane cousin:
  [pi-jev-control](https://github.com/goodruizhan/pi-jev-control)
  — named sensors; GUI unknown never force-click
  (`notes.md` §71).

## Using Jev to test and optimize the skill suite itself

- Treat the skill directory as a routing problem: rank all frontmatter
  descriptions against the live request (Choice), gate whether anything
  fits (nouls), then rerank the top-3 with full bodies and reject-allowed
  fits-nouls. Measured reference points: gate ≥0.30 mean, winner fits ≥0.40,
  shortlist 3, 700-char excerpts, 240 skills per request; 94.4% routing on
  synthetic requests vs 70.8% lexical baseline (GodsBoy, exploratory).
- Callability tests per skill: does its description route to itself under
  (a) literal trigger phrasing, (b) user paraphrase, (c) a near-miss
  neighbor skill present? Run as batched Choice questions over descriptions.
- Distinct descriptions are a retrieval feature — lookalike descriptions
  were the top failure source in the official skill_suggestion cookbook.
  Rewrite frontmatter like Choice criteria (what / not_for / examples).
- **Judge variance before judge trust** (danielgshea/jev-as-a-judge, 100
  repetitions over frozen outputs, jev-1.13.0): a Jev judge's repeated
  ratings varied 224× less on a quality metric and 279× less on a rubric
  than a generative LLM judge's, with 0% outcome disagreement. A judge that
  is consistent is one you can threshold; a judge that moves between runs
  is noise you cannot gate. Any grader used to test a skill — Jev or LLM —
  gets this variance check first, over frozen outputs, before its numbers
  mean anything.
- Gate vocabulary is converging across implementations; reuse it rather
  than inventing: allow / ask_human / deny (ndolinschi *vocab*),
  allow / block / review ([toolgate](https://github.com/fdemir/toolgate)
  *product* — Jev is not authorization; `notes.md` §55), BLOCK / ASK /
  ALLOW ([interlock](https://github.com/somoore/interlock) *kernel* —
  Jev is SENSOR, policy decides; `notes.md` §59), ok / retry /
  escalate / stop (harnessjudge). Same shape as the lifecycle gates above.

Hourly 0843 agent self-assessment: omni-/ask-jev probabilities are advisory, not calibrated guarantees. 13 focused checks and one mutually exclusive outcome. Do not treat low mutation-attribution p as identifying someone else. huncho journal/replay: change policy without re-inference. `notes.md` §114.
User-provided 0806 uniqueness lock: people who compare Jev against GPT-5.6 has never fine-tuned BERTForXYZ for living and it shows; zero shot classifiers; scale them as much as decoder only models; many problems solved with LLMs could have been solved with them, it was a skill issue; opt for DeBERTa and ModernBERT ones; BERTForXYZ → DeBERTa → ModernBERT; Jev vs GPT-5.6 bakeoffs are a category error; encoder / ZS classifiers; institutional HF voice; quote *theirs*; do not invent accuracy numbers; softmax/ZS scores still ≠ calibrated Noul; soft scores ≠ hard gates; @mervenoyann; likes 421 / 189; impressions 35498 / 9613; multimodal image<>text ZS as perception front-end; hf:MoritzLaurer/deberta-v3-large-zeroshot-v2.0 likes 139; hf:MoritzLaurer/ModernBERT-large-zeroshot-v2.0 likes 72; Bart, bert, deberta, modernbert, these are all LLMs; Maziyar quoted; Jev is exemplar not the mandate; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29.


Hourly 0843 uniqueness lock: A hunch is a probability with a policy attached; { enter: 0.8, exit: 0.6 } is hysteresis; replay a policy change without inference; Decision models are providers, not the product; huncho ≠ Kungie/gut ≠ carldaws/hunch ≠ tpellet/hunch; pretrained Qwen2.5 base ECE 0.030 (0.5B) / 0.040 (7B); instruct 0.302 / 0.269; 70.9% → 70.0% mean conf 74.1% → 96.7%; temperature scaling still matches it in-distribution; No Jev API was called; Qwen2.5 ≠ Archer; Qwen/Qwen3.8-27B ≠ Archer; 学習済みモデル v0.1 は準備中です; bool AUROC 0.523; 先頭だと0件、末尾だと250件; 温度を渡さない場合、確率は較正されていません; このリポジトリには Jev を呼ぶコードが存在しません; g0runmezadam/what-is-jev IS tunahansahin897/what-is-jev (same GitHub id 1378007307); 947 repos scored; A 273 · B 302 · C 372; LLM rubric ≠ benches; Data as of 2026-09-20; HEAD 895b9498; README SHA 3ae98c56; 13 focused checks and one mutually exclusive outcome; Probabilities are advisory, not calibrated guarantees; omni-/ask-jev ≠ pedroknigge/mcp_jev; pd.cut bins by equal width while jeval bins by quantile; ECE 0.113 and ECE 0.076; jeval drift is not implemented yet; rlaope/jeval ≠ dayhaysoos/jevals; calibration does not compose; ECE has exactly zero statistical power to detect the failure mode that kills trajectories; 25–60× headline withdrawn; P(all-correct): 0.0071 vs 0.0001; TCE / AMS; Qwen 3.8 sparring ≠ Archer; Deferred Crispification; light_cutoff_applied_to_combination 0; recorded run, kinematic animation; BANKING77 Accuracy BERT-Base 93.02 Jev 79.90; Analyse jev calibration (NLL, ECE) backlog; BERT figures are published supervised references, not zero-shot; 档位措辞效应 分数极差中位 0.50、最大 1.32; 修好后对照组是 0.01; 不是 benchmark; 概率没做 calibration; ~1,430 API calls, about $0.15; xiaohuaxi/jev-study ≠ wjdjdakf17/jev-study ≠ baekenough/jev-study; AND: product (independence assumed and recorded in the trace); chat model's stated confidence is not calibrated; circuit-vl-4b ≠ Archer; Bring your own API key; vamsikrishna2421/jev-usecases ≠ whyashthakker/awesome-jev-use-cases; catalog ≠ endorsement; SemIf 2237★ (+30 vs §111 2207); jevlike 1049★ (+6 vs 1043); TypeLLM/TypeLLM 16★; AnotiaWang 98★; yibie/awesome-jev 520★ (+14 vs 506); Laya likes 861 (was 822); tracker likes 66 (+2 vs 64) lastModified UNCHANGED; Blackwood likes 2 gated manual; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35; notes.md §114
User-provided 0915 uniqueness lock: TianyuCodings/NanoJev unified-games-v1 densify; A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.; One model, four games; ViZDoom Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128; Maze 225 attempts vs Jev 2738; Snake 30 food / 256 steps; held-out Maze 4/10 Snake 8/8 Basic 128/128 Predict 27/128; Untuned Qwen3-0.6B baseline; 18,760 questions per variant; 16,333 ViZDoom; 896 Predict Position expert episodes; hard_lr1e5; mix weights 1/3, 1/3, 1/6, 1/6; Hub C-Tianyu/NanoJev revision unified-games-v1 likes 58; dataset C-Tianyu/NanoJev-Data likes 5; HEAD 618cea6d906d54e128360786d12f703fff2b1245; 1289★ / 158 forks / size 64035; README SHA 4190093c64ee75b26e9726daa3b00cbcf6d3157a; MIT; caijinchun/nanojev-arena ≠ liao96312/jev-arena-nanojev ≠ zwliJay/jev-forge ≠ NanoJev; not TypeSafe Jev; open replica / specialist gameplay S1; soft scores ≠ hard gates; Game success ≠ calibrated Noul; local type boolean ≠ TypeSafe noul; invented_signal false; do not reopen or amend PR #31/#32/#33/#35; notes.md §115


**0920 jcr:** pre-action lookup is not a done-check and not a permission gate. Ambiguity / no-match / depth-limit are explicit abstention paths. NiazMorshed2007/jcr. `notes.md` §116.

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

**User-provided 1936 HIGH (`notes.md` §130).** sgoedecke/system-one first-sighting. SystemOne.from_pretrained. TypeSafe-compatible ≠ TypeSafe replica. mithalouni/system-one-open first-sighting. 76.7% vs Jev 86.9% *theirs*. replica ≠ TypeSafe. kotoba-lang/typed-decisions first-sighting. DeBERTa-v3-large 0.855 / 42 ms *theirs*. kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions. aisearchio 15-link census catalog ≠ endorsement. soft scores ≠ hard gates. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided 1936 uniqueness lock: sgoedecke/system-one 20★ HEAD ebde2a2db706 README SHA d331b567e2c3; SystemOne.from_pretrained; Batched single-token choice inference; TypeSafe-compatible; cache_prefix=True; LICENSE absent; sgoedecke/system-one ≠ mithalouni/system-one-open ≠ KathanModh259/system-one ≠ babybear-labs/system-one; TypeSafe-compatible ≠ TypeSafe replica; mithalouni/system-one-open 18★ MIT HEAD 77f1f7cccf8a README SHA 535f33028a68 LICENSE SHA 2f6f2cf1064e; Gemma 4 E2B / Gemma 3 270M Modal; 76.7% vs Jev 86.9% strict common subset *theirs*; 97 ms H100 *theirs*; 74.8% held-out *theirs*; replica ≠ TypeSafe; HF upload pending; kotoba-lang/typed-decisions 1★ Apache-2.0 HEAD 10d7834d3b99 README SHA 4d6bbf4c4e44 LICENSE SHA 513bb5e3cb4c; ModernBERT / DeBERTa / LLaDA-MoE; DeBERTa-v3-large 0.855 / 42 ms *theirs*; ModernBERT-base 0.717 / 68 ms *theirs*; LLaDA-MoE 0.835 / 676 ms *theirs*; kotoba-lang/typed-decisions ≠ convaiinnovations/laya-typed-decisions; encoder class member not Jev replica; aisearchio 15-link census catalog ≠ endorsement; 12 already carded 3 gaps this fold; soft scores ≠ hard gates; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §130

**Open-Jev densify (`notes.md` §125).** DENSIFY the original 1441 card, not a sibling first sighting. HEAD 4933ee84951f README SHA ce1a587219e4. LoRA + scalar head + calibration temperature. not merged base models. customer-service P50 85.03 vs Jev 295.26 *theirs*. 1024/32 slower 1015.90 vs 301.37 *theirs*. systems latency ≠ semantic equivalence. Open-Jev TREC pending. hard acc ≠ calibrated Noul. type-valid ≠ exact. LoRA ≠ RLCD replica. Qwen/Qwen3.8-27B ≠ Archer. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
User-provided Open-Jev densify uniqueness lock: Zefan-Cai/Open-Jev densify HEAD 4933ee84951f README SHA ce1a587219e4; pushed 2026-09-21T01:34Z; Astra TREC commit 1dd56990be7e pushed 2026-09-21T01:17Z; live 3★ (was 0★; star-noise is not the fold); LoRA adapters plus trained scalar decision head and calibration temperature; not merged base models; dataset ZefanCai/Open-Jev rev c67699e13d0a; Open-Jev-2B rev 0c7aa498b162; Open-Jev-9B rev 47e966881e48; 27B still in progress; Independent of TypeSafe; no RLCD/parity claims; LoRA ≠ RLCD replica; customer-service P50 local HTTP 85.03 ms vs Jev HTTPS 295.26 ms *theirs*; 1024 tokens/32 candidates Open-Jev slower 1015.90 vs 301.37 *theirs*; prefix caching experimental/off by default; CUDA prefix caching exceeded tolerance on 9/11 workloads; systems latency ≠ semantic equivalence; GPT Luna P50 918.13 ms Astra 1938.39 ms *theirs*; TREC-DL Jev/Luna/Astra completed; Open-Jev TREC pending; 80,816 training rows; 2B 94.71% / OOD 86.02%; 9B 97.54% / 91.97% *theirs* not Harbor; hard acc ≠ calibrated Noul; type-valid ≠ exact; Qwen/Qwen3.8-27B ≠ Archer; website https://zefan-cai.github.io/open-jev/; launch X thread https://x.com/Zefan_Cai/status/2101782158658695388 https://x.com/Zefan_Cai/status/2101786019607740436 https://x.com/Zefan_Cai/status/2101789698947793231; densify §125 not a sibling first sighting; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §125
**Hourly 1946 HIGH (`notes.md` §131).** X-sentiment does not execute trades. heyjunpenn/awesome-jev 485 catalog ≠ endorsement. jev-arena 62.69% vs 67.26% *theirs* not gold. 203.2s $0.84 vs 823.5s $1.50 *theirs*. one seed-0 trial *theirs*. Jev $0.018825 vs Astra $5.93 *theirs*. 10.59× *theirs*. 6 class flips. agreement ≠ accuracy. probabilities uncalibrated. Qwen3.8 ≠ Archer. Spanish −6.4 pp XNLI *theirs*. ECE 0.057→0.101 *theirs*. 72.2% vs 63.4% p_max≥0.9 coverage *theirs*. llm-to-jev description rewrite Convert LLM prompts to Jev prompts. SHA unchanged 234058ab372d. 3★. heuristic conversion ≠ calibrated Noul. skip Zefan-Cai/Open-Jev densify open #53. skip #54 three. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#52. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 1946 uniqueness lock: brainstormity/Jev-X-Sentiment-Analysis 136★ HEAD 5c932f941a92 README SHA bf4134b44cda; platform does not execute trades; heyjunpenn/awesome-jev 485 catalog ≠ endorsement; heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev ≠ ckaraca/awesome-jev ≠ yzfly/awesome-jev-zh ≠ shirenchuang/awsomejev ≠ andyrewlee/awesome-system-one; NanmiCoder/jev-arena 10k comments 62.69% vs 67.26% *theirs* not gold; 203.2s $0.84 vs 823.5s $1.50 *theirs*; AI-reviewed labels ≠ gold; openroboto-ai/jev-robot-control one seed-0 trial *theirs*; Jev $0.018825 vs Astra $5.93 *theirs*; one-trial robot ≠ Harbor; endman100/research-Qwen3.8-JevLike 10.59× *theirs*; 6 class flips; agreement ≠ accuracy; probabilities uncalibrated; Qwen3.8 ≠ Archer; 10.59× systems ≠ ECE; marcosmartinez/jev-acento Spanish −6.4 pp XNLI *theirs*; ECE 0.057→0.101 *theirs*; 72.2% vs 63.4% p_max≥0.9 coverage *theirs*; alexwestco/llm-to-jev description rewrite Convert LLM prompts to Jev prompts; SHA unchanged 234058ab372d; 3★; heuristic conversion ≠ calibrated Noul; desc rewrite ≠ SHA/behavior change; skip Zefan-Cai/Open-Jev densify open #53; skip sgoedecke/system-one mithalouni/system-one-open kotoba-lang/typed-decisions open #54; ikermoel/open-alternative-jev already §49; nrdz-labs/fast-jev-opencode already §62; mallahyari/system-one-benchmark already §61; does not execute; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; local_only ≠ Jev; rule-table ≠ model; replica ≠ TypeSafe; arunav25/jev-mcp ≠ jkudish/jev-mcp ≠ ThePFMind/jev-mcp ≠ burnigtm/jev-mcp; luckberonne/mini-jev ≠ r-ms/mini-jev ≠ samatv256/mini-Jev; Kwwwww74/OpenJev ≠ razorback16/openjev ≠ kyegomez/open-jev ≠ Zefan-Cai/Open-Jev; peach-zhang/typesafe-go ≠ kisshan13/typesafe-ai-go ≠ Nibir1/typesafe-go; laidick/system-one-benchmark ≠ mallahyari/system-one-benchmark; sahasrarjn/system-one ≠ sgoedecke/system-one; aboisvert/jevvy ≠ PanAchy/jevvy; andrest04/jev-lab ≠ javsanesq/jevlab; twilwa/pi-typesafe ≠ TheoOliveira/pi-jev; RuipuCui/jev-harness ≠ ismaelsoilet/jev-harness ≠ AntonioCoppe/jev-harness; Archer still promised_not_landed; Hub archerhume/4rcherhume HTTP 401; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52; notes.md §131
Hourly 2049 uniqueness lock: jaredpalmer/kev densify HEAD c096660c8da2 PLAN SHA 8d77dd271c66 README SHA unchanged 84b872488915; night-2 dates/unknowable/assertion; KEV_TEMPERATURE T≈2.0; Brier 0.291→0.267 ECE 0.105→0.039 *theirs*; 7.5%→3.2% *theirs*; grouped T rejected; Qwen3.6-35B-A3B smoke 0.812 *theirs*; 21M LoRA experts frozen; Hub --revision night2-du; MMLU-Pro 1000 Kev-9B 0.511 Jev 0.829 *theirs*; Qwen3.6 ≠ Archer; temperature scaling ≠ ECE unless measured; kotoba-lang/typed-decisions densify HEAD ff7f84e74d04 README SHA unchanged 4d6bbf4c4e44; feat expose trained OpenJev decision runtime; open_jev.py; tests/test_open_jev.py; generated_text: False; trained runtime ≠ TypeSafe; OpenJev.from_pretrained; decide_request kind typed-decisions/open-jev-v1; daftAI2026/awesome-jev ≠ heyjunpenn/awesome-jev ≠ yibie/awesome-jev ≠ MrJev/awesome-jev ≠ Promethe-us/awesome-jev; danielamitay/swev CoreML; serving substrate ≠ calibrated replica; smlayero/jev-debtgate CI gate cutoff still soft; Octalab-Inc/jqv stock Qwen3 decision API; franckverrot/lev ≠ jaredpalmer/kev; neko233-com/laya-go ≠ convaiinnovations/laya; tryAGI/TypeSafeAI ≠ official; abgregs/jev-experiments ≠ nak1b/jev-experiments ≠ dabit3/jev-experiments; jaanavit/gliner2-skill Locate ≠ decide; prasanthj/duckdb-jev SQL predicates; hf:Nebulaw1 legal LoRA ≠ RLCD replica; Qwen3.5 ≠ Archer; catalog ≠ endorsement; *theirs* not Harbor; SHA move is not a replica; skip-thin KadePrice123/jev-state-tracking hideri777/jev-application-sample; Hub --revision is a pin not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55; notes.md §132

**Hourly 2146 HIGH (`notes.md` §133).** Open-Jev provider quality densify HEAD a00559ea0ab2. README SHA unchanged ce1a587219e4. provider pipeline ≠ completed Open-Jev quality. CPU tests ≠ GPU scores. 65/76 72/76 66/76 60/76 71/76 *theirs*. Open-Jev TREC pending. cartpole Kev flip HEAD 922cc61490a0. fine-tuned Kev ≠ TypeSafe Jev. one record of 64. 81.25% 52/64 *theirs*. softmax ≠ calibrated Noul. ashare rewrite HEAD 26c7e95e6828. QMT mock/dry default no orders. AUC 0.532 *theirs*. does not execute. kevin Playwright + Onyx first card. 3.69ms *theirs* not Harbor. metask-jev-4b 79.6% / 80.1% *theirs*. cutoff 95% still soft. option order can change an answer. catalog ≠ endorsement. *theirs* not Harbor. SHA move is not a replica. Do not reopen or amend PR #23–#56. Does not bump 0.5.0. Skip Archer. `invented_signal: false`.
Hourly 2146 uniqueness lock: Zefan-Cai/Open-Jev densify HEAD a00559ea0ab2 README SHA unchanged ce1a587219e4; Publish prepared Open-Jev provider quality evaluation pipeline; 808 requests 1841 labelled decisions per model; Open-Jev GPU inference has not started; 48 CPU tests pass; Open-Jev TREC pending; 65/76 72/76 66/76 60/76 71/76 *theirs*; 117/140 109/140 135/140 *theirs*; JF100 232/300 227/300 300/300 *theirs*; FizzBuzz 299/300 300/300 300/300 *theirs*; mailroom 908/921 900/921 913/921 *theirs*; Jev TREC DL19/DL20 nDCG@10 0.275836/0.190667 strict *theirs*; Luna 0.729911/0.702082 *theirs*; Astra 0.736610/0.714484 *theirs*; provider pipeline ≠ completed Open-Jev quality; CPU tests ≠ GPU scores; tinmanlab/cartpole-jev densify HEAD 922cc61490a0 README SHA 0860958714f3; Active model Kev Not TypeSafe Jev; 81.25% 52/64 *theirs*; one record of 64; fine-tuned Kev ≠ TypeSafe Jev; softmax ≠ calibrated Noul; xuboboo/ashare-trader densify HEAD 26c7e95e6828 README SHA 7a860bdfa97b; premarket + intradaily; local probability model; QMT sidecar mock/dry default no orders; AUC 0.532 *theirs*; 36 组参数全部净期望为负; does not execute; gauravsaini/kevin first card Playwright + Onyx; Laya/Kev friends *theirs*; 3.69ms *theirs* not Harbor; metask-jev-4b 79.6% / 80.1% *theirs*; Bespoke Nimble-9B 74.8% / 63.5; Jev 76.0% / 75.3; lumen mixture-of-LoRA conformal; ardada2468/typedecide ≠ shkumbinhasani/typedecide; 87 of 144 order-unstable *theirs*; bonsai 192/231 ECE 0.037 *theirs*; 8GB; vercel-labs 95% Luna fallback; cutoff 95% still soft; tinmanlab/jev-qwen3.8-27b Qwen3.8 ≠ Archer; train-your-first-jev Qwen2.5-0.5B LoRA; sankaku-tech/jev-kit ≠ WaynezProg/jev-kit ≠ isiomaC/jevkit; jevfish DecisionScore 78.24 *theirs*; Typed Decision Bench 5387; reflex-gate CoT GBNF ≠ Noul; skip-thin IOCArena laya-mirror empty SHA; snsk JP 97.6 vs 36.9 *theirs*; yunhe-dev/awesomejev catalog ≠ endorsement; yunhe-dev/awesomejev ≠ heyjunpenn/awesome-jev ≠ daftAI2026/awesome-jev; wayfind/metask-jev ≠ metask-ai/metask-jev; mjyoke1111/jev-lab already §96; mizchi/jev-playground 19★; KaLM-Jev reranker ≠ Jev replica; *theirs* not Harbor; SHA move is not a replica; do not reopen or amend PR #23/#24/#25/#26/#27/#28/#29/#30/#31/#32/#33/#34/#35/#36/#37/#38/#39/#40/#41/#42/#43/#44/#45/#46/#47/#48/#49/#50/#51/#52/#53/#54/#55/#56; notes.md §133
