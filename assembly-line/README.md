# Assembly Line (SICP Edition)

Temporary assembly line directory for SICP files being processed through skill pipelines.

## Naming Convention

Files in this directory follow the naming convention:
```
[original-filename]-[assembly-line-id]-[step-number].org
```

For the 3-block split process, parts are named:
```
[original-filename]-part[N].org
[original-filename]-part[N]-trans-castilian-1.org
[original-filename]-part[N]-trans-castilian-2.org
```

Where:
- `original-filename` = name of the source file (without .org extension)
- `part[N]` = part number (part1, part2, part3, etc.)
- `assembly-line-id` = the ID of the assembly line being used (e.g., "trans-castilian")
- `step-number` = the step number that has been completed

**Important**: The filename indicates which step has been **completed**, not which step is currently being worked on.

## Processing Lifecycle

1. **Source files**: Files to be processed live in `sicp-castilian/`
2. **Start processing**: When processing begins, the file is **moved** (deleted from source) to `assembly-line/`
   - **IMPORTANT**: The original file is removed from the source directory
   - Example: `sicp-castilian/Chapter-1.org` is **deleted** and split into `assembly-line/Chapter-1-part1.org`, `assembly-line/Chapter-1-part2.org`, etc.
3. **During processing**: Intermediate files are stored in `assembly-line/` with the naming convention above
4. **After completion**: Final processed file is moved back to `sicp-castilian/` with a completion suffix
   - Example: After merging all parts → `sicp-castilian/Chapter-1-castilian.org`
   - The completion suffix (`-castilian`) indicates the file has been fully processed
   - Files without the completion suffix still need to be processed
5. **Cleanup**: All intermediate files are deleted from `assembly-line/` after successful completion

## What the Agent Needs

When processing a file, the agent only needs access to:
- The specific part being processed
- The current skill being applied (from uploaded files)
- The assembly line configuration instructions in `trans-castilian-sicp.md`

## Skills

Translation skills are located in the `skills/` directory:
- `skills/castilian-translation_OPTIMIZED.md`
- `skills/translate-code-comments_OPTIMIZED.md`
