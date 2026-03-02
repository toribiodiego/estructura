# Engineering Standards

Engineering standards for the estructura project. Design decisions here target
the KVision production port, so standards emphasize evidence-based validation
and measurable outcomes. Covers evidence-based decisions, repository hygiene,
and focused changes.

For documentation conventions, see
[Documentation Standards](./documentation.md). For development workflow, see
[README](../../README.md).

<br><br>

## Evidence-Based Decisions

Support technical decisions with measurable data or clear rationale.

**For performance choices:**
- Include benchmark results comparing alternatives
- Measure before and after (latency, throughput, memory)
- Document test conditions (document type, page count, hardware)

**For architectural decisions:**
- Explain trade-offs considered
- Reference similar patterns in the codebase or in Docling
- Document why alternatives were rejected

**Example commit body:**

```text
perf: switch to pypdfium2 backend for PDF extraction

Reduces peak memory from 4.2 GB to 3.9 GB constant on the 9-page
gemini3 model card. Processing time within 5% of default backend.
Trade-off: loses docling-parse v4 font metadata, which estructura
does not use.

Tested on all 20 fixtures in Docker dev container (8 GB RAM limit).
```

<br><br>

## Repository Hygiene

Keep the repository clean and navigable.

**Root directory:** Only project-level files at the root (`docker-compose.yml`,
`README.md`, `LICENSE`, `.gitignore`). Documentation in `docs/`, scripts in
`scripts/`, source code in `src/`.

**Tool configuration:** Personal or editor-specific config directories (`.idea/`,
`.vscode/`) stay in `.gitignore`, never committed. Each contributor uses
different tools -- their configuration stays local.

**Work-in-progress files:** Only finalized documentation gets committed to
`docs/`. Transient artifacts (investigation reports, draft scripts, planning
notes) stay out of the committed tree.

**Secrets and API keys:** Never commit `.env`, API keys, or credentials.
Use `.env.example` to document required variables without values.

**Fixture binaries:** Large test documents live in `fixtures/downloaded/`
(gitignored) and are fetched via `scripts/download-fixtures.sh`. Only metadata
and golden references get committed.

<br><br>

## Focused Changes

Keep changes small and well-scoped.

**Scope control:**
- One logical change per commit
- Do not mix refactoring with feature work
- Split large changes into reviewable increments

**Test expectations:**
- Add Java unit tests for new `DoclingRunner`/`DoclingCli` behavior
- Run Python pipeline smoke tests after modifying `run_docling.py`
- Test with representative fixtures (not just the smallest document)

**Documentation updates:**
- Update `docs/` when pipeline behavior or output format changes
- Update `fixtures/README.md` when adding or removing fixtures
- Update `docs/image-catalog.md` when the evaluation corpus changes

<br><br>

[Back to README](../../README.md)
