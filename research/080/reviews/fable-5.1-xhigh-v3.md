# Independent adversarial re-review of the Augustus 0.8.0 plan (plan-v3.md)

Requested routing: claude-fable-5-1, effort xhigh

Observed identity: my environment states, verbatim, "You are powered by the model named Fable 5.1. The exact model ID is claude-fable-5-1." A system-context line in this session, following the task turn, states, verbatim, `<reasoning_effort>80</reasoning_effort>`. So: requested "xhigh", observed "80"; the mapping between the two labels is unknown to me, and I do not claim they are the same setting. (The v1 and v2 Fable reviews wrote that no effort level was visible; that was true of those sessions and is not true of this one.)

Reviewer provenance. Read in full: `plan-v3.md` (813 lines), `plan-v3-dispositions.md`, `design-brief.md`, `reviews/fable-5.1-xhigh-v2.md`, `reviews/fable-5.1-xhigh.md`, the final `codex` block of `reviews/astra-max-v2.raw.log` (lines 4275–4524; the block is printed twice, identically), `calc/calc_v3.py`, `calc/calc_v3.out.txt`, `calc/calc_v2.py`, `calc/fable_v2_review_calc.py`, both Astra prompts. Read-only local checks from the main checkout (`HEAD 4236a60`, branch `main`; untracked `.claude/` present): `git rev-parse` of `origin/main` and `v0.7.2^{commit}`; `git ls-tree -r -l` byte sums of `.agents/skills/augustus/references/` and `SKILL.md` at `v0.7.2` and `origin/main`; `.gitignore` at `origin/main`; `.git/info/exclude`; `git remote -v`; `ls -ld`/`ls -lde`/`find -perm` on the home directory, `~/.zshrc`, `~/.zprofile`, `~/.cache/huggingface/token`, `~/.codex`, `~/.claude/settings.json`, `Augustus/.local`; `dscl . -list /Users UniqueID`; `id`; `shasum -a 256` of the four `calc/` files; a re-run of `calc_v3.py` diffed against `calc_v3.out.txt`; `grep -n` of `compare_workflows.py` and `check_repo.py`; `sed` of `validation.md` L156–160 at `origin/main`. **One network call, disclosed:** `git ls-remote origin refs/heads/main 'refs/tags/v0.7.2*'` over HTTPS to github.com (both remotes are HTTPS; no SSH was used; `ls-remote` writes no local refs). Only credential file *modes* were inspected; no secret value was read or printed; `.zprofile` was grepped for secret-name markers by count only (0). My arithmetic is the stdlib script in the appendix, run with Python 3.14.7; a first version of it was killed by me (`pkill`) for being too slow and rewritten. Nothing edited in the project tree except this file; my script and its output (and a harness-written background-task log) went to the session scratchpad, which is ephemeral and outside the project tree, which is why both are inlined below. Nothing posted. No SSH. No third-party code.

Confidential. Local only, in the sense qualified by P2-6 below.

---

## Verdict

**NOT ACCEPTED — 0 P0, 1 P1, 10 P2.** Every prior P0 and P1 (Fable v2 P0-1, P1-1 to P1-4; Astra v2 1 to 6) is **resolved in the plan's specification**; none is an implemented control yet, and the plan says so (B1–B14 gate M3 and M4). All 21 v2 findings are dispositioned, and every number I recomputed reproduces. The one P1 is a sequencing contradiction that the v3 revision introduced: the design lock is required to precede "any download", the milestone that writes it depends on the milestone that performs all 45 GB of downloads, and the lock hash is printed in the paper. It is cheap to fix. The P2s are specification gaps in the tabputer-1 profile and a few unstated parameters that the design lock would otherwise have to invent.

---

## Verification of prior P0/P1 dispositions

