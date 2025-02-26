from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import Base

class ServiceItem(Base):
    __tablename__ =  "service_items"

    id = Column (Integer, primary_key=True, index=True)
    service_order_id = Column(Integer, ForeignKey("service_orders.id"), nullable=False)
    part_id = Column(Integer, ForeignKey("parts.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_value = Column(Float, default=0.0)
    description = Column(String)

    service =  relationship("ServiceOrder", back_populates="service_items")
    part = relationship("Part", back_populates="service_items")

