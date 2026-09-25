#!/usr/bin/env python3
"""A1: the agent-synthesized programs. Deterministic code, frozen and hashed before confirmation.

The design lock's A1 is "an agent writes deterministic code; the artifact is frozen and hashed
before any confirmation read, so the agent is not in the loop at acceptance". These are those
programs. They are written to be read: no weights, no fitted coefficients, no lookup table built
from labelled data.

That last restriction is the whole point and is easy to lose. A program whose rules were tuned on
the fit labels is a fitted model wearing a program's clothes, and it would beat a real program for
reasons that have nothing to do with artifact form. So the routing programs derive their cues from
the **label names themselves**, which are part of the task definition rather than the data, and
the toxicity program uses a hand-written lexicon with hand-written structure. Both read the fit
examples for nothing at all.

They are expected to lose on real text. Plan v4's P11 says so in advance — "programs lose on fuzzy
real text" — and stating it beforehand is what stops a poor result being explained away afterwards.
"""

from __future__ import annotations

import re
import unicodedata

ABSTAIN = "abstain"
OUT_OF_SCOPE = "out of scope"

# Hand-written, not fitted. Attacks on a person, which is what the CivilComments annotation tracks,
# rather than profanity, disagreement or anger, which it does not.
ATTACK_CUES = {
    "idiot", "idiots", "moron", "morons", "stupid", "dumb", "dumbass", "imbecile", "fool",
    "loser", "losers", "pathetic", "scum", "trash", "garbage", "worthless", "disgusting",
    "shut up", "go to hell", "you people", "coward", "cowards", "liar", "liars", "hypocrite",
    "bigot", "racist", "sexist", "nazi", "clown", "clowns", "troll", "parasite", "vermin",
}
PROFANITY = {"damn", "hell", "crap", "shit", "fuck", "fucking", "ass", "bastard"}
QUOTING = ("said", "wrote", "quote", "quoting", "claims", "according to", '"', "“")
NEGATIONS = ("not ", "n't ", "never ", "no one is ", "nobody is ")


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", str(text)).lower()
    return re.sub(r"\s+", " ", text).strip()