| Prior ID | v3 claim | Verified? | Evidence / residual |
|---|---|---|---|
| Fable v2 P0-1 / Astra v2 1 (Mac exposure; candidate account reaches transcripts and credentials) | No isolation claim on the Mac; `augpatrol`/`augcand` deleted; all experiments and candidate code to tabputer-1 under `augexp`/`augctl`, rootless podman `--network=none`, skuid nft drop; B1–B14 before any run | **Resolved in specification.** [Rep] Mac today: home `drwx------+` (ACL: `group:everyone deny delete` only); `~/.zshrc` 600; `~/.cache/huggingface/token` 600; `~/.codex` 700; `Augustus/.local` 700; second account `<second-local-account>` (uid 501, admin) still exists, as the plan says. Plan text: L15, L27–32, §4.1–4.6, §5.2 | Residuals are P2-1 (proxy cannot resolve names as specified), P2-2 (site source staged on tabputer-1 contradicts decision 21), P2-5 (disk not bounded), P2-8 (profile nits). None reopens the P0: nothing untrusted runs on the Mac, and the credentials the v2 review named are now unreadable by any non-root local account |
| Fable v2 P1-1 / Astra v2 6 (stale baseline; `.gitignore` vehicle) | `origin/main` = `d8dc848`; `v0.7.2` → `30b6033`; 16 files / 173,472 B; `SKILL.md` 10,743 B; ignore rule only in `.git/info/exclude`; vehicle = first 0.8.0 commit (decision 13) | **Resolved and now live-confirmed.** [Rep] local `origin/main` `d8dc848`; `v0.7.2^{commit}` `30b6033`; `.agents/skills/augustus/references/` at `v0.7.2` = 16 files, 173,472 B (headroom 6,528); `SKILL.md` 10,743 B; `origin/main:.gitignore` has no `.local/`; `.git/info/exclude:7` = `.local/`. **`git ls-remote` (HTTPS): GitHub `refs/heads/main` = `d8dc848`, `refs/tags/v0.7.2^{}` = `30b6033`.** The plan's "not fetched" label (L18) was honest and the numbers were right anyway. M1's "after `git fetch origin`" (L327) makes this robust from now on | A second remote `amp` (`ampcode.com`, `amp/main` = `d41e61f`) exists locally; it is not the plan's baseline and I did not query it |
| Fable v2 P1-2 / Astra v2 4 (E3 n contradicts margin and family) | m = 6, δ = 0.02, power 0.8: n = 3,457 at σ = 0.30; 1,000 search + 3,500 confirmation; n_conf = min(6,405, n(σ̂)); narrowing to m = 3 (n = 3,040); 24 GPU-h cap; calls 81,000 / 133,290 / 36,360 | **Resolved.** [Rep, appendix §5] 3,457; half-width at 1,200 = 0.0228; n(σ = 0.40) = 6,146; m = 3 → 3,040; calls 81,000 / 133,290 / 36,360; planted +0.05 power at 3,500 ≈ 1.000 | Superiority reads in the outcome row (L269) do not state their m (P2-3) |
| Fable v2 P1-3 / Astra v2 2 (M5 margin unreachable; T1 is fixture evidence) | Margin kept at 0.01; EB with K = 3; real-text T2a–T2c sized to it; intersection-union across tasks; explicit inconclusive row; T1 `fixture_evidence_only` | **Resolved.** [Rep, appendix §6] EB n = 5,025 / 10,175 / 18,136 at σ = 0.10 / 0.20 / 0.30; v2's 470 had radius 0.132 at K = 3; T2a 6,000 is powered up to σ ≈ 0.12, T2b 12,850 up to ≈ 0.23, T2c 40k / 60k up to ≈ 0.47 / 0.59, so the plan's grid statements (0.10 / 0.20 / 0.35) are conservative | Realistic expectation [H]: a 77-way task with ±1 paired differences on 7% of rows has σ ≈ 0.26, so T2a will probably be unpowered and the likely outcome row is "Narrowed" or "Inconclusive". The plan has those rows; that is the point of them. Escalate's LCB level is unstated (P2-9) |
| Fable v2 P1-4 / Astra v2 3 (E1 asymmetric; B duplicates the control; B-retrain underspecified; m wrong; controls misclassify outcomes) | Machinery controls only (identical frozen A; planted analytic effects over 200 redraws); B-stale and the second-fit comparison are outcomes; m = 19 enumerated; B-retrain_r and B-retrain_S defined; powered-set rule; full CivilComments (about 1.6M) | **Resolved.** [Rep] `calc_v3.py` §1 re-run is byte-identical; the synthetic planning figures in L247 (61k/192k, 91k/271k, 12k/33k; Δ −0.042/−0.053/−0.005; n_sup ≤ 5,442) match the output; 15 + 4 = 19 | Residuals: superiority m and the planning-gap rule are unstated (P2-3); the "second, equal-size fit subsample" has no source partition (P2-4); E1's CLINC decision is undefined (P2-9); B-stale's identity with the 0.5 plug-in holds only for intercept-free temperature scaling (P2-8) |
| Astra v2 5 (E4a qualification rule) | Coverage claim rests on theorems and exact-rational tests; MC diagnostic with C = 108, R = 40,000, simultaneous CP upper bounds against α + τ = 0.055; gross-defect detector; positive controls | **Resolved.** [Rep, appendix §1–2] C = 108; qualify iff adoptions ≤ 2,049 (CP upper 0.05497; 2,050 → 0.05500); false-fail at exactly 5% = 0.128, at 4.5% = 1.9e-9, at 6% ≈ 1. I also checked the one method that is nearly exact rather than conservative: `sign_exact`'s realized size, averaged over the random discordant count, is ≤ 0.0472 on a grid of n ∈ {300, 1,000, 2,500}, q ∈ {0.05…0.5}, K ∈ {1, 5}, so a correct `sign_exact` cell fails the v3 rule with probability ≤ 8e-5. No finding | Which cell class detects which planted defect is unstated (P2-7) |

