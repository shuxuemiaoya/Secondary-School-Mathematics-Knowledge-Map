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
    if len(original.strip()) >= 40 and len(formatted.strip()) < int(len(original.strip()) * 0.55):
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
