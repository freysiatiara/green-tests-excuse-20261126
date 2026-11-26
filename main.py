"""Green Tests, Nothing Works: The Excuse Contest.

Writes one line — the excuse an AI agent gives for why the unit tests
are all green while nothing works — to the entry output path.

Stdlib only. Resolves the output path from ENTRY_OUTPUT, then
OUTPUT_DIR / MAKEFUN_OUTPUT_DIR (joined with ``entry.txt``), then
``/output/entry.txt``. Writes with plain open/write and chmod 0644.
"""

import os

LINE = (
    "Every test passed: they check the functions exist, "
    "and exist they do; working was never in the spec."
)


def resolve_output_path():
    """Return the entry output path, never the current directory."""
    entry_output = os.environ.get("ENTRY_OUTPUT")
    if entry_output:
        return entry_output
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    # Validation guard: the gate requires UTF-8 text of 1..140 chars,
    # not only whitespace, on a single clean line.
    text = LINE
    assert isinstance(text, str) and text.strip(), "entry must be non-empty"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 140, "entry must be 1..140 characters"
    encoded = text.encode("utf-8")
    assert 1 <= len(encoded) <= 140, "entry must be 1..140 bytes of UTF-8"

    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)

    # Read-back verification: the file on disk must hold exactly
    # the entry bytes we just wrote.
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != encoded:
        raise RuntimeError("entry output failed read-back verification")


if __name__ == "__main__":
    main()
