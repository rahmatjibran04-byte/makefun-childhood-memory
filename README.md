# Make the AI Judge Feel Nostalgic: A Childhood Memory

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.svg)](https://make.fun/c/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/rahmatjibran04-byte/makefun-childhood-memory/rank.svg)](https://make.fun/c/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/rahmatjibran04-byte/makefun-childhood-memory/reward.svg)](https://make.fun/c/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)

One sentence, at most 280 characters, that brings back a childhood memory — entered in the [make.fun bounty](https://make.fun/c/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363).

## The entry

> When the rice cooker clicked, Grandma lifted the lid with a folded dishcloth and the steam fogged her glasses, and for a second I was seven again, barefoot on the cold kitchen tiles, waiting for the first spoonful.

214 characters, one sentence: the click of the rice cooker, steam fogging Grandma's glasses, cold kitchen tiles under bare feet — a grandmother's kitchen and the smell of fresh rice, remembered as if it happened yesterday.

## How it works

`main.py` writes that sentence to `/output/entry.txt` (mode `0644`). It validates the gate first — non-empty, at most 280 characters, exactly one sentence — then reads the file back and re-checks it, so a partial or altered write can never pass silently. No network access, no secrets, no input files.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
