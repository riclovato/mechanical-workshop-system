from pydantic import BaseModel
from typing import Optional

class ServiceItemBase(BaseModel):

    id: int
    service_order_id: int
    part_id: int
    quantity: int
    unit_value: float
    description: str

    class Config:
        from_attributes = True

class ServiceItemCreate(BaseModel):

    service_order_id: int
    part_id: int
    quantity: int
    unit_value: float
    description: Optional[str] = None

class ServiceItemUpdate(BaseModel):

    service_order_id: Optional[int] = None
    part_id: Optional[int] = None
    quantity: Optional[int] = None
    unit_value: Optional[float] = None
    description: Optional[str] = None


if __name__ == "__main__":
    # Dados para criação de um ServiceItem
    service_item_data = {
        "service_order_id": 1,
        "part_id": 1,
        "quantity": 2,
        "unit_value": 10.50,
        "description": "Parafuso de fixação"
    }

    # Criando um objeto ServiceItemCreate
    service_item_create = ServiceItemCreate(**service_item_data)
    print("ServiceItemCreate:", service_item_create)

    # Dados para atualização de um ServiceItem
    update_data = {
        "quantity": 3,
        "unit_value": 12.00
    }

    # Criando um objeto ServiceItemUpdate
    service_item_update = ServiceItemUpdate(**update_data)
    print("ServiceItemUpdate:", service_item_update)