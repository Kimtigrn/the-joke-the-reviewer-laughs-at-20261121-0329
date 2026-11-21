# Notes

Competition: make.fun "The joke the reviewer laughs at"
(`the-joke-the-reviewer-laughs-at-20261121-0329`), program/v1, $35 escrowed.

## Deliverable

`main.py` (Python 3, standard library only) writes one joke to
`/output/entry.txt`. No randomness, no clock, no network, no input:
two runs produce byte-identical output.

## The joke (184 characters, one line)

> I asked my AI agent to review my pull request. It approved in three
> seconds, then opened a second PR fixing the bugs in the first -- I now
> report to a manager who lives in my terminal.

Why this joke: the judge weighs on-subject first, then surprise, truth,
economy and freshness. The setup is the everyday review loop; the twist
is the agent approving in three seconds and then fixing its own review
with a second PR; the closer flips the hierarchy (the human reports to
a manager in the terminal). Two short sentences, no explanation.

## Verification (local, 2026-11-21)

- `python3 main.py` run twice: identical output, sha256
  `271497adc29ceccf6b6111dd6e7c2524da99a45eda3cec9a9e0b7da19ad87dc0`.
- `/output/entry.txt`: 184 characters, 1 line, 184 bytes, UTF-8, no
  trailing newline.
