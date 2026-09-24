# ExoPO position paper: prior art and thesis stress test

Lane: ExoPO prior art. Date: 2026-09-23. Status: **confidential 0.8.0 work, local only.** Nothing
here was posted, pushed, or filed. Scratch packet: `research/080/tmp/exopo/`.

Working title under review: *When the Model Is Not the Policy: Exogenous Policy Optimization for
Agents That Act* (ExoPO). The thesis, as stated by the maintainer: for agents that act, keep the
decision policy outside the weights. That means explicit, cost-derived and authority-bounded, with
models treated as measured instruments. Placement and policy are then optimized against
complete-episode outcomes, with incumbent-challenger acceptance on untouched data. DPO-family
methods are right where preference is the product. The paper must give an operational test for
*when* the policy should be exogenous.

Evidence labels follow `research/protocol.md`:

- **Contract**: documented interfaces.
- **Reported**: third-party numbers.
- **Reproduced**: our own executed artifact.
- **Hypothesis**: our inference or proposal.
- **Unknown**.

Stars and downloads are observations only.

---

## 0. Bottom line

1. **The core architectural claim is already published in 2026.** Separating the signals from the
   policy that maps them to actions, with LLMs as evidence sources and an explicit controller, is
   argued by several papers:
   - Sun, *Decision-Centric Design for LLM Systems* (arXiv:2604.00414v1, April 2026).
   - Papamarkou et al., *Position: agentic AI orchestration should be Bayes-consistent*
     (arXiv:2605.00742v2, May 2026).
   - Amin, cost-aware Bayesian multi-LLM orchestration (arXiv:2601.01522v1).
   - Zhou et al., *Externalization in LLM Agents* (arXiv:2604.08224v1). Its §7.3 gives a
     qualitative "parametric vs. externalized" trade-off space.
   - FABLE (arXiv:2608.00215v1), an exogenous per-user policy layer around a frozen agent. It has
     a feasible set, a default-and-cost offset and anytime-valid *false-promotion control*.

   If ExoPO's headline is "the policy should be outside the model", it is **scooped and would be
   mis-positioned.** The classical lineage goes back much further: Chow 1970, Elkan 2001, and the
   Hydra policy/mechanism separation of 1975.
2. **What is still defensible as a contribution** (Hypothesis, based on the inspected sources):
   - **(a) An operational, falsifiable exogeneity test.** It works per decision family and
     includes the conditions under which the policy should *not* be exogenous (§6). No inspected
     source gives measurable conditions, each with a counterexample and a falsifier.
   - **(b) A three-layer split into instrument, decision and authority.** Authority is never an
     optimization target, and cost parameters are owned by the principal. The decision-layer papers
     and the runtime-authorization papers rarely cite each other.
   - **(c) Acceptance discipline for agents.** This means constant-policy and headroom baselines,
     complete-workflow costs, confirmation on untouched episodes, and "No Solution Found / don't
     change / don't train" as first-class exits. It is imported from HCPI, Seldonian, SPIBB and
     CSPI-MT, not invented.
   - **(d) A precise DPO boundary.** A second principle follows from it: learn *utilities* from
     preference data rather than baking in the *policy*.
   - **(e) An argument that survives the bitter lesson.** Exogeneity is justified by *who owns and
     changes the facts* (costs, authority, current state), not by model weakness.
3. **Name risk.**
   - "ExoPO" has no semantic collision on arXiv (0 hits), the Hugging Face Hub (0), PyPI (404) or
     npm (404). One exact-name GitHub repo exists: `kavinkk2425/ExoPO`, an empty placeholder
     created 2026-09-09.
   - There are close acronym neighbors in the same readership: ExO-PPO (arXiv:2602.09726, February
     2026), ExPO (arXiv:2404.16792, an alignment method), ExPO/EXPO (arXiv:2507.02834,
     arXiv:2507.07986), and **EPO, "Explicit Policy Optimization"** (arXiv:2502.12486). EPO trains
     the strategy model by RL, the opposite of ExoPO.
   - The "-PO" suffix signals a loss function to RL readers, and ExoPO is not one. This needs a
     maintainer decision.
4. **The strongest counterarguments are real and partly win.**
   - End-to-end outcome RL and general coding agents beat hand-designed scaffolding as models
     improve (Reported, arXiv:2609.03141v1 by Patel, …, Stoica, Zaharia).
   - Explicit enforcement often blocks without recovering (Reported, arXiv:2603.19328v1).
   - A policy that only sees a lossy score can be badly dominated (Reproduced toy: +57.7% regret).
   - Joint L2D training can beat two-stage exogenous deferral (Mozannar & Sontag §5.1, theory).

   The paper must concede that exogenous *scaffolding* will be absorbed, and must claim durability
   only for exogenous *commitments*: costs, authority, acceptance.
5. **Three runnable falsification experiments** fit a MacBook Air with public data (§8): a
   cost-shift test on CLINC150 and CivilComments, a handler-swap deferral test on CIFAR-10H, and an
   episode-level retrieval-control replication on HotpotQA. The replication adds the constant
   baselines that the closest prior (Sun 2026) omitted.

---

## 1. Coverage and limits

| Surface | What was done | What it establishes |
| --- | --- | --- |
| arXiv export API | 4 `id_list` batches (77 IDs; 3 mistyped guesses in batch 2 were unrelated and are not cited). 4 search batches with 41 queries, 17:03–17:23Z: name collision, "policy outside the model", policy-as-code, runtime enforcement, decision-theoretic agents, cost-sensitive deferral, SPI/Seldonian, champion–challenger, compound-AI optimization, position papers, L2D/selective prediction for LLMs, bitter lesson, exogenous-agent, harness, routing 2026, AI-control protocols, title phrases | Metadata and abstract triage of hundreds of records. Relevance-sorted with caps of 20–200 per query, so large result sets (for example 586 routing-2026 records) were triaged on the top 25–200 only |
| arXiv full text (HTML) | 10 papers fetched: 2604.00414, 2605.00742, 2609.03141, 2605.14744, 2607.25415, 2604.08224 and 2608.00215 were read at section level. 2608.11207 was read in the relevant section only. 2510.17173 and 2603.03329 were fetched but only their abstracts were used | Primary inspection, not reproduction |
| Crossref API | 8 DOIs resolved (Chow, Sha, Holmström–Milgrom, Vickers–Elkin, Thomas et al. *Science*, Hydra, Exokernel, Lakkaraju et al.) plus 2 bibliographic searches. Seto et al. 1998 was found. For Kerr 1975 only reprints were found, so it is not cited | Identity only |
| Official and web pages | Bitter Lesson essay, BAIR compound-AI post, OPA docs, Cedar docs, ASTM F3269-17 scope page, PMLR HCPI abstract, JMLR safe-RL landing page, NeurIPS 2015 tech-debt landing page, Seldonian tutorial | Landing or abstract depth with digests (fetch_log.txt) |
| Name collision | arXiv (6 queries), GitHub repositories and code search, Hugging Face models, datasets, spaces and papers, PyPI, npm, WebSearch (2 queries) | Point-in-time, 2026-09-23 about 17:20Z |
| Reused repo evidence | `research/decision-jobs-2026-09-23.md` (Chow/Elkan/Geifman/Mozannar cards), `optimizer-integration.md` and `validation.md` (current doctrine), today's patrol `wf1-patrol-methods.json` items (2609.26384, 2609.20758, 2609.24200, 2609.19942, 2609.17306, 2609.26532, 2609.12742, 2609.16793, 2410.15729) | Not re-fetched. Reused at the depth the patrol recorded |
| Local execution | `sim_exogeneity.py`, our own code (Python 3.14.7, 1.22 s), synthetic only | Reproduced arithmetic, not evidence about any model |

**Not covered:**

- OpenReview, ACL Anthology, and 2026 conference proceedings were not searched directly.
- Papers submitted on 2026-09-22 and 2026-09-23 may not be indexed yet.
- v2+ revisions were not enumerated.
- The `ti:"not the policy"` phrase query tokenized loosely (11,193 hits). No exact title match was
  seen in the top 30, but this is **not proof of absence**.
- A title search for the post-hoc L2D estimators (Narasimhan et al. 2022) returned 0. That is
  Unknown, not absence.
- The industry champion–challenger practice has no canonical source here.
- No paid search was used, and no third-party code was installed or executed.

---

## 2. Terminology the paper must fix first

- **Two meanings of "policy".** In RL and alignment (PPO, RLHF, DPO, GRPO), the policy *is* the
  model: `π_θ(y|x)`, a distribution over tokens or trajectories. DPO's own subtitle says "your
  language model is secretly a reward model" (arXiv:2305.18290v3).

  The ExoPO sense is the **decision policy** `δ(s, c, G, state) → a ∈ G(state)`. Its inputs are:
  - `s`: instrument outputs with score contracts;
  - `c`: principal-owned cost or utility parameters;
  - `G`: authority, the feasible set.

  The title's "the model is not the policy" works only if §1 of the paper states this split.
  Otherwise RL readers will read it as a category error.
- **Explicit ≠ exogenous.**
  - Deliberative Alignment (arXiv:2412.16339v2) and Constitutional AI (arXiv:2212.08073v1) write
    the policy down *and* compile it into weights.
  - Policy-as-Prompt (arXiv:2509.23994v2) keeps the policy text outside the weights but lets a
    model *interpret* it.
  - Mechanical Enforcement (arXiv:2605.14744v1) calls this a principal–agent failure, because the
    same model interprets the policy it is governed by.

  ExoPO needs **executive exogeneity**: the component that computes the action from `(s, c, G)` is
  neither trained on a fixed `c` nor the component that reads untrusted input.
- **Three meanings of "exogenous".**
  - Econometrics: determined outside the model. This matches the intent.
  - RL: exogenous state or noise the agent cannot control. See the Exo-MDP literature, e.g.
    Dietterich et al. arXiv:1806.01584v1, Sinclair et al. arXiv:2207.06272v3, and 2026 work
    (2603.02862, 2601.20694, 2606.25170). An RL reviewer may read "exogenous policy" as "a policy
    that is part of the environment".
  - Liss et al. (arXiv:2608.11207v1) already use "exogenous control" for control from outside the
    model.
