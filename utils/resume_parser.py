import re

def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"


def extract_phone(text):
    pattern = r"(\+?\d[\d\s\-]{8,15}\d)"
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"


def extract_links(text):
    github = "Not Found"
    linkedin = "Not Found"

    for word in text.split():
        lower = word.lower()

        if "github.com" in lower:
            github = word

        if "linkedin.com" in lower:
            linkedin = word

    return github, linkedin