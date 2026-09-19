# The toolbox sweep: how to find approaches and applications for a new primitive

Jev is out-of-distribution: no cookbook for most of its uses exists yet, and
prompting an LLM to "be creative with the docs" produces shallow rehashes of
the launch demos. This card is the *meta-method* — the repeatable procedure
for deriving new mappings and applications from tools you already know.
It is methodology-grade (hypothesis): each produced mapping still earns its
status individually (Contract / Empirical recipe / Hypothesis, per
mappings.md).

## Why toolbox substitution instead of brainstorming

A "be creative with the docs" prompt fails the same way for humans and
models: the concept is new, meaning hasn't been built. But every
practitioner owns a deep toolbox of methods that ARE in distribution —
statistics, decision theory, discrete math, operations research, signal
detection, psychology, game theory, logic, safety engineering. Software
is one place those methods live, not the only one (`mental-models.md`).
Jev's three primitives (a calibrated probability for a proposition; a
distribution over a fixed option set; an expectation over an ordered
rubric; all evaluated in parallel over one state) are narrow, so the
productive question is the inverse of "what can Jev do": **"which
component of a method I already trust is exactly a fast semantic
judgment over a fixed answer space, given a state?"** Swap that
component; keep the rest of the method in code.

## The sweep procedure

1. **Pin the primitive facts you're mapping TO** (verify live each pass):
   calibrated P(proposition) with no separate confidence (Noul); winner +
   full distribution + confidence, 1–255 options (Choice); probability-
   weighted expectation over 2–10 levels (Score); every question in one
   request sees the same state and is judged independently; ~70–500ms,
   ~$0.0004/case, output tokens free; 64k combined envelope; no generation,
   no arithmetic, no date math, calibration only in-distribution.
2. **Inventory a toolbox family** — one at a time: statistics, decision
   theory, signal processing, operations research, discrete math, game
   theory, experimental design, physics/measurement, psychometrics,
   behavioral economics. For each family, list its canonical components.
3. **Test each component for a judgment-shaped hole**: a step that (a) a
   knowledgeable person answers in ~a second given the right context, (b)
   has a closed answer space, (c) doesn't require derivation, counting, or
   arithmetic. That hole is substitutable with a Jev call; everything else
   stays deterministic.
4. **Classify the substitution** before writing code:
   - *Direct substitute* — the method was feasible but clunky (LLM judge,
     hand-tuned rule, manual review). Marginal win.
   - *Newly feasible* — the method was KNOWN but economically impossible:
     100–150× cost/latency per judgment is the unlock. These are the
     high-yield applications (MCTS value estimation, per-artifact context
     sieving, per-claim citation checks, 10 Hz-ish game judgment).
   - *Invalid* — violates a boundary (see below). Record it as a rejection,
     not a failure to imagine.
5. **Check the named-methods catalog** (`references/methods-catalog.md`)
   for prior art on the specific operator/theorem/algorithm before assuming
   the mapping is new — including the operators-and-theorems tier with its
   precondition rule (no named precondition = metaphor, not mapping).
6. **Compose and falsify**: build the decision card, define the falsifying
   experiment (mappings.md format), test on labeled data.

## Substitution patterns per family (seeded from launch-week evidence)

