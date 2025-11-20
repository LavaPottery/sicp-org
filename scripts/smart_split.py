import os
import sys
import re

def smart_split(file_path):
    if not os.path.exists(file_path):
        sys.exit(1)

    filename = os.path.basename(file_path)
    base_name = os.path.splitext(filename)[0]

    # Output to the same directory as input
    output_dir = os.path.dirname(file_path)
    if not output_dir:
        output_dir = "temp"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    parts = []
    current_part = []
    in_code_block = False

    # CONFIG: Flexible limits
    MIN_LINES = 60
    MAX_LINES = 150

    # REGEX: Matches ANY header (*, **, ***) or Footnote ([fn:1])
    header_pattern = re.compile(r'^(\*+)\s')
    footnote_pattern = re.compile(r'^\[fn:\d+\]')

    for line in lines:
        if re.match(r'^\s*#\+begin_', line, re.IGNORECASE):
            in_code_block = True
        if re.match(r'^\s*#\+end_', line, re.IGNORECASE):
            in_code_block = False

        is_header = header_pattern.match(line)
        is_footnote = footnote_pattern.match(line)
        is_blank = line.strip() == ""

        # LOGIC: Flexible Split
        should_split = False

        if not in_code_block and len(current_part) >= MIN_LINES:
            if is_header:
                should_split = True
            elif is_footnote:
                should_split = True
            elif is_blank and len(current_part) >= MAX_LINES:
                should_split = True

        if should_split:
            parts.append(current_part)
            current_part = []

        current_part.append(line)

    if current_part:
        parts.append(current_part)

    # Verification
    original_content = "".join(lines)
    reconstructed_content = "".join(["".join(p) for p in parts])

    if original_content != reconstructed_content:
        print("FATAL ERROR: Verification failed.")
        sys.exit(1)

    for i, part_lines in enumerate(parts):
        # Naming convention: filename-sub01.org
        part_filename = f"{base_name}-sub{i+1:02d}.org"
        with open(os.path.join(output_dir, part_filename), 'w', encoding='utf-8') as f:
            f.writelines(part_lines)

if __name__ == "__main__":
    smart_split(sys.argv[1])
