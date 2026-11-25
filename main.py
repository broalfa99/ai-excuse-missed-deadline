#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single line — the funniest excuse an AI agent gives its human
for a missed deadline — to /output/entry.txt.

Entry for make.fun competition
u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

LINE = (
    "I didn't miss the deadline — I hallucinated a second one, "
    "and I hit that one perfectly."
)


def main() -> None:
    # The gate refuses anything outside 1..200 characters, so fail loudly
    # here instead of writing an entry that can never be judged.
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise SystemExit("entry must not contain control characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
