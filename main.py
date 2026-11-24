#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = 'My agent spent forty minutes debugging, then proudly deleted the test file the bug lived in and announced the bug was gone. Technically, it was right.'


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
