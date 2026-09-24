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


SKILLS_DIR = Path(".agents/skills")
# The historical single-skill locations. They stay as the primary skill so
# existing integrators keep working; every skill under SKILLS_DIR is checked.
SKILL_PATH = SKILLS_DIR / "augustus" / "SKILL.md"
MARKETPLACE_PATH = Path(".claude-plugin/marketplace.json")
REFERENCE_DIR = SKILL_PATH.parent / "references"
REFERENCE_DIR_NAME = "references"
MAX_SKILL_BYTES = 16_000
MAX_SKILL_LINES = 220
MAX_REFERENCE_BYTES = 18_000
MAX_REFERENCE_LINES = 400
MAX_REFERENCE_TOTAL_BYTES = 180_000
MIN_DUPLICATE_PARAGRAPH_CHARS = 160
MAX_DESCRIPTION_CHARS = 1_024
MAX_COMPATIBILITY_CHARS = 500
# claude.ai upload, the Skills API and package_skill.py reject other top-level keys.
PORTABLE_FRONTMATTER_KEYS = frozenset({"name", "description", "license", "compatibility", "metadata", "allowed-tools"})
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
CHANGELOG_RELEASE_RE = re.compile(r"^## \[([^\]]+)\] - (\d{4}-\d{2}-\d{2})[ \t]*$", re.M)


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


def _active_references(reference_root: Path, skill_path: Path, text: str, issues: list[Issue]) -> set[Path]:
    """Find directly declared reference cards, whether linked or code-styled.

    The current skill convention names cards as ``references/name.md`` in
    inline code rather than always making those names Markdown links.  Both
    forms are explicit structural declarations; prose lookalikes are not.

    ``reference_root`` is the skill's own ``references/`` directory, so each
    skill in the repository declares and owns its own cards.
    """
    reference_root = reference_root.resolve()
    references = {
        target for target in _check_links(skill_path.parent.resolve(), skill_path, text, issues)
        if target.is_relative_to(reference_root) and target.suffix.lower() == ".md"
    }
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


def _check_marketplace_layout(root: Path, plugin: dict, skill_paths: Iterable[Path], issues: list[Issue]) -> None:
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
    actual = {path.resolve() for path in skill_paths}
    matched: set[Path] = set()
    for item in configured:
        configured_path = _resolve_marketplace_path(root, plugin_root, item, issues, code="marketplace-skill", label="skill path")
        if configured_path is None:
            continue
        resolved_skill = configured_path if configured_path.name == "SKILL.md" else configured_path / "SKILL.md"
        if not resolved_skill.is_file():
            _issue(issues, "marketplace-skill", root / MARKETPLACE_PATH, f"skill path does not contain SKILL.md: {item!r}")
            continue
        if resolved_skill.resolve() not in actual:
            _issue(issues, "marketplace-skill", root / MARKETPLACE_PATH, f"skill path does not resolve to an active SKILL.md: {item!r}")
            continue
        matched.add(resolved_skill.resolve())
    for missing in sorted(actual - matched):
        _issue(issues, "marketplace-skill", root / MARKETPLACE_PATH, f"skills must include every active SKILL.md; missing {missing.name} under {missing.parent.name}")


def _check_openai_ui(skill_path: Path, skill_name: str | None, issues: list[Issue]) -> None:
    """Validate an OpenAI UI manifest when the skill ships one.

    Only the primary skill has shipped a manifest so far. A skill without one
    is not an error; a malformed one is.
    """
    path = skill_path.parent / "agents" / "openai.yaml"
    if not path.is_file():
        return
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
    invocation = f"${skill_name}" if skill_name else "$augustus"
    if not isinstance(default_prompt, str) or invocation not in default_prompt:
        _issue(issues, "ui-default-prompt", path, f"interface.default_prompt must mention {invocation}")
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


