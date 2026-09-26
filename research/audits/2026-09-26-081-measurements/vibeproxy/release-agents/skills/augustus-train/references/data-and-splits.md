# Turn records into a defensible training set

**Placement:** before fitting or collecting more examples. This is a proposed
workflow, not evidence that a particular dataset is representative. Its
assumption is that the target can be labeled or observed with useful reliability.
If adjudicators cannot distinguish the target from missing evidence, improve the
task definition or defer that action instead of forcing a classifier to learn it.

## Define the label before cleaning away inconvenient records

Start with a small, varied sample of the raw records. Write an annotation guide
with inclusion/exclusion rules, decision-time evidence, positive and negative
examples, boundary cases, and a version. For a rating, define each level; for
regression, units and observation horizon; for ranking, the query and relevance
criterion. An observed action is not necessarily the correct label. A ticket
escalated by the old router may reflect its bias, not a need for escalation.

Use an application-owned record like this; fields are a design example, not a
schema imposed by a helper:

```json
{
  "id": "case-017", "group": "account-008",
  "event_time": "2026-08-01T09:00:00Z",
  "label_observed_at": "2026-08-04T09:00:00Z",
  "text": "Customer report visible before routing",
  "label": "review", "label_status": "adjudicated",
  "label_definition": "escalation-v2", "source_revision": "export-v3",
  "annotation_ids": ["annotation-031", "annotation-044"],
  "adjudication_id": "resolution-009", "evidence_kind": "adjudicated"
}
```

Double-label a targeted subset, including costly errors and disagreements, with
annotators initially independent of model predictions. Inspect disagreements by
class and cause; record both original judgments and the adjudicator's rationale.
Agreement alone is not truth. Repeated disagreement may mean the ontology needs
two labels, an explicit ambiguous state, or more evidence. Version corrections
and affected rows instead of silently overwriting history.

- **Missing label:** keep null and its reason; exclude from supervised loss unless
  the method explicitly handles unlabeled data. Never silently turn it negative.
- **Ambiguous label:** adjudicate, preserve a distribution for an appropriate loss,
  or retain it as a separate uncertainty slice. Do not conflate uncertain truth
  with the application's decision to abstain.
- **Partial observation:** delayed, censored and selectively reviewed cases need
  an observation policy. A missing outcome for an action never taken is not its
  failure. State which population the observed labels can support.
- **No matching option:** distinguish open-set `none` from insufficient evidence
  and from malformed output. Add examples of each relevant condition.

## Audit what the application can actually see

Count records, independent groups, label statuses, classes, sources, languages,
lengths, times and exclusions. Inspect duplicates, conflicting labels and empty
inputs. Freeze a reversible normalization rule; preserve raw data in its approved
store. Remove identifiers or answer-bearing text only when the deployment input
also lacks them. Do not erase meaningful punctuation, case, negation or units by
habit. Redact private fields before any authorized external upload.

Identify leakage such as resolution notes, future events, human routing decisions
and labels embedded in filenames. Build features from the decision-time view.
Fit vocabulary, imputation, scaling, embeddings that learn from task data, feature
selection and label-conditioned filters within training partitions only.
Cache keys need input hash, preprocessor and encoder revisions, not just row ID.

## Assign data roles at the real independence unit

1. Define the intended claim: new records from existing accounts, new accounts,
   later time periods, new sites, or unseen tasks. This determines the unit and
   exclusion boundary; there is no universally correct random row split.
2. Bind related cases before splitting: patient/account/thread, document chunks,
   query-item lists, duplicated events, translated/paraphrased originals, and
   synthetic siblings. Use group splits for new-group claims. Audit fuzzy/semantic
   duplication where exact checks cannot reveal it.
3. For a future-time claim, train before the cutoff and evaluate later; respect
   label-availability time and any purge/embargo window needed for overlapping
   outcomes. Recurring groups may be legitimate for a same-customer future claim,
   but must not be described as unseen-customer generalization.
4. Reserve **training**, **development/search**, and **confirmation** roles.
   A separate calibration/policy split is useful when fitting probability maps
   or selecting thresholds; it is not compulsory for deterministic rules or
   tiny exploratory datasets. Nested/grouped cross-validation or cross-fitting
   can use small development sets efficiently. It does not create a fresh final
   holdout after adaptive reuse.
5. Freeze IDs, groups, cutoffs, seeds, label-definition and normalization versions,
   and actual content hashes. Document missing classes and sample limitations.
   Use the same evaluation units for candidate and incumbent. Do not split until
   convenient scores appear, or duplicate rare rows across partitions.

