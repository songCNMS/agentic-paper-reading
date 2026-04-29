---
name: hf-weekly-agentic-report
description: Generate an agentic-LLM paper report from a Hugging Face weekly papers URL. Use when the user provides a Hugging Face papers weekly URL and wants relevant agentic LLM papers identified, saved as a markdown list, downloaded, parsed, summarized with main innovations, and compiled into a PDF.
---

# HF Weekly Agentic Report

## Quick Start

Use the bundled script for the full workflow:

```bash
python3 ~/.codex/skills/hf-weekly-agentic-report/scripts/generate_report.py \
  "https://huggingface.co/papers/week/2026-W18" \
  --output-dir . \
  --prefix 2026-W18-agentic
```

This creates:

- `<prefix>.md`: selected agentic-LLM papers with titles, arXiv IDs, categories, and inclusion notes.
- `<prefix>-summaries.md`: per-paper summaries with **Main innovation**, **中文版本**, and **中文锐评** highlights.
- `<prefix>.pdf`: compiled summary PDF.
- `<prefix>-assets/`: downloaded PDFs, parsed text, and metadata JSON.

## Workflow

1. Extract the week token from the Hugging Face URL when the user does not provide a prefix. Example: `2026-W18`.
2. Run `scripts/generate_report.py` with the URL and an output directory in the current project.
3. If dependencies are missing, install `pypdf` and `reportlab`, then rerun the script:

```bash
python3 -m pip install --user pypdf reportlab
```

4. Inspect the generated markdown and PDF. If the user asks for higher-quality summaries or sharper Chinese commentary, refine `<prefix>-summaries.md` using the parsed paper texts under `<prefix>-assets/texts/`, then rerender the PDF:

```bash
python3 ~/.codex/skills/hf-weekly-agentic-report/scripts/generate_report.py \
  "https://huggingface.co/papers/week/2026-W18" \
  --output-dir . \
  --prefix 2026-W18-agentic \
  --render-only
```

## Selection Policy

By default, select papers that are directly relevant to agentic LLMs, including:

- agent algorithms and agent RL
- multi-agent systems and coordination
- environment building and task synthesis
- benchmarks, datasets, and evaluation for agents
- memory, retrieval, RAG, and long-context systems for agents
- GUI, browser, terminal, and tool-use agents
- embodied, robotics, and VLA agents
- process reward models and step-level feedback
- agent safety, alignment, and strategic-risk evaluation

Use `--all` only when the user wants every paper on the weekly page included.

## Notes

- The script uses Hugging Face only for the weekly paper list and arXiv for metadata/PDFs.
- Summaries are generated from arXiv abstracts plus extracted paper text. They are concise first-pass summaries with bilingual Chinese sections; for publication-quality commentary, manually refine the summary markdown before final rendering.
- Do not commit generated assets unless the user explicitly asks. Downloaded PDFs can be large.
