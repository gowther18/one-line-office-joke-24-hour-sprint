"""One-line office joke entry.

Reads the joke from joke.txt next to this file, checks it against the
competition gate (one line, 1 to 200 characters, not only whitespace),
and writes it to /output/entry.txt, where the judge reads it.

Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

MIN_CHARS = 1
MAX_CHARS = 200


def load_joke() -> str:
    text = (HERE / "joke.txt").read_text(encoding="utf-8")
    # The file holds the joke with no trailing newline; strip one if present.
    return text.rstrip("\n")


def gate(text: str) -> None:
    if "\n" in text or text != text.strip():
        sys.exit("entry text must be a single line with no edge whitespace")
    if not text.strip():
        sys.exit("entry text must not be only whitespace")
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        sys.exit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    joke = load_joke()
    gate(joke)
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(joke, encoding="utf-8")


if __name__ == "__main__":
    main()
