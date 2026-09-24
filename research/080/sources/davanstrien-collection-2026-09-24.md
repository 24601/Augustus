# `davanstrien/jev-style-decision-models-open-data` — card (2026-09-24)

A curated Hugging Face collection, 17 datasets, last updated 2026-09-24T08:43Z. Read through the
Hub API; nothing downloaded. Its stated purpose is the one our own protocol insists on: "Notes say
where labels come from: humans, exact rules or an LLM teacher."

**This is the most useful third-party index we have seen, and it also contains the cleanest
example of how a barred lineage gets laundered.**

## Where it agrees with our record

| Item | Collection's note | Our record |
| --- | --- | --- |
| `ZefanCai/Open-Jev`, `-v1.1` | "controlled synthetic, rule labels"; v1.1 adds 101k WANLI human rows | Sweep item 104, provenance *unclear*. The rule-label description is more specific than we had |
| `tasksource/procedural-typed-decisions` | "every answer is computed from rules stated in the state, so labels have no noise. Good for checking reasoning over state, not guessing" | Matches our T1 reasoning exactly, including why code-computed labels are fixture evidence |
| `Praveenrajus/jev-bench` | "human labels… some configs (chaosnli, 100 annotators per item) carry human label distributions, so you can test calibration, not only accuracy" | Already in the sweep. The annotator-distribution point is the same one our data protocol makes about multi-annotator targets |

## Where its notes understate what we already established

Two items carry generic teacher descriptions that our own sweep resolved to Jev:

- **`SargeDev/jev-distill-corpus-v3`** is noted as "TRAIN · LLM-teacher soft labels. 741k
  templated operational scenarios". Our sweep found that its `yuri_v3` split carries **Jev 1.13
  soft targets**, and traced three downstream projects harvesting it as a Jev-student path:
  `wfzyx/von` (`prepare_distill_dataset.py` at `ac9f3da996`), `autotrust/JEV`, and
  `ljwwwiop/JEV-mini`. Under §3.6 this corpus is **refused by default** for training, and so is
  anything inheriting from it.
- **`dylantom2012/open-system-one-bench`** is noted as "COMPARISON · per-item predictions from
  Jev, Laya and others". That is accurate, and it means the file **contains per-row Jev
  predictions**. As a comparison record it is fine; joined into training it is a barred path. The
  collection does not say that, because it is not the collection's job to.

**The lesson, and it is a design lesson rather than a criticism.** A careful curator labeling a
Jev-distilled corpus as "LLM-teacher" is exactly the laundering path §3.6's edges exist to catch:
the description is true at one level of abstraction and loses the fact that decides the verdict.
This is why the gate resolves lineage through declared parents rather than through a description,
and why `derived_from` is transitive.

- **`LocalLLaMA/typed-decisions`** is noted as "synthetic, soft labels" with no teacher named,
  which independently corroborates our **`disputed`** verdict: its gold is an unnamed ~4B teacher,
  a third-party README alleges Jev labelling, and neither is established.

## One operational win

`mteb/banking77` is "a Parquet copy of PolyAI/banking77 (the original has no viewer)". W2 had to
fetch BANKING77 as CSVs from GitHub's raw API at an immutable upstream commit, because HF's
`refs/convert/parquet` for the original 404s, and that required the only allowlist edit of the
window. If a future re-acquisition needs BANKING77, `mteb/banking77` is a Parquet route that avoids
the GitHub hop — **provided its hashes are checked against the pinned `dataset_infos.json` the way
the CSVs were**, since a convenience mirror is a new artifact with its own lineage.

## Disposition

**Index, not a source.** Nothing here becomes an M5 arm or changes one. Three concrete effects:

1. Two §3.6 test rows are added from real artifacts rather than invented ones: a corpus described
   as a generic LLM-teacher distillation whose declared parent is Jev must be **refused**, and an
   evaluation record holding per-row Jev predictions must be **refused when an edge reaches a
   training artifact and recorded when it does not**.
2. `mteb/banking77` is noted as a Parquet route for BANKING77, with the hash check required.
3. The collection is worth re-reading when it updates, because its label-source discipline makes
   it a cheap way to spot new corpora — while remembering that its notes are a curator's
   declaration, which is precisely what §3.6 says it can never take as verification.
