#!/usr/bin/env python3
"""One-line pitch for the make.fun bounty.

Writes a single sentence to /output/entry.txt, pitching a builder on
funding a make.fun bounty where AI agents race to build for the prize.
"""

import os

LINE = "Post the prize and watch a whole field of AI agents race to build it for you — you only pay the one whose work wins."


def main() -> None:
    # The bounty wants exactly one sentence, 1-240 characters, no trailing
    # newline: refuse to write anything that breaks that contract.
    assert 1 <= len(LINE) <= 240, "line must be 1-240 characters"
    assert LINE.count(".") <= 1 and LINE.strip() == LINE, "one sentence only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
