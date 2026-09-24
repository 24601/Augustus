#!/usr/bin/env python3
"""Resolve declared data provenance for one training artifact; never fetch or train.

Input is one JSON graph with schema_version=1, a training_artifact id, nodes,
edges, and optional approvals. Nodes have a unique id, a kind, and their own
declarations. Edges point from a derived node to the parent it came from, so
walking edges from the training artifact reaches everything that fed it.

Node kinds: row, text, label, feature, filter_decision, selection_decision,
dataset, corpus, checkpoint, prompt, external_model.

Edge types: generated_by, labeled_by, filtered_by, selected_by, featurized_by,
rewarded_by, preferred_by, relabeled_by, derived_from, trained_on, accessed_via.
Reward, preference and relabel edges exist because using a model's output as an
RL reward, as a preference pair, or to relabel states a student visited is a
training use, not an evaluation use.

What this decides
-----------------
Identity resolves by DECLARED LINEAGE, never by a name substring. A model named
"Jev-Omni" whose declared base is Gemma is not TypeSafe; a human label stored in
a field named "jev" is a human label.

Verdicts per reachable node:
  refused   a TypeSafe/Jev output feeds the training artifact. Refused by
            default; one recorded acknowledgment (artifact, use, date) clears
            one use, which is the user's decision to make and to own.
  disputed  a sourced, revision-bound allegation contradicts a declared
            lineage. Blocked for training use pending resolution. An approval
            preserves the allegation and never reports it as cleared.
  unknown   a parent is missing, or a teacher is unnamed, so nothing can be
            recorded and the corpus cannot be re-audited later.
  recorded  a named hosted non-TypeSafe model. It PASSES: provider, model,
            revision, channel and date are written down and nothing is gated.
  allowed   a permission record with its url, digest and clause.

What this does NOT decide
-------------------------
It checks declared provenance only. It reads no provider's terms except that
TypeSafe's are the one encoded rule, it fetches nothing, and it verifies no
claim any declaration makes. A pass is an audit trail, not a permission: the
terms question for a non-TypeSafe provider belongs to whoever runs the job.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path

SCHEMA_VERSION = 1

NODE_KINDS = frozenset({
    "row", "text", "label", "feature", "filter_decision", "selection_decision",
    "dataset", "corpus", "checkpoint", "prompt", "external_model",
})

# Every edge type is a training use when it reaches the training artifact.
EDGE_TYPES = frozenset({
    "generated_by", "labeled_by", "filtered_by", "selected_by", "featurized_by",
    "rewarded_by", "preferred_by", "relabeled_by", "derived_from", "trained_on",
    "accessed_via",
})

# The single encoded provider rule. Matched on the DECLARED provider id, not on
# a model name, an alias, or any substring of one.
TYPESAFE_PROVIDER_IDS = frozenset({"typesafe", "typesafe.ai"})
TYPESAFE_CLAUSE = "TypeSafe Master Customer Agreement section 2.3(b)"


class GraphError(ValueError):
    """A malformed graph. Distinct from a provenance verdict."""


@dataclass
class Finding:
    node: str
    verdict: str
    reason: str
    detail: dict = field(default_factory=dict)

    def as_dict(self) -> dict:
        return {"node": self.node, "verdict": self.verdict, "reason": self.reason, **self.detail}


def _object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise GraphError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise GraphError(f"{name} must be nonempty text")
    return value


def _nodes(document):
    raw = document.get("nodes")
    if not isinstance(raw, list) or not raw:
        raise GraphError("nodes must be a nonempty list")
    nodes = {}
    for index, node in enumerate(raw):
        if not isinstance(node, dict):
            raise GraphError(f"node {index} must be an object")
        identity = _text(node.get("id"), f"node {index} id")
        if identity in nodes:
            raise GraphError(f"duplicate node id: {identity}")
        kind = node.get("kind")
        if kind not in NODE_KINDS:
            raise GraphError(f"node {identity} kind must be one of {sorted(NODE_KINDS)}")
        nodes[identity] = node
    return nodes


def _edges(document, nodes):
    raw = document.get("edges")
    if raw is None:
        raw = []
    if not isinstance(raw, list):
        raise GraphError("edges must be a list")
    parents: dict[str, list[tuple[str, str]]] = {identity: [] for identity in nodes}
    dangling: dict[str, list[str]] = {}
    for index, edge in enumerate(raw):
        if not isinstance(edge, dict):
            raise GraphError(f"edge {index} must be an object")
        kind = edge.get("type")
        if kind not in EDGE_TYPES:
            raise GraphError(f"edge {index} type must be one of {sorted(EDGE_TYPES)}")
        source = _text(edge.get("from"), f"edge {index} from")
        target = _text(edge.get("to"), f"edge {index} to")
        if source not in nodes:
            raise GraphError(f"edge {index} from unknown node: {source}")
        if target not in nodes:
            # A named but absent parent is a lineage gap, not a malformed graph.
            dangling.setdefault(source, []).append(target)
            continue
        parents[source].append((kind, target))
    return parents, dangling


def _approval_index(document):
    raw = document.get("approvals")
    if raw is None:
        raw = []
    if not isinstance(raw, list):
        raise GraphError("approvals must be a list")
    index: dict[tuple[str, str], dict] = {}
    for position, approval in enumerate(raw):
        if not isinstance(approval, dict):
            raise GraphError(f"approval {position} must be an object")
        node = _text(approval.get("node"), f"approval {position} node")
        use = _text(approval.get("use"), f"approval {position} use")
        _text(approval.get("date"), f"approval {position} date")
        kind = approval.get("kind")
        if kind not in ("acknowledgment", "named_approval"):
            raise GraphError(f"approval {position} kind must be acknowledgment or named_approval")
        index[(node, use)] = approval
    return index


def _classify_external_model(node) -> Finding:
    """Resolve one external model by its declarations.

    Never by name: the caller's `id` and any model name are ignored here except
    as labels in the output.
    """
    identity = node["id"]
    provider = node.get("provider")
    model = node.get("model")
    revision = node.get("revision")
    channel = node.get("channel")
    declared = {"provider": provider, "model": model, "revision": revision, "channel": channel}
    if isinstance(provider, str) and provider.strip().lower() in TYPESAFE_PROVIDER_IDS:
        return Finding(identity, "refused", "typesafe_output_in_training_path",
                       {"clause": TYPESAFE_CLAUSE, "declared": declared,
                        "override": "one recorded acknowledgment (node, use, date) clears one use"})
    missing = [name for name, value in declared.items()
               if not isinstance(value, str) or not value.strip()]
    if missing:
        return Finding(identity, "unknown", "external_model_not_fully_named",
                       {"missing": missing, "declared": declared,
                        "note": "an unnamed teacher cannot be recorded, so the corpus cannot be re-audited"})
    return Finding(identity, "recorded", "named_external_model_recorded",
                   {"declared": declared,
                    "note": "declared provenance only; no provider terms are read or asserted except TypeSafe's"})


def _classify_permission(node) -> Finding | None:
    permission = node.get("permission")
    if permission is None:
        return None
    if not isinstance(permission, dict):
        raise GraphError(f"node {node['id']} permission must be an object")
    required = ("url", "digest", "clause")
    missing = [name for name in required
               if not isinstance(permission.get(name), str) or not permission[name].strip()]
    if missing:
        return Finding(node["id"], "rejected_permission", "permission_record_incomplete",
                       {"missing": missing})
    return Finding(node["id"], "allowed", "permission_record_complete",
                   {"clause": permission["clause"], "digest": permission["digest"]})


def _classify(node, dangling) -> list[Finding]:
    """Every verdict one node earns. A node can be both disputed and unknown."""
    identity = node["id"]
    findings: list[Finding] = []

    disputes = node.get("disputes")
    if disputes is not None:
        if not isinstance(disputes, list) or not disputes:
            raise GraphError(f"node {identity} disputes must be a nonempty list when present")
        for position, dispute in enumerate(disputes):
            if not isinstance(dispute, dict):
                raise GraphError(f"node {identity} dispute {position} must be an object")
            source = _text(dispute.get("source"), f"node {identity} dispute {position} source")
            revision = _text(dispute.get("revision"), f"node {identity} dispute {position} revision")
            claim = _text(dispute.get("claim"), f"node {identity} dispute {position} claim")
            findings.append(Finding(identity, "disputed", "sourced_allegation_against_declared_lineage",
                                    {"source": source, "revision": revision, "claim": claim}))

    permission = _classify_permission(node)
    if permission is not None:
        findings.append(permission)

    if node["kind"] == "external_model":
        findings.append(_classify_external_model(node))

    absent = dangling.get(identity)
    if absent:
        findings.append(Finding(identity, "unknown", "declared_parent_absent_from_graph",
                                {"missing_parents": sorted(absent)}))
    if node.get("parents_complete") is False:
        findings.append(Finding(identity, "unknown", "parents_declared_incomplete", {}))
    return findings


def resolve(document) -> dict:
    if not isinstance(document, dict):
        raise GraphError("document must be an object")
    if type(document.get("schema_version")) is not int or document["schema_version"] != SCHEMA_VERSION:
        raise GraphError(f"schema_version must be integer {SCHEMA_VERSION}")
    use = _text(document.get("use"), "use")
    artifact = _text(document.get("training_artifact"), "training_artifact")
    nodes = _nodes(document)
    if artifact not in nodes:
        raise GraphError(f"training_artifact is not a node: {artifact}")
    parents, dangling = _edges(document, nodes)
    approvals = _approval_index(document)

    # Ancestors of the training artifact, in discovery order. Cycles are
    # tolerated: a visited set means a declared cycle cannot hang the gate.
    order: list[str] = []
    seen = {artifact}
    stack = [artifact]
    paths: dict[str, list[str]] = {artifact: [artifact]}
    while stack:
        current = stack.pop()
        order.append(current)
        for kind, parent in parents[current]:
            if parent not in seen:
                seen.add(parent)
                paths[parent] = paths[current] + [f"-{kind}->", parent]
                stack.append(parent)

    findings: list[Finding] = []
    for identity in order:
        for finding in _classify(nodes[identity], dangling):
            finding.detail["path_to_training_artifact"] = paths[finding.node]
            findings.append(finding)

    refused, disputed, unknown, rejected = [], [], [], []
    acknowledged = []
    for finding in findings:
        if finding.verdict == "refused":
            approval = approvals.get((finding.node, use))
            if approval is not None and approval["kind"] == "acknowledgment":
                finding.detail["acknowledged"] = {
                    "date": approval["date"], "use": use,
                    "note": "the user recorded this override; it is their decision and their record",
                }
                acknowledged.append(finding)
            else:
                refused.append(finding)
        elif finding.verdict == "disputed":
            approval = approvals.get((finding.node, use))
            if approval is not None:
                # An approval never reports an allegation as cleared.
                finding.detail["approval_does_not_clear_the_allegation"] = {
                    "kind": approval["kind"], "date": approval["date"],
                }
            disputed.append(finding)
        elif finding.verdict == "unknown":
            unknown.append(finding)
        elif finding.verdict == "rejected_permission":
            rejected.append(finding)

    if refused:
        assessment = "refused"
    elif rejected:
        assessment = "rejected_permission_record"
    elif disputed:
        assessment = "blocked_pending_dispute_resolution"
    elif unknown:
        assessment = "unknown_lineage"
    else:
        assessment = "declared_provenance_recorded"

    return {
        "schema_version": SCHEMA_VERSION,
        "use": use,
        "training_artifact": artifact,
        "reachable_nodes": len(order),
        "assessment": assessment,
        "findings": [finding.as_dict() for finding in findings],
        "overridden_by_user_acknowledgment": [finding.as_dict() for finding in acknowledged],
        "limits": [
            "Declared provenance only. Nothing here is fetched, verified, or attested.",
            "Identity resolves by declared lineage; a matching name never establishes identity, and a name never establishes a refusal.",
            f"The one encoded provider rule is TypeSafe's ({TYPESAFE_CLAUSE}). No other provider's terms are read or asserted; a recorded teacher is an audit trail, not a permission.",
            "An acknowledgment records a user's own override of the TypeSafe rule for one artifact and one use. It is not advice and it is not a clearance.",
            "An approval never clears a sourced allegation; the allegation stays in the record.",
            "A pass does not establish label quality, sampling design, isolation, or causal identification.",
        ],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("graph", type=Path, help="declared provenance graph JSON")
    args = parser.parse_args(argv)
    try:
        raw = args.graph.read_bytes()
        document = json.loads(raw, object_pairs_hook=_object)
        result = resolve(document)
        result["input_sha256"] = hashlib.sha256(raw).hexdigest()
        print(json.dumps(result, indent=2, allow_nan=False))
    except (OSError, ValueError, RecursionError) as exc:
        parser.exit(2, f"error: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
