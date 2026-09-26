from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / ".agents/skills/augustus/scripts/climb_ledger.py"
SPEC = importlib.util.spec_from_file_location("climb_ledger", SCRIPT)
ledger = importlib.util.module_from_spec(SPEC)
sys.modules["climb_ledger"] = ledger
SPEC.loader.exec_module(ledger)

CONFIG = {"evaluator_hash": "eval-abc", "split_hash": "split-def",
          "anchor_id": "incumbent-v1", "max_rounds": 3}


def round_entry(index, delta, rows, **extra):
    entry = {"index": index, "candidate_id": f"candidate-{index}", "delta_vs_anchor": delta,
             "evaluator_hash": CONFIG["evaluator_hash"], "split_hash": CONFIG["split_hash"],
             "challenge_row_ids": rows, "probes": {"nota_pair": "pass"}}
    entry.update(extra)
    return entry


def book(rounds, **extra):
    return {"schema_version": 1, "config": copy.deepcopy(CONFIG), "rounds": rounds,
            "confirmation_row_ids": ["held-out-1", "held-out-2"], **extra}


class ClimbLedgerTests(unittest.TestCase):
    def test_no_round_beating_the_anchor_retains_the_incumbent(self):
        result = ledger.replay(book([round_entry(1, +0.01, ["r1"]), round_entry(2, 0.0, ["r2"])]))
        self.assertEqual(result["terminal_state"], "incumbent_retained")
        self.assertEqual(result["best_delta_vs_anchor"], 0.0)

    def test_a_search_win_is_descriptive_until_confirmation(self):
        result = ledger.replay(book([round_entry(1, -0.05, ["r1"])]))
        self.assertEqual(result["terminal_state"], "insufficient_evidence")
        self.assertIn("descriptive until confirmation", result["note"])

    def test_a_confirmed_frozen_finalist_is_promoted(self):
        result = ledger.replay(book(
            [round_entry(1, -0.05, ["r1"])],
            frozen_finalists=["candidate-1"], confirmed_candidate="candidate-1"))
        self.assertEqual(result["terminal_state"], "promoted_candidate")
        self.assertEqual(result["promoted_candidate"], "candidate-1")

    def test_promoting_something_that_was_never_frozen_is_blocked(self):
        result = ledger.replay(book(
            [round_entry(1, -0.05, ["r1"])],
            frozen_finalists=["candidate-1"], confirmed_candidate="candidate-9"))
        self.assertEqual(result["terminal_state"], "blocked(candidate_was_not_a_frozen_finalist)")

    def test_evaluator_or_split_drift_fails_closed(self):
        for field in ("evaluator_hash", "split_hash"):
            with self.subTest(field=field):
                result = ledger.replay(book([round_entry(1, -0.05, ["r1"], **{field: "moved"})]))
                self.assertEqual(result["terminal_state"], "blocked(ledger_gate_failed)")
                self.assertEqual(result["blocked_by"][0]["gate"], field.replace("_hash", "_drift"))

    def test_reusing_a_previous_rounds_rows_is_blocked(self):
        result = ledger.replay(book([round_entry(1, -0.01, ["r1", "r2"]),
                                     round_entry(2, -0.09, ["r2", "r3"])]))
        self.assertEqual(result["terminal_state"], "blocked(ledger_gate_failed)")
        finding = result["blocked_by"][0]
        self.assertEqual(finding["gate"], "stale_challenge_rows")
        self.assertEqual(finding["detail"]["reused"], ["r2"])
        self.assertEqual(finding["detail"]["first_seen_in_round"], {"r2": 1})

    def test_a_changed_config_snapshot_is_tampering_not_a_round(self):
        moved = copy.deepcopy(CONFIG)
        moved["max_rounds"] = 99
        result = ledger.replay(book([round_entry(1, -0.05, ["r1"], config_snapshot=moved)]))
        self.assertEqual(result["terminal_state"], "blocked(ledger_gate_failed)")
        self.assertEqual(result["blocked_by"][0]["gate"], "config_immutable")

    def test_explicit_search_reuse_is_descriptive_and_confirmation_stays_separate(self):
        document = book([round_entry(1, -0.01, ["r1", "r2"]),
                         round_entry(2, -0.09, ["r2", "r3"])])
        document["config"]["search_reuse"] = True
        self.assertEqual(ledger.replay(document)["terminal_state"], "insufficient_evidence")
        document.update(frozen_finalists=["candidate-2"], confirmed_candidate="candidate-2")
        self.assertEqual(ledger.replay(document)["terminal_state"], "promoted_candidate")
        document["confirmation_row_ids"] = ["held-out-1", "r1"]
        self.assertEqual(ledger.replay(document)["terminal_state"],
                         "blocked(confirmation_overlaps_search)")

    def test_promotion_requires_a_run_candidate_and_confirmation_ids(self):
        document = book([round_entry(1, -0.05, ["r1"])],
                        frozen_finalists=["candidate-9"], confirmed_candidate="candidate-9")
        self.assertEqual(ledger.replay(document)["terminal_state"], "blocked(candidate_was_not_run)")
        document.update(frozen_finalists=["candidate-1"], confirmed_candidate="candidate-1")
        del document["confirmation_row_ids"]
        self.assertEqual(ledger.replay(document)["terminal_state"], "blocked(confirmation_rows_missing)")

    def test_duplicate_rows_and_nonboolean_search_reuse_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "must be unique"):
            ledger.replay(book([round_entry(1, -0.05, ["r1", "r1"])]))
        document = book([round_entry(1, -0.05, ["r1"])],
                        frozen_finalists=["candidate-1"], confirmed_candidate="candidate-1",
                        confirmation_row_ids=["held-out-1", "held-out-1"])
        with self.assertRaisesRegex(ValueError, "must be unique"):
            ledger.replay(document)
        document = book([])
        document["config"]["search_reuse"] = "false"
        with self.assertRaisesRegex(ValueError, "must be a boolean"):
            ledger.replay(document)

    def test_a_failed_probe_is_a_hard_gate(self):
        result = ledger.replay(book([round_entry(1, -0.05, ["r1"],
                                                 probes={"nota_pair": "pass", "recall_floor": "fail"})]))
        self.assertEqual(result["terminal_state"], "blocked(ledger_gate_failed)")
        self.assertEqual(result["blocked_by"][0]["detail"]["probes"], ["recall_floor"])

    def test_a_probe_that_did_not_run_is_not_a_probe_that_passed(self):
        result = ledger.replay(book([round_entry(1, -0.05, ["r1"], probes={"recall_floor": "not_run"})]))
        self.assertEqual(result["terminal_state"], "blocked(ledger_gate_failed)")
        self.assertEqual(result["blocked_by"][0]["gate"], "probe_not_run")

    def test_rounds_are_bounded_by_the_config(self):
        rounds = [round_entry(index, -0.01, [f"r{index}"]) for index in range(1, 5)]
        result = ledger.replay(book(rounds))
        self.assertEqual(result["terminal_state"], "blocked(ledger_gate_failed)")
        self.assertEqual(result["blocked_by"][0]["gate"], "round_bound_exceeded")

    def test_the_ledger_must_be_append_only_and_in_order(self):
        with self.assertRaisesRegex(ValueError, "append-only and in order"):
            ledger.replay(book([round_entry(1, -0.01, ["r1"]), round_entry(3, -0.02, ["r2"])]))

    def test_exceeding_a_metered_budget_pauses_rather_than_promotes(self):
        document = book([round_entry(1, -0.05, ["r1"], spend=7.5),
                         round_entry(2, -0.06, ["r2"], spend=7.5)],
                        frozen_finalists=["candidate-2"], confirmed_candidate="candidate-2")
        document["config"]["budget"] = 10
        result = ledger.replay(document)
        self.assertEqual(result["terminal_state"], "paused_budget")
        self.assertEqual(result["spend"], 15.0)

    def test_identification_and_sampling_stop_a_confirmed_promotion(self):
        base = book([round_entry(1, -0.05, ["r1"])],
                    frozen_finalists=["candidate-1"], confirmed_candidate="candidate-1")
        no_identification = copy.deepcopy(base)
        no_identification["identification_holds"] = False
        self.assertEqual(ledger.replay(no_identification)["terminal_state"],
                         "insufficient_causal_evidence")
        bad_sample = copy.deepcopy(base)
        bad_sample["confirmation_sampling_design"] = "convenience"
        self.assertEqual(ledger.replay(bad_sample)["terminal_state"], "unsupported_sampling_design")

    def test_g0_can_end_the_run_before_any_round(self):
        result = ledger.replay({"schema_version": 1,
                                "dont_train_reason": "an exact rule decides the family"})
        self.assertEqual(result["terminal_state"], "dont_train(an exact rule decides the family)")
        self.assertEqual(result["rounds_replayed"], 0)

    def test_one_question_is_asked_once(self):
        result = ledger.replay(book([round_entry(1, -0.05, ["r1"])],
                                    needs_human="is a misroute really 3x an abstention here?"))
        self.assertTrue(result["terminal_state"].startswith("needs_human("))

    def test_a_gate_failure_outranks_a_budget_pause_and_a_promotion(self):
        document = book([round_entry(1, -0.05, ["r1"], spend=99, evaluator_hash="moved")],
                        frozen_finalists=["candidate-1"], confirmed_candidate="candidate-1")
        document["config"]["budget"] = 1
        self.assertEqual(ledger.replay(document)["terminal_state"], "blocked(ledger_gate_failed)")

    def test_cli_exits_zero_only_on_a_decided_outcome(self):
        cases = {
            "promoted_candidate": (book([round_entry(1, -0.05, ["r1"])],
                                        frozen_finalists=["candidate-1"],
                                        confirmed_candidate="candidate-1"), 0),
            "incumbent_retained": (book([round_entry(1, +0.05, ["r1"])]), 0),
            "insufficient_evidence": (book([round_entry(1, -0.05, ["r1"])]), 1),
            "blocked(ledger_gate_failed)": (book([round_entry(1, -0.05, ["r1"],
                                                              evaluator_hash="moved")]), 1),
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.json"
            for state, (document, expected) in cases.items():
                with self.subTest(state=state):
                    path.write_text(json.dumps(document), encoding="utf-8")
                    run = subprocess.run([sys.executable, str(SCRIPT), str(path)],
                                         capture_output=True, text=True)
                    self.assertEqual(run.returncode, expected, run.stderr)
                    self.assertEqual(json.loads(run.stdout)["terminal_state"], state)
            path.write_text("{not json", encoding="utf-8")
            broken = subprocess.run([sys.executable, str(SCRIPT), str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(broken.returncode, 2)
            self.assertNotIn("Traceback", broken.stderr)


if __name__ == "__main__":
    unittest.main()
