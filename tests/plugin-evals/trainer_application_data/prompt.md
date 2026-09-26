---
plugins: ["../../../.agents"]
tags: [trigger]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---
Help me train a local support-intent classifier from our application's CSV export. It has 18,000 rows: individual replies from the same ticket, quoted copies, customer IDs, final queue, and resolution notes written after routing. Some billing tickets end up with engineering; two reviewers disagree about the right queue. We want to route the first incoming message for new customers next month. How should we turn this into a usable training and evaluation set?
