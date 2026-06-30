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
