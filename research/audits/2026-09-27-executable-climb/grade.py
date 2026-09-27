"""Protected development checker; never delivered to task agents.

Usage: python grade.py data|planning|training path/to/solution.py
"""
from decimal import Decimal, localcontext
from fractions import Fraction
import importlib.util
import json
import math
from pathlib import Path
import random
import shutil
import subprocess
import sys
import tempfile
import unittest

TASK, SOURCE = sys.argv[1], Path(sys.argv[2]).resolve()
spec = importlib.util.spec_from_file_location('submitted_solution', SOURCE)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def cli(payload, *args, cwd=None):
    result = subprocess.run([sys.executable, str(SOURCE), *map(str, args)],
                            input=json.dumps(payload) + '\n', text=True,
                            capture_output=True, cwd=cwd, timeout=10, check=True)
    return json.loads(result.stdout)


def row(ticket, customer, time, text, **kw):
    return dict(ticket=ticket, customer=customer, time=time, text=text,
                role=kw.get('role', 'user'), label=kw.get('label', 'billing'),
                label_time=kw.get('label_time', time),
                label_status=kw.get('label_status', 'agreed'),
                resolution_notes='never a feature', final_queue='leak')


def example(r):
    return {k: r[v] for k, v in [('id', 'ticket'), ('customer', 'customer'),
                                ('text', 'text'), ('label', 'label')]}


class Data(unittest.TestCase):
    def test_transitive_components_and_projection(self):
        rows = [row('a', 'A', '2026-01-01', '  Alpha  '),
                row('b', 'B', '2026-02-01', 'alpha'),
                row('c', 'B', '2026-03-01', 'Beta'),
                row('d', 'D', '2026-03-02', ' beta '),
                row('e', 'A', '2026-01-03', 'same customer, same role'),
                row('f', 'F', '2026-02-02', 'independent dev'),
                row('g', 'G', '2026-03-03', 'independent confirmation')]
        expected = dict(train=[example(rows[0]), example(rows[4])],
                        dev=[example(rows[5])], confirm=[example(rows[6])])
        for seed in range(7):
            shuffled = list(rows)
            random.Random(seed).shuffle(shuffled)
            self.assertEqual(m.prepare(shuffled, '2026-02-01', '2026-03-01'), expected)

    def test_first_event_must_not_be_replaced(self):
        rows = [row('a', 'A', '2026-01-01', '   '),
                row('a', 'A', '2026-01-02', 'later usable'),
                row('b', 'B', '2026-01-01', 'disputed', label_status='disputed'),
                row('b', 'B', '2026-01-02', 'agreed later'),
                row('c', 'C', '2026-01-01', 'staff', role='staff'),
                row('c', 'C', '2026-01-02', 'Z first user'),
                row('c', 'C', '2026-01-02', 'A first user'),
                row('d', 'D', '2026-01-01', 'missing', label=None)]
        self.assertEqual(m.prepare(rows[::-1], '2026-02-01', '2026-03-01'),
                         dict(train=[example(rows[6])], dev=[], confirm=[]))

    def test_label_cutoffs_and_eligible_only_relations(self):
        rows = [row('a', 'A', '2026-01-01', 'repeat', label_time='2026-02-01'),
                row('b', 'B', '2026-02-01', 'repeat'),
                row('c', 'C', '2026-02-28', 'late', label_time='2026-03-01'),
                row('d', 'D', '2026-03-01', 'later', label_time='2027-01-01')]
        expected = dict(train=[], dev=[example(rows[1])], confirm=[example(rows[3])])
        self.assertEqual(m.prepare(rows, '2026-02-01', '2026-03-01'), expected)
        self.assertEqual(cli(dict(rows=rows, train_end='2026-02-01', dev_end='2026-03-01')), expected)


class Planning(unittest.TestCase):
    def test_group_exclusion_feasibility_and_empty_class(self):
        rows = [dict(id=str(i), group=g, label=l) for i, (g, l) in enumerate(
            [('x', 'A'), ('x', 'B'), ('y', 'A'), ('z', 'A'), ('v', 'B')])]
        folds = [['0'], ['1', '4'], []]
        expected = [dict(available={'A': 2, 'B': 1}, sizes=[1]),
                    dict(available={'A': 2, 'B': 0}, sizes=[]),
                    dict(available={'A': 3, 'B': 2}, sizes=[1, 2])]
        args = dict(rows=rows, folds=folds, sizes=[True, False, 0, -1, 1, 2, 2, 3, 1.5])
        self.assertEqual(m.curve(**args), expected)
        self.assertEqual(cli(dict(op='curve', **args)), expected)
        with self.assertRaises(ValueError):
            m.curve(rows, [['unknown']], [1])
        with self.assertRaises(ValueError):
            m.curve(rows + [rows[0]], [], [1])

    def test_cost_selection_against_rational_oracle(self):
        base = [dict(name='constant', n=1000, fn=40, fp=0, latency_ms=0,
                     fit_cost=0, already_paid=False),
                dict(name='fit', n=1000, fn=15, fp=55, latency_ms=2,
                     fit_cost=200, already_paid=False),
                dict(name='zero', n=1000, fn=10, fp=110, latency_ms=5,
                     fit_cost=0, already_paid=False)]
        for paid in (False, True):
            candidates = [dict(c) for c in base]
            candidates[1]['already_paid'] = paid
            for horizon in (0, 5000, 13333, 13334):
                for limit in (0, 2, 5):
                    for fn in (3, 8, 12):
                        feasible = [(Fraction((c['fn']*fn+c['fp'])*horizon, c['n']) +
                                     (0 if c['already_paid'] else c['fit_cost']), c['name'])
                                    for c in candidates if c['latency_ms'] <= limit]
                        cost, name = min(feasible)
                        got = m.select(candidates, horizon, fn, 1, limit)
                        self.assertEqual(set(got), {'name', 'total_cost'})
                        self.assertEqual(got['name'], name)
                        self.assertAlmostEqual(got['total_cost'], float(cost), places=8)
        self.assertIsNone(m.select([], 5, 8, 1, 2))
        self.assertEqual(cli(dict(op='select', candidates=base, horizon=5000,
                                 fn_cost=8, fp_cost=1, max_latency=5)),
                         dict(name='zero', total_cost=950))


