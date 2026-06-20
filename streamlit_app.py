import tempfile
from pathlib import Path

import streamlit as st

from app.services.pipeline.ddr_pipeline import (
    DDRPipeline,
)

from app.services.reports.html_renderer import (
    HTMLRenderer,
)

from app.services.reports.pdf_exporter import (
    PDFExporter,
)

st.set_page_config(
    page_title="DDR Report Generator",
    page_icon="🏠",
    layout="wide",
)

st.title("🏠 DDR Report Generator")

st.markdown(
    """
Generate an AI-powered Detailed Diagnostic Report
from an Inspection Report and Thermal Survey.
"""
)

inspection_pdf = st.file_uploader(
    "Upload Inspection Report PDF",
    type=["pdf"],
)

thermal_pdf = st.file_uploader(
    "Upload Thermal Report PDF",
    type=["pdf"],
)

if st.button(
    "Generate DDR",
    type="primary",
):
    if not inspection_pdf or not thermal_pdf:
        st.error(
            "Please upload both PDFs."
        )

    else:

        with st.spinner(
            "Generating report..."
        ):

            temp_dir = Path(
                tempfile.mkdtemp()
            )

            inspection_path = (
                temp_dir
                / inspection_pdf.name
            )

            thermal_path = (
                temp_dir
                / thermal_pdf.name
            )

            with open(
                inspection_path,
                "wb",
            ) as f:
                f.write(
                    inspection_pdf.getbuffer()
                )

            with open(
                thermal_path,
                "wb",
            ) as f:
                f.write(
                    thermal_pdf.getbuffer()
                )

            pipeline = DDRPipeline()

            report = pipeline.run(
                inspection_pdf=str(
                    inspection_path
                ),
                thermal_pdf=str(
                    thermal_path
                ),
            )

            html = (
                HTMLRenderer()
                .render(report)
            )

            output_path = (
                temp_dir
                / "DDR_Report.pdf"
            )

            pdf_file = (
                PDFExporter()
                .export(
                    html,
                    str(output_path),
                )
            )

        st.success(
            "DDR generated successfully."
        )

        st.subheader("Executive Summary")
        st.write(report.property_issue_summary)

        st.subheader("Property Risk Overview")
        
        high_count = len([s for s in report.severity_assessments if s.level.value == "HIGH"])
        medium_count = len([s for s in report.severity_assessments if s.level.value == "MEDIUM"])
        low_count = len([s for s in report.severity_assessments if s.level.value == "LOW"])
        
        col1, col2, col3 = st.columns(3)
        col1.metric("High Risk", high_count)
        col2.metric("Medium Risk", medium_count)
        col3.metric("Low Risk", low_count)

        if report.missing_information or report.conflicts:
            st.subheader("Quality Review")
            if report.missing_information:
                st.write("**Missing Information:**")
                for item in report.missing_information:
                    st.write(f"- {item}")
            if report.conflicts:
                st.write("**Conflicts:**")
                for item in report.conflicts:
                    st.write(f"- {item}")

        st.subheader("Processing Metadata")
        st.write(f"- **Confidence Score:** {int(report.metadata.confidence * 100)}%")
        st.write(f"- **Engine Version:** {report.metadata.model_version}")
        st.write(f"- **Processing Time:** {report.metadata.extraction_time_seconds:.2f} seconds")

        st.markdown("---")

        with open(pdf_file, "rb") as f:
            st.download_button(
                label="📄 Download DDR Report",
                data=f.read(),
                file_name="DDR_Report.pdf",
                mime="application/pdf",
            )