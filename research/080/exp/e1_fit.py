#!/usr/bin/env python3
"""E1: embed, fit every arm, and report sigma-hat per contrast. Reads no confirmation label.

Runs as `augexp` on the GPU. It touches the fit, fit-B and calibration partitions, which carry
labels, and the confirmation INPUTS, which do not. The confirmation labels live with `augctl` and
this program never sees them: it writes per-arm actions, and `augctl` scores them.

What it produces is the input to the ANALYSIS LOCK: sigma-hat for each of the 19 contrasts,
measured on the calibration split, from which the required n and the powered set follow. Nothing
here reads a confirmation outcome, so the lock can be written and hashed before anything is
scored.

This program deliberately does NOT write confirmation predictions. Those come from a separate run,
AFTER the analysis lock is hashed, because one program that could produce both sigma-hat and the
predictions could also choose the lock to suit them.

Arms, from the E1 design lock:
  A            plug-in threshold C_FP/(C_FP+C_FN) on temperature-calibrated scores
  A_tuned      threshold tuned per ratio on the calibration split (descriptive only)
  B-stale      the 1:1-trained head at its own rule, which for temperature-only calibration
               with no intercept is exactly the plug-in frozen at 0.5 on the same scores
  B-retrain_r  a cost-weighted head retrained on the fit data at ratio r
  C            an MLP given the raw ratio as an input feature
  C*           a logistic head given log(C_FP/C_FN) with a free coefficient
  E            a contextual-bandit policy gradient with c as an input

Dependencies are torch and transformers only, both inside the pinned image. Logistic regression is
implemented here rather than pulled from scikit-learn, because assuming a library that may not be
in the image is how a run dies three hours in.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

# Fixed by the E1 design lock.
RATIOS = {"4:1": (4, 1), "1:1": (1, 1), "1:4": (1, 4),
          "1:9": (1, 9), "1:19": (1, 19), "1:49": (1, 49)}
TRAINING_RATIOS = ("1:1", "1:4", "1:9")
HELD_OUT_RATIOS = ("1:19", "1:49", "4:1")
SEED_FIT = 80_201
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def load_rows(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def embed(torch, transformers, texts, device, batch_size: int, budget_gib: float):
    """Mean-pooled MiniLM embeddings, L2-normalized. fp32, which M0 checked against CPU."""
    tokenizer = transformers.AutoTokenizer.from_pretrained(EMBED_MODEL)
    model = transformers.AutoModel.from_pretrained(EMBED_MODEL).to(device).eval()
    if device == "cuda" and budget_gib:
        total = torch.cuda.get_device_properties(0).total_memory / 2 ** 30
        torch.cuda.set_per_process_memory_fraction(min(1.0, budget_gib / total))
    out = []
    with torch.no_grad():
        for start in range(0, len(texts), batch_size):
            batch = texts[start:start + batch_size]
            encoded = tokenizer(batch, padding=True, truncation=True, max_length=256,
                                return_tensors="pt").to(device)
            hidden = model(**encoded).last_hidden_state
            mask = encoded["attention_mask"].unsqueeze(-1).float()
            pooled = (hidden * mask).sum(1) / mask.sum(1).clamp(min=1e-9)
            out.append(torch.nn.functional.normalize(pooled, dim=1).cpu())
    return torch.cat(out)


def fit_logistic(torch, features, labels, weights=None, *, epochs=200, lr=0.1, seed=SEED_FIT):
    """Plain logistic regression by full-batch Adam. Returns (w, b).

    `weights` gives per-example weights, which is how B-retrain_r encodes a cost ratio: a positive
    row counts C_FN and a negative row counts C_FP.
    """
    torch.manual_seed(seed)
    n, d = features.shape
    w = torch.zeros(d, 1, device=features.device, requires_grad=True)
    b = torch.zeros(1, device=features.device, requires_grad=True)
    optimizer = torch.optim.Adam([w, b], lr=lr)
    target = labels.float().view(-1, 1)
    sample_weight = None if weights is None else weights.view(-1, 1)
    for _ in range(epochs):
        optimizer.zero_grad()
        logits = features @ w + b
        loss = torch.nn.functional.binary_cross_entropy_with_logits(
            logits, target, weight=sample_weight, reduction="mean")
        loss.backward()
        optimizer.step()
    return w.detach(), b.detach()


def fit_temperature(torch, logits, labels, *, epochs=300, lr=0.05):
    """A single scalar temperature, NO INTERCEPT.

    The design lock requires this: with temperature-only scaling the 0.5 crossing does not move,
    so B-stale is exactly the plug-in frozen at 0.5 on the same scores. Platt scaling would add an
    intercept and quietly break that identity.
    """
    log_t = torch.zeros(1, device=logits.device, requires_grad=True)
    optimizer = torch.optim.Adam([log_t], lr=lr)
    target = labels.float().view(-1, 1)
    for _ in range(epochs):
        optimizer.zero_grad()
        loss = torch.nn.functional.binary_cross_entropy_with_logits(
            logits / log_t.exp(), target)
        loss.backward()
        optimizer.step()
    return log_t.detach().exp().item()


def fit_mlp(torch, features, labels, cost_feature, *, hidden=64, epochs=300, lr=0.01,
            seed=SEED_FIT):
    """Arm C: an MLP that takes the raw cost ratio as an input feature."""
    torch.manual_seed(seed + 1)
    n, d = features.shape
    model = torch.nn.Sequential(
        torch.nn.Linear(d + 1, hidden), torch.nn.ReLU(), torch.nn.Linear(hidden, 1)
    ).to(features.device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    inputs = torch.cat([features, cost_feature.view(-1, 1)], dim=1)
    target = labels.float().view(-1, 1)
    for _ in range(epochs):
        optimizer.zero_grad()
        loss = torch.nn.functional.binary_cross_entropy_with_logits(model(inputs), target)
        loss.backward()
        optimizer.step()
    return model


def fit_cost_conditioned(torch, features, labels, log_ratio, *, epochs=300, lr=0.1,
                         seed=SEED_FIT):
    """Arm C*: a logistic head given log(C_FP/C_FN) with its own free coefficient."""
    torch.manual_seed(seed + 2)
    n, d = features.shape
    w = torch.zeros(d, 1, device=features.device, requires_grad=True)
    gamma = torch.zeros(1, device=features.device, requires_grad=True)
    b = torch.zeros(1, device=features.device, requires_grad=True)
    optimizer = torch.optim.Adam([w, gamma, b], lr=lr)
    target = labels.float().view(-1, 1)
    for _ in range(epochs):
        optimizer.zero_grad()
        logits = features @ w + gamma * log_ratio.view(-1, 1) + b
        loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, target)
        loss.backward()
        optimizer.step()
    return w.detach(), gamma.detach(), b.detach()


def fit_bandit(torch, features, labels, log_ratio, costs, *, epochs=300, lr=0.05, seed=SEED_FIT):
    """Arm E: contextual-bandit policy gradient with c as an input.

    The policy picks act or abstain; the reward is the negative realized cost of that action. The
    gradient is the usual score-function estimator, taken over the policy's own samples.
    """
    torch.manual_seed(seed + 3)
    n, d = features.shape
    w = torch.zeros(d, 1, device=features.device, requires_grad=True)
    gamma = torch.zeros(1, device=features.device, requires_grad=True)
    b = torch.zeros(1, device=features.device, requires_grad=True)
    optimizer = torch.optim.Adam([w, gamma, b], lr=lr)
    c_fp, c_fn = costs
    for _ in range(epochs):
        optimizer.zero_grad()
        logits = features @ w + gamma * log_ratio.view(-1, 1) + b
        probability = torch.sigmoid(logits).clamp(1e-6, 1 - 1e-6)
        action = torch.bernoulli(probability)
        cost = torch.where((action > 0) & (labels.view(-1, 1) == 0), c_fp,
                           torch.where((action == 0) & (labels.view(-1, 1) == 1), c_fn,
                                       torch.zeros_like(probability)))
        log_probability = action * probability.log() + (1 - action) * (1 - probability).log()
        # Reward is the negative cost, so the policy climbs away from expensive actions.
        loss = ((cost - cost.mean()) * log_probability).mean()
        loss.backward()
        optimizer.step()
    return w.detach(), gamma.detach(), b.detach()


def per_case_cost(actions, labels, c_fp: float, c_fn: float):
    """Cost of each decision. Same definition the scorer uses, kept in one shape."""
    false_positive = (actions > 0) & (labels == 0)
    false_negative = (actions == 0) & (labels == 1)
    return false_positive.float() * c_fp + false_negative.float() * c_fn


def contrast_sigma(costs_left, costs_right) -> dict:
    """sigma-hat of the paired difference, which is what the analysis lock records."""
    differences = costs_left - costs_right
    n = differences.numel()
    mean = differences.mean().item()
    sd = differences.std(unbiased=True).item() if n > 1 else 0.0
    return {"n": n, "mean": mean, "sd": sd}


def build_arms(torch, calibrated_scores, features, labels, fitted, ratio: str) -> dict:
    """Every arm's ACTION on one split at one cost ratio."""
    fp, fn = RATIOS[ratio]
    c_fp, c_fn = fp / (fp + fn), fn / (fp + fn)
    threshold = c_fp  # the plug-in threshold C_FP/(C_FP+C_FN)
    log_ratio = torch.full((features.shape[0],), math.log(c_fp / c_fn), device=features.device)

    actions = {}
    actions["A"] = (calibrated_scores >= threshold).long()
    # B-stale is the 1:1 head at its own rule. With temperature-only calibration the 0.5 crossing
    # is unmoved, so this is the plug-in frozen at 0.5 on the same scores.
    actions["B-stale"] = (calibrated_scores >= 0.5).long()
    # A_tuned: the threshold that minimizes cost on THIS split. Descriptive only, by the lock.
    grid = torch.linspace(0.01, 0.99, 99, device=features.device)
    best, best_cost = threshold, None
    for candidate in grid.tolist():
        cost = per_case_cost((calibrated_scores >= candidate).long(), labels, c_fp, c_fn).mean()
        if best_cost is None or cost < best_cost:
            best, best_cost = candidate, cost
    actions["A_tuned"] = (calibrated_scores >= best).long()

    w, b = fitted["b_retrain"][ratio]
    actions[f"B-retrain_{ratio}"] = ((features @ w + b).squeeze(1) >= 0).long()

    model = fitted["c_mlp"]
    raw_ratio = torch.full((features.shape[0], 1), c_fn / c_fp, device=features.device)
    actions["C"] = (model(torch.cat([features, raw_ratio], dim=1)).squeeze(1) >= 0).long()

    w_c, gamma_c, b_c = fitted["c_star"]
    actions["C*"] = ((features @ w_c + gamma_c * log_ratio.view(-1, 1) + b_c
                      ).squeeze(1) >= 0).long()

    w_e, gamma_e, b_e = fitted["e_bandit"][ratio]
    actions["E"] = ((features @ w_e + gamma_e * log_ratio.view(-1, 1) + b_e
                     ).squeeze(1) >= 0).long()
    return actions, (c_fp, c_fn), best


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--stage", type=Path, default=Path("/srv/aug/stage/parts"))
    parser.add_argument("--corpus", default="civil")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--gpu-budget-gib", type=float, default=2.0)
    parser.add_argument("--limit", type=int, help="cap rows per partition, for a smoke run")
    args = parser.parse_args(argv)

    import torch
    import transformers

    device = "cuda" if torch.cuda.is_available() else "cpu"
    started = time.time()

    def read(name):
        rows = load_rows(args.stage / f"{args.corpus}-{name}" / "rows.json")
        return rows[:args.limit] if args.limit else rows

    fit_rows = read("fit")
    calibration_rows = read("calibration")
    report = {"corpus": args.corpus, "device": device,
              "rows": {"fit": len(fit_rows), "calibration": len(calibration_rows)}}

    fit_x = embed(torch, transformers, [r["text"] for r in fit_rows], device,
                  args.batch_size, args.gpu_budget_gib).to(device)
    fit_y = torch.tensor([int(r["label"]) for r in fit_rows], device=device)
    cal_x = embed(torch, transformers, [r["text"] for r in calibration_rows], device,
                  args.batch_size, args.gpu_budget_gib).to(device)
    cal_y = torch.tensor([int(r["label"]) for r in calibration_rows], device=device)
    report["embed_seconds"] = round(time.time() - started, 1)

    # The base head, fit at 1:1, is what A and B-stale both read.
    w, b = fit_logistic(torch, fit_x, fit_y)
    temperature = fit_temperature(torch, (fit_x @ w + b), fit_y)
    report["temperature"] = temperature
    report["temperature_note"] = "scalar, no intercept, so the 0.5 crossing is unmoved"

    fitted = {"b_retrain": {}, "e_bandit": {}}
    for ratio in RATIOS:
        fp, fn = RATIOS[ratio]
        c_fp, c_fn = fp / (fp + fn), fn / (fp + fn)
        weights = torch.where(fit_y == 1, c_fn, c_fp).float()
        fitted["b_retrain"][ratio] = fit_logistic(torch, fit_x, fit_y, weights)
        log_ratio = torch.full((fit_x.shape[0],), math.log(c_fp / c_fn), device=device)
        fitted["e_bandit"][ratio] = fit_bandit(torch, fit_x, fit_y, log_ratio, (c_fp, c_fn))
    mixed_ratio = torch.tensor(
        [RATIOS[TRAINING_RATIOS[i % len(TRAINING_RATIOS)]][1]
         / RATIOS[TRAINING_RATIOS[i % len(TRAINING_RATIOS)]][0]
         for i in range(fit_x.shape[0])], device=device, dtype=torch.float)
    fitted["c_mlp"] = fit_mlp(torch, fit_x, fit_y, mixed_ratio)
    fitted["c_star"] = fit_cost_conditioned(
        torch, fit_x, fit_y, torch.log(1.0 / mixed_ratio))

    cal_scores = torch.sigmoid((cal_x @ w + b).squeeze(1) / temperature)

    sigmas = []
    for ratio in RATIOS:
        actions, (c_fp, c_fn), tuned = build_arms(
            torch, cal_scores, cal_x, cal_y, fitted, ratio)
        costs = {name: per_case_cost(action, cal_y, c_fp, c_fn)
                 for name, action in actions.items()}
        mean_cost_a = costs["A"].mean().item()
        margin = 0.02 * mean_cost_a
        for left, right in (("A", "B-stale"), ("A", f"B-retrain_{ratio}"),
                            ("C", "A"), ("C*", "A"), ("E", "A")):
            stats = contrast_sigma(costs[left], costs[right])
            sigmas.append({
                "ratio": ratio, "contrast": f"{left} - {right}",
                "held_out": ratio in HELD_OUT_RATIOS,
                "margin": margin, "span": 2 * max(c_fp, c_fn),
                "cost_A": mean_cost_a, "tuned_threshold": tuned, **stats,
            })
    report["cost_of_A_by_ratio"] = {s["ratio"]: s["cost_A"] for s in sigmas}
    report["contrasts"] = sigmas
    report["wall_clock_s"] = round(time.time() - started, 1)
    report["reads_no_confirmation_label"] = True
    report["limits"] = [
        "sigma-hat is measured on the calibration split, before any confirmation row is read.",
        "A_tuned is descriptive only; the design lock excludes it from the family.",
        "No confirmation outcome is read here; augctl scores the predictions separately.",
    ]

    args.out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "contrasts"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
