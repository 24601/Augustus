# Coordinator instrument inspection

After committing the measurement contract, the coordinator downloaded both
protected archives and verified their SHA256 values against that contract.
The archives are now consumed evaluation material, not future holdouts.

The public prompts specify deterministic minimax-regret artifact construction
and ordinal-distribution serving. They disclose exact tie-breaking, rejection,
input-ownership and CLI rules. These are constrained implementation tasks, not
open-ended data acquisition or training tasks. Neither explicitly requests a
population report or a bootstrap forecast. This restricts what this experiment
can establish about the reporting patch; no task was replaced after inspection.

The private grader was read before task execution results were available.
Task 1's oracle enumerates pairwise regret independently of the reference's
scenario-minimum implementation. Task 2 uses exact rational expected losses.
Tests include input mutation, malformed evidence, tie and TTL boundaries,
ordering, fresh-process artifact reuse, and callable/CLI agreement. The grader
imports submissions and is not an adversarial-code sandbox; the execution
operator must separately isolate agent workspaces from private grading files.

Coordinator rerun in the Linux orb, Python 3.11:

```sh
python3 -B private/selftest.py
python3 -B private/grade.py private/reference
```

Results: seven independent oracle anchors passed; eight plausible mutants
rejected. Reference task 1: 1,484 checks, zero failures, 717 input cases.
Reference task 2: 229 checks, zero failures, 192 input cases. These validate
the instrument, not the agent or skill. Check counts are not independent tasks.
