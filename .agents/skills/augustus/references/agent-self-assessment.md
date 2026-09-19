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
  Stdout-prune cousin, same family, different job:
  [jev-pruner](https://github.com/tamaratran/jev-pruner) — Jev Noul on
  Bash chunks after a hard envelope; fail-safe original; archive
  (`notes.md` §53). Marketplace id still `fast-jev-output`.
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
  fails closed to `keep_full` (`notes.md` §50). Stdout prune is the
  same polarity:
  [jev-pruner](https://github.com/tamaratran/jev-pruner) fails closed
  to original output (`notes.md` §53). Tool *execution* is the
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
