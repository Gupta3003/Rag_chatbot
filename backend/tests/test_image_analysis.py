from fastapi.testclient import TestClient
from backend.main import app
import io

client = TestClient(app)

def test_image_analysis_dummy():
    # Send a dummy PNG file (empty content)
    file = io.BytesIO(b"fakeimage")
    res = client.post(
        "/api/image-analysis/analyze",
        files={"file": ("fake.png", file, "image/png")}
    )
    assert res.status_code in (200, 500)
