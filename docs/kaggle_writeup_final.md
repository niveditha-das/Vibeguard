# VibeGuard: A Multi-Agent Safety and Submission Auditor for Vibe-Coded Projects

## Project Summary

VibeGuard is a multi-agent audit tool that helps developers check whether a fast-built or AI-generated project is secure, documented, deployable, maintainable, and ready for submission.

The project focuses on a common problem in vibe coding: AI-assisted tools can help developers build quickly, but the resulting projects are not always safe, complete, or easy to evaluate. A project may appear functional while still containing hidden issues such as missing setup instructions, weak documentation, exposed secret files, unclear architecture, missing deployment guidance, or incomplete final submission materials.

VibeGuard addresses this by allowing a user to upload a project ZIP file and receive a structured audit report. The report includes category scores, detailed findings, recommendations, a downloadable Markdown report, and optional Gemini-powered improvement guidance.

## Project Links

* GitHub Repository: https://github.com/niveditha-das/Vibeguard
* Public Demo App: https://vibeguard-niveditha.streamlit.app/
* Architecture Documentation: https://github.com/niveditha-das/Vibeguard/blob/main/docs/architecture.md
* Sample Audit Report: https://github.com/niveditha-das/Vibeguard/blob/main/reports/sample_audit_report.md
* Demo Video Script: https://github.com/niveditha-das/Vibeguard/blob/main/docs/demo_video_script.md
* Final Submission Checklist: https://github.com/niveditha-das/Vibeguard/blob/main/docs/final_submission_checklist.md

## Problem

Vibe coding makes software development faster, but fast development can create incomplete or risky projects. This is especially important for AI-agent projects, where developers often work with APIs, environment variables, file access, tools, and external services.

Common issues include:

* Exposed `.env` files or credentials
* Hardcoded API keys or tokens
* Missing README setup instructions
* Missing deployment guidance
* Weak explanation of architecture
* No clear security section
* No sample output
* No final demo plan
* Missing explanation of course concepts

These problems can make a project harder to run, harder to judge, and less safe to share publicly.

## Solution

VibeGuard acts as a project auditor. The user uploads a ZIP file, and VibeGuard scans the project using specialist audit agents.

The system currently checks five major areas:

1. Security readiness
2. Documentation quality
3. Deployment readiness
4. Code quality indicators
5. Kaggle-style submission readiness

After the audit, VibeGuard displays a readiness dashboard with scores and finding counts. It also provides detailed findings, a file inventory, a downloadable Markdown audit report, capstone submission guidance, and Gemini-powered recommendations.

The goal is not to replace full static analysis tools. Instead, VibeGuard focuses on practical project readiness: whether a project is safe enough, clear enough, and complete enough to submit or share.

## Agent Architecture

VibeGuard uses a modular multi-agent workflow.

The user uploads a project ZIP file through the Streamlit web app. The app safely extracts the ZIP file, builds a file inventory, and passes the project information to the Orchestrator Agent.

The Orchestrator Agent coordinates five specialist agents:

1. Security Agent
   Checks for risky files and secret-like patterns, including `.env` files, credentials files, API keys, tokens, and private key blocks.

2. Documentation Agent
   Checks whether the README explains setup, installation, usage, architecture, security, and deployment.

3. Deployment Agent
   Checks whether the project includes files and signals needed to run or deploy the app, such as `requirements.txt`, `pyproject.toml`, `Dockerfile`, or an app entry point.

4. Code Quality Agent
   Checks basic maintainability indicators such as source files, test files, and project structure.

5. Kaggle Submission Agent
   Checks whether the project explains important capstone concepts such as agents, MCP, security, deployment, and architecture.

The final audit result is passed to a Markdown report generator and displayed in the Streamlit dashboard.

VibeGuard also includes a Gemini Recommendation Agent. This optional agent uses Gemini to turn the audit findings into an improvement plan, README suggestions, a writeup outline, a video script, and a final submission checklist.

## Implementation

