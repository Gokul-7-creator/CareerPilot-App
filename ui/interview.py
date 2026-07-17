import streamlit as st
from ml.mock_interview import evaluate_answer


def render_interview():

    st.markdown("# 🎤 AI Mock Interview")
    st.caption("Practice with AI and improve your interview skills.")

    st.divider()

    # ---------------- Questions ----------------

    st.markdown("## 📋 Generated Interview Questions")

    if st.session_state.questions:

        st.markdown(f"""
<div style="
background:#1E293B;
padding:25px;
border-radius:15px;
border-left:6px solid #3B82F6;
">

{st.session_state.questions}

</div>
""", unsafe_allow_html=True)

    else:
        st.warning("Generate interview questions first.")

    st.divider()

    # ---------------- Answer ----------------

    st.markdown("## 💬 Your Answer")

    question = st.text_input(
        "Interview Question",
        placeholder="Paste a question here..."
    )

    answer = st.text_area(
        "Answer",
        height=220,
        placeholder="Write your answer..."
    )

    if st.button("🤖 Evaluate Answer", use_container_width=True):

        if question and answer:

            with st.spinner("AI is evaluating your answer..."):

                feedback = evaluate_answer(question, answer)

            st.success("Evaluation Completed")

            st.markdown("## 📊 AI Feedback")

            st.markdown(f"""
<div style="
background:#1E293B;
padding:25px;
border-radius:15px;
border-left:6px solid #10B981;
">

{feedback}

</div>
""", unsafe_allow_html=True)

        else:
            st.warning("Please enter both the question and the answer.")