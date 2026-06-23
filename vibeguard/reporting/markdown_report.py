def build_markdown_report(audit_result: dict) -> str:
    scores = audit_result["scores"]
    findings = audit_result["findings"]

    lines = []
    lines.append("# VibeGuard Audit Report")
    lines.append("")
    lines.append(f"## Overall Readiness Score: {scores['overall']}/100")
    lines.append("")
    lines.append("## Category Scores")
    lines.append("")
    lines.append(f"- Security: {scores['security']}/100")
    lines.append(f"- Documentation: {scores['documentation']}/100")
    lines.append(f"- Deployment: {scores['deployment']}/100")
    lines.append(f"- Code Quality: {scores['code_quality']}/100")
    lines.append(f"- Kaggle Submission Readiness: {scores['kaggle']}/100")
    lines.append("")

    lines.append("## Findings")
    lines.append("")

    if not findings:
        lines.append("No major issues found.")
    else:
        for idx, finding in enumerate(findings, start=1):
            lines.append(f"### {idx}. [{finding['severity']}] {finding['title']}")
            lines.append("")
            lines.append(f"**Source:** `{finding.get('source', 'unknown')}`")
            lines.append("")
            lines.append(f"**Issue:** {finding['message']}")
            lines.append("")
            lines.append(f"**Recommendation:** {finding['recommendation']}")
            lines.append("")

    lines.append("## Recommended Next Steps")
    lines.append("")
    high = [f for f in findings if f["severity"] == "HIGH"]
    medium = [f for f in findings if f["severity"] == "MEDIUM"]

    if high:
        lines.append("1. Fix all HIGH severity security or submission blockers.")
        lines.append("2. Re-run VibeGuard after removing sensitive files or hardcoded secrets.")
        lines.append("3. Improve documentation before publishing the repository.")
    elif medium:
        lines.append("1. Improve README setup, architecture, and deployment sections.")
        lines.append("2. Add screenshots or architecture diagrams.")
        lines.append("3. Re-run VibeGuard before final submission.")
    else:
        lines.append("1. Prepare final demo video.")
        lines.append("2. Attach screenshots and report to the Kaggle Writeup.")
        lines.append("3. Submit before the deadline.")

    lines.append("")
    lines.append("## Kaggle Writeup Starter")
    lines.append("")
    lines.append("Suggested sections:")
    lines.append("")
    lines.append("- Problem Statement")
    lines.append("- Why Agents?")
    lines.append("- Solution Overview")
    lines.append("- Architecture")
    lines.append("- Security Features")
    lines.append("- Deployment")
    lines.append("- Demo Walkthrough")
    lines.append("- Limitations and Future Work")

    return "\n".join(lines)
