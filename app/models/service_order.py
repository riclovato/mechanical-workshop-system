from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy import DateTime

class ServiceOrder(Base):
    __tablename__= "service_orders"
   
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    mechanic_id = Column(Integer, ForeignKey("mechanics.id"), nullable=False)
    entry_date = Column (DateTime)
    completion_date = Column(DateTime)
    total_value = Column (Float, default=0.0)
 
    vehicle = relationship("Vehicle", back_populates="service_orders")
    mechanic = relationship("Mechanic", back_populates="service_orders")
    items = relationship("ServiceItem", back_populates="service_order")
