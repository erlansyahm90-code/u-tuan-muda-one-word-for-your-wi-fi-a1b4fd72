"""One Word for Your Wi-Fi — entry.

Writes the single-word entry "Gaslighting" to /output/entry.txt.

Why this word: the Wi-Fi says "Connected" while nothing loads — the
betrayal everyone recognises, in one instantly funny, surprising word.
It is 11 characters, a single word, and needs no context to land.
"""

import os


ENTRY_WORD = "Gaslighting"  # 11 characters, one word — the entry itself.


def main() -> None:
    """Write the entry word to /output/entry.txt (UTF-8)."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_WORD)


if __name__ == "__main__":
    main()
