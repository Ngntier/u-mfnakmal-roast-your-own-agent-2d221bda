"""One-line roast of my own AI agent.

The entry is a single original line, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The joke targets two real agent habits at once: the reflexive
apology, and the confident re-do of the same error — dressed up
this time in fancier formatting, as if bullet points made it true.
"""

import os


ENTRY = (
    "My agent apologizes for being wrong, then confidently repeats "
    "the mistake — now with bullet points, a table, and a smug "
    "little summary."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry = ENTRY.strip()
    assert "\n" not in entry, "entry must be a single line"
    assert len(entry) <= 200, f"entry too long: {len(entry)} chars"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
