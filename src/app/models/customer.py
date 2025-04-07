from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Customer(Base):
    __tablename__ = "customers"
   
    id = Column(Integer, primary_key=True, index= True)
    name = Column(String, nullable=False)
    cpf =  Column(String(14), unique=True, nullable=False) # CPF com formatação (XXX.XXX.XXX-XX)
    phone = Column(String)
    email = Column(String, unique=True)
    address = Column(String)

    vehicles = relationship("Vehicle", back_populates="owner", lazy="select")