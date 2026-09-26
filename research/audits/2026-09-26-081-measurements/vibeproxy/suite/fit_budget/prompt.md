---
plugins: ["../../../.agents"]
tags: [trigger]
max_turns: 12
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---
We route inbound requests into six queues. I have 24 independently labelled examples per queue, a laptop, and no measured result for the current rules. Should I fit a small model, fine-tune a large one, or collect more data first? Give me an executable experiment plan and a stop rule, not an actual training run.
