from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.car.schemas import Car, CarCreate
from src.car import services as car_service

router = APIRouter(prefix="/cars", tags=["Cars"])

# Listar todos
@router.get("/", response_model=list[Car])
def read_cars(db: Session = Depends(get_db)):
    return car_service.get_cars(db)

# Obtener uno
@router.get("/{car_id}", response_model=Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = car_service.get_car(db, car_id)
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

# Crear
@router.post("/", response_model=Car)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    return car_service.create_car(db, car)

# Actualizar
@router.put("/{car_id}", response_model=Car)
def update_car(car_id: int, car: CarCreate, db: Session = Depends(get_db)):
    db_car = car_service.update_car(db, car_id, car)
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

# Eliminar
@router.delete("/{car_id}", response_model=Car)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = car_service.delete_car(db, car_id)
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car
