from app.services.jd_analyzer import analyze_job_description


if __name__ == "__main__":

    jd = """
We are looking for a Senior Data Engineer with experience in AWS,
Python, ETL pipelines, and distributed data processing.

The candidate should have 5+ years experience building scalable
data platforms and managing cloud infrastructure.

Responsibilities include designing ETL pipelines,
maintaining data lakes, and collaborating with engineering teams.
"""

    result = analyze_job_description(jd)

    print("\nJD Analysis:\n")
    print(result)