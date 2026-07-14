# The-Nature-of-Code-Examples Python

![License](https://img.shields.io/github/license/yogeshhk/TheNatureOfCode)
![Last Commit](https://img.shields.io/github/last-commit/yogeshhk/TheNatureOfCode)

## Background

Daniel Shiffman's *[The Nature of Code](http://natureofcode.com/)* teaches how to
simulate natural systems — motion, forces, oscillation, particle systems,
autonomous agents, cellular automata, fractals, and more — through code. The
book's original examples are written in [Processing](http://processing.org)
(Java-flavored), and Shiffman later recorded a companion
[YouTube playlist](https://www.youtube.com/watch?v=6vX8wT1G798&list=PLRqwX-V7Uu6aFlwukCmDf0-1-uSR7mklK)
walking through them step by step.

This repository is a **Python port of that playlist**, built on top of
[py5](https://py5coding.org/) — a Python library that wraps Processing itself
(via a JVM bridge), rather than reimplementing its drawing/physics primitives
from scratch. That means the ported sketches stay close to the original
Processing API (`translate()`, `rotate()`, `push_matrix()`, vectors, noise,
etc.) while being written and run as ordinary Python scripts.

If you're looking for the book's raw content (text, illustrations, images,
CSS, etc.) rather than code, see the
[official Nature of Code repo](https://github.com/shiffman/The-Nature-of-Code).
The original Processing examples this port is based on
[live here](https://github.com/shiffman/The-Nature-of-Code-Examples), alongside
a [list of ports to other languages/frameworks](https://github.com/shiffman/The-Nature-of-Code-Examples/blob/master/README.md).

## Goals

- **Learn by porting.** Translating each Processing sketch to Python/py5 forces
  a closer read of the underlying physics and math than copy-pasting would.
- **Follow the book/playlist chapter by chapter**, keeping each example small,
  self-contained, and runnable on its own — mirroring how the original
  playlist presents them.
- **Stay a readable reference** for anyone who wants to see vectors, forces,
  oscillation, and (eventually) particle systems, agents, cellular automata,
  fractals, and neuroevolution expressed in idiomatic Python rather than Java.

This is a work in progress, not a finished port: coverage currently runs
through Chapter 3 (Oscillation/Springs) of the book. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the exact chapter-by-chapter coverage
map and where to pick up next.

## Installation and Running

Each sketch runs directly with Python, but the environment needs Java (for the
py5/Processing bridge) alongside a Python virtual environment. See
[SETUP_AND_RUN.md](SETUP_AND_RUN.md) for step-by-step setup instructions, or
[py5coding.org/content/install.html](https://py5coding.org/content/install.html)
for the upstream py5 installation guide.

## Available Examples
See [FILE_GUIDE.md](FILE_GUIDE.md) for a complete list of examples and what they demonstrate.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get set up and where coverage
of the book/playlist currently stops.

## Note
- Pycharm shows syntax error for variables like 'width', 'height', etc. But they can be used as is. They are defined in 'bulletin' module(?) in Github_p5\p5\sketch\userspace.py

## Disclaimer
Author (yogeshkulkarni@yahoo.com) gives no guarantee of the results of the program. It is just a fun script. Lot of improvements are still to be made. So, don’t depend on it at all.

