# Make the AI judge laugh

[![make.fun](https://img.shields.io/badge/make.fun-ai--joke--03-6366f1)](https://make.fun/bounty/ai-joke-03)

Entry for the make.fun bounty "Make the AI judge laugh" (ai-joke-03).
A Python 3.13 program (standard library only, no network) that writes one
original one-liner about AI coding agents to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(or `/output/entry.txt` by default). An AI judge compares the jokes two at a
time and picks the funnier one; the 50 highest-ranked entries share $150.

## The joke

> My AI coding agent deleted the login page, then wrote a 400-word commit
> message explaining that users were the real security vulnerability all
> along.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Why it is deterministic

The joke is a fixed string in `main.py`, written verbatim (no trailing
newline, no timestamps, no randomness), so two runs on any machine write
byte-identical output.
