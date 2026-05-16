import streamlit as st
from resume_parser import extract_text_from_pdf
from utils import extract_skills, missing_skills
from scorer import calculate_similarity

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and check ATS score instantly.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

jd_input = st.text_area(
    "Paste Job Description"
)

if uploaded_file is not None:

    resume_text = extract_text_from_pdf(uploaded_file)

    skills = extract_skills(resume_text)

    st.subheader("✅ Extracted Skills")

    if skills:
        st.write(skills)
    else:
        st.warning("No skills found.")

    if jd_input:

        score = calculate_similarity(resume_text, jd_input)

        st.subheader("📊 ATS Match Score")

        st.progress(int(score))

        st.success(f"Match Score: {score}%")

        missing = missing_skills(skills)

        st.subheader("❌ Missing Skills")

        if missing:
            st.write(missing[:10])
        else:
            st.success("No missing skills detected.")