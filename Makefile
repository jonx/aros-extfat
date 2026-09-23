# SPDX-License-Identifier: APL-1.1
# Copyright (c) 2026 John Knipper
.PHONY: check check-host check-provenance
check: check-provenance check-host
check-host:
	python3 tools/check-host.py
check-provenance:
	python3 tools/check-provenance.py
