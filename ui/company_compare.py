import streamlit as st
import pandas as pd

from rag.gemini_client import generate_job_description
from rag.gemini_client import analyze_resume

import re


def render_company_compare():

    st.subheader("🏢 Resume Comparison Across Companies")

    companies = [
        "Google",
        "Microsoft",
        "Amazon",
        "TCS",
        "Infosys"
    ]

    results = []

    resume = st.session_state.resume_text
    role = st.session_state.get("selected_role", "AI Engineer")

    for company in companies:

        jd = generate_job_description(role, company)

        report = analyze_resume(resume, jd)

        match = re.search(r"ATS Score[:\s]*([0-9]+)", report)

        score = int(match.group(1)) if match else 0

        if score >= 85:
            status = "🟢 Excellent"
        elif score >= 70:
            status = "🟡 Good"
        else:
            status = "🔴 Improve"

        results.append({
            "Company": company,
            "ATS Score": score,
            "Status": status
        })

    df = pd.DataFrame(results)

    st.dataframe(
        df.sort_values(
            "ATS Score",
            ascending=False
        ),
        use_container_width=True
    )