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
   Computer-use cousin of the same honesty:
   [gliner2-ultrafast](https://github.com/sahibzada-allahyar/gliner2-ultrafast)
   — loop `DONE` is termination, not verified success; apps inspect
   the actual result (`notes.md` §52).
4. **Stuck-detector**: three failures with the same strategy → ask for a
   new hypothesis, not another retry.
5. **Supervision during long runs** (foreman): separate concurrent loop
   estimates `meaningful_progress`, `implementation_complete`,
   `tests_sufficient`, `worker_stuck`, `work_off_track`,
   `ready_to_finish`; deterministic policy with hysteresis (retry counts,
   verification history) gates continue/stop/retry/verify. The model never
   commands; it estimates named probabilities. Same split as
   [jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab):
   **S1 keeps control**; optional S2 is one-use advice on low confidence
   and does not fly the drone (`notes.md` §46). Experimental viz, not a
   production supervisor. Computer-use speed layer of the same split:
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
6. **Context economy**: the context-sieve card
   (`references/applied-mappings.md#1-context-sieve`). Judge every large
   tool result with one relevance Noul before it enters context. Hide
   confident-no blocks behind a stub + recall key; always keep current
   instruction, recent turns, errors, and opaque blocks. winnow hides at
  relevance ≤0.22; fast-jev-compaction asks two nouls per tool call
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
  (`notes.md` §55). Do not copy mcp add.

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
  (`notes.md` §55). Session-memory *omit* fails open (dump the
  ledger): [carryforward](https://github.com/Dharundp6/jev-carryforward).
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
  ([jev-reviewer](https://github.com/choxos/jev-reviewer); `notes.md` §48).
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
  *product* — Jev is not authorization; `notes.md` §55), ok / retry /
  escalate / stop (harnessjudge). Same shape as the lifecycle gates above.
