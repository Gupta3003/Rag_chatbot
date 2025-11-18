# src/utils/api_client.py
import requests
import os

DEFAULT_BACKEND = os.environ.get("RAG_BACKEND_URL", "http://localhost:8000")

def chat_query(query, user_id="anonymous", top_k=5, use_memory=True, backend_url=None):
    backend = backend_url or DEFAULT_BACKEND
    url = f"{backend}/api/chat/query"
    payload = {"user_id": user_id, "query": query, "top_k": top_k, "use_memory": use_memory}
    resp = requests.post(url, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()

def text_generation(prompt, model=None, max_new_tokens=256, temperature=0.7, top_k=50, top_p=0.95, stop=None, backend_url=None):
    backend = backend_url or DEFAULT_BACKEND
    url = f"{backend}/api/text-generation/generate"
    payload = {
        "prompt": prompt,
        "max_new_tokens": max_new_tokens,
        "temperature": temperature,
        "top_k": top_k,
        "top_p": top_p,
        "stop": stop or None,
        "model": model
    }
    resp = requests.post(url, json=payload, timeout=120)
    resp.raise_for_status()
    return resp.json()

def image_analysis(file_bytes, filename="image.png", backend_url=None):
    backend = backend_url or DEFAULT_BACKEND
    url = f"{backend}/api/image-analysis/analyze"
    files = {"file": (filename, file_bytes, "application/octet-stream")}
    resp = requests.post(url, files=files, timeout=120)
    resp.raise_for_status()
    return resp.json()
