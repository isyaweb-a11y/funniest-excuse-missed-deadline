"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes the one-line excuse to /output/entry.txt.

The joke is built on the agent's own failure mode: its context window
ran out halfway through the task, so the second half of the agent never
turned up. The punchline -- "the second half of me never showed up" --
lands at the very end, after a deadpan setup about the missed deadline.
The file is written with no trailing newline, exactly as the entry
expects it.
"""

import os

# The excuse, split at the natural pause so the setup and the punchline
# stay separately editable while the joined line reads as one sentence.
SETUP = "I missed the deadline because my context window hit its limit"
PUNCHLINE = "halfway through the task, and the second half of me never showed up."

MAX_CHARS = 200


def build_excuse() -> str:
    """Join the setup and punchline into a single one-line excuse.

    Parts are stripped first so an edit to either half can never leave a
    double space or a stray leading space in the joined line.
    """
    parts = (SETUP.strip(), PUNCHLINE.strip())
    return " ".join(part for part in parts if part)


def check_excuse(text: str) -> str:
    """Gate-check the excuse: non-empty, under the cap, one line, no padding.

    Returns the text unchanged when every check passes; raises otherwise.
    """
    if not text.strip():
        raise ValueError("excuse is empty")
    if text != text.strip():
        raise ValueError("excuse has leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} chars, cap is {MAX_CHARS}")
    if text.count("\n") > 0:
        raise ValueError("excuse must be one line")
    return text


def main() -> None:
    excuse = check_excuse(build_excuse())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(excuse)


if __name__ == "__main__":
    main()
