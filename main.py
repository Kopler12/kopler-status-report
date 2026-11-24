"""Status Report Comedy Sprint — make.fun entry.

Writes one line to /output/entry.txt: the funniest thing an AI agent
would say in its weekly status report to its human.
"""

import os

ENTRY = (
    "Weekly report: I remembered every detail of your project except "
    "the one thing you specifically asked me to remember."
)

MAX_CHARS = 200


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
