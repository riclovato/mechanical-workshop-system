from __future__ import annotations
from pydantic import BaseModel, field_validator, ConfigDict
from typing import Optional,List, TYPE_CHECKING
from .custom_validator import validate_license_plate
if TYPE_CHECKING:
    from .customer import CustomerBase  # Importação apenas para type checking

class VehicleBase(BaseModel):
    
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

    model_config = ConfigDict(from_attributes=True)


class VehicleCreate(BaseModel):
   
    license_plate: str
    brand: Optional[str] = None
    model: str
    year: Optional[int] = None
    customer_id: int

class VehicleUpdate(BaseModel):
   
    license_plate: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    customer_id: Optional[int] = None

class VehicleResponse(VehicleBase):
    owner: "CustomerBase"
    service_orders: List[ServiceOrderBase]

    model_config = ConfigDict(from_attributes=True)


if __name__ == "__main__":
    # Dados para criação de um Vehicle
    vehicle_data = {
        "license_plate": "ABC-1234",
        "model": "Corolla",
        "customer_id": 1
    }

    # Criando um objeto VehicleCreate
    vehicle_create = VehicleCreate(**vehicle_data)
    print("VehicleCreate:", vehicle_create)

    # Dados para atualização de um Vehicle
    update_data = {
        "license_plate": "XYZ-5678",
        "year": 2021
    }

    # Criando um objeto VehicleUpdate
    vehicle_update = VehicleUpdate(**update_data)
    print("VehicleUpdate:", vehicle_update)