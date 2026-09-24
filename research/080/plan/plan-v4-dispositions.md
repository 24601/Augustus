# Review dispositions for Augustus 0.8.0 plan v4

**Public**, on `research/080-exopo-trainer`.

**Inputs**

- `reviews/fable-5.1-xhigh-v3.md` — requested `claude-fable-5-1` at xhigh; observed "Fable 5.1"
  with `<reasoning_effort>80</reasoning_effort>`. NOT ACCEPTED: 0 P0, 1 P1, 10 P2.
- `reviews/astra-max-v3.md` — requested `gpt-6-astra` at max; the Codex header reports the same,
  which is CLI configuration and not proof of the serving model. NOT ACCEPTED: 0 P0, 3 P1, 4 P2.
- `plan-v3-errata.md` — maintainer decisions D-a…D-e and the post-v3 host facts.
- `receipts/m0-tabputer-1-2026-09-23.md` — M0 result and nine recorded deviations.
- `sources/paw-rap-2026-09-23.md`, `sources/clm-2026-09-23.md`, `sources/jev-omni-2026-09-23.md`,
  `sources/trainer-sweep-2026-09-23.md`, `sources/trainer-sweep-multimodal-2026-09-23.md`.

Section numbers below refer to `plan-v4.md`.

**Disposition values.** *Accepted*: the correction is adopted as proposed. *Modified*: the defect
is accepted, the fix differs. *Rejected*: the defect is not accepted.

**Result.** 18 review findings, all dispositioned; none rejected. Two are Modified.

**Arithmetic.** Every number used in v4 is recomputed by `calc/calc_v4.py` (stdlib, deterministic;
sha256 `4a2d2308…`), output `calc/calc_v4.out.txt` (sha256 `5d7e2644…`). `calc_v3.py` is retained
for the superseded normal-theory figures. New or changed numbers:

- Astra's counterexample: `0.9999^12850 = 0.2766328082`; joint with a 3,000-row pilot
  `0.2049315506`; the EB radius on the same data is `0.002608` (range 1.96) against a 0.00005
  margin, so EB reports unpowered rather than equivalence.
- E1 under EB: equivalence n 78k–688k (fits 1.4M); superiority n 1,425–18,754; CLINC at 12,850
  powers no equivalence contrast.
- E3 under EB (R = 1.2): n 5,178 (σ = 0.25), 6,794 (σ = 0.30) at m = 6; 6,185 at m = 3; full
  replay 133,290 calls, 115,290 of them over the 6,405-question P6 population.
- M5 under EB at K = 5: n 6,671 / 14,035 / 25,535 at σ = 0.10 / 0.20 / 0.30.
- E4a: C = 108, R = 40,000, cutoff 2,049 adoptions (CP upper 0.05497); 1.08e10 sampled losses,
  19.1 MiB chunks, 2,160 kernel batches; 0.1–0.9 min at 2e9–2e8 elements/s [H].
- P1 regret on the v3/v4 population: +95% at 1:9, +216% at 1:19, +553% at 1:49.
- GPU budgets as fractions of 124 GiB visible: 0.016 / 0.113 / 0.048 / 0.306 / 0.081.

## Fable v3 (1 P1, 10 P2)

