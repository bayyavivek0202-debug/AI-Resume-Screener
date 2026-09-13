from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(job_description, resume_text):
    documents = [job_description, resume_text]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)
    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return round(score * 100, 2)

def calculate_skill_match(job_skills, resume_skills):
    if not job_skills:
        return 0.0
    matched = set(job_skills) & set(resume_skills)
    return round((len(matched) / len(set(job_skills))) * 100, 2)

def calculate_final_score(semantic_score, skill_score):
    return round((semantic_score * 0.4) + (skill_score * 0.6), 2)
