from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.vehicle import VehicleCreate, VehicleUpdate, VehicleResponse
from app.crud.crud_vehicle import CRUDVehicle
from app.db.session import get_db

router = APIRouter(prefix="/vehicles", tags=["vehicles"])

crud_vehicle = CRUDVehicle()
not_found =  "Vehicle not found"

@router.post("/", response_model=VehicleResponse)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return crud_vehicle.create(db, obj_in = vehicle)

@router.get("/{vehicle_id}", response_model=VehicleResponse)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = crud_vehicle.get(db, vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail = not_found)
    return vehicle

@router.get("/", response_model=list[VehicleResponse])
def read_vehicles(skip: int = 0, limit : int = 100, db: Session = Depends(get_db)):
    return crud_vehicle.get_multi(db, skip=skip, limit=limit) 

@router.put("/{vehicle_id}", response_model = VehicleResponse)
def update_vehicle(vehicle_id: int, vehicle: VehicleUpdate, db: Session = Depends(get_db)):
    db_vehicle = crud_vehicle.get(db, vehicle_id)
    if not db_vehicle:
        raise HTTPException(status_code=404, detaisl = "Vehicle not found")
    return crud_vehicle.update(db, db_obj=db_vehicle, obj_in=vehicle)

@router.delete("/{vehicle_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vehicle(vehicle_id: int , db: Session = Depends(get_db)) :
    db_vehicle = crud_vehicle.get(db, vehicle_id)
    if not db_vehicle:
        raise HTTPException(status_code = 404, detail = "Vehicle not found")
    crud_vehicle.remove(db, id=vehicle_id) 
    return None
   