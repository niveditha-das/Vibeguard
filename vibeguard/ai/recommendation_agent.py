import os
from typing import Any

from dotenv import load_dotenv


load_dotenv()


def gemini_is_configured() -> bool:
    """Return True if a Gemini API key appears to be configured."""
    return bool(os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"))


def build_recommendation_prompt(audit_result: dict[str, Any]) -> str:
    """Build a concise prompt from the VibeGuard audit result."""
    scores = audit_result["scores"]
    findings = audit_result["findings"]

    findings_text = []
    for finding in findings[:20]:
        findings_text.append(
            f"- Severity: {finding['severity']}\n"
            f"  Title: {finding['title']}\n"
            f"  Source: {finding.get('source', 'unknown')}\n"
            f"  Issue: {finding['message']}\n"
            f"  Recommendation: {finding['recommendation']}"
        )

    findings_block = "\n".join(findings_text) if findings_text else "No major findings."

    return f"""
You are VibeGuard, an expert AI project auditor.

The user uploaded a software project for a Kaggle-style AI agents capstone.
Your job is to generate practical improvement guidance based on this audit.

Scores:
- Overall: {scores['overall']}/100
- Security: {scores['security']}/100
- Documentation: {scores['documentation']}/100
- Deployment: {scores['deployment']}/100
- Code Quality: {scores['code_quality']}/100
- Kaggle Readiness: {scores['kaggle']}/100

Findings:
{findings_block}

Generate the following sections in Markdown:

## Executive Summary
Briefly explain the current project readiness.

## Top Priority Fixes
Give the 5 most important fixes in priority order.

## README Improvements
Suggest specific README sections the user should add or improve.

## Kaggle Writeup Outline
Create a strong Kaggle Writeup outline under 2,500 words.

## 5-Minute Video Script
Create a clear video script structure with timestamps.

## Final Submission Checklist
Give a checklist for final submission readiness.

Keep the advice specific, practical, and beginner-friendly.
Do not invent files or features that are not implied by the audit.
"""


def generate_ai_recommendations(audit_result: dict[str, Any]) -> str:
    """Generate AI-powered recommendations using Gemini.

    If Gemini is not configured or unavailable, return a helpful fallback message
    instead of crashing the app.
    """
    if not gemini_is_configured():
        return (
            "## Gemini Recommendations Not Enabled\n\n"
            "Gemini recommendations are optional. To enable them:\n\n"
            "1. Create a `.env` file in the project root.\n"
            "2. Add `GEMINI_API_KEY=your_key_here`.\n"
            "3. Restart the Streamlit app.\n\n"
            "The rule-based VibeGuard audit still works without Gemini."
        )

    try:
        from google import genai

        model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        client = genai.Client()

        prompt = build_recommendation_prompt(audit_result)

        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )

        if not response.text:
            return (
                "## Gemini returned an empty response\n\n"
                "The audit completed, but no AI recommendations were generated."
            )

        return response.text

    except Exception as exc:
        return (
            "## Gemini Recommendation Error\n\n"
            "The rule-based audit completed, but Gemini recommendations could not be generated.\n\n"
            f"Error: `{exc}`"
        )