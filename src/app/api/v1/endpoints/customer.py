from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.customer import CustomerCreate, CustomerResponse, CustomerUpdate
from app.crud.crud_customer import CRUDCustomer
from app.db.session import get_db

router = APIRouter(prefix="/customers", tags=["customers"])

crud_customer = CRUDCustomer()

@router.post("/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return crud_customer.create(db, obj_in = customer)


@router.get("/{customer_id}", response_model=CustomerResponse)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud_customer.get(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.get("/", response_model= List[CustomerResponse])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_customer.get_multi(db, skip=skip, limit=limit)


@router.put("/{customer_id}", response_model = CustomerResponse)
def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer =  crud_customer.get(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return crud_customer.update(db, db_obj = db_customer, obj_in = customer)

@router.delete("/{customer_id}", response_model = CustomerResponse)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud_customer.get(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail = "Customer not found")
    return crud_customer.remove(db, id=customer_id)
