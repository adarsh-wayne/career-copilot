from langchain_ollama import ChatOllama


def generate_answer(context: str, question: str):

    llm = ChatOllama(model="llama3.1:8b")

    prompt = f"""
You are an AI career assistant.

Use the provided context to answer the question.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    response = llm.invoke(prompt)

    return response.content