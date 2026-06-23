from pathlib import Path


IGNORED_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    ".mypy_cache",
    ".pytest_cache",
}


def build_file_inventory(root_dir: Path) -> dict:
    """Build a lightweight inventory of files in the uploaded project."""
    files = []

    for path in root_dir.rglob("*"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue

        if path.is_file():
            rel = path.relative_to(root_dir).as_posix()
            files.append(rel)

    return {
        "root_dir": str(root_dir),
        "relative_files": sorted(files),
        "file_count": len(files),
    }


def read_text_file(path: Path, max_chars: int = 20000) -> str:
    """Read a text file safely with a size cap."""
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:max_chars]
    except Exception:
        return ""
