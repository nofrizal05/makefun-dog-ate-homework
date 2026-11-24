#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one funny one-line excuse to /output/entry.txt.

Standard library only. Deterministic: every run writes the same line.
"""

import os

EXCUSE = (
    "My dog ate my homework, then wrote a better one, submitted it "
    "under my name, and got me an A I cannot explain."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # The excuse must stay exactly one line: no newline may sneak in.
    assert "\n" not in EXCUSE and "\r" not in EXCUSE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE + "\n")
    print(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
