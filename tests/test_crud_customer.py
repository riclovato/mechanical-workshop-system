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
        email ="fulano@example.com",
        address = "rua exemplo",
        phone = "01255842545"
    )

    customer = crud.create(db_session, obj_in = customer_data)
    
    assert customer.id  is not None
    assert customer.name == "Fulano de Tal"
    assert customer.cpf == "12345678901"
    assert customer.address == "rua exemplo"
    assert customer.phone == "01255842545"

    new_data = CustomerUpdate(name = "Fulaninho de Tal")

    updated_customer = crud.update(db_session, db_obj=customer, obj_in= new_data)
    db_session.refresh(updated_customer)

    assert updated_customer.id  is not None
    assert updated_customer.name == "Fulaninho de Tal"
    assert updated_customer.cpf == "12345678901"
    assert customer.address == "rua exemplo"
    assert customer.phone == "01255842545"

def test_get_by_email(db_session: Session):
    crud = CRUDCustomer(Customer)

    customer_data = CustomerCreate(
        name = "Cliente Email teste",
        cpf = "999988877766",
        email = "emailteste@testeget.com",
        phone = "12345678901",
        address = "Rua do Email, 000"
    )
    created_customer = crud.create(db_session, obj_in = customer_data)

    found_customer = crud.get_by_email(db_session, email = "emailteste@testeget.com")

    assert found_customer is not None
    assert found_customer.id == created_customer.id
    assert found_customer.email == "emailteste@testeget.com"
    assert found_customer.name == "Cliente Email teste"

    non_existent_customer = crud.get_by_email(db_session, email = "nao.existe@example.com")
    
    assert non_existent_customer is None

def test_get_by_cpf(db_session: Session):
    crud = CRUDCustomer(Customer)

    customer_data = CustomerCreate(
        name = "Cliente CPF teste",
        cpf = "01234567890123",
        email = "emailteste@testeget.com",
        phone = "12345678901",
        address = "Rua do CPF, 000"
    )
    created_customer = crud.create(db_session, obj_in = customer_data)

    found_customer = crud.get_by_cpf(db_session, cpf = "01234567890123")

    assert found_customer is not None
    assert found_customer.id == created_customer.id
    assert found_customer.cpf == "01234567890123"
    assert found_customer.address == "Rua do CPF, 000"
    assert found_customer.name == "Cliente CPF teste"

    non_existent_customer = crud.get_by_cpf(db_session, cpf = "01234567890124")

    assert non_existent_customer is None
