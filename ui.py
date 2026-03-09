import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze_jd"

st.set_page_config(page_title="Adarsh Career Copilot", layout="wide")

st.title("Adarsh Career Copilot")
st.write("AI-powered job match analysis for Adarsh's experience.")

jd = st.text_area("Paste Job Description")

if st.button("Analyze Job Fit"):

    with st.spinner("Analyzing job match..."):

        response = requests.post(API_URL, json={"job_description": jd})

        data = response.json()

        jd_analysis = data["jd_analysis"]
        match = data["match_analysis"]

        st.subheader("Match Score")

        score = match.get("match_score", 0)

        st.progress(score / 100)
        st.metric("Overall Match", f"{score}%")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Strong Matches")

            for item in match.get("strong_matches", []):
                st.success(item)

            st.subheader("Partial Matches")

            for item in match.get("partial_matches", []):
                st.info(item)

        with col2:

            st.subheader("Missing Skills")

            for item in match.get("missing_skills", []):
                st.warning(item)

            st.subheader("Project Evidence")

            for item in match.get("project_evidence", []):
                st.write("•", item)

        st.subheader("Positioning Advice")

        st.write(match.get("positioning_advice", ""))

        st.subheader("JD Analysis")

        st.write(jd_analysis)