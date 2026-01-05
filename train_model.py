# train_model.py — run with optional dataset path
import sys
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

# Get dataset path from argument or use default
if len(sys.argv) > 1:
    dataset_path = sys.argv[1]
else:
    dataset_path = 'job_dataset.csv'

print(f"Training with dataset: {dataset_path}")

# Load data
df = pd.read_csv(dataset_path)

# Auto-detect text and label columns
text_col = None
label_col = None
for col in df.columns:
    if col.lower() in ['description', 'text', 'job_description']:
        text_col = col
    if col.lower() in ['fraudulent', 'is_fake', 'label']:
        label_col = col

if not text_col or not label_col:
    print("Error: Could not find text or label column")
    sys.exit(1)

X = df[text_col].fillna('')
y = df[label_col]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorizer
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train_vec, y_train)

# Accuracy
y_pred = model.predict(X_test_vec)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.2f}")

# Save
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/fake_job_model.pkl')
joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')

print("Training complete!")