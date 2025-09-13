# job-platform-backend
📌 Job Board Backend (Django + PostgreSQL)
📖 Overview

The Job Board Backend is a RESTful API that enables employers to post jobs, applicants to apply for jobs, and admins to manage the platform.
It demonstrates modern backend development practices using Django REST Framework, PostgreSQL, JWT Authentication, and Swagger API documentation.

This project is built as part of the ALX ProDev Backend Engineering program.

✨ Features

👤 User roles: Admin, Employer, Applicant

🔐 Authentication & Authorization: JWT-based login & role-based access

💼 Job Management: Employers can post, update, and delete jobs

📄 Applications: Applicants can apply to jobs & track status

🔎 Search & Filter: Jobs can be searched by title, category, and location

📑 API Documentation: Interactive Swagger UI

🐳 Dockerized Setup (optional, if you add it later)

🛠️ Tech Stack

Backend Framework: Django, Django REST Framework

Database: PostgreSQL

Authentication: JWT (using djangorestframework-simplejwt)

API Docs: drf-yasg (Swagger UI & Redoc)

Containerization: Docker (optional)

🗄️ Database Schema
User
 ├── id, username, email, password, role
 └── roles: [ADMIN, EMPLOYER, APPLICANT]

Job
 ├── id, title, description, category, location, employer_id
 └── employer → User (role=EMPLOYER)

Application
 ├── id, job_id, applicant_id, status
 └── applicant → User (role=APPLICANT)

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/<your-username>/jobboard-backend-django.git
cd jobboard-backend-django

2. Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3. Setup Database (PostgreSQL)

Update settings.py with your DB credentials:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jobboard_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


Run migrations:

python manage.py migrate

4. Run the Development Server
python manage.py runserver


API available at: http://127.0.0.1:8000/api/

🔑 API Endpoints (Core)
Auth

POST /api/auth/register/ → Register user

POST /api/auth/login/ → Get JWT token

Jobs

GET /api/jobs/ → List jobs (with search & filters)

POST /api/jobs/ → Create job (Employer only)

GET /api/jobs/{id}/ → Retrieve job

PUT /api/jobs/{id}/ → Update job (Employer only)

DELETE /api/jobs/{id}/ → Delete job (Employer/Admin)

Applications

POST /api/jobs/{id}/apply/ → Apply for job (Applicant only)

GET /api/applications/ → View applications (Applicant → own, Employer → apps to their jobs)

PUT /api/applications/{id}/status/ → Update status (Employer/Admin)

📑 API Documentation

Interactive docs available at:

Swagger UI → /swagger/

Redoc → /redoc/

🧪 Testing

Run unit tests:

python manage.py test

📦 Deployment

(Optional section — fill if you deploy on Heroku, Render, or Docker.)

🙌 Acknowledgements

ALX ProDev Backend Engineering Program

Django REST Framework community

drf-yasg (Swagger UI)
