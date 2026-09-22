"""Exact finite examples and counterexamples, not model performance evidence."""
from fractions import Fraction as F
from itertools import product
import unittest


class CompositionLawTests(unittest.TestCase):
    def test_branch_risk_and_selection_conditioning(self):
        # Ten equally likely episodes. The gate keeps two, both bad for stage 2.
        selected = [True, True] + [False] * 8
        errors = [True, True] + [False] * 8
        marginal = F(sum(errors), 10)
        conditional = F(sum(g and e for g, e in zip(selected, errors)), sum(selected))
        self.assertEqual(marginal, F(1, 5))
        self.assertEqual(conditional, 1)
        joint = F(sum(g and e for g, e in zip(selected, errors)), 10)
        self.assertEqual(joint, F(sum(selected), 10) * conditional)
        self.assertNotEqual(joint, F(sum(selected), 10) * marginal)
        # Other branch has loss 1/4, all units included in a common loss scale.
        direct = sum((F(int(e)) if g else F(1, 4)) for g, e in zip(selected, errors)) / 10
        self.assertEqual(direct, F(1, 5) * conditional + F(4, 5) * F(1, 4))

    def test_union_bound_does_not_require_independence_and_can_be_tight(self):
        for first in product((False, True), repeat=4):
            for second in product((False, True), repeat=4):
                union = F(sum(a or b for a, b in zip(first, second)), 4)
                sum_marginals = F(sum(first) + sum(second), 4)
                self.assertLessEqual(union, min(1, sum_marginals))
        # Mutually exclusive failures differ from the independence calculation.
        self.assertEqual(F(1, 4) + F(1, 4), F(1, 2))
        self.assertNotEqual(F(1, 2), 1 - F(3, 4) ** 2)

    def test_bounded_loss_plugin_regret_by_exact_enumeration(self):
        checked = 0
        # Three feasible actions, two states; same actions/loss under p and q.
        for flat_losses in product((F(0), F(1, 2), F(1)), repeat=6):
            losses = list(zip(flat_losses[::2], flat_losses[1::2]))
            for p, q in product((F(0), F(1, 4), F(1, 2), F(3, 4), F(1)), repeat=2):
                p_risks = [p * yes + (1 - p) * no for yes, no in losses]
                q_risks = [q * yes + (1 - q) * no for yes, no in losses]
                selected = min(range(3), key=lambda i: q_risks[i])
                regret = p_risks[selected] - min(p_risks)
                self.assertLessEqual(regret, 2 * abs(p - q))
                checked += 1
        self.assertEqual(checked, 18225)

    def test_background_evidence_changes_signal_substitutability(self):
        worlds = list(product((0, 1), repeat=2))  # Y, C independent fair bits.
        def bayes_error(observe):
            groups = {}
            for y, c in worlds:
                counts = groups.setdefault(observe(y, c), [0, 0])
                counts[y] += 1
            return F(sum(min(counts) for counts in groups.values()), len(worlds))
        self.assertEqual(bayes_error(lambda y, c: c), F(1, 2))
        self.assertEqual(bayes_error(lambda y, c: y ^ c), F(1, 2))
        self.assertEqual(bayes_error(lambda y, c: (c, c)), F(1, 2))
        self.assertEqual(bayes_error(lambda y, c: (c, y ^ c)), 0)


if __name__ == "__main__":
    unittest.main()
