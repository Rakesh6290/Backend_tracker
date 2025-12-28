# Job Tracker – Backend

This repository contains the **backend** of the Job Tracker application.
The backend is built using **Django and Django REST Framework (DRF)** and provides REST APIs
consumed by a separate frontend application.

🌐 Live Backend API  
https://backend-tracker-bsxy.onrender.com

---

## 🚀 Tech Stack
- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Gunicorn
- Hosted on Render

---

## ✨ Features
- User authentication (JWT)
- User registration & login APIs
- Job application CRUD APIs
- Guest login support
- Secure API endpoints
- Django Admin panel
- PostgreSQL database integration

---

## 📂 Project Structure

backend/
│
├── manage.py
├── requirements.txt
│
├── job_tracker/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── apps/
│ ├── accounts/
│ │ ├── models.py
│ │ ├── views.py
│ │ ├── serializers.py
│ │ └── urls.py
│ │
│ └── jobs/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ └── urls.py
│
└── .env (not committed)


---

## 🔐 Authentication

The backend uses **JWT (JSON Web Tokens)** for authentication.

### Login API
POST /api/auth/login/

### Request Body
```json
{
  "username": "User1",
  "password": "Testing321"
}

Response
{
  "access": "jwt-access-token",
  "refresh": "jwt-refresh-token"
}

🔗 Frontend Integration

Frontend URL:

https://frontend-tracker-blue.vercel.app

CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "https://frontend-tracker-blue.vercel.app",
]

CSRF Configuration
CSRF_TRUSTED_ORIGINS = [
    "https://frontend-tracker-blue.vercel.app",
    "https://job_tracker.onrender.com",
]

Environment Variables

Set the following environment variables in Render Dashboard:

SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://username:password@host:port/dbname
ALLOWED_HOSTS=job_tracker.onrender.com

Local Setup
1️⃣ Clone Repository
git clone <backend-repo-url>
cd backend

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Migrations
python manage.py migrate

4️⃣ Create Superuser
python manage.py createsuperuser

5️⃣ Run Server
python manage.py runserver


Backend will run at:

http://127.0.0.1:8000/

🧑‍💻 Django Admin Panel
/admin/


Use superuser credentials created via createsuperuser.

🚀 Deployment

Platform: Render

Server: Gunicorn

Database: PostgreSQL

Auto deployment from GitHub main branch

❗ Important Notes

Frontend and backend are separate applications

Always use HTTPS in production

Ensure CORS & CSRF settings are correct

Production database is different from local database
