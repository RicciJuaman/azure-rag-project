from app.search import retrieve_top_k
from app.prompts import SYSTEM_PROMPT, build_user_prompt
from app.openai_client import generate_answer

def rag_answer(question: str):
    docs = retrieve_top_k(question, k=10)

    user_prompt = build_user_prompt(docs, question)
    answer = generate_answer(SYSTEM_PROMPT, user_prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": docs
    }
