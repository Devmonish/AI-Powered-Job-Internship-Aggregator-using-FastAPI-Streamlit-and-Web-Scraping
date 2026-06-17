#python scraper/c_wwr.py
### Clean We Work Remotely jobs data and save to CSV
import pandas as pd
import re

df = pd.read_csv("data/wwr_jobs.csv")

jobs = []

for _, row in df.iterrows():

    raw_text = str(row["raw_text"])
    url = row["job_url"]

    # Extract company after New / 2d / 3d / 9d
    company = ""

    match = re.search(
        r"(?:New|[0-9]+d)\s+(.*?)\s+(?:Remote|Full-Time|Featured|Anywhere|[A-Z][a-z]+,)",
        raw_text
    )

    if match:
        company = match.group(1)

    # Extract title (everything before New / 2d / 3d / 9d)
    title = raw_text

    for token in [" New ", " 2d ", " 3d ", " 9d "]:
        if token in raw_text:
            title = raw_text.split(token)[0]
            break

    # Basic location extraction
    location = ""

    if "Remote" in raw_text:
        location = "Remote"

    jobs.append({
        "title": title.strip(),
        "company": company.strip(),
        "location": location,
        "job_url": url,
        "source": row["source"]
    })

new_df = pd.DataFrame(jobs)

new_df.to_csv(
    "data/wwr_s.csv",
    index=False
)

print(new_df.head(20))
print(f"\nSaved {len(new_df)} jobs")