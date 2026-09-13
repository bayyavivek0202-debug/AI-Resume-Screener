# AI Resume Screening & Job Matching System

An AI/NLP-based student portfolio project that extracts text from resumes, detects relevant skills, compares resumes with a job description, and ranks candidates.

## Features

- PDF and DOCX resume upload
- Job description input
- Skill extraction
- TF-IDF semantic similarity
- Skill-match scoring
- Weighted overall match score
- Candidate ranking
- Matched and missing skills
- Streamlit web interface

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- python-docx
- Pandas
- Scikit-learn
- NumPy

## Run locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

## Project structure

```text
AI-Resume-Screener/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── matcher.py
│   └── skill_extractor.py
└── sample_data/
    └── sample_job_description.txt
```

## Scoring

The current prototype uses:

- 40% semantic similarity
- 60% skill match

This is a screening aid, not an automated hiring decision system. Human review should remain part of recruitment decisions.

## Privacy

Do not commit real candidates' resumes or personal information to a public GitHub repository. Use synthetic/sample documents for demonstrations.
