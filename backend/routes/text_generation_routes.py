from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from backend.core.huggingface_client import HuggingFaceClient

router = APIRouter()
hf = HuggingFaceClient()

class TextGenRequest(BaseModel):
    prompt: str
    max_new_tokens: Optional[int] = 256
    temperature: Optional[float] = 0.7
    top_k: Optional[int] = 50
    top_p: Optional[float] = 0.95
    stop: Optional[list] = None
    model: Optional[str] = None

class TextGenResponse(BaseModel):
    generated_text: str
    raw: Dict[str, Any]

@router.post("/generate", response_model=TextGenResponse)
def generate_text(req: TextGenRequest):
    try:
        result = hf.text_generation(
            prompt=req.prompt,
            model=req.model,
            max_new_tokens=req.max_new_tokens,
            temperature=req.temperature,
            top_k=req.top_k,
            top_p=req.top_p,
            stop=req.stop
        )
        return TextGenResponse(generated_text=result.get("generated_text", ""), raw=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
