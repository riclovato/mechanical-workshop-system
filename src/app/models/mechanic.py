from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class Mechanic(Base):
    __tablename__ = "mechanics"

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty =  Column(String)
    phone = Column(String, nullable=False)
    available = Column(Boolean, default=True)

    service_orders = relationship("ServiceOrder", back_populates="mechanic", lazy="select")