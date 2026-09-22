#!/usr/bin/env python3
"""Fast, structural checks for the published Augustus skill.

This deliberately validates repository structure and published metadata.  It
does not infer whether the prose makes a semantic claim correctly: that needs
review and evidence, not a literal-text gate.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import json
import re
import sys
from typing import Iterable
from urllib.parse import unquote, urlsplit

import yaml


SKILL_PATH = Path(".agents/skills/augustus/SKILL.md")
MARKETPLACE_PATH = Path(".claude-plugin/marketplace.json")
REFERENCE_DIR = SKILL_PATH.parent / "references"
MAX_SKILL_BYTES = 16_000
MAX_SKILL_LINES = 220
MAX_REFERENCE_BYTES = 18_000
MAX_REFERENCE_LINES = 400
MAX_REFERENCE_TOTAL_BYTES = 180_000
MIN_DUPLICATE_PARAGRAPH_CHARS = 160
MAX_DESCRIPTION_CHARS = 1_024
SKILL_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
SEMVER_RE = re.compile(
    r"^(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"
    r"(?:-(?:0|[1-9][0-9]*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
RUNTIME_RESEARCH_HEADING_RE = re.compile(
    r"^\s*(?:hourly\b|.*\bresearch\s+lock\b|.*\buniqueness\s+lock\b)", re.I
)
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
REFERENCE_PATH_RE = re.compile(r"(?<![A-Za-z0-9_.-])references/([A-Za-z0-9_.-]+\.md)(?![A-Za-z0-9_.-])")


@dataclass(frozen=True)
class Issue:
    code: str
    path: Path
    message: str

    def render(self, root: Path) -> str:
        try:
            display = self.path.relative_to(root)
        except ValueError:
            display = self.path
        return f"{display}: {self.code}: {self.message}"


def _issue(issues: list[Issue], code: str, path: Path, message: str) -> None:
    issues.append(Issue(code, path, message))


def _read(path: Path, issues: list[Issue]) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        _issue(issues, "missing-file", path, "required file is absent")
    except UnicodeDecodeError:
        _issue(issues, "invalid-utf8", path, "must be UTF-8 text")
    except OSError as exc:
        _issue(issues, "unreadable-file", path, f"cannot read required file: {exc}")
    return None


def _frontmatter(text: str, path: Path, issues: list[Issue]) -> dict | None:
    if not text.startswith("---\n"):
        _issue(issues, "frontmatter", path, "must start with YAML frontmatter")
        return None
    end = re.search(r"^---\s*$", text[4:], re.M)
    if end is None:
        _issue(issues, "frontmatter", path, "YAML frontmatter is not closed")
        return None
    try:
        parsed = yaml.safe_load(text[4 : 4 + end.start()])
    except yaml.YAMLError as exc:
        _issue(issues, "frontmatter", path, f"invalid YAML: {exc}")
        return None
    if not isinstance(parsed, dict):
        _issue(issues, "frontmatter", path, "frontmatter must be a mapping")
        return None
    return parsed


def _without_code(text: str) -> Iterable[tuple[int, str]]:
    """Yield Markdown lines outside fenced code blocks.

    Inline code is removed later for link scanning. This is intentionally a
    bounded Markdown scanner: it handles repository docs without treating
    prose-shaped text inside code examples as a link or heading.
    """
    fence: tuple[str, int] | None = None
    for number, line in enumerate(text.splitlines(), 1):
        found = FENCE_RE.match(line)
        if fence is not None:
            if (found and found.group(1)[0] == fence[0]
                    and len(found.group(1)) >= fence[1]
                    and not line[found.end():].strip()):
                fence = None
            continue
        if found:
            fence = (found.group(1)[0], len(found.group(1)))
            continue
        yield number, line


def _strip_inline_code(line: str) -> str:
    return re.sub(r"`+[^`]*`+", "", line)


def _markdown_destinations(text: str) -> Iterable[tuple[int, str]]:
    """Extract conventional inline Markdown destinations outside code blocks.

    Reference-style links are deliberately not supported; the public skill
    docs use inline links, and a future parser can replace this bounded scan if
    reference-style links become part of the published contract.
    """
    for number, raw_line in _without_code(text):
        line = _strip_inline_code(raw_line)
        index = 0
        while index < len(line):
            match = re.search(r"(?<!!)\[[^\]]*\]\(", line[index:])
            if match is None:
                break
            start = index + match.end()
            depth = 1
            cursor = start
            angle = False
            while cursor < len(line) and depth:
                char = line[cursor]
                if char == "<":
                    angle = True
                elif char == ">":
                    angle = False
                elif not angle and char == "(":
                    depth += 1
                elif not angle and char == ")":
                    depth -= 1
                cursor += 1
            if depth:
                break
            payload = line[start : cursor - 1].strip()
            if payload.startswith("<") and ">" in payload:
                destination = payload[1 : payload.index(">")]
            else:
                destination = payload.split(None, 1)[0] if payload else ""
            if destination:
                yield number, destination
            index = cursor


def _local_destination(destination: str) -> str | None:
    if destination.startswith("#"):
        return None
    parsed = urlsplit(destination)
    if parsed.scheme or destination.startswith("//"):
        return None
    return unquote(parsed.path)


def _check_links(boundary: Path, path: Path, text: str, issues: list[Issue]) -> set[Path]:
    targets: set[Path] = set()
    for line, destination in _markdown_destinations(text):
        try:
            local = _local_destination(destination)
        except ValueError as exc:
            _issue(issues, "broken-link", path, f"line {line} invalid URL: {destination}: {exc}")
            continue
        if local is None:
            continue
        if not local:
            continue
        candidate = (path.parent / local).resolve()
        try:
            candidate.relative_to(boundary)
        except ValueError:
            _issue(issues, "broken-link", path, f"line {line} escapes allowed root: {destination}")
            continue
        if not candidate.exists():
            _issue(issues, "broken-link", path, f"line {line} target does not exist: {destination}")
            continue
        targets.add(candidate)
    return targets


def _active_references(root: Path, skill_path: Path, text: str, issues: list[Issue]) -> set[Path]:
    """Find directly declared reference cards, whether linked or code-styled.

    The current skill convention names cards as ``references/name.md`` in
    inline code rather than always making those names Markdown links.  Both
    forms are explicit structural declarations; prose lookalikes are not.
    """
    references = {
        target for target in _check_links(skill_path.parent.resolve(), skill_path, text, issues)
        if target.is_relative_to((root / REFERENCE_DIR).resolve()) and target.suffix.lower() == ".md"
    }
    reference_root = (root / REFERENCE_DIR).resolve()
    for line, raw_line in _without_code(text):
        for match in REFERENCE_PATH_RE.finditer(raw_line):
            candidate = (reference_root / match.group(1)).resolve()
            try:
                candidate.relative_to(reference_root)
            except ValueError:
                _issue(issues, "active-reference", skill_path, f"line {line} escapes references: {match.group(0)}")
                continue
            if not candidate.is_file():
                _issue(issues, "active-reference", skill_path, f"line {line} does not exist: {match.group(0)}")
                continue
            references.add(candidate)
    return references


def _github_anchor(heading: str) -> str:
    value = heading.lower().strip()
    value = re.sub(r"[\[\]`*_]", "", value)
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def _check_headings(path: Path, text: str, issues: list[Issue], *, runtime: bool) -> None:
    anchors: dict[str, int] = {}
    for line, raw in _without_code(text):
        match = HEADING_RE.match(raw)
        if match is None:
            continue
        heading = match.group(2).strip()
        if runtime and RUNTIME_RESEARCH_HEADING_RE.match(heading):
            _issue(issues, "runtime-research-heading", path, f"line {line} is not runtime guidance")
        anchor = _github_anchor(heading)
        if not anchor:
            _issue(issues, "invalid-heading", path, f"line {line} has no usable anchor")
        elif anchor in anchors:
            _issue(issues, "duplicate-anchor", path, f"line {line} duplicates line {anchors[anchor]} ({anchor})")
        else:
            anchors[anchor] = line


def _paragraphs(text: str) -> Iterable[tuple[int, str]]:
    """Yield normalized prose paragraphs outside fenced code blocks.

    This is an exact-content check after whitespace normalization, not an
    attempt to decide whether two passages mean the same thing.  The minimum
    length keeps common policy sentences and short boilerplate out of scope.
    """
    first_line: int | None = None
    lines: list[str] = []
    for line_number, line in _without_code(text):
        if not line.strip():
            if lines and first_line is not None:
                paragraph = " ".join(" ".join(lines).split())
                if len(paragraph) >= MIN_DUPLICATE_PARAGRAPH_CHARS:
                    yield first_line, paragraph
            first_line = None
            lines = []
            continue
        if first_line is None:
            first_line = line_number
        lines.append(line)
    if lines and first_line is not None:
        paragraph = " ".join(" ".join(lines).split())
        if len(paragraph) >= MIN_DUPLICATE_PARAGRAPH_CHARS:
            yield first_line, paragraph


def _check_budget(path: Path, text: str, issues: list[Issue], *, byte_limit: int, line_limit: int) -> None:
    size = len(text.encode("utf-8"))
    lines = len(text.splitlines())
    if size > byte_limit:
        _issue(issues, "size-budget", path, f"{size} bytes exceeds {byte_limit}")
    if lines > line_limit:
        _issue(issues, "line-budget", path, f"{lines} lines exceeds {line_limit}")


def _marketplace_plugin(root: Path, skill_name: str, issues: list[Issue]) -> dict | None:
    path = root / MARKETPLACE_PATH
    raw = _read(path, issues)
    if raw is None:
        return None
    try:
        marketplace = json.loads(raw)
    except json.JSONDecodeError as exc:
        _issue(issues, "marketplace-json", path, f"invalid JSON: {exc.msg}")
        return None
    if not isinstance(marketplace, dict):
        _issue(issues, "marketplace-json", path, "marketplace must be a JSON object")
        return None
    marketplace_name = marketplace.get("name")
    if not isinstance(marketplace_name, str) or not SKILL_NAME_RE.fullmatch(marketplace_name):
        _issue(issues, "marketplace-name", path, "root name must be lowercase kebab-case (1-64 chars)")
    owner = marketplace.get("owner")
    if not isinstance(owner, dict) or not isinstance(owner.get("name"), str) or not owner["name"].strip():
        _issue(issues, "marketplace-owner", path, "owner.name must be non-empty text")
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list):
        _issue(issues, "marketplace-json", path, "plugins must be a list")
        return None
    matches = [entry for entry in plugins if isinstance(entry, dict) and entry.get("name") == skill_name]
    if len(matches) != 1:
        _issue(issues, "marketplace-plugin", path, f"expected one plugin named {skill_name!r}, found {len(matches)}")
        return None
    return matches[0]


def _resolve_marketplace_path(root: Path, plugin_root: Path, raw_path: object, issues: list[Issue], *, code: str, label: str) -> Path | None:
    if not isinstance(raw_path, str) or not raw_path.startswith("./"):
        _issue(issues, code, root / MARKETPLACE_PATH, f"{label} must be a relative path starting with ./")
        return None
    supplied = Path(raw_path)
    if supplied.is_absolute():
        _issue(issues, code, root / MARKETPLACE_PATH, f"{label} must be relative")
        return None
    base = root if label == "source" else plugin_root
    candidate = (base / supplied).resolve()
    boundary = root if label == "source" else plugin_root
    try:
        candidate.relative_to(boundary)
    except ValueError:
        _issue(issues, code, root / MARKETPLACE_PATH, f"{label} escapes its allowed root")
        return None
    return candidate


def _check_marketplace_layout(root: Path, plugin: dict, skill_path: Path, issues: list[Issue]) -> None:
    plugin_root = _resolve_marketplace_path(root, root, plugin.get("source"), issues, code="marketplace-source", label="source")
    if plugin_root is None:
        return
    if not plugin_root.is_dir():
        _issue(issues, "marketplace-source", root / MARKETPLACE_PATH, "source does not resolve to a directory")
        return
    if plugin.get("strict") is not False and not (plugin_root / ".claude-plugin/plugin.json").is_file():
        _issue(issues, "marketplace-manifest", root / MARKETPLACE_PATH, "a manifest-free plugin must explicitly set strict: false")
    configured = plugin.get("skills")
    if not isinstance(configured, list) or not configured:
        _issue(issues, "marketplace-skills", root / MARKETPLACE_PATH, "skills must be a non-empty list of relative paths")
        return
    actual = skill_path.resolve()
    matched_actual = False
    for item in configured:
        configured_path = _resolve_marketplace_path(root, plugin_root, item, issues, code="marketplace-skill", label="skill path")
        if configured_path is None:
            continue
        resolved_skill = configured_path if configured_path.name == "SKILL.md" else configured_path / "SKILL.md"
        if not resolved_skill.is_file():
            _issue(issues, "marketplace-skill", root / MARKETPLACE_PATH, f"skill path does not contain SKILL.md: {item!r}")
            continue
        if resolved_skill.resolve() != actual:
            _issue(issues, "marketplace-skill", root / MARKETPLACE_PATH, f"skill path does not resolve to the active SKILL.md: {item!r}")
            continue
        matched_actual = True
    if not matched_actual:
        _issue(issues, "marketplace-skill", root / MARKETPLACE_PATH, "skills must include the active SKILL.md")


def _check_openai_ui(skill_path: Path, issues: list[Issue]) -> None:
    path = skill_path.parent / "agents" / "openai.yaml"
    raw = _read(path, issues)
    if raw is None:
        return
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        _issue(issues, "ui-manifest", path, f"invalid YAML: {exc}")
        return
    interface = data.get("interface") if isinstance(data, dict) else None
    if not isinstance(interface, dict):
        _issue(issues, "ui-interface", path, "interface must be a mapping")
        return
    display_name = interface.get("display_name")
    if not isinstance(display_name, str) or not display_name.strip():
        _issue(issues, "ui-display-name", path, "interface.display_name must be non-empty text")
    short_description = interface.get("short_description")
    if not isinstance(short_description, str) or not 25 <= len(short_description.strip()) <= 64:
        _issue(issues, "ui-short-description", path, "interface.short_description must be 25-64 characters")
    default_prompt = interface.get("default_prompt")
    if not isinstance(default_prompt, str) or "$augustus" not in default_prompt:
        _issue(issues, "ui-default-prompt", path, "interface.default_prompt must mention $augustus")
    policy = data.get("policy") if isinstance(data, dict) else None
    if policy is not None:
        if not isinstance(policy, dict):
            _issue(issues, "ui-policy", path, "policy must be a mapping when present")
        elif "allow_implicit_invocation" in policy and not isinstance(policy["allow_implicit_invocation"], bool):
            _issue(issues, "ui-policy", path, "policy.allow_implicit_invocation must be boolean when present")
        if isinstance(policy, dict) and "implicit" in policy:
            _issue(issues, "ui-policy", path, "use allow_implicit_invocation, not implicit")
    asset_values: list[object] = []
    if isinstance(data, dict) and "assets" in data:
        assets = data["assets"]
        if isinstance(assets, dict):
            asset_values.extend(assets.values())
        elif isinstance(assets, list):
            asset_values.extend(assets)
        else:
            _issue(issues, "ui-assets", path, "assets must be a mapping or list when present")
    for key in ("icon_small", "icon_large"):
        if key in interface:
            asset_values.append(interface[key])
    skill_root = skill_path.parent.resolve()
    for asset in asset_values:
        if not isinstance(asset, str) or not asset:
            _issue(issues, "ui-assets", path, "asset references must be non-empty relative paths")
            continue
        supplied = Path(asset)
        if supplied.is_absolute():
            _issue(issues, "ui-assets", path, "asset references must be relative")
            continue
        candidate = (skill_root / supplied).resolve()
        try:
            candidate.relative_to(skill_root)
        except ValueError:
            _issue(issues, "ui-assets", path, "asset reference escapes the skill directory")
            continue
        if not candidate.is_file():
            _issue(issues, "ui-assets", path, f"asset does not exist: {asset}")


def _main_docs(root: Path) -> tuple[Path, ...]:
    return tuple(
        path for path in (
            root / "README.md",
            root / "docs" / "index.md",
            root / "docs" / "ecosystem.md",
            root / "docs" / "examples.md",
            root / "research" / "README.md",
        ) if path.exists()
    )


def check_repository(root: Path | str) -> list[Issue]:
    """Return every deterministic repository issue for ``root``.

    ``root`` is configurable so tests and downstream integrators can validate
    isolated fixtures without invoking a subprocess or changing cwd.
    """
    root_path = Path(root).resolve()
    issues: list[Issue] = []
    skill_path = root_path / SKILL_PATH
    skill_text = _read(skill_path, issues)
    if skill_text is None:
        return issues

    _check_budget(skill_path, skill_text, issues, byte_limit=MAX_SKILL_BYTES, line_limit=MAX_SKILL_LINES)
    metadata = _frontmatter(skill_text, skill_path, issues)
    skill_name: str | None = None
    version: str | None = None
    if metadata is not None:
        name = metadata.get("name")
        description = metadata.get("description")
        meta = metadata.get("metadata")
        if not isinstance(name, str) or not SKILL_NAME_RE.fullmatch(name):
            _issue(issues, "skill-name", skill_path, "name must be lowercase kebab-case (1-64 chars)")
        else:
            skill_name = name
        if not isinstance(description, str) or not description.strip() or len(description) > MAX_DESCRIPTION_CHARS:
            _issue(issues, "skill-description", skill_path, f"description must be non-empty text up to {MAX_DESCRIPTION_CHARS} characters")
        if not isinstance(meta, dict) or not isinstance(meta.get("version"), str):
            _issue(issues, "skill-version", skill_path, "metadata.version must be a string")
        else:
            version = meta["version"]
            if not SEMVER_RE.fullmatch(version):
                _issue(issues, "skill-version", skill_path, "metadata.version must be semantic version text")

    _check_headings(skill_path, skill_text, issues, runtime=True)
    linked_references = _active_references(root_path, skill_path, skill_text, issues)
    reference_root = root_path / REFERENCE_DIR
    all_references = set(reference_root.rglob("*.md")) if reference_root.is_dir() else set()
    for reference in sorted(all_references - linked_references):
        _issue(issues, "unreferenced-reference", reference, "runtime reference is not declared by SKILL.md")

    reference_bytes = 0
    paragraphs: dict[str, tuple[Path, int]] = {}
    for reference in sorted(all_references):
        reference_text = _read(reference, issues)
        if reference_text is None:
            continue
        reference_bytes += len(reference_text.encode("utf-8"))
        _check_budget(reference, reference_text, issues, byte_limit=MAX_REFERENCE_BYTES, line_limit=MAX_REFERENCE_LINES)
        _check_headings(reference, reference_text, issues, runtime=True)
        _check_links(skill_path.parent.resolve(), reference, reference_text, issues)
        for line, paragraph in _paragraphs(reference_text):
            first = paragraphs.get(paragraph)
            if first is not None and first[0] != reference:
                _issue(
                    issues,
                    "duplicate-paragraph",
                    reference,
                    f"line {line} duplicates {first[0].relative_to(root_path)} line {first[1]}",
                )
            else:
                paragraphs[paragraph] = (reference, line)
    if reference_bytes > MAX_REFERENCE_TOTAL_BYTES:
        _issue(issues, "reference-total-budget", root_path / REFERENCE_DIR, f"{reference_bytes} bytes exceeds {MAX_REFERENCE_TOTAL_BYTES}")

    for document in _main_docs(root_path):
        text = _read(document, issues)
        if text is not None:
            _check_headings(document, text, issues, runtime=document == root_path / "README.md")
            _check_links(root_path, document, text, issues)

    if skill_name is not None:
        plugin = _marketplace_plugin(root_path, skill_name, issues)
        if plugin is not None:
            _check_marketplace_layout(root_path, plugin, skill_path, issues)
            plugin_version = plugin.get("version")
            if not isinstance(plugin_version, str) or not SEMVER_RE.fullmatch(plugin_version):
                _issue(issues, "marketplace-version", root_path / MARKETPLACE_PATH, "plugin version must be semantic version text")
            if version is not None and plugin_version != version:
                _issue(issues, "version-mismatch", root_path / MARKETPLACE_PATH, f"plugin version {plugin_version!r} != skill version {version!r}")
            plugin_description = plugin.get("description")
            if not isinstance(plugin_description, str) or not plugin_description.strip() or len(plugin_description) > MAX_DESCRIPTION_CHARS:
                _issue(issues, "marketplace-description", root_path / MARKETPLACE_PATH, f"plugin description must be non-empty text up to {MAX_DESCRIPTION_CHARS} characters")
    _check_openai_ui(skill_path, issues)
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="repository root")
    args = parser.parse_args(argv)
    issues = check_repository(args.root)
    if issues:
        for issue in issues:
            print(issue.render(Path(args.root).resolve()))
        return 1
    print("repository quality checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
