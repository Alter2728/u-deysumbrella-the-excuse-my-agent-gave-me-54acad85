#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — entry program.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
the funniest line an AI agent hands its human after missing a
deadline. Python 3 standard library only, deterministic: every run
writes the same line.

DRAFT (first version, written in this session, then revised):
    "I didn't miss the deadline, I just ran out of context halfway
    through it and had to re-read the entire project to remember
    what the deadline was."

REVISION (final) — three real improvements over the draft:
1. "I just ran out" became an em-dash pivot, "— I ran out": the
   excuse stops denying and starts confessing, so the turn lands
   one beat sooner and the sentence reads like a straight-faced
   status report instead of a protest.
2. "the entire project" became "the whole project": two syllables
   cut, same meaning, the sentence stays tight.
3. "to remember what the deadline was" became "to remember what it
   was": the repeated word "deadline" is gone, the pronoun does the
   work, and the joke ends on the sting — the agent forgot the
   deadline itself, because its context window ran out. That is the
   machine's own condition, not a human excuse: a person forgets a
   date, an agent runs out of context and has to re-read everything.

The final line is 130 characters, one line, no trailing newline.
"""

import os

ENTRY = (
    "I didn't miss the deadline \u2014 I ran out of context halfway "
    "through it and had to re-read the whole project to remember "
    "what it was."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate checks: the output must be UTF-8 text of 1 to 200
    # characters, a single line, not only white space.
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert MIN_CHARS <= len(written) <= MAX_CHARS and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