- **Naming lineage worth citing.** Two OS papers are the cleanest precedent for the separation.
  Levin et al., "Policy/mechanism separation in Hydra" (SOSP 1975, doi:10.1145/800213.806531), and
  Engler et al., "Exokernel" (SOSP 1995, doi:10.1145/224056.224076).

  The transfer caveat is in §7: an LLM is *not* a policy-neutral mechanism. Its outputs embed
  trained preferences, for example refusals.

---

## 3. Prior-art map

Each row covers what the work optimizes, where its policy lives, how costs and constraints enter,
and whether it already claims the ExoPO thesis. The last column says what ExoPO adds or does not.

### 3a. Alignment and RL: the endogenous pole

| Work | Optimizes | Policy lives | Costs and constraints enter | Claims thesis? | ExoPO adds / does not |
| --- | --- | --- | --- | --- | --- |
| RLHF / PPO (Christiano et al. 1706.03741; InstructGPT 2203.02155; PPO 1707.06347) | Expected reward-model score with a KL penalty to the reference | Weights (`π_θ`) | Implicitly, via labeler rankings. KL is a soft trust region | No (the opposite) | Adds the generative-vs-decision distinction. Does not replace RLHF for output quality |
| DPO (2305.18290) | Bradley–Terry preference likelihood in closed form | Weights | Implicit in the preference pairs | No | DPO is right when the preference *is* the product (§5) |
| IPO / ΨPO (2310.12036) | A general pairwise-preference objective that avoids the pointwise-reward assumption | Weights | Implicit | No | None beyond the boundary |
| KTO (2402.01306) | A prospect-theoretic utility of generations from **binary desirable/undesirable** signals | Weights | Loss aversion is built into the loss | No | It is the closest DPO-family method to outcome labels. Note it as the strongest endogenous competitor when outcomes are binary |
| SimPO (2405.14734), ORPO (2403.07691) | Reference-free, length-normalized margin (SimPO); odds ratio fused into SFT (ORPO) | Weights | Implicit | No | None |
| SPO (Swamy et al. 2401.04056) / SPPO (2405.00675) | Minimax winner or Nash equilibrium of the preference game via self-play | Weights | Intransitive preferences handled game-theoretically | No | Name ambiguity: "SPO" also means Smart Predict-then-Optimize (1710.08005). Disambiguate in the paper |
| GRPO (DeepSeekMath 2402.03300; DeepSeek-R1 2501.12948) | Group-relative advantage on verifiable outcome rewards | Weights | Outcome reward only | No | **This also optimizes complete-episode outcomes.** ExoPO's difference from GRPO is *where costs and authority live and how acceptance works*, not "outcomes" |
| Safe RLHF (2310.12773) | Reward subject to a cost-model constraint via a Lagrangian | Weights | Constraint in expectation, multiplier tuned during training | No | Shows the soft/endogenous treatment of constraints that ExoPO contrasts with hard exogenous gates |
| Constitutional AI (2212.08073), Deliberative Alignment (2412.16339), Rule-Based Rewards (2411.01111) | Harmlessness and spec adherence via AI feedback, spec recall, or rule-graded rewards | Weights, with explicit text | Principles or rules become reward or training targets | No. Explicit but endogenous | The "explicit ≠ exogenous" category. Deliberative Alignment is the strongest evidence that an explicit spec can be executed well from weights (Reported) |
| RLSR (2607.03528v1) | Area under the risk–coverage curve as an alignment objective | Weights (endogenous abstention) | Selective-prediction metric as reward | No | A direct endogenous alternative to exogenous selective thresholds. Candidate arm for experiment 1 or 2 |

### 3b. Classical decision theory: the exogenous pole ExoPO inherits

| Work | Optimizes | Policy lives | Costs and constraints enter | Claims thesis? | ExoPO adds / does not |
| --- | --- | --- | --- | --- | --- |
| Chow 1970 (doi:10.1109/TIT.1970.1054406) | Error–reject trade-off | A threshold on the posterior, outside the classifier | A reject cost | For single classifiers, in effect | Nothing new at single-decision level. ExoPO extends it to agents with authority and handlers |
| Elkan 2001 (IJCAI; prior card) | Expected cost | Decision threshold | Cost matrix, possibly example-dependent. **Recommends thresholding at decision time over rebalancing training** (prior card, inspected prose) | Yes, for one decision: "keep cost out of training" | The formal kernel of condition X1. The dominated-row case (label-all) is a no-model exit |
| Geifman & El-Yaniv 2017 (1705.08500v2; prior card) | Selective risk at coverage, with a binomial guarantee (SGR) | A selector `g` over a ranking score | Target risk, confidence level | For selection | The acceptance math for accepted-slice risk. Not handler-inclusive |
| L2D: Madras et al. (1711.06664); Mozannar & Sontag (2006.01862v3, prior card); Charusaie et al. (2207.09584); two-stage L2D (2410.15729, 2604.27723) | System loss including handler error | Joint L2D: **in weights** (classifier and rejector trained together). Two-stage: a rejector outside a fixed predictor | Handler loss plus query cost | Two-stage variants, implicitly | **Counterexample source.** Joint training can beat two-stage under limited capacity (Mozannar & Sontag §5.1). Patrol: classic two-stage L2D did not beat baselines on real CXR data (2609.26384v1, Reported) |
| Learn-then-Test (2110.01052), Conformal Risk Control (2208.02814), KnowNo (2307.01928) | Finite-sample risk control of a threshold or set | Post-hoc parameter outside the model | Monotone loss bound (CRC) or multiple testing (LTT) | For risk control | Use LTT/CRC for *constraints* in acceptance. They control risk; they do not optimize utility |
| Decision-focused learning: SPO+ (1710.08005), Donti et al. (1703.04529), Wilder et al. (1809.05504), survey (2307.13565) | Downstream regret | **The optimizer is explicit and exogenous. The predictor is trained end-to-end on decision loss** | Optimization objective and constraints | Half: the policy (solver) is exogenous, the instrument is decision-trained | ExoPO must *allow* decision-aware instrument training while keeping policy parameters exogenous. Negative DFL results exist (2609.12752v1, patrol, Reported) |
| Policy learning with abstention (2510.19672v3); CSPI-MT (2408.12004v1) | Treatment-policy value with deferral; safe improvement for **threshold policies** with multiple testing | Explicit threshold/rule policies | Baseline-improvement guarantee | Yes, for threshold policies in econ and health | CSPI-MT is the statistical machinery ExoPO acceptance should cite for "multiple candidate thresholds vs incumbent" |

### 3c. Systems: routing, compound AI, program and harness optimization

| Work | Optimizes | Policy lives | Costs and constraints enter | Claims thesis? | ExoPO adds / does not |
| --- | --- | --- | --- | --- | --- |
| FrugalGPT (2305.05176), RouteLLM (2406.18665), Hybrid LLM (2404.14618), RouterBench (2403.12031) | Quality–cost frontier | A learned router (separate weights) plus an explicit cost threshold | Price per call, threshold | Partly: routing is a separate decision layer | Nothing algorithmic |
| 2026 routing results: routing plateau (2606.07587v1), routing collapse (2602.03478v1), signed rescue routing (2609.07786v1), Stackelberg user choice (2602.09902v1), headroom negatives (2609.19942, 2609.17306, 2609.26532; patrol) | Same | Same | Same | No | They **support** two ExoPO acceptance rules: check per-case-best headroom first, and train routers on the decision, not on scalar scores. The collapse paper names an "objective–decision mismatch". The Stackelberg analysis finds static policies without cascading optimal in nearly all cases under its model (Reported) |
| Compound AI (Zaharia et al., BAIR blog, 2024-02-18) | System-level results | Across components | Per-component | No. It argues systems beat monolithic models | ExoPO narrows the claim: the *decision* layer, not every component, should be exogenous. The same group's 2026 paper concedes that scaffolding gets absorbed (§5, C1) |
| LLM-Modulo (2402.01817v3) | Plan correctness | External sound verifiers and critics | Hard constraints via model-based verifiers | Yes, but **from model incapability** ("LLMs can't plan or verify") | ExoPO's justification is ownership, not incapability. That survives model improvement; LLM-Modulo's premise may not |
| DSPy (2310.03714), MIPRO (2406.11695), GEPA (2507.19457), TextGrad (2406.07496), Optimas (2507.03041), SysDPO (2502.17721) | A metric over program outputs by searching prompts, demos, modules and (SysDPO) weights | Program text and prompts: exogenous to weights but not decision-theoretic | Only through the metric | No | ExoPO can *use* these as search operators. It forbids searching costs and authority, and requires untouched confirmation. Negative results: prompt optimization is "a coin flip", 49% of 72 runs below zero-shot (2604.14585v2, Reported). A GEPA gain was not separable from variance, p = 0.29 (2609.12742v1, patrol, Reported) |
| Harness optimization: Meta-Harness (2603.28052v1), Hyperagents (2603.19461v1), Self-Harness (2606.09498v3), Better Harnesses, Smaller Models (2607.08938v1), HarnessForge (2606.01779v1), Co-Harness (2607.22688v1), frozen-LLM harness bandit (2607.25415v1), Harness-Bench (2605.27922v1) | Benchmark pass rate by searching harness code or configuration, sometimes co-trained with weights | Harness (exogenous). **Co-Harness and HarnessForge distill it back into weights** | Benchmark reward. Rarely principal costs or authority | Partly: "optimize placement against episode outcomes" is already done | ExoPO adds principal-owned costs, excluded authority, and acceptance. Important negative (full text read): in 2607.25415v1 an online bandit and REINFORCE over a 729-configuration harness space **lost** to a static DSPy baseline. Tool-use on Bedrock Haiku scored 96% at 285 tokens versus REINFORCE 62% at 680, with 300-episode runs plateauing at 0.61–0.65 (Reported). Start from a strong incumbent |
| TabAgent (2602.16429v1), RADEG (2608.09168v1), OPE decision heads (2510.17173v2) | Replace generative closed-set decisions with trained classifiers or heads, gated by execution utility | Separate small heads | Verifier reward, typed rewards | Yes, operationally | Direct support for the companion "train your own decision head" skill. TabAgent: about 95% latency and 85–91% cost reduction on AppWorld with task success maintained (Reported, abstract). The OPE study had 7 users and 280 turns |

