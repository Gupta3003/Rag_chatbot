def classify_intent(query: str) -> str:
    query = query.lower()
    if "nec" in query or "electrical code" in query:
        return "NEC"
    elif "wattmonk" in query or "company policy" in query:
        return "WATTMONK"
    return "GENERAL"
