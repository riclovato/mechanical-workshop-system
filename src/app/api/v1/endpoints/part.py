from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.part import PartCreate, PartUpdate, PartResponse
from app.crud.crud_part import CRUDPart
from app.db.session import get_db

router = APIRouter(prefix="/parts", tags=["parts"])
crud_part = CRUDPart()

@router.post("/", response_model=PartResponse)
def create_part(part: PartCreate, db: Session = Depends(get_db)):
    return crud_part.create(db, obj_in=part)

@router.get("/{part_id}", response_model=PartResponse)
def read_part(part_id: int, db: Session = Depends(get_db)):
    part = crud_part.get(db, part_id)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    return part

@router.get("/", response_model=list[PartResponse])
def read_parts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_part.get_multi(db, skip=skip, limit=limit)

@router.put("/{part_id}", response_model=PartResponse)
def update_part(part_id: int, part: PartUpdate, db: Session = Depends(get_db)):
    db_part = crud_part.get(db, part_id)
    if not db_part:
        raise HTTPException(status_code=404, detail="Part not found")
    return crud_part.update(db, db_obj=db_part, obj_in=part)

@router.delete("/{part_id}", response_model=PartResponse)
def delete_part(part_id: int, db: Session = Depends(get_db)):
    db_part = crud_part.get(db, part_id)
    if not db_part:
        raise HTTPException(status_code=404, detail="Part not found")
    crud_part.remove(db, id=part_id)
    return None