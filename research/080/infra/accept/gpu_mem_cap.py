"""Does GPU (GTT) memory count against the container's 16 GiB memory cgroup on this UMA APU?

Allocates 1 GiB bf16 CUDA tensors, touching each, up to --max-gib. Prints the cgroup's
memory.current after each step so the receipt shows whether GPU pages are charged. Exits 0 if
the allocation stopped at or below the cap (OOM or CUDA OOM), 3 if it exceeded the cap.
"""
import argparse
import sys

import torch

ap = argparse.ArgumentParser()
ap.add_argument("--max-gib", type=int, default=24)
ap.add_argument("--cap-gib", type=int, default=16)
args = ap.parse_args()


def cg(name):
    try:
        return open(f"/sys/fs/cgroup/{name}").read().strip()
    except OSError:
        return "n/a"


print("memory.max", cg("memory.max"), "swap.max", cg("memory.swap.max"), flush=True)
held = []
try:
    for i in range(args.max_gib):
        t = torch.ones((1 << 29,), dtype=torch.bfloat16, device="cuda")  # 1 GiB, written
        torch.cuda.synchronize()
        held.append(t)
        cur = int(cg("memory.current")) if cg("memory.current").isdigit() else -1
        print(f"GiB {i + 1} cgroup_current_GiB {cur / 2**30:.2f}", flush=True)
except torch.cuda.OutOfMemoryError as exc:
    print("CUDA OOM at", len(held), str(exc)[:120], flush=True)
print("HELD", len(held), flush=True)
sys.exit(3 if len(held) > args.cap_gib else 0)
