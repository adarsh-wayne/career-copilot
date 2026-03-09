from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
import re

CHROMA_PATH = "data/chroma"

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings,
)


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def get_source_priority(source: str) -> int:
    source = source.lower()

    if "knowledge_base/projects/" in source:
        return 1
    elif "knowledge_base/ai_projects/" in source:
        return 2
    elif "knowledge_base/resume/" in source:
        return 3
    elif "knowledge_base/experience/" in source:
        return 4
    else:
        return 5


def search_documents(query: str, k: int = 8):
    docs = vectorstore.similarity_search(query, k=k)

    # sort by folder priority
    docs = sorted(
        docs,
        key=lambda d: get_source_priority(d.metadata.get("source", ""))
    )

    # remove near-duplicates
    unique_docs = []
    seen = set()

    for doc in docs:
        cleaned = clean_text(doc.page_content[:200])

        if cleaned not in seen:
            seen.add(cleaned)
            doc.page_content = clean_text(doc.page_content)
            unique_docs.append(doc)

    return unique_docs[:5]