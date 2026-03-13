def build_rag_prompt(question: str, context_docs: list) -> str:
    context_text = "\n\n".join([doc.page_content for doc in context_docs])

    prompt = f"""
You are a helpful knowledge assistant.

Answer the user's question only using the provided context.
If the answer is not in the context, say:
"I could not find that information in the provided documents."

Context:
{context_text}

Question:
{question}

Provide:
1. A clear answer
2. A short supporting explanation
3. Mention that the answer is based on the uploaded documents
"""
    return prompt