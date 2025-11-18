from backend.core.retrieval import retrieve
from backend.core.huggingface_client import HuggingFaceClient
from backend.config import settings

hf = HuggingFaceClient()

class RAGModel:
    def __init__(self):
        self.text_model = settings.HF_TEXT_MODEL
        self.embed_model = settings.HF_EMBEDDING_MODEL

    def answer_query(self, query, top_k=5, conversation_history=None):
        docs = retrieve(query, top_k=top_k)
        context = "\n\n".join(
            [f"[{i+1}] {d['metadata'].get('text','')}" for i, d in enumerate(docs)]
        )
        prompt = f"Use the context to answer:\n\n{context}\n\nUser: {query}\nAnswer:"
        result = hf.text_generation(prompt=prompt)
        scores = [d["score"] for d in docs] if docs else [0.5]
        return {
            "answer": result.get("generated_text", "No answer."),
            "sources": [d["metadata"].get("source", "N/A") for d in docs],
            "confidence": float(sum(scores) / len(scores)),
        }
