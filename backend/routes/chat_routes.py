from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from backend.core.rag_model import RAGModel
from backend.memory.conversation_memory import ConversationMemory

router = APIRouter()
rag = RAGModel()
memory = ConversationMemory()

class ChatRequest(BaseModel):
    user_id: Optional[str] = "anonymous"
    query: str
    top_k: int = 5
    use_memory: bool = True

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]
    confidence: float

@router.post("/query", response_model=ChatResponse)
def chat_query(payload: ChatRequest):
    try:
        history = memory.get_history(payload.user_id) if payload.use_memory else []
        response = rag.answer_query(
            query=payload.query, top_k=payload.top_k, conversation_history=history
        )
        memory.append(payload.user_id, {"user": payload.query, "bot": response["answer"]})
        return ChatResponse(**response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
