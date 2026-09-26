---
plugins: ["../../../.agents"]
tags: [trigger]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---
We generate JSON with a large LLM to sort refund emails, then a service issues refunds when confidence is above 0.9. Audit this design. Emails may omit order IDs.
