from backend.core.intent_classifier import classify_intent

def test_intent_classify():
    assert classify_intent("NEC code") == "NEC"
    assert classify_intent("Wattmonk policy") == "WATTMONK"
    assert classify_intent("Tell me a joke") == "GENERAL"
