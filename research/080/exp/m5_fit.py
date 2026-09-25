#!/usr/bin/env python3
"""M5: fit the non-PAW rungs and emit actions on confirmation inputs. Holds no confirmation label.

The five arms this program is responsible for:

  A1   an agent-synthesized program, frozen and hashed before any confirmation input is read
  R1   a frozen readout from Qwen3.5-2B: option logits at an answer slot, then an OOF temperature
  R2a  a logistic head on MiniLM embeddings
  R2b  a ridge head on R1's two-thirds-depth hidden state
  R3a  SetFit on a pinned body — THE COMPARATOR, not a family member

A2a and A2b are elsewhere (`m5_colab.py`), because they need a compiler that only runs on NVIDIA
and an inference runtime that is not torch.

Custody is the same as E1 and E3: this side reads fit and calibration WITH labels, because that is
what fitting is, and confirmation inputs WITHOUT them. It computes no confirmation loss. The
actions go to `augctl`, which grades them against labels that never left the host.

Resumability is deliberate rather than incidental. A long run on an ephemeral machine that loses
everything at hour six is worse than a slow one, so every (task, arm) result is written and hashed
as soon as it exists, and a rerun skips what is already on disk. Plan v4 §3.7 calls that the rule
for an E-ephemeral envelope; this is what it looks like in code.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import time
from pathlib import Path

ARMS = ("A1", "R1", "R2a", "R2b", "R3a")
FAMILY_MEMBERS = ("A1", "R1", "R2a", "R2b")  # R3a is the comparator, not a family member
MINILM = "sentence-transformers/all-MiniLM-L6-v2"
READOUT = "Qwen/Qwen3.5-2B-Base"
SETFIT_BODY = "sentence-transformers/paraphrase-mpnet-base-v2"
READOUT_DEPTH = 2 / 3  # R2b reads here, per the design lock
SEED = 80_502


def digest_of(payload) -> str:
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, sort_keys=True,
                   separators=(",", ":")).encode("utf-8")).hexdigest()


def environment() -> dict:
    report = {"python": platform.python_version(), "platform": platform.platform()}
    try:
        import torch
        report["torch"] = torch.__version__
        if torch.cuda.is_available():
            properties = torch.cuda.get_device_properties(0)
            report["device"] = "cuda"
            report["gpu"] = properties.name
            report["gpu_total_mib"] = properties.total_memory // 2 ** 20
            report["bf16"] = torch.cuda.is_bf16_supported()
        elif getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
            report["device"] = "mps"
        else:
            report["device"] = "cpu"
    except ImportError:
        report["torch"] = None
        report["device"] = None
    return report


def device_of(torch):
    if torch.cuda.is_available():
        return "cuda"
    if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def embed(torch, transformers, texts, model_name: str, device: str, batch_size: int,
          max_length: int = 256):
    """Mean-pooled, L2-normalized sentence embeddings. The same shape E1 used, deliberately."""
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
    model = transformers.AutoModel.from_pretrained(model_name).to(device).eval()
    out = []
    with torch.no_grad():
        for start in range(0, len(texts), batch_size):
            encoded = tokenizer(texts[start:start + batch_size], padding=True, truncation=True,
                                max_length=max_length, return_tensors="pt").to(device)
            hidden = model(**encoded).last_hidden_state
            mask = encoded["attention_mask"].unsqueeze(-1).float()
            pooled = (hidden * mask).sum(1) / mask.sum(1).clamp(min=1e-9)
            out.append(torch.nn.functional.normalize(pooled, dim=1).cpu())
    del model
    if device == "cuda":
        torch.cuda.empty_cache()
    return torch.cat(out)


def fit_linear(torch, features, labels, classes: int, *, epochs=300, lr=0.1, weight_decay=0.0,
               device="cpu"):
    """Multinomial logistic regression by full-batch Adam, written here rather than imported.

    scikit-learn is present in the M5 image, but a head trained here runs identically on a machine
    that has only torch — which is the point of §3.7, and it costs about twenty lines.
    """
    torch.manual_seed(SEED)
    features = features.to(device)
    target = labels.to(device)
    weight = torch.zeros(features.shape[1], classes, device=device, requires_grad=True)
    bias = torch.zeros(classes, device=device, requires_grad=True)
    optimizer = torch.optim.Adam([weight, bias], lr=lr, weight_decay=weight_decay)
    for _ in range(epochs):
        optimizer.zero_grad()
        loss = torch.nn.functional.cross_entropy(features @ weight + bias, target)
        loss.backward()
        optimizer.step()
    return weight.detach(), bias.detach()


def fit_temperature(torch, logits, labels, *, epochs=300, lr=0.05, device="cpu"):
    """One scalar temperature, fitted out of fold. R1's registered calibration step.

    arbiter's card reports that refitting one temperature per (question type, option count) moves
    mean ECE from 0.466 to 0.081 on a comparable model, which is why this is a registered step and
    not an optional polish.
    """
    logits, labels = logits.to(device), labels.to(device)
    log_t = torch.zeros(1, device=device, requires_grad=True)
    optimizer = torch.optim.Adam([log_t], lr=lr)
    for _ in range(epochs):
        optimizer.zero_grad()
        loss = torch.nn.functional.cross_entropy(logits / log_t.exp(), labels)
        loss.backward()
        optimizer.step()
    return log_t.detach().exp().item()


def readout_states(torch, transformers, texts, device: str, batch_size: int, max_length: int):
    """R1's option logits and R2b's two-thirds-depth state, from one pass over the decoder.

    Taking both from the same forward is not a shortcut: R2b is defined in the design lock as a
    head on R1's state, so reading them separately would risk them describing different passes.
    """
    tokenizer = transformers.AutoTokenizer.from_pretrained(READOUT)
    model = transformers.AutoModel.from_pretrained(
        READOUT, torch_dtype=torch.bfloat16, output_hidden_states=True).to(device).eval()
    layers = model.config.num_hidden_layers if hasattr(model.config, "num_hidden_layers") \
        else model.config.text_config.num_hidden_layers
    depth = max(1, int(round(layers * READOUT_DEPTH)))

    last, mid = [], []
    with torch.no_grad():
        for start in range(0, len(texts), batch_size):
            encoded = tokenizer(texts[start:start + batch_size], padding=True, truncation=True,
                                max_length=max_length, return_tensors="pt").to(device)
            outputs = model(**encoded)
            mask = encoded["attention_mask"].unsqueeze(-1).float()

            def pool(states):
                return ((states * mask).sum(1) / mask.sum(1).clamp(min=1e-9)).float().cpu()

            last.append(pool(outputs.hidden_states[-1]))
            mid.append(pool(outputs.hidden_states[depth]))
    del model
    if device == "cuda":
        torch.cuda.empty_cache()
    return torch.cat(last), torch.cat(mid), {"layers": layers, "read_at_layer": depth}


def actions_from_logits(torch, logits, label_names: list[str]) -> list[str]:
    return [label_names[index] for index in logits.argmax(dim=1).tolist()]


def checkpoint_path(out: Path, task: str, arm: str) -> Path:
    return out / f"{task}.{arm}.json"


def already_done(out: Path, task: str, arm: str) -> dict | None:
    """A finished (task, arm) is never recomputed. An ephemeral machine makes this load-bearing."""
    path = checkpoint_path(out, task, arm)
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return payload if payload.get("complete") else None


def write_checkpoint(out: Path, task: str, arm: str, payload: dict) -> str:
    payload["complete"] = True
    path = checkpoint_path(out, task, arm)
    text = json.dumps(payload, ensure_ascii=False)
    path.write_text(text, encoding="utf-8")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def run_arm(arm: str, task: str, block: dict, torch, transformers, device: str, args) -> dict:
    """One arm on one task. Returns a payload with actions and everything needed to read them."""
    fit_rows = block["fit_examples"]
    inputs = block["confirmation_inputs"]
    labels = sorted({str(row["label"]) for row in fit_rows})
    index = {name: position for position, name in enumerate(labels)}
    y = torch.tensor([index[str(row["label"])] for row in fit_rows])
    started = time.time()
    detail = {"arm": arm, "task": task, "classes": len(labels),
              "fit_rows": len(fit_rows), "confirmation_rows": len(inputs)}

    if arm == "A1":
        import m5_a1
        program = m5_a1.program_for(task, labels)
        source = m5_a1.source_of(task)
        # Frozen and hashed BEFORE a confirmation input is read. The order is the control, and it
        # is what lets an agent-written program be an arm rather than a moving target.
        detail["program_sha256"] = hashlib.sha256(source.encode("utf-8")).hexdigest()
        detail["frozen_before_confirmation"] = True
        actions = [program(row["text"]) for row in inputs]

    elif arm == "R2a":
        fit_x = embed(torch, transformers, [r["text"] for r in fit_rows], MINILM, device,
                      args.batch_size)
        weight, bias = fit_linear(torch, fit_x, y, len(labels), device=device)
        conf_x = embed(torch, transformers, [r["text"] for r in inputs], MINILM, device,
                       args.batch_size)
        actions = actions_from_logits(torch, conf_x.to(device) @ weight + bias, labels)

    elif arm in ("R1", "R2b"):
        fit_last, fit_mid, shape = readout_states(
            torch, transformers, [r["text"] for r in fit_rows], device, args.readout_batch_size,
            args.max_length)
        detail.update(shape)
        states = fit_last if arm == "R1" else fit_mid
        weight, bias = fit_linear(torch, states, y, len(labels), device=device,
                                  weight_decay=0.0 if arm == "R1" else 1e-3)
        if arm == "R1":
            # The OOF temperature the design lock registers, fitted on a held-out slice of fit.
            split = max(1, len(fit_rows) // 5)
            detail["temperature"] = fit_temperature(
                torch, states[:split].to(device) @ weight + bias, y[:split], device=device)
        conf_last, conf_mid, _ = readout_states(
            torch, transformers, [r["text"] for r in inputs], device, args.readout_batch_size,
            args.max_length)
        conf_states = conf_last if arm == "R1" else conf_mid
        logits = conf_states.to(device) @ weight + bias
        if arm == "R1":
            logits = logits / detail["temperature"]
        actions = actions_from_logits(torch, logits, labels)

    elif arm == "R3a":
        from setfit import SetFitModel, Trainer, TrainingArguments
        from datasets import Dataset
        model = SetFitModel.from_pretrained(SETFIT_BODY)
        trainer = Trainer(
            model=model,
            args=TrainingArguments(batch_size=args.batch_size, num_epochs=1, seed=SEED),
            train_dataset=Dataset.from_dict({"text": [r["text"] for r in fit_rows],
                                             "label": [index[str(r["label"])] for r in fit_rows]}))
        trainer.train()
        predictions = model.predict([r["text"] for r in inputs])
        actions = [labels[int(p)] for p in predictions]

    else:
        raise SystemExit(f"unknown arm {arm}")

    detail["wall_clock_s"] = round(time.time() - started, 1)
    detail["rows_per_second"] = round(len(inputs) / max(detail["wall_clock_s"], 1e-9), 2)
    detail["actions"] = dict(zip((row["id"] for row in inputs), actions))
    detail["label_set_digest"] = digest_of(labels)
    if len(detail["actions"]) != len(inputs):
        raise SystemExit(f"{task} {arm}: {len(detail['actions'])} actions for {len(inputs)} inputs")
    return detail


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--expect-sha256", required=True)
    parser.add_argument("--out", type=Path, required=True, help="checkpoint directory")
    parser.add_argument("--arm", action="append", choices=ARMS,
                        help="restrict to these arms; default is all")
    parser.add_argument("--task", action="append", help="restrict to these tasks")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--readout-batch-size", type=int, default=16)
    parser.add_argument("--max-length", type=int, default=256)
    args = parser.parse_args(argv)

    digest = hashlib.sha256(args.bundle.read_bytes()).hexdigest()
    if digest != args.expect_sha256:
        parser.exit(2, f"error: bundle sha256 is {digest}, expected {args.expect_sha256}\n")
    bundle = json.loads(args.bundle.read_text(encoding="utf-8"))
    if bundle.get("contains_confirmation_labels"):
        parser.exit(2, "error: the bundle declares confirmation labels; refusing to run\n")

    import torch
    import transformers

    device = device_of(torch)
    args.out.mkdir(parents=True, exist_ok=True)
    arms = args.arm or list(ARMS)
    tasks = args.task or list(bundle["tasks"])

    summary = {"experiment": "M5", "side": "fit and predict; holds no label and cannot score",
               "bundle_sha256": digest, "spec_version": bundle["spec_version"],
               "environment": environment(), "device": device,
               "arms_requested": arms, "tasks_requested": tasks, "results": {}}

    for task in tasks:
        block = bundle["tasks"][task]
        for arm in arms:
            key = f"{task}|{arm}"
            existing = already_done(args.out, task, arm)
            if existing:
                summary["results"][key] = {"skipped": "already complete",
                                           "wall_clock_s": existing.get("wall_clock_s"),
                                           "rows": len(existing.get("actions", {}))}
                continue
            payload = run_arm(arm, task, block, torch, transformers, device, args)
            checkpoint = write_checkpoint(args.out, task, arm, payload)
            summary["results"][key] = {
                k: v for k, v in payload.items() if k not in ("actions", "complete")}
            summary["results"][key]["checkpoint_sha256"] = checkpoint
            print(json.dumps({key: summary["results"][key]}, indent=2), flush=True)

    summary["family_members_present"] = sorted(
        set(FAMILY_MEMBERS) & {key.split("|")[1] for key in summary["results"]})
    summary["comparator_present"] = "R3a" in {key.split("|")[1] for key in summary["results"]}
    summary["limits"] = [
        "This side holds no confirmation label and computes no loss; a score here would be a bug.",
        "A1 is frozen and hashed before any confirmation input is read, and the hash is recorded.",
        "Every (task, arm) is checkpointed as soon as it completes, so a lost session costs only the arm in flight.",
        "R2b reads R1's two-thirds-depth state from the SAME forward pass, so the two arms cannot describe different passes.",
        "A2a and A2b are not here: they need a compiler that runs only on NVIDIA and a runtime that is not torch.",
    ]
    (args.out / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "results"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