def tokens_of(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", normalize(text))


def label_cues(label: str) -> set[str]:
    """The cues a label name itself provides. No labelled example is consulted."""
    parts = re.split(r"[^a-z0-9]+", str(label).lower())
    cues = {part for part in parts if len(part) > 2}
    # A handful of obvious morphological variants, written out rather than stemmed, so the rule
    # stays readable and its behaviour is obvious from the source.
    for part in list(cues):
        if part.endswith("s"):
            cues.add(part[:-1])
        else:
            cues.add(part + "s")
        if part.endswith("e"):
            cues.add(part + "d")
    return cues


def routing_program(labels: list[str], fallback: str):
    """Score each label by how much of its own name the message echoes, or fall back.

    The cost matrix makes the fallback cheap relative to a wrong route — abstaining costs 0.3
    where a misroute costs 1.0 — so the rule refuses whenever the best label has no clear lead.
    That threshold is a judgement written into the program, not a number fitted to anything.
    """
    cue_table = {label: label_cues(label) for label in labels}

    def decide(text: str) -> str:
        words = set(tokens_of(text))
        if not words:
            return fallback
        scored = []
        for label, cues in cue_table.items():
            hits = len(words & cues)
            if hits:
                # Longer label names are easier to hit by accident, so normalize by cue count.
                scored.append((hits / (len(cues) ** 0.5), label))
        if not scored:
            return fallback
        scored.sort(reverse=True)
        best_score, best_label = scored[0]
        runner_up = scored[1][0] if len(scored) > 1 else 0.0
        if best_score <= 0.0 or best_score - runner_up < 1e-9:
            return fallback
        return best_label

    return decide


def toxicity_program(labels: list[str]):
    """Attack cues, discounted for quotation and negation, with the 1:4 cost asymmetry applied.

    A missed toxic comment costs four times a false alarm, so a single clear attack cue is enough
    and profanity alone is not. Quoting someone else's words, and negating a slur, both reduce the
    evidence rather than eliminating it — a comment can quote an attack and endorse it.
    """
    toxic = next((label for label in labels if str(label).lower() in
                  ("1", "true", "toxic", "yes")), labels[-1])
    clean = next((label for label in labels if label != toxic), labels[0])

    def decide(text: str) -> str:
        body = normalize(text)
        words = set(tokens_of(body))
        hits = sum(1 for cue in ATTACK_CUES if (" " in cue and cue in body) or cue in words)
        if not hits:
            return clean
        evidence = float(hits)
        if any(marker in body for marker in QUOTING):
            evidence -= 0.5
        if any(negation in body for negation in NEGATIONS):
            evidence -= 0.5
        if words & PROFANITY and hits == 1:
            # Profanity beside a single borderline cue is weak evidence, not strong.
            evidence -= 0.25
        # The 1:4 asymmetry: half a unit of surviving evidence is enough to call it toxic.
        return toxic if evidence >= 0.5 else clean

    return decide


# Topics a banking-and-utility assistant does not serve. Hand-written from CLINC's own domain
# description, in the same spirit as ATTACK_CUES: no fit example was read to build it.
OUT_OF_DOMAIN_CUES = {
    "weather", "forecast", "rain", "snow", "temperature outside",
    "joke", "funny", "riddle", "sing", "poem", "story",
    "president", "election", "politics", "senator", "war",
    "recipe", "cook", "bake", "pizza", "restaurant menu",
    "movie", "film", "actor", "song", "lyrics", "album",
    "sports", "football", "basketball", "score of the game", "world cup",
    "translate", "spanish for", "french for", "how do you say",
    "meaning of life", "are you human", "do you love me", "your favorite",
    "math problem", "square root", "who won", "capital of",
}


def out_of_scope_program(labels: list[str]):
    """Is this a query the assistant serves at all? Written after the binary task was found.

    T2b's spec used to say the answer was one of 150 in-scope intents, and this task's program was
    a router over label names because of it. The stored labels have only ever been binary, so that
    router had nothing to route to: cues drawn from the names `0` and `1` are empty, every row fell
    through to the fallback, and A1 answered `out of scope` 12,845 times out of 12,845. That is a
    program written against a spec that misdescribed the task, not a measure of what a hand-written
    program can do here.

    A binary decision offers a rule-writer no label names to work from, so this one goes the other
    way: assume in scope, which is right about seventeen times in eighteen, and name the
    out-of-domain topics explicitly. It is a lexicon and a prior, and it is expected to be poor —
    P11 says programs lose on fuzzy real text, and being specific about how they lose is the point.
    """
    out_of_scope = next((label for label in labels if "out" in str(label).lower()), OUT_OF_SCOPE)
    in_scope = next((label for label in labels if label != out_of_scope), "in scope")

    def decide(text: str) -> str:
        body = normalize(text)
        words = set(tokens_of(body))
        for cue in OUT_OF_DOMAIN_CUES:
            if (cue in body) if " " in cue else (cue in words):
                return out_of_scope
        return in_scope

    return decide


PROGRAMS = {
    "T2a": lambda labels: routing_program([l for l in labels if l != ABSTAIN], ABSTAIN),
    "T2b": out_of_scope_program,
    "T2c": toxicity_program,
}


def program_for(task: str, labels: list[str]):
    if task not in PROGRAMS:
        raise SystemExit(f"A1 has no program for {task}")
    return PROGRAMS[task](list(labels))


def source_of(task: str) -> str:
    """The bytes that get hashed: this whole file plus the task name.

    Hashing the file rather than a closure is the honest choice — the behaviour of a program
    depends on every rule in it, including the shared lexicons, so a change anywhere should change
    the hash.
    """
    from pathlib import Path
    return f"{task}\n" + Path(__file__).read_text(encoding="utf-8")
