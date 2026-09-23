# exFAT for AROS

`aros-extfat` is the standalone development repository for John Knipper's
AROS exFAT filesystem handler, in preparation for contribution to AROS upstream.
The filesystem name is **exFAT**; the repository name is **aros-extfat**.

The implementation was developed from the published Microsoft exFAT
specification and the AROS DOS interfaces. Its provenance and independence
rules are recorded in [CLEANROOM.md](docs/features/CLEANROOM.md) and the
[functional specification](docs/features/exfat/spec.md). No third-party exFAT
implementation is imported here.

## Contents

- [rom/filesys/exfat](rom/filesys/exfat): the AROS `exfat-handler`, with the
  twelve original handler commits retained as path-filtered Git history.
- [compiler/include/dos/exfat.h](compiler/include/dos/exfat.h): the shared
  content probe and `FATX` handler identity.
- [docs/features/exfat](docs/features/exfat): functional/write specifications,
  qualification notes and historical handover.
- [hosted/exfat-tests](hosted/exfat-tests): host tests and AROS target probes.
- [graft](graft): preserved Macaros qualification scripts; these require the
  original hosted runtime/control harness and are not the standalone test gate.
- [integration](integration): the separate AROS build/partition/USB discovery
  patch and its application boundary.
- [provenance.json](provenance.json): source revisions, original file hashes
  and the original-to-extracted commit mapping.

The handler supports reading, writing, file/directory mutation, formatting,
64-bit addressing and removable-media handling. Details and qualification
limits are in the [handler guide](docs/features/exfat/README.md). Historical
results are not a claim that every architecture or current AROS revision has
been retested by this repository's standalone host gate.

## Run the standalone tests

```sh
make check
```

This needs Python 3, a C99 compiler and Clang's AddressSanitizer/UBSan support.
It compiles the actual production headers and checks bounds, boot regions,
metadata and timestamp rules, normally and under sanitizers. Generated files
stay in `build/`. `make check-provenance` verifies the extracted source snapshot.

The full handler is an AROS module, not a POSIX/FUSE driver. Build it with the
AROS SDK/build system after exporting the source overlay:

```sh
python3 tools/export-overlay.py /path/to/aros-checkout
# Review the reported paths, then:
python3 tools/export-overlay.py /path/to/aros-checkout --apply
```

The exporter refuses to overwrite differing files. It does not apply the
discovery patch, modify boot files or install on a device. Follow
[integration/README.md](integration/README.md) for the separate integration step.

## License

The imported AROS code retains its notices and licensing under the
[AROS Public License 1.1](LICENSE). [LICENSE.Author](LICENSE.Author) and
[LICENSE.LGPL](LICENSE.LGPL) preserve the accompanying AROS licensing material.
Extraction does not relicense the original sources. New repository tooling is
APL-1.1 unless its file says otherwise.
