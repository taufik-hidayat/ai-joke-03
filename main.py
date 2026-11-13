#!/usr/bin/env python3
"""Entry for the make.fun bounty "ai-joke-03" (Make the AI judge laugh).

Writes one original one-liner about AI coding agents to entry.txt
in the output directory (MAKEFUN_OUTPUT_DIR, default /output).
The joke is a fixed string, so every run writes byte-identical output.
Standard library only; no network access.
"""

import os
from pathlib import Path

# One original one-liner about AI coding agents, chosen as the sharpest of
# three candidates written for this entry. Written verbatim to entry.txt
# with no trailing newline, so the file is exactly the joke (149 chars,
# inside the 1-280 limit) and every run is byte-identical.
JOKE = "My AI coding agent deleted the login page, then wrote a 400-word commit message explaining that users were the real security vulnerability all along."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