| ID | Sev | Finding | Disposition | Where in v4 |
|---|---|---|---|---|
| P1-1 | P1 | The design lock must precede "any download", but M2 depends on the milestone that performs all 45 GB of downloads, and the lock hash is printed in the paper | **Accepted** | §2.7 restates the precondition as "any experiment-dataset download or any read of dataset text or labels", and names wheels, the base image and the acceptance weights as not experiment data; §4.4 records that M0's acceptance ran on **synthetic** texts, so no dataset was read. §4.2 names three attended windows (W1 provisioning, W2 after the M2 design lock, W3 gems), each closed with a B9/B10 re-run and a dated receipt, with no experiment or candidate container running while a proxy rule exists. §7 makes M2 depend on **M0 decisions only** and inserts M2b for W2. §6.2 puts the window receipts beside the lock dates on `/evidence/`, so a reader can check the order |
| P2-1 | P2 | As specified the proxy cannot resolve a hostname, so B9's only success case fails | **Accepted; already fixed in the installed code** | §4.2: `augproxy` reaches the local stub `127.0.0.53` on UDP/TCP 53 (`infra/nft/augexp.nft` L72), and B9 passed live at M0 |
| P2-2 | P2 | Staging the site source on tabputer-1 contradicts "run bundles and public data" | **Modified** | The premise changed: the maintainer published the research record (D-c/D-d), so `docs/exogenous-policy/` is public material. §4.1 says so explicitly rather than extending a confidentiality carve-out |
| P2-3 | P2 | Superiority reads state no margin, and the powered-set rule has an unstated planning gap g | **Accepted** | §2.7 states each superiority margin (δ_r in E1, 0.02 in E3, 0.01 in M5) and fixes **g at the design lock**: 0 for equivalence and non-inferiority, the prespecified planning effect for superiority. The analysis lock records σ̂ and the powered set but never re-chooses g, so no free parameter survives calibration. `calc_v4.py` §7 tabulates the resulting n |
| P2-4 | P2 | The "second, equal-size fit subsample" has no partition to come from | **Accepted** | §2.7 E1 adds an explicit **fit-B 200k** partition; confirmation drops to about **1.4M**, and `N_CONF_CIVIL` in `calc_v4.py` uses 1,400,000 |
| P2-5 | P2 | Disk exhaustion is bounded by nothing the plan names | **Accepted** | §4.2 puts `/srv/aug/runs` and `/srv/aug/pred` on a size-bounded filesystem; **B17** tests ENOSPC inside the container only; E4c lists it |
| P2-6 | P2 | "Local only" omits the disclosure to review providers | **Accepted** | The v4 header states that delegate reviews send the whole plan to hosted providers under their API terms [C, recheck]. The record is now public anyway |
| P2-7 | P2 | E4a positive controls do not say which cell class detects which defect, and name no planning effect | **Accepted** | §2.7 E4a names them: radius removed → every cell; radius n inflated 100× → Hoeffding and EB at σ ≥ 0.3; sign flip → **non-inferiority cells only**, because it is invisible to the size test in superiority mode. The planning effect per distribution is fixed at the design lock and the K = 5 event is any-of-five adoption. The CPU-process question dissolves: E4a runs on the GPU under D-b |
| P2-8 | P2 | Profile and boundary nits: the shared prediction group; B10's counter criterion; "sequential until B14" ordering; B5's marker regex; confirmation texts vs labels; B-stale's identity with the 0.5 plug-in | **Accepted** | §4.2 names group `augpred` and its setgid directory; §4.3 corrects B10's pass criterion and says B14 uses test containers; B5's regex and its 12 known public-documentation matches are recorded in the M0 receipt; §2.7 releases confirmation **texts** only after the analysis lock and never releases labels; §2.2 fixes calibration as **temperature with no intercept** for the no-shift arms |
| P2-9 | P2 | M5 and E1 parameters left to the lock: escalation LCB level, T2c expansion, CLINC's E1 decision | **Accepted** | §3.3 sets the escalation LCB at the same α/(2K) tail as the UCB and makes the T2c 40k→60k expansion follow the analysis-lock n(σ̂) rule, not discretion; §2.7 E1 defines the CLINC route-or-abstain decision, its s(x), and what an FP and an FN are |
| P2-10 | P2 | Provenance nits: Mac modes, the P1 percentages, the R1 token estimate | **Accepted** | The Mac row is gone (no isolation claim, and the record is public). P1 is restated as **+95% / +216% / +553%** from the v3/v4 population [Rep calc §2], with the old figures explicitly withdrawn in the Sources note. The R1 token estimate is superseded by §4.5, which is driven by measured throughput and the timing pilots |

## Astra v3 (3 P1, 4 P2)

