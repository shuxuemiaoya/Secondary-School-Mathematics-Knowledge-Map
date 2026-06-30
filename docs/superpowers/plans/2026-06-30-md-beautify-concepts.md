# Markdown Beautify Concepts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a repo-local workflow that batch-processes mathematical Markdown files, using one LLM call per file to beautify layout and extract explicitly defined concepts into sibling `概念/` files.

**Architecture:** Implement a shared Python core under `scripts/md_beautify_concepts/`, expose a CLI at `scripts/md_beautify_concepts.py`, and keep Claude/Codex entries as thin wrappers around that core. The first implementation should support deterministic planning, validation, artifact writing, dry-run/apply paths, and a provider abstraction that can be tested with fixtures before wiring a real LLM provider.

**Tech Stack:** Python standard library, `pytest`, Markdown text fixtures, repo-local Claude skill files, repo-local Codex skill files.

---

## File Structure

- Create: `scripts/md_beautify_concepts.py`  
  CLI entry point for `plan`, `run`, and `resume`.
- Create: `scripts/md_beautify_concepts/__init__.py`  
  Package marker and version export.
- Create: `scripts/md_beautify_concepts/paths.py`  
  Path scanning, skip rules, UTF-8 path handling, and safe concept path resolution.
- Create: `scripts/md_beautify_concepts/models.py`  
  Dataclasses for manifest entries, concept files, LLM results, validation errors, and per-file state.
- Create: `scripts/md_beautify_concepts/provider.py`  
  Provider interface plus fixture provider for tests and dry local development.
- Create: `scripts/md_beautify_concepts/prompt.py`  
  Prompt assembly using `.claude/skills/beautify-md.md` as the rule source.
- Create: `scripts/md_beautify_concepts/validate.py`  
  JSON parsing and fail-closed validation gates.
- Create: `scripts/md_beautify_concepts/artifacts.py`  
  Run record creation, manifest/state/summary/failure/candidate/diff writing.
- Create: `scripts/md_beautify_concepts/runner.py`  
  Plan/run/resume orchestration.
- Create: `tests/test_md_beautify_concepts.py`  
  Focused tests for scan, dry-run, apply, validation, path safety, collisions, and Chinese paths.
- Modify: `.claude/skills/beautify-md.md`  
  Add a short command-first section that routes Claude/Claudian agents to the shared workflow.
- Create: `skills/mathos-md-beautify-concepts/SKILL.md`  
  Codex/MathOS skill entry that describes plan/dry-run/apply/resume and artifact inspection.
- Create: `skills/mathos-md-beautify-concepts/agents/openai.yaml`  
  UI metadata for the Codex skill.

---

### Task 1: Test The Scanner And Path Safety

**Files:**
- Create: `scripts/md_beautify_concepts/__init__.py`
- Create: `scripts/md_beautify_concepts/models.py`
- Create: `scripts/md_beautify_concepts/paths.py`
- Create: `tests/test_md_beautify_concepts.py`

- [ ] **Step 1: Write failing scanner and path-safety tests**

Add this initial content to `tests/test_md_beautify_concepts.py`:

```python
from pathlib import Path

import pytest

from scripts.md_beautify_concepts.paths import iter_markdown_targets, resolve_concept_path


def write_text(path: Path, text: str = "# Title\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_iter_markdown_targets_skips_generated_dirs(tmp_path: Path) -> None:
    write_text(tmp_path / "chapter.md")
    write_text(tmp_path / "nested" / "lesson.md")
    write_text(tmp_path / "概念" / "线段.md")
    write_text(tmp_path / "images" / "image.png.md")
    write_text(tmp_path / ".obsidian" / "config.md")
    write_text(tmp_path / ".claude" / "skills" / "beautify-md.md")
    write_text(tmp_path / "agent-memory" / "records" / "old.md")

    targets = [path.relative_to(tmp_path).as_posix() for path in iter_markdown_targets(tmp_path)]

    assert targets == ["chapter.md", "nested/lesson.md"]


def test_iter_markdown_targets_accepts_single_file(tmp_path: Path) -> None:
    source = tmp_path / "初中" / "课本" / "1 线段、射线、直线.md"
    write_text(source)

    assert list(iter_markdown_targets(source)) == [source]


def test_resolve_concept_path_stays_inside_sibling_concept_folder(tmp_path: Path) -> None:
    source = tmp_path / "初中" / "课本" / "lesson.md"
    write_text(source)

    result = resolve_concept_path(source, "线段.md")

    assert result == source.parent / "概念" / "线段.md"


def test_resolve_concept_path_rejects_nested_or_escaping_names(tmp_path: Path) -> None:
    source = tmp_path / "lesson.md"
    write_text(source)

    with pytest.raises(ValueError, match="direct child"):
        resolve_concept_path(source, "几何/线段.md")

    with pytest.raises(ValueError, match="direct child"):
        resolve_concept_path(source, "../线段.md")
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```powershell
python -m pytest tests/test_md_beautify_concepts.py -q
```

Expected: fail with `ModuleNotFoundError` or missing `iter_markdown_targets`.

- [ ] **Step 3: Implement scanner and path helpers**

Create `scripts/md_beautify_concepts/__init__.py`:

```python
__version__ = "0.1.0"
```

Create `scripts/md_beautify_concepts/models.py`:

```python
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class ManifestEntry:
    path: Path
    status: str
    reason: str = ""


