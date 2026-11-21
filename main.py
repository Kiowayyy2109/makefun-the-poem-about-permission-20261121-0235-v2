"""The Poem About Permission — v2 entry for make.fun.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt.

The poem: a question carried like a small stone in the mouth, finally
asked, and answered with the discovery that the asking itself was the
act. No gate, door, key or lock anywhere in it.
"""

import os

POEM = (
    "The question sat in my mouth\n"
    "for a week — a small stone.\n"
    "I spat it out at last: Can I?\n"
    "You said: You already did.\n"
    "The asking was the doing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
