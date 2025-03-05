from sqlalchemy.orm import Session
from typing import Type, TypeVar, List
from pydantic import BaseModel

T = TypeVar("T", bound = BaseModel)

class CRUDBase:
    def __init__(self, model: Type[T]):
        self.model = model 
    
    def create(self, db: Session, obj_in : T) -> T:
        db_obj = self.model(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, id: int) -> T:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[T]:
        return db.query(self.model).offset(skip).limit(limit).all()

    
    def update(self, db: Session, db_obj: T, obj_in: T) -> T:
        for key, value in obj_in.model_dump(exclude_unset=True).items():
            setattr(db_obj, key, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: int) -> T:
        db_obj = self.get(db, id)
        db.delete(db_obj)
        db.commit()
        return db_obj