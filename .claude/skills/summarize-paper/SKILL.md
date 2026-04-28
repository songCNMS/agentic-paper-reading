---
name: summarize-paper
description: Use this skill whenever the user sends a paper URL (arXiv, PDF link, etc.) or a bare arXiv ID (e.g. "2301.12345", "1706.03762v2", "cs.AI/0601001"). Downloads the paper using download_paper.py, reads the PDF, then produces a concise summary and a clear list of the paper's main contributions.
---

# Summarize Paper

Trigger this skill when the user's message consists of (or centrally references) a paper URL or arXiv ID with an implicit "tell me about this paper" intent. Examples that trigger:

- `https://arxiv.org/abs/1706.03762`
- `2301.12345`
- `https://example.com/papers/foo.pdf — what's this about?`

Do NOT trigger if the user is asking you to *do* something with the URL that isn't reading it (e.g. "download this" → use the script directly without summarizing; "cite this in my doc" → insert a citation).

## Steps

1. **Identify the source.** Extract the URL or arXiv ID from the user's message. If multiple are present, ask which one (or confirm you'll do all of them).

2. **Download the paper.** Run the project's downloader into a temp location:

   ```bash
   python3 download_paper.py "<source>" -o /tmp/
   ```

   The script handles arXiv IDs, abs/html/pdf arXiv URLs, and direct PDF URLs. Capture the output path it prints.

3. **Extract the text.** Use the `Read` tool on the downloaded PDF. If the PDF is large (>10 pages), read the first ~10 pages for abstract/intro/method, then skim later pages for results and conclusions using the `pages` parameter. Do not read every page of a long paper.

4. **Produce the response** with this structure:

   ### <Paper title> — <first author et al., year if known>
   *<venue / arXiv ID / link>*

   **Summary** (3-5 sentences): problem being solved, approach taken, headline result. Plain prose, no jargon the abstract doesn't already use.

   **Main contributions** (bulleted, 2-5 items): what is *new* in this paper — novel method, new dataset/benchmark, new theoretical result, empirical finding, etc. Each bullet is one sentence. Pull these from the authors' own "contributions" list if they have one; otherwise synthesize from the intro and results.

   **Why it matters** (1-2 sentences, optional): only include if the significance isn't obvious from the contributions.

## Guidelines

- Be faithful to the paper. Do not embellish results, invent numbers, or infer claims the authors didn't make. If a figure or number is central, quote it exactly.
- Distinguish claims from evidence: "the authors report X% improvement on Y" is better than "this method is X% better."
- If the PDF download fails (paywall, 404, etc.), report the error and suggest alternatives (e.g. search arXiv, check for an open-access version) rather than fabricating a summary.
- Keep the whole response tight — under ~300 words unless the user asks for depth.
