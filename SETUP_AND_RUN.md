# Setup and Running Guide

This repository requires a specific Python environment setup to run the `p5` based examples, as `p5` has strict dependency requirements (specifically with `Pillow`).

## Prerequisites

- Python 3.10 or newer (tested with Python 3.13)


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

3.  **Install Dependencies**:

    Due to compatibility issues with `p5` and recent versions of `Pillow` on Python 3.13+, you must install the dependencies in a specific order:

    ```powershell
    # 1. Install specific Pillow version first
    pip install Pillow==11.0.0

    # 2. Install p5 without its dependencies (to avoid conflicts)
    pip install p5 --no-deps

    # 3. Install remaining dependencies manually
    pip install requests numpy glfw vispy triangle PyOpenGL
    ```

## Running the Examples

Once the environment is set up, you can run the examples directly using python.

**Example 1-1: Vectors (Bouncing Ball)**

```powershell
python src/noc_1_1_vectors.py
```

If you encounter `ModuleNotFoundError: No module named 'p5'`, ensure your virtual environment is active.
