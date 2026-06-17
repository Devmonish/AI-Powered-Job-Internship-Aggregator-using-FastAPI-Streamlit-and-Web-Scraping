# python scraper/wwr.py

# This script scrapes job listings from We Work Remotely and saves the HTML content to a file for further processing.
""" 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

URL = "https://weworkremotely.com/remote-jobs"

headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
}

response = requests.get(URL, headers=headers)

print("Status Code:", response.status_code)

with open("data/wwr_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("HTML saved successfully.")
"""

# This script reads the saved HTML content from We Work Remotely and uses BeautifulSoup to parse it and extract information.
""" 
from bs4 import BeautifulSoup

with open("data/wwr_page.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

print("Title:", soup.title.text)

links = soup.find_all("a")

print("Total links:", len(links))

for link in links[:20]:
    print(link.get("href"))
"""

# This script specifically looks for job links in the saved HTML content from We Work Remotely and prints them out.
""" 
from bs4 import BeautifulSoup

with open("data/wwr_page.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a", href=True)

job_links = []

for link in links:
    href = link["href"]

    if "/remote-jobs/" in href:
        job_links.append(href)

print("Total job links found:", len(job_links))

for job in job_links[:30]:
    print(job)

    

# This script refines the previous one by filtering out certain links and printing the URL and text of the first valid job link found.
with open("data/wwr_page.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

job_links = []

for link in soup.find_all("a", href=True):
    href = link["href"]

    if "/remote-jobs/" in href and "find-your-plan" not in href:

        print("\n===================")
        print("URL:", href)
        print("TEXT:", link.get_text(" ", strip=True))

        break
"""


# This final script combines all the previous steps to scrape job listings from We Work Remotely, filter them, and save the results to a CSV file.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

url = "https://weworkremotely.com/remote-jobs"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

jobs = []

for link in soup.find_all("a", href=True):

    href = link["href"]

    if "/remote-jobs/" not in href:
        continue

    if "find-your-plan" in href:
        continue

    text = link.get_text(" ", strip=True)

    if len(text) < 15:
        continue

    jobs.append({
        "job_url": "https://weworkremotely.com" + href,
        "raw_text": text,
        "source": "We Work Remotely"
    })

df = pd.DataFrame(jobs)

df.drop_duplicates(subset=["job_url"], inplace=True)

df.to_csv("data/wwr_jobs.csv", index=False)

print(f"Saved {len(df)} jobs")
