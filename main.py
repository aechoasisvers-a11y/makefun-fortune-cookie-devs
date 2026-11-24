"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
Pure stdlib Python 3.13, deterministic: the same bytes every run.
"""

import os

ENTRY_TEXT = "Your future self is already debugging the shortcut you are about to take."

MAX_CHARS = 120


def check_entry(text: str) -> None:
    """Self-check: the entry must pass the kit's gate before we write it.

    Gate (RULES.txt): /output/entry.txt is UTF-8 text of 1 to 120
    characters, not only white space.
    """
    assert isinstance(text, str) and text, "entry text must be non-empty"
    assert text.strip(), "entry text must not be only white space"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, gate is 1-{MAX_CHARS}"
    )
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    check_entry(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    # Round-trip check: what landed on disk must be exactly the text
    # we intended, with no trailing newline added.
    with open(path, "rb") as f:
        written = f.read()
    assert written == ENTRY_TEXT.encode("utf-8"), "written bytes differ from entry text"
    assert not written.endswith(b"\n"), "no trailing newline allowed"


if __name__ == "__main__":
    main()
