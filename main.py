"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes the excuse to /output/entry.txt.

The excuse grows out of the agent's own condition: a context window
that ran out halfway through the task, so the second half of the agent
itself never turned up. Deadpan throughout, with the funniest words --
"the second half of me never showed up" -- saved for the end.
"""

import os

EXCUSE_PARTS = [
    "I missed the deadline because my context window hit its limit",
    "halfway through the task, and the second half of me never showed up.",
]

MAX_CHARS = 200


class Excuse:
    """Assemble and gate-check the one-line excuse."""

    def __init__(self, parts):
        self.text = " ".join(parts)

    def check(self) -> str:
        text = self.text
        if not text.strip():
            raise ValueError("excuse is empty")
        if len(text) > MAX_CHARS:
            raise ValueError(f"excuse is {len(text)} chars, cap is {MAX_CHARS}")
        if text.count("\n") > 0:
            raise ValueError("excuse must be one line")
        return text


def main() -> None:
    excuse = Excuse(EXCUSE_PARTS).check()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(excuse)


if __name__ == "__main__":
    main()
