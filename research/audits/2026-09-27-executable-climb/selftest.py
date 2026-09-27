"""Validate the checker against a reference and deliberately wrong variants."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
source = (ROOT / 'reference.py').read_text()
mutations = [
    ('data', 'nontransitive', 'group.update(linked)', 'group.update(linked)\n            break'),
    ('data', 'replace-first', "first.setdefault(r['ticket'], r)", "first[r['ticket']] = r"),
    ('planning', 'row-only', "r['group'] not in groups", "r['id'] not in fold"),
    ('planning', 'repay-sunk', "0 if c['already_paid'] else c['fit_cost']", "c['fit_cost']"),
    ('training', 'hard-targets', "-r['target']", "-int(r['target'] >= .5)"),
    ('training', 'ignore-temperature', "/bundle['temperature']", ''),
    ('training', 'positive-tie', 'positive < negative', 'positive <= negative'),
]
results = []
with tempfile.TemporaryDirectory() as directory:
    for task in ('data', 'planning', 'training'):
        run = subprocess.run([sys.executable, str(ROOT / 'grade.py'), task,
                              str(ROOT / 'reference.py')], capture_output=True, text=True)
        assert run.returncode == 0, run.stderr
        results.append(dict(task=task, variant='reference', accepted=True))
    for task, name, old, new in mutations:
        assert source.count(old) == 1, (name, source.count(old))
        path = Path(directory) / (name + '.py')
        path.write_text(source.replace(old, new))
        run = subprocess.run([sys.executable, str(ROOT / 'grade.py'), task, str(path)],
                             capture_output=True, text=True)
        summary = json.loads(run.stdout.splitlines()[-1])
        assert run.returncode == 1 and summary['failures'] > 0, (name, run.stderr)
        results.append(dict(task=task, variant=name, accepted=False,
                            assertion_failures=summary['failures']))
print(json.dumps(results, indent=2))
