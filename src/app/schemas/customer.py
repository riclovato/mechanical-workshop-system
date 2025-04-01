from __future__ import annotations
from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
from typing import Optional, List, TYPE_CHECKING
from .custom_validator import validate_cpf, validate_email, validate_phone  # Importação relativa
if TYPE_CHECKING:
    from .vehicle import VehicleBase  # Importação apenas para type checking
import re

#Schema base para Customer (usado para leitura)
class CustomerBase(BaseModel):
   
    id: int
    name: str
    cpf: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

    @field_validator("cpf")
    def validate_cpf(cls, v):
        if not re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", v):
            raise ValueError("Formato de CPF inválido. Use XXX.XXX.XXX-XX")
        return v
    
    @field_validator("email")
    def validate_email(cls, v):
        if "@example.com" not in v:  
            raise ValueError("Email deve pertencer ao domínio example.com")
        return v
    
    @field_validator("phone")
    def validate_phone(cls, v):
        # Aceita formatos como (11) 98888-8888 ou 11 988888888
        if not re.match(r"^\(\d{2}\) \d{5}-\d{4}$", v):
            raise ValueError("Formato inválido. Use (XX) XXXXX-XXXX")
        return v


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

class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True

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