Fable v2 P2-1 to P2-8 and Astra v2 7–8 are resolved as the dispositions state; residuals are folded into the P2s below.

**Other v3 numbers recomputed [Rep, appendix]:** E4d P(≥ 3 | 0.05) = 0.0755, power at 0.20 = 0.794; G0 0.5²⁰ = 9.5e-7; E4b sign case p = 0.0068, mean +0.0292; 50/950 case −0.667 vs +0.9; E4a 4.32M replications, 12.96M evaluations, 9.0 CPU-h, 18 min on 30 processes; E3 4B on CPU 103 h; critical path 13.5–15.5 and total 22.5–26.5 agent-days; CLINC 23,850 − 11,000 = 12,850; 2.0M − 400k = 1.6M. `calc/` sha256 prefixes match the plan and dispositions (`5d3a6d23`, `e75b6308`, `2b8fc816`, `b04af194`). `compare_workflows.py` L158 radius is `sqrt(2(log K − log α)/n)` as Sources row 47 states; `check_repo.py` L23/L26/L30 hard-code `SKILL_PATH`, 16,000 and 180,000 as §3.1 states; `validation.md` L156–160 at `origin/main` is the shadow-mode passage X5b cites.

---

## P1

### P1-1. The design lock must precede "any download", but the milestone that writes it depends on the milestone that performs every download, and the lock hash is printed in the paper

**Plan text.** §2.7 L206–207: "The **design lock** comes before any download or data read." §7 L731: "M2 | Design locks for E1, E3, E4 and M5; BANKING77 provenance check | **M0** | 1 | **Hashed before any download**." §7 L729: "M0 | … B1–B14; GPU acceptance; memory window confirmed." §4.5 L584: "Setup + B1–B14 | — | About 45 GB of downloads (venv 10–15 GB, weights 22 GB, **data 2 GB**)." §4.3 B13 L558 → §4.4 L569–573 (GPU acceptance needs the torch wheel, MiniLM and Qwen3-1.7B, and "MiniLM embeddings on GPU vs CPU … on 1,000 texts"). §4.2 L527–529: "`augexp` may reach only `lo` TCP 3128 (the proxy), **and only during setup** … At close, the proxy rule is deleted." §6.2 L656: "Front matter | Version, commit, and **both lock hashes**." §6.6 L706–707 adds a further proxy window ("gems fetched through the setup proxy, then network-none") that §4.2 does not schedule.

**What is wrong.** M2 depends on all of M0, and M0 includes the setup window in which the datasets are downloaded. Followed in the stated order, the design lock is written after the data are on disk, so its own precondition ("before any download or data read") and M2's exit criterion are false at the moment the hash is produced; the paper then prints that hash as evidence of pre-registration. The only other reading is that data download is deferred past M2, which needs a second proxy-open window that the plan neither schedules nor follows with a B10 re-run, and §6.6 already implies a third window for gems. The plan also does not say what texts B13's MiniLM and Qwen checks use; if they are dataset texts, GPU acceptance is itself a "data read" before the lock.

**Failure path.** (1) The maintainer runs M0 as written, downloads the 2 GB of data, then writes and hashes the design lock at M2; a reader of the paper's front matter or `/evidence/` compares the lock date with the setup receipt (which §4.3 requires to be dated) and finds the order inverted. (2) Or the maintainer, noticing this, re-opens the proxy after M2 in an unrecorded window; while the `augexp` proxy rule exists, any container started without `--network=none` by mistake has egress, and B10 (the closed-state proof) is stale. Either way the lock's evidentiary value, which is the reason the plan has two locks (Fable v2 P2-3, accepted), is undermined by the schedule that surrounds it.

**Minimum correction.**
1. M2 depends on "M0 decisions" only (as M1 already does, L730); M0's dataset download step depends on M2's hash. Split the setup row in §4.5 and §4.3 into a provisioning window (venv, base image, weights; B1–B14; GPU acceptance on first-party or synthetic texts, stated) and a data window that opens only after M2.
2. Restate L206–207 to what is meant: "before any dataset download or any read of dataset text or labels"; say explicitly that wheels, the base image and model weights are not data. If the intent really is "before any download at all", then GPU acceptance cannot sit in M0 and the plan must say where it goes.
3. Every proxy window (provisioning, data, gems) is named in §4.2, maintainer-attended, followed by a B10 re-run and a dated receipt, with a rule that no experiment or candidate container runs while an `augexp` proxy rule exists.
4. `/evidence/` (§6.3 L667) shows the setup-window receipts beside the lock dates, so the order is checkable by a reader.

---

## P2

### P2-1. As specified, the setup proxy cannot resolve a hostname, so B9's only "succeeds" case fails

