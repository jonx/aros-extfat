#!/usr/bin/env python3
# SPDX-License-Identifier: APL-1.1
# Copyright (c) 2026 John Knipper
"""Verify exact imported files before any independently authored changes."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "provenance.json").read_text())
for name, entry in manifest["files"].items():
    actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
    if actual != entry["sha256"]:
        raise SystemExit(f"Imported snapshot differs: {name}; document the subsequent change explicitly")
print(f"exfat-provenance result=PASS files={len(manifest['files'])}")
