from __future__ import annotations
from datetime import datetime
from typing import List
from .base import BaseSchema
from pydantic import ConfigDict  
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vehicle import VehicleSimple
    from .mechanic import MechanicSimple

class ServiceOrderBase(BaseSchema):
    id: int
    vehicle_id: int
    mechanic_id: int
    entry_date: datetime
    completion_date: datetime | None = None
    total_value: float

class ServiceOrderCreate(BaseSchema):
    vehicle_id: int
    mechanic_id: int
    entry_date: datetime
    completion_date: datetime | None = None
    total_value: float

class ServiceOrderUpdate(BaseSchema):
    vehicle_id: int | None = None
    mechanic_id: int | None = None
    entry_date: datetime | None = None
    completion_date: datetime | None = None
    total_value: float | None = None

class ServiceOrderSimple(BaseSchema):
    id: int
    entry_date: datetime
    completion_date: datetime | None = None 
  

class ServiceOrderResponse(ServiceOrderBase):
    vehicle: "VehicleSimple"
    mechanic: "MechanicSimple"
    
    model_config = ConfigDict(
    from_attributes=True,
    populate_by_name=True,
    json_schema_extra={
        "exclude": {
            "vehicle": ["service_orders", "owner"],  
            "mechanic": ["service_orders"]  
    }
    }
)


