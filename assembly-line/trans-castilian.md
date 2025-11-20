# Trans-Castilian Assembly Line (Universal System)

## DIRECT COMMANDS

### Phase 1: The Split (Universal)
1. **Setup**: Ensure working directories exist:
   ```bash
   mkdir -p temp trash
   ```
2. **Identify** the target file in `org-castilian/`.
3. **Define** the `BASENAME` (the filename without extension, e.g., `sicp1-1`).
4. **Execute Splitter**:
   ```bash
   python3 scripts/smart_split.py "org-castilian/[basename].org"
   ```
5. **Verify**: Check `temp/`. Ensure no file is excessively large (aiming for <150 lines).
6. **Safekeeping**: Move the original file from `org-castilian/` to `trash/`:
   ```bash
   mv "org-castilian/[basename].org" "trash/[basename].org"
   ```

### Phase 2: The Translation Loop
**Process every file in `temp/` matching `[basename]-part*.org` (in sorted order):**

1. **Step 1 (Translation)**:
   - Apply `skills/castilian-translation_OPTIMIZED.md`.
   - Save result to: `temp/[partname]-STEP1.org`
   
2. **Step 2 (Code Comments)**:
   - Read `temp/[partname]-STEP1.org`.
   - Apply `skills/translate-code-comments_OPTIMIZED.md`.
   - Save result to: `temp/[partname]-STEP2.org`

**Constraint**: Do not delete files in `temp/` until Phase 3 is verified.

### Phase 3: Finalization
**Merge (Python Sorted Method)**:
- Use Python to ensure parts are merged in strict numerical order and only match the current file's parts.
- Execute (replace `[basename]` with the actual name):
  ```bash
  python3 -c "import glob, sys; [sys.stdout.write(open(f).read()) for f in sorted(glob.glob('temp/[basename]-part*-STEP2.org'))]" > "org-castilian/[basename]-castilian.org"
  ```
