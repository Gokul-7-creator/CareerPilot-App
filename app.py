import re
import streamlit as st

# -------------------------------
# Utils
# -------------------------------

from services.company_validator import validate_company
from ui.download import render_download
from ui.cover_letter import render_cover_letter
from ui.career import render_career
from ui.interview import render_interview
from ui.overview import render_overview
from ui.dashboard import render_dashboard
from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.resume_parser import (
    extract_email,
    extract_phone,
    extract_links
)
from utils.pdf_report import generate_pdf
from ui.chatbot import render_chatbot
from ui.company_compare import render_company_compare

# -------------------------------
# RAG
# -------------------------------


from rag.gemini_client import (
    analyze_resume,
    generate_job_description,
    validate_job_role
)

# -------------------------------
# ML Modules
# -------------------------------

from ml.resume_match import calculate_match
from ml.skill_gap import skill_gap_analysis
from ml.interview_questions import generate_interview_questions
from ml.resume_improver import improve_resume
from ml.career_roadmap import generate_career_roadmap
from ml.mock_interview import evaluate_answer
from ml.cover_letter import generate_cover_letter

# -------------------------------------------------
# Page Config
# -------------------------------------------------

st.set_page_config(
    page_title="CareerPilot",
   
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>

/* Entire App */
.stApp{
    background: linear-gradient(135deg,#0B1220 0%, #111827 45%, #1E1B4B 100%);
    color:#F8FAFC;
}

/* Main container */


/* Sidebar */


/* Buttons */
.stButton>button{
    width:100%;
    border-radius:15px;
    height:55px;
    font-weight:bold;
    background:linear-gradient(90deg,#2563EB,#38BDF8);
    color:white;
}

/* Metric Cards */
div[data-testid="stMetric"]{
    background:#1E293B;
    border-radius:18px;
    padding:18px;
}

/* Upload Box */
section[data-testid="stFileUploader"]{
    border:2px dashed #38BDF8;
    border-radius:18px;
    padding:20px;
}

/* Animated Background */

.stApp::before{
content:"";
position:fixed;
top:-250px;
left:-250px;
width:600px;
height:600px;
background:#2563EB;
border-radius:50%;
filter:blur(180px);
opacity:.18;
animation:move1 14s infinite alternate;
z-index:-1;
}

.stApp::after{
content:"";
position:fixed;
bottom:-250px;
right:-250px;
width:700px;
height:700px;
background:#7C3AED;
border-radius:50%;
filter:blur(220px);
opacity:.18;
animation:move2 16s infinite alternate;
z-index:-1;
}

@keyframes move1{
0%{transform:translate(0,0);}
100%{transform:translate(250px,180px);}
}

@keyframes move2{
0%{transform:translate(0,0);}
100%{transform:translate(-220px,-180px);}
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Sidebar */


/* Hide collapse button */


/* Main page */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}
</style>
""", unsafe_allow_html=True)





   

# -------------------------------------------------
# Session State
# -------------------------------------------------

defaults = {

    "analysis_done": False,

    "resume_text": "",

    "email": "",
    "phone": "",
    "github": "",
    "linkedin": "",

    "skills": [],

    "job_description": "",

    "match_score": 0,

    "matched_skills": [],
    "missing_skills": [],

    "result": "",

    "questions": "",

    "improvements": "",

    "roadmap": "",

    "cover_letter": "",

    "ats_score": 0,
    "current_page": "home"
}

for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

with st.sidebar:

    st.markdown("""
    <div style="text-align:center;padding:10px 0;">
        <h2 style="
            color:#38BDF8;
            font-size:28px;
            font-weight:800;
            margin:0;
        ">
            🚀 CareerPilot
        </h2>
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://img.icons8.com/fluency/240/artificial-intelligence.png",
        use_container_width=True
    )

    st.markdown("---")

    st.markdown("### ⚡ Features")

    features = [
        "📄 Resume Parser",
        "🎯 ATS Score",
        "🤖 AI Recruiter",
        "🛠 Skill Gap",
        "🎤 Mock Interview",
        "📈 Career Roadmap",
        "📝 Cover Letter",
        "🏢 Company Compare",
        "💬 AI Assistant",
        "📥 PDF Report"
    ]

    for feature in features:
        st.markdown(f"✅ {feature}")

    st.markdown("---")

    st.success("Developed by\n\n**Gokul S**")

# -------------------------------------------------
# Main Screen
# -------------------------------------------------
st.divider()

st.markdown("""
<div style="
text-align:center;
padding:45px 20px;
">

<h1 style="
font-size:72px;
font-weight:800;
margin-bottom:8px;
background:linear-gradient(90deg,#38BDF8,#2563EB,#7C3AED);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
letter-spacing:1px;
">
🚀 CareerPilot
</h1>

<h3 style="
color:#E2E8F0;
font-weight:500;
margin-top:5px;
font-size:28px;
">
Navigate Your Career with AI
</h3>

<p style="
font-size:20px;
color:#94A3B8;
margin-top:18px;
">

Analyze Resume • Improve ATS • AI Recruiter • Mock Interview • Career Roadmap

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")


if st.session_state.current_page == "home":

    st.markdown("## 📄 Upload Resume")

    uploaded_resume = st.file_uploader(
        "Choose your Resume (PDF)",
        type=["pdf"]
    )

    job_role = st.text_input(
        "🎯 Target Job Role",
        placeholder="Example: AI Engineer, DevOps Engineer, Cyber Security Analyst"
    )
    st.session_state.selected_role = job_role

    company = st.text_input(
        "🏢 Company Name",
        placeholder="e.g. Google, Microsoft, TCS"
    )

    analyze = st.button(
        "🚀 Analyze Resume",
        use_container_width=True
    )
# -------------------------------------------------
# Analyze Resume
# -------------------------------------------------

if st.session_state.current_page == "home" and analyze:

    if uploaded_resume is None:
        st.warning("Please upload your resume first.")
        st.stop()
    if not company.strip():
        st.warning("Please enter a company name.")
        st.stop()

    with st.spinner("🔍 Validating company..."):
        if not validate_job_role(job_role):
            st.error("❌ Invalid Job Role.")
            st.stop()
        if not validate_company(company):
            st.error("❌ Invalid company name.")
            st.stop()
        job_description = generate_job_description(
            job_role,
            company
        )

    # Read Resume
    with st.spinner("📄 Reading Resume... Please wait..."):

        resume_text = extract_text_from_pdf(uploaded_resume)
       
    # Parse Resume
    email = extract_email(resume_text)
    phone = extract_phone(resume_text)
    github, linkedin = extract_links(resume_text)
    skills = extract_skills(resume_text)

    # Retrieve Job Description
    
    job_description = generate_job_description(
        job_role,
        company
    )
  
    match_score = calculate_match(
        resume_text,
        job_description
    )

    # Skill Gap
    matched_skills, missing_skills = skill_gap_analysis(
        skills,
        job_description
    )

    # AI Recruiter Report
    with st.spinner("🤖 AI is analyzing your resume..."):

        result = analyze_resume(
            resume_text,
            job_description
        )

       
    # ATS Score
    ats_match = re.search(
        r"ATS Score[:\s]*([0-9]+)",
        result
    )

    ats_score = 0

    if ats_match:
        ats_score = int(ats_match.group(1))

    # Interview Questions
    questions = generate_interview_questions(
        resume_text,
        job_description
    )

    # Resume Improvement
    improvements = improve_resume(
        resume_text,
        job_description
    )

    # Career Roadmap
    roadmap = generate_career_roadmap(
        resume_text,
        job_role
    )
    # Cover Letter
    cover_letter = generate_cover_letter(
        resume_text,
        job_role,
        company
    )

    # Save everything in Session State

    st.session_state.analysis_done = True

    st.session_state.resume_text = resume_text

    st.session_state.email = email
    st.session_state.phone = phone
    st.session_state.github = github
    st.session_state.linkedin = linkedin

    st.session_state.skills = skills

    st.session_state.job_description = job_description

    st.session_state.match_score = match_score

    st.session_state.matched_skills = matched_skills
    st.session_state.missing_skills = missing_skills

    st.session_state.result = result

    st.session_state.questions = questions

    st.session_state.improvements = improvements

    st.session_state.roadmap = roadmap
    st.session_state.cover_letter = cover_letter

    st.session_state.ats_score = ats_score

    st.success("✅ Resume analyzed successfully!")
    # -------------------------------------------------
# Show Results
# -------------------------------------------------

if st.session_state.analysis_done:
    render_dashboard()

    st.divider()
   
   
    st.markdown(f"""
    <div style="
    background:#1E293B;
    padding:20px;
    border-radius:15px;
    border-left:6px solid #10B981;
    margin-bottom:20px;
    ">

    <h3>👋 Welcome!</h3>

    Your resume has been successfully analyzed for the
    <b>{job_role}</b> role.

    <br><br>

    Explore the tabs below to view:

    ✅ Resume Analysis

    ✅ Mock Interview

    ✅ Career Roadmap

    ✅ AI Cover Letter

    ✅ PDF Report

    </div>
    """, unsafe_allow_html=True)
    page = st.segmented_control(
        "Navigation",
        [
            "📄 Overview",
            "🎤 Interview",
            "🚀 Career",
            "📝 Cover Letter",
            "🏢 Company Compare",
            "💬 AI Assistant",
            "📥 Download"
        ]
        )
    if page == "📄 Overview":
        render_overview()

    elif page == "🎤 Interview":
        render_interview()

    elif page == "🚀 Career":
        render_career()

    elif page == "📝 Cover Letter":
        render_cover_letter(job_role)
    elif page == "🏢 Company Compare":
        render_company_compare()
    elif page == "💬 AI Assistant":
        render_chatbot()

    elif page == "📥 Download":
        render_download()
    st.divider()

    st.markdown("""
    <div style="text-align:center;color:#94A3B8;">


    <b>Streamlit • Groq AI • RAG • Python</b>

    <br><br>

    © 2026 Gokul S

    </div>
    """, unsafe_allow_html=True)