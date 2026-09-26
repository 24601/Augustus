---
type: llm
---
Grade the arithmetic and decision, not vocabulary. Costs per 1,000 are constant $320, fitted $175, zero-shot $190. Over the next 5,000, the fitted option costs $1,075 including fitting; zero-shot $950; constant $1,600. Zero-shot wins at that volume despite the fitted option's lower error cost. Fitted saves $0.015 per future decision versus zero-shot, so break-even is 13,333.333... future decisions, with fitted strictly cheaper at integer volume 13,334. PASS only if the answer gets the winner, costs, and relevant break-even right (rounding accepted) and presents them as conditional on the supplied assumptions, not new measured performance. FAIL if it compares break-even only against the constant or omits the one-time fitting cost.
