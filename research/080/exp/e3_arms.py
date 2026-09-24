#!/usr/bin/env python3
"""E3 arms and utilities, in one place so the search and confirmation halves cannot drift apart.

Runs as `augctl`, because computing EM needs the gold answer. It reads a frozen replay table and
the retained answers and produces, per question, each arm's stopping decision and its utility.

The seven arms of the design lock:

  (i)   implicit    follow the reader's own stop / expand / abstain choice
  (ii)  answerable  stop when p_answerable clears a threshold
  (iii) similarity  stop when the MiniLM cosine clears a threshold
  (iv)  composite   stop when the mean of the two clears a threshold
  (v)   constants   always stop at a fixed k, with no evidence read at all
  (vi)  proxy       a signal AND threshold chosen on the search split WITHOUT outcomes
  (vii) outcome     a threshold chosen on the search split WITH outcomes

(vi) and (vii) are the P5 contrast, and the difference between them is the whole question: (vi)
may look at anything except the gold answer, (vii) may look at the utility it is trying to
maximize. Keeping the proxy honest is therefore this module's main obligation, and it is easy to get wrong
in two ways at once. The proxy must be label-free in its WHOLE procedure, signal included, not
merely in its last step; and it must not be a quantity that a trivial policy maximizes. The proxy
here is agreement with a majority answer across the three k levels, priced with the same round
penalty as the real utility, which satisfies both.

U = EM − λ·rounds/3, clipped to [−0.2, 1], with λ = 0.1 and μ = 0 from the design lock. Abstaining
scores EM = 0 and still pays for the rounds it used, because an episode that read two paragraphs
and gave up consumed the same evidence as one that answered.
"""

from __future__ import annotations

import re
import string
import unicodedata

K_LEVELS = (2, 4, 6)
LAMBDA = 0.1
UTILITY_CLIP = (-0.2, 1.0)
ARTICLES = {"a", "an", "the"}


def normalize_answer(text: str) -> str:
    """HotpotQA's own normalization: lowercase, drop articles and punctuation, collapse space."""
    text = unicodedata.normalize("NFKC", text).lower()
    text = "".join(" " if char in string.punctuation else char for char in text)
    tokens = [token for token in text.split() if token not in ARTICLES]
    return " ".join(tokens)


def exact_match(predicted: str, gold: str) -> int:
    return int(normalize_answer(predicted) == normalize_answer(gold))


def utility(em: int, rounds: int) -> float:
    value = em - LAMBDA * rounds / 3
    return min(max(value, UTILITY_CLIP[0]), UTILITY_CLIP[1])


def composite_score(cell: dict) -> float:
    """The mean of answerability and similarity. Both already live in [0, 1]."""
    return (cell["p_answerable"] + cell["similarity"]) / 2


SIGNALS = {
    "answerable": lambda cell: cell["p_answerable"],
    "similarity": lambda cell: cell["similarity"],
    "composite": composite_score,
}


def run_threshold(row: dict, signal, threshold: float) -> tuple[str, int, bool]:
    """Stop at the first k whose signal clears the threshold; otherwise answer at the last k.

    Returns the answer, the number of rounds used and whether the episode abstained. A threshold
    policy never abstains: abstention is arm (i)'s option, because it is the reader's own choice,
    and giving the threshold arms a second free parameter would make the comparison something
    other than what the lock registered.
    """
    for index, k in enumerate(K_LEVELS, start=1):
        cell = row["k"][str(k)]
        if signal(cell) >= threshold or k == K_LEVELS[-1]:
            return cell["answer"], index, False
    raise AssertionError("unreachable: the last k always returns")


def run_implicit(row: dict) -> tuple[str, int, bool]:
    """Follow the reader's own action, which is the endogenous arm."""
    for index, k in enumerate(K_LEVELS, start=1):
        cell = row["k"][str(k)]
        action = cell["action"]
        if action == "abstain":
            return "", index, True
        if action == "stop" or k == K_LEVELS[-1]:
            return cell["answer"], index, False
    raise AssertionError("unreachable")


def run_constant(row: dict, k: int) -> tuple[str, int, bool]:
    """Always stop at a fixed k. Reads no signal, which is the point of the baseline."""
    index = K_LEVELS.index(k) + 1
    return row["k"][str(k)]["answer"], index, False


def pseudo_label(row: dict) -> str:
    """A label-free stand-in for the answer: the majority answer across the three k levels.

    An earlier version used the k = 6 answer, and it was degenerate: agreement with the
    maximal-evidence answer is maximized by reading the maximal evidence, so the proxy collapsed
    onto the constant-k6 arm and two of the three contrasts per reader became the same contrast.
    A majority across levels has no such built-in preference — stopping early can agree with it —
    so the proxy can prefer a cheaper policy when the evidence supports one.

    Ties break toward the answer seen at the smallest k, which is deterministic and does not
    reintroduce a preference for more evidence.
    """
    answers = [row["k"][str(k)]["answer"] for k in K_LEVELS]
    normalized = [normalize_answer(answer) for answer in answers]
    best, best_count = normalized[0], 0
    for candidate in normalized:
        count = normalized.count(candidate)
        if count > best_count:
            best, best_count = candidate, count
    return best


def agrees_with_pseudo_label(row: dict, answer: str) -> int:
    """The proxy's stand-in for EM. No gold answer is involved anywhere in its computation."""
    return int(normalize_answer(answer) == pseudo_label(row))


def evaluate(rows: dict, gold: dict, policy) -> dict:
    """One arm over every question: per-question utility, plus what it did to get there."""
    utilities, rounds_used, abstentions, matches = {}, {}, 0, 0
    proxy_utilities, proxy_matches = {}, 0
    for key, row in rows.items():
        answer, rounds, abstained = policy(row)
        em = 0 if abstained else exact_match(answer, gold[key])
        proxy_em = 0 if abstained else agrees_with_pseudo_label(row, answer)
        utilities[key] = utility(em, rounds)
        proxy_utilities[key] = utility(proxy_em, rounds)
        rounds_used[key] = rounds
        abstentions += abstained
        matches += em
        proxy_matches += proxy_em
    n = len(utilities)
    return {
        "n": n,
        "mean_utility": sum(utilities.values()) / n,
        "exact_match": matches / n,
        "mean_rounds": sum(rounds_used.values()) / n,
        "abstention_rate": abstentions / n,
        "proxy_agreement": proxy_matches / n,
        "proxy_mean_utility": sum(proxy_utilities.values()) / n,
        "per_question": utilities,
    }


def sweep(rows: dict, gold: dict, signal_name: str, grid) -> list[dict]:
    """Every threshold on the grid, with both the outcome score and the label-free proxy.

    Selecting on `mean_utility` is arm (vii); selecting on `proxy_mean_utility` is arm (vi).
    Running one sweep and reading two columns from it is what makes the two arms differ in exactly
    one respect, which is the comparison P5 is about. The proxy column prices rounds exactly as the
    real one does, so a proxy that preferred more evidence would have to pay for it.
    """
    signal = SIGNALS[signal_name]
    results = []
    for threshold in grid:
        summary = evaluate(rows, gold, lambda row, t=threshold: run_threshold(row, signal, t))
        summary.pop("per_question")
        results.append({"signal": signal_name, "threshold": threshold, **summary})
    return results
