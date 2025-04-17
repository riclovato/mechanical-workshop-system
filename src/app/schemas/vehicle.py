from __future__ import annotations
from pydantic import field_validator,ConfigDict  
from .base import BaseSchema
from typing import List
from .custom_validator import validate_license_plate

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .customer import CustomerSimple
    from .service_order import ServiceOrderSimple

class VehicleBase(BaseSchema):
    id: int
    license_plate: str
    brand: str
    model: str
    year: int
    customer_id: int

    @field_validator("license_plate")
    def license_plate_validator_field(cls, value: str) -> str:
        if not validate_license_plate(value):
            raise ValueError("Placa Inválida.")
        return value

class VehicleCreate(BaseSchema):
    license_plate: str
    brand: str | None = None
    model: str
    year: int | None = None
    customer_id: int

class VehicleUpdate(BaseSchema):
    license_plate: str | None = None
    brand: str | None = None
    model: str | None = None
    year: int | None = None
    customer_id: int | None = None

class VehicleSimple(BaseSchema):
    id: int
    license_plate: str
    brand: str 
    model: str 
 

class VehicleResponse(VehicleBase):
    owner: "CustomerSimple"
    service_orders: List["ServiceOrderSimple"] = []
    
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
          json_schema_extra={
        "exclude": {"owner": ["vehicles"]}  
    }
    )

