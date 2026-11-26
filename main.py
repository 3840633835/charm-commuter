#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (140 characters at most) for the
invented city of Laggerton to /output/entry.txt, enforcing the kit's gate:
UTF-8 text of 1 to 140 characters, not only white space.

The entry was drafted fresh in-session from 37 candidates, scored against
the judge brief (see METHODOLOGY.md), and refined once: "light drizzle"
replaced bare "drizzle" to keep the register of a real forecast.

Run: `python3 main.py` writes /output/entry.txt. For local testing set
MAKEFUN_OUTPUT_DIR to another directory; the grader runs it with the
default /output.
"""

import os
import sys

# The entry: one line, 137 characters, 140 bytes, no trailing newline.
ENTRY = (
    "Laggerton: 11\u00b0, light drizzle. The rain arrives at 8:00 sharp, "
    "the bus at 8:07, and you at 8:06 \u2014 in Laggerton, you are the "
    "punctual one."
)

MAX_CHARS = 140


def check_gate(text):
    """Return a list of gate failures (empty means the entry passes)."""
    failures = []
    if not isinstance(text, str):
        failures.append("entry is not text")
        return failures
    if not (1 <= len(text) <= MAX_CHARS):
        failures.append(
            "entry is %d characters, outside the 1-%d gate"
            % (len(text), MAX_CHARS)
        )
    if not text.strip():
        failures.append("entry is only white space")
    if "\n" in text or "\r" in text:
        failures.append("entry is not one line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        failures.append("entry is not UTF-8 text")
    return failures


def main():
    failures = check_gate(ENTRY)
    if failures:
        for failure in failures:
            print("gate failed: %s" % failure, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print("cannot create output dir %s: %s" % (out_dir, exc), file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    # Write exact bytes, no trailing newline, mode 0644 so the grader
    # (which collects outputs as another user) can read it.
    with open(path, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    print("wrote %s (%d chars, %d bytes)" % (path, len(ENTRY), len(ENTRY.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
