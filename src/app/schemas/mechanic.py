from __future__ import annotations
from pydantic import field_validator,ConfigDict  
from .base import BaseSchema
from typing import List
from app.schemas.custom_validator import validate_phone
from typing import TYPE_CHECKING
  
if TYPE_CHECKING:
    from .service_order import ServiceOrderSimple

class MechanicBase(BaseSchema):
    id: int
    name: str
    specialty: str
    phone: str
    available: bool

    @field_validator("phone")
    def validate_phone_field(cls, value: str) -> str:
        normalized = validate_phone(value)
        if not normalized:
            raise ValueError("Número Inválido.")
        return normalized

class MechanicCreate(BaseSchema):
    name: str
    specialty: str
    phone: str
    available: bool

class MechanicUpdate(BaseSchema):
    name: str | None = None
    specialty: str | None = None
    phone: str | None = None
    available: bool | None = None

class MechanicSimple(BaseSchema):
    id: int
    name: str
    specialty: str


class MechanicResponse(MechanicBase):
    service_orders: List["ServiceOrderSimple"] = []
    
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
         json_schema_extra={
        "exclude": {"service_orders": {"__all__": ["mechanic"]}} 
    }
    )
