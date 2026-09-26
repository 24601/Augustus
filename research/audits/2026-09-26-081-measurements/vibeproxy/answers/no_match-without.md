I couldn't find any classifier code in this repo (a search for `billing`, `unsubscribe`, `softmax` and `threshold` came back empty). So this is a design fix you can apply to your own code.

## Why raising the threshold didn't help

The model has only three labels, and something like softmax makes their scores add up to 1. It can only answer "which of these three is it most like", never "none of these". An unsubscribe request is mostly about account and money, so billing takes almost all of the score and gets 1.0. That number shows how billing compares to sales and support. It doesn't show whether the request belongs in any of the three.

A threshold only filters on that number. When the wrong answer scores 1.0, no threshold will catch it. The design has no way to express "none of these".

## The fix: make "none of these" a real answer

**1. Add an explicit catch-all label.** Use `other` or `unroutable`, plus a named class for any frequent case like `account_management` or `unsubscribe`.

- **ML classifier:** retrain with labeled examples of out-of-scope requests: unsubscribes, spam, account deletion, and "wrong department". If the model never sees "none of these" in training, it can't predict it.
- **LLM classifier:** list `other` in the allowed outputs and describe each category precisely, including what it excludes. For example: "billing: questions about charges, invoices, refunds, payment methods. NOT subscription cancellation or email opt-out."

**2. Score each label independently instead of making them compete.** Use a sigmoid per label, or ask an LLM a yes/no question for each category. The scores no longer have to add up to 1, so all three can be low. Route to `other` when every score is below the threshold. At that point your threshold finally does something.

**3. Handle known out-of-scope intents before the classifier.** Unsubscribe and opt-out are often legally required (CAN-SPAM, GDPR), so don't let a probabilistic model decide where they go. Send them to the opt-out flow with a keyword or intent rule first, and send only the remaining requests to the classifier.

**4. Send `other` somewhere real.** That means a human triage queue or a general inbox. Track how much volume goes there. If a theme keeps showing up, make it its own class.

## Resulting flow

```
request
  → rule check (unsubscribe/opt-out/delete-account) → compliance flow
  → classifier with labels {sales, billing, technical_support, other}
       scored independently (sigmoid / per-label yes-no)
  → if max score < threshold OR label == other → human triage queue
  → else → route to team
```

## Verify it

Build a test set that includes out-of-scope requests (unsubscribe, spam, gibberish, wrong language) and check that they reach `other` or the rule path. Accuracy on in-scope requests alone can't show whether this bug is fixed.

If you point me to where the classifier lives or paste the code, I can make these changes directly.
