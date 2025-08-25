from sqlalchemy.orm import Session
from . import models, schemas

def get_sales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Sale).offset(skip).limit(limit).all()

def get_sale(db: Session, sale_id: int):
    return db.query(models.Sale).filter(models.Sale.id == sale_id).first()

def create_sale(db: Session, sale: schemas.SaleCreate):
    db_sale = models.Sale(
        car_id=sale.car_id,
        customer_name=sale.customer_name,
        price=sale.price
    )
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale
