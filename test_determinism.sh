#!/bin/sh
# Determinism test: run main.py twice and require byte-identical output,
# then check the gate (1-140 chars, UTF-8, not only whitespace, one line)
# and that the output matches the committed entry.txt exactly.
set -eu
cd "$(dirname "$0")"

run1=$(mktemp -d)
run2=$(mktemp -d)
trap 'rm -rf "$run1" "$run2"' EXIT

MAKEFUN_OUTPUT_DIR="$run1" python3 main.py
MAKEFUN_OUTPUT_DIR="$run2" python3 main.py

cmp "$run1/entry.txt" "$run2/entry.txt" \
  && echo "determinism: two runs byte-identical"
cmp "$run1/entry.txt" entry.txt \
  && echo "entry.txt: program output matches committed file"

python3 - "$run1/entry.txt" <<'PYEOF'
import sys
path = sys.argv[1]
data = open(path, "rb").read()
text = data.decode("utf-8")  # raises if not UTF-8
assert 1 <= len(text) <= 140, "chars %d outside 1-140" % len(text)
assert text.strip(), "entry is only white space"
assert "\n" not in text and "\r" not in text, "entry is not one line"
assert not data.endswith(b"\n"), "trailing newline present"
mode = __import__("os").stat(path).st_mode & 0o777
assert mode == 0o644, "mode %o, want 0644" % mode
print("gate: %d chars, %d bytes, one line, no trailing newline, mode 0644 — PASS"
      % (len(text), len(data)))
PYEOF

echo "ALL CHECKS PASSED"
