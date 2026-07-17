import re
import streamlit as st
from ml.mock_interview import evaluate_answer
from ml.career_roadmap import generate_career_roadmap
from ml.resume_improver import improve_resume
from ml.interview_questions import generate_interview_questions
from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.resume_parser import (
    extract_email,
    extract_phone,
    extract_links
)

from rag.rag_engine import RAGEngine
from rag.gemini_client import analyze_resume

from ml.resume_match import calculate_match
from ml.skill_gap import skill_gap_analysis

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="AI Recruiter Simulation",
    page_icon="🤖",
    layout="wide"
)
# -----------------------------------
# Session State
# -----------------------------------

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "job_description" not in st.session_state:
    st.session_state.job_description = ""

if "skills" not in st.session_state:
    st.session_state.skills = []

if "result" not in st.session_state:
    st.session_state.result = ""

if "email" not in st.session_state:
    st.session_state.email = ""

if "phone" not in st.session_state:
    st.session_state.phone = ""

if "github" not in st.session_state:
    st.session_state.github = ""

if "linkedin" not in st.session_state:
    st.session_state.linkedin = ""

if "match_score" not in st.session_state:
    st.session_state.match_score = 0

if "matched_skills" not in st.session_state:
    st.session_state.matched_skills = []

if "missing_skills" not in st.session_state:
    st.session_state.missing_skills = []

if "questions" not in st.session_state:
    st.session_state.questions = ""

if "improvements" not in st.session_state:
    st.session_state.improvements = ""

if "roadmap" not in st.session_state:
    st.session_state.roadmap = ""

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("🤖 AI Recruiter")

st.sidebar.markdown("""
### Features

- 📄 Resume Upload
- 📑 Resume Parsing
- 🛠 Skill Extraction
- 🎯 Resume Match
- 📚 RAG
- 🤖 AI Recruiter
- 📊 ATS Score
- 📈 Skill Gap Analysis
- 💬 AI Interview (Coming Soon)
""")

# -----------------------------------
# Main Page
# -----------------------------------

st.title("🤖 AI Recruiter Simulation")

st.write("Upload your resume and let AI evaluate it like a professional recruiter.")

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_role = st.selectbox(
    "Select Job Role",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Software Engineer",
        "Data Analyst"
    ]
)

# -----------------------------------
# Analyze Resume
# -----------------------------------

if st.button("Analyze Resume"):
    st.session_state.analysis_done=True
    if uploaded_resume is None:
        st.warning("Please upload a resume first.")

    else:

        with st.spinner("📄 Reading Resume..."):
            resume_text = extract_text_from_pdf(uploaded_resume)
            st.session_state.resume_text=resume_text

            email = extract_email(resume_text)
            phone = extract_phone(resume_text)
            github, linkedin = extract_links(resume_text)
            skills = extract_skills(resume_text)

        st.success("✅ Resume Parsed Successfully")

        # -----------------------------------
        # Resume Text
        # -----------------------------------

        st.subheader("📄 Resume")

        st.text_area(
            "Resume Text",
            resume_text,
            height=300
        )

        # -----------------------------------
        # Candidate Information
        # -----------------------------------

        st.subheader("👤 Candidate Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write("📧 Email")
            st.info(email if email else "Not Found")

            st.write("💻 GitHub")
            st.info(github if github else "Not Found")

        with col2:
            st.write("📱 Phone")
            st.info(phone if phone else "Not Found")

            st.write("🔗 LinkedIn")
            st.info(linkedin if linkedin else "Not Found")

        # -----------------------------------
        # Extracted Skills
        # -----------------------------------

        st.subheader("🛠 Extracted Skills")

        if skills:
            cols = st.columns(3)

            for i, skill in enumerate(skills):
                cols[i % 3].success(skill)

        else:
            st.warning("No skills detected.")

        # -----------------------------------
        # Retrieve Job Description
        # -----------------------------------

        rag = RAGEngine()

        job_description = rag.retrieve(job_role)

        # -----------------------------------
        # Resume Match
        # -----------------------------------

        match_score = calculate_match(
            resume_text,
            job_description
        )

        st.subheader("🎯 Resume Match")

        st.metric(
            "Resume Match %",
            f"{match_score}%"
        )

        st.progress(float(match_score) / 100)

        # -----------------------------------
        # Skill Gap Analysis
        # -----------------------------------

        matched_skills, missing_skills = skill_gap_analysis(
            skills,
            job_description
        )

        st.subheader("📈 Skill Gap Analysis")

        col1, col2 = st.columns(2)

        with col1:

            st.success("✅ Matching Skills")

            if matched_skills:

                for skill in matched_skills:
                    st.write(f"✅ {skill}")

            else:
                st.write("No matching skills found.")

        with col2:

            st.error("❌ Missing Skills")

            if missing_skills:

                for skill in missing_skills:
                    st.write(f"❌ {skill}")

            else:
                st.write("No missing skills.")

        # -----------------------------------
        # Job Description
        # -----------------------------------

        st.subheader("📚 Retrieved Job Description")

        st.info(job_description)

        # -----------------------------------
        # AI Analysis
        # -----------------------------------

        with st.spinner("🤖 AI Recruiter is analyzing your resume..."):

            result = analyze_resume(
                resume_text,
                job_description
            )

        # -----------------------------------
        # ATS Score
        # -----------------------------------

        st.subheader("📊 ATS Score")

        ats_match = re.search(
            r"ATS Score[:\s]*([0-9]+)",
            result
        )

        if ats_match:

            ats_score = int(ats_match.group(1))

            st.metric(
                "Overall ATS Score",
                f"{ats_score}/100"
            )

            st.progress(ats_score / 100)

        else:

            st.warning("ATS Score not found in AI response.")

        # -----------------------------------
        # AI Recruiter Report
        # -----------------------------------

        st.subheader("🤖 AI Recruiter Report")

        st.markdown(result)
        st.divider()

        st.subheader("🎤 AI Interview Questions")

        questions = generate_interview_questions(
            resume_text,
            job_description
)

        st.markdown(questions)
        st.divider()
        st.subheader("🎤 AI Mock Interview")
        question = st.text_input(
            "Interview Question",
            placeholder="Paste one generated interview question here"
        )
        answer = st.text_area(
            "Your Answer",
             height=200
        )
        if st.button("Evaluate Answer"):
            if question and answer:
                with st.spinner("Evaluating your answer..."):
                    feedback = evaluate_answer(
                        question,
                        answer
                    )
                st.markdown(feedback)
            else:
                st.warning("Please enter both the question and your answer.")
   
        st.divider()

        st.subheader("🚀 Resume Improvement Suggestions")

        with st.spinner("Finding improvements..."):
            improvements = improve_resume(
                resume_text,
                job_description
    )

        st.markdown(improvements)
        st.divider()

        st.subheader("🛣️ Personalized Career Roadmap")

        with st.spinner("Generating your career roadmap..."):
            roadmap = generate_career_roadmap(
                resume_text,
                job_role
    )

        st.markdown(roadmap)