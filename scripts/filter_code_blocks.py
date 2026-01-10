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
    # Skip standalone URLs/paths that are just output (not in sentences)
    if re.match(r'^\s*(/var/|/tmp/|http://|https://)', line_stripped):
        # Skip if it's a short standalone URL/path (likely output)
        if len(line_stripped) < 200:
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
in_traceback_block = False
while i < len(lines):
    line = lines[i]
    
    # Check for Traceback/Error blocks
    # Separator lines (----------) mark traceback blocks - skip everything between separators
    if re.match(r'^\s*-{10,}', line.strip()):  # Separator line (----------)
        if in_traceback_block:
            # This separator ends the traceback block
            in_traceback_block = False
            i += 1  # Skip ending separator
            continue
        else:
            # Check if next lines contain traceback content
            # Look ahead a few lines to see if this is a traceback block
            lookahead = min(5, len(lines) - i - 1)
            is_traceback = False
            for j in range(1, lookahead + 1):
                if i + j < len(lines):
                    next_line = lines[i + j]
                    if re.search(r'(Traceback|Error|Exception|KeyboardInterrupt|KeyError|ValueError|File ~|Input In|--->)', next_line):
                        is_traceback = True
                        break
                    # If we hit another separator or content, stop looking
                    if re.match(r'^\s*-{10,}|^\s*!\[|^\s*#\s+[A-Z]', next_line.strip()):
                        break
            if is_traceback:
                in_traceback_block = True
                i += 1  # Skip separator
                continue
    
    # Also check for traceback start without separator
    if not in_traceback_block and re.search(r'\s+(KeyboardInterrupt|KeyError|ValueError|TypeError|AttributeError|IndexError)\s+Traceback', line):
        in_traceback_block = True
        i += 1
        continue
    
    if in_traceback_block:
        # Skip until we hit another separator (marks end of traceback)
        if re.match(r'^\s*-{10,}', line.strip()):
            in_traceback_block = False
            i += 1
            continue
        # Skip ALL lines in traceback block - they're all error output
        # This includes: File paths, line numbers, code snippets, error messages
        # Only stop if we hit clear content markers (images, headings, code blocks)
        if re.match(r'^\s*!\[|^\s*#\s+[A-Z]|^\s*```', line.strip()):
            # Hit an image, heading, or code block - end traceback
            in_traceback_block = False
        elif re.match(r'^\s*[A-Z][a-z]+', line.strip()) and len(line.strip()) > 30 and not re.search(r'(File |Input |--->|Traceback)', line):
            # Hit a substantial sentence that's not traceback - might be content
            # But be conservative - if it has traceback markers, keep skipping
            if not re.search(r'(File |Input |--->|\d+\s+\||Traceback)', line):
                in_traceback_block = False
            else:
                i += 1
                continue
        else:
            # Skip this line (it's part of the traceback)
            i += 1
            continue
    
    # Check for traceback start without separator
    if re.search(r'\s+(KeyboardInterrupt|KeyError|ValueError|TypeError|AttributeError|IndexError)\s+Traceback', line):
        in_traceback_block = True
        i += 1
        continue
    
    # Check for standalone error lines (like "KeyboardInterrupt:" or "KeyError: 'Tm'")
    if re.match(r'^\s*(KeyboardInterrupt|KeyError|ValueError|TypeError|AttributeError|IndexError|NameError|ImportError):', line.strip()):
        in_traceback_block = True
        i += 1
        continue
    
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
