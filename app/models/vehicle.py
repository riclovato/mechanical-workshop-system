from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Vehicle(Base):
    __tablename__ ="vehicles"

    id = Column(Integer, primary_key=True, index=True)
    license_plate = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    owner =  relationship("Customer", back_populates="vehicles")

