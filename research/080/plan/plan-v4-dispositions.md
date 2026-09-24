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
