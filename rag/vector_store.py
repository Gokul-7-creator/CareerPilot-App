from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.index = None
        self.documents = []

    def build(self, documents):

        self.documents = list(documents.values())

        embeddings = self.model.encode(
            self.documents,
            convert_to_numpy=True
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            np.array(embeddings).astype("float32")
        )

    def search(self, query, top_k=1):

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        distances, indices = self.index.search(
            query_embedding.astype("float32"),
            top_k
        )

        return [
            self.documents[i]
            for i in indices[0]
        ]