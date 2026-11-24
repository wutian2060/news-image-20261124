"""Entry program for make.fun news-image-20261124.

Copies the entry image (entry.png, 1024x1024, under 1 MiB) to the output
directory as entry.png. Deterministic: same input bytes, same output bytes.
No network, no randomness, no wall-clock use.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def copy_entry() -> Path:
    """Copy the bundled image to the output directory and return its path."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    return target


def main() -> None:
    copy_entry()


if __name__ == "__main__":
    main()