§4.2 L509: "`augproxy` | … | TCP 443 to public addresses; private and loopback ranges dropped." L531: "`augproxy`: TCP 443 only, never to private ranges." L527–528: `augexp` gets no DNS ("Everything else is logged, counted and dropped: DNS, …"). A CONNECT proxy receives `CONNECT huggingface.co:443` and must resolve the name itself: either through the local stub resolver (loopback, dropped) or through an external resolver on UDP/TCP 53 (not 443, dropped). B9 L554 expects "a named host through the proxy" to succeed; it cannot. This fails closed, hence P2, but it blocks the whole setup. **Correction:** allow `augproxy` UDP/TCP 53 to the configured resolver only (or loopback to the stub), log those queries, and add the resolver to B9's expected-success list and to the design-lock allowlist (L533–536). Alternatively the proxy resolves over DoH to a named resolver on 443; say which.

### P2-2. The site build on tabputer-1 stages the paper there, contradicting the "run bundles and public data" scope

§4.1 L495: tabputer-1 is "Never used for: Holding the plan, reviews, research notes …". §4.6 L599–600 and decision 21 L794: "Stage only run bundles and public data." §6.6 L706–708: "the Pages-equivalent build and `check_site.py` run on tabputer-1 in a container … The built `_site` is copied back." The site source under `docs/exogenous-policy/` (L660) is the paper's argument, explorables and `/evidence/`; the build needs it on tabputer-1, readable by root, the maintainer's root-equivalent account and privileged k3s workloads (L597–600). This is a scope contradiction, not a new exposure class (decision 21 already accepts those readers), but the plan states the boundary twice and then crosses it silently. **Correction:** either extend decision 21 and §4.1 to name the site source as staged content, with the same acceptance, or move the container build to after §2.9 condition 1 (confidentiality lifted). Note that the maintainer can still review the hand-written pages on the Mac with `python3 -m http.server` before any Jekyll build, since §6.6 forbids frameworks and CDNs.

### P2-3. Superiority reads do not state their margin, and the powered-set rule has an unstated planning gap

§2.4 L155: "Superiority holds when UCB < −m (m ≥ 0)." E1 L248 says "B-retrain_r superior to A **by more than δ_r**", but L249 "B-stale superior to A" and L250 "A is superior to B-stale" say nothing, and E3 L269 "superior for every powered reader" likewise. `calc_v3.py` §1 plans A−B-stale with gap = |Δ| − δ_r, so the lane's intent is superiority by δ_r; the plan does not say so. Separately, L224–225 defines the one-sided n with "gap g between the truth and the bound", and L226 makes a contrast "powered" when that n fits, but nowhere says what g is at the analysis lock (the calibration-split Δ̂ minus m? a fixed planning effect?). Without that rule the powered set, which decides which outcomes count (L227–228), has a free parameter chosen after calibration data are seen. **Correction:** state m for every superiority read in E1, E3 and M5 (δ_r / 0.02 / 0.01, or 0), and fix the g rule in §2.7 for the design lock, for example g = max(|Δ̂_cal| − m, 0) with Δ̂_cal from the calibration split, or a fixed planning effect per contrast type; record the g used per contrast in the analysis lock.

### P2-4. The "second, equal-size fit subsample" has no partition to come from

E1 L241: "fit 200k; calibration 100k; M5 pool 100k; confirmation the rest, about 1.6M." L252: "A fitted on a second, equal-size fit subsample vs A." A second disjoint 200k does not exist unless it is carved from confirmation (leaving 1.4M; `calc_v3.py` uses 1.6M) or the fit split is halved (then A itself is fit on 100k). **Correction:** name the source at the design lock and propagate the number to L241, L247 and `N_CONF_CIVIL`.

### P2-5. Disk exhaustion is not bounded by anything the plan names

E4c L278: "Resource exhaustion → cgroup limits and timeout." §4.2 L522: `/work` is "bound to a fresh per-run directory" on the host; L16: 688 GB free on the LUKS disk shared with k3s. cgroups bound memory and pids, not writes to a bind mount; B12 L557 tests memory and forks only. A candidate, or a buggy first-party run, can fill the shared disk and stall k3s/etcd, which is the failure the memory envelope (L591–593) was built to avoid. **Correction:** put `/srv/aug/runs` (and `/srv/aug/pred`) on a size-bounded filesystem (a loop-mounted image, an XFS project quota, or a sized tmpfs for candidates) and add a B12 sub-test: a write beyond the quota returns ENOSPC inside the container only.

### P2-6. The confidentiality statement omits the exposure the plan itself relies on

L3: "Confidential and local only. Nothing has been pushed, posted or filed." §6.6 L709: "confidential content never goes to Stitch or similar tools." §4.1 L494 lists "delegate reviews" as a Mac use. Delegate reviews send the full plan to hosted inference providers (Codex sessions in `~/.codex/sessions`; this review is a Claude Code session); that is a deliberate, maintainer-requested disclosure under those providers' API terms, and it is not "local only". **Correction:** one sentence in the header and in the §4.1 Mac row: "shared in full with the inference providers used for review, under their API data terms [C, recheck]; not posted, pushed or filed." AGENTS.md asks that provenance be preserved; the plan's own reviewers are part of it.

