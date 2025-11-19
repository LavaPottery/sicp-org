# Trans-Castilian Assembly Line (SICP Edition)

## DIRECT COMMANDS - READ THIS FIRST

### Splitting Command
```
1. Read the org file
2. Parse into blocks: paragraph = 1 block, code block = 1 block, heading = 1 block, list = 1 block
3. Split into files containing exactly 3 blocks each
4. Save as: part1.org (blocks 1-3), part2.org (blocks 4-6), part3.org (blocks 7-9), etc.
5. Handle remainder: if 1 block left, go back and split last 4 blocks into 2+2
6. If 2 blocks left, save as final part with 2 blocks
```

### Processing Command
```
For each part file:
- Apply Step 1 skill → save as [filename]-part#-trans-castilian-1.org
- Apply Step 2 skill → save as [filename]-part#-trans-castilian-2.org
```

### Cleanup Command
```
After saving [filename]-castilian.org to org-castilian/:
1. DELETE ALL intermediate files from assembly-line/ for this filename
2. DELETE the original [filename].org from org-castilian/
This is mandatory.
```

---

## Assembly Line Steps

0. **Pre-Processing**: Split file into 3-block parts
1. **Step 1**: Apply `castilian-translation_OPTIMIZED.md` to each part
2. **Step 2**: Apply `translate-code-comments_OPTIMIZED.md` to each part
3. **Post-Processing**: Merge all parts back together
4. **Cleanup**: Delete all intermediate files

## Process Flow

### Pre-Processing: 3-Block Split

**FIRST: Check `assembly-line/` directory for existing work!**
- If parts already exist for this file (e.g., `[filename]-part#.org`), skip splitting
- Only split if no parts exist

**Splitting Process:**

1. **Move** the org file from `org-castilian/` to `assembly-line/`
2. **Parse into blocks**:
   - Each paragraph = 1 block
   - Each code block = 1 block (don't split mid-code-block)
   - Each heading = 1 block
   - Each list = 1 block
3. **Create part files with 3 blocks each**:
   - `[filename]-part1.org` = blocks 1-3
   - `[filename]-part2.org` = blocks 4-6
   - `[filename]-part3.org` = blocks 7-9
   - Continue...
4. **Handle remainder**:
   - 0 blocks left → perfect, done
   - 1 block left → go back, split last 4 blocks into 2+2 instead
   - 2 blocks left → save as final part with 2 blocks
5. **Delete** the original file from `assembly-line/` after splitting

**IMPORTANT**: Original file is deleted from `org-castilian/` when processing begins and only returns (with `-castilian` suffix) when fully complete.

### Main Processing: Translation Pipeline

**For each part file (part1.org, part2.org, etc.):**

**Step 1: Castilian Translation**
1. Read `[filename]-part#.org`
2. Apply skill: `castilian-translation_OPTIMIZED.md`
3. Save result as: `[filename]-part#-trans-castilian-1.org`
4. Delete `[filename]-part#.org`

**Step 2: Code Comment Translation**
1. Read `[filename]-part#-trans-castilian-1.org`
2. Apply skill: `translate-code-comments_OPTIMIZED.md`
3. Save result as: `[filename]-part#-trans-castilian-2.org`
4. Delete `[filename]-part#-trans-castilian-1.org`

### Post-Processing: Merge and Finalize

1. **Concatenate** all `[filename]-part#-trans-castilian-2.org` files in numerical order (part1, part2, part3...)
2. **Ensure proper spacing** between merged parts (blank line between parts)
3. **Save** final result to: `org-castilian/[filename]-castilian.org`

### Cleanup (MANDATORY)

After successfully saving `[filename]-castilian.org` to `org-castilian/`:

**DELETE from `assembly-line/`:**
- All `[filename]-part#-trans-castilian-2.org` files

**DELETE from `org-castilian/`:**
- The original `[filename].org` file (without `-castilian` suffix)

The `assembly-line/` directory should be empty for this filename after cleanup, and only `[filename]-castilian.org` should remain in `org-castilian/`.

## Example Workflow

**Input:** `org-castilian/chapter1.org` (30 blocks total)

**After Split:**
```
assembly-line/chapter1-part1.org     (blocks 1-3)
assembly-line/chapter1-part2.org     (blocks 4-6)
...
assembly-line/chapter1-part10.org    (blocks 28-30)
```

**After Step 1:**
```
assembly-line/chapter1-part1-trans-castilian-1.org
...
```

**After Step 2:**
```
assembly-line/chapter1-part1-trans-castilian-2.org
...
```

**After Merge:**
```
org-castilian/chapter1-castilian.org
```

**After Cleanup:**
```
assembly-line/  (empty)
org-castilian/chapter1-castilian.org  (only this remains - original chapter1.org is deleted)
```
```

## Trigger Prompt

```
Process the first org file that does NOT have `-castilian` in its filename from org-castilian/ through the trans-castilian assembly line.

Follow the instructions in trans-castilian-sicp.md.
```

## Skills Location

The translation skills are located in the `skills/` directory:
- `skills/castilian-translation_OPTIMIZED.md`
- `skills/translate-code-comments_OPTIMIZED.md`
