# 🚀 Job Aggregator

A full-stack Job & Internship Aggregator built using Python, FastAPI, SQLite, and Streamlit. The application collects job listings from We Work Remotely, stores them in a database, and provides an interactive dashboard for searching and filtering opportunities.

---

## 📌 Features

### Data Collection

* Scrapes real job listings from We Work Remotely
* Extracts job information such as:

  * Title
  * Company
  * Location
  * Job URL
* Stores data in CSV format

### Data Processing

* Cleans and structures scraped data
* Removes duplicates
* Converts raw job listings into structured records

### Database

* SQLite database integration
* Stores jobs with:

  * Title
  * Company
  * Location
  * Job URL
  * Source

### FastAPI Backend

Provides REST APIs for:

* `GET /jobs` → Fetch latest jobs
* `GET /job/{id}` → Fetch job by ID
* `GET /search` → Search jobs
* `GET /locations` → Get available locations
* `GET /companies` → Get available companies

### Streamlit Dashboard

* Keyword Search
* Location Filter
* Company Filter
* Pagination
* Direct Apply Links

---

## 🏗️ Project Architecture

```text
We Work Remotely
        │
        ▼
   Web Scraper
        │
        ▼
 Structured CSV
        │
        ▼
 SQLite Database
        │
        ▼
 FastAPI Backend
        │
        ▼
 Streamlit Dashboard
```

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI

### Web Scraping

* Requests
* BeautifulSoup

### Database

* SQLite

### Data Processing

* Pandas

### Frontend

* Streamlit

---

## 📂 Project Structure

```text
job_aggregator/
│
├── scraper/
│   ├── wwr.py
│   └── clean_wwr_v2.py
│
├── database/
│   ├── db.py
│   └── load.py
│
├── api/
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── wwr_jobs.csv
│   └── wwr_structured.csv
│
├── update_jobs.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/job-aggregator.git

cd job-aggregator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Update Job Data

```bash
python update_jobs.py
```

### Step 2: Start FastAPI

```bash
uvicorn api.main:app --reload
```

API Docs:

```text
http://127.0.0.1:8000/docs
```

### Step 3: Start Streamlit

```bash
streamlit run dashboard/app.py
```

Dashboard:

```text
http://localhost:8501
```

---

## 🔍 Search Examples

### Search by Keyword

```text
Python
Data Engineer
Product Manager
```

### Filter by Location

```text
Remote
Germany
France
Spain
```

### Filter by Company

```text
Toggl
Nearcut
Kojo
```

---

## 🎯 Future Improvements

* RemoteOK Integration
* Automatic Scheduled Updates
* Job Recommendation System
* User Authentication
* Email Notifications
* Deployment on Render & Streamlit Cloud
* Machine Learning Based Job Matching

---

## 💡 Learning Outcomes

This project demonstrates:

* Web Scraping
* Data Cleaning
* REST API Development
* Database Design
* FastAPI
* Streamlit
* End-to-End Full Stack Development
* Python Automation

---

## 👨‍💻 Author

Monish Jain

MBA Tech | Python Developer | FastAPI Enthusiast

GitHub: https://github.com/Devmonish
