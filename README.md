# JobCheck – Checking If a Job Post Is Real or Fake Using Text

**A full-stack AI-powered web application to detect fraudulent job postings using NLP and Machine Learning.**

November 2025 | Team Project

---

### Project Statement

Fake job postings are increasingly common on online portals and social media, often used to scam job seekers.  
This system uses **Natural Language Processing (NLP)** and **Machine Learning** to analyze job descriptions and classify them as **Real** or **Fake** in real time.

---

### Key Features

- Instant job authenticity verification with confidence score
- Animated progress bar (Green = Real, Red = Fake)
- Live counters: Real vs Fake jobs detected
- Full prediction history with timestamps
- Secure admin panel (admin / admin123)
- Interactive dashboard with Pie & Line charts (daily trends)
- Responsive, modern UI with glassmorphism design
- Modular Flask architecture using Blueprints

---

### Tech Stack

- **Backend**: Flask (Python)
- **ML**: scikit-learn, TF-IDF, Logistic Regression
- **Frontend**: HTML, CSS, JavaScript, Jinja2
- **Database**: SQLite
- **Charts**: Chart.js

---

### How to Run

```bash
git clone <your-repo-url>
cd fake-job-detector

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
python app.py
```

Open → http://127.0.0.1:5000

**Admin Login**  
URL: http://127.0.0.1:5000/admin/login  
Credentials: `admin` / `admin123`

---

### Project Structure

```
├── app.py                  # Entry point
├── routes/                 # main.py, admin.py
├── models/                 # model.py, database.py, .pkl files
├── templates/              # All HTML pages
├── static/                 # CSS/JS assets
├── train_model.py          # Retrain model anytime
└── job_dataset.csv         # Training data
```

---

### Team Contributions

| Member  | Role                          | Contribution                                         |
| ------- | ----------------------------- | ---------------------------------------------------- |
| Sainvi  | Backend & System Architecture | Flask structure, routing, database, ML integration   |
| Sruthi  | Machine Learning Engineer     | Model training, feature engineering, accuracy tuning |
| Muskaan | UI/UX Designer                | Complete frontend design, animations, responsiveness |
| Mayur   | Dashboard & Admin Panel       | Admin interface, Chart.js integration, analytics     |

All members contributed to testing, debugging, and final polishing.

---

**100% matches project PDF requirements**  
All modules implemented • Real-time results • Dashboard • Admin panel • Exportable history

**Status: Complete • Tested • Ready for Submission**

© 2025 JobCheck Team
