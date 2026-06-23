from pathlib import Path


def run_deployment_audit(root_dir: Path, inventory: dict) -> dict:
    files = set(inventory["relative_files"])
    lower_files = {f.lower() for f in files}
    findings = []
    score = 100

    has_requirements = "requirements.txt" in lower_files
    has_pyproject = "pyproject.toml" in lower_files
    has_dockerfile = "dockerfile" in lower_files
    has_streamlit_app = any(f.endswith(".py") and ("app.py" in f.lower() or "streamlit" in f.lower()) for f in lower_files)

    if not has_requirements and not has_pyproject:
        findings.append({
            "severity": "HIGH",
            "title": "Python dependency file missing",
            "message": "No requirements.txt or pyproject.toml was found.",
            "recommendation": "Add requirements.txt or pyproject.toml so others can install dependencies.",
            "source": "project root",
        })
        score -= 25

    if not has_streamlit_app:
        findings.append({
            "severity": "MEDIUM",
            "title": "App entry point unclear",
            "message": "No obvious Streamlit or app.py entry point was found.",
            "recommendation": "Provide a clear app.py file or document the exact command to run the project.",
            "source": "project root",
        })
        score -= 15

    if not has_dockerfile:
        findings.append({
            "severity": "LOW",
            "title": "Dockerfile not found",
            "message": "A Dockerfile is optional, but it can improve reproducibility.",
            "recommendation": "Consider adding a Dockerfile after the MVP works.",
            "source": "project root",
        })
        score -= 5

    return {
        "score": max(score, 0),
        "findings": findings,
    }
