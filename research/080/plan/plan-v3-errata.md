# Plan v3 errata and maintainer decisions (2026-09-23, after v3 was written)

Confidential, local only. These override plan v3 wherever they conflict. Plan v4 will fold them
in. Both in-flight reviews (Fable v3 and Astra v3) were started on v3 as written.

## Maintainer decisions (verbatim instructions, 2026-09-23 MDT evening)

| # | Instruction | Effect on v3 |
|---|---|---|
| D-a | "you can set up those users, ssh in, it has passwordless sudo" | Decision 21 is answered, and the coordinator agent (Opus 5.5, `claude-opus-5-5[1m]`) is **granted SSH and sudo on tabputer-1 for provisioning**. §4.1's "This lane does not SSH" and decision 21's "No agent gets sudo or SSH" are superseded for the coordinator only. Experiment principals still get no sudo. Every root command is logged in the provisioning receipt. |
| D-b | "everything has to run on GPU, that's idiotic, otherwise lets use colab" | **GPU for everything**, including candidate and hill-climb code. The CPU fallback in §4.4 and decision 23 is removed. If §4.4 GPU acceptance fails on tabputer-1, the fallback is **Colab** (earlier: "let me know if you need me to subscribe to colab pro+"), not CPU. The platform is fixed per experiment at its analysis lock; there is no silent switch mid-study. Colab runs carry no B1–B14 claim. Code and public data would go to Google, and the maintainer accepted that by choosing Colab as the fallback. |
| D-c | "basicaly, we can publish the skill, but lets not use jev to be safe in labeling of the data. if users of the skill want to, that is fine." | Decision 11 is answered for release. **Publishing `augustus-train` is the maintainer's accepted risk** (counsel question 1), so M9 no longer waits on counsel. **Our own experiments never put Jev in a labeling path** (labels, soft targets, filtering, selection). §3.6 changes for skill users: TypeSafe/Jev nodes become `restricted`, not `barred`. They are refused by default. The skill quotes MCA §2.3(b) and says it binds anyone who has accepted TypeSafe's terms. Only an explicit, recorded acknowledgment by the skill's user (artifact, use and date) clears one use. The skill never recommends Jev distillation. Still open: Jev as an evaluation comparator in our paper and site (counsel question 2). Default is excluded until the maintainer says otherwise. |
| D-d | "dude, stop worrying about counsel sutff, use jev, but just don't directly generate synthetic from it directly, otherwise, stop worrying and use it" | **Supersedes D-c's labeling rule and every counsel item.** Decision 11 (counsel) and decision 12 (website automation) are closed; there is no counsel step and no accept-risk gate. **Jev may be used**: as an evaluation comparator and baseline in the paper and site, as an arm in E1/E3, for routing, selection and filtering, and as inference-time features. **The one exclusion is that Jev output never becomes our training data**: no Jev-generated synthetic rows, labels, soft targets, rewards or preference pairs in our experiments or in any corpus we ship. In the skill, a Jev-generated training corpus is refused by default with one quoted line of MCA §2.3(b), and the user can override it; there is no other ceremony. Jev calls from tabputer-1 need a named egress path and a key the maintainer supplies. The setup proxy keeps denying typesafe.ai, because setup never needs it. |
| D-e | (asked whether PAW is tested or documented only) "yeah, and we hsould alslolook at he new stuff from paw's authok ruels as programs? if its worthy" | **PAW is a tested M5 arm.** Its hosted compile is allowed: `programasweights.com` hosts are added to the setup allowlist from the refusal log during a window. Only public-dataset specs and examples leave the box, never Jev-generated ones. Inference runs locally and offline in the container. The PAW author's newer rules-as-programs work gets a primary-source inspection and a worthiness verdict before it enters v4. **Done (worthy):** `research/paw-rap-2026-09-23.md`. A new MIT local single-GPU compiler (2026-09-22) makes PAW-standard compile on-box, and PAW-ft can run with a local teacher. Hosted compile is now only a fallback. RAP is required prior art for the ExoPO paper: exogenous rule checks as detection, not gating. |

## Coordinator facts observed after v3