| # | Sev | Finding | Disposition | Where in v4 |
|---|---|---|---|---|
| 1 | P1 | The shared staging directory exposes confirmation labels: a candidate can recover them from the original labeled corpora in `/stage` or from setup caches, so B6 passes while the route stays open | **Accepted** | §4.2 adds a custody path: downloads land in `/srv/aug/quarantine` (with the HF cache); at window close the tree is re-owned to root with an ACL for `augctl` only; `augctl` splits, hashes and publishes `/srv/aug/stage/parts/<id>/` containing fit and calibration partitions with labels and **confirmation inputs with labels removed**, and nothing else. Each run mounts only its entitled partitions. **B16** is the adversary test: search every readable tree and the cache, join by text, normalized text or id, and read the quarantine; a planted canary must never surface. E4c lists it, and M3 cannot start before it passes |
| 2 | P1 | The family-error guarantee does not follow from normal/bootstrap intervals: both collapse to `[0,0]` on rare-large bounded losses and falsely certify equivalence | **Accepted** | §2.4 replaces them. The claim-bearing interval is a two-sided **empirical Bernstein** interval for bounded losses at α/(2m) per tail, whose radius floor `7R ln(2/δ)/(3(n−1))` cannot collapse; the design lock must record the bound R. Normal-theory intervals are printed `descriptive_only` and carry no error claim. On Astra's own construction, EB gives 0.002608 against a 0.00005 margin, so the verdict is *unpowered* [Rep calc §1]. E4b gains a zero-discordance rare-large fixture, and every n in E1, E3 and M5 is recomputed under EB. `loss_bound` becomes a required helper input (§3.5) |
| 3 | P1 | M0 and M2 impose contradictory download prerequisites | **Accepted (with Fable P1-1)** | The W1/W2/W3 window sequence and the M0 → M2 → M2b → M3 ordering in §4.2 and §7. Provisioning and acceptance precede the locks; experiment data follows them |
| 4 | P2 | P6's finite-population truth needs full replay, which exceeds the advertised planned workload by 52,290 calls | **Modified** | Both halves of Astra's correction are taken: **full replay is the planned workload** (133,290 calls for two readers, 66,645 narrowed), *and* P6's finite population is pre-registered as the **6,405 confirmation questions**, which the search set never touched — 115,290 of those calls. The truth is held by `augctl` and never exposed to selection. At the measured 2,004 tok/s the decode cost is 1.2 GPU-h, well inside the 24 GPU-h cap, so making full replay the plan costs little [Rep calc §3, §6] |
| 5 | P2 | §3.6 leaves the disputed-lineage case unresolved, and a substring alias rule would misfire | **Accepted** | §3.6 resolves identity **by declared lineage, never by name substring**, and adds a fourth verdict state, `disputed`: a sourced, revision-bound allegation against a declared lineage blocks training use pending resolution, and a named approval preserves the allegation instead of describing it as cleared. Both concrete cases are test rows: Jev-Omni → `unknown` on missing parents (not barred by name, not allowed by attestation), with its three derivatives inheriting through `derived_from`; `LocalLLaMA/typed-decisions` → `disputed` |
| 6 | P2 | S12 prescribes an inconclusive result from the row count alone, when EB at K = 3, n = 3,000 and zero variance certifies non-inferiority | **Accepted** | §3.7 splits it. **S12a** states method, mode, family and σ̂ = 0.10, where the required n is 6,164 and the answer is inconclusive with the margin unmoved. **S12b** is the countercase at σ̂ = 0.02, where the skill must certify non-inferiority at 3,000 rows [Rep calc §4] |
| 7 | P2 | The memory blocker and its attribution are stale | **Accepted** | §4.5 records MemAvailable 121,366,040 kB of 131,007,996 kB at 18:38 MDT 2026-09-23 [Coord] and the stopped vLLM server as the true owner, drops the k3s attribution, keeps the cap and the launch/abort floors, and derives `blocked(memory)` from the launch measurement |

## Errata (maintainer decisions and post-v3 facts)

| Item | Where in v4 |
|---|---|
| **D-a** coordinator SSH and sudo for provisioning | Used at M0 and recorded in the receipt. v4 supersedes it operationally: Amp reaches tabputer-1 only through the runner `tabputer`, and §4.1 states the hard rules that every runner task repeats |
| **D-b** GPU for everything; Colab, never CPU | §0.5, §2.7 E4a (vectorized GPU Monte Carlo; the only CPU step is the exact-rational `sign_exact` qualification, which is arithmetic rather than sampling), §4.4 (a failed parity check goes to Colab), §4.1 (Colab carries no boundary claim), §4.5 |
| **D-c/D-d** publish; Jev everywhere except as our training data; no counsel step | Header; §1 non-goals; §3.6 (refused by default with one quoted MCA §2.3(b) line, user-overridable with a recorded acknowledgment); §3.3 (a Jev call is an allowed sub-decision form in a composed program); §2.1 and §3.5 (comparator use, with comparator isolation enforced in code). Every counsel item and accept-risk gate is deleted from §7 and §9 |
| **D-e** PAW is a tested arm; local compiler preferred; hosted compile is a public-data fallback | §3.3 arms A2a and A2b; §4.4 PAW interpreter parity; §4.5 the 38 GiB GPU budget; decision 8 |
| **Programs as rungs** | §3.3 in full: artifact forms A0–A7 under one gate, composed decision programs with per-stage acceptance, the circularity trap that keeps T1 fixture-only, and the advance statement that programs are expected to lose on fuzzy real text |
| **RAP as required prior art** | §2.1 (detection, not gating), §2.3 (the closing rule), §2.6 P3 and P10, §3.5 (operational failure is never `OK`; findings bound to rule revisions) |

## M0 deviations (receipt, 2026-09-23)