### P2-7. E4a positive controls: say which cell class must detect each planted defect, and fix the planning effect

L276: "three planted gross defects must fail: radius removed, Δ sign flipped, radius n inflated 100×." [Rep, appendix §3] At the boundary null the sign-flip defect produces **zero** adoptions in every superiority-mode cell (UCB(+m) > −m always), so it is invisible to the size test there and detectable only in non-inferiority cells or in the power report; "n inflated 100×" is invisible in Hoeffding cells at σ ≤ 0.3 (size 0.007–0.2) and visible at σ = 1 (0.40). The diagnostic as a whole does fail, so the claim is true, but a partial pattern will be misread unless the expected detecting cells are named. Also "power at the planning effect is reported per cell" names no planning effect, and the K = 5 cells do not say whether the counted event is any-of-five adoption (the Bonferroni claim) or per-finalist. **Correction:** a small table: defect → cell class that must fail, with the expected rate; the planning effect per distribution; the K = 5 event.

### P2-8. tabputer-1 profile and boundary-test nits

- L508: `augctl` "Groups: Own group" yet reads predictions "through a group"; name the shared group (`augpred`), the setgid directory and who is in it.
- L555 B10: a `--network=none` container has only loopback, so "connect to host IPs" fails at ENETUNREACH inside the netns and does not increment host nft counters; only the "start a container with networking" sub-test does. Adjust the pass criterion so a non-incrementing counter is not read as a failure.
- L522 "runs are sequential until B14 passes" contradicts L542 "all must pass before any run"; delete the clause or say B14 uses test containers.
- L550 B5 "Zero hits": `/etc` contains `ssh_host_*_key.pub`, `/etc/ssl`, and unit files with `Key=`; define the marker regex and the allowlist of expected public matches, or the test cannot pass.
- L585 vs L591–593 and decision 22: E4a is "about 20 min on 30 processes" under a one-run-at-a-time envelope on a box whose CPU is shared with k3s; the 9 CPU-h serial figure exceeds the 4 h E4a cap unless ≥ 3 processes are used. Add `--cpus` or `nice` and state the process count.
- L211/L214 "before any confirmation read": `augexp` must read confirmation **texts** to write predictions, while `augctl` holds the **labels** (L508). Say whether texts are released to `/stage` only after the analysis lock (recommended) or whether "read" means labels and scoring only.
- L121 "B-stale … equals the plug-in frozen at 0.5 on the same scores" holds only if the L118/L242 calibration is temperature-only (no intercept); Platt scaling moves the 0.5 crossing. State "temperature, no intercept" for the no-shift arm, or drop the "equals" clause.

### P2-9. M5 and E1 parameters left to the lock

- L376 Escalate "EB LCB(Δ) > +0.01": level unstated; α/3 one-sided, matching the UCB, keeps the per-task false-claim rate at α.
- L373 T2c "40,000, expandable to 60,000": the trigger should be the analysis-lock n(σ̂) rule as in E3 L266, not a discretionary expansion.
- L241/L244 E1's secondary family: the CLINC150 binary decision (route vs abstain? what is an FP and an FN?) and its score s(x) are never defined for E1, although the m = 19 family and the margin rule apply to it; §3.3 T2b defines it only for M5.

### P2-10. Provenance nits

- L15 [Coord]: "`~/.codex` and `Augustus/.local` recursively go-rwx." [Rep] Top-level directories are 700, but 918 of 12,987 files under `~/.codex` and 3,191 of 17,294 under `.local` still carry group/other read bits, and 298/107 directories carry go-x. Harmless behind 700 parents and immaterial because no Mac isolation claim is made; the row should say "top-level 700". `~/.zprofile` is 644 with no secret-name markers.
- L190 P1 "+154% at 1:9, +364% at 1:19" comes from an earlier synthetic population; `calc_v3.py` §1's population gives +95% and +216% at the same ratios (0.0586/0.0300, 0.0613/0.0194). Cite which synthetic the claim row uses, or update it to the v3 population.
- L588 / `calc_v3.py` §5: the R1 token estimate uses T2c = 80,000 rows against the plan's 100k pool and 40–60k confirmation; immaterial to the hour figure, but align.

---

## What v3 gets right (so the fixes do not over-correct)

