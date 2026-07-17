import re

def skill_gap_analysis(candidate_skills, job_description):

    job_description = job_description.lower()

    required_skills = [
        "python",
        "java",
        "c++",
        "sql",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "scikit-learn",
        "docker",
        "kubernetes",
        "aws",
        "azure",
        "google cloud",
        "power bi",
        "tableau",
        "excel",
        "flask",
        "django",
        "git",
        "github",
        "linux"
    ]

    required = []

    for skill in required_skills:
        if skill in job_description:
            required.append(skill)

    candidate = [s.lower() for s in candidate_skills]

    matched = []
    missing = []

    for skill in required:

        if skill in candidate:
            matched.append(skill.title())

        else:
            missing.append(skill.title())

    return matched, missing