VibeGuard is implemented in Python with Streamlit.

The main app is `app.py`. It handles the user interface, ZIP upload, audit settings, dashboard rendering, report download, and Gemini recommendation workflow.

The project is organized into modular folders:

* `vibeguard/agents/` contains the specialist audit agents and orchestrator.
* `vibeguard/tools/` contains utility tools for ZIP extraction, file inventory generation, and secret scanning.
* `vibeguard/reporting/` contains the Markdown report generator.
* `vibeguard/ai/` contains the Gemini-powered recommendation agent.
* `docs/` contains architecture documentation, screenshots, writeup drafts, and submission materials.
* `reports/` contains a sample generated audit report.
* `examples/` contains a sample bad project used for the demo.

The app uses Streamlit session state so audit results remain available after the user clicks buttons such as “Generate AI Recommendations.” This solved an important usability issue where Streamlit would otherwise reload and return to the upload state.

The deployed version runs publicly through Streamlit Community Cloud, while the source code is available in a public GitHub repository.

## Course Concepts Demonstrated

VibeGuard demonstrates several important course concepts.

### Multi-Agent System Design

The project separates the audit process into specialist agents. Each agent has a clear responsibility, and the Orchestrator Agent combines their findings into a final report.

### Tool Use

The agents rely on project scanning utilities such as safe ZIP extraction, file inventory generation, and secret scanning. This makes the agent workflow grounded in actual project files rather than only natural language reasoning.

### Security Features

Security is a central part of VibeGuard. The app detects risky files and secret-like patterns, including `.env` files, credentials files, API-key-like strings, token-like strings, and private key blocks. It also encourages safer project practices such as using `.env.example` instead of committing real secrets.

### Deployability

The project is deployable and publicly accessible. It includes a Streamlit interface, dependency file, GitHub repository, and public deployed app.

### AI-Powered Recommendations

Gemini is used to generate improvement guidance from the audit result. This makes the app more useful because it not only identifies problems, but also helps users decide how to fix them.

### MCP-Ready Architecture

The project is structured so that scanning tools can be exposed through an MCP server in a future version. This would allow agent tools such as file listing, file reading, secret scanning, and report generation to be called through a standardized tool interface.

## Demo Scenario

The demo uses the included `sample_bad_project.zip`.

The flow is:

1. Open the deployed VibeGuard app.
2. Upload `sample_bad_project.zip`.
3. Click “Run VibeGuard Audit.”
4. Show the readiness dashboard.
5. Show detailed findings.
6. Show the downloadable Markdown report.
7. Open AI Recommendations.
8. Click “Generate AI Recommendations.”
9. Show the Gemini-generated improvement plan.

This demo clearly shows the value of VibeGuard. A messy project is transformed into a structured readiness report with practical next steps.

## Results

The current version successfully performs project audits locally and through the deployed Streamlit app. It can identify common project readiness issues, including risky files, missing documentation sections, incomplete deployment guidance, and weak capstone concept explanations.

The app also generates a downloadable Markdown report and optional Gemini recommendations. This gives users both a diagnostic view and a practical improvement plan.

## Limitations

VibeGuard is currently an MVP. Some checks are rule-based, so the system may not catch every possible security or code quality issue. It does not yet execute tests, perform deep static analysis, or automatically modify project files.

Future improvements could include:

* GitHub repository URL scanning
* Deeper code analysis
* Test execution
* PDF report export
* Automatic README patch generation
* Stronger MCP server integration
* Google ADK implementation
* Architecture diagram generation
* Better severity scoring

## Conclusion

VibeGuard helps developers turn fast AI-generated prototypes into safer, clearer, more deployable, and more submission-ready projects.

The project shows that agents can be useful not only for generating software, but also for reviewing, improving, and preparing software for real-world use. By combining specialist audit agents, security checks, deployability checks, documentation review, and Gemini-powered recommendations, VibeGuard provides a practical tool for improving vibe-coded projects before they are shared or submitted.
