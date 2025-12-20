from pathlib import Path
from dotenv import load_dotenv

# Force-load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from fastapi import FastAPI
from app.rag import rag_answer

app = FastAPI(title="Azure RAG API")

@app.post("/ask")
def ask(payload: dict):
    return rag_answer(payload["question"])
