"""Run a Python script with a copy fallback when hard links are unsupported."""

from __future__ import annotations

import errno
import os
import runpy
import shutil
import sys
import tempfile
from pathlib import Path


ORIGINAL_LINK = os.link
UNSUPPORTED_WINERRORS = {1, 17, 50}
UNSUPPORTED_ERRNOS = {
    errno.EXDEV,
    getattr(errno, "ENOTSUP", errno.EINVAL),
    getattr(errno, "EOPNOTSUPP", errno.EINVAL),
}


def link_or_copy(source, destination, *args, **kwargs):
    try:
        return ORIGINAL_LINK(source, destination, *args, **kwargs)
    except OSError as error:
        if getattr(error, "winerror", None) not in UNSUPPORTED_WINERRORS and error.errno not in UNSUPPORTED_ERRNOS:
            raise
        if args or kwargs:
            raise
        return shutil.copy2(source, destination)


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="portable-link-check-") as temporary:
        root = Path(temporary)
        source, destination = root / "source.txt", root / "destination.txt"
        source.write_text("portable\n", encoding="utf-8", newline="\n")
        link_or_copy(source, destination)
        assert destination.read_bytes() == source.read_bytes()
    print("Portable-link runner self-check passed.")


def main() -> None:
    if sys.argv[1:] == ["--self-check"]:
        self_check()
        return
    if len(sys.argv) < 2:
        raise SystemExit("usage: run-python-with-portable-links.py SCRIPT [ARG ...]")
    script = Path(sys.argv[1]).resolve()
    if not script.is_file():
        raise SystemExit(f"script not found: {script}")
    sys.argv = sys.argv[1:]
    sys.path.insert(0, str(script.parent))
    os.link = link_or_copy
    runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    main()
