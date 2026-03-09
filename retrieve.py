from app.rag.retrieve import search_documents

if __name__ == "__main__":
    query = "What AWS and project management experience does Adarsh have?"
    results = search_documents(query)

    print("\nTop matching documents:\n")
    for i, doc in enumerate(results, start=1):
        print(f"Result {i}:")
        print(doc.page_content)
        print("-" * 50)