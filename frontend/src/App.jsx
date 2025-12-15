import { useState } from "react";
import { analyzeResume } from "./api";
import "./App.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!resume || !jd) {
      alert("Upload both files");
      return;
    }

    setLoading(true);
    const data = await analyzeResume(resume, jd);
    setResult(data);
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>AI Resume Analyzer</h1>

      <input type="file" onChange={(e) => setResume(e.target.files[0])} />
      <input type="file" onChange={(e) => setJd(e.target.files[0])} />

      <button onClick={handleSubmit}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {result && (
        <div className="result">
          <h2>Match Score</h2>
          <div className="progress-bar">
            <div className="progress" style={{ width: `${result.overall_score}%` }}>
              {result.overall_score}%
            </div>
          </div>
          <p><b>Verdict:</b></p>
          <div className="verdict">
            {result.verdict}
          </div>


          <h3>Matched Skills</h3>
          <div className="skills">
            {result.matched_skills.map((s, i) => (
              <span className="tag matched" key={i}>{s}</span>
            ))}
          </div>

          <h3>Missing Skills</h3>
          <div className="skills">
            {result.missing_skills.map((s, i) => (
              <span className="tag missing" key={i}>{s}</span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
