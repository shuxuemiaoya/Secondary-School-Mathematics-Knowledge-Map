PLUGIN_ID = "chinese_textbook_cleaner"
PLUGIN_VERSION = "1.0.0"

def analyze(markdown: str) -> dict:
    """
    Analyze the given Markdown text and return warnings and summary.
    Warnings and summary are flat lists of strings.
    """
    lines = markdown.splitlines()
    image_count = 0
    details_count = 0
    in_details = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("![]("):
            image_count += 1
        if stripped.startswith("<details>"):
            details_count += 1
            in_details = True
        elif stripped.startswith("</details>"):
            in_details = False

    warnings = []
    if image_count > 0:
        warnings.append(
            f"Found {image_count} image markdown lines that may be removed by the cleaner."
        )
    if details_count > 0:
        warnings.append(
            f"Found {details_count} <details> blocks that may be removed by the cleaner."
        )

    summary = [
        f"Image references: {image_count}",
        f"Details blocks: {details_count}",
    ]
    return {"warnings": warnings, "summary": summary}


def clean(markdown: str) -> str:
    """
    Remove image formatting and <details> blocks from the Markdown text.
    Heading lines are not modified.
    """
    lines = markdown.splitlines()
    cleaned_lines = []
    in_details = False

    for line in lines:
        stripped = line.strip()

        # Handle <details> blocks: remove everything between <details> and </details>
        if stripped.startswith("<details>"):
            in_details = True
            continue
        if in_details:
            if stripped.startswith("</details>"):
                in_details = False
            continue

        # Remove lines that start with an image markdown reference
        if stripped.startswith("![]("):
            continue

        # Keep the line as-is
        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)