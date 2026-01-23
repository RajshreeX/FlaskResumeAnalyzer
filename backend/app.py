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

# ────────────────────────────────────────────────
#  ← Add this small root route (minimal fix)
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "FlaskResumeAnalyzer backend is running",
        "test_endpoint": "/test",
        "main_endpoint": "/analyze (POST)"
    })
# ────────────────────────────────────────────────

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
    jd_text = request.form.get("jd_text", "").strip()
    jd_file = request.files.get("jd")

    if not resume:
        return jsonify({"error": "Resume required"}), 400

    if not jd_text and not jd_file:
        return jsonify({"error": "Job description required"}), 400

    # Save and process resume
    resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(resume_path)
    resume_text = preprocess(extract_text(resume_path))

    # Process JD
    if jd_text:
        jd_text = preprocess(jd_text)
    else:
        jd_path = os.path.join(UPLOAD_FOLDER, jd_file.filename)
        jd_file.save(jd_path)
        jd_text = preprocess(extract_text(jd_path))

    score = combined_score(resume_text, jd_text)
    verdict = get_verdict(score)

    resume_skills = extract_skills_from_text(resume_text)
    jd_skills = extract_skills_from_text(jd_text)

    return jsonify({
        "overall_score": score,
        "matched_skills": list(resume_skills & jd_skills),
        "missing_skills": list(jd_skills - resume_skills),
        "verdict": verdict
    })



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",10000)))


