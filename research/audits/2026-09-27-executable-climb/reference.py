"""Coordinator reference for validating the instrument, not shown to agents."""
import json
import math
from pathlib import Path
import sys


def prepare(rows, train_end, dev_end):
    first = {}
    for r in sorted(rows, key=lambda r: (r['time'], r['text'])):
        if r['role'] == 'user':
            first.setdefault(r['ticket'], r)
    eligible = []
    for r in first.values():
        if not r['text'].strip() or r['label'] is None or r['label_status'] != 'agreed':
            continue
        role = 0 if r['time'] < train_end else 1 if r['time'] < dev_end else 2
        if role < 2 and r['label_time'] >= (train_end, dev_end)[role]:
            continue
        eligible.append((r, role, ' '.join(r['text'].casefold().split())))
    output = {role: [] for role in ('train', 'dev', 'confirm')}
    unseen = set(range(len(eligible)))
    while unseen:
        group = {unseen.pop()}
        while True:
            linked = {j for j in unseen if any(
                eligible[j][0]['customer'] == eligible[i][0]['customer'] or
                eligible[j][2] == eligible[i][2] for i in group)}
            if not linked:
                break
            group.update(linked)
            unseen.difference_update(linked)
        role = min(eligible[i][1] for i in group)
        for i in group:
            r, assigned, _ = eligible[i]
            if assigned == role:
                output[('train', 'dev', 'confirm')[role]].append(
                    dict(id=r['ticket'], customer=r['customer'], text=r['text'], label=r['label']))
    for items in output.values():
        items.sort(key=lambda r: r['id'])
    return output


def curve(rows, folds, sizes):
    ids = {r['id'] for r in rows}
    if len(ids) != len(rows):
        raise ValueError('duplicate ID')
    result = []
    for fold in folds:
        if not set(fold) <= ids:
            raise ValueError('unknown ID')
        groups = {r['group'] for r in rows if r['id'] in fold}
        counts = {label: sum(r['label'] == label and r['group'] not in groups for r in rows)
                  for label in {r['label'] for r in rows}}
        available = sorted({s for s in sizes if type(s) is int and
                            0 < s <= min(counts.values(), default=0)})
        result.append(dict(available=counts, sizes=available))
    return result


def select(candidates, horizon, fn_cost, fp_cost, max_latency):
    feasible = [((c['fn']*fn_cost+c['fp']*fp_cost)/c['n']*horizon +
                 (0 if c['already_paid'] else c['fit_cost']), c['name'])
                for c in candidates if c['latency_ms'] <= max_latency]
    if not feasible:
        return None
    cost, name = min(feasible)
    return dict(name=name, total_cost=cost)


def sigmoid(z):
    if z >= 0:
        return 1/(1+math.exp(-z))
    e = math.exp(z)
    return e/(1+e)


def fit(rows, epochs, lr):
    w = b = 0.
    for _ in range(epochs):
        errors = [sigmoid(w*r['x']+b)-r['target'] for r in rows]
        w, b = (w-lr*sum(e*r['x'] for e, r in zip(errors, rows))/len(rows),
                b-lr*sum(errors)/len(rows))
    return dict(w=w, b=b)


def validate(bundle):
    for key in ('temperature', 'fn_cost', 'fp_cost'):
        v = bundle[key]
        if type(v) not in (float, int) or not math.isfinite(v) or v <= 0:
            raise ValueError(key)


def export(path, model, temperature, fn_cost, fp_cost):
    bundle = dict(model=model, temperature=temperature, fn_cost=fn_cost, fp_cost=fp_cost)
    validate(bundle)
    with open(path, 'x') as f:
        json.dump(bundle, f)


def load(path):
    bundle = json.loads(Path(path).read_text())
    validate(bundle)
    return bundle


def predict(bundle, x):
    p = sigmoid((bundle['model']['w']*x+bundle['model']['b'])/bundle['temperature'])
    scale = max(bundle['fn_cost'], bundle['fp_cost'])
    positive = (1-p)*(bundle['fp_cost']/scale)
    negative = p*(bundle['fn_cost']/scale)
    return dict(p=p, action='positive' if positive < negative else 'negative')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'fit':
        data = json.loads(Path(sys.argv[2]).read_text())
        export(sys.argv[3], fit(data['rows'], data['epochs'], data['lr']),
               data['temperature'], data['fn_cost'], data['fp_cost'])
    elif len(sys.argv) > 1 and sys.argv[1] == 'predict':
        bundle = load(sys.argv[2])
        for line in sys.stdin:
            print(json.dumps(predict(bundle, json.loads(line)['x'])))
    else:
        args = json.load(sys.stdin)
        op = args.pop('op', 'prepare')
        print(json.dumps({'prepare': prepare, 'curve': curve, 'select': select}[op](**args)))
