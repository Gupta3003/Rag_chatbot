import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from backend.core.huggingface_client import HuggingFaceClient
import numpy as np

hf = HuggingFaceClient()

def get_embeddings(texts):
    vectors = hf.embeddings(texts)
    if not vectors:
        return []
    normalized = [np.array(v) / (np.linalg.norm(v) + 1e-9) for v in vectors]
    return [v.tolist() for v in normalized]
