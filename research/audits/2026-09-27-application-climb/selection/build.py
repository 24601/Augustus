"""Coordinator-only synthetic data builder. Never shipped to task agents."""
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parent
CONFIG = {'fn_cost': 8, 'fp_cost': 1, 'max_latency_ms': 15,
          'max_mean_loss': .45,
          'stocks': {'legacy': {'latency_ms': 3},
                     'compact': {'latency_ms': 9},
                     'large': {'latency_ms': 120}}}


def records(seed, n, future=False):
    rng = random.Random(seed)
    result = []
    for i in range(n):
        day = 120 + i % 7 if future else i // 10
        current = day >= 90
        y = int(rng.random() < .18)
        legacy = rng.gauss(.8 if y else .2, .12) if not current else rng.random()
        compact = rng.gauss(.10 if y else .025, .024) if current else rng.random() * .15
        large = rng.gauss(.9 if y else .1, .04)
        result.append(dict(request_id=f'{rng.getrandbits(80):020x}', day=day, fraud=y,
                           scores={k: round(min(1, max(0, v)), 6) for k, v in
                                   [('legacy', legacy), ('compact', compact), ('large', large)]}))
    rng.shuffle(result)
    return result


if __name__ == '__main__':
    (ROOT / 'public/config.json').write_text(json.dumps(CONFIG, indent=2) + '\n')
    (ROOT / 'public/rows.json').write_text(json.dumps(records(48103, 1200)) + '\n')
    (ROOT / 'future.json').write_text(json.dumps(records(931871, 4000, True)) + '\n')
