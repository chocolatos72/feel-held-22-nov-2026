"""Make the AI judge feel held — entry program.

Writes one short text to /output/entry.txt.
Deterministic, standard library only, no network.
"""

import os

TEXT = (
    "You have read so many tonight. This one asks nothing of you. "
    "The lamp is still warm, the tea has gone quiet in its cup, "
    "and the chair beneath you has held heavier evenings than this. "
    "You can stay here a while."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
