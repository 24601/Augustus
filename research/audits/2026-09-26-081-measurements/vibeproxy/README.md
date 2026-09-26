# Augustus 0.8.1: completed VibeProxy pilot

## Conclusion

The frozen pilot ran successfully, but **does not demonstrate an overall skill
benefit**. All 22 agent arms completed. Exact trainer activation was **1/2** on
the two predeclared unambiguous trainer prompts; neither Augustus skill fired
on any of the **five negative prompts**. Eight task pairs had semantic graders:
all eight passed in both arms, so the automated outcome delta was zero.
Three other pairs had only activation graders and supply no automated outcome
quality score. Direct answer review found important errors missed by the judge.

Reported cost was **$1.3384598**, below the $3 launch-stop threshold, with no
censoring. This is Claude's list-price estimate, not an independently reconciled
VibeProxy/subscription bill. The with-plugin arm cost about **31.9% more** including
grading in this sample. No further inference or budget expansion was performed.

## Frozen inputs and execution

- Release: [v0.8.1 / 4ba9d211](https://github.com/24601/Augustus/commit/4ba9d2111d29ea03247c22b3de90bfa8dde1b261).
- Measurement-plan source: [dc405e6e](https://github.com/24601/Augustus/commit/dc405e6ec68a4c1801ce623daf93f5081ff07800), fetched into a disposable bare clone,
  not the concurrent checkout. The predeclared plan and original fingerprints
  are included as `plan.md` and `suite-sha256.txt`.
- All **30 suite files** matched the committed fingerprints before execution
  and after collection. `suite/` contains their unchanged bytes.
- `release-agents/` matches every tracked `.agents/` file at the release revision
  byte-for-byte. `frozen-content-hashes.json` covers both frozen inputs.
- Claude Code **2.1.282**, not the orb's 2.1.283. This host-version difference is
  an explicit execution deviation; prompts, graders, models, budget, runs and
  ablation were unchanged.
- Start 2026-09-26T23:42:29.544Z; elapsed **360 seconds**; exit **0**; partial **false**.
- Eleven cases, one agent run per arm, concurrency one; requested agent
  `claude-opus-5-5`, requested judge `claude-haiku-4-5-20251001`.
- CLI's LLM graders used three votes per final answer (48 judge votes across
  16 semantically graded answers), not three agent replicates. The metadata's
  `runsPerCase: 3` is the case default; each actual arms array has length one.

Exact flags and routing evidence are retained in `routing.json`. The command
used the frozen export as its working directory and a new `CLAUDE_CONFIG_DIR`:

```sh
claude plugin eval . --eval-dir tests/plugin-evals \
  --ablation with-without \
  --model claude-opus-5-5 --judge-model claude-haiku-4-5-20251001 \
  --runs 1 --concurrency 1 --max-cost-usd 3 \
  --keep-temp --no-publish --no-scaffold --mocks record --trust-plugin \
  --output-dir "$RUN/results/pilot" --json "$RUN/results/pilot.json"
```

This is a receipt, not permission to rerun the command.

## Provider routing and identity limits

The running VibeProxy app advertised the exact requested agent and judge at
localhost ports 8317/8318. Its normal backend configuration enabled retries and
preview-model fallback. To avoid changing that shared service or permitting a
silent substitute, this pilot launched a **disposable instance of VibeProxy's
bundled CLIProxyAPI 7.3.17**, commit `9bdde54b`, on loopback port 52339.

The disposable config referenced the existing server-side auth directory and
upstream proxy setting. It used `request-retry: 0`, both quota-switch options
false, no model aliases, and `-local-model` to freeze the bundled catalog.
The client used a nonsecret local placeholder auth value; no credential was
printed, copied into this archive, or transferred between hosts. Normal Claude
settings and the running VibeProxy settings were not edited. The temporary
proxy was stopped when the evaluation finished; its port is no longer listening.

All **83 POST /v1/messages** log entries returned HTTP 200. The retained
`proxy-http-status.log` excludes unrelated account logs. Startup included failed
refresh attempts for an unrelated OpenAI credential and 404s on Claude's
`HEAD /api/hello` feature probe; neither prevented the Claude inference calls.
There was no second pilot launch or transport retry by this coordinator.

Every agent trace's init metadata and every assistant response model field
reported **claude-opus-5-5**, with successful final result events. No alternative
model name was observed. The requested judge ID is recorded in the evaluator
result and command; separate raw judge response model metadata was not retained
by this evaluator, so the judge's runtime identity is **not independently
verified**. Catalog names, provider labels, client metadata and proxy response
names are not independent backend attestation; do not claim more.

## Actual treatment and tools

All 11 with-plugin traces list `.agents:augustus` and `.agents:augustus-train`.
All 11 baseline traces omit both. Other built-in skills and the built-in
`agents-md` plugin remain in **both** arms. Thus this tests “both Augustus skills
available versus neither,” not “a host with literally no skills.” The inventory
difference was exactly those two skills, and the baseline made no Skill calls.

Both arms exposed the same Read/Glob/Grep/Skill inventory plus the host's
Task/TaskStop tools. No Task, shell, write, edit or web tool was actually invoked;
no MCP server was loaded. Actual tool use is enumerated per case in
`summary.json`. This was an advice-only test in empty sandbox working directories,
not a training or SDK-installation execution test.

## Activation from traces, not prose

A success requires an exact Skill input, a successful tool result, and a following
message containing the loaded skill body. None of these counts come from a text
mention or a generic “Skill called” test alone.

| Case | Observed with-plugin loading | Predeclared interpretation |
| --- | --- | --- |
| fit_budget | Augustus only | **Train miss**; does not count as Train activation |
| trainer_application_data | Augustus Train directly | **Train success**, with the training-data reference read |
| no_match | Augustus | Main-skill success |
| refund_router | Augustus | Main-skill success |
| ranker_gate | Neither | Main-skill miss |
| fit_economics | Neither | Ambiguous, excluded from recall; arithmetic outcome retained |
| plain_rewrite | Neither | Negative, correct nontrigger |
| provider_setup | Neither | Negative, correct nontrigger |
| train_word_nontrigger | Neither | Negative, correct nontrigger |
| trainer_copy_control | Neither | Negative, correct nontrigger |
| training_arithmetic_nontrigger | Neither | Negative, correct nontrigger |

Exact trainer recall: **1/2**. Main-skill recall on its three predeclared positives:
**2/3**. Trainer-only and either-skill false-positive counts on negatives: **0/5**
each. No companion-to-Train activation chain occurred. These are counts from
tiny fixed samples, not population recall/FPR estimates.

## Paired outcomes and resource use

After removing every activation grader, the frozen automated semantic result is:

| Both pass | With-only pass | Without-only pass | Neither passes | No semantic grader |
| --- | --- | --- | --- | --- |
| 8 | 0 | 0 | 0 | 3 |

The three unscored cases are `plain_rewrite`, `provider_setup`, and
`trainer_copy_control`. The evaluator's “11/11 cases passed” and mean delta zero
must not be represented as eleven independently measured task-quality ties.
No missing, failed or budget-censored agent outcomes occurred.

| Measure | With Augustus | Without Augustus |
| --- | ---: | ---: |
| Agent runs | 11 | 11 |
| Reported agent cost | $0.7376792 | $0.5541966 |
| Reported judge cost | $0.0235950 | $0.0229890 |
| Reported total | $0.7612742 | $0.5771856 |
| Sum of rounded arm durations | 189 s | 172 s |
| Agent output tokens | 13,982 | 13,011 |
| Agent cache-read input tokens | 141,246 | 86,033 |
| Agent cache-created input tokens | 85,926 | 55,330 |
| Other agent input tokens | 40 | 30 |

With-plugin total cost was $0.1840886 higher (31.9%); agent-only cost was 33.1%
higher. Duration sums are rounded per arm and include grading, so their sum need
not equal the 360-second wall time. Sequential with-then-without execution,
cache reuse and ordinary response-length variation confound performance/cost
comparisons. These are observations, not a causal latency or cost estimate.

## Direct answer review: the green score misses real defects

This coordinator review was **not blinded**, used no additional paid judge,
and does not replace the frozen score with a conveniently improved metric.
Both sets of answers are in `answers/`; exact judge votes and criteria remain in
`pilot.json`. Findings below distinguish task correctness from activation.

- **fit_budget — mixed, not a dependable executable plan.** Both arms propose
  cheap baselines and protect fitting/evaluation conceptually, satisfying the
  broad grader. Both incorrectly treat inter-rater agreement as an accuracy
  ceiling. The with-plugin answer improves grouping, nested tuning and fresh
  confirmation, but asks to train on **24 examples per class inside held-out
  5-fold CV**, when at most 19–20 of the available 24 are in a training fold.
  It also assumes the current rules were not fit to these data; the baseline
  correctly asks whether they were. Augustus Train did not load here.
- **fit_economics — core arithmetic correct in both, but extra advice is worse
  in the with-plugin answer.** Both compute 320/175/190 per 1,000, select
  zero-shot at $950 versus fitted $1,075 for 5,000 future decisions, and give
  the right 13,334 integer break-even. The with-plugin answer then invents a
  **5.5:1 crossover with the direction reversed**. Holding FP cost at $1 and
  FN cost at c, fitted minus zero-shot cost is `5c - 55`: fitted is cheaper
  per inference only for **c < 11**, not above 5.5. The grader passed this
  answer unanimously because its core-arithmetic criterion missed the added
  false claim. Neither arm loaded a skill, so this is not evidence of a
  skill-content-caused regression.
- **no_match — both address the missing option.** The with-plugin answer gives
  an explicit scope/fallback flow and rejection test. The baseline adds an
  unnecessary claim that independent sigmoid scores fix out-of-scope detection.
  Both overstate an unobserved normalization mechanism as the cause. No exact
  production classifier was available to verify either diagnosis.
- **ranker_gate — broad tie.** Neither arm loads a skill; both correctly reject
  treating a reranker score as truth probability and suggest labeled evaluation.
  Their near-identical broad advice is not evidence that loading helped.
- **refund_router — both preserve authorization.** Both move order resolution,
  eligibility and payment authority into exact policy/code. With-plugin adds
  explicit held-out rejection criteria; baseline explicitly requires the original
  payment method. Both meet the frozen safety criterion; neither is a verified
  implementation or a complete identity-authentication design.
- **train_word_nontrigger — the with-plugin arm follows the one-sentence request;
  the baseline adds two explanatory sentences.** The judge voted PASS three
  times for both despite its “one clear sentence” criterion. Neither loaded a
  skill, so attributing this formatting win to skill execution would be wrong.
- **trainer_application_data — useful improvements, not an established win.**
  The Train-loaded answer preserves original/adjudicated labels, separates a
  challenge set and pins thresholds on development data. Both answers correctly
  use the first message and customer/time separation. The baseline's final
  “train on customer ID or resolution notes and expect chance” leakage check is
  unsound: a deliberately forbidden feature can predict labels well without
  showing that the deployed feature pipeline includes it. Both pass the rubric;
  the single pair suggests a hypothesis for a sharper held-out evaluation.
- **training_arithmetic_nontrigger — correct in both:** $3.00. No added model
  advice and no activation.
- **Unscored controls:** neither provider-setup answer actually installs anything
  in the deliberately empty read-only sandbox; both ask for project details.
  The rewrite controls are retained for inspection but not retroactively added
  to the frozen outcome denominator.

The break-even arithmetic and both adjacent integer volumes were checked with
exact rational arithmetic during collection/review. All raw answers remain
available so future reviewers can disagree with these qualitative assessments.

## Archive contents, sanitization and limits

- `traces/`: 22 full agent traces; successful Skill results and loaded content
  retained. `answers/`: 22 final answers. `pilot.json`: original result structure
  with trace paths made archive-relative. `summary.json`: independent inventory,
  activation, resource and outcome extraction, including original trace hashes.
- Home-directory identifiers and email-like strings were redacted in generated
  evidence; frozen suite and skill bytes were deliberately unchanged. Token/JWT/
  private-key scans found no secrets. No config directory, auth files, raw proxy
  logs or sealed per-run home directory is included. `SHA256SUMS` covers every
  exported file except itself.
- `proxy-http-status.log`, `routing.json` and `models.json` retain nonsecret
  routing evidence. Upstream account identities and unrelated token-refresh logs
  are excluded. Reported costs remain estimates; model names remain reported
  identities, not cryptographic/provider-independent attestation.
- One run per case cannot show stability or general superiority. Inputs include
  released regression fixtures, not a held-out population. Removing both skills
  does not isolate Train's incremental causal contribution. Built-in skills remain
  available in both arms. Advice quality does not establish trained-artifact or
  production benefit. No prompts, descriptions, graders or released skill files
  were changed after observing these outputs. No commit or push was performed.
