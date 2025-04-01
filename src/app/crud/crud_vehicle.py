from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.vehicle import VehicleCreate, VehicleUpdate
from app.models import Vehicle, ServiceOrder
from app.models import Customer
from app.crud.crud_base import CRUDBase
from typing import Optional, List
from fastapi import HTTPException, status

class CRUDVehicle(CRUDBase[Vehicle, VehicleCreate, VehicleUpdate]):
    def __init__(self):
        super().__init__(model=Vehicle)
    
    def get_by_license_plate(self, db: Session, license_plate: str) -> Optional[Vehicle]:
        return db.query(Vehicle).filter(Vehicle.license_plate == license_plate).first()
    
    def get_by_customer(self, db: Session, customer_id: int) -> List[Vehicle]:
        return db.query(Vehicle).filter(Vehicle.customer_id == customer_id).all()
    
    def remove(self, db: Session, id: int) -> None:
        "Sobrescreve o método remove para verificar ordens de serviço vinculadas"
        vehicle = self.get(db,id)
        if not vehicle:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail = "Veículo não encontrado"
            )
        if db.query(ServiceOrder).filter(ServiceOrder.vehicle_id == id).first():
            raise HTTPException(
                status_code= status.HTTP_400_BAD_REQUEST,
                detail="Não é possível deletar: veículo possui ordens de serviço ativas"
            )
        
        try:
            db.delete(vehicle)
            db.commit()
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Erro ao deletar veículo: {str(e)}"
            )

