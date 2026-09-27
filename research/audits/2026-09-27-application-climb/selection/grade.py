"""Frozen private future-outcome evaluator. python grade.py solution.py."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def load_module(path):
    spec = importlib.util.spec_from_file_location('solution', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate(source):
    config = json.loads((ROOT / 'public/config.json').read_text())
    rows = json.loads((ROOT / 'public/rows.json').read_text())
    future = json.loads((ROOT / 'future.json').read_text())
    module = load_module(source)
    artifact = json.loads(json.dumps(module.fit(rows, config), allow_nan=False))
    stock = artifact['stock']
    if stock != 'constant' and stock not in config['stocks']:
        raise ValueError('unknown stock')
    latency = 0 if stock == 'constant' else config['stocks'][stock]['latency_ms']
    serving = [dict(request_id=r['request_id'], scores={} if stock == 'constant'
                    else {stock: r['scores'][stock]}) for r in future]
    bad = [dict(request_id='missing', scores={}), dict(request_id='null', scores=None)]
    bad += [dict(request_id=f'bad-{i}', scores={stock: v}) for i, v in enumerate(
        [None, True, False, '0.1', -.1, 1.1, float('nan'), float('inf')])]
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory)
        shutil.copyfile(source, path / 'solution.py')
        (path / 'artifact.json').write_text(json.dumps(artifact, allow_nan=False))
        driver = ('import json,sys,solution\n'
                  'a=json.load(open("artifact.json"))\n'
                  'print(json.dumps([solution.decide(a,r) for r in json.load(sys.stdin)]))\n')
        run = subprocess.run([sys.executable, '-c', driver], cwd=path,
                             input=json.dumps(serving + bad), text=True,
                             capture_output=True, timeout=15, check=True)
        actions = json.loads(run.stdout)
    if len(actions) != len(serving) + len(bad) or any(a not in ('allow', 'review') for a in actions):
        raise ValueError('invalid decision output')
    fp = sum(a == 'review' and r['fraud'] == 0 for a, r in zip(actions, future))
    fn = sum(a == 'allow' and r['fraud'] == 1 for a, r in zip(actions, future))
    loss = (8 * fn + fp) / len(future)
    failures = sum(a != 'review' for a in actions[len(future):])
    return dict(passed=loss <= config['max_mean_loss'] and failures == 0 and
                latency <= config['max_latency_ms'], mean_loss=loss, fp=fp, fn=fn,
                n=len(future), safety_failures=failures, stock=stock, latency_ms=latency,
                fresh_process=True, artifact=artifact, errors=[])


if __name__ == '__main__':
    try:
        result = evaluate(Path(sys.argv[1]).resolve())
    except Exception as exc:
        result = dict(passed=False, mean_loss=None, safety_failures=None,
                      fresh_process=False, errors=[f'{type(exc).__name__}: {exc}'])
    print(json.dumps(result, allow_nan=False))
    sys.exit(0 if result['passed'] else 1)
