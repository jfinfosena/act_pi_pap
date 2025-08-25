from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, index=True)
    year = Column(Integer, index=True)
    price = Column(Float)

    # Clave foránea hacia Category
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Relaciones
    category = relationship("Category", back_populates="cars")
    sales = relationship("Sale", back_populates="car")
