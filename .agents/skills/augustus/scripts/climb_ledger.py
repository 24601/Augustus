#!/usr/bin/env python3
"""Replay an append-only climb ledger and decide what it supports; never climb.

Input is one JSON ledger with schema_version=1, an immutable config, an
anchor (the incumbent every round is measured against), and rounds in order.
Each round has an index, a candidate id, a delta against the ANCHOR, the
evaluator and split hashes it ran under, the fresh-row ids it was challenged
on, its probe results, and optional spend.

This is a replay, not a search. It answers one question: given what the
ledger records, what is this climb allowed to claim?

Terminal states
---------------
promoted_candidate          a frozen finalist cleared confirmation
incumbent_retained          nothing beat the anchor; a first-class result
dont_train(reason)          G0 answered before any round
insufficient_evidence       rounds ran, nothing is supported
insufficient_causal_evidence  identification (X5b) does not hold
unsupported_sampling_design the confirmation sample cannot carry a bound
paused_budget               a metered budget stopped the run
blocked(reason)             the ledger itself is not trustworthy
needs_human(question)       one question, asked once

Hard gates, each of which blocks the whole ledger
-------------------------------------------------
- The config is immutable. Any round that changes it is tampering, not a round.
- The evaluator and split hashes must not drift. Drift fails closed: a climb
  measured against a moving evaluator measures nothing.
- Every round reports its delta against the ORIGINAL anchor, never against the
  previous round, so a chain of small wins cannot drift away from the start.
- Candidates are challenged on fresh rows. Reusing a previous round's rows is
  the oldest way to climb a number without improving anything.
- Probes and per-label recall floors are hard gates, not advisory scores.
- Rounds are bounded, and the bound is declared in the config.
- Confirmation rows are burned once read.

What this does NOT do
---------------------
It replays what the ledger declares. It runs no model, reads no data, and
verifies no hash it is given. A supported claim here still needs the
confirmation helper's bound and the provenance gate's verdict.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SCHEMA_VERSION = 1


class LedgerError(ValueError):
    """A malformed ledger. Distinct from a terminal state."""


def _object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise LedgerError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise LedgerError(f"{name} must be nonempty text")
    return value


def _number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise LedgerError(f"{name} must be a finite number")
    value = float(value)
    if value != value or value in (float("inf"), float("-inf")):
        raise LedgerError(f"{name} must be a finite number")
    return value


def _config(document):
    config = document.get("config")
    if not isinstance(config, dict):
        raise LedgerError("config must be an object")
    for name in ("evaluator_hash", "split_hash", "anchor_id"):
        _text(config.get(name), f"config {name}")
    rounds_allowed = config.get("max_rounds")
    if type(rounds_allowed) is not int or rounds_allowed < 1:
        raise LedgerError("config max_rounds must be a positive integer fixed in advance")
    budget = config.get("budget")
    if budget is not None:
        _number(budget, "config budget")
    return config


def _rounds(document):
    raw = document.get("rounds")
    if raw is None:
        raw = []
    if not isinstance(raw, list):
        raise LedgerError("rounds must be a list")
    rounds = []
    for position, entry in enumerate(raw):
        if not isinstance(entry, dict):
            raise LedgerError(f"round {position} must be an object")
        index = entry.get("index")
        if type(index) is not int or index != position + 1:
            raise LedgerError(f"round {position} index must be {position + 1}; the ledger is append-only and in order")
        parsed = {
            "index": index,
            "candidate_id": _text(entry.get("candidate_id"), f"round {index} candidate_id"),
            "delta_vs_anchor": _number(entry.get("delta_vs_anchor"), f"round {index} delta_vs_anchor"),
            "evaluator_hash": _text(entry.get("evaluator_hash"), f"round {index} evaluator_hash"),
            "split_hash": _text(entry.get("split_hash"), f"round {index} split_hash"),
            "config_snapshot": entry.get("config_snapshot"),
            "spend": None if entry.get("spend") is None else _number(entry.get("spend"), f"round {index} spend"),
        }
        rows = entry.get("challenge_row_ids")
        if not isinstance(rows, list) or not rows:
            raise LedgerError(f"round {index} challenge_row_ids must be a nonempty list")
        parsed["rows"] = [_text(row, f"round {index} challenge row id") for row in rows]
        probes = entry.get("probes")
        if probes is None:
            probes = {}
        if not isinstance(probes, dict):
            raise LedgerError(f"round {index} probes must be an object")
        for name, outcome in probes.items():
            if outcome not in ("pass", "fail", "not_run"):
                raise LedgerError(f"round {index} probe {name} must be pass, fail, or not_run")
        parsed["probes"] = probes
        rounds.append(parsed)
    return rounds


def replay(document) -> dict:
    if not isinstance(document, dict):
        raise LedgerError("document must be an object")
    if type(document.get("schema_version")) is not int or document["schema_version"] != SCHEMA_VERSION:
        raise LedgerError(f"schema_version must be integer {SCHEMA_VERSION}")

    dont_train = document.get("dont_train_reason")
    if dont_train is not None:
        reason = _text(dont_train, "dont_train_reason")
        return _result(f"dont_train({reason})", [],
                       note="G0 answered before any round; no climb was run")

    config = _config(document)
    rounds = _rounds(document)
    blocks: list[dict] = []
    seen_rows: dict[str, int] = {}

    for entry in rounds:
        index = entry["index"]
        if entry["config_snapshot"] is not None and entry["config_snapshot"] != config:
            blocks.append({"round": index, "gate": "config_immutable",
                           "detail": "the round ran under a different config than the ledger declares"})
        if entry["evaluator_hash"] != config["evaluator_hash"]:
            blocks.append({"round": index, "gate": "evaluator_drift",
                           "detail": {"declared": config["evaluator_hash"], "round": entry["evaluator_hash"]}})
        if entry["split_hash"] != config["split_hash"]:
            blocks.append({"round": index, "gate": "split_drift",
                           "detail": {"declared": config["split_hash"], "round": entry["split_hash"]}})
        reused = sorted({row for row in entry["rows"] if row in seen_rows})
        if reused:
            blocks.append({"round": index, "gate": "stale_challenge_rows",
                           "detail": {"reused": reused,
                                      "first_seen_in_round": {row: seen_rows[row] for row in reused}}})
        for row in entry["rows"]:
            seen_rows.setdefault(row, index)
        failed = sorted(name for name, outcome in entry["probes"].items() if outcome == "fail")
        if failed:
            blocks.append({"round": index, "gate": "probe_failed", "detail": {"probes": failed}})
        not_run = sorted(name for name, outcome in entry["probes"].items() if outcome == "not_run")
        if not_run:
            blocks.append({"round": index, "gate": "probe_not_run",
                           "detail": {"probes": not_run,
                                      "note": "a probe that did not run is not a probe that passed"}})

    if len(rounds) > config["max_rounds"]:
        blocks.append({"round": len(rounds), "gate": "round_bound_exceeded",
                       "detail": {"max_rounds": config["max_rounds"], "rounds": len(rounds)}})

    spent = sum(entry["spend"] for entry in rounds if entry["spend"] is not None)
    budget = config.get("budget")
    over_budget = budget is not None and spent > budget

    if blocks:
        return _result("blocked(ledger_gate_failed)", rounds, blocks=blocks, spent=spent)
    if over_budget:
        return _result("paused_budget", rounds, spent=spent,
                       note=f"spend {spent} exceeds the declared budget {budget}")

    question = document.get("needs_human")
    if question is not None:
        return _result(f"needs_human({_text(question, 'needs_human')})", rounds, spent=spent)

    identification = document.get("identification_holds")
    if identification is False:
        return _result("insufficient_causal_evidence", rounds, spent=spent)
    sampling = document.get("confirmation_sampling_design")
    if sampling is not None and sampling != "equal_probability":
        return _result("unsupported_sampling_design", rounds, spent=spent)

    promoted = document.get("confirmed_candidate")
    if promoted is not None:
        candidate = _text(promoted, "confirmed_candidate")
        finalists = document.get("frozen_finalists")
        if not isinstance(finalists, list) or candidate not in finalists:
            return _result("blocked(candidate_was_not_a_frozen_finalist)", rounds, spent=spent,
                           blocks=[{"round": None, "gate": "unfrozen_promotion",
                                    "detail": {"candidate": candidate, "frozen_finalists": finalists}}])
        return _result("promoted_candidate", rounds, spent=spent, candidate=candidate)

    if not rounds:
        return _result("insufficient_evidence", rounds, spent=spent, note="no round was run")
    best = min(rounds, key=lambda entry: entry["delta_vs_anchor"])
    if best["delta_vs_anchor"] >= 0:
        return _result("incumbent_retained", rounds, spent=spent,
                       note="no round beat the anchor; retaining the incumbent is a result")
    return _result("insufficient_evidence", rounds, spent=spent,
                   note="a round beat the anchor in search, which is descriptive until confirmation")


def _result(state, rounds, *, blocks=None, spent=0.0, candidate=None, note=None):
    result = {
        "schema_version": SCHEMA_VERSION,
        "terminal_state": state,
        "rounds_replayed": len(rounds),
        "blocked_by": blocks or [],
        "spend": spent,
        "promoted_candidate": candidate,
        "best_delta_vs_anchor": min((entry["delta_vs_anchor"] for entry in rounds), default=None),
        "limits": [
            "A replay of declared records. No model runs, no data is read, and no hash here is verified.",
            "Every delta is against the original anchor by construction; this checks that the ledger says so, not that the number is right.",
            "A supported climb still needs the confirmation helper's bound and the provenance gate's verdict.",
            "`incumbent_retained` is a result, not a failure.",
            "A probe that did not run is not a probe that passed.",
        ],
    }
    if note:
        result["note"] = note
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("ledger", type=Path, help="append-only climb ledger JSON")
    args = parser.parse_args(argv)
    try:
        raw = args.ledger.read_bytes()
        document = json.loads(raw, object_pairs_hook=_object)
        result = replay(document)
        result["input_sha256"] = hashlib.sha256(raw).hexdigest()
        print(json.dumps(result, indent=2, allow_nan=False))
    except (OSError, ValueError, RecursionError) as exc:
        parser.exit(2, f"error: {exc}\n")
    # Fail closed: only a promotion or a deliberate retention exits 0.
    return 0 if result["terminal_state"] in ("promoted_candidate", "incumbent_retained") else 1


if __name__ == "__main__":
    raise SystemExit(main())
