## High-Level Pipeline

1. Resume and project documents are collected.
2. Documents are loaded and converted into text.
3. Text is split into smaller chunks.
4. Each chunk is embedded using **nomic-embed-text**.
5. Embeddings are stored in the **Chroma vector database**.
6. A user submits a job description through the UI.
7. **FastAPI** receives the request.
8. The retriever searches Chroma for the most relevant experience chunks.
9. Retrieved chunks are combined into a profile context.
10. **Llama 3.1** analyzes the job description against the retrieved context.
11. The backend generates structured output including:
   - match score
   - strong matches
   - partial matches
   - missing skills
   - project evidence
   - positioning advice
12. **Streamlit** renders the results in the UI.

---

## Key Features in V1

- Job description analysis
- Semantic retrieval over a project knowledge base
- Local RAG pipeline
- Structured JSON output
- Match score visualization
- Evidence-based project matching
- Document ingestion pipeline for new knowledge

---

## Challenges Faced

### 1. Retrieval Quality

Initial retrieval returned generic resume chunks instead of project-specific context.

**Solution**

- Restructured the knowledge base
- Improved chunking strategy
- Added retrieval prioritization so project documentation is preferred over generic resume content

---

### 2. LLM Output Instability

Free-text model responses were inconsistent and difficult to render in the UI.

**Solution**

- Enforced structured JSON responses
- Added score normalization logic inside the FastAPI match engine
- Improved prompt structure to stabilize model outputs

---

## What I Learned

- How a practical RAG pipeline works end to end
- Why chunking strategy and retrieval quality are critical
- How structured LLM outputs simplify UI rendering
- How FastAPI, LangChain, Chroma, and Ollama integrate into a working AI system

---

## Current State

V1 is a functional prototype that includes:

- Local backend
- Local vector database
- Local LLM inference
- Streamlit UI
- GitHub version control

---

## V2 Roadmap

Planned improvements include:

- React frontend
- Improved visual design
- AWS deployment
- Personal domain
- Metadata filtering and reranking for better retrieval
- Improved document management workflows

---

## How to Run Locally

1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate

2. Install dependencies
pip install -r requirements.txt
3. Start Ollama

Make sure Ollama is installed and required models are available.
ollama pull llama3.1:8b
ollama pull nomic-embed-text
ollama serve
4. Ingest documents
python ingest.py
5. Start FastAPI backend
uvicorn app.main:app --reload
6. Start Streamlit UI
streamlit run ui.py
Future Improvements

This repository contains the V1 prototype. Future iterations will focus on improving user experience, building a React frontend, and deploying the system to AWS with a personal domain.


After replacing it, run:

```bash
git add README.md
git commit -m "Improved README formatting and documentation"
git push