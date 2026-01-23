export async function analyzeResume(resumeFile, jdFile, jdText) {
  const formData = new FormData();

  formData.append("resume", resumeFile);

  if (jdText && jdText.trim()) {
    formData.append("jd_text", jdText);
  } else if (jdFile) {
    formData.append("jd", jdFile);
  }

  const response = await fetch("http://127.0.0.1:10000/analyze", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.error || "Bad Request");
  }

  return response.json();
}
