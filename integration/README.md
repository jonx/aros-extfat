# AROS integration

The source overlay consists of `rom/filesys/exfat/` and
`compiler/include/dos/exfat.h`. The handler's mmake target is `kernel-fs-exfat`;
it needs a configured AROS SDK, generated headers, DOS64 interfaces and the
normal link libraries. This repository does not vendor an operating system.

`aros-discovery.patch` contains the separate build inclusion and MBR/GPT/USB
discovery changes from the original AROS checkout. Its exact base and source
revision are recorded in `../provenance.json`. It covers eleven files and is
provided for review/rebasing, not blind application to arbitrary upstream heads.
It does not include unrelated hosted USB bridge changes or Apple-platform work.

In a disposable AROS checkout at the recorded base, first export the overlay,
then inspect and check the integration patch:

```sh
git apply --check /path/to/aros-extfat/integration/aros-discovery.patch
git apply /path/to/aros-extfat/integration/aros-discovery.patch
```

The historic `graft/exfat-*` scripts additionally require Macaros's hosted
control harness (`graft/aros-ctl` and its runtime). They preserve qualification
recipes and are not executed by `make check`. Physical-device helpers must be
reviewed and explicitly selected; no standalone gate writes a physical disk.

Preparing a public source repository is separate from submitting changes to
AROS upstream. An upstream submission needs a current rebase, target builds,
the hosted read/write/remount gates and review of the discovery changes.
