from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from .service_item import ServiceItemBase

class PartBase(BaseModel):
   
    id: int
    name: str
    code: str
    stock_quantity: int
    cost_price: float
    selling_price: float

    model_config = ConfigDict(from_attributes=True)

class PartCreate(BaseModel):
    
    name: str
    code: str
    stock_quantity: int
    cost_price: float
    selling_price: float

class PartUpdate(BaseModel):
   
    name: Optional[str] = None
    code: Optional[str] = None
    stock_quantity: Optional[int] = None
    cost_price: Optional[float] = None
    selling_price: Optional[float] = None

class PartResponse(PartBase):
    
    service_items: List[ServiceItemBase]

    model_config = ConfigDict(from_attributes=True)


if __name__ == "__main__":
    # Dados para criação de uma Part
    part_data = {
        "name": "Parafuso",
        "code": "PRF-001",
        "stock_quantity": 100,
        "cost_price": 0.50,
        "selling_price": 1.00
    }

    # Criando um objeto PartCreate
    part_create = PartCreate(**part_data)
    print("PartCreate:", part_create)

    # Dados para atualização de uma Part
    update_data = {
        "stock_quantity": 150,
        "selling_price": 1.20
    }

    # Criando um objeto PartUpdate
    part_update = PartUpdate(**update_data)
    print("PartUpdate:", part_update)