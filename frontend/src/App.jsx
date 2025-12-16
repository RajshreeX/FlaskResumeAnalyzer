import { useState } from "react";
import { analyzeResume } from "./api";
import "./App.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [jdText, setJdText] = useState("");


const handleSubmit = async () => {
  if (!resume) {
    alert("Please upload your resume");
    return;
  }

  if (!jd && !jdText.trim()) {
    alert("Please upload a JD file or paste JD text");
    return;
  }

  setResult(null); 
  setLoading(true);

  try {
    const data = await analyzeResume(resume, jd, jdText);
    setResult(data);
  } catch (err) {
    alert("Something went wrong. Try again.");
  }

  setLoading(false);
};

  return (
    <div className="container">
      <h1 className="title">AI Resume Analyzer</h1>
      <p className="subtitle">Check how well your resume matches a job description</p>

      <div className="upload-box">
        <label>Resume (PDF)</label>
        <input type="file" onChange={(e) => setResume(e.target.files[0])} />

        <label>Job Description (PDF)</label>
        <input type="file" onChange={(e) => setJd(e.target.files[0])} />
        <label>Or paste Job Description</label>
        <textarea placeholder="Paste job description here..." value={jdText} onChange={(e) => setJdText(e.target.value)} rows={6}/>
      </div>


      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {result && !loading && (
        <div className="card">
          <div className="result">
            <h2>Match Score</h2>
            <div className="progress-bar">
              <div className="progress" style={{ width: `${result.overall_score}%` }}>
                {result.overall_score}%
              </div>
            </div>

            <p><b>Verdict:</b></p>
            <div className={`verdict ${result.overall_score >= 60 ? "good" : "average"}`}>
              {result.verdict}
            </div>


            <h3>Matched Skills</h3>
            <div className="skills">
              {result.matched_skills?.map((s, i) => (
                <span className="tag matched" key={i}>{s}</span>
              ))}
            </div>

            <h3>Missing Skills</h3>
            <div className="skills">
              {result.missing_skills?.map((s, i) => (
                <span className="tag missing" key={i}>{s}</span>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
