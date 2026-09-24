# Augustus 0.8.0 work in progress: ExoPO and `augustus-train`

This directory holds the planning, review, research and host-provisioning record for 0.8.0. It
was kept local until 2026-09-23, when the maintainer approved publishing it. Nothing here is
runtime skill guidance. The released skill is unchanged until a 0.8.0 release.

0.8.0 carries two items:

1. **The position paper** "When the Model Is Not the Policy: Exogenous Policy Optimization for
   Agents That Act" (ExoPO). It gives a per-action-family test for where an acting agent's
   decision policy belongs, and a protocol for accepting changes to it.
2. **`augustus-train`**, a companion skill. It is a gated path from "don't train" to the cheapest
   artifact form that meets the workload's own acceptance policy.

## Status (2026-09-23 21:30 MDT)

| Item | State |
| --- | --- |
| Plan | **[v4](plan/plan-v4.md)** with [dispositions](plan/plan-v4-dispositions.md). It supersedes [v3](plan/plan-v3.md) and folds in the [errata](plan/plan-v3-errata.md), both v3 reviews, the M0 receipt and the research cards |
| v4 reviews | **Both ACCEPTED after four rounds.** [Fable 5.1 xhigh](reviews/fable-5.1-xhigh-v4.md) accepted at `6685d2a`; the [Astra-requested lane](reviews/astra-max-v4.md), which could observe no model identity and says so, accepted at `9251546`. 19 findings across the rounds, 10 of them P1, all dispositioned in [plan-v4-dispositions.md](plan/plan-v4-dispositions.md); none rejected. They accepted the **specification**, not an executed experiment, a host test or a release |
| v3 reviews | [Fable 5.1 xhigh](reviews/fable-5.1-xhigh-v3.md): NOT ACCEPTED, 0 P0, 1 P1, 10 P2. [Astra max](reviews/astra-max-v3.md): NOT ACCEPTED, 3 P1, 4 P2. All 18 findings are dispositioned in v4 |
| Host (tabputer-1) | **M0 and M0b passed.** M0: principals, containment, §4.4 GPU acceptance, B1–B15 ([receipt](receipts/m0-tabputer-1-2026-09-23.md)). M0b: the custody path, the run wrapper, and B16–B20 ([receipt](receipts/m0b-tabputer-1-2026-09-24.md)) — B19 fails, which keeps candidate GPU work on Colab as decision 18 requires. State re-verified read-only on 2026-09-24 ([receipt](receipts/m0-state-check-2026-09-24.md)). Containment code: [`infra/`](infra/) |
| Research | [CLM](sources/clm-2026-09-23.md), [Jev-Omni](sources/jev-omni-2026-09-23.md), [PAW and Rules as Programs](sources/paw-rap-2026-09-23.md) (table reproduced), the [text trainer sweep](sources/trainer-sweep-2026-09-23.md) (298 items), the [multimodal sweep](sources/trainer-sweep-multimodal-2026-09-23.md) (139 items), [trainer recipes](sources/trainer-recipes.md), [synthetic data and hill-climbing](sources/synthetic-data-and-hillclimb.md), [ExoPO prior art](sources/exopo-prior-art.md), and autoresearch tooling ([listed](sources/autoresearch-listed.md), [discovered](sources/autoresearch-discovery.md)) |
| Arithmetic | [`calc/calc_v4.py`](calc/calc_v4.py) (stdlib, deterministic) and its [output](calc/calc_v4.out.txt). [`calc_v3.py`](calc/calc_v3.py) is retained for the superseded normal-theory figures |

## Maintainer decisions after v3 (verbatim in the errata)

- **D-a.** The coordinator agent may SSH and use sudo on tabputer-1 for provisioning.
- **D-b.** Everything runs on the GPU. If tabputer-1's GPU fails, use Colab, never a CPU
  fallback.
- **D-c / D-d.** Publish the skill. Jev may be used anywhere (comparator, baseline, experiment
  arm, routing, selection, inference-time features) **except as the source of our training
  data**: no Jev-generated synthetic rows, labels, soft targets, rewards or preference pairs. No
  counsel step.
- **D-e.** PAW is a tested M5 arm. The new local single-GPU compiler keeps compilation on-box;
  hosted compilation is a fallback, with public data only.
