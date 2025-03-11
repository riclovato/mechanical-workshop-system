from typing import Generic, TypeVar, Optional, List, Type, Any
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.base import Base  # Importe sua Base SQLAlchemy

# Tipos genéricos
ModelType = TypeVar("ModelType", bound="Base")  # Modelo SQLAlchemy
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)  # Schema de criação Pydantic
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)  # Schema de atualização Pydantic

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        """Cria um novo registro no banco de dados"""
        db_obj = self.model(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        """Busca um registro por ID"""
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self, 
        db: Session, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[ModelType]:
        """Lista registros com paginação"""
        return db.query(self.model).offset(skip).limit(limit).all()

    def update(
        self, 
        db: Session, 
        db_obj: ModelType, 
        obj_in: UpdateSchemaType | dict[str, Any]
    ) -> ModelType:
        """Atualiza um registro existente"""
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        
        for field in update_data:
            setattr(db_obj, field, update_data[field])
        
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: int) -> Optional[ModelType]:
        """Remove um registro por ID"""
        db_obj = self.get(db, id)
        if db_obj:
            db.delete(db_obj)
            db.commit()
        return db_obj