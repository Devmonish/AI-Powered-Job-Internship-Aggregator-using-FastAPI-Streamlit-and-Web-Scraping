#python update_jobs/ujobs.py
# This script orchestrates the entire job update process by running the scraping, cleaning, and database loading scripts in sequence.

import subprocess
import time

print("=" * 50)
print("JOB AGGREGATOR UPDATE PIPELINE")
print("=" * 50)

# Step 1
print("\n[1/3] Scraping We Work Remotely...")

subprocess.run(
    ["python", "scraper/wwr.py"],
    check=True
)

print("✓ Scraping completed")

time.sleep(1)

# Step 2
print("\n[2/3] Cleaning data...")

subprocess.run(
    ["python", "scraper/c_wwr.py"],
    check=True
)

print("✓ Data cleaning completed")

time.sleep(1)

# Step 3
print("\n[3/3] Loading database...")

subprocess.run(
    ["python", "database/load.py"],
    check=True
)

print("✓ Database updated")

print("\n" + "=" * 50)
print("ALL TASKS COMPLETED SUCCESSFULLY")
print("=" * 50)