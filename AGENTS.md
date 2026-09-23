# Working on aros-extfat

This repository owns the exFAT handler and its specification-based tests.
Read README.md, docs/features/CLEANROOM.md and the exFAT specifications before
changing behavior. Use published specifications and AROS interfaces, not other
exFAT implementation source. Preserve imported copyrights and licenses.

Run `make check` before committing. Keep generated images, binaries and SDKs
out of Git. Source paths match the AROS tree so changes can become upstream
patches; integration changes belong separately in integration/.

The original source repositories remain untouched. Do not modify sibling
checkouts or contact AROS upstream as part of ordinary work here. Publication
to this repository does not authorize an upstream PR or submission.
