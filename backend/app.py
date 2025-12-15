from flask import Flask, request, jsonify
import os

from utils.extract_text import extract_text
from utils.preprocess import preprocess
from utils.scoring import calculate_score, find_missing_skills

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


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

    score = calculate_score(resume_text, jd_text)
    missing_skills = find_missing_skills(resume_text, jd_text)

    return jsonify({
        "match_score": score,
        "missing_skills": missing_skills
    })


if __name__ == "__main__":
    app.run(debug=True)
