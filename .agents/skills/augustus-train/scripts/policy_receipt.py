#!/usr/bin/env python3
"""Population-bound binary raw-score diagnostics, not confirmation or forecasting.

JSON input: population {name, selection, ids}, rows [{id, score, y}],
threshold, shift (>0), cost_fp, cost_fn. Positive action means score >= threshold.
Shifts are additive, without clipping. No probability interpretation is implied.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path


def number(value):
    if type(value) not in (int, float):
        raise ValueError('numbers must be finite and not boolean')
    try:
        if not math.isfinite(value):
            raise ValueError('numbers must be finite')
    except OverflowError as exc:
        raise ValueError('numbers must be finite') from exc
    return Fraction(value)


def receipt(data):
    population = data['population']
    for key in ('name', 'selection'):
        if not isinstance(population[key], str) or not population[key].strip():
            raise ValueError('population name and selection description required')
    ids = population['ids']
    if not isinstance(ids, list) or not ids or any(type(i) is not str or not i for i in ids):
        raise ValueError('nonempty population IDs required')
    if len(set(ids)) != len(ids):
        raise ValueError('duplicate population ID')
    rows = {}
    for row in data['rows']:
        key = row['id']
        if type(key) is not str or not key or key in rows:
            raise ValueError('invalid or duplicate row ID')
        if type(row['y']) is not int or row['y'] not in (0, 1):
            raise ValueError('y must be integer 0 or 1')
        rows[key] = (number(row['score']), row['y'])
    if not set(ids) <= rows.keys():
        raise ValueError('population ID absent from input rows')
    chosen = [rows[i] for i in ids]
    threshold, shift = number(data['threshold']), number(data['shift'])
    fp_cost, fn_cost = number(data['cost_fp']), number(data['cost_fn'])
    if shift <= 0 or min(fp_cost, fn_cost) < 0:
        raise ValueError('shift must be positive and costs nonnegative')
    reports = []
    for name, score_delta, threshold_delta in (
        ('baseline', 0, 0), ('score_down', -shift, 0), ('score_up', shift, 0),
        ('threshold_down', 0, -shift), ('threshold_up', 0, shift),
    ):
        actions = [s + score_delta >= threshold + threshold_delta for s, _ in chosen]
        fp = sum(a and y == 0 for a, (_, y) in zip(actions, chosen))
        fn = sum(not a and y == 1 for a, (_, y) in zip(actions, chosen))
        loss = (fp * fp_cost + fn * fn_cost) / len(chosen)
        reports.append(dict(intervention=name, n=len(chosen), positive_actions=sum(actions),
                            action_rate=sum(actions) / len(chosen), fp=fp, fn=fn,
                            mean_loss=float(loss)))
    selected = [{'id': i, 'score': str(rows[i][0]), 'y': rows[i][1]} for i in sorted(ids)]
    return dict(evidence='descriptive', population=dict(name=population['name'],
                selection=population['selection'], n=len(ids),
                selected_rows_sha256=hashlib.sha256(json.dumps(selected, sort_keys=True).encode()).hexdigest()),
                policy=dict(threshold=data['threshold'], shift=data['shift'],
                            cost_fp=data['cost_fp'], cost_fn=data['cost_fn'],
                            comparison='score >= threshold', clipping='none'),
                reports=reports)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key: {key}')
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    args = parser.parse_args()
    try:
        raw = args.input.read_bytes()
        data = json.loads(raw, object_pairs_hook=unique_object)
        result = receipt(data)
        result['input_sha256'] = hashlib.sha256(raw).hexdigest()
        print(json.dumps(result, allow_nan=False, indent=2))
    except (ValueError, KeyError, TypeError, OSError, OverflowError, RecursionError) as exc:
        parser.error(str(exc))


if __name__ == '__main__':
    main()
