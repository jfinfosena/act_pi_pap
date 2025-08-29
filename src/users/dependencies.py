from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.users import service

def get_current_user_by_username(username: str, db: Session = Depends(get_db)):
    user = service.get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user
