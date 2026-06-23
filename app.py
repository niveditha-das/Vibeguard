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

st.title("🛡️ VibeGuard")
st.subheader("AI Project Safety & Submission Auditor")

st.write(
    "Upload a ZIP file of your project. VibeGuard will inspect security, documentation, "
    "deployment readiness, code quality, and Kaggle submission readiness."
)

uploaded_file = st.file_uploader("Upload your project ZIP", type=["zip"])

with st.sidebar:
    st.header("Audit Options")
    include_security = st.checkbox("Security audit", value=True)
    include_docs = st.checkbox("Documentation audit", value=True)
    include_deployment = st.checkbox("Deployment audit", value=True)
    include_code_quality = st.checkbox("Code quality audit", value=True)
    include_kaggle = st.checkbox("Kaggle submission audit", value=True)

if uploaded_file is not None:
    if st.button("Run VibeGuard Audit", type="primary"):
        with st.spinner("Scanning project..."):
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

        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Overall", f"{audit_result['scores']['overall']}/100")
        col2.metric("Security", f"{audit_result['scores']['security']}/100")
        col3.metric("Docs", f"{audit_result['scores']['documentation']}/100")
        col4.metric("Deploy", f"{audit_result['scores']['deployment']}/100")
        col5.metric("Kaggle", f"{audit_result['scores']['kaggle']}/100")

        st.header("File Inventory")
        st.code("\n".join(inventory["relative_files"][:200]), language="text")

        st.header("Audit Findings")
        for finding in audit_result["findings"]:
            severity = finding["severity"]
            title = finding["title"]
            message = finding["message"]
            recommendation = finding["recommendation"]

            if severity == "HIGH":
                st.error(f"**{severity}: {title}**\n\n{message}\n\nRecommendation: {recommendation}")
            elif severity == "MEDIUM":
                st.warning(f"**{severity}: {title}**\n\n{message}\n\nRecommendation: {recommendation}")
            else:
                st.info(f"**{severity}: {title}**\n\n{message}\n\nRecommendation: {recommendation}")

        st.header("Markdown Report")
        st.download_button(
            label="Download audit_report.md",
            data=report_md,
            file_name="audit_report.md",
            mime="text/markdown",
        )
        st.code(report_md, language="markdown")
else:
    st.info("Upload a ZIP file to begin.")
