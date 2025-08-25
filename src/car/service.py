from sqlalchemy.orm import Session
from src.car.models import Car as CarModel
from src.car.schemas import CarCreate

# Obtener todos
def get_cars(db: Session):
    return db.query(CarModel).all()

# Obtener por ID
def get_car(db: Session, car_id: int):
    return db.query(CarModel).filter(CarModel.id == car_id).first()

# Crear
def create_car(db: Session, car: CarCreate):
    db_car = CarModel(
        brand=car.brand,
        model=car.model,
        year=car.year,
        price=car.price,
        available=car.available
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

# Actualizar
def update_car(db: Session, car_id: int, car: CarCreate):
    db_car = get_car(db, car_id)
    if db_car:
        db_car.brand = car.brand
        db_car.model = car.model
        db_car.year = car.year
        db_car.price = car.price
        db_car.available = car.available
        db.commit()
        db.refresh(db_car)
    return db_car

# Eliminar
def delete_car(db: Session, car_id: int):
    db_car = get_car(db, car_id)
    if db_car:
        db.delete(db_car)
        db.commit()
    return db_car
