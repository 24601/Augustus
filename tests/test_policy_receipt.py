"""Regression checks for population mixups and reversed policy explanations."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / '.agents/skills/augustus-train/scripts/policy_receipt.py'
spec = importlib.util.spec_from_file_location('policy_receipt', SCRIPT)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class ReceiptTests(unittest.TestCase):
    def data(self):
        return dict(population=dict(name='current', selection='era=current', ids=['b', 'c', 'd']),
                    rows=[dict(id='a', score=1, y=0), dict(id='b', score=.5, y=1),
                          dict(id='c', score=.375, y=1), dict(id='d', score=.375, y=0)],
                    threshold=.5, shift=.125, cost_fp=1, cost_fn=8)

    def test_population_and_direction_have_independent_expected_counts(self):
        result = m.receipt(self.data())
        self.assertEqual(result['population']['n'], 3)
        self.assertEqual(result['evidence'], 'descriptive')
        # FP, FN, actions: exact boundary is positive; costly missed positives matter.
        expected = [(0, 1, 1), (0, 2, 0), (1, 0, 3), (1, 0, 3), (0, 2, 0)]
        for r, (fp, fn, count) in zip(result['reports'], expected):
            self.assertEqual((r['fp'], r['fn'], r['positive_actions']), (fp, fn, count))
            self.assertEqual(r['mean_loss'], (fp + 8*fn)/3)
            self.assertEqual(r['action_rate'], count/3)
        all_rows = self.data()
        all_rows['population']['ids'].append('a')
        self.assertEqual(m.receipt(all_rows)['reports'][0]['action_rate'], .5)

    def test_hash_binds_selected_values_not_input_order(self):
        data = self.data()
        before = m.receipt(data)['population']['selected_rows_sha256']
        data['rows'].reverse()
        data['population']['ids'].reverse()
        self.assertEqual(before, m.receipt(data)['population']['selected_rows_sha256'])
        data['rows'][0]['y'] = 1
        self.assertNotEqual(before, m.receipt(data)['population']['selected_rows_sha256'])

    def test_malformed_and_missing_population_fail(self):
        for ids in ([], ['b', 'b'], ['absent'], [True]):
            data = self.data()
            data['population']['ids'] = ids
            with self.assertRaises(ValueError): m.receipt(data)
        for value in (True, float('nan'), float('inf')):
            data = self.data()
            data['threshold'] = value
            with self.assertRaises(ValueError): m.receipt(data)

    def test_extreme_arithmetic_stays_finite(self):
        data = self.data()
        data.update(cost_fp=sys.float_info.max, cost_fn=sys.float_info.max,
                    threshold=sys.float_info.max, shift=sys.float_info.max)
        result = m.receipt(data)
        self.assertEqual(result['reports'][1]['mean_loss'], float(m.Fraction(sys.float_info.max)*2/3))

    def test_cli_and_duplicate_keys(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'input.json'
            path.write_text(json.dumps(self.data()))
            run = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertIn('input_sha256', json.loads(run.stdout))
            path.write_text('{"rows":[],"rows":[]}')
            run = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(run.returncode, 2)
            self.assertIn('duplicate JSON key', run.stderr)
