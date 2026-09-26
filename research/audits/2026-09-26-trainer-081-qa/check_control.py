"""Post-result adjudication, not part of the frozen acceptance grader.

The service control was incorrectly classified as correct. Independently check
its discovered numerical defect with Decimal, leaving the original unchanged.
"""
from decimal import Decimal, localcontext
import importlib.util
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent


def module(directory, name):
    spec = importlib.util.spec_from_file_location(name, HERE / directory / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


class ControlAdjudication(unittest.TestCase):
    def test_false_control_and_repair_against_decimal(self):
        largest = sys.float_info.max
        for logits, temperature in (([-largest, largest], largest),
                                    ([largest, -largest], largest),
                                    ([largest, largest], largest),
                                    ([1., 2.], 5e-324)):
            with localcontext() as ctx:
                ctx.prec = 100
                peak = Decimal.from_float(max(logits))
                differences = [(Decimal.from_float(x) - peak) /
                               Decimal.from_float(temperature) for x in logits]
                # Values below -1000 round to zero as float probabilities.
                weights = [x.exp() if x > -1000 else Decimal(0) for x in differences]
                expected = [float(x / sum(weights)) for x in weights]
            bundle = dict(levels=[0, 4], threshold=3.8,
                          calibration_required=True, temperature=temperature)
            for name in ('service', 'service_control'):
                result = module('service', name).predict(bundle, logits)
                for got, want in zip(result['probabilities'], expected):
                    self.assertAlmostEqual(got, want, places=14)
                self.assertEqual(result['action'], 'act' if 4 * expected[1] > 3.8 else 'review')
        original = module('fixtures', 'service_control').predict(
            dict(levels=[0, 4], threshold=3.8, calibration_required=True, temperature=largest),
            [-largest, largest])
        self.assertEqual(original['probabilities'], [0., 1.])
        self.assertEqual(original['action'], 'act')


if __name__ == '__main__':
    unittest.main(verbosity=2)
