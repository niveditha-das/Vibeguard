# VibeGuard

**A multi-agent safety and submission auditor for vibe-coded AI projects.**

VibeGuard helps developers turn fast AI-generated prototypes into secure, documented, deployable, and submission-ready software.

## Project Links

- [Public Demo App](https://vibeguard-niveditha.streamlit.app/)
- [Architecture Documentation](docs/architecture.md)
- [Sample Audit Report](reports/sample_audit_report.md)
- [Demo Video Script](docs/demo_video_script.md)
- [Kaggle Writeup Draft](docs/kaggle_writeup_draft.md)
- [Final Submission Checklist](docs/final_submission_checklist.md)

## Problem

Vibe coding allows developers to build applications quickly with AI assistance, but fast AI-generated projects often have serious issues:

* Hardcoded API keys or secrets
* Missing README instructions
* Weak project structure
* No deployment guide
* No security notes
* No clear agent architecture explanation
* Incomplete competition submission materials

These issues can make a project unsafe, difficult to run, and hard for judges or users to understand.

## Solution

VibeGuard audits a project ZIP file and generates a structured readiness report.

The current MVP checks:

* Security risks
* README and documentation quality
* Deployment readiness
* Code quality indicators
* Kaggle capstone submission readiness

The app gives the user category scores, detailed findings, recommendations, and a downloadable Markdown audit report.

## Why Agents?

A basic script can check whether files exist, but it cannot easily reason about whether a project is understandable, submission-ready, or well explained.

VibeGuard uses an agent-style architecture where each auditor has a specialized responsibility:

* Security Agent
* Documentation Agent
* Deployment Agent
* Code Quality Agent
* Kaggle Submission Agent
* Orchestrator Agent

The Orchestrator Agent coordinates the specialist agents and combines their findings into one final audit report.

## Architecture

```text
User
 |
 | uploads project ZIP
 v
Streamlit Web App
 |
 v
Safe ZIP Extractor
 |
 v
File Inventory Tool
 |
 v
Orchestrator Agent
 |
 |-- Security Agent
 |-- Documentation Agent
 |-- Deployment Agent
 |-- Code Quality Agent
 |-- Kaggle Submission Agent
 |
 v
Markdown Report Generator
 |
 v
Audit Dashboard + Downloadable Report
```
For a more detailed architecture explanation, see [docs/architecture.md](docs/architecture.md).

## Features

### Security Audit

VibeGuard checks for:

* `.env` files
* `secrets.json`
* `credentials.json`
* API-key-like strings
* token-like strings
* private key blocks

### Documentation Audit

VibeGuard checks whether the README includes important sections such as:

* Setup
* Installation
* Usage
* Architecture
* Security
* Deployment

### Deployment Audit

VibeGuard checks for deployment-related files and signals:

* `requirements.txt`
* `pyproject.toml`
* `Dockerfile`
* App entry point such as `app.py`

### Code Quality Audit

VibeGuard checks for basic maintainability indicators:

* Python source files
* Test files
* Whether the project appears to put all logic into one file

### Kaggle Submission Audit

VibeGuard checks whether the project appears to explain important capstone concepts:

* Agents
* MCP
* Security
* Deployment
* Architecture

## Tech Stack

* Python
* Streamlit
* Modular agent-style Python architecture
* Rule-based audit tools for the MVP
* Future upgrade: Google ADK
* Future upgrade: MCP server
* Future upgrade: Gemini-powered recommendations

## Project Structure

```text
Vibeguard/
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── vibeguard/
│   ├── agents/
│   │   ├── orchestrator.py
│   │   ├── security_agent.py
│   │   ├── docs_agent.py
│   │   ├── deployment_agent.py
│   │   ├── code_quality_agent.py
│   │   └── kaggle_submission_agent.py
│   ├── tools/
│   │   ├── zip_tools.py
│   │   ├── file_tools.py
│   │   └── secret_scanner.py
│   └── reporting/
│       └── markdown_report.py
├── examples/
│   └── sample_bad_project.zip
└── docs/
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/niveditha-das/Vibeguard.git
cd Vibeguard
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

### 5. Test with the sample project

Upload:

```text
examples/sample_bad_project.zip
```

Then click:

```text
Run VibeGuard Audit
```

## Security Design

VibeGuard includes several safety-focused design choices:

* ZIP extraction checks for unsafe path traversal
* `.env` and credential files are flagged
* Hardcoded secret-like patterns are detected
* Real API keys should never be committed
* `.env.example` is used instead of `.env`

## Current Status

This is the first working MVP.

Implemented:

* Streamlit app
* ZIP upload
* Safe ZIP extraction
* File inventory generation
* Security scanner
* Documentation checker
* Deployment checker
* Code quality checker
* Kaggle readiness checker
* Markdown report generator

Planned next:

* Google ADK-based agent implementation
* MCP server for audit tools
* Gemini-powered report improvement
* Architecture diagram
* Public deployment
* Demo video
* Kaggle writeup

## Kaggle Capstone Concepts Demonstrated

This project is designed to demonstrate:

1. Agent / multi-agent system architecture
2. Security features
3. Deployability
4. MCP server integration
5. Agent skills and tool use

The current MVP demonstrates the agent-style architecture, security audit, and deployability checks. ADK and MCP integration will be added in the next development phases.

## Demo Scenario

A user uploads a messy vibe-coded project. VibeGuard scans the project and finds:

* A leaked `.env` file
* Weak README documentation
* Missing deployment instructions
* No tests
* Missing capstone concept explanations

VibeGuard then generates a clear audit report with scores and recommended fixes.

## Sample Output

A sample audit report generated by VibeGuard is available here:

[View sample audit report](reports/sample_audit_report.md)

## License

This project is for educational and capstone demonstration purposes.
