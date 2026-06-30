import sys
import os
from errno import EINVAL


def safe_print(value: object) -> None:
    text = str(value)
    encoding = sys.stdout.encoding or "utf-8"
    safe_text = text.encode(encoding, errors="backslashreplace").decode(encoding)
    try:
        print(safe_text)
    except BrokenPipeError:
        _silence_stdout()
        return
    except OSError as exc:
        if exc.errno == EINVAL:
            _silence_stdout()
            return
        raise


def _silence_stdout() -> None:
    sys.stdout = open(os.devnull, "w", encoding="utf-8")
