"""The Moon finally answers back.

For four billion years the Moon has listened to every wish, every
howl, every midnight promise whispered up at it, and never once
replied. This line is the reply: wry, old, and a little tired of
being wished upon. It is not a wish, not a poem, not a plea. It is
a comeback that lands in one read -- the Moon declining the job
everyone keeps assigning it, with the dry patience of a rock that
has seen it all before.
"""

import os
import sys

LINE = "I'm not your therapist. I'm a rock."

if not (1 <= len(LINE) <= 240) or not LINE.strip():
    sys.exit("error: entry must be 1-240 characters and not only whitespace")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(LINE)
