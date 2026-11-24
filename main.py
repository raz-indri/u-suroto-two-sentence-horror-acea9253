#!/usr/bin/env python3
"""Two-Sentence Horror -- make.fun entry (program/v1).

Writes exactly one horror story of exactly two sentences, at most
400 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: no randomness, no I/O besides the single output file.
"""

import os
import re

STORY = (
    "At 3 AM the baby monitor crackled to life, and my daughter's voice whispered, "
    "'Mummy, the man in my room says you stopped tucking me in years ago.' "
    "I ran upstairs barefoot \u2014 but her room has been empty since her funeral, "
    "and the whispering is coming from inside the walls."
)

MAX_CHARS = 400


def sentence_count(text: str) -> int:
    """Count sentence-ending punctuation marks (., !, ?)."""
    return len(re.findall(r"[.!?]", text))


def main() -> None:
    text = STORY.strip()
    assert sentence_count(text) == 2, (
        f"entry must be exactly two sentences, got {sentence_count(text)}"
    )
    assert len(text) <= MAX_CHARS, (
        f"entry must be at most {MAX_CHARS} characters, got {len(text)}"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
