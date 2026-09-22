# Activation examples

Use Augustus when the task needs judgment about where a bounded model
belongs or how its output should affect a decision. Examples:

- “Which parts of this agent should be classifiers instead of generated JSON?”
- “Should this route, rank, abstain, gather evidence, or ask a person?”
- “Can I threshold these scores? What does calibrated confidence mean here?”
- “Where could Jev, an encoder, or a local decision head improve this workflow?”
- “How can expected utility, VOI, MCDA, or signal detection help this decision?”
- “Which component of this classical algorithm could use semantic judgment?”
- “Review this approval gate, context sieve, search loop, or done-check.”
- “Does this use of a decision model actually replace proof or simulation?”

The domain can be software, an operational process, research, business,
or everyday planning. Bounded does not mean trivial: verify that the
available evidence supports the requested judgment.

Do not activate merely because a task mentions AI, code, a database, or a
decision in ordinary language. Routine arithmetic, exact lookups, text
generation, and provider installation do not need this skill. When the
user asks to implement an already chosen API, its current official docs
own the integration details; use Augustus only for a real placement or
evaluation question that remains.

For an existing workflow, start with [boundary audit](boundary-audit.md).
For a new problem, start with [mental models](mental-models.md), then
[judgment class](judgment-class.md). Load further references by the task,
not by matching every phrase in the request.
