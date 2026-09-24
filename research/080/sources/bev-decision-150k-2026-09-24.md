# BEV 150K Decision Mix — card (2026-09-24)

`avbiswas/bev-decision-150K` on Hugging Face. 150,000 English decision rows (train 125,614, test
24,386), Parquet, **license: unknown**. Read from the dataset card and the viewer's schema;
nothing downloaded and no row used. Figures are **Reported**.

A training mixture of bounded decisions in the Choice / Noul / Score shape: 296,582 questions over
150,000 rows, 40.7% Choice, 39.9% Noul, 19.4% Score, across 18 domains. The card is unusually
candid — it names which slices were LLM-rewritten, says the test split is a held-out portion of the
mixture rather than an independent benchmark, and warns that several labels mean less than their
names suggest.

## The finding that matters to us is a contamination boundary, not a capability

**Three of its eighteen domains are built from the corpora E1 and M5 use.** The card lists
CivilComments in the sentiment/moderation domain (25,156 rows), and CLINC150 and BANKING77 in
support and intent routing (12,656 rows). E1's confirmation split is CivilComments and CLINC150;
M5's T2a is BANKING77 and T2b reuses E1's CLINC partition.

So any model trained on this mixture has plausibly seen our confirmation rows, and our seeded
partitions give no protection against that: the leak is upstream of the partitioner. This does not
touch E1's completed result, which used a MiniLM encoder we fit ourselves. It constrains what may
be admitted later.

**Gate, recorded here so it is findable at M5 rather than rediscovered:** a candidate model whose
training data includes, or plausibly includes, this mixture cannot be scored on E1's or M5's
CivilComments, CLINC150 or BANKING77 splits and have the result read as held-out. Either the
candidate declares its corpora and is checked, or the result is reported as contaminated. The
dataset card asks for the same thing in the other direction: "evaluating on those same public
benchmarks requires checking record and source-family overlap first."

## Other limits worth carrying

- **No blanket license.** The card asserts none and uses `unknown` deliberately, flagging
  ProofWriter's unclear redistribution, third-party-authored NVD descriptions and Reddit-derived
  GoEmotions text. Redistribution or commercial use would require clearing each upstream source.
- **A 20,000-row slice had its questions rewritten by GPT-6 Luna**, with source-backed labels kept.
  The model authored no primary passages, but some upstream corpora are themselves synthetic or
  template-generated, so this is not a human-written corpus.
- **Score labels are ordinal indices, not calibrated probabilities**, which the card states
  outright. Neither the test split nor the Score outputs imply real-world calibration.
- Some choice alternatives are sampled or constructed and answer frequencies were rebalanced, so
  base rates in the mixture are not base rates anywhere.

## Disposition

**Discovery record and a contamination gate. Not a corpus we adopt, not an M5 arm, not a source of
training data here.** Nothing in it changes a lock. Its value is that it tells us, in advance and
in the publisher's own words, which of our evaluation corpora have been swept into a public
training mixture — which is the sort of thing that is much cheaper to know now than after a
candidate scores suspiciously well.