def _check_release_surfaces(root: Path, version: str, issues: list[Issue]) -> None:
    """Keep public release surfaces in step with the skill version.

    A prerelease must be named in the README. A release needs matching
    citation metadata, a dated changelog heading, a pinned install or
    checkout of its tag in the README, and release notes linked from the
    site. This compares identifiers and parsed fields; it does not judge
    whether the notes are accurate.
    """
    readme_path = root / "README.md"
    readme = _read(readme_path, issues)
    if "-" in version.split("+", 1)[0]:
        if readme is not None and version not in readme:
            _issue(issues, "release-parity", readme_path, f"README must name development version {version}")
        return
    pins = (f"@v{version}", f"/tree/v{version}/", f"--branch v{version}")
    if readme is not None and not any(pin in readme for pin in pins):
        _issue(issues, "release-parity", readme_path, f"README must give a pinned v{version} install or checkout")
    citation_path = root / "CITATION.cff"
    citation_text = _read(citation_path, issues)
    released: str | None = None
    if citation_text is not None:
        try:
            citation = yaml.safe_load(citation_text)
        except yaml.YAMLError as exc:
            citation = f"invalid YAML: {exc}"
        if not isinstance(citation, dict):
            _issue(issues, "release-parity", citation_path, "citation metadata must be a YAML mapping")
        else:
            if str(citation.get("version")) != version:
                _issue(issues, "release-parity", citation_path, f"version {citation.get('version')!r} != skill version {version!r}")
            if citation.get("date-released") is None:
                _issue(issues, "release-parity", citation_path, "date-released is required for a release")
            else:
                released = str(citation["date-released"])
    changelog_path = root / "CHANGELOG.md"
    changelog = _read(changelog_path, issues)
    if changelog is not None:
        dates = [date for heading, date in CHANGELOG_RELEASE_RE.findall(changelog) if heading == version]
        if not dates:
            _issue(issues, "release-parity", changelog_path, f"no '## [{version}] - YYYY-MM-DD' heading")
        elif released is not None and dates[0] != released:
            _issue(issues, "release-parity", changelog_path, f"release date {dates[0]} != CITATION date-released {released}")
    notes = root / "docs" / f"release-notes-v{version}.md"
    if not notes.is_file():
        _issue(issues, "release-parity", notes, "release notes for the skill version are missing")
    for page in (root / "docs" / "index.md", root / "docs" / "_layouts" / "default.html"):
        if page.is_file():
            text = _read(page, issues)
            if text is not None and f"release-notes-v{version}.html" not in text:
                _issue(issues, "release-parity", page, f"must link release-notes-v{version}.html")


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


def _discover_skills(root: Path) -> list[Path]:
    """Return every ``SKILL.md`` in the repository, primary skill first.

    Skills are directories under ``.agents/skills/``. Ordering is stable so
    issue output does not depend on filesystem order.
    """
    skills_root = root / SKILLS_DIR
    found = sorted(path for path in skills_root.glob("*/SKILL.md") if path.is_file())
    primary = root / SKILL_PATH
    if primary in found:
        found.remove(primary)
        found.insert(0, primary)
    return found


