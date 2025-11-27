# models/database.py
import sqlite3

DB_NAME = "predictions.db"   # ← ONE SINGLE DATABASE NAME

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS predictions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT DEFAULT (datetime('now')),
                  description TEXT,
                  label TEXT,
                  confidence REAL)''')
    conn.commit()
    conn.close()

def save_prediction(text, label, confidence):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO predictions (description, label, confidence) VALUES (?, ?, ?)",
              (text, label, confidence))
    conn.commit()
    conn.close()

def get_stats():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM predictions WHERE label='Fake Job'")
    fake = c.fetchone()[0] or 0
    c.execute("SELECT COUNT(*) FROM predictions WHERE label='Real Job'")
    real = c.fetchone()[0] or 0
    conn.close()
    return fake, real

def get_history():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT timestamp, description, label, confidence FROM predictions ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_chart_data():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT label, COUNT(*) FROM predictions GROUP BY label")
    pie = c.fetchall()
    c.execute("""SELECT DATE(timestamp) as date, COUNT(*) FROM predictions 
                 GROUP BY DATE(timestamp) ORDER BY date DESC LIMIT 10""")
    line_data = c.fetchall()
    dates = [row[0] for row in line_data[::-1]]
    counts = [row[1] for row in line_data[::-1]]
    conn.close()
    return pie, (dates, counts)