from pathlib import Path
from vibeguard.tools.file_tools import read_text_file


def run_kaggle_submission_audit(root_dir: Path, inventory: dict) -> dict:
    files = inventory["relative_files"]
    lower_files = {f.lower() for f in files}
    findings = []
    score = 100

    readme_candidates = [f for f in files if f.lower() == "readme.md" or f.lower().endswith("/readme.md")]
    readme_text = ""
    if readme_candidates:
        readme_text = read_text_file(root_dir / readme_candidates[0]).lower()

    required_concepts = ["agent", "mcp", "security", "deploy", "architecture"]
    missing_concepts = [c for c in required_concepts if c not in readme_text]

    for concept in missing_concepts:
        findings.append({
            "severity": "MEDIUM",
            "title": f"Capstone concept not clearly explained: {concept}",
            "message": f"The README does not clearly mention `{concept}`.",
            "recommendation": f"Add a section explaining how the project demonstrates `{concept}`.",
            "source": readme_candidates[0] if readme_candidates else "README.md",
        })
        score -= 8

    media_or_docs = any(f.startswith("docs/") or f.startswith("media/") for f in lower_files)
    if not media_or_docs:
        findings.append({
            "severity": "LOW",
            "title": "No docs/media folder found",
            "message": "The project does not include a docs or media folder for screenshots, architecture diagrams, or demo assets.",
            "recommendation": "Add docs/architecture.png and screenshots for the Kaggle media gallery.",
            "source": "project root",
        })
        score -= 5

    return {
        "score": max(score, 0),
        "findings": findings,
    }
