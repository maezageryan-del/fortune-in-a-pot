#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

A kind, funny fortune for the houseplant on the windowsill, told in
one line. The program writes exactly that line to /output/entry.txt:
98 characters, no trailing newline, the same bytes on every run.
"""

import os

ENTRY = "A sunbeam has had a crush on you all winter \u2014 this week, it finally stays past noon, just for you."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
