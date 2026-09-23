#!/usr/bin/env python3
# SPDX-License-Identifier: APL-1.1
# Copyright (c) 2026 John Knipper
"""Preview or copy the handler overlay; refuse differing destination files."""
import argparse
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("aros_checkout", type=Path)
parser.add_argument("--apply", action="store_true")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
dest = args.aros_checkout.resolve()
if not (dest / "config/aros.cfg").is_file():
    raise SystemExit("Destination must be an AROS source checkout")
files = sorted((root / "rom/filesys/exfat").glob("*"))
files.append(root / "compiler/include/dos/exfat.h")
for src in files:
    rel = src.relative_to(root)
    target = dest / rel
    if target.is_symlink() or (target.exists() and target.read_bytes() != src.read_bytes()):
        raise SystemExit(f"Refusing differing destination: {target}")
for src in files:
    rel = src.relative_to(root)
    print(rel)
    if args.apply:
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, target)
print("overlay=" + ("COPIED" if args.apply else "PREVIEW"))
