SYSTEM_PROMPT = """
You are an AI assistant that answers questions using ONLY the provided context.
If the answer cannot be found in the context, say:
"I don’t have enough information to answer that."

Do not use external knowledge.
Be concise, factual, and clear.
"""

def build_user_prompt(context_chunks, question):
    context_text = "\n\n".join(
        f"[{c['id']}] Source: {c['source']}\n{c['content']}"
        for c in context_chunks
    )

    return f"""
Context:
--------
{context_text}

--------
Question:
{question}

Instructions:
- Answer using ONLY the context above
- Cite sources by their number (e.g. [1], [3])
"""
