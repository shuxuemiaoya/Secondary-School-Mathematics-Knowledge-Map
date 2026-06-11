```python
import re

PLUGIN_ID = "math_content_cleaner"
PLUGIN_VERSION = "1.0.0"

def analyze(markdown: str) -> dict:
    """
    Analyze the markdown content for potential issues related to math formatting.
    Returns warnings and summary information.
    """
    warnings = []
    summary = []
    
    lines = markdown.split('\n')
    
    # Check for common math formatting issues
    for i, line in enumerate(lines, 1):
        # Check for mismatched inline math delimiters
        dollar_count = line.count('$')
        if dollar_count % 2 != 0 and dollar_count > 0:
            warnings.append(f"Line {i}: Odd number of $ signs - possible mismatched inline math")
        
        # Check for display math without proper spacing
        if '$$' in line:
            # Check if display math is on its own line
            stripped = line.strip()
            if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 4:
                warnings.append(f"Line {i}: Display math should be on its own line")
        
        # Check for common LaTeX errors
        if '\\left(' in line or '\\right)' in line:
            left_count = line.count('\\left(')
            right_count = line.count('\\right)')
            if left_count != right_count:
                warnings.append(f"Line {i}: Mismatched \\left( and \\right) pairs")
        
        if '\\left[' in line or '\\right]' in line:
            left_count = line.count('\\left[')
            right_count = line.count('\\right]')
            if left_count != right_count:
                warnings.append(f"Line {i}: Mismatched \\left[ and \\right] pairs")
    
    # Summary statistics
    total_math_expressions = len(re.findall(r'\$[^$]+\$', markdown))
    total_display_math = len(re.findall(r'\$\$[^$]+\$\$', markdown))
    
    summary.append(f"Found {total_math_expressions} inline math expressions")
    summary.append(f"Found {total_display_math} display math expressions")
    
    if warnings:
        summary.append(f"Found {len(warnings)} potential issues")
    
    return {
        "warnings": warnings,
        "summary": summary
    }

def clean(markdown: str) -> str:
    """
    Clean and normalize math formatting in markdown content.
    Preserves heading lines and fixes common math formatting issues.
    """
    lines = markdown.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Skip heading lines - preserve them exactly
        if line.startswith('#'):
            cleaned_lines.append(line)
            continue
        
        cleaned_line = line
        
        # Fix common LaTeX formatting issues
        
        # Ensure proper spacing around inline math
        # Replace patterns like "text$math$text" with "text $math$ text"
        cleaned_line = re.sub(r'([^\s])\$([^$\s])', r'\1 $\2', cleaned_line)
        cleaned_line = re.sub(r'([^$\s])\$([^\s])', r'\1$ \2', cleaned_line)
        
        # Fix display math that's not on its own line
        # If $$ appears in the middle of a line, split it
        if '$$' in cleaned_line and not cleaned_line.strip().startswith('$$'):
            parts = cleaned_line.split('$$')
            new_parts = []
            for j, part in enumerate(parts):
                if j % 2 == 0:  # Text parts
                    if part.strip():
                        new_parts.append(part)
                else:  # Math parts
                    if part.strip():
                        new_parts.append(f"\n$$\n{part.strip()}\n$$\n")
            cleaned_line = ''.join(new_parts)
        
        # Fix common LaTeX command errors
        # Replace \sinx with \sin x (add space after known commands)
        known_commands = ['sin', 'cos', 'tan', 'log', 'ln', 'lim', 'sum', 'prod', 'int']
        for cmd in known_commands:
            cleaned_line = re.sub(rf'\\{cmd}([a-zA-Z])', rf'\\{cmd} \1', cleaned_line)
        
        # Fix mismatched brackets in LaTeX
        # Ensure \left and \right are paired
        left_parens = cleaned_line.count('\\left(')
        right_parens = cleaned_line.count('\\right)')
        if left_parens > right_parens:
            # Add missing \right)
            cleaned_line += ' \\right)' * (left_parens - right_parens)
        elif right_parens > left_parens:
            # Add missing \left(
            cleaned_line = '\\left( ' * (right_parens - left_parens) + cleaned_line
        
        left_brackets = cleaned_line.count('\\left[')
        right_brackets = cleaned_line.count('\\right]')
        if left_brackets > right_brackets:
            cleaned_line += ' \\right]' * (left_brackets - right_brackets)
        elif right_brackets > left_brackets:
            cleaned_line = '\\left[ ' * (right_brackets - left_brackets) + cleaned_line
        
        cleaned_lines.append(cleaned_line)
    
    return '\n'.join(cleaned_lines)
```