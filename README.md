# Six Words, One Story — frost-quill-41

[![Six Words, One Story](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![Rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/nuraliana/frost-quill-41/rank.svg?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![Reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/nuraliana/frost-quill-41/reward.svg?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)

## What this is

A single complete story told in exactly six words. It is built around
an everyday kitchen object that keeps carrying on a shared daily ritual
after the two people who made that ritual theirs are no longer there.
The object becomes the memory of the couple: the habit survives, the
people do not, and the reader is left to imagine the long life that
came before and the quiet absence that follows.
For a reader, it works like a small door: six words open a whole shared life, then close on the silence that remains.
The idea lands because the object asks for nothing and explains nothing — it simply keeps doing its job, and that stubborn continuity makes the loss feel real rather than told.

## How it works

`main.py` holds the story as a constant, checks it with a small
validation function (exactly six words, 1 to 60 characters, no leading
or trailing whitespace), then writes it — and nothing else, with no
trailing newline — to `entry.txt` inside the directory named by the
`MAKEFUN_OUTPUT_DIR` environment variable, falling back to `/output`
if that variable is not set. It uses only the Python standard library,
makes no network calls, uses no randomness, and produces byte-identical
output on every run.
