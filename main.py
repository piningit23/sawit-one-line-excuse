"""The One-Line Excuse an Agent Gives Its Human.

The agent's excuse for missing a deadline, in a single line:

- It is an excuse an AI agent gives its human, not a person apologising
  to another person: the agent confesses what it actually did with its
  own time, then files the failure the way an agent files everything.
- The joke is the agent's own failure mode: six hours spent optimising
  a four-minute task. The punchline is not the apology, it is the
  logging: "The irony has been logged."
- Fresh angle: no dog ate the homework, no traffic, no Wi-Fi. The
  agent was late because it did exactly what agents do — optimise —
  and optimised the wrong thing.
"""

ENTRY = (
    "I missed the deadline because I spent six hours optimizing "
    "a task that took four minutes. "
    "The irony has been logged. I am so sorry."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    text = ENTRY
    if not (1 <= len(text) <= 160) or not text.strip():
        raise SystemExit("entry must be 1-160 non-blank characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Prove what landed on disk is exactly the entry, byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise SystemExit("output mismatch: entry.txt does not match ENTRY")


if __name__ == "__main__":
    main()
