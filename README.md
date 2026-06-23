# VibeGuard

VibeGuard is a multi-agent safety and submission auditor for vibe-coded projects.

It helps developers check whether a project is secure, documented, deployable, and ready for a Kaggle-style capstone submission.

## Current MVP

This starter version includes a local Streamlit app that can:

- Upload a ZIP project
- Extract and inspect the file tree safely
- Detect common secret patterns
- Check README quality
- Check deployment readiness
- Check Kaggle submission readiness
- Generate a Markdown audit report

## Tech Stack

- Python
- Streamlit
- Rule-based audit tools for the first MVP
- Future versions: Google ADK, MCP server, Gemini API

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

```text
vibeguard/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── vibeguard/
│   ├── agents/
│   ├── tools/
│   └── reporting/
├── examples/
└── docs/
```

## Security Note

Never commit real API keys, passwords, tokens, or `.env` files.
Use `.env.example` to document required environment variables.
