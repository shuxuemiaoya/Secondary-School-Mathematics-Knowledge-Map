# Markdown Beautify And Concept Extraction Workflow Design

## Goal

Build a reusable workflow for batch-processing mathematical Markdown files. For each source `.md` file, one LLM call should jointly:

1. Beautify and normalize Markdown layout.
2. Extract only newly and explicitly defined concepts from the current file/chapter.
3. Move each extracted concept definition into a sibling `概念/` folder.
4. Replace the concept definition location in the original text with an Obsidian Wikilink such as `[[概念/线段]]`.

The workflow must not distinguish between textbooks, exercise books, formula summaries, or other source categories. It treats all inputs as mathematical Markdown documents and adapts only to the document's internal structure.

## Existing Context

The repository already contains a Claude skill at `.claude/skills/beautify-md.md`. That file is the current rule source for:

- Concept extraction.
- Markdown layout beautification.
- Math formula handling.
- Obsidian Callout usage.
- Image, table, and OCR cleanup rules.

The new workflow should reuse those rules instead of duplicating competing instructions.

## Architecture

Use a double-entry, single-core design.

### Core Workflow

The core workflow lives in repo-local scripts and reference files. It is responsible for:

- Scanning single files or folders.
- Skipping generated and non-source directories.
- Calling the LLM once per source Markdown file.
- Validating model output before writing.
- Writing formatted source Markdown.
- Writing concept Markdown files under the source file's sibling `概念/` folder.
- Recording run artifacts and failures.
- Supporting dry-run, apply, and resume behavior.

### Claude / Claudian Entry

Use `.claude/skills/beautify-md.md` as the Claude-facing skill entry. Update it, if needed, so Claude agents call the shared core workflow instead of manually editing files one by one.

Optional later additions:

- `.claude/agents/md-beautify-concepts.md`
- `.claude/commands/md-beautify-concepts.md`

### Codex / MathOS Entry

Add a Codex/MathOS-style skill such as:

```text
skills/mathos-md-beautify-concepts/
  SKILL.md
  scripts/
  references/
```

This skill should be thin. It should describe when to use the workflow, which commands to run, and how to inspect run-state artifacts. The implementation should stay in the shared core scripts so Claude and Codex use the same behavior.

## Input Scope

Inputs can be:

- One `.md` file.
- One directory containing Markdown files.

Directory input expands recursively to matching `.md` files.

Default skipped paths:

- `概念/`
- `images/`
- `.git/`
- `.obsidian/`
- `.claude/`
- `.claudian/`
- `agent-memory/`
- `docs/superpowers/specs/`

The workflow should not process already extracted concept files unless the user explicitly requests that.

## File-Level Flow

For each source Markdown file:

1. Read the original Markdown as UTF-8.
2. Build one LLM request containing:
   - The source Markdown.
   - The current beautification and concept extraction rules.
   - A strict output schema.
3. Ask the LLM to return structured JSON with:
   - `formatted_markdown`: source Markdown after beautification and concept-link replacement.
   - `concept_files`: concept files to create under `概念/`.
   - `risk_notes`: uncertain decisions or skipped candidates.
4. Validate the JSON and content preservation gates.
5. In dry-run mode, write candidates and diffs only.
6. In apply mode, write the formatted source file and concept files only if validation passes.
7. Save per-file state and summary artifacts.

## LLM Output Contract

The model must return valid JSON, not prose.

Required top-level fields:

```json
{
  "formatted_markdown": "...",
  "concept_files": [
    {
      "name": "线段.md",
      "title": "线段",
      "body": "..."
    }
  ],
  "risk_notes": [
    "..."
  ]
}
```

Rules:

- `formatted_markdown` must be the complete replacement text for the source file.
- Concept links must use `[[概念/概念名]]`.
- Concept file names must be direct children of `概念/`; nested categories are not allowed.
- Concept files must contain only concepts explicitly defined in the current source file/chapter.
- Do not extract concepts merely mentioned or used without definition.
- Do not delete valid source content.
- Do not change mathematical meaning, exercise conditions, proofs, formulas, image paths, tables, or links.

## Validation Gates

A file may be written only when all required gates pass.

Required gates:

- JSON parses successfully.
- `formatted_markdown` is non-empty and not suspiciously shorter than the original.
- Markdown code fence count remains balanced.
- Math block delimiter count remains balanced.
- Image references are not reduced unless the removed reference is provably duplicate junk.
- Existing Wikilinks remain syntactically valid.
- Every new `[[概念/...]]` link has a corresponding concept file in the output or already exists under the sibling `概念/` folder.
- Concept file paths stay inside the sibling `概念/` folder.
- The source file is not modified when validation fails.

Recommended warning gates:

- Large text-size changes.
- Large heading-count changes.
- Large table-count changes.
- Added concept with very short or vague body.
- Concept file name collision with different existing content.

## Commands

Proposed command shape:

```powershell
python scripts/md_beautify_concepts.py plan "path\to\file-or-folder"
python scripts/md_beautify_concepts.py run "path\to\file-or-folder" --dry-run
python scripts/md_beautify_concepts.py run "path\to\file-or-folder" --apply
python scripts/md_beautify_concepts.py resume "agent-memory\records\<run-id>"
```

Behavior:

- `plan` scans and reports targets without calling the LLM.
- `run --dry-run` calls the LLM and writes candidates/artifacts but does not modify source files.
- `run --apply` calls the LLM and writes only files that pass validation.
- `resume` continues an interrupted or failed run using saved state.

## Run Artifacts

Each run should write a record folder:

```text
agent-memory/records/YYYY-MM-DD-md-beautify-concepts-<slug>/
  manifest.json
  run-state.json
  result-summary.json
  failures.json
  candidates/
  diffs/
  llm-responses/
```

Artifact purpose:

- `manifest.json`: all candidate source files and skip reasons.
- `run-state.json`: resumable per-file status.
- `result-summary.json`: compact success/failure summary for agents.
- `failures.json`: failed files, failed stage, and artifact pointers.
- `candidates/`: dry-run or failed candidate outputs.
- `diffs/`: source-to-candidate diffs.
- `llm-responses/`: raw model responses for audit and debugging.

## Error Handling

Fail closed for a file when:

- The LLM returns invalid JSON.
- Required fields are missing.
- Validation gates fail.
- A concept path would escape `概念/`.
- A source file changed on disk after planning and before apply.

The run may continue to later files, but failed files must not be partially written.

## Testing Strategy

Focused tests should cover:

- Single-file plan and dry-run.
- Folder expansion and skip rules.
- Concept file path safety.
- JSON validation failure.
- Missing concept file for new Wikilink.
- Existing concept collision behavior.
- UTF-8 Chinese paths.
- Protection of images, formulas, tables, and Wikilinks.

Use small fixture Markdown files rather than full textbook chapters for unit tests.

## Open Implementation Decisions

These can be decided during implementation:

- Exact LLM provider interface and environment variables.
- Whether `--apply` should stop on first failure or continue by default.
- Exact threshold for suspicious content shrinkage.
- Whether to overwrite existing same-name concept files when content is identical.

Default conservative choices:

- Continue after per-file failures, but report them clearly.
- Never overwrite conflicting existing concept files without recording a failure.
- Use dry-run as the recommended first command.
