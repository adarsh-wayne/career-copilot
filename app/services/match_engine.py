from langchain_ollama import ChatOllama
import json


def analyze_match(jd_analysis: str, profile_context: str):

    llm = ChatOllama(
        model="llama3.1:8b",
        temperature=0
    )

    prompt = f"""
You are an expert AI career analyst helping **Adarsh** evaluate job opportunities.

IMPORTANT RULES
- Refer to the candidate as **Adarsh** or **you**
- Never say "the candidate"
- Only use information from the provided profile context
- Do NOT invent experience
- Always reference project names when possible (Hardy Manufacturing, TrueBlue, BizInsightAI, Log1, etc.)

--------------------------------

JOB DESCRIPTION

{jd_analysis}

--------------------------------

ADARSH'S EXPERIENCE

{profile_context}

--------------------------------

Return ONLY valid JSON in this format:

{{
 "match_score": number between 0 and 100,

 "strong_matches": [
  "bullet points describing strongest relevant skills"
 ],

 "partial_matches": [
  "skills that exist but are not emphasized strongly"
 ],

 "missing_skills": [
  "skills required in JD but not clearly visible in experience"
 ],

 "project_evidence": [
  "ProjectName — explanation of why it is relevant"
 ],

 "positioning_advice": "short paragraph explaining how Adarsh should position himself in interviews"
}}

Do not add explanations outside JSON.
"""

    response = llm.invoke(prompt)

    text = response.content

    try:
        data = json.loads(text)

        score = data.get("match_score", 0)

        # Normalize score if model returns 0–10 scale
        if score <= 10:
            score = score * 10

        if score > 100:
            score = 100

        data["match_score"] = int(score)

        return data

    except Exception:

        return {
            "match_score": 0,
            "strong_matches": [],
            "partial_matches": [],
            "missing_skills": [],
            "project_evidence": [],
            "positioning_advice": text
        }