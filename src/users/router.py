from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.users import schemas, service
from src.core.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)

@router.get("/", response_model=List[schemas.UserRead])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service.get_users(db, skip=skip, limit=limit)
