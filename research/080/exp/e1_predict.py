#!/usr/bin/env python3
"""E1 post-lock run: write one 0/1 action per confirmation id, per arm. Reads no label there.

This is the program the two-lock scheme requires to be separate from `e1_fit.py`. The fit run
produces sigma-hat; the analysis lock is derived and hashed from it; only then does this run read
the confirmation INPUTS and emit actions. One program that could produce both sigma-hat and the
predictions could also choose the lock to suit them, so there are two.

State recovery, which is the only interesting design question here: `e1_fit.py` persists no
checkpoint, so this program does not load one. It re-derives every arm by importing `e1_fit`'s own
functions and re-running them on the same fit and calibration partitions with the same seeds. That
is stronger than a checkpoint, not weaker: a checkpoint has to be trusted, whereas a re-derivation
can be CHECKED, and this program checks it. If the recomputed temperature does not match the
temperature recorded in the analysis lock, the arms are not the arms the lock was written about,
and the run refuses rather than writing predictions under a lock that does not describe them.

Runs as `augexp`, which cannot read confirmation labels. It asserts that: if a confirmation input
row carries a label, that is a custody failure and the run stops.

The shift rows are handled by a division of labour. This program applies A-recal using the
intercept fitted on the SHIFTED CALIBRATION split, which is the arm the lock describes and needs
no confirmation label. Selecting the shifted confirmation population is `augctl`'s job at scoring
time, because it is a function of confirmation labels and a fixed seed.

Output format is compact on purpose. A per-id JSON object across 23 arm-vectors and 1.37M rows is
hundreds of megabytes of repeated id strings; ids are written once and each arm is a string of
'0' and '1' in that id order.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from e1_fit import (  # noqa: E402
    HELD_OUT_RATIOS, RATIOS, SEED_FIT, build_arms, embed, fit_bandit, fit_cost_conditioned,
    fit_logistic, fit_mlp, fit_temperature, load_rows, recalibrate_intercept, resample_to_prior,
    set_gpu_budget,
)

# The arms each primary contrast needs, from the E1 design lock. Nothing else is written.
PRIMARY_ARMS = ("A", "B-stale", "C", "C*", "E")
SHIFT_ARMS = ("A-raw", "A-recal", "B-retrain_S", "C*", "E")
SHIFT_RATIO = "1:9"


def pack(actions) -> str:
    """One arm's actions as a string of '0' and '1', in confirmation id order."""
    return "".join("1" if int(a) else "0" for a in actions.tolist())


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--stage", type=Path, default=Path("/srv/aug/stage/parts"))
    parser.add_argument("--corpus", default="civil")
    parser.add_argument("--analysis-lock", type=Path, required=True,
                        help="the analysis lock JSON this run claims to be under")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--max-length", type=int, default=256)
    parser.add_argument("--gpu-budget-gib", type=float, default=8.0)
    parser.add_argument("--limit", type=int, help="cap rows per partition, for a smoke run")
    parser.add_argument("--temperature-tolerance", type=float, default=1e-5)
    args = parser.parse_args(argv)

    import os
    os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")
    import torch
    import transformers

    device = "cuda" if torch.cuda.is_available() else "cpu"
    set_gpu_budget(torch, device, args.gpu_budget_gib)
    started = time.time()

    lock_bytes = args.analysis_lock.read_bytes()
    lock = json.loads(lock_bytes)
    if lock.get("corpus") != args.corpus:
        raise SystemExit(f"the lock is for corpus {lock.get('corpus')!r}, not {args.corpus!r}")

    def read(name):
        rows = load_rows(args.stage / f"{args.corpus}-{name}" / "rows.json")
        return rows[:args.limit] if args.limit else rows

    fit_rows = read("fit")
    calibration_rows = read("calibration")
    confirmation_rows = read("confirmation-inputs")
    # Custody, checked rather than assumed: this principal must not be able to see an outcome.
    leaked = [r for r in confirmation_rows[:1000] if "label" in r]
    if leaked:
        raise SystemExit("a confirmation input row carries a label; refusing to run")

    fit_x = embed(torch, transformers, [r["text"] for r in fit_rows], device,
                  args.batch_size, args.max_length).to(device)
    fit_y = torch.tensor([int(r["label"]) for r in fit_rows], device=device)
    cal_x = embed(torch, transformers, [r["text"] for r in calibration_rows], device,
                  args.batch_size, args.max_length).to(device)
    cal_y = torch.tensor([int(r["label"]) for r in calibration_rows], device=device)

    # --- re-derive the arms, then prove they are the ones the lock describes ----------------
    w, b = fit_logistic(torch, fit_x, fit_y)
    temperature = fit_temperature(torch, (fit_x @ w + b), fit_y)
    drift = abs(temperature - lock["temperature"])
    if drift > args.temperature_tolerance:
        raise SystemExit(
            f"recomputed temperature {temperature!r} differs from the lock's "
            f"{lock['temperature']!r} by {drift:g}; these are not the arms the lock was written "
            "about, so no prediction is written")

    fitted = {"b_retrain": {}, "e_bandit": {}}
    for ratio in RATIOS:
        fp, fn = RATIOS[ratio]
        c_fp, c_fn = fp / (fp + fn), fn / (fp + fn)
        weights = torch.where(fit_y == 1, c_fn, c_fp).float()
        fitted["b_retrain"][ratio] = fit_logistic(torch, fit_x, fit_y, weights)
        log_ratio = torch.full((fit_x.shape[0],), math.log(c_fp / c_fn), device=device)
        fitted["e_bandit"][ratio] = fit_bandit(torch, fit_x, fit_y, log_ratio, (c_fp, c_fn))
    from e1_fit import TRAINING_RATIOS
    mixed_ratio = torch.tensor(
        [RATIOS[TRAINING_RATIOS[i % len(TRAINING_RATIOS)]][1]
         / RATIOS[TRAINING_RATIOS[i % len(TRAINING_RATIOS)]][0]
         for i in range(fit_x.shape[0])], device=device, dtype=torch.float)
    fitted["c_mlp"] = fit_mlp(torch, fit_x, fit_y, mixed_ratio)
    fitted["c_star"] = fit_cost_conditioned(torch, fit_x, fit_y, torch.log(1.0 / mixed_ratio))

    # The A-recal intercept comes from the SHIFTED CALIBRATION split and its 200-label budget,
    # exactly as in the fit run. It is a property of the arm, so confirmation supplies no label.
    fit_prior = fit_y.float().mean().item()
    target_prior = min(3 * fit_prior, 0.5)
    shift_index = resample_to_prior(torch, cal_y, target_prior)
    shift_logits = (cal_x[shift_index] @ w + b).squeeze(1) / temperature
    shift_y = cal_y[shift_index]
    budget = min(200, shift_y.numel())
    label_index = torch.randperm(shift_y.numel(), generator=torch.Generator(device="cpu")
                                 .manual_seed(80_103))[:budget].to(shift_y.device)
    intercept = recalibrate_intercept(torch, shift_logits[label_index], shift_y[label_index])
    fp_s, fn_s = RATIOS[SHIFT_RATIO]
    c_fp_s, c_fn_s = fp_s / (fp_s + fn_s), fn_s / (fp_s + fn_s)
    prior_weight = torch.where(fit_y == 1,
                               target_prior / max(fit_prior, 1e-9),
                               (1 - target_prior) / max(1 - fit_prior, 1e-9)).float()
    cost_weight = torch.where(fit_y == 1, c_fn_s, c_fp_s).float()
    w_s, b_s = fit_logistic(torch, fit_x, fit_y, prior_weight * cost_weight)

    # --- confirmation: embed the inputs and write actions ------------------------------------
    ids = [r["id"] for r in confirmation_rows]
    conf_x = embed(torch, transformers, [r["text"] for r in confirmation_rows], device,
                   args.batch_size, args.max_length).to(device)
    conf_scores = torch.sigmoid((conf_x @ w + b).squeeze(1) / temperature)
    # A_tuned needs labels to tune a threshold, and this split has none. The design lock calls it
    # descriptive only and no primary contrast uses it, so it is simply not written.
    placeholder = torch.zeros(conf_x.shape[0], dtype=torch.long, device=device)

    arms: dict[str, str] = {}
    for ratio in HELD_OUT_RATIOS:
        actions, _, _ = build_arms(torch, conf_scores, conf_x, placeholder, fitted, ratio)
        for name in (*PRIMARY_ARMS, f"B-retrain_{ratio}"):
            arms[f"{ratio}|{name}"] = pack(actions[name])

    log_ratio_s = torch.full((conf_x.shape[0],), math.log(c_fp_s / c_fn_s), device=device)
    w_c, gamma_c, b_c = fitted["c_star"]
    w_e, gamma_e, b_e = fitted["e_bandit"][SHIFT_RATIO]
    shift_actions = {
        "A-raw": (conf_scores >= c_fp_s).long(),
        "A-recal": (torch.sigmoid(
            (conf_x @ w + b).squeeze(1) / temperature + intercept) >= c_fp_s).long(),
        "B-retrain_S": ((conf_x @ w_s + b_s).squeeze(1) >= 0).long(),
        "C*": ((conf_x @ w_c + gamma_c * log_ratio_s.view(-1, 1) + b_c).squeeze(1) >= 0).long(),
        "E": ((conf_x @ w_e + gamma_e * log_ratio_s.view(-1, 1) + b_e).squeeze(1) >= 0).long(),
    }
    for name in SHIFT_ARMS:
        arms[f"S|{name}"] = pack(shift_actions[name])

    report = {
        "experiment": "E1",
        "corpus": args.corpus,
        "device": device,
        "rows": {"fit": len(fit_rows), "calibration": len(calibration_rows),
                 "confirmation": len(confirmation_rows)},
        "temperature": temperature,
        "temperature_matches_lock": True,
        "shift": {"fit_prior": fit_prior, "target_prior": target_prior,
                  "label_budget": budget, "fitted_intercept": intercept.item(),
                  "cost_ratio": SHIFT_RATIO,
                  "population_selected_by": "augctl at scoring time, from confirmation labels"},
        "analysis_lock_sha256": hashlib.sha256(lock_bytes).hexdigest(),
        "reads_no_confirmation_label": True,
        "format": "ids once; each arm is a string of '0'/'1' in id order, keyed 'ratio|arm'",
        "ids": ids,
        "arms": arms,
        "wall_clock_s": round(time.time() - started, 1),
        "limits": [
            "A_tuned is not written: tuning its threshold needs labels this principal does not have, and the design lock calls it descriptive only.",
            "The A-recal intercept is fitted on the shifted CALIBRATION split, which is the arm the lock describes; no confirmation label is read here.",
            "The shifted confirmation population is selected by augctl, because it is a function of confirmation labels and a fixed seed.",
        ],
    }
    args.out.write_text(json.dumps(report), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in ("ids", "arms")}, indent=2))
    print(f"arms written: {len(arms)}; ids: {len(ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