- **Memory.** The ~106 GB was a `vllm serve` process inside the `vllm-strix` docker container
  (GTT owner pid 2184341), not k3s. It was stopped at the maintainer's instruction. At 18:38 MDT,
  MemAvailable was 121,366,040 kB (about 115.7 GiB) of 131,007,996 kB. The container is still up,
  with its server stopped. The "about 16 GB free today" in v3's provenance, §4.5 and decision 22 is
  stale. The envelope rules (16 GB cap, launch floor 24 GB, abort below 6 GB) stand.
- **GPU is reachable in a container today.** `vllm/vllm-openai-rocm:v0.29.0` (image
  `sha256:e5e47f6aaab675c252c381f0dac237b31b10d87bb74d092b07fb4065efd7f5a1`) reports
  torch `2.12.0+git6bbd260`, HIP `7.2.53211`, `cuda.is_available() = True`, with `gfx1151` in the
  arch list. Host ROCm is 7.2.4 on kernel 7.2.0-1-cachyos. §4.4 acceptance has **not** been run.
  Candidate answer to decision 23: this image, `docker save`d into root-owned stage and
  `podman load`ed as `augexp`, so no registry hosts are needed. Its Python version differs from
  the plan's CPython 3.12 and must be recorded.
- **GPU device modes.** `/dev/kfd` and `/dev/dri/renderD128` are mode 0666. Every local user can
  already open the GPU, so `render` group membership in §4.2 and §4.6 is not a control. Noted, not
  changed. Candidate containers get the GPU under D-b anyway.
- **Host network facts.**
  - ufw is active.
  - `nftables.service` is disabled. Its stock config flushes the ruleset, so it must not be used.
  - Existing nft tables: ip/ip6 filter, nat, raw and mangle, plus `inet modyl_jit`.
  - Loopback listeners include k3s (6443, 6444, 10248–10259), containerd, docker-proxy (5001,
    8000), a python3 on 5000, opencode, bpftune and resolved 127.0.0.53:53. Tailscale is
    <tailnet-ip> (100.64.0.0/10).
  - Port 3128 is free.
- **Fable v3 review** (`reviews/fable-5.1-xhigh-v3.md`): NOT ACCEPTED, 0 P0, 1 P1, 10 P2. P1-1: the
  design lock must precede any download, but M0 downloads data before the M2 lock. **M0 reading
  adopted now:** M0 downloads only infrastructure, meaning the base image (a local transfer, no
  download) and the §4.4 acceptance weights (MiniLM, Qwen3-1.7B). Experiment datasets
  (CivilComments, BANKING77, CLINC150) wait for the M2 design lock.

## Provisioning findings (2026-09-23, pre-load review by Fable 5.1 xhigh)

Review record: workflow `wf_d2b8c10c-93c` found 0 P0, 3 P1 and 7 P2. All ten are fixed, and a
delta re-review is pending. The reviewer confirmed the nft semantics: nothing can touch uid 0,
forwarded traffic, or the ufw and iptables-nft tables.

- **uid collision (P1-3, confirmed on the host).** Host uid 1001 is already used by processes
  inside the fleet-pr GitHub runner containers (`Runner.Listener`, `run.sh`; bridge networking, no
  userns remap). Sharing it would let `augexp` read those processes' `/proc/<pid>/environ`.
  Yama `ptrace_scope` = 1 restricts only attach. `augexp` and `augctl` were recreated as
  **48201** and **48202**; `augproxy` stays 947. The six uid-1001 container pids were unchanged
  before and after. Only rootless podman storage and first-party smoke-test output had existed
  under the old uid. **New boundary test B15:** no process or socket with a principal uid
  exists outside that principal's own slice or unit. The installer enforces this, and every run
  preflight must repeat it.
- **Local IPC bypass of the skuid filter (P1-1).** systemd-resolved (varlink and D-Bus), the
  tailscaled LocalAPI and the AF_UNIX sshd socket are mode 0666, so a root or system daemon could
  resolve or send on the principal's behalf. The fix has two parts: named-user ACL `---` on those
  sockets, re-applied by drop-ins when they are recreated, and a D-Bus user policy denying
  resolve1, network1, NetworkManager, import1, machine1 and portable1. With nsswitch set to
  `resolve [!UNAVAIL=return] ... dns`, lookups fall through to UDP 127.0.0.53, which the table
  drops. B9 and B10 must now also check `getent hosts`, `resolvectl query`, `busctl` resolve1
  and a tailscaled LocalAPI request, each as `augexp` and as `augctl`.
