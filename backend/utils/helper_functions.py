import hashlib

def text_to_id(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()
