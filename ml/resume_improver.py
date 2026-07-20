from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
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
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content