- **Shared-CDN reach through an allowlisted CONNECT (P1-2).** The proxy now requires a TLS
  ClientHello whose SNI equals the CONNECT host before it connects anywhere. Tunnel contents after
  the ClientHello are not inspected, so **§4.6 gains a non-claim**: domain fronting through a CDN
  that permits a Host header differing from SNI is not prevented.
- **Base image.** `vllm/vllm-openai-rocm:v0.29.0` (manifest `sha256:e5e47f6a…`) runs Python
  3.12.13, torch 2.12.0 (ROCm 7.2) and transformers 5.16.1. It was `docker save`d to
  `/srv/aug/stage/images/` (tar sha256 `ef2efb98…`) and `podman load`ed by `augexp`. A rootless
  hardened smoke test (`--network=none --read-only --cap-drop=all`, no-new-privileges, pids and
  memory limits, kfd and renderD128 passed) saw gfx1151 with 124 GiB and measured 22.4 bf16
  TFLOPS cold. Outbound connect was refused.

## M0 result (2026-09-23 20:53 MDT)

M0 passed: provisioning, containment, §4.4 GPU acceptance, and B1–B15. Full record:
`receipts/m0-tabputer-1-2026-09-23.md` (the raw root-command log stays local to the maintainer).
Deviations that v4 must fold in:
- uids are 48201 and 48202;
- the container profile needs `--memory-swap=16g` (125 GB zram);
- runs launch with `systemd-run --user`;
- **GPU memory is not charged to the container cgroup**, so every run needs a GPU-side budget
  plus a real MemAvailable watchdog;
- vLLM batching gives about 2,000 tok/s but only 60% batched-rerun identity;
- local IPC and other workloads' trees are part of the boundary (`augipc-acl`, D-Bus policy,
  `augfs-deny`);
- the proxy binds SNI to the CONNECT host.

## v4 scope addition: programs as rungs (maintainer question, 2026-09-23 21:00 MDT)

The maintainer asked whether PAW, rules-as-programs and their permutations that call classifiers
are kept in the trainer and the skill. Status: the released skill has them. Exact rules and policy
code are covered in the optimizer integration pattern and mixed-architecture. ProgramAsWeights
appears as a Hypothesis materialization loop in `optimizer-integration.md`. Plan v3 does not:
G0 has "an exact rule decides", T1 uses code-computed labels, and the ladder R0–R5 is models only.
v4 adds:
- **Artifact forms under one acceptance gate.** Exact program → synthesized program (an
  agent-written, deterministic, frozen artifact) → compiled local function (PAW) → R1–R4 model
  rungs → generalist.
- **Composed decision programs.** Code decomposes the decision, and each sub-decision takes its
  own cheapest adequate form: rule, head, PAW function, or a Jev call at inference, which D-d
  permits. Acceptance is end-to-end plus per stage. Sub-call latency and cost count. AND is
  never a product of marginals: ask the compound question, or aggregate batched Nouls in code.
  Program structure is a climb, so it goes through the climb ledger and frozen confirmation.
- **Traps to test.** A synthesized program scored on code-computed labels from its own family is
  circular, so T1 stays fixture-only. Real-text tasks T2a–c are the honest arms, and fuzzy text
  is where programs are expected to lose.
- **PAW fact (checked 2026-09-23).** The SDK is MIT (`programasweights/programasweights-python`,
  pushed 2026-09-22). Compilation runs on their hosted compiler (`paw-4b-*`, program IDs on
  their Hub); inference is local and offline-capable. An M5 PAW arm therefore needs
  `programasweights.com` allowlisted, and it sends spec plus examples off-box. That requires
  public data only, never Jev-generated examples, and a maintainer decision.

## Hard rules for work on tabputer-1

No reboot, since LUKS needs the passphrase at the console. No `pacman` install or upgrade. No
`nft flush ruleset`, and no edits to the ip/ip6 tables, `inet modyl_jit` or ufw. No restart of
docker, k3s, sshd or networking. No mode changes to `/home/basit` or `/srv/ci`. The plan, the
reviews and the research notes never go to tabputer-1; only run bundles do.
