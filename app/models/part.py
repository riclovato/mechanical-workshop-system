from sqlalchemy import Column, String, Integer,Float
from sqlalchemy.orm import relationship
from app.db.base import Base

class Part(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String,unique=True, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    cost_price =  Column(Float, nullable=False)
    selling_price = Column(Float, nullable=False)

    service_items = relationship("ServiceItem", back_populates="parts")
