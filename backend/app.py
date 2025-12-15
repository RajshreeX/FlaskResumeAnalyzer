from flask import Flask, request, jsonify
import os
from flask_cors import CORS
from utils.extract_text import extract_text
from utils.preprocess import preprocess
from utils.scoring import skill_match_score, find_missing_skills,extract_skills_from_text, combined_score


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/test")
def test():
    print("🔥 UPDATED FLASK CODE RUNNING")
    return {"msg": "UPDATED RESPONSE"}

def get_verdict(score):
    if score >= 70:
        return "Strong fit for the role"
    elif score >= 55:
        return "Good fit for fresher roles with minor skill gaps"
    elif score >= 40:
        return "Partial match – skill improvement recommended"
    else:
        return "Low match – significant upskilling required"

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    resume = request.files.get("resume")
    jd = request.files.get("jd")

    if not resume or not jd:
        return jsonify({"error": "Resume and JD required"}), 400

    resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    jd_path = os.path.join(UPLOAD_FOLDER, jd.filename)

    resume.save(resume_path)
    jd.save(jd_path)

    resume_text = preprocess(extract_text(resume_path))
    jd_text = preprocess(extract_text(jd_path))

    score = combined_score(resume_text, jd_text)
    verdict=get_verdict(score)
    resume_skills = extract_skills_from_text(resume_text)
    jd_skills = extract_skills_from_text(jd_text)

    matched_skills = list(resume_skills & jd_skills)
    missing_skills = list(jd_skills - resume_skills)
    

    return jsonify({
    "overall_score": score,
    "matched_skills": matched_skills,
    "missing_skills": missing_skills,
    "verdict": verdict
    })


if __name__ == "__main__":
    app.run(debug=True)


