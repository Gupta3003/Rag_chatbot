from backend.core.vector_db import SimpleVectorDB
import numpy as np

def test_vector_db_add_search():
    db = SimpleVectorDB()
    v = np.array([1.0, 0.0])
    db.add(v, {"source": "doc1"})
    res = db.search(v)
    assert isinstance(res, list)
    assert len(res) > 0