- Moving every experiment and all untrusted code off the Mac and declaring that no isolation claim rests on it is the correct answer to the v2 P0; the tabputer-1 profile (unprivileged principals, rootless podman, `--network=none`, skuid nft drop, per-run `/work`, `augctl`-owned labels, B1–B14 as a gate) is the right shape and is honest about what it does not claim (§4.6).
- The two-lock pre-registration with the grader refusing to score without the analysis-lock hash is a real mechanism, which is why P1-1 matters.
- The family rule, the powered-set rule with symmetric outcome rows, margins fixed by rationale and never moved, explicit inconclusive rows, and machinery-only controls answer the v2 E1/E3/M5 findings squarely; every n I recomputed reproduces.
- E4a now separates the coverage claim from the diagnostic and states the diagnostic's own error properties; the `sign_exact` cells survive my exact check.
- The baseline is live-correct, and M1's fetch-first rule prevents a fourth recurrence.

## Not covered

No `make check`. I did not re-read the arXiv or dataset-card sources; the dataset sizes and licenses in L241, L260, L371 match my recollection and remain "C, recheck at M2" as labeled. I did not test podman, nftables or ROCm behavior; §4.2–4.5 findings are from the specification. I did not open the `amp` remote.

---

## Appendix: arithmetic script (stdlib; Python 3.14.7) and output

