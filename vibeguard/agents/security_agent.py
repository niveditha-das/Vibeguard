from pathlib import Path
from vibeguard.tools.secret_scanner import scan_for_secrets


def run_security_audit(root_dir: Path, inventory: dict) -> dict:
    findings = scan_for_secrets(root_dir, inventory["relative_files"])

    score = 100
    for finding in findings:
        if finding["severity"] == "HIGH":
            score -= 25
        elif finding["severity"] == "MEDIUM":
            score -= 10
        else:
            score -= 5

    return {
        "score": max(score, 0),
        "findings": findings,
    }
