from pathlib import Path
from vibeguard.agents.security_agent import run_security_audit
from vibeguard.agents.docs_agent import run_documentation_audit
from vibeguard.agents.deployment_agent import run_deployment_audit
from vibeguard.agents.code_quality_agent import run_code_quality_audit
from vibeguard.agents.kaggle_submission_agent import run_kaggle_submission_audit


def run_audit(root_dir: Path, inventory: dict, options: dict) -> dict:
    """Run selected audits and combine their findings."""
    results = {}
    all_findings = []

    if options.get("security"):
        results["security"] = run_security_audit(root_dir, inventory)
    else:
        results["security"] = {"score": 100, "findings": []}

    if options.get("documentation"):
        results["documentation"] = run_documentation_audit(root_dir, inventory)
    else:
        results["documentation"] = {"score": 100, "findings": []}

    if options.get("deployment"):
        results["deployment"] = run_deployment_audit(root_dir, inventory)
    else:
        results["deployment"] = {"score": 100, "findings": []}

    if options.get("code_quality"):
        results["code_quality"] = run_code_quality_audit(root_dir, inventory)
    else:
        results["code_quality"] = {"score": 100, "findings": []}

    if options.get("kaggle"):
        results["kaggle"] = run_kaggle_submission_audit(root_dir, inventory)
    else:
        results["kaggle"] = {"score": 100, "findings": []}

    for category_result in results.values():
        all_findings.extend(category_result["findings"])

    scores = {
        "security": results["security"]["score"],
        "documentation": results["documentation"]["score"],
        "deployment": results["deployment"]["score"],
        "code_quality": results["code_quality"]["score"],
        "kaggle": results["kaggle"]["score"],
    }
    scores["overall"] = round(sum(scores.values()) / len(scores))

    return {
        "scores": scores,
        "findings": all_findings,
        "category_results": results,
        "inventory": inventory,
    }
