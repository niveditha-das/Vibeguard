from mcp_server.server import (
    list_project_files,
    run_security_scan,
    generate_vibeguard_markdown_report,
)


PROJECT_PATH = "examples/sample_bad_project"


def main():
    print("Testing VibeGuard MCP tool functions...\n")

    files = list_project_files(PROJECT_PATH)
    print("Files:")
    print(files)

    print("\nSecurity scan:")
    security = run_security_scan(PROJECT_PATH)
    print(security)

    print("\nMarkdown report:")
    report = generate_vibeguard_markdown_report(PROJECT_PATH)
    print(report[:1500])


if __name__ == "__main__":
    main()