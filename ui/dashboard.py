import streamlit as st

def render_dashboard():

    st.markdown("## 📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    cards = [
        ("📈 ATS Score", f"{st.session_state.ats_score}/100", "#3B82F6"),
        ("🎯 Resume Match", f"{st.session_state.match_score:.1f}%", "#10B981"),
        ("🛠 Skills", str(len(st.session_state.skills)), "#F59E0B"),
        ("❌ Missing Skills", str(len(st.session_state.missing_skills)), "#EF4444")
    ]

    for col, (title, value, color) in zip([col1, col2, col3, col4], cards):

        with col:
            st.markdown(
                f"""
            <div style="
            background:#1E293B;
            border-radius:20px;
            padding:25px;
            border-top:6px solid {color};
            text-align:center;
            box-shadow:0px 8px 20px rgba(0,0,0,0.25);
            ">

            <h4 style="color:white;">
            {title}
            </h4>

            <h1 style="color:{color};">
            {value}
            </h1>

            </div>
            """,
                unsafe_allow_html=True
            )

            