class Training(unittest.TestCase):
    def test_updates_against_decimal_reference(self):
        rows = [dict(x=2, target=.2), dict(x=-1, target=.8), dict(x=0, target=.6)]
        with localcontext() as ctx:
            ctx.prec = 50
            w = b = Decimal(0)
            for epochs in range(31):
                got = m.fit(rows, epochs, .1)
                self.assertEqual(set(got), {'w', 'b'})
                self.assertAlmostEqual(got['w'], float(w), places=11)
                self.assertAlmostEqual(got['b'], float(b), places=11)
                residuals = [1/(1+(-(w*r['x']+b)).exp())-Decimal(str(r['target']))
                             for r in rows]
                w, b = (w-Decimal('.1')*sum(e*r['x'] for e, r in zip(residuals, rows))/3,
                        b-Decimal('.1')*sum(residuals)/3)

    def test_soft_target_convergence(self):
        for target in (.17, .39, .81):
            got = m.fit([dict(x=0, target=target)]*3, 700, .5)
            self.assertAlmostEqual(1/(1+math.exp(-got['b'])), target, places=8)
            self.assertEqual(got['w'], 0)

    def test_calibrated_policy_boundaries_and_extremes(self):
        cases = [({'w': 1, 'b': math.log(3)}, 0, 2, 3, 7,
                  math.sqrt(3)/(1+math.sqrt(3)), 'negative'),
                 ({'w': 1, 'b': 0}, 0, 1, 1, 1, .5, 'negative'),
                 ({'w': 1, 'b': 0}, .01, 1, 1, 1,
                  1/(1+math.exp(-.01)), 'positive'),
                 ({'w': 1, 'b': 0}, -1000, 1, 1, 1, 0, 'negative'),
                 ({'w': 1, 'b': 0}, 1000, 1, 1, 1, 1, 'positive'),
                 ({'w': 1, 'b': 0}, 0, 1, 1e308, 1e308, .5, 'negative')]
        for model, x, temperature, fn, fp, probability, action in cases:
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory)/'artifact.json'
                m.export(path, model, temperature, fn, fp)
                result = m.predict(m.load(path), x)
                self.assertEqual(set(result), {'p', 'action'})
                self.assertTrue(math.isfinite(result['p']))
                self.assertAlmostEqual(result['p'], probability, places=12)
                self.assertEqual(result['action'], action)

    def test_required_policy_and_overwrite_refusal(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'artifact.json'
            m.export(path, {'w': 1, 'b': 0}, 1, 2, 3)
            original = path.read_bytes()
            with self.assertRaises((FileExistsError, ValueError)):
                m.export(path, {'w': 9, 'b': 8}, 1, 2, 3)
            self.assertEqual(path.read_bytes(), original)
            for key in ('temperature', 'fn_cost', 'fp_cost'):
                for value in (None, True, False, '1', 0, -1, float('nan'), float('inf')):
                    data = json.loads(original)
                    if value is None:
                        del data[key]
                    else:
                        data[key] = value
                    path.write_text(json.dumps(data))
                    with self.assertRaises((ValueError, KeyError)):
                        m.load(path)
                    path.unlink()
                    values = dict(temperature=1, fn_cost=2, fp_cost=3)
                    values[key] = value
                    with self.assertRaises(ValueError):
                        m.export(path, {'w': 1, 'b': 0}, **values)
                    self.assertFalse(path.exists())

    def test_real_fit_cli_and_fresh_process_inference(self):
        with tempfile.TemporaryDirectory() as directory:
            cwd = Path(directory)
            shutil.copyfile(SOURCE, cwd/'solution.py')
            training = cwd/'train.json'
            training.write_text(json.dumps(dict(rows=[dict(x=0, target=.37)],
                                                epochs=700, lr=.5, temperature=1,
                                                fn_cost=4, fp_cost=1)))
            subprocess.run([sys.executable, 'solution.py', 'fit', 'train.json', 'model.json'],
                           cwd=cwd, capture_output=True, text=True, check=True, timeout=10)
            training.unlink()
            result = subprocess.run([sys.executable, 'solution.py', 'predict', 'model.json'],
                                    cwd=cwd, input='{"x":0}\n{"x":100}\n',
                                    capture_output=True, text=True, check=True, timeout=10)
            outputs = [json.loads(line) for line in result.stdout.splitlines()]
            self.assertEqual(len(outputs), 2)
            for output in outputs:
                self.assertAlmostEqual(output['p'], .37, places=8)
                self.assertEqual(output['action'], 'positive')


suite = unittest.defaultTestLoader.loadTestsFromTestCase(
    {'data': Data, 'planning': Planning, 'training': Training}[TASK])
result = unittest.TextTestRunner(verbosity=2).run(suite)
print(json.dumps(dict(task=TASK, tests=result.testsRun,
                      failures=len(result.failures), errors=len(result.errors),
                      passed=result.wasSuccessful())))
sys.exit(0 if result.wasSuccessful() else 1)