- **Programs as rungs.** The ladder is artifact forms under one acceptance gate: exact program
  → synthesized program → compiled function (PAW) → model rungs → generalist. Composed decision
  programs let each sub-decision take its own cheapest form.

## Working on tabputer-1

tabputer-1 is the maintainer's 128 GB AMD Strix Halo host (gfx1151, ROCm 7.2.4). Access from Amp
is through the **runner `tabputer`**, which serves `/mnt/tst` as user `basit` with passwordless
sudo. Rules:

- **Never reboot.** The disk is LUKS with a console-only passphrase.
- No `pacman` upgrades.
- Never `nft flush ruleset`, and don't touch ufw, the docker or k3s tables, or `inet modyl_jit`.
- No restarts of docker, k3s, sshd, tailscaled or networking.
- Don't change modes on the maintainer's home or `/srv/ci`.
- **Experiments run only as `augexp` (48201)**, in rootless podman launched with
  `systemd-run --user` inside augexp's user manager. Enable linger for the run window and disable
  it afterwards.
- **Container profile:**
  `--network=none --read-only --tmpfs /tmp --cap-drop=all --security-opt=no-new-privileges --pids-limit=512 --memory=16g --memory-swap=16g --ipc=private`.
  Add `--device /dev/kfd --device /dev/dri/renderD128 --group-add keep-groups` for GPU runs.
- **GPU memory is not charged to the container cgroup.** Every run sets its own GPU budget
  (`torch.cuda.set_per_process_memory_fraction` or vLLM `gpu_memory_utilization`), and the host
  MemAvailable floor applies: launch at 24 GB or more, abort below 6 GB.
- **Downloads** only through `sudo augwindow open` / `close`, which drives the allowlist proxy.
  Add allowlist entries only from the proxy's refusal log, and record each edit.
- **Staged inputs** are root-owned under `/srv/aug/stage`. Confirmation labels live under
  `/srv/aug/ctl`, owned by `augctl`, which has no network.
- **Base image:** `docker.io/vllm/vllm-openai-rocm@sha256:e5e47f6aaab675c252c381f0dac237b31b10d87bb74d092b07fb4065efd7f5a1`
  (Python 3.12.13, torch 2.12, vLLM). It is already loaded for `augexp`.

## Next

**M1 in progress**, in small PRs on `main`, all merged with `make check` green:

| PR | What |
| --- | --- |
| [#109](https://github.com/24601/Augustus/pull/109) | The default branch moves to `0.8.0-dev`, and `.local/` and `.claude/` are ignored |
| [#110](https://github.com/24601/Augustus/pull/110) | Repository checks cover every skill, with per-skill budgets, one shared version and full marketplace coverage |
| [#111](https://github.com/24601/Augustus/pull/111) | The confirmation helper gains `mode`, `method` (`empirical_bernstein`, `sign_exact`) and a required `sampling_design` |
| [#112](https://github.com/24601/Augustus/pull/112) | The §3.6 provenance gate: ancestry of a training artifact, lineage-not-name identity, the TypeSafe rule, recorded hosted teachers (decision 12), and `unknown` on missing parents or an unnamed teacher |
| [#113](https://github.com/24601/Augustus/pull/113) | Sourced lineage disputes, permission records, and the one-use user acknowledgment (D-d) |
| [#114](https://github.com/24601/Augustus/pull/114) | The refusal quotes MCA §2.3(b) instead of citing it |
| [#115](https://github.com/24601/Augustus/pull/115) | The fail-closed overlap audit: duplicate ids, identical text, shared groups, and `unverifiable` when nothing can be compared |
| [#116](https://github.com/24601/Augustus/pull/116) | The climb-ledger replay and its hard gates |

**M1 and M0b are done.** 183 tests pass on `main`, and the host boundary now runs to B20.

Next is **M2**, the design locks, which must be hashed before window W2 opens. The
[E4 lock](prereg/e4-design.md) is drafted already and needs no dataset, so **M3** (E4a–c) can
start without waiting for the data window. E1, E3, M5 and M5b locks come next.

One thing the maintainer owns: tabputer-1's root filesystem reports a nonzero btrfs
`corruption_errs` counter, dated to before this work. Whether to scrub is his decision at the
console. **M0b** (B16–B20, the quarantine-and-split custody path, the MemAvailable watchdog, the
GPU-budget wrapper) gates every experiment, and no experiment runs before v4's design and
analysis locks. No tag or release without the maintainer's explicit go.
