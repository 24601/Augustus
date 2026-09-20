# Revisit / since last look

Catalogued repos are not done. Things change a lot. Hourly must
diff fingerprints against the last look and densify when the change
is material.

Revisit / since-last-look lock: catalogued repos are not done; store fingerprints default_sha, pushed_at, description_hash, release_tag; material change is README/API/release/calibration claim/serving port/bench rewrite; star-noise is stars/likes/forks alone; densify the prior notes section, do not mint a sibling first sighting; do not invent equivalence; SHA move is not a replica; treat revisit HIGH like novel HIGH for Augustus; notes.md §122

## Fingerprints to store

Default set, so hourly can diff without re-discovering the world:

| Field | What it catches |
| --- | --- |
| `default_sha` | Default-branch HEAD moved |
| `pushed_at` | GitHub push clock moved |
| `description_hash` | Repo / Space description rewritten |
| `release_tag` | Latest release tag moved or appeared |

Optional extras after a fingerprint hit (not substitutes for the four):
README SHA, OpenAPI / `/v1/systemone` surface, serving port or base URL,
calibration claim, bench rewrite.

Store lives in [`revisit_fingerprints.json`](revisit_fingerprints.json).
Helper: `python3 research/revisit_fingerprints.py --self-test`.

## Material change vs star-noise

**Material (revisit HIGH, treat like novel HIGH):**

- README rewrite (claims, API, install surface, serving port)
- API / primitive / `/v1/systemone` contract change
- New or moved release tag
- Calibration claim appeared, retracted, or restated
- Serving port, base URL, or bottle (GGUF / ONNX / MLX / ggmlc)
- Bench rewrite (new n, new metric, retracted headline)

**Star-noise (pulse only, not a fold):**

- Stars, watchers, forks, Hub likes
- `lastModified UNCHANGED` with likes-only jitter
- Issue-count flap, traffic graphs

A star jump on a thin README is still star-noise. A SHA move on a
0-star repo is still material.

## How densify cards update prior notes

1. Keep the original `notes.md` section id. Append a dated **since last
   look** densify card under that section.
2. Do not mint a sibling first-sighting section for the same source.
   Rename densify is still densify (SemIf §117), not a second census.
3. Quote the new README / API / release *theirs*. Keep the prior quotes
   so the card shows what changed.
4. Do not invent equivalence. SHA move is not a replica. Wire-compat is
   not a calibrated Noul. A new bench number is not Harbor. Argmax
   agree is not semantic equivalence.
5. Namesake locks stay (`a/x ≠ b/x`). Prior uniqueness locks stay one
   consecutive substring. Do not mutate them.
6. Class-relevant revisit HIGH gets the same overlay care as novel HIGH
   (notes, skill mapping if the class table moved, uniqueness if this
   hour is a fold). Skip is for star-noise and collisions, not for "we
   already have a card."

## Paste into hourly fold prompts

Treat **revisit HIGH** like **novel HIGH** for Augustus.

If fingerprints moved on a catalogued repo (`default_sha`,
`pushed_at`, `description_hash`, `release_tag`) or the README / API /
release / calibration claim / serving port / bench rewrote, densify
the prior notes card. Do not skip because it was already catalogued.
Stars / likes / forks alone is star-noise, not a fold. Do not invent
equivalence. SHA move is not a replica. Soft Noul ≠ hard gate.

## Offline check

```bash
python3 research/revisit_fingerprints.py --self-test
python3 .agents/skills/augustus/scripts/uniqueness_gate.py
```

Does not bump 0.5.0. Does not fetch the network. Merged #44 owns
§121. This protocol is §122.
