import streamlit as st
from utils.pdf_report import generate_pdf


def render_download():

    st.markdown("# 📥 Download Reports")
    st.caption("Download your AI-generated career report.")

    st.divider()

    st.info("""
Your report includes:

✅ Resume Analysis

✅ ATS Score

✅ Resume Match

✅ Skill Gap Analysis

✅ AI Recruiter Report

✅ Career Roadmap

✅ Cover Letter
""")

    st.divider()

    if st.button("📄 Generate PDF Report", use_container_width=True):

        with st.spinner("Generating PDF..."):

            filename = "AI_Career_Report.pdf"

            generate_pdf(
                filename,

                st.session_state.email,
                st.session_state.phone,
                st.session_state.github,
                st.session_state.linkedin,

                st.session_state.ats_score,
                st.session_state.match_score,

                st.session_state.matched_skills,
                st.session_state.missing_skills,

                st.session_state.result,
                st.session_state.questions,
                st.session_state.improvements,
                st.session_state.roadmap,
                st.session_state.cover_letter
            )

        st.success("✅ PDF Generated Successfully!")

        with open(filename, "rb") as pdf_file:

            st.download_button(
                label="⬇ Download PDF Report",
                data=pdf_file,
                file_name="AI_Career_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )