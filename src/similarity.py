from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(job_descriptions, candidate_skills):
    vectorizer = TfidfVectorizer()
    job_matrix = vectorizer.fit_transform(job_descriptions)
    candidate_matrix = vectorizer.transform(candidate_skills)
    return cosine_similarity(job_matrix, candidate_matrix)