@dataclass(frozen=True)
class ConceptFile:
    name: str
    title: str
    body: str


@dataclass(frozen=True)
class LlmResult:
    formatted_markdown: str
    concept_files: list[ConceptFile]
    risk_notes: list[str] = field(default_factory=list)
```

Create `scripts/md_beautify_concepts/paths.py`:

```python
from pathlib import Path


SKIPPED_DIRS = {
    ".git",
    ".obsidian",
    ".claude",
    ".claudian",
    "agent-memory",
    "docs",
    "images",
    "概念",
}


def should_skip_dir(path: Path) -> bool:
    return path.name in SKIPPED_DIRS


def iter_markdown_targets(input_path: Path) -> list[Path]:
    input_path = input_path.resolve()
    if input_path.is_file():
        return [input_path] if input_path.suffix.lower() == ".md" and not _has_skipped_part(input_path) else []
    if not input_path.exists():
        raise FileNotFoundError(str(input_path))

    targets: list[Path] = []
    for path in sorted(input_path.rglob("*.md")):
        if _has_skipped_part(path.relative_to(input_path)):
            continue
        targets.append(path.resolve())
    return targets


def _has_skipped_part(path: Path) -> bool:
    return any(part in SKIPPED_DIRS for part in path.parts)


def resolve_concept_path(source_path: Path, concept_name: str) -> Path:
    candidate_name = Path(concept_name)
    if len(candidate_name.parts) != 1 or candidate_name.name in {"", ".", ".."}:
        raise ValueError("Concept file name must be a direct child of 概念/")
    if candidate_name.suffix.lower() != ".md":
        raise ValueError("Concept file name must end with .md")

    concept_dir = source_path.resolve().parent / "概念"
    result = (concept_dir / candidate_name.name).resolve()
    if result.parent != concept_dir.resolve():
        raise ValueError("Concept file name must be a direct child of 概念/")
    return result
```

- [ ] **Step 4: Run tests to verify scanner passes**

Run:

```powershell
python -m pytest tests/test_md_beautify_concepts.py -q
```

Expected: all scanner tests pass.

- [ ] **Step 5: Commit scanner**

Run:

```powershell
git add scripts/md_beautify_concepts tests/test_md_beautify_concepts.py
git commit -m "feat: add md beautify target scanner"
```

---

### Task 2: Validate LLM JSON Output

**Files:**
- Modify: `scripts/md_beautify_concepts/models.py`
- Create: `scripts/md_beautify_concepts/validate.py`
- Modify: `tests/test_md_beautify_concepts.py`

- [ ] **Step 1: Add failing validation tests**

Append to `tests/test_md_beautify_concepts.py`:

```python
import json

from scripts.md_beautify_concepts.validate import parse_llm_json, validate_result


def test_parse_llm_json_requires_valid_json() -> None:
    with pytest.raises(ValueError, match="valid JSON"):
        parse_llm_json("not json")


def test_parse_llm_json_builds_concept_files() -> None:
    payload = json.dumps(
        {
            "formatted_markdown": "这里是 [[概念/线段]]。\n",
            "concept_files": [{"name": "线段.md", "title": "线段", "body": "# 线段\n\n有两个端点。\n"}],
            "risk_notes": ["kept conservative"],
        },
        ensure_ascii=False,
    )

    result = parse_llm_json(payload)

    assert result.formatted_markdown.startswith("这里是")
    assert result.concept_files[0].name == "线段.md"
    assert result.risk_notes == ["kept conservative"]


