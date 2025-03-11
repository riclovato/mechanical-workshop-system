from sqlalchemy.orm import Session
from app.schemas.vehicle import VehicleCreate, VehicleUpdate
from app.models import Vehicle
from app.models import Customer
from app.crud.crud_base import CRUDBase
from typing import Optional, List

class CRUDVehicle(CRUDBase[Vehicle, VehicleCreate, VehicleUpdate]):
    
    def get_by_license_plate(self, db: Session, license_plate: str) -> Optional[Vehicle]:
        return db.query(Vehicle).filter(Vehicle.license_plate == license_plate).first()
    
    def get_by_customer(self, db: Session, customer_id: int) -> List[Vehicle]:
        return db.query(Vehicle).filter(Vehicle.customer_id == customer_id).all()
    

