from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.products import models, schemas

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=schemas.ProductRead)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=list[schemas.ProductRead])
def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()
