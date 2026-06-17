#python database/load.py

## Load jobs from CSV into SQLite database with updated schema
import sqlite3
import pandas as pd

conn = sqlite3.connect("database/jobs.db")

df = pd.read_csv(
    "data/wwr_s.csv"
)

# Delete old jobs
conn.execute("DELETE FROM jobs")

# Insert fresh jobs
df.to_sql(
    "jobs",
    conn,
    if_exists="append",
    index=False
)

print(f"{len(df)} jobs inserted successfully!")

conn.commit()
conn.close()