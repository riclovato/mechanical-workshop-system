from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.service_order import ServiceOrderCreate, ServiceOrderUpdate, ServiceOrderResponse
from app.crud.crud_service_order import CRUDServiceOrder
from app.db.session import get_db
from app.models.service_item import ServiceItem

router = APIRouter(prefix="/service_orders", tags=["service_orders"])

crud = CRUDServiceOrder()
not_found = "Service order not found"

@router.post("/", response_model=ServiceOrderResponse)
def create_service_order(service_order: ServiceOrderCreate, db: Session = Depends(get_db)):
    return crud.create(db, obj_in=service_order)

@router.get("/{service_order_id}", response_model=ServiceOrderResponse) 
def read_service_order(service_order_id: int, db: Session = Depends(get_db)):
    service_order = crud.get(db, service_order_id)
    if not service_order:
        raise HTTPException(status_code=404, detail=not_found)
    return service_order

@router.get("/", response_model=list[ServiceOrderResponse])
def read_service_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_multi(db, skip=skip, limit=limit)

@router.put("/{service_order_id}", response_model=ServiceOrderResponse)
def update_service_order(service_order_id: int, service_order: ServiceOrderUpdate, db: Session = Depends(get_db)):
    db_service_order = crud.get(db, service_order_id)
    if not db_service_order:
        raise HTTPException(status_code=404, detail=not_found)
    return crud.update(db, db_obj=db_service_order, obj_in=service_order)

@router.delete("/{service_order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service_order(service_order_id: int, db: Session = Depends(get_db)):
    db_service_order = crud.get(db, service_order_id)
    if not db_service_order:
        raise HTTPException(status_code=404, detail=not_found)
    
    has_items = db.query(ServiceItem).filter(
        ServiceItem.service_order_id == service_order_id
    ).first()
    if has_items:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Não é possível excluir a ordem de serviço pois existem itens de serviço vinculados a ela. Delete os itens primeiro ou cancele-os."
            )
    
    crud.remove(db, id=service_order_id)
    return None