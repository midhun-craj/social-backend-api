from fastapi import FastAPI
from app import auth, users, friends, health, database, models

# models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(friends.router)
app.include_router(health.router)