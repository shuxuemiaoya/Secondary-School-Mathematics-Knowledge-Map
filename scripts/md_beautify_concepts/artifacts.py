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