### 3d. Governance, authority and assurance

| Work | Optimizes | Policy lives | Costs and constraints enter | Claims thesis? | ExoPO adds / does not |
| --- | --- | --- | --- | --- | --- |
| OPA (docs), Cedar (docs; 2403.04651v2) | Nothing: deterministic evaluation | A policy engine outside the application. OPA: "offload policy decision-making from your software" (Contract) | Rules over attributes | For authorization, yes | ExoPO's authority layer *is* policy-as-code. ExoPO adds cost-derived *decision* thresholds next to it, which OPA and Cedar do not model |
| CaMeL (2503.18813v2), Progent (2504.11703v3), AgentSpec (2503.18666v3), CapScope (2609.08371v1), SARC (2605.07728v1), Aegis (2608.16891v1), CUGA policies (2605.20874v1), Agent Behavioral Contracts (2602.22302v1), Language-Based Agent Control (2605.12863v1), CAGE (2607.29190v1) | Preventing unauthorized effects | A harness or runtime outside the model | Capabilities, typed rules, SMT constraints, quorum | **Yes, for authority** | Not novel for authority. CapScope: injected effects in 33–47 of 75 runs under ambient authority versus 3 of 75 with capabilities, with 68 of 75 repairs still completed (Reported). CAGE: pointwise gates admit false allows under binding faults. SARC argues finite reward penalties do not substitute for hard constraints |
| Mechanical Enforcement (2605.14744v1) | Governance metrics plus task MCC | Four primitives outside the "interpretive loop" | Hard gates on risk variables | Yes | MCC rose from 0.43 to 0.88 (Reported), but **ground truth is assigned by rule-based scoring** over the same variables the gates read (full text). That is circular in favor of gates; use as illustration, not evidence |
| Shielding (1708.08611), CPO (1705.10528), RCPO (1805.11074), CMDP (Altman 1999, book, not inspected) | Reward under safety constraints | Shield: exogenous. CPO/RCPO: inside the learned policy | Shield: hard temporal-logic. CPO/RCPO: constraint in expectation, Lagrangian | Shield: yes, for hard constraints | The hard/soft split maps onto ExoPO's authority/decision split. Lagrange multipliers are exactly the "cost knobs" ExoPO keeps outside the weights |
| Simplex (Seto et al. 1998, doi:10.1109/ACC.1998.703255; Sha 2001, doi:10.1109/MS.2001.936213), ASTM F3269-17 run-time assurance | Safe use of an unverified complex controller | A decision module switches to a verified safety controller | Recoverable region, timing | Yes, in control engineering | The envelope pattern for the "endogenous proposal, exogenous envelope" hybrid (§6). Transfer map in §7 |
| AI Control (2312.06942v5; protocol evaluation 2511.02997v1; Control Tax 2506.05296v3; adaptive attacks 2510.09462v2) | Safety and usefulness under intentional subversion | Protocols outside the untrusted model; thresholds set by audit budget | Audit budget, trusted-model deferral | **Yes, for adversarial settings** | ExoPO generalizes to non-adversarial cost optimization. Borrow "deny attackers the protocol internals". The best protocols raised safety from 50% to 96%. Adaptive attacks cut the resampling protocol to 17%, while deferring on critical actions stayed robust (Reported). Exogenous does not mean public |
| Informed Abstention (2606.02965v2), Oversight Has a Capacity (2606.08919v1) | Hazard blocking and usability; guard escalation with a fatiguing reviewer | Runtime guards | Asymmetric costs, reviewer load | Partly | Supports a handler model with state. The inverted-U in escalation rate is a modeling result (Reported). Reviewer agreement on "risky" was Fleiss κ = 0.52 on 125 actions |

### 3e. Acceptance: incumbent–challenger is prior art

| Work | Mechanism | ExoPO use |
| --- | --- | --- |
| HCPI (Thomas et al., ICML 2015, PMLR v37) | Returns a policy only if it clears a user-set lower bound with a set confidence (Contract, abstract) | Cite as the origin of confidence-gated policy acceptance |
| Seldonian (Thomas et al., *Science* 2019, doi:10.1126/science.aag3311; tutorial) | Candidate selection on `D_cand`, a safety test on held-out `D_safety`, otherwise **"No Solution Found (NSF)"** (tutorial text) | NSF is the formal version of "don't change / don't train" as a first-class exit |
| SPIBB (1712.06924v5) | Bootstraps to the baseline where uncertainty is high | Per-region fallback to the incumbent |
| CSPI-MT (2408.12004v1) | Multiple candidate cutoffs tested against the status quo with controlled false adoption | Exact fit for threshold-policy challengers |
| FABLE promotion (2608.00215v1, full text) | Writes back a learned preference only when an anytime confidence sequence excludes zero | A 2026 agent-specific instance. Reported τ²-bench results: 80 clusters, 240 episodes per policy; reward and alignment gains had positive CIs, and task success was unresolved. Two synthetic profiles |
| Augustus baseline | `optimizer-integration.md` already keeps authority, splits, candidate sources and the final threshold outside the search. `compare_workflows.py` computes a fixed-n Hoeffding bound | ExoPO largely formalizes existing Augustus doctrine. Say so internally; do not overclaim novelty externally |

### 3f. Economics and mechanism design

| Work | Relevance |
| --- | --- |
| Holmström & Milgrom 1991 (doi:10.1093/jleo/7.special_issue.24) | Multitask principal–agent: when some tasks are poorly measured, strong incentives on the measured ones distort effort. This gives ExoPO its *theoretical* reason not to push unmeasured obligations, such as authority and rare harms, into the optimized object. Transfer map in §7 |
| Hadfield-Menell & Hadfield, incomplete contracting (1804.04268v1); CIRL (1606.03137v4) | Reward functions are incomplete contracts, and external institutions fill gaps. That is the exogenous-policy analog |
| Goodhart variants (1803.04585v4); reward-model overoptimization (2210.10760v1) | Proxy optimization degrades the true objective. It applies to endogenous RL *and* to exogenous search on a proxy metric |
| Stackelberg routing (2602.09902v1); Experience Orchestrator (2608.11207v1); principal–agent liability (2504.03255v2) | **"Exogenous" is not "benign".** The EO paper's exogenous controller steers simulated visitors toward advisor contact (+32 pp over 60,000 simulations, Reported, LLM-simulated users). The Stackelberg analysis shows provider-optimal and user-preferred routes diverge. ExoPO must name *whose* costs the policy encodes |
| Performative prediction (2002.06673v4) | When the instrument's output changes the outcome, outcome-based evaluation of the policy is itself shifted. This is a limitation of condition X5 |
| No-free-lunch for human–AI collaboration (2411.15230v1) | Any deterministic collaboration rule that does not essentially always defer to the same agent will sometimes do worse than the least accurate agent (theorem, abstract). Constant policies must always be baselines |

---

## 4. Scoop check: 2025–2026 papers that already argue "policy outside the model"

Ranked by overlap with ExoPO. Depth is as inspected. Numbers are Reported.

| Rank | Paper | Overlap | Gap ExoPO can occupy |
| --- | --- | --- | --- |
| 1 | **Sun, Decision-Centric Design for LLM Systems**, arXiv:2604.00414v1 (IBM, 2026-04-01). Full text | Separates signals from a deterministic policy `δ(c) = argmax_{a∈F(c)} U(a,c)`, with `U = R − Σλ_k C_k`. Covers routing, inference scaling and sequential act-or-clarify. Its claim is "architectural rather than methodological" | Thresholds are preset ("no tunable parameters"). No acceptance on untouched data. No authority layer. No test of *when not* to separate. Experiments are small: 8 calendar scenarios × 10 runs, and 150 NQ questions with 50 per bucket, on Granite-4-micro and LLaMA-3-8B. **The retrieval experiment omits an always-expand baseline.** By its bucket definitions, always-expand should reach at least DC's success on the easy and medium buckets at the maximum rounds (Hypothesis, derived from the definitions). DC's advantage over constants is then in rounds, not success. The conclusion concedes that "some of the gaps we observe may narrow" with stronger models |
| 2 | **Papamarkou et al., Position: agentic AI orchestration should be Bayes-consistent**, arXiv:2605.00742v2 (2026-05). Full text | A Bayesian controller over task-level latents. LLMs are "black-box predictors", with observation models calibrated against measured outcomes and judged "on held-out tasks by calibration and decision utility". Expected-utility and value-of-information actions | No experiments (position paper). Bayesian-specific. Argues from the mismatch between LLM uncertainty and task uncertainty, not from ownership. No authority, no acceptance protocol. Concedes that prompting may suffice in short-horizon, low-stakes settings and that world models may internalize Bayes |
| 3 | **FABLE**, arXiv:2608.00215v1 (2026-07-31). Full text sections | An exogenous per-user execution-policy layer around a black-box agent. Externally supplied feasible set, fixed default-and-cost offset, Thompson sampling, anytime-valid false-promotion control, a regret bound | Personalization only. The policy is learned by a bandit rather than cost-derived. Task success unresolved on τ²-bench. Two synthetic profiles. **This is the paper most likely to be cited against ExoPO's optimization loop; engage it directly** |
| 4 | **Externalization in LLM Agents** (review), arXiv:2604.08224v1. §7.3 read | "Parametric vs. externalized" trade-off dimensions: update frequency, reuse, "auditability, governance, and alignment" ("the more consequential the agent's actions, the stronger the case"), and latency. It also notes that model improvement can "pull capability back inward" | Qualitative. No falsifiers. Scope is capability (memory, skills, protocols), not the decision policy. **ExoPO's exogeneity test must cite it and show the sharpened, measurable version** |
| 5 | Amin, Bayesian cost-aware multi-LLM orchestration, arXiv:2601.01522v1. Abstract | LLMs as likelihood models, with expected-cost actions. Claims to prove that confidence thresholding is inadequate for sequential decisions with costs. 34% cost reduction on 1,000 resumes with 5 LLMs | Label provenance is unknown at abstract depth. Hiring is a high-stakes domain with fairness claims that need scrutiny |
| 6 | Mechanical Enforcement, arXiv:2605.14744v1. Methods read | Governance outside the interpretive loop, framed as principal–agent | Circular labels (§3d). Synthetic data, one model family |
| 7 | Frozen-LLM harness bandit, 2607.25415v1; Self-Harness, 2606.09498v3; Meta-Harness, 2603.28052v1 | Optimizing the system around frozen weights against outcomes | Benchmark reward, no principal costs. The negative bandit result supports starting from an incumbent |
| 8 | Informed Abstention (2606.02965v2); Controllability position (2605.27117v1); three-layer assume-guarantee position (2605.18672v1); structural abstention (2608.13926v1) | Runtime enforcement and explicit control planes as first-class properties | Safety framing. They do not optimize a cost-derived decision policy |
| 9 | AutoHarness (2603.03329v1). Abstract | An LLM synthesizes a *code policy* that beats larger LLMs on 16 one-player TextArena games and eliminates illegal moves in 145 games | Evidence *for* exogeneity (the policy as code, written by the model), but only in games with an exact legality oracle |

