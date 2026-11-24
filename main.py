"""One Line of Earned Pride - make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for a street-food vendor whose
three years of pre-dawn work finally sell out before noon.
"""

import os

# Craft notes (why this line):
# - Earned, not asserted: three years of pre-dawn work do the earning;
#   the line never says "proud" or congratulates her.
# - Concrete scene, real person: Ibu Sari, her soto cart, the empty pot.
# - Lands in one read: the pride arrives with the last words, the
#   double wipe of a pot she cannot believe is finally empty.
# - Fresh: a street-food vendor at dawn, not a trophy, podium or graduation.

ENTRY = "Three years Ibu Sari pushed her soto cart out before dawn; today the last bowl sold before noon, and she wiped the empty pot twice, just to be sure it was really empty."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit("entry must be 1-240 characters, got %d" % len(text))
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print("wrote %d characters to %s" % (len(text), path))


if __name__ == "__main__":
    main()
