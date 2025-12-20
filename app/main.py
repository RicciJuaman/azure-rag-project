from fastapi import FastAPI
from app.rag import rag_answer

app = FastAPI(title="Azure RAG API")

@app.post("/ask")
def ask(payload: dict):
    question = payload.get("question")
    return rag_answer(question)
