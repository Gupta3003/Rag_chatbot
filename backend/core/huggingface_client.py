from huggingface_hub import InferenceClient
from backend.config import settings
import logging

log = logging.getLogger("huggingface_client")

class HuggingFaceClient:
    """Unified Hugging Face API client"""

    def __init__(self):
        self.client = InferenceClient(token=settings.HF_API_TOKEN)

    def text_generation(self, prompt, model=None, **kwargs):
        model = model or settings.HF_TEXT_MODEL
        if not model:
            raise ValueError("No HF_TEXT_MODEL configured.")
        result = self.client.text_generation(
            model=model,
            prompt=prompt,
            max_new_tokens=kwargs.get("max_new_tokens", 256),
            temperature=kwargs.get("temperature", 0.7),
            top_k=kwargs.get("top_k", 50),
            top_p=kwargs.get("top_p", 0.95),
            stop_sequences=kwargs.get("stop", []),
        )
        if isinstance(result, dict):
            return result
        return {"generated_text": str(result)}

    def embeddings(self, texts, model=None):
        model = model or settings.HF_EMBEDDING_MODEL
        if not model:
            raise ValueError("No HF_EMBEDDING_MODEL configured.")
        return self.client.feature_extraction(model=model, inputs=texts)

    def image_analysis(self, image_bytes, model=None):
        model = model or settings.HF_IMAGE_MODEL
        if not model:
            raise ValueError("No HF_IMAGE_MODEL configured.")
        result = self.client.image_to_text(model=model, image=image_bytes)
        if isinstance(result, list) and len(result) > 0:
            result = result[0]
        return {"text": result.get("generated_text", ""), "raw": result}
