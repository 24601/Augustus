# tabputer-1 state check, 2026-09-24 (read-only)

Operator: an Amp thread on the runner `tabputer` (`/mnt/tst`, user `basit`), mode `gpt6a-low`,
thread `T-01a0d1d1-4ac2-70d3-8a27-d70036798322`. **Nothing was changed.** Ten read-only commands
ran; no container started, no window opened, no linger enabled, no principal impersonated, no
nftables modification. Firewall rule bodies and addresses are deliberately not reproduced here.

Purpose: confirm that the M0 containment state plan v4 §4.2 describes is still the state of the
host, before M0b adds the custody path, the watchdog and B16–B20.

| Check | Result | Plan v4 says |
| --- | --- | --- |
| Principal uids | `augexp` 48201 (groups render, video), `augctl` 48202, `augproxy` 947 | §4.2 table: matches, including the M0 deviation from 1001/1002 |
| `/srv/aug` layout | `admin` and `ctl` 0700 (ctl owned by `augctl`), `inbox` and `stage` root-owned 0750 group `augexp`, `pred` owned by `augexp` with an ACL, `runs` 0700 `augexp`, `receipts` 0750 `augctl` | §4.2: matches |
| Containment units | `augexp-nft.service` enabled **and active**; `augipc-acl.service` active; `augexp-alarm.service` inactive (it is the dead-man timer, armed only during a window) | §4.2: matches |
| Download window | `augproxy.service` **inactive**, so the window is **closed** | §4.2: W1 was closed after M0, as required before any run |
| `inet augexp` table | Loaded, with the expected output, setup-window and per-principal chains and their named drop/accept counters. Contents not reproduced | §4.2: matches |
| Linger | `loginctl` reports neither principal is logged in or lingering | §4.2: linger is enabled only for a window and disabled afterwards |
| Memory | MemAvailable 119,653,848 kB ≈ **114.1 GiB** of 131,007,996 kB; swap 131,007,484 kB ≈ 124.9 GiB, 128,277,608 kB free | §4.5: far above the 24 GiB floor, and the zram swap that made `--memory-swap=16g` necessary is still present |
| GPU devices | `/dev/kfd` and `/dev/dri/renderD128` are **0666**, group `render` | §4.6 non-claim: `render` membership is not a control |
| Host | kernel `7.2.0-1-cachyos`, CachyOS; podman 6.1.0 | §4.4: unchanged since the M0 receipt |
| `/srv/aug/stage` | Contains `images` and `models` only — no dataset partitions | §4.2: W2 has not run, and no experiment data is on the host |
| `/srv/aug/quarantine` | **Does not exist** | Expected: it is M0b work, not yet built |
| `/srv/aug/receipts` | One entry, `accept-20260923T193032`, the §4.4 GPU acceptance receipt | M0 receipt: matches |

## Reading

The host is exactly where M0 left it, and nothing in plan v4's §4.2 description of the installed
state is stale. Two gaps are open work rather than drift:

1. `/srv/aug/quarantine` and the two-root data/weights split (§4.2, Fable v4 P1-B) do not exist
   yet. They are M0b.
2. `/srv/aug/stage` holds only the base image and the §4.4 acceptance weights. No experiment
   dataset is on the host, which is what the W2-after-M2 ordering requires.

No experiment ran, and none may run until v4's design and analysis locks and M0b's B16–B20.
