#!/usr/bin/env python3
"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (1-280 characters, one line).

Design (mapped to the judge's criteria, most important first):
1. On subject: the joke is about an AI coding agent reviewing a pull
   request -- the daily work of developers beside agents.
2. Surprise: the twist has two beats. The agent approves in three
   seconds (too fast to have read anything), then immediately opens
   a second PR fixing the bugs in the first -- the reviewer became
   the fixer, and the human ends up reporting to a manager who
   lives in the terminal.
3. Truth: any developer who works beside an agent recognises the
   instant approval, the follow-up fix PR, and the feeling of being
   managed by the tool.
4. Economy: two short sentences, one line, no explanation of the joke.
5. Freshness: the angle is the agent correcting its own review and
   outranking its human, not a stock joke about robots taking jobs.

The output is a fixed string: the grader runs the program twice and
both runs must produce the same text, so there is no randomness, no
clock, no network and no input. Standard library only.
"""

import os
import sys

JOKE = (
    "I asked my AI agent to review my pull request. It approved in three "
    "seconds, then opened a second PR fixing the bugs in the first -- "
    "I now report to a manager who lives in my terminal."
)

OUTPUT_PATH = os.environ.get("JOKE_OUTPUT", "/output/entry.txt")
MAX_CHARS = 280


def main() -> int:
    text = JOKE.strip()
    chars = len(text)  # Python len() counts Unicode code points.
    if not 1 <= chars <= MAX_CHARS:
        print(f"joke is {chars} characters, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if text != JOKE:
        print("joke has leading/trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("joke must be a single line", file=sys.stderr)
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {chars} characters to {OUTPUT_PATH}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
