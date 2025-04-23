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

social-backend-api/ <br>
├── app/ # Application source code <br>
│ ├── init.py # Init file for app package <br>
│ ├── main.py # FastAPI app instance and routing <br>
│ ├── database.py # Database connection and session setup <br>
│ ├── models.py # SQLAlchemy database models <br>
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