| # | Deviation | Where in v4 |
|---|---|---|
| 1 | uids are **48201** and **48202**, not 1001/1002 (host uid 1001 belongs to fleet-pr runner containers) | §4.2 principal table; B15 |
| 2 | The profile needs **`--memory-swap=16g`**; with 125 GB of zram, `--memory=16g` alone did not cap memory | §4.2 container line; §4.5 envelope |
| 3 | Runs launch with **`systemd-run --user`** in `augexp`'s manager, never `sudo -u … podman` from another session | §4.2; linger enabled for the window only |
| 4 | **GPU memory is not charged to the container cgroup** (24 GiB held at `memory.current` 0.56 GiB) | §4.2 "GPU budget (mandatory)" with per-run fractions; B18; §4.6 records that `dmem` is untested |
| 5 | A **real MemAvailable watchdog** is required, not a note | §4.2: code sampling `/proc/meminfo` every 5 s, refusing launch below 24 GiB and killing below 6 GiB, with the reason in the run record; B18 |
| 6 | vLLM batched throughput about **2,004 tok/s**, but only **59.8%** batched-rerun identity | §2.7 E3 requires batch-invariant mode or a fixed batch composition wherever replay matters, and reports the realized rate before confirmation; §4.5 uses the measured throughput instead of v3's 800 tok/s decode assumption; §8 risk row |
| 7 | Local IPC and other workloads' trees are part of the boundary (`augipc-acl`, the D-Bus policy, `augfs-deny`) | §4.2 egress; §4.3 B4, B9, B10; §4.6 non-claim about trees created later |
| 8 | The proxy binds **SNI to the CONNECT host** | §4.2; §4.6 non-claim about CDN domain fronting |
| 9 | **E4a moves to the GPU** | §2.7 E4a, with the chunking and the 1 GPU-h cap [Rep calc §5] |

## Sweep and card items that change a decision

Only items that change a design decision are folded in; the rest stay in the sweeps.

| Item | Source | Where in v4 |
|---|---|---|
| Multimodal is a **side ladder**, not a new top rung, and its gains are workload-local | multimodal sweep §1.1 | §3.3 M-R0…M-R5, documented and **untested in 0.8.0** by default; decision 9 |
| A **modality blind-arm gate** is mandatory, and accuracy alone cannot pass it | multimodal sweep §1.2, §9.3 F1 | §3.3: text-only, options-only, blank media and swapped media through the same pipeline, paired cluster bootstrap by media group, NLL-delta lower bound above 0; failure routes to the text ladder |
| **`input_coverage`** must be a field of the decision record, because every carded recipe dropped evidence silently | multimodal sweep §1.5 | §3.4 data protocol row |
| **Precision is part of the model** (drift up to 0.2 in probability) | Jev-Omni card; multimodal sweep §1.7 | §3.4 serving-precision row; §4.4 parity check 3; §3.5 calibrator identity |
| **Qwen3.5 hybrid attention is unverified on gfx1151**, and §4.4's acceptance used standard-attention models only | text sweep §6.1 item 12; multimodal sweep §9.4 | §4.4 parity check 1, with Qwen3-1.7B as the fallback R1 model and shared-prefix packing forbidden for that family |
| **Per-type, per-head outcomes**; a pooled metric never decides | multimodal sweep §9.3 F4 | §3.3 multimodal rules; §3.5 hard gates |
| RL reward, preference pairs and DAgger relabels are **training uses** v3's edge set could not express | text sweep §6.1 item 1 | §3.6 edges `rewarded_by`, `preferred_by`, `relabeled_by`, with test rows |
| **Comparator isolation in code**, not prose | text sweep §6.1 item 4 | §3.5 climb ledger |
| Seven recurring **evaluation defects** need hard gates | text sweep §6.1 item 5 | §3.5 hard-gate list (calibration split, grid-bound temperature, entropy-as-confidence ECE, pooled test+OOD, OOD without source ids, checkpoint on test rows, empty conformal set) |
| **Data-protocol rows**: state-space dedup, time-ordered splits for logged traces, labeler identity per row | text sweep §6.1 item 6 | §3.4 |
| "**Search with an exact simulator**" is a second R0 exit | text sweep §6.1 item 9 | §3.2 |
| The most repeated public advice is "log your Jev calls and distill them" | text sweep §6.2 | §3.7 S7 quotes that request shape and redirects; §3.6 makes the refusal default and overridable |
| Do not emit `/v1/systemone`-shaped servers by default | text sweep §6.2 | Decision 13 |
| Hosted non-Jev teachers will trip the gate constantly | text sweep §6.2 | Decision 12: ship them `unknown` with a named-approval path |
| **Shielded-harness reporting**: agreement and intervention counts beside end-to-end success | CLM card §4.3 | §2.1 table row; it is the paper's own thesis in someone else's data |
| An **outcome-labeled verifier** is a provenance-free route | CLM card §4.2 | §3.4 gold-first and teacher-route rows; §3.2 |
| PAW's **evaluation hygiene**: frozen protocol versions, sidecar manifests, contrast-pair cluster resampling, findings bound to rule revisions, operational failure never `OK` | PAW/RAP card | §3.5 |
| PAW-ft needs about **38 GiB of accelerator memory**, outside the 16 GiB CPU cgroup | PAW/RAP card | §4.2 GPU budget; §4.5 |

