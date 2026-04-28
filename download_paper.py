#!/usr/bin/env python3
"""Download a paper given a URL or arXiv ID."""
import argparse
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ARXIV_NEW = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")
ARXIV_OLD = re.compile(r"^[a-z\-]+(\.[A-Z]{2})?/\d{7}(v\d+)?$")


def is_arxiv_id(s: str) -> bool:
    return bool(ARXIV_NEW.match(s) or ARXIV_OLD.match(s))


def resolve_url(source: str) -> tuple[str, str]:
    """Return (pdf_url, default_filename)."""
    if is_arxiv_id(source):
        return f"https://arxiv.org/pdf/{source}.pdf", f"{source.replace('/', '_')}.pdf"

    parsed = urllib.parse.urlparse(source)
    if not parsed.scheme:
        raise ValueError(f"Not a valid URL or arXiv ID: {source}")

    if "arxiv.org" in parsed.netloc:
        # Normalize abs/html/pdf links to the PDF.
        m = re.search(r"/(?:abs|pdf|html)/([^?#]+?)(?:\.pdf)?/?$", parsed.path)
        if m:
            paper_id = m.group(1)
            return (
                f"https://arxiv.org/pdf/{paper_id}.pdf",
                f"{paper_id.replace('/', '_')}.pdf",
            )

    filename = Path(parsed.path).name or "paper.pdf"
    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"
    return source, filename


def download(url: str, dest: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "paper-downloader/1.0"})
    with urllib.request.urlopen(req) as resp, dest.open("wb") as f:
        while chunk := resp.read(1 << 16):
            f.write(chunk)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="URL or arXiv ID (e.g. 2301.12345)")
    parser.add_argument(
        "-o", "--output", type=Path, help="Output file or directory (default: CWD)"
    )
    args = parser.parse_args()

    url, default_name = resolve_url(args.source)

    if args.output is None:
        dest = Path.cwd() / default_name
    elif args.output.is_dir() or str(args.output).endswith("/"):
        args.output.mkdir(parents=True, exist_ok=True)
        dest = args.output / default_name
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        dest = args.output

    print(f"Downloading {url} -> {dest}")
    download(url, dest)
    print(f"Saved {dest} ({dest.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
