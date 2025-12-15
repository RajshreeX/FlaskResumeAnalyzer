from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    score = round(similarity * 100, 2)
    return score


def find_missing_skills(resume_text, jd_text):
    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())

    missing = jd_words - resume_words
    return list(missing)[:10]  # limit output
