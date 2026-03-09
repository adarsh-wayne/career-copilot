from app.services.jd_analyzer import analyze_job_description
from app.services.match_engine import analyze_match
from app.rag.retrieve import search_documents


if __name__ == "__main__":

    jd = """
We are looking for a Senior Data Engineer with experience in AWS,
Python, ETL pipelines, and distributed data processing.

The candidate should have 5+ years experience building scalable
data platforms and managing cloud infrastructure.
"""

    # Step 1: analyze JD
    jd_analysis = analyze_job_description(jd)

    print("\nJD Analysis:\n")
    print(jd_analysis)

    # Step 2: retrieve profile context
    docs = search_documents(jd)

    context = "\n\n".join([doc.page_content for doc in docs])

    # Step 3: compare JD vs profile
    result = analyze_match(jd_analysis, context)

    print("\nMatch Analysis:\n")
    print(result)