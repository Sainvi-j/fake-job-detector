"""# To be handled by Sruthi

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
    
    """


#code:-

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


if __name__ == "__main__":
    print("🔧 Initializing database...")
    init_db()
    print("✅ Database created successfully!")

    print("\n📝 Saving a test prediction...")
    save_prediction("This is a sample job description", "Fake", 88.5)

    print("\n📊 Fetching statistics...")
    fake, real = get_stats()
    print("Fake job count:", fake)
    print("Real job count:", real)

    print("\n📂 Fetching last 5 records...")
    history = get_history()
    for row in history[:5]:
        print(row)

    print("\n📈 Chart Data:")
    pie, line = get_chart_data()
    print("Pie Chart:", pie)
    print("Line Chart:", line)


# this is the output:-

PS C:\html info> & "C:/Program Files/Python312/python.exe" "c:/html info/database_handler.py"
🔧 Initializing database...
✅ Database created successfully!

📝 Saving a test prediction...

📊 Fetching statistics...
Fake job count: 2
Real job count: 0

📂 Fetching last 5 records...
('2025-11-25 22:53:04', 'This is a sample job description', 'Fake', 88.5)
('2025-11-25 22:52:34', 'This is a sample job description', 'Fake', 88.5)

📈 Chart Data:
Pie Chart: [('Fake', 2)]
Line Chart: [('2025-11-25', 2)]
    
