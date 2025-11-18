from PyPDF2 import PdfReader
import os

def load_pdfs(folder):
    docs = []
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder, file))
            text = "".join(page.extract_text() for page in reader.pages if page.extract_text())
            docs.append({"source": file, "text": text})
    return docs
