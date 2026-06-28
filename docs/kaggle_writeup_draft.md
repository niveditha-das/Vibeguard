# VibeGuard: A Multi-Agent Safety and Submission Auditor for Vibe-Coded Projects

## Project Summary

VibeGuard is a multi-agent audit tool that helps developers check whether a fast-built or AI-generated project is secure, documented, deployable, maintainable, and ready for capstone submission.

The project was built around a simple problem: vibe coding makes it easier to create software quickly, but fast AI-generated projects can often contain hidden risks. A project may appear to work, but still have missing setup instructions, weak documentation, exposed secret files, unclear architecture, missing deployment guidance, or incomplete submission materials.

VibeGuard addresses this by letting a user upload a project ZIP file and receive a structured audit report. The report includes category scores, detailed findings, recommendations, a downloadable Markdown report, and optional Gemini-powered improvement guidance.

## Problem

AI-assisted development can speed up software creation, but it can also create incomplete or unsafe projects. Developers may forget to check for:

* hardcoded API keys
* `.env` files committed into a project
* missing README instructions
* unclear deployment steps
* weak project structure
* missing tests
* incomplete explanation of agent architecture
* missing capstone submission materials

These issues are especially important in agent-based projects, where tools, files, APIs, and environment variables can introduce security and reliability risks.

## Solution

VibeGuard acts as a project auditor. A user uploads a ZIP file, and VibeGuard scans the project using specialist audit agents.

The current system checks:

* security risks
* README and documentation quality
* deployment readiness
* code quality indicators
* Kaggle-style capstone submission readiness

After the scan, VibeGuard generates a readiness dashboard and a downloadable Markdown report. If Gemini is configured, it can also generate an improvement plan, README suggestions, a Kaggle writeup outline, a 5-minute video structure, and a final submission checklist.

## Agent Architecture

VibeGuard uses a modular multi-agent workflow.

The main components are:

1. Streamlit Web App
   Provides the interface for uploading projects, running audits, viewing results, and downloading reports.

2. Safe ZIP Extractor
   Extracts the uploaded project safely and avoids unsafe ZIP paths.

3. File Inventory Tool
   Builds a list of project files so the audit agents can inspect the structure.

4. Orchestrator Agent
   Coordinates all specialist agents and combines their findings into a final audit result.

5. Security Agent
   Detects risky files and secret-like patterns such as `.env`, credentials files, API keys, tokens, and private key blocks.

6. Documentation Agent
   Checks whether the README explains setup, installation, usage, architecture, security, and deployment.

7. Deployment Agent
   Checks for files and signals needed to run or deploy the app, such as `requirements.txt`, `pyproject.toml`, `Dockerfile`, and app entry points.

8. Code Quality Agent
   Checks basic maintainability indicators such as source files, tests, and project structure.

9. Kaggle Submission Agent
   Checks whether the project explains important capstone concepts such as agents, MCP, security, deployment, and architecture.

10. Gemini Recommendation Agent
    Optionally uses Gemini to turn audit findings into practical project improvement guidance.

## Implementation

The project is implemented in Python with Streamlit.

The app accepts a ZIP file upload, extracts the project, builds a file inventory, runs each enabled audit agent, and displays the results in a dashboard. The result is also converted into a Markdown audit report that the user can download.

The app uses session state so that audit results remain available after the user clicks buttons such as “Generate AI Recommendations.” This improves the user experience and makes the Gemini workflow smoother.

The project also includes a sample bad project ZIP file and a sample audit report, so judges and users can understand the expected output.

## Course Concepts Demonstrated

VibeGuard demonstrates several important agent and deployment concepts:

1. Multi-agent system design
   The project separates auditing into specialist agents coordinated by an orchestrator.

2. Tool use
   The agents rely on project scanning tools such as ZIP extraction, file inventory generation, and secret scanning.

3. Security features
   VibeGuard detects risky files and secret-like patterns, and it encourages safe handling of environment variables.

4. Deployability
   The project includes a Streamlit interface, dependency file, GitHub repository, and public deployment.

5. AI-powered recommendations
   Gemini is used to generate improvement plans, README suggestions, writeup outlines, video scripts, and submission checklists.

## Demo Scenario

The demo uses a sample project called `sample_bad_project.zip`.

The user uploads the ZIP file into VibeGuard and clicks “Run VibeGuard Audit.” VibeGuard scans the project and shows:

* overall readiness score
* security score
* documentation score
* deployment score
* Kaggle readiness score
* detailed findings
* downloadable Markdown report
* Gemini-powered recommendations

This demo clearly shows how VibeGuard turns a messy project into an actionable improvement plan.

## Results

The current version successfully performs local and deployed audits. It identifies common project issues such as missing documentation, risky files, incomplete deployment instructions, and weak capstone readiness. It also generates a Markdown report and optional AI-powered recommendations.

## Limitations

The current version is an MVP. Some checks are rule-based and may not catch every possible issue. The system does not yet perform deep static analysis, execute tests, or automatically modify project files.

Future improvements could include:

* deeper code analysis
* GitHub repository URL scanning
* PDF report export
* automatic README patch generation
* stronger MCP server integration
* Google ADK implementation
* richer architecture visualization
* automated test detection and execution

## Conclusion

VibeGuard helps developers turn fast AI-generated prototypes into safer, clearer, more deployable, and submission-ready projects. It is useful because it focuses on the practical problems that appear after vibe coding: security, documentation, deployment, and final presentation quality.

The project shows how agents can be used not only to build software, but also to review and improve software before it is shared with others.
