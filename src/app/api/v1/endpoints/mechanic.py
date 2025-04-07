from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.mechanic import MechanicCreate, MechanicUpdate, MechanicResponse
from app.crud.crud_mechanic import CRUDMechanic
from app.db.session import get_db
from typing import List

router = APIRouter(prefix="/mechanics", tags=["mechanics"])

crud_mechanic = CRUDMechanic()
NOT_FOUND = "Mechanic not found"

@router.post("/", response_model=MechanicResponse)
def create_mechanic(mechanic: MechanicCreate, db: Session = Depends(get_db)):
    return crud_mechanic.create(db, obj_in = mechanic)

@router.get("/{mechanic_id}", response_model=MechanicResponse)
def read_mechanic(mechanic_id: int, db: Session = Depends(get_db)):
    mechanic = crud_mechanic.get(db, mechanic_id)
    if not mechanic:
        raise HTTPException(status_code=404, detail=NOT_FOUND)
    return mechanic

@router.get("/", response_model=List[MechanicResponse])
def read_mechanics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_mechanic.get_multi(db, skip=skip, limit=limit)

@router.put("/{mechanic_id}", response_model=MechanicResponse)
def update_mechanic(mechanic_id: int, mechanic: MechanicUpdate, db: Session = Depends(get_db)):
    db_mechanic = crud_mechanic.get(db, mechanic_id)
    if not db_mechanic:
        raise HTTPException(status_code=404, detail=NOT_FOUND)
    return crud_mechanic.update(db, db_obj=db_mechanic, obj_in=mechanic)

@router.delete("/{mechanic_id}", response_model=MechanicResponse)
def delete_mechanic(mechanic_id: int, db: Session = Depends(get_db)):
    db_mechanic = crud_mechanic.get(db, mechanic_id)
    if not db_mechanic:
        raise HTTPException(status_code=404, detail=NOT_FOUND)
    return crud_mechanic.remove(db, id=mechanic_id)
