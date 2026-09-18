# Jev inside optimizer and program frameworks (Ax, DSPy, and the pattern)

Grounded in live repos as of 2026-09-18: `ax-llm/ax` (native typesafe
provider, TypeScript-only), `typesafeainate/dspy-typesafeify` (Python DSPy
decorator PoC) + `jmanhype/jev-dspy-lab` (its measurement lab). Re-verify
against the archive before relying; both are young.

## The converging integration pattern

Every framework lands on the same shape: **typed outputs → one Jev request;
freeform outputs → the generative model; results recombined into the same
program interface.** The program's signature/prediction API does not change.

| Framework | Mechanism | Typed outputs | Freeform outputs |
|---|---|---|---|
| Ax (`ai({name:'typesafe'})`) | signature adapter: field descriptions become Noul/Choice/Score criteria | `boolean` (Noul + `trueThreshold`, default 0.5), `class` (Choice) | unsupported — second generative program |
| Ax native | `typesafe({apiKey}).systemOne({state, questions})` | Noul/Choice/Score with structured criteria | — |
| DSPy (`@typesafeify`) | signature-output annotation → hybrid execution plan | `bool` (thresholded Noul), `Literal` (Choice), configured score field (Score) | generative LM **after** typed results known |

## Design rules that transfer (from the adapter source, not vibes)

- Ax `trueThreshold` is **local conversion policy, never sent to the
  provider**; it applies to every boolean on that provider instance. One
  threshold per provider ≠ per-action costs — set per-action gates in your
  own policy layer instead of different provider instances.
- Field/description mapping is validated strictly: duplicate or unknown
  criteria keys and empty descriptions **fail before network access**.
  Quote class labels containing spaces/punctuation.
- Adapter rejects optional, array, nested, numeric, and freeform outputs
  pre-network. Numeric `min`/`max` does NOT become a Score rubric — use the
  native client for Scores.
- No streaming, no temperature, no samples, no media. `streamingForward()`
  returns a completed result, not a stream.
- Question keys are answer labels, not instructions — native entries need
  explicit `instructions`; Choice 1–255 labels, Score 2–10 levels.
- Chat log keeps `providerMetadata.typesafe.answers` — read distributions
  from there, not from the booleanized program result, when calibrating.

## Optimizers (GEPA / DSPy teleprompters) — what to couple, what not

- **Jev does not replace the optimizer's search role.** It replaces the
  *executor* of typed fields and the *judge* of scalar metrics. Keep the
  optimizer loop (GEPA Pareto / MIPRO-style proposal + selection) intact.
- **Judge consistency is Jev's optimizer win.** Axiom: optimizer metrics must
  be deterministic and cheap; an LLM-judge metric adds the judge's own
  variance into the search signal. The measured judge-variance recipe
  (100 reps over frozen outputs: Jev judge ratings varied 224–279× less than
  a GPT judge's, danielgshea/jev-dspy-lab-adjacent result) makes a Jev judge
  the defensible choice for optimizer metrics that need semantic judgment:
  same frozen-output variance check first, then wire the Jev judge as a
  deterministic-ish metric.
- **Teacher/student split fits the primitives**: teacher (frontier model)
  proposes candidates or distills criteria; student (Jev) executes the typed
  path cheaply. In Ax terms: strong `teacherAI`, cheap `studentAI`
  (`ai({name:'typesafe'})`), `maxMetricCalls` bounded.
- **Do not let the optimizer tune thresholds off the sweep it runs.** The
  jev-dspy-lab rule: threshold sweep is exploratory; the confirmatory gate
  is chosen before the run and reported from the same run, never the best
  sweep row. This is standard train/confirm discipline — frameworks will
  not enforce it for you.
- **Hybrid signatures need an explicit plan**: DSPy's decorator splits
  typed/freeform fields and feeds trusted typed results into the generative
  call. If your framework lacks this, replicate it: one systemOne call for
  all typed fields, then one generative call with those fields as inputs.
  Never interleave Noul results as if they were generated text.

## Calibration and measurement obligations (jev-dspy-lab)

Before trusting a Jev-decorated DSPy program: dataset-level calibration
(with bootstrap CIs), selective risk/coverage curve across gates, a fail-closed
abstention policy, and reproducible offline evidence with canonical request
hashes. PoC benchmarks on 3 cases without caching are a lead, not a result.

## Where the gaps are

- Ax typesafe support is **TypeScript-only** (AxIR backlog); no Python.
- DSPy integration is a **stripped-down PoC**; optimizer-aware tuning of
  Jev thresholds/criteria is not built — that work is open, and the
  honest claim to date is "decorator executes typed fields," not "Jev is
  optimizable inside DSPy."
- Nothing yet covers optimizing *against* Jev as the metric model
  end-to-end; if you build it, measure judge variance first (see above).
