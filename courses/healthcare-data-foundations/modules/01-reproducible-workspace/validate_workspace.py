"""Validate an FND-1 Module 01 starter or completed learner workspace."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parent
EXPECTED_DATA_SHA256 = "330da80c517c912fccd9bca3963aded84898dbb51e8b7271aa3bc53b0439c3ab"
EXPECTED_REQUIREMENTS = {
    "jupyterlab==4.6.3",
    "nbclient==0.10.2",
    "pandas==3.0.5",
}
CORE_FILES = (
    ".gitattributes",
    ".gitignore",
    "README.md",
    "VERSION",
    "requirements.txt",
    "analysis/r-smoke-test.R",
    "ai-use.md",
    "data/workspace_smoke_test.csv",
    "environment-note.md",
    "notebooks/01-smoke-test.ipynb",
    "outputs/.gitkeep",
    "reproducibility-check.md",
    "sql/00-smoke-test.sql",
    "src/smoke_test.py",
    "version-policy.md",
)
COMPLETION_FILES = (
    "outputs/python-sql-smoke.json",
    "outputs/r-smoke-test.txt",
)
RECORD_FILES = (
    "environment-note.md",
    "version-policy.md",
    "reproducibility-check.md",
    "ai-use.md",
)


class ValidationError(RuntimeError):
    """A learner workspace does not satisfy the release contract."""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def command(args: list[str], cwd: Path) -> str:
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=False)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise ValidationError(f"Command failed: {' '.join(args)}\n{detail}")
    return result.stdout.strip()


def validate_notebook(path: Path, require_outputs: bool) -> None:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Notebook is not valid JSON: {exc}") from exc
    if notebook.get("nbformat") != 4:
        raise ValidationError("Notebook must use nbformat 4.")
    code_cells = [cell for cell in notebook.get("cells", []) if cell.get("cell_type") == "code"]
    if len(code_cells) != 3:
        raise ValidationError(f"Notebook must contain three code cells; found {len(code_cells)}.")
    source = "\n".join("".join(cell.get("source", [])) for cell in code_cells)
    for required in ("pandas", "run_smoke_test", "WORKSPACE_SMOKE_TEST_PASS"):
        if required not in source:
            raise ValidationError(f"Notebook is missing required code: {required}")
    if require_outputs:
        if any(cell.get("execution_count") is None for cell in code_cells):
            raise ValidationError("Every notebook code cell must have a stored execution count.")
        outputs = json.dumps([cell.get("outputs", []) for cell in code_cells])
        if "WORKSPACE_SMOKE_TEST_PASS" not in outputs:
            raise ValidationError("Executed notebook must store the workspace pass marker.")


def validate_git(root: Path) -> None:
    if command(["git", "rev-parse", "--is-inside-work-tree"], root) != "true":
        raise ValidationError("Submission is not a Git repository.")
    branch = command(["git", "branch", "--show-current"], root)
    if branch != "main":
        raise ValidationError(f"Submission must be on main; found {branch or 'detached HEAD'}.")
    if command(["git", "status", "--porcelain"], root):
        raise ValidationError("Submission has uncommitted or untracked files.")
    commit_count = int(command(["git", "rev-list", "--count", "HEAD"], root))
    if commit_count < 3:
        raise ValidationError(f"Submission must preserve at least three commits; found {commit_count}.")
    merge_count = int(command(["git", "rev-list", "--count", "--merges", "HEAD"], root))
    if merge_count < 1:
        raise ValidationError("Submission must preserve at least one merge commit.")
    tag = "fnd1-setup-v0.1.0"
    if command(["git", "cat-file", "-t", tag], root) != "tag":
        raise ValidationError(f"{tag} must be an annotated Git tag.")
    tagged_commit = command(["git", "rev-list", "-n", "1", tag], root)
    head = command(["git", "rev-parse", "HEAD"], root)
    if tagged_commit != head:
        raise ValidationError(f"HEAD must be the commit identified by {tag}.")


def validate(root: Path, mode: str, require_r: bool = False, rscript: Path | None = None) -> int:
    if not root.is_dir():
        raise ValidationError(f"Workspace directory does not exist: {root}")
    missing = [name for name in CORE_FILES if not (root / name).is_file()]
    if missing:
        raise ValidationError(f"Missing required files: {', '.join(missing)}")

    if (root / "VERSION").read_text(encoding="utf-8").strip() != "0.1.0":
        raise ValidationError("VERSION must be 0.1.0 for the setup component.")
    requirements = {
        line.strip()
        for line in (root / "requirements.txt").read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    if requirements != EXPECTED_REQUIREMENTS:
        raise ValidationError(f"requirements.txt must contain the three exact pins: {sorted(EXPECTED_REQUIREMENTS)}")
    data_path = root / "data" / "workspace_smoke_test.csv"
    if sha256(data_path) != EXPECTED_DATA_SHA256:
        raise ValidationError("Synthetic smoke-test data fingerprint changed.")

    validate_notebook(root / "notebooks" / "01-smoke-test.ipynb", mode == "submission")
    python_output = command([sys.executable, "src/smoke_test.py"], root)
    if "WORKSPACE_SMOKE_TEST_PASS rows=3 total=15" not in python_output:
        raise ValidationError("Python and SQLite smoke test did not return the expected result.")

    if require_r:
        executable = str(rscript) if rscript else shutil.which("Rscript")
        if not executable:
            raise ValidationError("Rscript is required but was not found.")
        r_output = command([executable, "analysis/r-smoke-test.R"], root)
        r_result = (root / "outputs" / "r-smoke-test.txt").read_text(encoding="utf-8").strip()
        if r_result != "WORKSPACE_R_SMOKE_TEST_PASS rows=3 total=15":
            raise ValidationError(f"Supplied R smoke test returned an unexpected result: {r_output}")

    if mode == "submission":
        missing_outputs = [name for name in COMPLETION_FILES if not (root / name).is_file()]
        if missing_outputs:
            raise ValidationError(f"Missing completed outputs: {', '.join(missing_outputs)}")
        for name in RECORD_FILES:
            content = (root / name).read_text(encoding="utf-8")
            if "[REPLACE:" in content:
                raise ValidationError(f"{name} still contains learner placeholders.")
            if re.search(r"(?i)([A-Z]:\\Users\\|/Users/|/home/)", content):
                raise ValidationError(f"{name} contains a personal absolute path.")
        summary = json.loads((root / "outputs" / "python-sql-smoke.json").read_text(encoding="utf-8"))
        if summary.get("status") != "pass" or summary.get("result", {}).get("row_count") != 3:
            raise ValidationError("Python and SQLite output record is incomplete or changed.")
        r_result = (root / "outputs" / "r-smoke-test.txt").read_text(encoding="utf-8").strip()
        if r_result != "WORKSPACE_R_SMOKE_TEST_PASS rows=3 total=15":
            raise ValidationError("R output record is incomplete or changed.")
        validate_git(root)

    checks = 15 if mode == "starter" else 26
    print(f"FND-1 Module 01 {mode} validation passed: {checks} checks.")
    return checks


def git(args: list[str], cwd: Path) -> None:
    command(["git", *args], cwd)


def complete_fixture(root: Path) -> None:
    placeholder = re.compile(r"\[REPLACE:[^\]]+\]")
    for name in RECORD_FILES:
        path = root / name
        path.write_text(placeholder.sub("Verified reference value", path.read_text(encoding="utf-8")), encoding="utf-8")

    command([sys.executable, "src/smoke_test.py"], root)
    (root / "outputs" / "r-smoke-test.txt").write_text(
        "WORKSPACE_R_SMOKE_TEST_PASS rows=3 total=15\n", encoding="utf-8"
    )

    notebook_path = root / "notebooks" / "01-smoke-test.ipynb"
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    count = 1
    for cell in notebook["cells"]:
        if cell.get("cell_type") != "code":
            continue
        cell["execution_count"] = count
        cell["outputs"] = [{"name": "stdout", "output_type": "stream", "text": ["cell pass\n"]}]
        count += 1
    notebook["cells"][-1]["outputs"] = [
        {"name": "stdout", "output_type": "stream", "text": ["WORKSPACE_SMOKE_TEST_PASS rows=3 total=15\n"]}
    ]
    notebook_path.write_text(json.dumps(notebook, indent=1) + "\n", encoding="utf-8")

    git(["init", "-b", "main"], root)
    git(["config", "user.name", "Module 01 self-check"], root)
    git(["config", "user.email", "module01-self-check@example.invalid"], root)
    git(["add", "."], root)
    git(["commit", "-m", "chore: start FND-1 workspace"], root)
    git(["switch", "-c", "module-01-setup"], root)
    note = root / "environment-note.md"
    note.write_text(note.read_text(encoding="utf-8") + "\nBranch practice recorded.\n", encoding="utf-8")
    git(["add", "environment-note.md"], root)
    git(["commit", "-m", "docs: record reproducible environment"], root)
    git(["switch", "main"], root)
    git(["merge", "--no-ff", "module-01-setup", "-m", "merge: complete Module 01 setup"], root)
    git(["tag", "-a", "fnd1-setup-v0.1.0", "-m", "FND-1 Module 01 setup component"], root)


def self_check() -> None:
    from build_workspace import build

    with tempfile.TemporaryDirectory(prefix="fnd1-module01-validate-") as temp_dir:
        complete = Path(temp_dir) / "complete"
        build(complete)
        validate(complete, "starter")
        complete_fixture(complete)
        validate(complete, "submission")

        incomplete = Path(temp_dir) / "incomplete"
        shutil.copytree(complete, incomplete)
        (incomplete / "ai-use.md").unlink()
        try:
            validate(incomplete, "submission")
        except ValidationError:
            pass
        else:
            raise AssertionError("Validator accepted an incomplete submission.")
    print("FND-1 Module 01 validator self-check passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=Path, help="Learner workspace to validate")
    parser.add_argument("--mode", choices=("starter", "submission"), default="starter")
    parser.add_argument("--require-r", action="store_true", help="Run the supplied R smoke test")
    parser.add_argument("--rscript", type=Path, help="Exact Rscript executable")
    parser.add_argument("--self-check", action="store_true", help="Run valid and invalid fixtures")
    args = parser.parse_args()
    try:
        if args.self_check:
            self_check()
            return
        if args.workspace is None:
            parser.error("workspace is required unless --self-check is used")
        validate(args.workspace.resolve(), args.mode, args.require_r, args.rscript)
    except (FileExistsError, FileNotFoundError, ValidationError, ValueError) as exc:
        parser.exit(1, f"Validation failed: {exc}\n")


if __name__ == "__main__":
    main()
