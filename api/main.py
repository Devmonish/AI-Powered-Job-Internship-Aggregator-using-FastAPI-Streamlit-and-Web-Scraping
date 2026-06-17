#uvicorn api.main:app --reload
# This is the main API file for the Job Aggregator. It defines the endpoints for fetching jobs and searching for jobs.
#http://127.0.0.1:8000/jobs  for latest 20 jobs
#http://127.0.0.1:8000/search?keyword=python  for searching jobs by keyword in the raw_text field

from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Job Aggregator API Running"}


@app.get("/jobs")
def get_jobs():

    conn = sqlite3.connect("database/jobs.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM jobs
    LIMIT 20
    """)

    rows = cursor.fetchall()

    conn.close()

    jobs = []

    for row in rows:

        jobs.append({
            "id": row[0],
            "title": row[1],
            "company": row[2],
            "location": row[3],
            "job_url": row[4],
            "source": row[5]
        })

    return jobs


@app.get("/search")
def search_jobs(
    keyword: str = "",
    location: str = "All",
    company: str = "All",
    page: int = 1,
    limit: int = 10
):


    conn = sqlite3.connect("database/jobs.db")

    cursor = conn.cursor()

    offset = (page - 1) * limit

    query = """
    SELECT *
    FROM jobs
    WHERE (
        title LIKE ?
        OR company LIKE ?
        OR location LIKE ?
    )
    """

    params = [
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ]

    if location != "All":

        query += " AND location = ?"

        params.append(location)

    if company != "All":

        query += " AND company = ?"

        params.append(company)

    query += " LIMIT ? OFFSET ?"

    params.extend([limit, offset])

    cursor.execute(query, params)

    rows = cursor.fetchall()

    conn.close()

    jobs = []

    for row in rows:

        jobs.append({
            "id": row[0],
            "title": row[1],
            "company": row[2],
            "location": row[3],
            "job_url": row[4],
            "source": row[5]
        })

    return jobs







@app.get("/job/{job_id}")
def get_job(job_id: int):

    conn = sqlite3.connect("database/jobs.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM jobs
        WHERE id = ?
        """,
        (job_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if not row:
        return {"message": "Job not found"}

    return {
        "id": row[0],
        "title": row[1],
        "company": row[2],
        "location": row[3],
        "job_url": row[4],
        "source": row[5]
    }




# New endpoint to get distinct locations for dropdown
@app.get("/locations")
def get_locations():

    conn = sqlite3.connect("database/jobs.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT DISTINCT location
    FROM jobs
    WHERE location != ''
    ORDER BY location
    """)

    rows = cursor.fetchall()

    conn.close()

    locations = [row[0] for row in rows]

    return locations


# New endpoint to get distinct companies for dropdown
@app.get("/companies")
def get_companies():

    conn = sqlite3.connect("database/jobs.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT DISTINCT company
    FROM jobs
    WHERE company IS NOT NULL
      AND company != ''
    ORDER BY company
    """)

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]