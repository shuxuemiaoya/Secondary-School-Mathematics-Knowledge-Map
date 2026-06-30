import argparse
import json
from pathlib import Path

from md_beautify_concepts.console import safe_print
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
            safe_print(target)
        return 0

    if args.fixture_response is None:
        raise SystemExit("--fixture-response is required until the real LLM provider is configured")

    response = json.loads(args.fixture_response.read_text(encoding="utf-8"))
    provider = FixtureProvider({Path(args.path).resolve(): response})
    if args.dry_run:
        record = run_dry(args.path, args.record_dir, provider)
    else:
        record = run_apply(args.path, args.record_dir, provider)
    safe_print(record)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
