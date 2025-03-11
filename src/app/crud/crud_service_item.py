from sqlalchemy.orm import Session
from app.models.service_item import ServiceItem
from app.models.service_order import ServiceOrder
from app.models.part import Part
from app.crud.crud_base import CRUDBase
from app.schemas.service_item import ServiceItemCreate, ServiceItemUpdate
from typing import Optional

class CRUDServiceItem(CRUDBase[ServiceItem, ServiceItemCreate, ServiceItemUpdate]):

    def add_item_to_order(self, db: Session, service_order_id: int,
                          part_id: int, quantity: int, unit_value: float,
                          description: str) -> ServiceItem:
        
        service_order = db.query(ServiceOrder).get(service_order_id)
        if not service_order:
            raise ValueError(f"Ordem de serviço {service_order_id} não encontrada")
        
        part = db.query(Part).get(part_id)
        if not part:
            raise ValueError(f"Peça {part_id} não encontrada")
        
        service_item = ServiceItem(
            service_order_id = service_order_id,
            part_id = part_id,
            quantity = quantity,
            unit_value = unit_value,
            description = description)

        db.add(service_item)
        db.commit()
        db.refresh(service_item)

        return service_item