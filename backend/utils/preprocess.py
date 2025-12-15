import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    words = text.split()
    stop_words = set(stopwords.words("english"))

    cleaned_words = [w for w in words if w not in stop_words]

    return " ".join(cleaned_words)
