# code model.py

import pickle
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

# Ensure stopwords are downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Safe loading with fallback message
MODEL_PATH = 'fake_job_model.pkl'
VECTORIZER_PATH = 'tfidf_vectorizer.pkl'


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    words = [
        stemmer.stem(word)
        for word in text.split()
        if word not in stop_words
    ]

    return ' '.join(words)


def predict_job(text):
    # Basic validation
    if not text or not text.strip() or len(text) < 50:
        return "Invalid", 0

    # Check if model files exist
    if not os.path.exists(MODEL_PATH):
        return "Model not available", 0
    if not os.path.exists(VECTORIZER_PATH):
        return "Model not available", 0

    try:
        # Load model
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)

        # Load vectorizer
        with open(VECTORIZER_PATH, 'rb') as f:
            vectorizer = pickle.load(f)

        # Transform text
        cleaned_text = clean_text(text)
        vector = vectorizer.transform([cleaned_text])

        # Prediction
        prediction = model.predict(vector)[0]

        # Confidence score (safe for models without predict_proba)
        if hasattr(model, "predict_proba"):
            confidence = max(model.predict_proba(vector)[0]) * 100
        else:
            confidence = 75.0  # fallback default

        label = "Fake" if prediction == 0 else "Real"

        return label, round(confidence, 2)

    except Exception as e:
        print(f"Model loading error: {e}")
        return "Model error", 0


# Optional test runner
if __name__ == "__main__":
    text = input("Enter job description:\n")
    print(predict_job(text))




#output


PS C:\html info> python model.py
Enter job description:
We are hiring a Senior Data Scientist with 5+ years experience in Python and machine learning. Full-time in Bangalore office.
('Real', np.float64(76.64))
PS C:\html info> python model.py
Enter job description:
Urgent hiring! Work from home message on WhatsApp. Earn 10,000 daily.
('Fake', np.float64(91.38))
