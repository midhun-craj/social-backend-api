# FastAPI Social Backend API

A lightweight, production-grade social backend API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. Supports user authentication, profile management, friend requests, and JWT-based protected routes.

---

## 🚀 Features

- User registration and login with JWT
- Secure password hashing
- Auth-protected routes
- Friend request system (send, accept, reject)
- Friends listing
- Alembic-powered database migrations
- Fully containerized using Docker and Docker Compose
- Async unit testing with `httpx` and `pytest`

---

## 📦 Tech Stack

- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Alembic**
- **Docker & Docker Compose**
- **Pytest + httpx** for async testing

---

## 🛠️ Project Structure

social-backend-api/  
├── app/ # Application source code  
│ ├── init.py # Init file for app package  
│ ├── main.py # FastAPI app instance and routing  
│ ├── database.py # Database connection and session setup  
│ ├── models.py # SQLAlchemy database models  
│ ├── schemas.py # Pydantic models for request/response validation <br>
│ ├── auth.py # Authentication logic (JWT, login, register) <br>
│ ├── friends.py # Friend request and action endpoints <br>
│ └── utils.py # Utility functions (password hashing, token creation) <br>
├── alembic/ # Alembic migrations directory <br>
│ ├── versions/ # Migration versions <br>
│ ├── env.py # Alembic environment setup <br>
│ └── script.py.mako # Template for Alembic scripts <br>
├── tests/ # Unit tests <br>
│ ├── test_main.py # Tests for all the code <br>
├── Dockerfile # Dockerfile for building the app container <br>
├── docker-compose.yml # Docker Compose file for setting up app and database <br>
├── .env # Environment variables configuration <br>
├── requirements.txt # Python dependencies <br>
└── README.md # This README file <br>

---

## 📦 Setup Instructions

### 1. 📁 Clone the repository

```bash
git clone https://github.com/midhun-craj/social-backend-api.git
cd social-backend-api
```

### 2. Create a venv

```bash
python -m venv venv
source venv/bin/activate -> mac
venv\bin\activate -> windows
deactivate -> to deactivate the venv
```

### 3. 🐳 Run the project

```bash
BUILDKIT=1 COMPOSE_BAKE=true docker compose up --build -d
```

## 🗄️ Database Migrations

```bash
docker-compose exec backend-service alembic revision --autogenerate -m "your message"
docker-compose exec api alembic upgrade head
```

### for the sake of this project i didn't gitignored the .env file.

## 🧪 Run Tests

```bash
docker-compose exec pytest test/
````

## 📮 API Endpoints Overview
### Auth
-> POST /auth/register — Register a new user

-> POST /auth/login — Login and get JWT token

### Users
-> GET /users — List all users

-> GET /users/search?q= — Search by name

-> GET /profile — Get current user info

### Friends
-> POST /friends/request — Send a friend request

-> POST /friends/action — Accept or reject a friend request

-> GET /friends — List all friends

## ✅ Requirements

These are all the dependencies
```bash
alembic==1.15.2
annotated-types==0.7.0
anyio==4.9.0
bcrypt==4.3.0
certifi==2025.1.31
click==8.1.8
dnspython==2.7.0
ecdsa==0.19.1
email_validator==2.2.0
exceptiongroup==1.2.2
fastapi==0.115.12
h11==0.14.0
httpcore==1.0.8
httpx==0.28.1
idna==3.10
iniconfig==2.1.0
Mako==1.3.10
MarkupSafe==3.0.2
packaging==25.0
passlib==1.7.4
pluggy==1.5.0
psycopg2-binary==2.9.10
pyasn1==0.4.8
pydantic==2.11.3
pydantic_core==2.33.1
pytest==8.3.5
pytest-asyncio==0.26.0
python-dotenv==1.1.0
python-jose==3.4.0
python-multipart==0.0.20
rsa==4.9.1
six==1.17.0
sniffio==1.3.1
SQLAlchemy==2.0.40
starlette==0.46.2
tomli==2.2.1
typing-inspection==0.4.0
typing_extensions==4.13.2
uvicorn==0.34.2
```

Install locally (if not using Docker):
```bash
pip install -r requirements.txt
```

### 🧼 Shutdown

```bash
docker compose down
```







