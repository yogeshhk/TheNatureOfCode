# Contributing

Thanks for your interest in contributing to this repository. This is a
learner-driven port of Daniel Shiffman's *The Nature of Code*
(https://natureofcode.com/) [YouTube playlist](https://www.youtube.com/watch?v=6vX8wT1G798&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK)
to `py5`. Please follow the two steps below before opening a pull request.

## Step 1: Get the existing codebase running

Before changing or adding anything, confirm your environment can build and run
what's already here:

1. Follow [SETUP_AND_RUN.md](SETUP_AND_RUN.md) to install Python 3.10+, Java 17+,
   and `py5`.
2. Run a quick compile check with no GUI required:
   ```powershell
   python -m py_compile src/*.py
   ```
3. Run a handful of existing sketches directly to confirm they open a window and
   behave as described in [FILE_GUIDE.md](FILE_GUIDE.md), e.g.:
   ```powershell
   python src/noc_1_2_pvectorclass.py
   python src/noc_2_6_gravitationalattraction.py
   python src/noc_3_5_b_springs.py
   ```

If any of this fails, please open an issue with the error before continuing:
that's a real signal the setup docs need fixing.

## Step 2: Find out where coverage stops

The [YouTube playlist](https://www.youtube.com/watch?v=6vX8wT1G798&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK)
follows the book's chapter structure, and each file in `src/` already names the
video it corresponds to in its header comment (`Reference Youtube Video: ...&index=N`).
Cross-referencing every `index=N` marker currently in `src/` against the book's
own table of contents (https://natureofcode.com/) gives this coverage map:

| Book Chapter | Status in this repo | Corresponding files |
|---|---|---|
| Introduction / Chapter 0: Randomness | Implemented | `src/noc_I_*.py` |
| Chapter 1: Vectors | Implemented | `src/noc_1_*.py` |
| Chapter 2: Forces | Implemented | `src/noc_2_*.py` |
| Chapter 3: Oscillation | Implemented through Springs (playlist index 22, the highest index referenced anywhere in `src/`) | `src/noc_3_*.py` |
| Chapter 4: Particle Systems | **Not started** | none |
| Chapter 5: Autonomous Agents | Not started | none |
| Chapter 6: Physics Libraries | Not started | none |
| Chapter 7: Cellular Automata | Not started | none |
| Chapter 8: Fractals | Not started | none |
| Chapter 9: Evolutionary Computing | Not started | none |
| Chapter 10: Neural Networks | Not started | none |
| Chapter 11: Neuroevolution | Not started | none |

**Start here:** Chapter 4, Particle Systems, is the first chapter with no
corresponding example. Open the playlist, find the first Chapter 4 video after
playlist index 22, and port it following the existing naming convention
(`noc_4_<example>_<description>.py`, see [src/README.md](src/README.md)).

Note: the live playlist page renders its video list dynamically, so this table
was built from the book's published table of contents rather than scraping
video titles directly. If you spot a chapter/index mismatch once you're looking
at the actual playlist, please correct this table in your PR.

## Adding a new example

1. Follow the sketch structure and naming convention documented in
   [src/README.md](src/README.md).
2. Add the video's `index=N` to the header comment, the same way existing files
   do, so the coverage map above can be kept up to date.
3. Add a row to [FILE_GUIDE.md](FILE_GUIDE.md) describing the example.
4. Update the coverage table in this file if you complete a chapter.
