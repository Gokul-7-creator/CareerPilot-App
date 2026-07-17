from rag.gemini_client import analyze_resume


def generate_interview_questions(resume_text, job_description):
    result = analyze_resume(resume_text, job_description)

    if "Interview Questions" in result:
        return result.split("Interview Questions")[-1]

    return result