def test_validate_result_rejects_missing_concept_file_for_new_link(tmp_path: Path) -> None:
    source = tmp_path / "lesson.md"
    write_text(source, "线段有两个端点。\n")
    result = parse_llm_json(
        json.dumps(
            {
                "formatted_markdown": "[[概念/线段]]有两个端点。\n",
                "concept_files": [],
                "risk_notes": [],
            },
            ensure_ascii=False,
        )
    )

    errors = validate_result(source, "线段有两个端点。\n", result)

    assert any("missing concept file" in error for error in errors)


def test_validate_result_accepts_matching_concept_file(tmp_path: Path) -> None:
    source = tmp_path / "lesson.md"
    write_text(source, "线段有两个端点。\n")
    result = parse_llm_json(
        json.dumps(
            {
                "formatted_markdown": "[[概念/线段]]有两个端点。\n",
                "concept_files": [{"name": "线段.md", "title": "线段", "body": "# 线段\n\n有两个端点。\n"}],
                "risk_notes": [],
            },
            ensure_ascii=False,
        )
    )

    assert validate_result(source, "线段有两个端点。\n", result) == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```powershell
python -m pytest tests/test_md_beautify_concepts.py -q
```

Expected: fail with missing `validate` module.

- [ ] **Step 3: Implement JSON parsing and validation**

Create `scripts/md_beautify_concepts/validate.py`:

```python
import json
import re
from pathlib import Path
from typing import Any

from .models import ConceptFile, LlmResult
from .paths import resolve_concept_path


CONCEPT_LINK_RE = re.compile(r"\[\[概念/([^\]\|#]+)(?:[|#][^\]]*)?\]\]")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)|!\[\[[^\]]+\]\]")


def parse_llm_json(text: str) -> LlmResult:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"LLM response must be valid JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("LLM response must be a JSON object")

    formatted = payload.get("formatted_markdown")
    concept_items = payload.get("concept_files")
    risk_notes = payload.get("risk_notes", [])
    if not isinstance(formatted, str) or not formatted.strip():
        raise ValueError("formatted_markdown must be a non-empty string")
    if not isinstance(concept_items, list):
        raise ValueError("concept_files must be a list")
    if not isinstance(risk_notes, list) or not all(isinstance(item, str) for item in risk_notes):
        raise ValueError("risk_notes must be a list of strings")

    concepts: list[ConceptFile] = []
    for item in concept_items:
        concepts.append(_parse_concept(item))
    return LlmResult(formatted_markdown=formatted, concept_files=concepts, risk_notes=risk_notes)


def _parse_concept(item: Any) -> ConceptFile:
    if not isinstance(item, dict):
        raise ValueError("each concept file must be an object")
    name = item.get("name")
    title = item.get("title")
    body = item.get("body")
    if not all(isinstance(value, str) and value.strip() for value in [name, title, body]):
        raise ValueError("concept file name, title, and body must be non-empty strings")
    return ConceptFile(name=name, title=title, body=body)


def validate_result(source_path: Path, original: str, result: LlmResult) -> list[str]:
    errors: list[str] = []
    formatted = result.formatted_markdown
    if len(formatted.strip()) < max(20, int(len(original.strip()) * 0.55)):
        errors.append("formatted_markdown is suspiciously shorter than original")
    if formatted.count("```") % 2 != 0:
        errors.append("Markdown code fences are unbalanced")
    if formatted.count("$$") % 2 != 0:
        errors.append("Math block delimiters are unbalanced")
    if len(IMAGE_RE.findall(formatted)) < len(IMAGE_RE.findall(original)):
        errors.append("image references were reduced")

    produced_names = {Path(concept.name).stem for concept in result.concept_files}
    for concept in result.concept_files:
        try:
            resolve_concept_path(source_path, concept.name)
        except ValueError as exc:
            errors.append(str(exc))

    existing_dir = source_path.parent / "概念"
    existing_names = {path.stem for path in existing_dir.glob("*.md")} if existing_dir.exists() else set()
    for link_name in CONCEPT_LINK_RE.findall(formatted):
        if link_name not in produced_names and link_name not in existing_names:
            errors.append(f"missing concept file for new link: {link_name}")
    return errors
