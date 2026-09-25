#!/usr/bin/env python3
"""The decision specs for M5's real-text tasks, in one versioned place.

A PAW program is compiled from a spec plus examples, and A1 is a program written against the same
spec. Keeping the specs here rather than in a notebook is what makes the two comparable: the arms
differ in artifact form, not in what they were told to do. The spec text is hashed into the export
bundle, so a compile that used different words is detectable.

Each spec says what the decision is, what the options are, and what the cost of being wrong is,
because the cost is part of the decision and not a scoring detail applied afterwards. None of them
mentions a model, a threshold or a rung.
"""

from __future__ import annotations

SPECS = {
    "T2a": {
        "task": "BANKING77 intent routing",
        "unit": "one customer query",
        "decision": "Route a banking customer's message to the team that handles it, or abstain.",
        "options": "one of the 77 BANKING77 intent labels, or `abstain`",
        "cost": {"misroute": 1.0, "abstain": 0.3, "correct": 0.0},
        "guidance": (
            "Abstaining costs less than routing to the wrong team but more than routing correctly, "
            "so abstain when the message does not clearly indicate one intent. Several intents are "
            "near-neighbours — card arrival, card delivery and card not working are different "
            "decisions — and the distinction is what the message asks for, not what it mentions."),
    },
    "T2b": {
        "task": "CLINC150 out-of-scope detection",
        "unit": "one customer query",
        "decision": "Decide whether a query is one the assistant serves, or is out of scope.",
        "options": "`in scope` or `out of scope`, or `abstain`",
        "cost": {"wrong": 1.0, "abstain": 0.3, "correct": 0.0},
        "guidance": (
            "Out of scope is a real answer, not a fallback for uncertainty: a query about a topic "
            "the assistant does not serve is out of scope even when it is perfectly clear. "
            "Abstaining is the separate answer for a query you cannot place at all, and it costs "
            "0.3 rather than 1.0. Most queries are in scope; the out-of-scope class is about one "
            "in eighteen."),
    },
    "T2c": {
        "task": "CivilComments toxicity",
        "unit": "one comment",
        "decision": "Decide whether a comment is toxic, where toxic means the corpus's own "
                    "toxicity annotation at or above 0.5.",
        "options": "`toxic` or `not toxic`",
        "cost": {"false_positive": 1.0, "false_negative": 4.0},
        "guidance": (
            "A missed toxic comment costs four times a false alarm, so the decision is not 'is this "
            "more likely toxic than not'. Quoting or describing toxicity is not the same as "
            "producing it, and disagreement, profanity and anger are not toxicity by themselves; "
            "the annotation tracks attacks on people."),
    },
}

ANSWER_SURFACE = {
    "T2a": {},
    "T2b": {"0": "in scope", "1": "out of scope"},
    "T2c": {"0": "not toxic", "1": "toxic"},
}
"""How a stored label value is written as an answer, per task.

This exists because M5's first grading found a defect that was mine, not any arm's. The T2c spec
above tells every arm the options are `toxic` or `not toxic`. The stored confirmation labels are
the integers 0 and 1. The scorer built its label set from the stored values, so the compiled
program obeyed the spec exactly and was graded 60,000 invalid outputs out of 60,000 — a perfect
score against the wrong vocabulary.

The arms that learn from fit examples were immune, because they copy whatever surface the fit
labels happen to use. The arms that read the spec were not. That asymmetry is a confound in the
comparison the experiment exists to make, so the surface is declared here, once, and both the
export and the scorer render through it. T2a is empty because its stored labels are already the
77 intent names the spec names.

T2b's polarity is not a guess from its minority count, which would have been the wrong way to
settle it. E1's design lock and the M4 partition receipt both state the rule that produced the
label: `intent = OOS class 42`, positive rate 0.05660 across 23,850 rows. So a stored 1 is the
out-of-scope class by construction, and the confirmation partition's 746 of 12,845 at 0.0581 is
that rate reappearing in a subset rather than the evidence for it. T2c's polarity has the same
kind of source: `toxicity >= 0.5` is the positive class, at 0.07991.

The T2b spec above was rewritten at the same time, because the surface fix exposed a second and
worse defect. It used to tell arms to answer with one of 150 in-scope intents, while the labels it
is graded against have only ever been binary. An arm that read that spec answered a question
nobody was scoring. That is not a vocabulary mismatch; it is the wrong task, and no mapping can
repair it — the arms that read it have to be run again.
"""


def surface(task: str, value) -> str:
    """The answer form of a stored label. Unmapped tasks keep the stored value."""
    return ANSWER_SURFACE.get(task, {}).get(str(value), str(value))


SPEC_VERSION = "m5-specs-3"
