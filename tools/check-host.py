#!/usr/bin/env python3
# SPDX-License-Identifier: APL-1.1
# Copyright (c) 2026 John Knipper
"""Run the preserved host tests against this repository's production headers."""
import os
from pathlib import Path
import shlex
import subprocess

root = Path(__file__).resolve().parents[1]
out = root / "build/host"
out.mkdir(parents=True, exist_ok=True)
compiler = shlex.split(os.environ.get("CC", "clang"))
flags = ["-std=c99", "-O2", "-Wall", "-Wextra", "-Wconversion",
         "-Wsign-conversion", "-Werror", "-I" + str(root / "rom/filesys/exfat"),
         "-I" + str(root / "compiler/include")]
for name in ("t13a_bounds", "t_boot", "t_meta", "t_time"):
    for sanitized in (False, True):
        binary = out / (name + ("-san" if sanitized else ""))
        extra = ["-fsanitize=address,undefined", "-fno-omit-frame-pointer"] if sanitized else []
        subprocess.run(compiler + flags + extra +
                       [str(root / "hosted/exfat-tests" / (name + ".c")),
                        "-o", str(binary)], check=True)
        result = subprocess.run([str(binary)], text=True, capture_output=True,
                                env=dict(os.environ, UBSAN_OPTIONS="halt_on_error=1"))
        (out / (binary.name + ".log")).write_text(result.stdout + result.stderr)
        if result.returncode:
            print(result.stdout + result.stderr)
            result.check_returncode()
        print(f"{binary.name}: PASS")
print("exfat-host result=PASS suites=4 configurations=2 hardware_claim=false")