```

- [ ] **Step 4: Run validation tests**

Run:

```powershell
python -m pytest tests/test_md_beautify_concepts.py -q
```

Expected: all tests pass.

- [ ] **Step 5: Commit validation**

Run:

```powershell
git add scripts/md_beautify_concepts/validate.py scripts/md_beautify_concepts/models.py tests/test_md_beautify_concepts.py
git commit -m "feat: validate md beautify llm output"
```

---

### Task 3: Add Artifacts And Dry-Run Runner

**Files:**
- Create: `scripts/md_beautify_concepts/provider.py`
- Create: `scripts/md_beautify_concepts/artifacts.py`
- Create: `scripts/md_beautify_concepts/runner.py`
- Modify: `tests/test_md_beautify_concepts.py`

- [ ] **Step 1: Add failing dry-run artifact test**

Append to `tests/test_md_beautify_concepts.py`:

```python
from scripts.md_beautify_concepts.provider import FixtureProvider
from scripts.md_beautify_concepts.runner import run_dry


def test_run_dry_writes_candidate_artifacts_without_modifying_source(tmp_path: Path) -> None:
    source = tmp_path / "lesson.md"
    original = "线段有两个端点。\n"
    write_text(source, original)
    provider = FixtureProvider(
        {
            source.resolve(): {
                "formatted_markdown": "[[概念/线段]]有两个端点。\n",
                "concept_files": [{"name": "线段.md", "title": "线段", "body": "# 线段\n\n有两个端点。\n"}],
                "risk_notes": [],
            }
        }
    )

    record = run_dry(source, tmp_path / "agent-memory" / "records" / "test-run", provider)

    assert source.read_text(encoding="utf-8") == original
    assert (record / "candidates" / "lesson.md").exists()
    assert (record / "candidates" / "lesson" / "概念" / "线段.md").exists()
    assert (record / "result-summary.json").exists()
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```powershell
python -m pytest tests/test_md_beautify_concepts.py -q
```

Expected: fail with missing `provider` or `runner` module.

- [ ] **Step 3: Implement fixture provider, artifacts, and dry-run**

Create `scripts/md_beautify_concepts/provider.py`:

```python
import json
from pathlib import Path
from typing import Protocol


class Provider(Protocol):
    def complete_file(self, source_path: Path, prompt: str) -> str:
        ...


class FixtureProvider:
    def __init__(self, responses: dict[Path, dict]) -> None:
        self.responses = {path.resolve(): response for path, response in responses.items()}

    def complete_file(self, source_path: Path, prompt: str) -> str:
        del prompt
        try:
            response = self.responses[source_path.resolve()]
        except KeyError as exc:
            raise ValueError(f"No fixture response for {source_path}") from exc
        return json.dumps(response, ensure_ascii=False)
```

Create `scripts/md_beautify_concepts/artifacts.py`:

```python
import difflib
import json
from pathlib import Path

from .models import LlmResult


def ensure_record(record_dir: Path) -> Path:
    record_dir.mkdir(parents=True, exist_ok=True)
    for name in ["candidates", "diffs", "llm-responses"]:
        (record_dir / name).mkdir(exist_ok=True)
    return record_dir


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_dry_candidate(record_dir: Path, source_path: Path, original: str, result: LlmResult) -> None:
    candidate_path = record_dir / "candidates" / source_path.name
    candidate_path.write_text(result.formatted_markdown, encoding="utf-8")

    concept_base = record_dir / "candidates" / source_path.stem / "概念"
    concept_base.mkdir(parents=True, exist_ok=True)
    for concept in result.concept_files:
        (concept_base / concept.name).write_text(concept.body, encoding="utf-8")

    diff = "".join(
        difflib.unified_diff(
            original.splitlines(keepends=True),
            result.formatted_markdown.splitlines(keepends=True),
            fromfile=str(source_path),
            tofile=str(candidate_path),
        )
    )
    (record_dir / "diffs" / f"{source_path.stem}.diff").write_text(diff, encoding="utf-8")
```

Create `scripts/md_beautify_concepts/runner.py`:

