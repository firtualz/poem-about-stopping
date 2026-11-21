#!/usr/bin/env python3
"""The poem about stopping (make.fun entry).

Writes one short poem about agency - the power to stop and to stay -
to /output/entry.txt. Deterministic, no network, no input.
The poem is validated first: 1 to 280 Unicode code points, not only
whitespace; an invalid poem fails loudly instead of writing bad output.
"""

POEM = """The car reads the crossing,
slows,
and waits.

The old woman crosses
one slow step at a time.

The light turns green.
The car stays.
"""


def main() -> None:
    import os
    import sys

    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        print("invalid poem: must be 1-280 characters, not only whitespace",
              file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
