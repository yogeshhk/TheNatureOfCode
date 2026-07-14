# TODO — Upgrade Repo Action Items

Generated from the `/upgrade-repo-tech` review plan approved on 2026-07-14.
Checked off one at a time as each item is completed (see `reports/upgrade_14072026.md`
for the final write-up once everything here is done).

## Critical Issues

- [x] Fix `src/noc_1_5_acceleation.py`: `py5.Py5Vector.random_2D()` does not exist in
      the py5 API (confirmed against py5 reference docs) — replaced with
      `Py5Vector.random(dim=2)`.
- [x] Fix install-instructions mismatch: `CLAUDE.md` and `SETUP_AND_RUN.md` both said
      `pip install p5 --no-deps` (old library), but every script in `src/` does
      `import py5` (new library, which is Java/JVM-backed — not just a rename).
      Rewrote both docs: `pip install py5`, Java 17+ prerequisite, line-profiler
      troubleshooting note per py5's own install docs.
- [x] Fix `requirements.txt`: was an unrelated 273-package pip-freeze dump
      (Jupyter, matplotlib, macOS-only `pyobjc-framework-*` — won't install on
      Windows). Replaced with just `py5`, since pip resolves its
      platform-appropriate transitive deps automatically (confirmed against
      py5's PyPI metadata).

## Redundancy & Cleanup

- [x] `noc_1_5_acceleation.py` / `noc_1_6_acceleationtowardsmouse.py`: comment
      claimed "py5 Py5Vector has no built-in limit(), so cap manually" — this was
      incorrect (`Py5Vector.set_limit(max_mag)` exists). Replaced manual workaround
      with `set_limit()`.
- [x] `noc_2_2_applyingaforce.py` / `noc_2_3_simulatingwithmass.py` used
      `Py5Vector2D` while all other files use `Py5Vector` — normalized to
      `Py5Vector` for consistency.
- [x] Decide fate of `Notes_NatureOfCode.md` — user chose to remove it (it
      duplicated README.md content with no distinct purpose). Deleted.

## Discoverability & First Impressions

- [x] Fix README grammar: "This is the repository has Python implementations of..."
      -> "This repository contains Python implementations of..."
- [x] Add badges to README (license, last commit) — user confirmed
      `yogeshkulkarni/TheNatureOfCode`; added shields.io badges. Also fixed the
      README's outdated "made possible by PyP5" attribution line to credit py5.
- [ ] Screenshots/GIFs of example sketches — flagged as a manual follow-up; this
      environment can't render py5's GUI output headlessly.
- [x] Clean em-dashes in `CLAUDE.md` (2), `FILE_GUIDE.md` (1), `src/README.md` (6).

## Community & Trust Signals

- [x] Created `CONTRIBUTING.md` with the requested contributor procedure: (1) get
      the existing codebase compiling/running, (2) chapter-level coverage table
      cross-referencing the book's table of contents against `index=N` markers
      already in `src/*.py` headers, (3) explicit "start here" pointer.
- [x] Added a "Contributing" section to `README.md` pointing to `CONTRIBUTING.md`.
- [x] Ask user: add `CODE_OF_CONDUCT.md` / issue templates, or skip — user chose
      to skip both.

## Playlist Coverage Mapping (feeds into CONTRIBUTING.md)

- [x] Attempted to fetch the live YouTube playlist directly — it's JS-rendered
      and not scrapable via WebFetch; fell back to the book's official table of
      contents (natureofcode.com), which the playlist follows per this repo's
      own README.
- [x] Cross-referenced against the `index=N` values already embedded in each
      `src/*.py` file's header comment (highest index found: 22, in the Springs
      examples).
- [x] Built a chapter-level coverage table in `CONTRIBUTING.md`.
- [x] Identified the first uncovered chapter (Chapter 4: Particle Systems) as the
      "start here" pointer.

## Suggestions (non-critical)

- [x] Document `python -m py_compile src/*.py` as a quick sanity/smoke check —
      added to `SETUP_AND_RUN.md`; will also be referenced from CONTRIBUTING.md
      step 1.

## Manual / Follow-up (cannot be done by this agent)

- [ ] GitHub repo Settings: Description + Topics — needs the GitHub web UI; a
      step-by-step guide will be written when we reach this item.

## Future: Publish LinkedIn Post (do not act on this without explicit go-ahead)

- [x] Draft written: `docs/linkedin_post_draft.md` — covers recent changes
      (py5 bug fix, install-docs fix, requirements.txt cleanup) and how to
      contribute (CONTRIBUTING.md, Chapter 4 Particle Systems as start point).
- [x] Banner images created: `docs/banner_wide.svg` (1200x630, link-preview
      format) and `docs/banner_square.svg` (1200x1200, image-post format).
      Both are hand-built SVG motifs (vectors, oscillation, particles) since
      this environment can't render py5's actual GUI output to screenshot.
- [ ] Review/edit the draft text and banners whenever you're ready.
- [ ] Export the chosen SVG to PNG (LinkedIn doesn't accept SVG uploads) before
      attaching it.
- [ ] Publish to LinkedIn at the appropriate time — this is a manual step for
      you; not something to be done automatically.
