import streamlit as st
import pandas as pd
import fitz
from docx import Document

from src.skill_extractor import extract_skills
from src.matcher import calculate_similarity, calculate_skill_match, calculate_final_score


st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="wide",
)

st.title("📄 AI Resume Screening & Job Matching System")
st.caption("Upload a job description and candidate resumes to compare skills and rank candidates.")

def extract_pdf_text(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text() + "\n"
    pdf.close()
    return text

def extract_docx_text(file):
    document = Document(file)
    return "\n".join(p.text for p in document.paragraphs)

def extract_resume_text(file):
    name = file.name.lower()
    if name.endswith(".pdf"):
        return extract_pdf_text(file)
    if name.endswith(".docx"):
        return extract_docx_text(file)
    return ""

with st.sidebar:
    st.header("🎯 Job Description")
    job_description = st.text_area(
        "Paste the job description",
        height=300,
        placeholder="Example: Looking for a Python and Machine Learning intern with SQL, Pandas and Scikit-learn experience."
    )

uploaded_resumes = st.file_uploader(
    "📤 Upload candidate resumes (PDF or DOCX)",
    type=["pdf", "docx"],
    accept_multiple_files=True,
)

if st.button("🚀 Screen Candidates", type="primary"):
    if not job_description.strip():
        st.warning("Please enter a job description.")
        st.stop()

    if not uploaded_resumes:
        st.warning("Please upload at least one resume.")
        st.stop()

    job_skills = extract_skills(job_description)
    results = []

    for resume in uploaded_resumes:
        resume_text = extract_resume_text(resume)

        if not resume_text.strip():
            st.warning(f"Could not extract readable text from {resume.name}.")
            continue

        resume_skills = extract_skills(resume_text)
        semantic_score = calculate_similarity(job_description, resume_text)
        skill_score = calculate_skill_match(job_skills, resume_skills)
        final_score = calculate_final_score(semantic_score, skill_score)

        matched = sorted(set(job_skills) & set(resume_skills))
        missing = sorted(set(job_skills) - set(resume_skills))

        results.append({
            "Candidate": resume.name,
            "Match Score": final_score,
            "Semantic Score": semantic_score,
            "Skill Score": skill_score,
            "Matched Skills": ", ".join(matched) or "None detected",
            "Missing Skills": ", ".join(missing) or "None",
        })

    if not results:
        st.error("No readable resumes were found.")
        st.stop()

    results.sort(key=lambda x: x["Match Score"], reverse=True)
    df = pd.DataFrame(results)

    st.success(f"Screened {len(results)} candidate(s).")

    st.subheader("🏆 Candidate Ranking")
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("📊 Detailed Results")
    for result in results:
        with st.expander(f"{result['Candidate']} — {result['Match Score']}%"):
            c1, c2, c3 = st.columns(3)
            c1.metric("Overall Match", f"{result['Match Score']}%")
            c2.metric("Semantic Match", f"{result['Semantic Score']}%")
            c3.metric("Skill Match", f"{result['Skill Score']}%")
            st.write("**Matched Skills:**", result["Matched Skills"])
            st.write("**Missing Skills:**", result["Missing Skills"])
