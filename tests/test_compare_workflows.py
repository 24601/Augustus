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
        "sampling_design": "equal_probability",
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
        self.assertEqual(result["assessment"], "adjudicated_candidate_constraint_violation")

    def test_constraint_assessment_retains_each_evidence_kind(self):
        for kind in ("fixture", "proxy", "observed", "adjudicated"):
            data = receipt()
            data["evidence_kind"] = kind
            data["pairs"][0]["candidate"]["violations"] = ["test violation"]
            with self.subTest(kind=kind):
                result = compare.compare(data)
                self.assertEqual(result["evidence_kind"], kind)
                self.assertEqual(result["assessment"], f"{kind}_candidate_constraint_violation")

    def test_exclusions_are_explicit_unknown_or_caller_declared_not_adjustments(self):
        data = receipt()
        unknown = compare.compare(data)
        self.assertIsNone(unknown["excluded_units"])
        self.assertIsNone(unknown["missing_outcome_policy"])
        for excluded in (0, 3):
            data.update(excluded_units=excluded, missing_outcome_policy="Prespecified complete-case analysis; attrition sensitivity required separately.")
            result = compare.compare(data)
            self.assertEqual(result["excluded_units"], excluded)
            self.assertEqual(result["missing_outcome_policy"], data["missing_outcome_policy"])
            self.assertEqual(result["paired_units"], 4)
            self.assertEqual(result["mean_loss_delta"], unknown["mean_loss_delta"])
            # The arithmetic must not move: a declared exclusion is not an
            # attrition correction. The VERDICT may move, and for a nonzero
            # exclusion it must, which the attrition tests below cover.
            for field in ("upper_mean_loss_delta", "minimum_improvement",
                          "family_alpha", "comparison_count"):
                self.assertEqual(result["confirmation"][field],
                                 unknown["confirmation"][field])
            if excluded == 0:
                self.assertEqual(result["confirmation"], unknown["confirmation"])

    def test_exclusion_metadata_validates_without_coercion(self):
        for field, values in (("excluded_units", (True, False, -1, 0., "3", [])),
                              ("missing_outcome_policy", (False, 0, "", " ", []))):
            for value in values:
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    compare.compare(dict(receipt(), **{field: value}))

    def test_strict_margin_cannot_claim_support_at_reported_equality(self):
        data = receipt(16)
        data.update(loss_bound=.7, minimum_improvement=.1649435713375823)
        for pair in data["pairs"]:
            pair["incumbent"]["loss"] = .7
            pair["candidate"]["loss"] = .10670073329327479
        result = compare.compare(data)["confirmation"]
        self.assertGreaterEqual(result["upper_mean_loss_delta"], -data["minimum_improvement"])
        self.assertFalse(result["strict_margin_supported"])

    def test_confirmation_upper_rounds_outward_and_flag_matches_report(self):
        rng = random.Random(70324)
        for bound in (5e-324, 1e-300, .7, 1., 1e300, sys.float_info.max):
            for _ in range(30):
                data = receipt(rng.randrange(2, 20))
                data["loss_bound"] = bound
                exact_delta = Fraction(0)
                for pair in data["pairs"]:
                    old, new = rng.random()*bound, rng.random()*bound
                    pair["incumbent"]["loss"], pair["candidate"]["loss"] = old, new
                    exact_delta += Fraction(new) - Fraction(old)
                exact_delta /= len(data["pairs"])
                radius = math.sqrt(2 * -math.log(data["alpha"]) / len(data["pairs"]))
                exact_upper = min(Fraction(bound), exact_delta + Fraction(radius)*Fraction(bound))
                result = compare.compare(data)["confirmation"]
                upper = result["upper_mean_loss_delta"]
                self.assertGreaterEqual(Fraction(upper), exact_upper)
                self.assertLessEqual(upper, bound)
                self.assertEqual(result["strict_margin_supported"], upper < 0)
                if upper < 0:
                    data["minimum_improvement"] = -upper
                    self.assertFalse(compare.compare(data)["confirmation"]["strict_margin_supported"])

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


    def test_hoeffding_default_output_is_unchanged_by_the_new_fields(self):
        """The 0.7.2 bound must stay byte-identical when mode/method are absent."""
        data = receipt(100)
        data["pairs"][0]["candidate"]["loss"] = 0.5
        confirmation = compare.compare(data)["confirmation"]
        self.assertEqual(confirmation["method"],
                         "one-sided paired Hoeffding; fixed sample; Bonferroni family")
        self.assertEqual(sorted(confirmation), sorted([
            "method", "family_alpha", "comparison_count", "minimum_improvement",
            "upper_mean_loss_delta", "strict_margin_supported",
        ]))
        explicit = copy.deepcopy(data)
        explicit["mode"] = "superiority"
        explicit["method"] = "hoeffding"
        self.assertEqual(compare.compare(explicit)["confirmation"]["upper_mean_loss_delta"],
                         confirmation["upper_mean_loss_delta"])

    def test_empirical_bernstein_is_tighter_when_the_spread_is_small(self):
        data = receipt(400)
        data["evidence_kind"] = "observed"
        for index, pair in enumerate(data["pairs"]):
            pair["incumbent"]["loss"] = 0.5
            pair["candidate"]["loss"] = 0.5 if index else 0.4
        hoeffding = compare.compare(data)["confirmation"]["upper_mean_loss_delta"]
        data["method"] = "empirical_bernstein"
        bernstein = compare.compare(data)["confirmation"]["upper_mean_loss_delta"]
        self.assertLess(bernstein, hoeffding)

    def test_empirical_bernstein_radius_does_not_collapse_on_identical_arms(self):
        """The rare-large failure: every observed difference is zero, and a
        variance-only interval would certify equivalence at [0, 0]."""
        data = receipt(2000)
        data["evidence_kind"] = "observed"
        data["method"] = "empirical_bernstein"
        data["mode"] = "non_inferiority"
        data["minimum_improvement"] = 0.0005
        for pair in data["pairs"]:
            pair["incumbent"]["loss"] = 0.25
            pair["candidate"]["loss"] = 0.25
        result = compare.compare(data)
        self.assertEqual(result["mean_loss_delta"], 0)
        self.assertGreater(result["confirmation"]["upper_mean_loss_delta"], 0.0005)
        self.assertFalse(result["confirmation"]["strict_margin_supported"])
        self.assertEqual(result["assessment"], "insufficient_evidence")

    def test_non_inferiority_accepts_a_tie_that_superiority_refuses(self):
        data = receipt(4000)
        data["evidence_kind"] = "observed"
        data["method"] = "empirical_bernstein"
        data["minimum_improvement"] = 0.2
        for pair in data["pairs"]:
            pair["incumbent"]["loss"] = 0.3
            pair["candidate"]["loss"] = 0.3
        self.assertFalse(compare.compare(data)["confirmation"]["strict_margin_supported"])
        data["mode"] = "non_inferiority"
        result = compare.compare(data)
        self.assertTrue(result["confirmation"]["strict_margin_supported"])
        self.assertEqual(result["assessment"], "bound_supports_non_inferiority")

    def test_sign_exact_certifies_direction_with_an_exact_p_value(self):
        data = receipt(40)
        data["evidence_kind"] = "observed"
        data["method"] = "sign_exact"
        for index, pair in enumerate(data["pairs"]):
            pair["incumbent"]["loss"] = 1 if index < 20 else 0
            pair["candidate"]["loss"] = 0
        result = compare.compare(data)
        confirmation = result["confirmation"]
        self.assertEqual(confirmation["discordant_pairs"], 20)
        self.assertEqual(confirmation["candidate_wins"], 20)
        self.assertAlmostEqual(confirmation["exact_p_value"], 2 ** -20)
        self.assertIsNone(confirmation["upper_mean_loss_delta"])
        self.assertTrue(confirmation["strict_margin_supported"])

    def test_sign_exact_refuses_a_magnitude_claim_and_non_binary_losses(self):
        data = receipt(10)
        data["method"] = "sign_exact"
        data["minimum_improvement"] = 0.1
        with self.assertRaises(ValueError):
            compare.compare(data)
        data["minimum_improvement"] = 0
        data["pairs"][0]["candidate"]["loss"] = 0.5
        with self.assertRaises(ValueError):
            compare.compare(data)

    def test_sign_exact_without_discordant_pairs_is_not_support(self):
        data = receipt(30)
        data["method"] = "sign_exact"
        for pair in data["pairs"]:
            pair["incumbent"]["loss"] = 0
            pair["candidate"]["loss"] = 0
        confirmation = compare.compare(data)["confirmation"]
        self.assertEqual(confirmation["discordant_pairs"], 0)
        self.assertEqual(confirmation["exact_p_value"], 1.0)
        self.assertFalse(confirmation["strict_margin_supported"])

    def test_confirmation_requires_a_supported_sampling_design(self):
        data = receipt(10)
        del data["sampling_design"]
        with self.assertRaisesRegex(ValueError, "sampling_design"):
            compare.compare(data)
        data["sampling_design"] = "probability_proportional_to_size"
        with self.assertRaisesRegex(ValueError, "unsupported_sampling_design"):
            compare.compare(data)

    def test_search_does_not_require_confirmation_only_fields(self):
        data = receipt(10, "search")
        del data["sampling_design"]
        self.assertIsNone(compare.compare(data)["confirmation"])

    def test_unknown_mode_or_method_is_refused(self):
        for key, value in (("mode", "equivalence"), ("method", "bootstrap")):
            with self.subTest(key=key):
                data = receipt(10)
                data[key] = value
                with self.assertRaisesRegex(ValueError, key):
                    compare.compare(data)


    def test_declared_attrition_blocks_a_confirmation_support_claim(self):
        """The 50/950 case: better on the units that survived, worse overall."""
        data = receipt(60)
        data["evidence_kind"] = "observed"
        for index, pair in enumerate(data["pairs"]):
            pair["incumbent"]["loss"] = 1 if index < 50 else 0
            pair["candidate"]["loss"] = 0 if index < 50 else 1
        without = compare.compare(data)
        self.assertTrue(without["confirmation"]["strict_margin_supported"])
        data["excluded_units"] = 940
        data["missing_outcome_policy"] = "candidate abstained; those units were dropped"
        with_attrition = compare.compare(data)
        self.assertEqual(with_attrition["assessment"], "unsupported_attrition")
        self.assertFalse(with_attrition["confirmation"]["strict_margin_supported"])
        self.assertEqual(with_attrition["confirmation"]["blocked_by_attrition"]["excluded_units"], 940)

    def test_zero_declared_exclusions_is_not_attrition(self):
        data = receipt(100)
        data["evidence_kind"] = "observed"
        data["excluded_units"] = 0
        self.assertTrue(compare.compare(data)["confirmation"]["strict_margin_supported"])

    def test_attrition_does_not_mask_a_weaker_evidence_kind(self):
        data = receipt(60)
        data["excluded_units"] = 10
        self.assertEqual(compare.compare(data)["assessment"], "fixture_evidence_only")

    def test_search_phase_is_unaffected_by_declared_exclusions(self):
        data = receipt(60, "search")
        data["evidence_kind"] = "observed"
        data["excluded_units"] = 940
        self.assertEqual(compare.compare(data)["assessment"], "descriptive_search_only")


if __name__ == "__main__":
    unittest.main()
