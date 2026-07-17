SKILLS = [
    "Python", "Java", "C++", "C", "SQL", "MySQL",
    "Machine Learning", "Deep Learning", "Artificial Intelligence",
    "TensorFlow", "PyTorch", "Scikit-learn",
    "Pandas", "NumPy", "Power BI", "Excel",
    "AWS", "Azure", "Docker", "Kubernetes",
    "Git", "HTML", "CSS", "JavaScript",
    "React", "Node.js", "Flask", "Django"
]

def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(found_skills)