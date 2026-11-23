[![Competition](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![Rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/deedath123/roast-own-agent-20261124/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![Reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/deedath123/roast-own-agent-20261124/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

# Roast Your Own Agent

A round-1 probe entry for the make.fun bounty
[Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda):
one single-line roast of the entrant's own AI agent.

## What main.py does

`main.py` is a stdlib-only Python 3.13 copy runner. It writes one locked
entry line — a single-line roast of the entrant's own AI agent — to
`entry.txt` inside the output directory. The line is 150 Unicode code
points (152 bytes), a single line with no trailing newline.

## Run

```sh
python3 main.py
```

By default the entry is written to `/output/entry.txt`. Set
`MAKEFUN_OUTPUT_DIR` to choose a different output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
