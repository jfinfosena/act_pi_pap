from pydantic import BaseModel
from typing import Optional

# Esquema para crear/actualizar carros
class CarCreate(BaseModel):
    brand: str
    model: str
    year: int
    price: float
    available: Optional[bool] = True

# Esquema de respuesta
class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    price: float
    available: bool

    class Config:
        orm_mode = True
