```python
import re
from typing import List, Dict

PLUGIN_ID = "content_cleaner"
PLUGIN_VERSION = "1.0.0"


def analyze(markdown: str) -> Dict[str, List[str]]:
    """
    Analyze the markdown content and return warnings and a summary.
    """
    warnings: List[str] = []
    summary: List[str] = []

    # Count images
    images = re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", markdown)
    summary.append(f"Number of images: {len(images)}")

    # Count tables (simple heuristic: lines starting with | or containing | as table rows)
    table_rows = [line for line in markdown.splitlines() if line.strip().startswith("|")]
    summary.append(f"Lines that look like table rows: {len(table_rows)}")

    # Count <details> blocks
    details_open = len(re.findall(r"<details>", markdown))
    details_close = len(re.findall(r"</details>", markdown))
    summary.append(f"<details> blocks: {details_open} open, {details_close} close")

    if details_open != details_close:
        warnings.append("Mismatch between <details> and </details> tags.")

    # Count math blocks (display math)
    math_blocks = len(re.findall(r"\${2}", markdown))
    if math_blocks % 2 != 0:
        warnings.append("Odd number of $$ markers; possible unclosed math block.")
    summary.append(f"Display math markers ($$): {math_blocks}")

    # Check images with empty alt texts
    empty_alts = [path for alt, path in images if alt.strip() == ""]
    if empty_alts:
        warnings.append(f"{len(empty_alts)} image(s) have empty alt text.")

    # Very long alt texts (potential issues)
    long_alts = [(alt.strip(), path) for alt, path in images if len(alt) > 200]
    if long_alts:
        warnings.append(f"{len(long_alts)} image(s) have alt text longer than 200 characters.")

    # Report any line that starts with spaces and could be interpreted as code block
    code_like = [line for line in markdown.splitlines() if line.startswith("    ") and line.strip()]
    if code_like:
        summary.append(f"Indented lines (potential code blocks): {len(code_like)}")

    # Check for potential accidental deletion indicators (verbose)
    # (Nothing to warn about here beyond the above)

    return {
        "warnings": warnings,
        "summary": summary
    }


def clean(markdown: str) -> str:
    """
    Conservatively normalize the markdown formatting:
    - remove redundant blank lines
    - normalize surrounding whitespace
    - normalize image alt text without modifying paths or deleting images
    - fix spacing around headings
    Preserve all content, including math, details blocks, tables, images.
    """
    # Split into lines, preserving original line terminators? We'll use splitlines(True) to keep \n.
    # However, it's easier to work with a list of lines and join with \n at the end.
    lines = markdown.splitlines(keepends=False)  # without newline chars
    cleaned_lines: List[str] = []

    # First pass: normalize image alt texts (strip and collapse spaces)
    image_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

    def normalize_image(line: str) -> str:
        def repl(match):
            alt = match.group(1)
            path = match.group(2)
            # Normalize alt: strip and replace multiple whitespace with single space
            alt = " ".join(alt.strip().split())
            return f"![{alt}]({path})"
        return image_pattern.sub(repl, line)

    normalized_lines = [normalize_image(line) for line in lines]

    # Remove leading/trailing blank lines
    while normalized_lines and normalized_lines[0] == "":
        normalized_lines.pop(0)
    while normalized_lines and normalized_lines[-1] == "":
        normalized_lines.pop()

    # Collapse consecutive blank lines into at most one blank line (i.e., two consecutive empty strings become one)
    prev_blank = False
    for line in normalized_lines:
        if line == "":
            if not prev_blank:
                cleaned_lines.append("")
                prev_blank = True
        else:
            cleaned_lines.append(line)
            prev_blank = False

    # Ensure single blank line before and after headings (lines starting with #)
    i = 0
    while i < len(cleaned_lines):
        line = cleaned_lines[i]
        if line.lstrip().startswith("#"):  # heading
            # Insert a blank line before heading if not already present and not at the beginning
            if i > 0 and cleaned_lines[i-1] != "":
                cleaned_lines.insert(i, "")
                i += 1  # skip the inserted blank
            # Insert a blank line after heading if not at the end and next line is not blank
            if i + 1 < len(cleaned_lines) and cleaned_lines[i+1] != "":
                cleaned_lines.insert(i+1, "")
            i += 1
        else:
            i += 1

    # Join lines with newline character
    result = "\n".join(cleaned_lines)

    # Ensure the result ends with a single newline (some markdown processors prefer that)
    if not result.endswith("\n"):
        result += "\n"

    return result
```