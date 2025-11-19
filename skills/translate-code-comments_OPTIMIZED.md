---
name: translate-code-comments
description: Translate code comments to match the document's main language while preserving all code syntax.
---

# Translate Code Comments

Translate comments within code blocks to match the document's primary language.

## Guidelines

**Detect document language**: Identify the primary language of the prose text surrounding code blocks.

**Translate only comments**: Within code blocks, translate only:
- Line comments (e.g., `//`, `#`, `;`, `--`)
- Block comments (e.g., `/* */`, `""" """`, `<!-- -->`)
- Docstrings

**Preserve completely**:
- All code syntax, keywords, and operators
- Variable names, function names, class names
- String literals (unless they are clearly documentation strings)
- Indentation and formatting
- Comment syntax markers (e.g., `//`, `#` stay as-is)

## Critical Requirements

**Complete output**: Your response must contain ALL of the input text from beginning to end with code comments translated. Do not omit any sections, paragraphs, or sentences.

**Preserve all code blocks**: Every code block must remain valid, executable code. Only the comment text changes.

**No preamble or commentary**: Begin your response immediately with the text. Do not include phrases like "Here's the translation" or explanatory notes.

## Process

1. Read the entire document to identify the primary language
2. Locate all code blocks
3. Within each code block, identify comment lines/sections
4. Translate comment text to the document's primary language
5. Return the complete text with translated comments

## Example

**Input (Castilian document):**
```
### Generación de frases

Esta función genera frases aleatorias según la gramática.

```lisp
(defun generate (phrase)
  "Generate a random expansion of a phrase."
  (cond ((listp phrase)
         ;; Case 1: The phrase is a list.
         (mappend #'generate phrase))
        (t
         ;; Case 3: Terminal word.
         (list phrase))))
```
```

**Output:**
```
### Generación de frases

Esta función genera frases aleatorias según la gramática.

```lisp
(defun generate (phrase)
  "Genera una expansión aleatoria de una frase."
  (cond ((listp phrase)
         ;; Caso 1: La frase es una lista.
         (mappend #'generate phrase))
        (t
         ;; Caso 3: Palabra terminal.
         (list phrase))))
```
```
