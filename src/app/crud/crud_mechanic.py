from sqlalchemy.orm import Session
from app.models.mechanic import Mechanic
from app.crud.crud_base import CRUDBase
from app.schemas.mechanic import MechanicCreate, MechanicUpdate 
from typing import List

class CRUDMechanic(CRUDBase[Mechanic, MechanicCreate, MechanicUpdate]):

    def __init__(self):  
        super().__init__(model=Mechanic) 


    def get_available(self, db: Session) -> List[Mechanic]:
        return db.query(Mechanic).filter(Mechanic.available == True).all()