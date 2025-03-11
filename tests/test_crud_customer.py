import pytest
from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.crud.crud_customer import CRUDCustomer
from app.schemas.customer import CustomerCreate, CustomerUpdate

def test_create_customer(db_session: Session):
    crud = CRUDCustomer(Customer)
    customer_data = CustomerCreate(
        name = "Fulano de Tal",
        cpf = "12345678901",
        email ="fulano@example.com"
    )

    customer = crud.create(db_session, obj_in = customer_data)
    
    assert customer.id  is not None
    assert customer.name == "Fulano de Tal"
    assert customer.cpf == "12345678901"

