"""The Funniest Office Joke, Judged Head to Head.

Writes one single-line office joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The joke: a setup (putting office jargon in a will) with a turn
(the will is where you have the last word), punchline last.
It turns on "per my last email" -- the most universally recognised
passive-aggressive phrase in office life -- and escalates it
somewhere nobody expects: your last will and testament.
No network, no randomness, no input: the same bytes every run.
"""

import os
from pathlib import Path

# One line, 82 characters, UTF-8, no trailing newline inside the joke.
ENTRY_LINE = (
    "I put 'per my last email' in my will "
    "so my family knows I meant it the first time."
)


def _output_path() -> Path:
    """Resolve the output file, honouring $MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / "entry.txt"


def main() -> None:
    """Write the joke deterministically and validate the gate."""
    line = ENTRY_LINE
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line.strip() == line and "\n" not in line, "entry must be one line"
    out = _output_path()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    print(f"Wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()
