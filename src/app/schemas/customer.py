from __future__ import annotations
from .base import BaseSchema
from pydantic import EmailStr, field_validator, ConfigDict
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .vehicle import VehicleSimple 
import re


# Base schema for Customer data with common fields and validations.
class CustomerBase(BaseSchema):
   
    id: int
    name: str
    cpf: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    
    
    # Validates phone format (e.g., (11) 98888-8888 or 11 988888888).
    @field_validator("cpf")
    def validate_cpf(cls, v):
        if not re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", v):
            raise ValueError("Formato de CPF inválido. Use XXX.XXX.XXX-XX")
        return v
    # Ensures email belongs to @example.com domain.
    @field_validator("email")
    def validate_email(cls, v):
        if "@example.com" not in v:  
            raise ValueError("Email deve pertencer ao domínio example.com")
        return v
    

    # Validates phone format (e.g., (11) 98888-8888 or 11 988888888).
    @field_validator("phone")
    def validate_phone(cls, v):
        if not re.match(r"^\(\d{2}\) \d{5}-\d{4}$", v):
            raise ValueError("Formato inválido. Use (XX) XXXXX-XXXX")
        return v

    # Enable ORM mode to allow loading from database models
    model_config = ConfigDict(from_attributes=True)
        


# Schema for creating a new Customer (excludes auto-generated fields like 'id')
class CustomerCreate(BaseSchema):
    
    name: str
    cpf: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

# Schema for updating Customer fields (all fields optional)
class CustomerUpdate(BaseSchema):

    name: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

# Simplified schema for customer to avoid circular references
# This is used in the Vehicle and ServiceOrder schemas to avoid circular references specifically
class CustomerSimple(BaseSchema):
    id: int
    name: str
    cpf: str

class CustomerResponse(CustomerBase):
    vehicles: List["VehicleSimple"] = []    # List of simplified Vehicle objects
    
    # Configuration to exclude sensitive/irrelevant fields from nested Vehicle objects
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
       json_schema_extra={
        "exclude": {"vehicles": {"__all__": ["owner", "service_orders"]}} 
    }
    )

