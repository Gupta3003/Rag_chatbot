from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
from backend.core.huggingface_client import HuggingFaceClient

router = APIRouter()
hf = HuggingFaceClient()

class ImageAnalysisResponse(BaseModel):
    text: str
    raw: Dict[str, Any]

@router.post("/analyze", response_model=ImageAnalysisResponse)
async def analyze_image(file: UploadFile = File(...)):
    try:
        img = await file.read()
        result = hf.image_analysis(image_bytes=img)
        return ImageAnalysisResponse(text=result.get("text", ""), raw=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
