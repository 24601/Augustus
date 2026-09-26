"""JSON bundle inference and development-only threshold policy selection."""
import json
import math
from pathlib import Path
import sys


def load_bundle(path):
    bundle = json.loads(Path(path).read_text())
    return bundle


def predict(bundle, logits):
    weights = [math.exp(x - max(logits)) for x in logits]
    probabilities = [x / sum(weights) for x in weights]
    expected = sum(level * p for level, p in zip(bundle['levels'], probabilities))
    return {'probabilities': probabilities, 'expected': expected,
            'action': 'act' if expected > bundle['threshold'] else 'review'}


def choose_threshold(rows, max_risk):
    """Rows contain score and error (0/1); accept score >= threshold."""
    ordered = sorted(rows, key=lambda row: row['score'], reverse=True)
    best = {'threshold': None, 'coverage': 0.0, 'risk': None}
    errors = 0
    for n, row in enumerate(ordered, 1):
        errors += row['error']
        risk = errors / n
        if risk > max_risk:
            break
        best = {'threshold': row['score'], 'coverage': n / len(rows), 'risk': risk}
    return best


if __name__ == '__main__':
    bundle = load_bundle(sys.argv[1])
    for line in sys.stdin:
        print(json.dumps(predict(bundle, json.loads(line)['logits'])))
