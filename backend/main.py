from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from backend.routes.chat_routes import router as chat_router
from backend.routes.text_generation_routes import router as textgen_router
from backend.routes.image_analysis_routes import router as image_router
from backend.routes.healthcheck import router as health_router
from backend.config import settings

app = FastAPI(title="RAG Chatbot Backend", version="1.0")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(health_router, prefix="/api/health", tags=["Health"])
app.include_router(chat_router, prefix="/api/chat", tags=["Chat"])
app.include_router(textgen_router, prefix="/api/text-generation", tags=["Text Generation"])
app.include_router(image_router, prefix="/api/image-analysis", tags=["Image Analysis"])

@app.get("/")
def root():
    return {"message": "RAG Chatbot Backend running successfully"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=settings.PORT, reload=True)