The same search set can score many candidates: those scores guide development,
not confirmation. Keep confirmation labels/outcomes away from training, prompts,
teacher generation and reflection. Once inspected to make a change, that set is
development data for subsequent claims. If no independent sample is affordable,
report exploratory results and retain the incumbent rather than inventing certainty.

## Rare events need coverage without falsifying prevalence

Choose representative confirmation sampling for overall outcome loss and maintain
a separate challenge set for rare, severe, boundary and shifted cases. Report both.
Oversample rare classes for training when useful, recording weights and sampling
rates; reweight or select policy against deployment prevalence where justified.
A balanced training set's raw probability estimates need not match deployment.

For a stratified/oversampled evaluation, retain inclusion probabilities and use a
design-appropriate estimator and uncertainty calculation. The companion paired
helper's equal-probability bound is not that estimator. A slice with three positives
cannot establish a reliable recall floor; give counts and uncertainty, collect
more, or constrain the action. A large total row count does not fix this.

## Teacher and synthetic data have a different evidentiary role

Keep real, human-adjudicated, weak, teacher and synthetic labels distinguishable.
Record provider/model/revision, prompt, generation date/configuration, source
parents, filters, selection and relabeling, permission evidence and acquisition
cost. Measure valid-output rate, class mix, abstention, diversity and duplicate
families before scaling. Spot-check costly failures against independent labels.
Teacher agreement measures imitation, not application correctness.

Synthetic examples can target missing cases; they need not imitate deployment
frequency. Keep siblings together and do not generate from confirmation examples.
Filtering/selecting/rewarding with a teacher is also a training-data influence,
not just direct label generation. TypeSafe/Jev output has training restrictions;
verify applicable terms and authority before use. A recorded acknowledgment or
helper pass does not alter a provider's contract.

When lineage is material, run the companion
`scripts/provenance_gate.py`:

```sh
python3 "$AUGUSTUS/scripts/provenance_gate.py" lineage.json
```

Here and below, `AUGUSTUS` is the installed companion skill directory, not this
skill. Read `--help` before producing a graph. Its contract is `schema_version: 1`,
`training_artifact`, `nodes`, `edges` and optional `approvals`; edges go **derived
node → parent**. Node kinds include checkpoint, dataset, label, feature, prompt
and external_model. Edges such as `trained_on`, `labeled_by`, `selected_by` and
`filtered_by` include indirect training influences. It checks declarations, fetches
no terms, verifies no lineage and does not grant permission. Named non-TypeSafe
hosted models can be merely `recorded`, not legally cleared.

Known public-corpus overlap need not exclude a model from exploratory comparison
or exclude useful training data. Mark the specific overlap and the affected claim.
Such rows can measure behavior on those cases, but cannot serve as independent
generalization confirmation. Unknown pretraining lineage stays unknown. A local
split cannot undo upstream exposure; use newly collected or otherwise independent
confirmation for the claim that needs it.

## Run the overlap check when disjoint confirmation is claimed

Use the companion `scripts/overlap_audit.py` on a manifest you construct from
actual data, not a hand-written claim of separation:

```json
{
  "schema_version": 1,
  "partitions": [
    {"name": "fit", "items": [{"id": "a", "text": "First case", "group": "g1"}]},
    {"name": "confirm", "confirmation": true,
     "items": [{"id": "b", "text": "Second case", "group": "g2"}]}
  ]
}
```

```sh
python3 "$AUGUSTUS/scripts/overlap_audit.py" partitions.json
```

The helper checks cross-partition IDs, exact/caller-normalized text and declared
groups. At least one partition must declare confirmation. Items with neither text
nor group are unverifiable. It cannot discover translations, undeclared families,
pretraining overlap or future-information leakage. It flags shared groups even
when a same-group future-time design is intentional; document that design with
its own evidence rather than changing IDs to manufacture a clean result.

## Spend the next labeling hour where it can change the decision

Prioritize unresolved label definitions and suspected leakage first, then expensive
error slices, uncovered classes/modalities and representative drift. Disagreement,
uncertainty and novelty can guide acquisition, but uncertainty alone over-selects
noise and misses confidently wrong cases. Keep a random representative component,
deduplicate requests, and record selection reasons/propensities when available.
Allocate independent confirmation labels separately from active-learning labels.

**Falsifier:** if a corrected-label or targeted-data trial does not improve frozen
development loss/critical slices within budget, reject that acquisition hypothesis.
Do not relabel cases merely to agree with the candidate or call more teacher data
an improvement without independent checks.
