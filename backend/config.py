# backend/config.py
"""
Configuration for RAG Chatbot Backend
-------------------------------------
Loads all environment variables securely from `.env` file using Pydantic.
DO NOT hardcode API keys here.
"""

# backend/config.py
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Server
    PORT: int = 8000
    DEBUG: bool = True

    # Hugging Face API
    HF_API_TOKEN: str  # Loaded from .env (do not paste key here)
    HF_TEXT_MODEL: str = "mistralai/Mistral-7B-Instruct-v0.2:featherless-ai"  # lightweight CPU model
    HF_EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    HF_IMAGE_MODEL: str = "Salesforce/blip-image-captioning-base"

    # Vector store path
    VECTOR_PATH: str = "database/chroma_store/vector_store.npz"

    # CORS configuration
    CORS_ORIGINS: List[str] = ["http://localhost:8501", "http://localhost:3000"]

    # Logging
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"  # automatically loads variables from .env file


settings = Settings()
