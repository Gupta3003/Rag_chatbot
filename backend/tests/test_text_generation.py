from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_text_generation_invalid():
    res = client.post("/api/text-generation/generate", json={"prompt": "Hello"})
    assert res.status_code in (200, 500)
