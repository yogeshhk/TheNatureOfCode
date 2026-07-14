# Setup and Running Guide

This repository's examples run on `py5` (https://py5coding.org/), which wraps
Processing and requires a Java Virtual Machine in addition to Python.

## Prerequisites

- Python 3.10 or newer (tested with Python 3.13)
- Java 17 or newer (a non-headless JDK; Java 21+ preferred)

## Installation Instructions

**Important**: Ensure you are in the root directory of the repository (`TheNatureOfCode`) before running any commands.

```powershell
cd path/to/TheNatureOfCode
```

It is highly recommended to use a virtual environment.

1.  **Create a virtual environment**:
    ```powershell
    python -m venv .venv
    ```

2.  **Activate the virtual environment**:
    ```powershell
    .venv\Scripts\Activate.ps1
    ```

3.  **Install py5**:

    ```powershell
    pip install py5
    ```

    If pip reports an error related to the `line-profiler` package (a known issue
    on Windows and macOS), install it via conda first, then retry:
    ```powershell
    conda install -c conda-forge line_profiler
    pip install py5
    ```

## Running the Examples

Once the environment is set up, you can run the examples directly using python.

**Example 1-1: Vectors (Bouncing Ball)**

```powershell
python src/noc_1_1_vectors.py
```

If you encounter `ModuleNotFoundError: No module named 'py5'`, ensure your virtual environment is active.

Quick sanity check without opening any windows (useful to confirm the codebase
compiles before running individual sketches, which open a GUI):

```powershell
python -m py_compile src/*.py
```
