from pathlib import Path


def run_code_quality_audit(root_dir: Path, inventory: dict) -> dict:
    files = inventory["relative_files"]
    findings = []
    score = 100

    python_files = [f for f in files if f.endswith(".py")]
    test_files = [f for f in files if "test" in f.lower() and f.endswith(".py")]

    if len(python_files) == 0:
        findings.append({
            "severity": "MEDIUM",
            "title": "No Python files found",
            "message": "The audit did not find Python source files.",
            "recommendation": "Make sure the uploaded ZIP contains the actual project source code.",
            "source": "project root",
        })
        score -= 20

    if len(test_files) == 0:
        findings.append({
            "severity": "LOW",
            "title": "No tests found",
            "message": "No obvious Python test files were found.",
            "recommendation": "Add at least a small tests/ folder or explain manual testing in the README.",
            "source": "project root",
        })
        score -= 10

    if any(f.lower() == "app.py" for f in files) and len(python_files) == 1:
        findings.append({
            "severity": "MEDIUM",
            "title": "All logic may be in one file",
            "message": "Only one Python file was found. This can make the project harder to maintain.",
            "recommendation": "Split UI, tools, agents, and report generation into separate modules.",
            "source": "app.py",
        })
        score -= 15

    return {
        "score": max(score, 0),
        "findings": findings,
    }
