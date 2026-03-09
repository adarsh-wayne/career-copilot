from langchain_ollama import ChatOllama


def analyze_job_description(jd_text: str):

    llm = ChatOllama(model="llama3.1:8b")

    prompt = f"""
You are an AI job description analyzer.

Extract the following from the job description:

1. Role title
2. Required skills
3. Tools / technologies
4. Years of experience
5. Key responsibilities

Return the result in structured bullet points.

Job Description:
{jd_text}
"""

    response = llm.invoke(prompt)

    return response.content