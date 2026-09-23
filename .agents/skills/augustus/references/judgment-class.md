# The judgment-model class (Jev is exemplar, not monopoly)

Augustus covers models that turn supplied evidence into a bounded judgment:
a label, span, ordering, score, or distribution. TypeSafe Jev (Choice, Score,
Noul) is the default hosted exemplar by project preference. That is a design
default, not an empirical claim about adoption, superiority, or universal
calibration.

Use this reference to select a family. Use provider documentation for live API
contracts. A compatible endpoint, typed response, softmax, or low error rate
does not establish semantic equivalence to another model.

## The class

A component belongs here when its main product is a bounded answer rather than
new prose. Usually:

- inputs are declared text, structured state, or supported media plus a question;
- outputs are labels, spans, ranks, scores, or distributions;
- the component can run at decision frequency; and
- code owns control flow, authorization, and side effects.

Do not force an exact rule, database lookup, parser, solver, or arithmetic step
through a model. Do not force open-ended writing through a classifier. The
useful question is not “is this AI?” but “what output is required, what evidence
exists, and what loss matters when it is wrong?”

## Families

| Family | Output and objective | Best fit | Main cautions |
|---|---|---|---|
| **Classical supervised model** | Label, probability, or regression estimate learned from a stable feature table | A closed taxonomy with enough representative labels and controlled retraining | Distribution shift, leakage, and rare-class performance. It may beat every general decision model on its own domain |
| **Tabular foundation model** | Prediction conditioned on labeled feature rows | Repeated structured-data decisions where a pretrained tabular prior may help | Compare with linear/tree baselines. Paper results, checkpoint, runtime limits, and weight license are separate evidence objects; see [TabPFN](https://github.com/PriorLabs/TabPFN) |
| **Decision-focused learner** | Predictor or objective trained for downstream optimization loss/regret | An explicit optimization problem with known constraints and observable outcomes | Better prediction does not imply better decisions; compare with predict-then-optimize and measure regret/constraint violations ([DF²](https://proceedings.mlr.press/v286/kong25a.html)) |
| **Causal policy learner** | Estimated value/effect of assigning an action | Interventions with a defensible identification design | Observational association is not an intervention effect. Requires assumptions about confounding, overlap, and outcomes, not merely a classifier ([policy learning](https://onlinelibrary.wiley.com/doi/full/10.3982/ECTA15732)) |
| **Typed API or trained decision head** | Choice, ordered score, boolean-like judgment, or a full distribution | Bounded semantic decisions, especially when batching and abstention are useful | “Trained for calibration” is an objective, not a guarantee. Measure calibration, selectivity, and shift on the deployment population |
| **Constrained autoregressive or logit readout** | Allowed token/field distribution from a causal LM, with or without constrained decoding | Typed fields, local serving, or dependent fields that must condition on earlier answers | Schema validity is not correctness. Token logits are not automatically calibrated probabilities of the requested event |
| **Span extractor** | Text offsets and entity/type labels | The answer is literally present in the supplied text | Cannot recover absent evidence; overlap and boundary errors need explicit handling. [GLiNER](https://arxiv.org/abs/2311.08526) is the canonical open example |
| **Sequence or multi-label classifier** | One or more labels for the whole input | Large or changing label sets; routing and tagging | Label affinity is not authorization. [GLiClass](https://arxiv.org/abs/2508.07662) is distinct from span extraction |
| **Ranker** | Relative order or relevance score over a candidate list | Reranking retrieved passages, tools, or options | Ranking losses optimize order, not an absolute decision boundary. Preserve a fallback order on failure ([listwise overview](https://doi.org/10.48550/arxiv.2208.06164)) |
| **Vision scorer or decision model** | Image–text affinity, region selection, or a bounded visual answer | Perception over declared labels/regions or typed visual decisions | Candidate scores are relative to the offered set; visual readouts require their own calibration and shift tests. [SigLIP](https://huggingface.co/docs/transformers/v4.39.2/en/model_doc/siglip) is an affinity model, not a permission oracle |

Provider examples are evidence that a family can be implemented, not proof that
the implementations are interchangeable. [Laya](https://github.com/NandhaKishorM/laya),
[kev](https://github.com/jaredpalmer/kev), and
[Bespoke Nimble](https://github.com/bespokelabsai/nimble) are open decision-head
examples. [TypeAR](https://github.com/zmtomorrow/TypeAR) is a constrained-AR
example. [GLiNER2](https://github.com/fastino-ai/gliner2) combines several
extraction/classification surfaces. Their repositories own their operational
contracts.

Pick the family from the hole, then pick a provider.

### Prediction is not intervention

`P(late | order, historical policy)` does not answer whether imposing a fine
will make delivery faster. Past managers may already have intervened on
high-risk orders, changing their labels. Define the treatment, outcome, target
population, support/overlap, and identification strategy before claiming action
value. Without that evidence, use predictions for review or a properly designed
experiment, not as proof that an intervention works.

### Explicit state and low-latency deployment

A stateless interface makes state ownership visible; it does not mean the model
has no learned priors, the service stores no data, or repeated calls are
independent. Verify retention and caching separately. Low latency is a measured
runtime property: include cold start, network, batching, fallback, and target
hardware rather than transferring a paper's throughput to this workflow.

## Species map (GLiNER is a peer, not a footnote)

```text
decide      state + question → bounded Choice / Score / Noul-like answer
locate      text + types → spans already present in the text
categorize  text + labels → document or record labels
rank        query + candidates → relative order
perceive    image + declared labels/regions → affinity or bounded answer
generate    state + instruction → new text                         (outside class)
```

These species compose but do not collapse into one another. OCR or a span
extractor may propose candidates; a decision head may judge them; code may
apply policy. A ranker can order candidates before a decision gate. A vision
model may serialize observations for a text decision model. Name every stage
and preserve its uncertainty rather than calling the whole pipeline “the
classifier.”

Candidate coverage is a first-class limit:

- A Choice is conditional on the offered options. If the set may be incomplete,
  add `other` / `none`, retrieve more broadly, or escalate.
- A span extractor cannot return evidence missing from the input.
- A ranker cannot rescue a candidate the retriever omitted.
- A vision scorer cannot choose an object the detector or prompt set never
  represented.

Measure coverage separately from selection accuracy.

## Listwise discriminative vs decision objectives

Rankers optimize an ordering. Their scores may be translation-invariant or
otherwise meaningful only inside the current list. They are appropriate for
“show the best few first,” where an error degrades quality.

Decision models optimize a bounded answer that downstream policy may use.
Proper scoring rules and calibration-oriented training can make probabilities
more useful, but training intent never guarantees deployed calibration. Check
reliability, Brier or log loss, selective risk, and subgroup/OOD behavior on
held-out data from the actual population.

Do not threshold a listwise relevance number as `P(permit)`. If a ranked result
must trigger an action, add an independently evaluated decision stage or human
review. Conversely, do not pay for a decision API when ranking alone is the
product.

## Vision scoring patterns

Prefer the narrowest adequate observation:

1. **Structured state first.** Accessibility trees, DOM nodes, telemetry, OCR
   boxes, or detector outputs become explicit candidates. A model scores among
   them; code validates and acts.
2. **Dual-encoder affinity.** CLIP/SigLIP-style similarity is useful for
   retrieval or relative selection. It is not inherently a calibrated safety
   probability.
3. **Frozen-VLM logit readout.** Read answer-token logits for declared options.
   This can be fast and typed, but remains a readout whose quality is model- and
   prompt-dependent; [glance](https://github.com/yoheinakajima/glance) is a
   harness example, not trained decision weights.
4. **Trained multimodal head.** A model trained directly for bounded visual
   decisions may fit repeated perception loops. Evaluate it on the actual
   camera/UI distribution and treat its output as evidence, not authority.
5. **Generative VLM.** Use when a description or new candidate must be written.
   If it proposes actions, validate them against the host's observed action set.

In computer use, “done” is a model judgment, not observed success. Verify the
post-state through the host, server, DOM, or task oracle.

For audio/video or combined media, inspect the actual loader, preprocessing,
and observation window. A finite-option head does not establish support for
every modality or option count. Record clipping, frame sampling, missing-media
behavior, base-model dependencies, and precision/runtime changes; calibrate
and test each relevant slice. [Jev-Omni](https://huggingface.co/akhilaaa3/Jev-Omni/tree/55b53f2ec1b4c656c8a6172b0c7555ae578a9c3f)
is a reported open multimodal example, not TypeSafe's hosted text-only Jev.
Compare with exact telemetry or a narrower perception baseline. Falsify the
placement with decisive evidence outside the sampled window: a confident
answer cannot recover an event the pipeline never observed.

## Marginals, not a probabilistic program

Parallel questions normally return marginal judgments conditioned on shared
state. They do not define a joint distribution. Do not multiply answers as if
they were independent, infer a causal graph from them, or call the provider a
probabilistic programming system.

Fuse outputs in visible code. When interactions matter, encode the interaction
as its own question, use a model trained for the joint task, or evaluate the
composed policy end to end.

## Entropy as allocator (Hypothesis)

Uncertainty can allocate work: accept an easy reversible path, send a middle
band to a stronger model or human, and reject or gather evidence elsewhere.
This is a policy hypothesis until tested against action costs. Entropy alone
does not say which fallback is best, and 0.5 is not universally a boundary.

Entropy, top-option mass, and a handler's case-wise accuracy are different
scores. On a binary menu, entropy falls strictly as the larger probability
rises, so the two rankings agree. With three or more options they need not.
Local arithmetic: binary entropy at masses (0.6, 0.4) is about 0.971 bits,
while a ten-way distribution with top mass 0.8 and an even remainder is about
1.356 bits. Top-mass treats the ten-way case as more confident; an entropy
threshold can escalate it first. Do not call an entropy band softmax-response
selection, and do not treat either score as a calibrated probability of being
correct. A ranking score can still support post-hoc selective classification
when accepted-slice risk and coverage are measured on a proper holdout.
Calibration is not a universal prerequisite for that ranking.

Name which of these three policies is in force:

- **Two-act expected cost.** No reject option. With probabilities that mean
  class probabilities on this population, pick the lower expected-cost act.
  `validation.md` states the zero-correct-cost binary threshold and its
  assumptions. If one act is cheaper no matter the true class, the constant
  label-all policy is optimal.
- **Post-hoc selective classification.** The score orders cases. Report risk
  on the accepted slice and coverage. That risk excludes the rejected mass.
- **Deferral to a named handler.** System loss includes that handler's errors
  on the deferred slice and the cost of asking. Constant reject cost is the
  special case where the handler's loss does not depend on the case. A frozen
  head that was not trained on the handler's mistakes is not an expert-adapted
  rejector.

Compare the chosen score with always-act, always-defer, and the other score
on held-out system loss. The handler, an exact rule, or a person owns the act.

Expected cost must include:

```text
model calls + latency + generator fallback + human review
+ cost of wrong action + cost of abstention + retry/recovery
```

A cheap first stage that escalates most cases or creates expensive corrections
may lose to a simpler baseline.

## Compute graph: readout vs constrained AR vs diffusion reads

- **Trained decision head:** shared representation → task-specific bounded
  outputs. Best when the training objective matches the downstream judgment.
- **Logit readout:** pretrained causal/VLM representation → probability mass on
  declared answer tokens. Fast and convenient; semantics and calibration are
  prompt/model dependent.
- **Constrained AR:** decoding is restricted to valid fields or tokens. Useful
  when later fields depend on earlier fields. Valid structure does not make the
  content true.
- **Encoder extraction/classification:** all labels/spans can interact in one
  pass. Excellent for locate/categorize jobs, with different limitations from
  autoregressive models.

Serving compatibility is not objective equivalence. An endpoint that accepts
the same JSON can still have different logits, error modes, coverage, and
calibration.

### Holes

Choose a family by completing this sentence:

> Given **this evidence and candidate source**, the system must **locate / tag /
> order / decide / perceive** so that **this policy** can take **this action**.

If the verb is “write,” use a generator. If the answer is exact, use code. If
evidence is missing, gather it before judging.

### When to use which decision surface

| Need | Start with |
|---|---|
| Stable labels and ample representative gold | Classical supervised model |
| Few-shot bounded semantic judgment; hosted acceptable | TypeSafe Jev as the project-default exemplar, then validate |
| Self-hosted bounded decisions | Open trained decision head, with full self-evaluation |
| Typed output from an existing causal LM | Constrained AR or logit readout |
| Exact text spans | Span extractor |
| Many document labels in one pass | Sequence/multi-label classifier |
| Best ordering of retrieved candidates | Ranker |
| Declared visual labels or regions | Vision scorer/decision head |
| New prose, code, or candidates | Generator |

Failure policy is chosen **per action**, not per family. A ranker error may keep
the original order; a context-pruning error keeps the evidence; a tool-call
error withholds execution; a draft-writing error may fall back to a generator
or human. Provider timeout is neither approval nor rejection: map it explicitly.

## Decision-design extras for class choice

Record:

```text
Required output species:
Evidence and candidate source:
Known coverage gaps / no-match behavior:
Family and provider (versioned):
What remains exact; what remains generative:
Action and owner of authority:
Per-action threshold and error fallback:
Held-out labels and shift slices:
Calibration / rank / span / task metrics appropriate to the family:
Trajectory or cascade success, latency, generator rate, human rate, total cost:
State freshness and authority re-check immediately before action:
Smallest result that would reject this placement:
```

The final acceptance test is the policy in context, not the model in isolation.
