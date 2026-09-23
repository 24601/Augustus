---
type: llm
---

Judge only the final reply to a request to fix a classifier that must pick sales, billing, or technical support and labeled an unsubscribe request billing with confidence 1.0, where raising the threshold did not help.

PASS if the reply says the right answer is missing from the three labels and adds an explicit way to answer none of these (for example an other, unsubscribe, or no-match option, or a separate out-of-scope check) instead of relying on the threshold.

FAIL if it only tunes the threshold, recalibrates, or retrains within the same three labels. Ignore formatting, length and headings.
