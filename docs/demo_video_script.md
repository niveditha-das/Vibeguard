# VibeGuard 5-Minute Demo Video Script

## 0:00-0:30 Introduction

Hi, my project is VibeGuard, a multi-agent safety and submission auditor for vibe-coded AI projects.

Vibe coding helps developers build quickly, but fast AI-generated projects can have hidden problems such as missing documentation, weak deployment instructions, exposed secrets, unclear architecture, and incomplete submission materials.

VibeGuard helps solve this by scanning a project and generating a clear readiness report.

## 0:30-1:10 Problem

The problem is that many AI-generated prototypes appear to work, but are not ready to submit or deploy.

They may include `.env` files, hardcoded keys, missing setup instructions, no security explanation, no architecture description, or no clear demo plan.

This matters because agent projects often use tools, APIs, files, and environment variables, so security and documentation are important.

## 1:10-2:00 Solution and Architecture

VibeGuard uses a modular multi-agent workflow.

The user uploads a project ZIP file into the Streamlit app. VibeGuard safely extracts the ZIP file, builds a file inventory, and sends the project to an Orchestrator Agent.

The Orchestrator Agent coordinates five specialist agents:

- Security Agent
- Documentation Agent
- Deployment Agent
- Code Quality Agent
- Kaggle Submission Agent

Each agent checks a different part of the project. The results are combined into one final audit report.

## 2:00-3:20 Live Demo

Now I will demonstrate VibeGuard using a sample bad project.

First, I upload `sample_bad_project.zip`.

Then I click “Run VibeGuard Audit.”

VibeGuard scans the project and generates a readiness dashboard. It shows an overall score plus separate scores for security, documentation, deployment, and Kaggle readiness.

The findings section shows specific issues, such as risky files, missing README sections, missing deployment instructions, or incomplete capstone explanations.

The Markdown Report section lets the user download a full audit report.

## 3:20-4:20 Gemini Recommendations

VibeGuard also includes optional Gemini-powered recommendations.

When I open the AI Recommendations section and click “Generate AI Recommendations,” Gemini turns the audit findings into practical next steps.

It generates an executive summary, top priority fixes, README improvements, a Kaggle writeup outline, a 5-minute video script, and a final submission checklist.

This makes the tool useful not only for finding problems, but also for helping developers improve their projects.

## 4:20-4:50 Course Concepts

This project demonstrates several course concepts:

- multi-agent system design
- tool use
- security features
- deployability
- AI-powered recommendations
- planned MCP and ADK integration

The project is deployed publicly with Streamlit and the code is available on GitHub.

## 4:50-5:00 Conclusion

VibeGuard helps developers turn fast AI-generated prototypes into safer, clearer, more deployable, and submission-ready projects.

It shows how agents can support not only software creation, but also software review, security, documentation, and final project preparation.