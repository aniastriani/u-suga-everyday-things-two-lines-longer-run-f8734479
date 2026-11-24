"""Everyday Things, Two Lines — a queue, explained to a 10-year-old.

Writes the two-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt:
line 1 explains a queue through one analogy; line 2 says what the
analogy maps and what it leaves out. Pure standard library only.
"""

import os

LINE_1 = (
    "A queue is a train with no engine: every person is a carriage "
    "hitched to the one ahead, and nobody moves until the carriage "
    "at the very front rolls away."
)

LINE_2 = (
    "The train works because a queue moves only when its front moves, "
    "one person at a time in order, but it leaves out that real people "
    "can step out, swap places, or walk away entirely, and carriages "
    "never can."
)


def main() -> None:
    text = LINE_1 + "\n" + LINE_2 + "\n"
    # The gate wants UTF-8 text of 1 to 400 characters, not only
    # whitespace, in exactly two lines: one sentence explaining the
    # everyday thing, one sentence on what the analogy maps and
    # what it leaves out.
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars"
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 2, f"entry has {len(lines)} lines, want 2"
    assert all(line.strip() for line in lines), "blank line in entry"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
