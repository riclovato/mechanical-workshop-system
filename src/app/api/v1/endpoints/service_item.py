from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.service_item import ServiceItemCreate, ServiceItemUpdate, ServiceItemResponse
from app.crud.crud_service_item import CRUDServiceItem
from app.db.session import get_db

router = APIRouter(prefix="/service_items", tags=["service_items"])

crud_service_item = CRUDServiceItem()
not_found = "Service item not found"

@router.post("/", response_model=ServiceItemResponse)
def create_service_item(service_item: ServiceItemCreate, db: Session = Depends(get_db)):
    return crud_service_item.create(db, obj_in=service_item)

@router.get("/{service_item_id}", response_model=ServiceItemResponse)
def read_service_item(service_item_id: int, db: Session = Depends(get_db)):
    service_item = crud_service_item.get(db, service_item_id)
    if not service_item:
        raise HTTPException(status_code=404, detail=not_found)
    return service_item

@router.get("/", response_model=list[ServiceItemResponse])
def read_service_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_service_item.get_multi(db, skip=skip, limit=limit)

@router.put("/{service_item_id}", response_model=ServiceItemResponse)
def update_service_item(service_item_id: int, service_item: ServiceItemUpdate, db: Session = Depends(get_db)):
    db_service_item = crud_service_item.get(db, service_item_id)
    if not db_service_item:
        raise HTTPException(status_code=404, detail=not_found)
    return crud_service_item.update(db, db_obj=db_service_item, obj_in=service_item)

@router.delete("/{service_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service_item(service_item_id: int, db: Session = Depends(get_db)):
    db_service_item = crud_service_item.get(db, service_item_id)
    if not db_service_item:
        raise HTTPException(status_code=404, detail=not_found)
    crud_service_item.remove(db, id=service_item_id)
    return None