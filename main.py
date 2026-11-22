#!/usr/bin/env python3
"""Hand the finished Sunday front page to the grader, unchanged.

Entry for make.fun competition news-image-20261122 (@tapetelo):
a single 1024x1024 image that sums up Sunday 22 November 2026 —
35 stories across 7 regions, led by the COP31 deal text in Antalya,
two tankers struck leaving the Strait of Hormuz, and the Russian
cargo ship Sparta II burning in the Gulf of Finland.

The artwork was composed as a broadsheet page and rendered once;
the resulting PNG sits next to this script as entry.png. Grading
happens in a bare sandbox with nothing installed, so this script
sticks to the standard library and does exactly one thing: place
that PNG at $MAKEFUN_OUTPUT_DIR/entry.png (falling back to /output),
byte for byte, on every run.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

ARTWORK = "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
CHUNK = 1 << 16
EXPECTED_PIXELS = (1024, 1024)
SIZE_GATE_BYTES = 1_048_576  # the competition's 1 MiB intake gate


def artwork_beside_script() -> Path:
    return Path(__file__).resolve().parent / ARTWORK


def destination_folder() -> Path:
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(configured) if configured else Path("/output")


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(CHUNK):
            hasher.update(block)
    return hasher.hexdigest()


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as stream:
        header = stream.read(24)
    if len(header) < 24 or not header.startswith(PNG_SIGNATURE):
        raise ValueError(f"{path} does not start with a PNG signature")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def stream_copy(source: Path, target: Path) -> None:
    with source.open("rb") as incoming, target.open("wb") as outgoing:
        while block := incoming.read(CHUNK):
            outgoing.write(block)


def place_artwork() -> int:
    source = artwork_beside_script()
    if not source.is_file():
        print(f"missing artwork: {source}", file=sys.stderr)
        return 1
    if source.stat().st_size > SIZE_GATE_BYTES:
        print(f"artwork over the 1 MiB gate: {source}", file=sys.stderr)
        return 1
    width, height = png_dimensions(source)
    if (width, height) != EXPECTED_PIXELS:
        print(f"unexpected artwork size: {width}x{height}", file=sys.stderr)
        return 1
    folder = destination_folder()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / ARTWORK
    stream_copy(source, target)
    if target.stat().st_size != source.stat().st_size:
        print(f"short copy: {target}", file=sys.stderr)
        return 1
    if digest(target) != digest(source):
        print(f"copy mismatch: {target}", file=sys.stderr)
        return 1
    print(f"delivered {target} ({width}x{height}, {target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(place_artwork())
