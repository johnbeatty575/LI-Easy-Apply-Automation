import sqlite3
import logging
from datetime import datetime

# Database setup
def initialize_db():
    try:
        conn = sqlite3.connect("applications.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_title TEXT NOT NULL,
                company TEXT NOT NULL,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        logging.info("Database initialized successfully.")
    except Exception as e:
        logging.error(f"Failed to initialize database: {e}")
    finally:
        if conn:
            conn.close()

# Save application to database
def save_application(job_title, company):
    try:
        conn = sqlite3.connect("applications.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO applications (job_title, company) VALUES (?, ?)
        ''', (job_title, company))
        conn.commit()
        logging.info(f"Saved application to database: {job_title} at {company}.")
    except Exception as e:
        logging.error(f"Failed to save application to database: {e}")
    finally:
        if conn:
            conn.close()

# Log application to file
def log_application(job_title, company):
    logging.info(f"Applied to {job_title} at {company}.")