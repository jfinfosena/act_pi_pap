from pydantic import BaseModel
from datetime import datetime

class SaleBase(BaseModel):
    car_id: int
    customer_name: str
    price: float

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
