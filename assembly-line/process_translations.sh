#!/bin/bash
# Process all sicp2-2 parts through translation pipeline
# This script will be used to track which files have been processed

cd /home/user/sicp-org/assembly-line

# Count total parts
total=$(ls sicp2-2-part*.org 2>/dev/null | grep -v "trans-castilian" | wc -l)
echo "Total parts to process: $total"

# Count completed Step 1
step1_done=$(ls sicp2-2-part*-trans-castilian-1.org 2>/dev/null | wc -l)
echo "Step 1 completed: $step1_done/$total"

# Count completed Step 2
step2_done=$(ls sicp2-2-part*-trans-castilian-2.org 2>/dev/null | wc -l)
echo "Step 2 completed: $step2_done/$total"

# List next files to process
echo ""
echo "Next files needing Step 1 processing:"
for i in {1..5}; do
  if [ ! -f "sicp2-2-part${i}-trans-castilian-1.org" ] && [ -f "sicp2-2-part${i}.org" ]; then
    echo "  - sicp2-2-part${i}.org"
  fi
done
