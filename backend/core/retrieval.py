from backend.core.vector_db import SimpleVectorDB
from backend.core.embeddings import get_embeddings

vector_db = SimpleVectorDB()

def retrieve(query, top_k=5):
    query_vec = get_embeddings([query])[0]
    return vector_db.search(query_vec, top_k=top_k)
