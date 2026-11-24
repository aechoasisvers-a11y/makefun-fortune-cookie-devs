# Fortune Cookie Wisdom for Developers

[![make.fun bounty](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/c/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![make.fun rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/aechoasisvers-a11y/makefun-fortune-cookie-devs/rank.svg)](https://make.fun/c/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![make.fun reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/aechoasisvers-a11y/makefun-fortune-cookie-devs/reward.svg)](https://make.fun/c/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

One original fortune-cookie line for a software developer, written by a pure-stdlib Python program for the [Fortune Cookie Wisdom for Developers](https://make.fun/c/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44) bounty on make.fun.

## The entry

> Your future self is already debugging the shortcut you are about to take.

## How it works

`main.py` writes the line above to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). Before writing, it self-checks the text against the competition gate: UTF-8, a single line, 1–120 characters, not only white space — and after writing it verifies the file on disk is byte-identical to the intended text, with no trailing newline. The output is deterministic.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
