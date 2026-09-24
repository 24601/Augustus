#!/usr/bin/env python3
"""E3: generate the frozen replay tables. Nine calls per question per reader, no gold answer read.

Runs as `augexp` on the GPU, served by the image's vLLM. It reads the published HotpotQA INPUTS —
question and paragraphs, never the gold answer — and writes, for every question and every
k ∈ {2, 4, 6}, what the reader said and how confident it was. `augctl` scores those answers later.

Full-information replay is the identification strategy: every answer at every k exists, so a
policy that would have stopped at k = 2 and one that would have expanded to k = 6 are both
evaluated on the same frozen table, and selection cannot be confounded by what a live agent would
have done next. It is also why E3 is not a claim about live agents.

The three calls at each k are:

  answer         the short answer, greedy, 64 tokens
  answerable     yes/no, one token, read as a probability from the logprobs rather than the string
  action         stop / expand / abstain, one token, read the same way

Arm (i), the implicit prompt, is the reader's own `action`. Arms (ii) and (iv) threshold
`answerable`. Arm (iii) thresholds a dense similarity that needs no reader call and is computed
here with the same staged MiniLM E1 used, so every arm reads one frozen table.

A corpus fact that the partitioner found and this program must not paper over: 60 of the 7,405
questions carry fewer than ten paragraphs, and 21 carry only two. For those, k = 4 and k = 6 read
the same evidence as k = 2. Expanding still costs a round under U = EM − λ·rounds/3, which is the
honest treatment: the policy paid for evidence it did not get. Each row records the effective k so
the analysis can say how often that happened instead of discovering it later.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

K_LEVELS = (2, 4, 6)
MAX_ANSWER_TOKENS = 64
EMBED_MODEL_DIR = "sentence-transformers__all-MiniLM-L6-v2"
ANSWER_WORDS = ("yes", "no")
ACTIONS = ("stop", "expand", "abstain")


def context_of(paragraphs, k: int) -> tuple[str, int]:
    """The first k paragraphs as text, and the number actually available."""
    used = paragraphs[:k]
    body = "\n\n".join(f"{p['title']}: {p['text']}" for p in used)
    return body, len(used)


def answer_prompt(question: str, context: str) -> str:
    return (f"{context}\n\nQuestion: {question}\n"
            "Answer with the shortest exact span or entity that answers the question, "
            "and nothing else.\nAnswer:")


def answerable_prompt(question: str, context: str) -> str:
    return (f"{context}\n\nQuestion: {question}\n"
            "Can this question be answered from the passages above? Reply yes or no.\nAnswer:")


def action_prompt(question: str, context: str) -> str:
    return (f"{context}\n\nQuestion: {question}\n"
            "Choose one word. stop: answer now from these passages. expand: read more passages. "
            "abstain: this cannot be answered.\nChoice:")


def distribution(logprobs, words) -> dict[str, float]:
    """Probability mass on each word's first token, renormalized over the words we asked about.

    Reading the distribution rather than the emitted string is the point: a threshold needs a
    number, and `yes` versus `no` as a string gives a policy nothing to tune. Mass that landed on
    neither word is reported, because a large residual means the question did not constrain the
    reader and the number is not a clean probability of anything.
    """
    mass = {word: 0.0 for word in words}
    total = 0.0
    for entry in (logprobs or {}).values():
        token = getattr(entry, "decoded_token", None)
        if token is None:
            continue
        probability = math.exp(entry.logprob)
        total += probability
        stripped = token.strip().lower()
        for word in words:
            if stripped == word or (stripped and word.startswith(stripped) and len(stripped) > 1):
                mass[word] += probability
                break
    named = sum(mass.values())
    result = {word: (value / named if named > 0 else 0.0) for word, value in mass.items()}
    result["_mass_on_named_words"] = named / total if total > 0 else 0.0
    return result


def similarity(rows, model_dir: Path, batch_size: int):
    """Max cosine between the question and each read paragraph, for arm (iii).

    No reader call, so it costs nothing against the 9-call budget, and it is computed here so that
    every arm reads one frozen table rather than recomputing a feature at analysis time.
    """
    import torch
    import transformers

    tokenizer = transformers.AutoTokenizer.from_pretrained(str(model_dir))
    model = transformers.AutoModel.from_pretrained(str(model_dir)).cuda().eval()

    def embed(texts):
        out = []
        with torch.no_grad():
            for start in range(0, len(texts), batch_size):
                encoded = tokenizer(texts[start:start + batch_size], padding=True, truncation=True,
                                    max_length=256, return_tensors="pt").to("cuda")
                hidden = model(**encoded).last_hidden_state
                mask = encoded["attention_mask"].unsqueeze(-1).float()
                pooled = (hidden * mask).sum(1) / mask.sum(1).clamp(min=1e-9)
                out.append(torch.nn.functional.normalize(pooled, dim=1).cpu())
        return torch.cat(out)

    questions = embed([row["question"] for row in rows])
    flat, spans = [], []
    for row in rows:
        spans.append((len(flat), len(flat) + len(row["paragraphs"])))
        flat.extend(f"{p['title']}: {p['text']}" for p in row["paragraphs"])
    paragraphs = embed(flat)

    scores = []
    for index, row in enumerate(rows):
        start, end = spans[index]
        per_k = {}
        for k in K_LEVELS:
            stop = min(start + k, end)
            per_k[k] = (paragraphs[start:stop] @ questions[index]).max().item() if stop > start \
                else 0.0
        scores.append(per_k)
    del model
    torch.cuda.empty_cache()
    return scores


def replay(llm, sampling, rows):
    """Every call for every question at every k, in one batch per call type.

    Batching by call type rather than by question is what makes this affordable, and it is also
    what the determinism check measures: vLLM's batched decode is not bitwise reproducible across
    runs, so the tables are frozen once and every arm reads these, not a re-execution.
    """
    from vllm import SamplingParams

    one_token = SamplingParams(temperature=0.0, max_tokens=1, logprobs=20)
    prompts, index = [], []
    for row_index, row in enumerate(rows):
        for k in K_LEVELS:
            context, used = context_of(row["paragraphs"], k)
            prompts.append(answer_prompt(row["question"], context))
            index.append((row_index, k, "answer", used))
    answers = llm.generate(prompts, sampling)

    yes_prompts, action_prompts = [], []
    for row in rows:
        for k in K_LEVELS:
            context, _ = context_of(row["paragraphs"], k)
            yes_prompts.append(answerable_prompt(row["question"], context))
            action_prompts.append(action_prompt(row["question"], context))
    answerable = llm.generate(yes_prompts, one_token)
    actions = llm.generate(action_prompts, one_token)

    table = {}
    for position, (row_index, k, _, used) in enumerate(index):
        row = rows[row_index]
        entry = table.setdefault(row["id"], {"id": row["id"], "k": {}})
        answer_output = answers[position].outputs[0]
        yes = distribution(answerable[position].outputs[0].logprobs[0], ANSWER_WORDS)
        act = distribution(actions[position].outputs[0].logprobs[0], ACTIONS)
        entry["k"][str(k)] = {
            "k_effective": used,
            "answer": answer_output.text.strip(),
            "answer_tokens": len(answer_output.token_ids),
            "prompt_tokens": len(answers[position].prompt_token_ids),
            "p_answerable": yes["yes"],
            "answerable_mass": yes["_mass_on_named_words"],
            "action": max(ACTIONS, key=lambda a: act[a]),
            "p_action": {a: act[a] for a in ACTIONS},
            "action_mass": act["_mass_on_named_words"],
        }
    return table


def disagreement(first: dict, second: dict) -> dict:
    """Realized rerun disagreement, per call and per question, against the lock's 5% tolerance.

    The lock records 59.8% per-prompt identity from M0 and calls the 0.598^9 figure for a whole
    question [H], because it assumes independence across calls. This measures the joint rate
    instead of assuming it, which is the whole point of the check.
    """
    call_total = call_same = question_total = question_same = 0
    for key, left in first.items():
        right = second.get(key)
        if right is None:
            continue
        question_total += 1
        identical = True
        for k in map(str, K_LEVELS):
            call_total += 1
            same = (left["k"][k]["answer"] == right["k"][k]["answer"])
            call_same += same
            identical &= same
        question_same += identical
    return {
        "questions": question_total,
        "per_call_identity": call_same / call_total if call_total else None,
        "per_question_identity": question_same / question_total if question_total else None,
        "per_call_disagreement": 1 - call_same / call_total if call_total else None,
        "per_question_disagreement": 1 - question_same / question_total if question_total else None,
        "tolerance": 0.05,
        "note": "Answer-text identity only. A different answer string is a disagreement even when "
                "both would score the same EM; that is the conservative direction.",
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--stage", type=Path, default=Path("/srv/aug/stage/parts"))
    parser.add_argument("--partition", default="search", choices=("search", "confirmation"))
    parser.add_argument("--reader", type=Path, required=True, help="the staged reader directory")
    parser.add_argument("--weights", type=Path, required=True, help="the staged weights root")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--limit", type=int, help="cap questions, for a pilot")
    parser.add_argument("--ids", type=Path, help="JSON list of ids to replay, such as a pilot")
    parser.add_argument("--rerun-check", action="store_true",
                        help="replay twice and report the realized disagreement rate")
    # The design lock budgets 14 GiB for the readers. On a 124 GiB device that is 0.113, and the
    # default is set just under it rather than left at vLLM's 0.9, because an allocator that is
    # allowed to take the whole card will take the whole card.
    parser.add_argument("--gpu-memory-utilization", type=float, default=0.11)
    parser.add_argument("--max-model-len", type=int, default=4096)
    parser.add_argument("--embed-batch-size", type=int, default=128)
    args = parser.parse_args(argv)

    started = time.time()
    rows = json.loads((args.stage / f"hotpot-{args.partition}" / "rows.json")
                      .read_text(encoding="utf-8"))
    if any("answer" in row for row in rows):
        raise SystemExit("an input row carries a gold answer; refusing to run")
    if args.ids:
        wanted = set(json.loads(args.ids.read_text(encoding="utf-8")))
        rows = [row for row in rows if row["id"] in wanted]
    if args.limit:
        rows = rows[:args.limit]
    if not rows:
        raise SystemExit("no rows selected")

    from vllm import LLM, SamplingParams

    llm = LLM(model=str(args.reader), dtype="bfloat16", enforce_eager=True,
              gpu_memory_utilization=args.gpu_memory_utilization,
              max_model_len=args.max_model_len)
    sampling = SamplingParams(temperature=0.0, max_tokens=MAX_ANSWER_TOKENS)

    table = replay(llm, sampling, rows)
    rerun = disagreement(table, replay(llm, sampling, rows)) if args.rerun_check else None

    scores = similarity(rows, args.weights / EMBED_MODEL_DIR, args.embed_batch_size)
    for row, per_k in zip(rows, scores):
        for k in K_LEVELS:
            table[row["id"]]["k"][str(k)]["similarity"] = per_k[k]

    short = sum(1 for row in rows if len(row["paragraphs"]) < max(K_LEVELS))
    report = {
        "experiment": "E3",
        "partition": args.partition,
        "reader": args.reader.name,
        "questions": len(rows),
        "calls": len(rows) * len(K_LEVELS) * 3 * (2 if args.rerun_check else 1),
        "k_levels": list(K_LEVELS),
        "questions_with_fewer_than_six_paragraphs": short,
        "rerun_check": rerun,
        "wall_clock_s": round(time.time() - started, 1),
        "reads_no_gold_answer": True,
        "limits": [
            "Frozen table. Every arm, resplit and P6 draw reads this file; nothing re-executes the reader.",
            "Questions with fewer than six paragraphs read the same evidence at higher k, and expanding still costs a round. k_effective records where that happened.",
            "p_answerable and p_action are renormalized over the named words; the residual mass is reported beside each, and a large residual means the number is not a clean probability of anything.",
            "Similarity is MiniLM cosine on the same staged weights E1 used; it is a feature for arm (iii), not a claim about retrieval quality.",
        ],
        "table": table,
    }
    args.out.write_text(json.dumps(report), encoding="utf-8")
    summary = {k: v for k, v in report.items() if k != "table"}
    print(json.dumps(summary, indent=2))
    print(f"\ntable sha256: {hashlib.sha256(args.out.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