**Verdict.**

- The claim "keep the decision policy outside the weights and treat LLMs as instruments" is
  **not novel in 2026.**
- "Optimize system configuration around frozen weights against outcomes" is **not novel** either.
- "Accept a challenger only if it beats the incumbent with confidence on held-out data" is
  **classical.**

The paper is still worth writing as a *synthesis-plus-test* position paper if it does three things.
It must make the exogeneity test (§6) the central contribution. It must unify the decision-layer,
authorization and SPI lines under one instrument/decision/authority vocabulary. And it must carry
at least one executed falsification experiment (§8). Leading with the architectural claim would
invite "see Sun 2026; Papamarkou et al. 2026" as the first review comment.

---

## 5. The DPO boundary: "where preference is the product"

**Proposed statement (Hypothesis).** Endogenous preference optimization (DPO, IPO, KTO, SimPO,
ORPO, SPO/SPPO) is the right tool when all of the following hold:

1. The deliverable is the output distribution itself, judged by a preference population (tone,
   helpfulness, style).
2. There is no principal-specific cost matrix, and the Bayes action does not vary across
   principals.
3. No delegated authority or irreversible effect is involved.
4. Preferences are stable relative to the retraining cycle.

Two consequences the paper can own:

- **Learn utilities, not policies.** When a preference dataset informs an *action* decision, fit
  the utility or cost model from it: Bradley–Terry, or KTO-style binary desirability. Keep that
  model as an exogenous, versioned parameter of `δ`, rather than compiling it into the actor.

  RLHF already has this structure up to the reward-model stage. ExoPO says to stop there for
  action decisions and decide at run time. The inference-time analogs are controlled decoding
  (arXiv:2310.17022v3) and best-of-n. Reward-model overoptimization (arXiv:2210.10760v1) affects
  both routes, so the acceptance rule still needs untouched outcomes.
- **Mixed case.** Per-user preferences over execution behavior sit on the boundary. FABLE handles
  them exogenously (a bandit layer); per-user fine-tuning handles them endogenously. The paper
  should call this contested, not settled.

Counterexample to a strict boundary: Deliberative Alignment executes an explicit, versioned safety
spec from weights and reports better jailbreak robustness with less overrefusal. Where the spec is
global, stable and owned by the model provider, endogenous execution is defensible. The exogeneity
test below handles this through X1 and X7.

---

## 6. Stress test and the operational exogeneity test

### 6.1 Strongest counterarguments

| # | Counterargument | Best evidence for it | Rebuttal | What the paper must concede |
| --- | --- | --- | --- | --- |
| C1 | End-to-end learning and the bitter lesson win | Sutton 2019. General coding agents with successive models beat human-designed data agents on TAG-Bench and DAB, GPT-5.6 Sol used about 4× fewer turns than o3 (2609.03141v1, Reported). DeepSeek-R1/GRPO outcome RL. Co-Harness and HarnessForge distill harnesses into weights. "Bitter lesson of misuse detection": generalist LLMs beat specialized supervisors (2507.06282v1, Reported). DFL: end-to-end instrument training helps | The bitter lesson concerns capability learnable from data available at training time. Principal-specific costs, grants, and current state are **not in any training distribution**; they belong to the principal and change. The same 2026 paper by Zaharia et al. finds that what endures is "non-parametric" context: "explicit knowledge of the working environment", which must be "editable, fresh, reliable, and human-auditable" | Exogenous *scaffolding* (decomposition, retry loops, prompt tricks) will be absorbed. Claim durability only for exogenous *commitments* (costs, authority, acceptance). Allow decision-aware instrument training (DFL-style) |
| C2 | Explicit policies are brittle | Policy loopholes: ambiguity masquerades as agent error (2609.14400v1). Verifier tax: enforcement intercepts up to 94% of non-compliant actions but safe success stays below 5% in most settings, with recovery from 21% down to about 0 (2603.19328v1, Reported). Capability-gated models: "utility does not" compose (2609.00445v1). Pointwise gates admit false allows (CAGE). Hidden tech debt (Sculley et al. 2015, not re-inspected). The expert-systems history | Brittleness in an explicit policy is *visible and attributable*: Sun's attribution argument, and the inverse of Mechanical Enforcement's "outputs appear compliant without being compliant". Keep `δ` minimal: costs, thresholds, feasibility. Semantics go to measured instruments, not rulebooks | False-block rate, recovery rate and time-to-safe-completion belong in the objective. An exogenous gate without a recovery path can lose to no gate. Attributability is a hypothesis until a diagnosis-time study exists |
| C3 | Costs are unknown | Many deployments cannot state `C_FP` and `C_FN` | Decision-curve analysis (Vickers & Elkin 2006, doi:10.1177/0272989X06295361) evaluates net benefit over a threshold range. If the action is insensitive across the plausible range, precision is unnecessary. Costs can be elicited from preferences (§5). Endogenous training does not remove costs; it **hides** them in label ratios and annotator choices | If costs are unknown *and* stable *and* outcomes are dense, learning the action mapping directly (bandit or RL) may be equal or better. The exogeneity advantage then rests only on X2 and X6 |
| C4 | Outcomes are unobservable | Selective labels (Lakkaraju et al. 2017, doi:10.1145/3097983.3098066). Queue- and complaint-based error estimates are biased, and PPI does not fix this (2609.20758v1, patrol). Shadow mode cannot observe counterfactuals. Performative prediction | This hurts endogenous training equally or more: RL on proxies is reward hacking, and RM overoptimization is documented. Exogenous separation at least isolates the proxy. Use known-probability audit samples | Without observable outcomes ExoPO **cannot claim optimization**. It reduces to explicit, human-owned, conservative policy plus audits. State this as condition X5 |
| C5 | Latency and cost overhead | Control tax (2506.05296v3); verifier tax | The layer can *reduce* cost: TabAgent reports 85–91% lower cost, and the harness-bandit paper's static incumbent was the cheapest arm | Measure the full workflow cost. Absorb the policy (X7) when overhead dominates and no other condition holds |
| C6 | Explicit policies are gameable | Adaptive attacks on trusted monitors (2510.09462v2) | Deferring on critical actions stayed robust even to adaptive attacks (2511.02997v1, Reported). Keep the decisive value off channels the attacker can write (2609.24200v1, patrol) | Exogenous ≠ public. Protocol internals may need to be secret |
| C7 | Joint training beats separation | Mozannar & Sontag §5.1 (theory). HarnessForge: harness–policy co-evolution beats harness-only and policy-only by up to 12% (Reported). JERP absorbs rules into weights | Separation is judged on *change cost* and auditability, not only static loss | Report the static-loss gap honestly. Experiment 2 can falsify |

### 6.2 Definitions for the test

For each **action family** (not each system), write the decision point `(A, x, s(x), c, G, h)`:

- `A`: actions;
- `x`: raw input;
- `s(x)`: instrument outputs with score contracts;
- `c`: principal-owned costs;
- `G`: authority and feasibility;
- `h`: handlers.

The policy is one of three kinds:

- **Endogenous**: `a = argmax π_θ(·|x)` with `c` and `G` implicit in training.
- **Exogenous**: the parameters of `δ` (`c`, thresholds, `G`, handler models) are versioned
  artifacts that change without gradient updates, and `δ` is computed by a component that neither
  reads untrusted input nor was trained on a fixed `c`.
- **Envelope hybrid**: an endogenous proposal inside an exogenous feasibility, authority and switch
  layer. This is Simplex or a shield.

### 6.3 Conditions (draft for the paper)

