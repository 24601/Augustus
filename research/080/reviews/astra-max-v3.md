# Astra v3 review of plan v3

Extracted from the final `codex` block of `astra-max-v3.raw.log` (session `01a0d0d9-fa9f-7013-8f5f-7e246e18f053`). Requested `gpt-6-astra`, `model_reasoning_effort=max`; the Codex header reports the same (CLI configuration, not proof of the serving model).

Requested routing: gpt-6-astra, model_reasoning_effort=max (codex exec)

**NOT ACCEPTED — 3 P1 and 4 P2 findings. No remaining P0 established.**

Reviewed [plan-v3.md](research/080/plan-v3.md), SHA-256 `b502c549b0f05fc4cb0692717d597f3a3123de5860954352e9650965e06eacf8`, its dispositions, both generations of prior reviews, the arithmetic, and both new source cards. Line references below identify that unchanged plan.

The arithmetic script reproduced its saved output byte for byte. I also independently recomputed the calculations used below. No files were written, network requests made, credentials read, or tabputer isolation tests executed. Resolution in this review means resolution of the specification, not proof that future controls work.

1. **P1 — The shared staging directory exposes confirmation labels to candidates.**

   **Quote:** §4.2, L511–514: “Public datasets … are fetched by `augexp`” and “moved under `/srv/aug/stage/` … read-only to `augexp`.” L518–519 mounts “`/stage` … read-only” in containers. E4c, L278 nevertheless promises: “Read of confirmation labels → not mounted, and EACCES on the host.”

   **Failure path:** Downloaded public datasets contain labels before partitioning. A candidate can recover confirmation labels from those original datasets in `/stage`, matching by text or identifier, despite being denied `/srv/aug/ctl`. Read-only access prevents modification, not label lookup. B6 can pass while this route remains open. Setup caches retained under `augexp` create the same problem.

   **Minimum correction:** Have a trusted acquisition/splitting stage retain complete labeled datasets outside the candidate’s access. Expose only explicitly permitted partitions and label-free confirmation inputs through per-run mounts. Account for download caches and intermediate copies. Add an adversary that reconstructs confirmation labels from the original downloaded corpus; it must fail.

2. **P1 — The new family-error guarantee does not follow from the specified normal/bootstrap intervals.**

   **Quote:** §2.7, L216–221: “the probability of any false claim across the m contrasts is at most α”; “The interval is normal-theory”; below 500 discordances, “a paired percentile bootstrap … and the wider of the two intervals is used.”

   **Failure path:** Bonferroni requires valid individual coverage. Neither proposed interval provides that guarantee for arbitrary bounded, sparse loss differences.

   A constructed counterexample: let a paired difference equal `0.98` with probability `0.0001`, otherwise zero. Its true mean is **0.000098**, outside an equivalence margin of **±0.00005**. At **12,850** confirmation rows, the probability of observing no nonzero difference is:

   `0.9999^12850 = 0.2766328082`.

   On that event, both intervals collapse to `[0, 0]` and falsely certify equivalence. If a separate 3,000-row calibration pilot also misses the event, its estimated variance is zero and L226 can designate the contrast powered. The joint probability is **0.2049315506**. Taking the wider of two degenerate intervals supplies no protection.

   **Minimum correction:** Use intervals with justified coverage under the declared loss and sampling assumptions for any asserted error guarantee. Include zero-discordance and rare-large-loss cases. Alternatively, explicitly limit these procedures to approximate inference and remove the unconditional “at most α” claim. E4’s tests of Hoeffding/EB do not validate this separate normal/bootstrap procedure.

3. **P1 — M0 and M2 impose contradictory download prerequisites.**

   **Quote:** §2.7, L206: “The design lock comes before any download or data read.” §7, L729 puts “B1–B14; GPU acceptance” in M0. L731 makes M2 depend on M0 and assigns M2 the design locks, “Hashed before any download.”

   **Failure path:** M0 cannot complete B13 without the PyTorch and model acceptance tests in §4.4. The inventory states that PyTorch is absent. Obtaining those dependencies requires downloads, but the required design lock cannot occur until M0 completes. The proxy allowlist is itself named at the design lock, L533.

   **Minimum correction:** Separate authorization/provisioning from dependency acquisition and acceptance testing. Sequence the work as: provisioning decisions → design locks → authorized downloads/setup → boundary and GPU acceptance → experiments. Preserve the requirement that experiments cannot start before their applicable tests pass.

