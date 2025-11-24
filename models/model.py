# To be handled by Shruti

import pickle
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

# Safe loading with fallback message
MODEL_PATH = 'fake_job_model.pkl'
VECTORIZER_PATH = 'tfidf_vectorizer.pkl'

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in text.split() if word not in stop_words]
    return ' '.join(words)

def predict_job(text):
    if not text.strip() or len(text) < 50:
        return "Invalid", 0

    # Check if model files exist
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        return "Model not available", 0

    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        with open(VECTORIZER_PATH, 'rb') as f:
            vectorizer = pickle.load(f)

        cleaned = clean_text(text)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)[0]
        confidence = max(model.predict_proba(vec)[0]) * 100
        result = "Fake" if prediction == 0 else "Real"
        return result, round(confidence, 2)

    except Exception as e:
        print(f"Model loading error: {e}")
        return "Model error", 0