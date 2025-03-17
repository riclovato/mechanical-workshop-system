from sqlalchemy.orm import Session
from app.models import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate
from app.crud.crud_base import CRUDBase
from typing import Optional

class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):
    
    def __init__(self):
        # Passa o modelo Customer para a classe base
        super().__init__(model=Customer)  
    
    def get_by_email(self, db: Session, email: str) -> Optional[Customer]:
        return db.query(Customer).filter(Customer.email == email).first()
    
    def get_by_cpf(self, db: Session, cpf: str) -> Optional[Customer]:
        return db.query(Customer).filter(Customer.cpf == cpf).first()
    