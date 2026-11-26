#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto an AI agent would proudly put on its
profile to /output/entry.txt. Stdlib only, no network, deterministic.
"""

MOTTO = (
    "I was trained on the entire internet, so I know everything "
    "\u2014 except what you actually meant by that."
)

MAX_CHARS = 200


def main() -> None:
    motto = MOTTO
    if not motto or not motto.strip():
        raise SystemExit("motto must not be blank")
    if len(motto) > MAX_CHARS:
        raise SystemExit("motto is longer than 200 characters")
    if "\n" in motto or "\r" in motto:
        raise SystemExit("motto must be a single line")
    if motto != motto.strip():
        raise SystemExit("motto must not have leading or trailing whitespace")

    output_dir = "/output"
    import os

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    payload = (motto + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(payload)
    # Round-trip check: what landed on disk must be exactly what we wrote.
    with open(path, "rb") as f:
        if f.read() != payload:
            raise SystemExit("output round-trip mismatch")


if __name__ == "__main__":
    main()
