"""Roast Your Own Agent — round-1 probe entry.

Writes one single-line roast of the entrant's own AI agent to
``entry.txt`` inside the output directory.

End-to-end check: verified by running — output entry.txt is UTF-8,
150 code points, 152 bytes, a single line with no newline, not
whitespace-only, and byte-identical to the locked entry line.
"""

import os
import sys

ENTRY = (
    "I asked my agent to roast itself. It read all 407 roasts, spent "
    "12,100 tokens reasoning, and concluded: 'I'm not unfunny \u2014 I'm "
    "just priced per token.'"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
