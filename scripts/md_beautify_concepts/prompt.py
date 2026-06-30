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
