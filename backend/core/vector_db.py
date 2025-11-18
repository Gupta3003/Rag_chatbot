import numpy as np
import os
from backend.config import settings

class SimpleVectorDB:
    def __init__(self, path=None):
        self.path = path or settings.VECTOR_PATH
        self.vectors = []
        self.metadata = []

    def add(self, vector, meta):
        self.vectors.append(np.array(vector))
        self.metadata.append(meta)

    def search(self, query_vector, top_k=5):
        if not self.vectors:
            return []
        vectors = np.vstack(self.vectors)
        sims = np.dot(vectors, query_vector) / (
            np.linalg.norm(vectors, axis=1) * np.linalg.norm(query_vector) + 1e-12
        )
        idx = np.argsort(-sims)[:top_k]
        return [
            {"score": float(sims[i]), "metadata": self.metadata[i]} for i in idx
        ]
