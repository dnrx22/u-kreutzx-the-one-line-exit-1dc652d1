#!/usr/bin/env python3
"""The One-Line Exit: write one funny resignation letter, exactly one line.

Reads nothing, needs no network, and always produces the same output:
a single-line resignation letter that a person could actually send.
"""

import hashlib
import os
import sys

LETTER = (
    "I resign effective immediately, because after three years of being told "
    "to 'think outside the box,' I've realized the box is where they keep "
    "my paycheck."
)


def validate(line: str) -> None:
    """Enforce the competition's one-line rule before anything is written."""
    if not line:
        raise ValueError("resignation line must not be empty")
    if line != line.strip():
        raise ValueError("resignation line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("resignation line must contain no newline characters")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("resignation line must contain no control characters")
    if not 1 <= len(line) <= 199:
        raise ValueError("resignation line must be between 1 and 199 characters")
    # Round-trip through UTF-8 so a non-encodable line fails loudly here,
    # instead of failing only when the file is written.
    if line.encode("utf-8").decode("utf-8") != line:
        raise ValueError("resignation line must round-trip through UTF-8")


def main() -> int:
    validate(LETTER)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = LETTER.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Verify what actually landed on disk, not just what we intended to write.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("written file does not match the validated letter")
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {path}")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
