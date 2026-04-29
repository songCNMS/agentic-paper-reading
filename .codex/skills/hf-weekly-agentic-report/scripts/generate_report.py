#!/usr/bin/env python3
"""Generate an agentic-LLM weekly paper report from a Hugging Face papers URL."""

from __future__ import annotations

import argparse
import html
import json
import re
import textwrap
import time
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

try:
    from pypdf import PdfReader
except Exception as exc:  # pragma: no cover - environment guard
    raise SystemExit("Missing dependency pypdf. Install with: python3 -m pip install --user pypdf") from exc

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
except Exception as exc:  # pragma: no cover - environment guard
    raise SystemExit("Missing dependency reportlab. Install with: python3 -m pip install --user reportlab") from exc


AGENTIC_KEYWORDS = [
    "agent", "agents", "agentic", "multi-agent", "autonomous", "tool", "tools",
    "browser", "gui", "terminal", "web", "search", "retrieval", "rag", "memory",
    "long-horizon", "multi-turn", "environment", "benchmark", "evaluation",
    "world model", "robot", "robotic", "embodied", "vision-language-action", "vla",
    "process reward", "reward model", "rl", "reinforcement", "distillation",
    "safety", "alignment", "strategic", "task synthesis", "simulation",
]


@dataclass
class Paper:
    arxiv_id: str
    title: str
    category: str = "Agentic LLM"
    why_included: str = ""
    versioned_id: str = ""
    authors: list[str] | None = None
    published: str = ""
    updated: str = ""
    abstract: str = ""
    pages: int | None = None
    status: str = "pending"


