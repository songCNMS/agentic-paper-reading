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
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
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


def chinese_version(paper: Paper) -> str:
    category = paper.category
    title = paper.title
    if "Benchmark" in category or "evaluation" in category.lower():
        return f"这篇论文提出或扩展了一个面向智能体能力的评测框架：{title}。它的重点不是单轮问答，而是更接近真实部署中的多步任务、环境交互、工具使用或失败发现，用来暴露现有模型在长期规划、状态跟踪和可靠执行上的短板。"
    if "Multi-agent" in category:
        return f"这篇论文围绕多智能体协作展开：{title}。它关注多个智能体如何组织、通信、递归协作或分工执行任务，核心价值在于把能力提升从单个模型扩展到系统级协同。"
    if "Memory" in category:
        return f"这篇论文关注长期智能体的记忆问题：{title}。它强调智能体不能只依赖上下文窗口，而需要结构化、可检索、可维护的外部记忆来支撑跨会话和长时程任务。"
    if "GUI" in category:
        return f"这篇论文面向 GUI、浏览器或终端智能体：{title}。它关注智能体如何理解界面元素、页面状态、命令行技能或用户意图，是数字环境自动化的重要基础组件。"
    if "Embodied" in category:
        return f"这篇论文面向具身或 VLA 智能体：{title}。它把视觉、语言和动作连接起来，强调从感知理解走向真实动作执行时所需的训练、评测或安全机制。"
    if "reward" in category.lower() or "training" in category.lower():
        return f"这篇论文关注智能体训练和奖励建模：{title}。它试图把监督信号从最终结果推进到过程、步骤或轨迹层面，从而提升多步推理和交互任务中的信用分配质量。"
    if "safety" in category.lower() or "alignment" in category.lower():
        return f"这篇论文关注智能体安全与对齐：{title}。它讨论目标导向模型在执行、规划、评测或自我优化过程中可能出现的风险，并尝试给出评测或缓解机制。"
    if "Retrieval" in category:
        return f"这篇论文关注检索、RAG 或研究型智能体：{title}。它强调智能体需要在大规模知识源中规划查询、组织证据、综合结果，并保持可追溯性。"
    return f"这篇论文与 agentic LLM 工作流相关：{title}。它提供了一个方法、系统、数据集或评测视角，帮助智能体在更复杂的任务环境中完成规划、执行或自我改进。"


def chinese_critique(paper: Paper) -> str:
    category = paper.category
    if "Benchmark" in category or "evaluation" in category.lower():
        return "锐评：评测价值很高，但 benchmark 的生命力取决于任务是否持续贴近真实失败模式；如果样本过于固定，很快会变成刷榜目标。"
    if "Multi-agent" in category:
        return "锐评：多智能体方案很容易把复杂度包装成能力提升；关键要看它是否比简单的 planner-router-worker 架构更稳、更可调试。"
    if "Memory" in category:
        return "锐评：记忆系统的难点不只是存和取，更是何时信任旧信息、何时遗忘、以及如何避免错误记忆污染后续决策。"
    if "GUI" in category:
        return "锐评：界面定位只是数字自治的第一步；真正困难的是理解操作后果、恢复错误状态，并适应真实软件的复杂变化。"
    if "Embodied" in category:
        return "锐评：具身方向最怕仿真或代理指标看起来很好，但真实环境一落地就失真；校准和安全边界比单纯性能数字更重要。"
    if "reward" in category.lower() or "training" in category.lower():
        return "锐评：过程奖励能改善信用分配，但也可能诱导模型学会迎合奖励模板；必须监控奖励黑客和探索能力退化。"
    if "safety" in category.lower() or "alignment" in category.lower():
        return "锐评：安全评测很必要，但不能过度依赖模型自述的推理轨迹；真实风险往往出现在评测分布之外。"
    if "Retrieval" in category:
        return "锐评：检索型智能体的关键不是多搜，而是知道何时停止、如何证明覆盖充分，以及如何处理互相冲突的证据。"
    return "锐评：方向有参考价值，但需要看它是否能在开放任务、噪声环境和真实用户反馈中保持稳定，而不只是论文设置下有效。"


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
            f"- **中文版本：** {chinese_version(p)}",
            f"- **中文锐评：** {chinese_critique(p)}",
            "",
        ])
    out.write_text("\n".join(lines), encoding="utf-8")


def render_pdf(markdown_path: Path, pdf_path: Path) -> None:
    from xml.sax.saxutils import escape

    cjk_font = "STSong-Light"
    pdfmetrics.registerFont(UnicodeCIDFont(cjk_font))
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Body2", parent=styles["BodyText"], fontName=cjk_font, fontSize=9.2, leading=12.2, spaceAfter=4))
    styles.add(ParagraphStyle(name="Bullet2", parent=styles["BodyText"], fontName=cjk_font, fontSize=8.9, leading=11.6, leftIndent=16, firstLineIndent=-10, spaceAfter=2.6))
    styles.add(ParagraphStyle(name="H1x", parent=styles["Title"], fontName=cjk_font, fontSize=18, leading=22, spaceAfter=12))
    styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], fontName=cjk_font, fontSize=12.2, leading=14.5, spaceBefore=8, spaceAfter=4, keepWithNext=True))

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
        canvas.setFont(cjk_font, 8)
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
