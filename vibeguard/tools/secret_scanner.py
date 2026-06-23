import re
from pathlib import Path
from vibeguard.tools.file_tools import read_text_file


SECRET_PATTERNS = {
    "Generic API Key": re.compile(r"(?i)(api[_-]?key|apikey)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    "Generic Token": re.compile(r"(?i)(token|access_token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    "AWS Access Key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "Private Key Block": re.compile(r"-----BEGIN (RSA |EC |OPENSSH |)?PRIVATE KEY-----"),
}


SENSITIVE_FILENAMES = {
    ".env",
    "secrets.json",
    "credentials.json",
    "service_account.json",
}


def scan_for_secrets(root_dir: Path, relative_files: list[str]) -> list[dict]:
    findings = []

    for rel in relative_files:
        path = root_dir / rel
        filename = path.name

        if filename in SENSITIVE_FILENAMES:
            findings.append({
                "severity": "HIGH",
                "title": "Sensitive file included",
                "message": f"`{rel}` looks like a secrets or credentials file.",
                "recommendation": "Remove this file from the repository and provide a safe .env.example instead.",
                "source": rel,
            })

        if path.suffix.lower() not in {".py", ".js", ".ts", ".json", ".toml", ".yaml", ".yml", ".env", ".txt", ".md"}:
            continue

        content = read_text_file(path)
        for pattern_name, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                findings.append({
                    "severity": "HIGH",
                    "title": f"Possible secret detected: {pattern_name}",
                    "message": f"`{rel}` may contain a hardcoded secret.",
                    "recommendation": "Move secrets into environment variables and rotate any exposed credentials.",
                    "source": rel,
                })

    return findings
