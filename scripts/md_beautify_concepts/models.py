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
