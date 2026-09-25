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
        "task": "CLINC150 route-or-abstain with an out-of-scope class",
        "unit": "one customer query",
        "decision": "Route a query to an in-scope intent, or declare it out of scope.",
        "options": "one of the 150 in-scope intents, or `out of scope`",
        "cost": {"misroute": 1.0, "abstain": 0.3, "correct": 0.0},
        "guidance": (
            "Out of scope is a real answer, not a fallback for uncertainty: a query about a topic "
            "the assistant does not serve is out of scope even when it is perfectly clear. A query "
            "that is in scope but ambiguous between two intents is a different case, and abstaining "
            "there costs 0.3 rather than 1.0."),
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

T2b is deliberately absent. Its stored labels are two integers, which means the task is binary
in-scope/out-of-scope as E1 built it, and not the 151-way routing the spec above describes. Which
integer is out of scope is not recorded anywhere in this repository, and guessing would invert the
task. It stays unmapped, and the scorer refuses T2b rather than assuming a polarity.
"""


def surface(task: str, value) -> str:
    """The answer form of a stored label. Unmapped tasks keep the stored value."""
    return ANSWER_SURFACE.get(task, {}).get(str(value), str(value))


SPEC_VERSION = "m5-specs-2"
