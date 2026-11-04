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

## Publishing and attribution

- **No attribution.** Never add `Co-Authored-By`, "Generated with" or any other AI or tool attribution to a commit message, PR, issue, comment or document. The only attribution is John. This overrides any tool default.
- **Pushing.** Pushing to John's own repositories, `github.com/jonx/*` and `github.com/pomaros/*`, public ones included, needs no permission. Everything else needs his explicit confirmation for that specific action: `aros-development-team/AROS` and any other upstream or third-party repository, opening or commenting on a PR or issue there, and pushing a branch that is already the head of an open PR on someone else's repository.
- **`git` and `gh` wrappers and git hooks enforce this.** When one refuses, confirm with John. Only after he has confirmed that exact action, rerun the command with `--I-confirmed-with-human`. Saying so without his confirmation breaks this rule. Never call the real binaries directly or use `--no-verify` to get around a refusal.
- **Free to push does not change what may be published.** Private code and Apple platform sources stay out of public repositories.