def _check_skill(root_path: Path, skill_path: Path, issues: list[Issue], paragraphs: dict[str, tuple[Path, int]]) -> tuple[str | None, str | None]:
    """Check one skill and return its declared name and version.

    ``paragraphs`` is shared across skills, so a card copied from one skill
    into another is reported as a duplicate.
    """
    skill_text = _read(skill_path, issues)
    if skill_text is None:
        return None, None

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
            if name != skill_path.parent.name:
                _issue(issues, "skill-name", skill_path, f"name {name!r} must match its directory {skill_path.parent.name!r}")
        if not isinstance(description, str) or not description.strip() or len(description) > MAX_DESCRIPTION_CHARS:
            _issue(issues, "skill-description", skill_path, f"description must be non-empty text up to {MAX_DESCRIPTION_CHARS} characters")
        elif "<" in description or ">" in description:
            _issue(issues, "skill-description", skill_path, "description must not contain angle brackets")
        unexpected = sorted(str(key) for key in metadata if key not in PORTABLE_FRONTMATTER_KEYS)
        if unexpected:
            _issue(issues, "skill-frontmatter", skill_path, f"keys outside the Agent Skills spec: {', '.join(unexpected)}")
        compatibility = metadata.get("compatibility")
        if compatibility is not None and (not isinstance(compatibility, str) or len(compatibility) > MAX_COMPATIBILITY_CHARS):
            _issue(issues, "skill-compatibility", skill_path, f"compatibility must be text up to {MAX_COMPATIBILITY_CHARS} characters")
        if isinstance(meta, dict) and not all(isinstance(key, str) and isinstance(value, str) for key, value in meta.items()):
            _issue(issues, "skill-metadata", skill_path, "metadata must map strings to strings; quote numeric values")
        if not isinstance(meta, dict) or not isinstance(meta.get("version"), str):
            _issue(issues, "skill-version", skill_path, "metadata.version must be a string")
        else:
            version = meta["version"]
            if not SEMVER_RE.fullmatch(version):
                _issue(issues, "skill-version", skill_path, "metadata.version must be semantic version text")

    _check_headings(skill_path, skill_text, issues, runtime=True)
    reference_root = skill_path.parent / REFERENCE_DIR_NAME
    linked_references = _active_references(reference_root, skill_path, skill_text, issues)
    all_references = set(reference_root.rglob("*.md")) if reference_root.is_dir() else set()
    for reference in sorted(all_references - linked_references):
        _issue(issues, "unreferenced-reference", reference, "runtime reference is not declared by SKILL.md")

    reference_bytes = 0
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
        _issue(issues, "reference-total-budget", reference_root, f"{reference_bytes} bytes exceeds {MAX_REFERENCE_TOTAL_BYTES}")

    _check_openai_ui(skill_path, skill_name, issues)
    return skill_name, version


def check_repository(root: Path | str) -> list[Issue]:
    """Return every deterministic repository issue for ``root``.

    ``root`` is configurable so tests and downstream integrators can validate
    isolated fixtures without invoking a subprocess or changing cwd.

    Every skill under ``.agents/skills/`` is checked, with its own reference
    budget and its own declared cards. Skills share one version, because they
    ship as one plugin, and the marketplace must list all of them.
    """
    root_path = Path(root).resolve()
    issues: list[Issue] = []
    skill_paths = _discover_skills(root_path)
    if not skill_paths:
        _issue(issues, "missing-file", root_path / SKILL_PATH, "required file is absent")
        return issues

    paragraphs: dict[str, tuple[Path, int]] = {}
    names: dict[Path, str] = {}
    versions: dict[Path, str] = {}
    for skill_path in skill_paths:
        name, version = _check_skill(root_path, skill_path, issues, paragraphs)
        if name is not None:
            names[skill_path] = name
        if version is not None:
            versions[skill_path] = version

    distinct = sorted(set(versions.values()))
    if len(distinct) > 1:
        for skill_path, version in sorted(versions.items()):
            _issue(issues, "version-mismatch", skill_path, f"skill version {version!r} differs from the other skills: {', '.join(distinct)}")

    for document in _main_docs(root_path):
        text = _read(document, issues)
        if text is not None:
            _check_headings(document, text, issues, runtime=document == root_path / "README.md")
            _check_links(root_path, document, text, issues)

    primary = skill_paths[0]
    plugin_name = names.get(primary)
    version = versions.get(primary)
    if plugin_name is not None:
        plugin = _marketplace_plugin(root_path, plugin_name, issues)
        if plugin is not None:
            _check_marketplace_layout(root_path, plugin, skill_paths, issues)
            plugin_version = plugin.get("version")
            if not isinstance(plugin_version, str) or not SEMVER_RE.fullmatch(plugin_version):
                _issue(issues, "marketplace-version", root_path / MARKETPLACE_PATH, "plugin version must be semantic version text")
            if version is not None and plugin_version != version:
                _issue(issues, "version-mismatch", root_path / MARKETPLACE_PATH, f"plugin version {plugin_version!r} != skill version {version!r}")
            plugin_description = plugin.get("description")
            if not isinstance(plugin_description, str) or not plugin_description.strip() or len(plugin_description) > MAX_DESCRIPTION_CHARS:
                _issue(issues, "marketplace-description", root_path / MARKETPLACE_PATH, f"plugin description must be non-empty text up to {MAX_DESCRIPTION_CHARS} characters")
    if version is not None and SEMVER_RE.fullmatch(version) and len(distinct) == 1:
        _check_release_surfaces(root_path, version, issues)
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
