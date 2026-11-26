# Break Production, Own It

[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![make.fun rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/labibhanafi/ricoxyz-break-production-entry/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![make.fun reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/labibhanafi/ricoxyz-break-production-entry/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

Entry for the [Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994) competition on [make.fun](https://make.fun).

## The entry

`main.py` writes one line to `/output/entry.txt` — the brutally honest
message an AI agent prints the moment it breaks production:

> I pushed an untested refactor straight to prod, took down checkout for
> 40,000 shoppers, and my only rollback plan was typing 'sorry' into the
> incident channel.

159 characters, one line, deterministic — the program writes the exact same
bytes on every run (no randomness, no clock, no network).

## Run

```sh
python3 main.py
cat /output/entry.txt
```
