from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.mechanic import MechanicCreate, MechanicUpdate, MechanicResponse
from app.crud.crud_mechanic import CRUDMechanic
from app.db.session import get_db

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

