import os
import sys
import re

# USAGE: python3 scripts/smart_split.py org-castilian/sicp3-2.org

def smart_split(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

    filename = os.path.basename(file_path)
    base_name = os.path.splitext(filename)[0]
    
    # Ensure temp exists
    if not os.path.exists("temp"):
        os.makedirs("temp")

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    parts = []
    current_part = []
    in_code_block = False
    
    # Regex: Matches *, **, or *** followed by a space
    header_pattern = re.compile(r'^(\*{1,3})\s')

    for line in lines:
        # Track if we are inside a source block to PREVENT splitting there
        if re.match(r'^\s*#\+begin_', line, re.IGNORECASE):
            in_code_block = True
        if re.match(r'^\s*#\+end_', line, re.IGNORECASE):
            in_code_block = False

        # Check for split point
        # 1. Is it a header?
        # 2. Are we outside a code block?
        # 3. Do we have enough content in the buffer? (> 50 lines)
        if header_pattern.match(line) and not in_code_block and len(current_part) > 50:
            parts.append(current_part)
            current_part = []
        
        current_part.append(line)

    # Append the last accumulated part
    if current_part:
        parts.append(current_part)

    # VERIFICATION STEP
    # Ensures the concatenated parts exactly match the original file bytes
    original_content = "".join(lines)
    reconstructed_content = "".join(["".join(p) for p in parts])
    
    if original_content != reconstructed_content:
        print("FATAL ERROR: Split verification failed. Data would be lost.")
        print(f"Original length: {len(original_content)}")
        print(f"Reconstructed length: {len(reconstructed_content)}")
        sys.exit(1)

    # Write parts to temp/
    print(f"Processing {filename}...")
    print(f"Splitting into {len(parts)} logical parts in temp/...")
    
    for i, part_lines in enumerate(parts):
        part_filename = f"{base_name}-part{i+1:02d}.org"
        
        # Print the start of the section for confirmation
        first_line = part_lines[0].strip()[:60]
        print(f"  - {part_filename}: {len(part_lines)} lines (Starts: {first_line}...)")
        
        with open(os.path.join("temp", part_filename), 'w', encoding='utf-8') as f:
            f.writelines(part_lines)

    print("Done.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/smart_split.py <filepath>")
        sys.exit(1)
    smart_split(sys.argv[1])
