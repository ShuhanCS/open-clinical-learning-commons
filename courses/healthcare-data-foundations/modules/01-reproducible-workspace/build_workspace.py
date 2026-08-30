"""Copy the Module 01 learner workspace to a new target directory."""

from __future__ import annotations

import argparse
import shutil
import tempfile
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
TEMPLATE = MODULE_ROOT / "template"
REQUIRED_TEMPLATE_FILES = (
    ".gitattributes",
    ".gitignore",
    "README.md",
    "VERSION",
    "requirements.txt",
    "analysis/r-smoke-test.R",
    "data/workspace_smoke_test.csv",
    "notebooks/01-smoke-test.ipynb",
    "sql/00-smoke-test.sql",
    "src/smoke_test.py",
)


def build(target: Path) -> Path:
    """Copy the immutable starter template to a target that does not exist."""
    missing = [name for name in REQUIRED_TEMPLATE_FILES if not (TEMPLATE / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Starter template is incomplete: {', '.join(missing)}")
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing target: {target}")
    shutil.copytree(TEMPLATE, target)
    return target


def self_check() -> None:
    with tempfile.TemporaryDirectory(prefix="fnd1-module01-build-") as temp_dir:
        target = Path(temp_dir) / "learner-workspace"
        build(target)
        assert all((target / name).is_file() for name in REQUIRED_TEMPLATE_FILES)
        try:
            build(target)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Builder did not protect an existing target.")
    print("Workspace builder self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", type=Path, help="New learner-workspace path")
    parser.add_argument("--self-check", action="store_true", help="Run the built-in check")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if args.target is None:
        parser.error("target is required unless --self-check is used")
    target = build(args.target.resolve())
    print(f"Learner workspace created: {target}")


if __name__ == "__main__":
    main()
