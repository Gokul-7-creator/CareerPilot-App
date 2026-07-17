from rag.gemini_client import ask_ai


def generate_cover_letter(resume_text, job_role, company):

    prompt = f"""
You are an expert HR professional.

Candidate Resume:
{resume_text}

Target Job Role:
{job_role}

Company:
{company}

Write a professional cover letter.

Requirements:

- Address the hiring manager.
- Mention why the candidate is suitable.
- Mention relevant skills.
- Mention enthusiasm.
- End professionally.

Return ONLY the cover letter.
"""

    return ask_ai(prompt)