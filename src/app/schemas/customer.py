from __future__ import annotations
from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
from typing import Optional, List, TYPE_CHECKING
from .custom_validator import validate_cpf, validate_email, validate_phone  # Importação relativa
if TYPE_CHECKING:
    from .vehicle import VehicleBase  # Importação apenas para type checking

#Schema base para Customer (usado para leitura)
class CustomerBase(BaseModel):
   
    id: int
    name: str
    cpf: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

    @field_validator("cpf")
    def validate_cpf_field(cls, value: str) -> str:
        if not validate_cpf(value):
            raise ValueError("CPF inválido.")
        return value
    
    @field_validator("email")
    def validate_email_field(cls, value: EmailStr) -> EmailStr:
        if not validate_email(value):
            raise ValueError("Email Inválido.")
        return value
    
    @field_validator("phone")
    def validate_phone_field(cls, value: str) -> str:
        if not validate_phone(value):
            raise ValueError("Número Inválido.")
        return value


    model_config = ConfigDict(from_attributes=True)
        


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

class CustomerResponse(CustomerBase):  # Herda de CustomerBase
    vehicles: List["VehicleBase"] # Adiciona a lista de veículos
        
    model_config = ConfigDict(from_attributes=True)

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