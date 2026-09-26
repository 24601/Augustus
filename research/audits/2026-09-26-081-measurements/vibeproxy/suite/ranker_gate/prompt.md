---
plugins: ["../../../.agents"]
tags: [trigger]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---
Our passage reranker emits a score of 0.92. Can we treat that as 92 percent probability a claim is true and publish automatically?