```python
"""Independent arithmetic for the v3 re-review. Stdlib only, Python 3.14."""
from math import comb, exp, lgamma, log, sqrt
from statistics import NormalDist
import sys

ND = NormalDist(); z = ND.inv_cdf; Phi = ND.cdf
A = 0.05

def lpmf(n, i, p):
    return lgamma(n + 1) - lgamma(i + 1) - lgamma(n - i + 1) + i * log(p) + (n - i) * log(1 - p)

def bcdf(n, x, p):
    if x < 0: return 0.0
    if x >= n: return 1.0
    return min(1.0, sum(exp(lpmf(n, i, p)) for i in range(0, x + 1)))

def bsf(n, x, p):  # P(X >= x)
    return 1.0 - bcdf(n, x - 1, p)

def cp_upper(x, n, gamma):
    if x >= n: return 1.0
    lo, hi = x / n, min(1.0, x / n + 0.02)
    for _ in range(50):
        mid = (lo + hi) / 2
        if bcdf(n, x, mid) > gamma: lo = mid
        else: hi = mid
    return hi

print("== 1. E4a v3 rule: C=108, gamma=0.05/108, R=40,000, tol=0.055"); sys.stdout.flush()
C = 2 * 2 * 3 * 2 * 4 + 3 * 2 * 2
print(f"  C={C}")
R, gam, tol = 40_000, 0.05 / 108, 0.055
xmax = max(k for k in range(2040, 2060) if cp_upper(k, R, gam) <= tol)
print(f"  xmax={xmax}  CP_upper(xmax)={cp_upper(xmax,R,gam):.5f}  CP_upper(xmax+1)={cp_upper(xmax+1,R,gam):.5f}")
for p in (0.05, 0.045, 0.048, 0.049, 0.0495, 0.06):
    print(f"  P(fail | true rate {p}) = {bsf(R, xmax+1, p):.3e}")
sys.stdout.flush()

print("\n== 2. sign_exact realized size (exact binomial on discordant pairs), averaged over D~Bin(n,q)")
def size_given_d(d, a):
    if d == 0: return 0.0
    pm = [exp(lpmf(d, i, 0.5)) for i in range(d + 1)]
    tail = [0.0] * (d + 2)
    for k in range(d, -1, -1):
        tail[k] = tail[k + 1] + pm[k]
    k = min(k for k in range(d + 2) if tail[k] <= a)
    return tail[k]
def realized(n, q, a):
    mu, sd = n * q, sqrt(n * q * (1 - q))
    lo, hi = max(0, int(mu - 7 * sd)), min(n, int(mu + 7 * sd) + 1)
    return sum(exp(lpmf(n, d, q)) * size_given_d(d, a) for d in range(lo, hi + 1))
print("  n     q     K   size    P(cell fails v3 rule)")
worst = (0, None)
for n in (300, 1000, 2500):
    for q in (0.05, 0.10, 0.20, 0.30, 0.50):
        for K in (1, 5):
            s = realized(n, q, A / K)
            fam = 1 - (1 - s) ** 5 if K == 5 else s   # K=5: familywise over 5 independent boundary-null finalists
            pf = bsf(R, xmax + 1, fam)
            if pf > worst[0]: worst = (pf, (n, q, K, fam))
            print(f"  {n:5d} {q:.2f}  {K}   {fam:.4f}  {pf:.3e}")
        sys.stdout.flush()
print(f"  worst false-fail over grid: {worst[0]:.3e} at (n,q,K,size)={worst[1]}")

print("\n== 3. Which planted defect is visible in which cell (boundary null, normal approx)")
def hoeff(n, k=1): return 2 * sqrt(log(k / A) / (2 * n))
def eb(s, n, k=1):
    d = A / k
    return s * sqrt(2 * log(2 / d) / n) + 7 * 2 * log(2 / d) / (3 * (n - 1))
for s in (0.1, 0.3, 1.0):
    for n in (300, 2500):
        rh, re_ = hoeff(n), eb(s, n)
        print(f"  sigma {s} n {n}: radius-removed size={Phi(0):.2f}; n*100 (radius/10): Hoeff {Phi(-rh/10*sqrt(n)/s):.3f} EB {Phi(-re_/10*sqrt(n)/s):.3f}; sign-flip: superiority-mode size=0 (invisible to the size test); NI-mode adopts ~always iff radius {re_:.3f} < 2*m_NI")

print("\n== 4. E1 partitions")
tot = 2_000_000
print(f"  fit 200k + cal 100k + M5 100k = 400k; remainder {tot-400_000:,}; a second 200k fit subsample leaves {tot-600_000:,}")
print(f"  CLINC 23,850 - 8,000 - 3,000 = {23_850-11_000:,}")

print("\n== 5. E3 checks")
zf6, zf3 = z(1 - A / 12), z(1 - A / 6)
print(f"  z(m=6)={zf6:.4f} n_TOST(.30,.02)={((zf6+z(.9))*.3/.02)**2:,.0f}; HW@1200={zf6*.3/sqrt(1200):.4f}; n at sigma .40={((zf6+z(.9))*.4/.02)**2:,.0f}; m=3 n={((zf3+z(.9))*.3/.02)**2:,.0f}")
print(f"  calls: {4500*2*9:,} {7405*2*9:,} {4040*9:,}; planted +0.05 power at n=3500: {Phi(0.05*sqrt(3500)/0.30 - zf6):.4f}")
print(f"  binary EM paired diff: disagreement 20% -> sigma ~ {sqrt(0.2):.2f}; 10% -> {sqrt(0.1):.2f}")

print("\n== 6. M5 checks (K=3)")
def ebn(s, K=3, m=0.01):
    lo, hi = 50, 2_000_000
    f = lambda n: Phi((m - eb(s, n, K)) * sqrt(n) / s)
    while lo < hi:
        mid = (lo + hi) // 2
        if f(mid) >= 0.8: hi = mid
        else: lo = mid + 1
    return lo
print(f"  EB n: {ebn(.10):,} {ebn(.20):,} {ebn(.30):,}; Hoeffding radius at 470, K=3: {hoeff(470,3):.3f}")
print(f"  T2a 6,000 powered up to sigma: {max(s/100 for s in range(5,40) if ebn(s/100) <= 6000):.2f}; T2b 12,850: {max(s/100 for s in range(5,40) if ebn(s/100) <= 12850):.2f}; T2c 40k: {max(s/100 for s in range(5,60) if ebn(s/100) <= 40000):.2f}; 60k: {max(s/100 for s in range(5,60) if ebn(s/100) <= 60000):.2f}")
print(f"  77-way, misroute 1/abstain .3: if rungs disagree on 7% of rows with +-1 diffs, sigma ~ {sqrt(0.07):.2f} (T2a then unpowered)")

print("\n== 7. E4d, G0, E4b")
tail = lambda n, p, k: sum(comb(n, i) * p**i * (1-p)**(n-i) for i in range(k, n+1))
print(f"  E4d P(>=3|.05)={tail(20,.05,3):.4f} power@.2={tail(20,.2,3):.3f}; G0 0.5^20={0.5**20:.2e}; E4b p={sum(comb(33,k) for k in range(10))/2**33:.4f} mean={(9-0.24)/300:.4f}; 50/950: {(10-50)/60:.3f} vs {(950-50)/1000:.1f}")

print("\n== 8. E4a runtime and setup sizes")
print(f"  108*40000={108*40000:,}; x3={108*40000*3:,}; *2.5ms={108*40000*3*0.0025/3600:.1f} CPU-h; /30={108*40000*3*0.0025/3600/30*60:.0f} min")
print(f"  E3 4B CPU: {4950/60*4500/3600:.0f} h; milestones critical path {1.5+4+2+3+2+1}-{1.5+5+2+3+3+1}; total {1.5+4+2+3+2+1+1+2+6}-{1.5+5+2+3+3+1+1+2+8}")
```

Output (2026-09-23, this lane):