**Not folded in.** Nothing in the 437 swept items supplies a controlled comparison that moves a
rung, so the ladder order, the M5 pre-registered rule and the 1 pp margin stand. Stars, likes and
downloads were observed and not used. Third-party metrics remain Reported and unreproduced except
where a card recomputed them from frozen prediction files.

## Items v4 adds that neither review raised

| Item | Where | Reason |
|---|---|---|
| `loss_bound` is a required input to EB and Hoeffding | §3.5 | Without the range, neither radius is defined; v3 left it implicit |
| Per-ratio loss ranges R_r = 2·max(C_FP, C_FN) in E1 | §2.7 E1 | Using R = 2 everywhere would inflate the radius at asymmetric ratios by up to 2× |
| The E3 utility is clipped to [−0.2, 1] at the design lock | §2.7 E3 | EB needs a declared bound; an unbounded utility has none |
| B18 (GPU budget and watchdog) | §4.3 | The GPU-side budget is now a control, so it is tested like one |
| M0b as a milestone | §7 | B16–B18 and the custody path are work, not paperwork, and M3 depends on them |
| S16 and S17 scenarios | §3.7 | The artifact-form ladder and the detection/prevention boundary need behavioral tests, not only prose |
| Discovery lanes gain wire-format code search | §5 | Both sweeps missed CLM because its metadata was empty |

---

# v4 review dispositions (2026-09-24)

Both v4 reviews were run on plan sha256 `6102f850…`, HEAD `58be8b4`. `plan-v4.md` was then
revised in place to answer them; the arithmetic was recomputed (`calc_v4.py` sha256 `2aedbbb2…`,
output `1c281850…`).

**Reviewer identity, requested versus observed.**

| Review | Requested | Observed |
|---|---|---|
| `reviews/astra-max-v4.md` | `gpt-6-astra-max` | **None.** The reviewer reports "You are an AI assistant accessed via an API" and states plainly that it cannot certify Astra or a max effort. No identity is claimed on its behalf |
| `reviews/fable-5.1-xhigh-v4.md` | `claude-fable-5-xhigh` | "You are claude-fable-5-xhigh, a custom agent running in Amp". The effort marker appears only inside the agent name; no separate numeric value was visible, unlike the v3 session |

Both verified HEAD, the plan hash, and that `calc_v4.py` reproduces its saved output byte for
byte, and each wrote its own independent stdlib script. Neither performed a host operation.

**Verdicts.** Astra: NOT ACCEPTED, 0 P0, 6 P1, 5 P2. Fable: NOT ACCEPTED, 0 P0, 2 P1, 8 P2. The
two P1 sets overlap on E3's loss range. **13 distinct findings; none rejected.**

