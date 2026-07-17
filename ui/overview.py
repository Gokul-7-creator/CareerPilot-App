import streamlit as st

def render_overview():

    st.markdown("# 📄 Resume Analysis")
    st.caption("Complete AI-powered analysis of your resume")

    st.divider()

    # ---------------- Candidate ----------------

    st.markdown("## 👤 Candidate Information")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"""
**📧 Email**

{st.session_state.email}

**📱 Phone**

{st.session_state.phone}
""")

    with col2:
        st.info(f"""
**💻 GitHub**

{st.session_state.github}

**🔗 LinkedIn**

{st.session_state.linkedin}
""")

    st.divider()

    # ---------------- Skills ----------------

    st.markdown("## 🛠 Extracted Skills")

    if st.session_state.skills:

        cols = st.columns(4)

        for i, skill in enumerate(st.session_state.skills):
            with cols[i % 4]:
                st.markdown(
                    f"""
                <div style="
                background:#2563EB;
                padding:8px;
                border-radius:25px;
                text-align:center;
                color:white;
                font-weight:bold;
                margin:4px;
                ">
                {skill}
                </div>
                """,
                unsafe_allow_html=True
                )

    else:
        st.warning("No skills detected.")

    st.divider()

    # ---------------- Resume Match ----------------

    st.markdown("## 🎯 Resume Match")

    st.progress(st.session_state.match_score / 100)

    match = st.session_state.match_score

    st.progress(match / 100)

    if match >= 80:
        st.success(f"🎯 Resume Match: {match:.1f}%")
    elif match >= 60:
        st.warning(f"⚠ Resume Match: {match:.1f}%")
    else:
        st.error(f"❌ Resume Match: {match:.1f}%")

    st.divider()

    # ---------------- ATS ----------------

    st.markdown("## 📊 ATS Score")

    score = st.session_state.ats_score

    st.progress(score / 100)

    if score >= 85:
        st.success(f"🟢 Excellent ATS Score: {score}/100")
    elif score >= 70:
        st.warning(f"🟡 Good ATS Score: {score}/100")
    else:
        st.error(f"🔴 Low ATS Score: {score}/100")

    # ---------------- Missing Skills ----------------

    st.markdown("## ❌ Missing Skills")

    if st.session_state.missing_skills:

        cols = st.columns(4)

        for i, skill in enumerate(st.session_state.missing_skills):
            with cols[i % 4]:
                st.markdown(
                    f"""
                <div style="
                background:#EF4444;
                padding:8px;
                border-radius:25px;
                text-align:center;
                color:white;
                font-weight:bold;
                margin:4px;
                ">
                {skill}
                </div>
                """,
                unsafe_allow_html=True
                )

    else:
        st.success("No missing skills 🎉")

    st.divider()

    # ---------------- Recruiter Report ----------------

    st.markdown("## 🤖 AI Recruiter Report")

    st.info(st.session_state.result)