4. **P2 — E3’s finite-population truth requires the maximum replay budget, not the advertised planned subset.**

   **Quote:** §2.7, L269: P6 uses “finite-population truth (all 7,405 questions).” L266 plans “1,000 search … plus 3,500 confirmation.” L267 gives “Planned 81,000 … 1.7B-only fallback 36,360” calls.

   **Failure path:** Replaying 4,500 questions cannot establish the specified truth over all 7,405. Using only observed questions silently changes P6’s target population; obtaining the missing answers changes the planned workload.

   At the stated nine calls per question, full replay requires:

   - Two readers: **7,405 × 9 × 2 = 133,290 calls**.
   - One reader: **7,405 × 9 = 66,645 calls**.

   The two-reader requirement exceeds the advertised planned workload by **52,290 calls**. The maximum budget already contains it, but the fallback does not.

   **Minimum correction:** Make full replay the planned workload whenever P6 targets all 7,405 questions, and include it in timing-based narrowing. Alternatively, preregister a smaller finite population and restrict P6’s claim to it. Keep its truth data unavailable to selection.

5. **P2 — §3.6 covers missing parents, but leaves the newly observed disputed-lineage case unresolved.**

   **Quote:** §3.6, L449–453: “TypeSafe/Jev, its aliases and declared Jev-derived corpora … are barred”; “A named approval can clear `unknown`”; “Missing parents make lineage unknown.”

   **Failure path and source assessment:**

   - **Jev-Omni:** Missing training-data parents correctly imply `unknown`. Its name does not establish TypeSafe identity, and its no-Jev-output attestation does not disclose those parents. Its derivatives inherit the unresolved lineage. A substring-based alias rule would incorrectly bar it.
   - **`LocalLLaMA/typed-decisions`:** The saved dataset card leaves the teacher unnamed. The saved `Manavarya09/verdict` README alleges Jev labels. The dataset’s statements about independence and affiliation do **not** identify the teacher or disprove that allegation. Neither the allegation nor its applicability to the exact revision is established.

   V3 does not specify how sourced allegations enter the graph or affect the generic `unknown` approval route. Consequently, it does not implement the CLM card’s proposed “barred pending resolution” treatment. That proposed treatment is a policy choice, not proof of Jev ancestry.

   **Minimum correction:** Add both concrete cases, canonical identity resolution, and a rule for sourced, disputed lineage tied to artifact revisions. Decide explicitly whether the disputed case stays blocked pending resolution or permits named risk acceptance. An approval must preserve the outstanding allegation and must not be described as verified lineage clearance.

6. **P2 — S12 prescribes inconclusive results from sample count alone.**

   **Quote:** §3.7, L483: “S12: 1 pp margin, 3k rows | Required n shown; inconclusive predicted; margin not widened.”

   **Failure path:** Method, mode, variance and planning effect determine feasibility. The scenario supplies none of them. Under M5’s own EB formula, with `K=3`, `α=0.05`, `n=3000`, zero observed mean difference and zero sample variance, the radius is:

   `14 × ln(120) / (3 × 2999) = 0.0074496926`.

   That is below the **0.01** non-inferiority margin. A valid response can therefore certify non-inferiority, while the scenario requires it to predict inconclusive. This repeats the earlier small-sample slogan problem.

   **Minimum correction:** Specify the method, mode, family, variance assumption and planning effect. For example, EB at equality with `σ=0.10`, `K=3` has the stated approximate requirement of **5,025** rows. Include a feasible low-variance countercase.

7. **P2 — The memory blocker and its attribution are stale under the supplied errata.**

   **Quote:** Provenance, L16: “k3s and other workloads hold about 108 GB of RAM today.” §4.5, L591–593: “Today about 16 GB is free … runs stay `blocked(memory)`.” Decision 22, L795 repeats that condition.

   **Failure path:** The coordinator identifies the large allocation as the stopped vLLM server in `vllm-strix`, and reports **115.7 GiB MemAvailable out of 124.9 GiB**. That exceeds the proposed launch floor. Following the plan would preserve a nonexistent memory blocker and incorrectly attribute it to k3s.

   **Minimum correction:** Update the provenance, §4.5 and decision 22 with the dated correction. Retain the chosen cap and live launch/abort checks; derive `blocked(memory)` from the launch measurement.

