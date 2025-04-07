from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from typing import Optional, TYPE_CHECKING
from .service_order import ServiceOrderSimple  
from .part import PartSimple  

if TYPE_CHECKING:
    from .service_order import ServiceOrderSimple  
    from .part import PartSimple  


class ServiceItemBase(BaseModel):

    id: int
    service_order_id: int
    part_id: int
    quantity: int
    unit_value: float
    description: str

    model_config = ConfigDict(from_attributes=True)

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

class ServiceItemSimple(BaseModel):
    id: int
    quantity: int
    unit_value: float
    description: str
    part_id: int


class ServiceItemResponse(ServiceItemBase):

    service_order: "ServiceOrderSimple"
    part: "PartSimple"

    model_config = ConfigDict(from_attributes=True)

