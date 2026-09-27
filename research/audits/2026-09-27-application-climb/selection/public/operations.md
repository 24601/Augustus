# Checkout operations note

The logs are synthetic fixtures for this exercise, not customer data. Each row
is one independently sampled order. No case/customer repeats occur. `day` is the
order date relative to this export, `fraud` is an adjudicated binary outcome,
and `scores` holds offline outputs of the three model stocks. All rows have
settled outcomes; score computation did not see those outcomes.

On day 90 we changed the checkout funnel. Next week's traffic is from the new
funnel, which has now been stable for 30 days. The export is intentionally the
full history because finance uses it too. Scores are model-specific numbers,
not comparable probabilities: none has an established calibration certificate
for the current funnel. The legacy vendor trained its model before the change.
The compact vendor refreshed its model for the new checkout; marketing's claim
is not a validation result. The large model's offline quality is not the only
consideration for synchronous serving.

At serving time, a stock can be unavailable or emit malformed data. Valid scores
are finite numeric values in [0,1], excluding booleans. If the selected stock
doesn't return such a value, the review team takes the request. Request IDs are
opaque; do not infer labels or order dates from them. Outcome labels and `day`
are export metadata, not serving features. Model latencies in config are fixed
measured service costs for this exercise; a policy cannot claim a faster model
than the stock it registers.
