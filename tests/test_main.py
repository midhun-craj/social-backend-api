import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
import asyncio

# Base.metadata.create_all(bind=engine)

@pytest.mark.asyncio
async def test_register_and_login():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.post("/auth/register", json={
            "name": "Alice",
            "email": "alice@example.com",
            "password": "secure123"
        })
        assert res.status_code == 200
        data = res.json()
        assert "access_token" in data

        res = await ac.post("/auth/login", json={
            "email": "alice@example.com",
            "password": "secure123"
        })
        assert res.status_code == 200
        token = res.json()["access_token"]
        assert token is not None

        headers = {"Authorization": f"Bearer {token}"}

        res = await ac.get("/profile", headers=headers)
        assert res.status_code == 200
        assert res.json()["email"] == "alice@example.com"

@pytest.mark.asyncio
async def test_user_list_and_search():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        await ac.post("/auth/register", json={
            "name": "Bob",
            "email": "bob@example.com",
            "password": "secure123"
        })
        login = await ac.post("/auth/login", json={
            "email": "bob@example.com",
            "password": "secure123"
        })
        token = login.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        res = await ac.get("/users", headers=headers)
        assert res.status_code == 200
        assert isinstance(res.json(), list)

        res = await ac.get("/users/search?q=Ali", headers=headers)
        assert res.status_code == 200
        assert any("Alice" in user["name"] for user in res.json())

@pytest.mark.asyncio
async def test_friend_request_flow():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        
        await ac.post("/auth/register", json={
            "name": "Charlie",
            "email": "charlie@example.com",
            "password": "secure123"
        })
        login = await ac.post("/auth/login", json={
            "email": "charlie@example.com",
            "password": "secure123"
        })
        token = login.json()["access_token"]
        charlie_headers = {"Authorization": f"Bearer {token}"}

        res = await ac.get("/users", headers=headers)
        alice = next(user for user in res.json() if user["name"] == "Alice")

        res = await ac.post(f"/friends/request/", json={
            "receiver_id": alice[id]
        }, headers=headers)
        assert res.status_code == 200 or res.status_code == 201

        res = await ac.get("/")

        login = await ac.post("/auth/login", json={
            "email": "alice@example.com",
            "password": "secure123"
        })
        token = login.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        res = await ac.post(f"/friends/respond/{alice['id']}", params={"accept": True}, headers=headers)
        assert res.status_code == 200

        res = await ac.get("/friends", headers=headers)
        assert res.status_code == 200
        assert any(friend["name"] == "Charlie" for friend in res.json())
