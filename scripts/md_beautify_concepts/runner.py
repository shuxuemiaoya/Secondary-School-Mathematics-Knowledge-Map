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
