import streamlit as st


def render_cover_letter(job_role):

    st.markdown("# 📝 AI Cover Letter")
    st.caption("Generate a professional cover letter tailored to your target role.")

    st.divider()

    if st.button("✨ Generate Cover Letter", use_container_width=True):

        if st.session_state.cover_letter:

            st.success("✅ Cover Letter Generated Successfully!")

            st.markdown(f"""
<div style="
background:#1E293B;
padding:30px;
border-radius:15px;
border:1px solid #334155;
line-height:1.8;
font-size:17px;
">

{st.session_state.cover_letter.replace(chr(10), "<br>")}

</div>
""", unsafe_allow_html=True)

            st.write("")

            st.download_button(
                "📄 Download Cover Letter",
                data=st.session_state.cover_letter,
                file_name="Cover_Letter.txt",
                mime="text/plain",
                use_container_width=True
            )

        else:

            st.warning("Please analyze your resume first.")