from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app import models, schemas, auth
import random

router = APIRouter()

@router.get("/profile", response_model=schemas.UserOut)
def get_my_profile(current_user: models.User = Depends(auth.get_current_user)):
    return current_user

@router.get("/users", response_model=list[schemas.UserOut])
def list_users(current_user: models.User = Depends(auth.get_current_user),
                db: Session = Depends(auth.get_db),
                skip: int = 0,
                limit: int = 10,):
    return db.query(models.User)\
        .filter(models.User.id != current_user.id)\
        .offset(skip).limit(limit).all()

@router.get("/users/search", response_model=list[schemas.UserOut])
def search_users_by_name(q: str = Query(..., min_length=1),
                        current_user: models.User = Depends(auth.get_current_user),
                        db: Session = Depends(auth.get_db),
                        skip: int = 0,
                        limit: int = 10,):
    return db.query(models.User)\
        .filter(models.User.id != current_user.id)\
        .filter(models.User.name.like(f"%{q}%"))\
        .offset(skip).limit(limit).all()

@router.get("/suggestions", response_model=list[schemas.UserOut])
def suggest_users(
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(auth.get_db),
    limit: int = 5,
):
    all_users = db.query(models.User)\
            .filter(models.User.id != current_user.id)\
            .all()
    suggested = random.sample(all_users, min(limit, len(all_users)))
    return suggested