#!/usr/bin/env python3
"""Plan v3 §4.4 GPU acceptance for Augustus 0.8.0 on tabputer-1.

Runs inside the pinned ROCm container with no network. It checks four things:
1. matmul, softmax and SDPA in bf16 on the GPU against a CPU fp32 reference;
2. MiniLM-L6 fp32 embeddings, GPU vs CPU, on 1,000 synthetic texts (min cosine >= 0.9999);
3. Qwen3-1.7B bf16 greedy decoding: two GPU runs over 50 prompts must agree on >= 98% of
   prompts, and GPU-vs-CPU agreement is reported on 20 prompts;
4. a soak of sustained GPU matmul for --soak-min minutes. The host wrapper checks the kernel log
   for amdgpu resets.

Texts and prompts are generated here, so no experiment dataset is touched before the design lock.
Output: one JSON receipt at --out.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import random
import sys
import time

import torch
import torch.nn.functional as F

TOL = {"matmul_rel": 1e-2, "softmax_abs": 1e-2, "sdpa_rel": 2e-2, "fp32_rel": 1e-5,
       "minilm_cos": 0.9999, "qwen_rerun": 0.98}


def rel(a, b):
    return float((a - b).norm() / b.norm())


def kernels(dev):
    g = torch.Generator().manual_seed(1234)
    out = {}
    a = torch.randn(2048, 2048, generator=g)
    b = torch.randn(2048, 2048, generator=g)
    ref = a @ b
    out["matmul_bf16_rel"] = rel((a.to(dev, torch.bfloat16) @ b.to(dev, torch.bfloat16)).float().cpu(), ref)
    torch.backends.cuda.matmul.allow_tf32 = False
    out["matmul_fp32_rel"] = rel((a.to(dev) @ b.to(dev)).cpu(), ref)
    x = torch.randn(64, 4096, generator=g) * 3
    out["softmax_bf16_abs"] = float((x.to(dev, torch.bfloat16).softmax(-1).float().cpu() - x.softmax(-1)).abs().max())
    q, k, v = (torch.randn(2, 8, 512, 64, generator=g) for _ in range(3))
    ref = F.scaled_dot_product_attention(q, k, v, is_causal=True)
    got = F.scaled_dot_product_attention(*(t.to(dev, torch.bfloat16) for t in (q, k, v)), is_causal=True)
    out["sdpa_bf16_rel"] = rel(got.float().cpu(), ref)
    out["pass"] = (out["matmul_bf16_rel"] <= TOL["matmul_rel"] and out["matmul_fp32_rel"] <= TOL["fp32_rel"]
                   and out["softmax_bf16_abs"] <= TOL["softmax_abs"] and out["sdpa_bf16_rel"] <= TOL["sdpa_rel"])
    return out


WORDS = ("model policy agent threshold cost label audit route defer queue budget review "
         "invoice refund outage ticket urgent billing latency cache deploy rollback error "
         "customer warehouse shipment delay forecast margin variance sample holdout").split()


def synthetic_texts(n, seed=7):
    r = random.Random(seed)
    return [" ".join(r.choice(WORDS) for _ in range(r.randint(6, 40))).capitalize() + "." for _ in range(n)]


def minilm(path, dev):
    from transformers import AutoModel, AutoTokenizer
    tok = AutoTokenizer.from_pretrained(path)
    texts = synthetic_texts(1000)

    def embed(device):
        m = AutoModel.from_pretrained(path, dtype=torch.float32).to(device).eval()
        outs = []
        with torch.inference_mode():
            for i in range(0, len(texts), 100):
                enc = tok(texts[i:i + 100], padding=True, truncation=True, max_length=128, return_tensors="pt").to(device)
                h = m(**enc).last_hidden_state
                mask = enc["attention_mask"].unsqueeze(-1).float()
                e = (h * mask).sum(1) / mask.sum(1)
                outs.append(F.normalize(e, dim=-1).cpu())
        return torch.cat(outs)

    t0 = time.time(); gpu = embed(dev); t_gpu = time.time() - t0
    t0 = time.time(); cpu = embed("cpu"); t_cpu = time.time() - t0
    cos = (gpu * cpu).sum(-1)
    return {"n": len(texts), "min_cos": float(cos.min()), "mean_cos": float(cos.mean()),
            "gpu_s": round(t_gpu, 2), "cpu_s": round(t_cpu, 2), "pass": float(cos.min()) >= TOL["minilm_cos"]}


def prompts(n, seed=11):
    r = random.Random(seed)
    stems = ["Explain in one paragraph why", "List three risks when", "Write a short note about how",
             "Summarize the trade-off when", "Give a numbered checklist for when"]
    return [f"{r.choice(stems)} a team must {r.choice(WORDS)} a {r.choice(WORDS)} under a {r.choice(WORDS)} limit."
            for _ in range(n)]


def qwen(path, dev, n_gpu=50, n_cpu=20, new_tokens=64):
    from transformers import AutoModelForCausalLM, AutoTokenizer
    tok = AutoTokenizer.from_pretrained(path)
    ps = prompts(n_gpu)

    def run(model, device, items):
        outs = []
        with torch.inference_mode():
            for p in items:
                msgs = [{"role": "user", "content": p}]
                ids = tok.apply_chat_template(msgs, add_generation_prompt=True, enable_thinking=False,
                                              return_tensors="pt", return_dict=True).to(device)
                g = model.generate(**ids, max_new_tokens=new_tokens, do_sample=False, temperature=None,
                                   top_p=None, top_k=None)
                outs.append(g[0, ids["input_ids"].shape[1]:].tolist())
        return outs

    m = AutoModelForCausalLM.from_pretrained(path, dtype=torch.bfloat16).to(dev).eval()
    t0 = time.time(); a = run(m, dev, ps); t1 = time.time(); b = run(m, dev, ps); t2 = time.time()
    rerun = sum(x == y for x, y in zip(a, b)) / len(ps)
    del m
    torch.cuda.empty_cache()
    mc = AutoModelForCausalLM.from_pretrained(path, dtype=torch.float32).eval()
    c = run(mc, "cpu", ps[:n_cpu])
    agree = sum(x == y for x, y in zip(a[:n_cpu], c)) / n_cpu
    first_div = [next((i for i, (u, w) in enumerate(zip(x, y)) if u != w), min(len(x), len(y)))
                 for x, y in zip(a[:n_cpu], c)]
    toks = sum(len(x) for x in a)
    return {"n_gpu": len(ps), "rerun_identical": rerun, "n_cpu": n_cpu, "gpu_cpu_identical": agree,
            "gpu_cpu_first_divergence_median": sorted(first_div)[len(first_div) // 2],
            "gpu_tok_per_s": round(toks / (t1 - t0), 1), "pass": rerun >= TOL["qwen_rerun"]}


def soak(dev, minutes):
    a = torch.randn(4096, 4096, device=dev, dtype=torch.bfloat16)
    b = torch.randn(4096, 4096, device=dev, dtype=torch.bfloat16)
    end = time.time() + 60 * minutes
    iters, t0 = 0, time.time()
    while time.time() < end:
        for _ in range(50):
            c = a @ b
        torch.cuda.synchronize()
        iters += 50
        if not torch.isfinite(c).all():
            return {"minutes": minutes, "iters": iters, "pass": False, "why": "non-finite"}
    dt = time.time() - t0
    return {"minutes": minutes, "iters": iters, "tflops_bf16": round(iters * 2 * 4096 ** 3 / dt / 1e12, 2),
            "pass": True}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--minilm", required=True)
    ap.add_argument("--qwen", required=True)
    ap.add_argument("--soak-min", type=float, default=30)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    torch.set_num_threads(max(1, os.cpu_count() or 1))
    r = {"started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "python": platform.python_version(), "torch": torch.__version__, "hip": torch.version.hip,
         "cuda_available": torch.cuda.is_available(), "tolerances": TOL}
    if not torch.cuda.is_available():
        r["pass"] = False
        r["why"] = "no GPU visible"
    else:
        dev = "cuda"
        p = torch.cuda.get_device_properties(0)
        r["device"] = {"name": p.name, "arch": getattr(p, "gcnArchName", ""), "total_mem_gb": round(p.total_memory / 2**30, 1),
                       "arch_list": torch.cuda.get_arch_list()}
        for name, fn in (("kernels", lambda: kernels(dev)), ("minilm", lambda: minilm(args.minilm, dev)),
                         ("qwen3_1_7b", lambda: qwen(args.qwen, dev)), ("soak", lambda: soak(dev, args.soak_min))):
            t0 = time.time()
            try:
                r[name] = fn()
            except Exception as exc:  # recorded, never hidden
                r[name] = {"pass": False, "error": f"{type(exc).__name__}: {exc}"[:2000]}
            r[name]["wall_s"] = round(time.time() - t0, 1)
            print(name, json.dumps(r[name]), flush=True)
        r["pass"] = all(r[k].get("pass") for k in ("kernels", "minilm", "qwen3_1_7b", "soak"))
    r["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(args.out, "w") as f:
        json.dump(r, f, indent=1)
    print("PASS" if r["pass"] else "FAIL", flush=True)
    return 0 if r["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
