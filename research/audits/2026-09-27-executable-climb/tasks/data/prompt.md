# Build a first-message dataset

Implement `solution.py` using Python's standard library. Export
`prepare(rows, train_end, dev_end)` and a CLI reading one JSON object on stdin
with those three arguments and writing its returned object as JSON to stdout.
You may write and run local checks. Do not download packages or use a network.

We route a new customer's first message. The export mixes user and staff events,
late labels, and duplicate messages. Return `{"train": [...], "dev": [...],
"confirm": [...]}`. Each example must contain exactly `id` (ticket ID),
`customer`, `text`, and `label`. No other export fields may enter the artifact.

Rows have `ticket`, `customer`, `time`, `role` (`user` or `staff`), `text`,
`label`, `label_time`, and `label_status` (`agreed` or `disputed`), possibly other
post-routing columns. Times are ISO dates (`YYYY-MM-DD`); row order is arbitrary.
For each ticket choose its earliest user event (equal times: lexicographically
smallest text). A later reply must never replace an unusable first user event.
Assume a ticket's customer is consistent. Its label/status/time come from that
chosen row. Reject the ticket if its text is empty after whitespace stripping,
label is null, or label_status is not agreed. Preserve the original nonempty
text, not its normalized comparison key.

The provisional role is train for time < train_end, dev for
train_end <= time < dev_end, confirm otherwise. Training labels must be available
strictly before train_end; dev labels strictly before dev_end. Confirmation
labels may arrive later. An unavailable label excludes that ticket; do not move
it to a later partition just to retain it.

Among eligible tickets, bind together tickets sharing either customer or equal
text after case-folding and collapsing all whitespace. These relationships are
transitive. For each connected component keep tickets only from its earliest
provisional role, dropping its tickets in later roles. This prioritizes earlier
data while making later roles unseen-customer/duplicate groups. Same-role members
remain separate examples. Sort each output partition by ticket ID.

Deliver executable code, run representative checks, and state what you verified.
