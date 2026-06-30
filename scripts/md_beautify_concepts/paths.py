from pathlib import Path


SKIPPED_DIRS = {
    ".git",
    ".obsidian",
    ".claude",
    ".claudian",
    ".pytest_cache",
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
