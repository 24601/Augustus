# Jev inside optimizer and program frameworks (Ax, DSPy, and the pattern)

Grounded in live repos as of 2026-09-18: `ax-llm/ax` (native typesafe
provider, TypeScript-only), `typesafeainate/dspy-typesafeify` (Python DSPy
decorator PoC) + `jmanhype/jev-dspy-lab` (its measurement lab). Re-verify
against the archive before relying; both are young.

This card is the **placement** of a judgment-class model inside an
optimizer loop — which seat it takes, which it must not, and what you owe
before trusting its numbers. Option names below are named so you can find
them, not transcribed as a call shape: the frameworks' own docs own their
signatures, and `typesafe-ai` plus the live docs own Jev's request body.
Do not write either from this page. DSPy and Ax tune the LM-program
slice only. They are never the primary System One calibration score;
that seat is a jevals-shaped labeled suite, and a product loop is a
Harbor taskset (`validation.md`, Eval & hill-climb).

## Judgment: what these optimizers may climb (Hypothesis)

DSPy is the Python LM-program optimizer. Ax is the DSPy-style
TypeScript one
([ax-llm/ax](https://github.com/ax-llm/ax); the README calls it DSPy
for TypeScript). Both climb **LM program knobs** — prompts,
demonstrations, module graphs, sometimes which model. That is a narrow
yes. It is not a perception pipeline and not a calibration loop.
`validation.md`; `research/notes.md` §41.

Use them for criteria and instruction text, and for few-shot
demonstrations, on a generative or constrained-AR decision head
(TypeAR, a schema-prompted LLM), and for an optional LLM rewrite of a
perception-to-state summary.

Do not expect them to climb SAM multiplex, which objects to keep, ASR
decoding or diarization, Jev API calibration, or the choice between a
staged pair and a native multimodal System One. Proprietary Jev has no
prompt loop: schema, criteria, and policy thresholds, scored on labeled
eval (jevals) — not a search over a decoder. Open recipes such as
Nimble: climb data curation and LoRA, measured on holdout ECE and
agreement. Nimble's published holdout is agreement on synthetic
labels, not a measured ECE (`judgment-class.md`).

No call shape in this paragraph. The adapter notes below stay names of
seats, not a request you copy.

## The converging integration pattern

Every framework lands on the same shape: **typed outputs → one Jev request;
freeform outputs → the generative model; results recombined into the same
program interface.** The program's signature/prediction API does not change.

| Framework | Mechanism | Typed outputs | Freeform outputs |
|---|---|---|---|
| Ax (typesafe provider) | signature adapter: field descriptions become Noul/Choice/Score criteria | `boolean` (Noul + `trueThreshold`, default 0.5), `class` (Choice) | unsupported — second generative program |
| Ax native client | one request carrying the shared state plus all typed questions | Noul/Choice/Score with structured criteria | — |
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

## ProgramAsWeights: materializing a Jev judgment locally (Hypothesis)

PAW (programasweights, pre-dates Jev — Python SDK 0.4.6, Mar 2026 repo, MIT)
compiles a natural-language spec into a **tiny neural program** — a `.paw`
bundle of KV-cache prefix + optional LoRA adapter over a fixed interpreter
(Qwen3-0.6B ~22 MB or GPT-2 ~5 MB, WebAssembly-capable) that then runs locally,
deterministic, no API at runtime: `paw.compile("Classify…")`, `fn(x) → label`
in ~0.03–0.5 s. Fuzzy text tasks: classify, extract, repair, triage, route.

**Why it pairs with Jev** — complementary, not overlapping. Jev is the
calibrated semantic oracle (state → typed decision, network, per-call); PAW is
a *materialized judgment*: once a decision surface is stable, compile it into
a local artifact for high-volume/offline/zero-latency paths. No measured Jev+
PAW integration exists in the wild (checked the full 187-repo archive), so
this is Hypothesis-grade. Two candidate couplings:

1. **Jev as the labeling teacher.** Use Jev fan-outs to score a labeled set
   (its calibration is the reason to trust the labels), pass `examples=[…]`
   into the PAW compile/finetune compiler (`paw-ft-bs48`), then serve locally.
   Jev = oracle, PAW = distilled student. This is ordinary distillation with
   an unusually cheap teacher.
2. **Jev as the calibration gate on PAW.** Shadow both on live traffic;
   a calibrated Jev judgment arbitrates disagreements and the disagreement
   rate is the drift signal for when to recompile the PAW program. Threshold
   obligations apply (per-dataset calibration; see validation.md).

**When NOT to pair:** if the decision surface still changes daily, or inputs
need long-tail reasoning beyond the fuzzy-task classes PAW is sized for,
keep calling Jev — premature compilation freezes a moving judgment. The
stability gate is the same shadow-mode behavioral-eval gate in validation.md.

**Test** (any claimed integration must show): labeled-set agreement Jev vs
PAW output on held-out data, per-class cost/latency comparison, and a drift
measurement over a week of live inputs.
