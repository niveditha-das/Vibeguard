import streamlit as st

from vibeguard.tools.zip_tools import extract_zip_safely
from vibeguard.tools.file_tools import build_file_inventory
from vibeguard.agents.orchestrator import run_audit
from vibeguard.reporting.markdown_report import build_markdown_report


st.set_page_config(
    page_title="VibeGuard",
    page_icon="🛡️",
    layout="wide",
)


def score_label(score: int) -> str:
    if score >= 85:
        return "Excellent"
    if score >= 70:
        return "Good"
    if score >= 50:
        return "Needs Work"
    return "High Risk"


def score_help(score: int) -> str:
    if score >= 85:
        return "This area looks strong."
    if score >= 70:
        return "This area is usable but can be improved."
    if score >= 50:
        return "This area needs attention before submission."
    return "This area may block a safe or complete submission."


def render_finding(finding: dict) -> None:
    severity = finding["severity"]
    title = finding["title"]
    message = finding["message"]
    recommendation = finding["recommendation"]
    source = finding.get("source", "unknown")

    body = (
        f"**Source:** `{source}`\n\n"
        f"**Issue:** {message}\n\n"
        f"**Recommendation:** {recommendation}"
    )

    if severity == "HIGH":
        st.error(f"**{severity}: {title}**\n\n{body}")
    elif severity == "MEDIUM":
        st.warning(f"**{severity}: {title}**\n\n{body}")
    else:
        st.info(f"**{severity}: {title}**\n\n{body}")


def render_score_card(title: str, score: int) -> None:
    st.metric(title, f"{score}/100", score_label(score))
    st.caption(score_help(score))


st.title("🛡️ VibeGuard")
st.markdown(
    """
    ### Multi-Agent Safety & Submission Auditor for Vibe-Coded Projects

    VibeGuard helps developers check whether an AI-generated or fast-built project is
    **secure, documented, deployable, maintainable, and ready for capstone submission**.
    """
)

with st.expander("What does VibeGuard check?", expanded=False):
    st.markdown(
        """
        VibeGuard currently performs five audits:

        1. **Security Audit**: looks for `.env` files, credentials, tokens, private keys, and API-key-like strings.
        2. **Documentation Audit**: checks whether the README explains setup, usage, architecture, security, and deployment.
        3. **Deployment Audit**: checks for dependency files and a clear app entry point.
        4. **Code Quality Audit**: checks for source files, tests, and maintainability indicators.
        5. **Kaggle Submission Audit**: checks whether the project explains agent concepts, MCP, security, deployment, and architecture.
        """
    )

st.divider()

with st.sidebar:
    st.header("Audit Settings")
    st.write("Choose which audit agents to run.")

    include_security = st.checkbox("Security Agent", value=True)
    include_docs = st.checkbox("Documentation Agent", value=True)
    include_deployment = st.checkbox("Deployment Agent", value=True)
    include_code_quality = st.checkbox("Code Quality Agent", value=True)
    include_kaggle = st.checkbox("Kaggle Submission Agent", value=True)

    st.divider()

    st.markdown(
        """
        **Demo tip:**  
        Upload `examples/sample_bad_project.zip` to see VibeGuard find realistic issues.
        """
    )

uploaded_file = st.file_uploader(
    "Upload a project ZIP file",
    type=["zip"],
    help="Upload a ZIP archive containing the project you want VibeGuard to audit.",
)

if uploaded_file is None:
    st.info("Upload a ZIP file to begin the audit.")
    st.stop()

if st.button("Run VibeGuard Audit", type="primary", use_container_width=True):
    with st.spinner("Running VibeGuard agents..."):
        extract_dir = extract_zip_safely(uploaded_file)
        inventory = build_file_inventory(extract_dir)

        options = {
            "security": include_security,
            "documentation": include_docs,
            "deployment": include_deployment,
            "code_quality": include_code_quality,
            "kaggle": include_kaggle,
        }

        audit_result = run_audit(extract_dir, inventory, options)
        report_md = build_markdown_report(audit_result)

    st.success("Audit complete.")

    scores = audit_result["scores"]
    findings = audit_result["findings"]

    high_count = len([f for f in findings if f["severity"] == "HIGH"])
    medium_count = len([f for f in findings if f["severity"] == "MEDIUM"])
    low_count = len([f for f in findings if f["severity"] == "LOW"])

    st.header("Readiness Dashboard")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        render_score_card("Overall", scores["overall"])
    with col2:
        render_score_card("Security", scores["security"])
    with col3:
        render_score_card("Docs", scores["documentation"])
    with col4:
        render_score_card("Deploy", scores["deployment"])
    with col5:
        render_score_card("Kaggle", scores["kaggle"])

    st.subheader("Finding Summary")

    s1, s2, s3, s4 = st.columns(4)
    s1.metric("High Severity", high_count)
    s2.metric("Medium Severity", medium_count)
    s3.metric("Low Severity", low_count)
    s4.metric("Files Scanned", inventory["file_count"])

    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Findings", "File Inventory", "Markdown Report", "Submission Help"]
    )

    with tab1:
        st.header("Detailed Findings")

        if not findings:
            st.success("No major findings detected.")
        else:
            severity_filter = st.radio(
                "Filter by severity",
                ["All", "HIGH", "MEDIUM", "LOW"],
                horizontal=True,
            )

            filtered_findings = findings
            if severity_filter != "All":
                filtered_findings = [
                    f for f in findings if f["severity"] == severity_filter
                ]

            if not filtered_findings:
                st.info(f"No {severity_filter} findings.")
            else:
                for finding in filtered_findings:
                    render_finding(finding)

    with tab2:
        st.header("Project File Inventory")
        st.caption("First 250 files are shown.")
        st.code("\n".join(inventory["relative_files"][:250]), language="text")

    with tab3:
        st.header("Downloadable Audit Report")

        st.download_button(
            label="Download audit_report.md",
            data=report_md,
            file_name="audit_report.md",
            mime="text/markdown",
            use_container_width=True,
        )

        st.code(report_md, language="markdown")

    with tab4:
        st.header("Capstone Submission Guidance")

        st.markdown(
            """
            For a strong Kaggle capstone submission, your final project should include:

            - Clear problem statement
            - Explanation of why agents are useful
            - Architecture diagram
            - Public GitHub repository
            - Public demo or setup instructions
            - Short video demonstration
            - Security explanation
            - Deployment explanation
            - At least three course concepts demonstrated
            """
        )

        st.subheader("Suggested Video Structure")

        st.markdown(
            """
            1. **Problem**: vibe-coded projects can be insecure and incomplete.
            2. **Solution**: VibeGuard audits projects before submission or deployment.
            3. **Architecture**: show the orchestrator and specialist audit agents.
            4. **Demo**: upload the sample bad project and show the report.
            5. **Technical Concepts**: explain security, deployability, ADK/MCP plan, and agent tools.
            """
        )