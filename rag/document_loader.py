from pathlib import Path


def load_job_descriptions():
    """
    Loads all job description text files from data/job_descriptions
    """

    job_descriptions = {}

    folder = Path("data/job_descriptions")

    for file in folder.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            job_descriptions[file.stem] = f.read()

    return job_descriptions