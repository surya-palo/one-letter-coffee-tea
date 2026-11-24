"""One Letter: Coffee or Tea.

Writes exactly one letter to /output/entry.txt — "A" for coffee.
No word, no explanation, no punctuation, no trailing newline:
the gate requires UTF-8 text of exactly 1 character.
Python standard library only.
"""

import os

LETTER = "A"  # coffee

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    data = LETTER.encode("utf-8")
    assert len(data) == 1, "entry must be exactly one byte"
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Self-check: what landed on disk must be exactly the one letter.
    with open(OUTPUT_PATH, "rb") as f:
        assert f.read() == data, "written entry does not match the letter"


if __name__ == "__main__":
    main()
