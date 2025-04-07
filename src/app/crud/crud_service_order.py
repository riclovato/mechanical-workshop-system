from sqlalchemy.orm import Session
from app.models.service_order import ServiceOrder
from app.crud.crud_base import CRUDBase
from app.schemas.service_order import ServiceOrderCreate, ServiceOrderUpdate
from typing import Optional

class CRUDServiceOrder(CRUDBase[ServiceOrder, ServiceOrderCreate, ServiceOrderUpdate]):
    def __init__(self):  
        super().__init__(model=ServiceOrder) 


    def update_status(self, db: Session, service_order_id: int, new_status: str) -> Optional[ServiceOrder]:
        allowed_statuses = {"pending", "in_progress", "completed", "cancelled"}
        if new_status not in allowed_statuses:
            raise ValueError(f"Status Inválido: {new_status}. Status Permitidos: {allowed_statuses}")
        
        service_order = self.get(db, service_order_id)
        if service_order:
            service_order.status = new_status
            db.commit()
            db.refres(service_order)
        return service_order
    

   

    def calculate_total(self, db: Session, service_order_id: int) -> Optional[ServiceOrder]:

        service_order = self.get(db, service_order_id)
        if service_order:
            total = 0
            # calcula total somando (quantidade * valor unitário) de cada item 
            for item in service_order.service_items:
                total += item.quantity * item.unit_value
            service_order.total_value = total
            db.commit()
            db.refresh(service_order)

        return service_order