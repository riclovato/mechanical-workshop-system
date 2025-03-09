from sqlalchemy.orm import Session
from app.models import Customer
from app.crud import CRUDBase
from typing import Optional

class CRUDCustomer(CRUDBase):
    
    def get_by_email(self, db: Session, email: str) -> Optional[Customer]:
        return db.query(Customer).filter(Customer.email == email).first()
    
    def get_by_cpf(self, db: Session, cpf: str) -> Optional[Customer]:
        return db.query(Customer).filter(Customer.cpf == cpf).first()
    