---
plugins: ["../../../.agents"]
tags: [trigger]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---
A classifier must pick sales, billing, or technical support. It assigns an unsubscribe request to billing with confidence 1.0. Raising the threshold did not help. Fix the design.