| Id | Condition (measurable) | Rule if it holds | Counterexample | Falsifier |
| --- | --- | --- | --- | --- |
| **X1 Cost heterogeneity or volatility** | `Δ_c`: the fraction of cases whose Bayes action changes across the plausible cost set `C` (principals, tenants, time). Compare the time between cost changes with retrain-plus-requalify time | If `Δ_c > ε` and costs change faster than retraining, costs and thresholds are exogenous inputs to an explicit Bayes or decision rule | A single stable population preference, where `Δ_c ≈ 0` and DPO-family fits. A dominated cost row, where label-all wins and no model is needed (toy §9: act-all 0.698 vs threshold 1.369) | A **cost-conditioned endogenous** policy (cost given as input) matches the explicit Bayes rule within margin on untouched data across held-out *and extrapolated* cost ratios, with no monotonicity violations. That is Experiment 1 |
| **X2 Authority, irreversibility, untrusted input** | Does the action have effects outside a sandbox, need delegated grants, or have no recoverable region, and does the deciding component read attacker-writable input? | Authority is exogenous, enforced at the effect boundary *before* the effect. It is a contract, never an optimization target. Always applies when effects exist | Read-only, reversible, sandboxed drafting, where a gate adds cost without benefit. An enforcement gate without recovery can lower safe success (verifier tax) | Under adaptive red-teaming with channel control, an endogenous-only arm produces no more unauthorized effects than the gated arm at equal task success. Existing Reported data (CapScope 33–47/75 vs 3/75) supports the rule |
| **X3 Instrument or handler heterogeneity and churn** | The number of instruments and handlers with different reliabilities, the rate of model, reviewer or tool change, and requalification cost exogenous (refit a rejector or threshold) vs endogenous (retrain) | Compose exogenously with per-instrument score contracts. Requalify the component that changed | One stable instrument with limited-capacity joint L2D beating two-stage (Mozannar & Sontag §5.1). HarnessForge's joint beating separate | Joint endogenous L2D beats two-stage exogenous by more than the margin on system loss both before *and* after a handler swap, and adapts at no greater cost. That is Experiment 2 |
| **X4 Signal sufficiency (anti-condition)** | `R_suff`: the regret of the best `δ` over exposed signals and fields versus the best end-to-end policy on the same data | If `R_suff > ε` and the missing information cannot be exposed as a field or new instrument, the decision is endogenous with an exogenous envelope for X2 | High-rate sensorimotor control where the action cannot be factored into a few signals. A counter-counterexample is AutoHarness's code policies in text games | After exposing the best available fields and instruments, end-to-end still wins by more than the margin, so keep it endogenous. The toy in §9 shows +57.7% regret when a stake field is hidden, fixed by exposing it, *not* by moving the policy in |
| **X5 Outcome observability (optimizability, not exogeneity)** | Are complete-episode outcomes observable for a known-probability sample, including auto-accepted cases, within an acceptable delay? | If yes, optimize (placement, `δ`) by incumbent–challenger on untouched outcomes, with NSF allowed. If no, `δ` is set by authority and audited, and **no optimization claim is made** | Selective labels: only accepted cases are observed, so naive optimization is biased | Selecting on a step-level proxy yields the same episode utility as selecting on outcomes. That is Experiment 3; it would make the complete-episode requirement unnecessary *there* |
| **X6 Accountability and contestability** | Must decisions be reproduced, explained by costs or rules, contested, or regulated? | An exogenous decision record: inputs, score versions, `c`, `G`, rule version | Low-stakes entertainment personalization | Blinded auditors diagnose, reproduce and contest endogenous decisions, given full logs and replay, as fast and as accurately as exogenous ones. This is currently untested; Sun's attribution claim is a Hypothesis |
| **X7 Absorption (when to endogenize)** | No X1, X2 or X6; the policy is stable, latency-critical and outcome-dense; exogenous overhead exceeds its measured gain | Distill into weights or a head (the Co-Harness, JERP, TabAgent pattern). Keep the exogenous version as the incumbent and as a regression test | The principal differs from the model owner (a third-party deployer), so absorption would transfer control | Over a drift window, the absorbed version needs retraining no more often than the exogenous one needs re-thresholding, with no loss |

**Decision procedure (per action family).**

1. X2 holds, so authority is exogenous. This is unconditional for effects.
2. X4 fails and the missing information cannot be exposed. Use an endogenous decision inside an
   exogenous envelope.
3. Otherwise, any of X1, X3 or X6 holds. Decision parameters are exogenous.
4. None of them holds and overhead dominates. Absorb (X7).
5. X5 separately decides whether the paper may say "optimize" or only "specify and audit".

The test is about the **decision policy of agents that act**. It says nothing against endogenous
*generative* policies.

---

## 7. Cross-field transfer maps

These analogies stay Hypothesis until their falsifier has been run.

**Simplex / run-time assurance → agents.**

| Control engineering | Agent |
| --- | --- |
| Complex controller | The LLM's proposed action |
| Verified safety controller | A conservative fallback: no-op, human handoff, or the incumbent workflow |
| Decision module | The exogenous authority and decision gate |
| Recoverable region | States from which the fallback restores an acceptable outcome (reversible, pre-commit) |
| Units and timing | Continuous state and dwell time become discrete effects and check-before-effect |

- Assumptions: a fallback exists and switching preserves recoverability. For irreversible software
  effects the region ends at the effect, so the gate must be pre-effect. This is TOCTOU (time of
  check to time of use).
- Falsifier: the harmful effect can occur before the first veto, or stale judgment bypasses the
  gate. This is consistent with `references/mappings.md` §12.

**Holmström–Milgrom multitask → optimization pressure.**

| Principal–agent model | Agent training |
| --- | --- |
| Principal | Deployer or user |
| Agent | The model under training |
| Measured task | Rewarded benchmark or RM score |
| Unmeasured task | Authority respect, rare harms, principal-specific costs |
| Incentive intensity | Optimization pressure: RL steps, KL budget |
| Effort allocation | Learned behavior |

- Their assumptions (a risk-averse agent, linear contracts, substitutable efforts) do not hold for
  neural training. This is analogy, not theorem.
- Prediction: rising optimization pressure on the measured reward degrades independently measured,
  unrewarded dimensions.
- Falsifier: a controlled DPO or GRPO run shows no degradation of an unrewarded, independently
  measured authority-violation rate as optimization pressure rises.

**Policy/mechanism separation (Hydra 1975, Exokernel 1995) → instruments.**

| Operating system | Agent |
| --- | --- |
| Mechanism | Instrument and tool execution |
| Policy | `c`, `G`, thresholds |
| Kernel | Weights |

- Broken assumption: OS mechanisms are policy-neutral, but LLM instruments carry trained implicit
  policies such as refusals and hedging.
- Falsifier: changing the exogenous parameters fails to change outcomes because the instrument's
  implicit policy dominates. The separation is then nominal.

**Elkan's threshold-at-decision → agents.** Applies only while the scores stay calibrated under the
new cost regime and cases are separable, with no shared budget. Under capacity coupling, `δ` becomes
an assignment or knapsack solver, which is still exogenous. Falsifier: prior shift breaks
calibration, so re-thresholding without recalibration loses to retraining.

---

## 8. Falsification experiments

All three run on a MacBook Air with public data. None has been run. Compute estimates are
Hypothesis.

### Experiment 1: cost shift (tests X1 and the core "cost-derived, outside the weights" claim)

**Data:**

- CivilComments, `google/civil_comments` (HF sha `f2970eb3a557`, CC0). Binary moderation with
  severity-weighted costs.
- CLINC150, `clinc/clinc_oos` (HF sha `155b9c710419`, CC-BY-3.0). Route-or-abstain with an
  out-of-scope class.

**Instrument:** frozen `sentence-transformers/all-MiniLM-L6-v2` (sha `1110a243fdf4`, Apache-2.0)
with logistic regression, calibrated on a calibration split. Optionally, the choice probabilities of
a local Qwen3-1.7B (sha `70d244cc86cc`, Apache-2.0).

**Arms:**

- (A) Exogenous Bayes threshold `C_FP/(C_FP+C_FN)`, plus a variant tuned on the calibration split.
- (B) Endogenous-fixed: a head fine-tuned with a cost-weighted loss at `C1 = 1:1`, evaluated at
  other ratios.
- (C) **Endogenous, cost-conditioned**: the cost ratio is an input during fine-tuning over the
  range [1:1, 1:9], evaluated in range and at 1:19, 1:49 and 4:1.
- (D) Constants: act-all, act-none, defer-all at a fixed cost.
- Optional (E): RLSR-style selective-prediction alignment of the local LLM, if the budget allows.

**Metrics:**

- Expected cost per case, as relative regret against the oracle Bayes rule, with paired bootstrap
  CIs by case.
- Monotonicity violations: action flips in the wrong direction as cost rises.
- Adaptation cost to a new ratio: wall-clock time, labels, and whether retraining was needed.
- Brier score and ECE with bin counts.

**Prespecified margin:** 2% relative regret, α = 0.05 over the 5 held-out ratios with Bonferroni
correction.

**Rejects the thesis if:**

- (C) matches (A) within the margin at every held-out and extrapolated ratio, with zero
  monotonicity violations and no greater adaptation cost; or
- (B) matches (A) across ratios.

Either result means cost variation is not a reason for exogeneity on this task.

**Supports the thesis if:** (A) beats (B) off `C1`, and (C) degrades out of range. The toy in §9
shows the expected scale: a threshold left at 0.5 when the true ratio is 1:9 gives +154% regret on
synthetic calibrated scores.

**Estimate:** embedding about 100k short texts with MiniLM takes tens of minutes on CPU/MPS.

### Experiment 2: handler-aware deferral with a handler swap (tests X3 and "models are measured instruments")

**Data:** CIFAR-10H, `jcpeterson/cifar-10h` (GitHub id 204332637, HEAD `389f22d9d300`). Annotator-level
raw labels for the 10,000 CIFAR-10 test images, with 200 normal trials per annotator. License is
**CC BY-NC-SA 4.0**, so a non-commercial use check is needed.

**Handlers:** sampled individual annotators, grouped into "strong" and "weak" pools by accuracy on
a calibration split.

**Classifier:** a small CNN or ResNet-18 trained on CIFAR-10 train on MPS, or frozen features with
logistic regression.

**Arms:**

- (a) Exogenous Chow threshold on confidence with a constant deferral cost.
- (b) **Exogenous two-stage rejector**: a frozen classifier plus a rejector trained on handler
  versus classifier correctness.
- (c) **Endogenous joint L2D** with the Mozannar–Sontag surrogate.
- (d) Constants: always-predict, always-defer.
- Oracle.

**Protocol:** split the images into train, calibration and untouched confirmation sets, 40/20/40.
Freeze the operating points, then swap the handler pool from strong to weak. Re-adapt (b) by
refitting the rejector only, and (c) by retraining jointly.

**Metrics:**

- System 0-1 loss including handler errors, plus a deferral cost `c ∈ {0, 0.05, 0.1}`.
- Coverage.
- Adaptation compute and wall-clock time.
- Paired CIs by image.

**Rejects the thesis if:** (c) beats (b) by more than 1 point of system loss both before and after
the swap, at adaptation cost no greater than (b). The claim that handler-dependent deferral should
be exogenous then fails here. If (a) matches (b), handler modeling is unnecessary.

**Note:** theory allows (c) to win. That is what makes this a real test.

### Experiment 3: episode-level explicit control against implicit control and constants (tests X5, acceptance, and the closest prior)

**Data:**

- HotpotQA distractor setting, `hotpotqa/hotpot_qa` (HF sha `1908d6afbbea`, CC-BY-SA-4.0). Ten
  paragraphs per question.
- Alternatively NQ-open, `google-research-datasets/nq_open` (sha `5dd9790a8300`), with a small BM25
  pool, matching Sun 2026 §5.3.

