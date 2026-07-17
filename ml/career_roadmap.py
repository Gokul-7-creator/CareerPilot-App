import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_career_roadmap(resume_text, job_role):

    prompt = f"""
You are an AI Career Mentor.

Candidate Resume:
{resume_text}

Target Role:
{job_role}

Generate a detailed 6-month learning roadmap.

Include:

1. Skills to Learn
2. Technologies
3. Projects
4. Certifications
5. Interview Preparation
6. Final Goal

Use proper headings and bullet points.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content