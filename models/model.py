# models/model.py
import os
import re
import joblib                          
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Paths inside models folder
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, 'fake_job_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'tfidf_vectorizer.pkl')

# Download stopwords
try:
    nltk.data.find('corpora/stopwords')
except:
    nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    text = re.sub(r'[^a-z\s]', '', text.lower())
    words = [stemmer.stem(w) for w in text.split() if w not in stop_words]
    return ' '.join(words)

def predict_job(text):
    if not text or len(text.strip()) < 30:
        return "Invalid", 0

    if not os.path.exists(MODEL_PATH):
        print("MODEL FILE MISSING:", MODEL_PATH)
        return "Model missing", 0
    if not os.path.exists(VECTORIZER_PATH):
        print("VECTORIZER MISSING:", VECTORIZER_PATH)
        return "Vectorizer missing", 0

    try:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)

        cleaned = clean_text(text)
        X = vectorizer.transform([cleaned])
        prediction = model.predict(X)[0]
        confidence = max(model.predict_proba(X)[0]) * 100

        label = "Fake Job" if prediction == 0 else "Real Job"
        return label, round(confidence, 1)

    except Exception as e:
        print(f"MODEL FAILED: {e}")
        return "Error", 0