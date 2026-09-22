from fractions import Fraction
import importlib.util
import json
import math
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents/skills/augustus/scripts/evaluate_decisions.py"
SPEC = importlib.util.spec_from_file_location("evaluate_decisions", SCRIPT)
evaluate = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(evaluate)


class EvaluateDecisionsTests(unittest.TestCase):
    def jsonl(self, rows):
        handle = tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False)
        self.addCleanup(lambda: Path(handle.name).unlink(missing_ok=True))
        for row in rows:
            handle.write(json.dumps(row) + "\n")
        handle.close()
        return handle.name

    def binary_jsonl(self, content):
        handle = tempfile.NamedTemporaryFile(suffix=".jsonl", delete=False)
        self.addCleanup(lambda: Path(handle.name).unlink(missing_ok=True))
        handle.write(content)
        handle.close()
        return handle.name

    def test_load_rejects_bool_nan_and_duplicate_ids(self):
        for row in (
            {"id": "a", "p": True, "y": 1},
            {"id": "a", "p": float("nan"), "y": 1},
            {"id": "a", "p": 0.5, "y": True},
            {"id": "a", "p": 0.5, "y": 1, "p_base": float("nan")},
        ):
            with self.subTest(row=row):
                with self.assertRaises(ValueError):
                    evaluate.load(self.jsonl([row]))
        with self.assertRaisesRegex(ValueError, "duplicate id"):
            evaluate.load(self.jsonl([
                {"id": "same", "p": 0.1, "y": 0},
                {"id": "same", "p": 0.9, "y": 1},
            ]))

    def test_complete_binary_metrics_use_action_rate_not_selective_coverage(self):
        rows = [
            {"id": "tn", "p": 0.1, "y": 0},
            {"id": "fn", "p": 0.2, "y": 1},
            {"id": "tp", "p": 0.8, "y": 1},
            {"id": "fp", "p": 0.9, "y": 0},
        ]
        result = evaluate.sweep(rows, [0.8], cost_fp=2, cost_fn=3)[0]
        self.assertEqual(result["action_rate"], 0.5)
        self.assertEqual(result["coverage"], result["action_rate"])
        self.assertEqual((result["fp"], result["fn"]), (1, 1))
        self.assertEqual(result["cost"], 1.25)
        self.assertAlmostEqual(evaluate.brier(rows), 0.375)

    def test_ambiguous_json_and_oversized_numbers_are_input_errors(self):
        for content in (
            b'{"id":"a","p":0.01,"p":0.99,"y":0}\n',
            ('{"id":"a","p":' + '1' * 401 + ',"y":0}\n').encode(),
        ):
            with self.subTest(prefix=content[:50]):
                path = self.binary_jsonl(content)
                run = subprocess.run([sys.executable, str(SCRIPT), path],
                                     text=True, capture_output=True)
                self.assertEqual(run.returncode, 2)
                self.assertIn("line 1:", run.stderr)
                self.assertNotIn("Traceback", run.stderr)
                self.assertEqual(run.stdout, "")

    def test_json_nesting_exhaustion_is_a_normal_input_error(self):
        # Decoder recursion limits differ by Python version. Exercise the
        # failure contract without demanding rejection of valid deep JSON.
        path = self.jsonl([{"id": "a", "p": 0.5, "y": 0}])
        with patch.object(evaluate.json, "loads", side_effect=RecursionError("too deep")):
            with self.assertRaisesRegex(ValueError, "line 1: invalid JSON"):
                evaluate.load(path)

    def test_large_finite_costs_do_not_overflow_before_averaging(self):
        rows = [{"id": str(i), "p": 0.9, "y": 0} for i in range(2)]
        self.assertEqual(evaluate.sweep(rows, [0.5], 1e308, 1)[0]["cost"], 1e308)
        self.assertEqual(evaluate.selective_policy(rows, 0.2, 0.8, 1e308, 1, 1)["cost"], 1e308)
        rows = [{"id": str(i), "p": 0.5, "y": 0} for i in range(2)]
        self.assertEqual(evaluate.selective_policy(rows, 0.2, 0.8, 1, 1, 1e308)["cost"], 1e308)

    def test_selective_cost_preserves_maximum_and_subnormal_constant_means(self):
        rows = [
            {"p": .9, "y": 0},
            {"p": .1, "y": 1}, {"p": .1, "y": 1},
            {"p": .5, "y": 0}, {"p": .5, "y": 0},
        ]
        for value in (sys.float_info.max, 1e-323, 5e-324):
            with self.subTest(value=value):
                result = evaluate.selective_policy(rows, .2, .8, value, value, value)
                self.assertEqual((result["fp"], result["fn"], result["abstentions"]), (1, 2, 2))
                self.assertEqual(result["cost"], value)
                self.assertEqual(evaluate._complete_cost(1, 1, 2, value, value), value)

    def test_weighted_cost_matches_exact_oracle_for_mixed_magnitudes(self):
        for costs in ((sys.float_info.max, 1e308, 0.0), (5e-324, 1e-323, 1.5e-323)):
            for fp in range(6):
                for fn in range(6-fp):
                    counts = (fp, fn, 5-fp-fn)
                    expected = float(sum(Fraction(c)*n for c, n in zip(costs, counts)) / 5)
                    self.assertEqual(evaluate._weighted_cost(5, *zip(costs, counts)), expected)

    def test_negative_class_log_loss_does_not_cancel_small_probabilities(self):
        for p in (5e-324, 1e-20, 1e-17, 1e-10, .5):
            expected = -math.log1p(-p)
            with self.subTest(p=p):
                self.assertGreater(expected, 0)
                self.assertEqual(evaluate.log_loss([{"p": p, "y": 0}]*3), expected)
        self.assertEqual(evaluate.log_loss([{"p": 1.0, "y": 0}]), math.inf)
        self.assertEqual(evaluate.log_loss([{"p": 0.0, "y": 0}]), 0)

    def test_selective_policy_boundary_and_cost_arithmetic(self):
        rows = [
            {"id": "lower", "p": 0.2, "y": 1},
            {"id": "middle", "p": 0.5, "y": 0},
            {"id": "upper", "p": 0.8, "y": 0},
        ]
        result = evaluate.selective_policy(rows, 0.2, 0.8, 2, 3, 0.5)
        self.assertEqual((result["fp"], result["fn"], result["abstentions"]), (1, 1, 1))
        self.assertEqual(result["decided_coverage"], 2 / 3)
        self.assertEqual(result["selective_error"], 1.0)
        self.assertEqual(result["cost"], 5.5 / 3)
        self.assertIn("p <= lower", result["tie_policy"])

    def test_all_abstain_has_no_selective_error(self):
        rows = [
            {"id": "one", "p": 0.2, "y": 0},
            {"id": "two", "p": 0.8, "y": 1},
        ]
        result = evaluate.selective_policy(rows, 0.0, 1.0)
        self.assertEqual(result["decided_coverage"], 0.0)
        self.assertEqual(result["abstention_rate"], 1.0)
        self.assertIsNone(result["selective_error"])
        self.assertIsNone(result["cost"])

    def test_costs_are_explicit_and_zero_action_is_considered(self):
        rows = [{"id": "one", "p": 1.0, "y": 0}]
        self.assertIsNone(evaluate.sweep(rows, [0.5])[0]["cost"])
        with self.assertRaisesRegex(ValueError, "supplied together"):
            evaluate.sweep(rows, [0.5], cost_fp=1)
        with self.assertRaisesRegex(ValueError, "cost-abstain"):
            evaluate.selective_policy(rows, 0.2, 0.8, cost_fp=1, cost_fn=1)
        best = evaluate.cost_optimal_threshold(rows, cost_fp=1, cost_fn=1)
        self.assertEqual(best["policy"], "always_negative")
        self.assertIsNone(best["threshold"])
        self.assertEqual(best["cost"], 0.0)

    def test_selective_thresholds_require_a_nonempty_abstention_band(self):
        rows = [{"id": "one", "p": 0.5, "y": 1}]
        with self.assertRaisesRegex(ValueError, "lower-threshold < upper-threshold"):
            evaluate.selective_policy(rows, 0.5, 0.5)

    def test_quantile_ties_and_reliability_labels_are_order_safe(self):
        grouped = [{"id": str(i), "p": 0.5, "y": y}
                   for i, y in enumerate([0, 0, 1, 1])]
        interleaved = [grouped[i] for i in (0, 2, 1, 3)]
        self.assertEqual(evaluate.ece_quantile(grouped, bins=2), 0.0)
        self.assertEqual(
            evaluate.ece_quantile(grouped, bins=2),
            evaluate.ece_quantile(interleaved, bins=2),
        )
        labels = evaluate.reliability([
            {"id": "a", "p": 0.0, "y": 0},
            {"id": "b", "p": 1.0, "y": 1},
        ], bins=3)
        self.assertEqual(labels[0]["bin"], "[0,0.333333333333)")
        self.assertEqual(labels[-1]["bin"], "[0.666666666667,1]")

    def test_auc_handles_ties_in_n_log_n_path_and_one_class_is_undefined(self):
        rows = [
            {"id": "negative-low", "p": 0.1, "y": 0},
            {"id": "negative-tie", "p": 0.5, "y": 0},
            {"id": "positive-tie", "p": 0.5, "y": 1},
            {"id": "positive-high", "p": 0.9, "y": 1},
        ]
        self.assertEqual(evaluate.pairwise_ranking_auc(rows), 0.875)
        self.assertIsNone(evaluate.pairwise_ranking_auc([
            {"id": "only", "p": 0.5, "y": 1},
        ]))

    def test_log_loss_reports_infinity_for_an_impossible_observed_outcome(self):
        self.assertEqual(evaluate.log_loss([
            {"id": "wrong-certainty", "p": 0.0, "y": 1},
        ]), float("inf"))
        self.assertEqual(evaluate.log_loss([
            {"id": "right-certainty", "p": 1.0, "y": 1},
        ]), 0.0)

    def test_cli_prints_selective_metrics_only_when_opted_in(self):
        path = self.jsonl([
            {"id": "one", "p": 0.2, "y": 0},
            {"id": "two", "p": 0.8, "y": 1},
        ])
        run = subprocess.run(
            [sys.executable, str(SCRIPT), path, "--lower-threshold", "0.2",
             "--upper-threshold", "0.8", "--cost-fp", "2", "--cost-fn", "3",
             "--cost-abstain", "0.5"],
            text=True, capture_output=True, check=True,
        )
        self.assertIn("action_rate=", run.stdout)
        self.assertIn("selective lower=0.2 upper=0.8", run.stdout)
        self.assertIn("decided_coverage=1.000", run.stdout)
        self.assertIn("IN_SAMPLE_CALIBRATION_ONLY", run.stdout)

    def test_cli_rejects_invalid_metrics_arguments_before_reporting(self):
        path = self.jsonl([{"id": "one", "p": 0.5, "y": 1}])
        run = subprocess.run(
            [sys.executable, str(SCRIPT), path, "--thresholds", "1.2"],
            text=True, capture_output=True,
        )
        self.assertEqual(run.returncode, 2)
        self.assertIn("threshold must be in [0,1]", run.stderr)
        self.assertNotIn("n=", run.stdout)

    def test_cli_reports_invalid_utf8_as_an_argument_error(self):
        path = self.binary_jsonl(b'{"id":"one","p":0.5,"y":1}\n\xff')
        run = subprocess.run(
            [sys.executable, str(SCRIPT), path], text=True, capture_output=True,
        )
        self.assertEqual(run.returncode, 2)
        self.assertIn("cannot read UTF-8 JSONL", run.stderr)
        self.assertNotIn("Traceback", run.stderr)
        self.assertEqual(run.stdout, "")


if __name__ == "__main__":
    unittest.main()