```python
from pathlib import Path

from .artifacts import ensure_record, write_dry_candidate, write_json
from .paths import iter_markdown_targets
from .provider import Provider
from .validate import parse_llm_json, validate_result


def run_dry(input_path: Path, record_dir: Path, provider: Provider) -> Path:
    record_dir = ensure_record(record_dir)
    targets = iter_markdown_targets(input_path)
    manifest = [{"path": str(path), "status": "planned"} for path in targets]
    write_json(record_dir / "manifest.json", manifest)

    results = []
    failures = []
    for source_path in targets:
        original = source_path.read_text(encoding="utf-8")
        raw = provider.complete_file(source_path, original)
        (record_dir / "llm-responses" / f"{source_path.stem}.json").write_text(raw, encoding="utf-8")
        try:
            result = parse_llm_json(raw)
            errors = validate_result(source_path, original, result)
        except ValueError as exc:
            errors = [str(exc)]
            result = None
        if errors or result is None:
            failures.append({"path": str(source_path), "errors": errors})
            continue
        write_dry_candidate(record_dir, source_path, original, result)
        results.append({"path": str(source_path), "status": "candidate-written"})

    write_json(record_dir / "failures.json", failures)
    write_json(
        record_dir / "result-summary.json",
        {"planned": len(targets), "succeeded": len(results), "failed": len(failures), "mode": "dry-run"},
    )
    write_json(record_dir / "run-state.json", {"results": results, "failures": failures})
    return record_dir
```

- [ ] **Step 4: Run dry-run tests**

Run:

```powershell
python -m pytest tests/test_md_beautify_concepts.py -q
```

Expected: all tests pass.

- [ ] **Step 5: Commit dry-run runner**

Run:

```powershell
git add scripts/md_beautify_concepts tests/test_md_beautify_concepts.py
git commit -m "feat: add md beautify dry run artifacts"
```

---

### Task 4: Add Apply Mode And CLI

**Files:**
- Modify: `scripts/md_beautify_concepts/runner.py`
- Create: `scripts/md_beautify_concepts.py`
- Modify: `tests/test_md_beautify_concepts.py`

- [ ] **Step 1: Add failing apply-mode test**

Append to `tests/test_md_beautify_concepts.py`:

```python
from scripts.md_beautify_concepts.runner import run_apply


def test_run_apply_writes_source_and_concepts_after_validation(tmp_path: Path) -> None:
    source = tmp_path / "lesson.md"
    write_text(source, "线段有两个端点。\n")
    provider = FixtureProvider(
        {
            source.resolve(): {
                "formatted_markdown": "[[概念/线段]]有两个端点。\n",
                "concept_files": [{"name": "线段.md", "title": "线段", "body": "# 线段\n\n有两个端点。\n"}],
                "risk_notes": [],
            }
        }
    )

    run_apply(source, tmp_path / "agent-memory" / "records" / "apply-run", provider)

    assert source.read_text(encoding="utf-8") == "[[概念/线段]]有两个端点。\n"
    assert (source.parent / "概念" / "线段.md").read_text(encoding="utf-8") == "# 线段\n\n有两个端点。\n"
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```powershell
python -m pytest tests/test_md_beautify_concepts.py -q
```

Expected: fail with missing `run_apply`.

- [ ] **Step 3: Implement apply mode**

Append to `scripts/md_beautify_concepts/runner.py`:

```python
from .paths import resolve_concept_path


def run_apply(input_path: Path, record_dir: Path, provider: Provider) -> Path:
    record_dir = ensure_record(record_dir)
    targets = iter_markdown_targets(input_path)
    write_json(record_dir / "manifest.json", [{"path": str(path), "status": "planned"} for path in targets])

    results = []
    failures = []
    for source_path in targets:
        original = source_path.read_text(encoding="utf-8")
        raw = provider.complete_file(source_path, original)
        (record_dir / "llm-responses" / f"{source_path.stem}.json").write_text(raw, encoding="utf-8")
        try:
            result = parse_llm_json(raw)
            errors = validate_result(source_path, original, result)
        except ValueError as exc:
            failures.append({"path": str(source_path), "errors": [str(exc)]})
            continue
        if errors:
            failures.append({"path": str(source_path), "errors": errors})
            continue

        for concept in result.concept_files:
            concept_path = resolve_concept_path(source_path, concept.name)
            concept_path.parent.mkdir(parents=True, exist_ok=True)
            if concept_path.exists() and concept_path.read_text(encoding="utf-8") != concept.body:
                failures.append({"path": str(source_path), "errors": [f"concept collision: {concept.name}"]})
                break
            concept_path.write_text(concept.body, encoding="utf-8")
        else:
            source_path.write_text(result.formatted_markdown, encoding="utf-8")
            results.append({"path": str(source_path), "status": "applied"})

    write_json(record_dir / "failures.json", failures)
    write_json(
        record_dir / "result-summary.json",
        {"planned": len(targets), "succeeded": len(results), "failed": len(failures), "mode": "apply"},
    )
    write_json(record_dir / "run-state.json", {"results": results, "failures": failures})
    return record_dir
