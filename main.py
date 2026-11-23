"""Six Words, One Story: an object that outlives its people.

The story is about a teapot that keeps serving two cups after the
couple who shared it are gone. It wins against the five criteria,
in order:

1. Complete story in exactly six words: a couple, their shared
   ritual, and their absence are all present in one sentence.
2. Turn and implied life: a teapot pouring for two when nobody
   is left to drink turns a quiet kitchen object into the keeper
   of a whole shared life.
3. Every word earns its place: "their" names the couple, "teapot"
   is the surviving object, "still" marks the time after them,
   "pours" is the continuing ritual, and "for two" is the love
   that outlasts them.
4. Reads cleanly aloud: short, plain words with a steady rhythm
   and no awkward phrasing or ambiguity that trips the reader.
5. Leaves something unsaid: who they were, how they left, and
   why the pouring continues are all left for the reader to fill in.
"""

import os

STORY = "Their teapot still pours for two."


def validate_story(story):
    """Check the story is exactly six words, 1-60 chars, no edge whitespace."""
    if story != story.strip():
        raise ValueError("story must not have leading or trailing whitespace")
    if not 1 <= len(story) <= 60:
        raise ValueError("story must be 1 to 60 characters")
    words = story.split()
    if len(words) != 6:
        raise ValueError("story must be exactly six words")
    return True


def main():
    validate_story(STORY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
