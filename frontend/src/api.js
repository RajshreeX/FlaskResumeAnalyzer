export async function analyzeResume(resumeFile, jdFile) {
  const formData = new FormData();
  formData.append("resume", resumeFile);
  formData.append("jd", jdFile);

  const response = await fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    body: formData
  });

  return response.json();
}
