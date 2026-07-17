from rag.document_loader import load_job_descriptions
from rag.vector_store import VectorStore


class RAGEngine:

    def __init__(self):

        self.documents = load_job_descriptions()

        self.vector_db = VectorStore()

        self.vector_db.build(
            self.documents
        )

    def retrieve(self, job_role):

        result = self.vector_db.search(
            job_role,
            top_k=1
        )
        if result:
            return result[0]

        return None