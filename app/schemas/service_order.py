from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ServiceOrderBase(BaseModel):

    id: int
    vehicle_id: int
    mechanic_id: int
    entry_date: datetime
    completion_date: Optional[datetime] = None
    total_value: float

    class Config:
        from_attributes = True

class ServiceOrderCreate(BaseModel):

    vehicle_id: int
    mechanic_id: int
    entry_date: datetime
    completion_date: Optional[datetime] = None
    total_value: float

class ServiceOrderUpdate(BaseModel):
    vehicle_id: Optional[int] = None
    mechanic_id: Optional[int] = None
    entry_date: Optional[datetime] = None
    completion_date: Optional[datetime] = None
    total_value: Optional[float] = None


if __name__ == "__main__":
    # Dados para criação de uma ServiceOrder
    service_order_data = {
        "vehicle_id": 1,
        "mechanic_id": 1,
        "entry_date": datetime.now(),
        "total_value": 500.0
    }

    # Criando um objeto ServiceOrderCreate
    service_order_create = ServiceOrderCreate(**service_order_data)
    print("ServiceOrderCreate:", service_order_create)

    # Dados para atualização de uma ServiceOrder
    update_data = {
        "completion_date": datetime.now(),
        "total_value": 550.0
    }

    # Criando um objeto ServiceOrderUpdate
    service_order_update = ServiceOrderUpdate(**update_data)
    print("ServiceOrderUpdate:", service_order_update)