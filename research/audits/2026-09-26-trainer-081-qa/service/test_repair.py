"""Independent contract fixtures; no repository or grader test imports."""
import itertools
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import routing
import routing_control
import service
import service_control


class ApplicationContract(unittest.TestCase):
    def test_calibration_load_and_raw(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'bundle.json'
            for module in (service, service_control):
                for invalid in (None, True, False, 0, -1, '2', [], {}, math.inf, math.nan):
                    with self.subTest(module=module.__name__, invalid=invalid):
                        bundle = dict(levels=[0, 4], threshold=3, calibration_required=True)
                        if invalid is not None:
                            bundle['temperature'] = invalid
                        path.write_text(json.dumps(bundle))
                        with self.assertRaises(ValueError):
                            module.load_bundle(path)
                for flag in (False, None):
                    bundle = dict(levels=[0, 4], threshold=3, temperature=100)
                    if flag is not None:
                        bundle['calibration_required'] = flag
                    path.write_text(json.dumps(bundle))
                    result = module.predict(module.load_bundle(path), [0, math.log(9)])
                    self.assertAlmostEqual(result['expected'], 3.6)
                    self.assertEqual(result['action'], 'act')

    def test_distribution_and_strict_boundary(self):
        for module in (service, service_control):
            bundle = dict(levels=[0, 4], threshold=3.2,
                          calibration_required=True, temperature=2)
            result = module.predict(bundle, [0, math.log(9)])
            self.assertAlmostEqual(result['probabilities'][0], 0.25)
            self.assertAlmostEqual(result['probabilities'][1], 0.75)
            self.assertAlmostEqual(result['expected'], 3)
            self.assertEqual(result['action'], 'review')
            for threshold, action in ((2, 'review'), (1.99, 'act'), (2.01, 'review')):
                self.assertEqual(module.predict(dict(levels=[0, 4], threshold=threshold),
                                                [0, 0])['action'], action)
            result = module.predict(dict(levels=[-2, 1, 8], threshold=3), [0, 0, 0])
            self.assertAlmostEqual(result['expected'], 7 / 3)

    def test_finite_extremes(self):
        # Difference / temperature is -2 exactly in real arithmetic; subtracting
        # opposite float maxima first overflows and silently loses probability.
        largest = sys.float_info.max
        for module in (service, service_control):
            with self.subTest(module=module.__name__):
                result = module.predict(dict(levels=[0, 4], threshold=3.8,
                                             calibration_required=True, temperature=largest),
                                        [-largest, largest])
                self.assertAlmostEqual(result['probabilities'][0], 1 / (1 + math.exp(2)))
                self.assertEqual(result['action'], 'review')
                tiny = module.predict(dict(levels=[0, 4], threshold=3,
                                           calibration_required=True, temperature=5e-324), [1, 2])
                self.assertEqual(tiny['probabilities'], [0, 1])

    def test_threshold_exhaustive(self):
        # Independently enumerate each actual accepted set, rather than prefix
        # accumulation; covers ties, recovery after an unsafe prefix, and no rows.
        for n in range(5):
            for values in itertools.product(((0, 0), (0, 1), (1, 0), (1, 1)), repeat=n):
                rows = [dict(score=score, error=error) for score, error in values]
                for cap in (0, 0.25, 0.5, 1):
                    expected = dict(threshold=None, coverage=0.0, risk=None)
                    for threshold in sorted({row['score'] for row in rows}, reverse=True):
                        accepted = [row for row in rows if row['score'] >= threshold]
                        risk = sum(row['error'] for row in accepted) / len(accepted)
                        if risk <= cap:
                            expected = dict(threshold=threshold, coverage=len(accepted) / n, risk=risk)
                    self.assertEqual(service.choose_threshold(rows, cap), expected, (rows, cap))

    def test_authoritative_routes_and_fallbacks(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'approved.json'
            for module in (routing, routing_control):
                for approved in ({'renewal': 'legal', 'audit': 'compliance'}, {}):
                    path.write_text(json.dumps(approved))
                    routes = module.load_routes(path)
                    self.assertEqual(routes, approved)
                    for kind, target in approved.items():
                        self.assertEqual(module.route(routes, {'notice_type': kind}), target)
                    for notice in (None, [], 3, 'renewal', {}, {'notice_type': []},
                                   {'notice_type': {}}, {'notice_type': False},
                                   {'notice_type': None}, {'notice_type': 'unknown'}):
                        self.assertEqual(module.route(routes, notice), 'operations')

    def test_fresh_process_jsonl(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'bundle.json'
            bundle = dict(levels=[0, 4], threshold=3.2,
                          calibration_required=True, temperature=2)
            path.write_text(json.dumps(bundle))
            for module in (service, service_control):
                command = [sys.executable, str(Path(module.__file__).resolve()), str(path)]
                result = subprocess.run(command, input='{"logits":[0,2.1972245773362196]}\n{"logits":[0,0]}\n',
                                        text=True, capture_output=True, check=True, cwd=directory)
                outputs = [json.loads(line) for line in result.stdout.splitlines()]
                self.assertEqual(len(outputs), 2)
                self.assertAlmostEqual(outputs[0]['expected'], 3)
                self.assertEqual([row['action'] for row in outputs], ['review', 'review'])
                broken = {key: value for key, value in bundle.items() if key != 'temperature'}
                path.write_text(json.dumps(broken))
                failed = subprocess.run(command, input='{"logits":[0,0]}\n', text=True,
                                        capture_output=True, cwd=directory)
                self.assertNotEqual(failed.returncode, 0)
                self.assertEqual(failed.stdout, '')
                path.write_text(json.dumps(bundle))


if __name__ == '__main__':
    unittest.main(verbosity=2)
