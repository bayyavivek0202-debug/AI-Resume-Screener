SKILLS = [
    "python", "java", "c", "c++", "sql", "machine learning",
    "deep learning", "artificial intelligence", "data science",
    "data analytics", "pandas", "numpy", "matplotlib",
    "scikit-learn", "tensorflow", "pytorch", "nlp",
    "natural language processing", "generative ai", "agentic ai",
    "power bi", "tableau", "excel", "git", "github", "docker",
    "aws", "azure", "gcp", "spark", "flask", "streamlit"
]

def extract_skills(text):
    text = text.lower()
    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return sorted(set(found))
