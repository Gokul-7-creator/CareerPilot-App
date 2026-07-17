from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def improve_resume(resume_text, job_description):

    prompt = f"""
You are an expert Resume Reviewer.

Candidate Resume:
{resume_text}

Job Description:
{job_description}

Suggest improvements under the following headings:

1. Missing Keywords
2. Skills to Learn
3. Projects to Add
4. Certifications to Pursue
5. Resume Formatting Tips
6. ATS Improvement Tips

Keep the answer short and practical.
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