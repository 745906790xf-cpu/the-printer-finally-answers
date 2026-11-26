"""The printer answers back.

After years of jams, cryptic codes and thumps, the office printer
finally says something. This program writes that one line to
/output/entry.txt so the judge can read it. The line never changes
between runs: no randomness, no clock, no network, just the same
fixed comeback every time.
"""

from pathlib import Path

DESTINATION = Path("/output/entry.txt")
CHARACTER_LIMIT = 240
COMEBACK = "Paper jam, tray 2. I fed 12,438 sheets this month. I jammed on the one you needed."


def _is_single_line(text):
    """True when text is one clean line the gate will accept."""
    if not text:
        return False
    if text != text.strip():
        return False
    if len(text) > CHARACTER_LIMIT:
        return False
    return all(ord(character) >= 32 for character in text)


def _publish(text):
    """Put the comeback in place, then read it back to be sure."""
    # Refuse to write anything the gate would throw out, so a bad line
    # fails loudly here instead of scoring zero in the sandbox.
    if not _is_single_line(text):
        raise ValueError("comeback breaks the gate: check length and line breaks")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text, encoding="utf-8")
    stored = DESTINATION.read_text(encoding="utf-8")
    if stored != text:
        raise ValueError("read-back mismatch: the file does not hold the comeback")
    print("printer answered in", len(text), "characters:", text)


def main():
    _publish(COMEBACK)


main()
