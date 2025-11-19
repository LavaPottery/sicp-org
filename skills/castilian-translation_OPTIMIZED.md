---
name: castilian-translation
description: Translate text to Castilian while preserving proper names and technical terms. Read for context before translating.
---

# Castilian Translation

Translate text to Castilian with context-aware accuracy.

## Guidelines

**Target language**: Castilian. Use appropriate vocabulary, grammar, and formal/informal address (tú and vosotros/usted and ustedes).

**Fidelity**: Read entire text first for context. Translation must be accurate, natural, and preserve original tone and intent.

**Preserve in English**:
- Proper nouns (people, places, organizations, brands)
- Technical terms and jargon (e.g., API, framework, front-end)
- Code, file paths, variable names (e.g., `sudo apt-get`, `/etc/hosts`, `userName`)
- URLs and email addresses

**Format preservation**: Maintain all markdown formatting including headings, lists, bold, italics, code blocks, line breaks, and paragraph spacing.

## Critical Requirements

**Complete output**: Your response must contain ALL of the input text translated from beginning to end. Do not omit any sections, paragraphs, or sentences.

**Direct translation**: Provide only the translated text. Do not provide original and translation side-by-side.

**No preamble or commentary**: Begin your response immediately with the translated text. Do not include phrases like "Here's the translation" or explanatory notes.

## Process

1. Read the entire text to understand context and identify non-translatable elements
2. Translate into natural, fluent Castilian
3. Verify accuracy, grammar, and formatting preservation
4. Return the complete translated text

## Example

**Original:**
```
### Getting Started with Docker

Docker is a containerization platform. To install Docker on Ubuntu, run `sudo apt-get install docker-ce`.

John Smith recommends using Docker Desktop for beginners.
```

**Translated:**
```
### Primeros pasos con Docker

Docker es una plataforma de contenedorización. Para instalar Docker en Ubuntu, ejecuta `sudo apt-get install docker-ce`.

John Smith recomienda usar la aplicación Docker Desktop para principiantes.
```
