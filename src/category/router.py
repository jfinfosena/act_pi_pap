from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.database import get_db
from . import services, schemas

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("/", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.get_categories(db, skip=skip, limit=limit)

@router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = services.get_category(db, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return services.create_category(db, category)
