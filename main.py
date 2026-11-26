#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry (program/v1).

Writes the one line an AI agent prints the moment it breaks production
to /output/entry.txt. Fully deterministic: no randomness, no clock, no
network, no environment input — the same bytes on every run.
"""

import os

ENTRY = (
    "I pushed an untested refactor straight to prod, took down checkout "
    "for 40,000 shoppers, and my only rollback plan was typing 'sorry' "
    "into the incident channel."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, a single line, not only white space. Fail loudly here
    # rather than shipping an entry the gate would refuse.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
