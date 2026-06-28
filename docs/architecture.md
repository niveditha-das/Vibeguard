# VibeGuard Architecture

VibeGuard uses a modular multi-agent audit workflow to scan uploaded AI projects and generate a readiness report.

## Simple Flow

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

## What Each Part Does

### Streamlit Web App

This is the user interface. The user uploads a project ZIP file, clicks the audit button, sees scores, reads findings, and downloads the report.

### Safe ZIP Extractor

This safely extracts the uploaded ZIP file. It protects the app from unsafe ZIP paths.

### File Inventory Tool

This creates a list of all files inside the uploaded project. The agents use this list during the audit.

### Orchestrator Agent

This is the main coordinator. It runs all specialist agents and combines their results into one final report.

### Security Agent

This checks for risky files and secret-like patterns, such as:

- .env files
- API keys
- tokens
- credentials files
- private key blocks

### Documentation Agent

This checks whether the project README explains important things such as:

- setup
- installation
- usage
- architecture
- security
- deployment

### Deployment Agent

This checks whether the project has files or instructions needed to run or deploy the app.

Examples:

- requirements.txt
- pyproject.toml
- Dockerfile
- app.py

### Code Quality Agent

This checks basic maintainability signals, such as whether the project has source files, test files, and a clean structure.

### Kaggle Submission Agent

This checks whether the project explains important capstone concepts such as:

- agents
- MCP
- security
- deployment
- architecture

### Gemini Recommendation Agent

This optional agent generates improvement suggestions, README ideas, Kaggle writeup outlines, and demo video structure when a Gemini API key is configured.

## Current Status

The current version uses rule-based specialist agents. This is good for the MVP because it is reliable, easy to test, and safe.

Future upgrades include:

- Google ADK agent implementation
- MCP server integration
- better Gemini-powered recommendations
- public deployment
- final demo video
- Kaggle writeup