#!/usr/bin/env python3
import os
import sys

expected = "RESAMPLE"
path = "resampled_recovered.txt"

if not os.path.exists(path):
    print("RESAMPLE_BROKEN_FAIL")
    print("missing resampled_recovered.txt")
    sys.exit(1)

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read().strip()

print(f"RESAMPLED_RECOVERED_TEXT={text}")

if text != expected:
    print("RESAMPLE_BROKEN_OK")
else:
    print("RESAMPLE_BROKEN_FAIL")
