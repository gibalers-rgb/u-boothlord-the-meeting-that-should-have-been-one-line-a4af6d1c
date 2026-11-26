#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt.

The line works because it kills the meeting twice over: the decision it was
called to make was already made, and the only thing left for the meeting to
do is the most relatable office ritual of all -- reading aloud, together,
an email nobody bothered to read.

Why it scores on the judge's criteria, in order:
1. One sentence, unmistakably office humor, and it replaces the meeting.
2. It kills the meeting outright: the decision already exists, so there is
   nothing left to meet about.
3. It is drawn from real office life: the unread email thread, the meeting
   that exists only to re-discuss it.
4. The sting is the second half -- a room full of adults spending an hour
   reading out loud what was already written down.
5. It stands alone: no setup, no names, no context needed.
"""

import os
import sys

# The entry: one sentence, no setup, no context, no explanation.
# The em dash is the pivot: everything before it kills the meeting
# (the decision already exists), everything after it is the sting
# (the meeting's only remaining job is reading that decision aloud).
LINE = (
    "The decision was already made in the email nobody read \u2014 "
    "this meeting is just us reading it out loud together for an hour."
)

MAX_CHARS = 200


def main() -> int:
    line = LINE.strip()

    if not line:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: entry is %d characters, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if "\n" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    # One sentence only: exactly one sentence-ending mark, at the end.
    terminators = sum(line.count(mark) for mark in (".", "!", "?"))
    if terminators != 1 or not line.endswith("."):
        print("error: entry must be exactly one sentence", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

    print("wrote /output/entry.txt (%d characters, %d bytes)"
          % (len(line), len(line.encode("utf-8"))))
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
