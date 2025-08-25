from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.database import get_db
from . import services, schemas

router = APIRouter(
    prefix="/sales",
    tags=["sales"]
)

@router.get("/", response_model=list[schemas.Sale])
def read_sales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.get_sales(db, skip=skip, limit=limit)

@router.get("/{sale_id}", response_model=schemas.Sale)
def read_sale(sale_id: int, db: Session = Depends(get_db)):
    db_sale = services.get_sale(db, sale_id)
    if not db_sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale

@router.post("/", response_model=schemas.Sale)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return services.create_sale(db, sale)
