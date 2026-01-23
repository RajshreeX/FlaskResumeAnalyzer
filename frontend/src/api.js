export async function analyzeResume(resumeFile, jdFile, jdText) {
  const formData = new FormData();

  formData.append("resume", resumeFile);

  if (jdText && jdText.trim()) {
    formData.append("jd_text", jdText);
  } else if (jdFile) {
    formData.append("jd", jdFile);
  }

  const response = await fetch("https://flaskresumeanalyzer-2.onrender.com/analyze", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.error || "Bad Request");
  }

  return response.json();
}
