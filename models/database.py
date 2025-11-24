# To be handled by Shruti

import sqlite3
from datetime import datetime

DB_NAME = "job_predictions.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS predictions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  job_text TEXT,
                  result TEXT,
                  confidence REAL)''')
    conn.commit()
    conn.close()

def save_prediction(job_text, result, confidence):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO predictions (timestamp, job_text, result, confidence) VALUES (?, ?, ?, ?)",
              (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), job_text, result, confidence))
    conn.commit()
    conn.close()

def get_stats():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM predictions WHERE result='Fake'")
    fake = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM predictions WHERE result='Real'")
    real = c.fetchone()[0]
    conn.close()
    return fake, real

def get_history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT timestamp, job_text, result, confidence FROM predictions ORDER BY id DESC LIMIT 50")
    rows = c.fetchall()
    conn.close()
    return rows

def get_chart_data():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Pie data
    c.execute("SELECT result, COUNT(*) FROM predictions GROUP BY result")
    pie = c.fetchall()
    # Daily trend (last 10 days)
    c.execute("""SELECT DATE(timestamp), COUNT(*) FROM predictions 
                 GROUP BY DATE(timestamp) ORDER BY timestamp DESC LIMIT 10""")
    line = c.fetchall()
    conn.close()
    return pie, line