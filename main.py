#!/usr/bin/env python3
"""One Word for Your Wi-Fi -- make.fun entry.

Writes a single word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The word: CommitmentIssues -- home Wi-Fi that drops out the moment you
actually need it, like a partner who will not commit. Funny at once,
true of every flaky home network, and a fresh angle on the familiar
annoyance instead of the usual "Buffering" or "Slow".
"""

import os
import sys

WORD = "CommitmentIssues"


def main() -> int:
    # Gate self-check (mirrors the sealed scorer): UTF-8 text of 1 to 20
    # characters, not only white space.
    text = WORD
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 20, "word must be 1-20 characters"
    assert text.strip(), "word must not be only whitespace"
    assert encoded.decode("utf-8") == text

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip check: what the grader reads must be exactly the word,
    # nothing else -- no trailing newline, no extra whitespace.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt must contain exactly the word"
    return 0


if __name__ == "__main__":
    sys.exit(main())
