import copy
from fractions import Fraction
import importlib.util
import json
import math
from pathlib import Path
import random
import struct
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / ".agents/skills/augustus/scripts/compare_workflows.py"
SPEC = importlib.util.spec_from_file_location("compare_workflows", SCRIPT)
compare = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(compare)


def receipt(n=4, phase="confirm"):
    return {
        "schema_version": 1, "phase": phase,
        "incumbent_id": "baseline-v1", "candidate_id": "candidate-v2",
        "dataset_id": "synthetic-test-fixture", "outcome_definition": "bounded task loss",
        "sampling_unit": "one independent episode (assumption, not attested)",
        "evidence_kind": "fixture", "loss_bound": 1,
        "alpha": 0.05, "minimum_improvement": 0, "comparison_count": 1,
        "pairs": [{
            "id": str(i),
            "incumbent": {"loss": 1, "cost": 2, "latency_ms": 3, "violations": []},
            "candidate": {"loss": 0, "cost": 1, "latency_ms": 4, "violations": []},
        } for i in range(n)],
    }


class WorkflowComparisonTests(unittest.TestCase):
    def test_paired_arithmetic_and_fixed_sample_bound(self):
        data = receipt(100)
        data["pairs"][0]["candidate"]["loss"] = 0.5
        result = compare.compare(data)
        self.assertEqual(result["paired_units"], 100)
        self.assertAlmostEqual(result["mean_loss_delta"], -0.995)
        expected = -0.995 + math.sqrt(2 * math.log(20) / 100)
        self.assertAlmostEqual(result["confirmation"]["upper_mean_loss_delta"], expected)
        self.assertTrue(result["confirmation"]["strict_margin_supported"])
        self.assertEqual(result["candidate"]["mean_latency_ms"], 4)
        self.assertEqual(result["assessment"], "fixture_evidence_only")

    def test_search_has_no_confirmation_despite_apparent_win(self):
        data = receipt(100, "search")
        data["evidence_kind"] = "adjudicated"
        result = compare.compare(data)
        self.assertIsNone(result["confirmation"])
        self.assertEqual(result["assessment"], "descriptive_search_only")

    def test_small_confirmation_is_inconclusive_and_family_penalty_matters(self):
        data = receipt(4)
        data["evidence_kind"] = "observed"
        self.assertEqual(compare.compare(data)["assessment"], "insufficient_evidence")
        data = receipt(100)
        single = compare.compare(data)["confirmation"]["upper_mean_loss_delta"]
        data["comparison_count"] = 100
        multiple = compare.compare(data)["confirmation"]["upper_mean_loss_delta"]
        self.assertGreater(multiple, single)

    def test_constraint_violation_overrides_better_loss(self):
        data = receipt(100)
        data["evidence_kind"] = "adjudicated"
        data["pairs"][4]["candidate"]["violations"] = ["permission check failed"]
        result = compare.compare(data)
        self.assertTrue(result["confirmation"]["strict_margin_supported"])
        self.assertEqual(result["candidate"]["units_with_violations"], 1)
        self.assertEqual(result["assessment"], "observed_candidate_constraint_violation")

    def test_unknown_cost_is_not_zero_or_known_only_average(self):
        data = receipt()
        data["pairs"][0]["candidate"]["cost"] = None
        result = compare.compare(data)
        self.assertIsNone(result["candidate"]["mean_cost"])
        self.assertEqual(result["candidate"]["known_cost_units"], 3)
        self.assertEqual(result["incumbent"]["mean_cost"], 2)

    def test_duplicate_units_missing_pairs_and_schema_are_rejected(self):
        data = receipt()
        data["pairs"][1]["id"] = "0"
        with self.assertRaisesRegex(ValueError, "duplicate pair"):
            compare.compare(data)
        for mutation in (
            {"schema_version": True}, {"schema_version": 1.0}, {"phase": "deploy"},
            {"pairs": []}, {"candidate_id": "baseline-v1"}, {"evidence_kind": "verified"},
            {"comparison_count": True}, {"comparison_count": 0}, {"sampling_unit": " "},
        ):
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                compare.compare(dict(receipt(), **mutation))
        data = receipt()
        del data["pairs"][0]["candidate"]
        with self.assertRaises(ValueError):
            compare.compare(data)

    def test_invalid_and_out_of_bound_numbers_are_rejected(self):
        for value in (True, -1, 1.1, float("nan"), float("inf"), 10**400):
            data = receipt()
            data["pairs"][0]["candidate"]["loss"] = value
            with self.subTest(value_type=type(value)), self.assertRaises(ValueError):
                compare.compare(data)
        for field, value in (("alpha", 0), ("alpha", 1), ("loss_bound", 0),
                             ("minimum_improvement", -1), ("minimum_improvement", 2)):
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                compare.compare(dict(receipt(), **{field: value}))

    def test_explicit_unknown_and_typed_violation_list_required(self):
        data = receipt()
        del data["pairs"][0]["candidate"]["cost"]
        with self.assertRaisesRegex(ValueError, "use null"):
            compare.compare(data)
        for value in (None, False, [""], [False]):
            data = receipt()
            data["pairs"][0]["candidate"]["violations"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                compare.compare(data)

    def test_proxy_does_not_become_outcome_evidence(self):
        data = receipt(100)
        data["evidence_kind"] = "proxy"
        result = compare.compare(data)
        self.assertTrue(result["confirmation"]["strict_margin_supported"])
        self.assertEqual(result["assessment"], "proxy_evidence_only")

    def test_extreme_finite_losses_costs_and_alpha_stay_finite(self):
        data = receipt(100)
        data["loss_bound"] = 1e308
        data["alpha"] = 5e-324
        for pair in data["pairs"]:
            pair["incumbent"]["loss"] = 1e308
            pair["candidate"]["cost"] = 1e308
        result = compare.compare(data)
        self.assertEqual(result["candidate"]["mean_cost"], 1e308)
        self.assertTrue(math.isfinite(result["confirmation"]["upper_mean_loss_delta"]))
        json.dumps(result, allow_nan=False)

    def test_exact_mean_preserves_constant_extremes_and_subnormal_values(self):
        for value in (sys.float_info.max, 1e308, 1e-308, 1e-323, 5e-324):
            for n in (2, 3, 7, 1000):
                data = receipt(n, "search")
                data["loss_bound"] = value
                for pair in data["pairs"]:
                    for arm in ("incumbent", "candidate"):
                        for metric in ("loss", "cost", "latency_ms"):
                            pair[arm][metric] = value
                with self.subTest(value=value, n=n):
                    result = compare.compare(data)
                    for arm in ("incumbent", "candidate"):
                        for metric in ("mean_loss", "mean_cost", "mean_latency_ms"):
                            self.assertEqual(result[arm][metric], value)
                    self.assertEqual(result["mean_loss_delta"], 0)
                    json.dumps(result, allow_nan=False)

    def test_mean_matches_exact_ratio_oracle_across_magnitudes_and_signs(self):
        samples = (
            [sys.float_info.max, sys.float_info.max, 0.0],
            [5e-324, 1e-323, 1.5e-323],
            [-1.0, 1.0, 5e-324],
            [1.0, -0.5, 1e-20, 0.0],
        )
        for values in samples:
            expected = float(sum(Fraction(value) for value in values) / len(values))
            with self.subTest(values=values):
                self.assertEqual(compare._mean(values), expected)
                self.assertEqual(compare._mean(list(reversed(values))), expected)

    def test_random_finite_means_match_exact_oracle_and_stay_within_range(self):
        rng = random.Random(70322)
        for _ in range(512):
            values = []
            size = rng.randrange(1, 20)
            while len(values) < size:
                value = struct.unpack(">d", rng.getrandbits(64).to_bytes(8, "big"))[0]
                if math.isfinite(value):
                    values.append(value)
            expected = float(sum(map(Fraction, values)) / len(values))
            actual = compare._mean(values)
            self.assertEqual(actual, expected)
            self.assertTrue(min(values) <= actual <= max(values))
            self.assertEqual(compare._mean(list(reversed(values))), actual)

    def test_paired_delta_survives_normalization_and_cancellation_extremes(self):
        for bound, losses, expected in (
            (sys.float_info.max, [(0., 1e-20)], 1e-20),
            (2., [(0., 5e-324)], 5e-324),
            (sys.float_info.max, [(0., 1.), (1., 1e-20)], 5e-21),
        ):
            data = receipt(len(losses), "search")
            data["loss_bound"] = bound
            for pair, (old, new) in zip(data["pairs"], losses):
                pair["incumbent"]["loss"] = old
                pair["candidate"]["loss"] = new
            with self.subTest(bound=bound, losses=losses):
                self.assertEqual(compare.compare(data)["mean_loss_delta"], expected)
                for pair in data["pairs"]:
                    pair["incumbent"], pair["candidate"] = pair["candidate"], pair["incumbent"]
                self.assertEqual(compare.compare(data)["mean_loss_delta"], -expected)

    def test_random_paired_deltas_match_exact_rational_oracle(self):
        rng = random.Random(70323)
        for _ in range(300):
            data = receipt(rng.randrange(1, 9), "search")
            data["loss_bound"] = sys.float_info.max
            expected = Fraction(0)
            for pair in data["pairs"]:
                for arm in ("incumbent", "candidate"):
                    while True:
                        value = struct.unpack(">d", rng.getrandbits(63).to_bytes(8, "big"))[0]
                        if math.isfinite(value):
                            pair[arm]["loss"] = value
                            break
                expected += Fraction(pair["candidate"]["loss"]) - Fraction(pair["incumbent"]["loss"])
            expected = float(expected / len(data["pairs"]))
            actual = compare.compare(data)["mean_loss_delta"]
            self.assertEqual(actual, expected)
            data["pairs"].reverse()
            self.assertEqual(compare.compare(data)["mean_loss_delta"], actual)

    def test_fixed_sample_two_point_null_respects_declared_error_budget(self):
        # Independent fair +/-1 deltas have true mean zero. Enumerate the
        # exact binomial rejection probability, not Monte Carlo or real data.
        for n in (1, 2, 3, 5, 10, 20, 40, 80):
            for family in (1, 3, 10):
                error = Fraction(0)
                for wins in range(n + 1):
                    data = receipt(n)
                    data["evidence_kind"] = "observed"
                    data["comparison_count"] = family
                    for pair in data["pairs"][wins:]:
                        pair["incumbent"]["loss"] = 0
                        pair["candidate"]["loss"] = 1
                    result = compare.compare(data)
                    if result["confirmation"]["strict_margin_supported"]:
                        error += Fraction(math.comb(n, wins), 2**n)
                with self.subTest(n=n, family=family):
                    self.assertLessEqual(error, Fraction(1, 20*family))

    def test_schema_mutations_fail_normally_or_produce_serializable_results(self):
        values = (None, True, False, -1, 0, 1, 1.5, "", "bad", [], {},
                  ["bad"], {"bad": 1}, float("nan"), float("inf"))
        paths = [(key,) for key in receipt()]
        paths += [("pairs", 0, key) for key in ("id", "incumbent", "candidate")]
        paths += [("pairs", 0, arm, key) for arm in ("incumbent", "candidate")
                  for key in ("loss", "cost", "latency_ms", "violations")]
        for path in paths:
            for value in values:
                data = receipt()
                target = data
                for key in path[:-1]:
                    target = target[key]
                target[path[-1]] = value
                with self.subTest(path=path, value=value):
                    try:
                        result = compare.compare(data)
                    except ValueError:
                        continue
                    # Valid mutations may pass; all other exception types
                    # escape and fail the test. Successful outputs stay JSON.
                    json.dumps(result, allow_nan=False)

    def test_input_is_not_mutated_and_pair_order_does_not_change_metrics(self):
        data = receipt(5)
        data["pairs"][0]["candidate"]["loss"] = 0.75
        original = copy.deepcopy(data)
        result = compare.compare(data)
        self.assertEqual(data, original)
        data["pairs"].reverse()
        self.assertEqual(compare.compare(data), result)

    def test_cli_runs_standalone_and_hashes_exact_input(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "paired.json"
            path.write_text(json.dumps(receipt()), encoding="utf-8")
            run = subprocess.run([sys.executable, "-I", str(SCRIPT), str(path)],
                                 cwd=directory, text=True, capture_output=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            result = json.loads(run.stdout)
            self.assertEqual(result["paired_units"], 4)
            self.assertEqual(result["input_sha256"], compare.hashlib.sha256(path.read_bytes()).hexdigest())
            self.assertEqual(path.read_text(), json.dumps(receipt()))

    def test_cli_malformed_json_duplicates_utf8_and_io_are_normal_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            for body in (b'{"schema_version":1,"schema_version":1}', b'{', b'\xff'):
                path.write_bytes(body)
                run = subprocess.run([sys.executable, "-I", str(SCRIPT), str(path)],
                                     text=True, capture_output=True)
                self.assertEqual(run.returncode, 2)
                self.assertNotIn("Traceback", run.stderr)
                self.assertEqual(run.stdout, "")
            run = subprocess.run([sys.executable, "-I", str(SCRIPT), directory],
                                 text=True, capture_output=True)
            self.assertEqual(run.returncode, 2)
            self.assertNotIn("Traceback", run.stderr)

    def test_decoder_exhaustion_is_reported(self):
        with patch.object(Path, "read_bytes", return_value=b"{}"), \
             patch.object(compare.json, "loads", side_effect=RecursionError("deep")), \
             patch.object(sys, "stderr"):
            with self.assertRaises(SystemExit) as raised:
                compare.main(["unused.json"])
        self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
