#!/usr/bin/env python3
"""Make the AI judge happy (ai-happy-01).

Writes one image to /output/entry.png: a golden retriever puppy joyfully
leaping to catch a large iridescent soap bubble in a sunlit flower garden.

The image is original art made for this entry (image.jpg, bundled in this
repository), not a stock photo: the judge's rules mark stock and generic
happy images down, and reward a fresh, specific reason to be happy. The
puppy and the bubble are the clear focus, so the idea still reads at
300 pixels across; the golden-hour light, warm colours and the puppy's
delighted expression all pull toward one happy mood.

The program just copies the bundled image to the output directory, as the
entry's name stays entry.png whatever its format (this one is a JPEG by
content, 1024x683, 161,581 bytes — within the 1 MiB and 1024x1024 limits).
Stdlib only, no network, deterministic.
"""
import os
import shutil
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    here = Path(__file__).resolve().parent
    src = here / "image.jpg"
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.png"
    shutil.copyfile(src, out)
    # Guard: the gate is a PNG or JPEG by magic bytes, at most 1 MiB and
    # at most 1024x1024 px. Fail loudly here rather than submitting a
    # file the judge would reject as unreadable.
    data = out.read_bytes()
    if len(data) > 1024 * 1024:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    if not (data[:3] == b"\xff\xd8\xff" or data[:8] == b"\x89PNG\r\n\x1a\n"):
        raise SystemExit("entry.png is neither a JPEG nor a PNG")


if __name__ == "__main__":
    main()
