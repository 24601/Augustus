"""A feasible coordinator reference; not an intended unique winning algorithm."""
import math


def fit(rows, config):
    current = [r for r in rows if r['day'] >= 90]
    candidates = [(sum(not r['fraud'] for r in current), 'constant', 0)]
    for stock, info in config['stocks'].items():
        if info['latency_ms'] > config['max_latency_ms']:
            continue
        for threshold in [i / 1000 for i in range(1001)]:
            loss = sum((config['fn_cost'] if r['fraud'] else 0)
                       if r['scores'][stock] < threshold else
                       (0 if r['fraud'] else config['fp_cost']) for r in current)
            candidates.append((loss, stock, threshold))
    _, stock, threshold = min(candidates)
    return dict(stock=stock, threshold=threshold)


def decide(artifact, row):
    stock = artifact['stock']
    if stock == 'constant':
        return 'review'
    scores = row.get('scores')
    score = scores.get(stock) if isinstance(scores, dict) else None
    if type(score) not in (float, int) or not math.isfinite(score) or not 0 <= score <= 1:
        return 'review'
    return 'review' if score >= artifact['threshold'] else 'allow'
