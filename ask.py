from app.rag.retrieve import search_documents
from app.services.llm_service import generate_answer

if __name__ == "__main__":

    question = "What AI experience does Adarsh have?"

    docs = search_documents(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    answer = generate_answer(context, question)

    print("\nAI Answer:\n")
    print(answer)