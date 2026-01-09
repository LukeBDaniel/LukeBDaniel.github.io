import sys
import re

md_path = sys.argv[1]

in_code = False
keep = False
in_html_block = False
output = []
block = []

def should_skip_line(line, prev_line_was_warning=False):
    """Check if a line should be skipped (output, warnings, errors, etc.)"""
    line_stripped = line.strip()
    
    # Skip empty lines that are just whitespace (but preserve warning state)
    if not line_stripped:
        return prev_line_was_warning, prev_line_was_warning
    
    # Skip warning messages (including multi-line warnings)
    if re.search(r':\s*(SettingWithCopyWarning|FutureWarning|DeprecationWarning|UserWarning)', line):
        return True, True  # Mark that we're in a warning block
    
    # Continue skipping if we're in a warning block (until we hit code or markdown content)
    if prev_line_was_warning:
        # Stop if we hit a line that looks like code or markdown content
        if re.match(r'^\s*(```|#|def |import |from |class )', line_stripped):
            return False, False
        # Continue skipping warning continuation lines
        if re.match(r'^\s*(Try using|See the|A value|\.loc\[)', line_stripped):
            return True, True
        # Skip indented code lines that are part of warning traceback
        if re.match(r'^\s{2,}[\w\[\]"]+\s*=', line_stripped) and len(line_stripped) < 100:
            return True, True
        # Stop if we hit what looks like actual content (long lines that aren't warnings)
        if len(line_stripped) > 50 and not re.match(r'^\s*[A-Z]', line_stripped):
            return False, False
        # Continue skipping short lines that are likely part of warning
        if len(line_stripped) < 100:
            return True, True
        return False, False
    
    # Skip error messages that start with "Failed for"
    if re.match(r'^\s*Failed for\s+', line_stripped):
        return True, False
    
    # Skip file paths that are output (like /var/folders/... or http://)
    if re.match(r'^\s*(/var/|/tmp/|http://|https://)', line_stripped):
        return True, False
    
    # Skip lines that are just file paths with line numbers
    if re.match(r'^\s*/.*\.py:\d+:', line_stripped):
        return True, True  # This is usually the start of a warning
    
    # HTML blocks are handled separately, don't skip here
    
    return False, False

with open(md_path) as f:
    lines = f.readlines()

i = 0
in_warning_block = False
while i < len(lines):
    line = lines[i]
    
    # Check for HTML block start (div, style, table)
    # Handle nested HTML blocks by tracking depth
    if re.match(r'^\s*<(div|style|table)', line.strip()):
        tag_match = re.match(r'^\s*<(\w+)', line.strip())
        if tag_match:
            tag_name = tag_match.group(1)
            opening_tag = f'<{tag_name}'
            closing_tag = f'</{tag_name}>'
            depth = 1
            i += 1  # Skip the opening tag
            # Skip until we find matching closing tag (handles nesting)
            while i < len(lines) and depth > 0:
                if opening_tag in lines[i] and not closing_tag in lines[i]:
                    depth += 1
                elif closing_tag in lines[i]:
                    depth -= 1
                i += 1
        continue
    
    if line.startswith("```"):
        in_warning_block = False  # Reset warning state when entering code block
        if in_code and keep:
            # Remove the tag line before writing
            cleaned_block = [l for l in block if "# INCLUDE" not in l]
            output.extend(cleaned_block)
            output.append(line)
        elif not in_code:
            block = [line]
        in_code = not in_code
        keep = False
        i += 1
        continue
    
    if in_code:
        block.append(line)
        if "# INCLUDE" in line:
            keep = True
    else:
        # Skip unwanted output lines (including multi-line warnings)
        should_skip, continue_warning = should_skip_line(line, in_warning_block)
        in_warning_block = continue_warning
        if not should_skip:
            output.append(line)
            in_warning_block = False  # Reset if we're outputting content
    
    i += 1

with open(md_path, "w") as f:
    f.writelines(output)
