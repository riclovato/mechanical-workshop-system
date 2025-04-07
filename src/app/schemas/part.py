from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from typing import TYPE_CHECKING


if TYPE_CHECKING:
     from .service_item import ServiceItemSimple


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


class PartSimple(BaseModel):
    
        id: int
        name: str
        code: str
        stock_quantity: int
        cost_price: float
        selling_price: float

class PartResponse(PartBase):
    
    service_items: List[ServiceItemSimple]

    model_config = ConfigDict(from_attributes=True)



