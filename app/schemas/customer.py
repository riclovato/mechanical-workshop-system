from pydantic import BaseModel, EmailStr
from typing import Optional

#Schema base para Customer (usado para leitura)
class CustomerBase(BaseModel):
   
    id: int
    name: str
    cpf: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

    class Config:
        from_attributes = True # Habilita a compatibilidade com ORM (SQLAlchemy)

#Schema para criação de um Customer
class CustomerCreate(BaseModel):
    
    name: str
    cpf: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

#Schema para atualização de um Customer
class CustomerUpdate(BaseModel):

    name: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None


# Testando os schemas
if __name__ == "__main__":
    customer_data = {
        "name": "João Silva",
        "cpf" : "123.456.789-00",
        "email": "joao.silva@example.com",
        "phone": "(11)99999-9999",
        "address": "Rua Exemplo, 123"
    }

    customer_create = CustomerCreate(**customer_data)
    print("CustomerCreate:", customer_create)

    update_data = {
        "phone": "(11) 88888-8888",
        "email": "joao.novo@example.com"
    }

    customer_update = CustomerUpdate(**update_data)
    print("CustomerUpdate:", customer_update)