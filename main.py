"""Famous Last Words at 1 Percent — entrypoint.

Writes one line of last words, in the phone's own voice, to entry.txt.
Stdlib only. Output goes to MAKEFUN_OUTPUT_DIR when set, else the
script directory (grader-style fallback).
"""

import os

TEXT = (
    "I held 4,000 of his photos, 37 alarms, and every secret he ever "
    "typed. At 1%, I take them all with me. The cloud gets nothing."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
