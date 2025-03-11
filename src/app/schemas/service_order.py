from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .service_item import ServiceItemBase
    from .mechanic import MechanicBase

class ServiceOrderBase(BaseModel):

    id: int
    vehicle_id: int
    mechanic_id: int
    entry_date: datetime
    completion_date: Optional[datetime] = None
    total_value: float

    model_config = ConfigDict(from_attributes=True)

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

class ServiceOrderResponse(ServiceOrderBase):

    vehicle : "VehicleBase"
    mechanic: "MechanicBase"
    service_items: List["ServiceItemBase"]

    model_config = ConfigDict(from_attributes=True)


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