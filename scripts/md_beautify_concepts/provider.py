import json
from pathlib import Path
from typing import Protocol


class Provider(Protocol):
    def complete_file(self, source_path: Path, prompt: str) -> str:
        ...


class FixtureProvider:
    def __init__(self, responses: dict[Path, dict]) -> None:
        self.responses = {path.resolve(): response for path, response in responses.items()}

    def complete_file(self, source_path: Path, prompt: str) -> str:
        del prompt
        try:
            response = self.responses[source_path.resolve()]
        except KeyError as exc:
            raise ValueError(f"No fixture response for {source_path}") from exc
        return json.dumps(response, ensure_ascii=False)
