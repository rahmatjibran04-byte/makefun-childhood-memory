"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence (at most 280 characters) recalling a childhood
memory to /output/entry.txt. No network access, no secrets, no input
files: the sentence is embedded below and validated against the gate
before it is written.
"""

import os

ENTRY = (
    "When the rice cooker clicked, Grandma lifted the lid with a folded "
    "dishcloth and the steam fogged her glasses, and for a second I was "
    "seven again, barefoot on the cold kitchen tiles, waiting for the "
    "first spoonful."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > 280:
        raise ValueError(f"entry is {len(text)} characters, over the 280 limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back what was written and re-check the gate on the real bytes,
    # so a partial or altered write can never pass silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("read-back mismatch: /output/entry.txt differs")
    if not (1 <= len(written) <= 280) or written.strip() != written:
        raise ValueError("read-back failed the gate")


if __name__ == "__main__":
    main()