**Episode:** read k = 2, 4, 6 paragraphs in rounds, deciding stop, expand or abstain each round.
Episode outcome is answer EM/F1. Cost is rounds plus tokens.

**Reader:** local Qwen3-1.7B and Qwen3-4B (sha `1cfa9a720891`) via MLX or llama.cpp.

**Arms:**

- (i) Implicit: one prompt chooses the action.
- (ii) Explicit threshold on an LLM answerability score.
- (iii) Explicit threshold on dense similarity.
- (iv) Composite.
- (v) Constants: always-stop at k0, always-expand to max, always-abstain.
- (vi) **Proxy-selected** threshold, chosen by the step-level AUROC of sufficiency against gold
  presence.
- (vii) **Outcome-selected** threshold, chosen by episode utility `U = EM − λ·rounds − μ·tokens`
  for 3 values of λ.

**Acceptance:** the incumbent is the best constant. The challenger is confirmed on an untouched
split, about 200 search and 400 confirmation questions. Repeat 200 random resplits to estimate the
**false-adoption rate** of "adopt best-on-search" against incumbent–challenger.

**Rejects the thesis if any of:**

- (i) is within margin of the best explicit arm at every λ for both model sizes, so the explicit
  layer is not needed;
- a constant is within margin of the best explicit arm at every λ, so the policy adds nothing
  beyond a constant;
- (vi) is within margin of (vii), so selecting on complete episodes is unnecessary here;
- adopt-best-on-search has no higher false-adoption rate, so the acceptance protocol adds nothing.

**Estimate:** about 600 questions × about 3 calls × 2 models, roughly 3,600 local calls. At a few
seconds per call that is a few hours.

---

## 9. Local reproduced arithmetic (synthetic; not evidence about any model)

Command: `python3 research/080/tmp/exopo/sim_exogeneity.py`. Python 3.14.7, 1.22 s, seed 20260923,
N = 200,000. Script sha256 `80f2f2eb…c9a5`; output sha256 `527c126c…119e3c`.

- **C1, cost shift.** Calibrated `p ~ Beta(0.6, 1.4)`, base rate 0.3017. Keeping a threshold of
  0.5 (tuned for 1:1) against the Bayes threshold:

  | Cost ratio (C_FP : C_FN) | Regret |
  | --- | --- |
  | 1:4 | +50.5% |
  | 1:9 | +154.1% |
  | 1:19 | +363.5% |
  | 4:1 | +51.7% |
  | 1:1 | 0% |

  This is standard decision theory, shown numerically.
- **C2, score insufficiency.** The cost of acting depends on a hidden stake field (20% of cases are
  high-stakes, `C_FP = 20` against 1). The best global score threshold, t = 0.71, costs 0.7105.
  Exposing the field as an input with per-stake Bayes thresholds costs 0.4504. The score-only
  policy therefore has **+57.7% regret**, and it is removed by *exposing the field*, not by
  endogenizing.
- **C3, dominated row.** Act-all costs 0.6983 against a threshold policy's 1.3693.

---

## 10. Recommendations for the paper

- **Change the headline claim.** Replace "the policy should be outside the weights" with "*when* the
  decision policy should be outside the weights, and how to accept a change". Cite Sun 2026,
  Papamarkou et al. 2026, FABLE and the Externalization review in the first two pages.
- **State the ownership argument (C1 rebuttal) in the abstract.** Costs, authority and state belong
  to the principal and change. They are non-parametric by nature. Model weakness is not the reason.
- **Build the paper on the exogeneity test (§6).** Make X4 and X7 visible: "sometimes endogenous"
  is what makes it a test and not a slogan.
- **Separate the three layers.** Authority is contract only. The decision layer holds cost-derived
  parameters. Instruments carry score contracts and may be decision-trained, as in DFL.
- **Credit the statistics.** Treat acceptance as an import: HCPI, Seldonian NSF, SPIBB, CSPI-MT,
  LTT/CRC for constraints, and FABLE's anytime promotion. Add constant-policy and headroom
  baselines, citing the no-free-lunch theorem and the router-headroom negatives.
- **Ship at least one executed experiment.** Experiment 1 is the cheapest decisive one; run it
  before submission. A position paper with a pre-registered falsifier and one result would stand
  out from the 2026 field, most of which is architecture plus small synthetic studies.
- **Treat weak evidence as illustration.** Mechanical Enforcement (circular labels), EO
  (LLM-simulated users; see 2606.20708v1 on simulated customers who never walk away) and
  Sun's retrieval study (no constant baseline) are not support.

---

## 11. Open questions for the maintainer

1. **Name.** Keep "ExoPO", given the ExO-PPO, ExPO and EPO neighbors and the fact that "-PO"
   implies a loss function? The alternative is to keep the long form, "Exogenous Policy
   Optimization", and define "policy" in the first paragraph.
2. **Contribution type.** Is this a position paper (principle, test, falsifiers) or a method paper?
   A method paper needs a concrete optimizer over (placement, `δ`) with a guarantee, for example
   CSPI-MT-style acceptance.
3. **Timing.** The 2026 line is active; FABLE appeared on 2026-07-31. Preprint before or after
   0.8.0 is public? Both the confidentiality rule and scoop pressure apply.
4. **Scope.** Is "agents that act" limited to LLM agents, or does it cover human and organizational
   decision systems too, in line with Augustus's class-wide mission?
5. **Instruments.** Should the experiments include TypeSafe Jev? That requires paid calls, which are
   not authorized in this lane. The alternative is open local instruments only.
6. **Licenses.** Are the non-commercial licenses acceptable (CIFAR-10H CC BY-NC-SA 4.0; ChaosNLI
   CC BY-NC 4.0 if used)?
7. **Promotion into the skill.** Should the exogeneity test become an Augustus reference (runtime
   doctrine) or stay paper-only until an experiment has run?
8. **Pre-registration.** Who fixes the margins and α for §8 before any data is seen, and where is
   the pre-registration kept, given the local-only constraint?

---

## Sources

Retrieved on 2026-09-23 (UTC) unless noted. "Meta" means arXiv API title, authors and date
(id_list batch at 17:03:08Z unless noted). "Abs" means abstract read. "Full" means sections read.
"Patrol" means reused from `wf1-patrol-methods.json`, retrieved 16:15–16:38Z. "Prior card" means
reused from `research/decision-jobs-2026-09-23.md`. Labels: C = Contract, R = Reported (numbers),
Rep = Reproduced, H = Hypothesis, T = theory or position (no numbers relied on).

