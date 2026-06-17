#python database/check.py
# This file is used to check the structure of the database.
import sqlite3

conn = sqlite3.connect("database/jobs.db")

cursor = conn.cursor()

cursor.execute("PRAGMA table_info(jobs)")

for row in cursor.fetchall():
    print(row)

conn.close()