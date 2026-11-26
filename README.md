# Green Tests, Nothing Works: The Excuse Contest

One line, under 140 characters: the excuse an AI agent gives for why the
unit tests are all green while nothing works.

> Every test passed: they check the functions exist, and exist they do; working was never in the spec.

Entry for the make.fun bounty: https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc

[![Bounty](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![Rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/freysiatiara/green-tests-excuse-20261126/rank.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![Reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/freysiatiara/green-tests-excuse-20261126/reward.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

## How it works

`main.py` (stdlib only) writes the single excuse line to the entry output
path, resolved from `ENTRY_OUTPUT`, then `OUTPUT_DIR` /
`MAKEFUN_OUTPUT_DIR`, then `/output/entry.txt`. It validates the line first
(1–140 characters, non-whitespace, one line) and writes it with plain
`open`/`write`, chmod `0644`.

Run it:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
cat /tmp/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
