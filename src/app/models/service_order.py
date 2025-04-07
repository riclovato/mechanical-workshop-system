from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy import DateTime
from enum import Enum as PyEnum
from sqlalchemy import Enum

class ServiceOrderStatus(PyEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class ServiceOrder(Base):
    __tablename__= "service_orders"
   
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    mechanic_id = Column(Integer, ForeignKey("mechanics.id"), nullable=False)
    status = Column(Enum(ServiceOrderStatus), default = ServiceOrderStatus.PENDING)
    entry_date = Column (DateTime)
    completion_date = Column(DateTime)
    total_value = Column (Float, default=0.0)
 
    vehicle = relationship("Vehicle", back_populates="service_orders", lazy="select")
    mechanic = relationship("Mechanic", back_populates="service_orders", lazy="select")
    items = relationship("ServiceItem", back_populates="service_order", lazy="select")