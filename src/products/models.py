from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from src.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)

    reviews = relationship("Review", back_populates="product")
