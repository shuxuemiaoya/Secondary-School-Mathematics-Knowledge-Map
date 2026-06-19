import os
from pathlib import Path
import re

def get_target_root():
    return input().strip()

def protect_blocks(text):
    blocks = []
    placeholders = []
    # protect fenced code blocks
    def repl_code(m):
        blocks.append(m.group(0))
        idx = len(blocks) - 1
        placeholder = f'__PROTECTED_BLOCK_{idx}__'
        placeholders.append(placeholder)
        return placeholder
    text = re.sub(r'```[\s\S]*?```', repl_code, text)
    # protect inline code
    def repl_inline(m):
        blocks.append(m.group(0))
        idx = len(blocks) - 1
        placeholder = f'__PROTECTED_BLOCK_{idx}__'
        placeholders.append(placeholder)
        return placeholder
    text = re.sub(r'`[^`]*`', repl_inline, text)
    # protect display math $$...$$
    def repl_dmath(m):
        blocks.append(m.group(0))
        idx = len(blocks) - 1
        placeholder = f'__PROTECTED_BLOCK_{idx}__'
        placeholders.append(placeholder)
        return placeholder
    text = re.sub(r'\$\$[\s\S]*?\$\$', repl_dmath, text)
    # protect inline math $...$
    def repl_imath(m):
        blocks.append(m.group(0))
        idx = len(blocks) - 1
        placeholder = f'__PROTECTED_BLOCK_{idx}__'
        placeholders.append(placeholder)
        return placeholder
    text = re.sub(r'(?<!\$)\$(?!\$)[^\$]*\$(?!\$)', repl_imath, text)
    # protect HTML blocks (including <details>, <table>, etc.)
    def repl_html(m):
        blocks.append(m.group(0))
        idx = len(blocks) - 1
        placeholder = f'__PROTECTED_BLOCK_{idx}__'
        placeholders.append(placeholder)
        return placeholder
    text = re.sub(r'<(details|table|tr|td|th|center|img)[^>]*>[\s\S]*?</\1>', repl_html, text, flags=re.IGNORECASE)
    # protect single HTML tags like <img .../>
    def repl_single_html(m):
        blocks.append(m.group(0))
        idx = len(blocks) - 1
        placeholder = f'__PROTECTED_BLOCK_{idx}__'
        placeholders.append(placeholder)
        return placeholder
    text = re.sub(r'<img[^>]*/?>', repl_single_html, text)
    # protect markdown images
    def repl_img(m):
        blocks.append(m.group(0))
        idx = len(blocks) - 1
        placeholder = f'__PROTECTED_BLOCK_{idx}__'
        placeholders.append(placeholder)
        return placeholder
    text = re.sub(r'!\[.*?\]\(.*?\)', repl_img, text)
    # protect obsidian links/embeds
    def repl_obsidian(m):
        blocks.append(m.group(0))
        idx = len(blocks) - 1
        placeholder = f'__PROTECTED_BLOCK_{idx}__'
        placeholders.append(placeholder)
        return placeholder
    text = re.sub(r'!?\[\[.*?\]\]', repl_obsidian, text)
    # protect callouts >[!...]
    def repl_callout(m):
        blocks.append(m.group(0))
        idx = len(blocks) - 1
        placeholder = f'__PROTECTED_BLOCK_{idx}__'
        placeholders.append(placeholder)
        return placeholder
    text = re.sub(r'^>\s*\[!.*?\].*$', repl_callout, text, flags=re.MULTILINE)
    # protect YAML frontmatter
    def repl_yaml(m):
        blocks.append(m.group(0))
        idx = len(blocks) - 1
        placeholder = f'__PROTECTED_BLOCK_{idx}__'
        placeholders.append(placeholder)
        return placeholder
    if text.startswith('---'):
        m = re.match(r'^---[\s\S]*?---\n', text)
        if m:
            text = repl_yaml(m)
    # protect heading lines
    def repl_heading(m):
        blocks.append(m.group(0))
        idx = len(blocks) - 1
        placeholder = f'__PROTECTED_BLOCK_{idx}__'
        placeholders.append(placeholder)
        return placeholder
    text = re.sub(r'^#{1,6} .*$', repl_heading, text, flags=re.MULTILINE)
    return text, blocks, placeholders

def restore_blocks(text, blocks, placeholders):
    for i, placeholder in enumerate(placeholders):
        text = text.replace(placeholder, blocks[i], 1)
    return text

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    text, blocks, placeholders = protect_blocks(original)
    # conservative normalization: remove redundant emphasis markers
    # only when the enclosed text and line structure remain unchanged
    # remove ** or __ around a word/phrase if it's clearly redundant (e.g., **text** -> text)
    # but only if it doesn't affect protected content (already protected)
    # normalize whitespace: replace multiple spaces with single space, but not in protected blocks
    # We'll work on the text with placeholders
    # Remove redundant bold markers **...** where the content is a single word and no other formatting
    # This is safe because we already protected code, math, etc.
    # We'll do a simple pass: replace **word** with word if word has no spaces and no other markers
    # But to be conservative, we only do it for obvious cases like **text** where text is alphanumeric
    text = re.sub(r'\*\*([a-zA-Z0-9]+)\*\*', r'\1', text)
    # Remove redundant italic markers *...* similarly
    text = re.sub(r'(?<!\*)\*([a-zA-Z0-9]+)\*(?!\*)', r'\1', text)
    # Remove redundant underscore italic _..._
    text = re.sub(r'(?<!_)_([a-zA-Z0-9]+)_(?!_)', r'\1', text)
    # Normalize multiple spaces to single space (but not newlines)
    text = re.sub(r'[ \t]+', ' ', text)
    # Normalize spaces around newlines: remove spaces at end of lines
    text = re.sub(r' +\n', '\n', text)
    # Normalize multiple blank lines to at most one blank line
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = restore_blocks(text, blocks, placeholders)
    if text != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)

def main():
    root = get_target_root()
    root_path = Path(root)
    skip_dirs = {'.git', 'node_modules', '.obsidian', '.trash', '__pycache__'}
    for md_file in root_path.rglob('*.md'):
        # check if any parent directory is in skip_dirs
        if any(part in skip_dirs for part in md_file.relative_to(root_path).parts):
            continue
        replace_in_file(str(md_file))

if __name__ == "__main__":
    main()
