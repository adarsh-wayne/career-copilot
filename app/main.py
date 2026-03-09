from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from app.rag.ingest import ingest_documents
from app.services.jd_analyzer import analyze_job_description
from app.services.match_engine import analyze_match
from app.rag.retrieve import search_documents

app = FastAPI(title="AI Career Copilot")


class JDRequest(BaseModel):
    job_description: str


@app.get("/")
def root():
    return {"message": "AI Career Copilot API running"}


@app.post("/analyze_jd")
def analyze_jd(request: JDRequest):

    jd_text = request.job_description

    # Step 1 — analyze job description
    jd_analysis = analyze_job_description(jd_text)

    # Step 2 — retrieve profile data
    docs = search_documents(jd_text)

    context = "\n\n".join([doc.page_content for doc in docs])

    # Step 3 — compare JD with profile
    match_result = analyze_match(jd_analysis, context)

    return {
        "jd_analysis": jd_analysis,
        "match_analysis": match_result
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    upload_folder = "knowledge_base/uploads"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run ingestion so the new document is indexed
    ingest_documents()

    return {"message": "File uploaded and ingested successfully"}