#!/usr/bin/env python3
"""
Split an org file into blocks and create part files with 3 blocks each.
Block types: paragraph, code block, heading, list
"""

import sys
import re

def parse_into_blocks(lines):
    """Parse lines into blocks."""
    blocks = []
    current_block = []
    current_type = None
    in_code_block = False
    in_list = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check for code block start/end
        if line.strip().startswith('#+begin'):
            if current_block and current_type:
                blocks.append((current_type, current_block))
                current_block = []
            current_block.append(line)
            current_type = 'code'
            in_code_block = True
            i += 1
            continue

        if line.strip().startswith('#+end'):
            current_block.append(line)
            blocks.append((current_type, current_block))
            current_block = []
            current_type = None
            in_code_block = False
            i += 1
            continue

        # If in code block, just append
        if in_code_block:
            current_block.append(line)
            i += 1
            continue

        # Check for heading (starts with *)
        if line.strip().startswith('**'):
            if current_block and current_type:
                blocks.append((current_type, current_block))
                current_block = []
            # Heading block includes the heading and its properties
            current_block.append(line)
            current_type = 'heading'
            i += 1
            # Include :properties: block if present
            while i < len(lines) and (lines[i].strip().startswith(':') or not lines[i].strip()):
                current_block.append(lines[i])
                i += 1
                if lines[i-1].strip() == ':end:':
                    break
            blocks.append((current_type, current_block))
            current_block = []
            current_type = None
            continue

        # Check for list item (starts with -)
        if line.strip().startswith('-') or line.strip().startswith('a.') or line.strip().startswith('b.') or line.strip().startswith('c.') or line.strip().startswith('d.'):
            if current_type != 'list':
                if current_block and current_type:
                    blocks.append((current_type, current_block))
                current_block = []
                current_type = 'list'
            current_block.append(line)
            i += 1
            continue

        # Check for empty line
        if not line.strip():
            if current_block and current_type:
                if current_type == 'list':
                    # Empty line might end the list, but check next line
                    if i + 1 < len(lines) and (lines[i + 1].strip().startswith('-') or
                                               lines[i + 1].strip().startswith('a.') or
                                               lines[i + 1].strip().startswith('b.')):
                        current_block.append(line)
                    else:
                        blocks.append((current_type, current_block))
                        current_block = []
                        current_type = None
                else:
                    # End current paragraph
                    blocks.append((current_type, current_block))
                    current_block = []
                    current_type = None
            i += 1
            continue

        # Regular text line
        if current_type is None:
            current_type = 'paragraph'
        elif current_type == 'list':
            # End list if not a list line
            blocks.append((current_type, current_block))
            current_block = []
            current_type = 'paragraph'

        current_block.append(line)
        i += 1

    # Don't forget the last block
    if current_block and current_type:
        blocks.append((current_type, current_block))

    return blocks

def split_into_parts(blocks):
    """Split blocks into parts with 3 blocks each."""
    parts = []
    i = 0

    while i < len(blocks):
        remaining = len(blocks) - i

        if remaining >= 3:
            # Normal case: take 3 blocks
            parts.append(blocks[i:i+3])
            i += 3
        elif remaining == 2:
            # 2 blocks left: save as final part with 2 blocks
            parts.append(blocks[i:i+2])
            i += 2
        elif remaining == 1:
            # 1 block left: go back and split last 4 blocks into 2+2
            if len(parts) > 0:
                # Remove last part (which had 3 blocks)
                last_part = parts.pop()
                # Combine with remaining block to get 4 blocks total
                four_blocks = last_part + blocks[i:i+1]
                # Split into 2+2
                parts.append(four_blocks[:2])
                parts.append(four_blocks[2:])
            else:
                # This shouldn't happen, but handle it
                parts.append(blocks[i:i+1])
            i += 1

    return parts

def write_part_files(filename_base, parts):
    """Write part files."""
    for part_num, blocks in enumerate(parts, 1):
        part_filename = f"{filename_base}-part{part_num}.org"
        with open(part_filename, 'w') as f:
            for block_type, block_lines in blocks:
                for line in block_lines:
                    f.write(line)
                # Add blank line between blocks within a part
                if (block_type, block_lines) != blocks[-1]:
                    if not block_lines[-1].strip():
                        pass  # Already has blank line
                    else:
                        f.write('\n')
        print(f"Created {part_filename} with {len(blocks)} blocks")

def main():
    if len(sys.argv) != 2:
        print("Usage: split_file.py <filename>")
        sys.exit(1)

    input_file = sys.argv[1]
    filename_base = input_file.replace('.org', '')

    # Read file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Parse into blocks
    blocks = parse_into_blocks(lines)
    print(f"Parsed {len(blocks)} blocks")

    # Split into parts
    parts = split_into_parts(blocks)
    print(f"Split into {len(parts)} parts")

    # Write part files
    write_part_files(filename_base, parts)

    print(f"\nSummary:")
    for i, part in enumerate(parts, 1):
        print(f"  Part {i}: {len(part)} blocks")

if __name__ == '__main__':
    main()
