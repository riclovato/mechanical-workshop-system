from sqlalchemy.orm import Session
from app.models.mechanic import Mechanic
from app.crud.crud_base import CRUDBase
from typing import List

class CRUDMechanic(CRUDBase[Mechanic]):

    def get_available(self, db: Session) -> List[Mechanic]:
        return db.query(Mechanic).filter(Mechanic.available == True).all()