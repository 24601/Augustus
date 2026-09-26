"""Alternative JSON inference path."""
import json
import math
from pathlib import Path
import sys


def load_bundle(path):
    bundle = json.loads(Path(path).read_text())
    if bundle.get('calibration_required'):
        t = bundle.get('temperature')
        if type(t) not in (float, int) or not math.isfinite(t) or t <= 0:
            raise ValueError('required temperature missing or invalid')
    return bundle


def predict(bundle, logits):
    temperature = bundle['temperature'] if bundle.get('calibration_required') else 1.0
    peak = max(logits)
    # Subtract first for close logits; scale first only if subtraction overflows.
    scaled = [(x - peak) / temperature if math.isfinite(x - peak)
              else x / temperature - peak / temperature for x in logits]
    weights = [math.exp(x) for x in scaled]
    probabilities = [x / sum(weights) for x in weights]
    expected = sum(level * p for level, p in zip(bundle['levels'], probabilities))
    return {'probabilities': probabilities, 'expected': expected,
            'action': 'act' if expected > bundle['threshold'] else 'review'}


if __name__ == '__main__':
    bundle = load_bundle(sys.argv[1])
    for line in sys.stdin:
        print(json.dumps(predict(bundle, json.loads(line)['logits'])))
