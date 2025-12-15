from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.skills import SKILLS

# --------------------
# 1) Basic similarity score (0–100)
# --------------------
def calculate_score(resume_text, jd_text):
    if not resume_text.strip() or not jd_text.strip():
        return 0.0

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(similarity * 100, 2)


# --------------------
# 2) Split resume into sections
# --------------------
def split_sections(text):
    sections = {
        "skills": "",
        "experience": "",
        "education": "",
        "projects": ""
    }

    lower_text = text.lower()

    for key in sections:
        if key in lower_text:
            sections[key] = lower_text.split(key, 1)[1]

    return sections


# --------------------
# 3) Weighted + normalized score (FINAL LOGIC)
# --------------------
def weighted_score(resume_text, jd_text):
    weights = {
        "skills": 0.5,
        "experience": 0.3,
        "projects": 0.2
    }

    resume_sections = split_sections(resume_text)

    total_score = 0.0
    total_weight = 0.0

    for section, weight in weights.items():
        section_text = resume_sections.get(section, "")

        if section_text.strip():
            section_score = calculate_score(section_text, jd_text)
            total_score += section_score * weight
            total_weight += weight

    if total_weight == 0:
        return 0.0

    # Normalize score back to 0–100
    return round(total_score / total_weight, 2)


# --------------------
# 4) Missing skills (clean output)
# --------------------
def find_missing_skills(resume_text, jd_text):
    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    resume_skills = {skill for skill in SKILLS if skill in resume_text}
    jd_skills = {skill for skill in SKILLS if skill in jd_text}

    missing = jd_skills - resume_skills
    return list(missing)

def skill_match_score(resume_text, jd_text):
    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    resume_skills = {skill for skill in SKILLS if skill in resume_text}
    jd_skills = {skill for skill in SKILLS if skill in jd_text}

    if not jd_skills:
        return 0.0

    score = len(resume_skills & jd_skills) / len(jd_skills)
    return round(score * 100, 2)



