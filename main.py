#!/usr/bin/env python3
"""Deliver the finished 22 November 2026 front page to the grader.

The picture beside this file is the complete one-page summary of
Sunday 22 November 2026 for competition news-image-20261122:
three hero stories, ten medium stories and twenty-two briefs across
seven regions, with a numbers bar, a numbered map and a date check
that names the earlier days' stories left out. It was drawn as an
HTML broadsheet and rendered with a headless browser at exactly
1024 by 1024 pixels; the render is bundled here as entry.png
(364,234 bytes, under the 1 MiB gate).

The sandbox installs nothing, so this program uses only the
standard library. Its single job is to place the bundled picture
where the grader looks for it, byte for byte, on both runs.
"""

import hashlib
import os
import shutil
import sys

PICTURE_NAME = "entry.png"


def bundled_picture_path():
    """Return the path of the bundled picture next to this file."""
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, PICTURE_NAME)


def grader_output_folder():
    """Return the grader output folder, honouring the local override."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def sha256_of(path):
    """Return the SHA-256 of a file, read in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def deliver_picture():
    """Copy the bundled picture into the output folder, verified."""
    source = bundled_picture_path()
    if not os.path.isfile(source):
        print(f"{PICTURE_NAME} is missing beside {__file__}", file=sys.stderr)
        return 1
    folder = grader_output_folder()
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, PICTURE_NAME)
    shutil.copyfile(source, target)
    # The grader runs this program twice and both runs must write
    # identical bytes, so confirm the delivered file is exactly the
    # bundled picture — same size and same SHA-256 — before success.
    if os.path.getsize(target) != os.path.getsize(source):
        print(f"{target} is not a complete copy of {source}", file=sys.stderr)
        return 1
    if sha256_of(target) != sha256_of(source):
        print(f"{target} does not match {source}", file=sys.stderr)
        return 1
    print(f"wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(deliver_picture())
