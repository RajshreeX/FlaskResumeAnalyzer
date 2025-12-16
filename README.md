# 🚀 AI Resume Analyzer  
![Python](https://img.shields.io/badge/Python-Flask-blue)
![React](https://img.shields.io/badge/Frontend-React-blue)
![AI](https://img.shields.io/badge/NLP-TF--IDF-green)
![Status](https://img.shields.io/badge/Project-Active-success)

### AI-powered Resume–Job Matching System (Flask + React)


A full-stack AI-powered web application that analyzes how well a resume matches a given job description. The system provides an **explainable match score**, highlights **matched and missing skills**, and gives a clear verdict to help candidates understand their skill gaps.

---

## 🚀 Features

* Upload resume and job description (PDF)
* Skill-based matching using a curated skill list
* NLP-based text similarity scoring
* Explainable output with matched & missing skills
* Overall compatibility score with verdict
* Clean and interactive React UI

---

## ⭐ Key Highlights

- Explainable AI scoring (not black-box)
- Real-world hiring use case
- Full-stack architecture
- Clean REST API design

---

## 🧠 How It Works

The application combines **rule-based skill matching** with **NLP techniques** to avoid unrealistic or misleading scores.

1. **Text Extraction**
   Resume and job description PDFs are parsed to extract raw text.

2. **Skill Extraction**
   A predefined skill ontology is used to detect explicit skills from both documents.

3. **Scoring Logic**

   * Skill overlap score (higher weight)
   * Text similarity score using TF-IDF + cosine similarity
   * Final score is a weighted combination of both

4. **Explainability**
   The system returns:

   * Matched skills
   * Missing skills
   * Overall score
   * Verdict (Good fit / Partial match)

---

## 🧱 Tech Stack

**Frontend:** React (Vite), CSS
**Backend:** Flask (Python)
**AI / NLP:** TF-IDF, cosine similarity (scikit-learn)
**Other:** PDF parsing, REST API

---

## 📁 Project Structure

```
AI-Resume-Analyzer/
├── backend/
│   ├── app.py
│   └── utils/
│       ├── scoring.py
│       └── skills.py
├── frontend/
│   └── src/
│       ├── App.jsx
│       ├── api.js
│       └── App.css
└── README.md

```

---

## ▶️ Running the Project Locally

### Backend

```bash
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
npm install
npm run dev
```

---

## 📊 Sample Output

* Match Score: `61.11%`
* Matched Skills: Java, Python, React, SQL, Git
* Missing Skills: Node.js, REST API, MongoDB
* Verdict: *Good fit for fresher roles with minor skill gaps*

---

## 📌 Why This Project Matters

* Focuses on **explainable AI**, not black-box scoring
* Solves a real-world hiring problem
* Demonstrates full-stack + AI integration
* Designed with recruiter and candidate usability in mind

---

## 🎥 Demo

> Local demo available.  
> API tested using Postman with real resume & JD PDFs.

---

## 🔮 Future Improvements

* Resume keyword suggestions
* Role-specific scoring weights
* Semantic embeddings (BERT / Sentence Transformers)
* User authentication & history
* Deployment with Docker

---

## 👩‍💻 Author

Built as a portfolio project to demonstrate **full-stack development and applied AI for hiring technology**.

---

📌 This project demonstrates skills relevant for:
- Software Engineer (Fresher)
- Full-Stack Developer
- AI / ML Engineer (Applied NLP)

