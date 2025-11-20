import os
import sys
import re

def smart_split(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

    filename = os.path.basename(file_path)
    base_name = os.path.splitext(filename)[0]
    
    # Ensure temp directory exists
    if not os.path.exists("temp"):
        os.makedirs("temp")

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    parts = []
    current_part = []
    in_code_block = False
    
    # CONFIGURATION: The Safety Nets
    MIN_LINES = 60      # Don't split tiny crumbs
    MAX_LINES = 150     # Soft Limit: Look for a clean break if we get this big
    HARD_LIMIT = 300    # Hard Limit: Force a break (not implemented yet to avoid breaking code, relying on soft limit logic)
    
    # REGEX 1: Universal Headers (Matches *, **, ***, ****, *****...)
    header_pattern = re.compile(r'^(\*+)\s')
    
    # REGEX 2: Footnote definitions (e.g., [fn:1])
    footnote_pattern = re.compile(r'^\[fn:\d+\]')

    for line in lines:
        # 1. Code Block Protection (The "Sacred Text" Rule)
        if re.match(r'^\s*#\+begin_', line, re.IGNORECASE):
            in_code_block = True
        if re.match(r'^\s*#\+end_', line, re.IGNORECASE):
            in_code_block = False

        is_header = header_pattern.match(line)
        is_footnote = footnote_pattern.match(line)
        is_blank = line.strip() == ""
        
        # 2. Split Logic
        should_split = False
        
        # Only split if we aren't inside a code block and we have enough content
        if not in_code_block and len(current_part) >= MIN_LINES:
            # Priority A: Logical Structure
            if is_header:
                should_split = True
            elif is_footnote:
                should_split = True
            # Priority B: Safety Valve (File is getting too big, find a blank line)
            elif is_blank and len(current_part) >= MAX_LINES:
                should_split = True

        if should_split:
            parts.append(current_part)
            current_part = []
        
        current_part.append(line)

    # Catch the last part
    if current_part:
        parts.append(current_part)

    # 3. Verification (Byte-Perfect Check)
    original_content = "".join(lines)
    reconstructed_content = "".join(["".join(p) for p in parts])
    
    if original_content != reconstructed_content:
        print("FATAL ERROR: Split verification failed. Data would be lost.")
        sys.exit(1)

    # 4. Write Output
    print(f"Processing {filename}...")
    print(f"Universal Split: Created {len(parts)} parts.")
    
    for i, part_lines in enumerate(parts):
        part_filename = f"{base_name}-part{i+1:02d}.org"
        first_line = part_lines[0].strip()[:50]
        # Write to temp/
        with open(os.path.join("temp", part_filename), 'w', encoding='utf-8') as f:
            f.writelines(part_lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/smart_split.py <filepath>")
        sys.exit(1)
    smart_split(sys.argv[1])
