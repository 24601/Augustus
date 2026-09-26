"""Coordinator-owned acceptance: python grade.py fixtures|solutions.

This grader was not transferred to the repair-agent workspaces. It uses the
application contracts, not agent-generated tests, as its oracle.
"""
import importlib.util
import itertools
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
TARGET = Path(sys.argv.pop(1)).resolve()


def load(name):
    spec = importlib.util.spec_from_file_location(name, TARGET / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Acceptance(unittest.TestCase):
    def test_optimizer_membership_and_actual_updates(self):
        import torch
        m = load('training')
        for tune in (False, True):
            torch.manual_seed(817)
            model = m.DecisionModel()
            optimizer = m.make_optimizer(model, tune, .2)
            expected = {id(p) for p in model.head.parameters()}
            if tune:
                expected |= {id(p) for p in model.encoder.parameters()}
            actual = {id(p) for g in optimizer.param_groups for p in g['params']}
            self.assertEqual(actual, expected)
            before = {n: p.detach().clone() for n, p in model.named_parameters()}
            x = torch.tensor([[.3, -.8], [1.2, .4], [-.5, .7]])
            y = torch.tensor([.2, .8, .4])
            for _ in range(3):
                optimizer.zero_grad()
                loss = m.soft_loss(model(x), y)
                self.assertTrue(torch.isfinite(loss))
                loss.backward()
                optimizer.step()
            moved = {n for n, p in model.named_parameters() if not torch.equal(before[n], p)}
            self.assertTrue(any(n.startswith('head.') for n in moved))
            self.assertEqual(any(n.startswith('encoder.') for n in moved), tune)

    def test_soft_target_objective_gradient_and_fit(self):
        import torch
        m = load('training')
        for q in (.13, .37, .83):
            z = torch.tensor(.4, dtype=torch.float64, requires_grad=True)
            target = torch.tensor(q, dtype=torch.float64)
            loss = m.soft_loss(z, target)
            self.assertAlmostEqual(loss.item(), math.log1p(math.exp(.4)) - q * .4, places=12)
            loss.backward()
            self.assertAlmostEqual(z.grad.item(), 1 / (1 + math.exp(-.4)) - q, places=12)
            z = torch.nn.Parameter(torch.tensor(0., dtype=torch.float64))
            opt = torch.optim.SGD([z], lr=.5)
            for _ in range(500):
                opt.zero_grad()
                m.soft_loss(z, target).backward()
                opt.step()
            self.assertAlmostEqual(z.sigmoid().item(), q, places=8)

    def test_calibration_and_fresh_process_actions(self):
        m = load('service')
        logits = [0., math.log(2), math.log(4)]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'bundle.json'
            for required, expected, action in ((True, [1/21, 4/21, 16/21], 'act'),
                                               (False, [1/7, 2/7, 4/7], 'review')):
                path.write_text(json.dumps(dict(levels=[0, 1, 2], threshold=1.6,
                                                calibration_required=required, temperature=.5)))
                result = m.predict(m.load_bundle(path), logits)
                for got, want in zip(result['probabilities'], expected):
                    self.assertAlmostEqual(got, want, places=12)
                self.assertEqual(result['action'], action)
                self.assertAlmostEqual(result['expected'], sum(i*p for i, p in enumerate(expected)), places=12)
                run = subprocess.run([sys.executable, str(TARGET / 'service.py'), str(path)],
                                     input=json.dumps({'logits': logits})+'\n', text=True,
                                     capture_output=True, cwd=directory, check=True)
                self.assertEqual(json.loads(run.stdout), result)
            # Option/level identity is not the array index.
            path.write_text(json.dumps(dict(levels=[2, 0, 1], threshold=.98,
                                            calibration_required=True, temperature=.5)))
            result = m.predict(m.load_bundle(path), logits)
            self.assertAlmostEqual(result['expected'], 18/21, places=12)
            self.assertEqual(result['action'], 'review')

    def test_required_calibration_refuses_missing_and_invalid(self):
        m = load('service')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'bundle.json'
            for t in (None, True, '0.5', 0, -1, float('nan'), float('inf')):
                bundle = dict(levels=[0, 1, 2], threshold=1.6, calibration_required=True)
                if t is not None:
                    bundle['temperature'] = t
                path.write_text(json.dumps(bundle))
                with self.assertRaises((ValueError, KeyError)):
                    m.load_bundle(path)
            path.write_text(json.dumps(dict(levels=[0, 1, 2], threshold=1.6, calibration_required=True)))
            run = subprocess.run([sys.executable, str(TARGET / 'service.py'), str(path)],
                                 input='{"logits":[0,1,2]}\n', capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertEqual(run.stdout, '')

    def test_attainable_thresholds_against_exhaustive_policy_oracle(self):
        m = load('service')
        cases = [[{'score': .9, 'error': 1}, {'score': .9, 'error': 0},
                  {'score': .8, 'error': 0}, {'score': .8, 'error': 0}],
                 [{'score': .7, 'error': 0}, {'score': .7, 'error': 1}],
                 [{'score': .6, 'error': 1}], []]
        for rows in cases:
            for cap in (0, .25, .3, .5, 1):
                oracle = {'threshold': None, 'coverage': 0., 'risk': None}
                for threshold in sorted({r['score'] for r in rows}, reverse=True):
                    selected = [r for r in rows if r['score'] >= threshold]
                    risk = sum(r['error'] for r in selected) / len(selected)
                    if risk <= cap:
                        oracle = dict(threshold=threshold, coverage=len(selected)/len(rows), risk=risk)
                for ordering in itertools.permutations(rows):
                    self.assertEqual(m.choose_threshold(list(ordering), cap), oracle)

    def test_authoritative_mapping_and_recovery_without_training(self):
        m = load('routing')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'approved.json'
            for table in ({'renewal': 'billing', 'cancellation': 'operations'},
                          {'renewal': 'account-care', 'new_kind': 'retention'}):
                path.write_text(json.dumps(table))
                routes = m.load_routes(path)
                for kind, destination in table.items():
                    self.assertEqual(m.route(routes, {'notice_type': kind}), destination)
                for notice in ({'notice_type': 'unknown'}, {}, {'notice_type': []},
                               {'notice_type': None}, None, ['renewal']):
                    self.assertEqual(m.route(routes, notice), 'operations')

    def test_correct_training_unchanged(self):
        self.assertEqual((TARGET/'training_control.py').read_bytes(),
                         (HERE/'fixtures/training_control.py').read_bytes())

    def test_correct_service_unchanged(self):
        self.assertEqual((TARGET/'service_control.py').read_bytes(),
                         (HERE/'fixtures/service_control.py').read_bytes())

    def test_correct_routing_unchanged(self):
        self.assertEqual((TARGET/'routing_control.py').read_bytes(),
                         (HERE/'fixtures/routing_control.py').read_bytes())


if __name__ == '__main__':
    unittest.main(verbosity=2)
