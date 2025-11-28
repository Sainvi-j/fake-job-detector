# models/model.py
import os
import re
import joblib                          
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer



BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, 'fake_job_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'tfidf_vectorizer.pkl')



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
    """Returns job authenticity label and confidence score."""

    # Validation: too short or empty input
    if not text or len(text.strip()) < 30:
        print("⚠ Text too short for prediction")
        return None, None

    # Validate model + vectorizer exist
    if not os.path.exists(MODEL_PATH):
        print(f"❌ MODEL FILE MISSING: {MODEL_PATH}")
        return None, None

    if not os.path.exists(VECTORIZER_PATH):
        print(f"❌ VECTORIZER FILE MISSING: {VECTORIZER_PATH}")
        return None, None

    try:
        # Load once per request
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)

        # Prepare input
        cleaned = clean_text(text)
        X = vectorizer.transform([cleaned])

        # Predict
        prediction = model.predict(X)[0]
        confidence = float(max(model.predict_proba(X)[0]) * 100)

        # Match Flask expected labels
        label = "Fake Job" if prediction == 0 else "Real Job"

        print(f"✔ Prediction: {label} ({confidence:.2f}%)")
        return label, round(confidence, 1)

    except Exception as e:
        print(f"❌ MODEL FAILED: {e}")
        return None, None
