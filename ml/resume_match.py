from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_match(resume_text, job_description):
    resume_embedding = model.encode([resume_text])
    jd_embedding = model.encode([job_description])

    similarity = cosine_similarity(
        resume_embedding,
        jd_embedding
    )[0][0]

    return float(round(similarity * 100, 2))