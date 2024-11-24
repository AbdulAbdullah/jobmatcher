# AI-Powered Resume Parser & Job Matcher

An advanced Django-based web application that processes resumes, extracts skills using Natural Language Processing (NLP), and matches candidates to job postings using similarity scoring.

---

## Features

1. **Resume Parsing**:
   - Extracts text from resumes in PDF format using PyPDF2.

2. **Skills Extraction**:
   - Uses spaCy NLP to identify and extract relevant skills from resumes.

3. **Job Matching**:
   - Compares resumes and job descriptions using TF-IDF vectorization.
   - Calculates match scores with cosine similarity.

4. **RESTful API**:
   - Upload resumes via API endpoints.
   - Match resumes to job postings and calculate match percentages.

---

## Tech Stack

- **Backend**: Django REST Framework
- **NLP**: spaCy
- **PDF Parsing**: PyPDF2
- **Similarity Scoring**: Scikit-learn
- **Database**: SQLite (default) / PostgreSQL (production)

---

## Installation

### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- pip
- Virtualenv (optional but recommended)

### Steps

1. Clone the Repository:
   ```bash
   git clone https://github.com/AbdulAbdullah/jobmatcher.git
   cd jobmatcher


2. Create and Activate a Virtual Environment:
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows: env\Scripts\activate

3. Install Dependencies:
    ```bash
    pip install -r requirements.txt

4. Apply Migrations:
    ```bash
    python manage.py migrate

5. Run the Server:
    ```bash
    ./manage.py runserver

6. Access the API at:
    ```bash
    http://127.0.0.1:8000/


# Usage
## API Endpoints

1. Upload Resume

- **Endpoint**: POST /upload-resume/
- **Description**: Uploads a PDF resume and extracts skills.
- **Request Body**:
  ```json
  {
    "candidate_name": "Gojo Satoru",
    "email": "gojosatoru@example.com", 
    "file": "<PDF File>"
  }
  ```
- **Response**:
  ```json
  {
  "message": "Resume uploaded successfully",
  "skills": ["Python", "Django", "Machine Learning", "Demon Hunting", "Domain Expansion", "Limitless"]
    }
  ```    

2. Match Resume with Job

-   **Endpoint**: POST /match-job/
-   **Description**: Matches a resume with a job posting and calculates a match score.
-   **Request Body**:
    ```json
    {
  "resume_id": 1,
  "job_id": 2
    }
    ```
-   **Response**:
    ```json
    {
  "resume": 1,
  "job_posting": 2,
  "match_score": 85.34
    }
    ```