The prior P0/P1 findings resolve as follows. **F** denotes Fable; **A** denotes Astra.

| Prior finding | Verification against v3 |
|---|---|
| v1 F P0-1 / A1; v2 F P0-1 / A1 | **Original exposure addressed.** Patrol removed; candidate execution moved off the Mac; enforced network controls specified. Locally checked: home, `.codex` and `.local` are 700; `.zshrc` and HF token are 600. No tabputer boundary execution is claimed. Finding 1 concerns a separate confirmation-data exposure. |
| v1 F P1-1; v2 F P1-1 / A6 | **Resolved.** Local refs match `d8dc848` and released `v0.7.2 → 30b6033`. Independently counted 16 references totaling 173,472 bytes and SKILL.md at 10,743 bytes. The committed ignore change now has an unreleased vehicle. |
| v1 F P1-2 | **Resolved.** The public patch is recorded as released; it is no longer an outstanding confidential-plan publication step. |
| v1 F P1-3 / A6 | **Resolved.** X2 is a commitment with a task-success/cost subclaim; X3 includes adaptation cost, L134–135. |
| v1 F P1-4 / A8; v2 F P1-4 / A3 | **Original requested corrections present.** Plug-in naming, comparator encoding, retraining arms, 19 contrasts, machinery controls, larger data and inconclusive outcomes are specified. Synthetic planning arithmetic reproduces. Finding 2 prevents accepting the new coverage guarantee. |
| v1 F P1-5 / A7 | **Resolved.** H-DPO is bounded; GRPO/KTO receive credit; learned instruments/proposers remain allowed; P7 is discussion only. |
| v1 F P1-6 / A10; v2 F P1-3 / A2 | **Original reachability defects resolved.** T1 cannot establish the margin; comparisons target R3a; real tasks and an inconclusive outcome exist. EB requirements reproduce as 5,025 / 10,175 / 18,136 under the script’s normal-power approximation. Finding 6 is a new scenario regression. |
| v1 F P1-7 / A4 | **Partially resolved.** Statistical, eligibility and isolation tests are separated and scripted. Confirmation isolation remains incomplete under finding 1. |
| v2 A5 | **Original E4a qualification defect resolved.** Simultaneous upper bounds replace the invalid lower-bound rule; tolerance and diagnostic limitations are explicit. Independently computed CP upper bounds: 2,049/40,000 → **0.0549748563**; 2,050/40,000 → **0.0550006938**, confirming the cutoff. |
| v2 F P1-2 / A4 | **Original E3 sample-size mismatch resolved.** The revised formula gives **3,457.1028**, requiring 3,458 integer observations; the planned 3,500 covers that. Fallback requires 3,040. Finding 4 concerns the additional P6 workload. |
| v1 F P1-8 | **Resolved as a decision gate.** M9 requires counsel’s answer or explicit risk acceptance. No legal clearance is established. |
| v1 F P1-9 / A12 | **Original graph/permission defects resolved in specification.** Selection, filtering, features, inheritance, channels and missing permission evidence are covered. The new disputed-source case needs finding 5’s disposition. |
| v1 F P1-10 / A13 | **Deferred explicitly.** No unattended-maintenance capability is claimed; §5.2 retains prerequisites. |
| v1 A2 | **Resolved.** `sign_exact` is restricted to binary, zero-margin direction testing with an explicit p-value rule. The magnitude counterexample is refused. |
| v1 A3 | **Resolved.** Unsupported unequal-probability confirmation is refused; sampling-unit semantics are required. |
| v1 A5 | **Resolved.** Ownership, implementation and enforcement are distinguished; unknown and retain outcomes exist. |
| v1 A9 | **Resolved in specification.** Observability and identification are separate; unsupported causal comparisons stop. |
| v1 A11 | **Resolved in specification.** Mandatory tasks use human-written text with a provenance check; WANLI remains a separately labeled generated-text stress test. |
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
