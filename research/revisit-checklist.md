# Revisit a catalogued source

Treat **revisit HIGH like novel HIGH** when behavior or evidence changes.
Use the same canonical source identity and existing notes section.

## Fingerprints

The offline helper `revisit_fingerprints.py` requires all four fields:

| Field | Meaning |
| --- | --- |
| `default_sha` | Full lowercase 40-character HEAD, or explicit null when unavailable |
| `pushed_at` | GitHub UTC push timestamp ending in Z, or null |
| `description_hash` | SHA-256 first 12 lowercase hex characters of the description, or null |
| `release_tag` | Nonempty release tag or explicit null |

README hashes and commit timestamps are useful additional evidence but are
not substitutes for description hashes and push timestamps. Source IDs must
agree when comparing observations; verify renames using stable host identity.
Collector entries use canonical `id`, retain `requested_id`, and record GitHub's
stable `node_id`. Compare individual `sources[]` entries, not the whole receipt.
If the canonical ID changed, inspect the stable identity and record the rename
before updating a baseline; do not suppress a cross-source mismatch.

## Review a change

1. Compare the new receipt with the stored snapshot. A moved SHA or timestamp
   triggers inspection; it does not alone establish a material capability change.
   The helper reports `review` / `inspect_diff` with
   `capability_change_claimed: false`. Only explicitly supplied, inspected
   `material_signals` yield `material` / `densify`; stars alone are `star_noise`.
2. Inspect changes to README claims, APIs, release contents, calibration,
   serving behavior, and benchmarks. Keep stars/likes/forks as observations.
3. Record retrieval time, revision, the prior claim, the new claim, and its
   evidence status. Missing evidence is not a negative finding.
4. Add a dated update to the existing source card. Preserve retractions and
   contradictory findings rather than silently overwriting them.
5. Promote only an actual design lesson to its relevant reference. Keep
   identity locks and hourly accounting out of runtime guidance and the site.
6. Run `make check` and inspect the diff before handoff. Scripts do not
   update baselines or publish on their own.

Run `python3 research/revisit_fingerprints.py --help` for offline comparison
and validation commands. The [research protocol](protocol.md) owns claim
status and promotion; the [fold prompt](prompts/research-fold.md) is reusable.
