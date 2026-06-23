from pathlib import Path
import tempfile
import zipfile


def extract_zip_safely(uploaded_file) -> Path:
    """Extract a user-uploaded ZIP into a temporary directory.

    Prevents Zip Slip path traversal by ensuring every extracted path remains
    inside the destination directory.
    """
    temp_dir = Path(tempfile.mkdtemp(prefix="vibeguard_"))

    with zipfile.ZipFile(uploaded_file, "r") as zip_ref:
        for member in zip_ref.infolist():
            target_path = temp_dir / member.filename
            resolved_target = target_path.resolve()

            if not str(resolved_target).startswith(str(temp_dir.resolve())):
                raise ValueError(f"Unsafe ZIP entry detected: {member.filename}")

        zip_ref.extractall(temp_dir)

    return temp_dir
