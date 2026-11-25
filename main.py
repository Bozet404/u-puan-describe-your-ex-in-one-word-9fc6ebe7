#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

The program writes exactly one word to $OUTPUT_DIR/entry.txt: a
one-word verdict on a former partner. No extra text, no punctuation,
nothing else attached.
"""

import os

# The verdict: an ex, summed up in a single word. Like cancelling a
# subscription you should never have signed up for in the first place.
WORD = "Unsubscribe"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
