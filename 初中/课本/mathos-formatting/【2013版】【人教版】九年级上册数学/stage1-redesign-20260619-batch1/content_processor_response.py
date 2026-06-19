```python
import os
from pathlib import Path
import re

def get_target_root():
    return input().strip()

def protect_blocks(text):
    # Protect fenced code blocks
    code_blocks = []
    def code_replacer(m):
        code_blocks.append(m.group(0))
        return f"__CODEBLOCK_{len(code_blocks)-1}__"
    text = re.sub(r'```[\s\S]*?```', code_replacer, text)
    
    # Protect inline code
    inline_codes = []
    def inline_code_replacer(m):
        inline_codes.append(m.group(0))
        return f"__INLINECODE_{len(inline_codes)-1}__"
    text = re.sub(r'`[^`]+`', inline_code_replacer, text)
    
    # Protect display math ($$...$$)
    display_maths = []
    def display_math_replacer(m):
        display_maths.append(m.group(0))
        return f"__DISPLAYMATH_{len(display_maths)-1}__"
    text = re.sub(r'\$\$[\s\S]*?\$\$', display_math_replacer, text)
    
    # Protect inline math ($...$)
    inline_maths = []
    def inline_math_replacer(m):
        inline_maths.append(m.group(0))
        return f"__INLINEMATH_{len(inline_maths)-1}__"
    text = re.sub(r'(?<!\$)\$(?!\$)[^\$]+\$(?!\$)', inline_math_replacer, text)
    
    # Protect details blocks
    details_blocks = []
    def details_replacer(m):
        details_blocks.append(m.group(0))
        return f"__DETAILSBLOCK_{len(details_blocks)-1}__"
    text = re.sub(r'<details>[\s\S]*?</details>', details_replacer, text, flags=re.IGNORECASE)
    
    # Protect HTML blocks (simple tags)
    html_blocks = []
    def html_replacer(m):
        html_blocks.append(m.group(0))
        return f"__HTMLBLOCK_{len(html_blocks)-1}__"
    text = re.sub(r'<[^>]+>', html_replacer, text)
    
    # Protect image references
    images = []
    def image_replacer(m):
        images.append(m.group(0))
        return f"__IMAGE_{len(images)-1}__"
    text = re.sub(r'!\[.*?\]\(.*?\)', image_replacer, text)
    
    # Protect Obsidian links/embeds
    obsidian_links = []
    def obsidian_replacer(m):
        obsidian_links.append(m.group(0))
        return f"__OBSIDIAN_{len(obsidian_links)-1}__"
    text = re.sub(r'\[\[.*?\]\]', obsidian_replacer, text)
    
    # Protect callouts (> [!...])
    callouts = []
    def callout_replacer(m):
        callouts.append(m.group(0))
        return f"__CALLOUT_{len(callouts)-1}__"
    text = re.sub(r'>\s*\[!.*?\][\s\S]*?(?=\n\n|\Z)', callout_replacer, text)
    
    # Protect template variables
    template_vars = []
    def template_replacer(m):
        template_vars.append(m.group(0))
        return f"__TEMPLATE_{len(template_vars)-1}__"
    text = re.sub(r'{{.*?}}', template_replacer, text)
    
    # Protect heading lines
    headings = []
    def heading_replacer(m):
        headings.append(m.group(0))
        return f"__HEADING_{len(headings)-1}__"
    text = re.sub(r'^#{1,6} .*$', heading_replacer, text, flags=re.MULTILINE)
    
    # Protect Markdown tables
    tables = []
    def table_replacer(m):
        tables.append(m.group(0))
        return f"__TABLE_{len(tables)-1}__"
    text = re.sub(r'^[|].*$', table_replacer, text, flags=re.MULTILINE)
    
    return text, {
        'code_blocks': code_blocks,
        'inline_codes': inline_codes,
        'display_maths': display_maths,
        'inline_maths': inline_maths,
        'details_blocks': details_blocks,
        'html_blocks': html_blocks,
        'images': images,
        'obsidian_links': obsidian_links,
        'callouts': callouts,
        'template_vars': template_vars,
        'headings': headings,
        'tables': tables
    }

def restore_blocks(text, blocks):
    # Restore in reverse order to avoid placeholder conflicts
    for key in ['tables', 'headings', 'template_vars', 'callouts', 'obsidian_links', 'images', 'html_blocks', 'details_blocks', 'inline_maths', 'display_maths', 'inline_codes', 'code_blocks']:
        for i, block in enumerate(blocks[key]):
            placeholder = f"__{key.upper()}_{i}__"
            text = text.replace(placeholder, block)
    return text

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    text = original
    
    # Protect blocks
    protected_text, blocks = protect_blocks(text)
    
    # Normalize whitespace (conservative)
    # Remove trailing whitespace from lines
    protected_text = re.sub(r'[ \t]+$', '', protected_text, flags=re.MULTILINE)
    # Ensure single blank line between paragraphs (but not inside protected blocks)
    protected_text = re.sub(r'\n{3,}', '\n\n', protected_text)
    
    # Remove redundant emphasis markers (only when safe)
    # Remove double asterisks around text that is already bolded by other means? No, too risky.
    # Only remove obvious formatting typos like **text** where it's clearly a typo for *text*? No, too risky.
    
    # Restore blocks
    result = restore_blocks(protected_text, blocks)
    
    # Write only if changed
    if result != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)

def main():
    root = get_target_root()
    root_path = Path(root)
    skip_dirs = {'.git', 'node_modules', '.obsidian', '.trash', '__pycache__'}
    
    for md_file in root_path.rglob('*.md'):
        # Check if any parent directory is in skip list
        should_skip = False
        for parent in md_file.parents:
            if parent.name in skip_dirs:
                should_skip = True
                break
        if should_skip:
            continue
        
        replace_in_file(str(md_file))

if __name__ == "__main__":
    main()
```