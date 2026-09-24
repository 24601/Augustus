#!/usr/bin/env python3
"""E3: split HotpotQA distractor validation into search and confirmation, and publish INPUTS only.

Runs as `augctl`, which holds the corpora. It writes two things that live in different places for
the rest of E3:

  - the question and its ten distractor paragraphs, published to the staging tree the replay run
    can read;
  - the gold answer, retained with `augctl` and never published, because EM against gold is a
    label and the replay principal must not be able to compute its own score.

The split is seeded and fixed here: search 1,000 questions, which carry the 100-question sigma
pilot and the 50-question timing pilot as their first rows in shuffled order, and confirmation
the remaining 6,405. The design lock names those sizes; nothing here chooses them.

Paragraph order is the dataset's own order, not a retrieval ranking. The rounds read k ∈ {2, 4, 6}
of those paragraphs, so the order is part of the frozen input and is recorded in the manifest
digest rather than re-derived later.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import unicodedata
from pathlib import Path

SEED = 80_301
SEARCH_N = 1_000
SIGMA_PILOT_N = 100
TIMING_PILOT_N = 50
EXPECTED_ROWS = 7_405


def normalize(text: str) -> str:
    """NFKC, casefold, collapsed whitespace. Used only for the duplicate check and the digest."""
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def digest(rows: list[dict]) -> str:
    """A canonical digest of the rows, so two runs can be compared without shipping the rows."""
    payload = json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def read_validation(path: Path) -> list[dict]:
    """The distractor validation shard, as {id, question, answer, paragraphs}."""
    import pyarrow.parquet as pq

    table = pq.read_table(path)
    columns = {name: table.column(name).to_pylist() for name in table.column_names}
    if "context" not in columns:
        raise SystemExit(f"no context column; found {sorted(columns)}")

    rows = []
    for index in range(table.num_rows):
        context = columns["context"][index]
        # HotpotQA's context is {title: [...], sentences: [[...], ...]} or a list of pairs,
        # depending on the export. Both shapes appear in the wild, so handle both rather than
        # guessing and finding out after an hour of replay.
        if isinstance(context, dict):
            titles, sentence_lists = context["title"], context["sentences"]
        else:
            titles = [item[0] for item in context]
            sentence_lists = [item[1] for item in context]
        paragraphs = [{"title": title, "text": "".join(sentences)}
                      for title, sentences in zip(titles, sentence_lists)]
        rows.append({
            "id": columns["id"][index],
            "question": columns["question"][index],
            "answer": columns["answer"][index],
            "paragraphs": paragraphs,
        })
    return rows


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--parquet", type=Path, required=True)
    parser.add_argument("--stage", type=Path, required=True,
                        help="where the INPUTS are written; augexp reads this")
    parser.add_argument("--labels", type=Path, required=True,
                        help="where the gold answers are retained; augctl only")
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args(argv)

    rows = read_validation(args.parquet)
    if len(rows) != EXPECTED_ROWS:
        raise SystemExit(f"expected {EXPECTED_ROWS} validation rows, read {len(rows)}; "
                         "the design lock names that count and this is not it")

    seen, deduped = set(), []
    for row in rows:
        key = normalize(row["question"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)

    order = list(range(len(deduped)))
    random.Random(SEED).shuffle(order)
    search = [deduped[i] for i in order[:SEARCH_N]]
    confirmation = [deduped[i] for i in order[SEARCH_N:]]

    def publish(name, subset):
        inputs = [{"id": r["id"], "question": r["question"], "paragraphs": r["paragraphs"]}
                  for r in subset]
        labels = [{"id": r["id"], "answer": r["answer"]} for r in subset]
        (args.stage / f"hotpot-{name}").mkdir(parents=True, exist_ok=True)
        (args.stage / f"hotpot-{name}" / "rows.json").write_text(
            json.dumps(inputs, ensure_ascii=False), encoding="utf-8")
        (args.labels).mkdir(parents=True, exist_ok=True)
        (args.labels / f"hotpot-{name}-answers.json").write_text(
            json.dumps(labels, ensure_ascii=False), encoding="utf-8")
        return {"rows": len(inputs), "inputs_digest": digest(inputs),
                "answers_digest": digest(labels)}

    manifest = {
        "experiment": "E3",
        "corpus": "hotpot_qa distractor validation",
        "seed": SEED,
        "rows_in": len(rows),
        "rows_after_dedup": len(deduped),
        "exact_duplicate_questions_dropped": len(rows) - len(deduped),
        "partitions": {"search": publish("search", search),
                       "confirmation": publish("confirmation", confirmation)},
        # The pilots are the first rows of the shuffled search set, so they are fixed by the same
        # seed and need no second draw. Naming them here is what makes them prespecified.
        "sigma_pilot": {"n": SIGMA_PILOT_N,
                        "ids": [r["id"] for r in search[:SIGMA_PILOT_N]]},
        "timing_pilot": {"n": TIMING_PILOT_N,
                         "ids": [r["id"] for r in search[SIGMA_PILOT_N:
                                                        SIGMA_PILOT_N + TIMING_PILOT_N]]},
        "limits": [
            "Paragraph order is the dataset's own, not a retrieval ranking; k reads the first k of them.",
            "Gold answers are retained by augctl and never published; the replay principal cannot score itself.",
            "Deduplication is on the exact normalized question, which does not catch paraphrases.",
        ],
    }
    args.manifest.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: v for k, v in manifest.items()
                      if k not in ("sigma_pilot", "timing_pilot")}, indent=2))
    print(f"\nsigma pilot {SIGMA_PILOT_N} ids, timing pilot {TIMING_PILOT_N} ids, both recorded")
    print(f"manifest sha256: {hashlib.sha256(args.manifest.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
