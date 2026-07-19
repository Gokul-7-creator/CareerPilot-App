import os
from dotenv import load_dotenv
from groq import Groq
from groq import RateLimitError

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------------------------------
# Generic AI Prompt
# ---------------------------------------

def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except RateLimitError as e:
        print("========== GROQ RATE LIMIT ==========")
        print(e)
        print("=====================================")
        raise


# ---------------------------------------
# Resume Analysis
# ---------------------------------------

def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an expert HR recruiter.

Analyze the following resume against the given job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return your answer in exactly this format:

ATS Score: <score out of 100>

Strengths:
- ...

Weaknesses:
- ...

Missing Skills:
- ...

Hiring Decision:
- Hire / Reject / Consider

Interview Questions:
1.
2.
3.
4.
5.

Do not ask the user any questions.
Do not say "It looks like you didn't type anything."
Analyze only the information provided.
"""

    print("========== PROMPT SENT TO GROQ ==========")
    print(prompt)
    print("=========================================")

    return ask_ai(prompt)

# ---------------------------------------
# Dynamic Job Description Generator
# ---------------------------------------

def generate_job_description(job_role, company):

    prompt = f"""
You are an experienced HR recruiter.

Generate a professional job description for the following position.

Job Role:
{job_role}

Company:
{company}

Include:

1. Job Summary
2. Responsibilities
3. Required Skills
4. Preferred Skills
5. Qualifications
6. ATS Keywords

Return only the job description.
"""

    return ask_ai(prompt)   
def validate_job_role(job_role):

    prompt = f"""
You are an HR expert.

Determine whether "{job_role}" is a real professional job role.

Rules:
- Reply ONLY "VALID" if it is a real job title.
- Reply ONLY "INVALID" if it is not a real job title.
- Do not explain anything.
"""

    response = ask_ai(prompt).strip().upper()

    return response == "VALID"