| Family | Component → Jev shape | Status |
|---|---|---|
| Statistics: ensemble/ variance reduction | Self-consistency: repeat the same judgment N times over one state; use entropy/disagreement across repeats as a review signal (cheap because output tokens are free) | **Empirical recipe** (self-consistency cookbooks, jev-1.13.0) |
| Statistics: judge variance | Repeated judgments over frozen outputs to qualify ANY judge before its numbers are trusted; Jev judge spread 224–279× lower than a GPT judge | **Empirical recipe** (jev-as-a-judge) |
| Decision theory: Neyman–Pearson | One threshold per action scaled to error cost; abstention path | **Contract + empirical** (confidence-routing; pi-jev thresholds) |
| Statistics: point estimation | Score expectation as an estimate — but read the full distribution beside it ([0,1,0] vs [.5,0,.5] both = 1.0) | **Contract** |
| Probabilistic method: priors | Choice distribution as P(s,a) policy prior (MCTS/PUCT); Choice confidences as calibrated gating | **Empirical recipe** (jev-mcts, calibrated vs exact truth) |
| Search: value function | Score rubric as leaf value V(s) — only where a simulator validates outcomes; speculative depth hard-capped at 2 | **Empirical recipe** (jev-mcts fidelity split) |
| Measurement theory: probe vs estimate | Only post-execution probes concede milestones; model estimates never do — "estimation wearing a measurement costume" is the rejection template | **Empirical recipe** (jev-mcts, pi-warden done-check) |
| Experimental design: perturbation | Behavioral tests as the stats layer: candidate removal, option-order shuffle, letter-shuffle on screenshot Choice, distractor injection, boundary cases | **Contract-level** (validation.md); letter-shuffle receipt: blackwood-rlcd 0.133 vs Jev 1.13 0.587 on 300 web steps (`notes.md` §46) |
| Experimental design: frozen protocol bake-off | Decision-model vs constrained LLMs vs deterministic baselines; accuracy + ECE + latency + cost + honesty; raw logs; recompute | **Empirical as Harbor/jevals practice** (DMB v2; jevals-data CC-BY-4.0 boards + JSONL; `notes.md` §49). Do not merge Banking77 across protocols |
| Experimental design: pre-registered AMBIGUOUS eval | Kill/go printed; cascade margin sensitivity; AUROC ≠ ECE; serving-path ≠ model-speed; same-day errata | **Empirical as Harbor/jevals practice (honest negative)** (jev-baselines-eval; cascade sign-flip; confidence=1.0 theater; encoder-with-labels; `notes.md` §55) |
| Experimental design: extractable-from-state axis | Same question with vs without a supporting passage; citation paraphrase vs reversed-meaning | **Empirical as a boundary map** (jev-capability-atlas history suite N=3; `notes.md` §49). Qualitative, not a knowledge-breadth estimate |
| Experimental design: combinatorial negative | Cell-wise Choice assembly of a grid vs extractive keep/drop | **Empirical as a negative** (ARC-AGI Direct Jev 4/400; `notes.md` §49) |
| Experimental design: collab arms | `llm_autonomous` vs `scripted_plus_jev` vs `llm_plus_jev`; Wilson + McNemar; the decision model is **not** a peer arm | **Empirical as a harness shape** (jev-testbench; bake into jevals/Harbor, `notes.md` §48) |
| Experimental design: Harbor on/off routing | Same coding-agent task with routing on vs off; hidden verifier; cheaper unsolved is not a saving | **Empirical as a *shape* and one-run signal** (jev-gateway-bench; `notes.md` §51). Pair CI merge-gate with Harbor + rh-guard |
| Discrete math: width vs depth | Fan out in width (parallel ≈ free), pay depth linearly; two-stage only when next options depend on an earlier answer | **Empirical recipe** (fan-out: 12.2× cheaper, 10× faster) |
| Psychology: Kahneman | System 2 generates/proposes (LLM), System 1 discriminates (Jev); never the reverse. S1 keeps control; optional S2 is one-use advice and does not fly. Productized cascade: `conf ≥ τ` → S1 decides else S2 writes; routing fails open / safety fails closed; **routing accuracy unmeasured**; keyword fallback ≠ S1. **Harbor-shaped cousin:** decide→policy→LLM leftover with three compare arms on labelled emails (jav-email-cascade; Noul 0.5 never rounded; mock gen-json flat-confidence is *their mock*). S1 specialists + S2 coordinator is the same split (reification-labs/foreman is description-only Phoenix scaffold this pass — do not invent an Elixir API). Indexer: S1 GLiNER extract on the bulk, escalate LLM on the tail (10–50× unfilled). Healthcare: S1 remainder after NEWS2/code, S2 blinded review (explore-typesafe-ai; synthetic; not clinically validated) | **Empirical recipe** (mcts-agent role split; 2026-09-18 mixed-architecture discourse; jev-reflex-autonomy-lab as a control-loop shape, `notes.md` §46; [dual-process-ai](https://github.com/taro1985/dual-process-ai) as a business/life cascade, `notes.md` §49; s1-graphify-indexer, `notes.md` §51; explore-typesafe-ai, `notes.md` §55; jav-email-cascade, `notes.md` §60). **Route ≠ memory:** a cheap intent gate skips memory/tool *tours* on easy routes; memory still writes; complex still searches (jev-hermes, `notes.md` §48) |
| IR / cascades | Cheap relevance / irrelevance before an expensive ranker or generator | **Empirical recipe** (RAG cookbook; jevprune; git-jev-stage; LlamaIndex Jev rerank; jev-pruner stdout after size/format envelope, `notes.md` §53). **Empirical as architecture** (decision-native-rag-skills retrieve-wide→decide→evidence-set; Hypothesis as a measured win, `notes.md` §55). **Empirical as README** (jev-sift classify-first MCP; mocks ≠ accuracy; errors/truncation ≠ irrelevant, `notes.md` §56). **Empirical as stripped-repo card** (jevgrep 79% top-5 vs BM25 40% / grep 20%; keyword still wins exact strings, `notes.md` §58). **Empirical as one-run** (Jev-RAG ≥70% cost / 72% latency vs Spark *rerank*; full-context Spark still faster, `notes.md` §58). **Empirical as line meaning-grep** (jev-semgrep AND/OR/NOT JP↔EN; 0.94/0.98 *theirs*, `notes.md` §61). **Empirical as evidence packets** (jevex 1/8→6/8 n=8; packet HitFile diagnostic, `notes.md` §61; **n=16** 160s→69s, `notes.md` §72) |
| IR / extractive keep-drop | Number candidates in code; model selects; copy verbatim; `redecide` thresholds on the log with no new calls. Compaction: same pointer job on tool results (Jev Noul/Score *or* GLiNER encoder). Computer-use: same pointer job on observed a11y/DOM controls (Jev *or* GLiNER2 *or* Cua-S1 option-attention *or* Stagehand harness pick *or* closed-vote JevOnly / host-owned waymode *or* ego-jev indexed viewport). Stdout: same pointer job on Bash chunks after a hard envelope (Jev Noul). Showcase: score-among-observed (ads, on-screen posts). **Evidence-synthesis two-pass:** relative Choice then absolute Noul; *Not found* is an answer; human tick never overwritten (**choxos/jev-reviewer**, ≠ egma-ai) | **Empirical recipe** (testimonial-miner; jev-reviewer pointer-not-generator, `notes.md` §48; gliner25-compaction char-offset + fail-closed keep_full, `notes.md` §50; gliner2-ultrafast observe→score→act, `notes.md` §52; jev-pruner, `notes.md` §53; cua-s1 specialist form, source-only, `notes.md` §54). **Empirical as PR body** Stagehand #2955 pick-and-copy (37/75 no-LLM ~0.5s vs 4.37s *theirs*; pick ≠ replacement, `notes.md` §57). **Empirical as README architecture** JevOnly no planner / waymode host-owned (`notes.md` §61). **Empirical as n=3 medians** ego-jev hot-click (~2× vs per-step LLM; not a bench; `notes.md` §65). **Empirical as one-session bench** jev-compactor 64.5%/366ms (`notes.md` §65); later product-arm **73%**/350ms/4 of 4 (`notes.md` §68). **Empirical as 500-trajectory bench** dizk/jev-lens 79% fewer tokens (`notes.md` §68). **Empirical as README** pi-om keep/kind verbatim (`notes.md` §68). Atlas class pattern: Your Signal / Near Here (`notes.md` §56). **Empirical as README delta** choxos/jev-reviewer **12★** two-pass / 18-q **4.6 s / $0.0101** *theirs*; human check is the product (`notes.md` §74) |
| Spec / lint | Project-defined semantic rules as predicates over a diff; linter owns hard rules. AST remainder: Tree-sitter units, then typed questions; do not execute scanned code. Plain-English PR check: one condition + min-confidence; fail-closed on error. Skills→oxlint: AST/precheck prove, guidance whole-file in state, remainder judged — not a hard gate. **Sentence-as-rule:** ast-grep subjects × Jev `ask:` (mizchi/jevlint; 13/15 1.00/1.00 *theirs*; fail-open no-verdict; ≠ huntedman/JevLint) | **Empirical recipe** (jev-pref contract; Abide productized path — replay 93 sessions, edit precision ~26% / turn ~73% before tune, `notes.md` §47; JevLint file-level Noul; pi-warden; snifftest unsure-band; jevscan AST∩semantic, `tenbin` owns the lint skill, `notes.md` §48; if-ai, `notes.md` §51). **Empirical as Phoenix experiment** (jev-oxlint fixtures agree with the human answer key; routing sharp; coarse hint not, `notes.md` §58). **Empirical as 13/15 corpus** (mizchi/jevlint, `notes.md` §70). jev-marshal is Watch / empty this pass |
| Formal methods / DST / safety | Judgment triages counterexamples, failing seeds, and named-rule conformance; proof/MC/DST stay with their tools. Alloy finder ≠ Apalache BMC ≠ Quint run. DST trio: Antithesis hypervisor / Resonate HQ Lean+oracle+SDK (durable async) / PufferLib env+seed. Noul is a sensor, not a discharged PO. Semi-formal diagrams are vocabularies, not enforcers. Eval integrity: check the instrument, not just the score. Effect contracts, not surface tokens. **TLA+ compose:** protocol in TLC, oracle is Jev, escalate is the valve (never confidently wrong). **Coverage ledger:** exception queue visible; mint ≠ product brain | **Hypothesis as product**, **Contract** as ownership (matching `mappings.md` §8 and `methods-catalog.md`; worked shape pi-warden — `formal-methods.md`, `formal-semi-formal.md`). **Empirical as FINDINGS ledger** (dinostomp; 99 of 189 against itself; `dinostomp jev` if-statement hygiene; `notes.md` §62). **Empirical as certification** (construct-auto-classifier; privilege ≠ verdict; landed-script / headless≠auto-approve; `notes.md` §63, §68). **Empirical as TLC + chaos table** (jev-labs; 1,080 golden 0 wrong *theirs*; `notes.md` §67). **Empirical as README** (seal; `notes.md` §67) |
| Decision analysis: VOI | Gather as an enumerated act; pay iff expected decision-loss drop > cost. Wake/resume: skip the LLM turn only if the judge answers and p is low (Horvitz); user-message / skip-limit already answer without a model. Selective memory: score a verbatim ledger; dump on failure; never judge the rules. Classify-first: pay for a full agent open iff relevance might change the act. **Specialist vs few-shot:** pay for a local head iff downstream *reads* p (Domain-jev-maker). **Training-data VOI:** pay for teacher/human labels iff confidence says they change the outcome (jev-triage); do not distill Jev as teacher. **Decision-model latency cost:** pay for sync Jev on a router iff quality gains beat hundreds of ms tail (slo-router negative). **Human-review VOI:** pay for a look iff the filter is unsure (jev-lens; never green unless sure). **Skill-library VOI:** pay to load a skill iff it changes the next step (skillranker; abstention first-class). **Same-intent cache:** pay for the LLM iff intent is new (jevcache 0 FP/100). **Human-feed VOI:** pay for a click iff worth-your-attention (ThinkyMiner/Winnow; ≠ kevinpita/winnow). **Second-call VOI:** pay for the narrating main-model turn iff generation is still required (hermes-jev-router). **Hunk-review VOI:** pay for generative review of a hunk iff Jev says it is worth looking at (prune-review; safety escarpment always keeps concurrency/auth/a11y/startup; ~20% cost target). **Intent-search VOI:** pay to judge a place the diff did not touch (jev-intent-review; UNKNOWN cheaper than false VERIFIED). **No-text-step VOI:** pay the LLM only when writing is the job (jev-use 186 vs 2,672 ms). **Batch ranking VOI:** one request per ten (jevfeed). **Empty compact-proxy skip:** IPECTER slogan only | **Hypothesis** as calculator (`mappings.md` §6; `mental-models.md`). wakegate 21/21 is smoke (`notes.md` §51). carryforward 9×3 is a hint (`notes.md` §55). jev-sift mocks ≠ accuracy (`notes.md` §56). Domain-jev-maker is Empirical as their RESULTS.md (`notes.md` §60). jev-triage is Empirical as README architecture (`notes.md` §61). **Empirical as a *negative*** (slo-router p95 77.93→490.38 same routes; `notes.md` §63). **Empirical as README** (jev-lens never blocks; `notes.md` §63). **Empirical as README** (skillranker 52★; hook fail-open; `notes.md` §66). **Empirical as eval finding** (carryforward 0/4; tools≠use; `notes.md` §68). **Empirical as 500-trajectory** (dizk/jev-lens compress-before-first-send; `notes.md` §68). **Empirical as n=100** (jevcache 0 FP; `notes.md` §69). **Empirical as unreviewed goldens** (ThinkyMiner/Winnow 80%/90%; `notes.md` §69). **Empirical as 22-run cost** (prune-review 1.18% with 305% outlier *theirs*; `notes.md` §70). **Empirical as CLI** (jev-intent-review; `notes.md` §70). **Empirical as 95-call card** (jev-use; `notes.md` §71). **Empirical as README** (jevfeed; `notes.md` §71). **Empirical as n=16** (jevex; `notes.md` §72). **Empirical as 13 labelled** (commitjev; `notes.md` §72). **Empirical as latency table** (pi-jev-compact; `notes.md` §72). **Empty skip** (IPECTER runway; `notes.md` §72). **Empirical as README** (classifier-dev escalate-under-threshold; `notes.md` §73) |
| Signal detection | Noul as evidence variable; criterion from costs and base rate; ROC/PR on your labels. Operator owns the criterion; a plugin must not self-tune the safety bar. Exactness raises a quality floor — it must not override capability. Privilege ≠ verdict. Ranking ≠ calibration: never hard-threshold raw p as a frequency. **Sureness:** inspect the vector (entropy/margin), not only max_prob. **Conflict ≠ ignorance:** name those states as Choice options. **BBQ:** stereotype/uncertainty/cost as one card; not a general bias cert. **Dual-channel ECE:** correctness-head ≠ distribution ECE; like-for-like before a 15× badge. **Escalate-under-threshold:** smart re-asks single-label <0.7; multi-label ignores (classifier-dev; 0.7 is *theirs*) | **Hypothesis** for non-SWE plots (`mappings.md` §7). **Empirical as measured OMP suppression** (omp-greenlight default 40.9% / 0 of 94 on labelled corpus; live traffic unlabelled; `notes.md` §62). **Empirical as live analysis** (slo-router exactness floor; 3/8 label disagreements did not change routes; `notes.md` §63). **Empirical as certification** (construct-auto-classifier; `sudo status` can be safe; `notes.md` §63). **Empirical as 8,000-judgment audit** (does-jev-confidence; AUC ~0.91; stated ~75% vs human ~10%; `notes.md` §64). **Empirical as 60-q library** (how-sure-is-jev; Choice confidence = max_prob; `notes.md` §67). **Empirical as HA measurements** (HA-Jev; not for locks; `notes.md` §68). **Empirical as owner-run smoke** (jev-preflight fail-open attention; `notes.md` §68). **Empirical as NCML field note** (typed-evaluation-collapse; `notes.md` §69). **Empirical as full BBQ** (jev-bbq-experiment 97.28%/0.04/0.34/$0.3429 *theirs*; `notes.md` §70). **Hypothesis until independent run** (openJev-verdict-2.0 + PR #1; `notes.md` §71). **Empirical as 13 labelled** (commitjev middle band; `notes.md` §72). **Empirical as MASSIVE** (laya-multilingual confident-wrong OOD; `notes.md` §72). **Empirical as GUI 336** (chakuho coverage ≠ correctness; `notes.md` §72). **Empirical as Hub eval** (schema-scorer peaked ranking; `notes.md` §72) |
| Safety engineering: STPA | Sensor ≠ constraint; table of unsafe control actions if the sensor lies. Host deny stays above Jev prompt-suppression. Judgment ≠ permission. Contracts on effects, not tokens. Attention filter ≠ permission gate. **Jev supplies evidence, code owns authority**. **Turnstile:** policy first, Jev remainder, replay. **SEAL:** coverage ledger; no silent advance. **Never confidently wrong:** escalate instead of hard-gate. **Typed baton:** escalate/continue/abort; gate never grants. **Persist constraints:** conversational policy survives compaction; Jev never writes it (pi-heed). **Pi control plane:** named sensors; GUI never force-click (pi-jev-control). **jev-use gate:** fail-open deny/ask. **Silent FALLBACK:** digest names the model that answered (classifier-dev granite F1 0.546 vs advertised ~0.800 *theirs*; rh-guard owns the gate) | **Contract** as ownership (`mappings.md` §8; Leveson). **Empirical as architecture** (interlock: Jev SENSOR, policy.py constraint, secrets never in agent; type-safe ≠ correct; `notes.md` §59). **Empirical as measured suppression** (omp-greenlight: not a sandbox; operator owns bar; `notes.md` §62). **Hypothesis / outline** (skill-broker: Jev never grants access; sibling to turnstile/skillranker; `notes.md` §62, §67). **Empirical as certification** (construct-auto-classifier: effect contracts; fail-closed; `notes.md` §63). **Empirical as README** (jev-lens: never blocks the agent; `notes.md` §63). **Empirical as slogan** (actiongate-jev: positive p never overrides a deterministic failure; `notes.md` §64). **Empirical as README** (turnstile: evidence ≠ authority + replay; `notes.md` §66). **Empirical as TLC + chaos** (jev-labs; `notes.md` §67). **Empirical as README** (seal; `notes.md` §67). **Empirical as README** (jev-handoff: gate never grants; fail-open; `notes.md` §69). **Empirical as 79-session bench** (pi-heed 98.5%/0 false block *theirs*; `notes.md` §70). **Empirical as README** (pi-jev-control / jev-use; `notes.md` §71). **Empirical as README** (mailordinal inbox policy; `notes.md` §72). **Identity lock** (hermes-plugin-jev is Agnes not TypeSafe; `notes.md` §72) |
| Experimental design: native-probability arena | Analytic worlds; Brier/ECE/reliability; fan-out as measurement economics; teeth stubs | **Empirical as their live card** (jev-arena 145 noul Brier 0.0059 / ECE 0.0620; sonar/vickrey/bracket suite; `notes.md` §59) |
| Experimental design: evidence-gated question packs | Pack.yaml + golden cases + evidence.md; pin version; no numbers → not verified. Runner: record/replay CI offline (accuracy/ECE/Brier/cost/latency; exit 0/1/2; McNemar) | **Empirical as registry + runner** (jev-packs nine packs *theirs*; **jevassert LANDED**; 2,990-case matrix Jev/Sonnet 5 accuracy tie, Jev better calibrated 7/9, ~250× cheaper; sms-spam 0.953/0.040; `notes.md` §64, §70). **Hunch:** measurement owns endorsement |
| Experimental design: failure-finding arena | BYOK pairwise harness; find wrong questions, do not crown a winner | **Empirical as runnable harness** (chenmingtang830/jevarena ≠ meetr1912/jev-arena; not measured findings; `notes.md` §70) |
| Experimental design: BBQ stereotype/uncertainty/cost | Full 58,492; amb vs inf; bias + $ + latency; not a general bias cert | **Empirical as full-set card** (jev-bbq-experiment 97.28%/0.04/0.34/$0.3429 *theirs*; `notes.md` §70) |
| Experimental design: Harbor SGR-judge contract | Frozen Jev vs schema-guided LLM judges; invalid = FN; cost/latency; incomplete ≠ headline | **Empirical as contract, not a score** (jev-judge-bench; 21 offline tests; canaries ≠ quality; **no quality headline yet**; ≠ jevarena/jevbench; `notes.md` §71) |
| Experimental design: recipe samples vs benches | Handmade 16–36; authors declare not-a-bench; cost/latency still reportable | **Empirical as recipe atlas** (jev-cookbook 425/$0.015; browser 5/6 *theirs*; `notes.md` §71) |
| Experimental design: competing NAR claim-audit | Like-for-like ECE; n/CI; throughput ≠ latency; vendor-baseline rows named | **Hypothesis until independent run** (openJev-verdict-2.0 77.10%/0.0636/0.0144 *theirs* + PR #1; ≠ IamBusy/OpenJev; `notes.md` §71) |
| Experimental design: 1-token logprob vs hosted Jev | Coverage ≠ correctness; `__none__` gold; shuffle/mix; numeric-rule probe | **Empirical as 336-case GUI + mario** (chakuho; `notes.md` §72) |
| Experimental design: replica engine argmax-parity | Speedup at 100% argmax; family adapters; MPS-only honesty | **Empirical as README** (jevinf 2.57×/2.27×; `notes.md` §72) |
| Experimental design: files-to-read n=16 | Same cheap agent both arms; 90s-cap finish; keep older n=8 | **Empirical as author-run** (jevex; `notes.md` §72) |
| Experimental design: commit middle-band | Three-way criterion; regex first; small clean control named | **Empirical as 13 labelled** (commitjev; `notes.md` §72) |
| Experimental design: language OOD / confident-wrong | Script-route before p; MASSIVE + XNLI; T refit | **Empirical as Hub card** (laya-multilingual; `notes.md` §72) |
| Experimental design: schema-conditioned encoder | Grouped softmax; peaked p = ranking; Hub-only if GitHub 404 | **Empirical as Hub eval** (schema-scorer v2 0.841; `notes.md` §72) |
| Experimental design: public vs_jev + named caveats | Tracked JSON on the site; read eval/README; train-on-test n=7 honesty | **Empirical as eval/README** (classifier-dev F1 0.887 / 230–232 ms; AG News 87.7%; granite 0.546 vs advertised 0.800 *theirs*; `notes.md` §73) |
| Experimental design: prompted-JSON local bake-off | Same engine, five backbones; AG News/BoolQ/SST-5; two input lengths; caveats first | **Empirical as evaluation-results-2026-09-18** (githubnext/localjev 1,200 req; Qwen3.6 76.7% / Gemma 26B 75.0% / DiffusionGemma 74.2% short *theirs*; not logits; not calibrated; `notes.md` §75) |
| Experimental design: ranking vs calibration on human labels | AUC vs ECE/Brier vs annotator rates; Platt/isotonic held-out; wording as a factor | **Empirical as 8,000-judgment audit** (does-jev-confidence; stated ~75% vs human ~10%; ~96% ECE removed; jevcal ~100 rows; `notes.md` §64) |
| Experimental design: OOD calibration / sign by type | Unknowable policy label; ECE/floor; refit T per Choice/Score/Noul | **Empirical as 900-ticket table** (jev-ood-calibration; priority 44.7%/mean p 0.74/T 3.40; boolean T 0.66; `notes.md` §66) |
| Experimental design: thinking-budget bake-off | Frozen 100-task set; attach reasoning budget; intervals | **Empirical as exploratory release** (jev-frontier-100; Jev 77.0% vs 4B/2048 96.7%; not preregistered; `notes.md` §66) |
| Experimental design: scored Jev-class bake-off | Capability/Speed/Cost composite; calibration off the rank; native vs verbalized | **Empirical as v1.1 artifact** (jevbench; Main Score 0.6/0.2/0.2; Jev 1.13.0 87.6 *theirs*; unofficial; `notes.md` §67) |
| Experimental design: pointer compact vs LLM summarize | Saved tokens vs invented paths vs early-fact recall vs latency/cost | **Empirical as product-arm table** (jev-compactor later **73%**/350ms/4 of 4 vs shipped summarizers; earlier vs-Sonnet 64.5%/366ms; `notes.md` §65, §68) |
| Experimental design: pre-send views vs post-send prune | Tokens before first send; cache cost; harm on later edits | **Empirical as 500-trajectory** (dizk/jev-lens 79% fewer; post-send +17% cost; `notes.md` §68) |
| Product decision: independent open-Jev class | Finite-choice+prob without TypeSafe; wire-compat ≠ replica. **Replica substrates** (design, not vendor-lock): Rust/WebGPU (grande), Clojure/Jolt Laya (laya-jolt byte parity), CPU SemIf (leesk212/JEV-CPU; Meanblock 404), ONNX ModernBERT (local-jev measured not equivalent), GLiNER2 spec (Eran-BA; spec ≠ jeff). **Prompted-JSON wire** (githubnext/localjev; **≠** kunchenguid/local-jev; wire-compat ≠ logit-equiv vs razorback16/openjev). **Competing NAR claims** are an audit object (openJev-verdict-2.0; ≠ IamBusy/OpenJev) | **Empirical as their docs** (openvons LM 0.916 vs 27B 0.875; JevPick 3.2–4.8×; `notes.md` §68). **Empirical as RESULTS.md** (IamBusy/OpenJev 45/60 `/v1/decide` ≠ drop-in; `notes.md` §69). **Empirical as latency table** (semif-serve 1164 vs 178 ms; runoff ≠ softmax; `notes.md` §69). **Empirical as JGLUE + isolation** (grande JNLI 0.614 ECE 0.088 T=2.81 / JCQA 0.853 / 270M 0.710/0.710 *theirs*; `notes.md` §70). **Empirical as byte parity** (laya-jolt; `notes.md` §70). **Empirical as 136-ckpt** (local-jev done 30%/shape 57%; `notes.md` §70). **Empirical as README + 1,200-req eval** (githubnext/localjev **261★**; Qwen3.6 76.7% / Gemma 26B 75.0% / DiffusionGemma 74.2% short *theirs*; not calibrated; `notes.md` §75). **Hypothesis until independent run** (openJev-verdict-2.0 + PR #1; `notes.md` §71) |
| Experimental design: same-intent cache vs cosine | False-positive rate of admitting a cached completion | **Empirical as n=100** (jevcache Jev 0 FP vs Jaccard@0.35 fpr 0.48; `notes.md` §69) |
| Experimental design: zeroshot vs BERT-family | Acc/AUC vs clean `-c`; contamination DiD; label-equivalence | **Empirical as 7-set table** (jev-zeroshot-vs-bert +0.05–+0.13; ~230 / >2048 labels; `notes.md` §69) |
| Experimental design: conflict vs ignorance schema | Noul collapse vs named Choice escape vs binary lexical bias | **Empirical as NCML field note v0.3** (typed-evaluation-collapse; `notes.md` §69) |
| Experimental design: BM25 vs Jev skill routing | Roster size 50–500; hit / miss / false_load | **Empirical as harness, not a score** (pi-jev-skill-bench 43 gold; no live numbers this pass; `notes.md` §69) |
| Experimental design: ranking family on soft scores | Pairwise inversion / Score ordinality / two-decimal ties; request-shape as a factor | **Empirical as independent measurement** (jev-orderby-bench six gates; Score 0.143 weak link; recodelabs batch-40 fails ranking; calibration ≠ sortable; `notes.md` §60) |
| Product decision: wire-compat backend | Self-host the System One *wire* on an encoder when GPU economics beat hosted and the accuracy gap is acceptable | **Empirical as their RESULTS.md** (jeff GLiFormer ~6× L4 HTTP / ~24× A10G direct; AG News 75.5% vs 90.5%; CPU more expensive; not a Jev replica; `notes.md` §60) |
| Constrained-AR PCD vs calibrated decide | O(1) schema-valid speed is not a Noul | **Empirical as their n=50 table** (system-one-benchmark; Jev 84.0% / Brier 0.1096 vs local MLX PCD 52% / 0.3884; `notes.md` §61) |
| Optimizer vs control plane | Ax/DSPy climb LM knobs; typed deterministic plane around the program; DSPy drafts AFTER route+action | **Empirical as architecture** (jev-dspy-control-plane; offline stubs ≠ quality; `notes.md` §59) |
| Bandits / RL | Value from observed rewards only — Jev provides none; rejected without an environment. PufferLib Ocean is a trainer contract, not a baseline | **Rejected** (standing boundary) |

Invalid-but-tempting (record these so they don't get rediscovered): treating
parallel Noul answers as independent evidence and multiplying them into a
joint probability (they share the state); Jev as p-value (Noul is a belief,
not a test statistic); cross-question Score comparability without a shared,
versioned rubric; using calibration to certify an individual answer
(calibration describes groups, not cases); treating Jev as a stack
replacement for an LLM (mixed architecture is the default —
`references/mixed-architecture.md`); treating a Noul as a proof, a
model-check, or a DST property (`references/formal-methods.md`);
TOCTOU-of-Noul as authorize; tautological spec + "looks good";
PufferLib Ocean scores as a comparative baseline.

## The application-finding procedure (top-down, domain-first)

1. **Enumerate decision points** in the workflow: every place a human would
   glance and answer in a second, or where a boolean/enum/rank sits in code
   behind hand-tuned rules, regexes, or "we check it manually."
2. **Apply the economics inversion**: for each, ask "what method would I use
   if this judgment cost ~$0.0004 and ~100ms instead of seconds and cents?"
   The answers you'd previously discard as too expensive (per-block context
   judgments, per-claim citation checks, per-candidate gates) are the
   applications — that is the rethink, not re-running old prompts cheaper.
3. **Classify each decision point**: exact → code; semantic judgment → Jev;
   generation → LLM (after Jev routes/filters/verifies); irreversible or
   uncertain → human. Assign per-action thresholds from error costs.
4. **Shape the state**: one request's questions must be answerable from the
   state as given — filter to what each judgment needs (context rot is
   measured), keep arithmetic/dates in code, name state paths explicitly.
5. **Falsify**: held-out labels, thresholds selected on split A reported on
   split B, judge-variance check if a Jev judge is part of the loop, and the
   behavioral perturbation tests. A use-case passes when its falsifying
   experiment fails to reject it.

## The second generator: the composition algebra
(`references/composition-algebra.md`) crosses positions (operand, gate,
post-judge, selector, comparator, prior, estimator/controller, metric,
verifier, discretizer, terminator) × known constructs — each cell checkable
against a governing rule, filtered by the economics inversion, falsified
before promotion. Use it with the sweep: the sweep asks "is there a
judgment-shaped hole?"; the algebra asks "where could one sit?"

## Escalation for very new problem shapes

When the shape doesn't match any worked mapping (e.g. a 10k-candidate
decomposition, a streaming judgment problem), don't prompt for creativity —
escalate to the closest *classical* method (search, screening, cascades,
importance sampling) and redo step 3 of the sweep on it. The library of
mappings grows one falsified card at a time; a card enters mappings.md only
with an acceptance test that ran.
