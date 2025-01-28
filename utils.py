import logging

# Configure logging
logging.basicConfig(
    filename='logs/application_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def log_application(job_title, company):
    """Log details of applied jobs."""
    logging.info(f"Applied to {job_title} at {company}")
    
import sqlite3

# Initialize SQLite database
def initialize_db():
    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY,
            job_title TEXT,
            company TEXT,
            applied_on DATE DEFAULT CURRENT_DATE
        )
    ''')
    conn.commit()
    conn.close()

def save_application(job_title, company):
    """Save job application details to SQLite."""
    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO applications (job_title, company)
        VALUES (?, ?)
    ''', (job_title, company))
    conn.commit()
    conn.close()
