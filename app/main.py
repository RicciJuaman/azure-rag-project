from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import rag_answer

app = FastAPI(title="Azure RAG API")

class AskRequest(BaseModel):
    question: str

@app.post("/ask")
def ask(payload: AskRequest):
    return rag_answer(payload.question)
