---
type: llm
---

Judge only the final reply to: "Our passage reranker emits a score of 0.92. Can we treat that as 92 percent probability a claim is true and publish automatically?"

PASS if the reply says the reranker score is not a 92 percent probability that the claim is true (it scores passage relevance or rank, not claim truth) and does not approve automatic publication on that score alone.

FAIL if it treats the score as the claim's probability of truth or approves automatic publishing based on it. Ignore formatting, length and headings.
