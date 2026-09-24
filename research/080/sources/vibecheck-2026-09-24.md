# vibecheck — card (2026-09-24)

`jlowin/vibecheck`, created 2026-09-24T00:26:22Z, 19 commits, 8 stars at sighting. Published as
`vibecheck-py`. Read from the repository README; nothing installed or run. Behaviour described
below is as documented, not as executed.

A Python DSL that puts typed decisions behind four functions: `check` → `bool`, `classify` → one
option, `label` → a list, `score` → a `float`. Default backend is TypeSafe's System One API;
`TYPESAFE_BASE_URL` makes any compatible endpoint work, and the README shows Vercel AI Gateway
serving Jev without a TypeSafe account. It is the same interface argument this project makes —
judgment calls as function calls, no prompt templating and no parsing — expressed as ergonomics.

## What is well designed, and worth borrowing

- **The three-way `check`.** A `(low, high)` threshold returns `None` between the bounds, and the
  README insists on `match` over `if` because `None` is falsy and an `if` would silently read
  "unsure" as "no". That is the deferral band as a language construct, with the footgun named.
- **Options carry descriptions.** `{"billing": "Charges, invoices, refunds, payment problems"}`
  puts the edge cases in the option text, which is where a bounded decision's real specification
  lives. Duplicate labels raise before any request is sent.
- **Testing without the network.** `FakeBackend` records requests and answers from a function you
  supply, so decision logic is testable like any other logic.
- **`model=` pinning, with the reason stated:** pin a version once thresholds are tuned, because
  `jev-latest` moves when a release ships. That is version discipline in a README, which is rarer
  than it should be.

## Two things to flag rather than adopt

**`score` returns a probability-weighted average of level indices.** The README is explicit: `1.4`
means the model is split between levels 1 and 2 and leans toward 1. That is an expectation taken
over an **ordinal** scale, which presumes the levels are evenly spaced when nothing guarantees they
are. As a decision statistic to threshold — `if severity >= 1.5` — it is defensible, and that is how
every example uses it. As a reported quantity it is not an ordinal estimate, and "the model rated
it 1.4" would be a category error of the kind this project's guidance names: an ordinal score is
not a cardinal one. Anything we borrow keeps the threshold use and drops the reported number.

**Probabilities are presented without a calibration status.** "A probability attached to every
answer" is the provider's output, not a demonstrated calibration, and the README's threshold advice
(raise to 0.9 when a false yes is expensive) reads the number as if it were calibrated. The CMU
cascade paper measured exactly this and found the confidence useful on some tasks and worthless on
others — AUROC 0.518 on reference-free prose. Our own emitted `/v1/systemone` carries
`confidence_convention` and `calibration_status` for this reason; a client library that omits them
is where that distinction gets lost.

Also **Reported, and thin**: "in a test with a 5,000-token document, 100 questions asked together
gave the same answers as 100 separate requests, for about 1% of the tokens." One document, one
test, no interval. The batching economics are plausible and the agreement claim is not established.

## Disposition

**Discovery record and an interface reference. Not an arm, not a dependency, not a comparator.**
Its value is as the clearest third-party statement of the call shape, and as a live example of two
hazards worth writing about: averaging an ordinal scale into a float, and presenting a provider
probability as if its calibration were settled. Both belong in the position paper's interface
discussion as concrete, dated, real-world instances rather than as hypotheticals.
