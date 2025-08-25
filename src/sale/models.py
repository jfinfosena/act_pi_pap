from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from src.core.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    amount = Column(Float)

    # Relación inversa con Car
    car = relationship("Car", back_populates="sales")
