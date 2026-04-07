# src — Nature of Code Examples

Each `.py` file here is a **standalone py5 sketch**. Run any one directly:

```bash
python src/<filename>.py
```

## Naming Convention

```
noc_<chapter>_<example>_<description>.py
```

- `noc_I_*`  — Introduction chapter (randomness, noise)
- `noc_1_*`  — Chapter 1: Vectors
- `noc_2_*`  — Chapter 2: Forces
- `noc_3_*`  — Chapter 3: Oscillation

Letter suffixes (`_a`, `_b`) indicate variant implementations of the same concept —
typically procedural (`_a`) followed by object-oriented (`_b`).

## Sketch Structure

Every file follows this pattern:

```python
import py5

# Class definitions

def setup():
    py5.size(640, 360)
    # initialise sketch-level state

def draw():
    py5.background(255)
    # update + display each frame

if __name__ == "__main__":
    py5.run_sketch()
```

## Placeholder Files

`noc_I_0_introduction.py` and `noc_2_1_whatisaforce.py` are intentionally empty —
the corresponding video segments introduce concepts verbally with no runnable code.

## Adding a New Example

1. Copy the sketch structure above into a new file following the naming convention.
2. Add a row to `FILE_GUIDE.md` in the repo root.
