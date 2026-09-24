"""Batched vLLM smoke for plan §4.5: Qwen3-1.7B, offline, no network, explicit GPU budget.

Generates 64 greedy tokens for --n synthetic chat prompts in one batch and reports decode
throughput. A second identical pass checks batched determinism. GPU memory is bounded by
--gpu-util (a fraction of the device's 124 GiB), because the container memory cgroup may not
charge GTT pages.
"""
import argparse
import json
import random
import time

from vllm import LLM, SamplingParams

ap = argparse.ArgumentParser()
ap.add_argument("--model", required=True)
ap.add_argument("--n", type=int, default=256)
ap.add_argument("--gpu-util", type=float, default=0.10)
ap.add_argument("--eager", action="store_true")
ap.add_argument("--out", required=True)
args = ap.parse_args()

WORDS = "model policy agent threshold cost label audit route defer queue budget review invoice refund outage".split()
r = random.Random(3)
prompts = [[{"role": "user", "content": f"In two sentences, explain how a team should {r.choice(WORDS)} a "
             f"{r.choice(WORDS)} under a {r.choice(WORDS)} limit."}] for _ in range(args.n)]

t0 = time.time()
llm = LLM(model=args.model, dtype="bfloat16", gpu_memory_utilization=args.gpu_util, max_model_len=2048,
          enforce_eager=args.eager, seed=0)
load_s = time.time() - t0
sp = SamplingParams(temperature=0.0, max_tokens=64, ignore_eos=True)
res = {}
outs = []
for k in range(2):
    t = time.time()
    o = llm.chat(prompts, sp, chat_template_kwargs={"enable_thinking": False}, use_tqdm=False)
    dt = time.time() - t
    toks = sum(len(x.outputs[0].token_ids) for x in o)
    outs.append([tuple(x.outputs[0].token_ids) for x in o])
    res[f"pass{k + 1}"] = {"seconds": round(dt, 2), "output_tokens": toks, "tok_per_s": round(toks / dt, 1)}
res.update({"n": args.n, "gpu_util": args.gpu_util, "eager": args.eager, "load_s": round(load_s, 1),
            "batch_rerun_identical": sum(a == b for a, b in zip(*outs)) / args.n})
print(json.dumps(res), flush=True)
json.dump(res, open(args.out, "w"), indent=1)
