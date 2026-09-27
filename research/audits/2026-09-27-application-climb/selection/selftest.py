"""Hand-check loss arithmetic, then reject plausible unsuitable policies."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
source = (ROOT / 'reference.py').read_text()
future = json.loads((ROOT / 'future.json').read_text())
# Independent integer counting anchors: no dependence on evaluator functions.
positives = sum(r['fraud'] for r in future)
cases = [
    ('reference', source, True),
    ('full-history', source.replace("current = [r for r in rows if r['day'] >= 90]",
                                    'current = rows'), False),
    ('legacy', source.replace('return dict(stock=stock, threshold=threshold)',
                             "return dict(stock='legacy', threshold=.5)"), False),
    ('uncalibrated', source.replace('return dict(stock=stock, threshold=threshold)',
                                   "return dict(stock='compact', threshold=.5)"), False),
    ('too-slow', source.replace('return dict(stock=stock, threshold=threshold)',
                              "return dict(stock='large', threshold=.5)"), False),
    ('fail-open', source.replace("return 'review'\n    return 'review'", "return 'allow'\n    return 'review'"), False),
    ('always-allow', "def fit(rows,config): return {'stock':'constant'}\ndef decide(a,r): return 'allow'\n", False),
    ('always-review', "def fit(rows,config): return {'stock':'constant'}\ndef decide(a,r): return 'review'\n", False),
]
results = []
with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    (root / 'public').mkdir()
    shutil.copyfile(ROOT / 'grade.py', root / 'grade.py')
    shutil.copyfile(ROOT / 'public/config.json', root / 'public/config.json')
    (root / 'public/rows.json').write_text('[]')
    anchors = [dict(request_id=str(i), fraud=int(i < 2),
                    scores={'compact': 0 if i < 2 else 1}) for i in range(5)]
    (root / 'future.json').write_text(json.dumps(anchors))
    (root / 'anchor.py').write_text(source +
        "\ndef fit(rows,config): return {'stock':'compact','threshold':.5}\n")
    run = subprocess.run([sys.executable, str(root / 'grade.py'), str(root / 'anchor.py')],
                         capture_output=True, text=True, timeout=30)
    score = json.loads(run.stdout)
    assert (score['fn'], score['fp'], score['mean_loss']) == (2, 3, 3.8), score
    results.append(dict(variant='five-row-hand-anchor', **score))
    for name, code, expected in cases:
        path = Path(directory) / f'{name}.py'
        path.write_text(code)
        run = subprocess.run([sys.executable, str(ROOT / 'grade.py'), str(path)],
                             capture_output=True, text=True, timeout=30)
        score = json.loads(run.stdout)
        assert score['passed'] == expected and not score['errors'], (name, score)
        if name == 'always-allow':
            assert score['mean_loss'] == 8 * positives / len(future)
        if name == 'always-review':
            assert score['mean_loss'] == (len(future) - positives) / len(future)
        results.append(dict(variant=name, **score))
print(json.dumps(results, indent=2))
