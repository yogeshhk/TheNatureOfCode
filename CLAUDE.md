# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python implementations of [The Nature of Code](http://natureofcode.com/) by Daniel Shiffman, ported from Processing to **py5** (https://py5coding.org/). All examples live as standalone scripts in `src/`.

## Environment Setup

Requires Python 3.10+, Java 17+ (non-headless JVM), and a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1          # Windows PowerShell

pip install py5
```

If pip reports an error related to the `line-profiler` package on Windows, install
it via conda first (`conda install -c conda-forge line_profiler`), then retry
`pip install py5`.

## Running Examples

Each script is self-contained and run directly:

```bash
python src/noc_1_2_pvectorclass.py
```

All scripts follow the same py5 sketch pattern: `setup()`, `draw()`, and `py5.run_sketch()` at module level.

## Code Architecture

Every example file is a standalone py5 sketch with this structure:

```python
import py5

# Class definitions (Mover, Ball, Liquid, Spring, etc.)

def setup():
    py5.size(400, 300)
    # initialize sketch globals

def draw():
    py5.background(255)
    # update and display objects

if __name__ == "__main__":
    py5.run_sketch()
```

**py5 API notes:**
- Use `py5.Py5Vector` (not `p5.Vector`) for 2D/3D vectors
- Global sketch state (width, height, mouse_x, mouse_y, frame_count) is accessed via `py5.*`
- `push_matrix()`/`pop_matrix()` for transform stacks; `translate()`, `rotate()` for transforms
- PyCharm may flag `width`, `height` etc. as undefined; they are valid py5 globals

**File naming convention:** `noc_<chapter>_<example>_<description>.py`  
- `noc_I_*` = Introduction chapter (randomness, noise)  
- `noc_1_*` = Chapter 1 (Vectors)  
- `noc_2_*` = Chapter 2 (Forces)  
- `noc_3_*` = Chapter 3 (Oscillation)

See `FILE_GUIDE.md` for a full list of examples and what each demonstrates.