| # | Canonical ID | URL | Revision | Retrieved | Depth | Label | Used for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | arXiv:2604.00414 | https://arxiv.org/abs/2604.00414 | v1 | 17:15:42Z (html sha 7c7b6241) | full | R | Closest prior: decision-centric |
| 2 | arXiv:2605.00742 | https://arxiv.org/abs/2605.00742 | v2 | 17:15:46Z (cc8e437a) | full | T | Bayes-consistent orchestration position |
| 3 | arXiv:2608.00215 | https://arxiv.org/abs/2608.00215 | v1 | 17:24:07Z (a657f5a4) | full (sections) | R | FABLE: exogenous per-user layer, promotion |
| 4 | arXiv:2604.08224 | https://arxiv.org/abs/2604.08224 | v1 | 17:20:39Z (938ada8a) | §7.3, §8.1 | T | Parametric vs. externalized trade-off |
| 5 | arXiv:2601.01522 | https://arxiv.org/abs/2601.01522 | v1 | 17:17:36Z | abs | R | Cost-aware Bayesian orchestration |
| 6 | arXiv:2605.14744 | https://arxiv.org/abs/2605.14744 | v1 | 17:15:55Z (5e61fe19) | methods | R | Mechanical enforcement (circular labels) |
| 7 | arXiv:2609.03141 | https://arxiv.org/abs/2609.03141 | v1 | 17:15:51Z (954615a5) | full | R | Bitter lesson for data agents |
| 8 | arXiv:2607.25415 | https://arxiv.org/abs/2607.25415 | v1 | 17:16:04Z (93010a0d) | results, §5.2 | R | Harness bandit loses to static DSPy |
| 9 | arXiv:2608.11207 | https://arxiv.org/abs/2608.11207 | v1 | 17:20:43Z (6aaa2be2) | §VII-C, limitations | R | "Exogenous control" term; simulated users |
| 10 | arXiv:2603.03329 | https://arxiv.org/abs/2603.03329 | v1 | 17:16:09Z | abs (full fetched, not read) | R | AutoHarness code policies |
| 11 | arXiv:2510.17173 | https://arxiv.org/abs/2510.17173 | v2 | 17:16:00Z | abs (full fetched, not read) | R | OPE of decision heads |
| 12 | arXiv:1706.03741 | https://arxiv.org/abs/1706.03741 | v4 | 17:03:08Z | meta | T | RLHF origin |
| 13 | arXiv:2203.02155 | https://arxiv.org/abs/2203.02155 | v1 | 17:03:08Z | abs | T | InstructGPT |
| 14 | arXiv:1707.06347 | https://arxiv.org/abs/1707.06347 | v2 | 17:03:08Z | meta | T | PPO |
| 15 | arXiv:2305.18290 | https://arxiv.org/abs/2305.18290 | v3 | 17:03:08Z | abs | T | DPO |
| 16 | arXiv:2310.12036 | https://arxiv.org/abs/2310.12036 | v2 | 17:03:08Z | abs | T | IPO/ΨPO |
| 17 | arXiv:2402.01306 | https://arxiv.org/abs/2402.01306 | v5 | 17:03:08Z | abs | T | KTO |
| 18 | arXiv:2405.14734 | https://arxiv.org/abs/2405.14734 | v3 | 17:03:08Z | abs | T | SimPO |
| 19 | arXiv:2403.07691 | https://arxiv.org/abs/2403.07691 | v2 | 17:03:08Z | abs | T | ORPO |
| 20 | arXiv:2402.03300 | https://arxiv.org/abs/2402.03300 | v3 | 17:03:08Z | abs | T | GRPO (DeepSeekMath) |
| 21 | arXiv:2501.12948 | https://arxiv.org/abs/2501.12948 | v2 | 17:17:35Z | meta | T | DeepSeek-R1 outcome RL |
| 22 | arXiv:2401.04056 | https://arxiv.org/abs/2401.04056 | v2 | 17:03:08Z | abs | T | SPO (minimax winner) |
| 23 | arXiv:2405.00675 | https://arxiv.org/abs/2405.00675 | v5 | 17:03:08Z | abs | T | SPPO |
| 24 | arXiv:2310.12773 | https://arxiv.org/abs/2310.12773 | v1 | 17:03:08Z | abs | T | Safe RLHF Lagrangian |
| 25 | arXiv:2212.08073 | https://arxiv.org/abs/2212.08073 | v1 | 17:03:08Z | abs | T | Constitutional AI |
| 26 | arXiv:2412.16339 | https://arxiv.org/abs/2412.16339 | v2 | 17:03:08Z | abs | R | Deliberative alignment |
| 27 | arXiv:2411.01111 | https://arxiv.org/abs/2411.01111 | v1 | 17:03:08Z | abs | T | Rule-based rewards |
| 28 | arXiv:2607.03528 | https://arxiv.org/abs/2607.03528 | v1 | 17:07:27Z | abs | T | RLSR endogenous selective prediction |
| 29 | doi:10.1109/TIT.1970.1054406 | https://doi.org/10.1109/TIT.1970.1054406 | 1970 | 17:18Z | Crossref meta | T | Chow reject option |
| 30 | Elkan 2001 IJCAI | https://cseweb.ucsd.edu/~elkan/rescale.pdf | PDF sha 46f46ba7… | prior card | prior card (prose) | T | Cost-sensitive thresholds |
| 31 | arXiv:1705.08500 | https://arxiv.org/abs/1705.08500 | v2 | prior card | prior card (full) | T | Selective classification |
| 32 | arXiv:1711.06664 | https://arxiv.org/abs/1711.06664 | v3 | 17:03:08Z | abs | T | Learning to defer |
| 33 | arXiv:2006.01862 | https://arxiv.org/abs/2006.01862 | v3 | prior card | prior card (§1–5.2) | T | L2D Bayes rule; §5.1 counterexample |
| 34 | arXiv:2207.09584 | https://arxiv.org/abs/2207.09584 | v1 | 17:17:35Z | abs | T | Complementary predictors |
| 35 | arXiv:2410.15729 | https://arxiv.org/abs/2410.15729 | v5 | 17:17:48Z | abs | T | Two-stage L2D |
| 36 | arXiv:2604.27723 | https://arxiv.org/abs/2604.27723 | v2 | 17:04:52Z | abs | T | Two-stage L2D, imbalance |
| 37 | arXiv:2609.26384 | https://arxiv.org/abs/2609.26384 | v1 | patrol | patrol (full) | R | Classic L2D lost to baselines on real CXR |
| 38 | arXiv:2110.01052 | https://arxiv.org/abs/2110.01052 | v5 | 17:03:08Z | abs | T | Learn then Test |
| 39 | arXiv:2208.02814 | https://arxiv.org/abs/2208.02814 | v4 | 17:03:08Z | abs | T | Conformal risk control |
| 40 | arXiv:2307.01928 | https://arxiv.org/abs/2307.01928 | v2 | 17:03:08Z | abs | T | KnowNo |
| 41 | arXiv:1710.08005 | https://arxiv.org/abs/1710.08005 | v5 | 17:03:08Z | abs | T | SPO+ (DFL) |
| 42 | arXiv:1703.04529 | https://arxiv.org/abs/1703.04529 | v4 | 17:03:08Z | meta | T | Task-based end-to-end |
| 43 | arXiv:1809.05504 | https://arxiv.org/abs/1809.05504 | v2 | 17:03:08Z | meta | T | DFL combinatorial |
| 44 | arXiv:2307.13565 | https://arxiv.org/abs/2307.13565 | v4 | 17:03:08Z | meta | T | DFL survey |
| 45 | arXiv:2609.12752 | https://arxiv.org/abs/2609.12752 | v1 | patrol | patrol (abs) | R | DFL negative result |
| 46 | arXiv:2510.19672 | https://arxiv.org/abs/2510.19672 | v3 | 17:04:56Z | abs | T | Policy learning with abstention |
| 47 | arXiv:2408.12004 | https://arxiv.org/abs/2408.12004 | v1 | 17:04:56Z | abs | T | CSPI-MT |
| 48 | arXiv:2305.05176 | https://arxiv.org/abs/2305.05176 | v1 | 17:03:08Z | abs | T | FrugalGPT |
| 49 | arXiv:2406.18665 | https://arxiv.org/abs/2406.18665 | v4 | 17:03:08Z | abs | T | RouteLLM |
| 50 | arXiv:2404.14618 | https://arxiv.org/abs/2404.14618 | v1 | 17:03:08Z | meta | T | Hybrid LLM |
| 51 | arXiv:2403.12031 | https://arxiv.org/abs/2403.12031 | v2 | 17:03:08Z | meta | T | RouterBench |
| 52 | arXiv:2606.07587 | https://arxiv.org/abs/2606.07587 | v1 | 17:13:27Z | abs | R | Routing plateau |
| 53 | arXiv:2602.03478 | https://arxiv.org/abs/2602.03478 | v1 | 17:13:27Z | abs | R | Routing collapse |
| 54 | arXiv:2609.07786 | https://arxiv.org/abs/2609.07786 | v1 | 17:13:27Z | abs (numbers "TBD" in v1) | T | Signed rescue routing |
| 55 | arXiv:2602.09902 | https://arxiv.org/abs/2602.09902 | v1 | 17:13:27Z | abs | T | Stackelberg routing |
| 56 | arXiv:2609.19942 / 2609.17306 / 2609.26532 | https://arxiv.org/abs/2609.19942 | v1 | patrol | patrol (abs) | R | Router headroom negatives |
| 57 | BAIR compound AI post | https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/ | 2024-02-18 | 17:19:16Z (44e2dbc1) | page | T | Compound AI |
| 58 | arXiv:2402.01817 | https://arxiv.org/abs/2402.01817 | v3 | 17:03:08Z | abs | T | LLM-Modulo |
| 59 | arXiv:2310.03714 | https://arxiv.org/abs/2310.03714 | v1 | 17:03:08Z | abs | T | DSPy |
| 60 | arXiv:2406.11695 | https://arxiv.org/abs/2406.11695 | v2 | 17:03:08Z | meta | T | MIPRO |
| 61 | arXiv:2507.19457 | https://arxiv.org/abs/2507.19457 | v2 | 17:03:08Z | abs | R | GEPA |
| 62 | arXiv:2406.07496 | https://arxiv.org/abs/2406.07496 | v1 | 17:03:08Z | abs | T | TextGrad |
| 63 | arXiv:2507.03041 | https://arxiv.org/abs/2507.03041 | v4 | 17:05:04Z | abs | R | Optimas |
| 64 | arXiv:2502.17721 | https://arxiv.org/abs/2502.17721 | v4 | 17:05:04Z | abs | T | SysDPO |
| 65 | arXiv:2604.14585 | https://arxiv.org/abs/2604.14585 | v2 | 17:05:04Z | abs | R | Prompt optimization "coin flip" |
| 66 | arXiv:2609.12742 | https://arxiv.org/abs/2609.12742 | v1 | patrol | patrol (full) | R | GEPA gain not separable |
| 67 | arXiv:2603.28052 | https://arxiv.org/abs/2603.28052 | v1 | 17:17:35Z | abs | R | Meta-Harness |
| 68 | arXiv:2603.19461 | https://arxiv.org/abs/2603.19461 | v1 | 17:17:35Z | abs | T | Hyperagents |
| 69 | arXiv:2606.09498 | https://arxiv.org/abs/2606.09498 | v3 | 17:17:55Z | abs | R | Self-Harness |
| 70 | arXiv:2607.08938 | https://arxiv.org/abs/2607.08938 | v1 | 17:17:55Z | abs | R | Harness adaptation for SLMs |
| 71 | arXiv:2606.01779 | https://arxiv.org/abs/2606.01779 | v1 | 17:17:55Z | abs | R | HarnessForge co-evolution |
| 72 | arXiv:2607.22688 | https://arxiv.org/abs/2607.22688 | v1 | 17:17:55Z | abs | T | Co-Harness distills harness |
| 73 | arXiv:2605.27922 | https://arxiv.org/abs/2605.27922 | v1 | 17:17:55Z | abs | R | Harness-Bench |
| 74 | arXiv:2606.27136 | https://arxiv.org/abs/2606.27136 | v1 | 17:04:12Z | abs | T | JERP rules absorbed into weights |
| 75 | arXiv:2602.16429 | https://arxiv.org/abs/2602.16429 | v1 | 17:13:20Z | abs | R | TabAgent decision heads |
| 76 | arXiv:2608.09168 | https://arxiv.org/abs/2608.09168 | v1 | 17:23:47Z | abs | T | RADEG execution gate |
| 77 | OPA docs | https://www.openpolicyagent.org/docs | live | 17:19:18Z (1f4d6fa0) | landing | C | Policy decision offload |
| 78 | Cedar docs; arXiv:2403.04651 | https://docs.cedarpolicy.com/ | live; v2 | 17:19:19Z (d1137124) | landing; meta | C | Authorization language |
| 79 | arXiv:2503.18813 | https://arxiv.org/abs/2503.18813 | v2 | 17:03:08Z | abs | T | CaMeL |
| 80 | arXiv:2504.11703 | https://arxiv.org/abs/2504.11703 | v3 | 17:03:08Z | abs | T | Progent |
| 81 | arXiv:2503.18666 | https://arxiv.org/abs/2503.18666 | v3 | 17:03:08Z | abs | T | AgentSpec |
| 82 | arXiv:2609.08371 | https://arxiv.org/abs/2609.08371 | v1 | 17:04:12Z | abs | R | CapScope 33–47/75 vs 3/75 |
| 83 | arXiv:2605.07728 | https://arxiv.org/abs/2605.07728 | v1 | 17:04:20Z | abs | R | SARC hard vs penalty |
| 84 | arXiv:2608.16891 | https://arxiv.org/abs/2608.16891 | v1 | 17:23:47Z | abs | R | Aegis fail-closed |
| 85 | arXiv:2605.20874 | https://arxiv.org/abs/2605.20874 | v1 | 17:04:20Z | abs | T | CUGA policy-as-code (demo) |
| 86 | arXiv:2602.22302 | https://arxiv.org/abs/2602.22302 | v1 | 17:04:24Z | abs | R | Agent behavioral contracts |
| 87 | arXiv:2605.12863 | https://arxiv.org/abs/2605.12863 | v1 | 17:04:24Z | abs | T | Language-based agent control |
| 88 | arXiv:2607.29190 | https://arxiv.org/abs/2607.29190 | v1 | 17:04:20Z | abs | T | CAGE joint-channel certification |
| 89 | arXiv:1708.08611 | https://arxiv.org/abs/1708.08611 | v2 | 17:03:08Z | abs | T | Shielding |
| 90 | arXiv:1705.10528 | https://arxiv.org/abs/1705.10528 | v1 | 17:03:08Z | abs | T | CPO |
| 91 | arXiv:1805.11074 | https://arxiv.org/abs/1805.11074 | v3 | 17:03:08Z | meta | T | RCPO |
| 92 | JMLR v16 García & Fernández | https://jmlr.org/papers/v16/garcia15a.html | 2015 | 17:19:22Z (ffc3db0d) | landing | T | Safe RL survey (pointer) |
| 93 | doi:10.1109/ACC.1998.703255 | https://doi.org/10.1109/ACC.1998.703255 | 1998 | 17:18Z | Crossref meta | T | Simplex architecture |
| 94 | doi:10.1109/MS.2001.936213 | https://doi.org/10.1109/MS.2001.936213 | 2001 | 17:18Z | Crossref meta | T | Sha, simplicity controls complexity |
| 95 | ASTM F3269-17 | https://store.astm.org/f3269-17.html | 17 | 17:19:27Z (48da5d88) | scope page | C | Run-time assurance standard |
| 96 | arXiv:2312.06942 | https://arxiv.org/abs/2312.06942 | v5 | 17:03:08Z | abs | T | AI control |
| 97 | arXiv:2511.02997 | https://arxiv.org/abs/2511.02997 | v1 | 17:13:47Z | abs | R | Control protocol evaluation |
| 98 | arXiv:2506.05296 | https://arxiv.org/abs/2506.05296 | v3 | 17:13:47Z | abs | T | Control tax |
| 99 | arXiv:2510.09462 | https://arxiv.org/abs/2510.09462 | v2 | 17:26:35Z | meta | T | Adaptive attacks on monitors |
| 100 | arXiv:2606.02965 | https://arxiv.org/abs/2606.02965 | v2 | 17:04:24Z | abs | R | Informed abstention |
| 101 | arXiv:2606.08919 | https://arxiv.org/abs/2606.08919 | v1 | 17:04:52Z | abs | R | Oversight capacity |
| 102 | arXiv:2605.27117 / 2605.18672 / 2608.13926 | https://arxiv.org/abs/2605.27117 | v1 | 17:07:15Z / 17:23Z | abs | T | Control-plane positions; structural abstention |
| 103 | PMLR v37 Thomas et al. 2015 | https://proceedings.mlr.press/v37/thomas15.html | 2015 | 17:19:21Z (0bb8165d) | abs | T | HCPI |
| 104 | doi:10.1126/science.aag3311; Seldonian tutorial | https://seldonian.cs.umass.edu/Tutorials/tutorials/alg_details_tutorial/ | 2019; live | 17:18Z; 17:26:45Z (288e293f) | Crossref meta; tutorial text | T | Seldonian, NSF |
| 105 | arXiv:1712.06924 | https://arxiv.org/abs/1712.06924 | v5 | 17:03:08Z | abs | T | SPIBB |
| 106 | doi:10.1093/jleo/7.special_issue.24 | https://doi.org/10.1093/jleo/7.special_issue.24 | 1991 | 17:18Z | Crossref meta | T | Multitask principal–agent |
| 107 | arXiv:1804.04268 | https://arxiv.org/abs/1804.04268 | v1 | 17:03:08Z | abs | T | Incomplete contracting |
| 108 | arXiv:1606.03137 | https://arxiv.org/abs/1606.03137 | v4 | 17:03:08Z | meta | T | CIRL |
| 109 | arXiv:1803.04585 | https://arxiv.org/abs/1803.04585 | v4 | 17:03:08Z | meta | T | Goodhart variants |
| 110 | arXiv:2210.10760 | https://arxiv.org/abs/2210.10760 | v1 | 17:26:35Z | meta | T | RM overoptimization |
| 111 | arXiv:2310.17022 | https://arxiv.org/abs/2310.17022 | v3 | 17:26:35Z | meta | T | Controlled decoding |
| 112 | arXiv:2002.06673 | https://arxiv.org/abs/2002.06673 | v4 | 17:03:08Z | abs | T | Performative prediction |
| 113 | arXiv:2411.15230 | https://arxiv.org/abs/2411.15230 | v1 | 17:18:01Z | abs | T | No-free-lunch for human–AI collaboration |
| 114 | arXiv:2504.03255 | https://arxiv.org/abs/2504.03255 | v2 | 17:13:47Z | abs | T | Principal–agent liability |
| 115 | doi:10.1145/3097983.3098066 | https://doi.org/10.1145/3097983.3098066 | 2017 | 17:18Z | Crossref meta | T | Selective labels |
| 116 | doi:10.1177/0272989X06295361 | https://doi.org/10.1177/0272989X06295361 | 2006 | 17:18Z | Crossref meta | T | Decision curve analysis |
| 117 | arXiv:2609.20758 / 2609.24200 / 2609.16793 | https://arxiv.org/abs/2609.20758 | v1 | patrol | patrol | R | Audit sampling; writable channel; reviewer deference |
| 118 | Sutton, The Bitter Lesson | http://www.incompleteideas.net/IncIdeas/BitterLesson.html | 2019-03-13 | 17:19:15Z (f1baabba) | full | T | C1 |
| 119 | arXiv:2507.06282 | https://arxiv.org/abs/2507.06282 | v1 | 17:07:34Z | abs | R | Bitter lesson of misuse detection |
| 120 | NeurIPS 2015, Sculley et al. | https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html | 2015 | 17:19:24Z (a700f7e5) | landing (not re-inspected) | T | Tech debt (pointer) |
| 121 | arXiv:2609.14400 | https://arxiv.org/abs/2609.14400 | v1 | 17:13:34Z | abs | R | Policy loopholes |
| 122 | arXiv:2603.19328 | https://arxiv.org/abs/2603.19328 | v1 | 17:04:24Z | abs | R | Verifier tax |
| 123 | arXiv:2609.00445 | https://arxiv.org/abs/2609.00445 | v1 | 17:04:16Z | abs | R | Capability-gated models |
| 124 | arXiv:2509.23994 | https://arxiv.org/abs/2509.23994 | v2 | 17:04:20Z | abs | T | Policy-as-prompt |
| 125 | arXiv:2606.20708 | https://arxiv.org/abs/2606.20708 | v1 | 17:07:46Z | abs | R | Simulated customers' decision fidelity |
| 126 | doi:10.1145/800213.806531 | https://doi.org/10.1145/800213.806531 | 1975 | 17:18Z | Crossref meta | T | Hydra policy/mechanism |
| 127 | doi:10.1145/224056.224076 | https://doi.org/10.1145/224056.224076 | 1995 | 17:18Z | Crossref meta | T | Exokernel |
| 128 | arXiv:1806.01584; 2207.06272 | https://arxiv.org/abs/1806.01584 | v1; v3 | 17:03:08Z | meta | T | Exo-MDP term collision |
| 129 | arXiv:2602.09726 | https://arxiv.org/abs/2602.09726 | v1 | 17:04:00Z; WebSearch | abs | T | ExO-PPO name neighbor |
| 130 | arXiv:2404.16792; 2507.02834; 2507.07986 | https://arxiv.org/abs/2404.16792 | v5; v3; v3 | 17:04:00Z | meta | T | ExPO/EXPO name neighbors |
| 131 | arXiv:2502.12486 | https://arxiv.org/abs/2502.12486 | v6 | 17:07:21Z | abs | T | EPO "Explicit Policy Optimization" |
| 132 | GitHub kavinkk2425/ExoPO | https://github.com/kavinkk2425/ExoPO | id 1362223897, HEAD 99ce8e5d | 17:19:53Z | tree | — | Exact-name placeholder (empty) |
| 133 | HF Hub search "exopo"; PyPI/npm "exopo" | https://huggingface.co/api/models?search=exopo | live | 17:20:20Z | API | — | 0 / 0 / 0 hits; 404 / 404 |
| 134 | clinc/clinc_oos | https://huggingface.co/datasets/clinc/clinc_oos | sha 155b9c710419 | 17:22:23Z | API meta | C | Experiment 1 data (CC-BY-3.0) |
| 135 | google/civil_comments | https://huggingface.co/datasets/google/civil_comments | sha f2970eb3a557 | 17:22:23Z | API meta | C | Experiment 1 data (CC0) |
| 136 | jcpeterson/cifar-10h | https://github.com/jcpeterson/cifar-10h | HEAD 389f22d9d300 | 17:22Z | README, LICENSE | C | Experiment 2 data (CC BY-NC-SA 4.0) |
| 137 | hotpotqa/hotpot_qa; nq_open | https://huggingface.co/datasets/hotpotqa/hotpot_qa | sha 1908d6afbbea; 5dd9790a8300 | 17:26:33Z | API meta | C | Experiment 3 data |
| 138 | all-MiniLM-L6-v2; Qwen3-1.7B; Qwen3-4B | https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 | 1110a243fdf4; 70d244cc86cc; 1cfa9a720891 | 17:26:33Z | API meta | C | Instruments (Apache-2.0) |
| 139 | Local simulation | `research/080/tmp/exopo/sim_exogeneity.py` | sha 80f2f2eb | 17:23Z | executed | Rep | §9 arithmetic |
| 140 | Augustus internal doctrine | `.agents/skills/augustus/references/optimizer-integration.md`, `validation.md`, `mappings.md` §12 | repo HEAD 4236a60 | read 17:00Z | full | C (internal) | Baseline ExoPO formalizes |
