"""Time Machine Warning Label — funniest warning label entry.

Writes the single-line warning label to /output/entry.txt (absolute path).
Standard library only. No trailing newline: the label is exactly 104 chars.
"""

import os

ENTRY = "WARNING: Do not meet yourself. If you do, do not lend yourself money. You will not pay yourself back."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