def fetch_url(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "hf-weekly-agentic-report/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "ignore")


def week_prefix(url: str) -> str:
    match = re.search(r"/week/([^/?#]+)", url)
    return f"{match.group(1)}-agentic" if match else "hf-weekly-agentic"


def parse_hf_week(html_text: str) -> list[Paper]:
    seen: set[str] = set()
    papers: list[Paper] = []
    for match in re.finditer(r'href="(/papers/(\d{4}\.\d{4,5}))"[^>]*>(.*?)</a>', html_text, re.S):
        arxiv_id = match.group(2)
        raw = re.sub(r"<.*?>", "", match.group(3))
        title = html.unescape(" ".join(raw.split()))
        if not title or title.isdigit() or arxiv_id in seen:
            continue
        seen.add(arxiv_id)
        papers.append(Paper(arxiv_id=arxiv_id, title=title))
    return papers


def is_agentic(paper: Paper) -> bool:
    haystack = f"{paper.title} {paper.abstract}".lower()
    return any(keyword in haystack for keyword in AGENTIC_KEYWORDS)


def infer_category(title: str, abstract: str) -> str:
    h = f"{title} {abstract}".lower()
    if "multi-agent" in h:
        return "Multi-agent systems"
    if "benchmark" in h or "evaluation" in h or "eval" in title.lower():
        return "Benchmark / evaluation"
    if "memory" in h:
        return "Memory"
    if "gui" in h or "browser" in h or "terminal" in h:
        return "GUI/browser/terminal agents"
    if "robot" in h or "embodied" in h or "vision-language-action" in h or "vla" in h:
        return "Embodied / VLA agents"
    if "reward" in h or "reinforcement" in h or "rl" in h or "distillation" in h:
        return "Agent training / rewards"
    if "safety" in h or "alignment" in h or "risk" in h:
        return "Agent safety / alignment"
    if "retrieval" in h or "rag" in h or "search" in h:
        return "Retrieval / research agents"
    if "world model" in h or "simulation" in h:
        return "World models / simulation"
    return "Agentic LLM"


def inclusion_note(category: str) -> str:
    notes = {
        "Multi-agent systems": "Relevant to multi-agent coordination, organization, or collaboration.",
        "Benchmark / evaluation": "Relevant as an agent benchmark, dataset, or evaluation method.",
        "Memory": "Relevant to persistent memory for long-horizon agents.",
        "GUI/browser/terminal agents": "Relevant to agents that operate digital interfaces or tools.",
        "Embodied / VLA agents": "Relevant to embodied, robotic, or VLA agent systems.",
        "Agent training / rewards": "Relevant to agent training, RL, process rewards, or distillation.",
        "Agent safety / alignment": "Relevant to agent safety, alignment, or strategic-risk evaluation.",
        "Retrieval / research agents": "Relevant to retrieval, RAG, search, or research-agent workflows.",
        "World models / simulation": "Relevant to agent world models, simulation, or environment dynamics.",
    }
    return notes.get(category, "Relevant to agentic LLM systems.")


def enrich_arxiv(papers: list[Paper]) -> None:
    ids = [p.arxiv_id for p in papers]
    if not ids:
        return
    api = "https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(ids)
    xml = fetch_url(api)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entries = {}
    for entry in ET.fromstring(xml).findall("a:entry", ns):
        versioned = entry.find("a:id", ns).text.rsplit("/", 1)[-1]
        base = versioned.split("v")[0]
        entries[base] = entry
    for paper in papers:
        entry = entries.get(paper.arxiv_id)
        if entry is None:
            continue
        paper.versioned_id = entry.find("a:id", ns).text.rsplit("/", 1)[-1]
        paper.title = " ".join(entry.find("a:title", ns).text.split())
        paper.abstract = " ".join(entry.find("a:summary", ns).text.split())
        paper.published = entry.find("a:published", ns).text[:10]
        paper.updated = entry.find("a:updated", ns).text[:10]
        paper.authors = [a.find("a:name", ns).text for a in entry.findall("a:author", ns)[:8]]
        paper.category = infer_category(paper.title, paper.abstract)
        paper.why_included = inclusion_note(paper.category)


def download_and_parse(papers: list[Paper], assets_dir: Path, sleep_s: float = 0.2) -> None:
    pdf_dir = assets_dir / "pdfs"
    text_dir = assets_dir / "texts"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    text_dir.mkdir(parents=True, exist_ok=True)
    for idx, paper in enumerate(papers, 1):
        pdf_path = pdf_dir / f"{paper.arxiv_id}.pdf"
        text_path = text_dir / f"{paper.arxiv_id}.txt"
        try:
            if not pdf_path.exists() or pdf_path.stat().st_size < 1000:
                url = f"https://arxiv.org/pdf/{paper.arxiv_id}.pdf"
                print(f"[{idx}/{len(papers)}] download {paper.arxiv_id}", flush=True)
                urllib.request.urlretrieve(url, pdf_path)
                time.sleep(sleep_s)
            print(f"[{idx}/{len(papers)}] parse {paper.arxiv_id}", flush=True)
            reader = PdfReader(str(pdf_path))
            paper.pages = len(reader.pages)
            if not text_path.exists() or text_path.stat().st_size < 1000:
                chunks = []
                for page_no, page in enumerate(reader.pages, 1):
                    try:
                        chunks.append(f"\n\n===== PAGE {page_no} =====\n{page.extract_text() or ''}")
                    except Exception as exc:
                        chunks.append(f"\n\n===== PAGE {page_no} =====\n[EXTRACTION_ERROR {type(exc).__name__}: {exc}]")
                text_path.write_text("".join(chunks), encoding="utf-8")
            paper.status = "ok"
        except Exception as exc:
            paper.status = f"error: {type(exc).__name__}: {exc}"


def innovation_from(paper: Paper) -> str:
    title = paper.title
    abstract = paper.abstract
    lower = f"{title} {abstract}".lower()
    if "benchmark" in lower:
        return "Introduces a targeted benchmark/evaluation setting for measuring agent capabilities that existing tests under-cover."
    if "process reward" in lower or "reward model" in lower:
        return "Adds process-level feedback so agent training can credit intermediate reasoning or actions rather than only final outcomes."
    if "multi-agent" in lower:
        return "Proposes a new structure or training approach for coordinating multiple agents beyond fixed pipelines."
    if "memory" in lower:
        return "Improves long-horizon agent memory by structuring what is stored and retrieved for future decisions."
    if "gui" in lower:
        return "Targets GUI understanding or grounding as a core primitive for autonomous computer-use agents."
    if "world model" in lower or "simulation" in lower:
        return "Uses world modeling or simulation to support planning, evaluation, or action-conditioned prediction."
    if "safety" in lower or "risk" in lower or "alignment" in lower:
        return "Defines or mitigates agentic safety risks that emerge from goal-directed behavior."
    return "Contributes a new method, dataset, or system component for more capable agentic LLM workflows."


def concise_summary(paper: Paper) -> str:
    abstract = paper.abstract.strip()
    if not abstract:
        return "No arXiv abstract was available; see the parsed PDF text for details."
    # Keep a compact first-pass summary from the abstract.
    sentences = re.split(r"(?<=[.!?])\s+", abstract)
    return " ".join(sentences[:3])[:850]


def write_list_markdown(papers: list[Paper], out: Path, source_url: str) -> None:
    lines = [
        f"# Agentic LLM Papers from Hugging Face Weekly Papers",
        "",
        f"Source: {source_url}",
        "",
        "| Category | Title | arXiv ID | Why included |",
        "|---|---|---:|---|",
    ]
    for p in papers:
        lines.append(f"| {p.category} | {p.title} | {p.arxiv_id} | {p.why_included} |")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_summary_markdown(papers: list[Paper], out: Path, list_name: str, assets_name: str) -> None:
    lines = [
        "# Agentic LLM Paper Summaries",
        "",
        f"Source list: `{list_name}`",
        "",
        f"Process: arXiv PDFs were downloaded into `{assets_name}/pdfs/` and parsed into text under `{assets_name}/texts/`.",
        "",
    ]
    for idx, p in enumerate(papers, 1):
        lines.extend([
            f"## {idx}. {p.title}",
            "",
            f"- **arXiv:** {p.arxiv_id}",
            f"- **Type:** {p.category}",
            f"- **Main innovation:** {innovation_from(p)}",
            f"- **Summary:** {concise_summary(p)}",
            f"- **Agentic relevance:** {p.why_included}",
            f"- **Takeaway:** Review this paper when working on {p.category.lower()} for agentic LLM systems.",
            "",
        ])
    out.write_text("\n".join(lines), encoding="utf-8")


def render_pdf(markdown_path: Path, pdf_path: Path) -> None:
    from xml.sax.saxutils import escape

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Body2", parent=styles["BodyText"], fontSize=9.2, leading=12.2, spaceAfter=4))
    styles.add(ParagraphStyle(name="Bullet2", parent=styles["BodyText"], fontSize=8.9, leading=11.6, leftIndent=16, firstLineIndent=-10, spaceAfter=2.6))
    styles.add(ParagraphStyle(name="H1x", parent=styles["Title"], fontSize=18, leading=22, spaceAfter=12))
    styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], fontSize=12.2, leading=14.5, spaceBefore=8, spaceAfter=4, keepWithNext=True))

    def inline(s: str) -> str:
        s = escape(s)
        s = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
        return s

    story = []
    for line in markdown_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            story.append(Spacer(1, 3.5))
        elif line.startswith("# "):
            story.append(Paragraph(inline(line[2:].strip()), styles["H1x"]))
        elif line.startswith("## "):
            story.append(Paragraph(inline(line[3:].strip()), styles["H2x"]))
        elif line.startswith("- "):
            story.append(Paragraph("• " + inline(line[2:].strip()), styles["Bullet2"]))
        else:
            story.append(Paragraph(inline(line.strip()), styles["Body2"]))

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#666666"))
        canvas.drawString(0.7 * inch, 0.45 * inch, markdown_path.stem)
        canvas.drawRightString(letter[0] - 0.7 * inch, 0.45 * inch, f"Page {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(str(pdf_path), pagesize=letter, rightMargin=0.65 * inch, leftMargin=0.65 * inch, topMargin=0.7 * inch, bottomMargin=0.7 * inch, title=markdown_path.stem)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Hugging Face weekly papers URL, e.g. https://huggingface.co/papers/week/2026-W18")
    parser.add_argument("--output-dir", type=Path, default=Path.cwd())
    parser.add_argument("--prefix", default=None)
    parser.add_argument("--all", action="store_true", help="Include all papers, not only agentic-relevant papers")
    parser.add_argument("--render-only", action="store_true", help="Only render <prefix>-summaries.md to <prefix>.pdf")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.prefix or week_prefix(args.url)
    list_md = args.output_dir / f"{prefix}.md"
    summary_md = args.output_dir / f"{prefix}-summaries.md"
    pdf_path = args.output_dir / f"{prefix}.pdf"
    assets_dir = args.output_dir / f"{prefix}-assets"

    if args.render_only:
        render_pdf(summary_md, pdf_path)
        print(f"Rendered {pdf_path}")
        return 0

    page = fetch_url(args.url)
    papers = parse_hf_week(page)
    enrich_arxiv(papers)
    if not args.all:
        papers = [p for p in papers if is_agentic(p)]
    write_list_markdown(papers, list_md, args.url)
    download_and_parse(papers, assets_dir)
    (assets_dir / "metadata.json").write_text(json.dumps([asdict(p) for p in papers], indent=2, ensure_ascii=False), encoding="utf-8")
    write_summary_markdown(papers, summary_md, list_md.name, assets_dir.name)
    render_pdf(summary_md, pdf_path)
    print(f"Wrote {list_md}")
    print(f"Wrote {summary_md}")
    print(f"Wrote {pdf_path}")
    print(f"Selected {len(papers)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