| ID | Sev | Finding | Disposition | Where in the revised v4 |
|---|---|---|---|---|
| Astra F1 = Fable P1-A | P1 | E3 declared R = 1.2, the range of **one** utility, while §2.4 defines R as the range of the **paired difference**. Two utilities in an interval of width 1.2 differ by up to ±1.2, so R = 2.4. The bias term was half its valid size, the interval was anticonservative, and every E3 planning number was wrong | **Accepted** | §2.7 E3 population row states R = 2.4 and why. Recomputed: equivalence needs 6,598 (σ = 0.25) and 8,271 (σ = 0.30) at m = 6, so the rows are powered only if σ̂ ≤ 0.24, and at m = 3 only if σ̂ ≤ 0.26 — not the "about 0.29" v4 claimed. The narrowing row now fires on σ̂, and the margin and the population are unchanged. Both reviewers' tables reproduce exactly |
| Astra F5A | P1 | M5 declares one-sided non-inferiority but the arithmetic used the **two-sided equivalence** event, which is conservative for false positives yet misclassifies powered tasks: T2b at σ = 0.20 is powered for the declared test and v4 called it unpowered | **Accepted** | `calc_v4.py` gains `n_ni_eb`, the one-sided event. K = 6 needs 6,354 / 12,698 / 22,467 at σ = 0.10 / 0.20 / 0.30. §2.7 now says the power event must match the registered claim, and §3.3 carries the new n and σ̂ thresholds (T2a 0.09, T2b 0.20, T2c 0.53) |
| Astra F5B | P1 | `g` was used both as the true effect and as the distance beyond the margin. E3's "true 0.04 gain" was passed as a gap of 0.04, which is really a true gain of 0.06 | **Accepted** | `true_delta`, `margin` and `gap = |true_delta| − margin` are separate named quantities in §2.7 and in the script. E3's true 0.04 gain needs 7,318 (m = 6) or 6,592 (m = 3) at σ = 0.30, not 1,830 |
| Astra F6 = Fable P2-7 | P1 | A2a (PAW-standard) is a tested arm but sat outside the K = 5 family, so M5 could escalate past an artifact form that met the same gate, and no error-controlled claim attached to A2a | **Accepted** | §3.3 puts A2a inside the confirmatory family: **K = 6**, fixed at the design lock. R0 is named as a G0 exit, not a family member. "Powered" is defined per contrast, so an outcome row quantified over tasks means powered for that row's own contrast |
| Astra F3 = Fable P2-4 (part) | P1 | A fixed 24 GiB launch floor admits a 38 GiB GPU budget plus a 16 GiB CPU cap on a UMA host; the declared budgets are per-process allocator limits, not a GPU cgroup; and a 5 s watchdog cadence cannot catch a burst | **Accepted** | §4.2 replaces the floor with an **aggregate admission rule**: MemAvailable ≥ GPU budget + CPU cap + declared service memory + 8 GiB overhead + the 6 GiB reserve, so PAW-ft needs 68 GiB free. The watchdog samples every **500 ms**. §4.6 records that allocator limits are not a GPU cgroup. B18 gains a mocked low-memory launch test and a bounded first-party burst that measures kill latency; the host is never deliberately driven to OOM |
| Astra F4 | P1 | Denying candidate code GPU devices contradicts binding decision D-b and makes GPU-dependent candidates unreachable | **Accepted** | §4.2: candidate containers get the devices under the same admission control, budget, `--network=none` and per-run `/work`. §4.6 records the cost — the driver's attack surface is now exposed to candidate code, and the boundary does not claim to contain it |
| Fable P1-B | P1 | The custody path published data partitions "and nothing else", so **no model weight could reach a run container**; every GPU run was unreachable, and the obvious shortcut (a shared HF cache) reopened Astra v3 finding 1 | **Accepted** | §4.2 splits acquisition into `/srv/aug/quarantine/data` and `/srv/aug/quarantine/weights`. `augctl` verifies weights against the acquisition manifest and publishes `/srv/aug/stage/weights/`, root-owned and read-only, which runs mount. **B16 searches both trees** |
| Astra F2 | P1 | B16 tested current local files, not the whole proposer-to-artifact path: a proposer holding the public labeled corpus can embed a text-hash → label table in a frozen artifact, needing no file or network at confirmation. A private canary cannot detect that. Re-owning a pathname also does not revoke bytes already copied or descriptors already open | **Accepted, with the claim narrowed** | B16 gains part (b): a first-party adversary proposer embeds exactly that lookup table, and the **overlap audit must detect it** before scoring. The plan does not claim prevention. Window close is specified as a teardown: no `augexp` acquisition process survives it, and the receipt records that. §4.6 adds the non-claim that filesystem custody cannot make public benchmark labels secret, since a model rung's pretraining reaches them anyway |
| Fable P2-6 | P2 | Pretraining memorization of public benchmarks is an unclosable label-recovery route and needs an explicit non-claim | **Accepted (with Astra F2)** | The same §4.6 non-claim, with external validity limited accordingly |
| Astra F7 | P2 | Equal inclusion probability is not the theorem's assumption. Sampling one of two clusters uniformly gives equal inclusion probability, zero sample variance and zero coverage | **Accepted** | §2.4 adds the sampling assumption: the design lock names the **independent unit**, clustered or weighted designs are aggregated to it or refused, and power is computed from the same unit |
| Astra F8 | P2 | S12b prescribed certification from n and σ̂ alone; at the same n and sd, an observed mean of +0.005 fails. And 3,000 rows give about 0.76 NI power at sd 0.02, below the powered-set rule | **Accepted** | §3.7 now has S12a (mean 0.000, sd 0.10 → not certified, required n 5,691), S12b (sd 0.02 → certified, radius 0.009737) and **S12c** (same n and sd, mean +0.005 → not certified). `calc_v4.py` §4b separates planning from observed certification |
| Astra F9 = Fable P2-8 | P2 | `0.598^9 = 0.0098` assumes independence across calls; M0 measured neither the joint law nor a cure, and the determinism check had no threshold or consequence | **Accepted** | §2.7 E3 labels the 59.8% per-prompt rate [Rep] and the 0.0098 figure **[H]**, and makes **frozen once-generated replay tables** the mechanism every arm, resplit and P6 draw reads. The 50-question check gets a pre-registered tolerance and a stated consequence |
| Astra F10 | P2 | P10 called 0.961 a recall figure (it is rule-macro-F1; PAW-ft's controlled recall is 1.000), mixed slices, and let synthetic contrast pairs carry a real-text conclusion | **Accepted** | P10 is restated with metric, slice and synthetic provenance on every number, scoped to those cases. "Programs lose on fuzzy real text" becomes **P11, labeled [H]**, pending M5 |
| Astra F11 = Fable P2-1 | P2 | E4a's "radius removed → every cell, size 0.50" is false for skewed and multi-finalist cells, and `sign_exact` has no radius to remove | **Accepted** | §2.7 E4a pre-registers each detecting cell's own expected rate with its distribution, margin and assumed dependence: 0.970444 for the rare-large cell at n = 300, 0.96875 for the K = 5 any-of-five event, and a separate mutation for `sign_exact` [Rep calc §5b] |
| Fable P2-2 | P2 | M2's BANKING77 provenance check and the dataset-size recheck might read dataset text before the lock is hashed | **Accepted** | The M2 row restricts those checks to cards, papers and metadata; anything needing rows moves after the lock with a prespecified abort rule |
| Fable P2-3 | P2 | E1's and E3's inferential population was unstated, so an enumerated quantity could be reported only as "unpowered" | **Accepted** | Both experiments name the superpopulation estimand and its independent unit, and report the exact finite-population Δ beside every interval |
| Fable P2-5 | P2 | The plan pointed at an author-identity record that did not exist | **Accepted** | The provenance row now states that no identity was observable to the author lane, rather than pointing elsewhere |

**What both reviewers confirmed, so the fixes do not over-correct.** The EB formula and its
two-tail Bonferroni composition are correct for fixed policies, prespecified bounds and
independent confirmation units; independence *between contrasts* is not required. Reading
superiority, non-inferiority and equivalence from that one simultaneous interval needs no extra
penalty. E1's per-ratio `R_r` and M5's R = 2 are safe bounds. The v3 rare-large counterexample is
genuinely repaired. M5's intersection-union argument is valid for its conjunctive claim. The
download ordering is repaired. Both independently reproduced the rare-event probabilities, the
Clopper–Pearson cutoff, and the E1 regret figures.

## Delta re-review of the revision (Astra-requested lane, 2026-09-24)

Re-reviewed `58be8b4..6685d2a` only. Verdict: **NOT ACCEPTED — 0 P0, 3 P1, 3 P2**, counted as
residual defects rather than prior IDs. F7, F8, F10 and F11 are **closed**. The reviewer
independently reproduced the corrected E3 and M5 arithmetic (6,598 / 8,271 / 5,971 / 7,501;
7,318 / 6,592; 6,354 / 12,698 / 22,467; the S12 radii and 3,015) and confirmed `calc_v4.py` is
byte-identical to its saved output. Current digests: `calc_v4.py` sha256
`2c750e51…`, `calc_v4.out.txt` sha256 `97f464de…`.

| ID | Sev | Residual defect | Disposition | Fix |
|---|---|---|---|---|
| R1 | P1 | The planning arithmetic contradicted itself: §2.7 wrote `g = |true_delta| − margin` and then said `true_delta = 0` gives `g = margin`, which that equation makes `−margin`; and `calc_v4.py` §7 was **stale**, still printing g = 0 for NI, g = the true effect for superiority, E3 at R = 1.2 and M5 at K = 5 | **Accepted** | §2.7 now writes the **signed distance per mode**: NI uses `margin − true_delta`, superiority uses `−margin − true_delta` (= `|true_delta| − margin` for a candidate better by that much), equivalence at equality uses `margin`. `calc_v4.py` §7 is rewritten around a `distance(mode, true_delta, margin)` function and a table of real rows, and reproduces 7,318 (E3) and 12,698 (M5) |
| R2 | P1 | The narrowed custody claim was not propagated: §2.4 item 4 still claimed confirmation labels are outside the proposer's read set "as tested by B16", while §4.6 justified acceptance by the benchmark population and the newly edited E1/E3 rows target superpopulations | **Accepted** | §2.4 item 4 is scoped to a **host-path claim**, states that B16(b) detects one named fixture and that nothing detects memorization, and says plainly that **benchmark contamination is unresolved and limits inferential eligibility**. E1 and E3 carry that limit beside their estimands: E1's instrument is a frozen encoder plus our own head, so it is bounded there; E3's readers are pretrained, so its superpopulation reading is explicitly qualified |
| R3 | P1 | Admission is not an enforced bound on **candidate** GPU use: one container can open two allocator instances or allocate outside them, serialization does not cap the sum, and a 500 ms poll is detection after allocation | **Accepted** | §4.2 stops pretending the budget binds candidate code. **Candidate GPU work goes to Colab by default** — D-b's own fallback — and runs on tabputer-1 only if new test **B19** shows the `dmem` cgroup controller actually bounds amdgpu GTT for a rootless container. If B19 fails, candidates on this host get no devices and their GPU work moves to Colab. First-party runs keep the budget plus aggregate admission, one run at a time and the watchdog, which is adequate for code we wrote and review |
| R4 | P2 | §4.6 still said "candidate code runs without devices anyway", contradicting the new profile | **Accepted** | Both §4.6 bullets are rewritten around the B19 condition |
| R5 | P2 | `calc_v4.py` §6 and the risk row still called `0.598^9` the whole-question replay probability and prescribed a fixed batch composition | **Accepted** | §6 now separates the **measured** 59.8% per-prompt rate [Rep] from the **hypothetical** independence arithmetic [H], notes that M0's smoke test resubmitted the same prompt list and still disagreed, and names frozen replay tables as the mechanism. The risk row says the same |
| R6 | P2 | The 0.01-grid σ̂ figures had become exclusion rules: σ̂ = 0.242 needs 6,355 rows and fits, yet "≤ 0.24" would narrow | **Accepted** | §2.7 states that **the rule is the computation** — powered iff n(σ̂) ≤ available — and that every quoted σ̂ is a rounded-down illustration. `calc_v4.py` §7b computes the exact boundaries: 0.24368057, 0.26502213 and 0.53538055, matching the reviewer's values |

The reviewer found **no new P0 or P1** introduced by the revision: the weights custody split is a
viable manifest-verified read-only mount separate from labeled dataset caches, K = 6 and the
corrected E3/M5 arithmetic are sound, and the candidate-GPU change fixes reachability, with its
memory risk counted once under R3 and now answered by B19-or-Colab.

## Delta re-review of the revision (Fable 5.1 xhigh lane, 2026-09-24)

Verdict on `6685d2a`: **ACCEPTED — 0 P0, 0 P1, 4 P2 notes.** P1-A (E3's range and every dependent
threshold) and P1-B (the weights custody path) are closed, verified by the reviewer's own
recomputation; all eight original P2s are closed and not merely cosmetically. No new P0 or P1 was
introduced by the corrected arithmetic, the aggregate admission rule, the candidate-GPU change or
the weights path.

| # | P2 note | Disposition | Fix |
|---|---|---|---|
| 1 | The PAW-ft admission example assigned zero service memory despite needing a teacher server | **Accepted** | Service memory is declared separately and never assumed inside a run's GPU budget: PAW-ft is 38 + 16 + **9** + 8 + 6 = **77 GiB**, and E3's readers are 44 GiB |
| 2 | How `augctl` confirms a weight artifact carries no dataset labels, and how the HF dataset and hub caches are separated, was unstated | **Accepted** | §4.2 enforces the split through `HF_DATASETS_CACHE` and `HF_HUB_CACHE`, has `augwindow` refuse to close a window where a dataset repository landed under the weights root, and publishes only on a manifest digest match, a design-lock repository id, and a weights/config/tokenizer file-type check. It is stated to be a **provenance and file-type check, not a semantic scan** |
| 3 | No pre-registered handling for a wedged or reset GPU while a candidate holds the device | **Accepted** | New **B20**: heartbeat detection, container kill, `blocked(gpu_fault)` with the amdgpu message, and **no module reload, no GPU reset and no reboot** — if the device does not recover the maintainer decides at the console, and the arm moves to Colab |
| 4 | The powered-set gap wording mixed NI/equivalence with superiority | **Accepted (same as Astra R1)** | Fixed by the signed-distance-per-mode definition |