```

- [ ] **Step 4: Add CLI entry point**

Create `scripts/md_beautify_concepts.py`:

```python
import argparse
from pathlib import Path

from md_beautify_concepts.provider import FixtureProvider
from md_beautify_concepts.runner import run_apply, run_dry


def main() -> int:
    parser = argparse.ArgumentParser(description="Beautify Markdown and extract concepts.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan_parser = subparsers.add_parser("plan")
    plan_parser.add_argument("path", type=Path)

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("path", type=Path)
    mode = run_parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    run_parser.add_argument("--record-dir", type=Path, default=Path("agent-memory/records/manual-md-beautify-concepts"))
    run_parser.add_argument("--fixture-response", type=Path)

    args = parser.parse_args()
    if args.command == "plan":
        from md_beautify_concepts.paths import iter_markdown_targets

        for target in iter_markdown_targets(args.path):
            print(target)
        return 0

    if args.fixture_response is None:
        raise SystemExit("--fixture-response is required until the real LLM provider is configured")
    import json

    response = json.loads(args.fixture_response.read_text(encoding="utf-8"))
    provider = FixtureProvider({Path(args.path).resolve(): response})
    if args.dry_run:
        record = run_dry(args.path, args.record_dir, provider)
    else:
        record = run_apply(args.path, args.record_dir, provider)
    print(record)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 5: Run apply tests and CLI smoke test**

Run:

```powershell
python -m pytest tests/test_md_beautify_concepts.py -q
python scripts/md_beautify_concepts.py plan .
```

Expected: tests pass; plan prints Markdown target paths.

- [ ] **Step 6: Commit apply and CLI**

Run:

```powershell
git add scripts/md_beautify_concepts.py scripts/md_beautify_concepts tests/test_md_beautify_concepts.py
git commit -m "feat: apply md beautify concept outputs"
```

---

### Task 5: Add Prompt Assembly And Skill Entries

**Files:**
- Create: `scripts/md_beautify_concepts/prompt.py`
- Modify: `scripts/md_beautify_concepts/runner.py`
- Modify: `.claude/skills/beautify-md.md`
- Create: `skills/mathos-md-beautify-concepts/SKILL.md`
- Create: `skills/mathos-md-beautify-concepts/agents/openai.yaml`

- [ ] **Step 1: Add prompt assembly**

Create `scripts/md_beautify_concepts/prompt.py`:

```python
from pathlib import Path


def build_prompt(source_path: Path, markdown: str, rules_path: Path = Path(".claude/skills/beautify-md.md")) -> str:
    rules = rules_path.read_text(encoding="utf-8")
    return f"""You are processing one mathematical Markdown file.

Return valid JSON only with these fields:
- formatted_markdown: complete replacement Markdown for the source file
- concept_files: list of objects with name, title, body
- risk_notes: list of strings

Rules:
{rules}

Source path:
{source_path}

Source Markdown:
```markdown
{markdown}
```
"""
```

- [ ] **Step 2: Route runner through prompt builder**

Modify `scripts/md_beautify_concepts/runner.py` so both `run_dry` and `run_apply` call:

```python
from .prompt import build_prompt
```

Replace:

```python
raw = provider.complete_file(source_path, original)
```

with:

```python
raw = provider.complete_file(source_path, build_prompt(source_path, original))
```

- [ ] **Step 3: Add Claude skill routing note**

At the top of `.claude/skills/beautify-md.md`, after the title block, add:

```markdown
## 推荐批量工作流

当用户要求批量美化 Markdown、提取概念、生成 `概念/` 文件夹，或同时完成这两件事时，优先调用仓库共享脚本，而不是逐个手工编辑文件。

推荐命令：

```powershell
python scripts/md_beautify_concepts.py plan "path\to\file-or-folder"
python scripts/md_beautify_concepts.py run "path\to\file-or-folder" --dry-run
python scripts/md_beautify_concepts.py run "path\to\file-or-folder" --apply
```

规则：一次 LLM 调用同时完成排版美化和概念提取；原文定义位置替换为 `[[概念/概念名]]`；概念文件直接写入源文件同目录的 `概念/`。
```

- [ ] **Step 4: Create Codex skill**

Create `skills/mathos-md-beautify-concepts/SKILL.md`:

```markdown
---
name: mathos-md-beautify-concepts
description: Batch beautify mathematical Markdown files and extract explicitly defined concepts into sibling Obsidian `概念/` files. Use when the user asks to process one Markdown file or a folder of Markdown files for layout cleanup, formula/image/table-safe formatting, concept extraction, Wikilink replacement, dry-run/apply execution, or run artifact inspection.
---

# MathOS Markdown Beautify And Concepts

Use this workflow for mathematical Markdown files in this repository. Treat all inputs as mathematical Markdown; do not branch by textbook, exercise book, or formula-summary source type.

## Commands

Plan without calling the LLM:

```powershell
python scripts/md_beautify_concepts.py plan "path\to\file-or-folder"
```

Dry run:

```powershell
python scripts/md_beautify_concepts.py run "path\to\file-or-folder" --dry-run
```

Apply:

```powershell
python scripts/md_beautify_concepts.py run "path\to\file-or-folder" --apply
```

## Contract

- One LLM call per source `.md` file.
- The same call must return formatted Markdown and concept files.
- Concept links use `[[概念/概念名]]`.
- Concept files are direct children of the source file's sibling `概念/` folder.
- Extract only concepts explicitly defined in the current file/chapter.
- Fail closed on invalid JSON, path escape, missing concept file, broken fences, broken math blocks, or suspicious content loss.

## Artifacts

Inspect `agent-memory/records/<run-id>/result-summary.json` first. If a run failed, inspect `failures.json` and the referenced raw response or candidate artifact.
```

Create `skills/mathos-md-beautify-concepts/agents/openai.yaml`:

```yaml
display_name: Markdown Beautify Concepts
short_description: Batch beautify math Markdown and extract concept files.
default_prompt: Plan or run Markdown beautification and concept extraction for the provided file or folder.
```

- [ ] **Step 5: Run tests and prompt smoke**

Run:

```powershell
python -m pytest tests/test_md_beautify_concepts.py -q
python -m py_compile scripts/md_beautify_concepts.py scripts/md_beautify_concepts/*.py
```

Expected: tests pass; compile succeeds.

- [ ] **Step 6: Commit prompt and skills**

Run:

```powershell
git add scripts/md_beautify_concepts .claude/skills/beautify-md.md skills/mathos-md-beautify-concepts
git commit -m "feat: add md beautify concept skill entries"
```

---

### Task 6: Final Verification

**Files:**
- Verify: `scripts/md_beautify_concepts.py`
- Verify: `scripts/md_beautify_concepts/*.py`
- Verify: `tests/test_md_beautify_concepts.py`
- Verify: `.claude/skills/beautify-md.md`
- Verify: `skills/mathos-md-beautify-concepts/SKILL.md`
- Verify: `skills/mathos-md-beautify-concepts/agents/openai.yaml`

- [ ] **Step 1: Run full focused verification**

Run:

```powershell
python -m pytest tests/test_md_beautify_concepts.py -q
python -m py_compile scripts/md_beautify_concepts.py scripts/md_beautify_concepts/*.py
git diff --check
```

Expected: all commands succeed.

- [ ] **Step 2: Inspect status**

Run:

```powershell
git status --short
```

Expected: only unrelated pre-existing user changes remain, or no changes if all implementation commits were made.

- [ ] **Step 3: Report completion**

Report:

```text
Implemented the shared Markdown beautify and concept extraction workflow, including scanner, validation, dry-run/apply artifacts, CLI, Claude routing, and Codex skill entry.
```

---

## Self-Review

Spec coverage:

- Unified mathematical Markdown handling: Task 1 scanner and Task 5 skill wording.
- Single LLM call per file: Task 3 provider and Task 5 prompt assembly.
- Concept files under sibling `概念/`: Task 1 path safety and Task 4 apply mode.
- Dry-run/apply artifacts: Task 3 and Task 4.
- Validation gates: Task 2.
- Claude and Codex double entry: Task 5.
- Tests and verification: Tasks 1 through 6.

No placeholders remain. Function names are consistent across tasks: `iter_markdown_targets`, `resolve_concept_path`, `parse_llm_json`, `validate_result`, `run_dry`, `run_apply`, and `build_prompt`.
