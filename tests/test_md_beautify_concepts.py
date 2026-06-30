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
