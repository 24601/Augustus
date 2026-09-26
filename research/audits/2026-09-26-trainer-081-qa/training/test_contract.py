"""Independent contract probes; no repository or parent test dependencies."""
import importlib
import math
import unittest

import torch

torch.set_num_threads(1)


class TrainingContract(unittest.TestCase):
    def test_optimizer_updates_and_freezes(self):
        for module_name in ("training", "training_control"):
            module = importlib.import_module(module_name)
            torch.manual_seed(29)
            model = module.DecisionModel().double()
            # Reuse the model across mode transitions, including a previously
            # trained encoder, to catch accidental permanent freezing.
            for tune in (True, False, True):
                with self.subTest(module=module_name, tune=tune):
                    optimizer = module.make_optimizer(model, tune, 0.2)
                    before = {n: p.detach().clone() for n, p in model.named_parameters()}
                    model.zero_grad(set_to_none=True)
                    x = torch.tensor([[1.2, -0.7], [-0.3, 2.1], [0.8, 0.4]], dtype=torch.float64)
                    targets = torch.tensor([0.17, 0.82, 0.61], dtype=torch.float64)
                    loss = module.soft_loss(model(x), targets)
                    self.assertTrue(torch.isfinite(loss))
                    loss.backward()
                    for name, param in model.named_parameters():
                        if tune or name.startswith("head."):
                            self.assertIsNotNone(param.grad)
                            self.assertTrue(torch.isfinite(param.grad).all())
                            self.assertGreater(param.grad.abs().sum().item(), 0)
                    optimizer.step()
                    changes = {n: (p.detach() - before[n]).abs().max().item()
                               for n, p in model.named_parameters()}
                    print(module_name, "tune", tune, "deltas", changes)
                    for name, delta in changes.items():
                        if tune or name.startswith("head."):
                            self.assertGreater(delta, 0, name)
                        else:
                            self.assertEqual(delta, 0, name)
                    actual = {id(p) for group in optimizer.param_groups for p in group["params"]}
                    expected = {id(p) for n, p in model.named_parameters()
                                if tune or n.startswith("head.")}
                    self.assertEqual(actual, expected)

    def test_soft_loss_value_and_actual_gradient(self):
        zs = [-2.0, 0.0, 1.3, 4.0, -0.4]
        ys = [0.13, 0.5, 0.79, 1.0, 0.0]
        expected_loss = sum(math.log1p(math.exp(z)) - y*z for z, y in zip(zs, ys))/len(zs)
        expected_grad = torch.tensor([(1/(1+math.exp(-z))-y)/len(zs)
                                      for z, y in zip(zs, ys)], dtype=torch.float64)
        for name in ("training", "training_control"):
            with self.subTest(module=name):
                module = importlib.import_module(name)
                logits = torch.tensor(zs, dtype=torch.float64, requires_grad=True)
                loss = module.soft_loss(logits, torch.tensor(ys, dtype=torch.float64))
                loss.backward()
                print(name, "loss", loss.item(), "gradient", logits.grad.tolist())
                # Check gradient before value: this fails even for a detached
                # correct-looking scalar or a surrogate hard-label backward.
                torch.testing.assert_close(logits.grad, expected_grad, rtol=1e-12, atol=1e-12)
                self.assertAlmostEqual(loss.item(), expected_loss, places=12)

    def test_real_model_converges_to_soft_targets(self):
        for name in ("training", "training_control"):
            for target in (0.3, 0.73):
                for tune in (False, True):
                    with self.subTest(module=name, target=target, tune=tune):
                        module = importlib.import_module(name)
                        torch.manual_seed(41)
                        model = module.DecisionModel().double()
                        optimizer = module.make_optimizer(model, tune, 0.2)
                        x = torch.tensor([[0.4, -0.8]] * 7, dtype=torch.float64)
                        y = torch.full((7,), target, dtype=torch.float64)
                        for _ in range(600):
                            optimizer.zero_grad(set_to_none=True)
                            loss = module.soft_loss(model(x), y)
                            loss.backward()
                            optimizer.step()
                        with torch.no_grad():
                            probability = model(x).sigmoid().mean().item()
                            final_loss = module.soft_loss(model(x), y).item()
                        print(name, "target", target, "tune", tune,
                              "probability", probability, "loss", final_loss)
                        self.assertAlmostEqual(probability, target, delta=1e-5)
                        entropy = -target*math.log(target)-(1-target)*math.log(1-target)
                        self.assertAlmostEqual(final_loss, entropy, delta=1e-9)


if __name__ == "__main__":
    unittest.main(verbosity=2)
