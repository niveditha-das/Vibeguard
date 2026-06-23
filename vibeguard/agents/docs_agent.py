from pathlib import Path
from vibeguard.tools.file_tools import read_text_file


REQUIRED_README_SECTIONS = [
    "setup",
    "installation",
    "usage",
    "architecture",
    "security",
    "deployment",
]


def run_documentation_audit(root_dir: Path, inventory: dict) -> dict:
    files = inventory["relative_files"]
    findings = []

    readme_candidates = [f for f in files if f.lower() == "readme.md" or f.lower().endswith("/readme.md")]

    if not readme_candidates:
        findings.append({
            "severity": "HIGH",
            "title": "README missing",
            "message": "No README.md file was found.",
            "recommendation": "Add a README with problem, solution, setup, usage, architecture, and deployment sections.",
            "source": "README.md",
        })
        return {"score": 30, "findings": findings}

    readme_path = root_dir / readme_candidates[0]
    readme = read_text_file(readme_path).lower()

    score = 100

    for section in REQUIRED_README_SECTIONS:
        if section not in readme:
            severity = "MEDIUM" if section in {"setup", "usage", "deployment"} else "LOW"
            findings.append({
                "severity": severity,
                "title": f"README missing {section} section",
                "message": f"The README does not appear to explain `{section}`.",
                "recommendation": f"Add a clear `{section}` section to help judges and users understand the project.",
                "source": readme_candidates[0],
            })
            score -= 10 if severity == "MEDIUM" else 5

    if len(readme) < 1000:
        findings.append({
            "severity": "MEDIUM",
            "title": "README is too short",
            "message": "The README appears brief and may not provide enough setup or architecture detail.",
            "recommendation": "Expand the README with screenshots, setup commands, architecture, and example output.",
            "source": readme_candidates[0],
        })
        score -= 10

    return {
        "score": max(score, 0),
        "findings": findings,
    }
