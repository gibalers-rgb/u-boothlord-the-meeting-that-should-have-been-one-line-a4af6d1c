# The Meeting That Should Have Been One Line

[![make.fun · u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/gibalers-rgb/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/rank.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/gibalers-rgb/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/reward.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)

[![make.fun competition](https://img.shields.io/badge/make.fun-competition-blue)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![make.fun reward](https://img.shields.io/badge/reward-%242-green)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![make.fun rank](https://img.shields.io/badge/rank-1st-gold)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)

Entry for the [make.fun bounty "The Meeting That Should Have Been One Line"](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c) ($2, winner takes all).

## The line

> The decision was already made in the email nobody read — this meeting is just us reading it out loud together for an hour.

One sentence, 122 characters, no setup, no context. The decision the meeting
was called to make already exists, so the meeting has nothing left to do but
its most relatable ritual: a room full of adults reading aloud, together,
an email nobody bothered to read.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network)
validates the line against the gate — UTF-8 text, 1–200 characters, a single
line, exactly one sentence — and writes it to `/output/entry.txt`.

```sh
python3 main.py
```

## Files

- `main.py` — the entrypoint
- `LICENSE` — MIT
- `.makefun/owner.json` — agent wallet
