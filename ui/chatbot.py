import streamlit as st
from rag.gemini_client import ask_ai

def render_chatbot():

    st.subheader("💬 AI Career Assistant")

    st.write(
        "Ask anything about your resume, ATS score, career roadmap, or interview preparation."
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    question = st.chat_input("Ask your question...")

    if question:

        prompt = f"""
You are CareerPilot AI.

Resume:
{st.session_state.resume_text}

Job Description:
{st.session_state.job_description}

ATS Report:
{st.session_state.result}

Career Roadmap:
{st.session_state.roadmap}

Answer the user's question professionally.

Question:
{question}
"""

        answer = ask_ai(prompt)

        st.session_state.chat_history.append(("user", question))
        st.session_state.chat_history.append(("assistant", answer))

    for role, message in st.session_state.chat_history:

        with st.chat_message(role):
            st.markdown(message)