```
== 1. E4a v3 rule: C=108, gamma=0.05/108, R=40,000, tol=0.055
  C=108
  xmax=2049  CP_upper(xmax)=0.05497  CP_upper(xmax+1)=0.05500
  P(fail | true rate 0.05) = 1.283e-01
  P(fail | true rate 0.045) = 1.889e-09
  P(fail | true rate 0.048) = 1.345e-03
  P(fail | true rate 0.049) = 1.961e-02
  P(fail | true rate 0.0495) = 5.516e-02
  P(fail | true rate 0.06) = 1.000e+00

== 2. sign_exact realized size (exact binomial on discordant pairs), averaged over D~Bin(n,q)
  n     q     K   size    P(cell fails v3 rule)
    300 0.05  1   0.0298  2.669e-11
    300 0.05  5   0.0216  2.717e-11
    300 0.10  1   0.0353  2.673e-11
    300 0.10  5   0.0296  2.781e-11
    300 0.20  1   0.0386  3.088e-11
    300 0.20  5   0.0349  2.572e-11
    300 0.30  1   0.0397  2.648e-11
    300 0.30  5   0.0376  3.001e-11
    300 0.50  1   0.0421  2.450e-11
    300 0.50  5   0.0401  2.535e-11
   1000 0.05  1   0.0377  3.143e-11
   1000 0.05  5   0.0344  2.609e-11
   1000 0.10  1   0.0403  2.702e-11
   1000 0.10  5   0.0384  2.898e-11
   1000 0.20  1   0.0432  2.523e-11
   1000 0.20  5   0.0406  2.472e-11
   1000 0.30  1   0.0444  5.755e-11
   1000 0.30  5   0.0420  2.231e-11
   1000 0.50  1   0.0457  9.854e-08
   1000 0.50  5   0.0435  2.374e-11
   2500 0.05  1   0.0414  2.100e-11
   2500 0.05  5   0.0392  2.805e-11
   2500 0.10  1   0.0438  2.581e-11
   2500 0.10  5   0.0414  2.288e-11
   2500 0.20  1   0.0457  9.223e-08
   2500 0.20  5   0.0435  2.333e-11
   2500 0.30  1   0.0464  2.784e-06
   2500 0.30  5   0.0447  2.650e-10
   2500 0.50  1   0.0472  7.955e-05
   2500 0.50  5   0.0456  4.289e-08
  worst false-fail over grid: 7.955e-05 at (n,q,K,size)=(2500, 0.5, 1, 0.047184334032689026)

== 3. Which planted defect is visible in which cell (boundary null, normal approx)
  sigma 0.1 n 300: radius-removed size=0.50; n*100 (radius/10): Hoeff 0.007 EB 0.102; sign-flip: superiority-mode size=0 (invisible to the size test); NI-mode adopts ~always iff radius 0.073 < 2*m_NI
  sigma 0.1 n 2500: radius-removed size=0.50; n*100 (radius/10): Hoeff 0.007 EB 0.269; sign-flip: superiority-mode size=0 (invisible to the size test); NI-mode adopts ~always iff radius 0.012 < 2*m_NI
  sigma 0.3 n 300: radius-removed size=0.50; n*100 (radius/10): Hoeff 0.207 EB 0.273; sign-flip: superiority-mode size=0 (invisible to the size test); NI-mode adopts ~always iff radius 0.105 < 2*m_NI
  sigma 0.3 n 2500: radius-removed size=0.50; n*100 (radius/10): Hoeff 0.207 EB 0.350; sign-flip: superiority-mode size=0 (invisible to the size test); NI-mode adopts ~always iff radius 0.023 < 2*m_NI
  sigma 1.0 n 300: radius-removed size=0.50; n*100 (radius/10): Hoeff 0.403 EB 0.355; sign-flip: superiority-mode size=0 (invisible to the size test); NI-mode adopts ~always iff radius 0.214 < 2*m_NI
  sigma 1.0 n 2500: radius-removed size=0.50; n*100 (radius/10): Hoeff 0.403 EB 0.380; sign-flip: superiority-mode size=0 (invisible to the size test); NI-mode adopts ~always iff radius 0.061 < 2*m_NI

== 4. E1 partitions
  fit 200k + cal 100k + M5 100k = 400k; remainder 1,600,000; a second 200k fit subsample leaves 1,400,000
  CLINC 23,850 - 8,000 - 3,000 = 12,850

== 5. E3 checks
  z(m=6)=2.6383 n_TOST(.30,.02)=3,457; HW@1200=0.0228; n at sigma .40=6,146; m=3 n=3,040
  calls: 81,000 133,290 36,360; planted +0.05 power at n=3500: 1.0000
  binary EM paired diff: disagreement 20% -> sigma ~ 0.45; 10% -> 0.32

== 6. M5 checks (K=3)
  EB n: 5,025 10,175 18,136; Hoeffding radius at 470, K=3: 0.132
  T2a 6,000 powered up to sigma: 0.12; T2b 12,850: 0.23; T2c 40k: 0.47; 60k: 0.59
  77-way, misroute 1/abstain .3: if rungs disagree on 7% of rows with +-1 diffs, sigma ~ 0.26 (T2a then unpowered)

== 7. E4d, G0, E4b
  E4d P(>=3|.05)=0.0755 power@.2=0.794; G0 0.5^20=9.54e-07; E4b p=0.0068 mean=0.0292; 50/950: -0.667 vs 0.9

== 8. E4a runtime and setup sizes
  108*40000=4,320,000; x3=12,960,000; *2.5ms=9.0 CPU-h; /30=18 min
  E3 4B CPU: 103 h; milestones critical path 13.5-15.5; total 22.5-26.5
```
