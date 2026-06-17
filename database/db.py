#python database/db.py
# This script creates a SQLite database and a table to store job listings scraped from We Work Remotely.

#After deleting previous jobs.db we created new using structured then load csv in it

import sqlite3

conn = sqlite3.connect("database/jobs.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    job_url TEXT UNIQUE,
    source TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")