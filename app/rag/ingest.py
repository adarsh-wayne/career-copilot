from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    UnstructuredWordDocumentLoader,
    TextLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "data/chroma"
KNOWLEDGE_PATH = "knowledge_base"


def load_documents():
    loaders = [
        DirectoryLoader(
            KNOWLEDGE_PATH,
            glob="**/*.pdf",
            loader_cls=PyPDFLoader,
            show_progress=True,
        ),
        DirectoryLoader(
            KNOWLEDGE_PATH,
            glob="**/*.docx",
            loader_cls=UnstructuredWordDocumentLoader,
            show_progress=True,
        ),
        DirectoryLoader(
            KNOWLEDGE_PATH,
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
            show_progress=True,
        ),
        DirectoryLoader(
            KNOWLEDGE_PATH,
            glob="**/*.txt",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
            show_progress=True,
        ),
    ]

    docs = []
    for loader in loaders:
        try:
            docs.extend(loader.load())
        except Exception as e:
            print(f"Loader failed: {e}")

    return docs


def ingest_documents():
    docs = load_documents()

    if not docs:
        print("No documents found in knowledge_base.")
        return

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
    )

    chunks = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
    )

    vectorstore.persist()

    print(f"Ingested {len(chunks)} chunks into vector database.")