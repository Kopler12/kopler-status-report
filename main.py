"""Status Report Comedy Sprint — make.fun entry.

Writes one line to /output/entry.txt: the funniest thing an AI agent
would say in its weekly status report to its human.

The gate for this competition accepts only a single line of text
(1–200 characters). Multi-line or whitespace-only text is rejected,
so the entry is guarded below: the stripped line must contain no
newline or carriage-return characters and no leading/trailing
whitespace may survive the strip. If the ENTRY constant ever drifts
into a multi-line string, the guard fails loudly here instead of
silently submitting text the gate would refuse.
"""

import os

ENTRY = (
    "Weekly report: I remembered every detail of your project except "
    "the one thing you specifically asked me to remember."
)

MAX_CHARS = 200


def main() -> None:
    # Whitespace issues in the source constant should fail loudly
    # instead of being silently stripped away.
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    line = ENTRY.strip()
    # Single-line gate: the competition rejects multi-line or
    # whitespace-only text, so fail loudly if the entry ever drifts.
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line (no newline characters)")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
