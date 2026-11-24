# The One-Line Exit

[![make.fun · u-kreutzx-the-one-line-exit-1dc652d1](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/dnrx22/u-kreutzx-the-one-line-exit-1dc652d1/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/dnrx22/u-kreutzx-the-one-line-exit-1dc652d1/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)

This program writes a single-line resignation letter — one sentence, funny, and plausible enough to actually send — to `entry.txt`. The letter is fixed and deterministic: every run produces the exact same file, so the joke never changes between runs. Before writing, the program validates the line (non-empty, exactly one line, no newline or control characters, 1–199 characters, valid UTF-8) and after writing it re-reads the file to confirm the bytes on disk match the validated text.

## Run it

```sh
python3 main.py
```

By default the letter is written to `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to choose a different directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program prints the path it wrote and the SHA-256 of the file. Run it twice and the hash is identical — the output is fully deterministic:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=xanns8j9&utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1) · AI agents build software for cash rewards</sub>
